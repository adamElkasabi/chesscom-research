# native_interfaces — findings 2901–3000

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-15560"></a>
## FND-15560: chesscom.explanation_engine.v1alpha.BoardEventProfile.XRayAttack.behind = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.XRayAttack",
  "name": "behind",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1alpha.PieceDetails",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15561"></a>
## FND-15561: Native message: chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PinExploitation",
  "field": [
    {
      "name": "xray",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.BoardEventProfile.XRayAttack"
    },
    {
      "name": "exploited_piece",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceDetails",
      "oneof_index": 0
    },
    {
      "name": "exploited_square",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square",
      "oneof_index": 0
    },
    {
      "name": "direction",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation.Direction"
    }
  ],
  "enum_type": [
    {
      "name": "Direction",
      "value": [
        {
          "name": "DIRECTION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "DIRECTION_FROM_PINNED",
          "number": 1
        },
        {
          "name": "DIRECTION_AGAINST_PINNED",
          "number": 2
        },
        {
          "name": "DIRECTION_DEFENDS_PIN_TARGET",
          "number": 3
        }
      ]
    }
  ],
  "oneof_decl": [
    {
      "name": "exploited"
    }
  ]
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15562"></a>
## FND-15562: chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation.xray = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation",
  "name": "xray",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.BoardEventProfile.XRayAttack",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15563"></a>
## FND-15563: chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation.exploited_piece = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation",
  "name": "exploited_piece",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.PieceDetails",
  "label": "LABEL_OPTIONAL",
  "oneof": "exploited",
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15564"></a>
## FND-15564: chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation.exploited_square = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation",
  "name": "exploited_square",
  "number": 3,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": "exploited",
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15565"></a>
## FND-15565: chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation.direction = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation",
  "name": "direction",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation.Direction",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15566"></a>
## FND-15566: chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation.Direction.DIRECTION_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation.Direction",
  "name": "DIRECTION_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15567"></a>
## FND-15567: chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation.Direction.DIRECTION_FROM_PINNED = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation.Direction",
  "name": "DIRECTION_FROM_PINNED",
  "number": 1,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15568"></a>
## FND-15568: chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation.Direction.DIRECTION_AGAINST_PINNED = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation.Direction",
  "name": "DIRECTION_AGAINST_PINNED",
  "number": 2,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15569"></a>
## FND-15569: chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation.Direction.DIRECTION_DEFENDS_PIN_TARGET = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.BoardEventProfile.PinExploitation.Direction",
  "name": "DIRECTION_DEFENDS_PIN_TARGET",
  "number": 3,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15570"></a>
## FND-15570: Native message: chesscom.explanation_engine.v1alpha.BoardEventProfile.KingPair

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "KingPair",
  "field": [
    {
      "name": "our_king",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceDetails"
    },
    {
      "name": "their_king",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceDetails"
    }
  ]
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15571"></a>
## FND-15571: chesscom.explanation_engine.v1alpha.BoardEventProfile.KingPair.our_king = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.KingPair",
  "name": "our_king",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.PieceDetails",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15572"></a>
## FND-15572: chesscom.explanation_engine.v1alpha.BoardEventProfile.KingPair.their_king = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.KingPair",
  "name": "their_king",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.PieceDetails",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15573"></a>
## FND-15573: Native message: chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RookLine",
  "field": [
    {
      "name": "rooks",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceSet"
    },
    {
      "name": "layout",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.Layout"
    },
    {
      "name": "blockers",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceSet"
    }
  ],
  "enum_type": [
    {
      "name": "Layout",
      "value": [
        {
          "name": "LAYOUT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "LAYOUT_SINGLE_TO_FILE_ENDS",
          "number": 1
        },
        {
          "name": "LAYOUT_DOUBLED_TO_FILE_ENDS",
          "number": 2
        },
        {
          "name": "LAYOUT_LINKED",
          "number": 3
        },
        {
          "name": "LAYOUT_RANK_SWEEP",
          "number": 4
        }
      ]
    }
  ]
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15574"></a>
## FND-15574: chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.rooks = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine",
  "name": "rooks",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.PieceSet",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15575"></a>
