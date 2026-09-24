"""factory_tooldisc.py — D-108 tool/MCP capability discovery (DISCOVER → RESEARCH → EVALUATE → SANDBOX → PROBATION).

  python tools/factory_tooldisc.py <need> [--max 2] [--dry-run]      e.g. "sqlite", "filesystem", "web search"

Sources (all free, keyless): the official MCP registry (registry.modelcontextprotocol.io), PyPI JSON, the npm registry,
GitHub's public repo API. Rules are evidence-based, never popularity-only (owner contract): licence must be permissive,
a release within RECENT_DAYS, repo not archived, dependency count bounded, and the server must run LOCALLY over stdio —
hosted "remote" servers are rejected (data leaves the machine, lock-in). SANDBOX (laptop only): install into a throw-away
venv / npx cache with every API key stripped from the environment, speak MCP JSON-RPC over stdio (initialize →
tools/list), record the tool names. Anything that passes lands in registry/tools.json as kind=mcp on PROBATION with
verified=INFERRED; it is NOT attached to any bot — wiring an MCP server into a bot's config is a permission change and
needs the owner (SECURITY §6). Every verdict, including rejections, is written to registry/tool_candidates.json so the
same candidate is not re-evaluated for LEDGER_DAYS.
"""
from __future__ import annotations
import json, os, re, shutil, subprocess, sys, tempfile, time, pathlib, urllib.request, urllib.error

ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO") or pathlib.Path(__file__).resolve().parents[1])
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "core"))
from factory.registry import Registry, ToolEntry   # noqa: E402

MCP_REG = "https://registry.modelcontextprotocol.io/v0.1/servers"
PERMISSIVE = ("MIT", "APACHE", "BSD", "ISC", "MPL", "UNLICENSE", "0BSD", "CC0")
RECENT_DAYS = 365
MAX_DEPS = 40
LEDGER_DAYS = 14
LEDGER = ROOT / "registry" / "tool_candidates.json"
HIGH_RISK = re.compile(r"exec|shell|command|run_|write|delete|remove|sudo|kill|deploy", re.I)
WIN = os.name == "nt"


def _fetch(url: str, timeout: int = 20) -> dict | None:
    req = urllib.request.Request(url, headers={"User-Agent": "aifactory-tooldisc/1.0", "Accept": "application/json"})
    for attempt in (1, 2):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except Exception:
            if attempt == 1: time.sleep(2)
    return None


def _ledger() -> dict:
    try: return json.loads(LEDGER.read_text(encoding="utf-8"))
    except Exception: return {"verdicts": {}}


def _save_ledger(l: dict) -> None:
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    LEDGER.write_text(json.dumps(l, indent=1, sort_keys=True), encoding="utf-8")


# ---------- DISCOVER ----------
def discover(need: str, fetch=None, limit: int = 30) -> list[dict]:
    """Official MCP registry search → normalised candidates. Keeps only local stdio packages (pypi or npm)."""
    fetch = fetch or _fetch
    d = fetch(f"{MCP_REG}?search={urllib.request.quote(need)}&version=latest&limit={limit}") or {}
    out = []
    for s in d.get("servers", []):
        v = s.get("server", {}); meta = (s.get("_meta") or {}).get("io.modelcontextprotocol.registry/official", {})
        pk = None
        for p in v.get("packages", []) or []:
            if p.get("registryType") in ("pypi", "npm") and (p.get("transport") or {}).get("type", "stdio") == "stdio":
                pk = p; break
        out.append({"name": v.get("name"), "title": v.get("title") or v.get("name"), "version": v.get("version"),
                    "description": (v.get("description") or "")[:200], "repo": (v.get("repository") or {}).get("url"),
                    "package": pk, "remote_only": not pk and bool(v.get("remotes")),
                    "status": meta.get("status"), "updated": meta.get("updatedAt")})
    return out


