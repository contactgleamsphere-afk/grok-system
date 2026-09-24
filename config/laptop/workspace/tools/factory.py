"""Bot-factory entry point for MASTER 001 (lives inside the master's workspace so `exec` may run it).

    python tools/factory.py create "<plain-English objective>"   # synchronous (blocks ~2-5 min)
    python tools/factory.py queue create "<objective>" | test <id> | repair <id> | monitor [ids]   # async via job queue
    python tools/factory.py tools | queue tooldisc "<need>"                                     # D-114: tool catalogue / MCP discovery
    python tools/factory.py queue plan "<multi-stage objective>"   # planner -> one create per stage
    python tools/factory.py queue probe | discover | bench        # model-lane health / new free lanes / quality scores
    python tools/factory.py jobs | audit [bot_id] | report | lanes
    python tools/factory.py schedule add <bot_id> "<5-field cron>" --task "..." [--in <inbox name>]   # D-076 recurring work
    python tools/factory.py schedule list | remove <sid> | enable <sid> | disable <sid>
    python tools/factory.py approve <job_id> --allow fs:read,fs:write,shell:workspace   # D-070 owner grants a paused job's permission request
    python tools/factory.py test <bot_id>
    python tools/factory.py list

It only forwards to the repo pipeline (C:\\AI\\Factory\\repo\\tools\\factory_pipeline.py) with the repo root set.
All policy (permissions, chain, escape test, id allocation, status) is enforced there, not here.
"""
import os, re, subprocess, sys, json, pathlib
REPO = pathlib.Path(os.environ.get("AIFACTORY_REPO", r"C:\AI\Factory\repo"))
PIPE = REPO / "tools" / "factory_pipeline.py"

