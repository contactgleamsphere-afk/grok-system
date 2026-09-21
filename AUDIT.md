# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 1 | 2026-09-21 19:39:01 | 0a39c2e1 |  | job.enqueued | owner | {"kind": "create", "payload": {"objective": "Create a JSON-to-Markdown table bot: given a workspace file named records.json containing a JSO |
| 2 | 2026-09-21 19:39:02 | 31ffc26e | 005 | job.enqueued | owner | {"kind": "test", "payload": {"bot_id": "005"}} |
| 3 | 2026-09-21 19:39:04 | fe3b6a6b |  | job.enqueued | owner | {"kind": "monitor", "payload": {"only": ["2", "3"], "day": "2026-09-21"}} |
| 4 | 2026-09-21 19:39:05 | 31ffc26e |  | job.dedup | owner | {"kind": "test"} |
| 5 | 2026-09-21 19:39:07 | 0a39c2e1 |  | job.claimed | w1 | {"attempt": 1} |
| 6 | 2026-09-21 19:40:14 | 0a39c2e1 | 006 | bot.created | w1 | {"name": "json-to-markdown-table", "tools": ["read_file", "write_file"], "permissions": ["fs:read", "fs:write"], "chain": ["groq-gptoss120b" |
| 7 | 2026-09-21 19:40:14 | 0a39c2e1 | 006 | bot.tested | w1 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 PASS 15s [done] expect='2' last='RESULT: 2' \| T3 PASS 24s [done] expect='0'  |
| 8 | 2026-09-21 19:40:14 | 0a39c2e1 | 006 | job.done | w1 | {"summary": {"bot_id": "006", "name": "json-to-markdown-table", "pass": 4, "total": 4, "status": "active", "verified": "VERIFIED"}} |
| 9 | 2026-09-21 19:40:47 | fe3b6a6b |  | job.cancelled | owner | {} |
| 10 | 2026-09-21 19:40:48 | 7c69d3cf |  | job.enqueued | owner | {"kind": "monitor", "payload": {"only": ["002", "003"], "day": "2026-09-21"}} |
| 11 | 2026-09-21 19:40:50 | 7c69d3cf |  | job.claimed | w2 | {"attempt": 1} |
| 12 | 2026-09-21 19:41:32 | 31ffc26e | 005 | job.claimed | w3 | {"attempt": 1} |
| 13 | 2026-09-21 19:42:46 | 31ffc26e |  | job.released | owner | {"uncount": true} |
| 14 | 2026-09-21 19:42:48 | 7c69d3cf |  | job.released | owner | {"uncount": false} |
| 15 | 2026-09-21 19:42:49 | 7c69d3cf |  | job.claimed | w4 | {"attempt": 2} |
| 16 | 2026-09-21 19:45:42 | 7c69d3cf | 002 | bot.monitored | w4 | {"result": "2/2", "before": "active", "after": "active"} |
| 17 | 2026-09-21 19:45:42 | 7c69d3cf | 003 | bot.monitored | w4 | {"result": "4/4", "before": "active", "after": "active"} |
| 18 | 2026-09-21 19:45:42 | 7c69d3cf |  | job.done | w4 | {"summary": {}} |
| 19 | 2026-09-21 19:45:42 | 31ffc26e | 005 | job.claimed | w4 | {"attempt": 1} |
| 20 | 2026-09-21 19:47:49 | 31ffc26e | 005 | bot.tested | w4 | {"result": "T1 PASS 11s [done] expect='X_OK' last='X_OK' \| T2 PASS 47s [done] expect='1' last='RESULT: 1' \| T3 PASS 56s [done] expect='0'  |
| 21 | 2026-09-21 19:47:49 | 31ffc26e | 005 | job.done | w4 | {"summary": {"bot_id": "005", "status": "active", "verified": "VERIFIED"}} |
| 22 | 2026-09-21 19:48:28 | 009ae02a |  | job.enqueued | owner | {"kind": "monitor", "payload": {"only": ["004"], "day": "2026-09-21"}} |
| 23 | 2026-09-21 19:48:30 | 009ae02a |  | job.claimed | w5 | {"attempt": 1} |
| 24 | 2026-09-21 19:50:00 | 009ae02a | 004 | bot.monitored | w5 | {"result": "2/4", "before": "active", "after": "testing"} |
| 25 | 2026-09-21 19:50:00 | 009ae02a | 004 | bot.demoted | w5 | {"to": "testing"} |
| 26 | 2026-09-21 19:50:00 | a5c299d7 | 004 | job.enqueued | w5 | {"kind": "repair", "payload": {"bot_id": "004", "max_rounds": 2}} |
| 27 | 2026-09-21 19:50:00 | 009ae02a |  | job.done | w5 | {"summary": {}} |
| 28 | 2026-09-21 19:50:00 | a5c299d7 | 004 | job.claimed | w5 | {"attempt": 1} |
| 29 | 2026-09-21 19:50:15 | a5c299d7 | 004 | bot.repair | w5 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "gemini:gemini-3.5-flash-lite", "sandbox": null, "rejected": "instruction |
| 30 | 2026-09-21 19:50:15 | a5c299d7 | 004 | job.failed | w5 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 31 | 2026-09-21 19:51:25 | a5c299d7 |  | job.resumed | owner | {} |
| 32 | 2026-09-21 19:51:57 | a5c299d7 |  | job.resumed | owner | {} |
| 33 | 2026-09-21 19:51:58 | a5c299d7 | 004 | job.claimed | w6 | {"attempt": 1} |
| 34 | 2026-09-21 19:54:53 | a5c299d7 | 004 | bot.repair | w6 | {"ok": true, "status": "active", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-120b", "sandbox": "4/4", "rejected": null}], "boundary |
| 35 | 2026-09-21 19:54:53 | a5c299d7 | 004 | bot.promoted | w6 | {"to": "active"} |
| 36 | 2026-09-21 19:54:53 | a5c299d7 | 004 | job.done | w6 | {"summary": {"bot_id": "004", "name": "changelog-writer", "status": "active", "verified": "VERIFIED"}} |
| 37 | 2026-09-21 19:56:25 | efc687cf |  | job.enqueued | master-001 | {"kind": "create", "payload": {"objective": "Create a word-frequency bot: given a workspace text file named input.txt, count how often each  |
| 38 | 2026-09-21 19:56:30 | efc687cf |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 39 | 2026-09-21 19:57:13 | bbafb536 |  | job.enqueued | master-001 | {"kind": "create", "payload": {"objective": "Create a TODO-extractor bot: given a workspace file named notes.txt, find every line containing |
| 40 | 2026-09-21 20:03:25 | efc687cf | 006 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "word-frequency-bot", "tools": ["read_file", "write_file"], "permissions": {"fs:read": ["read_file"], "fs:write": ["write_file"]},  |
| 41 | 2026-09-21 20:03:25 | efc687cf | 006 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] expect='X_OK' last='X_OK' \| T2 PASS 38s [done] expect='apple' last='apple' \| T3 PASS 51s [done] expect='thr |
| 42 | 2026-09-21 20:03:25 | efc687cf | 006 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "006", "name": "word-frequency-bot", "pass": 3, "total": 4, "status": "testing", "verified": "UNVERIFIED"}} |
| 43 | 2026-09-21 20:03:25 | bbafb536 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 44 | 2026-09-21 20:08:36 | 39f42e32 |  | job.enqueued | builder | {"kind": "create", "payload": {"objective": "Create a word-frequency bot: given a workspace text file named input.txt, count how often each  |
| 45 | 2026-09-21 20:10:02 | 39f42e32 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 46 | 2026-09-21 20:10:04 | bbafb536 | 007 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "todo-extractor", "tools": ["read_file", "write_file"], "permissions": {"fs:read": ["read_file"], "fs:write": ["write_file"]}, "cha |
| 47 | 2026-09-21 20:10:04 | bbafb536 | 007 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 14s [done] expect='X_OK' last='+ FullyQualifiedErrorId : NativeCommandError' \| T2 FAIL 108s [done] expect='2' last='aft |
| 48 | 2026-09-21 20:10:04 | bbafb536 | 007 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "name": "todo-extractor", "pass": 1, "total": 4, "status": "testing", "verified": "UNVERIFIED"}} |
| 49 | 2026-09-21 20:21:06 | 74c74bee | 007 | job.enqueued | builder | {"kind": "test", "payload": {"bot_id": "007"}} |
| 50 | 2026-09-21 20:21:09 | 74c74bee | 007 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 51 | 2026-09-21 20:21:41 | 39f42e32 | 008 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "word-frequency-bot", "tools": ["read_file", "write_file"], "permissions": {"fs:read": true, "fs:write": true}, "chain": ["groq-gpt |
| 52 | 2026-09-21 20:21:41 | 39f42e32 | 008 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 303s [TIMEOUT] expect='X_OK' last='' \| T2 PASS 171s [done] expect='apple' last='apple' \| T3 PASS 131s [done] expect='d |
| 53 | 2026-09-21 20:21:41 | 39f42e32 | 008 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "008", "name": "word-frequency-bot", "pass": 3, "total": 4, "status": "testing", "verified": "UNVERIFIED"}} |
| 54 | 2026-09-21 20:28:24 | 74c74bee | 007 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 47s [done] expect='X_OK' last='X_OK' \| T2 PASS 170s [done] expect='2' last='2' \| T3 PASS 128s [done] expect='0' last=' |
| 55 | 2026-09-21 20:28:24 | 74c74bee | 007 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "status": "active", "verified": "VERIFIED"}} |
| 56 | 2026-09-21 20:31:15 | c12a1af9 | 007 | job.enqueued | builder | {"kind": "test", "payload": {"bot_id": "007"}} |
| 57 | 2026-09-21 20:31:16 | c12a1af9 | 007 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 58 | 2026-09-21 20:31:34 | c12a1af9 |  | job.cancelled | owner | {} |
| 59 | 2026-09-21 20:32:25 | c12a1af9 |  | job.cancelled | owner | {} |
| 60 | 2026-09-21 20:32:25 | 5e4217a5 | 008 | job.enqueued | builder | {"kind": "test", "payload": {"bot_id": "008"}} |
| 61 | 2026-09-21 20:32:30 | 5e4217a5 | 008 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 62 | 2026-09-21 20:38:29 | c12a1af9 | 007 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 7s [done] expect='X_OK' last='X_OK' \| T2 PASS 169s [done] expect='2' last='2' \| T3 PASS 169s [done] expect='0' last='0 |
| 63 | 2026-09-21 20:38:29 | c12a1af9 | 007 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "status": "active", "verified": "VERIFIED"}} |
| 64 | 2026-09-21 20:40:22 | 5e4217a5 | 008 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 47s [done] expect='X_OK' last='X_OK' \| T2 PASS 169s [done] expect='apple' last='apple' \| T3 PASS 169s [done] expect='d |
| 65 | 2026-09-21 20:40:22 | 5e4217a5 | 008 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "008", "status": "active", "verified": "VERIFIED"}} |
| 66 | 2026-09-21 20:50:12 | 19628fd7 |  | job.enqueued | builder | {"kind": "monitor", "payload": {"only": ["006", "007", "008"], "day": "2026-09-21"}} |
| 67 | 2026-09-21 20:50:14 | 19628fd7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 68 | 2026-09-21 21:12:15 | 19628fd7 | 006 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "4/4", "before": "active", "after": "active"} |
| 69 | 2026-09-21 21:12:15 | 19628fd7 | 007 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "4/4", "before": "active", "after": "active"} |
| 70 | 2026-09-21 21:12:15 | 19628fd7 | 008 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "4/4", "before": "active", "after": "active"} |
| 71 | 2026-09-21 21:12:15 | 19628fd7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
