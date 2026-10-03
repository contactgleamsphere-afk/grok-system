# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
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
| 4106 | 2026-10-02 21:47:30 | 85d83de6 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4107 | 2026-10-02 21:58:17 | 85d83de6 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 54s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 4108 | 2026-10-02 21:58:17 | 85d83de6 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 54s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 4109 | 2026-10-02 21:58:17 | 4916bbd0 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "7cee742138cd40ebaca15f9893987810", "after_quota": "85d83de62e774c46934395b898f1d |
| 4110 | 2026-10-02 21:58:17 | 85d83de6 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4111 | 2026-10-02 22:02:29 | d41885d1 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4112 | 2026-10-02 22:13:58 | d41885d1 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 79s [d |
| 4113 | 2026-10-02 22:13:58 | d41885d1 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 79s [d |
| 4114 | 2026-10-02 22:13:58 | c7c830da | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "f945f8750a8f4a44bbd14c6cad3f551f", "after_quota": "d41885d143a5418f8fd9b55d95e8c |
| 4115 | 2026-10-02 22:13:58 | d41885d1 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4116 | 2026-10-02 22:14:02 | 1e45bf31 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4117 | 2026-10-02 22:24:52 | 1e45bf31 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 29s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 51s [d |
| 4118 | 2026-10-02 22:24:52 | 1e45bf31 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 29s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 51s [d |
| 4119 | 2026-10-02 22:24:52 | bd9b738b | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fb0da05846d84df389ca213d3b687a2e", "after_quota": "1e45bf31be914a60a4d771fd5c924 |
| 4120 | 2026-10-02 22:24:52 | 1e45bf31 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4121 | 2026-10-02 22:24:52 | f8772d1e | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4122 | 2026-10-02 22:36:06 | f8772d1e | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 4123 | 2026-10-02 22:36:06 | f8772d1e | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 34s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 59s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 4124 | 2026-10-02 22:36:06 | 0c93124c | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "33bb3dfca7974c0fa99c4acf2c4af42d", "after_quota": "f8772d1ecebb486fbc7725d92e0e2 |
| 4125 | 2026-10-02 22:36:06 | f8772d1e | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4126 | 2026-10-02 22:36:06 | 716de28c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4127 | 2026-10-02 22:41:34 | caee5ec1 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4128 | 2026-10-02 22:41:35 | b3deef9b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-02T23"}} |
| 4129 | 2026-10-02 22:41:51 | caee5ec1 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 4130 | 2026-10-02 22:41:51 | e3962516 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-02", "trigger": "blocked:gemini-flash36"}} |
| 4131 | 2026-10-02 22:41:51 | 7d8ce118 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-02", "trigger": "blocked:gemini-flash36"}} |
| 4132 | 2026-10-02 22:41:51 | f9af908b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-02", "trigger": "blocked:gemini-flash36"}} |
| 4133 | 2026-10-02 22:41:51 | 65ecc914 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-02", "trigger": "blocked:gemini-flash36"}} |
| 4134 | 2026-10-02 22:41:51 | 7410941b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-02", "trigger": "blocked:gemini-flash36"}} |
| 4135 | 2026-10-02 22:41:51 | fbcfd1ff |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-02", "trigger": "blocked:gemini-flash36"}} |
| 4136 | 2026-10-02 22:41:51 | caee5ec1 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qw |
| 4137 | 2026-10-02 22:41:55 | e3962516 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4138 | 2026-10-02 22:41:55 | e3962516 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4139 | 2026-10-02 22:41:59 | 7d8ce118 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4140 | 2026-10-02 22:42:21 | 7d8ce118 |  | lane.rejected | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-2.5-flash", "reason": "probe gone: [{\n  \"error\": {\n    \"code\": 404,\n    \"message\": \"this model models/gemini-2.5 |
| 4141 | 2026-10-02 22:42:21 | 7d8ce118 |  | lane.discovered | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "reason": "probe 2.24s loop 3.8s", "provider": "gemini"} |
| 4142 | 2026-10-02 22:42:21 | 7d8ce118 |  | lane.rejected | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-2.5-flash-lite", "reason": "probe gone: [{\n  \"error\": {\n    \"code\": 404,\n    \"message\": \"this model models/gemin |
| 4143 | 2026-10-02 22:42:21 | 7d8ce118 |  | lane.rejected | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-3-flash-preview", "reason": "probe no_tool_call: ", "provider": "gemini"} |
| 4144 | 2026-10-02 22:42:21 | 7d8ce118 |  | lane.rejected | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-3.5-flash", "reason": "probe no_tool_call: ", "provider": "gemini"} |
| 4145 | 2026-10-02 22:42:21 | 7d8ce118 |  | config.presets | svc-LAPTOP-LRE6PSA8 | {"added": ["gemini-flash-latest"]} |
| 4146 | 2026-10-02 22:42:21 | d313c567 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"lanes": ["gemini-flash-latest"], "day": "2026-10-02"}} |
| 4147 | 2026-10-02 22:42:21 | 7d8ce118 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": ["gemini-flash-latest"]}} |
| 4148 | 2026-10-02 22:42:25 | ef59cb87 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4149 | 2026-10-02 22:42:25 | a292b979 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-02T23"}} |
| 4150 | 2026-10-02 22:42:25 | ef59cb87 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4151 | 2026-10-02 22:42:29 | f9af908b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4152 | 2026-10-02 22:42:51 | f9af908b |  | lane.discovered | svc-LAPTOP-LRE6PSA8 | {"model": "apodex/apodex-1.1-mini:free", "reason": "probe 2.05s loop 2.11s", "provider": "openrouter"} |
| 4153 | 2026-10-02 22:42:51 | f9af908b |  | lane.rejected | svc-LAPTOP-LRE6PSA8 | {"model": "dots-studio/dots-3-note-preview:free", "reason": "loop: final answer ''", "provider": "openrouter"} |
| 4154 | 2026-10-02 22:42:51 | f9af908b |  | lane.rejected | svc-LAPTOP-LRE6PSA8 | {"model": "liquid/lfm-2.5-2.6b:free", "reason": "loop: final answer ''", "provider": "openrouter"} |
| 4155 | 2026-10-02 22:42:51 | f9af908b |  | lane.rejected | svc-LAPTOP-LRE6PSA8 | {"model": "poolside/laguna-s-2.1:free", "reason": "loop: did not call add", "provider": "openrouter"} |
| 4156 | 2026-10-02 22:42:51 | f9af908b |  | lane.rejected | svc-LAPTOP-LRE6PSA8 | {"model": "thinkingmachines/inkling:free", "reason": "probe auth: {\"error\":{\"message\":\"thinkingmachines/inkling:free is only available  |
| 4157 | 2026-10-02 22:42:51 | f9af908b |  | config.presets | svc-LAPTOP-LRE6PSA8 | {"added": ["or-apodex-11-mini"]} |
| 4158 | 2026-10-02 22:42:51 | 6ae91506 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"lanes": ["or-apodex-11-mini"], "day": "2026-10-02"}} |
| 4159 | 2026-10-02 22:42:51 | f9af908b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": ["or-apodex-11-mini"]}} |
| 4160 | 2026-10-02 22:42:54 | 65ecc914 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4161 | 2026-10-02 22:42:54 | 65ecc914 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4162 | 2026-10-02 22:42:58 | 7410941b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4163 | 2026-10-02 22:42:58 | 7410941b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4164 | 2026-10-02 22:43:01 | fbcfd1ff |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4165 | 2026-10-02 22:43:01 | fbcfd1ff |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4166 | 2026-10-02 22:43:05 | d313c567 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4167 | 2026-10-02 22:44:19 | d313c567 |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "gemini-flash-latest", "result": "2/4", "quota": 0, "secs": 72} |
| 4168 | 2026-10-02 22:44:19 | d313c567 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["gemini-flash-latest", "2/4"]]}} |
| 4169 | 2026-10-02 22:44:22 | 6ae91506 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4170 | 2026-10-02 22:45:12 | 6ae91506 |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "or-apodex-11-mini", "result": "4/4", "quota": 0, "secs": 49} |
| 4171 | 2026-10-02 22:45:12 | 6ae91506 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["or-apodex-11-mini", "4/4"]]}} |
| 4172 | 2026-10-02 22:47:11 | 716de28c | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 54s [d |
| 4173 | 2026-10-02 22:47:11 | 716de28c | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 53s [done] report expect='FACTORY' cmd=True \| T3 PASS 54s [d |
| 4174 | 2026-10-02 22:47:11 | b2875558 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "07f6c614ba604417a7ba43b9713ba043", "after_quota": "716de28c53474324aecf5703c527a |
| 4175 | 2026-10-02 22:47:11 | 716de28c | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4176 | 2026-10-03 00:08:38 | b3deef9b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4177 | 2026-10-03 00:43:39 | a292b979 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4178 | 2026-10-03 00:43:41 | 92c073df |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T01"}} |
| 4179 | 2026-10-03 00:43:43 | db07cddc |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T01"}} |
| 4180 | 2026-10-03 00:43:43 | a292b979 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4181 | 2026-10-03 00:43:49 | b3deef9b |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 4182 | 2026-10-03 00:43:49 | b3deef9b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 4183 | 2026-10-03 00:43:49 | 92c073df |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 4184 | 2026-10-03 00:44:11 | b3deef9b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", |
| 4185 | 2026-10-03 00:44:15 | 6fd7ea7d | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4186 | 2026-10-03 00:44:27 | b3deef9b |  | job.orphaned_result | svc-LAPTOP-LRE6PSA8 | {"summary": "{'probed': 20, 'healthy': ['gemini-flash', 'gemini-flash-latest', 'gemini-gemini-flash-lite-latest', 'gemini-gemma26b', 'gemini |
| 4187 | 2026-10-03 00:55:51 | 6fd7ea7d | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 89s [done] report expect='FACTORY' cmd=True \| T3 PASS 56s [d |
| 4188 | 2026-10-03 00:55:51 | 6fd7ea7d | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 89s [done] report expect='FACTORY' cmd=True \| T3 PASS 56s [d |
| 4189 | 2026-10-03 00:55:51 | c15ff76e | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "bf07a48621114fc5917f1ae0b280ba93", "after_quota": "6fd7ea7d8f3045cb8c883229bb070 |
| 4190 | 2026-10-03 00:55:51 | 6fd7ea7d | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4191 | 2026-10-03 00:55:52 | 4916bbd0 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4192 | 2026-10-03 01:07:40 | 4916bbd0 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 49s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 4193 | 2026-10-03 01:07:40 | 4916bbd0 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 49s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 4194 | 2026-10-03 01:07:40 | 4916bbd0 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4195 | 2026-10-03 01:07:40 | d6015a6e | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "retry_of": "4916bbd0dcce4bda8fcbbb026cb5365 |
| 4196 | 2026-10-03 01:07:40 | 4916bbd0 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4197 | 2026-10-03 01:07:42 | c7c830da | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4198 | 2026-10-03 01:21:28 | c7c830da | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 57s [d |
| 4199 | 2026-10-03 01:21:28 | c7c830da | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 55s [done] report expect='FACTORY' cmd=True \| T3 PASS 57s [d |
| 4200 | 2026-10-03 01:21:28 | c7c830da | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4201 | 2026-10-03 01:21:28 | 57e0cf74 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "c7c830da9a544809953e4b06fa69351 |
| 4202 | 2026-10-03 01:21:28 | c7c830da | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4203 | 2026-10-03 01:21:29 | bd9b738b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4204 | 2026-10-03 01:34:05 | bd9b738b | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 50s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 4205 | 2026-10-03 01:34:05 | bd9b738b | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 50s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [d |
| 4206 | 2026-10-03 01:34:05 | cc6074e6 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fb0da05846d84df389ca213d3b687a2e", "after_quota": "bd9b738b8b3a405eb5f519a7afd84 |
| 4207 | 2026-10-03 01:34:05 | bd9b738b | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4208 | 2026-10-03 01:34:09 | 0c93124c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4209 | 2026-10-03 01:43:45 | 92c073df |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4210 | 2026-10-03 01:43:45 | 13e54a10 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T02"}} |
| 4211 | 2026-10-03 01:44:03 | 92c073df |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", |
| 4212 | 2026-10-03 01:44:07 | db07cddc |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4213 | 2026-10-03 01:44:07 | 1051fb63 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T02"}} |
| 4214 | 2026-10-03 01:44:07 | db07cddc |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4215 | 2026-10-03 01:45:31 | 99e5653e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4216 | 2026-10-03 01:45:32 | 99e5653e |  | audit.verified | svc-LAPTOP-LRE6PSA8 | {"rows": 4214, "hashed": 3462, "first_bad": null} |
| 4217 | 2026-10-03 01:45:32 | 091fe87e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-10-04"}} |
| 4218 | 2026-10-03 01:45:32 | f9f92dd0 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-10-03"}} |
| 4219 | 2026-10-03 01:45:32 | c7a3b266 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-10-03"}} |
| 4220 | 2026-10-03 01:45:32 | 076d0055 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-10-03"}} |
| 4221 | 2026-10-03 01:45:32 | 99e5653e |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4222 | 2026-10-03 01:45:36 | 076d0055 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4223 | 2026-10-03 01:45:36 | 8cbe2fa9 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "076d00557198429696acd4c0a35af210", "day": "2026-10-03"}} |
| 4224 | 2026-10-03 01:45:36 | 99f16adc | 029 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "029", "monitor_of": "076d00557198429696acd4c0a35af210", "day": "2026-10-03"}} |
| 4225 | 2026-10-03 01:45:36 | 076d0055 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "029"], "jobs": ["8cbe2fa9", "99f16adc"]} |
| 4226 | 2026-10-03 01:45:36 | 076d0055 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4227 | 2026-10-03 01:45:40 | 99f16adc | 029 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4228 | 2026-10-03 01:46:38 | 0c93124c | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 70s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 4229 | 2026-10-03 01:46:38 | 0c93124c | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 70s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 4230 | 2026-10-03 01:46:38 | f5bc1e3c | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "33bb3dfca7974c0fa99c4acf2c4af42d", "after_quota": "0c93124c972e46fe9fe6cd6ecc9d5 |
| 4231 | 2026-10-03 01:46:38 | 0c93124c | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4232 | 2026-10-03 01:46:41 | d6015a6e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4233 | 2026-10-03 01:46:59 | 99f16adc | 029 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] expect='X_OK' last='X_OK' \| T2 FAIL 35s [done] expect='3' last='\u00e2\u2020\u00b3 write bots.txt' \| T3 FAI |
| 4234 | 2026-10-03 01:46:59 | 99f16adc | 029 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] expect='X_OK' last='X_OK' \| T2 FAIL 35s [done] expect='3' last='\u00e2\u2020\u00b3 write bots.txt' \| T3 FAI |
| 4235 | 2026-10-03 01:46:59 | 99f16adc | 029 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4236 | 2026-10-03 01:46:59 | 70811e2d | 029 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "029", "max_rounds": 2}} |
| 4237 | 2026-10-03 01:46:59 | 99f16adc | 029 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "029", "status": "testing", "verified": "UNVERIFIED"}} |
| 4238 | 2026-10-03 01:47:04 | 70811e2d | 029 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4239 | 2026-10-03 02:00:15 | 70811e2d | 029 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": "3/4", "rejected": null}, {"round": |
| 4240 | 2026-10-03 02:00:15 | 70811e2d | 029 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 4241 | 2026-10-03 02:00:18 | f9f92dd0 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4242 | 2026-10-03 02:00:18 | f9f92dd0 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": []}} |
| 4243 | 2026-10-03 02:00:22 | c7a3b266 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4244 | 2026-10-03 02:00:54 | c7a3b266 |  | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "security", "next_state": "paused", "attempt": 1, "error": "FactoryError: could not produce a valid spec after 3 attempts: |
| 4245 | 2026-10-03 02:07:07 | d6015a6e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 17s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 112s [done] report expect='FACTORY' cmd=True \| T3 PASS 167s  |
| 4246 | 2026-10-03 02:07:07 | d6015a6e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 17s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 112s [done] report expect='FACTORY' cmd=True \| T3 PASS 167s  |
| 4247 | 2026-10-03 02:07:07 | a05c175f | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "d6015a6ea68f49a59de47c9add2b6bb6", "after_quota": "d6015a6ea68f49a59de47c9add2b6 |
| 4248 | 2026-10-03 02:07:07 | d6015a6e | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4249 | 2026-10-03 02:07:08 | 57e0cf74 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4250 | 2026-10-03 02:27:27 | 57e0cf74 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 66s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 132s [done] report expect='FACTORY' cmd=True \| T3 PASS 127s  |
| 4251 | 2026-10-03 02:27:27 | 57e0cf74 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 66s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 132s [done] report expect='FACTORY' cmd=True \| T3 PASS 127s  |
| 4252 | 2026-10-03 02:27:27 | c1e911a5 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "57e0cf7480894637b52c052c45b1dcea", "after_quota": "57e0cf7480894637b52c052c45b1d |
| 4253 | 2026-10-03 02:27:27 | 57e0cf74 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4254 | 2026-10-03 02:27:27 | b2875558 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4255 | 2026-10-03 02:43:48 | 13e54a10 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4256 | 2026-10-03 02:43:48 | 4c160338 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T03"}} |
| 4257 | 2026-10-03 02:44:06 | 13e54a10 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "ok", "before": "INFERRED", "after": "VERIFIED", "detail": null} |
| 4258 | 2026-10-03 02:44:06 | 13e54a10 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 4259 | 2026-10-03 02:44:06 | 13e54a10 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-gemma26b", "groq-gptoss120b", "groq-gptoss20b", "g |
| 4260 | 2026-10-03 02:44:11 | 1051fb63 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4261 | 2026-10-03 02:44:12 | 3a2547ff |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T03"}} |
| 4262 | 2026-10-03 02:44:12 | 1051fb63 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4263 | 2026-10-03 02:49:35 | b2875558 | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 4264 | 2026-10-03 02:49:37 | 8cbe2fa9 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4265 | 2026-10-03 03:11:44 | 8cbe2fa9 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 4266 | 2026-10-03 03:11:45 | b2875558 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 4267 | 2026-10-03 03:30:30 | 076d0055 |  | job.dedup | nightly-task | {"kind": "monitor", "note": "slot already done"} |
| 4268 | 2026-10-03 03:33:53 | b2875558 | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 4269 | 2026-10-03 03:33:57 | c15ff76e | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4270 | 2026-10-03 03:43:48 | 4c160338 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4271 | 2026-10-03 03:43:49 | 2d46a8c5 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T04"}} |
| 4272 | 2026-10-03 03:44:01 | 4c160338 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-gemma26b", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b" |
| 4273 | 2026-10-03 03:44:16 | 3a2547ff |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4274 | 2026-10-03 03:44:16 | f6f0d036 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T04"}} |
| 4275 | 2026-10-03 03:44:16 | 3a2547ff |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4276 | 2026-10-03 03:56:08 | c15ff76e | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
