# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 2577 | 2026-09-27 10:04:11 | 503129d5 | 027 | bot.ran | fast-LAPTOP-LRE6PSA8 | {"ok": true, "produced": [], "secs": 41, "reply": "RESULT: 0", "chain": "gemini-gemini-flash-lite-latest"} |
| 2578 | 2026-09-27 10:04:11 | 503129d5 | 027 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "027", "name": "run", "status": "ok "}} |
| 2579 | 2026-09-27 10:04:27 | de920621 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [d |
| 2580 | 2026-09-27 10:04:27 | de920621 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [d |
| 2581 | 2026-09-27 10:04:27 | de920621 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2582 | 2026-09-27 10:04:27 | 18fc5545 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "de92062169c04aeda0da0cf84992e13 |
| 2583 | 2026-09-27 10:04:27 | de920621 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2584 | 2026-09-27 10:18:51 | 252fcb22 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2585 | 2026-09-27 10:21:45 | 252fcb22 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [d |
| 2586 | 2026-09-27 10:21:45 | 252fcb22 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [d |
| 2587 | 2026-09-27 10:21:45 | 252fcb22 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2588 | 2026-09-27 10:21:45 | bf357b8a | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "252fcb22a1dc4d539abc824783c9e9c |
| 2589 | 2026-09-27 10:21:45 | 252fcb22 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2590 | 2026-09-27 10:34:29 | 18fc5545 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2591 | 2026-09-27 10:37:25 | 18fc5545 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [do |
| 2592 | 2026-09-27 10:37:25 | 18fc5545 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [do |
| 2593 | 2026-09-27 10:37:25 | 18fc5545 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2594 | 2026-09-27 10:37:25 | 2414722a | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "18fc5545e55d415bb6cb6dd1de85164 |
| 2595 | 2026-09-27 10:37:25 | 18fc5545 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2596 | 2026-09-27 10:51:47 | bf357b8a | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2597 | 2026-09-27 10:55:22 | bf357b8a | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [do |
| 2598 | 2026-09-27 10:55:22 | bf357b8a | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [do |
| 2599 | 2026-09-27 10:55:22 | bf357b8a | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2600 | 2026-09-27 10:55:22 | 5a2b3caf | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "bf357b8a29b9483aa89dc0f7a85b3e2 |
| 2601 | 2026-09-27 10:55:22 | bf357b8a | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2602 | 2026-09-27 10:59:00 | bc6c1367 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2603 | 2026-09-27 10:59:00 | 88c99a0b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-27T11"}} |
| 2604 | 2026-09-27 10:59:23 | bc6c1367 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 2605 | 2026-09-27 11:00:17 | 6def4486 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2606 | 2026-09-27 11:00:17 | 793c48be |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-27T12"}} |
| 2607 | 2026-09-27 11:00:17 | 6def4486 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2608 | 2026-09-27 11:07:26 | 2414722a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2609 | 2026-09-27 11:10:24 | 2414722a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 15s [d |
| 2610 | 2026-09-27 11:10:24 | 2414722a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 15s [d |
| 2611 | 2026-09-27 11:10:24 | 2414722a | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2612 | 2026-09-27 11:10:24 | c8a06098 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "2414722acddf437db9611fb4fc99920 |
| 2613 | 2026-09-27 11:10:24 | 2414722a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2614 | 2026-09-27 11:25:23 | 5a2b3caf | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2615 | 2026-09-27 11:31:44 | 5a2b3caf | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [do |
| 2616 | 2026-09-27 11:31:44 | 5a2b3caf | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [do |
| 2617 | 2026-09-27 11:31:44 | 5a2b3caf | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2618 | 2026-09-27 11:31:44 | a7a3251b | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "5a2b3caf17da429385cf6775a1a0b0e |
| 2619 | 2026-09-27 11:31:44 | 5a2b3caf | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2620 | 2026-09-27 11:40:26 | c8a06098 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2621 | 2026-09-27 11:49:04 | 374622aa | 027 | job.enqueued | master-001 | {"kind": "run", "payload": {"bot_id": "027", "task": "summarize the factory's weekly self-review and include a count of created bots", "in": |
| 2622 | 2026-09-27 11:49:08 | 374622aa | 027 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2623 | 2026-09-27 11:49:41 | 374622aa | 027 | bot.ran | fast-LAPTOP-LRE6PSA8 | {"ok": true, "produced": [], "secs": 32, "reply": "Using config: C:\\AI\\Factory\\run\\botcfg\\027-task.json", "chain": "gemini-gemini-flash |
| 2624 | 2026-09-27 11:49:41 | 374622aa | 027 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "027", "name": "run", "status": "ok "}} |
| 2625 | 2026-09-27 11:50:11 | c8a06098 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 54s [d |
| 2626 | 2026-09-27 11:50:11 | c8a06098 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 54s [d |
| 2627 | 2026-09-27 11:50:11 | c8a06098 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2628 | 2026-09-27 11:50:11 | 8de834d5 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "c8a0609840bb4342ad3948caa116799 |
| 2629 | 2026-09-27 11:50:11 | c8a06098 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2630 | 2026-09-27 11:59:01 | 88c99a0b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2631 | 2026-09-27 11:59:01 | 092262db |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-27T12"}} |
| 2632 | 2026-09-27 11:59:19 | 88c99a0b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qw |
| 2633 | 2026-09-27 12:00:17 | 793c48be |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2634 | 2026-09-27 12:00:18 | ed16b7b3 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-27T13"}} |
| 2635 | 2026-09-27 12:00:18 | 793c48be |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2636 | 2026-09-27 12:01:46 | a7a3251b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2637 | 2026-09-27 12:14:02 | a7a3251b | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 103s [done] report expect='FACTORY' cmd=True \| T3 PASS 64s [ |
| 2638 | 2026-09-27 12:14:02 | a7a3251b | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 103s [done] report expect='FACTORY' cmd=True \| T3 PASS 64s [ |
| 2639 | 2026-09-27 12:14:02 | a7a3251b | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2640 | 2026-09-27 12:14:02 | 7560f693 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "a7a3251b1495441db5dbba1ba28cd73 |
| 2641 | 2026-09-27 12:14:02 | a7a3251b | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2642 | 2026-09-27 12:20:12 | 8de834d5 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2643 | 2026-09-27 12:30:44 | 8de834d5 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 54s [done] report expect='FACTORY' cmd=True \| T3 PASS 53s [do |
| 2644 | 2026-09-27 12:30:44 | 8de834d5 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 54s [done] report expect='FACTORY' cmd=True \| T3 PASS 53s [do |
| 2645 | 2026-09-27 12:30:44 | 8de834d5 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2646 | 2026-09-27 12:30:44 | 0c4528ad | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "8de834d540c046c5a5b6219ffa1aea2 |
| 2647 | 2026-09-27 12:30:44 | 8de834d5 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2648 | 2026-09-27 14:02:23 | ed16b7b3 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2649 | 2026-09-27 14:02:23 | 092262db |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2650 | 2026-09-27 14:02:24 | 06a21c84 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-27T15"}} |
| 2651 | 2026-09-27 14:50:46 | cc6dbeee |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-27T15"}} |
| 2652 | 2026-09-27 14:50:46 | ed16b7b3 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2653 | 2026-09-27 14:50:51 | 092262db |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 2654 | 2026-09-27 14:50:51 | 092262db |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 2655 | 2026-09-27 14:50:51 | 06a21c84 |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 2656 | 2026-09-27 14:52:00 | 092262db |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq- |
| 2657 | 2026-09-27 14:52:06 | 7560f693 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2658 | 2026-09-27 14:52:15 | 092262db |  | job.orphaned_result | fast-LAPTOP-LRE6PSA8 | {"summary": "{'probed': 20, 'healthy': ['gemini-flash', 'gemini-flash38', 'gemini-gemini-flash-lite-latest', 'gemini-gemma26b', 'gemini-lite |
| 2659 | 2026-09-27 15:01:53 | 7560f693 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 76s [done] report expect='FACTORY' cmd=True \| T3 PASS 63s [d |
| 2660 | 2026-09-27 15:01:53 | 7560f693 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 76s [done] report expect='FACTORY' cmd=True \| T3 PASS 63s [d |
| 2661 | 2026-09-27 15:01:53 | 7560f693 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2662 | 2026-09-27 15:01:53 | e5b67ac6 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "7560f69369e84164bc0dedc30b9cfaa |
| 2663 | 2026-09-27 15:01:53 | 7560f693 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2664 | 2026-09-27 15:01:55 | 0c4528ad | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2665 | 2026-09-27 15:02:27 | 06a21c84 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2666 | 2026-09-27 15:02:27 | 609cbe8c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-27T16"}} |
| 2667 | 2026-09-27 15:02:46 | 06a21c84 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq- |
| 2668 | 2026-09-27 15:13:46 | 0c4528ad | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 77s [d |
| 2669 | 2026-09-27 15:13:46 | 0c4528ad | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 77s [d |
| 2670 | 2026-09-27 15:13:46 | 0c4528ad | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2671 | 2026-09-27 15:13:46 | 9b8338f6 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "0c4528ad78ff4f49922241cc765e6df |
| 2672 | 2026-09-27 15:13:46 | 0c4528ad | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2673 | 2026-09-27 15:31:55 | e5b67ac6 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2674 | 2026-09-27 15:44:20 | e5b67ac6 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 63s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 2675 | 2026-09-27 15:44:20 | e5b67ac6 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 63s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 2676 | 2026-09-27 15:44:20 | e5b67ac6 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2677 | 2026-09-27 15:44:20 | bfdd1597 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "e5b67ac6d094472cb066975a0041952 |
| 2678 | 2026-09-27 15:44:20 | e5b67ac6 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2679 | 2026-09-27 15:44:21 | 9b8338f6 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2680 | 2026-09-27 15:50:51 | cc6dbeee |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2681 | 2026-09-27 15:50:52 | d125629c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-27T16"}} |
| 2682 | 2026-09-27 15:50:52 | cc6dbeee |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2683 | 2026-09-27 15:55:33 | 9b8338f6 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 2684 | 2026-09-27 15:55:33 | 9b8338f6 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 2685 | 2026-09-27 15:55:33 | 9b8338f6 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2686 | 2026-09-27 15:55:33 | 6bcf758e | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "9b8338f66883443994f9da2ffed1161 |
| 2687 | 2026-09-27 15:55:33 | 9b8338f6 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2688 | 2026-09-27 16:02:29 | 609cbe8c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2689 | 2026-09-27 16:02:29 | b9103be1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-27T17"}} |
| 2690 | 2026-09-27 16:02:53 | 609cbe8c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b |
| 2691 | 2026-09-27 16:14:23 | bfdd1597 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2692 | 2026-09-27 16:26:54 | bfdd1597 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 100s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [ |
| 2693 | 2026-09-27 16:26:54 | bfdd1597 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 100s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [ |
| 2694 | 2026-09-27 16:26:54 | bfdd1597 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2695 | 2026-09-27 16:26:54 | 9da18f93 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "bfdd1597bfc645d88bf3aab23dc0996 |
| 2696 | 2026-09-27 16:26:54 | bfdd1597 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2697 | 2026-09-27 16:26:59 | 6bcf758e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2698 | 2026-09-27 16:38:52 | 6bcf758e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 2699 | 2026-09-27 16:38:52 | 6bcf758e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 2700 | 2026-09-27 16:38:52 | 5622d1ef | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "6bcf758e5e1d47099cbdb599abb2f786", "after_quota": "6bcf758e5e1d47099cbdb599abb2f |
| 2701 | 2026-09-27 16:38:52 | 6bcf758e | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2702 | 2026-09-27 16:50:53 | d125629c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2703 | 2026-09-27 16:50:53 | 31503b5a |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-27T17"}} |
| 2704 | 2026-09-27 16:50:53 | d125629c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2705 | 2026-09-27 16:56:55 | 9da18f93 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2706 | 2026-09-27 17:02:33 | b9103be1 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2707 | 2026-09-27 17:02:33 | dc082234 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-27T18"}} |
| 2708 | 2026-09-27 17:02:57 | b9103be1 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 2709 | 2026-09-27 17:02:57 | ca9b6391 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-09-27", "trigger": "blocked:gemini-flash36"}} |
| 2710 | 2026-09-27 17:02:57 | 70f44c73 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-09-27", "trigger": "blocked:gemini-flash36"}} |
| 2711 | 2026-09-27 17:02:57 | 3f1cce3e |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-27", "trigger": "blocked:gemini-flash36"}} |
| 2712 | 2026-09-27 17:02:57 | 2de17048 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-27", "trigger": "blocked:gemini-flash36"}} |
| 2713 | 2026-09-27 17:02:57 | 88cf4134 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-27", "trigger": "blocked:gemini-flash36"}} |
| 2714 | 2026-09-27 17:02:57 | fe7e90ca |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-27", "trigger": "blocked:gemini-flash36"}} |
| 2715 | 2026-09-27 17:02:57 | b9103be1 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qw |
| 2716 | 2026-09-27 17:03:02 | ca9b6391 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2717 | 2026-09-27 17:03:02 | ca9b6391 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 2718 | 2026-09-27 17:03:07 | 70f44c73 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2719 | 2026-09-27 17:03:08 | 70f44c73 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 2720 | 2026-09-27 17:03:13 | 3f1cce3e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2721 | 2026-09-27 17:03:14 | 3f1cce3e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 2722 | 2026-09-27 17:03:19 | 2de17048 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2723 | 2026-09-27 17:03:19 | 2de17048 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 2724 | 2026-09-27 17:03:23 | 88cf4134 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2725 | 2026-09-27 17:03:23 | 88cf4134 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 2726 | 2026-09-27 17:03:27 | fe7e90ca |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2727 | 2026-09-27 17:03:27 | fe7e90ca |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 2728 | 2026-09-27 17:08:23 | 9da18f93 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 2729 | 2026-09-27 17:08:23 | 9da18f93 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 59s [d |
| 2730 | 2026-09-27 17:08:23 | 9da18f93 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2731 | 2026-09-27 17:08:23 | de7ade5c | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "9da18f9325354658b95fe186c6c6e2d |
| 2732 | 2026-09-27 17:08:23 | 9da18f93 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2733 | 2026-09-27 17:38:24 | de7ade5c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2734 | 2026-09-27 17:50:00 | de7ade5c | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 2735 | 2026-09-27 17:50:00 | de7ade5c | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 2736 | 2026-09-27 17:50:00 | de7ade5c | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2737 | 2026-09-27 17:50:00 | 7989ffdc | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "de7ade5c374548bf8b5256ea2af12d9 |
| 2738 | 2026-09-27 17:50:00 | de7ade5c | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2739 | 2026-09-27 17:50:55 | 31503b5a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2740 | 2026-09-27 17:50:55 | 9c6c39a8 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-27T18"}} |
| 2741 | 2026-09-27 17:50:55 | 31503b5a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2742 | 2026-09-27 18:02:35 | dc082234 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2743 | 2026-09-27 18:02:35 | f65a08d6 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-27T19"}} |
| 2744 | 2026-09-27 18:02:58 | dc082234 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 2745 | 2026-09-27 18:02:58 | dc082234 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gp |
| 2746 | 2026-09-27 18:20:02 | 7989ffdc | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2747 | 2026-09-27 18:32:10 | 7989ffdc | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 2748 | 2026-09-27 18:32:10 | 7989ffdc | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 2749 | 2026-09-27 18:32:10 | 7989ffdc | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2750 | 2026-09-27 18:32:10 | 35361536 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "7989ffdce734446abea6620e4bb81b2 |
| 2751 | 2026-09-27 18:32:10 | 7989ffdc | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2752 | 2026-09-27 18:38:54 | 5622d1ef | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2753 | 2026-09-27 18:50:56 | 9c6c39a8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2754 | 2026-09-27 18:50:57 | 6d750294 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-27T19"}} |
| 2755 | 2026-09-27 18:50:57 | 9c6c39a8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2756 | 2026-09-27 18:52:06 | 5622d1ef | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 2757 | 2026-09-27 18:52:06 | 5622d1ef | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 2758 | 2026-09-27 18:52:06 | 5622d1ef | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2759 | 2026-09-27 18:52:06 | 755bae1d | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "5622d1ef14844e268311187bd1509f0 |
| 2760 | 2026-09-27 18:52:06 | 5622d1ef | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2761 | 2026-09-27 21:14:40 | f65a08d6 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2762 | 2026-09-27 21:14:40 | f14d8be7 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-27T22"}} |
| 2763 | 2026-09-27 21:14:48 | 6d750294 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2764 | 2026-09-27 21:15:02 | d3e50c5d |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-27T22"}} |
| 2765 | 2026-09-27 21:15:02 | 6d750294 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2766 | 2026-09-27 21:15:08 | 35361536 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2767 | 2026-09-27 21:15:18 | f65a08d6 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-l |
| 2768 | 2026-09-27 21:24:18 | 35361536 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 54s [done] report expect='FACTORY' cmd=True \| T3 PASS 52s [d |
| 2769 | 2026-09-27 21:24:18 | 35361536 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 54s [done] report expect='FACTORY' cmd=True \| T3 PASS 52s [d |
| 2770 | 2026-09-27 21:24:18 | 35361536 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2771 | 2026-09-27 21:24:18 | cba34842 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "35361536a4204770beed9866e4745da |
| 2772 | 2026-09-27 21:24:18 | 35361536 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2773 | 2026-09-27 21:24:20 | 755bae1d | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2774 | 2026-09-27 21:35:43 | 755bae1d | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 49s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 56s [d |
| 2775 | 2026-09-27 21:35:43 | 755bae1d | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 49s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 56s [d |
| 2776 | 2026-09-27 21:35:43 | 755bae1d | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2777 | 2026-09-27 21:35:43 | 0168b47b | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "755bae1d7efb47bb9c5ef3ec34170f6 |
| 2778 | 2026-09-27 21:35:43 | 755bae1d | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2779 | 2026-09-27 21:54:19 | cba34842 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2780 | 2026-09-27 22:03:48 | 2566f26c | 027 | job.enqueued | master-001 | {"kind": "run", "payload": {"bot_id": "027", "task": "review the factory status and update the self-review to include the total number of bo |
| 2781 | 2026-09-27 22:03:53 | 2566f26c | 027 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2782 | 2026-09-27 22:05:06 | 2566f26c | 027 | bot.ran | fast-LAPTOP-LRE6PSA8 | {"ok": true, "produced": [], "secs": 72, "reply": "\u00e2\u2020\u00b3 read SOUL.md", "chain": "gemini-gemini-flash-lite-latest"} |
| 2783 | 2026-09-27 22:05:06 | 2566f26c | 027 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "027", "name": "run", "status": "ok "}} |
| 2784 | 2026-09-27 22:06:03 | cba34842 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 2785 | 2026-09-27 22:06:03 | cba34842 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 2786 | 2026-09-27 22:06:03 | cba34842 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2787 | 2026-09-27 22:06:03 | 2747b9fd | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "cba34842923f46148177f20f3ab65f4 |
| 2788 | 2026-09-27 22:06:03 | cba34842 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2789 | 2026-09-27 22:06:05 | 0168b47b | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2790 | 2026-09-27 22:14:42 | f14d8be7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2791 | 2026-09-27 22:14:42 | 4c9f5482 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-27T23"}} |
| 2792 | 2026-09-27 22:14:57 | f14d8be7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemma26b", "groq-gptoss120b", "groq-gptoss20b", "groq-q |
| 2793 | 2026-09-27 22:15:06 | d3e50c5d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2794 | 2026-09-27 22:15:07 | 7faa8790 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-27T23"}} |
| 2795 | 2026-09-27 22:15:07 | d3e50c5d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2796 | 2026-09-27 22:28:14 | 0168b47b | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 2797 | 2026-09-27 22:29:16 | 0168b47b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 2798 | 2026-09-27 22:48:11 | 0168b47b | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 69s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 124s [done] report expect='FACTORY' cmd=True \| T3 PASS 91s [ |
| 2799 | 2026-09-27 22:48:12 | 0168b47b | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 69s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 124s [done] report expect='FACTORY' cmd=True \| T3 PASS 91s [ |
| 2800 | 2026-09-27 22:48:12 | eff17c52 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "0168b47b0454491bbe5ad5cb4beaa8ea", "after_quota": "0168b47b0454491bbe5ad5cb4beaa |
| 2801 | 2026-09-27 22:48:12 | 0168b47b | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2802 | 2026-09-27 22:48:14 | 2747b9fd | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2803 | 2026-09-27 23:08:41 | 2747b9fd | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 78s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 149s [done] report expect='FACTORY' cmd=True \| T3 PASS 84s [ |
| 2804 | 2026-09-27 23:08:41 | 2747b9fd | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 78s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 149s [done] report expect='FACTORY' cmd=True \| T3 PASS 84s [ |
| 2805 | 2026-09-27 23:08:41 | 9b453632 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "2747b9fd5d9c48f2980e492fe3995bf3", "after_quota": "2747b9fd5d9c48f2980e492fe3995 |
| 2806 | 2026-09-27 23:08:41 | 2747b9fd | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2807 | 2026-09-27 23:14:44 | 4c9f5482 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2808 | 2026-09-27 23:14:44 | cee38882 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-28T00"}} |
| 2809 | 2026-09-27 23:15:11 | 7faa8790 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2810 | 2026-09-27 23:15:11 | 9e6bab05 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-28T00"}} |
| 2811 | 2026-09-27 23:15:11 | 7faa8790 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2812 | 2026-09-27 23:15:49 | 4c9f5482 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-flash38", "gemini-gemma26b", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3 |
| 2813 | 2026-09-28 00:14:44 | cee38882 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2814 | 2026-09-28 00:14:44 | beb522de |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-28T01"}} |
| 2815 | 2026-09-28 00:15:13 | 9e6bab05 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2816 | 2026-09-28 00:15:13 | 66e79d3e |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-28T01"}} |
| 2817 | 2026-09-28 00:15:13 | 9e6bab05 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2818 | 2026-09-28 00:15:16 | cee38882 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemma26b", "groq-gptoss120b", "groq-gptoss20b", "groq-q |
| 2819 | 2026-09-28 01:30:30 | beb522de |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2820 | 2026-09-28 01:30:30 | 66e79d3e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2821 | 2026-09-28 01:30:30 | fc453a3f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-28T02"}} |
| 2822 | 2026-09-28 01:30:31 | beb522de |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 2823 | 2026-09-28 01:30:31 | c705cf8c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-28T01-retry", "retry_of": "beb522de515d406e90e1a6bcd51527f9"}} |
| 2824 | 2026-09-28 01:30:31 | beb522de |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2825 | 2026-09-28 01:30:34 | eff17c52 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2826 | 2026-09-28 01:30:35 | 81cad91a |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-28T02"}} |
| 2827 | 2026-09-28 01:30:35 | 66e79d3e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2828 | 2026-09-28 01:40:32 | c705cf8c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2829 | 2026-09-28 01:40:32 | fc453a3f |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 2830 | 2026-09-28 01:41:00 | c705cf8c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-flash38", "gemini-gemma26b", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3 |
| 2831 | 2026-09-28 01:41:46 | eff17c52 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 102s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [ |
| 2832 | 2026-09-28 01:41:46 | eff17c52 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 102s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [ |
| 2833 | 2026-09-28 01:41:46 | 5013c9f9 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "0168b47b0454491bbe5ad5cb4beaa8ea", "after_quota": "eff17c527d7c47e8b0eea4f955f7c |
| 2834 | 2026-09-28 01:41:46 | eff17c52 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2835 | 2026-09-28 01:41:49 | 9b453632 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2836 | 2026-09-28 01:56:54 | 9b453632 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 45s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 85s [done] report expect='FACTORY' cmd=True \| T3 PASS 87s [d |
| 2837 | 2026-09-28 01:56:54 | 9b453632 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 45s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 85s [done] report expect='FACTORY' cmd=True \| T3 PASS 87s [d |
| 2838 | 2026-09-28 01:56:54 | ec968d47 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "2747b9fd5d9c48f2980e492fe3995bf3", "after_quota": "9b4536328f894f588928e3eb6d905 |
| 2839 | 2026-09-28 01:56:54 | 9b453632 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2840 | 2026-09-28 07:26:17 | c6ebd328 |  | job.enqueued | nightly-task | {"kind": "monitor", "payload": {"only": null, "day": "2026-09-28"}} |
| 2841 | 2026-09-29 18:01:47 |  |  | factory.outage | fast-LAPTOP-LRE6PSA8 | {"gap_min": 2075, "silent_since": "2026-09-28T07:26:17", "last_event": "job.enqueued", "cause": "power loss / battery flat (kernel-power 41) |
| 2842 | 2026-09-29 18:01:48 |  |  | factory.outage | svc-LAPTOP-LRE6PSA8 | {"gap_min": 2075, "silent_since": "2026-09-28T07:26:17", "last_event": "job.enqueued", "cause": "power loss / battery flat (kernel-power 41) |
| 2843 | 2026-09-29 18:01:48 | fc453a3f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2844 | 2026-09-29 18:01:48 | 4f6d66a5 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-29T19"}} |
| 2845 | 2026-09-29 18:01:49 | 81cad91a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2846 | 2026-09-29 18:01:49 | 9b18bfe0 | 018 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "run", "payload": {"bot_id": "018", "task": "Sum order totals per country into totals.csv", "in": "C:\\AI\\Factory\\workspace\\inbo |
| 2847 | 2026-09-29 18:01:49 |  | 018 | schedule.fired | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "fire": "2026-09-29T07:00", "job": "9b18bfe0"} |
| 2848 | 2026-09-29 18:01:49 | c256f1f3 | 027 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "run", "payload": {"bot_id": "027", "task": "Perform weekly self-review, including a count of all bots created in the factory to da |
| 2849 | 2026-09-29 18:01:49 |  | 027 | schedule.fired | fast-LAPTOP-LRE6PSA8 | {"sid": "c9e4d22f", "fire": "2026-09-28T09:00", "job": "c256f1f3"} |
| 2850 | 2026-09-29 18:01:50 | 7f41dddc |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-29T19"}} |
| 2851 | 2026-09-29 18:01:50 | 81cad91a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2852 | 2026-09-29 18:01:57 | 5013c9f9 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2853 | 2026-09-29 18:02:54 | fc453a3f |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "or-ling-30-flash-fin", "outcome": "gone", "before": "VERIFIED", "after": "BLOCKED", "detail": "{\"error\":{\"message\":\"this mod |
| 2854 | 2026-09-29 18:02:54 | fc453a3f |  | model.retired | svc-LAPTOP-LRE6PSA8 | {"model": "or-nex-n25-pro", "reason": "gone: {\"error\":{\"message\":\"this model is unavailable for free. the paid version "} |
| 2855 | 2026-09-29 18:02:54 | b62be530 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-09-29", "trigger": "blocked:or-ling-30-flash-fin"}} |
| 2856 | 2026-09-29 18:02:54 | c9e9f708 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-09-29", "trigger": "blocked:or-ling-30-flash-fin"}} |
| 2857 | 2026-09-29 18:02:54 | feed78f0 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-29", "trigger": "blocked:or-ling-30-flash-fin"}} |
| 2858 | 2026-09-29 18:02:54 | 00a18cc0 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-29", "trigger": "blocked:or-ling-30-flash-fin"}} |
| 2859 | 2026-09-29 18:02:54 | a237fa20 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-29", "trigger": "blocked:or-ling-30-flash-fin"}} |
| 2860 | 2026-09-29 18:02:54 | de32e89e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-29", "trigger": "blocked:or-ling-30-flash-fin"}} |
| 2861 | 2026-09-29 18:02:54 | fc453a3f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "groq-gptoss120b", "groq-gptoss20b", "groq-qwe |
| 2862 | 2026-09-29 18:03:04 | b62be530 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2863 | 2026-09-29 18:03:05 | b62be530 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 2864 | 2026-09-29 18:03:13 | c9e9f708 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2865 | 2026-09-29 18:03:15 | c9e9f708 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 2866 | 2026-09-29 18:03:21 | feed78f0 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2867 | 2026-09-29 18:03:24 | feed78f0 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 2868 | 2026-09-29 18:03:30 | 00a18cc0 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2869 | 2026-09-29 18:03:30 | 00a18cc0 |  | owner.needed | svc-LAPTOP-LRE6PSA8 | {"provider": "cerebras", "reason": "set CEREBRAS_API_KEY (User env) after signing up: https://cloud.cerebras.ai (free tier ~1M tokens/day)"} |
| 2870 | 2026-09-29 18:03:30 | 00a18cc0 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 2871 | 2026-09-29 18:03:36 | a237fa20 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2872 | 2026-09-29 18:03:36 | a237fa20 |  | owner.needed | svc-LAPTOP-LRE6PSA8 | {"provider": "nvidia", "reason": "set NVIDIA_API_KEY (User env) after signing up: https://build.nvidia.com (free ~40 rpm, tool-capable model |
| 2873 | 2026-09-29 18:03:36 | a237fa20 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 2874 | 2026-09-29 18:03:44 | de32e89e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2875 | 2026-09-29 18:03:45 | de32e89e |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 2876 | 2026-09-29 18:03:51 | c6ebd328 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2877 | 2026-09-29 18:03:51 | 579491c3 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2878 | 2026-09-29 18:03:51 | 1ecb9227 | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "003", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2879 | 2026-09-29 18:03:51 | 0f59f40f | 005 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "005", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2880 | 2026-09-29 18:03:51 | 09146563 | 006 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "006", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2881 | 2026-09-29 18:03:51 | 0f19ad75 | 007 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "007", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2882 | 2026-09-29 18:03:51 | 96e43656 | 008 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "008", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2883 | 2026-09-29 18:03:51 | 09ce9ce4 | 009 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "009", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2884 | 2026-09-29 18:03:51 | e6462e61 | 011 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "011", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2885 | 2026-09-29 18:03:51 | 8eec6c54 | 012 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "012", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2886 | 2026-09-29 18:03:51 | 0969955b | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "013", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2887 | 2026-09-29 18:03:51 | 7ce257a8 | 014 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "014", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2888 | 2026-09-29 18:03:51 | 598a5cc4 | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "016", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2889 | 2026-09-29 18:03:51 | fd26f12c | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "017", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2890 | 2026-09-29 18:03:51 | 37ca8049 | 018 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "018", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2891 | 2026-09-29 18:03:51 | f2bb4b62 | 019 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "019", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2892 | 2026-09-29 18:03:51 | bb48c3f9 | 022 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "022", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2893 | 2026-09-29 18:03:51 | 6a59bbe3 | 023 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "023", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2894 | 2026-09-29 18:03:51 | 5929288f | 024 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "024", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2895 | 2026-09-29 18:03:51 | 65e0de3b | 025 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "025", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2896 | 2026-09-29 18:03:51 | 30f205bc | 026 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "026", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2897 | 2026-09-29 18:03:51 | 4da83d39 | 027 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "027", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "day": "2026-09-28"}} |
| 2898 | 2026-09-29 18:03:51 | c6ebd328 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "003", "005", "006", "007", "008", "009", "011", "012", "013", "014", "016", "017", "018", "019", "022", "023", "024", "025 |
| 2899 | 2026-09-29 18:03:51 | c6ebd328 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2900 | 2026-09-29 18:03:57 | 9b18bfe0 | 018 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2901 | 2026-09-29 18:04:11 | 9b18bfe0 | 018 | bot.ran | svc-LAPTOP-LRE6PSA8 | {"ok": true, "produced": [], "secs": 13, "reply": "Using config: C:\\AI\\Factory\\run\\botcfg\\018-task.json", "chain": "groq-gptoss120b"} |
| 2902 | 2026-09-29 18:04:11 | 9b18bfe0 | 018 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "name": "run", "status": "ok "}} |
| 2903 | 2026-09-29 18:04:16 | c256f1f3 | 027 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2904 | 2026-09-29 18:04:29 | c256f1f3 | 027 | bot.ran | svc-LAPTOP-LRE6PSA8 | {"ok": true, "produced": [], "secs": 11, "reply": "Using config: C:\\AI\\Factory\\run\\botcfg\\027-task.json", "chain": "gemini-gemini-flash |
| 2905 | 2026-09-29 18:04:29 | c256f1f3 | 027 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "027", "name": "run", "status": "ok "}} |
| 2906 | 2026-09-29 18:04:32 | 934b7127 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2907 | 2026-09-29 18:04:32 | 934b7127 |  | audit.verified | svc-LAPTOP-LRE6PSA8 | {"rows": 2905, "hashed": 2153, "first_bad": null} |
| 2908 | 2026-09-29 18:04:32 | d85823bb |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-09-30"}} |
| 2909 | 2026-09-29 18:04:32 | dda50f35 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-09-29"}} |
| 2910 | 2026-09-29 18:04:32 | 09024b3a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-09-29"}} |
| 2911 | 2026-09-29 18:04:32 | 33d3730f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-09-29"}} |
| 2912 | 2026-09-29 18:04:32 | 934b7127 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2913 | 2026-09-29 18:04:37 | 33d3730f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2914 | 2026-09-29 18:04:37 | cfc7b1fc | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2915 | 2026-09-29 18:04:37 | 96c4c77a | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "003", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2916 | 2026-09-29 18:04:37 | e717ddc1 | 005 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "005", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2917 | 2026-09-29 18:04:37 | 4d8b6f21 | 006 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "006", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2918 | 2026-09-29 18:04:37 | 3b04ee67 | 007 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "007", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2919 | 2026-09-29 18:04:37 | 2f8c68e5 | 008 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "008", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2920 | 2026-09-29 18:04:37 | 92b55be6 | 009 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "009", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2921 | 2026-09-29 18:04:37 | a0ca3faa | 011 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "011", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2922 | 2026-09-29 18:04:37 | 46a9742e | 012 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "012", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2923 | 2026-09-29 18:04:37 | c1be9289 | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "013", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2924 | 2026-09-29 18:04:37 | 3053504b | 014 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "014", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2925 | 2026-09-29 18:04:37 | 9746e6aa | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "016", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2926 | 2026-09-29 18:04:37 | e70a2e86 | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "017", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2927 | 2026-09-29 18:04:37 | 38770f25 | 018 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "018", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2928 | 2026-09-29 18:04:37 | 665ef041 | 019 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "019", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2929 | 2026-09-29 18:04:37 | 196465d0 | 022 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "022", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2930 | 2026-09-29 18:04:37 | 24eb3217 | 023 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "023", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2931 | 2026-09-29 18:04:37 | 349839fb | 024 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "024", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2932 | 2026-09-29 18:04:37 | ff9a5304 | 025 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "025", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2933 | 2026-09-29 18:04:37 | 8a363ecb | 026 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "026", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2934 | 2026-09-29 18:04:37 | fbcc0040 | 027 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "027", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "day": "2026-09-29"}} |
| 2935 | 2026-09-29 18:04:37 | 33d3730f |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "003", "005", "006", "007", "008", "009", "011", "012", "013", "014", "016", "017", "018", "019", "022", "023", "024", "025 |
| 2936 | 2026-09-29 18:04:37 | 33d3730f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2937 | 2026-09-29 18:04:41 | 1ecb9227 | 003 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2938 | 2026-09-29 18:05:56 | 1ecb9227 | 003 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='RESULT: X_OK' \| T2 FAIL 6s [done] expect='3' last='' \| T3 PASS 34s [done] expect='6' la |
| 2939 | 2026-09-29 18:05:56 | 1ecb9227 | 003 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='RESULT: X_OK' \| T2 FAIL 6s [done] expect='3' last='' \| T3 PASS 34s [done] expect='6' la |
| 2940 | 2026-09-29 18:05:56 | 1ecb9227 | 003 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2941 | 2026-09-29 18:05:56 | 1826bc15 | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "003", "max_rounds": 2}} |
| 2942 | 2026-09-29 18:05:56 | 1ecb9227 | 003 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "status": "testing", "verified": "UNVERIFIED"}} |
| 2943 | 2026-09-29 18:06:04 | 1826bc15 | 003 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2944 | 2026-09-29 18:07:10 | 3ec8a25d |  | job.enqueued | master-001 | {"kind": "create", "payload": {"objective": "Perform weekly self-review, including a count of all bots created in the factory"}} |
| 2945 | 2026-09-29 18:07:33 | 5013c9f9 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [d |
| 2946 | 2026-09-29 18:07:33 | 5013c9f9 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [d |
| 2947 | 2026-09-29 18:07:33 | 5013c9f9 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2948 | 2026-09-29 18:07:33 | de0ebcc5 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "5013c9f9485a4a3bb03f449fef77f74 |
| 2949 | 2026-09-29 18:07:33 | 5013c9f9 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2950 | 2026-09-29 18:07:42 | ec968d47 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2951 | 2026-09-29 18:08:47 | 1826bc15 | 003 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-120b", "sandbox": "1/4", "rejected": null}, {"round" |
| 2952 | 2026-09-29 18:08:47 | 1826bc15 | 003 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 2953 | 2026-09-29 18:08:52 | 3ec8a25d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2954 | 2026-09-29 18:08:59 | 3ec8a25d | 028 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "weekly-self-review", "tools": ["read_file", "write_file", "web_search"], "permissions": ["fs:read", "fs:write", "net:search", "net |
| 2955 | 2026-09-29 18:09:45 | 3ec8a25d | 028 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 7s [done] expect='X_OK' last='' \| T2 PASS 24s [done] expect='3' last='RESULT: 3' \| T3 FAIL 2s [done] expect='5' last=' |
| 2956 | 2026-09-29 18:09:45 | da8c8c2d | 028 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "028", "retest_of": "3ec8a25d148b49e5aad06a0ec23fa5fb"}} |
| 2957 | 2026-09-29 18:09:45 | 3ec8a25d | 028 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "028", "name": "weekly-self-review", "pass": 2, "total": 4, "status": "testing", "verified": "UNVERIFIED"}} |
| 2958 | 2026-09-29 18:09:50 | da8c8c2d | 028 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2959 | 2026-09-29 18:10:52 | da8c8c2d | 028 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 8s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\028.json' \| T2 PASS 13s [done] expect='3' las |
| 2960 | 2026-09-29 18:10:52 | 9155875e | 028 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "028", "retest_of": "3ec8a25d148b49e5aad06a0ec23fa5fb", "after_quota": "da8c8c2df2414390af46ec0bbc031 |
| 2961 | 2026-09-29 18:10:52 | da8c8c2d | 028 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "028", "status": "testing", "verified": "UNVERIFIED"}} |
| 2962 | 2026-09-29 18:10:56 | 0f59f40f | 005 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2963 | 2026-09-29 18:12:08 | 0f59f40f | 005 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 PASS 25s [done] expect='1' last='RESULT: 1' \| T3 FAIL 25s [done] expect='0'  |
| 2964 | 2026-09-29 18:12:08 | 0f59f40f | 005 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] expect='X_OK' last='X_OK' \| T2 PASS 25s [done] expect='1' last='RESULT: 1' \| T3 FAIL 25s [done] expect='0'  |
| 2965 | 2026-09-29 18:12:08 | 0f59f40f | 005 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2966 | 2026-09-29 18:12:09 | 2a020aa6 | 005 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "005", "max_rounds": 2}} |
| 2967 | 2026-09-29 18:12:09 | 0f59f40f | 005 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "005", "status": "testing", "verified": "UNVERIFIED"}} |
| 2968 | 2026-09-29 18:12:09 | ec968d47 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 2969 | 2026-09-29 18:12:09 | ec968d47 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 2970 | 2026-09-29 18:12:09 | ec968d47 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2971 | 2026-09-29 18:12:09 | 23ec7b81 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "ec968d47c9244c56a1754735a4739fe |
| 2972 | 2026-09-29 18:12:09 | ec968d47 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2973 | 2026-09-29 18:12:14 | 2a020aa6 | 005 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2974 | 2026-09-29 18:12:20 | 579491c3 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2975 | 2026-09-29 18:13:09 | 2a020aa6 | 005 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-120b", "sandbox": null, "rejected": ["fallback 'or-d |
| 2976 | 2026-09-29 18:13:09 | 2a020aa6 | 005 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
