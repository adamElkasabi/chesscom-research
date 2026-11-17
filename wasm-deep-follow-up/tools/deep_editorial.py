#!/usr/bin/env python3
"""Final human-readable editorial pass. Does not change binary evidence or analysis records."""
from pathlib import Path
import json,collections
O=Path('/var/tmp/wasm-deep/output');R=O/'reports'
def put(n,t):(R/n).write_text(t)
S=json.loads((O/'analysis-summary.json').read_text());counts=sum((collections.Counter(x['function_statuses'])for x in S),collections.Counter())
put('00-START-HERE.md','''# Deep WebAssembly follow-up
## Status: PARTIALLY AUDITED — not an exhaustive semantic reconstruction

### Verified coverage

- **29 distinct core-module identities:** 25 downloaded or assembled runtime modules, including the original five, plus four inline/constructed capability probes. These are **not 29 chess engines**.
- **225,335 defined functions and 70,475,093 decoded instructions.** Every defined function has an explicit status. There are zero final decode errors, and all 29 modules passed V8 validation without target execution.
- The original **48,089 defined functions** retain their module IDs, indices, body offsets, sizes, and signatures.
- Added direct callsites, callers/callees, SCCs, export reachability, initial tables, type-filtered indirect candidate pools, and host-mediated `invoke_*` dispatch evidence.
- A **46-function connected CEE analysis derivative** retains 29 direct callsites between selected real bodies. Native WABT validation, WAT printing, and decompilation succeeded. It is explicitly **not a functional engine**: unselected functions remain external boundaries and data are placeholders.
- Recovered **45 published source-map source contents** from two Rive maps. Retrieved two complete NNUE parameter payloads and checked their hashes and headers.

### What remains incomplete

Most functions are structurally analyzed, **not semantically understood**. The full CEE feature factory, important transitive business callees, Torch search/evaluation, complete schemas, model tensors, dynamic-dispatch fixed points, and every potential public build generation remain unresolved. No accuracy, rating, classification, or engine-parity claim is established.

| Final status | Defined functions |
|---|---:|
'''+''.join(f'| {k} | {v:,} |\n' for k,v in counts.items())+'''
Most `UNDERSTOOD` entries are exact empty/constant bodies and tiny probes. They are not thousands of understood business algorithms. The six `MOSTLY UNDERSTOOD` reviews are narrowly qualified, hash/index-specific findings.

### Read next

1. [Discovery and provenance](01-discovery-and-provenance.md)
2. [Module inventory and variants](02-modules-and-variants.md)
3. [Function and call-graph method](03-function-and-callgraph-method.md)
4. [CEE semantic case studies](04-CEE-semantic-case-studies.md)
5. [Memory and companion data](05-memory-and-companions.md)
6. [Rive source recovery and dynamic modules](06-rive-and-dynamic-modules.md)
7. [Architecture and reconstructability](07-architecture-and-reconstructability.md)
8. [Limitations and next steps](08-limitations-and-next-steps.md)
9. [Evidence and packaging](09-evidence-and-packaging.md)

All historical chapters and baseline member contents are preserved. This additive follow-up supersedes only the specific coverage statements it explicitly updates.

**Storage limitation:** the original five binaries remain embedded. Newly acquired large runtime binaries and NNUE payloads are not all embedded; their exact hashes, URLs, retrieval results, and derived analysis are retained. See the retention manifest and hash-verifying retrieval helper. This limitation is not represented as complete raw-evidence preservation.
''')
put('01-discovery-and-provenance.md','''# Discovery and provenance

## Verified starting point

The authoritative baseline ZIP contained 2,475 members and 100,385,944 bytes, with SHA256:

`aa4a215514161ca7f588a0dda342e36bace49ead965012e2ec0662bb4ef9321f`

It was verified before extraction. Every baseline member's contents are checked again against the replacement. Compression changes do not change member contents.

## Search coverage

The loader/reference scan fully reads 423 selected distinct textual sources from the existing manifest. `discovery-source-scan.json` records exact source IDs, locations, bytes, and hashes. This is **not** a claim to have OCR-reviewed every screenshot or semantically interpreted every source.

Discovery followed historical WASM references; default/no-SIMD/no-Worker/single variants; embedded Rive package versions; primary/fallback URLs; multipart loader logic; workers; source maps; model references; and inline `Uint8Array` modules. Constructed URL candidates are marked as such.

| Evidence log | GET records | Meaning |
|---|---:|---|
| `retrieval-log.json` | 37 | Binary/reference attempts, aliases, failures, HTML, six Torch parts |
| `companion-loader-retrieval.json` | 24 | Declared or derived wrapper URLs |
| `additional-companion-retrieval.json` | 3 | Multipart wrapper and two Rive source maps |
| `worker-and-glue-default-retrieval.json` | 6 | Four worker defaults and two generated-glue defaults; all 404 |
| `model-companion-retrieval.json` | 4 | Two WDL 404s and two complete NNUE 200 payloads |

**Total: 74 HTTP GET records across five logs.** No credentials, cookies, private keys, signed-URL bypass, or unauthorized testing were used. Returned HTTP metadata are retained where available; missing headers or timestamps are not fabricated.

## Identity rules applied

- `binary-inventory.json` is the unique complete-module inventory by SHA256.
- URL identity is separate from binary identity. Equal filenames or exports do not merge modules.
- A GitHub HTML response is not a module. A magic prefix alone is not sufficient proof of a complete module.
- Torch part zero was removed as a standalone identity. The loader declares six parts and concatenates them in numeric order. The resulting 74,951,979-byte module validates, with SHA256 `38b70a9507d46b1f2b6f73583b7658cda514041e72beb7ae8708eb995d688b30`.
- Four inline/constructed capability probes have their own exact bytes and identities. Four-byte magic-comparison constants are not modules.
- JavaScript `.data` properties are not asset paths. `classified-companion-assets.json` separates concrete NNUE parameters, opening books, frontend WDL metadata, and unresolved model/data candidates.

## Discovery boundary

This was a bounded passive/static investigation with legitimate public retrieval. It does not enumerate every imaginable version number, authenticated production request, screenshot-only reference, dynamic script payload, or unobserved asset catalog. The inventory is expanded evidence, not proof of universal completeness.
''')
# Keep generated exact per-module table, replace prose surrounding it.
p=R/'02-modules-and-variants.md';t=p.read_text();table=t[t.index('|Binary ID|'):t.index('\nSee`binary-inventory.json`')]
put(p.name,'''# Modules and version/target distinctions

'''+table+'''

The table distinguishes complete downloaded/assembled runtimes from inline/constructed probes. See `binary-inventory.json` for complete SHA256 values and aliases, and `module-comparison-matrix.json` for sections, types, memories, tags, globals, data, and actual opcode features.

### Hash-proved aliases

- The legacy generic CEE vendor URL matches baseline 1.130.285 default (`module-002`).
- The staff vendor URL matches 1.130.254 default (`new-binary-016`).
- Other identities are kept separate. ID 024 was an incomplete multipart lead, so its absence is intentional.

### Section-level comparison

No two of these 29 modules have identical raw Code-section payload hashes. Similar export names, function counts, or Type-section hashes therefore do not justify merging them.

Within each Rive version, main/fallback modules have equal raw Data-section payload hashes but different Code-section hashes. This is consistent with code-target variation; it does not prove all other sections or behavior are identical.

Baseline Torch Lite single (`005`) and assembled Torch single (`026`) share Type- and Export-section payload hashes, while their Code/Data and whole-module hashes differ. The same caution applies to `torch-lite` 013 versus `torch` 014. Matching ABI shapes do not establish equal weights, algorithms, versions, or configuration.

### Format and toolchain evidence

All are WebAssembly core v1 modules, not Component Model binaries. CEE PD (`015`) has one native exception tag, attribute 0, type 0. Its Tag section was initially unparsed, then explicitly decoded; the final remainder inventory is empty.

Emscripten attribution is grounded in actual glue/import/export conventions. Producer/debug metadata are inventoried, not invented. No Rust source/type/layout reconstruction is claimed without Rust-specific evidence. Unsupported GC immediates would be an explicit error; none were silently ignored in this dataset.
''')
put('03-function-and-callgraph-method.md','''# Function coverage and call-graph method

## Per-function records

The final records cover **225,335 defined functions** and **70,475,093 decoded instructions**. Each has a module-qualified neutral ID, exact index and signature, locals, body offset/size, instruction/opcode counts, direct callers/callees, initial-table membership, exports, globals, memory/table operations, integer constants, selected string references, and explicit analysis status/evidence.

Full float/vector immediates are not all materialized in the summary. Arbitrary full instruction regeneration requires the original binary or hash-checked retrieval. The selected CEE WAT derivative separately preserves selected original instruction bodies, with index remapping documented.

Each `deep-functions/<binary-id>/` contains:

| Artifact | Contents |
|---|---|
| `structure.json` | Sections, types, imports, exports, tables, memories, globals, start, elements, code, data, custom sections, data count, tags |
| `functions-enriched.jsonl` | Every final defined-function record |
| `import-function-statuses.json` | Every imported-function boundary and explicit structural status |
| `direct-call-sites.jsonl` | Direct edges with original instruction offsets |
| `indirect-dispatch-sites.jsonl` | Native indirect and host `invoke_*` sites |
| `initial-table.json` | Initial slot-to-function map |
| `indirect-candidate-pools.json` | Type-compatible initial candidates |
| `direct-strongly-connected-components.json` | Direct-only SCCs |
| `export-reachability.json` | Direct and conditional initial-dispatch-augmented reachability |
| `memory-data-map.json` | Data regions, offsets, hashes, globals, and limits |
| `table-reference-mutation-ledger.json` | Native table/reference operations and host-mutation caveat |
| `opcode-features.json` | Observed opcodes and actual feature use |
| String, validation, error, summary files | Evidence and QC |

JSONL files are plain text inside the ZIP, compressed with ZIPLZMA. Scratch tools use nested `.jsonl.gz`; the package removes only that outer gzip layer, not records.

## Host-mediated dispatch matters

CEE `module-002` has these reachability counts:

| Export | Direct | With identified initial-table candidate edges |
|---|---:|---:|
| `CEE_Init` | 33 | 1,229 |
| `CEE_NewFeature` | 89 | 483 |
| `CEE_Run` | 92 | 509 |

These are conditional static counts, **not an exact or sound-complete dynamic call graph**.

The actual baseline glue contains `invoke_ii:function(index,a1){...return dynCall_ii(index,a1)...}`, including stack restoration and Emscripten exception handling. This confirms that the first argument is a table slot. The graph shortcut through that host wrapper is therefore evidence-based, but it is still conditional on initial table contents.

## Analysis limits

The abstraction tracks straight-line constants, locals, arithmetic, and initial static memory reads. Control flow and memory writes clear abstract state. It is not a full CFG fixed point, alias analysis, path-feasibility engine, or context-sensitive interprocedural dataflow analysis. Initial reads can become stale after writes. JS table mutation cannot be disproved by absence of native `table.set`.

Type-filtered pools overapproximate initial table candidates only. SCCs are direct-only. Unresolved calls remain explicit and are not labeled dead code.

## Independent checks and corrected failures

An initial CEE batch produced 291 decode errors because the WABT opcode table spells `0xC0`–`0xC4` with uppercase hex digits. The lookup regex was corrected and the batch rerun: **zero final decode errors**.

An initial native WABT validation was killed with -9; this was not interpreted as binary invalidity. Independent V8 validation under Node 20.20.2 succeeded for all 29 modules, without target instantiation/execution.

The connected 46-function CEE derivative independently passed native WABT validation, WAT printing, and decompilation. It retains 29 direct callsites between selected real bodies. Unselected/host-dispatched functions remain boundaries, and original data are replaced by placeholders. **Never execute it as a reconstructed engine.**

Automatic `UNDERSTOOD` statuses are restricted to exact empty/constant bodies or individually reviewed tiny probes. Forwarders are partial because callee effects are not inferred. Manual reviews are applied only to an exact hash/index and recorded separately in `semantic-function-reviews.json`.
''')
put('04-CEE-semantic-case-studies.md','''# CEE semantic reconstruction: bounded, hash-specific case studies

All native function indices here refer **only** to `module-002`, SHA256:

`b94aaeec32ee0458aeba42a9d431a15f37c16740c030868c691c0697b3203373`

Indices are not assumed stable across builds. Non-export names below are inferred labels, not recovered source names. Raw evidence is in the connected-slice manifest/decompilation, function/table/memory records, and baseline JavaScript bridge.

## 1. Initialization options are not established pointer/length

`CEE_InitWithOpts` (1666) takes two i32 values and forwards them to 1664 behind Asyncify guards. In 1664, normal-flow values are clamped and passed to count-consuming initializers. The earlier “pointer/length probable” ABI placeholder is therefore **superseded**, not repeated as fact.

`CEE_Init` (1667), normal-flow pseudocode:

```text
available = fn22950()
second = clamp(available, 2, 9) - 1
fn1664(1, second)
```

Function 22950 calls `invoke_ii(slot=26277, argument=84)`, returns the positive result or zero, and propagates exceptions. Initial table slot 26277 targets 22947, a sysconf-style query.

The latter reads a signed 16-bit sentinel at `8679184 + 2*key`, then handles negative sentinels through a switch. At key 84 the original bytes are `07ff` = -249; the corresponding switch case returns 1. Under the original static table/data, default `CEE_Init` consequently invokes `1664(1,1)`.

This is an **initial-state reconstruction**, not a measured production configuration or proof of one physical core. The table or memory may change. Exact user-facing option names remain unknown.

Function 1664 initializes stream/runtime state, clamps at least one count to `1..min(available,8)`, calls initial slot 2000 → 1950, conditionally follows another counted path through slot 2002 → 252, and initializes three global collections through 1731. Function 1950 allocates 44-byte objects and appends pointers to vector-like globals at 12158908/12158912/12158916, followed by task/thread-related construction.

**Status:** 1666/1667/22950/22947 mostly understood with qualified boundaries; 1664/1950 partial. The runtime bookkeeping is not a chess algorithm.

## 2. Game handles have a concrete composite bit layout

NewFeature's candidate body 1686 reaches function 1741 through initial slot 2026. Its normal-flow behavior is:

```text
high = arithmetic_shift_right_i32(handle, 20)
low  = handle & 0x000fffff
pair = fn1670_lookup(global_collection_12157984, high)
if pair.object == null:
    result = null
else:
    base = fn7890(pair.object)
    result = fn8691(base, low)
release_temporary_shared_ownership(pair.control)
return result
```

The 20-bit split is exact. A public game handle is therefore not established as a raw linear-memory pointer. “High collection key / low subentry selector” is a bounded interpretation; no generation-counter meaning or board struct is invented. Functions 7890 and 8691 remain semantic boundaries.

**Status:** 1741 mostly understood.

## 3. The registry lookup is a reconstructable algorithm

Function 1670 takes an output pair, container pointer, and integer key. Normal-flow pseudocode:

```text
enter_or_lock(container + 4)
count   = load_u32(container + 32)
buckets = load_pointer(container + 28)
if count == 0 or load_u32(container + 40) == 0:
    write_zero_pair(); unlock(); return

bucket = key & (count - 1) if popcount(count) <= 1
         else key if key < count else key % count
node = first_chain_node(buckets[bucket])
while node != null and bucket_of(node.hash, count) == bucket:
    if node.hash == key and node.key == key:
        out.object  = node.value_object   # node +12
        out.control = node.value_control  # node +16
        if out.control: increment_refcount(out.control + 4)
        unlock(); return
    node = node.next
write_zero_pair()
unlock()
```

The power-of-two masking versus modulo selection and chained lookup are real algorithm evidence. Offsets describe this 32-bit build, not a universal C++ ABI. C++ unordered-map/shared-pointer attribution is supported by the pattern, but exact typedefs and concurrency guarantees are not recovered.

Function 1671 repeats the bucket/key walk, then invokes unlink helper 1672 and reference-count/destructor cleanup. Removing an entry is not assumed equivalent to one `free`.

**Status:** lookup 1670 mostly understood; erase 1671 partial.

## 4. NewFeature: marshalling, factory, parse, registration

The baseline JavaScript bridge supplies four numeric arguments:

```text
bytes = jsBuffer.length * jsBuffer.BYTES_PER_ELEMENT
p = malloc(bytes)
HEAPU8.set(jsBuffer, p)
try:
    h = ccall('CEE_NewFeature', number,
              [number,number,number,number],
              [gameHandle, featureID, p, bytes])
    post_error_if(h < 0) else post_handle(h)
finally:
    if p != 0: free(p)
```

This proves the JS staging-buffer lifetime. It does not prove every native path copies all bytes before return. Typed-array behavior must be checked against real callers; all non-Uint8 cases have not been validated.

Export 1694 is an Asyncify/exception shell. Initial slot 2038 → 1686 exposes these stages:

1. Resolve the composite game handle through 1741.
2. Enter feature-ID-driven factory/descriptor work, including slot 2027 → 1984 and slot 2028 → 1687.
3. Follow an input-message validation/parse path with the exact error text **“Unable to parse feature message”** at memory 115868.
4. Allocate 184 bytes and invoke constructor-like function 1961.
5. Insert into global registry 12157936 through slot 2031 → 1688 and return a handle.
6. Handle exceptions and error/log formatting, including **“exception occurred: {}; callstack: {}”** and **“unknown exception occurred”**.

Conservative pseudocode:

```text
NewFeature(gameHandle, featureID, input, length):
    game = resolve_composite_handle(gameHandle)
    factory_state = feature_factory_dispatch(featureID, game, ...unknown...)
    descriptor = resolve_feature_descriptor(featureID)
    parse_and_validate_input_or_report_error()
    feature = construct_state_in_184byte_allocation(...unknown fields...)
    return insert_feature_registry(feature)
```

Function 1984 is 31,638 bytes and decompiles to approximately 200 KB. It is preserved in the selected connected analysis, but most of its large lazy-initialization/factory branches are not interpreted. There is no proven exhaustive feature-ID-to-schema dictionary or reconstructed scoring formula.

**Status:** 1694/1686 partial; 1984 structurally analyzed. The presence of parser errors does not identify review classification math.

## 5. Run and disposal use the same registry family

JavaScript calls `CEE_Run(handle,0)` through async `ccall`; a result ≤0 produces an error. The integer return is not established as the completed score payload; output/completion have separate bridge channels.

Export 1699 reaches candidate body 1698 through initial slot 2052. That body uses initial slot 2043 → 1670 to look up a handle in global registry 12157936. Its failure path contains **“Invalid Feature handle”** at memory 114487. Later object/virtual/host-mediated work dispatch and cleanup remain only partially interpreted.

Disposal export 1697 reaches 1671 through initial slot 2041. The resulting map erase and shared-ownership cleanup are stronger evidence of a feature-handle API than the misleading JS local variable name `game_point` in that wrapper.

**Status:** Run/disposal shells and candidate Run body partial. Actual feature execution, callback schemas, and scheduling remain open.

## 6. Compiler state is not domain state

Global 0 initializes to 26,691,088 and acts as the linear-memory stack pointer in selected decompiled frames. Global 2/3 usage is consistent with Asyncify state/data bookkeeping: normal, unwind, and rewind paths. Memory word 18297676 is repeatedly used around Emscripten exception wrappers.

Those patterns must not be renamed as chess feature/classification states. Readable pseudocode above omits bookkeeping only for explanation; raw decompilation retains it. Cleanup and exception paths are not claimed equivalent to normal flow.
''')
put('05-memory-and-companions.md','''# Memory, static data, and companion resources

Every module has a `memory-data-map.json` with active/passive segment lengths, hashes, binary offsets, initial memory addresses, and bounded hex previews. Limits and shared/memory64 flags are structural facts; `memory.grow` instruction counts are separate observations. Runtime heap shape, growth, and allocation lifetimes were not measured.

Baseline facts remain:

| Module | Memory |
|---|---|
| CEE 001/002 | 386 MiB initial, 2 GiB maximum, nonshared |
| Stockfish 003 | Fixed 512 MiB imported shared memory |
| Stockfish 004 | 64 MiB initial, 2 GiB maximum, nonshared |
| Torch 005 | Fixed 512 MiB, nonshared |

New modules' exact declarations are in the comparison matrix. Variant names are not treated as proof of thread support.

## Bounded CEE layout reconstruction

- Composite game handle: arithmetic high part shifted by 20, low 20-bit mask.
- Lookup container: bucket pointer +28, bucket count +32, nonempty/state field +40.
- Lookup node: next +0, hash +4, key +8, value object +12, control pointer +16.
- Shared output pair: two 32-bit pointers; observed control-block counter at +4.
- Feature construction requests 184 bytes; one counted-pool path requests 44 bytes. This does not mean all fields are known.
- Small-string-style patterns use a sign byte at +11 and pointer/length fields. Exact source `std::string` typedef/ABI is inferred, not recovered from debug types.
- The JS protobuf command bridge allocates request bytes and an 8,192-byte response buffer, calls a four-number ABI, copies via `.slice()`, then frees. This is marshalling evidence, not proof that every native path respects the capacity or every schema is mapped.

## Two actual NNUE networks

| Public filename | Complete bytes | SHA256 |
|---|---:|---|
| `nn-ad9b42354671.nnue` | 47,001,499 | `ad9b423546714137916bd38978af6fd68d7b8951bef25ff76bf43da72d6cb786` |
| `nn-5af11540bbfe.nnue` | 40,119,326 | `5af11540bbfefcb54e38c5dd000cab4b469dfa7599a1d55be5d2722c20a8929b` |

Both returned HTTP 200 in full. Their observed NNUE-layout version is `0x7af32f20`, with different architecture hashes and the 75-byte description:

> Network trained with the https://github.com/glinscott/nnue-pytorch trainer.

This is real parameter-file evidence. Complete tensor decoding and compatibility with every Stockfish build are not established. Historical one-byte 206 responses are not substituted for these full acquisitions.

## Other companion boundaries

Saved HTML explicitly declares `/bundles/web/wdl/model.json` and `group1-shard1of1.bin`; both returned 404 in this pass. They are frontend WDL leads, not proven CEE/Torch imports. Already-abandoned coach/charm endpoints were not reprobed. The Charm bridge accepts model bytes and an optional key, but no private key or encrypted model was bypassed/recovered.

Large Torch data sections demonstrate static-payload variation, not automatically a `.pt`, ONNX format, tensor layout, or recovered model algorithm. Opening books are classified separately; hundreds are optional application assets, not proven dependencies of every WASM module. JavaScript `.data` properties are not asset paths.
''')
put('06-rive-and-dynamic-modules.md','''# Rive source recovery and dynamic-module boundaries

## Actual published source contents

Two public `rive.js.map` files contain 45 source-content entries: 16 for 2.38.2 and 29 for 2.49.3. Extracted, privacy-scrubbed sources are under `rive-recovered-sources/`. The reconstruction index records original names, map URL/hash, raw content hash, scrubbed hash, and loader excerpts.

These are **real published TypeScript/JavaScript sources**, not synthesized WASM source.

## Loader semantics

The default WASM URL is package/version-qualified unpkg `rive.wasm`; fallback uses jsdelivr `rive_fallback.wasm`. The runtime's `locateFile:()=>attemptedUrl` overrides the generated `webgl2_advanced.wasm` default. A 404 for that generated default is therefore not proof of a production dependency failure.

On primary failure, the loader clears any in-memory binary, switches to an eligible fallback, and retries. Repeated fallback failure resets loading/error queues. The source reveals both URL selection and recovery-state behavior.

Version 2.49.3 only attempts a threaded build when the imported threaded implementation is a function, the thread URL is enabled, no host binary overrides it, and threads have not already been tried. It checks cross-origin isolation, posting a SharedArrayBuffer to MessageChannel, and validation of a 63-byte atomic/SIMD probe. The map also contains an ignored `rive_threads.mjs` entry. Its constructed thread URL returned 404; this does not prove that this package selects that path in production.

## Four small module identities

| ID | Bytes | Defined functions | Purpose |
|---|---:|---:|---|
| 027 | 63 | 2 | Shared memory, atomic load, SIMD validation |
| 028 | 31 | 1 | Static frontend SIMD capability check; repeated occurrences alias |
| 029 | 43 | 1 | Constructed zero-vector SIMD capability check |
| 030 | 64 | 1 | Constructed relaxed SIMD `i8x16.relaxed_swizzle` check |

These have exact bytes, hashes, structures, and validation results despite lacking separate `.wasm` URLs. A four-byte magic-check constant is not a module.

## Dynamic WASM rewriting

Saved source SRC-1137 also parses/rewrites WASM sections: extracting custom payloads, lifting a start function into `__riveLiftedStart`, converting shared defined memory into an import, and making data segments passive for worker setup. Adjacent code coordinates parallel workers and shared control blocks.

These are genuine dynamic transformation mechanisms. Their possible outputs cannot be enumerated without input script payloads and runtime observations. Two literal probe-builder calls were resolved exactly as 029/030; arbitrary script-dependent transformed modules remain explicitly unresolved.

Rive is third-party animation/graphics/runtime infrastructure. Its function counts are not newly understood chess algorithms.
''')
put('07-architecture-and-reconstructability.md','''# Architecture and reconstructability

```mermaid
flowchart TD
  UI[Frontend application] --> Manager[JS engine selection / worker RPC]
  Manager --> CEE[CEE core + Emscripten glue]
  Manager --> SF[Stockfish variants + NNUE]
  Manager --> Torch[Torch variants / multipart static data]
  UI --> Rive[Rive animation / script runtime]
  Rive --> Loader[Primary / fallback / capability probes]
  Rive --> Dynamic[Script-dependent WASM transforms]
  CEE --> Host[invoke wrappers / callbacks / scheduler]
  Host --> Table[Function table / dynCall trampolines]
  Table --> CEE
  UI -. separate services; exact transaction unproved .-> Backend[Historical HTTP/RPC and server evidence]
```

Interop is evidenced through JavaScript selection, marshalling, and imports—not an assumption that all modules directly link. No proven native cross-module graph connects a CEE index to a Stockfish or Rive index; indices are module-local. Worker RPC and buffers are architectural boundaries, not one combined native address space.

### Attribution

- **Stockfish:** strong lineage evidence from glue license/source attribution, UCI/NNUE interfaces, and real NNUE payloads. Exact fork patches and production configuration remain incomplete.
- **Torch:** branding and matching exports do not identify open-source PyTorch or prove equal models.
- **CEE:** application-specific explanation/feature logic mixed with substantial C++/Emscripten runtime. Compiler helpers must not be counted as business algorithms.
- **Rive:** third-party graphics/script runtime, separate from CEE review classification.

Historical backend chapters remain historical/public/secondary evidence. This pass does not turn CloudSQL/MySQL/PHP/Symfony observations into private endpoints, table schemas, SQL statements, or recovered server-side CEAC algorithms.

### What can be reconstructed

**Now:** exact ABIs and static structures; selected handle/container algorithms; JS copy/free behavior; loader retry/variant logic; selected raw decompilation.

**With substantial further work:** CEE feature factories/schemas/CFGs; Torch search/evaluation; tensor formats; virtual dispatch; allocation lifetimes.

**Not from this evidence alone:** original names/comments/typedefs; private encryption keys; unobserved runtime inputs and backend databases; all unobserved builds; behavioral parity without controlled functional tests.
''')
put('08-limitations-and-next-steps.md','''# Coverage ledger and next steps

## Structurally completed for the acquired inventory

- 29 complete core modules, all V8-valid.
- 225,335 defined-function records; zero final decode errors or section remainders.
- Original 48,089 function indices preserved.
- Section/type/import/export/table/memory/global/start/element/code/data/custom/data-count/tag inventories.
- Actual opcode features, direct graphs/SCCs, and conditional initial-table dispatch.
- URL/hash/alias separation; multipart assembly; workers/maps/models and failures recorded.

## Not exhaustively satisfied

| Requirement | Actual boundary |
|---|---|
| Understand all important functions | Most remain structural; CEE case studies are bounded |
| Full CFG/dataflow for every function | Not done; selected decompilation is not full semantic recovery |
| Sound indirect-dispatch fixed point | Not done |
| Decode all model tensors/weights | Not done |
| Discover every accessible build/dynamic module | Not established |
| Fetch every companion path | Not done; many book leads classified only |
| Authenticated production HAR/runtime coverage | Not available |
| CEE/Torch functional parity, labels, accuracy, ratings | Not established |
| Recover original source | Not delivered; real Rive maps and decompiler output are distinguished |
| Embed every acquired raw payload | Not possible within this package's persistence budget; exclusions explicit |

## Highest-value continuation

1. Resolve CEE 1984's factory branches, instantiated types, parser schemas, and actual feature-ID callers. Do not confuse engine build versions with feature IDs.
2. Follow 7890/8691 handle subentries, 1961 feature-state fields, and 1672 erase/destructor ownership.
3. Build bounded interprocedural CFG/dataflow slices through selected feature parsers and output callbacks, cross-referencing real JS protobuf schemas.
4. Track table mutations, dynCall trampolines, callbacks, and memory aliases to a fixed point. Initial slots remain conditional until stability is proved.
5. Only then execute controlled, network-denied fixtures with understood imports and inputs. Prior stub instantiation was not a review test.
6. Decode NNUE architecture/layout against exact engine builds before claiming network compatibility.
7. Capture authorized runtime asset selection to resolve WDL/Charm/Torch configuration and Rive script-derived modules. No authentication/key bypass.

This is an additive investigation checkpoint, not a claim that the extreme-depth mission is finished.
''')
put('09-evidence-and-packaging.md','''# Evidence, packaging, and reproduction

## Baseline preservation and replacement

The old ZIP is retained until replacement QC passes, then atomically replaced at the canonical `website-complete-forensic-audit.zip` path. Every baseline member's contents remain unchanged. The existing restore map and `restore-workspace.py` remain usable because the canonical filename and member paths are preserved.

## Compression compatibility

This archive uses **ZIPLZMA, method 14**. Python 3's `zipfile` and 7-Zip support it; some built-in unzip viewers do not. Plain JSONL members can be streamed through `zipfile.open`. They are not nested gzip in the final ZIP.

## Explicit raw-payload exclusions

The original five baseline binaries remain embedded. Newly retrieved large runtime binaries and the two NNUE parameter payloads were analyzed in scratch but are **not all embedded**, because the persistent workspace is capped. Every such decision is recorded in `packaging-retention.json` with exact URLs, bytes, hashes, status, and reason. Inline probes are included.

The retrieval logs, all derived structural/semantic records, source-map contents, bounded source evidence, and analysis scripts are included. This is an explicit delivery limitation, not complete raw-evidence preservation.

`retrieve-evidence.py` restores excluded public payloads to a downloaded local copy, checking exact SHA256. Multipart Torch uses six ordered part URLs, individual part checks, concatenation, and a final hash check. Mutable upstream URLs may change or disappear; the helper cannot guarantee future availability. Large restoration is not automatic inside this capped workspace.

## Privacy and reproducibility

Public source-map/glue text is scrubbed for email and obvious bearer credentials, while raw acquisition hashes remain in provenance. Pattern-based screening is not proof that every possible PII format is absent. Raw versus scrubbed content hashes and offsets must not be confused.

Scripts under `tools/` document the actual method and retain scratch defaults/toolchain dependencies. They are not represented as a fully portable one-command installation. The exact WABT opcode metadata is retained; native WABT/V8 tool versions and outcomes are recorded.

The follow-up has its own source/finding indices and checksums without renumbering historical IDs. The final QC report records member preservation, CRC, manifests, status totals, JSON parsing, and archive size.
''')
print('Editorial pass:10 readable chapters')
