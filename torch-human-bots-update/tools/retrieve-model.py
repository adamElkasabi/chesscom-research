#!/usr/bin/env python3
"""Explicit opt-in download; refuses hash drift. Does not run anything."""
import urllib.request,hashlib,sys
from pathlib import Path
url='https://www.chess.com/r2/assets-chess-engine/models/topaz_jackdaw.bin.q8mix'
expected='1f78db3d3184550ff56db7a0f14b72910b039a894dcc97ff8ef7bb8915f26423'
if len(sys.argv)!=2:raise SystemExit('Usage: python3 retrieve-model.py DESTINATION')
p=Path(sys.argv[1]);assert not p.exists(),'refusing overwrite'
with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as r:
 b=r.read(11946340)
assert len(b)==11946339,'unexpected length'
assert hashlib.sha256(b).hexdigest()==expected,'hash mismatch: URL content changed; no file written'
p.write_bytes(b)
print('Verified',p,len(b),expected)
