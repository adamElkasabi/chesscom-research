// Main numeric/codec regression entry point uses the real bundled CEE now.
// The old Stockfish threshold/formula implementation is intentionally gone.
import assert from 'node:assert/strict';
import { START_FEN, Board, pgnToUci } from '../lib/chess.js';
const uci = pgnToUci('1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 *');
assert.equal(uci.length, 6);
const board = new Board(START_FEN);
for (const move of uci) board.apply(move);
assert.equal(board.fullmove, 4);
assert.equal(board.turn, 'w');
console.log('PASS PGN and board plumbing');
await import('./cee-review-test.mjs');
