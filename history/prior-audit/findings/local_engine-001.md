# local_engine — findings 1–11

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18889"></a>
## FND-18889: Legacy external UCI wrapper remains but is not the current native review pipeline

**Category:** local_engine  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

extension/lib/engines.js defines Stockfish16.1/Torch/TorchLite workers,loader#wasm resolution,NNUE/hash/thread initialization and UCI parsing. client-math.js retains old presentation helpers and an overbroad server-only comment. Current review.js imports CeeClient rather than the external UciEngine,so presence of these files does not prove they drive production reviews.

### Evidence

- **SRC-0046** `extension/lib/engines.js` — [preserved redacted evidence](../evidence/text/2467338dbc85faaa4d9bbcecfe3149a33de8a0a241be526e3ca2ee245db52450.js)
  Character offset 1610.

```text
on name Threads value 1', 'setoption name Hash value 64'],
    enumValue: 11,
  },
};

export class UciEngine {
  constructor(presetKey = 'stockfish-nnue-16') {
    const p = ENGINE_PRESETS[presetKey];
    if (!p) throw new Error('unknown engine preset ' + presetKey);
    this.preset = p;
    this.key = presetKey;
    this.lines = [];
    this.bestmove = null;
    this._waiters = [];
    this.ready = this._boot();
  
```
- **SRC-0044** `extension/lib/client-math.js` — [preserved redacted evidence](../evidence/text/e45a0e0e5467deec1b3f896f0f5c7d8af5a9bef7862b10ad910917e13a92af40.js)
- **SRC-0049** `extension/lib/review.js` — [preserved redacted evidence](../evidence/text/5f056d321e317d758a6d9882be84d2b32b60555244d92454645b7c2f3229f21d.js)

**Source references:** SRC-0046, SRC-0044, SRC-0049  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18933"></a>
## FND-18933: CEE JS is a loader/bridge, WASM contains native machinery

**Category:** local_engine  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

The loader is about129KB and exposes Emscripten/native CEE APIs. WASM strings and extracted descriptors include TorchHuman,Maia,torch_search_mode,PVtrees and native source paths. Presence of strings proves embedded machinery, not that every model/feature is usable or a separate Torch Human binary exists.

### Evidence

- **SRC-0031** `extension/engines/cee/explanation-engine.js` — [preserved redacted evidence](../evidence/text/46761f54ffdd6550b3fe90553e3c13d1a49828b3c44b680845afcc20c0666c70.js)
- **SRC-0034** `extension/engines/cee/explanation-engine.wasm` — [preserved redacted evidence](../evidence/binary-strings/b94aaeec32ee0458aeba42a9d431a15f37c16740c030868c691c0697b3203373.txt)
  Character offset 25701.

```text
lity raw formatVersion
chesscom.explanation_engine.v1alpha.InternalFeatureCharmInferenceRequest.fen
TorchHuman
charm-ctl
charm-small
Unable to get Charm model
google.protobuf.FieldMask
NNMult mode requires a top-level 'nn' config block
charm-pack
UCI LimitStrength
Keying PositionSearch requires RunSearchRequest.game_review_search_settings to define a Strength
Keying GameState requires RunSearchRequest.game_review_sea
```

**Source references:** SRC-0031, SRC-0034  
**URL references:** None independently associated  
**Related findings:** FND-19887, FND-20139, FND-18934, FND-18940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18934"></a>
## FND-18934: Human mode requires a Torch engine

**Category:** local_engine  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Native error string includes "is not a Torch engine, and Torch Human mode requires one". This is a requirement check in the shipped binary; it does not make Stockfish a Human engine or document all accepted engine-instance IDs.

### Evidence

- **SRC-0034** `extension/engines/cee/explanation-engine.wasm` — [preserved redacted evidence](../evidence/binary-strings/b94aaeec32ee0458aeba42a9d431a15f37c16740c030868c691c0697b3203373.txt)
  Character offset 32857.

```text
earch requires an engine type
Keying GameState requires an engine type
' is not a Torch engine, and Torch Human mode requires one
PVTree Options provided, but Torch is not the selected engine
UnleashedPersonality requires Torch or Stockfish 12+ engine
CEE_AddArtifactFromFile
expected_points_at_charm_scale
handle_pvtree
info string pvtree
UCI_AnalyseMode
GradeTrainItemMove requires a played move to grade
Invalid first
```

**Source references:** SRC-0034  
**URL references:** None independently associated  
**Related findings:** FND-18933, FND-18940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18935"></a>
## FND-18935: Local human request changes actual UCI command shape

**Category:** local_engine  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Feature29 RunSearch1000nodes with torchSearchMode.mode.case=human produced go nodes1000 pvtrees with splitDepthLimit6,splitWidthLimit2,allowedExcessWidth2,rating2100,max_allowed_cp_margin100,ep_loss_margin0.02. Control used searchmoves. This is execution evidence that the flag is not ignored, not proof of exact server settings.

