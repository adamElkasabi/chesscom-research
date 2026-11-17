#!/usr/bin/env python3
from pathlib import Path
import sys,json,re,hashlib,collections,math,html,zipfile
sys.path.insert(0,'/home/user/.local/lib/audit-protobuf')
from google.protobuf.descriptor_pb2 import FileDescriptorProto,FieldDescriptorProto
from google.protobuf.json_format import MessageToDict
ROOT=Path('/home/user'); OUT=ROOT/'website-audit'; META=OUT/'audit-metadata'
S=json.loads((META/'source-manifest.json').read_text()); SM={s['id']:s for s in S}; LOC={s['location']:s for s in S}
U=[json.loads(l) for l in (META/'urls.jsonl').read_text().splitlines()]; UM={u['url']:u for u in U}
# Idempotent generation from recovered inventory; do not accumulate old IDs.
for s in S:s['findings']=[]
for u in U:
 u['related_findings']=[]
 u.pop('historical_http_observations',None)
F=[]; ROUTES=[]; SCHEMAS=[]; TRIALS=[]; SERVICES=[]; DOCBLOCKS=[]; COVER=[];GAPS=[];CONTRA=[]
TEXT={s['id']:(OUT/s['evidence_copy']).read_text(errors='replace') for s in S if s.get('evidence_copy') and s['type'] not in ['native_protobuf_descriptor']}
def text(loc):return TEXT.get(LOC.get(loc,{}).get('id'),'')
def src(loc):
 if loc not in LOC:raise KeyError(loc)
 return LOC[loc]['id']
def dump(p,obj):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,indent=2,ensure_ascii=False))
def put(p,t):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(t)
def pretty(x):return json.dumps(x,indent=2,ensure_ascii=False)
def urlids(sids):return [u['id'] for u in U if any(s in u['source_ids'] for s in sids)]
def add(cat,title,desc,sids,locator='',classification='verified observation',verification='verified',confidence='high',why='Exact content of the cited stored artifact; not a claim of current live deployment.',notes='',evidence=None,record=None):
 fid=f'FND-{len(F)+1:05d}';refs=[]
 for sid in sids:
  st=TEXT.get(sid,'');i=st.find(locator) if locator else -1
  excerpt=st[max(0,i-100):i+min(1500,max(len(locator)+160,320))] if i>=0 else ''
  refs.append({'source_id':sid,'location':SM[sid]['location'],'locator':locator or 'full structured record / document block','character_offset':i if i>=0 else None,'excerpt':excerpt})
 f={'id':fid,'category':cat,'title':title,'detailed_description':desc,'classification':classification,'evidence':evidence or refs,'url_references':[],
    'source_references':sids,'confidence':{'level':confidence,'explanation':why},'verification_status':verification,'related_findings':[],
    'additional_notes':notes,'structured_record':record}
 F.append(f)
 for sid in sids:SM[sid]['findings'].append(fid)
 return fid

def claim(cat,title,desc,locations,needle='',**kwargs):
 return add(cat,title,desc,[src(l) for l in locations],needle,**kwargs)

# Batch1 — preserve every original documentation block, not merely its summary.
seen={}
for s in S:
 if s['type']!='original_markdown':continue
 st=TEXT[s['id']]
 if s['sha256'] in seen:
  old=seen[s['sha256']]
  for fid in old:
   f=F[int(fid.split('-')[1])-1];f['source_references'].append(s['id']);s['findings'].append(fid)
  continue
 heading='Document opening';buf=[];start=1;inside=False;fids=[]
 def flush():
  global buf,start
  if not ''.join(buf).strip():buf=[];return
  block='\n'.join(buf).strip()
  fid=add('historical_documentation',heading+' — block '+str(start),block,[s['id']],
   verification='historical',classification='unknown',confidence='medium',
   why='Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.',
   evidence=[{'source_id':s['id'],'location':s['location'],'line_start':start,'line_end':start+len(buf)-1,'exact_redacted_block':block}],
   notes='This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.')
  fids.append(fid);DOCBLOCKS.append({'source_id':s['id'],'finding_id':fid,'section':heading,'line_start':start});buf=[]
 for n,line in enumerate(st.splitlines(),1):
  if line.startswith('#') and not inside:
   flush();heading=line.lstrip('# ').strip();start=n+1;continue
  if line.startswith('```'):inside=not inside
  if not line.strip() and not inside:flush();start=n+1
  else:
   if not buf:start=n
   buf.append(line)
 flush();seen[s['sha256']]=fids

