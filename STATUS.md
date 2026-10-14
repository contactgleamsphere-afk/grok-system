# FACTORY STATUS — 2026-10-14T03:34:39

**Worker:** running — last worker activity 0 min ago

**Bots:** 0/33 active   **Queue:** {"cancelled": 42, "done": 1543, "failed": 5, "paused": 48, "queued": 13, "running": 2}   **Healthy lanes:** gemini-flash-latest, gemini-flash38, gemini-gemini-flash-lite-latest, gemini-gemma26b, gemini-lite, gemini-lite31, groq-gptoss120b, groq-gptoss20b, groq-qwen27b, local3b, local4b, or-lfm-25-26b, or-nemotron-3-ultra-550b-a55b, or-nemotron-35-lightning

## Needs attention
- OUTAGE in the last 24 h: down 62 min from 2026-10-14T02:31 — power loss / battery flat (kernel-power 41)
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
- job b6c2d434 canary paused (security)
- job 0c642780 canary paused (security)
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
- bot 031 weekly-self-review is testing
- bot 032 weekly-self-review is testing
- bot 033 weekly-selfreview-count-bots is testing
- 1 retired / 1 paused bots (see Bots table)
- lane gemini-flash36 BLOCKED: tool_call_score decayed below 0.3
- lane or-apodex-11-mini BLOCKED: gone: {"error":{"message":"no endpoints found for apodex/apodex-1.1-mini:free.",
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
| 031 | weekly-self-review | testing | UNVERIFIED | fs:read, fs:write |
| 032 | weekly-self-review | testing | UNVERIFIED | fs:read, fs:write, net:search, net:fetch |
| 033 | weekly-selfreview-count-bots | testing | UNVERIFIED | fs:read, fs:write |

## Jobs (24h)
| id | kind | state | att | class | bot | objective |
|---|---|---|---|---|---|---|
| edafcea5 | test | failed | 3 | transient | 001 |  |
| 5524de8c | test | done | 1 | - | 001 |  |
| 93fc5c42 | test | done | 1 | - | 001 |  |
| 1523484a | test | done | 1 | - | 001 |  |
| 55933f61 | report | running | 1 | - | - |  |
| 0a51ed8f | tick | done | 1 | - | - |  |
| 6db6e081 | probe | done | 1 | - | - |  |
| 698180d8 | test | done | 1 | - | 001 |  |
| d2b1b3ff | test | done | 1 | - | 001 |  |
| 30b7be50 | tick | done | 1 | - | - |  |
| 5427a0cf | probe | done | 1 | - | - |  |
| b3ab4afa | test | done | 1 | - | 001 |  |
| d6343b48 | test | done | 1 | - | 001 |  |
| d94c7611 | test | done | 1 | - | 001 |  |
| 7e0bf6cd | tick | done | 1 | - | - |  |
| a4edddc0 | probe | done | 1 | - | - |  |
| 2fe26cd9 | discover | done | 1 | - | - |  |
| f8633ff8 | discover | done | 1 | - | - |  |
| 3a9b2f5b | discover | done | 1 | - | - |  |
| 507de104 | discover | done | 1 | - | - |  |
| 888a2931 | discover | done | 1 | - | - |  |
| 439d408a | discover | done | 1 | - | - |  |
| e0916f59 | test | done | 1 | - | 001 |  |
| 59337fcb | test | done | 1 | - | 001 |  |
| 3015c529 | test | done | 1 | - | 001 |  |
| 680335d1 | test | done | 1 | - | 001 |  |
| 74b22dd1 | tick | done | 1 | - | - |  |
| 9d43f9c9 | probe | done | 1 | - | - |  |
| 8e562932 | test | done | 1 | - | 001 |  |
| b2abcb78 | test | done | 1 | - | 001 |  |
| 0f0e844c | test | done | 1 | - | 001 |  |
| 9a98e6f7 | test | done | 1 | - | 001 |  |
| f5cc5dd0 | test | done | 1 | - | 001 |  |
| 09fc9827 | tick | done | 1 | - | - |  |
| b70aa8c0 | probe | done | 1 | - | - |  |
| 9ca57765 | test | done | 1 | - | 001 |  |
| e0056f0c | test | done | 1 | - | 001 |  |
| cdc189c9 | test | done | 1 | - | 001 |  |
| 6cc17c4a | test | failed | 3 | transient | 001 |  |
| 98037d6a | tick | done | 1 | - | - |  |
| adcba1c4 | probe | done | 1 | - | - |  |
| 19c838c2 | test | done | 2 | transient | 001 |  |
| aa35caa3 | test | done | 1 | - | 001 |  |
| b7f8bfef | test | done | 1 | - | 001 |  |
| d894a64c | tick | done | 1 | - | - |  |
| 9f2509a2 | probe | done | 1 | - | - |  |
| 0b5cb79d | probe | done | 1 | - | - |  |
| 9d8bd63f | tick | done | 1 | - | - |  |
| ce3c1fa8 | probe | done | 1 | - | - |  |
| 8a38358b | discover | done | 1 | - | - |  |
| e3e7478f | discover | done | 1 | - | - |  |
| a8775d77 | discover | done | 1 | - | - |  |
| f17649df | discover | done | 1 | - | - |  |
| 77dbdc5d | discover | done | 1 | - | - |  |
| 7a51debf | discover | done | 1 | - | - |  |
| 5a603559 | test | done | 1 | - | 001 |  |
| 8abcd887 | test | done | 1 | - | 001 |  |
| 72c80422 | tick | done | 1 | - | - |  |
| c031edb4 | probe | done | 1 | - | - |  |
| 5006ba9b | discover | done | 1 | - | - |  |
| 274f4799 | discover | done | 1 | - | - |  |
| 49619093 | discover | done | 1 | - | - |  |
| 9586ae60 | discover | done | 1 | - | - |  |
| 5dab72ed | discover | done | 1 | - | - |  |
| b8e6a152 | discover | done | 1 | - | - |  |
| 10206006 | monitor | done | 1 | - | - |  |
| 77c04c86 | test | done | 1 | - | 031 |  |
| 142dd6d7 | test | done | 1 | - | 031 |  |
| 1b2d61cb | test | running | 2 | transient | 001 |  |
| 9c35778b | test | queued | 1 | - | 001 |  |
| 1c048b97 | test | queued | 0 | - | 001 |  |
| ce49c72e | tick | done | 1 | - | - |  |
| 86bed3db | probe | done | 1 | - | - |  |
| 9d2bb420 | discover | done | 1 | - | - |  |
| 270c471a | discover | done | 1 | - | - |  |
| f5d56718 | discover | done | 1 | - | - |  |
| 0954e62b | discover | done | 1 | - | - |  |
| f3f6b49b | discover | done | 1 | - | - |  |
| a01d44d1 | discover | done | 1 | - | - |  |
| 0c4d053e | tick | done | 1 | - | - |  |
| 4f12ad4a | probe | done | 1 | - | - |  |
| b1717ca4 | discover | done | 1 | - | - |  |
| 6c0395cb | discover | done | 1 | - | - |  |
| fc776a5c | discover | done | 1 | - | - |  |
| 7ad6e347 | discover | done | 1 | - | - |  |
| 2cbbae4c | discover | done | 1 | - | - |  |
| 3d744ddf | discover | done | 1 | - | - |  |
| 14978851 | repair | queued | 1 | - | 031 |  |
| 0842ece4 | probe | queued | 0 | - | - |  |
| f691e0dc | tick | queued | 0 | - | - |  |

## Lane quality (D-050, reference suite, rolling window)
| lane | score | secs | runs |
|---|---|---|---|
| or-lfm-25-26b | 3/3 | 31 | 1 |
| or-apodex-11-mini | 4/4 | 49 | 1 |
| or-nemotron-3-ultra-550b-a55b | 4/4 | 62 | 1 |
| groq-gptoss120b | 9/9 | 77 | 3 |
| or-nemotron-35-lightning | 2/2 | 564 | 1 |
| groq-gptoss20b | 7/8 | 127 | 2 |
| gemini-gemma26b | 5/6 | 65 | 2 |
| gemini-gemini-flash-lite-latest | 5/8 | 44 | 2 |
| gemini-lite31 | 4/8 | 53 | 2 |
| gemini-flash36 | 2/4 | 63 | 1 |
| gemini-flash-latest | 2/4 | 72 | 1 |
| groq-qwen27b | 4/8 | 107 | 2 |
| gemini-flash | 3/8 | 177 | 2 |
| gemini-flash38 | 3/8 | 207 | 2 |
| gemini-lite | 3/8 | 326 | 2 |

## Lanes
| id | provider | state | latency s |
|---|---|---|---|
| gemini-flash | gemini | error | 6.62 |
| gemini-flash-latest | gemini | ok | 1.24 |
| gemini-flash36 | gemini | BLOCKED | 2.78 |
| gemini-flash38 | gemini | ok | 29.85 |
| gemini-gemini-flash-lite-latest | gemini | ok | 0.98 |
| gemini-gemma26b | gemini | ok | 1.08 |
| gemini-lite | gemini | ok | 0.97 |
| gemini-lite31 | gemini | ok | 0.61 |
| groq-gptoss120b | groq | ok | 0.55 |
| groq-gptoss20b | groq | ok | 0.54 |
| groq-qwen27b | groq | ok | 0.31 |
| local3b | ollama | ok | - |
| local4b | ollama | ok | - |
| or-apodex-11-mini | openrouter | BLOCKED | 0.91 |
| or-lfm-25-26b | openrouter | ok | 0.9 |
| or-nemotron-3-ultra-550b-a55b | openrouter | ok | 2.7 |
| or-nemotron-35-lightning | openrouter | ok | 1.62 |
| ovh-gptoss20b | custom | BLOCKED | - |
| ovh-llama70b | custom | BLOCKED | - |
| ovh-mistral24b | custom | BLOCKED | - |
