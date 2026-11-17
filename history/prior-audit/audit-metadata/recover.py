#!/usr/bin/env python3
"""Offline recovery only. Never executes website JS, accesses an account, or changes originals."""
from pathlib import Path
import json,hashlib,re,zipfile,collections,html,os
ROOT=Path('/home/user'); OUT=ROOT/'website-audit'; META=OUT/'audit-metadata'
originals=json.loads((META/'original-snapshot.json').read_text())
SOURCES=[]; DATA={}; BYLOC={}; URLS={}; REDACTIONS=collections.Counter()

def scrub(s):
    # Redact personal fixture handles and IDs, credentials and credential-like literals.
    s=re.sub(r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b','[REDACTED_EMAIL]',s)
    s=re.sub(r'\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{8,}\b','[REDACTED_JWT]',s)
    s=re.sub(r'(?i)(https?://)[^/\s:@]+:[^/\s@]+@',r'\1[REDACTED_USERINFO]@',s)
    s=re.sub(r'(?i)([?&](?:access_token|refresh_token|token|api_key|apikey|secret|password|session|sessionid|csrf|auth|key)=)[^&\s\"\'<>`]*',r'\1[REDACTED]',s)
    # Literal assignments only, not schema/property names or variables.
    pat=r'''(?i)((?:["'`])?(?:api[_-]?key|access[_-]?token|refresh[_-]?token|csrf[_-]?token|csrfToken|password|authorization|session[_-]?id|sessionId|secret|userId|user_id|username|firstName|lastName|displayName)(?:["'`])?\s*[:=]\s*)(["'`])([^\n"'`]{1,300})\2'''
    s=re.sub(pat,lambda m:m[1]+m[2]+'[REDACTED_LITERAL]'+m[2] if '${' not in m[3] else m[0],s)
    s=re.sub(r'(?i)(["\'](?:userId|user_id)["\']\s*:\s*)\d+',r'\1"[REDACTED_ID]"',s)
    s=re.sub(r'(?i)((?:csrf|token|api-key|password)[^>]{0,80}\b(?:content|value)\s*=\s*["\'])[^"\']+(["\'])',r'\1[REDACTED]\2',s)
    for name in ['DotingProspect','Adam-it','Justin-Reid-BOT','Khaleel91','kingBeetlejuice1']:
        s=s.replace(name,'[PUBLIC_PLAYER_HANDLE_REDACTED]')
    for ident in ['620664862','403789339','198665411']:
        s=s.replace(ident,'[PUBLIC_USER_ID_REDACTED]')
    # Encoded API logs can contain embedded PGNs/identities; decoded technical
    # command logs are separately preserved. Do not distribute opaque payloads.
    s=re.sub(r'(API_LOG: )[A-Za-z0-9+/=]{80,}',r'\1[REDACTED_ENCODED_PAYLOAD]',s)
    s=re.sub(r'(?i)(["\'`]?(?:sitekey|data-sitekey)["\'`]?\s*[:=]\s*["\'`])[^"\'`]{8,}(["\'`])',r'\1[REDACTED_PUBLIC_SITE_KEY]\2',s)
    # Sentry DSN embeds a public ingestion key; preserve the shape, not the value.
    s=re.sub(r'(https://)[a-f0-9]{16,64}(@[^\s"\'`<>]+)',r'\1[REDACTED_PUBLIC_DSN_KEY]\2',s)
    return s

def jwrite(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,ensure_ascii=False))
def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
def typ(loc):
    x=loc.lower()
    if x.endswith('.md'):return 'original_markdown'
    if x.endswith('.proto'):return 'rendered_protobuf_schema'
    if 'wasm-descriptors' in x and x.endswith('.bin'):return 'native_protobuf_descriptor'
    if x.endswith('.wasm'):return 'wasm_binary'
    if x.endswith('.nnue'):return 'neural_network_asset'
    if x.endswith('.zip'):return 'archive'
    if x.endswith('.json'):return 'json_artifact'
    if x.endswith(('.js','.mjs','.cjs','.py','.sh')):return 'source_code'
    if x.endswith('.html'):return 'saved_html'
    if x.endswith('.pgn'):return 'game_fixture'
    if x.endswith(('.out','.txt','.sha256','.csv')):return 'notes_logs_or_dataset'
    return 'other'