# Batch2 — protobuf declarations, with namespaces and all field numbers retained.
seen_schema={}
for s in S:
 if s['type']=='rendered_protobuf_schema':
  st=TEXT[s['id']];pkgm=re.search(r'^package\s+([^;]+);',st,re.M);pkg=pkgm[1] if pkgm else ''
  key=(s['sha256'],'rendered')
  if key in seen_schema:
   for fid in seen_schema[key]:F[int(fid.split('-')[1])-1]['source_references'].append(s['id']);s['findings'].append(fid)
   continue
  fids=[];stack=[]
  for ln,line in enumerate(st.splitlines(),1):
   mm=re.match(r'\s*(message|enum|oneof|service)\s+(\w+)\s*\{',line)
   if mm:
    kind,name=mm.groups();parent='.'.join(x[1] for x in stack if x[0]!='oneof');fq='.'.join(x for x in [pkg,parent,name] if x)
    rec={'kind':kind,'full_name':fq,'name':name,'package':pkg,'source_id':s['id'],'line':ln,'source_format':'rendered proto'}
    SCHEMAS.append(rec);fid=add('data_models',f'{kind} declaration: {fq}',line.strip(),[s['id']],line.strip(),record=rec);fids.append(fid);stack.append((kind,name));continue
   if line.strip().startswith('}'):
    if stack:stack.pop()
    continue
   mf=re.match(r'\s*(?:(optional|repeated|required)\s+)?([.\w]+(?:<[^>]+>)?)\s+(\w+)\s*=\s*(-?\d+)(.*)',line)
   me=re.match(r'\s*(\w+)\s*=\s*(-?\d+)\s*;',line)
   parent='.'.join(x[1] for x in stack if x[0]!='oneof');fq='.'.join(x for x in [pkg,parent] if x)
   if mf:
    label,ft,name,num,rest=mf.groups();rec={'kind':'field','message':fq,'name':name,'number':int(num),'type':ft,'label':label or 'unspecified','oneof':next((x[1] for x in reversed(stack) if x[0]=='oneof'),None),'source_id':s['id'],'line':ln,'source_format':'rendered proto'}
    SCHEMAS.append(rec);fids.append(add('data_models',f'{fq}.{name} = {num}',line.strip(),[s['id']],line.strip(),record=rec,notes='Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.'))
   elif me and stack and stack[-1][0]=='enum':
    name,num=me.groups();rec={'kind':'enum_value','enum':fq,'name':name,'number':int(num),'source_id':s['id'],'line':ln,'source_format':'rendered proto'}
    SCHEMAS.append(rec);fids.append(add('data_models',f'{fq}.{name} = {num}',line.strip(),[s['id']],line.strip(),record=rec))
  seen_schema[key]=fids
 elif s['type']=='native_protobuf_descriptor':
  key=(s['sha256'],'native')
  if key in seen_schema:
   for fid in seen_schema[key]:F[int(fid.split('-')[1])-1]['source_references'].append(s['id']);s['findings'].append(fid)
   continue
  d=FileDescriptorProto.FromString((OUT/s['evidence_copy']).read_bytes());fids=[]
  full=MessageToDict(d,preserving_proto_field_name=True)
  dump(OUT/'registries/native-descriptors'/(s['sha256']+'.json'),full)
  def enums(es,parent):
   for en in es:
    fq='.'.join([parent,en.name]);rec={'kind':'enum','full_name':fq,'source_id':s['id'],'source_format':'native descriptor'};SCHEMAS.append(rec)
    for v in en.value:
     r={'kind':'enum_value','enum':fq,'name':v.name,'number':v.number,'source_id':s['id'],'source_format':'native descriptor'};SCHEMAS.append(r);fids.append(add('native_interfaces',fq+'.'+v.name+' = '+str(v.number),pretty(r),[s['id']],record=r))
  def messages(ms,parent):
   for msg in ms:
    fq='.'.join([parent,msg.name]);rec={'kind':'message','full_name':fq,'source_id':s['id'],'source_format':'native descriptor'};SCHEMAS.append(rec)
    fids.append(add('native_interfaces','Native message: '+fq,pretty(MessageToDict(msg,preserving_proto_field_name=True)),[s['id']],record=rec))
    for fld in msg.field:
     r={'kind':'field','message':fq,'name':fld.name,'number':fld.number,'type':fld.type_name or FieldDescriptorProto.Type.Name(fld.type),'label':FieldDescriptorProto.Label.Name(fld.label),'oneof':msg.oneof_decl[fld.oneof_index].name if fld.HasField('oneof_index') else None,'proto3_optional':fld.proto3_optional,'source_id':s['id'],'source_format':'native descriptor'};SCHEMAS.append(r)
     fids.append(add('native_interfaces',fq+'.'+fld.name+' = '+str(fld.number),pretty(r),[s['id']],record=r))
    enums(msg.enum_type,fq);messages(msg.nested_type,fq)
  messages(d.message_type,d.package);enums(d.enum_type,d.package)
  for sv in d.service:
   for m in sv.method:
    r={'service':d.package+'.'+sv.name,'method':m.name,'input_type':m.input_type,'output_type':m.output_type,'client_streaming':m.client_streaming,'server_streaming':m.server_streaming,'source_id':s['id']};SERVICES.append(r);fids.append(add('api_schema_services','Declared RPC '+r['service']+'/'+m.name,pretty(r),[s['id']],record=r,notes='RPC descriptor does not itself reveal deployed URL, authentication or runtime status.'))
  seen_schema[key]=fids

