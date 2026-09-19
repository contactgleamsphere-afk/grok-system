import urllib.request,json,time
for m in ["gpt-oss-20b","Mistral-Small-3.2-24B-Instruct-2506"]:
    t=time.time()
    req=urllib.request.Request("https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/chat/completions",data=json.dumps({"model":m,"messages":[{"role":"user","content":"Reply with exactly: OK"}],"max_tokens":8}).encode(),headers={"Content-Type":"application/json","Authorization":"Bearer anonymous"})
    try:
        r=urllib.request.urlopen(req,timeout=30); print(m,r.status,json.load(r)["choices"][0]["message"]["content"][:20],f"{time.time()-t:.1f}s")
    except Exception as e: print(m,"ERR",getattr(e,'code',e),f"{time.time()-t:.1f}s")
