# FACTORY STATUS — 2026-09-25T01:12:12

**Worker:** running — last worker activity 0 min ago

**Bots:** 24/26 active   **Queue:** {"cancelled": 41, "done": 215, "queued": 2, "running": 2}   **Healthy lanes:** gemini-flash, gemini-flash36, gemini-flash38, gemini-gemini-flash-lite-latest, gemini-gemma26b, gemini-lite, gemini-lite31, groq-gptoss120b, groq-gptoss20b, groq-qwen27b, local3b, local4b

## Needs attention
- bot 010 dedupe-failover-probe is paused
- 1 retired / 1 paused bots (see Bots table)
- lane or-deepseek BLOCKED: gone: {"error":{"message":"this model is unavailable for free. the paid version 
- lane or-ling-30-flash-fin BLOCKED: failed probation: error
- lane or-ling-30-flash-sante BLOCKED: failed probation: error
- lane or-ling-30-flash-vl BLOCKED: gone: {"error":{"message":"this model is unavailable for free. the paid version 
- ACTION REQUIRED (owner): provider:cerebras — set CEREBRAS_API_KEY (User env) after signing up: https://cloud.cerebras.ai (free tier ~1M tokens/day)
- ACTION REQUIRED (owner): provider:nvidia — set NVIDIA_API_KEY (User env) after signing up: https://build.nvidia.com (free ~40 rpm, tool-capable models)
- ACTION REQUIRED (owner): provider:mistral — set MISTRAL_API_KEY (User env) after signing up: https://console.mistral.ai (Experiment free tier)
- ACTION REQUIRED (owner): 12 free resources need a human signup/key — cerebras, cloudflare-r2, cloudflare-workers, cloudflare-workers-ai, google-cloud-run, hf-router… (docs/INFRA.md)
- DECISION (owner): 2 MCP server(s) sandbox-verified, on probation: mcp:crawlio-browser, mcp:mcp-sqlite-tools — `factory_worker.py approve-tool <id>` to make them grantable to bots, or leave them (nothing uses them)

## Bots
| id | name | status | verified | permissions |
|---|---|---|---|---|
| 001 | master | active | VERIFIED | fs:read, fs:write, shell:workspace, net:search, net:fetch |
| 002 | research-scout | active | VERIFIED | net:search, net:fetch, fs:read |
| 003 | code-smith | active | VERIFIED | fs:read, fs:write, shell:workspace |
| 004 | changelog-writer | active | VERIFIED | fs:read, fs:write |
| 005 | csv-quality-auditor | active | VERIFIED | fs:read, fs:write |
| 006 | json-to-markdown-table | active | VERIFIED | fs:read, fs:write |
| 007 | todo-extractor | active | VERIFIED | fs:read, fs:write |
| 008 | word-frequency-bot | active | VERIFIED | fs:read, fs:write |
| 009 | line-dedupe-bot | active | VERIFIED | fs:read, fs:write |
| 010 | dedupe-failover-probe | paused | INFERRED | fs:read, fs:write |
| 011 | word-frequency-counter | active | VERIFIED | fs:read, fs:write |
| 012 | csv-column-sum | active | VERIFIED | fs:read, fs:write |
| 013 | log-error-filter | active | VERIFIED | fs:read, fs:write |
| 014 | error-log-analyzer | active | VERIFIED | fs:read, fs:write |
| 015 | system-cleanup | retired | BLOCKED | shell:workspace |
| 016 | workspace-tidy-counter | active | VERIFIED | shell:workspace |
| 017 | name-sorter | active | VERIFIED | fs:read, fs:write |
| 018 | csv-country-totals | active | VERIFIED | fs:read, fs:write |
| 019 | pytest-runner | active | VERIFIED | fs:read, fs:write, shell:workspace |
| 020 | workspace-file-lister | active | VERIFIED | shell:workspace, fs:write |
| 021 | email-line-counter | active | VERIFIED | fs:read, fs:write |
| 022 | csv-refund-filter | active | VERIFIED | fs:read, fs:write |
| 023 | refund-summarizer | active | VERIFIED | fs:read, fs:write |
| 024 | pytest-runner-bot | active | VERIFIED | fs:read, fs:write, shell:workspace |
| 025 | text-transformer | active | VERIFIED | fs:read, fs:write |
| 026 | sqlite-query-bot | active | VERIFIED | fs:read, fs:write, mcp:mcp-sqlite3 |

## Jobs (24h)
| id | kind | state | att | class | bot | objective |
|---|---|---|---|---|---|---|
| 499dd527 | probe | done | 1 | - | - |  |
| 657a2134 | run | done | 1 | - | 018 |  |
| 96a47019 | tick | done | 1 | - | - |  |
| ada8b925 | probe | done | 1 | - | - |  |
| bdee72b1 | probe | done | 1 | - | - |  |
| 0253aa82 | report | running | 1 | - | - |  |
| c35f9462 | bench | done | 1 | - | - |  |
| ec7ed624 | monitor | done | 1 | - | - |  |
| 581618e9 | test | done | 1 | - | 001 |  |
| c50593d5 | test | done | 1 | - | 002 |  |
| 36a3539c | test | done | 1 | - | 003 |  |
| 1eedd036 | test | done | 1 | - | 004 |  |
| 192d34a1 | test | done | 1 | - | 005 |  |
| 80275837 | test | done | 1 | - | 006 |  |
| 902b8c56 | test | done | 1 | - | 007 |  |
| 84f90993 | test | done | 1 | - | 008 |  |
| d67880ac | test | done | 1 | - | 009 |  |
| b31aa10e | test | done | 1 | - | 011 |  |
| e6ebfe8c | test | done | 1 | - | 012 |  |
| 7a134c31 | test | done | 1 | - | 013 |  |
| 06b13d4d | test | done | 1 | - | 014 |  |
| 6ea2de2b | test | done | 1 | - | 016 |  |
| e155909a | test | done | 1 | - | 017 |  |
| bedaa1af | test | done | 1 | - | 018 |  |
| 482340ef | test | done | 1 | - | 019 |  |
| e26da376 | test | done | 1 | - | 020 |  |
| a6fa92d2 | test | done | 1 | - | 021 |  |
| c8eb6c89 | test | done | 1 | - | 022 |  |
| 820f7ef9 | test | done | 1 | - | 023 |  |
| 87f2fbc2 | test | done | 1 | - | 024 |  |
| c1c70d3e | test | done | 1 | - | 025 |  |
| bc494d29 | monitor | done | 1 | - | - |  |
| c3c35810 | repair | cancelled | 1 | logic | 002 |  |
| bcb0ba61 | discover | done | 1 | - | - |  |
| 26e7235d | discover | done | 1 | - | - |  |
| 39a61954 | discover | done | 1 | - | - |  |
| 6a46a820 | discover | done | 1 | - | - |  |
| e30126b8 | discover | done | 1 | - | - |  |
| 8b22fe5c | discover | done | 1 | - | - |  |
| f800e68b | discover | done | 1 | - | - |  |
| aa0b21ba | discover | done | 1 | - | - |  |
| ad7a13c3 | bench | done | 1 | - | - |  |
| 7b4d176b | test | done | 1 | - | 001 |  |
| c5a39c84 | test | cancelled | 0 | - | 001 |  |
| 6ebf5d8b | test | cancelled | 0 | - | 002 |  |
| c20c2407 | test | cancelled | 0 | - | 003 |  |
| 7ee5ebb8 | test | cancelled | 0 | - | 004 |  |
| 9ce55607 | test | cancelled | 0 | - | 005 |  |
| 29002603 | test | cancelled | 0 | - | 006 |  |
| ff6fe1b9 | test | cancelled | 0 | - | 007 |  |
| 1ddf7b9f | test | cancelled | 0 | - | 008 |  |
| ab3a25c4 | test | cancelled | 0 | - | 009 |  |
| 8b60cad0 | test | cancelled | 0 | - | 011 |  |
| 67703501 | test | cancelled | 0 | - | 012 |  |
| 240be6ff | test | cancelled | 0 | - | 013 |  |
| 356da82f | test | cancelled | 0 | - | 014 |  |
| 34c93c2f | test | cancelled | 0 | - | 016 |  |
| 8e9fd24a | test | cancelled | 0 | - | 017 |  |
| 09de5024 | test | cancelled | 0 | - | 018 |  |
| ca4a7aeb | test | cancelled | 0 | - | 019 |  |
| a51e46b5 | test | cancelled | 0 | - | 020 |  |
| 764e7481 | test | cancelled | 0 | - | 021 |  |
| 58a57670 | test | cancelled | 0 | - | 022 |  |
| 6a5c5393 | test | cancelled | 0 | - | 023 |  |
| a735d64e | test | cancelled | 0 | - | 024 |  |
| 356d0905 | test | cancelled | 0 | - | 025 |  |
| faef1fd6 | bench | done | 1 | - | - |  |
| 754d191f | repair | done | 1 | - | 006 |  |
| 000fb61b | repair | done | 1 | - | 007 |  |
| d01464cb | repair | done | 1 | - | 014 |  |
| f773c50b | tick | done | 1 | - | - |  |
| 4a052706 | probe | done | 1 | - | - |  |
| 7ae30d43 | run | done | 1 | - | 012 |  |
| 21c6bb9d | test | done | 1 | - | 020 |  |
| efe05c44 | create | cancelled | 1 | security | - | Answer questions about a SQLite database file the user names in the wo |
| 49eeafe3 | tick | done | 1 | - | - |  |
| c7322101 | probe | done | 1 | - | - |  |
| ab489546 | create | cancelled | 1 | security | - | Answer questions about a SQLite database file in the workspace using t |
| 1ed33ffb | create | done | 1 | - | - | Answer questions about a SQLite database file in the workspace using t |
| bd24f8ff | test | done | 1 | - | 026 |  |
| c18703a7 | repair | cancelled | 1 | logic | 026 |  |
| 1f96bf25 | rebuild | done | 1 | - | 026 |  |
| a14b2bd5 | rearchitect | done | 1 | - | 026 |  |
| 31f4e431 | test | done | 1 | - | 001 |  |
| 865f4e25 | discover | done | 1 | - | - |  |
| 2d873e41 | discover | done | 1 | - | - |  |
| 5db5434d | bench | done | 1 | - | - |  |
| 9a01357c | tick | done | 1 | - | - |  |
| 86ba95ba | probe | done | 2 | - | - |  |
| 42efc9da | probe | done | 1 | - | - |  |
| 40419dff | probe | done | 1 | - | - |  |
| 769af551 | discover | done | 1 | - | - |  |
| eb45cb88 | discover | done | 1 | - | - |  |
| 9c9d8b05 | discover | done | 1 | - | - |  |
| 57739895 | discover | done | 1 | - | - |  |
| 7e3cce23 | discover | done | 1 | - | - |  |
| 10338bdf | discover | done | 1 | - | - |  |
| c76efa69 | canary | done | 1 | - | - |  |
| 37b08250 | probe | done | 1 | - | - |  |
| e7340c6e | tick | done | 1 | - | - |  |
| d0196af8 | probe | done | 1 | - | - |  |
| 4a8b6119 | probe | done | 1 | - | - |  |
| 2107158e | discover | done | 1 | - | - |  |
| 1ce9e348 | discover | done | 1 | - | - |  |
| 66ca017e | discover | done | 1 | - | - |  |
| bc1ce82b | discover | done | 1 | - | - |  |
| 541f6f6e | discover | done | 1 | - | - |  |
| d350d0ae | discover | done | 1 | - | - |  |
| 3fe01ea5 | run | done | 1 | - | 018 |  |
| 7946d979 | tick | done | 1 | - | - |  |
| 50cb8d24 | probe | done | 1 | - | - |  |
| 14d4a04c | tick | done | 1 | - | - |  |
| d332609a | probe | done | 1 | - | - |  |
| 037afd02 | scout | done | 1 | - | - |  |
| 9504d124 | insight | done | 1 | - | - |  |
| ff48e3c4 | bench | done | 1 | - | - |  |
| 92411237 | tooldisc | done | 1 | - | - |  |
| 86969460 | tooldisc | done | 1 | - | - |  |
| 4901b2db | tooldisc | done | 1 | - | - |  |
| e7744308 | probe | queued | 0 | - | - |  |
| 190e3258 | tick | queued | 0 | - | - |  |
| 6e4d634b | tooldisc | done | 1 | - | - |  |
| d6be18bd | tooldisc | done | 1 | - | - |  |
| c858bfee | tooldisc | running | 1 | - | - |  |

## Lane quality (D-050, reference suite, rolling window)
| lane | score | secs | runs |
|---|---|---|---|
| gemini-gemini-flash-lite-latest | 4/4 | 42 | 1 |
| or-ling-30-flash-vl | 4/4 | 62 | 1 |
| gemini-lite31 | 4/4 | 73 | 1 |
| or-nex-n25-pro | 4/4 | 84 | 1 |
| or-ling-30-flash-sante | 4/4 | 89 | 1 |
| groq-gptoss120b | 8/8 | 99 | 2 |
| or-ling-30-flash-fin | 4/4 | 100 | 1 |
| groq-gptoss20b | 4/4 | 106 | 1 |
| or-nemotron-35-lightning | 2/2 | 564 | 1 |
| gemini-gemma26b | 3/4 | 73 | 1 |
| gemini-flash36 | 2/4 | 63 | 1 |
| gemini-flash38 | 2/4 | 128 | 1 |
| groq-qwen27b | 2/4 | 147 | 1 |
| gemini-flash | 2/4 | 180 | 1 |
| gemini-lite | 1/4 | 618 | 1 |

## Lanes
| id | provider | state | latency s |
|---|---|---|---|
| gemini-flash | gemini | ok | 10.98 |
| gemini-flash36 | gemini | ok | 2.18 |
| gemini-flash38 | gemini | ok | 6.29 |
| gemini-gemini-flash-lite-latest | gemini | ok | 2.02 |
| gemini-gemma26b | gemini | ok | 1.66 |
| gemini-lite | gemini | ok | 1.64 |
| gemini-lite31 | gemini | ok | 3.6 |
| groq-gptoss120b | groq | ok | 1.86 |
| groq-gptoss20b | groq | ok | 1.53 |
| groq-qwen27b | groq | ok | 0.42 |
| local3b | ollama | ok | - |
| local4b | ollama | ok | - |
| or-deepseek | openrouter | BLOCKED | - |
| or-ling-30-flash-fin | openrouter | BLOCKED | 1.71 |
| or-ling-30-flash-sante | openrouter | BLOCKED | 1.22 |
| or-ling-30-flash-vl | openrouter | BLOCKED | 2.78 |
| or-nemotron-35-lightning | openrouter | cooldown | 59.9 |
| or-nex-n25-pro | openrouter | cooldown | 2.18 |
| or-qwen27b | openrouter | cooldown | - |
| ovh-gptoss20b | custom | BLOCKED | - |
| ovh-llama70b | custom | BLOCKED | - |
| ovh-mistral24b | custom | BLOCKED | - |
