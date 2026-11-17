#!/usr/bin/env python3
"""Instruction-level normal-control CFG for selected original CEE bodies,not the derivative."""
from pathlib import Path
import json,gzip,collections
O=Path('/var/tmp/wasm-deep/output');ns={};s=Path('/home/user/forensic-mission-tools/deep_analyze.py').read_text();exec(s[:s.index('\nimport os\nONLY=')],ns)
b=next(x for x in json.loads((O/'binary-inventory.json').read_text()) if x['binary_id']=='module-002');d,raw=ns['parse'](Path(b['path']));manifest=json.loads((O/'cee-connected-slice/slice-manifest.json').read_text());selected=manifest['selected_original_functions'];functions={x['index']:x for x in d['functions']};summ=[];output=O/'cee-connected-slice/selected-original-cfg.jsonl.gz'
with gzip.open(output,'wt',compresslevel=9) as out:
 for idx in selected:
  f=functions[idx];ins=list(ns['instructions'](raw,f['body_offset'],f['end_offset']));nodes=[];control=[];root={'kind':'function','entry':ins[0]['offset'],'end':ins[-1]['offset'],'after':'EXIT'};stack=[root];frames={};branch_context={};nxt={x['offset']:(ins[i+1]['offset'] if i+1<len(ins) else 'EXIT')for i,x in enumerate(ins)}
  for x in ins:
   op=x['opcode'];off=x['offset'];nodes.append({k:x[k]for k in ['offset','end','opcode','immediates']})
   if op in ['block','loop','if','try','try_table']:
    frame={'kind':op,'entry':off,'body_entry':nxt[off]};frames[off]=frame;stack.append(frame)
   elif op=='else':stack[-1]['else']=off;frames[off]=stack[-1]
   elif op=='end':
    fr=stack.pop();fr['end']=off;fr['after']=nxt[off]
   elif op in ['br','br_if','br_table']:branch_context[off]=stack[:]
  if stack:raise ValueError('Unbalanced structured control')
  def target(context,depth):
   fr=context[-1-depth];return fr['body_entry'] if fr['kind']=='loop' else fr['after']
  edges=[]
  for x in ins:
   off=x['offset'];op=x['opcode'];im=x['immediates'];targets=[]
   if op=='if':
    fr=frames[off];targets=[(nxt[off],'condition_true'),(nxt[fr['else']] if 'else'in fr else fr['after'],'condition_false')]
   elif op=='else':targets=[(frames[off]['after'],'skip_else_after_then')]
   elif op in ['br','br_if']:
    targets=[(target(branch_context[off],im['index']),'branch')]
    if op=='br_if':targets.append((nxt[off],'condition_false'))
   elif op=='br_table':
    targets=[(target(branch_context[off],depth),'case_'+str(i))for i,depth in enumerate(im['labels'])];targets.append((target(branch_context[off],im['default_label']),'default'))
   elif op in ['return','return_call','return_call_indirect','return_call_ref']:targets=[('EXIT',op)]
   elif op in ['unreachable','throw','rethrow']:targets=[]
   else:targets=[(nxt[off],'normal')]
   for t,kind in targets:edges.append({'from':off,'to':t,'kind':kind})
  known={x['offset']for x in ins}|{'EXIT'};assert all(e['to']in known for e in edges)
  r={'binary_id':'module-002','function_index':idx,'original_body_offset':f['body_offset'],'original_body_bytes':f['body_bytes'],'instruction_nodes':nodes,'normal_control_edges':edges,'scope':'Original binary normal-control CFG. No exception unwind edges,interprocedural call-return edges,path feasibility,stackSSA,or alias fixedpoint. Calls retain original immediates. Block end/loop branch targets resolved structurally.'};out.write(json.dumps(r)+'\n');summ.append({'function_index':idx,'instruction_nodes':len(nodes),'normal_control_edges':len(edges),'branch_count':sum(x['opcode']in['br','br_if','br_table','if']for x in ins)})
(O/'cee-connected-slice/cfg-summary.json').write_text(json.dumps({'functions':summ,'functions_count':len(summ),'instruction_nodes':sum(x['instruction_nodes']for x in summ),'normal_edges':sum(x['normal_control_edges']for x in summ),'qualification':'Bounded selected-function normal-control graph only;not full semantic understanding.'},indent=2));print(len(summ),'functions',sum(x['instruction_nodes']for x in summ),'instruction nodes')
