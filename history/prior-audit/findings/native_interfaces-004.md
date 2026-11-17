# native_interfaces — findings 301–400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-12960"></a>
## FND-12960: chesscom.engine.v1.Engine.ENGINE_SF16_1_NNUE = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.engine.v1.Engine",
  "name": "ENGINE_SF16_1_NNUE",
  "number": 10,
  "source_id": "SRC-0896",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0896** `research/refinement/wasm-descriptors/chesscom_engine_v1_engine.proto.bin` — [preserved redacted evidence](../evidence/descriptors/507814555389d32a65495f08838a90455b9930c48f2e9c801ddcdd7fd82c5ff6.bin)

**Source references:** SRC-0896, SRC-1698  
**URL references:** None independently associated  
**Related findings:** FND-12950, FND-12951, FND-12952

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12961"></a>
## FND-12961: chesscom.engine.v1.Engine.ENGINE_TORCH_3 = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.engine.v1.Engine",
  "name": "ENGINE_TORCH_3",
  "number": 11,
  "source_id": "SRC-0896",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0896** `research/refinement/wasm-descriptors/chesscom_engine_v1_engine.proto.bin` — [preserved redacted evidence](../evidence/descriptors/507814555389d32a65495f08838a90455b9930c48f2e9c801ddcdd7fd82c5ff6.bin)

**Source references:** SRC-0896, SRC-1698  
**URL references:** None independently associated  
**Related findings:** FND-12950, FND-12951, FND-12952

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12962"></a>
## FND-12962: chesscom.engine.v1.Engine.ENGINE_TORCH_HUMAN = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.engine.v1.Engine",
  "name": "ENGINE_TORCH_HUMAN",
  "number": 12,
  "source_id": "SRC-0896",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0896** `research/refinement/wasm-descriptors/chesscom_engine_v1_engine.proto.bin` — [preserved redacted evidence](../evidence/descriptors/507814555389d32a65495f08838a90455b9930c48f2e9c801ddcdd7fd82c5ff6.bin)

**Source references:** SRC-0896, SRC-1698  
**URL references:** None independently associated  
**Related findings:** FND-12950, FND-12951, FND-12952

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12963"></a>
## FND-12963: chesscom.engine.v1.Engine.ENGINE_SF18_NNUE = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.engine.v1.Engine",
  "name": "ENGINE_SF18_NNUE",
  "number": 13,
  "source_id": "SRC-0896",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0896** `research/refinement/wasm-descriptors/chesscom_engine_v1_engine.proto.bin` — [preserved redacted evidence](../evidence/descriptors/507814555389d32a65495f08838a90455b9930c48f2e9c801ddcdd7fd82c5ff6.bin)

**Source references:** SRC-0896, SRC-1698  
**URL references:** None independently associated  
**Related findings:** FND-12950, FND-12951, FND-12952

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12964"></a>
## FND-12964: chesscom.engine.v1.Engine.ENGINE_SF19_NNUE = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.engine.v1.Engine",
  "name": "ENGINE_SF19_NNUE",
  "number": 14,
  "source_id": "SRC-0896",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0896** `research/refinement/wasm-descriptors/chesscom_engine_v1_engine.proto.bin` — [preserved redacted evidence](../evidence/descriptors/507814555389d32a65495f08838a90455b9930c48f2e9c801ddcdd7fd82c5ff6.bin)

**Source references:** SRC-0896, SRC-1698  
**URL references:** None independently associated  
**Related findings:** FND-12950, FND-12951, FND-12952

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12965"></a>
## FND-12965: Native message: chesscom.engine.v1.Evaluation

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Evaluation",
  "field": [
    {
      "name": "score",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.engine.v1.Score"
    },
    {
      "name": "variation",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    }
  ]
}

### Evidence

- **SRC-0897** `research/refinement/wasm-descriptors/chesscom_engine_v1_evaluation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/97548bc6496023a039eb13ba840c1d7565c78d29ee875c71f5ae1ec8beb7e7ce.bin)

**Source references:** SRC-0897, SRC-1785  
**URL references:** None independently associated  
**Related findings:** FND-12966, FND-12967

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12966"></a>
## FND-12966: chesscom.engine.v1.Evaluation.score = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.engine.v1.Evaluation",
  "name": "score",
  "number": 1,
  "type": ".chesscom.engine.v1.Score",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0897",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0897** `research/refinement/wasm-descriptors/chesscom_engine_v1_evaluation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/97548bc6496023a039eb13ba840c1d7565c78d29ee875c71f5ae1ec8beb7e7ce.bin)

