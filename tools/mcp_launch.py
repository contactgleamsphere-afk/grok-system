"""mcp_launch.py — D-112: start an owner-approved MCP server *inside* a bot's workspace.

  python tools/mcp_launch.py <bot_dir> -- <command> [args...]

nanobot spawns MCP servers with its own cwd, so a relative path like "fixture.db" was created next to nanobot instead
of being read from the bot workspace (bot 026, 2026-09-24). This launcher chdir()s into the bot directory, strips
secrets from the environment (servers get no API keys unless the owner adds them explicitly) and execs the server
with stdio inherited. Confinement note (INFERRED): this fixes relative paths; it does NOT stop a server that is
handed an absolute path outside the workspace — hence such servers stay risk=high and need an explicit grant.
"""
from __future__ import annotations
import os, re, subprocess, sys


def main(argv: list[str]) -> int:
    if len(argv) < 3 or "--" not in argv:
        print(__doc__); return 2
    bot_dir = argv[0]; cmd = argv[argv.index("--") + 1:]
    os.chdir(bot_dir)
    env = {k: v for k, v in os.environ.items() if not re.search(r"KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL", k, re.I)}
    env["AIFACTORY_BOT_DIR"] = bot_dir
    p = subprocess.Popen(cmd, cwd=bot_dir, env=env)          # stdin/stdout inherited → MCP stdio passes straight through
    try:
        return p.wait()
    except KeyboardInterrupt:
        p.terminate(); return 130


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
