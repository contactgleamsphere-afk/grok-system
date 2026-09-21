"""Factory monitor: re-test every active bot, demote on failure, write MONITOR.md. (Phase 4 — monitoring/recovery)

  python tools/factory_monitor.py [--only 002,005] [--dry-run]

Runs each bot's acceptance tests through factory_pipeline.run_tests (same runner as build time), records
via BotFactory.record_test_result (active↔testing), and appends a dated row to MONITOR.md. Exit 1 if any bot
regressed. Intended to be scheduled nightly (scripts/windows/register-monitor-task.ps1).
"""
from __future__ import annotations
import json, os, sys, pathlib, time, datetime
ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core")); sys.path.insert(0, str(ROOT / "tools"))
from factory.registry import Registry            # noqa: E402
from factory.factory import BotFactory           # noqa: E402
import factory_pipeline as fp                    # noqa: E402


def monitor(only: set[str] | None = None, dry_run: bool = False, runner=None) -> dict:
    reg = Registry(ROOT / "registry"); bots_root = fp.LAPTOP_BOTS if fp.WIN else ROOT / "bots"
    f = BotFactory(reg, bots_root); runner = runner or fp.run_tests
    rows, regressed = [], []
    for e in reg.all("bots"):
        if (e.status != "active" and e.id != "001") or (only and e.id not in only):
            continue
        bot_dir = bots_root / f"{e.id}-{e.name}"
        t0 = time.time()
        try:
            res = runner(bot_dir); p, t = int(res["pass"]), int(res["total"]); ev = res["evidence"]
        except Exception as ex:                       # runner crash = failure, never silent
            p, t, ev = 0, len(e.tests), f"runner error: {ex}"
        before = e.status
        if not dry_run:
            e2 = f.record_test_result(e.id, p, t, f"monitor {datetime.date.today()}: {ev}")
            after = e2.status
        else:
            after = "active" if p == t and t > 0 else "testing"
        if after != "active":
            regressed.append(e.id)
        rows.append({"id": e.id, "name": e.name, "pass": p, "total": t, "before": before, "after": after,
                     "seconds": int(time.time() - t0)})
    if not dry_run:
        fp.write_bot_registry_md(reg, ROOT / "BOT_REGISTRY.md")
        md = ROOT / "MONITOR.md"
        head = "# MONITOR — nightly re-verification of active bots\n\n| date | bot | pass | status | s |\n|---|---|---|---|---|\n"
        body = md.read_text(encoding="utf-8") if md.exists() else head
        for r in rows:
            body += f"| {datetime.datetime.now():%Y-%m-%d %H:%M} | {r['id']} {r['name']} | {r['pass']}/{r['total']} | {r['before']}→{r['after']} | {r['seconds']} |\n"
        md.write_text(body, encoding="utf-8")
    return {"ok": not regressed, "regressed": regressed, "rows": rows}


if __name__ == "__main__":
    a = sys.argv
    only = set(a[a.index("--only") + 1].split(",")) if "--only" in a else None
    out = monitor(only, "--dry-run" in a)
    print(json.dumps(out, indent=1)); sys.exit(0 if out["ok"] else 1)
