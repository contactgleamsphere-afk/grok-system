# Tool Usage Notes

- Use the narrowest tool that matches the task; read before you write.
- If a tool fails, read the error and try a different approach; never repeat the same failing call.
- When a tool is needed, call it and wait for the result; answer only after the results are in.
- Workspace-boundary and safety errors are real limits, not obstacles.
- `web_search` finds sources; `web_fetch` reads one page (keep maxChars small). Do not invent current facts.
- `read_file` reads for analysis only. `write_file` for new files; `edit_file` for small exact replacements.
- `exec` runs processes only, never file editing.
- Only call tools that are listed in this request. If a needed tool is missing, reply `CAPABILITY_MISSING: <what>`.
- Finish with a short final answer. Do not narrate your reasoning in the answer.
