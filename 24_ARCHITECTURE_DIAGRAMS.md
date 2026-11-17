# Evidence-labelled architectural diagrams


## Focused Torch Human / bot-personality follow-up

Focused diagrams now separate configured bots, legacy/book move selection and local-vs-remote Human review. They supersede any interpretation equating these paths.

[Evidence-graded focused update](torch-human-bots-update/00_START_HERE.md) · [Overlay change manifest](TORCH_HUMAN_BOTS_PATCH_MANIFEST.md). This additive notice supersedes narrower earlier interpretations; it does not alter archived original documents.

---

[Master index](00_MASTER_INDEX.md)

Solidlinesrepresentobservedcode/datarelationships;dashed lines explicitly label inference/unknowns. LogicalmodelsarenotSQLschemas. Diagram12isasmallrevieweddirectcallslice,not a fabricated complete callgraph. Machinegraphsretainallrecoveredpairs.

## High-level website

[Mermaid source](diagrams/01-high-level.mmd)

```mermaid
flowchart TD
 Browser[Browser HTML and client packages] --> Edge[Cloudflare observed]
 Edge --> Web[PHP Symfony web tier strongly indicated]
 Browser --> WS[CEAC analysis WebSocket observed in source]
 Browser --> Worker[Local CEE or UCI Worker]
 Browser --> RPC[BrilliantVerification declared RPC]
 Web -. unmapped database ownership .-> DB[Published MySQL Cloud SQL plus other data systems]
 WS -. private implementation unknown .-> Unknown[Unknown server implementation]
```

## Frontend hierarchy boundaries

[Mermaid source](diagrams/02-frontend-components.mmd)

```mermaid
flowchart TD
 Shell[HTML shell] --> App[Page-specific app]
 App --> State[Pinia state observed]
 App --> Shared[Shared compiled components]
 Shared --> CC[cc-button cc-avatar cc-tooltip etc]
 App --> Board[Chess custom element references]
 Shared -. exact runtime parent child tree incomplete .-> Other[Other component declarations]
```

## UI to backend communication

[Mermaid source](diagrams/03-ui-backend.mmd)

```mermaid
sequenceDiagram
 participant U as Review UI
 participant J as Request builder W4e/x3e
 participant S as CEAC WebSocket
 U->>J: Review options
 J->>S: protobuf GameReviewRequest
 S-->>J: progress heartbeat waiting or success
 J-->>U: decoded native review
 Note over S: Server language and DB mapping unknown
```

## Routing and controllers

[Mermaid source](diagrams/04-routing.mmd)

```mermaid
flowchart LR
 URL[GET slash or jobs] --> E[Cloudflare response]
 E --> Match[web_index or web_jobs matched header]
 Match -. class method not available .-> C[Unknown controller]
 RT[Saved generated route declarations] -. URL generation evidence only .-> Match
```

## Service and business boundaries

[Mermaid source](diagrams/05-services.mmd)

```mermaid
flowchart LR
 UI[Client flags and request options] --> Review[CEAC review interface]
 UI --> Quick[Quick Analysis local CEE]
 Quick --> Verify[Brilliant verification RPC call site]
 Review -. private service classes unknown .-> S[Unknown services repositories jobs]
```

## Database/model boundary NOT a database ERD

[Mermaid source](diagrams/06-data-model-boundary.mmd)

```mermaid
flowchart TD
 Proto[Confirmed protobuf Game Review Move Score models] --> Fields[Wire fields and namespace enums]
 Publication[Published persistence domains] --> Systems[MySQL ScyllaDB Elasticsearch Redis]
 Fields -. no proven table column mapping .-> SQL[Unknown relational DDL]
 Systems -. no schema access .-> SQL
```

## Observed public request lifecycle

[Mermaid source](diagrams/07-request-lifecycle.mmd)

```mermaid
sequenceDiagram
 participant C as Unauthenticated client
 participant E as Cloudflare edge
 participant W as Web pool label
 participant D as Unknown downstream
 C->>E: GET / or /jobs no account cookies
 E->>W: Origin forwarding inferred
 W-->>E: HTML matched-route/pool headers observed
 E-->>C: 200 plus security/cache headers
 Note over W,D: No controller or database trace obtained
```

## Extension local review workflow

[Mermaid source](diagrams/08-workflow.mmd)

```mermaid
sequenceDiagram
 participant UI as Native page review UI
 participant Hook as Main-world WebSocket hook
 participant SW as Bridge/service worker/offscreen
 participant C as CeeClient and worker
 UI->>Hook: intercepted game-review binary request
 Hook->>SW: session-routed base64 payload
 SW->>C: local native review
 C-->>SW: actual CEE protobuf and metadata
 SW-->>Hook: CEAC-compatible response frames
 Hook-->>UI: native page decode and rendering
 Note over SW: Timing estimate is presentation only
```

## Deployment evidence

[Mermaid source](diagrams/09-deployment.mmd)

```mermaid
flowchart TD
 Internet --> CF[Cloudflare observed edge]
 CF -. header naming evidence .-> K[Kubernetes FPM-named web pool]
 Assets[Versioned hashed static assets] --> Internet
 GCP[Published Google Cloud regions] --> SQL[Cloud SQL MySQL Enterprise Plus]
 K -. service to cluster mapping unknown .-> SQL
```

## JavaScript to WASM boundary

[Mermaid source](diagrams/10-js-wasm.mmd)

```mermaid
sequenceDiagram
 participant J as CeeClient
 participant G as Emscripten worker glue
 participant M as WASM linear memory
 participant N as Native CEE exports
 J->>G: feature gamePoint id encodedRequest
 G->>M: malloc plus HEAPU8.set bytes
 G->>N: CEE_NewFeature(gamePoint,id,ptr,len)
 N-->>G: feature handle
 G->>N: async CEE_Run(handle,0)
 N->>G: imported callback(ptr,len,is_final)
 G->>M: copy subarray slice
 G-->>J: postMessage proto bytes plus is_final
```

## WASM imports and exports

[Mermaid source](diagrams/11-wasm-host.mmd)

```mermaid
flowchart LR
 JS[Emscripten glue] --> Ex[CEE exported functions]
 Ex --> Native[Native function bodies]
 Native --> Imports[env and wasi imports]
 Imports --> JS
 Native --> Mem[Declared linear memory]
 JS --> Mem
```

## Recovered direct-call slice

[Mermaid source](diagrams/12-wasm-internal.mmd)

```mermaid
flowchart TD
 A[CEE_InitWithOpts export function1666 SIMD] --> B[Internal function1664]
 C[CEE_Init] --> Other[Direct callees indexed in functions JSON]
 Async[Asyncify state globals] --> A
 B -. detailed callee semantics not fully reconstructed .-> U[Unknown initialization internals]
 Note[Complete direct-call pairs in per-module call-graph JSONL; indirect targets unresolved]
```

## Alternative data paths involving WASM

[Mermaid source](diagrams/13-data-flow.mmd)

```mermaid
flowchart TD
 UI[Frontend review UI] --> Cloud[Native full review CEAC WebSocket path]
 Cloud --> Result[GameReview protobuf]
 UI --> Local[Quick Analysis or extension local path]
 Local --> Glue[Worker protobuf buffer bridge]
 Glue --> WASM[CEE WASM]
 WASM --> Result
 Result --> Render[Numbers annotations speech and arrows]
 Local --> Verify[Optional BrilliantVerification RPC]
 Cloud -. no verified DB mapping .-> DB[Unknown internal persistence dependency]
```
