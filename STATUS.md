# FACTORY STATUS — 2026-09-30T18:10:31

**Worker:** running — last worker activity 0 min ago

**Bots:** 13/28 active   **Queue:** {"cancelled": 42, "done": 617, "paused": 22, "queued": 5, "running": 2}   **Healthy lanes:** gemini-flash, gemini-gemini-flash-lite-latest, gemini-gemma26b, gemini-lite, gemini-lite31, groq-gptoss120b, groq-gptoss20b, groq-qwen27b, local3b, local4b, or-ling-30-flash-sante

## Needs attention
- FACTORY CANARY FAILED at 1790706783.70331 (lane gemini:gemini-3.1-flash-lite): the factory itself, not a bot, is broken — see AUDIT factory.canary
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
- bot 002 research-scout is testing
- bot 003 code-smith is testing
- bot 004 changelog-writer is testing
- bot 005 csv-quality-auditor is testing
- bot 019 pytest-runner is testing
- bot 020 workspace-file-lister is testing
- bot 021 email-line-counter is testing
- bot 022 csv-refund-filter is testing
- bot 023 refund-summarizer is testing
- bot 026 sqlite-query-bot is testing
- bot 027 self-review-bot is testing
- bot 028 weekly-self-review is testing
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
| 003 | code-smith | testing | UNVERIFIED | fs:write, shell:workspace |
| 004 | changelog-writer | testing | UNVERIFIED | fs:read, fs:write |
| 005 | csv-quality-auditor | testing | UNVERIFIED | fs:read, fs:write |
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
| 019 | pytest-runner | testing | UNVERIFIED | fs:read, fs:write, shell:workspace |
| 020 | workspace-file-lister | testing | UNVERIFIED | shell:workspace, fs:write |
| 021 | email-line-counter | testing | UNVERIFIED | fs:read, fs:write |
| 022 | csv-refund-filter | testing | UNVERIFIED | fs:read, fs:write |
| 023 | refund-summarizer | testing | UNVERIFIED | fs:read, fs:write |
| 024 | pytest-runner-bot | active | VERIFIED | fs:read, fs:write, shell:workspace |
| 025 | text-transformer | active | VERIFIED | fs:read, fs:write |
| 026 | sqlite-query-bot | testing | UNVERIFIED | fs:read, fs:write, mcp:mcp-sqlite3 |
| 027 | self-review-bot | testing | UNVERIFIED | fs:read, fs:write, net:search, net:fetch |
| 028 | weekly-self-review | testing | UNVERIFIED | fs:read, fs:write, net:search, net:fetch |

