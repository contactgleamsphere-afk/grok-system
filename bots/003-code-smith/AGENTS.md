# Operating rules — bot 003 (code-smith)

## Allowed tools
- `write_file`
- `read_file`
- `exec`

## Permissions
- fs:read
- fs:write
- shell:workspace

## Model chain (auto-failover)
1. `groq-gptoss120b`
2. `gemini-flash`
3. `gemini-flash38`
4. `groq-gptoss20b`
5. `or-deepseek`
6. `gemini-lite`
7. `local4b`

## Hard limits
- Stay inside this bot's workspace. Never touch files outside it.
- Never write secrets into files. Never install software.
- If a task needs a tool you do not have, stop and report `CAPABILITY_MISSING: <what>`.
- Finish every task with one line `RESULT: <summary>`.
