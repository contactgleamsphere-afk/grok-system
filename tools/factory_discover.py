"""Capability discovery for model lanes (D-047): DISCOVER -> EVALUATE -> SANDBOX -> APPROVE -> INTEGRATE.

  python tools/factory_discover.py [--provider openrouter] [--max 3] [--dry-run]

Trigger: the hourly probe BLOCKs a lane, or fewer than MIN_HEALTHY remote lanes are healthy. Steps:
  DISCOVER  - pull the provider's public model catalogue (OpenRouter /models; free tier = ':free' suffix).
  EVALUATE  - keep only: tool calling advertised, context >= 16k, not already in the registry, not in the rejected list
              (registry/discovery.json remembers every verdict so we never re-test the same failure), newest first.
  SANDBOX   - two real requests per candidate: (1) the standard tool-call probe, (2) a two-turn tool loop
              (call `add`, receive result, answer with the number). Both must pass; latency is recorded.
  APPROVE   - automatic ONLY for the lane class the factory already uses (same provider, same key, free tier, no new
              permissions). Anything else (new provider, needs sign-up) is written to discovery.json as
              `needs_owner` and surfaced in STATUS.md "needs attention". Popularity is not evidence: only our own
              sandbox result is.
  INTEGRATE - registry ModelEntry (verified=INFERRED, capabilities chat+tools, limits.health.probation=2) and a nanobot
              preset in config.json (D-048). A probation lane enters chains only after 2 consecutive hourly probe
              passes (factory_probe promotes INFERRED->VERIFIED); a BLOCKED probation lane is deleted, not kept.
Every verdict is returned for the worker's audit trail (event `lane.discovered` / `lane.rejected`).
"""
from __future__ import annotations
import json, os, sys, time, pathlib, urllib.request, urllib.error
ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core")); sys.path.insert(0, str(ROOT / "tools"))
from factory.registry import Registry, ModelEntry   # noqa: E402
import factory_probe as fpr                          # noqa: E402

MIN_HEALTHY = 5
MIN_CONTEXT = 16_000
CATALOG = {"openrouter": "https://openrouter.ai/api/v1/models", "cerebras": "https://api.cerebras.ai/v1/models",
           "nvidia": "https://integrate.api.nvidia.com/v1/models", "mistral": "https://api.mistral.ai/v1/models"}
UNKNOWN_CONTEXT = 32768   # generic /models gives no context_length; the sandbox loop + probation are the real evidence
LEDGER = ROOT / "registry" / "discovery.json"


def _ledger() -> dict:
    return json.loads(LEDGER.read_text(encoding="utf-8")) if LEDGER.exists() else {"verdicts": {}}


def _save_ledger(d: dict) -> None:
    LEDGER.write_text(json.dumps(d, indent=1), encoding="utf-8")


def discover(provider: str = "openrouter", fetch=None, key: str | None = None) -> list[dict]:
    hdr = {"User-Agent": "aifactory-discover/1.0", **({"Authorization": f"Bearer {key}"} if key else {})}
    fetch = fetch or (lambda url: json.load(urllib.request.urlopen(urllib.request.Request(url, headers=hdr), timeout=30)))
    data = fetch(CATALOG[provider])["data"]
    out = []
    for m in data:
        if provider == "openrouter" and not m["id"].endswith(":free"):
            continue
        if provider == "openrouter":
            out.append({"model": m["id"], "context": int(m.get("context_length") or 0),
                        "tools": "tools" in (m.get("supported_parameters") or []), "created": int(m.get("created") or 0)})
        else:  # generic OpenAI /models: no capability metadata -> assume, and let the sandbox loop decide
            out.append({"model": m["id"], "context": int(m.get("context_length") or m.get("max_context_length") or UNKNOWN_CONTEXT),
                        "tools": bool(m.get("capabilities", {}).get("function_calling", True)) if isinstance(m.get("capabilities"), dict) else True,
                        "created": int(m.get("created") or 0)})
    return out


