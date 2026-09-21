# FACTORY STATUS — 2026-09-21T23:09:17

**Bots:** 8/9 active   **Queue:** {"cancelled": 1, "done": 17, "running": 1}   **Healthy lanes:** gemini-gemma26b, gemini-lite, gemini-lite31, groq-gptoss120b, groq-gptoss20b, groq-qwen27b, local3b, local4b

## Needs attention
- lane or-deepseek BLOCKED: gone: {"error":{"message":"this model is unavailable for free. the paid version is available now - use this slug instead: deepseek/deepseek-v4-flash-0731","code":404}

## Bots
| id | name | status | verified | permissions |
|---|---|---|---|---|
| 001 | master | building | VERIFIED | fs:read, fs:write, shell:workspace, net:search, net:fetch |
| 002 | research-scout | active | VERIFIED | net:search, net:fetch, fs:read |
| 003 | code-smith | active | VERIFIED | fs:read, fs:write, shell:workspace |
| 004 | changelog-writer | active | VERIFIED | fs:read, fs:write |
| 005 | csv-quality-auditor | active | VERIFIED | fs:read, fs:write |
| 006 | json-to-markdown-table | active | VERIFIED | fs:read, fs:write |
| 007 | todo-extractor | active | VERIFIED | fs:read, fs:write |
| 008 | word-frequency-bot | active | VERIFIED | fs:read, fs:write |
| 009 | line-dedupe-bot | active | VERIFIED | fs:read, fs:write |

## Jobs (24h)
| id | kind | state | att | class | bot | objective |
|---|---|---|---|---|---|---|
| 0a39c2e1 | create | done | 1 | - | - | Create a JSON-to-Markdown table bot: given a workspace file named reco |
| 31ffc26e | test | done | 1 | - | 005 |  |
| fe3b6a6b | monitor | cancelled | 0 | - | - |  |
| 7c69d3cf | monitor | done | 2 | - | - |  |
| 009ae02a | monitor | done | 1 | - | - |  |
| a5c299d7 | repair | done | 1 | logic | 004 |  |
| efc687cf | create | done | 1 | - | - | Create a word-frequency bot: given a workspace text file named input.t |
| bbafb536 | create | done | 1 | - | - | Create a TODO-extractor bot: given a workspace file named notes.txt, f |
| 39f42e32 | create | done | 1 | - | - | Create a word-frequency bot: given a workspace text file named input.t |
| 74c74bee | test | done | 1 | - | 007 |  |
| c12a1af9 | test | done | 1 | - | 007 |  |
| 5e4217a5 | test | done | 1 | - | 008 |  |
| 19628fd7 | monitor | done | 1 | - | - |  |
| 9bad8732 | probe | done | 1 | logic | - |  |
| f781e2f8 | probe | done | 1 | logic | - |  |
| e0c940c2 | test | done | 2 | - | 006 |  |
| 043bd1f8 | create | done | 1 | - | - | Create a line-dedupe bot: given a workspace file named lines.txt, remo |
| 5754cd51 | test | done | 1 | - | 009 |  |
| 08d39529 | report | running | 1 | - | - |  |

## Lanes
| id | provider | state | latency s |
|---|---|---|---|
| gemini-flash | gemini | quota | - |
| gemini-flash36 | gemini | no_tool_call | - |
| gemini-flash38 | gemini | quota | - |
| gemini-gemma26b | gemini | ok | 1.02 |
| gemini-lite | gemini | ok | 0.74 |
| gemini-lite31 | gemini | ok | 1.47 |
| groq-gptoss120b | groq | ok | 0.61 |
| groq-gptoss20b | groq | ok | 0.54 |
| groq-qwen27b | groq | ok | 0.42 |
| local3b | ollama | ok | - |
| local4b | ollama | ok | - |
| or-deepseek | openrouter | BLOCKED | - |
| or-qwen27b | openrouter | quota | - |
| ovh-gptoss20b | custom | BLOCKED | - |
| ovh-llama70b | custom | BLOCKED | - |
| ovh-mistral24b | custom | BLOCKED | - |
