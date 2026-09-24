"""Print the live model chain for a bot (D-040): bot.json model_policy re-resolved against the CURRENT registry
(BLOCKED lanes dropped, quota-cooled lanes skipped, local tail guaranteed). Used by run-bot-tests.ps1 so deployed
bots follow lane health without rewriting their bundles. Falls back to the frozen resolved_chain on any error.

  python tools/factory_chain.py <bot_dir>      -> {"primary": "...", "fallbacks": [...], "source": "live|frozen"}
"""
from __future__ import annotations
import json, os, sys, pathlib
ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core"))


def live_chain(bot_dir: pathlib.Path) -> dict:
    spec = json.loads((bot_dir / "bot.json").read_text(encoding="utf-8"))
    frozen = spec.get("resolved_chain") or []
    try:
        from factory.registry import Registry
        from factory.factory import BotFactory
        f = BotFactory(Registry(ROOT / "registry"), bot_dir.parent)
        chain = f.resolve_chain(spec["model_policy"])
        src = "live+topup:" + ",".join(f.last_topup) if getattr(f, "last_topup", None) else "live"   # D-103
    except Exception:
        chain, src = frozen, "frozen"
    if not chain:
        chain, src = frozen, "frozen"
    return {"primary": chain[0], "fallbacks": chain[1:], "source": src, "frozen": frozen}


if __name__ == "__main__":
    print(json.dumps(live_chain(pathlib.Path(sys.argv[1]))))
