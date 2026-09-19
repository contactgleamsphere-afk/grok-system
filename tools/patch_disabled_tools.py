import pathlib,shutil
p=pathlib.Path(r"C:\AI\Factory\.venv\Lib\site-packages\nanobot\agent\tools\loader.py")
s=p.read_text(encoding="utf-8")
old='''                    if not tool_cls.enabled(ctx):
                        continue
                    tool = tool_cls.create(ctx)'''
new='''                    if not tool_cls.enabled(ctx):
                        continue
                    tool = tool_cls.create(ctx)
                    # AI-Factory patch (2026-09-19): allow trimming the tool set via env
                    # AIFACTORY_DISABLED_TOOLS="a,b,c" to cut prompt tokens for small-TPM lanes.
                    if tool.name in _aifactory_disabled():
                        continue'''
helper='''
import os as _os
def _aifactory_disabled() -> set[str]:
    return {t.strip() for t in _os.environ.get("AIFACTORY_DISABLED_TOOLS", "").split(",") if t.strip()}

'''
if "_aifactory_disabled" in s: print("already patched")
elif old in s:
    shutil.copy(p,str(p)+".orig-0.3.5"); s=s.replace(old,new).replace("\nclass ToolLoader:",helper+"\nclass ToolLoader:",1); p.write_text(s,encoding="utf-8"); print("patched loader")
else: print("PATTERN NOT FOUND"); raise SystemExit(1)
