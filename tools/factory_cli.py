"""AI Factory CLI.
  python tools/factory_cli.py build <spec.json> [--overwrite] [--bots-root DIR] [--registry DIR]
  python tools/factory_cli.py validate <spec.json>
  python tools/factory_cli.py record <bot_id> <passed> <total> "<evidence>"
  python tools/factory_cli.py tests <bot_id>        # print prompt/expected pairs as JSON
"""
import json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "core"))
from factory.registry import Registry
from factory.botspec import validate_spec
from factory.factory import BotFactory, parse_tests

def main(argv):
    if len(argv) < 2: print(__doc__); return 2
    reg_dir = ROOT / "registry"; bots_root = ROOT / "bots"
    if "--registry" in argv: reg_dir = pathlib.Path(argv[argv.index("--registry") + 1])
    if "--bots-root" in argv: bots_root = pathlib.Path(argv[argv.index("--bots-root") + 1])
    reg = Registry(reg_dir); f = BotFactory(reg, bots_root)
    cmd = argv[1]
    if cmd == "validate":
        spec = json.loads(pathlib.Path(argv[2]).read_text(encoding="utf-8"))
        p = validate_spec(spec, reg); print("\n".join(p) if p else "OK"); return 1 if p else 0
    if cmd == "build":
        spec = json.loads(pathlib.Path(argv[2]).read_text(encoding="utf-8"))
        r = f.build(spec, overwrite="--overwrite" in argv)
        print(json.dumps({"bot_dir": str(r.bot_dir), "chain": r.chain, "disabled_tools": r.disabled_tools, "files": r.files}, indent=1)); return 0
    if cmd == "record":
        e = f.record_test_result(argv[2], int(argv[3]), int(argv[4]), argv[5] if len(argv) > 5 else "")
        print(e.id, e.status, e.verified); return 0
    if cmd == "tests":
        e = reg.get("bots", argv[2]); print(json.dumps(parse_tests(e.tests))); return 0
    print(__doc__); return 2

if __name__ == "__main__":
    sys.exit(main(sys.argv))
