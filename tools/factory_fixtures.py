"""factory_fixtures.py — D-111: materialise a bot's declared test fixtures into its workspace.

  python tools/factory_fixtures.py <bot_dir>     → writes each spec fixture (text or SQLite-from-SQL); prints JSON

Called by run-bot-tests.ps1 before EVERY test (the artefact sweep removes workspace files after each test). Fixtures
are declared in bot.json (spec.fixtures, validated by botspec: plain filename, ≤4 files, ≤4 KB, text XOR sql).
Never overwrites bundle files; refuses names that resolve outside the workspace.
"""
from __future__ import annotations
import json, pathlib, sqlite3, sys

BUNDLE = {"AGENTS.md", "SOUL.md", "TESTS.md", "RECOVERY.md", "TEST_RESULTS.md", "HEARTBEAT.md", "USER.md", "bot.json", "nanobot.patch.json", ".gitignore"}


def materialise(bot_dir: pathlib.Path, fixtures: list[dict] | None = None) -> dict:
    bot_dir = pathlib.Path(bot_dir)
    if fixtures is None:
        fixtures = (json.loads((bot_dir / "bot.json").read_text(encoding="utf-8")).get("fixtures") or [])
    written, skipped = [], []
    for f in fixtures[:4]:
        name = str(f.get("name", ""))
        dest = (bot_dir / name)
        if not name or "/" in name or "\\" in name or name in BUNDLE or dest.resolve().parent != bot_dir.resolve():
            skipped.append(name); continue
        if dest.exists():
            try: dest.unlink()
            except PermissionError:                      # Windows: a previous test's server still holds the file
                skipped.append(name + " (locked)"); continue
        if "sql" in f:
            con = sqlite3.connect(dest)
            try: con.executescript(str(f["sql"])[:4096]); con.commit()
            finally: con.close()
        else:
            dest.write_text(str(f.get("text", ""))[:4096], encoding="utf-8")
        written.append(name)
    return {"written": written, "skipped": skipped}


if __name__ == "__main__":
    print(json.dumps(materialise(pathlib.Path(sys.argv[1]))))
