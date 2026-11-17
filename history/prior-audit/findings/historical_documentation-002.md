# historical_documentation — findings 101–200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-00101"></a>
## FND-00101: 2. Where the premium line actually is — block 94

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
vp = (e) => flag && e.gameRatingV2 !== undefined;   // 46,853 — show at all?
yp = (e) => e.gameRatingV2 || e.effectiveElo;       //      — which number wins
xp = (e) => e.gameRatingV2 === 0
    ? 'There were not enough moves to rate this game.'
    : `Old Game Rating: ${...}`;                    // 47,090
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 94–100.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00102"></a>
## FND-00102: 2. Where the premium line actually is — block 102

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Note the two names: `gameRatingV2` is the current model, `effectiveElo` /
"Old Game Rating" is the legacy one, kept as a fallback. **`gameRatingV2`
takes precedence when present**, including when it is `0` — a legitimate
"too few moves" answer, not a missing value.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 102–105.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00103"></a>
## FND-00103: 2. Where the premium line actually is — block 107

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 107–107.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00104"></a>
## FND-00104: 3.1 Endpoints — block 113

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

All recovered from the `EW.Urls` table at offset **1,812,384**:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 113–113.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00105"></a>
## FND-00105: 3.1 Endpoints — block 115

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Key | URL | Feature flag that selects it |
| --- | --- | --- |
| `ProdServerIDLGameReview` | `wss://analysis.chess.com:443/v2/game-review` | default |
| `StagingServerIDLGameReview` | `wss://analysis-staging.chess.com:443/v2/game-review` | `analysis_staging_server_idl` |
| `SandboxServerIDLGameReview` | `wss://analysis-sandbox.chess.com:443/v2/game-review` | `analysis_sandbox_server_idl` |
| `ProdServerIDLRunSearch` | `wss://analysis.chess.com:443/v2/run-search` | — |
| `StagingServerIDLRunSearch` | `wss://analysis-staging.chess.com:443/v2/run-search` | — |
| `NewMax` | `wss://max-analysis.prod.chess-platform.com:443` | maximum-strength analysis |
| `StagingMax` | `wss://max-analysis.staging.chess-platform.com:443` | — |

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 115–123.

**Source references:** SRC-2047  
**URL references:** <wss://analysis-sandbox.chess.com:443/v2/game-review>, <wss://analysis-staging.chess.com:443/v2/game-review>, <wss://analysis-staging.chess.com:443/v2/run-search>, <wss://analysis.chess.com:443/v2/game-review>, <wss://analysis.chess.com:443/v2/run-search>, <wss://max-analysis.prod.chess-platform.com:443>, <wss://max-analysis.staging.chess-platform.com:443>  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00106"></a>
## FND-00106: 3.1 Endpoints — block 125

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Selector (`O4e()`, same offset):

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 125–125.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00107"></a>
## FND-00107: 3.1 Endpoints — block 127

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
function O4e() {
  if (features.includes('analysis_sandbox_server_idl')) return EW.Types.SandboxServerIDLGameReview;
  if (features.includes('analysis_staging_server_idl') || isStaging()) return EW.Types.StagingServerIDLGameReview;
  return EW.Types.ProdServerIDLGameReview;
}
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 127–133.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00108"></a>
## FND-00108: 3.1 Endpoints — block 135

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Note the host split: `analysis.chess.com` for game review and position search,
`max-analysis.prod.chess-platform.com` for the deep "Maximum" engine. Two
different servers, two different jobs.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 135–137.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00109"></a>
## FND-00109: 3.1 Endpoints — block 139

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

There is also a same-origin override used by the dev harness —
`window.chesscom.analysis.ceacSocketSameOrigin` — which rewrites the socket URL
to the page origin (`l3e()`). That is the hook worth knowing if you ever want
to run your own analysis server locally.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 139–142.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00110"></a>
## FND-00110: 3.2 Framing — block 146

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

