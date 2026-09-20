"""AI Factory end-to-end pipeline (Phase 4).

    objective -> spec (LLM via the routing chain) -> validate -> build -> tests -> record -> BOT_REGISTRY

Usage (laptop or repo):
  python tools/factory_pipeline.py create "<plain-English objective>" [--id 004] [--dry-run] [--no-tests]
  python tools/factory_pipeline.py test <bot_id>              # run acceptance tests + record only
  python tools/factory_pipeline.py spec "<objective>"         # print the generated spec, build nothing

Design rules (see DECISIONS D-021..D-025):
  * The LLM only proposes a spec. Everything that matters (permissions, tool allow-list, chain, escape test)
    is enforced by BotFactory + validate_spec, not by the model.
  * New bot IDs are allocated from the registry (never overwrite an existing id from this entry point).
  * Tests run through the same runner as human-triggered runs (scripts/windows/run-bot-tests.ps1)
    so evidence is identical in shape.
"""
from __future__ import annotations
import json, os, re, subprocess, sys, pathlib, time, urllib.request

ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core"))
from factory.registry import Registry                      # noqa: E402
from factory.botspec import validate_spec                  # noqa: E402
from factory.factory import BotFactory, FactoryError       # noqa: E402

WIN = os.name == "nt"
LAPTOP_BOTS = pathlib.Path(r"C:\AI\Factory\bots")
RUNNER = pathlib.Path(r"C:\AI\Factory\tools\run-bot-tests.ps1")

# ---------------------------------------------------------------- LLM lane (OpenAI-compatible, chain order)
LANES = [  # (name, base, env key, model) — mirrors registry order: Groq -> Gemini -> OpenRouter -> local
    ("groq", "https://api.groq.com/openai/v1", "GROQ_API_KEY", "openai/gpt-oss-120b"),
    ("gemini", "https://generativelanguage.googleapis.com/v1beta/openai", "GEMINI_API_KEY", "gemini-3.7-flash"),
    ("gemini", "https://generativelanguage.googleapis.com/v1beta/openai", "GEMINI_API_KEY", "gemini-3.5-flash-lite"),
    ("openrouter", "https://openrouter.ai/api/v1", "OPENROUTER_API_KEY", "deepseek/deepseek-v4-flash-0731:free"),
    ("ollama", "http://127.0.0.1:11434/v1", None, "qwen3:4b"),
]


