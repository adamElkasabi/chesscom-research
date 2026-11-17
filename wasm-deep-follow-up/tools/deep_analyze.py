#!/usr/bin/env python3
"""Instruction-boundary checked function enrichment. No target code execution."""
from pathlib import Path
import json,re,collections,hashlib,struct,bisect,gzip,subprocess,time
B=Path('/var/tmp/wasm-deep');P=B/'input/website-audit';O=B/'output';D=O/'deep-functions';D.mkdir(exist_ok=True)
# Reuse audited section parser,not its execution loop.
code=Path('/home/user/forensic-mission-tools/wasm_analyze.py').read_text();ns={};exec(code[:code.index('\nMODULES=[]')],ns)
parse=ns['parse'];Reader=ns['Reader'];vt=ns['vt']
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False))
OPS={}
for line in (B/'tools/opcode.def').read_text().splitlines():
 m=re.match(r'WABT_OPCODE\(([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*(0x[0-9a-fA-F]+|0),\s*(0x[0-9a-fA-F]+|0),\s*\w+,\s*"([^"]+)"',line)
 if m:
  result,a,b,c,mem,pref,num,name=m.groups();OPS[(int(pref,0),int(num,0))]={'name':name,'parameters':[x.strip() for x in [a,b,c] if x.strip()!='___'],'result':result.strip()}

def instructions(raw,begin,end):
 r=Reader(raw,begin);locals=[]
 for _ in range(r.u()):locals.append({'count':r.u(),'type':vt(r)})
 first=r.p
 while r.p<end:
  off=r.p;op=r.byte();pref=0;sub=op;imm={}
  if op in [0xfc,0xfd,0xfe,0xfb]:pref=op;sub=r.u()
  meta=OPS.get((pref,sub))
  if not meta:raise ValueError(f'unsupported opcode {pref:x}:{sub:x} offset{off:x}')
  if not pref:
   if op in [2,3,4,6]:imm['block_type']=r.signed()
   elif op in [7,8,9,0x0c,0x0d,0x10,0x12,0x14,0x15,0x18,0x20,0x21,0x22,0x23,0x24,0x25,0x26,0x3f,0x40,0xd2,0xd5,0xd6]:imm['index']=r.u()
   elif op==0x0e:imm['labels']=r.vec(r.u);imm['default_label']=r.u()
   elif op in [0x11,0x13]:imm['type_index']=r.u();imm['table_index']=r.u()
   elif op==0x1c:imm['value_types']=r.vec(lambda:vt(r))
   elif 0x28<=op<=0x3e:imm['alignment']=r.u();imm['offset']=r.u()
   elif op in [0x41,0x42]:imm['value']=r.signed()
   elif op==0x43:imm['value']=struct.unpack('<f',r.take(4))[0]
   elif op==0x44:imm['value']=struct.unpack('<d',r.take(8))[0]
   elif op==0xd0:imm['heap_type']=r.signed()
   elif op==0x1f:
    imm['block_type']=r.signed();clauses=[]
    for _ in range(r.u()):
     k=r.byte();c={'kind':k}
     if k in [0,1]:c['tag_index']=r.u()
     c['label_index']=r.u();clauses.append(c)
    imm['catches']=clauses
  elif pref==0xfc:
   if sub in [8,10,12,14]:imm['index1']=r.u();imm['index2']=r.u()
   elif sub in [9,11,13,15,16,17]:imm['index']=r.u()
  elif pref==0xfd:
   if sub<=11 or 84<=sub<=93:imm['alignment']=r.u();imm['offset']=r.u()
   if sub in [12,13]:imm['bytes']=r.take(16).hex()
   elif 21<=sub<=34 or 84<=sub<=91:imm['lane']=r.byte()
  elif pref==0xfe:
   if sub==3:imm['reserved']=r.byte()
   else:imm['alignment']=r.u();imm['offset']=r.u()
  elif pref==0xfb:raise ValueError('GC immediate decoding not implemented; not silently consumed')
  if r.p>end:raise ValueError('Instruction extends beyond function body')
  yield {'offset':off,'end':r.p,'opcode':meta['name'],'immediates':imm,'prefix':pref,'subopcode':sub,'meta':meta,'locals':locals if off==first else None}
 if r.p!=end:raise ValueError('Function boundary mismatch')

