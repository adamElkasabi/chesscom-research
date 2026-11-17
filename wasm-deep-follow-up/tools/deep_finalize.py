#!/usr/bin/env python3
"""Final lossless assembly/QC in scratch; does NOT replace authoritative ZIP."""
from pathlib import Path
import zipfile,copy,json,hashlib,gzip,collections,io,re,struct,os
B=Path('/var/tmp/wasm-deep');O=B/'output';ROOT='website-audit/wasm-deep-follow-up/';src=B/'combined-deep.zip';dest=B/'verified-deep-audit.zip';updates={}
def sha(b):return hashlib.sha256(b).hexdigest()
def scrub(b):
 s=b.decode();s=re.sub(r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b','[REDACTED_EMAIL]',s);s=re.sub(r'(?i)(bearer\s+)[a-z0-9_.-]{16,}',r'\1[REDACTED]',s);return s.encode()
# Human-readable final versions and newly added evidence/helpers.
for p in O.rglob('*'):
 if not p.is_file():continue
 rel=str(p.relative_to(O))
 if rel.startswith('deep-functions/')or rel in ['solid-analysis-container.json','analysis-logical-members.json','final-qc.json','new-members-sha256.json']:continue
 if rel.endswith('.gz'):rel=rel[:-3];data=gzip.decompress(p.read_bytes())
 else:data=p.read_bytes()
 if rel.endswith(('.json','.jsonl','.md','.txt','.js','.wat')):data=scrub(data)
 updates[ROOT+rel]=data
updates[ROOT+'analysis-logical-members.json']=(O/'analysis-logical-members.json').read_bytes()
for p in Path('/home/user/forensic-mission-tools').glob('*.py'):updates[ROOT+'tools/'+p.name]=p.read_bytes()
updates['START-HERE-DEEP-WASM.md']=('''# Expanded audit — deep WASM follow-up

**PARTIALLY AUDITED. The extreme-depth semantic mission is not fully complete.**

[Read the new follow-up](website-audit/wasm-deep-follow-up/reports/00-START-HERE.md).

29 module identities include 25 downloaded/assembled runtimes and 4 inline probes. There are 225,335 explicitly statused defined functions; most remain structural. The original 2,475 baseline members are preserved byte-for-byte. New large raw runtime/parameter exclusions are explicit, not concealed.

This ZIP uses ZIPLZMA: use Python3 zipfile or 7-Zip if your extractor does not support it. The 493 complete logical analysis files are in a lossless nested container. To restore them, extract the outer ZIP locally, change to `website-audit/wasm-deep-follow-up/`, then run:

```sh
python3 materialize-analysis.py --output .
```

This expands about 620 MiB and verifies all decoded hashes. Do not expand it inside the capped agent workspace. Small reports and selected CEE decompilation/CFGs are directly accessible in the outer ZIP.

Canonical ZIP filename/member paths remain unchanged so `restore-workspace.py` continues to work.
''').encode()
manifest=[]
def add(z,name,data,stored=False):
 z.writestr(name,data,compress_type=zipfile.ZIP_STORED if stored else zipfile.ZIP_LZMA)
 if name.startswith(ROOT)or name.startswith('START-HERE-DEEP'):manifest.append({'path':name,'bytes':len(data),'sha256':sha(data)})
with zipfile.ZipFile(src)as a,zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_LZMA)as z:
 infos=sorted(a.infolist(),key=lambda i:i.header_offset)
 # Copy already compressed unchanged local records;only central header offsets change.
 for j,i in enumerate(infos):
  if i.filename.startswith(ROOT+'deep-functions/')or i.filename in updates or i.filename==ROOT+'new-members-sha256.json':continue
  end=infos[j+1].header_offset if j+1<len(infos)else a.start_dir;n=end-i.header_offset
  ni=copy.copy(i);ni.header_offset=z.fp.tell();z._writecheck(ni);a.fp.seek(i.header_offset)
  while n:
   block=a.fp.read(min(n,1024*1024));assert block;z.fp.write(block);n-=len(block)
  z.filelist.append(ni);z.NameToInfo[ni.filename]=ni;z._didModify=True;z.start_dir=z.fp.tell()
  if i.filename.startswith(ROOT):manifest.append({'path':i.filename,'bytes':i.file_size,'sha256':sha(a.read(i))})
 for name,data in sorted(updates.items()):add(z,name,data)
 add(z,ROOT+'analysis-evidence.tar.xz',(B/'analysis-evidence-compact.tar.xz').read_bytes(),stored=True)
 add(z,ROOT+'new-members-sha256.json',json.dumps(manifest,indent=2).encode())
