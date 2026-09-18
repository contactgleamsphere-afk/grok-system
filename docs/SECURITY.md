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
