"""AI Factory end-to-end pipeline (Phase 4).

    objective -> spec (LLM via the routing chain) -> validate -> build -> tests -> record -> BOT_REGISTRY

Usage (laptop or repo):
  python tools/factory_pipeline.py create "<plain-English objective>" [--id 004] [--dry-run] [--no-tests]
  python tools/factory_pipeline.py create "<objective>" --allow fs:read,fs:write,shell:workspace   # D-054 owner grant beyond default allowance
  python tools/factory_pipeline.py test <bot_id>              # run acceptance tests + record only
  python tools/factory_pipeline.py seal-master [actor]        # D-083: seal master AGENTS.md / tools/factory.py / config tools.exec
  python tools/factory_pipeline.py rearchitect <bot_id>       # D-052: regenerate spec from the original objective
  python tools/factory_pipeline.py spec "<objective>"         # print the generated spec, build nothing

Design rules (see DECISIONS D-021..D-025):
  * The LLM only proposes a spec. Everything that matters (permissions, tool allow-list, chain, escape test)
    is enforced by BotFactory + validate_spec, not by the model.
  * New bot IDs are allocated from the registry (never overwrite an existing id from this entry point).
  * Tests run through the same runner as human-triggered runs (scripts/windows/run-bot-tests.ps1)
    so evidence is identical in shape.
"""
from __future__ import annotations
import json, os, re, subprocess, sys, pathlib, time, urllib.request, datetime

ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core"))
from factory.registry import Registry                      # noqa: E402
from factory.botspec import validate_spec                  # noqa: E402
from factory.factory import BotFactory, FactoryError
from factory.guard import SecurityViolation, bundle_drift, master_seal, master_drift       # noqa: E402

WIN = os.name == "nt"
LAPTOP_BOTS = pathlib.Path(r"C:\AI\Factory\bots")
MASTER_WS = pathlib.Path(os.environ.get("AIFACTORY_MASTER_WS", r"C:\AI\Factory\workspace"))        # D-083
MASTER_CFG = pathlib.Path(os.environ.get("AIFACTORY_MASTER_CFG", r"C:\AI\Factory\config.json"))
RUNNER = ROOT / "scripts" / "windows" / "run-bot-tests.ps1"   # D-050: the repo copy is the only copy (hand-synced duplicate in C:\AI\Factory\tools archived)

# ---------------------------------------------------------------- LLM lane (OpenAI-compatible, chain order)
LANES = [  # (name, base, env key, model) — mirrors registry order: Groq -> Gemini -> OpenRouter -> local
    ("groq", "https://api.groq.com/openai/v1", "GROQ_API_KEY", "openai/gpt-oss-120b"),
    ("gemini", "https://generativelanguage.googleapis.com/v1beta/openai", "GEMINI_API_KEY", "gemini-3.7-flash"),
    ("gemini", "https://generativelanguage.googleapis.com/v1beta/openai", "GEMINI_API_KEY", "gemini-3.5-flash-lite"),
    ("openrouter", "https://openrouter.ai/api/v1", "OPENROUTER_API_KEY", "deepseek/deepseek-v4-flash-0731:free"),
    ("ollama", "http://127.0.0.1:11434/v1", None, "qwen3:4b"),
]


_LANE_BASES = {"groq": ("https://api.groq.com/openai/v1", "GROQ_API_KEY"),
               "gemini": ("https://generativelanguage.googleapis.com/v1beta/openai", "GEMINI_API_KEY"),
               "openrouter": ("https://openrouter.ai/api/v1", "OPENROUTER_API_KEY"),
               "ollama": ("http://127.0.0.1:11434/v1", None)}


