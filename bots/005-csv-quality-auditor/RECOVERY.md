# Recovery — bot 005

- Bundle: `C:\AI\Factory\bots\005-csv-quality-auditor` (regenerate with `python tools/factory_cli.py build <spec.json> --overwrite`).
- Rollback: delete the bundle dir and remove the entry from registry/bots.json; nothing else is touched.
- If the primary model is down the chain fails over automatically; if all remote lanes are down the bot runs on the local model (slow).
- Memory lives only in `memory/MEMORY.md` inside the bundle.
