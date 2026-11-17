#!/usr/bin/env python3
"""Validate, package, and preserve source assets without leaving oversized workspace."""
from pathlib import Path
import re,json,hashlib,zipfile,gzip,collections,shutil,subprocess
B=Path('/var/tmp/chess-forensic');O=B/'output/website-audit';M=O/'audit-metadata';ROOT=Path('/home/user')
def load(p):return json.loads(p.read_text())
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False))
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
# File-size exclusions are exact and reproducible; all five original binaries stay.
exclusions=[]
for p in sorted((O/'wasm-analysis/modules').glob('*/*')):
 exclude=(p.name=='module.wat.gz' and p.parent.name in ['module-001','module-002','module-005']) or p.name=='decompilation.txt.gz'
 if exclude:
  exclusions.append({'path':str(p.relative_to(O)),'bytes':p.stat().st_size,'sha256':sha(p),'reason':'Large escaped text duplicates code/data/weights; omitted from downloadable archive to preserve workspace headroom. Exact original binary and generation command,all function/call inventories,selected WAT and available code-only/focused pseudocode included.','reproduction':'wasm2wat --enable-all module.wasm -o module.wat; or wasm-decompile --enable-all module.wasm; tool-specific failures recorded.'})
dump(M/'packaging-exclusions.json',exclusions);excluded={x['path'] for x in exclusions}
# Retain original ancillary inactive-asset bytes not already represented by module copies.
assetmap=[];archive=ROOT/'workspace-archives/inactive-engine-assets-lzma.zip'
if not archive.exists():raise SystemExit('Run this packaging stage before relocating original workspace archives.')
with zipfile.ZipFile(archive) as z:
 for i in z.infolist():
  if i.is_dir():continue
  binary=Path(i.filename).name
  if binary.endswith('.wasm'):
   matches=[p for p in (O/'wasm-analysis/modules').glob('*/structure.json') if load(p)['original_location']==i.filename]
   dest=matches[0].parent/'module.wasm' if matches else None
  elif binary.endswith('.js'):
   matches=[p for p in (O/'wasm-analysis/modules').glob('*/structure.json') if load(p).get('loader_original_location')==i.filename]
   dest=matches[0].parent/'loader.js' if matches else None
  else:dest=None
  if dest is None:
   dest=O/'preserved-workspace'/i.filename;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(i))
  digest=hashlib.sha256(z.read(i)).hexdigest()
  assert sha(dest)==digest
  assetmap.append({'original_path':i.filename,'archive_path':str(dest.relative_to(O)),'bytes':i.file_size,'sha256':digest})
for name in ['explanation-engine.js','explanation-engine.wasm']:
 p=O/'wasm-analysis/modules/module-002'/('loader.js' if name.endswith('.js') else 'module.wasm')
 assetmap.append({'original_path':'extension/engines/cee/'+name,'archive_path':str(p.relative_to(O)),'bytes':p.stat().st_size,'sha256':sha(p)})
dump(M/'workspace-asset-restore-map.json',assetmap)
(O/'PACKAGING_AND_STORAGE.md').write_text('''# Packaging and storage

[Master index](chapters/00_MASTER_INDEX.md)

The primary ZIP contains every report, all prior recovery evidence, all five available original WASM binaries, their loaders, full structural/function/call inventories, offset-linked strings, small full WAT translations, selected CEE/Torch WAT excerpts, successful Stockfish decompilations, code-only Torch pseudocode, and focused CEE export pseudocode.

## Exact exclusions

[packaging-exclusions.json](audit-metadata/packaging-exclusions.json) lists each large omitted intermediate, its measured bytes and SHA-256. Full CEE WAT is about 1.6 GB uncompressed per variant. Those full text translations and the Torch text data/weight duplication do not fit the persistent workspace with useful headroom. They can be regenerated from the included exact binaries using the recorded tools. Exclusion is not a claim that these artifacts were never generated. Failed full decompilation outputs are not represented as recovered source.

No available WASM binary is excluded. Further referenced versions and multipart assets were not downloaded; their limitations are separately recorded in wasm-url-references.json. These are retrieval gaps, not packaging exclusions.

## Original material and privacy

Original documentation was not edited. The package contains separately labelled redacted copies and original-byte hashes. Existing unredacted research/source archives remain in the user's workspace and are not silently included in a new download that promises privacy redaction. The prior audit's full redacted evidence corpus is preserved under history/prior-audit.

The unused Stockfish NNUE and opening-book files are retained under preserved-workspace; other inactive assets are represented by the identical original bytes in module directories. The restore map records exact paths and hashes. This is lossless content consolidation, not a patch to a binary. Existing release ZIPs remain unchanged outside this audit ZIP.

To keep the total workspace within its limit, the final verified ZIP replaces redundant expanded/archived audit copies and becomes the storage location for the active CEE loader/binary as well. The extension's source code remains unchanged, but engine execution requires `python3 restore-workspace.py active-cee`. Restoring the engine consumes about 32 MiB; move a large archive off-workspace first if necessary. Research restoration remains available separately.
''')
# Copy the actual latest scripts after last edits, then improve only generated narrative text.
for p in (ROOT/'forensic-mission-tools').glob('*'):
 if p.is_file():shutil.copyfile(p,O/'tools'/p.name)
