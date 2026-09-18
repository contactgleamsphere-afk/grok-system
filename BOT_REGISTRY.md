<!-- generated from registry/bots.json — edit the JSON, not this file -->
# bots

| id | name | purpose | status | model_policy | tools | permissions | workspace | version | schedules | tests | verified | notes | updated |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | master | Orchestrates the AI Factory; creates and supervises other bots | building | {'fallbacks': [], 'primary': 'local3b'} | ['exec', 'read_file', 'write_file', 'web_search', 'web_fetch'] | ['fs:read', 'fs:write', 'shell:workspace', 'net:search', 'net:fetch'] | C:\AI\Factory\workspace | 0.1.0 | [] | ['nanobot agent -m "Reply with exactly: PHASE1_OK" -> PHASE1_OK'] | VERIFIED | Identity files SOUL.md/AGENTS.md in config/laptop/ — not yet deployed to workspace. | 2026-09-18T17:28:28+00:00 |
