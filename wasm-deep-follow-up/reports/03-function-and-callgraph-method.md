# Function coverage and call-graph method

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

The listed paths are logical members of `analysis-evidence.tar.xz`. Run `materialize-analysis.py` after downloading/extracting to restore exact plain JSON/JSONL. Lossless integer/column encoding reduces repetitive callsite storage; every decoded member is hash-checked. Scratch tools use `.jsonl.gz`; no records are omitted.

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

### Feature-gated validation outcome

Node 20 rejects the relaxed-SIMD capability probe 030 with default features, as the probe is designed to test. It validates with `--experimental-wasm-relaxed-simd`; independent native WABT `--enable-all` also succeeds. The other 28 modules pass default V8 validation. A feature-gated rejection is distinguished from malformed bytes.

### Selected original CFGs

`cee-connected-slice/selected-original-cfg.jsonl` adds 46 original-function normal-control graphs: 36,154 instruction nodes with original offsets/immediates and structurally resolved if/else, loop, branch, branch-table, and return edges. This is not a full interprocedural, exception-aware, path-feasible CFG fixed point or dataflow proof. It supplements rather than upgrades the semantic statuses.
