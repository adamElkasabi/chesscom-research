#!/usr/bin/env python3
from pathlib import Path
import json,gzip,collections,hashlib,re
O=Path('/var/tmp/wasm-deep/output');R=O/'reports';R.mkdir(exist_ok=True)
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False))
def doc(n,s):(R/n).write_text(s)
# Manual semantic review,restricted to exact hashes and explicitly named functions.
reviews={
1666:('MOSTLY UNDERSTOOD','initialization_options_forwarder','Forwards its two i32 values to function1664 through Asyncify resume guards. They are NOT shown to be pointer/length;1664 clamps counts and builds pools.','No CEE chess algorithm is contained in this wrapper.'),
1667:('MOSTLY UNDERSTOOD','default_initializer','Calls22950,computes clamp(result,2,9)-1,and invokes1664(1,computed).','With the initial table/static sysconf table,22950returns1 and second argument evaluates1. This is initial-state reconstruction,not a measured initialized session.'),
1664:('PARTIALLY UNDERSTOOD','initialize_runtime_and_counted_pools','Sets up stream/runtime state,queries22950,clamps one supplied count to1..min(available,8),invokes slot2000->1950,and conditionally sets another counted path through slot2002->252;initializes three global collections through1731.','Counted resource pools are evidenced. Do not rename every count as physical cores or infer review classification math.'),
22950:('MOSTLY UNDERSTOOD','positive_sysconf_84_wrapper','Host invoke_ii(slot26277,84) targets22947 in the initial table;returns the positive result,otherwise0;contains exception propagation.','sysconf attribution is convention/shape supported;JS host/table changes could change the target.'),
22947:('MOSTLY UNDERSTOOD','sysconf_style_constant_query','Unsigned key<=250 selects signed16at8679184+2*key;zero/invalid sets word18295192=28 and returns-1;negative sentinels use a switch including1,0,limits,and function154.','Key84 reads-249(lowbyte7)and follows the constant1 case. Error code28 is not reinterpreted as a specific POSIX name without target ABI proof.'),
1670:('MOSTLY UNDERSTOOD','locked_integer_key_hash_lookup','Locks/context-enters base+4,uses bucket count atbase+32 and bucket pointer atbase+28;uses key&(count-1)for power-of-two counts and key%countotherwise;walks chained nodes while bucket/keymatch;copies object/controlblock pair and increments referencecount,or writes a zero pair;unlocks.','Looks like a C++unordered-map/shared-pointer pattern. Exact source container typedef and all concurrency guarantees not recovered.'),
1671:('PARTIALLY UNDERSTOOD','locked_integer_key_hash_erase','Uses the same bucket/key selection and chained-node walk as1670,then invokes unlink helper1672 and referencecount/destructor cleanup.','Cleanup/destructor helper semantics not fully reconstructed.'),
1741:('MOSTLY UNDERSTOOD','decode_composite_game_handle','Splits input into signed highpart(handle>>20)and low20bits(handle&1048575);looks up highpart in collection12157984 via1670;on success follows7890and8691 using lowpart;releases temporary shared ownership and returns selected pointer/null.','High/low split is exact. The logical meaning of highpart beyond container identity and lowpart beyond subentry selection remains inferred.'),
1686:('PARTIALLY UNDERSTOOD','create_feature_body_candidate','Reached from CEE_NewFeature via literal slot2038. Resolves game handle via1741,uses feature-ID dispatch/factory1984 and descriptor/name helper1687,contains a message-parse failure path with exact string Unable to parse feature message,allocates184bytes and calls1961,then inserts into global12157936 via1688 and returns a handle.','The entire31,638byte1984factory,feature-specific parser schemas and algorithms are not semantically decoded. Presence of error text does not identify a scoring formula.'),
1694:('PARTIALLY UNDERSTOOD','CEE_NewFeature_export_shell','4xi32->i32 export;Asyncify/exception guards;initial slot2038 resolves1686. JavaScript supplies game handle,featureID,inputpointer,bytecount and frees staging input after return.','Input pointer/length evidenced byJSbridge;caller free does not prove whether native code copies all bytes internally.'),
1698:('PARTIALLY UNDERSTOOD','run_feature_body_candidate','Reached from CEE_Run via slot2052. Looks up handle in global12157936 through slot2043->1670;contains Invalid Feature handle error path;uses object/vtable/host-mediated work dispatch and cleanup.','Feature-internal search/classification and callback scheduling still unresolved. Not an engine-parity proof.'),
1699:('PARTIALLY UNDERSTOOD','CEE_Run_export_shell','2xi32->i32 export with Asyncify/exception shell;initial slot2052 resolves1698. JSccallpasses(handle,0)withasync:true;JSreports failure forretval<=0.','Native return value is not a completed score payload;completion/data are separate bridge channels.'),
1697:('PARTIALLY UNDERSTOOD','CEE_DisposeFeature_export_shell','i32->void export;initial literal slot2041targets1671. Matches feature-handle removal from the same map family used during Run.','Referencecounts/destructors mean removal is not assumed equivalent to a single free.'),
1731:('PARTIALLY UNDERSTOOD','initialize_global_collections','Initializes/locks/unlocks collections at12157936,12157984,13074148 through1674,22864,1732,22279.','Exact collection ownership/payload mapping beyond feature/game usage remains partial.'),
1950:('PARTIALLY UNDERSTOOD','allocate_counted_runtime_pool','Clamps supplied nonnegative count against22950;loops allocating44byte objects and appending pointers in global vector-like12158908/12158912/12158916;sets up further8byte task/thread-related objects and thread constructor failure path.','These are structural object sizes,not invented source struct definitions or evidence that WASMshared-memorythreads are enabled.'),
1984:('STRUCTURALLY ANALYZED','feature_factory_or_descriptor_dispatch_candidate','31,638byte function reached from NewFeature through slot2027. Large static/lazy initialization and indirect object construction are preserved in selected decompilation.','Not promoted to a parsed feature-ID registry. Most feature-specific business logic remains unread.'),
}
overlays=[]
for idx,(status,name,ev,lim) in reviews.items():overlays.append({'function_id':'module-002.function_'+str(idx).zfill(6),'binary_sha256':'b94aaeec32ee0458aeba42a9d431a15f37c16740c030868c691c0697b3203373','function_index':idx,'inferred_name':name,'inferred_name_is_original':False,'analysis_status':status,'semantic_evidence':ev,'limitations':lim,'raw_evidence':['deep-functions/module-002/structure.json','deep-functions/module-002/functions-enriched.jsonl','cee-connected-slice/selected-implementations.txt','deep-functions/module-002/indirect-dispatch-sites.jsonl']})
p=O/'deep-functions/module-002/functions-enriched.jsonl.gz';rows=[]
with gzip.open(p,'rt') as f:
 for l in f:
  row=json.loads(l);review=next((r for r in overlays if r['function_index']==row['index']),None)
  if review:row.update({k:review[k] for k in ['inferred_name','analysis_status','semantic_evidence']});row['semantic_limitations']=review['limitations'];row['semantic_review_record']='semantic-function-reviews.json#'+row['function_id']
  rows.append(row)
