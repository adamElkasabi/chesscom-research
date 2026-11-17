# Knowledge gaps and uncertainty register

[Master index](00_MASTER_INDEX.md)

These are explicit omissions/limits,not silently assumed features. Further work is recovery/semantic review before any optional new network investigation.

## GAP-001 — Unavailable independent conversation history

```json
{
  "id": "GAP-001",
  "title": "Unavailable independent conversation history",
  "what_is_missing": "No other conversation archive,search API,or persistent-memory index exposed.",
  "why_it_matters": "Cannot reconstruct omitted turns or all prior tool results.",
  "sources_checked": [
    "accessible-conversation/current-and-condensed-history"
  ],
  "resolvable_with_available_sources": "No",
  "additional_evidence_needed": "User export of other conversations/tool transcripts."
}
```

## GAP-002 — Expected documentation count does not match recovered files

```json
{
  "id": "GAP-002",
  "title": "Expected documentation count does not match recovered files",
  "what_is_missing": "Six loose Markdown originals and four archived variants,not approximatelyadozenuniqueinvestigationdocuments.",
  "why_it_matters": "Some cited documents may be missing.",
  "sources_checked": [
    "uploads/REVERSE-ENGINEERING.md",
    "uploads/PREMIUM-ANALYSIS.md",
    "extension/README.md"
  ],
  "resolvable_with_available_sources": "Partly: recovered all inventoried MD content",
  "additional_evidence_needed": "Provide CLIENT-SIDE.md,REDOWNLOAD.md,and other original documents or archives."
}
```

## GAP-003 — External REA evidence unavailable

```json
{
  "id": "GAP-003",
  "title": "External REA evidence unavailable",
  "what_is_missing": "Backing evidence bundle and individual2355findings inaccessible.",
  "why_it_matters": "Quoted static analyzer metrics and unresolved semantics cannot be audited directly.",
  "sources_checked": [
    "uploads/REVERSE-ENGINEERING.md",
    "uploads/PREMIUM-ANALYSIS.md"
  ],
  "resolvable_with_available_sources": "No",
  "additional_evidence_needed": "Original REA evidence export/repository."
}
```

## GAP-004 — Minified frontend semantic coverage

```json
{
  "id": "GAP-004",
  "title": "Minified frontend semantic coverage",
  "what_is_missing": "All saved bundles fully scanned for literals/routes/references; not every function and branch independently semantically interpreted.",
  "why_it_matters": "Regex/declaration extraction cannot establish all business logic.",
  "sources_checked": [
    "research/shared.eager.BOGLllgUUR.chunk.js",
    "research/refinement/live-chunks/client.e0da4c65.BIjoPk3wAJ.chunk.js",
    "research/analysis.js"
  ],
  "resolvable_with_available_sources": "Partly; requires additional bounded semantic batches",
  "additional_evidence_needed": "AST extraction/de-minification and reviewed call-graph analysis per remaining module."
}
```

## GAP-005 — Native algorithm internals

```json
{
  "id": "GAP-005",
  "title": "Native algorithm internals",
  "what_is_missing": "Full WASM instruction semantics,model weights and exact rating/accuracy algorithms not recovered.",
  "why_it_matters": "Local execution outcomes do not reveal every algorithm or cloud configuration.",
  "sources_checked": [
    "extension/engines/cee/explanation-engine.wasm"
  ],
  "resolvable_with_available_sources": "Partly; major additional reverse engineering needed",
  "additional_evidence_needed": "Native source/debugsymbols or bounded disassembly/native function mapping."
}
```

## GAP-006 — Authenticated browser runtime

```json
{
  "id": "GAP-006",
  "title": "Authenticated browser runtime",
  "what_is_missing": "No logged-in website profile,DevTools network capture,cookies or session trace available.",
  "why_it_matters": "Cannot verify account-specific routing,real cloud requests or role behavior.",
  "sources_checked": [
    "accessible-conversation/current-and-condensed-history",
    "research/browser-pipeline-test.json"
  ],
  "resolvable_with_available_sources": "No",
  "additional_evidence_needed": "Authorized user-provided redacted HAR/WS capture and relevant runtime settings."
}
```

