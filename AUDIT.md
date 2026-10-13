# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 6981 | 2026-10-11 06:06:46 | abdda5ab | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6982 | 2026-10-11 06:06:49 | db0fe640 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6983 | 2026-10-11 06:19:24 | db0fe640 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 54s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6984 | 2026-10-11 06:19:24 | db0fe640 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 54s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6985 | 2026-10-11 06:19:24 | d597bd29 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "c6d15792faef4854ae2126211a52cb62", "after_quota": "db0fe640f2f4410ca93434f428a96 |
| 6986 | 2026-10-11 06:19:24 | db0fe640 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6987 | 2026-10-11 06:19:25 | 0689a1f2 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6988 | 2026-10-11 06:31:12 | 0689a1f2 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 6989 | 2026-10-11 06:31:12 | 0689a1f2 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 6990 | 2026-10-11 06:31:12 | 08a97ba0 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "062a8aeee53a43b2acb9a934d07fbf4b", "after_quota": "0689a1f287b1456583e2bf1d853f8 |
| 6991 | 2026-10-11 06:31:12 | 0689a1f2 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6992 | 2026-10-11 06:31:13 | 7241e219 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6993 | 2026-10-11 06:42:53 | 7241e219 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 6994 | 2026-10-11 06:42:53 | 7241e219 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 6995 | 2026-10-11 06:42:53 | 3b8aaf5c | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "139734ae344e49089147d3f47942ffc6", "after_quota": "7241e219a0dc41c0ba818b06bb7e3 |
| 6996 | 2026-10-11 06:42:53 | 7241e219 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6997 | 2026-10-11 06:42:56 | f3e3352b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6998 | 2026-10-11 06:54:12 | f3e3352b | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 54s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6999 | 2026-10-11 06:54:12 | f3e3352b | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 54s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 7000 | 2026-10-11 06:54:12 | 67f6eb9c | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "41923cc5baaa4b7ba7c14909b7abe137", "after_quota": "f3e3352b2ca8475899186e997f8b6 |
| 7001 | 2026-10-11 06:54:12 | f3e3352b | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7002 | 2026-10-11 06:54:12 | ad05ad78 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7003 | 2026-10-11 06:55:21 | b33c79d0 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7004 | 2026-10-11 06:55:21 | 7ff3e852 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-11T07"}} |
| 7005 | 2026-10-11 06:55:31 | b33c79d0 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss1 |
| 7006 | 2026-10-11 06:56:19 | 8cb8eb01 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7007 | 2026-10-11 06:56:19 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7008 | 2026-10-11 06:56:19 | b217065b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-11T07"}} |
| 7009 | 2026-10-11 06:56:19 | 8cb8eb01 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7010 | 2026-10-11 07:06:53 | ad05ad78 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 70s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 7011 | 2026-10-11 07:06:53 | ad05ad78 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 70s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 7012 | 2026-10-11 07:06:53 | 4563587c | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ad05ad784cb643aea91e5a42f9c1b9f8", "after_quota": "ad05ad784cb643aea91e5a42f9c1b |
| 7013 | 2026-10-11 07:06:53 | ad05ad78 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7014 | 2026-10-11 07:06:54 | a35c8dd3 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7015 | 2026-10-11 07:18:41 | a35c8dd3 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 7016 | 2026-10-11 07:18:41 | a35c8dd3 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 7017 | 2026-10-11 07:18:41 | 03bf5015 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "a35c8dd3257c45229ac4b0d597896 |
| 7018 | 2026-10-11 07:18:41 | a35c8dd3 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7019 | 2026-10-11 07:18:43 | ec79f13c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7020 | 2026-10-11 07:30:29 | ec79f13c | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 76s [d |
| 7021 | 2026-10-11 07:30:29 | ec79f13c | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 76s [d |
| 7022 | 2026-10-11 07:30:29 | dcd599f1 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fe371a05201e499c9cc16d620128e678", "after_quota": "ec79f13c9e22450fb101cf746e159 |
| 7023 | 2026-10-11 07:30:29 | ec79f13c | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7024 | 2026-10-11 07:30:31 | 26da8c48 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7025 | 2026-10-11 07:44:16 | 26da8c48 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 54s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 127s [ |
| 7026 | 2026-10-11 07:44:16 | 26da8c48 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 54s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 127s [ |
| 7027 | 2026-10-11 07:44:16 | ea36c3ba | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "b55e8b342b7b4b37acedb240a933539f", "after_quota": "26da8c485ccd4c37a7027027412e4 |
| 7028 | 2026-10-11 07:44:16 | 26da8c48 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7029 | 2026-10-11 07:44:19 | adaf4c56 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7030 | 2026-10-11 07:55:25 | 7ff3e852 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7031 | 2026-10-11 07:55:25 | bc73aaf4 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-11T08"}} |
| 7032 | 2026-10-11 07:55:43 | 7ff3e852 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 7033 | 2026-10-11 07:55:43 | 7ff3e852 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gem |
| 7034 | 2026-10-11 07:56:22 | b217065b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7035 | 2026-10-11 07:56:22 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7036 | 2026-10-11 07:56:22 | b2f3be5b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-11T08"}} |
| 7037 | 2026-10-11 07:56:22 | b217065b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7038 | 2026-10-11 07:56:24 | adaf4c56 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 7039 | 2026-10-11 07:56:24 | adaf4c56 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 7040 | 2026-10-11 07:56:24 | 2849fd50 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5fd9d18c4aa1414aafe3e0fba01dde29", "after_quota": "adaf4c56d4db43b39d55e9cdaa5d3 |
| 7041 | 2026-10-11 07:56:24 | adaf4c56 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7042 | 2026-10-11 07:56:25 | df7e22b9 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7043 | 2026-10-11 08:09:02 | df7e22b9 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 86s [done] report expect='FACTORY' cmd=True \| T3 PASS 64s [d |
| 7044 | 2026-10-11 08:09:02 | df7e22b9 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 86s [done] report expect='FACTORY' cmd=True \| T3 PASS 64s [d |
| 7045 | 2026-10-11 08:09:02 | 8b0f8a09 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "9aa0054ee0124b40bb21b2daef2bc049", "after_quota": "df7e22b9f06f4c81b20c94adcf1f8 |
| 7046 | 2026-10-11 08:09:02 | df7e22b9 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7047 | 2026-10-11 08:09:03 | 99b7c926 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7048 | 2026-10-11 08:20:30 | 99b7c926 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 24s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 7049 | 2026-10-11 08:20:31 | 99b7c926 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 24s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 7050 | 2026-10-11 08:20:31 | f8ad7e5a | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "99b7c92662884eb6bbfad3f6b0630 |
| 7051 | 2026-10-11 08:20:31 | 99b7c926 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7052 | 2026-10-11 08:20:32 | 4c91245e | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7053 | 2026-10-11 08:32:45 | 4c91245e | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 7054 | 2026-10-11 08:32:45 | 4c91245e | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 7055 | 2026-10-11 08:32:45 | 4b9aabd5 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a5c9b2241151489ea85e56994e87fa75", "after_quota": "4c91245ef1eb421193f364b993c94 |
| 7056 | 2026-10-11 08:32:45 | 4c91245e | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7057 | 2026-10-11 08:32:49 | d597bd29 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7058 | 2026-10-11 08:44:44 | d597bd29 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 7059 | 2026-10-11 08:44:44 | d597bd29 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 7060 | 2026-10-11 08:44:44 | 16d3872d | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "c6d15792faef4854ae2126211a52cb62", "after_quota": "d597bd29e11b40c6ba75d1e50969d |
| 7061 | 2026-10-11 08:44:44 | d597bd29 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7062 | 2026-10-11 08:44:46 | 08a97ba0 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7063 | 2026-10-11 08:55:29 | bc73aaf4 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7064 | 2026-10-11 08:55:29 | d3e98568 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-11T09"}} |
| 7065 | 2026-10-11 08:56:04 | bc73aaf4 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemi |
| 7066 | 2026-10-11 08:56:23 | b2f3be5b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7067 | 2026-10-11 08:56:23 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7068 | 2026-10-11 08:56:23 | 959cea0b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-11T09"}} |
| 7069 | 2026-10-11 08:56:23 | b2f3be5b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7070 | 2026-10-11 08:58:38 | 08a97ba0 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 117s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 62s [done] report expect='FACTORY' cmd=True \| T3 PASS 76s [ |
| 7071 | 2026-10-11 08:58:38 | 08a97ba0 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 117s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 62s [done] report expect='FACTORY' cmd=True \| T3 PASS 76s [ |
| 7072 | 2026-10-11 08:58:38 | b232befe | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "062a8aeee53a43b2acb9a934d07fbf4b", "after_quota": "08a97ba0442e45998f7957477af29 |
| 7073 | 2026-10-11 08:58:38 | 08a97ba0 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7074 | 2026-10-11 08:58:42 | 3b8aaf5c | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7075 | 2026-10-11 09:11:14 | 3b8aaf5c | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 62s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 7076 | 2026-10-11 09:11:14 | 3b8aaf5c | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 62s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 7077 | 2026-10-11 09:11:14 | 2fe7d6b0 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "139734ae344e49089147d3f47942ffc6", "after_quota": "3b8aaf5c8f034b44b28fecf6c5219 |
| 7078 | 2026-10-11 09:11:14 | 3b8aaf5c | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7079 | 2026-10-11 09:11:14 | 67f6eb9c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7080 | 2026-10-11 09:23:44 | 67f6eb9c | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 64s [done] report expect='FACTORY' cmd=True \| T3 FAIL 48s [d |
| 7081 | 2026-10-11 09:23:44 | 67f6eb9c | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 64s [done] report expect='FACTORY' cmd=True \| T3 FAIL 48s [d |
| 7082 | 2026-10-11 09:23:44 | 67f6eb9c | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7083 | 2026-10-11 09:23:44 | 46dd4d1a | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "retry_of": "67f6eb9c587d488eb84912e41ff781a |
| 7084 | 2026-10-11 09:23:44 | 67f6eb9c | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7085 | 2026-10-11 09:23:45 | 4563587c | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7086 | 2026-10-11 14:42:19 | 4563587c |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 7087 | 2026-10-11 14:42:19 | d3e98568 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7088 | 2026-10-11 14:42:25 | d66ccc47 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-11T15"}} |
| 7089 | 2026-10-11 14:42:56 | 4563587c |  | job.readopted | svc-LAPTOP-LRE6PSA8 | {} |
| 7090 | 2026-10-11 14:43:34 | d3e98568 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemi |
| 7091 | 2026-10-11 14:43:49 | 959cea0b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7092 | 2026-10-11 14:43:49 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7093 | 2026-10-11 14:43:52 | 10c6da9c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-11T15"}} |
| 7094 | 2026-10-11 14:43:52 | 959cea0b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7095 | 2026-10-11 14:44:28 | 4563587c | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7096 | 2026-10-11 14:44:31 | 46dd4d1a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7097 | 2026-10-11 15:05:08 | 46dd4d1a |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 7098 | 2026-10-11 15:05:08 | 46dd4d1a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 7099 | 2026-10-11 16:21:15 | 46dd4d1a |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 7100 | 2026-10-11 16:21:15 | d66ccc47 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7101 | 2026-10-11 16:21:54 | 0b1124ec |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-11T17"}} |
| 7102 | 2026-10-11 16:22:27 | 46dd4d1a |  | job.readopted | fast-LAPTOP-LRE6PSA8 | {} |
| 7103 | 2026-10-11 16:22:45 | d66ccc47 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptos |
| 7104 | 2026-10-11 16:22:58 | 10c6da9c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7105 | 2026-10-11 16:22:58 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7106 | 2026-10-11 16:22:59 | b7f9b8eb |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-11T17"}} |
| 7107 | 2026-10-11 16:22:59 | 10c6da9c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7108 | 2026-10-11 16:36:58 | 46dd4d1a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 34s [done] report expect='FACTORY' cmd=True \| T3 PASS 121s [ |
| 7109 | 2026-10-11 16:36:58 | 46dd4d1a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 34s [done] report expect='FACTORY' cmd=True \| T3 PASS 121s [ |
| 7110 | 2026-10-11 16:36:58 | ac1a9ae3 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "46dd4d1a1e3b4c8e89ec1cfb1453caa1", "after_quota": "46dd4d1a1e3b4c8e89ec1cfb1453c |
| 7111 | 2026-10-11 16:36:58 | 46dd4d1a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7112 | 2026-10-11 16:36:59 | 4563587c | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 7113 | 2026-10-11 16:51:34 | 4563587c | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 7114 | 2026-10-11 16:51:34 | 4563587c | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 7115 | 2026-10-11 16:51:34 | 583bff99 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ad05ad784cb643aea91e5a42f9c1b9f8", "after_quota": "4563587cb90d4949a5f5a77a93346 |
| 7116 | 2026-10-11 16:51:34 | 4563587c | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7117 | 2026-10-11 16:51:38 | 03bf5015 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7118 | 2026-10-11 17:02:59 | 03bf5015 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 7119 | 2026-10-11 17:02:59 | 03bf5015 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 7120 | 2026-10-11 17:02:59 | 1a2b86df | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "03bf501590e346f4a5930f4901d73 |
| 7121 | 2026-10-11 17:02:59 | 03bf5015 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7122 | 2026-10-11 17:03:04 | dcd599f1 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7123 | 2026-10-11 17:14:30 | dcd599f1 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 7124 | 2026-10-11 17:14:30 | dcd599f1 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 7125 | 2026-10-11 17:14:30 | 0594097a | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fe371a05201e499c9cc16d620128e678", "after_quota": "dcd599f1b44a497bbe3d37042ae45 |
| 7126 | 2026-10-11 17:14:30 | dcd599f1 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7127 | 2026-10-11 17:14:34 | ea36c3ba | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7128 | 2026-10-11 17:21:55 | 0b1124ec |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7129 | 2026-10-11 17:21:55 | a0e8ce38 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-11T18"}} |
| 7130 | 2026-10-11 17:22:14 | 0b1124ec |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gem |
| 7131 | 2026-10-11 17:23:02 | b7f9b8eb |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7132 | 2026-10-11 17:23:03 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7133 | 2026-10-11 17:23:03 | 8d25635b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-11T18"}} |
| 7134 | 2026-10-11 17:23:03 | b7f9b8eb |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7135 | 2026-10-11 17:25:31 | ea36c3ba | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 54s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 7136 | 2026-10-11 17:25:31 | ea36c3ba | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 54s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 7137 | 2026-10-11 17:25:31 | 7731f537 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "b55e8b342b7b4b37acedb240a933539f", "after_quota": "ea36c3ba63dd462e83fb917f85da0 |
| 7138 | 2026-10-11 17:25:31 | ea36c3ba | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7139 | 2026-10-11 17:25:32 | 2849fd50 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7140 | 2026-10-11 17:36:54 | 2849fd50 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 7141 | 2026-10-11 17:36:54 | 2849fd50 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 7142 | 2026-10-11 17:36:54 | cef764b9 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5fd9d18c4aa1414aafe3e0fba01dde29", "after_quota": "2849fd5074c147a1bdb7b493ab7e2 |
| 7143 | 2026-10-11 17:36:54 | 2849fd50 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7144 | 2026-10-11 17:36:55 | 8b0f8a09 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7145 | 2026-10-11 17:48:47 | 8b0f8a09 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 7146 | 2026-10-11 17:48:47 | 8b0f8a09 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 7147 | 2026-10-11 17:48:47 | 54ed109a | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "9aa0054ee0124b40bb21b2daef2bc049", "after_quota": "8b0f8a0989bd4b7d858fb07297f66 |
| 7148 | 2026-10-11 17:48:47 | 8b0f8a09 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7149 | 2026-10-11 17:48:48 | f8ad7e5a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7150 | 2026-10-11 18:00:01 | f8ad7e5a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 47s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 7151 | 2026-10-11 18:00:01 | f8ad7e5a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 47s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 7152 | 2026-10-11 18:00:01 | 84bb3b09 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "f8ad7e5a27eb4524906e60287ccd2 |
| 7153 | 2026-10-11 18:00:01 | f8ad7e5a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7154 | 2026-10-11 18:00:03 | 4b9aabd5 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7155 | 2026-10-11 18:11:42 | 4b9aabd5 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 56s [d |
| 7156 | 2026-10-11 18:11:42 | 4b9aabd5 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 56s [d |
| 7157 | 2026-10-11 18:11:42 | d5c437bd | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a5c9b2241151489ea85e56994e87fa75", "after_quota": "4b9aabd5004f4499a780f240b8eb4 |
| 7158 | 2026-10-11 18:11:42 | 4b9aabd5 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7159 | 2026-10-11 18:11:45 | 16d3872d | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7160 | 2026-10-11 18:21:57 | a0e8ce38 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7161 | 2026-10-11 18:21:57 | 915fcf67 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-11T19"}} |
| 7162 | 2026-10-11 18:22:52 | a0e8ce38 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemi |
| 7163 | 2026-10-11 18:23:05 | 8d25635b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7164 | 2026-10-11 18:23:05 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7165 | 2026-10-11 18:23:06 | 96c57061 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-11T19"}} |
| 7166 | 2026-10-11 18:23:06 | 8d25635b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7167 | 2026-10-11 18:23:42 | 16d3872d | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 76s [d |
| 7168 | 2026-10-11 18:23:42 | 16d3872d | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 76s [d |
| 7169 | 2026-10-11 18:23:42 | edafcea5 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "c6d15792faef4854ae2126211a52cb62", "after_quota": "16d3872d175f46ccb08a1b623aee5 |
| 7170 | 2026-10-11 18:23:42 | 16d3872d | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7171 | 2026-10-11 18:23:45 | b232befe | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7172 | 2026-10-11 18:36:38 | b232befe | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 82s [d |
| 7173 | 2026-10-11 18:36:38 | b232befe | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 82s [d |
| 7174 | 2026-10-11 18:36:38 | 5524de8c | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "062a8aeee53a43b2acb9a934d07fbf4b", "after_quota": "b232befeb5ce4130851904988eedd |
| 7175 | 2026-10-11 18:36:38 | b232befe | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7176 | 2026-10-11 18:36:41 | 2fe7d6b0 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7177 | 2026-10-11 18:50:29 | 2fe7d6b0 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 50s [done] report expect='FACTORY' cmd=False \| T3 PASS 132s  |
| 7178 | 2026-10-11 18:50:29 | 2fe7d6b0 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 50s [done] report expect='FACTORY' cmd=False \| T3 PASS 132s  |
| 7179 | 2026-10-11 18:50:29 | 2fe7d6b0 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7180 | 2026-10-11 18:50:29 | 58e2c099 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "2fe7d6b08e8d48fdb38eea10a85ffe3 |
| 7181 | 2026-10-11 18:50:29 | 2fe7d6b0 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7182 | 2026-10-11 18:50:32 | ac1a9ae3 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7183 | 2026-10-11 19:02:50 | ac1a9ae3 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 7184 | 2026-10-11 19:02:50 | ac1a9ae3 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 7185 | 2026-10-11 19:02:50 | 93fc5c42 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "46dd4d1a1e3b4c8e89ec1cfb1453caa1", "after_quota": "ac1a9ae379f345c5bd9ed6431a783 |
| 7186 | 2026-10-11 19:02:50 | ac1a9ae3 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7187 | 2026-10-11 19:02:54 | 583bff99 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7188 | 2026-10-11 19:14:30 | 583bff99 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 7189 | 2026-10-11 19:14:30 | 583bff99 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 7190 | 2026-10-11 19:14:30 | 1523484a | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ad05ad784cb643aea91e5a42f9c1b9f8", "after_quota": "583bff994e0742a1916d69db3df67 |
| 7191 | 2026-10-11 19:14:30 | 583bff99 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7192 | 2026-10-11 19:14:35 | 1a2b86df | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7193 | 2026-10-11 19:22:00 | 915fcf67 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7194 | 2026-10-11 19:22:00 | e13dee01 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-11T20"}} |
| 7195 | 2026-10-11 19:23:17 | 915fcf67 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 7196 | 2026-10-11 19:23:20 | 96c57061 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7197 | 2026-10-11 19:23:20 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7198 | 2026-10-11 19:23:21 | 68b63fd1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-11T20"}} |
| 7199 | 2026-10-11 19:23:21 | 96c57061 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7200 | 2026-10-11 19:25:23 | 1a2b86df | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [do |
| 7201 | 2026-10-11 19:25:23 | 1a2b86df | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [do |
| 7202 | 2026-10-11 19:25:23 | 888a5269 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "1a2b86dfcc70401e9c47635b66d27 |
| 7203 | 2026-10-11 19:25:23 | 1a2b86df | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7204 | 2026-10-11 19:25:25 | 58e2c099 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7205 | 2026-10-11 19:36:14 | 58e2c099 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 7206 | 2026-10-11 19:36:14 | 58e2c099 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 7207 | 2026-10-11 19:36:14 | 58e2c099 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7208 | 2026-10-11 19:36:14 | 5e3cb81d | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "58e2c0991f4b4fbf92ad0cb7553631c |
| 7209 | 2026-10-11 19:36:14 | 58e2c099 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7210 | 2026-10-11 19:36:18 | 0594097a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7211 | 2026-10-11 19:48:45 | 0594097a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 70s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 57s [d |
| 7212 | 2026-10-11 19:48:45 | 0594097a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 70s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 57s [d |
| 7213 | 2026-10-11 19:48:45 | b8338b41 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fe371a05201e499c9cc16d620128e678", "after_quota": "0594097a83ad426a9e27b483c1d96 |
| 7214 | 2026-10-11 19:48:45 | 0594097a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7215 | 2026-10-11 19:48:50 | 7731f537 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7216 | 2026-10-11 20:01:27 | 7731f537 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 42s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 7217 | 2026-10-11 20:01:27 | 7731f537 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 42s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 7218 | 2026-10-11 20:01:27 | a6414b9b | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "b55e8b342b7b4b37acedb240a933539f", "after_quota": "7731f53713a14324b402fe0416017 |
| 7219 | 2026-10-11 20:01:27 | 7731f537 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7220 | 2026-10-11 20:01:31 | cef764b9 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7221 | 2026-10-11 20:48:04 | cef764b9 |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 7222 | 2026-10-11 20:48:04 | e13dee01 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7223 | 2026-10-11 20:48:05 | 56cb34df |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-11T21"}} |
| 7224 | 2026-10-13 00:03:55 | cef764b9 |  | job.readopted | svc-LAPTOP-LRE6PSA8 | {} |
| 7225 | 2026-10-13 00:04:22 | e13dee01 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local4b", "or-apodex-11-mini", "or-nemotron-35-lightning"], " |
| 7226 | 2026-10-13 00:04:34 | 68b63fd1 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7227 | 2026-10-13 00:04:34 | 38a82f20 | 031 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "run", "payload": {"bot_id": "031", "task": "Perform weekly self-review and count how many bots were created", "in": null, "out": n |
| 7228 | 2026-10-13 00:04:35 |  | 031 | schedule.fired | fast-LAPTOP-LRE6PSA8 | {"sid": "4c980140", "fire": "2026-10-12T07:00", "job": "38a82f20"} |
| 7229 | 2026-10-13 00:04:35 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7230 | 2026-10-13 00:04:37 | 5700db87 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-13T01"}} |
| 7231 | 2026-10-13 00:04:38 | 68b63fd1 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7232 | 2026-10-13 00:04:44 | 56cb34df |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7233 | 2026-10-13 00:04:44 | 48445198 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-13T01"}} |
| 7234 | 2026-10-13 00:04:52 | 93c7b416 |  | job.enqueued | nightly-task | {"kind": "monitor", "payload": {"only": null, "day": "2026-10-13"}} |
| 7235 | 2026-10-13 00:06:19 | 56cb34df |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "TimeoutError"} |
| 7236 | 2026-10-13 00:06:19 | 56cb34df |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "TimeoutError"} |
| 7237 | 2026-10-13 00:06:19 | 56cb34df |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 7238 | 2026-10-13 00:06:19 | 56cb34df |  | model.retired | fast-LAPTOP-LRE6PSA8 | {"model": "or-ling-30-flash-sante", "reason": "gone: {\"error\":{\"message\":\"this model is unavailable for free. the paid version "} |
| 7239 | 2026-10-13 00:06:19 | 23f004fa |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-13", "trigger": "blocked:gemini-flash,gemini-flash-latest,gemini-flash3 |
| 7240 | 2026-10-13 00:06:19 | 848c22cd |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-13", "trigger": "blocked:gemini-flash,gemini-flash-latest,gemini-flas |
| 7241 | 2026-10-13 00:06:19 | 96a4497b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-13", "trigger": "blocked:gemini-flash,gemini-flash-latest,gemini- |
| 7242 | 2026-10-13 00:06:19 | 9b61a867 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-13", "trigger": "blocked:gemini-flash,gemini-flash-latest,gemini-fl |
| 7243 | 2026-10-13 00:06:19 | edae1f0a |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-13", "trigger": "blocked:gemini-flash,gemini-flash-latest,gemini-flas |
| 7244 | 2026-10-13 00:06:19 | 2510d211 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-13", "trigger": "blocked:gemini-flash,gemini-flash-latest,gemini-fla |
| 7245 | 2026-10-13 00:06:19 | 56cb34df |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gpto |
| 7246 | 2026-10-13 00:06:22 | 23f004fa |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7247 | 2026-10-13 00:06:23 | 23f004fa |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7248 | 2026-10-13 00:06:25 | 848c22cd |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7249 | 2026-10-13 00:06:25 | 848c22cd |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7250 | 2026-10-13 00:06:28 | 96a4497b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7251 | 2026-10-13 00:07:13 | 96a4497b |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "dots-studio/dots-3-note-preview:free", "reason": "loop: final answer ''", "provider": "openrouter"} |
| 7252 | 2026-10-13 00:07:13 | 96a4497b |  | lane.discovered | fast-LAPTOP-LRE6PSA8 | {"model": "liquid/lfm-2.5-2.6b:free", "reason": "probe 0.92s loop 1.39s", "provider": "openrouter"} |
| 7253 | 2026-10-13 00:07:13 | 96a4497b |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "poolside/laguna-s-2.1:free", "reason": "loop: did not call add", "provider": "openrouter"} |
| 7254 | 2026-10-13 00:07:13 | 96a4497b |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "thinkingmachines/inkling:free", "reason": "probe auth: {\"error\":{\"message\":\"thinkingmachines/inkling:free is only available  |
| 7255 | 2026-10-13 00:07:13 | 96a4497b |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "poolside/laguna-xs-2.1:free", "reason": "loop: HTTP 429 {\"error\":{\"message\":\"Provider returned error\",\"code\":429,\"metada |
| 7256 | 2026-10-13 00:07:13 | 96a4497b |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "cohere/north-mini-code:free", "reason": "probe no_tool_call: ", "provider": "openrouter"} |
| 7257 | 2026-10-13 00:07:13 | 96a4497b |  | lane.discovered | fast-LAPTOP-LRE6PSA8 | {"model": "nvidia/nemotron-3-ultra-550b-a55b:free", "reason": "probe 4.95s loop 24.78s", "provider": "openrouter"} |
| 7258 | 2026-10-13 00:07:13 | 96a4497b |  | config.presets | fast-LAPTOP-LRE6PSA8 | {"added": ["or-lfm-25-26b", "or-nemotron-3-ultra-550b-a55b"]} |
| 7259 | 2026-10-13 00:07:13 | aeec9e45 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"lanes": ["or-lfm-25-26b", "or-nemotron-3-ultra-550b-a55b"], "day": "2026-10-13"}} |
| 7260 | 2026-10-13 00:07:13 | 96a4497b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": ["or-lfm-25-26b", "or-nemotron-3-ultra-550b-a55b"]}} |
| 7261 | 2026-10-13 00:07:16 | 9b61a867 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7262 | 2026-10-13 00:07:16 | 9b61a867 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7263 | 2026-10-13 00:07:18 | edae1f0a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7264 | 2026-10-13 00:07:18 | edae1f0a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7265 | 2026-10-13 00:07:21 | 2510d211 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7266 | 2026-10-13 00:07:21 | 2510d211 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7267 | 2026-10-13 00:07:24 | 38a82f20 | 031 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7268 | 2026-10-13 00:07:33 | 38a82f20 | 031 | bot.ran | fast-LAPTOP-LRE6PSA8 | {"ok": true, "produced": ["bots.log"], "secs": 9, "reply": "RESULT: 0", "chain": "gemini-gemini-flash-lite-latest"} |
| 7269 | 2026-10-13 00:07:33 | 38a82f20 | 031 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "031", "name": "run", "status": "ok bots.log"}} |
| 7270 | 2026-10-13 00:07:36 | b3cfc47e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7271 | 2026-10-13 00:07:36 | b3cfc47e |  | audit.verified | fast-LAPTOP-LRE6PSA8 | {"rows": 7269, "hashed": 6517, "first_bad": null} |
| 7272 | 2026-10-13 00:07:36 | 55933f61 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-10-14"}} |
| 7273 | 2026-10-13 00:07:36 | 408aa9ea |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-10-13"}} |
| 7274 | 2026-10-13 00:07:36 | 0c642780 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-10-13"}} |
| 7275 | 2026-10-13 00:07:36 | b3cfc47e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7276 | 2026-10-13 00:16:21 | cef764b9 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7277 | 2026-10-13 00:16:24 | 5e3cb81d | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7278 | 2026-10-13 00:28:13 | 5e3cb81d | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 20s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 23s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 7279 | 2026-10-13 00:28:13 | 5e3cb81d | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 20s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 23s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 7280 | 2026-10-13 00:28:13 | 35fdd956 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5e3cb81dcaef415aa193471d2cd92af9", "after_quota": "5e3cb81dcaef415aa193471d2cd92 |
| 7281 | 2026-10-13 00:28:13 | 5e3cb81d | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7282 | 2026-10-13 00:28:15 | cef764b9 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 7283 | 2026-10-13 00:28:15 | 93c7b416 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7284 | 2026-10-13 00:28:15 | f9b10c1e | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "93c7b41641d741fd9f8715d1023433fe", "day": "2026-10-13"}} |
| 7285 | 2026-10-13 00:28:15 | ef10c05d | 031 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "031", "monitor_of": "93c7b41641d741fd9f8715d1023433fe", "day": "2026-10-13"}} |
| 7286 | 2026-10-13 00:28:15 | 93c7b416 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "031"], "jobs": ["f9b10c1e", "ef10c05d"]} |
| 7287 | 2026-10-13 00:28:15 | 93c7b416 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7288 | 2026-10-13 00:28:18 | aeec9e45 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7289 | 2026-10-13 00:31:08 | aeec9e45 |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "or-lfm-25-26b", "result": "3/4", "quota": 0, "secs": 31} |
| 7290 | 2026-10-13 00:31:08 | aeec9e45 |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "or-nemotron-3-ultra-550b-a55b", "result": "4/4", "quota": 0, "secs": 62} |
| 7291 | 2026-10-13 00:31:08 | aeec9e45 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["or-lfm-25-26b", "3/4"], ["or-nemotron-3-ultra-550b-a55b", "4/4"]]}} |
| 7292 | 2026-10-13 00:31:11 | ef10c05d | 031 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7293 | 2026-10-13 00:31:43 | ef10c05d | 031 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 7s [done] expect='X_OK' last='X_OK' \| T2 PASS 8s [done] expect='3' last='RESULT: 3' \| T3 PASS 8s [done] expect='2' las |
| 7294 | 2026-10-13 00:31:43 | ef10c05d | 031 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 7s [done] expect='X_OK' last='X_OK' \| T2 PASS 8s [done] expect='3' last='RESULT: 3' \| T3 PASS 8s [done] expect='2' las |
| 7295 | 2026-10-13 00:31:43 | ef10c05d | 031 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "031", "status": "active", "verified": "VERIFIED"}} |
| 7296 | 2026-10-13 00:31:45 | 408aa9ea |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7297 | 2026-10-13 00:32:35 | 408aa9ea |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "or-nemotron-35-lightning", "result": "0/4", "quota": 3, "secs": 49} |
| 7298 | 2026-10-13 00:32:35 | 408aa9ea |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["or-nemotron-35-lightning", "0/4 q3"]]}} |
| 7299 | 2026-10-13 00:32:38 | 0c642780 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7300 | 2026-10-13 00:32:41 | 0c642780 |  | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "security", "next_state": "paused", "attempt": 1, "error": "FactoryError: could not produce a valid spec after 3 attempts: |
| 7301 | 2026-10-13 00:41:50 | cef764b9 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 7s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 37s [done] report expect='FACTORY' cmd=True \| T3 PASS 53s [do |
| 7302 | 2026-10-13 00:41:50 | cef764b9 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 7s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 37s [done] report expect='FACTORY' cmd=True \| T3 PASS 53s [do |
| 7303 | 2026-10-13 00:41:50 | f876d821 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5fd9d18c4aa1414aafe3e0fba01dde29", "after_quota": "cef764b9ad334d26b799e1eef0992 |
| 7304 | 2026-10-13 00:41:50 | cef764b9 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7305 | 2026-10-13 00:41:53 | 54ed109a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7306 | 2026-10-13 00:54:55 | 54ed109a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 70s [done] report expect='FACTORY' cmd=True \| T3 PASS 77s [d |
| 7307 | 2026-10-13 00:54:55 | 54ed109a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 70s [done] report expect='FACTORY' cmd=True \| T3 PASS 77s [d |
| 7308 | 2026-10-13 00:54:55 | 54ed109a | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7309 | 2026-10-13 00:54:55 | edc88e8d | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "54ed109aed494a8ba4c564e9ed91816 |
| 7310 | 2026-10-13 00:54:55 | 54ed109a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7311 | 2026-10-13 00:54:57 | 84bb3b09 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7312 | 2026-10-13 01:04:39 | 5700db87 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7313 | 2026-10-13 01:04:40 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7314 | 2026-10-13 01:04:40 | 4e2eedaf |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-13T02"}} |
| 7315 | 2026-10-13 01:04:40 | 5700db87 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7316 | 2026-10-13 01:04:48 | 48445198 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7317 | 2026-10-13 01:04:48 | 9641e7c2 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-13T02"}} |
| 7318 | 2026-10-13 01:05:45 | 48445198 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 7319 | 2026-10-13 01:05:45 | 48445198 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash38", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\ |
| 7320 | 2026-10-13 01:05:45 | 1a8fb940 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-13", "trigger": "blocked:gemini-flash38"}} |
| 7321 | 2026-10-13 01:05:45 | 9b803416 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-13", "trigger": "blocked:gemini-flash38"}} |
| 7322 | 2026-10-13 01:05:45 | b7bd0932 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-13", "trigger": "blocked:gemini-flash38"}} |
| 7323 | 2026-10-13 01:05:45 | c1ee42b2 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-13", "trigger": "blocked:gemini-flash38"}} |
| 7324 | 2026-10-13 01:05:45 | b0781bd8 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-13", "trigger": "blocked:gemini-flash38"}} |
| 7325 | 2026-10-13 01:05:45 | ebab5a2a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-13", "trigger": "blocked:gemini-flash38"}} |
| 7326 | 2026-10-13 01:05:45 | 48445198 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash-latest", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq- |
| 7327 | 2026-10-13 01:05:48 | 1a8fb940 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7328 | 2026-10-13 01:05:48 | 1a8fb940 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7329 | 2026-10-13 01:05:51 | 9b803416 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7330 | 2026-10-13 01:05:51 | 9b803416 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7331 | 2026-10-13 01:05:54 | b7bd0932 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7332 | 2026-10-13 01:06:06 | b7bd0932 |  | lane.rejected | svc-LAPTOP-LRE6PSA8 | {"model": "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free", "reason": "loop: KeyError", "provider": "openrouter"} |
| 7333 | 2026-10-13 01:06:06 | b7bd0932 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7334 | 2026-10-13 01:06:10 | c1ee42b2 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7335 | 2026-10-13 01:06:10 | c1ee42b2 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7336 | 2026-10-13 01:06:12 | b0781bd8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7337 | 2026-10-13 01:06:12 | b0781bd8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7338 | 2026-10-13 01:06:15 | ebab5a2a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7339 | 2026-10-13 01:06:15 | ebab5a2a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7340 | 2026-10-13 01:11:54 | 84bb3b09 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 70s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 7341 | 2026-10-13 01:11:54 | 84bb3b09 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 70s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 7342 | 2026-10-13 01:11:54 | 0ec74895 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "84bb3b09d6bd4e0c8f2ffb85a2253 |
| 7343 | 2026-10-13 01:11:54 | 84bb3b09 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7344 | 2026-10-13 01:11:57 | d5c437bd | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7345 | 2026-10-13 01:29:53 | d5c437bd | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 190s [done] report expect='FACTORY' cmd=True \| T3 FAIL 245s  |
| 7346 | 2026-10-13 01:29:53 | d5c437bd | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 190s [done] report expect='FACTORY' cmd=True \| T3 FAIL 245s  |
| 7347 | 2026-10-13 01:29:53 | ae80d13a | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a5c9b2241151489ea85e56994e87fa75", "after_quota": "d5c437bd517e4b4e942c25fd92326 |
| 7348 | 2026-10-13 01:29:53 | d5c437bd | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7349 | 2026-10-13 01:29:54 | edc88e8d | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7350 | 2026-10-13 01:52:07 | edc88e8d | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7351 | 2026-10-13 01:52:08 | edafcea5 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7352 | 2026-10-13 02:04:44 | 4e2eedaf |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7353 | 2026-10-13 02:04:44 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7354 | 2026-10-13 02:04:45 | 457a314b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-13T03"}} |
| 7355 | 2026-10-13 02:04:45 | 4e2eedaf |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7356 | 2026-10-13 02:04:50 | 9641e7c2 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7357 | 2026-10-13 02:04:50 | fbaa4432 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-13T03"}} |
| 7358 | 2026-10-13 02:05:10 | 9641e7c2 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 7359 | 2026-10-13 02:05:10 | 9641e7c2 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash38", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 7360 | 2026-10-13 02:05:10 | 9641e7c2 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gem |
| 7361 | 2026-10-13 02:14:28 | edafcea5 | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7362 | 2026-10-13 02:14:31 | edc88e8d | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 7363 | 2026-10-13 02:36:55 | edc88e8d | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7364 | 2026-10-13 02:37:00 | edafcea5 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 7365 | 2026-10-13 02:59:10 | edafcea5 | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7366 | 2026-10-13 02:59:14 | edc88e8d | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 7367 | 2026-10-13 03:04:46 | 457a314b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7368 | 2026-10-13 03:04:46 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7369 | 2026-10-13 03:04:46 | 0a51ed8f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-13T04"}} |
| 7370 | 2026-10-13 03:04:46 | 457a314b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7371 | 2026-10-13 03:04:55 | fbaa4432 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7372 | 2026-10-13 03:04:55 | 6db6e081 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-13T04"}} |
| 7373 | 2026-10-13 03:05:24 | fbaa4432 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gem |
| 7374 | 2026-10-13 03:20:01 | edc88e8d | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 45s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 89s [done] report expect='FACTORY' cmd=False \| T3 FAIL 193s  |
| 7375 | 2026-10-13 03:20:01 | edc88e8d | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 45s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 89s [done] report expect='FACTORY' cmd=False \| T3 FAIL 193s  |
| 7376 | 2026-10-13 03:20:01 | edc88e8d | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7377 | 2026-10-13 03:20:01 | 698180d8 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "edc88e8dcadb4650816d3d495b5c5ea |
| 7378 | 2026-10-13 03:20:02 | edc88e8d | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 1, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7379 | 2026-10-13 03:20:06 | edafcea5 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 7380 | 2026-10-13 03:42:15 | edafcea5 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "failed", "attempt": 3, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
