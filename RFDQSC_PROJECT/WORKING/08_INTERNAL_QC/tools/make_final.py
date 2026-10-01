#!/usr/bin/env python3
"""Phase 14: assemble 09_OUTPUTS and the clean submission package. Run from WORKING/."""
import os, shutil, zipfile, re, hashlib
S="RFDQSC"; O="09_OUTPUTS"
shutil.rmtree(O,ignore_errors=True); os.makedirs(O+"/submission_stage")
# 1. FINAL tex / bib (flat names)
t=open("02_MANUSCRIPT/RFDQSC_WORKING.tex",encoding="utf-8").read()
assert t.count("\\bibliography{RFDQSC_references}")==1
t=t.replace("\\bibliography{RFDQSC_references}","\\bibliography{RFDQSC_FINAL}")
open(f"{O}/{S}_FINAL.tex","w",encoding="utf-8").write(t)
shutil.copy("03_REFERENCES/RFDQSC_references.bib",f"{O}/{S}_FINAL.bib")
# 2. ESM_2.zip = curated code
with zipfile.ZipFile(f"{O}/ESM_2.zip","w",zipfile.ZIP_DEFLATED) as z:
    for f in sorted(os.listdir("04_CODE/curated")):
        p="04_CODE/curated/"+f
        if os.path.isfile(p) and not f.endswith(".pyc"): z.write(p,"ESM_2/"+f)
# 3. cover letter + readme
shutil.copy("08_INTERNAL_QC/templates/COVER_LETTER.txt",f"{O}/COVER_LETTER.txt"); shutil.copy("08_INTERNAL_QC/templates/SUBMISSION_README.txt",f"{O}/SUBMISSION_README.txt")
# 4. submission package (flat LaTeX files + supplementary + cover letter; no internal files)
stage=O+"/submission_stage"
for src,dst in [(f"{O}/{S}_FINAL.tex",f"{S}_FINAL.tex"),(f"{O}/{S}_FINAL.bib",f"{S}_FINAL.bib"),
                ("02_MANUSCRIPT/sn-jnl.cls","sn-jnl.cls"),("02_MANUSCRIPT/sn-mathphys-num.bst","sn-mathphys-num.bst"),
                ("02_MANUSCRIPT/supplementary/ESM_1.pdf","ESM_1.pdf"),("02_MANUSCRIPT/supplementary/ESM_1.tex","ESM_1.tex"),
                (f"{O}/ESM_2.zip","ESM_2.zip"),(f"{O}/COVER_LETTER.txt","COVER_LETTER.txt"),(f"{O}/SUBMISSION_README.txt","SUBMISSION_README.txt")]:
    if os.path.exists(src): shutil.copy(src,f"{stage}/{dst}")
    else: print("MISSING",src)
with zipfile.ZipFile(f"{O}/{S}_FINAL_SUBMISSION_PACKAGE.zip","w",zipfile.ZIP_DEFLATED) as z:
    for f in sorted(os.listdir(stage)): z.write(f"{stage}/{f}",f)
shutil.rmtree(stage)
print(sorted(os.listdir(O)))
