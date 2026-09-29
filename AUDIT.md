# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
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
| 2977 | 2026-09-29 18:13:14 | 09146563 | 006 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2978 | 2026-09-29 18:14:25 | 09146563 | 006 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 FAIL 15s [done] expect='2' last='\u00e2\u2020\u00b3 write records.json' \| T3 |
| 2979 | 2026-09-29 18:14:25 | 09146563 | 006 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 FAIL 15s [done] expect='2' last='\u00e2\u2020\u00b3 write records.json' \| T3 |
| 2980 | 2026-09-29 18:14:25 | 09146563 | 006 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2981 | 2026-09-29 18:14:25 | 5def33a0 | 006 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "006", "max_rounds": 2}} |
| 2982 | 2026-09-29 18:14:25 | 09146563 | 006 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "006", "status": "testing", "verified": "UNVERIFIED"}} |
| 2983 | 2026-09-29 18:14:34 | 5def33a0 | 006 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2984 | 2026-09-29 18:15:47 | 5def33a0 | 006 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-120b", "sandbox": null, "rejected": ["fallback 'or-d |
| 2985 | 2026-09-29 18:15:47 | 5def33a0 | 006 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 2986 | 2026-09-29 18:15:52 | 0f19ad75 | 007 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2987 | 2026-09-29 18:16:51 | 579491c3 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 2988 | 2026-09-29 18:16:51 | 579491c3 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 2989 | 2026-09-29 18:16:51 | 579491c3 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2990 | 2026-09-29 18:16:51 | 061a0266 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "retry_of": "579491c38e0f4d489fb1f7874802eeb |
| 2991 | 2026-09-29 18:16:51 | 579491c3 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2992 | 2026-09-29 18:16:56 | 96e43656 | 008 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2993 | 2026-09-29 18:19:26 | 0f19ad75 | 007 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 34s [done] expect='X_OK' last='\u00e2\u2020\u00b3 read memory/history.jsonl' \| T2 PASS 42s [done] expect='2' last='2' \ |
| 2994 | 2026-09-29 18:19:26 | 0f19ad75 | 007 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 34s [done] expect='X_OK' last='\u00e2\u2020\u00b3 read memory/history.jsonl' \| T2 PASS 42s [done] expect='2' last='2' \ |
| 2995 | 2026-09-29 18:19:26 | 0f19ad75 | 007 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2996 | 2026-09-29 18:19:26 | 38b3cc11 | 007 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "007", "max_rounds": 2}} |
| 2997 | 2026-09-29 18:19:26 | 0f19ad75 | 007 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "status": "testing", "verified": "UNVERIFIED"}} |
| 2998 | 2026-09-29 18:19:33 | 38b3cc11 | 007 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2999 | 2026-09-29 18:20:29 | 96e43656 | 008 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] expect='X_OK' last='X_OK' \| T2 PASS 88s [done] expect='apple' last='RESULT: apple' \| T3 PASS 92s [done] exp |
| 3000 | 2026-09-29 18:20:29 | 96e43656 | 008 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] expect='X_OK' last='X_OK' \| T2 PASS 88s [done] expect='apple' last='RESULT: apple' \| T3 PASS 92s [done] exp |
| 3001 | 2026-09-29 18:20:29 | 96e43656 | 008 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "008", "status": "active", "verified": "VERIFIED"}} |
| 3002 | 2026-09-29 18:20:35 | 09ce9ce4 | 009 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3003 | 2026-09-29 18:23:08 | 38b3cc11 | 007 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 3004 | 2026-09-29 18:23:08 | 38b3cc11 | 007 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 3005 | 2026-09-29 18:23:08 | 38b3cc11 | 007 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "status": "active"}} |
| 3006 | 2026-09-29 18:23:13 | e6462e61 | 011 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3007 | 2026-09-29 18:25:48 | 09ce9ce4 | 009 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] expect='X_OK' last='X_OK' \| T2 PASS 87s [done] expect='3' last='RESULT: 3' \| T3 PASS 149s [done] expect='1' |
| 3008 | 2026-09-29 18:25:48 | 09ce9ce4 | 009 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] expect='X_OK' last='X_OK' \| T2 PASS 87s [done] expect='3' last='RESULT: 3' \| T3 PASS 149s [done] expect='1' |
| 3009 | 2026-09-29 18:25:49 | 09ce9ce4 | 009 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "009", "status": "active", "verified": "VERIFIED"}} |
| 3010 | 2026-09-29 18:26:06 | 8eec6c54 | 012 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3011 | 2026-09-29 18:26:16 | e6462e61 | 011 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] expect='X_OK' last='RESULT: X_OK' \| T2 PASS 54s [done] expect='2' last='2' \| T3 PASS 58s [done] expect='3'  |
| 3012 | 2026-09-29 18:26:16 | e6462e61 | 011 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] expect='X_OK' last='RESULT: X_OK' \| T2 PASS 54s [done] expect='2' last='2' \| T3 PASS 58s [done] expect='3'  |
| 3013 | 2026-09-29 18:26:16 | e6462e61 | 011 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "011", "status": "active", "verified": "VERIFIED"}} |
| 3014 | 2026-09-29 18:26:20 | 0969955b | 013 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3015 | 2026-09-29 18:28:37 | 8eec6c54 | 012 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='X_OK' \| T2 PASS 74s [done] expect='60' last='RESULT: Summed amount column to 60.' \| T3  |
| 3016 | 2026-09-29 18:28:37 | 8eec6c54 | 012 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='X_OK' \| T2 PASS 74s [done] expect='60' last='RESULT: Summed amount column to 60.' \| T3  |
| 3017 | 2026-09-29 18:28:37 | 8eec6c54 | 012 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "012", "status": "active", "verified": "VERIFIED"}} |
| 3018 | 2026-09-29 18:28:42 | 7ce257a8 | 014 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3019 | 2026-09-29 18:31:30 | 7ce257a8 | 014 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 83s [done] expect='5' last='RESULT: 5' \| T3 PASS 62s [done] expect='Time |
| 3020 | 2026-09-29 18:31:30 | 7ce257a8 | 014 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 83s [done] expect='5' last='RESULT: 5' \| T3 PASS 62s [done] expect='Time |
| 3021 | 2026-09-29 18:31:30 | 7ce257a8 | 014 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "014", "status": "active", "verified": "VERIFIED"}} |
| 3022 | 2026-09-29 18:31:35 | 598a5cc4 | 016 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3023 | 2026-09-29 18:31:49 | 0969955b | 013 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='X_OK' \| T2 PASS 190s [done] expect='1' last='1' \| T3 PASS 44s [done] expect='0' last='0 |
| 3024 | 2026-09-29 18:31:49 | 0969955b | 013 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='X_OK' \| T2 PASS 190s [done] expect='1' last='1' \| T3 PASS 44s [done] expect='0' last='0 |
| 3025 | 2026-09-29 18:31:49 | 0969955b | 013 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "013", "status": "active", "verified": "VERIFIED"}} |
| 3026 | 2026-09-29 18:31:52 | fd26f12c | 017 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3027 | 2026-09-29 18:32:38 | 598a5cc4 | 016 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 16s [done] expect='2' last='RESULT: 2' \| T3 PASS 22s [done] expect='3' l |
| 3028 | 2026-09-29 18:32:38 | 598a5cc4 | 016 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 16s [done] expect='2' last='RESULT: 2' \| T3 PASS 22s [done] expect='3' l |
| 3029 | 2026-09-29 18:32:38 | 598a5cc4 | 016 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "016", "status": "active", "verified": "VERIFIED"}} |
| 3030 | 2026-09-29 18:32:42 | 37ca8049 | 018 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3031 | 2026-09-29 18:33:40 | fd26f12c | 017 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 47s [done] expect='3' last='RESULT: 3' \| T3 PASS 38s [done] expect='3' l |
| 3032 | 2026-09-29 18:33:40 | fd26f12c | 017 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 47s [done] expect='3' last='RESULT: 3' \| T3 PASS 38s [done] expect='3' l |
| 3033 | 2026-09-29 18:33:40 | fd26f12c | 017 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "017", "status": "active", "verified": "VERIFIED"}} |
| 3034 | 2026-09-29 18:33:44 | f2bb4b62 | 019 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3035 | 2026-09-29 18:34:51 | f2bb4b62 | 019 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 28s [done] expect='1' last='RESULT: 1' \| T3 PASS 30s [done] expect='CONF |
| 3036 | 2026-09-29 18:34:51 | f2bb4b62 | 019 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 28s [done] expect='1' last='RESULT: 1' \| T3 PASS 30s [done] expect='CONF |
| 3037 | 2026-09-29 18:34:51 | f2bb4b62 | 019 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "019", "status": "active", "verified": "VERIFIED"}} |
| 3038 | 2026-09-29 18:34:55 | bb48c3f9 | 022 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3039 | 2026-09-29 18:35:19 | 37ca8049 | 018 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] expect='X_OK' last='X_OK' \| T2 PASS 37s [done] expect='30' last='RESULT: 30' \| T3 PASS 41s [done] expect='2 |
| 3040 | 2026-09-29 18:35:19 | 37ca8049 | 018 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 48s [done] expect='X_OK' last='X_OK' \| T2 PASS 37s [done] expect='30' last='RESULT: 30' \| T3 PASS 41s [done] expect='2 |
| 3041 | 2026-09-29 18:35:19 | 37ca8049 | 018 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "status": "active", "verified": "VERIFIED"}} |
| 3042 | 2026-09-29 18:35:22 | 6a59bbe3 | 023 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3043 | 2026-09-29 18:39:11 | bb48c3f9 | 022 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 121s [done] expect='2' last='RESULT: 2' \| T3 PASS 100s [done] expect='2' |
| 3044 | 2026-09-29 18:39:11 | bb48c3f9 | 022 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 121s [done] expect='2' last='RESULT: 2' \| T3 PASS 100s [done] expect='2' |
| 3045 | 2026-09-29 18:39:11 | bb48c3f9 | 022 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "022", "status": "active", "verified": "VERIFIED"}} |
| 3046 | 2026-09-29 18:39:15 | de0ebcc5 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3047 | 2026-09-29 18:39:26 | 6a59bbe3 | 023 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='RESULT: X_OK' \| T2 PASS 162s [done] expect='36.0' last='RESULT: 36.0' \| T3 FAIL 62s [don |
| 3048 | 2026-09-29 18:39:26 | 6a59bbe3 | 023 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='RESULT: X_OK' \| T2 PASS 162s [done] expect='36.0' last='RESULT: 36.0' \| T3 FAIL 62s [don |
| 3049 | 2026-09-29 18:39:26 | 6a59bbe3 | 023 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3050 | 2026-09-29 18:39:26 | 8615298f | 023 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "023", "max_rounds": 2}} |
| 3051 | 2026-09-29 18:39:26 | 6a59bbe3 | 023 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "023", "status": "testing", "verified": "UNVERIFIED"}} |
| 3052 | 2026-09-29 18:39:30 | 5929288f | 024 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3053 | 2026-09-29 18:40:03 | 5929288f | 024 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 8s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\024.json' \| T2 FAIL 12s [done] expect='2' las |
| 3054 | 2026-09-29 18:40:03 | 5929288f | 024 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 8s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\024.json' \| T2 FAIL 12s [done] expect='2' las |
| 3055 | 2026-09-29 18:40:03 | 9ddad2e1 | 024 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "024", "retest_of": "5929288ffa7f4d548094388c6e23f2f1", "after_quota": "5929288ffa7f4d548094388c6e23f |
| 3056 | 2026-09-29 18:40:03 | 5929288f | 024 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "024", "status": "active", "verified": "VERIFIED"}} |
| 3057 | 2026-09-29 18:40:07 | 65e0de3b | 025 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3058 | 2026-09-29 18:40:38 | 65e0de3b | 025 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 5s [done] expect='LIVENESS_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\025.json' \| T2 FAIL 13s [done] expect= |
| 3059 | 2026-09-29 18:40:38 | 65e0de3b | 025 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 5s [done] expect='LIVENESS_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\025.json' \| T2 FAIL 13s [done] expect= |
| 3060 | 2026-09-29 18:40:38 | 65e0de3b | 025 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3061 | 2026-09-29 18:40:38 | be8c781b | 025 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "025", "max_rounds": 2}} |
| 3062 | 2026-09-29 18:40:38 | 65e0de3b | 025 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "025", "status": "testing", "verified": "UNVERIFIED"}} |
| 3063 | 2026-09-29 18:40:43 | 30f205bc | 026 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3064 | 2026-09-29 18:42:16 | de0ebcc5 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [d |
| 3065 | 2026-09-29 18:42:16 | de0ebcc5 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [d |
| 3066 | 2026-09-29 18:42:16 | de0ebcc5 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3067 | 2026-09-29 18:42:16 | 764968eb | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "de0ebcc5c27f48e3bf57407fee7e657 |
| 3068 | 2026-09-29 18:42:16 | de0ebcc5 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3069 | 2026-09-29 18:42:20 | 23ec7b81 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3070 | 2026-09-29 18:42:30 | 30f205bc | 026 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 7s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\026.json' \| T2 FAIL 73s [done] expect='3' las |
| 3071 | 2026-09-29 18:42:30 | 30f205bc | 026 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 7s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\026.json' \| T2 FAIL 73s [done] expect='3' las |
| 3072 | 2026-09-29 18:42:30 | 30f205bc | 026 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3073 | 2026-09-29 18:42:30 | c3aed36d | 026 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "026", "max_rounds": 2}} |
| 3074 | 2026-09-29 18:42:30 | 30f205bc | 026 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "026", "status": "testing", "verified": "UNVERIFIED"}} |
| 3075 | 2026-09-29 18:42:33 | 4da83d39 | 027 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3076 | 2026-09-29 18:42:56 | 4da83d39 | 027 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 8s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\027.json' \| T2 PASS 12s [done] expect='2' las |
| 3077 | 2026-09-29 18:42:56 | 4da83d39 | 027 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 8s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\027.json' \| T2 PASS 12s [done] expect='2' las |
| 3078 | 2026-09-29 18:42:57 | 4da83d39 | 027 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3079 | 2026-09-29 18:42:57 | 8a77eba4 | 027 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "027", "max_rounds": 2}} |
| 3080 | 2026-09-29 18:42:57 | 4da83d39 | 027 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "027", "status": "testing", "verified": "UNVERIFIED"}} |
| 3081 | 2026-09-29 18:43:00 | 96c4c77a | 003 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3082 | 2026-09-29 18:43:29 | 96c4c77a | 003 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 8s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\003.json' \| T2 FAIL 9s [done] expect='3' last |
| 3083 | 2026-09-29 18:43:29 | 96c4c77a | 003 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 8s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\003.json' \| T2 FAIL 9s [done] expect='3' last |
| 3084 | 2026-09-29 18:43:29 | 96c4c77a | 003 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3085 | 2026-09-29 18:43:29 | 2ae8b6da | 003 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "003", "max_rounds": 2}} |
| 3086 | 2026-09-29 18:43:29 | 96c4c77a | 003 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "status": "testing", "verified": "UNVERIFIED"}} |
| 3087 | 2026-09-29 18:43:33 | e717ddc1 | 005 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3088 | 2026-09-29 18:45:27 | 23ec7b81 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [do |
| 3089 | 2026-09-29 18:45:27 | 23ec7b81 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 14s [do |
| 3090 | 2026-09-29 18:45:27 | 23ec7b81 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3091 | 2026-09-29 18:45:27 | ebcd50e4 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "23ec7b81970a48b0af75726582c5f75 |
| 3092 | 2026-09-29 18:45:27 | 23ec7b81 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3093 | 2026-09-29 18:45:30 | 8615298f | 023 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3094 | 2026-09-29 18:45:53 | e717ddc1 | 005 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 15s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\005.json' \| T2 FAIL 12s [done] expect='1' la |
| 3095 | 2026-09-29 18:45:53 | e717ddc1 | 005 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 15s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\005.json' \| T2 FAIL 12s [done] expect='1' la |
| 3096 | 2026-09-29 18:45:53 | e717ddc1 | 005 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3097 | 2026-09-29 18:45:53 | 9d53582f | 005 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "005", "max_rounds": 2}} |
| 3098 | 2026-09-29 18:45:53 | e717ddc1 | 005 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "005", "status": "testing", "verified": "UNVERIFIED"}} |
| 3099 | 2026-09-29 18:45:57 | cfc7b1fc | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3100 | 2026-09-29 18:46:07 | 8615298f | 023 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-120b", "sandbox": null, "rejected": ["fallback 'or-l |
| 3101 | 2026-09-29 18:46:07 | 8615298f | 023 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3102 | 2026-09-29 18:46:12 | be8c781b | 025 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3103 | 2026-09-29 18:46:43 | be8c781b | 025 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-120b", "sandbox": null, "rejected": ["fallback 'or-l |
| 3104 | 2026-09-29 18:46:44 | be8c781b | 025 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3105 | 2026-09-29 18:46:48 | c3aed36d | 026 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3106 | 2026-09-29 18:47:29 | c3aed36d | 026 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-ne |
| 3107 | 2026-09-29 18:47:29 | c3aed36d | 026 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3108 | 2026-09-29 18:47:33 | 8a77eba4 | 027 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3109 | 2026-09-29 18:48:22 | 8a77eba4 | 027 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 3110 | 2026-09-29 18:48:22 | 8a77eba4 | 027 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 3111 | 2026-09-29 18:48:22 | 8a77eba4 | 027 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "027", "status": "active"}} |
| 3112 | 2026-09-29 18:48:26 | 2ae8b6da | 003 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3113 | 2026-09-29 18:49:11 | cfc7b1fc | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 10s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [do |
| 3114 | 2026-09-29 18:49:11 | cfc7b1fc | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 10s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [do |
| 3115 | 2026-09-29 18:49:11 | cfc7b1fc | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3116 | 2026-09-29 18:49:11 | 252a5b8d | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "cfc7b1fcf2dc49f98b4dcfba530c0e9 |
| 3117 | 2026-09-29 18:49:11 | cfc7b1fc | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3118 | 2026-09-29 18:49:16 | 061a0266 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3119 | 2026-09-29 18:51:03 | 2ae8b6da | 003 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": "1/4", "rejected": null}, {"round": |
| 3120 | 2026-09-29 18:51:03 | 2ae8b6da | 003 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3121 | 2026-09-29 18:51:08 | 9d53582f | 005 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3122 | 2026-09-29 18:53:03 | 061a0266 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 21s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 3123 | 2026-09-29 18:53:03 | 061a0266 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 21s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 3124 | 2026-09-29 18:53:03 | 061a0266 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3125 | 2026-09-29 18:53:03 | a0577b9d | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "retry_of": "061a0266b60141249679d771b2f460a |
| 3126 | 2026-09-29 18:53:03 | 061a0266 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3127 | 2026-09-29 18:53:07 | 4d8b6f21 | 006 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3128 | 2026-09-29 18:57:11 | 9d53582f | 005 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-de |
| 3129 | 2026-09-29 18:57:11 | 9d53582f | 005 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3130 | 2026-09-29 18:57:15 | 3b04ee67 | 007 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3131 | 2026-09-29 19:02:12 | 4d8b6f21 | 006 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 75s [done] expect='X_OK' last='X_OK' \| T2 PASS 152s [done] expect='2' last='2' \| T3 PASS 231s [done] expect='0' last=' |
| 3132 | 2026-09-29 19:02:12 | 4d8b6f21 | 006 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 75s [done] expect='X_OK' last='X_OK' \| T2 PASS 152s [done] expect='2' last='2' \| T3 PASS 231s [done] expect='0' last=' |
| 3133 | 2026-09-29 19:02:12 | 4d8b6f21 | 006 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "006", "status": "active", "verified": "VERIFIED"}} |
| 3134 | 2026-09-29 19:02:18 | 4f6d66a5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3135 | 2026-09-29 19:02:18 | bddec4ba |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-29T20"}} |
| 3136 | 2026-09-29 19:03:35 | 4f6d66a5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 3137 | 2026-09-29 19:03:39 | 7f41dddc |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3138 | 2026-09-29 19:03:40 | 2d6263e3 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-29T20"}} |
| 3139 | 2026-09-29 19:03:40 | 7f41dddc |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3140 | 2026-09-29 19:03:44 | 2f8c68e5 | 008 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3141 | 2026-09-29 19:04:46 | 3b04ee67 | 007 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 47s [done] expect='X_OK' last='X_OK' \| T2 PASS 152s [done] expect='2' last='2' \| T3 PASS 147s [done] expect='0' last=' |
| 3142 | 2026-09-29 19:04:46 | 3b04ee67 | 007 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 47s [done] expect='X_OK' last='X_OK' \| T2 PASS 152s [done] expect='2' last='2' \| T3 PASS 147s [done] expect='0' last=' |
| 3143 | 2026-09-29 19:04:46 | 3b04ee67 | 007 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "status": "active", "verified": "VERIFIED"}} |
| 3144 | 2026-09-29 19:04:50 | 92b55be6 | 009 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3145 | 2026-09-29 19:07:06 | 92b55be6 | 009 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 48s [done] expect='3' last='RESULT: 3 unique lines' \| T3 PASS 57s [done] |
| 3146 | 2026-09-29 19:07:06 | 92b55be6 | 009 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 48s [done] expect='3' last='RESULT: 3 unique lines' \| T3 PASS 57s [done] |
| 3147 | 2026-09-29 19:07:06 | 92b55be6 | 009 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "009", "status": "active", "verified": "VERIFIED"}} |
| 3148 | 2026-09-29 19:07:10 | a0ca3faa | 011 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3149 | 2026-09-29 19:08:29 | a0ca3faa | 011 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 26s [done] expect='2' last='2' \| T3 PASS 28s [done] expect='3' last='3' |
| 3150 | 2026-09-29 19:08:29 | a0ca3faa | 011 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 26s [done] expect='2' last='2' \| T3 PASS 28s [done] expect='3' last='3' |
| 3151 | 2026-09-29 19:08:29 | a0ca3faa | 011 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "011", "status": "active", "verified": "VERIFIED"}} |
| 3152 | 2026-09-29 19:08:33 | 46a9742e | 012 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3153 | 2026-09-29 19:08:58 | 2f8c68e5 | 008 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 229s [done] expect='apple' last='apple' \| T3 PASS 60s [done] expect='dog |
| 3154 | 2026-09-29 19:08:58 | 2f8c68e5 | 008 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 229s [done] expect='apple' last='apple' \| T3 PASS 60s [done] expect='dog |
| 3155 | 2026-09-29 19:08:58 | 2f8c68e5 | 008 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "008", "status": "active", "verified": "VERIFIED"}} |
| 3156 | 2026-09-29 19:09:01 | c1be9289 | 013 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3157 | 2026-09-29 19:10:16 | 46a9742e | 012 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 21s [done] expect='60' last='60' \| T3 PASS 27s [done] expect='22' last=' |
| 3158 | 2026-09-29 19:10:16 | 46a9742e | 012 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 21s [done] expect='60' last='60' \| T3 PASS 27s [done] expect='22' last=' |
| 3159 | 2026-09-29 19:10:16 | 46a9742e | 012 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "012", "status": "active", "verified": "VERIFIED"}} |
| 3160 | 2026-09-29 19:10:20 | 3053504b | 014 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3161 | 2026-09-29 19:11:07 | c1be9289 | 013 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] expect='X_OK' last='X_OK' \| T2 PASS 36s [done] expect='1' last='RESULT: 1' \| T3 PASS 42s [done] expect='0'  |
| 3162 | 2026-09-29 19:11:07 | c1be9289 | 013 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] expect='X_OK' last='X_OK' \| T2 PASS 36s [done] expect='1' last='RESULT: 1' \| T3 PASS 42s [done] expect='0'  |
| 3163 | 2026-09-29 19:11:07 | c1be9289 | 013 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "013", "status": "active", "verified": "VERIFIED"}} |
| 3164 | 2026-09-29 19:11:10 | 9746e6aa | 016 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3165 | 2026-09-29 19:11:48 | 9746e6aa | 016 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 7s [done] expect='X_OK' last='X_OK' \| T2 PASS 12s [done] expect='2' last='RESULT: 2' \| T3 PASS 10s [done] expect='3' l |
| 3166 | 2026-09-29 19:11:48 | 9746e6aa | 016 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 7s [done] expect='X_OK' last='X_OK' \| T2 PASS 12s [done] expect='2' last='RESULT: 2' \| T3 PASS 10s [done] expect='3' l |
| 3167 | 2026-09-29 19:11:48 | 9746e6aa | 016 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "016", "status": "active", "verified": "VERIFIED"}} |
| 3168 | 2026-09-29 19:11:52 | 3053504b | 014 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 53s [done] expect='5' last='RESULT: 5' \| T3 PASS 17s [done] expect='Time |
| 3169 | 2026-09-29 19:11:52 | e70a2e86 | 017 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3170 | 2026-09-29 19:11:52 | 3053504b | 014 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 53s [done] expect='5' last='RESULT: 5' \| T3 PASS 17s [done] expect='Time |
| 3171 | 2026-09-29 19:11:52 | 3053504b | 014 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "014", "status": "active", "verified": "VERIFIED"}} |
| 3172 | 2026-09-29 19:11:57 | 38770f25 | 018 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3173 | 2026-09-29 19:13:58 | 38770f25 | 018 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] expect='X_OK' last='X_OK' \| T2 PASS 17s [done] expect='30' last='RESULT: 30' \| T3 PASS 49s [done] expect='2 |
| 3174 | 2026-09-29 19:13:58 | 38770f25 | 018 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] expect='X_OK' last='X_OK' \| T2 PASS 17s [done] expect='30' last='RESULT: 30' \| T3 PASS 49s [done] expect='2 |
| 3175 | 2026-09-29 19:13:58 | 38770f25 | 018 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "status": "active", "verified": "VERIFIED"}} |
| 3176 | 2026-09-29 19:14:03 | 764968eb | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3177 | 2026-09-29 19:14:04 | e70a2e86 | 017 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] expect='X_OK' last='X_OK' \| T2 PASS 58s [done] expect='3' last='RESULT: 3' \| T3 PASS 38s [done] expect='3'  |
| 3178 | 2026-09-29 19:14:04 | e70a2e86 | 017 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] expect='X_OK' last='X_OK' \| T2 PASS 58s [done] expect='3' last='RESULT: 3' \| T3 PASS 38s [done] expect='3'  |
| 3179 | 2026-09-29 19:14:04 | 46a02802 | 017 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "017", "retest_of": "e70a2e86354842e5bf3f27c193a033e0", "after_quota": "e70a2e86354842e5bf3f27c193a03 |
| 3180 | 2026-09-29 19:14:04 | e70a2e86 | 017 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "017", "status": "active", "verified": "VERIFIED"}} |
| 3181 | 2026-09-29 19:14:08 | 665ef041 | 019 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3182 | 2026-09-29 19:14:35 | 665ef041 | 019 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 4s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\019.json' \| T2 FAIL 11s [done] expect='1' las |
| 3183 | 2026-09-29 19:14:35 | 665ef041 | 019 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 4s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\019.json' \| T2 FAIL 11s [done] expect='1' las |
| 3184 | 2026-09-29 19:14:35 | 665ef041 | 019 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3185 | 2026-09-29 19:14:35 | 70dc72a1 | 019 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "019", "max_rounds": 2}} |
| 3186 | 2026-09-29 19:14:35 | 665ef041 | 019 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "019", "status": "testing", "verified": "UNVERIFIED"}} |
| 3187 | 2026-09-29 19:14:39 | 196465d0 | 022 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3188 | 2026-09-29 19:15:15 | 196465d0 | 022 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 5s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\022.json' \| T2 FAIL 8s [done] expect='2' last |
| 3189 | 2026-09-29 19:15:15 | 196465d0 | 022 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 5s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\022.json' \| T2 FAIL 8s [done] expect='2' last |
| 3190 | 2026-09-29 19:15:15 | 196465d0 | 022 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3191 | 2026-09-29 19:15:15 | ce9c717b | 022 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "022", "max_rounds": 2}} |
| 3192 | 2026-09-29 19:15:15 | 196465d0 | 022 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "022", "status": "testing", "verified": "UNVERIFIED"}} |
| 3193 | 2026-09-29 19:15:19 | 24eb3217 | 023 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3194 | 2026-09-29 19:17:00 | 764968eb | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [do |
| 3195 | 2026-09-29 19:17:00 | 764968eb | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [do |
| 3196 | 2026-09-29 19:17:00 | 764968eb | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3197 | 2026-09-29 19:17:00 | 73c0022b | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "764968eb7f4243efbded68bc80ab59c |
| 3198 | 2026-09-29 19:17:00 | 764968eb | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3199 | 2026-09-29 19:17:03 | ebcd50e4 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3200 | 2026-09-29 19:17:03 | 24eb3217 | 023 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 7s [done] expect='X_OK' last='X_OK' \| T2 PASS 51s [done] expect='36.0' last='RESULT: 36.0' \| T3 FAIL 34s [done] expect |
| 3201 | 2026-09-29 19:17:03 | 24eb3217 | 023 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 7s [done] expect='X_OK' last='X_OK' \| T2 PASS 51s [done] expect='36.0' last='RESULT: 36.0' \| T3 FAIL 34s [done] expect |
| 3202 | 2026-09-29 19:17:03 | 24eb3217 | 023 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3203 | 2026-09-29 19:17:03 | d229874c | 023 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "023", "max_rounds": 2}} |
| 3204 | 2026-09-29 19:17:03 | 24eb3217 | 023 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "023", "status": "testing", "verified": "UNVERIFIED"}} |
| 3205 | 2026-09-29 19:17:07 | 349839fb | 024 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3206 | 2026-09-29 19:17:42 | 349839fb | 024 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 4s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\024.json' \| T2 FAIL 11s [done] expect='2' las |
| 3207 | 2026-09-29 19:17:42 | 349839fb | 024 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 4s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\024.json' \| T2 FAIL 11s [done] expect='2' las |
| 3208 | 2026-09-29 19:17:42 | 349839fb | 024 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3209 | 2026-09-29 19:17:42 | 472caf57 | 024 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "024", "max_rounds": 2}} |
| 3210 | 2026-09-29 19:17:42 | 349839fb | 024 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "024", "status": "testing", "verified": "UNVERIFIED"}} |
| 3211 | 2026-09-29 19:17:46 | ff9a5304 | 025 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3212 | 2026-09-29 19:18:17 | ff9a5304 | 025 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] expect='LIVENESS_OK' last='LIVENESS_OK' \| T2 FAIL 4s [done] expect='HELLO WORLD' last='Using config: C:\\AI\ |
| 3213 | 2026-09-29 19:18:17 | ff9a5304 | 025 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 15s [done] expect='LIVENESS_OK' last='LIVENESS_OK' \| T2 FAIL 4s [done] expect='HELLO WORLD' last='Using config: C:\\AI\ |
| 3214 | 2026-09-29 19:18:17 | 0e05bf69 | 025 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "025", "retest_of": "ff9a530447274bf2ba7ea8a8c72da7f9", "after_quota": "ff9a530447274bf2ba7ea8a8c72da |
| 3215 | 2026-09-29 19:18:17 | ff9a5304 | 025 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "025", "status": "testing", "verified": "UNVERIFIED"}} |
| 3216 | 2026-09-29 19:18:20 | 8a363ecb | 026 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3217 | 2026-09-29 19:19:28 | 8a363ecb | 026 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 14s [done] expect='X_OK' last='with transport 'stdio'' \| T2 FAIL 10s [done] expect='3' last='with transport 'stdio'' \| |
| 3218 | 2026-09-29 19:19:28 | 8a363ecb | 026 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 14s [done] expect='X_OK' last='with transport 'stdio'' \| T2 FAIL 10s [done] expect='3' last='with transport 'stdio'' \| |
| 3219 | 2026-09-29 19:19:28 | 8a363ecb | 026 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3220 | 2026-09-29 19:19:28 | 0656e7cc | 026 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "026", "max_rounds": 2}} |
| 3221 | 2026-09-29 19:19:28 | 8a363ecb | 026 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "026", "status": "testing", "verified": "UNVERIFIED"}} |
| 3222 | 2026-09-29 19:19:31 | fbcc0040 | 027 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3223 | 2026-09-29 19:20:24 | fbcc0040 | 027 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 30s [done] expect='2' last='RESULT: 2' \| T3 FAIL 13s [done] expect='CONF |
| 3224 | 2026-09-29 19:20:24 | fbcc0040 | 027 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] expect='X_OK' last='X_OK' \| T2 PASS 30s [done] expect='2' last='RESULT: 2' \| T3 FAIL 13s [done] expect='CONF |
| 3225 | 2026-09-29 19:20:24 | b468005e | 027 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "027", "retest_of": "fbcc0040bd964286b6e51a21834b408d", "after_quota": "fbcc0040bd964286b6e51a21834b4 |
| 3226 | 2026-09-29 19:20:24 | fbcc0040 | 027 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "027", "status": "active", "verified": "VERIFIED"}} |
| 3227 | 2026-09-29 19:20:33 | ebcd50e4 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 19s [do |
| 3228 | 2026-09-29 19:20:33 | ebcd50e4 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 19s [do |
| 3229 | 2026-09-29 19:20:33 | ebcd50e4 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3230 | 2026-09-29 19:20:33 | 69f3367a | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "ebcd50e48e4a448e8e50057bd0f56b7 |
| 3231 | 2026-09-29 19:20:33 | ebcd50e4 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3232 | 2026-09-29 19:20:34 | 252a5b8d | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3233 | 2026-09-29 19:20:36 | 70dc72a1 | 019 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3234 | 2026-09-29 19:21:12 | 70dc72a1 | 019 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-li |
| 3235 | 2026-09-29 19:21:12 | 70dc72a1 | 019 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3236 | 2026-09-29 19:21:15 | ce9c717b | 022 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3237 | 2026-09-29 19:21:56 | ce9c717b | 022 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-li |
| 3238 | 2026-09-29 19:21:56 | ce9c717b | 022 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3239 | 2026-09-29 19:22:00 | d229874c | 023 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3240 | 2026-09-29 19:23:37 | d229874c | 023 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-li |
| 3241 | 2026-09-29 19:23:37 | d229874c | 023 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3242 | 2026-09-29 19:23:40 | 472caf57 | 024 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3243 | 2026-09-29 19:24:55 | 472caf57 | 024 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 3244 | 2026-09-29 19:24:55 | 472caf57 | 024 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 3245 | 2026-09-29 19:24:55 | 472caf57 | 024 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "024", "status": "active"}} |
| 3246 | 2026-09-29 19:24:59 | 0656e7cc | 026 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3247 | 2026-09-29 19:26:35 | 252a5b8d | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [do |
| 3248 | 2026-09-29 19:26:35 | 252a5b8d | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 13s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [do |
| 3249 | 2026-09-29 19:26:35 | 252a5b8d | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 3250 | 2026-09-29 19:26:35 | 176c95ca | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "252a5b8dab6d4dda9c57864ab31d7eb |
| 3251 | 2026-09-29 19:26:35 | 252a5b8d | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3252 | 2026-09-29 19:26:36 | 0656e7cc | 026 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": ["fallback 'or-ne |
| 3253 | 2026-09-29 19:26:36 | 0656e7cc | 026 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 3254 | 2026-09-29 19:26:39 | a0577b9d | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3255 | 2026-09-29 19:26:43 | dda50f35 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3256 | 2026-09-29 19:27:42 | dda50f35 |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "or-qwen27b", "result": "2/4", "quota": 0, "secs": 58} |
| 3257 | 2026-09-29 19:27:42 | dda50f35 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["or-qwen27b", "2/4"]]}} |
| 3258 | 2026-09-29 19:27:45 | 09024b3a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3259 | 2026-09-29 19:33:03 | 09024b3a |  | factory.canary | svc-LAPTOP-LRE6PSA8 | {"verdict": "FAIL", "lane": "gemini:gemini-3.1-flash-lite", "chain": ["gemini-lite31", "or-ling-30-flash-sante", "or-nemotron-35-lightning", |
| 3260 | 2026-09-29 19:33:03 | 09024b3a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"pass": 1, "total": 2}} |
| 3261 | 2026-09-29 19:37:25 | a0577b9d | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 62s [d |
| 3262 | 2026-09-29 19:37:25 | a0577b9d | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 52s [done] report expect='FACTORY' cmd=True \| T3 PASS 62s [d |
| 3263 | 2026-09-29 19:37:25 | edd55734 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a0577b9d22b54bf8ad00cd895bd0c6e7", "after_quota": "a0577b9d22b54bf8ad00cd895bd0c |
| 3264 | 2026-09-29 19:37:25 | a0577b9d | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3265 | 2026-09-29 19:47:00 | 73c0022b | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3266 | 2026-09-29 19:58:03 | 0d658a6f | 027 | job.enqueued | master-001 | {"kind": "run", "payload": {"bot_id": "027", "task": "read the code for bot 028 and tell me how it performs the weekly self-review", "in": " |
| 3267 | 2026-09-29 19:58:04 | 0d658a6f | 027 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3268 | 2026-09-29 19:58:35 | 73c0022b | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 3269 | 2026-09-29 19:58:35 | 73c0022b | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 61s [done] report expect='FACTORY' cmd=True \| T3 PASS 58s [d |
| 3270 | 2026-09-29 19:58:35 | 2c510b7c | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "73c0022bd5074aad890aa36856ac76d0", "after_quota": "73c0022bd5074aad890aa36856ac7 |
| 3271 | 2026-09-29 19:58:35 | 73c0022b | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 3272 | 2026-09-29 19:58:39 | 69f3367a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3273 | 2026-09-29 19:58:40 | 0d658a6f | 027 | bot.ran | svc-LAPTOP-LRE6PSA8 | {"ok": true, "produced": [], "secs": 35, "reply": "\u00e2\u2020\u00b3 read bots/bot028/README.md", "chain": "gemini-gemini-flash-lite-latest |
| 3274 | 2026-09-29 19:58:40 | 0d658a6f | 027 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "027", "name": "run", "status": "ok "}} |
| 3275 | 2026-09-29 20:02:19 | bddec4ba |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3276 | 2026-09-29 20:02:19 | 06281ead |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-29T21"}} |
| 3277 | 2026-09-29 20:05:14 | bddec4ba |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b", "local4b", "or-l |
| 3278 | 2026-09-29 20:05:18 | 2d6263e3 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3279 | 2026-09-29 20:05:19 | f4e79228 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-29T21"}} |
| 3280 | 2026-09-29 20:05:19 | 2d6263e3 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 3281 | 2026-09-29 20:10:52 | 9155875e | 028 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 3282 | 2026-09-29 20:11:25 | 69f3367a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 75s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 3283 | 2026-09-29 20:11:25 | 69f3367a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 31s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 75s [done] report expect='FACTORY' cmd=True \| T3 PASS 55s [d |
| 3284 | 2026-09-29 20:11:25 | 6629b411 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "69f3367abff946268d48a65cfce000ca", "after_quota": "69f3367abff946268d48a65cfce00 |
| 3285 | 2026-09-29 20:11:25 | 69f3367a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
