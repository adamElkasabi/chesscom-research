# business_logic — findings 1–7

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18905"></a>
## FND-18905: Numeric page depths select named strength

**Category:** business_logic  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

P4e maps18->Fast,22->Standard,24->Deep,26->Maximum; fallback Fast. Strength enum is1/2/3/4. A depth menu selection is not a guarantee the engine searches every position to that exact depth.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1813037.

```text
window.chesscom.features.includes(`game_review_platinum_report_card`)&&af()}var N4e=r((()=>{of()}));function P4e(e){switch(e){case 18:return mN.Strength.Fast;case 22:return mN.Strength.Standard;case 24:return mN.Strength.Deep;case 26:return mN.Strength.Maximum;default:return mN.Strength.Fast}}var F4e=r((()=>{hN()})),I4e,L4e=r((()=>{iD(),V(),gh(),I4e=class extends hd{constructor(...e){super(...e),R(this,`fen`,``),R(th
```
- **SRC-0334** `research/proto/chesscom/engine/v1/strength.proto` — [preserved redacted evidence](../evidence/text/f0ea702032bf270096aea4a69dc474d0d4f5e606859f45fd3430db4183ecf398.proto)

**Source references:** SRC-1137, SRC-0334  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117, FND-02520, FND-02521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18906"></a>
## FND-18906: Torch Human engine selection is feature-gated

**Category:** business_logic  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

A4e checks web_analysis_torch_human_v2. With the flag, Stockfish16 selection yields SF16_1_NNUE, other selection yields TORCH_HUMAN; without it, SF16_1_NNUE. W4e sets useGameStateCache false for TORCH_HUMAN. The causal reason for disabling cache is not proved by that expression.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1812692.

```text
)?EW.Types.StagingServerIDLGameReview:EW.Types.ProdServerIDLGameReview}var k4e=r((()=>{Gf(),DW()}));function A4e(e){return window.chesscom.features.includes(`web_analysis_torch_human_v2`)?e===sP.Engine.FullAnalysisOptions.Stockfish16?sA.SF16_1_NNUE:sA.TORCH_HUMAN:sA.SF16_1_NNUE}var j4e=r((()=>{gj(),EM(),cP(),mP(),gP()}));function M4e(){return window.chesscom.features.includes(`game_review_platinum_report_card`)&&af()
```

**Source references:** SRC-1137  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18907"></a>
## FND-18907: Report-card entitlement modifies request options

**Category:** business_logic  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

M4e combines game_review_platinum_report_card and af(); af checks analysis.hasUnlimitedReview and non-Diamond state. W4e carries reportCardEntitled/includeTrainTakeaways/canAccessLockedTakeaways. Client flags do not establish a server authorization bypass.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1812915.

```text
tockfish16?sA.SF16_1_NNUE:sA.TORCH_HUMAN:sA.SF16_1_NNUE}var j4e=r((()=>{gj(),EM(),cP(),mP(),gP()}));function M4e(){return window.chesscom.features.includes(`game_review_platinum_report_card`)&&af()}var N4e=r((()=>{of()}));function P4e(e){switch(e){case 18:return mN.Strength.Fast;case 22:return mN.Strength.Standard;case 24:return mN.Strength.Deep;case 26:return mN.Strength.Maximum;default:return mN.Strength.Fast}}var 
```
- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)

**Source references:** SRC-1137, SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117, FND-00085, FND-00086

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18908"></a>
## FND-18908: Displayed Game Rating is not the WDL model

**Category:** business_logic  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

The report-card adapter copies native effectiveRating/gameRatingV2. The WDL/confidence-band arithmetic affects prose/bands, not a proven rating-generation algorithm. An old claim that no shipped file can calculate rating is superseded by the executable CEE WASM producing effectiveRating locally.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1701055.

```text
rn UU;let{data:t,glyphs:n}=kqe(e.reportsByPhase),r=Aqe(e.reportsByCategory),i=e.effectiveRating??0,{gameRatingV2:a}=e;return t.length===0&&r.length===0&&i===0&&a===void 0?UU:{effectiveElo:i,gameRatingV2:a,data:t,glyphs:n,categories:r}}function Mqe(e){return e?{white:jqe(e.white),black:jqe(e.black),speech:e.speech??``}:Nqe}var UU,Nqe,Pqe,Fqe,Iqe,Lqe=r((()=>{iD(),rU(),HU(),Xp(),UU={effectiveElo:0,data:[],glyphs:{},cate
```
- **SRC-0049** `extension/lib/review.js` — [preserved redacted evidence](../evidence/text/5f056d321e317d758a6d9882be84d2b32b60555244d92454645b7c2f3229f21d.js)
  Character offset 3215.

