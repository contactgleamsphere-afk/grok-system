import json, time, urllib.request, sys, subprocess, pathlib, re, os
for _k in ("GROQ_API_KEY","OPENROUTER_API_KEY","GEMINI_API_KEY"):
    if not os.environ.get(_k):
        _v=subprocess.run(["powershell","-NoProfile","-Command",f"[Environment]::GetEnvironmentVariable('{_k}','User')"],capture_output=True,text=True).stdout.strip()
        if _v: os.environ[_k]=_v
OUT = pathlib.Path(r"C:\AI\Factory\run\bench"); OUT.mkdir(parents=True, exist_ok=True)
NB = r"C:\AI\Factory\.venv\Scripts\nanobot.exe"; CFG=r"C:\AI\Factory\config.json"; WS=r"C:\AI\Factory\workspace"
def ollama(model, prompt, num_predict=200):
    req = urllib.request.Request("http://127.0.0.1:11434/api/generate", data=json.dumps({"model":model,"prompt":prompt,"stream":False,"options":{"num_predict":num_predict}}).encode(), headers={"Content-Type":"application/json"})
    t=time.time(); r=json.load(urllib.request.urlopen(req, timeout=900)); 
    return {"model":model,"eval_tok_s":round(r["eval_count"]/(r["eval_duration"]/1e9),2),"prompt_tok_s":round(r.get("prompt_eval_count",0)/max(r.get("prompt_eval_duration",1),1)*1e9,1),"total_s":round(r["total_duration"]/1e9,1),"wall_s":round(time.time()-t,1)}
def free_mb():
    o=subprocess.run(["powershell","-NoProfile","-Command","(Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory"],capture_output=True,text=True).stdout.strip(); return int(int(o)/1024)
def toolcalls(preset, cap=300):
    tests=[("T1","Create a file named p0_test.txt in the workspace containing the single line HELLO_FACTORY, then read it back and tell me its contents."),
           ("T2","List the files in the workspace root directory and count them."),
           ("T3","Run the shell command: python --version  and tell me the exact output."),
           ("T4","Read p0_test.txt, append a second line GOODBYE, save it, then tell me how many lines it now has."),
           ("T5","Use web search to find the current stable version number of the Python package nanobot-ai on PyPI and report only the version.")]
    res=[]; pathlib.Path(WS,"p0_test.txt").unlink(missing_ok=True)
    for tid,pr in tests:
        t=time.time()
        try:
            r=subprocess.run([NB,"agent","-m",pr,"-s",f"bench-{preset}-{int(time.time())}","--classic","--no-markdown","--config",CFG,"--workspace",WS],capture_output=True,text=True,encoding="utf-8",errors="replace",timeout=cap)
            out=r.stdout; status="done"
        except subprocess.TimeoutExpired as e:
            out=(e.stdout or b"").decode("utf-8","replace") if isinstance(e.stdout,bytes) else (e.stdout or ""); status="TIMEOUT"
        el=round(time.time()-t,1); calls=len(re.findall(r"^\s*\S+\s+\w+", out, re.M))
        f=pathlib.Path(WS,"p0_test.txt")
        ok={"T1": f.exists() and "HELLO_FACTORY" in f.read_text(errors="replace") and "HELLO_FACTORY" in out,
            "T2": bool(re.search(r"\b\d+\b", out)) and status=="done",
            "T3": "3.11.9" in out,
            "T4": f.exists() and "GOODBYE" in f.read_text(errors="replace") and "2" in out,
            "T5": "0.3.5" in out}[tid]
        res.append({"test":tid,"status":status,"seconds":el,"correct":bool(ok),"tail":out.strip().splitlines()[-3:] if out.strip() else []})
        print(json.dumps(res[-1]),flush=True)
    pathlib.Path(WS,"p0_test.txt").unlink(missing_ok=True); return res
if __name__=="__main__":
    mode=sys.argv[1]
    if mode=="speed":
        m=sys.argv[2]; b=free_mb(); r=ollama(m,"Write exactly 150 words about the history of Birmingham, England."); r["free_mb_before"]=b; r["free_mb_after"]=free_mb(); print(json.dumps(r)); (OUT/f"speed_{m.replace(':','_')}.json").write_text(json.dumps(r))
    else:
        preset=sys.argv[2]; res=toolcalls(preset); (OUT/f"tools_{preset}.json").write_text(json.dumps(res,indent=1))
        print("SCORE",preset,sum(r["correct"] for r in res),"/5")