**Source references:** SRC-0897, SRC-1785  
**URL references:** None independently associated  
**Related findings:** FND-12965, FND-12967

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12967"></a>
## FND-12967: chesscom.engine.v1.Evaluation.variation = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.engine.v1.Evaluation",
  "name": "variation",
  "number": 2,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0897",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0897** `research/refinement/wasm-descriptors/chesscom_engine_v1_evaluation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/97548bc6496023a039eb13ba840c1d7565c78d29ee875c71f5ae1ec8beb7e7ce.bin)

**Source references:** SRC-0897, SRC-1785  
**URL references:** None independently associated  
**Related findings:** FND-12965, FND-12966

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12968"></a>
## FND-12968: Native message: chesscom.engine.v1.Score

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Score",
  "field": [
    {
      "name": "score",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Score"
    },
    {
      "name": "depth",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "nodes",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT64"
    },
    {
      "name": "engine",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.engine.v1.Engine"
    },
    {
      "name": "variation",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "strength",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.engine.v1.Strength",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_strength"
    }
  ]
}

### Evidence

- **SRC-0898** `research/refinement/wasm-descriptors/chesscom_engine_v1_score.proto.bin` — [preserved redacted evidence](../evidence/descriptors/16099927d36c6109fb364623d9839dd11647bff2accf011e1448f513f6bd4d62.bin)

**Source references:** SRC-0898, SRC-1879  
**URL references:** None independently associated  
**Related findings:** FND-12969, FND-12970

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12969"></a>
## FND-12969: chesscom.engine.v1.Score.score = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.engine.v1.Score",
  "name": "score",
  "number": 1,
  "type": ".chesscom.chess.v1.Score",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0898",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0898** `research/refinement/wasm-descriptors/chesscom_engine_v1_score.proto.bin` — [preserved redacted evidence](../evidence/descriptors/16099927d36c6109fb364623d9839dd11647bff2accf011e1448f513f6bd4d62.bin)

**Source references:** SRC-0898, SRC-1879  
**URL references:** None independently associated  
**Related findings:** FND-12968, FND-12970

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12970"></a>
## FND-12970: chesscom.engine.v1.Score.depth = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.engine.v1.Score",
  "name": "depth",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0898",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0898** `research/refinement/wasm-descriptors/chesscom_engine_v1_score.proto.bin` — [preserved redacted evidence](../evidence/descriptors/16099927d36c6109fb364623d9839dd11647bff2accf011e1448f513f6bd4d62.bin)

**Source references:** SRC-0898, SRC-1879  
**URL references:** None independently associated  
**Related findings:** FND-12968, FND-12969

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12971"></a>
## FND-12971: chesscom.engine.v1.Score.nodes = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.engine.v1.Score",
  "name": "nodes",
  "number": 6,
  "type": "TYPE_INT64",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0898",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0898** `research/refinement/wasm-descriptors/chesscom_engine_v1_score.proto.bin` — [preserved redacted evidence](../evidence/descriptors/16099927d36c6109fb364623d9839dd11647bff2accf011e1448f513f6bd4d62.bin)

**Source references:** SRC-0898, SRC-1879  
**URL references:** None independently associated  
**Related findings:** FND-12968, FND-12969, FND-12970

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12972"></a>
## FND-12972: chesscom.engine.v1.Score.engine = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.engine.v1.Score",
  "name": "engine",
  "number": 3,
  "type": ".chesscom.engine.v1.Engine",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0898",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0898** `research/refinement/wasm-descriptors/chesscom_engine_v1_score.proto.bin` — [preserved redacted evidence](../evidence/descriptors/16099927d36c6109fb364623d9839dd11647bff2accf011e1448f513f6bd4d62.bin)

**Source references:** SRC-0898, SRC-1879  
**URL references:** None independently associated  
**Related findings:** FND-12968, FND-12969, FND-12970

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12973"></a>
## FND-12973: chesscom.engine.v1.Score.variation = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.engine.v1.Score",
  "name": "variation",
  "number": 4,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0898",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0898** `research/refinement/wasm-descriptors/chesscom_engine_v1_score.proto.bin` — [preserved redacted evidence](../evidence/descriptors/16099927d36c6109fb364623d9839dd11647bff2accf011e1448f513f6bd4d62.bin)

