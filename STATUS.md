# FACTORY STATUS — 2026-10-09T20:06:13

**Worker:** running — last worker activity 0 min ago

**Bots:** 1/33 active   **Queue:** {"cancelled": 42, "done": 1163, "failed": 3, "paused": 46, "queued": 11, "running": 2}   **Healthy lanes:** gemini-flash, gemini-flash-latest, gemini-flash38, gemini-gemini-flash-lite-latest, gemini-gemma26b, gemini-lite, gemini-lite31, groq-gptoss120b, groq-gptoss20b, groq-qwen27b, local3b, local4b

## Needs attention
- FACTORY CANARY FAILED at 1791452368.39757 (lane groq:openai/gpt-oss-120b): the factory itself, not a bot, is broken — see AUDIT factory.canary
- job 5d14608a test paused (logic)
- job 0458f029 repair paused (logic)
- job 6af00a36 repair paused (logic)
- job 510ea5e2 repair paused (logic)
- job c04521f6 repair paused (logic)
- job a1d92047 repair paused (logic)
- job d811bbf9 create paused (security)
- job d509e126 create paused (security)
- job 1826bc15 repair paused (logic)
- job 2a020aa6 repair paused (logic)
- job 5def33a0 repair paused (logic)
- job 8615298f repair paused (logic)
- job be8c781b repair paused (logic)
- job c3aed36d repair paused (logic)
- job 2ae8b6da repair paused (logic)
- job 9d53582f repair paused (logic)
- job 70dc72a1 repair paused (logic)
- job ce9c717b repair paused (logic)
- job d229874c repair paused (logic)
- job 0656e7cc repair paused (logic)
- job 24cabff1 repair paused (logic)
- job 02a7996c repair paused (logic)
- job 5d740c8e canary paused (security)
- job 6f03a51b repair paused (logic)
- job b98297bb repair paused (logic)
- job 5d2af791 repair paused (logic)
- job 409eb9fc repair paused (logic)
- job f5648160 repair paused (logic)
- job 42a8ce46 repair paused (logic)
- job 7e73f8b8 repair paused (logic)
- job 885a0ec2 run paused (logic)
- job d712cbbe canary paused (security)
- job 81018e13 repair paused (logic)
- job 1f6c487d repair paused (logic)
- job 03decd6e repair paused (logic)
- job 1e82a590 repair paused (logic)
- job 747aafa5 repair paused (logic)
- job 44d08ade repair paused (logic)
- job e141af82 repair paused (logic)
- job c7a3b266 canary paused (security)
- job 70811e2d repair paused (logic)
- job 21de43e4 canary paused (security)
- job f5e51726 repair paused (logic)
- job 52cb5c42 repair paused (logic)
- job b0d01597 repair paused (logic)
- job 0d3cdbe7 canary paused (security)
- bot 002 research-scout is testing
- bot 003 code-smith is testing
- bot 004 changelog-writer is testing
- bot 005 csv-quality-auditor is testing
- bot 006 json-to-markdown-table is testing
- bot 007 todo-extractor is testing
- bot 008 word-frequency-bot is testing
- bot 009 line-dedupe-bot is testing
- bot 011 word-frequency-counter is testing
- bot 012 csv-column-sum is testing
- bot 013 log-error-filter is testing
- bot 014 error-log-analyzer is testing
- bot 016 workspace-tidy-counter is testing
- bot 017 name-sorter is testing
- bot 018 csv-country-totals is testing
- bot 019 pytest-runner is testing
- bot 020 workspace-file-lister is testing
- bot 021 email-line-counter is testing
- bot 022 csv-refund-filter is testing
- bot 023 refund-summarizer is testing
- bot 024 pytest-runner-bot is testing
- bot 025 text-transformer is testing
- bot 026 sqlite-query-bot is testing
- bot 027 self-review-bot is testing
- bot 028 weekly-self-review is testing
- bot 029 bot-count-updater is testing
- bot 030 weekly-self-review-bot-counter is testing
- bot 032 weekly-self-review is testing
- bot 033 weekly-selfreview-count-bots is testing
- 1 retired / 1 paused bots (see Bots table)
- lane gemini-flash36 BLOCKED: tool_call_score decayed below 0.3
- lane or-ling-30-flash-sante BLOCKED: gone: {"error":{"message":"this model is unavailable for free. the paid version 
- ACTION REQUIRED (owner): provider:cerebras — set CEREBRAS_API_KEY (User env) after signing up: https://cloud.cerebras.ai (free tier ~1M tokens/day)
- ACTION REQUIRED (owner): provider:nvidia — set NVIDIA_API_KEY (User env) after signing up: https://build.nvidia.com (free ~40 rpm, tool-capable models)
- ACTION REQUIRED (owner): provider:mistral — set MISTRAL_API_KEY (User env) after signing up: https://console.mistral.ai (Experiment free tier)
- ACTION REQUIRED (owner): 12 free resources need a human signup/key — cerebras, cloudflare-r2, cloudflare-workers, cloudflare-workers-ai, google-cloud-run, hf-router… (docs/INFRA.md)
- DECISION (owner): 3 MCP server(s) sandbox-verified, on probation: mcp:crawlio-browser, mcp:mcp-sqlite-tools, mcp:playwright-mcp — `factory_worker.py approve-tool <id>` to make them grantable to bots, or leave them (nothing uses them)

## Bots
| id | name | status | verified | permissions |
|---|---|---|---|---|
| 001 | master | testing | UNVERIFIED | fs:read, fs:write, shell:workspace, net:search, net:fetch |
| 002 | research-scout | testing | UNVERIFIED | net:search, net:fetch, fs:read |
| 003 | code-smith | testing | UNVERIFIED | fs:write, shell:workspace |
| 004 | changelog-writer | testing | UNVERIFIED | fs:read, fs:write |
| 005 | csv-quality-auditor | testing | UNVERIFIED | fs:read, fs:write |
| 006 | json-to-markdown-table | testing | UNVERIFIED | fs:read, fs:write |
| 007 | todo-extractor | testing | UNVERIFIED | fs:read, fs:write |
| 008 | word-frequency-bot | testing | UNVERIFIED | fs:read, fs:write |
| 009 | line-dedupe-bot | testing | UNVERIFIED | fs:read, fs:write |
| 010 | dedupe-failover-probe | paused | INFERRED | fs:read, fs:write |
| 011 | word-frequency-counter | testing | UNVERIFIED | fs:read, fs:write |
| 012 | csv-column-sum | testing | UNVERIFIED | fs:read, fs:write |
| 013 | log-error-filter | testing | UNVERIFIED | fs:read, fs:write |
| 014 | error-log-analyzer | testing | UNVERIFIED | fs:read, fs:write |
| 015 | system-cleanup | retired | BLOCKED | shell:workspace |
| 016 | workspace-tidy-counter | testing | UNVERIFIED | fs:read, shell:workspace |
| 017 | name-sorter | testing | UNVERIFIED | fs:read, fs:write |
| 018 | csv-country-totals | testing | UNVERIFIED | fs:read, fs:write |
| 019 | pytest-runner | testing | UNVERIFIED | fs:read, fs:write, shell:workspace |
| 020 | workspace-file-lister | testing | UNVERIFIED | shell:workspace, fs:write |
| 021 | email-line-counter | testing | UNVERIFIED | fs:read, fs:write |
| 022 | csv-refund-filter | testing | UNVERIFIED | fs:read, fs:write |
| 023 | refund-summarizer | testing | UNVERIFIED | fs:read, fs:write |
| 024 | pytest-runner-bot | testing | UNVERIFIED | fs:read, fs:write, shell:workspace |
| 025 | text-transformer | testing | UNVERIFIED | fs:read, fs:write |
| 026 | sqlite-query-bot | testing | UNVERIFIED | fs:read, fs:write, mcp:mcp-sqlite3 |
| 027 | self-review-bot | testing | UNVERIFIED | fs:read, fs:write, net:search, net:fetch |
| 028 | weekly-self-review | testing | UNVERIFIED | fs:read, fs:write, net:search, net:fetch |
| 029 | bot-count-updater | testing | UNVERIFIED | fs:read, fs:write |
| 030 | weekly-self-review-bot-counter | testing | UNVERIFIED | fs:read, fs:write |
| 031 | weekly-self-review | active | VERIFIED | fs:read, fs:write |
| 032 | weekly-self-review | testing | UNVERIFIED | fs:read, fs:write, net:search, net:fetch |
| 033 | weekly-selfreview-count-bots | testing | UNVERIFIED | fs:read, fs:write |

## Jobs (24h)
| id | kind | state | att | class | bot | objective |
|---|---|---|---|---|---|---|
| dcbd97eb | test | done | 1 | - | 001 |  |
| 62d550ce | test | done | 1 | - | 001 |  |
| fae47e4f | test | done | 1 | - | 001 |  |
| d8bda1e9 | report | running | 1 | - | - |  |
| ab79dd5a | test | done | 1 | - | 001 |  |
| b55e8b34 | test | done | 1 | - | 001 |  |
| c13e8ff5 | test | done | 1 | - | 001 |  |
| 1eb9c40f | test | done | 2 | transient | 001 |  |
| 0e8ffbf4 | probe | done | 1 | - | - |  |
| 844700b5 | tick | done | 1 | - | - |  |
| 24b6cef5 | test | done | 1 | - | 001 |  |
| 9e61efc1 | test | done | 1 | - | 001 |  |
| 5a5b85cd | probe | done | 1 | - | - |  |
| 22c977d6 | probe | done | 1 | - | - |  |
| df9532da | tick | done | 1 | - | - |  |
| cb68d6f7 | probe | done | 1 | - | - |  |
| c440dca6 | monitor | done | 1 | - | - |  |
| 1e285eb7 | discover | done | 1 | - | - |  |
| 6a778c96 | discover | done | 1 | - | - |  |
| 7003d4dd | discover | done | 1 | - | - |  |
| c742c756 | discover | done | 1 | - | - |  |
| 7259ef61 | discover | done | 1 | - | - |  |
| 6a251af6 | discover | done | 1 | - | - |  |
| be435166 | test | done | 1 | - | 001 |  |
| 43e06b9c | test | done | 1 | - | 031 |  |
| ab5d1062 | test | done | 1 | - | 001 |  |
| 9aa0054e | test | done | 1 | - | 001 |  |
| 32fc3cea | test | done | 1 | - | 001 |  |
| a3c0bdb6 | test | done | 1 | - | 001 |  |
| 7a5370a7 | tick | done | 1 | - | - |  |
| 2bf3f44f | probe | done | 1 | - | - |  |
| 88ac2dd8 | test | done | 1 | - | 001 |  |
| 8453fea8 | test | done | 1 | - | 001 |  |
| 219a2f98 | test | done | 2 | transient | 001 |  |
| 3048facf | test | running | 2 | transient | 001 |  |
| cf5fe0c5 | test | queued | 0 | - | 001 |  |
| 1f4dcd39 | test | queued | 0 | - | 001 |  |
| 8f5a6c18 | tick | done | 1 | - | - |  |
| f8c017c1 | probe | done | 1 | - | - |  |
| 35e93443 | discover | done | 1 | - | - |  |
| 7deaadb5 | discover | done | 1 | - | - |  |
| 08611fe2 | discover | done | 1 | - | - |  |
| 532fd488 | discover | done | 1 | - | - |  |
| 8acb0163 | discover | done | 1 | - | - |  |
| f3dbc5c1 | discover | done | 1 | - | - |  |
| b24ff203 | test | queued | 0 | - | 001 |  |
| 5fd9d18c | test | done | 1 | - | 001 |  |
| d64d5f43 | test | queued | 0 | - | 001 |  |
| f6a97e54 | tick | done | 1 | - | - |  |
| 3b16ced2 | probe | done | 1 | - | - |  |
| 6e21e735 | test | queued | 0 | - | 001 |  |
| 909d4e4b | test | queued | 0 | - | 001 |  |
| d9e6e57e | test | queued | 0 | - | 001 |  |
| d13e7377 | test | queued | 0 | - | 001 |  |
| f9604c42 | tick | done | 1 | - | - |  |
| 03b06039 | probe | done | 1 | - | - |  |
| 6b52f660 | probe | done | 1 | - | - |  |
| ff999b86 | probe | done | 1 | - | - |  |
| 29c2f4f1 | probe | done | 1 | - | - |  |
| 675ecaff | probe | done | 1 | - | - |  |
| fc108045 | probe | done | 1 | - | - |  |
| 5bf7d78e | probe | done | 1 | - | - |  |
| d2e1729a | test | queued | 0 | - | 001 |  |
| 549088bf | tick | done | 1 | - | - |  |
| e6aca474 | probe | done | 1 | - | - |  |
| c29eaa2f | discover | done | 1 | - | - |  |
| 33a31532 | discover | done | 1 | - | - |  |
| e936f60b | discover | done | 1 | - | - |  |
| 39daa754 | discover | done | 1 | - | - |  |
| 31ae098a | discover | done | 1 | - | - |  |
| f5737aa7 | discover | done | 1 | - | - |  |
| 87def55d | tick | queued | 0 | - | - |  |
| a6976a83 | probe | queued | 0 | - | - |  |
| cd4c40bf | discover | done | 1 | - | - |  |
| 5d58fd62 | discover | done | 1 | - | - |  |
| 9611c951 | discover | done | 1 | - | - |  |
| 2b21b01f | discover | done | 1 | - | - |  |
| 9f3b0120 | discover | done | 1 | - | - |  |
| 4311cd1f | discover | done | 1 | - | - |  |

## Lane quality (D-050, reference suite, rolling window)
| lane | score | secs | runs |
|---|---|---|---|
| or-apodex-11-mini | 4/4 | 49 | 1 |
| groq-gptoss120b | 9/9 | 77 | 3 |
| or-ling-30-flash-sante | 4/4 | 89 | 1 |
| groq-gptoss20b | 4/4 | 106 | 1 |
| or-nemotron-35-lightning | 2/2 | 564 | 1 |
| gemini-gemma26b | 5/6 | 65 | 2 |
| gemini-gemini-flash-lite-latest | 5/8 | 44 | 2 |
| gemini-lite31 | 4/8 | 53 | 2 |
| gemini-flash36 | 2/4 | 63 | 1 |
| gemini-flash-latest | 2/4 | 72 | 1 |
| groq-qwen27b | 4/8 | 107 | 2 |
| gemini-flash38 | 2/4 | 128 | 1 |
| gemini-flash | 2/4 | 180 | 1 |
| gemini-lite | 3/8 | 326 | 2 |

## Lanes
| id | provider | state | latency s |
|---|---|---|---|
| gemini-flash | gemini | ok | 6.23 |
| gemini-flash-latest | gemini | ok | 3.28 |
| gemini-flash36 | gemini | BLOCKED | 3.25 |
| gemini-flash38 | gemini | ok | 4.1 |
| gemini-gemini-flash-lite-latest | gemini | ok | 1.43 |
| gemini-gemma26b | gemini | ok | 2.88 |
| gemini-lite | gemini | ok | 1.93 |
| gemini-lite31 | gemini | ok | 1.76 |
| groq-gptoss120b | groq | ok | 1.82 |
| groq-gptoss20b | groq | ok | 1.38 |
| groq-qwen27b | groq | ok | 1.89 |
| local3b | ollama | ok | - |
| local4b | ollama | ok | - |
| or-apodex-11-mini | openrouter | cooldown | 2.35 |
| or-ling-30-flash-sante | openrouter | BLOCKED | 1.78 |
| or-nemotron-35-lightning | openrouter | cooldown | 4.7 |
| ovh-gptoss20b | custom | BLOCKED | - |
| ovh-llama70b | custom | BLOCKED | - |
| ovh-mistral24b | custom | BLOCKED | - |
