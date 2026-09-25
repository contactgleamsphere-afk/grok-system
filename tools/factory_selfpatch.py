"""D-122 self-improvement stage 2 — the factory proposes CODE, never applies it.

    proposal (insight) or owner request
      → an LLM lane drafts exact find/replace edits for ONE allowed file
      → edits are checked against the security envelope (paths, size, forbidden tokens, no new I/O imports)
      → applied in a throw-away git worktree on branch proposal/<slug>
      → core/tests must pass there (real pytest, same suite the worker gates on)
      → branch pushed; a pull request is opened with the evidence; GitHub Actions CI re-runs the suite off-laptop
      → the OWNER merges (or closes). main is never touched by this module.

What the envelope forbids (so self-improvement can never silently expand privilege): editing guard/registry/jobs/
worker/config/scripts/workflows/security docs; touching lines that mention permissions, allowances, approvals,
shell/network scopes or keys; adding subprocess/socket/ctypes/urllib/os.system/eval/exec; more than MAX_LINES
changed lines; more than one file per patch. Everything is audited by the worker (`factory.selfpatch`).
"""
from __future__ import annotations
import datetime, json, os, pathlib, re, subprocess, sys, time, urllib.request

ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "core"))

PATCHABLE = ("tools/factory_insight.py", "tools/factory_report.py", "tools/factory_bench.py", "tools/factory_monitor.py",
             "tools/factory_repair.py", "tools/factory_discover.py", "tools/factory_tooldisc.py", "tools/factory_scout.py",
             "tools/factory_probe.py", "tools/factory_pipeline.py", "core/factory/factory.py", "core/factory/botspec.py",
             "core/tests/test_bench.py")
FORBIDDEN_LINE = re.compile(r"allowed_permissions|allowance|approve|permission|shell:|net:|_KEY|TOKEN|SECRET|seal|guard|"
                            r"restrictToWorkspace|allowedEnvKeys|revoke|sandbox_env|_clean_env", re.I)
FORBIDDEN_CODE = re.compile(r"\b(subprocess|socket|ctypes|urllib|requests|httpx|shutil\.rmtree|os\.system|os\.remove|os\.unlink|"
                            r"eval|exec|__import__|importlib|winreg|schtasks|powershell)\b")
MAX_LINES = 80
REPO = "contactgleamsphere-afk/grok-system"

PROMPT = """You are improving a small Python code base (an AI bot factory). Make the SMALLEST change that addresses the
proposal below, in exactly one file, as exact text edits. Rules: keep behaviour otherwise identical; do not touch
permissions, security, approvals, credentials or network code; no new imports of subprocess/socket/urllib/ctypes;
prefer adding or tightening a check over rewriting; if a unit test file is the target, add ONE focused test.
Return ONLY JSON: {"file": "<one of the allowed paths>", "summary": "<one sentence>",
"edits": [{"find": "<exact existing text, 1-12 lines, unique in the file>", "replace": "<new text>"}]}
Allowed files: %s

PROPOSAL
kind: %s   severity: %s
evidence: %s
suggestion: %s

CURRENT FILE (%s), line-numbered for reference — quote text exactly WITHOUT the numbers:
%s
"""


def _numbered(text: str, max_lines: int = 700) -> str:
    lines = text.splitlines()[:max_lines]
    return "\n".join(f"{i + 1:4d}| {ln}" for i, ln in enumerate(lines))


def pick_file(proposal: dict) -> str:
    k = proposal.get("kind", ""); s = (proposal.get("suggestion", "") + proposal.get("evidence", "")).lower()
    if "spec_consistency" in s or k == "architect": return "tools/factory_pipeline.py"
    if k == "template" or "runner" in s or "matcher" in s: return "tools/factory_pipeline.py"
    if k == "repair": return "tools/factory_repair.py"
    if k == "lanes" or "bench" in s or "chain" in s: return "tools/factory_pipeline.py"
    if k == "quality": return "tools/factory_insight.py"
    return "tools/factory_insight.py"


def draft(proposal: dict, file: str, src: str, chat=None, feedback: str = "", skip: set | None = None) -> tuple[dict | None, str, str]:
    """→ (edits_json | None, lane, raw). One attempt per call via the pipeline's failover chat(); `feedback` carries the
    previous envelope error so the next attempt (on a different lane when possible) can correct it."""
    import factory_pipeline as fp
    chat = chat or fp.chat
    msg = PROMPT % (", ".join(PATCHABLE), proposal.get("kind"), proposal.get("severity"), proposal.get("evidence", "")[:800],
                    proposal.get("suggestion", "")[:800], file, _numbered(src))
    if feedback: msg += f"\nPREVIOUS ATTEMPT WAS REJECTED: {feedback}\nQuote `find` text EXACTLY as in the file (same backslashes, quotes and spaces); pick a shorter unique anchor if needed.\n"
    try: text, lane = chat([{"role": "user", "content": msg}], max_tokens=3000, skip=skip)
    except TypeError: text, lane = chat([{"role": "user", "content": msg}], max_tokens=3000)
    return _parse(text), lane, text[:400]


