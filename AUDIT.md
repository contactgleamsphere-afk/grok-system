# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
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
| 7381 | 2026-10-13 03:42:18 | 5524de8c | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7382 | 2026-10-13 04:04:01 | 5524de8c | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 166s [done] report expect='FACTORY' cmd=False \| T3 FAIL 245s |
| 7383 | 2026-10-13 04:04:01 | 5524de8c | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 166s [done] report expect='FACTORY' cmd=False \| T3 FAIL 245s |
| 7384 | 2026-10-13 04:04:01 | 5524de8c | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7385 | 2026-10-13 04:04:01 | d2b1b3ff | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "43103e8f79ba46789af203ddbfb9e1ab", "retry_of": "5524de8c1dde43fcbde84b930211660 |
| 7386 | 2026-10-13 04:04:01 | 5524de8c | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 1, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7387 | 2026-10-13 04:04:02 | 698180d8 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7388 | 2026-10-13 04:04:46 | 0a51ed8f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7389 | 2026-10-13 04:04:47 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7390 | 2026-10-13 04:04:47 | 30b7be50 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-13T05"}} |
| 7391 | 2026-10-13 04:04:47 | 0a51ed8f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7392 | 2026-10-13 04:04:56 | 6db6e081 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7393 | 2026-10-13 04:04:56 | 5427a0cf |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-13T05"}} |
| 7394 | 2026-10-13 04:05:16 | 6db6e081 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 7395 | 2026-10-13 04:05:16 | 6db6e081 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gem |
| 7396 | 2026-10-13 04:21:18 | 698180d8 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 50s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 90s [done] report expect='FACTORY' cmd=False \| T3 FAIL 170s  |
| 7397 | 2026-10-13 04:21:18 | 698180d8 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 50s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 90s [done] report expect='FACTORY' cmd=False \| T3 FAIL 170s  |
| 7398 | 2026-10-13 04:21:18 | 698180d8 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7399 | 2026-10-13 04:21:18 | b3ab4afa | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "698180d8a20a48ca9f46be19c196ac6 |
| 7400 | 2026-10-13 04:21:18 | 698180d8 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 2, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7401 | 2026-10-13 04:21:19 | 93fc5c42 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7402 | 2026-10-13 04:40:16 | 93fc5c42 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 53s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 93s [done] report expect='FACTORY' cmd=False \| T3 FAIL 164s  |
| 7403 | 2026-10-13 04:40:16 | 93fc5c42 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 53s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 93s [done] report expect='FACTORY' cmd=False \| T3 FAIL 164s  |
| 7404 | 2026-10-13 04:40:16 | 93fc5c42 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7405 | 2026-10-13 04:40:16 | d6343b48 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "retry_of": "93fc5c4286d9478aacc1ebf93de8ef4 |
| 7406 | 2026-10-13 04:40:16 | 93fc5c42 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 2, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7407 | 2026-10-13 04:40:20 | d2b1b3ff | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7408 | 2026-10-13 04:57:43 | d2b1b3ff | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 43s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 54s [done] report expect='FACTORY' cmd=False \| T3 FAIL 156s  |
| 7409 | 2026-10-13 04:57:43 | d2b1b3ff | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 43s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 54s [done] report expect='FACTORY' cmd=False \| T3 FAIL 156s  |
| 7410 | 2026-10-13 04:57:43 | d2b1b3ff | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7411 | 2026-10-13 04:57:43 | d94c7611 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "43103e8f79ba46789af203ddbfb9e1ab", "retry_of": "d2b1b3ffc6db4a96b9d9baea664bc86 |
| 7412 | 2026-10-13 04:57:43 | d2b1b3ff | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 2, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7413 | 2026-10-13 04:57:46 | b3ab4afa | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7414 | 2026-10-13 05:04:48 | 30b7be50 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7415 | 2026-10-13 05:04:48 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7416 | 2026-10-13 05:04:49 | 7e0bf6cd |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-13T06"}} |
| 7417 | 2026-10-13 05:04:49 | 30b7be50 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7418 | 2026-10-13 05:04:59 | 5427a0cf |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7419 | 2026-10-13 05:04:59 | a4edddc0 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-13T06"}} |
| 7420 | 2026-10-13 05:05:15 | 5427a0cf |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 7421 | 2026-10-13 05:05:16 | 2fe26cd9 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-13", "trigger": "blocked:gemini-flash36"}} |
| 7422 | 2026-10-13 05:05:16 | f8633ff8 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-13", "trigger": "blocked:gemini-flash36"}} |
| 7423 | 2026-10-13 05:05:16 | 3a9b2f5b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-13", "trigger": "blocked:gemini-flash36"}} |
| 7424 | 2026-10-13 05:05:16 | 507de104 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-13", "trigger": "blocked:gemini-flash36"}} |
| 7425 | 2026-10-13 05:05:16 | 888a2931 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-13", "trigger": "blocked:gemini-flash36"}} |
| 7426 | 2026-10-13 05:05:16 | 439d408a |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-13", "trigger": "blocked:gemini-flash36"}} |
| 7427 | 2026-10-13 05:05:16 | 5427a0cf |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gpto |
| 7428 | 2026-10-13 05:05:24 | 2fe26cd9 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7429 | 2026-10-13 05:05:24 | 2fe26cd9 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7430 | 2026-10-13 05:05:27 | f8633ff8 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7431 | 2026-10-13 05:05:28 | f8633ff8 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7432 | 2026-10-13 05:05:31 | 3a9b2f5b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7433 | 2026-10-13 05:05:31 | 3a9b2f5b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7434 | 2026-10-13 05:05:34 | 507de104 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7435 | 2026-10-13 05:05:34 | 507de104 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7436 | 2026-10-13 05:05:37 | 888a2931 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7437 | 2026-10-13 05:05:38 | 888a2931 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7438 | 2026-10-13 05:05:41 | 439d408a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7439 | 2026-10-13 05:05:41 | 439d408a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7440 | 2026-10-13 05:16:08 | b3ab4afa | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 75s [done] report expect='FACTORY' cmd=False \| T3 FAIL 77s [ |
| 7441 | 2026-10-13 05:16:08 | b3ab4afa | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 75s [done] report expect='FACTORY' cmd=False \| T3 FAIL 77s [ |
| 7442 | 2026-10-13 05:16:08 | b3ab4afa | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7443 | 2026-10-13 05:16:08 | e0916f59 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "b3ab4afaf56448638cfc1ec3a2d981a |
| 7444 | 2026-10-13 05:16:08 | b3ab4afa | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7445 | 2026-10-13 05:16:10 | d6343b48 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7446 | 2026-10-13 05:32:49 | d6343b48 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 68s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 170s [done] report expect='FACTORY' cmd=False \| T3 FAIL 168s |
| 7447 | 2026-10-13 05:32:49 | d6343b48 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 68s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 170s [done] report expect='FACTORY' cmd=False \| T3 FAIL 168s |
| 7448 | 2026-10-13 05:32:49 | d6343b48 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7449 | 2026-10-13 05:32:49 | 59337fcb | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "retry_of": "d6343b483c104acf95afeb715f9e1cd |
| 7450 | 2026-10-13 05:32:49 | d6343b48 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7451 | 2026-10-13 05:32:52 | d94c7611 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7452 | 2026-10-13 05:46:58 | d94c7611 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 75s [done] report expect='FACTORY' cmd=False \| T3 FAIL 166s  |
| 7453 | 2026-10-13 05:46:58 | d94c7611 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 75s [done] report expect='FACTORY' cmd=False \| T3 FAIL 166s  |
| 7454 | 2026-10-13 05:46:58 | d94c7611 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7455 | 2026-10-13 05:46:58 | 3015c529 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "43103e8f79ba46789af203ddbfb9e1ab", "retry_of": "d94c76115a734b16a5f1456c2f12422 |
| 7456 | 2026-10-13 05:46:58 | d94c7611 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7457 | 2026-10-13 05:47:02 | e0916f59 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7458 | 2026-10-13 05:58:46 | e0916f59 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 74s [done] report expect='FACTORY' cmd=False \| T3 FAIL 76s [ |
| 7459 | 2026-10-13 05:58:46 | e0916f59 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 74s [done] report expect='FACTORY' cmd=False \| T3 FAIL 76s [ |
| 7460 | 2026-10-13 05:58:46 | e0916f59 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7461 | 2026-10-13 05:58:46 | 680335d1 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "e0916f595c694ab1990f0cf03a47dff |
| 7462 | 2026-10-13 05:58:46 | e0916f59 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7463 | 2026-10-13 05:58:49 | 1523484a | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7464 | 2026-10-13 06:04:49 | 7e0bf6cd |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7465 | 2026-10-13 06:04:49 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7466 | 2026-10-13 06:04:49 | 74b22dd1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-13T07"}} |
| 7467 | 2026-10-13 06:04:49 | 7e0bf6cd |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7468 | 2026-10-13 06:05:02 | a4edddc0 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7469 | 2026-10-13 06:05:02 | 9d43f9c9 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-13T07"}} |
| 7470 | 2026-10-13 06:05:27 | a4edddc0 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite |
| 7471 | 2026-10-13 06:13:59 | 1523484a | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 81s [done] report expect='FACTORY' cmd=False \| T3 FAIL 132s  |
| 7472 | 2026-10-13 06:13:59 | 1523484a | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 81s [done] report expect='FACTORY' cmd=False \| T3 FAIL 132s  |
| 7473 | 2026-10-13 06:13:59 | 1523484a | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7474 | 2026-10-13 06:13:59 | 8e562932 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "b9848c6f9e244793b86bd8b0a5d38f4c", "retry_of": "1523484ace664ad9877916ec7db671c |
| 7475 | 2026-10-13 06:13:59 | 1523484a | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7476 | 2026-10-13 06:14:01 | 59337fcb | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7477 | 2026-10-13 06:25:23 | 59337fcb | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 74s [done] report expect='FACTORY' cmd=False \| T3 FAIL 76s [ |
| 7478 | 2026-10-13 06:25:23 | 59337fcb | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 74s [done] report expect='FACTORY' cmd=False \| T3 FAIL 76s [ |
| 7479 | 2026-10-13 06:25:23 | 59337fcb | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7480 | 2026-10-13 06:25:23 | b2abcb78 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "retry_of": "59337fcb20624cedbbdedcd17459a8a |
| 7481 | 2026-10-13 06:25:23 | 59337fcb | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7482 | 2026-10-13 06:25:26 | 3015c529 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7483 | 2026-10-13 06:37:34 | 3015c529 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 77s [done] report expect='FACTORY' cmd=False \| T3 FAIL 134s  |
| 7484 | 2026-10-13 06:37:34 | 3015c529 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 77s [done] report expect='FACTORY' cmd=False \| T3 FAIL 134s  |
| 7485 | 2026-10-13 06:37:34 | 3015c529 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7486 | 2026-10-13 06:37:34 | 0f0e844c | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "43103e8f79ba46789af203ddbfb9e1ab", "retry_of": "3015c5292fcc4b4384a34ad5082d086 |
| 7487 | 2026-10-13 06:37:34 | 3015c529 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7488 | 2026-10-13 06:37:37 | 680335d1 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7489 | 2026-10-13 06:50:29 | 680335d1 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 132s [done] report expect='FACTORY' cmd=False \| T3 FAIL 76s  |
| 7490 | 2026-10-13 06:50:29 | 680335d1 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 132s [done] report expect='FACTORY' cmd=False \| T3 FAIL 76s  |
| 7491 | 2026-10-13 06:50:29 | 680335d1 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7492 | 2026-10-13 06:50:29 | 9a98e6f7 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "680335d162694e7b987487bb8c4cfd1 |
| 7493 | 2026-10-13 06:50:29 | 680335d1 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7494 | 2026-10-13 06:50:32 | 8e562932 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7495 | 2026-10-13 07:01:38 | 8e562932 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 75s [done] report expect='FACTORY' cmd=False \| T3 FAIL 77s [ |
| 7496 | 2026-10-13 07:01:38 | 8e562932 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 75s [done] report expect='FACTORY' cmd=False \| T3 FAIL 77s [ |
| 7497 | 2026-10-13 07:01:38 | 8e562932 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7498 | 2026-10-13 07:01:38 | f5cc5dd0 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "b9848c6f9e244793b86bd8b0a5d38f4c", "retry_of": "8e5629324bbf477eb54f2f7cb14deb4 |
| 7499 | 2026-10-13 07:01:38 | 8e562932 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7500 | 2026-10-13 07:01:39 | b2abcb78 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7501 | 2026-10-13 07:04:51 | 74b22dd1 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7502 | 2026-10-13 07:04:51 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7503 | 2026-10-13 07:04:52 | 09fc9827 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-13T08"}} |
| 7504 | 2026-10-13 07:04:52 | 74b22dd1 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7505 | 2026-10-13 07:05:06 | 9d43f9c9 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7506 | 2026-10-13 07:05:06 | b70aa8c0 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-13T08"}} |
| 7507 | 2026-10-13 07:05:33 | 9d43f9c9 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gem |
| 7508 | 2026-10-13 07:12:55 | b2abcb78 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 76s [done] report expect='FACTORY' cmd=False \| T3 FAIL 82s [ |
| 7509 | 2026-10-13 07:12:55 | b2abcb78 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 76s [done] report expect='FACTORY' cmd=False \| T3 FAIL 82s [ |
| 7510 | 2026-10-13 07:12:55 | b2abcb78 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7511 | 2026-10-13 07:12:55 | 9ca57765 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "retry_of": "b2abcb78ffda4ae7a557e6df2a347bc |
| 7512 | 2026-10-13 07:12:55 | b2abcb78 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7513 | 2026-10-13 07:12:57 | 0f0e844c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7514 | 2026-10-13 07:25:45 | 0f0e844c | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 74s [done] report expect='FACTORY' cmd=False \| T3 FAIL 81s [ |
| 7515 | 2026-10-13 07:25:45 | 0f0e844c | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 74s [done] report expect='FACTORY' cmd=False \| T3 FAIL 81s [ |
| 7516 | 2026-10-13 07:25:45 | 0f0e844c | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7517 | 2026-10-13 07:25:45 | e0056f0c | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "43103e8f79ba46789af203ddbfb9e1ab", "retry_of": "0f0e844c1b104632931c55360be6cdf |
| 7518 | 2026-10-13 07:25:45 | 0f0e844c | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7519 | 2026-10-13 07:25:48 | 9a98e6f7 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7520 | 2026-10-13 07:41:04 | 9a98e6f7 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 76s [done] report expect='FACTORY' cmd=False \| T3 FAIL 244s  |
| 7521 | 2026-10-13 07:41:04 | 9a98e6f7 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 76s [done] report expect='FACTORY' cmd=False \| T3 FAIL 244s  |
| 7522 | 2026-10-13 07:41:04 | 9a98e6f7 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7523 | 2026-10-13 07:41:04 | cdc189c9 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "9a98e6f71ad9433d93c8aac8a8b16cb |
| 7524 | 2026-10-13 07:41:04 | 9a98e6f7 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7525 | 2026-10-13 07:41:04 | f5cc5dd0 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7526 | 2026-10-13 07:55:31 | f5cc5dd0 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 76s [done] report expect='FACTORY' cmd=False \| T3 FAIL 166s  |
| 7527 | 2026-10-13 07:55:31 | f5cc5dd0 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 76s [done] report expect='FACTORY' cmd=False \| T3 FAIL 166s  |
| 7528 | 2026-10-13 07:55:31 | f5cc5dd0 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7529 | 2026-10-13 07:55:31 | 6cc17c4a | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "b9848c6f9e244793b86bd8b0a5d38f4c", "retry_of": "f5cc5dd0b38d481eb7841a7f83aa145 |
| 7530 | 2026-10-13 07:55:31 | f5cc5dd0 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7531 | 2026-10-13 07:55:34 | 9ca57765 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7532 | 2026-10-13 08:04:55 | 09fc9827 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7533 | 2026-10-13 08:04:55 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7534 | 2026-10-13 08:04:55 | 98037d6a |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-13T09"}} |
| 7535 | 2026-10-13 08:04:55 | 09fc9827 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7536 | 2026-10-13 08:05:08 | b70aa8c0 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7537 | 2026-10-13 08:05:08 | adcba1c4 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-13T09"}} |
| 7538 | 2026-10-13 08:07:32 | b70aa8c0 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen2 |
| 7539 | 2026-10-13 08:08:10 | 9ca57765 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 44s [done] report expect='FACTORY' cmd=False \| T3 FAIL 109s  |
| 7540 | 2026-10-13 08:08:10 | 9ca57765 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 44s [done] report expect='FACTORY' cmd=False \| T3 FAIL 109s  |
| 7541 | 2026-10-13 08:08:10 | 9ca57765 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7542 | 2026-10-13 08:08:10 | 19c838c2 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "retry_of": "9ca57765545144e7990b81b16d71762 |
| 7543 | 2026-10-13 08:08:10 | 9ca57765 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7544 | 2026-10-13 08:08:13 | e0056f0c | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7545 | 2026-10-13 08:23:24 | e0056f0c | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 166s [done] report expect='FACTORY' cmd=False \| T3 FAIL 164s |
| 7546 | 2026-10-13 08:23:24 | e0056f0c | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 166s [done] report expect='FACTORY' cmd=False \| T3 FAIL 164s |
| 7547 | 2026-10-13 08:23:24 | e0056f0c | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7548 | 2026-10-13 08:23:24 | aa35caa3 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "43103e8f79ba46789af203ddbfb9e1ab", "retry_of": "e0056f0ca82a45b89e9bba0e7f44f33 |
| 7549 | 2026-10-13 08:23:24 | e0056f0c | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7550 | 2026-10-13 08:23:26 | cdc189c9 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7551 | 2026-10-13 08:37:41 | cdc189c9 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 76s [done] report expect='FACTORY' cmd=False \| T3 FAIL 130s  |
| 7552 | 2026-10-13 08:37:41 | cdc189c9 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 76s [done] report expect='FACTORY' cmd=False \| T3 FAIL 130s  |
| 7553 | 2026-10-13 08:37:41 | cdc189c9 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7554 | 2026-10-13 08:37:41 | b7f8bfef | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "cdc189c9b54e4e8a808cd5ed42764d4 |
| 7555 | 2026-10-13 08:37:41 | cdc189c9 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7556 | 2026-10-13 08:37:42 | 6cc17c4a | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7557 | 2026-10-13 14:35:17 | 6cc17c4a |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 7558 | 2026-10-13 14:35:18 | 98037d6a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7559 | 2026-10-13 14:35:22 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7560 | 2026-10-13 14:35:30 | d894a64c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-13T15"}} |
| 7561 | 2026-10-13 14:35:30 | 98037d6a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7562 | 2026-10-13 14:35:32 | adcba1c4 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7563 | 2026-10-13 14:35:32 | 9f2509a2 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-13T15"}} |
| 7564 | 2026-10-13 14:35:34 | adcba1c4 |  | probe.network_down | fast-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 7565 | 2026-10-13 14:35:34 | 0b5cb79d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-13T09-retry", "retry_of": "adcba1c438f4473983c3e42be24d9523"}} |
| 7566 | 2026-10-13 14:35:35 | adcba1c4 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7567 | 2026-10-13 14:35:54 | 6cc17c4a |  | job.readopted | svc-LAPTOP-LRE6PSA8 | {} |
| 7568 | 2026-10-13 14:45:31 | 6cc17c4a | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7569 | 2026-10-13 14:45:36 | 0b5cb79d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7570 | 2026-10-13 14:45:36 | 9f2509a2 |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 7571 | 2026-10-13 14:45:36 | 19c838c2 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7572 | 2026-10-13 14:47:25 | 0b5cb79d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", "local4b"], "change |
| 7573 | 2026-10-13 15:07:44 | 19c838c2 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7574 | 2026-10-13 15:07:47 | 6cc17c4a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 7575 | 2026-10-13 15:29:55 | 6cc17c4a | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7576 | 2026-10-13 15:29:55 | 19c838c2 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 7577 | 2026-10-13 15:35:32 | d894a64c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7578 | 2026-10-13 15:35:32 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7579 | 2026-10-13 15:35:33 | 9d8bd63f |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-13T16"}} |
| 7580 | 2026-10-13 15:35:33 | d894a64c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7581 | 2026-10-13 15:35:38 | 9f2509a2 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7582 | 2026-10-13 15:35:38 | ce3c1fa8 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-13T16"}} |
| 7583 | 2026-10-13 15:37:23 | 9f2509a2 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "TimeoutError"} |
| 7584 | 2026-10-13 15:37:23 | 9f2509a2 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\":  |
| 7585 | 2026-10-13 15:37:23 | 9f2509a2 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash38", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\ |
| 7586 | 2026-10-13 15:37:23 | 8a38358b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-13", "trigger": "blocked:gemini-flash,gemini-flash-latest,gemini-flash3 |
| 7587 | 2026-10-13 15:37:23 | e3e7478f |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-13", "trigger": "blocked:gemini-flash,gemini-flash-latest,gemini-flas |
| 7588 | 2026-10-13 15:37:23 | a8775d77 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-13", "trigger": "blocked:gemini-flash,gemini-flash-latest,gemini- |
| 7589 | 2026-10-13 15:37:23 | f17649df |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-13", "trigger": "blocked:gemini-flash,gemini-flash-latest,gemini-fl |
| 7590 | 2026-10-13 15:37:23 | 77dbdc5d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-13", "trigger": "blocked:gemini-flash,gemini-flash-latest,gemini-flas |
| 7591 | 2026-10-13 15:37:23 | 7a51debf |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-13", "trigger": "blocked:gemini-flash,gemini-flash-latest,gemini-fla |
| 7592 | 2026-10-13 15:37:23 | 9f2509a2 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemma26b", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", "local4b"], "changed": [["gemini |
| 7593 | 2026-10-13 15:37:29 | 8a38358b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7594 | 2026-10-13 15:37:30 | 8a38358b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7595 | 2026-10-13 15:37:36 | e3e7478f |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7596 | 2026-10-13 15:37:38 | e3e7478f |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7597 | 2026-10-13 15:37:47 | a8775d77 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7598 | 2026-10-13 15:37:50 | a8775d77 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7599 | 2026-10-13 15:37:56 | f17649df |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7600 | 2026-10-13 15:37:56 | f17649df |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7601 | 2026-10-13 15:38:03 | 77dbdc5d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7602 | 2026-10-13 15:38:03 | 77dbdc5d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7603 | 2026-10-13 15:38:08 | 7a51debf |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7604 | 2026-10-13 15:38:08 | 7a51debf |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7605 | 2026-10-13 15:48:24 | 19c838c2 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 46s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 156s [done] report expect='FACTORY' cmd=False \| T3 FAIL 100s |
| 7606 | 2026-10-13 15:48:24 | 19c838c2 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 46s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 156s [done] report expect='FACTORY' cmd=False \| T3 FAIL 100s |
| 7607 | 2026-10-13 15:48:24 | 19c838c2 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7608 | 2026-10-13 15:48:24 | 5a603559 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "retry_of": "19c838c2aa394a6e8bff9febb32b7ca |
| 7609 | 2026-10-13 15:48:24 | 19c838c2 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 2, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7610 | 2026-10-13 15:48:29 | 6cc17c4a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 7611 | 2026-10-13 16:10:38 | 6cc17c4a | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "failed", "attempt": 3, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7612 | 2026-10-13 16:10:42 | aa35caa3 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7613 | 2026-10-13 16:28:42 | aa35caa3 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 47s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 93s [done] report expect='FACTORY' cmd=False \| T3 FAIL 248s  |
| 7614 | 2026-10-13 16:28:42 | aa35caa3 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 47s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 93s [done] report expect='FACTORY' cmd=False \| T3 FAIL 248s  |
| 7615 | 2026-10-13 16:28:42 | aa35caa3 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7616 | 2026-10-13 16:28:42 | 8abcd887 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "43103e8f79ba46789af203ddbfb9e1ab", "retry_of": "aa35caa31b754207914b505aeadb4a5 |
| 7617 | 2026-10-13 16:28:42 | aa35caa3 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 2, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7618 | 2026-10-13 16:28:45 | b7f8bfef | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7619 | 2026-10-13 16:35:37 | 9d8bd63f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7620 | 2026-10-13 16:35:37 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7621 | 2026-10-13 16:35:38 | 72c80422 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-13T17"}} |
| 7622 | 2026-10-13 16:35:38 | 9d8bd63f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7623 | 2026-10-13 16:35:42 | ce3c1fa8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7624 | 2026-10-13 16:35:42 | c031edb4 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-13T17"}} |
| 7625 | 2026-10-13 16:37:02 | ce3c1fa8 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-gemini-flash-lite-latest", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "TimeoutError"} |
| 7626 | 2026-10-13 16:37:02 | 5006ba9b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-13", "trigger": "blocked:gemini-gemini-flash-lite-latest"}} |
| 7627 | 2026-10-13 16:37:02 | 274f4799 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-13", "trigger": "blocked:gemini-gemini-flash-lite-latest"}} |
| 7628 | 2026-10-13 16:37:02 | 49619093 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-13", "trigger": "blocked:gemini-gemini-flash-lite-latest"}} |
| 7629 | 2026-10-13 16:37:02 | 9586ae60 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-13", "trigger": "blocked:gemini-gemini-flash-lite-latest"}} |
| 7630 | 2026-10-13 16:37:02 | 5dab72ed |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-13", "trigger": "blocked:gemini-gemini-flash-lite-latest"}} |
| 7631 | 2026-10-13 16:37:02 | b8e6a152 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-13", "trigger": "blocked:gemini-gemini-flash-lite-latest"}} |
| 7632 | 2026-10-13 16:37:02 | 10206006 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": ["031"], "day": "2026-10-13", "canary_for": ["gemini-gemini-flash-lite-latest"]}} |
| 7633 | 2026-10-13 16:37:02 | ce3c1fa8 |  | monitor.canary | svc-LAPTOP-LRE6PSA8 | {"lanes": ["gemini-gemini-flash-lite-latest"], "bots": ["031"]} |
| 7634 | 2026-10-13 16:37:02 | ce3c1fa8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", "local4b"], "ch |
| 7635 | 2026-10-13 16:37:08 | 5006ba9b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7636 | 2026-10-13 16:37:09 | 5006ba9b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7637 | 2026-10-13 16:37:18 | 274f4799 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7638 | 2026-10-13 16:37:18 | 274f4799 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7639 | 2026-10-13 16:37:24 | 49619093 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7640 | 2026-10-13 16:37:24 | 49619093 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7641 | 2026-10-13 16:37:31 | 9586ae60 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7642 | 2026-10-13 16:37:31 | 9586ae60 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7643 | 2026-10-13 16:37:36 | 5dab72ed |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7644 | 2026-10-13 16:37:36 | 5dab72ed |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7645 | 2026-10-13 16:37:41 | b8e6a152 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7646 | 2026-10-13 16:37:41 | b8e6a152 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7647 | 2026-10-13 16:37:47 | 10206006 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7648 | 2026-10-13 16:37:47 | 77c04c86 | 031 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "031", "monitor_of": "10206006ad0f4d95bfaf0875ad326c16", "day": "2026-10-13"}} |
| 7649 | 2026-10-13 16:37:47 | 10206006 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["031"], "jobs": ["77c04c86"]} |
| 7650 | 2026-10-13 16:37:47 | 10206006 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7651 | 2026-10-13 16:37:51 | 77c04c86 | 031 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7652 | 2026-10-13 16:41:55 | 77c04c86 | 031 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 62s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\031.json' \| T2 PASS 47s [done] expect='3' la |
| 7653 | 2026-10-13 16:41:55 | 77c04c86 | 031 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 62s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\031.json' \| T2 PASS 47s [done] expect='3' la |
| 7654 | 2026-10-13 16:41:55 | 142dd6d7 | 031 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "031", "retest_of": "77c04c86b66e451886358ec35ff7d8d3", "after_quota": "77c04c86b66e451886358ec35ff7d |
| 7655 | 2026-10-13 16:41:55 | 77c04c86 | 031 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "031", "status": "active", "verified": "VERIFIED"}} |
| 7656 | 2026-10-13 16:45:10 | b7f8bfef | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 45s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 56s [done] report expect='FACTORY' cmd=False \| T3 FAIL 174s  |
| 7657 | 2026-10-13 16:45:10 | b7f8bfef | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 45s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 56s [done] report expect='FACTORY' cmd=False \| T3 FAIL 174s  |
| 7658 | 2026-10-13 16:45:10 | b7f8bfef | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7659 | 2026-10-13 16:45:10 | 1b2d61cb | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "b7f8bfef2015466cb380d5aebe83eee |
| 7660 | 2026-10-13 16:45:10 | b7f8bfef | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 2, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7661 | 2026-10-13 16:45:15 | 5a603559 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7662 | 2026-10-13 17:04:12 | 5a603559 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 47s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 93s [done] report expect='FACTORY' cmd=False \| T3 FAIL 252s  |
| 7663 | 2026-10-13 17:04:12 | 5a603559 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 47s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 93s [done] report expect='FACTORY' cmd=False \| T3 FAIL 252s  |
| 7664 | 2026-10-13 17:04:12 | 5a603559 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7665 | 2026-10-13 17:04:12 | 9c35778b | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "retry_of": "5a603559a1e148919ba305433535fec |
| 7666 | 2026-10-13 17:04:12 | 5a603559 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 2, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7667 | 2026-10-13 17:04:17 | 8abcd887 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7668 | 2026-10-13 17:25:10 | 8abcd887 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 47s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 95s [done] report expect='FACTORY' cmd=False \| T3 FAIL 247s  |
| 7669 | 2026-10-13 17:25:10 | 8abcd887 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 47s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 95s [done] report expect='FACTORY' cmd=False \| T3 FAIL 247s  |
| 7670 | 2026-10-13 17:25:10 | 8abcd887 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7671 | 2026-10-13 17:25:10 | 1c048b97 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "43103e8f79ba46789af203ddbfb9e1ab", "retry_of": "8abcd887576e41a08e5d5c04c99cc4d |
| 7672 | 2026-10-13 17:25:10 | 8abcd887 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 3, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7673 | 2026-10-13 17:25:14 | 1b2d61cb | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7674 | 2026-10-13 17:35:41 | 72c80422 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7675 | 2026-10-13 17:35:41 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7676 | 2026-10-13 17:35:42 | ce49c72e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-13T18"}} |
| 7677 | 2026-10-13 17:35:42 | 72c80422 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7678 | 2026-10-13 17:35:46 | c031edb4 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7679 | 2026-10-13 17:35:46 | 86bed3db |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-13T18"}} |
| 7680 | 2026-10-13 17:37:30 | c031edb4 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-gemini-flash-lite-latest", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 7681 | 2026-10-13 17:37:30 | c031edb4 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-lite", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\n   |
| 7682 | 2026-10-13 17:37:30 | 9d2bb420 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-13", "trigger": "blocked:gemini-lite"}} |
| 7683 | 2026-10-13 17:37:30 | 270c471a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-13", "trigger": "blocked:gemini-lite"}} |
| 7684 | 2026-10-13 17:37:30 | f5d56718 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-13", "trigger": "blocked:gemini-lite"}} |
| 7685 | 2026-10-13 17:37:30 | 0954e62b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-13", "trigger": "blocked:gemini-lite"}} |
| 7686 | 2026-10-13 17:37:30 | f3f6b49b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-13", "trigger": "blocked:gemini-lite"}} |
| 7687 | 2026-10-13 17:37:30 | a01d44d1 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-13", "trigger": "blocked:gemini-lite"}} |
| 7688 | 2026-10-13 17:37:30 | c031edb4 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", "local4b"], "cha |
| 7689 | 2026-10-13 17:37:35 | 9d2bb420 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7690 | 2026-10-13 17:37:36 | 9d2bb420 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