def sigkey(s):return ','.join(s['parameters'])+'->'+','.join(s['results'])
def scc(graph,nodes):
 seen=set();order=[]
 for root in nodes:
  if root in seen:continue
  seen.add(root);st=[(root,iter(graph.get(root,[])))]
  while st:
   node,it=st[-1]
   try:
    q=next(it)
    if q not in seen:seen.add(q);st.append((q,iter(graph.get(q,[]))))
   except StopIteration:order.append(node);st.pop()
 rev=collections.defaultdict(list)
 for a,bs in graph.items():
  for b in bs:rev[b].append(a)
 seen=set();components=[]
 for root in reversed(order):
  if root in seen:continue
  seen.add(root);st=[root];group=[]
  while st:
   a=st.pop();group.append(a)
   for b in rev.get(a,[]):
    if b not in seen:seen.add(b);st.append(b)
  components.append(group)
 return components
import os
ONLY=set(filter(None,os.environ.get('WASM_ONLY','').split(',')))
SUMMARY=[x for x in json.loads((O/'analysis-summary.json').read_text()) if x['binary_id'] not in ONLY] if ONLY and (O/'analysis-summary.json').exists() else []
for binary in json.loads((O/'binary-inventory.json').read_text()):
 if ONLY and binary['binary_id'] not in ONLY:continue
 mid=binary['binary_id'];out=D/mid;out.mkdir(exist_ok=True);start=time.monotonic();print('BEGIN',mid,binary['bytes'],flush=True)
 try:d,raw=parse(Path(binary['path']))
 except Exception as ex:
  dump(out/'analysis-error.json',{'error':repr(ex),'binary':binary});SUMMARY.append({'binary_id':mid,'error':repr(ex)});continue
 dump(out/'structure.json',d)
 validation=subprocess.run(['node','--max-old-space-size=128',*(['--experimental-wasm-relaxed-simd'] if mid=='new-binary-030' else []),'-e',"const fs=require('fs');const valid=WebAssembly.validate(fs.readFileSync(process.argv[1]));console.log(JSON.stringify({valid}));process.exit(valid?0:2)",binary['path']],capture_output=True,text=True,timeout=35)
 dump(out/'validation.json',{'tool':'V8 WebAssembly.validate under Node20.20.2; no instantiation or target execution','v8_flags':['--experimental-wasm-relaxed-simd'] if mid=='new-binary-030' else [],'exit_code':validation.returncode,'stdout':validation.stdout,'stderr':validation.stderr,'note':'A native WABT validation attempt was killed(-9) on baseline CEE during the initial batch. V8 is an independent bounded structural validator,not a recovered engine function test.'})
 imports={i['function_index']:i for i in d['imports'] if i['kind']=='function'};functions={f['index']:f for f in d['functions']};sigs={i:f['signature'] for i,f in functions.items()};sigs.update({i:f['signature'] for i,f in imports.items()});type_sigs={t['index']:{'parameters':t['parameters'],'results':t['results']} for t in d['types']}
 exports=collections.defaultdict(list)
 for e in d['exports']:
  if e['kind']=='function':exports[e['index']].append(e['name'])
 # Exact initial table image,not a claim about runtime mutation.
 table={};elementunknown=0
 for e in d['elements']:
  ops=e.get('offset_expression',{}).get('ops',[])
  if e.get('mode')=='active' and len(ops)==1 and ops[0]['op']=='i32.const':
   idxs=e.get('function_indices')
   if idxs is None:idxs=[x['ops'][0]['index'] if len(x.get('ops',[]))==1 and x['ops'][0]['op']=='ref.func' else None for x in e.get('initializers',[])]
   for j,idx in enumerate(idxs):
    if idx is not None:table[(e.get('table_index',0),ops[0]['value']+j)]=idx
  else:elementunknown+=1
 pools=collections.defaultdict(set)
 for (ti,slot),fi in table.items():pools[(ti,sigkey(sigs[fi]))].add(fi)
 poolids={key:f'pool-{i:04d}' for i,key in enumerate(pools,1)}
 dump(out/'indirect-candidate-pools.json',[{'id':poolids[k],'table_index':k[0],'signature':k[1],'initial_candidate_function_indices':sorted(v),'status':'Initial table type-compatible candidates only; host/exported table or native writes can change targets.'} for k,v in pools.items()])
 dump(out/'initial-table.json',[{'table':ti,'slot':slot,'function_index':fi} for (ti,slot),fi in sorted(table.items())])
 # Offset-linked relevant strings/static regions; no arbitrary binary text promoted to semantics.
 ranges=[];stringmap={};interesting=re.compile(r'accuracy|rating|classif|brilliant|review|feature|human|pvtrees|normalize|centipawn|torch_search|n_async|engine_pool|exception|invalid|metadata|protobuf|InitWith|malloc|free|alloc|\.cc\b|\.cpp\b|NNUE|Stockfish|Rive|Skia|shader',re.I)
 for seg in d['data_segments']:
  ops=seg.get('offset_expression',{}).get('ops',[])
  if len(ops)!=1 or ops[0]['op']!='i32.const':continue
  addr=ops[0]['value'];bo=seg['binary_offset'];sz=seg['bytes'];ranges.append((addr,addr+sz,bo))
  for m in re.finditer(rb'[\x20-\x7e]{6,2048}',raw[bo:bo+sz]):
   text=m[0].decode()
   if interesting.search(text):
    text=re.sub(r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b','[REDACTED_EMAIL]',text);stringmap[addr+m.start()]={'memory_address':addr+m.start(),'file_offset':bo+m.start(),'text':text}
 ranges.sort();rstarts=[x[0] for x in ranges]
 def initial_u32(addr):
  i=bisect.bisect_right(rstarts,addr)-1
  if i>=0:
   lo,hi,off=ranges[i]
   if lo<=addr and addr+4<=hi:return int.from_bytes(raw[off+addr-lo:off+addr-lo+4],'little')
  return None
 dump(out/'relevant-data-strings.json',list(stringmap.values()))
 graph=collections.defaultdict(set);callers=collections.defaultdict(set);aug=collections.defaultdict(set);rows=[];sites=[];memsites=[];stringrefs=[];status=collections.Counter();opcodes=collections.Counter();features=collections.Counter();errors=[]
 edgefile=gzip.open(out/'direct-call-sites.jsonl.gz','wt')
 for f in d['functions']:
  fi=f['index'];cnt=collections.Counter();constants=collections.Counter();globalsused=collections.Counter();memb=collections.Counter();tables=collections.Counter();callees=collections.Counter();indirect=[];refs=[];stack=[];localsval={};patterns=[];localdecl=[];instructioncount=0
  def popn(n):
   if not n:return []
   if len(stack)<n:v=[None]*(n-len(stack))+stack[:];stack.clear();return v
   v=stack[-n:];del stack[-n:];return v
  def dispatch(kind,ins,signature,tableidx,indexvalue,importname=None):
   key=(tableidx,sigkey(signature));target=table.get((tableidx,indexvalue[0])) if indexvalue and isinstance(indexvalue[0],int) else None
   if target is not None and sigkey(sigs[target])!=key[1]:target=None
   rec={'caller':fi,'instruction_offset':ins['offset'],'kind':kind,'type_signature':key[1],'table_index':tableidx,'candidate_pool':poolids.get(key),'candidate_count':len(pools.get(key,[])),'abstract_slot':indexvalue[0] if indexvalue else None,'slot_basis':indexvalue[1] if indexvalue else 'unknown data flow','initial_table_candidate':target,'import_wrapper':importname,'status':'INITIAL_SLOT_CANDIDATE' if target is not None else 'TYPE_FILTERED_INITIAL_CANDIDATES' if key in pools else 'UNRESOLVED'};sites.append(rec);indirect.append(rec)
   if target is not None:aug[fi].add(target)
  try:
   for ins in instructions(raw,f['body_offset'],f['end_offset']):
    instructioncount+=1;name=ins['opcode'];imm=ins['immediates'];cnt[name]+=1;opcodes[name]+=1
    if ins.get('locals') is not None:localdecl=ins['locals']
    if len(patterns)<20:patterns.append((name,imm))
    if ins['prefix']==0xfd:features['SIMD_instructions']+=1
    if ins['prefix']==0xfd and ins['subopcode']>=0x100:features['relaxed_SIMD_instructions']+=1
    if ins['prefix']==0xfe:features['atomics_instructions']+=1
    if ins['prefix']==0xfc and ins['subopcode']>=8:features['bulk_memory_or_table_instructions']+=1
    if name.startswith(('ref.','table.')):features['reference_or_table_instructions']+=1
    if name in ['return_call','return_call_indirect','return_call_ref']:features['tail_call_instructions']+=1
    if name in ['try','catch','throw','rethrow','delegate','try_table','catch_all']:features['native_exception_instructions']+=1
    if name in ['i32.const','i64.const']:
     value=imm['value'];constants[value]+=1;stack.append((value,'literal'))
     if value in stringmap:refs.append(value);stringrefs.append({'function':fi,'instruction_offset':ins['offset'],**stringmap[value]})
    elif name in ['f32.const','f64.const']:stack.append((imm['value'],'literal float'))
    elif name=='local.get':stack.append(localsval.get(imm['index']))
    elif name in ['local.set','local.tee']:
     v=popn(1)[0];localsval[imm['index']]=v
     if name=='local.tee':stack.append(v)
    elif name.startswith('global.'):
     globalsused[str(imm['index'])+':'+name]+=1
     if name=='global.get':stack.append(None)
     else:popn(1)
    elif name in ['call','return_call']:
     target=imm['index'];sig=sigs[target];args=popn(len(sig['parameters']));graph[fi].add(target);aug[fi].add(target);callers[target].add(fi);callees[target]+=1
     edgefile.write(json.dumps({'caller':fi,'callee':target,'offset':ins['offset']})+'\n')
     imp=imports.get(target)
     if imp and imp['name'].startswith('invoke_') and sig['parameters'] and sig['parameters'][0]=='i32':dispatch('HOST_INVOKE_DISPATCH',ins,{'parameters':sig['parameters'][1:],'results':sig['results']},0,args[0],imp['name'])
     for _ in sig['results']:stack.append(None)
    elif name in ['call_indirect','return_call_indirect']:
     slot=popn(1)[0];sig=type_sigs[imm['type_index']];popn(len(sig['parameters']));dispatch('WASM_CALL_INDIRECT',ins,sig,imm['table_index'],slot)
     for _ in sig['results']:stack.append(None)
    elif name in ['call_ref','return_call_ref']:
     sites.append({'caller':fi,'instruction_offset':ins['offset'],'kind':name,'type_index':imm['index'],'status':'UNRESOLVED_REFERENCE_CALL'});stack.clear()
    elif 'load' in name and ('offset' in imm):
     memb[name]+=1;addr=popn(1)[0];value=None
     if name=='i32.load' and addr and isinstance(addr[0],int):
      v=initial_u32((addr[0]+imm['offset'])&0xffffffff)
      if v is not None:value=(v,'initial-memory read; runtime mutation not excluded')
     stack.append(value)
    elif ('store' in name or 'atomic' in name) and 'offset' in imm:memb[name]+=1;stack.clear();localsval.clear()
    elif name.startswith('memory.'):
     memb[name]+=1;stack.clear();localsval.clear()
    elif name.startswith('table.'):
     tables[name]+=1;stack.clear();localsval.clear()
    elif name in ['i32.add','i32.sub','i32.mul','i32.and','i32.or','i32.xor','i32.shl','i32.shr_u']:
     a,b=popn(2);v=None
     if a and b and isinstance(a[0],int) and isinstance(b[0],int):
      aa,bb=a[0],b[0]
      x={'i32.add':lambda:aa+bb,'i32.sub':lambda:aa-bb,'i32.mul':lambda:aa*bb,'i32.and':lambda:aa&bb,'i32.or':lambda:aa|bb,'i32.xor':lambda:aa^bb,'i32.shl':lambda:aa<<(bb&31),'i32.shr_u':lambda:(aa&0xffffffff)>>(bb&31)}[name]()&0xffffffff;v=(x,'straight-line constant expression' if a[1]=='literal' and b[1]=='literal' else 'abstract initial-state expression')
     stack.append(v)
    elif name=='drop':popn(1)
    elif name in ['block','loop','if','else','end','br','br_if','br_table','return','unreachable','try','catch','catch_all','throw','rethrow','delegate','try_table','ref.func','ref.null']:
     stack.clear();localsval.clear()
    else:
     meta=ins['meta'];popn(len(meta['parameters']))
     if meta['result']!='___':stack.append(None)
   complete=True
  except Exception as ex:complete=False;errors.append({'function':fi,'error':repr(ex)})
  state='STRUCTURALLY ANALYZED' if complete else 'UNANALYZED';semantic='No function-level semantic claim beyond decoded structure.'
  if complete and instructioncount==1 and patterns[0][0]=='end':state='UNDERSTOOD';semantic='Exact empty function body; no instructions with side effects.'
  elif complete and instructioncount==2 and patterns[0][0] in ['i32.const','i64.const','f32.const','f64.const'] and patterns[1][0]=='end':state='UNDERSTOOD';semantic='Exact constant-return body: '+str(patterns[0][1].get('value'))+'. No higher-level meaning inferred.'
  elif complete and instructioncount<=20 and patterns and len(callees)==1 and all(n in ['local.get','call','return_call','end','return'] for n,im in patterns):state='PARTIALLY UNDERSTOOD';semantic='Argument-forwarding wrapper around one callee; callee effects not reconstructed by this pattern.'
  status[state]+=1
  rows.append({'function_id':mid+'.function_'+str(fi).zfill(6),'index':fi,'original_symbol_names':exports.get(fi,[]),'inferred_name':None,'type_index':f['type_index'],'signature':f['signature'],'locals':localdecl,'instruction_count':instructioncount,'decode_complete':complete,'body_offset':f['body_offset'],'body_bytes':f['body_bytes'],'direct_callees':dict(callees),'direct_callers':[],'indirect_sites':len(indirect),'globals':dict(globalsused),'memory_operations':dict(memb),'table_operations':dict(tables),'i32_i64_constants':dict(constants),'relevant_string_addresses':sorted(set(refs)),'opcodes':dict(cnt),'analysis_status':state,'semantic_evidence':semantic})
 edgefile.close()
 for f in rows:f['direct_callers']=sorted(callers.get(f['index'],[]))
 with gzip.open(out/'functions-enriched.jsonl.gz','wt',compresslevel=7) as z:
  for f in rows:z.write(json.dumps(f,allow_nan=False)+'\n')
 with gzip.open(out/'indirect-dispatch-sites.jsonl.gz','wt') as z:
  for x in sites:z.write(json.dumps(x)+'\n')
 dump(out/'string-crossreferences.json',stringrefs);dump(out/'opcode-features.json',{'opcode_counts':dict(opcodes),'observed_feature_instructions':dict(features),'feature_note':'SIMD/atomics/etc counts indicate actual decoded instruction usage. Memory64/shared memory are separately structural flags. Unsupported GC decoding is explicitly reported,not counted absent.'});dump(out/'decode-errors.json',errors)
 allnodes=list(sigs);components=scc(graph,allnodes);dump(out/'direct-strongly-connected-components.json',{'scope':'Direct-call graph only; host/indirect dispatch can add recursion.','components':sorted(components,key=len,reverse=True)})
 reach=[]
 for export in d['exports']:
  if export['kind']!='function':continue
  def reachable(g):
   seen={export['index']};todo=[export['index']]
   while todo:
    a=todo.pop()
    for q in g.get(a,[]):
     if q not in seen:seen.add(q);todo.append(q)
   return seen
  direct=reachable(graph);initial=reachable(aug);reach.append({'export':export['name'],'function_index':export['index'],'direct_reachable_count':len(direct),'initial_dispatch_augmented_reachable_count':len(initial),'new_initial_candidates':sorted(initial-direct),'status':'Augmented reachability includes initial-table candidates; not a sound complete dynamic call graph.'})
 dump(out/'export-reachability.json',reach)
 dispatchcounts=collections.Counter(x['kind']+':'+x['status'] for x in sites)
 summary={'binary_id':mid,'sha256':binary['sha256'],'bytes':binary['bytes'],'defined_functions':len(rows),'complete_function_decodes':sum(x['decode_complete'] for x in rows),'instruction_count':sum(x['instruction_count'] for x in rows),'function_statuses':dict(status),'dispatch':dict(dispatchcounts),'relevant_string_references':len(stringrefs),'direct_SCC_count':len(components),'largest_direct_SCC':max(map(len,components),default=0),'validation_exit':validation.returncode,'unparsed_section_remainders':[x for x in d['sections'] if x.get('parser_remainder')],'elapsed_seconds':round(time.monotonic()-start,3)}
 dump(out/'summary.json',summary);SUMMARY.append(summary);dump(O/'analysis-summary.json',SUMMARY);print('DONE',mid,len(rows),'errors',len(errors),summary['elapsed_seconds'],flush=True)
print('ALL DONE',len(SUMMARY),flush=True)
