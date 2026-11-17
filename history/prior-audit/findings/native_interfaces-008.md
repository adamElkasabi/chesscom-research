# native_interfaces — findings 701–800

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-13360"></a>
## FND-13360: chesscom.explanation_engine.v1.BookMovesSettings.move_count = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BookMovesSettings",
  "name": "move_count",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13361"></a>
## FND-13361: Native message: chesscom.explanation_engine.v1.SamplingSettings

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SamplingSettings",
  "field": [
    {
      "name": "probability_threshold",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    }
  ]
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13362"></a>
## FND-13362: chesscom.explanation_engine.v1.SamplingSettings.probability_threshold = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SamplingSettings",
  "name": "probability_threshold",
  "number": 1,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13363"></a>
## FND-13363: Native message: chesscom.explanation_engine.v1.AdditiveBehavior

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AdditiveBehavior",
  "field": [
    {
      "name": "name",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "enabled",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "weight",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    },
    {
      "name": "rules",
      "number": 4,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MatcherRule"
    },
    {
      "name": "piece_bonuses",
      "number": 5,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PieceBonus"
    },
    {
      "name": "max_eval_drop",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.EvalThreshold",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "max_advantage",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.EvalThreshold",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "context",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.BotMoveBehaviorContext"
    },
    {
      "name": "legacy_bot",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.LegacyBot",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "nn",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.NnConfig",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "coherence",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CoherenceConfig",
      "oneof_index": 4,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_max_eval_drop"
    },
    {
      "name": "_max_advantage"
    },
    {
      "name": "_legacy_bot"
    },
    {
      "name": "_nn"
    },
    {
      "name": "_coherence"
    }
  ]
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13364"></a>
## FND-13364: chesscom.explanation_engine.v1.AdditiveBehavior.name = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AdditiveBehavior",
  "name": "name",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13365"></a>
## FND-13365: chesscom.explanation_engine.v1.AdditiveBehavior.enabled = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AdditiveBehavior",
  "name": "enabled",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13366"></a>
## FND-13366: chesscom.explanation_engine.v1.AdditiveBehavior.weight = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AdditiveBehavior",
  "name": "weight",
  "number": 3,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13367"></a>
## FND-13367: chesscom.explanation_engine.v1.AdditiveBehavior.rules = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AdditiveBehavior",
  "name": "rules",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.MatcherRule",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13368"></a>
## FND-13368: chesscom.explanation_engine.v1.AdditiveBehavior.piece_bonuses = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AdditiveBehavior",
  "name": "piece_bonuses",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.PieceBonus",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13369"></a>
## FND-13369: chesscom.explanation_engine.v1.AdditiveBehavior.max_eval_drop = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AdditiveBehavior",
  "name": "max_eval_drop",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.EvalThreshold",
  "label": "LABEL_OPTIONAL",
  "oneof": "_max_eval_drop",
  "proto3_optional": true,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13370"></a>
## FND-13370: chesscom.explanation_engine.v1.AdditiveBehavior.max_advantage = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AdditiveBehavior",
  "name": "max_advantage",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.EvalThreshold",
  "label": "LABEL_OPTIONAL",
  "oneof": "_max_advantage",
  "proto3_optional": true,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13371"></a>
## FND-13371: chesscom.explanation_engine.v1.AdditiveBehavior.context = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AdditiveBehavior",
  "name": "context",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1.BotMoveBehaviorContext",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13372"></a>
## FND-13372: chesscom.explanation_engine.v1.AdditiveBehavior.legacy_bot = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AdditiveBehavior",
  "name": "legacy_bot",
  "number": 9,
  "type": ".chesscom.explanation_engine.v1.LegacyBot",
  "label": "LABEL_OPTIONAL",
  "oneof": "_legacy_bot",
  "proto3_optional": true,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13373"></a>
## FND-13373: chesscom.explanation_engine.v1.AdditiveBehavior.nn = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AdditiveBehavior",
  "name": "nn",
  "number": 10,
  "type": ".chesscom.explanation_engine.v1.NnConfig",
  "label": "LABEL_OPTIONAL",
  "oneof": "_nn",
  "proto3_optional": true,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13374"></a>