One WebSocket, binary frames, one protobuf message per frame. The client sets
`binaryType = 'arraybuffer'` and each frame is decoded as a
`GameReviewResponse` (`C3e()`, offset 1,836,513):

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 146–148.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00111"></a>
## FND-00111: 3.2 Framing — block 150

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
e.onmessage = (ev) => {
  if (!(ev.data instanceof ArrayBuffer)) return;
  let a;
  try { a = Mk(OH, new Uint8Array(ev.data)); }       // OH = GameReviewResponse
  catch { /* logs "Invalid response from analysis server." and closes */ }
  SW('info', `IDL /v2/game-review frame (...)`)       // every frame is logged
};
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 150–158.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00112"></a>
## FND-00112: 3.2 Framing — block 160

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The connection has a **10 s timeout** (`k3e = 1e4`) — much shorter than a review
takes, so it guards the *handshake*, not the stream.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 160–161.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00113"></a>
## FND-00113: 3.3 Liveness on a long stream — block 165

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The request asks for `heartbeatIntervalSeconds: 5`, and the server answers with
`GameReviewResponse.heartbeat` frames while it works. When the fleet is busy it
sends `waiting_for_capacity` instead — that is the "there are a few people
ahead of you" message. Progress arrives as `progress { float progress }`, which
drives the progress bar.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 165–169.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00114"></a>
## FND-00114: 3.4 The other socket — block 173

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`run-search` also exists as a **plain JSON** socket, used by the board's own
analysis mode rather than Game Review:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 173–174.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00115"></a>
## FND-00115: 3.4 The other socket — block 176

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```json
{ "id": "...", "fen": "...", "uciMoves": ["e2e4"] }
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 176–178.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00116"></a>
## FND-00116: 3.4 The other socket — block 180

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

with `heartbeat` and `waitingForCapacity` JSON messages. Same server, same
routing, no protobuf. If you only want *an evaluation* rather than a review,
this is the simpler interface.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 180–182.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00117"></a>
## FND-00117: 3.4 The other socket — block 184

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 184–184.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00118"></a>
## FND-00118: 4. The request, field by field — block 188

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Reconstructed from `W4e()` at offset **1,814,722**. This is the entire
construction, only renamed:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 188–189.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00119"></a>
## FND-00119: 4. The request, field by field — block 191

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 191–254.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00120"></a>
## FND-00120: 4.1 Engine selection (two-tier) — block 258

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
function pickEngine() {
  if (!feature('web_analysis_torch_human_v2')) return Engine.SF16_1_NNUE;
  return fullAnalysisEngine === 'stockfish16' ? Engine.SF16_1_NNUE : Engine.TORCH_HUMAN;
}
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 258–263.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00121"></a>
## FND-00121: 4.1 Engine selection (two-tier) — block 265

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`Engine` enum (from `chesscom/engine/v1`):

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 265–265.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00122"></a>
## FND-00122: 4.1 Engine selection (two-tier) — block 267

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```
1 SF12   2 SF15   3 SF15_NNUE   4 SF15_1   5 SF15_1_NNUE   6 SF16_NNUE
7 SF9_FAIRPLAY_V1   8 DRAGON_3_3   9 KOMODO_3_3   10 SF16_1_NNUE
11 TORCH_3   12 TORCH_HUMAN   13 SF18_NNUE
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 267–271.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00123"></a>
## FND-00123: 4.1 Engine selection (two-tier) — block 273

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**`TORCH_HUMAN` is the interesting one.** It is a human-like engine, and its
presence switches the evaluator off the game-state cache
(`useGameStateCache = engine !== TORCH_HUMAN`) — human-like evaluations are not
reusable between related positions, because the whole point is that they are
*not* objectively best. This is what makes "Great" and "Brilliant" findable:
a move a human would find but an engine would not is not scored as a blunder.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 273–278.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00124"></a>
## FND-00124: 4.2 Depth — block 282

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Four named strengths, mapped from a numeric depth by `P4e()` at offset
**1,813,265**:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 282–283.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00125"></a>
## FND-00125: 4.2 Depth — block 285

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| Page depth | Strength | Meaning |
| --- | --- | --- |
| 18 | `STRENGTH_FAST` | quick review |
| 22 | `STRENGTH_STANDARD` | default |
| 24 | `STRENGTH_DEEP` | "Deep" |
| 26 | `STRENGTH_MAXIMUM` | "Maximum" — the only one routed to `max-analysis.prod.chess-platform.com` |
| anything else | `STRENGTH_FAST` | fallback |

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 285–291.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00126"></a>
## FND-00126: 4.3 Envelope types — block 295

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`GameReviewRequest` (`chesscom/ceac/v2/game_review.proto`) — note the gaps in
field numbers, which is where the newer features were bolted on:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 295–296.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00127"></a>
## FND-00127: 4.3 Envelope types — block 298

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 298–310.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00128"></a>
## FND-00128: 4.3 Envelope types — block 312

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`Product` enum tells the server what to bill and what to enable:
`GAME_REVIEW=2`, `INSIGHTS=3`, `ADVANCED_STATS=8`, `BRILLIANT_VERIFICATION=12`,
`TRAIN=13`. `Client` is `WEB=1`, `TRAIN=17`, etc.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 312–314.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00129"></a>
## FND-00129: 4.3 Envelope types — block 316

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 316–316.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00130"></a>
## FND-00130: 5. The response tree — block 320

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

