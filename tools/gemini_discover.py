import os,json,urllib.request,time,re
g=os.environ["GEMINI_API_KEY"]
r=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models?key={g}")
ms=[m["name"].split("/")[1] for m in json.load(urllib.request.urlopen(r,timeout=60))["models"] if "generateContent" in m.get("supportedGenerationMethods",[])]
cands=[m for m in ms if re.search(r"flash|lite|gemma",m) and not re.search(r"tts|image|audio|omni|live|embedding",m)]
tools=[{"type":"function","function":{"name":"echo","description":"echo text","parameters":{"type":"object","properties":{"text":{"type":"string"}},"required":["text"]}}}]
for m in cands:
    r=urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",data=json.dumps({"model":m,"messages":[{"role":"user","content":"Call echo with text PING. No prose."}],"tools":tools,"max_tokens":64}).encode(),headers={"Authorization":f"Bearer {g}","Content-Type":"application/json"})
    t=time.time()
    try:
        d=json.load(urllib.request.urlopen(r,timeout=45)); tc=d["choices"][0]["message"].get("tool_calls"); print(f"OK   {m:34s} tool_call={bool(tc)} {time.time()-t:.1f}s")
    except urllib.error.HTTPError as e:
        b=e.read().decode(errors="replace"); q=re.findall(r'"quotaId":\s*"([^"]+)"|"quotaValue":\s*"([^"]+)"|retry in ([0-9.]+s)',b)
        print(f"{e.code}  {m:34s} {[x for t in q for x in t if x][:4]}")
    except Exception as e: print("ERR ",m,str(e)[:80])