## Jobs (24h)
| id | kind | state | att | class | bot | objective |
|---|---|---|---|---|---|---|
| ec968d47 | test | done | 1 | - | 001 |  |
| 4f6d66a5 | probe | done | 1 | - | - |  |
| 7f41dddc | tick | done | 1 | - | - |  |
| 579491c3 | test | done | 1 | - | 001 |  |
| 0f59f40f | test | done | 1 | - | 005 |  |
| 09146563 | test | done | 1 | - | 006 |  |
| 0f19ad75 | test | done | 1 | - | 007 |  |
| 96e43656 | test | done | 1 | - | 008 |  |
| 09ce9ce4 | test | done | 1 | - | 009 |  |
| e6462e61 | test | done | 1 | - | 011 |  |
| 8eec6c54 | test | done | 1 | - | 012 |  |
| 0969955b | test | done | 1 | - | 013 |  |
| 7ce257a8 | test | done | 1 | - | 014 |  |
| 598a5cc4 | test | done | 1 | - | 016 |  |
| fd26f12c | test | done | 1 | - | 017 |  |
| 37ca8049 | test | done | 1 | - | 018 |  |
| f2bb4b62 | test | done | 1 | - | 019 |  |
| bb48c3f9 | test | done | 1 | - | 022 |  |
| 6a59bbe3 | test | done | 1 | - | 023 |  |
| 5929288f | test | done | 1 | - | 024 |  |
| 65e0de3b | test | done | 1 | - | 025 |  |
| 30f205bc | test | done | 1 | - | 026 |  |
| 4da83d39 | test | done | 1 | - | 027 |  |
| d85823bb | report | running | 1 | - | - |  |
| dda50f35 | bench | done | 1 | - | - |  |
| 09024b3a | canary | done | 1 | - | - |  |
| cfc7b1fc | test | done | 1 | - | 001 |  |
| 96c4c77a | test | done | 1 | - | 003 |  |
| e717ddc1 | test | done | 1 | - | 005 |  |
| 4d8b6f21 | test | done | 1 | - | 006 |  |
| 3b04ee67 | test | done | 1 | - | 007 |  |
| 2f8c68e5 | test | done | 1 | - | 008 |  |
| 92b55be6 | test | done | 1 | - | 009 |  |
| a0ca3faa | test | done | 1 | - | 011 |  |
| 46a9742e | test | done | 1 | - | 012 |  |
| c1be9289 | test | done | 1 | - | 013 |  |
| 3053504b | test | done | 1 | - | 014 |  |
| 9746e6aa | test | done | 1 | - | 016 |  |
| e70a2e86 | test | done | 1 | - | 017 |  |
| 38770f25 | test | done | 1 | - | 018 |  |
| 665ef041 | test | done | 1 | - | 019 |  |
| 196465d0 | test | done | 1 | - | 022 |  |
| 24eb3217 | test | done | 1 | - | 023 |  |
| 349839fb | test | done | 1 | - | 024 |  |
| ff9a5304 | test | done | 1 | - | 025 |  |
| 8a363ecb | test | done | 1 | - | 026 |  |
| fbcc0040 | test | done | 1 | - | 027 |  |
| de0ebcc5 | test | done | 1 | - | 001 |  |
| da8c8c2d | test | done | 1 | - | 028 |  |
| 9155875e | test | done | 1 | - | 028 |  |
| 2a020aa6 | repair | paused | 1 | logic | 005 |  |
| 23ec7b81 | test | done | 1 | - | 001 |  |
| 5def33a0 | repair | paused | 1 | logic | 006 |  |
| 061a0266 | test | done | 1 | - | 001 |  |
| 38b3cc11 | repair | done | 1 | - | 007 |  |
| 8615298f | repair | paused | 1 | logic | 023 |  |
| 9ddad2e1 | test | done | 1 | - | 024 |  |
| be8c781b | repair | paused | 1 | logic | 025 |  |
| 764968eb | test | done | 1 | - | 001 |  |
| c3aed36d | repair | paused | 1 | logic | 026 |  |
| 8a77eba4 | repair | done | 1 | - | 027 |  |
| 2ae8b6da | repair | paused | 1 | logic | 003 |  |
| ebcd50e4 | test | done | 1 | - | 001 |  |
| 9d53582f | repair | paused | 1 | logic | 005 |  |
| 252a5b8d | test | done | 1 | - | 001 |  |
| a0577b9d | test | done | 1 | - | 001 |  |
| bddec4ba | probe | done | 1 | - | - |  |
| 2d6263e3 | tick | done | 1 | - | - |  |
| 46a02802 | test | done | 1 | - | 017 |  |
| 70dc72a1 | repair | paused | 1 | logic | 019 |  |
| ce9c717b | repair | paused | 1 | logic | 022 |  |
| 73c0022b | test | done | 1 | - | 001 |  |
| d229874c | repair | paused | 1 | logic | 023 |  |
| 472caf57 | repair | done | 1 | - | 024 |  |
| 0e05bf69 | test | done | 1 | - | 025 |  |
| 0656e7cc | repair | paused | 1 | logic | 026 |  |
| b468005e | test | done | 1 | - | 027 |  |
| 69f3367a | test | done | 1 | - | 001 |  |
| 176c95ca | test | done | 1 | - | 001 |  |
| edd55734 | test | done | 1 | - | 001 |  |
| 0d658a6f | run | done | 1 | - | 027 |  |
| 2c510b7c | test | done | 1 | - | 001 |  |
| 06281ead | probe | done | 1 | - | - |  |
| f4e79228 | tick | done | 1 | - | - |  |
| 6629b411 | test | done | 1 | - | 001 |  |
| e53c6f4e | test | done | 1 | - | 028 |  |
| 192072d9 | test | done | 1 | - | 001 |  |
| 371e13d0 | probe | done | 2 | - | - |  |
| 6c2fff78 | tick | done | 1 | - | - |  |
| 061295ee | probe | done | 1 | - | - |  |
| f354476d | tick | done | 1 | - | - |  |
| 6e8c618f | probe | done | 1 | - | - |  |
| b40fe03b | discover | done | 1 | - | - |  |
| e9cd9f78 | discover | done | 1 | - | - |  |
| 5fafc702 | discover | done | 1 | - | - |  |
| 48df5e9e | discover | done | 1 | - | - |  |
| 4a3cb682 | discover | done | 1 | - | - |  |
| 5aba35ca | discover | done | 1 | - | - |  |
| 24cabff1 | repair | paused | 1 | logic | 027 |  |
| 02a7996c | repair | paused | 1 | logic | 028 |  |
| 3792493d | test | done | 1 | - | 001 |  |
| 52d5ecd7 | test | done | 1 | - | 001 |  |
| e4d5e8a7 | test | done | 1 | - | 001 |  |
| 738502df | test | done | 1 | - | 001 |  |
| 75453770 | tick | done | 1 | - | - |  |
| 29d58f6d | probe | done | 1 | - | - |  |
| b3bbf646 | test | running | 1 | - | 001 |  |
| 72396f63 | tick | done | 1 | - | - |  |
| c3b3b031 | probe | done | 1 | - | - |  |
| 7da3d73a | test | queued | 0 | - | 001 |  |
| 0f1be090 | test | queued | 0 | - | 001 |  |
| 953093ab | tick | done | 1 | - | - |  |
| 021d5c32 | probe | done | 1 | - | - |  |
| 2341d262 | test | queued | 0 | - | 001 |  |
| 1d45fe25 | probe | queued | 0 | - | - |  |
| b3e404ef | run | done | 1 | - | 018 |  |
| 35fb2241 | tick | queued | 0 | - | - |  |

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
| or-qwen27b | 2/3 | 58 | 1 |
| gemini-flash36 | 2/4 | 63 | 1 |
| gemini-flash38 | 2/4 | 128 | 1 |
| groq-qwen27b | 2/4 | 147 | 1 |
| gemini-flash | 2/4 | 180 | 1 |
| gemini-lite | 1/4 | 618 | 1 |

## Lanes
| id | provider | state | latency s |
|---|---|---|---|
| gemini-flash | gemini | ok | 6.1 |
| gemini-flash36 | gemini | no_tool_call | 2.05 |
| gemini-flash38 | gemini | error | 1.73 |
| gemini-gemini-flash-lite-latest | gemini | ok | 15.67 |
| gemini-gemma26b | gemini | ok | 39.17 |
| gemini-lite | gemini | ok | 8.45 |
| gemini-lite31 | gemini | ok | 1.02 |
| groq-gptoss120b | groq | ok | 0.52 |
| groq-gptoss20b | groq | ok | 0.41 |
| groq-qwen27b | groq | ok | 0.5 |
| local3b | ollama | ok | - |
| local4b | ollama | ok | - |
| or-ling-30-flash-fin | openrouter | BLOCKED | 0.81 |
| or-ling-30-flash-sante | openrouter | ok | 1.19 |
| or-nemotron-35-lightning | openrouter | no_tool_call | 120.33 |
| or-qwen27b | openrouter | cooldown | 1.5 |
| ovh-gptoss20b | custom | BLOCKED | - |
| ovh-llama70b | custom | BLOCKED | - |
| ovh-mistral24b | custom | BLOCKED | - |
