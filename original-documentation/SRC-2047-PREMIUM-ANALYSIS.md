# Chess.com premium analysis, end to end

What actually happens when you press **Game Review**, how accuracy is computed,
where the estimated Elo comes from, and what every classification means —
reconstructed from the production JavaScript bundles, not from documentation.

**Target:** the Game Review / advanced-analysis stack served to `www.chess.com/analysis`
**Method:** byte-offset reads of the shipped bundles (REA `analyze-javascript-application`,
evidence record `ev_a9a06871…479bcce`) plus protobuf
descriptor extraction; every schema claim is validated offline against libprotobuf (§10.3)
**Date:** 2026-11-11
**Companion:** `REVERSE-ENGINEERING.md` covers the *live-board* evaluation bar that the
extension taps; this document covers the *post-game* premium analysis, which is a
different server and a different protocol.

Written against these bundles (downloaded to `raw/`, since deleted — see
`REDOWNLOAD.md` to fetch them again):

| File | Size | What it holds |
| --- | --- | --- |
| `chunks/shared.eager.BOGLllgUUR.chunk.js` | 3.66 MB | CEAC transport, request builder, response → UI mapping, rating model |
| `chunks/tab-review.88a71be6.GEFrxdGEBZ.chunk.js` | 85 KB | the Game Review UI: report card, accuracy, rating display rules |
| `analysis.js` | 297 KB | analysis page bootstrap |
| 422 `FileDescriptorProto` blobs | — | every protobuf schema, rendered to `ALL-SCHEMAS.proto` (12,971 lines) |

> **No live calls were made from this sandbox.** Everything below is static
> analysis of downloaded files plus offline round-trip verification (§10.2–10.3).
> §10.1 tells you how to capture a real session on your own machine.

---

## 1. The short version

Chess.com's premium analysis is **not** computed in your browser. The browser
sends your game to an analysis server over a protobuf-over-WebSocket protocol
called **CEAC IDL**, and the server streams back a `GameReview` message
containing the accuracy number, the Elo estimate, a classification for every
move, and human-readable explanations.

The browser's job is almost entirely **presentation**: it renders the report
card, colours the moves, and plays the sentences. There is exactly *one*
analytic thing it computes locally — a confidence band derived from your rating
that decides which "you lost your winning advantage" sentence to show (§7.2).

```
                        ┌─────────────────────────────────────────┐
  your game  ──────────▶ │  wss://analysis.chess.com:443           │
  (protobuf)             │         /v2/game-review                 │
                         │                                         │
                         │  Stockfish 16.1 NNUE / Torch "human"    │
                         │  + explanation engine (CEE)             │
                         └──────────────┬──────────────────────────┘
                                        │ stream of GameReviewResponse
                                        ▼
        ┌───────────────────────────────────────────────────────┐
        │ browser: accuracy, report card, classifications,      │
        │          sentences, arrows — render only              │
        └───────────────────────────────────────────────────────┘
```

---

## 2. Where the premium line actually is

The paywall is not in the analysis; it is in **which fields the server is asked
to fill in**. Four checks decide it, all in
`shared.eager.BOGLllgUUR.chunk.js`:

| Function | Offset | Logic | Effect |
| --- | --- | --- | --- |
| `af()` | 315,764 | `analysis?.hasUnlimitedReview === true && user?.isDiamond !== true` | is this account entitled to *unlimited* reviews |
| `M4e()` | 1,813,143 | `features.includes('game_review_platinum_report_card') && af()` | **turns the report card on** |
| `Om(1)` | 327,157 | `return !user?.isDiamond && e > 0` | gates "locked takeaways" |
| `Am()` | — | `context.user && features.includes('web_game_review_train_cta') && features.includes('web_new_train')` | the Train CTA |

`M4e()` flows straight into the request (§4):

```js
...l || u ? { gameReviewOptions: HO(zGe, {
    reportCardEntitled: l,                       // <- M4e()
    includeTrainTakeaways: u,                    // <- Am()
    canAccessLockedTakeaways: u && !Om(1),
}) } : {}
```

So **the Elo estimate is a server feature flag, not a client calculation**. The
client does not compute a rating and then hide it behind a modal — it asks for
`report_card_entitled: true` and the server either populates
`GameReviewPlayerReportCard` or leaves it empty. That is why a free account
cannot obtain the number by patching out a CSS blur.

The UI side confirms it (`tab-review...chunk.js`):

```js
vp = (e) => flag && e.gameRatingV2 !== undefined;   // 46,853 — show at all?
yp = (e) => e.gameRatingV2 || e.effectiveElo;       //      — which number wins
xp = (e) => e.gameRatingV2 === 0
    ? 'There were not enough moves to rate this game.'
    : `Old Game Rating: ${...}`;                    // 47,090
```

Note the two names: `gameRatingV2` is the current model, `effectiveElo` /
"Old Game Rating" is the legacy one, kept as a fallback. **`gameRatingV2`
takes precedence when present**, including when it is `0` — a legitimate
"too few moves" answer, not a missing value.

---

## 3. Transport: CEAC IDL

### 3.1 Endpoints

All recovered from the `EW.Urls` table at offset **1,812,384**:

