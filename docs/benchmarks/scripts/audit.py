#!/usr/bin/env python3
"""Blindness audit: read every subagent transcript of this session, find those started with a
bench prompt file, and check each tool call against what that prompt allows.
Usage: audit.py [substring of prompt path to filter, e.g. runs/set3/A/]"""
import json, glob, re, sys, os
SUB = "/root/.claude/projects/-home-claude/294ae12b-0374-5d1c-8907-d6f5ec6e7da7/subagents"
flt = sys.argv[1] if len(sys.argv) > 1 else "runs/"
ok = bad = 0; seen = {}; edits = []
for f in sorted(glob.glob(f"{SUB}/agent-*.jsonl")):
    first_prompt = None; calls = []; model = None
    for line in open(f, encoding="utf-8"):
        try: o = json.loads(line)
        except Exception: continue
        m = o.get("message") or {}
        if m.get("model"): model = m["model"]
        c = m.get("content")
        if first_prompt is None and m.get("role") == "user":
            first_prompt = c if isinstance(c, str) else " ".join(x.get("text", "") for x in c if isinstance(x, dict))
        if isinstance(c, list):
            for x in c:
                if isinstance(x, dict) and x.get("type") == "tool_use":
                    inp = x.get("input") or {}
                    calls.append((x.get("name"), inp.get("file_path") or inp.get("path") or inp.get("command") or inp.get("pattern") or json.dumps(inp)[:80]))
    if not first_prompt: continue
    pm = re.search(r"(/home/claude/bench/\S+?\.md)", first_prompt)
    if not pm or flt not in pm.group(1): continue
    pfile = pm.group(1)
    allowed = {pfile}
    if os.path.exists(pfile):
        ptxt = open(pfile, encoding="utf-8").read()
        allowed |= set(re.findall(r"`(/home/claude/bench/[^`]+)`", ptxt))
    outs = set(p for p in allowed if p.endswith(".csv") and "/runs/" in p)   # the batch's own output file
    viol = [(n, p) for n, p in calls if not ((n in ("Read", "Write") and p in allowed) or (n == "Edit" and p in outs))]
    if any(n == "Edit" for n, p in calls): edits.append(pfile.replace("/home/claude/bench/", ""))
    key = pfile.replace("/home/claude/bench/", "")
    seen[key] = seen.get(key, 0) + 1
    if viol:
        bad += 1; print("VIOLATION", key, os.path.basename(f), model, viol[:6])
    else:
        ok += 1
models = set()
print(f"audited {ok+bad} coding subagents matching '{flt}': {ok} clean, {bad} with calls outside the allowed files")
if edits: print("subagents that used Edit on their own output file (allowed):", edits)
dup = {k: v for k, v in seen.items() if v > 1}
if dup: print("prompts run more than once:", dup)
