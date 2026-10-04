# FACTORY STATUS — 2026-10-04T13:44:10

**Worker:** running — last worker activity 0 min ago

**Bots:** 3/30 active   **Queue:** {"cancelled": 42, "done": 858, "failed": 3, "paused": 41, "queued": 7, "running": 2}   **Healthy lanes:** gemini-flash, gemini-flash-latest, gemini-flash36, gemini-flash38, gemini-gemini-flash-lite-latest, gemini-gemma26b, gemini-lite, gemini-lite31, groq-gptoss120b, groq-gptoss20b, groq-qwen27b, local3b, local4b, or-apodex-11-mini, or-ling-30-flash-sante, or-nemotron-35-lightning

## Needs attention
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
- 1 retired / 1 paused bots (see Bots table)
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
| 029 | bot-count-updater | active | VERIFIED | fs:read, fs:write |
| 030 | weekly-self-review-bot-counter | active | VERIFIED | fs:read, fs:write |

## Jobs (24h)
| id | kind | state | att | class | bot | objective |
|---|---|---|---|---|---|---|
| 091fe87e | report | running | 1 | - | - |  |
| 7791cfd1 | test | done | 1 | - | 001 |  |
| f4c035f5 | test | done | 1 | - | 001 |  |
| b2987a9a | test | done | 1 | - | 001 |  |
| 91683a5e | test | done | 1 | - | 001 |  |
| 4014c5d9 | test | done | 1 | - | 001 |  |
| 30d2a0d2 | probe | done | 1 | - | - |  |
| 47e72b7d | tick | done | 1 | - | - |  |
| c4ba12f8 | test | done | 1 | - | 001 |  |
| ae553c47 | probe | done | 1 | - | - |  |
| 6b090e08 | tick | done | 1 | - | - |  |
| 1811ab9e | test | done | 1 | - | 001 |  |
| c9049357 | probe | done | 1 | - | - |  |
| 9b82e36b | tick | done | 1 | - | - |  |
| 9bce9ff8 | test | done | 1 | - | 001 |  |
| ca238808 | test | done | 1 | - | 001 |  |
| 70406b7d | test | done | 1 | - | 001 |  |
| 28936172 | test | done | 1 | - | 001 |  |
| b160cb81 | probe | done | 1 | - | - |  |
| 34937a4e | discover | done | 1 | - | - |  |
| 4feb3742 | discover | done | 1 | - | - |  |
| 33306e02 | discover | done | 1 | - | - |  |
| 3a5ef1c6 | discover | done | 1 | - | - |  |
| e38dbc3f | discover | done | 1 | - | - |  |
| dfffb806 | discover | done | 1 | - | - |  |
| 7c4c7496 | tick | done | 1 | - | - |  |
| bdd006b0 | test | done | 1 | - | 001 |  |
| 0013387b | test | done | 1 | - | 001 |  |
| 3e606ba8 | probe | done | 1 | - | - |  |
| f5fee259 | tick | done | 1 | - | - |  |
| e203c351 | test | done | 1 | - | 001 |  |
| d423a523 | test | done | 1 | - | 001 |  |
| 7054866c | test | done | 1 | - | 001 |  |
| 8de380de | probe | done | 1 | - | - |  |
| 5d0438a1 | discover | done | 1 | - | - |  |
| 7b57e6cb | discover | done | 1 | - | - |  |
| 96ca3eae | discover | done | 1 | - | - |  |
| f7ccc654 | discover | done | 1 | - | - |  |
| 8bb50c87 | discover | done | 1 | - | - |  |
| 10db6ef6 | discover | done | 1 | - | - |  |
| 2b1c3328 | tick | done | 1 | - | - |  |
| dcf400b5 | test | failed | 3 | transient | 001 |  |
| cd511712 | test | done | 3 | transient | 001 |  |
| 9452394f | test | running | 1 | - | 001 |  |
| ab903e40 | probe | done | 1 | - | - |  |
| c5c8de46 | tick | done | 1 | - | - |  |
| 29eba64b | test | queued | 0 | - | 001 |  |
| cc838b03 | test | queued | 0 | - | 001 |  |
| d071eb0a | probe | done | 1 | - | - |  |
| fdb14c2e | tick | done | 1 | - | - |  |
| a38a7043 | test | queued | 0 | - | 001 |  |
| b2e299d3 | probe | done | 1 | - | - |  |
| 6960ee36 | tick | done | 1 | - | - |  |
| eddcd50c | probe | done | 1 | - | - |  |
| 83500f74 | tick | done | 1 | - | - |  |
| aa91a845 | test | queued | 0 | - | 001 |  |
| 3d977ea8 | probe | queued | 0 | - | - |  |
| e3e27be7 | monitor | queued | 0 | - | - |  |
| b3e37bd2 | tick | queued | 0 | - | - |  |

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
| gemini-gemma26b | 3/4 | 73 | 1 |
| or-qwen27b | 2/3 | 58 | 1 |
| gemini-flash36 | 2/4 | 63 | 1 |
| gemini-flash-latest | 2/4 | 72 | 1 |
| gemini-flash38 | 2/4 | 128 | 1 |
| groq-qwen27b | 2/4 | 147 | 1 |
| gemini-flash | 2/4 | 180 | 1 |
| gemini-lite | 1/4 | 618 | 1 |

## Lanes
| id | provider | state | latency s |
|---|---|---|---|
| gemini-flash | gemini | ok | 5.72 |
| gemini-flash-latest | gemini | ok | 3.84 |
| gemini-flash36 | gemini | ok | 2.46 |
| gemini-flash38 | gemini | ok | 4.58 |
| gemini-gemini-flash-lite-latest | gemini | ok | 1.08 |
| gemini-gemma26b | gemini | ok | 1.09 |
| gemini-lite | gemini | ok | 0.83 |
| gemini-lite31 | gemini | ok | 5.08 |
| groq-gptoss120b | groq | ok | 0.84 |
| groq-gptoss20b | groq | ok | 0.63 |
| groq-qwen27b | groq | ok | 0.4 |
| local3b | ollama | ok | - |
| local4b | ollama | ok | - |
| or-apodex-11-mini | openrouter | ok | 1.62 |
| or-ling-30-flash-sante | openrouter | ok | 1.19 |
| or-nemotron-35-lightning | openrouter | ok | 1.85 |
| or-qwen27b | openrouter | cooldown | 13.09 |
| ovh-gptoss20b | custom | BLOCKED | - |
| ovh-llama70b | custom | BLOCKED | - |
| ovh-mistral24b | custom | BLOCKED | - |