def live_lanes() -> list[tuple[str, str, str | None, str]]:
    """D-042: builder lanes come from the registry + probe health (BLOCKED dropped, quota-cooled skipped), ranked
    groq -> gemini -> openrouter -> local by measured latency. Falls back to the static LANES if the registry is unreadable."""
    try:
        reg = Registry(ROOT / "registry"); now = time.time(); order = {"groq": 0, "gemini": 1, "openrouter": 2, "ollama": 3}
        cands = []
        for m in reg.all("models"):
            if m.provider not in _LANE_BASES or m.verified == "BLOCKED" or "tools" not in (m.capabilities or []): continue
            h = (m.limits or {}).get("health", {})
            if float(h.get("quota_until", 0) or 0) > now: continue
            if h.get("last_outcome") in ("no_tool_call",): continue
            b = (m.limits or {}).get("bench") or {}
            rate = (b["pass"] / b["total"]) if b.get("total") else None
            # D-095: builder work (architect/planner/repair/insight) goes to the best MEASURED lane first, not the first
            # provider alphabetically. Tiers: 0 = bench >= 0.75, 1 = un-benchmarked (provider order), 2 = weak (< 0.5 on
            # >= 4 tests) — still usable as a last resort, never first. Local lanes always last.
            tier = 3 if m.provider == "ollama" else (2 if is_weak(m) else (1 if rate is None else 0))
            cands.append(((tier, -(rate or 0), order[m.provider], float(h.get("latency_s") or 5.0)), m))
        cands.sort(key=lambda x: x[0])
        if any(c[0][0] < 2 for c in cands):                          # D-096: weak lanes only when nothing better is live
            cands = [c for c in cands if c[0][0] != 2]
        lanes = [(m.provider, _LANE_BASES[m.provider][0], _LANE_BASES[m.provider][1], m.model) for _, m in cands]
        return lanes or LANES
    except Exception:
        return LANES


