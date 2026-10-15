# FACTORY STATUS — 2026-10-15T10:10:33

**Worker:** running — last worker activity 0 min ago

**Bots:** 0/33 active   **Queue:** {"cancelled": 42, "done": 1668, "failed": 7, "paused": 49, "queued": 11, "running": 2}   **Healthy lanes:** gemini-flash-latest, gemini-gemini-flash-lite-latest, gemini-lite, gemini-lite31, groq-gptoss120b, groq-gptoss20b, groq-qwen27b, local3b, local4b

## Needs attention
- FACTORY CANARY FAILED at 1791945707.46473 (lane groq:openai/gpt-oss-20b): the factory itself, not a bot, is broken — see AUDIT factory.canary
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
- job 14978851 repair paused (logic)
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
- lane gemini-flash38 BLOCKED: 3 consecutive errors: [{ "error": { "code": 503, "message": "this model is curre
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
| f9b10c1e | test | done | 1 | - | 001 |  |
| f876d821 | test | failed | 3 | transient | 001 |  |
| 0ec74895 | test | failed | 3 | transient | 001 |  |
| ae80d13a | test | done | 1 | - | 001 |  |
| 825829e8 | report | running | 1 | - | - |  |
| e2869fda | test | done | 1 | - | 001 |  |
| fc146198 | test | done | 1 | - | 001 |  |
| ceb330c7 | test | done | 1 | - | 001 |  |
| 529d6be2 | test | done | 1 | - | 001 |  |
| a8403e44 | test | done | 1 | - | 001 |  |
| 56718df5 | test | done | 1 | - | 001 |  |
| e80bcd61 | test | done | 1 | - | 001 |  |
| 214b4c30 | test | done | 1 | - | 001 |  |
| 0cbb7165 | probe | done | 1 | - | - |  |
| 851644e8 | tick | done | 1 | - | - |  |
| 15b6a9ef | probe | done | 1 | - | - |  |
| a11fa142 | discover | done | 1 | - | - |  |
| 8594b03c | discover | done | 1 | - | - |  |
| f20d577e | discover | done | 1 | - | - |  |
| 11758c44 | discover | done | 1 | - | - |  |
| a269167e | discover | done | 1 | - | - |  |
| 91e0d319 | discover | done | 1 | - | - |  |
| c027b3b0 | tick | done | 1 | - | - |  |
| 7b5aa26d | test | done | 1 | - | 001 |  |
| e32c1507 | test | done | 1 | - | 001 |  |
| f0a7add9 | test | done | 1 | - | 001 |  |
| e1bba806 | test | done | 1 | - | 001 |  |
| 8188cb64 | probe | done | 1 | - | - |  |
| b22e199f | tick | done | 1 | - | - |  |
| 09eb4142 | test | done | 1 | - | 001 |  |
| 93b1d742 | test | done | 1 | - | 001 |  |
| 3a1cba65 | test | done | 1 | - | 001 |  |
| da38a03e | test | done | 1 | - | 001 |  |
| 72f87ba6 | probe | done | 1 | - | - |  |
| 7b2aa9f9 | test | done | 3 | transient | 001 |  |
| aafdd71b | tick | done | 1 | - | - |  |
| 421c497d | test | done | 2 | transient | 001 |  |
| 16edca8e | test | done | 3 | transient | 001 |  |
| 891f375d | test | done | 1 | - | 001 |  |
| e8402ec9 | test | done | 1 | - | 001 |  |
| 4f89b711 | probe | done | 1 | - | - |  |
| 62ccdabf | discover | done | 1 | - | - |  |
| fb75b79c | discover | done | 1 | - | - |  |
| 44a008e3 | discover | done | 1 | - | - |  |
| 6ab593b5 | discover | done | 1 | - | - |  |
| 2062104d | discover | done | 1 | - | - |  |
| 399e426d | discover | done | 1 | - | - |  |
| a728264b | tick | done | 1 | - | - |  |
| da5c605f | test | done | 1 | - | 001 |  |
| e349b46e | test | done | 1 | - | 001 |  |
| 1d4d924b | test | done | 1 | - | 001 |  |
| 01291e79 | test | queued | 0 | - | 001 |  |
| 12211cd8 | probe | done | 1 | - | - |  |
| 6dbe6573 | discover | done | 1 | - | - |  |
| 34c379e2 | discover | done | 1 | - | - |  |
| fa941204 | discover | done | 1 | - | - |  |
| 3078a88f | discover | done | 1 | - | - |  |
| 39011089 | discover | done | 1 | - | - |  |
| 8e5ec14a | discover | done | 1 | - | - |  |
| 585d7c88 | test | queued | 0 | - | 001 |  |
| 2cbc59ff | tick | done | 1 | - | - |  |
| 95f1688c | probe | done | 1 | - | - |  |
| a4f7d49b | tick | done | 1 | - | - |  |
| 50c9dc64 | test | done | 3 | transient | 001 |  |
| 7838d8fd | test | queued | 0 | - | 001 |  |
| b26f40de | probe | done | 1 | - | - |  |
| fca5af08 | tick | done | 1 | - | - |  |
| 8bdeddda | probe | done | 1 | - | - |  |
| 6c9b4839 | discover | done | 1 | - | - |  |
| 24975f92 | discover | done | 1 | - | - |  |
| 34c4e275 | discover | done | 1 | - | - |  |
| 18de3bfd | discover | done | 1 | - | - |  |
| 5844091f | discover | done | 1 | - | - |  |
| 3eeb0a9d | discover | done | 1 | - | - |  |
| 6bae1547 | tick | done | 1 | - | - |  |
| d4220485 | probe | done | 1 | - | - |  |
| cec87203 | probe | done | 1 | - | - |  |
| ae1ae481 | test | queued | 0 | - | 001 |  |
| 85478d12 | test | done | 1 | - | 001 |  |
| 762d9d2c | discover | done | 1 | - | - |  |
| 46b621a3 | test | done | 1 | - | 001 |  |
| 15ff8e1a | tick | done | 1 | - | - |  |
| f8b3662d | probe | done | 1 | - | - |  |
| f90c1262 | test | queued | 0 | - | 001 |  |
| a69dc170 | test | queued | 0 | - | 001 |  |
| 9a8bdecc | test | queued | 0 | - | 001 |  |
| 32a6272c | test | running | 1 | - | 001 |  |
| 244fedab | tick | done | 1 | - | - |  |
| 205c15fe | probe | done | 1 | - | - |  |
| 4e456ff7 | test | queued | 0 | - | 001 |  |
| 0d697328 | test | queued | 0 | - | 001 |  |
| 56755eba | tick | queued | 0 | - | - |  |
| 832ce531 | probe | queued | 0 | - | - |  |

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
| gemini-flash | gemini | error | 12.2 |
| gemini-flash-latest | gemini | ok | 24.19 |
| gemini-flash36 | gemini | BLOCKED | 1.24 |
| gemini-flash38 | gemini | BLOCKED | 8.9 |
| gemini-gemini-flash-lite-latest | gemini | ok | 0.63 |
| gemini-gemma26b | gemini | error | 1.14 |
| gemini-lite | gemini | ok | 1.02 |
| gemini-lite31 | gemini | ok | 2.07 |
| groq-gptoss120b | groq | ok | 0.48 |
| groq-gptoss20b | groq | ok | 0.35 |
| groq-qwen27b | groq | ok | 0.2 |
| local3b | ollama | ok | - |
| local4b | ollama | ok | - |
| or-apodex-11-mini | openrouter | BLOCKED | 0.91 |
| or-lfm-25-26b | openrouter | cooldown | 0.9 |
| or-nemotron-3-ultra-550b-a55b | openrouter | cooldown | 2.7 |
| or-nemotron-35-lightning | openrouter | cooldown | 1.62 |
| ovh-gptoss20b | custom | BLOCKED | - |
| ovh-llama70b | custom | BLOCKED | - |
| ovh-mistral24b | custom | BLOCKED | - |