## FND-13374: chesscom.explanation_engine.v1.AdditiveBehavior.coherence = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AdditiveBehavior",
  "name": "coherence",
  "number": 11,
  "type": ".chesscom.explanation_engine.v1.CoherenceConfig",
  "label": "LABEL_OPTIONAL",
  "oneof": "_coherence",
  "proto3_optional": true,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13375"></a>
## FND-13375: Native message: chesscom.explanation_engine.v1.NnMultBehavior

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "NnMultBehavior",
  "field": [
    {
      "name": "name",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "enabled",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "weight",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    },
    {
      "name": "rules",
      "number": 4,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.NnMultRule"
    },
    {
      "name": "max_eval_drop",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "max_advantage",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "context",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.BotMoveBehaviorContext"
    }
  ],
  "oneof_decl": [
    {
      "name": "_max_eval_drop"
    },
    {
      "name": "_max_advantage"
    }
  ]
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13376"></a>
## FND-13376: chesscom.explanation_engine.v1.NnMultBehavior.name = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnMultBehavior",
  "name": "name",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13377"></a>
## FND-13377: chesscom.explanation_engine.v1.NnMultBehavior.enabled = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnMultBehavior",
  "name": "enabled",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13378"></a>
## FND-13378: chesscom.explanation_engine.v1.NnMultBehavior.weight = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnMultBehavior",
  "name": "weight",
  "number": 3,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13379"></a>
## FND-13379: chesscom.explanation_engine.v1.NnMultBehavior.rules = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnMultBehavior",
  "name": "rules",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.NnMultRule",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13380"></a>
## FND-13380: chesscom.explanation_engine.v1.NnMultBehavior.max_eval_drop = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnMultBehavior",
  "name": "max_eval_drop",
  "number": 5,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_max_eval_drop",
  "proto3_optional": true,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13381"></a>
## FND-13381: chesscom.explanation_engine.v1.NnMultBehavior.max_advantage = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnMultBehavior",
  "name": "max_advantage",
  "number": 6,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_max_advantage",
  "proto3_optional": true,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13382"></a>
## FND-13382: chesscom.explanation_engine.v1.NnMultBehavior.context = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnMultBehavior",
  "name": "context",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.BotMoveBehaviorContext",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13383"></a>
## FND-13383: Native message: chesscom.explanation_engine.v1.MatcherRule

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "MatcherRule",
  "field": [
    {
      "name": "circumstances",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.Circumstance"
    },
    {
      "name": "tags",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.AnalysisType"
    },
    {
      "name": "move_classifications",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
    },
    {
      "name": "weight",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_weight"
    }
  ]
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13384"></a>
## FND-13384: chesscom.explanation_engine.v1.MatcherRule.circumstances = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MatcherRule",
  "name": "circumstances",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.Circumstance",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13385"></a>
## FND-13385: chesscom.explanation_engine.v1.MatcherRule.tags = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MatcherRule",
  "name": "tags",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.AnalysisType",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13386"></a>
## FND-13386: chesscom.explanation_engine.v1.MatcherRule.move_classifications = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MatcherRule",
  "name": "move_classifications",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.MoveClassification",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13387"></a>
## FND-13387: chesscom.explanation_engine.v1.MatcherRule.weight = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MatcherRule",
  "name": "weight",
  "number": 4,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": "_weight",
  "proto3_optional": true,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13388"></a>
