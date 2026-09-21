"""Self-improvement v0: failure -> demote -> regenerate instructions -> sandbox test -> restore active only on pass.

  python tools/factory_repair.py <bot_id> [--max-rounds 2]

Contract (D-029):
  * Precondition: bot status is `testing` (the monitor demoted it). Never touches an `active` bot.
  * The LLM (via the routing chain) may change ONLY `instructions`. id, name, tools, permissions, model_policy,
    tests are frozen: a permission/tool diff after repair is a hard failure.
  * Candidate is built into a SANDBOX bundle (bots/<id>-<name>-repair) and tested there; production bundle is
    untouched until the candidate passes every test.
  * On pass: spec + bundle replaced, status -> active (via record_test_result), previous instructions kept in
    specs/history/. On fail after max rounds: bot stays `testing`, evidence recorded, exit 1.
"""
from __future__ import annotations
import json, os, re, shutil, sys, pathlib, datetime
ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core")); sys.path.insert(0, str(ROOT / "tools"))
from factory.registry import Registry                        # noqa: E402
from factory.botspec import validate_spec                    # noqa: E402
from factory.factory import BotFactory, FactoryError         # noqa: E402
import factory_pipeline as fp                                # noqa: E402

FROZEN = ("id", "name", "tools", "permissions", "model_policy", "tests")

REPAIR_PROMPT = """You maintain bots for an AI Factory. A bot FAILED its acceptance tests. Rewrite ONLY its `instructions`
so it passes, keeping the same purpose. You may not add tools, permissions or tests.

BOT PURPOSE: {purpose}
TOOLS AVAILABLE (fixed): {tools}
CURRENT INSTRUCTIONS:
{instructions}

ACCEPTANCE TESTS (prompt -> expected final line):
{tests}

TEST RESULT (failed): {evidence}
{last_lines}

Write new instructions (40-150 words, concrete, tell the bot exactly how to compute each expected value and to end
its reply with only the expected token). Return ONLY JSON: {{"instructions": "..."}}"""


def _spec_path(reg: Registry, e) -> pathlib.Path:
    return ROOT / "specs" / f"{e.id}-{e.name}.json"


def _tail(raw: str, n: int = 12) -> str:
    lines = [l for l in raw.splitlines() if l.strip() and not l.startswith("20")][-n:]
    return "LAST OUTPUT LINES:\n" + "\n".join(l[:160] for l in lines)


def regenerate_instructions(spec: dict, evidence: str, raw: str = "") -> tuple[str, str]:
    msg = REPAIR_PROMPT.format(purpose=spec["purpose"], tools=", ".join(spec["tools"]),
                               instructions=spec["instructions"], tests="\n".join(spec["tests"]),
                               evidence=evidence[:600], last_lines=_tail(raw))
    for _ in range(3):
        text, lane = fp.chat([{"role": "user", "content": msg}], max_tokens=700)
        m = re.search(r"\{.*\}", text, re.S)
        try:
            new = json.loads(m.group(0) if m else text)["instructions"].strip()
        except Exception:
            continue
        if 30 <= len(new.split()) <= 220 and new != spec["instructions"]:
            return new, lane
    raise FactoryError("repair: chain did not return usable instructions")


def permissions_unchanged(before: dict, after: dict) -> list[str]:
    return [k for k in FROZEN if json.dumps(before.get(k), sort_keys=True) != json.dumps(after.get(k), sort_keys=True)]