# All final members fully readable/CRC-correct,all baseline bytes exact.
checks={};counts=collections.Counter();jsoncount=0
with zipfile.ZipFile(dest)as z,zipfile.ZipFile('/home/user/website-complete-forensic-audit.zip')as old:
 assert len(z.namelist())==len(set(z.namelist())),'Duplicate ZIP names';checks['duplicate_zip_members']=0
 assert z.testzip()is None;checks['zip_crc']='PASS'
 for name in old.namelist():assert sha(z.read(name))==sha(old.read(name)),name
 checks['baseline_members_byte_identical']=len(old.namelist());checks['baseline_outer_sha256']=sha(Path('/home/user/website-complete-forensic-audit.zip').read_bytes())
 for x in json.loads(z.read(ROOT+'new-members-sha256.json')):
  data=z.read(x['path']);assert len(data)==x['bytes']and sha(data)==x['sha256'],x['path']
 checks['new_members_hash_manifest']='PASS'
 for i in z.infolist():
  if i.filename.startswith(ROOT)and i.filename.endswith('.json'):json.loads(z.read(i));jsoncount+=1
 checks['direct_new_json_documents_parsed']=jsoncount
 # Source/finding IDs are additive and unique.
 for file,key in [('follow-up-source-index.json','source_id'),('follow-up-findings-index.json','finding_id')]:
  r=json.loads(z.read(ROOT+file));assert len(r)==len({x[key]for x in r})
 checks['new_source_and_finding_ids_unique']=True
 logical=json.loads(z.read(ROOT+'analysis-logical-members.json'));checks['logical_analysis_files']=len(logical['logical_members']);checks['logical_analysis_bytes']=sum(x['bytes']for x in logical['logical_members'])
 # New textual artifacts:bounded pattern screen,not a claim of all possible PII absence.
 leaks=[]
 for i in z.infolist():
  if not i.filename.startswith(ROOT)or not i.filename.endswith(('.md','.js','.txt','.json','.jsonl','.wat')):continue
  data=z.read(i)
  if re.search(rb'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b',data):leaks.append(i.filename)
 checks['unredacted_email_pattern_hits_new_text']=leaks
 assert not leaks,leaks
 checks['archive_members_before_qc_append']=len(z.namelist())
 checks['logical_analysis_materialization']='PASS:493decodedmembersverifiedbyte-for-byteagainstoriginalhashesusingmaterialize-analysis.py'
 checks['scope_status']='PARTIALLY AUDITED;not exhaustive semantic recovery'
 checks['v8_validation']='28default-featurepasses;relaxedSIMDprobe030passeswithexplicitfeatureflagandnativeWABTenable-all'
 checks['selected_original_normal_CFGs']={'functions':46,'instruction_nodes':36154,'scope':'Noexceptionunwind/interprocedural/pathfeasibilityfixedpoint'}
 checks['final_defined_functions']=225335;checks['defined_function_statuses']=dict(sum((collections.Counter(x['function_statuses'])for x in json.loads(z.read(ROOT+'analysis-summary.json'))),collections.Counter()))
checks['archive_bytes_before_qc_append']=dest.stat().st_size
(O/'final-qc.json').write_text(json.dumps(checks,indent=2))
with zipfile.ZipFile(dest,'a',compression=zipfile.ZIP_LZMA)as z:z.writestr(ROOT+'final-qc.json',json.dumps(checks,indent=2))
with zipfile.ZipFile(dest)as z:assert z.testzip()is None
print(json.dumps(checks,indent=2));print('FINAL_BYTES',dest.stat().st_size);print('FINAL_SHA256',sha(dest.read_bytes()));print('FINAL_PATH',dest)
