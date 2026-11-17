# native_interfaces — findings 2001–2100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-14660"></a>
## FND-14660: chesscom.explanation_engine.v1.InternalFeatureSetMoveAnnotationsRequest.annotation = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureSetMoveAnnotationsRequest",
  "name": "annotation",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.MoveAnnotation",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1012",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1012** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_set_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/20a5bf1004ba4f91a6bd73da074d2b845b6208aae7b1169f69e82d3f3ba6d87c.bin)

**Source references:** SRC-1012, SRC-1895  
**URL references:** None independently associated  
**Related findings:** FND-14659, FND-14661

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14661"></a>
## FND-14661: Native message: chesscom.explanation_engine.v1.InternalFeatureSetMoveAnnotationsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureSetMoveAnnotationsResponse"
}

### Evidence

- **SRC-1012** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_set_move_annotations.proto.bin` — [preserved redacted evidence](../evidence/descriptors/20a5bf1004ba4f91a6bd73da074d2b845b6208aae7b1169f69e82d3f3ba6d87c.bin)

**Source references:** SRC-1012, SRC-1895  
**URL references:** None independently associated  
**Related findings:** FND-14659, FND-14660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14662"></a>
## FND-14662: Native message: chesscom.explanation_engine.v1.InternalFeatureUciToGameStateRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureUciToGameStateRequest",
  "field": [
    {
      "name": "uci_commands",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1013** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_uci_to_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/864d80fab9d2fe5bc4e6b24589cf58b35e9ea74b301f4f5514fe1685d962be3c.bin)

**Source references:** SRC-1013, SRC-1827  
**URL references:** None independently associated  
**Related findings:** FND-14663, FND-14664

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14663"></a>
## FND-14663: chesscom.explanation_engine.v1.InternalFeatureUciToGameStateRequest.uci_commands = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureUciToGameStateRequest",
  "name": "uci_commands",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1013",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1013** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_uci_to_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/864d80fab9d2fe5bc4e6b24589cf58b35e9ea74b301f4f5514fe1685d962be3c.bin)

**Source references:** SRC-1013, SRC-1827  
**URL references:** None independently associated  
**Related findings:** FND-14662, FND-14664

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14664"></a>
## FND-14664: Native message: chesscom.explanation_engine.v1.InternalFeatureUciToGameStateResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureUciToGameStateResponse",
  "field": [
    {
      "name": "game_state",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameState"
    }
  ]
}

### Evidence

- **SRC-1013** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_uci_to_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/864d80fab9d2fe5bc4e6b24589cf58b35e9ea74b301f4f5514fe1685d962be3c.bin)

**Source references:** SRC-1013, SRC-1827  
**URL references:** None independently associated  
**Related findings:** FND-14662, FND-14663

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14665"></a>
## FND-14665: chesscom.explanation_engine.v1.InternalFeatureUciToGameStateResponse.game_state = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureUciToGameStateResponse",
  "name": "game_state",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GameState",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1013",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1013** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_uci_to_game_state.proto.bin` — [preserved redacted evidence](../evidence/descriptors/864d80fab9d2fe5bc4e6b24589cf58b35e9ea74b301f4f5514fe1685d962be3c.bin)

**Source references:** SRC-1013, SRC-1827  
**URL references:** None independently associated  
**Related findings:** FND-14662, FND-14663, FND-14664

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14666"></a>
## FND-14666: Native message: chesscom.explanation_engine.v1.InternalFeatureUpdateDeveloperOptionsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureUpdateDeveloperOptionsRequest",
  "field": [
    {
      "name": "options",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.DeveloperOptions"
    }
  ]
}

### Evidence

- **SRC-1014** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_update_developer_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7b42314c945256cfb703a946041221c2246a2e807e2c848b85ccd7c5db72843b.bin)

**Source references:** SRC-1014, SRC-1792  
**URL references:** None independently associated  
**Related findings:** FND-14667, FND-14668

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14667"></a>
## FND-14667: chesscom.explanation_engine.v1.InternalFeatureUpdateDeveloperOptionsRequest.options = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureUpdateDeveloperOptionsRequest",
  "name": "options",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.DeveloperOptions",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1014",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1014** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_update_developer_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7b42314c945256cfb703a946041221c2246a2e807e2c848b85ccd7c5db72843b.bin)

**Source references:** SRC-1014, SRC-1792  
**URL references:** None independently associated  
**Related findings:** FND-14666, FND-14668

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14668"></a>
## FND-14668: Native message: chesscom.explanation_engine.v1.InternalFeatureUpdateDeveloperOptionsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureUpdateDeveloperOptionsResponse",
  "field": [
    {
      "name": "options",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.DeveloperOptions"
    }
  ]
}

