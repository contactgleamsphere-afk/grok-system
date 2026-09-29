# FACTORY STATUS — 2026-09-29T18:04:32

**Worker:** running — last worker activity 0 min ago

**Bots:** 20/27 active   **Queue:** {"cancelled": 42, "done": 515, "paused": 8, "queued": 24, "running": 2}   **Healthy lanes:** gemini-gemini-flash-lite-latest, gemini-gemma26b, gemini-lite, groq-gptoss120b, groq-gptoss20b, groq-qwen27b, local3b, local4b, or-ling-30-flash-sante

## Needs attention
- OUTAGE in the last 24 h: down 2075 min from 2026-09-28T07:26 — power loss / battery flat (kernel-power 41)
- job 5d14608a test paused (logic)
- job 0458f029 repair paused (logic)
- job 6af00a36 repair paused (logic)
- job 510ea5e2 repair paused (logic)
- job c04521f6 repair paused (logic)
- job a1d92047 repair paused (logic)
- job d811bbf9 create paused (security)
- job d509e126 create paused (security)
- bot 002 research-scout is testing
- bot 004 changelog-writer is testing
- bot 020 workspace-file-lister is testing
- bot 021 email-line-counter is testing
- 1 retired / 1 paused bots (see Bots table)
- lane or-ling-30-flash-fin BLOCKED: gone: {"error":{"message":"this model is unavailable for free. the paid version 
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
| 003 | code-smith | active | VERIFIED | fs:write, shell:workspace |
| 004 | changelog-writer | testing | UNVERIFIED | fs:read, fs:write |
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
| 016 | workspace-tidy-counter | active | VERIFIED | fs:read, shell:workspace |
| 017 | name-sorter | active | VERIFIED | fs:read, fs:write |
| 018 | csv-country-totals | active | VERIFIED | fs:read, fs:write |
| 019 | pytest-runner | active | VERIFIED | fs:read, fs:write, shell:workspace |
| 020 | workspace-file-lister | testing | UNVERIFIED | shell:workspace, fs:write |
| 021 | email-line-counter | testing | UNVERIFIED | fs:read, fs:write |
| 022 | csv-refund-filter | active | VERIFIED | fs:read, fs:write |
| 023 | refund-summarizer | active | VERIFIED | fs:read, fs:write |
| 024 | pytest-runner-bot | active | VERIFIED | fs:read, fs:write, shell:workspace |
| 025 | text-transformer | active | VERIFIED | fs:read, fs:write |
| 026 | sqlite-query-bot | active | VERIFIED | fs:read, fs:write, mcp:mcp-sqlite3 |
| 027 | self-review-bot | active | VERIFIED | fs:read, fs:write, net:search, net:fetch |

## Jobs (24h)
| id | kind | state | att | class | bot | objective |
|---|---|---|---|---|---|---|
| 934b7127 | report | running | 1 | - | - |  |
| fc453a3f | probe | done | 1 | - | - |  |
| 81cad91a | tick | done | 1 | - | - |  |
| 5013c9f9 | test | running | 1 | - | 001 |  |
| c6ebd328 | monitor | done | 1 | - | - |  |
| 4f6d66a5 | probe | queued | 0 | - | - |  |
| 9b18bfe0 | run | done | 1 | - | 018 |  |
| c256f1f3 | run | done | 1 | - | 027 |  |
| 7f41dddc | tick | queued | 0 | - | - |  |
| b62be530 | discover | done | 1 | - | - |  |
| c9e9f708 | discover | done | 1 | - | - |  |
| feed78f0 | discover | done | 1 | - | - |  |
| 00a18cc0 | discover | done | 1 | - | - |  |
| a237fa20 | discover | done | 1 | - | - |  |
| de32e89e | discover | done | 1 | - | - |  |
| 579491c3 | test | queued | 0 | - | 001 |  |
| 1ecb9227 | test | queued | 0 | - | 003 |  |
| 0f59f40f | test | queued | 0 | - | 005 |  |
| 09146563 | test | queued | 0 | - | 006 |  |
| 0f19ad75 | test | queued | 0 | - | 007 |  |
| 96e43656 | test | queued | 0 | - | 008 |  |
| 09ce9ce4 | test | queued | 0 | - | 009 |  |
| e6462e61 | test | queued | 0 | - | 011 |  |
| 8eec6c54 | test | queued | 0 | - | 012 |  |
| 0969955b | test | queued | 0 | - | 013 |  |
| 7ce257a8 | test | queued | 0 | - | 014 |  |
| 598a5cc4 | test | queued | 0 | - | 016 |  |
| fd26f12c | test | queued | 0 | - | 017 |  |
| 37ca8049 | test | queued | 0 | - | 018 |  |
| f2bb4b62 | test | queued | 0 | - | 019 |  |
| bb48c3f9 | test | queued | 0 | - | 022 |  |
| 6a59bbe3 | test | queued | 0 | - | 023 |  |
| 5929288f | test | queued | 0 | - | 024 |  |
| 65e0de3b | test | queued | 0 | - | 025 |  |
| 30f205bc | test | queued | 0 | - | 026 |  |
| 4da83d39 | test | queued | 0 | - | 027 |  |

## Lane quality (D-050, reference suite, rolling window)
| lane | score | secs | runs |
|---|---|---|---|
| gemini-gemini-flash-lite-latest | 4/4 | 42 | 1 |
| gemini-lite31 | 4/4 | 73 | 1 |
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
| gemini-flash | gemini | error | 2.4 |
| gemini-flash36 | gemini | no_tool_call | 2.03 |
| gemini-flash38 | gemini | error | 3.4 |
| gemini-gemini-flash-lite-latest | gemini | ok | 1.12 |
| gemini-gemma26b | gemini | ok | 1.51 |
| gemini-lite | gemini | ok | 1.02 |
| gemini-lite31 | gemini | error | 2.45 |
| groq-gptoss120b | groq | ok | 0.8 |
| groq-gptoss20b | groq | ok | 1.27 |
| groq-qwen27b | groq | ok | 0.73 |
| local3b | ollama | ok | - |
| local4b | ollama | ok | - |
| or-ling-30-flash-fin | openrouter | BLOCKED | 0.81 |
| or-ling-30-flash-sante | openrouter | ok | 1.53 |
| or-nemotron-35-lightning | openrouter | error | 15.26 |
| or-qwen27b | openrouter | cooldown | 1.78 |
| ovh-gptoss20b | custom | BLOCKED | - |
| ovh-llama70b | custom | BLOCKED | - |
| ovh-mistral24b | custom | BLOCKED | - |