# ---------- RESEARCH ----------
def research(c: dict, fetch=None) -> dict:
    """Facts from the package index and the repo. Every field may be None; evaluate() treats unknown as a finding."""
    fetch = fetch or _fetch
    f = {"licence": None, "released": None, "deps": None, "yanked": False, "archived": None, "stars": None, "pushed": None}
    pk = c.get("package") or {}
    if pk.get("registryType") == "pypi":
        d = fetch(f"https://pypi.org/pypi/{pk['identifier']}/json")
        if d:
            info = d.get("info", {}); rel = d.get("releases", {}).get(info.get("version"), [])
            lic = info.get("license") or ""
            cls = [x for x in info.get("classifiers", []) if x.startswith("License ::")]
            f["licence"] = (lic if len(lic) < 40 else "") or (cls[-1].split("::")[-1].strip() if cls else None) or (info.get("license_expression") or None)
            f["deps"] = len(info.get("requires_dist") or [])
            f["released"] = max((x.get("upload_time_iso_8601", "") for x in rel), default=None) or None
            f["yanked"] = any(x.get("yanked") for x in rel)
    elif pk.get("registryType") == "npm":
        d = fetch(f"https://registry.npmjs.org/{pk['identifier']}")
        if d:
            latest = (d.get("dist-tags") or {}).get("latest"); ver = (d.get("versions") or {}).get(latest, {})
            f["licence"] = d.get("license") if isinstance(d.get("license"), str) else (ver.get("license") if isinstance(ver.get("license"), str) else None)
            f["deps"] = len(ver.get("dependencies") or {})
            f["released"] = (d.get("time") or {}).get(latest)
    m = re.match(r"https?://github\.com/([^/]+)/([^/#?]+)", c.get("repo") or "")
    if m:
        d = fetch(f"https://api.github.com/repos/{m.group(1)}/{m.group(2).removesuffix('.git')}")
        if d and "full_name" in d:
            f["archived"] = bool(d.get("archived")); f["stars"] = d.get("stargazers_count"); f["pushed"] = d.get("pushed_at")
            f["licence"] = f["licence"] or ((d.get("license") or {}).get("spdx_id"))
    return f


# ---------- EVALUATE ----------
def _days_since(iso: str | None, now: float) -> float | None:
    if not iso: return None
    try:
        import datetime
        return (now - datetime.datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp()) / 86400
    except Exception:
        return None


def evaluate(c: dict, facts: dict, now: float | None = None) -> tuple[str, list[str]]:
    """'keep' or 'rejected' with reasons. Evidence rules; stars are recorded but never decide."""
    now = now or time.time(); why = []
    if c.get("remote_only"): why.append("remote-only (hosted; data leaves the machine, lock-in)")
    if not c.get("package"): why.append("no local stdio package (pypi/npm)")
    if c.get("status") not in (None, "active"): why.append(f"registry status {c.get('status')}")
    lic = (facts.get("licence") or "").upper()
    if not lic: why.append("licence unknown")
    elif not any(p in lic for p in PERMISSIVE): why.append(f"licence not permissive: {facts['licence']}")
    age = _days_since(facts.get("released"), now)
    if age is None: why.append("release date unknown")
    elif age > RECENT_DAYS: why.append(f"stale: last release {int(age)} days ago")
    if facts.get("yanked"): why.append("latest release yanked")
    if facts.get("archived"): why.append("repository archived")
    if facts.get("deps") is not None and facts["deps"] > MAX_DEPS: why.append(f"{facts['deps']} dependencies > {MAX_DEPS}")
    return ("keep" if not why else "rejected"), why


# ---------- SANDBOX (laptop) ----------
def _clean_env() -> dict:
    env = {k: v for k, v in os.environ.items() if not re.search(r"KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL", k, re.I)}
    env["PYTHONIOENCODING"] = "utf-8"; env["NO_COLOR"] = "1"
    return env


def _kill_tree(p: subprocess.Popen) -> None:
    try:
        if WIN: subprocess.run(["taskkill", "/PID", str(p.pid), "/T", "/F"], capture_output=True, timeout=30)
        else: p.kill()
    except Exception: pass


