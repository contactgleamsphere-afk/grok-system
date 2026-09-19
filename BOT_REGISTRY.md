# BOT_REGISTRY

Generated from registry/bots.json.

| id | name | status | verified | primary | fallbacks | tools | permissions | workspace | notes | updated |
|---|---|---|---|---|---|---|---|---|---|---|
| 001 | master | building | VERIFIED | local3b |  | exec, read_file, write_file, web_search, web_fetch | fs:read, fs:write, shell:workspace, net:search, net:fetch | `C:\AI\Factory\workspace` | Identity files SOUL.md/AGENTS.md in config/laptop/ — not yet deployed to workspace. | 2026-09-18T17:28:28+00:00 |
| 002 | research-scout | testing | UNVERIFIED | groq-qwen27b | groq-gptoss120b, local4b | web_search, web_fetch, read_file | net:search, net:fetch, fs:read | `/home/user/grok-system/bots/002-research-scout` | tests 1/2: T1 SCOUT_OK PASS 12s; T2 multi-step web research TIMEOUT (Groq 8k TPM -> 429 -> falls to local4b which cannot finish in 480s). See TEST_RESULTS 2026-09-19 16:xx | 2026-09-19T15:51:26+00:00 |
