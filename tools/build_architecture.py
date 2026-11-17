#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,collections,hashlib,gzip,shutil,urllib.parse
sys.path.insert(0,str(Path(__file__).resolve().parent));from collection_layout import route
B=Path('/var/tmp/chess-forensic');O=B/'output/website-audit';P=O/'history/prior-audit';M=O/'audit-metadata';R=O/'registries';W=O/'wasm-analysis'
def load(p):return json.loads(p.read_text())
def dump(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,ensure_ascii=False))
def put(p,t):rel,t=route(Path(p).relative_to(O).as_posix(),t);p=O/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(t)
S=load(M/'source-manifest.json');SM={s['id']:s for s in S};byloc={s['location']:s for s in S}
for p in [M/'public-request-log.json',M/'dns-tls-observations.json']:
 if str(p.relative_to(O)) not in byloc:
  r={'id':f'SRC-{3000+sum(int(s["id"].split("-")[1])>=3000 for s in S):04d}','location':str(p.relative_to(O)),'type':'new_passive_observation_log','bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'review_status':'fully reviewed recorded responses/DNS/TLS; no authenticated runtime access','incorporated':True,'limits':'Per-response observation only; not full deployment topology or origin inspection.'};S.append(r);SM[r['id']]=r;byloc[r['location']]=r
F=[]
def add(title,cat,desc,sources,artifact=None,evidence='',confidence='CONFIRMED',alternatives='No alternative to the exact stored declaration; its runtime applicability may differ.',unknowns='Current authenticated cloud behavior and unobserved branches are not established.',related=None):
 fid=f'FND-{30000+len(F):05d}';f={'id':fid,'title':title,'category':cat,'description':desc,'classification':confidence,'verification_status':'direct stored evidence reviewed' if confidence=='CONFIRMED' else 'qualified inference / external historical report','source_references':sources,'artifact':artifact,'evidence':evidence,'confidence':confidence,'alternative_explanations':alternatives,'remaining_unknowns':unknowns,'related_findings':related or []};F.append(f);return fid
pub=lambda n:next(s['id'] for s in S if s['location']==f'evidence/new-public/PUBLIC-{n:03d}.txt')
ps=byloc['audit-metadata/public-request-log.json']['id'];tls=byloc['audit-metadata/dns-tls-observations.json']['id']
TECH=[]
def tech(layer,name,confidence,evidence,sids,scope,alternative='Different products/services may use other stacks; no exclusive platform-wide claim.'):
 fid=add(name+' — '+layer,'technology_stack',scope,sids,evidence=evidence,confidence=confidence,alternatives=alternative)
 TECH.append({'layer':layer,'technology':name,'classification':confidence,'evidence':evidence,'source_ids':sids,'scope':scope,'alternative_explanations':alternative,'finding_id':fid})
tech('Backend language','PHP','STRONGLY INDICATED','Public job posting explicitly requests PHP/Symfony; live public response pool label k8s-prod-fpm-catch-all.',[pub(3),ps],'PHP is strongly indicated for the main website. The fpm label is infrastructure naming evidence,not direct process inspection; CEAC analysis service language remains unknown.')
tech('Backend framework','Symfony','STRONGLY INDICATED','PHP job advert names Symfony; saved route token/default/requirement/host tables follow Symfony routing conventions.',[pub(3),'SRC-0090'],'Symfony-based web tier historically documented and supported by client routing artifacts; no exact deployed Symfony version or controller source retrieved.')
tech('Database','MySQL / Cloud SQL Enterprise Plus','CONFIRMED','2024-03-11 Google Cloud article authored by Chess.com principal engineer: migration to Cloud SQL for MySQL Enterprise Plus; independent MySQL customer page.',[pub(1),pub(2)],'Confirmed publicly reported use of MySQL and Cloud SQL Enterprise Plus,not an inspection of a live database. Article specifically discusses settings and other persisted domains; no endpoint-to-cluster mapping.')
for n in ['ScyllaDB','Elasticsearch','Redis']:
 tech('Data systems',n,'CONFIRMED','Google Cloud article explicitly lists MySQL,ScyllaDB,Elasticsearch and Redis among operational databases.',[pub(1)],'Confirmed use reported in the 2024 engineering article. Exact current versions,schemas,keys,ownership and service assignment remain unknown.')
tech('ORM / data access','Doctrine','PROBABLE','Expired PHP backend job posting names Doctrine.',[pub(3)],'Historically advertised stack; no composer.lock,entity mapping,Doctrine connection config or server source available. Do not assert all current services use Doctrine.')
for n,pat in [('Vue','Vue compiled __name,__vccOpts declarations and versioned vendor imports'),('Pinia','Pinia imports and createPinia usage'),('Svelte runtime','svelte-related style/runtime markers and compiled component lifecycle helpers')]:
 tech('Frontend',n,'CONFIRMED' if n!='Svelte runtime' else 'STRONGLY INDICATED',pat,['SRC-0090'],'Saved analysis/play bundles contain these client implementation indicators. Product/page-specific and historical; exact major versions need literal package metadata. Vue and Svelte-related compiled code can coexist.')
tech('UI framework','Custom cc-* components','CONFIRMED','367 recovered implementation declarations/references across stored code; cc-button,cc-icon,cc-avatar,cc-select,cc-tooltip among literal names.',['SRC-0090'],'Compiled component declarations and current design-system stylesheet establish a custom shared component layer; the inventory is declaration-level,not a complete runtime tree.')
tech('CSS framework','Custom design system; no generic framework established','CONFIRMED','Four fetched named stylesheets; custom --color/--font/--motion tokens and cc-* selectors.',[byloc['evidence/new-public/PUBLIC-007.css']['id']],'Custom CSS is directly observed. Bootstrap,Tailwind and Material UI are not established by this batch; absence of recognized markers is not proof of absence.')
tech('JavaScript','JavaScript and compiled modular bundles','CONFIRMED','Existing source files,ES imports,workers,dynamic chunk names and package paths.',['SRC-0090'],'Delivered JavaScript is direct evidence; TypeScript authoring is probable from ecosystem/compiled patterns,not proven for every module.')
tech('Architecture pattern','Hybrid multi-page/client-component frontend','STRONGLY INDICATED','Saved pages contain server-provided HTML/bootstrap data and import page-specific client packages; reactive components update analysis state.',['SRC-0090','SRC-0781',ps],'Not a single uniform SPA. Server-rendered shell plus client-rendered applications is supported; exact SSR framework/template engine unknown.')
tech('Backend architecture','Separate web / analysis / verification service boundaries','CONFIRMED','Game Review WebSocket host,run-search variants,BrilliantVerification RPC definitions and main web routes.',['SRC-0090'],'Observable API boundaries,not proof of a specific Kubernetes pod count,microservice source organization,controller class tree or one service per protocol.')
tech('Web server / edge','Cloudflare edge','CONFIRMED','New public responses: Server:cloudflare,CF-RAY,cf-cache-status,Cloudflare NEL report host.',[ps,tls],'Observed edge response; origin web server may differ and is not exposed by Server header. Apache,Nginx,IIS unknown.')
tech('Application runtime','FPM-named Kubernetes web pool','STRONGLY INDICATED','X-Chesscom-Server-Pool and X-Chesscom-Ingress-Pool: k8s-prod-fpm-catch-all.',[ps],'Strong naming evidence for Kubernetes/FPM web path. Exact PHP version,container image,orchestration topology and ingress implementation unknown.')
tech('Hosting','Google Cloud multi-region database deployment','CONFIRMED','Google Cloud engineering article describes databases in several regions and Cloud SQL migration.',[pub(1)],'Confirmed published deployment at article date; not proof every service or asset origin lives in Google Cloud.')
tech('Build system','Vite-style asset pipeline / hashed client packages','CONFIRMED','/bundles/app/vite/ stylesheets,/r2/client-packages/<page>/<version>/ imports and hashed chunks.',['SRC-0090',ps],'Observed output conventions. Rolldown-related wrappers appear in some packages but exact full build pipeline and all tool versions unknown.')
tech('WASM compiler','Emscripten-style C/C++ toolchain','STRONGLY INDICATED','Module.ccall,HEAPU8,embind,Asyncify,env.invoke_*,C++ exception imports and native .cc/.cpp strings.',['SRC-0031'],'Generated runtime fingerprint strongly supports Emscripten/LLVM-family C/C++ compilation. No name,producers or DWARF custom sections in the five binaries; exact compiler/toolchain versions unknown.')
# Explicitly investigate requested alternatives without inventing negative certainty.
for layer,names in {'Backend alternatives':['C# / ASP.NET / ASP.NET Core / MVC / Web Forms / Razor Pages','Node.js / Express / NestJS','Python / Django / Flask / FastAPI','Java / Spring / Spring Boot / Jakarta EE','Ruby / Rails','Go / other service languages'], 'Other PHP frameworks':['Laravel','CodeIgniter / CakePHP / Yii','WordPress / Drupal / Joomla'], 'Database alternatives':['MariaDB','Microsoft SQL Server','PostgreSQL','SQLite','Oracle','MongoDB'], 'ORM alternatives':['Entity Framework','Eloquent','Hibernate','Sequelize / Prisma','SQLAlchemy / Django ORM','Active Record / raw SQL / custom DAL']}.items():
 for name in names:TECH.append({'layer':layer,'technology':name,'classification':'UNKNOWN','evidence':'No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof.','source_ids':[ps],'scope':'Investigated as an alternative; not confirmed and not ruled out elsewhere in a large polyglot platform. Historical CTO search excerpt mentions Java,Jetty,CometD,MyBatis and Mongo; original page fetch403,so not promoted into a current direct observation.','finding_id':add(name+' remains unconfirmed','technology_alternatives','Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.',[ps],confidence='UNKNOWN',alternatives='Technology could be used by services not visible in the inspected assets.')})
dump(M/'technology-evidence.json',TECH)
# Actual observed route-name response relationship,without inventing controller class names.
for r in load(M/'public-request-log.json'):
 if 'www.chess.com' in r['url'] and r['id'] in ['PUBLIC-004','PUBLIC-005']:
  add('Public response matched route '+r['headers'].get('X-Chesscom-Matched','unknown'),'routing',r['url']+' returned200with matched route metadata. No controller method/class or DB query captured.',[ps],artifact='audit-metadata/public-request-log.json',evidence=json.dumps(r['headers'],ensure_ascii=False),unknowns='Physical controller,PHPmethod,authorization middleware and downstream query remain unknown.')
add('Public response security headers','security','Two newly fetched unauthenticated HTML responses carry HSTSmax-age31536000/includeSubDomains,X-Content-Type-Options:nosniff,X-Frame-Options:SAMEORIGIN,CSPframe-ancestors self,andCOOPsame-origin-allow-popups. These are per-response observations,not all-site policy guarantees.',[ps],artifact='audit-metadata/public-request-log.json',evidence='See PUBLIC-004 and PUBLIC-005 response header objects.',unknowns='No authenticated session,CORS credential flow,CSRF processing,rate-limit test or full cookie attributes preserved. No CSP-script-src policy inferred from frame-ancestors alone.')
add('Reported clock/date conflict retained','provenance','System/session date is2026-11-13 while public Date headers report2026-11-15 and historical artifacts include later timestamps. Preserve original raw labels; do not use this discrepancy to invent chronology or assert current deploy age.',[ps],artifact='audit-metadata/public-request-log.json',confidence='CONFIRMED',evidence='Date headers and source labels retained; new verification is labelled by batch,not silently normalized.')
# Granular UI findings and CSS artifacts.
components=load(R/'components.json')
for c in components:
 sources=sorted(set(x['source_id'] for x in c['occurrences'] if x['source_id']));c['finding_id']=add('Implementation component '+c['component_name'],'ui_components',c['implementation_evidence']+'. '+c['purpose']+' '+c['relationships'],sources,artifact='registries/components.json',evidence=c['occurrences'][0]['excerpt'],unknowns='Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.')
dump(R/'components.json',components)
css=load(R/'design-system.json')
for c in css:add('Stylesheet '+Path(c['file']).name,'design_system',f'{len(c["variables"])} CSS variable declarations,{len(c["media_queries"])}media queries,{len(c["selectors"])}selector records; font faces/families/exported breakpoints retained.',[c['source_id']],artifact='registries/design-system.json',evidence=json.dumps({'variables':c['variables'][:3],'export_blocks':c['export_blocks'][:1]}),unknowns='Cascade order/themes matter; repeated variable names may have different scoped values. No claim the extracted selector inventory is a complete visual specification.')
# Per-module findings,complete import/export records and exact function/index/signature inventories.
modules=[];impex=[];funcstats=[];newmanifest=[]
def importpurpose(name):
 if name.startswith('invoke_'):return 'Emscripten-style indirect-call/exception adapter; the signature encodes ABI kinds. Not a business-logic function.'
 if '__cxa' in name or 'llvm_eh' in name:return 'C++ exception-handling ABI support,not a web API.'
 if name.startswith('fd_'):return 'WASI-style file descriptor shim. Host capability depends on JS implementation; not direct unrestricted OS access.'
 if name=='random_get':return 'Host-provided random bytes. Does not prove a particular cryptographic protocol.'
 if 'emscripten' in name:return 'Emscripten runtime/heap/time/async support; exact purpose depends on the specific import name and glue excerpt.'
 if 'syscall' in name or 'mmap' in name:return 'POSIX/Emscripten filesystem/mapping compatibility shim; not evidence of private server filesystem access.'
 return 'Unknown business/runtime purpose unless mapped to a concrete loader implementation. Minified import names are not semantic names.'
for md in sorted((W/'modules').glob('module-*')):
 d=load(md/'structure.json');sid=next(s['id'] for s in S if s.get('location')==str((md/'module.wasm').relative_to(O)));loaderid=next(s['id'] for s in S if s.get('location')==str((md/'loader.js').relative_to(O)));loader=(md/'loader.js').read_text();mid=d['module_id'];modrel=str(md.relative_to(O))
 d['ownership']='Custom explanation engine / embedded engines' if 'explanation-engine' in d['original_location'] else 'Third-party Stockfish engine build' if 'stockfish' in d['original_location'] else 'Proprietary Torch Lite chess-engine build; exact source ownership not inspected'
 fid=add(mid+' complete structural inventory','wasm_structure',f'{d["bytes"]}bytes; SHA256{d["sha256"]}; {len(d["functions"])}defined functions,{sum(x["kind"]=="function" for x in d["imports"])}imported functions,{len(d["exports"])}exports. All section offsets,types,limits,globals,elements,data and function body spans retained.',[sid],artifact=modrel+'/structure.json',evidence='Magic'+d['magic']+';version'+str(d['version'])+';no custom sections.' if not d['custom_sections'] else json.dumps(d['custom_sections']))
 add(mid+' function and call-graph analysis','wasm_functions',f'{d["direct_call_pairs"]}direct caller/callee pairs;{d["direct_call_sites"]}static direct-call sites;{d["indirect_call_sites"]}indirect-call sites. Exact direct call indices recovered from full WAT. Indirect dispatch targets not resolved; opcode frequencies are syntactic counts,not execution profiling.',[sid],artifact=modrel+'/functions.json',evidence='See call-graph.jsonl.gz and opcode-statistics.json.',related=[fid])
 add(mid+' strings and data offsets','wasm_strings',f'{d["ascii_candidates"]}ASCII candidates,{d["relevant_string_candidates"]}keyword-relevant candidates,{d["utf16_candidates"]}UTF16candidates. Strings linked to original file offsets and active data memory addresses when constant-resolvable. Random code/weight bytes can resemble text.',[sid],artifact=modrel+'/strings.txt',evidence='All-ASCII candidates are separately gzipped; relevant output is not a semantic analysis of every string.',related=[fid])
 add(mid+' memory/host boundary','wasm_memory',json.dumps({'defined_memories':d['memories'],'imported_memories':[x for x in d['imports'] if x['kind']=='memory'],'tables':d['tables'],'data_segments':len(d['data_segments'])}),[sid],artifact=modrel+'/structure.json',evidence='Memory limits use64KiBpages; shared flag is explicit.',related=[fid])
 runtime=load(md/'runtime-observation.json');add(mid+' new controlled instantiation','wasm_runtime','Bounded Node instantiation succeeded with explicitly stubbed imports; this is not engine search/review correctness. Initial module003failed due unhandled imported memory,then passed using exact descriptor limits. Stack-query exports were called only when present.',[sid],artifact=modrel+'/runtime-observation.json',evidence=json.dumps(runtime.get('observation',runtime),ensure_ascii=False),related=[fid],unknowns='No native whole-game review rerun,new server query,or cloud parity test. Historical successful full CEE/Human tests retained separately.')
 for direction,items in [('import',d['imports']),('export',d['exports'])]:
  for item in items:
   name=item['name'];purpose=importpurpose(name) if direction=='import' else ('Named CEE native API; wrapper passes protobuf handles/buffers where present.' if name.startswith('CEE_') else 'Runtime/engine export; semantic identity requires wrapper/call-site evidence.')
   # Preserve exact minified or descriptive names; find literal ABI assignments in glue.
   candidates=[name+':','.'+name,'["'+name+'"]','.'+name+'=']
   pos=next((loader.find(q) for q in candidates if loader.find(q)>=0),-1);snippet=loader[max(0,pos-100):pos+700] if pos>=0 else ''
   rec={'module_id':mid,'direction':direction,**item,'apparent_purpose':purpose,'loader_character_offset':pos if pos>=0 else None,'loader_excerpt':snippet,'semantic_confidence':'PROBABLE' if pos>=0 and len(name)>3 else 'UNKNOWN','evidence_confidence':'CONFIRMED declaration'}
   rec['finding_id']=add(mid+' '+direction+' '+(item.get('module','')+'.' if direction=='import' else '')+name,'wasm_imports_exports',purpose,[sid,loaderid],artifact=modrel+'/imports-exports-annotated.json',evidence=json.dumps(rec,ensure_ascii=False),unknowns='Name/type are confirmed. Semantic label is qualified; a literal loader match can be unrelated until its actual property/call context is reviewed.',related=[fid]);impex.append(rec)
 annotated=[x for x in impex if x['module_id']==mid];dump(md/'imports-exports-annotated.json',annotated)
 # Relevant glue mappings for actual exported CEE buffer APIs.
 if 'explanation-engine' in d['original_location']:
  start=loader.find('let api_call_map');end=loader.find('function startCall',start)
  put(md/'javascript-bridge-excerpt.js',loader[start:end])
  add(mid+' exact protobuf buffer boundary','wasm_javascript','js_buf_to_c_buf allocates length*BYTES_PER_ELEMENT,HEAPU8.set copies bytes. CEE_NewFeature(gamePoint,featureId,ptr,len) returns handle and frees input buffer in finally. CEE_Run(handle,0) is async; imported callback copies HEAPU8.subarray(ptr,ptr+size).slice() into postMessage({proto,is_final}). The protocol payload is real protobuf,not JSON.',[sid,loaderid],artifact=modrel+'/javascript-bridge-excerpt.js',evidence='CEE_NewFeature has native(i32,i32,i32,i32)->i32;CEE_Run(i32,i32)->i32. Import callback and exact wrapper retained.',related=[fid])
  add(mid+' actual CEE_InitWithOpts native signature','wasm_javascript','Binary export CEE_InitWithOpts has two i32parameters and no result. It forwards to an internal function through Asyncify instrumentation. Earlier JS-functionlength0was not the native ABI. Interpretation as(ptr,len) is supported by protobuf wrapper conventions but the generic initialization call itself is not proven by this signature alone.',[sid,loaderid],artifact=modrel+'/focused-decompilation/CEE_InitWithOpts.pseudocode.txt',evidence=json.dumps(next(x for x in d['exports'] if x['name']=='CEE_InitWithOpts')),related=[fid],unknowns='No claim of arbitrary initialization-option compatibility or a successful TorchHuman toggle from InitWithOpts.')
  add(mid+' focused native function reconstruction','wasm_decompilation','Five export bodies decompiled using analysis-only modules with signature-correct imported stubs for all other functions; globals/tables/memory declarations retained,but original data omitted. Full decompilation attempts failed: JS WABT memory-out-of-bounds; native process killed137under2GiBaddressspace/60sCPUbound. These failures are tooling/resource outcomes,not proof of engine invalidity.',[sid],artifact=modrel+'/focused-decompilation/results.json',evidence='CEE_Init,CEE_InitWithOpts,CEE_NewFeature,CEE_DisposeFeature,CEE_Run each decompiled successfully. Numeric fields/types/names in pseudocode are decompiler assignments,not recovered source identifiers.',related=[fid])
 # Correctly label capped selected-function excerpts (allocator can exceed50KB).
 selected=md/'selected-functions.wat';t=selected.read_text();t=t.replace(';; EXACT selected function forms',';; EXACT selected function excerpts').replace('Function names below are export names, not inferred internals.','Function names below are export names, not inferred internals.\n;; Each capture is capped near50KB; large functions may end mid-body. Full function byte spans,signatures and complete call-site inventories remain available.');selected.write_text(t)
 # Data-free pseudocode for Torch avoids redistributing weights twice in escaped text.
 if (md/'decompilation.txt.gz').exists():
  with gzip.open(md/'decompilation.txt.gz','rt') as src,(md/'decompilation-code-only.txt').open('w') as dst:
   dst.write('// WABT decompilation with data declarations removed to avoid duplicated binary payloads. Original binary and data-segment hashes retained.\n');skip=False
   for line in src:
    if line.startswith('data '):skip=True
    if skip:
     if line.rstrip().endswith(';'):skip=False
     continue
    dst.write(line)
 dump(md/'structure.json',d);modules.append(d)
 funcstats.append({'module_id':mid,'defined_functions':len(d['functions']),'imported_functions':sum(i['kind']=='function' for i in d['imports']),'exported_functions':sum(i['kind']=='function' for i in d['exports']),'exports_total':len(d['exports']),'direct_pairs':d['direct_call_pairs'],'indirect_call_sites':d['indirect_call_sites']})
dump(W/'module-manifest.json',[{k:v for k,v in d.items() if k not in ['functions','types','imports','exports','elements','globals','data_segments']} for d in modules]);dump(W/'function-counts.json',funcstats);dump(W/'imports-exports-all.json',impex)
# Map exact available origins onto old URL candidates; preserve the others as unresolved.
refs=load(W/'wasm-url-references.json')
for r in refs:
 literal=r['literal'];canonical=urllib.parse.urljoin('https://www.chess.com/',literal) if '${' not in literal and '$i' not in literal else None
 matches=[d['module_id'] for d in modules if d['original_url_from_saved_download_script']==canonical]
 if matches:r['available_matching_modules']=matches;r['retrieval_status']='Exact saved download-script URL matches available binary; historical local bytes analyzed,not re-downloaded.';r['limitation']='Current deployed-byte equality not checked.'
dump(W/'wasm-url-references.json',refs)
# New findings kept as a separate ledger and also combined with the unchanged historical ledger.
for s in S:s['extended_finding_ids']=[f['id'] for f in F if s['id'] in f['source_references']]
dump(M/'source-manifest.json',S)
with (M/'new-findings-ledger.jsonl').open('w') as z:
 for f in F:z.write(json.dumps(f,ensure_ascii=False)+'\n')
with (M/'findings-ledger.jsonl').open('w') as z:
 for line in (P/'audit-metadata/findings-ledger.jsonl').read_text().splitlines():z.write(line+'\n')
 for f in F:z.write(json.dumps(f,ensure_ascii=False)+'\n')
# Unified URL index retains every historical occurrence; new URLs extracted only from actual evidence text/observations.
urls=[json.loads(l) for l in (P/'audit-metadata/urls.jsonl').read_text().splitlines()];urlmap={u['url']:u for u in urls}
for s in S:
 if int(s['id'].split('-')[1])<3000:continue
 f=O/s['location']
 if f.suffix not in ['.html','.txt','.css','.json','.js']:continue
 text=f.read_text(errors='replace')
 found=[(m[0].rstrip('.,;'),m.start()) for m in re.finditer(r'(?:https?|wss?)://[^\s"\'`<>\\]+',text)]
 # Attribute and CSS-url references remain relative; never invent a host.
 for m in re.finditer(r'(?:href|src|action)\s*=\s*["\']([^"\']+)["\']|url\(\s*["\']?([^\s)"\']+)',text,re.I):
  literal=m[1] or m[2]
  if literal and not literal.startswith(('data:','javascript:','#','mailto:')):found.append((literal,m.start()))
 if s.get('url','').startswith('https://'):found.append((s['url'],0))
 for u,pos in found:
  if u not in urlmap:
   r={'id':f'URL-{30000+sum(int(x["id"].split("-")[1])>=30000 for x in urls):05d}','url':u,'reference_form':'absolute' if re.match(r'^(?:https?|wss?)://',u) else 'relative','type':'new_public_evidence_literal','source_ids':[],'occurrences':[],'directly_visited':False,'verification_status':'Observed literal only unless public request record matches exactly.','date':'new passive batch; raw response dates retained with conflict caveat','related_findings':[]};urls.append(r);urlmap[u]=r
  r=urlmap[u]
  if s['id'] not in r['source_ids']:r['source_ids'].append(s['id'])
  r['occurrences'].append({'source_id':s['id'],'character_offset':pos,'context':text[max(0,pos-100):pos+250]})
for req in load(M/'public-request-log.json'):
 if req['url'] in urlmap:urlmap[req['url']]['directly_visited']='New unauthenticated GET';urlmap[req['url']]['verification_status']='HTTP'+str(req.get('status','error'))+';see PUBLICrequestlog; no authenticated access.'
with (M/'urls.jsonl').open('w') as z:
 for u in urls:z.write(json.dumps(u,ensure_ascii=False)+'\n')
# Linkable new finding shards retain every mandatory evidence/confidence field.
finddir=O/'findings';finddir.mkdir(exist_ok=True);shards=[]
for start in range(0,len(F),60):
 batch=F[start:start+60];name=f'extended-findings-{start//60+1:03d}.md';shards.append(name);body=['# Extended findings\n\n[Master index](../00_MASTER_INDEX.md)\n']
 for f in batch:
  body+=['\n<a id="'+f['id']+'"></a>\n## '+f['id']+' — '+f['title']+'\n\n',f['description']+'\n\n','- Category: '+f['category']+'\n- Classification/confidence: '+f['classification']+'\n- Verification: '+f['verification_status']+'\n- Sources: '+', '.join(f['source_references'])+'\n- Alternatives: '+f['alternative_explanations']+'\n- Remaining unknowns: '+f['remaining_unknowns']+'\n- Related findings: '+(', '.join(f['related_findings']) or 'See related source/module/category records')+'\n']
  if f['artifact']:body.append('- [Exact supporting artifact](../'+f['artifact']+')\n')
  if f['evidence']:body.append('\n```text\n'+f['evidence']+'\n```\n')
 put(finddir/name,''.join(body))
put(finddir/'FINDINGS_INDEX.md','# Findings index\n\n[Master index](../00_MASTER_INDEX.md)\n\n'+''.join('- ['+n+']('+n+')\n' for n in shards)+'\n- [All21,056 prior recovery findings](../history/prior-audit/findings/FINDINGS_INDEX.md)\n- [Combined machine ledger](../audit-metadata/findings-ledger.jsonl)\n\nPrior records retain their original classification vocabulary. Their verified observations refer to stored declarations/results,not necessarily current website runtime. Extended records use CONFIRMED/STRONGLY INDICATED/PROBABLE/SPECULATIVE/UNKNOWN.\n')
COUNTS={'overall_status':'PARTIALLY AUDITED; private backend/schema/cloud configuration partly UNVERIFIABLE','prior_source_occurrences':2049,'new_source_records':len(S)-2049,'total_source_records':len(S),'original_markdown_occurrences_inspected':10,'loose_original_markdown_files':6,'unique_original_markdown_contents':8,'offline_files_reprocessed_in_new_batch':len(load(M/'new-offline-source-scan.json')),'prior_findings':21056,'new_findings':len(F),'total_finding_records':21056+len(F),'new_findings_by_confidence':dict(collections.Counter(f['classification'] for f in F)),'all_url_relative_reference_literals':len(urls),'absolute_URL_literals':sum(u.get('reference_form')=='absolute' for u in urls),'prior_route_declarations':321,'prior_endpoint_candidates':235,'prior_declared_RPC_methods':241,'new_public_GET_requests':len(load(M/'public-request-log.json')),'HTML_artifacts_in_new_page_inventory':len(load(R/'page-markup-inventory.json')),'target_saved_or_fetched_page_artifacts':4,'implementation_component_declaration_variants':len(components),'CSS_files_fetched':len(css),'CSS_variable_declarations':sum(len(c['variables']) for c in css),'unique_CSS_variable_names':len(set(v['name'] for c in css for v in c['variables'])),'media_queries':sum(len(c['media_queries']) for c in css),'script_import_records':len(load(R/'script-imports.json')),'available_unique_WASM_binaries':len(modules),'WASM_reference_literals_from_prior_evidence':len(refs),'WASM_modules_structurally_analyzed':len(modules),'WASM_modules_validated':sum(d['tool_commands'][0]['exit_code']==0 for d in modules),'WASM_modules_instantiated_with_stubs':sum(load(md/'runtime-observation.json').get('returncode')==0 for md in sorted((W/'modules').glob('module-*'))),'defined_WASM_functions':sum(x['defined_functions'] for x in funcstats),'imported_WASM_functions':sum(x['imported_functions'] for x in funcstats),'exported_WASM_function_entries':sum(x['exported_functions'] for x in funcstats),'WASM_exports_all_kinds':sum(x['exports_total'] for x in funcstats),'WASM_direct_call_pairs':sum(x['direct_pairs'] for x in funcstats),'focused_CEE_export_decompilations':10,'full_module_decompilations_succeeded':3,'prior_explicit_unavailable_sources':18,'prior_gaps':16,'prior_contradictions':13}
dump(M/'completeness-metrics.json',COUNTS)
# Documentation renderer shares these reviewed in-memory records.
exec(Path('/home/user/forensic-mission-tools/render_mission.py').read_text())
print(json.dumps(COUNTS,indent=2))