## GAP-007 — Complete website beyond investigation scope

```json
{
  "id": "GAP-007",
  "title": "Complete website beyond investigation scope",
  "what_is_missing": "Login,registration,passwordreset,payments,allprivatepages,andfullnavigationnot investigated.",
  "why_it_matters": "Route declarations alone do not establish workflows or access rules.",
  "sources_checked": [
    "research/shared.eager.BOGLllgUUR.chunk.js",
    "research/refinement/live-game-page.html"
  ],
  "resolvable_with_available_sources": "No without new investigation",
  "additional_evidence_needed": "Separate authorized passive browser study scoped by feature."
}
```

## GAP-008 — HTTP security headers/cookies/CORS

```json
{
  "id": "GAP-008",
  "title": "HTTP security headers/cookies/CORS",
  "what_is_missing": "No full current header,cookieattribute,CSRFtokenflow evidence.",
  "why_it_matters": "Cannot make verified security posture claims.",
  "sources_checked": [
    "research/probe-results.txt",
    "research/analysis.html"
  ],
  "resolvable_with_available_sources": "No",
  "additional_evidence_needed": "Redacted response headers and authorized session observations."
}
```

## GAP-009 — Backend/database stack

```json
{
  "id": "GAP-009",
  "title": "Backend/database stack",
  "what_is_missing": "No private server source,database schema or authenticated admin access.",
  "why_it_matters": "Frontend vendor names/routes do not establish implementation technology.",
  "sources_checked": [
    "research/shared.eager.BOGLllgUUR.chunk.js",
    "research/refinement/live-checkmate.js"
  ],
  "resolvable_with_available_sources": "No",
  "additional_evidence_needed": "Official architecture/source documentation or independently observed server evidence."
}
```

## GAP-010 — Cloud TorchHuman parity

```json
{
  "id": "GAP-010",
  "title": "Cloud TorchHuman parity",
  "what_is_missing": "Exact engine build,nodes,normalization,model availability,rating parameters and hidden options unknown.",
  "why_it_matters": "Local human mode works butaccuracy/talliesnotmatching.2100defaultmaydiffer.",
  "sources_checked": [
    "research/refinement/results/comparison-human.json"
  ],
  "resolvable_with_available_sources": "Partly; more offline experiments possible",
  "additional_evidence_needed": "Authorized cloud request/response/config trace or official parameters."
}
```

## GAP-011 — Individual reference move labels

```json
{
  "id": "GAP-011",
  "title": "Individual reference move labels",
  "what_is_missing": "Only aggregate Chess.com reference tallies known.",
  "why_it_matters": "Cannot fill Chess.com per-move comparison accurately.",
  "sources_checked": [
    "research/refinement/target.json",
    "torch-human-comparison.md"
  ],
  "resolvable_with_available_sources": "No",
  "additional_evidence_needed": "User export/screenshot/annotatedPGN with every original reference classification."
}
```

## GAP-012 — Selected coach/threat feature verification

```json
{
  "id": "GAP-012",
  "title": "Selected coach/threat feature verification",
  "what_is_missing": "Audio generally confirmed by user; selected-coach assets and threat-arrow fetch not separately verified.",
  "why_it_matters": "Cannot generalize sound success to all coaches/arrow workflows.",
  "sources_checked": [
    "accessible-conversation/current-and-condensed-history",
    "extension/README.md"
  ],
  "resolvable_with_available_sources": "Partly",
  "additional_evidence_needed": "Authorized runtime checks and preserved redacted asset/failure logs."
}
```

## GAP-013 — v0.1.9 actual device confirmation

