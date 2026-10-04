# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 4295 | 2026-10-03 11:14:12 | cc6074e6 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4296 | 2026-10-03 11:16:57 | cc6074e6 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 10s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4297 | 2026-10-03 11:16:57 | cc6074e6 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 10s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4298 | 2026-10-03 11:16:57 | cc6074e6 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4299 | 2026-10-03 11:16:57 | df618110 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "496e3afd58764673a6b80d4e1d7f4792", "retry_of": "cc6074e60d46488e86d85488290b0b0 |
| 4300 | 2026-10-03 11:16:57 | cc6074e6 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4301 | 2026-10-03 11:16:57 | f5bc1e3c | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4302 | 2026-10-03 11:21:00 | f5bc1e3c | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4303 | 2026-10-03 11:21:00 | f5bc1e3c | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4304 | 2026-10-03 11:21:00 | f5bc1e3c | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4305 | 2026-10-03 11:21:00 | f074797d | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "f5bc1e3c866246e7aee83d2a0c15e74 |
| 4306 | 2026-10-03 11:21:00 | f5bc1e3c | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4307 | 2026-10-03 11:21:00 | a05c175f | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4308 | 2026-10-03 11:23:19 | 39387973 |  | job.enqueued | master-001 | {"kind": "create", "payload": {"objective": "Improve the factory weekly self-review to also count how many bots were created"}} |
| 4309 | 2026-10-03 11:23:23 | 39387973 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4310 | 2026-10-03 11:23:25 | 39387973 | 030 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "weekly-self-review-bot-counter", "tools": ["read_file", "write_file"], "permissions": ["fs:read", "fs:write"], "chain": ["gemini-g |
| 4311 | 2026-10-03 11:24:08 | a05c175f | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 9s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [don |
| 4312 | 2026-10-03 11:24:08 | a05c175f | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 9s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [don |
| 4313 | 2026-10-03 11:24:08 | a05c175f | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4314 | 2026-10-03 11:24:08 | 9e73e71a | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "retry_of": "a05c175fc0634f378acd04b68d4eba0 |
| 4315 | 2026-10-03 11:24:08 | a05c175f | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4316 | 2026-10-03 11:24:12 | c1e911a5 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4317 | 2026-10-03 11:24:22 | 39387973 | 030 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 34s [done] expect='X_OK' last='+ FullyQualifiedErrorId : NativeCommandError' \| T2 PASS 10s [done] expect='3' last='RESU |
| 4318 | 2026-10-03 11:24:22 | 965aa88d | 030 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "030", "retest_of": "39387973a2c6440bab2350d11badb420"}} |
| 4319 | 2026-10-03 11:24:22 | 39387973 | 030 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "030", "name": "weekly-self-review-bot-counter", "pass": 2, "total": 4, "status": "testing", "verified": "UNVERIFIED" |
| 4320 | 2026-10-03 11:24:25 | 965aa88d | 030 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4321 | 2026-10-03 11:24:54 | 965aa88d | 030 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 6s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\030.json' \| T2 PASS 10s [done] expect='3' las |
| 4322 | 2026-10-03 11:24:54 | adb5ff47 | 030 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "030", "max_rounds": 2, "rearchitected": false}} |
| 4323 | 2026-10-03 11:24:54 | 965aa88d | 030 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "030", "status": "testing", "verified": "UNVERIFIED"}} |
| 4324 | 2026-10-03 11:24:58 | adb5ff47 | 030 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4325 | 2026-10-03 11:27:56 | adb5ff47 | 030 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": "3/4", "rejected": null}, {"round": 1 |
| 4326 | 2026-10-03 11:27:56 | adb5ff47 | 030 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 4327 | 2026-10-03 11:27:56 | adb5ff47 | 030 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "030", "name": "weekly-self-review-bot-counter", "status": "active", "verified": "VERIFIED"}} |
| 4328 | 2026-10-03 11:28:04 | c1e911a5 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [do |
| 4329 | 2026-10-03 11:28:04 | c1e911a5 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [do |
| 4330 | 2026-10-03 11:28:04 | c1e911a5 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4331 | 2026-10-03 11:28:04 | 9928616b | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "c1e911a56f9940698af7ab87b8b880c |
| 4332 | 2026-10-03 11:28:04 | c1e911a5 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4333 | 2026-10-03 11:28:05 | 8cbe2fa9 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 4334 | 2026-10-03 11:31:03 | 8cbe2fa9 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [d |
| 4335 | 2026-10-03 11:31:03 | 8cbe2fa9 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [d |
| 4336 | 2026-10-03 11:31:03 | 8cbe2fa9 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4337 | 2026-10-03 11:31:03 | eaaf77a7 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "076d00557198429696acd4c0a35af210", "retry_of": "8cbe2fa9803a4814b654f9dbc286a1e |
| 4338 | 2026-10-03 11:31:03 | 8cbe2fa9 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4339 | 2026-10-03 11:42:32 | 9f518f13 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4340 | 2026-10-03 11:45:09 | 9f518f13 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [do |
| 4341 | 2026-10-03 11:45:09 | 9f518f13 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [do |
| 4342 | 2026-10-03 11:45:09 | 9f518f13 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4343 | 2026-10-03 11:45:09 | 5b6778f7 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "9f518f13a3f6482aaf228b68728d841 |
| 4344 | 2026-10-03 11:45:09 | 9f518f13 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4345 | 2026-10-03 11:46:57 | df618110 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4346 | 2026-10-03 11:49:03 | df618110 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4347 | 2026-10-03 11:49:03 | df618110 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4348 | 2026-10-03 11:49:03 | df618110 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4349 | 2026-10-03 11:49:03 | ebeb00d9 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "496e3afd58764673a6b80d4e1d7f4792", "retry_of": "df61811016a34db78e4b85b73b227fe |
| 4350 | 2026-10-03 11:49:03 | df618110 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4351 | 2026-10-03 11:51:01 | f074797d | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4352 | 2026-10-03 11:53:51 | f074797d | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 10s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4353 | 2026-10-03 11:53:51 | f074797d | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 10s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4354 | 2026-10-03 11:53:51 | f074797d | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4355 | 2026-10-03 11:53:51 | aeb856dd | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "f074797d764444b98a6a3bf3940af76 |
| 4356 | 2026-10-03 11:53:51 | f074797d | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4357 | 2026-10-03 11:54:10 | 9e73e71a | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4358 | 2026-10-03 11:57:12 | 9e73e71a | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [d |
| 4359 | 2026-10-03 11:57:12 | 9e73e71a | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [d |
| 4360 | 2026-10-03 11:57:12 | 9e73e71a | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4361 | 2026-10-03 11:57:12 | 88b3f1c4 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "retry_of": "9e73e71a93864c7589728633d9edf63 |
| 4362 | 2026-10-03 11:57:12 | 9e73e71a | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4363 | 2026-10-03 11:58:06 | 9928616b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4364 | 2026-10-03 12:00:46 | 9928616b | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [do |
| 4365 | 2026-10-03 12:00:46 | 9928616b | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [do |
| 4366 | 2026-10-03 12:00:46 | 9928616b | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4367 | 2026-10-03 12:00:46 | 52cdfc83 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "9928616b52a047a998e1548273d5744 |
| 4368 | 2026-10-03 12:00:46 | 9928616b | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4369 | 2026-10-03 12:01:03 | eaaf77a7 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4370 | 2026-10-03 12:09:44 | eaaf77a7 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 4371 | 2026-10-03 12:09:44 | eaaf77a7 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 4372 | 2026-10-03 12:09:44 | 7791cfd1 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "eaaf77a7b4ff439c830c6b7949a76355", "after_quota": "eaaf77a7b4ff439c830c6b7949a76 |
| 4373 | 2026-10-03 12:09:44 | eaaf77a7 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4374 | 2026-10-03 12:12:36 | 6453139b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4375 | 2026-10-03 12:12:36 | 70c181a5 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T13"}} |
| 4376 | 2026-10-03 12:12:57 | 6453139b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "gr |
| 4377 | 2026-10-03 12:13:06 | 80da9646 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4378 | 2026-10-03 12:13:06 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4379 | 2026-10-03 12:13:07 | e7478817 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T13"}} |
| 4380 | 2026-10-03 12:13:07 | 80da9646 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4381 | 2026-10-03 12:15:11 | 5b6778f7 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4382 | 2026-10-03 12:28:31 | 5b6778f7 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [do |
| 4383 | 2026-10-03 12:28:31 | 5b6778f7 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [do |
| 4384 | 2026-10-03 12:28:31 | f4c035f5 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5b6778f745304b77970b63b5b66bcf37", "after_quota": "5b6778f745304b77970b63b5b66bc |
| 4385 | 2026-10-03 12:28:31 | 5b6778f7 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4386 | 2026-10-03 12:28:34 | ebeb00d9 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4387 | 2026-10-03 12:41:01 | ebeb00d9 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 4388 | 2026-10-03 12:41:01 | ebeb00d9 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 4389 | 2026-10-03 12:41:01 | b2987a9a | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ebeb00d9ad6a4a4b8186056ccf5c3196", "after_quota": "ebeb00d9ad6a4a4b8186056ccf5c3 |
| 4390 | 2026-10-03 12:41:01 | ebeb00d9 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4391 | 2026-10-03 12:41:05 | aeb856dd | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4392 | 2026-10-03 12:53:32 | aeb856dd | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 41s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 4393 | 2026-10-03 12:53:32 | aeb856dd | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 41s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 4394 | 2026-10-03 12:53:32 | 91683a5e | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "aeb856dd164049c2891f58c9d8248e0f", "after_quota": "aeb856dd164049c2891f58c9d8248 |
| 4395 | 2026-10-03 12:53:32 | aeb856dd | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4396 | 2026-10-03 12:53:36 | 88b3f1c4 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4397 | 2026-10-03 13:06:46 | 88b3f1c4 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4398 | 2026-10-03 13:06:46 | 88b3f1c4 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4399 | 2026-10-03 13:06:46 | 4014c5d9 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "88b3f1c4827a4f3e95248a3f8017f9fc", "after_quota": "88b3f1c4827a4f3e95248a3f8017f |
| 4400 | 2026-10-03 13:06:46 | 88b3f1c4 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4401 | 2026-10-03 13:06:47 | 52cdfc83 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4402 | 2026-10-03 13:12:41 | 70c181a5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4403 | 2026-10-03 13:12:41 | 30d2a0d2 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T14"}} |
| 4404 | 2026-10-03 13:13:08 | 70c181a5 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 4405 | 2026-10-03 13:13:08 | 090b5ee6 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4406 | 2026-10-03 13:13:08 | 8583a832 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4407 | 2026-10-03 13:13:08 | fa27c6c8 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4408 | 2026-10-03 13:13:08 | f9702150 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4409 | 2026-10-03 13:13:08 | 74d04bfc |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4410 | 2026-10-03 13:13:08 | 7a60f27a |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4411 | 2026-10-03 13:13:08 | 70c181a5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "gr |
| 4412 | 2026-10-03 13:13:12 | e7478817 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4413 | 2026-10-03 13:13:12 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4414 | 2026-10-03 13:13:13 | 47e72b7d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T14"}} |
| 4415 | 2026-10-03 13:13:13 | e7478817 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4416 | 2026-10-03 13:13:17 | 090b5ee6 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4417 | 2026-10-03 13:13:18 | 090b5ee6 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4418 | 2026-10-03 13:13:22 | 8583a832 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4419 | 2026-10-03 13:13:23 | 8583a832 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4420 | 2026-10-03 13:13:27 | fa27c6c8 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4421 | 2026-10-03 13:13:30 | fa27c6c8 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4422 | 2026-10-03 13:13:35 | f9702150 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4423 | 2026-10-03 13:13:35 | f9702150 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4424 | 2026-10-03 13:13:39 | 74d04bfc |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4425 | 2026-10-03 13:13:39 | 74d04bfc |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4426 | 2026-10-03 13:13:43 | 7a60f27a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4427 | 2026-10-03 13:13:43 | 7a60f27a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4428 | 2026-10-03 13:20:04 | 52cdfc83 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4429 | 2026-10-03 13:20:04 | 52cdfc83 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4430 | 2026-10-03 13:20:04 | c4ba12f8 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "52cdfc8326cb4d02890da99fe7ba0b4c", "after_quota": "52cdfc8326cb4d02890da99fe7ba0 |
| 4431 | 2026-10-03 13:20:04 | 52cdfc83 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4432 | 2026-10-03 14:09:46 | 7791cfd1 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4433 | 2026-10-03 14:12:42 | 30d2a0d2 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4434 | 2026-10-03 14:12:42 | ae553c47 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T15"}} |
| 4435 | 2026-10-03 14:13:08 | 30d2a0d2 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 4436 | 2026-10-03 14:13:08 | 30d2a0d2 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gp |
| 4437 | 2026-10-03 14:13:18 | 47e72b7d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4438 | 2026-10-03 14:13:18 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4439 | 2026-10-03 14:13:19 | 6b090e08 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T15"}} |
| 4440 | 2026-10-03 14:13:19 | 47e72b7d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4441 | 2026-10-03 14:22:51 | 7791cfd1 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 75s [done] report expect='FACTORY' cmd=True \| T3 PASS 73s [d |
| 4442 | 2026-10-03 14:22:51 | 7791cfd1 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 75s [done] report expect='FACTORY' cmd=True \| T3 PASS 73s [d |
| 4443 | 2026-10-03 14:22:51 | 1811ab9e | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "eaaf77a7b4ff439c830c6b7949a76355", "after_quota": "7791cfd117e5456da042251bfa430 |
| 4444 | 2026-10-03 14:22:51 | 7791cfd1 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4445 | 2026-10-03 16:10:49 | ae553c47 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4446 | 2026-10-03 16:10:50 | 6b090e08 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4447 | 2026-10-03 16:10:51 | c9049357 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T17"}} |
| 4448 | 2026-10-03 16:10:51 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4449 | 2026-10-03 16:10:58 | 9b82e36b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T17"}} |
| 4450 | 2026-10-03 16:10:58 | 6b090e08 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4451 | 2026-10-03 16:11:03 | f4c035f5 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4452 | 2026-10-03 16:11:40 | ae553c47 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemi |
| 4453 | 2026-10-03 16:23:50 | f4c035f5 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 94s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 4454 | 2026-10-03 16:23:50 | f4c035f5 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 94s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 4455 | 2026-10-03 16:23:50 | 9bce9ff8 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5b6778f745304b77970b63b5b66bcf37", "after_quota": "f4c035f524374f2b8d335e9cc62c8 |
| 4456 | 2026-10-03 16:23:50 | f4c035f5 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4457 | 2026-10-03 16:23:54 | b2987a9a | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4458 | 2026-10-03 16:36:26 | b2987a9a | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4459 | 2026-10-03 16:36:26 | b2987a9a | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4460 | 2026-10-03 16:36:26 | ca238808 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ebeb00d9ad6a4a4b8186056ccf5c3196", "after_quota": "b2987a9ab34c4f9b943c555412d7a |
| 4461 | 2026-10-03 16:36:26 | b2987a9a | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4462 | 2026-10-03 16:36:30 | 91683a5e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4463 | 2026-10-03 16:48:57 | 91683a5e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 4464 | 2026-10-03 16:48:57 | 91683a5e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 4465 | 2026-10-03 16:48:57 | 70406b7d | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "aeb856dd164049c2891f58c9d8248e0f", "after_quota": "91683a5e976743ad81af9e3b1b693 |
| 4466 | 2026-10-03 16:48:57 | 91683a5e | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4467 | 2026-10-03 16:49:00 | 4014c5d9 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4468 | 2026-10-03 17:01:37 | 4014c5d9 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4469 | 2026-10-03 17:01:37 | 4014c5d9 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4470 | 2026-10-03 17:01:37 | 28936172 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "88b3f1c4827a4f3e95248a3f8017f9fc", "after_quota": "4014c5d9abc54ea0bc24da7d99b45 |
| 4471 | 2026-10-03 17:01:37 | 4014c5d9 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4472 | 2026-10-03 17:01:40 | c4ba12f8 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4473 | 2026-10-03 17:10:52 | c9049357 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4474 | 2026-10-03 17:10:52 | b160cb81 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T18"}} |
| 4475 | 2026-10-03 17:11:18 | c9049357 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 4476 | 2026-10-03 17:11:18 | 34937a4e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4477 | 2026-10-03 17:11:18 | 4feb3742 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4478 | 2026-10-03 17:11:18 | 33306e02 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4479 | 2026-10-03 17:11:18 | 3a5ef1c6 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4480 | 2026-10-03 17:11:18 | e38dbc3f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4481 | 2026-10-03 17:11:18 | dfffb806 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4482 | 2026-10-03 17:11:18 | c9049357 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qw |
| 4483 | 2026-10-03 17:11:22 | 9b82e36b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4484 | 2026-10-03 17:11:22 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4485 | 2026-10-03 17:11:22 | 7c4c7496 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T18"}} |
| 4486 | 2026-10-03 17:11:22 | 9b82e36b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4487 | 2026-10-03 17:11:25 | 34937a4e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4488 | 2026-10-03 17:11:25 | 34937a4e |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4489 | 2026-10-03 17:11:29 | 4feb3742 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4490 | 2026-10-03 17:11:29 | 4feb3742 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4491 | 2026-10-03 17:11:33 | 33306e02 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4492 | 2026-10-03 17:11:33 | 33306e02 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4493 | 2026-10-03 17:11:36 | 3a5ef1c6 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4494 | 2026-10-03 17:11:36 | 3a5ef1c6 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4495 | 2026-10-03 17:11:39 | e38dbc3f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4496 | 2026-10-03 17:11:39 | e38dbc3f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4497 | 2026-10-03 17:11:42 | dfffb806 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4498 | 2026-10-03 17:11:42 | dfffb806 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4499 | 2026-10-03 17:13:58 | c4ba12f8 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 4500 | 2026-10-03 17:13:58 | c4ba12f8 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 4501 | 2026-10-03 17:13:58 | bdd006b0 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "52cdfc8326cb4d02890da99fe7ba0b4c", "after_quota": "c4ba12f8869b4bc7b98cb6549eccb |
| 4502 | 2026-10-03 17:13:58 | c4ba12f8 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4503 | 2026-10-03 17:14:01 | 1811ab9e | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4504 | 2026-10-03 17:26:56 | 1811ab9e | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4505 | 2026-10-03 17:26:56 | 1811ab9e | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4506 | 2026-10-03 17:26:56 | 0013387b | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "eaaf77a7b4ff439c830c6b7949a76355", "after_quota": "1811ab9ef1394a738ac0b9d34fe47 |
| 4507 | 2026-10-03 17:26:56 | 1811ab9e | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4508 | 2026-10-03 18:10:53 | b160cb81 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4509 | 2026-10-03 18:10:53 | 3e606ba8 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T19"}} |
| 4510 | 2026-10-03 18:11:27 | 7c4c7496 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4511 | 2026-10-03 18:11:27 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4512 | 2026-10-03 18:11:27 | f5fee259 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T19"}} |
| 4513 | 2026-10-03 18:11:27 | 7c4c7496 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4514 | 2026-10-03 18:12:01 | b160cb81 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 4515 | 2026-10-03 18:12:01 | b160cb81 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwe |
| 4516 | 2026-10-03 18:23:52 | 9bce9ff8 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4517 | 2026-10-03 18:36:28 | 9bce9ff8 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 87s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [do |
| 4518 | 2026-10-03 18:36:28 | 9bce9ff8 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 87s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [do |
| 4519 | 2026-10-03 18:36:28 | e203c351 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5b6778f745304b77970b63b5b66bcf37", "after_quota": "9bce9ff87cb549b6b310b187092c5 |
| 4520 | 2026-10-03 18:36:28 | 9bce9ff8 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4521 | 2026-10-03 18:36:30 | ca238808 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4522 | 2026-10-03 18:49:20 | ca238808 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4523 | 2026-10-03 18:49:20 | ca238808 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4524 | 2026-10-03 18:49:20 | d423a523 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ebeb00d9ad6a4a4b8186056ccf5c3196", "after_quota": "ca2388084a454ec997f6f858e794a |
| 4525 | 2026-10-03 18:49:20 | ca238808 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4526 | 2026-10-03 18:49:22 | 70406b7d | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4527 | 2026-10-03 19:02:22 | 70406b7d | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 75s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 4528 | 2026-10-03 19:02:22 | 70406b7d | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 75s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 4529 | 2026-10-03 19:02:22 | 7054866c | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "aeb856dd164049c2891f58c9d8248e0f", "after_quota": "70406b7d0c7840ec9957fb0225e69 |
| 4530 | 2026-10-03 19:02:22 | 70406b7d | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4531 | 2026-10-03 19:02:25 | 28936172 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4532 | 2026-10-03 19:10:56 | 3e606ba8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4533 | 2026-10-03 19:10:56 | 8de380de |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T20"}} |
| 4534 | 2026-10-03 19:12:09 | 3e606ba8 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 4535 | 2026-10-03 19:12:09 | 5d0438a1 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4536 | 2026-10-03 19:12:09 | 7b57e6cb |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4537 | 2026-10-03 19:12:09 | 96ca3eae |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4538 | 2026-10-03 19:12:09 | f7ccc654 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4539 | 2026-10-03 19:12:09 | 8bb50c87 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4540 | 2026-10-03 19:12:09 | 10db6ef6 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4541 | 2026-10-03 19:12:09 | 3e606ba8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash-latest", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", " |
| 4542 | 2026-10-03 19:12:12 | f5fee259 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4543 | 2026-10-03 19:12:12 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4544 | 2026-10-03 19:12:12 | 2b1c3328 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T20"}} |
| 4545 | 2026-10-03 19:12:12 | f5fee259 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4546 | 2026-10-03 19:12:15 | 5d0438a1 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4547 | 2026-10-03 19:12:16 | 5d0438a1 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4548 | 2026-10-03 19:12:19 | 7b57e6cb |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4549 | 2026-10-03 19:12:19 | 7b57e6cb |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4550 | 2026-10-03 19:12:22 | 96ca3eae |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4551 | 2026-10-03 19:12:22 | 96ca3eae |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4552 | 2026-10-03 19:12:26 | f7ccc654 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4553 | 2026-10-03 19:12:26 | f7ccc654 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4554 | 2026-10-03 19:12:29 | 8bb50c87 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4555 | 2026-10-03 19:12:29 | 8bb50c87 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4556 | 2026-10-03 19:12:32 | 10db6ef6 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4557 | 2026-10-03 19:12:32 | 10db6ef6 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4558 | 2026-10-03 19:15:54 | 28936172 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 76s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 4559 | 2026-10-03 19:15:54 | 28936172 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 76s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 4560 | 2026-10-03 19:15:54 | dcf400b5 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "88b3f1c4827a4f3e95248a3f8017f9fc", "after_quota": "28936172ea17466a9dc41918106b6 |
| 4561 | 2026-10-03 19:15:54 | 28936172 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4562 | 2026-10-03 19:15:55 | bdd006b0 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4563 | 2026-10-03 19:30:36 | bdd006b0 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 46s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 113s [done] report expect='FACTORY' cmd=True \| T3 PASS 95s [ |
| 4564 | 2026-10-03 19:30:36 | bdd006b0 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 46s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 113s [done] report expect='FACTORY' cmd=True \| T3 PASS 95s [ |
| 4565 | 2026-10-03 19:30:36 | cd511712 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "52cdfc8326cb4d02890da99fe7ba0b4c", "after_quota": "bdd006b0c04a4255b89511894d31e |
| 4566 | 2026-10-03 19:30:36 | bdd006b0 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4567 | 2026-10-03 19:30:38 | 0013387b | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4568 | 2026-10-03 19:44:34 | 0013387b | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 4569 | 2026-10-03 19:44:34 | 0013387b | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 4570 | 2026-10-03 19:44:34 | 9452394f | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "eaaf77a7b4ff439c830c6b7949a76355", "after_quota": "0013387be52c4f47930485ed4b975 |
| 4571 | 2026-10-03 19:44:34 | 0013387b | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4572 | 2026-10-03 20:10:58 | 8de380de |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4573 | 2026-10-03 20:10:58 | ab903e40 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T21"}} |
| 4574 | 2026-10-03 20:11:45 | 8de380de |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 4575 | 2026-10-03 20:11:45 | 8de380de |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemma26b", "groq-gptoss120b", "g |
| 4576 | 2026-10-03 20:12:13 | 2b1c3328 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4577 | 2026-10-03 20:12:13 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4578 | 2026-10-03 20:12:14 | c5c8de46 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T21"}} |
| 4579 | 2026-10-03 20:12:14 | 2b1c3328 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4580 | 2026-10-03 20:36:31 | e203c351 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4581 | 2026-10-03 20:50:02 | e203c351 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 76s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [do |
| 4582 | 2026-10-03 20:50:02 | e203c351 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 76s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [do |
| 4583 | 2026-10-03 20:50:02 | 29eba64b | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5b6778f745304b77970b63b5b66bcf37", "after_quota": "e203c35185654d1fb292fbb3028be |
| 4584 | 2026-10-03 20:50:02 | e203c351 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4585 | 2026-10-03 20:50:06 | d423a523 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4586 | 2026-10-03 21:04:24 | d423a523 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 43s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 84s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 4587 | 2026-10-03 21:04:24 | d423a523 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 43s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 84s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 4588 | 2026-10-03 21:04:24 | cc838b03 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ebeb00d9ad6a4a4b8186056ccf5c3196", "after_quota": "d423a523159c4481ac99ac3afd691 |
| 4589 | 2026-10-03 21:04:24 | d423a523 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4590 | 2026-10-03 21:04:28 | 7054866c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4591 | 2026-10-03 21:10:58 | ab903e40 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4592 | 2026-10-03 21:10:58 | d071eb0a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T22"}} |
| 4593 | 2026-10-03 21:11:26 | ab903e40 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemma26b", "groq-gptoss120b", "groq-gptoss20b",  |
| 4594 | 2026-10-03 21:12:15 | c5c8de46 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4595 | 2026-10-03 21:12:15 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4596 | 2026-10-03 21:12:15 | fdb14c2e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T22"}} |
| 4597 | 2026-10-03 21:12:15 | c5c8de46 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4598 | 2026-10-03 21:23:00 | 7054866c | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 82s [done] report expect='FACTORY' cmd=True \| T3 PASS 104s [ |
| 4599 | 2026-10-03 21:23:00 | 7054866c | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 82s [done] report expect='FACTORY' cmd=True \| T3 PASS 104s [ |
| 4600 | 2026-10-03 21:23:00 | a38a7043 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "aeb856dd164049c2891f58c9d8248e0f", "after_quota": "7054866c11384415b5ccc89a6b409 |
| 4601 | 2026-10-03 21:23:00 | 7054866c | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4602 | 2026-10-03 21:23:04 | dcf400b5 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4603 | 2026-10-03 21:45:11 | dcf400b5 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 4604 | 2026-10-03 21:45:16 | cd511712 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4605 | 2026-10-03 22:07:23 | cd511712 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 4606 | 2026-10-03 22:07:27 | dcf400b5 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 4607 | 2026-10-03 22:11:03 | d071eb0a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4608 | 2026-10-03 22:11:03 | b2e299d3 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T23"}} |
| 4609 | 2026-10-03 22:11:24 | d071eb0a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemma26b", "groq-gptoss120b", "groq-gptoss20b",  |
| 4610 | 2026-10-03 22:12:18 | fdb14c2e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4611 | 2026-10-03 22:12:18 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4612 | 2026-10-03 22:12:19 | 6960ee36 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T23"}} |
| 4613 | 2026-10-03 22:12:19 | fdb14c2e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4614 | 2026-10-03 22:29:34 | dcf400b5 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 4615 | 2026-10-03 22:29:37 | cd511712 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 4616 | 2026-10-03 22:51:49 | cd511712 | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 4617 | 2026-10-03 22:51:50 | dcf400b5 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 4618 | 2026-10-03 23:11:08 | b2e299d3 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4619 | 2026-10-03 23:11:08 | eddcd50c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-04T00"}} |
| 4620 | 2026-10-03 23:11:39 | b2e299d3 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-gemma26b", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b" |
| 4621 | 2026-10-03 23:12:20 | 6960ee36 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4622 | 2026-10-03 23:12:20 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4623 | 2026-10-03 23:12:20 | 83500f74 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-04T00"}} |
| 4624 | 2026-10-03 23:12:20 | 6960ee36 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4625 | 2026-10-03 23:13:59 | dcf400b5 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "failed", "attempt": 3, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 4626 | 2026-10-03 23:13:59 | cd511712 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 4627 | 2026-10-03 23:58:57 | cd511712 |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 4628 | 2026-10-03 23:58:58 | 9452394f | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4629 | 2026-10-04 13:43:15 | cd511712 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 72s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 145s [done] report expect='FACTORY' cmd=False \| T3 FAIL 247s |
| 4630 | 2026-10-04 13:43:15 | cd511712 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 72s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 145s [done] report expect='FACTORY' cmd=False \| T3 FAIL 247s |
| 4631 | 2026-10-04 13:43:15 | cd511712 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4632 | 2026-10-04 13:43:18 | aa91a845 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "cd511712d59a4ac8a881a9cfe5d9986 |
| 4633 | 2026-10-04 13:43:18 | cd511712 |  | job.readopted | fast-LAPTOP-LRE6PSA8 | {} |
| 4634 | 2026-10-04 13:43:18 | cd511712 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 1, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4635 | 2026-10-04 13:43:28 | 9452394f |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 4636 | 2026-10-04 13:43:28 | eddcd50c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4637 | 2026-10-04 13:43:28 | 3d977ea8 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-04T14"}} |
| 4638 | 2026-10-04 13:43:40 | e3e27be7 |  | job.enqueued | nightly-task | {"kind": "monitor", "payload": {"only": null, "day": "2026-10-04"}} |
| 4639 | 2026-10-04 13:43:44 | 9452394f |  | job.readopted | svc-LAPTOP-LRE6PSA8 | {} |
| 4640 | 2026-10-04 13:44:00 | eddcd50c |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "or-apodex-11-mini", "outcome": "ok", "before": "INFERRED", "after": "VERIFIED", "detail": null} |
| 4641 | 2026-10-04 13:44:00 | eddcd50c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemi |
| 4642 | 2026-10-04 13:44:05 | 83500f74 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4643 | 2026-10-04 13:44:05 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4644 | 2026-10-04 13:44:06 | b3e37bd2 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-04T14"}} |
| 4645 | 2026-10-04 13:44:06 | 83500f74 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4646 | 2026-10-04 13:44:10 | 091fe87e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4647 | 2026-10-04 13:44:10 | 091fe87e |  | audit.verified | fast-LAPTOP-LRE6PSA8 | {"rows": 4645, "hashed": 3893, "first_bad": null} |
| 4648 | 2026-10-04 13:44:10 | b0113ecf |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-10-05"}} |
| 4649 | 2026-10-04 13:44:10 | cf0d36ff |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-10-04"}} |
| 4650 | 2026-10-04 13:44:10 | 21de43e4 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-10-04"}} |
| 4651 | 2026-10-04 13:44:10 | 091fe87e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4652 | 2026-10-04 13:48:35 | 9452394f | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 4653 | 2026-10-04 13:48:35 | 29eba64b | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4654 | 2026-10-04 13:48:39 | e3e27be7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4655 | 2026-10-04 13:48:39 | 3a6cb779 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "e3e27be7486c486399ca49575cec8d90", "day": "2026-10-04"}} |
| 4656 | 2026-10-04 13:48:39 | cd8d97ae | 028 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "028", "monitor_of": "e3e27be7486c486399ca49575cec8d90", "day": "2026-10-04"}} |
| 4657 | 2026-10-04 13:48:39 | 1a0a33c6 | 029 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "029", "monitor_of": "e3e27be7486c486399ca49575cec8d90", "day": "2026-10-04"}} |
| 4658 | 2026-10-04 13:48:39 | 10c3b87f | 030 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "030", "monitor_of": "e3e27be7486c486399ca49575cec8d90", "day": "2026-10-04"}} |
| 4659 | 2026-10-04 13:48:39 | e3e27be7 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "028", "029", "030"], "jobs": ["3a6cb779", "cd8d97ae", "1a0a33c6", "10c3b87f"]} |
| 4660 | 2026-10-04 13:48:39 | e3e27be7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4661 | 2026-10-04 13:48:43 | cd8d97ae | 028 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4662 | 2026-10-04 13:49:25 | cd8d97ae | 028 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 5s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\028.json' \| T2 PASS 17s [done] expect='3' las |
| 4663 | 2026-10-04 13:49:25 | cd8d97ae | 028 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 5s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\028.json' \| T2 PASS 17s [done] expect='3' las |
| 4664 | 2026-10-04 13:49:25 | cd8d97ae | 028 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4665 | 2026-10-04 13:49:25 | 24eeae92 | 028 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "028", "max_rounds": 2}} |
| 4666 | 2026-10-04 13:49:25 | cd8d97ae | 028 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "028", "status": "testing", "verified": "UNVERIFIED"}} |
| 4667 | 2026-10-04 13:49:29 | 24eeae92 | 028 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4668 | 2026-10-04 13:52:52 | 24eeae92 | 028 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": "3/4", "rejected": null}, {"round": 2 |
| 4669 | 2026-10-04 13:52:52 | 24eeae92 | 028 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 4670 | 2026-10-04 13:52:52 | 24eeae92 | 028 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "028", "name": "weekly-self-review", "status": "active", "verified": "VERIFIED"}} |
| 4671 | 2026-10-04 13:52:58 | 1a0a33c6 | 029 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4672 | 2026-10-04 13:53:17 | 29eba64b | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 20s [done] report expect='FACTORY' cmd=True \| T3 PASS 19s [d |
| 4673 | 2026-10-04 13:53:17 | 29eba64b | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 20s [done] report expect='FACTORY' cmd=True \| T3 PASS 19s [d |
| 4674 | 2026-10-04 13:53:17 | 29eba64b | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4675 | 2026-10-04 13:53:17 | f4adcc9c | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "29eba64b2db24eb880cbcbebfdb107a |
| 4676 | 2026-10-04 13:53:17 | 29eba64b | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4677 | 2026-10-04 13:53:24 | 9452394f | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 4678 | 2026-10-04 13:53:57 | 1a0a33c6 | 029 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] expect='X_OK' last='X_OK' \| T2 FAIL 10s [done] expect='3' last='Using config: C:\\AI\\Factory\\run\\botcfg\\ |
| 4679 | 2026-10-04 13:53:57 | 1a0a33c6 | 029 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] expect='X_OK' last='X_OK' \| T2 FAIL 10s [done] expect='3' last='Using config: C:\\AI\\Factory\\run\\botcfg\\ |
| 4680 | 2026-10-04 13:53:57 | 1a0a33c6 | 029 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4681 | 2026-10-04 13:53:57 | 70811e2d |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "repair"} |
| 4682 | 2026-10-04 13:53:57 | 1a0a33c6 | 029 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "029", "status": "testing", "verified": "UNVERIFIED"}} |
| 4683 | 2026-10-04 13:54:02 | 10c3b87f | 030 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4684 | 2026-10-04 13:54:50 | 10c3b87f | 030 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='X_OK' last='X_OK' \| T2 PASS 16s [done] expect='3' last='3' \| T3 FAIL 2s [done] expect='2' last='' \ |
| 4685 | 2026-10-04 13:54:50 | 10c3b87f | 030 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='X_OK' last='X_OK' \| T2 PASS 16s [done] expect='3' last='3' \| T3 FAIL 2s [done] expect='2' last='' \ |
| 4686 | 2026-10-04 13:54:50 | 10c3b87f | 030 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4687 | 2026-10-04 13:54:50 | f5e51726 | 030 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "030", "max_rounds": 2}} |
| 4688 | 2026-10-04 13:54:50 | 10c3b87f | 030 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "030", "status": "testing", "verified": "UNVERIFIED"}} |
| 4689 | 2026-10-04 13:54:56 | f5e51726 | 030 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4690 | 2026-10-04 13:57:18 | 9452394f | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 20s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 4691 | 2026-10-04 13:57:18 | 9452394f | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 20s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 4692 | 2026-10-04 13:57:18 | 9452394f | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4693 | 2026-10-04 13:57:18 | 8fd667bf | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "076d00557198429696acd4c0a35af210", "retry_of": "9452394ffc1841c0bec59f9cd496cc4 |
| 4694 | 2026-10-04 13:57:18 | 9452394f | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
