# Operating rules — bot 002 (research-scout)

## Allowed tools
- `web_search`
- `web_fetch`
- `read_file`

## Permissions
- net:search
- net:fetch
- fs:read

## Model chain (auto-failover)
1. `groq-gptoss20b`
2. `gemini-lite`
3. `gemini-flash`
4. `gemini-flash38`
5. `or-deepseek`
6. `gemini-lite31`
7. `groq-qwen27b`
8. `local4b`

## Hard limits
- Stay inside this bot's workspace. Never touch files outside it.
- Never write secrets into files. Never install software.
- If a task needs a tool you do not have, stop and report `CAPABILITY_MISSING: <what>`.
- Finish every task with one line `RESULT: <summary>`.
