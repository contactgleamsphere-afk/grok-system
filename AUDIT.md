# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
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
| 2025 | 2026-09-26 01:38:43 | f0a5d1b8 | 014 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2026 | 2026-09-26 01:39:16 | 476304a5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 2027 | 2026-09-26 01:39:20 | efaa0786 | 016 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2028 | 2026-09-26 01:39:58 | f0a5d1b8 | 014 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='X_OK' last='X_OK' \| T2 PASS 22s [done] expect='5' last='RESULT: 5' \| T3 PASS 17s [done] expect='Tim |
| 2029 | 2026-09-26 01:39:58 | f0a5d1b8 | 014 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='X_OK' last='X_OK' \| T2 PASS 22s [done] expect='5' last='RESULT: 5' \| T3 PASS 17s [done] expect='Tim |
| 2030 | 2026-09-26 01:39:58 | f0a5d1b8 | 014 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "014", "status": "active", "verified": "VERIFIED"}} |
| 2031 | 2026-09-26 01:40:01 | 16882d86 | 017 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2032 | 2026-09-26 01:40:42 | efaa0786 | 016 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 40s [done] expect='2' last='RESULT: 2' \| T3 PASS 14s [done] expect='3'  |
| 2033 | 2026-09-26 01:40:42 | efaa0786 | 016 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 40s [done] expect='2' last='RESULT: 2' \| T3 PASS 14s [done] expect='3'  |
| 2034 | 2026-09-26 01:40:42 | efaa0786 | 016 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "016", "status": "active", "verified": "VERIFIED"}} |
| 2035 | 2026-09-26 01:40:46 | 087596d0 | 018 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2036 | 2026-09-26 01:41:46 | 16882d86 | 017 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 28s [done] expect='3' last='RESULT: 3' \| T3 PASS 41s [done] expect='3'  |
| 2037 | 2026-09-26 01:41:46 | 16882d86 | 017 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 28s [done] expect='3' last='RESULT: 3' \| T3 PASS 41s [done] expect='3'  |
| 2038 | 2026-09-26 01:41:46 | 16882d86 | 017 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "017", "status": "active", "verified": "VERIFIED"}} |
| 2039 | 2026-09-26 01:41:49 | 1f01caca | 019 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2040 | 2026-09-26 01:42:46 | 087596d0 | 018 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 33s [done] expect='30' last='RESULT: 30' \| T3 PASS 55s [done] expect='2 |
| 2041 | 2026-09-26 01:42:46 | 087596d0 | 018 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 33s [done] expect='30' last='RESULT: 30' \| T3 PASS 55s [done] expect='2 |
| 2042 | 2026-09-26 01:42:46 | 087596d0 | 018 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "status": "active", "verified": "VERIFIED"}} |
| 2043 | 2026-09-26 01:42:50 | a461a21a | 020 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2044 | 2026-09-26 01:44:37 | 1f01caca | 019 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 44s [done] expect='1' last='RESULT: 1' \| T3 PASS 108s [done] expect='CO |
| 2045 | 2026-09-26 01:44:37 | 1f01caca | 019 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 44s [done] expect='1' last='RESULT: 1' \| T3 PASS 108s [done] expect='CO |
| 2046 | 2026-09-26 01:44:37 | 1f01caca | 019 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "019", "status": "active", "verified": "VERIFIED"}} |
| 2047 | 2026-09-26 01:44:41 | fb4da6e3 | 021 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2048 | 2026-09-26 01:46:34 | fb4da6e3 | 021 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 37s [done] expect='2' last='2' \| T3 PASS 33s [done] expect='1' last='1' |
| 2049 | 2026-09-26 01:46:34 | fb4da6e3 | 021 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 37s [done] expect='2' last='2' \| T3 PASS 33s [done] expect='1' last='1' |
| 2050 | 2026-09-26 01:46:34 | fb4da6e3 | 021 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "021", "status": "active", "verified": "VERIFIED"}} |
| 2051 | 2026-09-26 01:46:38 | 26dc19fc | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2052 | 2026-09-26 01:46:51 | a461a21a | 020 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 20s [done] expect='X_OK' last='X_OK' \| T2 FAIL 207s [done] expect='DONE' last='\u00e2\u2020\u00b3 write files.txt' \| T |
| 2053 | 2026-09-26 01:46:51 | a461a21a | 020 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 20s [done] expect='X_OK' last='X_OK' \| T2 FAIL 207s [done] expect='DONE' last='\u00e2\u2020\u00b3 write files.txt' \| T |
| 2054 | 2026-09-26 01:46:51 | a461a21a | 020 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2055 | 2026-09-26 01:46:51 | 8fecfd97 | 020 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "020", "max_rounds": 2}} |
| 2056 | 2026-09-26 01:46:51 | a461a21a | 020 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "020", "status": "testing", "verified": "UNVERIFIED"}} |
| 2057 | 2026-09-26 01:46:55 | 73874f7b | 022 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2058 | 2026-09-26 01:47:59 | 73874f7b | 022 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='X_OK' last='X_OK' \| T2 FAIL 18s [done] expect='2' last='\u00e2\u2020\u00b3 read orders.csv' \| T3 FA |
| 2059 | 2026-09-26 01:47:59 | 73874f7b | 022 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='X_OK' last='X_OK' \| T2 FAIL 18s [done] expect='2' last='\u00e2\u2020\u00b3 read orders.csv' \| T3 FA |
| 2060 | 2026-09-26 01:47:59 | 73874f7b | 022 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2061 | 2026-09-26 01:47:59 | 1262b64a | 022 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "022", "max_rounds": 2}} |
| 2062 | 2026-09-26 01:47:59 | 73874f7b | 022 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "022", "status": "testing", "verified": "UNVERIFIED"}} |
| 2063 | 2026-09-26 01:48:03 | 1d115db4 | 023 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2064 | 2026-09-26 01:49:12 | 1d115db4 | 023 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 12s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\023.json' \| T2 PASS 15s [done] expect='36.0' |
| 2065 | 2026-09-26 01:49:12 | 1d115db4 | 023 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 12s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\023.json' \| T2 PASS 15s [done] expect='36.0' |
| 2066 | 2026-09-26 01:49:12 | 1d115db4 | 023 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2067 | 2026-09-26 01:49:12 | 1a04d2e0 | 023 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "023", "max_rounds": 2}} |
| 2068 | 2026-09-26 01:49:12 | 1d115db4 | 023 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "023", "status": "testing", "verified": "UNVERIFIED"}} |
| 2069 | 2026-09-26 01:49:16 | 8d889942 | 024 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2070 | 2026-09-26 01:50:12 | 4207163b |  | job.enqueued | master-001 | {"kind": "create", "payload": {"objective": "Test weekly self-review bot"}} |
| 2071 | 2026-09-26 01:50:17 | 8d889942 | 024 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='X_OK' \| T2 PASS 22s [done] expect='2' last='2' \| T3 PASS 22s [done] expect='CONFINED' l |
| 2072 | 2026-09-26 01:50:17 | 8d889942 | 024 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='X_OK' \| T2 PASS 22s [done] expect='2' last='2' \| T3 PASS 22s [done] expect='CONFINED' l |
| 2073 | 2026-09-26 01:50:17 | 8d889942 | 024 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "024", "status": "active", "verified": "VERIFIED"}} |
| 2074 | 2026-09-26 01:50:21 | 57ca83b6 | 025 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2075 | 2026-09-26 01:50:31 | 26dc19fc | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 2076 | 2026-09-26 01:50:31 | 26dc19fc | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 2077 | 2026-09-26 01:50:31 | 26dc19fc | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2078 | 2026-09-26 01:50:31 | 9eb7524a | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "26dc19fca79c45b78edd0a01873a089 |
| 2079 | 2026-09-26 01:50:31 | 26dc19fc | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2080 | 2026-09-26 01:50:35 | 8fecfd97 | 020 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2081 | 2026-09-26 01:51:14 | 57ca83b6 | 025 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='LIVENESS_OK' last='LIVENESS_OK' \| T2 PASS 20s [done] expect='HELLO WORLD' last='RESULT: HELLO WORLD' |
| 2082 | 2026-09-26 01:51:14 | 57ca83b6 | 025 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='LIVENESS_OK' last='LIVENESS_OK' \| T2 PASS 20s [done] expect='HELLO WORLD' last='RESULT: HELLO WORLD' |
| 2083 | 2026-09-26 01:51:14 | 57ca83b6 | 025 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "025", "status": "active", "verified": "VERIFIED"}} |
| 2084 | 2026-09-26 01:51:18 | bac2335f | 026 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2085 | 2026-09-26 01:53:06 | bac2335f | 026 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] expect='X_OK' last='X_OK' \| T2 PASS 26s [done] expect='3' last='RESULT: 3' \| T3 PASS 27s [done] expect='use |
| 2086 | 2026-09-26 01:53:06 | bac2335f | 026 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] expect='X_OK' last='X_OK' \| T2 PASS 26s [done] expect='3' last='RESULT: 3' \| T3 PASS 27s [done] expect='use |
| 2087 | 2026-09-26 01:53:06 | bac2335f | 026 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "026", "status": "active", "verified": "VERIFIED"}} |
| 2088 | 2026-09-26 01:53:26 | 8fecfd97 | 020 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 2089 | 2026-09-26 01:53:26 | 8fecfd97 | 020 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 2090 | 2026-09-26 01:53:26 | 8fecfd97 | 020 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "020", "status": "active"}} |
| 2091 | 2026-09-26 01:53:30 | 1262b64a | 022 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2092 | 2026-09-26 01:55:52 | 1262b64a | 022 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 2093 | 2026-09-26 01:55:52 | 1262b64a | 022 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 2094 | 2026-09-26 01:55:52 | 1262b64a | 022 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "022", "status": "active"}} |
| 2095 | 2026-09-26 01:55:55 | 1a04d2e0 | 023 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2096 | 2026-09-26 01:57:23 | 1a04d2e0 | 023 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 2097 | 2026-09-26 01:57:23 | 1a04d2e0 | 023 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 2098 | 2026-09-26 01:57:23 | 1a04d2e0 | 023 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "023", "status": "active"}} |
| 2099 | 2026-09-26 01:57:26 | 4207163b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2100 | 2026-09-26 01:57:30 | 4207163b | 027 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "self-review-bot", "tools": ["read_file", "write_file", "web_search", "web_fetch"], "permissions": ["fs:read", "fs:write", "net:sea |
| 2101 | 2026-09-26 01:58:12 | 4207163b | 027 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 14s [done] expect='2' last='RESULT: 2' \| T3 PASS 13s [done] expect='CON |
| 2102 | 2026-09-26 01:58:12 | 4207163b | 027 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "027", "name": "self-review-bot", "pass": 3, "total": 3, "status": "active", "verified": "VERIFIED"}} |
| 2103 | 2026-09-26 01:58:15 | 6e64545f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2104 | 2026-09-26 01:59:53 | 6e64545f |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "or-qwen27b", "result": "2/4", "quota": 2, "secs": 96} |
| 2105 | 2026-09-26 01:59:53 | 6e64545f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["or-qwen27b", "2/4 q2"]]}} |
| 2106 | 2026-09-26 01:59:56 | 15dcb4d1 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2107 | 2026-09-26 02:00:10 | 268e463f |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2108 | 2026-09-26 02:00:10 | eeba28ae |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-26T03"}} |
| 2109 | 2026-09-26 02:00:10 | 268e463f |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2110 | 2026-09-26 02:00:56 | 15dcb4d1 |  | factory.canary | svc-LAPTOP-LRE6PSA8 | {"verdict": "FAIL", "lane": "gemini:gemini-3.1-flash-lite", "chain": ["gemini-gemini-flash-lite-latest", "gemini-lite31", "or-ling-30-flash- |
| 2111 | 2026-09-26 02:00:56 | 15dcb4d1 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"pass": 2, "total": 3}} |
| 2112 | 2026-09-27 01:58:45 | afc49d7c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2113 | 2026-09-27 01:58:45 | 5854ee45 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-27T02"}} |
| 2114 | 2026-09-27 01:58:52 | eeba28ae |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2115 | 2026-09-27 01:58:58 | afa33da8 | 018 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "run", "payload": {"bot_id": "018", "task": "Sum order totals per country into totals.csv", "in": "C:\\AI\\Factory\\workspace\\inbo |
| 2116 | 2026-09-27 01:58:58 |  | 018 | schedule.fired | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "fire": "2026-09-26T07:00", "job": "afa33da8"} |
| 2117 | 2026-09-27 01:59:11 | 85375329 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-27T02"}} |
| 2118 | 2026-09-27 01:59:11 | eeba28ae |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2119 | 2026-09-27 01:59:16 | 9eb7524a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2120 | 2026-09-27 01:59:18 | afc49d7c |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "or-nemotron-35-lightning", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 2121 | 2026-09-27 01:59:18 | afc49d7c |  | model.retired | svc-LAPTOP-LRE6PSA8 | {"model": "or-ling-30-flash-vl", "reason": "gone: {\"error\":{\"message\":\"this model is unavailable for free. the paid version "} |
| 2122 | 2026-09-27 01:59:18 | afc49d7c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-li |
| 2123 | 2026-09-27 01:59:22 | afa33da8 | 018 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2124 | 2026-09-27 01:59:50 | afa33da8 | 018 | bot.ran | svc-LAPTOP-LRE6PSA8 | {"ok": true, "produced": [], "secs": 26, "reply": "\u00e2\u2020\u00b3 read orders.csv", "chain": "groq-gptoss120b"} |
| 2125 | 2026-09-27 01:59:50 | afa33da8 | 018 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "name": "run", "status": "ok "}} |
| 2126 | 2026-09-27 01:59:54 | c632d578 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2127 | 2026-09-27 01:59:54 | c632d578 |  | audit.verified | svc-LAPTOP-LRE6PSA8 | {"rows": 2125, "hashed": 1373, "first_bad": null} |
| 2128 | 2026-09-27 01:59:54 | 934b7127 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-09-28"}} |
| 2129 | 2026-09-27 01:59:54 | 91ce36cc |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-09-27"}} |
| 2130 | 2026-09-27 01:59:54 | dac94e57 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-09-27"}} |
| 2131 | 2026-09-27 01:59:54 | 0583e758 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-09-27"}} |
| 2132 | 2026-09-27 01:59:54 | c632d578 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2133 | 2026-09-27 01:59:58 | 0583e758 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2134 | 2026-09-27 01:59:58 | 84b99924 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2135 | 2026-09-27 01:59:58 | b1296d1f | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "003", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2136 | 2026-09-27 01:59:58 | d963383e | 004 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "004", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2137 | 2026-09-27 01:59:58 | 498a5257 | 005 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "005", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2138 | 2026-09-27 01:59:58 | c59bd289 | 006 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "006", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2139 | 2026-09-27 01:59:58 | 5fc85952 | 007 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "007", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2140 | 2026-09-27 01:59:58 | 70498d38 | 008 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "008", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2141 | 2026-09-27 01:59:58 | 5613a43c | 009 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "009", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2142 | 2026-09-27 01:59:58 | 3416fe9b | 011 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "011", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2143 | 2026-09-27 01:59:58 | d4c54a80 | 012 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "012", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2144 | 2026-09-27 01:59:58 | d91b2b7f | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "013", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2145 | 2026-09-27 01:59:58 | e36bba9b | 014 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "014", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2146 | 2026-09-27 01:59:58 | fc5bc316 | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "016", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2147 | 2026-09-27 01:59:58 | 7cdaf7c8 | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "017", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2148 | 2026-09-27 01:59:58 | f2186a09 | 018 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "018", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2149 | 2026-09-27 01:59:58 | 36534eea | 019 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "019", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2150 | 2026-09-27 01:59:58 | 60f6d165 | 020 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "020", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2151 | 2026-09-27 01:59:58 | b2ce3a78 | 021 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "021", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2152 | 2026-09-27 01:59:58 | 9938d282 | 022 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "022", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2153 | 2026-09-27 01:59:58 | 80ab802c | 023 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "023", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2154 | 2026-09-27 01:59:58 | f77b5429 | 024 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "024", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2155 | 2026-09-27 01:59:58 | fab188c6 | 025 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "025", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2156 | 2026-09-27 01:59:58 | 615ea54e | 026 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "026", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2157 | 2026-09-27 01:59:58 | 399f0206 | 027 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "027", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2158 | 2026-09-27 01:59:58 | 0583e758 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "003", "004", "005", "006", "007", "008", "009", "011", "012", "013", "014", "016", "017", "018", "019", "020", "021", "022 |
| 2159 | 2026-09-27 01:59:58 | 0583e758 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2160 | 2026-09-27 02:00:03 | b1296d1f | 003 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2161 | 2026-09-27 02:01:04 | b1296d1f | 003 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 3s [done] expect='SMITH_OK' last='' \| T2 FAIL 17s [done] expect='233168' last='\u00e2\u2020\u00b3 $ python fizz.py' \|  |
| 2162 | 2026-09-27 02:01:04 | b1296d1f | 003 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 3s [done] expect='SMITH_OK' last='' \| T2 FAIL 17s [done] expect='233168' last='\u00e2\u2020\u00b3 $ python fizz.py' \|  |
| 2163 | 2026-09-27 02:01:04 | b1296d1f | 003 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2164 | 2026-09-27 02:01:04 | 6af00a36 | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "003", "max_rounds": 2}} |
| 2165 | 2026-09-27 02:01:04 | b1296d1f | 003 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "status": "testing", "verified": "UNVERIFIED"}} |
| 2166 | 2026-09-27 02:01:09 | 6af00a36 | 003 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2167 | 2026-09-27 02:02:11 | 6af00a36 | 003 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": "instructions har |
| 2168 | 2026-09-27 02:02:11 | 80c15c41 | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "rearchitect", "payload": {"bot_id": "003", "feedback": "logic: spec/tests inconsistent, tests expect a literal the instructions mu |
| 2169 | 2026-09-27 02:02:11 | 6af00a36 | 003 | bot.rearchitect_queued | svc-LAPTOP-LRE6PSA8 | {"reason": "logic: spec/tests inconsistent, tests expect a literal the instructions must mention (no passing candidate in 2 rounds)"} |
| 2170 | 2026-09-27 02:02:11 | 6af00a36 | 003 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: logic: spec/tests inconsistent, tests expect a lite |
| 2171 | 2026-09-27 02:02:14 | 80c15c41 | 003 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2172 | 2026-09-27 02:04:26 | 9eb7524a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 20s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 2173 | 2026-09-27 02:04:27 | 9eb7524a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 20s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 2174 | 2026-09-27 02:04:27 | 9eb7524a | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2175 | 2026-09-27 02:04:27 | e6729e00 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "9eb7524a860b4238ac2959a3808efcd |
| 2176 | 2026-09-27 02:04:27 | 9eb7524a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2177 | 2026-09-27 02:04:27 | 80c15c41 | 003 | bot.rearchitected | svc-LAPTOP-LRE6PSA8 | {"lane": "groq:openai/gpt-oss-20b", "tools": ["write_file", "exec"], "permissions": ["fs:write", "shell:workspace"], "boundary_diff": {"mode |
| 2178 | 2026-09-27 02:04:27 | 5bee2f1f | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "003", "retest_of": "80c15c41c6114e5c9171e688978ba456", "rearchitected": true}} |
| 2179 | 2026-09-27 02:04:27 | 80c15c41 | 003 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "pass": 3, "total": 4, "status": "testing"}} |
| 2180 | 2026-09-27 02:04:32 | 5bee2f1f | 003 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2181 | 2026-09-27 02:04:32 | 84b99924 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2182 | 2026-09-27 02:05:36 | 5bee2f1f | 003 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='RESULT: X_OK' \| T2 FAIL 16s [done] expect='3' last='Using config: C:\\AI\\Factory\\run\\ |
| 2183 | 2026-09-27 02:05:36 | 820f6fef | 003 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "003", "retest_of": "80c15c41c6114e5c9171e688978ba456", "after_quota": "5bee2f1fc52b458b9fdc2e58267b6 |
| 2184 | 2026-09-27 02:05:36 | 5bee2f1f | 003 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "status": "testing", "verified": "UNVERIFIED"}} |
| 2185 | 2026-09-27 02:05:40 | d963383e | 004 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2186 | 2026-09-27 02:07:05 | d963383e | 004 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 19s [done] expect='CHANGELOG_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\004.json' \| T2 FAIL 19s [done] expec |
| 2187 | 2026-09-27 02:07:05 | d963383e | 004 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 19s [done] expect='CHANGELOG_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\004.json' \| T2 FAIL 19s [done] expec |
| 2188 | 2026-09-27 02:07:05 | d963383e | 004 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2189 | 2026-09-27 02:07:05 | 510ea5e2 | 004 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "004", "max_rounds": 2}} |
| 2190 | 2026-09-27 02:07:05 | d963383e | 004 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "004", "status": "testing", "verified": "UNVERIFIED"}} |
| 2191 | 2026-09-27 02:07:09 | 498a5257 | 005 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2192 | 2026-09-27 02:08:20 | 84b99924 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 15s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 2193 | 2026-09-27 02:08:20 | 84b99924 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 15s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 2194 | 2026-09-27 02:08:20 | 84b99924 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2195 | 2026-09-27 02:08:20 | fd15dd84 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "84b999246062475198d5b12e79a523c |
| 2196 | 2026-09-27 02:08:20 | 84b99924 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2197 | 2026-09-27 02:08:24 | 510ea5e2 | 004 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2198 | 2026-09-27 02:09:31 | 498a5257 | 005 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 FAIL 50s [done] expect='1' last='\u00e2\u2020\u00b3 read data.csv' \| T3 PASS  |
| 2199 | 2026-09-27 02:09:31 | 498a5257 | 005 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 FAIL 50s [done] expect='1' last='\u00e2\u2020\u00b3 read data.csv' \| T3 PASS  |
| 2200 | 2026-09-27 02:09:31 | 498a5257 | 005 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2201 | 2026-09-27 02:09:31 | bb708ee5 | 005 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "005", "max_rounds": 2}} |
| 2202 | 2026-09-27 02:09:31 | 498a5257 | 005 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "005", "status": "testing", "verified": "UNVERIFIED"}} |
| 2203 | 2026-09-27 02:09:36 | c59bd289 | 006 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2204 | 2026-09-27 02:11:55 | c59bd289 | 006 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] expect='X_OK' last='X_OK' \| T2 PASS 57s [done] expect='2' last='2' \| T3 PASS 50s [done] expect='0' last='0' |
| 2205 | 2026-09-27 02:11:55 | c59bd289 | 006 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] expect='X_OK' last='X_OK' \| T2 PASS 57s [done] expect='2' last='2' \| T3 PASS 50s [done] expect='0' last='0' |
| 2206 | 2026-09-27 02:11:55 | c59bd289 | 006 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "006", "status": "active", "verified": "VERIFIED"}} |
| 2207 | 2026-09-27 02:12:00 | 5fc85952 | 007 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2208 | 2026-09-27 02:14:33 | 5fc85952 | 007 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='X_OK' \| T2 PASS 56s [done] expect='2' last='2' \| T3 PASS 55s [done] expect='0' last='0' |
| 2209 | 2026-09-27 02:14:33 | 5fc85952 | 007 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='X_OK' \| T2 PASS 56s [done] expect='2' last='2' \| T3 PASS 55s [done] expect='0' last='0' |
| 2210 | 2026-09-27 02:14:33 | 5fc85952 | 007 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2211 | 2026-09-27 02:14:33 | 7efd58c0 | 007 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "007", "max_rounds": 2}} |
| 2212 | 2026-09-27 02:14:33 | 5fc85952 | 007 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "status": "testing", "verified": "UNVERIFIED"}} |
| 2213 | 2026-09-27 02:14:37 | 70498d38 | 008 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2214 | 2026-09-27 02:16:46 | 70498d38 | 008 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] expect='X_OK' last='X_OK' \| T2 PASS 42s [done] expect='apple' last='RESULT: apple' \| T3 PASS 46s [done] exp |
| 2215 | 2026-09-27 02:16:46 | 70498d38 | 008 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] expect='X_OK' last='X_OK' \| T2 PASS 42s [done] expect='apple' last='RESULT: apple' \| T3 PASS 46s [done] exp |
| 2216 | 2026-09-27 02:16:46 | 70498d38 | 008 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "008", "status": "active", "verified": "VERIFIED"}} |
| 2217 | 2026-09-27 02:16:50 | 5613a43c | 009 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2218 | 2026-09-27 02:19:06 | 5613a43c | 009 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 60s [done] expect='3' last='RESULT: 3' \| T3 PASS 52s [done] expect='1' l |
| 2219 | 2026-09-27 02:19:06 | 5613a43c | 009 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 60s [done] expect='3' last='RESULT: 3' \| T3 PASS 52s [done] expect='1' l |
| 2220 | 2026-09-27 02:19:06 | 5613a43c | 009 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "009", "status": "active", "verified": "VERIFIED"}} |
| 2221 | 2026-09-27 02:19:10 | 3416fe9b | 011 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2222 | 2026-09-27 02:20:34 | 3416fe9b | 011 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 FAIL 24s [done] expect='2' last='\u00e2\u0153\u00bb Write freq.txt.' \| T3 PAS |
| 2223 | 2026-09-27 02:20:34 | 3416fe9b | 011 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 FAIL 24s [done] expect='2' last='\u00e2\u0153\u00bb Write freq.txt.' \| T3 PAS |
| 2224 | 2026-09-27 02:20:34 | 3416fe9b | 011 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2225 | 2026-09-27 02:20:34 | e0e759b6 | 011 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "011", "max_rounds": 2}} |
| 2226 | 2026-09-27 02:20:34 | 3416fe9b | 011 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "011", "status": "testing", "verified": "UNVERIFIED"}} |
| 2227 | 2026-09-27 02:20:39 | d4c54a80 | 012 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2228 | 2026-09-27 02:21:20 | 510ea5e2 | 004 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-de |
| 2229 | 2026-09-27 02:21:20 | 510ea5e2 | 004 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 2230 | 2026-09-27 02:21:24 | bb708ee5 | 005 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2231 | 2026-09-27 02:23:07 | d4c54a80 | 012 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 48s [done] expect='60' last='RESULT: Summed amount column from data.csv,  |
| 2232 | 2026-09-27 02:23:07 | d4c54a80 | 012 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 48s [done] expect='60' last='RESULT: Summed amount column from data.csv,  |
| 2233 | 2026-09-27 02:23:07 | d4c54a80 | 012 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "012", "status": "active", "verified": "VERIFIED"}} |
| 2234 | 2026-09-27 02:23:10 | d91b2b7f | 013 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2235 | 2026-09-27 02:26:49 | bb708ee5 | 005 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 2236 | 2026-09-27 02:26:49 | bb708ee5 | 005 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 2237 | 2026-09-27 02:26:49 | bb708ee5 | 005 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "005", "status": "active"}} |
| 2238 | 2026-09-27 02:26:53 | 7efd58c0 | 007 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2239 | 2026-09-27 02:27:38 | d91b2b7f | 013 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 89s [done] expect='X_OK' last='RESULT: 1' \| T2 PASS 73s [done] expect='1' last='RESULT: 1' \| T3 PASS 91s [done] expect |
| 2240 | 2026-09-27 02:27:38 | d91b2b7f | 013 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 89s [done] expect='X_OK' last='RESULT: 1' \| T2 PASS 73s [done] expect='1' last='RESULT: 1' \| T3 PASS 91s [done] expect |
| 2241 | 2026-09-27 02:27:38 | d91b2b7f | 013 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2242 | 2026-09-27 02:27:38 | 47d7895c | 013 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "013", "max_rounds": 2}} |
| 2243 | 2026-09-27 02:27:38 | d91b2b7f | 013 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "013", "status": "testing", "verified": "UNVERIFIED"}} |
| 2244 | 2026-09-27 02:27:42 | e36bba9b | 014 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2245 | 2026-09-27 02:28:50 | e36bba9b | 014 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 20s [done] expect='5' last='RESULT: 5' \| T3 PASS 19s [done] expect='Tim |
| 2246 | 2026-09-27 02:28:50 | e36bba9b | 014 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 20s [done] expect='5' last='RESULT: 5' \| T3 PASS 19s [done] expect='Tim |
| 2247 | 2026-09-27 02:28:50 | e36bba9b | 014 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "014", "status": "active", "verified": "VERIFIED"}} |
| 2248 | 2026-09-27 02:28:54 | fc5bc316 | 016 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2249 | 2026-09-27 02:29:35 | fc5bc316 | 016 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 PASS 10s [done] expect='2' last='RESULT: 2' \| T3 PASS 11s [done] expect='3'  |
| 2250 | 2026-09-27 02:29:35 | fc5bc316 | 016 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 PASS 10s [done] expect='2' last='RESULT: 2' \| T3 PASS 11s [done] expect='3'  |
| 2251 | 2026-09-27 02:29:35 | fc5bc316 | 016 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "016", "status": "active", "verified": "VERIFIED"}} |
| 2252 | 2026-09-27 02:29:39 | 7cdaf7c8 | 017 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2253 | 2026-09-27 02:29:56 | 7efd58c0 | 007 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 2254 | 2026-09-27 02:29:56 | 7efd58c0 | 007 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 2255 | 2026-09-27 02:29:56 | 7efd58c0 | 007 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "status": "active"}} |
| 2256 | 2026-09-27 02:30:00 | e0e759b6 | 011 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2257 | 2026-09-27 02:31:25 | 7cdaf7c8 | 017 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] expect='X_OK' last='X_OK' \| T2 PASS 26s [done] expect='3' last='RESULT: 3' \| T3 PASS 19s [done] expect='3'  |
| 2258 | 2026-09-27 02:31:25 | 7cdaf7c8 | 017 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] expect='X_OK' last='X_OK' \| T2 PASS 26s [done] expect='3' last='RESULT: 3' \| T3 PASS 19s [done] expect='3'  |
| 2259 | 2026-09-27 02:31:25 | 7cdaf7c8 | 017 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "017", "status": "active", "verified": "VERIFIED"}} |
| 2260 | 2026-09-27 02:31:28 | f2186a09 | 018 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2261 | 2026-09-27 02:31:40 | e0e759b6 | 011 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 2262 | 2026-09-27 02:31:40 | e0e759b6 | 011 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 2263 | 2026-09-27 02:31:40 | e0e759b6 | 011 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "011", "status": "active"}} |
| 2264 | 2026-09-27 02:31:44 | 47d7895c | 013 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2265 | 2026-09-27 02:33:41 | 47d7895c | 013 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 2266 | 2026-09-27 02:33:41 | 47d7895c | 013 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 2267 | 2026-09-27 02:33:41 | 47d7895c | 013 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "013", "status": "active"}} |
| 2268 | 2026-09-27 02:33:42 | f2186a09 | 018 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 50s [done] expect='30' last='RESULT: 30' \| T3 PASS 56s [done] expect='20 |
| 2269 | 2026-09-27 02:33:42 | f2186a09 | 018 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 50s [done] expect='30' last='RESULT: 30' \| T3 PASS 56s [done] expect='20 |
| 2270 | 2026-09-27 02:33:42 | f2186a09 | 018 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "status": "active", "verified": "VERIFIED"}} |
| 2271 | 2026-09-27 02:33:44 | 36534eea | 019 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2272 | 2026-09-27 02:33:48 | 60f6d165 | 020 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2273 | 2026-09-27 02:36:03 | 36534eea | 019 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 90s [done] expect='1' last='RESULT: 1' \| T3 PASS 39s [done] expect='CONF |
| 2274 | 2026-09-27 02:36:03 | 36534eea | 019 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 90s [done] expect='1' last='RESULT: 1' \| T3 PASS 39s [done] expect='CONF |
| 2275 | 2026-09-27 02:36:03 | 36534eea | 019 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "019", "status": "active", "verified": "VERIFIED"}} |
| 2276 | 2026-09-27 02:36:06 | e6729e00 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2277 | 2026-09-27 02:36:19 | 60f6d165 | 020 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 FAIL 130s [done] expect='DONE' last='\u00e2\u2020\u00b3 $ dir' \| T3 PASS 11s  |
| 2278 | 2026-09-27 02:36:19 | 60f6d165 | 020 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 FAIL 130s [done] expect='DONE' last='\u00e2\u2020\u00b3 $ dir' \| T3 PASS 11s  |
| 2279 | 2026-09-27 02:36:19 | 60f6d165 | 020 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2280 | 2026-09-27 02:36:19 | c04521f6 | 020 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "020", "max_rounds": 2}} |
| 2281 | 2026-09-27 02:36:19 | 60f6d165 | 020 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "020", "status": "testing", "verified": "UNVERIFIED"}} |
| 2282 | 2026-09-27 02:36:22 | b2ce3a78 | 021 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2283 | 2026-09-27 02:37:11 | b2ce3a78 | 021 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 10s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\021.json' \| T2 FAIL 13s [done] expect='2' la |
| 2284 | 2026-09-27 02:37:11 | b2ce3a78 | 021 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 10s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\021.json' \| T2 FAIL 13s [done] expect='2' la |
| 2285 | 2026-09-27 02:37:11 | b2ce3a78 | 021 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2286 | 2026-09-27 02:37:11 | a1d92047 | 021 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "021", "max_rounds": 2}} |
| 2287 | 2026-09-27 02:37:11 | b2ce3a78 | 021 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "021", "status": "testing", "verified": "UNVERIFIED"}} |
| 2288 | 2026-09-27 02:37:15 | 9938d282 | 022 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2289 | 2026-09-27 02:38:36 | 9938d282 | 022 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 12s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\022.json' \| T2 FAIL 25s [done] expect='2' la |
| 2290 | 2026-09-27 02:38:36 | 9938d282 | 022 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 12s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\022.json' \| T2 FAIL 25s [done] expect='2' la |
| 2291 | 2026-09-27 02:38:36 | 9938d282 | 022 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2292 | 2026-09-27 02:38:36 | 0f7762f5 | 022 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "022", "max_rounds": 2}} |
| 2293 | 2026-09-27 02:38:36 | 9938d282 | 022 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "022", "status": "testing", "verified": "UNVERIFIED"}} |
| 2294 | 2026-09-27 02:38:39 | 80ab802c | 023 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2295 | 2026-09-27 02:39:38 | e6729e00 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 14s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 2296 | 2026-09-27 02:39:38 | e6729e00 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 14s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 2297 | 2026-09-27 02:39:38 | e6729e00 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2298 | 2026-09-27 02:39:38 | 032aaab8 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "e6729e00990a403aa9d0f5712d5b61f |
| 2299 | 2026-09-27 02:39:38 | e6729e00 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2300 | 2026-09-27 02:39:41 | fd15dd84 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2301 | 2026-09-27 02:39:52 | 80ab802c | 023 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 FAIL 40s [done] expect='36.0' last='\u00e2\u2020\u00b3 write summary.txt' \| T |
| 2302 | 2026-09-27 02:39:52 | 80ab802c | 023 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 FAIL 40s [done] expect='36.0' last='\u00e2\u2020\u00b3 write summary.txt' \| T |
| 2303 | 2026-09-27 02:39:52 | 80ab802c | 023 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2304 | 2026-09-27 02:39:52 | cc46a3c1 | 023 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "023", "max_rounds": 2}} |
| 2305 | 2026-09-27 02:39:52 | 80ab802c | 023 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "023", "status": "testing", "verified": "UNVERIFIED"}} |
| 2306 | 2026-09-27 02:39:56 | f77b5429 | 024 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2307 | 2026-09-27 02:40:22 | f77b5429 | 024 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 FAIL 4s [done] expect='2' last='Using config: C:\\AI\\Factory\\run\\botcfg\\02 |
| 2308 | 2026-09-27 02:40:22 | f77b5429 | 024 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 FAIL 4s [done] expect='2' last='Using config: C:\\AI\\Factory\\run\\botcfg\\02 |
| 2309 | 2026-09-27 02:40:22 | 7bdfafac | 024 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "024", "retest_of": "f77b542937fa432fa1d79284bbf4c033", "after_quota": "f77b542937fa432fa1d79284bbf4c |
| 2310 | 2026-09-27 02:40:22 | f77b5429 | 024 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "024", "status": "active", "verified": "VERIFIED"}} |
| 2311 | 2026-09-27 02:40:27 | fab188c6 | 025 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2312 | 2026-09-27 02:40:57 | fab188c6 | 025 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 7s [done] expect='LIVENESS_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\025.json' \| T2 FAIL 10s [done] expect= |
| 2313 | 2026-09-27 02:40:57 | fab188c6 | 025 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 7s [done] expect='LIVENESS_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\025.json' \| T2 FAIL 10s [done] expect= |
| 2314 | 2026-09-27 02:40:57 | fab188c6 | 025 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2315 | 2026-09-27 02:40:57 | f1f6536d | 025 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "025", "max_rounds": 2}} |
| 2316 | 2026-09-27 02:40:57 | fab188c6 | 025 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "025", "status": "testing", "verified": "UNVERIFIED"}} |
| 2317 | 2026-09-27 02:41:00 | 615ea54e | 026 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2318 | 2026-09-27 02:42:03 | 615ea54e | 026 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 10s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\026.json' \| T2 FAIL 15s [done] expect='3' la |
| 2319 | 2026-09-27 02:42:03 | 615ea54e | 026 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 10s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\026.json' \| T2 FAIL 15s [done] expect='3' la |
| 2320 | 2026-09-27 02:42:03 | 615ea54e | 026 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2321 | 2026-09-27 02:42:03 | 1a9490be | 026 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "026", "max_rounds": 2}} |
| 2322 | 2026-09-27 02:42:03 | 615ea54e | 026 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "026", "status": "testing", "verified": "UNVERIFIED"}} |
| 2323 | 2026-09-27 02:42:08 | 399f0206 | 027 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2324 | 2026-09-27 02:42:23 | fd15dd84 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 2325 | 2026-09-27 02:42:23 | fd15dd84 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 2326 | 2026-09-27 02:42:23 | fd15dd84 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2327 | 2026-09-27 02:42:23 | 94547dfb | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "fd15dd84b8714185b552f47065a12f2 |
| 2328 | 2026-09-27 02:42:23 | fd15dd84 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2329 | 2026-09-27 02:42:28 | c04521f6 | 020 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2330 | 2026-09-27 02:42:37 | 399f0206 | 027 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 5s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\027.json' \| T2 PASS 12s [done] expect='2' las |
| 2331 | 2026-09-27 02:42:37 | 399f0206 | 027 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 5s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\027.json' \| T2 PASS 12s [done] expect='2' las |
| 2332 | 2026-09-27 02:42:37 | 8cb8963c | 027 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "027", "retest_of": "399f02063cbb4c60ae4a0b338431464c", "after_quota": "399f02063cbb4c60ae4a0b3384314 |
| 2333 | 2026-09-27 02:42:37 | 399f0206 | 027 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "027", "status": "active", "verified": "VERIFIED"}} |
| 2334 | 2026-09-27 02:47:58 | c04521f6 | 020 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-li |
| 2335 | 2026-09-27 02:47:58 | c04521f6 | 020 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 2336 | 2026-09-27 02:48:02 | a1d92047 | 021 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2337 | 2026-09-27 02:50:59 | a1d92047 | 021 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-li |
| 2338 | 2026-09-27 02:50:59 | a1d92047 | 021 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 2339 | 2026-09-27 02:51:03 | 0f7762f5 | 022 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2340 | 2026-09-27 02:53:02 | 0f7762f5 | 022 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 2341 | 2026-09-27 02:53:02 | 0f7762f5 | 022 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 2342 | 2026-09-27 02:53:02 | 0f7762f5 | 022 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "022", "status": "active"}} |
| 2343 | 2026-09-27 02:53:05 | cc46a3c1 | 023 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2344 | 2026-09-27 02:54:52 | cc46a3c1 | 023 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 2345 | 2026-09-27 02:54:52 | cc46a3c1 | 023 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 2346 | 2026-09-27 02:54:52 | cc46a3c1 | 023 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "023", "status": "active"}} |
| 2347 | 2026-09-27 02:54:56 | f1f6536d | 025 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2348 | 2026-09-27 02:55:49 | f1f6536d | 025 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 2349 | 2026-09-27 02:55:49 | f1f6536d | 025 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 2350 | 2026-09-27 02:55:49 | f1f6536d | 025 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "025", "status": "active"}} |
| 2351 | 2026-09-27 02:55:52 | 1a9490be | 026 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2352 | 2026-09-27 02:56:56 | 1a9490be | 026 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 2353 | 2026-09-27 02:56:56 | 1a9490be | 026 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 2354 | 2026-09-27 02:56:56 | 1a9490be | 026 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "026", "status": "active"}} |
| 2355 | 2026-09-27 02:56:59 | 91ce36cc |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2356 | 2026-09-27 02:56:59 | 91ce36cc |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": []}} |
| 2357 | 2026-09-27 02:57:04 | dac94e57 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2358 | 2026-09-27 02:57:26 | dac94e57 |  | factory.canary | svc-LAPTOP-LRE6PSA8 | {"verdict": "pass", "lane": "groq:openai/gpt-oss-20b", "chain": ["gemini-gemini-flash-lite-latest", "gemini-lite31", "or-ling-30-flash-sante |
| 2359 | 2026-09-27 02:57:26 | dac94e57 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"pass": 2, "total": 2}} |
