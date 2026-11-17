# 06 — Evidence map and reproduction

[Start](00_START_HERE.md)

## Evidence locations

| Question | Primary evidence |
|---|---|
| Exact public script URLs/bytes/hashes and safe headers | `evidence/source-manifest.json`, `evidence/public-scripts/` |
| Source symbol → exact source span | `evidence/extracted-functions.json` (source-relative JavaScript UTF-16 code-unit offsets, not guessed line numbers) |
| Descriptor provenance and native service feature routing | `descriptor-index.json`, `current-descriptors.json`, `service-routing.json` |
| Archived review source / glue identity | `baseline-source-references.json`; original SRC-1137/SRC-0014 remain in the full audit |
| Website activation observations without raw page PII | `page-safe-observations.json` |
| Offline fallback counts / displayed vs requested strength | `offline-catalog-analysis.json`; exact original public fallback script |
| Actual model bytes identity / header / record layout | `model-retrieval.json`, `model-header.json`, `model-tensor-manifest.json` |
| Native positive/negative and Human/legacy requests/results | `runtime-charm.json`, `runtime-charm-missing.json`, `runtime-human-*.json`, `runtime-legacy.json` |
| Failed initial harness timeout / other failed attempts | `runtime-charm-initial-timeout.json`, `attempt-ledger.json` |
| Historical command-level Human distinction | `historical-search-logs/` and untouched SRC-0871/SRC-1628/SRC-1629/SRC-1631 originals |
| Exact extracted-function branch/mapping tests | `frontend-function-tests.json`, `tools/test-functions.cjs` |
| What each conclusion is allowed to claim | `claims.json` |

Current descriptors are raw original bytes encoded in JSON. Native descriptor/proto files are recovered schema evidence; their generated `.proto` views are explanatory and the original binary descriptors remain available. Custom options are parsed numerically, not by assuming every RPC-looking method is a remote HTTP call. The limited wire parser retains raw option hex even where a bytes field also admits an incidental structural decode.

## Reproduce the safe/pure checks

Python standard library and Node20 are sufficient. No network access is required for these checks:

```sh
node website-audit/torch-human-bots-update/tools/test-functions.cjs
# expected: 32 checks passed
```

These checks execute the exact stored function bodies with mocks. Input enum maps are explicit test fixtures based on recovered enum definitions. They test semantic mapping, skill conversion, configured/direct-return behavior, fallback ordering, missing-game-point and stale-node queue behavior; they do not run a browser or native engine.

To redo AST extraction, copy the public scripts to a scratch source directory and restore the exact SRC-1137 bytes from the baseline path given in `baseline-source-references.json` as `SRC-1137.js` there. Then run:

```sh
SOURCE_DIR=/path/to/scratch-source node --expose-internals \
  website-audit/torch-human-bots-update/tools/extract.cjs
```

This uses Node's **internal** bundled Acorn; its availability is version-sensitive. It parses modules without importing/executing their initialization, captures exact function spans, extracts original template-literal descriptors and evaluates only the fallback catalog array in a bounded VM. Outputs go to that scratch source directory. Descriptor decoding can then use `EVIDENCE_DIR=/path/to/scratch-source python3 .../tools/decode_descriptors.py`.

## Optional model re-retrieval and parse

This deliberately downloads the11,946,339-byte model **only when explicitly run**:

```sh
python3 website-audit/torch-human-bots-update/tools/retrieve-model.py /scratch/topaz.bin
python3 website-audit/torch-human-bots-update/tools/parse_model.py \
  /scratch/topaz.bin /scratch/model-manifest.json
```

The downloader refuses an existing destination and refuses length/hash drift without writing a file. A current URL may later change or fail; that does not change the recorded binary identity. No model training or execution occurs in those two steps.

## Optional native reproduction — original bytes, sequential only

Restore these exact bytes from the **unchanged baseline full audit** into a scratch `cee/` directory:

1. `website-audit/wasm-analysis/modules/module-002/module.wasm` → `cee/explanation-engine.wasm` (SHA256 `b94aaeec32ee0458aeba42a9d431a15f37c16740c030868c691c0697b3203373`).
2. Baseline SRC-0014 path in `baseline-source-references.json` → `cee/explanation-engine.js` (SHA256 `46761f54ffdd6550b3fe90553e3c13d1a49828b3c44b680845afcc20c0666c70`).

Do not substitute files based merely on names/version strings. The wrapper is an original retained local extension research artifact; the test does not assert a newly downloaded worker hash. Do not run any connected-analysis derivative or placeholder module.

```sh
mkdir -p /scratch/results
CEE_DIR=/scratch/cee/ CHARM_MODEL=/scratch/topaz.bin RESULT_DIR=/scratch/results/ \
 node website-audit/torch-human-bots-update/tools/probe.mjs charm
# Use the same command with charm-missing, legacy, human-normal,
# human-default, human-no-maia, one at a time.
```

Trailing `/` in CEE_DIR and RESULT_DIR is required by this minimal runner. A rejecting fetch hook and75-second JS deadline are installed. Missing-model is an intentional negative control that exits nonzero. Run untrusted/large native binaries only inside an appropriate disposable sandbox with memory/time/network controls; the JS fetch hook alone is not OS isolation. Four concurrent large engines were not safe for this environment and were not used for final evidence.

The runner records binary hashes/native version and uses original descriptor-based protobuf encoding. Its synthetic diagnostic configuration is labeled in output. It creates no website session and makes no move on an external account. Outputs go to RESULT_DIR so packaged evidence need not be overwritten. Native elapsed values are local observations, not reliable cross-machine benchmarks.

## Verify and apply the overlay

Follow `TORCH_HUMAN_BOTS_PATCH_MANIFEST.md`. The machine manifest records before/after SHA256s for replacements, after SHA256s for additions and every expected path. Verification is offline and does not delete or extract anything. Original full-archive SHA256 remains `b0fc69d224b390b13f7d44fa59c19ab17eb02ceff260e51459ca80ee0b715282`.
