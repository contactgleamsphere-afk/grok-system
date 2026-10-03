# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
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
| 4277 | 2026-10-03 03:56:12 | b2875558 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 4278 | 2026-10-03 04:18:21 | b2875558 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "failed", "attempt": 3, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 4279 | 2026-10-03 04:18:24 | c15ff76e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 4280 | 2026-10-03 04:34:11 | c15ff76e |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 4281 | 2026-10-03 04:34:11 | c15ff76e | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 4282 | 2026-10-03 11:12:30 | c15ff76e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 2745s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 21761s [done] report expect='FACTORY' cmd=True \| T3 PASS 7 |
| 4283 | 2026-10-03 11:12:30 | c15ff76e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 2745s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 21761s [done] report expect='FACTORY' cmd=True \| T3 PASS 7 |
| 4284 | 2026-10-03 11:12:30 | c15ff76e | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4285 | 2026-10-03 11:12:30 | 9f518f13 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "c15ff76ebc524466b5507eb13830118 |
| 4286 | 2026-10-03 11:12:30 | c15ff76e | 001 | job.orphaned_result | fast-LAPTOP-LRE6PSA8 | {"summary": "{'bot_id': '001', 'tests': \"T1 FAIL 2745s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 21761s [done] report expect=' |
| 4287 | 2026-10-03 11:12:35 | 2d46a8c5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4288 | 2026-10-03 11:12:35 | 6453139b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T12"}} |
| 4289 | 2026-10-03 11:12:58 | 2d46a8c5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemi |
| 4290 | 2026-10-03 11:13:02 | f6f0d036 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4291 | 2026-10-03 11:13:02 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4292 | 2026-10-03 11:13:03 | 80da9646 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T12"}} |
| 4293 | 2026-10-03 11:13:03 | f6f0d036 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4294 | 2026-10-03 11:14:09 | c15ff76e | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "failed", "attempt": 3, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 4295 | 2026-10-03 11:14:12 | cc6074e6 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4296 | 2026-10-03 11:16:57 | cc6074e6 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 10s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4297 | 2026-10-03 11:16:57 | cc6074e6 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 10s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4298 | 2026-10-03 11:16:57 | cc6074e6 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4299 | 2026-10-03 11:16:57 | df618110 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "496e3afd58764673a6b80d4e1d7f4792", "retry_of": "cc6074e60d46488e86d85488290b0b0 |
| 4300 | 2026-10-03 11:16:57 | cc6074e6 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4301 | 2026-10-03 11:16:57 | f5bc1e3c | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4302 | 2026-10-03 11:21:00 | f5bc1e3c | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4303 | 2026-10-03 11:21:00 | f5bc1e3c | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4304 | 2026-10-03 11:21:00 | f5bc1e3c | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4305 | 2026-10-03 11:21:00 | f074797d | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "f5bc1e3c866246e7aee83d2a0c15e74 |
| 4306 | 2026-10-03 11:21:00 | f5bc1e3c | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4307 | 2026-10-03 11:21:00 | a05c175f | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4308 | 2026-10-03 11:23:19 | 39387973 |  | job.enqueued | master-001 | {"kind": "create", "payload": {"objective": "Improve the factory weekly self-review to also count how many bots were created"}} |
| 4309 | 2026-10-03 11:23:23 | 39387973 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4310 | 2026-10-03 11:23:25 | 39387973 | 030 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "weekly-self-review-bot-counter", "tools": ["read_file", "write_file"], "permissions": ["fs:read", "fs:write"], "chain": ["gemini-g |
| 4311 | 2026-10-03 11:24:08 | a05c175f | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 9s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [don |
| 4312 | 2026-10-03 11:24:08 | a05c175f | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 9s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [don |
| 4313 | 2026-10-03 11:24:08 | a05c175f | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4314 | 2026-10-03 11:24:08 | 9e73e71a | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "retry_of": "a05c175fc0634f378acd04b68d4eba0 |
| 4315 | 2026-10-03 11:24:08 | a05c175f | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4316 | 2026-10-03 11:24:12 | c1e911a5 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4317 | 2026-10-03 11:24:22 | 39387973 | 030 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 34s [done] expect='X_OK' last='+ FullyQualifiedErrorId : NativeCommandError' \| T2 PASS 10s [done] expect='3' last='RESU |
| 4318 | 2026-10-03 11:24:22 | 965aa88d | 030 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "030", "retest_of": "39387973a2c6440bab2350d11badb420"}} |
| 4319 | 2026-10-03 11:24:22 | 39387973 | 030 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "030", "name": "weekly-self-review-bot-counter", "pass": 2, "total": 4, "status": "testing", "verified": "UNVERIFIED" |
| 4320 | 2026-10-03 11:24:25 | 965aa88d | 030 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4321 | 2026-10-03 11:24:54 | 965aa88d | 030 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 6s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\030.json' \| T2 PASS 10s [done] expect='3' las |
| 4322 | 2026-10-03 11:24:54 | adb5ff47 | 030 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "030", "max_rounds": 2, "rearchitected": false}} |
| 4323 | 2026-10-03 11:24:54 | 965aa88d | 030 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "030", "status": "testing", "verified": "UNVERIFIED"}} |
| 4324 | 2026-10-03 11:24:58 | adb5ff47 | 030 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4325 | 2026-10-03 11:27:56 | adb5ff47 | 030 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": "3/4", "rejected": null}, {"round": 1 |
| 4326 | 2026-10-03 11:27:56 | adb5ff47 | 030 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 4327 | 2026-10-03 11:27:56 | adb5ff47 | 030 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "030", "name": "weekly-self-review-bot-counter", "status": "active", "verified": "VERIFIED"}} |
| 4328 | 2026-10-03 11:28:04 | c1e911a5 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [do |
| 4329 | 2026-10-03 11:28:04 | c1e911a5 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [do |
| 4330 | 2026-10-03 11:28:04 | c1e911a5 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4331 | 2026-10-03 11:28:04 | 9928616b | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "c1e911a56f9940698af7ab87b8b880c |
| 4332 | 2026-10-03 11:28:04 | c1e911a5 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4333 | 2026-10-03 11:28:05 | 8cbe2fa9 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 4334 | 2026-10-03 11:31:03 | 8cbe2fa9 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [d |
| 4335 | 2026-10-03 11:31:03 | 8cbe2fa9 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [d |
| 4336 | 2026-10-03 11:31:03 | 8cbe2fa9 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4337 | 2026-10-03 11:31:03 | eaaf77a7 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "076d00557198429696acd4c0a35af210", "retry_of": "8cbe2fa9803a4814b654f9dbc286a1e |
| 4338 | 2026-10-03 11:31:03 | 8cbe2fa9 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4339 | 2026-10-03 11:42:32 | 9f518f13 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4340 | 2026-10-03 11:45:09 | 9f518f13 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [do |
| 4341 | 2026-10-03 11:45:09 | 9f518f13 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 11s [do |
| 4342 | 2026-10-03 11:45:09 | 9f518f13 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4343 | 2026-10-03 11:45:09 | 5b6778f7 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "9f518f13a3f6482aaf228b68728d841 |
| 4344 | 2026-10-03 11:45:09 | 9f518f13 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4345 | 2026-10-03 11:46:57 | df618110 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4346 | 2026-10-03 11:49:03 | df618110 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4347 | 2026-10-03 11:49:03 | df618110 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4348 | 2026-10-03 11:49:03 | df618110 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4349 | 2026-10-03 11:49:03 | ebeb00d9 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "496e3afd58764673a6b80d4e1d7f4792", "retry_of": "df61811016a34db78e4b85b73b227fe |
| 4350 | 2026-10-03 11:49:03 | df618110 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4351 | 2026-10-03 11:51:01 | f074797d | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4352 | 2026-10-03 11:53:51 | f074797d | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 10s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4353 | 2026-10-03 11:53:51 | f074797d | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 8s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 10s [done] report expect='FACTORY' cmd=True \| T3 PASS 10s [do |
| 4354 | 2026-10-03 11:53:51 | f074797d | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4355 | 2026-10-03 11:53:51 | aeb856dd | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "f074797d764444b98a6a3bf3940af76 |
| 4356 | 2026-10-03 11:53:51 | f074797d | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4357 | 2026-10-03 11:54:10 | 9e73e71a | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4358 | 2026-10-03 11:57:12 | 9e73e71a | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [d |
| 4359 | 2026-10-03 11:57:12 | 9e73e71a | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [d |
| 4360 | 2026-10-03 11:57:12 | 9e73e71a | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4361 | 2026-10-03 11:57:12 | 88b3f1c4 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "c6ebd328452848dd8bc03064b97b6ff1", "retry_of": "9e73e71a93864c7589728633d9edf63 |
| 4362 | 2026-10-03 11:57:12 | 9e73e71a | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4363 | 2026-10-03 11:58:06 | 9928616b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4364 | 2026-10-03 12:00:46 | 9928616b | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [do |
| 4365 | 2026-10-03 12:00:46 | 9928616b | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 11s [done] report expect='FACTORY' cmd=True \| T3 PASS 12s [do |
| 4366 | 2026-10-03 12:00:46 | 9928616b | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 4367 | 2026-10-03 12:00:46 | 52cdfc83 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "9928616b52a047a998e1548273d5744 |
| 4368 | 2026-10-03 12:00:46 | 9928616b | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4369 | 2026-10-03 12:01:03 | eaaf77a7 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4370 | 2026-10-03 12:09:44 | eaaf77a7 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 4371 | 2026-10-03 12:09:44 | eaaf77a7 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 12s [done] report expect='FACTORY' cmd=True \| T3 PASS 13s [d |
| 4372 | 2026-10-03 12:09:44 | 7791cfd1 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "eaaf77a7b4ff439c830c6b7949a76355", "after_quota": "eaaf77a7b4ff439c830c6b7949a76 |
| 4373 | 2026-10-03 12:09:44 | eaaf77a7 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4374 | 2026-10-03 12:12:36 | 6453139b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4375 | 2026-10-03 12:12:36 | 70c181a5 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T13"}} |
| 4376 | 2026-10-03 12:12:57 | 6453139b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "gr |
| 4377 | 2026-10-03 12:13:06 | 80da9646 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4378 | 2026-10-03 12:13:06 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4379 | 2026-10-03 12:13:07 | e7478817 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T13"}} |
| 4380 | 2026-10-03 12:13:07 | 80da9646 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4381 | 2026-10-03 12:15:11 | 5b6778f7 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4382 | 2026-10-03 12:28:31 | 5b6778f7 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [do |
| 4383 | 2026-10-03 12:28:31 | 5b6778f7 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 60s [done] report expect='FACTORY' cmd=True \| T3 PASS 89s [do |
| 4384 | 2026-10-03 12:28:31 | f4c035f5 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5b6778f745304b77970b63b5b66bcf37", "after_quota": "5b6778f745304b77970b63b5b66bc |
| 4385 | 2026-10-03 12:28:31 | 5b6778f7 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4386 | 2026-10-03 12:28:34 | ebeb00d9 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4387 | 2026-10-03 12:41:01 | ebeb00d9 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 4388 | 2026-10-03 12:41:01 | ebeb00d9 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 71s [d |
| 4389 | 2026-10-03 12:41:01 | b2987a9a | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ebeb00d9ad6a4a4b8186056ccf5c3196", "after_quota": "ebeb00d9ad6a4a4b8186056ccf5c3 |
| 4390 | 2026-10-03 12:41:01 | ebeb00d9 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4391 | 2026-10-03 12:41:05 | aeb856dd | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4392 | 2026-10-03 12:53:32 | aeb856dd | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 41s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 4393 | 2026-10-03 12:53:32 | aeb856dd | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 41s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 4394 | 2026-10-03 12:53:32 | 91683a5e | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "aeb856dd164049c2891f58c9d8248e0f", "after_quota": "aeb856dd164049c2891f58c9d8248 |
| 4395 | 2026-10-03 12:53:32 | aeb856dd | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4396 | 2026-10-03 12:53:36 | 88b3f1c4 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4397 | 2026-10-03 13:06:46 | 88b3f1c4 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4398 | 2026-10-03 13:06:46 | 88b3f1c4 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4399 | 2026-10-03 13:06:46 | 4014c5d9 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "88b3f1c4827a4f3e95248a3f8017f9fc", "after_quota": "88b3f1c4827a4f3e95248a3f8017f |
| 4400 | 2026-10-03 13:06:46 | 88b3f1c4 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4401 | 2026-10-03 13:06:47 | 52cdfc83 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4402 | 2026-10-03 13:12:41 | 70c181a5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4403 | 2026-10-03 13:12:41 | 30d2a0d2 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T14"}} |
| 4404 | 2026-10-03 13:13:08 | 70c181a5 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 4405 | 2026-10-03 13:13:08 | 090b5ee6 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4406 | 2026-10-03 13:13:08 | 8583a832 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4407 | 2026-10-03 13:13:08 | fa27c6c8 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4408 | 2026-10-03 13:13:08 | f9702150 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4409 | 2026-10-03 13:13:08 | 74d04bfc |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4410 | 2026-10-03 13:13:08 | 7a60f27a |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4411 | 2026-10-03 13:13:08 | 70c181a5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "gr |
| 4412 | 2026-10-03 13:13:12 | e7478817 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4413 | 2026-10-03 13:13:12 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4414 | 2026-10-03 13:13:13 | 47e72b7d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T14"}} |
| 4415 | 2026-10-03 13:13:13 | e7478817 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4416 | 2026-10-03 13:13:17 | 090b5ee6 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4417 | 2026-10-03 13:13:18 | 090b5ee6 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4418 | 2026-10-03 13:13:22 | 8583a832 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4419 | 2026-10-03 13:13:23 | 8583a832 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4420 | 2026-10-03 13:13:27 | fa27c6c8 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4421 | 2026-10-03 13:13:30 | fa27c6c8 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4422 | 2026-10-03 13:13:35 | f9702150 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4423 | 2026-10-03 13:13:35 | f9702150 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4424 | 2026-10-03 13:13:39 | 74d04bfc |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4425 | 2026-10-03 13:13:39 | 74d04bfc |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4426 | 2026-10-03 13:13:43 | 7a60f27a |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4427 | 2026-10-03 13:13:43 | 7a60f27a |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4428 | 2026-10-03 13:20:04 | 52cdfc83 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4429 | 2026-10-03 13:20:04 | 52cdfc83 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 41s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4430 | 2026-10-03 13:20:04 | c4ba12f8 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "52cdfc8326cb4d02890da99fe7ba0b4c", "after_quota": "52cdfc8326cb4d02890da99fe7ba0 |
| 4431 | 2026-10-03 13:20:04 | 52cdfc83 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4432 | 2026-10-03 14:09:46 | 7791cfd1 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4433 | 2026-10-03 14:12:42 | 30d2a0d2 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4434 | 2026-10-03 14:12:42 | ae553c47 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T15"}} |
| 4435 | 2026-10-03 14:13:08 | 30d2a0d2 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 4436 | 2026-10-03 14:13:08 | 30d2a0d2 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gp |
| 4437 | 2026-10-03 14:13:18 | 47e72b7d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4438 | 2026-10-03 14:13:18 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4439 | 2026-10-03 14:13:19 | 6b090e08 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T15"}} |
| 4440 | 2026-10-03 14:13:19 | 47e72b7d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4441 | 2026-10-03 14:22:51 | 7791cfd1 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 75s [done] report expect='FACTORY' cmd=True \| T3 PASS 73s [d |
| 4442 | 2026-10-03 14:22:51 | 7791cfd1 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 75s [done] report expect='FACTORY' cmd=True \| T3 PASS 73s [d |
| 4443 | 2026-10-03 14:22:51 | 1811ab9e | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "eaaf77a7b4ff439c830c6b7949a76355", "after_quota": "7791cfd117e5456da042251bfa430 |
| 4444 | 2026-10-03 14:22:51 | 7791cfd1 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4445 | 2026-10-03 16:10:49 | ae553c47 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4446 | 2026-10-03 16:10:50 | 6b090e08 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4447 | 2026-10-03 16:10:51 | c9049357 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T17"}} |
| 4448 | 2026-10-03 16:10:51 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4449 | 2026-10-03 16:10:58 | 9b82e36b |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T17"}} |
| 4450 | 2026-10-03 16:10:58 | 6b090e08 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4451 | 2026-10-03 16:11:03 | f4c035f5 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4452 | 2026-10-03 16:11:40 | ae553c47 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemi |
| 4453 | 2026-10-03 16:23:50 | f4c035f5 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 94s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 4454 | 2026-10-03 16:23:50 | f4c035f5 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 10s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 94s [done] report expect='FACTORY' cmd=True \| T3 PASS 69s [d |
| 4455 | 2026-10-03 16:23:50 | 9bce9ff8 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5b6778f745304b77970b63b5b66bcf37", "after_quota": "f4c035f524374f2b8d335e9cc62c8 |
| 4456 | 2026-10-03 16:23:50 | f4c035f5 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4457 | 2026-10-03 16:23:54 | b2987a9a | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4458 | 2026-10-03 16:36:26 | b2987a9a | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4459 | 2026-10-03 16:36:26 | b2987a9a | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 36s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4460 | 2026-10-03 16:36:26 | ca238808 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ebeb00d9ad6a4a4b8186056ccf5c3196", "after_quota": "b2987a9ab34c4f9b943c555412d7a |
| 4461 | 2026-10-03 16:36:26 | b2987a9a | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4462 | 2026-10-03 16:36:30 | 91683a5e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4463 | 2026-10-03 16:48:57 | 91683a5e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 4464 | 2026-10-03 16:48:57 | 91683a5e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 66s [d |
| 4465 | 2026-10-03 16:48:57 | 70406b7d | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "aeb856dd164049c2891f58c9d8248e0f", "after_quota": "91683a5e976743ad81af9e3b1b693 |
| 4466 | 2026-10-03 16:48:57 | 91683a5e | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4467 | 2026-10-03 16:49:00 | 4014c5d9 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4468 | 2026-10-03 17:01:37 | 4014c5d9 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4469 | 2026-10-03 17:01:37 | 4014c5d9 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 35s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 66s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4470 | 2026-10-03 17:01:37 | 28936172 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "88b3f1c4827a4f3e95248a3f8017f9fc", "after_quota": "4014c5d9abc54ea0bc24da7d99b45 |
| 4471 | 2026-10-03 17:01:37 | 4014c5d9 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4472 | 2026-10-03 17:01:40 | c4ba12f8 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4473 | 2026-10-03 17:10:52 | c9049357 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4474 | 2026-10-03 17:10:52 | b160cb81 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T18"}} |
| 4475 | 2026-10-03 17:11:18 | c9049357 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 4476 | 2026-10-03 17:11:18 | 34937a4e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4477 | 2026-10-03 17:11:18 | 4feb3742 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4478 | 2026-10-03 17:11:18 | 33306e02 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4479 | 2026-10-03 17:11:18 | 3a5ef1c6 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4480 | 2026-10-03 17:11:18 | e38dbc3f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4481 | 2026-10-03 17:11:18 | dfffb806 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4482 | 2026-10-03 17:11:18 | c9049357 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qw |
| 4483 | 2026-10-03 17:11:22 | 9b82e36b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4484 | 2026-10-03 17:11:22 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4485 | 2026-10-03 17:11:22 | 7c4c7496 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T18"}} |
| 4486 | 2026-10-03 17:11:22 | 9b82e36b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4487 | 2026-10-03 17:11:25 | 34937a4e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4488 | 2026-10-03 17:11:25 | 34937a4e |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4489 | 2026-10-03 17:11:29 | 4feb3742 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4490 | 2026-10-03 17:11:29 | 4feb3742 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4491 | 2026-10-03 17:11:33 | 33306e02 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4492 | 2026-10-03 17:11:33 | 33306e02 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4493 | 2026-10-03 17:11:36 | 3a5ef1c6 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4494 | 2026-10-03 17:11:36 | 3a5ef1c6 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4495 | 2026-10-03 17:11:39 | e38dbc3f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4496 | 2026-10-03 17:11:39 | e38dbc3f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4497 | 2026-10-03 17:11:42 | dfffb806 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4498 | 2026-10-03 17:11:42 | dfffb806 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 4499 | 2026-10-03 17:13:58 | c4ba12f8 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 4500 | 2026-10-03 17:13:58 | c4ba12f8 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 71s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 4501 | 2026-10-03 17:13:58 | bdd006b0 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "52cdfc8326cb4d02890da99fe7ba0b4c", "after_quota": "c4ba12f8869b4bc7b98cb6549eccb |
| 4502 | 2026-10-03 17:13:58 | c4ba12f8 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4503 | 2026-10-03 17:14:01 | 1811ab9e | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4504 | 2026-10-03 17:26:56 | 1811ab9e | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4505 | 2026-10-03 17:26:56 | 1811ab9e | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 69s [done] report expect='FACTORY' cmd=True \| T3 PASS 72s [d |
| 4506 | 2026-10-03 17:26:56 | 0013387b | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "eaaf77a7b4ff439c830c6b7949a76355", "after_quota": "1811ab9ef1394a738ac0b9d34fe47 |
| 4507 | 2026-10-03 17:26:56 | 1811ab9e | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4508 | 2026-10-03 18:10:53 | b160cb81 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4509 | 2026-10-03 18:10:53 | 3e606ba8 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T19"}} |
| 4510 | 2026-10-03 18:11:27 | 7c4c7496 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4511 | 2026-10-03 18:11:27 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4512 | 2026-10-03 18:11:27 | f5fee259 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T19"}} |
| 4513 | 2026-10-03 18:11:27 | 7c4c7496 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4514 | 2026-10-03 18:12:01 | b160cb81 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 4515 | 2026-10-03 18:12:01 | b160cb81 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-flash38", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwe |
| 4516 | 2026-10-03 18:23:52 | 9bce9ff8 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4517 | 2026-10-03 18:36:28 | 9bce9ff8 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 87s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [do |
| 4518 | 2026-10-03 18:36:28 | 9bce9ff8 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 87s [done] report expect='FACTORY' cmd=True \| T3 PASS 70s [do |
| 4519 | 2026-10-03 18:36:28 | e203c351 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5b6778f745304b77970b63b5b66bcf37", "after_quota": "9bce9ff87cb549b6b310b187092c5 |
| 4520 | 2026-10-03 18:36:28 | 9bce9ff8 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4521 | 2026-10-03 18:36:30 | ca238808 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4522 | 2026-10-03 18:49:20 | ca238808 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4523 | 2026-10-03 18:49:20 | ca238808 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 4524 | 2026-10-03 18:49:20 | d423a523 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "ebeb00d9ad6a4a4b8186056ccf5c3196", "after_quota": "ca2388084a454ec997f6f858e794a |
| 4525 | 2026-10-03 18:49:20 | ca238808 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4526 | 2026-10-03 18:49:22 | 70406b7d | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4527 | 2026-10-03 19:02:22 | 70406b7d | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 75s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 4528 | 2026-10-03 19:02:22 | 70406b7d | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 37s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 75s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 4529 | 2026-10-03 19:02:22 | 7054866c | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "aeb856dd164049c2891f58c9d8248e0f", "after_quota": "70406b7d0c7840ec9957fb0225e69 |
| 4530 | 2026-10-03 19:02:22 | 70406b7d | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 4531 | 2026-10-03 19:02:25 | 28936172 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4532 | 2026-10-03 19:10:56 | 3e606ba8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4533 | 2026-10-03 19:10:56 | 8de380de |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-03T20"}} |
| 4534 | 2026-10-03 19:12:09 | 3e606ba8 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 4535 | 2026-10-03 19:12:09 | 5d0438a1 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4536 | 2026-10-03 19:12:09 | 7b57e6cb |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4537 | 2026-10-03 19:12:09 | 96ca3eae |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4538 | 2026-10-03 19:12:09 | f7ccc654 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4539 | 2026-10-03 19:12:09 | 8bb50c87 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4540 | 2026-10-03 19:12:09 | 10db6ef6 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-03", "trigger": "blocked:gemini-flash36"}} |
| 4541 | 2026-10-03 19:12:09 | 3e606ba8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash-latest", "gemini-flash38", "gemini-gemma26b", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", " |
| 4542 | 2026-10-03 19:12:12 | f5fee259 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4543 | 2026-10-03 19:12:12 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 4544 | 2026-10-03 19:12:12 | 2b1c3328 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-03T20"}} |
| 4545 | 2026-10-03 19:12:12 | f5fee259 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 4546 | 2026-10-03 19:12:15 | 5d0438a1 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4547 | 2026-10-03 19:12:16 | 5d0438a1 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 4548 | 2026-10-03 19:12:19 | 7b57e6cb |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 4549 | 2026-10-03 19:12:19 | 7b57e6cb |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
