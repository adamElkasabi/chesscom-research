#!/usr/bin/env python3
"""Readability pass on NEW narrative reports only, never evidence/code/old records."""
from pathlib import Path
import sys,re,json
sys.path.insert(0,'/var/tmp/chess-forensic/tools/wordninja');import wordninja
O=Path('/var/tmp/chess-forensic/output/website-audit');metrics=json.loads((O/'audit-metadata/completeness-metrics.json').read_text())
# Preserve technical terms when segmenting concatenated lower-case narrative words.
terms=['protobuf','decompilation','decompiler','decompiled','subdomains','callee','callees','frontend','backend','workspace','runtime','callgraph','callgraphs','metadata','namespace','namespaces','bytecode','bytecodes','syscalls','syscall','toolchain','toolchains','unretrieved','unreviewed','WebAssembly']
def splitword(m):
 w=m[0];parts=re.split('('+'|'.join(sorted(terms,key=len,reverse=True))+')',w)
 out=[]
 for x in parts:
  if not x:continue
  out.append(x if x in terms else ' '.join(wordninja.split(x)))
 return ' '.join(out)
paths=list((O/'chapters').glob('*.md'))+list((O/'wasm-analysis').glob('*.md'))+list((O/'wasm-analysis/modules').glob('*/module-report.md'))
for p in paths:
 t=p.read_text();parts=re.split(r'(```.*?```|`[^`\n]*`|https?://[^\s)<>]+|\]\([^)]*\))',t,flags=re.S)
 for i in range(0,len(parts),2):parts[i]=re.sub(r'\b[a-z]{18,}\b',splitword,parts[i])
 t=''.join(parts).replace('All49kdefined','All48,089defined').replace('Noall-featurebehaviorclaim','No all-feature behavior claim')
 p.write_text(t)
# Clear, human-reviewed opening and conclusion; detailed registries/reports remain linked.
(O/'chapters/01_EXECUTIVE_OVERVIEW.md').write_text('''# Executive overview

[Master index](00_MASTER_INDEX.md)

**Overall status: PARTIALLY AUDITED.** This extends the preserved Chess.com knowledge recovery with new passive architecture evidence and dedicated offline analysis of all five locally available WASM binaries. It is not a reconstruction of unavailable private source code, a database schema dump, or a semantic explanation of every native function.

## Major architectural discoveries

1. **MySQL is supported by direct published evidence.** A March 11, 2024 Google Cloud article authored by a Chess.com principal engineer describes migration to Cloud SQL for MySQL Enterprise Plus. It also explicitly names ScyllaDB, Elasticsearch, and Redis. This establishes published technology use, not a database-to-endpoint mapping or a guarantee about every current service.
2. **PHP/Symfony are strongly indicated for the web tier.** Public PHP/Symfony job evidence is corroborated by generated route conventions and newly observed `k8s-prod-fpm-catch-all` response-pool labels. The implementation language of the separate CEAC service remains unknown.
3. **The UI uses a real shared implementation layer.** Saved bundles contain Vue/Pinia and Svelte-related compiled-runtime indicators. Four actual referenced CSS files expose a custom cc-* design system. The inventory records 367 implementation declaration variants, 1,240 CSS variable declarations, 633 distinct variable names, and 52 media-query occurrences. These are not a complete runtime component tree or all interactive states.
4. **CEE is substantive native computation, not just presentation.** Its binary interfaces and prior local executions support real search/review/classification/rating machinery. This does not establish parity with cloud engine builds, options, or scoring configuration.
5. **Native parameter types are recoverable despite misleading JavaScript arity.** The binary exports `CEE_InitWithOpts(i32,i32)->void`, `CEE_NewFeature(i32,i32,i32,i32)->i32`, and `CEE_Run(i32,i32)->i32`. JavaScript `.length === 0` was not the native ABI.
6. **WASM builds have materially different memory requirements.** CEE declares 386 MiB initial non-shared memory with a 2 GiB maximum. The Stockfish no-Worker build imports fixed 512 MiB shared memory; the single build defines 64 MiB initial non-shared memory. Torch Lite defines fixed 512 MiB non-shared memory. These are address-space declarations, not resident-memory measurements.

## What the new WASM work actually achieved

All five binaries were structurally parsed and validated. Function signatures, body offsets, imports/exports, globals, tables, element/data segments, opcode frequencies, direct-call graphs, and offset-linked string candidates were recovered. All five instantiated with explicit stub hosts under resource and capability restrictions; that is not a functional game-review test.

Full decompilation succeeded for two Stockfish modules and Torch Lite. Full CEE decompilation failed within the recorded tool/resource bounds; ten focused export-body decompilations succeeded using analysis-only typed stubs for other functions. Those derivatives are explicitly labelled and are not recovered original C++ source.

## Important incomplete areas

Additional referenced WASM versions, Rive assets, and multipart Torch references remain un-retrieved. Many functions have structural accounting but no independently reviewed semantic description. No private controllers, repositories, SQL tables/columns/indexes, ORM configuration, authenticated browser session, complete security policy, or exact cloud algorithm configuration was obtained. Inaccessible conversations and the external REA record remain unavailable.

The source and finding counts below include declarations, protocol fields, literal references, and recorded experimental outputs. They are not counts of independently verified current website features.

## Actual counts

'''+ '| Metric | Actual |\n|---|---|\n'+''.join('| '+k+' | '+str(v).replace('|','\\|')+' |\n' for k,v in metrics.items()))
# Explicitly index the file-size/retrieval distinction where a reader will not miss it.
p=O/'chapters/25_FINAL_ARCHITECTURE_ASSESSMENT.md';t=p.read_text();t+='''

## Completion statement

The architecture is reconstructed only to the boundary supported by the evidence. The database product can now be identified from primary published material, but its private schema cannot. The web tier is strongly indicated to use PHP/Symfony, but this is not proof that every backend service shares that stack. Every available local WASM binary was structurally processed; every referenced version was not retrieved, and every native function was not semantically explained.

**This remains PARTIALLY AUDITED, with important private internals UNVERIFIABLE from the available evidence.** The continuation checkpoint names the remaining batches. Do not treat the presence of all requested chapter files as full completion.
''';p.write_text(t)
