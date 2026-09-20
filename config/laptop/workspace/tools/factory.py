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
    sys.stdout.write(r.stdout[-6000:]); sys.stderr.write(r.stderr[-1500:])
    return r.returncode

if __name__ == "__main__": sys.exit(main(sys.argv))
