# api_network — findings 1–14

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18892"></a>
## FND-18892: Production Game Review WebSocket

**Category:** api_network  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

The saved EW.Urls table declares wss://analysis.chess.com:443/v2/game-review. x3e constructs/encodes W4e output, opens S3e socket and sends the request; C3e decodes binary responses. This is static source evidence, not a captured logged-in cloud request.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1834609.

```text
ction v3e(){return _3e()}function y3e(){_3e()}function b3e(){return rG}function nG(e){return e===rG}async function x3e(e){let{depth:t}=e,n=kU();if(!n){bW(`Game board is not available for CEAC.`);return}let r=dJe(n),i=window.chesscom.analysis.extraGameData?.isRated,a=fM(),o=n.getHeaders(),{game:s,consumedNodes:c}=uJe(r,{isRated:typeof i==`boolean`?i:void 0,gameUuid:$4e(),legacyGameId:a&&/^\d+$/.test(a)?BigInt(a):void 
```

**Source references:** SRC-1137  
**URL references:** <wss://analysis.chess.com:443/v2/game-review>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18893"></a>
## FND-18893: ProdServerIDLRunSearch endpoint

**Category:** api_network  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

wss://analysis.chess.com:443/v2/run-search is a declared historical endpoint in EW.Urls. Protocol purpose is inferred from its table key/call sites; current reachability, authentication and authorization were not tested by this audit.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1811802.