## FND-13388: Native message: chesscom.explanation_engine.v1.NnMultRule

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "NnMultRule",
  "field": [
    {
      "name": "pieces",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PieceGate",
      "oneof_index": 0
    },
    {
      "name": "board_events",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MatcherGroup",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "body"
    }
  ]
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13389"></a>
## FND-13389: chesscom.explanation_engine.v1.NnMultRule.pieces = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnMultRule",
  "name": "pieces",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PieceGate",
  "label": "LABEL_OPTIONAL",
  "oneof": "body",
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13390"></a>
## FND-13390: chesscom.explanation_engine.v1.NnMultRule.board_events = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnMultRule",
  "name": "board_events",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.MatcherGroup",
  "label": "LABEL_OPTIONAL",
  "oneof": "body",
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13391"></a>
## FND-13391: Native message: chesscom.explanation_engine.v1.MatcherGroup

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "MatcherGroup",
  "field": [
    {
      "name": "matchers",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MatcherRule"
    }
  ]
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13392"></a>
## FND-13392: chesscom.explanation_engine.v1.MatcherGroup.matchers = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MatcherGroup",
  "name": "matchers",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.MatcherRule",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13393"></a>
## FND-13393: Native message: chesscom.explanation_engine.v1.PieceGate

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PieceGate",
  "field": [
    {
      "name": "pieces",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.PieceType"
    }
  ]
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13394"></a>
## FND-13394: chesscom.explanation_engine.v1.PieceGate.pieces = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PieceGate",
  "name": "pieces",
  "number": 1,
  "type": ".chesscom.chess.v1.PieceType",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13395"></a>
## FND-13395: Native message: chesscom.explanation_engine.v1.PieceBonus

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PieceBonus",
  "field": [
    {
      "name": "piece_type",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.PieceType"
    },
    {
      "name": "bonus",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    }
  ]
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13396"></a>
## FND-13396: chesscom.explanation_engine.v1.PieceBonus.piece_type = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PieceBonus",
  "name": "piece_type",
  "number": 1,
  "type": ".chesscom.chess.v1.PieceType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13397"></a>
## FND-13397: chesscom.explanation_engine.v1.PieceBonus.bonus = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PieceBonus",
  "name": "bonus",
  "number": 2,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13398"></a>
## FND-13398: Native message: chesscom.explanation_engine.v1.EvalThreshold

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "EvalThreshold",
  "field": [
    {
      "name": "cp",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "penalty",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    }
  ]
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13399"></a>
## FND-13399: chesscom.explanation_engine.v1.EvalThreshold.cp = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvalThreshold",
  "name": "cp",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13400"></a>
## FND-13400: chesscom.explanation_engine.v1.EvalThreshold.penalty = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvalThreshold",
  "name": "penalty",
  "number": 2,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13401"></a>
