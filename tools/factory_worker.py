"""Factory worker: drains the persistent job queue (create / test / repair / monitor) with leases + audit.

  python tools/factory_worker.py run   [--once] [--worker NAME] [--idle-exit 30]
  python tools/factory_worker.py add create "<objective>" [--priority 3]
  python tools/factory_worker.py add plan "<multi-part objective>" [--max 4]     # D-053: decompose -> N creates
  python tools/factory_worker.py add test|repair|rearchitect <bot_id>
  python tools/factory_worker.py add monitor
  python tools/factory_worker.py add bench [--lanes a,b] [--stale-only] [--max N]   # D-050 lane quality
  python tools/factory_worker.py status | jobs | resume <job_id> | cancel <job_id> | release <job_id> [--uncount] | audit [bot_id] [--width N]

Autonomous loop (capability 1): a `create` job that ends VERIFIED enqueues nothing more (monitor covers it);
a `monitor` job enqueues a `repair` job for every bot it demoted; a `repair` that fails pauses with a class
(security/logic → human) or retries with backoff (quota/transient/model → other lane via the chain).
Security (capability 6): every create/repair result is checked with guard.assert_no_silent_expansion against the
pre-job spec; a violation pauses the job and audits it — it never reaches the registry.
"""
from __future__ import annotations
import json, os, sys, time, socket, pathlib, datetime, traceback
ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core")); sys.path.insert(0, str(ROOT / "tools"))
from factory.jobs import JobStore                                     # noqa: E402
from factory.guard import assert_no_silent_expansion, diff_boundaries, SecurityViolation  # noqa: E402
from factory.registry import Registry                                 # noqa: E402
from factory.factory import FactoryError                              # noqa: E402
import factory_pipeline as fp                                          # noqa: E402
import factory_repair as fr                                            # noqa: E402
import factory_monitor as fm                                           # noqa: E402
import factory_probe as fpr                                            # noqa: E402
import factory_report as frp                                           # noqa: E402
import factory_discover as fdc                                         # noqa: E402
import factory_bench as fbn
import factory_plan as fpl

DB = ROOT / "run" / "jobs.sqlite3"
LEASE = 300          # D-043: short lease + heartbeat every 60 s -> a dead worker is detected within 5 min


def _spec_of(bot_id: str) -> dict | None:
    reg = Registry(ROOT / "registry"); e = reg.get("bots", bot_id)
    if not e: return None
    p = ROOT / "specs" / f"{e.id}-{e.name}.json"
    d = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"permissions": e.permissions, "tools": e.tools, "model_policy": e.model_policy}
    patch = ROOT / "bots" / f"{e.id}-{e.name}" / "nanobot.patch.json"
    if not patch.exists() and fp.WIN: patch = fp.LAPTOP_BOTS / f"{e.id}-{e.name}" / "nanobot.patch.json"
    if patch.exists(): d["env"] = json.loads(patch.read_text(encoding="utf-8")).get("env", {})
    return d


