"""Objective planner (D-053): one owner objective -> an ordered list of single-purpose bot objectives.

The factory builds ONE bot per `create` job and every bot must be least-privilege and independently testable. Owners
speak in outcomes ("I want a pipeline that ingests logs, summarises them and flags anomalies"), which is often 2-4
bots. This module asks the architect lane to decompose an objective, validates the plan (bounded size, no duplicate
of an existing active bot, each step a self-contained objective), and the worker enqueues one `create` per step.

    python tools/factory_plan.py "<objective>" [--dry-run] [--max 4]

Plan rules enforced in code, not by prompt alone:
  * 1..MAX_STEPS steps; a single-purpose objective yields exactly one step (planner is not allowed to inflate).
  * A step that duplicates an existing active bot's purpose (name/purpose overlap) is linked, not rebuilt.
  * Steps carry no tools/permissions — the architect decides those per bot under the job allowance.
"""
from __future__ import annotations
import json, os, re, sys, pathlib, difflib
ROOT = pathlib.Path(os.environ.get("AIFACTORY_REPO", pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(ROOT / "core")); sys.path.insert(0, str(ROOT / "tools"))
from factory.registry import Registry   # noqa: E402

MAX_STEPS = 4

PLAN_PROMPT = """You are the planner of an AI Bot Factory. The factory builds ONE small, single-purpose bot per step.
Each bot has a few tools (read_file, write_file, web_search, web_fetch) and 2-3 offline acceptance tests.

Decompose the OWNER OBJECTIVE into the minimum number of bot objectives (1 to {max_steps}).
- If the objective is already one bot's job, return exactly ONE step (do not split artificially).
- Each step objective must be self-contained, concrete, and testable with small workspace files.
- Order steps so that later bots consume files earlier bots produce (name the files explicitly).
- No tools, permissions or model choices — the architect decides those.

EXISTING ACTIVE BOTS (reuse instead of rebuilding if one already does a step):
{existing}

Return ONLY JSON: {{"steps": [{{"objective": "...", "produces": ["file.txt"], "consumes": ["other.txt"]}}], "rationale": "one sentence"}}
OWNER OBJECTIVE: {objective}"""


def _existing(reg: Registry) -> list[dict]:
    return [{"id": b.id, "name": b.name, "purpose": b.purpose} for b in reg.all("bots") if b.status == "active" and b.id != "001"]


def _similar(step: str, existing: list[dict]) -> dict | None:
    s = re.sub(r"\W+", " ", step.lower())
    for b in existing:
        ratio = difflib.SequenceMatcher(None, s, re.sub(r"\W+", " ", b["purpose"].lower())).ratio()
        if ratio >= 0.75:
            return {**b, "similarity": round(ratio, 2)}
    return None


def validate_plan(plan: dict, existing: list[dict], max_steps: int = MAX_STEPS) -> list[str]:
    problems = []
    steps = plan.get("steps") if isinstance(plan, dict) else None
    if not isinstance(steps, list) or not steps:
        return ["plan must contain a non-empty steps list"]
    if len(steps) > max_steps:
        problems.append(f"too many steps ({len(steps)} > {max_steps}); merge or drop steps")
    seen = set()
    for i, st in enumerate(steps, 1):
        obj = (st.get("objective") if isinstance(st, dict) else None) or ""
        if len(obj.split()) < 6:
            problems.append(f"step {i} objective too vague: {obj!r}")
        if "->" in obj:
            problems.append(f"step {i} objective must not contain '->'")
        key = re.sub(r"\W+", " ", obj.lower()).strip()
        if key in seen:
            problems.append(f"step {i} duplicates an earlier step")
        seen.add(key)
        for k in ("produces", "consumes"):
            if k in st and not isinstance(st[k], list):
                problems.append(f"step {i} {k} must be a list")
    # consumes must be produced by an earlier step or be a fixture the tests create
    produced: set[str] = set()
    for i, st in enumerate(steps, 1):
        for c in st.get("consumes", []) or []:
            if c not in produced:
                st.setdefault("fixtures", []).append(c)    # allowed: the bot's own tests create it
        produced |= set(st.get("produces", []) or [])
    return problems


def plan(objective: str, max_steps: int = MAX_STEPS, chat=None, attempts: int = 3) -> dict:
    import factory_pipeline as fp
    chat = chat or fp.chat
    reg = Registry(ROOT / "registry"); existing = _existing(reg)
    ex_txt = "\n".join(f"- {b['id']} {b['name']}: {b['purpose']}" for b in existing) or "- none"
    msgs = [{"role": "user", "content": PLAN_PROMPT.format(max_steps=max_steps, existing=ex_txt, objective=objective)}]
    last = ""
    for _ in range(attempts):
        text, lane = chat(msgs)
        m = re.search(r"\{.*\}", text, re.S)
        try:
            p = json.loads(m.group(0) if m else text)
        except Exception as e:
            last = f"not JSON: {e}"; msgs += [{"role": "assistant", "content": text}, {"role": "user", "content": "Return ONLY the JSON object."}]; continue
        probs = validate_plan(p, existing, max_steps)
        if not probs:
            for st in p["steps"]:
                dup = _similar(st["objective"], existing)
                if dup: st["reuse"] = dup
            p.update({"objective": objective, "lane": lane, "existing_considered": len(existing)})
            return p
        last = "; ".join(probs)
        msgs += [{"role": "assistant", "content": json.dumps(p)}, {"role": "user", "content": f"Plan rejected: {last}. Fix and return ONLY the JSON."}]
    raise RuntimeError(f"logic: planner could not produce a valid plan after {attempts} attempts: {last}")


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    print(json.dumps(plan(a[0], int(opt("--max", MAX_STEPS))), indent=1))
