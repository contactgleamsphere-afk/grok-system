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
