#!/usr/bin/env python3
from pathlib import Path
import json,re,urllib.parse,urllib.request,urllib.error,hashlib
B=Path('/var/tmp/wasm-deep');O=B/'output';refs=json.loads((O/'companion-reference-inventory.json').read_text());assets={}
for r in refs:
 lit=r['literal']
 if not re.fullmatch(r'(?:https?://[^\s]+|/?(?:bundles|r2|assets|engines)/[^\s]+)\.(?:nnue|bin|pt|onnx|bzp|weights|model|data|db|sqlite|gz|br|json)',lit,re.I):continue
 # Already-abandoned authenticated/model probes stay historical; never reprobe.
 u=urllib.parse.urljoin('https://www.chess.com/',lit)
 kind='opening-book payload' if '/books/' in u or '/book-' in u else 'NNUE evaluation parameters' if u.endswith('.nnue') else 'frontend WDL neural-network parameters' if '/wdl/' in u else 'model/data candidate; runtime dependency unproven'
 assets.setdefault(u,{'url':u,'classification':kind,'references':[],'qualification':'Literal reference does not prove this is fetched by every WASM build.'})['references'].append({'source_id':r['source_id'],'offset':r['offset'],'literal':lit})
# wdlJsonModel string is an explicit source literal even when the original broad scanner missed json extension.
assets.setdefault('https://www.chess.com/bundles/web/wdl/model.json',{'url':'https://www.chess.com/bundles/web/wdl/model.json','classification':'frontend WDL neural-network topology','references':[{'source_id':'SRC-0065 and SRC-0777','literal':"wdlJsonModel: /bundles/web/wdl/model.json"}],'qualification':'Frontend metadata reference; not automatically a CEE/Torch WASM import.'})
results=[]
for u in ['https://www.chess.com/bundles/web/wdl/model.json','https://www.chess.com/bundles/web/wdl/group1-shard1of1.bin','https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue','https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue']:
 rec={'url':u,'method':'GET','credentials':'none','source':assets.get(u)}
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30) as r:
   raw=r.read(64000001);rec.update({'http_status':r.status,'headers':{k:('[OMITTED]' if k.lower()=='set-cookie' else v) for k,v in r.headers.items()}})
  if len(raw)>64000000:rec['truncated']=True
  p=B/'downloads'/(hashlib.sha256(u.encode()).hexdigest()+'.model-body');p.write_bytes(raw);rec.update({'body_path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'complete_payload_proven':rec['http_status']==200 and not rec.get('truncated',False)})
  if u.endswith('model.json'):
   try:
    j=json.loads(raw);rec['top_level_keys']=list(j);rec['weights_manifest']=j.get('weightsManifest');rec['format']=j.get('format');rec['generatedBy']=j.get('generatedBy')
   except Exception:pass
 except urllib.error.HTTPError as e:rec.update({'http_status':e.code,'error':str(e)})
 except Exception as e:rec['error']=repr(e)
 results.append(rec);print(u,rec.get('http_status'),rec.get('bytes'),flush=True)
(O/'classified-companion-assets.json').write_text(json.dumps(list(assets.values()),indent=2));(O/'model-companion-retrieval.json').write_text(json.dumps(results,indent=2))