### Evidence

- **SRC-1014** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_update_developer_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7b42314c945256cfb703a946041221c2246a2e807e2c848b85ccd7c5db72843b.bin)

**Source references:** SRC-1014, SRC-1792  
**URL references:** None independently associated  
**Related findings:** FND-14666, FND-14667

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14669"></a>
## FND-14669: chesscom.explanation_engine.v1.InternalFeatureUpdateDeveloperOptionsResponse.options = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureUpdateDeveloperOptionsResponse",
  "name": "options",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.DeveloperOptions",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1014",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1014** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_update_developer_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7b42314c945256cfb703a946041221c2246a2e807e2c848b85ccd7c5db72843b.bin)

**Source references:** SRC-1014, SRC-1792  
**URL references:** None independently associated  
**Related findings:** FND-14666, FND-14667, FND-14668

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14670"></a>
## FND-14670: Native message: chesscom.explanation_engine.v1.DeveloperOptions

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "DeveloperOptions",
  "field": [
    {
      "name": "coach_debug_info",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "assume_speech_always_present",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_coach_debug_info"
    },
    {
      "name": "_assume_speech_always_present"
    }
  ],
  "reserved_range": [
    {
      "start": 1,
      "end": 3
    }
  ]
}

### Evidence

- **SRC-1014** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_update_developer_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7b42314c945256cfb703a946041221c2246a2e807e2c848b85ccd7c5db72843b.bin)

**Source references:** SRC-1014, SRC-1792  
**URL references:** None independently associated  
**Related findings:** FND-14666, FND-14667, FND-14668

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14671"></a>
## FND-14671: chesscom.explanation_engine.v1.DeveloperOptions.coach_debug_info = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.DeveloperOptions",
  "name": "coach_debug_info",
  "number": 3,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_coach_debug_info",
  "proto3_optional": true,
  "source_id": "SRC-1014",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1014** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_update_developer_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7b42314c945256cfb703a946041221c2246a2e807e2c848b85ccd7c5db72843b.bin)

**Source references:** SRC-1014, SRC-1792  
**URL references:** None independently associated  
**Related findings:** FND-14666, FND-14667, FND-14668

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14672"></a>
## FND-14672: chesscom.explanation_engine.v1.DeveloperOptions.assume_speech_always_present = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.DeveloperOptions",
  "name": "assume_speech_always_present",
  "number": 4,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_assume_speech_always_present",
  "proto3_optional": true,
  "source_id": "SRC-1014",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1014** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_update_developer_options.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7b42314c945256cfb703a946041221c2246a2e807e2c848b85ccd7c5db72843b.bin)

**Source references:** SRC-1014, SRC-1792  
**URL references:** None independently associated  
**Related findings:** FND-14666, FND-14667, FND-14668

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14673"></a>
## FND-14673: Native message: chesscom.explanation_engine.v1.InternalFeatureWebDemoJsonRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureWebDemoJsonRequest"
}

### Evidence

- **SRC-1016** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_web_demo_json.proto.bin` — [preserved redacted evidence](../evidence/descriptors/880b17ac8cf50960d505e543a69620a2678d5b1cf017344382821f75ca22da39.bin)

**Source references:** SRC-1016, SRC-1897  
**URL references:** None independently associated  
**Related findings:** FND-14674, FND-14675

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14674"></a>
## FND-14674: Native message: chesscom.explanation_engine.v1.InternalFeatureWebDemoJsonResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureWebDemoJsonResponse",
  "field": [
    {
      "name": "web_demo_json",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1016** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_web_demo_json.proto.bin` — [preserved redacted evidence](../evidence/descriptors/880b17ac8cf50960d505e543a69620a2678d5b1cf017344382821f75ca22da39.bin)

**Source references:** SRC-1016, SRC-1897  
**URL references:** None independently associated  
**Related findings:** FND-14673, FND-14675

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14675"></a>
## FND-14675: chesscom.explanation_engine.v1.InternalFeatureWebDemoJsonResponse.web_demo_json = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InternalFeatureWebDemoJsonResponse",
  "name": "web_demo_json",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1016",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1016** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_internal_feature_web_demo_json.proto.bin` — [preserved redacted evidence](../evidence/descriptors/880b17ac8cf50960d505e543a69620a2678d5b1cf017344382821f75ca22da39.bin)

**Source references:** SRC-1016, SRC-1897  
**URL references:** None independently associated  
**Related findings:** FND-14673, FND-14674

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14676"></a>
## FND-14676: Native message: chesscom.explanation_engine.v1.InvalidGameUnparsable

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InvalidGameUnparsable"
}