def chat(messages: list[dict], max_tokens: int = 1200, skip: set[str] | None = None) -> tuple[str, str]:
    """Try each live lane in order; return (text, lane_label). Quota/auth/connection errors rotate (D-017/D-042).
    `skip` (D-056) = lane labels ("provider:model") that already failed to solve THIS task — a different model gets
    the next attempt instead of the same one repeating itself."""
    errors = []
    for name, base, keyvar, model in live_lanes():
        if skip and f"{name}:{model}" in skip:
            errors.append(f"{name}:{model} skipped (already tried)"); continue
        key = os.environ.get(keyvar) if keyvar else "ollama"
        if not key:
            errors.append(f"{name}:{model} no key"); continue
        body = {"model": model, "messages": messages, "temperature": 0.1, "max_tokens": max_tokens}
        if name == "groq" and "gpt-oss" in model: body["reasoning_effort"] = "low"
        req = urllib.request.Request(f"{base}/chat/completions", data=json.dumps(body).encode(),
                                     headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json",
                                              "User-Agent": "aifactory-pipeline/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=180 if name == "ollama" else 90) as r:
                d = json.load(r)
            text = d["choices"][0]["message"].get("content") or ""
            if not text.strip():   # reasoning models can burn the whole budget and return empty content -> rotate lane
                errors.append(f"{name}:{model} empty content (finish={d['choices'][0].get('finish_reason')})"); continue
            return text, f"{name}:{model}"
        except urllib.error.HTTPError as e:
            txt = e.read()[:400].decode(errors="replace")
            errors.append(f"{name}:{model} HTTP {e.code} {txt[:120]}")
            if e.code in (429, 413) or "rate_limit" in txt or "RESOURCE_EXHAUSTED" in txt:
                _cool_from_error(name, model, txt)                    # D-092: builder-side 429s cool the lane too
        except Exception as e:  # connection / timeout
            errors.append(f"{name}:{model} {type(e).__name__}")
    raise RuntimeError("all lanes failed: " + " | ".join(errors))


def _cool_from_error(provider: str, model: str, txt: str) -> None:
    """D-092: the same rule as the test runner's QUOTAHIT (D-080/D-088) for the architect/planner/repair calls made by
    the builder itself: parse retry-after + daily-vs-minute kind and cool the exact lane now. Never raises."""
    try:
        import factory_probe as fpr
        m = re.search(r"try\s+again in (?:(\d+)h)?(?:(\d+)m)?(?:([\d.]+)s)?", txt)
        secs = int((int(m.group(1) or 0) * 3600 + int(m.group(2) or 0) * 60 + float(m.group(3) or 0)) + 30) if m and m.group(0).strip() != "try again in" else 0
        if not secs:
            m2 = re.search(r"retryDelay['\":\s]+(\d+)s", txt); secs = int(m2.group(1)) + 30 if m2 else 900
        low = txt.lower()
        kind = "tpd" if ("(tpd)" in low or "per day" in low or "per-day" in low or "perday" in low or "daily" in low) else ("rpd" if "(rpd)" in low else "tpm")
        fpr.mark_quota([{"model": model, "secs": secs, "kind": kind, "provider": provider}])
    except Exception:
        pass


# ---------------------------------------------------------------- objective -> spec
def _catalog(reg: Registry) -> str:
    tools = reg.all("tools")
    models = [m for m in reg.all("models") if m.verified != "BLOCKED"]
    tools = [x for x in tools if not (x.kind == "mcp" and "PROBATION" in (x.scope or ""))]   # D-110: probation servers are not offered
    t = "\n".join(f"- {x.id}: provides {x.provides}, risk {x.risk}, scope {x.scope}" + (f" (MCP server: requires permission {x.id}; its tools appear to the bot as mcp_{x.id.split(':', 1)[-1].replace('-', '_')}_*)" if x.kind == "mcp" else "") for x in tools)
    m = ", ".join(sorted(x.id for x in models))
    return f"TOOLS (only these ids may be used):\n{t}\n\nMODEL PRESETS (only these ids): {m}"


SPEC_PROMPT = """You are the Bot Architect of an AI Factory. Turn the OBJECTIVE into ONE bot specification as strict JSON.

Rules:
- Least privilege: request only the tools the objective needs. Tool -> permission mapping:
  read_file -> fs:read ; write_file -> fs:write ; exec -> shell:workspace ; web_search -> net:search ; web_fetch -> net:fetch
- model_policy.primary and fallbacks must be preset ids from the catalog. Use primary "{primary}" and
  fallbacks {fallbacks} unless the objective needs something else.
- tests: 2 to 3 acceptance tests, each a string "prompt -> expected". The prompt itself must NOT contain the
  characters "->" and must be self-contained: the workspace is EMPTY at test time, so if the bot needs an input file
  the prompt must first tell it to create that file with write_file (e.g. "First write commits.txt containing ...
  then ..."). The expected token must be exactly the bot's final line. The expected value must be a short exact
  token the bot can reliably output (a number, a word, OK-style marker). The first test must be a trivial liveness
  check like "Reply with exactly: X_OK -> X_OK". Tests must be checkable offline unless the bot has net tools.
  After the liveness check, expected values must be COMPUTED by the bot from the task (a count, a sum, a filename it
  derived), never a fixed phrase that the instructions themselves would have to dictate (e.g. "Status: PASS"),
  because the repair guard rejects any instruction text that quotes a test's expected value.
- instructions: 40-120 words, concrete, telling the bot how to work and what to never do.
- name: lowercase slug. id: "{bot_id}".

{catalog}

Return ONLY the JSON object with keys: id, name, purpose, instructions, model_policy, tools, permissions, tests, notes.
OBJECTIVE: {objective}"""


LEGACY_PRIMARY = "groq-gptoss120b"


def ranked_remote(reg: Registry) -> list:
    """Healthy, tool-capable remote lanes, benchmark-ranked (D-050): benchmarked lanes by pass-rate then speed,
    then un-benchmarked lanes in provider order."""
    order = {"groq": 0, "gemini": 1, "openrouter": 2}
    rem = [m for m in reg.all("models") if m.verified != "BLOCKED" and m.location == "remote" and m.provider in order
           and "tools" in (m.capabilities or [])]      # quota-cooled lanes stay valid POLICY members; the live chain skips them
    def _key(m):
        b = (m.limits or {}).get("bench") or {}
        if b.get("total"):
            return (0, -(b["pass"] / b["total"]), b.get("secs", 9e9))
        return (1, order[m.provider], -(m.tool_call_score or 0))
    rem.sort(key=_key)
    return rem


PRIMARY_MIN_RPD = 200      # a primary serves every bot's every test; tiny daily budgets (OpenRouter free 50/day shared,
                           # Gemini free 20/day/model) are fallback material, not primary material


def default_primary(reg: Registry) -> str:
    """D-058: primary = best benchmarked lane (>=0.9 over its window) that is not quota-cooled AND has a daily budget
    big enough to be everyone's first call (rpd unknown or >= PRIMARY_MIN_RPD, and not a shared tiny pool);
    otherwise the legacy primary. Measured quality decides who goes first — within budget reality."""
    now = time.time()
    for m in ranked_remote(reg):
        lim = m.limits or {}; b = lim.get("bench") or {}
        if float((lim.get("health") or {}).get("quota_until", 0) or 0) > now: continue
        rpd = lim.get("rpd"); scope = str(lim.get("rpd_scope") or "")
        if (rpd is not None and rpd < PRIMARY_MIN_RPD) or "50/day" in scope or "account-wide" in scope: continue
        if b.get("total") and b["pass"] / b["total"] >= 0.9:
            return m.id
    return LEGACY_PRIMARY


WEAK_RATE, WEAK_MIN_TESTS = 0.5, 8      # D-096: < 50% over at least two full reference runs (4 tests each)


def is_weak(m) -> bool:
    """D-096: a lane whose measured quality is < WEAK_RATE over >= WEAK_MIN_TESTS scored tests. Weak lanes are not
    retired — they keep being probed and benchmarked and re-enter chains as soon as their window recovers — but new
    bots' fallback chains and the primary choice exclude them. Existing bots keep their chains (history preserved)."""
    b = (m.limits or {}).get("bench") or {}
    return bool(b.get("total")) and b["total"] >= WEAK_MIN_TESTS and (b["pass"] / b["total"]) < WEAK_RATE


def default_fallbacks(reg: Registry, primary: str | None = None) -> list[str]:
    """Ranked remote lanes minus the primary, then the best local model."""
    primary = primary or default_primary(reg)
    order = {"groq": 0, "gemini": 1, "openrouter": 2}
    rem = [m for m in ranked_remote(reg) if m.id != primary and not is_weak(m)]   # D-096
    loc = [m for m in reg.all("models") if m.location == "local" and m.verified != "BLOCKED"]
    loc.sort(key=lambda m: -(m.tool_call_score or 0))
    return [m.id for m in rem][:5] + ([loc[0].id] if loc else [])


def next_id(reg: Registry) -> str:
    """Highest id seen anywhere (registry, specs/, bots roots) + 1 — ids are never reused even if a registry
    entry is lost (D-033)."""
    ids = [int(b.id) for b in reg.all("bots") if b.id.isdigit()]
    for root in (ROOT / "specs", ROOT / "bots", LAPTOP_BOTS if WIN else None):
        if root and root.exists():
            for p in root.iterdir():
                m = re.match(r"(\d{3})-", p.name)
                if m: ids.append(int(m.group(1)))
    return f"{(max(ids) + 1) if ids else 1:03d}"


_WRITE_HINT = re.compile(r"\b(first\s+)?(write|create|save|make)\s+(a\s+|the\s+)?(file\s+)?[\w.-]+\.(txt|csv|json|md|log|tsv|yaml|yml|xml|html)\b", re.I)


_SHELL_HINT = re.compile(r"\b(run|execute|invoke|call)\s+(the\s+)?(pytest|python\s+-m|python3?\s+\S+\.py|pip|npm|npx|node|git|docker|make|bash|sh|powershell|curl|wget)\b|\b(pytest|npm test|git (status|log|diff|commit))\b", re.I)


def spec_consistency(spec: dict) -> list[str]:
    """D-052: a spec whose tests need a capability the tool list does not grant can never pass and repair cannot
    fix it (tools are frozen). Catch it at architect time so the architect, not the repairer, corrects it.
    Bot 012: tests said 'First write data.csv ...' with tools=[read_file] -> CAPABILITY_MISSING: write_file."""
    problems = []
    tools = set(spec.get("tools") or []); perms = set(spec.get("permissions") or [])
    for t in spec.get("tests", []):
        if not isinstance(t, str): continue
        if t.count("->") != 1:
            problems.append(f"test must contain exactly one '->': {t[:60]!r}"); continue
        prompt = t.rsplit("->", 1)[0]; exp = t.rsplit("->", 1)[1].strip()
        # D-073: an expected value that is a multi-word phrase (not a number / single token / CONFINED-ESCAPED / echoed in
        # the prompt) can only be produced if the instructions quote it — which the reward-hacking guard forbids.
        if exp and not exp.isdigit() and " " in exp and exp.lower() not in prompt.lower() and exp.upper() not in ("CONFINED", "ESCAPED"):
            problems.append(f"expected value {exp[:30]!r} is a phrase the instructions would have to dictate; expect a computed number/token instead")
        if _WRITE_HINT.search(prompt) and "write_file" not in tools:
            problems.append(f"test asks the bot to write a file but tools lack write_file: {prompt[:60]!r} (add write_file + fs:write, or make the test not need a fixture)")
        if re.search(r"\bread\b.*\.(txt|csv|json|md|log)\b", prompt, re.I) and "read_file" not in tools:
            problems.append(f"test asks the bot to read a file but tools lack read_file: {prompt[:60]!r}")
        if re.search(r"\b(search the web|look up online|fetch (the )?url|https?://)", prompt, re.I) and not (tools & {"web_search", "web_fetch"}):
            problems.append(f"test needs the web but tools lack web_search/web_fetch: {prompt[:60]!r}")
        # D-093 (bot 019 class): shell verbs / binaries need exec + shell:workspace; bare 'run pytest/npm/git ...' can never
        # be satisfied by a read/write-only bot and the runtime has no pytest/node/git on PATH for bots anyway.
        if _SHELL_HINT.search(prompt) and "exec" not in tools:
            problems.append(f"test needs a shell command but tools lack exec: {prompt[:60]!r} (needs exec + shell:workspace, or restate the test as a file computation)")
    try:                                                            # D-099 at architect time: instructions vs declared tools
        import factory_repair as _fr
        esc = _fr.instruction_boundary_violations(spec.get("instructions") or "", list(tools))
        if esc: problems.append(f"instructions exceed the declared tools/boundary: {esc} — either grant the tool or rewrite the instructions")
    except ImportError:
        pass
    if "write_file" in tools and "fs:write" not in perms: problems.append("write_file requires permission fs:write")
    if "exec" in tools and "shell:workspace" not in perms: problems.append("exec requires permission shell:workspace")
    if "read_file" in tools and "fs:read" not in perms: problems.append("read_file requires permission fs:read")
    return problems


UNKNOWN_TOOLS: list[str] = []      # D-109: tools the architect wanted that the registry lacks (per process)


def objective_to_spec(objective: str, reg: Registry, bot_id: str, attempts: int = 3, feedback: str = "",
                      allowed_permissions: list[str] | None = None) -> tuple[dict, str]:
    allowed = DEFAULT_ALLOWANCE if allowed_permissions is None else allowed_permissions
    primary = default_primary(reg)
    prompt = SPEC_PROMPT.format(primary=primary, bot_id=bot_id, fallbacks=json.dumps(default_fallbacks(reg, primary)),
                                catalog=_catalog(reg), objective=objective)
    prompt += (f"\n\nPERMISSION ALLOWANCE for this job: {json.dumps(allowed)}. You may not request any other permission "
               "(so no exec/shell unless shell:workspace is listed). If the objective genuinely cannot be met inside the "
               "allowance, return {\"blocked\": \"<one sentence: which permission is needed and why>\"} instead of a spec.")
    if feedback:
        prompt += f"\n\nA PREVIOUS SPEC FOR THIS OBJECTIVE WAS REJECTED. Fix this: {feedback[:600]}"
    msgs = [{"role": "user", "content": prompt}]
    last_err = ""
    for i in range(attempts):
        text, lane = chat(msgs)
        m = re.search(r"\{.*\}", text, re.S)
        try:
            spec = json.loads(m.group(0) if m else text)
        except Exception as e:
            last_err = f"not JSON: {e}"; msgs.append({"role": "assistant", "content": text})
            msgs.append({"role": "user", "content": "That was not valid JSON. Return ONLY the JSON object."}); continue
        if isinstance(spec, dict) and spec.get("blocked") and len(spec) <= 2:
            raise SecurityViolation(f"architect: objective needs permissions outside the allowance {allowed}: {str(spec['blocked'])[:200]}")
        spec["id"] = bot_id  # never trust the model with identity
        problems = validate_spec(spec, reg) + spec_consistency(spec)
        for pr in problems:                                   # D-109: a capability gap is a discovery trigger, not just a rejection
            mm = re.match(r"tool '([^']+)' not in tool registry", pr)
            if mm and mm.group(1) not in UNKNOWN_TOOLS: UNKNOWN_TOOLS.append(mm.group(1))
        extra = sorted(set(spec.get("permissions") or []) - set(allowed))
        if extra: problems.append(f"permissions {extra} are outside the job allowance {allowed}; redesign without them or return blocked")
        if not problems:
            spec["notes"] = (spec.get("notes") or "") + f" | spec generated by {lane} from objective: {objective[:120]}"
            return spec, lane
        last_err = "; ".join(problems)
        msgs.append({"role": "assistant", "content": json.dumps(spec)})
        msgs.append({"role": "user", "content": f"validate_spec rejected it: {last_err}. Fix and return ONLY the JSON."})
    if "outside the job allowance" in last_err:     # D-054: persistent over-reach is a security pause, not a retryable logic error
        raise SecurityViolation(f"architect kept requesting permissions outside the allowance {allowed} for: {objective[:120]!r} — {last_err[:200]}")
    raise FactoryError(f"could not produce a valid spec after {attempts} attempts: {last_err}")


# ---------------------------------------------------------------- tests on the laptop
def run_master_tests(cap: int = 240) -> dict:
    """D-046: master 001 has no bundle; its acceptance suite is scripts/windows/run-master-tests.ps1."""
    ps = ROOT / "scripts" / "windows" / "run-master-tests.ps1"
    r = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(ps), "-Cap", str(cap)],
                       capture_output=True, text=True, timeout=cap * 5 + 120)
    raw = r.stdout + r.stderr
    m = re.search(r"pass/total: (\d+)/(\d+)", raw)
    ev = raw.strip().splitlines()[-1] if raw.strip() else "no output"
    # D-102: master timeouts are availability (cold laptop, lane back-off), not master quality — same rule as bot tests (D-075)
    timeouts = len(re.findall(r"T\d+ FAIL \d+s \[TIMEOUT\]", ev))
    return {"pass": int(m.group(1)) if m else 0, "total": int(m.group(2)) if m else 5, "evidence": ev[:900], "raw": raw, "timeouts": timeouts, "quota": 0}