One `GameReviewResponse` per frame; fields 1–5 are a oneof (`progress`,
`success`, `failure`, `heartbeat`, `waiting_for_capacity`). The payload arrives
in `success.game_review`:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 320–322.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00131"></a>
## FND-00131: 5. The response tree — block 324

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 324–348.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00132"></a>
## FND-00132: 5. The response tree — block 350

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`Review.played_moves` is the per-move detail the board renders:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 350–350.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00133"></a>
## FND-00133: 5. The response tree — block 352

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 352–372.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00134"></a>
## FND-00134: 5. The response tree — block 374

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`Score` is the shared currency everywhere (`chesscom/chess/v1/score.proto`):

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 374–374.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00135"></a>
## FND-00135: 5. The response tree — block 376

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```proto
message Score {
  sint32 score_centipawns_white = 1;   // always white's point of view
  int32  mate_in_white          = 2;
  int32  mate_in_black          = 3;
  Stalemate stalemate           = 4;
}
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 376–383.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00136"></a>
## FND-00136: 5. The response tree — block 385

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The client immediately converts it to pawns (`zU()`, offset ≈ 1,699,000):
`cp = score_centipawns_white / 100` (`Tqe = 100`), mate → `±1000` (`wqe = 1e3`).

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 385–386.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00137"></a>
## FND-00137: 5.1 Response → UI — block 390

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`AJe()` at offset **1,711,579** is the whole mapping. It is short because the
server has already done the analysis:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 390–391.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00138"></a>
## FND-00138: 5.1 Response → UI — block 393

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 393–404.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00139"></a>
## FND-00139: 5.1 Response → UI — block 406

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

and

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 406–406.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00140"></a>
## FND-00140: 5.1 Response → UI — block 408

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
function toCaps(acc) {                              // offset 1,699,347
  return {
    white: { ...EMPTY_CAPS, all: acc?.white ?? 0 },  // {all,B,K,N,P,Q,R}
    black: { ...EMPTY_CAPS, all: acc?.black ?? 0 },
  };
}
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 408–415.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00141"></a>
## FND-00141: 5.1 Response → UI — block 417

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**The headline accuracy is `highlights.accuracy.{white,black}` verbatim.** No
client-side recomputation. The per-piece `B/K/N/P/Q/R` slots exist in the model
and are filled from `ColorAccuracy.accuracy_by_piece_type` when the detailed
accuracy payload is present.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 417–420.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00142"></a>
## FND-00142: 5.1 Response → UI — block 422

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 422–422.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00143"></a>
## FND-00143: 6.1 CAPS2 — block 428

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`chesscom/explanation_engine/v1/accuracy.proto` names the algorithm outright:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 428–428.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00144"></a>
## FND-00144: 6.1 CAPS2 — block 430

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 430–445.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00145"></a>
## FND-00145: 6.1 CAPS2 — block 447

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

So **CAPS2** is the name of the accuracy model ("Chess.com Accuracy
Percentage Score", v2). It is fed by average centipawn loss — the schema says
so explicitly — but the transform from loss to a 0–100 score happens on the
server. The client never sees the loss for the report card, only
`accuracy_overall`.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 447–451.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00146"></a>
## FND-00146: 6.1 CAPS2 — block 453

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The tooltip text in the UI (offset 49,042 of `tab-review...`) describes it as a
score "from 0-100 when compared to the top chess computer moves".

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 453–454.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00147"></a>
## FND-00147: 6.1 CAPS2 — block 456

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Feature key **280** (`FEATURE_ID_INTERNAL_FEATURE_CAPS2 = 280`) gates the rollout, and
`cee_c_api_calls` in the response echoes which explanation endpoints ran.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 456–457.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00148"></a>
## FND-00148: 6.2 What accuracy is *not* — block 461

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

There is no client-side formula for accuracy. Searching the 3.66 MB bundle for
`centipawn`, `winPercent`, `expectedScore`, `performanceRating` returns
**nothing**. The only `Math.exp` / `Math.log` expressions in the analysis code
are the two rating models in §7 — one for *display* (W/D/L), one for *speech
bands*.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 461–465.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00149"></a>
## FND-00149: 6.2 What accuracy is *not* — block 467

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 467–467.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00150"></a>
## FND-00150: 7. Elo prediction — block 471

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

There are two completely separate systems. Conflating them is the usual mistake.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 471–471.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00151"></a>
## FND-00151: 7.1 The real one: the server report card — block 475

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 475–495.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00152"></a>
## FND-00152: 7.1 The real one: the server report card — block 497

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The client's job (`jqe()`, offset **1,701,418**) is a straight copy plus a
"is it empty" test:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 497–498.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00153"></a>
## FND-00153: 7.1 The real one: the server report card — block 500

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 500–511.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00154"></a>
## FND-00154: 7.1 The real one: the server report card — block 513

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Phase keys are `GAME_PHASE_OPENING → 'gp0'`, `MIDDLEGAME → 'gp1'`,
`ENDGAME → 'gp2'`. Categories are renamed
`OPENING_CATEGORY → 'Opening'`, `TACTICS_CATEGORY → 'Tactics'`,
`STRATEGY_CATEGORY → 'Strategy'`, `ENDGAME_CATEGORY → 'Endgame'`; a missing
`performance` defaults to `'good'`.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 513–517.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00155"></a>
## FND-00155: 7.1 The real one: the server report card — block 519

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**What can be stated from the bundles:** the server returns one rating for the
game (`game_rating_v2`), a legacy one (`effective_rating`), and a per-category
figure with a *signed* change. Because `rating_change` is signed and
per-category, the card can say "+45 in the Opening, −60 in Tactics" — a
breakdown, not a single delta.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 519–523.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00156"></a>
## FND-00156: 7.1 The real one: the server report card — block 525

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**What cannot be stated:** the mapping from evaluations to a rating is not in
any shipped file. There is no formula to recover, no constant to read, and no
client-side recomputation to intercept — the three fields are copied straight
out of the response. Any claim about *how* the number is derived (percentile
over recent games, a performance-rating transform, an NN) would be guesswork.
What is verifiable is the interface: given these fields, the UI shows a rating;
without `game_rating_v2`, it shows the legacy number or nothing at all.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 525–531.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00157"></a>
## FND-00157: 7.2 The decoy: the client-side W/D/L model — block 535

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`b(e, t)` at offset **522,636** is a real, self-contained rating→result model.
It appears in the shared chunk, which is why it is easy to mistake for the
"Elo prediction":

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 535–537.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00158"></a>
## FND-00158: 7.2 The decoy: the client-side W/D/L model — block 539

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 539–552.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00159"></a>
## FND-00159: 7.2 The decoy: the client-side W/D/L model — block 554

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Measured output (`node crosscheck/wdl.mjs`):

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 554–554.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00160"></a>
## FND-00160: 7.2 The decoy: the client-side W/D/L model — block 556

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| White | Black | win | draw | loss | White score |
| --- | --- | --- | --- | --- | --- |
| 2000 | 2000 | 0.573 | 0.026 | 0.401 | 0.586 |
| 2400 | 2000 | 0.916 | 0.025 | 0.059 | 0.929 |
| 2000 | 1200 | 0.996 | 0.004 | 0.000 | 0.998 |
| 2800 | 2000 | 0.971 | 0.029 | 0.000 | 0.986 |
| 1200 | 2000 | 0.027 | 0.016 | 0.958 | 0.034 |

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 556–562.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00161"></a>
## FND-00161: 7.2 The decoy: the client-side W/D/L model — block 564

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

A 400-point gap gives a 0.93 expected score, and a 2000-vs-2000 game is a
slightly-better-than-coin-flip (0.586) — this is fitted to *fast time-control
online chess*, where decisive games are the norm and draws are rare. The
draw term collapsing to ~2.6% is the signature: it is not the classical Elo
curve.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 564–568.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00162"></a>
## FND-00162: 7.2 The decoy: the client-side W/D/L model — block 570

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Where it is used: **nowhere near the report card.** `ySt()` / `xSt()`
(offsets 2,768,245 and 2,768,546) turn this into five *confidence bands* and
pick one of 10 canned sentences:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 570–572.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00163"></a>
## FND-00163: 7.2 The decoy: the client-side W/D/L model — block 574

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```js
const BANDS = { Winning: 0.2, Better: 0.4, Equal: 0.5, Worse: 0.65, Losing: 0.8 };  // for White
// for Black the same map is mirrored: 0.8, 0.65, 0.5, 0.4, 0.2

