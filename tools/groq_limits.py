import os,urllib.request,json
k=os.environ["GROQ_API_KEY"];H={"Content-Type":"application/json","Authorization":"Bearer "+k,"User-Agent":"ai-factory-probe/1.0"}
for m in ["openai/gpt-oss-120b","openai/gpt-oss-20b","qwen/qwen3.8-27b","groq/compound","groq/compound-mini"]:
    req=urllib.request.Request("https://api.groq.com/openai/v1/chat/completions",data=json.dumps({"model":m,"messages":[{"role":"user","content":"hi"}],"max_tokens":2}).encode(),headers=H)
    try:
        r=urllib.request.urlopen(req,timeout=30); h=r.headers
        print(m,"| RPM",h.get("x-ratelimit-limit-requests"),"RPD-remaining",h.get("x-ratelimit-remaining-requests"),"| TPM",h.get("x-ratelimit-limit-tokens"),"TPD?",h.get("x-ratelimit-limit-tokens-day"))
    except urllib.error.HTTPError as e: print(m,"HTTP",e.code,e.read()[:150])