```json
{
  "id": "GAP-013",
  "title": "v0.1.9 actual device confirmation",
  "what_is_missing": "Timing estimator unit/mocked-offscreen/native regression tests exist; no later user report or stored real device timings.",
  "why_it_matters": "Estimated progress persistence and accuracy on user device remain unconfirmed.",
  "sources_checked": [
    "extension/test/progress-test.mjs",
    "accessible-conversation/current-and-condensed-history"
  ],
  "resolvable_with_available_sources": "No",
  "additional_evidence_needed": "User completion/runtimeconsole and timing history with identifiers removed."
}
```

## GAP-014 — Unknown original log targets

```json
{
  "id": "GAP-014",
  "title": "Unknown original log targets",
  "what_is_missing": "Some repeated404callback/coachmodelURLs not in accessible summary.",
  "why_it_matters": "Cannot recover exact reference without inventing.",
  "sources_checked": [
    "accessible-conversation/current-and-condensed-history"
  ],
  "resolvable_with_available_sources": "No",
  "additional_evidence_needed": "Original network logs/tool result export."
}
```

## GAP-015 — Clock/chronology inconsistency

```json
{
  "id": "GAP-015",
  "title": "Clock/chronology inconsistency",
  "what_is_missing": "Session date,originaldocumentdates2026-11-11,andartifactlogtimes2026-11-14/15differ.",
  "why_it_matters": "Do not claim current deploy or exact observation date from mtimes.",
  "sources_checked": [
    "uploads/PREMIUM-ANALYSIS.md",
    "uploads/REVERSE-ENGINEERING.md",
    "accessible-conversation/current-and-condensed-history"
  ],
  "resolvable_with_available_sources": "No definitive mapping",
  "additional_evidence_needed": "Trusted timestamped exports/timezone provenance."
}
```

## GAP-016 — Saved input/result configuration divergence

```json
{
  "id": "GAP-016",
  "title": "Saved input/result configuration divergence",
  "what_is_missing": "1 trial records differ from current config file.",
  "why_it_matters": "Can cause false claims about which parameters produced a cached result.",
  "sources_checked": [
    "research/refinement/sweep.mjs"
  ],
  "resolvable_with_available_sources": "Yes: use embedded result.config as execution provenance",
  "additional_evidence_needed": "Freshrerunrequiredonlyifchangedconfigoutputisneeded; auditdoesnotrerun."
}
```

## Unavailable sources

### UNAV-001

```json
{
  "id": "UNAV-001",
  "source": "Other conversations / historical tool transcript exports",
  "reason": "No conversation-history retrieval mechanism or export available.",
  "references": [
    "SRC-2049"
  ]
}
```
### UNAV-002

```json
{
  "id": "UNAV-002",
  "source": "Separate persistent-memory database",
  "reason": "No memory-search tool exposed; only current supplied context exists.",
  "references": [
    "SRC-2049"
  ]
}
```
### UNAV-003

```json
{
  "id": "UNAV-003",
  "source": "Original browser profile/history/DevTools HAR and WS session",
  "reason": "No authorized profile/capture available; saved HTML is not a browser history export.",
  "references": [
    "SRC-2049"
  ]
}
```
### UNAV-004

