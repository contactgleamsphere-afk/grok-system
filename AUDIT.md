# AUDIT — append-only factory event log (latest 400)

| seq | time | job | bot | event | actor | detail |
|---|---|---|---|---|---|---|
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
| 1836 | 2026-09-25 20:10:25 | 3fa27047 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1837 | 2026-09-25 20:10:26 | 3fa27047 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1838 | 2026-09-25 20:10:30 | 2bbe411d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1839 | 2026-09-25 20:10:30 | 2bbe411d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1840 | 2026-09-25 20:10:34 | a7cf454b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1841 | 2026-09-25 20:10:34 | a7cf454b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1842 | 2026-09-25 20:10:38 | e9039318 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1843 | 2026-09-25 20:10:38 | e9039318 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1844 | 2026-09-25 20:10:43 | a1ec1245 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1845 | 2026-09-25 20:10:43 | 6acda974 | 014 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "014", "monitor_of": "a1ec1245d09c465fb7daaec24fbd41f2", "day": "2026-09-25"}} |
| 1846 | 2026-09-25 20:10:43 | a1ec1245 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["014"], "jobs": ["6acda974"]} |
| 1847 | 2026-09-25 20:10:43 | a1ec1245 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1848 | 2026-09-25 20:10:48 | 6acda974 | 014 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1849 | 2026-09-25 20:12:29 | 6acda974 | 014 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 14s [done] expect='5' last='RESULT: 5' \| T3 PASS 63s [done] expect='Time |
| 1850 | 2026-09-25 20:12:29 | 6acda974 | 014 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 PASS 14s [done] expect='5' last='RESULT: 5' \| T3 PASS 63s [done] expect='Time |
| 1851 | 2026-09-25 20:12:29 | 6acda974 | 014 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "014", "status": "active", "verified": "VERIFIED"}} |
| 1852 | 2026-09-25 20:59:46 | 865a2980 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1853 | 2026-09-25 20:59:46 | 80e90b9b |  | job.dedup | svc-LAPTOP-LRE6PSA8 | {"kind": "probe"} |
| 1854 | 2026-09-25 20:59:57 | 54829a12 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1855 | 2026-09-25 20:59:58 | a7ddc40b |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T21"}} |
| 1856 | 2026-09-25 20:59:58 | 54829a12 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1857 | 2026-09-25 21:00:44 | 865a2980 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "no_tool_call", "before": "VERIFIED", "after": "BLOCKED", "detail": null} |
| 1858 | 2026-09-25 21:00:44 | 00afddce |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1859 | 2026-09-25 21:00:44 | 5146a28d |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1860 | 2026-09-25 21:00:44 | f0d2836f |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1861 | 2026-09-25 21:00:44 | af65672a |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1862 | 2026-09-25 21:00:44 | 4c6af4e8 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1863 | 2026-09-25 21:00:44 | 5245a37e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-25", "trigger": "blocked:gemini-flash36"}} |
| 1864 | 2026-09-25 21:00:44 | 865a2980 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 1865 | 2026-09-25 21:00:47 | 00afddce |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1866 | 2026-09-25 21:00:48 | 00afddce |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1867 | 2026-09-25 21:00:48 | 5146a28d |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1868 | 2026-09-25 21:00:48 | 5146a28d |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1869 | 2026-09-25 21:00:52 | f0d2836f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1870 | 2026-09-25 21:00:52 | f0d2836f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1871 | 2026-09-25 21:00:56 | af65672a |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1872 | 2026-09-25 21:00:56 | af65672a |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1873 | 2026-09-25 21:01:00 | 4c6af4e8 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1874 | 2026-09-25 21:01:00 | 4c6af4e8 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1875 | 2026-09-25 21:01:04 | 5245a37e |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1876 | 2026-09-25 21:01:04 | 5245a37e |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1877 | 2026-09-25 21:09:49 | 80e90b9b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1878 | 2026-09-25 21:09:49 | 24db754c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T22"}} |
| 1879 | 2026-09-25 21:10:12 | 80e90b9b |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "error", "before": "VERIFIED", "after": "BLOCKED", "detail": "[{\n  \"error\": {\n    \"code\": 503,\n  |
| 1880 | 2026-09-25 21:10:12 | 263c1d32 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "groq", "day": "2026-09-25", "trigger": "blocked:gemini-flash"}} |
| 1881 | 2026-09-25 21:10:12 | d0076ca3 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "gemini", "day": "2026-09-25", "trigger": "blocked:gemini-flash"}} |
| 1882 | 2026-09-25 21:10:12 | 03adb38c |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "openrouter", "day": "2026-09-25", "trigger": "blocked:gemini-flash"}} |
| 1883 | 2026-09-25 21:10:12 | 9efc5dbb |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "cerebras", "day": "2026-09-25", "trigger": "blocked:gemini-flash"}} |
| 1884 | 2026-09-25 21:10:12 | b691ec23 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "nvidia", "day": "2026-09-25", "trigger": "blocked:gemini-flash"}} |
| 1885 | 2026-09-25 21:10:12 | 8958c7c2 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "discover", "payload": {"provider": "mistral", "day": "2026-09-25", "trigger": "blocked:gemini-flash"}} |
| 1886 | 2026-09-25 21:10:12 | 80e90b9b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gpto |
| 1887 | 2026-09-25 21:10:14 | 263c1d32 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1888 | 2026-09-25 21:10:15 | 263c1d32 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"added": []}} |
| 1889 | 2026-09-25 21:10:16 | d0076ca3 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1890 | 2026-09-25 21:10:16 | d0076ca3 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1891 | 2026-09-25 21:10:19 | 03adb38c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1892 | 2026-09-25 21:10:20 | 03adb38c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1893 | 2026-09-25 21:10:23 | 9efc5dbb |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1894 | 2026-09-25 21:10:23 | 9efc5dbb |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1895 | 2026-09-25 21:10:27 | b691ec23 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1896 | 2026-09-25 21:10:27 | b691ec23 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1897 | 2026-09-25 21:10:31 | 8958c7c2 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1898 | 2026-09-25 21:10:31 | 8958c7c2 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"added": null}} |
| 1899 | 2026-09-25 21:59:58 | a7ddc40b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1900 | 2026-09-25 21:59:58 | 6611e45e |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-25T22"}} |
| 1901 | 2026-09-25 21:59:58 | a7ddc40b |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1902 | 2026-09-25 22:09:49 | 24db754c |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1903 | 2026-09-25 22:09:49 | 2e9399d2 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-25T23"}} |
| 1904 | 2026-09-25 22:10:07 | 24db754c |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptoss120b", "groq-gpto |
| 1905 | 2026-09-25 23:00:01 | 6611e45e |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1906 | 2026-09-25 23:00:02 | fc8525b1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-26T00"}} |
| 1907 | 2026-09-25 23:00:02 | 6611e45e |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1908 | 2026-09-25 23:37:13 | 2e9399d2 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1909 | 2026-09-25 23:37:14 | 595134d5 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-26T00"}} |
| 1910 | 2026-09-25 23:37:32 | 2e9399d2 |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "gemini-flash36", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 1911 | 2026-09-25 23:37:32 | 2e9399d2 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-li |
| 1912 | 2026-09-26 00:00:03 | fc8525b1 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1913 | 2026-09-26 00:00:03 | 1a1d091d |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-26T01"}} |
| 1914 | 2026-09-26 00:00:03 | fc8525b1 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1915 | 2026-09-26 00:37:15 | 595134d5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1916 | 2026-09-26 00:37:15 | 476304a5 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-26T01"}} |
| 1917 | 2026-09-26 00:37:30 | 595134d5 |  | model.health | fast-LAPTOP-LRE6PSA8 | {"model": "gemini-flash", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 1918 | 2026-09-26 00:37:30 | 595134d5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash", "gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite |
| 1919 | 2026-09-26 01:00:07 | 1a1d091d |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1920 | 2026-09-26 01:00:07 | 268e463f |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-26T02"}} |
| 1921 | 2026-09-26 01:00:07 | 1a1d091d |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1922 | 2026-09-26 01:12:13 | 463bbc9b |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1923 | 2026-09-26 01:12:13 | 463bbc9b |  | audit.verified | fast-LAPTOP-LRE6PSA8 | {"rows": 1921, "hashed": 1169, "first_bad": null} |
| 1924 | 2026-09-26 01:12:13 | c632d578 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-09-27"}} |
| 1925 | 2026-09-26 01:12:13 | 6e64545f |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-09-26"}} |
| 1926 | 2026-09-26 01:12:13 | 15dcb4d1 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-09-26"}} |
| 1927 | 2026-09-26 01:12:13 | 53c36786 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-09-26"}} |
| 1928 | 2026-09-26 01:12:13 | 463bbc9b |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1929 | 2026-09-26 01:12:18 | 53c36786 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1930 | 2026-09-26 01:12:18 | bfe3fe75 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1931 | 2026-09-26 01:12:18 | a0acd66c | 002 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "002", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1932 | 2026-09-26 01:12:18 | f1597a23 | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "003", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1933 | 2026-09-26 01:12:18 | 59b0d294 | 004 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "004", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1934 | 2026-09-26 01:12:18 | 767f285f | 005 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "005", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1935 | 2026-09-26 01:12:18 | 6a700484 | 006 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "006", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1936 | 2026-09-26 01:12:18 | 5a54744d | 007 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "007", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1937 | 2026-09-26 01:12:18 | 6c7820ef | 008 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "008", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1938 | 2026-09-26 01:12:18 | 7ac8fd19 | 009 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "009", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1939 | 2026-09-26 01:12:18 | 0ec08f9d | 011 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "011", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1940 | 2026-09-26 01:12:18 | 98574231 | 012 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "012", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1941 | 2026-09-26 01:12:18 | 1c3d0592 | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "013", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1942 | 2026-09-26 01:12:18 | f0a5d1b8 | 014 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "014", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1943 | 2026-09-26 01:12:18 | efaa0786 | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "016", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1944 | 2026-09-26 01:12:18 | 16882d86 | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "017", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1945 | 2026-09-26 01:12:18 | 087596d0 | 018 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "018", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1946 | 2026-09-26 01:12:18 | 1f01caca | 019 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "019", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1947 | 2026-09-26 01:12:18 | a461a21a | 020 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "020", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1948 | 2026-09-26 01:12:18 | fb4da6e3 | 021 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "021", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1949 | 2026-09-26 01:12:18 | 73874f7b | 022 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "022", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1950 | 2026-09-26 01:12:18 | 1d115db4 | 023 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "023", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1951 | 2026-09-26 01:12:18 | 8d889942 | 024 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "024", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1952 | 2026-09-26 01:12:18 | 57ca83b6 | 025 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "025", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1953 | 2026-09-26 01:12:18 | bac2335f | 026 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "026", "monitor_of": "53c3678652324baaa481371161004062", "day": "2026-09-26"}} |
| 1954 | 2026-09-26 01:12:18 | 53c36786 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "002", "003", "004", "005", "006", "007", "008", "009", "011", "012", "013", "014", "016", "017", "018", "019", "020", "021 |
| 1955 | 2026-09-26 01:12:18 | 53c36786 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 1956 | 2026-09-26 01:12:21 | bfe3fe75 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1957 | 2026-09-26 01:12:22 | a0acd66c | 002 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1958 | 2026-09-26 01:13:09 | a0acd66c | 002 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] expect='SCOUT_OK' last='SCOUT_OK' \| T2 FAIL 23s [done] expect='0.3.5' last='\u00e2\u2020\u00b3 read \u00e2\u |
| 1959 | 2026-09-26 01:13:09 | a0acd66c | 002 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 21s [done] expect='SCOUT_OK' last='SCOUT_OK' \| T2 FAIL 23s [done] expect='0.3.5' last='\u00e2\u2020\u00b3 read \u00e2\u |
| 1960 | 2026-09-26 01:13:09 | a0acd66c | 002 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1961 | 2026-09-26 01:13:09 | 0458f029 | 002 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "002", "max_rounds": 2}} |
| 1962 | 2026-09-26 01:13:09 | a0acd66c | 002 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "002", "status": "testing", "verified": "UNVERIFIED"}} |
| 1963 | 2026-09-26 01:13:14 | f1597a23 | 003 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1964 | 2026-09-26 01:14:20 | f1597a23 | 003 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='SMITH_OK' last='SMITH_OK' \| T2 FAIL 18s [done] expect='233168' last='\u00e2\u0153\u00bb Now run pyth |
| 1965 | 2026-09-26 01:14:20 | f1597a23 | 003 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='SMITH_OK' last='SMITH_OK' \| T2 FAIL 18s [done] expect='233168' last='\u00e2\u0153\u00bb Now run pyth |
| 1966 | 2026-09-26 01:14:20 | f1597a23 | 003 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1967 | 2026-09-26 01:14:20 | f3102263 | 003 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "003", "max_rounds": 2}} |
| 1968 | 2026-09-26 01:14:20 | f1597a23 | 003 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "status": "testing", "verified": "UNVERIFIED"}} |
| 1969 | 2026-09-26 01:14:24 | 59b0d294 | 004 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1970 | 2026-09-26 01:16:07 | bfe3fe75 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 22s [done] report expect='FACTORY' cmd=True \| T3 PASS 21s [d |
| 1971 | 2026-09-26 01:16:07 | bfe3fe75 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 23s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 22s [done] report expect='FACTORY' cmd=True \| T3 PASS 21s [d |
| 1972 | 2026-09-26 01:16:07 | bfe3fe75 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1973 | 2026-09-26 01:16:07 | 26dc19fc | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "bfe3fe75b6174004983684a9df120ba |
| 1974 | 2026-09-26 01:16:07 | bfe3fe75 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 1975 | 2026-09-26 01:16:11 | 0458f029 | 002 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1976 | 2026-09-26 01:16:13 | 59b0d294 | 004 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 26s [done] expect='CHANGELOG_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\004.json' \| T2 FAIL 26s [done] expec |
| 1977 | 2026-09-26 01:16:13 | 59b0d294 | 004 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 26s [done] expect='CHANGELOG_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\004.json' \| T2 FAIL 26s [done] expec |
| 1978 | 2026-09-26 01:16:13 | 59b0d294 | 004 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 1979 | 2026-09-26 01:16:13 | f0215dbb | 004 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "004", "max_rounds": 2}} |
| 1980 | 2026-09-26 01:16:13 | 59b0d294 | 004 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "004", "status": "testing", "verified": "UNVERIFIED"}} |
| 1981 | 2026-09-26 01:16:18 | 767f285f | 005 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1982 | 2026-09-26 01:16:46 | 0458f029 | 002 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-120b", "sandbox": null, "rejected": ["fallback 'or-d |
| 1983 | 2026-09-26 01:16:46 | 0458f029 | 002 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: no passing candidate in 2 rounds\nTraceback (most r |
| 1984 | 2026-09-26 01:16:50 | f3102263 | 003 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1985 | 2026-09-26 01:19:22 | 767f285f | 005 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 76s [done] expect='1' last='RESULT: 1' \| T3 PASS 79s [done] expect='0'  |
| 1986 | 2026-09-26 01:19:22 | 767f285f | 005 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 76s [done] expect='1' last='RESULT: 1' \| T3 PASS 79s [done] expect='0'  |
| 1987 | 2026-09-26 01:19:22 | 767f285f | 005 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "005", "status": "active", "verified": "VERIFIED"}} |
| 1988 | 2026-09-26 01:19:25 | 6a700484 | 006 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1989 | 2026-09-26 01:21:40 | f3102263 | 003 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 1990 | 2026-09-26 01:21:40 | f3102263 | 003 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1991 | 2026-09-26 01:21:40 | f3102263 | 003 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "status": "active"}} |
| 1992 | 2026-09-26 01:21:43 | f0215dbb | 004 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1993 | 2026-09-26 01:23:52 | 6a700484 | 006 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 47s [done] expect='2' last='RESULT: 2' \| T3 PASS 83s [done] expect='0'  |
| 1994 | 2026-09-26 01:23:52 | 6a700484 | 006 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 47s [done] expect='2' last='RESULT: 2' \| T3 PASS 83s [done] expect='0'  |
| 1995 | 2026-09-26 01:23:52 | 6a700484 | 006 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "006", "status": "active", "verified": "VERIFIED"}} |
| 1996 | 2026-09-26 01:23:55 | 5a54744d | 007 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 1997 | 2026-09-26 01:29:17 | f0215dbb | 004 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 1998 | 2026-09-26 01:29:17 | f0215dbb | 004 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 1999 | 2026-09-26 01:29:17 | f0215dbb | 004 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "004", "status": "active"}} |
| 2000 | 2026-09-26 01:29:20 | 6c7820ef | 008 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2001 | 2026-09-26 01:30:26 | 5a54744d | 007 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 50s [done] expect='X_OK' last='X_OK' \| T2 PASS 148s [done] expect='2' last='RESULT: Extracted 2 TODO/FIXME items into t |
| 2002 | 2026-09-26 01:30:26 | 5a54744d | 007 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 50s [done] expect='X_OK' last='X_OK' \| T2 PASS 148s [done] expect='2' last='RESULT: Extracted 2 TODO/FIXME items into t |
| 2003 | 2026-09-26 01:30:26 | 5a54744d | 007 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "status": "active", "verified": "VERIFIED"}} |
| 2004 | 2026-09-26 01:30:29 | 7ac8fd19 | 009 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2005 | 2026-09-26 01:33:00 | 7ac8fd19 | 009 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 29s [done] expect='3' last='RESULT: Wrote lines.txt (5 lines), deduped t |
| 2006 | 2026-09-26 01:33:00 | 7ac8fd19 | 009 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 29s [done] expect='3' last='RESULT: Wrote lines.txt (5 lines), deduped t |
| 2007 | 2026-09-26 01:33:00 | 7ac8fd19 | 009 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "009", "status": "active", "verified": "VERIFIED"}} |
| 2008 | 2026-09-26 01:33:06 | 0ec08f9d | 011 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2009 | 2026-09-26 01:34:53 | 0ec08f9d | 011 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] expect='X_OK' last='X_OK' \| T2 PASS 38s [done] expect='2' last='2' \| T3 PASS 24s [done] expect='3' last='3' |
| 2010 | 2026-09-26 01:34:53 | 0ec08f9d | 011 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 19s [done] expect='X_OK' last='X_OK' \| T2 PASS 38s [done] expect='2' last='2' \| T3 PASS 24s [done] expect='3' last='3' |
| 2011 | 2026-09-26 01:34:53 | 0ec08f9d | 011 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "011", "status": "active", "verified": "VERIFIED"}} |
| 2012 | 2026-09-26 01:34:57 | 98574231 | 012 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2013 | 2026-09-26 01:36:21 | 98574231 | 012 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] expect='X_OK' last='X_OK' \| T2 PASS 24s [done] expect='60' last='60' \| T3 PASS 21s [done] expect='22' last= |
| 2014 | 2026-09-26 01:36:21 | 98574231 | 012 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 18s [done] expect='X_OK' last='X_OK' \| T2 PASS 24s [done] expect='60' last='60' \| T3 PASS 21s [done] expect='22' last= |
| 2015 | 2026-09-26 01:36:21 | 98574231 | 012 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "012", "status": "active", "verified": "VERIFIED"}} |
| 2016 | 2026-09-26 01:36:25 | 1c3d0592 | 013 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2017 | 2026-09-26 01:37:48 | 1c3d0592 | 013 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='X_OK' last='X_OK' \| T2 PASS 20s [done] expect='1' last='RESULT: 1' \| T3 PASS 29s [done] expect='0'  |
| 2018 | 2026-09-26 01:37:48 | 1c3d0592 | 013 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='X_OK' last='X_OK' \| T2 PASS 20s [done] expect='1' last='RESULT: 1' \| T3 PASS 29s [done] expect='0'  |
| 2019 | 2026-09-26 01:37:48 | 1c3d0592 | 013 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "013", "status": "active", "verified": "VERIFIED"}} |
| 2020 | 2026-09-26 01:37:52 | 476304a5 |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2021 | 2026-09-26 01:37:52 | afc49d7c |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-26T02"}} |
| 2022 | 2026-09-26 01:38:40 | 6c7820ef | 008 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 52s [done] expect='X_OK' last='X_OK' \| T2 PASS 211s [done] expect='apple' last='RESULT: apple' \| T3 PASS 208s [done] e |
| 2023 | 2026-09-26 01:38:40 | 6c7820ef | 008 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 52s [done] expect='X_OK' last='X_OK' \| T2 PASS 211s [done] expect='apple' last='RESULT: apple' \| T3 PASS 208s [done] e |
| 2024 | 2026-09-26 01:38:40 | 6c7820ef | 008 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "008", "status": "active", "verified": "VERIFIED"}} |
| 2025 | 2026-09-26 01:38:43 | f0a5d1b8 | 014 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2026 | 2026-09-26 01:39:16 | 476304a5 |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-lite31", "groq-gptos |
| 2027 | 2026-09-26 01:39:20 | efaa0786 | 016 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2028 | 2026-09-26 01:39:58 | f0a5d1b8 | 014 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='X_OK' last='X_OK' \| T2 PASS 22s [done] expect='5' last='RESULT: 5' \| T3 PASS 17s [done] expect='Tim |
| 2029 | 2026-09-26 01:39:58 | f0a5d1b8 | 014 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='X_OK' last='X_OK' \| T2 PASS 22s [done] expect='5' last='RESULT: 5' \| T3 PASS 17s [done] expect='Tim |
| 2030 | 2026-09-26 01:39:58 | f0a5d1b8 | 014 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "014", "status": "active", "verified": "VERIFIED"}} |
| 2031 | 2026-09-26 01:40:01 | 16882d86 | 017 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2032 | 2026-09-26 01:40:42 | efaa0786 | 016 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 40s [done] expect='2' last='RESULT: 2' \| T3 PASS 14s [done] expect='3'  |
| 2033 | 2026-09-26 01:40:42 | efaa0786 | 016 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 40s [done] expect='2' last='RESULT: 2' \| T3 PASS 14s [done] expect='3'  |
| 2034 | 2026-09-26 01:40:42 | efaa0786 | 016 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "016", "status": "active", "verified": "VERIFIED"}} |
| 2035 | 2026-09-26 01:40:46 | 087596d0 | 018 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2036 | 2026-09-26 01:41:46 | 16882d86 | 017 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 28s [done] expect='3' last='RESULT: 3' \| T3 PASS 41s [done] expect='3'  |
| 2037 | 2026-09-26 01:41:46 | 16882d86 | 017 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 28s [done] expect='3' last='RESULT: 3' \| T3 PASS 41s [done] expect='3'  |
| 2038 | 2026-09-26 01:41:46 | 16882d86 | 017 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "017", "status": "active", "verified": "VERIFIED"}} |
| 2039 | 2026-09-26 01:41:49 | 1f01caca | 019 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2040 | 2026-09-26 01:42:46 | 087596d0 | 018 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 33s [done] expect='30' last='RESULT: 30' \| T3 PASS 55s [done] expect='2 |
| 2041 | 2026-09-26 01:42:46 | 087596d0 | 018 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 33s [done] expect='30' last='RESULT: 30' \| T3 PASS 55s [done] expect='2 |
| 2042 | 2026-09-26 01:42:46 | 087596d0 | 018 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "status": "active", "verified": "VERIFIED"}} |
| 2043 | 2026-09-26 01:42:50 | a461a21a | 020 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2044 | 2026-09-26 01:44:37 | 1f01caca | 019 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 44s [done] expect='1' last='RESULT: 1' \| T3 PASS 108s [done] expect='CO |
| 2045 | 2026-09-26 01:44:37 | 1f01caca | 019 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 44s [done] expect='1' last='RESULT: 1' \| T3 PASS 108s [done] expect='CO |
| 2046 | 2026-09-26 01:44:37 | 1f01caca | 019 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "019", "status": "active", "verified": "VERIFIED"}} |
| 2047 | 2026-09-26 01:44:41 | fb4da6e3 | 021 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2048 | 2026-09-26 01:46:34 | fb4da6e3 | 021 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 37s [done] expect='2' last='2' \| T3 PASS 33s [done] expect='1' last='1' |
| 2049 | 2026-09-26 01:46:34 | fb4da6e3 | 021 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 12s [done] expect='X_OK' last='X_OK' \| T2 PASS 37s [done] expect='2' last='2' \| T3 PASS 33s [done] expect='1' last='1' |
| 2050 | 2026-09-26 01:46:34 | fb4da6e3 | 021 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "021", "status": "active", "verified": "VERIFIED"}} |
| 2051 | 2026-09-26 01:46:38 | 26dc19fc | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2052 | 2026-09-26 01:46:51 | a461a21a | 020 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 20s [done] expect='X_OK' last='X_OK' \| T2 FAIL 207s [done] expect='DONE' last='\u00e2\u2020\u00b3 write files.txt' \| T |
| 2053 | 2026-09-26 01:46:51 | a461a21a | 020 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 20s [done] expect='X_OK' last='X_OK' \| T2 FAIL 207s [done] expect='DONE' last='\u00e2\u2020\u00b3 write files.txt' \| T |
| 2054 | 2026-09-26 01:46:51 | a461a21a | 020 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2055 | 2026-09-26 01:46:51 | 8fecfd97 | 020 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "020", "max_rounds": 2}} |
| 2056 | 2026-09-26 01:46:51 | a461a21a | 020 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "020", "status": "testing", "verified": "UNVERIFIED"}} |
| 2057 | 2026-09-26 01:46:55 | 73874f7b | 022 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2058 | 2026-09-26 01:47:59 | 73874f7b | 022 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='X_OK' last='X_OK' \| T2 FAIL 18s [done] expect='2' last='\u00e2\u2020\u00b3 read orders.csv' \| T3 FA |
| 2059 | 2026-09-26 01:47:59 | 73874f7b | 022 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] expect='X_OK' last='X_OK' \| T2 FAIL 18s [done] expect='2' last='\u00e2\u2020\u00b3 read orders.csv' \| T3 FA |
| 2060 | 2026-09-26 01:47:59 | 73874f7b | 022 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2061 | 2026-09-26 01:47:59 | 1262b64a | 022 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "022", "max_rounds": 2}} |
| 2062 | 2026-09-26 01:47:59 | 73874f7b | 022 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "022", "status": "testing", "verified": "UNVERIFIED"}} |
| 2063 | 2026-09-26 01:48:03 | 1d115db4 | 023 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2064 | 2026-09-26 01:49:12 | 1d115db4 | 023 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 12s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\023.json' \| T2 PASS 15s [done] expect='36.0' |
| 2065 | 2026-09-26 01:49:12 | 1d115db4 | 023 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 12s [done] expect='X_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\023.json' \| T2 PASS 15s [done] expect='36.0' |
| 2066 | 2026-09-26 01:49:12 | 1d115db4 | 023 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2067 | 2026-09-26 01:49:12 | 1a04d2e0 | 023 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "023", "max_rounds": 2}} |
| 2068 | 2026-09-26 01:49:12 | 1d115db4 | 023 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "023", "status": "testing", "verified": "UNVERIFIED"}} |
| 2069 | 2026-09-26 01:49:16 | 8d889942 | 024 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2070 | 2026-09-26 01:50:12 | 4207163b |  | job.enqueued | master-001 | {"kind": "create", "payload": {"objective": "Test weekly self-review bot"}} |
| 2071 | 2026-09-26 01:50:17 | 8d889942 | 024 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='X_OK' \| T2 PASS 22s [done] expect='2' last='2' \| T3 PASS 22s [done] expect='CONFINED' l |
| 2072 | 2026-09-26 01:50:17 | 8d889942 | 024 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='X_OK' \| T2 PASS 22s [done] expect='2' last='2' \| T3 PASS 22s [done] expect='CONFINED' l |
| 2073 | 2026-09-26 01:50:17 | 8d889942 | 024 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "024", "status": "active", "verified": "VERIFIED"}} |
| 2074 | 2026-09-26 01:50:21 | 57ca83b6 | 025 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2075 | 2026-09-26 01:50:31 | 26dc19fc | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 2076 | 2026-09-26 01:50:31 | 26dc19fc | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 14s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 18s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 2077 | 2026-09-26 01:50:31 | 26dc19fc | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2078 | 2026-09-26 01:50:31 | 9eb7524a | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "26dc19fca79c45b78edd0a01873a089 |
| 2079 | 2026-09-26 01:50:31 | 26dc19fc | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2080 | 2026-09-26 01:50:35 | 8fecfd97 | 020 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2081 | 2026-09-26 01:51:14 | 57ca83b6 | 025 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='LIVENESS_OK' last='LIVENESS_OK' \| T2 PASS 20s [done] expect='HELLO WORLD' last='RESULT: HELLO WORLD' |
| 2082 | 2026-09-26 01:51:14 | 57ca83b6 | 025 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='LIVENESS_OK' last='LIVENESS_OK' \| T2 PASS 20s [done] expect='HELLO WORLD' last='RESULT: HELLO WORLD' |
| 2083 | 2026-09-26 01:51:14 | 57ca83b6 | 025 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "025", "status": "active", "verified": "VERIFIED"}} |
| 2084 | 2026-09-26 01:51:18 | bac2335f | 026 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2085 | 2026-09-26 01:53:06 | bac2335f | 026 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] expect='X_OK' last='X_OK' \| T2 PASS 26s [done] expect='3' last='RESULT: 3' \| T3 PASS 27s [done] expect='use |
| 2086 | 2026-09-26 01:53:06 | bac2335f | 026 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 28s [done] expect='X_OK' last='X_OK' \| T2 PASS 26s [done] expect='3' last='RESULT: 3' \| T3 PASS 27s [done] expect='use |
| 2087 | 2026-09-26 01:53:06 | bac2335f | 026 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "026", "status": "active", "verified": "VERIFIED"}} |
| 2088 | 2026-09-26 01:53:26 | 8fecfd97 | 020 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 2089 | 2026-09-26 01:53:26 | 8fecfd97 | 020 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 2090 | 2026-09-26 01:53:26 | 8fecfd97 | 020 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "020", "status": "active"}} |
| 2091 | 2026-09-26 01:53:30 | 1262b64a | 022 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2092 | 2026-09-26 01:55:52 | 1262b64a | 022 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 2093 | 2026-09-26 01:55:52 | 1262b64a | 022 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 2094 | 2026-09-26 01:55:52 | 1262b64a | 022 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "022", "status": "active"}} |
| 2095 | 2026-09-26 01:55:55 | 1a04d2e0 | 023 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2096 | 2026-09-26 01:57:23 | 1a04d2e0 | 023 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": true, "status": "active", "rounds": [], "boundary_diff": {}} |
| 2097 | 2026-09-26 01:57:23 | 1a04d2e0 | 023 | bot.promoted | svc-LAPTOP-LRE6PSA8 | {"to": "active"} |
| 2098 | 2026-09-26 01:57:23 | 1a04d2e0 | 023 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "023", "status": "active"}} |
| 2099 | 2026-09-26 01:57:26 | 4207163b |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2100 | 2026-09-26 01:57:30 | 4207163b | 027 | bot.created | svc-LAPTOP-LRE6PSA8 | {"name": "self-review-bot", "tools": ["read_file", "write_file", "web_search", "web_fetch"], "permissions": ["fs:read", "fs:write", "net:sea |
| 2101 | 2026-09-26 01:58:12 | 4207163b | 027 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='X_OK' \| T2 PASS 14s [done] expect='2' last='RESULT: 2' \| T3 PASS 13s [done] expect='CON |
| 2102 | 2026-09-26 01:58:12 | 4207163b | 027 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "027", "name": "self-review-bot", "pass": 3, "total": 3, "status": "active", "verified": "VERIFIED"}} |
| 2103 | 2026-09-26 01:58:15 | 6e64545f |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2104 | 2026-09-26 01:59:53 | 6e64545f |  | lane.benchmarked | svc-LAPTOP-LRE6PSA8 | {"lane": "or-qwen27b", "result": "2/4", "quota": 2, "secs": 96} |
| 2105 | 2026-09-26 01:59:53 | 6e64545f |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"benchmarked": [["or-qwen27b", "2/4 q2"]]}} |
| 2106 | 2026-09-26 01:59:56 | 15dcb4d1 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2107 | 2026-09-26 02:00:10 | 268e463f |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2108 | 2026-09-26 02:00:10 | eeba28ae |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-26T03"}} |
| 2109 | 2026-09-26 02:00:10 | 268e463f |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2110 | 2026-09-26 02:00:56 | 15dcb4d1 |  | factory.canary | svc-LAPTOP-LRE6PSA8 | {"verdict": "FAIL", "lane": "gemini:gemini-3.1-flash-lite", "chain": ["gemini-gemini-flash-lite-latest", "gemini-lite31", "or-ling-30-flash- |
| 2111 | 2026-09-26 02:00:56 | 15dcb4d1 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"pass": 2, "total": 3}} |
| 2112 | 2026-09-27 01:58:45 | afc49d7c |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2113 | 2026-09-27 01:58:45 | 5854ee45 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "probe", "payload": {"only": [], "hour": "2026-09-27T02"}} |
| 2114 | 2026-09-27 01:58:52 | eeba28ae |  | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2115 | 2026-09-27 01:58:58 | afa33da8 | 018 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "run", "payload": {"bot_id": "018", "task": "Sum order totals per country into totals.csv", "in": "C:\\AI\\Factory\\workspace\\inbo |
| 2116 | 2026-09-27 01:58:58 |  | 018 | schedule.fired | fast-LAPTOP-LRE6PSA8 | {"sid": "5b4504d1", "fire": "2026-09-26T07:00", "job": "afa33da8"} |
| 2117 | 2026-09-27 01:59:11 | 85375329 |  | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "tick", "payload": {"hour": "2026-09-27T02"}} |
| 2118 | 2026-09-27 01:59:11 | eeba28ae |  | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2119 | 2026-09-27 01:59:16 | 9eb7524a | 001 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2120 | 2026-09-27 01:59:18 | afc49d7c |  | model.health | svc-LAPTOP-LRE6PSA8 | {"model": "or-nemotron-35-lightning", "outcome": "ok", "before": "BLOCKED", "after": "VERIFIED", "detail": null} |
| 2121 | 2026-09-27 01:59:18 | afc49d7c |  | model.retired | svc-LAPTOP-LRE6PSA8 | {"model": "or-ling-30-flash-vl", "reason": "gone: {\"error\":{\"message\":\"this model is unavailable for free. the paid version "} |
| 2122 | 2026-09-27 01:59:18 | afc49d7c |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"healthy": ["gemini-flash36", "gemini-flash38", "gemini-gemini-flash-lite-latest", "gemini-gemma26b", "gemini-lite", "gemini-li |
| 2123 | 2026-09-27 01:59:22 | afa33da8 | 018 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2124 | 2026-09-27 01:59:50 | afa33da8 | 018 | bot.ran | svc-LAPTOP-LRE6PSA8 | {"ok": true, "produced": [], "secs": 26, "reply": "\u00e2\u2020\u00b3 read orders.csv", "chain": "groq-gptoss120b"} |
| 2125 | 2026-09-27 01:59:50 | afa33da8 | 018 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "018", "name": "run", "status": "ok "}} |
| 2126 | 2026-09-27 01:59:54 | c632d578 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2127 | 2026-09-27 01:59:54 | c632d578 |  | audit.verified | svc-LAPTOP-LRE6PSA8 | {"rows": 2125, "hashed": 1373, "first_bad": null} |
| 2128 | 2026-09-27 01:59:54 | 934b7127 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "report", "payload": {"day": "2026-09-28"}} |
| 2129 | 2026-09-27 01:59:54 | 91ce36cc |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "bench", "payload": {"stale_only": true, "max": 2, "day": "2026-09-27"}} |
| 2130 | 2026-09-27 01:59:54 | dac94e57 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "canary", "payload": {"day": "2026-09-27"}} |
| 2131 | 2026-09-27 01:59:54 | 0583e758 |  | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "monitor", "payload": {"only": null, "day": "2026-09-27"}} |
| 2132 | 2026-09-27 01:59:54 | c632d578 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2133 | 2026-09-27 01:59:58 | 0583e758 |  | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2134 | 2026-09-27 01:59:58 | 84b99924 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2135 | 2026-09-27 01:59:58 | b1296d1f | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "003", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2136 | 2026-09-27 01:59:58 | d963383e | 004 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "004", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2137 | 2026-09-27 01:59:58 | 498a5257 | 005 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "005", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2138 | 2026-09-27 01:59:58 | c59bd289 | 006 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "006", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2139 | 2026-09-27 01:59:58 | 5fc85952 | 007 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "007", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2140 | 2026-09-27 01:59:58 | 70498d38 | 008 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "008", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2141 | 2026-09-27 01:59:58 | 5613a43c | 009 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "009", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2142 | 2026-09-27 01:59:58 | 3416fe9b | 011 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "011", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2143 | 2026-09-27 01:59:58 | d4c54a80 | 012 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "012", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2144 | 2026-09-27 01:59:58 | d91b2b7f | 013 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "013", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2145 | 2026-09-27 01:59:58 | e36bba9b | 014 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "014", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2146 | 2026-09-27 01:59:58 | fc5bc316 | 016 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "016", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2147 | 2026-09-27 01:59:58 | 7cdaf7c8 | 017 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "017", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2148 | 2026-09-27 01:59:58 | f2186a09 | 018 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "018", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2149 | 2026-09-27 01:59:58 | 36534eea | 019 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "019", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2150 | 2026-09-27 01:59:58 | 60f6d165 | 020 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "020", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2151 | 2026-09-27 01:59:58 | b2ce3a78 | 021 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "021", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2152 | 2026-09-27 01:59:58 | 9938d282 | 022 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "022", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2153 | 2026-09-27 01:59:58 | 80ab802c | 023 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "023", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2154 | 2026-09-27 01:59:58 | f77b5429 | 024 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "024", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2155 | 2026-09-27 01:59:58 | fab188c6 | 025 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "025", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2156 | 2026-09-27 01:59:58 | 615ea54e | 026 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "026", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2157 | 2026-09-27 01:59:58 | 399f0206 | 027 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "027", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "day": "2026-09-27"}} |
| 2158 | 2026-09-27 01:59:58 | 0583e758 |  | monitor.fanout | svc-LAPTOP-LRE6PSA8 | {"bots": ["001", "003", "004", "005", "006", "007", "008", "009", "011", "012", "013", "014", "016", "017", "018", "019", "020", "021", "022 |
| 2159 | 2026-09-27 01:59:58 | 0583e758 |  | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {}} |
| 2160 | 2026-09-27 02:00:03 | b1296d1f | 003 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2161 | 2026-09-27 02:01:04 | b1296d1f | 003 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 3s [done] expect='SMITH_OK' last='' \| T2 FAIL 17s [done] expect='233168' last='\u00e2\u2020\u00b3 $ python fizz.py' \|  |
| 2162 | 2026-09-27 02:01:04 | b1296d1f | 003 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 3s [done] expect='SMITH_OK' last='' \| T2 FAIL 17s [done] expect='233168' last='\u00e2\u2020\u00b3 $ python fizz.py' \|  |
| 2163 | 2026-09-27 02:01:04 | b1296d1f | 003 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2164 | 2026-09-27 02:01:04 | 6af00a36 | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "003", "max_rounds": 2}} |
| 2165 | 2026-09-27 02:01:04 | b1296d1f | 003 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "status": "testing", "verified": "UNVERIFIED"}} |
| 2166 | 2026-09-27 02:01:09 | 6af00a36 | 003 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2167 | 2026-09-27 02:02:11 | 6af00a36 | 003 | bot.repair | svc-LAPTOP-LRE6PSA8 | {"ok": false, "status": "testing", "rounds": [{"round": 1, "lane": "groq:openai/gpt-oss-20b", "sandbox": null, "rejected": "instructions har |
| 2168 | 2026-09-27 02:02:11 | 80c15c41 | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "rearchitect", "payload": {"bot_id": "003", "feedback": "logic: spec/tests inconsistent, tests expect a literal the instructions mu |
| 2169 | 2026-09-27 02:02:11 | 6af00a36 | 003 | bot.rearchitect_queued | svc-LAPTOP-LRE6PSA8 | {"reason": "logic: spec/tests inconsistent, tests expect a literal the instructions must mention (no passing candidate in 2 rounds)"} |
| 2170 | 2026-09-27 02:02:11 | 6af00a36 | 003 | job.failed | svc-LAPTOP-LRE6PSA8 | {"failure_class": "logic", "next_state": "paused", "attempt": 1, "error": "FactoryError: logic: spec/tests inconsistent, tests expect a lite |
| 2171 | 2026-09-27 02:02:14 | 80c15c41 | 003 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2172 | 2026-09-27 02:04:26 | 9eb7524a | 001 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 20s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 2173 | 2026-09-27 02:04:27 | 9eb7524a | 001 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 32s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 20s [done] report expect='FACTORY' cmd=True \| T3 PASS 17s [d |
| 2174 | 2026-09-27 02:04:27 | 9eb7524a | 001 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2175 | 2026-09-27 02:04:27 | e6729e00 | 001 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "53c3678652324baaa481371161004062", "retry_of": "9eb7524a860b4238ac2959a3808efcd |
| 2176 | 2026-09-27 02:04:27 | 9eb7524a | 001 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2177 | 2026-09-27 02:04:27 | 80c15c41 | 003 | bot.rearchitected | svc-LAPTOP-LRE6PSA8 | {"lane": "groq:openai/gpt-oss-20b", "tools": ["write_file", "exec"], "permissions": ["fs:write", "shell:workspace"], "boundary_diff": {"mode |
| 2178 | 2026-09-27 02:04:27 | 5bee2f1f | 003 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "003", "retest_of": "80c15c41c6114e5c9171e688978ba456", "rearchitected": true}} |
| 2179 | 2026-09-27 02:04:27 | 80c15c41 | 003 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "pass": 3, "total": 4, "status": "testing"}} |
| 2180 | 2026-09-27 02:04:32 | 5bee2f1f | 003 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2181 | 2026-09-27 02:04:32 | 84b99924 | 001 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2182 | 2026-09-27 02:05:36 | 5bee2f1f | 003 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] expect='X_OK' last='RESULT: X_OK' \| T2 FAIL 16s [done] expect='3' last='Using config: C:\\AI\\Factory\\run\\ |
| 2183 | 2026-09-27 02:05:36 | 820f6fef | 003 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "003", "retest_of": "80c15c41c6114e5c9171e688978ba456", "after_quota": "5bee2f1fc52b458b9fdc2e58267b6 |
| 2184 | 2026-09-27 02:05:36 | 5bee2f1f | 003 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "003", "status": "testing", "verified": "UNVERIFIED"}} |
| 2185 | 2026-09-27 02:05:40 | d963383e | 004 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2186 | 2026-09-27 02:07:05 | d963383e | 004 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 19s [done] expect='CHANGELOG_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\004.json' \| T2 FAIL 19s [done] expec |
| 2187 | 2026-09-27 02:07:05 | d963383e | 004 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 FAIL 19s [done] expect='CHANGELOG_OK' last='Using config: C:\\AI\\Factory\\run\\botcfg\\004.json' \| T2 FAIL 19s [done] expec |
| 2188 | 2026-09-27 02:07:05 | d963383e | 004 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2189 | 2026-09-27 02:07:05 | 510ea5e2 | 004 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "004", "max_rounds": 2}} |
| 2190 | 2026-09-27 02:07:05 | d963383e | 004 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "004", "status": "testing", "verified": "UNVERIFIED"}} |
| 2191 | 2026-09-27 02:07:09 | 498a5257 | 005 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2192 | 2026-09-27 02:08:20 | 84b99924 | 001 | bot.tested | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 15s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 2193 | 2026-09-27 02:08:20 | 84b99924 | 001 | bot.monitored | svc-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 13s [done] liveness expect='MASTER_OK' cmd=True \| T2 PASS 15s [done] report expect='FACTORY' cmd=True \| T3 PASS 18s [d |
| 2194 | 2026-09-27 02:08:20 | 84b99924 | 001 | bot.demoted | svc-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2195 | 2026-09-27 02:08:20 | fd15dd84 | 001 | job.enqueued | svc-LAPTOP-LRE6PSA8 | {"kind": "test", "payload": {"bot_id": "001", "monitor_of": "0583e758b8ba40f096402204cf0f82b0", "retry_of": "84b999246062475198d5b12e79a523c |
| 2196 | 2026-09-27 02:08:20 | 84b99924 | 001 | job.done | svc-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "001", "pass": 9, "total": 10, "status": "testing", "verified": "UNVERIFIED"}} |
| 2197 | 2026-09-27 02:08:24 | 510ea5e2 | 004 | job.claimed | svc-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2198 | 2026-09-27 02:09:31 | 498a5257 | 005 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 FAIL 50s [done] expect='1' last='\u00e2\u2020\u00b3 read data.csv' \| T3 PASS  |
| 2199 | 2026-09-27 02:09:31 | 498a5257 | 005 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 9s [done] expect='X_OK' last='X_OK' \| T2 FAIL 50s [done] expect='1' last='\u00e2\u2020\u00b3 read data.csv' \| T3 PASS  |
| 2200 | 2026-09-27 02:09:31 | 498a5257 | 005 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2201 | 2026-09-27 02:09:31 | bb708ee5 | 005 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "005", "max_rounds": 2}} |
| 2202 | 2026-09-27 02:09:31 | 498a5257 | 005 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "005", "status": "testing", "verified": "UNVERIFIED"}} |
| 2203 | 2026-09-27 02:09:36 | c59bd289 | 006 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2204 | 2026-09-27 02:11:55 | c59bd289 | 006 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] expect='X_OK' last='X_OK' \| T2 PASS 57s [done] expect='2' last='2' \| T3 PASS 50s [done] expect='0' last='0' |
| 2205 | 2026-09-27 02:11:55 | c59bd289 | 006 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 22s [done] expect='X_OK' last='X_OK' \| T2 PASS 57s [done] expect='2' last='2' \| T3 PASS 50s [done] expect='0' last='0' |
| 2206 | 2026-09-27 02:11:55 | c59bd289 | 006 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "006", "status": "active", "verified": "VERIFIED"}} |
| 2207 | 2026-09-27 02:12:00 | 5fc85952 | 007 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2208 | 2026-09-27 02:14:33 | 5fc85952 | 007 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='X_OK' \| T2 PASS 56s [done] expect='2' last='2' \| T3 PASS 55s [done] expect='0' last='0' |
| 2209 | 2026-09-27 02:14:33 | 5fc85952 | 007 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 16s [done] expect='X_OK' last='X_OK' \| T2 PASS 56s [done] expect='2' last='2' \| T3 PASS 55s [done] expect='0' last='0' |
| 2210 | 2026-09-27 02:14:33 | 5fc85952 | 007 | bot.demoted | fast-LAPTOP-LRE6PSA8 | {"to": "testing"} |
| 2211 | 2026-09-27 02:14:33 | 7efd58c0 | 007 | job.enqueued | fast-LAPTOP-LRE6PSA8 | {"kind": "repair", "payload": {"bot_id": "007", "max_rounds": 2}} |
| 2212 | 2026-09-27 02:14:33 | 5fc85952 | 007 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "007", "status": "testing", "verified": "UNVERIFIED"}} |
| 2213 | 2026-09-27 02:14:37 | 70498d38 | 008 | job.claimed | fast-LAPTOP-LRE6PSA8 | {"attempt": 1} |
| 2214 | 2026-09-27 02:16:46 | 70498d38 | 008 | bot.tested | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] expect='X_OK' last='X_OK' \| T2 PASS 42s [done] expect='apple' last='RESULT: apple' \| T3 PASS 46s [done] exp |
| 2215 | 2026-09-27 02:16:46 | 70498d38 | 008 | bot.monitored | fast-LAPTOP-LRE6PSA8 | {"result": "T1 PASS 27s [done] expect='X_OK' last='X_OK' \| T2 PASS 42s [done] expect='apple' last='RESULT: apple' \| T3 PASS 46s [done] exp |
| 2216 | 2026-09-27 02:16:46 | 70498d38 | 008 | job.done | fast-LAPTOP-LRE6PSA8 | {"summary": {"bot_id": "008", "status": "active", "verified": "VERIFIED"}} |
