#!/usr/bin/env python3
"""Bounded offline WASM structure/disassembly recovery. Originals read-only."""
from pathlib import Path
import sys,json,re,hashlib,subprocess,time,collections,gzip,shutil,bisect,os
BASE=Path('/var/tmp/chess-forensic');IN=BASE/'input';OUT=BASE/'output/website-audit/wasm-analysis';TOOLS=BASE/'tools/node_modules/wabt/bin';OUT.mkdir(parents=True,exist_ok=True)
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False))
def scrub(t):
 t=re.sub(r'\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{8,}\b','[REDACTED_JWT]',t)
 t=re.sub(r'(?i)([?&](?:token|key|secret|password|session|access_token)=)[^\s&"<>]+',r'\1[REDACTED]',t)
 t=re.sub(r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b','[REDACTED_EMAIL]',t)
 return t
class Reader:
 def __init__(self,b,p=0):self.b=b;self.p=p
 def byte(self):v=self.b[self.p];self.p+=1;return v
 def u(self):
  v=0;s=0
  while True:
   b=self.byte();v|=(b&127)<<s
   if not b&128:return v
   s+=7
 def signed(self):
  v=0;s=0
  while True:
   b=self.byte();v|=(b&127)<<s;s+=7
   if not b&128:break
  return v-(1<<s) if b&64 else v
 def take(self,n):s=self.b[self.p:self.p+n];self.p+=n;return s
 def string(self):return self.take(self.u()).decode('utf8',errors='replace')
 def vec(self,fn):return [fn() for _ in range(self.u())]
VT={0x7f:'i32',0x7e:'i64',0x7d:'f32',0x7c:'f64',0x7b:'v128',0x70:'funcref',0x6f:'externref'}
def vt(r):
 b=r.byte();return VT.get(b,hex(b))
def limits(r):
 flags=r.u();d={'flags':flags,'minimum':r.u(),'shared':bool(flags&2),'memory64':bool(flags&4)}
 if flags&1:d['maximum']=r.u()
 return d
def expr(r):
 start=r.p;ops=[]
 while True:
  op=r.byte()
  if op==0x0b:break
  if op in [0x41,0x42]:ops.append({'op':'i32.const' if op==0x41 else 'i64.const','value':r.signed()})
  elif op in [0x23,0xd2]:ops.append({'op':'global.get' if op==0x23 else 'ref.func','index':r.u()})
  elif op==0xd0:ops.append({'op':'ref.null','type':vt(r)})
  elif op in [0x43,0x44]:ops.append({'op':'f32.const' if op==0x43 else 'f64.const','raw':r.take(4 if op==0x43 else 8).hex()})
  else:raise ValueError('unhandled initializer '+hex(op)+' at '+str(r.p-1))
 return {'ops':ops,'file_offset':start,'byte_length':r.p-start}
def parse(path):
 b=path.read_bytes();r=Reader(b,8);d={'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'magic':b[:4].hex(),'version':int.from_bytes(b[4:8],'little'),'sections':[],'types':[],'imports':[],'exports':[],'functions':[],'tables':[],'memories':[],'globals':[],'elements':[],'data_segments':[],'custom_sections':[]};fntypes=[];importf=[]
 while r.p<len(b):
  start=r.p;sid=r.byte();size=r.u();payload=r.p;end=payload+size;rr=Reader(b,payload)
  sec={'id':sid,'header_offset':start,'payload_offset':payload,'payload_bytes':size,'end':end};d['sections'].append(sec)
  if sid==0:
   name=rr.string();d['custom_sections'].append({'name':name,'offset':payload,'size':size,'metadata_preview':scrub(b[rr.p:min(end,rr.p+4000)].decode('utf8',errors='replace'))})
  elif sid==1:
   for i in range(rr.u()):
    form=rr.byte()
    if form!=0x60:raise ValueError('Non-function type '+hex(form))
    d['types'].append({'index':i,'parameters':rr.vec(lambda:vt(rr)),'results':rr.vec(lambda:vt(rr))})
  elif sid==2:
   for _ in range(rr.u()):
    it={'module':rr.string(),'name':rr.string()};kind=rr.byte();it['kind']={0:'function',1:'table',2:'memory',3:'global',4:'tag'}.get(kind,kind)
    if kind==0:it['type_index']=rr.u();it['function_index']=len(importf);importf.append(it)
    elif kind==1:it['element_type']=vt(rr);it['limits']=limits(rr)
    elif kind==2:it['limits']=limits(rr)
    elif kind==3:it['value_type']=vt(rr);it['mutable']=bool(rr.byte())
    elif kind==4:it['attribute']=rr.byte();it['type_index']=rr.u()
    d['imports'].append(it)
  elif sid==3:fntypes=rr.vec(rr.u)
  elif sid==4:
   for _ in range(rr.u()):d['tables'].append({'element_type':vt(rr),'limits':limits(rr)})
  elif sid==5:d['memories']=rr.vec(lambda:limits(rr))
  elif sid==6:
   for i in range(rr.u()):d['globals'].append({'index':i,'value_type':vt(rr),'mutable':bool(rr.byte()),'initializer':expr(rr)})
  elif sid==7:
   for _ in range(rr.u()):d['exports'].append({'name':rr.string(),'kind':{0:'function',1:'table',2:'memory',3:'global',4:'tag'}.get((k:=rr.byte()),k),'index':rr.u()})
  elif sid==8:d['start_function_index']=rr.u()
  elif sid==9:
   for ei in range(rr.u()):
    flags=rr.u();e={'index':ei,'flags':flags}
    if flags in [0,2,4,6]:
     e['mode']='active';e['table_index']=rr.u() if flags in [2,6] else 0;e['offset_expression']=expr(rr)
    else:e['mode']='declarative' if flags&2 else 'passive'
    if flags&4:
     if flags!=4:e['element_type']=vt(rr)
     e['initializers']=rr.vec(lambda:expr(rr))
    else:
     if flags!=0:e['element_kind']=rr.byte()
     e['function_indices']=rr.vec(rr.u)
    d['elements'].append(e)
  elif sid==10:
   count=rr.u()
   for i in range(count):
    n=rr.u();body=rr.p;rr.p+=n;d['functions'].append({'index':len(importf)+i,'type_index':fntypes[i],'body_offset':body,'body_bytes':n,'end_offset':body+n})
  elif sid==11:
   for i in range(rr.u()):
    flags=rr.u();seg={'index':i,'flags':flags,'mode':'passive' if flags==1 else 'active'}
    if flags!=1:seg['memory_index']=rr.u() if flags==2 else 0;seg['offset_expression']=expr(rr)
    n=rr.u();seg['binary_offset']=rr.p;seg['bytes']=n;seg['sha256']=hashlib.sha256(b[rr.p:rr.p+n]).hexdigest();rr.p+=n
    d['data_segments'].append(seg)
  elif sid==12:d['declared_data_count']=rr.u()
  elif sid==13:
   d['tags']=[]
   for ti in range(rr.u()):d['tags'].append({'defined_tag_index':ti,'attribute':rr.byte(),'type_index':rr.u()})
  if sid and sid not in [0] and rr.p!=end:sec['parser_bytes_consumed']=rr.p-payload;sec['parser_remainder']=end-rr.p
  r.p=end
 sig={t['index']:{'parameters':t['parameters'],'results':t['results']} for t in d['types']}
 for x in importf:x['signature']=sig[x['type_index']]
 funcs={f['index']:f for f in d['functions']}
 for f in d['functions']:f['signature']=sig[f['type_index']]
 for e in d['exports']:
  if e['kind']=='function':
   fn=funcs.get(e['index'],next((i for i in importf if i['function_index']==e['index']),{}));e['signature']=fn.get('signature');e['type_index']=fn.get('type_index')
 return d,b

def run(args,out,seconds=180):
 start=time.monotonic()
 try:
  with out.open('w') as f, out.with_suffix(out.suffix+'.stderr').open('w') as e:
   proc=subprocess.run(['timeout',str(seconds),'node','--max-old-space-size=2048',str(TOOLS/args[0]),*map(str,args[1:])],stdout=f,stderr=e,timeout=seconds+5)
  return {'command':['wabt1.0.39',*map(str,args)],'exit_code':proc.returncode,'seconds':round(time.monotonic()-start,3),'stdout_file':out.name,'stderr_file':out.with_suffix(out.suffix+'.stderr').name}
 except subprocess.TimeoutExpired:return {'command':args[0],'exit_code':'outer timeout','seconds':round(time.monotonic()-start,3)}
MODULES=[]
for path in sorted((IN/'extension/engines').rglob('*.wasm')):
 mid=f'module-{len(MODULES)+1:03d}';od=OUT/'modules'/mid;od.mkdir(parents=True,exist_ok=True)
 print('BEGIN',mid,path,flush=True);d,b=parse(path);d['module_id']=mid;d['original_location']=str(path.relative_to(IN));shutil.copyfile(path,od/'module.wasm')
 # Preserve exact loader text; all files here are public engines, no player fixtures.
 loader=path.with_suffix('.js')
 if loader.exists():shutil.copyfile(loader,od/'loader.js');d['loader_original_location']=str(loader.relative_to(IN))
 commands=[]
 commands.append(run(['wasm-validate','--enable-all',path],od/'validation.txt',90))
 commands.append(run(['wasm-objdump','-h',path],od/'section-summary.txt',60))
 # Full WAT translation, then gzip; function-level analyses stream this exact output.
 wat=BASE/(mid+'.wat');commands.append(run(['wasm2wat','--enable-all',path],wat,180))
 opcounts=collections.Counter();callpairs=collections.Counter();indirect=collections.Counter();funcops={};selected={};export_indices={e['index'] for e in d['exports'] if e['kind']=='function'}
 wanted_names=['CEE_Init','CEE_InitWithOpts','CEE_NewGame','CEE_Run','CEE_NewFeature','CEE_DisposeFeature','CEE_GetMetadata','CEE_GetProtoSchemas','malloc','free','uci_command','init']
 wanted={e['index'] for e in d['exports'] if e['kind']=='function' and (e['name'] in wanted_names or len(export_indices)<25)}
 current=None;buf=[];counts=collections.Counter();currentcalls=collections.Counter();max_capture=50000
 with wat.open(errors='replace') as f, gzip.open(od/'module.wat.gz','wt',compresslevel=7) as gz:
  for line in f:
   gz.write(line)
   mm=re.match(r'  \(func \(;(\d+);\)',line)
   if mm:
    if current is not None:
     funcops[current]={'opcodes':dict(counts),'direct_callees':dict(currentcalls),'indirect_call_sites':indirect[current]}
     if current in wanted:selected[current]=''.join(buf)
    current=int(mm[1]);counts=collections.Counter();currentcalls=collections.Counter();buf=[]
   elif line.startswith('  ('):
    if current is not None:
     funcops[current]={'opcodes':dict(counts),'direct_callees':dict(currentcalls),'indirect_call_sites':indirect[current]}
     if current in wanted:selected[current]=''.join(buf)
    current=None
   if current is not None:
    if current in wanted and sum(map(len,buf))<max_capture:buf.append(line)
    op=re.match(r'\s+([a-z][a-z0-9_.]+)(?:\s|$)',line)
    if op:
     mnemonic=op[1];counts[mnemonic]+=1;opcounts[mnemonic]+=1
     if mnemonic in ['call','return_call']:
      cm=re.match(r'\s+\w+\s+(\d+)',line)
      if cm:target=int(cm[1]);callpairs[(current,target)]+=1;currentcalls[target]+=1
     elif mnemonic in ['call_indirect','return_call_indirect']:indirect[current]+=1
 for f in d['functions']:f.update(funcops.get(f['index'],{}));f['export_names']=[e['name'] for e in d['exports'] if e['kind']=='function' and e['index']==f['index']]
 with gzip.open(od/'call-graph.jsonl.gz','wt') as g:
  for (a,c),n in sorted(callpairs.items()):g.write(json.dumps({'caller':a,'callee':c,'static_call_sites':n})+'\n')
 dump(od/'opcode-statistics.json',dict(opcounts));d['direct_call_pairs']=len(callpairs);d['direct_call_sites']=sum(callpairs.values());d['indirect_call_sites']=sum(indirect.values());d['wat_bytes']=wat.stat().st_size
 (od/'selected-functions.wat').write_text(';; EXACT selected function forms from module.wat.gz.\n;; This is an excerpt, NOT a complete executable module. Function names below are export names, not inferred internals.\n'+''.join(';; Exports: '+', '.join(e['name'] for e in d['exports'] if e['kind']=='function' and e['index']==idx)+'\n'+v for idx,v in selected.items()))
 # Full decompilation is attempted with a strict bound; captured nonzero outcomes remain explicit.
 dec=od/'decompilation.txt';commands.append(run(['wasm-decompile','--enable-all',path],dec,120))
 if commands[-1]['exit_code']==0:
  with dec.open('rb') as f,gzip.open(od/'decompilation.txt.gz','wb',compresslevel=7) as z:shutil.copyfileobj(f,z)
  dec.unlink()
 # Offset-linked all-ASCII candidates plus meaningful subset, not claims of human-readable semantics for random code.
 relevant=re.compile(r'CEE_|Torch|Stockfish|NNUE|Maia|[Hh]uman|pvtrees|search_mode|Emscripten|emscripten|LLVM|clang|protobuf|accuracy|rating|classification|EvaluateGame|RunSearch|assert|malloc|cannot|error|\.proto|\.cpp|\.cc\b|https?://|normalize|Normalize|Hash',re.I)
 strings=[];allcount=0
 data_ranges=d['data_segments'];starts=[x['binary_offset'] for x in data_ranges]
 with gzip.open(od/'all-ascii-strings.jsonl.gz','wt') as g:
  for m in re.finditer(rb'[\x20-\x7e]{6,}',b):
   val=scrub(m[0].decode());off=m.start();si=bisect.bisect_right(starts,off)-1;seg=data_ranges[si] if si>=0 else None
   rec={'file_offset':off,'bytes':len(m[0]),'text':val,'location':'data' if seg and off<seg['binary_offset']+seg['bytes'] else 'other/code'}
   if rec['location']=='data':
    rec['data_segment']=seg['index'];ops=seg.get('offset_expression',{}).get('ops',[])
    if len(ops)==1 and ops[0]['op']=='i32.const':rec['memory_address']=ops[0]['value']+off-seg['binary_offset']
   g.write(json.dumps(rec,ensure_ascii=False)+'\n');allcount+=1
   if relevant.search(val):strings.append(rec)
 utf16=[]
 for endian,pat,enc in [('LE',rb'(?:[\x20-\x7e]\x00){6,}','utf-16-le'),('BE',rb'(?:\x00[\x20-\x7e]){6,}','utf-16-be')]:
  for m in re.finditer(pat,b):utf16.append({'file_offset':m.start(),'encoding':endian,'text':scrub(m[0].decode(enc))})
 dump(od/'utf16-candidates.json',utf16)
 with gzip.open(od/'relevant-strings.jsonl.gz','wt') as z:
  for rec in strings:z.write(json.dumps(rec,ensure_ascii=False)+'\n')
 (od/'strings.txt').write_text('# Offset-linked relevant ASCII strings (hex file offset); all candidates and UTF16 candidates are separate.\n'+'\n'.join(f'0x{x["file_offset"]:08x} '+x['text'] for x in strings))
 d['ascii_candidates']=allcount;d['relevant_string_candidates']=len(strings);d['utf16_candidates']=len(utf16);d['tool_commands']=commands
 dump(od/'structure.json',d);dump(od/'imports-exports.json',{'types':d['types'],'imports':d['imports'],'exports':d['exports'],'tables':d['tables'],'memories':d['memories'],'globals':d['globals']});dump(od/'functions.json',d['functions']);dump(od/'data-segments.json',d['data_segments'])
 MODULES.append({k:v for k,v in d.items() if k not in ['functions','types','imports','exports','elements','data_segments','globals']})
 dump(OUT/'module-manifest.json',MODULES);wat.unlink(missing_ok=True)
 print('DONE',mid,'functions',len(d['functions']),'imports',len(d['imports']),'exports',len(d['exports']),'watgz',(od/'module.wat.gz').stat().st_size,'decomp',commands[-1]['exit_code'],flush=True)
print('ALL DONE',len(MODULES),flush=True)
