#!/usr/bin/env python3
"""Restore exact deep-functions JSON/JSONL from the lossless analysis container.
Python3 stdlib only. Run on a downloaded local copy, not the capped workspace.
python materialize-analysis.py --container analysis-evidence.tar.xz --output .
Every decoded member is checked against exact byte length and SHA256.
"""
from pathlib import Path
import argparse,tarfile,json,hashlib
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--container',default=str(Path(__file__).with_name('analysis-evidence.tar.xz')));p.add_argument('--manifest',default=str(Path(__file__).with_name('analysis-logical-members.json')));p.add_argument('--output',default='.');p.add_argument('--verify-only',action='store_true');a=p.parse_args();out=Path(a.output).resolve();manifest=json.loads(Path(a.manifest).read_text());rows={r['encoded_path']:r for r in manifest['logical_members']};physical={r['path']:r for r in manifest['encoded_members']};seen=set()
def decode(data,codec):
 if codec=='identity':return data
 if codec=='dcv1':
  if data[:4]!=b'DCV1':raise ValueError('Bad DCV1 signature')
  pos=4;pc=po=0;output=bytearray()
  def u():
   nonlocal pos
   value=shift=0
   while True:
    if pos>=len(data):raise ValueError('Truncated varint')
    b=data[pos];pos+=1;value|=(b&127)<<shift
    if not b&128:return value
    shift+=7
    if shift>63:raise ValueError('Oversized varint')
  while pos<len(data):
   pc+=u();callee=u();po+=u();output.extend((json.dumps({'caller':pc,'callee':callee,'offset':po})+'\n').encode())
  return bytes(output)
 if codec=='columns-v1':
  x=json.loads(data);assert x['codec']=='columns-v1';columns={}
  for k,c in x['columns'].items():
   if 'delta'in c:
    total=0;vals=[]
    for v in c['delta']:total+=v;vals.append(total)
   elif 'dictionary'in c:vals=[c['dictionary'][j]for j in c['indices']]
   else:vals=c['values']
   assert len(vals)==x['rows'];columns[k]=vals
  return ''.join(json.dumps({k:columns[k][i]for k in x['orders'][x['order_ids'][i]]})+'\n'for i in range(x['rows'])).encode()
 raise ValueError('Unknown codec '+codec)
with tarfile.open(a.container,'r|xz')as tar:
 for member in tar:
  if not member.isfile()or member.name not in rows:raise ValueError('Unexpected/non-file tar member '+member.name)
  r=rows[member.name];b=tar.extractfile(member).read();ph=physical[member.name];assert len(b)==ph['bytes']and hashlib.sha256(b).hexdigest()==ph['sha256'];data=decode(b,r['codec']);assert len(data)==r['bytes']and hashlib.sha256(data).hexdigest()==r['sha256'],'Decoded hash mismatch: '+r['path'];seen.add(member.name)
  if not a.verify_only:
   dest=(out/r['path']).resolve()
   if out not in dest.parents:raise ValueError('Unsafe output path')
   if dest.exists():
    if dest.read_bytes()!=data:raise ValueError('Differing output exists: '+str(dest))
   else:dest.parent.mkdir(exist_ok=True,parents=True);dest.write_bytes(data)
if seen!=set(rows):raise ValueError('Missing container members')
print('Verified',len(seen),'exact analysis members.'+(' No files written.'if a.verify_only else ' Materialized under '+str(out)))
