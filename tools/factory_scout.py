"""D-118 infrastructure scout — the free-first inventory the router and the owner both read.

    registry/infra.json   machine-readable: every known £0 resource (LLM API, compute, hosting, storage), how it is
                          obtained (keyless / human signup / card verification), what we hold (key configured and
                          VALID, keyless reachable, in use, missing), last check, evidence.
    docs/INFRA.md         the same as a table + ONE consolidated owner action list.

Rules (contract): legitimate only — one polite GET per keyless endpoint, `GET /models` with our own key for keyed
ones; never sign up, never rotate identities, never probe around a 429. A resource that needs a human (signup,
card verification, CAPTCHA) is reported, not attempted. Catalogue rows are RESEARCH (dated) until a live check
turns them VERIFIED; checks only ever touch resources we already hold or that are public by design.
"""
from __future__ import annotations
import datetime, json, os, pathlib, sys, time, urllib.error, urllib.request

ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
INFRA = ROOT / "registry" / "infra.json"
DOC = ROOT / "docs" / "INFRA.md"
RESEARCHED = "2026-09-24"

# kind: llm | compute | hosting | storage.  obtain: keyless | signup | signup+card.  key: env var we look for.
CATALOG: list[dict] = [
    # ---- LLM APIs (router lanes) ----
    {"id": "groq", "kind": "llm", "obtain": "signup", "key": "GROQ_API_KEY", "check": "https://api.groq.com/openai/v1/models",
     "signup": "https://console.groq.com", "free": "~30 RPM / 14.4k RPD, no card; llama/qwen/gpt-oss, tool calling"},
    {"id": "gemini", "kind": "llm", "obtain": "signup", "key": "GEMINI_API_KEY", "check": "https://generativelanguage.googleapis.com/v1beta/openai/models",
     "signup": "https://aistudio.google.com/apikey", "free": "Gemini Flash class free, low RPD on newest, no card"},
    {"id": "openrouter", "kind": "llm", "obtain": "signup", "key": "OPENROUTER_API_KEY", "check": "https://openrouter.ai/api/v1/models",
     "signup": "https://openrouter.ai/keys", "free": ":free models 50 req/day (1000/day after a one-off $10 top-up)"},
    {"id": "cerebras", "kind": "llm", "obtain": "signup", "key": "CEREBRAS_API_KEY", "check": "https://api.cerebras.ai/v1/models",
     "signup": "https://cloud.cerebras.ai", "free": "~1M tok/day free tier; very fast llama/qwen/gpt-oss"},
    {"id": "nvidia", "kind": "llm", "obtain": "signup", "key": "NVIDIA_API_KEY", "check": "https://integrate.api.nvidia.com/v1/models",
     "signup": "https://build.nvidia.com", "free": "~40 RPM free on build.nvidia.com; nemotron/minimax tool-capable"},
    {"id": "mistral", "kind": "llm", "obtain": "signup", "key": "MISTRAL_API_KEY", "check": "https://api.mistral.ai/v1/models",
     "signup": "https://console.mistral.ai", "free": "'Experiment' free tier (rate-limited), tool calling"},
    {"id": "cloudflare-workers-ai", "kind": "llm", "obtain": "signup", "key": "CLOUDFLARE_API_TOKEN", "check": None,
     "signup": "https://dash.cloudflare.com", "free": "10k neurons/day; llama/qwen/gemma; needs account id + token"},
    {"id": "zai", "kind": "llm", "obtain": "signup", "key": "ZAI_API_KEY", "check": None,
     "signup": "https://z.ai", "free": "GLM Flash ~1000 req/day free"},
    {"id": "hf-router", "kind": "llm", "obtain": "signup", "key": "HF_TOKEN", "check": "https://router.huggingface.co/v1/models",
     "signup": "https://huggingface.co/settings/tokens", "free": "small monthly inference credit; many OSS models"},
    {"id": "ollama-cloud", "kind": "llm", "obtain": "signup", "key": "OLLAMA_API_KEY", "check": None,
     "signup": "https://ollama.com", "free": "free tier of hosted large models via the local ollama CLI"},
    {"id": "ovh-anon", "kind": "llm", "obtain": "keyless", "key": None, "check": "https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/models",
     "signup": None, "free": "anonymous, tight per-IP/min quota — emergency fallback only (D-010)"},
    {"id": "pollinations", "kind": "llm", "obtain": "keyless", "key": None, "check": "https://text.pollinations.ai/models",
     "signup": None, "free": "keyless, best-effort availability"},
    {"id": "ollama-local", "kind": "llm", "obtain": "keyless", "key": None, "check": "http://127.0.0.1:11434/api/tags",
     "signup": None, "free": "local models on the laptop (qwen2.5:3b, qwen3:4b) — always available, weak on tools"},
    # ---- compute / hosting / storage ----
    {"id": "github", "kind": "storage", "obtain": "signup", "key": None, "check": "https://api.github.com/repos/contactgleamsphere-afk/grok-system",
     "signup": "https://github.com", "free": "repo = durable state + audit; Actions 2000 min/month private (unused so far)"},
    {"id": "github-actions", "kind": "compute", "obtain": "signup", "key": None, "check": None,
     "signup": "https://github.com/features/actions", "free": "scheduled/CI runners on the same account; candidate for off-laptop unit tests"},
    {"id": "cloudflare-workers", "kind": "hosting", "obtain": "signup", "key": "CLOUDFLARE_API_TOKEN", "check": None,
     "signup": "https://dash.cloudflare.com", "free": "100k req/day Workers + Pages; already the tunnel provider (quick tunnel, keyless)"},
    {"id": "cloudflare-quick-tunnel", "kind": "hosting", "obtain": "keyless", "key": None, "check": "tunnel",
     "signup": None, "free": "trycloudflare quick tunnel — how SSH reaches the laptop (no account)"},
    {"id": "hf-spaces", "kind": "hosting", "obtain": "signup", "key": "HF_TOKEN", "check": None,
     "signup": "https://huggingface.co/spaces", "free": "free CPU Spaces (2 vCPU/16 GB, sleeps when idle)"},
    {"id": "oracle-always-free", "kind": "compute", "obtain": "signup+card", "key": None, "check": None,
     "signup": "https://www.oracle.com/cloud/free/", "free": "Always Free ARM 4 OCPU/24 GB VM — best £0 24/7 host; card verification is a human step"},
    {"id": "google-cloud-run", "kind": "hosting", "obtain": "signup+card", "key": None, "check": None,
     "signup": "https://cloud.google.com/run", "free": "2M req/month free tier; card verification required"},
    {"id": "koyeb", "kind": "hosting", "obtain": "signup", "key": None, "check": None,
     "signup": "https://www.koyeb.com", "free": "one free nano web service"},
    {"id": "render", "kind": "hosting", "obtain": "signup", "key": None, "check": None,
     "signup": "https://render.com", "free": "free web service (spins down after idle)"},
    {"id": "cloudflare-r2", "kind": "storage", "obtain": "signup", "key": "CLOUDFLARE_API_TOKEN", "check": None,
     "signup": "https://dash.cloudflare.com", "free": "10 GB object storage, no egress fees"},
]