def repair(bot_id: str, max_rounds: int = 2, runner=None, chat=None) -> dict:
    reg = Registry(ROOT / "registry"); bots_root = fp.LAPTOP_BOTS if fp.WIN else ROOT / "bots"
    f = BotFactory(reg, bots_root); runner = runner or fp.run_tests
    if chat: fp.chat = chat
    e = reg.get("bots", bot_id)
    if e is None: raise FactoryError(f"unknown bot {bot_id}")
    if e.status != "testing":
        return {"ok": False, "bot_id": bot_id, "error": f"repair only runs on demoted bots (status={e.status})"}
    sp = _spec_path(reg, e); spec = json.loads(sp.read_text(encoding="utf-8"))
    before = {k: spec.get(k) for k in FROZEN}
    evidence = e.notes; raw = ""
    log = {"bot_id": bot_id, "name": e.name, "rounds": [], "permissions_before": before["permissions"]}
    sandbox_root = bots_root; sandbox_name = f"{e.id}-{e.name}-repair"
    for rnd in range(1, max_rounds + 1):
        new_instr, lane = regenerate_instructions(spec, evidence, raw)
        cand = {**spec, "instructions": new_instr, "name": f"{e.name}-repair"}
        changed = permissions_unchanged(before, {**cand, "name": e.name})
        problems = validate_spec(cand, reg)
        if changed or problems:
            log["rounds"].append({"round": rnd, "lane": lane,
                                  "rejected": f"frozen fields changed: {changed}" if changed else problems})
            spec = json.loads(sp.read_text(encoding="utf-8"))   # discard any mutation, reload pristine spec
            continue
        # sandbox: separate registry copy so production entry is never touched by the candidate build
        sb_reg_dir = ROOT / "run" / "repair-registry"; shutil.rmtree(sb_reg_dir, ignore_errors=True)
        shutil.copytree(ROOT / "registry", sb_reg_dir)
        sb = BotFactory(Registry(sb_reg_dir), sandbox_root)
        shutil.rmtree(sandbox_root / sandbox_name, ignore_errors=True)
        r = sb.build(cand, overwrite=True)
        res = runner(r.bot_dir); p, t = int(res["pass"]), int(res["total"]); raw = res.get("raw", "")
        log["rounds"].append({"round": rnd, "lane": lane, "sandbox": f"{p}/{t}", "evidence": res["evidence"][:400],
                              "instructions": new_instr})
        evidence = res["evidence"]
        if p == t and t > 0:
            # promote: archive old instructions, write spec, rebuild production bundle, record pass -> active
            hist = ROOT / "specs" / "history"; hist.mkdir(exist_ok=True)
            (hist / f"{e.id}-{e.name}-{datetime.datetime.now():%Y%m%d-%H%M%S}.json").write_text(
                json.dumps(spec, indent=2), encoding="utf-8")
            spec["instructions"] = new_instr
            spec["notes"] = (spec.get("notes") or "") + f" | repaired {datetime.date.today()} by {lane} (round {rnd})"
            sp.write_text(json.dumps(spec, indent=2), encoding="utf-8")
            f.build(spec, overwrite=True)                       # production bundle from the accepted spec
            after_entry = f.record_test_result(bot_id, p, t, f"repair round {rnd} via {lane}: {res['evidence']}")
            after = json.loads(sp.read_text(encoding="utf-8"))
            log.update({"ok": True, "status": after_entry.status, "verified": after_entry.verified,
                        "permissions_after": after["permissions"], "frozen_diff": permissions_unchanged(before, after)})
            shutil.rmtree(sandbox_root / sandbox_name, ignore_errors=True)
            _cleanup_sandbox_entry(reg, f"{e.id}")
            fp.write_bot_registry_md(reg, ROOT / "BOT_REGISTRY.md")
            return log
    log.update({"ok": False, "status": reg.get("bots", bot_id).status, "permissions_after": before["permissions"],
                "error": f"no passing candidate in {max_rounds} rounds"})
    shutil.rmtree(sandbox_root / sandbox_name, ignore_errors=True)
    return log


def _cleanup_sandbox_entry(reg: Registry, bot_id: str) -> None:
    # sandbox builds used a registry copy, so nothing to remove from production; kept for symmetry/safety.
    return None


if __name__ == "__main__":
    a = sys.argv
    if len(a) < 2: print(__doc__); sys.exit(2)
    rounds = int(a[a.index("--max-rounds") + 1]) if "--max-rounds" in a else 2
    try:
        out = repair(a[1], rounds)
    except (FactoryError, RuntimeError) as ex:
        out = {"ok": False, "error": str(ex)}
    (ROOT / "run").mkdir(exist_ok=True)
    (ROOT / "run" / f"repair-{a[1]}-{datetime.datetime.now():%Y%m%d-%H%M%S}.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(json.dumps(out, indent=1)); sys.exit(0 if out.get("ok") else 1)
