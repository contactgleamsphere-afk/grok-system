import pathlib,shutil,re
p=pathlib.Path(r"C:\AI\Factory\.venv\Lib\site-packages\nanobot\providers\fallback_provider.py")
s=p.read_text(encoding="utf-8")
old='''        """Turn provider exceptions into error responses without swallowing cancellation."""
        try:
            return await call(provider, kwargs), None
        except asyncio.CancelledError:
            raise
        except Exception as exc:'''
new='''        """Turn provider exceptions into error responses without swallowing cancellation."""
        # AI-Factory patch D-017 (2026-09-19): quota-aware lane retry.
        # Small free tiers (Groq 8k TPM) reset in <10s; waiting beats dropping to a slow local model.
        try:
            for _attempt in range(int(_os.environ.get("AIFACTORY_QUOTA_RETRIES", "3")) + 1):
                response = await call(provider, kwargs)
                if response.finish_reason != "error":
                    return response, None
                text = (response.content or "").lower()
                status = response.error_status_code
                if not (status in (413, 429) or "rate limit" in text or "rate_limit" in text):
                    return response, None
                wait = LLMProvider._extract_retry_after_from_response(response)
                if wait is None:
                    m = re.search(r"try again in ([0-9.]+)\\s*(ms|s|m)", text)
                    if m:
                        v = float(m.group(1)); wait = v / 1000 if m.group(2) == "ms" else v * 60 if m.group(2) == "m" else v
                # daily-quota exhaustion (Groq TPD/RPD): waiting is pointless -> rotate lane now
                if "per day" in text or "tpd" in text or "rpd" in text or (wait is not None and wait > 60):
                    logger.warning("quota-aware retry: '{}' daily quota exhausted, rotating lane", kwargs.get("model") or provider.get_default_model())
                    return response, None
                if wait is None:
                    wait = 4.0
                if wait > float(_os.environ.get("AIFACTORY_QUOTA_MAX_WAIT", "20")):
                    return response, None
                logger.warning("quota-aware retry: '{}' rate-limited, waiting {:.1f}s (attempt {})", kwargs.get("model") or provider.get_default_model(), wait + 0.5, _attempt + 1)
                await asyncio.sleep(wait + 0.5)
            return response, None
        except asyncio.CancelledError:
            raise
        except Exception as exc:'''
if "daily quota exhausted" in s: print("already patched"); raise SystemExit(0)
if "AI-Factory patch D-017" in s:
    # replace the previous D-017 block in place (keeps other patches intact)
    start=s.index('        """Turn provider exceptions into error responses without swallowing cancellation."""')
    end=s.index("        except Exception as exc:", start)
    s=s[:start]+new+s[end+len("        except Exception as exc:"):]
    p.write_text(s,encoding="utf-8"); print("re-patched D-017 in place"); raise SystemExit(0)
elif old in s:
    if not pathlib.Path(str(p)+".orig-0.3.5").exists(): shutil.copy(p,str(p)+".orig-0.3.5")
    s=s.replace(old,new)
    if "import os as _os" not in s: s=s.replace("import asyncio\n","import asyncio\nimport os as _os\nimport re\n",1)
    p.write_text(s,encoding="utf-8"); print("patched quota-aware retry")
else: print("PATTERN NOT FOUND"); raise SystemExit(1)