def handle(job: dict, store: JobStore, worker: str) -> dict:
    kind, p = job["kind"], job["payload"]; jid = job["id"]
    if kind == "plan":
        # D-053: objective -> 1..N single-purpose bot objectives -> one create job each (same allowance, chained parent)
        res = fpl.plan(p["objective"], int(p.get("max", fpl.MAX_STEPS)))
        queued = []
        for i, st in enumerate(res["steps"], 1):
            if st.get("reuse"):
                store.audit("plan.reused", job_id=jid, actor=worker, step=i, bot_id=st["reuse"]["id"], similarity=st["reuse"]["similarity"]); continue
            j = store.enqueue("create", {"objective": st["objective"], "plan": jid, "step": i, "produces": st.get("produces", []),
                                         "allowed_permissions": p.get("allowed_permissions", ["fs:read", "fs:write", "net:search", "net:fetch"])},
                              priority=int(p.get("priority", 5)), parent=jid, actor=worker)
            queued.append((i, j["id"][:8]))
        store.audit("plan.made", job_id=jid, actor=worker, lane=res["lane"], steps=len(res["steps"]), queued=queued, rationale=res.get("rationale", "")[:200])
        return {"name": f"plan:{len(res['steps'])} steps", "status": "queued " + ",".join(q[1] for q in queued), "lane": res["lane"]}
    if kind == "create":
        # D-054: allowance is enforced INSIDE cmd_create before any file is written (post-hoc check let bot 015 be built)
        res = fp.cmd_create(p["objective"], p.get("id"), False, False, p.get("allowed_permissions", fp.DEFAULT_ALLOWANCE))
        spec = res["spec"]
        store.audit("bot.created", job_id=jid, bot_id=res["bot_id"], actor=worker, name=res["name"], tools=spec["tools"],
                    permissions=spec["permissions"], chain=res.get("chain"), lane=res.get("spec_lane"))
        store.audit("bot.tested", job_id=jid, bot_id=res["bot_id"], actor=worker, result=res.get("tests"), status=res.get("status"))
        if res.get("status") != "active":
            # D-036: a fresh bot that misses on first run gets exactly one automatic re-test (flaky lanes / timeouts);
            # if the re-test also fails the test handler escalates to repair, which fails closed.
            store.enqueue("test", {"bot_id": res["bot_id"], "retest_of": jid}, priority=3, parent=jid, actor=worker)
        return res
    if kind == "test":
        before = _spec_of(p["bot_id"]); res = fp.cmd_test(p["bot_id"])
        store.audit("bot.tested", job_id=jid, bot_id=p["bot_id"], actor=worker, result=res["tests"], status=res["status"],
                    inconclusive=bool(res.get("inconclusive")), quota=res.get("quota", 0))
        if res.get("inconclusive"):     # D-051: lanes were rate-limited, not the bot's fault -> same test again in 2h, no repair
            store.enqueue("test", {"bot_id": p["bot_id"], "retest_of": p.get("retest_of") or jid, "after_quota": jid},
                          priority=3, parent=jid, actor=worker, not_before=time.time() + 7200)
            return res
        if res["status"] != "active" and p.get("retest_of"):
            store.enqueue("repair", {"bot_id": p["bot_id"], "max_rounds": 2, "rearchitected": bool(p.get("rearchitected"))}, priority=2, parent=jid, actor=worker)
        return res
    if kind == "repair":
        before = _spec_of(p["bot_id"])
        if before is None: raise FactoryError(f"unknown bot {p['bot_id']}")
        res = fr.repair(p["bot_id"], p.get("max_rounds", 2))
        after = _spec_of(p["bot_id"])
        d = assert_no_silent_expansion(before, after, context=f"repair {p['bot_id']}")   # raises -> security pause
        store.audit("bot.repair", job_id=jid, bot_id=p["bot_id"], actor=worker, ok=res.get("ok"), status=res.get("status"),
                    rounds=[{k: r.get(k) for k in ("round", "lane", "sandbox", "rejected")} for r in res.get("rounds", [])],
                    boundary_diff=d)
        if res.get("ok"):
            store.audit("bot.promoted", job_id=jid, bot_id=p["bot_id"], actor=worker, to="active")
        else:
            err = res.get("error") or "repair produced no passing candidate"
            if err.startswith("logic: spec/tests inconsistent") and not p.get("rearchitected"):
                # D-052: instructions can't fix it -> one automatic re-architect from the original objective
                store.enqueue("rearchitect", {"bot_id": p["bot_id"], "feedback": err[:400], "from_repair": jid}, priority=2, parent=jid, actor=worker)
                store.audit("bot.rearchitect_queued", job_id=jid, bot_id=p["bot_id"], actor=worker, reason=err[:200])
            raise FactoryError(err)
        return res
    if kind == "rearchitect":
        before = _spec_of(p["bot_id"])
        if before is None: raise FactoryError(f"unknown bot {p['bot_id']}")
        allowance = p.get("allowed_permissions", ["fs:read", "fs:write", "net:search", "net:fetch"])
        res = fp.cmd_rearchitect(p["bot_id"], p.get("feedback", ""), allowance)
        if not res.get("ok"): raise FactoryError(res.get("error"))
        after = _spec_of(p["bot_id"])
        # D-052: NOT silent — the diff is audited and bounded by the job allowance; shell/net beyond allowance is impossible
        d = diff_boundaries(before, after)
        store.audit("bot.rearchitected", job_id=jid, bot_id=p["bot_id"], actor=worker, lane=res.get("spec_lane"), tools=res["spec"]["tools"],
                    permissions=res["spec"]["permissions"], boundary_diff=d, result=res.get("tests"), status=res.get("status"))
        if res.get("status") == "active":
            store.audit("bot.promoted", job_id=jid, bot_id=p["bot_id"], actor=worker, to="active")
            # a paused repair for this bot is now moot: clear it so "needs attention" stays truthful
            for j in store.list():
                if j["state"] == "paused" and j["kind"] == "repair" and j["payload"].get("bot_id") == p["bot_id"]:
                    store.cancel(j["id"], actor=worker); store.audit("job.superseded", job_id=j["id"], bot_id=p["bot_id"], actor=worker, by=jid)
        else:
            # one re-test like a fresh create; the test handler escalates to repair (flagged so repair->rearchitect can't loop)
            store.enqueue("test", {"bot_id": p["bot_id"], "retest_of": jid, "rearchitected": True}, priority=3, parent=jid, actor=worker)
        return {k: res.get(k) for k in ("bot_id", "spec_lane", "pass", "total", "status", "boundary_diff")}
    if kind == "probe":
        res = fpr.run(set(p["only"]) if p.get("only") else None)
        for r in res["changed"]:
            store.audit("model.health", job_id=jid, actor=worker, model=r["id"], outcome=r["outcome"],
                        before=r["before"], after=r["after"], detail=r.get("detail"))
        if res["changed"]: _sync_presets()          # BLOCKED lanes leave nanobot config immediately
        if not res["healthy"] and not p.get("only"):
            raise RuntimeError("transient: probe found no healthy remote lane")
        # D-047: a lane went BLOCKED, or the healthy remote pool is thin -> discover replacements (dedup by day)
        remote_ok = [r for r in res["rows"] if r.get("outcome") == "ok" and r["id"] not in ("local3b", "local4b")]
        newly_blocked = [c for c in res["changed"] if c["after"] == "BLOCKED"]
        if not p.get("only") and (newly_blocked or len(remote_ok) < fdc.MIN_HEALTHY):
            store.enqueue("discover", {"provider": "openrouter", "day": datetime.date.today().isoformat(),
                                       "trigger": "blocked:" + ",".join(c["id"] for c in newly_blocked) if newly_blocked else f"healthy={len(remote_ok)}"},
                          priority=2, parent=jid, actor=worker)
        nxt = (datetime.datetime.now() + datetime.timedelta(hours=1))
        if not p.get("only"): store.enqueue("probe", {"only": [], "hour": nxt.strftime("%Y-%m-%dT%H")}, priority=1, parent=jid, actor=worker,
                      not_before=time.time() + 3600)
        return {"probed": res["probed"], "healthy": res["healthy"], "changed": [(c["id"], c["after"]) for c in res["changed"]]}
    if kind == "discover":
        res = fdc.run(p.get("provider", "openrouter"), int(p.get("max", 2)))
        for v in res.get("verdicts", []):
            if v["verdict"] in ("approved", "rejected"):
                store.audit("lane.discovered" if v["verdict"] == "approved" else "lane.rejected", job_id=jid, actor=worker,
                            model=v["model"], reason=v["reason"], provider=res.get("provider"))
        if res.get("added"):
            store.audit("config.presets", job_id=jid, actor=worker, added=res["added"])
            _sync_presets()
            store.enqueue("bench", {"lanes": res["added"], "day": datetime.date.today().isoformat()}, priority=4, parent=jid, actor=worker)
        return {k: res.get(k) for k in ("skipped", "healthy_before", "catalog", "evaluated", "added")}
    if kind == "bench":
        # D-050: pinned single-lane quality score on the reference suite; ranks default_fallbacks()
        res = fbn.run(p.get("lanes") or None, p.get("ref", fbn.REF_BOT), bool(p.get("stale_only")), int(p.get("max", 3)))
        for r in res["results"]:
            store.audit("lane.benchmarked", job_id=jid, actor=worker, lane=r["lane"], result=f"{r['pass']}/{r['total']}", quota=r.get("quota", 0), secs=r["secs"])
        for r in res["errors"]:
            store.audit("lane.bench_error", job_id=jid, actor=worker, lane=r["lane"], error=r["error"])
        return {"benchmarked": [(r["lane"], f"{r['pass']}/{r['total']}" + (f" q{r['quota']}" if r.get("quota") else "")) for r in res["results"]], "errors": res["errors"], "rank": res["rank"][:8]}
    if kind == "report":
        r = frp.build(); (ROOT / "STATUS.md").write_text(frp.markdown(r), encoding="utf-8")
        nxt = datetime.datetime.now() + datetime.timedelta(days=1)
        store.enqueue("report", {"day": nxt.strftime("%Y-%m-%d")}, priority=6, parent=jid, actor=worker, not_before=time.time() + 86400)
        store.enqueue("bench", {"stale_only": True, "max": 2, "day": datetime.date.today().isoformat()}, priority=7, parent=jid, actor=worker)
        return {"bots_active": r["bots"]["active"], "attention": r["attention"][:10], "healthy_lanes": r["healthy_lanes"]}
    if kind == "monitor":
        # D-035 pre-flight: a bloated config makes every test fail for the wrong reason — refuse to demote on it
        cfg_path = pathlib.Path(r"C:\AI\Factory\config.json")
        if cfg_path.exists():
            from factory.guard import config_hygiene
            probs = config_hygiene(json.loads(cfg_path.read_bytes().decode("utf-8")), cfg_path.stat().st_size)
            if probs:
                store.audit("config.unhealthy", job_id=jid, actor=worker, problems=probs)
                raise RuntimeError("logic: config.json unhealthy, monitor aborted before demoting anyone: " + "; ".join(probs))
        res = fm.monitor(set(p["only"]) if p.get("only") else None)
        for r in res["rows"]:
            store.audit("bot.monitored", job_id=jid, bot_id=r["id"], actor=worker, result=f"{r['pass']}/{r['total']}", before=r["before"], after=r["after"],
                        inconclusive=bool(r.get("inconclusive")), quota=r.get("quota", 0))
            if r.get("inconclusive"):
                continue
            if r["after"] != "active":
                store.audit("bot.demoted", job_id=jid, bot_id=r["id"], actor=worker, to=r["after"])
                store.enqueue("repair", {"bot_id": r["id"], "max_rounds": 2}, priority=2, parent=jid, actor=worker)
        if res.get("inconclusive"):
            store.enqueue("monitor", {"only": res["inconclusive"], "day": datetime.date.today().isoformat(), "retry_of": jid},
                          priority=3, parent=jid, actor=worker, not_before=time.time() + 7200)
        return res
    raise FactoryError(f"unknown job kind {kind}")