| Key | URL | Feature flag that selects it |
| --- | --- | --- |
| `ProdServerIDLGameReview` | `wss://analysis.chess.com:443/v2/game-review` | default |
| `StagingServerIDLGameReview` | `wss://analysis-staging.chess.com:443/v2/game-review` | `analysis_staging_server_idl` |
| `SandboxServerIDLGameReview` | `wss://analysis-sandbox.chess.com:443/v2/game-review` | `analysis_sandbox_server_idl` |
| `ProdServerIDLRunSearch` | `wss://analysis.chess.com:443/v2/run-search` | — |
| `StagingServerIDLRunSearch` | `wss://analysis-staging.chess.com:443/v2/run-search` | — |
| `NewMax` | `wss://max-analysis.prod.chess-platform.com:443` | maximum-strength analysis |
| `StagingMax` | `wss://max-analysis.staging.chess-platform.com:443` | — |

Selector (`O4e()`, same offset):

```js
function O4e() {
  if (features.includes('analysis_sandbox_server_idl')) return EW.Types.SandboxServerIDLGameReview;
  if (features.includes('analysis_staging_server_idl') || isStaging()) return EW.Types.StagingServerIDLGameReview;
  return EW.Types.ProdServerIDLGameReview;
}
```

Note the host split: `analysis.chess.com` for game review and position search,
`max-analysis.prod.chess-platform.com` for the deep "Maximum" engine. Two
different servers, two different jobs.

There is also a same-origin override used by the dev harness —
`window.chesscom.analysis.ceacSocketSameOrigin` — which rewrites the socket URL
to the page origin (`l3e()`). That is the hook worth knowing if you ever want
to run your own analysis server locally.

### 3.2 Framing

One WebSocket, binary frames, one protobuf message per frame. The client sets
`binaryType = 'arraybuffer'` and each frame is decoded as a
`GameReviewResponse` (`C3e()`, offset 1,836,513):

```js
e.onmessage = (ev) => {
  if (!(ev.data instanceof ArrayBuffer)) return;
  let a;
  try { a = Mk(OH, new Uint8Array(ev.data)); }       // OH = GameReviewResponse
  catch { /* logs "Invalid response from analysis server." and closes */ }
  SW('info', `IDL /v2/game-review frame (...)`)       // every frame is logged
};
```

The connection has a **10 s timeout** (`k3e = 1e4`) — much shorter than a review
takes, so it guards the *handshake*, not the stream.

### 3.3 Liveness on a long stream

The request asks for `heartbeatIntervalSeconds: 5`, and the server answers with
`GameReviewResponse.heartbeat` frames while it works. When the fleet is busy it
sends `waiting_for_capacity` instead — that is the "there are a few people
ahead of you" message. Progress arrives as `progress { float progress }`, which
drives the progress bar.

### 3.4 The other socket

`run-search` also exists as a **plain JSON** socket, used by the board's own
analysis mode rather than Game Review:

```json
{ "id": "...", "fen": "...", "uciMoves": ["e2e4"] }
```

with `heartbeat` and `waitingForCapacity` JSON messages. Same server, same
routing, no protobuf. If you only want *an evaluation* rather than a review,
this is the simpler interface.

---

## 4. The request, field by field

Reconstructed from `W4e()` at offset **1,814,722**. This is the entire
construction, only renamed:

```js
function buildGameReviewRequest({ chessGameProto, depth }) {
  const strength      = depthToStrength(depth);            // 18/22/24/26 -> FAST/STANDARD/DEEP/MAXIMUM
  const userColor     = currentOrientation();              // WHITE | BLACK | undefined
  const skillsOn      = shouldShowGameReviewSkills();
  const coach         = feature('game_review_user_selected_coach') ? selectedCoach() : null;
  const charmOn       = feature('cee_charm_inference_grv2');
  const trickyOn      = feature('cee_tricky_classification');

  return GameReviewRequest.create({
    newGameReq: NewGameRequest.create({
      newGame: { from: { case: 'game', value: chessGameProto } },
      settings: GameReviewSettings.create({
        ...(userColor === undefined ? {} : { userColor }),
        ...(skillsOn ? { enableSkills: true } : {}),
        ...(trickyOn ? { enabledFeatureFlags: ['cee_tricky_classification'] } : {}),
      }),
    }),

    runSearchReq: RunSearchRequest.create({
      search: { case: 'gameReviewSearchSettings', value: GameReviewSearchSettings.create({ strength }) },
      searchMoves: [],
      streamResults: false,
      heartbeatIntervalSeconds: 0,
    }),

    engine: pickEngine(),

    gameEvaluationOptions: GameEvaluationOptions.create({
      useGameStateCache: pickEngine() !== Engine.TORCH_HUMAN,
      useSerialEvaluations: false,
    }),

    requestMetadata: RequestMetadata.create({
      client: Client.WEB,               // 1
      product: Product.GAME_REVIEW,     // 2
      receivedTime: now(),
    }),

    requestOptions: RequestOptions.create({
      heartbeatIntervalSeconds: 5,
      useProgressUpdates: true,
    }),

    // premium
    ...(reportCardEntitled || trainCta
      ? { gameReviewOptions: GameReviewOptions.create({
            reportCardEntitled,
            includeTrainTakeaways: trainCta,
            canAccessLockedTakeaways: trainCta && !isLocked(),
        }) }
      : {}),

    ...(coach ? { setCoach: SetCoachRequest.create({ textId: coach.textId, locale: coach.locale }) } : {}),

    ...(skillsOn || charmOn
      ? { charmInfReq: CharmInferenceRequest.create({
            ...(skillsOn ? { tricky: TrickyCharmConfig.create() } : {}),
            ...(charmOn ? { grv2: GameReviewCharmV2Config.create() } : {}),
        }) }
      : {}),
  });
}
```