def _parse(text: str) -> dict | None:
    """Models wrap JSON in fences and put Python source (with \\b, \\s, \\d …) inside strings — invalid JSON escapes.
    Try strict, then with invalid escapes doubled, then non-strict (raw newlines)."""
    t = re.sub(r"<thought>.*?</thought>", "", text, flags=re.S)                  # gemma reasoning blocks
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t.strip(), flags=re.M)
    m = re.search(r"\{.*\}", t, re.S)
    if not m: return None
    cand = m.group(0)
    for fix in (lambda x: x, lambda x: re.sub(r'\\(?![\\/"bfnrtu])', r"\\\\", x)):
        for strict in (True, False):
            try:
                d = json.loads(fix(cand), strict=strict)
                if isinstance(d, dict) and d.get("edits"): return d
            except Exception:
                continue
    return None


def check_envelope(patch: dict, src: str) -> tuple[str | None, str]:
    """Returns (error | None, new_source). Pure — the security envelope, unit-testable without git or an LLM."""
    f = patch.get("file")
    if f not in PATCHABLE: return f"file not patchable: {f}", src
    edits = patch.get("edits") or []
    if not (1 <= len(edits) <= 8): return f"{len(edits)} edits (need 1..8)", src
    new = src; changed = 0
    for e in edits:
        find, rep = str(e.get("find", "")), str(e.get("replace", ""))
        if not find.strip(): return "empty find", src
        if new.count(find) != 1: return f"find text not unique/absent ({new.count(find)} matches): {find[:60]!r}", src
        for ln in find.splitlines() + rep.splitlines():
            if FORBIDDEN_LINE.search(ln): return f"touches a security-relevant line: {ln.strip()[:70]!r}", src
        for ln in rep.splitlines():
            if FORBIDDEN_CODE.search(ln) and not FORBIDDEN_CODE.search(find): return f"introduces forbidden code: {ln.strip()[:70]!r}", src
        changed += max(len(find.splitlines()), len(rep.splitlines()))
        new = new.replace(find, rep, 1)
    if changed > MAX_LINES: return f"{changed} changed lines > {MAX_LINES}", src
    try: compile(new, f, "exec")
    except SyntaxError as e: return f"result does not compile: {e}", src
    return None, new


def _git(args: list[str], cwd: pathlib.Path, timeout: int = 120) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True, timeout=timeout)


def _token() -> str | None:
    if os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN"): return os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if os.name == "nt":   # same source repo-sync pushes with: the owner's User-scope GITHUB_TOKEN (not visible in an SSH session's env)
        try:
            r = subprocess.run(["powershell", "-NoProfile", "-Command", "[Environment]::GetEnvironmentVariable('GITHUB_TOKEN','User')"],
                               capture_output=True, text=True, timeout=20)
            if r.stdout.strip(): return r.stdout.strip()
        except Exception:
            pass
    url = _git(["config", "--get", "remote.origin.url"], ROOT).stdout.strip()
    m = re.match(r"https://[^:]+:([^@]+)@github\.com/", url)
    if m: return m.group(1)
    try:   # the worker's own session can read the credential store that repo-sync pushes with (not an SSH session)
        r = subprocess.run(["git", "credential", "fill"], input="protocol=https\nhost=github.com\n\n", cwd=str(ROOT),
                           capture_output=True, text=True, timeout=20, env={**os.environ, "GIT_TERMINAL_PROMPT": "0", "GCM_INTERACTIVE": "never"})
        for ln in r.stdout.splitlines():
            if ln.startswith("password="): return ln.split("=", 1)[1].strip() or None
    except Exception:
        pass
    return None


