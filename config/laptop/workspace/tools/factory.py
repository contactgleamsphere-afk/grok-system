"""Bot-factory entry point for MASTER 001 (lives inside the master's workspace so `exec` may run it).

    python tools/factory.py create "<plain-English objective>"
    python tools/factory.py test <bot_id>
    python tools/factory.py list

It only forwards to the repo pipeline (C:\\AI\\Factory\\repo\\tools\\factory_pipeline.py) with the repo root set.
All policy (permissions, chain, escape test, id allocation, status) is enforced there, not here.
"""
import os, subprocess, sys, json, pathlib
REPO = pathlib.Path(os.environ.get("AIFACTORY_REPO", r"C:\AI\Factory\repo"))
PIPE = REPO / "tools" / "factory_pipeline.py"

def main(a):
    if len(a) < 2: print(__doc__); return 2
    env = {**os.environ, "AIFACTORY_REPO": str(REPO), "PYTHONIOENCODING": "utf-8"}
    if a[1] == "list":
        b = json.loads((REPO / "registry" / "bots.json").read_text(encoding="utf-8"))
        for k, v in sorted(b.items()): print(f"{k} {v['name']:20s} {v['status']:9s} {v['verified']:10s} tools={','.join(v['tools'])}")
        return 0
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