def chat(messages: list[dict], max_tokens: int = 1200) -> tuple[str, str]:
    """Try each lane in order; return (text, lane_label). Quota/auth/connection errors rotate (D-017)."""
    errors = []
    for name, base, keyvar, model in LANES:
        key = os.environ.get(keyvar) if keyvar else "ollama"
        if not key:
            errors.append(f"{name}:{model} no key"); continue
        body = {"model": model, "messages": messages, "temperature": 0.1, "max_tokens": max_tokens}
        req = urllib.request.Request(f"{base}/chat/completions", data=json.dumps(body).encode(),
                                     headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json",
                                              "User-Agent": "aifactory-pipeline/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=180 if name == "ollama" else 90) as r:
                d = json.load(r)
            return d["choices"][0]["message"]["content"] or "", f"{name}:{model}"
        except urllib.error.HTTPError as e:
            errors.append(f"{name}:{model} HTTP {e.code} {e.read()[:120].decode(errors='replace')}")
        except Exception as e:  # connection / timeout
            errors.append(f"{name}:{model} {type(e).__name__}")
    raise RuntimeError("all lanes failed: " + " | ".join(errors))


# ---------------------------------------------------------------- objective -> spec
def _catalog(reg: Registry) -> str:
    tools = reg.all("tools")
    models = [m for m in reg.all("models") if m.verified != "BLOCKED"]
    t = "\n".join(f"- {x.id}: provides {x.provides}, risk {x.risk}, scope {x.scope}" for x in tools)
    m = ", ".join(sorted(x.id for x in models))
    return f"TOOLS (only these ids may be used):\n{t}\n\nMODEL PRESETS (only these ids): {m}"


SPEC_PROMPT = """You are the Bot Architect of an AI Factory. Turn the OBJECTIVE into ONE bot specification as strict JSON.

Rules:
- Least privilege: request only the tools the objective needs. Tool -> permission mapping:
  read_file -> fs:read ; write_file -> fs:write ; exec -> shell:workspace ; web_search -> net:search ; web_fetch -> net:fetch
- model_policy.primary and fallbacks must be preset ids from the catalog. Use primary "{primary}" and
  fallbacks ["gemini-flash","gemini-flash38","groq-gptoss20b","or-deepseek","gemini-lite","local4b"] unless the objective needs something else.
- tests: 2 to 3 acceptance tests, each a string "prompt -> expected". The expected value must be a short exact
  token the bot can reliably output (a number, a word, OK-style marker). The first test must be a trivial liveness
  check like "Reply with exactly: X_OK -> X_OK". Tests must be checkable offline unless the bot has net tools.
- instructions: 40-120 words, concrete, telling the bot how to work and what to never do.
- name: lowercase slug. id: "{bot_id}".

{catalog}

Return ONLY the JSON object with keys: id, name, purpose, instructions, model_policy, tools, permissions, tests, notes.
OBJECTIVE: {objective}"""


def next_id(reg: Registry) -> str:
    ids = [int(b.id) for b in reg.all("bots") if b.id.isdigit()]
    return f"{(max(ids) + 1) if ids else 1:03d}"


def objective_to_spec(objective: str, reg: Registry, bot_id: str, attempts: int = 3) -> tuple[dict, str]:
    msgs = [{"role": "user", "content": SPEC_PROMPT.format(primary="groq-gptoss120b", bot_id=bot_id,
                                                           catalog=_catalog(reg), objective=objective)}]
    last_err = ""
    for i in range(attempts):
        text, lane = chat(msgs)
        m = re.search(r"\{.*\}", text, re.S)
        try:
            spec = json.loads(m.group(0) if m else text)
        except Exception as e:
            last_err = f"not JSON: {e}"; msgs.append({"role": "assistant", "content": text})
            msgs.append({"role": "user", "content": "That was not valid JSON. Return ONLY the JSON object."}); continue
        spec["id"] = bot_id  # never trust the model with identity
        problems = validate_spec(spec, reg)
        if not problems:
            spec["notes"] = (spec.get("notes") or "") + f" | spec generated by {lane} from objective: {objective[:120]}"
            return spec, lane
        last_err = "; ".join(problems)
        msgs.append({"role": "assistant", "content": json.dumps(spec)})
        msgs.append({"role": "user", "content": f"validate_spec rejected it: {last_err}. Fix and return ONLY the JSON."})
    raise FactoryError(f"could not produce a valid spec after {attempts} attempts: {last_err}")


# ---------------------------------------------------------------- tests on the laptop
def run_tests(bot_dir: pathlib.Path, cap: int = 300) -> dict:
    if not WIN or not RUNNER.exists():
        raise RuntimeError("acceptance tests run on the laptop only (run-bot-tests.ps1 missing)")
    cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(RUNNER),
           "-BotDir", str(bot_dir), "-Cap", str(cap)]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=cap * 6 + 120).stdout
    m = re.search(r"RESULTJSON (\{.*\})", out)
    if not m:
        raise RuntimeError("runner produced no RESULTJSON:\n" + out[-1500:])
    res = json.loads(m.group(1)); res["raw"] = out
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
def cmd_create(objective: str, bot_id: str | None, dry_run: bool, no_tests: bool) -> dict:
    reg = Registry(ROOT / "registry"); bots_root = LAPTOP_BOTS if WIN else ROOT / "bots"
    f = BotFactory(reg, bots_root)
    bot_id = bot_id or next_id(reg)
    if reg.get("bots", bot_id):
        raise FactoryError(f"bot {bot_id} exists; pipeline never overwrites (use factory_cli build --overwrite)")
    t0 = time.time()
    spec, lane = objective_to_spec(objective, reg, bot_id)
    report = {"bot_id": bot_id, "name": spec["name"], "spec_lane": lane, "spec": spec}
    if dry_run:
        return report
    (ROOT / "specs").mkdir(exist_ok=True)
    (ROOT / "specs" / f"{bot_id}-{spec['name']}.json").write_text(json.dumps(spec, indent=2), encoding="utf-8")
    r = f.build(spec)
    report.update({"bot_dir": str(r.bot_dir), "files": r.files, "chain": r.chain, "disabled_tools": len(r.disabled_tools)})
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


def cmd_test(bot_id: str) -> dict:
    reg = Registry(ROOT / "registry"); f = BotFactory(reg, LAPTOP_BOTS if WIN else ROOT / "bots")
    e = reg.get("bots", bot_id)
    if not e:
        raise FactoryError(f"unknown bot {bot_id}")
    bot_dir = (LAPTOP_BOTS if WIN else ROOT / "bots") / f"{e.id}-{e.name}"
    res = run_tests(bot_dir)
    e = f.record_test_result(bot_id, int(res["pass"]), int(res["total"]), res["evidence"])
    write_bot_registry_md(reg, ROOT / "BOT_REGISTRY.md")
    return {"bot_id": bot_id, "tests": res["evidence"], "status": e.status, "verified": e.verified}


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__); return 2
    cmd, arg = argv[1], argv[2]
    opt = lambda k, d=None: argv[argv.index(k) + 1] if k in argv else d
    try:
        if cmd == "create":
            out = cmd_create(arg, opt("--id"), "--dry-run" in argv, "--no-tests" in argv)
        elif cmd == "spec":
            out = cmd_create(arg, opt("--id"), True, True)
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