## FND-13401: Native message: chesscom.explanation_engine.v1.EvalRange

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "EvalRange",
  "field": [
    {
      "name": "min_cp",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "max_cp",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13402"></a>
## FND-13402: chesscom.explanation_engine.v1.EvalRange.min_cp = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvalRange",
  "name": "min_cp",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13403"></a>
## FND-13403: chesscom.explanation_engine.v1.EvalRange.max_cp = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvalRange",
  "name": "max_cp",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13404"></a>
## FND-13404: Native message: chesscom.explanation_engine.v1.BotMoveBehaviorContext

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "BotMoveBehaviorContext",
  "field": [
    {
      "name": "game_phase",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.GamePhase",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "eval_range",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.EvalRange",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "rules",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MatcherRule"
    },
    {
      "name": "position_shapes",
      "number": 4,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.PositionShape"
    }
  ],
  "oneof_decl": [
    {
      "name": "_game_phase"
    },
    {
      "name": "_eval_range"
    }
  ]
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13405"></a>
## FND-13405: chesscom.explanation_engine.v1.BotMoveBehaviorContext.game_phase = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotMoveBehaviorContext",
  "name": "game_phase",
  "number": 1,
  "type": ".chesscom.chess.v1.GamePhase",
  "label": "LABEL_OPTIONAL",
  "oneof": "_game_phase",
  "proto3_optional": true,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13406"></a>
## FND-13406: chesscom.explanation_engine.v1.BotMoveBehaviorContext.eval_range = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotMoveBehaviorContext",
  "name": "eval_range",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.EvalRange",
  "label": "LABEL_OPTIONAL",
  "oneof": "_eval_range",
  "proto3_optional": true,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13407"></a>
## FND-13407: chesscom.explanation_engine.v1.BotMoveBehaviorContext.rules = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotMoveBehaviorContext",
  "name": "rules",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.MatcherRule",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13408"></a>
## FND-13408: chesscom.explanation_engine.v1.BotMoveBehaviorContext.position_shapes = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotMoveBehaviorContext",
  "name": "position_shapes",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.PositionShape",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13409"></a>
## FND-13409: Native message: chesscom.explanation_engine.v1.LegacyBot

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LegacyBot",
  "field": [
    {
      "name": "rating",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "personality",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.BotPersonality"
    },
    {
      "name": "weight",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    }
  ]
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13410"></a>
## FND-13410: chesscom.explanation_engine.v1.LegacyBot.rating = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LegacyBot",
  "name": "rating",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13411"></a>
## FND-13411: chesscom.explanation_engine.v1.LegacyBot.personality = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LegacyBot",
  "name": "personality",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.BotPersonality",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13412"></a>
## FND-13412: chesscom.explanation_engine.v1.LegacyBot.weight = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.LegacyBot",
  "name": "weight",
  "number": 3,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13413"></a>
## FND-13413: Native message: chesscom.explanation_engine.v1.NnConfig

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "NnConfig",
  "field": [
    {
      "name": "arch",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.ModelArch"
    },
    {
      "name": "model",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "rating",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "weight",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    },
    {
      "name": "charm_input_search_depth",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "temperature",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    },
    {
      "name": "rating_scale",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "time_taken_multiplier",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    }
  ]
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13414"></a>
## FND-13414: chesscom.explanation_engine.v1.NnConfig.arch = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnConfig",
  "name": "arch",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.ModelArch",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13415"></a>
## FND-13415: chesscom.explanation_engine.v1.NnConfig.model = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnConfig",
  "name": "model",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13416"></a>
## FND-13416: chesscom.explanation_engine.v1.NnConfig.rating = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnConfig",
  "name": "rating",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13417"></a>
## FND-13417: chesscom.explanation_engine.v1.NnConfig.weight = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnConfig",
  "name": "weight",
  "number": 4,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13418"></a>
## FND-13418: chesscom.explanation_engine.v1.NnConfig.charm_input_search_depth = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnConfig",
  "name": "charm_input_search_depth",
  "number": 5,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13419"></a>
## FND-13419: chesscom.explanation_engine.v1.NnConfig.temperature = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnConfig",
  "name": "temperature",
  "number": 6,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13420"></a>
## FND-13420: chesscom.explanation_engine.v1.NnConfig.rating_scale = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnConfig",
  "name": "rating_scale",
  "number": 7,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13421"></a>
## FND-13421: chesscom.explanation_engine.v1.NnConfig.time_taken_multiplier = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NnConfig",
  "name": "time_taken_multiplier",
  "number": 8,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13422"></a>
## FND-13422: Native message: chesscom.explanation_engine.v1.CoherenceConfig

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CoherenceConfig",
  "field": [
    {
      "name": "n_back",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "arch",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.ModelArch"
    },
    {
      "name": "model",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "rating",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "charm_input_search_depth",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "weight",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    }
  ]
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13423"></a>
## FND-13423: chesscom.explanation_engine.v1.CoherenceConfig.n_back = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoherenceConfig",
  "name": "n_back",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13424"></a>
## FND-13424: chesscom.explanation_engine.v1.CoherenceConfig.arch = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoherenceConfig",
  "name": "arch",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.ModelArch",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13425"></a>
## FND-13425: chesscom.explanation_engine.v1.CoherenceConfig.model = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoherenceConfig",
  "name": "model",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13426"></a>
## FND-13426: chesscom.explanation_engine.v1.CoherenceConfig.rating = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoherenceConfig",
  "name": "rating",
  "number": 4,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13427"></a>
## FND-13427: chesscom.explanation_engine.v1.CoherenceConfig.charm_input_search_depth = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoherenceConfig",
  "name": "charm_input_search_depth",
  "number": 5,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13428"></a>
## FND-13428: chesscom.explanation_engine.v1.CoherenceConfig.weight = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoherenceConfig",
  "name": "weight",
  "number": 6,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13429"></a>
## FND-13429: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionShape",
  "name": "POSITION_SHAPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13430"></a>
## FND-13430: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_PASSIVE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionShape",
  "name": "POSITION_SHAPE_PASSIVE",
  "number": 1,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13431"></a>
## FND-13431: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_ACTIVE = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionShape",
  "name": "POSITION_SHAPE_ACTIVE",
  "number": 2,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13432"></a>
## FND-13432: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_CLOSED = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionShape",
  "name": "POSITION_SHAPE_CLOSED",
  "number": 3,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13433"></a>
## FND-13433: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_OPEN = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionShape",
  "name": "POSITION_SHAPE_OPEN",
  "number": 4,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13434"></a>
## FND-13434: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_SEMI_OPEN = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionShape",
  "name": "POSITION_SHAPE_SEMI_OPEN",
  "number": 5,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13435"></a>
## FND-13435: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_THREATENED = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionShape",
  "name": "POSITION_SHAPE_THREATENED",
  "number": 6,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13436"></a>
## FND-13436: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_THREATENING = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionShape",
  "name": "POSITION_SHAPE_THREATENING",
  "number": 7,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13437"></a>
## FND-13437: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_CALM = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionShape",
  "name": "POSITION_SHAPE_CALM",
  "number": 8,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13438"></a>
## FND-13438: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_SHARP = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PositionShape",
  "name": "POSITION_SHAPE_SHARP",
  "number": 9,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13439"></a>
## FND-13439: chesscom.explanation_engine.v1.ModelArch.MODEL_ARCH_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.ModelArch",
  "name": "MODEL_ARCH_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13440"></a>
## FND-13440: chesscom.explanation_engine.v1.ModelArch.MODEL_ARCH_CHARM = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.ModelArch",
  "name": "MODEL_ARCH_CHARM",
  "number": 1,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13441"></a>
## FND-13441: chesscom.explanation_engine.v1.ModelArch.MODEL_ARCH_CHARM_SMALL = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.ModelArch",
  "name": "MODEL_ARCH_CHARM_SMALL",
  "number": 2,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13442"></a>
## FND-13442: chesscom.explanation_engine.v1.ModelArch.MODEL_ARCH_MAIA = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.ModelArch",
  "name": "MODEL_ARCH_MAIA",
  "number": 3,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13443"></a>
## FND-13443: chesscom.explanation_engine.v1.ModelArch.MODEL_ARCH_MAIA3 = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.ModelArch",
  "name": "MODEL_ARCH_MAIA3",
  "number": 4,
  "source_id": "SRC-0904",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0904** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_bot_move_configuration.proto.bin` — [preserved redacted evidence](../evidence/descriptors/90afa533aa7db1142f8318cb6732c53b07b431002ed4f39179c73ef7d59317b4.bin)

**Source references:** SRC-0904, SRC-1755  
**URL references:** None independently associated  
**Related findings:** FND-13337, FND-13338, FND-13339

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13444"></a>
## FND-13444: chesscom.explanation_engine.v1.CeeInternalComponent.CEE_INTERNAL_COMPONENT_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CeeInternalComponent",
  "name": "CEE_INTERNAL_COMPONENT_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0905",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0905** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_cee_internal_component.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3fb3eeb3edc1da2a095ef5375dac3b222462fa4b04515426fa51c9874089c7d7.bin)

**Source references:** SRC-0905, SRC-1675  
**URL references:** None independently associated  
**Related findings:** FND-13445, FND-13446

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13445"></a>
## FND-13445: chesscom.explanation_engine.v1.CeeInternalComponent.CEE_INTERNAL_COMPONENT_LUA = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CeeInternalComponent",
  "name": "CEE_INTERNAL_COMPONENT_LUA",
  "number": 1,
  "source_id": "SRC-0905",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0905** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_cee_internal_component.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3fb3eeb3edc1da2a095ef5375dac3b222462fa4b04515426fa51c9874089c7d7.bin)

**Source references:** SRC-0905, SRC-1675  
**URL references:** None independently associated  
**Related findings:** FND-13444, FND-13446

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13446"></a>
## FND-13446: chesscom.explanation_engine.v1.CeeInternalComponent.CEE_INTERNAL_COMPONENT_POSITION_DIFFICULTY = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CeeInternalComponent",
  "name": "CEE_INTERNAL_COMPONENT_POSITION_DIFFICULTY",
  "number": 2,
  "source_id": "SRC-0905",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0905** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_cee_internal_component.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3fb3eeb3edc1da2a095ef5375dac3b222462fa4b04515426fa51c9874089c7d7.bin)

**Source references:** SRC-0905, SRC-1675  
**URL references:** None independently associated  
**Related findings:** FND-13444, FND-13445

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13447"></a>
## FND-13447: chesscom.explanation_engine.v1.CeeInternalComponent.CEE_INTERNAL_COMPONENT_TORCH_SMALL = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CeeInternalComponent",
  "name": "CEE_INTERNAL_COMPONENT_TORCH_SMALL",
  "number": 3,
  "source_id": "SRC-0905",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0905** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_cee_internal_component.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3fb3eeb3edc1da2a095ef5375dac3b222462fa4b04515426fa51c9874089c7d7.bin)

**Source references:** SRC-0905, SRC-1675  
**URL references:** None independently associated  
**Related findings:** FND-13444, FND-13445, FND-13446

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13448"></a>
## FND-13448: chesscom.explanation_engine.v1.CeeInternalComponent.CEE_INTERNAL_COMPONENT_TORCH_LARGE = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CeeInternalComponent",
  "name": "CEE_INTERNAL_COMPONENT_TORCH_LARGE",
  "number": 4,
  "source_id": "SRC-0905",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0905** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_cee_internal_component.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3fb3eeb3edc1da2a095ef5375dac3b222462fa4b04515426fa51c9874089c7d7.bin)

**Source references:** SRC-0905, SRC-1675  
**URL references:** None independently associated  
**Related findings:** FND-13444, FND-13445, FND-13446

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13449"></a>
## FND-13449: chesscom.explanation_engine.v1.CeeInternalComponent.CEE_INTERNAL_COMPONENT_KOMODO = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CeeInternalComponent",
  "name": "CEE_INTERNAL_COMPONENT_KOMODO",
  "number": 5,
  "source_id": "SRC-0905",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0905** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_cee_internal_component.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3fb3eeb3edc1da2a095ef5375dac3b222462fa4b04515426fa51c9874089c7d7.bin)

**Source references:** SRC-0905, SRC-1675  
**URL references:** None independently associated  
**Related findings:** FND-13444, FND-13445, FND-13446

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13450"></a>
## FND-13450: chesscom.explanation_engine.v1.CeeInternalComponent.CEE_INTERNAL_COMPONENT_INTERNAL_FEATURES = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CeeInternalComponent",
  "name": "CEE_INTERNAL_COMPONENT_INTERNAL_FEATURES",
  "number": 6,
  "source_id": "SRC-0905",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0905** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_cee_internal_component.proto.bin` — [preserved redacted evidence](../evidence/descriptors/3fb3eeb3edc1da2a095ef5375dac3b222462fa4b04515426fa51c9874089c7d7.bin)

**Source references:** SRC-0905, SRC-1675  
**URL references:** None independently associated  
**Related findings:** FND-13444, FND-13445, FND-13446

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13451"></a>
## FND-13451: chesscom.explanation_engine.v1.CeeInternalEngine.CEE_INTERNAL_ENGINE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CeeInternalEngine",
  "name": "CEE_INTERNAL_ENGINE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0906",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0906** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_cee_internal_engine.proto.bin` — [preserved redacted evidence](../evidence/descriptors/782fc002de68910e00d0a32fb12cd2048aa7cc88e6114defdb11f48e62508362.bin)

**Source references:** SRC-0906, SRC-1850  
**URL references:** None independently associated  
**Related findings:** FND-13452, FND-13453

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13452"></a>
## FND-13452: chesscom.explanation_engine.v1.CeeInternalEngine.CEE_INTERNAL_ENGINE_KOMODO = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CeeInternalEngine",
  "name": "CEE_INTERNAL_ENGINE_KOMODO",
  "number": 1,
  "source_id": "SRC-0906",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0906** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_cee_internal_engine.proto.bin` — [preserved redacted evidence](../evidence/descriptors/782fc002de68910e00d0a32fb12cd2048aa7cc88e6114defdb11f48e62508362.bin)

**Source references:** SRC-0906, SRC-1850  
**URL references:** None independently associated  
**Related findings:** FND-13451, FND-13453

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13453"></a>
## FND-13453: chesscom.explanation_engine.v1.CeeInternalEngine.CEE_INTERNAL_ENGINE_TORCH = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.CeeInternalEngine",
  "name": "CEE_INTERNAL_ENGINE_TORCH",
  "number": 2,
  "source_id": "SRC-0906",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0906** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_cee_internal_engine.proto.bin` — [preserved redacted evidence](../evidence/descriptors/782fc002de68910e00d0a32fb12cd2048aa7cc88e6114defdb11f48e62508362.bin)

**Source references:** SRC-0906, SRC-1850  
**URL references:** None independently associated  
**Related findings:** FND-13451, FND-13452

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13454"></a>
## FND-13454: Native message: chesscom.explanation_engine.v1.MovePrediction

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "MovePrediction",
  "field": [
    {
      "name": "move",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    },
    {
      "name": "uci_move",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "probability",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_FLOAT"
    }
  ]
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13455, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13455"></a>
## FND-13455: chesscom.explanation_engine.v1.MovePrediction.move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MovePrediction",
  "name": "move",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0907",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13456"></a>
## FND-13456: chesscom.explanation_engine.v1.MovePrediction.uci_move = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MovePrediction",
  "name": "uci_move",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0907",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13455

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13457"></a>
## FND-13457: chesscom.explanation_engine.v1.MovePrediction.probability = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MovePrediction",
  "name": "probability",
  "number": 3,
  "type": "TYPE_FLOAT",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0907",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13455, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13458"></a>
## FND-13458: Native message: chesscom.explanation_engine.v1.CharmInferenceResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CharmInferenceResult",
  "field": [
    {
      "name": "model_key",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "elo",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "moves",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MovePrediction"
    },
    {
      "name": "expected_points",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_FLOAT"
    },
    {
      "name": "rank_probabilities",
      "number": 5,
      "label": "LABEL_REPEATED",
      "type": "TYPE_FLOAT"
    },
    {
      "name": "strength_probabilities",
      "number": 6,
      "label": "LABEL_REPEATED",
      "type": "TYPE_FLOAT"
    },
    {
      "name": "time_taken_probabilities",
      "number": 7,
      "label": "LABEL_REPEATED",
      "type": "TYPE_FLOAT"
    },
    {
      "name": "ldw_probabilities",
      "number": 8,
      "label": "LABEL_REPEATED",
      "type": "TYPE_FLOAT"
    },
    {
      "name": "strength_rating_sensitive_probabilities",
      "number": 9,
      "label": "LABEL_REPEATED",
      "type": "TYPE_FLOAT"
    },
    {
      "name": "engine_line_uci_moves",
      "number": 10,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    },
    {
      "name": "engine",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.engine.v1.Engine",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_engine"
    }
  ]
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13455, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13459"></a>
## FND-13459: chesscom.explanation_engine.v1.CharmInferenceResult.model_key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CharmInferenceResult",
  "name": "model_key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0907",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0907** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/ecf527efa5de0c30e29c215d2421868ba4f1fca3af14d9d7dfdc2773578b4dbd.bin)

**Source references:** SRC-0907, SRC-1663  
**URL references:** None independently associated  
**Related findings:** FND-13454, FND-13455, FND-13456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
