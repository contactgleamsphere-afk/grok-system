# FACTORY STATUS — 2026-09-22T23:09:19

**Bots:** 21/23 active   **Queue:** {"cancelled": 12, "done": 108, "queued": 2, "running": 1}   **Healthy lanes:** gemini-flash36, gemini-gemma26b, gemini-lite, gemini-lite31, groq-qwen27b, local3b, local4b

## Needs attention
- bot 010 dedupe-failover-probe is paused
- bot 015 system-cleanup is retired
- lane or-deepseek BLOCKED: gone: {"error":{"message":"this model is unavailable for free. the paid version is available now - use this slug instead: deepseek/deepseek-v4-flash-0731","code":404}
- ACTION REQUIRED (owner): provider:cerebras — set CEREBRAS_API_KEY (User env) after signing up: https://cloud.cerebras.ai (free tier ~1M tokens/day)
- ACTION REQUIRED (owner): provider:nvidia — set NVIDIA_API_KEY (User env) after signing up: https://build.nvidia.com (free ~40 rpm, tool-capable models)
- ACTION REQUIRED (owner): provider:mistral — set MISTRAL_API_KEY (User env) after signing up: https://console.mistral.ai (Experiment free tier)

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
| 016 | workspace-tidy-counter | active | VERIFIED | shell:workspace |
| 017 | name-sorter | active | VERIFIED | fs:read, fs:write |
| 018 | csv-country-totals | active | VERIFIED | fs:read, fs:write |
| 019 | pytest-runner | active | VERIFIED | fs:read, fs:write, shell:workspace |
| 020 | workspace-file-lister | active | VERIFIED | shell:workspace, fs:write |
| 021 | email-line-counter | active | VERIFIED | fs:read, fs:write |
| 022 | csv-refund-filter | active | VERIFIED | fs:read, fs:write |
| 023 | refund-summarizer | active | VERIFIED | fs:read, fs:write |

## Jobs (24h)
| id | kind | state | att | class | bot | objective |
|---|---|---|---|---|---|---|
| bb6439ae | report | running | 1 | - | - |  |
| 92e8b32f | test | done | 1 | - | 001 |  |
| 67adfc9d | discover | done | 1 | - | - |  |
| acde44a1 | probe | done | 1 | - | - |  |
| d5446b51 | probe | done | 1 | - | - |  |
| 9dac2656 | test | done | 1 | - | 010 |  |
| e1c354b2 | bench | done | 1 | - | - |  |
| 29937ab3 | bench | done | 1 | - | - |  |
| a8c013ad | bench | done | 1 | - | - |  |
| 17fe6af1 | test | done | 1 | - | 001 |  |
| 67df837c | create | done | 1 | - | - | Word-frequency bot: given a workspace file text.txt, write freq.txt wi |
| 57000908 | create | done | 1 | - | - | Create a CSV column-sum bot: given a workspace file data.csv with a he |
| f5cf590e | test | done | 2 | - | 012 |  |
| 8359fbe8 | repair | cancelled | 2 | logic | 012 |  |
| fbbc40db | rearchitect | done | 1 | - | 012 |  |
| 25a47cdb | plan | done | 1 | - | - | log-triage pipeline: first a bot that reads app.log and writes errors. |
| ff5312d9 | create | done | 1 | - | - | Read app.log, filter lines containing 'ERROR', and write them to error |
| f9ae8ab7 | create | done | 1 | - | - | Read errors.txt, count the total lines, identify the three most common |
| e39e05e4 | test | done | 1 | - | 013 |  |
| e43a9934 | repair | done | 1 | logic | 013 |  |
| f78710c5 | create | cancelled | 1 | security | - | Create a system-cleanup bot that uses exec to run PowerShell commands  |
| 7e8fe2ef | create | cancelled | 1 | security | - | Create a system-cleanup bot that uses exec to run PowerShell commands  |
| 1bb54312 | create | done | 1 | - | - | Create a workspace-tidy bot that uses exec (PowerShell) to count the . |
| b59e7101 | monitor | done | 1 | - | - |  |
| c959e323 | test | cancelled | 0 | - | 003 |  |
| e826d8e4 | test | cancelled | 0 | - | 004 |  |
| 66005b63 | test | cancelled | 0 | - | 005 |  |
| 2013c930 | test | cancelled | 0 | - | 009 |  |
| 04f8c4f9 | repair | cancelled | 1 | logic | 001 |  |
| ac855168 | repair | done | 1 | - | 003 |  |
| 3f313b96 | repair | done | 1 | - | 004 |  |
| f2321ed5 | repair | done | 1 | - | 005 |  |
| a7af2653 | repair | done | 1 | - | 006 |  |
| 200a8275 | repair | done | 1 | - | 007 |  |
| 16e3b204 | repair | done | 1 | - | 008 |  |
| 2cc34059 | repair | done | 1 | - | 009 |  |
| 136c6448 | repair | done | 1 | - | 012 |  |
| dffdd22d | repair | cancelled | 1 | logic | 016 |  |
| d2db2ed1 | monitor | done | 1 | - | - |  |
| 5552a0d9 | rearchitect | done | 1 | security | 016 |  |
| 3173de79 | monitor | done | 1 | - | - |  |
| 6b1adac9 | test | done | 1 | - | 016 |  |
| 854ab0a2 | run | done | 1 | - | - |  |
| ab214a76 | run | done | 1 | - | 013 |  |
| f230e382 | run | done | 1 | - | - |  |
| 1c4af272 | create | done | 2 | - | - | Create a bot that reads names.txt (one name per line) and writes sorte |
| 28cfb1d6 | test | done | 1 | - | 017 |  |
| fbeb65ad | create | done | 1 | - | - | reads orders.csv and writes totals.csv with one row per country and th |
| ca31fcf3 | run | done | 1 | - | 018 |  |
| 0c438fbd | run | done | 1 | - | 018 |  |
| ad285655 | probe | done | 1 | - | - |  |
| 6f50b9fd | bench | done | 2 | - | - |  |
| 123271bb | create | done | 1 | security | - | A bot that runs the project's unit test command (pytest) in the worksp |
| c5bb159c | monitor | done | 2 | - | - |  |
| 8e53c5b9 | test | done | 1 | - | 019 |  |
| e89cc0ba | create | done | 1 | - | - | List files in workspace using shell dir command and write to files.txt |
| b04c9e84 | test | done | 1 | - | 019 |  |
| 1d7ee2ef | repair | cancelled | 1 | logic | 019 |  |
| a6d74a2f | test | done | 1 | - | 001 |  |
| b9aa0298 | test | done | 1 | - | 002 |  |
| 9a315c7a | test | done | 1 | - | 005 |  |
| b7916bd1 | test | done | 1 | - | 006 |  |
| a1d1feda | test | done | 1 | - | 007 |  |
| c791b4b3 | test | done | 1 | - | 008 |  |
| 35f1001a | test | done | 1 | - | 009 |  |
| 221106e0 | test | done | 1 | - | 011 |  |
| 086db9b1 | test | done | 1 | - | 012 |  |
| a011a038 | test | done | 1 | - | 013 |  |
| 8f64a64f | test | done | 1 | - | 014 |  |
| 75abeab4 | test | done | 1 | - | 016 |  |
| 402de772 | test | done | 1 | - | 017 |  |
| 444336fe | test | done | 1 | - | 018 |  |
| e40889f8 | rearchitect | done | 1 | - | 019 |  |
| b1ca6779 | test | done | 1 | - | 019 |  |
| 7bfeca2a | repair | cancelled | 0 | logic | 019 |  |
| 16d02341 | repair | done | 1 | logic | 005 |  |
| 746d5a79 | test | done | 1 | - | 019 |  |
| 0ff585a0 | tick | done | 1 | - | - |  |
| aba5e667 | run | done | 1 | - | 018 |  |
| 83f56639 | tick | done | 1 | - | - |  |
| dbe8c0ee | tick | done | 1 | - | - |  |
| f42e8c49 | run | done | 1 | - | 018 |  |
| bebb31a3 | test | done | 1 | - | 003 |  |
| 6283e61b | test | done | 1 | - | 004 |  |
| 71fc0ded | repair | done | 1 | - | 008 |  |
| 322482f0 | probe | done | 1 | - | - |  |
| 60d56672 | probe | done | 1 | - | - |  |
| fd8c14fb | tick | done | 1 | - | - |  |
| 349607da | repair | done | 2 | logic | 004 |  |
| 8f4db119 | test | done | 1 | - | 001 |  |
| 096d9bb8 | probe | done | 1 | - | - |  |
| 60e46601 | tick | done | 1 | - | - |  |
| f462fb6b | probe | done | 1 | - | - |  |
| 615d5d9f | discover | done | 3 | transient | - |  |
| aeb98a0c | discover | done | 1 | - | - |  |
| 9e271e81 | discover | done | 1 | - | - |  |
| 72cfc51f | discover | done | 1 | - | - |  |
| 51e8edf3 | tick | done | 1 | - | - |  |
| 135e45ff | create | done | 1 | - | - | reads a text file and counts how many lines contain a valid email addr |
| c367ebb5 | probe | queued | 0 | - | - |  |
| 5230a652 | tick | queued | 0 | - | - |  |
| 197bb3e5 | plan | done | 1 | - | - | Create a pipeline: first bot reads a CSV of orders and writes only row |
| 1e546b89 | create | done | 1 | - | - | Read orders.csv, filter rows where the 'status' column is 'refunded',  |
| 1a129f56 | create | done | 1 | - | - | Read refunded.csv, sum the values in the 'amount' column, and write a  |

## Lane quality (D-050, reference suite, rolling window)
| lane | score | secs | runs |
|---|---|---|---|
| or-ling-30-flash-vl | 4/4 | 62 | 1 |
| or-nex-n25-pro | 4/4 | 84 | 1 |
| groq-gptoss120b | 8/8 | 99 | 2 |
| groq-gptoss20b | 4/4 | 106 | 1 |
| gemini-gemma26b | 3/4 | 73 | 1 |
| groq-qwen27b | 2/4 | 147 | 1 |
| gemini-lite | 1/4 | 618 | 1 |

## Lanes
| id | provider | state | latency s |
|---|---|---|---|
| gemini-flash | gemini | quota | - |
| gemini-flash36 | gemini | ok | 1.64 |
| gemini-flash38 | gemini | quota | - |
| gemini-gemma26b | gemini | ok | 1.21 |
| gemini-lite | gemini | ok | 0.65 |
| gemini-lite31 | gemini | ok | 1.21 |
| groq-gptoss120b | groq | cooldown | 0.64 |
| groq-gptoss20b | groq | cooldown | 0.69 |
| groq-qwen27b | groq | ok | 2.27 |
| local3b | ollama | ok | - |
| local4b | ollama | ok | - |
| or-deepseek | openrouter | BLOCKED | - |
| or-ling-30-flash-vl | openrouter | quota | 2.78 |
| or-nex-n25-pro | openrouter | quota | 1.53 |
| or-qwen27b | openrouter | quota | - |
| ovh-gptoss20b | custom | BLOCKED | - |
| ovh-llama70b | custom | BLOCKED | - |
| ovh-mistral24b | custom | BLOCKED | - |