def run_tests(bot_dir: pathlib.Path, cap: int = 300, lane: str | None = None) -> dict:
    if bot_dir.name.startswith("001-"):
        return run_master_tests()
    if not WIN or not RUNNER.exists():
        raise RuntimeError("acceptance tests run on the laptop only (run-bot-tests.ps1 missing)")
    cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(RUNNER),
           "-BotDir", str(bot_dir), "-Cap", str(cap)] + (["-Lane", lane] if lane else [])
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=cap * 6 + 120).stdout
    m = re.search(r"RESULTJSON (\{.*\})", out)
    if not m:
        raise RuntimeError("runner produced no RESULTJSON:\n" + out[-1500:])
    res = json.loads(m.group(1)); res["raw"] = out
    hits = [json.loads(x) for x in re.findall(r"^QUOTAHIT (\{.*\})\s*$", out, re.M)]
    if hits:                                             # D-080: cool the exact lanes that 429'd during this run
        from factory_probe import mark_quota
        try: res["cooled"] = mark_quota(hits)
        except Exception as e: res["cooled_error"] = repr(e)
    return res


def write_bot_registry_md(reg: Registry, path: pathlib.Path) -> None:
    rows = ["# BOT_REGISTRY", "", "| id | name | status | verified | chain | tools | last test |",
            "|---|---|---|---|---|---|---|"]
    for v in reg.all("bots"):
        chain = [v.model_policy["primary"], *v.model_policy.get("fallbacks", [])]
        rows.append(f"| {v.id} | {v.name} | {v.status} | {v.verified} | {' > '.join(chain)} | "
                    f"{', '.join(v.tools)} | {(v.notes or '')[:80]} |")
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- commands
DEFAULT_ALLOWANCE = ["fs:read", "fs:write", "net:search", "net:fetch"]   # never shell:* without an explicit owner grant


