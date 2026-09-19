import os,json,urllib.request,time
def h(k): v=os.environ.get(k) or ""; return f"{k}: present len={len(v)}" if v else f"{k}: MISSING"
for k in ("GROQ_API_KEY","GEMINI_API_KEY","OPENROUTER_API_KEY"): print(h(k))
tools=[{"type":"function","function":{"name":"echo","description":"echo text","parameters":{"type":"object","properties":{"text":{"type":"string"}},"required":["text"]}}}]
def probe(name,url,key,model):
    r=urllib.request.Request(url,data=json.dumps({"model":model,"messages":[{"role":"user","content":"Call echo with text PING. No prose."}],"tools":tools,"max_tokens":64}).encode(),headers={"Authorization":f"Bearer {key}","Content-Type":"application/json","User-Agent":"aifactory-probe/1.0"})
    t=time.time()
    try:
        d=json.load(urllib.request.urlopen(r,timeout=60)); tc=d["choices"][0]["message"].get("tool_calls"); print(f"{name:11s} {model:40s} tool_call={bool(tc)} {time.time()-t:.1f}s")
    except urllib.error.HTTPError as e: print(f"{name:11s} {model:40s} HTTP {e.code}: {e.read()[:140].decode(errors='replace').replace(chr(10),' ')}")
probe("gemini","https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",os.environ["GEMINI_API_KEY"],"gemini-3.6-flash")
probe("openrouter","https://openrouter.ai/api/v1/chat/completions",os.environ["OPENROUTER_API_KEY"],"deepseek/deepseek-v4-flash-0731:free")
r=urllib.request.Request("https://openrouter.ai/api/v1/key",headers={"Authorization":f"Bearer {os.environ['OPENROUTER_API_KEY']}"}); print("openrouter free quota:",json.load(urllib.request.urlopen(r))["data"]["free_model_daily_requests"])
