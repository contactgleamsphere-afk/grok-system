# BOT_REGISTRY

| id | name | status | verified | chain | tools | last test |
|---|---|---|---|---|---|---|
| 001 | master | active | VERIFIED | local3b | exec, read_file, write_file, web_search, web_fetch | tests 4/4: T1 PASS 11s [done] liveness expect='MASTER_OK' cmd=True | T2 PASS 85s |
| 002 | research-scout | active | VERIFIED | groq-gptoss20b > gemini-lite > gemini-flash > gemini-flash38 > or-deepseek > gemini-lite31 > groq-qwen27b > local4b | web_search, web_fetch, read_file | tests 2/2: T1 PASS 10s [done] expect='SCOUT_OK' last='SCOUT_OK' | T2 PASS 124s [ |
| 003 | code-smith | active | VERIFIED | groq-gptoss120b > gemini-flash > gemini-flash38 > groq-gptoss20b > or-deepseek > gemini-lite > local4b | write_file, read_file, exec | tests 4/4: T1 PASS 10s [done] expect='SMITH_OK' last='SMITH_OK' | T2 PASS 98s [d |
| 004 | changelog-writer | active | VERIFIED | groq-gptoss120b > gemini-flash > gemini-flash38 > groq-gptoss20b > or-deepseek > gemini-lite > local4b | read_file, write_file | tests 4/4: T1 PASS 11s [done] expect='CHANGELOG_OK' last='CHANGELOG_OK' | T2 PAS |
| 005 | csv-quality-auditor | active | VERIFIED | groq-gptoss120b > gemini-flash > gemini-flash38 > groq-gptoss20b > or-deepseek > gemini-lite > local4b | read_file, write_file | tests 4/4: monitor 2026-09-20: T1 PASS 66s [done] expect='X_OK' last='X_OK' | T2 |
| 006 | json-to-markdown-table | active | VERIFIED | groq-gptoss120b > gemini-flash > gemini-flash38 > groq-gptoss20b > or-deepseek > gemini-lite > local4b | read_file, write_file | tests 4/4: T1 PASS 10s [done] expect='X_OK' last='X_OK' | T2 PASS 35s [done] exp |
| 007 | todo-extractor | active | VERIFIED | groq-gptoss120b > gemini-flash > gemini-flash38 > groq-gptoss20b > or-deepseek > gemini-lite > local4b | read_file, write_file | tests 4/4: monitor 2026-09-21: T1 PASS 55s [done] expect='X_OK' last='X_OK' | T2 |
| 008 | word-frequency-bot | active | VERIFIED | groq-gptoss120b > gemini-flash > gemini-flash38 > groq-gptoss20b > or-deepseek > gemini-lite > local4b | read_file, write_file | tests 4/4: monitor 2026-09-21: T1 PASS 50s [done] expect='X_OK' last='X_OK' | T2 |
| 009 | line-dedupe-bot | active | VERIFIED | groq-gptoss120b > groq-gptoss20b > groq-qwen27b > gemini-flash > gemini-flash38 > gemini-gemma26b > local3b | read_file, write_file | tests 4/4: T1 PASS 10s [done] expect='X_OK' last='X_OK' | T2 PASS 29s [done] exp |