# Recover the authoritative frontend FileDescriptorProto blobs too. The older
# rendered .proto generator omits services/options, so reading renderings alone
# would silently lose information already present in the existing registry.
import base64
registry_source=LOC['extension/lib/descriptors.js']
registry_text=TEXT[registry_source['id']]
registry_match=re.search(r'export const DESCRIPTORS\s*=\s*(\{.*\})\s*;',registry_text,re.S)
FRONTEND_DESCRIPTOR_STATS={'files':0,'service_methods':0,'source_id':registry_source['id']}
if registry_match:
 for proto_name,b64 in json.loads(registry_match[1]).items():
  raw=base64.b64decode(b64+'='*((-len(b64))%4));fd=FileDescriptorProto.FromString(raw);full=MessageToDict(fd,preserving_proto_field_name=True)
  filehash=hashlib.sha256(raw).hexdigest();dest=OUT/'registries/frontend-descriptors'/(filehash+'.json');dump(dest,full)
  FRONTEND_DESCRIPTOR_STATS['files']+=1
  add('authoritative_frontend_descriptors','Full frontend descriptor: '+proto_name,pretty(full),[registry_source['id']],proto_name,
   verification='historical',notes='New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.',record={'kind':'file_descriptor','name':proto_name,'sha256':filehash,'decoded_json':str(dest.relative_to(OUT))})
  for sv in fd.service:
   for method in sv.method:
    r={'service':fd.package+'.'+sv.name,'method':method.name,'input_type':method.input_type,'output_type':method.output_type,'client_streaming':method.client_streaming,'server_streaming':method.server_streaming,'source_id':registry_source['id'],'source_format':'frontend FileDescriptorProto'}
    SERVICES.append(r);FRONTEND_DESCRIPTOR_STATS['service_methods']+=1
    add('api_schema_services','Frontend-declared RPC '+r['service']+'/'+method.name,pretty(r),[registry_source['id']],proto_name,verification='historical',record=r,notes='Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.')
dump(OUT/'registries/frontend-descriptor-recovery.json',FRONTEND_DESCRIPTOR_STATS)

# Batch3 — static route objects. Reconstruct path patterns from reversed Symfony tokens.
def balanced(st,start):
 depth=0;quote=None;esc=False
 for i in range(start,len(st)):
  ch=st[i]
  if quote:
   if esc:esc=False
   elif ch=='\\':esc=True
   elif ch==quote:quote=None
   continue
  if ch in "'\"`":quote=ch;continue
  if ch=='{':depth+=1
  elif ch=='}':
   depth-=1
   if depth==0:return st[start:i+1]
 return None