```text
ServerIDLGameReview:`ProdServerIDLGameReview`,StagingServerIDLRunSearch:`StagingServerIDLRunSearch`,ProdServerIDLRunSearch:`ProdServerIDLRunSearch`};e.Urls={[t.NewMax]:`wss://max-analysis.prod.chess-platform.com:443`,[t.StagingMax]:`wss://max-analysis.staging.chess-platform.com:443`,[t.SandboxServerIDLGameReview]:`wss://analysis-sandbox.chess.com:443/v2/game-review`,[t.StagingServerIDLGameReview]:`wss://analysis-stag
```

**Source references:** SRC-1137  
**URL references:** <wss://analysis.chess.com:443/v2/run-search>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18894"></a>
## FND-18894: StagingServerIDLGameReview endpoint

**Category:** api_network  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

wss://analysis-staging.chess.com:443/v2/game-review is a declared historical endpoint in EW.Urls. Protocol purpose is inferred from its table key/call sites; current reachability, authentication and authorization were not tested by this audit.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1811642.

```text
es={NewMax:`NewMax`,StagingMax:`StagingMax`,SandboxServerIDLGameReview:`SandboxServerIDLGameReview`,StagingServerIDLGameReview:`StagingServerIDLGameReview`,ProdServerIDLGameReview:`ProdServerIDLGameReview`,StagingServerIDLRunSearch:`StagingServerIDLRunSearch`,ProdServerIDLRunSearch:`ProdServerIDLRunSearch`};e.Urls={[t.NewMax]:`wss://max-analysis.prod.chess-platform.com:443`,[t.StagingMax]:`wss://max-analysis.staging.
```

**Source references:** SRC-1137  
**URL references:** <wss://analysis-staging.chess.com:443/v2/game-review>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18895"></a>
## FND-18895: SandboxServerIDLGameReview endpoint

**Category:** api_network  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

wss://analysis-sandbox.chess.com:443/v2/game-review is a declared historical endpoint in EW.Urls. Protocol purpose is inferred from its table key/call sites; current reachability, authentication and authorization were not tested by this audit.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1811586.

```text
al=2e3,e.StreamTypes={Reconnect:`reconnect`};let t=e.Types={NewMax:`NewMax`,StagingMax:`StagingMax`,SandboxServerIDLGameReview:`SandboxServerIDLGameReview`,StagingServerIDLGameReview:`StagingServerIDLGameReview`,ProdServerIDLGameReview:`ProdServerIDLGameReview`,StagingServerIDLRunSearch:`StagingServerIDLRunSearch`,ProdServerIDLRunSearch:`ProdServerIDLRunSearch`};e.Urls={[t.NewMax]:`wss://max-analysis.prod.chess-platf
```

**Source references:** SRC-1137  
**URL references:** <wss://analysis-sandbox.chess.com:443/v2/game-review>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18896"></a>
## FND-18896: StagingServerIDLRunSearch endpoint

**Category:** api_network  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

wss://analysis-staging.chess.com:443/v2/run-search is a declared historical endpoint in EW.Urls. Protocol purpose is inferred from its table key/call sites; current reachability, authentication and authorization were not tested by this audit.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1811748.

```text
gServerIDLGameReview:`StagingServerIDLGameReview`,ProdServerIDLGameReview:`ProdServerIDLGameReview`,StagingServerIDLRunSearch:`StagingServerIDLRunSearch`,ProdServerIDLRunSearch:`ProdServerIDLRunSearch`};e.Urls={[t.NewMax]:`wss://max-analysis.prod.chess-platform.com:443`,[t.StagingMax]:`wss://max-analysis.staging.chess-platform.com:443`,[t.SandboxServerIDLGameReview]:`wss://analysis-sandbox.chess.com:443/v2/game-revie
```

**Source references:** SRC-1137  
**URL references:** <wss://analysis-staging.chess.com:443/v2/run-search>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18897"></a>
## FND-18897: NewMax endpoint

**Category:** api_network  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

wss://max-analysis.prod.chess-platform.com:443 is a declared historical endpoint in EW.Urls. Protocol purpose is inferred from its table key/call sites; current reachability, authentication and authorization were not tested by this audit.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1811546.

```text
ssageReceived`},e.DefaultReconnectInterval=2e3,e.StreamTypes={Reconnect:`reconnect`};let t=e.Types={NewMax:`NewMax`,StagingMax:`StagingMax`,SandboxServerIDLGameReview:`SandboxServerIDLGameReview`,StagingServerIDLGameReview:`StagingServerIDLGameReview`,ProdServerIDLGameReview:`ProdServerIDLGameReview`,StagingServerIDLRunSearch:`StagingServerIDLRunSearch`,ProdServerIDLRunSearch:`ProdServerIDLRunSearch`};e.Urls={[t.NewM
```

**Source references:** SRC-1137  
**URL references:** <wss://max-analysis.prod.chess-platform.com:443>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18898"></a>
## FND-18898: StagingMax endpoint

**Category:** api_network  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

wss://max-analysis.staging.chess-platform.com:443 is a declared historical endpoint in EW.Urls. Protocol purpose is inferred from its table key/call sites; current reachability, authentication and authorization were not tested by this audit.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1811562.

```text
e.DefaultReconnectInterval=2e3,e.StreamTypes={Reconnect:`reconnect`};let t=e.Types={NewMax:`NewMax`,StagingMax:`StagingMax`,SandboxServerIDLGameReview:`SandboxServerIDLGameReview`,StagingServerIDLGameReview:`StagingServerIDLGameReview`,ProdServerIDLGameReview:`ProdServerIDLGameReview`,StagingServerIDLRunSearch:`StagingServerIDLRunSearch`,ProdServerIDLRunSearch:`ProdServerIDLRunSearch`};e.Urls={[t.NewMax]:`wss://max-a
```

**Source references:** SRC-1137  
**URL references:** <wss://max-analysis.staging.chess-platform.com:443>  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18899"></a>
## FND-18899: CEAC frame boundaries are WebSocket message boundaries

**Category:** api_network  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

C3e decodes the ArrayBuffer directly as GameReviewResponse. extension frame() is identity normalization to Uint8Array and unframe() returns one message; there is no extra length-prefix framing in this adapter.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
- **SRC-0048** `extension/lib/protobuf.js` — [preserved redacted evidence](../evidence/text/9bfe315bd2c6c56a3c843cfd78efac6ff20485db2d0ca073cc752b1266e44e5a.js)
  Character offset 16558.

```text
fromBinary(GameReviewResponse)`),
 * so "framing" here is just a normalisation to a Uint8Array.
 */
export function frame(bytes) {
  return bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes);
}

/** Split a concatenated byte stream into individual messages (identity). */
export function unframe(bytes) {
  return [frame(bytes)];
}

/** Encode + frame in one step. */
export function frameMessage(typeName, obj)
```

**Source references:** SRC-1137, SRC-0048  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117, FND-18914, FND-19365

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18900"></a>
## FND-18900: Handshake timeout is separate from review duration

**Category:** api_network  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

S3e opens a WebSocket, sets binaryType=arraybuffer and uses k3e=1e4 to reject a connection not opened in ten seconds. This does not time-limit completed review computation to ten seconds.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1836103.

```text
r.binaryType=`arraybuffer`;let i=setTimeout(()=>{r.readyState!==WebSocket.OPEN&&(r.close(),n(Error(`CEAC IDL WebSocket connection timeout`)))},k3e);r.onopen=()=>{clearTimeout(i),r.onerror=null,t(r)},r.onerror=()=>{clearTimeout(i),n(Error(`CEAC IDL WebSocket connection failed`))}})}function C3e(e,t,n){let r=!1,i=()=>{r||(r=!0,e.onmessage=null,e.onclose=null,e.onerror=null,O3e(e),g3e(i))};return e.onmessage=e=>{if(r||!
```

**Source references:** SRC-1137  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18901"></a>
## FND-18901: Response stream is a tagged oneof

**Category:** api_network  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GameReviewResponse has progress,success,failure,heartbeat,waiting_for_capacity cases. Numeric field details are in the schema registry. A progress case is not proof the engine is moving forward between frames.

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 771.

```text
chRequest set_coach = 7;
  optional .chesscom.ceac.v2.GameReviewOptions game_review_options = 9;
}

message GameReviewResponse {
  oneof result {
  .chesscom.ceac.v2.GameReviewResponseProgress progress = 1;
  .chesscom.ceac.v2.GameReviewResponseSuccess success = 2;
  .chesscom.ceac.v2.GameReviewResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for
```

**Source references:** SRC-0233  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18902"></a>
## FND-18902: Request heartbeat settings

**Category:** api_network  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

The saved W4e request uses requestOptions heartbeatIntervalSeconds5/useProgressUpdatestrue; its runSearchReq has heartbeatIntervalSeconds0 and streamResultsfalse. These are different message levels, not inconsistent settings.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1815858.

```text
questMetadata:HO(bH,{client:_H.WEB,product:vH.GAME_REVIEW,receivedTime:Uk()}),requestOptions:HO(xH,{heartbeatIntervalSeconds:5,useProgressUpdates:!0}),...l||u?{gameReviewOptions:HO(zGe,{reportCardEntitled:l,includeTrainTakeaways:u,canAccessLockedTakeaways:u&&!Om(1)})}:{},...o?{setCoach:HO(PUe,{textId:o.textId,locale:o.locale})}:{},...s||c?{charmInfReq:HO(eWe,{...s?{tricky:HO(nWe)}:{},...c?{grv2:HO(tWe)}:{}})}:{}})}va
```

**Source references:** SRC-1137  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18903"></a>
## FND-18903: Remote run-search has a historical JSON path too

**Category:** api_network  
**Classification:** unknown  
**Verification:** historical  
**Confidence:** medium — Exact content of the cited stored artifact; not a claim of current live deployment.

Uploaded documentation describes a plain-JSON run-search socket taking id,fen,uciMoves and returning heartbeat/waitingForCapacity. It is not the same wire representation as CEAC GameReviewResponse. Retain as historical report unless independently tied to a specific saved call site.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Character offset 7952.

```text
gress }`, which
drives the progress bar.

### 3.4 The other socket

`run-search` also exists as a **plain JSON** socket, used by the board's own
analysis mode rather than Game Review:

```json
{ "id": "...", "fen": "...", "uciMoves": ["e2e4"] }
```

with `heartbeat` and `waitingForCapacity` JSON messages. Same server, same
routing, no protobuf. If you only want *an evaluation* rather than a review,
this is the simple
```

