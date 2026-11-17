#!/usr/bin/env python3
from pathlib import Path
import json,re,hashlib,urllib.parse,urllib.request,urllib.error,time,concurrent.futures
B=Path('/var/tmp/wasm-deep');P=B/'input/website-audit';D=B/'downloads';D.mkdir(exist_ok=True);O=B/'output';O.mkdir(exist_ok=True)
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False))
S=json.loads((P/'audit-metadata/source-manifest.json').read_text());U=[json.loads(l) for l in (P/'audit-metadata/urls.jsonl').read_text().splitlines()]
leads={};scan=[];companions=[]
def lead(url,source,context='',kind='binary_candidate',derived=False):
 if not url.startswith(('https://','http://')):return
 r=leads.setdefault(url,{'url':url,'kind':kind,'discovery_sources':[],'contexts':[],'derived_from_explicit_template':derived})
 if source not in r['discovery_sources']:r['discovery_sources'].append(source)
 if context and context not in r['contexts']:r['contexts'].append(context[:700])
# Every historical literal is explicitly dispositioned,even non-resolvable templates/doc links.
historical=json.loads((P/'wasm-analysis/wasm-url-references.json').read_text())
for r in historical:
 lit=r['literal'];rec={'literal':lit,'reference_id':r['reference_id'],'source_ids':r['source_ids']}
 if '${' in lit or '$i' in lit:rec['disposition']='Template: resolved below where package/loop metadata is available; no guessed variable values.'
 elif 'github.com' in lit:rec['disposition']='Repository/documentation reference,not itself a WASM binary.'
 else:
  u=urllib.parse.urljoin('https://www.chess.com/',lit);lead(u,r['reference_id'],kind='historical_binary_candidate',derived=not lit.startswith('http'));rec.update({'resolved_url':u,'disposition':'Unauthenticated GET scheduled.'})
 r['followup_disposition']=rec
for s in S:
 rel=s.get('evidence_copy') or s['location'];p=P/rel
 if not p.is_file() or p.suffix not in ['.js','.mjs','.cjs','.html','.css','.md','.txt','.json','.jsonl']:continue
 # Avoid rescanning identical evidence blobs while retaining source aliases.
 raw=p.read_bytes();digest=hashlib.sha256(raw).hexdigest()
 if any(x['sha256']==digest for x in scan):continue
 t=raw.decode('utf8',errors='replace');scan.append({'source_id':s['id'],'location':rel,'bytes_read':len(raw),'sha256':digest,'limits':'Complete text read and loader/asset-reference scan; not all functions semantically interpreted.'})
 for m in re.finditer(r'(?:https?://[^\s"\'`<>\\]+|(?:\.?\.?/|r2/|bundles/)[^\s"\'`<>\\]*)\.(?:wasm|data|bin|model|pt|onnx|weights|nnue)(?:\?[^\s"\'`<>]*)?',t):
  v=m[0];companions.append({'source_id':s['id'],'literal':v,'offset':m.start(),'context':t[max(0,m.start()-130):m.end()+150]})
  if v.endswith('.wasm') and '${' not in v and '$i' not in v:
   u=urllib.parse.urljoin('https://www.chess.com/',v)
   # Bare engine-relative runtime strings require the loader base,not the website root.
   if v.startswith(('http','/r2/','r2/','/bundles/','bundles/','/rive-wasm/')):lead(u,s['id'],t[max(0,m.start()-100):m.end()+100],derived=not v.startswith('http'))
 for m in re.finditer(r'"name":"(@rive-app/[^"\n]+)","version":"([^"\n]+)"',t):
  name,version=m.groups()
  for host,suffix in [('https://unpkg.com/','/rive.wasm'),('https://cdn.jsdelivr.net/npm/','/rive_fallback.wasm')]:lead(host+name+'@'+version+suffix,s['id'],m[0],kind='resolved_rive_package_template',derived=True)
  if 'rive_threads.wasm' in t:lead('https://unpkg.com/'+name+'@'+version+'/rive_threads.wasm',s['id'],'Threads path appears in same saved package; runtime gate still applies.',kind='resolved_rive_package_template',derived=True)
# Exact saved fetch-assets.sh loop supplies part range0..5 (not brute force).
for i in range(6):lead(f'https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e-part-{i}.wasm','saved fetch-assets.sh','for i in0 1 2 3 4 5; multipart loader source must confirm concatenation.',kind='multipart_engine_part',derived=True)
# Explicit existing255/285 CEE URLs already known from downloaded-origin records.
for p in (P/'wasm-analysis/modules').glob('*/structure.json'):
 d=json.loads(p.read_text());lead(d['original_url_from_saved_download_script'],str(p.relative_to(P)))