function evalThreshold(probability, rating) {
  // invert a logistic fitted to the rating scale, then rescale to pawns
  return Math.log(1 / probability - 1) / (0.004 * ((0.0685 * rating - 12) / 100)) / 100;
}
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 574–582.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00164"></a>
## FND-00164: 7.2 The decoy: the client-side W/D/L model — block 584

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`rating` = **max(WhiteElo, BlackElo)**, defaulting to 2000 (`M4 = 2e3`). The
result is in **pawns** (the score it is compared against was divided by 100 in
§5). Measured (`node crosscheck/rating-bands.mjs`):

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 584–586.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00165"></a>
## FND-00165: 7.2 The decoy: the client-side W/D/L model — block 588

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

| max rating | Winning | Better | Equal | Worse | Losing |
| --- | --- | --- | --- | --- | --- |
| 800 | +8.10 | +2.37 | 0.00 | −3.62 | −8.10 |
| 1200 | +4.94 | +1.44 | 0.00 | −2.20 | −4.94 |
| 1600 | +3.55 | +1.04 | 0.00 | −1.59 | −3.55 |
| 2000 | +2.77 | +0.81 | 0.00 | −1.24 | −2.77 |
| 2400 | +2.27 | +0.67 | 0.00 | −1.02 | −2.27 |
| 2800 | +1.93 | +0.56 | 0.00 | −0.86 | −1.93 |

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 588–595.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00166"></a>
## FND-00166: 7.2 The decoy: the client-side W/D/L model — block 597

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 597–606.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00167"></a>
## FND-00167: 7.2 The decoy: the client-side W/D/L model — block 608

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

