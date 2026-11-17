#!/usr/bin/env python3
"""Decompile selected complete CEE export bodies using signature-correct stubs.
This is an ANALYSIS DERIVATIVE, never an original executable reconstruction.
"""
from pathlib import Path
import json,re,subprocess,gzip,shutil
B=Path('/var/tmp/chess-forensic');W=B/'output/website-audit/wasm-analysis';T=B/'tools/native/usr/bin'
for md in sorted((W/'modules').glob('module-*')):
 d=json.loads((md/'structure.json').read_text());original=Path(d['original_location']).name;native=B/'native-decompile'/(original+'.txt');exitfile=native.with_suffix(native.suffix.replace('.txt','.exit'))
 # Preserve successful native full decompilation for the small Stockfish modules.
 ef=B/'native-decompile'/(original+'.exit');er=B/'native-decompile'/(original+'.stderr')
 if ef.exists():
  (md/'native-decompilation-status.json').write_text(json.dumps({'tool':'native WABT1.0.36','exit_code':int(ef.read_text()),'limit':'CPU60s,wall75s,addressspace2GiB','stderr':er.read_text() if er.exists() else ''},indent=2))
  if ef.read_text().strip()=='0' and native.exists():
   with native.open('rb') as f,gzip.open(md/'decompilation.native.txt.gz','wb',compresslevel=7) as z:shutil.copyfileobj(f,z)
 if 'explanation-engine' not in original:continue
 focused=md/'focused-decompilation';focused.mkdir(exist_ok=True);parts=(md/'selected-functions.wat').read_text().split(';; Exports: ')[1:]
 # All function indices remain stable through one signature-correct stub per original function.
 funcs={i['function_index']:i for i in d['imports'] if i['kind']=='function'};funcs.update({i['index']:i for i in d['functions']})
 header=['(module\n']
 for t in d['types']:header.append(f' (type (func '+(' (param '+ ' '.join(t['parameters'])+')' if t['parameters'] else '')+(' (result '+' '.join(t['results'])+')' if t['results'] else '')+'))\n')
 for idx,f in sorted(funcs.items()):header.append(f' (import "analysis_stub" "original_fn_{idx}" (func (type {f["type_index"]})))\n')
 for table in d['tables']:
  l=table['limits'];header.append(f' (table {l["minimum"]} '+(str(l['maximum'])+' ' if 'maximum' in l else '')+table['element_type']+')\n')
 for mem in d['memories']:header.append(f' (memory {mem["minimum"]} {mem.get("maximum",mem["minimum"])})\n')
 for gl in d['globals']:
  typ=gl['value_type'];v=gl['initializer']['ops'][0]['value'];header.append(' (global '+('(mut '+typ+')' if gl['mutable'] else typ)+f' ({typ}.const {v}))\n')
 header=''.join(header);results=[]
 for part in parts:
  name,body=part.split('\n',1);name=name.strip()
  if name not in ['CEE_Init','CEE_InitWithOpts','CEE_NewFeature','CEE_Run','CEE_DisposeFeature']:continue
  body=re.sub(r'\(func \(;\d+;\)', '(func $analyzed',body,count=1)
  wat=focused/(name+'.analysis-stubs.wat');wasm=focused/(name+'.analysis-stubs.wasm');wat.write_text(';; ANALYSIS DERIVATIVE: other functions are imports; original memory data omitted. Not for execution.\n'+header+body+' (export "'+name+'" (func $analyzed))\n)')
  cp=subprocess.run([str(T/'wat2wasm'),'--enable-all',str(wat),'-o',str(wasm)],capture_output=True,text=True,timeout=30)
  rec={'export':name,'compile_exit':cp.returncode,'stderr':cp.stderr,'scope':'Exact export function body from original WAT, but all callees are typed imports and data segments are absent; address constants remain numeric. Generated analysis-only module must not be mistaken for recovered source.'}
  if cp.returncode==0:
   dec=focused/(name+'.pseudocode.txt');p=subprocess.run([str(T/'wasm-decompile'),'--enable-all',str(wasm),'-o',str(dec)],capture_output=True,text=True,timeout=30);rec.update({'decompile_exit':p.returncode,'decompile_stderr':p.stderr})
   # Stub signatures vastly inflate output; preserve only actual analyzed function pseudocode.
   if p.returncode==0:
    txt=dec.read_text();start=txt.find('export function '+name);rec['selection_found']=start>=0
    if start>=0:dec.write_text('// Decompiled analysis derivative: typed stub imports replace ALL other functions.\n'+txt[start:])
  results.append(rec)
  # The synthetic .wasm contains no new evidence; .wat reproduces it and avoids confusing original-module counts.
  wasm.unlink(missing_ok=True)
 (focused/'results.json').write_text(json.dumps(results,indent=2))
 print(md.name,[(x['export'],x.get('decompile_exit')) for x in results],flush=True)
