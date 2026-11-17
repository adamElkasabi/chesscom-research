# Executed by build_audit.py. All counts are computed from recovered artifacts.
from urllib.parse import urlsplit
cats=collections.defaultdict(list)
for f in F:cats[f['category']].append(f)
FIND_LINK={};shard_index=[]
# Render detailed, bounded findings files; do not truncate source blocks or schema details.
for cat,items in cats.items():
 for start in range(0,len(items),100):
  batch=items[start:start+100];name=f'{cat}-{start//100+1:03d}.md';rel='findings/'+name
  blocks=[f'# {cat} — findings {start+1}–{start+len(batch)}\n\n[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)\n']
  for f in batch:
   FIND_LINK[f['id']]=rel+'#'+f['id']
   blocks.append(f'\n<a id="{f["id"]}"></a>\n## {f["id"]}: {f["title"]}\n\n'
    +f'**Category:** {f["category"]}  \n**Classification:** {f["classification"]}  \n**Verification:** {f["verification_status"]}  \n**Confidence:** {f["confidence"]["level"]} — {f["confidence"]["explanation"]}\n\n'
    +f['detailed_description']+'\n\n### Evidence\n\n')
   for e in f['evidence']:
    ss=SM[e['source_id']];dest=ss.get('evidence_copy')
    blocks.append(f'- **{ss["id"]}** `{ss["location"]}`'+(f' — [preserved redacted evidence](../{dest})' if dest else '')+'\n')
    if e.get('line_start'):blocks.append(f'  Lines {e["line_start"]}–{e.get("line_end",e["line_start"])}.\n')
    if e.get('character_offset') is not None:blocks.append('  Character offset '+str(e['character_offset'])+'.\n')
    if e.get('excerpt'):blocks.append('\n```text\n'+e['excerpt']+'\n```\n')
   blocks.append('\n**Source references:** '+', '.join(f['source_references'])+'  \n**URL references:** '+(', '.join('<'+u+'>' for u in f['url_references']) or 'None independently associated')+'  \n**Related findings:** '+(', '.join(f['related_findings']) or 'None assigned')+'\n\n**Additional notes:** '+(f['additional_notes'] or 'No additional caveat recorded beyond the source scope and confidence above.')+'\n')
  put(OUT/rel,''.join(blocks));shard_index.append((rel,len(batch),cat))
def fl(fid):return f'[{fid}]({FIND_LINK[fid]})'
def table(head,rows):return '| '+' | '.join(head)+' |\n| '+' | '.join('---' for _ in head)+' |\n'+'\n'.join('| '+' | '.join(str(v).replace('|','\\|').replace('\n',' ') for v in row)+' |' for row in rows)+'\n'
def chapter(name,title,intro,categories=(),extra=''):
 selected=[f for cat in categories for f in cats.get(cat,[])]
 body='# '+title+'\n\n[Master index](00_MASTER_INDEX.md)\n\n'+intro+'\n\n'+extra
 if selected:body+='\n## Detailed findings\n\n'+''.join('- '+fl(f['id'])+' — '+f['title']+'\n' for f in selected)
 put(OUT/name,body)
# Source inventory split into manageable pages; every source is still a full record.
source_shards=[]
for start in range(0,len(S),100):
 rel=f'registries/sources-{start//100+1:03d}.md';source_shards.append(rel);parts=['# Source inventory\n\n[Master index](../00_MASTER_INDEX.md)\n']
 for s in S[start:start+100]:
  parts.append(f'\n## {s["id"]} — `{s["location"]}`\n\n')
  parts.append(f'- Type: {s["type"]}; bytes: {s["bytes"]}; SHA-256: `{s["sha256"]}`.\n- Purpose: {s["purpose"]}\n- Reviewed: full content processed; method: '+', '.join(s['review_method'])+'.\n- Semantic review: '+s['semantic_review']+'.\n- Main topics: '+(', '.join(s['main_topics']) or 'No separately extracted finding; see preserved evidence')+'.\n- Findings: '+str(s['finding_count'])+'; types: '+json.dumps(s['finding_types'])+'.\n- URL/reference count: '+str(s['url_count'])+'.\n- Incorporated: '+str(s['incorporated'])+'.\n')
  if s.get('evidence_copy'):parts.append(f'- [Preserved evidence](../{s["evidence_copy"]}) (privacy-redacted where needed).\n')
  parts.append('- Cross-references: '+(', '.join('`'+r+'`' for r in s['cross_references']) or 'None extracted')+'.\n- Limits / potential missing sections: '+('; '.join(s['limitations']+s['potential_missing_sections']) or 'Static artifacts do not verify current deployed behavior.')+'\n')
  if s.get('accounting_note'):parts.append('- Accounting: '+s['accounting_note']+'\n')
  if s['findings']:parts.append('- Finding IDs: '+', '.join(f'[{fid}](../{FIND_LINK[fid]})' for fid in s['findings'])+'\n')
 put(OUT/rel,''.join(parts))
