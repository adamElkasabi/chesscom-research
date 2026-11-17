#!/usr/bin/env python3
"""Connected selected-function slice. Analysis derivative, NEVER original or runnable reconstruction."""
from pathlib import Path
import json,re,subprocess,hashlib
B=Path('/var/tmp/wasm-deep');O=B/'output';T=Path('/var/tmp/chess-forensic/tools/native/usr/bin');ns={};code=Path('/home/user/forensic-mission-tools/deep_analyze.py').read_text();exec(code[:code.index('\nimport os\nONLY=')],ns);instructions=ns['instructions']
def u(n):
 b=bytearray()
 while n>127:b.append((n&127)|128);n>>=7
 b.append(n);return bytes(b)
def string(s):b=s.encode();return u(len(b))+b
def section(i,payload):return bytes([i])+u(len(payload))+payload
def dump(p,v):p.write_text(json.dumps(v,indent=2))
D=O/'deep-functions/module-002';d=json.loads((D/'structure.json').read_text());binary=next(x for x in json.loads((O/'binary-inventory.json').read_text()) if x['binary_id']=='module-002');raw=Path(binary['path']).read_bytes();F={f['index']:f for f in d['functions']};I={i['function_index']:i for i in d['imports'] if i['kind']=='function'};N=len(F)+len(I)
selected=[1679,1687,1688,1689,1690,1741,1954,1961,1965,1984,22947,22950,165,1664,1665,1666,1667,1670,1671,1686,1694,1695,1696,1697,1698,1699,1731,1888,1889,1892,1901,1906,1907,1909,1911,1943,1950,1970,4396,18367,18368,18370,18380,18527,18550,18562]
selected=sorted(set(x for x in selected if x in F));remap={idx:N+k for k,idx in enumerate(selected)}
parts={s['id']:raw[s['payload_offset']:s['end']] for s in d['sections'] if s['id']!=0};dest=O/'cee-connected-slice';dest.mkdir(exist_ok=True)
imports=u(N)
for idx in range(N):
 f=I.get(idx) or F[idx];imports+=string('boundary')+string('original_fn_'+str(idx))+b'\x00'+u(f['type_index'])
exports=[];codes=[];links=[];boundaries=set()
for idx in selected:
 f=F[idx];patch=[];cursor=f['body_offset'];chunks=[]
 for ins in instructions(raw,f['body_offset'],f['end_offset']):
  if ins['opcode'] in ['call','return_call','ref.func']:
   old=ins['immediates']['index']
   if old in remap:
    chunks.append(raw[cursor:ins['offset']]);chunks.append(raw[ins['offset']:ins['offset']+1]+u(remap[old]));cursor=ins['end'];links.append({'caller_original':idx,'callee_original':old,'rewritten_callee_index':remap[old],'original_instruction_offset':ins['offset']})
   else:boundaries.add(old)
 chunks.append(raw[cursor:f['end_offset']]);body=b''.join(chunks);codes.append(u(len(body))+body);exports.append(string('original_fn_'+str(idx))+b'\x00'+u(remap[idx]))
output=b'\0asm\x01\0\0\0'+section(1,parts[1])+section(2,imports)+section(3,u(len(selected))+b''.join(u(F[x]['type_index']) for x in selected))
for sid in [4,5,6]:
 if sid in parts:output+=section(sid,parts[sid])
output+=section(7,u(len(exports))+b''.join(exports))
# Keep exact original table image, but imported boundary entries remain external. This is deliberate and documented.
if 9 in parts:output+=section(9,parts[9])
# Empty passive data placeholders preserve indices needed by bulk-memory validation; never execute this derivative.
ndata=len(d['data_segments'])
if 12 in parts:output+=section(12,u(ndata))
output+=section(10,u(len(codes))+b''.join(codes))
if ndata:output+=section(11,u(ndata)+b'\x01\x00'*ndata)
wasm=dest/'connected-analysis-derivative.wasm';wasm.write_bytes(output)
results=[]
for tool,args in [('wasm-validate',[]),('wasm2wat',['-o',str(dest/'connected-analysis-derivative.wat')]),('wasm-decompile',['-o',str(dest/'connected-pseudocode.txt')])]:
 p=subprocess.run(['timeout','40',str(T/tool),'--enable-all',str(wasm),*args],capture_output=True,text=True);results.append({'tool':'native WABT1.0.36 '+tool,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
# Remove thousands of typed boundary declarations from the readable view; original complete tool output stays separate.
p=dest/'connected-pseudocode.txt'
if p.exists():
 text=p.read_text();m=re.search(r'(?:export )?function original_fn_',text)
 if m:(dest/'selected-implementations.txt').write_text('// ANALYSIS DERIVATIVE. Selected direct calls connect real original bodies; nonselected/host-dispatched functions remain external. Original data replaced by empty placeholders. NEVER EXECUTE.\n'+text[m.start():])
dump(dest/'slice-manifest.json',{'original_binary_sha256':binary['sha256'],'selected_original_functions':selected,'original_to_slice_function_index':remap,'rewritten_selected_direct_calls':links,'unselected_boundary_function_indices':sorted(boundaries),'tool_results':results,'limitations':['Exact selected bodies except function-index remapping.','Selected direct callees are real bodies,unlike the earlier single-export/all-stub derivatives.','Host-mediated indirect dispatch still crosses typed boundaries; table entries retain original indices.','Original data content omitted and passive placeholders inserted. Numeric address constants refer to original data map,not derivative memory contents.','Not original source. Not an executable reproduction. Never runtime-tested or safe to run as a functional engine.']})
print('SELECTED',len(selected),'connected callsites',len(links),'tool results',[(x['tool'],x['exit_code']) for x in results])
