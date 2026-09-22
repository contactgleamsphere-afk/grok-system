"""Lane health probe (D-037): a real, minimal tool-call request against every keyed remote model in the registry.

  python tools/factory_probe.py [--only gemini-flash,or-deepseek] [--dry-run]

For each model: send one chat request that MUST produce a tool call (function `ping`). Outcome classes:
  ok           -> verified stays/returns to VERIFIED, health.ok=True, latency recorded
  quota (429)  -> health.quota_until = now + 15 min (chains skip it until then; not BLOCKED, quota is temporary)
  gone (404 / "no longer available" / "decommissioned") -> verified=BLOCKED  (the chain drops it)
  auth (401/403 non-quota) -> BLOCKED + note "key/auth"  (owner action; audited)
  error (5xx / timeout)    -> health.failures += 1; BLOCKED after 3 consecutive failures
  no_tool_call             -> tool_call_score decays; BLOCKED if < 0.3
A model that was BLOCKED by the probe and passes again is restored to VERIFIED automatically (self-healing lanes).
Local (ollama) models are pinged via /api/tags only. Results are returned as a dict for the worker's audit trail.
"""
from __future__ import annotations
import json, os, sys, time, pathlib, urllib.request, urllib.error
ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core"))
from factory.registry import Registry  # noqa: E402

BASES = {
    "groq": ("https://api.groq.com/openai/v1", "GROQ_API_KEY"),
    "gemini": ("https://generativelanguage.googleapis.com/v1beta/openai", "GEMINI_API_KEY"),
    "openrouter": ("https://openrouter.ai/api/v1", "OPENROUTER_API_KEY"),
    # D-069: 2026 free tiers that need a human signup (no card). The factory never self-applies; a missing key
    # becomes a needs_owner notice in STATUS.md with the signup URL.
    "cerebras": ("https://api.cerebras.ai/v1", "CEREBRAS_API_KEY"),
    "nvidia": ("https://integrate.api.nvidia.com/v1", "NVIDIA_API_KEY"),
    "mistral": ("https://api.mistral.ai/v1", "MISTRAL_API_KEY"),
}
SIGNUP = {  # RESEARCH 2026-09: free tier, no card, OpenAI-compatible, tool calling
    "cerebras": "https://cloud.cerebras.ai (free tier ~1M tokens/day)",
    "nvidia": "https://build.nvidia.com (free ~40 rpm, tool-capable models)",
    "mistral": "https://console.mistral.ai (Experiment free tier)",
}
QUOTA_COOLDOWN_S = 900
GONE_MARKERS = ("no longer available", "decommissioned", "not found", "does not exist", "has been retired")
TOOL = {"type": "function", "function": {"name": "ping", "description": "Reply to a liveness check.",
                                         "parameters": {"type": "object", "properties": {"ok": {"type": "boolean"}}, "required": ["ok"]}}}


def probe_remote(base: str, key: str, model: str, timeout: int = 45) -> dict:
    body = {"model": model, "messages": [{"role": "user", "content": "Call the ping tool with ok=true. Do not answer in text."}],
            "tools": [TOOL], "tool_choice": "auto", "max_tokens": 64, "temperature": 0}
    if "gpt-oss" in model: body["reasoning_effort"] = "low"
    req = urllib.request.Request(f"{base}/chat/completions", data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json", "User-Agent": "aifactory-probe/1.0"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = json.load(r)
        msg = d["choices"][0]["message"]
        called = bool(msg.get("tool_calls")) and msg["tool_calls"][0]["function"]["name"] == "ping"
        return {"outcome": "ok" if called else "no_tool_call", "latency_s": round(time.time() - t0, 2)}
    except urllib.error.HTTPError as e:
        txt = e.read()[:300].decode(errors="replace").lower()
        if e.code == 429 or "quota" in txt or "rate limit" in txt:
            return {"outcome": "quota", "http": e.code, "detail": txt[:160]}
        if e.code == 404 or any(m in txt for m in GONE_MARKERS):
            return {"outcome": "gone", "http": e.code, "detail": txt[:160]}
        if e.code in (401, 403):
            return {"outcome": "auth", "http": e.code, "detail": txt[:160]}
        return {"outcome": "error", "http": e.code, "detail": txt[:160]}
    except Exception as e:
        return {"outcome": "error", "detail": type(e).__name__}


def probe_local(model: str, timeout: int = 5) -> dict:
    try:
        with urllib.request.urlopen("http://127.0.0.1:11434/api/tags", timeout=timeout) as r:
            names = [m["name"] for m in json.load(r).get("models", [])]
        return {"outcome": "ok" if model in names else "gone", "detail": "ollama up" if model in names else f"{model} not pulled"}
    except Exception as e:
        return {"outcome": "error", "detail": f"ollama down: {type(e).__name__}"}


def apply(entry, res: dict, now: float) -> tuple[str, str]:
    """Mutate the registry entry from a probe result. Returns (before_verified, after_verified)."""
    before = entry.verified
    h = dict(entry.limits.get("health", {}))
    h["last_probe"] = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(now)); h["last_outcome"] = res["outcome"]
    o = res["outcome"]
    if o == "ok":
        h["failures"] = 0; h["ok"] = True; h.pop("quota_until", None); h["latency_s"] = res.get("latency_s")
        if before == "BLOCKED" and h.get("blocked_by") == "probe":
            entry.verified = "VERIFIED"; h.pop("blocked_by", None)   # self-heal
        if before == "INFERRED" and "probation" in h:                # D-047 probation: N clean probes -> VERIFIED
            h["probation"] = int(h["probation"]) - 1
            if h["probation"] <= 0: entry.verified = "VERIFIED"; h.pop("probation", None)
        entry.tool_call_score = min(1.0, (entry.tool_call_score or 0.5) * 0.8 + 0.2)
    elif o == "quota":
        h["ok"] = False; h["quota_until"] = now + QUOTA_COOLDOWN_S
    elif o in ("gone", "auth"):
        h["ok"] = False; h["blocked_by"] = "probe"; h["reason"] = f"{o}: {res.get('detail', '')}"[:200]
        entry.verified = "BLOCKED"
    if entry.verified == "INFERRED" and "probation" in h and o in ("gone", "auth", "error", "no_tool_call"):
        # D-047: a probation lane gets no second chances — one failure and it is BLOCKED (and pruned by presets sync)
        h["ok"] = False; h["blocked_by"] = "probe"; h["reason"] = f"failed probation: {o}"; entry.verified = "BLOCKED"
    elif o == "error":
        h["failures"] = int(h.get("failures", 0)) + 1; h["ok"] = False
        if h["failures"] >= 3:
            h["blocked_by"] = "probe"; h["reason"] = f"3 consecutive errors: {res.get('detail', '')}"[:200]; entry.verified = "BLOCKED"
    elif o == "no_tool_call":
        entry.tool_call_score = round((entry.tool_call_score or 1.0) * 0.6, 2); h["ok"] = False
        if entry.tool_call_score < 0.3:
            h["blocked_by"] = "probe"; h["reason"] = "tool_call_score decayed below 0.3"; entry.verified = "BLOCKED"
    entry.limits = {**entry.limits, "health": h}
    return before, entry.verified


