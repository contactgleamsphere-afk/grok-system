<!-- generated from registry/tools.json — edit the JSON, not this file -->
# tools

| id | kind | provides | risk | scope | verified | notes | updated |
|---|---|---|---|---|---|---|---|
| exec | builtin | ['shell'] | high | workspace-only (restrictToWorkspace; NO OS sandbox on Windows) | VERIFIED | nanobot 0.3.5 built-in; reported registered in Phase 1 WebUI | 2026-09-18T17:28:28+00:00 |
| read_file | builtin | ['filesystem'] | low | workspace-only | VERIFIED | nanobot 0.3.5 built-in; reported registered in Phase 1 WebUI | 2026-09-18T17:28:28+00:00 |
| web_fetch | builtin | ['net_fetch'] | low | SSRF guard on | INFERRED | nanobot 0.3.5 built-in; reported registered in Phase 1 WebUI | 2026-09-18T17:28:28+00:00 |
| web_search | builtin | ['web_search'] | low | duckduckgo, keyless | VERIFIED | nanobot 0.3.5 built-in; reported registered in Phase 1 WebUI | 2026-09-18T17:28:28+00:00 |
| write_file | builtin | ['filesystem'] | medium | workspace-only | VERIFIED | nanobot 0.3.5 built-in; reported registered in Phase 1 WebUI | 2026-09-18T17:28:28+00:00 |
