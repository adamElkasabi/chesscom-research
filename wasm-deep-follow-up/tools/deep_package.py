#!/usr/bin/env python3
from pathlib import Path
import json,zipfile,gzip,hashlib,re,os,time,shutil
B=Path('/var/tmp/wasm-deep');O=B/'output';OUT=B/'combined-deep.zip';ROOT='website-audit/wasm-deep-follow-up/';manifest=[]
def scrub(s):
 s=re.sub(r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b','[REDACTED_EMAIL]',s)
 return re.sub(r'(?i)(bearer\s+)[a-z0-9_.-]{16,}',r'\1[REDACTED]',s)
ret=[];payloads=[]
for b in json.loads((O/'binary-inventory.json').read_text()):
 base=b['binary_id'].startswith('module-');include=b['bytes']<200 and not base
 p='website-audit/wasm-analysis/modules/'+b['binary_id']+'/module.wasm' if base else ROOT+'retained-payloads/'+b['binary_id']+'.wasm' if include else None
 r={'payload_kind':'core module','binary_id':b['binary_id'],'bytes':b['bytes'],'sha256':b['sha256'],'urls':b.get('urls',[]),'included':bool(base or include),'archive_path':p,'reason':'Baseline original retained unchanged' if base else 'Small exact inline/constructed module retained' if include else 'Publicly retrieved complete module analyzed in scratch;raw copy excluded from capped persistent package. Exact source URLs/hash and all derived records retained.','restoration':'six ordered parts;concatenate and verify final hash' if b['binary_id']=='new-binary-026' else 'GET exact URL and verify SHA256' if b.get('urls') else 'Exact inline probe bytes included'}
 ret.append(r)
 if include:payloads.append((p,Path(b['path'])))
for b in json.loads((O/'model-companion-retrieval.json').read_text()):
 if b.get('body_path'):
  already=b['sha256']=='5af11540bbfefcb54e38c5dd000cab4b469dfa7599a1d55be5d2722c20a8929b'
  ret.append({'payload_kind':'NNUE parameters','bytes':b['bytes'],'sha256':b['sha256'],'urls':[b['url']],'included':already,'archive_path':'website-audit/preserved-workspace/extension/engines/stockfish/nn-5af11540bbfe.nnue' if already else None,'reason':'Acquired full public payload hash-matches an existing preserved baseline member;raw bytes already included.' if already else '47MBparameterpayloadexcludedduetopersistentworkspacecap;headers/hashes/retrievalprovenanceretained.','restoration':'Restore exact preserved baseline member' if already else 'GET exact URL and verify SHA256'})
(O/'packaging-retention.json').write_text(json.dumps(ret,indent=2))
# Downloaded companion text is retained scrubbed;raw acquisition hashes stay in retrieval log.
texts=[];seen=set()
for log in ['companion-loader-retrieval.json','additional-companion-retrieval.json','worker-and-glue-default-retrieval.json']:
 for r in json.loads((O/log).read_text()):
  p=r.get('body_path')
  if not p or not Path(p).exists() or p in seen:continue
  seen.add(p);raw=Path(p).read_bytes()
  if raw[:4]==b'\0asm':continue
  try:txt=raw.decode()
  except UnicodeDecodeError:continue
  name=ROOT+'retrieved-text/'+hashlib.sha256(r['url'].encode()).hexdigest()+('.map.json' if '.map' in r['url'] else '.js')
  texts.append((name,scrub(txt).encode(),{'url':r['url'],'raw_body_sha256':hashlib.sha256(raw).hexdigest(),'scrubbed_path':name}))
(O/'retrieved-text-packaging-map.json').write_text(json.dumps([x[2]for x in texts],indent=2))
def add(z,name,data,kind='new evidence'):
 z.writestr(name,data,compress_type=zipfile.ZIP_LZMA);manifest.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'kind':kind})
t=time.monotonic()
shutil.copyfile(B/'baseline-lzma.zip',OUT)
with zipfile.ZipFile(OUT,'a',compression=zipfile.ZIP_LZMA) as z:
 print('baseline compressed entries copied without recompression',round(time.monotonic()-t,1),flush=True)
 add(z,'START-HERE-DEEP-WASM.md',b'# Expanded audit: deep WASM follow-up\n\nStatus: PARTIALLY AUDITED. The extreme-depth semantic mission is NOT fully complete.\n\nRead [the new follow-up](website-audit/wasm-deep-follow-up/reports/00-START-HERE.md).\n\n29 module identities include 25 downloaded/assembled runtimes and 4 inline probes. 225,335 defined functions have explicit structural/semantic statuses; most remain structural. All 2,475 baseline members are preserved unchanged. Newly acquired large raw modules/model payloads are excluded explicitly in the retention manifest because of storage limits.\n\nThis ZIP uses ZIPLZMA: use Python3 zipfile or 7-Zip if your built-in extractor does not support it. The canonical ZIP filename is preserved so restore-workspace.py continues to work.\n')
 for p in sorted(O.rglob('*')):
  if not p.is_file() or p.name in ['final-qc.json','new-members-sha256.json']:continue
  rel=str(p.relative_to(O));data=p.read_bytes()
  if p.suffix=='.gz':data=gzip.decompress(data);rel=rel[:-3]
  # JSON/text enrichment contains already-scrubbed strings;apply email scrubbing to remaining textual retrieval provenance.
  if rel.endswith(('.json','.jsonl','.txt','.md','.wat')):data=scrub(data.decode()).encode()
  add(z,ROOT+rel,data)
 for name,p in payloads:add(z,name,p.read_bytes(),'retained inline module')
 for name,data,_ in texts:add(z,name,data,'retrieved scrubbed companion text')
 for p in sorted(Path('/home/user/forensic-mission-tools').glob('*.py')):add(z,ROOT+'tools/'+p.name,p.read_bytes(),'analysis script')
 add(z,ROOT+'tools/opcode.def',(B/'tools/opcode.def').read_bytes(),'WABT1.0.36opcode metadata')
 add(z,ROOT+'new-members-sha256.json',json.dumps(manifest,indent=2).encode(),'manifest')
 print('newmembers',len(manifest),'totalbytes',OUT.stat().st_size,'seconds',round(time.monotonic()-t,1),flush=True)
print('FINALSIZE',OUT.stat().st_size,flush=True)