### 4.1 Engine selection (two-tier)

```js
function pickEngine() {
  if (!feature('web_analysis_torch_human_v2')) return Engine.SF16_1_NNUE;
  return fullAnalysisEngine === 'stockfish16' ? Engine.SF16_1_NNUE : Engine.TORCH_HUMAN;
}
```

`Engine` enum (from `chesscom/engine/v1`):

```
1 SF12   2 SF15   3 SF15_NNUE   4 SF15_1   5 SF15_1_NNUE   6 SF16_NNUE
7 SF9_FAIRPLAY_V1   8 DRAGON_3_3   9 KOMODO_3_3   10 SF16_1_NNUE
11 TORCH_3   12 TORCH_HUMAN   13 SF18_NNUE
```

**`TORCH_HUMAN` is the interesting one.** It is a human-like engine, and its
presence switches the evaluator off the game-state cache
(`useGameStateCache = engine !== TORCH_HUMAN`) — human-like evaluations are not
reusable between related positions, because the whole point is that they are
*not* objectively best. This is what makes "Great" and "Brilliant" findable:
a move a human would find but an engine would not is not scored as a blunder.

### 4.2 Depth

Four named strengths, mapped from a numeric depth by `P4e()` at offset
**1,813,265**:

| Page depth | Strength | Meaning |
| --- | --- | --- |
| 18 | `STRENGTH_FAST` | quick review |
| 22 | `STRENGTH_STANDARD` | default |
| 24 | `STRENGTH_DEEP` | "Deep" |
| 26 | `STRENGTH_MAXIMUM` | "Maximum" — the only one routed to `max-analysis.prod.chess-platform.com` |
| anything else | `STRENGTH_FAST` | fallback |

### 4.3 Envelope types

`GameReviewRequest` (`chesscom/ceac/v2/game_review.proto`) — note the gaps in
field numbers, which is where the newer features were bolted on:

```proto
message GameReviewRequest {
  NewGameRequest       new_game_req            = 1;
  RunSearchRequest     run_search_req          = 2;
  Engine               engine                  = 3;
  GameEvaluationOptions game_evaluation_options = 4;
  RequestMetadata      request_metadata        = 5;
  RequestOptions       request_options         = 6;
  SetCoachRequest      set_coach               = 7;
  CharmInferenceRequest charm_inf_req          = 8;   // skills / tricky / grv2
  GameReviewOptions    game_review_options     = 9;   // <- premium lives here
}
```

`Product` enum tells the server what to bill and what to enable:
`GAME_REVIEW=2`, `INSIGHTS=3`, `ADVANCED_STATS=8`, `BRILLIANT_VERIFICATION=12`,
`TRAIN=13`. `Client` is `WEB=1`, `TRAIN=17`, etc.

---

## 5. The response tree

One `GameReviewResponse` per frame; fields 1–5 are a oneof (`progress`,
`success`, `failure`, `heartbeat`, `waiting_for_capacity`). The payload arrives
in `success.game_review`:

```proto
message GameReviewResponseSuccess {
  GameReview game_review      = 2;
  repeated string cee_c_api_calls = 100;   // which CEE endpoints the server hit
}

message GameReview {
  EvalGraph  eval_graph = 1;   // per-ply Score + classification
  Highlights highlights = 2;   // accuracy, tallies, report card, summary
  Review     review     = 3;   // per-move detail + sentences
  GameResult result     = 4;
  Metadata   metadata   = 5;   // annotated PGN
  Opening    opening    = 6;   // ECO code, name, URL
}

message Highlights {
  string              game_summary                = 1;
  Accuracy            accuracy                    = 3;   // { float white=1; float black=2; }
  ClassificationTallies classification_tallies    = 4;
  GameReviewReportCard  report_card               = 5;   // <- the Elo estimate
  Takeaways             takeaways                 = 6;
  CoachEmotion          game_summary_coach_emotion = 7;
  string                game_summary_play         = 8;
}
```

`Review.played_moves` is the per-move detail the board renders:

```proto
message PlayedMove {
  bool          is_key_moment             = 1;
  Move          played_move               = 2;   // { move, classification, score, speech }
  Move          best_alternative_move     = 3;
  Color         moved_color               = 4;
  CoachEmotion  coach_emotion             = 5;
  SkillsPosition skills_earned            = 6;   // playable, hash-signed
  repeated PlayedMove explain_line        = 7;   // literal sentence alternatives
  Move          best_next_move            = 8;
}

message Move {
  ChessMove         move                = 1;   // from, to, promotion, time_taken_ms, clocks
  MoveClassification move_classification = 3;
  Score             score               = 4;
  Speech            speech              = 5;
  repeated ShowMoves show_moves_buttons = 6;
  BoardMarkings     board_markings      = 7;   // arrows + squares
}
```

