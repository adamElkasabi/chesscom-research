# Torch Human client-side investigation

## Confirmed execution, not just strings
Using the shipped explanation-engine.wasm (CEE 1.130.285), isolated RunSearch feature 29 accepted torchSearchMode human and completed a 1000-node opening-position search. Both control and human probes completed with progress=1. Fetch was replaced with a rejecting function; neither made a fetch attempt. The engine was executed locally through its Node wrapper, not in a browser UI, so this is local WASM execution proof, not a Chrome Game Review integration test.

Both responses log `engine: Torch master-20260925-87ee25a`. Ordinary mode returns score +17cp, depth 6; human mode +18cp, depth 5, with different returned variations. Decoded internal API logs show ordinary `go nodes 1000 searchmoves ...` versus human `go nodes 1000 pvtrees ... rating 2100 ... ep_loss_margin 0.02`. No errors/warnings recorded. The human request is therefore not simply ignored. Low-level evaluations retain engine enum 11; this alone does not prove the human mode was disabled.

Evidence files: results/probe-normal-offline.json, results/probe-human-offline.json; probe-normal-decoded-log.txt, probe-human-decoded-log.txt; human-probe.mjs and configs/probe-*.json. Human-no-Maia also completed in a separate unblocked-fetch test, with the same aggregate score as human.

## Website Game Review routing
Saved analysis frontend shared.eager.BOGLllgUUR.chunk.js:
- A4e chooses TORCH_HUMAN (12) when web_analysis_torch_human_v2 is enabled and selected engine is not Stockfish16.
- W4e serializes that engine in a CEAC GameReviewRequest with Fast/Standard/etc; disables game-state cache for Torch Human.
- x3e encodes it and sends over WebSocket via S3e to server selected by O4e, normally wss://analysis.chess.com:443/v2/game-review.
- C3e processes responses from that server.
Thus the inspected website full-review path requests Torch Human from a server; it is not proof of browser-side full Torch Human Game Review. Local worker loading for quick analysis/other features must not be conflated with this route.

## Remaining limitations
No successful full human-mode Game Review, no parity with cloud scores, no confirmed separate humanLine or Maia prediction output. Internal feature288 PVtrees probes with rating100 still timed out even at1000nodes. Normal and human EvaluateGame54 earlier aborted. Do not promote those failures to evidence the local RunSearch mode is unsupported.

Extension production files unchanged; all five working-v0.1.7.sha256 checks passed after this investigation.
