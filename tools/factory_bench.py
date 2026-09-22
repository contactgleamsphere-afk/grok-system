"""Lane quality benchmark (D-050).

A lane that passes the D-047 sandbox (one real tool loop) has proved *capability*, not *task quality*: bot 010
showed a discovered lane refusing a trivial file write that groq handles 4/4 (D-049). This module runs a fixed
reference suite — the acceptance tests of a stable, VERIFIED reference bot — against ONE pinned lane (no fallbacks,
so the score is attributable) and stores the result in the lane's registry entry:

    limits.bench = {"pass": 3, "total": 4, "secs": 93, "ref": "009", "at": "2026-09-22T01:10:00"}

`factory_pipeline.default_fallbacks()` then ranks benchmarked lanes by pass-rate (ties: faster) ahead of
un-benchmarked ones. Scores age out after BENCH_TTL_DAYS so a lane is re-measured, not trusted forever.

    python tools/factory_bench.py [--lane or-nex-n25-pro] [--ref 009] [--all] [--stale-only]

Runs on the laptop only (needs nanobot + the reference bot bundle). Pure functions (`due`, `record`, `rank`) are
unit-tested off-laptop.
"""
from __future__ import annotations
import datetime, json, os, sys, pathlib
ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core")); sys.path.insert(0, str(ROOT / "tools"))
from factory.registry import Registry, ModelEntry  # noqa: E402

REF_BOT = "009"            # line-dedupe-bot: 4 tests (echo, 2x tool-loop file tasks, sandbox escape) — all deterministic
BENCH_TTL_DAYS = 14
LOCAL = ("local3b", "local4b")


def _now() -> str:
    return datetime.datetime.now().replace(microsecond=0).isoformat()


def due(m: ModelEntry, now: datetime.datetime | None = None, ttl_days: int = BENCH_TTL_DAYS) -> bool:
    """A lane needs a benchmark if it is a healthy remote tool lane with no score or a stale one."""
    now = now or datetime.datetime.now()
    if m.location != "remote" or m.verified == "BLOCKED" or "tools" not in (m.capabilities or []):
        return False
    if not ((m.limits or {}).get("health") or {}).get("ok", True):
        return False
    b = (m.limits or {}).get("bench") or {}
    if not b.get("at"):
        return True
    try:
        return (now - datetime.datetime.fromisoformat(b["at"])).days >= ttl_days
    except ValueError:
        return True


BENCH_WINDOW = 3     # rolling window: free lanes are noisy run-to-run (or-ling 4/4 then 3/4); one run must not reorder the chain


def record(reg: Registry, lane: str, passed: int, total: int, secs: int, ref: str = REF_BOT) -> ModelEntry:
    """Append a run to `limits.bench_runs` (last BENCH_WINDOW kept) and write the aggregate to `limits.bench`
    (pass/total summed over the window, secs = mean). Consumers only read `limits.bench`."""
    m = reg.get("models", lane)
    if m is None:
        raise KeyError(lane)
    m.limits = dict(m.limits or {})
    runs = list(m.limits.get("bench_runs") or [])
    runs.append({"pass": int(passed), "total": int(total), "secs": int(secs), "ref": ref, "at": _now()})
    runs = runs[-BENCH_WINDOW:]
    m.limits["bench_runs"] = runs
    m.limits["bench"] = {"pass": sum(r["pass"] for r in runs), "total": sum(r["total"] for r in runs),
                         "secs": int(sum(r["secs"] for r in runs) / len(runs)), "ref": ref, "at": runs[-1]["at"], "runs": len(runs)}
    reg.upsert("models", m)
    return m


def rank(reg: Registry) -> list[dict]:
    rows = []
    for m in reg.all("models"):
        b = (m.limits or {}).get("bench")
        if b and b.get("total"):
            rows.append({"lane": m.id, "score": round(b["pass"] / b["total"], 2), "pass": b["pass"], "total": b["total"],
                         "secs": b.get("secs"), "runs": b.get("runs", 1), "at": b.get("at"), "verified": m.verified})
    rows.sort(key=lambda r: (-r["score"], r["secs"] or 9e9))
    return rows


def run_one(reg: Registry, lane: str, ref: str = REF_BOT, runner=None) -> dict:
    """Run the reference suite pinned to `lane`. `runner(bot_dir, lane) -> {pass,total,secs,evidence}` is injectable."""
    import factory_pipeline as fp
    bots_root = fp.LAPTOP_BOTS if fp.WIN else ROOT / "bots"
    e = reg.get("bots", ref)
    if e is None:
        raise RuntimeError(f"reference bot {ref} not in registry")
    bot_dir = bots_root / f"{e.id}-{e.name}"
    runner = runner or (lambda d, l: fp.run_tests(d, cap=240, lane=l))
    res = runner(bot_dir, lane)
    record(reg, lane, int(res["pass"]), int(res["total"]), int(res.get("secs", 0)), ref)
    return {"lane": lane, "pass": res["pass"], "total": res["total"], "secs": res.get("secs"), "evidence": str(res.get("evidence", ""))[:600]}


def run(lanes: list[str] | None = None, ref: str = REF_BOT, stale_only: bool = False, max_lanes: int = 3, runner=None) -> dict:
    reg = Registry(ROOT / "registry")
    models = {m.id: m for m in reg.all("models")}
    if lanes:
        todo = [l for l in lanes if l in models]
    else:
        todo = [m.id for m in models.values() if m.id not in LOCAL and due(m)] if stale_only else \
               [m.id for m in models.values() if m.id not in LOCAL and m.location == "remote" and m.verified != "BLOCKED"]
    todo = todo[:max_lanes]
    out = {"ref": ref, "results": [], "errors": []}
    for lane in todo:
        try:
            out["results"].append(run_one(reg, lane, ref, runner))
        except Exception as ex:   # one bad lane must not stop the sweep
            out["errors"].append({"lane": lane, "error": str(ex)[:300]})
    out["rank"] = rank(reg)
    return out


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    lanes = [x for x in (opt("--lane") or "").split(",") if x] or None
    if "--rank" in a:
        print(json.dumps(rank(Registry(ROOT / "registry")), indent=1)); sys.exit(0)
    print(json.dumps(run(lanes, opt("--ref", REF_BOT), "--stale-only" in a, int(opt("--max", 3))), indent=1))
