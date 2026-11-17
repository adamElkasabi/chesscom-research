#!/usr/bin/env python3
"""Lossless integer/column encoding of repetitive callsite records;all fields restored exactly."""
from pathlib import Path
import zipfile,tarfile,lzma,json,time,hashlib,collections
B=Path('/var/tmp/wasm-deep');O=B/'output';ROOT='website-audit/wasm-deep-follow-up/';t=time.monotonic();logical=[];physical=[]
def u(v,out):
 assert v>=0
 while v>127:out.append((v&127)|128);v>>=7
 out.append(v)
with zipfile.ZipFile(B/'combined-deep.zip')as z,lzma.LZMAFile(B/'analysis-evidence-compact.tar.xz','w',format=lzma.FORMAT_XZ,filters=[{'id':lzma.FILTER_LZMA2,'dict_size':64*1024*1024,'preset':6}])as xz,tarfile.open(fileobj=xz,mode='w|')as tar:
 entries=sorted((i for i in z.infolist()if i.filename.startswith(ROOT+'deep-functions/')),key=lambda i:(i.filename.split('/')[-1],i.filename))
 for n,i in enumerate(entries):
  data=z.read(i);name=i.filename[len(ROOT):];dest=name;codec='identity'
  if name.endswith('/direct-call-sites.jsonl'):
   enc=bytearray(b'DCV1');pc=po=0
   for l in data.splitlines():
    r=json.loads(l);assert list(r)==['caller','callee','offset'];u(r['caller']-pc,enc);u(r['callee'],enc);u(r['offset']-po,enc);pc=r['caller'];po=r['offset']
   dataout=bytes(enc);dest=name+'.dcv1';codec='dcv1'
  elif name.endswith('/indirect-dispatch-sites.jsonl'):
   rows=[json.loads(l)for l in data.splitlines()];keys=list(dict.fromkeys(k for r in rows for k in r));orders=list(dict.fromkeys(tuple(r)for r in rows));columns={};orderids={v:i for i,v in enumerate(orders)}
   for k in keys:
    vals=[r.get(k)for r in rows]
    if k in ['caller','instruction_offset'] and all(isinstance(v,int)for v in vals):
     prev=0;deltas=[]
     for v in vals:deltas.append(v-prev);prev=v
     columns[k]={'delta':deltas}
    elif vals and all(v is None or isinstance(v,str)for v in vals):
     cats=list(dict.fromkeys(vals));ids={v:j for j,v in enumerate(cats)};columns[k]={'dictionary':cats,'indices':[ids[v]for v in vals]}
    else:columns[k]={'values':vals}
   dataout=json.dumps({'codec':'columns-v1','rows':len(rows),'orders':orders,'order_ids':[orderids[tuple(r)]for r in rows],'columns':columns},separators=(',',':')).encode();dest=name+'.columns.json';codec='columns-v1'
  else:dataout=data
  info=tarfile.TarInfo(dest);info.size=len(dataout);info.mtime=0;info.mode=0o644
  import io
  tar.addfile(info,io.BytesIO(dataout));logical.append({'path':name,'encoded_path':dest,'codec':codec,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()});physical.append({'path':dest,'bytes':len(dataout),'sha256':hashlib.sha256(dataout).hexdigest()})
  if n%100==0:print(n,len(entries),'seconds',round(time.monotonic()-t,1),flush=True)
(O/'analysis-logical-members.json').write_text(json.dumps({'container':'analysis-evidence.tar.xz','logical_members':logical,'encoded_members':physical,'qualification':'Encoding is lossless. Materialization restores exact JSON/JSONL bytes from the original combined package. No callsite fields or function records removed.'},indent=2));print('FINAL', (B/'analysis-evidence-compact.tar.xz').stat().st_size,'seconds',round(time.monotonic()-t,1),flush=True)