CODE_FILES = [pathlib.Path(__file__), *sorted((ROOT / "core" / "factory").glob("*.py")), *sorted((ROOT / "tools").glob("factory_*.py"))]


def _code_stamp() -> float:
    return max((f.stat().st_mtime for f in CODE_FILES if f.exists()), default=0.0)


def _sync_presets() -> None:
    """D-048: nanobot modelPresets mirror the registry for every non-BLOCKED remote model (config.json is the runtime)."""
    import factory_presets
    try: factory_presets.sync()
    except Exception as e: JobStore(DB).audit("config.presets_error", actor="worker", error=str(e)[:200])


STATE_PATHS = ["registry", "specs", "AUDIT.md", "MONITOR.md", "BOT_REGISTRY.md", "STATUS.md"]


def _commit_state(kind: str, jid8: str) -> None:
    """D-041: factory state (registry, specs, audit) is committed to git after every job so it can never be lost by a
    sync/reset. Local commit only; the push is done by the sync script (network may be down). Never raises."""
    import subprocess
    try:
        env = {**os.environ, "GIT_TERMINAL_PROMPT": "0", "GCM_INTERACTIVE": "Never", "GIT_ASKPASS": "echo"}
        g = lambda *a: subprocess.run(["git", *a], cwd=str(ROOT), capture_output=True, text=True, timeout=60, env=env)
        g("add", "-A", "--", *STATE_PATHS)
        if g("diff", "--cached", "--quiet").returncode != 0:
            g("-c", "user.name=AI Factory Worker", "-c", "user.email=contactgleamsphere-afk+worker@users.noreply.github.com",
              "commit", "-q", "-m", f"state: after {kind} job {jid8}")
            tok = os.environ.get("GITHUB_TOKEN")
            if tok:   # push with the token in the URL and every credential helper disabled -> can never block on a GUI prompt
                url = f"https://x-access-token:{tok}@github.com/contactgleamsphere-afk/grok-system.git"
                nh = ["-c", "credential.helper=", "-c", "core.askPass=", "-c", "credential.interactive=never"]
                g(*nh, "fetch", "-q", url, "main"); g("rebase", "-q", "FETCH_HEAD"); g(*nh, "push", "-q", url, "HEAD:main")
    except Exception:
        pass