# URL registry pages preserve ALL occurrences, not just one deduplicated discovery.
url_shards=[]
for start in range(0,len(U),50):
 rel=f'registries/urls-{start//50+1:03d}.md';url_shards.append(rel);parts=['# URL and reference inventory\n\n[Master index](../00_MASTER_INDEX.md)\n']
 for u in U[start:start+50]:
  display='<'+u['url']+'>' if u['reference_form']=='absolute' else '`'+u['url']+'`'
  parts.append(f'\n## {u["id"]}\n\n{display}\n\n- Type: {u["type"]}; form: {u["reference_form"]}.\n- Visited: {u["directly_visited"]}.\n- Verified: {u["verification_status"]}.\n- Date: {u["date"]}.\n- Related findings: '+', '.join(f'[{x}](../{FIND_LINK[x]})' for x in u['related_findings'])+'.\n')
  for occ in u['occurrences']:
   parts.append(f'\n### {occ["source_id"]} at character {occ["character_offset"]}\n\n```text\n{occ["context"]}\n```\n')
 put(OUT/rel,''.join(parts))
# Route inventory pages contain methods/defaults/requirements and explicitly unknown runtime fields.
route_shards=[]
for start in range(0,len(ROUTES),40):
 rel=f'registries/routes-{start//40+1:03d}.md';route_shards.append(rel);parts=['# Declared page and route inventory\n\n[Master index](../00_MASTER_INDEX.md)\n']
 for r in ROUTES[start:start+40]:
  parts.append(f'\n## {r["id"]} — {r["route_name"]}\n\n- URL pattern (derived): `{r["url_pattern"]}`\n- Methods: '+', '.join(r['http_methods'])+'\n- Purpose: '+r['purpose']+'\n- Title,roles,authentication,forms,UI,data,redirects,errors: not established by this static declaration.\n- Sources: '+', '.join(r['source_ids'])+'\n- Detailed finding: '+f'[{r["finding_id"]}](../{FIND_LINK[r["finding_id"]]})'+'\n\n```javascript\n'+r['raw_route_declaration']+'\n```\n')
 put(OUT/rel,''.join(parts))
# Every recovered absolute API/WS-looking literal and declared callback route is documented.
ENDPOINTS=[]
for u in U:
 if u['type']=='api_or_websocket_candidate':
  ENDPOINTS.append({'id':f'API-{len(ENDPOINTS)+1:04d}','reference':u['url'],'kind':'observed URL literal candidate',
   'http_method':'WebSocket handshake GET' if u['url'].startswith('wss:') else 'not established by URL literal',
   'authentication':'not established','request_headers':'not captured','request_body':'not inferred; see relevant schema/call-site findings','response':'not inferred; see native CEAC/BrilliantVerification schema findings',
   'observed_status':'see historical-http-probes.json if exact URL is present','pagination':'not established','filtering_sorting':'not established','redirects':'not established','source_ids':u['source_ids'],'url_id':u['id'],'related_findings':u['related_findings']})
for r in ROUTES:
 if any(x in r['route_name'].lower() for x in ['callback','rpc','api_']) or '/callback/' in r['url_pattern']:
  ENDPOINTS.append({'id':f'API-{len(ENDPOINTS)+1:04d}','reference':r['url_pattern'],'kind':'declared route, not observed request','http_method':r['http_methods'],
   'request_headers':'not captured','request_body':'not established','response':'not established','observed_status':'not observed','authentication':'not established',
   'pagination':'not established','filtering_sorting':'not established','redirects':'not established','source_ids':r['source_ids'],'route_id':r['id'],'related_findings':[r['finding_id']]})
dump(OUT/'registries/endpoints.json',ENDPOINTS)
end_shards=[]
for start in range(0,len(ENDPOINTS),50):
 rel=f'registries/endpoints-{start//50+1:03d}.md';end_shards.append(rel)
 put(OUT/rel,'# Endpoint declarations and candidates\n\n[Master index](../00_MASTER_INDEX.md)\n\n'+''.join('## '+r['id']+'\n\n```json\n'+pretty(r)+'\n```\n\n' for r in ENDPOINTS[start:start+50]))