def open_pr(branch: str, title: str, body: str, token: str | None) -> dict:
    if not token: return {"ok": False, "reason": "no GitHub token available to open the PR (branch pushed; open it by hand)"}
    req = urllib.request.Request(f"https://api.github.com/repos/{REPO}/pulls", method="POST",
                                 data=json.dumps({"title": title, "head": branch, "base": "main", "body": body}).encode(),
                                 headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json", "User-Agent": "aifactory-selfpatch/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r: d = json.load(r)
        return {"ok": True, "url": d.get("html_url"), "number": d.get("number")}
    except urllib.error.HTTPError as e:
        return {"ok": False, "reason": f"PR HTTP {e.code}: {e.read(300).decode('utf-8', 'replace')}"}
    except Exception as e:
        return {"ok": False, "reason": repr(e)[:200]}


def run(proposal: dict, slug: str, chat=None, tester=None, pusher=None, pr=None) -> dict:
    """End to end for ONE proposal. tester(worktree)->(ok, tail); pusher(worktree, branch)->(ok, msg); pr(...)->dict."""
    t0 = time.time(); file = pick_file(proposal); src = (ROOT / file).read_text(encoding="utf-8")
    out = {"ok": False, "file": file, "lane": None, "branch": None, "pr": None, "attempts": 0}
    feedback, skip, patch, new = "", set(), None, src
    for attempt in range(3):                                   # live 2026-09-25: first draft misquoted regex escapes → retry with the error
        out["attempts"] = attempt + 1
        patch, lane, raw = draft(proposal, file, src, chat, feedback, skip); out["lane"] = lane; skip.add(lane)
        if not patch: feedback = f"no usable JSON: {raw[:120]}"; continue
        if patch.get("file") and patch["file"] != file and patch["file"] in PATCHABLE and (ROOT / patch["file"]).exists():
            file = patch["file"]; src = (ROOT / file).read_text(encoding="utf-8"); out["file"] = file
        patch["file"] = file
        err, new = check_envelope(patch, src)
        if not err: break
        feedback = err; out["summary"] = patch.get("summary"); patch = None
    if not patch: out["reason"] = f"envelope after {out['attempts']} attempts: {feedback}"; return out
    branch = f"proposal/{datetime.date.today().isoformat()}-{re.sub(r'[^a-z0-9]+', '-', slug.lower())[:40]}"
    wt = ROOT / "run" / "selfpatch" / branch.split("/")[-1]
    out["branch"] = branch; out["summary"] = patch.get("summary")
    try:
        if wt.exists(): _git(["worktree", "remove", "--force", str(wt)], ROOT)
        _git(["fetch", "-q", "origin", "main"], ROOT)
        r = _git(["worktree", "add", "-B", branch, str(wt), "origin/main"], ROOT)
        if r.returncode: out["reason"] = f"worktree: {r.stderr[-200:]}"; return out
        (wt / file).write_text(new, encoding="utf-8")
        ok, tail = (tester or _pytest)(wt)
        out["tests"] = tail
        if not ok: out["reason"] = f"tests red in worktree: {tail}"; return out
        _git(["add", file], wt); _git(["-c", "user.name=AI Factory", "-c", "user.email=factory@local", "commit", "-q", "-m",
                                       f"proposal: {patch.get('summary', slug)[:70]}\n\nkind={proposal.get('kind')} severity={proposal.get('severity')}\nevidence: {proposal.get('evidence', '')[:300]}\n\nFactory-authored (D-122). Tests green in worktree. Owner review required."], wt)
        pok, pmsg = (pusher or _push)(wt, branch)
        if not pok: out["reason"] = f"push: {pmsg}"; return out
        body = (f"**Factory-authored change (D-122) — review before merging; nothing is applied to `main` by the factory.**\n\n"
                f"Proposal: `{proposal.get('kind')}` / {proposal.get('severity')}\n\nEvidence: {proposal.get('evidence', '')[:600]}\n\n"
                f"Suggestion: {proposal.get('suggestion', '')[:600]}\n\nDraft lane: `{lane}` · file: `{file}` · edits: {len(patch['edits'])}\n\n"
                f"Local tests in worktree: `{tail}` · CI re-runs the suite on this branch.\n\nEnvelope: single file, ≤{MAX_LINES} lines, no security-relevant lines, no new I/O imports.")
        res = (pr or open_pr)(branch, f"[factory] {patch.get('summary', slug)[:60]}", body, _token())
        out["pr"] = res.get("url") if res.get("ok") else None
        out["ok"] = True; out["pr_status"] = res
        return out
    finally:
        _git(["worktree", "remove", "--force", str(wt)], ROOT); out["secs"] = int(time.time() - t0)


def _pytest(wt: pathlib.Path) -> tuple[bool, str]:
    r = subprocess.run([sys.executable, "-m", "pytest", str(wt / "core" / "tests"), "-q", "-p", "no:cacheprovider", "-x"],
                       cwd=str(wt), capture_output=True, text=True, timeout=900, env={**os.environ, "AIFACTORY_REPO": str(wt)})
    lines = [ln for ln in (r.stdout or r.stderr).strip().splitlines() if ln.strip()]
    return r.returncode == 0, (lines[-1] if lines else "no output")[:160]


def _push(wt: pathlib.Path, branch: str) -> tuple[bool, str]:
    tok = _token()
    url = f"https://x-access-token:{tok}@github.com/{REPO}.git" if tok else "origin"
    r = _git(["-c", "credential.helper=", "push", "-q", "-f", url, f"HEAD:refs/heads/{branch}"], wt, timeout=180)
    return r.returncode == 0, (r.stderr or r.stdout)[-200:].replace(tok or "\0", "***")


def load_proposal(date: str, index: int) -> tuple[dict, str]:
    d = json.loads((ROOT / "proposals" / f"{date}.json").read_text(encoding="utf-8"))
    props = d.get("proposals", d) if isinstance(d, dict) else d
    p = props[index - 1]
    return p, f"{date}-{index}-{p.get('kind', 'x')}"


if __name__ == "__main__":
    if len(sys.argv) < 3: print("usage: factory_selfpatch.py <proposals-date> <index>  |  request \"<change request>\""); sys.exit(2)
    if sys.argv[1] == "request":
        p, slug = {"kind": "owner-request", "severity": "medium", "evidence": "owner request", "suggestion": " ".join(sys.argv[2:])}, "owner-" + str(int(time.time()))
    else:
        p, slug = load_proposal(sys.argv[1], int(sys.argv[2]))
    print(json.dumps(run(p, slug), indent=1))