def main(a):
    if len(a) < 2: print(__doc__); return 2
    env = {**os.environ, "AIFACTORY_REPO": str(REPO), "PYTHONIOENCODING": "utf-8"}
    if a[1] == "list":
        b = json.loads((REPO / "registry" / "bots.json").read_text(encoding="utf-8"))
        for k, v in sorted(b.items()): print(f"{k} {v['name']:20s} {v['status']:9s} {v['verified']:10s} tools={','.join(v['tools'])}")
        return 0
    if a[1] == "tools":
        # D-114: tool catalogue for the owner — builtins + discovered MCP servers with their state. Read-only; approval is CLI-only.
        t = json.loads((REPO / "registry" / "tools.json").read_text(encoding="utf-8"))
        print("TOOLS id kind risk state")
        for k, v in sorted(t.items()):
            state = v.get("verified", "?")
            if v.get("kind") == "mcp":
                try: n = json.loads(v.get("notes") or "{}")
                except Exception: n = {}
                state = "APPROVED" if n.get("install") and "PROBATION" not in (v.get("scope") or "") else "PROBATION (owner: approve-tool on the laptop)"
                state += f" tools={len(n.get('tools') or [])} licence={n.get('licence')}"
            print(f"{k} {v.get('kind')} {v.get('risk')} {state}")
        return 0
    if a[1] == "lanes":
        # model lanes: health + benchmark rank (D-050). Compact: the master runs on small-context lanes.
        m = json.loads((REPO / "registry" / "models.json").read_text(encoding="utf-8"))
        rows = []
        for k, v in m.items():
            if v.get("location") != "remote": continue
            h = (v.get("limits") or {}).get("health") or {}; b = (v.get("limits") or {}).get("bench") or {}
            rows.append((k, v["verified"], "ok" if h.get("ok", True) else h.get("last_outcome", "?"), f"{b['pass']}/{b['total']}" if b.get("total") else "-", b.get("secs")))
        rows.sort(key=lambda r: (r[1] == "BLOCKED", -(int(r[3].split("/")[0]) / int(r[3].split("/")[1])) if r[3] != "-" else 1))
        print("LANES lane verified health bench secs")
        for r in rows: print(" ".join(str(x) for x in r))
        return 0
    if a[1] == "job":
        # D-064: one job's outcome for the owner: state, class, error, and what it produced (bots / files) — compact
        import sqlite3
        c = sqlite3.connect(str(REPO / "run" / "jobs.sqlite3")); pre = a[2]
        row = c.execute("SELECT id,kind,state,failure_class,error,payload FROM jobs WHERE id LIKE ?", (pre + "%",)).fetchone()
        if not row: print(f"no job starting with {pre}"); return 1
        jid, kind, state, cls, err, payload = row; pl = json.loads(payload)
        print(f"JOB {jid[:8]} {kind} {state}" + (f" class={cls}" if cls else "") + (f" error={err[:200]}" if err else ""))
        if state == "paused" and cls == "security" and "allowance" in (err or ""):
            m = re.search(r"needs? (?:permissions? )?(?:outside the allowance \[[^\]]*\]: )?(.{0,160})", err or "")
            print(f"  NEEDS OWNER DECISION: permission outside allowance {pl.get('allowed_permissions')}: {m.group(1) if m else err[:160]}")
            print(f"  if the owner says yes: python tools/factory.py approve {jid[:8]} --allow <comma-separated perms>")
        ev = c.execute("SELECT event,bot_id,detail FROM audit WHERE job_id=? ORDER BY seq", (jid,)).fetchall()
        for e, b, d in ev:
            if e in ("bot.created", "bot.tested", "bot.promoted", "bot.demoted", "bot.ran", "plan.made", "plan.reused", "security.violation", "bot.rearchitected", "bot.repair"):
                dd = json.loads(d or "{}"); short = {k: dd[k] for k in ("name", "status", "result", "produced", "reply", "steps", "queued", "error", "ok") if k in dd}
                print(f"  {e} {b or ''} {json.dumps(short)[:220]}")
        kids = c.execute("SELECT id,kind,state,payload FROM jobs WHERE parent=? ORDER BY created", (jid,)).fetchall()
        for k, kk, ks, kp in kids: print(f"  child {k[:8]} {kk} {ks} {json.loads(kp).get('bot_id') or json.loads(kp).get('objective', '')[:50]}")
        return 0
    if a[1] == "runs":
        runs = pathlib.Path(r"C:\AI\Factory\run\runs")
        for d in sorted([d for d in runs.iterdir() if d.is_dir() and not d.name.startswith("_")], key=lambda d: d.stat().st_mtime)[-8:]:
            rj = d / "RUN.json"; ok = json.loads(rj.read_text(encoding="utf-8")).get("ok") if rj.exists() else None
            files = [f.relative_to(d).as_posix() for f in d.rglob("*") if f.is_file() and f.name != "RUN.json" and "_stage" not in f.parts]
            print(f"{d.name} ok={ok} files={','.join(files)[:150]}")
        return 0
    if a[1] == "report":
        r = subprocess.run([sys.executable, str(REPO / "tools" / "factory_report.py"), "--brief"], env=env, cwd=str(REPO), capture_output=True, text=True, timeout=120)
        print((r.stdout + r.stderr)[:1000]); return r.returncode
    if a[1] == "schedule":
        # D-076: recurring runs. Same inbox contract as `queue run` (names only, never outside paths).
        w = REPO / "tools" / "factory_schedule.py"; rest = list(a[2:])
        if "--in" in rest:
            i = rest.index("--in"); name = pathlib.Path(rest[i + 1]).name
            inbox = pathlib.Path(__file__).resolve().parents[1] / "inbox" / name
            if not inbox.is_dir(): print(f"inbox folder '{name}' not found under workspace/inbox"); return 1
            rest[i + 1] = str(inbox)
        r = subprocess.run([sys.executable, str(w), *rest, *(["--actor", "master-001"] if rest and rest[0] == "add" else [])], env=env, cwd=str(REPO), capture_output=True, text=True, timeout=120)
        print((r.stdout + r.stderr)[-900:]); return r.returncode
    if a[1] == "approve":
        # D-070: the only way a paused (security) job gets more permission is an explicit owner grant relayed here.
        # shell:system / net:* beyond allowance are refused by the worker; the grant + resume are audited.
        if len(a) < 5 or a[3] != "--allow": print("usage: approve <job_id> --allow perm1,perm2"); return 2
        w = REPO / "tools" / "factory_worker.py"
        r = subprocess.run([sys.executable, str(w), "resume", a[2], "--allow", a[4], "--actor", "owner-via-master"], env=env, cwd=str(REPO), capture_output=True, text=True, timeout=120)
        print((r.stdout + r.stderr)[-600:]); return r.returncode
    if a[1] in ("queue", "jobs", "audit"):
        w = REPO / "tools" / "factory_worker.py"
        if a[1] == "queue":
            kind = a[2]; rest = a[3:]
            argv = [sys.executable, str(w), "add", kind, *rest, "--actor", "master-001"]
            for flag in ("--in", "--then-run"):
                if kind in ("run", "plan", "create") and flag in rest:
                    # D-064: the master only ever names an inbox folder (its own workspace, never an outside path — the exec
                    # guard rightly refuses those). inbox/<name> -> absolute path for the worker.
                    i = rest.index(flag); name = pathlib.Path(rest[i + 1]).name
                    inbox = pathlib.Path(__file__).resolve().parents[1] / "inbox" / name
                    if not inbox.is_dir(): print(f"inbox folder '{name}' not found under workspace/inbox; available: {[d.name for d in (inbox.parent).glob('*') if d.is_dir()] if inbox.parent.exists() else []}"); return 1
                    argv[argv.index(flag) + 1] = str(inbox)
            if kind == "monitor" and rest: argv = [sys.executable, str(w), "add", "monitor", "--only", rest[0], "--actor", "master-001"]
        else:
            argv = [sys.executable, str(w), a[1], *a[2:]]
        r = subprocess.run(argv, env=env, cwd=str(REPO), capture_output=True, text=True, timeout=120)
        print((r.stdout + r.stderr)[-900:]); return r.returncode
    missing = [k for k in ("GROQ_API_KEY", "GEMINI_API_KEY", "OPENROUTER_API_KEY") if not env.get(k)]
    if missing: print(json.dumps({"ok": False, "error": f"lane keys not visible to exec: {missing} (config tools.exec.allowedEnvKeys)"})); return 1
    r = subprocess.run([sys.executable, str(PIPE), *a[1:]], env=env, cwd=str(REPO), capture_output=True, text=True, timeout=3600)
    # Compact summary only: the master runs on small-context lanes (8k). Full JSON is kept on disk.
    log = REPO / "run"; log.mkdir(exist_ok=True)
    (log / f"factory-{a[1]}-{(a[2] if len(a) > 2 else 'x')[:20].replace(' ', '_')}.json").write_text(r.stdout + r.stderr, encoding="utf-8")
    try:
        d = json.loads(r.stdout[r.stdout.rfind("{\n \"bot_id\"") if "{\n \"bot_id\"" in r.stdout else r.stdout.rfind("{"):])
        keys = ("ok", "bot_id", "name", "spec_lane", "chain", "files", "tests", "pass", "total", "status", "verified", "error")
        out = {k: d[k] for k in keys if k in d}
        if "spec" in d: out["tools"] = d["spec"].get("tools"); out["permissions"] = d["spec"].get("permissions")
        print(json.dumps(out)[:900])
    except Exception:
        print((r.stdout + r.stderr)[-700:])
    return r.returncode

if __name__ == "__main__": sys.exit(main(sys.argv))
