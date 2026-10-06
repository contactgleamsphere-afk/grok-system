# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 4739 | 2026-10-04 14:35:09 | 754c7cd3 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 17s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 4740 | 2026-10-04 14:35:09 | 754c7cd3 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4741 | 2026-10-04 14:35:09 | 40f8cb60 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "496e3afd58764673a6b80d4e1d7f4792", "retry_of": "754c7cd3e52d44bca520690e920db00 |
| 4742 | 2026-10-04 14:35:09 | 754c7cd3 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4743 | 2026-10-04 14:35:12 | f79c53db | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4744 | 2026-10-04 14:40:28 | f79c53db | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 17s [done] report expect='FACTORY' cmd=True \| T3 PASS 16s [d |
| 4745 | 2026-10-04 14:40:28 | f79c53db | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 17s [done] report expect='FACTORY' cmd=True \| T3 PASS 16s [d |
| 4746 | 2026-10-04 14:40:28 | f79c53db | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4747 | 2026-10-04 14:40:28 | 77881c8a | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "f79c53db008a4a37a532bd3ffb7148e |
| 4748 | 2026-10-04 14:40:28 | f79c53db | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4749 | 2026-10-04 14:40:29 | afb9f6f5 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4750 | 2026-10-04 14:43:28 | 3d977ea8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4751 | 2026-10-04 14:43:28 | 13c2fcc2 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-04T15"}} |
| 4752 | 2026-10-04 14:44:13 | 3d977ea8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash-latest", "gemini-flash36", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", " |
| 4753 | 2026-10-04 14:44:17 | b3e37bd2 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4754 | 2026-10-04 14:44:17 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4755 | 2026-10-04 14:44:18 | f643009e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-04T15"}} |
| 4756 | 2026-10-04 14:44:18 | b3e37bd2 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4757 | 2026-10-04 14:54:23 | afb9f6f5 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 63s [done] report expect='FACTORY' cmd=True \| T3 PASS 39s [d |
| 4758 | 2026-10-04 14:54:23 | afb9f6f5 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 63s [done] report expect='FACTORY' cmd=True \| T3 PASS 39s [d |
| 4759 | 2026-10-04 14:54:23 | 0fcbde87 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "afb9f6f5ab6a418db3f5bd977c09026e", "after_quota": "afb9f6f5ab6a418db3f5bd977c090 |
| 4760 | 2026-10-04 14:54:23 | afb9f6f5 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4761 | 2026-10-04 14:54:28 | 07e26f32 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4762 | 2026-10-04 15:24:14 | 07e26f32 |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 4763 | 2026-10-04 15:24:14 | 07e26f32 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 4764 | 2026-10-04 15:25:56 | 07e26f32 | 001 | job.orphaned_result | fast-LAPTOP-LRE6PSA8 | {"error": "Command '['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', 'C:\\\\AI\\\\Factory\\\\repo\\\\scripts\\\\windows\\ |
| 4765 | 2026-10-04 15:38:00 | 07e26f32 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 76s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 4766 | 2026-10-04 15:38:01 | 07e26f32 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 76s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 4767 | 2026-10-04 15:38:01 | 1785f254 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "07e26f32402644c6a7533696fca37040", "after_quota": "07e26f32402644c6a7533696fca37 |
| 4768 | 2026-10-04 15:38:01 | 07e26f32 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4769 | 2026-10-04 15:38:05 | 8df68b4e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4770 | 2026-10-04 15:43:31 | 13c2fcc2 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4771 | 2026-10-04 15:43:31 | 1344d1db |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-04T16"}} |
| 4772 | 2026-10-04 15:44:11 | 13c2fcc2 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "gro |
| 4773 | 2026-10-04 15:44:19 | f643009e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4774 | 2026-10-04 15:44:19 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4775 | 2026-10-04 15:44:20 | 7426515a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-04T16"}} |
| 4776 | 2026-10-04 15:44:20 | f643009e |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4777 | 2026-10-04 15:51:07 | 8df68b4e |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 4778 | 2026-10-04 15:51:07 | 8df68b4e | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 4779 | 2026-10-04 15:51:07 | 8df68b4e |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 4780 | 2026-10-04 16:04:55 | 8df68b4e | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 80s [done] report expect='FACTORY' cmd=True \| T3 PASS 79s [d |
| 4781 | 2026-10-04 16:04:55 | 8df68b4e | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 80s [done] report expect='FACTORY' cmd=True \| T3 PASS 79s [d |
| 4782 | 2026-10-04 16:04:55 | 80d0007d | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "8df68b4e54e54c76825de45193e93e05", "after_quota": "8df68b4e54e54c76825de45193e93 |
| 4783 | 2026-10-04 16:04:55 | 8df68b4e | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4784 | 2026-10-04 16:04:58 | 7ac3c1ce | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4785 | 2026-10-04 16:17:42 | 7ac3c1ce | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 4786 | 2026-10-04 16:17:42 | 7ac3c1ce | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 4787 | 2026-10-04 16:17:42 | 80768061 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "7ac3c1cedde04eafb0831bbd85fe7d5e", "after_quota": "7ac3c1cedde04eafb0831bbd85fe7 |
| 4788 | 2026-10-04 16:17:42 | 7ac3c1ce | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4789 | 2026-10-04 16:17:45 | 40f8cb60 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4790 | 2026-10-04 16:29:55 | 40f8cb60 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4791 | 2026-10-04 16:29:55 | 40f8cb60 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4792 | 2026-10-04 16:29:55 | abfbd09c | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "40f8cb60c2554b72ab00e23f2a950 |
| 4793 | 2026-10-04 16:29:55 | 40f8cb60 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4794 | 2026-10-04 16:29:56 | 77881c8a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4795 | 2026-10-04 16:42:34 | 77881c8a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4796 | 2026-10-04 16:42:34 | 77881c8a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 68s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4797 | 2026-10-04 16:42:34 | f20f93d1 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "77881c8a8a21429c95000f5ff5430657", "after_quota": "77881c8a8a21429c95000f5ff5430 |
| 4798 | 2026-10-04 16:42:34 | 77881c8a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4799 | 2026-10-04 16:43:33 | 1344d1db |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4800 | 2026-10-04 16:43:33 | dc6e18de |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-04T17"}} |
| 4801 | 2026-10-04 16:43:58 | 1344d1db |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "gr |
| 4802 | 2026-10-04 16:44:21 | 7426515a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4803 | 2026-10-04 16:44:21 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4804 | 2026-10-04 16:44:21 | bf698996 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-04T17"}} |
| 4805 | 2026-10-04 16:44:21 | 7426515a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4806 | 2026-10-04 16:54:25 | 0fcbde87 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4807 | 2026-10-04 17:07:30 | 0fcbde87 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4808 | 2026-10-04 17:07:30 | 0fcbde87 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4809 | 2026-10-04 17:07:30 | e3099199 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "afb9f6f5ab6a418db3f5bd977c09026e", "after_quota": "0fcbde873acf4b48b2795b3128bb3 |
| 4810 | 2026-10-04 17:07:30 | 0fcbde87 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4811 | 2026-10-04 17:38:02 | 1785f254 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4812 | 2026-10-04 17:43:35 | dc6e18de |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4813 | 2026-10-04 17:43:35 | 7d9282f3 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-04T18"}} |
| 4814 | 2026-10-04 17:44:34 | dc6e18de |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "gro |
| 4815 | 2026-10-04 17:44:37 | bf698996 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4816 | 2026-10-04 17:44:37 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4817 | 2026-10-04 17:44:38 | a500471e |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-04T18"}} |
| 4818 | 2026-10-04 17:44:38 | bf698996 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4819 | 2026-10-04 17:51:28 | 1785f254 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 81s [done] report expect='FACTORY' cmd=True \| T3 PASS 75s [do |
| 4820 | 2026-10-04 17:51:28 | 1785f254 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 81s [done] report expect='FACTORY' cmd=True \| T3 PASS 75s [do |
| 4821 | 2026-10-04 17:51:28 | 2e2fba20 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "07e26f32402644c6a7533696fca37040", "after_quota": "1785f254116346ea8d600677c5c4f |
| 4822 | 2026-10-04 17:51:28 | 1785f254 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4823 | 2026-10-04 18:04:56 | 80d0007d | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4824 | 2026-10-04 18:18:35 | 80d0007d | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 73s [done] report expect='FACTORY' cmd=True \| T3 PASS 73s [d |
| 4825 | 2026-10-04 18:18:35 | 80d0007d | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 73s [done] report expect='FACTORY' cmd=True \| T3 PASS 73s [d |
| 4826 | 2026-10-04 18:18:35 | ef9271c4 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "8df68b4e54e54c76825de45193e93e05", "after_quota": "80d0007da94c4dd5842b9464fce1b |
| 4827 | 2026-10-04 18:18:35 | 80d0007d | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4828 | 2026-10-04 18:18:36 | 80768061 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4829 | 2026-10-04 18:30:56 | 80768061 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 4830 | 2026-10-04 18:30:56 | 80768061 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 4831 | 2026-10-04 18:30:56 | 80768061 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4832 | 2026-10-04 18:30:56 | a2f5a601 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "076d00557198429696acd4c0a35af210", "retry_of": "80768061331948febcde902e7b20970 |
| 4833 | 2026-10-04 18:30:56 | 80768061 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4834 | 2026-10-04 18:30:59 | abfbd09c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4835 | 2026-10-04 18:43:35 | abfbd09c | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 4836 | 2026-10-04 18:43:35 | abfbd09c | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 4837 | 2026-10-04 18:43:35 | 20604f3a | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "40f8cb60c2554b72ab00e23f2a9503aa", "after_quota": "abfbd09cade24f1193d4604480eb8 |
| 4838 | 2026-10-04 18:43:35 | abfbd09c | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4839 | 2026-10-04 18:43:36 | 7d9282f3 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4840 | 2026-10-04 18:43:36 | 77064141 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-04T19"}} |
| 4841 | 2026-10-04 18:43:38 | f20f93d1 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4842 | 2026-10-04 18:43:53 | 7d9282f3 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "gro |
| 4843 | 2026-10-04 18:44:42 | a500471e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4844 | 2026-10-04 18:44:42 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4845 | 2026-10-04 18:44:42 | 9522cede |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-04T19"}} |
| 4846 | 2026-10-04 18:44:42 | a500471e |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4847 | 2026-10-04 18:57:14 | f20f93d1 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4848 | 2026-10-04 18:57:14 | f20f93d1 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4849 | 2026-10-04 18:57:14 | f512992d | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "77881c8a8a21429c95000f5ff5430657", "after_quota": "f20f93d1e0dc4a6581725203aa00e |
| 4850 | 2026-10-04 18:57:14 | f20f93d1 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4851 | 2026-10-04 19:00:57 | a2f5a601 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4852 | 2026-10-04 19:13:54 | a2f5a601 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 72s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4853 | 2026-10-04 19:13:54 | a2f5a601 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 72s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4854 | 2026-10-04 19:13:54 | 434d7bd4 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a2f5a601f2d84985b479c18f015c9c2e", "after_quota": "a2f5a601f2d84985b479c18f015c9 |
| 4855 | 2026-10-04 19:13:54 | a2f5a601 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4856 | 2026-10-04 19:13:57 | e3099199 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4857 | 2026-10-04 19:27:54 | e3099199 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 55s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 73s [done] report expect='FACTORY' cmd=True \| T3 PASS 90s [d |
| 4858 | 2026-10-04 19:27:54 | e3099199 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 55s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 73s [done] report expect='FACTORY' cmd=True \| T3 PASS 90s [d |
| 4859 | 2026-10-04 19:27:54 | f1dca4c9 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "afb9f6f5ab6a418db3f5bd977c09026e", "after_quota": "e309919929564a969221c6f7bc8b5 |
| 4860 | 2026-10-04 19:27:54 | e3099199 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4861 | 2026-10-04 19:43:36 | 77064141 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4862 | 2026-10-04 19:43:36 | 506575ae |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-04T20"}} |
| 4863 | 2026-10-04 19:44:03 | 77064141 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "gr |
| 4864 | 2026-10-04 19:44:45 | 9522cede |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4865 | 2026-10-04 19:44:45 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4866 | 2026-10-04 19:44:45 | 8cc811ec |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-04T20"}} |
| 4867 | 2026-10-04 19:44:45 | 9522cede |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4868 | 2026-10-04 19:51:29 | 2e2fba20 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4869 | 2026-10-04 20:04:36 | 2e2fba20 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 74s [done] report expect='FACTORY' cmd=True \| T3 PASS 74s [do |
| 4870 | 2026-10-04 20:04:36 | 2e2fba20 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 74s [done] report expect='FACTORY' cmd=True \| T3 PASS 74s [do |
| 4871 | 2026-10-04 20:04:36 | 910bf161 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "07e26f32402644c6a7533696fca37040", "after_quota": "2e2fba20c7d84d278e0805565b5d5 |
| 4872 | 2026-10-04 20:04:36 | 2e2fba20 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4873 | 2026-10-04 20:18:36 | ef9271c4 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4874 | 2026-10-04 20:31:44 | ef9271c4 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 72s [done] report expect='FACTORY' cmd=True \| T3 PASS 75s [d |
| 4875 | 2026-10-04 20:31:44 | ef9271c4 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 72s [done] report expect='FACTORY' cmd=True \| T3 PASS 75s [d |
| 4876 | 2026-10-04 20:31:44 | 5d6673a0 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "8df68b4e54e54c76825de45193e93e05", "after_quota": "ef9271c4cd3e44c68818f2cee71ec |
| 4877 | 2026-10-04 20:31:44 | ef9271c4 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4878 | 2026-10-04 20:43:38 | 506575ae |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4879 | 2026-10-04 20:43:38 | 2db310a7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-04T21"}} |
| 4880 | 2026-10-04 20:43:39 | 20604f3a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4881 | 2026-10-04 20:43:55 | 506575ae |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 4882 | 2026-10-04 20:43:55 | f7bdefcb |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-04", "trigger": "blocked:gemini-flash36"}} |
| 4883 | 2026-10-04 20:43:55 | a7ebec03 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-04", "trigger": "blocked:gemini-flash36"}} |
| 4884 | 2026-10-04 20:43:55 | 8594c049 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-04", "trigger": "blocked:gemini-flash36"}} |
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