# Versions254/285 and default/no-simd are literal loader choices in saved bundles.
for v in ['1.130.254','1.130.285']:
 for mode in ['default','no-simd']:lead(f'https://www.chess.com/r2/assets-chess-engine/explanation-engine/{v}/{mode}/explanation-engine.wasm','saved CEE version/SIMD loader branches','Version/base/SIMD path reconstructed from explicit frontend constants.',kind='explicit_version_and_SIMD_branch',derived=True)
# Retrieve only concrete public leads. No credentials,cookies,source-map guesses or private model-key attempts.
def get(rec):
 r=dict(rec);url=r['url'];name=hashlib.sha256(url.encode()).hexdigest();dest=D/(name+'.body');start=time.monotonic();r.update({'method':'GET','credentials':'none','max_download_bytes':268435456,'attempt_count':1})
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; passive public WASM research)','Accept':'*/*'})
  with urllib.request.urlopen(req,timeout=35) as res:
   headers=dict(res.headers.items());r.update({'http_status':res.status,'final_url':res.url,'headers':{k:('[OMITTED]' if k.lower()=='set-cookie' else v) for k,v in headers.items()}});h=hashlib.sha256();n=0
   with dest.open('wb') as f:
    while True:
     data=res.read(1024*1024)
     if not data:break
     n+=len(data)
     if n>r['max_download_bytes']:raise RuntimeError('Response exceeded explicit256MiB body limit; incomplete response not a binary identity.')
     h.update(data);f.write(data)
   prefix=dest.read_bytes()[:8];r.update({'bytes':n,'sha256':h.hexdigest(),'body_path':str(dest),'magic_prefix':prefix.hex(),'is_core_wasm':prefix[:4]==b'\0asm' and prefix[4:]==b'\x01\0\0\0','complete_response':True})
   if prefix[:4]!=b'\0asm' and rec['kind']!='multipart_engine_part':r['interpretation']='Retrieved non-WASM body; not counted as a module.'
 except urllib.error.HTTPError as e:r.update({'http_status':e.code,'error':str(e),'complete_response':False})
 except Exception as e:r.update({'error':repr(e),'complete_response':False})
 r['elapsed_seconds']=round(time.monotonic()-start,3);print(r.get('http_status','ERROR'),r.get('bytes',0),url,flush=True);return r
results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for r in pool.map(get,list(leads.values())):
  results.append(r);dump(O/'retrieval-log.json',results)
# Retrieve actual JS wrappers for newly discovered concrete engine/Rive names (same stems declared in paths).
wrappers=[]
for r in results:
 if not r.get('is_core_wasm') or r['kind']=='multipart_engine_part':continue
 url=r['url']
 if url.endswith('/rive.wasm'):j=url[:-len('rive.wasm')]+'rive.js'
 elif 'rive_fallback' in url or 'rive_threads' in url:continue
 else:j=url[:-5]+'.js'
 if j not in [x['url'] for x in wrappers]:wrappers.append(get({'url':j,'kind':'companion_loader_candidate','discovery_sources':[url],'contexts':['Same-stem wrapper; candidate until body inspected.'],'derived_from_explicit_template':True}))
dump(O/'companion-loader-retrieval.json',wrappers);dump(O/'historical-reference-dispositions.json',historical);dump(O/'discovery-source-scan.json',scan);dump(O/'companion-reference-inventory.json',companions)
# Build hash inventory without conflating URL aliases and modules. Existing originals always retained.
binaries={}
for p in sorted((P/'wasm-analysis/modules').glob('*/module.wasm')):
 raw=p.read_bytes();sha=hashlib.sha256(raw).hexdigest();d=json.loads((p.parent/'structure.json').read_text());binaries[sha]={'sha256':sha,'bytes':len(raw),'path':str(p),'existing_module_id':p.parent.name,'urls':[d['original_url_from_saved_download_script']],'classification':'available baseline module','provenance':['previous verified audit']}
for r in results:
 if r.get('is_core_wasm') and r.get('complete_response'):
  a=binaries.setdefault(r['sha256'],{'sha256':r['sha256'],'bytes':r['bytes'],'path':r['body_path'],'urls':[],'classification':'newly retrieved core module','provenance':[]})
  if r['url'] not in a['urls']:a['urls'].append(r['url'])
  a['provenance'].append(r['url'])
# Multipart assembly requires confirming the actual wrapper ordering; keep parts as parts until that batch.
for i,a in enumerate(binaries.values(),1):a['binary_id']=a.get('existing_module_id') or f'new-binary-{i:03d}'
dump(O/'binary-inventory.json',list(binaries.values()))
print('DONE public retrievals',len(results),'unique binaries',len(binaries),'wrappers',len(wrappers),flush=True)
