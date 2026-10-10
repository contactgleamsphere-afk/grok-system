# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
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
| 6079 | 2026-10-09 22:06:35 | 909d4e4b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6080 | 2026-10-09 22:18:00 | 909d4e4b | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 6081 | 2026-10-09 22:18:00 | 909d4e4b | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 6082 | 2026-10-09 22:18:00 | 2f157f08 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5fd9d18c4aa1414aafe3e0fba01dde29", "after_quota": "909d4e4b637d4966bd7c35c7d96b1 |
| 6083 | 2026-10-09 22:18:00 | 909d4e4b | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6084 | 2026-10-09 22:18:01 | d9e6e57e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6085 | 2026-10-09 22:29:11 | d9e6e57e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6086 | 2026-10-09 22:29:11 | d9e6e57e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 6087 | 2026-10-09 22:29:11 | 7e4ce7d2 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ab5d10624c564c16b855f074ef29fa09", "after_quota": "d9e6e57eb768468e89fb05673e4a8 |
| 6088 | 2026-10-09 22:29:11 | d9e6e57e | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6089 | 2026-10-09 22:29:15 | 63b3b071 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6090 | 2026-10-09 22:41:10 | 63b3b071 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 6091 | 2026-10-09 22:41:10 | 63b3b071 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 6092 | 2026-10-09 22:41:10 | 18a1cfe8 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "63b3b07178d24c138fa4079bf61c4073", "after_quota": "63b3b07178d24c138fa4079bf61c4 |
| 6093 | 2026-10-09 22:41:10 | 63b3b071 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6094 | 2026-10-09 22:41:10 | d13e7377 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6095 | 2026-10-09 22:52:57 | d13e7377 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 73s [d |
| 6096 | 2026-10-09 22:52:57 | d13e7377 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 73s [d |
| 6097 | 2026-10-09 22:52:57 | 6472c8da | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "9aa0054ee0124b40bb21b2daef2bc049", "after_quota": "d13e7377bf2642a3aa085620d52ba |
| 6098 | 2026-10-09 22:52:57 | d13e7377 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6099 | 2026-10-09 22:52:59 | cceb6137 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6100 | 2026-10-09 23:04:20 | bfd8b8ea |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6101 | 2026-10-09 23:04:20 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 6102 | 2026-10-09 23:04:22 | 8a1e233b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-10T00"}} |
| 6103 | 2026-10-09 23:04:22 | bfd8b8ea |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6104 | 2026-10-09 23:04:25 | cceb6137 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 47s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 6105 | 2026-10-09 23:04:25 | cceb6137 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 47s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 6106 | 2026-10-09 23:04:25 | 8f7a3355 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "d2e1729a75cc4dd499e5716e334fcec1", "after_quota": "cceb6137a7634b06b39cdccafea38 |
| 6107 | 2026-10-09 23:04:25 | cceb6137 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6108 | 2026-10-09 23:04:29 | 838c36cb |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6109 | 2026-10-09 23:04:29 | 97b8924c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-10T00"}} |
| 6110 | 2026-10-09 23:04:37 | 7effb335 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6111 | 2026-10-09 23:05:05 | 838c36cb |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 6112 | 2026-10-09 23:19:00 | 7effb335 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 97s [done] report expect='FACTORY' cmd=True \| T3 PASS 88s [d |
| 6113 | 2026-10-09 23:19:00 | 7effb335 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 97s [done] report expect='FACTORY' cmd=True \| T3 PASS 88s [d |
| 6114 | 2026-10-09 23:19:00 | 6284f181 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "7effb335b9004c2eb6744408d5ff5 |
| 6115 | 2026-10-09 23:19:00 | 7effb335 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6116 | 2026-10-09 23:19:01 | 082d548a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6117 | 2026-10-09 23:30:54 | 082d548a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 6118 | 2026-10-09 23:30:54 | 082d548a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 6119 | 2026-10-09 23:30:54 | 95313df2 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "41923cc5baaa4b7ba7c14909b7abe137", "after_quota": "082d548a059d47c0b6693d6c9d747 |
| 6120 | 2026-10-09 23:30:54 | 082d548a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6121 | 2026-10-09 23:30:55 | 7b939e15 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6122 | 2026-10-09 23:44:05 | 7b939e15 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 74s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 79s [done] report expect='FACTORY' cmd=True \| T3 PASS 73s [d |
| 6123 | 2026-10-09 23:44:05 | 7b939e15 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 74s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 79s [done] report expect='FACTORY' cmd=True \| T3 PASS 73s [d |
| 6124 | 2026-10-09 23:44:05 | e87b6b40 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "7b939e1502824fbd91f70a48cf80f |
| 6125 | 2026-10-09 23:44:05 | 7b939e15 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6126 | 2026-10-09 23:44:09 | 23700797 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6127 | 2026-10-09 23:55:52 | 23700797 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 56s [d |
| 6128 | 2026-10-09 23:55:52 | 23700797 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 56s [d |
| 6129 | 2026-10-09 23:55:52 | b6f952f7 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "b55e8b342b7b4b37acedb240a933539f", "after_quota": "23700797a5cf486f955701314690b |
| 6130 | 2026-10-09 23:55:52 | 23700797 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6131 | 2026-10-10 00:04:26 | 8a1e233b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6132 | 2026-10-10 00:04:26 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 6133 | 2026-10-10 00:04:26 | 38ffcb70 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-10T01"}} |
| 6134 | 2026-10-10 00:04:26 | 8a1e233b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6135 | 2026-10-10 00:04:30 | 97b8924c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6136 | 2026-10-10 00:04:30 | 6757cbd5 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-10T01"}} |
| 6137 | 2026-10-10 00:05:10 | 97b8924c |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 6138 | 2026-10-10 00:05:10 | 37e608b8 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-10", "trigger": "blocked:gemini-flash36"}} |
| 6139 | 2026-10-10 00:05:10 | c8ab344c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-10", "trigger": "blocked:gemini-flash36"}} |
| 6140 | 2026-10-10 00:05:10 | 283647a6 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-10", "trigger": "blocked:gemini-flash36"}} |
| 6141 | 2026-10-10 00:05:10 | 06a2063f |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-10", "trigger": "blocked:gemini-flash36"}} |
| 6142 | 2026-10-10 00:05:10 | f23e2d50 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-10", "trigger": "blocked:gemini-flash36"}} |
| 6143 | 2026-10-10 00:05:10 | 7e972e6f |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-10", "trigger": "blocked:gemini-flash36"}} |
| 6144 | 2026-10-10 00:05:10 | 97b8924c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss1 |
| 6145 | 2026-10-10 00:05:11 | 37e608b8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6146 | 2026-10-10 00:05:12 | 37e608b8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 6147 | 2026-10-10 00:05:14 | c8ab344c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6148 | 2026-10-10 00:05:14 | c8ab344c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6149 | 2026-10-10 00:05:17 | 283647a6 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6150 | 2026-10-10 00:05:17 | 283647a6 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6151 | 2026-10-10 00:05:21 | 06a2063f |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6152 | 2026-10-10 00:05:21 | 06a2063f |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6153 | 2026-10-10 00:05:25 | f23e2d50 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6154 | 2026-10-10 00:05:25 | f23e2d50 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6155 | 2026-10-10 00:05:29 | 7e972e6f |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6156 | 2026-10-10 00:05:29 | 7e972e6f |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 6157 | 2026-10-10 00:06:33 | fac9e34b | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6158 | 2026-10-10 00:21:03 | fac9e34b | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 6159 | 2026-10-10 00:21:03 | fac9e34b | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 6160 | 2026-10-10 00:21:03 | fac9e34b | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 6161 | 2026-10-10 00:21:03 | 8cec1d2e | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "fac9e34b00f14092967f642ed368aeb |
| 6162 | 2026-10-10 00:21:03 | fac9e34b | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6163 | 2026-10-10 00:21:04 | 2f157f08 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6164 | 2026-10-10 00:32:56 | 2f157f08 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 6165 | 2026-10-10 00:32:56 | 2f157f08 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 6166 | 2026-10-10 00:32:56 | 96662f05 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5fd9d18c4aa1414aafe3e0fba01dde29", "after_quota": "2f157f08b5c74bcb8ceeb21a03a20 |
| 6167 | 2026-10-10 00:32:56 | 2f157f08 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6168 | 2026-10-10 00:32:57 | 7e4ce7d2 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6169 | 2026-10-10 00:44:07 | 7e4ce7d2 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 56s [d |
| 6170 | 2026-10-10 00:44:07 | 7e4ce7d2 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 56s [d |
| 6171 | 2026-10-10 00:44:08 | d362fb80 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ab5d10624c564c16b855f074ef29fa09", "after_quota": "7e4ce7d2691242d68c9bdd01fc68d |
| 6172 | 2026-10-10 00:44:08 | 7e4ce7d2 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6173 | 2026-10-10 00:44:09 | 18a1cfe8 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6174 | 2026-10-10 00:57:14 | 18a1cfe8 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 74s [d |
| 6175 | 2026-10-10 00:57:14 | 18a1cfe8 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 74s [d |
| 6176 | 2026-10-10 00:57:14 | 18a1cfe8 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 6177 | 2026-10-10 00:57:14 | 8affd9ea | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "f174fbc671544e27bad96250dd6ea9e2", "retry_of": "18a1cfe862324976979afefff5158b5 |
| 6178 | 2026-10-10 00:57:14 | 18a1cfe8 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6179 | 2026-10-10 00:57:17 | 8cec1d2e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6180 | 2026-10-10 01:03:43 | 8cec1d2e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 63s [d |
| 6181 | 2026-10-10 01:03:43 | 8cec1d2e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 63s [d |
| 6182 | 2026-10-10 01:03:43 | 8cec1d2e | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 6183 | 2026-10-10 01:03:43 | 139734ae | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "8cec1d2e48784ef5bb3a66063b22887 |
| 6184 | 2026-10-10 01:03:43 | 8cec1d2e | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6185 | 2026-10-10 01:03:44 | 6472c8da | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6186 | 2026-10-10 01:04:31 | 38ffcb70 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6187 | 2026-10-10 01:04:31 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 6188 | 2026-10-10 01:04:32 | 95cedfc7 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-10T02"}} |
| 6189 | 2026-10-10 01:04:32 | 38ffcb70 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6190 | 2026-10-10 01:04:33 | 6757cbd5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6191 | 2026-10-10 01:04:33 | 30a0c9b0 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-10T02"}} |
| 6192 | 2026-10-10 01:05:09 | 6757cbd5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini |
| 6193 | 2026-10-10 01:12:39 | 6472c8da | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 16s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 6194 | 2026-10-10 01:12:39 | 6472c8da | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 16s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 6195 | 2026-10-10 01:12:39 | 3992735d | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "9aa0054ee0124b40bb21b2daef2bc049", "after_quota": "6472c8da450443678010d40ae998a |
| 6196 | 2026-10-10 01:12:39 | 6472c8da | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6197 | 2026-10-10 01:12:43 | 8f7a3355 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6198 | 2026-10-10 01:24:30 | 8f7a3355 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 76s [done] report expect='FACTORY' cmd=True \| T3 PASS 62s [d |
| 6199 | 2026-10-10 01:24:30 | 8f7a3355 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 76s [done] report expect='FACTORY' cmd=True \| T3 PASS 62s [d |
| 6200 | 2026-10-10 01:24:30 | 50d208b3 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "d2e1729a75cc4dd499e5716e334fcec1", "after_quota": "8f7a3355fa6947119c960aec1e428 |
| 6201 | 2026-10-10 01:24:30 | 8f7a3355 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6202 | 2026-10-10 01:24:30 | 6284f181 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6203 | 2026-10-10 01:40:58 | 6284f181 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 198s [ |
| 6204 | 2026-10-10 01:40:58 | 6284f181 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 198s [ |
| 6205 | 2026-10-10 01:40:58 | dd4de290 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "6284f181f7084a49bd6dd92de0558 |
| 6206 | 2026-10-10 01:40:58 | 6284f181 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6207 | 2026-10-10 01:40:59 | 8affd9ea | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6208 | 2026-10-10 01:53:04 | 8affd9ea | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 63s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 6209 | 2026-10-10 01:53:04 | 8affd9ea | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 63s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 6210 | 2026-10-10 01:53:04 | 3276a941 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "8affd9ea9584421dbd15aa5168a98c50", "after_quota": "8affd9ea9584421dbd15aa5168a98 |
| 6211 | 2026-10-10 01:53:04 | 8affd9ea | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6212 | 2026-10-10 01:53:06 | 139734ae | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6213 | 2026-10-10 02:04:21 | 139734ae | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 50s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 6214 | 2026-10-10 02:04:21 | 139734ae | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 50s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 6215 | 2026-10-10 02:04:21 | b0b40d7c | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "139734ae344e49089147d3f47942ffc6", "after_quota": "139734ae344e49089147d3f47942f |
| 6216 | 2026-10-10 02:04:21 | 139734ae | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6217 | 2026-10-10 02:04:22 | 95313df2 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6218 | 2026-10-10 02:04:35 | 95cedfc7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6219 | 2026-10-10 02:04:35 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 6220 | 2026-10-10 02:04:36 | c2019829 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-10T03"}} |
| 6221 | 2026-10-10 02:04:36 | 95cedfc7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6222 | 2026-10-10 02:04:39 | 30a0c9b0 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6223 | 2026-10-10 02:04:39 | af260709 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-10T03"}} |
| 6224 | 2026-10-10 02:04:48 | 30a0c9b0 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gpto |
| 6225 | 2026-10-10 02:16:57 | 95313df2 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 86s [done] report expect='FACTORY' cmd=True \| T3 PASS 110s [ |
| 6226 | 2026-10-10 02:16:57 | 95313df2 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 86s [done] report expect='FACTORY' cmd=True \| T3 PASS 110s [ |
| 6227 | 2026-10-10 02:16:57 | 6c6f3109 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "41923cc5baaa4b7ba7c14909b7abe137", "after_quota": "95313df2c0884b3a82ce2c5c6f893 |
| 6228 | 2026-10-10 02:16:57 | 95313df2 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6229 | 2026-10-10 02:17:02 | e87b6b40 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6230 | 2026-10-10 02:28:14 | e87b6b40 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 57s [d |
| 6231 | 2026-10-10 02:28:14 | e87b6b40 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 57s [d |
| 6232 | 2026-10-10 02:28:14 | a8cf88c3 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "e87b6b408f0848d3ac5864e192118 |
| 6233 | 2026-10-10 02:28:14 | e87b6b40 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6234 | 2026-10-10 02:28:17 | b6f952f7 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6235 | 2026-10-10 02:40:01 | b6f952f7 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 62s [d |
| 6236 | 2026-10-10 02:40:01 | b6f952f7 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 62s [d |
| 6237 | 2026-10-10 02:40:01 | 28520876 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "b55e8b342b7b4b37acedb240a933539f", "after_quota": "b6f952f7ebb848e69c505de758405 |
| 6238 | 2026-10-10 02:40:01 | b6f952f7 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6239 | 2026-10-10 02:40:04 | 96662f05 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6240 | 2026-10-10 02:52:21 | 96662f05 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [d |
| 6241 | 2026-10-10 02:52:21 | 96662f05 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [d |
| 6242 | 2026-10-10 02:52:21 | e780eed9 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5fd9d18c4aa1414aafe3e0fba01dde29", "after_quota": "96662f05632c40e4ac3984ad7c659 |
| 6243 | 2026-10-10 02:52:21 | 96662f05 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6244 | 2026-10-10 02:52:25 | d362fb80 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6245 | 2026-10-10 03:04:02 | d362fb80 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 6246 | 2026-10-10 03:04:02 | d362fb80 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 6247 | 2026-10-10 03:04:02 | b7c3fc31 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ab5d10624c564c16b855f074ef29fa09", "after_quota": "d362fb8073744e97b4876f8bb0921 |
| 6248 | 2026-10-10 03:04:02 | d362fb80 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6249 | 2026-10-10 03:04:40 | c2019829 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6250 | 2026-10-10 03:04:40 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 6251 | 2026-10-10 03:04:41 | af260709 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6252 | 2026-10-10 03:04:41 | c76da1c9 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-10T04"}} |
| 6253 | 2026-10-10 03:04:41 | e712583d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-10T04"}} |
| 6254 | 2026-10-10 03:04:41 | c2019829 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6255 | 2026-10-10 03:04:51 | af260709 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 6256 | 2026-10-10 03:04:51 | af260709 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 6257 | 2026-10-10 03:12:39 | 3992735d | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6258 | 2026-10-10 03:24:19 | 3992735d | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 29s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 64s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 6259 | 2026-10-10 03:24:19 | 3992735d | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 29s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 64s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 6260 | 2026-10-10 03:24:19 | 54df4cbc | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "9aa0054ee0124b40bb21b2daef2bc049", "after_quota": "3992735d50dd45b995c31ecdfcdab |
| 6261 | 2026-10-10 03:24:19 | 3992735d | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6262 | 2026-10-10 03:24:30 | 50d208b3 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6263 | 2026-10-10 03:30:16 | 43103e8f |  | job.enqueued | nightly-task | {"kind": "monitor", "payload": {"only": null, "day": "2026-10-10"}} |
| 6264 | 2026-10-10 03:30:17 | 43103e8f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6265 | 2026-10-10 03:30:17 | 061e6085 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "43103e8f79ba46789af203ddbfb9e1ab", "day": "2026-10-10"}} |
| 6266 | 2026-10-10 03:30:17 | d539c4b2 | 031 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "031", "monitor_of": "43103e8f79ba46789af203ddbfb9e1ab", "day": "2026-10-10"}} |
| 6267 | 2026-10-10 03:30:17 | 43103e8f |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "031"], "jobs": ["061e6085", "d539c4b2"]} |
| 6268 | 2026-10-10 03:30:17 | 43103e8f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6269 | 2026-10-10 03:30:22 | d539c4b2 | 031 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6270 | 2026-10-10 03:31:05 | d539c4b2 | 031 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] expect='X_OK' last='X_OK' \| T2 PASS 11s [done] expect='3' last='RESULT: 3' \| T3 PASS 10s [done] expect='2'  |
| 6271 | 2026-10-10 03:31:05 | d539c4b2 | 031 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] expect='X_OK' last='X_OK' \| T2 PASS 11s [done] expect='3' last='RESULT: 3' \| T3 PASS 10s [done] expect='2'  |
| 6272 | 2026-10-10 03:31:05 | d539c4b2 | 031 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "031", "status": "active", "verified": "VERIFIED"}} |
| 6273 | 2026-10-10 03:35:10 | 50d208b3 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 31s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 6274 | 2026-10-10 03:35:10 | 50d208b3 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 31s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 6275 | 2026-10-10 03:35:10 | 9574aaa8 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "d2e1729a75cc4dd499e5716e334fcec1", "after_quota": "50d208b34d63454c8fad381633a9e |
| 6276 | 2026-10-10 03:35:10 | 50d208b3 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6277 | 2026-10-10 03:35:13 | 061e6085 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6278 | 2026-10-10 03:46:31 | 061e6085 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 49s [done] report expect='FACTORY' cmd=True \| T3 PASS 54s [d |
| 6279 | 2026-10-10 03:46:31 | 061e6085 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 49s [done] report expect='FACTORY' cmd=True \| T3 PASS 54s [d |
| 6280 | 2026-10-10 03:46:31 | f4fb2409 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "061e60858b6b40ab97cdcb408451a9e8", "after_quota": "061e60858b6b40ab97cdcb408451a |
| 6281 | 2026-10-10 03:46:31 | 061e6085 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6282 | 2026-10-10 03:46:34 | dd4de290 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6283 | 2026-10-10 03:58:11 | dd4de290 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 6284 | 2026-10-10 03:58:12 | dd4de290 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 6285 | 2026-10-10 03:58:12 | 7bb1cb35 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "dd4de290ee2f44598862fa2e608cc |
| 6286 | 2026-10-10 03:58:12 | dd4de290 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6287 | 2026-10-10 03:58:15 | 3276a941 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6288 | 2026-10-10 04:04:41 | c76da1c9 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6289 | 2026-10-10 04:04:41 | 8c5240d0 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-10T05"}} |
| 6290 | 2026-10-10 04:05:01 | c76da1c9 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 6291 | 2026-10-10 04:05:04 | e712583d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6292 | 2026-10-10 04:05:04 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 6293 | 2026-10-10 04:05:05 | 071b50f9 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-10T05"}} |
| 6294 | 2026-10-10 04:05:05 | e712583d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6295 | 2026-10-10 04:10:37 | 3276a941 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 6296 | 2026-10-10 04:10:37 | 3276a941 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 6297 | 2026-10-10 04:10:37 | 2027168a | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "8affd9ea9584421dbd15aa5168a98c50", "after_quota": "3276a9413fb344b48aa6b9f70c716 |
| 6298 | 2026-10-10 04:10:37 | 3276a941 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6299 | 2026-10-10 04:10:38 | b0b40d7c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6300 | 2026-10-10 04:22:25 | b0b40d7c | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 57s [d |
| 6301 | 2026-10-10 04:22:25 | b0b40d7c | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 57s [d |
| 6302 | 2026-10-10 04:22:25 | db955230 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "139734ae344e49089147d3f47942ffc6", "after_quota": "b0b40d7c00174e6d9e6da4aef228a |
| 6303 | 2026-10-10 04:22:25 | b0b40d7c | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6304 | 2026-10-10 04:22:27 | 6c6f3109 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6305 | 2026-10-10 04:34:13 | 6c6f3109 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 54s [done] report expect='FACTORY' cmd=True \| T3 PASS 57s [d |
| 6306 | 2026-10-10 04:34:13 | 6c6f3109 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 54s [done] report expect='FACTORY' cmd=True \| T3 PASS 57s [d |
| 6307 | 2026-10-10 04:34:13 | 4a8210eb | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "41923cc5baaa4b7ba7c14909b7abe137", "after_quota": "6c6f31093cb041d9bf800a0677e6c |
| 6308 | 2026-10-10 04:34:13 | 6c6f3109 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6309 | 2026-10-10 04:34:14 | a8cf88c3 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6310 | 2026-10-10 04:46:56 | a8cf88c3 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 6311 | 2026-10-10 04:46:56 | a8cf88c3 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 6312 | 2026-10-10 04:46:56 | ceb0fb9b | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "a8cf88c348e24f058fb76014556c5 |
| 6313 | 2026-10-10 04:46:56 | a8cf88c3 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6314 | 2026-10-10 04:46:58 | 28520876 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6315 | 2026-10-10 04:59:10 | 28520876 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 93s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 6316 | 2026-10-10 04:59:10 | 28520876 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 93s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 6317 | 2026-10-10 04:59:10 | db4d01a3 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "b55e8b342b7b4b37acedb240a933539f", "after_quota": "28520876440f44beaccf97acb3ddc |
| 6318 | 2026-10-10 04:59:10 | 28520876 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 6319 | 2026-10-10 04:59:13 | e780eed9 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6320 | 2026-10-10 05:04:45 | 8c5240d0 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6321 | 2026-10-10 05:04:45 | 37c2acb5 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-10T06"}} |
| 6322 | 2026-10-10 05:05:08 | 8c5240d0 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 6323 | 2026-10-10 05:05:08 | a48e4687 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-10", "trigger": "blocked:gemini-flash36"}} |
| 6324 | 2026-10-10 05:05:08 | 5e1d815b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-10", "trigger": "blocked:gemini-flash36"}} |
| 6325 | 2026-10-10 05:05:08 | fe03e6c1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-10", "trigger": "blocked:gemini-flash36"}} |
| 6326 | 2026-10-10 05:05:08 | c8eb4400 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-10", "trigger": "blocked:gemini-flash36"}} |
| 6327 | 2026-10-10 05:05:08 | f32db6d3 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-10", "trigger": "blocked:gemini-flash36"}} |
| 6328 | 2026-10-10 05:05:08 | 0cefaaa1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-10", "trigger": "blocked:gemini-flash36"}} |
| 6329 | 2026-10-10 05:05:08 | 8c5240d0 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gpto |
| 6330 | 2026-10-10 05:05:11 | 071b50f9 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6331 | 2026-10-10 05:05:11 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 6332 | 2026-10-10 05:05:12 | d94dd50c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-10T06"}} |
| 6333 | 2026-10-10 05:05:12 | 071b50f9 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 6334 | 2026-10-10 05:05:15 | a48e4687 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6335 | 2026-10-10 05:05:15 | a48e4687 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 6336 | 2026-10-10 05:05:19 | 5e1d815b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6337 | 2026-10-10 05:05:29 | 5e1d815b |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-2.5-flash", "reason": "probe gone: [{\n  \"error\": {\n    \"code\": 404,\n    \"message\": \"this model models/gemini-2.5 |
| 6338 | 2026-10-10 05:05:29 | 5e1d815b |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-2.5-flash-lite", "reason": "probe gone: [{\n  \"error\": {\n    \"code\": 404,\n    \"message\": \"this model models/gemin |
| 6339 | 2026-10-10 05:05:29 | 5e1d815b |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-3-flash-preview", "reason": "probe no_tool_call: ", "provider": "gemini"} |
| 6340 | 2026-10-10 05:05:29 | 5e1d815b |  | lane.rejected | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-3.5-flash", "reason": "loop: final answer '4'", "provider": "gemini"} |
| 6341 | 2026-10-10 05:05:29 | 5e1d815b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 6342 | 2026-10-10 05:05:32 | fe03e6c1 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 6343 | 2026-10-10 05:05:35 | fe03e6c1 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