# Semantic annotations for actual observed pages, not a fabricated whole-site crawl.
pages=[]
for loc in ['research/analysis.html','research/refinement/live-game-page.html']:
 st=text(loc);title=re.search(r'<title[^>]*>(.*?)</title>',st,re.S|re.I)
 pages.append({'source_id':src(loc),'saved_page':loc,'title':html.unescape(title[1]).strip() if title else 'not extracted','links':[u['id'] for u in U if src(loc) in u['source_ids']],
 'access':'historical saved public/logged-out HTML; no authenticated profile in audit','forms_and_inputs':'See preserved full HTML; behavior beyond static markup not established','redirects':'original/final redirect chain not preserved','api_calls':'script imports are static references, not a runtime HAR'})
dump(OUT/'registries/saved-pages.json',pages)

st=json.loads((META/'scan-statistics.json').read_text())
loosemd=[s for s in S if s['type']=='original_markdown' and not s['parent_source_id']]
archive_md=[s for s in S if s['type']=='original_markdown' and s['parent_source_id']]
status_counts=collections.Counter(f['classification'] for f in F);vcounts=collections.Counter(f['verification_status'] for f in F)
METRICS={'audit_status':'PARTIALLY AUDITED — complete byte/text scan and structured recovery; incomplete semantic interpretation of large bundles/native algorithms',
 'original_documentation_files_discovered':len(loosemd),'original_documentation_files_inspected':len(loosemd),'archived_markdown_members_inspected':len(archive_md),'unique_original_markdown_contents':len(set(s['sha256'] for s in S if s['type']=='original_markdown')),
 'original_workspace_files_inventoried':len(originals) if 'originals' in globals() else len(json.loads((META/'original-snapshot.json').read_text())),
 'total_source_records_processed':len(S),'other_artifacts_content_processed':sum(s['type'] not in ['original_markdown','conversation_reconstruction'] for s in S),
 'memory_conversation_sources_accessed':sum(s['type']=='conversation_reconstruction' for s in S),'findings_recovered':len(F),'findings_classified_verified_observation':status_counts['verified observation'],
 'findings_verification_status_verified':vcounts['verified'],'inferred_findings':status_counts['inference'],'hypotheses':status_counts['hypothesis'],'unknown_or_documentary_unverified_claims':status_counts['unknown'],
 'absolute_urls':st['absolute_urls'],'relative_references':len(U)-st['absolute_urls'],'all_unique_url_and_relative_references':len(U),'url_occurrences':sum(len(u['occurrences']) for u in U),
 'api_endpoint_declarations_or_candidates':len(ENDPOINTS),'rpc_methods_declared_in_native_descriptors':len(SERVICES),'declared_route_records':len(ROUTES),'saved_page_artifacts':len(pages),
 'unresolved_knowledge_gaps':len(GAPS),'contradictions_or_version_distinctions':len(CONTRA),'inaccessible_source_entries':len(UNAVAILABLE),
 'curated_semantic_findings':len(CURATED),'schema_records':len(SCHEMAS),'original_document_blocks_preserved':len(DOCBLOCKS),'unique_trial_result_records':len(TRIALS)}
dump(META/'completeness-metrics.json',METRICS)
# Findings index with precise counts and granularity caveat.
put(OUT/'findings/FINDINGS_INDEX.md','# Findings index\n\n[Master index](../00_MASTER_INDEX.md)\n\n'+f'{len(F)} uniquely numbered records, including individual schema fields/enum values, historical documentary blocks, source URL literals, and experiment outputs. This count is NOT a count of independently runtime-verified website behaviors.\n\n'+''.join(f'- [{rel.split("/")[-1]}]({rel.split("/")[-1]}) — {num} records ({cat})\n' for rel,num,cat in shard_index))
chapter('01_EXECUTIVE_OVERVIEW.md','Executive overview and scope',
 'This is an offline forensic recovery of the Chess.com investigation and its local extension, not a newly authenticated whole-site audit. All original files remain intact. Every original file and archive member was read for content/checksum/type-specific extraction, but not every function in multi-megabyte minified bundles or every WASM instruction has been semantically audited. **Overall status: partially audited.**\n\nThe new corpus preserves redacted evidence, every original Markdown block, exact schema namespaces/fields, every recovered URL occurrence, route declarations, trial outcomes, and claim conflicts. No production website mutation or new endpoint probing was performed.',extra='## Actual metrics\n\n'+table(['Metric','Result'],METRICS.items())+'\n## Main corrections\n\n- Website Game Review uses a server in the inspected native frontend, while shipped CEE can nevertheless calculate reviews locally.\n- Legacy analysis and compact CEE classifications are different enums.\n- Low-level engine11 does not rule out an active human-mode search.\n- A complete experimental human-preloaded review exists, but cloud parity does not.\n- Old audio-unknown notes were followed by user confirmation.\n- 2%progress was a coarse milestone, not a confirmed hidden-badge regression.\n- v0.1.9progress is a calibrated local duration estimate, not engine position progress.\n- Schema coexistence of CAPS2andaverageCP loss does not reveal the accuracy formula.\n')