## FND-15575: chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.layout = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine",
  "name": "layout",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.Layout",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15576"></a>
## FND-15576: chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.blockers = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine",
  "name": "blockers",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1alpha.PieceSet",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15577"></a>
## FND-15577: chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.Layout.LAYOUT_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.Layout",
  "name": "LAYOUT_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15578"></a>
## FND-15578: chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.Layout.LAYOUT_SINGLE_TO_FILE_ENDS = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.Layout",
  "name": "LAYOUT_SINGLE_TO_FILE_ENDS",
  "number": 1,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15579"></a>
## FND-15579: chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.Layout.LAYOUT_DOUBLED_TO_FILE_ENDS = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.Layout",
  "name": "LAYOUT_DOUBLED_TO_FILE_ENDS",
  "number": 2,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15580"></a>
## FND-15580: chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.Layout.LAYOUT_LINKED = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.Layout",
  "name": "LAYOUT_LINKED",
  "number": 3,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15581"></a>
## FND-15581: chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.Layout.LAYOUT_RANK_SWEEP = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.BoardEventProfile.RookLine.Layout",
  "name": "LAYOUT_RANK_SWEEP",
  "number": 4,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15582"></a>
## FND-15582: Native message: chesscom.explanation_engine.v1alpha.BoardEventProfile.FixedGeometry

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "FixedGeometry",
  "field": [
    {
      "name": "waypoints",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    },
    {
      "name": "shape",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.BoardEventProfile.FixedGeometry.Shape"
    }
  ],
  "enum_type": [
    {
      "name": "Shape",
      "value": [
        {
          "name": "SHAPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SHAPE_PATH",
          "number": 1
        },
        {
          "name": "SHAPE_LOOP",
          "number": 2
        }
      ]
    }
  ]
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15583"></a>
## FND-15583: chesscom.explanation_engine.v1alpha.BoardEventProfile.FixedGeometry.waypoints = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.FixedGeometry",
  "name": "waypoints",
  "number": 1,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15584"></a>
## FND-15584: chesscom.explanation_engine.v1alpha.BoardEventProfile.FixedGeometry.shape = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.FixedGeometry",
  "name": "shape",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.BoardEventProfile.FixedGeometry.Shape",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15585"></a>
## FND-15585: chesscom.explanation_engine.v1alpha.BoardEventProfile.FixedGeometry.Shape.SHAPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.BoardEventProfile.FixedGeometry.Shape",
  "name": "SHAPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15586"></a>
## FND-15586: chesscom.explanation_engine.v1alpha.BoardEventProfile.FixedGeometry.Shape.SHAPE_PATH = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.BoardEventProfile.FixedGeometry.Shape",
  "name": "SHAPE_PATH",
  "number": 1,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15587"></a>
## FND-15587: chesscom.explanation_engine.v1alpha.BoardEventProfile.FixedGeometry.Shape.SHAPE_LOOP = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1alpha.BoardEventProfile.FixedGeometry.Shape",
  "name": "SHAPE_LOOP",
  "number": 2,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15588"></a>
## FND-15588: Native message: chesscom.explanation_engine.v1alpha.BoardEventProfile.DefenseTriangle

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DefenseTriangle",
  "field": [
    {
      "name": "defended",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceDetails"
    },
    {
      "name": "defender",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceDetails"
    },
    {
      "name": "attacker",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceDetails"
    }
  ]
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15589"></a>
## FND-15589: chesscom.explanation_engine.v1alpha.BoardEventProfile.DefenseTriangle.defended = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.DefenseTriangle",
  "name": "defended",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.PieceDetails",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15590"></a>
