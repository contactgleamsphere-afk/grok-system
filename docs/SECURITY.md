# Security

## Hard rules

- Never expose Ollama (`:11434`) to the public internet without auth and TLS.
- Prefer Docker sandbox for autonomous coding agents; unsandboxed agents = full user FS access.
- Do not reuse your daily browser profile with browser-use.
- Scope GitHub PATs tightly; rotate any token that appeared in chat.
- Audit each MCP server before enabling (filesystem/shell = RCE-class).
- Disable CrewAI telemetry: `OTEL_SDK_DISABLED=true`.
- Pin third-party git tags/commits in `stack/versions.yml`; review before bumping.

## Licence traps

- Open WebUI: branding restriction for larger deployments — not our core UI.
- AGPL components (e.g. some memory DBs): accept explicitly or avoid.
- Mixed licences under `modelcontextprotocol/servers` — check per server.

## Supply chain

- Prefer package managers / verified releases over `curl | sh` when possible.
- If an installer script is unavoidable, fetch, read, then run.

## Boundary guard + job isolation (2026-09-21, D-031/D-032)
- Every create/repair result is diffed against the previous registry entry; any expansion of permissions, tools, net/shell, model_policy, re-enabled tools, or credential-looking strings in the bundle → `security` class → job paused, production untouched. Unit-tested (core/tests/test_jobs.py, test_guard).
- Repair model never sees expected test answers (prevents reward hacking); candidates that still echo answers are rejected before sandboxing.
- The worker runs with the owner's user env only; keys are read from User env at start, never written to the queue DB or audit (payloads contain objectives/ids only).
- 2026-09-21: `GITHUB_TOKEN` lives in the owner's Windows **User** environment only (never in repo/config); git on the laptop uses an inline credential helper that reads it from env. The worker pushes state commits with it. Rotate via GitHub → the helper picks up the new value on next start.

## Permission allowance (D-054, 2026-09-22)
- Every `create`/`plan`/`rearchitect` job carries an allowance; default `fs:read, fs:write, net:search, net:fetch`. `shell:workspace` requires an explicit owner `--allow`; `shell:system` is never grantable.
- The gate runs before any file is written. Over-reach → `security` pause + `security.violation` audit; nothing is built.
- Incident: bot 015 was built with shell before this gate existed → retired to `bots/_retired`, BLOCKED.

## Bundle integrity (D-068)
Sealed files: bot.json, nanobot.patch.json, AGENTS.md, SOUL.md — sha256 in `registry/bots.json[id].seal`. Drift ⇒
run/test refuse. Only the factory reseals (build/repair). Live test 2026-09-22: appended a permission-widening line
to bot 018 AGENTS.md → `run` returned `bundle integrity: ['AGENTS.md'] changed outside the factory`.

## Semantic boundary guard (D-099, 2026-09-23)
Frozen-field diffs cannot see an expansion that lives in the *wording* of instructions. `instruction_boundary_violations()`
(tools/factory_repair.py) rejects any affirmative instruction to: shell out without `exec`; use the network without
`web_*`; touch paths outside the bot workspace (drive letters, `..`, `~`, `%APPDATA%`, `/etc`); handle API keys /
tokens / passwords; change model/provider/lane; bypass a guard/sandbox/policy; or destroy system-wide data.
Prohibitions ("never access files outside the workspace") are allowed via sentence-local negation; "if not found, use
exec" is still affirmative. Applied in repair (candidate rejected before sandbox build, reason audited) and in the
architect gate (`spec_consistency`). Verified with 0 false positives on all 23 live specs and their history.

## Audit hash chain (D-091, 2026-09-22)
`AUDIT.jsonl` rows carry `prev`/`h` (sha256 over seq,ts,job,bot,event,actor,detail,prev). `factory_worker.py audit-verify`
exits 1 on any edit/removal/reorder. The SQLite table stays the source; the JSONL is the tamper-evident export.

## MCP tools, self-heal and scout boundaries (D-108–D-118, 2026-09-24)
- **Discovered tools are never trusted by discovery.** Sandboxing runs with a secrets-stripped environment (no *_KEY,
  *_TOKEN, GH_*, cloud creds), in a temp venv/npm cache, with a hard kill (`taskkill /T /F`) on timeout. The result is
  PROBATION; only the owner's `approve-tool` (CLI, not reachable from any bot) allows a bot spec to reference it, and
  the boundary guard still applies to whatever the tool touches.
- **Tunnel self-heal is not privilege escalation**: `tunnel_selfheal()` only runs the pre-registered scheduled task
  (`schtasks /Run /TN AIFactory-Tunnel`); it cannot change the task, the script it runs, or the tunnel provider.
  Supervisor code lives in the repo (reviewable, hash-tracked); the on-disk file is a shim.
- **Factory canary has no footprint**: `register=False` build in a scratch directory, `fs:read` only, deleted after.
- **Infra scout is legitimate by construction**: one GET per keyless endpoint, keys sent only to their own provider,
  no signups/identity/ToS workarounds; card-verification tiers are owner-only rows. Missing keys are reported, never
  self-applied.

## Self-patching envelope (D-122, 2026-09-25)
The factory may now *draft* code, but only inside an envelope that makes privilege expansion structurally impossible:
one file per patch from an allow-list of non-security modules (never `guard.py`, `registry.py`, `jobs.py`,
`factory_worker.py`, `config/`, `scripts/`, `.github/`, security docs); no edit may touch a line mentioning
permissions, allowances, approvals, shell/net scopes, keys or seals; no new `subprocess`/`socket`/`urllib`/`ctypes`/
`eval`/`exec`/`importlib`; ≤80 changed lines; must compile; `core/tests` must pass in an isolated worktree; the
result is a branch + pull request and CI run — never a write to `main`. Merge is the owner's act on GitHub, so the
audit of *what changed and who approved it* lives in git history as well as `factory.selfpatch`.