### Evidence

- **SRC-1017** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_invalid_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0af799a6d67c915037ab095243286f91e0811374b28655eb16a6367263238834.bin)

**Source references:** SRC-1017, SRC-1844  
**URL references:** None independently associated  
**Related findings:** FND-14677, FND-14678

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14677"></a>
## FND-14677: Native message: chesscom.explanation_engine.v1.InvalidGameIllegalMove

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InvalidGameIllegalMove"
}

### Evidence

- **SRC-1017** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_invalid_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0af799a6d67c915037ab095243286f91e0811374b28655eb16a6367263238834.bin)

**Source references:** SRC-1017, SRC-1844  
**URL references:** None independently associated  
**Related findings:** FND-14676, FND-14678

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14678"></a>
## FND-14678: Native message: chesscom.explanation_engine.v1.InvalidGameIllegalKingCount

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InvalidGameIllegalKingCount"
}

### Evidence

- **SRC-1017** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_invalid_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0af799a6d67c915037ab095243286f91e0811374b28655eb16a6367263238834.bin)

**Source references:** SRC-1017, SRC-1844  
**URL references:** None independently associated  
**Related findings:** FND-14676, FND-14677

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14679"></a>
## FND-14679: Native message: chesscom.explanation_engine.v1.InvalidGamePawnOnBackRank

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InvalidGamePawnOnBackRank"
}

### Evidence

- **SRC-1017** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_invalid_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0af799a6d67c915037ab095243286f91e0811374b28655eb16a6367263238834.bin)

**Source references:** SRC-1017, SRC-1844  
**URL references:** None independently associated  
**Related findings:** FND-14676, FND-14677, FND-14678

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14680"></a>
## FND-14680: Native message: chesscom.explanation_engine.v1.InvalidGameKingsAdjacent

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InvalidGameKingsAdjacent"
}

### Evidence

- **SRC-1017** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_invalid_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0af799a6d67c915037ab095243286f91e0811374b28655eb16a6367263238834.bin)

**Source references:** SRC-1017, SRC-1844  
**URL references:** None independently associated  
**Related findings:** FND-14676, FND-14677, FND-14678

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14681"></a>
## FND-14681: Native message: chesscom.explanation_engine.v1.InvalidGameKingCapturable

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InvalidGameKingCapturable"
}

### Evidence

- **SRC-1017** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_invalid_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0af799a6d67c915037ab095243286f91e0811374b28655eb16a6367263238834.bin)

**Source references:** SRC-1017, SRC-1844  
**URL references:** None independently associated  
**Related findings:** FND-14676, FND-14677, FND-14678

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14682"></a>
## FND-14682: Native message: chesscom.explanation_engine.v1.InvalidGame

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InvalidGame",
  "field": [
    {
      "name": "unparsable",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.InvalidGameUnparsable",
      "oneof_index": 0
    },
    {
      "name": "illegal_move",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.InvalidGameIllegalMove",
      "oneof_index": 0
    },
    {
      "name": "illegal_king_count",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.InvalidGameIllegalKingCount",
      "oneof_index": 0
    },
    {
      "name": "pawn_on_back_rank",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.InvalidGamePawnOnBackRank",
      "oneof_index": 0
    },
    {
      "name": "kings_adjacent",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.InvalidGameKingsAdjacent",
      "oneof_index": 0
    },
    {
      "name": "king_capturable",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.InvalidGameKingCapturable",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "invalid_game"
    }
  ]
}

### Evidence

- **SRC-1017** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_invalid_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0af799a6d67c915037ab095243286f91e0811374b28655eb16a6367263238834.bin)

**Source references:** SRC-1017, SRC-1844  
**URL references:** None independently associated  
**Related findings:** FND-14676, FND-14677, FND-14678

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14683"></a>
## FND-14683: chesscom.explanation_engine.v1.InvalidGame.unparsable = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InvalidGame",
  "name": "unparsable",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.InvalidGameUnparsable",
  "label": "LABEL_OPTIONAL",
  "oneof": "invalid_game",
  "proto3_optional": false,
  "source_id": "SRC-1017",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1017** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_invalid_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0af799a6d67c915037ab095243286f91e0811374b28655eb16a6367263238834.bin)

**Source references:** SRC-1017, SRC-1844  
**URL references:** None independently associated  
**Related findings:** FND-14676, FND-14677, FND-14678

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14684"></a>
## FND-14684: chesscom.explanation_engine.v1.InvalidGame.illegal_move = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InvalidGame",
  "name": "illegal_move",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.InvalidGameIllegalMove",
  "label": "LABEL_OPTIONAL",
  "oneof": "invalid_game",
  "proto3_optional": false,
  "source_id": "SRC-1017",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1017** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_invalid_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0af799a6d67c915037ab095243286f91e0811374b28655eb16a6367263238834.bin)

