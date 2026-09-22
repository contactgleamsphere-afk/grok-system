"""Self-improvement, stage 1 (D-057): evidence → proposals. Never self-applying.

The factory already repairs *bots*. This module looks at the factory's OWN behaviour (audit table, registry, bench)
and turns recurring patterns into concrete, reviewable improvement proposals for the factory itself:

    proposals/YYYY-MM-DD.md      human-readable, one section per finding, each with evidence + suggested change
    proposals/YYYY-MM-DD.json    machine-readable (kind, severity, evidence, suggestion, auto_actionable)

Rules (from the owner's contract): propose → (human/architect) review → sandbox → test → approve. This module
only does the first step. The only actions it may take itself are ones that are already-approved factory
mechanisms (e.g. enqueue a `bench` for a lane with no score, enqueue `probe --only` for a lane that timed out):
those are listed as `auto_actionable` and enqueued by the worker with an audit entry.

    python tools/factory_insight.py [--days 7] [--write]
"""
from __future__ import annotations
import collections, datetime, json, os, re, sys, pathlib, time
ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core")); sys.path.insert(0, str(ROOT / "tools"))
from factory.registry import Registry   # noqa: E402
from factory.jobs import JobStore       # noqa: E402

FAIL_RE = re.compile(r"T(\d) FAIL (\d+)s \[(\w+)\] expect='([^']*)' last='([^']*)'")


def _classify_fail(status: str, expect: str, last: str) -> str:
    if status == "TIMEOUT": return "timeout"
    if "CAPABILITY_MISSING" in last: return "capability_missing"
    if "429" in last or "rate" in last.lower(): return "quota"
    if not last: return "empty_reply"
    if "request fitting" in last or "tiktoken" in last or ("context" in last.lower() and "token" in last.lower()): return "context_overflow"
    if "NativeCommandError" in last or "CommandNotFound" in last or "is not recognized" in last: return "shell_error"
    if expect and re.search(r"(^|\s|:)" + re.escape(expect) + r"(\s|$|\.)", last): return "answer_wrapped"      # right value, wrong format (e.g. "RESULT: 1 line")
    return "wrong_answer"


def gather(days: int = 7) -> dict:
    """Pure data collection: failure classes, lanes used by failed builds, bench coverage, paused jobs, repair stats."""
    store = JobStore(ROOT / "run" / "jobs.sqlite3"); reg = Registry(ROOT / "registry")
    since = time.time() - days * 86400
    rows = [r for r in store.audit_rows(5000) if r["ts"] >= since]
    fails = collections.Counter(); fail_examples = collections.defaultdict(list)
    tests_run = 0
    for r in rows:
        if r["event"] != "bot.tested": continue
        d = json.loads(r["detail"] or "{}"); res = d.get("result") or ""
        tests_run += 1
        for n, secs, st, exp, last in FAIL_RE.findall(res):
            k = _classify_fail(st, exp, last); fails[k] += 1
            if len(fail_examples[k]) < 3: fail_examples[k].append({"bot": r["bot_id"], "test": int(n), "expect": exp[:40], "last": last[:80]})
    repairs = [json.loads(r["detail"] or "{}") for r in rows if r["event"] == "bot.repair"]
    repair_ok = sum(1 for x in repairs if x.get("ok")); repair_rounds = sum(len(x.get("rounds", [])) for x in repairs)
    rejected = [x for x in repairs for rd in x.get("rounds", []) if rd.get("rejected")]
    jobs = store.list()
    paused = [{"id": j["id"][:8], "kind": j["kind"], "class": j.get("failure_class"), "error": (j.get("error") or "")[:160]} for j in jobs if j["state"] == "paused"]
    failed_classes = collections.Counter(j.get("failure_class") for j in jobs if j["state"] in ("failed", "paused") and float(j["updated"]) >= since)
    models = reg.all("models")
    remote_ok = [m for m in models if m.location == "remote" and m.verified != "BLOCKED" and ((m.limits or {}).get("health") or {}).get("ok", True)]
    unbenched = [m.id for m in remote_ok if not ((m.limits or {}).get("bench") or {}).get("total")]
    weak = [(m.id, b) for m in remote_ok for b in [((m.limits or {}).get("bench") or {})] if b.get("total") and b["pass"] / b["total"] < 0.75]
    sec = [json.loads(r["detail"] or "{}").get("error", "")[:160] for r in rows if r["event"] == "security.violation"]
    lane_of_failed_spec = collections.Counter()
    for r in rows:
        if r["event"] == "bot.created":
            d = json.loads(r["detail"] or "{}"); lane_of_failed_spec[d.get("lane") or "?"] += 0
    return {"days": days, "tests_run": tests_run, "fails": dict(fails), "fail_examples": dict(fail_examples),
            "repairs": {"total": len(repairs), "ok": repair_ok, "rounds": repair_rounds, "rejected_candidates": len(rejected)},
            "paused": paused, "failed_classes": dict(failed_classes), "unbenched_lanes": unbenched,
            "weak_lanes": [{"id": i, "score": f"{b['pass']}/{b['total']}"} for i, b in weak], "security_violations": sec,
            "bots": {"total": len(reg.all("bots")), "active": sum(1 for b in reg.all("bots") if b.status == "active")}}