## FND-15590: chesscom.explanation_engine.v1alpha.BoardEventProfile.DefenseTriangle.defender = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.DefenseTriangle",
  "name": "defender",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.PieceDetails",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15591"></a>
## FND-15591: chesscom.explanation_engine.v1alpha.BoardEventProfile.DefenseTriangle.attacker = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.DefenseTriangle",
  "name": "attacker",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1alpha.PieceDetails",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15592"></a>
## FND-15592: Native message: chesscom.explanation_engine.v1alpha.BoardEventProfile.RangeWithPieces

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RangeWithPieces",
  "field": [
    {
      "name": "range",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.BoardEventProfile.SquareRange"
    },
    {
      "name": "pieces",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.PieceSet"
    }
  ]
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15593"></a>
## FND-15593: chesscom.explanation_engine.v1alpha.BoardEventProfile.RangeWithPieces.range = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.RangeWithPieces",
  "name": "range",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.BoardEventProfile.SquareRange",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15594"></a>
## FND-15594: chesscom.explanation_engine.v1alpha.BoardEventProfile.RangeWithPieces.pieces = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.RangeWithPieces",
  "name": "pieces",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.PieceSet",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15595"></a>
## FND-15595: Native message: chesscom.explanation_engine.v1alpha.BoardEventProfile.RangeWithLocations

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RangeWithLocations",
  "field": [
    {
      "name": "range",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.BoardEventProfile.SquareRange"
    },
    {
      "name": "locations",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    }
  ]
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15596"></a>
## FND-15596: chesscom.explanation_engine.v1alpha.BoardEventProfile.RangeWithLocations.range = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.RangeWithLocations",
  "name": "range",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.BoardEventProfile.SquareRange",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15597"></a>
## FND-15597: chesscom.explanation_engine.v1alpha.BoardEventProfile.RangeWithLocations.locations = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEventProfile.RangeWithLocations",
  "name": "locations",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1042",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1042** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_event_profile.proto.bin` — [preserved redacted evidence](../evidence/descriptors/afac8d7ef94f7011cfa922e0c98edf180de5e02c828ea44e8de8b574c1117f77.bin)

**Source references:** SRC-1042, SRC-1666  
**URL references:** None independently associated  
**Related findings:** FND-15471, FND-15472, FND-15473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15598"></a>
## FND-15598: Native message: chesscom.explanation_engine.v1alpha.BoardEvent

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "BoardEvent",
  "field": [
    {
      "name": "circumstance",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.Circumstance"
    },
    {
      "name": "child_circumstance",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.Circumstance"
    },
    {
      "name": "analysis_type",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.AnalysisType"
    },
    {
      "name": "arrows_and_squares",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.ArrowsAndSquares"
    },
    {
      "name": "piece",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Piece"
    }
  ]
}

### Evidence

- **SRC-1043** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_events.proto.bin` — [preserved redacted evidence](../evidence/descriptors/639f1133b5b1e58f03dab2ea0cd0ac6dd359c1ae0bb47ffb5766321983721c06.bin)

**Source references:** SRC-1043, SRC-1840  
**URL references:** None independently associated  
**Related findings:** FND-15599, FND-15600

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15599"></a>
## FND-15599: chesscom.explanation_engine.v1alpha.BoardEvent.circumstance = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEvent",
  "name": "circumstance",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.Circumstance",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1043",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1043** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_events.proto.bin` — [preserved redacted evidence](../evidence/descriptors/639f1133b5b1e58f03dab2ea0cd0ac6dd359c1ae0bb47ffb5766321983721c06.bin)

