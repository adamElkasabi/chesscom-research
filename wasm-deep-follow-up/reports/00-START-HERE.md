# Deep WebAssembly follow-up


## Focused Torch Human / bot-personality follow-up

A later focused follow-up now traces Human and bot paths and executes the genuine recovered Charm-small model. Prior structural function coverage is unchanged; this is not exhaustive native semantic recovery.

[Evidence-graded focused update](../../torch-human-bots-update/00_START_HERE.md) · [Overlay change manifest](../../TORCH_HUMAN_BOTS_PATCH_MANIFEST.md). This additive notice supersedes narrower earlier interpretations; it does not alter archived original documents.

---
## Status: PARTIALLY AUDITED — not an exhaustive semantic reconstruction

### Verified coverage

- **29 distinct core-module identities:** 25 downloaded or assembled runtime modules, including the original five, plus four inline/constructed capability probes. These are **not 29 chess engines**.
- **225,335 defined functions and 70,475,093 decoded instructions.** Every defined function has an explicit status. There are zero final decode errors, and all 29 modules passed V8 validation without target execution (relaxed-SIMD probe 030 requires the explicit V8 feature flag).
- The original **48,089 defined functions** retain their module IDs, indices, body offsets, sizes, and signatures.
- Added direct callsites, callers/callees, SCCs, export reachability, initial tables, type-filtered indirect candidate pools, and host-mediated `invoke_*` dispatch evidence.
- A **46-function connected CEE analysis derivative** retains 29 direct callsites between selected real bodies. Native WABT validation, WAT printing, and decompilation succeeded. It is explicitly **not a functional engine**: unselected functions remain external boundaries and data are placeholders.
- Recovered **45 published source-map source contents** from two Rive maps. Retrieved two complete NNUE parameter payloads and checked their hashes and headers.

### What remains incomplete

Most functions are structurally analyzed, **not semantically understood**. The full CEE feature factory, important transitive business callees, Torch search/evaluation, complete schemas, model tensors, dynamic-dispatch fixed points, and every potential public build generation remain unresolved. No accuracy, rating, classification, or engine-parity claim is established.

| Final status | Defined functions |
|---|---:|
| STRUCTURALLY ANALYZED | 209,715 |
| UNDERSTOOD | 13,560 |
| PARTIALLY UNDERSTOOD | 2,054 |
| MOSTLY UNDERSTOOD | 6 |

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

**Accessing the complete function records:** they are losslessly packed in `analysis-evidence.tar.xz`. After downloading/extracting the outer ZIP locally, run `python3 materialize-analysis.py --output .` from the follow-up directory. The helper restores and verifies all 493 exact logical analysis members. See the packaging chapter before attempting to expand them.