def propose(ev: dict) -> list[dict]:
    """Turn evidence into proposals. Each has kind, severity, evidence, suggestion, auto_actionable (an approved
    mechanism the worker may enqueue) — never a code change."""
    P: list[dict] = []
    f = ev["fails"]; total_f = sum(f.values()) or 1
    if f.get("answer_wrapped", 0) >= 2:
        P.append({"kind": "template", "severity": "medium",
                  "evidence": f"{f['answer_wrapped']} of {total_f} test failures had the right value inside a sentence ({ev['fail_examples']['answer_wrapped'][:2]})",
                  "suggestion": "Tighten the bot AGENTS template 'RESULT: <answer>' rule further or let the runner accept `RESULT: <expected> ...` when the expected token is the first word after the prefix. Needs a human decision: stricter bots vs. looser matcher.",
                  "auto_actionable": None})
    if f.get("context_overflow", 0) >= 1:
        P.append({"kind": "lanes", "severity": "medium",
                  "evidence": f"{f['context_overflow']} failures where the prompt no longer fit the lane's context ({ev['fail_examples']['context_overflow'][:2]})",
                  "suggestion": "A small-TPM lane was primary for a bot with a long tool contract/history. Check config hygiene (D-035) and maxToolResultChars; consider excluding <16k-context lanes from chains of bots with >2 tools.",
                  "auto_actionable": None})
    if f.get("timeout", 0) >= 2:
        P.append({"kind": "lanes", "severity": "medium",
                  "evidence": f"{f['timeout']} test timeouts in {ev['days']}d ({ev['fail_examples']['timeout'][:2]})",
                  "suggestion": "Timeouts are usually a slow/over-loaded primary. Compare bench `secs` per lane and consider lowering per-test cap from 300 s only after the chain's median is known.",
                  "auto_actionable": {"kind": "probe", "payload": {"only": [], "hour": datetime.datetime.now().strftime("%Y-%m-%dT%H")}}})
    if f.get("capability_missing", 0) >= 1:
        P.append({"kind": "architect", "severity": "high" if f["capability_missing"] >= 2 else "low",
                  "evidence": f"{f['capability_missing']} CAPABILITY_MISSING failures ({ev['fail_examples']['capability_missing'][:2]})",
                  "suggestion": "spec_consistency (D-052/D-093) covers write/read/web/shell hints; if these prompts use other verbs, extend its patterns.",
                  "auto_actionable": None})
    if f.get("wrong_answer", 0) / total_f > 0.5 and f.get("wrong_answer", 0) >= 4:
        P.append({"kind": "quality", "severity": "medium",
                  "evidence": f"{f['wrong_answer']} genuinely wrong answers of {total_f} failures",
                  "suggestion": "Most failures are reasoning quality, not plumbing. Primary and builder lanes are already bench-ranked (D-050/D-095); check whether the weak lanes below are still in chains.",
                  "auto_actionable": None})
    if ev["unbenched_lanes"]:
        P.append({"kind": "lanes", "severity": "low", "evidence": f"lanes without a quality score: {ev['unbenched_lanes']}",
                  "suggestion": "Benchmark them so default_fallbacks() can rank them.",
                  "auto_actionable": {"kind": "bench", "payload": {"lanes": ev["unbenched_lanes"][:3], "day": datetime.date.today().isoformat(), "trigger": "insight"}}})
    if ev["weak_lanes"]:
        P.append({"kind": "lanes", "severity": "low", "evidence": f"lanes scoring <75% on the reference suite: {ev['weak_lanes']}",
                  "suggestion": "They sit at the tail of the chain; lanes <50% over a full window are auto-demoted from chains by D-096 (see registry notes).",
                  "auto_actionable": None})
    r = ev["repairs"]
    if r["total"] >= 2 and r["ok"] / r["total"] < 0.5:
        P.append({"kind": "repair", "severity": "medium", "evidence": f"repair success {r['ok']}/{r['total']} ({r['rounds']} rounds, {r['rejected_candidates']} rejected candidates)",
                  "suggestion": "Repair rewrites only instructions. When the failing test is a fixture/format issue the fix belongs in the template (D-053 finding); consider a 'diagnose' step that classifies the failure before choosing repair vs rearchitect.",
                  "auto_actionable": None})
    if ev["paused"]:
        P.append({"kind": "attention", "severity": "high" if any(p["class"] == "security" for p in ev["paused"]) else "medium",
                  "evidence": f"{len(ev['paused'])} paused jobs: {ev['paused'][:3]}",
                  "suggestion": "Owner decision per job: `resume <id> [--allow …]` or `cancel <id>`.", "auto_actionable": None})
    if ev["security_violations"]:
        P.append({"kind": "security", "severity": "info", "evidence": f"{len(ev['security_violations'])} security violations caught: {ev['security_violations'][:2]}",
                  "suggestion": "No action — the gate worked. Listed so the owner sees what was refused.", "auto_actionable": None})
    return P


