# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 7844 | 2026-10-14 05:34:36 | 121a8faf |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7845 | 2026-10-14 05:34:36 | 121a8faf |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7846 | 2026-10-14 05:34:39 | e9160798 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7847 | 2026-10-14 05:34:40 | e9160798 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7848 | 2026-10-14 05:34:43 | b9d990b5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7849 | 2026-10-14 05:34:43 | b9d990b5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7850 | 2026-10-14 05:45:29 | 5efdb56b | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7851 | 2026-10-14 05:45:29 | a6414b9b | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7852 | 2026-10-14 06:07:47 | a6414b9b | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7853 | 2026-10-14 06:07:49 | 5efdb56b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 7854 | 2026-10-14 06:30:05 | 5efdb56b | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7855 | 2026-10-14 06:30:07 | a6414b9b | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 7856 | 2026-10-14 06:33:53 | 51e35987 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7857 | 2026-10-14 06:33:53 | 5f447373 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T07"}} |
| 7858 | 2026-10-14 06:34:13 | 51e35987 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 7859 | 2026-10-14 06:34:13 | 51e35987 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash38", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\ |
| 7860 | 2026-10-14 06:34:14 | b2ff79e3 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-14", "trigger": "blocked:gemini-flash38"}} |
| 7861 | 2026-10-14 06:34:14 | 24015a60 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-14", "trigger": "blocked:gemini-flash38"}} |
| 7862 | 2026-10-14 06:34:14 | aa27e63c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-14", "trigger": "blocked:gemini-flash38"}} |
| 7863 | 2026-10-14 06:34:14 | c4376025 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-14", "trigger": "blocked:gemini-flash38"}} |
| 7864 | 2026-10-14 06:34:14 | 3d55d0ca |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-14", "trigger": "blocked:gemini-flash38"}} |
| 7865 | 2026-10-14 06:34:14 | 6380611a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-14", "trigger": "blocked:gemini-flash38"}} |
| 7866 | 2026-10-14 06:34:14 | 51e35987 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini |
| 7867 | 2026-10-14 06:34:21 | 9b9bd998 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7868 | 2026-10-14 06:34:21 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7869 | 2026-10-14 06:34:21 | 1b256c30 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T07"}} |
| 7870 | 2026-10-14 06:34:21 | 9b9bd998 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7871 | 2026-10-14 06:34:28 | b2ff79e3 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7872 | 2026-10-14 06:34:29 | b2ff79e3 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7873 | 2026-10-14 06:34:35 | 24015a60 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7874 | 2026-10-14 06:34:35 | 24015a60 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7875 | 2026-10-14 06:34:39 | aa27e63c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7876 | 2026-10-14 06:34:39 | aa27e63c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7877 | 2026-10-14 06:34:43 | c4376025 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7878 | 2026-10-14 06:34:43 | c4376025 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7879 | 2026-10-14 06:34:46 | 3d55d0ca |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7880 | 2026-10-14 06:34:46 | 3d55d0ca |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7881 | 2026-10-14 06:34:50 | 6380611a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7882 | 2026-10-14 06:34:50 | 6380611a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7883 | 2026-10-14 06:52:25 | a6414b9b | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7884 | 2026-10-14 06:52:25 | 5efdb56b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 7885 | 2026-10-14 07:11:56 | 5efdb56b | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 75s [d |
| 7886 | 2026-10-14 07:11:56 | 5efdb56b | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 75s [d |
| 7887 | 2026-10-14 07:11:56 | 5efdb56b | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7888 | 2026-10-14 07:11:56 | 773c8a3b | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "5efdb56bee7e4b39a17a58573ececd2 |
| 7889 | 2026-10-14 07:11:56 | 5efdb56b | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7890 | 2026-10-14 07:11:57 | a6414b9b | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 7891 | 2026-10-14 07:30:54 | a6414b9b | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 209s [done] report expect='FACTORY' cmd=True \| T3 PASS 153s  |
| 7892 | 2026-10-14 07:30:54 | a6414b9b | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 209s [done] report expect='FACTORY' cmd=True \| T3 PASS 153s  |
| 7893 | 2026-10-14 07:30:54 | a6414b9b | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7894 | 2026-10-14 07:30:54 | fefd1328 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "76b09e8217e8440b9a0f1bc14f76a1be", "retry_of": "a6414b9b2652444d8a6d1bacb9ecfa1 |
| 7895 | 2026-10-14 07:30:54 | a6414b9b | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7896 | 2026-10-14 07:30:57 | 35fdd956 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7897 | 2026-10-14 07:33:54 | 5f447373 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7898 | 2026-10-14 07:33:54 | 41febb49 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T08"}} |
| 7899 | 2026-10-14 07:36:07 | 5f447373 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gpto |
| 7900 | 2026-10-14 07:36:12 | 1b256c30 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7901 | 2026-10-14 07:36:12 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7902 | 2026-10-14 07:36:13 | 83ce1d18 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T08"}} |
| 7903 | 2026-10-14 07:36:13 | 1b256c30 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7904 | 2026-10-14 07:49:04 | 35fdd956 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 84s [done] report expect='FACTORY' cmd=True \| T3 PASS 232s [ |
| 7905 | 2026-10-14 07:49:04 | 35fdd956 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 84s [done] report expect='FACTORY' cmd=True \| T3 PASS 232s [ |
| 7906 | 2026-10-14 07:49:04 | 56718df5 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5e3cb81dcaef415aa193471d2cd92af9", "after_quota": "35fdd956d07845faa3af01ff01bf2 |
| 7907 | 2026-10-14 07:49:04 | 35fdd956 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7908 | 2026-10-14 07:49:04 | 773c8a3b | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7909 | 2026-10-14 08:07:13 | 773c8a3b | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 122s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 73s [done] report expect='FACTORY' cmd=True \| T3 PASS 212s  |
| 7910 | 2026-10-14 08:07:13 | 773c8a3b | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 122s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 73s [done] report expect='FACTORY' cmd=True \| T3 PASS 212s  |
| 7911 | 2026-10-14 08:07:13 | e80bcd61 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "773c8a3bd76049e6b5a24b3e92ea65fc", "after_quota": "773c8a3bd76049e6b5a24b3e92ea6 |
| 7912 | 2026-10-14 08:07:13 | 773c8a3b | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7913 | 2026-10-14 08:07:15 | fefd1328 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7914 | 2026-10-14 08:23:13 | fefd1328 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 70s [done] report expect='FACTORY' cmd=True \| T3 PASS 98s [d |
| 7915 | 2026-10-14 08:23:13 | fefd1328 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 70s [done] report expect='FACTORY' cmd=True \| T3 PASS 98s [d |
| 7916 | 2026-10-14 08:23:13 | 214b4c30 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fefd132857c64f0d981f48b23770a2c5", "after_quota": "fefd132857c64f0d981f48b23770a |
| 7917 | 2026-10-14 08:23:13 | fefd1328 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7918 | 2026-10-14 08:23:13 | f876d821 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7919 | 2026-10-14 08:33:58 | 41febb49 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7920 | 2026-10-14 08:33:58 | cd310974 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T09"}} |
| 7921 | 2026-10-14 08:36:50 | 41febb49 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen2 |
| 7922 | 2026-10-14 08:36:56 | 83ce1d18 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7923 | 2026-10-14 08:36:57 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7924 | 2026-10-14 08:36:58 | 5831bd8f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T09"}} |
| 7925 | 2026-10-14 08:36:58 | 83ce1d18 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7926 | 2026-10-14 08:45:30 | f876d821 | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7927 | 2026-10-14 08:45:32 | 0ec74895 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7928 | 2026-10-14 09:07:51 | 0ec74895 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7929 | 2026-10-14 09:07:51 | f876d821 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 7930 | 2026-10-14 09:30:05 | f876d821 | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7931 | 2026-10-14 09:30:08 | 0ec74895 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 7932 | 2026-10-14 09:34:00 | cd310974 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7933 | 2026-10-14 09:34:00 | 0cbb7165 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T10"}} |
| 7934 | 2026-10-14 09:35:31 | cd310974 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\n  |
| 7935 | 2026-10-14 09:35:31 | cd310974 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "TimeoutError"} |
| 7936 | 2026-10-14 09:35:31 | 5be59b08 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-14", "trigger": "blocked:gemini-flash,gemini-flash-latest"}} |
| 7937 | 2026-10-14 09:35:31 | 31c84008 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-14", "trigger": "blocked:gemini-flash,gemini-flash-latest"}} |
| 7938 | 2026-10-14 09:35:31 | 8022dedc |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-14", "trigger": "blocked:gemini-flash,gemini-flash-latest"}} |
| 7939 | 2026-10-14 09:35:32 | f95d33a3 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-14", "trigger": "blocked:gemini-flash,gemini-flash-latest"}} |
| 7940 | 2026-10-14 09:35:32 | 210293d1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-14", "trigger": "blocked:gemini-flash,gemini-flash-latest"}} |
| 7941 | 2026-10-14 09:35:32 | 011e22ea |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-14", "trigger": "blocked:gemini-flash,gemini-flash-latest"}} |
| 7942 | 2026-10-14 09:35:32 | cd310974 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen2 |
| 7943 | 2026-10-14 09:35:36 | 5be59b08 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7944 | 2026-10-14 09:35:36 | 5be59b08 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7945 | 2026-10-14 09:35:40 | 31c84008 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7946 | 2026-10-14 09:35:41 | 31c84008 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7947 | 2026-10-14 09:35:45 | 8022dedc |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7948 | 2026-10-14 09:35:47 | 8022dedc |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7949 | 2026-10-14 09:35:54 | f95d33a3 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7950 | 2026-10-14 09:35:54 | f95d33a3 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7951 | 2026-10-14 09:36:01 | 210293d1 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7952 | 2026-10-14 09:36:01 | 210293d1 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7953 | 2026-10-14 09:36:06 | 011e22ea |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7954 | 2026-10-14 09:36:06 | 011e22ea |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7955 | 2026-10-14 09:37:00 | 5831bd8f |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7956 | 2026-10-14 09:37:00 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7957 | 2026-10-14 09:37:00 | 851644e8 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T10"}} |
| 7958 | 2026-10-14 09:37:00 | 5831bd8f |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7959 | 2026-10-14 09:52:20 | 0ec74895 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7960 | 2026-10-14 09:52:21 | f876d821 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 7961 | 2026-10-14 10:14:30 | f876d821 | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "failed", "attempt": 3, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7962 | 2026-10-14 10:14:31 | 0ec74895 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 7963 | 2026-10-14 10:34:05 | 0cbb7165 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7964 | 2026-10-14 10:34:05 | 15b6a9ef |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T11"}} |
| 7965 | 2026-10-14 10:35:34 | 0cbb7165 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 7966 | 2026-10-14 10:35:34 | 0cbb7165 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 7967 | 2026-10-14 10:35:34 | 0cbb7165 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash38", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 7968 | 2026-10-14 10:35:34 | 0cbb7165 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-gemma26b", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "TimeoutError"} |
| 7969 | 2026-10-14 10:35:34 | a11fa142 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-14", "trigger": "blocked:gemini-gemma26b"}} |
| 7970 | 2026-10-14 10:35:34 | 8594b03c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-14", "trigger": "blocked:gemini-gemma26b"}} |
| 7971 | 2026-10-14 10:35:34 | f20d577e |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-14", "trigger": "blocked:gemini-gemma26b"}} |
| 7972 | 2026-10-14 10:35:34 | 11758c44 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-14", "trigger": "blocked:gemini-gemma26b"}} |
| 7973 | 2026-10-14 10:35:34 | a269167e |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-14", "trigger": "blocked:gemini-gemma26b"}} |
| 7974 | 2026-10-14 10:35:34 | 91e0d319 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-14", "trigger": "blocked:gemini-gemma26b"}} |
| 7975 | 2026-10-14 10:35:34 | 0cbb7165 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-lite", "gemini- |
| 7976 | 2026-10-14 10:35:38 | a11fa142 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7977 | 2026-10-14 10:35:38 | a11fa142 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7978 | 2026-10-14 10:35:42 | 8594b03c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7979 | 2026-10-14 10:35:42 | 8594b03c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7980 | 2026-10-14 10:35:49 | f20d577e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7981 | 2026-10-14 10:35:49 | f20d577e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7982 | 2026-10-14 10:35:54 | 11758c44 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7983 | 2026-10-14 10:35:54 | 11758c44 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7984 | 2026-10-14 10:36:00 | a269167e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7985 | 2026-10-14 10:36:00 | a269167e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7986 | 2026-10-14 10:36:05 | 91e0d319 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7987 | 2026-10-14 10:36:05 | 91e0d319 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7988 | 2026-10-14 10:36:42 | 0ec74895 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "failed", "attempt": 3, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7989 | 2026-10-14 10:36:45 | ae80d13a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7990 | 2026-10-14 10:37:01 | 851644e8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7991 | 2026-10-14 10:37:01 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7992 | 2026-10-14 10:37:01 | c027b3b0 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T11"}} |
| 7993 | 2026-10-14 10:37:01 | 851644e8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7994 | 2026-10-14 10:52:06 | ae80d13a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 62s [done] report expect='FACTORY' cmd=True \| T3 PASS 63s [d |
| 7995 | 2026-10-14 10:52:06 | ae80d13a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 62s [done] report expect='FACTORY' cmd=True \| T3 PASS 63s [d |
| 7996 | 2026-10-14 10:52:06 | 7b5aa26d | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a5c9b2241151489ea85e56994e87fa75", "after_quota": "ae80d13a959f4992a85296926ad75 |
| 7997 | 2026-10-14 10:52:06 | ae80d13a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7998 | 2026-10-14 10:52:09 | fc146198 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7999 | 2026-10-14 11:04:26 | fc146198 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 8000 | 2026-10-14 11:04:26 | fc146198 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 8001 | 2026-10-14 11:04:26 | e32c1507 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "1c048b97a00941b4a0a2a31b29aec1c6", "after_quota": "fc1461982f254f77ba8c74e777b3c |
| 8002 | 2026-10-14 11:04:26 | fc146198 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8003 | 2026-10-14 11:04:30 | ceb330c7 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8004 | 2026-10-14 11:17:08 | ceb330c7 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 8005 | 2026-10-14 11:17:09 | ceb330c7 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 8006 | 2026-10-14 11:17:09 | f0a7add9 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "4940d9aa166d426aadfe8f833d27143c", "after_quota": "ceb330c7d0e44e3b85819725cc274 |
| 8007 | 2026-10-14 11:17:09 | ceb330c7 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8008 | 2026-10-14 11:17:11 | 529d6be2 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8009 | 2026-10-14 11:29:48 | 529d6be2 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 70s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 8010 | 2026-10-14 11:29:48 | 529d6be2 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 70s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 8011 | 2026-10-14 11:29:48 | e1bba806 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fe371a05201e499c9cc16d620128e678", "after_quota": "529d6be2a1a04290887eab70ed429 |
| 8012 | 2026-10-14 11:29:48 | 529d6be2 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8013 | 2026-10-14 11:29:52 | a8403e44 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8014 | 2026-10-14 11:34:08 | 15b6a9ef |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8015 | 2026-10-14 11:34:08 | 8188cb64 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T12"}} |
| 8016 | 2026-10-14 11:36:55 | 15b6a9ef |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemini-flash-lite-latest", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptoss2 |
| 8017 | 2026-10-14 11:37:03 | c027b3b0 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8018 | 2026-10-14 11:37:03 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8019 | 2026-10-14 11:37:04 | b22e199f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T12"}} |
| 8020 | 2026-10-14 11:37:04 | c027b3b0 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8021 | 2026-10-14 11:42:41 | a8403e44 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 64s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 63s [done] report expect='FACTORY' cmd=True \| T3 PASS 64s [d |
| 8022 | 2026-10-14 11:42:41 | a8403e44 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 64s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 63s [done] report expect='FACTORY' cmd=True \| T3 PASS 64s [d |
| 8023 | 2026-10-14 11:42:41 | 09eb4142 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "30e368943ffb4b7a92841d88069a53ca", "after_quota": "a8403e44fa1241c1a34f5e964472b |
| 8024 | 2026-10-14 11:42:41 | a8403e44 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8025 | 2026-10-14 11:42:42 | 56718df5 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8026 | 2026-10-14 11:55:40 | 56718df5 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 8027 | 2026-10-14 11:55:40 | 56718df5 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 8028 | 2026-10-14 11:55:40 | 93b1d742 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5e3cb81dcaef415aa193471d2cd92af9", "after_quota": "56718df58428445d962d40e2cea5c |
| 8029 | 2026-10-14 11:55:40 | 56718df5 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8030 | 2026-10-14 11:55:40 | e80bcd61 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8031 | 2026-10-14 12:09:41 | e80bcd61 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 63s [done] report expect='FACTORY' cmd=True \| T3 PASS 65s [d |
| 8032 | 2026-10-14 12:09:41 | e80bcd61 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 63s [done] report expect='FACTORY' cmd=True \| T3 PASS 65s [d |
| 8033 | 2026-10-14 12:09:41 | 3a1cba65 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "773c8a3bd76049e6b5a24b3e92ea65fc", "after_quota": "e80bcd61bc2740b287cad448df24c |
| 8034 | 2026-10-14 12:09:41 | e80bcd61 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8035 | 2026-10-14 12:09:45 | 214b4c30 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8036 | 2026-10-14 12:22:22 | 214b4c30 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 65s [d |
| 8037 | 2026-10-14 12:22:22 | 214b4c30 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 65s [d |
| 8038 | 2026-10-14 12:22:22 | da38a03e | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fefd132857c64f0d981f48b23770a2c5", "after_quota": "214b4c30943d442ea13acbef0cb9b |
| 8039 | 2026-10-14 12:22:22 | 214b4c30 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8040 | 2026-10-14 12:22:25 | f9b10c1e | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8041 | 2026-10-14 12:34:13 | 8188cb64 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8042 | 2026-10-14 12:34:13 | 72f87ba6 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T13"}} |
| 8043 | 2026-10-14 12:35:10 | 8188cb64 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 8044 | 2026-10-14 12:35:10 | 8188cb64 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptos |
| 8045 | 2026-10-14 12:35:19 | f9b10c1e | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 87s [d |
| 8046 | 2026-10-14 12:35:19 | f9b10c1e | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 87s [d |
| 8047 | 2026-10-14 12:35:19 | 7b2aa9f9 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "f9b10c1ee6d14bebb81112682f64492f", "after_quota": "f9b10c1ee6d14bebb81112682f644 |
| 8048 | 2026-10-14 12:35:19 | f9b10c1e | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8049 | 2026-10-14 12:35:20 | e2869fda | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8050 | 2026-10-14 12:37:08 | b22e199f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8051 | 2026-10-14 12:37:08 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8052 | 2026-10-14 12:37:09 | aafdd71b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T13"}} |
| 8053 | 2026-10-14 12:37:09 | b22e199f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8054 | 2026-10-14 12:47:51 | e2869fda | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 90s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 8055 | 2026-10-14 12:47:51 | e2869fda | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 90s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 8056 | 2026-10-14 12:47:51 | 421c497d | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "e2869fda5a2d4e378949f05aa52924a5", "after_quota": "e2869fda5a2d4e378949f05aa5292 |
| 8057 | 2026-10-14 12:47:51 | e2869fda | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8058 | 2026-10-14 12:52:07 | 7b5aa26d | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8059 | 2026-10-14 13:06:01 | 7b5aa26d | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 44s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 80s [done] report expect='FACTORY' cmd=True \| T3 PASS 81s [d |
| 8060 | 2026-10-14 13:06:01 | 7b5aa26d | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 44s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 80s [done] report expect='FACTORY' cmd=True \| T3 PASS 81s [d |
| 8061 | 2026-10-14 13:06:01 | 16edca8e | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a5c9b2241151489ea85e56994e87fa75", "after_quota": "7b5aa26d629c4c888613435e831eb |
| 8062 | 2026-10-14 13:06:01 | 7b5aa26d | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8063 | 2026-10-14 13:06:05 | e32c1507 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8064 | 2026-10-14 13:18:20 | e32c1507 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 62s [done] report expect='FACTORY' cmd=True \| T3 PASS 62s [d |
| 8065 | 2026-10-14 13:18:20 | e32c1507 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 62s [done] report expect='FACTORY' cmd=True \| T3 PASS 62s [d |
| 8066 | 2026-10-14 13:18:20 | 891f375d | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "1c048b97a00941b4a0a2a31b29aec1c6", "after_quota": "e32c1507c64c446b881fbdf6e1404 |
| 8067 | 2026-10-14 13:18:20 | e32c1507 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8068 | 2026-10-14 13:18:21 | f0a7add9 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8069 | 2026-10-14 13:32:28 | f0a7add9 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 170s [ |
| 8070 | 2026-10-14 13:32:28 | f0a7add9 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 170s [ |
| 8071 | 2026-10-14 13:32:28 | e8402ec9 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "4940d9aa166d426aadfe8f833d27143c", "after_quota": "f0a7add91e2640c48072f3baef839 |
| 8072 | 2026-10-14 13:32:28 | f0a7add9 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8073 | 2026-10-14 13:32:29 | e1bba806 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8074 | 2026-10-14 13:34:17 | 72f87ba6 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8075 | 2026-10-14 13:34:17 | 4f89b711 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T14"}} |
| 8076 | 2026-10-14 13:35:23 | 72f87ba6 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\":  |
| 8077 | 2026-10-14 13:35:23 | 72f87ba6 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 8078 | 2026-10-14 13:35:23 | 72f87ba6 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash38", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\ |
| 8079 | 2026-10-14 13:35:23 | 62ccdabf |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-14", "trigger": "blocked:gemini-flash-latest,gemini-flash36,gemini-flas |
| 8080 | 2026-10-14 13:35:23 | fb75b79c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-14", "trigger": "blocked:gemini-flash-latest,gemini-flash36,gemini-fl |
| 8081 | 2026-10-14 13:35:23 | 44a008e3 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-14", "trigger": "blocked:gemini-flash-latest,gemini-flash36,gemin |
| 8082 | 2026-10-14 13:35:23 | 6ab593b5 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-14", "trigger": "blocked:gemini-flash-latest,gemini-flash36,gemini- |
| 8083 | 2026-10-14 13:35:23 | 2062104d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-14", "trigger": "blocked:gemini-flash-latest,gemini-flash36,gemini-fl |
| 8084 | 2026-10-14 13:35:23 | 399e426d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-14", "trigger": "blocked:gemini-flash-latest,gemini-flash36,gemini-f |
| 8085 | 2026-10-14 13:35:23 | 72f87ba6 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen2 |
| 8086 | 2026-10-14 13:35:26 | 62ccdabf |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8087 | 2026-10-14 13:35:27 | 62ccdabf |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 8088 | 2026-10-14 13:35:31 | fb75b79c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8089 | 2026-10-14 13:35:31 | fb75b79c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8090 | 2026-10-14 13:35:34 | 44a008e3 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8091 | 2026-10-14 13:35:34 | 44a008e3 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8092 | 2026-10-14 13:35:37 | 6ab593b5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8093 | 2026-10-14 13:35:37 | 6ab593b5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8094 | 2026-10-14 13:35:41 | 2062104d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8095 | 2026-10-14 13:35:41 | 2062104d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8096 | 2026-10-14 13:35:45 | 399e426d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8097 | 2026-10-14 13:35:45 | 399e426d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8098 | 2026-10-14 13:37:13 | aafdd71b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8099 | 2026-10-14 13:37:13 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8100 | 2026-10-14 13:37:14 | a728264b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T14"}} |
| 8101 | 2026-10-14 13:37:14 | aafdd71b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8102 | 2026-10-14 13:45:53 | e1bba806 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 77s [done] report expect='FACTORY' cmd=True \| T3 PASS 84s [d |
| 8103 | 2026-10-14 13:45:53 | e1bba806 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 77s [done] report expect='FACTORY' cmd=True \| T3 PASS 84s [d |
| 8104 | 2026-10-14 13:45:53 | da5c605f | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fe371a05201e499c9cc16d620128e678", "after_quota": "e1bba8061cf241ed9aa389e507b80 |
| 8105 | 2026-10-14 13:45:53 | e1bba806 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8106 | 2026-10-14 13:45:53 | 09eb4142 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8107 | 2026-10-14 13:58:09 | 09eb4142 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 8108 | 2026-10-14 13:58:09 | 09eb4142 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 8109 | 2026-10-14 13:58:09 | e349b46e | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "30e368943ffb4b7a92841d88069a53ca", "after_quota": "09eb414216b94d13916e0044d10c1 |
| 8110 | 2026-10-14 13:58:09 | 09eb4142 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8111 | 2026-10-14 13:58:13 | 93b1d742 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8112 | 2026-10-14 14:10:28 | 93b1d742 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 62s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 8113 | 2026-10-14 14:10:28 | 93b1d742 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 62s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 8114 | 2026-10-14 14:10:28 | 1d4d924b | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5e3cb81dcaef415aa193471d2cd92af9", "after_quota": "93b1d742a2c34d20a294e76aefd62 |
| 8115 | 2026-10-14 14:10:28 | 93b1d742 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8116 | 2026-10-14 14:10:28 | 3a1cba65 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8117 | 2026-10-14 14:23:29 | 3a1cba65 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 76s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 8118 | 2026-10-14 14:23:29 | 3a1cba65 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 76s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 8119 | 2026-10-14 14:23:29 | 01291e79 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "773c8a3bd76049e6b5a24b3e92ea65fc", "after_quota": "3a1cba65ca82420ca0009f54b9f0e |
| 8120 | 2026-10-14 14:23:29 | 3a1cba65 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8121 | 2026-10-14 14:23:33 | da38a03e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8122 | 2026-10-14 14:34:18 | 4f89b711 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8123 | 2026-10-14 14:34:18 | 12211cd8 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T15"}} |
| 8124 | 2026-10-14 14:34:59 | 4f89b711 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\n  |
| 8125 | 2026-10-14 14:34:59 | 4f89b711 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-gemma26b", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 8126 | 2026-10-14 14:34:59 | 6dbe6573 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-14", "trigger": "blocked:gemini-flash"}} |
| 8127 | 2026-10-14 14:34:59 | 34c379e2 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-14", "trigger": "blocked:gemini-flash"}} |
| 8128 | 2026-10-14 14:34:59 | fa941204 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-14", "trigger": "blocked:gemini-flash"}} |
| 8129 | 2026-10-14 14:34:59 | 3078a88f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-14", "trigger": "blocked:gemini-flash"}} |
| 8130 | 2026-10-14 14:34:59 | 39011089 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-14", "trigger": "blocked:gemini-flash"}} |
| 8131 | 2026-10-14 14:34:59 | 8e5ec14a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-14", "trigger": "blocked:gemini-flash"}} |
| 8132 | 2026-10-14 14:35:00 | 4f89b711 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gpto |
| 8133 | 2026-10-14 14:35:03 | 6dbe6573 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8134 | 2026-10-14 14:35:04 | 6dbe6573 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 8135 | 2026-10-14 14:35:07 | 34c379e2 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8136 | 2026-10-14 14:35:07 | 34c379e2 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8137 | 2026-10-14 14:35:12 | fa941204 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8138 | 2026-10-14 14:35:12 | fa941204 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8139 | 2026-10-14 14:35:17 | 3078a88f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8140 | 2026-10-14 14:35:17 | 3078a88f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8141 | 2026-10-14 14:35:21 | 39011089 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8142 | 2026-10-14 14:35:21 | 39011089 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8143 | 2026-10-14 14:35:25 | 8e5ec14a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8144 | 2026-10-14 14:35:25 | 8e5ec14a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8145 | 2026-10-14 14:35:37 | da38a03e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 8146 | 2026-10-14 14:35:37 | da38a03e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 8147 | 2026-10-14 14:35:37 | 585d7c88 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fefd132857c64f0d981f48b23770a2c5", "after_quota": "da38a03ea59c4e6ab33c9249a3b53 |
| 8148 | 2026-10-14 14:35:37 | da38a03e | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8149 | 2026-10-14 14:35:39 | 7b2aa9f9 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8150 | 2026-10-14 14:37:17 | a728264b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8151 | 2026-10-14 14:37:17 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8152 | 2026-10-14 14:37:18 | 2cbc59ff |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T15"}} |
| 8153 | 2026-10-14 14:37:18 | a728264b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8154 | 2026-10-14 14:57:47 | 7b2aa9f9 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8155 | 2026-10-14 14:57:50 | 421c497d | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8156 | 2026-10-14 15:19:57 | 421c497d | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8157 | 2026-10-14 15:20:02 | 7b2aa9f9 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 8158 | 2026-10-14 15:34:23 | 12211cd8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8159 | 2026-10-14 15:34:23 | 95f1688c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T16"}} |
| 8160 | 2026-10-14 15:34:37 | 12211cd8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "groq-gptoss120b", "groq-gptoss20b", "groq-qwe |
| 8161 | 2026-10-14 15:37:21 | 2cbc59ff |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8162 | 2026-10-14 15:37:21 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8163 | 2026-10-14 15:37:21 | a4f7d49b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T16"}} |
| 8164 | 2026-10-14 15:37:21 | 2cbc59ff |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8165 | 2026-10-14 15:42:11 | 7b2aa9f9 | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8166 | 2026-10-14 15:42:15 | 421c497d | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 8167 | 2026-10-14 16:01:34 | 421c497d | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 63s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 218s [done] report expect='FACTORY' cmd=True \| T3 PASS 104s  |
| 8168 | 2026-10-14 16:01:34 | 421c497d | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 63s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 218s [done] report expect='FACTORY' cmd=True \| T3 PASS 104s  |
| 8169 | 2026-10-14 16:01:34 | 421c497d | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 8170 | 2026-10-14 16:01:34 | 50c9dc64 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "abdd8333716b46e4b457f3e3406bd86a", "retry_of": "421c497d92014828b6a6692e0d4fbd0 |
| 8171 | 2026-10-14 16:01:34 | 421c497d | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8172 | 2026-10-14 16:01:37 | 7b2aa9f9 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 8173 | 2026-10-14 16:20:22 | 7b2aa9f9 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 42s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 211s [done] report expect='FACTORY' cmd=True \| T3 PASS 94s [ |
| 8174 | 2026-10-14 16:20:22 | 7b2aa9f9 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 42s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 211s [done] report expect='FACTORY' cmd=True \| T3 PASS 94s [ |
| 8175 | 2026-10-14 16:20:22 | 7838d8fd | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "f9b10c1ee6d14bebb81112682f64492f", "after_quota": "7b2aa9f96a5e4a659ef0d3026486d |
| 8176 | 2026-10-14 16:20:22 | 7b2aa9f9 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8177 | 2026-10-14 16:20:24 | 16edca8e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8178 | 2026-10-14 16:34:27 | 95f1688c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8179 | 2026-10-14 16:34:27 | b26f40de |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T17"}} |
| 8180 | 2026-10-14 16:34:47 | 95f1688c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-lite", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", " |
| 8181 | 2026-10-14 16:37:21 | a4f7d49b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8182 | 2026-10-14 16:37:21 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8183 | 2026-10-14 16:37:22 | fca5af08 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T17"}} |
| 8184 | 2026-10-14 16:37:22 | a4f7d49b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8185 | 2026-10-14 16:42:35 | 16edca8e | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8186 | 2026-10-14 16:42:36 | 50c9dc64 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8187 | 2026-10-14 17:04:42 | 50c9dc64 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8188 | 2026-10-14 17:04:44 | 16edca8e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 8189 | 2026-10-14 17:26:51 | 16edca8e | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8190 | 2026-10-14 17:26:52 | 50c9dc64 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 8191 | 2026-10-14 17:34:30 | b26f40de |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8192 | 2026-10-14 17:34:30 | 8bdeddda |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T18"}} |
| 8193 | 2026-10-14 17:34:44 | b26f40de |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-lite31", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\n |
| 8194 | 2026-10-14 17:34:44 | 6c9b4839 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-14", "trigger": "blocked:gemini-lite31"}} |
| 8195 | 2026-10-14 17:34:44 | 24975f92 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-14", "trigger": "blocked:gemini-lite31"}} |
| 8196 | 2026-10-14 17:34:44 | 34c4e275 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-14", "trigger": "blocked:gemini-lite31"}} |
| 8197 | 2026-10-14 17:34:44 | 18de3bfd |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-14", "trigger": "blocked:gemini-lite31"}} |
| 8198 | 2026-10-14 17:34:44 | 5844091f |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-14", "trigger": "blocked:gemini-lite31"}} |
| 8199 | 2026-10-14 17:34:44 | 3eeb0a9d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-14", "trigger": "blocked:gemini-lite31"}} |
| 8200 | 2026-10-14 17:34:44 | b26f40de |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-lite", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", " |
| 8201 | 2026-10-14 17:34:48 | 6c9b4839 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8202 | 2026-10-14 17:34:48 | 6c9b4839 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 8203 | 2026-10-14 17:34:51 | 24975f92 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8204 | 2026-10-14 17:34:53 | 24975f92 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 8205 | 2026-10-14 17:34:56 | 34c4e275 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8206 | 2026-10-14 17:34:58 | 34c4e275 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 8207 | 2026-10-14 17:35:01 | 18de3bfd |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8208 | 2026-10-14 17:35:01 | 18de3bfd |  | owner.needed | fast-LAPTOP-LRE6PSA8 | {"provider": "cerebras", "reason": "set CEREBRAS_API_KEY (User env) after signing up: https://cloud.cerebras.ai (free tier ~1M tokens/day)"} |
| 8209 | 2026-10-14 17:35:01 | 18de3bfd |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8210 | 2026-10-14 17:35:04 | 5844091f |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8211 | 2026-10-14 17:35:05 | 5844091f |  | owner.needed | fast-LAPTOP-LRE6PSA8 | {"provider": "nvidia", "reason": "set NVIDIA_API_KEY (User env) after signing up: https://build.nvidia.com (free ~40 rpm, tool-capable model |
| 8212 | 2026-10-14 17:35:05 | 5844091f |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8213 | 2026-10-14 17:35:08 | 3eeb0a9d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8214 | 2026-10-14 17:35:08 | 3eeb0a9d |  | owner.needed | fast-LAPTOP-LRE6PSA8 | {"provider": "mistral", "reason": "set MISTRAL_API_KEY (User env) after signing up: https://console.mistral.ai (Experiment free tier)"} |
| 8215 | 2026-10-14 17:35:08 | 3eeb0a9d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8216 | 2026-10-15 00:24:26 | 50c9dc64 |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 8217 | 2026-10-15 00:24:26 | fca5af08 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8218 | 2026-10-15 00:24:28 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8219 | 2026-10-15 00:25:02 | 6bae1547 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-15T01"}} |
| 8220 | 2026-10-15 00:25:02 | fca5af08 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8221 | 2026-10-15 00:25:04 | 50c9dc64 |  | job.readopted | svc-LAPTOP-LRE6PSA8 | {} |
| 8222 | 2026-10-15 00:25:05 | 8bdeddda |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8223 | 2026-10-15 00:25:05 | d4220485 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T01"}} |
| 8224 | 2026-10-15 00:25:06 | 8bdeddda |  | probe.network_down | fast-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8225 | 2026-10-15 00:25:06 | cec87203 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T18-retry", "retry_of": "8bdeddda2de645119224d8e0a8d21851"}} |
| 8226 | 2026-10-15 00:25:06 | 8bdeddda |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8227 | 2026-10-15 00:35:10 | cec87203 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8228 | 2026-10-15 00:35:10 | d4220485 |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8229 | 2026-10-15 00:35:30 | cec87203 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 8230 | 2026-10-15 00:35:30 | cec87203 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-lite31", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 8231 | 2026-10-15 00:35:30 | cec87203 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss1 |
| 8232 | 2026-10-15 00:36:11 | 50c9dc64 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8233 | 2026-10-15 00:36:13 | 16edca8e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 8234 | 2026-10-15 00:51:43 | 16edca8e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 120s [done] report expect='FACTORY' cmd=True \| T3 PASS 135s  |
| 8235 | 2026-10-15 00:51:43 | 16edca8e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 120s [done] report expect='FACTORY' cmd=True \| T3 PASS 135s  |
| 8236 | 2026-10-15 00:51:43 | ae1ae481 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a5c9b2241151489ea85e56994e87fa75", "after_quota": "16edca8e04364537a29ff8c7b4617 |
| 8237 | 2026-10-15 00:51:43 | 16edca8e | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8238 | 2026-10-15 00:51:46 | 50c9dc64 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 8239 | 2026-10-15 01:03:39 | 50c9dc64 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 81s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 103s [done] report expect='FACTORY' cmd=True \| T3 PASS 100s  |
| 8240 | 2026-10-15 01:03:39 | 50c9dc64 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 81s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 103s [done] report expect='FACTORY' cmd=True \| T3 PASS 100s  |
| 8241 | 2026-10-15 01:03:39 | 50c9dc64 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 8242 | 2026-10-15 01:03:39 | 85478d12 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "abdd8333716b46e4b457f3e3406bd86a", "retry_of": "50c9dc64785044cf90eda416f7d1828 |
| 8243 | 2026-10-15 01:03:39 | 50c9dc64 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
