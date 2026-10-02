# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 3706 | 2026-09-30 22:09:29 | be7ecc01 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3707 | 2026-09-30 22:11:02 | c31e227e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 3708 | 2026-09-30 22:11:02 | c31e227e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 3709 | 2026-09-30 22:11:02 | 2a19c229 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "f2538a50d0d74959a9284ddf41fe13dc", "after_quota": "c31e227e1ed74d24aacafba16e54f |
| 3710 | 2026-09-30 22:11:02 | c31e227e | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3711 | 2026-09-30 22:11:04 | 64b571f1 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3712 | 2026-09-30 22:22:49 | 64b571f1 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 3713 | 2026-09-30 22:22:49 | 64b571f1 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 61s [d |
| 3714 | 2026-09-30 22:22:49 | af18c815 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "c86fde5b9f3249a696c69dd430ddd566", "after_quota": "64b571f140bc436d85f42463eb988 |
| 3715 | 2026-09-30 22:22:49 | 64b571f1 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3716 | 2026-09-30 22:22:52 | 68b9c7c1 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3717 | 2026-09-30 22:35:10 | 68b9c7c1 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 3718 | 2026-09-30 22:35:10 | 68b9c7c1 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 3719 | 2026-09-30 22:35:10 | 602a3fa3 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "348606642c1d455ca3fa0f011dcc1967", "after_quota": "68b9c7c1bb06497a95c6c9e3037bd |
| 3720 | 2026-09-30 22:35:10 | 68b9c7c1 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3721 | 2026-09-30 23:20:25 | 43cba625 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3722 | 2026-09-30 23:20:25 | f82f607a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3723 | 2026-09-30 23:20:25 | ad27fc01 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-01T00"}} |
| 3724 | 2026-09-30 23:20:36 | b762c8eb |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-01T00"}} |
| 3725 | 2026-09-30 23:20:36 | f82f607a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3726 | 2026-09-30 23:20:53 | 43cba625 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qw |
| 3727 | 2026-09-30 23:47:22 | 25892fff | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3728 | 2026-09-30 23:58:06 | 25892fff | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 57s [d |
| 3729 | 2026-09-30 23:58:06 | 25892fff | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 57s [d |
| 3730 | 2026-09-30 23:58:06 | 25892fff | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3731 | 2026-09-30 23:58:06 | e8540642 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "25892fff7f3944c7b52fe5ea6c1063e |
| 3732 | 2026-09-30 23:58:06 | 25892fff | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3733 | 2026-09-30 23:59:24 | 1446fcc7 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3734 | 2026-10-01 00:11:40 | 1446fcc7 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 97s [d |
| 3735 | 2026-10-01 00:11:40 | 1446fcc7 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 57s [done] report expect='FACTORY' cmd=True \| T3 PASS 97s [d |
| 3736 | 2026-10-01 00:11:40 | 5a64e9db | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "502b64cea6fb4ebb9b31ce8ee7c1cf06", "after_quota": "1446fcc75a234baf8e0fe6c668179 |
| 3737 | 2026-10-01 00:11:40 | 1446fcc7 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3738 | 2026-10-01 00:11:40 | 2a19c229 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3739 | 2026-10-01 00:20:29 | ad27fc01 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3740 | 2026-10-01 00:20:29 | 8caa5d96 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-01T01"}} |
| 3741 | 2026-10-01 00:20:38 | ad27fc01 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 3742 | 2026-10-01 00:20:38 | ad27fc01 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-gemma26b", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 500, |
| 3743 | 2026-10-01 00:20:38 | 703054e7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-01", "trigger": "blocked:gemini-flash36,gemini-gemma26b"}} |
| 3744 | 2026-10-01 00:20:38 | a2e2f56e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-01", "trigger": "blocked:gemini-flash36,gemini-gemma26b"}} |
| 3745 | 2026-10-01 00:20:38 | 898aad60 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-01", "trigger": "blocked:gemini-flash36,gemini-gemma26b"}} |
| 3746 | 2026-10-01 00:20:38 | bc7ae9ef |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-01", "trigger": "blocked:gemini-flash36,gemini-gemma26b"}} |
| 3747 | 2026-10-01 00:20:38 | ed026db8 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-01", "trigger": "blocked:gemini-flash36,gemini-gemma26b"}} |
| 3748 | 2026-10-01 00:20:38 | bfe4d02a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-01", "trigger": "blocked:gemini-flash36,gemini-gemma26b"}} |
| 3749 | 2026-10-01 00:20:38 | ad27fc01 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash38", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", "local4b"], "changed": [["gemini- |
| 3750 | 2026-10-01 00:20:41 | b762c8eb |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3751 | 2026-10-01 00:20:41 | 0017d5c7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-01T01"}} |
| 3752 | 2026-10-01 00:20:41 | b762c8eb |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3753 | 2026-10-01 00:20:44 | 703054e7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3754 | 2026-10-01 00:20:45 | 703054e7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 3755 | 2026-10-01 00:20:47 | a2e2f56e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3756 | 2026-10-01 00:20:48 | a2e2f56e |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 3757 | 2026-10-01 00:20:51 | 898aad60 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3758 | 2026-10-01 00:20:52 | 898aad60 |  | lane.rejected | svc-LAPTOP-LRE6PSA8 | {"model": "thinkingmachines/inkling-small:free", "reason": "probe auth: {\"error\":{\"message\":\"thinkingmachines/inkling-small:free is onl |
| 3759 | 2026-10-01 00:20:52 | 898aad60 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 3760 | 2026-10-01 00:20:55 | bc7ae9ef |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3761 | 2026-10-01 00:20:55 | bc7ae9ef |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3762 | 2026-10-01 00:20:58 | ed026db8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3763 | 2026-10-01 00:20:58 | ed026db8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3764 | 2026-10-01 00:21:01 | bfe4d02a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3765 | 2026-10-01 00:21:01 | bfe4d02a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3766 | 2026-10-01 00:22:59 | 2a19c229 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 3767 | 2026-10-01 00:22:59 | 2a19c229 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 33s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 58s [done] report expect='FACTORY' cmd=True \| T3 PASS 60s [d |
| 3768 | 2026-10-01 00:22:59 | d95c367c | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "f2538a50d0d74959a9284ddf41fe13dc", "after_quota": "2a19c229856b4472a6969e1653d8b |
| 3769 | 2026-10-01 00:22:59 | 2a19c229 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3770 | 2026-10-01 00:22:59 | af18c815 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3771 | 2026-10-01 00:41:02 | af18c815 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 106s [done] report expect='FACTORY' cmd=True \| T3 PASS 83s [ |
| 3772 | 2026-10-01 00:41:02 | af18c815 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 106s [done] report expect='FACTORY' cmd=True \| T3 PASS 83s [ |
| 3773 | 2026-10-01 00:41:02 | fd5ae898 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "c86fde5b9f3249a696c69dd430ddd566", "after_quota": "af18c815cf914d408e37524aef2e1 |
| 3774 | 2026-10-01 00:41:02 | af18c815 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3775 | 2026-10-01 00:41:03 | e8540642 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3776 | 2026-10-01 00:58:14 | e8540642 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 55s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 104s [done] report expect='FACTORY' cmd=True \| T3 PASS 102s  |
| 3777 | 2026-10-01 00:58:14 | e8540642 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 55s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 104s [done] report expect='FACTORY' cmd=True \| T3 PASS 102s  |
| 3778 | 2026-10-01 00:58:14 | d616c8ba | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "e85406426dc6462bbc1f93f46d2aa77e", "after_quota": "e85406426dc6462bbc1f93f46d2aa |
| 3779 | 2026-10-01 00:58:14 | e8540642 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3780 | 2026-10-01 00:58:17 | 602a3fa3 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3781 | 2026-10-01 01:14:01 | 602a3fa3 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 56s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 103s [done] report expect='FACTORY' cmd=True \| T3 PASS 92s [ |
| 3782 | 2026-10-01 01:14:01 | 602a3fa3 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 56s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 103s [done] report expect='FACTORY' cmd=True \| T3 PASS 92s [ |
| 3783 | 2026-10-01 01:14:01 | d6562839 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "348606642c1d455ca3fa0f011dcc1967", "after_quota": "602a3fa38413437eabb7b8d88e160 |
| 3784 | 2026-10-01 01:14:01 | 602a3fa3 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3785 | 2026-10-01 01:20:30 | 8caa5d96 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3786 | 2026-10-01 01:20:30 | 09b4b27c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-01T02"}} |
| 3787 | 2026-10-01 01:20:42 | 8caa5d96 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\n  |
| 3788 | 2026-10-01 01:20:42 | 8caa5d96 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 3789 | 2026-10-01 01:20:42 | f9ec6a4c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-01", "trigger": "blocked:gemini-flash"}} |
| 3790 | 2026-10-01 01:20:42 | f1a1a56c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-01", "trigger": "blocked:gemini-flash"}} |
| 3791 | 2026-10-01 01:20:42 | c9322d1d |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-01", "trigger": "blocked:gemini-flash"}} |
| 3792 | 2026-10-01 01:20:42 | fb7e15df |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-01", "trigger": "blocked:gemini-flash"}} |
| 3793 | 2026-10-01 01:20:42 | 064b8a49 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-01", "trigger": "blocked:gemini-flash"}} |
| 3794 | 2026-10-01 01:20:42 | 5a3049f7 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-01", "trigger": "blocked:gemini-flash"}} |
| 3795 | 2026-10-01 01:20:43 | 8caa5d96 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-flash38", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", "local4b", "or- |
| 3796 | 2026-10-01 01:20:44 | 0017d5c7 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3797 | 2026-10-01 01:20:44 | b863515d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-01T02"}} |
| 3798 | 2026-10-01 01:20:44 | 0017d5c7 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3799 | 2026-10-01 01:20:46 | f9ec6a4c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3800 | 2026-10-01 01:20:46 | f9ec6a4c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 3801 | 2026-10-01 01:20:49 | f1a1a56c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3802 | 2026-10-01 01:20:49 | f1a1a56c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3803 | 2026-10-01 01:20:53 | c9322d1d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3804 | 2026-10-01 01:20:53 | c9322d1d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3805 | 2026-10-01 01:20:56 | fb7e15df |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3806 | 2026-10-01 01:20:56 | fb7e15df |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3807 | 2026-10-01 01:21:01 | 064b8a49 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3808 | 2026-10-01 01:21:01 | 064b8a49 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3809 | 2026-10-01 01:21:04 | 5a3049f7 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3810 | 2026-10-01 01:21:04 | 5a3049f7 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 3811 | 2026-10-01 02:11:41 | 5a64e9db | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3812 | 2026-10-01 02:20:32 | 09b4b27c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3813 | 2026-10-01 02:20:32 | fe6c7aed |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-01T03"}} |
| 3814 | 2026-10-01 02:20:59 | 09b4b27c |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 3815 | 2026-10-01 02:21:00 | 09b4b27c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", "local4b", "or-li |
| 3816 | 2026-10-01 02:21:03 | b863515d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3817 | 2026-10-01 02:21:04 | 130008d4 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-01T03"}} |
| 3818 | 2026-10-01 02:21:04 | b863515d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3819 | 2026-10-01 02:26:36 | 5a64e9db | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 93s [done] report expect='FACTORY' cmd=True \| T3 PASS 79s [d |
| 3820 | 2026-10-01 02:26:36 | 5a64e9db | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 93s [done] report expect='FACTORY' cmd=True \| T3 PASS 79s [d |
| 3821 | 2026-10-01 02:26:36 | d12b9e5f | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "502b64cea6fb4ebb9b31ce8ee7c1cf06", "after_quota": "5a64e9db48564d98ae63254fa1da5 |
| 3822 | 2026-10-01 02:26:36 | 5a64e9db | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3823 | 2026-10-01 02:26:37 | d95c367c | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3824 | 2026-10-01 02:40:37 | d95c367c | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 94s [done] report expect='FACTORY' cmd=True \| T3 PASS 35s [d |
| 3825 | 2026-10-01 02:40:37 | d95c367c | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 94s [done] report expect='FACTORY' cmd=True \| T3 PASS 35s [d |
| 3826 | 2026-10-01 02:40:37 | 44159f49 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "f2538a50d0d74959a9284ddf41fe13dc", "after_quota": "d95c367c13a74737b7848bfa0ab8d |
| 3827 | 2026-10-01 02:40:37 | d95c367c | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3828 | 2026-10-01 02:41:05 | fd5ae898 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3829 | 2026-10-02 01:43:37 | fd5ae898 |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 3830 | 2026-10-02 01:43:37 | fe6c7aed |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3831 | 2026-10-02 01:43:42 | 6ddafcef |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-02T02"}} |
| 3832 | 2026-10-02 01:44:10 | fd5ae898 |  | job.readopted | svc-LAPTOP-LRE6PSA8 | {} |
| 3833 | 2026-10-02 01:44:25 | fe6c7aed |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-gemma26b", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 3834 | 2026-10-02 01:44:25 | fe6c7aed |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-l |
| 3835 | 2026-10-02 01:44:30 | 130008d4 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3836 | 2026-10-02 01:44:30 | 9662e40c | 018 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "run", "payload": {"bot_id": "018", "task": "Sum order totals per country into totals.csv", "in": "C:\\AI\\Factory\\workspace\\inbo |
| 3837 | 2026-10-02 01:44:30 |  | 018 | schedule.fired | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "fire": "2026-10-01T07:00", "job": "9662e40c"} |
| 3838 | 2026-10-02 01:44:33 | 59cf05fb |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-02T02"}} |
| 3839 | 2026-10-02 01:44:33 | 130008d4 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3840 | 2026-10-02 01:44:37 | 9662e40c | 018 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3841 | 2026-10-02 01:45:26 | 9662e40c | 018 | bot.ran | fast-LAPTOP-LRE6PSA8 | {"ok": true, "produced": ["totals.csv"], "secs": 41, "reply": "RESULT: success", "chain": "groq-gptoss120b"} |
| 3842 | 2026-10-02 01:45:26 | 9662e40c | 018 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "name": "run", "status": "ok totals.csv"}} |
| 3843 | 2026-10-02 01:45:30 | 1b7650d4 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3844 | 2026-10-02 01:45:31 | 1b7650d4 |  | audit.verified | fast-LAPTOP-LRE6PSA8 | {"rows": 3842, "hashed": 3090, "first_bad": null} |
| 3845 | 2026-10-02 01:45:31 | 99e5653e |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-10-03"}} |
| 3846 | 2026-10-02 01:45:31 | 0c3f5f27 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-10-02"}} |
| 3847 | 2026-10-02 01:45:31 | d712cbbe |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-10-02"}} |
| 3848 | 2026-10-02 01:45:31 | df14302d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-10-02"}} |
| 3849 | 2026-10-02 01:45:31 | 1b7650d4 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3850 | 2026-10-02 01:47:31 | fd5ae898 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 3851 | 2026-10-02 01:47:34 | d616c8ba | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3852 | 2026-10-02 01:47:35 | df14302d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3853 | 2026-10-02 01:47:35 | 4a92b32a | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3854 | 2026-10-02 01:47:35 | a6892e23 | 009 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "009", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3855 | 2026-10-02 01:47:35 | d8b0189e | 011 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "011", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3856 | 2026-10-02 01:47:35 | dd0512b5 | 012 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "012", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3857 | 2026-10-02 01:47:35 | 3338d776 | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "013", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3858 | 2026-10-02 01:47:35 | 1fbba810 | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "016", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3859 | 2026-10-02 01:47:35 | d2350314 | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "017", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3860 | 2026-10-02 01:47:35 | 9a381a38 | 018 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "018", "monitor_of": "df14302d7564425b9a49f64f7d268591", "day": "2026-10-02"}} |
| 3861 | 2026-10-02 01:47:35 | df14302d |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "009", "011", "012", "013", "016", "017", "018"], "jobs": ["4a92b32a", "a6892e23", "d8b0189e", "dd0512b5", "3338d776", "1fb |
| 3862 | 2026-10-02 01:47:35 | df14302d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3863 | 2026-10-02 01:47:38 | a6892e23 | 009 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3864 | 2026-10-02 14:43:45 |  |  | factory.outage | fast-LAPTOP-LRE6PSA8 | {"gap_min": 776, "silent_since": "2026-10-02T01:47:38", "last_event": "job.claimed", "cause": "power loss / battery flat (kernel-power 41)", |
| 3865 | 2026-10-02 14:43:45 |  |  | factory.outage | svc-LAPTOP-LRE6PSA8 | {"gap_min": 776, "silent_since": "2026-10-02T01:47:38", "last_event": "job.claimed", "cause": "power loss / battery flat (kernel-power 41)", |
| 3866 | 2026-10-02 14:43:45 | d616c8ba |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 3867 | 2026-10-02 14:43:45 | a6892e23 |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 3868 | 2026-10-02 14:43:45 | 6ddafcef |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3869 | 2026-10-02 14:43:45 | 22bc8b7b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-02T15"}} |
| 3870 | 2026-10-02 14:43:46 | 59cf05fb |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3871 | 2026-10-02 14:43:46 | ae821249 | 018 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "run", "payload": {"bot_id": "018", "task": "Sum order totals per country into totals.csv", "in": "C:\\AI\\Factory\\workspace\\inbo |
| 3872 | 2026-10-02 14:43:46 |  | 018 | schedule.fired | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "fire": "2026-10-02T07:00", "job": "ae821249"} |
| 3873 | 2026-10-02 14:43:51 | 845fc841 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-02T15"}} |
| 3874 | 2026-10-02 14:43:51 | 59cf05fb |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3875 | 2026-10-02 14:43:56 | fd5ae898 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 3876 | 2026-10-02 14:44:52 | 6ddafcef |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 3877 | 2026-10-02 14:44:56 | ae821249 | 018 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3878 | 2026-10-02 14:45:09 | ae821249 | 018 | bot.ran | svc-LAPTOP-LRE6PSA8 | {"ok": true, "produced": [], "secs": 12, "reply": "Using config: C:\\AI\\Factory\\run\\botcfg\\018-task.json", "chain": "groq-gptoss120b"} |
| 3879 | 2026-10-02 14:45:09 | ae821249 | 018 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "name": "run", "status": "ok "}} |
| 3880 | 2026-10-02 14:45:15 | a6892e23 | 009 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 3881 | 2026-10-02 14:46:14 | a6892e23 | 009 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 9s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\009.json' \| T2 FAIL 22s [done] expect='3' las |
| 3882 | 2026-10-02 14:46:14 | a6892e23 | 009 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 9s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\009.json' \| T2 FAIL 22s [done] expect='3' las |
| 3883 | 2026-10-02 14:46:14 | a6892e23 | 009 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3884 | 2026-10-02 14:46:14 | 81018e13 | 009 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "009", "max_rounds": 2}} |
| 3885 | 2026-10-02 14:46:14 | a6892e23 | 009 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "009", "status": "testing", "verified": "UNVERIFIED"}} |
| 3886 | 2026-10-02 14:46:18 | 81018e13 | 009 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3887 | 2026-10-02 14:48:06 | fd5ae898 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 17s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 21s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 3888 | 2026-10-02 14:48:06 | fd5ae898 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 17s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 21s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 3889 | 2026-10-02 14:48:06 | fd5ae898 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3890 | 2026-10-02 14:48:06 | 6ad0fa67 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "fd5ae89845f5488c87d7a76361ca95a |
| 3891 | 2026-10-02 14:48:06 | fd5ae898 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3892 | 2026-10-02 14:48:09 | d616c8ba | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 3893 | 2026-10-02 14:49:34 | 81018e13 | 009 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": "1/4", "rejected": null}, {"round": |
| 3894 | 2026-10-02 14:49:34 | 81018e13 | 009 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3895 | 2026-10-02 14:49:38 | d8b0189e | 011 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3896 | 2026-10-02 14:51:08 | d8b0189e | 011 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 8s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\011.json' \| T2 FAIL 13s [done] expect='2' las |
| 3897 | 2026-10-02 14:51:08 | d8b0189e | 011 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 8s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\011.json' \| T2 FAIL 13s [done] expect='2' las |
| 3898 | 2026-10-02 14:51:08 | d8b0189e | 011 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3899 | 2026-10-02 14:51:08 | 1f6c487d | 011 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "011", "max_rounds": 2}} |
| 3900 | 2026-10-02 14:51:08 | d8b0189e | 011 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "011", "status": "testing", "verified": "UNVERIFIED"}} |
| 3901 | 2026-10-02 14:51:12 | 1f6c487d | 011 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3902 | 2026-10-02 14:51:52 | d616c8ba | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 15s [done] report expect='FACTORY' cmd=True \| T3 PASS 15s [d |
| 3903 | 2026-10-02 14:51:52 | d616c8ba | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 15s [done] report expect='FACTORY' cmd=True \| T3 PASS 15s [d |
| 3904 | 2026-10-02 14:51:52 | d616c8ba | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3905 | 2026-10-02 14:51:52 | 65022efd | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "d616c8ba0758462cba0386d59c8ceb4 |
| 3906 | 2026-10-02 14:51:52 | d616c8ba | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3907 | 2026-10-02 14:51:56 | d6562839 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3908 | 2026-10-02 14:52:11 | 1f6c487d | 011 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-li |
| 3909 | 2026-10-02 14:52:11 | 1f6c487d | 011 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3910 | 2026-10-02 14:52:15 | dd0512b5 | 012 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3911 | 2026-10-02 14:52:59 | dd0512b5 | 012 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 7s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\012.json' \| T2 FAIL 13s [done] expect='60' la |
| 3912 | 2026-10-02 14:52:59 | dd0512b5 | 012 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 7s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\012.json' \| T2 FAIL 13s [done] expect='60' la |
| 3913 | 2026-10-02 14:52:59 | 3f10d64d | 012 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "012", "retest_of": "dd0512b53f4c4b75860363e7ccdc8b85", "after_quota": "dd0512b53f4c4b75860363e7ccdc8 |
| 3914 | 2026-10-02 14:52:59 | dd0512b5 | 012 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "012", "status": "active", "verified": "VERIFIED"}} |
| 3915 | 2026-10-02 14:53:02 | 3338d776 | 013 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3916 | 2026-10-02 14:54:39 | 3338d776 | 013 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 8s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\013.json' \| T2 FAIL 14s [done] expect='1' las |
| 3917 | 2026-10-02 14:54:39 | 3338d776 | 013 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 8s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\013.json' \| T2 FAIL 14s [done] expect='1' las |
| 3918 | 2026-10-02 14:54:39 | 3338d776 | 013 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3919 | 2026-10-02 14:54:39 | 03decd6e | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "013", "max_rounds": 2}} |
| 3920 | 2026-10-02 14:54:39 | 3338d776 | 013 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "013", "status": "testing", "verified": "UNVERIFIED"}} |
| 3921 | 2026-10-02 14:54:44 | 03decd6e | 013 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3922 | 2026-10-02 14:54:53 | d6562839 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 3923 | 2026-10-02 14:54:53 | d6562839 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 3924 | 2026-10-02 14:54:53 | d6562839 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3925 | 2026-10-02 14:54:53 | 8b5239a3 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "retry_of": "d656283932334030beddb64e25ca6a6 |
| 3926 | 2026-10-02 14:54:53 | d6562839 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3927 | 2026-10-02 14:54:56 | d12b9e5f | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3928 | 2026-10-02 14:55:21 | 03decd6e | 013 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-li |
| 3929 | 2026-10-02 14:55:21 | 03decd6e | 013 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3930 | 2026-10-02 14:55:25 | 1fbba810 | 016 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3931 | 2026-10-02 14:56:10 | 1fbba810 | 016 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 9s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\016.json' \| T2 PASS 18s [done] expect='2' las |
| 3932 | 2026-10-02 14:56:10 | 1fbba810 | 016 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 9s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\016.json' \| T2 PASS 18s [done] expect='2' las |
| 3933 | 2026-10-02 14:56:10 | 1fbba810 | 016 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3934 | 2026-10-02 14:56:10 | 1e82a590 | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "016", "max_rounds": 2}} |
| 3935 | 2026-10-02 14:56:10 | 1fbba810 | 016 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "016", "status": "testing", "verified": "UNVERIFIED"}} |
| 3936 | 2026-10-02 14:56:15 | 1e82a590 | 016 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3937 | 2026-10-02 14:56:50 | 1e82a590 | 016 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-ne |
| 3938 | 2026-10-02 14:56:50 | 1e82a590 | 016 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3939 | 2026-10-02 14:56:53 | d2350314 | 017 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3940 | 2026-10-02 14:58:12 | d2350314 | 017 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 10s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\017.json' \| T2 FAIL 16s [done] expect='3' la |
| 3941 | 2026-10-02 14:58:12 | d2350314 | 017 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 10s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\017.json' \| T2 FAIL 16s [done] expect='3' la |
| 3942 | 2026-10-02 14:58:12 | d2350314 | 017 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3943 | 2026-10-02 14:58:12 | 747aafa5 | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "017", "max_rounds": 2}} |
| 3944 | 2026-10-02 14:58:12 | d2350314 | 017 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "017", "status": "testing", "verified": "UNVERIFIED"}} |
| 3945 | 2026-10-02 14:58:16 | 747aafa5 | 017 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3946 | 2026-10-02 14:59:07 | d12b9e5f | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 17s [done] report expect='FACTORY' cmd=True \| T3 PASS 21s [d |
| 3947 | 2026-10-02 14:59:07 | d12b9e5f | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 17s [done] report expect='FACTORY' cmd=True \| T3 PASS 21s [d |
| 3948 | 2026-10-02 14:59:07 | d12b9e5f | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3949 | 2026-10-02 14:59:07 | 6fcb78cb | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "d12b9e5f468e4bbfbdbf71e6d015a13 |
| 3950 | 2026-10-02 14:59:07 | d12b9e5f | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3951 | 2026-10-02 14:59:10 | 44159f49 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3952 | 2026-10-02 14:59:27 | 747aafa5 | 017 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-li |
| 3953 | 2026-10-02 14:59:27 | 747aafa5 | 017 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3954 | 2026-10-02 14:59:31 | 9a381a38 | 018 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3955 | 2026-10-02 15:00:35 | 9a381a38 | 018 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 10s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\018.json' \| T2 FAIL 17s [done] expect='30' l |
| 3956 | 2026-10-02 15:00:35 | 9a381a38 | 018 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 10s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\018.json' \| T2 FAIL 17s [done] expect='30' l |
| 3957 | 2026-10-02 15:00:35 | 9a381a38 | 018 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3958 | 2026-10-02 15:00:35 | 44d08ade | 018 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "018", "max_rounds": 2}} |
| 3959 | 2026-10-02 15:00:35 | 9a381a38 | 018 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "status": "testing", "verified": "UNVERIFIED"}} |
| 3960 | 2026-10-02 15:00:40 | 44d08ade | 018 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3961 | 2026-10-02 15:01:47 | 44d08ade | 018 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-li |
| 3962 | 2026-10-02 15:01:47 | 44d08ade | 018 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3963 | 2026-10-02 15:01:51 | 0c3f5f27 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3964 | 2026-10-02 15:01:51 | 0c3f5f27 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": []}} |
| 3965 | 2026-10-02 15:01:54 | d712cbbe |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3966 | 2026-10-02 15:01:58 | d712cbbe |  | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "security", "next_state": "paused", "attempt": 1, "error": "FactoryError: could not produce a valid spec after 3 attempts: |
| 3967 | 2026-10-02 15:02:53 | 44159f49 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 17s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 3968 | 2026-10-02 15:02:53 | 44159f49 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 17s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 3969 | 2026-10-02 15:02:53 | 44159f49 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3970 | 2026-10-02 15:02:53 | 168cd1be | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "496e3afd58764673a6b80d4e1d7f4792", "retry_of": "44159f49741e4a7da03058eb28d580c |
| 3971 | 2026-10-02 15:02:53 | 44159f49 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3972 | 2026-10-02 15:02:57 | 4a92b32a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3973 | 2026-10-02 15:07:01 | 4a92b32a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 22s [done] report expect='FACTORY' cmd=True \| T3 PASS 22s [d |
| 3974 | 2026-10-02 15:07:01 | 4a92b32a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 22s [done] report expect='FACTORY' cmd=True \| T3 PASS 22s [d |
| 3975 | 2026-10-02 15:07:01 | 4a92b32a | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3976 | 2026-10-02 15:07:01 | bf07a486 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "4a92b32aacec4cb6be605b6099a6bc2 |
| 3977 | 2026-10-02 15:07:01 | 4a92b32a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3978 | 2026-10-02 15:18:07 | 6ad0fa67 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3979 | 2026-10-02 18:41:25 | 6ad0fa67 |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 3980 | 2026-10-02 18:41:26 | 22bc8b7b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3981 | 2026-10-02 18:41:29 | d9005eea |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-02T19"}} |
| 3982 | 2026-10-02 18:41:50 | 6ad0fa67 |  | job.readopted | svc-LAPTOP-LRE6PSA8 | {} |
| 3983 | 2026-10-02 18:42:12 | 22bc8b7b |  | model.retired | fast-LAPTOP-LRE6PSA8 | {"model": "or-ling-30-flash-fin", "reason": "gone: {\"error\":{\"message\":\"this model is unavailable for free. the paid version "} |
| 3984 | 2026-10-02 18:42:12 | 22bc8b7b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite |
| 3985 | 2026-10-02 18:42:16 | 845fc841 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3986 | 2026-10-02 18:42:16 | 019fdba2 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-02T19"}} |
| 3987 | 2026-10-02 18:42:16 | 845fc841 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3988 | 2026-10-02 18:42:19 | 3f10d64d | 012 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3989 | 2026-10-02 18:42:58 | 3f10d64d | 012 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] expect='X_OK' last='X_OK' \| T2 FAIL 2s [done] expect='60' last='' \| T3 PASS 12s [done] expect='22' last='RE |
| 3990 | 2026-10-02 18:42:58 | 3f10d64d | 012 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] expect='X_OK' last='X_OK' \| T2 FAIL 2s [done] expect='60' last='' \| T3 PASS 12s [done] expect='22' last='RE |
| 3991 | 2026-10-02 18:42:58 | 3f10d64d | 012 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3992 | 2026-10-02 18:42:58 | e141af82 | 012 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "012", "max_rounds": 2}} |
| 3993 | 2026-10-02 18:42:58 | 3f10d64d | 012 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "012", "status": "testing", "verified": "UNVERIFIED"}} |
| 3994 | 2026-10-02 18:44:10 | 6ad0fa67 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 3995 | 2026-10-02 18:44:12 | 65022efd | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3996 | 2026-10-02 18:44:13 | e141af82 | 012 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3997 | 2026-10-02 18:45:18 | e141af82 | 012 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-li |
| 3998 | 2026-10-02 18:45:18 | e141af82 | 012 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3999 | 2026-10-02 18:47:29 | 65022efd | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 24s [done] report expect='FACTORY' cmd=True \| T3 PASS 15s [d |
| 4000 | 2026-10-02 18:47:30 | 65022efd | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 24s [done] report expect='FACTORY' cmd=True \| T3 PASS 15s [d |
| 4001 | 2026-10-02 18:47:30 | 65022efd | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4002 | 2026-10-02 18:47:30 | cec4d6a5 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "65022efdd1a04697b7181d63ced43b2 |
| 4003 | 2026-10-02 18:47:30 | 65022efd | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4004 | 2026-10-02 18:47:31 | 6ad0fa67 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 4005 | 2026-10-02 18:50:14 | 7db59fbb |  | job.enqueued | master-001 | {"kind": "create", "payload": {"objective": "Update the weekly self-review report script so that it also counts how many bots were created"} |
| 4006 | 2026-10-02 18:50:54 | 6ad0fa67 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 17s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 4007 | 2026-10-02 18:50:54 | 6ad0fa67 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 17s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 4008 | 2026-10-02 18:50:54 | 6ad0fa67 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4009 | 2026-10-02 18:50:54 | afc7408b | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "6ad0fa674df944bca8162e03b5bff68 |
| 4010 | 2026-10-02 18:50:54 | 6ad0fa67 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4011 | 2026-10-02 18:50:58 | 8b5239a3 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4012 | 2026-10-02 18:50:58 | 7db59fbb |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4013 | 2026-10-02 18:51:01 | 7db59fbb | 029 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "bot-count-updater", "tools": ["read_file", "write_file"], "permissions": ["fs:read", "fs:write"], "chain": ["gemini-gemini-flash-l |
| 4014 | 2026-10-02 18:52:45 | 7db59fbb | 029 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 20s [done] expect='X_OK' last='+ FullyQualifiedErrorId : NativeCommandError' \| T2 FAIL 35s [done] expect='3' last='\u00 |
| 4015 | 2026-10-02 18:52:45 | 76599715 | 029 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "029", "retest_of": "7db59fbb462d480fb5f8c7f307ccf304"}} |
| 4016 | 2026-10-02 18:52:45 | 7db59fbb | 029 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "029", "name": "bot-count-updater", "pass": 0, "total": 4, "status": "testing", "verified": "UNVERIFIED"}} |
| 4017 | 2026-10-02 18:52:53 | 76599715 | 029 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4018 | 2026-10-02 18:54:23 | 76599715 | 029 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 22s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\029.json' \| T2 FAIL 30s [done] expect='3' la |
| 4019 | 2026-10-02 18:54:23 | a8bf91c0 | 029 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "029", "retest_of": "7db59fbb462d480fb5f8c7f307ccf304", "after_quota": "76599715a4514741a14cd68ae3a4b |
| 4020 | 2026-10-02 18:54:23 | 76599715 | 029 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "029", "status": "testing", "verified": "UNVERIFIED"}} |
| 4021 | 2026-10-02 18:55:28 | 8b5239a3 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 36s [done] report expect='FACTORY' cmd=True \| T3 PASS 27s [d |
| 4022 | 2026-10-02 18:55:28 | 8b5239a3 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 36s [done] report expect='FACTORY' cmd=True \| T3 PASS 27s [d |
| 4023 | 2026-10-02 18:55:28 | 8b5239a3 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4024 | 2026-10-02 18:55:28 | 7cee7421 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "retry_of": "8b5239a3a4c84faf98c67f01b67859b |
| 4025 | 2026-10-02 18:55:28 | 8b5239a3 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4026 | 2026-10-02 18:55:31 | 6fcb78cb | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4027 | 2026-10-02 18:58:56 | 6fcb78cb | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 4028 | 2026-10-02 18:58:56 | 6fcb78cb | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 25s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 4029 | 2026-10-02 18:58:56 | 6fcb78cb | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4030 | 2026-10-02 18:58:56 | f945f875 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "6fcb78cbe80d42d28acb33fca9619a0 |
| 4031 | 2026-10-02 18:58:56 | 6fcb78cb | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4032 | 2026-10-02 18:58:57 | 168cd1be | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4033 | 2026-10-02 19:03:02 | 168cd1be | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [do |
| 4034 | 2026-10-02 19:03:02 | 168cd1be | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [do |
| 4035 | 2026-10-02 19:03:02 | 168cd1be | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4036 | 2026-10-02 19:03:02 | fb0da058 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "496e3afd58764673a6b80d4e1d7f4792", "retry_of": "168cd1bea29f4d36a58adf0ea441fe5 |
| 4037 | 2026-10-02 19:03:02 | 168cd1be | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4038 | 2026-10-02 19:03:04 | bf07a486 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4039 | 2026-10-02 19:14:25 | bf07a486 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 45s [d |
| 4040 | 2026-10-02 19:14:25 | bf07a486 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 45s [d |
| 4041 | 2026-10-02 19:14:25 | 1a919ad7 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "bf07a48621114fc5917f1ae0b280ba93", "after_quota": "bf07a48621114fc5917f1ae0b280b |
| 4042 | 2026-10-02 19:14:25 | bf07a486 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4043 | 2026-10-02 19:17:32 | cec4d6a5 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4044 | 2026-10-02 19:26:49 | cec4d6a5 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 64s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 4045 | 2026-10-02 19:26:49 | cec4d6a5 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 64s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 4046 | 2026-10-02 19:26:49 | cec4d6a5 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4047 | 2026-10-02 19:26:49 | 33bb3dfc | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "cec4d6a558f547f59ec7b3574d66fff |
| 4048 | 2026-10-02 19:26:49 | cec4d6a5 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4049 | 2026-10-02 19:26:50 | afc7408b | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4050 | 2026-10-02 19:36:01 | afc7408b | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 4051 | 2026-10-02 19:36:01 | afc7408b | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 4052 | 2026-10-02 19:36:01 | afc7408b | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4053 | 2026-10-02 19:36:01 | 07f6c614 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "afc7408bc5ff46a2a6464f1c98cc6b4 |
| 4054 | 2026-10-02 19:36:01 | afc7408b | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4055 | 2026-10-02 19:36:05 | 7cee7421 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4056 | 2026-10-02 19:41:31 | d9005eea |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4057 | 2026-10-02 19:41:31 | f2351e2c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-02T20"}} |
| 4058 | 2026-10-02 19:42:04 | d9005eea |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq- |
| 4059 | 2026-10-02 19:42:18 | 019fdba2 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4060 | 2026-10-02 19:42:19 | def22afc |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-02T20"}} |
| 4061 | 2026-10-02 19:42:19 | 019fdba2 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4062 | 2026-10-02 19:47:29 | 7cee7421 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 51s [d |
| 4063 | 2026-10-02 19:47:29 | 7cee7421 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 51s [d |
| 4064 | 2026-10-02 19:47:29 | 85d83de6 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "7cee742138cd40ebaca15f9893987810", "after_quota": "7cee742138cd40ebaca15f9893987 |
| 4065 | 2026-10-02 19:47:29 | 7cee7421 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4066 | 2026-10-02 19:47:33 | f945f875 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4067 | 2026-10-02 20:02:27 | f945f875 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 80s [done] report expect='FACTORY' cmd=True \| T3 PASS 129s [ |
| 4068 | 2026-10-02 20:02:27 | f945f875 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 80s [done] report expect='FACTORY' cmd=True \| T3 PASS 129s [ |
| 4069 | 2026-10-02 20:02:27 | d41885d1 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "f945f8750a8f4a44bbd14c6cad3f551f", "after_quota": "f945f8750a8f4a44bbd14c6cad3f5 |
| 4070 | 2026-10-02 20:02:27 | f945f875 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4071 | 2026-10-02 20:02:30 | fb0da058 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4072 | 2026-10-02 20:13:19 | fb0da058 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 4073 | 2026-10-02 20:13:19 | fb0da058 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 56s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 4074 | 2026-10-02 20:13:19 | 1e45bf31 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fb0da05846d84df389ca213d3b687a2e", "after_quota": "fb0da05846d84df389ca213d3b687 |
| 4075 | 2026-10-02 20:13:19 | fb0da058 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4076 | 2026-10-02 20:13:21 | 33bb3dfc | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4077 | 2026-10-02 20:24:04 | 33bb3dfc | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 29s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 52s [d |
| 4078 | 2026-10-02 20:24:04 | 33bb3dfc | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 29s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 51s [done] report expect='FACTORY' cmd=True \| T3 PASS 52s [d |
| 4079 | 2026-10-02 20:24:04 | f8772d1e | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "33bb3dfca7974c0fa99c4acf2c4af42d", "after_quota": "33bb3dfca7974c0fa99c4acf2c4af |
| 4080 | 2026-10-02 20:24:04 | 33bb3dfc | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4081 | 2026-10-02 20:24:08 | 07f6c614 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4082 | 2026-10-02 20:34:53 | 07f6c614 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 51s [d |
| 4083 | 2026-10-02 20:34:53 | 07f6c614 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 30s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 51s [d |
| 4084 | 2026-10-02 20:34:53 | 716de28c | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "07f6c614ba604417a7ba43b9713ba043", "after_quota": "07f6c614ba604417a7ba43b9713ba |
| 4085 | 2026-10-02 20:34:53 | 07f6c614 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4086 | 2026-10-02 20:41:32 | f2351e2c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4087 | 2026-10-02 20:41:32 | 00d3b1f4 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-02T21"}} |
| 4088 | 2026-10-02 20:42:19 | def22afc |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4089 | 2026-10-02 20:42:20 | 01cf8bd0 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-02T21"}} |
| 4090 | 2026-10-02 20:42:20 | def22afc |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4091 | 2026-10-02 20:42:50 | f2351e2c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", "local4b", "or- |
| 4092 | 2026-10-02 20:54:24 | a8bf91c0 | 029 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4093 | 2026-10-02 20:55:11 | a8bf91c0 | 029 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] expect='X_OK' last='X_OK' \| T2 PASS 12s [done] expect='3' last='RESULT: 3' \| T3 PASS 13s [done] expect='0'  |
| 4094 | 2026-10-02 20:55:11 | a8bf91c0 | 029 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "029", "status": "active", "verified": "VERIFIED"}} |
| 4095 | 2026-10-02 21:14:29 | 1a919ad7 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4096 | 2026-10-02 21:25:04 | 1a919ad7 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 53s [do |
| 4097 | 2026-10-02 21:25:04 | 1a919ad7 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 53s [do |
| 4098 | 2026-10-02 21:25:04 | 6fd7ea7d | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "bf07a48621114fc5917f1ae0b280ba93", "after_quota": "1a919ad770c3465e9b14664b8a6cf |
| 4099 | 2026-10-02 21:25:04 | 1a919ad7 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4100 | 2026-10-02 21:41:33 | 00d3b1f4 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4101 | 2026-10-02 21:41:33 | caee5ec1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-02T22"}} |
| 4102 | 2026-10-02 21:42:21 | 01cf8bd0 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4103 | 2026-10-02 21:42:22 | ef59cb87 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-02T22"}} |
| 4104 | 2026-10-02 21:42:22 | 01cf8bd0 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4105 | 2026-10-02 21:42:25 | 00d3b1f4 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gp |
