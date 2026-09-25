"""Factory status report (D-044): one JSON/markdown snapshot of bots, queue, lane health and recent audit — used by
Master 001 (`factory.py report`) to answer "what happened?" and written daily to STATUS.md by the `report` job.

  python tools/factory_report.py [--md]
"""
from __future__ import annotations
import json, os, sys, pathlib, time, datetime
ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core"))
from factory.registry import Registry   # noqa: E402
from factory.jobs import JobStore       # noqa: E402


def build() -> dict:
    reg = Registry(ROOT / "registry"); store = JobStore(ROOT / "run" / "jobs.sqlite3"); now = time.time()
    bots = [{"id": b.id, "name": b.name, "status": b.status, "verified": b.verified, "permissions": b.permissions}
            for b in sorted(reg.all("bots"), key=lambda b: b.id)]
    lanes = []
    for m in reg.all("models"):
        h = (m.limits or {}).get("health", {})
        state = "BLOCKED" if m.verified == "BLOCKED" else ("cooldown" if float(h.get("quota_until", 0) or 0) > now else h.get("last_outcome", "unprobed"))
        lanes.append({"id": m.id, "provider": m.provider, "state": state, "latency_s": h.get("latency_s"), "reason": h.get("reason")})
    # D-047 needs_owner: free lanes that require a human signup/key — the factory never self-applies
    owner = []
    led = ROOT / "registry" / "discovery.json"
    if led.exists():
        try:
            for k, v in json.loads(led.read_text(encoding="utf-8")).get("verdicts", {}).items():   # D-069: was reading the wrong level
                if v.get("verdict") == "needs_owner": owner.append(f"ACTION REQUIRED (owner): {k} — {v.get('reason', '')[:140]}")
        except Exception: pass
    inf = ROOT / "registry" / "infra.json"                                                          # D-118
    if inf.exists():
        try:
            rs = json.loads(inf.read_text(encoding="utf-8")).get("resources", {})
            miss = sorted(k for k, v in rs.items() if v.get("status") in ("missing", "invalid_key"))
            if miss: owner.append(f"ACTION REQUIRED (owner): {len(miss)} free resources need a human signup/key — {', '.join(miss[:6])}{'…' if len(miss) > 6 else ''} (docs/INFRA.md)")
        except Exception: pass
    prob = sorted(t.id for t in reg.all("tools") if t.kind == "mcp" and "PROBATION" in (t.scope or ""))   # D-108/D-110
    if prob:
        owner.append(f"DECISION (owner): {len(prob)} MCP server(s) sandbox-verified, on probation: {', '.join(prob)} — "
                     f"`factory_worker.py approve-tool <id>` to make them grantable to bots, or leave them (nothing uses them)")
    st = ROOT / "run" / "selftest.json"          # D-074
    try:
        stj = json.loads(st.read_text(encoding="utf-8"))
        if not stj.get("ok"): owner.append(f"WORKER BLOCKED: core/tests red on current code ({stj.get('tail')}) — fix and push; nothing is processed until then")
    except Exception: pass
    bench = sorted([(m.id, (m.limits or {}).get("bench")) for m in reg.all("models") if (m.limits or {}).get("bench", {}).get("total")],
                   key=lambda x: (-(x[1]["pass"] / x[1]["total"]), x[1].get("secs", 9e9)))
    jobs = store.list()
    recent = [j for j in jobs if now - float(j["updated"]) < 86400]
    audit = store.audit_rows(limit=25)
    live = liveness(store, jobs, now)                                   # D-100
    head = [f"FACTORY {live['state'].upper()}: {live['reason']}"] if live["state"] != "running" else []
    rows600 = store.audit_rows(limit=600)
    out_ = next((r for r in rows600 if r["event"] == "factory.outage"), None)                          # D-121
    outage = None
    if out_:
        try: od = json.loads(out_["detail"]) if isinstance(out_.get("detail"), str) else (out_.get("detail") or {})
        except Exception: od = {}
        outage = {"at": out_.get("ts"), **{k: od.get(k) for k in ("gap_min", "silent_since", "cause")}}
        if now - float(out_["ts"]) < 86400:
            head.append(f"OUTAGE in the last 24 h: down {od.get('gap_min')} min from {str(od.get('silent_since'))[:16]} — {od.get('cause')}")
    tam = next((r for r in rows600 if r["event"] in ("audit.verified", "audit.TAMPERED")), None)     # D-123
    if tam and tam["event"] == "audit.TAMPERED":
        head.insert(0, f"AUDIT CHAIN BROKEN at {str(tam.get('ts'))[:16]}: audit/*.jsonl no longer verifies — treat history after the break as untrusted (see `audit-verify`)")
    can = next((r for r in rows600 if r["event"] == "factory.canary"), None)       # D-117
    canary = None
    if can:
        try: d = json.loads(can["detail"]) if isinstance(can.get("detail"), str) else (can.get("detail") or {})
        except Exception: d = {}
        canary = {"at": can.get("ts"), "verdict": d.get("verdict"), "lane": d.get("lane"), "secs": d.get("secs")}
        if d.get("verdict") == "FAIL":
            head.append(f"FACTORY CANARY FAILED at {str(can.get('ts'))[:16]} (lane {d.get('lane')}): the factory itself, not a bot, is broken — see AUDIT factory.canary")
    return {"generated": datetime.datetime.now().isoformat(timespec="seconds"),
            "bots": {"active": sum(b["status"] == "active" for b in bots), "total": len(bots), "list": bots},
            "queue": store.summary(), "canary": canary, "outage": outage,
            "jobs_24h": [{"id": j["id"][:8], "kind": j["kind"], "state": j["state"], "attempts": j["attempts"], "class": j.get("failure_class"),
                          "bot": j["payload"].get("bot_id"), "objective": (j["payload"].get("objective") or "")[:70]} for j in recent],
            "lanes": lanes, "healthy_lanes": [l["id"] for l in lanes if l["state"] == "ok"],
            "attention": head + [f"job {j['id'][:8]} {j['kind']} paused ({j.get('failure_class')})" for j in jobs if j["state"] == "paused"]
                         + [f"bot {b['id']} {b['name']} is {b['status']}" for b in bots if b["status"] not in ("active", "retired") and b["id"] != "001"
                            and not (b["status"] == "paused" and now - _updated_ts(reg.get("bots", b["id"])) > 3 * 86400)]   # D-104: settled paused/retired bots are counts, not alarms
                         + ([f"{sum(b['status'] == 'retired' for b in bots)} retired / {sum(b['status'] == 'paused' for b in bots)} paused bots (see Bots table)"]
                            if any(b["status"] in ("retired", "paused") for b in bots) else [])
                         + [f"lane {l['id']} BLOCKED: {' '.join(str(l['reason']).split())[:80]}" for l in lanes if l["state"] == "BLOCKED" and l.get("reason")]
                         + owner,
            "liveness": live,
            "bench": [{"id": i, "score": f"{b['pass']}/{b['total']}", "secs": b.get("secs"), "runs": b.get("runs", 1)} for i, b in bench],
            "recent_audit": [f"{a['ts']} {a['event']} {a.get('bot_id') or ''}".strip() for a in audit]}