```text
uracy || {},
    tallies: highlights.classificationTallies || {},
    ratings: { white: card.white?.gameRatingV2 ?? card.white?.effectiveRating,
      black: card.black?.gameRatingV2 ?? card.black?.effectiveRating },
    ratingSources,
    opening: gameReview.opening?.openingName || null,
    ceeVersion: gameReview.metadata?.ceeVersion,
    speechSentences, audioHashes, explanationArrows,
  };
}

/** Build the exact 
```
- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Character offset 4662.

```text
ng out a CSS blur.

The UI side confirms it (`tab-review...chunk.js`):

```js
vp = (e) => flag && e.gameRatingV2 !== undefined;   // 46,853 — show at all?
yp = (e) => e.gameRatingV2 || e.effectiveElo;       //      — which number wins
xp = (e) => e.gameRatingV2 === 0
    ? 'There were not enough moves to rate this game.'
    : `Old Game Rating: ${...}`;                    // 47,090
```

Note the two names: `gameRatin
```

**Source references:** SRC-1137, SRC-0049, SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117, FND-18888, FND-18889

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18909"></a>
## FND-18909: CAPS2 schema does not establish its mathematical dependency

**Category:** business_logic  
**Classification:** inference  
**Verification:** partially verified  
**Confidence:** high — The schema declaration is direct; the limitation is logical: fields alone do not establish causation.

AccuracyAlgorithm includes CAPS2; ColorAccuracy carries accuracy_overall and avg_centipawn_loss. Coexistence of these fields does NOT prove accuracy is a simple transform of average centipawn loss, nor reveal the exact native algorithm. Preserve older stronger claims as unverified.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Character offset 16646.

```text
ccuracy_by_piece_type` when the detailed
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
  repeated GamePhaseAc
```
- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 201.

```text
ion_engine.v1;

enum AccuracyAlgorithm {
  ACCURACY_ALGORITHM_UNSPECIFIED = 0;
  ACCURACY_ALGORITHM_CAPS2 = 1;
}

message PieceTypeAccuracy {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double accuracy_score = 2;
}

message GamePhaseAccuracy {
  optional .chesscom.chess.v1.GamePhase game_phase = 1;
  optional double accuracy_score = 2;
}

message ColorAccuracy {
  optional .chesscom.chess.v1.Co
```

**Source references:** SRC-2047, SRC-0335  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087, FND-02526, FND-02527

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18910"></a>
## FND-18910: WDL model constants preserved without conflating their role

**Category:** business_logic  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Historical document records arctan win/loss coefficients0.20773843,2.49085889,2.47841945 and0.20720905,2.49626837,2.48220286; draw term uses exp and normalization w+l+d. Full exact formula and computed tables remain preserved in original document blocks, not substituted for native Game Rating.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Character offset 21252.

```text
nction wdl(whiteElo, blackElo) {
  const e = whiteElo / 100, t = blackElo / 100;
  const w = clamp( 0.20773843 * Math.atan(2.49085889*e - 2.47841945*t)
                 + 0.02262979*e - 0.02256839*t + 0.52239679, 0, 1);
  const l = clamp(-0.20720905 * Math.atan(2.49626837*e - 2.48220286*t)
                 - 0.02352551*e + 0.02172627*t + 0.49443923, 0, 1);
  const d = clamp( Math.exp(0.037043456*e + 0.178106427*t - 8
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)

**Source references:** SRC-2047, SRC-1137  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087, FND-18108, FND-18109

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18911"></a>
## FND-18911: Rating confidence-band inverse-logistic formula

**Category:** business_logic  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Historical source describes log(1/probability-1)/(0.004*((0.0685*rating-12)/100))/100, with rating=max(playerElos), fallback2000. It is used for pawn-score prose bands, not headline rating. The full five-band thresholds and ten downgrade sentence keys are preserved in documentary blocks.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Character offset 22997.

```text
tted to the rating scale, then rescale to pawns
  return Math.log(1 / probability - 1) / (0.004 * ((0.0685 * rating - 12) / 100)) / 100;
}
```

`rating` = **max(WhiteElo, BlackElo)**, defaulting to 2000 (`M4 = 2e3`). The
result is in **pawns** (the score it is compared against was divided by 100 in
§5). Measured (`node crosscheck/rating-bands.mjs`):

| max rating | Winning | Better | Equal | Worse | Losing |
| --- | 
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 229694.

```text
7e-4,-0.10264 -0.0418,-0.20088 -0.11407,-0.27377 L 5.771601,6.0056148 c -0.03098,-0.03803 -0.07016,-0.06856 -0.1146,-0.0893 -0.04445,-0.02075 -0.09302,-0.03116 -0.14206,-0.03047 -0.09975,0.00412 -0.19392,0.04711 -0.26237,0.11977 L 2.919801,8.321285 2.514841,8.7262349 c -0.03683,0.03533 -0.06598,0.07788 -0.0856,0.1249801 -0.01963,0.04711 -0.02932,0.09777 -0.02847,0.14879 -0.00341,0.04998 0.00457,0.10007 0.02334,0.1465
```

**Source references:** SRC-2047, SRC-1137  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087, FND-18108, FND-18109

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
