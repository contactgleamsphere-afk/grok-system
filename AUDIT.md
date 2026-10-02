# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 3480 | 2026-09-30 18:24:05 | 0f1be090 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 15s [done] report expect='FACTORY' cmd=True \| T3 FAIL 11s [d |
| 3481 | 2026-09-30 18:24:05 | 0f1be090 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3482 | 2026-09-30 18:24:05 | 791d6548 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "0f1be09004b2406f89151eab5a6c7b7 |
| 3483 | 2026-09-30 18:24:05 | 0f1be090 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3484 | 2026-09-30 18:24:10 | 2341d262 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3485 | 2026-09-30 18:24:30 | 01c504a5 | 007 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 66s [done] expect='X_OK' last='\u00e2\u2020\u00b3 read notes.txt' \| T2 FAIL 14s [done] expect='2' last='Using config: C |
| 3486 | 2026-09-30 18:24:30 | 01c504a5 | 007 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 66s [done] expect='X_OK' last='\u00e2\u2020\u00b3 read notes.txt' \| T2 FAIL 14s [done] expect='2' last='Using config: C |
| 3487 | 2026-09-30 18:24:30 | 01c504a5 | 007 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3488 | 2026-09-30 18:24:30 | b98297bb | 007 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "007", "max_rounds": 2}} |
| 3489 | 2026-09-30 18:24:30 | 01c504a5 | 007 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "status": "testing", "verified": "UNVERIFIED"}} |
| 3490 | 2026-09-30 18:24:33 | b98297bb | 007 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3491 | 2026-09-30 18:25:16 | b98297bb | 007 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-de |
| 3492 | 2026-09-30 18:25:16 | b98297bb | 007 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3493 | 2026-09-30 18:25:20 | 19621fe3 | 008 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3494 | 2026-09-30 18:26:58 | 19621fe3 | 008 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 FAIL 11s [done] expect='apple' last='\u00e2\u2020\u00b3 write input.txt' \| T3 |
| 3495 | 2026-09-30 18:26:58 | 19621fe3 | 008 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 FAIL 11s [done] expect='apple' last='\u00e2\u2020\u00b3 write input.txt' \| T3 |
| 3496 | 2026-09-30 18:26:58 | 19621fe3 | 008 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3497 | 2026-09-30 18:26:58 | 5d2af791 | 008 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "008", "max_rounds": 2}} |
| 3498 | 2026-09-30 18:26:58 | 19621fe3 | 008 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "008", "status": "testing", "verified": "UNVERIFIED"}} |
| 3499 | 2026-09-30 18:27:02 | 5d2af791 | 008 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3500 | 2026-09-30 18:27:08 | 2341d262 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [do |
| 3501 | 2026-09-30 18:27:08 | 2341d262 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [do |
| 3502 | 2026-09-30 18:27:08 | 2341d262 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3503 | 2026-09-30 18:27:08 | 421d8d74 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "2341d262ef534057819d9ed9ab77ecf |
| 3504 | 2026-09-30 18:27:08 | 2341d262 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3505 | 2026-09-30 18:27:11 | fefc49ba | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3506 | 2026-09-30 18:27:47 | 5d2af791 | 008 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-de |
| 3507 | 2026-09-30 18:27:47 | 5d2af791 | 008 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3508 | 2026-09-30 18:27:52 | 1fc8cc29 | 009 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3509 | 2026-09-30 18:28:27 | 1fc8cc29 | 009 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 5s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\009.json' \| T2 FAIL 10s [done] expect='3' las |
| 3510 | 2026-09-30 18:28:27 | 1fc8cc29 | 009 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 5s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\009.json' \| T2 FAIL 10s [done] expect='3' las |
| 3511 | 2026-09-30 18:28:27 | 1fc8cc29 | 009 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3512 | 2026-09-30 18:28:27 | a119d185 | 009 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "009", "max_rounds": 2}} |
| 3513 | 2026-09-30 18:28:27 | 1fc8cc29 | 009 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "009", "status": "testing", "verified": "UNVERIFIED"}} |
| 3514 | 2026-09-30 18:28:31 | a119d185 | 009 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3515 | 2026-09-30 18:30:07 | fefc49ba | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [do |
| 3516 | 2026-09-30 18:30:07 | fefc49ba | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [do |
| 3517 | 2026-09-30 18:30:07 | fefc49ba | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3518 | 2026-09-30 18:30:07 | ca6d528e | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "496e3afd58764673a6b80d4e1d7f4792", "retry_of": "fefc49ba6a66418c9b4227593fb6ac4 |
| 3519 | 2026-09-30 18:30:07 | fefc49ba | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3520 | 2026-09-30 18:30:11 | 7633df72 | 011 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3521 | 2026-09-30 18:33:31 | 7633df72 | 011 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='RESULT: X_OK' \| T2 PASS 71s [done] expect='2' last='2' \| T3 PASS 104s [done] expect='3' |
| 3522 | 2026-09-30 18:33:31 | 7633df72 | 011 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='RESULT: X_OK' \| T2 PASS 71s [done] expect='2' last='2' \| T3 PASS 104s [done] expect='3' |
| 3523 | 2026-09-30 18:33:31 | 7633df72 | 011 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "011", "status": "active", "verified": "VERIFIED"}} |
| 3524 | 2026-09-30 18:33:35 | 8bb02e28 | 012 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3525 | 2026-09-30 18:35:37 | a119d185 | 009 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": "2/4", "rejected": null}, {"round": 2 |
| 3526 | 2026-09-30 18:35:37 | a119d185 | 009 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 3527 | 2026-09-30 18:35:37 | a119d185 | 009 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "009", "name": "line-dedupe-bot", "status": "active", "verified": "VERIFIED"}} |
| 3528 | 2026-09-30 18:35:41 | aa9194b1 | 013 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3529 | 2026-09-30 18:37:12 | 8bb02e28 | 012 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='RESULT: X_OK' \| T2 PASS 46s [done] expect='60' last='60' \| T3 PASS 123s [done] expect=' |
| 3530 | 2026-09-30 18:37:12 | 8bb02e28 | 012 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='RESULT: X_OK' \| T2 PASS 46s [done] expect='60' last='60' \| T3 PASS 123s [done] expect=' |
| 3531 | 2026-09-30 18:37:12 | 8bb02e28 | 012 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "012", "status": "active", "verified": "VERIFIED"}} |
| 3532 | 2026-09-30 18:37:17 | 22a15f2a | 014 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3533 | 2026-09-30 18:42:30 | aa9194b1 | 013 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 107s [done] expect='1' last='RESULT: 1' \| T3 PASS 106s [done] expect='0 |
| 3534 | 2026-09-30 18:42:30 | aa9194b1 | 013 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 107s [done] expect='1' last='RESULT: 1' \| T3 PASS 106s [done] expect='0 |
| 3535 | 2026-09-30 18:42:30 | aa9194b1 | 013 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "013", "status": "active", "verified": "VERIFIED"}} |
| 3536 | 2026-09-30 18:42:35 | a3da1a8d | 016 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3537 | 2026-09-30 18:43:16 | a3da1a8d | 016 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 10s [done] expect='2' last='RESULT: 2' \| T3 PASS 12s [done] expect='3' l |
| 3538 | 2026-09-30 18:43:16 | a3da1a8d | 016 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 10s [done] expect='2' last='RESULT: 2' \| T3 PASS 12s [done] expect='3' l |
| 3539 | 2026-09-30 18:43:16 | a3da1a8d | 016 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "016", "status": "active", "verified": "VERIFIED"}} |
| 3540 | 2026-09-30 18:43:22 | 715b8f1a | 017 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3541 | 2026-09-30 18:49:23 | 715b8f1a | 017 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 FAIL 4s [done] expect='3' last='Using config: C:\\AI\\Factory\\run\\botcfg\\01 |
| 3542 | 2026-09-30 18:49:23 | 715b8f1a | 017 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 FAIL 4s [done] expect='3' last='Using config: C:\\AI\\Factory\\run\\botcfg\\01 |
| 3543 | 2026-09-30 18:49:23 | 5734063d | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "017", "retest_of": "715b8f1aea8d487eaf9f98f6f0792c1c", "after_quota": "715b8f1aea8d487eaf9f98f6f0792 |
| 3544 | 2026-09-30 18:49:23 | 715b8f1a | 017 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "017", "status": "active", "verified": "VERIFIED"}} |
| 3545 | 2026-09-30 18:49:28 | afaa17a7 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3546 | 2026-09-30 18:49:29 | 22a15f2a | 014 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 71s [done] expect='X_OK' last='X_OK' \| T2 FAIL 305s [TIMEOUT] expect='5' last='' \| T3 PASS 231s [done] expect='Timeout |
| 3547 | 2026-09-30 18:49:29 | 22a15f2a | 014 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 71s [done] expect='X_OK' last='X_OK' \| T2 FAIL 305s [TIMEOUT] expect='5' last='' \| T3 PASS 231s [done] expect='Timeout |
| 3548 | 2026-09-30 18:49:29 | 22a15f2a | 014 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3549 | 2026-09-30 18:49:29 | 409eb9fc | 014 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "014", "max_rounds": 2}} |
| 3550 | 2026-09-30 18:49:29 | 22a15f2a | 014 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "014", "status": "testing", "verified": "UNVERIFIED"}} |
| 3551 | 2026-09-30 18:49:33 | b51dcb92 | 018 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3552 | 2026-09-30 18:50:11 | b51dcb92 | 018 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 3s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\018.json' \| T2 FAIL 11s [done] expect='30' la |
| 3553 | 2026-09-30 18:50:11 | b51dcb92 | 018 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 3s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\018.json' \| T2 FAIL 11s [done] expect='30' la |
| 3554 | 2026-09-30 18:50:11 | 934721ee | 018 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "018", "retest_of": "b51dcb92fc6649559bb29d9d4fee3af3", "after_quota": "b51dcb92fc6649559bb29d9d4fee3 |
| 3555 | 2026-09-30 18:50:11 | b51dcb92 | 018 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "status": "active", "verified": "VERIFIED"}} |
| 3556 | 2026-09-30 18:50:15 | 6813ec37 | 024 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3557 | 2026-09-30 18:50:40 | 6813ec37 | 024 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 3s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\024.json' \| T2 FAIL 11s [done] expect='2' las |
| 3558 | 2026-09-30 18:50:40 | 6813ec37 | 024 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 3s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\024.json' \| T2 FAIL 11s [done] expect='2' las |
| 3559 | 2026-09-30 18:50:40 | 6813ec37 | 024 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3560 | 2026-09-30 18:50:40 | f5648160 | 024 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "024", "max_rounds": 2}} |
| 3561 | 2026-09-30 18:50:40 | 6813ec37 | 024 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "024", "status": "testing", "verified": "UNVERIFIED"}} |
| 3562 | 2026-09-30 18:50:45 | 914578dc | 025 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3563 | 2026-09-30 18:51:56 | afaa17a7 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [do |
| 3564 | 2026-09-30 18:51:56 | afaa17a7 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [do |
| 3565 | 2026-09-30 18:51:56 | afaa17a7 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3566 | 2026-09-30 18:51:56 | c4afa11d | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "afaa17a7882f4b1aa6f46a0cfa8acb7 |
| 3567 | 2026-09-30 18:51:56 | afaa17a7 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3568 | 2026-09-30 18:52:00 | cafa3a07 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3569 | 2026-09-30 18:52:00 | 914578dc | 025 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 7s [done] expect='LIVENESS_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\025.json' \| T2 FAIL 55s [done] expect= |
| 3570 | 2026-09-30 18:52:00 | 914578dc | 025 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 7s [done] expect='LIVENESS_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\025.json' \| T2 FAIL 55s [done] expect= |
| 3571 | 2026-09-30 18:52:00 | 914578dc | 025 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3572 | 2026-09-30 18:52:00 | 42a8ce46 | 025 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "025", "max_rounds": 2}} |
| 3573 | 2026-09-30 18:52:00 | 914578dc | 025 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "025", "status": "testing", "verified": "UNVERIFIED"}} |
| 3574 | 2026-09-30 18:55:23 | cafa3a07 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [do |
| 3575 | 2026-09-30 18:55:23 | cafa3a07 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [do |
| 3576 | 2026-09-30 18:55:23 | cafa3a07 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3577 | 2026-09-30 18:55:23 | 9a330171 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "retry_of": "cafa3a07ae52474485cee614ae5cdd2 |
| 3578 | 2026-09-30 18:55:23 | cafa3a07 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3579 | 2026-09-30 18:55:26 | 791d6548 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3580 | 2026-09-30 18:55:29 | 409eb9fc | 014 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3581 | 2026-09-30 18:56:21 | 409eb9fc | 014 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-li |
| 3582 | 2026-09-30 18:56:21 | 409eb9fc | 014 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3583 | 2026-09-30 18:56:27 | f5648160 | 024 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3584 | 2026-09-30 18:57:07 | f5648160 | 024 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-li |
| 3585 | 2026-09-30 18:57:07 | f5648160 | 024 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3586 | 2026-09-30 18:57:12 | 42a8ce46 | 025 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3587 | 2026-09-30 18:58:05 | 42a8ce46 | 025 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": "instructions har |
| 3588 | 2026-09-30 18:58:05 | ab1e0d92 | 025 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "rearchitect", "payload": {"bot_id": "025", "feedback": "logic: spec/tests inconsistent, tests expect a literal the instructions mu |
| 3589 | 2026-09-30 18:58:05 | 42a8ce46 | 025 | bot.rearchitect_queued | svc-LAPTOP-LRE6PSA8 | {"reason": "logic: spec/tests inconsistent, tests expect a literal the instructions must mention (no passing candidate in 2 rounds)"} |
| 3590 | 2026-09-30 18:58:05 | 42a8ce46 | 025 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: logic: spec/tests inconsistent, tests expect a lite |
| 3591 | 2026-09-30 18:58:09 | 791d6548 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [d |
| 3592 | 2026-09-30 18:58:09 | 791d6548 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [d |
| 3593 | 2026-09-30 18:58:09 | 791d6548 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3594 | 2026-09-30 18:58:09 | a0a1b9ab | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "791d6548c0c649d7bf7112aa42b5dbd |
| 3595 | 2026-09-30 18:58:09 | 791d6548 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3596 | 2026-09-30 18:58:10 | 421d8d74 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3597 | 2026-09-30 19:01:12 | 421d8d74 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [d |
| 3598 | 2026-09-30 19:01:12 | 421d8d74 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [d |
| 3599 | 2026-09-30 19:01:12 | 421d8d74 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3600 | 2026-09-30 19:01:12 | 502b64ce | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "421d8d746b734b578e9c9f9e7b84c52 |
| 3601 | 2026-09-30 19:01:12 | 421d8d74 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3602 | 2026-09-30 19:01:15 | ca6d528e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3603 | 2026-09-30 19:01:17 | ab1e0d92 | 025 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3604 | 2026-09-30 19:02:17 | ab1e0d92 | 025 | bot.rearchitected | svc-LAPTOP-LRE6PSA8 | {"lane": "groq:openai/gpt-oss-20b", "tools": ["read_file", "write_file"], "permissions": ["fs:read", "fs:write"], "boundary_diff": {"model_p |
| 3605 | 2026-09-30 19:02:17 | 2fef54b7 | 025 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "025", "retest_of": "ab1e0d9250fc4e02a44da9a933afd1a6", "rearchitected": true}} |
| 3606 | 2026-09-30 19:02:17 | ab1e0d92 | 025 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "025", "pass": 1, "total": 4, "status": "testing"}} |
| 3607 | 2026-09-30 19:02:25 | 2fef54b7 | 025 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3608 | 2026-09-30 19:03:11 | 2fef54b7 | 025 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] expect='X_OK' last='X_OK' \| T2 FAIL 3s [done] expect='OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\ |
| 3609 | 2026-09-30 19:03:11 | 7e73f8b8 | 025 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "025", "max_rounds": 2, "rearchitected": true}} |
| 3610 | 2026-09-30 19:03:11 | 2fef54b7 | 025 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "025", "status": "testing", "verified": "UNVERIFIED"}} |
| 3611 | 2026-09-30 19:03:16 | 7e73f8b8 | 025 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3612 | 2026-09-30 19:04:24 | 7e73f8b8 | 025 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": "instructions har |
| 3613 | 2026-09-30 19:04:24 | 7e73f8b8 | 025 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: logic: spec/tests inconsistent, tests expect a lite |
| 3614 | 2026-09-30 19:04:31 | a3db23b5 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3615 | 2026-09-30 19:04:31 | a3db23b5 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": []}} |
| 3616 | 2026-09-30 19:04:36 | 5d740c8e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3617 | 2026-09-30 19:04:41 | 5d740c8e |  | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "security", "next_state": "paused", "attempt": 1, "error": "FactoryError: could not produce a valid spec after 3 attempts: |
| 3618 | 2026-09-30 19:07:31 | 1d45fe25 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3619 | 2026-09-30 19:07:31 | c19a33bc |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-30T20"}} |
| 3620 | 2026-09-30 19:07:52 | ca6d528e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 23s [d |
| 3621 | 2026-09-30 19:07:52 | ca6d528e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 23s [d |
| 3622 | 2026-09-30 19:07:52 | ca6d528e | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3623 | 2026-09-30 19:07:52 | f2538a50 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "496e3afd58764673a6b80d4e1d7f4792", "retry_of": "ca6d528ed0a4469f95566436e36e2ac |
| 3624 | 2026-09-30 19:07:52 | ca6d528e | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3625 | 2026-09-30 19:07:57 | 35fb2241 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3626 | 2026-09-30 19:07:59 | 08e63748 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-30T20"}} |
| 3627 | 2026-09-30 19:07:59 | 35fb2241 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3628 | 2026-09-30 19:09:02 | 1d45fe25 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-l |
| 3629 | 2026-09-30 19:22:00 | c4afa11d | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3630 | 2026-09-30 19:25:21 | c4afa11d | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 27s [done] report expect='FACTORY' cmd=True \| T3 PASS 29s [d |
| 3631 | 2026-09-30 19:25:21 | c4afa11d | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 27s [done] report expect='FACTORY' cmd=True \| T3 PASS 29s [d |
| 3632 | 2026-09-30 19:25:21 | c4afa11d | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3633 | 2026-09-30 19:25:21 | c86fde5b | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "c4afa11dae3646e191a59bc7b6ee8ee |
| 3634 | 2026-09-30 19:25:21 | c4afa11d | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3635 | 2026-09-30 19:25:25 | 9a330171 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3636 | 2026-09-30 19:28:22 | 9a330171 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 10s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [do |
| 3637 | 2026-09-30 19:28:22 | 9a330171 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 10s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [do |
| 3638 | 2026-09-30 19:28:22 | 9a330171 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3639 | 2026-09-30 19:28:22 | 34860664 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "retry_of": "9a330171f6b0484b93faa435da1bfae |
| 3640 | 2026-09-30 19:28:22 | 9a330171 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3641 | 2026-09-30 19:28:25 | a0a1b9ab | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3642 | 2026-09-30 19:35:32 | a0a1b9ab | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 10s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [do |
| 3643 | 2026-09-30 19:35:32 | a0a1b9ab | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 10s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [do |
| 3644 | 2026-09-30 19:35:32 | 4fd160dc | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a0a1b9ab216b4a118bb051444ec5ab5a", "after_quota": "a0a1b9ab216b4a118bb051444ec5a |
| 3645 | 2026-09-30 19:35:32 | a0a1b9ab | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3646 | 2026-09-30 19:35:36 | 502b64ce | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3647 | 2026-09-30 19:43:55 | 885a0ec2 | 028 | job.enqueued | master-001 | {"kind": "run", "payload": {"bot_id": "028", "task": "review the factory and count how many bots were created", "in": "C:\\AI\\Factory\\work |
| 3648 | 2026-09-30 19:43:57 | 885a0ec2 | 028 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3649 | 2026-09-30 19:43:57 | 885a0ec2 | 028 | bot.ran | fast-LAPTOP-LRE6PSA8 | {"ok": false, "produced": null, "secs": null, "reply": "", "chain": null} |
| 3650 | 2026-09-30 19:43:57 | 885a0ec2 | 028 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: logic: run failed: bot 028 is testing, only active  |
| 3651 | 2026-09-30 19:46:39 | 502b64ce | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 51s [d |
| 3652 | 2026-09-30 19:46:39 | 502b64ce | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 51s [d |
| 3653 | 2026-09-30 19:46:39 | 06a924e4 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "502b64cea6fb4ebb9b31ce8ee7c1cf06", "after_quota": "502b64cea6fb4ebb9b31ce8ee7c1c |
| 3654 | 2026-09-30 19:46:39 | 502b64ce | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3655 | 2026-09-30 19:46:41 | f2538a50 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3656 | 2026-09-30 19:58:06 | f2538a50 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 29s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 52s [d |
| 3657 | 2026-09-30 19:58:06 | f2538a50 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 29s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 52s [d |
| 3658 | 2026-09-30 19:58:06 | c31e227e | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "f2538a50d0d74959a9284ddf41fe13dc", "after_quota": "f2538a50d0d74959a9284ddf41fe1 |
| 3659 | 2026-09-30 19:58:06 | f2538a50 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3660 | 2026-09-30 19:58:08 | c86fde5b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3661 | 2026-09-30 20:07:31 | c19a33bc |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3662 | 2026-09-30 20:07:31 | 18042d50 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-30T21"}} |
| 3663 | 2026-09-30 20:09:18 | c86fde5b | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 50s [done] report expect='FACTORY' cmd=True \| T3 PASS 54s [d |
| 3664 | 2026-09-30 20:09:18 | c86fde5b | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 50s [done] report expect='FACTORY' cmd=True \| T3 PASS 54s [d |
| 3665 | 2026-09-30 20:09:18 | 64b571f1 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "c86fde5b9f3249a696c69dd430ddd566", "after_quota": "c86fde5b9f3249a696c69dd430ddd |
| 3666 | 2026-09-30 20:09:18 | c86fde5b | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3667 | 2026-09-30 20:09:21 | c19a33bc |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qw |
| 3668 | 2026-09-30 20:09:22 | 08e63748 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3669 | 2026-09-30 20:09:23 | baef1892 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-30T21"}} |
| 3670 | 2026-09-30 20:09:23 | 08e63748 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3671 | 2026-09-30 20:09:26 | 34860664 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3672 | 2026-09-30 20:20:21 | 34860664 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 56s [d |
| 3673 | 2026-09-30 20:20:21 | 34860664 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 56s [d |
| 3674 | 2026-09-30 20:20:21 | 68b9c7c1 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "348606642c1d455ca3fa0f011dcc1967", "after_quota": "348606642c1d455ca3fa0f011dcc1 |
| 3675 | 2026-09-30 20:20:21 | 34860664 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3676 | 2026-09-30 20:49:27 | 5734063d | 017 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3677 | 2026-09-30 20:50:13 | 934721ee | 018 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3678 | 2026-09-30 20:50:51 | 5734063d | 017 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 19s [done] expect='3' last='RESULT: 3' \| T3 PASS 21s [done] expect='3' l |
| 3679 | 2026-09-30 20:50:51 | 5734063d | 017 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 19s [done] expect='3' last='RESULT: 3' \| T3 PASS 21s [done] expect='3' l |
| 3680 | 2026-09-30 20:50:51 | 5734063d | 017 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "017", "status": "active", "verified": "VERIFIED"}} |
| 3681 | 2026-09-30 20:51:53 | 934721ee | 018 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 PASS 34s [done] expect='30' last='RESULT: 30' \| T3 PASS 37s [done] expect='2 |
| 3682 | 2026-09-30 20:51:53 | 934721ee | 018 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 PASS 34s [done] expect='30' last='RESULT: 30' \| T3 PASS 37s [done] expect='2 |
| 3683 | 2026-09-30 20:51:53 | 934721ee | 018 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "status": "active", "verified": "VERIFIED"}} |
| 3684 | 2026-09-30 21:07:32 | 18042d50 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3685 | 2026-09-30 21:07:32 | acd6e0e7 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-30T22"}} |
| 3686 | 2026-09-30 21:08:06 | 18042d50 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash38", "gemini-gemma26b", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b" |
| 3687 | 2026-09-30 21:09:25 | baef1892 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3688 | 2026-09-30 21:09:26 | be7ecc01 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-30T22"}} |
| 3689 | 2026-09-30 21:09:26 | baef1892 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3690 | 2026-09-30 21:35:36 | 4fd160dc | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3691 | 2026-09-30 21:47:19 | 4fd160dc | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 3692 | 2026-09-30 21:47:19 | 4fd160dc | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 3693 | 2026-09-30 21:47:19 | 25892fff | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a0a1b9ab216b4a118bb051444ec5ab5a", "after_quota": "4fd160dc251f4b0191e709b11ea28 |
| 3694 | 2026-09-30 21:47:19 | 4fd160dc | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3695 | 2026-09-30 21:47:23 | 06a924e4 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3696 | 2026-09-30 21:59:22 | 06a924e4 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 64s [d |
| 3697 | 2026-09-30 21:59:22 | 06a924e4 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 64s [d |
| 3698 | 2026-09-30 21:59:22 | 1446fcc7 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "502b64cea6fb4ebb9b31ce8ee7c1cf06", "after_quota": "06a924e48e2643879f7b3e49657d8 |
| 3699 | 2026-09-30 21:59:22 | 06a924e4 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3700 | 2026-09-30 21:59:24 | c31e227e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3701 | 2026-09-30 22:07:33 | acd6e0e7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3702 | 2026-09-30 22:07:33 | 43cba625 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-30T23"}} |
| 3703 | 2026-09-30 22:08:13 | acd6e0e7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwe |
| 3704 | 2026-09-30 22:09:28 | be7ecc01 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3705 | 2026-09-30 22:09:29 | f82f607a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-30T23"}} |
| 3706 | 2026-09-30 22:09:29 | be7ecc01 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3707 | 2026-09-30 22:11:02 | c31e227e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 3708 | 2026-09-30 22:11:02 | c31e227e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 3709 | 2026-09-30 22:11:02 | 2a19c229 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "f2538a50d0d74959a9284ddf41fe13dc", "after_quota": "c31e227e1ed74d24aacafba16e54f |
| 3710 | 2026-09-30 22:11:02 | c31e227e | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3711 | 2026-09-30 22:11:04 | 64b571f1 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3712 | 2026-09-30 22:22:49 | 64b571f1 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 3713 | 2026-09-30 22:22:49 | 64b571f1 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 3714 | 2026-09-30 22:22:49 | af18c815 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "c86fde5b9f3249a696c69dd430ddd566", "after_quota": "64b571f140bc436d85f42463eb988 |
| 3715 | 2026-09-30 22:22:49 | 64b571f1 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3716 | 2026-09-30 22:22:52 | 68b9c7c1 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3717 | 2026-09-30 22:35:10 | 68b9c7c1 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 3718 | 2026-09-30 22:35:10 | 68b9c7c1 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 3719 | 2026-09-30 22:35:10 | 602a3fa3 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "348606642c1d455ca3fa0f011dcc1967", "after_quota": "68b9c7c1bb06497a95c6c9e3037bd |
| 3720 | 2026-09-30 22:35:10 | 68b9c7c1 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3721 | 2026-09-30 23:20:25 | 43cba625 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3722 | 2026-09-30 23:20:25 | f82f607a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3723 | 2026-09-30 23:20:25 | ad27fc01 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-01T00"}} |
| 3724 | 2026-09-30 23:20:36 | b762c8eb |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-01T00"}} |
| 3725 | 2026-09-30 23:20:36 | f82f607a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3726 | 2026-09-30 23:20:53 | 43cba625 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qw |
| 3727 | 2026-09-30 23:47:22 | 25892fff | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3728 | 2026-09-30 23:58:06 | 25892fff | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 57s [d |
| 3729 | 2026-09-30 23:58:06 | 25892fff | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 57s [d |
| 3730 | 2026-09-30 23:58:06 | 25892fff | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3731 | 2026-09-30 23:58:06 | e8540642 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "25892fff7f3944c7b52fe5ea6c1063e |
| 3732 | 2026-09-30 23:58:06 | 25892fff | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3733 | 2026-09-30 23:59:24 | 1446fcc7 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3734 | 2026-10-01 00:11:40 | 1446fcc7 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 97s [d |
| 3735 | 2026-10-01 00:11:40 | 1446fcc7 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 97s [d |
| 3736 | 2026-10-01 00:11:40 | 5a64e9db | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "502b64cea6fb4ebb9b31ce8ee7c1cf06", "after_quota": "1446fcc75a234baf8e0fe6c668179 |
| 3737 | 2026-10-01 00:11:40 | 1446fcc7 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3738 | 2026-10-01 00:11:40 | 2a19c229 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3739 | 2026-10-01 00:20:29 | ad27fc01 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3740 | 2026-10-01 00:20:29 | 8caa5d96 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-01T01"}} |
| 3741 | 2026-10-01 00:20:38 | ad27fc01 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 3742 | 2026-10-01 00:20:38 | ad27fc01 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-gemma26b", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 500, |
| 3743 | 2026-10-01 00:20:38 | 703054e7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-01", "trigger": "blocked:gemini-flash36,gemini-gemma26b"}} |
| 3744 | 2026-10-01 00:20:38 | a2e2f56e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-01", "trigger": "blocked:gemini-flash36,gemini-gemma26b"}} |
| 3745 | 2026-10-01 00:20:38 | 898aad60 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-01", "trigger": "blocked:gemini-flash36,gemini-gemma26b"}} |
| 3746 | 2026-10-01 00:20:38 | bc7ae9ef |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-01", "trigger": "blocked:gemini-flash36,gemini-gemma26b"}} |
| 3747 | 2026-10-01 00:20:38 | ed026db8 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-01", "trigger": "blocked:gemini-flash36,gemini-gemma26b"}} |
| 3748 | 2026-10-01 00:20:38 | bfe4d02a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-01", "trigger": "blocked:gemini-flash36,gemini-gemma26b"}} |
| 3749 | 2026-10-01 00:20:38 | ad27fc01 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash38", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", "local4b"], "changed": [["gemini- |
| 3750 | 2026-10-01 00:20:41 | b762c8eb |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3751 | 2026-10-01 00:20:41 | 0017d5c7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-01T01"}} |
| 3752 | 2026-10-01 00:20:41 | b762c8eb |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3753 | 2026-10-01 00:20:44 | 703054e7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3754 | 2026-10-01 00:20:45 | 703054e7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 3755 | 2026-10-01 00:20:47 | a2e2f56e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3756 | 2026-10-01 00:20:48 | a2e2f56e |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 3757 | 2026-10-01 00:20:51 | 898aad60 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3758 | 2026-10-01 00:20:52 | 898aad60 |  | lane.rejected | svc-LAPTOP-LRE6PSA8 | {"model": "thinkingmachines/inkling-small:free", "reason": "probe auth: {\"error\":{\"message\":\"thinkingmachines/inkling-small:free is onl |
| 3759 | 2026-10-01 00:20:52 | 898aad60 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 3760 | 2026-10-01 00:20:55 | bc7ae9ef |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3761 | 2026-10-01 00:20:55 | bc7ae9ef |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3762 | 2026-10-01 00:20:58 | ed026db8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3763 | 2026-10-01 00:20:58 | ed026db8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3764 | 2026-10-01 00:21:01 | bfe4d02a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3765 | 2026-10-01 00:21:01 | bfe4d02a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3766 | 2026-10-01 00:22:59 | 2a19c229 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 3767 | 2026-10-01 00:22:59 | 2a19c229 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 3768 | 2026-10-01 00:22:59 | d95c367c | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "f2538a50d0d74959a9284ddf41fe13dc", "after_quota": "2a19c229856b4472a6969e1653d8b |
| 3769 | 2026-10-01 00:22:59 | 2a19c229 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3770 | 2026-10-01 00:22:59 | af18c815 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3771 | 2026-10-01 00:41:02 | af18c815 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 106s [done] report expect='FACTORY' cmd=True \| T3 PASS 83s [ |
| 3772 | 2026-10-01 00:41:02 | af18c815 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 106s [done] report expect='FACTORY' cmd=True \| T3 PASS 83s [ |
| 3773 | 2026-10-01 00:41:02 | fd5ae898 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "c86fde5b9f3249a696c69dd430ddd566", "after_quota": "af18c815cf914d408e37524aef2e1 |
| 3774 | 2026-10-01 00:41:02 | af18c815 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3775 | 2026-10-01 00:41:03 | e8540642 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3776 | 2026-10-01 00:58:14 | e8540642 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 55s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 104s [done] report expect='FACTORY' cmd=True \| T3 PASS 102s  |
| 3777 | 2026-10-01 00:58:14 | e8540642 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 55s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 104s [done] report expect='FACTORY' cmd=True \| T3 PASS 102s  |
| 3778 | 2026-10-01 00:58:14 | d616c8ba | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "e85406426dc6462bbc1f93f46d2aa77e", "after_quota": "e85406426dc6462bbc1f93f46d2aa |
| 3779 | 2026-10-01 00:58:14 | e8540642 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3780 | 2026-10-01 00:58:17 | 602a3fa3 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3781 | 2026-10-01 01:14:01 | 602a3fa3 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 56s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 103s [done] report expect='FACTORY' cmd=True \| T3 PASS 92s [ |
| 3782 | 2026-10-01 01:14:01 | 602a3fa3 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 56s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 103s [done] report expect='FACTORY' cmd=True \| T3 PASS 92s [ |
| 3783 | 2026-10-01 01:14:01 | d6562839 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "348606642c1d455ca3fa0f011dcc1967", "after_quota": "602a3fa38413437eabb7b8d88e160 |
| 3784 | 2026-10-01 01:14:01 | 602a3fa3 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3785 | 2026-10-01 01:20:30 | 8caa5d96 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3786 | 2026-10-01 01:20:30 | 09b4b27c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-01T02"}} |
| 3787 | 2026-10-01 01:20:42 | 8caa5d96 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\n  |
| 3788 | 2026-10-01 01:20:42 | 8caa5d96 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 3789 | 2026-10-01 01:20:42 | f9ec6a4c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-01", "trigger": "blocked:gemini-flash"}} |
| 3790 | 2026-10-01 01:20:42 | f1a1a56c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-01", "trigger": "blocked:gemini-flash"}} |
| 3791 | 2026-10-01 01:20:42 | c9322d1d |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-01", "trigger": "blocked:gemini-flash"}} |
| 3792 | 2026-10-01 01:20:42 | fb7e15df |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-01", "trigger": "blocked:gemini-flash"}} |
| 3793 | 2026-10-01 01:20:42 | 064b8a49 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-01", "trigger": "blocked:gemini-flash"}} |
| 3794 | 2026-10-01 01:20:42 | 5a3049f7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-01", "trigger": "blocked:gemini-flash"}} |
| 3795 | 2026-10-01 01:20:43 | 8caa5d96 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-flash38", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", "local4b", "or- |
| 3796 | 2026-10-01 01:20:44 | 0017d5c7 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3797 | 2026-10-01 01:20:44 | b863515d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-01T02"}} |
| 3798 | 2026-10-01 01:20:44 | 0017d5c7 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3799 | 2026-10-01 01:20:46 | f9ec6a4c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3800 | 2026-10-01 01:20:46 | f9ec6a4c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 3801 | 2026-10-01 01:20:49 | f1a1a56c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3802 | 2026-10-01 01:20:49 | f1a1a56c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3803 | 2026-10-01 01:20:53 | c9322d1d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3804 | 2026-10-01 01:20:53 | c9322d1d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3805 | 2026-10-01 01:20:56 | fb7e15df |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3806 | 2026-10-01 01:20:56 | fb7e15df |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3807 | 2026-10-01 01:21:01 | 064b8a49 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3808 | 2026-10-01 01:21:01 | 064b8a49 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3809 | 2026-10-01 01:21:04 | 5a3049f7 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3810 | 2026-10-01 01:21:04 | 5a3049f7 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3811 | 2026-10-01 02:11:41 | 5a64e9db | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3812 | 2026-10-01 02:20:32 | 09b4b27c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3813 | 2026-10-01 02:20:32 | fe6c7aed |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-01T03"}} |
| 3814 | 2026-10-01 02:20:59 | 09b4b27c |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 3815 | 2026-10-01 02:21:00 | 09b4b27c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", "local4b", "or-li |
| 3816 | 2026-10-01 02:21:03 | b863515d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3817 | 2026-10-01 02:21:04 | 130008d4 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-01T03"}} |
| 3818 | 2026-10-01 02:21:04 | b863515d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3819 | 2026-10-01 02:26:36 | 5a64e9db | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 93s [done] report expect='FACTORY' cmd=True \| T3 PASS 79s [d |
| 3820 | 2026-10-01 02:26:36 | 5a64e9db | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 93s [done] report expect='FACTORY' cmd=True \| T3 PASS 79s [d |
| 3821 | 2026-10-01 02:26:36 | d12b9e5f | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "502b64cea6fb4ebb9b31ce8ee7c1cf06", "after_quota": "5a64e9db48564d98ae63254fa1da5 |
| 3822 | 2026-10-01 02:26:36 | 5a64e9db | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3823 | 2026-10-01 02:26:37 | d95c367c | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3824 | 2026-10-01 02:40:37 | d95c367c | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 94s [done] report expect='FACTORY' cmd=True \| T3 PASS 35s [d |
| 3825 | 2026-10-01 02:40:37 | d95c367c | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 94s [done] report expect='FACTORY' cmd=True \| T3 PASS 35s [d |
| 3826 | 2026-10-01 02:40:37 | 44159f49 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "f2538a50d0d74959a9284ddf41fe13dc", "after_quota": "d95c367c13a74737b7848bfa0ab8d |
| 3827 | 2026-10-01 02:40:37 | d95c367c | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3828 | 2026-10-01 02:41:05 | fd5ae898 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3829 | 2026-10-02 01:43:37 | fd5ae898 |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 3830 | 2026-10-02 01:43:37 | fe6c7aed |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3831 | 2026-10-02 01:43:42 | 6ddafcef |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-02T02"}} |
| 3832 | 2026-10-02 01:44:10 | fd5ae898 |  | job.readopted | svc-LAPTOP-LRE6PSA8 | {} |
| 3833 | 2026-10-02 01:44:25 | fe6c7aed |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-gemma26b", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 3834 | 2026-10-02 01:44:25 | fe6c7aed |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-l |
| 3835 | 2026-10-02 01:44:30 | 130008d4 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3836 | 2026-10-02 01:44:30 | 9662e40c | 018 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "run", "payload": {"bot_id": "018", "task": "Sum order totals per country into totals.csv", "in": "C:\\AI\\Factory\\workspace\\inbo |
| 3837 | 2026-10-02 01:44:30 |  | 018 | schedule.fired | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "fire": "2026-10-01T07:00", "job": "9662e40c"} |
| 3838 | 2026-10-02 01:44:33 | 59cf05fb |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-02T02"}} |
| 3839 | 2026-10-02 01:44:33 | 130008d4 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3840 | 2026-10-02 01:44:37 | 9662e40c | 018 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3841 | 2026-10-02 01:45:26 | 9662e40c | 018 | bot.ran | fast-LAPTOP-LRE6PSA8 | {"ok": true, "produced": ["totals.csv"], "secs": 41, "reply": "RESULT: success", "chain": "groq-gptoss120b"} |
| 3842 | 2026-10-02 01:45:26 | 9662e40c | 018 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "name": "run", "status": "ok totals.csv"}} |
| 3843 | 2026-10-02 01:45:30 | 1b7650d4 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3844 | 2026-10-02 01:45:31 | 1b7650d4 |  | audit.verified | fast-LAPTOP-LRE6PSA8 | {"rows": 3842, "hashed": 3090, "first_bad": null} |
| 3845 | 2026-10-02 01:45:31 | 99e5653e |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-10-03"}} |
| 3846 | 2026-10-02 01:45:31 | 0c3f5f27 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-10-02"}} |
| 3847 | 2026-10-02 01:45:31 | d712cbbe |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-10-02"}} |
| 3848 | 2026-10-02 01:45:31 | df14302d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-10-02"}} |
| 3849 | 2026-10-02 01:45:31 | 1b7650d4 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3850 | 2026-10-02 01:47:31 | fd5ae898 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 3851 | 2026-10-02 01:47:34 | d616c8ba | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3852 | 2026-10-02 01:47:35 | df14302d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3853 | 2026-10-02 01:47:35 | 4a92b32a | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3854 | 2026-10-02 01:47:35 | a6892e23 | 009 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "009", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3855 | 2026-10-02 01:47:35 | d8b0189e | 011 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "011", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3856 | 2026-10-02 01:47:35 | dd0512b5 | 012 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "012", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3857 | 2026-10-02 01:47:35 | 3338d776 | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "013", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3858 | 2026-10-02 01:47:35 | 1fbba810 | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "016", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3859 | 2026-10-02 01:47:35 | d2350314 | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "017", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3860 | 2026-10-02 01:47:35 | 9a381a38 | 018 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "018", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3861 | 2026-10-02 01:47:35 | df14302d |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "009", "011", "012", "013", "016", "017", "018"], "jobs": ["4a92b32a", "a6892e23", "d8b0189e", "dd0512b5", "3338d776", "1fb |
| 3862 | 2026-10-02 01:47:35 | df14302d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3863 | 2026-10-02 01:47:38 | a6892e23 | 009 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3864 | 2026-10-02 14:43:45 |  |  | factory.outage | fast-LAPTOP-LRE6PSA8 | {"gap_min": 776, "silent_since": "2026-10-02T01:47:38", "last_event": "job.claimed", "cause": "power loss / battery flat (kernel-power 41)", |
| 3865 | 2026-10-02 14:43:45 |  |  | factory.outage | svc-LAPTOP-LRE6PSA8 | {"gap_min": 776, "silent_since": "2026-10-02T01:47:38", "last_event": "job.claimed", "cause": "power loss / battery flat (kernel-power 41)", |
| 3866 | 2026-10-02 14:43:45 | d616c8ba |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 3867 | 2026-10-02 14:43:45 | a6892e23 |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 3868 | 2026-10-02 14:43:45 | 6ddafcef |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3869 | 2026-10-02 14:43:45 | 22bc8b7b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-02T15"}} |
| 3870 | 2026-10-02 14:43:46 | 59cf05fb |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3871 | 2026-10-02 14:43:46 | ae821249 | 018 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "run", "payload": {"bot_id": "018", "task": "Sum order totals per country into totals.csv", "in": "C:\\AI\\Factory\\workspace\\inbo |
| 3872 | 2026-10-02 14:43:46 |  | 018 | schedule.fired | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "fire": "2026-10-02T07:00", "job": "ae821249"} |
| 3873 | 2026-10-02 14:43:51 | 845fc841 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-02T15"}} |
| 3874 | 2026-10-02 14:43:51 | 59cf05fb |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3875 | 2026-10-02 14:43:56 | fd5ae898 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 3876 | 2026-10-02 14:44:52 | 6ddafcef |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 3877 | 2026-10-02 14:44:56 | ae821249 | 018 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3878 | 2026-10-02 14:45:09 | ae821249 | 018 | bot.ran | svc-LAPTOP-LRE6PSA8 | {"ok": true, "produced": [], "secs": 12, "reply": "Using config: C:\\AI\\Factory\\run\\botcfg\\018-task.json", "chain": "groq-gptoss120b"} |
| 3879 | 2026-10-02 14:45:09 | ae821249 | 018 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "name": "run", "status": "ok "}} |