route_map={}
for s in S:
 if s['type'] not in ['source_code','saved_html']:continue
 st=TEXT.get(s['id'],'')
 for m in re.finditer(r'([A-Za-z_$][\w$]*):\{tokens:\[',st):
  obj=balanced(st,m.start()+len(m[1])+1)
  if not obj:continue
  key=(m[1],hashlib.sha256(obj.encode()).hexdigest())
  if key in route_map:
   r=route_map[key]
   if s['id'] not in r['source_ids']:r['source_ids'].append(s['id'])
   continue
  tokenpart=obj.split('defaults:',1)[0]
  chunks=[]
  # Token regexes themselves contain ] characters. Balance arrays while
  # respecting quoted strings instead of terminating at the first literal ].
  arrays=[];arraystack=[];quote=None;escaped=False
  for ai,ch in enumerate(tokenpart):
   if quote:
    if escaped:escaped=False
    elif ch=='\\':escaped=True
    elif ch==quote:quote=None
    continue
   if ch in "'\"`":quote=ch;continue
   if ch=='[':arraystack.append(ai)
   elif ch==']' and arraystack:
    begin=arraystack.pop();fragment=tokenpart[begin:ai+1]
    if re.match(r'\[\s*[`"\'](?:text|variable)[`"\']',fragment):arrays.append(fragment)
  for fragment in arrays:
   vals=re.findall(r'[`"\']([^`"\']*)[`"\']',fragment)
   if not vals:continue
   if vals[0]=='text' and len(vals)>1:chunks.append(vals[1])
   elif vals[0]=='variable' and len(vals)>3:chunks.append(vals[1]+'{'+vals[3]+'}')
  pattern=''.join(reversed(chunks)) or '[pattern not decoded]'
  methods=re.search(r'methods:\[([^\]]*)\]',obj);ms=re.findall(r'[`"\']([^`"\']+)[`"\']',methods[1]) if methods else []
  r={'id':f'RTE-{len(route_map)+1:04d}','route_name':m[1],'url_pattern':pattern,'http_methods':ms or ['not established; empty/missing route constraint'],
    'title':'not observed','purpose':'declared route '+m[1],'accessibility':'not established by route declaration','authentication':'not established','roles':'not established','forms':'not established',
    'response':'not observed','redirects':'not observed','source_ids':[s['id']],'character_offset':m.start(),'raw_route_declaration':obj,'discovery':'static generated route table; NOT a successful request'}
  route_map[key]=r
for r in route_map.values():
 fid=add('routes','Declared route '+r['route_name'],pretty(r),r['source_ids'],r['raw_route_declaration'][:100],verification='historical',record=r,
 notes='Reconstructed path is derived from stored tokens, not a newly visited or invented concrete URL. Preserve defaults/requirements in raw declaration.');r['finding_id']=fid;ROUTES.append(r)

