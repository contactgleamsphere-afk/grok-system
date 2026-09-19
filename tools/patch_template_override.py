"""AI-Factory patch D-020: let a bot bundle override nanobot prompt templates.
If env AIFACTORY_TEMPLATE_DIR is set, Jinja looks there first, then in nanobot/templates.
Idempotent. Original kept as .orig-0.3.5."""
import pathlib, shutil
p = pathlib.Path(r"C:\AI\Factory\.venv\Lib\site-packages\nanobot\utils\prompt_templates.py")
s = p.read_text(encoding="utf-8")
if "AIFACTORY_TEMPLATE_DIR" in s:
    print("already patched"); raise SystemExit(0)
old = "        loader=FileSystemLoader(str(_TEMPLATES_ROOT)),"
new = ("        # AI-Factory patch D-020: per-bot template overrides (AIFACTORY_TEMPLATE_DIR searched first)\n"
       "        loader=FileSystemLoader([d for d in [__import__('os').environ.get('AIFACTORY_TEMPLATE_DIR', ''), str(_TEMPLATES_ROOT)] if d]),")
if old not in s:
    print("PATTERN NOT FOUND"); raise SystemExit(1)
if not pathlib.Path(str(p) + ".orig-0.3.5").exists():
    shutil.copy(p, str(p) + ".orig-0.3.5")
p.write_text(s.replace(old, new), encoding="utf-8"); print("patched template override")
