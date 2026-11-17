#!/usr/bin/env bash
set -u
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
ROOT='https://www.chess.com'
D='extension/engines'
get() { # get <relative-url> <dest>
  local u="$ROOT/$1" dst="$2"
  mkdir -p "$(dirname "$dst")"
  if [ -s "$dst" ]; then echo "SKIP  $dst"; return 0; fi
  local code size
  code=$(curl -sS -m 600 -A "$UA" -o "$dst" -w '%{http_code}' "$u")
  size=$(stat -c%s "$dst" 2>/dev/null || echo 0)
  if [ "$code" != 200 ] && [ "$code" != 206 ]; then echo "FAIL  $code $dst  ($u)"; rm -f "$dst"; return 1; fi
  printf 'OK    %-58s %10s bytes\n' "$dst" "$size"
}
export -f get; export UA ROOT D

# --- explanation engine (current build 1.130.285) ---
get 'r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.js'  "$D/cee/explanation-engine.js" &
get 'r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.wasm' "$D/cee/explanation-engine.wasm" &
get 'r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanation-engine.js'    "$D/cee/explanation-engine.no-simd.js" &
get 'r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanation-engine.wasm'   "$D/cee/explanation-engine.no-simd.wasm" &
wait
# --- torch (single threaded, no SharedArrayBuffer needed) ---
get 'r2/assets-chess-engine/Torch/torch-2-single-697050e.js' "$D/torch/torch-2-single.js" &
for i in 0 1 2 3 4 5; do
  get "r2/assets-chess-engine/Torch/torch-2-single-697050e-part-$i.wasm" "$D/torch/torch-2-single-part-$i.wasm" &
done
get 'r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js'   "$D/torch-lite/torch-2-lite-single.js" &
get 'r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm' "$D/torch-lite/torch-2-lite-single.wasm" &
wait
# --- stockfish ---
get 'bundles/app/js/engine/stockfish-nnue-16-single.js'  "$D/stockfish/stockfish-nnue-16-single.js" &
get 'bundles/app/js/engine/stockfish-nnue-16-single.wasm' "$D/stockfish/stockfish-nnue-16-single.wasm" &
get 'bundles/app/js/engine/stockfish-nnue-16-no-Worker.js'  "$D/stockfish/stockfish-nnue-16-no-Worker.js" &
get 'bundles/app/js/engine/stockfish-nnue-16-no-Worker.wasm' "$D/stockfish/stockfish-nnue-16-no-Worker.wasm" &
get 'bundles/app/js/engine/nn-5af11540bbfe.nnue' "$D/stockfish/nn-5af11540bbfe.nnue" &
wait
# --- opening book ---
get 'bundles/app/js/engine/book-small.json' "$D/book/book-small.json" &
wait
echo "=== done ==="
