# BOT_REGISTRY

Generated from registry/bots.json.

| id | name | status | verified | primary | fallbacks | tools | permissions | workspace | notes | updated |
|---|---|---|---|---|---|---|---|---|---|---|
| 001 | master | building | VERIFIED | local3b |  | exec, read_file, write_file, web_search, web_fetch | fs:read, fs:write, shell:workspace, net:search, net:fetch | `C:\AI\Factory\workspace` | Identity files SOUL.md/AGENTS.md in config/laptop/ — not yet deployed to workspace. | 2026-09-18T17:28:28+00:00 |
| 002 | research-scout | testing | UNVERIFIED | groq-gptoss20b | groq-qwen27b, groq-gptoss120b, local4b | web_search, web_fetch, read_file | net:search, net:fetch, fs:read | `/home/user/grok-system/bots/002-research-scout` | tests 1/2: T1 SCOUT_OK PASS x6; T2 web-research blocked: Groq free tier TPD 200k/model/day exhausted by the day's benchmarks (qwen27b 196k, gpt-oss-120b 198k used); gpt-oss-20b alone at 8k TPM cannot finish a 7-step task in 480s | 2026-09-19T16:35:21+00:00 |