chapter('02_SOURCE_INVENTORY.md','Complete source inventory',
 f'{len(S)} source records: original files, individually read archive members, and one current/condensed conversation reconstruction. Duplicate content retains separate source provenance and equivalent-content IDs. Reviewed means the content was actually read by a tool/script; it does not imply exhaustive semantic interpretation.\n\nBinary files were hashed and inspected for strings/descriptors; no full native disassembly is claimed.',extra='## Inventory shards\n\n'+''.join(f'- [{x}]({x})\n' for x in source_shards)+'\n## Machine-readable\n\n- [Full source manifest](audit-metadata/source-manifest.json)\n- [Original pre-audit SHA-256 snapshot](audit-metadata/original-snapshot.json)\n- [Unavailable sources](audit-metadata/unavailable-sources.json)\n- [Conversation recovery and limitations](audit-metadata/conversation-recovery.txt)\n')
chapter('03_RECOVERED_KNOWLEDGE.md','Recovered knowledge — granular entry points',
 'Do not substitute this map for the detailed records. Each finding includes the requested category,description,classification,evidence,URL/source references,confidence,verification status,relations and caveats. Historical documentation blocks remain complete after privacy redaction.',extra='- [All detailed findings](findings/FINDINGS_INDEX.md)\n- [Machine-readable finding ledger](audit-metadata/findings-ledger.jsonl)\n- [Schemas](registries/schemas.json)\n- [Native descriptor JSON directory](registries/native-descriptors/)\n- [Trial outcomes](registries/trials.json)\n- [Original document blocks](registries/document-blocks.json)\n\n## Curated semantic findings\n\n'+''.join('- '+fl(fid)+' — '+F[int(fid.split('-')[1])-1]['title']+'\n' for fid in CURATED))
chapter('04_SITE_MAP_AND_ROUTES.md','Site map and declared routes',
 f'{len(ROUTES)}distinct route-name/declaration pairs recovered from stored generated route tables. Patterns were reconstructed from reversed Symfony-style token arrays; declared hosts/defaults/regexes are preserved. A declared route is not evidence of successful access,authentication policy,HTTPstatus,or current deployment.',('routes',),extra='## Route inventory shards\n\n'+''.join(f'- [{x}]({x})\n' for x in route_shards)+'\n[Machine route registry](registries/routes.json)\n')
chapter('05_PAGE_INVENTORY.md','Page inventory and accessibility boundaries',
 'The saved HTML artifacts cover the analysis page and example live-game page. Uploaded historical research also targets /play/computer, but its original runtime session is not available. Native links include analysis/review, classroom and other routes; they were not all visited. For declared private-looking routes,authentication/roles remain unknown.',extra='```json\n'+pretty(pages)+'\n```\n\nEvery additional discovered declaration is in [the route inventory](04_SITE_MAP_AND_ROUTES.md). Every page-like absolute/relative literal remains in [the URL index](16_URL_AND_REFERENCE_INDEX.md). No complete authenticated navigation tree is claimed.\n')
chapter('06_FRONTEND_ARCHITECTURE.md','Frontend architecture',
 'Saved public bundles establish package imports,Vue/Pinia APIs,custom elements,Vite/Rolldown-style packaging,dynamic chunks,feature flags,storage and workers. Different pages/package dates can use different component stacks. Svelte-like interpretation in old evaluation-bar research is an inference,not a version-verified library identity. See preserved source snippets and exact imports.',('frontend','architecture','evaluation_bar','extension','progress'))
chapter('07_BACKEND_ARCHITECTURE.md','Backend architecture and limits',
 'Externally supported relationships: CEAC Game Review and run-search WebSockets,maximum-analysis host variants,BrilliantVerification RPC declarations,report-card payloads. No backend source/database/private repository was accessed. Generated route tables do not prove a backend language/framework. Models and client flags do not establish server authorization enforcement. Unknown implementation details remain in the gaps register.',('api_schema_services',))