def _get(url: str, key: str | None = None, timeout: int = 15) -> tuple[int, str]:
    hdr = {"User-Agent": "aifactory-scout/1.0", **({"Authorization": f"Bearer {key}"} if key else {})}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=hdr), timeout=timeout) as r:
            return r.status, r.read(400).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read(200).decode("utf-8", "replace")
    except Exception as e:
        return -1, repr(e)[:120]


def _load() -> dict:
    return json.loads(INFRA.read_text(encoding="utf-8")) if INFRA.exists() else {"resources": {}}


def check(entry: dict, env: dict, getter=_get, tunnel_url: str | None = None) -> dict:
    """One resource → status. Statuses: configured (key valid) | invalid_key | keyless_ok | keyless_down | in_use |
    missing (owner signup) | unknown (nothing checkable, catalogue only)."""
    keyvar, url = entry.get("key"), entry.get("check")
    out = {"checked": datetime.datetime.now().isoformat(timespec="seconds"), "evidence": ""}
    if url == "tunnel":
        code, body = getter(tunnel_url) if tunnel_url else (-1, "no tunnel url")
        out.update(status="in_use" if code in (200, 404, 401) else "keyless_down", evidence=f"{code}")
        return out
    if keyvar:
        if not env.get(keyvar):
            out.update(status="missing", evidence=f"{keyvar} not set"); return out
        if not url:
            out.update(status="configured", evidence=f"{keyvar} set (no /models endpoint to validate)"); return out
        code, body = getter(url, env[keyvar])
        out.update(status="configured" if code == 200 else ("invalid_key" if code in (401, 403) else "configured"),
                   evidence=f"GET /models -> {code}")
        return out
    if url:
        code, body = getter(url)
        ok = code == 200
        out.update(status=("in_use" if entry["kind"] != "llm" else "keyless_ok") if ok else ("keyless_down" if entry["obtain"] == "keyless" else "unknown"),
                   evidence=f"GET -> {code}")
        return out
    out.update(status="unknown" if entry["obtain"] != "signup+card" else "missing", evidence="catalogue only (RESEARCH)")
    return out