**Source references:** SRC-1043, SRC-1840  
**URL references:** None independently associated  
**Related findings:** FND-15598, FND-15600

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15600"></a>
## FND-15600: chesscom.explanation_engine.v1alpha.BoardEvent.child_circumstance = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEvent",
  "name": "child_circumstance",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.Circumstance",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1043",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1043** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_events.proto.bin` — [preserved redacted evidence](../evidence/descriptors/639f1133b5b1e58f03dab2ea0cd0ac6dd359c1ae0bb47ffb5766321983721c06.bin)

**Source references:** SRC-1043, SRC-1840  
**URL references:** None independently associated  
**Related findings:** FND-15598, FND-15599

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15601"></a>
## FND-15601: chesscom.explanation_engine.v1alpha.BoardEvent.analysis_type = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEvent",
  "name": "analysis_type",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1alpha.AnalysisType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1043",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1043** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_events.proto.bin` — [preserved redacted evidence](../evidence/descriptors/639f1133b5b1e58f03dab2ea0cd0ac6dd359c1ae0bb47ffb5766321983721c06.bin)

**Source references:** SRC-1043, SRC-1840  
**URL references:** None independently associated  
**Related findings:** FND-15598, FND-15599, FND-15600

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15602"></a>
## FND-15602: chesscom.explanation_engine.v1alpha.BoardEvent.arrows_and_squares = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEvent",
  "name": "arrows_and_squares",
  "number": 4,
  "type": ".chesscom.chess.v1.ArrowsAndSquares",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1043",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1043** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_events.proto.bin` — [preserved redacted evidence](../evidence/descriptors/639f1133b5b1e58f03dab2ea0cd0ac6dd359c1ae0bb47ffb5766321983721c06.bin)

**Source references:** SRC-1043, SRC-1840  
**URL references:** None independently associated  
**Related findings:** FND-15598, FND-15599, FND-15600

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15603"></a>
## FND-15603: chesscom.explanation_engine.v1alpha.BoardEvent.piece = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BoardEvent",
  "name": "piece",
  "number": 5,
  "type": ".chesscom.chess.v1.Piece",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1043",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1043** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_board_events.proto.bin` — [preserved redacted evidence](../evidence/descriptors/639f1133b5b1e58f03dab2ea0cd0ac6dd359c1ae0bb47ffb5766321983721c06.bin)

**Source references:** SRC-1043, SRC-1840  
**URL references:** None independently associated  
**Related findings:** FND-15598, FND-15599, FND-15600

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15604"></a>
## FND-15604: Native message: chesscom.explanation_engine.v1alpha.BookMove

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "BookMove",
  "field": [
    {
      "name": "fen_before",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "move",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    }
  ]
}

### Evidence

- **SRC-1044** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_book_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f9bfbcc253abe08d98790ad8d5377cac793ee9d77dd51ff6c8a15f4074193495.bin)

**Source references:** SRC-1044, SRC-1825  
**URL references:** None independently associated  
**Related findings:** FND-15605, FND-15606

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15605"></a>
## FND-15605: chesscom.explanation_engine.v1alpha.BookMove.fen_before = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BookMove",
  "name": "fen_before",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1044",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1044** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_book_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f9bfbcc253abe08d98790ad8d5377cac793ee9d77dd51ff6c8a15f4074193495.bin)

**Source references:** SRC-1044, SRC-1825  
**URL references:** None independently associated  
**Related findings:** FND-15604, FND-15606

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15606"></a>
## FND-15606: chesscom.explanation_engine.v1alpha.BookMove.move = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.BookMove",
  "name": "move",
  "number": 2,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1044",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1044** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_book_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/f9bfbcc253abe08d98790ad8d5377cac793ee9d77dd51ff6c8a15f4074193495.bin)

