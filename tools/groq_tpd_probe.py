import os,urllib.request,json,time,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
k=os.environ["GROQ_API_KEY"];H={"Content-Type":"application/json","Authorization":"Bearer "+k,"User-Agent":"ai-factory-probe/1.0"}
# ~4.5k token request like a real agent step
big="word "*4200
import sys as _s; m=_s.argv[1]
for i in range(1):
    req=urllib.request.Request("https://api.groq.com/openai/v1/chat/completions",data=json.dumps({"model":m,"messages":[{"role":"user","content":big+" Reply OK"}],"max_tokens":4}).encode(),headers=H)
    t=time.time()
    try:
        r=urllib.request.urlopen(req,timeout=60); print(i,"OK",f"{time.time()-t:.1f}s",{k:v for k,v in r.headers.items() if 'ratelimit' in k.lower()})
    except urllib.error.HTTPError as e:
        print(i,"HTTP",e.code,{k:v for k,v in e.headers.items() if 'ratelimit' in k.lower() or k.lower()=='retry-after'}); print("   BODY:",e.read().decode()[:500])