chapter('08_API_AND_NETWORK_INVENTORY.md','API and network inventory',
 f'{len(ENDPOINTS)}API/WS-looking URL literals or declared callback routes are inventoried below. They are explicitly labelled candidates/declarations,not all observed successful endpoints. Headers,auth,request/response,status,pagination and filtering remain unknown unless preserved in a specific call site/schema/probe. No live credentials or captured cookies are copied.',('api_network','network_probe_observations'),extra='## Endpoint shards\n\n'+''.join(f'- [{x}]({x})\n' for x in end_shards)+'\n## Full machine records\n\n- [Endpoints](registries/endpoints.json)\n- [Historical HTTP probes](registries/historical-http-probes.json)\n- [Declared RPC service methods](registries/rpc-services.json)\n- [Schema fields and message types](registries/schemas.json)\n\nThe full CEAC request/response code and example trees from PREMIUM-ANALYSIS are preserved as individual [documentary findings](findings/FINDINGS_INDEX.md), not collapsed into this endpoint table.\n')
chapter('09_AUTHENTICATION_AND_SESSIONS.md','Authentication,authorization and sessions',
 'No logged-in browser/session/HAR/cookie export was available. Login/logout/registration/password-reset mechanisms and cookie/token values were not recovered as verified workflows. Generated route names and token-related schema fields are declarations only. Local entitlement patches cannot be reported as server account authorization changes. All secret-like literals and fixture handles in copied evidence were redacted; originals are unmodified.',('security',),extra='[Unavailable-source inventory](audit-metadata/unavailable-sources.json) · [Knowledge gaps](18_KNOWLEDGE_GAPS_AND_UNCERTAINTIES.md)\n')
chapter('10_FORMS_AND_BUSINESS_LOGIC.md','Forms and business logic',
 'Supported workflows are Game Review initiation,request option selection,server response presentation,local adapter compatibility,Quick Analysis and post-verification,plus the historical evaluation-bar settings. Form field markup may be present in saved HTML but no complete submission/validation flow was captured for general account forms. Do not invent required fields or endpoints from a form label.',('business_logic',))
chapter('11_DATA_MODELS_AND_RELATIONSHIPS.md','Data models and relationships',
 f'{len(SCHEMAS)}structured schema declaration records preserve rendered frontend and native descriptors separately. Field numbers,types,repetition,oneofs,enumvalues,packages and service methods are retained. These are protocol/interface models,not database schemas; optional fields need not appear in every payload. Duplicate namespaces and wire-compatible variants are not silently merged.',extra='- [Complete schema registry](registries/schemas.json)\n- [Decoded native descriptor files](registries/native-descriptors/)\n- [Detailed data-model findings](findings/FINDINGS_INDEX.md)\n\n## Curated model distinctions\n\n'+''.join('- '+fl(f['id'])+' — '+f['title']+'\n' for f in cats['data_models'] if f['id'] in CURATED)+'\nNative-interface and field-level entries are split into bounded findings files rather than repeated here.\n')
chapter('12_INFRASTRUCTURE_AND_DEPLOYMENT.md','Infrastructure and deployment',
 'Historical asset probes preserve exact URLs/status/content type/download size. Range206/onebyte must not be confused with a complete engine file. Versioned/hash package paths and production/staging/sandbox endpoints are exposed deployment evidence; provider,DNS/TLSdetails,cacheheaderpolicyanddatabasehostingwere not established.',('infrastructure',))
chapter('13_SECURITY_OBSERVATIONS.md','Passive security-related observations',
 'No exploitation,credential attack,destructive test or authorization bypass was performed by this audit. Record distinctions: extension-local CSP versus website response CSP; client entitlement flags versus server rights; native validation_hash field versus assessed cryptographic implementation; static route existence versus access authorization. No finding here is presented as a confirmed vulnerability without supporting runtime evidence.',('security',))
chapter('14_UI_AND_USER_WORKFLOWS.md','UI and user workflows',
 'The page renders native response numbers,classifications,annotations,speech hashes and arrows; the extension preserves its CEAC decode/dispatch path. User sound/UIconfirmationisdistinctfrommockbrowserorexecutableWASMtests. The progress-estimation and hidden-card sequence is preserved,including the explicit retraction of the original failure report.',('progress','evaluation_bar'),extra='See [full reference comparison](evidence/text/'+LOC['torch-human-comparison.md']['sha256']+'.md) and [native review move findings](findings/FINDINGS_INDEX.md). No cloud per-move labels have been invented.\n')
chapter('15_EXTERNAL_SERVICES_AND_DEPENDENCIES.md','External services and dependencies',
 'Every literal external URL is retained in the global registry with all source occurrences. Known source-level integrations include Turnstile,consent scripts,Sentry/analytics/ads,chess asset hosts,Vue/Pinia vendor bundles and npm/GitHub package metadata. Embedded metadata does not confer repository access or prove a service was contacted in a particular runtime session.',('external_services',),extra='[Complete URL registry](16_URL_AND_REFERENCE_INDEX.md)\n')
