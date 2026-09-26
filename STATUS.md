# FACTORY STATUS — 2026-09-26T01:12:13

**Worker:** running — last worker activity 0 min ago

**Bots:** 24/26 active   **Queue:** {"cancelled": 42, "done": 319, "paused": 1, "queued": 2, "running": 1}   **Healthy lanes:** gemini-flash, gemini-flash36, gemini-gemini-flash-lite-latest, gemini-gemma26b, gemini-lite, gemini-lite31, groq-gptoss120b, groq-gptoss20b, groq-qwen27b, local3b, local4b

## Needs attention
- job 5d14608a test paused (logic)
- 1 retired / 1 paused bots (see Bots table)
- lane or-ling-30-flash-vl BLOCKED: gone: {"error":{"message":"this model is unavailable for free. the paid version 
- lane or-nemotron-35-lightning BLOCKED: failed probation: error
- lane or-nex-n25-pro BLOCKED: gone: {"error":{"message":"no endpoints found for nex-agi/nex-n2.5-pro:free.","c
- ACTION REQUIRED (owner): provider:cerebras — set CEREBRAS_API_KEY (User env) after signing up: https://cloud.cerebras.ai (free tier ~1M tokens/day)
- ACTION REQUIRED (owner): provider:nvidia — set NVIDIA_API_KEY (User env) after signing up: https://build.nvidia.com (free ~40 rpm, tool-capable models)
- ACTION REQUIRED (owner): provider:mistral — set MISTRAL_API_KEY (User env) after signing up: https://console.mistral.ai (Experiment free tier)
- ACTION REQUIRED (owner): 12 free resources need a human signup/key — cerebras, cloudflare-r2, cloudflare-workers, cloudflare-workers-ai, google-cloud-run, hf-router… (docs/INFRA.md)
- DECISION (owner): 3 MCP server(s) sandbox-verified, on probation: mcp:crawlio-browser, mcp:mcp-sqlite-tools, mcp:playwright-mcp — `factory_worker.py approve-tool <id>` to make them grantable to bots, or leave them (nothing uses them)

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

## Jobs (24h)
| id | kind | state | att | class | bot | objective |
|---|---|---|---|---|---|---|
| e7744308 | probe | done | 1 | - | - |  |
| 190e3258 | tick | done | 1 | - | - |  |
| c858bfee | tooldisc | done | 1 | - | - |  |
| 463bbc9b | report | running | 1 | - | - |  |
| 6ba4e1dc | bench | done | 1 | - | - |  |
| 1b095896 | canary | done | 1 | - | - |  |
| de1d7fdc | monitor | done | 1 | - | - |  |
| c22c4f11 | test | done | 1 | - | 001 |  |
| 3bb0fc5b | test | done | 1 | - | 002 |  |
| 080bdd3e | test | done | 1 | - | 003 |  |
| 7591a1b5 | test | done | 1 | - | 004 |  |
| f649f932 | test | done | 1 | - | 005 |  |
| 5d14608a | test | paused | 1 | logic | 006 |  |
| 5d804e5d | test | done | 1 | - | 007 |  |
| 8f56eb65 | test | done | 1 | - | 008 |  |
| bd7cfb9e | test | done | 1 | - | 009 |  |
| 8dac341b | test | done | 1 | - | 011 |  |
| 2cb15941 | test | done | 1 | - | 012 |  |
| 31459526 | test | done | 1 | - | 013 |  |
| 667ce093 | test | done | 1 | - | 014 |  |
| 4b8fb54e | test | done | 1 | - | 016 |  |
| 5ba4ca8c | test | done | 1 | - | 017 |  |
| e5ef19df | test | done | 1 | - | 018 |  |
| 13956caf | test | done | 1 | - | 019 |  |
| 3b53fab8 | test | done | 1 | - | 020 |  |
| 72522ac3 | test | done | 1 | - | 021 |  |
| 2332bee3 | test | done | 1 | - | 022 |  |
| 35e53778 | test | done | 1 | - | 023 |  |
| e766a89e | test | done | 1 | - | 024 |  |
| e3d0b490 | test | done | 1 | - | 025 |  |
| 3f73d2dd | test | done | 1 | - | 026 |  |
| abe5c895 | repair | done | 1 | - | 002 |  |
| 0fe79cdf | repair | done | 2 | - | 003 |  |
| 29346aa8 | repair | done | 1 | - | 004 |  |
| 6f04db95 | probe | done | 1 | - | - |  |
| abed8a6c | tick | done | 1 | - | - |  |
| 738a787a | discover | done | 1 | - | - |  |
| 55ab81e6 | discover | done | 1 | - | - |  |
| c7800973 | discover | done | 1 | - | - |  |
| cbe38d31 | discover | done | 1 | - | - |  |
| 99ef519c | discover | done | 1 | - | - |  |
| c0780098 | discover | done | 1 | - | - |  |
| 1952fb1c | selfpatch | done | 1 | - | - |  |
| c3cae46b | test | done | 1 | - | 013 |  |
| cc163779 | repair | cancelled | 1 | logic | 016 |  |
| 88222656 | rearchitect | done | 1 | - | 016 |  |
| 7847f8ec | test | done | 1 | - | 014 |  |
| 9b60274b | repair | done | 1 | - | 017 |  |
| 509087ef | probe | done | 1 | - | - |  |
| 5866157b | discover | done | 1 | - | - |  |
| 71d0bcfc | discover | done | 1 | - | - |  |
| 9b42f1aa | discover | done | 1 | - | - |  |
| 52fea279 | discover | done | 1 | - | - |  |
| 279f51c7 | discover | done | 1 | - | - |  |
| d540257b | discover | done | 1 | - | - |  |
| 586e9f0e | tick | done | 1 | - | - |  |
| 3d281d06 | test | done | 1 | - | 020 |  |
| d62f34ea | test | done | 1 | - | 021 |  |
| 321d882a | probe | done | 1 | - | - |  |
| 5249b5ec | tick | done | 1 | - | - |  |
| 9c18c9e9 | repair | done | 1 | - | 013 |  |
| 03fe2791 | probe | done | 1 | - | - |  |
| dae5c79f | run | done | 1 | - | 018 |  |
| e354bd05 | tick | done | 1 | - | - |  |
| a35b45be | test | done | 2 | - | 020 |  |
| 0a541bde | probe | done | 1 | - | - |  |
| e1e4c7f4 | tick | done | 1 | - | - |  |
| 4f127831 | probe | done | 1 | - | - |  |
| b7558c0f | tick | done | 1 | - | - |  |
| 426bd52b | discover | done | 1 | - | - |  |
| 624ec5f9 | discover | done | 1 | - | - |  |
| 29f3da03 | discover | done | 1 | - | - |  |
| a3514a3e | discover | done | 1 | - | - |  |
| c14ad4dd | discover | done | 1 | - | - |  |
| 23979c6a | discover | done | 1 | - | - |  |
| 865a2980 | probe | done | 1 | - | - |  |
| 96ccf58b | probe | done | 1 | - | - |  |
| 54829a12 | tick | done | 1 | - | - |  |
| 80e90b9b | probe | done | 1 | - | - |  |
| 134bba89 | discover | done | 1 | - | - |  |
| 01537a5d | discover | done | 1 | - | - |  |
| 3fa27047 | discover | done | 1 | - | - |  |
| 2bbe411d | discover | done | 1 | - | - |  |
| a7cf454b | discover | done | 1 | - | - |  |
| e9039318 | discover | done | 1 | - | - |  |
| a1ec1245 | monitor | done | 1 | - | - |  |
| 6acda974 | test | done | 1 | - | 014 |  |
| a7ddc40b | tick | done | 1 | - | - |  |
| 00afddce | discover | done | 1 | - | - |  |
| 5146a28d | discover | done | 1 | - | - |  |
| f0d2836f | discover | done | 1 | - | - |  |
| af65672a | discover | done | 1 | - | - |  |
| 4c6af4e8 | discover | done | 1 | - | - |  |
| 5245a37e | discover | done | 1 | - | - |  |
| 24db754c | probe | done | 1 | - | - |  |
| 263c1d32 | discover | done | 1 | - | - |  |
| d0076ca3 | discover | done | 1 | - | - |  |
| 03adb38c | discover | done | 1 | - | - |  |
| 9efc5dbb | discover | done | 1 | - | - |  |
| b691ec23 | discover | done | 1 | - | - |  |
| 8958c7c2 | discover | done | 1 | - | - |  |
| 6611e45e | tick | done | 1 | - | - |  |
| 2e9399d2 | probe | done | 1 | - | - |  |
| fc8525b1 | tick | done | 1 | - | - |  |
| 595134d5 | probe | done | 1 | - | - |  |
| 1a1d091d | tick | done | 1 | - | - |  |
| 476304a5 | probe | queued | 0 | - | - |  |
| 268e463f | tick | queued | 0 | - | - |  |

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
| gemini-flash | gemini | ok | 4.91 |
| gemini-flash36 | gemini | ok | 2.01 |
| gemini-flash38 | gemini | error | 7.04 |
| gemini-gemini-flash-lite-latest | gemini | ok | 0.92 |
| gemini-gemma26b | gemini | ok | 0.93 |
| gemini-lite | gemini | ok | 0.66 |
| gemini-lite31 | gemini | ok | 2.65 |
| groq-gptoss120b | groq | ok | 0.38 |
| groq-gptoss20b | groq | ok | 0.34 |
| groq-qwen27b | groq | ok | 0.16 |
| local3b | ollama | ok | - |
| local4b | ollama | ok | - |
| or-ling-30-flash-fin | openrouter | cooldown | 0.91 |
| or-ling-30-flash-sante | openrouter | cooldown | 0.84 |
| or-ling-30-flash-vl | openrouter | BLOCKED | 2.78 |
| or-nemotron-35-lightning | openrouter | BLOCKED | 59.9 |
| or-nex-n25-pro | openrouter | BLOCKED | 2.18 |
| or-qwen27b | openrouter | cooldown | - |
| ovh-gptoss20b | custom | BLOCKED | - |
| ovh-llama70b | custom | BLOCKED | - |
| ovh-mistral24b | custom | BLOCKED | - |
