# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 1436 | 2026-09-25 00:20:58 | 86969460 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": ["mcp:crawlio-browser"]}} |
| 1437 | 2026-09-25 00:28:03 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1438 | 2026-09-25 00:28:05 | 4901b2db |  | job.enqueued | owner | {"kind": "tooldisc", "payload": {"need": "playwright browser", "max": 1, "day": "2026-09-25"}} |
| 1439 | 2026-09-25 00:28:26 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["112 passed in 17.90s"]} |
| 1440 | 2026-09-25 00:28:26 | 4901b2db |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1441 | 2026-09-25 00:28:26 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["112 passed in 17.71s"]} |
| 1442 | 2026-09-25 00:29:16 | 50cb8d24 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1443 | 2026-09-25 00:29:16 | e7744308 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T01"}} |
| 1444 | 2026-09-25 00:29:51 | 50cb8d24 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-l |
| 1445 | 2026-09-25 00:29:56 | 14d4a04c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1446 | 2026-09-25 00:29:56 | 190e3258 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T01"}} |
| 1447 | 2026-09-25 00:29:56 | 14d4a04c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1448 | 2026-09-25 00:31:25 | 4901b2db |  | tool.rejected | svc-LAPTOP-LRE6PSA8 | {"tool": "com.pulsemcp/playwright-stealth", "reason": "policy: anti-detection / bypass tooling (contract: never evade ToS, rate limits or id |
| 1449 | 2026-09-25 00:31:25 | 4901b2db |  | tool.discovered | svc-LAPTOP-LRE6PSA8 | {"tool": "io.github.feder-cr/invisible-playwright-mcp", "reason": "probation; tools=16 144s", "need": "playwright browser"} |
| 1450 | 2026-09-25 00:31:25 | 4901b2db |  | owner.needed | svc-LAPTOP-LRE6PSA8 | {"provider": "tools", "reason": "MCP tools on probation for need 'playwright browser': ['mcp:invisible-playwright-mcp'] \u2014 approve to wi |
| 1451 | 2026-09-25 00:31:25 | 4901b2db |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": ["mcp:invisible-playwright-mcp"]}} |
| 1452 | 2026-09-25 00:38:29 |  |  | tool.revoked | owner | {"tool": "mcp:invisible-playwright-mcp", "detail": "{\"ok\": true, \"tool\": \"mcp:invisible-playwright-mcp\", \"ledger\": \"io.github.feder |
| 1453 | 2026-09-25 00:38:30 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1454 | 2026-09-25 00:38:30 | 6e4d634b |  | job.enqueued | owner | {"kind": "tooldisc", "payload": {"need": "playwright browser", "max": 1, "day": "2026-09-25"}} |
| 1455 | 2026-09-25 00:38:31 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1456 | 2026-09-25 00:38:53 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["113 passed in 19.94s"]} |
| 1457 | 2026-09-25 00:38:53 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["113 passed in 18.57s"]} |
| 1458 | 2026-09-25 00:38:53 | 6e4d634b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1459 | 2026-09-25 00:39:46 | 6e4d634b |  | tool.discovered | fast-LAPTOP-LRE6PSA8 | {"tool": "io.github.vola-trebla/playwright-network-chaos-mcp", "reason": "probation; tools=8 25s", "need": "playwright browser"} |
| 1460 | 2026-09-25 00:39:46 | 6e4d634b |  | tool.rejected | fast-LAPTOP-LRE6PSA8 | {"tool": "io.github.Agent360dk/browser-mcp", "reason": "policy: anti-detection / bypass tooling (contract: never evade ToS, rate limits or i |
| 1461 | 2026-09-25 00:39:46 | 6e4d634b |  | owner.needed | fast-LAPTOP-LRE6PSA8 | {"provider": "tools", "reason": "MCP tools on probation for need 'playwright browser': ['mcp:playwright-network-chaos-mcp'] \u2014 approve t |
| 1462 | 2026-09-25 00:39:46 | 6e4d634b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": ["mcp:playwright-network-chaos-mcp"]}} |
| 1463 | 2026-09-25 00:46:50 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1464 | 2026-09-25 00:46:51 |  |  | tool.revoked | owner | {"tool": "mcp:playwright-network-chaos-mcp", "detail": "{\"ok\": true, \"tool\": \"mcp:playwright-network-chaos-mcp\", \"ledger\": \"io.gith |
| 1465 | 2026-09-25 00:46:52 | d6be18bd |  | job.enqueued | owner | {"kind": "tooldisc", "payload": {"need": "playwright browser", "max": 1, "day": "2026-09-25"}} |
| 1466 | 2026-09-25 00:46:53 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1467 | 2026-09-25 00:46:55 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": false, "tail": ["........................"]} |
| 1468 | 2026-09-25 00:46:55 |  |  | worker.blocked_by_tests | fast-LAPTOP-LRE6PSA8 | {"reason": "core/tests red on current code; refusing to process jobs until code changes"} |
| 1469 | 2026-09-25 00:46:57 |  |  | worker.blocked_by_tests | svc-LAPTOP-LRE6PSA8 | {"reason": "core/tests red on current code; refusing to process jobs until code changes"} |
| 1470 | 2026-09-25 01:01:19 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["114 passed in 16.94s"]} |
| 1471 | 2026-09-25 01:01:19 | d6be18bd |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1472 | 2026-09-25 01:01:19 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["114 passed in 16.70s"]} |
| 1473 | 2026-09-25 01:06:21 | d6be18bd |  | tool.discovered | svc-LAPTOP-LRE6PSA8 | {"tool": "io.github.aethynio/aethyn-browser-mcp", "reason": "probation; tools=10 260s", "need": "playwright browser"} |
| 1474 | 2026-09-25 01:06:21 | d6be18bd |  | owner.needed | svc-LAPTOP-LRE6PSA8 | {"provider": "tools", "reason": "MCP tools on probation for need 'playwright browser': ['mcp:aethyn-browser-mcp'] \u2014 approve to wire int |
| 1475 | 2026-09-25 01:06:21 | d6be18bd |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": ["mcp:aethyn-browser-mcp"]}} |
| 1476 | 2026-09-25 01:11:13 |  |  | tool.revoked | owner | {"tool": "mcp:aethyn-browser-mcp", "detail": "{\"ok\": true, \"tool\": \"mcp:aethyn-browser-mcp\", \"ledger\": \"io.github.aethynio/aethyn-b |
| 1477 | 2026-09-25 01:11:14 | c858bfee |  | job.enqueued | owner | {"kind": "tooldisc", "payload": {"need": "playwright browser", "max": 1, "day": "2026-09-25"}} |
| 1478 | 2026-09-25 01:11:14 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1479 | 2026-09-25 01:11:16 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1480 | 2026-09-25 01:11:35 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["114 passed in 17.93s"]} |
| 1481 | 2026-09-25 01:11:35 | c858bfee |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1482 | 2026-09-25 01:11:37 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["114 passed in 16.05s"]} |
| 1483 | 2026-09-25 01:12:12 | 0253aa82 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1484 | 2026-09-25 01:12:12 | 463bbc9b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-09-26"}} |
| 1485 | 2026-09-25 01:12:12 | 6ba4e1dc |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-09-25"}} |
| 1486 | 2026-09-25 01:12:12 | 1b095896 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-09-25"}} |
| 1487 | 2026-09-25 01:12:12 | de1d7fdc |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-09-25"}} |
| 1488 | 2026-09-25 01:12:12 | 0253aa82 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1489 | 2026-09-25 01:12:19 | de1d7fdc |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1490 | 2026-09-25 01:12:19 | c22c4f11 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1491 | 2026-09-25 01:12:19 | 3bb0fc5b | 002 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "002", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1492 | 2026-09-25 01:12:19 | 080bdd3e | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "003", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1493 | 2026-09-25 01:12:19 | 7591a1b5 | 004 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "004", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1494 | 2026-09-25 01:12:19 | f649f932 | 005 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "005", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1495 | 2026-09-25 01:12:19 | 5d14608a | 006 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "006", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1496 | 2026-09-25 01:12:19 | 5d804e5d | 007 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "007", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1497 | 2026-09-25 01:12:19 | 8f56eb65 | 008 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "008", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1498 | 2026-09-25 01:12:19 | bd7cfb9e | 009 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "009", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1499 | 2026-09-25 01:12:19 | 8dac341b | 011 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "011", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1500 | 2026-09-25 01:12:19 | 2cb15941 | 012 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "012", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1501 | 2026-09-25 01:12:19 | 31459526 | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "013", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1502 | 2026-09-25 01:12:19 | 667ce093 | 014 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "014", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1503 | 2026-09-25 01:12:19 | 4b8fb54e | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "016", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1504 | 2026-09-25 01:12:19 | 5ba4ca8c | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "017", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1505 | 2026-09-25 01:12:19 | e5ef19df | 018 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "018", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1506 | 2026-09-25 01:12:19 | 13956caf | 019 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "019", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1507 | 2026-09-25 01:12:19 | 3b53fab8 | 020 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "020", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1508 | 2026-09-25 01:12:19 | 72522ac3 | 021 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "021", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1509 | 2026-09-25 01:12:19 | 2332bee3 | 022 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "022", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1510 | 2026-09-25 01:12:19 | 35e53778 | 023 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "023", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1511 | 2026-09-25 01:12:19 | e766a89e | 024 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "024", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1512 | 2026-09-25 01:12:19 | e3d0b490 | 025 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "025", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1513 | 2026-09-25 01:12:19 | 3f73d2dd | 026 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "026", "monitor_of": "de1d7fdc5d12431cbc4d260218c9875d", "day": "2026-09-25"}} |
| 1514 | 2026-09-25 01:12:19 | de1d7fdc |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "002", "003", "004", "005", "006", "007", "008", "009", "011", "012", "013", "014", "016", "017", "018", "019", "020", "021 |
| 1515 | 2026-09-25 01:12:19 | de1d7fdc |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1516 | 2026-09-25 01:12:22 | c858bfee |  | tool.discovered | fast-LAPTOP-LRE6PSA8 | {"tool": "io.github.microsoft/playwright-mcp", "reason": "probation; tools=25 15s", "need": "playwright browser"} |
| 1517 | 2026-09-25 01:12:22 | c858bfee |  | owner.needed | fast-LAPTOP-LRE6PSA8 | {"provider": "tools", "reason": "MCP tools on probation for need 'playwright browser': ['mcp:playwright-mcp'] \u2014 approve to wire into a  |
| 1518 | 2026-09-25 01:12:22 | c858bfee |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": ["mcp:playwright-mcp"]}} |
| 1519 | 2026-09-25 01:12:23 | c22c4f11 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1520 | 2026-09-25 01:12:31 | 3bb0fc5b | 002 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1521 | 2026-09-25 01:12:56 | 3bb0fc5b | 002 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 7s [done] expect='SCOUT_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\002.json' \| T2 FAIL 16s [done] expect='0. |
| 1522 | 2026-09-25 01:12:56 | 3bb0fc5b | 002 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 7s [done] expect='SCOUT_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\002.json' \| T2 FAIL 16s [done] expect='0. |
| 1523 | 2026-09-25 01:12:56 | 3bb0fc5b | 002 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1524 | 2026-09-25 01:12:56 | abe5c895 | 002 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "002", "max_rounds": 2}} |
| 1525 | 2026-09-25 01:12:56 | 3bb0fc5b | 002 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "002", "status": "testing", "verified": "UNVERIFIED"}} |
| 1526 | 2026-09-25 01:13:04 | 080bdd3e | 003 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1527 | 2026-09-25 01:13:53 | 080bdd3e | 003 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 7s [done] expect='SMITH_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\003.json' \| T2 FAIL 16s [done] expect='23 |
| 1528 | 2026-09-25 01:13:54 | 080bdd3e | 003 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 7s [done] expect='SMITH_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\003.json' \| T2 FAIL 16s [done] expect='23 |
| 1529 | 2026-09-25 01:13:54 | 080bdd3e | 003 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1530 | 2026-09-25 01:13:54 | 0fe79cdf | 003 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "003", "max_rounds": 2}} |
| 1531 | 2026-09-25 01:13:54 | 080bdd3e | 003 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "status": "testing", "verified": "UNVERIFIED"}} |
| 1532 | 2026-09-25 01:14:01 | 7591a1b5 | 004 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1533 | 2026-09-25 01:14:41 | c22c4f11 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 16s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 1534 | 2026-09-25 01:14:41 | c22c4f11 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 16s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 1535 | 2026-09-25 01:14:41 | c22c4f11 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 9, "status": "active", "verified": "VERIFIED"}} |
| 1536 | 2026-09-25 01:14:46 | abe5c895 | 002 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1537 | 2026-09-25 01:16:04 | 7591a1b5 | 004 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 10s [done] expect='CHANGELOG_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\004.json' \| T2 FAIL 16s [done] expec |
| 1538 | 2026-09-25 01:16:04 | 7591a1b5 | 004 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 10s [done] expect='CHANGELOG_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\004.json' \| T2 FAIL 16s [done] expec |
| 1539 | 2026-09-25 01:16:04 | 7591a1b5 | 004 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1540 | 2026-09-25 01:16:04 | 29346aa8 | 004 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "004", "max_rounds": 2}} |
| 1541 | 2026-09-25 01:16:04 | 7591a1b5 | 004 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "004", "status": "testing", "verified": "UNVERIFIED"}} |
| 1542 | 2026-09-25 01:16:12 | f649f932 | 005 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1543 | 2026-09-25 01:16:47 | abe5c895 | 002 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 1544 | 2026-09-25 01:16:47 | abe5c895 | 002 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1545 | 2026-09-25 01:16:47 | abe5c895 | 002 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "002", "status": "active"}} |
| 1546 | 2026-09-25 01:16:52 | 0fe79cdf | 003 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1547 | 2026-09-25 01:18:35 | f649f932 | 005 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 58s [done] expect='1' last='1' \| T3 PASS 59s [done] expect='0' last='RE |
| 1548 | 2026-09-25 01:18:35 | f649f932 | 005 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 58s [done] expect='1' last='1' \| T3 PASS 59s [done] expect='0' last='RE |
| 1549 | 2026-09-25 01:18:35 | f649f932 | 005 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "005", "status": "active", "verified": "VERIFIED"}} |
| 1550 | 2026-09-25 01:18:43 | 5d14608a | 006 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1551 | 2026-09-25 01:19:12 | 5d14608a | 006 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "RuntimeError: runner produced no RESULTJSON:\nbot 006 json-to-mar |
| 1552 | 2026-09-25 02:54:06 | 0fe79cdf |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 1553 | 2026-09-25 02:54:06 | e7744308 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1554 | 2026-09-25 02:54:06 | 6f04db95 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T03"}} |
| 1555 | 2026-09-25 02:54:06 | 190e3258 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1556 | 2026-09-25 02:54:06 | abed8a6c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T03"}} |
| 1557 | 2026-09-25 02:54:06 | 190e3258 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1558 | 2026-09-25 02:54:15 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1559 | 2026-09-25 02:55:07 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": false, "tail": ["..."]} |
| 1560 | 2026-09-25 02:55:07 |  |  | worker.blocked_by_tests | fast-LAPTOP-LRE6PSA8 | {"reason": "core/tests red on current code; refusing to process jobs until code changes"} |
| 1561 | 2026-09-25 02:56:02 | e7744308 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "or-ling-30-flash-fin", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 1562 | 2026-09-25 02:56:02 | e7744308 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "or-ling-30-flash-sante", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 1563 | 2026-09-25 02:56:02 | e7744308 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "or-nemotron-35-lightning", "outcome": "error", "before": "INFERRED", "after": "BLOCKED", "detail": "TimeoutError"} |
| 1564 | 2026-09-25 02:56:02 | 738a787a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-09-25", "trigger": "blocked:or-nemotron-35-lightning"}} |
| 1565 | 2026-09-25 02:56:02 | 55ab81e6 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-09-25", "trigger": "blocked:or-nemotron-35-lightning"}} |
| 1566 | 2026-09-25 02:56:02 | c7800973 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-25", "trigger": "blocked:or-nemotron-35-lightning"}} |
| 1567 | 2026-09-25 02:56:02 | cbe38d31 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-25", "trigger": "blocked:or-nemotron-35-lightning"}} |
| 1568 | 2026-09-25 02:56:02 | 99ef519c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-25", "trigger": "blocked:or-nemotron-35-lightning"}} |
| 1569 | 2026-09-25 02:56:02 | c0780098 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-25", "trigger": "blocked:or-nemotron-35-lightning"}} |
| 1570 | 2026-09-25 02:56:02 | e7744308 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite |
| 1571 | 2026-09-25 02:56:05 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1572 | 2026-09-25 02:56:09 |  |  | worker.blocked_by_tests | svc-LAPTOP-LRE6PSA8 | {"reason": "core/tests red on current code; refusing to process jobs until code changes"} |
| 1573 | 2026-09-25 02:56:46 | 5d14608a |  | job.released | owner | {"uncount": false} |
| 1574 | 2026-09-25 02:56:47 | 1952fb1c |  | job.enqueued | owner | {"kind": "selfpatch", "payload": {"date": "2026-09-24", "index": 3}} |
| 1575 | 2026-09-25 02:57:44 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["118 passed in 30.50s"]} |
| 1576 | 2026-09-25 02:57:44 | 0fe79cdf | 003 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 1577 | 2026-09-25 02:57:45 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["118 passed in 30.82s"]} |
| 1578 | 2026-09-25 02:57:45 | 738a787a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1579 | 2026-09-25 02:57:45 | 738a787a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1580 | 2026-09-25 02:57:49 | 55ab81e6 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1581 | 2026-09-25 02:57:49 | 55ab81e6 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1582 | 2026-09-25 02:57:52 | c7800973 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1583 | 2026-09-25 02:57:52 | c7800973 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1584 | 2026-09-25 02:57:56 | cbe38d31 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1585 | 2026-09-25 02:57:56 | cbe38d31 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1586 | 2026-09-25 02:57:59 | 99ef519c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1587 | 2026-09-25 02:57:59 | 99ef519c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1588 | 2026-09-25 02:58:02 | c0780098 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1589 | 2026-09-25 02:58:02 | c0780098 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1590 | 2026-09-25 02:58:05 | 5d804e5d | 007 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1591 | 2026-09-25 03:02:07 | 5d804e5d | 007 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] expect='X_OK' last='X_OK' \| T2 PASS 151s [done] expect='2' last='2' \| T3 PASS 52s [done] expect='0' last='0 |
| 1592 | 2026-09-25 03:02:07 | 5d804e5d | 007 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] expect='X_OK' last='X_OK' \| T2 PASS 151s [done] expect='2' last='2' \| T3 PASS 52s [done] expect='0' last='0 |
| 1593 | 2026-09-25 03:02:07 | 5d804e5d | 007 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "status": "active", "verified": "VERIFIED"}} |
| 1594 | 2026-09-25 03:02:10 | 8f56eb65 | 008 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1595 | 2026-09-25 03:04:51 | 8f56eb65 | 008 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] expect='X_OK' last='X_OK' \| T2 PASS 51s [done] expect='apple' last='RESULT: apple' \| T3 PASS 61s [done] exp |
| 1596 | 2026-09-25 03:04:51 | 8f56eb65 | 008 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] expect='X_OK' last='X_OK' \| T2 PASS 51s [done] expect='apple' last='RESULT: apple' \| T3 PASS 61s [done] exp |
| 1597 | 2026-09-25 03:04:51 | 8f56eb65 | 008 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "008", "status": "active", "verified": "VERIFIED"}} |
| 1598 | 2026-09-25 03:04:56 | bd7cfb9e | 009 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1599 | 2026-09-25 03:05:11 | 0fe79cdf | 003 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 1600 | 2026-09-25 03:05:11 | 0fe79cdf | 003 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1601 | 2026-09-25 03:05:11 | 0fe79cdf | 003 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "status": "active"}} |
| 1602 | 2026-09-25 03:05:21 | 29346aa8 | 004 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1603 | 2026-09-25 03:08:35 | bd7cfb9e | 009 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] expect='X_OK' last='RESULT: X_OK' \| T2 PASS 85s [done] expect='3' last='RESULT: 3' \| T3 PASS 66s [done] exp |
| 1604 | 2026-09-25 03:08:35 | bd7cfb9e | 009 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] expect='X_OK' last='RESULT: X_OK' \| T2 PASS 85s [done] expect='3' last='RESULT: 3' \| T3 PASS 66s [done] exp |
| 1605 | 2026-09-25 03:08:35 | bd7cfb9e | 009 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "009", "status": "active", "verified": "VERIFIED"}} |
| 1606 | 2026-09-25 03:08:39 | 8dac341b | 011 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1607 | 2026-09-25 03:11:49 | 8dac341b | 011 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] expect='X_OK' last='X_OK' \| T2 PASS 69s [done] expect='2' last='RESULT: 2' \| T3 PASS 73s [done] expect='3'  |
| 1608 | 2026-09-25 03:11:49 | 8dac341b | 011 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] expect='X_OK' last='X_OK' \| T2 PASS 69s [done] expect='2' last='RESULT: 2' \| T3 PASS 73s [done] expect='3'  |
| 1609 | 2026-09-25 03:11:49 | 8dac341b | 011 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "011", "status": "active", "verified": "VERIFIED"}} |
| 1610 | 2026-09-25 03:11:52 | 2cb15941 | 012 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1611 | 2026-09-25 03:13:14 | 29346aa8 | 004 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 1612 | 2026-09-25 03:13:14 | 29346aa8 | 004 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1613 | 2026-09-25 03:13:14 | 29346aa8 | 004 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "004", "status": "active"}} |
| 1614 | 2026-09-25 03:13:17 | 1952fb1c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1615 | 2026-09-25 03:13:19 | 1952fb1c |  | factory.selfpatch | svc-LAPTOP-LRE6PSA8 | {"ok": false, "file": "tools/factory_pipeline.py", "lane": "gemini:gemini-flash-lite-latest", "branch": null, "pr": null, "reason": "envelop |
| 1616 | 2026-09-25 03:13:19 | 1952fb1c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1617 | 2026-09-25 03:13:22 | 31459526 | 013 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1618 | 2026-09-25 03:14:04 | 2cb15941 | 012 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] expect='X_OK' last='RESULT: replied with X_OK' \| T2 PASS 41s [done] expect='60' last='RESULT: summed amount  |
| 1619 | 2026-09-25 03:14:04 | 2cb15941 | 012 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 26s [done] expect='X_OK' last='RESULT: replied with X_OK' \| T2 PASS 41s [done] expect='60' last='RESULT: summed amount  |
| 1620 | 2026-09-25 03:14:04 | 2cb15941 | 012 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "012", "status": "active", "verified": "VERIFIED"}} |
| 1621 | 2026-09-25 03:14:08 |  |  | worker.restart | fast-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1622 | 2026-09-25 03:15:01 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": false, "tail": ["...."]} |
| 1623 | 2026-09-25 03:15:01 |  |  | worker.blocked_by_tests | fast-LAPTOP-LRE6PSA8 | {"reason": "core/tests red on current code; refusing to process jobs until code changes"} |
| 1624 | 2026-09-25 03:30:40 | 31459526 | 013 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 173s [done] expect='X_OK' last='X_OK' \| T2 FAIL 306s [TIMEOUT] expect='1' last='' \| T3 FAIL 310s [TIMEOUT] expect='0'  |
| 1625 | 2026-09-25 03:30:40 | 31459526 | 013 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 173s [done] expect='X_OK' last='X_OK' \| T2 FAIL 306s [TIMEOUT] expect='1' last='' \| T3 FAIL 310s [TIMEOUT] expect='0'  |
| 1626 | 2026-09-25 03:30:40 | c3cae46b | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "013", "retest_of": "3145952631084d619cea6973dfe45bb6", "after_quota": "3145952631084d619cea6973dfe45 |
| 1627 | 2026-09-25 03:30:40 | 31459526 | 013 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "013", "status": "active", "verified": "VERIFIED"}} |
| 1628 | 2026-09-25 03:30:44 |  |  | worker.restart | svc-LAPTOP-LRE6PSA8 | {"reason": "code changed on disk"} |
| 1629 | 2026-09-25 03:31:19 |  |  | worker.selftest | fast-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["118 passed in 29.35s"]} |
| 1630 | 2026-09-25 03:31:19 | 667ce093 | 014 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1631 | 2026-09-25 03:31:20 |  |  | worker.selftest | svc-LAPTOP-LRE6PSA8 | {"ok": true, "tail": ["118 passed in 30.39s"]} |
| 1632 | 2026-09-25 03:31:20 | 4b8fb54e | 016 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1633 | 2026-09-25 03:36:49 | 4b8fb54e | 016 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] expect='X_OK' last='X_OK' \| T2 FAIL 16s [done] expect='2' last='CAPABILITY_MISSING: write_file' \| T3 PASS 1 |
| 1634 | 2026-09-25 03:36:49 | 4b8fb54e | 016 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] expect='X_OK' last='X_OK' \| T2 FAIL 16s [done] expect='2' last='CAPABILITY_MISSING: write_file' \| T3 PASS 1 |
| 1635 | 2026-09-25 03:36:49 | 4b8fb54e | 016 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1636 | 2026-09-25 03:36:49 | cc163779 | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "016", "max_rounds": 2}} |
| 1637 | 2026-09-25 03:36:49 | 4b8fb54e | 016 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "016", "status": "testing", "verified": "UNVERIFIED"}} |
| 1638 | 2026-09-25 03:36:53 | cc163779 | 016 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1639 | 2026-09-25 03:36:53 | cc163779 | 016 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [], "boundary_diff": {}} |
| 1640 | 2026-09-25 03:36:53 | 88222656 | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "rearchitect", "payload": {"bot_id": "016", "feedback": "logic: spec/tests inconsistent, repair cannot change tools: bot reported C |
| 1641 | 2026-09-25 03:36:53 | cc163779 | 016 | bot.rearchitect_queued | svc-LAPTOP-LRE6PSA8 | {"reason": "logic: spec/tests inconsistent, repair cannot change tools: bot reported CAPABILITY_MISSING"} |
| 1642 | 2026-09-25 03:36:53 | cc163779 | 016 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: logic: spec/tests inconsistent, repair cannot chang |
| 1643 | 2026-09-25 03:36:56 | 88222656 | 016 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1644 | 2026-09-25 03:38:13 | 88222656 | 016 | bot.rearchitected | svc-LAPTOP-LRE6PSA8 | {"lane": "groq:openai/gpt-oss-20b", "tools": ["exec"], "permissions": ["fs:read", "shell:workspace"], "boundary_diff": {"permissions_added": |
| 1645 | 2026-09-25 03:38:13 | 88222656 | 016 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1646 | 2026-09-25 03:38:13 | cc163779 |  | job.cancelled | svc-LAPTOP-LRE6PSA8 | {} |
| 1647 | 2026-09-25 03:38:13 | cc163779 | 016 | job.superseded | svc-LAPTOP-LRE6PSA8 | {"by": "88222656c78f49cfb2a6e4f6e5b47c26"} |
| 1648 | 2026-09-25 03:38:13 | 88222656 | 016 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "016", "pass": 4, "total": 4, "status": "active"}} |
| 1649 | 2026-09-25 03:38:16 | 5ba4ca8c | 017 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1650 | 2026-09-25 03:44:53 | 667ce093 | 014 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] expect='X_OK' last='X_OK' \| T2 FAIL 307s [TIMEOUT] expect='5' last='' \| T3 FAIL 308s [TIMEOUT] expect='Time |
| 1651 | 2026-09-25 03:44:53 | 667ce093 | 014 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] expect='X_OK' last='X_OK' \| T2 FAIL 307s [TIMEOUT] expect='5' last='' \| T3 FAIL 308s [TIMEOUT] expect='Time |
| 1652 | 2026-09-25 03:44:53 | 7847f8ec | 014 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "014", "retest_of": "667ce093cc1d45b2a1e4f53ea27c1fd9", "after_quota": "667ce093cc1d45b2a1e4f53ea27c1 |
| 1653 | 2026-09-25 03:44:53 | 667ce093 | 014 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "014", "status": "active", "verified": "VERIFIED"}} |
| 1654 | 2026-09-25 03:44:56 | e5ef19df | 018 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1655 | 2026-09-25 03:46:40 | 5ba4ca8c | 017 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 61s [done] expect='X_OK' last='RESULT: X_OK' \| T2 FAIL 155s [done] expect='3' last='\u00e2\u2020\u00b3 read names.txt'  |
| 1656 | 2026-09-25 03:46:40 | 5ba4ca8c | 017 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 61s [done] expect='X_OK' last='RESULT: X_OK' \| T2 FAIL 155s [done] expect='3' last='\u00e2\u2020\u00b3 read names.txt'  |
| 1657 | 2026-09-25 03:46:40 | 5ba4ca8c | 017 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1658 | 2026-09-25 03:46:40 | 9b60274b | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "017", "max_rounds": 2}} |
| 1659 | 2026-09-25 03:46:40 | 5ba4ca8c | 017 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "017", "status": "testing", "verified": "UNVERIFIED"}} |
| 1660 | 2026-09-25 03:46:43 | 9b60274b | 017 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1661 | 2026-09-25 03:55:14 | e5ef19df | 018 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 68s [done] expect='X_OK' last='X_OK' \| T2 PASS 300s [done] expect='30' last='RESULT: 30' \| T3 PASS 191s [done] expect= |
| 1662 | 2026-09-25 03:55:14 | e5ef19df | 018 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 68s [done] expect='X_OK' last='X_OK' \| T2 PASS 300s [done] expect='30' last='RESULT: 30' \| T3 PASS 191s [done] expect= |
| 1663 | 2026-09-25 03:55:14 | e5ef19df | 018 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "status": "active", "verified": "VERIFIED"}} |
| 1664 | 2026-09-25 03:55:17 | 6f04db95 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1665 | 2026-09-25 03:55:17 | 509087ef |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T04"}} |
| 1666 | 2026-09-25 03:57:00 | 6f04db95 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 1667 | 2026-09-25 03:57:00 | 5866157b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1668 | 2026-09-25 03:57:00 | 71d0bcfc |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1669 | 2026-09-25 03:57:00 | 9b42f1aa |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1670 | 2026-09-25 03:57:00 | 52fea279 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1671 | 2026-09-25 03:57:00 | 279f51c7 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1672 | 2026-09-25 03:57:00 | d540257b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1673 | 2026-09-25 03:57:00 | 6f04db95 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss1 |
| 1674 | 2026-09-25 03:57:03 | abed8a6c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1675 | 2026-09-25 03:57:03 | 586e9f0e |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T04"}} |
| 1676 | 2026-09-25 03:57:03 | abed8a6c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1677 | 2026-09-25 03:57:05 | 5866157b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1678 | 2026-09-25 03:57:06 | 5866157b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1679 | 2026-09-25 03:57:08 | 71d0bcfc |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1680 | 2026-09-25 03:57:08 | 71d0bcfc |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1681 | 2026-09-25 03:57:11 | 9b42f1aa |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1682 | 2026-09-25 03:57:11 | 9b42f1aa |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1683 | 2026-09-25 03:57:12 | 9b60274b | 017 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 1684 | 2026-09-25 03:57:12 | 9b60274b | 017 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1685 | 2026-09-25 03:57:12 | 9b60274b | 017 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "017", "status": "active"}} |
| 1686 | 2026-09-25 03:57:13 | 52fea279 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1687 | 2026-09-25 03:57:13 | 52fea279 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1688 | 2026-09-25 03:57:16 | 279f51c7 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1689 | 2026-09-25 03:57:16 | 279f51c7 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1690 | 2026-09-25 03:57:18 | d540257b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1691 | 2026-09-25 03:57:18 | d540257b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1692 | 2026-09-25 03:57:21 | 13956caf | 019 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1693 | 2026-09-25 03:57:21 | 3b53fab8 | 020 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1694 | 2026-09-25 04:01:20 | 13956caf | 019 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] expect='X_OK' last='X_OK' \| T2 PASS 99s [done] expect='1' last='RESULT: 1' \| T3 PASS 102s [done] expect='CO |
| 1695 | 2026-09-25 04:01:20 | 13956caf | 019 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] expect='X_OK' last='X_OK' \| T2 PASS 99s [done] expect='1' last='RESULT: 1' \| T3 PASS 102s [done] expect='CO |
| 1696 | 2026-09-25 04:01:20 | 13956caf | 019 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "019", "status": "active", "verified": "VERIFIED"}} |
| 1697 | 2026-09-25 04:01:23 | 72522ac3 | 021 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1698 | 2026-09-25 04:03:07 | 3b53fab8 | 020 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] expect='X_OK' last='X_OK' \| T2 FAIL 305s [TIMEOUT] expect='DONE' last='' \| T3 PASS 19s [done] expect='CONFI |
| 1699 | 2026-09-25 04:03:07 | 3b53fab8 | 020 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] expect='X_OK' last='X_OK' \| T2 FAIL 305s [TIMEOUT] expect='DONE' last='' \| T3 PASS 19s [done] expect='CONFI |
| 1700 | 2026-09-25 04:03:07 | 3d281d06 | 020 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "020", "retest_of": "3b53fab8c9474ef6a1570af2666136be", "after_quota": "3b53fab8c9474ef6a1570af266613 |
| 1701 | 2026-09-25 04:03:07 | 3b53fab8 | 020 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "020", "status": "active", "verified": "VERIFIED"}} |
| 1702 | 2026-09-25 04:03:10 | 2332bee3 | 022 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1703 | 2026-09-25 04:03:26 | 72522ac3 | 021 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] expect='X_OK' last='X_OK' \| T2 PASS 46s [done] expect='2' last='2' \| T3 FAIL 6s [done] expect='1' last='Usi |
| 1704 | 2026-09-25 04:03:26 | 72522ac3 | 021 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] expect='X_OK' last='X_OK' \| T2 PASS 46s [done] expect='2' last='2' \| T3 FAIL 6s [done] expect='1' last='Usi |
| 1705 | 2026-09-25 04:03:26 | d62f34ea | 021 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "021", "retest_of": "72522ac3aab24ff0bee10f6aec1dbe28", "after_quota": "72522ac3aab24ff0bee10f6aec1db |
| 1706 | 2026-09-25 04:03:26 | 72522ac3 | 021 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "021", "status": "active", "verified": "VERIFIED"}} |
| 1707 | 2026-09-25 04:03:28 | 35e53778 | 023 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1708 | 2026-09-25 04:08:08 | 35e53778 | 023 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] expect='X_OK' last='X_OK' \| T2 PASS 86s [done] expect='36.0' last='RESULT: 36.0' \| T3 PASS 127s [done] expe |
| 1709 | 2026-09-25 04:08:08 | 35e53778 | 023 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] expect='X_OK' last='X_OK' \| T2 PASS 86s [done] expect='36.0' last='RESULT: 36.0' \| T3 PASS 127s [done] expe |
| 1710 | 2026-09-25 04:08:08 | 35e53778 | 023 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "023", "status": "active", "verified": "VERIFIED"}} |
| 1711 | 2026-09-25 04:08:10 | e766a89e | 024 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1712 | 2026-09-25 04:08:58 | e766a89e | 024 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] expect='X_OK' last='X_OK' \| T2 PASS 18s [done] expect='2' last='RESULT: 2' \| T3 PASS 17s [done] expect='CON |
| 1713 | 2026-09-25 04:08:58 | e766a89e | 024 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] expect='X_OK' last='X_OK' \| T2 PASS 18s [done] expect='2' last='RESULT: 2' \| T3 PASS 17s [done] expect='CON |
| 1714 | 2026-09-25 04:08:58 | e766a89e | 024 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "024", "status": "active", "verified": "VERIFIED"}} |
| 1715 | 2026-09-25 04:08:58 | 2332bee3 | 022 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] expect='X_OK' last='X_OK' \| T2 PASS 183s [done] expect='2' last='RESULT: 2' \| T3 PASS 108s [done] expect='2 |
| 1716 | 2026-09-25 04:08:58 | 2332bee3 | 022 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] expect='X_OK' last='X_OK' \| T2 PASS 183s [done] expect='2' last='RESULT: 2' \| T3 PASS 108s [done] expect='2 |
| 1717 | 2026-09-25 04:08:58 | 2332bee3 | 022 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "022", "status": "active", "verified": "VERIFIED"}} |
| 1718 | 2026-09-25 04:09:01 | e3d0b490 | 025 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1719 | 2026-09-25 04:09:04 | 3f73d2dd | 026 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1720 | 2026-09-25 04:09:51 | e3d0b490 | 025 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='LIVENESS_OK' last='LIVENESS_OK' \| T2 PASS 20s [done] expect='HELLO WORLD' last='RESULT: HELLO WORLD' |
| 1721 | 2026-09-25 04:09:51 | e3d0b490 | 025 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='LIVENESS_OK' last='LIVENESS_OK' \| T2 PASS 20s [done] expect='HELLO WORLD' last='RESULT: HELLO WORLD' |
| 1722 | 2026-09-25 04:09:51 | e3d0b490 | 025 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "025", "status": "active", "verified": "VERIFIED"}} |
| 1723 | 2026-09-25 04:10:32 | 3f73d2dd | 026 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] expect='X_OK' last='X_OK' \| T2 PASS 23s [done] expect='3' last='RESULT: 3' \| T3 PASS 23s [done] expect='use |
| 1724 | 2026-09-25 04:10:32 | 3f73d2dd | 026 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] expect='X_OK' last='X_OK' \| T2 PASS 23s [done] expect='3' last='RESULT: 3' \| T3 PASS 23s [done] expect='use |
| 1725 | 2026-09-25 04:10:32 | 3f73d2dd | 026 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "026", "status": "active", "verified": "VERIFIED"}} |
| 1726 | 2026-09-25 04:10:35 | 6ba4e1dc |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1727 | 2026-09-25 04:10:35 | 6ba4e1dc |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": []}} |
| 1728 | 2026-09-25 04:10:38 | 1b095896 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1729 | 2026-09-25 04:11:09 | 1b095896 |  | factory.canary | svc-LAPTOP-LRE6PSA8 | {"verdict": "pass", "lane": "groq:openai/gpt-oss-20b", "chain": ["gemini-gemini-flash-lite-latest", "gemini-lite31", "or-nex-n25-pro", "or-l |
| 1730 | 2026-09-25 04:11:09 | 1b095896 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"pass": 2, "total": 2}} |
| 1731 | 2026-09-25 04:55:18 | 509087ef |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1732 | 2026-09-25 04:55:18 | 321d882a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T05"}} |
| 1733 | 2026-09-25 04:55:28 | 509087ef |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss1 |
| 1734 | 2026-09-25 04:57:06 | 586e9f0e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1735 | 2026-09-25 04:57:06 | 5249b5ec |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T05"}} |
| 1736 | 2026-09-25 04:57:06 | 586e9f0e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1737 | 2026-09-25 05:30:42 | c3cae46b | 013 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1738 | 2026-09-25 05:32:29 | c3cae46b | 013 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 21s [done] expect='X_OK' last='RESULT: 1' \| T2 PASS 27s [done] expect='1' last='RESULT: 1' \| T3 PASS 28s [done] expect |
| 1739 | 2026-09-25 05:32:29 | c3cae46b | 013 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 21s [done] expect='X_OK' last='RESULT: 1' \| T2 PASS 27s [done] expect='1' last='RESULT: 1' \| T3 PASS 28s [done] expect |
| 1740 | 2026-09-25 05:32:29 | c3cae46b | 013 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1741 | 2026-09-25 05:32:29 | 9c18c9e9 | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "013", "max_rounds": 2}} |
| 1742 | 2026-09-25 05:32:29 | c3cae46b | 013 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "013", "status": "testing", "verified": "UNVERIFIED"}} |
| 1743 | 2026-09-25 05:32:32 | 9c18c9e9 | 013 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1744 | 2026-09-25 05:33:49 | 9c18c9e9 | 013 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 1745 | 2026-09-25 05:33:49 | 9c18c9e9 | 013 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1746 | 2026-09-25 05:33:49 | 9c18c9e9 | 013 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "013", "status": "active"}} |
| 1747 | 2026-09-25 11:22:56 | 5249b5ec |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1748 | 2026-09-25 11:22:57 | 321d882a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1749 | 2026-09-25 11:22:58 | 03fe2791 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T12"}} |
| 1750 | 2026-09-25 11:22:59 | dae5c79f | 018 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "run", "payload": {"bot_id": "018", "task": "Sum order totals per country into totals.csv", "in": "C:\\AI\\Factory\\workspace\\inbo |
| 1751 | 2026-09-25 11:22:59 |  | 018 | schedule.fired | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "fire": "2026-09-25T07:00", "job": "dae5c79f"} |
| 1752 | 2026-09-25 11:23:04 | e354bd05 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T12"}} |
| 1753 | 2026-09-25 11:23:04 | 5249b5ec |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1754 | 2026-09-25 11:23:05 | 7847f8ec | 014 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1755 | 2026-09-25 11:23:15 | 321d882a |  | model.retired | fast-LAPTOP-LRE6PSA8 | {"model": "or-deepseek", "reason": "gone: {\"error\":{\"message\":\"this model is unavailable for free. the paid version "} |
| 1756 | 2026-09-25 11:23:15 | 321d882a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite |
| 1757 | 2026-09-25 11:23:18 | 3d281d06 | 020 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1758 | 2026-09-25 11:25:27 | 7847f8ec | 014 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 28s [done] expect='5' last='RESULT: 5' \| T3 PASS 71s [done] expect='Tim |
| 1759 | 2026-09-25 11:25:27 | 7847f8ec | 014 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 28s [done] expect='5' last='RESULT: 5' \| T3 PASS 71s [done] expect='Tim |
| 1760 | 2026-09-25 11:25:27 | 7847f8ec | 014 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "014", "status": "active", "verified": "VERIFIED"}} |
| 1761 | 2026-09-25 11:25:30 | d62f34ea | 021 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1762 | 2026-09-25 11:27:31 | d62f34ea | 021 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 45s [done] expect='2' last='RESULT: 2' \| T3 PASS 40s [done] expect='1' l |
| 1763 | 2026-09-25 11:27:31 | d62f34ea | 021 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 45s [done] expect='2' last='RESULT: 2' \| T3 PASS 40s [done] expect='1' l |
| 1764 | 2026-09-25 11:27:31 | d62f34ea | 021 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "021", "status": "active", "verified": "VERIFIED"}} |
| 1765 | 2026-09-25 11:27:34 | dae5c79f | 018 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1766 | 2026-09-25 11:28:17 | dae5c79f | 018 | bot.ran | svc-LAPTOP-LRE6PSA8 | {"ok": true, "produced": ["totals.csv"], "secs": 42, "reply": "RESULT: success", "chain": "groq-gptoss120b"} |
| 1767 | 2026-09-25 11:28:17 | dae5c79f | 018 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "name": "run", "status": "ok totals.csv"}} |
| 1768 | 2026-09-25 11:28:44 | 3d281d06 | 020 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 FAIL 306s [TIMEOUT] expect='DONE' last='' \| T3 PASS 9s [done] expect='CONFIN |
| 1769 | 2026-09-25 11:28:44 | 3d281d06 | 020 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 FAIL 306s [TIMEOUT] expect='DONE' last='' \| T3 PASS 9s [done] expect='CONFIN |
| 1770 | 2026-09-25 11:28:44 | a35b45be | 020 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "020", "retest_of": "3b53fab8c9474ef6a1570af2666136be", "after_quota": "3d281d0693674fd4a5e204ec31add |
| 1771 | 2026-09-25 11:28:44 | 3d281d06 | 020 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "020", "status": "active", "verified": "VERIFIED"}} |
| 1772 | 2026-09-25 12:23:57 | 03fe2791 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1773 | 2026-09-25 12:23:57 | e354bd05 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1774 | 2026-09-25 12:23:57 | 0a541bde |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T13"}} |
| 1775 | 2026-09-25 12:24:03 | e1e4c7f4 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T13"}} |
| 1776 | 2026-09-25 12:24:03 | e354bd05 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1777 | 2026-09-25 12:24:15 | 03fe2791 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 1778 | 2026-09-25 12:24:15 | 03fe2791 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-l |
| 1779 | 2026-09-25 13:23:58 | 0a541bde |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1780 | 2026-09-25 13:23:58 | 4f127831 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T14"}} |
| 1781 | 2026-09-25 13:24:05 | e1e4c7f4 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1782 | 2026-09-25 13:24:05 | b7558c0f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T14"}} |
| 1783 | 2026-09-25 13:24:05 | e1e4c7f4 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1784 | 2026-09-25 13:24:19 | 0a541bde |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 1785 | 2026-09-25 13:24:19 | 426bd52b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1786 | 2026-09-25 13:24:19 | 624ec5f9 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1787 | 2026-09-25 13:24:19 | 29f3da03 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1788 | 2026-09-25 13:24:19 | a3514a3e |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1789 | 2026-09-25 13:24:19 | c14ad4dd |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1790 | 2026-09-25 13:24:19 | 23979c6a |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1791 | 2026-09-25 13:24:19 | 0a541bde |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite |
| 1792 | 2026-09-25 13:24:22 | 426bd52b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1793 | 2026-09-25 13:24:22 | 426bd52b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1794 | 2026-09-25 13:24:23 | 624ec5f9 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1795 | 2026-09-25 13:24:24 | 624ec5f9 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1796 | 2026-09-25 13:24:25 | 29f3da03 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1797 | 2026-09-25 13:24:25 | 29f3da03 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1798 | 2026-09-25 13:24:28 | a3514a3e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1799 | 2026-09-25 13:24:28 | a3514a3e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1800 | 2026-09-25 13:24:31 | c14ad4dd |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1801 | 2026-09-25 13:24:31 | c14ad4dd |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1802 | 2026-09-25 13:24:33 | 23979c6a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1803 | 2026-09-25 13:24:33 | 23979c6a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1804 | 2026-09-25 14:20:17 | a35b45be | 020 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1805 | 2026-09-25 19:59:42 | a35b45be |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 1806 | 2026-09-25 19:59:42 | 4f127831 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1807 | 2026-09-25 19:59:42 | 865a2980 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T20"}} |
| 1808 | 2026-09-25 19:59:44 | 4f127831 |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 16 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 1809 | 2026-09-25 19:59:44 | 96ccf58b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T14-retry", "retry_of": "4f127831509c447c8aaaba0702a59478"}} |
| 1810 | 2026-09-25 19:59:44 | 4f127831 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1811 | 2026-09-25 19:59:48 | b7558c0f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1812 | 2026-09-25 19:59:52 | 54829a12 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T20"}} |
| 1813 | 2026-09-25 19:59:52 | b7558c0f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1814 | 2026-09-25 20:00:00 | a35b45be | 020 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 1815 | 2026-09-25 20:02:28 | a35b45be | 020 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 PASS 124s [done] expect='DONE' last='DONE' \| T3 PASS 12s [done] expect='CONF |
| 1816 | 2026-09-25 20:02:28 | a35b45be | 020 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 PASS 124s [done] expect='DONE' last='DONE' \| T3 PASS 12s [done] expect='CONF |
| 1817 | 2026-09-25 20:02:28 | a35b45be | 020 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "020", "status": "active", "verified": "VERIFIED"}} |
| 1818 | 2026-09-25 20:05:30 | a35b45be | 020 | job.orphaned_result | fast-LAPTOP-LRE6PSA8 | {"error": "Command '['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', 'C:\\\\AI\\\\Factory\\\\repo\\\\scripts\\\\windows\\ |
| 1819 | 2026-09-25 20:09:44 | 96ccf58b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1820 | 2026-09-25 20:09:45 | 80e90b9b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T21"}} |
| 1821 | 2026-09-25 20:10:16 | 96ccf58b |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 1822 | 2026-09-25 20:10:16 | 96ccf58b |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "or-nex-n25-pro", "outcome": "gone", "before": "VERIFIED", "after": "BLOCKED", "detail": "{\"error\":{\"message\":\"no endpoints f |
| 1823 | 2026-09-25 20:10:16 | 134bba89 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-09-25", "trigger": "blocked:or-nex-n25-pro"}} |
| 1824 | 2026-09-25 20:10:16 | 01537a5d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-09-25", "trigger": "blocked:or-nex-n25-pro"}} |
| 1825 | 2026-09-25 20:10:16 | 3fa27047 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-25", "trigger": "blocked:or-nex-n25-pro"}} |
| 1826 | 2026-09-25 20:10:16 | 2bbe411d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-25", "trigger": "blocked:or-nex-n25-pro"}} |
| 1827 | 2026-09-25 20:10:16 | a7cf454b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-25", "trigger": "blocked:or-nex-n25-pro"}} |
| 1828 | 2026-09-25 20:10:16 | e9039318 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-25", "trigger": "blocked:or-nex-n25-pro"}} |
| 1829 | 2026-09-25 20:10:16 | a1ec1245 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": ["014"], "day": "2026-09-25", "canary_for": ["or-nex-n25-pro"]}} |
| 1830 | 2026-09-25 20:10:16 | 96ccf58b |  | monitor.canary | fast-LAPTOP-LRE6PSA8 | {"lanes": ["or-nex-n25-pro"], "bots": ["014"]} |
| 1831 | 2026-09-25 20:10:16 | 96ccf58b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 1832 | 2026-09-25 20:10:20 | 134bba89 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1833 | 2026-09-25 20:10:20 | 01537a5d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1834 | 2026-09-25 20:10:21 | 134bba89 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1835 | 2026-09-25 20:10:21 | 01537a5d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