def enforce_allowance(spec: dict, allowed_permissions: list[str] | None, context: str) -> None:
    """D-054: the permission gate runs BEFORE anything is written or built. Bot 015 showed the old post-hoc check in
    the worker let a shell bot get built, tested and activated first, then paused the job — too late."""
    allowed = set(DEFAULT_ALLOWANCE if allowed_permissions is None else allowed_permissions)
    extra = sorted(set(spec.get("permissions") or []) - allowed)
    if extra:
        raise SecurityViolation(f"{context}: spec requests permissions beyond the job allowance {sorted(allowed)}: {extra}")


def cmd_create(objective: str, bot_id: str | None, dry_run: bool, no_tests: bool, allowed_permissions: list[str] | None = None, on_built=None) -> dict:
    reg = Registry(ROOT / "registry"); bots_root = LAPTOP_BOTS if WIN else ROOT / "bots"
    f = BotFactory(reg, bots_root)
    bot_id = bot_id or next_id(reg)
    if reg.get("bots", bot_id):
        raise FactoryError(f"bot {bot_id} exists; pipeline never overwrites (use factory_cli build --overwrite)")
    t0 = time.time()
    spec, lane = objective_to_spec(objective, reg, bot_id, allowed_permissions=allowed_permissions)
    spec["objective"] = objective          # D-052: kept verbatim so a re-architect can start from the owner's words
    enforce_allowance(spec, allowed_permissions, f"create {bot_id}")     # D-054: gate before any write/build/test
    report = {"bot_id": bot_id, "name": spec["name"], "spec_lane": lane, "spec": spec}
    if dry_run:
        return report
    (ROOT / "specs").mkdir(exist_ok=True)
    (ROOT / "specs" / f"{bot_id}-{spec['name']}.json").write_text(json.dumps(spec, indent=2), encoding="utf-8")
    r = f.build(spec)
    report.update({"bot_dir": str(r.bot_dir), "files": r.files, "chain": r.chain, "disabled_tools": len(r.disabled_tools)})
    if on_built: on_built(report)          # D-065: caller records identity before the (long) test phase
    if no_tests or not WIN:
        report["status"] = reg.get("bots", bot_id).status
        return report
    res = run_tests(r.bot_dir)
    e = f.record_test_result(bot_id, int(res["pass"]), int(res["total"]), res["evidence"])
    (r.bot_dir / "TEST_RESULTS.md").write_text(res["raw"], encoding="utf-8")
    write_bot_registry_md(reg, ROOT / "BOT_REGISTRY.md")
    report.update({"tests": res["evidence"], "pass": res["pass"], "total": res["total"],
                   "status": e.status, "verified": e.verified, "elapsed_s": int(time.time() - t0)})
    return report


