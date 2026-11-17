# native_interfaces — findings 4401–4500

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-17060"></a>
## FND-17060: chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextAssetRequest.google_sheet_list = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextAssetRequest",
  "name": "google_sheet_list",
  "number": 1,
  "type": ".chesscom.text_item.v1alpha.GoogleSheetList",
  "label": "LABEL_OPTIONAL",
  "oneof": "input",
  "proto3_optional": false,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17061"></a>
## FND-17061: chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextAssetRequest.text_item_list = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextAssetRequest",
  "name": "text_item_list",
  "number": 2,
  "type": ".chesscom.text_item.v1alpha.TextItemList",
  "label": "LABEL_OPTIONAL",
  "oneof": "input",
  "proto3_optional": false,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17062"></a>
## FND-17062: Native message: chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextAssetResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGenerateCoachTextAssetResponse",
  "field": [
    {
      "name": "text_asset_json",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "sentences_for_audio_generation",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.text_item.v1alpha.AudioSentence"
    },
    {
      "name": "warnings",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17063"></a>
## FND-17063: chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextAssetResponse.text_asset_json = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextAssetResponse",
  "name": "text_asset_json",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17064"></a>
## FND-17064: chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextAssetResponse.sentences_for_audio_generation = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextAssetResponse",
  "name": "sentences_for_audio_generation",
  "number": 2,
  "type": ".chesscom.text_item.v1alpha.AudioSentence",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17065"></a>
## FND-17065: chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextAssetResponse.warnings = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextAssetResponse",
  "name": "warnings",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17066"></a>
## FND-17066: Native message: chesscom.text_item.v1alpha.AudioSentence

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AudioSentence",
  "field": [
    {
      "name": "presentation_sentence",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "source",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.text_item.v1alpha.AudioSentenceSource"
    }
  ]
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17067"></a>
## FND-17067: chesscom.text_item.v1alpha.AudioSentence.presentation_sentence = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.AudioSentence",
  "name": "presentation_sentence",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17068"></a>
## FND-17068: chesscom.text_item.v1alpha.AudioSentence.source = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.AudioSentence",
  "name": "source",
  "number": 2,
  "type": ".chesscom.text_item.v1alpha.AudioSentenceSource",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17069"></a>
## FND-17069: chesscom.text_item.v1alpha.AudioSentenceSource.AUDIO_SENTENCE_SOURCE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.AudioSentenceSource",
  "name": "AUDIO_SENTENCE_SOURCE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17070"></a>
## FND-17070: chesscom.text_item.v1alpha.AudioSentenceSource.AUDIO_SENTENCE_SOURCE_HIGH_PRIORITY = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.AudioSentenceSource",
  "name": "AUDIO_SENTENCE_SOURCE_HIGH_PRIORITY",
  "number": 1,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17071"></a>
## FND-17071: chesscom.text_item.v1alpha.AudioSentenceSource.AUDIO_SENTENCE_SOURCE_GAME_REVIEW = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.AudioSentenceSource",
  "name": "AUDIO_SENTENCE_SOURCE_GAME_REVIEW",
  "number": 2,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17072"></a>
## FND-17072: chesscom.text_item.v1alpha.AudioSentenceSource.AUDIO_SENTENCE_SOURCE_GAME_REVIEW_OPENINGS = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.AudioSentenceSource",
  "name": "AUDIO_SENTENCE_SOURCE_GAME_REVIEW_OPENINGS",
  "number": 3,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17073"></a>
## FND-17073: chesscom.text_item.v1alpha.AudioSentenceSource.AUDIO_SENTENCE_SOURCE_GAME_SUMMARY = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.AudioSentenceSource",
  "name": "AUDIO_SENTENCE_SOURCE_GAME_SUMMARY",
  "number": 4,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17074"></a>
## FND-17074: chesscom.text_item.v1alpha.AudioSentenceSource.AUDIO_SENTENCE_SOURCE_PLAY_VS_COACH_SCENARIOS = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.AudioSentenceSource",
  "name": "AUDIO_SENTENCE_SOURCE_PLAY_VS_COACH_SCENARIOS",
  "number": 5,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17075"></a>
## FND-17075: chesscom.text_item.v1alpha.AudioSentenceSource.AUDIO_SENTENCE_SOURCE_PLAY_VS_COACH_OPENINGS = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.AudioSentenceSource",
  "name": "AUDIO_SENTENCE_SOURCE_PLAY_VS_COACH_OPENINGS",
  "number": 6,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17076"></a>
## FND-17076: chesscom.text_item.v1alpha.AudioSentenceSource.AUDIO_SENTENCE_SOURCE_PUZZLES = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.AudioSentenceSource",
  "name": "AUDIO_SENTENCE_SOURCE_PUZZLES",
  "number": 7,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17077"></a>
## FND-17077: chesscom.text_item.v1alpha.AudioSentenceSource.AUDIO_SENTENCE_SOURCE_COURSE_RECOMMENDATIONS = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.AudioSentenceSource",
  "name": "AUDIO_SENTENCE_SOURCE_COURSE_RECOMMENDATIONS",
  "number": 8,
  "source_id": "SRC-1108",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1108** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_asset.proto.bin` — [preserved redacted evidence](../evidence/descriptors/38a06c2701ebd28255044b2aa4ff29966773a81a4dd0920c7082ff5904f765e9.bin)

**Source references:** SRC-1108, SRC-1757  
**URL references:** None independently associated  
**Related findings:** FND-17059, FND-17060, FND-17061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17078"></a>
## FND-17078: Native message: chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextItemsRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGenerateCoachTextItemsRequest",
  "field": [
    {
      "name": "google_sheet_list",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.text_item.v1alpha.GoogleSheetList"
    }
  ]
}

### Evidence

- **SRC-1109** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0e67c71744e2b393e80b3bbe28f235c0bffd19c99695aca5bb98c7ec3b9a3e43.bin)

**Source references:** SRC-1109, SRC-1783  
**URL references:** None independently associated  
**Related findings:** FND-17079, FND-17080

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17079"></a>
## FND-17079: chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextItemsRequest.google_sheet_list = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextItemsRequest",
  "name": "google_sheet_list",
  "number": 1,
  "type": ".chesscom.text_item.v1alpha.GoogleSheetList",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1109",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1109** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0e67c71744e2b393e80b3bbe28f235c0bffd19c99695aca5bb98c7ec3b9a3e43.bin)

**Source references:** SRC-1109, SRC-1783  
**URL references:** None independently associated  
**Related findings:** FND-17078, FND-17080

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17080"></a>
## FND-17080: Native message: chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextItemsResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "InternalFeatureGenerateCoachTextItemsResponse",
  "field": [
    {
      "name": "text_item_list",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.text_item.v1alpha.TextItemList"
    },
    {
      "name": "warnings",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1109** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0e67c71744e2b393e80b3bbe28f235c0bffd19c99695aca5bb98c7ec3b9a3e43.bin)

**Source references:** SRC-1109, SRC-1783  
**URL references:** None independently associated  
**Related findings:** FND-17078, FND-17079

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17081"></a>
## FND-17081: chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextItemsResponse.text_item_list = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextItemsResponse",
  "name": "text_item_list",
  "number": 1,
  "type": ".chesscom.text_item.v1alpha.TextItemList",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1109",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1109** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0e67c71744e2b393e80b3bbe28f235c0bffd19c99695aca5bb98c7ec3b9a3e43.bin)

**Source references:** SRC-1109, SRC-1783  
**URL references:** None independently associated  
**Related findings:** FND-17078, FND-17079, FND-17080

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17082"></a>
## FND-17082: chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextItemsResponse.warnings = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.InternalFeatureGenerateCoachTextItemsResponse",
  "name": "warnings",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1109",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1109** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_internal_feature_generate_coach_text_items.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0e67c71744e2b393e80b3bbe28f235c0bffd19c99695aca5bb98c7ec3b9a3e43.bin)

**Source references:** SRC-1109, SRC-1783  
**URL references:** None independently associated  
**Related findings:** FND-17078, FND-17079, FND-17080

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17083"></a>
## FND-17083: Native message: chesscom.text_item.v1alpha.PuzzleGoalTextContext

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PuzzleGoalTextContext",
  "field": [
    {
      "name": "puzzle_goal",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PuzzleGoal"
    },
    {
      "name": "key_board_event",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.BoardEvent",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_key_board_event"
    }
  ]
}

### Evidence

- **SRC-1110** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_puzzle_goal_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5fe28c4e7d07ef7ce9c7f18d9ab7585d90e4dee9388b660cf656b859b84d697a.bin)

**Source references:** SRC-1110, SRC-1721  
**URL references:** None independently associated  
**Related findings:** FND-17084, FND-17085

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17084"></a>
## FND-17084: chesscom.text_item.v1alpha.PuzzleGoalTextContext.puzzle_goal = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.PuzzleGoalTextContext",
  "name": "puzzle_goal",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PuzzleGoal",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1110",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1110** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_puzzle_goal_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5fe28c4e7d07ef7ce9c7f18d9ab7585d90e4dee9388b660cf656b859b84d697a.bin)

**Source references:** SRC-1110, SRC-1721  
**URL references:** None independently associated  
**Related findings:** FND-17083, FND-17085

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17085"></a>
## FND-17085: chesscom.text_item.v1alpha.PuzzleGoalTextContext.key_board_event = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.PuzzleGoalTextContext",
  "name": "key_board_event",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1alpha.BoardEvent",
  "label": "LABEL_OPTIONAL",
  "oneof": "_key_board_event",
  "proto3_optional": true,
  "source_id": "SRC-1110",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1110** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_puzzle_goal_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5fe28c4e7d07ef7ce9c7f18d9ab7585d90e4dee9388b660cf656b859b84d697a.bin)

**Source references:** SRC-1110, SRC-1721  
**URL references:** None independently associated  
**Related findings:** FND-17083, FND-17084

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17086"></a>
## FND-17086: Native message: chesscom.text_item.v1alpha.TakeawayTextContext

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "TakeawayTextContext",
  "field": [
    {
      "name": "stat",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.stats.v1.AdvancedStatType"
    },
    {
      "name": "trend",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.text_item.v1alpha.TakeawayTextContextTrend"
    },
    {
      "name": "skill",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.text_item.v1alpha.TakeawayTextContextQuality"
    },
    {
      "name": "performance",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.text_item.v1alpha.TakeawayTextContextQuality"
    }
  ]
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17087"></a>
## FND-17087: chesscom.text_item.v1alpha.TakeawayTextContext.stat = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TakeawayTextContext",
  "name": "stat",
  "number": 1,
  "type": ".chesscom.stats.v1.AdvancedStatType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17088"></a>
## FND-17088: chesscom.text_item.v1alpha.TakeawayTextContext.trend = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TakeawayTextContext",
  "name": "trend",
  "number": 2,
  "type": ".chesscom.text_item.v1alpha.TakeawayTextContextTrend",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17089"></a>
## FND-17089: chesscom.text_item.v1alpha.TakeawayTextContext.skill = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TakeawayTextContext",
  "name": "skill",
  "number": 3,
  "type": ".chesscom.text_item.v1alpha.TakeawayTextContextQuality",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17090"></a>
## FND-17090: chesscom.text_item.v1alpha.TakeawayTextContext.performance = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TakeawayTextContext",
  "name": "performance",
  "number": 4,
  "type": ".chesscom.text_item.v1alpha.TakeawayTextContextQuality",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17091"></a>
## FND-17091: Native message: chesscom.text_item.v1alpha.AdvancedStatCategoryTakeawayTextContext

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "AdvancedStatCategoryTakeawayTextContext",
  "field": [
    {
      "name": "stat",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.stats.v1.AdvancedStatType"
    },
    {
      "name": "trend",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.text_item.v1alpha.TakeawayTextContextTrend"
    },
    {
      "name": "skill",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.text_item.v1alpha.TakeawayTextContextQuality"
    }
  ]
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17092"></a>
## FND-17092: chesscom.text_item.v1alpha.AdvancedStatCategoryTakeawayTextContext.stat = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.AdvancedStatCategoryTakeawayTextContext",
  "name": "stat",
  "number": 1,
  "type": ".chesscom.stats.v1.AdvancedStatType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17093"></a>
## FND-17093: chesscom.text_item.v1alpha.AdvancedStatCategoryTakeawayTextContext.trend = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.AdvancedStatCategoryTakeawayTextContext",
  "name": "trend",
  "number": 2,
  "type": ".chesscom.text_item.v1alpha.TakeawayTextContextTrend",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17094"></a>
## FND-17094: chesscom.text_item.v1alpha.AdvancedStatCategoryTakeawayTextContext.skill = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.AdvancedStatCategoryTakeawayTextContext",
  "name": "skill",
  "number": 3,
  "type": ".chesscom.text_item.v1alpha.TakeawayTextContextQuality",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17095"></a>
## FND-17095: chesscom.text_item.v1alpha.TakeawayTextContextTrend.TAKEAWAY_TEXT_CONTEXT_TREND_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TakeawayTextContextTrend",
  "name": "TAKEAWAY_TEXT_CONTEXT_TREND_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17096"></a>
## FND-17096: chesscom.text_item.v1alpha.TakeawayTextContextTrend.TAKEAWAY_TEXT_CONTEXT_TREND_ANY = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TakeawayTextContextTrend",
  "name": "TAKEAWAY_TEXT_CONTEXT_TREND_ANY",
  "number": 1,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17097"></a>
## FND-17097: chesscom.text_item.v1alpha.TakeawayTextContextTrend.TAKEAWAY_TEXT_CONTEXT_TREND_UP = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TakeawayTextContextTrend",
  "name": "TAKEAWAY_TEXT_CONTEXT_TREND_UP",
  "number": 2,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17098"></a>
## FND-17098: chesscom.text_item.v1alpha.TakeawayTextContextTrend.TAKEAWAY_TEXT_CONTEXT_TREND_DOWN = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TakeawayTextContextTrend",
  "name": "TAKEAWAY_TEXT_CONTEXT_TREND_DOWN",
  "number": 3,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17099"></a>
## FND-17099: chesscom.text_item.v1alpha.TakeawayTextContextQuality.TAKEAWAY_TEXT_CONTEXT_QUALITY_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TakeawayTextContextQuality",
  "name": "TAKEAWAY_TEXT_CONTEXT_QUALITY_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17100"></a>
## FND-17100: chesscom.text_item.v1alpha.TakeawayTextContextQuality.TAKEAWAY_TEXT_CONTEXT_QUALITY_ANY = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TakeawayTextContextQuality",
  "name": "TAKEAWAY_TEXT_CONTEXT_QUALITY_ANY",
  "number": 1,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17101"></a>
## FND-17101: chesscom.text_item.v1alpha.TakeawayTextContextQuality.TAKEAWAY_TEXT_CONTEXT_QUALITY_BAD = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TakeawayTextContextQuality",
  "name": "TAKEAWAY_TEXT_CONTEXT_QUALITY_BAD",
  "number": 2,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17102"></a>
## FND-17102: chesscom.text_item.v1alpha.TakeawayTextContextQuality.TAKEAWAY_TEXT_CONTEXT_QUALITY_GOOD = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TakeawayTextContextQuality",
  "name": "TAKEAWAY_TEXT_CONTEXT_QUALITY_GOOD",
  "number": 3,
  "source_id": "SRC-1111",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1111** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_takeaway_text_context.proto.bin` — [preserved redacted evidence](../evidence/descriptors/365606db712c5bf36df73f3530561a55c85680b46d788740413698e42d5cbd5a.bin)

**Source references:** SRC-1111, SRC-1723  
**URL references:** None independently associated  
**Related findings:** FND-17086, FND-17087, FND-17088

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17103"></a>
## FND-17103: Native message: chesscom.text_item.v1alpha.TextContext

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "TextContext",
  "field": [
    {
      "name": "board_event",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.BoardEvent",
      "oneof_index": 0
    },
    {
      "name": "move_classification",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassification",
      "oneof_index": 0
    },
    {
      "name": "non_chess_text_type",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.NonChessTextType",
      "oneof_index": 0
    },
    {
      "name": "book_move",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.BookMove",
      "oneof_index": 0
    },
    {
      "name": "speech_trigger_label",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.SpeechTriggerLabel",
      "oneof_index": 0
    },
    {
      "name": "post_hint_type",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.PostHintType",
      "oneof_index": 0
    },
    {
      "name": "coach_choice_type",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.CoachChoiceType",
      "oneof_index": 0
    },
    {
      "name": "report_card_highlight",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.ReportCardHighlight",
      "oneof_index": 0
    },
    {
      "name": "elo_comparison",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.EloComparison",
      "oneof_index": 0
    },
    {
      "name": "puzzle_goal",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.text_item.v1alpha.PuzzleGoalTextContext",
      "oneof_index": 0
    },
    {
      "name": "color",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Color",
      "oneof_index": 0
    },
    {
      "name": "game_status",
      "number": 12,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.GameStatus",
      "oneof_index": 0
    },
    {
      "name": "variation_theme_prompt",
      "number": 13,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0
    },
    {
      "name": "game_summary",
      "number": 14,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1alpha.GameSummary",
      "oneof_index": 0
    },
    {
      "name": "gr_takeaway",
      "number": 15,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.text_item.v1alpha.TakeawayTextContext",
      "oneof_index": 0
    },
    {
      "name": "adv_stat_category_takeaway",
      "number": 16,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.text_item.v1alpha.AdvancedStatCategoryTakeawayTextContext",
      "oneof_index": 0
    },
    {
      "name": "coach_exercise_type",
      "number": 17,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1alpha.CoachExerciseType",
      "oneof_index": 0
    },
    {
      "name": "illegal_move_case",
      "number": 18,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.IllegalMoveCase",
      "oneof_index": 0
    },
    {
      "name": "train_goal",
      "number": 19,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.text_item.v1alpha.TrainGoalTextContext",
      "oneof_index": 0
    },
    {
      "name": "train_reply",
      "number": 20,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.text_item.v1alpha.TrainReplyTextContext",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "context"
    }
  ]
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17104"></a>
## FND-17104: chesscom.text_item.v1alpha.TextContext.board_event = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "board_event",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1alpha.BoardEvent",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17105"></a>
## FND-17105: chesscom.text_item.v1alpha.TextContext.move_classification = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "move_classification",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.MoveClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17106"></a>
## FND-17106: chesscom.text_item.v1alpha.TextContext.non_chess_text_type = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "non_chess_text_type",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.NonChessTextType",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17107"></a>
## FND-17107: chesscom.text_item.v1alpha.TextContext.book_move = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "book_move",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1alpha.BookMove",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17108"></a>
## FND-17108: chesscom.text_item.v1alpha.TextContext.speech_trigger_label = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "speech_trigger_label",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1alpha.SpeechTriggerLabel",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17109"></a>
## FND-17109: chesscom.text_item.v1alpha.TextContext.post_hint_type = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "post_hint_type",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1alpha.PostHintType",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17110"></a>
## FND-17110: chesscom.text_item.v1alpha.TextContext.coach_choice_type = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "coach_choice_type",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1alpha.CoachChoiceType",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17111"></a>
## FND-17111: chesscom.text_item.v1alpha.TextContext.report_card_highlight = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "report_card_highlight",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1alpha.ReportCardHighlight",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17112"></a>
## FND-17112: chesscom.text_item.v1alpha.TextContext.elo_comparison = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "elo_comparison",
  "number": 9,
  "type": ".chesscom.explanation_engine.v1alpha.EloComparison",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17113"></a>
## FND-17113: chesscom.text_item.v1alpha.TextContext.puzzle_goal = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "puzzle_goal",
  "number": 10,
  "type": ".chesscom.text_item.v1alpha.PuzzleGoalTextContext",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17114"></a>
## FND-17114: chesscom.text_item.v1alpha.TextContext.color = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "color",
  "number": 11,
  "type": ".chesscom.chess.v1.Color",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17115"></a>
## FND-17115: chesscom.text_item.v1alpha.TextContext.game_status = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "game_status",
  "number": 12,
  "type": ".chesscom.explanation_engine.v1alpha.GameStatus",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17116"></a>
## FND-17116: chesscom.text_item.v1alpha.TextContext.variation_theme_prompt = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "variation_theme_prompt",
  "number": 13,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17117"></a>
## FND-17117: chesscom.text_item.v1alpha.TextContext.game_summary = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "game_summary",
  "number": 14,
  "type": ".chesscom.explanation_engine.v1alpha.GameSummary",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17118"></a>
## FND-17118: chesscom.text_item.v1alpha.TextContext.gr_takeaway = 15

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "gr_takeaway",
  "number": 15,
  "type": ".chesscom.text_item.v1alpha.TakeawayTextContext",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17119"></a>
## FND-17119: chesscom.text_item.v1alpha.TextContext.adv_stat_category_takeaway = 16

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "adv_stat_category_takeaway",
  "number": 16,
  "type": ".chesscom.text_item.v1alpha.AdvancedStatCategoryTakeawayTextContext",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17120"></a>
## FND-17120: chesscom.text_item.v1alpha.TextContext.coach_exercise_type = 17

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "coach_exercise_type",
  "number": 17,
  "type": ".chesscom.explanation_engine.v1alpha.CoachExerciseType",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17121"></a>
## FND-17121: chesscom.text_item.v1alpha.TextContext.illegal_move_case = 18

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "illegal_move_case",
  "number": 18,
  "type": ".chesscom.explanation_engine.v1.IllegalMoveCase",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17122"></a>
## FND-17122: chesscom.text_item.v1alpha.TextContext.train_goal = 19

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "train_goal",
  "number": 19,
  "type": ".chesscom.text_item.v1alpha.TrainGoalTextContext",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17123"></a>
## FND-17123: chesscom.text_item.v1alpha.TextContext.train_reply = 20

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextContext",
  "name": "train_reply",
  "number": 20,
  "type": ".chesscom.text_item.v1alpha.TrainReplyTextContext",
  "label": "LABEL_OPTIONAL",
  "oneof": "context",
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17124"></a>
## FND-17124: Native message: chesscom.text_item.v1alpha.TextRatingRange

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "TextRatingRange",
  "field": [
    {
      "name": "min",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "max",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_min"
    },
    {
      "name": "_max"
    }
  ]
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17125"></a>
## FND-17125: chesscom.text_item.v1alpha.TextRatingRange.min = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextRatingRange",
  "name": "min",
  "number": 1,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_min",
  "proto3_optional": true,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17126"></a>
## FND-17126: chesscom.text_item.v1alpha.TextRatingRange.max = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextRatingRange",
  "name": "max",
  "number": 2,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_max",
  "proto3_optional": true,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17127"></a>
## FND-17127: Native message: chesscom.text_item.v1alpha.TextItem

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "TextItem",
  "field": [
    {
      "name": "text_item_id",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "context",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.text_item.v1alpha.TextContext"
    },
    {
      "name": "text_style",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.text_item.v1alpha.TextStyle"
    },
    {
      "name": "piece_specificity",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.text_item.v1alpha.PieceSpecificity"
    },
    {
      "name": "text_product",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.text_item.v1alpha.TextProduct"
    },
    {
      "name": "text_type",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.text_item.v1alpha.TextType"
    },
    {
      "name": "content",
      "number": 7,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    },
    {
      "name": "coach_text_id",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "eligible_pieces",
      "number": 9,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.PieceType"
    },
    {
      "name": "rating_range",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.text_item.v1alpha.TextRatingRange"
    },
    {
      "name": "tier",
      "number": 11,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "ply_limit",
      "number": 12,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "metadata",
      "number": 13,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.text_item.v1alpha.TextItem.MetadataEntry"
    },
    {
      "name": "expanded_piece",
      "number": 14,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.PieceType",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "audio_url_hashes",
      "number": 15,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    }
  ],
  "nested_type": [
    {
      "name": "MetadataEntry",
      "field": [
        {
          "name": "key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "value",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {
        "map_entry": true
      }
    }
  ],
  "oneof_decl": [
    {
      "name": "_tier"
    },
    {
      "name": "_ply_limit"
    },
    {
      "name": "_expanded_piece"
    }
  ]
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17128"></a>
## FND-17128: chesscom.text_item.v1alpha.TextItem.text_item_id = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "text_item_id",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17129"></a>
## FND-17129: chesscom.text_item.v1alpha.TextItem.context = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "context",
  "number": 2,
  "type": ".chesscom.text_item.v1alpha.TextContext",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17130"></a>
## FND-17130: chesscom.text_item.v1alpha.TextItem.text_style = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "text_style",
  "number": 3,
  "type": ".chesscom.text_item.v1alpha.TextStyle",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17131"></a>
## FND-17131: chesscom.text_item.v1alpha.TextItem.piece_specificity = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "piece_specificity",
  "number": 4,
  "type": ".chesscom.text_item.v1alpha.PieceSpecificity",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17132"></a>
## FND-17132: chesscom.text_item.v1alpha.TextItem.text_product = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "text_product",
  "number": 5,
  "type": ".chesscom.text_item.v1alpha.TextProduct",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17133"></a>
## FND-17133: chesscom.text_item.v1alpha.TextItem.text_type = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "text_type",
  "number": 6,
  "type": ".chesscom.text_item.v1alpha.TextType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17134"></a>
## FND-17134: chesscom.text_item.v1alpha.TextItem.content = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "content",
  "number": 7,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17135"></a>
## FND-17135: chesscom.text_item.v1alpha.TextItem.coach_text_id = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "coach_text_id",
  "number": 8,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17136"></a>
## FND-17136: chesscom.text_item.v1alpha.TextItem.eligible_pieces = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "eligible_pieces",
  "number": 9,
  "type": ".chesscom.chess.v1.PieceType",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17137"></a>
## FND-17137: chesscom.text_item.v1alpha.TextItem.rating_range = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "rating_range",
  "number": 10,
  "type": ".chesscom.text_item.v1alpha.TextRatingRange",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17138"></a>
## FND-17138: chesscom.text_item.v1alpha.TextItem.tier = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "tier",
  "number": 11,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_tier",
  "proto3_optional": true,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17139"></a>
## FND-17139: chesscom.text_item.v1alpha.TextItem.ply_limit = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "ply_limit",
  "number": 12,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_ply_limit",
  "proto3_optional": true,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17140"></a>
## FND-17140: chesscom.text_item.v1alpha.TextItem.metadata = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "metadata",
  "number": 13,
  "type": ".chesscom.text_item.v1alpha.TextItem.MetadataEntry",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17141"></a>
## FND-17141: chesscom.text_item.v1alpha.TextItem.expanded_piece = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "expanded_piece",
  "number": 14,
  "type": ".chesscom.chess.v1.PieceType",
  "label": "LABEL_OPTIONAL",
  "oneof": "_expanded_piece",
  "proto3_optional": true,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17142"></a>
## FND-17142: chesscom.text_item.v1alpha.TextItem.audio_url_hashes = 15

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem",
  "name": "audio_url_hashes",
  "number": 15,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17143"></a>
## FND-17143: Native message: chesscom.text_item.v1alpha.TextItem.MetadataEntry

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "MetadataEntry",
  "field": [
    {
      "name": "key",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "value",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ],
  "options": {
    "map_entry": true
  }
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17144"></a>
## FND-17144: chesscom.text_item.v1alpha.TextItem.MetadataEntry.key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem.MetadataEntry",
  "name": "key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17145"></a>
## FND-17145: chesscom.text_item.v1alpha.TextItem.MetadataEntry.value = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItem.MetadataEntry",
  "name": "value",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17146"></a>
## FND-17146: Native message: chesscom.text_item.v1alpha.TextItemList

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "TextItemList",
  "field": [
    {
      "name": "text_items",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.text_item.v1alpha.TextItem"
    }
  ]
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17147"></a>
## FND-17147: chesscom.text_item.v1alpha.TextItemList.text_items = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.text_item.v1alpha.TextItemList",
  "name": "text_items",
  "number": 1,
  "type": ".chesscom.text_item.v1alpha.TextItem",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17148"></a>
## FND-17148: chesscom.text_item.v1alpha.TextStyle.TEXT_STYLE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TextStyle",
  "name": "TEXT_STYLE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17149"></a>
## FND-17149: chesscom.text_item.v1alpha.TextStyle.TEXT_STYLE_PERSONAL = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TextStyle",
  "name": "TEXT_STYLE_PERSONAL",
  "number": 1,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17150"></a>
## FND-17150: chesscom.text_item.v1alpha.TextStyle.TEXT_STYLE_OPPOSING_PERSONAL = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TextStyle",
  "name": "TEXT_STYLE_OPPOSING_PERSONAL",
  "number": 2,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17151"></a>
## FND-17151: chesscom.text_item.v1alpha.TextStyle.TEXT_STYLE_OPPOSING_COACH = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TextStyle",
  "name": "TEXT_STYLE_OPPOSING_COACH",
  "number": 3,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17152"></a>
## FND-17152: chesscom.text_item.v1alpha.TextStyle.TEXT_STYLE_IMPERSONAL = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TextStyle",
  "name": "TEXT_STYLE_IMPERSONAL",
  "number": 4,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17153"></a>
## FND-17153: chesscom.text_item.v1alpha.TextStyle.TEXT_STYLE_NO_PERSONALITY = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TextStyle",
  "name": "TEXT_STYLE_NO_PERSONALITY",
  "number": 5,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17154"></a>
## FND-17154: chesscom.text_item.v1alpha.TextStyle.TEXT_STYLE_PLAY_COACH = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TextStyle",
  "name": "TEXT_STYLE_PLAY_COACH",
  "number": 6,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17155"></a>
## FND-17155: chesscom.text_item.v1alpha.TextStyle.TEXT_STYLE_SELF = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TextStyle",
  "name": "TEXT_STYLE_SELF",
  "number": 7,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17156"></a>
## FND-17156: chesscom.text_item.v1alpha.TextStyle.TEXT_STYLE_HINT = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TextStyle",
  "name": "TEXT_STYLE_HINT",
  "number": 8,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17157"></a>
## FND-17157: chesscom.text_item.v1alpha.TextStyle.TEXT_STYLE_BOT = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TextStyle",
  "name": "TEXT_STYLE_BOT",
  "number": 9,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17158"></a>
## FND-17158: chesscom.text_item.v1alpha.TextStyle.TEXT_STYLE_PLAYER = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TextStyle",
  "name": "TEXT_STYLE_PLAYER",
  "number": 10,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-17159"></a>
## FND-17159: chesscom.text_item.v1alpha.TextStyle.TEXT_STYLE_VARIATION_THEME_PROMPT = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.text_item.v1alpha.TextStyle",
  "name": "TEXT_STYLE_VARIATION_THEME_PROMPT",
  "number": 11,
  "source_id": "SRC-1112",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1112** `research/refinement/wasm-descriptors/chesscom_text_item_v1alpha_text_item.proto.bin` — [preserved redacted evidence](../evidence/descriptors/4da5d719171bc481d4454ac43154c6ebc330424bad7968972545c656da9de554.bin)

**Source references:** SRC-1112, SRC-1871  
**URL references:** None independently associated  
**Related findings:** FND-17103, FND-17104, FND-17105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