with gzip.open(p,'wt',compresslevel=9) as f:
 for row in rows:f.write(json.dumps(row)+'\n')
# Every capability-probe body is small enough to state exact effect,without pretending it is chess logic.
for mid in ['new-binary-027','new-binary-028','new-binary-029','new-binary-030']:
 p=O/'deep-functions'/mid/'functions-enriched.jsonl.gz';rr=[]
 with gzip.open(p,'rt') as f:
  for l in f:
   r=json.loads(l);r['analysis_status']='UNDERSTOOD';r['inferred_name']='capability_probe_'+str(r['index']);r['semantic_evidence']='Exact small capability-probe body: '+str(r['opcodes'])+'. This module is validated for support,not executed as chess logic.';rr.append(r)
 with gzip.open(p,'wt',compresslevel=9) as f:
  for r in rr:f.write(json.dumps(r)+'\n')
# Final authoritative aggregate is reconciled from final per-function records,not old progress logs.
summaries=[]
for p in sorted((O/'deep-functions').iterdir()):
 if not (p/'summary.json').exists():continue
 s=json.loads((p/'summary.json').read_text());counts=collections.Counter()
 with gzip.open(p/'functions-enriched.jsonl.gz','rt') as f:
  for l in f:counts[json.loads(l)['analysis_status']]+=1
 s['function_statuses']=dict(counts);dump(p/'summary.json',s);summaries.append(s)
dump(O/'analysis-summary.json',summaries);dump(O/'semantic-function-reviews.json',overlays)
S=sum((collections.Counter(x['function_statuses']) for x in summaries),collections.Counter());N=sum(x['defined_functions'] for x in summaries);INS=sum(x['instruction_count'] for x in summaries)
doc('00-START-HERE.md',f'''# Deep WebAssembly follow-up — PARTIALLY AUDITED

## What was actually achieved

- **29 distinct core-module hashes:**25downloaded/assembled runtime modules(including the original5),plus4inline/constructed capability probes.25network modules are NOT29chess engines.
- **{N:,}defined functions;{INS:,}decoded instructions.** Every defined function has an explicit status. All bodies decoded to their declared boundaries;zero decode errors. All29modules passedV8`WebAssembly.validate`;validation is not execution or source recovery.
- The original48,089defined functions remain covered under the original5module IDs. Added177,246defined functions belong to additional module identities,not function aliases.
- Direct callsites,callers/callees,SCCs,export reachability,initial tables,type-filtered indirect candidate pools,and host-mediated`invoke_*`dispatch evidence are included.
- A connected46functionCEEanalysis derivative preserves29selected direct callsites and original selected function bodies except index remapping. It passed nativeWABTvalidation/WAT/decompilation. This derivative is explicitly nonfunctional:unselected functions remain boundaries and data are placeholders.
- 45source-map source contents recovered from2Rive maps,including realTypeScript loader logic.2NNUEparameterpayloads retrieved completely and hashed;their headers independently identify nnue-pytorch training provenance.

## This is NOT the requested exhaustive semantic reconstruction

The great majority of functions remain **STRUCTURALLY ANALYZED**,not understood. The fullCEEfeature factory,all important transitive business callees,Torchsearch/evaluation algorithms,weight tensors,all schema fields,dynamic dispatch fixed points,and all potential public build generations have NOTbeen reconstructed. No reviewaccuracy/rating/classification parity is established. Public references do not prove current production execution.

Final status counts:

|Status|Defined functions|
|---|---:|
'''+''.join(f'|{k}|{v:,}|\n' for k,v in S.items())+'''
`UNDERSTOOD`mostly counts exact empty/constant bodies and tiny probes;it must not be read as13,000business algorithms understood. `MOSTLY UNDERSTOOD`reviews are hash/index-specific,with limitations. Imported functions have a separate explicit structural-status inventory.

## Read in this order

1.[Scope and discovery](01-discovery-and-provenance.md)
2.[Modules and variants](02-modules-and-variants.md)
3.[Function coverage and dispatch](03-function-and-callgraph-method.md)
4.[CEE semantic reconstruction](04-CEE-semantic-case-studies.md)
5.[Memory and companion data](05-memory-and-companions.md)
6.[Rive source-map reconstruction](06-rive-and-dynamic-modules.md)
7.[Architecture and boundaries](07-architecture-and-reconstructability.md)
8.[Coverage gaps and continuation](08-limitations-and-next-steps.md)
9.[Evidence and packaging guide](09-evidence-and-packaging.md)

Historical chapters00–25andWASM00–12remain untouched in the enclosing audit. This additive follow-up supersedes only the specific coverage statements it explicitly updates.
''')
doc('01-discovery-and-provenance.md','''# Scope, discovery, and source identity

The baseline ZIP was integrity-verified before extraction:2,475members,100,385,944bytes,SHA256`aa4a215514161ca7f588a0dda342e36bace49ead965012e2ec0662bb4ef9321f`. All baseline member contents are preserved byte-for-byte in the replacement;ZIPcompression is changed losslessly.

The full-text loader/reference scan reads423distinct selected textual sources from the existing source manifest;it is not a claim to have OCR-reviewed every screenshot or semantically read every source. See`discovery-source-scan.json`for exact source IDs,locations,bytes,and hashes. The broader existing source/finding/archive indexes remain historical evidence.

Discovery followed historicalWASMreferences,version/default/no-simd/no-Worker/singleloaderforms,embeddedRivepackageversions,explicitprimary/fallbackURLs,multipartloaderlogic,workers,sourcemaps,companionmodelreferences,andinlineUint8Arraycore-modulemagic. ConstructedURLattemptsareseparatelyqualified;nohistoryoffivebinarieswaspromotedtocompleteness.

Identity tiers:
1.`binary-inventory.json`:unique complete modules by cryptographic hash.
2.`retrieval-log.json`:37binary/referenceGETattempts,includingaliases,404s,HTMLresponses,and6Torchparts.
3.`companion-loader-retrieval.json`:24derived/declaredwrapperGETs.
4.`additional-companion-retrieval.json`:multipartwrapperand2explicitRivemaps.
5.`worker-and-glue-default-retrieval.json`:4worker-defaultand2generated-glue-defaultWASM404s.
6.`model-companion-retrieval.json`:2WDL404sand2completeNNUE200payloads.
7.`embedded-wasm-dispositions.json`:literalmodulesversusmagic-onlychecksversusdynamicbuilders.

Total74newHTTPGETrecordsacrossthe5retrievallogsabove(37+24+3+6+4). No credentials,cookies,privateAPIcredentials,signed-URLbypass,orunauthorizedtestingwereused. HTTPDate/ETag/contenttype/lastmodifiedandotherreturnedmetadataarepreservedwhereavailable;failedHTTPresponsesmayhaveonlystatus/error. No fabricatedheadersorretrievaltimestampsarefilledin.

A200HTMLGitHubpageisnotamodule. A200responsecontainingWASMmagicisstillnotacceptedifincomplete. Torchpart0wasremovedasastandalonemoduleaftervalidationidentifieditwasapart;the6orderedpartsproduceexactly74,951,979bytes,SHA256`38b70a9507d46b1f2b6f73583b7658cda514041e72beb7ae8708eb995d688b30`. Theloaderdeclares6partsandconcatenatesinnumericorder;theassembledmodulevalidates.

The`.data`propertyinJavaScriptisnotanassetpath. Broadscanoutputisretainedasleads,notpromotedtofiledependencies. `classified-companion-assets.json`filtersconcretepathlikeassetextensionsandseparatesopeningbooks,NNUE,andfrontendWDLmetadata. Hundreds of bookpathsareoptionalapplicationassets,notproveddependenciesofeverymodule.

**Scope gap:**Thisisaboundedpassivestatic/publicretrievalinvestigation,noteverypossibleChess.comversionnumberorallproductiontraffic. NoauthenticatedHAR,currentbrowsermodelrequests,OCRexhaustiveness,oras-yet-undiscovereddynamicassetcatalogisclaimed.
''')
M=json.loads((O/'module-comparison-matrix.json').read_text());I=json.loads((O/'binary-inventory.json').read_text());lines=[]
for m in M:
 b=next(x for x in I if x['binary_id']==m['binary_id']);url=(b.get('urls')or[b.get('source','inline/constructed source')])[0];f=m['actual_feature_instructions'];lines.append(f"|{m['binary_id']}|{m['bytes']:,}|{m['defined_functions']:,}|{f.get('SIMD_instructions',0):,}|{f.get('atomics_instructions',0):,}|{url}|\n")
