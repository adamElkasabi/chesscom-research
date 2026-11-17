#!/usr/bin/env python3
"""Bounded structural parser for the observed q8mix container; no forward pass or dequantization claim."""
import argparse,struct,json,hashlib,collections,math
from pathlib import Path

def parse(path):
 b=Path(path).read_bytes();p=0
 def read(n):
  nonlocal p
  if n<0 or p+n>len(b):raise ValueError('out-of-bounds at '+str(p))
  x=b[p:p+n];p+=n;return x
 def u64():return struct.unpack('<Q',read(8))[0]
 assert read(4)==b'json','unknown container marker';n=u64();metadata=json.loads(read(n));count=u64();assert count<10000
 records=[]
 for i in range(count):
  start=p;n=u64();assert n<1024;name=read(n).decode('utf8');bits=read(1)[0];assert bits in(8,16,32)
  scalar=struct.unpack('<f',read(4))[0]if bits!=32 else None
  if scalar is not None:assert math.isfinite(scalar)
  length=u64();assert length<100_000_000;data=p;payload=read(length*bits//8)
  records.append(dict(index=i,record_offset=start,name=name,bits=bits,scalar_f32=scalar,element_count=length,payload_offset=data,payload_bytes=len(payload),payload_sha256=hashlib.sha256(payload).hexdigest()))
 assert p==len(b),'unparsed trailer'
 return dict(file_bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),metadata=metadata,record_count=count,bits_record_counts=dict(collections.Counter(x['bits']for x in records)),element_count=sum(x['element_count']for x in records),end_offset=p,unparsed_bytes=len(b)-p,qualification='Structurally consistent parse, validated by native load of same file. Tensor names/counts are evidence; scalar dequantization and full forward equations not independently recovered.',records=records)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('model');a.add_argument('output');args=a.parse_args();Path(args.output).write_text(json.dumps(parse(args.model),indent=2)+'\n')
