#!/usr/bin/env python3
from pathlib import Path
import json,re,urllib.parse,urllib.request,urllib.error,hashlib
B=Path('/var/tmp/wasm-deep');O=B/'output';rows=json.loads((O/'companion-loader-retrieval.json').read_text());seen={};out=[]
for r in rows:
 if not r.get('body_path'):continue
 t=Path(r['body_path']).read_text(errors='replace')
 for m in re.finditer(r'["\'`]([^"\'`\n]{0,150}(?:\.worker\.js|webgl2_advanced\.wasm))["\'`]',t):
  lit=m[1]
  if '$' in lit:continue
  u=urllib.parse.urljoin(r['url'],lit)
  if u in seen:seen[u]['sources'].append(r['url']);continue
  seen[u]={'url':u,'sources':[r['url']],'literal':lit,'context':t[max(0,m.start()-100):m.end()+180],'qualification':'Referenced generated-glue default. Runtime locateFile/worker overrides may select another resource.'}
previous=json.loads((O/'worker-and-glue-default-retrieval.json').read_text()) if (O/'worker-and-glue-default-retrieval.json').exists() else []
for r in seen.values():
 old=next((x for x in previous if x['url']==r['url']),None)
 if old:out.append(old);continue
 try:
  with urllib.request.urlopen(urllib.request.Request(r['url'],headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as res:raw=res.read(32000000);r.update({'http_status':res.status,'headers':{k:('[OMITTED]' if k.lower()=='set-cookie' else v) for k,v in res.headers.items()}})
  p=B/'downloads'/(hashlib.sha256(r['url'].encode()).hexdigest()+'.worker-body');p.write_bytes(raw);r.update({'body_path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'core_wasm':raw[:8]==b'\0asm\1\0\0\0'})
 except urllib.error.HTTPError as e:r.update({'http_status':e.code,'error':str(e)})
 except Exception as e:r['error']=repr(e)
 out.append(r);print(r.get('http_status'),r['url'],flush=True)
(O/'worker-and-glue-default-retrieval.json').write_text(json.dumps(out,indent=2))