chapter('16_URL_AND_REFERENCE_INDEX.md','Exhaustive recovered URL/reference index',
 f'{len(U)}unique recovered references: **{st["absolute_urls"]}absolute URLs** and **{len(U)-st["absolute_urls"]}relative URL/asset references**, retaining **{sum(len(u["occurrences"]) for u in U)}source occurrences**. Deduplication preserves all contexts and source IDs. A literal is not a successful request. Relative paths are deliberately not promoted into invented full URLs; template strings remain templates. Exact supplied game URLs are retained but player handles are redacted in copied evidence.',extra=''.join(f'- [{x}]({x})\n' for x in url_shards)+'\n[Machine-readable URLs and all occurrences](audit-metadata/urls.jsonl)\n')
chapter('17_HISTORICAL_FINDINGS.md','Historical findings,failed attempts and release sequence',
 'This recovery retains old source offsets,analyzer limitations,failed probes,OOMattempts,timeouts,aborts,unpromoted sketches,and successive release/readmeversions. A trial configurationfileisnotacompletedtrial. Later discoveries supersede broad earlier conclusions without overwriting the earlier documents.',('historical',),extra='## Experiments\n\n[All per-trial records](registries/trials.json) · [Detailed experiment findings](findings/FINDINGS_INDEX.md)\n\n## Existing Markdown snapshots\n\n'+''.join('- `'+s['location']+'` — '+s['id']+'\n' for s in S if s['type']=='original_markdown')+'\n## Configuration/result consistency\n\n'+(f'{len(CONFIG_MISMATCHES)} mismatches retained in [config-result-mismatches.json](registries/config-result-mismatches.json).' if CONFIG_MISMATCHES else 'No divergence found between embedded executed trial configs and corresponding current input JSON files that exist. This does not prove every current plan entry was executed.')+'\n')
chapter('18_KNOWLEDGE_GAPS_AND_UNCERTAINTIES.md','Knowledge gaps and uncertainty register',
 'These are explicit omissions/limits,not silently assumed features. Further work is recovery/semantic review before any optional new network investigation.',extra='\n'.join('## '+g['id']+' — '+g['title']+'\n\n```json\n'+pretty(g)+'\n```\n' for g in GAPS)+'\n## Unavailable sources\n\n'+''.join('### '+g['id']+'\n\n```json\n'+pretty(g)+'\n```\n' for g in UNAVAILABLE))
chapter('19_CONTRADICTIONS_AND_DUPLICATES.md','Contradictions,version distinctions and duplicates',
 'Competing claims are preserved rather than silently harmonized. Namespaces,pipeline differences,chronology and evidence quality are stated per record. Duplicate sources are recorded by checksum in the source manifest; separate provenance remains even when evidence copies share content.',extra='\n'.join('## '+x['id']+' — '+x['title']+'\n\n```json\n'+pretty(x)+'\n```\n' for x in CONTRA)+'\n## Duplicate content groups\n\n[Source manifest](audit-metadata/source-manifest.json) retains same_content_source_ids for every checksum match,including archive-member versions. No overwritten documentation is used to reconcile conflicts.\n')
# Original-document coverage per actual Markdown source.
coverage=[]
for s in S:
 if s['type']!='original_markdown':continue
 coverage.append({'source_id':s['id'],'path':s['location'],'bytes':s['bytes'],'headings':s.get('headings',[]),'block_findings':len(s['findings']),'findings':s['findings'],'all_text_preserved_after_redaction':True,
  'original_missing_sections':'Later native human success,full experimental comparison and v0.1.9timing history are absent from older uploaded documents; newer notes remain time-bounded.','limitations':'Historical claims are not automatically independently verified. Missing cited artifacts are listed separately.'})