### Evidence

- **SRC-0786** `research/refinement/probe-human-decoded-log.txt` — [preserved redacted evidence](../evidence/text/b60812946f93d0fec18aa67a30bb831542870aa7c7aaf338ce6ae3cfb449fa1e.txt)
  Character offset 885.

```text
cmd position fen rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
request cmd go nodes 1000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 1 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02
output info depth 1 seldepth 1 mult
```
- **SRC-0788** `research/refinement/probe-normal-decoded-log.txt` — [preserved redacted evidence](../evidence/text/fc6a30e936c2a0c6f15a458fdc52a1a744fe2294c8e5b3501cd3d9c4b252dbd1.txt)

**Source references:** SRC-0786, SRC-0788  
**URL references:** None independently associated  
**Related findings:** FND-20812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18936"></a>
## FND-18936: Offline local Human probe completed

**Category:** local_engine  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Stored probe-human-offline.json records progress1,+18cp,depth5,nodes859,underlying engine11 and engine log Torch master-20260925-87ee25a. The runner replaces fetch with a rejecting function and records attempts; none was recorded. This is a Node-wrapper local WASM test, not a Chrome UI/cloud-network trace.

### Evidence

- **SRC-0838** `research/refinement/results/probe-human-offline.json` — [preserved redacted evidence](../evidence/text/0961e9ec73c34d2d6963726adddc0c9d8d4fe911421d9d594fc7a85b5682b683.json)
  Character offset 1350.

```text
  }
            ]
          }
        ],
        "progress": 1,
        "log": [
          "engine: Torch master-20260925-87ee25a"
        ]
      }
    }
  ],
  "elapsedSeconds": 1.541,
  "searchLogs": [
    "Explanation Engine 1.130.285 (C) 2025 Chess.com, LLC",
    "[2026-11-14 20:21:40.184] [cee-ostream-logger] [info] CEE - API_LOG: [REDACTED_ENCODED_PAYLOAD]",
    "",
    "[2026-11-14 20:21:40.211] [cee-ostream-
```
- **SRC-0746** `research/refinement/human-probe.mjs` — [preserved redacted evidence](../evidence/text/f710e7c6d24bbaf1649874f7974692eedf445f700152e80b7142034f1f12fbe8.mjs)

**Source references:** SRC-0838, SRC-0746  
**URL references:** None independently associated  
**Related findings:** FND-18859, FND-18937

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18937"></a>
## FND-18937: Offline normal control completed

**Category:** local_engine  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Stored normal control records+17cp,depth6,nodes717,progress1,engine11, same Torch build. Thus engine11 does not by itself diagnose whether human search logic ran.

### Evidence

- **SRC-0840** `research/refinement/results/probe-normal-offline.json` — [preserved redacted evidence](../evidence/text/1fbe6d1ae3661e771905f598ec51fc6101fb3358a97884161c353b29b5ad6390.json)
  Character offset 537.

```text

            "case": "scoreCentipawnsWhite",
            "value": 17
          }
        },
        "depth": 6,
        "engine": 11,
        "nodes": 717
      },
      "response": {
        "evaluations": [
          {
            "score": {
              "score": {
                "score": {
                  "case": "scoreCentipawnsWhite",
                  "value": 17
                }
              },
         
```
- **SRC-0838** `research/refinement/results/probe-human-offline.json` — [preserved redacted evidence](../evidence/text/0961e9ec73c34d2d6963726adddc0c9d8d4fe911421d9d594fc7a85b5682b683.json)

**Source references:** SRC-0840, SRC-0838  
**URL references:** None independently associated  
**Related findings:** FND-18861, FND-18859, FND-18936

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18938"></a>
## FND-18938: Human underlying enum11 and CEAC requested enum12 are different layers

**Category:** local_engine  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Website CEAC Engine.TORCH_HUMAN is12; native search still reports underlying Torch11 when human mode runs. Earlier ID-only inference was too strict. This does not mean all ordinary CEE11 reviews automatically used human mode.

### Evidence

- **SRC-2049** `accessible-conversation/current-and-condensed-history` — [preserved redacted evidence](../evidence/text/b295bb5af6a3f9a3463e5be596f3ba2ea176d41d66915d311049a0980c38495a.txt)
  Character offset 4987.

```text
ands to PVtrees rather than ordinary searchmoves. Both human and normal results retained underlying engine11. Prior inference "engine11 means human mode inactive" was retracted as too strict.
- Normal probe returned+17cp,depth6; human+18cp,depth5; log engine Torch master-20260925-87ee25a. Human logs included internal rating2100. This proves local execution of a human search mode, not server parity, standalone Maia pr
```
- **SRC-0838** `research/refinement/results/probe-human-offline.json` — [preserved redacted evidence](../evidence/text/0961e9ec73c34d2d6963726adddc0c9d8d4fe911421d9d594fc7a85b5682b683.json)
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)