```json
{
  "id": "UNAV-004",
  "source": "REA ev_a9a06871d585d6f7e3034afca02807f6a559738b9db111ce2259360bf479bcce",
  "reason": "Only cited in uploaded documents; external record not accessible.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
### UNAV-005

```json
{
  "id": "UNAV-005",
  "source": "CLIENT-SIDE.md",
  "reason": "Referenced historical artifact not found at that path in the complete original file inventory. Related/re-downloaded schemas or bundles may exist; they are indexed separately, not claimed identical without checksum proof.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
### UNAV-006

```json
{
  "id": "UNAV-006",
  "source": "REDOWNLOAD.md",
  "reason": "Referenced historical artifact not found at that path in the complete original file inventory. Related/re-downloaded schemas or bundles may exist; they are indexed separately, not claimed identical without checksum proof.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
### UNAV-007

```json
{
  "id": "UNAV-007",
  "source": "ALL-SCHEMAS.proto",
  "reason": "Referenced historical artifact not found at that path in the complete original file inventory. Related/re-downloaded schemas or bundles may exist; they are indexed separately, not claimed identical without checksum proof.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
### UNAV-008

```json
{
  "id": "UNAV-008",
  "source": "chesscom/evidence/app-bundle.json",
  "reason": "Referenced historical artifact not found at that path in the complete original file inventory. Related/re-downloaded schemas or bundles may exist; they are indexed separately, not claimed identical without checksum proof.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
### UNAV-009

```json
{
  "id": "UNAV-009",
  "source": "tools/ceac-dump.mjs",
  "reason": "Referenced historical artifact not found at that path in the complete original file inventory. Related/re-downloaded schemas or bundles may exist; they are indexed separately, not claimed identical without checksum proof.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
### UNAV-010

```json
{
  "id": "UNAV-010",
  "source": "tools/protoread.py",
  "reason": "Referenced historical artifact not found at that path in the complete original file inventory. Related/re-downloaded schemas or bundles may exist; they are indexed separately, not claimed identical without checksum proof.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
### UNAV-011

```json
{
  "id": "UNAV-011",
  "source": "tools/extract-client-tables.py",
  "reason": "Referenced historical artifact not found at that path in the complete original file inventory. Related/re-downloaded schemas or bundles may exist; they are indexed separately, not claimed identical without checksum proof.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
### UNAV-012

```json
{
  "id": "UNAV-012",
  "source": "crosscheck/crosscheck.py",
  "reason": "Referenced historical artifact not found at that path in the complete original file inventory. Related/re-downloaded schemas or bundles may exist; they are indexed separately, not claimed identical without checksum proof.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
### UNAV-013

```json
{
  "id": "UNAV-013",
  "source": "crosscheck/analysis_subset_pb2.py",
  "reason": "Referenced historical artifact not found at that path in the complete original file inventory. Related/re-downloaded schemas or bundles may exist; they are indexed separately, not claimed identical without checksum proof.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
### UNAV-014

```json
{
  "id": "UNAV-014",
  "source": "client/analysis-client.mjs",
  "reason": "Referenced historical artifact not found at that path in the complete original file inventory. Related/re-downloaded schemas or bundles may exist; they are indexed separately, not claimed identical without checksum proof.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
### UNAV-015

```json
{
  "id": "UNAV-015",
  "source": "chess-eval-bar/page-agent.js",
  "reason": "Referenced historical artifact not found at that path in the complete original file inventory. Related/re-downloaded schemas or bundles may exist; they are indexed separately, not claimed identical without checksum proof.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
### UNAV-016

```json
{
  "id": "UNAV-016",
  "source": "chess-eval-bar/test/logic.test.mjs",
  "reason": "Referenced historical artifact not found at that path in the complete original file inventory. Related/re-downloaded schemas or bundles may exist; they are indexed separately, not claimed identical without checksum proof.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
### UNAV-017

```json
{
  "id": "UNAV-017",
  "source": "raw/play-computer.js",
  "reason": "Referenced historical artifact not found at that path in the complete original file inventory. Related/re-downloaded schemas or bundles may exist; they are indexed separately, not claimed identical without checksum proof.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
### UNAV-018

```json
{
  "id": "UNAV-018",
  "source": "raw/shared.eager.B4_eyo3T4t.chunk.js",
  "reason": "Referenced historical artifact not found at that path in the complete original file inventory. Related/re-downloaded schemas or bundles may exist; they are indexed separately, not claimed identical without checksum proof.",
  "references": [
    "SRC-2047",
    "SRC-2048"
  ]
}
```