STALE_WORKER_S = 2 * 3600      # hourly probe/tick chain + 15-min task tick: >2 h of silence means nobody is executing
STUCK_QUEUE_S = 30 * 60        # a queued job older than this while a worker is alive = pick loop broken


def _updated_ts(entry) -> float:
    try: return datetime.datetime.fromisoformat(str(getattr(entry, "updated", ""))).timestamp()
    except Exception: return 0.0


def liveness(store, jobs: list[dict], now: float) -> dict:
    """D-100: is anything actually executing? Evidence = the newest audit row written by a worker (job.claimed/done,
    worker.selftest/restart, probe/tick). STATUS.md used to show yesterday's numbers as if current; with the laptop
    asleep the owner could not tell. `state`: running | stalled (worker silent > 2 h) | stuck (alive but queue not
    draining) | idle-blocked (self-test red)."""
    rows = store.audit_rows(limit=400)
    worker_rows = [r for r in rows if r["event"].startswith(("job.claimed", "job.done", "job.failed", "worker.")) or r["event"] in ("lane.probed", "tick.fired")]
    last = max((float(r["ts"]) for r in worker_rows), default=0.0)
    age = now - last if last else None
    queued = [j for j in jobs if j["state"] == "queued" and float(j.get("not_before") or 0) <= now]
    oldest_ready = min((now - float(j["created"]) for j in queued), default=0.0)
    st = ROOT / "run" / "selftest.json"
    try:
        selftest_ok = bool(json.loads(st.read_text(encoding="utf-8")).get("ok"))
    except Exception:
        selftest_ok = True
    if not selftest_ok:
        state, reason = "idle-blocked", "worker self-test gate is red; nothing is processed until the tests pass"
    elif age is None or age > STALE_WORKER_S:
        state, reason = "stalled", (f"no worker activity for {int(age // 60)} min" if age else "no worker activity on record") + " (laptop asleep/offline or worker task dead)"
    elif queued and oldest_ready > STUCK_QUEUE_S and age > STUCK_QUEUE_S:
        state, reason = "stuck", f"{len(queued)} ready jobs waiting {int(oldest_ready // 60)} min while the worker is silent"
    else:
        state, reason = "running", f"last worker activity {int((age or 0) // 60)} min ago"
    return {"state": state, "reason": reason, "last_worker_ts": last, "ready_queued": len(queued), "oldest_ready_min": int(oldest_ready // 60)}


def markdown(r: dict) -> str:
    lv = r.get("liveness") or {}
    out = [f"# FACTORY STATUS — {r['generated']}", "", f"**Worker:** {lv.get('state', '?')} — {lv.get('reason', '')}", "",
           f"**Bots:** {r['bots']['active']}/{r['bots']['total']} active   **Queue:** {json.dumps(r['queue'])}   **Healthy lanes:** {', '.join(r['healthy_lanes']) or 'none'}", ""]
    if r["attention"]:
        out += ["## Needs attention"] + [f"- {a}" for a in r["attention"]] + [""]
    out += ["## Bots", "| id | name | status | verified | permissions |", "|---|---|---|---|---|"]
    out += [f"| {b['id']} | {b['name']} | {b['status']} | {b['verified']} | {', '.join(b['permissions'])} |" for b in r["bots"]["list"]]
    out += ["", "## Jobs (24h)", "| id | kind | state | att | class | bot | objective |", "|---|---|---|---|---|---|---|"]
    out += [f"| {j['id']} | {j['kind']} | {j['state']} | {j['attempts']} | {j['class'] or '-'} | {j['bot'] or '-'} | {j['objective']} |" for j in r["jobs_24h"]]
    if r.get("bench"):
        out += ["", "## Lane quality (D-050, reference suite, rolling window)", "| lane | score | secs | runs |", "|---|---|---|---|"]
        out += [f"| {b['id']} | {b['score']} | {b['secs']} | {b['runs']} |" for b in r["bench"]]
    out += ["", "## Lanes", "| id | provider | state | latency s |", "|---|---|---|---|"]
    out += [f"| {l['id']} | {l['provider']} | {l['state']} | {l['latency_s'] or '-'} |" for l in r["lanes"]]
    return "\n".join(out) + "\n"


def brief(r: dict) -> str:
    """<=900 chars for small-context masters (D-044): counts, attention items, last 3 jobs. Full detail is in STATUS.md."""
    lv = r.get("liveness") or {}
    lines = [f"FACTORY {r['generated'][:16]} [{lv.get('state', '?')}: {lv.get('reason', '')[:70]}]: bots {r['bots']['active']}/{r['bots']['total']} active; "
             f"queue {json.dumps(r['queue'])}; healthy lanes {len(r['healthy_lanes'])}."]
    lines += ["ATTENTION: " + ("; ".join(a[:90] for a in r["attention"][:5]) if r["attention"] else "nothing")]
    last = r["jobs_24h"][-3:]
    lines += ["LAST JOBS: " + "; ".join(f"{j['kind']} {j['bot'] or j['objective'][:30] or ''} -> {j['state']}" for j in last)]
    lines += ["Full report: STATUS.md"]
    return "\n".join(lines)[:900]


if __name__ == "__main__":
    r = build()
    print(markdown(r) if "--md" in sys.argv else brief(r) if "--brief" in sys.argv else json.dumps(r, indent=1))
