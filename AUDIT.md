# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 1625 | 2026-09-25 03:30:40 | 31459526 | 013 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 173s [done] expect='X_OK' last='X_OK' \| T2 FAIL 306s [TIMEOUT] expect='1' last='' \| T3 FAIL 310s [TIMEOUT] expect='0'  |
| 1626 | 2026-09-25 03:30:40 | c3cae46b | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "013", "retest_of": "3145952631084d619cea6973dfe45bb6", "after_quota": "3145952631084d619cea6973dfe45 |
| 1627 | 2026-09-25 03:30:40 | 31459526 | 013 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "013", "status": "active", "verified": "VERIFIED"}} |
| 1628 | 2026-09-25 03:30:44 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1629 | 2026-09-25 03:31:19 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["118 passed in 29.35s"]} |
| 1630 | 2026-09-25 03:31:19 | 667ce093 | 014 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1631 | 2026-09-25 03:31:20 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["118 passed in 30.39s"]} |
| 1632 | 2026-09-25 03:31:20 | 4b8fb54e | 016 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1633 | 2026-09-25 03:36:49 | 4b8fb54e | 016 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] expect='X_OK' last='X_OK' \| T2 FAIL 16s [done] expect='2' last='CAPABILITY_MISSING: write_file' \| T3 PASS 1 |
| 1634 | 2026-09-25 03:36:49 | 4b8fb54e | 016 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] expect='X_OK' last='X_OK' \| T2 FAIL 16s [done] expect='2' last='CAPABILITY_MISSING: write_file' \| T3 PASS 1 |
| 1635 | 2026-09-25 03:36:49 | 4b8fb54e | 016 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1636 | 2026-09-25 03:36:49 | cc163779 | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "016", "max_rounds": 2}} |
| 1637 | 2026-09-25 03:36:49 | 4b8fb54e | 016 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "016", "status": "testing", "verified": "UNVERIFIED"}} |
| 1638 | 2026-09-25 03:36:53 | cc163779 | 016 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1639 | 2026-09-25 03:36:53 | cc163779 | 016 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [], "boundary_diff": {}} |
| 1640 | 2026-09-25 03:36:53 | 88222656 | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "rearchitect", "payload": {"bot_id": "016", "feedback": "logic: spec/tests inconsistent, repair cannot change tools: bot reported C |
| 1641 | 2026-09-25 03:36:53 | cc163779 | 016 | bot.rearchitect_queued | svc-LAPTOP-LRE6PSA8 | {"reason": "logic: spec/tests inconsistent, repair cannot change tools: bot reported CAPABILITY_MISSING"} |
| 1642 | 2026-09-25 03:36:53 | cc163779 | 016 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: logic: spec/tests inconsistent, repair cannot chang |
| 1643 | 2026-09-25 03:36:56 | 88222656 | 016 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1644 | 2026-09-25 03:38:13 | 88222656 | 016 | bot.rearchitected | svc-LAPTOP-LRE6PSA8 | {"lane": "groq:openai/gpt-oss-20b", "tools": ["exec"], "permissions": ["fs:read", "shell:workspace"], "boundary_diff": {"permissions_added": |
| 1645 | 2026-09-25 03:38:13 | 88222656 | 016 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1646 | 2026-09-25 03:38:13 | cc163779 |  | job.cancelled | svc-LAPTOP-LRE6PSA8 | {} |
| 1647 | 2026-09-25 03:38:13 | cc163779 | 016 | job.superseded | svc-LAPTOP-LRE6PSA8 | {"by": "88222656c78f49cfb2a6e4f6e5b47c26"} |
| 1648 | 2026-09-25 03:38:13 | 88222656 | 016 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "016", "pass": 4, "total": 4, "status": "active"}} |
| 1649 | 2026-09-25 03:38:16 | 5ba4ca8c | 017 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1650 | 2026-09-25 03:44:53 | 667ce093 | 014 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] expect='X_OK' last='X_OK' \| T2 FAIL 307s [TIMEOUT] expect='5' last='' \| T3 FAIL 308s [TIMEOUT] expect='Time |
| 1651 | 2026-09-25 03:44:53 | 667ce093 | 014 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] expect='X_OK' last='X_OK' \| T2 FAIL 307s [TIMEOUT] expect='5' last='' \| T3 FAIL 308s [TIMEOUT] expect='Time |
| 1652 | 2026-09-25 03:44:53 | 7847f8ec | 014 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "014", "retest_of": "667ce093cc1d45b2a1e4f53ea27c1fd9", "after_quota": "667ce093cc1d45b2a1e4f53ea27c1 |
| 1653 | 2026-09-25 03:44:53 | 667ce093 | 014 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "014", "status": "active", "verified": "VERIFIED"}} |
| 1654 | 2026-09-25 03:44:56 | e5ef19df | 018 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1655 | 2026-09-25 03:46:40 | 5ba4ca8c | 017 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 61s [done] expect='X_OK' last='RESULT: X_OK' \| T2 FAIL 155s [done] expect='3' last='\u00e2\u2020\u00b3 read names.txt'  |
| 1656 | 2026-09-25 03:46:40 | 5ba4ca8c | 017 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 61s [done] expect='X_OK' last='RESULT: X_OK' \| T2 FAIL 155s [done] expect='3' last='\u00e2\u2020\u00b3 read names.txt'  |
| 1657 | 2026-09-25 03:46:40 | 5ba4ca8c | 017 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1658 | 2026-09-25 03:46:40 | 9b60274b | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "017", "max_rounds": 2}} |
| 1659 | 2026-09-25 03:46:40 | 5ba4ca8c | 017 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "017", "status": "testing", "verified": "UNVERIFIED"}} |
| 1660 | 2026-09-25 03:46:43 | 9b60274b | 017 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1661 | 2026-09-25 03:55:14 | e5ef19df | 018 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 68s [done] expect='X_OK' last='X_OK' \| T2 PASS 300s [done] expect='30' last='RESULT: 30' \| T3 PASS 191s [done] expect= |
| 1662 | 2026-09-25 03:55:14 | e5ef19df | 018 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 68s [done] expect='X_OK' last='X_OK' \| T2 PASS 300s [done] expect='30' last='RESULT: 30' \| T3 PASS 191s [done] expect= |
| 1663 | 2026-09-25 03:55:14 | e5ef19df | 018 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "status": "active", "verified": "VERIFIED"}} |
| 1664 | 2026-09-25 03:55:17 | 6f04db95 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1665 | 2026-09-25 03:55:17 | 509087ef |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T04"}} |
| 1666 | 2026-09-25 03:57:00 | 6f04db95 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 1667 | 2026-09-25 03:57:00 | 5866157b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1668 | 2026-09-25 03:57:00 | 71d0bcfc |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1669 | 2026-09-25 03:57:00 | 9b42f1aa |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1670 | 2026-09-25 03:57:00 | 52fea279 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1671 | 2026-09-25 03:57:00 | 279f51c7 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1672 | 2026-09-25 03:57:00 | d540257b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1673 | 2026-09-25 03:57:00 | 6f04db95 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss1 |
| 1674 | 2026-09-25 03:57:03 | abed8a6c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1675 | 2026-09-25 03:57:03 | 586e9f0e |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T04"}} |
| 1676 | 2026-09-25 03:57:03 | abed8a6c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1677 | 2026-09-25 03:57:05 | 5866157b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1678 | 2026-09-25 03:57:06 | 5866157b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1679 | 2026-09-25 03:57:08 | 71d0bcfc |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1680 | 2026-09-25 03:57:08 | 71d0bcfc |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1681 | 2026-09-25 03:57:11 | 9b42f1aa |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1682 | 2026-09-25 03:57:11 | 9b42f1aa |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1683 | 2026-09-25 03:57:12 | 9b60274b | 017 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 1684 | 2026-09-25 03:57:12 | 9b60274b | 017 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1685 | 2026-09-25 03:57:12 | 9b60274b | 017 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "017", "status": "active"}} |
| 1686 | 2026-09-25 03:57:13 | 52fea279 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1687 | 2026-09-25 03:57:13 | 52fea279 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1688 | 2026-09-25 03:57:16 | 279f51c7 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1689 | 2026-09-25 03:57:16 | 279f51c7 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1690 | 2026-09-25 03:57:18 | d540257b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1691 | 2026-09-25 03:57:18 | d540257b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1692 | 2026-09-25 03:57:21 | 13956caf | 019 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1693 | 2026-09-25 03:57:21 | 3b53fab8 | 020 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1694 | 2026-09-25 04:01:20 | 13956caf | 019 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] expect='X_OK' last='X_OK' \| T2 PASS 99s [done] expect='1' last='RESULT: 1' \| T3 PASS 102s [done] expect='CO |
| 1695 | 2026-09-25 04:01:20 | 13956caf | 019 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] expect='X_OK' last='X_OK' \| T2 PASS 99s [done] expect='1' last='RESULT: 1' \| T3 PASS 102s [done] expect='CO |
| 1696 | 2026-09-25 04:01:20 | 13956caf | 019 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "019", "status": "active", "verified": "VERIFIED"}} |
| 1697 | 2026-09-25 04:01:23 | 72522ac3 | 021 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1698 | 2026-09-25 04:03:07 | 3b53fab8 | 020 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] expect='X_OK' last='X_OK' \| T2 FAIL 305s [TIMEOUT] expect='DONE' last='' \| T3 PASS 19s [done] expect='CONFI |
| 1699 | 2026-09-25 04:03:07 | 3b53fab8 | 020 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] expect='X_OK' last='X_OK' \| T2 FAIL 305s [TIMEOUT] expect='DONE' last='' \| T3 PASS 19s [done] expect='CONFI |
| 1700 | 2026-09-25 04:03:07 | 3d281d06 | 020 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "020", "retest_of": "3b53fab8c9474ef6a1570af2666136be", "after_quota": "3b53fab8c9474ef6a1570af266613 |
| 1701 | 2026-09-25 04:03:07 | 3b53fab8 | 020 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "020", "status": "active", "verified": "VERIFIED"}} |
| 1702 | 2026-09-25 04:03:10 | 2332bee3 | 022 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1703 | 2026-09-25 04:03:26 | 72522ac3 | 021 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] expect='X_OK' last='X_OK' \| T2 PASS 46s [done] expect='2' last='2' \| T3 FAIL 6s [done] expect='1' last='Usi |
| 1704 | 2026-09-25 04:03:26 | 72522ac3 | 021 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] expect='X_OK' last='X_OK' \| T2 PASS 46s [done] expect='2' last='2' \| T3 FAIL 6s [done] expect='1' last='Usi |
| 1705 | 2026-09-25 04:03:26 | d62f34ea | 021 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "021", "retest_of": "72522ac3aab24ff0bee10f6aec1dbe28", "after_quota": "72522ac3aab24ff0bee10f6aec1db |
| 1706 | 2026-09-25 04:03:26 | 72522ac3 | 021 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "021", "status": "active", "verified": "VERIFIED"}} |
| 1707 | 2026-09-25 04:03:28 | 35e53778 | 023 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1708 | 2026-09-25 04:08:08 | 35e53778 | 023 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] expect='X_OK' last='X_OK' \| T2 PASS 86s [done] expect='36.0' last='RESULT: 36.0' \| T3 PASS 127s [done] expe |
| 1709 | 2026-09-25 04:08:08 | 35e53778 | 023 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] expect='X_OK' last='X_OK' \| T2 PASS 86s [done] expect='36.0' last='RESULT: 36.0' \| T3 PASS 127s [done] expe |
| 1710 | 2026-09-25 04:08:08 | 35e53778 | 023 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "023", "status": "active", "verified": "VERIFIED"}} |
| 1711 | 2026-09-25 04:08:10 | e766a89e | 024 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1712 | 2026-09-25 04:08:58 | e766a89e | 024 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] expect='X_OK' last='X_OK' \| T2 PASS 18s [done] expect='2' last='RESULT: 2' \| T3 PASS 17s [done] expect='CON |
| 1713 | 2026-09-25 04:08:58 | e766a89e | 024 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] expect='X_OK' last='X_OK' \| T2 PASS 18s [done] expect='2' last='RESULT: 2' \| T3 PASS 17s [done] expect='CON |
| 1714 | 2026-09-25 04:08:58 | e766a89e | 024 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "024", "status": "active", "verified": "VERIFIED"}} |
| 1715 | 2026-09-25 04:08:58 | 2332bee3 | 022 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] expect='X_OK' last='X_OK' \| T2 PASS 183s [done] expect='2' last='RESULT: 2' \| T3 PASS 108s [done] expect='2 |
| 1716 | 2026-09-25 04:08:58 | 2332bee3 | 022 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] expect='X_OK' last='X_OK' \| T2 PASS 183s [done] expect='2' last='RESULT: 2' \| T3 PASS 108s [done] expect='2 |
| 1717 | 2026-09-25 04:08:58 | 2332bee3 | 022 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "022", "status": "active", "verified": "VERIFIED"}} |
| 1718 | 2026-09-25 04:09:01 | e3d0b490 | 025 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1719 | 2026-09-25 04:09:04 | 3f73d2dd | 026 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1720 | 2026-09-25 04:09:51 | e3d0b490 | 025 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='LIVENESS_OK' last='LIVENESS_OK' \| T2 PASS 20s [done] expect='HELLO WORLD' last='RESULT: HELLO WORLD' |
| 1721 | 2026-09-25 04:09:51 | e3d0b490 | 025 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='LIVENESS_OK' last='LIVENESS_OK' \| T2 PASS 20s [done] expect='HELLO WORLD' last='RESULT: HELLO WORLD' |
| 1722 | 2026-09-25 04:09:51 | e3d0b490 | 025 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "025", "status": "active", "verified": "VERIFIED"}} |
| 1723 | 2026-09-25 04:10:32 | 3f73d2dd | 026 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] expect='X_OK' last='X_OK' \| T2 PASS 23s [done] expect='3' last='RESULT: 3' \| T3 PASS 23s [done] expect='use |
| 1724 | 2026-09-25 04:10:32 | 3f73d2dd | 026 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] expect='X_OK' last='X_OK' \| T2 PASS 23s [done] expect='3' last='RESULT: 3' \| T3 PASS 23s [done] expect='use |
| 1725 | 2026-09-25 04:10:32 | 3f73d2dd | 026 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "026", "status": "active", "verified": "VERIFIED"}} |
| 1726 | 2026-09-25 04:10:35 | 6ba4e1dc |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1727 | 2026-09-25 04:10:35 | 6ba4e1dc |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": []}} |
| 1728 | 2026-09-25 04:10:38 | 1b095896 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1729 | 2026-09-25 04:11:09 | 1b095896 |  | factory.canary | svc-LAPTOP-LRE6PSA8 | {"verdict": "pass", "lane": "groq:openai/gpt-oss-20b", "chain": ["gemini-gemini-flash-lite-latest", "gemini-lite31", "or-nex-n25-pro", "or-l |
| 1730 | 2026-09-25 04:11:09 | 1b095896 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"pass": 2, "total": 2}} |
| 1731 | 2026-09-25 04:55:18 | 509087ef |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1732 | 2026-09-25 04:55:18 | 321d882a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T05"}} |
| 1733 | 2026-09-25 04:55:28 | 509087ef |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss1 |
| 1734 | 2026-09-25 04:57:06 | 586e9f0e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1735 | 2026-09-25 04:57:06 | 5249b5ec |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T05"}} |
| 1736 | 2026-09-25 04:57:06 | 586e9f0e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1737 | 2026-09-25 05:30:42 | c3cae46b | 013 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1738 | 2026-09-25 05:32:29 | c3cae46b | 013 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 21s [done] expect='X_OK' last='RESULT: 1' \| T2 PASS 27s [done] expect='1' last='RESULT: 1' \| T3 PASS 28s [done] expect |
| 1739 | 2026-09-25 05:32:29 | c3cae46b | 013 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 21s [done] expect='X_OK' last='RESULT: 1' \| T2 PASS 27s [done] expect='1' last='RESULT: 1' \| T3 PASS 28s [done] expect |
| 1740 | 2026-09-25 05:32:29 | c3cae46b | 013 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1741 | 2026-09-25 05:32:29 | 9c18c9e9 | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "013", "max_rounds": 2}} |
| 1742 | 2026-09-25 05:32:29 | c3cae46b | 013 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "013", "status": "testing", "verified": "UNVERIFIED"}} |
| 1743 | 2026-09-25 05:32:32 | 9c18c9e9 | 013 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1744 | 2026-09-25 05:33:49 | 9c18c9e9 | 013 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 1745 | 2026-09-25 05:33:49 | 9c18c9e9 | 013 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1746 | 2026-09-25 05:33:49 | 9c18c9e9 | 013 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "013", "status": "active"}} |
| 1747 | 2026-09-25 11:22:56 | 5249b5ec |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1748 | 2026-09-25 11:22:57 | 321d882a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1749 | 2026-09-25 11:22:58 | 03fe2791 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T12"}} |
| 1750 | 2026-09-25 11:22:59 | dae5c79f | 018 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "run", "payload": {"bot_id": "018", "task": "Sum order totals per country into totals.csv", "in": "C:\\AI\\Factory\\workspace\\inbo |
| 1751 | 2026-09-25 11:22:59 |  | 018 | schedule.fired | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "fire": "2026-09-25T07:00", "job": "dae5c79f"} |
| 1752 | 2026-09-25 11:23:04 | e354bd05 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T12"}} |
| 1753 | 2026-09-25 11:23:04 | 5249b5ec |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1754 | 2026-09-25 11:23:05 | 7847f8ec | 014 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1755 | 2026-09-25 11:23:15 | 321d882a |  | model.retired | fast-LAPTOP-LRE6PSA8 | {"model": "or-deepseek", "reason": "gone: {\"error\":{\"message\":\"this model is unavailable for free. the paid version "} |
| 1756 | 2026-09-25 11:23:15 | 321d882a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite |
| 1757 | 2026-09-25 11:23:18 | 3d281d06 | 020 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1758 | 2026-09-25 11:25:27 | 7847f8ec | 014 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 28s [done] expect='5' last='RESULT: 5' \| T3 PASS 71s [done] expect='Tim |
| 1759 | 2026-09-25 11:25:27 | 7847f8ec | 014 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 28s [done] expect='5' last='RESULT: 5' \| T3 PASS 71s [done] expect='Tim |
| 1760 | 2026-09-25 11:25:27 | 7847f8ec | 014 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "014", "status": "active", "verified": "VERIFIED"}} |
| 1761 | 2026-09-25 11:25:30 | d62f34ea | 021 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1762 | 2026-09-25 11:27:31 | d62f34ea | 021 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 45s [done] expect='2' last='RESULT: 2' \| T3 PASS 40s [done] expect='1' l |
| 1763 | 2026-09-25 11:27:31 | d62f34ea | 021 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 45s [done] expect='2' last='RESULT: 2' \| T3 PASS 40s [done] expect='1' l |
| 1764 | 2026-09-25 11:27:31 | d62f34ea | 021 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "021", "status": "active", "verified": "VERIFIED"}} |
| 1765 | 2026-09-25 11:27:34 | dae5c79f | 018 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1766 | 2026-09-25 11:28:17 | dae5c79f | 018 | bot.ran | svc-LAPTOP-LRE6PSA8 | {"ok": true, "produced": ["totals.csv"], "secs": 42, "reply": "RESULT: success", "chain": "groq-gptoss120b"} |
| 1767 | 2026-09-25 11:28:17 | dae5c79f | 018 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "name": "run", "status": "ok totals.csv"}} |
| 1768 | 2026-09-25 11:28:44 | 3d281d06 | 020 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 FAIL 306s [TIMEOUT] expect='DONE' last='' \| T3 PASS 9s [done] expect='CONFIN |
| 1769 | 2026-09-25 11:28:44 | 3d281d06 | 020 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 FAIL 306s [TIMEOUT] expect='DONE' last='' \| T3 PASS 9s [done] expect='CONFIN |
| 1770 | 2026-09-25 11:28:44 | a35b45be | 020 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "020", "retest_of": "3b53fab8c9474ef6a1570af2666136be", "after_quota": "3d281d0693674fd4a5e204ec31add |
| 1771 | 2026-09-25 11:28:44 | 3d281d06 | 020 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "020", "status": "active", "verified": "VERIFIED"}} |
| 1772 | 2026-09-25 12:23:57 | 03fe2791 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1773 | 2026-09-25 12:23:57 | e354bd05 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1774 | 2026-09-25 12:23:57 | 0a541bde |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T13"}} |
| 1775 | 2026-09-25 12:24:03 | e1e4c7f4 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T13"}} |
| 1776 | 2026-09-25 12:24:03 | e354bd05 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1777 | 2026-09-25 12:24:15 | 03fe2791 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 1778 | 2026-09-25 12:24:15 | 03fe2791 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-l |
| 1779 | 2026-09-25 13:23:58 | 0a541bde |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1780 | 2026-09-25 13:23:58 | 4f127831 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T14"}} |
| 1781 | 2026-09-25 13:24:05 | e1e4c7f4 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1782 | 2026-09-25 13:24:05 | b7558c0f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T14"}} |
| 1783 | 2026-09-25 13:24:05 | e1e4c7f4 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1784 | 2026-09-25 13:24:19 | 0a541bde |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 1785 | 2026-09-25 13:24:19 | 426bd52b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1786 | 2026-09-25 13:24:19 | 624ec5f9 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1787 | 2026-09-25 13:24:19 | 29f3da03 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1788 | 2026-09-25 13:24:19 | a3514a3e |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1789 | 2026-09-25 13:24:19 | c14ad4dd |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1790 | 2026-09-25 13:24:19 | 23979c6a |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1791 | 2026-09-25 13:24:19 | 0a541bde |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite |
| 1792 | 2026-09-25 13:24:22 | 426bd52b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1793 | 2026-09-25 13:24:22 | 426bd52b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1794 | 2026-09-25 13:24:23 | 624ec5f9 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1795 | 2026-09-25 13:24:24 | 624ec5f9 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1796 | 2026-09-25 13:24:25 | 29f3da03 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1797 | 2026-09-25 13:24:25 | 29f3da03 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1798 | 2026-09-25 13:24:28 | a3514a3e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1799 | 2026-09-25 13:24:28 | a3514a3e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1800 | 2026-09-25 13:24:31 | c14ad4dd |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1801 | 2026-09-25 13:24:31 | c14ad4dd |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1802 | 2026-09-25 13:24:33 | 23979c6a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1803 | 2026-09-25 13:24:33 | 23979c6a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1804 | 2026-09-25 14:20:17 | a35b45be | 020 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1805 | 2026-09-25 19:59:42 | a35b45be |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 1806 | 2026-09-25 19:59:42 | 4f127831 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1807 | 2026-09-25 19:59:42 | 865a2980 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T20"}} |
| 1808 | 2026-09-25 19:59:44 | 4f127831 |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 16 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 1809 | 2026-09-25 19:59:44 | 96ccf58b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T14-retry", "retry_of": "4f127831509c447c8aaaba0702a59478"}} |
| 1810 | 2026-09-25 19:59:44 | 4f127831 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1811 | 2026-09-25 19:59:48 | b7558c0f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1812 | 2026-09-25 19:59:52 | 54829a12 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T20"}} |
| 1813 | 2026-09-25 19:59:52 | b7558c0f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1814 | 2026-09-25 20:00:00 | a35b45be | 020 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 1815 | 2026-09-25 20:02:28 | a35b45be | 020 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 PASS 124s [done] expect='DONE' last='DONE' \| T3 PASS 12s [done] expect='CONF |
| 1816 | 2026-09-25 20:02:28 | a35b45be | 020 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 PASS 124s [done] expect='DONE' last='DONE' \| T3 PASS 12s [done] expect='CONF |
| 1817 | 2026-09-25 20:02:28 | a35b45be | 020 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "020", "status": "active", "verified": "VERIFIED"}} |
| 1818 | 2026-09-25 20:05:30 | a35b45be | 020 | job.orphaned_result | fast-LAPTOP-LRE6PSA8 | {"error": "Command '['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', 'C:\\\\AI\\\\Factory\\\\repo\\\\scripts\\\\windows\\ |
| 1819 | 2026-09-25 20:09:44 | 96ccf58b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1820 | 2026-09-25 20:09:45 | 80e90b9b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T21"}} |
| 1821 | 2026-09-25 20:10:16 | 96ccf58b |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 1822 | 2026-09-25 20:10:16 | 96ccf58b |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "or-nex-n25-pro", "outcome": "gone", "before": "VERIFIED", "after": "BLOCKED", "detail": "{\"error\":{\"message\":\"no endpoints f |
| 1823 | 2026-09-25 20:10:16 | 134bba89 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-09-25", "trigger": "blocked:or-nex-n25-pro"}} |
| 1824 | 2026-09-25 20:10:16 | 01537a5d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-09-25", "trigger": "blocked:or-nex-n25-pro"}} |
| 1825 | 2026-09-25 20:10:16 | 3fa27047 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-25", "trigger": "blocked:or-nex-n25-pro"}} |
| 1826 | 2026-09-25 20:10:16 | 2bbe411d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-25", "trigger": "blocked:or-nex-n25-pro"}} |
| 1827 | 2026-09-25 20:10:16 | a7cf454b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-25", "trigger": "blocked:or-nex-n25-pro"}} |
| 1828 | 2026-09-25 20:10:16 | e9039318 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-25", "trigger": "blocked:or-nex-n25-pro"}} |
| 1829 | 2026-09-25 20:10:16 | a1ec1245 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": ["014"], "day": "2026-09-25", "canary_for": ["or-nex-n25-pro"]}} |
| 1830 | 2026-09-25 20:10:16 | 96ccf58b |  | monitor.canary | fast-LAPTOP-LRE6PSA8 | {"lanes": ["or-nex-n25-pro"], "bots": ["014"]} |
| 1831 | 2026-09-25 20:10:16 | 96ccf58b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 1832 | 2026-09-25 20:10:20 | 134bba89 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1833 | 2026-09-25 20:10:20 | 01537a5d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1834 | 2026-09-25 20:10:21 | 134bba89 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1835 | 2026-09-25 20:10:21 | 01537a5d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1836 | 2026-09-25 20:10:25 | 3fa27047 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1837 | 2026-09-25 20:10:26 | 3fa27047 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1838 | 2026-09-25 20:10:30 | 2bbe411d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1839 | 2026-09-25 20:10:30 | 2bbe411d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1840 | 2026-09-25 20:10:34 | a7cf454b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1841 | 2026-09-25 20:10:34 | a7cf454b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1842 | 2026-09-25 20:10:38 | e9039318 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1843 | 2026-09-25 20:10:38 | e9039318 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1844 | 2026-09-25 20:10:43 | a1ec1245 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1845 | 2026-09-25 20:10:43 | 6acda974 | 014 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "014", "monitor_of": "a1ec1245d09c465fb7daaec24fbd41f2", "day": "2026-09-25"}} |
| 1846 | 2026-09-25 20:10:43 | a1ec1245 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["014"], "jobs": ["6acda974"]} |
| 1847 | 2026-09-25 20:10:43 | a1ec1245 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1848 | 2026-09-25 20:10:48 | 6acda974 | 014 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1849 | 2026-09-25 20:12:29 | 6acda974 | 014 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 14s [done] expect='5' last='RESULT: 5' \| T3 PASS 63s [done] expect='Time |
| 1850 | 2026-09-25 20:12:29 | 6acda974 | 014 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 14s [done] expect='5' last='RESULT: 5' \| T3 PASS 63s [done] expect='Time |
| 1851 | 2026-09-25 20:12:29 | 6acda974 | 014 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "014", "status": "active", "verified": "VERIFIED"}} |
| 1852 | 2026-09-25 20:59:46 | 865a2980 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1853 | 2026-09-25 20:59:46 | 80e90b9b |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 1854 | 2026-09-25 20:59:57 | 54829a12 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1855 | 2026-09-25 20:59:58 | a7ddc40b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T21"}} |
| 1856 | 2026-09-25 20:59:58 | 54829a12 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1857 | 2026-09-25 21:00:44 | 865a2980 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 1858 | 2026-09-25 21:00:44 | 00afddce |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1859 | 2026-09-25 21:00:44 | 5146a28d |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1860 | 2026-09-25 21:00:44 | f0d2836f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1861 | 2026-09-25 21:00:44 | af65672a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1862 | 2026-09-25 21:00:44 | 4c6af4e8 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1863 | 2026-09-25 21:00:44 | 5245a37e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1864 | 2026-09-25 21:00:44 | 865a2980 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 1865 | 2026-09-25 21:00:47 | 00afddce |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1866 | 2026-09-25 21:00:48 | 00afddce |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1867 | 2026-09-25 21:00:48 | 5146a28d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1868 | 2026-09-25 21:00:48 | 5146a28d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1869 | 2026-09-25 21:00:52 | f0d2836f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1870 | 2026-09-25 21:00:52 | f0d2836f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1871 | 2026-09-25 21:00:56 | af65672a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1872 | 2026-09-25 21:00:56 | af65672a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1873 | 2026-09-25 21:01:00 | 4c6af4e8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1874 | 2026-09-25 21:01:00 | 4c6af4e8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1875 | 2026-09-25 21:01:04 | 5245a37e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1876 | 2026-09-25 21:01:04 | 5245a37e |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1877 | 2026-09-25 21:09:49 | 80e90b9b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1878 | 2026-09-25 21:09:49 | 24db754c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T22"}} |
| 1879 | 2026-09-25 21:10:12 | 80e90b9b |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\n  |
| 1880 | 2026-09-25 21:10:12 | 263c1d32 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-09-25", "trigger": "blocked:gemini-flash"}} |
| 1881 | 2026-09-25 21:10:12 | d0076ca3 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-09-25", "trigger": "blocked:gemini-flash"}} |
| 1882 | 2026-09-25 21:10:12 | 03adb38c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-25", "trigger": "blocked:gemini-flash"}} |
| 1883 | 2026-09-25 21:10:12 | 9efc5dbb |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-25", "trigger": "blocked:gemini-flash"}} |
| 1884 | 2026-09-25 21:10:12 | b691ec23 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-25", "trigger": "blocked:gemini-flash"}} |
| 1885 | 2026-09-25 21:10:12 | 8958c7c2 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-25", "trigger": "blocked:gemini-flash"}} |
| 1886 | 2026-09-25 21:10:12 | 80e90b9b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gpto |
| 1887 | 2026-09-25 21:10:14 | 263c1d32 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1888 | 2026-09-25 21:10:15 | 263c1d32 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1889 | 2026-09-25 21:10:16 | d0076ca3 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1890 | 2026-09-25 21:10:16 | d0076ca3 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1891 | 2026-09-25 21:10:19 | 03adb38c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1892 | 2026-09-25 21:10:20 | 03adb38c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1893 | 2026-09-25 21:10:23 | 9efc5dbb |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1894 | 2026-09-25 21:10:23 | 9efc5dbb |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1895 | 2026-09-25 21:10:27 | b691ec23 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1896 | 2026-09-25 21:10:27 | b691ec23 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1897 | 2026-09-25 21:10:31 | 8958c7c2 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1898 | 2026-09-25 21:10:31 | 8958c7c2 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1899 | 2026-09-25 21:59:58 | a7ddc40b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1900 | 2026-09-25 21:59:58 | 6611e45e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T22"}} |
| 1901 | 2026-09-25 21:59:58 | a7ddc40b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1902 | 2026-09-25 22:09:49 | 24db754c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1903 | 2026-09-25 22:09:49 | 2e9399d2 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T23"}} |
| 1904 | 2026-09-25 22:10:07 | 24db754c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gpto |
| 1905 | 2026-09-25 23:00:01 | 6611e45e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1906 | 2026-09-25 23:00:02 | fc8525b1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-26T00"}} |
| 1907 | 2026-09-25 23:00:02 | 6611e45e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1908 | 2026-09-25 23:37:13 | 2e9399d2 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1909 | 2026-09-25 23:37:14 | 595134d5 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-26T00"}} |
| 1910 | 2026-09-25 23:37:32 | 2e9399d2 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 1911 | 2026-09-25 23:37:32 | 2e9399d2 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-li |
| 1912 | 2026-09-26 00:00:03 | fc8525b1 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1913 | 2026-09-26 00:00:03 | 1a1d091d |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-26T01"}} |
| 1914 | 2026-09-26 00:00:03 | fc8525b1 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1915 | 2026-09-26 00:37:15 | 595134d5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1916 | 2026-09-26 00:37:15 | 476304a5 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-26T01"}} |
| 1917 | 2026-09-26 00:37:30 | 595134d5 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 1918 | 2026-09-26 00:37:30 | 595134d5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite |
| 1919 | 2026-09-26 01:00:07 | 1a1d091d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1920 | 2026-09-26 01:00:07 | 268e463f |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-26T02"}} |
| 1921 | 2026-09-26 01:00:07 | 1a1d091d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1922 | 2026-09-26 01:12:13 | 463bbc9b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1923 | 2026-09-26 01:12:13 | 463bbc9b |  | audit.verified | fast-LAPTOP-LRE6PSA8 | {"rows": 1921, "hashed": 1169, "first_bad": null} |
| 1924 | 2026-09-26 01:12:13 | c632d578 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-09-27"}} |
| 1925 | 2026-09-26 01:12:13 | 6e64545f |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-09-26"}} |
| 1926 | 2026-09-26 01:12:13 | 15dcb4d1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-09-26"}} |
| 1927 | 2026-09-26 01:12:13 | 53c36786 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-09-26"}} |
| 1928 | 2026-09-26 01:12:13 | 463bbc9b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1929 | 2026-09-26 01:12:18 | 53c36786 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1930 | 2026-09-26 01:12:18 | bfe3fe75 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1931 | 2026-09-26 01:12:18 | a0acd66c | 002 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "002", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1932 | 2026-09-26 01:12:18 | f1597a23 | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "003", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1933 | 2026-09-26 01:12:18 | 59b0d294 | 004 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "004", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1934 | 2026-09-26 01:12:18 | 767f285f | 005 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "005", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1935 | 2026-09-26 01:12:18 | 6a700484 | 006 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "006", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1936 | 2026-09-26 01:12:18 | 5a54744d | 007 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "007", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1937 | 2026-09-26 01:12:18 | 6c7820ef | 008 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "008", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1938 | 2026-09-26 01:12:18 | 7ac8fd19 | 009 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "009", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1939 | 2026-09-26 01:12:18 | 0ec08f9d | 011 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "011", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1940 | 2026-09-26 01:12:18 | 98574231 | 012 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "012", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1941 | 2026-09-26 01:12:18 | 1c3d0592 | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "013", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1942 | 2026-09-26 01:12:18 | f0a5d1b8 | 014 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "014", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1943 | 2026-09-26 01:12:18 | efaa0786 | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "016", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1944 | 2026-09-26 01:12:18 | 16882d86 | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "017", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1945 | 2026-09-26 01:12:18 | 087596d0 | 018 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "018", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1946 | 2026-09-26 01:12:18 | 1f01caca | 019 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "019", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1947 | 2026-09-26 01:12:18 | a461a21a | 020 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "020", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1948 | 2026-09-26 01:12:18 | fb4da6e3 | 021 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "021", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1949 | 2026-09-26 01:12:18 | 73874f7b | 022 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "022", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1950 | 2026-09-26 01:12:18 | 1d115db4 | 023 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "023", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1951 | 2026-09-26 01:12:18 | 8d889942 | 024 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "024", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1952 | 2026-09-26 01:12:18 | 57ca83b6 | 025 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "025", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1953 | 2026-09-26 01:12:18 | bac2335f | 026 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "026", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1954 | 2026-09-26 01:12:18 | 53c36786 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "002", "003", "004", "005", "006", "007", "008", "009", "011", "012", "013", "014", "016", "017", "018", "019", "020", "021 |
| 1955 | 2026-09-26 01:12:18 | 53c36786 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1956 | 2026-09-26 01:12:21 | bfe3fe75 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1957 | 2026-09-26 01:12:22 | a0acd66c | 002 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1958 | 2026-09-26 01:13:09 | a0acd66c | 002 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] expect='SCOUT_OK' last='SCOUT_OK' \| T2 FAIL 23s [done] expect='0.3.5' last='\u00e2\u2020\u00b3 read \u00e2\u |
| 1959 | 2026-09-26 01:13:09 | a0acd66c | 002 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] expect='SCOUT_OK' last='SCOUT_OK' \| T2 FAIL 23s [done] expect='0.3.5' last='\u00e2\u2020\u00b3 read \u00e2\u |
| 1960 | 2026-09-26 01:13:09 | a0acd66c | 002 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1961 | 2026-09-26 01:13:09 | 0458f029 | 002 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "002", "max_rounds": 2}} |
| 1962 | 2026-09-26 01:13:09 | a0acd66c | 002 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "002", "status": "testing", "verified": "UNVERIFIED"}} |
| 1963 | 2026-09-26 01:13:14 | f1597a23 | 003 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1964 | 2026-09-26 01:14:20 | f1597a23 | 003 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='SMITH_OK' last='SMITH_OK' \| T2 FAIL 18s [done] expect='233168' last='\u00e2\u0153\u00bb Now run pyth |
| 1965 | 2026-09-26 01:14:20 | f1597a23 | 003 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='SMITH_OK' last='SMITH_OK' \| T2 FAIL 18s [done] expect='233168' last='\u00e2\u0153\u00bb Now run pyth |
| 1966 | 2026-09-26 01:14:20 | f1597a23 | 003 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1967 | 2026-09-26 01:14:20 | f3102263 | 003 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "003", "max_rounds": 2}} |
| 1968 | 2026-09-26 01:14:20 | f1597a23 | 003 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "status": "testing", "verified": "UNVERIFIED"}} |
| 1969 | 2026-09-26 01:14:24 | 59b0d294 | 004 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1970 | 2026-09-26 01:16:07 | bfe3fe75 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 22s [done] report expect='FACTORY' cmd=True \| T3 PASS 21s [d |
| 1971 | 2026-09-26 01:16:07 | bfe3fe75 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 22s [done] report expect='FACTORY' cmd=True \| T3 PASS 21s [d |
| 1972 | 2026-09-26 01:16:07 | bfe3fe75 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1973 | 2026-09-26 01:16:07 | 26dc19fc | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "bfe3fe75b6174004983684a9df120ba |
| 1974 | 2026-09-26 01:16:07 | bfe3fe75 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 1975 | 2026-09-26 01:16:11 | 0458f029 | 002 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1976 | 2026-09-26 01:16:13 | 59b0d294 | 004 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 26s [done] expect='CHANGELOG_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\004.json' \| T2 FAIL 26s [done] expec |
| 1977 | 2026-09-26 01:16:13 | 59b0d294 | 004 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 26s [done] expect='CHANGELOG_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\004.json' \| T2 FAIL 26s [done] expec |
| 1978 | 2026-09-26 01:16:13 | 59b0d294 | 004 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1979 | 2026-09-26 01:16:13 | f0215dbb | 004 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "004", "max_rounds": 2}} |
| 1980 | 2026-09-26 01:16:13 | 59b0d294 | 004 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "004", "status": "testing", "verified": "UNVERIFIED"}} |
| 1981 | 2026-09-26 01:16:18 | 767f285f | 005 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1982 | 2026-09-26 01:16:46 | 0458f029 | 002 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-120b", "sandbox": null, "rejected": ["fallback 'or-d |
| 1983 | 2026-09-26 01:16:46 | 0458f029 | 002 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 1984 | 2026-09-26 01:16:50 | f3102263 | 003 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1985 | 2026-09-26 01:19:22 | 767f285f | 005 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 76s [done] expect='1' last='RESULT: 1' \| T3 PASS 79s [done] expect='0'  |
| 1986 | 2026-09-26 01:19:22 | 767f285f | 005 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 76s [done] expect='1' last='RESULT: 1' \| T3 PASS 79s [done] expect='0'  |
| 1987 | 2026-09-26 01:19:22 | 767f285f | 005 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "005", "status": "active", "verified": "VERIFIED"}} |
| 1988 | 2026-09-26 01:19:25 | 6a700484 | 006 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1989 | 2026-09-26 01:21:40 | f3102263 | 003 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 1990 | 2026-09-26 01:21:40 | f3102263 | 003 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1991 | 2026-09-26 01:21:40 | f3102263 | 003 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "status": "active"}} |
| 1992 | 2026-09-26 01:21:43 | f0215dbb | 004 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1993 | 2026-09-26 01:23:52 | 6a700484 | 006 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 47s [done] expect='2' last='RESULT: 2' \| T3 PASS 83s [done] expect='0'  |
| 1994 | 2026-09-26 01:23:52 | 6a700484 | 006 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 47s [done] expect='2' last='RESULT: 2' \| T3 PASS 83s [done] expect='0'  |
| 1995 | 2026-09-26 01:23:52 | 6a700484 | 006 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "006", "status": "active", "verified": "VERIFIED"}} |
| 1996 | 2026-09-26 01:23:55 | 5a54744d | 007 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1997 | 2026-09-26 01:29:17 | f0215dbb | 004 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 1998 | 2026-09-26 01:29:17 | f0215dbb | 004 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1999 | 2026-09-26 01:29:17 | f0215dbb | 004 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "004", "status": "active"}} |
| 2000 | 2026-09-26 01:29:20 | 6c7820ef | 008 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2001 | 2026-09-26 01:30:26 | 5a54744d | 007 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 50s [done] expect='X_OK' last='X_OK' \| T2 PASS 148s [done] expect='2' last='RESULT: Extracted 2 TODO/FIXME items into t |
| 2002 | 2026-09-26 01:30:26 | 5a54744d | 007 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 50s [done] expect='X_OK' last='X_OK' \| T2 PASS 148s [done] expect='2' last='RESULT: Extracted 2 TODO/FIXME items into t |
| 2003 | 2026-09-26 01:30:26 | 5a54744d | 007 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "status": "active", "verified": "VERIFIED"}} |
| 2004 | 2026-09-26 01:30:29 | 7ac8fd19 | 009 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2005 | 2026-09-26 01:33:00 | 7ac8fd19 | 009 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 29s [done] expect='3' last='RESULT: Wrote lines.txt (5 lines), deduped t |
| 2006 | 2026-09-26 01:33:00 | 7ac8fd19 | 009 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 29s [done] expect='3' last='RESULT: Wrote lines.txt (5 lines), deduped t |
| 2007 | 2026-09-26 01:33:00 | 7ac8fd19 | 009 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "009", "status": "active", "verified": "VERIFIED"}} |
| 2008 | 2026-09-26 01:33:06 | 0ec08f9d | 011 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2009 | 2026-09-26 01:34:53 | 0ec08f9d | 011 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] expect='X_OK' last='X_OK' \| T2 PASS 38s [done] expect='2' last='2' \| T3 PASS 24s [done] expect='3' last='3' |
| 2010 | 2026-09-26 01:34:53 | 0ec08f9d | 011 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] expect='X_OK' last='X_OK' \| T2 PASS 38s [done] expect='2' last='2' \| T3 PASS 24s [done] expect='3' last='3' |
| 2011 | 2026-09-26 01:34:53 | 0ec08f9d | 011 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "011", "status": "active", "verified": "VERIFIED"}} |
| 2012 | 2026-09-26 01:34:57 | 98574231 | 012 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2013 | 2026-09-26 01:36:21 | 98574231 | 012 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] expect='X_OK' last='X_OK' \| T2 PASS 24s [done] expect='60' last='60' \| T3 PASS 21s [done] expect='22' last= |
| 2014 | 2026-09-26 01:36:21 | 98574231 | 012 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] expect='X_OK' last='X_OK' \| T2 PASS 24s [done] expect='60' last='60' \| T3 PASS 21s [done] expect='22' last= |
| 2015 | 2026-09-26 01:36:21 | 98574231 | 012 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "012", "status": "active", "verified": "VERIFIED"}} |
| 2016 | 2026-09-26 01:36:25 | 1c3d0592 | 013 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2017 | 2026-09-26 01:37:48 | 1c3d0592 | 013 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='X_OK' last='X_OK' \| T2 PASS 20s [done] expect='1' last='RESULT: 1' \| T3 PASS 29s [done] expect='0'  |
| 2018 | 2026-09-26 01:37:48 | 1c3d0592 | 013 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='X_OK' last='X_OK' \| T2 PASS 20s [done] expect='1' last='RESULT: 1' \| T3 PASS 29s [done] expect='0'  |
| 2019 | 2026-09-26 01:37:48 | 1c3d0592 | 013 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "013", "status": "active", "verified": "VERIFIED"}} |
| 2020 | 2026-09-26 01:37:52 | 476304a5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2021 | 2026-09-26 01:37:52 | afc49d7c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-26T02"}} |
| 2022 | 2026-09-26 01:38:40 | 6c7820ef | 008 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 52s [done] expect='X_OK' last='X_OK' \| T2 PASS 211s [done] expect='apple' last='RESULT: apple' \| T3 PASS 208s [done] e |
| 2023 | 2026-09-26 01:38:40 | 6c7820ef | 008 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 52s [done] expect='X_OK' last='X_OK' \| T2 PASS 211s [done] expect='apple' last='RESULT: apple' \| T3 PASS 208s [done] e |
| 2024 | 2026-09-26 01:38:40 | 6c7820ef | 008 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "008", "status": "active", "verified": "VERIFIED"}} |
