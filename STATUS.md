# FACTORY STATUS — 2026-10-07T15:36:01

**Worker:** running — last worker activity 0 min ago

**Bots:** 3/33 active   **Queue:** {"cancelled": 42, "done": 1033, "failed": 3, "paused": 44, "queued": 8, "running": 2}   **Healthy lanes:** gemini-gemini-flash-lite-latest, gemini-gemma26b, gemini-lite, gemini-lite31, groq-gptoss120b, groq-gptoss20b, groq-qwen27b, local3b, local4b, or-apodex-11-mini, or-ling-30-flash-sante, or-nemotron-35-lightning

## Needs attention
- FACTORY CANARY FAILED at 1791288262.81003 (lane groq:openai/gpt-oss-120b): the factory itself, not a bot, is broken — see AUDIT factory.canary
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
- bot 029 bot-count-updater is testing
- bot 030 weekly-self-review-bot-counter is testing
- bot 032 weekly-self-review is testing
- 1 retired / 1 paused bots (see Bots table)
- lane gemini-flash BLOCKED: 3 consecutive errors: [{ "error": { "code": 503, "message": "this model is curre
- lane gemini-flash-latest BLOCKED: 3 consecutive errors: TimeoutError
- lane gemini-flash36 BLOCKED: 3 consecutive errors: [{ "error": { "code": 503, "message": "this model is curre
- lane or-qwen27b BLOCKED: gone: {"error":{"message":"this model is unavailable for free. the paid version 
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
| 028 | weekly-self-review | active | VERIFIED | fs:read, fs:write, net:search, net:fetch |
| 029 | bot-count-updater | testing | UNVERIFIED | fs:read, fs:write |
| 030 | weekly-self-review-bot-counter | testing | UNVERIFIED | fs:read, fs:write |
| 031 | weekly-self-review | active | VERIFIED | fs:read, fs:write |
| 032 | weekly-self-review | testing | UNVERIFIED | fs:read, fs:write, net:search, net:fetch |
| 033 | weekly-selfreview-count-bots | active | VERIFIED | fs:read, fs:write |

## Jobs (24h)
| id | kind | state | att | class | bot | objective |
|---|---|---|---|---|---|---|
| 453de9e9 | report | running | 1 | - | - |  |
| 9676251c | test | done | 1 | - | 001 |  |
| eb2b6405 | test | done | 1 | - | 001 |  |
| 41923cc5 | test | done | 1 | - | 001 |  |
| f9c5d9ce | test | done | 1 | - | 001 |  |
| d9f18eed | probe | done | 1 | - | - |  |
| 074d01d0 | tick | done | 1 | - | - |  |
| 7f355c4b | test | done | 1 | - | 001 |  |
| 2a4bed6b | test | done | 1 | - | 001 |  |
| 59e6d0c1 | test | done | 1 | - | 001 |  |
| b0498475 | test | done | 1 | - | 001 |  |
| 48fc3c01 | probe | done | 1 | - | - |  |
| 024aa1df | discover | done | 1 | - | - |  |
| ee737074 | discover | done | 1 | - | - |  |
| 51997579 | discover | done | 1 | - | - |  |
| 8e0d8bb8 | discover | done | 1 | - | - |  |
| da181f18 | discover | done | 1 | - | - |  |
| 758a94a4 | discover | done | 1 | - | - |  |
| 8db17bc2 | tick | done | 1 | - | - |  |
| a01459ef | test | done | 1 | - | 001 |  |
| 7313be42 | test | done | 1 | - | 001 |  |
| 90523c21 | probe | done | 1 | - | - |  |
| 8e877c8d | discover | done | 1 | - | - |  |
| 739dd74c | discover | done | 1 | - | - |  |
| 74dcb2a5 | discover | done | 1 | - | - |  |
| e59c0b07 | discover | done | 1 | - | - |  |
| a3f68afa | discover | done | 1 | - | - |  |
| afd7e099 | discover | done | 1 | - | - |  |
| d7038ac8 | tick | done | 1 | - | - |  |
| 79387b5d | test | done | 1 | - | 001 |  |
| 0a2edb66 | test | done | 1 | - | 001 |  |
| 77246653 | test | done | 1 | - | 001 |  |
| 007adb20 | test | done | 1 | - | 001 |  |
| 70e885e4 | probe | done | 1 | - | - |  |
| dab76f62 | discover | done | 1 | - | - |  |
| 60bb558d | discover | done | 1 | - | - |  |
| e7fa41fc | discover | done | 1 | - | - |  |
| ad36a460 | discover | done | 1 | - | - |  |
| 2021e169 | discover | done | 1 | - | - |  |
| ac3fc65d | discover | done | 1 | - | - |  |
| 70f255b2 | tick | done | 1 | - | - |  |
| 66e5d795 | test | done | 1 | - | 001 |  |
| 0a38da93 | test | done | 1 | - | 001 |  |
| 00a4f8d4 | test | done | 1 | - | 001 |  |
| 90e0f175 | probe | done | 1 | - | - |  |
| 52127838 | tick | done | 1 | - | - |  |
| 879e06a3 | test | done | 2 | transient | 001 |  |
| 989112db | test | running | 1 | - | 001 |  |
| 8083faff | test | queued | 0 | - | 001 |  |
| 5410d886 | probe | done | 1 | - | - |  |
| 90ce8b53 | tick | done | 1 | - | - |  |
| 41a32998 | test | queued | 0 | - | 001 |  |
| e294457f | test | queued | 0 | - | 001 |  |
| 1b5eae2b | test | queued | 0 | - | 001 |  |
| 3200a504 | test | queued | 0 | - | 001 |  |
| 1c85b500 | probe | done | 1 | - | - |  |
| 4ce09cb7 | tick | done | 1 | - | - |  |
| f8e1f6e5 | probe | done | 1 | - | - |  |
| 9f252969 | discover | done | 1 | - | - |  |
| 4cea3d1b | discover | done | 1 | - | - |  |
| 8f09c864 | discover | done | 1 | - | - |  |
| 4b8b103b | discover | done | 1 | - | - |  |
| ca675b53 | discover | done | 1 | - | - |  |
| d498f52c | discover | done | 1 | - | - |  |
| 35b91d1a | tick | queued | 0 | - | - |  |
| 762a5e34 | probe | queued | 0 | - | - |  |
| 26c0efd9 | discover | done | 1 | - | - |  |
| 17c55e79 | discover | done | 1 | - | - |  |
| e9f39103 | discover | done | 1 | - | - |  |
| fb296dd4 | discover | done | 1 | - | - |  |
| 365a4bf4 | discover | done | 1 | - | - |  |
| a1c8b352 | discover | done | 1 | - | - |  |
| 328c36fa | test | queued | 0 | - | 001 |  |

## Lane quality (D-050, reference suite, rolling window)
| lane | score | secs | runs |
|---|---|---|---|
| gemini-gemini-flash-lite-latest | 4/4 | 42 | 1 |
| or-apodex-11-mini | 4/4 | 49 | 1 |
| gemini-lite31 | 4/4 | 73 | 1 |
| or-ling-30-flash-sante | 4/4 | 89 | 1 |
| groq-gptoss120b | 8/8 | 99 | 2 |
| groq-gptoss20b | 4/4 | 106 | 1 |
| or-nemotron-35-lightning | 2/2 | 564 | 1 |
| gemini-gemma26b | 5/6 | 65 | 2 |
| or-qwen27b | 2/3 | 58 | 1 |
| gemini-flash36 | 2/4 | 63 | 1 |
| gemini-flash-latest | 2/4 | 72 | 1 |
| groq-qwen27b | 4/8 | 107 | 2 |
| gemini-flash38 | 2/4 | 128 | 1 |
| gemini-flash | 2/4 | 180 | 1 |
| gemini-lite | 1/4 | 618 | 1 |

## Lanes
| id | provider | state | latency s |
|---|---|---|---|
| gemini-flash | gemini | BLOCKED | 5.82 |
| gemini-flash-latest | gemini | BLOCKED | 5.43 |
| gemini-flash36 | gemini | BLOCKED | 7.85 |
| gemini-flash38 | gemini | error | 4.7 |
| gemini-gemini-flash-lite-latest | gemini | ok | 1.27 |
| gemini-gemma26b | gemini | ok | 2.25 |
| gemini-lite | gemini | ok | 0.92 |
| gemini-lite31 | gemini | ok | 1.23 |
| groq-gptoss120b | groq | ok | 3.38 |
| groq-gptoss20b | groq | ok | 0.71 |
| groq-qwen27b | groq | ok | 0.38 |
| local3b | ollama | ok | - |
| local4b | ollama | ok | - |
| or-apodex-11-mini | openrouter | ok | 1.65 |
| or-ling-30-flash-sante | openrouter | ok | 1.54 |
| or-nemotron-35-lightning | openrouter | ok | 7.54 |
| or-qwen27b | openrouter | BLOCKED | 3.69 |
| ovh-gptoss20b | custom | BLOCKED | - |
| ovh-llama70b | custom | BLOCKED | - |
| ovh-mistral24b | custom | BLOCKED | - |
