# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
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
| 5815 | 2026-10-09 05:43:33 | 9aa0054e | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 5816 | 2026-10-09 05:43:33 | 9aa0054e | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 5817 | 2026-10-09 05:43:33 | 8453fea8 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "9aa0054ee0124b40bb21b2daef2bc049", "after_quota": "9aa0054ee0124b40bb21b2daef2bc |
| 5818 | 2026-10-09 05:43:33 | 9aa0054e | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5819 | 2026-10-09 05:43:37 | ab79dd5a | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5820 | 2026-10-09 05:55:23 | ab79dd5a | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 5821 | 2026-10-09 05:55:23 | ab79dd5a | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 5822 | 2026-10-09 05:55:23 | 219a2f98 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "df24e745ca8143daad1c58a7c3f21ddd", "after_quota": "ab79dd5af55345e0a166f2bce61e4 |
| 5823 | 2026-10-09 05:55:23 | ab79dd5a | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5824 | 2026-10-09 05:55:23 | c13e8ff5 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5825 | 2026-10-09 06:06:02 | c13e8ff5 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 5826 | 2026-10-09 06:06:02 | c13e8ff5 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 5827 | 2026-10-09 06:06:02 | 3048facf | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "c13e8ff530e14f93a608eef9b6b40 |
| 5828 | 2026-10-09 06:06:02 | c13e8ff5 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5829 | 2026-10-09 06:06:03 | 24b6cef5 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5830 | 2026-10-09 06:18:10 | 24b6cef5 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 74s [d |
| 5831 | 2026-10-09 06:18:10 | 24b6cef5 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 74s [d |
| 5832 | 2026-10-09 06:18:10 | cf5fe0c5 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "41923cc5baaa4b7ba7c14909b7abe137", "after_quota": "24b6cef5a067486aaf0820b7d5bc1 |
| 5833 | 2026-10-09 06:18:10 | 24b6cef5 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5834 | 2026-10-09 06:18:12 | 9e61efc1 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5835 | 2026-10-09 06:30:02 | 9e61efc1 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 63s [done] report expect='FACTORY' cmd=True \| T3 PASS 73s [d |
| 5836 | 2026-10-09 06:30:02 | 9e61efc1 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 63s [done] report expect='FACTORY' cmd=True \| T3 PASS 73s [d |
| 5837 | 2026-10-09 06:30:02 | 1f4dcd39 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "9e61efc19b66483ca5a3bf4ccca42 |
| 5838 | 2026-10-09 06:30:02 | 9e61efc1 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5839 | 2026-10-09 06:30:05 | b55e8b34 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5840 | 2026-10-09 06:30:57 | 7a5370a7 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5841 | 2026-10-09 06:30:57 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5842 | 2026-10-09 06:30:57 | 8f5a6c18 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-09T07"}} |
| 5843 | 2026-10-09 06:30:57 | 7a5370a7 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5844 | 2026-10-09 06:31:01 | 2bf3f44f |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5845 | 2026-10-09 06:31:01 | f8c017c1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T07"}} |
| 5846 | 2026-10-09 06:31:41 | 2bf3f44f |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 5847 | 2026-10-09 06:31:41 | 35e93443 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5848 | 2026-10-09 06:31:41 | 7deaadb5 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5849 | 2026-10-09 06:31:41 | 08611fe2 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5850 | 2026-10-09 06:31:41 | 532fd488 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5851 | 2026-10-09 06:31:41 | 8acb0163 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5852 | 2026-10-09 06:31:41 | f3dbc5c1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5853 | 2026-10-09 06:31:41 | 2bf3f44f |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gem |
| 5854 | 2026-10-09 06:31:45 | 35e93443 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5855 | 2026-10-09 06:31:46 | 35e93443 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5856 | 2026-10-09 06:31:49 | 7deaadb5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5857 | 2026-10-09 06:31:49 | 7deaadb5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5858 | 2026-10-09 06:31:53 | 08611fe2 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5859 | 2026-10-09 06:31:53 | 08611fe2 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5860 | 2026-10-09 06:31:57 | 532fd488 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5861 | 2026-10-09 06:31:57 | 532fd488 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5862 | 2026-10-09 06:32:01 | 8acb0163 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5863 | 2026-10-09 06:32:01 | 8acb0163 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5864 | 2026-10-09 06:32:04 | f3dbc5c1 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5865 | 2026-10-09 06:32:04 | f3dbc5c1 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5866 | 2026-10-09 06:42:03 | b55e8b34 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 5867 | 2026-10-09 06:42:03 | b55e8b34 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 5868 | 2026-10-09 06:42:03 | b24ff203 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "b55e8b342b7b4b37acedb240a933539f", "after_quota": "b55e8b342b7b4b37acedb240a9335 |
| 5869 | 2026-10-09 06:42:03 | b55e8b34 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5870 | 2026-10-09 06:42:04 | be435166 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5871 | 2026-10-09 06:54:36 | be435166 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 5872 | 2026-10-09 06:54:36 | be435166 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 5873 | 2026-10-09 06:54:36 | be435166 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5874 | 2026-10-09 06:54:36 | 5fd9d18c | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "c440dca6e7ce4de1bbf56dcbf0b9a042", "retry_of": "be4351667ade4af9ac7beed175cd327 |
| 5875 | 2026-10-09 06:54:36 | be435166 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5876 | 2026-10-09 07:07:58 | 32fc3cea | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5877 | 2026-10-09 07:20:34 | 32fc3cea | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 65s [d |
| 5878 | 2026-10-09 07:20:34 | 32fc3cea | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 65s [d |
| 5879 | 2026-10-09 07:20:34 | d64d5f43 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "dc90fd03027d4e1a9270d756d6532ee9", "after_quota": "32fc3cea4efa488abcbeb0500c2dc |
| 5880 | 2026-10-09 07:20:34 | 32fc3cea | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5881 | 2026-10-09 07:20:37 | a3c0bdb6 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5882 | 2026-10-09 07:30:59 | 8f5a6c18 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5883 | 2026-10-09 07:30:59 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5884 | 2026-10-09 07:31:00 | f6a97e54 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-09T08"}} |
| 5885 | 2026-10-09 07:31:00 | 8f5a6c18 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5886 | 2026-10-09 07:31:04 | f8c017c1 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5887 | 2026-10-09 07:31:04 | 3b16ced2 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T08"}} |
| 5888 | 2026-10-09 07:31:29 | f8c017c1 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "groq-g |
| 5889 | 2026-10-09 07:35:31 | a3c0bdb6 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 65s [d |
| 5890 | 2026-10-09 07:35:31 | a3c0bdb6 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 65s [d |
| 5891 | 2026-10-09 07:35:31 | 6e21e735 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a8dfa7853d6241f1ab5469b02c857c1b", "after_quota": "a3c0bdb65aa14df0bc1b3d63554ea |
| 5892 | 2026-10-09 07:35:31 | a3c0bdb6 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5893 | 2026-10-09 07:35:34 | 5fd9d18c | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5894 | 2026-10-09 07:47:52 | 5fd9d18c | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 74s [d |
| 5895 | 2026-10-09 07:47:52 | 5fd9d18c | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 74s [d |
| 5896 | 2026-10-09 07:47:52 | 909d4e4b | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5fd9d18c4aa1414aafe3e0fba01dde29", "after_quota": "5fd9d18c4aa1414aafe3e0fba01dd |
| 5897 | 2026-10-09 07:47:52 | 5fd9d18c | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5898 | 2026-10-09 07:47:56 | 88ac2dd8 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5899 | 2026-10-09 08:00:04 | 88ac2dd8 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 63s [d |
| 5900 | 2026-10-09 08:00:04 | 88ac2dd8 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 63s [d |
| 5901 | 2026-10-09 08:00:04 | d9e6e57e | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ab5d10624c564c16b855f074ef29fa09", "after_quota": "88ac2dd830324a22b756fed00ec9d |
| 5902 | 2026-10-09 08:00:04 | 88ac2dd8 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5903 | 2026-10-09 08:00:07 | 8453fea8 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5904 | 2026-10-09 08:12:09 | 8453fea8 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 62s [done] report expect='FACTORY' cmd=True \| T3 PASS 83s [d |
| 5905 | 2026-10-09 08:12:09 | 8453fea8 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 62s [done] report expect='FACTORY' cmd=True \| T3 PASS 83s [d |
| 5906 | 2026-10-09 08:12:09 | d13e7377 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "9aa0054ee0124b40bb21b2daef2bc049", "after_quota": "8453fea8f5f94c1897d3cc9111c9a |
| 5907 | 2026-10-09 08:12:09 | 8453fea8 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5908 | 2026-10-09 08:12:11 | 219a2f98 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5909 | 2026-10-09 09:23:06 | f6a97e54 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5910 | 2026-10-09 09:23:07 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5911 | 2026-10-09 09:23:13 | f9604c42 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-09T10"}} |
| 5912 | 2026-10-09 09:23:13 | f6a97e54 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5913 | 2026-10-09 09:23:14 | 3b16ced2 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5914 | 2026-10-09 09:23:14 | 03b06039 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T10"}} |
| 5915 | 2026-10-09 09:23:14 | 3b16ced2 |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 5916 | 2026-10-09 09:23:14 | 6b52f660 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T08-retry", "retry_of": "3b16ced204a34abc8b33532b7726d6fc"}} |
| 5917 | 2026-10-09 09:23:14 | 3b16ced2 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5918 | 2026-10-09 09:26:03 | 219a2f98 | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 5919 | 2026-10-09 09:26:04 | 3048facf | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5920 | 2026-10-09 09:33:16 | 6b52f660 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5921 | 2026-10-09 09:33:16 | 03b06039 |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 5922 | 2026-10-09 09:33:16 | 6b52f660 |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 5923 | 2026-10-09 09:33:16 | ff999b86 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T08-retry-retry", "retry_of": "6b52f660a3db446da69ec94946a3e976"}} |
| 5924 | 2026-10-09 09:33:16 | 6b52f660 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5925 | 2026-10-09 09:43:18 | ff999b86 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5926 | 2026-10-09 09:43:18 | 03b06039 |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 5927 | 2026-10-09 09:43:18 | ff999b86 |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 5928 | 2026-10-09 09:43:18 | 29c2f4f1 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T08-retry-retry-retry", "retry_of": "ff999b86af5e4eafa8963de9295e3bc2"}} |
| 5929 | 2026-10-09 09:43:18 | ff999b86 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5930 | 2026-10-09 09:48:10 | 3048facf | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 5931 | 2026-10-09 09:48:10 | 219a2f98 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 5932 | 2026-10-09 09:53:20 | 29c2f4f1 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5933 | 2026-10-09 09:53:20 | 03b06039 |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 5934 | 2026-10-09 09:53:20 | 29c2f4f1 |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 5935 | 2026-10-09 09:53:20 | 675ecaff |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T08-retry-retry-retry-retry", "retry_of": "29c2f4f1914a40ff95bd81695431a112"}} |
| 5936 | 2026-10-09 09:53:20 | 29c2f4f1 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5937 | 2026-10-09 10:03:21 | 675ecaff |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5938 | 2026-10-09 10:03:21 | fc108045 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T11"}} |
| 5939 | 2026-10-09 10:03:22 | 675ecaff |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 5940 | 2026-10-09 10:03:22 | 5bf7d78e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T08-retry-retry-retry-retry-retry", "retry_of": "675ecaff3d7240728583eacb53de20 |
| 5941 | 2026-10-09 10:03:22 | 675ecaff |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5942 | 2026-10-09 10:07:04 | 219a2f98 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 50s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 102s [done] report expect='FACTORY' cmd=False \| T3 FAIL 153s |
| 5943 | 2026-10-09 10:07:04 | 219a2f98 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 50s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 102s [done] report expect='FACTORY' cmd=False \| T3 FAIL 153s |
| 5944 | 2026-10-09 10:07:04 | 219a2f98 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5945 | 2026-10-09 10:07:04 | d2e1729a | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "076d00557198429696acd4c0a35af210", "retry_of": "219a2f98f6f04bb3b405b78d566c516 |
| 5946 | 2026-10-09 10:07:04 | 219a2f98 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 2, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5947 | 2026-10-09 10:07:05 | 3048facf | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 5948 | 2026-10-09 10:13:23 | 5bf7d78e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5949 | 2026-10-09 10:13:23 | fc108045 |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 5950 | 2026-10-09 10:14:01 | 5bf7d78e |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 5951 | 2026-10-09 10:14:01 | 5bf7d78e |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemi |
| 5952 | 2026-10-09 11:00:40 | 3048facf |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 5953 | 2026-10-09 11:00:40 | f9604c42 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5954 | 2026-10-09 11:00:40 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5955 | 2026-10-09 16:46:17 | 549088bf |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-09T17"}} |
| 5956 | 2026-10-09 16:46:17 | f9604c42 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5957 | 2026-10-09 16:46:33 | 03b06039 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5958 | 2026-10-09 16:46:33 | e6aca474 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T17"}} |
| 5959 | 2026-10-09 16:47:01 | 3048facf |  | job.readopted | fast-LAPTOP-LRE6PSA8 | {} |
| 5960 | 2026-10-09 16:47:10 | 03b06039 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 5961 | 2026-10-09 16:47:10 | 03b06039 |  | model.retired | svc-LAPTOP-LRE6PSA8 | {"model": "or-qwen27b", "reason": "gone: {\"error\":{\"message\":\"this model is unavailable for free. the paid version "} |
| 5962 | 2026-10-09 16:47:10 | c29eaa2f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5963 | 2026-10-09 16:47:10 | 33a31532 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5964 | 2026-10-09 16:47:10 | e936f60b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5965 | 2026-10-09 16:47:10 | 39daa754 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5966 | 2026-10-09 16:47:10 | 31ae098a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5967 | 2026-10-09 16:47:10 | f5737aa7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5968 | 2026-10-09 16:47:10 | 03b06039 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gem |
| 5969 | 2026-10-09 16:47:18 | fc108045 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5970 | 2026-10-09 16:47:18 | e6aca474 |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 5971 | 2026-10-09 20:03:56 | fc108045 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 5972 | 2026-10-09 20:03:56 | fc108045 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-lite", "gemin |
| 5973 | 2026-10-09 20:04:03 | 549088bf |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5974 | 2026-10-09 20:04:03 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5975 | 2026-10-09 20:04:05 | 87def55d |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-09T21"}} |
| 5976 | 2026-10-09 20:04:05 | 549088bf |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5977 | 2026-10-09 20:04:10 | e6aca474 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5978 | 2026-10-09 20:04:10 | a6976a83 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T21"}} |
| 5979 | 2026-10-09 20:04:44 | e6aca474 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 5980 | 2026-10-09 20:04:44 | cd4c40bf |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5981 | 2026-10-09 20:04:44 | 5d58fd62 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5982 | 2026-10-09 20:04:44 | 9611c951 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5983 | 2026-10-09 20:04:44 | 2b21b01f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5984 | 2026-10-09 20:04:44 | 9f3b0120 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5985 | 2026-10-09 20:04:44 | 4311cd1f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-09", "trigger": "blocked:gemini-flash36"}} |
| 5986 | 2026-10-09 20:04:44 | e6aca474 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gem |
| 5987 | 2026-10-09 20:04:51 | c29eaa2f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5988 | 2026-10-09 20:04:52 | c29eaa2f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5989 | 2026-10-09 20:04:59 | 33a31532 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5990 | 2026-10-09 20:05:00 | 33a31532 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5991 | 2026-10-09 20:05:06 | e936f60b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5992 | 2026-10-09 20:05:08 | e936f60b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5993 | 2026-10-09 20:05:14 | 39daa754 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5994 | 2026-10-09 20:05:14 | 39daa754 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5995 | 2026-10-09 20:05:20 | 31ae098a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5996 | 2026-10-09 20:05:20 | 31ae098a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5997 | 2026-10-09 20:05:27 | f5737aa7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5998 | 2026-10-09 20:05:27 | f5737aa7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5999 | 2026-10-09 20:05:32 | cd4c40bf |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6000 | 2026-10-09 20:05:34 | cd4c40bf |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 6001 | 2026-10-09 20:05:40 | 5d58fd62 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6002 | 2026-10-09 20:05:40 | 5d58fd62 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6003 | 2026-10-09 20:05:47 | 9611c951 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6004 | 2026-10-09 20:05:47 | 9611c951 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6005 | 2026-10-09 20:05:54 | 2b21b01f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6006 | 2026-10-09 20:05:54 | 2b21b01f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6007 | 2026-10-09 20:05:59 | 9f3b0120 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6008 | 2026-10-09 20:05:59 | 9f3b0120 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6009 | 2026-10-09 20:06:06 | 4311cd1f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6010 | 2026-10-09 20:06:06 | 4311cd1f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6011 | 2026-10-09 20:06:12 | d8bda1e9 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6012 | 2026-10-09 20:06:13 | d8bda1e9 |  | audit.verified | svc-LAPTOP-LRE6PSA8 | {"rows": 6010, "hashed": 5258, "first_bad": null} |
| 6013 | 2026-10-09 20:06:13 | ef09c4af |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-10-10"}} |
| 6014 | 2026-10-09 20:06:13 | 862feac2 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-10-09"}} |
| 6015 | 2026-10-09 20:06:13 | b8ad7bb0 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-10-09"}} |
| 6016 | 2026-10-09 20:06:13 | d8bda1e9 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6017 | 2026-10-09 20:06:19 | 862feac2 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6018 | 2026-10-09 20:07:09 | 3048facf | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 6019 | 2026-10-09 20:07:16 | d2e1729a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6020 | 2026-10-09 20:15:18 | 862feac2 |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "gemini-flash", "result": "1/4", "quota": 0, "secs": 175} |
| 6021 | 2026-10-09 20:15:18 | 862feac2 |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "gemini-flash38", "result": "1/4", "quota": 0, "secs": 286} |
| 6022 | 2026-10-09 20:15:18 | 862feac2 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["gemini-flash", "1/4"], ["gemini-flash38", "1/4"]]}} |
| 6023 | 2026-10-09 20:15:26 | b8ad7bb0 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6024 | 2026-10-09 20:16:18 | b8ad7bb0 |  | factory.canary | svc-LAPTOP-LRE6PSA8 | {"verdict": "FAIL", "lane": "groq:openai/gpt-oss-20b", "chain": ["groq-gptoss120b", "groq-gptoss20b", "gemini-gemma26b", "gemini-gemini-flas |
| 6025 | 2026-10-09 20:16:18 | b8ad7bb0 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"pass": 2, "total": 3}} |
| 6026 | 2026-10-09 20:26:48 | d2e1729a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 119s [done] report expect='FACTORY' cmd=True \| T3 FAIL 246s  |
| 6027 | 2026-10-09 20:26:48 | d2e1729a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 119s [done] report expect='FACTORY' cmd=True \| T3 FAIL 246s  |
| 6028 | 2026-10-09 20:26:48 | cceb6137 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "d2e1729a75cc4dd499e5716e334fcec1", "after_quota": "d2e1729a75cc4dd499e5716e334fc |
| 6029 | 2026-10-09 20:26:48 | d2e1729a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6030 | 2026-10-09 20:26:49 | 3048facf | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 6031 | 2026-10-09 20:41:17 | 3048facf | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 42s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 78s [d |
| 6032 | 2026-10-09 20:41:17 | 3048facf | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 42s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 78s [d |
| 6033 | 2026-10-09 20:41:17 | 7effb335 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "3048facf4636448ca33f4f42d0aa0 |
| 6034 | 2026-10-09 20:41:17 | 3048facf | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6035 | 2026-10-09 20:41:18 | cf5fe0c5 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6036 | 2026-10-09 20:56:24 | cf5fe0c5 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 63s [done] report expect='FACTORY' cmd=True \| T3 PASS 76s [d |
| 6037 | 2026-10-09 20:56:24 | cf5fe0c5 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 63s [done] report expect='FACTORY' cmd=True \| T3 PASS 76s [d |
| 6038 | 2026-10-09 20:56:25 | 082d548a | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "41923cc5baaa4b7ba7c14909b7abe137", "after_quota": "cf5fe0c5079347d4b04147116ccc7 |
| 6039 | 2026-10-09 20:56:25 | cf5fe0c5 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6040 | 2026-10-09 20:56:29 | 1f4dcd39 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6041 | 2026-10-09 21:04:07 | 87def55d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6042 | 2026-10-09 21:04:07 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 6043 | 2026-10-09 21:04:13 | 14031ed8 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-09T22"}} |
| 6044 | 2026-10-09 21:04:13 | 87def55d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6045 | 2026-10-09 21:04:18 | a6976a83 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6046 | 2026-10-09 21:04:19 | bb314448 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T22"}} |
| 6047 | 2026-10-09 21:04:35 | a6976a83 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss1 |
| 6048 | 2026-10-09 21:09:30 | 1f4dcd39 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 73s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 6049 | 2026-10-09 21:09:30 | 1f4dcd39 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 73s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 6050 | 2026-10-09 21:09:30 | 7b939e15 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "1f4dcd39e38e4aac87567a6e555a9 |
| 6051 | 2026-10-09 21:09:30 | 1f4dcd39 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6052 | 2026-10-09 21:09:32 | b24ff203 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6053 | 2026-10-09 21:22:40 | b24ff203 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 42s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 6054 | 2026-10-09 21:22:40 | b24ff203 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 42s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 6055 | 2026-10-09 21:22:40 | 23700797 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "b55e8b342b7b4b37acedb240a933539f", "after_quota": "b24ff203ae844f19bff123d0eba97 |
| 6056 | 2026-10-09 21:22:40 | b24ff203 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6057 | 2026-10-09 21:22:44 | d64d5f43 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6058 | 2026-10-09 21:36:52 | d64d5f43 |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 6059 | 2026-10-09 21:36:52 | d64d5f43 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 6060 | 2026-10-09 21:46:47 | d64d5f43 | 001 | job.orphaned_result | svc-LAPTOP-LRE6PSA8 | {"error": "Command '['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', 'C:\\\\AI\\\\Factory\\\\repo\\\\scripts\\\\windows\\ |
| 6061 | 2026-10-09 21:53:58 | d64d5f43 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 251s [TIMEOUT] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 FAIL 10 |
| 6062 | 2026-10-09 21:53:58 | d64d5f43 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 251s [TIMEOUT] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 FAIL 10 |
| 6063 | 2026-10-09 21:53:58 | d64d5f43 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 6064 | 2026-10-09 21:53:58 | 63b3b071 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "f174fbc671544e27bad96250dd6ea9e2", "retry_of": "d64d5f438fba4a19bf4929f48d3b934 |
| 6065 | 2026-10-09 21:53:58 | d64d5f43 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 7, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6066 | 2026-10-09 21:54:02 | 6e21e735 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6067 | 2026-10-09 22:04:18 | 14031ed8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6068 | 2026-10-09 22:04:18 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 6069 | 2026-10-09 22:04:19 | bfd8b8ea |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-09T23"}} |
| 6070 | 2026-10-09 22:04:19 | 14031ed8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6071 | 2026-10-09 22:04:23 | bb314448 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6072 | 2026-10-09 22:04:23 | 838c36cb |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-09T23"}} |
| 6073 | 2026-10-09 22:05:07 | bb314448 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 6074 | 2026-10-09 22:05:07 | bb314448 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite |
| 6075 | 2026-10-09 22:06:32 | 6e21e735 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 79s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 6076 | 2026-10-09 22:06:32 | 6e21e735 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 79s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 6077 | 2026-10-09 22:06:32 | fac9e34b | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a8dfa7853d6241f1ab5469b02c857c1b", "after_quota": "6e21e735346d4ac4b792dc6cfeebf |
| 6078 | 2026-10-09 22:06:32 | 6e21e735 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