**Source references:** SRC-2049, SRC-0838, SRC-1137  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-18924, FND-18859, FND-18936, FND-18937

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18939"></a>
## FND-18939: Feature29/79/54/288 do not behave interchangeably

**Category:** local_engine  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Successful RunSearch29 and GetGameReviewEvaluations79 human paths coexist with timed-out InternalFeatureRunPvTrees288 and aborted EvaluateGame54, including a normal control. A timeout or assertion in one interface does not prove all local human support is absent.

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)
- **SRC-0842** `research/refinement/results/probe-pvtree-human.json` — [preserved redacted evidence](../evidence/text/43fc0cef1993371775e1447ce3db95a71391464001ea7b5fa724fd24c151d6a6.json)
  Character offset 540.

```text
archOnly": true,
    "timeoutSeconds": 20
  },
  "started": "2026-11-14T20:20:37.827Z",
  "error": "trial timeout after 20s",
  "warnings": []
}
```
- **SRC-0827** `research/refinement/results/normalized-evaluate-normal.json` — [preserved redacted evidence](../evidence/text/68a206e4b11c88aad3f4639678d58ff815320a2c8458afcc4f5ebb1dad4b87da.json)

**Source references:** SRC-0799, SRC-0842, SRC-0827  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591, FND-18863

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18940"></a>
## FND-18940: Native mode incompatibility strings

**Category:** local_engine  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

WASM says torch_search_mode.human is incompatible with reduce_nodes_on_successive_multisearch_searches; that reduction also requires multisearch without pvtrees and a nodes-only limit. Treat these as declared native validation constraints, not newly tested every-branch behavior.

### Evidence

- **SRC-0034** `extension/engines/cee/explanation-engine.wasm` — [preserved redacted evidence](../evidence/binary-strings/b94aaeec32ee0458aeba42a9d431a15f37c16740c030868c691c0697b3203373.txt)
  Character offset 48242.

```text
n Engine knows.
Reduce_nodes_on_successive_multisearch_searches is incompatible with time_limit_ms.
torch_search_mode.human is incompatible with reduce_nodes_on_successive_multisearch_searches.
Reduce_nodes_on_successive_multisearch_searches is incompatible with use_pvtrees.
missing or invalid feature game point in request: this feature requires a valid RPC-level game point (the `game_point` arg passed to the call). 
```

**Source references:** SRC-0034  
**URL references:** None independently associated  
**Related findings:** FND-18933, FND-18934

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18941"></a>
## FND-18941: Engine-instance options are not engine enum IDs

**Category:** local_engine  
**Classification:** inference  
**Verification:** partially verified  
**Confidence:** medium — Exact content of the cited stored artifact; not a claim of current live deployment.

Native v1alpha EngineInstanceOptions carries binary_path,type,web_worker.script_url; InitEnginePool returns instance.id,pid. An engine_id parameter may refer to an instance rather than enum11/12. Presence alone does not establish a supported browser external-engine configuration.

### Evidence

- **SRC-1051** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_engine_instance_options.proto.txt` — [preserved redacted evidence](../evidence/text/65f2cb2532e22938ac32c7b7429986c33a5f855516e29fcdd7b12a9cb55a1c58.txt)
  Character offset 235.

```text
hesscom/engine/v1/engine.proto"
message_type {
  name: "EngineInstanceOptions"
  field {
    name: "binary_path"
    number: 1
    label: LABEL_OPTIONAL
    type: TYPE_STRING
  }
  field {
    name: "type"
    number: 2
    label: LABEL_OPTIONAL
    type: TYPE_ENUM
    type_name: ".chesscom.engine.v1.Engine"
  }
  field {
    name: "web_worker"
    number: 3
    label: LABEL_OPTIONAL
    type: TYPE_MESSAGE
    type_n
```

**Source references:** SRC-1051  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18942"></a>
## FND-18942: CEE export JS arity is uninformative about native signature

**Category:** local_engine  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

export-signatures.json records CEE_Init0 and CEE_InitWithOpts0 JS arity. InitWithOptsCall descriptor has n_async_task_processors and engine_pool_size. Arity0 is not proof the native API takes no options or provides a TorchHuman toggle.

### Evidence

- **SRC-0732** `research/refinement/export-signatures.json` — [preserved redacted evidence](../evidence/text/6cc54a61fa9ec17753879a7d4e19cde54fd784b22e1e95e1f268dcb279aea48e.json)
  Character offset 5.

```text
{
  "CEE_Init": 0,
  "CEE_InitWithOpts": 0
}
```
- **SRC-0872** `research/refinement/torch-human-evidence.txt` — [preserved redacted evidence](../evidence/text/cef44a26b2193147ec602199be2491c42998bf4ea7fcf33e096b3ca73e6f8452.txt)

**Source references:** SRC-0732, SRC-0872  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