`Score` is the shared currency everywhere (`chesscom/chess/v1/score.proto`):

```proto
message Score {
  sint32 score_centipawns_white = 1;   // always white's point of view
  int32  mate_in_white          = 2;
  int32  mate_in_black          = 3;
  Stalemate stalemate           = 4;
}
```

The client immediately converts it to pawns (`zU()`, offset ≈ 1,699,000):
`cp = score_centipawns_white / 100` (`Tqe = 100`), mate → `±1000` (`wqe = 1e3`).

### 5.1 Response → UI

`AJe()` at offset **1,711,579** is the whole mapping. It is short because the
server has already done the analysis:

```js
gameProps = {
  annotatedPgn: metadata.annotatedPgn,
  CAPS:         toCaps(review.accuracy),            // white/black headline %
  gameSummary:  highlights.gameSummary,
  reportCard:   toReportCard(highlights.reportCard),
  takeaways:    highlights.takeaways,
  tallies:      highlights.classificationTallies,
  startingFen:  review.startingFen,
  ...
};
```

and

```js
function toCaps(acc) {                              // offset 1,699,347
  return {
    white: { ...EMPTY_CAPS, all: acc?.white ?? 0 },  // {all,B,K,N,P,Q,R}
    black: { ...EMPTY_CAPS, all: acc?.black ?? 0 },
  };
}
```

**The headline accuracy is `highlights.accuracy.{white,black}` verbatim.** No
client-side recomputation. The per-piece `B/K/N/P/Q/R` slots exist in the model
and are filled from `ColorAccuracy.accuracy_by_piece_type` when the detailed
accuracy payload is present.

---

## 6. Accuracy

### 6.1 CAPS2

`chesscom/explanation_engine/v1/accuracy.proto` names the algorithm outright:

```proto
enum AccuracyAlgorithm {
  ACCURACY_ALGORITHM_UNSPECIFIED = 0;
  ACCURACY_ALGORITHM_CAPS2      = 1;
}

message ColorAccuracy {
  Color color = 1;
  repeated PieceTypeAccuracy accuracy_by_piece_type = 2;
  repeated GamePhaseAccuracy accuracy_by_game_phase = 3;
  double accuracy_overall    = 4;
  double avg_centipawn_loss  = 5;      // the raw ingredient
}

message VariationAccuracy { repeated ColorAccuracy accuracy_by_color = 1; }
```