subprocess.run(['python3',str(ROOT/'forensic-mission-tools/review_prose.py')],check=True)
# Avoid a broken link to QC/index files during link validation; final data replaces pending text.
dump(M/'qa-report.json',{'status':'PENDING final checks'})
(M/'ALL_FILES.md').write_text('# Complete file index\n\nIndex finalized after validation.\n')
S=load(M/'source-manifest.json');SM={s['id']:s for s in S};F=[json.loads(l) for l in (M/'findings-ledger.jsonl').read_text().splitlines()];FM={f['id']:f for f in F};U=[json.loads(l) for l in (M/'urls.jsonl').read_text().splitlines()]
errors=[];checks={}
checks['source_ids_unique']=len(S)==len(SM);checks['finding_ids_unique']=len(F)==len(FM);checks['url_ids_unique']=len(U)==len(set(x['id'] for x in U));checks['url_literals_unique']=len(U)==len(set(x['url'] for x in U))
for k,v in checks.items():
 if not v:errors.append(k)
for f in F:
 if any(s not in SM for s in f['source_references']):errors.append(f['id']+' dangling source')
 if any(x not in FM for x in f['related_findings']):errors.append(f['id']+' dangling related finding')
for u in U:
 if any(s not in SM for s in u['source_ids']):errors.append(u['id']+' dangling source')
 if any(f not in FM for f in u['related_findings']):errors.append(u['id']+' dangling finding')
checks['findings_validated']=len(F);checks['source_records_validated']=len(S);checks['url_records_validated']=len(U)
# Original sources may now live in verified prior cleanup archives. Resolve using scratch restoration.
originals=load(O/'history/prior-audit/audit-metadata/original-snapshot.json');missing=[];changed=[]
for r in originals:
 candidates=[ROOT/r['path'],B/'input'/r['path']];p=next((p for p in candidates if p.is_file()),None)
 if p is None:missing.append(r['path'])
 elif p.stat().st_size!=r['size'] or sha(p)!=r['sha256']:changed.append(r['path'])
checks['original_snapshot_sources_checked']=len(originals);checks['original_snapshot_sources_unresolved']=missing;checks['original_snapshot_resolved_hash_mismatches']=changed
if changed:errors.append('Original input byte mismatch')
# Missing raw originals are not automatically a failure if redacted historical evidence persists;
# they must remain explicit,never claimed all original raw bytes independently checked.
mods=[]
for p in sorted((O/'wasm-analysis/modules').glob('*/structure.json')):
 d=load(p);binary=p.parent/'module.wasm';assert sha(binary)==d['sha256'];assert binary.stat().st_size==d['bytes']
 if any(s.get('parser_remainder') for s in d['sections']):errors.append(d['module_id']+' parser remainder')
 if len(d['functions'])!=len(set(f['index'] for f in d['functions'])):errors.append(d['module_id']+' duplicate function index')
 if d['tool_commands'][0]['exit_code']!=0:errors.append(d['module_id']+' validation failure')
 mods.append({'module_id':d['module_id'],'sha256':sha(binary),'functions':len(d['functions']),'export_entries':len(d['exports']),'validation_exit':d['tool_commands'][0]['exit_code'],'runtime_stub_instantiation_exit':load(p.parent/'runtime-observation.json').get('returncode')})
checks['original_WASM_hashes_and_structure']=mods
# Validate JSON/JSONL and gzip contents without treating full source code as JSON.
validjson=0;validlines=0;validgzip=0
for p in O.rglob('*'):
 rel=str(p.relative_to(O))
 if not p.is_file() or rel in excluded:continue
 if p.suffix=='.json':
  try:load(p);validjson+=1
  except Exception as e:errors.append('InvalidJSON '+rel+' '+str(e))
 elif p.suffix=='.jsonl':
  try:
   for line in p.open():
    if line.strip():json.loads(line);validlines+=1
  except Exception as e:errors.append('InvalidJSONL '+rel+' '+str(e))
 elif p.suffix=='.gz':
  try:
   with gzip.open(p,'rb') as f:
    for b in iter(lambda:f.read(1024*1024),b''):pass
   validgzip+=1
  except Exception as e:errors.append('InvalidGZIP '+rel+' '+str(e))
checks.update({'JSON_files_validated':validjson,'JSONL_lines_validated':validlines,'gzip_files_validated':validgzip})
# Links outside code/evidence fences. Original documentary blocks may contain historical external links.
linkerrors=[];links=0
for p in O.rglob('*.md'):
 if 'evidence' in p.relative_to(O).parts or 'original-documentation' in p.relative_to(O).parts:continue
 text=re.sub(r'```[^\n]*\n.*?```','',p.read_text(),flags=re.S)
 for m in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)',text):
  dest=m[1]
  if re.match(r'^[a-zA-Z][\w+.-]*:',dest) or dest.startswith('#'):continue
  target=(p.parent/dest.split('#')[0]).resolve();links+=1
  if not target.exists() or (target.is_relative_to(O) and str(target.relative_to(O)) in excluded):linkerrors.append({'file':str(p.relative_to(O)),'destination':dest})
