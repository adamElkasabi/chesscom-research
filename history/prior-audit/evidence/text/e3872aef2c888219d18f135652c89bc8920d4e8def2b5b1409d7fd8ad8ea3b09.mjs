import fs from 'node:fs';
import path from 'node:path';
const dir=path.dirname(new URL(import.meta.url).pathname);
const rows=fs.readdirSync(path.join(dir,'results')).filter(n=>n.endsWith('.json')).map(n=>JSON.parse(fs.readFileSync(path.join(dir,'results',n))));
const names=['baseline','uci-normalize-off','normalized-UseSoftNodes-true','normalized-Hash-64','normalized-standard'];
const fmt=n=>Number(n).toFixed(2), pair=o=>`${fmt(o.white)} / ${fmt(o.black)}`;
const table=names.map(id=>{const r=rows.find(x=>x.config.id===id);return `| ${id} | ${pair(r.actual.accuracy)} | ${r.actual.ratings.white} / ${r.actual.ratings.black} |`}).join('\n');
const holdout=JSON.parse(fs.readFileSync(path.join(dir,'holdout-validation.json')));
const holdoutTable=holdout.map(r=>`| ${r.id} | ${r.actual?pair(r.actual.accuracy):'FAILED'} | ${r.actual?r.actual.ratings.white+' / '+r.actual.ratings.black:'—'} |`).join('\n');
const fence=String.fromCharCode(96).repeat(3);
const doc=`# Torch refinement — findings and release decision

## Decision
**Keep the working v0.1.7 release unchanged.** Genuine embedded-engine settings can improve the newest reference, but the improvement does not consistently generalize. No new extension release is being claimed or substituted.

## What was tested
An automated, bounded search executed **${rows.length} trial configurations**, including repeat checks. ${rows.filter(r=>r.actual).length} returned complete numeric results; ${rows.filter(r=>!r.actual).length} failed or timed out. Separate holdout validation tested the two earlier fixtures. This is not an exhaustive search of every possible parameter value.

Trials run the actual bundled CEE/Torch WASM and preserve its returned scores. No fitted accuracy curves, rating correction formulas, per-game overrides, or relabeling of Torch as Torch Human were used. Search dimensions included supported UCI options, strength, classification version, node/depth limits, hash size, soft nodes, and embedded human-search paths. Raw failures remain recorded rather than treated as successful results.

## Torch Human
The shipped WASM contains TorchHuman/Maia/human-line machinery, and its protobuf descriptors expose human-mode requests. Saved Chess.com frontend code selects engine 12 for the Torch Human feature. This is strong evidence that it is an embedded mode, not evidence of a separately downloadable add-on.

**I did not successfully activate Torch Human for a complete review.** Completed ordinary reviews still reported engine 11. A native human-PV-tree probe timed out; whole-game EvaluateGame probes aborted, including a normal-mode control. Those failures do not establish that Human is unsupported, and the normal control failure prevents attributing the abort specifically to Human.

## Newest reference: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED]
All numbers below are White / Black. Target: accuracy **71.70 / 99.00**, ratings **100 / 1000**.

| Configuration | Accuracy | Game ratings |
|---|---:|---:|
${table}

Fast strength was retained except in normalized-standard. The Normalize-off result reproduced exactly in two additional clean trials. Normalize-off plus Hash=64 also reproduced exactly in additional clean trials.

### Classification trade-off
Normalize=false plus Hash=64 was the best aggregate match under the declared comparison objective: sum of absolute accuracy errors + twice the summed absolute tally differences + summed rating errors / 100. This objective only ranks real outputs; it never generates review scores.

With Normalize=false, Hash=64, all Black classification tallies match the reference exactly: Book 2, Great 1, Best 2, Excellent 5, other categories 0. White remains wrong: Book 2, Excellent 2, Mistake 5, Blunder 1 (other categories 0), versus target Book 2, Excellent 4, Good 1, Mistake 2, Blunder 1. Its accuracy is worse than some other candidates, so there is no single winner on every metric.

## Cross-game validation
Each held-out game was evaluated under baseline, Normalize=false, and Normalize=false plus Hash=64. Player color followed the prior fixture setup; no player rating or PGN header was optimized.

Targets:
- Human fixture: accuracy **76.80 / 70.20**, ratings **1350 / 600**.
- Bot fixture: accuracy **86.80 / 79.80**, ratings **1850 / 1500**.

| Fixture / configuration | Accuracy | Game ratings |
|---|---:|---:|
${holdoutTable}

Turning normalization off worsened the earlier human fixture in both accuracy and ratings. The candidate therefore fails the cross-game promotion check, even though it helps the latest reference and improves some bot-game metrics. This is evidence against blindly applying it globally, not proof that all possible configurations have been ruled out.

## Files and reproducibility
- trial.mjs: isolated actual-WASM trial runner.
- sweep.mjs: bounded search orchestrator and explicit ranking objective.
- configs/, results/: input configurations and raw outcomes, including errors.
- target.json: newest reference aggregate targets.
- leaderboard*.json and plan*.json: phase rankings/plans.
- validate.mjs, holdout/, holdout-validation.json: separate cross-game validation.
- torch-human-evidence.txt, uci-options.txt, wasm-descriptors/: native evidence.
- working-v0.1.7.sha256: checksums for protected production files.

Commands from the project root:

${fence}sh
CONCURRENCY=1 node research/refinement/sweep.mjs
PHASE=2 CONCURRENCY=1 node research/refinement/sweep.mjs
PHASE=3 CONCURRENCY=1 node research/refinement/sweep.mjs
node research/refinement/validate.mjs
node research/refinement/trial.mjs CONFIG.json OUTPUT.json
sha256sum -c research/refinement/working-v0.1.7.sha256
${fence}

Existing sweep results are reused. Run one engine trial at a time: parallel WASM reviews exhausted sandbox resources in an earlier attempt. Failed resource-pressure artifacts are kept separate and excluded from the trial count above.

Staged files, if present, are unvalidated implementation sketches only. They are not production code, not part of a delivered update, and should not be installed.
`;
fs.writeFileSync('/home/user/torch-refinement-findings.md',doc);
console.log('Report written:',rows.length,'configurations;',holdout.length,'holdout trials');
