#!/usr/bin/env python3
"""Explicit, hash-verifying recovery of excluded PUBLIC evidence. Python3 stdlib.
Run locally after downloading the audit. Default --list makes no network request.
Example: python retrieve-evidence.py --archive website-complete-forensic-audit.zip --id new-binary-026 --output ./recovered --fetch
"""
from pathlib import Path
import argparse,json,zipfile,urllib.request,hashlib,shutil,os
ROOT='website-audit/wasm-deep-follow-up/'
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--archive',default='website-complete-forensic-audit.zip');p.add_argument('--list',action='store_true');p.add_argument('--id',help='binary ID or exact payload SHA256');p.add_argument('--fetch',action='store_true',help='Explicitly authorize public GET(s) and local output');p.add_argument('--output',default='recovered-public-evidence');a=p.parse_args()
with zipfile.ZipFile(a.archive) as z:
 rows=json.loads(z.read(ROOT+'packaging-retention.json'));requests=json.loads(z.read(ROOT+'retrieval-log.json'))
 if a.list or not a.fetch:
  for r in rows:print(r.get('binary_id',r['sha256']),r['bytes'],'embedded' if r['included'] else 'excluded',r['sha256'])
  if not a.fetch:raise SystemExit('No network request made. Select --id and --fetch on a local downloaded copy to recover a payload.')
 if not a.id:raise SystemExit('--id is required with --fetch')
 matches=[r for r in rows if r.get('binary_id')==a.id or r['sha256']==a.id]
 if len(matches)!=1:raise SystemExit('ID must match exactly one known payload')
 r=matches[0];out=Path(a.output).resolve();out.mkdir(exist_ok=True,parents=True);name=r.get('binary_id',r['sha256'])+('.wasm' if r['payload_kind']=='core module' else '.nnue');dest=out/name
 if dest.exists():
  if dest.stat().st_size==r['bytes'] and hashlib.sha256(dest.read_bytes()).hexdigest()==r['sha256']:raise SystemExit('Existing output verified: '+str(dest))
  raise SystemExit('Refusing to overwrite differing existing output: '+str(dest))
 if r['included']:
  data=z.read(r['archive_path']);assert len(data)==r['bytes'] and hashlib.sha256(data).hexdigest()==r['sha256'];dest.write_bytes(data);raise SystemExit('Restored embedded payload: '+str(dest))
 def fetch(url,path,size,sha):
  if not url.startswith(('https://www.chess.com/','https://unpkg.com/','https://cdn.jsdelivr.net/')):raise SystemExit('URL outside recorded public origins')
  h=hashlib.sha256();n=0
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Public-evidence-hash-verifier/1.0'}),timeout=60) as response,path.open('xb') as f:
    if response.status!=200:raise ValueError('Expected complete HTTP200,got '+str(response.status))
    while True:
     b=response.read(1024*1024)
     if not b:break
     n+=len(b)
     if n>size:raise ValueError('Response exceeds exact recorded byte length')
     h.update(b);f.write(b)
   if n!=size or h.hexdigest()!=sha:raise ValueError('Payload changed or incomplete;bytes/hash mismatch')
  except Exception:
   path.unlink(missing_ok=True);raise
 urls=r['urls'];tmp=out/(name+'.partial')
 if tmp.exists():raise SystemExit('Partial destination exists;review/remove it first: '+str(tmp))
 if r.get('binary_id')=='new-binary-026':
  try:
   with tmp.open('xb') as f:
    for i,url in enumerate(urls):
     rr=next(x for x in requests if x['url']==url and x.get('sha256'));part=out/(name+'.part-'+str(i))
     fetch(url,part,rr['bytes'],rr['sha256'])
     with part.open('rb') as q:shutil.copyfileobj(q,f)
     part.unlink()
   if tmp.stat().st_size!=r['bytes'] or hashlib.sha256(tmp.read_bytes()).hexdigest()!=r['sha256']:raise ValueError('Assembled Torch hash/size mismatch')
  except Exception:tmp.unlink(missing_ok=True);raise
 else:
  errors=[]
  for url in urls:
   try:fetch(url,tmp,r['bytes'],r['sha256']);break
   except Exception as e:errors.append(str(e))
  else:raise SystemExit('No recorded URL produced the exact payload: '+repr(errors))
 os.replace(tmp,dest);print('Verified and recovered:',dest,'SHA256',r['sha256'])