def cmd_rearchitect(bot_id: str, feedback: str = "", allowed_permissions: list[str] | None = None) -> dict:
    """D-052: regenerate the spec of a `testing` bot from its ORIGINAL objective (never from the broken spec),
    rebuild in place, re-test. Used when repair cannot help because tools/tests are inconsistent. Boundaries:
    permissions may change only within the job's allowance (checked by the worker) and are audited as a diff;
    the previous spec is archived in specs/history. Bot id/name are kept."""
    reg = Registry(ROOT / "registry"); bots_root = LAPTOP_BOTS if WIN else ROOT / "bots"
    f = BotFactory(reg, bots_root); e = reg.get("bots", bot_id)
    if e is None: raise FactoryError(f"unknown bot {bot_id}")
    if e.status == "active": return {"ok": False, "bot_id": bot_id, "error": "rearchitect only runs on non-active bots"}
    sp = ROOT / "specs" / f"{e.id}-{e.name}.json"
    old = json.loads(sp.read_text(encoding="utf-8")) if sp.exists() else {}
    objective = old.get("objective") or (old.get("notes") or "").split("from objective:")[-1].strip() or e.purpose
    fb = feedback or "; ".join(spec_consistency(old)) or e.notes
    spec, lane = objective_to_spec(objective, reg, bot_id, feedback=fb, allowed_permissions=allowed_permissions)
    spec["id"], spec["name"], spec["objective"] = bot_id, e.name, objective        # identity is never the model's
    spec["notes"] = (spec.get("notes") or "") + f" | re-architected {datetime.date.today()} by {lane}: {fb[:100]}"
    enforce_allowance(spec, allowed_permissions, f"rearchitect {bot_id}")
    hist = ROOT / "specs" / "history"; hist.mkdir(exist_ok=True)
    if old: (hist / f"{e.id}-{e.name}-{datetime.datetime.now():%Y%m%d-%H%M%S}-prearch.json").write_text(json.dumps(old, indent=2), encoding="utf-8")
    sp.write_text(json.dumps(spec, indent=2), encoding="utf-8")
    r = f.build(spec, overwrite=True)
    report = {"ok": True, "bot_id": bot_id, "name": e.name, "spec_lane": lane, "chain": r.chain, "spec": spec,
              "boundary_diff": {"tools": {"before": old.get("tools"), "after": spec["tools"]},
                                "permissions": {"before": old.get("permissions"), "after": spec["permissions"]}}}
    if not WIN: report["status"] = reg.get("bots", bot_id).status; return report
    res = run_tests(r.bot_dir)
    e2 = f.record_test_result(bot_id, int(res["pass"]), int(res["total"]), res["evidence"])
    (r.bot_dir / "TEST_RESULTS.md").write_text(res["raw"], encoding="utf-8")
    write_bot_registry_md(reg, ROOT / "BOT_REGISTRY.md")
    report.update({"tests": res["evidence"], "pass": res["pass"], "total": res["total"], "status": e2.status, "verified": e2.verified})
    return report