def mcp_handshake(cmd: list[str], cwd: str, env: dict, timeout: int = 60) -> dict:
    """Speak MCP over stdio: initialize → notifications/initialized → tools/list. Returns tool names or the failure.
    Reads stdout on a thread and kills the whole process tree on timeout (npx/uvx spawn the real server as a grandchild
    that keeps the pipe open — a plain subprocess.run(timeout=) hangs forever there; seen live 2026-09-24)."""
    import threading
    msgs = [{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18", "capabilities": {},
                                                                          "clientInfo": {"name": "aifactory-sandbox", "version": "1"}}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}]
    try:
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, env=env,
                             text=True, encoding="utf-8", errors="replace", bufsize=1)
    except Exception as e:
        return {"ok": False, "reason": f"spawn failed: {e!r}"[:200]}
    got: dict = {}; lines: list[str] = []; done = threading.Event()

    def reader():
        try:
            for line in p.stdout:
                line = line.strip(); lines.append(line[:300])
                if not line.startswith("{"): continue
                try: m = json.loads(line)
                except Exception: continue
                if m.get("id") in (1, 2): got[m["id"]] = m
                if 2 in got: break
        finally:
            done.set()
    threading.Thread(target=reader, daemon=True).start()
    try:
        for m in msgs:
            p.stdin.write(json.dumps(m) + "\n"); p.stdin.flush()
            if m.get("id") == 1:                       # give the server a moment to answer initialize before the rest
                t_end = time.time() + timeout
                while 1 not in got and time.time() < t_end and not done.is_set(): time.sleep(0.2)
        t_end = time.time() + timeout
        while 2 not in got and time.time() < t_end and not done.is_set(): time.sleep(0.2)
    except Exception as e:
        got.setdefault("err", repr(e)[:120])
    finally:
        _kill_tree(p)
        try: err = p.stderr.read()[-300:] if p.stderr else ""
        except Exception: err = ""
    if 2 not in got:
        return {"ok": False, "reason": ("no tools/list result" if 1 in got else f"no initialize result in {timeout}s"),
                "stderr": err, "stdout_tail": lines[-3:]}
    server = ((got[1].get("result") or {}).get("serverInfo") or {}).get("name") if 1 in got else None
    tools = [t.get("name") for t in ((got[2].get("result") or {}).get("tools") or [])]
    return {"ok": True, "server": server, "tools": tools}


def sandbox(c: dict, timeout: int = 180) -> dict:
    """Throw-away install + handshake with secrets stripped. Laptop only (needs pip/npx). Never touches the factory venv."""
    pk = c["package"]; tmp = tempfile.mkdtemp(prefix="aif-tool-")
    env = _clean_env(); t0 = time.time()
    try:
        if pk["registryType"] == "pypi":
            venv = pathlib.Path(tmp) / "venv"
            subprocess.run([sys.executable, "-m", "venv", str(venv)], check=True, capture_output=True, timeout=120)
            py = venv / ("Scripts" if WIN else "bin") / ("python.exe" if WIN else "python")
            spec = pk["identifier"] + (f"=={pk['version']}" if pk.get("version") else "")
            r = subprocess.run([str(py), "-m", "pip", "install", "-q", "--no-cache-dir", "--disable-pip-version-check", spec],
                               capture_output=True, text=True, timeout=timeout, env=env)
            if r.returncode != 0: return {"ok": False, "stage": "install", "reason": r.stderr[-300:]}
            scripts = venv / ("Scripts" if WIN else "bin")
            names = [pk["identifier"], pk["identifier"].replace("_", "-"), pk["identifier"].replace("-", "_")]
            exe = next((p for n in names for p in scripts.glob(n + ("*.exe" if WIN else "")) if p.is_file()), None)
            cmd = [str(exe)] if exe else [str(py), "-m", pk["identifier"].replace("-", "_")]
        else:
            npx = shutil.which("npx.cmd") or shutil.which("npx")
            if not npx: return {"ok": False, "stage": "install", "reason": "npx not available"}
            env["npm_config_cache"] = str(pathlib.Path(tmp) / "npm"); env["NPM_CONFIG_CACHE"] = env["npm_config_cache"]
            spec = pk["identifier"] + (f"@{pk['version']}" if pk.get("version") else "")
            cmd = [npx, "-y", spec]
        cmd += [str(a.get("value") or a.get("default") or "") for a in (pk.get("packageArguments") or []) if a.get("type") == "positional" and (a.get("value") or a.get("default"))]
        hs = mcp_handshake(cmd, tmp, env, timeout=min(timeout, 120))
        hs["stage"] = "handshake"; hs["secs"] = int(time.time() - t0); hs["cmd"] = cmd[:3]
        return hs
    except subprocess.TimeoutExpired:
        return {"ok": False, "stage": "install", "reason": f"install exceeded {timeout}s"}
    except Exception as e:
        return {"ok": False, "stage": "sandbox", "reason": repr(e)[:200]}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ---------- PROBATION ----------
