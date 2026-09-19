import os,json,urllib.request,time,sys
def post(url,hdr,body):
    r=urllib.request.Request(url,data=json.dumps(body).encode(),headers={**hdr,"Content-Type":"application/json"})
    t=time.time()
    try:
        with urllib.request.urlopen(r,timeout=60) as f: d=json.load(f); return time.time()-t,d,None
    except urllib.error.HTTPError as e: return time.time()-t,None,f"{e.code} {e.read()[:300].decode(errors='replace')}"
    except Exception as e: return time.time()-t,None,repr(e)
tools=[{"type":"function","function":{"name":"echo","description":"echo text","parameters":{"type":"object","properties":{"text":{"type":"string"}},"required":["text"]}}}]
msgs=[{"role":"user","content":"Call the echo tool with text LANE_OK. Do not answer in prose."}]
g=os.environ.get("GEMINI_API_KEY"); o=os.environ.get("OPENROUTER_API_KEY")
for m in ["gemini-2.5-flash","gemini-2.5-flash-lite","gemini-2.0-flash"]:
    dt,d,err=post("https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",{"Authorization":f"Bearer {g}"},{"model":m,"messages":msgs,"tools":tools})
    tc=d and d["choices"][0]["message"].get("tool_calls")
    print(f"gemini {m:28s} {dt:4.1f}s tool_call={bool(tc)} {'' if not err else err[:200]}")
r=urllib.request.Request("https://openrouter.ai/api/v1/models",headers={"Authorization":f"Bearer {o}"})
free=[x for x in json.load(urllib.request.urlopen(r,timeout=60))["data"] if x["id"].endswith(":free") and "tools" in (x.get("supported_parameters") or [])]
free.sort(key=lambda x:-(x.get("context_length") or 0))
print("openrouter :free tool-capable:",len(free)); print([x["id"] for x in free[:15]])
for m in [x["id"] for x in free[:6]]:
    dt,d,err=post("https://openrouter.ai/api/v1/chat/completions",{"Authorization":f"Bearer {o}"},{"model":m,"messages":msgs,"tools":tools})
    tc=d and d["choices"][0]["message"].get("tool_calls")
    print(f"openrouter {m:45s} {dt:4.1f}s tool_call={bool(tc)} {'' if not err else err[:160]}")
