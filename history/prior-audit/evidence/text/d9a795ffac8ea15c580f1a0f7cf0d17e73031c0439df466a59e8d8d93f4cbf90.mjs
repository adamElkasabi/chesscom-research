// Real CEE wasm, real CEAC envelope. Does not assert fake cloud parity.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { encodeMessage, decodeMessage, frame, unframe } from '../lib/protobuf.js';
import { buildGameReview, MC } from '../lib/review.js';
import { ceeWorkerFactory } from './cee-worker-shim.mjs';

const pgn = fs.readFileSync(new URL('../../research/fixtures/doting-prospect.pgn', import.meta.url), 'utf8');
const target = {
  accuracy: { white: 71.7, black: 99.0 }, ratings: { white: 100, black: 1000 },
  tallies: {
    white: { BOOK: 2, BRILLIANT: 0, GREAT_FIND: 0, BEST: 0, EXCELLENT: 4, GOOD: 1, INACCURACY: 0, MISTAKE: 2, MISSED: 0, BLUNDER: 1 },
    black: { BOOK: 2, BRILLIANT: 0, GREAT_FIND: 1, BEST: 2, EXCELLENT: 5, GOOD: 0, INACCURACY: 0, MISTAKE: 0, MISSED: 0, BLUNDER: 0 },
  },
};
const request = {
  newGameReq: { newGame: {
    from: { case: 'pgnGame', value: { pgn, takeFirstGameOnly: true, metadata: {
      players: [ { color: 1, name: '[PUBLIC_PLAYER_HANDLE_REDACTED]', ratings: [{ rating: 100 }] },
        { color: 2, name: '[PUBLIC_PLAYER_HANDLE_REDACTED]', ratings: [{ rating: 333 }] } ],
      result: { result: 2, resultType: 1 },
      timeControl: { control: { case: 'base', value: { baseMs: 600000n, incrementMs: 0n } } },
      isRated: true, chesscomMetadata: { legacyGameId: 186934806892n, gameSource: 2 },
    } } }, settings: { userColor: 2, enableSkills: true },
  } },
  runSearchReq: { search: { case: 'gameReviewSearchSettings', value: { strength: 1 } } },
  engine: 12,
};
const progress = [];
const workloads = [];
const start = Date.now();
const result = await buildGameReview({ requestBytes: encodeMessage('.chesscom.ceac.v2.GameReviewRequest', request),
  workerFactory: ceeWorkerFactory, onProgress: p => progress.push(p),
  onWorkload: workload => workloads.push(workload), onLog: console.log });
assert.equal(workloads.length, 1, 'one timing workload per review');
assert.equal(workloads[0].plies, 20, 'timing uses the native parsed move count');
assert.equal(JSON.parse(workloads[0].searchKey).value.strength, 1, 'timing profile uses actual Fast search settings');
const response = decodeMessage('.chesscom.ceac.v2.GameReviewResponse', result.bytes);
assert.equal(response.result.case, 'success');
const g = response.result.value.gameReview;
assert.equal(g.review.playedMoves.length, 20);
assert.equal(g.evalGraph.evalGraphTicks.length, 20);
assert.equal(g.result.result, 2, 'correct winner');
assert.equal(g.result.resultType, 1, 'checkmate');
assert.equal(g.review.playedMoves.at(-1).movedColor, 2);
assert.ok(g.metadata.ceeVersion.major > 0);
assert.ok(g.metadata.annotatedPgn.includes('Nc2#'));
assert.ok(g.review.startingFen.includes(' '));
assert.ok(g.review.finalFen.includes(' '));
assert.ok(result.stats.audioHashes > 0, 'native speech hashes retained');
assert.ok(result.stats.explanationArrows > 0, 'native explanation arrows retained');
assert.deepEqual(result.stats.actualEngines, [11], 'do not relabel Torch as Torch Human');
assert.equal(result.stats.engineMatchesRequest, false);
assert.equal(progress[0], 0); assert.equal(progress.at(-1), 1);
for (const color of ['white', 'black']) {
  assert.equal(g.highlights.reportCard[color].gameRatingV2, g.highlights.reportCard[color].effectiveRating,
    'V2 UI alias is the exact CEE legacy rating, not a formula');
  const tally = g.highlights.classificationTallies[color];
  assert.equal(tally.reduce((sum, row) => sum + (row.tally || 0), 0), 10);
}
const encoded = encodeMessage('.chesscom.ceac.v2.GameReviewResponse', response);
assert.deepEqual(encoded, result.bytes);
assert.deepEqual(unframe(frame(result.bytes))[0], result.bytes);

// Also save a fully decoded review for inspection and accurate future diffs.
const names = Object.fromEntries(Object.entries(MC).map(([k,v]) => [v,k]));
const tallies = Object.fromEntries(['white','black'].map(color => [color,
  Object.fromEntries(g.highlights.classificationTallies[color].map(row => [names[row.moveClassification], row.tally || 0]))]));
const actual = { accuracy: result.stats.accuracy, ratings: result.stats.ratings, tallies };
const artifact = { elapsedSeconds: (Date.now()-start)/1000, target, actual, stats: result.stats,
  cloudParity: { accuracy: false, ratings: actual.ratings.white === target.ratings.white && actual.ratings.black === target.ratings.black,
    note: 'Engine mismatch is unresolved; no hard-coded target substitutions.' }, gameReview: g };
fs.writeFileSync(new URL('../../research/doting-extension-cee.json', import.meta.url), JSON.stringify(artifact, null, 2));
console.log(JSON.stringify({ elapsedSeconds: artifact.elapsedSeconds, actual, target, stats: result.stats }, null, 2));
console.log('ALL CEE INTEGRATION CHECKS PASS (cloud parity remains OPEN)');
