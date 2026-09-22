"""Mirror registry models into nanobot modelPresets (D-048). Never touches providers/keys. Removes presets for models
the registry has BLOCKED so nanobot can never route to a dead lane. Returns (added, removed).

  python tools/factory_presets.py [--dry-run]
"""
from __future__ import annotations
import json, os, sys, pathlib, shutil, time
ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core"))
from factory.registry import Registry  # noqa: E402
CONFIG = pathlib.Path(os.environ.get("AIFACTORY_CONFIG", r"C:\AI\Factory\config.json"))
SMALL_TPM = {"groq": (8200, 768)}     # provider -> (contextWindowTokens, maxTokens) for 8k-TPM free tiers


def sync(config_path: pathlib.Path = CONFIG, dry_run: bool = False) -> tuple[list[str], list[str]]:
    reg = Registry(ROOT / "registry")
    c = json.loads(config_path.read_text(encoding="utf-8"))
    presets = c.setdefault("modelPresets", {})
    added, removed = [], []
    known = {m.id for m in reg.all("models")}
    for pid in list(presets):        # presets not backed by any registry entry are stale (e.g. old failover-test stubs)
        if pid not in known and presets[pid].get("provider") in ("groq", "gemini", "openrouter", "custom"):
            presets.pop(pid); removed.append(pid)
    for m in reg.all("models"):
        if m.verified == "BLOCKED":                      # any provider: a BLOCKED lane must not be routable
            if m.id in presets: presets.pop(m.id); removed.append(m.id)
            continue
        if m.provider not in ("groq", "gemini", "openrouter"): continue   # auto-ADD only for keyed providers we probe
        if m.id not in presets:
            ctx, mx = SMALL_TPM.get(m.provider, (32768, 2048))
            presets[m.id] = {"model": m.model, "provider": m.provider, "maxTokens": mx, "contextWindowTokens": ctx, "temperature": 0.2}
            added.append(m.id)
    # D-062: the master's own chain follows the same policy as every child bot (bench-ranked primary within budget,
    # cross-provider fallbacks, local tail) instead of a hand-wired list that strands it when one provider's day quota ends.
    chain_changed = False
    try:
        sys.path.insert(0, str(ROOT / "tools")); import factory_pipeline as fp
        primary = fp.default_primary(reg); fallbacks = fp.default_fallbacks(reg, primary)
        loc = [m for m in reg.all("models") if m.location == "local" and m.verified != "BLOCKED" and m.id in presets]
        if loc and not any(f in {m.id for m in loc} for f in fallbacks): fallbacks.append(loc[0].id)
        d = c.setdefault("agents", {}).setdefault("defaults", {})
        if primary in presets and (d.get("modelPreset") != primary or d.get("fallbackModels") != fallbacks):
            d["modelPreset"], d["fallbackModels"] = primary, [f for f in fallbacks if f in presets]; chain_changed = True
    except Exception:
        pass
    if (added or removed or chain_changed) and not dry_run:
        shutil.copy(config_path, config_path.with_suffix(f".bak-{time.strftime('%Y%m%d%H%M%S')}"))
        config_path.write_text(json.dumps(c, indent=2, ensure_ascii=False), encoding="utf-8")
    if chain_changed: added.append(f"master-chain:{c['agents']['defaults']['modelPreset']}>{','.join(c['agents']['defaults']['fallbackModels'])}")
    return added, removed


if __name__ == "__main__":
    print(json.dumps(dict(zip(("added", "removed"), sync(dry_run="--dry-run" in sys.argv)))))
