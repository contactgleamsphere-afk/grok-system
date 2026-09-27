# FACTORY STATUS — 2026-09-27T01:59:54

**Worker:** running — last worker activity 0 min ago

**Bots:** 23/27 active   **Queue:** {"cancelled": 42, "done": 359, "paused": 2, "queued": 2, "running": 2}   **Healthy lanes:** gemini-flash36, gemini-flash38, gemini-gemini-flash-lite-latest, gemini-gemma26b, gemini-lite, gemini-lite31, groq-gptoss120b, groq-gptoss20b, groq-qwen27b, local3b, local4b, or-ling-30-flash-fin, or-ling-30-flash-sante, or-nemotron-35-lightning

## Needs attention
- FACTORY CANARY FAILED at 1790384456.57993 (lane gemini:gemini-3.1-flash-lite): the factory itself, not a bot, is broken — see AUDIT factory.canary
- job 5d14608a test paused (logic)
- job 0458f029 repair paused (logic)
- bot 002 research-scout is testing
- 1 retired / 1 paused bots (see Bots table)
- lane or-nex-n25-pro BLOCKED: gone: {"error":{"message":"no endpoints found for nex-agi/nex-n2.5-pro:free.","c
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
| 016 | workspace-tidy-counter | active | VERIFIED | fs:read, shell:workspace |
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
| 027 | self-review-bot | active | VERIFIED | fs:read, fs:write, net:search, net:fetch |

## Jobs (24h)
| id | kind | state | att | class | bot | objective |
|---|---|---|---|---|---|---|
| 268e463f | tick | done | 1 | - | - |  |
| c632d578 | report | running | 1 | - | - |  |
| 15dcb4d1 | canary | done | 1 | - | - |  |
| afc49d7c | probe | done | 1 | - | - |  |
| 9eb7524a | test | running | 1 | - | 001 |  |
| eeba28ae | tick | done | 1 | - | - |  |
| 5854ee45 | probe | queued | 0 | - | - |  |
| afa33da8 | run | done | 1 | - | 018 |  |
| 85375329 | tick | queued | 0 | - | - |  |

## Lane quality (D-050, reference suite, rolling window)
| lane | score | secs | runs |
|---|---|---|---|
| gemini-gemini-flash-lite-latest | 4/4 | 42 | 1 |
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
| gemini-flash | gemini | error | 4.91 |
| gemini-flash36 | gemini | ok | 2.32 |
| gemini-flash38 | gemini | ok | 3.84 |
| gemini-gemini-flash-lite-latest | gemini | ok | 1.03 |
| gemini-gemma26b | gemini | ok | 1.11 |
| gemini-lite | gemini | ok | 0.8 |
| gemini-lite31 | gemini | ok | 1.21 |
| groq-gptoss120b | groq | ok | 1.94 |
| groq-gptoss20b | groq | ok | 1.13 |
| groq-qwen27b | groq | ok | 0.42 |
| local3b | ollama | ok | - |
| local4b | ollama | ok | - |
| or-ling-30-flash-fin | openrouter | ok | 1.39 |
| or-ling-30-flash-sante | openrouter | ok | 1.22 |
| or-nemotron-35-lightning | openrouter | ok | 1.56 |
| or-nex-n25-pro | openrouter | BLOCKED | 2.18 |
| or-qwen27b | openrouter | cooldown | 1.64 |
| ovh-gptoss20b | custom | BLOCKED | - |
| ovh-llama70b | custom | BLOCKED | - |
| ovh-mistral24b | custom | BLOCKED | - |
