# API and network inventory

[Master index](00_MASTER_INDEX.md)

235API/WS-looking URL literals or declared callback routes are inventoried below. They are explicitly labelled candidates/declarations,not all observed successful endpoints. Headers,auth,request/response,status,pagination and filtering remain unknown unless preserved in a specific call site/schema/probe. No live credentials or captured cookies are copied.

## Endpoint shards

- [registries/endpoints-001.md](registries/endpoints-001.md)
- [registries/endpoints-002.md](registries/endpoints-002.md)
- [registries/endpoints-003.md](registries/endpoints-003.md)
- [registries/endpoints-004.md](registries/endpoints-004.md)
- [registries/endpoints-005.md](registries/endpoints-005.md)

## Full machine records

- [Endpoints](registries/endpoints.json)
- [Historical HTTP probes](registries/historical-http-probes.json)
- [Declared RPC service methods](registries/rpc-services.json)
- [Schema fields and message types](registries/schemas.json)

The full CEAC request/response code and example trees from PREMIUM-ANALYSIS are preserved as individual [documentary findings](findings/FINDINGS_INDEX.md), not collapsed into this endpoint table.

## Detailed findings

- [FND-18892](findings/api_network-001.md#FND-18892) — Production Game Review WebSocket
- [FND-18893](findings/api_network-001.md#FND-18893) — ProdServerIDLRunSearch endpoint
- [FND-18894](findings/api_network-001.md#FND-18894) — StagingServerIDLGameReview endpoint
- [FND-18895](findings/api_network-001.md#FND-18895) — SandboxServerIDLGameReview endpoint
- [FND-18896](findings/api_network-001.md#FND-18896) — StagingServerIDLRunSearch endpoint
- [FND-18897](findings/api_network-001.md#FND-18897) — NewMax endpoint
- [FND-18898](findings/api_network-001.md#FND-18898) — StagingMax endpoint
- [FND-18899](findings/api_network-001.md#FND-18899) — CEAC frame boundaries are WebSocket message boundaries
- [FND-18900](findings/api_network-001.md#FND-18900) — Handshake timeout is separate from review duration
- [FND-18901](findings/api_network-001.md#FND-18901) — Response stream is a tagged oneof
- [FND-18902](findings/api_network-001.md#FND-18902) — Request heartbeat settings
- [FND-18903](findings/api_network-001.md#FND-18903) — Remote run-search has a historical JSON path too
- [FND-18904](findings/api_network-001.md#FND-18904) — Same-origin socket override is not a new public endpoint
- [FND-18922](findings/api_network-001.md#FND-18922) — Brilliant verification can modify a local tally afterward
- [FND-18986](findings/network_probe_observations-001.md#FND-18986) — Historical GET probe https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm
- [FND-18987](findings/network_probe_observations-001.md#FND-18987) — Historical GET probe https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js
- [FND-18988](findings/network_probe_observations-001.md#FND-18988) — Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm
- [FND-18989](findings/network_probe_observations-001.md#FND-18989) — Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm
- [FND-18990](findings/network_probe_observations-001.md#FND-18990) — Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js
- [FND-18991](findings/network_probe_observations-001.md#FND-18991) — Historical GET probe https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js
- [FND-18992](findings/network_probe_observations-001.md#FND-18992) — Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js
- [FND-18993](findings/network_probe_observations-001.md#FND-18993) — Historical GET probe https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js
- [FND-18994](findings/network_probe_observations-001.md#FND-18994) — Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js
- [FND-18995](findings/network_probe_observations-001.md#FND-18995) — Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js
- [FND-18996](findings/network_probe_observations-001.md#FND-18996) — Historical GET probe https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js
- [FND-18997](findings/network_probe_observations-001.md#FND-18997) — Historical GET probe https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js
- [FND-18998](findings/network_probe_observations-001.md#FND-18998) — Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm
- [FND-18999](findings/network_probe_observations-001.md#FND-18999) — Historical GET probe https://www.chess.com/bundles/app/js/engine/stockfish.js
- [FND-19000](findings/network_probe_observations-001.md#FND-19000) — Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm
- [FND-19001](findings/network_probe_observations-001.md#FND-19001) — Historical GET probe https://www.chess.com/bundles/app/js/engine/stockfish.wasm
- [FND-19002](findings/network_probe_observations-001.md#FND-19002) — Historical GET probe https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm
- [FND-19003](findings/network_probe_observations-001.md#FND-19003) — Historical GET probe https://www.chess.com/bundles/app/js/engine/torch.js
- [FND-19004](findings/network_probe_observations-001.md#FND-19004) — Historical GET probe https://www.chess.com/robots.txt
- [FND-19005](findings/network_probe_observations-001.md#FND-19005) — Historical GET probe https://www.chess.com/bundles/app/js/engine/torch-lite.js
- [FND-19006](findings/network_probe_observations-001.md#FND-19006) — Historical GET probe https://www.chess.com/bundles/app/js/engine/books/eco.json
- [FND-19007](findings/network_probe_observations-001.md#FND-19007) — Historical GET probe https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue
- [FND-19008](findings/network_probe_observations-001.md#FND-19008) — Historical GET probe https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue
- [FND-19009](findings/network_probe_observations-001.md#FND-19009) — Historical GET probe https://www.chess.com/analysis
- [FND-19010](findings/network_probe_observations-001.md#FND-19010) — Historical GET probe https://www.chess.com/bundles/app/js/engine/torch.wasm
- [FND-19011](findings/network_probe_observations-001.md#FND-19011) — Historical GET probe https://www.chess.com/bundles/app/js/engine/torch-lite.wasm
- [FND-19012](findings/network_probe_observations-001.md#FND-19012) — Historical GET probe bundles/app/js/engine/stockfish-nnue-16-no-Worker.js
- [FND-19013](findings/network_probe_observations-001.md#FND-19013) — Historical GET probe bundles/app/js/engine/stockfish-nnue-16-no-Worker.wasm
- [FND-19014](findings/network_probe_observations-001.md#FND-19014) — Historical GET probe bundles/app/js/engine/stockfish-nnue-16-single.js
- [FND-19015](findings/network_probe_observations-001.md#FND-19015) — Historical GET probe bundles/app/js/engine/stockfish-nnue-16-single.wasm
- [FND-19016](findings/network_probe_observations-001.md#FND-19016) — Historical GET probe bundles/app/js/engine/stockfish-single.js
- [FND-19017](findings/network_probe_observations-001.md#FND-19017) — Historical GET probe bundles/app/js/engine/stockfish-single.wasm
- [FND-19018](findings/network_probe_observations-001.md#FND-19018) — Historical GET probe bundles/app/js/engine/stockfish-nnue-16-no-simd.js
- [FND-19019](findings/network_probe_observations-001.md#FND-19019) — Historical GET probe bundles/app/js/engine/stockfish-nnue-16-no-simd.wasm
- [FND-19020](findings/network_probe_observations-001.md#FND-19020) — Historical GET probe bundles/app/js/engine/stockfish.asm.js
- [FND-19021](findings/network_probe_observations-001.md#FND-19021) — Historical GET probe bundles/app/js/engine/book-small.json
- [FND-19022](findings/network_probe_observations-001.md#FND-19022) — Historical GET probe bundles/app/js/vendor/explanation-engine/explanation-engine.js
- [FND-19023](findings/network_probe_observations-001.md#FND-19023) — Historical GET probe bundles/app/js/vendor/explanation-engine/explanation-engine.wasm
- [FND-19024](findings/network_probe_observations-001.md#FND-19024) — Historical GET probe r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.js
- [FND-19025](findings/network_probe_observations-001.md#FND-19025) — Historical GET probe r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.wasm
- [FND-19026](findings/network_probe_observations-001.md#FND-19026) — Historical GET probe r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanation-engine.js
- [FND-19027](findings/network_probe_observations-001.md#FND-19027) — Historical GET probe r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanation-engine.wasm
- [FND-19028](findings/network_probe_observations-001.md#FND-19028) — Historical GET probe r2/assets-chess-engine/explanation-engine/1.130.212/no-simd/explanation-engine.js
- [FND-19029](findings/network_probe_observations-001.md#FND-19029) — Historical GET probe r2/assets-chess-engine/explanation-engine/1.130.212/no-simd/explanation-engine.wasm