**Source references:** SRC-1017, SRC-1844  
**URL references:** None independently associated  
**Related findings:** FND-14676, FND-14677, FND-14678

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14685"></a>
## FND-14685: chesscom.explanation_engine.v1.InvalidGame.illegal_king_count = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InvalidGame",
  "name": "illegal_king_count",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.InvalidGameIllegalKingCount",
  "label": "LABEL_OPTIONAL",
  "oneof": "invalid_game",
  "proto3_optional": false,
  "source_id": "SRC-1017",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1017** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_invalid_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0af799a6d67c915037ab095243286f91e0811374b28655eb16a6367263238834.bin)

**Source references:** SRC-1017, SRC-1844  
**URL references:** None independently associated  
**Related findings:** FND-14676, FND-14677, FND-14678

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14686"></a>
## FND-14686: chesscom.explanation_engine.v1.InvalidGame.pawn_on_back_rank = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InvalidGame",
  "name": "pawn_on_back_rank",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.InvalidGamePawnOnBackRank",
  "label": "LABEL_OPTIONAL",
  "oneof": "invalid_game",
  "proto3_optional": false,
  "source_id": "SRC-1017",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1017** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_invalid_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0af799a6d67c915037ab095243286f91e0811374b28655eb16a6367263238834.bin)

**Source references:** SRC-1017, SRC-1844  
**URL references:** None independently associated  
**Related findings:** FND-14676, FND-14677, FND-14678

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14687"></a>
## FND-14687: chesscom.explanation_engine.v1.InvalidGame.kings_adjacent = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InvalidGame",
  "name": "kings_adjacent",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.InvalidGameKingsAdjacent",
  "label": "LABEL_OPTIONAL",
  "oneof": "invalid_game",
  "proto3_optional": false,
  "source_id": "SRC-1017",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1017** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_invalid_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0af799a6d67c915037ab095243286f91e0811374b28655eb16a6367263238834.bin)

**Source references:** SRC-1017, SRC-1844  
**URL references:** None independently associated  
**Related findings:** FND-14676, FND-14677, FND-14678

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14688"></a>
## FND-14688: chesscom.explanation_engine.v1.InvalidGame.king_capturable = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.InvalidGame",
  "name": "king_capturable",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.InvalidGameKingCapturable",
  "label": "LABEL_OPTIONAL",
  "oneof": "invalid_game",
  "proto3_optional": false,
  "source_id": "SRC-1017",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1017** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_invalid_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0af799a6d67c915037ab095243286f91e0811374b28655eb16a6367263238834.bin)

**Source references:** SRC-1017, SRC-1844  
**URL references:** None independently associated  
**Related findings:** FND-14676, FND-14677, FND-14678

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14689"></a>
## FND-14689: chesscom.explanation_engine.v1.Locale.LOCALE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Locale",
  "name": "LOCALE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1018",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1018** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_language.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8151d009218a3b165b662baf79104eedb094a48fe2614b3b958793aa563cc953.bin)

**Source references:** SRC-1018, SRC-1717  
**URL references:** None independently associated  
**Related findings:** FND-14690, FND-14691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14690"></a>
## FND-14690: chesscom.explanation_engine.v1.Locale.LOCALE_DE_DE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Locale",
  "name": "LOCALE_DE_DE",
  "number": 1,
  "source_id": "SRC-1018",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1018** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_language.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8151d009218a3b165b662baf79104eedb094a48fe2614b3b958793aa563cc953.bin)

**Source references:** SRC-1018, SRC-1717  
**URL references:** None independently associated  
**Related findings:** FND-14689, FND-14691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14691"></a>
## FND-14691: chesscom.explanation_engine.v1.Locale.LOCALE_EN_US = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Locale",
  "name": "LOCALE_EN_US",
  "number": 2,
  "source_id": "SRC-1018",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1018** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_language.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8151d009218a3b165b662baf79104eedb094a48fe2614b3b958793aa563cc953.bin)

**Source references:** SRC-1018, SRC-1717  
**URL references:** None independently associated  
**Related findings:** FND-14689, FND-14690

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14692"></a>
## FND-14692: chesscom.explanation_engine.v1.Locale.LOCALE_ES_ES = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Locale",
  "name": "LOCALE_ES_ES",
  "number": 3,
  "source_id": "SRC-1018",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1018** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_language.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8151d009218a3b165b662baf79104eedb094a48fe2614b3b958793aa563cc953.bin)