def purpose(loc,t):
    if '/proto/' in loc or 'wasm-descriptors' in loc:return 'Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.'
    if '/results/' in loc or '/holdout/' in loc:return 'Isolated experiment configuration/result or validation artifact; inspect config/error before interpreting output.'
    if '/configs/' in loc:return 'Experiment input; configuration existence is NOT proof the trial completed.'
    if 'resource-failed' in loc:return 'Resource-pressure failed attempt, not a valid numerical result.'
    if '/test/' in loc:return 'Test harness or simulated browser/engine fixture; not a production Chess.com network trace.'
    if 'staged/' in loc:return 'Unpromoted implementation sketch; must not be mistaken for production.'
    if loc.startswith('extension/engines/'):return 'Locally packaged website engine asset.'
    if loc.startswith('extension/'):return 'Current extension implementation/documentation; distinguish from native website code.'
    if loc.startswith('uploads/'):return 'User-supplied historical investigation document; some claims require correction or original evidence is absent.'
    if 'chunk' in loc or loc.endswith(('analysis.js','play.js','checkmate.js')):return 'Saved public frontend bundle; static content, not authenticated runtime observation.'
    return 'Historical investigation material; preserve exact contents and provenance.'

ABS=re.compile(r'(?:https?|wss?|git\+https):(?:\\?/){2}[^\s"\'`<>\x00-\x1f]+')
REL=re.compile(r'''["'`]((?:/{1,2}(?![/*])|\./|r2/|bundles/)[^\s"'`<>\x00-\x1f]{1,1000})["'`]''')
def urltype(u):
    if u.startswith('wss:') or re.search(r'/(?:rpc|callback|api|v[12]/(?:game-review|run-search))[/\?]?',u):return 'api_or_websocket_candidate'
    if re.search(r'\.(?:js|wasm|css|png|svg|webp|jpg|jpeg|mp3|ogg|woff2?|nnue|bin|bzp)(?:[?#]|$)',u) or '/r2/' in u or '/bundles/' in u:return 'asset'
    if u.startswith(('/', 'https://www.chess.com')):return 'page_or_route_candidate'
    return 'external_or_documentation'

def addurl(raw,sid,offset,context,kind='absolute'):
    u=scrub(raw).replace('\\/','/').rstrip('.,;')
    # Do not strip balanced query/fragment syntax; trailing JS delimiters are flagged, not claimed visited.
    if len(u)>2500:return
    rec=URLS.setdefault(u,{'url':u,'type':urltype(u),'reference_form':kind,'source_ids':[],'occurrences':[],
       'directly_visited':'not established from literal alone','verification_status':'observed literal only; not re-fetched during this audit',
       'date':'source-embedded date if present; filesystem time is not a verification date','related_findings':[]})
    if sid not in rec['source_ids']:rec['source_ids'].append(sid)
    rec['occurrences'].append({'source_id':sid,'character_offset':offset,'context':scrub(context)[:500]})