**Source references:** SRC-0898, SRC-1879  
**URL references:** None independently associated  
**Related findings:** FND-12968, FND-12969, FND-12970

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12974"></a>
## FND-12974: chesscom.engine.v1.Score.strength = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.engine.v1.Score",
  "name": "strength",
  "number": 5,
  "type": ".chesscom.engine.v1.Strength",
  "label": "LABEL_OPTIONAL",
  "oneof": "_strength",
  "proto3_optional": true,
  "source_id": "SRC-0898",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0898** `research/refinement/wasm-descriptors/chesscom_engine_v1_score.proto.bin` — [preserved redacted evidence](../evidence/descriptors/16099927d36c6109fb364623d9839dd11647bff2accf011e1448f513f6bd4d62.bin)

**Source references:** SRC-0898, SRC-1879  
**URL references:** None independently associated  
**Related findings:** FND-12968, FND-12969, FND-12970

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12975"></a>
## FND-12975: chesscom.engine.v1.Strength.STRENGTH_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.engine.v1.Strength",
  "name": "STRENGTH_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0899",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0899** `research/refinement/wasm-descriptors/chesscom_engine_v1_strength.proto.bin` — [preserved redacted evidence](../evidence/descriptors/829d54ea69238485fdbd33643058f988ff7f77c4f3aeb48744d07d1e8d86c2ad.bin)

**Source references:** SRC-0899, SRC-1859  
**URL references:** None independently associated  
**Related findings:** FND-12976, FND-12977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12976"></a>
## FND-12976: chesscom.engine.v1.Strength.STRENGTH_FAST = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.engine.v1.Strength",
  "name": "STRENGTH_FAST",
  "number": 1,
  "source_id": "SRC-0899",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0899** `research/refinement/wasm-descriptors/chesscom_engine_v1_strength.proto.bin` — [preserved redacted evidence](../evidence/descriptors/829d54ea69238485fdbd33643058f988ff7f77c4f3aeb48744d07d1e8d86c2ad.bin)

**Source references:** SRC-0899, SRC-1859  
**URL references:** None independently associated  
**Related findings:** FND-12975, FND-12977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12977"></a>
## FND-12977: chesscom.engine.v1.Strength.STRENGTH_STANDARD = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.engine.v1.Strength",
  "name": "STRENGTH_STANDARD",
  "number": 2,
  "source_id": "SRC-0899",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0899** `research/refinement/wasm-descriptors/chesscom_engine_v1_strength.proto.bin` — [preserved redacted evidence](../evidence/descriptors/829d54ea69238485fdbd33643058f988ff7f77c4f3aeb48744d07d1e8d86c2ad.bin)

**Source references:** SRC-0899, SRC-1859  
**URL references:** None independently associated  
**Related findings:** FND-12975, FND-12976

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12978"></a>
## FND-12978: chesscom.engine.v1.Strength.STRENGTH_DEEP = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.engine.v1.Strength",
  "name": "STRENGTH_DEEP",
  "number": 3,
  "source_id": "SRC-0899",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0899** `research/refinement/wasm-descriptors/chesscom_engine_v1_strength.proto.bin` — [preserved redacted evidence](../evidence/descriptors/829d54ea69238485fdbd33643058f988ff7f77c4f3aeb48744d07d1e8d86c2ad.bin)

**Source references:** SRC-0899, SRC-1859  
**URL references:** None independently associated  
**Related findings:** FND-12975, FND-12976, FND-12977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12979"></a>
## FND-12979: chesscom.engine.v1.Strength.STRENGTH_MAXIMUM = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.engine.v1.Strength",
  "name": "STRENGTH_MAXIMUM",
  "number": 4,
  "source_id": "SRC-0899",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0899** `research/refinement/wasm-descriptors/chesscom_engine_v1_strength.proto.bin` — [preserved redacted evidence](../evidence/descriptors/829d54ea69238485fdbd33643058f988ff7f77c4f3aeb48744d07d1e8d86c2ad.bin)