**Source references:** SRC-1018, SRC-1717  
**URL references:** None independently associated  
**Related findings:** FND-14689, FND-14690, FND-14691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14693"></a>
## FND-14693: chesscom.explanation_engine.v1.Locale.LOCALE_FR_FR = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Locale",
  "name": "LOCALE_FR_FR",
  "number": 4,
  "source_id": "SRC-1018",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1018** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_language.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8151d009218a3b165b662baf79104eedb094a48fe2614b3b958793aa563cc953.bin)

**Source references:** SRC-1018, SRC-1717  
**URL references:** None independently associated  
**Related findings:** FND-14689, FND-14690, FND-14691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14694"></a>
## FND-14694: chesscom.explanation_engine.v1.Locale.LOCALE_IT_IT = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Locale",
  "name": "LOCALE_IT_IT",
  "number": 5,
  "source_id": "SRC-1018",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1018** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_language.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8151d009218a3b165b662baf79104eedb094a48fe2614b3b958793aa563cc953.bin)

**Source references:** SRC-1018, SRC-1717  
**URL references:** None independently associated  
**Related findings:** FND-14689, FND-14690, FND-14691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14695"></a>
## FND-14695: chesscom.explanation_engine.v1.Locale.LOCALE_PL_PL = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Locale",
  "name": "LOCALE_PL_PL",
  "number": 6,
  "source_id": "SRC-1018",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1018** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_language.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8151d009218a3b165b662baf79104eedb094a48fe2614b3b958793aa563cc953.bin)

**Source references:** SRC-1018, SRC-1717  
**URL references:** None independently associated  
**Related findings:** FND-14689, FND-14690, FND-14691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14696"></a>
## FND-14696: chesscom.explanation_engine.v1.Locale.LOCALE_PT_PT = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Locale",
  "name": "LOCALE_PT_PT",
  "number": 7,
  "source_id": "SRC-1018",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1018** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_language.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8151d009218a3b165b662baf79104eedb094a48fe2614b3b958793aa563cc953.bin)

**Source references:** SRC-1018, SRC-1717  
**URL references:** None independently associated  
**Related findings:** FND-14689, FND-14690, FND-14691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14697"></a>
## FND-14697: chesscom.explanation_engine.v1.Locale.LOCALE_RU_RU = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Locale",
  "name": "LOCALE_RU_RU",
  "number": 8,
  "source_id": "SRC-1018",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1018** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_language.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8151d009218a3b165b662baf79104eedb094a48fe2614b3b958793aa563cc953.bin)

**Source references:** SRC-1018, SRC-1717  
**URL references:** None independently associated  
**Related findings:** FND-14689, FND-14690, FND-14691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14698"></a>
## FND-14698: chesscom.explanation_engine.v1.Locale.LOCALE_TR_TR = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Locale",
  "name": "LOCALE_TR_TR",
  "number": 9,
  "source_id": "SRC-1018",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1018** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_language.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8151d009218a3b165b662baf79104eedb094a48fe2614b3b958793aa563cc953.bin)

**Source references:** SRC-1018, SRC-1717  
**URL references:** None independently associated  
**Related findings:** FND-14689, FND-14690, FND-14691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14699"></a>
## FND-14699: chesscom.explanation_engine.v1.Locale.LOCALE_AR_SA = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Locale",
  "name": "LOCALE_AR_SA",
  "number": 10,
  "source_id": "SRC-1018",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1018** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_language.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8151d009218a3b165b662baf79104eedb094a48fe2614b3b958793aa563cc953.bin)

**Source references:** SRC-1018, SRC-1717  
**URL references:** None independently associated  
**Related findings:** FND-14689, FND-14690, FND-14691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14700"></a>
## FND-14700: chesscom.explanation_engine.v1.Locale.LOCALE_ID_ID = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Locale",
  "name": "LOCALE_ID_ID",
  "number": 11,
  "source_id": "SRC-1018",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1018** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_language.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8151d009218a3b165b662baf79104eedb094a48fe2614b3b958793aa563cc953.bin)

**Source references:** SRC-1018, SRC-1717  
**URL references:** None independently associated  
**Related findings:** FND-14689, FND-14690, FND-14691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14701"></a>
## FND-14701: chesscom.explanation_engine.v1.Locale.LOCALE_KO_KR = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Locale",
  "name": "LOCALE_KO_KR",
  "number": 12,
  "source_id": "SRC-1018",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1018** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_language.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8151d009218a3b165b662baf79104eedb094a48fe2614b3b958793aa563cc953.bin)

