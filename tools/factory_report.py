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
    bench = sorted([(m.id, (m.limits or {}).get("bench")) for m in reg.all("models") if (m.limits or {}).get("bench", {}).get("total")],
                   key=lambda x: (-(x[1]["pass"] / x[1]["total"]), x[1].get("secs", 9e9)))
    jobs = store.list()
    recent = [j for j in jobs if now - float(j["updated"]) < 86400]
    audit = store.audit_rows(limit=25)
    return {"generated": datetime.datetime.now().isoformat(timespec="seconds"),
            "bots": {"active": sum(b["status"] == "active" for b in bots), "total": len(bots), "list": bots},
            "queue": store.summary(),
            "jobs_24h": [{"id": j["id"][:8], "kind": j["kind"], "state": j["state"], "attempts": j["attempts"], "class": j.get("failure_class"),
                          "bot": j["payload"].get("bot_id"), "objective": (j["payload"].get("objective") or "")[:70]} for j in recent],
            "lanes": lanes, "healthy_lanes": [l["id"] for l in lanes if l["state"] == "ok"],
            "attention": [f"job {j['id'][:8]} {j['kind']} paused ({j.get('failure_class')})" for j in jobs if j["state"] == "paused"]
                         + [f"bot {b['id']} {b['name']} is {b['status']}" for b in bots if b["status"] not in ("active",) and b["id"] != "001"]
                         + [f"lane {l['id']} BLOCKED: {l['reason']}" for l in lanes if l["state"] == "BLOCKED" and l.get("reason")]
                         + owner,
            "bench": [{"id": i, "score": f"{b['pass']}/{b['total']}", "secs": b.get("secs"), "runs": b.get("runs", 1)} for i, b in bench],
            "recent_audit": [f"{a['ts']} {a['event']} {a.get('bot_id') or ''}".strip() for a in audit]}


def markdown(r: dict) -> str:
    out = [f"# FACTORY STATUS — {r['generated']}", "",
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
    lines = [f"FACTORY {r['generated'][:16]}: bots {r['bots']['active']}/{r['bots']['total']} active; queue {json.dumps(r['queue'])}; "
             f"healthy lanes {len(r['healthy_lanes'])}."]
    lines += ["ATTENTION: " + ("; ".join(a[:90] for a in r["attention"][:5]) if r["attention"] else "nothing")]
    last = r["jobs_24h"][-3:]
    lines += ["LAST JOBS: " + "; ".join(f"{j['kind']} {j['bot'] or j['objective'][:30] or ''} -> {j['state']}" for j in last)]
    lines += ["Full report: STATUS.md"]
    return "\n".join(lines)[:900]


if __name__ == "__main__":
    r = build()
    print(markdown(r) if "--md" in sys.argv else brief(r) if "--brief" in sys.argv else json.dumps(r, indent=1))
