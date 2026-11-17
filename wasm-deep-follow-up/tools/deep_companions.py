#!/usr/bin/env python3
from pathlib import Path
import re,json,urllib.request,urllib.parse,urllib.error,hashlib
B=Path('/var/tmp/wasm-deep');O=B/'output';D=B/'downloads';rows=json.loads((O/'companion-loader-retrieval.json').read_text());new=[];maps=[]
loader=D/'torch-part-loader.js';new.append({'url':'https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js','method':'GET','retrieval_tool':'curl-fsSL','status':'successful curl-fsSL exit0; exact numeric response headers not captured','body_path':str(loader),'bytes':loader.stat().st_size,'sha256':hashlib.sha256(loader.read_bytes()).hexdigest(),'evidence':'IS_ASYNCIFY=1;enginePartsCount=6;Buffer.concat buffers in numeric part order.'})
for rec in rows:
 if not rec.get('body_path'):continue
 t=Path(rec['body_path']).read_text(errors='replace')
 for m in re.finditer(r'sourceMappingURL=([^\s*]+)',t):
  lit=m[1].rstrip('/');u=urllib.parse.urljoin(rec['url'],lit)
  if u in [r['url'] for r in maps]:continue
  r={'url':u,'discovery_source':rec['url'],'literal':lit,'method':'GET','credentials':'none'}
  try:
   with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as response:raw=response.read(15000000);r.update({'http_status':response.status,'headers':{k:('[OMITTED]' if k.lower()=='set-cookie' else v) for k,v in response.headers.items()}})
   p=D/(hashlib.sha256(u.encode()).hexdigest()+'.map');p.write_bytes(raw);r.update({'body_path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()});j=json.loads(raw);r['map_source_count']=len(j.get('sources',[]));r['source_names']=j.get('sources',[]);r['sources_content_present']=bool(j.get('sourcesContent'))
  except Exception as e:r['error']=repr(e)
  maps.append(r);print(r.get('http_status'),u,flush=True)
# Snapshot exact loader excerpts for marshalling/shared-memory/parts/resources,without claiming .data property references are assets.
refs=[]
for r in rows+new:
 if not r.get('body_path'):continue
 t=Path(r['body_path']).read_text(errors='replace')
 for pattern in [r'enginePartsCount',r'Buffer\.concat',r'loadParts',r'\.data["\'`]',r'["\'`][^"\'`\n]{1,160}\.(?:model|pt|onnx|weights|nnue|bin|data)["\'`]',r'wasmMemory',r'SharedArrayBuffer',r'new WebAssembly\.Memory',r'locateFile',r'getWasmTableEntry',r'invoke_[a-z]+',r'\.wasmBinary',r'\.instantiateStreaming']:
  matches=list(re.finditer(pattern,t))
  for m in matches[:30]:refs.append({'source_url':r['url'],'pattern':pattern,'offset':m.start(),'excerpt':t[max(0,m.start()-150):m.end()+350]})
(O/'additional-companion-retrieval.json').write_text(json.dumps(new+maps,indent=2));(O/'loader-mechanism-contexts.json').write_text(json.dumps(refs,indent=2));print('DONE additional',len(new+maps),'loadercontexts',len(refs))