def run(env: dict | None = None, getter=_get, tunnel_url: str | None = None, write: bool = True) -> dict:
    env = dict(os.environ) if env is None else env
    if tunnel_url is None:
        tf = ROOT / "run" / "tunnel.txt"
        tunnel_url = tf.read_text(encoding="utf-8").splitlines()[0].strip() if tf.exists() else None
    reg = _load(); res = reg.setdefault("resources", {})
    for e in CATALOG:
        r = check(e, env, getter, tunnel_url)
        prev = res.get(e["id"], {})
        res[e["id"]] = {**e, **r, "researched": RESEARCHED, "first_seen": prev.get("first_seen", r["checked"]),
                        "verified": "VERIFIED" if r["status"] in ("configured", "keyless_ok", "in_use", "invalid_key", "keyless_down") else "RESEARCH"}
    reg["updated"] = datetime.datetime.now().isoformat(timespec="seconds")
    owner = [(k, v) for k, v in res.items() if v["status"] in ("missing", "invalid_key")]
    summary = {"configured": sorted(k for k, v in res.items() if v["status"] == "configured"),
               "invalid_key": sorted(k for k, v in res.items() if v["status"] == "invalid_key"),
               "keyless_ok": sorted(k for k, v in res.items() if v["status"] == "keyless_ok"),
               "in_use": sorted(k for k, v in res.items() if v["status"] == "in_use"),
               "down": sorted(k for k, v in res.items() if v["status"] == "keyless_down"),
               "owner_signup": sorted(k for k, v in res.items() if v["status"] == "missing"),
               "unknown": sorted(k for k, v in res.items() if v["status"] == "unknown")}
    if write:
        INFRA.parent.mkdir(parents=True, exist_ok=True)
        INFRA.write_text(json.dumps(reg, indent=1), encoding="utf-8")
        DOC.write_text(render(reg, summary), encoding="utf-8")
    return {"summary": summary, "owner": [(k, v["signup"], v["key"]) for k, v in owner], "resources": len(res)}


def render(reg: dict, summary: dict) -> str:
    res = reg["resources"]
    lines = [f"# Free infrastructure inventory (D-118) — updated {reg.get('updated')}", "",
             "Legitimate only: keyless endpoints get one polite GET; keyed ones are validated with the key we already hold; "
             "anything needing a human (signup / card / CAPTCHA) is listed for the owner and never attempted by the factory.", "",
             "| id | kind | how obtained | status | evidence | free tier | checked |", "|---|---|---|---|---|---|---|"]
    for k, v in sorted(res.items(), key=lambda kv: (kv[1]["kind"], kv[0])):
        lines.append(f"| {k} | {v['kind']} | {v['obtain']} | **{v['status']}** ({v['verified']}) | {v['evidence']} | {v['free']} | {v['checked'][:16]} |")
    lines += ["", "## ACTION REQUIRED (owner) — free resources the factory cannot obtain itself", ""]
    todo = [(k, v) for k, v in res.items() if v["status"] in ("missing", "invalid_key")]
    if not todo: lines.append("- none")
    for k, v in sorted(todo, key=lambda kv: ({"llm": 0, "compute": 1, "hosting": 2, "storage": 3}[kv[1]["kind"]], kv[0])):
        what = "key is INVALID — regenerate" if v["status"] == "invalid_key" else ("sign up (card verification needed)" if v["obtain"] == "signup+card" else "sign up (no card)")
        setk = f", then set User env `{v['key']}` on the laptop" if v.get("key") else ""
        lines.append(f"- **{k}** ({v['kind']}): {what} at {v['signup']}{setk} — {v['free']}")
    lines += ["", f"Summary: configured {summary['configured']}; keyless ok {summary['keyless_ok']}; in use {summary['in_use']}; "
                  f"down {summary['down']}; awaiting owner {summary['owner_signup']}; invalid keys {summary['invalid_key']}."]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    r = run(write="--dry" not in sys.argv)
    print(json.dumps(r["summary"], indent=1)); print("owner:", r["owner"])