def tool_id(c: dict) -> str:
    return "mcp:" + re.sub(r"[^a-z0-9]+", "-", (c.get("name") or "").lower().split("/")[-1]).strip("-")[:40]


def integrate(reg: Registry, c: dict, facts: dict, hs: dict, need: str) -> ToolEntry:
    risky = [t for t in hs.get("tools", []) if HIGH_RISK.search(t or "")]
    e = ToolEntry(id=tool_id(c), kind="mcp", provides=[need] + (["write"] if risky else []),
                  risk="high" if risky else "medium", verified="INFERRED",
                  scope="PROBATION — not attached to any bot; owner approval required to wire into a bot config (SECURITY §6)",
                  notes=json.dumps({"registry_name": c["name"], "version": c.get("version"), "package": {k: c["package"].get(k) for k in ("registryType", "identifier", "version")},
                                    "repo": c.get("repo"), "licence": facts.get("licence"), "released": facts.get("released"), "deps": facts.get("deps"),
                                    "stars": facts.get("stars"), "tools": hs.get("tools", [])[:25], "server": hs.get("server"), "sandbox_secs": hs.get("secs"),
                                    "risky_tools": risky[:10]}, sort_keys=True)[:1500])
    reg.upsert("tools", e)
    return e


def run(need: str, max_new: int = 2, dry_run: bool = False, fetch=None, sandboxer=None) -> dict:
    reg = Registry(ROOT / "registry"); ledger = _ledger(); now = time.time(); day = time.strftime("%Y-%m-%d")
    fetch = fetch or _fetch; sandboxer = sandboxer or sandbox
    known = {t.id for t in reg.all("tools")}
    cands = discover(need, fetch)
    verdicts, added = [], []; attempts = 0; t_end = time.time() + 20 * 60
    for c in cands:
        key = f"{c.get('name')}:{c.get('version')}"
        if tool_id(c) in known: verdicts.append((c, "known", "already in registry")); continue
        prev = ledger["verdicts"].get(key)
        if prev and now - prev.get("ts", 0) < LEDGER_DAYS * 86400: verdicts.append((c, "ledger", prev["verdict"])); continue
        facts = research(c, fetch)
        v, why = evaluate(c, facts, now)
        if v != "keep": verdicts.append((c, "rejected", "; ".join(why))); continue
        if len(added) >= max_new or attempts >= 2 * max_new or time.time() > t_end:
            verdicts.append((c, "deferred", "budget reached (max_new / attempts / 20 min)")); continue
        if not (WIN or sandboxer is not sandbox):
            verdicts.append((c, "deferred", "sandbox runs on the laptop only")); continue
        attempts += 1; hs = sandboxer(c)
        if not hs.get("ok"): verdicts.append((c, "rejected", f"sandbox {hs.get('stage')}: {hs.get('reason', '')[:120]}")); continue
        verdicts.append((c, "approved", f"probation; tools={len(hs.get('tools', []))} {hs.get('secs')}s"))
        if not dry_run: added.append(integrate(reg, c, facts, hs, need).id)
        else: added.append(tool_id(c))
    if not dry_run:
        for c, v, r in verdicts:
            if v in ("rejected", "approved"):
                ledger["verdicts"][f"{c.get('name')}:{c.get('version')}"] = {"verdict": v, "reason": r[:200], "ts": now, "date": day, "need": need}
        _save_ledger(ledger)
    return {"need": need, "candidates": len(cands), "added": added,
            "verdicts": [{"name": c.get("name"), "verdict": v, "reason": r[:160]} for c, v, r in verdicts]}


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0].startswith("-"): print(__doc__); sys.exit(2)
    mx = int(a[a.index("--max") + 1]) if "--max" in a else 2
    print(json.dumps(run(a[0], mx, "--dry-run" in a), indent=1))