def markdown(ev: dict, P: list[dict]) -> str:
    out = [f"# Factory self-review — {datetime.date.today()} (last {ev['days']} days)", "",
           f"tests run: {ev['tests_run']} · failures by class: {ev['fails']} · repairs ok {ev['repairs']['ok']}/{ev['repairs']['total']} · bots {ev['bots']['active']}/{ev['bots']['total']} active", ""]
    if not P: out.append("No proposals — nothing recurring in the evidence.")
    for i, p in enumerate(P, 1):
        out += [f"## {i}. [{p['severity']}] {p['kind']}", f"**Evidence:** {p['evidence']}", "", f"**Proposal:** {p['suggestion']}", "",
                f"**Auto action:** {'enqueued ' + p['auto_actionable']['kind'] if p['auto_actionable'] else 'none — needs review'}", ""]
    out += ["---", "Generated by tools/factory_insight.py. Proposals are never applied to factory code automatically (D-057)."]
    return "\n".join(out) + "\n"


def run(days: int = 7, write: bool = True) -> dict:
    ev = gather(days); P = propose(ev)
    paths = {}
    if write:
        d = ROOT / "proposals"; d.mkdir(exist_ok=True)
        stem = datetime.date.today().isoformat()
        (d / f"{stem}.md").write_text(markdown(ev, P), encoding="utf-8")
        (d / f"{stem}.json").write_text(json.dumps({"evidence": ev, "proposals": P}, indent=1), encoding="utf-8")
        paths = {"md": str(d / f"{stem}.md"), "json": str(d / f"{stem}.json")}
    return {"evidence": ev, "proposals": P, "paths": paths}


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    out = run(int(opt("--days", 7)), "--write" in a)
    print(markdown(out["evidence"], out["proposals"]))