**This produces prose, never a rating.** It is the mechanism behind the
"coach" voice, and it is the only piece of analysis logic that ships to the
browser.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 608–610.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00168"></a>
## FND-00168: 7.2 The decoy: the client-side W/D/L model — block 612

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 612–612.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00169"></a>
## FND-00169: 8. Move classifications — block 616

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 616–626.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00170"></a>
## FND-00170: 8. Move classifications — block 628

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The phase-split variants exist so a middlegame mistake and an opening
inaccuracy can carry different weights in the accuracy model and different
sentences. The UI collapses them back to the base class for the glyph.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 628–630.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00171"></a>
## FND-00171: 8. Move classifications — block 632

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The 19 visible badges map to: `Brilliant, GreatFind, Tricky, Book, BestMove,
Excellent, Good, Inaccuracy, Mistake, Miss (rendered "Missed"), Blunder,
Forced`, plus `MissedWin`. "Tricky" is not in the enum — it is a *charm*
inference label (requested via `charmInfReq`, §4), gated by the `cee_tricky_classification` feature flag,
which is why it can be absent from older reviews.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 632–636.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00172"></a>
## FND-00172: 8. Move classifications — block 638

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Per-side tallies come from `ClassificationTallies`:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 638–638.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00173"></a>
## FND-00173: 8. Move classifications — block 640

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```proto
message ClassificationTally { MoveClassification move_classification = 1; int32 tally = 2; }
message ClassificationTallies { repeated ClassificationTally white = 1; repeated ClassificationTally black = 2; }
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 640–643.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00174"></a>
## FND-00174: 8. Move classifications — block 645

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The UI's local accumulator (offset **1,133,145**) shows the full set of counters
a game can report, including the phase splits and per-piece split:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 645–646.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00175"></a>
## FND-00175: 8. Move classifications — block 648

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 648–659.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00176"></a>
## FND-00176: 8. Move classifications — block 661

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`GP0/GP1/GP2` are the opening / middlegame / endgame splits. And
`engine: SF16_1_NNUE` appears alongside them, so each review records which
engine produced it — a review made by `TORCH_HUMAN` is not numerically
comparable to one made by Stockfish.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 661–664.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00177"></a>
## FND-00177: 8. Move classifications — block 666

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 666–666.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00178"></a>
## FND-00178: 9.1 Advanced stats — 102 categories — block 672

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`AdvancedStatType` is the premium stats taxonomy. Structure, not a flat list:
five namespaces × what you did / what you allowed:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 672–673.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00179"></a>
## FND-00179: 9.1 Advanced stats — 102 categories — block 675

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 675–688.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00180"></a>
## FND-00180: 9.1 Advanced stats — 102 categories — block 690

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Percentiles are per-user aggregates:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 690–690.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00181"></a>
## FND-00181: 9.1 Advanced stats — 102 categories — block 692

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 692–701.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00182"></a>
## FND-00182: 9.1 Advanced stats — 102 categories — block 703

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

That two-sided structure is why the same stat can read "you are in the 71st
percentile" and "this game you scored below your average" at the same time.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 703–704.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00183"></a>
## FND-00183: 9.2 Skills and the validation hash — block 708

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```proto
message SkillsPosition {
  int32  ply             = 1;
  repeated Skill skills  = 2;     // 73 values
  string validation_hash = 3;     // signed by CEE
}
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 708–714.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00184"></a>
## FND-00184: 9.2 Skills and the validation hash — block 716

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