# Batch4 — experiments and full native review outputs. Do not count plan-only entries as executions.
trialhash={}
for s in S:
 if s['type']!='json_artifact':continue
 try:j=json.loads(TEXT[s['id']])
 except:continue
 if not isinstance(j,dict):continue
 istrial=isinstance(j.get('config'),dict) and ('started'in j or 'actual'in j or 'error'in j)
 if istrial:
  key=s['sha256']
  if key in trialhash:
   fid=trialhash[key];F[int(fid.split('-')[1])-1]['source_references'].append(s['id']);s['findings'].append(fid);continue
  record={k:j[k] for k in ['config','started','actual','engines','numericHash','actualSettings','elapsedSeconds','speech','error','warnings','evaluateGame','networkAttempts'] if k in j}
  record['source_id']=s['id'];record['outcome']='complete numeric result' if 'actual'in j else ('error/timeout' if 'error'in j else 'search-only result')
  if 'resource-failed' in s['location']:record['outcome']='invalid resource-pressure attempt; not a numerical result'
  if 'preSearch'in j:record['completed_presearch_points']=len(j['preSearch']);record['presearch_progress_values']=[v.get('response',{}).get('progress') for v in j['preSearch']]
  if 'searchAudit'in j:record['searchAudit']=j['searchAudit']
  fid=add('experiments','Trial '+str(j['config'].get('id',s['location']))+' — '+record['outcome'],pretty(record),[s['id']],verification='historical',record=record);trialhash[key]=fid;record['finding_id']=fid;TRIALS.append(record)
 # Complete native reviews may be the JSON itself, a gameReview property, or CEAC envelope.
 candidates=[]
 if isinstance(j.get('gameReview'),dict):candidates.append(j['gameReview'])
 if 'review'in j and 'highlights'in j:candidates.append(j)
 for g in candidates:
  summary={k:g[k] for k in ['highlights','result','opening','metadata'] if k in g}
  add('native_review_outputs','Stored native review payload: '+s['location'],pretty(summary),[s['id']],verification='historical',notes='Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.')
  for i,m in enumerate(g.get('review',{}).get('playedMoves',[]),1):
   add('native_review_moves',f'Ply {i} in {s["location"]}',pretty(m),[s['id']],verification='historical',record={'ply':i,'move_record':m},notes='Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.')

# Machine-readable registries for later reports.
for name,data in [('schemas',SCHEMAS),('routes',ROUTES),('trials',TRIALS),('rpc-services',SERVICES),('document-blocks',DOCBLOCKS)]:dump(OUT/'registries'/(name+'.json'),data)
# Curated findings are added in a separate reviewed batch.
exec((META/'curated.py').read_text())

# Preserve actual historical probe status separately from mere URL literals.
for probe in PROBES:
 literal=probe['target_literal']
 if literal in UM:
  u=UM[literal];u.setdefault('historical_http_observations',[]).append(probe)
  u['directly_visited']='Historical GET probe recorded; see source and byte-range caveat.'
  u['verification_status']='Historical HTTP status '+str(probe['http_status'])+'; not re-fetched in this audit.'
# URL declarations are findings too; retain each occurrence and distinguish unvisited literal from endpoint.
for u in U:
 fid=add('url_references',u['url'],pretty({k:v for k,v in u.items() if k!='occurrences'}),u['source_ids'],
 verification='historical',notes='URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.',
 evidence=[{'source_id':x['source_id'],'character_offset':x['character_offset'],'excerpt':x['context']} for x in u['occurrences']],record={'url_id':u['id'],'url':u['url']})
 u['related_findings'].append(fid);F[-1]['url_references']=[u['url']]

# Link findings to exact URLs when they occur in the description/evidence (not every URL in a whole bundle).
for f in F:
 found=[];body=f['detailed_description']
 for m in re.finditer(r'(?:https?|wss?|git\+https)://[^\s"\'`<>]+',body):
  literal=m[0].rstrip('.,;')
  if literal in UM:
   found.append(literal)
   if f['id'] not in UM[literal]['related_findings']:UM[literal]['related_findings'].append(f['id'])
 f['url_references']=sorted(set(f['url_references']+found))
# Relations based on shared direct source, plus separately curated contradiction links.
for f in F:
 near=[]
 for sid in f['source_references'][:2]:near.extend(SM[sid]['findings'][:3])
 f['related_findings']=list(dict.fromkeys(x for x in near if x!=f['id']))[:5]
for s in S:
 s['findings']=list(dict.fromkeys(s['findings']));s['finding_count']=len(s['findings']);s['main_topics']=sorted(set(F[int(x.split('-')[1])-1]['category'] for x in s['findings']))
 s['finding_types']=dict(collections.Counter(F[int(x.split('-')[1])-1]['classification'] for x in s['findings']))
 s['incorporated']=True
 s['potential_missing_sections']=['Minified code beyond extracted declarations/call sites is not exhaustively semantically interpreted.'] if s['type']=='source_code' and s['bytes']>100000 else []
 if not s['findings']:s['accounting_note']='Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.'

# Render comprehensive outputs with per-finding mandatory fields and navigable shards.
exec((META/'render_audit.py').read_text())
