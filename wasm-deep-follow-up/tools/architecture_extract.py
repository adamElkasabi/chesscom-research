#!/usr/bin/env python3
from pathlib import Path
import re,json,hashlib,collections,shutil,urllib.parse,gzip
B=Path('/var/tmp/chess-forensic');I=B/'input';O=B/'output/website-audit';R=O/'registries';R.mkdir(exist_ok=True)
def dump(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,ensure_ascii=False))
# Reuse the original scrubber without rerunning its inventory/output side effects.
old=(I/'website-audit/audit-metadata/recover.py').read_text();ns={'re':re};exec(old[old.index('def scrub('):old.index('\ndef jwrite')],ns);scrub=ns['scrub']
PRIOR=O/'history/prior-audit'
if not PRIOR.exists():shutil.copytree(I/'website-audit',PRIOR)
S=json.loads((PRIOR/'audit-metadata/source-manifest.json').read_text());SM={s['location']:s for s in S};new=[]
# New evidence sources retain unique SRC IDs rather than recycling old ones.
for p in sorted((O/'evidence/new-public').glob('*')):
 if not p.is_file():continue
 sid=f'SRC-{3000+len(new):04d}';data=p.read_bytes();rec={'id':sid,'location':str(p.relative_to(O)),'type':'new_passive_public_evidence','bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'review_status':'full content read, targeted semantic review; not every unrelated script function interpreted','incorporated':True,'limits':'Public unauthenticated response only; source publication date may be older than observation.'};new.append(rec)
# Enumerate actual code/component/CSS declarations with exact offsets. Names are not guessed from screenshots.
components={};imports=[];storage=[];maps=[];keywords=[];scanned=[]
patterns={'React':r'\bReact\b|react-dom','Angular':r'@angular/|angular\.module','Vue':r'__vccOpts|__name:|/vue[./]|vue\.[A-Za-z0-9_-]+\.js','Svelte':r'\bsvelte\b|svelte/internal','Pinia':r'pinia|createPinia','jQuery':r'jQuery|jquery','Bootstrap':r'bootstrap(?:\.min)?\.css','Tailwind':r'tailwindcss|@tailwind','Material UI':r'@mui/|@material-ui/','Nuxt':r'__NUXT__|nuxt/','Next.js':r'__NEXT_DATA__|/_next/','Symfony-route-style':r'hosttokens:|prefix:|tokens:\[','Sass':r'\.scss\b|sass','Webpack':r'webpackChunk|__webpack_require__','Vite':r'/vite/|__vite__','Rolldown':r'rolldown','PHP':r'\bPHP\b|\.php\b','Doctrine':r'\bDoctrine\b','MySQL':r'\bMySQL\b','ASP.NET':r'ASP\.NET|__VIEWSTATE|X-AspNet','Laravel':r'laravel|XSRF-TOKEN','Django':r'csrftoken|django','Rails':r'Rails|_rails' }
files=sorted((I/'research').rglob('*'))+sorted(Path('/home/user/extension').rglob('*'))
for p in files:
 if not p.is_file():continue
 rel=str(p.relative_to(I)) if p.is_relative_to(I) else str(p.relative_to('/home/user'));data=p.read_bytes();scanned.append({'location':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'review':'complete bytes read; JS/HTML targeted declaration scan, not whole-program semantic review'})
 if p.suffix not in ['.js','.mjs','.cjs','.html','.css']:continue
 text=scrub(data.decode('utf8',errors='replace'));sid=SM.get(rel,{}).get('id')
 # Only original unarchived sources scanned here; prior manifest retains archive occurrences.
 for m in re.finditer(r'__name:\s*[`"\']([^`"\']+)',text):
  name=m[1];key=(name,hashlib.sha256(text[max(0,m.start()-40):m.start()+400].encode()).hexdigest());rec=components.setdefault(key,{'component_name':name,'implementation_evidence':'Vue compiled component __name declaration','occurrences':[],'purpose':'Name suggests '+name.replace('-',' ')+'; precise props/events captured only in the adjacent source excerpt, not inferred globally.','relationships':'Declaration/import context, not a recovered complete runtime hierarchy.','confidence':'CONFIRMED declaration; semantics require call-site interpretation'})
  rec['occurrences'].append({'source_id':sid,'location':rel,'character_offset':m.start(),'excerpt':text[max(0,m.start()-120):m.start()+1100]})
 for m in re.finditer(r'(?:customElements\.define\(|customElements\.get\()\s*[`"\']([^`"\']+)',text):
  name=m[1];key=('element:'+name,name);rec=components.setdefault(key,{'component_name':name,'implementation_evidence':'custom-element registration/lookup literal','occurrences':[],'purpose':'Custom element; full behavior depends on implementation/call sites.','relationships':'No global component hierarchy inferred.','confidence':'CONFIRMED reference, definition vs lookup distinguished in excerpt'})
  rec['occurrences'].append({'source_id':sid,'location':rel,'character_offset':m.start(),'excerpt':text[max(0,m.start()-80):m.start()+600]})
 for m in re.finditer(r'(?:import\s*(?:[^;\n]{0,500}?from\s*)?|import\()\s*[`"\']([^`"\']+)[`"\']',text):imports.append({'source_id':sid,'location':rel,'offset':m.start(),'target_literal':m[1],'status':'static import reference, not a fetched or executed request'})
 for m in re.finditer(r'(localStorage|sessionStorage|indexedDB)(.{0,150})',text):storage.append({'source_id':sid,'location':rel,'offset':m.start(),'excerpt':m[0]})
 for m in re.finditer(r'(?:sourceMappingURL=)([^\s*]+)',text):maps.append({'source_id':sid,'location':rel,'offset':m.start(),'literal':m[1],'retrieved':False,'limitation':'Reference recorded; no broad source-map guessing or credentialed access.'})
 for tech,pat in patterns.items():
  matches=list(re.finditer(pat,text,re.I))
  if matches:keywords.append({'technology':tech,'source_id':sid,'location':rel,'count':len(matches),'examples':[{'offset':m.start(),'excerpt':text[max(0,m.start()-100):m.end()+150]} for m in matches[:5]],'meaning':'Lexical indicator only. Historical notes,embedded third-party text,and unrelated substrings can be false positives; see reviewed technology matrix.'})
C=list(components.values())
for n,c in enumerate(C,1):c['id']=f'UI-{n:04d}'
dump(R/'components.json',C);dump(R/'script-imports.json',imports);dump(R/'browser-storage.json',storage);dump(R/'source-map-references.json',maps);dump(R/'technology-literal-indicators.json',keywords);dump(O/'audit-metadata/new-offline-source-scan.json',scanned)
# Full actual CSS token/selector/font/media-query extraction across fetched stylesheets.
css=[]
for p in sorted((O/'evidence/new-public').glob('*.css')):
 text=p.read_text();sid=next(s['id'] for s in new if s['location']==str(p.relative_to(O)))
 rec={'source_id':sid,'file':str(p.relative_to(O)),'variables':[{'name':m[1],'value':m[2],'offset':m.start()} for m in re.finditer(r'(--[\w-]+)\s*:\s*([^;}]+)',text)],'media_queries':[{'condition':m[1],'offset':m.start()} for m in re.finditer(r'@media\s*([^{}]+)\{',text)],'font_faces':re.findall(r'@font-face\s*\{[^}]+\}',text),'font_families':sorted(set(re.findall(r'font-family:([^;}]+)',text))),'selectors':[{'selector':m[1].strip(),'offset':m.start()} for m in re.finditer(r'([^{}]+)\{',text) if not m[1].lstrip().startswith('@')],'export_blocks':re.findall(r':export\{[^}]+\}',text)}
 css.append(rec)
dump(R/'design-system.json',css)
# HTML static inventory distinguishes actual tags/forms from implemented backend handlers.
pages=[]
for p in [I/'research/analysis.html',I/'research/refinement/live-game-page.html',*sorted((O/'evidence/new-public').glob('*.html'))]:
 text=scrub(p.read_text());loc=str(p.relative_to(O)) if p.is_relative_to(O) else str(p.relative_to(I));sid=next((s['id'] for s in new if s['location']==loc),SM.get(loc,{}).get('id'));title=re.search(r'<title[^>]*>(.*?)</title>',text,re.S|re.I)
 pages.append({'source_id':sid,'location':loc,'title':title[1].strip() if title else None,'forms':[{'opening_tag':m[0],'offset':m.start()} for m in re.finditer(r'<form\b[^>]*>',text,re.I)],'inputs':[{'tag':m[0],'offset':m.start()} for m in re.finditer(r'<(?:input|select|textarea)\b[^>]*>',text,re.I)],'stylesheets':re.findall(r'<link[^>]*rel=["\']stylesheet["\'][^>]*>',text,re.I),'script_opening_tags':re.findall(r'<script\b[^>]*>',text,re.I),'limits':'Saved/public unauthenticated static HTML only; forms not submitted, roles/session/error/redirect behavior not inferred.'})
dump(R/'page-markup-inventory.json',pages)
# Module URL literals and download-script origins, preserving templates/guessed failures.
U=[json.loads(l) for l in (PRIOR/'audit-metadata/urls.jsonl').read_text().splitlines()];wasmrefs=[]
for u in U:
 if '.wasm' not in u['url']:continue
 url=u['url'];status='Referenced; no available matching standalone binary established by this literal.'
 if '${' in url or '$i' in url:status='Unresolved template, not a single exact module URL.'
 elif 'github.com' in url:status='Repository/documentation URL, not a binary asset.'
 wasmrefs.append({'reference_id':u['id'],'literal':url,'source_ids':u['source_ids'],'occurrences':u['occurrences'],'retrieval_status':status,'new_download_attempted':False,'limitation':'Previously available concrete binaries analyzed; additional versions,templates and multipart Torch references require a further bounded retrieval batch. No invented404orcurrentavailabilityclaim. Historical HTTP outcomes remain in prior audit.'})
dump(O/'wasm-analysis/wasm-url-references.json',wasmrefs)
# Actual offline downloads are sourced to the saved download script, not a guessed current URL.
origins={
 'explanation-engine.no-simd.wasm':'https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanation-engine.wasm',
 'explanation-engine.wasm':'https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.wasm',
 'stockfish-nnue-16-no-Worker.wasm':'https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16-no-Worker.wasm',
 'stockfish-nnue-16-single.wasm':'https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16-single.wasm',
 'torch-2-lite-single.wasm':'https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm'}
for p in sorted((O/'wasm-analysis/modules').glob('*/structure.json')):
 d=json.loads(p.read_text());d['original_url_from_saved_download_script']=origins[Path(d['original_location']).name];d['retrieval_status']='Available exact local bytes preserved; no new download or current deployment equivalence assumed.';dump(p,d)
 for name in ['module.wasm','loader.js']:
  f=p.parent/name
  if f.exists():new.append({'id':f'SRC-{3000+len(new):04d}','location':str(f.relative_to(O)),'type':'available_original_wasm' if name.endswith('wasm') else 'original_loader_glue','bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'original_location':d['original_location'] if name.endswith('wasm') else d.get('loader_original_location'),'url':d['original_url_from_saved_download_script'] if name.endswith('wasm') else 'See original download script for wrapper URL','review_status':'complete structural/function-index/call-graph/opcode/string extraction; selected export semantics reviewed' if name.endswith('wasm') else 'targeted import/export/marshalling/loading semantics reviewed; not every generated runtime branch','incorporated':True,'limits':'Function inventory is not a semantic explanation of every function.'})
# Original Markdown copies remain privacy-redacted, originals intact elsewhere.
D=O/'original-documentation';D.mkdir(exist_ok=True)
for s in S:
 if s['type']!='original_markdown' or not s.get('evidence_copy'):continue
 p=PRIOR/s['evidence_copy'];dest=D/(s['id']+'-'+Path(s['location']).name)
 if p.exists():dest.write_text(p.read_text());
# Unified manifest retains original schema while fixing copied evidence locations.
for s in S:
 if s.get('evidence_copy'):s['evidence_copy']='history/prior-audit/'+s['evidence_copy']
 s['recovery_batch']='prior audited recovery; historical status retained'
S+=new;dump(O/'audit-metadata/source-manifest.json',S);dump(O/'audit-metadata/new-source-manifest.json',new)
print(json.dumps({'new_sources':len(new),'offline_files_read':len(scanned),'implementation_component_declarations':len(C),'css_files':len(css),'css_variable_declarations':sum(len(x['variables']) for x in css),'media_queries':sum(len(x['media_queries']) for x in css),'script_imports':len(imports),'source_map_references':len(maps),'WASM_reference_literals':len(wasmrefs),'page_markup_artifacts':len(pages)},indent=2))