73 skills, e.g. `SKILL_FORK=21`, `SKILL_ROYAL_FORK=31`,
`SKILL_BRILLIANT_SACRIFICE=37`, `SKILL_OPPOSITION=65`,
`SKILL_ROOK_BEHIND_OWN_PASSED_PAWN=64`. These are what the step-by-step
explanation shows ("this move develops a piece with tempo") and they feed
puzzles.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 716–720.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00185"></a>
## FND-00185: 9.2 Skills and the validation hash — block 722

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`validation_hash` is the anti-tamper mechanism: the server signs which skills it
awarded, so a client cannot claim skills it did not earn. The client logs this
explicitly when the ids CEE needs are missing:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 722–724.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00186"></a>
## FND-00186: 9.2 Skills and the validation hash — block 726

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```
'0/3 IDL /v2/game-review — skills on; CEE has the ids to sign validationHash'
'0/3 IDL /v2/game-review — skills on but MISSING ids CEE needs; validationHash will come back empty'
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 726–729.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00187"></a>
## FND-00187: 9.2 Skills and the validation hash — block 731

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

CEE needs **white user id, black user id and game id** to sign. A game without
all three (guest, anonymous import) gets an empty hash and therefore no
persisted skill credit.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 731–733.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00188"></a>
## FND-00188: 9.3 Explanations — block 737

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`AnalysisType` has 300 values (`ANALYSIS_TYPE_FORK`, `..._SKEWER`,
`..._DIRECT_SACRIFICE_CAPTURE`, `..._IGNORES_THREAT`, `..._ZUGZWANG` …). They are
the taxonomy behind `Move.speech` and `explain_line`, which arrives as
**pre-rendered text**, not as a template to fill:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 737–740.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00189"></a>
## FND-00189: 9.3 Explanations — block 742

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```proto
message PlayedMove {
  repeated PlayedMove explain_line = 7;   // literal alternatives: a b c d
}
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 742–746.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00190"></a>
## FND-00190: 9.3 Explanations — block 748

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