**Source references:** SRC-0899, SRC-1859  
**URL references:** None independently associated  
**Related findings:** FND-12975, FND-12976, FND-12977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12980"></a>
## FND-12980: Native message: chesscom.explanation_engine.v1.PieceTypeAccuracy

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PieceTypeAccuracy",
  "field": [
    {
      "name": "piece_type",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.PieceType"
    },
    {
      "name": "accuracy_score",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    }
  ]
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12981, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12981"></a>
## FND-12981: chesscom.explanation_engine.v1.PieceTypeAccuracy.piece_type = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PieceTypeAccuracy",
  "name": "piece_type",
  "number": 1,
  "type": ".chesscom.chess.v1.PieceType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0900",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12982"></a>
## FND-12982: chesscom.explanation_engine.v1.PieceTypeAccuracy.accuracy_score = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PieceTypeAccuracy",
  "name": "accuracy_score",
  "number": 2,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0900",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12981

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12983"></a>
## FND-12983: Native message: chesscom.explanation_engine.v1.GamePhaseAccuracy

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GamePhaseAccuracy",
  "field": [
    {
      "name": "game_phase",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.GamePhase"
    },
    {
      "name": "accuracy_score",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    }
  ]
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12981, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12984"></a>
## FND-12984: chesscom.explanation_engine.v1.GamePhaseAccuracy.game_phase = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GamePhaseAccuracy",
  "name": "game_phase",
  "number": 1,
  "type": ".chesscom.chess.v1.GamePhase",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0900",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12981, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12985"></a>
## FND-12985: chesscom.explanation_engine.v1.GamePhaseAccuracy.accuracy_score = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GamePhaseAccuracy",
  "name": "accuracy_score",
  "number": 2,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0900",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12981, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12986"></a>
## FND-12986: Native message: chesscom.explanation_engine.v1.ColorAccuracy

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ColorAccuracy",
  "field": [
    {
      "name": "color",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Color"
    },
    {
      "name": "accuracy_by_piece_type",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PieceTypeAccuracy"
    },
    {
      "name": "accuracy_by_game_phase",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GamePhaseAccuracy"
    },
    {
      "name": "accuracy_overall",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    },
    {
      "name": "avg_centipawn_loss",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_DOUBLE"
    }
  ]
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12981, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12987"></a>
## FND-12987: chesscom.explanation_engine.v1.ColorAccuracy.color = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ColorAccuracy",
  "name": "color",
  "number": 1,
  "type": ".chesscom.chess.v1.Color",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0900",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12981, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12988"></a>
## FND-12988: chesscom.explanation_engine.v1.ColorAccuracy.accuracy_by_piece_type = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ColorAccuracy",
  "name": "accuracy_by_piece_type",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.PieceTypeAccuracy",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0900",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12981, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12989"></a>
## FND-12989: chesscom.explanation_engine.v1.ColorAccuracy.accuracy_by_game_phase = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ColorAccuracy",
  "name": "accuracy_by_game_phase",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.GamePhaseAccuracy",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0900",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12981, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12990"></a>
## FND-12990: chesscom.explanation_engine.v1.ColorAccuracy.accuracy_overall = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ColorAccuracy",
  "name": "accuracy_overall",
  "number": 4,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0900",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12981, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12991"></a>
## FND-12991: chesscom.explanation_engine.v1.ColorAccuracy.avg_centipawn_loss = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ColorAccuracy",
  "name": "avg_centipawn_loss",
  "number": 5,
  "type": "TYPE_DOUBLE",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0900",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12981, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12992"></a>
## FND-12992: Native message: chesscom.explanation_engine.v1.VariationAccuracy

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "VariationAccuracy",
  "field": [
    {
      "name": "accuracy_by_color",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.ColorAccuracy"
    }
  ]
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12981, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12993"></a>
## FND-12993: chesscom.explanation_engine.v1.VariationAccuracy.accuracy_by_color = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.VariationAccuracy",
  "name": "accuracy_by_color",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.ColorAccuracy",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0900",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12981, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12994"></a>
## FND-12994: chesscom.explanation_engine.v1.AccuracyAlgorithm.ACCURACY_ALGORITHM_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AccuracyAlgorithm",
  "name": "ACCURACY_ALGORITHM_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0900",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12981, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12995"></a>