dump(OUT/'registries/original-document-coverage.json',coverage)
chapter('20_ORIGINAL_DOCUMENT_COVERAGE.md','Original document coverage and missing discoveries',
 'Every recovered standalone/archived Markdown content was read,privacy-redacted into a separate evidence copy,and preserved block-by-block in the ledger. No original document was edited. Archived versions are not silently replaced by the current README.',extra=table(['Source','Original path','Preserved/linked finding count'],[(x['source_id'],'`'+x['path']+'`',len(x['findings'])) for x in coverage])+'\n## Findings absent from the two uploaded foundational documents\n\n- Working local CEE review implementation and user-confirmed audio/UI.\n- Correct compact CEE classification namespace alongside legacy analysis enum.\n- Quota gate canCreate/locked,late assignments,replacement-object regressions.\n- WebSocket brand checking and actual Chrome runtime JSON/base64/offscreen lifetime issues.\n-61-configuration bounded tuning and holdout regressions.\n- Locally executable Torch human RunSearch and the limits of engine-IDdiagnosis.\n- Full21-position human-preloaded review and matched-control comparison.\n- Quick Analysis binary/legacy split and possible server Brilliantverification.\n- Conditional built-in binary debug logging and reported undefined-global failure.\n- Hidden badge v0.1.8and calibrated duration estimate v0.1.9.\n- Revisions to server-only,no-local-ratingandCAPS2causationclaims.\n\nSome of these appear in later original Markdown files; this section means absent from the two foundational uploads,not absent from every original document.\n\n[Full original-document coverage](registries/original-document-coverage.json)\n')
# Source-specific accounting for all original file types, not merely those with findings.
put(OUT/'21_COMPLETENESS_AND_QC.md','# Completeness and quality control\n\n[Master index](00_MASTER_INDEX.md)\n\n**Overall: PARTIALLY AUDITED.** All inventoried accessible file/member contents were processed and evidence/accounting preserved. Detailed semantic analysis of every remaining minified function/native algorithm is not complete; no full-websiteorcomplete-memoryclaimismade.\n\n## Actual counts\n\n'+table(['Metric','Result'],METRICS.items())+'\n## Scope distinctions\n\n- **Fully processed within the extraction scope:** original content inventory/checksums,all Markdown blocks,structured schemas,native descriptor parsing,all stored result JSONs,static route extraction,URL/reference occurrence scan.\n- **Partially audited:** larger bundles/source code beyond extracted call sites/declarations; native binaries beyond strings/descriptors/execution evidence; arbitrary HTMLworkflowsemantics.\n- **Unverifiable with available evidence:** other conversations/REA backing evidence,current authenticated flows,private backend/database,exact cloud algorithms/configuration.\n\n## QA outputs\n\n- [Machine QC report](audit-metadata/qa-report.json)\n- [Source manifest](audit-metadata/source-manifest.json)\n- [Completeness metrics](audit-metadata/completeness-metrics.json)\n- [Original file preservation snapshot](audit-metadata/original-snapshot.json)\n- [Explicit checkpoint and next steps](audit-metadata/audit-progress.md)\n\nNo new production website probes were performed. Softwaredependencyinstallationwaslimitedtoalocalprotobufparser; downloadedpackagesarenotsourcesofwebsiteclaims.\n')
# Save ledgers after all relations are finalized.
with (META/'findings-ledger.jsonl').open('w') as f:
 for x in F:f.write(json.dumps(x,ensure_ascii=False)+'\n')
with (META/'urls.jsonl').open('w') as f:
 for x in U:f.write(json.dumps(x,ensure_ascii=False)+'\n')
