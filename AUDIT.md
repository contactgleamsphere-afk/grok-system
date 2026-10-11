# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 6796 | 2026-10-11 02:14:32 | 9ce5ad7b | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "139734ae344e49089147d3f47942ffc6", "after_quota": "cc02da075a154eddb500fb2eefd62 |
| 6797 | 2026-10-11 02:14:32 | cc02da07 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6798 | 2026-10-11 02:14:34 | 29b0b257 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6799 | 2026-10-11 02:28:20 | 29b0b257 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 70s [done] report expect='FACTORY' cmd=True \| T3 PASS 102s [ |
| 6800 | 2026-10-11 02:28:20 | 29b0b257 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 70s [done] report expect='FACTORY' cmd=True \| T3 PASS 102s [ |
| 6801 | 2026-10-11 02:28:20 | 1f7039b7 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "41923cc5baaa4b7ba7c14909b7abe137", "after_quota": "29b0b257be6d48de80613d6c83ce4 |
| 6802 | 2026-10-11 02:28:20 | 29b0b257 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6803 | 2026-10-11 02:28:24 | 61f16e1b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6804 | 2026-10-11 02:40:46 | 61f16e1b | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 6805 | 2026-10-11 02:40:46 | 61f16e1b | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 6806 | 2026-10-11 02:40:46 | f62aa317 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "61f16e1b1517422cbcc79ea5311b5 |
| 6807 | 2026-10-11 02:40:46 | 61f16e1b | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6808 | 2026-10-11 02:40:50 | fe371a05 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6809 | 2026-10-11 02:52:44 | fe371a05 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 6810 | 2026-10-11 02:52:44 | fe371a05 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 6811 | 2026-10-11 02:52:44 | 1fb2187f | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fe371a05201e499c9cc16d620128e678", "after_quota": "fe371a05201e499c9cc16d620128e |
| 6812 | 2026-10-11 02:52:44 | fe371a05 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6813 | 2026-10-11 02:52:46 | b86506e5 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6814 | 2026-10-11 02:55:14 | 2ee09965 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6815 | 2026-10-11 02:55:14 | ff19a2e8 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-11T03"}} |
| 6816 | 2026-10-11 02:55:54 | 2ee09965 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 6817 | 2026-10-11 02:55:54 | 2ee09965 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gem |
| 6818 | 2026-10-11 02:55:57 | 1871d280 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6819 | 2026-10-11 02:55:57 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 6820 | 2026-10-11 02:55:57 | ca865945 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-11T03"}} |
| 6821 | 2026-10-11 02:55:57 | 1871d280 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6822 | 2026-10-11 03:05:18 | b86506e5 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 64s [d |
| 6823 | 2026-10-11 03:05:18 | b86506e5 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 64s [d |
| 6824 | 2026-10-11 03:05:18 | 63f3f6e0 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "b55e8b342b7b4b37acedb240a933539f", "after_quota": "b86506e5b0664f54a6e0d95366f82 |
| 6825 | 2026-10-11 03:05:19 | b86506e5 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6826 | 2026-10-11 03:05:21 | 99e9bd34 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6827 | 2026-10-11 03:17:43 | 99e9bd34 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 74s [d |
| 6828 | 2026-10-11 03:17:43 | 99e9bd34 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 74s [d |
| 6829 | 2026-10-11 03:17:43 | 058d6b65 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5fd9d18c4aa1414aafe3e0fba01dde29", "after_quota": "99e9bd34f90c408caa180e68bf1a6 |
| 6830 | 2026-10-11 03:17:43 | 99e9bd34 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6831 | 2026-10-11 03:17:43 | 21d8755c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6832 | 2026-10-11 03:30:04 | 21d8755c | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 53s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6833 | 2026-10-11 03:30:04 | 21d8755c | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 53s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6834 | 2026-10-11 03:30:04 | ba222abd | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "9aa0054ee0124b40bb21b2daef2bc049", "after_quota": "21d8755c2f2e4cba938763fe77141 |
| 6835 | 2026-10-11 03:30:04 | 21d8755c | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6836 | 2026-10-11 03:30:05 | fba5e31f | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6837 | 2026-10-11 03:30:24 | b9848c6f |  | job.enqueued | nightly-task | {"kind": "monitor", "payload": {"only": null, "day": "2026-10-11"}} |
| 6838 | 2026-10-11 03:30:28 | b9848c6f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6839 | 2026-10-11 03:30:28 | ad05ad78 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "b9848c6f9e244793b86bd8b0a5d38f4c", "day": "2026-10-11"}} |
| 6840 | 2026-10-11 03:30:28 | f73eab2f | 031 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "031", "monitor_of": "b9848c6f9e244793b86bd8b0a5d38f4c", "day": "2026-10-11"}} |
| 6841 | 2026-10-11 03:30:28 | b9848c6f |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "031"], "jobs": ["ad05ad78", "f73eab2f"]} |
| 6842 | 2026-10-11 03:30:28 | b9848c6f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6843 | 2026-10-11 03:30:33 | f73eab2f | 031 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6844 | 2026-10-11 03:31:53 | f73eab2f | 031 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 14s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\031.json' \| T2 PASS 24s [done] expect='3' la |
| 6845 | 2026-10-11 03:31:53 | f73eab2f | 031 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 14s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\031.json' \| T2 PASS 24s [done] expect='3' la |
| 6846 | 2026-10-11 03:31:53 | 05dbd693 | 031 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "031", "retest_of": "f73eab2fa56d400f92a706f35b25d869", "after_quota": "f73eab2fa56d400f92a706f35b25d |
| 6847 | 2026-10-11 03:31:53 | f73eab2f | 031 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "031", "status": "active", "verified": "VERIFIED"}} |
| 6848 | 2026-10-11 03:42:41 | fba5e31f | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 42s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 65s [d |
| 6849 | 2026-10-11 03:42:41 | fba5e31f | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 42s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 65s [d |
| 6850 | 2026-10-11 03:42:41 | 926fd491 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "fba5e31f135848278879bf4ec6d1d |
| 6851 | 2026-10-11 03:42:41 | fba5e31f | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6852 | 2026-10-11 03:42:44 | 8233aee4 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6853 | 2026-10-11 03:54:42 | 8233aee4 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6854 | 2026-10-11 03:54:42 | 8233aee4 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6855 | 2026-10-11 03:54:42 | abdda5ab | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a5c9b2241151489ea85e56994e87fa75", "after_quota": "8233aee48e6c495eb63ab4856f2bc |
| 6856 | 2026-10-11 03:54:42 | 8233aee4 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6857 | 2026-10-11 03:54:46 | 1c8e370f | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6858 | 2026-10-11 03:55:18 | ff19a2e8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6859 | 2026-10-11 03:55:18 | 320a334f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-11T04"}} |
| 6860 | 2026-10-11 03:55:49 | ff19a2e8 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 6861 | 2026-10-11 03:55:49 | 5be95d54 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-11", "trigger": "blocked:gemini-flash36"}} |
| 6862 | 2026-10-11 03:55:49 | 6f4506ec |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-11", "trigger": "blocked:gemini-flash36"}} |
| 6863 | 2026-10-11 03:55:49 | 5a0786b6 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-11", "trigger": "blocked:gemini-flash36"}} |
| 6864 | 2026-10-11 03:55:49 | 87387045 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-11", "trigger": "blocked:gemini-flash36"}} |
| 6865 | 2026-10-11 03:55:49 | 5aade554 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-11", "trigger": "blocked:gemini-flash36"}} |
| 6866 | 2026-10-11 03:55:49 | 071541d0 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-11", "trigger": "blocked:gemini-flash36"}} |
| 6867 | 2026-10-11 03:55:49 | ff19a2e8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite |
| 6868 | 2026-10-11 03:55:53 | 5be95d54 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6869 | 2026-10-11 03:55:54 | 5be95d54 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 6870 | 2026-10-11 03:55:56 | 6f4506ec |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6871 | 2026-10-11 03:55:57 | 6f4506ec |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 6872 | 2026-10-11 03:56:00 | ca865945 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6873 | 2026-10-11 03:56:00 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 6874 | 2026-10-11 03:56:00 | c52204df |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-11T04"}} |
| 6875 | 2026-10-11 03:56:00 | ca865945 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6876 | 2026-10-11 03:56:03 | 5a0786b6 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6877 | 2026-10-11 03:56:04 | 5a0786b6 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 6878 | 2026-10-11 03:56:07 | 87387045 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6879 | 2026-10-11 03:56:07 | 87387045 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6880 | 2026-10-11 03:56:10 | 5aade554 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6881 | 2026-10-11 03:56:10 | 5aade554 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6882 | 2026-10-11 03:56:14 | 071541d0 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6883 | 2026-10-11 03:56:14 | 071541d0 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6884 | 2026-10-11 04:06:43 | 1c8e370f | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 62s [d |
| 6885 | 2026-10-11 04:06:43 | 1c8e370f | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 62s [d |
| 6886 | 2026-10-11 04:06:43 | db0fe640 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "c6d15792faef4854ae2126211a52cb62", "after_quota": "1c8e370fb6924f54ae3ea6028a516 |
| 6887 | 2026-10-11 04:06:43 | 1c8e370f | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6888 | 2026-10-11 04:06:43 | 433b41a9 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6889 | 2026-10-11 04:18:16 | 433b41a9 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 6890 | 2026-10-11 04:18:16 | 433b41a9 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 6891 | 2026-10-11 04:18:16 | 0689a1f2 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "062a8aeee53a43b2acb9a934d07fbf4b", "after_quota": "433b41a9deae41a6ae270d85c83e0 |
| 6892 | 2026-10-11 04:18:16 | 433b41a9 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6893 | 2026-10-11 04:18:18 | 9ce5ad7b | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6894 | 2026-10-11 04:30:53 | 9ce5ad7b | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6895 | 2026-10-11 04:30:53 | 9ce5ad7b | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6896 | 2026-10-11 04:30:53 | 7241e219 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "139734ae344e49089147d3f47942ffc6", "after_quota": "9ce5ad7bf25f4eeeaffe2d92d9de1 |
| 6897 | 2026-10-11 04:30:53 | 9ce5ad7b | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6898 | 2026-10-11 04:30:55 | 1f7039b7 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6899 | 2026-10-11 04:42:53 | 1f7039b7 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 6900 | 2026-10-11 04:42:53 | 1f7039b7 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 6901 | 2026-10-11 04:42:53 | f3e3352b | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "41923cc5baaa4b7ba7c14909b7abe137", "after_quota": "1f7039b7cfea4594a44159cfca22e |
| 6902 | 2026-10-11 04:42:53 | 1f7039b7 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6903 | 2026-10-11 04:42:57 | f62aa317 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6904 | 2026-10-11 04:55:18 | 320a334f |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6905 | 2026-10-11 04:55:18 | 776921fd |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-11T05"}} |
| 6906 | 2026-10-11 04:55:19 | f62aa317 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 72s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 6907 | 2026-10-11 04:55:19 | f62aa317 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 72s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 6908 | 2026-10-11 04:55:19 | a35c8dd3 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "f62aa317954041e7b44962a821448 |
| 6909 | 2026-10-11 04:55:19 | f62aa317 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6910 | 2026-10-11 04:55:22 | 1fb2187f | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6911 | 2026-10-11 04:56:10 | 320a334f |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 6912 | 2026-10-11 04:56:10 | 320a334f |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 6913 | 2026-10-11 04:56:14 | c52204df |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6914 | 2026-10-11 04:56:14 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 6915 | 2026-10-11 04:56:14 | f50db38d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-11T05"}} |
| 6916 | 2026-10-11 04:56:14 | c52204df |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6917 | 2026-10-11 05:06:45 | 1fb2187f | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6918 | 2026-10-11 05:06:45 | 1fb2187f | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6919 | 2026-10-11 05:06:45 | ec79f13c | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fe371a05201e499c9cc16d620128e678", "after_quota": "1fb2187fcb4f4db9b22e350fd15bc |
| 6920 | 2026-10-11 05:06:45 | 1fb2187f | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6921 | 2026-10-11 05:06:48 | 63f3f6e0 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6922 | 2026-10-11 05:18:42 | 63f3f6e0 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 6923 | 2026-10-11 05:18:42 | 63f3f6e0 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 6924 | 2026-10-11 05:18:42 | 26da8c48 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "b55e8b342b7b4b37acedb240a933539f", "after_quota": "63f3f6e0cc8141b392367fa904f3a |
| 6925 | 2026-10-11 05:18:42 | 63f3f6e0 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6926 | 2026-10-11 05:18:44 | 058d6b65 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6927 | 2026-10-11 05:30:32 | 058d6b65 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6928 | 2026-10-11 05:30:32 | 058d6b65 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6929 | 2026-10-11 05:30:32 | adaf4c56 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5fd9d18c4aa1414aafe3e0fba01dde29", "after_quota": "058d6b65ffe7426b84a6a70c40b31 |
| 6930 | 2026-10-11 05:30:32 | 058d6b65 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6931 | 2026-10-11 05:30:35 | ba222abd | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6932 | 2026-10-11 05:31:56 | 05dbd693 | 031 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6933 | 2026-10-11 05:32:51 | 05dbd693 | 031 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 4s [done] expect='X_OK' last='' \| T2 PASS 18s [done] expect='3' last='RESULT: 3' \| T3 PASS 16s [done] expect='2' last= |
| 6934 | 2026-10-11 05:32:51 | 05dbd693 | 031 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 4s [done] expect='X_OK' last='' \| T2 PASS 18s [done] expect='3' last='RESULT: 3' \| T3 PASS 16s [done] expect='2' last= |
| 6935 | 2026-10-11 05:32:51 | 05dbd693 | 031 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 6936 | 2026-10-11 05:32:51 | ed2020a0 | 031 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "031", "max_rounds": 2}} |
| 6937 | 2026-10-11 05:32:51 | 05dbd693 | 031 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "031", "status": "testing", "verified": "UNVERIFIED"}} |
| 6938 | 2026-10-11 05:42:47 | ba222abd | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 29s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 63s [d |
| 6939 | 2026-10-11 05:42:47 | ba222abd | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 29s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 63s [d |
| 6940 | 2026-10-11 05:42:47 | df7e22b9 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "9aa0054ee0124b40bb21b2daef2bc049", "after_quota": "ba222abd7ddb496383e0700f44b2d |
| 6941 | 2026-10-11 05:42:47 | ba222abd | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6942 | 2026-10-11 05:42:50 | 926fd491 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6943 | 2026-10-11 05:42:50 | ed2020a0 | 031 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6944 | 2026-10-11 05:43:58 | ed2020a0 | 031 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 6945 | 2026-10-11 05:43:58 | ed2020a0 | 031 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 6946 | 2026-10-11 05:43:58 | ed2020a0 | 031 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "031", "status": "active"}} |
| 6947 | 2026-10-11 05:54:49 | 926fd491 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 6948 | 2026-10-11 05:54:49 | 926fd491 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 6949 | 2026-10-11 05:54:49 | 99b7c926 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "926fd491a7f041518efd268bff5ad |
| 6950 | 2026-10-11 05:54:49 | 926fd491 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6951 | 2026-10-11 05:54:53 | abdda5ab | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6952 | 2026-10-11 05:55:19 | 776921fd |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6953 | 2026-10-11 05:55:19 | b33c79d0 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-11T06"}} |
| 6954 | 2026-10-11 05:55:33 | 776921fd |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 6955 | 2026-10-11 05:55:33 | 3c2b0478 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-11", "trigger": "blocked:gemini-flash36"}} |
| 6956 | 2026-10-11 05:55:33 | 61c91ee7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-11", "trigger": "blocked:gemini-flash36"}} |
| 6957 | 2026-10-11 05:55:33 | 416d19ce |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-11", "trigger": "blocked:gemini-flash36"}} |
| 6958 | 2026-10-11 05:55:33 | 42acc990 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-11", "trigger": "blocked:gemini-flash36"}} |
| 6959 | 2026-10-11 05:55:33 | 88d5c990 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-11", "trigger": "blocked:gemini-flash36"}} |
| 6960 | 2026-10-11 05:55:34 | 7ebb4e0c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-11", "trigger": "blocked:gemini-flash36"}} |
| 6961 | 2026-10-11 05:55:34 | 776921fd |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gpto |
| 6962 | 2026-10-11 05:55:37 | 3c2b0478 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6963 | 2026-10-11 05:55:37 | 3c2b0478 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 6964 | 2026-10-11 05:55:40 | 61c91ee7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6965 | 2026-10-11 05:55:40 | 61c91ee7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6966 | 2026-10-11 05:55:43 | 416d19ce |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6967 | 2026-10-11 05:55:43 | 416d19ce |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6968 | 2026-10-11 05:55:46 | 42acc990 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6969 | 2026-10-11 05:55:46 | 42acc990 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6970 | 2026-10-11 05:55:49 | 88d5c990 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6971 | 2026-10-11 05:55:49 | 88d5c990 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6972 | 2026-10-11 05:55:52 | 7ebb4e0c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6973 | 2026-10-11 05:55:52 | 7ebb4e0c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6974 | 2026-10-11 05:56:16 | f50db38d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6975 | 2026-10-11 05:56:16 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 6976 | 2026-10-11 05:56:16 | 8cb8eb01 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-11T06"}} |
| 6977 | 2026-10-11 05:56:16 | f50db38d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6978 | 2026-10-11 06:06:46 | abdda5ab | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 6979 | 2026-10-11 06:06:46 | abdda5ab | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 6980 | 2026-10-11 06:06:46 | 4c91245e | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a5c9b2241151489ea85e56994e87fa75", "after_quota": "abdda5ab139845ef84d2fdf4347c3 |
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
