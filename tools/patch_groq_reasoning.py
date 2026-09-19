import re,pathlib,shutil
p=pathlib.Path(r"C:\AI\Factory\.venv\Lib\site-packages\nanobot\providers\registry.py")
s=p.read_text(encoding="utf-8")
old='''        name="groq",
        keywords=("groq",),
        env_key="GROQ_API_KEY",
        display_name="Groq",
        backend="openai_compat",
        default_api_base="https://api.groq.com/openai/v1",
    ),'''
new='''        name="groq",
        keywords=("groq",),
        env_key="GROQ_API_KEY",
        display_name="Groq",
        backend="openai_compat",
        default_api_base="https://api.groq.com/openai/v1",
        # AI-Factory patch (2026-09-19): Groq 400s on assistant history that
        # carries reasoning_content ("property 'reasoning_content' is unsupported").
        strip_history_reasoning_content=True,
    ),'''
if new in s: print("already patched")
elif old in s:
    shutil.copy(p, str(p)+".orig-0.3.5"); p.write_text(s.replace(old,new),encoding="utf-8"); print("patched")
else: print("PATTERN NOT FOUND"); raise SystemExit(1)