dump(META/'source-manifest.json',S)
# Navigation index links every generated document; data directories also indexed below.
chapters=sorted(p for p in OUT.glob('*.md') if p.name!='00_MASTER_INDEX.md')
put(OUT/'00_MASTER_INDEX.md','# Chess.com — forensic knowledge recovery and internal audit\n\n**Status: PARTIALLY AUDITED, with full source-content/structured-extraction inventory.** This is not a claim to have recovered unavailable conversations or exhaustively interpreted every native instruction/minified function. See [completeness and QC](21_COMPLETENESS_AND_QC.md). Originals are preserved. All technical claims retain provenance and verification limits.\n\n## Counts\n\n'+table(['Measure','Actual count'],[(k,METRICS[k]) for k in ['total_source_records_processed','findings_recovered','absolute_urls','relative_references','api_endpoint_declarations_or_candidates','declared_route_records','unresolved_knowledge_gaps','contradictions_or_version_distinctions']])+'\n## Chapters\n\n'+''.join(f'- [{p.name}]({p.name})\n' for p in chapters)+'\n## Granular evidence and registries\n\n- [All detailed finding files](findings/FINDINGS_INDEX.md)\n- [Machine finding ledger](audit-metadata/findings-ledger.jsonl)\n- [Source manifest](audit-metadata/source-manifest.json)\n- [Every URL occurrence](audit-metadata/urls.jsonl)\n- [Original file hashes](audit-metadata/original-snapshot.json)\n- [Conversation reconstruction,not transcript search](audit-metadata/conversation-recovery.txt)\n- [Metadata and registry file index](audit-metadata/ALL_FILES.md)\n- [Checkpoint and remaining work](audit-metadata/audit-progress.md)\n\n## How to read this corpus\n\n1. Start with the overview/scope,then use chapter/category links for semantic findings.\n2. Schema/route/URL records preserve fine-grained declarations; these are not automatically current runtime observations.\n3. Follow SRCIDs to full redacted evidence copies/checksums and FNDIDs to detailed claims.\n4. Compare claim conflicts before reusing old implementation conclusions.\n5. Consult the checkpoint before claiming completion or extending the audit.\n\n## Privacy and time provenance\n\nCopied evidence redacts fixture player handles,email/credential-like literals,session/public-ingestion-keyvalues where detected. Original files were not changed. Binary engines/modelweightsarenotduplicatedintheZIP; hashes,relevant strings and native schema interfaces preserve the audited evidence. Session date and artifact timestamps conflict; source-embedded dates are retained as historical provenance,not silently normalized into a deployment date.\n')
put(META/'audit-progress.md',f'''# Audit checkpoint and continuation instructions

## Status
PARTIALLY AUDITED. Recovery/extraction and report-generation pass completed; semantic exhaustion of all saved code/native internals is NOT complete.

## Batch 0 — initial inventory
Original pre-audit files snapshotted with SHA-256. Six loose Markdown files directly read. Archive listings inspected. No separate memory/history search tool available.

## Batch 1 — source-content recovery
{len(S)}source records processed,including913archive members and one current/condensed-conversation reconstruction. All inventoried bytes read. Textual evidence preserved after redaction/deduplication; native binaries hashed and relevant strings extracted. {len(U)}unique URL/relative references with {sum(len(u['occurrences']) for u in U)}occurrences.

## Batch 2 — original documentation
{len(coverage)}Markdown file/member records,{len(set(s['sha256'] for s in S if s['type']=='original_markdown'))}unique contents. Every nonempty body block/code/table preserved as findings with lines; sources remain unchanged. Referenced unavailable documents recorded separately.

## Batch 3 — schemas/routes/results
{len(SCHEMAS)}schema records,{len(ROUTES)}route declarations,{len(TRIALS)}unique trial records; per-ply review payloads preserved. Every native descriptor decoded. Config/result consistency checked. These are static/recorded observations,not fresh network/runtime tests.

## Batch 4 — semantic review and contradictions
{len(CURATED)}curated findings,{len(CONTRA)}claim conflicts/version distinctions,{len(GAPS)}knowledge gaps. Corrected overbroad server-only/engine-ID/CAPS2claims without editing originals. Userconfirmationandretractionkeptdistinctfromindependenttests.

## Batch 5 — ledgers and QC
All chapter documents,source/URL/route shards,detailed finding shards and machine ledgers generated. QA output records exact reference/hash checks. New downloadable ZIP is an audit product,notanextensionrelease.

## What remains
- Additional semantic batches for each large frontend bundle: enumerate function/callsite coverage rather than assuming a literal scan recovered all behavior.
- Native instruction/model semantics: not a completed decompilation,do not claim exact rating/CAPS2algorithm or all human-modeconfiguration.
- Unknown original conversation/REA/otherreferencedsources require exports; cannot retrieve through available tools.
- Authenticated workflows,header/cookie/security/backenddetails require separately authorized new evidence; no guessed completions.
- Optional future verification must be labeled new investigation and kept separate from this historical recovery.

## Reproduce/continue
Scripts are in audit-metadata/:recover.py creates inventory/evidence/URLs from the original-snapshot;build_audit.py runs structured extraction plus curated.py and render_audit.py. recover.pyisnotanewnetworkprobe. Native descriptor parser uses Python protobuf. Before rerunning,takecaretonotoverwritefuturenewauditadditions;originalfilesarestrictlyread-only.

## Evidence accounting
Every accessible source has reviewedmethod and incorporatedaccounting in source-manifest. Reviewedmeansactuallyread/scanned; semantic_reviewandlimitationsstatewherehuman-levelinterpretationisincomplete. Do not upgrade overallstatus merely because everyfilewasreadorallrequestedchapterfilesexist.
''')
# Link every new document/data/evidence file via a complete index, not a huge master page.
allfiles=sorted(str(p.relative_to(OUT)) for p in OUT.rglob('*') if p.is_file() and p.name!='ALL_FILES.md')
put(META/'ALL_FILES.md','# Complete audit output file index\n\n[Master index](../00_MASTER_INDEX.md)\n\n'+''.join('- ['+p+'](../'+p+')\n' for p in allfiles)+'\nThis index includes redacted evidence blobs and machine registries. Original engine/model binaries and original ZIP containers are hashed/indexed,not copied wholesale.\n')
print(pretty(METRICS))