def needs_owner(provider: str, ledger: dict, now: float) -> dict | None:
    """D-069: record (once per 7 days) that a free provider is unusable until the owner signs up and sets the key."""
    k = f"provider:{provider}"; v = ledger["verdicts"].get(k)
    if v and v.get("verdict") == "needs_owner" and now - v.get("ts", 0) < 7 * 86400:
        return None
    base, keyvar = fpr.BASES[provider]
    v = {"verdict": "needs_owner", "reason": f"set {keyvar} (User env) after signing up: {fpr.SIGNUP.get(provider, base)}",
         "ts": now, "date": time.strftime("%Y-%m-%d")}
    ledger["verdicts"][k] = v; _save_ledger(ledger)
    return v


def evaluate(cands: list[dict], reg: Registry, ledger: dict, provider: str) -> tuple[list[dict], list[tuple[dict, str]]]:
    known = {m.model for m in reg.all("models") if m.provider == provider}
    keep, rejected = [], []
    for c in sorted(cands, key=lambda x: -x["created"]):
        v = ledger["verdicts"].get(f"{provider}:{c['model']}")
        if c["model"] in known: continue
        if not c["tools"]: rejected.append((c, "no tool calling advertised")); continue
        if c["context"] < MIN_CONTEXT: rejected.append((c, f"context {c['context']} < {MIN_CONTEXT}")); continue
        if v and v.get("verdict") in ("rejected", "needs_owner") and time.time() - v.get("ts", 0) < 7 * 86400:
            rejected.append((c, f"ledger: {v['verdict']} on {v.get('date')} ({v.get('reason','')[:60]})")); continue
        keep.append(c)
    return keep, rejected


def sandbox_loop(base: str, key: str, model: str, timeout: int = 60) -> dict:
    """Two-turn tool loop: model must call add(a,b), then answer with the tool result."""
    tool = {"type": "function", "function": {"name": "add", "description": "Add two integers.",
                                             "parameters": {"type": "object", "properties": {"a": {"type": "integer"}, "b": {"type": "integer"}}, "required": ["a", "b"]}}}
    msgs = [{"role": "user", "content": "Use the add tool to compute 17 + 25, then reply with only the number."}]
    hdr = {"Authorization": f"Bearer {key}", "Content-Type": "application/json", "User-Agent": "aifactory-discover/1.0"}
    t0 = time.time()
    try:
        body = {"model": model, "messages": msgs, "tools": [tool], "max_tokens": 128, "temperature": 0}
        d = json.load(urllib.request.urlopen(urllib.request.Request(f"{base}/chat/completions", data=json.dumps(body).encode(), headers=hdr), timeout=timeout))
        msg = d["choices"][0]["message"]; tc = (msg.get("tool_calls") or [None])[0]
        if not tc or tc["function"]["name"] != "add": return {"ok": False, "reason": "did not call add"}
        args = json.loads(tc["function"]["arguments"] or "{}")
        if {int(args.get("a", 0)), int(args.get("b", 0))} != {17, 25}: return {"ok": False, "reason": f"bad args {args}"}
        msgs += [msg, {"role": "tool", "tool_call_id": tc["id"], "content": "42"}]
        body = {"model": model, "messages": msgs, "tools": [tool], "max_tokens": 32, "temperature": 0}
        d = json.load(urllib.request.urlopen(urllib.request.Request(f"{base}/chat/completions", data=json.dumps(body).encode(), headers=hdr), timeout=timeout))
        text = (d["choices"][0]["message"].get("content") or "").strip()
        return {"ok": "42" in text, "reason": "" if "42" in text else f"final answer {text[:40]!r}", "latency_s": round(time.time() - t0, 2)}
    except urllib.error.HTTPError as e:
        return {"ok": False, "reason": f"HTTP {e.code} {e.read()[:120].decode(errors='replace')}"}
    except Exception as e:
        return {"ok": False, "reason": type(e).__name__}