def run(worker: str, once: bool = False, idle_exit: int = 0) -> int:
    store = JobStore(DB); idle_since = time.time(); processed = 0; stamp = _code_stamp()
    while True:
        # D-039: a long-lived worker must never run stale code — exit between jobs when any factory module changed;
        # the supervisor loop (run-worker.ps1) relaunches it with fresh modules.
        if _code_stamp() != stamp:
            store.audit("worker.restart", actor=worker, reason="code changed on disk"); return processed
        job = store.claim(worker, LEASE)
        if not job:
            if once or (idle_exit and time.time() - idle_since > idle_exit): break
            time.sleep(5); continue
        idle_since = time.time(); processed += 1
        import threading
        stop = threading.Event()

        def _beat():
            hb = JobStore(DB)                      # own connection: sqlite objects are not thread-safe
            while not stop.wait(60):
                try: hb.heartbeat(job["id"], worker, LEASE)
                except Exception: pass
        threading.Thread(target=_beat, daemon=True).start()
        try:
            res = handle(job, store, worker)
            store.done(job["id"], res if isinstance(res, dict) else {"result": res}, worker)
        except SecurityViolation as e:
            store.audit("security.violation", job_id=job["id"], bot_id=job["payload"].get("bot_id"), actor=worker, error=str(e))
            store.fail(job["id"], f"security: {e}", worker)
        except Exception as e:
            store.fail(job["id"], f"{type(e).__name__}: {e}\n{traceback.format_exc()[-800:]}", worker)
        stop.set()
        store.audit_export(ROOT / "AUDIT.md")
        _commit_state(job["kind"], job["id"][:8])
        if once: break
    store.audit_export(ROOT / "AUDIT.md")
    return processed


