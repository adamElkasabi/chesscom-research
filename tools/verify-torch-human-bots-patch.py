#!/usr/bin/env python3
"""Offline verification only: never extracts, overwrites, deletes, or downloads."""
import argparse,hashlib,json,zipfile
from pathlib import PurePosixPath

def sha(b):return hashlib.sha256(b).hexdigest()
p=argparse.ArgumentParser();p.add_argument('--patch',required=True);p.add_argument('--baseline',required=True);a=p.parse_args()
with open(a.baseline,'rb') as f:
 h=hashlib.file_digest(f,'sha256').hexdigest()
assert h=='b0fc69d224b390b13f7d44fa59c19ab17eb02ceff260e51459ca80ee0b715282','wrong baseline'
with zipfile.ZipFile(a.patch) as patch,zipfile.ZipFile(a.baseline) as base:
 names=patch.namelist();assert len(names)==len(set(names)),'duplicate path'
 mn='website-audit/TORCH_HUMAN_BOTS_PATCH_MANIFEST.json';m=json.loads(patch.read(mn));expected={x['path']for x in m['files']}|{mn};assert set(names)==expected,'unexpected/missing archive member'
 assert patch.testzip() is None,'CRC failure'
 for row in m['files']:
  n=row['path'];path=PurePosixPath(n);assert not path.is_absolute() and '..'not in path.parts and n.startswith('website-audit/'),'unsafe path'
  assert not n.startswith(('website-audit/original-documentation/','website-audit/history/')),'original artifacts must not be changed'
  b=patch.read(n);assert len(b)==row['after_bytes']and sha(b)==row['after_sha256'],n+' payload mismatch'
  if row['action']=='replace':assert n in base.namelist()and sha(base.read(n))==row['before_sha256'],n+' baseline mismatch'
  else:assert row['action']=='add'and n not in base.namelist(),n+' addition collision'
 print('PASS:',len(m['files']),'listed payloads plus manifest;',sum(r['action']=='replace'for r in m['files']),'replacements. Baseline hash, payloads, paths and CRC verified.')