**Source references:** SRC-1018, SRC-1717  
**URL references:** None independently associated  
**Related findings:** FND-14689, FND-14690, FND-14691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14702"></a>
## FND-14702: Native message: chesscom.explanation_engine.v1.AnnotationArrow

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AnnotationArrow",
  "field": [
    {
      "name": "from",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    },
    {
      "name": "to",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    },
    {
      "name": "color",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.AnnotationColor"
    }
  ]
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14703"></a>
## FND-14703: chesscom.explanation_engine.v1.AnnotationArrow.from = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AnnotationArrow",
  "name": "from",
  "number": 1,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14704"></a>
## FND-14704: chesscom.explanation_engine.v1.AnnotationArrow.to = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AnnotationArrow",
  "name": "to",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14705"></a>
## FND-14705: chesscom.explanation_engine.v1.AnnotationArrow.color = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AnnotationArrow",
  "name": "color",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.AnnotationColor",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14706"></a>
## FND-14706: Native message: chesscom.explanation_engine.v1.AnnotationSquare

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AnnotationSquare",
  "field": [
    {
      "name": "square",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    },
    {
      "name": "color",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.AnnotationColor"
    }
  ]
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14707"></a>
## FND-14707: chesscom.explanation_engine.v1.AnnotationSquare.square = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AnnotationSquare",
  "name": "square",
  "number": 1,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14708"></a>
## FND-14708: chesscom.explanation_engine.v1.AnnotationSquare.color = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.AnnotationSquare",
  "name": "color",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.AnnotationColor",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14709"></a>
## FND-14709: Native message: chesscom.explanation_engine.v1.MoveAnnotation

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "MoveAnnotation",
  "field": [
    {
      "name": "comments",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    },
    {
      "name": "before_comment",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "nags",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_INT32"
    },
    {
      "name": "arrows",
      "number": 4,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.AnnotationArrow"
    },
    {
      "name": "highlighted_squares",
      "number": 5,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.AnnotationSquare"
    }
  ],
  "oneof_decl": [
    {
      "name": "_before_comment"
    }
  ]
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14710"></a>
## FND-14710: chesscom.explanation_engine.v1.MoveAnnotation.comments = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveAnnotation",
  "name": "comments",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14711"></a>
## FND-14711: chesscom.explanation_engine.v1.MoveAnnotation.before_comment = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveAnnotation",
  "name": "before_comment",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_before_comment",
  "proto3_optional": true,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14712"></a>
## FND-14712: chesscom.explanation_engine.v1.MoveAnnotation.nags = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveAnnotation",
  "name": "nags",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14713"></a>
## FND-14713: chesscom.explanation_engine.v1.MoveAnnotation.arrows = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveAnnotation",
  "name": "arrows",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.AnnotationArrow",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14714"></a>
## FND-14714: chesscom.explanation_engine.v1.MoveAnnotation.highlighted_squares = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveAnnotation",
  "name": "highlighted_squares",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.AnnotationSquare",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14715"></a>
## FND-14715: chesscom.explanation_engine.v1.AnnotationColor.ANNOTATION_COLOR_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnnotationColor",
  "name": "ANNOTATION_COLOR_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14716"></a>
## FND-14716: chesscom.explanation_engine.v1.AnnotationColor.ANNOTATION_COLOR_GREEN = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnnotationColor",
  "name": "ANNOTATION_COLOR_GREEN",
  "number": 1,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14717"></a>
## FND-14717: chesscom.explanation_engine.v1.AnnotationColor.ANNOTATION_COLOR_RED = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnnotationColor",
  "name": "ANNOTATION_COLOR_RED",
  "number": 2,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14718"></a>
## FND-14718: chesscom.explanation_engine.v1.AnnotationColor.ANNOTATION_COLOR_YELLOW = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnnotationColor",
  "name": "ANNOTATION_COLOR_YELLOW",
  "number": 3,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14719"></a>
## FND-14719: chesscom.explanation_engine.v1.AnnotationColor.ANNOTATION_COLOR_BLUE = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.AnnotationColor",
  "name": "ANNOTATION_COLOR_BLUE",
  "number": 4,
  "source_id": "SRC-1019",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1019** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_annotation.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fee8b1bccbfb146364f4e481153c90cf0c04ed41224dcddc8ec6f131a7d835a.bin)

**Source references:** SRC-1019, SRC-1754  
**URL references:** None independently associated  
**Related findings:** FND-14702, FND-14703, FND-14704

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14720"></a>
## FND-14720: Native message: chesscom.explanation_engine.v1.EvalClassification

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "EvalClassification",
  "field": [
    {
      "name": "move_classification",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
    },
    {
      "name": "evaluation",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.engine.v1.Evaluation"
    }
  ]
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14721"></a>
## FND-14721: chesscom.explanation_engine.v1.EvalClassification.move_classification = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvalClassification",
  "name": "move_classification",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.MoveClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14722"></a>