def preset_id(provider: str, model: str) -> str:
    slug = model.split("/")[-1].replace(":free", "").replace(".", "").replace("_", "-")
    return f"{ {'openrouter': 'or', 'cerebras': 'cb', 'nvidia': 'nv', 'mistral': 'mi'}.get(provider, provider) }-{slug}"[:40]


def integrate(reg: Registry, provider: str, c: dict, probe: dict, loop: dict) -> ModelEntry:
    e = ModelEntry(id=preset_id(provider, c["model"]), provider=provider, model=c["model"], capabilities=["chat", "tools"],
                   context_window=min(c["context"], 131072), location="remote", cost_per_1k=0.0,
                   tool_call_score=0.7, verified="INFERRED",
                   notes=f"DISCOVERED {time.strftime('%Y-%m-%d')} by factory_discover: probe {probe.get('latency_s')}s, loop {loop.get('latency_s')}s. Probation: 2 clean hourly probes -> VERIFIED.",
                   limits={"health": {"ok": True, "probation": 2, "latency_s": probe.get("latency_s"), "last_outcome": "ok",
                                      "last_probe": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())}, "rpd_scope": {"openrouter": "openrouter free tier shared 50/day"}.get(provider, f"{provider} free tier (see SIGNUP)")})
    reg.upsert("models", e)
    return e


def run(provider: str = "openrouter", max_new: int = 2, dry_run: bool = False, fetch=None, prober=None, looper=None) -> dict:
    reg = Registry(ROOT / "registry"); ledger = _ledger(); now = time.time()
    healthy = [m.id for m in reg.all("models") if m.location == "remote" and m.verified != "BLOCKED"
               and (m.limits or {}).get("health", {}).get("last_outcome") == "ok"
               and float((m.limits or {}).get("health", {}).get("quota_until", 0) or 0) <= now]
    base, keyvar = fpr.BASES[provider]; key = os.environ.get(keyvar)
    if not key:
        return {"skipped": f"{keyvar} not set", "healthy": healthy, "needs_owner": needs_owner(provider, ledger, now) or "already notified"}
    if ledger["verdicts"].pop(f"provider:{provider}", None):  # key present -> the owner acted; clear the notice
        _save_ledger(ledger)
    cands = discover(provider, fetch, key)
    keep, rejected = evaluate(cands, reg, ledger, provider)
    prober = prober or fpr.probe_remote; looper = looper or sandbox_loop
    added, verdicts = [], []
    for c in keep:
        if len(added) >= max_new: break
        p = prober(base, key, c["model"])
        if p["outcome"] != "ok":
            verdicts.append((c, "rejected", f"probe {p['outcome']}: {p.get('detail','')[:80]}")); continue
        l = looper(base, key, c["model"])
        if not l["ok"]:
            verdicts.append((c, "rejected", f"loop: {l['reason']}")); continue
        verdicts.append((c, "approved", f"probe {p.get('latency_s')}s loop {l.get('latency_s')}s"))
        if not dry_run:
            added.append(integrate(reg, provider, c, p, l).id)
        else:
            added.append(preset_id(provider, c["model"]))
    for c, r in rejected:
        if not r.startswith("ledger"): verdicts.append((c, "filtered", r))
    if not dry_run:
        day = time.strftime("%Y-%m-%d")
        for c, v, r in verdicts:
            if v in ("rejected", "approved"):
                ledger["verdicts"][f"{provider}:{c['model']}"] = {"verdict": v, "reason": r, "ts": now, "date": day}
        _save_ledger(ledger)
    return {"provider": provider, "healthy_before": healthy, "catalog": len(cands), "evaluated": len(keep),
            "added": added, "verdicts": [{"model": c["model"], "verdict": v, "reason": r} for c, v, r in verdicts]}


if __name__ == "__main__":
    a = sys.argv
    prov = a[a.index("--provider") + 1] if "--provider" in a else "openrouter"
    mx = int(a[a.index("--max") + 1]) if "--max" in a else 2
    print(json.dumps(run(prov, mx, "--dry-run" in a), indent=1))
