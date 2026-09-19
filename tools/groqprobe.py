import os,urllib.request,json,time
k=os.environ.get("GROQ_API_KEY","")
print("key len",len(k),"prefix",k[:4])
H={"Content-Type":"application/json","Authorization":"Bearer "+k,"User-Agent":"ai-factory-probe/1.0"}
r=urllib.request.urlopen(urllib.request.Request("https://api.groq.com/openai/v1/models",headers=H),timeout=30)
ids=sorted(m["id"] for m in json.load(r)["data"]); print("models:",len(ids)); print([i for i in ids if "llama-3.3" in i or "gpt-oss" in i or "qwen" in i or "kimi" in i])
tools=[{"type":"function","function":{"name":"get_time","description":"Get current time in a city","parameters":{"type":"object","properties":{"city":{"type":"string"}},"required":["city"]}}}]
for m in ["llama-3.3-70b-versatile","openai/gpt-oss-120b"]:
    t=time.time()
    req=urllib.request.Request("https://api.groq.com/openai/v1/chat/completions",data=json.dumps({"model":m,"messages":[{"role":"user","content":"What time is it in Paris? Use the tool."}],"tools":tools,"max_tokens":200}).encode(),headers=H)
    try:
        d=json.load(urllib.request.urlopen(req,timeout=60)); msg=d["choices"][0]["message"]
        print(m, "tool_calls" if msg.get("tool_calls") else "TEXT", json.dumps(msg.get("tool_calls",[{}])[0].get("function")) if msg.get("tool_calls") else msg.get("content","")[:80], f"{time.time()-t:.1f}s")
    except urllib.error.HTTPError as e: print(m,"HTTP",e.code,e.read()[:200])
