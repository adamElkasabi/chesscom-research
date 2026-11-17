#!/usr/bin/env python3
"""Lossless solid compression of new analysis records only. Baseline ZIP members unaffected."""
from pathlib import Path
import zipfile,tarfile,lzma,time,json,hashlib
B=Path('/var/tmp/wasm-deep');ROOT='website-audit/wasm-deep-follow-up/';src=B/'combined-deep.zip';dest=B/'analysis-evidence.tar.xz';t=time.monotonic();rows=[]
with zipfile.ZipFile(src)as z,lzma.LZMAFile(dest,'w',format=lzma.FORMAT_XZ,filters=[{'id':lzma.FILTER_LZMA2,'dict_size':64*1024*1024,'preset':6}]) as xz,tarfile.open(fileobj=xz,mode='w|')as tar:
 entries=sorted((i for i in z.infolist()if i.filename.startswith(ROOT+'deep-functions/')),key=lambda i:(i.filename.split('/')[-1],i.filename))
 for n,i in enumerate(entries):
  info=tarfile.TarInfo(i.filename[len(ROOT):]);info.size=i.file_size;info.mtime=0;info.mode=0o644
  with z.open(i) as f:tar.addfile(info,f)
  rows.append({'path':info.name,'bytes':i.file_size,'zip_member_crc32':format(i.CRC,'08x')})
  if n%80==0:print(n,len(entries),'seconds',round(time.monotonic()-t,1),'compressedbytes',dest.stat().st_size,flush=True)
(B/'output/solid-analysis-container.json').write_text(json.dumps({'path':'analysis-evidence.tar.xz','format':'POSIX tar with XZ/LZMA2 solid compression,64MiBdictionary','members':rows,'why':'Lossless cross-module compression to preserve all acquired analysis records while retaining every historical ZIP member under persistence budget. Extract into wasm-deep-follow-up directory to materialize deep-functions/.','no_record_omissions':True},indent=2));print('FINAL',dest.stat().st_size,'seconds',round(time.monotonic()-t,1),flush=True)
