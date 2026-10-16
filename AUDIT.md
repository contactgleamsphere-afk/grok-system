# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
| 8204 | 2026-10-14 17:34:53 | 24975f92 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 8205 | 2026-10-14 17:34:56 | 34c4e275 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8206 | 2026-10-14 17:34:58 | 34c4e275 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 8207 | 2026-10-14 17:35:01 | 18de3bfd |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8208 | 2026-10-14 17:35:01 | 18de3bfd |  | owner.needed | fast-LAPTOP-LRE6PSA8 | {"provider": "cerebras", "reason": "set CEREBRAS_API_KEY (User env) after signing up: https://cloud.cerebras.ai (free tier ~1M tokens/day)"} |
| 8209 | 2026-10-14 17:35:01 | 18de3bfd |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8210 | 2026-10-14 17:35:04 | 5844091f |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8211 | 2026-10-14 17:35:05 | 5844091f |  | owner.needed | fast-LAPTOP-LRE6PSA8 | {"provider": "nvidia", "reason": "set NVIDIA_API_KEY (User env) after signing up: https://build.nvidia.com (free ~40 rpm, tool-capable model |
| 8212 | 2026-10-14 17:35:05 | 5844091f |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8213 | 2026-10-14 17:35:08 | 3eeb0a9d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8214 | 2026-10-14 17:35:08 | 3eeb0a9d |  | owner.needed | fast-LAPTOP-LRE6PSA8 | {"provider": "mistral", "reason": "set MISTRAL_API_KEY (User env) after signing up: https://console.mistral.ai (Experiment free tier)"} |
| 8215 | 2026-10-14 17:35:08 | 3eeb0a9d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8216 | 2026-10-15 00:24:26 | 50c9dc64 |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 8217 | 2026-10-15 00:24:26 | fca5af08 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8218 | 2026-10-15 00:24:28 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8219 | 2026-10-15 00:25:02 | 6bae1547 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-15T01"}} |
| 8220 | 2026-10-15 00:25:02 | fca5af08 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8221 | 2026-10-15 00:25:04 | 50c9dc64 |  | job.readopted | svc-LAPTOP-LRE6PSA8 | {} |
| 8222 | 2026-10-15 00:25:05 | 8bdeddda |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8223 | 2026-10-15 00:25:05 | d4220485 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T01"}} |
| 8224 | 2026-10-15 00:25:06 | 8bdeddda |  | probe.network_down | fast-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8225 | 2026-10-15 00:25:06 | cec87203 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-14T18-retry", "retry_of": "8bdeddda2de645119224d8e0a8d21851"}} |
| 8226 | 2026-10-15 00:25:06 | 8bdeddda |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8227 | 2026-10-15 00:35:10 | cec87203 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8228 | 2026-10-15 00:35:10 | d4220485 |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8229 | 2026-10-15 00:35:30 | cec87203 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 8230 | 2026-10-15 00:35:30 | cec87203 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-lite31", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 8231 | 2026-10-15 00:35:30 | cec87203 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss1 |
| 8232 | 2026-10-15 00:36:11 | 50c9dc64 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8233 | 2026-10-15 00:36:13 | 16edca8e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 8234 | 2026-10-15 00:51:43 | 16edca8e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 120s [done] report expect='FACTORY' cmd=True \| T3 PASS 135s  |
| 8235 | 2026-10-15 00:51:43 | 16edca8e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 120s [done] report expect='FACTORY' cmd=True \| T3 PASS 135s  |
| 8236 | 2026-10-15 00:51:43 | ae1ae481 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a5c9b2241151489ea85e56994e87fa75", "after_quota": "16edca8e04364537a29ff8c7b4617 |
| 8237 | 2026-10-15 00:51:43 | 16edca8e | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8238 | 2026-10-15 00:51:46 | 50c9dc64 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 8239 | 2026-10-15 01:03:39 | 50c9dc64 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 81s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 103s [done] report expect='FACTORY' cmd=True \| T3 PASS 100s  |
| 8240 | 2026-10-15 01:03:39 | 50c9dc64 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 81s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 103s [done] report expect='FACTORY' cmd=True \| T3 PASS 100s  |
| 8241 | 2026-10-15 01:03:39 | 50c9dc64 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 8242 | 2026-10-15 01:03:39 | 85478d12 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "abdd8333716b46e4b457f3e3406bd86a", "retry_of": "50c9dc64785044cf90eda416f7d1828 |
| 8243 | 2026-10-15 01:03:39 | 50c9dc64 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8244 | 2026-10-15 01:03:42 | 891f375d | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8245 | 2026-10-15 01:06:45 | 762d9d2c |  | job.enqueued | master-001 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-15", "trigger": "manual"}} |
| 8246 | 2026-10-15 01:06:50 | 762d9d2c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8247 | 2026-10-15 01:06:51 | 762d9d2c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 8248 | 2026-10-15 01:13:33 | 891f375d | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 36s [done] report expect='FACTORY' cmd=True \| T3 FAIL 51s [d |
| 8249 | 2026-10-15 01:13:33 | 891f375d | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 36s [done] report expect='FACTORY' cmd=True \| T3 FAIL 51s [d |
| 8250 | 2026-10-15 01:13:33 | 891f375d | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 8251 | 2026-10-15 01:13:33 | 46b621a3 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "43103e8f79ba46789af203ddbfb9e1ab", "retry_of": "891f375db0704520af72529daf070fc |
| 8252 | 2026-10-15 01:13:33 | 891f375d | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8253 | 2026-10-15 01:13:36 | e8402ec9 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8254 | 2026-10-15 01:25:04 | 6bae1547 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8255 | 2026-10-15 01:25:04 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8256 | 2026-10-15 01:25:05 | 15ff8e1a |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-15T02"}} |
| 8257 | 2026-10-15 01:25:05 | 6bae1547 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8258 | 2026-10-15 01:25:08 | d4220485 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8259 | 2026-10-15 01:25:08 | f8b3662d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T02"}} |
| 8260 | 2026-10-15 01:25:29 | d4220485 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss1 |
| 8261 | 2026-10-15 01:27:38 | e8402ec9 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 69s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 70s [done] report expect='FACTORY' cmd=True \| T3 PASS 74s [d |
| 8262 | 2026-10-15 01:27:38 | e8402ec9 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 69s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 70s [done] report expect='FACTORY' cmd=True \| T3 PASS 74s [d |
| 8263 | 2026-10-15 01:27:38 | f90c1262 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "4940d9aa166d426aadfe8f833d27143c", "after_quota": "e8402ec9d78445608dacc0906f30f |
| 8264 | 2026-10-15 01:27:38 | e8402ec9 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8265 | 2026-10-15 01:27:42 | da5c605f | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8266 | 2026-10-15 01:41:18 | da5c605f | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 72s [done] report expect='FACTORY' cmd=True \| T3 PASS 86s [d |
| 8267 | 2026-10-15 01:41:18 | da5c605f | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 72s [done] report expect='FACTORY' cmd=True \| T3 PASS 86s [d |
| 8268 | 2026-10-15 01:41:18 | a69dc170 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fe371a05201e499c9cc16d620128e678", "after_quota": "da5c605f2c9a404ca9ac517617354 |
| 8269 | 2026-10-15 01:41:18 | da5c605f | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8270 | 2026-10-15 01:41:19 | 85478d12 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8271 | 2026-10-15 01:54:17 | 85478d12 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 72s [done] report expect='FACTORY' cmd=True \| T3 PASS 76s [d |
| 8272 | 2026-10-15 01:54:17 | 85478d12 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 72s [done] report expect='FACTORY' cmd=True \| T3 PASS 76s [d |
| 8273 | 2026-10-15 01:54:17 | 9a8bdecc | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "85478d125abc4bb78d1345ebc19d14e0", "after_quota": "85478d125abc4bb78d1345ebc19d1 |
| 8274 | 2026-10-15 01:54:17 | 85478d12 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8275 | 2026-10-15 01:54:18 | 46b621a3 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8276 | 2026-10-15 02:11:11 | 46b621a3 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "    + FullyQualifiedErrorId : 2106,PSSessionStateBroken", "status": "testing", "inconclusive": false, "quota": 0} |
| 8277 | 2026-10-15 02:11:11 | 46b621a3 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "    + FullyQualifiedErrorId : 2106,PSSessionStateBroken", "after": "testing", "inconclusive": false, "quota": 0} |
| 8278 | 2026-10-15 02:11:11 | 46b621a3 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 8279 | 2026-10-15 02:11:11 | 32a6272c | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "43103e8f79ba46789af203ddbfb9e1ab", "retry_of": "46b621a381ec4013b70feba12270b2f |
| 8280 | 2026-10-15 02:11:11 | 46b621a3 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8281 | 2026-10-15 02:11:16 | e349b46e | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8282 | 2026-10-15 02:25:09 | 15ff8e1a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8283 | 2026-10-15 02:25:09 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8284 | 2026-10-15 02:25:09 | 244fedab |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-15T03"}} |
| 8285 | 2026-10-15 02:25:09 | 15ff8e1a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8286 | 2026-10-15 02:25:15 | f8b3662d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8287 | 2026-10-15 02:25:15 | 205c15fe |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T03"}} |
| 8288 | 2026-10-15 02:25:39 | f8b3662d |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 8289 | 2026-10-15 02:25:39 | f8b3662d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini |
| 8290 | 2026-10-15 02:29:03 | e349b46e | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "    + PSComputerName        : localhost", "status": "testing", "inconclusive": false, "quota": 0} |
| 8291 | 2026-10-15 02:29:03 | e349b46e | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "    + PSComputerName        : localhost", "after": "testing", "inconclusive": false, "quota": 0} |
| 8292 | 2026-10-15 02:29:03 | e349b46e | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 8293 | 2026-10-15 02:29:03 | 4e456ff7 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "496e3afd58764673a6b80d4e1d7f4792", "retry_of": "e349b46e153d49fb81648ed392b520d |
| 8294 | 2026-10-15 02:29:03 | e349b46e | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8295 | 2026-10-15 02:29:06 | 1d4d924b | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8296 | 2026-10-15 02:44:25 | 1d4d924b | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 58s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 110s [ |
| 8297 | 2026-10-15 02:44:26 | 1d4d924b | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 58s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 110s [ |
| 8298 | 2026-10-15 02:44:26 | 0d697328 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "5e3cb81dcaef415aa193471d2cd92af9", "after_quota": "1d4d924b511a4a999f791ef6142a0 |
| 8299 | 2026-10-15 02:44:26 | 1d4d924b | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8300 | 2026-10-15 02:44:28 | 32a6272c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8301 | 2026-10-15 10:08:18 | 32a6272c |  | job.lease_expired | svc-LAPTOP-LRE6PSA8 | {} |
| 8302 | 2026-10-15 10:08:19 | 244fedab |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8303 | 2026-10-15 10:08:21 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8304 | 2026-10-15 10:08:56 | 56755eba |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-15T11"}} |
| 8305 | 2026-10-15 10:08:56 | 244fedab |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8306 | 2026-10-15 10:09:06 | 205c15fe |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8307 | 2026-10-15 10:09:06 | 832ce531 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T11"}} |
| 8308 | 2026-10-15 10:09:18 | 32a6272c |  | job.readopted | fast-LAPTOP-LRE6PSA8 | {} |
| 8309 | 2026-10-15 10:10:27 | 205c15fe |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash-latest", "gemini-gemini-flash-lite-latest", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq- |
| 8310 | 2026-10-15 10:10:33 | 825829e8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8311 | 2026-10-15 10:10:33 | 825829e8 |  | audit.verified | svc-LAPTOP-LRE6PSA8 | {"rows": 8309, "hashed": 7557, "first_bad": null} |
| 8312 | 2026-10-15 10:10:33 | b870dd75 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-10-16"}} |
| 8313 | 2026-10-15 10:10:33 | 7c8d99c3 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-10-15"}} |
| 8314 | 2026-10-15 10:10:33 | 5890e6f6 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-10-15"}} |
| 8315 | 2026-10-15 10:10:33 | 09327984 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-10-15"}} |
| 8316 | 2026-10-15 10:10:33 | 825829e8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8317 | 2026-10-15 10:10:38 | 09327984 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8318 | 2026-10-15 10:10:38 | ddd0d108 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "09327984c00e4518b33e1c8840b53ca3", "day": "2026-10-15"}} |
| 8319 | 2026-10-15 10:10:38 | 09327984 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001"], "jobs": ["ddd0d108"]} |
| 8320 | 2026-10-15 10:10:38 | 09327984 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8321 | 2026-10-15 10:10:43 | 7c8d99c3 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8322 | 2026-10-15 10:10:43 | 7c8d99c3 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": []}} |
| 8323 | 2026-10-15 10:10:48 | 5890e6f6 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8324 | 2026-10-15 10:10:52 | 5890e6f6 |  | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "security", "next_state": "paused", "attempt": 1, "error": "FactoryError: could not produce a valid spec after 3 attempts: |
| 8325 | 2026-10-15 10:14:25 | 09327984 |  | job.dedup | nightly-task | {"kind": "monitor", "note": "slot already done"} |
| 8326 | 2026-10-15 10:29:13 | 32a6272c | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8327 | 2026-10-15 10:29:14 | 4e456ff7 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8328 | 2026-10-15 10:51:50 | 4e456ff7 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8329 | 2026-10-15 10:51:52 | 32a6272c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 8330 | 2026-10-15 11:09:00 | 56755eba |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8331 | 2026-10-15 11:09:00 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8332 | 2026-10-15 11:09:00 | d17f8621 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-15T12"}} |
| 8333 | 2026-10-15 11:09:00 | 56755eba |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8334 | 2026-10-15 11:09:09 | 832ce531 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8335 | 2026-10-15 11:09:09 | f9ac8cc5 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T12"}} |
| 8336 | 2026-10-15 11:10:25 | 832ce531 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-gemini-flash-lite-latest", "gemini-lite", "gemini-lite31", "groq-gpt |
| 8337 | 2026-10-15 11:14:39 | 32a6272c | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8338 | 2026-10-15 11:14:42 | 4e456ff7 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 8339 | 2026-10-15 11:36:53 | 4e456ff7 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 2, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8340 | 2026-10-15 11:36:58 | 32a6272c | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 8341 | 2026-10-15 11:59:13 | 32a6272c | 001 | job.failed | fast-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "failed", "attempt": 3, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8342 | 2026-10-15 11:59:17 | 4e456ff7 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 3} |
| 8343 | 2026-10-15 12:09:04 | d17f8621 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8344 | 2026-10-15 12:09:05 |  | 018 | schedule.skipped | svc-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8345 | 2026-10-15 12:09:05 | 9af46346 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-15T13"}} |
| 8346 | 2026-10-15 12:09:05 | d17f8621 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8347 | 2026-10-15 12:09:10 | f9ac8cc5 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8348 | 2026-10-15 12:09:10 | 82c93961 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T13"}} |
| 8349 | 2026-10-15 12:11:33 | f9ac8cc5 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-gemma26b", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 500, |
| 8350 | 2026-10-15 12:11:33 | c9dfc3fe |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-15", "trigger": "blocked:gemini-gemma26b"}} |
| 8351 | 2026-10-15 12:11:33 | 3acc64d6 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-15", "trigger": "blocked:gemini-gemma26b"}} |
| 8352 | 2026-10-15 12:11:33 | 518116a9 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-15", "trigger": "blocked:gemini-gemma26b"}} |
| 8353 | 2026-10-15 12:11:33 | f17a6f90 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-15", "trigger": "blocked:gemini-gemma26b"}} |
| 8354 | 2026-10-15 12:11:33 | 0a3c68da |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-15", "trigger": "blocked:gemini-gemma26b"}} |
| 8355 | 2026-10-15 12:11:33 | 972fa658 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-15", "trigger": "blocked:gemini-gemma26b"}} |
| 8356 | 2026-10-15 12:11:33 | f9ac8cc5 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-gemini-flash-lite-latest", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptoss2 |
| 8357 | 2026-10-15 12:11:43 | c9dfc3fe |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8358 | 2026-10-15 12:11:44 | c9dfc3fe |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 8359 | 2026-10-15 12:11:52 | 3acc64d6 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8360 | 2026-10-15 12:11:54 | 3acc64d6 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 8361 | 2026-10-15 12:11:59 | 518116a9 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8362 | 2026-10-15 12:12:00 | 518116a9 |  | lane.rejected | svc-LAPTOP-LRE6PSA8 | {"model": "thinkingmachines/inkling-small:free", "reason": "probe auth: {\"error\":{\"message\":\"thinkingmachines/inkling-small:free is onl |
| 8363 | 2026-10-15 12:12:00 | 518116a9 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 8364 | 2026-10-15 12:12:03 | f17a6f90 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8365 | 2026-10-15 12:12:03 | f17a6f90 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8366 | 2026-10-15 12:12:07 | 0a3c68da |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8367 | 2026-10-15 12:12:07 | 0a3c68da |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8368 | 2026-10-15 12:12:11 | 972fa658 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8369 | 2026-10-15 12:12:11 | 972fa658 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8370 | 2026-10-15 12:21:06 | 4e456ff7 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 68s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 248s [TIMEOUT] report expect='FACTORY' cmd=False \| T3 FAIL 2 |
| 8371 | 2026-10-15 12:21:06 | 4e456ff7 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 68s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 248s [TIMEOUT] report expect='FACTORY' cmd=False \| T3 FAIL 2 |
| 8372 | 2026-10-15 12:21:06 | 4e456ff7 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 8373 | 2026-10-15 12:21:06 | 1d545c4a | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "496e3afd58764673a6b80d4e1d7f4792", "retry_of": "4e456ff7e6674717b907e5f1011ebd0 |
| 8374 | 2026-10-15 12:21:06 | 4e456ff7 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 6, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8375 | 2026-10-15 12:21:10 | 01291e79 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8376 | 2026-10-15 12:33:59 | 01291e79 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 8377 | 2026-10-15 12:33:59 | 01291e79 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 67s [d |
| 8378 | 2026-10-15 12:33:59 | 1f853053 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "773c8a3bd76049e6b5a24b3e92ea65fc", "after_quota": "01291e794f6d415a8daf7accb6bc9 |
| 8379 | 2026-10-15 12:33:59 | 01291e79 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8380 | 2026-10-15 12:34:02 | 585d7c88 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8381 | 2026-10-15 12:47:30 | 585d7c88 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 51s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 83s [done] report expect='FACTORY' cmd=True \| T3 PASS 81s [d |
| 8382 | 2026-10-15 12:47:30 | 585d7c88 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 51s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 83s [done] report expect='FACTORY' cmd=True \| T3 PASS 81s [d |
| 8383 | 2026-10-15 12:47:30 | a462b20c | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "fefd132857c64f0d981f48b23770a2c5", "after_quota": "585d7c88852245d389ae93f57244b |
| 8384 | 2026-10-15 12:47:30 | 585d7c88 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8385 | 2026-10-15 12:47:34 | 7838d8fd | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8386 | 2026-10-15 13:00:45 | 7838d8fd | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 85s [d |
| 8387 | 2026-10-15 13:00:45 | 7838d8fd | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 39s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 67s [done] report expect='FACTORY' cmd=True \| T3 PASS 85s [d |
| 8388 | 2026-10-15 13:00:45 | 3286fc15 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "f9b10c1ee6d14bebb81112682f64492f", "after_quota": "7838d8fd678d4329848e9835454ba |
| 8389 | 2026-10-15 13:00:45 | 7838d8fd | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8390 | 2026-10-15 13:00:49 | 1d545c4a | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8391 | 2026-10-15 13:09:05 | 9af46346 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8392 | 2026-10-15 13:09:05 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8393 | 2026-10-15 13:09:06 | 808aa83f |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-15T14"}} |
| 8394 | 2026-10-15 13:09:06 | 9af46346 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8395 | 2026-10-15 13:09:14 | 82c93961 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8396 | 2026-10-15 13:09:14 | 925d90d1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T14"}} |
| 8397 | 2026-10-15 13:10:13 | 82c93961 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen2 |
| 8398 | 2026-10-15 13:13:30 | 1d545c4a | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 64s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 8399 | 2026-10-15 13:13:30 | 1d545c4a | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 64s [done] report expect='FACTORY' cmd=True \| T3 PASS 68s [d |
| 8400 | 2026-10-15 13:13:30 | 89f88404 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "1d545c4afe8b46f4a9c9d3e951ed6909", "after_quota": "1d545c4afe8b46f4a9c9d3e951ed6 |
| 8401 | 2026-10-15 13:13:30 | 1d545c4a | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8402 | 2026-10-15 13:13:32 | ae1ae481 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8403 | 2026-10-15 13:26:45 | ae1ae481 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 64s [d |
| 8404 | 2026-10-15 13:26:45 | ae1ae481 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 38s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 65s [done] report expect='FACTORY' cmd=True \| T3 PASS 64s [d |
| 8405 | 2026-10-15 13:26:45 | af60019c | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "a5c9b2241151489ea85e56994e87fa75", "after_quota": "ae1ae481889044e7a76466ac215ed |
| 8406 | 2026-10-15 13:26:45 | ae1ae481 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8407 | 2026-10-15 13:26:48 | f90c1262 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8408 | 2026-10-16 10:52:51 | f90c1262 |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 8409 | 2026-10-16 10:53:01 | 808aa83f |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8410 | 2026-10-16 10:53:17 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8411 | 2026-10-16 10:53:17 | f90c1262 |  | job.readopted | svc-LAPTOP-LRE6PSA8 | {} |
| 8412 | 2026-10-16 10:53:37 | bdeb9e25 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-16T11"}} |
| 8413 | 2026-10-16 10:53:37 | 808aa83f |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8414 | 2026-10-16 10:53:42 | 925d90d1 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8415 | 2026-10-16 10:53:42 | 414a8f1b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-16T11"}} |
| 8416 | 2026-10-16 10:53:43 | 925d90d1 |  | probe.network_down | fast-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8417 | 2026-10-16 10:53:43 | fd795f3b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T14-retry", "retry_of": "925d90d13cad42388f1cf20962eac748"}} |
| 8418 | 2026-10-16 10:53:43 | 925d90d1 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8419 | 2026-10-16 10:53:49 | b870dd75 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8420 | 2026-10-16 10:53:50 | b870dd75 |  | audit.verified | fast-LAPTOP-LRE6PSA8 | {"rows": 8418, "hashed": 7666, "first_bad": null} |
| 8421 | 2026-10-16 10:53:53 | 4e557385 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-10-17"}} |
| 8422 | 2026-10-16 10:53:53 | b4f33739 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-10-16"}} |
| 8423 | 2026-10-16 10:53:55 | 48ca0b76 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-10-16"}} |
| 8424 | 2026-10-16 10:54:11 | 4a6927b6 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-10-16"}} |
| 8425 | 2026-10-16 10:54:11 | b870dd75 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8426 | 2026-10-16 10:54:17 | 4a6927b6 |  | job.dedup | nightly-task | {"kind": "monitor"} |
| 8427 | 2026-10-16 11:01:40 | f90c1262 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 64s [done] report expect='FACTORY' cmd=True \| T3 PASS 65s [d |
| 8428 | 2026-10-16 11:01:40 | f90c1262 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 40s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 64s [done] report expect='FACTORY' cmd=True \| T3 PASS 65s [d |
| 8429 | 2026-10-16 11:01:40 | f90c1262 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 8430 | 2026-10-16 11:01:40 | 8732a69d | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "retry_of": "f90c1262bfb44daf8d2e80463508745 |
| 8431 | 2026-10-16 11:01:40 | f90c1262 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 7, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8432 | 2026-10-16 11:01:42 | a69dc170 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8433 | 2026-10-16 11:03:43 | fd795f3b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8434 | 2026-10-16 11:03:43 | 9db99607 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-16T12"}} |
| 8435 | 2026-10-16 11:03:44 | fd795f3b |  | probe.network_down | fast-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8436 | 2026-10-16 11:03:44 | 2c9358fc |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T14-retry-retry", "retry_of": "fd795f3b66dc488dae80070137305439"}} |
| 8437 | 2026-10-16 11:03:44 | fd795f3b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8438 | 2026-10-16 11:13:46 | 2c9358fc |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8439 | 2026-10-16 11:13:46 | 9db99607 |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8440 | 2026-10-16 11:13:47 | 2c9358fc |  | probe.network_down | fast-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8441 | 2026-10-16 11:13:47 | 2a6af73e |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T14-retry-retry-retry", "retry_of": "2c9358fcaaa34069be937a74677e0a44"}} |
| 8442 | 2026-10-16 11:13:47 | 2c9358fc |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8443 | 2026-10-16 11:23:51 | 2a6af73e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8444 | 2026-10-16 11:23:51 | 9db99607 |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8445 | 2026-10-16 11:23:51 | 2a6af73e |  | probe.network_down | fast-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8446 | 2026-10-16 11:23:51 | 74de9a9c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T14-retry-retry-retry-retry", "retry_of": "2a6af73e60ec4d68abce25f1f73d56e9"}} |
| 8447 | 2026-10-16 11:23:51 | 2a6af73e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8448 | 2026-10-16 11:23:55 | a69dc170 | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8449 | 2026-10-16 11:23:57 | 9a8bdecc | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8450 | 2026-10-16 11:33:53 | 74de9a9c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8451 | 2026-10-16 11:33:53 | 9db99607 |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8452 | 2026-10-16 11:33:54 | 74de9a9c |  | probe.network_down | fast-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8453 | 2026-10-16 11:33:54 | 3a052695 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T14-retry-retry-retry-retry-retry", "retry_of": "74de9a9c02544063b72507a71d3446 |
| 8454 | 2026-10-16 11:33:54 | 74de9a9c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8455 | 2026-10-16 12:30:28 | 9a8bdecc |  | job.lease_expired | fast-LAPTOP-LRE6PSA8 | {} |
| 8456 | 2026-10-16 12:30:28 | 3a052695 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8457 | 2026-10-16 12:30:29 | 69ca9d83 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-16T13"}} |
| 8458 | 2026-10-16 12:30:31 | 3a052695 |  | probe.network_down | fast-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8459 | 2026-10-16 12:30:31 | 8e8fa6b1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T14-retry-retry-retry-retry-retry-retry", "retry_of": "3a052695f7f24b78aba57191 |
| 8460 | 2026-10-16 12:30:31 | 3a052695 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8461 | 2026-10-16 12:30:35 | bdeb9e25 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8462 | 2026-10-16 12:30:35 |  | 018 | schedule.skipped | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "reason": "bot testing"} |
| 8463 | 2026-10-16 12:30:36 | 49c1f9c7 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-10-16T13"}} |
| 8464 | 2026-10-16 12:30:36 | bdeb9e25 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8465 | 2026-10-16 12:30:37 | 414a8f1b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8466 | 2026-10-16 12:30:37 | 69ca9d83 |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8467 | 2026-10-16 12:30:37 | 414a8f1b |  | probe.network_down | fast-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8468 | 2026-10-16 12:30:37 | 4c528adb |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-16T11-retry", "retry_of": "414a8f1bf90a4eddadbf60bee1d12e33"}} |
| 8469 | 2026-10-16 12:30:37 | 414a8f1b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8470 | 2026-10-16 12:30:38 | 9db99607 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8471 | 2026-10-16 12:30:38 | 69ca9d83 |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8472 | 2026-10-16 12:30:39 | 9db99607 |  | probe.network_down | fast-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8473 | 2026-10-16 12:30:39 | 37bfd506 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-16T12-retry", "retry_of": "9db99607a4e140faaf7313be762ee49d"}} |
| 8474 | 2026-10-16 12:30:39 | 9db99607 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8475 | 2026-10-16 12:30:39 | 8732a69d | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8476 | 2026-10-16 12:31:03 | 9a8bdecc |  | job.readopted | svc-LAPTOP-LRE6PSA8 | {} |
| 8477 | 2026-10-16 12:34:00 | 9a8bdecc | 001 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "transient", "next_state": "queued", "attempt": 1, "error": "TimeoutExpired: Command '['powershell', '-NoProfile', '-Execu |
| 8478 | 2026-10-16 12:34:02 | 4a6927b6 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8479 | 2026-10-16 12:34:02 | 49f1b187 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "4a6927b6447747a1b4c4217776261da0", "day": "2026-10-16"}} |
| 8480 | 2026-10-16 12:34:02 | 4a6927b6 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001"], "jobs": ["49f1b187"]} |
| 8481 | 2026-10-16 12:34:02 | 4a6927b6 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8482 | 2026-10-16 12:34:02 | b4f33739 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8483 | 2026-10-16 12:34:02 | b4f33739 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": []}} |
| 8484 | 2026-10-16 12:34:03 | 48ca0b76 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8485 | 2026-10-16 12:34:03 | 48ca0b76 |  | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "RuntimeError: all lanes failed: groq:openai/gpt-oss-120b URLError |
| 8486 | 2026-10-16 12:40:34 | 8e8fa6b1 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8487 | 2026-10-16 12:40:34 | 69ca9d83 |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8488 | 2026-10-16 12:40:35 | 8e8fa6b1 |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8489 | 2026-10-16 12:40:35 | dde421c1 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T14-retry-retry-retry-retry-retry-retry-retry", "retry_of": "8e8fa6b1c571428cb2 |
| 8490 | 2026-10-16 12:40:35 | 8e8fa6b1 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8491 | 2026-10-16 12:40:41 | 4c528adb |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8492 | 2026-10-16 12:40:41 | 69ca9d83 |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8493 | 2026-10-16 12:40:41 | 4c528adb |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8494 | 2026-10-16 12:40:41 | 0387ef84 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-16T11-retry-retry", "retry_of": "4c528adb787f4eedb76b4fa4f710b62a"}} |
| 8495 | 2026-10-16 12:40:41 | 4c528adb |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8496 | 2026-10-16 12:40:42 | 37bfd506 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8497 | 2026-10-16 12:40:42 | 69ca9d83 |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8498 | 2026-10-16 12:40:43 | 37bfd506 |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8499 | 2026-10-16 12:40:43 | 01175374 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-16T12-retry-retry", "retry_of": "37bfd5068ed04321bfc24cbfe1c8a0bf"}} |
| 8500 | 2026-10-16 12:40:43 | 37bfd506 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8501 | 2026-10-16 12:50:39 | dde421c1 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8502 | 2026-10-16 12:50:39 | 69ca9d83 |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8503 | 2026-10-16 12:50:40 | dde421c1 |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8504 | 2026-10-16 12:50:40 | ac5b49ba |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-15T14-retry-retry-retry-retry-retry-retry-retry-retry", "retry_of": "dde421c1ad7f |
| 8505 | 2026-10-16 12:50:40 | dde421c1 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8506 | 2026-10-16 12:50:42 | 0387ef84 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8507 | 2026-10-16 12:50:42 | 69ca9d83 |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8508 | 2026-10-16 12:50:45 | 0387ef84 |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8509 | 2026-10-16 12:50:45 | 043066e1 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-16T11-retry-retry-retry", "retry_of": "0387ef84f2024880814c08ef360cdb17"}} |
| 8510 | 2026-10-16 12:50:45 | 0387ef84 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8511 | 2026-10-16 12:50:47 | 01175374 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8512 | 2026-10-16 12:50:47 | 69ca9d83 |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8513 | 2026-10-16 12:50:48 | 01175374 |  | probe.network_down | svc-LAPTOP-LRE6PSA8 | {"detail": "all 15 remote lanes across 3 providers errored in one sweep -> local network outage, health untouched"} |
| 8514 | 2026-10-16 12:50:48 | 64c6792d |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-16T12-retry-retry-retry", "retry_of": "0117537429504dadbe4922152491f2bc"}} |
| 8515 | 2026-10-16 12:50:48 | 01175374 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 8516 | 2026-10-16 12:51:47 | 8732a69d | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 145s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 245s [TIMEOUT] report expect='FACTORY' cmd=False \| T3 FAIL  |
| 8517 | 2026-10-16 12:51:47 | 8732a69d | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 145s [done] liveness expect='MASTER_OK' cmd=True \| T2 FAIL 245s [TIMEOUT] report expect='FACTORY' cmd=False \| T3 FAIL  |
| 8518 | 2026-10-16 12:51:47 | 8732a69d | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 8519 | 2026-10-16 12:51:47 | 37ba78fb | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "1c1bcdfb30db4c05870f61a3c116427f", "retry_of": "8732a69d5f20410c98c447eaaf6e181 |
| 8520 | 2026-10-16 12:51:47 | 8732a69d | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 2, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8521 | 2026-10-16 12:51:48 | a69dc170 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 8522 | 2026-10-16 13:00:41 | ac5b49ba |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8523 | 2026-10-16 13:00:41 | 689cc06f |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-10-16T14"}} |
| 8524 | 2026-10-16 13:03:10 | ac5b49ba |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\":  |
| 8525 | 2026-10-16 13:03:10 | ac5b49ba |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-gemma26b", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 8526 | 2026-10-16 13:03:10 | 09c2f6de |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-16", "trigger": "blocked:gemini-flash-latest"}} |
| 8527 | 2026-10-16 13:03:10 | d5eb2432 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-16", "trigger": "blocked:gemini-flash-latest"}} |
| 8528 | 2026-10-16 13:03:10 | f5d5b555 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-16", "trigger": "blocked:gemini-flash-latest"}} |
| 8529 | 2026-10-16 13:03:10 | 2ef6b3f7 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-16", "trigger": "blocked:gemini-flash-latest"}} |
| 8530 | 2026-10-16 13:03:10 | 20951e9d |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-16", "trigger": "blocked:gemini-flash-latest"}} |
| 8531 | 2026-10-16 13:03:10 | 083eafec |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-16", "trigger": "blocked:gemini-flash-latest"}} |
| 8532 | 2026-10-16 13:03:10 | ac5b49ba |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gpto |
| 8533 | 2026-10-16 13:03:15 | 043066e1 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8534 | 2026-10-16 13:03:15 | 689cc06f |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8535 | 2026-10-16 13:05:28 | 043066e1 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash-latest", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 8536 | 2026-10-16 13:05:28 | 043066e1 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash38", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 8537 | 2026-10-16 13:05:28 | 043066e1 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash-latest", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gem |
| 8538 | 2026-10-16 13:05:32 | 64c6792d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8539 | 2026-10-16 13:05:32 | 689cc06f |  | job.dedup | fast-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8540 | 2026-10-16 13:05:43 | a69dc170 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 121s [done] report expect='FACTORY' cmd=True \| T3 FAIL 54s [ |
| 8541 | 2026-10-16 13:05:44 | a69dc170 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 121s [done] report expect='FACTORY' cmd=True \| T3 FAIL 54s [ |
| 8542 | 2026-10-16 13:05:44 | a69dc170 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 8543 | 2026-10-16 13:05:44 | a56f4044 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "f174fbc671544e27bad96250dd6ea9e2", "retry_of": "a69dc170e05c4c00b71a5c118c9310a |
| 8544 | 2026-10-16 13:05:44 | a69dc170 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8545 | 2026-10-16 13:05:48 | 09c2f6de |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8546 | 2026-10-16 13:05:49 | 09c2f6de |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 8547 | 2026-10-16 13:05:53 | d5eb2432 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8548 | 2026-10-16 13:05:54 | d5eb2432 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 8549 | 2026-10-16 13:06:02 | f5d5b555 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8550 | 2026-10-16 13:06:07 | f5d5b555 |  | lane.discovered | svc-LAPTOP-LRE6PSA8 | {"model": "nvidia/nemotron-3.5-super-vl:free", "reason": "probe 1.65s loop 2.48s", "provider": "openrouter"} |
| 8551 | 2026-10-16 13:06:07 | f5d5b555 |  | config.presets | svc-LAPTOP-LRE6PSA8 | {"added": ["or-nemotron-35-super-vl"]} |
| 8552 | 2026-10-16 13:06:08 | 95f4a23c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"lanes": ["or-nemotron-35-super-vl"], "day": "2026-10-16"}} |
| 8553 | 2026-10-16 13:06:08 | f5d5b555 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": ["or-nemotron-35-super-vl"]}} |
| 8554 | 2026-10-16 13:06:11 | 2ef6b3f7 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8555 | 2026-10-16 13:06:11 | 2ef6b3f7 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8556 | 2026-10-16 13:06:14 | 20951e9d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8557 | 2026-10-16 13:06:14 | 20951e9d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8558 | 2026-10-16 13:06:17 | 083eafec |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8559 | 2026-10-16 13:06:17 | 083eafec |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8560 | 2026-10-16 13:06:20 | 9a8bdecc | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 2} |
| 8561 | 2026-10-16 13:07:09 | 64c6792d |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "or-nemotron-3-ultra-550b-a55b", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "TimeoutError"} |
| 8562 | 2026-10-16 13:07:09 | 05259876 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-10-16", "trigger": "blocked:or-nemotron-3-ultra-550b-a55b"}} |
| 8563 | 2026-10-16 13:07:09 | 43b6674b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-10-16", "trigger": "blocked:or-nemotron-3-ultra-550b-a55b"}} |
| 8564 | 2026-10-16 13:07:09 | df2b02ca |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-10-16", "trigger": "blocked:or-nemotron-3-ultra-550b-a55b"}} |
| 8565 | 2026-10-16 13:07:09 | 3c2a3782 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-10-16", "trigger": "blocked:or-nemotron-3-ultra-550b-a55b"}} |
| 8566 | 2026-10-16 13:07:09 | 90002f23 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-10-16", "trigger": "blocked:or-nemotron-3-ultra-550b-a55b"}} |
| 8567 | 2026-10-16 13:07:09 | f342cc06 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-10-16", "trigger": "blocked:or-nemotron-3-ultra-550b-a55b"}} |
| 8568 | 2026-10-16 13:07:09 | 64c6792d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "groq-gptoss120b", "groq-gptoss20b", "groq-qwen27b", "local3b |
| 8569 | 2026-10-16 13:07:13 | 05259876 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8570 | 2026-10-16 13:07:13 | 05259876 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 8571 | 2026-10-16 13:07:17 | 43b6674b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8572 | 2026-10-16 13:07:17 | 43b6674b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8573 | 2026-10-16 13:07:20 | df2b02ca |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8574 | 2026-10-16 13:07:20 | df2b02ca |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8575 | 2026-10-16 13:07:24 | 3c2a3782 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8576 | 2026-10-16 13:07:24 | 3c2a3782 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8577 | 2026-10-16 13:07:27 | 90002f23 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8578 | 2026-10-16 13:07:27 | 90002f23 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8579 | 2026-10-16 13:07:31 | f342cc06 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8580 | 2026-10-16 13:07:31 | f342cc06 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 8581 | 2026-10-16 13:16:25 | 9a8bdecc | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 15s [done] report expect='FACTORY' cmd=True \| T3 PASS 86s [d |
| 8582 | 2026-10-16 13:16:25 | 9a8bdecc | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 15s [done] report expect='FACTORY' cmd=True \| T3 PASS 86s [d |
| 8583 | 2026-10-16 13:16:25 | a793c414 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "retest_of": "85478d125abc4bb78d1345ebc19d14e0", "after_quota": "9a8bdecc02644930a66d63f5ddc6f |
| 8584 | 2026-10-16 13:16:25 | 9a8bdecc | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8585 | 2026-10-16 13:16:28 | 0d697328 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8586 | 2026-10-16 13:21:04 | 0d697328 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 37s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 8587 | 2026-10-16 13:21:04 | 0d697328 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 37s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 8588 | 2026-10-16 13:21:04 | 0d697328 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 8589 | 2026-10-16 13:21:04 | 1a389171 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "33d3730f13e945aa8839588d7a0ec4b7", "retry_of": "0d6973285ff94507b0a7a2d2b896b90 |
| 8590 | 2026-10-16 13:21:04 | 0d697328 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 8, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8591 | 2026-10-16 13:21:05 | 1f853053 | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8592 | 2026-10-16 13:21:08 | 95f4a23c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8593 | 2026-10-16 13:21:56 | 95f4a23c |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "or-nemotron-35-super-vl", "result": "2/4", "quota": 0, "secs": 47} |
| 8594 | 2026-10-16 13:21:56 | 95f4a23c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["or-nemotron-35-super-vl", "2/4"]]}} |
| 8595 | 2026-10-16 13:27:51 | 1f853053 | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 23s [done] report expect='FACTORY' cmd=True \| T3 FAIL 100s [ |
| 8596 | 2026-10-16 13:27:51 | 1f853053 | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 23s [done] report expect='FACTORY' cmd=True \| T3 FAIL 100s [ |
| 8597 | 2026-10-16 13:27:51 | 1f853053 | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 8598 | 2026-10-16 13:27:51 | a702e4a1 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "df14302d7564425b9a49f64f7d268591", "retry_of": "1f85305368944d65b5554c0bddaa9e2 |
| 8599 | 2026-10-16 13:27:51 | 1f853053 | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 7, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 8600 | 2026-10-16 13:27:54 | 37ba78fb | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8601 | 2026-10-16 13:30:31 | 69ca9d83 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 8602 | 2026-10-16 13:30:31 | 689cc06f |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 8603 | 2026-10-16 13:32:53 | 69ca9d83 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gpto |
