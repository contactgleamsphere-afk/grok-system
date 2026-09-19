import pathlib,shutil
p=pathlib.Path(r"C:\AI\Factory\.venv\Lib\site-packages\nanobot\providers\fallback_provider.py")
s=p.read_text(encoding="utf-8")
old='''        if kind in _NON_FALLBACK_ERROR_KINDS:
            return False
        if any(
            token in value
            for value in structured_values
            for token in _NON_FALLBACK_ERROR_KINDS
        ):
            return False
        if status in {401, 403}:'''
new='''        # AI-Factory patch (2026-09-19): Groq reports per-minute token caps as
        # HTTP 413 / type=invalid_request_error / code=rate_limit_exceeded.
        # That is a quota condition, not a bad request -> fall back.
        if status == 413 or "rate_limit" in code or "rate_limit" in text[:400]:
            return True
        # model emitted an invalid/hallucinated tool call -> another model may do better
        if "tool_use_failed" in code or "tool call validation failed" in text[:400]:
            return True
        if kind in _NON_FALLBACK_ERROR_KINDS:
            return False
        if any(
            token in value
            for value in structured_values
            for token in _NON_FALLBACK_ERROR_KINDS
        ):
            return False
        if status in {401, 403}:'''
if "tool call validation failed" in s: print("already patched")
elif "AI-Factory patch (2026-09-19): Groq reports" in s:
    s=s.replace('''        if status == 413 or "rate_limit" in code or "rate_limit" in text[:400]:
            return True''', '''        if status == 413 or "rate_limit" in code or "rate_limit" in text[:400]:
            return True
        # model emitted an invalid/hallucinated tool call -> another model may do better
        if "tool_use_failed" in code or "tool call validation failed" in text[:400]:
            return True'''); p.write_text(s,encoding="utf-8"); print("extended 413 patch with tool_use_failed")
elif old in s: shutil.copy(p,str(p)+".orig-0.3.5"); p.write_text(s.replace(old,new),encoding="utf-8"); print("patched fallback_provider")
else: print("PATTERN NOT FOUND"); raise SystemExit(1)