def run(only: set[str] | None = None, dry_run: bool = False, prober_remote=probe_remote, prober_local=probe_local) -> dict:
    reg = Registry(ROOT / "registry"); now = time.time(); rows = []
    for e in reg.all("models"):
        if only and e.id not in only: continue
        if e.provider in BASES:
            base, keyvar = BASES[e.provider]; key = os.environ.get(keyvar)
            if not key:
                rows.append({"id": e.id, "outcome": "skipped", "detail": f"{keyvar} not set"}); continue
            res = prober_remote(base, key, e.model)
        elif e.provider == "ollama":
            res = prober_local(e.model)
        else:
            rows.append({"id": e.id, "outcome": "skipped", "detail": f"provider {e.provider} has no prober"}); continue
        before, after = apply(e, res, now)
        if not dry_run: reg.upsert("models", e)
        rows.append({"id": e.id, "model": e.model, **res, "before": before, "after": after})
    changed = [r for r in rows if r.get("before") != r.get("after")]
    retired = [] if dry_run else retire_gone(reg, now)
    return {"probed": len(rows), "rows": rows, "changed": changed, "retired": retired,
            "healthy": [r["id"] for r in rows if r.get("outcome") == "ok"]}


RETIRE_AFTER_S = 3 * 86400


def retire_gone(reg: Registry, now: float) -> list[dict]:
    """D-069: a remote lane BLOCKED as 'gone' (404/decommissioned) that has stayed gone for 3 days is retired: removed
    from the registry (bots' chains already skip BLOCKED lanes) and recorded in the discovery ledger so it is never
    re-added under the same slug. Quota/auth/error blocks are NOT retired (they self-heal)."""
    out = []
    for e in reg.all("models"):
        h = (e.limits or {}).get("health", {})
        if e.verified != "BLOCKED" or e.location != "remote" or not str(h.get("reason", "")).startswith("gone"):
            continue
        try: since = time.mktime(time.strptime(h.get("first_gone") or h.get("last_probe"), "%Y-%m-%dT%H:%M:%S")) - time.timezone
        except Exception: continue
        if "first_gone" not in h:                       # start the clock on first sight
            e.limits = {**e.limits, "health": {**h, "first_gone": h.get("last_probe")}}; reg.upsert("models", e); continue
        if now - since >= RETIRE_AFTER_S:
            led = ROOT / "registry" / "discovery.json"
            try: ledger = json.loads(led.read_text(encoding="utf-8"))
            except Exception: ledger = {"verdicts": {}}
            ledger.setdefault("verdicts", {})[f"{e.provider}:{e.model}"] = {"verdict": "rejected", "reason": f"retired after 3 days gone: {h.get('reason','')[:80]}",
                                                                          "ts": now, "date": time.strftime("%Y-%m-%d")}
            led.write_text(json.dumps(ledger, indent=1), encoding="utf-8")
            reg.remove("models", e.id); out.append({"id": e.id, "model": e.model, "reason": h.get("reason", "")[:80]})
    return out


def main(argv: list[str]) -> int:
    only = None
    if "--only" in argv: only = set(argv[argv.index("--only") + 1].split(","))
    out = run(only, "--dry-run" in argv)
    for r in out["rows"]:
        print(f"{r['id']:<16} {r.get('outcome'):<12} {r.get('before','-'):<10}->{r.get('after','-'):<10} {r.get('latency_s', r.get('detail',''))}")
    print(json.dumps({"probed": out["probed"], "healthy": out["healthy"], "changed": [(c["id"], c["after"]) for c in out["changed"]]}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
