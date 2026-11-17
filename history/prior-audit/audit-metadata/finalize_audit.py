#!/usr/bin/env python3
"""Offline validation and packaging. No original file writes or website access."""
from pathlib import Path
import json,re,hashlib,collections,zipfile,urllib.parse
ROOT=Path('/home/user');P=ROOT/'website-audit';M=P/'audit-metadata'
def load(p):return json.loads(p.read_text())
def dump(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False))
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
 return h.hexdigest()
S=load(M/'source-manifest.json');SM={s['id']:s for s in S}
F=[json.loads(l) for l in (M/'findings-ledger.jsonl').read_text().splitlines()];FM={f['id']:f for f in F}
U=[json.loads(l) for l in (M/'urls.jsonl').read_text().splitlines()];UM={u['id']:u for u in U}
errors=[];checks={};warnings=[]
for name,items in [('source',S),('finding',F),('url',U)]:
 ids=[x['id'] for x in items];checks[name+'_ids_unique']=len(ids)==len(set(ids))
 if not checks[name+'_ids_unique']:errors.append('Duplicate '+name+' IDs')
for f in F:
 if any(sid not in SM for sid in f['source_references']):errors.append(f['id']+' dangling source')
 if any(fid not in FM for fid in f['related_findings']):errors.append(f['id']+' dangling related finding')
 if not f['source_references']:errors.append(f['id']+' missing source')
 if any(x not in f for x in ['category','title','detailed_description','classification','evidence','url_references','confidence','verification_status','additional_notes']):errors.append(f['id']+' missing fields')
 for e in f['evidence']:
  if e['source_id'] not in SM:errors.append(f['id']+' dangling evidence')
for s in S:
 if any(fid not in FM for fid in s['findings']):errors.append(s['id']+' dangling finding')
 if s.get('evidence_copy') and not (P/s['evidence_copy']).exists():errors.append(s['id']+' missing evidence copy')
for u in U:
 if any(sid not in SM for sid in u['source_ids']):errors.append(u['id']+' dangling source')
 if any(fid not in FM for fid in u['related_findings']):errors.append(u['id']+' dangling finding')
checks['source_finding_url_referential_integrity']=not errors
originals=load(M/'original-snapshot.json');changed=[];missing=[]
for r in originals:
 f=ROOT/r['path']
 if not f.is_file():missing.append(r['path'])
 elif f.stat().st_size!=r['size'] or sha(f)!=r['sha256']:changed.append(r['path'])
checks['original_files_checked']=len(originals);checks['original_files_missing']=missing;checks['original_files_modified']=changed
if changed or missing:errors.append('Original preservation failed')
# ZIP member checksums prove archive occurrences are individually content-accounted.
archive_checks=[]
for r in originals:
 f=ROOT/r['path']
 if f.suffix=='.zip':
  members=0;fail=[]
  with zipfile.ZipFile(f) as z:
   for i in z.infolist():
    if i.is_dir():continue
    members+=1;loc=r['path']+'!/'+i.filename
    matched=[s for s in S if s['location']==loc]
    digest=hashlib.sha256(z.read(i)).hexdigest()
    if not any(s['sha256']==digest for s in matched):fail.append(loc)
  archive_checks.append({'archive':r['path'],'members_verified':members,'failures':fail})
  if fail:errors.append('Archive member accounting failed: '+r['path'])
checks['archive_member_checks']=archive_checks
# Explicitly compare document bodies with the ledger. Headings are indexed separately.
doc_checks=[]
for s in S:
 if s['type']!='original_markdown':continue
 body=(P/s['evidence_copy']).read_text();inside=False;nonheading=[]
 for line in body.splitlines():
  if line.startswith('#') and not inside:continue
  if line.startswith('```'):inside=not inside
  if line.strip():nonheading.append(line)
 preserved='\n'.join(FM[fid]['detailed_description'] for fid in s['findings'] if FM[fid]['category']=='historical_documentation')
 missing_lines=[line for line in nonheading if line not in preserved]
 doc_checks.append({'source_id':s['id'],'body_nonempty_lines_checked':len(nonheading),'missing_body_lines':len(missing_lines)})
 if missing_lines:errors.append(s['id']+' documentation body omitted')
checks['original_markdown_body_coverage']=doc_checks
# Internal Markdown links in prose only; original code and exact evidence are not generated navigation.
link_errors=[];links=0
for f in P.rglob('*.md'):
 if 'evidence' in f.relative_to(P).parts:continue
 t=f.read_text();t=re.sub(r'```[^\n]*\n.*?```','',t,flags=re.S)
 for match in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)',t):
  dest=match[1]
  if re.match(r'^[a-zA-Z][\w+.-]*:',dest) or dest.startswith('#'):continue
  path=urllib.parse.unquote(dest.split('#')[0]);target=(f.parent/path).resolve();links+=1
  if not target.exists():link_errors.append({'file':str(f.relative_to(P)),'target':dest})
  elif '#FND-' in dest:
   anchor=dest.split('#',1)[1]
   if anchor not in FM:link_errors.append({'file':str(f.relative_to(P)),'missing_anchor':anchor})
checks['internal_markdown_links_checked']=links;checks['internal_link_errors']=link_errors
if link_errors:errors.append('Broken generated internal links')
# Inspect actual generated route patterns against raw declarations.
routes=load(P/'registries/routes.json');route_errors=[]
for r in routes:
 raw=r['raw_route_declaration'].split('defaults:',1)[0];variables=re.findall(r'[`\"\']variable[`\"\']\s*,\s*[`\"\'][^`\"\']*[`\"\']\s*,\s*[`\"\'][^`\"\']*[`\"\']\s*,\s*[`\"\'](\w+)[`\"\']',raw)
 for v in variables:
  if '{'+v+'}' not in r['url_pattern']:route_errors.append({'route':r['id'],'missing_variable':v})