## FND-14722: chesscom.explanation_engine.v1.EvalClassification.evaluation = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EvalClassification",
  "name": "evaluation",
  "number": 2,
  "type": ".chesscom.engine.v1.Evaluation",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14723"></a>
## FND-14723: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassification",
  "name": "MOVE_CLASSIFICATION_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14724"></a>
## FND-14724: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_BOOK = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassification",
  "name": "MOVE_CLASSIFICATION_BOOK",
  "number": 1,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14725"></a>
## FND-14725: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_BRILLIANT = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassification",
  "name": "MOVE_CLASSIFICATION_BRILLIANT",
  "number": 2,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14726"></a>
## FND-14726: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_GREAT_FIND = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassification",
  "name": "MOVE_CLASSIFICATION_GREAT_FIND",
  "number": 3,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14727"></a>
## FND-14727: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_BEST = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassification",
  "name": "MOVE_CLASSIFICATION_BEST",
  "number": 4,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14728"></a>
## FND-14728: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_EXCELLENT = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassification",
  "name": "MOVE_CLASSIFICATION_EXCELLENT",
  "number": 5,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14729"></a>
## FND-14729: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_GOOD = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassification",
  "name": "MOVE_CLASSIFICATION_GOOD",
  "number": 6,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14730"></a>
## FND-14730: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_INACCURACY = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassification",
  "name": "MOVE_CLASSIFICATION_INACCURACY",
  "number": 7,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14731"></a>
## FND-14731: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_MISTAKE = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassification",
  "name": "MOVE_CLASSIFICATION_MISTAKE",
  "number": 8,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14732"></a>
## FND-14732: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_BLUNDER = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassification",
  "name": "MOVE_CLASSIFICATION_BLUNDER",
  "number": 9,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14733"></a>
## FND-14733: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_MISSED = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassification",
  "name": "MOVE_CLASSIFICATION_MISSED",
  "number": 10,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14734"></a>
## FND-14734: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_FORCED = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassification",
  "name": "MOVE_CLASSIFICATION_FORCED",
  "number": 11,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14735"></a>
## FND-14735: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_TRICKY = 20

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassification",
  "name": "MOVE_CLASSIFICATION_TRICKY",
  "number": 20,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14736"></a>
## FND-14736: chesscom.explanation_engine.v1.MoveClassificationVersion.MOVE_CLASSIFICATION_VERSION_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassificationVersion",
  "name": "MOVE_CLASSIFICATION_VERSION_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14737"></a>
## FND-14737: chesscom.explanation_engine.v1.MoveClassificationVersion.MOVE_CLASSIFICATION_VERSION_V2 = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassificationVersion",
  "name": "MOVE_CLASSIFICATION_VERSION_V2",
  "number": 1,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14738"></a>