## FND-12995: chesscom.explanation_engine.v1.AccuracyAlgorithm.ACCURACY_ALGORITHM_CAPS2 = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AccuracyAlgorithm",
  "name": "ACCURACY_ALGORITHM_CAPS2",
  "number": 1,
  "source_id": "SRC-0900",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0900** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_accuracy.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9b6c96aa5704780229e47bc833fafad0f369f7ed5540c106b3ee804e4f495029.bin)

**Source references:** SRC-0900, SRC-1883  
**URL references:** None independently associated  
**Related findings:** FND-12980, FND-12981, FND-12982

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12996"></a>
## FND-12996: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12997"></a>
## FND-12997: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_STALEMATE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_STALEMATE",
  "number": 1,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12998"></a>
## FND-12998: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FIFTY_MOVE = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_FIFTY_MOVE",
  "number": 2,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12999"></a>
## FND-12999: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_REPETITION = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_REPETITION",
  "number": 3,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13000"></a>
## FND-13000: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_INSUFFICIENT = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_INSUFFICIENT",
  "number": 4,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13001"></a>
## FND-13001: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE",
  "number": 5,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13002"></a>
## FND-13002: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE",
  "number": 6,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13003"></a>
## FND-13003: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_IGNORES_THREAT = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_IGNORES_THREAT",
  "number": 7,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13004"></a>
## FND-13004: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_INDIRECT_SACRIFICE = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_INDIRECT_SACRIFICE",
  "number": 8,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13005"></a>
## FND-13005: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CHECKMATE = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_CHECKMATE",
  "number": 9,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13006"></a>
## FND-13006: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORCES_MATE = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_FORCES_MATE",
  "number": 11,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13007"></a>
## FND-13007: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE",
  "number": 12,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13008"></a>
## FND-13008: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_SLOWER_MATE = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_SLOWER_MATE",
  "number": 14,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13009"></a>
## FND-13009: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_STILL_MATE = 15

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_STILL_MATE",
  "number": 15,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13010"></a>
## FND-13010: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MATE_THREAT = 16

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_MATE_THREAT",
  "number": 16,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13011"></a>
## FND-13011: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_INTERESTING = 17

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_INTERESTING",
  "number": 17,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13012"></a>
## FND-13012: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FREE_PIECE = 18

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_FREE_PIECE",
  "number": 18,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13013"></a>
## FND-13013: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_QUASI_FREE_PIECE = 19

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_QUASI_FREE_PIECE",
  "number": 19,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13014"></a>
## FND-13014: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK = 20

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK",
  "number": 20,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13015"></a>
## FND-13015: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORK_WITH_MATE = 21

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_FORK_WITH_MATE",
  "number": 21,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13016"></a>
## FND-13016: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORK = 22

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_FORK",
  "number": 22,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13017"></a>
## FND-13017: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MULTI_ATTACK = 23

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_MULTI_ATTACK",
  "number": 23,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13018"></a>
## FND-13018: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_SKEWER = 24

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_SKEWER",
  "number": 24,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13019"></a>
## FND-13019: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DOUBLE_CHECK = 25

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_DOUBLE_CHECK",
  "number": 25,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13020"></a>
## FND-13020: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT = 26

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT",
  "number": 26,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13021"></a>
## FND-13021: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DISCOVERED_ATTACK = 27

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_DISCOVERED_ATTACK",
  "number": 27,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13022"></a>
## FND-13022: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PROMOTION = 28

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_PROMOTION",
  "number": 28,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13023"></a>
## FND-13023: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DISCOVERED_CHECK = 29

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_DISCOVERED_CHECK",
  "number": 29,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13024"></a>
## FND-13024: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE = 30

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE",
  "number": 30,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13025"></a>
## FND-13025: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_THREATENS_PINNED = 31

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_THREATENS_PINNED",
  "number": 31,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13026"></a>
## FND-13026: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PAWNS = 32

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PAWNS",
  "number": 32,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13027"></a>
## FND-13027: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORCES_DOUBLED_PAWNS = 33

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_FORCES_DOUBLED_PAWNS",
  "number": 33,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13028"></a>
## FND-13028: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORCES_ISOLATED_PAWN = 34

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_FORCES_ISOLATED_PAWN",
  "number": 34,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13029"></a>
## FND-13029: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_EQUAL_TRADE = 35

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_EQUAL_TRADE",
  "number": 35,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13030"></a>
