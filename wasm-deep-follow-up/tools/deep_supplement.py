#!/usr/bin/env python3
from pathlib import Path
import json,gzip,collections,re,hashlib,struct
B=Path('/var/tmp/wasm-deep');O=B/'output';inv=json.loads((O/'binary-inventory.json').read_text())
def dump(p,x):p.parent.mkdir(exist_ok=True,parents=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False))
def scrub(s):
 s=re.sub(r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b','[REDACTED_EMAIL]',s)
 s=re.sub(r'(?i)(bearer\s+)[a-z0-9_.-]{16,}',r'\1[REDACTED]',s)
 return s
mat=[];tags=[]
for b in inv:
 p=O/'deep-functions'/b['binary_id'];d=json.loads((p/'structure.json').read_text());raw=Path(b['path']).read_bytes();features=json.loads((p/'opcode-features.json').read_text());sec=[]
 for s in d['sections']:
  a=s['payload_offset'];z=s['end'];sec.append({'id':s['id'],'header_offset':s['header_offset'],'payload_offset':a,'bytes':z-a,'sha256':hashlib.sha256(raw[a:z]).hexdigest()})
 m={'binary_id':b['binary_id'],'sha256':b['sha256'],'bytes':b['bytes'],'format':'WebAssembly core module v1; not Component Model','defined_functions':len(d['functions']),'imported_functions':sum(x['kind']=='function' for x in d['imports']),'tables':d['tables'],'memories':d['memories'],'imported_memories':[x for x in d['imports'] if x['kind']=='memory'],'globals':d['globals'],'start_function_index':d.get('start_function_index'),'defined_tags':d.get('tags',[]),'imported_tags':[x for x in d['imports'] if x['kind']=='tag'],'custom_sections':d['custom_sections'],'declared_data_count':d.get('declared_data_count'),'data_segment_bytes':sum(x['bytes'] for x in d['data_segments']),'data_segments_count':len(d['data_segments']),'element_segments_count':len(d['elements']),'exported_names':[e['name'] for e in d['exports']],'actual_feature_instructions':features['observed_feature_instructions'],'section_payload_hashes':sec,'compiler_attribution':'No producer custom section is not proof of compiler absence. Emscripten conventions are inferred from exact glue/imports/export names; no Rust toolchain claim without evidence.'}
 mat.append(m)
 # Complete memory region map and raw evidence addressing,not invented C structs.
 regions=[]
 for s in d['data_segments']:
  expr=s.get('offset_expression',{}).get('ops',[]);addr=expr[0]['value'] if len(expr)==1 and expr[0]['op']=='i32.const' else None
  regions.append({**s,'initial_memory_start':addr,'initial_memory_end_exclusive':None if addr is None else addr+s['bytes'],'preview_hex':raw[s['binary_offset']:s['binary_offset']+min(48,s['bytes'])].hex(),'qualification':'Static initialization bytes,not proof of unchanged runtime memory or a named struct.'})
 dump(p/'memory-data-map.json',{'defined_memories':d['memories'],'imported_memories':m['imported_memories'],'globals':d['globals'],'active_and_passive_data_regions':regions,'growth_support_instruction_count':features['opcode_counts'].get('memory.grow',0),'unresolved':['Runtime allocation shapes and lifetime traces have not been measured.','Pointer-shaped constants are not named structs.','Large static data may contain model parameters,but size alone is not evidence of format or algorithm.']})
 # Explicit import statuses; imports are host boundaries,not invented native function bodies.
 dump(p/'import-function-statuses.json',[{**i,'function_id':b['binary_id']+'.function_'+str(i['function_index']).zfill(6),'analysis_status':'STRUCTURALLY ANALYZED','semantic_evidence':'Exact import module/name/type; host implementation not recovered from this function body.'} for i in d['imports'] if i['kind']=='function'])
 # Separate compact opcode mutation ledger,with function/callsite evidence.
 muts=[];members=collections.defaultdict(list)
 for x in json.loads((p/'initial-table.json').read_text()):members[x['function_index']].append({'table_index':x['table'],'slot':x['slot']})
 exports=collections.defaultdict(list)
 for e in d['exports']:
  if e['kind']=='function':exports[e['index']].append(e['name'])
 rows=[]
 with gzip.open(p/'functions-enriched.jsonl.gz','rt') as f:
  for l in f:
   r=json.loads(l);r['direct_export_names']=exports.get(r['index'],[]);r['initial_table_membership']=members.get(r['index'],[])
   if r['table_operations'] or r['opcodes'].get('ref.func') or r['opcodes'].get('call_ref'):muts.append({'function_id':r['function_id'],'index':r['index'],'table_operations':r['table_operations'],'ref_func_count':r['opcodes'].get('ref.func',0),'call_ref_count':r['opcodes'].get('call_ref',0)})
   rows.append(r)
 with gzip.open(p/'functions-enriched.jsonl.gz','wt',compresslevel=9) as f:
  for r in rows:f.write(json.dumps(r,allow_nan=False)+'\n')
 dump(p/'table-reference-mutation-ledger.json',{'native_mutating_or_reference_functions':muts,'exported_tables':[x for x in d['exports'] if x['kind']=='table'],'imported_tables':[x for x in d['imports'] if x['kind']=='table'],'qualification':'Absence of native table.set does not prove no JS Table.set/addFunction/imported-table writes. Initial-table candidates are conditional,not exact lifetime dispatch.'})
# Code/data equality grouping independent of module name.
section_groups={}
for sid,label in [(10,'code'),(11,'data'),(1,'type'),(7,'export')]:
 groups=collections.defaultdict(list)
 for x in mat:
  for s in x['section_payload_hashes']:
   if s['id']==sid:groups[s['sha256']].append(x['binary_id'])
 section_groups[label]=[{'sha256':k,'binary_ids':v} for k,v in groups.items() if len(v)>1]
dump(O/'module-comparison-matrix.json',mat);dump(O/'section-hash-equivalence.json',section_groups)
# Extract source maps' actual sourcesContent to independently traceable,privacy-scrubbed files.
maprows=[]
for item in json.loads((O/'additional-companion-retrieval.json').read_text()):
 if 'sources_content_present' not in item:continue
 sm=json.loads(Path(item['body_path']).read_text());version='2.38.2' if '2.38.2' in item['url'] else '2.49.3'
 for i,(name,content) in enumerate(zip(sm['sources'],sm.get('sourcesContent',[]))):
  if content is None:continue
  clean=scrub(content);path=O/'rive-recovered-sources'/version/(str(i).zfill(2)+'-'+re.sub('[^a-zA-Z0-9_.-]','_',name.split('/')[-1] or 'source')+'.txt');path.parent.mkdir(exist_ok=True,parents=True);path.write_text(clean)
  hits=[]
  for pat in ['setWasmUrl','fallback','rive_threads','locateFile','fetch(','fetch (','instantiate','WebAssembly','loadRuntime','worker','wasmBinaryFile']:
   starts=[m.start() for m in re.finditer(re.escape(pat),clean)]
   for a in starts[:30]:hits.append({'pattern':pat,'offset':a,'excerpt':clean[max(0,a-100):a+280]})
  maprows.append({'map_url':item['url'],'map_sha256':item['sha256'],'source_name':scrub(name),'source_index':i,'source_content_sha256':hashlib.sha256(content.encode()).hexdigest(),'scrubbed_content_sha256':hashlib.sha256(clean.encode()).hexdigest(),'output_path':str(path.relative_to(O)),'loader_evidence':hits})
dump(O/'rive-sourcemap-reconstruction.json',maprows)
# NNUE public companion signature,not an unproved decoder.
models=[]
for r in json.loads((O/'model-companion-retrieval.json').read_text()):
 if not r.get('body_path'):continue
 raw=Path(r['body_path']).read_bytes();m={k:r[k] for k in ['url','http_status','bytes','sha256','complete_payload_proven']};m['first_32_bytes_hex']=raw[:32].hex()
 if r['url'].endswith('.nnue') and len(raw)>=12:
  v,h,n=struct.unpack('<III',raw[:12]);m.update({'header_version_u32_le':v,'header_architecture_hash_u32_le':h,'description_length_u32_le':n,'description_bounded_ascii':scrub(raw[12:12+min(n,2048)].decode('ascii',errors='replace')),'qualification':'Header fields follow observed Stockfish NNUE layout convention. No claim that every engine build accepts this exact network. No arbitrary weights interpreted as code.'})
 models.append(m)
dump(O/'nnue-companion-signatures.json',models)
print('Supplemented',len(mat),'modules, recovered',len(maprows),'source-map source contents')
