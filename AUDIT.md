# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
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
| 7691 | 2026-10-13 17:37:41 | 270c471a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7692 | 2026-10-13 17:37:41 | 270c471a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7693 | 2026-10-13 17:37:45 | f5d56718 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7694 | 2026-10-13 17:37:45 | f5d56718 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7695 | 2026-10-13 17:37:49 | 0954e62b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7696 | 2026-10-13 17:37:49 | 0954e62b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7697 | 2026-10-13 17:37:53 | f3f6b49b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7698 | 2026-10-13 17:37:53 | f3f6b49b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7699 | 2026-10-13 17:37:58 | a01d44d1 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7700 | 2026-10-13 17:37:58 | a01d44d1 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7701 | 2026-10-14 02:24:50 | ce49c72e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7702 | 2026-10-14 02:24:52 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7703 | 2026-10-14 02:25:00 | 0c4d053e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T03"}} |
| 7704 | 2026-10-14 02:25:00 | ce49c72e |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7705 | 2026-10-14 02:25:06 | 86bed3db |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7706 | 2026-10-14 02:25:06 | 4f12ad4a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T03"}} |
| 7707 | 2026-10-14 02:25:20 | 1b2d61cb | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 7708 | 2026-10-14 02:25:24 | 9c35778b | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7709 | 2026-10-14 02:26:21 | 86bed3db |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 7710 | 2026-10-14 02:26:21 | 86bed3db |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "or-apodex-11-mini", "outcome": "gone", "before": "VERIFIED", "after": "BLOCKED", "detail": "{\"error\":{\"message\":\"no endpoint |
| 7711 | 2026-10-14 02:26:21 | 86bed3db |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "or-lfm-25-26b", "outcome": "ok", "before": "INFERRED", "after": "VERIFIED", "detail": null} |
| 7712 | 2026-10-14 02:26:21 | 86bed3db |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "or-nemotron-3-ultra-550b-a55b", "outcome": "ok", "before": "INFERRED", "after": "VERIFIED", "detail": null} |
| 7713 | 2026-10-14 02:26:21 | b1717ca4 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-14", "trigger": "blocked:or-apodex-11-mini"}} |
| 7714 | 2026-10-14 02:26:21 | 6c0395cb |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-14", "trigger": "blocked:or-apodex-11-mini"}} |
| 7715 | 2026-10-14 02:26:21 | fc776a5c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-14", "trigger": "blocked:or-apodex-11-mini"}} |
| 7716 | 2026-10-14 02:26:21 | 7ad6e347 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-14", "trigger": "blocked:or-apodex-11-mini"}} |
| 7717 | 2026-10-14 02:26:21 | 2cbbae4c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-14", "trigger": "blocked:or-apodex-11-mini"}} |
| 7718 | 2026-10-14 02:26:21 | 3d744ddf |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-14", "trigger": "blocked:or-apodex-11-mini"}} |
| 7719 | 2026-10-14 02:26:21 | 86bed3db |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", |
| 7720 | 2026-10-14 02:26:26 | b1717ca4 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7721 | 2026-10-14 02:26:27 | b1717ca4 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7722 | 2026-10-14 02:26:31 | 6c0395cb |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7723 | 2026-10-14 02:26:32 | 6c0395cb |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7724 | 2026-10-14 02:26:37 | fc776a5c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7725 | 2026-10-14 02:26:39 | fc776a5c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7726 | 2026-10-14 02:26:44 | 7ad6e347 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7727 | 2026-10-14 02:26:44 | 7ad6e347 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7728 | 2026-10-14 02:26:48 | 2cbbae4c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7729 | 2026-10-14 02:26:48 | 2cbbae4c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7730 | 2026-10-14 02:26:53 | 3d744ddf |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7731 | 2026-10-14 02:26:53 | 3d744ddf |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7732 | 2026-10-14 02:26:57 | 142dd6d7 | 031 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7733 | 2026-10-14 02:30:56 | 142dd6d7 | 031 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 48s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\031.json' \| T2 FAIL 92s [done] expect='3' la |
| 7734 | 2026-10-14 02:30:56 | 142dd6d7 | 031 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 48s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\031.json' \| T2 FAIL 92s [done] expect='3' la |
| 7735 | 2026-10-14 02:30:56 | 142dd6d7 | 031 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7736 | 2026-10-14 02:30:56 | 14978851 | 031 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "031", "max_rounds": 2}} |
| 7737 | 2026-10-14 02:30:56 | 142dd6d7 | 031 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "031", "status": "testing", "verified": "UNVERIFIED"}} |
| 7738 | 2026-10-14 02:31:03 | 14978851 | 031 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7739 | 2026-10-14 03:33:44 |  |  | factory.outage | fast-LAPTOP-LRE6PSA8 | {"gap_min": 62, "silent_since": "2026-10-14T02:31:03", "last_event": "job.claimed", "cause": "power loss / battery flat (kernel-power 41)",  |
| 7740 | 2026-10-14 03:33:44 |  |  | factory.outage | svc-LAPTOP-LRE6PSA8 | {"gap_min": 62, "silent_since": "2026-10-14T02:31:03", "last_event": "job.claimed", "cause": "power loss / battery flat (kernel-power 41)",  |
| 7741 | 2026-10-14 03:33:44 | 9c35778b |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 7742 | 2026-10-14 03:33:44 | 14978851 |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 7743 | 2026-10-14 03:33:44 | 0c4d053e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7744 | 2026-10-14 03:33:45 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7745 | 2026-10-14 03:33:45 | 4f12ad4a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7746 | 2026-10-14 03:33:45 | 0842ece4 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T04"}} |
| 7747 | 2026-10-14 03:33:45 | f691e0dc |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T04"}} |
| 7748 | 2026-10-14 03:33:45 | 0c4d053e |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7749 | 2026-10-14 03:33:52 | 1b2d61cb | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 7750 | 2026-10-14 03:34:33 | 4f12ad4a |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 7751 | 2026-10-14 03:34:33 | 4f12ad4a |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash38", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 7752 | 2026-10-14 03:34:33 | 4f12ad4a |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-lite", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 7753 | 2026-10-14 03:34:33 | 4f12ad4a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash-latest", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemi |
| 7754 | 2026-10-14 03:34:38 | 55933f61 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7755 | 2026-10-14 03:34:38 | 55933f61 |  | audit.verified | fast-LAPTOP-LRE6PSA8 | {"rows": 7753, "hashed": 7001, "first_bad": null} |
| 7756 | 2026-10-14 03:34:39 | 825829e8 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-10-15"}} |
| 7757 | 2026-10-14 03:34:39 | 1a261d95 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-10-14"}} |
| 7758 | 2026-10-14 03:34:39 | ba4e59ac |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-10-14"}} |
| 7759 | 2026-10-14 03:34:39 | abdd8333 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-10-14"}} |
| 7760 | 2026-10-14 03:34:39 | 55933f61 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7761 | 2026-10-14 03:39:00 | 1b2d61cb | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 37s [done] report expect='FACTORY' cmd=True \| T3 PASS 88s [d |
| 7762 | 2026-10-14 03:39:00 | 1b2d61cb | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 37s [done] report expect='FACTORY' cmd=True \| T3 PASS 88s [d |
| 7763 | 2026-10-14 03:39:00 | 1b2d61cb | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7764 | 2026-10-14 03:39:00 | bb3c72b9 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "1b2d61cb68e94cd6b45ef925e051a48 |
| 7765 | 2026-10-14 03:39:00 | 1b2d61cb | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7766 | 2026-10-14 03:39:02 | 9c35778b | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 7767 | 2026-10-14 03:39:04 | 14978851 | 031 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 7768 | 2026-10-14 03:41:17 | 14978851 | 031 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-120b", "sandbox": null, "rejected": ["fallback 'or-l |
| 7769 | 2026-10-14 03:41:17 | 14978851 | 031 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 2, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 7770 | 2026-10-14 03:41:21 | abdd8333 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7771 | 2026-10-14 03:41:21 | e2869fda | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "abdd8333716b46e4b457f3e3406bd86a", "day": "2026-10-14"}} |
| 7772 | 2026-10-14 03:41:21 | abdd8333 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001"], "jobs": ["e2869fda"]} |
| 7773 | 2026-10-14 03:41:21 | abdd8333 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7774 | 2026-10-14 03:41:24 | 1a261d95 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7775 | 2026-10-14 03:41:24 | 1a261d95 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": []}} |
| 7776 | 2026-10-14 03:41:27 | ba4e59ac |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7777 | 2026-10-14 03:41:47 | ba4e59ac |  | factory.canary | svc-LAPTOP-LRE6PSA8 | {"verdict": "FAIL", "lane": "groq:openai/gpt-oss-20b", "chain": ["groq-gptoss20b", "gemini-gemma26b", "local3b"], "result": "T1 FAIL 2s [don |
| 7778 | 2026-10-14 03:41:47 | ba4e59ac |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"pass": 1, "total": 2}} |
| 7779 | 2026-10-14 03:50:42 | 9c35778b | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 22s [done] report expect='FACTORY' cmd=True \| T3 PASS 35s [d |
| 7780 | 2026-10-14 03:50:42 | 9c35778b | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 22s [done] report expect='FACTORY' cmd=True \| T3 PASS 35s [d |
| 7781 | 2026-10-14 03:50:42 | 9c35778b | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7782 | 2026-10-14 03:50:42 | 4940d9aa | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "retry_of": "9c35778ba7724858a9afc3719e7f1bb |
| 7783 | 2026-10-14 03:50:42 | 9c35778b | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7784 | 2026-10-14 03:50:46 | 1c048b97 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7785 | 2026-10-14 04:05:34 | 1c048b97 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 166s [ |
| 7786 | 2026-10-14 04:05:34 | 1c048b97 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 166s [ |
| 7787 | 2026-10-14 04:05:34 | fc146198 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "1c048b97a00941b4a0a2a31b29aec1c6", "after_quota": "1c048b97a00941b4a0a2a31b29aec |
| 7788 | 2026-10-14 04:05:34 | 1c048b97 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7789 | 2026-10-14 04:05:38 | 888a5269 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7790 | 2026-10-14 04:22:31 | 888a5269 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 7791 | 2026-10-14 04:22:31 | 888a5269 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 7792 | 2026-10-14 04:22:31 | 888a5269 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7793 | 2026-10-14 04:22:31 | 30e36894 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "496e3afd58764673a6b80d4e1d7f4792", "retry_of": "888a5269107a401f8fac81ca1a66fc2 |
| 7794 | 2026-10-14 04:22:31 | 888a5269 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7795 | 2026-10-14 04:22:34 | bb3c72b9 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7796 | 2026-10-14 04:33:46 | 0842ece4 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7797 | 2026-10-14 04:33:46 | 74e50336 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T05"}} |
| 7798 | 2026-10-14 04:34:07 | 0842ece4 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "groq-gptoss120b", "groq-gptoss20b", "groq-qwe |
| 7799 | 2026-10-14 04:34:11 | f691e0dc |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7800 | 2026-10-14 04:34:12 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7801 | 2026-10-14 04:34:12 | 7d2fff1e |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T05"}} |
| 7802 | 2026-10-14 04:34:12 | f691e0dc |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7803 | 2026-10-14 04:35:43 | bb3c72b9 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 106s [ |
| 7804 | 2026-10-14 04:35:43 | bb3c72b9 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 106s [ |
| 7805 | 2026-10-14 04:35:43 | bb3c72b9 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 7806 | 2026-10-14 04:35:43 | 5efdb56b | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "bb3c72b9a2f343d79a4dff412973c74 |
| 7807 | 2026-10-14 04:35:43 | bb3c72b9 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7808 | 2026-10-14 04:35:46 | 4940d9aa | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7809 | 2026-10-14 04:49:39 | 4940d9aa | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 73s [d |
| 7810 | 2026-10-14 04:49:39 | 4940d9aa | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 73s [d |
| 7811 | 2026-10-14 04:49:39 | ceb330c7 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "4940d9aa166d426aadfe8f833d27143c", "after_quota": "4940d9aa166d426aadfe8f833d271 |
| 7812 | 2026-10-14 04:49:39 | 4940d9aa | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7813 | 2026-10-14 04:49:43 | b8338b41 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7814 | 2026-10-14 05:08:35 | b8338b41 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 42s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 192s [done] report expect='FACTORY' cmd=True \| T3 FAIL 254s  |
| 7815 | 2026-10-14 05:08:35 | b8338b41 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 42s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 192s [done] report expect='FACTORY' cmd=True \| T3 FAIL 254s  |
| 7816 | 2026-10-14 05:08:35 | 529d6be2 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fe371a05201e499c9cc16d620128e678", "after_quota": "b8338b416ed342d38d69e8de9299b |
| 7817 | 2026-10-14 05:08:35 | b8338b41 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7818 | 2026-10-14 05:08:39 | 30e36894 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7819 | 2026-10-14 05:23:14 | 30e36894 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 43s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 92s [d |
| 7820 | 2026-10-14 05:23:14 | 30e36894 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 43s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 92s [d |
| 7821 | 2026-10-14 05:23:14 | a8403e44 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "30e368943ffb4b7a92841d88069a53ca", "after_quota": "30e368943ffb4b7a92841d88069a5 |
| 7822 | 2026-10-14 05:23:14 | 30e36894 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 7823 | 2026-10-14 05:23:16 | 5efdb56b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7824 | 2026-10-14 05:33:49 | 74e50336 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7825 | 2026-10-14 05:33:49 | 51e35987 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T06"}} |
| 7826 | 2026-10-14 05:34:12 | 74e50336 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\n  |
| 7827 | 2026-10-14 05:34:12 | d137fed9 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-14", "trigger": "blocked:gemini-flash"}} |
| 7828 | 2026-10-14 05:34:12 | f89523e1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-14", "trigger": "blocked:gemini-flash"}} |
| 7829 | 2026-10-14 05:34:12 | 297ff9e5 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-14", "trigger": "blocked:gemini-flash"}} |
| 7830 | 2026-10-14 05:34:12 | 121a8faf |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-14", "trigger": "blocked:gemini-flash"}} |
| 7831 | 2026-10-14 05:34:12 | e9160798 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-14", "trigger": "blocked:gemini-flash"}} |
| 7832 | 2026-10-14 05:34:12 | b9d990b5 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-14", "trigger": "blocked:gemini-flash"}} |
| 7833 | 2026-10-14 05:34:12 | 74e50336 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-lite", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", " |
| 7834 | 2026-10-14 05:34:16 | 7d2fff1e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7835 | 2026-10-14 05:34:16 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 7836 | 2026-10-14 05:34:17 | 9b9bd998 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-14T06"}} |
| 7837 | 2026-10-14 05:34:17 | 7d2fff1e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 7838 | 2026-10-14 05:34:25 | d137fed9 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7839 | 2026-10-14 05:34:26 | d137fed9 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 7840 | 2026-10-14 05:34:29 | f89523e1 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7841 | 2026-10-14 05:34:29 | f89523e1 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 7842 | 2026-10-14 05:34:33 | 297ff9e5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 7843 | 2026-10-14 05:34:33 | 297ff9e5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
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
