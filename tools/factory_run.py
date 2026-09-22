"""D-063: RUN a built bot (or a whole plan) on real input — the factory's output is bots that do work, not bots that
only pass their own tests.

    python tools/factory_run.py bot 013 --task "Filter ERROR lines from app.log into errors.txt" --in C:\\x\\in --out C:\\x\\out
    python tools/factory_run.py plan 25a47cdb --in C:\\x\\in --out C:\\x\\out

`plan` looks up the plan job's steps (from the audit / create jobs), resolves each step to its bot (created or reused),
and runs them in order: step N's produced files are staged as step N+1's inputs (in the same run directory). Each
step is checked against its declared `produces` — a missing declared output fails the run at that step (no silent
"success"). Everything is written to <out>/<step>-<bot>/ plus RUN.json; nothing touches the bot bundles.
"""
from __future__ import annotations
import datetime, json, os, re, shutil, subprocess, sys, pathlib, time
ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core")); sys.path.insert(0, str(ROOT / "tools"))
from factory.registry import Registry            # noqa: E402
from factory.guard import bundle_drift            # noqa: E402
from factory.jobs import JobStore                # noqa: E402
import factory_pipeline as fp                    # noqa: E402

TASK_RUNNER = ROOT / "scripts" / "windows" / "run-bot-task.ps1"
RUNS = pathlib.Path(r"C:\AI\Factory\run\runs") if fp.WIN else ROOT / "run" / "runs"


def run_bot(bot_id: str, task: str, in_dir: pathlib.Path | None, out_dir: pathlib.Path, cap: int = 300, runner=None) -> dict:
    reg = Registry(ROOT / "registry"); e = reg.get("bots", bot_id)
    if e is None: raise ValueError(f"unknown bot {bot_id}")
    if e.status != "active":
        return {"ok": False, "bot": bot_id, "error": f"bot {bot_id} is {e.status}, only active bots run real tasks"}
    bot_dir = (fp.LAPTOP_BOTS if fp.WIN else ROOT / "bots") / f"{e.id}-{e.name}"
    drift = bundle_drift(bot_dir, getattr(e, "seal", None))        # D-068
    if drift and drift != ["<unsealed>"]:
        return {"ok": False, "bot": bot_id, "error": f"bundle integrity: sealed files changed outside the factory: {drift}; rebuild/repair to reseal"}
    if runner is None:
        if not fp.WIN or not TASK_RUNNER.exists():
            raise RuntimeError("real tasks run on the laptop only (run-bot-task.ps1)")
        def runner(bot_dir, task, in_dir, out_dir, cap):
            cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(TASK_RUNNER), "-BotDir", str(bot_dir),
                   "-Task", task, "-InDir", str(in_dir or ""), "-OutDir", str(out_dir), "-Cap", str(cap)]
            out = subprocess.run(cmd, capture_output=True, text=True, timeout=cap * 2 + 120).stdout
            m = re.search(r"RESULTJSON (\{.*\})", out)
            if not m: raise RuntimeError("task runner produced no RESULTJSON:\n" + out[-1200:])
            return json.loads(m.group(1))
    res = runner(bot_dir, task, in_dir, out_dir, cap)
    res["ok"] = res.get("status") == "done" and not res.get("quota")
    res["bot"] = bot_id
    return res


def plan_steps(store: JobStore, plan_prefix: str) -> list[dict]:
    """Ordered steps of a plan job: created bots (from create jobs with payload.plan) and reused ones (plan.reused audit)."""
    pj = store.resolve(plan_prefix)
    steps: dict[int, dict] = {}
    for j in store.list():
        if j["kind"] == "create" and j["payload"].get("plan") == pj:
            bot = None
            for r in store.audit_rows(5000):
                if r["job_id"] == j["id"] and r["event"] == "bot.created": bot = r["bot_id"]; break
            steps[int(j["payload"]["step"])] = {"objective": j["payload"]["objective"], "produces": j["payload"].get("produces", []), "bot": bot, "job": j["id"][:8]}
    for r in store.audit_rows(5000):
        if r["job_id"] == pj and r["event"] == "plan.reused":
            d = json.loads(r["detail"]); steps[int(d["step"])] = {"objective": f"(reused bot {d['bot_id']})", "produces": [], "bot": d["bot_id"], "job": None, "reused": True}
    return [dict(step=i, **steps[i]) for i in sorted(steps)]


def run_plan(plan_prefix: str, in_dir: pathlib.Path | None, out_root: pathlib.Path | None = None, cap: int = 300, runner=None) -> dict:
    store = JobStore(ROOT / "run" / "jobs.sqlite3")
    steps = plan_steps(store, plan_prefix)
    if not steps: return {"ok": False, "error": f"plan {plan_prefix}: no steps found"}
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_root = out_root or (RUNS / f"plan-{plan_prefix[:8]}-{stamp}")
    out_root.mkdir(parents=True, exist_ok=True)
    stage = out_root / "_stage"; stage.mkdir(exist_ok=True)
    if in_dir:
        for f in pathlib.Path(in_dir).iterdir():
            if f.is_file(): shutil.copy(f, stage / f.name)
    report = {"plan": plan_prefix, "started": stamp, "steps": [], "ok": True}
    for st in steps:
        if not st.get("bot"):
            report["steps"].append({**st, "ok": False, "error": "step has no bot (create failed or still queued)"}); report["ok"] = False; break
        step_out = out_root / f"{st['step']}-{st['bot']}"
        task = st["objective"] + (f" The input files are already in the workspace: {', '.join(sorted(p.name for p in stage.iterdir()))}." if any(stage.iterdir()) else "")
        r = run_bot(st["bot"], task, stage, step_out, cap, runner)
        missing = [f for f in (st.get("produces") or []) if not (step_out / f).exists()]
        r["missing_outputs"] = missing
        if missing: r["ok"] = False; r["error"] = f"declared outputs not produced: {missing}"
        report["steps"].append({**st, **{k: r.get(k) for k in ("ok", "status", "secs", "produced", "reply", "quota", "missing_outputs", "error", "log", "chain")}})
        if not r["ok"]: report["ok"] = False; break
        for f in step_out.iterdir():             # step N's outputs become step N+1's inputs (inputs persist too)
            if f.is_file(): shutil.copy(f, stage / f.name)
    report["outputs"] = sorted(p.name for p in stage.iterdir())
    (out_root / "RUN.json").write_text(json.dumps(report, indent=1), encoding="utf-8")
    report["dir"] = str(out_root)
    return report


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    if a and a[0] == "bot":
        out = run_bot(a[1], opt("--task", ""), pathlib.Path(opt("--in")) if opt("--in") else None, pathlib.Path(opt("--out", str(RUNS / f"bot-{a[1]}"))), int(opt("--cap", 300)))
    elif a and a[0] == "plan":
        out = run_plan(a[1], pathlib.Path(opt("--in")) if opt("--in") else None, pathlib.Path(opt("--out")) if opt("--out") else None, int(opt("--cap", 300)))
    else:
        print(__doc__); sys.exit(2)
    print(json.dumps(out, indent=1, default=str)); sys.exit(0 if out.get("ok") else 1)
