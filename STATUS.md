# FACTORY STATUS — 2026-10-03T01:45:32

**Worker:** running — last worker activity 0 min ago

**Bots:** 1/29 active   **Queue:** {"cancelled": 42, "done": 767, "paused": 39, "queued": 7, "running": 2}   **Healthy lanes:** gemini-flash, gemini-gemma26b, gemini-lite31, groq-gptoss120b, groq-gptoss20b, groq-qwen27b, local3b, local4b

## Needs attention
- OUTAGE in the last 24 h: down 776 min from 2026-10-02T01:47 — power loss / battery flat (kernel-power 41)
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
- 1 retired / 1 paused bots (see Bots table)
- lane gemini-flash36 BLOCKED: tool_call_score decayed below 0.3
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
| 029 | bot-count-updater | active | VERIFIED | fs:read, fs:write |

## Jobs (24h)
| id | kind | state | att | class | bot | objective |
|---|---|---|---|---|---|---|
| fd5ae898 | test | done | 2 | transient | 001 |  |
| d616c8ba | test | done | 2 | - | 001 |  |
| d6562839 | test | done | 1 | - | 001 |  |
| d12b9e5f | test | done | 1 | - | 001 |  |
| 44159f49 | test | done | 1 | - | 001 |  |
| 6ddafcef | probe | done | 1 | - | - |  |
| 59cf05fb | tick | done | 1 | - | - |  |
| 99e5653e | report | running | 1 | - | - |  |
| 0c3f5f27 | bench | done | 1 | - | - |  |
| d712cbbe | canary | paused | 1 | security | - |  |
| df14302d | monitor | done | 1 | - | - |  |
| 4a92b32a | test | done | 1 | - | 001 |  |
| a6892e23 | test | done | 2 | - | 009 |  |
| d8b0189e | test | done | 1 | - | 011 |  |
| dd0512b5 | test | done | 1 | - | 012 |  |
| 3338d776 | test | done | 1 | - | 013 |  |
| 1fbba810 | test | done | 1 | - | 016 |  |
| d2350314 | test | done | 1 | - | 017 |  |
| 9a381a38 | test | done | 1 | - | 018 |  |
| 22bc8b7b | probe | done | 1 | - | - |  |
| ae821249 | run | done | 1 | - | 018 |  |
| 845fc841 | tick | done | 1 | - | - |  |
| 81018e13 | repair | paused | 1 | logic | 009 |  |
| 6ad0fa67 | test | done | 2 | transient | 001 |  |
| 1f6c487d | repair | paused | 1 | logic | 011 |  |
| 65022efd | test | done | 1 | - | 001 |  |
| 3f10d64d | test | done | 1 | - | 012 |  |
| 03decd6e | repair | paused | 1 | logic | 013 |  |
| 8b5239a3 | test | done | 1 | - | 001 |  |
| 1e82a590 | repair | paused | 1 | logic | 016 |  |
| 747aafa5 | repair | paused | 1 | logic | 017 |  |
| 6fcb78cb | test | done | 1 | - | 001 |  |
| 44d08ade | repair | paused | 1 | logic | 018 |  |
| 168cd1be | test | done | 1 | - | 001 |  |
| bf07a486 | test | done | 1 | - | 001 |  |
| d9005eea | probe | done | 1 | - | - |  |
| 019fdba2 | tick | done | 1 | - | - |  |
| e141af82 | repair | paused | 1 | logic | 012 |  |
| cec4d6a5 | test | done | 1 | - | 001 |  |
| 7db59fbb | create | done | 1 | - | - | Update the weekly self-review report script so that it also counts how |
| afc7408b | test | done | 1 | - | 001 |  |
| 76599715 | test | done | 1 | - | 029 |  |
| a8bf91c0 | test | done | 1 | - | 029 |  |
| 7cee7421 | test | done | 1 | - | 001 |  |
| f945f875 | test | done | 1 | - | 001 |  |
| fb0da058 | test | done | 1 | - | 001 |  |
| 1a919ad7 | test | done | 1 | - | 001 |  |
| 33bb3dfc | test | done | 1 | - | 001 |  |
| 07f6c614 | test | done | 1 | - | 001 |  |
| f2351e2c | probe | done | 1 | - | - |  |
| def22afc | tick | done | 1 | - | - |  |
| 85d83de6 | test | done | 1 | - | 001 |  |
| d41885d1 | test | done | 1 | - | 001 |  |
| 1e45bf31 | test | done | 1 | - | 001 |  |
| f8772d1e | test | done | 1 | - | 001 |  |
| 716de28c | test | done | 1 | - | 001 |  |
| 00d3b1f4 | probe | done | 1 | - | - |  |
| 01cf8bd0 | tick | done | 1 | - | - |  |
| 6fd7ea7d | test | done | 1 | - | 001 |  |
| caee5ec1 | probe | done | 1 | - | - |  |
| ef59cb87 | tick | done | 1 | - | - |  |
| 4916bbd0 | test | done | 1 | - | 001 |  |
| c7c830da | test | done | 1 | - | 001 |  |
| bd9b738b | test | done | 1 | - | 001 |  |
| 0c93124c | test | running | 1 | - | 001 |  |
| b3deef9b | probe | done | 2 | - | - |  |
| e3962516 | discover | done | 1 | - | - |  |
| 7d8ce118 | discover | done | 1 | - | - |  |
| f9af908b | discover | done | 1 | - | - |  |
| 65ecc914 | discover | done | 1 | - | - |  |
| 7410941b | discover | done | 1 | - | - |  |
| fbcfd1ff | discover | done | 1 | - | - |  |
| d313c567 | bench | done | 1 | - | - |  |
| a292b979 | tick | done | 1 | - | - |  |
| 6ae91506 | bench | done | 1 | - | - |  |
| b2875558 | test | queued | 0 | - | 001 |  |
| 92c073df | probe | done | 1 | - | - |  |
| db07cddc | tick | done | 1 | - | - |  |
| c15ff76e | test | queued | 0 | - | 001 |  |
| d6015a6e | test | queued | 0 | - | 001 |  |
| 57e0cf74 | test | queued | 0 | - | 001 |  |
| cc6074e6 | test | queued | 0 | - | 001 |  |
| 13e54a10 | probe | queued | 0 | - | - |  |
| 1051fb63 | tick | queued | 0 | - | - |  |

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
| gemini-flash | gemini | ok | 4.75 |
| gemini-flash-latest | gemini | cooldown | 10.42 |
| gemini-flash36 | gemini | BLOCKED | 2.41 |
| gemini-flash38 | gemini | cooldown | 1.69 |
| gemini-gemini-flash-lite-latest | gemini | cooldown | 9.37 |
| gemini-gemma26b | gemini | ok | 1.21 |
| gemini-lite | gemini | cooldown | 1.17 |
| gemini-lite31 | gemini | ok | 2.92 |
| groq-gptoss120b | groq | ok | 0.72 |
| groq-gptoss20b | groq | ok | 0.55 |
| groq-qwen27b | groq | ok | 0.47 |
| local3b | ollama | ok | - |
| local4b | ollama | ok | - |
| or-apodex-11-mini | openrouter | cooldown | 1.07 |
| or-ling-30-flash-sante | openrouter | cooldown | 0.99 |
| or-nemotron-35-lightning | openrouter | cooldown | 0.91 |
| or-qwen27b | openrouter | cooldown | 13.09 |
| ovh-gptoss20b | custom | BLOCKED | - |
| ovh-llama70b | custom | BLOCKED | - |
| ovh-mistral24b | custom | BLOCKED | - |