doc('02-modules-and-variants.md','''# Module inventory and version comparison

|Binary ID|Bytes|Defined functions|SIMD instructions|Atomic instructions|FirstURL/source|
|---|---:|---:|---:|---:|---|
'''+''.join(lines)+'''
See`binary-inventory.json`forfullSHA256andallobservedURLaliases;`module-comparison-matrix.json`forsectionhashes/types/features/memory/tags/data/globals/start/customsections. OriginalmoduleIDs001–005areunchanged. ThegapID024isintentional:itwasanincompletemultipartlead,notacompletemodule.

Hash-provedaliases:legacygenericCEEvendorURLmatchesbaseline1.130.285default(module002);staffvendormatches1.130.254default(new016). Othermoduleidentitiesremainseparate.

No2ofthese29moduleshaveanidenticalrawCode-sectionpayloadhash. Similarfunctioncounts,exportnames,andType-sectionhashesdonotjustifymerging. TherawData-sectionpayloadhashmatcheswithineachRivemain/fallbackversionpair,whilecodehashesdiffer. Thisisconsistentwithcode-targetvariationbutdoesnotprovethatallothersectionsorbehaviorareidentical.

TorchLite-singlebaseline005andassembledTorchsingle026haveidenticalType-andExport-sectionpayloadhashes,butdistinctCode/Data/wholemodulehashesandverydifferentfilesizes. Thisisnotproofofidenticalalgorithms,weights,version,orconfiguration. Similarlytorch-lite013andtorch014shareType/ExportpayloadsbutnotCodepayloads.

AllarecoreWASMv1,notComponentModelbinaries. Nativeexceptiontagsection13inCEEpd015containsoneattribut e0tagwithtype0;theinitialparserdidnotconsumethissectionandwascorrected. Finalsectionremainderinventoryisempty. NoGC-instructionencounterwasignored;allencounteredinstructionswereconsumed.TheanalyzerwouldexplicitlyrejectunsupportedGCimmediates.

Compiler/toolchainmetadataisnotinventedfromfilename. Emscriptenisstronglyevidencedbyactualglue/import/exportconventions. NoRustsource/type/layoutreconstructionisclaimedinabsenceofRustspecificdebug/producer evidence.
'''.replace('attribut e','attribute'))
doc('03-function-and-callgraph-method.md',f'''# Per-function coverage, dispatch, and analysis method

Thefunctionrecordscover{N:,}definedfunctionsand{INS:,}decodedinstructions. Eachhasmodule-qualifiedneutralID,exactindex,type/signature,locals,bodyoffset/size,instruction/opcodecounts,directcallers/callees,initial-tablemembership,exports,globals,memory/tableoperations,integerconstants,selectedstaticstringreferences,andstatus/evidence. Fullfloat/vectorimmediatesarenotallmaterializedinthesummaryrecords;originalbinariesorhashcheckedretrievalareneededforarbitraryfullinstructionregeneration. SelectedCEEoriginalinstructionsarealsoavailableintheWATderivativewithmanifestindexmapping.

Filesinsideeach`deep-functions/<binary-id>/`:
- `structure.json`:types/imports/exports/tables/memories/globals/start/elements/code/data/custom/datacount/tags.
- `functions-enriched.jsonl`:allfinaldefinedfunctionrecords.
- `import-function-statuses.json`:allimportedfunctionboundarieswithexplicitstructuralstatus.
- `direct-call-sites.jsonl`:per-instructiondirectedgeswithoriginalbyteoffset.
- `indirect-dispatch-sites.jsonl`:nativecall_indirectandhostinvoke_*sites.
- `initial-table.json`,`indirect-candidate-pools.json`:initialslotmapping/typecompatiblecandidatepools.
- `direct-strongly-connected-components.json`,`export-reachability.json`.
- `memory-data-map.json`,`table-reference-mutation-ledger.json`,`opcode-features.json`,`string-crossreferences.json`,`relevant-data-strings.json`.
- `validation.json`,`decode-errors.json`,`summary.json`.

InthisZIP,theJSONLmembersarestoredasplaintextcompressedbyZIPLZMA,ratherthannestedgzip. Scratchanalysisscriptsuse`.jsonl.gz`;thisisonlyapackagingtransformation,notdataomission.

## The important CEE correction

Baseline002CEE_Init(function1667)has33direct-reachablenodesbut1,229nodesafteraddingidentifiedinitial-tabletargetsfromnativeandhost-mediateddispatch. CEE_NewFeature:89->483;CEE_Run:92->509. Thesearecandidateaugmentedcounts,NOTasoundcompleteorexactdynamicgraph.

Theactualgluehas`invoke_ii:function(index,a1){{...return dynCall_ii(index,a1)...}}`,withstackrestore/EmscriptenEHhandling. Thefirstargumentreallyisafunctionslot;theABIisnotinferredonlyfromanimportname. TheimportwrapperitselfandtheinternaldynCalltrampolineareadditionalboundaries;thegraphshortcutmodelsaconditionalpossiblecallee,notexecutioncount.

Abstractionlimits:straightlineconstant/locals/arithmeticandinitialstaticmemoryreadsaretracked. Controlflowandmemorywritesclearabstractstate. ThereisnofullCFGfixedpoint,aliasanalysis,pathfeasibility,orcontext-sensitiveinterproceduraldataflow. Initial-memoryreadsmaybestaleafterruntimewrites. ExternaltablemutationandJS`addFunction`/Table.setcannotbedisprovedbynonativetable.setopcode. Typecompatiblepoolsareoverapproximationsforinitialtableonly,notclosed-worldruntimecandidateproofs. SCCsaredirectonly;indirect/hostcallsaddcycles. Anunresolvedsiteisexplicitlyretained,notcalleddeadcode.

## Decode/validator QC

WABT1.0.36opcode-tablemetadatawasusedforinstructionnames/immediateformats. InitialCEErunhad291errorsbecauseWABTspells0xC0–0xC4withuppercasehexdigits;thelookupregexwascorrectedandthebatchrerun. Finalerrors:0. AninitialnativeWABTvalidationprocesswaskilled(-9),notinterpretedasinvalidbinary. IndependentV8validationunderNode20.20.2succeededforall29moduleswithoutinstantiatingorexecutingthetargetmodule.

The46functionCEEconnectedderivativealsoindependentlypassednativeWABTvalidation,WATprinting,anddecompilation. Itretains29directcallsbetweenselectedrealbodies. Host/indirecttargetsstillcrossboundariesunlessreadmanuallyagainstevidencedslotmaps. Derivativedataareemptyplaceholders;**neverexecutethisderivativeasanengine**.

AutomaticUNDERSTOODstatusesapplyonlytoexactempty/constantbodiesorindividuallyreviewedtinyprobes. ForwardersarePARTIALLYUNDERSTOODbecausecalleeffectsremainunknown. Semanticreviewsareseparatefromrawevidencein`semantic-function-reviews.json`andareappliedtothefinalfunctionrecords.
''')
doc('04-CEE-semantic-case-studies.md','''# CEE semantic reconstruction — hash-specific, bounded

AllfunctionindicesinthischapterreferONLYtomodule002,SHA256`b94aaeec32ee0458aeba42a9d431a15f37c16740c030868c691c0697b3203373`. Theyarenotassumedstableacrossversions/no-SIMDbuilds. Originalsymbolsarestatedonlyforexports;othernamesareinferredandqualified. Evidence:`semantic-function-reviews.json`,`cee-connected-slice/slice-manifest.json`,`selected-implementations.txt`,andtheoriginalmodule'sfunction/table/memorymaps.

## 1. Initialization options are not established pointer/length

`CEE_InitWithOpts`1666takes2i32andforwardsboth to1664withAsyncifyguards. In1664,normal-flowvaluesareclampedandpassedto count-consumingresourceinitializers. TheearlierABIplaceholder“ptr/lenprobable”isNOTsupportedbythisnewcalleeinspectionandissuperseded.

`CEE_Init`1667normal-flowpseudocode:

```text
available = fn22950()
second = clamp(available, 2, 9) - 1
fn1664(1, second)
```

`fn22950`normal-flowpseudocode:

```text
x = host_invoke_ii(slot=26277, argument=84)
# initial table[26277] = function22947
if no_exception: return max_signed(x, 0)
propagate_exception()
```

`fn22947`is asysconf-stylequerywithstatic16bitsentineltableandswitch. At8679184+2*84,theoriginalstaticbytesare`07ff`=-249. Thecorrespondingswitchcase returns1. Thusunderthestaticinitialtable/data,defaultCEE_Initinvokes1664(1,1). Thisisnotameasuredruntimeconfigurationanddoesnotproveabrowserwilluseonephysicalcore;host/table/memorychangescanmatter.

`fn1664`createsstream/runtimecontext,clampsatleastonecountto1..min(available,8),callsinitialslot2000->1950,andconditionallyanothercountedpathslot2002->252. Itinitializesthreeglobalcollectionsusing1731. `fn1950`allocates44byteobjectsandappendsintoavectorlikeglobalregion12158908/12158912/12158916;itcontainsadditionaltask/thread-relatedconstruction. Callingthesearguments“counts”isbettergroundedthanpointer/length;exactuserfacingoptionnamesremainunknown.

**Status:**1666/1667MOSTLYUNDERSTOOD;1664/1950PARTIALLYUNDERSTOOD. ErrorsincludeEmscriptenexceptionflaghandlingandcleanup,notjustnormal-flowarithmetic.

## 2. Composite game handles have an actual bit layout

NewFeature'scandidatebody1686callsinitialslot2026->1741. `fn1741`:

```text
high = arithmetic_shift_right_i32(handle, 20)
low = handle & 0x000fffff
pair = locked_lookup(global_collection_12157984, high)  # fn1670
if pair.object == null:
    result = null
else:
    base = fn7890(pair.object)
    result = fn8691(base, low)
release_temporary_shared_ownership(pair.control_block)
return result
```

The20bitsplitisexact. Itisevidencethatthepublicgamehandleisnotnecessarilyarawlinear-memorypointer. “highcollectionkey/lowsubentry”isaboundedinference;noinventedgenerationcounterorboardlayoutisassigned. Shared-controlblockcleanuphasvtable-mediateddestructorsandallocatorboundaries.

**Status:**1741MOSTLYUNDERSTOODwith7890/8691stillboundaries.

## 3. The handle map lookup is a reconstructable algorithm

`fn1670(out, container, key)`normal-flowpseudocode:

```text
enter_or_lock(container + 4)
count = load_u32(container + 32)
buckets = load_pointer(container + 28)
if count == 0 or load_u32(container + 40) == 0: return_zero_pair_and_unlock()
if popcount(count) <= 1:
    bucket = key & (count - 1)
else:
    bucket = key if key < count else key % count
node = first_chain_node(buckets[bucket])
while node != null and bucket_of(node.hash, count) == bucket:
    if node.hash == key and node.key == key:
        out.object = node.value_object       # observed node +12
        out.control = node.value_control     # observed node +16
        if out.control: increment_reference_count(out.control + 4)
        unlock_and_return()
    node = node.next
out.object = 0
out.control = 0
unlock_and_return()
```

Offsetsareobserved32bitlayoutforTHISbuild,notanassertionofuniversalC++standard-libraryABI. Thepower-of-twomaskingversusmodulobucketingandchainedlookupareactualalgorithmevidence. Lock/unlockfunctionattributionispresumedfromentry/exitpatternandnotaconcurrencyproof. Erase1671usesthesamebucket/keywalkthen1672unlinkandreference-count/destructcleanup.

**Status:**1670MOSTLYUNDERSTOOD,1671PARTIALLYUNDERSTOOD.

## 4. NewFeature is marshalling + factory + parse + registration, not one score formula

JavaScriptbridgeevidence(thebaseline`javascript-bridge-excerpt.js`andloader):

```text
bytes = jsBuffer.length * jsBuffer.BYTES_PER_ELEMENT
p = malloc(bytes)
HEAPU8.set(jsBuffer, p)
try:
    h = ccall('CEE_NewFeature', number,
              [number,number,number,number], [gameHandle,featureID,p,bytes])
    if h < 0: post error from CEE_GetLastError()
    else: post handle h
finally: if p != 0: free(p)
```

ThisprovesJSstagingbufferlifetime,notnativecopy/retainbehaviorforallfeaturetypes. `HEAPU8.set`andBYTES_PER_ELEMENTmustbeinterpretedagainstactualcallers'typedarrays;wehavenotvalidatedallnon-Uint8inputcases.

Export1694isanAsyncify/exceptionshell. Initialslot2038->1686reveals:
- gamehandledecode1741;
- featureID-drivenfactory/descriptorpathslot2027->1984,withslot2028->1687name/descriptorhelper;
- inputmessageparsepathcontainingexact`Unable to parse feature message`atmemory115868;
-184byteobjectallocationandconstructor1961;
- insertionintoglobal12157936viaslot2031->1688;
- returnedhandleandexception/logformattingpaths(`exception occurred: {}; callstack: {}`and`unknown exception occurred`).

1984is31,638bytesanditsdecompiledbodyis~200KB. Itisincluded,notabandoned,butmostofitslargefactory/lazy-initializationbusinessbranchesarenotsemanticallyinterpreted. ThereisnoprovendictionarymappingallfeatureIDstoschemasoralgorithmsyet. Pseudocodeisthereforeintentionallypartial:

```text
NewFeature(gameHandle, featureID, input, length):
    game = resolve_composite_game_handle(gameHandle)
    descriptor_or_factory = factory_dispatch(featureID, game, ...unknown_details)
    name_or_error = resolve_feature_descriptor(featureID)
    parse_and_validate_input_or_report('Unable to parse feature message')
    object = construct_feature_state_in_184byte_allocation(...)
    return insert_into_feature_registry_12157936(object)
```

**Status:**1694/1686PARTIALLYUNDERSTOOD;1984STRUCTURALLYANALYZED. Noscore/rating/accuracyformulaisclaimed.

## 5. Run and disposal share a registry, not a raw pointer API

JavaScriptcalls`CEE_Run(handle,0)`throughasync`ccall`;return<=0postsanerror. Export1699initialslot2052->1698usesinitialslot2043->1670tolookupthehandleinglobal12157936. Itsfailurepathcontains`Invalid Feature handle`at114487. Laterworkusesfunction/objectdispatchandcleanup;thepayload/completioncallbacksareseparatefromtheintegerreturnstatus.

Disposal1697initialslot2041->1671erasesviaasimilarlockedmapwalkandreference-countcleanup. Destructionisnotassumedtobeasinglefree. TheJSvariable`game_point`intheDisposeFeaturewrapperdoesnotprovethenativeargumentisagamehandle;thecross-pathregistryevidenceisstrongerthanalocalvariablename.

**Status:**Run/disposalshellsandcandidatebodyPARTIALLYUNDERSTOOD. Callbackpayloadschemasandactualfeatureexecutiongraphsremainopen.

## 6. Asyncify and exception state are not chess domain state

Module002global0initializes26,691,088andactsastackpointerindecompiledframes;global2/global3areconsistentwithAsyncifystate/datapointerusage(0normal,1unwind,2rewindpatterns). Memoryword18297676isrepeatedlyset/readaroundEmscriptenEHwrappers. Thesecompiler/runtimepatternsdominatethedecompiledshellsandmustnotbemisnamedasfeatureclassificationstates.

ReadablepseudocodeaboveremovesthesecontrolbookkeepingdetailsONLYforexplanation. Rawselecteddecompilationretainsthem,andmanifestmarksthedata-lessderivativeasnon-runnable. Cleanup/exceptionpathsarepartlyunderstood,notdiscardedasequivalenttonormalflow.
''')
doc('05-memory-and-companions.md','''# Linear memory, static data, and companion resources

`memory-data-map.json`ineachmodulemapsallactive/passivesegments,lengths,hashes,binaryoffsets,initialmemoryaddresses,and48bytehexpreviews. Table/memorylimitsandshared/memory64flagscome fromstructure,notfilenames. Actualmemory.growinstructioncountsaredistinctfromhavinggrowabledeclaredlimits. Runtimeheapshapeandgrownsizewerenotmeasured.

Originalbaseline memoryfactsremain:CEE001/002initial386MiB,max2GiB,nonshared;Stockfish003fixed512MiBimportedshared;004initial64MiB/max2GiBnonshared;Torch005fixed512MiBnonshared. Allnewlimitsarelistedpermodulein`module-comparison-matrix.json`withoutassumingthatthevariantnameimpliesthreadsupport.

## Concrete CEE layouts inferred from instructions
- Compositegamehandle:highpartarithmeticshift20,low20bitmask,notnecessarilyarawpointer.
- Registrycontainer1670:bucketpointer+28,bucketcount+32,nonemptycount/state+40;nodescarrynext+0,hash+4,key+8,valueobject+12,controlblock+16.
- Temporaryshared-pair:2pointer-sized32bitwords;controlblockreferencecounterat+4inobservedcode. FullC++object/vtablelayoutandlifetimeprotocolremainincomplete.
- NewFeatureconstructorpathallocates184bytes;countedpoolpath44bytes. Theseallocationrequestsarenotproofthatalllogicalobjectfieldsareknown.
- Small-stringoptimizationpatternsusebyte+11signandpointer/lengthfields;exactsource`std::string`ABIisinferred,notrecoveredfromdebugtypes.
- JSprotobufcommandbridgeallocatesrequestbytesand8192responsebytes,callsthe4numberABI,copiestheresponsewith`.slice()`beforefreeing. Thisisobservablemarshalling,notproofthatallnativepathsrespect8192orallprotocolmessageshavebeenmapped.

## Actual external model/parameter distinctions

TwoexplicitNNUEURLswereretrievedHTTP200infull:
- `nn-ad9b42354671.nnue`:47,001,499bytes,SHA256`ad9b423546714137916bd38978af6fd68d7b8951bef25ff76bf43da72d6cb786`.
- `nn-5af11540bbfe.nnue`:40,119,326bytes,SHA256`5af11540bbfefcb54e38c5dd000cab4b469dfa7599a1d55be5d2722c20a8929b`.

BothbeginwithNNUE-layoutversion0x7af32f20andabounded75bytedescription:`Network trained with the https://github.com/glinscott/nnue-pytorch trainer.` Architecturehashesdiffer. Thisisrealparameterfileevidence;wedidnotdecodealltensorlayersorproveeveryStockfishbuild'scompatibility. Priorhistorical1byte206responsesarenotsubstitutedforthesefullretrievals.

SavedHTMLexplicitlydeclared`/bundles/web/wdl/model.json`and`group1-shard1of1.bin`;bothreturned404inthisfollow-up. TheyarefrontendWDLmodelleads,notprovedCEEorTorchimports. Already-abandonedcoach/charmendpointswerenotreprobed. Charmloadbridgeacceptsbytesandoptionalkey,butnopublicmodel/keyretrievalisbypassedandnoencryptedweightsarerecovered.

TorchlargeData-sectionsanddifferentfilesizesareevidenceofembeddedstaticpayloadvariation,notautomaticallyaPyTorch.pt/ONNXfileorcompleteexplanationofweights. Openingbooksareseparatelyclassified. JS.datafieldsarenotfilesystemassets.
''')
doc('06-rive-and-dynamic-modules.md','''# Rive: actual source recovery and a new completeness boundary

Twoexplicitpublicsource maps(`rive.js.map`)contain45`sourcesContent`entries:16for2.38.2,29for2.49.3. Extractedprivacy-scrubbedsourcesareunder`rive-recovered-sources/`;`rive-sourcemap-reconstruction.json`mapsoriginalnames,mapURL/hash,rawsource-contenthash,scrubbedhash,andspecificloaderoffsets. TheseareactualpublishedTypeScript/JSsourcecontents,notsynthesizedWASMsource.

Theloaderdefaultisapackage-versionqualifiedunpkg`rive.wasm`;fallbackisjsdelivr`rive_fallback.wasm`. `locateFile:()=>attemptedUrl`overridesgenerated`webgl2_advanced.wasm`defaults. ThusfailedGETsofthosegenerateddefaultsarenotevidenceofabrokenproductiondependency. Onprimaryfailuretheloaderclearsin-memorywasmBinary,switchestoeligiblefallback,andretries;repeatedfallbackfailureclearsloading/errorqueues. Thisisbothnetworkselectionandstate-recoverylogic.

2.49.3addsthreadedbuildselectiononlyif`threads.default`isafunction,threadURLisnonnull,hostbinaryisnotforced,andthreadsattempthasnotalreadyoccurred. Itchecks`crossOriginIsolated`,whetheraSharedArrayBuffercanbepostedtoaMessageChannel,andvalidationofthe63byteatomic/SIMDprobe. Sourcemapalsohasanignored`rive_threads.mjs`moduleentry. TheconstructedthreadURLreturned404;thisdoesnotmeanthispackageactuallyselectsthreadsinthisdeployment.

Fourdistinctsmallprobeidentitiesarenowretained:
- new027:63bytecoremodulewithsharedmemory,atomicload,andSIMDconstant;2definedfunctions.
- new028:31bytestaticSIMDprobe;1function;multipleoriginalbundleoccurrencesarealiases.
- new029:43byteSIMDv128.constmodulegeneratedbyexactliteralbuilder;1function.
- new030:64byterelaxedSIMDswizzleprobeconstructedfrom2zero-vectorconstantsandsubopcode0x100;1function.

Thesearemoduleswithoutseparate.wasmURLs. A4bytemagicconstantusedforresponseverificationisNOTamodule.

## Dynamic script-module transformations

ActualsavedSRC-1137codealsohasWASMsectionparsingandrewritingfunctions:extractingnamedcustompayloads,liftingstarttoexport`__riveLiftedStart`,movingashareddefinedmemoryintoanimport,andturningdatasegmentspassiveforworkerinitialization. Othercodecoordinatesparallelworkersandsharedcontrolblocks. ThesearelegitimatedynamicWASMtransforms,notnetworkmoduleidentitieswecanfullyenumeratewithouttheinputscriptpayloads/runtimeexecution.

The29moduleinventoryisthereforenot“allmodulesChess.comcouldeverconstruct.” Twoliteralconstructorinvocationsarefullyresolvedas029/030;arbitraryscript-dependenttransformedmodulesremainexplicitlyunresolved. Noarbitraryembeddedbinaryblobisclaimedtobeanadditionalvalidatedmodulewithoutbytes/hash/validation.

Riveisthird-partygraphics/animation/runtimeinfrastructure,notevidenceofCEEclassificationmath. ItslargefunctioncountsdoNOTrepresentnewlyunderstoodchessbusinesslogic.
''')
doc('07-architecture-and-reconstructability.md','''# Architecture, interoperation, and reconstructability

```mermaid
flowchart TD
  UI[Chess.com frontend application] --> Manager[JS engine selection and worker RPC]
  Manager --> CEE[CEE core module and Emscripten glue]
  Manager --> SF[Stockfish variants and NNUE parameters]
  Manager --> Torch[Torch variants; multipart or embedded static data]
  UI --> Rive[Rive animation and script runtime]
  Rive --> Loader[Primary/fallback loader and capability probes]
  Rive --> Dynamic[Script-dependent WASM rewriting / worker memory setup]
  CEE --> Host[invoke_* host wrappers / callbacks / async scheduler]
  Host --> Table[WASM function table and dynCall trampolines]
  Table --> CEE
  UI -. independent services; exact transaction unproved .-> Backend[Historical HTTP/RPC and server evidence]
```

InteroperationisevidencedbyJSselection/marshalling/imports,notbyassertingthatallmoduleslinkdirectly. Noprovennativecross-modulecallgraphlinksCEEfunctionindexestoStockfishorRivefunctionindices;functionindicesaremodule-local. WorkerRPCandtypedbuffersarecross-domainboundaries,notasinglecombinednativeaddressspace.

Stockfishlineageisstronglyindicatedbygluelicense/sourceattribution,UCI/NNUEinterfaces,andactualNNUEpayloads. Exactforkpatchsetandcurrentproductionconfigurationarenotfullyrecovered. TorchbrandingandmatchingexportshapesdonotidentifyopensourcePyTorchorproveequalmodels. CEEisapplication-specificexplanation/featurelogicwithsubstantialC++/Emscriptenruntime;systemlibraryhelpersmustnotbecountedasbusinesslogic. Riveisthird-partygraphics/runtime.

Existingbackendchaptersarehistorical/secondary/publicarchitectureevidenceonly. Thisfollow-updoesnotupgradeCloudSQL/MySQL/PHP/Symfonyobservationsintoprivate2026endpoints,tabledefinitions,SQLqueries,orserver-sideCEACalgorithms. BrowserWASMdoesnotrevealallbackendbehavior.

Reconstructablenow:exactimport/exportABIs,staticsectionstructures,selectedhandle/layoutalgorithms,JSstaging/copy/freeownership,loaderretry/variantlogic,andselectedrawfunctiondecompilation. Partiallyreconstructablewithmorework:CEEfeaturefactory/schema/CFGs,Torchsearch/evaluation,modeltensorformats,virtualdispatchandallocationlifetimes. Notrecoverablefromthisevidencealone:originalsourcecomments/names/typedefs,privateencryptionkeys,allruntimeinputs/backenddatabases,allunobservedbuildgenerations,orbehavioralparitywithouttests.
''')
doc('08-limitations-and-next-steps.md','''# Honest coverage ledger and continuation priorities

## Completed at the structural level
-29uniquecompletecoremodules;allV8validationssucceed.
-225,335definedfunctionrecords;zeroimmediatedecodeerrors;no finalunparsedsectionremainders.
-48,089originaldefinedfunctionindicesretained;moduleIDsunchanged.
-Types/imports/exports/code/data/elements/tables/memories/globals/start/custom/datacount/tags;actualfeatureopcodes;directgraphs/SCCs/conditionalinitialdispatch.
-URL/alias/hashdistinction;multipartassembly;workers/maps/modelleadsandfailedresultsretained.

## Partial, not satisfied exhaustively
- Semanticunderstandingofallimportantfunctions:NOTcomplete.Mostfunctionsarestillstructural.
- FullCFG/dataflowslicingforallfunctions:NOTdone. Selecteddecompilationisnotall-functionsemanticreconstruction.
- Soundindirect-dispatchfixedpoint/tablemutationmodel:NOTdone.
- Allmodelweights/tensorformats/decryption:NOTdone.
- Everypossiblepublicvariant/version/dynamicmodule:NOTestablished.
- Everycompanionpathfetched:NOTdone;hundredsofopeningbookleadsclassified,notallretrieved.
- AuthenticatedproductionbrowserHARandactualruntimecoverage:NOTavailable.
- FunctionalCEE/Torchengineparity/reviewlabels/ratings:NOTestablished.
- Fullrecoveredsource:NOTdelivered;decompileroutputandrealRivesourcemapsaredistinct.

## Most valuable next steps
1.ResolveCEE1984'sfeature-IDfactorybranchesandtheirinstantiatedtypes,thenfollowtheparseandRunworkdispatchforfeatureIDs254/285-relatedknowncallerprotocolswithoutassumingversionnumbersarefeatureIDs.
2.Reconstruct7890/8691handle-subentrylayoutand1961featureobjectfields;follow1672erase/destructorownership.
3.Useboundedmulti-functionCFG/symbolic/dataflowanalysisaroundactualselectedfeatureparsersandoutputcallbacks;mapprotobufwirefieldstoJSschemaevidence.
4.Tracktablewrites,JSdynCalltrampolines,callbacks,andmemoryaliasinginterprocedurally. Treatinitialtabletargetsonlyasconditionaluntilprovedstable.
5.Runcontrollednetwork-deniedfunctionalfixturesonlyafterhostimports/inputschemasarereconstructed;priorstubinstantiationisnotareviewtest.
6.ValidateNNUEarchitecture/size/layoutagainstexactStockfishversionsandtraceactualnetworkselection,beforeclaimingmodelcompatibility.
7.CaptureauthorizedruntimeassetselectiontoresolveWDL/Charm/TorchmodelconfigandRivescript-derivedmodules.Noauth/keybypass.

Thisdeliveryisausefuladditiveinvestigationcheckpoint,notaconcealedclaimthatth eextreme-depthmissionhasbeenfullysatisfied.
'''.replace('th e','the'))
doc('09-evidence-and-packaging.md','''# Evidence, packaging, and reproduction

TheoldbaselineZIPiskeptuntilreplacementQCpasses;thenitisreplacedatomicallyatthecanonical`website-complete-forensic-audit.zip`path. Everybaseline membercontentremainsunchanged;thehistoricalmemberhashesareindependentlycheckedagainsttheoldZIP. Existingrestoremapand`restore-workspace.py`remainvalidbecausecanonicalfilenameandbaselinepathsarepreserved.

ZIPuses**ZIPLZMA(method14)**losslesscompressiontokeepwithintheworkspacepersistencebudget. Python3`zipfile`and7-Zipsupportthis;somebuilt-inunzipviewersdonot. JSONLfilecontentisnotgzip-nestedintheZIP;itcanbestreamedwith`zipfile.open`. Allnewreport/evidence/toolmembersarelistedandhashedinthefollow-upmanifest.

Largepubliclyretrievednewmodule/modelpayloadsmaybenotembeddedduetothe128MiBworkspacepersistencecap. **See`packaging-retention.json`foranevery-payloadinclusion/exclusiondecision,exactURL/bytes/hash,andreason.** Originalfivebaselinebinariesandalloriginalbaseline membersremainembedded. Inlineprobesareembedded. Newstructural/semanticrecords,provenance,andboundedsourceexcerptsareincluded. Absenceofnewrawpayloadsisanexplicitdeliverylimitation,notfailedretrievalorpretendedpreservation.

`retrieve-evidence.py`canrestoreexcludedcompletepublicpayloadsonadownloadedlocalcopyusingexactURLandSHA256checks;mutableupstreamURLsarenotguaranteedto remainavailableorunchanged. Noauthbypassisused. ForthemultipartTorchmodule,theordered6URLsareverifiedindividuallythenconcatenatedandthefinalhashchecked. Newrawbinaryrestorationisnotautomaticinsidethecappedworkspace.

Privacy:source-map/gluepublictextisscrubbedforemailandobviousbearercredentialswithrawacquisitionhashpreserved. NNUEweightsarenotrenderedaspersonaldata. Originalbaselineprivacydecisionsarepreserved,notretroactivelychanged. Byteoffsetsofthescrubbedsourcecontentsarenotclaimedtobeunalteredrawsourceoffsetsunlesshashesmatch. Thisisapattern-basedprivacyreview,notproofthatallpossiblePIIstylesareabsent.

Rerunnableanalysis scripts are included under`tools/`. They retain scratch-pathdefaultsfromthisexecution;setuppathsandoriginalWABTtoolsareexplainedintheirsource. Scriptsareevidenceofthemethod,notaclaimofaone-commandfullyportabletoolchaininstallation.
''')
# Stable source/finding indexing adds records without rewriting original IDs.
findings=[]
claims=[('29unique core-module identities,including4inlineprobes','binary-inventory.json','HIGH'),('225335definedfunctionsdecodedwithzeroerrors;V8validation29/29','analysis-summary.json','HIGH'),('CEE_InitWithOptspointer/lengthguesssupersededbycountclampingcalleevidence','semantic-function-reviews.json','HIGH'),('CEE_Initdirect33versusinitialdispatchaugmented1229','deep-functions/module-002/export-reachability.json','HIGH:conditional-static-model'),('Gamehandleshaveexacthigh/low20bitsplit','cee-connected-slice/1741.txt','HIGH:exact-build'),('2completeNNUEparameterpayloadsdownloaded;notWASMmodules','nnue-companion-signatures.json','HIGH'),('45publishedsource-map sourcecontentsrecovered','rive-sourcemap-reconstruction.json','HIGH'),('DynamicRiveWASMrewritingprecludesunqualifiedstaticmodulecompleteness','embedded-wasm-dispositions.json','HIGH:codepresent;runtimecoverageunknown')]
for i,(c,e,confidence) in enumerate(claims,1):findings.append({'finding_id':'WDEEP-F-'+str(i).zfill(4),'claim':c,'evidence':e,'confidence':confidence,'status':'Observed/bounded inference;see linked report for limitations'})
dump(O/'follow-up-findings-index.json',findings)
reconcile=[]
for mid in ['module-001','module-002','module-003','module-004','module-005']:
 old=json.loads((Path('/var/tmp/wasm-deep/input/website-audit/wasm-analysis/modules')/mid/'structure.json').read_text());new=json.loads((O/'deep-functions'/mid/'structure.json').read_text());assert old['sha256']==new['sha256'];assert[(x['index'],x['body_offset'],x['body_bytes'],x['signature'])for x in old['functions']]==[(x['index'],x['body_offset'],x['body_bytes'],x['signature'])for x in new['functions']];reconcile.append({'baseline_module_id':mid,'sha256_unchanged':True,'every_defined_index_body_offset_size_signature_unchanged':True,'defined_functions':len(new['functions'])})
dump(O/'baseline-function-reconciliation.json',{'modules':reconcile,'baseline_defined_total':sum(x['defined_functions']for x in reconcile),'new_defined_total':N,'baseline_members_unchanged':'Verified again at final ZIP QC;see final-qc.json'})
print('REPORTS',len(list(R.iterdir())),'functions',N,'instructions',INS,'statuses',S)
