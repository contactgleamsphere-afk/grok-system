# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 5415 | 2026-10-07 15:30:09 | 17c55e79 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5416 | 2026-10-07 15:31:01 | e9f39103 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5417 | 2026-10-07 15:31:01 | e9f39103 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5418 | 2026-10-07 15:31:05 | fb296dd4 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5419 | 2026-10-07 15:31:05 | fb296dd4 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5420 | 2026-10-07 15:31:10 | 365a4bf4 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5421 | 2026-10-07 15:31:10 | 365a4bf4 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5422 | 2026-10-07 15:31:14 | a1c8b352 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5423 | 2026-10-07 15:31:14 | a1c8b352 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5424 | 2026-10-07 15:31:18 | 879e06a3 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 5425 | 2026-10-07 15:35:22 | 879e06a3 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 16s [d |
| 5426 | 2026-10-07 15:35:22 | 879e06a3 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 16s [d |
| 5427 | 2026-10-07 15:35:22 | 879e06a3 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5428 | 2026-10-07 15:35:22 | 328c36fa | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "879e06a341fb4ff28542ceda90e4157 |
| 5429 | 2026-10-07 15:35:22 | 879e06a3 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5430 | 2026-10-07 15:35:26 | 989112db | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5431 | 2026-10-07 15:36:01 | 453de9e9 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5432 | 2026-10-07 15:36:01 | 453de9e9 |  | audit.verified | svc-LAPTOP-LRE6PSA8 | {"rows": 5429, "hashed": 4677, "first_bad": null} |
| 5433 | 2026-10-07 15:36:01 | 0490db0c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-10-08"}} |
| 5434 | 2026-10-07 15:36:01 | 4bf074c7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-10-07"}} |
| 5435 | 2026-10-07 15:36:01 | 06d62a7e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-10-07"}} |
| 5436 | 2026-10-07 15:36:01 | f174fbc6 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-10-07"}} |
| 5437 | 2026-10-07 15:36:01 | 453de9e9 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5438 | 2026-10-07 15:36:06 | f174fbc6 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5439 | 2026-10-07 15:36:06 | dc90fd03 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "f174fbc671544e27bad96250dd6ea9e2", "day": "2026-10-07"}} |
| 5440 | 2026-10-07 15:36:06 | ee508172 | 028 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "028", "monitor_of": "f174fbc671544e27bad96250dd6ea9e2", "day": "2026-10-07"}} |
| 5441 | 2026-10-07 15:36:06 | 996de8af | 031 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "031", "monitor_of": "f174fbc671544e27bad96250dd6ea9e2", "day": "2026-10-07"}} |
| 5442 | 2026-10-07 15:36:06 | d49e60c4 | 033 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "033", "monitor_of": "f174fbc671544e27bad96250dd6ea9e2", "day": "2026-10-07"}} |
| 5443 | 2026-10-07 15:36:06 | f174fbc6 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "028", "031", "033"], "jobs": ["dc90fd03", "ee508172", "996de8af", "d49e60c4"]} |
| 5444 | 2026-10-07 15:36:06 | f174fbc6 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5445 | 2026-10-07 15:36:10 | ee508172 | 028 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5446 | 2026-10-07 15:46:10 | ee508172 | 028 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 5s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\028.json' \| T2 FAIL 117s [done] expect='3' la |
| 5447 | 2026-10-07 15:46:10 | ee508172 | 028 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 5s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\028.json' \| T2 FAIL 117s [done] expect='3' la |
| 5448 | 2026-10-07 15:46:10 | 704fa219 | 028 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "028", "retest_of": "ee508172d0bc4293b1e4245d206a0b49", "after_quota": "ee508172d0bc4293b1e4245d206a0 |
| 5449 | 2026-10-07 15:46:10 | ee508172 | 028 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "028", "status": "active", "verified": "VERIFIED"}} |
| 5450 | 2026-10-07 15:46:17 | 996de8af | 031 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5451 | 2026-10-07 15:48:26 | 996de8af | 031 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 46s [done] expect='X_OK' last='X_OK' \| T2 FAIL 10s [done] expect='3' last='Using config: C:\\AI\\Factory\\run\\botcfg\\ |
| 5452 | 2026-10-07 15:48:26 | 996de8af | 031 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 46s [done] expect='X_OK' last='X_OK' \| T2 FAIL 10s [done] expect='3' last='Using config: C:\\AI\\Factory\\run\\botcfg\\ |
| 5453 | 2026-10-07 15:48:26 | 996de8af | 031 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5454 | 2026-10-07 15:48:26 | 7e51672b | 031 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "031", "max_rounds": 2}} |
| 5455 | 2026-10-07 15:48:26 | 996de8af | 031 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "031", "status": "testing", "verified": "UNVERIFIED"}} |
| 5456 | 2026-10-07 15:48:32 | 7e51672b | 031 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5457 | 2026-10-07 15:54:19 | 989112db | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 35s [done] report expect='FACTORY' cmd=True \| T3 PASS 117s [ |
| 5458 | 2026-10-07 15:54:19 | 989112db | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 35s [done] report expect='FACTORY' cmd=True \| T3 PASS 117s [ |
| 5459 | 2026-10-07 15:54:19 | 4f69d4cc | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "00a4f8d453cd46b3af1d72958415e586", "after_quota": "989112dbeac04633bcff0118408a6 |
| 5460 | 2026-10-07 15:54:19 | 989112db | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5461 | 2026-10-07 15:54:24 | 8083faff | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5462 | 2026-10-08 10:27:18 | 7e51672b | 031 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 5463 | 2026-10-08 10:27:17 | 35b91d1a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5464 | 2026-10-08 10:27:17 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5465 | 2026-10-08 10:27:18 | 968f7eaa |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-08T11"}} |
| 5466 | 2026-10-08 10:27:18 | 35b91d1a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5467 | 2026-10-08 10:27:22 | 762a5e34 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5468 | 2026-10-08 10:27:22 | 4f8bd296 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-08T11"}} |
| 5469 | 2026-10-08 10:29:10 | 762a5e34 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 5470 | 2026-10-08 10:29:10 | 762a5e34 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash38", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "TimeoutError"} |
| 5471 | 2026-10-08 10:29:10 | 6ddd2e39 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-08", "trigger": "blocked:gemini-flash38"}} |
| 5472 | 2026-10-08 10:29:10 | 9bc6b6a7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-08", "trigger": "blocked:gemini-flash38"}} |
| 5473 | 2026-10-08 10:29:10 | a9c07bd0 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-08", "trigger": "blocked:gemini-flash38"}} |
| 5474 | 2026-10-08 10:29:10 | 126cc7a1 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-08", "trigger": "blocked:gemini-flash38"}} |
| 5475 | 2026-10-08 10:29:10 | 43f9ec82 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-08", "trigger": "blocked:gemini-flash38"}} |
| 5476 | 2026-10-08 10:29:10 | bdb9b692 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-08", "trigger": "blocked:gemini-flash38"}} |
| 5477 | 2026-10-08 10:29:10 | 762a5e34 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss1 |
| 5478 | 2026-10-08 10:29:14 | 7e51672b | 031 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 5479 | 2026-10-08 10:30:02 | 7e51672b | 031 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 5480 | 2026-10-08 10:30:02 | 7e51672b | 031 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 5481 | 2026-10-08 10:30:02 | 7e51672b | 031 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "031", "status": "active"}} |
| 5482 | 2026-10-08 10:30:08 | 6ddd2e39 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5483 | 2026-10-08 10:30:09 | 6ddd2e39 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5484 | 2026-10-08 10:30:13 | 9bc6b6a7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5485 | 2026-10-08 10:30:14 | 9bc6b6a7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5486 | 2026-10-08 10:30:19 | a9c07bd0 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5487 | 2026-10-08 10:30:21 | a9c07bd0 |  | lane.rejected | svc-LAPTOP-LRE6PSA8 | {"model": "thinkingmachines/inkling-small:free", "reason": "probe auth: {\"error\":{\"message\":\"thinkingmachines/inkling-small:free is onl |
| 5488 | 2026-10-08 10:30:21 | a9c07bd0 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5489 | 2026-10-08 10:30:25 | 126cc7a1 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5490 | 2026-10-08 10:30:25 | 126cc7a1 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5491 | 2026-10-08 10:30:29 | 43f9ec82 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5492 | 2026-10-08 10:30:29 | 43f9ec82 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5493 | 2026-10-08 10:30:34 | bdb9b692 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5494 | 2026-10-08 10:30:34 | bdb9b692 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5495 | 2026-10-08 10:30:38 | 704fa219 | 028 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5496 | 2026-10-08 10:31:43 | 8083faff | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 5497 | 2026-10-08 10:31:45 | 704fa219 | 028 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 PASS 13s [done] expect='3' last='RESULT: 3' \| T3 FAIL 31s [done] expect='5'  |
| 5498 | 2026-10-08 10:31:45 | 704fa219 | 028 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 PASS 13s [done] expect='3' last='RESULT: 3' \| T3 FAIL 31s [done] expect='5'  |
| 5499 | 2026-10-08 10:31:45 | 704fa219 | 028 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5500 | 2026-10-08 10:31:45 | b0d01597 | 028 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "028", "max_rounds": 2}} |
| 5501 | 2026-10-08 10:31:45 | 704fa219 | 028 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "028", "status": "testing", "verified": "UNVERIFIED"}} |
| 5502 | 2026-10-08 10:31:48 | 328c36fa | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5503 | 2026-10-08 10:31:53 | b0d01597 | 028 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5504 | 2026-10-08 10:33:51 | b0d01597 | 028 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-120b", "sandbox": "2/4", "rejected": null}, {"round" |
| 5505 | 2026-10-08 10:33:51 | b0d01597 | 028 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 5506 | 2026-10-08 10:33:56 | d49e60c4 | 033 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5507 | 2026-10-08 10:34:55 | d49e60c4 | 033 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 3s [done] expect='X_OK' last='' \| T2 PASS 12s [done] expect='2' last='RESULT: 2' \| T3 PASS 32s [done] expect='0' last= |
| 5508 | 2026-10-08 10:34:55 | d49e60c4 | 033 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 3s [done] expect='X_OK' last='' \| T2 PASS 12s [done] expect='2' last='RESULT: 2' \| T3 PASS 32s [done] expect='0' last= |
| 5509 | 2026-10-08 10:34:55 | d49e60c4 | 033 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5510 | 2026-10-08 10:34:55 | cfae58f1 | 033 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "033", "max_rounds": 2}} |
| 5511 | 2026-10-08 10:34:55 | d49e60c4 | 033 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "033", "status": "testing", "verified": "UNVERIFIED"}} |
| 5512 | 2026-10-08 10:35:00 | cfae58f1 | 033 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5513 | 2026-10-08 10:35:50 | cfae58f1 | 033 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 5514 | 2026-10-08 10:35:50 | cfae58f1 | 033 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 5515 | 2026-10-08 10:35:50 | cfae58f1 | 033 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "033", "status": "active"}} |
| 5516 | 2026-10-08 10:35:54 | 4bf074c7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5517 | 2026-10-08 10:37:37 | 328c36fa | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 17s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 5518 | 2026-10-08 10:37:37 | 328c36fa | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 17s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 5519 | 2026-10-08 10:37:37 | 328c36fa | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5520 | 2026-10-08 10:37:37 | 6de94a7d | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "328c36fa74be43a294a2a569f11df46 |
| 5521 | 2026-10-08 10:37:37 | 328c36fa | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5522 | 2026-10-08 10:37:42 | 8083faff | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 5523 | 2026-10-08 10:38:32 | 4bf074c7 |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "gemini-gemini-flash-lite-latest", "result": "1/4", "quota": 0, "secs": 46} |
| 5524 | 2026-10-08 10:38:32 | 4bf074c7 |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "gemini-lite", "result": "2/4", "quota": 0, "secs": 34} |
| 5525 | 2026-10-08 10:38:32 | 4bf074c7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["gemini-gemini-flash-lite-latest", "1/4"], ["gemini-lite", "2/4"]]}} |
| 5526 | 2026-10-08 10:38:39 | 06d62a7e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5527 | 2026-10-08 10:39:28 | 06d62a7e |  | factory.canary | svc-LAPTOP-LRE6PSA8 | {"verdict": "FAIL", "lane": "groq:openai/gpt-oss-120b", "chain": ["groq-gptoss120b", "or-apodex-11-mini", "gemini-lite31", "or-ling-30-flash |
| 5528 | 2026-10-08 10:39:28 | 06d62a7e |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"pass": 1, "total": 2}} |
| 5529 | 2026-10-08 10:51:37 | 8083faff | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 17s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 5530 | 2026-10-08 10:51:37 | 8083faff | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 17s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 5531 | 2026-10-08 10:51:37 | 9931daef | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "df24e745ca8143daad1c58a7c3f21ddd", "after_quota": "8083faff052344ee93a18b8c09a8a |
| 5532 | 2026-10-08 10:51:37 | 8083faff | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5533 | 2026-10-08 10:51:40 | 41a32998 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5534 | 2026-10-08 11:03:26 | 41a32998 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 95s [d |
| 5535 | 2026-10-08 11:03:27 | 41a32998 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 95s [d |
| 5536 | 2026-10-08 11:03:27 | ff352cca | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "41a329982cc543d6a54ed6a865be1 |
| 5537 | 2026-10-08 11:03:27 | 41a32998 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5538 | 2026-10-08 11:03:27 | e294457f | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5539 | 2026-10-08 11:08:33 | e294457f | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 14s [done] report expect='FACTORY' cmd=True \| T3 PASS 39s [d |
| 5540 | 2026-10-08 11:08:33 | e294457f | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 14s [done] report expect='FACTORY' cmd=True \| T3 PASS 39s [d |
| 5541 | 2026-10-08 11:08:33 | e294457f | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5542 | 2026-10-08 11:08:33 | a4a72581 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "e294457f11f24609a0c03b5d41c90a8 |
| 5543 | 2026-10-08 11:08:33 | e294457f | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5544 | 2026-10-08 11:08:33 | 6de94a7d | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5545 | 2026-10-08 11:16:19 | 6de94a7d | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 29s [done] report expect='FACTORY' cmd=True \| T3 PASS 21s [d |
| 5546 | 2026-10-08 11:16:19 | 6de94a7d | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 29s [done] report expect='FACTORY' cmd=True \| T3 PASS 21s [d |
| 5547 | 2026-10-08 11:16:19 | 689553c7 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "6de94a7d866b41ed9b15d56fda65f914", "after_quota": "6de94a7d866b41ed9b15d56fda65f |
| 5548 | 2026-10-08 11:16:19 | 6de94a7d | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5549 | 2026-10-08 11:16:22 | 1b5eae2b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5550 | 2026-10-08 11:25:30 | 1b5eae2b | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 42s [done] report expect='FACTORY' cmd=True \| T3 PASS 50s [d |
| 5551 | 2026-10-08 11:25:30 | 1b5eae2b | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 42s [done] report expect='FACTORY' cmd=True \| T3 PASS 50s [d |
| 5552 | 2026-10-08 11:25:30 | 14ae23f3 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "41923cc5baaa4b7ba7c14909b7abe137", "after_quota": "1b5eae2bafe744b6b12742aae1671 |
| 5553 | 2026-10-08 11:25:30 | 1b5eae2b | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5554 | 2026-10-08 11:25:34 | 3200a504 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5555 | 2026-10-08 11:27:19 | 968f7eaa |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5556 | 2026-10-08 11:27:19 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5557 | 2026-10-08 11:27:20 | 5e96235c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-08T12"}} |
| 5558 | 2026-10-08 11:27:20 | 968f7eaa |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5559 | 2026-10-08 11:27:24 | 4f8bd296 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5560 | 2026-10-08 11:27:24 | 824fed7b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-08T12"}} |
| 5561 | 2026-10-08 11:28:08 | 4f8bd296 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 5562 | 2026-10-08 11:28:08 | 4f8bd296 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash38", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 5563 | 2026-10-08 11:28:08 | 4f8bd296 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-l |
| 5564 | 2026-10-08 11:34:57 | 3200a504 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 64s [done] report expect='FACTORY' cmd=True \| T3 PASS 34s [d |
| 5565 | 2026-10-08 11:34:57 | 3200a504 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 64s [done] report expect='FACTORY' cmd=True \| T3 PASS 34s [d |
| 5566 | 2026-10-08 11:34:57 | 7b9fb063 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "3200a504f6604a6499bbb0e94ff5a |
| 5567 | 2026-10-08 11:34:57 | 3200a504 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5568 | 2026-10-08 11:34:57 | 4f69d4cc | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5569 | 2026-10-08 11:45:09 | 4f69d4cc | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 48s [d |
| 5570 | 2026-10-08 11:45:09 | 4f69d4cc | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 48s [d |
| 5571 | 2026-10-08 11:45:09 | 2cc11256 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "00a4f8d453cd46b3af1d72958415e586", "after_quota": "4f69d4ccb2934031884d0d3fb181a |
| 5572 | 2026-10-08 11:45:09 | 4f69d4cc | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5573 | 2026-10-08 11:45:12 | a4a72581 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5574 | 2026-10-08 11:54:21 | a4a72581 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 36s [done] report expect='FACTORY' cmd=True \| T3 PASS 37s [d |
| 5575 | 2026-10-08 11:54:21 | a4a72581 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 36s [done] report expect='FACTORY' cmd=True \| T3 PASS 37s [d |
| 5576 | 2026-10-08 11:54:21 | 3d2ef52e | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a4a72581e5ea46dbb084cdad721d4774", "after_quota": "a4a72581e5ea46dbb084cdad721d4 |
| 5577 | 2026-10-08 11:54:21 | a4a72581 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5578 | 2026-10-08 11:54:21 | dc90fd03 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5579 | 2026-10-08 12:05:03 | dc90fd03 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 43s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 5580 | 2026-10-08 12:05:03 | dc90fd03 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 43s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 5581 | 2026-10-08 12:05:03 | 7719fcdd | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "dc90fd03027d4e1a9270d756d6532ee9", "after_quota": "dc90fd03027d4e1a9270d756d6532 |
| 5582 | 2026-10-08 12:05:03 | dc90fd03 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5583 | 2026-10-08 13:14:33 | 5e96235c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5584 | 2026-10-08 13:14:34 | 824fed7b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5585 | 2026-10-08 13:14:37 | a87fa102 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-08T14"}} |
| 5586 | 2026-10-08 13:14:38 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5587 | 2026-10-08 13:14:53 | fb879817 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-08T14"}} |
| 5588 | 2026-10-08 13:14:53 | 5e96235c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5589 | 2026-10-08 13:15:00 | 9931daef | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5590 | 2026-10-08 13:15:46 | 824fed7b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-l |
| 5591 | 2026-10-08 13:24:02 | 9931daef | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 80s [done] report expect='FACTORY' cmd=True \| T3 PASS 37s [d |
| 5592 | 2026-10-08 13:24:02 | 9931daef | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 80s [done] report expect='FACTORY' cmd=True \| T3 PASS 37s [d |
| 5593 | 2026-10-08 13:24:02 | 52fb8506 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "df24e745ca8143daad1c58a7c3f21ddd", "after_quota": "9931daef7b4c47e9925a501f88751 |
| 5594 | 2026-10-08 13:24:02 | 9931daef | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5595 | 2026-10-08 13:24:05 | ff352cca | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5596 | 2026-10-08 13:32:26 | ff352cca | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 34s [done] report expect='FACTORY' cmd=True \| T3 PASS 30s [d |
| 5597 | 2026-10-08 13:32:26 | ff352cca | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 34s [done] report expect='FACTORY' cmd=True \| T3 PASS 30s [d |
| 5598 | 2026-10-08 13:32:26 | 41b0fd08 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "ff352ccadb42446faba8f97d04cf6 |
| 5599 | 2026-10-08 13:32:26 | ff352cca | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5600 | 2026-10-08 13:32:28 | 689553c7 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5601 | 2026-10-08 13:42:35 | 689553c7 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 31s [done] report expect='FACTORY' cmd=True \| T3 PASS 32s [d |
| 5602 | 2026-10-08 13:42:35 | 689553c7 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 31s [done] report expect='FACTORY' cmd=True \| T3 PASS 32s [d |
| 5603 | 2026-10-08 13:42:35 | 000c654f | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "6de94a7d866b41ed9b15d56fda65f914", "after_quota": "689553c779f9496f9bd69490247d3 |
| 5604 | 2026-10-08 13:42:35 | 689553c7 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5605 | 2026-10-08 13:42:36 | 14ae23f3 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5606 | 2026-10-08 13:52:12 | 14ae23f3 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 31s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [d |
| 5607 | 2026-10-08 13:52:12 | 14ae23f3 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 31s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [d |
| 5608 | 2026-10-08 13:52:12 | 7e3d1eac | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "41923cc5baaa4b7ba7c14909b7abe137", "after_quota": "14ae23f3cbd641de8b46703ec1ab0 |
| 5609 | 2026-10-08 13:52:12 | 14ae23f3 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5610 | 2026-10-08 13:52:15 | 7b9fb063 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5611 | 2026-10-08 14:02:16 | 7b9fb063 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 43s [d |
| 5612 | 2026-10-08 14:02:16 | 7b9fb063 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 43s [d |
| 5613 | 2026-10-08 14:02:16 | cbca7d55 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "7b9fb0633aef4087a611c9e56db12 |
| 5614 | 2026-10-08 14:02:16 | 7b9fb063 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5615 | 2026-10-08 14:02:17 | 2cc11256 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5616 | 2026-10-08 14:11:52 | 2cc11256 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 31s [done] report expect='FACTORY' cmd=True \| T3 PASS 43s [d |
| 5617 | 2026-10-08 14:11:52 | 2cc11256 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 31s [done] report expect='FACTORY' cmd=True \| T3 PASS 43s [d |
| 5618 | 2026-10-08 14:11:52 | 2cc11256 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5619 | 2026-10-08 14:11:52 | a8dfa785 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "2cc11256b2a64dc18f80c8589e8537d |
| 5620 | 2026-10-08 14:11:52 | 2cc11256 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5621 | 2026-10-08 14:11:56 | 3d2ef52e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5622 | 2026-10-08 14:14:42 | a87fa102 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5623 | 2026-10-08 14:14:42 | 26fa5dd7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-08T15"}} |
| 5624 | 2026-10-08 14:16:13 | a87fa102 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 5625 | 2026-10-08 14:16:13 | a87fa102 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gem |
| 5626 | 2026-10-08 14:16:18 | fb879817 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5627 | 2026-10-08 14:16:18 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5628 | 2026-10-08 14:16:18 | ccc89ce0 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-08T15"}} |
| 5629 | 2026-10-08 14:16:18 | fb879817 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5630 | 2026-10-08 14:21:46 | 3d2ef52e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 39s [done] report expect='FACTORY' cmd=True \| T3 PASS 43s [d |
| 5631 | 2026-10-08 14:21:46 | 3d2ef52e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 39s [done] report expect='FACTORY' cmd=True \| T3 PASS 43s [d |
| 5632 | 2026-10-08 14:21:46 | dcbd97eb | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a4a72581e5ea46dbb084cdad721d4774", "after_quota": "3d2ef52ee63b420589834b5b406fe |
| 5633 | 2026-10-08 14:21:46 | 3d2ef52e | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5634 | 2026-10-08 14:21:50 | 7719fcdd | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5635 | 2026-10-08 14:32:52 | 7719fcdd | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 87s [d |
| 5636 | 2026-10-08 14:32:52 | 7719fcdd | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 87s [d |
| 5637 | 2026-10-08 14:32:52 | 62d550ce | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "dc90fd03027d4e1a9270d756d6532ee9", "after_quota": "7719fcdd57764e9fb60a214c0d209 |
| 5638 | 2026-10-08 14:32:52 | 7719fcdd | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5639 | 2026-10-08 14:41:56 | a8dfa785 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5640 | 2026-10-08 14:52:22 | a8dfa785 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 44s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 40s [d |
| 5641 | 2026-10-08 14:52:22 | a8dfa785 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 44s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 40s [d |
| 5642 | 2026-10-08 14:52:22 | fae47e4f | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a8dfa7853d6241f1ab5469b02c857c1b", "after_quota": "a8dfa7853d6241f1ab5469b02c857 |
| 5643 | 2026-10-08 14:52:22 | a8dfa785 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5644 | 2026-10-08 15:14:43 | 26fa5dd7 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5645 | 2026-10-08 15:14:43 | cd0d50e3 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-08T16"}} |
| 5646 | 2026-10-08 15:15:51 | 26fa5dd7 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss1 |
| 5647 | 2026-10-08 15:16:19 | ccc89ce0 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5648 | 2026-10-08 15:16:19 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5649 | 2026-10-08 15:16:19 | 98c3fb4d |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-08T16"}} |
| 5650 | 2026-10-08 15:16:19 | ccc89ce0 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5651 | 2026-10-08 15:24:03 | 52fb8506 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5652 | 2026-10-08 15:36:01 | 0490db0c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5653 | 2026-10-08 15:36:01 | 0490db0c |  | audit.verified | fast-LAPTOP-LRE6PSA8 | {"rows": 5650, "hashed": 4898, "first_bad": null} |
| 5654 | 2026-10-08 15:36:01 | d8bda1e9 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-10-09"}} |
| 5655 | 2026-10-08 15:36:01 | 6e4e327a |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-10-08"}} |
| 5656 | 2026-10-08 15:36:01 | 0d3cdbe7 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-10-08"}} |
| 5657 | 2026-10-08 15:36:01 | 76b09e82 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-10-08"}} |
| 5658 | 2026-10-08 15:36:01 | 0490db0c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5659 | 2026-10-08 15:36:20 | 52fb8506 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 34s [done] report expect='FACTORY' cmd=True \| T3 PASS 36s [d |
| 5660 | 2026-10-08 15:36:20 | 52fb8506 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 34s [done] report expect='FACTORY' cmd=True \| T3 PASS 36s [d |
| 5661 | 2026-10-08 15:36:20 | ab79dd5a | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "df24e745ca8143daad1c58a7c3f21ddd", "after_quota": "52fb85060a9a4515ace70d6a081a2 |
| 5662 | 2026-10-08 15:36:20 | 52fb8506 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5663 | 2026-10-08 15:36:21 | 41b0fd08 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5664 | 2026-10-08 15:36:24 | 76b09e82 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5665 | 2026-10-08 15:36:24 | b55e8b34 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "76b09e8217e8440b9a0f1bc14f76a1be", "day": "2026-10-08"}} |
| 5666 | 2026-10-08 15:36:24 | 1985bef5 | 031 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "031", "monitor_of": "76b09e8217e8440b9a0f1bc14f76a1be", "day": "2026-10-08"}} |
| 5667 | 2026-10-08 15:36:24 | 76b09e82 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "031"], "jobs": ["b55e8b34", "1985bef5"]} |
| 5668 | 2026-10-08 15:36:24 | 76b09e82 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5669 | 2026-10-08 15:36:33 | 1985bef5 | 031 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5670 | 2026-10-08 15:37:45 | 1985bef5 | 031 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 FAIL 26s [done] expect='3' last='\u00e2\u2020\u00b3 write bots.log' \| T3 PASS |
| 5671 | 2026-10-08 15:37:45 | 1985bef5 | 031 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 FAIL 26s [done] expect='3' last='\u00e2\u2020\u00b3 write bots.log' \| T3 PASS |
| 5672 | 2026-10-08 15:37:45 | 1985bef5 | 031 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5673 | 2026-10-08 15:37:45 | bb74df66 | 031 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "031", "max_rounds": 2}} |
| 5674 | 2026-10-08 15:37:45 | 1985bef5 | 031 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "031", "status": "testing", "verified": "UNVERIFIED"}} |
| 5675 | 2026-10-08 15:37:49 | bb74df66 | 031 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5676 | 2026-10-08 15:40:34 | bb74df66 | 031 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": "3/4", "rejected": null}, {"round": 2 |
| 5677 | 2026-10-08 15:40:34 | bb74df66 | 031 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 5678 | 2026-10-08 15:40:34 | bb74df66 | 031 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "031", "name": "weekly-self-review", "status": "active", "verified": "VERIFIED"}} |
| 5679 | 2026-10-08 15:40:38 | 6e4e327a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5680 | 2026-10-08 15:43:02 | 6e4e327a |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "gemini-lite31", "result": "0/4", "quota": 0, "secs": 33} |
| 5681 | 2026-10-08 15:43:02 | 6e4e327a |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "groq-gptoss120b", "result": "1/4", "quota": 3, "secs": 34} |
| 5682 | 2026-10-08 15:43:02 | 6e4e327a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["gemini-lite31", "0/4"], ["groq-gptoss120b", "1/4 q3"]]}} |
| 5683 | 2026-10-08 15:43:07 | 0d3cdbe7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5684 | 2026-10-08 15:44:01 | 0d3cdbe7 |  | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "security", "next_state": "paused", "attempt": 1, "error": "FactoryError: could not produce a valid spec after 3 attempts: |
| 5685 | 2026-10-08 15:52:09 | 41b0fd08 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 89s [done] report expect='FACTORY' cmd=True \| T3 PASS 179s [ |
| 5686 | 2026-10-08 15:52:09 | 41b0fd08 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 89s [done] report expect='FACTORY' cmd=True \| T3 PASS 179s [ |
| 5687 | 2026-10-08 15:52:09 | c13e8ff5 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "41b0fd08859b482886671eb3a1e81 |
| 5688 | 2026-10-08 15:52:09 | 41b0fd08 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5689 | 2026-10-08 15:52:11 | 000c654f | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5690 | 2026-10-08 16:04:17 | 000c654f | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 48s [d |
| 5691 | 2026-10-08 16:04:17 | 000c654f | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 48s [d |
| 5692 | 2026-10-08 16:04:17 | 000c654f | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5693 | 2026-10-08 16:04:17 | 1eb9c40f | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "000c654ff30841e6a401d6371369e7c |
| 5694 | 2026-10-08 16:04:17 | 000c654f | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5695 | 2026-10-08 16:04:19 | 7e3d1eac | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5696 | 2026-10-08 16:14:47 | cd0d50e3 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5697 | 2026-10-08 16:14:48 | 0e8ffbf4 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-08T17"}} |
| 5698 | 2026-10-08 16:16:30 | cd0d50e3 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "TimeoutError"} |
| 5699 | 2026-10-08 16:16:30 | 52015306 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-08", "trigger": "blocked:gemini-flash36"}} |
| 5700 | 2026-10-08 16:16:30 | a1646b1c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-08", "trigger": "blocked:gemini-flash36"}} |
| 5701 | 2026-10-08 16:16:30 | ef1a4cae |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-08", "trigger": "blocked:gemini-flash36"}} |
| 5702 | 2026-10-08 16:16:30 | 1f20f793 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-08", "trigger": "blocked:gemini-flash36"}} |
| 5703 | 2026-10-08 16:16:30 | f41ed0ee |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-08", "trigger": "blocked:gemini-flash36"}} |
| 5704 | 2026-10-08 16:16:30 | b871be57 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-08", "trigger": "blocked:gemini-flash36"}} |
| 5705 | 2026-10-08 16:16:30 | cd0d50e3 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "groq-gptoss |
| 5706 | 2026-10-08 16:16:35 | 98c3fb4d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5707 | 2026-10-08 16:16:35 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5708 | 2026-10-08 16:16:35 | 844700b5 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-08T17"}} |
| 5709 | 2026-10-08 16:16:35 | 98c3fb4d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5710 | 2026-10-08 16:16:39 | 52015306 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5711 | 2026-10-08 16:16:40 | 52015306 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5712 | 2026-10-08 16:16:44 | a1646b1c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5713 | 2026-10-08 16:16:44 | a1646b1c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5714 | 2026-10-08 16:16:48 | ef1a4cae |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5715 | 2026-10-08 16:16:48 | ef1a4cae |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5716 | 2026-10-08 16:16:54 | 1f20f793 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5717 | 2026-10-08 16:16:54 | 1f20f793 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5718 | 2026-10-08 16:16:59 | f41ed0ee |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5719 | 2026-10-08 16:16:59 | f41ed0ee |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5720 | 2026-10-08 16:17:04 | b871be57 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5721 | 2026-10-08 16:17:04 | b871be57 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5722 | 2026-10-08 16:21:49 | 7e3d1eac | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 96s [done] report expect='FACTORY' cmd=True \| T3 PASS 95s [d |
| 5723 | 2026-10-08 16:21:49 | 7e3d1eac | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 96s [done] report expect='FACTORY' cmd=True \| T3 PASS 95s [d |
| 5724 | 2026-10-08 16:21:49 | 24b6cef5 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "41923cc5baaa4b7ba7c14909b7abe137", "after_quota": "7e3d1eac911d467480f7762fa0f10 |
| 5725 | 2026-10-08 16:21:49 | 7e3d1eac | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5726 | 2026-10-08 16:21:53 | cbca7d55 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5727 | 2026-10-08 16:42:53 | cbca7d55 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 55s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 122s [done] report expect='FACTORY' cmd=True \| T3 PASS 118s  |
| 5728 | 2026-10-08 16:42:53 | cbca7d55 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 55s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 122s [done] report expect='FACTORY' cmd=True \| T3 PASS 118s  |
| 5729 | 2026-10-08 16:42:53 | 9e61efc1 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "cbca7d55439b4199ac30acf800de6 |
| 5730 | 2026-10-08 16:42:53 | cbca7d55 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5731 | 2026-10-08 16:42:55 | 1eb9c40f | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5732 | 2026-10-08 17:48:20 | 1eb9c40f |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 5733 | 2026-10-08 17:48:20 | 0e8ffbf4 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5734 | 2026-10-09 04:30:18 | 5a5b85cd |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-08T18"}} |
| 5735 | 2026-10-09 04:30:27 | 0e8ffbf4 |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 5736 | 2026-10-09 04:30:28 | 22c977d6 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-08T17-retry", "retry_of": "0e8ffbf464ca4f10aab3cc730963f4e9"}} |
| 5737 | 2026-10-09 04:30:28 | 0e8ffbf4 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5738 | 2026-10-09 04:30:41 | 1eb9c40f |  | job.readopted | fast-LAPTOP-LRE6PSA8 | {} |
| 5739 | 2026-10-09 04:30:46 | 844700b5 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5740 | 2026-10-09 04:30:46 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5741 | 2026-10-09 04:30:49 | df9532da |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-09T05"}} |
| 5742 | 2026-10-09 04:30:49 | 844700b5 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5743 | 2026-10-09 04:30:52 | 5a5b85cd |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5744 | 2026-10-09 04:30:52 | cb68d6f7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T05"}} |
| 5745 | 2026-10-09 04:31:11 | c440dca6 |  | job.enqueued | nightly-task | {"kind": "monitor", "payload": {"only": null, "day": "2026-10-09"}} |
| 5746 | 2026-10-09 04:31:27 | 5a5b85cd |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 5747 | 2026-10-09 04:31:27 | 5a5b85cd |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "or-ling-30-flash-sante", "outcome": "gone", "before": "VERIFIED", "after": "BLOCKED", "detail": "{\"error\":{\"message\":\"this m |
| 5748 | 2026-10-09 04:31:27 | 1e285eb7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-09", "trigger": "blocked:or-ling-30-flash-sante"}} |
| 5749 | 2026-10-09 04:31:27 | 6a778c96 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-09", "trigger": "blocked:or-ling-30-flash-sante"}} |
| 5750 | 2026-10-09 04:31:27 | 7003d4dd |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-09", "trigger": "blocked:or-ling-30-flash-sante"}} |
| 5751 | 2026-10-09 04:31:27 | c742c756 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-09", "trigger": "blocked:or-ling-30-flash-sante"}} |
| 5752 | 2026-10-09 04:31:27 | 7259ef61 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-09", "trigger": "blocked:or-ling-30-flash-sante"}} |
| 5753 | 2026-10-09 04:31:27 | 6a251af6 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-09", "trigger": "blocked:or-ling-30-flash-sante"}} |
| 5754 | 2026-10-09 04:31:27 | 5a5b85cd |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemi |
| 5755 | 2026-10-09 04:31:33 | 1e285eb7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5756 | 2026-10-09 04:31:34 | 1e285eb7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5757 | 2026-10-09 04:31:39 | 6a778c96 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5758 | 2026-10-09 04:31:40 | 6a778c96 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5759 | 2026-10-09 04:31:52 | 7003d4dd |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5760 | 2026-10-09 04:31:57 | 7003d4dd |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5761 | 2026-10-09 04:32:00 | c742c756 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5762 | 2026-10-09 04:32:00 | c742c756 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5763 | 2026-10-09 04:32:04 | 7259ef61 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5764 | 2026-10-09 04:32:04 | 7259ef61 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5765 | 2026-10-09 04:32:07 | 6a251af6 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5766 | 2026-10-09 04:32:07 | 6a251af6 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5767 | 2026-10-09 04:32:10 | c440dca6 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5768 | 2026-10-09 04:32:10 | be435166 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "c440dca6e7ce4de1bbf56dcbf0b9a042", "day": "2026-10-09"}} |
| 5769 | 2026-10-09 04:32:10 | 43e06b9c | 031 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "031", "monitor_of": "c440dca6e7ce4de1bbf56dcbf0b9a042", "day": "2026-10-09"}} |
| 5770 | 2026-10-09 04:32:10 | c440dca6 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "031"], "jobs": ["be435166", "43e06b9c"]} |
| 5771 | 2026-10-09 04:32:10 | c440dca6 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5772 | 2026-10-09 04:32:13 | 43e06b9c | 031 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5773 | 2026-10-09 04:33:02 | 43e06b9c | 031 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 12s [done] expect='3' last='RESULT: 3' \| T3 PASS 12s [done] expect='2'  |
| 5774 | 2026-10-09 04:33:02 | 43e06b9c | 031 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 12s [done] expect='3' last='RESULT: 3' \| T3 PASS 12s [done] expect='2'  |
| 5775 | 2026-10-09 04:33:02 | 43e06b9c | 031 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "031", "status": "active", "verified": "VERIFIED"}} |
| 5776 | 2026-10-09 04:37:39 | 1eb9c40f | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 5777 | 2026-10-09 04:37:41 | dcbd97eb | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5778 | 2026-10-09 04:40:30 | 22c977d6 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5779 | 2026-10-09 04:40:30 | cb68d6f7 |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 5780 | 2026-10-09 04:40:57 | 22c977d6 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemi |
| 5781 | 2026-10-09 04:46:54 | dcbd97eb | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 121s [done] report expect='FACTORY' cmd=True \| T3 PASS 136s  |
| 5782 | 2026-10-09 04:46:54 | dcbd97eb | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 121s [done] report expect='FACTORY' cmd=True \| T3 PASS 136s  |
| 5783 | 2026-10-09 04:46:54 | dcbd97eb | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5784 | 2026-10-09 04:46:54 | ab5d1062 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "dcbd97eb1e13412eb16f2424a4f8e82 |
| 5785 | 2026-10-09 04:46:54 | dcbd97eb | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5786 | 2026-10-09 04:46:56 | 1eb9c40f | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 5787 | 2026-10-09 04:54:17 | 1eb9c40f | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 5788 | 2026-10-09 04:54:17 | 1eb9c40f | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 5789 | 2026-10-09 04:54:17 | 1eb9c40f | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5790 | 2026-10-09 04:54:17 | 9aa0054e | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "1eb9c40fc55d43179097e11b9d1648d |
| 5791 | 2026-10-09 04:54:17 | 1eb9c40f | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 7, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5792 | 2026-10-09 04:54:19 | 62d550ce | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5793 | 2026-10-09 05:07:57 | 62d550ce | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 82s [done] report expect='FACTORY' cmd=True \| T3 PASS 132s [ |
| 5794 | 2026-10-09 05:07:57 | 62d550ce | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 82s [done] report expect='FACTORY' cmd=True \| T3 PASS 132s [ |
| 5795 | 2026-10-09 05:07:57 | 32fc3cea | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "dc90fd03027d4e1a9270d756d6532ee9", "after_quota": "62d550ce8d714f16969e84e295213 |
| 5796 | 2026-10-09 05:07:57 | 62d550ce | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5797 | 2026-10-09 05:08:02 | fae47e4f | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5798 | 2026-10-09 05:20:32 | fae47e4f | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 64s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [d |
| 5799 | 2026-10-09 05:20:32 | fae47e4f | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 64s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [d |
| 5800 | 2026-10-09 05:20:32 | a3c0bdb6 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a8dfa7853d6241f1ab5469b02c857c1b", "after_quota": "fae47e4f98064fd1a8eef45bffd62 |
| 5801 | 2026-10-09 05:20:32 | fae47e4f | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5802 | 2026-10-09 05:20:35 | ab5d1062 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5803 | 2026-10-09 05:30:52 | df9532da |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5804 | 2026-10-09 05:30:52 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5805 | 2026-10-09 05:30:52 | 7a5370a7 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-09T06"}} |
| 5806 | 2026-10-09 05:30:52 | df9532da |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5807 | 2026-10-09 05:31:00 | cb68d6f7 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5808 | 2026-10-09 05:31:00 | 2bf3f44f |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T06"}} |
| 5809 | 2026-10-09 05:31:50 | ab5d1062 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 5810 | 2026-10-09 05:31:50 | ab5d1062 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 5811 | 2026-10-09 05:31:50 | 88ac2dd8 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ab5d10624c564c16b855f074ef29fa09", "after_quota": "ab5d10624c564c16b855f074ef29f |
| 5812 | 2026-10-09 05:31:50 | ab5d1062 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5813 | 2026-10-09 05:31:54 | 9aa0054e | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5814 | 2026-10-09 05:32:18 | cb68d6f7 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gem |