## FND-14738: chesscom.explanation_engine.v1.MoveClassificationVersion.MOVE_CLASSIFICATION_VERSION_V3 = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MoveClassificationVersion",
  "name": "MOVE_CLASSIFICATION_VERSION_V3",
  "number": 2,
  "source_id": "SRC-1020",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1020** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_classification.proto.bin` — [preserved redacted evidence](../evidence/descriptors/c9c383fd3bcd77b61b6159fbed39428850106e8851407f4ff0adac4af37f9f84.bin)

**Source references:** SRC-1020, SRC-1787  
**URL references:** None independently associated  
**Related findings:** FND-14720, FND-14721, FND-14722

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14739"></a>
## FND-14739: Native message: chesscom.explanation_engine.v1.PieceMove

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PieceMove",
  "field": [
    {
      "name": "from",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    },
    {
      "name": "to",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    },
    {
      "name": "piece",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Piece"
    }
  ]
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14740"></a>
## FND-14740: chesscom.explanation_engine.v1.PieceMove.from = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PieceMove",
  "name": "from",
  "number": 1,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14741"></a>
## FND-14741: chesscom.explanation_engine.v1.PieceMove.to = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PieceMove",
  "name": "to",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14742"></a>
## FND-14742: chesscom.explanation_engine.v1.PieceMove.piece = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PieceMove",
  "name": "piece",
  "number": 3,
  "type": ".chesscom.chess.v1.Piece",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14743"></a>
## FND-14743: Native message: chesscom.explanation_engine.v1.NormalMove

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "NormalMove",
  "field": [
    {
      "name": "moved_piece",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PieceMove"
    },
    {
      "name": "captured_piece",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Piece",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_captured_piece"
    }
  ]
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14744"></a>
## FND-14744: chesscom.explanation_engine.v1.NormalMove.moved_piece = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NormalMove",
  "name": "moved_piece",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PieceMove",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14745"></a>
## FND-14745: chesscom.explanation_engine.v1.NormalMove.captured_piece = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.NormalMove",
  "name": "captured_piece",
  "number": 2,
  "type": ".chesscom.chess.v1.Piece",
  "label": "LABEL_OPTIONAL",
  "oneof": "_captured_piece",
  "proto3_optional": true,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14746"></a>
## FND-14746: Native message: chesscom.explanation_engine.v1.CastlingMove

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CastlingMove",
  "field": [
    {
      "name": "king_move",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PieceMove"
    },
    {
      "name": "rook_move",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PieceMove"
    }
  ]
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14747"></a>
## FND-14747: chesscom.explanation_engine.v1.CastlingMove.king_move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CastlingMove",
  "name": "king_move",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PieceMove",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14748"></a>
## FND-14748: chesscom.explanation_engine.v1.CastlingMove.rook_move = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CastlingMove",
  "name": "rook_move",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.PieceMove",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14749"></a>
## FND-14749: Native message: chesscom.explanation_engine.v1.PromotionMove

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PromotionMove",
  "field": [
    {
      "name": "moved_piece",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PieceMove"
    },
    {
      "name": "captured_piece",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Piece",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "promoted_piece_type",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.PromotionPieceType"
    }
  ],
  "oneof_decl": [
    {
      "name": "_captured_piece"
    }
  ]
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14750"></a>
## FND-14750: chesscom.explanation_engine.v1.PromotionMove.moved_piece = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PromotionMove",
  "name": "moved_piece",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PieceMove",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14751"></a>
## FND-14751: chesscom.explanation_engine.v1.PromotionMove.captured_piece = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PromotionMove",
  "name": "captured_piece",
  "number": 2,
  "type": ".chesscom.chess.v1.Piece",
  "label": "LABEL_OPTIONAL",
  "oneof": "_captured_piece",
  "proto3_optional": true,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14752"></a>
## FND-14752: chesscom.explanation_engine.v1.PromotionMove.promoted_piece_type = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PromotionMove",
  "name": "promoted_piece_type",
  "number": 3,
  "type": ".chesscom.chess.v1.PromotionPieceType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14753"></a>
## FND-14753: Native message: chesscom.explanation_engine.v1.EnpassantMove

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "EnpassantMove",
  "field": [
    {
      "name": "moved_piece",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PieceMove"
    },
    {
      "name": "capture_square",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    }
  ]
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14754"></a>
## FND-14754: chesscom.explanation_engine.v1.EnpassantMove.moved_piece = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EnpassantMove",
  "name": "moved_piece",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PieceMove",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14755"></a>
## FND-14755: chesscom.explanation_engine.v1.EnpassantMove.capture_square = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.EnpassantMove",
  "name": "capture_square",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14756"></a>
## FND-14756: Native message: chesscom.explanation_engine.v1.NullMove

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "NullMove"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14757"></a>
## FND-14757: Native message: chesscom.explanation_engine.v1.MoveDetails

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "MoveDetails",
  "field": [
    {
      "name": "move_string",
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
    },
    {
      "name": "time_taken_ms",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "regular_move",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.NormalMove",
      "oneof_index": 0
    },
    {
      "name": "castling_move",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CastlingMove",
      "oneof_index": 0
    },
    {
      "name": "promotion_move",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PromotionMove",
      "oneof_index": 0
    },
    {
      "name": "en_passant_move",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.EnpassantMove",
      "oneof_index": 0
    },
    {
      "name": "null_move",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.NullMove",
      "oneof_index": 0
    },
    {
      "name": "moved_color",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Color"
    },
    {
      "name": "full_move_number",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "game_result",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.GameResult",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "kind"
    },
    {
      "name": "_game_result"
    }
  ]
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14758"></a>
## FND-14758: chesscom.explanation_engine.v1.MoveDetails.move_string = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveDetails",
  "name": "move_string",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14759"></a>
## FND-14759: chesscom.explanation_engine.v1.MoveDetails.move = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.MoveDetails",
  "name": "move",
  "number": 2,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1021",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1021** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_move_details.proto.bin` — [preserved redacted evidence](../evidence/descriptors/bf6d8c0f83c8bd001c9488d0fbe305360c47d8b1ce9e874c615c201d3e534a6f.bin)

**Source references:** SRC-1021, SRC-1777  
**URL references:** None independently associated  
**Related findings:** FND-14739, FND-14740, FND-14741

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