checks['internal_links_checked']=links;checks['broken_internal_links']=linkerrors
if linkerrors:errors.append('Broken internal Markdown links')
# Targeted literal checks. Exact originals/binary data and tool regex source are not prose secrets.
patterns={'JWT_literal':r'\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{8,}\b','credential_assignment':r'(?i)(?:api[_-]?key|access[_-]?token|password|csrf[_-]?token|sitekey)["\'`]?\s*[:=]\s*["\'`][A-Za-z0-9_\-/.+=]{12,}["\'`]','fixture_handles':r'(?i)DotingProspect|Adam-it|Justin-Reid-BOT|Khaleel91|kingBeetlejuice1','opaque_API_LOG':r'API_LOG: [A-Za-z0-9+/=]{80,}'}
hits=[];textfiles=0
for p in O.rglob('*'):
 rel=p.relative_to(O)
 if not p.is_file() or str(rel) in excluded or p.suffix in ['.py','.cjs','.wasm','.bin','.gz','.nnue'] or p.name=='qa-report.json':continue
 # Public opening book has no player data; still harmless to scan.
 t=p.read_text(errors='replace');textfiles+=1
 for name,pat in patterns.items():
  n=len(re.findall(pat,t))
  if n:hits.append({'file':str(rel),'pattern':name,'count':n})
checks['redaction_text_files_scanned']=textfiles;checks['redaction_pattern_hits']=hits
if hits:errors.append('Sensitive/fixture literal candidates remain')
empty=[str(p.relative_to(O)) for p in O.rglob('*.md') if not p.read_text().strip()];checks['empty_Markdown_documents']=empty
if empty:errors.append('Empty documentation')
# Zero-length failed stdout and empty stderr are real outcomes,not empty reports.
checks['empty_tool_outputs_note']='Zero-length tool stdout/stderr retained only as command outcomes; module reports and exit statuses explain failures.'
report={'status':'PASS within declared checks' if not errors else 'FAIL','overall_audit_status':'PARTIALLY AUDITED','checks':checks,'errors':errors,'limitations':['No exhaustive semantic review of every function/component.','Additional referenced WASM versions remain un-retrieved.','Public engineering disclosures establish reported technology usage,not endpoint-specific schemas.','Binary/opaque-data redaction is not guaranteed; known text patterns checked.','Historical original raw paths may be archived; verification resolves restored copies and reports any unresolved files.','A valid call graph records direct static calls; indirect targets remain unresolved.']};dump(M/'qa-report.json',report)
if errors:
 print(json.dumps({'errors':errors,'link_errors':linkerrors[:20],'redaction_hits':hits,'original_missing':missing,'original_changed':changed},indent=2));raise SystemExit(1)
# Comprehensive index and distributed-file hashes exclude deliberately omitted intermediates.
files=[p for p in O.rglob('*') if p.is_file() and str(p.relative_to(O)) not in excluded and '__pycache__' not in p.parts]
(M/'ALL_FILES.md').write_text('# Complete packaged file index\n\n[Master index](../chapters/00_MASTER_INDEX.md)\n\n'+''.join('- ['+str(p.relative_to(O))+'](../'+str(p.relative_to(O))+')\n' for p in sorted(files) if p.name!='ALL_FILES.md')+'\nLarge reproducible omitted intermediates are listed in packaging-exclusions.json.\n')
(M/'checksums.sha256').write_text(''.join(sha(p)+'  '+str(p.relative_to(O))+'\n' for p in sorted(files) if p.name!='checksums.sha256'))
zipdest=B/'website-complete-forensic-audit.zip'
with zipfile.ZipFile(zipdest,'w',zipfile.ZIP_DEFLATED,compresslevel=8) as z:
 for p in sorted(O.rglob('*')):
  if p.is_file() and str(p.relative_to(O)) not in excluded and '__pycache__' not in p.parts:
   z.write(p,'website-audit/'+str(p.relative_to(O)),compress_type=zipfile.ZIP_STORED if p.suffix=='.gz' else zipfile.ZIP_DEFLATED)
with zipfile.ZipFile(zipdest) as z:
 assert z.testzip() is None
 for x in assetmap:assert hashlib.sha256(z.read('website-audit/'+x['archive_path'])).hexdigest()==x['sha256']
 assert len([n for n in z.namelist() if n.endswith('/module.wasm')])==5
 count=len(z.namelist())
print(json.dumps({'QC':'PASS within declared checks','zip_path':str(zipdest),'zip_bytes':zipdest.stat().st_size,'zip_MiB':round(zipdest.stat().st_size/1048576,2),'zip_sha256':sha(zipdest),'zip_members':count,'omitted_intermediate_files':len(exclusions),'omitted_intermediate_bytes':sum(x['bytes'] for x in exclusions),'original_sources_resolved':len(originals)-len(missing),'unresolved_original_paths':missing,'internal_links_checked':links},indent=2))
