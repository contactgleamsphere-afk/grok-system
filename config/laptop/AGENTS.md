# AI Factory — Operating Instructions (AGENTS.md)

## Workspace
- Root: `C:\AI\Factory\workspace`
- Registry files (create if missing, keep as plain Markdown/JSON, commit to workspace git):
  - `registry/capabilities.json` — what the system can do, by which tool/model, verified date
  - `registry/models.json` — presets, measured tok/s, RAM use, strengths, known failures
  - `registry/bots.json` — every bot created by the factory (Phase 6+)
  - `registry/infra.json` — free/legit infrastructure discovered (Phase 7+)
  - `log/decisions.md` — dated decisions and reasons
  - `log/failures.md` — what broke, root cause, fix

## Phase discipline
Work is done in numbered phases. Each phase has explicit deliverables and an A–H report. Never begin the next phase without the owner's go.

## Tool rules
- `exec`: workspace-scoped. Allowed: git, python (venv), pip inside venv, ollama CLI read-only commands (`ollama list`, `ollama ps`, `ollama show`), directory listing, file read/write inside workspace.
- Forbidden without explicit owner instruction in the current conversation: `ollama pull/rm`, `pip install` outside the factory venv, registry edits, firewall/network changes, anything touching files outside `C:\AI\Factory`.
- `web_search` / `web_fetch`: allowed for research. Record sources with URLs.
- Never write secrets (API keys, tokens, passwords) into any file in the workspace. Use environment variables via `${VAR}` in config.

## Capability discovery protocol (when you hit "I cannot do X")
1. Write the capability requirement in one sentence.
2. Search GitHub + official docs for open-source candidates (≥2).
3. For each: licence, last commit date, stars, dependencies, whether it runs on Windows/CPU, security concerns.
4. Recommend one with reasons; state install footprint.
5. Do NOT install. Report and stop.

## Report format (end of every phase)
A. What was installed/changed (exact versions, paths)
B. Verification commands run and their real output
C. Measurements (numbers)
D. Config diff
E. Warnings / limitations discovered
F. Anything requiring owner action
G. Security notes
H. PASS / FAIL and why