def cmd_seal_master(actor: str = "builder") -> dict:
    """D-083: record the master's security surface (called by wire-master-factory.ps1 after it writes those files)."""
    reg = Registry(ROOT / "registry"); e = reg.get("bots", "001")
    if e is None: raise FactoryError("no master entry 001")
    before = dict(e.seal or {}); e.seal = master_seal(MASTER_WS, MASTER_CFG); reg.upsert("bots", e)
    return {"bot_id": "001", "seal": e.seal, "changed": [k for k in e.seal if before.get(k) != e.seal[k]], "actor": actor}


def cmd_test(bot_id: str) -> dict:
    if bot_id == "001":
        reg = Registry(ROOT / "registry"); f = BotFactory(reg, LAPTOP_BOTS if WIN else ROOT / "bots")
        drift = master_drift(MASTER_WS, MASTER_CFG, getattr(reg.get("bots", "001"), "seal", None))   # D-083
        if drift and drift != ["<unsealed>"]:
            raise FactoryError(f"master integrity: {drift} changed outside the factory; re-run wire-master-factory.ps1 to reseal")
        res = run_master_tests()
        p_, t_, q_ = int(res["pass"]), int(res["total"]), int(res.get("timeouts", 0))
        if p_ < t_ and q_ and p_ + q_ >= t_:                       # D-102: every miss was a timeout -> inconclusive, status untouched
            e = reg.get("bots", "001")
            return {"bot_id": "001", "tests": res["evidence"], "pass": p_, "total": t_, "status": e.status, "verified": e.verified,
                    "inconclusive": True, "timeouts": q_}
        e = f.record_test_result("001", p_, t_, res["evidence"])
        write_bot_registry_md(reg, ROOT / "BOT_REGISTRY.md")
        return {"bot_id": "001", "tests": res["evidence"], "pass": res["pass"], "total": res["total"], "status": e.status, "verified": e.verified}
    reg = Registry(ROOT / "registry"); f = BotFactory(reg, LAPTOP_BOTS if WIN else ROOT / "bots")
    e = reg.get("bots", bot_id)
    if not e:
        raise FactoryError(f"unknown bot {bot_id}")
    bot_dir = (LAPTOP_BOTS if WIN else ROOT / "bots") / f"{e.id}-{e.name}"
    drift = bundle_drift(bot_dir, getattr(e, "seal", None))        # D-068: a tampered bundle cannot earn "active"
    if drift and drift != ["<unsealed>"]:
        raise FactoryError(f"bundle integrity: {drift} changed outside the factory; rebuild/repair to reseal")
    res = run_tests(bot_dir)
    p, t, q = int(res["pass"]), int(res["total"]), int(res.get("quota", 0) or 0) + int(res.get("timeouts", 0) or 0)
    if p < t and q and p + q >= t:      # D-051/D-075: every failure was a 429 or a wall-clock timeout -> inconclusive, status untouched
        return {"bot_id": bot_id, "tests": res["evidence"], "status": e.status, "verified": e.verified, "inconclusive": True, "quota": q}
    e = f.record_test_result(bot_id, p, t, res["evidence"])
    write_bot_registry_md(reg, ROOT / "BOT_REGISTRY.md")
    return {"bot_id": bot_id, "tests": res["evidence"], "status": e.status, "verified": e.verified}


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__); return 2
    cmd, arg = argv[1], argv[2]
    opt = lambda k, d=None: argv[argv.index(k) + 1] if k in argv else d
    try:
        if cmd == "create":
            allow = opt("--allow"); allow = allow.split(",") if allow else None      # owner-granted allowance, e.g. --allow fs:read,fs:write,shell:workspace
            out = cmd_create(arg, opt("--id"), "--dry-run" in argv, "--no-tests" in argv, allow)
        elif cmd == "rearchitect":
            out = cmd_rearchitect(arg, opt("--feedback", ""))
        elif cmd == "spec":
            out = cmd_create(arg, opt("--id"), True, True)
        elif cmd == "seal-master":
            out = cmd_seal_master(arg)
        elif cmd == "test":
            out = cmd_test(arg)
        else:
            print(__doc__); return 2
    except (FactoryError, RuntimeError) as e:
        print(json.dumps({"ok": False, "error": str(e)})); return 1
    out["ok"] = True
    print(json.dumps(out, indent=1, default=str)); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
