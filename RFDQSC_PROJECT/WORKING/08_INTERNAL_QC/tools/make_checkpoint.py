#!/usr/bin/env python3
"""Build a cumulative checkpoint zip from the WORKING tree and verify its integrity.
usage: make_checkpoint.py <phase-number>   (run from RFDQSC_PROJECT/ ; WORKING/ and CHECKPOINTS/ are siblings)"""
import sys, os, hashlib, zipfile, datetime
ph=int(sys.argv[1]); tag=f"{ph:02d}"
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../WORKING/08_INTERNAL_QC -> WORKING
W=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","..")); 
out=os.path.abspath(os.path.join(W,"..","CHECKPOINTS")); os.makedirs(out,exist_ok=True)
man=os.path.join(W,"00_STATE","CHECKPOINT_MANIFEST.md")
files=[]
for d,_,fs in os.walk(W):
    for f in sorted(fs):
        p=os.path.join(d,f); rel=os.path.relpath(p,W)
        if rel=="00_STATE/CHECKPOINT_MANIFEST.md" or "__pycache__" in rel: continue
        files.append(rel)
files.sort()
lines=[f"# CHECKPOINT MANIFEST — CHECKPOINT_PHASE_{tag}",f"Generated {datetime.date.today()} · {len(files)} files (this manifest excluded; its own hash cannot be self-listed)","","| SHA-256 | bytes | path |","|---|---|---|"]
for rel in files:
    p=os.path.join(W,rel); h=hashlib.sha256(open(p,'rb').read()).hexdigest()
    lines.append(f"| {h} | {os.path.getsize(p)} | {rel} |")
open(man,"w").write("\n".join(lines)+"\n")
zp=os.path.join(out,f"RFDQSC_CHECKPOINT_PHASE_{tag}.zip")
with zipfile.ZipFile(zp,"w",zipfile.ZIP_DEFLATED) as z:
    for rel in files+["00_STATE/CHECKPOINT_MANIFEST.md"]:
        z.write(os.path.join(W,rel),f"CHECKPOINT_PHASE_{tag}/{rel}")
# integrity verification
req=["00_STATE/PROJECT_STATE.md","00_STATE/CURRENT_PHASE.txt","00_STATE/COMPLETED_PHASES.txt","00_STATE/CHECKPOINT_MANIFEST.md","00_STATE/RESUME_INSTRUCTIONS.md","06_VALUE_LEDGER/VALUE_LEDGER.csv","08_INTERNAL_QC/CHANGELOG.md","08_INTERNAL_QC/AUTHOR_DECISIONS.md","08_INTERNAL_QC/REVIEWER_QA.md","08_INTERNAL_QC/VOICE_CHANGES.md","01_BASELINE/BASELINE_SHA256.txt"]+[f"07_PHASE_REPORTS/PHASE_{i:02d}_{n}.md" for i,n in []]
with zipfile.ZipFile(zp) as z:
    names=set(z.namelist()); assert z.testzip() is None
    miss=[r for r in req if f"CHECKPOINT_PHASE_{tag}/{r}" not in names]
    reports=[n for n in names if "/07_PHASE_REPORTS/PHASE_" in n]
    assert not miss, miss
    assert len(reports)>=ph+0 if ph>0 else len(reports)>=1, reports
    # every phase 0..ph must have a report
    for i in range(ph+1):
        assert any(f"/07_PHASE_REPORTS/PHASE_{i:02d}_" in n for n in names), f"report for phase {i} missing"
    # manifest hashes match zip content
    for line in z.read(f"CHECKPOINT_PHASE_{tag}/00_STATE/CHECKPOINT_MANIFEST.md").decode().splitlines():
        if line.startswith("| ") and not line.startswith("| SHA") and not line.startswith("|---"):
            h,b,rel=[c.strip() for c in line.strip("|").split("|")]
            assert hashlib.sha256(z.read(f"CHECKPOINT_PHASE_{tag}/{rel}")).hexdigest()==h, rel
    cur=z.read(f"CHECKPOINT_PHASE_{tag}/00_STATE/CURRENT_PHASE.txt").decode()
    assert f"CURRENT_PHASE={tag}" in cur, cur
print("OK",zp,len(files)+1,"files",os.path.getsize(zp),"bytes")