def main(a: list[str]) -> int:
    if len(a) < 2: print(__doc__); return 2
    store = JobStore(DB); cmd = a[1]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    if cmd == "run":
        n = run(opt("--worker", f"{socket.gethostname()}-{os.getpid()}"), "--once" in a, int(opt("--idle-exit", 0)))
        print(json.dumps({"processed": n, "queue": store.summary()})); return 0
    if cmd == "add":
        kind = a[2]
        if kind == "create":
            pl = {"objective": a[3]}
            if opt("--allow"): pl["allowed_permissions"] = opt("--allow").split(",")     # D-054: explicit owner grant (recorded in the job + audit)
            j = store.enqueue("create", pl, priority=int(opt("--priority", 5)), actor=opt("--actor", "owner"))
        elif kind == "plan": j = store.enqueue("plan", {"objective": a[3], "max": int(opt("--max", 4))}, priority=int(opt("--priority", 5)), actor=opt("--actor", "owner"))
        elif kind == "rearchitect": j = store.enqueue("rearchitect", {"bot_id": a[3], "feedback": opt("--feedback", ""), "t": int(time.time())}, priority=2, actor=opt("--actor", "owner"))
        elif kind in ("test", "repair"): j = store.enqueue(kind, {"bot_id": a[3]}, priority=int(opt("--priority", 4)), actor=opt("--actor", "owner"))
        elif kind == "probe":
            only = [x for x in opt("--only", "").split(",") if x]
            j = store.enqueue("probe", {"only": only, "hour": datetime.datetime.now().strftime("%Y-%m-%dT%H")}, priority=1, actor=opt("--actor", "owner"))
        elif kind == "discover":
            j = store.enqueue("discover", {"provider": opt("--provider", "openrouter"), "day": str(datetime.date.today()), "trigger": "manual"}, priority=2, actor=opt("--actor", "owner"))
        elif kind == "bench":
            lanes = [x for x in opt("--lanes", "").split(",") if x]
            j = store.enqueue("bench", {"lanes": lanes, "stale_only": "--stale-only" in a, "max": int(opt("--max", 3)), "day": str(datetime.date.today()), "t": int(time.time())}, priority=4, actor=opt("--actor", "owner"))
        elif kind == "report":
            j = store.enqueue("report", {"day": str(datetime.date.today())}, priority=6, actor=opt("--actor", "owner"))
        elif kind == "monitor":
            only = [x.strip().zfill(3) for x in str(opt("--only", "")).split(",") if x.strip()] or None   # zfill: shells turn 002 into 2
            j = store.enqueue("monitor", {"only": only, "day": str(datetime.date.today())}, priority=3, actor=opt("--actor", "owner"))
        else: print(__doc__); return 2
        print(json.dumps({"job_id": j["id"], "state": j["state"], "kind": j["kind"]})); return 0
    if cmd == "status": print(json.dumps(store.summary())); return 0
    if cmd == "jobs":
        for j in store.list(): print(f"{j['id'][:8]} {j['kind']:8s} {j['state']:9s} att={j['attempts']} cls={j['failure_class'] or '-':9s} {json.dumps(j['payload'])[:70]}")
        return 0
    if cmd == "resume":
        ids = [j["id"] for j in store.list(["paused", "failed"])] if (len(a) < 3 or a[2] == "--all") else [store.resolve(a[2])]
        for i in ids: store.resume(i)
        print(json.dumps({"resumed": [i[:8] for i in ids]})); return 0
    if cmd == "cancel": print(json.dumps(store.cancel(store.resolve(a[2]))["state"])); return 0
    if cmd == "release": print(json.dumps(store.release(store.resolve(a[2]), uncount="--uncount" in a)["state"])); return 0
    if cmd == "audit":
        for r in reversed(store.audit_rows(40, a[2] if len(a) > 2 else None)):
            print(f"{datetime.datetime.fromtimestamp(r['ts']):%H:%M:%S} {r['event']:20s} job={str(r['job_id'])[:8]} bot={r['bot_id'] or '-'} {r['detail'][:int(opt('--width', 110))]}")
        return 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