**Source references:** SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18904"></a>
## FND-18904: Same-origin socket override is not a new public endpoint

**Category:** api_network  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

The historical frontend references window.chesscom.analysis.ceacSocketSameOrigin. This changes routing on the client; it does not establish a currently exposed standalone local server.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1833779.

```text
ColorsAsNumbers.White,$W.white)})}));function c3e(e){let t=EW.Urls[e];if(window.chesscom?.analysis?.ceacSocketSameOrigin)return l3e(t);if(!d3e.has(e))return t;let n=u3e();return n?t.replace(f3e,n):t}function l3e(e){if(!e)return e;let{pathname:t,search:n}=new URL(e);return t===`/`?e:`${window.location.protocol===`https:`?`wss:`:`ws:`}//${window.location.host}${t}${n}`}function u3e(){let e=window.location.hostname.toLo
```
- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Character offset 6673.

```text
ent jobs.

There is also a same-origin override used by the dev harness —
`window.chesscom.analysis.ceacSocketSameOrigin` — which rewrites the socket URL
to the page origin (`l3e()`). That is the hook worth knowing if you ever want
to run your own analysis server locally.

### 3.2 Framing

One WebSocket, binary frames, one protobuf message per frame. The client sets
`binaryType = 'arraybuffer'` and each frame is deco
```

**Source references:** SRC-1137, SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117, FND-00085, FND-00086

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18922"></a>
## FND-18922: Brilliant verification can modify a local tally afterward

**Category:** api_network  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

The Quick Analysis client creates a BrilliantVerificationService using /rpc/ceac, collects brilliant move indices, sends game metadata,selected engine and Fast searchSettings, then replaces the relevant brilliant count with returned classifications. This is declared behavior, not a captured RPC. It prevents assuming the final post-game card is wholly local.

### Evidence

- **SRC-0752** `research/refinement/live-chunks/client.e0da4c65.BIjoPk3wAJ.chunk.js` — [preserved redacted evidence](../evidence/text/5919dccce274c55ef86cf454d90cf46ed1d0a18dcb86be4ccdb0c70f625d1dea.js)
  Character offset 39653.

```text
)=>{z(),Ka=qt.FAST})),Ja,Ya=t((()=>{Oi(),Ue(),a(),Ja=ht(Ei,Ye(ct({BrilliantVerificationService:()=>`/rpc/ceac`})))})),Xa,Za=t((()=>{it(),(function(e){e.MaxLines=5;let t;(function(e){e.Default=De,e.FullAnalysisOptions={Latest:`latest`,Stockfish15:`stockfish15`,Stockfish151:`stockfish15.1 nnue`,Stockfish16:`stockfish16 nnue`,TorchHuman:`torch-human`}})(t||=e.Engine||={})})(Xa||={})})),Qa,$a=t((()=>{Za(),Qa=Xa.Engine.Fu
```

**Source references:** SRC-0752  
**URL references:** None independently associated  
**Related findings:** FND-18891, FND-18917, FND-18918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
