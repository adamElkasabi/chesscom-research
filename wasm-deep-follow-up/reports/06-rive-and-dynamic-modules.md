# Rive source recovery and dynamic-module boundaries

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