checks['route_records_checked']=len(routes);checks['route_variable_errors']=route_errors
if route_errors:errors.append('Route variable reconstruction failed')
# Static literal redaction checks. This is not a mathematical proof of absence of all PII.
patterns={
 'jwt_literal':r'\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{8,}\b',
 'opaque_encoded_api_log':r'API_LOG: [A-Za-z0-9+/=]{80,}',
 'credential_assignment_literal':r'(?i)(?:api[_-]?key|access[_-]?token|password|csrf[_-]?token|sitekey)["\'`]?\s*[:=]\s*["\'`][A-Za-z0-9_\-/.+=]{12,}["\'`]',
 'known_fixture_handles':r'(?i)DotingProspect|Adam-it|Justin-Reid-BOT|Khaleel91|kingBeetlejuice1'}
redaction_hits=[];scanned=0
for f in P.rglob('*'):
 if not f.is_file() or f.suffix in ['.py','.bin']:continue
 if f.name in ['qa-report.json','checksums.sha256','ALL_FILES.md']:continue
 t=f.read_text(errors='replace');scanned+=1
 for name,pattern in patterns.items():
  matches=re.findall(pattern,t)
  if matches:redaction_hits.append({'file':str(f.relative_to(P)),'category':name,'count':len(matches)})
checks['redaction_scanned_text_files']=scanned;checks['redaction_pattern_hits']=redaction_hits
if redaction_hits:errors.append('Residual sensitive/fixture literal pattern matches; inspect before delivery')
warnings=[
 'Verified-observation findings usually verify stored declaration/content or recorded output, NOT current authenticated website behavior.',
 'Findings count includes granular schema fields,documentary blocks,URL literals and per-ply payloads; do not interpret it as independent website features.',
 'Entire minified bundles and native WASM/model semantics remain partially audited.',
 'No independent conversation-history/memory export,REA evidence backend,logged-in browser profile or private backend accessed.',
 'Redaction is heuristic; no guarantee against arbitrary unknown identifiers. Public game reference URLs remain as explicitly supplied technical references.',
 'Inaccessible-source count counts explicit missing entries,not every possible unmentioned legacy file.',
 'Source-embedded timestamps conflict with session date; no fabricated normalization or current deploy assertion.',
 'API endpoint registry includes literal candidates and declared routes; extraction false positives are preserved and not promoted into successful endpoints.']
report={'status':'PASS within declared checks' if not errors else 'FAIL — packaging blocked','checks':checks,'errors':errors,'warnings':warnings,
 'scope_statement':'All inventoried original/member bytes processed and originals unchanged. Semantic audit partial. No new website network probes performed.'}
dump(M/'qa-report.json',report)
if errors:
 print(json.dumps({'errors':errors,'redaction_hits':redaction_hits,'link_errors':link_errors[:30],'route_errors':route_errors[:10]},indent=2));raise SystemExit(1)
# Add final QC result to checkpoint, with no invented timestamp.
progress=M/'audit-progress.md';t=progress.read_text();t=t.split('\n## Final machine QC\n')[0]
progress.write_text(t+'\n## Final machine QC\n\n'+str(len(originals))+'original file hashes unchanged; '+str(sum(x['members_verified'] for x in archive_checks))+'archive member hashes matched; source/finding/URL IDs and generated links validated. All recovered Markdown body lines accounted for. Defined redaction patterns returned no residual hits in distributed text. See qa-report.json for exact checks and non-guarantees. Overall audit remains PARTIAL.\n')
# Index is comprehensive, including the QC/checksum outputs produced at the end.
files=sorted(str(f.relative_to(P)) for f in P.rglob('*') if f.is_file() and '__pycache__' not in f.parts and f.name!='ALL_FILES.md')
for extra in ['audit-metadata/checksums.sha256']:
 if extra not in files:files.append(extra)
(M/'ALL_FILES.md').write_text('# Complete audit output file index\n\n[Master index](../00_MASTER_INDEX.md)\n\n'+''.join('- ['+name+'](../'+name+')\n' for name in sorted(files))+'\nSource binaries/models and original ZIPs are hashed/indexed,not copied wholesale. All distributed text evidence is a separate redacted copy.\n')
files=sorted(f for f in P.rglob('*') if f.is_file() and '__pycache__' not in f.parts and f.name!='checksums.sha256')
(M/'checksums.sha256').write_text(''.join(sha(f)+'  '+str(f.relative_to(P))+'\n' for f in files))
archive=ROOT/'chesscom-knowledge-recovery-audit.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as z:
 for f in sorted(P.rglob('*')):
  if f.is_file() and '__pycache__' not in f.parts:z.write(f,'website-audit/'+str(f.relative_to(P)))
with zipfile.ZipFile(archive) as z:
 bad=z.testzip()
 if bad:raise RuntimeError('ZIP CRC check failed:'+bad)
 members=len(z.namelist())
print(json.dumps({'qc':'PASS within declared checks','audit_status':'PARTIAL','original_files_unchanged':len(originals),'archive_members_verified':sum(x['members_verified'] for x in archive_checks),'internal_links_validated':links,'zip':str(archive),'zip_bytes':archive.stat().st_size,'zip_sha256':sha(archive),'zip_members':members},indent=2))