def add_source(loc,b,parent=None,kind=None):
    sid=f'SRC-{len(SOURCES)+1:04d}';t=kind or typ(loc);sha=hashlib.sha256(b).hexdigest()
    rec={'id':sid,'type':t,'location':loc,'parent_source_id':parent,'bytes':len(b),'sha256':sha,'purpose':purpose(loc,t),
      'reviewed':True,'review_method':[],'semantic_review':'partial unless a structured type or explicitly reviewed document',
      'limitations':[],'incorporated':False,'findings':[],'url_count':0,'cross_references':[]}
    SOURCES.append(rec);BYLOC[loc]=sid
    if t=='archive':rec['review_method']=['ZIP member listing, checksums, member-by-member content processing'];return sid
    if t in ['wasm_binary','neural_network_asset','native_protobuf_descriptor']:
        rec['review_method']=['read entire binary; checksum; string/interface extraction where applicable']
        rec['limitations'].append('Not a full instruction-level/native algorithm or network-weight semantic audit.')
        strings=re.findall(rb'[\x20-\x7e]{8,}',b)
        relevant=[x.decode('ascii') for x in strings if re.search(rb'https?://|wss?://|Torch|torch|[Mm]aia|CEE_|feature_|\.proto|\.cpp|\.h$|requires|incompatible|unsupported|UCI|[Cc]harm|[Pp][Vv][Tt]ree|validation_hash',x)]
        text='\n'.join(relevant)
        if t=='native_protobuf_descriptor':
            (OUT/'evidence/descriptors').mkdir(parents=True,exist_ok=True)
            path=Path('evidence/descriptors')/(sha+'.bin');(OUT/path).write_bytes(b);rec['evidence_copy']=str(path)
        else:
            path=Path('evidence/binary-strings')/(sha+'.txt');write(OUT/path,scrub(text));rec['evidence_copy']=str(path)
        rec['extracted_relevant_strings']=len(relevant)
    else:
        try:text=b.decode('utf-8');rec['encoding']='UTF-8'
        except UnicodeDecodeError:text=b.decode('utf-8',errors='replace');rec['limitations'].append('Non-UTF8 bytes replaced in textual inspection.')
        rec['review_method']=['full text read; URL and reference scan; type-specific structured extraction']
        safe=scrub(text)
        if safe!=text:rec['redacted_evidence']=True;REDACTIONS[t]+=1
        ext=Path(loc.split('!/')[-1]).suffix or '.txt';path=Path('evidence/text')/(sha+ext)
        write(OUT/path,safe);rec['evidence_copy']=str(path)
        rec['lines']=len(text.splitlines());rec['headings']=[scrub(h) for h in re.findall(r'^#{1,6}\s+(.+)',text,re.M)]
        if t=='original_markdown':rec['semantic_review']='direct document reading plus block-level extraction; claims are not automatically validated'
        if t=='json_artifact':
            try:
                obj=json.loads(text);rec['json_type']=type(obj).__name__;rec['top_level_keys']=list(obj)[:100] if isinstance(obj,dict) else None
            except Exception as e:rec['limitations'].append('JSON parse error: '+str(e))
        rec['cross_references']=sorted(set(re.findall(r'`([^`\n]{1,200}\.(?:md|mjs|js|proto|json|py|bin|html|wasm))`',text)))[:500]
    DATA[sid]=text
    for m in ABS.finditer(text):addurl(m[0],sid,m.start(),text[max(0,m.start()-90):m.end()+90])
    for m in REL.finditer(text):addurl(m[1],sid,m.start(1),text[max(0,m.start()-90):m.end()+90],'relative_literal')
    rec['url_count']=sum(sid in u['source_ids'] for u in URLS.values())
    return sid

for row in originals:
    loc=row['path'];b=(ROOT/loc).read_bytes();sid=add_source(loc,b)
    if loc.endswith('.zip'):
        with zipfile.ZipFile(ROOT/loc) as z:
            for i in z.infolist():
                if i.is_dir():continue
                add_source(loc+'!/'+i.filename,z.read(i),sid)
# Record the accessible conversation as one source, not a fictional external archive.
conv=(META/'conversation-recovery.txt').read_bytes();sid=add_source('accessible-conversation/current-and-condensed-history',conv,kind='conversation_reconstruction')
SOURCES[-1]['limitations']=['Reconstructed from context available in this session; not a full transcript/export and not a separate memory search.']
SOURCES[-1]['semantic_review']='directly reviewed current conversation and condensed history'
# Deduplicate evidence while preserving each source occurrence.
byhash=collections.defaultdict(list)
for s in SOURCES:byhash[s['sha256']].append(s['id'])
for s in SOURCES:s['same_content_source_ids']=[x for x in byhash[s['sha256']] if x!=s['id']]
for i,(u,r) in enumerate(sorted(URLS.items()),1):r['id']=f'URL-{i:05d}'
jwrite(META/'source-manifest.json',SOURCES)
jwrite(META/'source-content-index.json',{sid:rec.get('evidence_copy') for sid,rec in [(s['id'],s) for s in SOURCES] if rec.get('evidence_copy')})
jwrite(META/'source-locations.json',BYLOC)
with (META/'urls.jsonl').open('w') as f:
 for u in sorted(URLS.values(),key=lambda x:x['id']):f.write(json.dumps(u,ensure_ascii=False)+'\n')
jwrite(META/'scan-statistics.json',{'original_files':len(originals),'sources_including_archive_members_and_conversation':len(SOURCES),'archive_members':sum(bool(s['parent_source_id']) for s in SOURCES),'original_markdown_sources':sum(s['type']=='original_markdown' for s in SOURCES),'unique_urls_and_relative_references':len(URLS),'absolute_urls':sum(u.startswith(('http:','https:','wss:','ws:','git+https:')) for u in URLS),'redacted_evidence_sources_by_type':REDACTIONS})
print(json.dumps(json.loads((META/'scan-statistics.json').read_text()),indent=2))
