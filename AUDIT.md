# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 4885 | 2026-10-04 20:43:55 | 596c673f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-04", "trigger": "blocked:gemini-flash36"}} |
| 4886 | 2026-10-04 20:43:55 | 08388440 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-04", "trigger": "blocked:gemini-flash36"}} |
| 4887 | 2026-10-04 20:43:55 | ad981b46 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-04", "trigger": "blocked:gemini-flash36"}} |
| 4888 | 2026-10-04 20:43:55 | 506575ae |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "gr |
| 4889 | 2026-10-04 20:43:59 | f7bdefcb |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4890 | 2026-10-04 20:43:59 | f7bdefcb |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4891 | 2026-10-04 20:44:02 | a7ebec03 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4892 | 2026-10-04 20:44:04 | a7ebec03 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4893 | 2026-10-04 20:44:07 | 8594c049 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4894 | 2026-10-04 20:44:09 | 8594c049 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4895 | 2026-10-04 20:44:12 | 596c673f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4896 | 2026-10-04 20:44:12 | 596c673f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4897 | 2026-10-04 20:44:15 | 08388440 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4898 | 2026-10-04 20:44:15 | 08388440 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4899 | 2026-10-04 20:44:19 | ad981b46 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4900 | 2026-10-04 20:44:19 | ad981b46 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4901 | 2026-10-04 20:44:47 | 8cc811ec |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4902 | 2026-10-04 20:44:47 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4903 | 2026-10-04 20:44:48 | f2b0c3a3 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-04T21"}} |
| 4904 | 2026-10-04 20:44:48 | 8cc811ec |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4905 | 2026-10-04 20:57:03 | 20604f3a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 82s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 4906 | 2026-10-04 20:57:03 | 20604f3a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 82s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 4907 | 2026-10-04 20:57:03 | 9e805040 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "20604f3ad9d1471c98ca880e9137c |
| 4908 | 2026-10-04 20:57:03 | 20604f3a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4909 | 2026-10-04 20:57:17 | f512992d | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4910 | 2026-10-04 21:10:27 | f512992d | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 72s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 4911 | 2026-10-04 21:10:27 | f512992d | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 72s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 4912 | 2026-10-04 21:10:27 | d9e8918c | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "77881c8a8a21429c95000f5ff5430657", "after_quota": "f512992d62ff45518ae9e4a75dc21 |
| 4913 | 2026-10-04 21:10:27 | f512992d | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4914 | 2026-10-04 21:13:55 | 434d7bd4 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4915 | 2026-10-04 21:27:07 | 434d7bd4 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 4916 | 2026-10-04 21:27:07 | 434d7bd4 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 4917 | 2026-10-04 21:27:07 | f8237861 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a2f5a601f2d84985b479c18f015c9c2e", "after_quota": "434d7bd4c43743fc98b70056320bd |
| 4918 | 2026-10-04 21:27:07 | 434d7bd4 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4919 | 2026-10-04 21:27:55 | f1dca4c9 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4920 | 2026-10-04 21:42:11 | f1dca4c9 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 76s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 4921 | 2026-10-04 21:42:11 | f1dca4c9 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 76s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 4922 | 2026-10-04 21:42:11 | 78f5347c | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "afb9f6f5ab6a418db3f5bd977c09026e", "after_quota": "f1dca4c95f844822af80c1fe4c990 |
| 4923 | 2026-10-04 21:42:11 | f1dca4c9 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4924 | 2026-10-04 21:43:39 | 2db310a7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4925 | 2026-10-04 21:43:39 | 17090594 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-04T22"}} |
| 4926 | 2026-10-04 21:44:06 | 2db310a7 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 4927 | 2026-10-04 21:44:06 | 2db310a7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "gro |
| 4928 | 2026-10-04 21:44:49 | f2b0c3a3 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4929 | 2026-10-04 21:44:49 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4930 | 2026-10-04 21:44:50 | 69f13025 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-04T22"}} |
| 4931 | 2026-10-04 21:44:50 | f2b0c3a3 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4932 | 2026-10-04 22:04:36 | 910bf161 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4933 | 2026-10-04 22:18:04 | 910bf161 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 73s [done] report expect='FACTORY' cmd=True \| T3 PASS 76s [d |
| 4934 | 2026-10-04 22:18:04 | 910bf161 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 73s [done] report expect='FACTORY' cmd=True \| T3 PASS 76s [d |
| 4935 | 2026-10-04 22:18:04 | b88085b5 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "07e26f32402644c6a7533696fca37040", "after_quota": "910bf161ab714be698bd5cb4de538 |
| 4936 | 2026-10-04 22:18:04 | 910bf161 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4937 | 2026-10-04 22:31:44 | 5d6673a0 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4938 | 2026-10-04 22:43:44 | 17090594 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4939 | 2026-10-04 22:43:44 | 5fee5cc7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-04T23"}} |
| 4940 | 2026-10-04 22:44:03 | 5d6673a0 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 72s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4941 | 2026-10-04 22:44:03 | 5d6673a0 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 72s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4942 | 2026-10-04 22:44:03 | 5d6673a0 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4943 | 2026-10-04 22:44:03 | dadc6ba3 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "5d6673a0709d408895d24b7ff42bf3a |
| 4944 | 2026-10-04 22:44:03 | 5d6673a0 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4945 | 2026-10-04 22:44:04 | 17090594 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 4946 | 2026-10-04 22:44:04 | 6856fd73 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-04", "trigger": "blocked:gemini-flash36"}} |
| 4947 | 2026-10-04 22:44:04 | 66cc5cf1 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-04", "trigger": "blocked:gemini-flash36"}} |
| 4948 | 2026-10-04 22:44:04 | f443e017 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-04", "trigger": "blocked:gemini-flash36"}} |
| 4949 | 2026-10-04 22:44:04 | b89aacf5 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-04", "trigger": "blocked:gemini-flash36"}} |
| 4950 | 2026-10-04 22:44:04 | 0e224835 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-04", "trigger": "blocked:gemini-flash36"}} |
| 4951 | 2026-10-04 22:44:04 | ad76c738 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-04", "trigger": "blocked:gemini-flash36"}} |
| 4952 | 2026-10-04 22:44:04 | 17090594 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "gr |
| 4953 | 2026-10-04 22:44:07 | 6856fd73 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4954 | 2026-10-04 22:44:07 | 6856fd73 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4955 | 2026-10-04 22:44:10 | 66cc5cf1 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4956 | 2026-10-04 22:44:10 | 66cc5cf1 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4957 | 2026-10-04 22:44:13 | f443e017 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4958 | 2026-10-04 22:44:13 | f443e017 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4959 | 2026-10-04 22:44:17 | b89aacf5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4960 | 2026-10-04 22:44:17 | b89aacf5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4961 | 2026-10-04 22:44:21 | 0e224835 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4962 | 2026-10-04 22:44:21 | 0e224835 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4963 | 2026-10-04 22:44:23 | ad76c738 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4964 | 2026-10-04 22:44:23 | ad76c738 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4965 | 2026-10-04 22:44:52 | 69f13025 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4966 | 2026-10-04 22:44:52 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4967 | 2026-10-04 22:44:52 | 0d82a8f2 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-04T23"}} |
| 4968 | 2026-10-04 22:44:52 | 69f13025 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4969 | 2026-10-04 22:57:05 | 9e805040 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4970 | 2026-10-04 23:13:07 | 9e805040 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 29s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 74s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 4971 | 2026-10-04 23:13:07 | 9e805040 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 29s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 74s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 4972 | 2026-10-04 23:13:07 | d05e9958 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "9e805040e662432ca06bae415e9c0 |
| 4973 | 2026-10-04 23:13:07 | 9e805040 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4974 | 2026-10-04 23:13:11 | d9e8918c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4975 | 2026-10-04 23:33:05 | d9e8918c | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 65s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 129s [done] report expect='FACTORY' cmd=True \| T3 PASS 124s  |
| 4976 | 2026-10-04 23:33:05 | d9e8918c | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 65s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 129s [done] report expect='FACTORY' cmd=True \| T3 PASS 124s  |
| 4977 | 2026-10-04 23:33:05 | 88179f03 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "77881c8a8a21429c95000f5ff5430657", "after_quota": "d9e8918c59c7425181e2590849ce9 |
| 4978 | 2026-10-04 23:33:05 | d9e8918c | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4979 | 2026-10-04 23:33:08 | dadc6ba3 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4980 | 2026-10-04 23:43:44 | 5fee5cc7 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4981 | 2026-10-04 23:43:44 | fb30cd9a |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-05T00"}} |
| 4982 | 2026-10-04 23:43:55 | 5fee5cc7 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-gemma26b", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "loc |
| 4983 | 2026-10-04 23:44:53 | 0d82a8f2 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4984 | 2026-10-04 23:44:53 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4985 | 2026-10-04 23:44:53 | 0ee8fcfb |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-05T00"}} |
| 4986 | 2026-10-04 23:44:53 | 0d82a8f2 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4987 | 2026-10-04 23:52:05 | dadc6ba3 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 65s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 155s [done] report expect='FACTORY' cmd=True \| T3 PASS 123s  |
| 4988 | 2026-10-04 23:52:05 | dadc6ba3 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 65s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 155s [done] report expect='FACTORY' cmd=True \| T3 PASS 123s  |
| 4989 | 2026-10-04 23:52:05 | dadc6ba3 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4990 | 2026-10-04 23:52:05 | 013d3a09 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "dadc6ba3de2947aa839d709532c1c9a |
| 4991 | 2026-10-04 23:52:05 | dadc6ba3 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4992 | 2026-10-04 23:52:09 | f8237861 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4993 | 2026-10-05 00:10:59 | f8237861 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 67s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 125s [done] report expect='FACTORY' cmd=True \| T3 PASS 124s  |
| 4994 | 2026-10-05 00:10:59 | f8237861 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 67s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 125s [done] report expect='FACTORY' cmd=True \| T3 PASS 124s  |
| 4995 | 2026-10-05 00:10:59 | f8237861 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4996 | 2026-10-05 00:10:59 | 44c3b1a8 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "076d00557198429696acd4c0a35af210", "retry_of": "f8237861be614d69a1131bbf882251e |
| 4997 | 2026-10-05 00:10:59 | f8237861 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4998 | 2026-10-05 00:11:01 | 78f5347c | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4999 | 2026-10-06 12:52:07 | 78f5347c |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 5000 | 2026-10-06 12:52:07 | fb30cd9a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5001 | 2026-10-06 12:52:11 | 7155e0da |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-06T13"}} |
| 5002 | 2026-10-06 12:52:25 | 78f5347c |  | job.readopted | svc-LAPTOP-LRE6PSA8 | {} |
| 5003 | 2026-10-06 12:53:05 | 1c1bcdfb |  | job.enqueued | nightly-task | {"kind": "monitor", "payload": {"only": null, "day": "2026-10-06"}} |
| 5004 | 2026-10-06 12:53:23 | fb30cd9a |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 5005 | 2026-10-06 12:53:23 | fb30cd9a |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "or-qwen27b", "outcome": "gone", "before": "VERIFIED", "after": "BLOCKED", "detail": "{\"error\":{\"message\":\"this model is unav |
| 5006 | 2026-10-06 12:53:23 | 2c009804 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-06", "trigger": "blocked:or-qwen27b"}} |
| 5007 | 2026-10-06 12:53:23 | efb0711e |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-06", "trigger": "blocked:or-qwen27b"}} |
| 5008 | 2026-10-06 12:53:23 | 0bb335ec |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-06", "trigger": "blocked:or-qwen27b"}} |
| 5009 | 2026-10-06 12:53:23 | 06f0973f |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-06", "trigger": "blocked:or-qwen27b"}} |
| 5010 | 2026-10-06 12:53:23 | a5b1d157 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-06", "trigger": "blocked:or-qwen27b"}} |
| 5011 | 2026-10-06 12:53:23 | bd4700e5 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-06", "trigger": "blocked:or-qwen27b"}} |
| 5012 | 2026-10-06 12:53:23 | fb30cd9a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-li |
| 5013 | 2026-10-06 12:53:29 | 0ee8fcfb |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5014 | 2026-10-06 12:53:29 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5015 | 2026-10-06 12:53:29 |  | 030 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "e98fb290", "reason": "bot testing"} |
| 5016 | 2026-10-06 12:53:30 | 53d3779f |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-06T13"}} |
| 5017 | 2026-10-06 12:53:30 | 0ee8fcfb |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5018 | 2026-10-06 12:53:34 | 2c009804 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5019 | 2026-10-06 12:53:35 | 2c009804 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5020 | 2026-10-06 12:53:40 | efb0711e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5021 | 2026-10-06 12:53:41 | efb0711e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5022 | 2026-10-06 12:53:46 | 0bb335ec |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5023 | 2026-10-06 12:53:48 | 0bb335ec |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5024 | 2026-10-06 12:53:54 | 06f0973f |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5025 | 2026-10-06 12:53:54 | 06f0973f |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5026 | 2026-10-06 12:53:59 | a5b1d157 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5027 | 2026-10-06 12:53:59 | a5b1d157 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5028 | 2026-10-06 12:54:05 | bd4700e5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5029 | 2026-10-06 12:54:05 | bd4700e5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5030 | 2026-10-06 12:54:09 | b0113ecf |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5031 | 2026-10-06 12:54:09 | b0113ecf |  | audit.verified | fast-LAPTOP-LRE6PSA8 | {"rows": 5029, "hashed": 4277, "first_bad": null} |
| 5032 | 2026-10-06 12:54:09 | 453de9e9 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-10-07"}} |
| 5033 | 2026-10-06 12:54:09 | 5cd5456d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-10-06"}} |
| 5034 | 2026-10-06 12:54:09 | dbeda246 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-10-06"}} |
| 5035 | 2026-10-06 12:54:09 | b0113ecf |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5036 | 2026-10-06 12:56:28 | 78f5347c | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 5037 | 2026-10-06 12:56:29 | 013d3a09 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5038 | 2026-10-06 12:56:33 | 1c1bcdfb |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5039 | 2026-10-06 12:56:33 | 6878b5df | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "day": "2026-10-06"}} |
| 5040 | 2026-10-06 12:56:33 | fd9a18b0 | 028 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "028", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "day": "2026-10-06"}} |
| 5041 | 2026-10-06 12:56:33 | 1c1bcdfb |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "028"], "jobs": ["6878b5df", "fd9a18b0"]} |
| 5042 | 2026-10-06 12:56:33 | 1c1bcdfb |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5043 | 2026-10-06 12:56:37 | fd9a18b0 | 028 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5044 | 2026-10-06 12:57:33 | fd9a18b0 | 028 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 4s [done] expect='X_OK' last='' \| T2 FAIL 14s [done] expect='3' last='Using config: C:\\AI\\Factory\\run\\botcfg\\028.j |
| 5045 | 2026-10-06 12:57:33 | fd9a18b0 | 028 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 4s [done] expect='X_OK' last='' \| T2 FAIL 14s [done] expect='3' last='Using config: C:\\AI\\Factory\\run\\botcfg\\028.j |
| 5046 | 2026-10-06 12:57:33 | fd9a18b0 | 028 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5047 | 2026-10-06 12:57:33 | c49654c3 | 028 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "028", "max_rounds": 2}} |
| 5048 | 2026-10-06 12:57:33 | fd9a18b0 | 028 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "028", "status": "testing", "verified": "UNVERIFIED"}} |
| 5049 | 2026-10-06 12:57:38 | c49654c3 | 028 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5050 | 2026-10-06 13:00:01 | c49654c3 | 028 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-120b", "sandbox": "4/4", "rejected": null}], "boundary |
| 5051 | 2026-10-06 13:00:01 | c49654c3 | 028 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 5052 | 2026-10-06 13:00:01 | c49654c3 | 028 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "028", "name": "weekly-self-review", "status": "active", "verified": "VERIFIED"}} |
| 5053 | 2026-10-06 13:00:07 | 5cd5456d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5054 | 2026-10-06 13:00:59 | 013d3a09 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 14s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 5055 | 2026-10-06 13:00:59 | 013d3a09 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 14s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 5056 | 2026-10-06 13:00:59 | 013d3a09 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5057 | 2026-10-06 13:00:59 | 368a661a | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "013d3a09bccb43969d75b3b5dfee0bc |
| 5058 | 2026-10-06 13:00:59 | 013d3a09 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5059 | 2026-10-06 13:01:04 | 44c3b1a8 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5060 | 2026-10-06 13:03:30 | 5cd5456d |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "gemini-gemma26b", "result": "2/4", "quota": 0, "secs": 57} |
| 5061 | 2026-10-06 13:03:30 | 5cd5456d |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "groq-qwen27b", "result": "2/4", "quota": 0, "secs": 68} |
| 5062 | 2026-10-06 13:03:30 | 5cd5456d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["gemini-gemma26b", "2/4"], ["groq-qwen27b", "2/4"]]}} |
| 5063 | 2026-10-06 13:03:37 | dbeda246 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5064 | 2026-10-06 13:04:22 | dbeda246 |  | factory.canary | svc-LAPTOP-LRE6PSA8 | {"verdict": "FAIL", "lane": "groq:openai/gpt-oss-120b", "chain": ["gemini-gemini-flash-lite-latest", "or-apodex-11-mini", "gemini-lite31", " |
| 5065 | 2026-10-06 13:04:22 | dbeda246 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"pass": 1, "total": 2}} |
| 5066 | 2026-10-06 13:04:44 | 44c3b1a8 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [d |
| 5067 | 2026-10-06 13:04:44 | 44c3b1a8 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [d |
| 5068 | 2026-10-06 13:04:44 | 44c3b1a8 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5069 | 2026-10-06 13:04:44 | d8b9793d | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "076d00557198429696acd4c0a35af210", "retry_of": "44c3b1a8a7ad4dbeafd240874009de0 |
| 5070 | 2026-10-06 13:04:44 | 44c3b1a8 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5071 | 2026-10-06 13:04:48 | 78f5347c | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 5072 | 2026-10-06 13:10:31 | 78f5347c | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 15s [done] report expect='FACTORY' cmd=True \| T3 PASS 16s [d |
| 5073 | 2026-10-06 13:10:31 | 78f5347c | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 15s [done] report expect='FACTORY' cmd=True \| T3 PASS 16s [d |
| 5074 | 2026-10-06 13:10:31 | 78f5347c | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5075 | 2026-10-06 13:10:31 | 1da3fd71 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "e3e27be7486c486399ca49575cec8d90", "retry_of": "78f5347cfd7c4f16ad6e2fe3632cf74 |
| 5076 | 2026-10-06 13:10:31 | 78f5347c | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5077 | 2026-10-06 13:10:34 | b88085b5 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5078 | 2026-10-06 13:14:08 | b88085b5 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 15s [d |
| 5079 | 2026-10-06 13:14:08 | b88085b5 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 15s [d |
| 5080 | 2026-10-06 13:14:08 | b88085b5 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5081 | 2026-10-06 13:14:08 | f0ad66fc | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "b88085b55a164469bcfc311a2dd6de8 |
| 5082 | 2026-10-06 13:14:08 | b88085b5 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5083 | 2026-10-06 13:14:10 | d05e9958 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5084 | 2026-10-06 13:17:33 | f3c99a58 |  | job.enqueued | master-001 | {"kind": "create", "payload": {"objective": "Perform the weekly self-review of the AI Factory, including counting how many bots were created |
| 5085 | 2026-10-06 13:20:19 | d05e9958 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 5086 | 2026-10-06 13:20:19 | d05e9958 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 5087 | 2026-10-06 13:20:19 | 9676251c | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "d05e99588ca147c88021ebddf7d03 |
| 5088 | 2026-10-06 13:20:19 | d05e9958 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5089 | 2026-10-06 13:20:23 | 88179f03 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5090 | 2026-10-06 13:20:24 | f3c99a58 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5091 | 2026-10-06 13:20:27 | f3c99a58 | 032 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "weekly-self-review", "tools": ["read_file", "write_file", "web_search", "web_fetch"], "permissions": ["fs:read", "fs:write", "net: |
| 5092 | 2026-10-06 13:22:27 | f3c99a58 | 032 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 21s [done] expect='X_OK' last='+ FullyQualifiedErrorId : NativeCommandError' \| T2 PASS 57s [done] expect='3' last='RESU |
| 5093 | 2026-10-06 13:22:27 | bb3451e5 | 032 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "032", "retest_of": "f3c99a58d98d402bad7277c34736f3db"}} |
| 5094 | 2026-10-06 13:22:27 | f3c99a58 | 032 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "032", "name": "weekly-self-review", "pass": 2, "total": 4, "status": "testing", "verified": "UNVERIFIED"}} |
| 5095 | 2026-10-06 13:22:32 | bb3451e5 | 032 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5096 | 2026-10-06 13:24:13 | bb3451e5 | 032 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 16s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\032.json' \| T2 FAIL 34s [done] expect='3' la |
| 5097 | 2026-10-06 13:24:13 | 52cb5c42 | 032 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "032", "max_rounds": 2, "rearchitected": false}} |
| 5098 | 2026-10-06 13:24:13 | bb3451e5 | 032 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "032", "status": "testing", "verified": "UNVERIFIED"}} |
| 5099 | 2026-10-06 13:24:17 | 52cb5c42 | 032 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5100 | 2026-10-06 13:26:19 | 88179f03 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 5101 | 2026-10-06 13:26:19 | 88179f03 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 5102 | 2026-10-06 13:26:19 | 88179f03 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5103 | 2026-10-06 13:26:19 | 733d8574 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "88179f0325a0454ba2f78e284db6d66 |
| 5104 | 2026-10-06 13:26:19 | 88179f03 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5105 | 2026-10-06 13:26:23 | 6878b5df | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5106 | 2026-10-06 13:27:20 | 52cb5c42 | 032 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-120b", "sandbox": "3/4", "rejected": null}, {"round" |
| 5107 | 2026-10-06 13:27:20 | 52cb5c42 | 032 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 5108 | 2026-10-06 13:30:16 | 6878b5df | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 16s [done] report expect='FACTORY' cmd=True \| T3 PASS 15s [d |
| 5109 | 2026-10-06 13:30:16 | 6878b5df | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 16s [done] report expect='FACTORY' cmd=True \| T3 PASS 15s [d |
| 5110 | 2026-10-06 13:30:16 | 6878b5df | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5111 | 2026-10-06 13:30:16 | f94d8bcc | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "retry_of": "6878b5dfdd17445bb939915c8794e1b |
| 5112 | 2026-10-06 13:30:16 | 6878b5df | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5113 | 2026-10-06 13:30:59 | 368a661a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5114 | 2026-10-06 13:34:24 | 368a661a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [do |
| 5115 | 2026-10-06 13:34:24 | 368a661a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [do |
| 5116 | 2026-10-06 13:34:24 | 368a661a | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5117 | 2026-10-06 13:34:24 | 5497f756 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "368a661ab4684a1d827d48ab89bcf02 |
| 5118 | 2026-10-06 13:34:24 | 368a661a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5119 | 2026-10-06 13:34:46 | d8b9793d | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5120 | 2026-10-06 13:38:27 | d8b9793d | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 14s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [d |
| 5121 | 2026-10-06 13:38:27 | d8b9793d | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 14s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [d |
| 5122 | 2026-10-06 13:38:27 | d8b9793d | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5123 | 2026-10-06 13:38:27 | df24e745 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "076d00557198429696acd4c0a35af210", "retry_of": "d8b9793d2a3649a6acb99f50c0dd1d0 |
| 5124 | 2026-10-06 13:38:27 | d8b9793d | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5125 | 2026-10-06 13:40:31 | 1da3fd71 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5126 | 2026-10-06 13:45:48 | 1da3fd71 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [d |
| 5127 | 2026-10-06 13:45:48 | 1da3fd71 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [d |
| 5128 | 2026-10-06 13:45:48 | 1da3fd71 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5129 | 2026-10-06 13:45:48 | 17403faf | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "e3e27be7486c486399ca49575cec8d90", "retry_of": "1da3fd71f5e14a5eb1c62226b95366f |
| 5130 | 2026-10-06 13:45:48 | 1da3fd71 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5131 | 2026-10-06 13:45:49 | f0ad66fc | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5132 | 2026-10-06 13:52:12 | 7155e0da |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5133 | 2026-10-06 13:52:12 | ecf3b4fe |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-06T14"}} |
| 5134 | 2026-10-06 13:52:50 | 7155e0da |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash-latest", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "lo |
| 5135 | 2026-10-06 13:53:35 | 53d3779f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5136 | 2026-10-06 13:53:35 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5137 | 2026-10-06 13:53:35 | de7e0c02 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-06T14"}} |
| 5138 | 2026-10-06 13:53:35 | 53d3779f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5139 | 2026-10-06 13:57:30 | f0ad66fc | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 56s [d |
| 5140 | 2026-10-06 13:57:30 | f0ad66fc | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 56s [d |
| 5141 | 2026-10-06 13:57:30 | eb2b6405 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "f0ad66fce1d34d7ab721da1e4bff23b8", "after_quota": "f0ad66fce1d34d7ab721da1e4bff2 |
| 5142 | 2026-10-06 13:57:30 | f0ad66fc | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5143 | 2026-10-06 13:57:31 | 733d8574 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5144 | 2026-10-06 14:11:51 | 733d8574 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 82s [done] report expect='FACTORY' cmd=True \| T3 PASS 86s [d |
| 5145 | 2026-10-06 14:11:51 | 733d8574 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 82s [done] report expect='FACTORY' cmd=True \| T3 PASS 86s [d |
| 5146 | 2026-10-06 14:11:51 | 733d8574 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5147 | 2026-10-06 14:11:51 | 3be89af3 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "733d857493b14e619ef0fea885fa79e |
| 5148 | 2026-10-06 14:11:51 | 733d8574 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5149 | 2026-10-06 14:11:55 | f94d8bcc | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5150 | 2026-10-06 14:29:15 | f94d8bcc | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 121s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [ |
| 5151 | 2026-10-06 14:29:15 | f94d8bcc | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 121s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [ |
| 5152 | 2026-10-06 14:29:15 | f94d8bcc | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5153 | 2026-10-06 14:29:15 | 41923cc5 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "retry_of": "f94d8bcc4f9c4ebbbb50a418f6b48f7 |
| 5154 | 2026-10-06 14:29:15 | f94d8bcc | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5155 | 2026-10-06 14:29:17 | 5497f756 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5156 | 2026-10-06 14:44:00 | 5497f756 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 87s [done] report expect='FACTORY' cmd=True \| T3 PASS 86s [d |
| 5157 | 2026-10-06 14:44:00 | 5497f756 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 87s [done] report expect='FACTORY' cmd=True \| T3 PASS 86s [d |
| 5158 | 2026-10-06 14:44:00 | f9c5d9ce | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5497f75686eb410db39c01ca0fd4b162", "after_quota": "5497f75686eb410db39c01ca0fd4b |
| 5159 | 2026-10-06 14:44:00 | 5497f756 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5160 | 2026-10-06 14:44:01 | df24e745 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5161 | 2026-10-06 14:52:15 | ecf3b4fe |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5162 | 2026-10-06 14:52:15 | d9f18eed |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-06T15"}} |
| 5163 | 2026-10-06 14:52:39 | ecf3b4fe |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", |
| 5164 | 2026-10-06 14:53:39 | de7e0c02 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5165 | 2026-10-06 14:53:39 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5166 | 2026-10-06 14:53:40 | 074d01d0 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-06T15"}} |
| 5167 | 2026-10-06 14:53:40 | de7e0c02 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5168 | 2026-10-06 14:58:34 | df24e745 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 88s [done] report expect='FACTORY' cmd=True \| T3 PASS 90s [d |
| 5169 | 2026-10-06 14:58:34 | df24e745 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 88s [done] report expect='FACTORY' cmd=True \| T3 PASS 90s [d |
| 5170 | 2026-10-06 14:58:34 | 7f355c4b | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "df24e745ca8143daad1c58a7c3f21ddd", "after_quota": "df24e745ca8143daad1c58a7c3f21 |
| 5171 | 2026-10-06 14:58:34 | df24e745 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5172 | 2026-10-06 14:58:34 | 17403faf | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5173 | 2026-10-06 15:14:56 | 17403faf | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 51s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 96s [done] report expect='FACTORY' cmd=True \| T3 PASS 120s [ |
| 5174 | 2026-10-06 15:14:56 | 17403faf | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 51s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 96s [done] report expect='FACTORY' cmd=True \| T3 PASS 120s [ |
| 5175 | 2026-10-06 15:14:56 | 2a4bed6b | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "17403fafae114f329b45eb4032a3c |
| 5176 | 2026-10-06 15:14:56 | 17403faf | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5177 | 2026-10-06 15:15:00 | 3be89af3 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5178 | 2026-10-06 15:30:21 | 3be89af3 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 45s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 84s [done] report expect='FACTORY' cmd=True \| T3 PASS 94s [d |
| 5179 | 2026-10-06 15:30:21 | 3be89af3 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 45s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 84s [done] report expect='FACTORY' cmd=True \| T3 PASS 94s [d |
| 5180 | 2026-10-06 15:30:21 | 59e6d0c1 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "3be89af3cfd2474896a4a3c1ab0251a4", "after_quota": "3be89af3cfd2474896a4a3c1ab025 |
| 5181 | 2026-10-06 15:30:21 | 3be89af3 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5182 | 2026-10-06 15:30:22 | 41923cc5 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5183 | 2026-10-06 15:45:24 | 41923cc5 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 88s [done] report expect='FACTORY' cmd=True \| T3 PASS 93s [d |
| 5184 | 2026-10-06 15:45:24 | 41923cc5 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 88s [done] report expect='FACTORY' cmd=True \| T3 PASS 93s [d |
| 5185 | 2026-10-06 15:45:24 | b0498475 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "41923cc5baaa4b7ba7c14909b7abe137", "after_quota": "41923cc5baaa4b7ba7c14909b7abe |
| 5186 | 2026-10-06 15:45:24 | 41923cc5 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5187 | 2026-10-06 15:45:27 | 9676251c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5188 | 2026-10-06 15:52:19 | d9f18eed |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5189 | 2026-10-06 15:52:19 | 48fc3c01 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-06T16"}} |
| 5190 | 2026-10-06 15:52:38 | d9f18eed |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash38", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\ |
| 5191 | 2026-10-06 15:52:38 | 024aa1df |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-06", "trigger": "blocked:gemini-flash38"}} |
| 5192 | 2026-10-06 15:52:38 | ee737074 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-06", "trigger": "blocked:gemini-flash38"}} |
| 5193 | 2026-10-06 15:52:38 | 51997579 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-06", "trigger": "blocked:gemini-flash38"}} |
| 5194 | 2026-10-06 15:52:38 | 8e0d8bb8 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-06", "trigger": "blocked:gemini-flash38"}} |
| 5195 | 2026-10-06 15:52:38 | da181f18 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-06", "trigger": "blocked:gemini-flash38"}} |
| 5196 | 2026-10-06 15:52:38 | 758a94a4 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-06", "trigger": "blocked:gemini-flash38"}} |
| 5197 | 2026-10-06 15:52:38 | d9f18eed |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b |
| 5198 | 2026-10-06 15:52:42 | 024aa1df |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5199 | 2026-10-06 15:52:43 | 024aa1df |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5200 | 2026-10-06 15:52:48 | ee737074 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5201 | 2026-10-06 15:52:48 | ee737074 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5202 | 2026-10-06 15:52:53 | 51997579 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5203 | 2026-10-06 15:52:53 | 51997579 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5204 | 2026-10-06 15:52:57 | 8e0d8bb8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5205 | 2026-10-06 15:52:57 | 8e0d8bb8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5206 | 2026-10-06 15:53:02 | da181f18 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5207 | 2026-10-06 15:53:02 | da181f18 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5208 | 2026-10-06 15:53:06 | 758a94a4 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5209 | 2026-10-06 15:53:06 | 758a94a4 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5210 | 2026-10-06 15:53:41 | 074d01d0 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5211 | 2026-10-06 15:53:41 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5212 | 2026-10-06 15:53:42 | 8db17bc2 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-06T16"}} |
| 5213 | 2026-10-06 15:53:42 | 074d01d0 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5214 | 2026-10-06 16:00:51 | 9676251c | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 60s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 89s [done] report expect='FACTORY' cmd=True \| T3 PASS 85s [d |
| 5215 | 2026-10-06 16:00:51 | 9676251c | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 60s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 89s [done] report expect='FACTORY' cmd=True \| T3 PASS 85s [d |
| 5216 | 2026-10-06 16:00:51 | a01459ef | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "9676251c2542467bb5dce76c4844e |
| 5217 | 2026-10-06 16:00:51 | 9676251c | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5218 | 2026-10-06 16:00:53 | eb2b6405 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5219 | 2026-10-06 16:16:42 | eb2b6405 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 93s [done] report expect='FACTORY' cmd=True \| T3 PASS 93s [d |
| 5220 | 2026-10-06 16:16:42 | eb2b6405 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 93s [done] report expect='FACTORY' cmd=True \| T3 PASS 93s [d |
| 5221 | 2026-10-06 16:16:42 | 7313be42 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "f0ad66fce1d34d7ab721da1e4bff23b8", "after_quota": "eb2b6405e57047db8e73e0e4898e7 |
| 5222 | 2026-10-06 16:16:42 | eb2b6405 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5223 | 2026-10-06 16:44:02 | f9c5d9ce | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5224 | 2026-10-06 16:52:20 | 48fc3c01 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5225 | 2026-10-06 16:52:20 | 90523c21 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-06T17"}} |
| 5226 | 2026-10-06 16:53:05 | 48fc3c01 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\":  |
| 5227 | 2026-10-06 16:53:05 | 8e877c8d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-06", "trigger": "blocked:gemini-flash-latest"}} |
| 5228 | 2026-10-06 16:53:05 | 739dd74c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-06", "trigger": "blocked:gemini-flash-latest"}} |
| 5229 | 2026-10-06 16:53:05 | 74dcb2a5 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-06", "trigger": "blocked:gemini-flash-latest"}} |
| 5230 | 2026-10-06 16:53:05 | e59c0b07 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-06", "trigger": "blocked:gemini-flash-latest"}} |
| 5231 | 2026-10-06 16:53:05 | a3f68afa |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-06", "trigger": "blocked:gemini-flash-latest"}} |
| 5232 | 2026-10-06 16:53:05 | afd7e099 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-06", "trigger": "blocked:gemini-flash-latest"}} |
| 5233 | 2026-10-06 16:53:05 | 48fc3c01 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b |
| 5234 | 2026-10-06 16:53:10 | 8e877c8d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5235 | 2026-10-06 16:53:10 | 8e877c8d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5236 | 2026-10-06 16:53:14 | 739dd74c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5237 | 2026-10-06 16:53:14 | 739dd74c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5238 | 2026-10-06 16:53:18 | 74dcb2a5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5239 | 2026-10-06 16:53:18 | 74dcb2a5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5240 | 2026-10-06 16:53:22 | e59c0b07 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5241 | 2026-10-06 16:53:22 | e59c0b07 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5242 | 2026-10-06 16:53:27 | a3f68afa |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5243 | 2026-10-06 16:53:27 | a3f68afa |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5244 | 2026-10-06 16:53:31 | afd7e099 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5245 | 2026-10-06 16:53:31 | afd7e099 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5246 | 2026-10-06 16:53:45 | 8db17bc2 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5247 | 2026-10-06 16:53:45 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5248 | 2026-10-06 16:53:46 | d7038ac8 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-06T17"}} |
| 5249 | 2026-10-06 16:53:46 | 8db17bc2 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5250 | 2026-10-06 16:57:19 | f9c5d9ce | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 84s [done] report expect='FACTORY' cmd=True \| T3 PASS 47s [d |
| 5251 | 2026-10-06 16:57:19 | f9c5d9ce | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 84s [done] report expect='FACTORY' cmd=True \| T3 PASS 47s [d |
| 5252 | 2026-10-06 16:57:19 | 79387b5d | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5497f75686eb410db39c01ca0fd4b162", "after_quota": "f9c5d9cebe5948dcb54f6a5f85779 |
| 5253 | 2026-10-06 16:57:19 | f9c5d9ce | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5254 | 2026-10-06 16:58:35 | 7f355c4b | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5255 | 2026-10-06 17:13:09 | 7f355c4b | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 44s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 85s [done] report expect='FACTORY' cmd=True \| T3 PASS 95s [d |
| 5256 | 2026-10-06 17:13:09 | 7f355c4b | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 44s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 85s [done] report expect='FACTORY' cmd=True \| T3 PASS 95s [d |
| 5257 | 2026-10-06 17:13:09 | 0a2edb66 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "df24e745ca8143daad1c58a7c3f21ddd", "after_quota": "7f355c4be57f4db8b95ef2e0d3313 |
| 5258 | 2026-10-06 17:13:09 | 7f355c4b | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5259 | 2026-10-06 17:14:59 | 2a4bed6b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5260 | 2026-10-06 17:30:03 | 2a4bed6b | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 43s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 91s [done] report expect='FACTORY' cmd=True \| T3 PASS 81s [d |
| 5261 | 2026-10-06 17:30:03 | 2a4bed6b | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 43s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 91s [done] report expect='FACTORY' cmd=True \| T3 PASS 81s [d |
| 5262 | 2026-10-06 17:30:03 | 77246653 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "2a4bed6b27b2412282db10d83f624 |
| 5263 | 2026-10-06 17:30:03 | 2a4bed6b | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5264 | 2026-10-06 17:30:22 | 59e6d0c1 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5265 | 2026-10-06 17:45:48 | 59e6d0c1 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 70s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 79s [done] report expect='FACTORY' cmd=True \| T3 PASS 113s [ |
| 5266 | 2026-10-06 17:45:48 | 59e6d0c1 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 70s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 79s [done] report expect='FACTORY' cmd=True \| T3 PASS 113s [ |
| 5267 | 2026-10-06 17:45:48 | 007adb20 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "3be89af3cfd2474896a4a3c1ab0251a4", "after_quota": "59e6d0c135c84c8ea5b68a746352d |
| 5268 | 2026-10-06 17:45:48 | 59e6d0c1 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5269 | 2026-10-06 17:45:50 | b0498475 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5270 | 2026-10-06 17:52:23 | 90523c21 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5271 | 2026-10-06 17:52:23 | 70e885e4 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-06T18"}} |
| 5272 | 2026-10-06 17:53:48 | 90523c21 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\n  |
| 5273 | 2026-10-06 17:53:48 | 90523c21 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 5274 | 2026-10-06 17:53:48 | dab76f62 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-06", "trigger": "blocked:gemini-flash"}} |
| 5275 | 2026-10-06 17:53:48 | 60bb558d |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-06", "trigger": "blocked:gemini-flash"}} |
| 5276 | 2026-10-06 17:53:48 | e7fa41fc |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-06", "trigger": "blocked:gemini-flash"}} |
| 5277 | 2026-10-06 17:53:48 | ad36a460 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-06", "trigger": "blocked:gemini-flash"}} |
| 5278 | 2026-10-06 17:53:48 | 2021e169 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-06", "trigger": "blocked:gemini-flash"}} |
| 5279 | 2026-10-06 17:53:48 | ac3fc65d |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-06", "trigger": "blocked:gemini-flash"}} |
| 5280 | 2026-10-06 17:53:48 | 90523c21 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash-latest", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "lo |
| 5281 | 2026-10-06 17:53:52 | d7038ac8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5282 | 2026-10-06 17:53:52 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5283 | 2026-10-06 17:53:52 | 70f255b2 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-06T18"}} |
| 5284 | 2026-10-06 17:53:52 | d7038ac8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