The client picks one (`ESt()` builds the 10 downgrade keys like `WinningBetter`, and the
sentences are already localised, with `%color%` placeholders). Explanation
generation is a separate service reached by `cee_c_api_calls`, with feature
keys `ADVANCED_STATS_CATEGORY_SPEECH=279`, `GET_COACH_EMOTION=281`,
`GENERATE_COACH_TEXT_ITEMS=282`.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 748–752.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00191"></a>
## FND-00191: 9.3 Explanations — block 754

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

---

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 754–754.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00192"></a>
## FND-00192: 10. Verifying this yourself — block 758

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Nothing below requires an account, and none of it runs from this sandbox.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 758–758.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00193"></a>
## FND-00193: 10.1 Capture a real frame (on your own machine, your own account) — block 762

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

1. Open DevTools → Network → WS, tick **Preserve log**.
2. Go to `https://www.chess.com/analysis/game/live/<your-game-id>` and press
   **Game Review**.
3. Click the `wss://analysis.chess.com/443/v2/game-review` entry. You will see
   frames come in as binary. The `success` frame is the one you want.
4. Right-click → *Copy message* → *Copy as binary* (Chrome) or use
   `copy(new Uint8Array(...))`. Save it as `frame.bin`.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 762–768.

**Source references:** SRC-2047  
**URL references:** <https://www.chess.com/analysis/game/live/>, <wss://analysis.chess.com/443/v2/game-review>  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00194"></a>
## FND-00194: 10.1 Capture a real frame (on your own machine, your own account) — block 770

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

Or, more reliably, paste this in the console *before* starting the review and
copy the base64 it prints:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 770–771.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00195"></a>
## FND-00195: 10.1 Capture a real frame (on your own machine, your own account) — block 773

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 773–788.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00196"></a>
## FND-00196: 10.2 Decode it — block 792

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```bash
node tools/ceac-dump.mjs frame.bin             # human-readable tree
node tools/ceac-dump.mjs frame.bin --json      # machine-readable
node tools/ceac-dump.mjs --selftest            # 20 checks, no network
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 792–796.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00197"></a>
## FND-00197: 10.2 Decode it — block 798

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

A `success` frame prints, in outline:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 798–798.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00198"></a>
## FND-00198: 10.2 Decode it — block 800

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

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

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 800–819.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00199"></a>
## FND-00199: 10.2 Decode it — block 821

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

`--selftest` writes a synthetic frame byte-by-byte and asserts 20 decoded
values including a `sint32` of −310, a 10-byte sign-extended negative `int32`,
enum names, floats and repeated fields. It passes offline:

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 821–823.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.

<a id="FND-00200"></a>
## FND-00200: 10.2 Decode it — block 825

**Category:** historical_documentation  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Faithful recovery of a historical documentary claim. It may be correct, inferred, superseded, or unsupported; see curated findings and contradictions.

```
20/20 checks passed — fixture is 300 bytes
```

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Lines 825–827.

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** This block is preserved verbatim after privacy redaction. Its presence does not independently verify the technical assertion.
