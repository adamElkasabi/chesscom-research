# Audit checkpoint and continuation instructions

## Status
PARTIALLY AUDITED. Recovery/extraction and report-generation pass completed; semantic exhaustion of all saved code/native internals is NOT complete.

## Batch 0 — initial inventory
Original pre-audit files snapshotted with SHA-256. Six loose Markdown files directly read. Archive listings inspected. No separate memory/history search tool available.

## Batch 1 — source-content recovery
2049source records processed,including913archive members and one current/condensed-conversation reconstruction. All inventoried bytes read. Textual evidence preserved after redaction/deduplication; native binaries hashed and relevant strings extracted. 1925unique URL/relative references with 8487occurrences.

## Batch 2 — original documentation
10Markdown file/member records,8unique contents. Every nonempty body block/code/table preserved as findings with lines; sources remain unchanged. Referenced unavailable documents recorded separately.

## Batch 3 — schemas/routes/results
17254schema records,321route declarations,83unique trial records; per-ply review payloads preserved. Every native descriptor decoded. Config/result consistency checked. These are static/recorded observations,not fresh network/runtime tests.

## Batch 4 — semantic review and contradictions
200curated findings,13claim conflicts/version distinctions,16knowledge gaps. Corrected overbroad server-only/engine-ID/CAPS2claims without editing originals. Userconfirmationandretractionkeptdistinctfromindependenttests.

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

## Final machine QC

1135original file hashes unchanged; 913archive member hashes matched; source/finding/URL IDs and generated links validated. All recovered Markdown body lines accounted for. Defined redaction patterns returned no residual hits in distributed text. See qa-report.json for exact checks and non-guarantees. Overall audit remains PARTIAL.