So **CAPS2** is the name of the accuracy model ("Chess.com Accuracy
Percentage Score", v2). It is fed by average centipawn loss — the schema says
so explicitly — but the transform from loss to a 0–100 score happens on the
server. The client never sees the loss for the report card, only
`accuracy_overall`.

The tooltip text in the UI (offset 49,042 of `tab-review...`) describes it as a
score "from 0-100 when compared to the top chess computer moves".

Feature key **280** (`FEATURE_ID_INTERNAL_FEATURE_CAPS2 = 280`) gates the rollout, and
`cee_c_api_calls` in the response echoes which explanation endpoints ran.

### 6.2 What accuracy is *not*

There is no client-side formula for accuracy. Searching the 3.66 MB bundle for
`centipawn`, `winPercent`, `expectedScore`, `performanceRating` returns
**nothing**. The only `Math.exp` / `Math.log` expressions in the analysis code
are the two rating models in §7 — one for *display* (W/D/L), one for *speech
bands*.

---

## 7. Elo prediction

There are two completely separate systems. Conflating them is the usual mistake.

### 7.1 The real one: the server report card

```proto
message GameReviewPlayerReportCard {
  repeated GamePhaseReportCard reports_by_phase       = 1;
  repeated AdvancedStatCategoryReportCard reports_by_category = 2;
  int32 effective_rating     = 4;    // legacy "Old Game Rating"
  int32 game_rating_v2       = 5;    // current model
}

message GamePhaseReportCard {
  MoveClassification accuracy_glyph = 1;   // a *classification*, not a number
  GamePhase          phase          = 2;   // OPENING / MIDDLEGAME / ENDGAME
  float              accuracy       = 3;
}

message AdvancedStatCategoryReportCard {
  AdvancedStatType    category     = 1;    // OPENING / TACTICS / STRATEGY / ENDGAME / CLOCK
  MoveClassification  performance  = 2;
  int32               new_rating   = 3;    // per-category estimate
  int32               rating_change= 4;    // signed delta, e.g. -60
}
```

The client's job (`jqe()`, offset **1,701,418**) is a straight copy plus a
"is it empty" test:

```js
function toPlayerCard(e) {
  if (!e) return EMPTY;
  const { data, glyphs } = byPhase(e.reportsByPhase);     // gp0/gp1/gp2
  const categories       = byCategory(e.reportsByCategory);
  const effectiveElo     = e.effectiveRating ?? 0;
  const { gameRatingV2 } = e;
  return data.length === 0 && categories.length === 0 && effectiveElo === 0 && gameRatingV2 === undefined
    ? EMPTY                                                // nothing to show
    : { effectiveElo, gameRatingV2, data, glyphs, categories };
}
```

Phase keys are `GAME_PHASE_OPENING → 'gp0'`, `MIDDLEGAME → 'gp1'`,
`ENDGAME → 'gp2'`. Categories are renamed
`OPENING_CATEGORY → 'Opening'`, `TACTICS_CATEGORY → 'Tactics'`,
`STRATEGY_CATEGORY → 'Strategy'`, `ENDGAME_CATEGORY → 'Endgame'`; a missing
`performance` defaults to `'good'`.

**What can be stated from the bundles:** the server returns one rating for the
game (`game_rating_v2`), a legacy one (`effective_rating`), and a per-category
figure with a *signed* change. Because `rating_change` is signed and
per-category, the card can say "+45 in the Opening, −60 in Tactics" — a
breakdown, not a single delta.

**What cannot be stated:** the mapping from evaluations to a rating is not in
any shipped file. There is no formula to recover, no constant to read, and no
client-side recomputation to intercept — the three fields are copied straight
out of the response. Any claim about *how* the number is derived (percentile
over recent games, a performance-rating transform, an NN) would be guesswork.
What is verifiable is the interface: given these fields, the UI shows a rating;
without `game_rating_v2`, it shows the legacy number or nothing at all.

### 7.2 The decoy: the client-side W/D/L model

`b(e, t)` at offset **522,636** is a real, self-contained rating→result model.
It appears in the shared chunk, which is why it is easy to mistake for the
"Elo prediction":

```js
function wdl(whiteElo, blackElo) {
  const e = whiteElo / 100, t = blackElo / 100;
  const w = clamp( 0.20773843 * Math.atan(2.49085889*e - 2.47841945*t)
                 + 0.02262979*e - 0.02256839*t + 0.52239679, 0, 1);
  const l = clamp(-0.20720905 * Math.atan(2.49626837*e - 2.48220286*t)
                 - 0.02352551*e + 0.02172627*t + 0.49443923, 0, 1);
  const d = clamp( Math.exp(0.037043456*e + 0.178106427*t - 8.069742932)
                 + 0.004823544 * Math.exp(-1.364136591 * (e - t) ** 2)
                 - 0.001625539, 0, 1);
  const s = w + l + d;
  return { w: w/s, b: l/s, d: d/s };     // normalised to sum to 1
}
```

Measured output (`node crosscheck/wdl.mjs`):

| White | Black | win | draw | loss | White score |
| --- | --- | --- | --- | --- | --- |
| 2000 | 2000 | 0.573 | 0.026 | 0.401 | 0.586 |
| 2400 | 2000 | 0.916 | 0.025 | 0.059 | 0.929 |
| 2000 | 1200 | 0.996 | 0.004 | 0.000 | 0.998 |
| 2800 | 2000 | 0.971 | 0.029 | 0.000 | 0.986 |
| 1200 | 2000 | 0.027 | 0.016 | 0.958 | 0.034 |

A 400-point gap gives a 0.93 expected score, and a 2000-vs-2000 game is a
slightly-better-than-coin-flip (0.586) — this is fitted to *fast time-control
online chess*, where decisive games are the norm and draws are rare. The
draw term collapsing to ~2.6% is the signature: it is not the classical Elo
curve.

Where it is used: **nowhere near the report card.** `ySt()` / `xSt()`
(offsets 2,768,245 and 2,768,546) turn this into five *confidence bands* and
pick one of 10 canned sentences:

```js
const BANDS = { Winning: 0.2, Better: 0.4, Equal: 0.5, Worse: 0.65, Losing: 0.8 };  // for White
// for Black the same map is mirrored: 0.8, 0.65, 0.5, 0.4, 0.2

function evalThreshold(probability, rating) {
  // invert a logistic fitted to the rating scale, then rescale to pawns
  return Math.log(1 / probability - 1) / (0.004 * ((0.0685 * rating - 12) / 100)) / 100;
}
```

`rating` = **max(WhiteElo, BlackElo)**, defaulting to 2000 (`M4 = 2e3`). The
result is in **pawns** (the score it is compared against was divided by 100 in
§5). Measured (`node crosscheck/rating-bands.mjs`):

| max rating | Winning | Better | Equal | Worse | Losing |
| --- | --- | --- | --- | --- | --- |
| 800 | +8.10 | +2.37 | 0.00 | −3.62 | −8.10 |
| 1200 | +4.94 | +1.44 | 0.00 | −2.20 | −4.94 |
| 1600 | +3.55 | +1.04 | 0.00 | −1.59 | −3.55 |
| 2000 | +2.77 | +0.81 | 0.00 | −1.24 | −2.77 |
| 2400 | +2.27 | +0.67 | 0.00 | −1.02 | −2.27 |
| 2800 | +1.93 | +0.56 | 0.00 | −0.86 | −1.93 |

Read that as: *"how big an advantage does a player of this level need before we
call the position winning?"* A 2800 needs +1.93 pawns; an 800 needs +8.10. The
client classifies both the played move and the best alternative, then keys off
`${playedBand}${bestBand}`. Only the **10 downgrades** have sentences —
`WinningBetter`, `WinningEqual`, `WinningWorse`, `WinningLosing`, `BetterEqual`,
`BetterWorse`, `BetterLosing`, `EqualWorse`, `EqualLosing`, `WorseLosing` — and
each holds two impersonal and two personal phrasings (40 sentences). The
`WinningBetter` pair reads: *"You still have an advantage, but you no longer
have a winning position."* An improvement, or no change at all, falls back to the
plain played-move label.

**This produces prose, never a rating.** It is the mechanism behind the
"coach" voice, and it is the only piece of analysis logic that ships to the
browser.

---

## 8. Move classifications

```proto
enum MoveClassification {          // 32 values
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  BOOK = 1;      BRILLIANT = 2;   GREATFIND = 3;  BEST = 4;    EXCELLENT = 5;
  GOOD = 6;      INACCURACY = 7;  MISTAKE = 11;   BLUNDER = 15;
  FORCED = 19;   MISS = 20;       MISSED_MATE = 24; FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;  CRITICAL = 27;  MISSEDWIN = 28;
  // 8,9,10 / 12,13,14 / 16,17,18 / 21,22,23 / 29,30,31 are the same five
  // classes split by game phase: *_OPENING_PHASE, *_MID_GAME_PHASE, *_END_GAME_PHASE
}
```

The phase-split variants exist so a middlegame mistake and an opening
inaccuracy can carry different weights in the accuracy model and different
sentences. The UI collapses them back to the base class for the glyph.

The 19 visible badges map to: `Brilliant, GreatFind, Tricky, Book, BestMove,
Excellent, Good, Inaccuracy, Mistake, Miss (rendered "Missed"), Blunder,
Forced`, plus `MissedWin`. "Tricky" is not in the enum — it is a *charm*
inference label (requested via `charmInfReq`, §4), gated by the `cee_tricky_classification` feature flag,
which is why it can be absent from older reviews.

Per-side tallies come from `ClassificationTallies`:

```proto
message ClassificationTally { MoveClassification move_classification = 1; int32 tally = 2; }
message ClassificationTallies { repeated ClassificationTally white = 1; repeated ClassificationTally black = 2; }
```

The UI's local accumulator (offset **1,133,145**) shows the full set of counters
a game can report, including the phase splits and per-piece split:

```js
{
  CAPS:    { all: 0, B: 0, K: 0, N: 0, P: 0, Q: 0, R: 0 },
  pieceMoves: { B: 0, K: 0, N: 0, P: 0, Q: 0, R: 0 },
  tallies: {
    best, excellent, good, inaccuracy, mistake, blunder, forced, book,
    missedMate, fasterMate, winningToLosing, missedWin, greatFind, tricky,
    miss, critical, brilliant,
    blunderGP0, missedWinGP0, blunderGP1, missedWinGP1, blunderGP2, missedWinGP2,
  },
}
```

`GP0/GP1/GP2` are the opening / middlegame / endgame splits. And
`engine: SF16_1_NNUE` appears alongside them, so each review records which
engine produced it — a review made by `TORCH_HUMAN` is not numerically
comparable to one made by Stockfish.

---

## 9. Advanced stats, skills, explanations

### 9.1 Advanced stats — 102 categories

`AdvancedStatType` is the premium stats taxonomy. Structure, not a flat list:
five namespaces × what you did / what you allowed:

- **Tactics** (found / allowed): checkmates, free pieces, all tactics,
  unthemed tactics, forks, pins, discoveries, removes-defenders, trapped
  pieces, sacrifices — 10 topics × 2 directions.
- **Accuracy by position type**: strategic, attacking, defending, space,
  piece-activity, pawn-structure, then repeated for open / semi-open / closed,
  then endgame, king-pawn, rook-pawn, queen, other.
- **Strategic good/bad**: king safety, development, centre control, backward /
  isolated / doubled pawns, pawn chains, passed pawns, outposts, open files,
  piece activity, blockades, trades, space, occupying the centre, central
  breaks — 15 topics × 2 directions (56–89).
- **Time management** (90–96): `TIME_BLUNDERS`, `TIME_DISCERNMENT`,
  `TIME_PRESSURE_ACCURACY`, `CLOCK_ADVANTAGE`, `FLAG_RATE`, `SWINDLE_RATE`,
  `RUSHED_GAME_RATE`.
- **Categories** (100–104): the summary buckets the report card shows.

Percentiles are per-user aggregates:

```proto
message AdvancedStatsUser {
  repeated AdvancedStatPercentile advanced_stats_percentiles = 1;
  repeated AdvancedStatCategoryStats category_performances   = 2;
}
message AdvancedStatsForGame {
  AdvancedStatsUser  advanced_stats_user  = 1;   // vs. your history
  AdvancedStatsOther advanced_stats_other = 2;   // vs. this game's players
}
```

That two-sided structure is why the same stat can read "you are in the 71st
percentile" and "this game you scored below your average" at the same time.

### 9.2 Skills and the validation hash

```proto
message SkillsPosition {
  int32  ply             = 1;
  repeated Skill skills  = 2;     // 73 values
  string validation_hash = 3;     // signed by CEE
}
```

73 skills, e.g. `SKILL_FORK=21`, `SKILL_ROYAL_FORK=31`,
`SKILL_BRILLIANT_SACRIFICE=37`, `SKILL_OPPOSITION=65`,
`SKILL_ROOK_BEHIND_OWN_PASSED_PAWN=64`. These are what the step-by-step
explanation shows ("this move develops a piece with tempo") and they feed
puzzles.

`validation_hash` is the anti-tamper mechanism: the server signs which skills it
awarded, so a client cannot claim skills it did not earn. The client logs this
explicitly when the ids CEE needs are missing:

```
'0/3 IDL /v2/game-review — skills on; CEE has the ids to sign validationHash'
'0/3 IDL /v2/game-review — skills on but MISSING ids CEE needs; validationHash will come back empty'
```

CEE needs **white user id, black user id and game id** to sign. A game without
all three (guest, anonymous import) gets an empty hash and therefore no
persisted skill credit.

### 9.3 Explanations

`AnalysisType` has 300 values (`ANALYSIS_TYPE_FORK`, `..._SKEWER`,
`..._DIRECT_SACRIFICE_CAPTURE`, `..._IGNORES_THREAT`, `..._ZUGZWANG` …). They are
the taxonomy behind `Move.speech` and `explain_line`, which arrives as
**pre-rendered text**, not as a template to fill:

```proto
message PlayedMove {
  repeated PlayedMove explain_line = 7;   // literal alternatives: a b c d
}
```

The client picks one (`ESt()` builds the 10 downgrade keys like `WinningBetter`, and the
sentences are already localised, with `%color%` placeholders). Explanation
generation is a separate service reached by `cee_c_api_calls`, with feature
keys `ADVANCED_STATS_CATEGORY_SPEECH=279`, `GET_COACH_EMOTION=281`,
`GENERATE_COACH_TEXT_ITEMS=282`.

---

## 10. Verifying this yourself

Nothing below requires an account, and none of it runs from this sandbox.

### 10.1 Capture a real frame (on your own machine, your own account)

1. Open DevTools → Network → WS, tick **Preserve log**.
2. Go to `https://www.chess.com/analysis/game/live/<your-game-id>` and press
   **Game Review**.
3. Click the `wss://analysis.chess.com/443/v2/game-review` entry. You will see
   frames come in as binary. The `success` frame is the one you want.
4. Right-click → *Copy message* → *Copy as binary* (Chrome) or use
   `copy(new Uint8Array(...))`. Save it as `frame.bin`.

Or, more reliably, paste this in the console *before* starting the review and
copy the base64 it prints:

```js
(() => {
  const NativeWS = window.WebSocket;
  window.WebSocket = class extends NativeWS {
    constructor(...args) {
      super(...args);
      this.binaryType = 'arraybuffer';
      this.addEventListener('message', (ev) => {
        if (!(ev.data instanceof ArrayBuffer)) return;
        const b64 = btoa(String.fromCharCode(...new Uint8Array(ev.data)));
        console.log('CEAC frame', ev.data.byteLength, 'bytes', b64);
      });
    }
  };
})();
```

### 10.2 Decode it

```bash
node tools/ceac-dump.mjs frame.bin             # human-readable tree
node tools/ceac-dump.mjs frame.bin --json      # machine-readable
node tools/ceac-dump.mjs --selftest            # 20 checks, no network
```

A `success` frame prints, in outline:

```
success: {
  game_review: {
    eval_graph: { eval_graph_ticks: [ { move_score: { score_centipawns_white: 24 }, move_classification: BOOK }, ... ] }
    highlights: {
      accuracy: { white: 87.25, black: 82.5 }
      classification_tallies: { white: [ { move_classification: BOOK, tally: 6 }, ... ] }
      report_card: {
        white: {
          reports_by_phase: [ { phase: OPENING, accuracy: 97.5, accuracy_glyph: BEST }, ... ]
          reports_by_category: [ { category: OPENING_CATEGORY, new_rating: 2415, rating_change: 45 }, ... ]
          effective_rating: 2040
          game_rating_v2: 1987
        }
      }
    }
  }
  cee_c_api_calls: [ 'get_coach_emotion' ]
}
```

`--selftest` writes a synthetic frame byte-by-byte and asserts 20 decoded
values including a `sint32` of −310, a 10-byte sign-extended negative `int32`,
enum names, floats and repeated fields. It passes offline:

```
20/20 checks passed — fixture is 300 bytes
```

### 10.3 The stronger check

The field numbers in this document were recovered by reading descriptors, so the
real test is whether they match a *real* protobuf implementation.
`crosscheck/` does that: it builds the message with libprotobuf, serialises it,
and compares my decoder's output field by field. It needs Google's runtime,
which is not part of this workspace — `pip install protobuf grpcio-tools` first.
The generated `analysis_subset_pb2.py` is committed, so only the `protobuf`
runtime is strictly required.

```
$ cd /home/user/chesscom/crosscheck && python3 crosscheck.py
PASS  accuracy_white         encoded=     87.25  decoded=87.25
PASS  effective_rating       encoded=      2040  decoded=2040
PASS  tactics_change         encoded=       -60  decoded=-60
PASS  negative_cp            encoded=      -310  decoded=-310
...
23/23 cross-checks passed — libprotobuf frame was 362 bytes
```

That is the evidence that the schema in this document is right, independent of
chess.com being reachable.

### 10.4 No-network statement

This sandbox has no route to chess.com and no account. Every claim above is
from static analysis of the downloaded bundles, every formula was executed
locally (Node), and every schema was validated against libprotobuf offline.

---

## 11. What is computed where

| Number the user sees | Producer | Where in the bundle |
| --- | --- | --- |
| Accuracy % | server, CAPS2 | `highlights.accuracy` → `pqe()` 1,699,347 |
| Elo estimate | server, report card | `report_card.*.gameRatingV2` → `jqe()` 1,701,418 |
| Per-phase accuracy | server | `reports_by_phase[].accuracy` |
| Per-category rating + delta | server | `reports_by_category[].new_rating / rating_change` |
| Move classification | server | `Move.move_classification`, `EvalGraphTick` |
| Tally counts | server | `ClassificationTallies` |
| Eval graph points | server | `EvalGraph.eval_graph_ticks[].move_score` |
| Explanation sentences | server (CEE), pre-rendered | `Move.speech`, `explain_line` |
| Arrows / highlights | server | `BoardMarkings` |
| Annotated PGN | server | `Metadata.annotated_pgn` |
| "Winning / better / equal" band | **client** | `xSt()` 2,768,546 |
| Which sentence variant | **client** | `ESt()` + 10-key (downgrade) table |
| Show-or-hide the report card | **client** | `vp()` in `tab-review...` |

One line: the client owns **word choice and visibility**, the server owns
**every number**.

---

## 12. What this means for the eval-bar extension

Nothing here changes the extension, and nothing here should. The extension
drives the *live board's* `wc-evaluation-bar`, which is a different code path:
that bar is fed by a local Stockfish worker and `onEvaluationUpdate({score,
mateIn, depth})`, not by CEAC. The premium review is a batched, server-side,
post-game product.

Three things are worth borrowing:

1. **`Engine.TORCH_HUMAN` explains the "Great/Brilliant" mystery.** Those badges
   are not thresholds on centipawn loss; they come from an engine that models
   plausible human moves. A local Stockfish bar will never reproduce them, and
   it should not try.
2. **The rating-scaled bands (§7.2) are a genuinely good idea for the hover
   preview.** "How big an advantage counts as winning" genuinely depends on the
   level of play. The band table is already inverted for us: 2.77 pawns at 2000,
   1.93 at 2800. It is a sentence-picker, so it must stay out of the numeric
   readout — but it is a defensible way to choose a *colour* for a hover cue.
3. **The `Score` message is the one convention to keep.** Everything is
   `score_centipawns_white` — always White's point of view, never the side to
   move's. The extension already normalises this way; the premium stack proves
   it is the house style.

---

## 13. Appendix: files

| Path | What |
| --- | --- |
| `PREMIUM-ANALYSIS.md` | this document |
| `CLIENT-SIDE.md` | inventory of everything that runs in the browser + what was extracted |
| `schemas/*.proto` | 28 extracted schemas, package-prefixed |
| `ALL-SCHEMAS.proto` | all 422 descriptors rendered (12,971 lines) |
| `client/` | extracted tables + `analysis-client.mjs` + 100-check test |
| `tools/ceac-dump.mjs` | dependency-free frame decoder + 20-check selftest + fixture writer |
| `tools/protoread.py` | descriptor → `.proto` renderer |
| `tools/extract-client-tables.py` | regenerates `client/*.json` from the bundles |
| `crosscheck/` | libprotobuf round-trip proof (23 checks) |

The raw bundles (`raw/`) and descriptor blobs (`proto/`) were deleted to keep
the workspace small; both are re-derivable — see `REDOWNLOAD.md`. The rendered
schemas, the extracted tables and the tests were kept, so everything that
*proves* the claims still runs offline.

### Offsets cited above

All are character offsets into `chunks/shared.eager.BOGLllgUUR.chunk.js`
(3,660,286 bytes) unless stated.

| Offset | Symbol |
| --- | --- |
| 315,764 | `af()` unlimited-review entitlement |
| 327,157 | `Om()` locked-takeaway check |
| 522,636 | `wdl()` rating → win/draw/loss model |
| 1,133,145 | empty CAPS / tallies accumulator |
| 1,699,347 | `pqe()` accuracy → UI |
| 1,701,418 | `jqe()` report card → UI |
| 1,711,579 | `AJe()` response → gameProps |
| 1,812,384 | `EW.Urls` endpoint table |
| 1,813,143 | `M4e()` report-card entitlement |
| 1,813,265 | `P4e()` depth → strength |
| 1,814,722 | `W4e()` request builder |
| 1,836,513 | `C3e()` frame decoder |
| 2,768,245 | `ySt()` band → pawn thresholds |
| 2,768,546 | `xSt()` move → band classifier |
| 46,853 / 47,090 / 49,042 | `tab-review...`: rating display rules, tooltip text |
