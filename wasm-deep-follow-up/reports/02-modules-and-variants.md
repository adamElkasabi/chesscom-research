# Modules and version/target distinctions

|Binary ID|Bytes|Defined functions|SIMD instructions|Atomic instructions|FirstURL/source|
|---|---:|---:|---:|---:|---|
|module-001|32,865,067|22,922|0|0|https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanation-engine.wasm|
|module-002|32,922,478|22,953|24,166|0|https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.wasm|
|module-003|693,497|756|2,596|412|https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16-no-Worker.wasm|
|module-004|574,106|709|0|0|https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16-single.wasm|
|module-005|7,234,687|749|3,508|0|https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm|
|new-binary-006|673,189|754|1,987|414|https://www.chess.com/bundles/app/js/engine/stockfish-nnue-15.1-no-Worker.wasm|
|new-binary-007|683,786|758|0|447|https://www.chess.com/bundles/app/js/engine/stockfish-nnue-15.1-no-simd.wasm|
|new-binary-008|687,595|756|2,006|447|https://www.chess.com/bundles/app/js/engine/stockfish-nnue-15.1.wasm|
|new-binary-009|697,387|760|0|445|https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16-no-simd.wasm|
|new-binary-010|707,847|758|2,615|445|https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm|
|new-binary-011|1,381,822|4,631|0|0|https://www.chess.com/bundles/app/js/engine/stockfish-single.wasm|
|new-binary-012|385,560|951|0|501|https://www.chess.com/bundles/app/js/engine/stockfish.wasm|
|new-binary-013|6,840,976|752|2,644|328|https://www.chess.com/bundles/app/js/engine/torch-lite.wasm|
|new-binary-014|47,327,363|752|2,527|328|https://www.chess.com/bundles/app/js/engine/torch.wasm|
|new-binary-015|16,184,029|7,783|478|0|https://www.chess.com/bundles/app/js/vendor/explanation-engine-pd/explanation-engine.wasm|
|new-binary-016|32,766,847|22,824|24,084|0|https://www.chess.com/bundles/app/js/vendor/explanation-engine-staff/explanation-engine.wasm|
|new-binary-017|7,036,486|801|3,514|385|https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm|
|new-binary-018|32,557,049|22,565|23,901|0|https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm|
|new-binary-019|32,500,913|22,534|0|0|https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/no-simd/explanation-engine.wasm|
|new-binary-020|2,447,540|21,413|0|0|https://unpkg.com/@rive-app/webgl2@2.38.2/rive.wasm|
|new-binary-021|2,448,937|21,413|0|0|https://cdn.jsdelivr.net/npm/@rive-app/webgl2@2.38.2/rive_fallback.wasm|
|new-binary-022|2,385,648|11,744|8,435|0|https://unpkg.com/@rive-app/webgl2@2.49.3/rive.wasm|
|new-binary-023|2,414,644|11,750|0|0|https://cdn.jsdelivr.net/npm/@rive-app/webgl2@2.49.3/rive_fallback.wasm|
|new-binary-025|32,711,388|22,793|0|0|https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.254/no-simd/explanation-engine.wasm|
|new-binary-026|74,951,979|749|3,173|0|https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e-part-0.wasm|
|new-binary-027|63|2|1|1|Rive2.49.3source map runtimeLoader.ts:threadsProbe|
|new-binary-028|31|1|2|0|inline/constructed source|
|new-binary-029|43|1|1|0|inline/constructed source|
|new-binary-030|64|1|3|0|inline/constructed source|


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
