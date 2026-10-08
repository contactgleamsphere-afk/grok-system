# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
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
| 5285 | 2026-10-06 17:53:55 | dab76f62 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5286 | 2026-10-06 17:53:56 | dab76f62 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5287 | 2026-10-06 17:54:00 | 60bb558d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5288 | 2026-10-06 17:54:00 | 60bb558d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5289 | 2026-10-06 17:54:03 | e7fa41fc |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5290 | 2026-10-06 17:54:03 | e7fa41fc |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5291 | 2026-10-06 17:54:07 | ad36a460 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5292 | 2026-10-06 17:54:07 | ad36a460 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5293 | 2026-10-06 17:54:10 | 2021e169 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5294 | 2026-10-06 17:54:10 | 2021e169 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5295 | 2026-10-06 17:54:13 | ac3fc65d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5296 | 2026-10-06 17:54:13 | ac3fc65d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5297 | 2026-10-06 18:00:17 | b0498475 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 46s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 82s [done] report expect='FACTORY' cmd=True \| T3 PASS 80s [d |
| 5298 | 2026-10-06 18:00:17 | b0498475 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 46s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 82s [done] report expect='FACTORY' cmd=True \| T3 PASS 80s [d |
| 5299 | 2026-10-06 18:00:17 | 66e5d795 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "41923cc5baaa4b7ba7c14909b7abe137", "after_quota": "b049847505294477ac0e8e4863972 |
| 5300 | 2026-10-06 18:00:17 | b0498475 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5301 | 2026-10-06 18:00:53 | a01459ef | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5302 | 2026-10-06 18:15:33 | a01459ef | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 44s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 89s [done] report expect='FACTORY' cmd=True \| T3 PASS 82s [d |
| 5303 | 2026-10-06 18:15:33 | a01459ef | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 44s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 89s [done] report expect='FACTORY' cmd=True \| T3 PASS 82s [d |
| 5304 | 2026-10-06 18:15:33 | 0a38da93 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "a01459ef34b24748b78a56f12f35b |
| 5305 | 2026-10-06 18:15:33 | a01459ef | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5306 | 2026-10-06 18:16:42 | 7313be42 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5307 | 2026-10-06 18:31:00 | 7313be42 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 46s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 81s [done] report expect='FACTORY' cmd=True \| T3 PASS 86s [d |
| 5308 | 2026-10-06 18:31:00 | 7313be42 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 46s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 81s [done] report expect='FACTORY' cmd=True \| T3 PASS 86s [d |
| 5309 | 2026-10-06 18:31:00 | 7313be42 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 5310 | 2026-10-06 18:31:00 | 00a4f8d4 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "7313be42371942959294380488bd1a8 |
| 5311 | 2026-10-06 18:31:00 | 7313be42 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5312 | 2026-10-06 18:52:26 | 70e885e4 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5313 | 2026-10-06 18:52:26 | 90e0f175 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-06T19"}} |
| 5314 | 2026-10-06 18:53:11 | 70e885e4 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash38", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 5315 | 2026-10-06 18:53:11 | 70e885e4 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", " |
| 5316 | 2026-10-06 18:53:55 | 70f255b2 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5317 | 2026-10-06 18:53:55 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5318 | 2026-10-06 18:53:56 | 52127838 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-06T19"}} |
| 5319 | 2026-10-06 18:53:56 | 70f255b2 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5320 | 2026-10-06 18:57:20 | 79387b5d | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5321 | 2026-10-06 19:10:39 | 79387b5d | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 75s [done] report expect='FACTORY' cmd=True \| T3 PASS 86s [d |
| 5322 | 2026-10-06 19:10:39 | 79387b5d | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 75s [done] report expect='FACTORY' cmd=True \| T3 PASS 86s [d |
| 5323 | 2026-10-06 19:10:39 | 879e06a3 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5497f75686eb410db39c01ca0fd4b162", "after_quota": "79387b5d22f749239adb0b3b5676f |
| 5324 | 2026-10-06 19:10:39 | 79387b5d | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5325 | 2026-10-06 19:10:42 | 00a4f8d4 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5326 | 2026-10-06 19:25:37 | 00a4f8d4 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 45s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 81s [done] report expect='FACTORY' cmd=True \| T3 PASS 79s [d |
| 5327 | 2026-10-06 19:25:37 | 00a4f8d4 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 45s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 81s [done] report expect='FACTORY' cmd=True \| T3 PASS 79s [d |
| 5328 | 2026-10-06 19:25:37 | 989112db | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "00a4f8d453cd46b3af1d72958415e586", "after_quota": "00a4f8d453cd46b3af1d72958415e |
| 5329 | 2026-10-06 19:25:37 | 00a4f8d4 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5330 | 2026-10-06 19:25:39 | 0a2edb66 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5331 | 2026-10-06 19:42:42 | 0a2edb66 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 46s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 84s [done] report expect='FACTORY' cmd=True \| T3 PASS 199s [ |
| 5332 | 2026-10-06 19:42:42 | 0a2edb66 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 46s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 84s [done] report expect='FACTORY' cmd=True \| T3 PASS 199s [ |
| 5333 | 2026-10-06 19:42:42 | 8083faff | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "df24e745ca8143daad1c58a7c3f21ddd", "after_quota": "0a2edb66cd3248f98367f7026d259 |
| 5334 | 2026-10-06 19:42:42 | 0a2edb66 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5335 | 2026-10-06 19:42:46 | 77246653 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5336 | 2026-10-06 19:52:27 | 90e0f175 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5337 | 2026-10-06 19:52:27 | 5410d886 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-06T20"}} |
| 5338 | 2026-10-06 19:53:10 | 90e0f175 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq- |
| 5339 | 2026-10-06 19:53:59 | 52127838 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5340 | 2026-10-06 19:53:59 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5341 | 2026-10-06 19:53:59 | 90ce8b53 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-06T20"}} |
| 5342 | 2026-10-06 19:53:59 | 52127838 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5343 | 2026-10-06 19:57:39 | 77246653 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 44s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 85s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [d |
| 5344 | 2026-10-06 19:57:39 | 77246653 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 44s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 85s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [d |
| 5345 | 2026-10-06 19:57:39 | 41a32998 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "17403fafae114f329b45eb4032a3c599", "after_quota": "772466532dcc4826855a15d716859 |
| 5346 | 2026-10-06 19:57:39 | 77246653 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5347 | 2026-10-06 19:57:43 | 007adb20 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5348 | 2026-10-06 20:12:23 | 007adb20 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 46s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 83s [done] report expect='FACTORY' cmd=True \| T3 PASS 85s [d |
| 5349 | 2026-10-06 20:12:23 | 007adb20 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 46s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 83s [done] report expect='FACTORY' cmd=True \| T3 PASS 85s [d |
| 5350 | 2026-10-06 20:12:23 | e294457f | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "3be89af3cfd2474896a4a3c1ab0251a4", "after_quota": "007adb20b8834498b1c665f4d9ac4 |
| 5351 | 2026-10-06 20:12:23 | 007adb20 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5352 | 2026-10-06 20:12:24 | 66e5d795 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5353 | 2026-10-06 20:28:12 | 66e5d795 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 84s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [d |
| 5354 | 2026-10-06 20:28:12 | 66e5d795 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 84s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [d |
| 5355 | 2026-10-06 20:28:12 | 1b5eae2b | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "41923cc5baaa4b7ba7c14909b7abe137", "after_quota": "66e5d79544b6455a9cf8aab745565 |
| 5356 | 2026-10-06 20:28:12 | 66e5d795 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5357 | 2026-10-06 20:28:14 | 0a38da93 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5358 | 2026-10-06 20:46:53 | 0a38da93 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 115s [done] report expect='FACTORY' cmd=True \| T3 PASS 162s  |
| 5359 | 2026-10-06 20:46:53 | 0a38da93 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 115s [done] report expect='FACTORY' cmd=True \| T3 PASS 162s  |
| 5360 | 2026-10-06 20:46:53 | 3200a504 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "0a38da9312774e20b07c297fd4127 |
| 5361 | 2026-10-06 20:46:53 | 0a38da93 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 5362 | 2026-10-06 20:52:28 | 5410d886 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5363 | 2026-10-06 20:52:28 | 1c85b500 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-06T21"}} |
| 5364 | 2026-10-06 20:52:46 | 5410d886 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash38", "gemini-gemma26b", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", "local4b"], "c |
| 5365 | 2026-10-06 20:54:00 | 90ce8b53 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5366 | 2026-10-06 20:54:00 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5367 | 2026-10-06 20:54:01 | 4ce09cb7 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-06T21"}} |
| 5368 | 2026-10-06 20:54:01 | 90ce8b53 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5369 | 2026-10-06 21:10:41 | 879e06a3 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5370 | 2026-10-06 23:37:59 | 879e06a3 |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 5371 | 2026-10-06 23:38:00 | 1c85b500 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5372 | 2026-10-07 15:21:48 | 879e06a3 |  | job.readopted | fast-LAPTOP-LRE6PSA8 | {} |
| 5373 | 2026-10-07 15:21:48 | f8e1f6e5 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-07T00"}} |
| 5374 | 2026-10-07 15:23:07 | 1c85b500 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "URLError"} |
| 5375 | 2026-10-07 15:23:07 | 9f252969 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-07", "trigger": "blocked:gemini-flash-latest"}} |
| 5376 | 2026-10-07 15:23:07 | 4cea3d1b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-07", "trigger": "blocked:gemini-flash-latest"}} |
| 5377 | 2026-10-07 15:23:07 | 8f09c864 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-07", "trigger": "blocked:gemini-flash-latest"}} |
| 5378 | 2026-10-07 15:23:07 | 4b8b103b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-07", "trigger": "blocked:gemini-flash-latest"}} |
| 5379 | 2026-10-07 15:23:07 | ca675b53 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-07", "trigger": "blocked:gemini-flash-latest"}} |
| 5380 | 2026-10-07 15:23:07 | d498f52c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-07", "trigger": "blocked:gemini-flash-latest"}} |
| 5381 | 2026-10-07 15:23:07 | 1c85b500 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", "local4b", "or-apod |
| 5382 | 2026-10-07 15:23:11 | 4ce09cb7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5383 | 2026-10-07 15:23:11 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 5384 | 2026-10-07 15:23:12 | 35b91d1a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-07T16"}} |
| 5385 | 2026-10-07 15:23:12 | 4ce09cb7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 5386 | 2026-10-07 15:23:17 | f8e1f6e5 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5387 | 2026-10-07 15:23:17 | 762a5e34 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-07T16"}} |
| 5388 | 2026-10-07 15:25:17 | f8e1f6e5 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\ |
| 5389 | 2026-10-07 15:25:17 | 26c0efd9 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-07", "trigger": "blocked:gemini-flash36"}} |
| 5390 | 2026-10-07 15:25:17 | 17c55e79 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-07", "trigger": "blocked:gemini-flash36"}} |
| 5391 | 2026-10-07 15:25:17 | e9f39103 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-07", "trigger": "blocked:gemini-flash36"}} |
| 5392 | 2026-10-07 15:25:17 | fb296dd4 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-07", "trigger": "blocked:gemini-flash36"}} |
| 5393 | 2026-10-07 15:25:17 | 365a4bf4 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-07", "trigger": "blocked:gemini-flash36"}} |
| 5394 | 2026-10-07 15:25:17 | a1c8b352 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-07", "trigger": "blocked:gemini-flash36"}} |
| 5395 | 2026-10-07 15:25:17 | f8e1f6e5 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gpto |
| 5396 | 2026-10-07 15:25:21 | 9f252969 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5397 | 2026-10-07 15:25:21 | 9f252969 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5398 | 2026-10-07 15:25:26 | 4cea3d1b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5399 | 2026-10-07 15:25:27 | 4cea3d1b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5400 | 2026-10-07 15:25:32 | 8f09c864 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5401 | 2026-10-07 15:25:35 | 8f09c864 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5402 | 2026-10-07 15:25:40 | 4b8b103b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5403 | 2026-10-07 15:25:40 | 4b8b103b |  | owner.needed | svc-LAPTOP-LRE6PSA8 | {"provider": "cerebras", "reason": "set CEREBRAS_API_KEY (User env) after signing up: https://cloud.cerebras.ai (free tier ~1M tokens/day)"} |
| 5404 | 2026-10-07 15:25:40 | 4b8b103b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5405 | 2026-10-07 15:25:44 | ca675b53 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5406 | 2026-10-07 15:25:44 | ca675b53 |  | owner.needed | svc-LAPTOP-LRE6PSA8 | {"provider": "nvidia", "reason": "set NVIDIA_API_KEY (User env) after signing up: https://build.nvidia.com (free ~40 rpm, tool-capable model |
| 5407 | 2026-10-07 15:25:44 | ca675b53 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5408 | 2026-10-07 15:25:48 | d498f52c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5409 | 2026-10-07 15:25:48 | d498f52c |  | owner.needed | svc-LAPTOP-LRE6PSA8 | {"provider": "mistral", "reason": "set MISTRAL_API_KEY (User env) after signing up: https://console.mistral.ai (Experiment free tier)"} |
| 5410 | 2026-10-07 15:25:48 | d498f52c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 5411 | 2026-10-07 15:25:52 | 26c0efd9 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 5412 | 2026-10-07 15:25:54 | 26c0efd9 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 5413 | 2026-10-07 15:28:08 | 879e06a3 | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 5414 | 2026-10-07 15:30:09 | 17c55e79 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
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