## FND-13030: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_IMMEDIATE_RECAPTURE = 36

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_IMMEDIATE_RECAPTURE",
  "number": 36,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13031"></a>
## FND-13031: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_OBVIOUS_RECAPTURE = 37

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_OBVIOUS_RECAPTURE",
  "number": 37,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13032"></a>
## FND-13032: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CAPTURES_CHECKER = 38

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_CAPTURES_CHECKER",
  "number": 38,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13033"></a>
## FND-13033: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_COUNTER_THREAT = 39

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_COUNTER_THREAT",
  "number": 39,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13034"></a>
## FND-13034: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_REMOVES_ATTACKER = 40

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_REMOVES_ATTACKER",
  "number": 40,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13035"></a>
## FND-13035: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BLOCKS_ATTACKER = 41

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_BLOCKS_ATTACKER",
  "number": 41,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13036"></a>
## FND-13036: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_UNPINS_DEFENDER = 42

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_UNPINS_DEFENDER",
  "number": 42,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13037"></a>
## FND-13037: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PINS_ATTACKER = 43

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_PINS_ATTACKER",
  "number": 43,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13038"></a>
## FND-13038: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PIN = 44

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_PIN",
  "number": 44,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13039"></a>
## FND-13039: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_RELATIVE_PIN = 45

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_RELATIVE_PIN",
  "number": 45,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13040"></a>
## FND-13040: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PROTECTS_PIECE = 46

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_PROTECTS_PIECE",
  "number": 46,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13041"></a>
## FND-13041: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DEFENDS_PIECE = 47

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_DEFENDS_PIECE",
  "number": 47,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13042"></a>
## FND-13042: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CREATES_LUFT = 48

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_CREATES_LUFT",
  "number": 48,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13043"></a>
## FND-13043: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_GAMBITS_PAWN = 49

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_GAMBITS_PAWN",
  "number": 49,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13044"></a>
## FND-13044: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER = 50

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER",
  "number": 50,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13045"></a>
## FND-13045: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_STRIKES_AT_CENTER = 51

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_STRIKES_AT_CENTER",
  "number": 51,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13046"></a>
## FND-13046: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MAKES_PASSED_PAWN = 52

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_MAKES_PASSED_PAWN",
  "number": 52,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13047"></a>
## FND-13047: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PREVENTS_CASTLING = 53

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_PREVENTS_CASTLING",
  "number": 53,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13048"></a>
## FND-13048: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_TAKES_OUTPOST = 54

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_TAKES_OUTPOST",
  "number": 54,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13049"></a>
## FND-13049: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CHALLENGES_OPEN_FILE = 55

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_CHALLENGES_OPEN_FILE",
  "number": 55,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13050"></a>
## FND-13050: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_TAKES_OPEN_FILE = 56

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_TAKES_OPEN_FILE",
  "number": 56,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13051"></a>
## FND-13051: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ROOK_BEHIND_OWN_PAWN = 57

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_ROOK_BEHIND_OWN_PAWN",
  "number": 57,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13052"></a>
## FND-13052: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN = 58

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN",
  "number": 58,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13053"></a>
## FND-13053: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BLOCKS_CHECKER = 59

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_BLOCKS_CHECKER",
  "number": 59,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13054"></a>
## FND-13054: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_KICKS_CHECKER = 60

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_KICKS_CHECKER",
  "number": 60,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13055"></a>
## FND-13055: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_EVADES_CHECK = 61

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_EVADES_CHECK",
  "number": 61,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13056"></a>
## FND-13056: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_KICKS = 62

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_KICKS",
  "number": 62,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13057"></a>
## FND-13057: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ROOK_ON_SEVENTH = 63

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_ROOK_ON_SEVENTH",
  "number": 63,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13058"></a>
## FND-13058: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO = 64

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO",
  "number": 64,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13059"></a>
## FND-13059: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_WINS_TEMPO = 65

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnalysisType",
  "name": "ANALYSIS_TYPE_WINS_TEMPO",
  "number": 65,
  "source_id": "SRC-0901",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0901** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_analysis_type.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9e3d03487aadcf45e729e8c1a7a331feb5630b8fe4d96d7e53876d171891410e.bin)

**Source references:** SRC-0901, SRC-1661  
**URL references:** None independently associated  
**Related findings:** FND-12996, FND-12997, FND-12998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
