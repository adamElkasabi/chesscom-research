#!/usr/bin/env python3
"""Selective recovery after forensic-archive consolidation. Python stdlib only."""
from pathlib import Path
import argparse,json,zipfile,hashlib
R=Path(__file__).resolve().parent;A=R/'website-complete-forensic-audit.zip'
p=argparse.ArgumentParser(description=__doc__);p.add_argument('group',nargs='?',choices=['active-cee','inactive-engines','research','audit']);p.add_argument('--list',action='store_true');args=p.parse_args()
if args.list or not args.group:
 print('active-cee: restore active CEE loader/WASM (~32 MiB; requires headroom)')
 print('inactive-engines: restore legacy engines/NNUE/book (~80 MiB; requires headroom)')
 print('research: restore research-workspace.zip (~13 MiB)')
 print('audit: expand full new audit (very large; use downloaded ZIP outside this workspace instead)')
 raise SystemExit()
with zipfile.ZipFile(A) as z:
 if args.group in ['active-cee','inactive-engines']:
  mapping=json.loads(z.read('website-audit/audit-metadata/workspace-asset-restore-map.json'))
  entries=[x for x in mapping if (x['original_path'] in ['extension/engines/cee/explanation-engine.js','extension/engines/cee/explanation-engine.wasm'])==(args.group=='active-cee')]
  needed=sum(x['bytes'] for x in entries if not (R/x['original_path']).exists())
  used=sum(f.stat().st_size for f in R.rglob('*') if f.is_file())
  if used+needed>128*1048576:raise SystemExit('Restoration would exceed 128 MiB. Download/move a large archive off-workspace first. Needed additional MiB: '+str(round(needed/1048576,2)))
  for x in entries:
   data=z.read('website-audit/'+x['archive_path']);assert hashlib.sha256(data).hexdigest()==x['sha256'];dest=R/x['original_path']
   if dest.exists() and dest.read_bytes()!=data:raise SystemExit('Differing destination; move aside first: '+str(dest))
   dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
  print('Restored',args.group);raise SystemExit()
if args.group=='research':
 with zipfile.ZipFile(R/'workspace-archives/research-workspace.zip') as z: z.extractall(R)
 print('Research restored; check remaining headroom.')
else:raise SystemExit('Full audit expansion is intentionally blocked inside the capped workspace. Download the ZIP and extract locally, or use zipfile to read selected members.')
