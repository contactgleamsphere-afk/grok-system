import os,json,urllib.request,time
k=os.environ["GROQ_API_KEY"]
tools=[{"type":"function","function":{"name":"echo","description":"echo text","parameters":{"type":"object","properties":{"text":{"type":"string"}},"required":["text"]}}}]
for m in ["openai/gpt-oss-120b","openai/gpt-oss-20b"]:
    ok=0;ts=[]
    for i in range(5):
        r=urllib.request.Request("https://api.groq.com/openai/v1/chat/completions",data=json.dumps({"model":m,"messages":[{"role":"user","content":f"Call the echo tool with text BENCH_{i}. No prose."}],"tools":tools,"max_tokens":200}).encode(),headers={"Authorization":f"Bearer {k}","Content-Type":"application/json","User-Agent":"aifactory-bench/1.0"})
        t=time.time()
        try:
            d=json.load(urllib.request.urlopen(r,timeout=60)); tc=d["choices"][0]["message"].get("tool_calls"); ok+=bool(tc and f"BENCH_{i}" in tc[0]["function"]["arguments"])
        except Exception as e: print("  err",m,str(e)[:120])
        ts.append(round(time.time()-t,2))
    print(f"{m} tool_calls={ok}/5 latency={ts}")
