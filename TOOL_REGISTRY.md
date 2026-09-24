<!-- generated from registry/tools.json — edit the JSON, not this file -->
# tools

| id | kind | provides | risk | scope | verified | notes | updated |
|---|---|---|---|---|---|---|---|
| exec | builtin | ['shell'] | high | workspace-only (restrictToWorkspace; NO OS sandbox on Windows) | VERIFIED | nanobot 0.3.5 built-in; reported registered in Phase 1 WebUI | 2026-09-18T17:28:28+00:00 |
| read_file | builtin | ['filesystem'] | low | workspace-only | VERIFIED | nanobot 0.3.5 built-in; reported registered in Phase 1 WebUI | 2026-09-18T17:28:28+00:00 |
| web_fetch | builtin | ['net_fetch'] | low | SSRF guard on | INFERRED | nanobot 0.3.5 built-in; reported registered in Phase 1 WebUI | 2026-09-18T17:28:28+00:00 |
| web_search | builtin | ['web_search'] | low | duckduckgo, keyless | VERIFIED | nanobot 0.3.5 built-in; reported registered in Phase 1 WebUI | 2026-09-18T17:28:28+00:00 |
| write_file | builtin | ['filesystem'] | medium | workspace-only | VERIFIED | nanobot 0.3.5 built-in; reported registered in Phase 1 WebUI | 2026-09-18T17:28:28+00:00 |

<!-- mcp-probation:start -->
## MCP servers on probation (auto, D-108)
Discovered by `factory_tooldisc.py`; sandbox-verified (stdio handshake, secrets stripped). **Not attached to any bot** — owner approval is required to wire one into a bot config.

| id | risk | verified | licence | released | tools | source |
|---|---|---|---|---|---|---|
| mcp:mcp-sqlite3 | high | INFERRED | MIT | 2026-03-31 | 25 (get_sqlite_version, get_sqlite3_version, complete_sql_statement, connect_database…) | https://github.com/daedalus/mcp-sqlite3 |
<!-- mcp-probation:end -->
