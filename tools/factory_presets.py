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
    if (added or removed) and not dry_run:
        shutil.copy(config_path, config_path.with_suffix(f".bak-{time.strftime('%Y%m%d%H%M%S')}"))
        config_path.write_text(json.dumps(c, indent=2, ensure_ascii=False), encoding="utf-8")
    return added, removed


if __name__ == "__main__":
    print(json.dumps(dict(zip(("added", "removed"), sync(dry_run="--dry-run" in sys.argv)))))
