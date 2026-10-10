# FACTORY STATUS — 2026-10-10T20:55:08

**Worker:** running — last worker activity 0 min ago

**Bots:** 1/33 active   **Queue:** {"cancelled": 42, "done": 1304, "failed": 3, "paused": 46, "queued": 12, "running": 2}   **Healthy lanes:** gemini-gemini-flash-lite-latest, gemini-lite, gemini-lite31, groq-gptoss120b, groq-gptoss20b, groq-qwen27b, local3b, local4b

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
- lane gemini-flash BLOCKED: 3 consecutive errors: URLError
- lane gemini-flash-latest BLOCKED: 3 consecutive errors: URLError
- lane gemini-flash38 BLOCKED: 3 consecutive errors: [{ "error": { "code": 503, "message": "this model is curre
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
| cf5fe0c5 | test | done | 1 | - | 001 |  |
| 1f4dcd39 | test | done | 1 | - | 001 |  |
| b24ff203 | test | done | 1 | - | 001 |  |
| d64d5f43 | test | done | 2 | - | 001 |  |
| 6e21e735 | test | done | 1 | - | 001 |  |
| 909d4e4b | test | done | 1 | - | 001 |  |
| d9e6e57e | test | done | 1 | - | 001 |  |
| d13e7377 | test | done | 1 | - | 001 |  |
| 87def55d | tick | done | 1 | - | - |  |
| a6976a83 | probe | done | 1 | - | - |  |
| ef09c4af | report | running | 1 | - | - |  |
| cceb6137 | test | done | 1 | - | 001 |  |
| 7effb335 | test | done | 1 | - | 001 |  |
| 082d548a | test | done | 1 | - | 001 |  |
| 14031ed8 | tick | done | 1 | - | - |  |
| bb314448 | probe | done | 1 | - | - |  |
| 7b939e15 | test | done | 1 | - | 001 |  |
| 23700797 | test | done | 1 | - | 001 |  |
| 63b3b071 | test | done | 1 | - | 001 |  |
| bfd8b8ea | tick | done | 1 | - | - |  |
| 838c36cb | probe | done | 1 | - | - |  |
| fac9e34b | test | done | 1 | - | 001 |  |
| 2f157f08 | test | done | 1 | - | 001 |  |
| 7e4ce7d2 | test | done | 1 | - | 001 |  |
| 18a1cfe8 | test | done | 1 | - | 001 |  |
| 6472c8da | test | done | 1 | - | 001 |  |
| 8a1e233b | tick | done | 1 | - | - |  |
| 8f7a3355 | test | done | 1 | - | 001 |  |
| 97b8924c | probe | done | 1 | - | - |  |
| 6284f181 | test | done | 1 | - | 001 |  |
| 95313df2 | test | done | 1 | - | 001 |  |
| e87b6b40 | test | done | 1 | - | 001 |  |
| b6f952f7 | test | done | 1 | - | 001 |  |
| 38ffcb70 | tick | done | 1 | - | - |  |
| 6757cbd5 | probe | done | 1 | - | - |  |
| 37e608b8 | discover | done | 1 | - | - |  |
| c8ab344c | discover | done | 1 | - | - |  |
| 283647a6 | discover | done | 1 | - | - |  |
| 06a2063f | discover | done | 1 | - | - |  |
| f23e2d50 | discover | done | 1 | - | - |  |
| 7e972e6f | discover | done | 1 | - | - |  |
| 8cec1d2e | test | done | 1 | - | 001 |  |
| 96662f05 | test | done | 1 | - | 001 |  |
| d362fb80 | test | done | 1 | - | 001 |  |
| 8affd9ea | test | done | 1 | - | 001 |  |
| 139734ae | test | done | 1 | - | 001 |  |
| 95cedfc7 | tick | done | 1 | - | - |  |
| 30a0c9b0 | probe | done | 1 | - | - |  |
| 3992735d | test | done | 1 | - | 001 |  |
| 50d208b3 | test | done | 1 | - | 001 |  |
| dd4de290 | test | done | 1 | - | 001 |  |
| 3276a941 | test | done | 1 | - | 001 |  |
| b0b40d7c | test | done | 1 | - | 001 |  |
| c2019829 | tick | done | 1 | - | - |  |
| af260709 | probe | done | 1 | - | - |  |
| 6c6f3109 | test | done | 1 | - | 001 |  |
| a8cf88c3 | test | done | 1 | - | 001 |  |
| 28520876 | test | done | 1 | - | 001 |  |
| e780eed9 | test | done | 1 | - | 001 |  |
| b7c3fc31 | test | done | 1 | - | 001 |  |
| c76da1c9 | probe | done | 1 | - | - |  |
| e712583d | tick | done | 1 | - | - |  |
| 54df4cbc | test | done | 1 | - | 001 |  |
| 43103e8f | monitor | done | 1 | - | - |  |
| 061e6085 | test | done | 1 | - | 001 |  |
| d539c4b2 | test | done | 1 | - | 031 |  |
| 9574aaa8 | test | done | 1 | - | 001 |  |
| f4fb2409 | test | done | 1 | - | 001 |  |
| 7bb1cb35 | test | done | 1 | - | 001 |  |
| 8c5240d0 | probe | done | 1 | - | - |  |
| 071b50f9 | tick | done | 1 | - | - |  |
| 2027168a | test | done | 1 | - | 001 |  |
| db955230 | test | done | 1 | - | 001 |  |
| 4a8210eb | test | done | 1 | - | 001 |  |
| ceb0fb9b | test | done | 1 | - | 001 |  |
| db4d01a3 | test | done | 1 | - | 001 |  |
| 37c2acb5 | probe | done | 1 | - | - |  |
| a48e4687 | discover | done | 1 | - | - |  |
| 5e1d815b | discover | done | 1 | - | - |  |
| fe03e6c1 | discover | done | 1 | - | - |  |
| c8eb4400 | discover | done | 1 | - | - |  |
| f32db6d3 | discover | done | 1 | - | - |  |
| 0cefaaa1 | discover | done | 1 | - | - |  |
| d94dd50c | tick | done | 1 | - | - |  |
| 77817a90 | test | done | 1 | - | 001 |  |
| d679b7bf | test | done | 1 | - | 001 |  |
| d1accb4c | test | done | 1 | - | 001 |  |
| cef62a54 | test | done | 1 | - | 001 |  |
| cda951d6 | test | done | 1 | - | 001 |  |
| d69fdeca | probe | done | 1 | - | - |  |
| 41b1bbc5 | tick | done | 1 | - | - |  |
| 1f94ebc9 | test | done | 1 | - | 001 |  |
| 6a2167e7 | test | done | 1 | - | 001 |  |
| e82a74fd | test | done | 1 | - | 001 |  |
| a52ea0f4 | test | done | 1 | - | 001 |  |
| ef30c6f9 | test | done | 1 | - | 001 |  |
| cc4cabf9 | probe | done | 1 | - | - |  |
| b9792fae | tick | done | 1 | - | - |  |
| 7e36d324 | test | done | 1 | - | 001 |  |
| d3b68c25 | test | done | 1 | - | 001 |  |
| c4c5255a | test | done | 1 | - | 001 |  |
| 785be7a5 | test | done | 1 | - | 001 |  |
| c6d15792 | test | done | 1 | - | 001 |  |
| e59d3ee1 | probe | done | 1 | - | - |  |
| 09f71473 | tick | done | 1 | - | - |  |
| 062a8aee | test | done | 1 | - | 001 |  |
| 4024cc05 | test | done | 1 | - | 001 |  |
| 9fa0690f | test | done | 1 | - | 001 |  |
| 762af7bd | test | done | 1 | - | 001 |  |
| f6da4a4f | test | done | 1 | - | 001 |  |
| db0dc424 | probe | done | 1 | - | - |  |
| d66ae928 | tick | done | 1 | - | - |  |
| bed3e3bf | test | done | 1 | - | 001 |  |
| 2b0a19fb | test | done | 1 | - | 001 |  |
| da8fad42 | test | done | 1 | - | 001 |  |
| 269b8228 | test | done | 1 | - | 001 |  |
| bd883a1c | test | done | 2 | transient | 001 |  |
| 535c72d8 | probe | done | 1 | - | - |  |
| 15bc7352 | tick | done | 1 | - | - |  |
| e2c8f4f7 | test | done | 1 | - | 001 |  |
| b2fa28e0 | test | done | 1 | - | 001 |  |
| 7351a137 | test | done | 1 | - | 001 |  |
| 4564a182 | test | running | 1 | - | 001 |  |
| b44a5f67 | probe | done | 1 | - | - |  |
| 23b996a2 | tick | done | 1 | - | - |  |
| 116f3576 | test | queued | 0 | - | 001 |  |
| 75addaf6 | test | queued | 0 | - | 001 |  |
| dfd3bb9f | test | queued | 0 | - | 001 |  |
| fb6ec68d | test | queued | 0 | - | 001 |  |
| 6ea5960b | probe | done | 1 | - | - |  |
| 4b767e3a | test | queued | 0 | - | 001 |  |
| c0a9dca8 | tick | done | 1 | - | - |  |
| 414e6008 | test | queued | 0 | - | 001 |  |
| 7abed604 | probe | done | 1 | - | - |  |
| 77689686 | tick | done | 1 | - | - |  |
| a5c9b224 | test | done | 1 | - | 001 |  |
| c7674e54 | test | queued | 0 | - | 001 |  |
| 0b885e07 | test | queued | 0 | - | 001 |  |
| 869cedaf | probe | done | 1 | - | - |  |
| 7b78cead | tick | done | 1 | - | - |  |
| 86c060e1 | test | queued | 0 | - | 001 |  |
| b1757974 | test | queued | 0 | - | 001 |  |
| 09cc209d | probe | queued | 0 | - | - |  |
| e7010275 | discover | done | 1 | - | - |  |
| a6a00628 | discover | done | 1 | - | - |  |
| 3a91933d | discover | done | 1 | - | - |  |
| f730a766 | discover | done | 1 | - | - |  |
| 4a9c47e6 | discover | done | 1 | - | - |  |
| 8db99bfe | discover | done | 1 | - | - |  |
| 5731c7cb | tick | queued | 0 | - | - |  |

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
| gemini-flash | 3/8 | 177 | 2 |
| gemini-flash38 | 3/8 | 207 | 2 |
| gemini-lite | 3/8 | 326 | 2 |

## Lanes
| id | provider | state | latency s |
|---|---|---|---|
| gemini-flash | gemini | BLOCKED | 11.47 |
| gemini-flash-latest | gemini | BLOCKED | 6.5 |
| gemini-flash36 | gemini | error | 2.0 |
| gemini-flash38 | gemini | BLOCKED | 6.25 |
| gemini-gemini-flash-lite-latest | gemini | ok | 0.93 |
| gemini-gemma26b | gemini | error | 1.36 |
| gemini-lite | gemini | ok | 0.86 |
| gemini-lite31 | gemini | ok | 5.7 |
| groq-gptoss120b | groq | ok | 1.03 |
| groq-gptoss20b | groq | ok | 0.68 |
| groq-qwen27b | groq | ok | 0.57 |
| local3b | ollama | ok | - |
| local4b | ollama | ok | - |
| or-apodex-11-mini | openrouter | cooldown | 1.63 |
| or-ling-30-flash-sante | openrouter | BLOCKED | 1.78 |
| or-nemotron-35-lightning | openrouter | cooldown | 2.18 |
| ovh-gptoss20b | custom | BLOCKED | - |
| ovh-llama70b | custom | BLOCKED | - |
| ovh-mistral24b | custom | BLOCKED | - |