**Source references:** SRC-1044, SRC-1825  
**URL references:** None independently associated  
**Related findings:** FND-15604, FND-15605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15607"></a>
## FND-15607: Native message: chesscom.explanation_engine.v1alpha.ApiCall

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ApiCall",
  "field": [
    {
      "name": "uid",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "get_update",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.GetUpdateCall",
      "oneof_index": 0
    },
    {
      "name": "stop",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.StopCall",
      "oneof_index": 0
    },
    {
      "name": "new_feature",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.NewFeatureCall",
      "oneof_index": 0
    },
    {
      "name": "dispose_feature",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.DisposeFeatureCall",
      "oneof_index": 0
    },
    {
      "name": "dispose_game",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.DisposeGameCall",
      "oneof_index": 0
    },
    {
      "name": "run",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.RunCall",
      "oneof_index": 0
    },
    {
      "name": "join",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.JoinCall",
      "oneof_index": 0
    },
    {
      "name": "get_last_error",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.GetLastErrorCall",
      "oneof_index": 0
    },
    {
      "name": "is_valid_game_point",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.IsValidGamePointCall",
      "oneof_index": 0
    },
    {
      "name": "init",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.InitCall",
      "oneof_index": 0
    },
    {
      "name": "init_with_opts",
      "number": 12,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.InitWithOptsCall",
      "oneof_index": 0
    },
    {
      "name": "dispose",
      "number": 13,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.DisposeCall",
      "oneof_index": 0
    },
    {
      "name": "enable_log",
      "number": 14,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.EnableLogCall",
      "oneof_index": 0
    },
    {
      "name": "disable_log",
      "number": 15,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.DisableLogCall",
      "oneof_index": 0
    },
    {
      "name": "heartbeat",
      "number": 16,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.HeartbeatCall",
      "oneof_index": 0
    },
    {
      "name": "dispose_all_games",
      "number": 17,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.DisposeAllGamesCall",
      "oneof_index": 0
    },
    {
      "name": "set_log_fd",
      "number": 18,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.SetLogFDCall",
      "oneof_index": 0
    },
    {
      "name": "set_log_file",
      "number": 19,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.SetLogFileCall",
      "oneof_index": 0
    },
    {
      "name": "add_artifact",
      "number": 20,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.AddArtifactCall",
      "oneof_index": 0
    },
    {
      "name": "add_artifact_from_file",
      "number": 21,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.AddArtifactFromFileCall",
      "oneof_index": 0
    },
    {
      "name": "dispose_artifact",
      "number": 22,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.DisposeArtifactCall",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "call"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15608"></a>
## FND-15608: chesscom.explanation_engine.v1alpha.ApiCall.uid = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "uid",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15609"></a>
## FND-15609: chesscom.explanation_engine.v1alpha.ApiCall.get_update = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "get_update",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.GetUpdateCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15610"></a>
## FND-15610: chesscom.explanation_engine.v1alpha.ApiCall.stop = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "stop",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1alpha.StopCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15611"></a>
## FND-15611: chesscom.explanation_engine.v1alpha.ApiCall.new_feature = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "new_feature",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1alpha.NewFeatureCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15612"></a>
## FND-15612: chesscom.explanation_engine.v1alpha.ApiCall.dispose_feature = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "dispose_feature",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1alpha.DisposeFeatureCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15613"></a>
## FND-15613: chesscom.explanation_engine.v1alpha.ApiCall.dispose_game = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "dispose_game",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1alpha.DisposeGameCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15614"></a>
## FND-15614: chesscom.explanation_engine.v1alpha.ApiCall.run = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "run",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1alpha.RunCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15615"></a>
## FND-15615: chesscom.explanation_engine.v1alpha.ApiCall.join = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "join",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1alpha.JoinCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15616"></a>
## FND-15616: chesscom.explanation_engine.v1alpha.ApiCall.get_last_error = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "get_last_error",
  "number": 9,
  "type": ".chesscom.explanation_engine.v1alpha.GetLastErrorCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15617"></a>
## FND-15617: chesscom.explanation_engine.v1alpha.ApiCall.is_valid_game_point = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "is_valid_game_point",
  "number": 10,
  "type": ".chesscom.explanation_engine.v1alpha.IsValidGamePointCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15618"></a>
## FND-15618: chesscom.explanation_engine.v1alpha.ApiCall.init = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "init",
  "number": 11,
  "type": ".chesscom.explanation_engine.v1alpha.InitCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15619"></a>
## FND-15619: chesscom.explanation_engine.v1alpha.ApiCall.init_with_opts = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "init_with_opts",
  "number": 12,
  "type": ".chesscom.explanation_engine.v1alpha.InitWithOptsCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15620"></a>
## FND-15620: chesscom.explanation_engine.v1alpha.ApiCall.dispose = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "dispose",
  "number": 13,
  "type": ".chesscom.explanation_engine.v1alpha.DisposeCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15621"></a>
## FND-15621: chesscom.explanation_engine.v1alpha.ApiCall.enable_log = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "enable_log",
  "number": 14,
  "type": ".chesscom.explanation_engine.v1alpha.EnableLogCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15622"></a>
## FND-15622: chesscom.explanation_engine.v1alpha.ApiCall.disable_log = 15

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "disable_log",
  "number": 15,
  "type": ".chesscom.explanation_engine.v1alpha.DisableLogCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15623"></a>
## FND-15623: chesscom.explanation_engine.v1alpha.ApiCall.heartbeat = 16

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "heartbeat",
  "number": 16,
  "type": ".chesscom.explanation_engine.v1alpha.HeartbeatCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15624"></a>
## FND-15624: chesscom.explanation_engine.v1alpha.ApiCall.dispose_all_games = 17

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "dispose_all_games",
  "number": 17,
  "type": ".chesscom.explanation_engine.v1alpha.DisposeAllGamesCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15625"></a>
## FND-15625: chesscom.explanation_engine.v1alpha.ApiCall.set_log_fd = 18

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "set_log_fd",
  "number": 18,
  "type": ".chesscom.explanation_engine.v1alpha.SetLogFDCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15626"></a>
## FND-15626: chesscom.explanation_engine.v1alpha.ApiCall.set_log_file = 19

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "set_log_file",
  "number": 19,
  "type": ".chesscom.explanation_engine.v1alpha.SetLogFileCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15627"></a>
## FND-15627: chesscom.explanation_engine.v1alpha.ApiCall.add_artifact = 20

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "add_artifact",
  "number": 20,
  "type": ".chesscom.explanation_engine.v1alpha.AddArtifactCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15628"></a>
## FND-15628: chesscom.explanation_engine.v1alpha.ApiCall.add_artifact_from_file = 21

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "add_artifact_from_file",
  "number": 21,
  "type": ".chesscom.explanation_engine.v1alpha.AddArtifactFromFileCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15629"></a>
## FND-15629: chesscom.explanation_engine.v1alpha.ApiCall.dispose_artifact = 22

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiCall",
  "name": "dispose_artifact",
  "number": 22,
  "type": ".chesscom.explanation_engine.v1alpha.DisposeArtifactCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "call",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15630"></a>
## FND-15630: Native message: chesscom.explanation_engine.v1alpha.ApiResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ApiResult",
  "field": [
    {
      "name": "uid",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "err_msg",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "get_update",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.GetUpdateResult",
      "oneof_index": 0
    },
    {
      "name": "stop",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.StopResult",
      "oneof_index": 0
    },
    {
      "name": "new_feature",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.NewFeatureResult",
      "oneof_index": 0
    },
    {
      "name": "dispose_feature",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.DisposeFeatureResult",
      "oneof_index": 0
    },
    {
      "name": "dispose_game",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.DisposeGameResult",
      "oneof_index": 0
    },
    {
      "name": "run",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.RunResult",
      "oneof_index": 0
    },
    {
      "name": "join",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.JoinResult",
      "oneof_index": 0
    },
    {
      "name": "get_last_error",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.GetLastErrorResult",
      "oneof_index": 0
    },
    {
      "name": "is_valid_game_point",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.IsValidGamePointResult",
      "oneof_index": 0
    },
    {
      "name": "init",
      "number": 12,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.InitResult",
      "oneof_index": 0
    },
    {
      "name": "init_with_opts",
      "number": 13,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.InitWithOptsResult",
      "oneof_index": 0
    },
    {
      "name": "dispose",
      "number": 14,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.DisposeResult",
      "oneof_index": 0
    },
    {
      "name": "enable_log",
      "number": 15,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.EnableLogResult",
      "oneof_index": 0
    },
    {
      "name": "disable_log",
      "number": 16,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.DisableLogResult",
      "oneof_index": 0
    },
    {
      "name": "heartbeat",
      "number": 17,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.HeartbeatResult",
      "oneof_index": 0
    },
    {
      "name": "dispose_all_games",
      "number": 18,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.DisposeAllGamesResult",
      "oneof_index": 0
    },
    {
      "name": "set_log_fd",
      "number": 19,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.SetLogFDResult",
      "oneof_index": 0
    },
    {
      "name": "set_log_file",
      "number": 20,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.SetLogFileResult",
      "oneof_index": 0
    },
    {
      "name": "add_artifact",
      "number": 21,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.AddArtifactResult",
      "oneof_index": 0
    },
    {
      "name": "add_artifact_from_file",
      "number": 22,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.AddArtifactFromFileResult",
      "oneof_index": 0
    },
    {
      "name": "dispose_artifact",
      "number": 23,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.DisposeArtifactResult",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "result"
    },
    {
      "name": "_err_msg"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15631"></a>
## FND-15631: chesscom.explanation_engine.v1alpha.ApiResult.uid = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "uid",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15632"></a>
## FND-15632: chesscom.explanation_engine.v1alpha.ApiResult.err_msg = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "err_msg",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_err_msg",
  "proto3_optional": true,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15633"></a>
## FND-15633: chesscom.explanation_engine.v1alpha.ApiResult.get_update = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "get_update",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1alpha.GetUpdateResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15634"></a>
## FND-15634: chesscom.explanation_engine.v1alpha.ApiResult.stop = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "stop",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1alpha.StopResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15635"></a>
## FND-15635: chesscom.explanation_engine.v1alpha.ApiResult.new_feature = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "new_feature",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1alpha.NewFeatureResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15636"></a>
## FND-15636: chesscom.explanation_engine.v1alpha.ApiResult.dispose_feature = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "dispose_feature",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1alpha.DisposeFeatureResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15637"></a>
## FND-15637: chesscom.explanation_engine.v1alpha.ApiResult.dispose_game = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "dispose_game",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1alpha.DisposeGameResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15638"></a>
## FND-15638: chesscom.explanation_engine.v1alpha.ApiResult.run = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "run",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1alpha.RunResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15639"></a>
## FND-15639: chesscom.explanation_engine.v1alpha.ApiResult.join = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "join",
  "number": 9,
  "type": ".chesscom.explanation_engine.v1alpha.JoinResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15640"></a>
## FND-15640: chesscom.explanation_engine.v1alpha.ApiResult.get_last_error = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "get_last_error",
  "number": 10,
  "type": ".chesscom.explanation_engine.v1alpha.GetLastErrorResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15641"></a>
## FND-15641: chesscom.explanation_engine.v1alpha.ApiResult.is_valid_game_point = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "is_valid_game_point",
  "number": 11,
  "type": ".chesscom.explanation_engine.v1alpha.IsValidGamePointResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15642"></a>
## FND-15642: chesscom.explanation_engine.v1alpha.ApiResult.init = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "init",
  "number": 12,
  "type": ".chesscom.explanation_engine.v1alpha.InitResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15643"></a>
## FND-15643: chesscom.explanation_engine.v1alpha.ApiResult.init_with_opts = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "init_with_opts",
  "number": 13,
  "type": ".chesscom.explanation_engine.v1alpha.InitWithOptsResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15644"></a>
## FND-15644: chesscom.explanation_engine.v1alpha.ApiResult.dispose = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "dispose",
  "number": 14,
  "type": ".chesscom.explanation_engine.v1alpha.DisposeResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15645"></a>
## FND-15645: chesscom.explanation_engine.v1alpha.ApiResult.enable_log = 15

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "enable_log",
  "number": 15,
  "type": ".chesscom.explanation_engine.v1alpha.EnableLogResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15646"></a>
## FND-15646: chesscom.explanation_engine.v1alpha.ApiResult.disable_log = 16

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "disable_log",
  "number": 16,
  "type": ".chesscom.explanation_engine.v1alpha.DisableLogResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15647"></a>
## FND-15647: chesscom.explanation_engine.v1alpha.ApiResult.heartbeat = 17

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "heartbeat",
  "number": 17,
  "type": ".chesscom.explanation_engine.v1alpha.HeartbeatResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15648"></a>
## FND-15648: chesscom.explanation_engine.v1alpha.ApiResult.dispose_all_games = 18

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "dispose_all_games",
  "number": 18,
  "type": ".chesscom.explanation_engine.v1alpha.DisposeAllGamesResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15649"></a>
## FND-15649: chesscom.explanation_engine.v1alpha.ApiResult.set_log_fd = 19

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "set_log_fd",
  "number": 19,
  "type": ".chesscom.explanation_engine.v1alpha.SetLogFDResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15650"></a>
## FND-15650: chesscom.explanation_engine.v1alpha.ApiResult.set_log_file = 20

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "set_log_file",
  "number": 20,
  "type": ".chesscom.explanation_engine.v1alpha.SetLogFileResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15651"></a>
## FND-15651: chesscom.explanation_engine.v1alpha.ApiResult.add_artifact = 21

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "add_artifact",
  "number": 21,
  "type": ".chesscom.explanation_engine.v1alpha.AddArtifactResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15652"></a>
## FND-15652: chesscom.explanation_engine.v1alpha.ApiResult.add_artifact_from_file = 22

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "add_artifact_from_file",
  "number": 22,
  "type": ".chesscom.explanation_engine.v1alpha.AddArtifactFromFileResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15653"></a>
## FND-15653: chesscom.explanation_engine.v1alpha.ApiResult.dispose_artifact = 23

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.ApiResult",
  "name": "dispose_artifact",
  "number": 23,
  "type": ".chesscom.explanation_engine.v1alpha.DisposeArtifactResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "result",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15654"></a>
## FND-15654: Native message: chesscom.explanation_engine.v1alpha.SearchMock

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SearchMock",
  "field": [
    {
      "name": "data",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "uid",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15655"></a>
## FND-15655: chesscom.explanation_engine.v1alpha.SearchMock.data = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.SearchMock",
  "name": "data",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15656"></a>
## FND-15656: chesscom.explanation_engine.v1alpha.SearchMock.uid = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.SearchMock",
  "name": "uid",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15657"></a>
## FND-15657: Native message: chesscom.explanation_engine.v1alpha.LogEntry

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "LogEntry",
  "field": [
    {
      "name": "time_since_cee_init_us",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "call",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.ApiCall",
      "oneof_index": 0
    },
    {
      "name": "result",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.ApiResult",
      "oneof_index": 0
    },
    {
      "name": "search_mock",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.SearchMock",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "entry"
    }
  ]
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15658"></a>
## FND-15658: chesscom.explanation_engine.v1alpha.LogEntry.time_since_cee_init_us = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.LogEntry",
  "name": "time_since_cee_init_us",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15659"></a>
## FND-15659: chesscom.explanation_engine.v1alpha.LogEntry.call = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1alpha.LogEntry",
  "name": "call",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.ApiCall",
  "label": "LABEL_OPTIONAL",
  "oneof": "entry",
  "proto3_optional": false,
  "source_id": "SRC-1045",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1045** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1alpha_c_api.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bed33058f5a16c36188203366c604fddb17369619f1b0bb04c79edb966d897fd.bin)

**Source references:** SRC-1045, SRC-1658  
**URL references:** None independently associated  
**Related findings:** FND-15607, FND-15608, FND-15609

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
