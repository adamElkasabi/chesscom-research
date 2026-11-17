# native_interfaces — findings 1001–1100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-13660"></a>
## FND-13660: Native message: chesscom.explanation_engine.v1.GenerateTrainItemGoalSpeechRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GenerateTrainItemGoalSpeechRequest",
  "field": [
    {
      "name": "challenge",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.train.v1.TrainChallenge"
    }
  ]
}

### Evidence

- **SRC-0936** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_generate_train_item_goal_speech.proto.bin` — [preserved redacted evidence](../evidence/descriptors/79ee79d5b4a84e6352a7fb188db144e9aa1ffde00241f2f89dea9e5437a9544d.bin)

**Source references:** SRC-0936, SRC-1862  
**URL references:** None independently associated  
**Related findings:** FND-13661, FND-13662

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13661"></a>
## FND-13661: chesscom.explanation_engine.v1.GenerateTrainItemGoalSpeechRequest.challenge = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GenerateTrainItemGoalSpeechRequest",
  "name": "challenge",
  "number": 1,
  "type": ".chesscom.train.v1.TrainChallenge",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0936",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0936** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_generate_train_item_goal_speech.proto.bin` — [preserved redacted evidence](../evidence/descriptors/79ee79d5b4a84e6352a7fb188db144e9aa1ffde00241f2f89dea9e5437a9544d.bin)

**Source references:** SRC-0936, SRC-1862  
**URL references:** None independently associated  
**Related findings:** FND-13660, FND-13662

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13662"></a>
## FND-13662: Native message: chesscom.explanation_engine.v1.GenerateTrainItemGoalSpeechResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GenerateTrainItemGoalSpeechResponse",
  "field": [
    {
      "name": "goal_speech",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    }
  ]
}

### Evidence

- **SRC-0936** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_generate_train_item_goal_speech.proto.bin` — [preserved redacted evidence](../evidence/descriptors/79ee79d5b4a84e6352a7fb188db144e9aa1ffde00241f2f89dea9e5437a9544d.bin)

**Source references:** SRC-0936, SRC-1862  
**URL references:** None independently associated  
**Related findings:** FND-13660, FND-13661

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13663"></a>
## FND-13663: chesscom.explanation_engine.v1.GenerateTrainItemGoalSpeechResponse.goal_speech = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GenerateTrainItemGoalSpeechResponse",
  "name": "goal_speech",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0936",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0936** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_generate_train_item_goal_speech.proto.bin` — [preserved redacted evidence](../evidence/descriptors/79ee79d5b4a84e6352a7fb188db144e9aa1ffde00241f2f89dea9e5437a9544d.bin)

**Source references:** SRC-0936, SRC-1862  
**URL references:** None independently associated  
**Related findings:** FND-13660, FND-13661, FND-13662

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13664"></a>
## FND-13664: Native message: chesscom.explanation_engine.v1.GenerateUuidV1Request

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GenerateUuidV1Request"
}

### Evidence

- **SRC-0937** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_generate_uuid_v1.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9f56cdcd3f83a2597fce34a02c5b039e2f50224cd7c8bb29a0972fe120cf187c.bin)

**Source references:** SRC-0937, SRC-1834  
**URL references:** None independently associated  
**Related findings:** FND-13665, FND-13666

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13665"></a>
## FND-13665: Native message: chesscom.explanation_engine.v1.GenerateUuidV1Response

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GenerateUuidV1Response",
  "field": [
    {
      "name": "uuid",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0937** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_generate_uuid_v1.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9f56cdcd3f83a2597fce34a02c5b039e2f50224cd7c8bb29a0972fe120cf187c.bin)

**Source references:** SRC-0937, SRC-1834  
**URL references:** None independently associated  
**Related findings:** FND-13664, FND-13666

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13666"></a>
## FND-13666: chesscom.explanation_engine.v1.GenerateUuidV1Response.uuid = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GenerateUuidV1Response",
  "name": "uuid",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0937",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0937** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_generate_uuid_v1.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9f56cdcd3f83a2597fce34a02c5b039e2f50224cd7c8bb29a0972fe120cf187c.bin)

**Source references:** SRC-0937, SRC-1834  
**URL references:** None independently associated  
**Related findings:** FND-13664, FND-13665

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13667"></a>
## FND-13667: Native message: chesscom.explanation_engine.v1.GetBotChatRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetBotChatRequest",
  "field": [
    {
      "name": "bot_name",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "move_notation",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.MoveNotation",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "request_hint",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "json",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "options": {
        "deprecated": true
      },
      "oneof_index": 2,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_move_notation"
    },
    {
      "name": "_request_hint"
    },
    {
      "name": "_json"
    }
  ]
}

### Evidence

- **SRC-0938** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5a1148934a40da0323986ac532dac54986a4641da207425562d9f48853668310.bin)

**Source references:** SRC-0938, SRC-1714  
**URL references:** None independently associated  
**Related findings:** FND-13668, FND-13669

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13668"></a>
## FND-13668: chesscom.explanation_engine.v1.GetBotChatRequest.bot_name = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetBotChatRequest",
  "name": "bot_name",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0938",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0938** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5a1148934a40da0323986ac532dac54986a4641da207425562d9f48853668310.bin)

**Source references:** SRC-0938, SRC-1714  
**URL references:** None independently associated  
**Related findings:** FND-13667, FND-13669

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13669"></a>
## FND-13669: chesscom.explanation_engine.v1.GetBotChatRequest.move_notation = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetBotChatRequest",
  "name": "move_notation",
  "number": 2,
  "type": ".chesscom.chess.v1.MoveNotation",
  "label": "LABEL_OPTIONAL",
  "oneof": "_move_notation",
  "proto3_optional": true,
  "source_id": "SRC-0938",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0938** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5a1148934a40da0323986ac532dac54986a4641da207425562d9f48853668310.bin)

**Source references:** SRC-0938, SRC-1714  
**URL references:** None independently associated  
**Related findings:** FND-13667, FND-13668

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13670"></a>
## FND-13670: chesscom.explanation_engine.v1.GetBotChatRequest.request_hint = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetBotChatRequest",
  "name": "request_hint",
  "number": 3,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_request_hint",
  "proto3_optional": true,
  "source_id": "SRC-0938",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0938** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5a1148934a40da0323986ac532dac54986a4641da207425562d9f48853668310.bin)

**Source references:** SRC-0938, SRC-1714  
**URL references:** None independently associated  
**Related findings:** FND-13667, FND-13668, FND-13669

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13671"></a>
## FND-13671: chesscom.explanation_engine.v1.GetBotChatRequest.json = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetBotChatRequest",
  "name": "json",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_json",
  "proto3_optional": true,
  "source_id": "SRC-0938",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0938** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5a1148934a40da0323986ac532dac54986a4641da207425562d9f48853668310.bin)

**Source references:** SRC-0938, SRC-1714  
**URL references:** None independently associated  
**Related findings:** FND-13667, FND-13668, FND-13669

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13672"></a>
## FND-13672: Native message: chesscom.explanation_engine.v1.GetBotChatResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetBotChatResponse",
  "field": [
    {
      "name": "speech",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    },
    {
      "name": "hinted_move",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.MoveDetails",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "json",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "options": {
        "deprecated": true
      },
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "trigger_info",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.BotChatTriggerInfo",
      "oneof_index": 2,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_hinted_move"
    },
    {
      "name": "_json"
    },
    {
      "name": "_trigger_info"
    }
  ]
}

### Evidence

- **SRC-0938** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5a1148934a40da0323986ac532dac54986a4641da207425562d9f48853668310.bin)

**Source references:** SRC-0938, SRC-1714  
**URL references:** None independently associated  
**Related findings:** FND-13667, FND-13668, FND-13669

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13673"></a>
## FND-13673: chesscom.explanation_engine.v1.GetBotChatResponse.speech = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetBotChatResponse",
  "name": "speech",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0938",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0938** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5a1148934a40da0323986ac532dac54986a4641da207425562d9f48853668310.bin)

**Source references:** SRC-0938, SRC-1714  
**URL references:** None independently associated  
**Related findings:** FND-13667, FND-13668, FND-13669

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13674"></a>
## FND-13674: chesscom.explanation_engine.v1.GetBotChatResponse.hinted_move = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetBotChatResponse",
  "name": "hinted_move",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.MoveDetails",
  "label": "LABEL_OPTIONAL",
  "oneof": "_hinted_move",
  "proto3_optional": true,
  "source_id": "SRC-0938",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0938** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5a1148934a40da0323986ac532dac54986a4641da207425562d9f48853668310.bin)

**Source references:** SRC-0938, SRC-1714  
**URL references:** None independently associated  
**Related findings:** FND-13667, FND-13668, FND-13669

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13675"></a>
## FND-13675: chesscom.explanation_engine.v1.GetBotChatResponse.json = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetBotChatResponse",
  "name": "json",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_json",
  "proto3_optional": true,
  "source_id": "SRC-0938",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0938** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5a1148934a40da0323986ac532dac54986a4641da207425562d9f48853668310.bin)

**Source references:** SRC-0938, SRC-1714  
**URL references:** None independently associated  
**Related findings:** FND-13667, FND-13668, FND-13669

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13676"></a>
## FND-13676: chesscom.explanation_engine.v1.GetBotChatResponse.trigger_info = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetBotChatResponse",
  "name": "trigger_info",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.BotChatTriggerInfo",
  "label": "LABEL_OPTIONAL",
  "oneof": "_trigger_info",
  "proto3_optional": true,
  "source_id": "SRC-0938",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0938** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5a1148934a40da0323986ac532dac54986a4641da207425562d9f48853668310.bin)

**Source references:** SRC-0938, SRC-1714  
**URL references:** None independently associated  
**Related findings:** FND-13667, FND-13668, FND-13669

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13677"></a>
## FND-13677: Native message: chesscom.explanation_engine.v1.BotChatTriggerInfo

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "BotChatTriggerInfo",
  "field": [
    {
      "name": "label",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "alternative",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32"
    },
    {
      "name": "personality",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0938** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5a1148934a40da0323986ac532dac54986a4641da207425562d9f48853668310.bin)

**Source references:** SRC-0938, SRC-1714  
**URL references:** None independently associated  
**Related findings:** FND-13667, FND-13668, FND-13669

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13678"></a>
## FND-13678: chesscom.explanation_engine.v1.BotChatTriggerInfo.label = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotChatTriggerInfo",
  "name": "label",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0938",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0938** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5a1148934a40da0323986ac532dac54986a4641da207425562d9f48853668310.bin)

**Source references:** SRC-0938, SRC-1714  
**URL references:** None independently associated  
**Related findings:** FND-13667, FND-13668, FND-13669

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13679"></a>
## FND-13679: chesscom.explanation_engine.v1.BotChatTriggerInfo.alternative = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotChatTriggerInfo",
  "name": "alternative",
  "number": 2,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0938",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0938** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5a1148934a40da0323986ac532dac54986a4641da207425562d9f48853668310.bin)

**Source references:** SRC-0938, SRC-1714  
**URL references:** None independently associated  
**Related findings:** FND-13667, FND-13668, FND-13669

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13680"></a>
## FND-13680: chesscom.explanation_engine.v1.BotChatTriggerInfo.personality = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.BotChatTriggerInfo",
  "name": "personality",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0938",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0938** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5a1148934a40da0323986ac532dac54986a4641da207425562d9f48853668310.bin)

**Source references:** SRC-0938, SRC-1714  
**URL references:** None independently associated  
**Related findings:** FND-13667, FND-13668, FND-13669

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13681"></a>
## FND-13681: Native message: chesscom.explanation_engine.v1.GetBotMoveRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetBotMoveRequest",
  "field": [
    {
      "name": "options",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.BotOptions"
    },
    {
      "name": "engine",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.BotEngine"
    }
  ]
}

### Evidence

- **SRC-0939** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a62625acb1f1330e868e86585c79bbd81baea366bdae3721675b81171ed6292a.bin)

**Source references:** SRC-0939, SRC-1722  
**URL references:** None independently associated  
**Related findings:** FND-13682, FND-13683

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13682"></a>
## FND-13682: chesscom.explanation_engine.v1.GetBotMoveRequest.options = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetBotMoveRequest",
  "name": "options",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.BotOptions",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0939",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0939** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a62625acb1f1330e868e86585c79bbd81baea366bdae3721675b81171ed6292a.bin)

**Source references:** SRC-0939, SRC-1722  
**URL references:** None independently associated  
**Related findings:** FND-13681, FND-13683

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13683"></a>
## FND-13683: chesscom.explanation_engine.v1.GetBotMoveRequest.engine = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetBotMoveRequest",
  "name": "engine",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.BotEngine",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0939",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0939** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a62625acb1f1330e868e86585c79bbd81baea366bdae3721675b81171ed6292a.bin)

**Source references:** SRC-0939, SRC-1722  
**URL references:** None independently associated  
**Related findings:** FND-13681, FND-13682

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13684"></a>
## FND-13684: Native message: chesscom.explanation_engine.v1.GetBotMoveResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetBotMoveResponse",
  "field": [
    {
      "name": "move",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    }
  ]
}

### Evidence

- **SRC-0939** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a62625acb1f1330e868e86585c79bbd81baea366bdae3721675b81171ed6292a.bin)

**Source references:** SRC-0939, SRC-1722  
**URL references:** None independently associated  
**Related findings:** FND-13681, FND-13682, FND-13683

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13685"></a>
## FND-13685: chesscom.explanation_engine.v1.GetBotMoveResponse.move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetBotMoveResponse",
  "name": "move",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0939",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0939** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_bot_move.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a62625acb1f1330e868e86585c79bbd81baea366bdae3721675b81171ed6292a.bin)

**Source references:** SRC-0939, SRC-1722  
**URL references:** None independently associated  
**Related findings:** FND-13681, FND-13682, FND-13683

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13686"></a>
## FND-13686: Native message: chesscom.explanation_engine.v1.GetChess960InitialPositionRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetChess960InitialPositionRequest",
  "field": [
    {
      "name": "initial_position_index",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-0940** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_chess960_initial_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d267f8a426aed6c0cef0bde61955c9fbdf3248fb70910c446a72bf6a759bcc22.bin)

**Source references:** SRC-0940, SRC-1852  
**URL references:** None independently associated  
**Related findings:** FND-13687, FND-13688

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13687"></a>
## FND-13687: chesscom.explanation_engine.v1.GetChess960InitialPositionRequest.initial_position_index = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetChess960InitialPositionRequest",
  "name": "initial_position_index",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0940",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0940** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_chess960_initial_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d267f8a426aed6c0cef0bde61955c9fbdf3248fb70910c446a72bf6a759bcc22.bin)

**Source references:** SRC-0940, SRC-1852  
**URL references:** None independently associated  
**Related findings:** FND-13686, FND-13688

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13688"></a>
## FND-13688: Native message: chesscom.explanation_engine.v1.GetChess960InitialPositionResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetChess960InitialPositionResponse",
  "field": [
    {
      "name": "fen_position",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0940** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_chess960_initial_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d267f8a426aed6c0cef0bde61955c9fbdf3248fb70910c446a72bf6a759bcc22.bin)

**Source references:** SRC-0940, SRC-1852  
**URL references:** None independently associated  
**Related findings:** FND-13686, FND-13687

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13689"></a>
## FND-13689: chesscom.explanation_engine.v1.GetChess960InitialPositionResponse.fen_position = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetChess960InitialPositionResponse",
  "name": "fen_position",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0940",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0940** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_chess960_initial_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d267f8a426aed6c0cef0bde61955c9fbdf3248fb70910c446a72bf6a759bcc22.bin)

**Source references:** SRC-0940, SRC-1852  
**URL references:** None independently associated  
**Related findings:** FND-13686, FND-13687, FND-13688

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13690"></a>
## FND-13690: Native message: chesscom.explanation_engine.v1.GetCoachChatRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetCoachChatRequest"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13691"></a>
## FND-13691: Native message: chesscom.explanation_engine.v1.GetCoachChatResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetCoachChatResponse",
  "field": [
    {
      "name": "debug_info",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CoachChatDebugInfo",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "speech",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "retry_mistake",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.RetryMistake",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "flip_board_mistake",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.FlipBoardMistake",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "skills_earned",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SkillsPosition"
    },
    {
      "name": "coach_emotion",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.CoachEmotion",
      "oneof_index": 4,
      "proto3_optional": true
    },
    {
      "name": "retry_miss",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.RetryMiss",
      "oneof_index": 5,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_debug_info"
    },
    {
      "name": "_speech"
    },
    {
      "name": "_retry_mistake"
    },
    {
      "name": "_flip_board_mistake"
    },
    {
      "name": "_coach_emotion"
    },
    {
      "name": "_retry_miss"
    }
  ]
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13692"></a>
## FND-13692: chesscom.explanation_engine.v1.GetCoachChatResponse.debug_info = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetCoachChatResponse",
  "name": "debug_info",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.CoachChatDebugInfo",
  "label": "LABEL_OPTIONAL",
  "oneof": "_debug_info",
  "proto3_optional": true,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13693"></a>
## FND-13693: chesscom.explanation_engine.v1.GetCoachChatResponse.speech = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetCoachChatResponse",
  "name": "speech",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": "_speech",
  "proto3_optional": true,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13694"></a>
## FND-13694: chesscom.explanation_engine.v1.GetCoachChatResponse.retry_mistake = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetCoachChatResponse",
  "name": "retry_mistake",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.RetryMistake",
  "label": "LABEL_OPTIONAL",
  "oneof": "_retry_mistake",
  "proto3_optional": true,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13695"></a>
## FND-13695: chesscom.explanation_engine.v1.GetCoachChatResponse.flip_board_mistake = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetCoachChatResponse",
  "name": "flip_board_mistake",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.FlipBoardMistake",
  "label": "LABEL_OPTIONAL",
  "oneof": "_flip_board_mistake",
  "proto3_optional": true,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13696"></a>
## FND-13696: chesscom.explanation_engine.v1.GetCoachChatResponse.skills_earned = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetCoachChatResponse",
  "name": "skills_earned",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.SkillsPosition",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13697"></a>
## FND-13697: chesscom.explanation_engine.v1.GetCoachChatResponse.coach_emotion = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetCoachChatResponse",
  "name": "coach_emotion",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.CoachEmotion",
  "label": "LABEL_OPTIONAL",
  "oneof": "_coach_emotion",
  "proto3_optional": true,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13698"></a>
## FND-13698: chesscom.explanation_engine.v1.GetCoachChatResponse.retry_miss = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetCoachChatResponse",
  "name": "retry_miss",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.RetryMiss",
  "label": "LABEL_OPTIONAL",
  "oneof": "_retry_miss",
  "proto3_optional": true,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13699"></a>
## FND-13699: Native message: chesscom.explanation_engine.v1.RetryMistake

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RetryMistake",
  "field": [
    {
      "name": "speech",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    },
    {
      "name": "arrows_and_squares",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.ArrowsAndSquares"
    },
    {
      "name": "keep_playing_choice",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CoachChoice"
    },
    {
      "name": "retry_choice",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CoachChoice"
    },
    {
      "name": "ply_until_cooldown",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32"
    },
    {
      "name": "board_event",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13700"></a>
## FND-13700: chesscom.explanation_engine.v1.RetryMistake.speech = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMistake",
  "name": "speech",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13701"></a>
## FND-13701: chesscom.explanation_engine.v1.RetryMistake.arrows_and_squares = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMistake",
  "name": "arrows_and_squares",
  "number": 2,
  "type": ".chesscom.chess.v1.ArrowsAndSquares",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13702"></a>
## FND-13702: chesscom.explanation_engine.v1.RetryMistake.keep_playing_choice = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMistake",
  "name": "keep_playing_choice",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.CoachChoice",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13703"></a>
## FND-13703: chesscom.explanation_engine.v1.RetryMistake.retry_choice = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMistake",
  "name": "retry_choice",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.CoachChoice",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13704"></a>
## FND-13704: chesscom.explanation_engine.v1.RetryMistake.ply_until_cooldown = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMistake",
  "name": "ply_until_cooldown",
  "number": 5,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13705"></a>
## FND-13705: chesscom.explanation_engine.v1.RetryMistake.board_event = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMistake",
  "name": "board_event",
  "number": 6,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13706"></a>
## FND-13706: Native message: chesscom.explanation_engine.v1.FlipBoardMistake

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "FlipBoardMistake",
  "field": [
    {
      "name": "refutation_move",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    },
    {
      "name": "arrows_and_squares",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.ArrowsAndSquares"
    },
    {
      "name": "board_event",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "offer_speech",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    },
    {
      "name": "switch_sides_choice",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CoachChoice"
    },
    {
      "name": "decline_choice",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CoachChoice"
    },
    {
      "name": "success_speech",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    },
    {
      "name": "failure_speech",
      "number": 8,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    },
    {
      "name": "failure_almost_speech",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    },
    {
      "name": "continue_after_flip_choice",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CoachChoice"
    }
  ]
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13707"></a>
## FND-13707: chesscom.explanation_engine.v1.FlipBoardMistake.refutation_move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.FlipBoardMistake",
  "name": "refutation_move",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13708"></a>
## FND-13708: chesscom.explanation_engine.v1.FlipBoardMistake.arrows_and_squares = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.FlipBoardMistake",
  "name": "arrows_and_squares",
  "number": 2,
  "type": ".chesscom.chess.v1.ArrowsAndSquares",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13709"></a>
## FND-13709: chesscom.explanation_engine.v1.FlipBoardMistake.board_event = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.FlipBoardMistake",
  "name": "board_event",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13710"></a>
## FND-13710: chesscom.explanation_engine.v1.FlipBoardMistake.offer_speech = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.FlipBoardMistake",
  "name": "offer_speech",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13711"></a>
## FND-13711: chesscom.explanation_engine.v1.FlipBoardMistake.switch_sides_choice = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.FlipBoardMistake",
  "name": "switch_sides_choice",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.CoachChoice",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13712"></a>
## FND-13712: chesscom.explanation_engine.v1.FlipBoardMistake.decline_choice = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.FlipBoardMistake",
  "name": "decline_choice",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.CoachChoice",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13713"></a>
## FND-13713: chesscom.explanation_engine.v1.FlipBoardMistake.success_speech = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.FlipBoardMistake",
  "name": "success_speech",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13714"></a>
## FND-13714: chesscom.explanation_engine.v1.FlipBoardMistake.failure_speech = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.FlipBoardMistake",
  "name": "failure_speech",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13715"></a>
## FND-13715: chesscom.explanation_engine.v1.FlipBoardMistake.failure_almost_speech = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.FlipBoardMistake",
  "name": "failure_almost_speech",
  "number": 10,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13716"></a>
## FND-13716: chesscom.explanation_engine.v1.FlipBoardMistake.continue_after_flip_choice = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.FlipBoardMistake",
  "name": "continue_after_flip_choice",
  "number": 9,
  "type": ".chesscom.explanation_engine.v1.CoachChoice",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13717"></a>
## FND-13717: Native message: chesscom.explanation_engine.v1.RetryMiss

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RetryMiss",
  "field": [
    {
      "name": "speech",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    },
    {
      "name": "arrows_and_squares",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.ArrowsAndSquares"
    },
    {
      "name": "keep_playing_choice",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CoachChoice"
    },
    {
      "name": "retry_choice",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CoachChoice"
    },
    {
      "name": "board_event",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "attempt_speech",
      "number": 6,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    },
    {
      "name": "failure_speech",
      "number": 7,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    },
    {
      "name": "success_speech",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    },
    {
      "name": "success_moves",
      "number": 9,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    }
  ]
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13718"></a>
## FND-13718: chesscom.explanation_engine.v1.RetryMiss.speech = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMiss",
  "name": "speech",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13719"></a>
## FND-13719: chesscom.explanation_engine.v1.RetryMiss.arrows_and_squares = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMiss",
  "name": "arrows_and_squares",
  "number": 2,
  "type": ".chesscom.chess.v1.ArrowsAndSquares",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13720"></a>
## FND-13720: chesscom.explanation_engine.v1.RetryMiss.keep_playing_choice = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMiss",
  "name": "keep_playing_choice",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.CoachChoice",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13721"></a>
## FND-13721: chesscom.explanation_engine.v1.RetryMiss.retry_choice = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMiss",
  "name": "retry_choice",
  "number": 4,
  "type": ".chesscom.explanation_engine.v1.CoachChoice",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13722"></a>
## FND-13722: chesscom.explanation_engine.v1.RetryMiss.board_event = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMiss",
  "name": "board_event",
  "number": 5,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13723"></a>
## FND-13723: chesscom.explanation_engine.v1.RetryMiss.attempt_speech = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMiss",
  "name": "attempt_speech",
  "number": 6,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13724"></a>
## FND-13724: chesscom.explanation_engine.v1.RetryMiss.failure_speech = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMiss",
  "name": "failure_speech",
  "number": 7,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13725"></a>
## FND-13725: chesscom.explanation_engine.v1.RetryMiss.success_speech = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMiss",
  "name": "success_speech",
  "number": 8,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13726"></a>
## FND-13726: chesscom.explanation_engine.v1.RetryMiss.success_moves = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMiss",
  "name": "success_moves",
  "number": 9,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13727"></a>
## FND-13727: Native message: chesscom.explanation_engine.v1.CoachChoice

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CoachChoice",
  "field": [
    {
      "name": "button_text",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "response_speech",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech"
    },
    {
      "name": "response_move",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_response_move"
    }
  ]
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13728"></a>
## FND-13728: chesscom.explanation_engine.v1.CoachChoice.button_text = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoachChoice",
  "name": "button_text",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13729"></a>
## FND-13729: chesscom.explanation_engine.v1.CoachChoice.response_speech = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoachChoice",
  "name": "response_speech",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13730"></a>
## FND-13730: chesscom.explanation_engine.v1.CoachChoice.response_move = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoachChoice",
  "name": "response_move",
  "number": 3,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": "_response_move",
  "proto3_optional": true,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13731"></a>
## FND-13731: Native message: chesscom.explanation_engine.v1.CoachChatDebugInfo

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CoachChatDebugInfo",
  "field": [
    {
      "name": "speech_debug_info",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SpeechDebugInfo"
    },
    {
      "name": "retry_mistake_debug_info",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.RetryMistakeDebugInfo"
    },
    {
      "name": "used_botchat_triggers",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    },
    {
      "name": "used_board_events",
      "number": 4,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    },
    {
      "name": "flip_board_mistake_debug_info",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo"
    }
  ]
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13732"></a>
## FND-13732: chesscom.explanation_engine.v1.CoachChatDebugInfo.speech_debug_info = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoachChatDebugInfo",
  "name": "speech_debug_info",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.SpeechDebugInfo",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13733"></a>
## FND-13733: chesscom.explanation_engine.v1.CoachChatDebugInfo.retry_mistake_debug_info = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoachChatDebugInfo",
  "name": "retry_mistake_debug_info",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.RetryMistakeDebugInfo",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13734"></a>
## FND-13734: chesscom.explanation_engine.v1.CoachChatDebugInfo.used_botchat_triggers = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoachChatDebugInfo",
  "name": "used_botchat_triggers",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13735"></a>
## FND-13735: chesscom.explanation_engine.v1.CoachChatDebugInfo.used_board_events = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoachChatDebugInfo",
  "name": "used_board_events",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13736"></a>
## FND-13736: chesscom.explanation_engine.v1.CoachChatDebugInfo.flip_board_mistake_debug_info = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoachChatDebugInfo",
  "name": "flip_board_mistake_debug_info",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13737"></a>
## FND-13737: Native message: chesscom.explanation_engine.v1.RetryMistakeDebugInfo

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "RetryMistakeDebugInfo",
  "field": [
    {
      "name": "move_classification",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
    },
    {
      "name": "player_is_winning",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL"
    },
    {
      "name": "ply_until_cooldown",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13738"></a>
## FND-13738: chesscom.explanation_engine.v1.RetryMistakeDebugInfo.move_classification = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMistakeDebugInfo",
  "name": "move_classification",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.MoveClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13739"></a>
## FND-13739: chesscom.explanation_engine.v1.RetryMistakeDebugInfo.player_is_winning = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMistakeDebugInfo",
  "name": "player_is_winning",
  "number": 2,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13740"></a>
## FND-13740: chesscom.explanation_engine.v1.RetryMistakeDebugInfo.ply_until_cooldown = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.RetryMistakeDebugInfo",
  "name": "ply_until_cooldown",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13741"></a>
## FND-13741: Native message: chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "FlipBoardMistakeDebugInfo",
  "field": [
    {
      "name": "move_classification",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
    },
    {
      "name": "ply_until_flip_board_cooldown",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13742"></a>
## FND-13742: chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo.move_classification = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo",
  "name": "move_classification",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.MoveClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13743"></a>
## FND-13743: chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo.ply_until_flip_board_cooldown = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo",
  "name": "ply_until_flip_board_cooldown",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0942",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0942** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_chat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a90ea666208c3f20056aec5a57fa773077b75329e7146932ff93b641a550fd3a.bin)

**Source references:** SRC-0942, SRC-1824  
**URL references:** None independently associated  
**Related findings:** FND-13690, FND-13691, FND-13692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13744"></a>
## FND-13744: Native message: chesscom.explanation_engine.v1.GetCoachHintRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetCoachHintRequest"
}

### Evidence

- **SRC-0943** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_hint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/aedd97b81c3e13431a50459da31a393e19ea768372afdff18e8ef32df1c4e21e.bin)

**Source references:** SRC-0943, SRC-1807  
**URL references:** None independently associated  
**Related findings:** FND-13745, FND-13746

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13745"></a>
## FND-13745: Native message: chesscom.explanation_engine.v1.GetCoachHintResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetCoachHintResponse",
  "field": [
    {
      "name": "hint",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CoachHint",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_hint"
    }
  ]
}

### Evidence

- **SRC-0943** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_hint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/aedd97b81c3e13431a50459da31a393e19ea768372afdff18e8ef32df1c4e21e.bin)

**Source references:** SRC-0943, SRC-1807  
**URL references:** None independently associated  
**Related findings:** FND-13744, FND-13746

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13746"></a>
## FND-13746: chesscom.explanation_engine.v1.GetCoachHintResponse.hint = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetCoachHintResponse",
  "name": "hint",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.CoachHint",
  "label": "LABEL_OPTIONAL",
  "oneof": "_hint",
  "proto3_optional": true,
  "source_id": "SRC-0943",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0943** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_hint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/aedd97b81c3e13431a50459da31a393e19ea768372afdff18e8ef32df1c4e21e.bin)

**Source references:** SRC-0943, SRC-1807  
**URL references:** None independently associated  
**Related findings:** FND-13744, FND-13745

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13747"></a>
## FND-13747: Native message: chesscom.explanation_engine.v1.CoachHint

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "CoachHint",
  "field": [
    {
      "name": "move",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    },
    {
      "name": "speech",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.Speech",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "speech_debug_info",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SpeechDebugInfo",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_speech"
    },
    {
      "name": "_speech_debug_info"
    }
  ]
}

### Evidence

- **SRC-0943** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_hint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/aedd97b81c3e13431a50459da31a393e19ea768372afdff18e8ef32df1c4e21e.bin)

**Source references:** SRC-0943, SRC-1807  
**URL references:** None independently associated  
**Related findings:** FND-13744, FND-13745, FND-13746

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13748"></a>
## FND-13748: chesscom.explanation_engine.v1.CoachHint.move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoachHint",
  "name": "move",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0943",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0943** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_hint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/aedd97b81c3e13431a50459da31a393e19ea768372afdff18e8ef32df1c4e21e.bin)

**Source references:** SRC-0943, SRC-1807  
**URL references:** None independently associated  
**Related findings:** FND-13744, FND-13745, FND-13746

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13749"></a>
## FND-13749: chesscom.explanation_engine.v1.CoachHint.speech = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoachHint",
  "name": "speech",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.Speech",
  "label": "LABEL_OPTIONAL",
  "oneof": "_speech",
  "proto3_optional": true,
  "source_id": "SRC-0943",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0943** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_hint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/aedd97b81c3e13431a50459da31a393e19ea768372afdff18e8ef32df1c4e21e.bin)

**Source references:** SRC-0943, SRC-1807  
**URL references:** None independently associated  
**Related findings:** FND-13744, FND-13745, FND-13746

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13750"></a>
## FND-13750: chesscom.explanation_engine.v1.CoachHint.speech_debug_info = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.CoachHint",
  "name": "speech_debug_info",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.SpeechDebugInfo",
  "label": "LABEL_OPTIONAL",
  "oneof": "_speech_debug_info",
  "proto3_optional": true,
  "source_id": "SRC-0943",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0943** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_coach_hint.proto.bin` — [preserved redacted evidence](../evidence/descriptors/aedd97b81c3e13431a50459da31a393e19ea768372afdff18e8ef32df1c4e21e.bin)

**Source references:** SRC-0943, SRC-1807  
**URL references:** None independently associated  
**Related findings:** FND-13744, FND-13745, FND-13746

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13751"></a>
## FND-13751: Native message: chesscom.explanation_engine.v1.GetCompressedPositionRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetCompressedPositionRequest",
  "field": [
    {
      "name": "position",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Position",
      "oneof_index": 0
    },
    {
      "name": "fen",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "position_to_convert"
    }
  ]
}

### Evidence

- **SRC-0944** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_compressed_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0220e19fc23cd9623812bc37281679956ed29d0a87dbfc833cdd1185990ac0a6.bin)

**Source references:** SRC-0944, SRC-1742  
**URL references:** None independently associated  
**Related findings:** FND-13752, FND-13753

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13752"></a>
## FND-13752: chesscom.explanation_engine.v1.GetCompressedPositionRequest.position = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetCompressedPositionRequest",
  "name": "position",
  "number": 1,
  "type": ".chesscom.chess.v1.Position",
  "label": "LABEL_OPTIONAL",
  "oneof": "position_to_convert",
  "proto3_optional": false,
  "source_id": "SRC-0944",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0944** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_compressed_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0220e19fc23cd9623812bc37281679956ed29d0a87dbfc833cdd1185990ac0a6.bin)

**Source references:** SRC-0944, SRC-1742  
**URL references:** None independently associated  
**Related findings:** FND-13751, FND-13753

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13753"></a>
## FND-13753: chesscom.explanation_engine.v1.GetCompressedPositionRequest.fen = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetCompressedPositionRequest",
  "name": "fen",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "position_to_convert",
  "proto3_optional": false,
  "source_id": "SRC-0944",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0944** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_compressed_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0220e19fc23cd9623812bc37281679956ed29d0a87dbfc833cdd1185990ac0a6.bin)

**Source references:** SRC-0944, SRC-1742  
**URL references:** None independently associated  
**Related findings:** FND-13751, FND-13752

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13754"></a>
## FND-13754: Native message: chesscom.explanation_engine.v1.GetCompressedPositionResponse

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetCompressedPositionResponse",
  "field": [
    {
      "name": "compressed_position",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BYTES"
    }
  ]
}

### Evidence

- **SRC-0944** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_compressed_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0220e19fc23cd9623812bc37281679956ed29d0a87dbfc833cdd1185990ac0a6.bin)

**Source references:** SRC-0944, SRC-1742  
**URL references:** None independently associated  
**Related findings:** FND-13751, FND-13752, FND-13753

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13755"></a>
## FND-13755: chesscom.explanation_engine.v1.GetCompressedPositionResponse.compressed_position = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetCompressedPositionResponse",
  "name": "compressed_position",
  "number": 1,
  "type": "TYPE_BYTES",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0944",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0944** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_compressed_position.proto.bin` — [preserved redacted evidence](../evidence/descriptors/0220e19fc23cd9623812bc37281679956ed29d0a87dbfc833cdd1185990ac0a6.bin)

**Source references:** SRC-0944, SRC-1742  
**URL references:** None independently associated  
**Related findings:** FND-13751, FND-13752, FND-13753

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13756"></a>
## FND-13756: Native message: chesscom.explanation_engine.v1.GetErgonomicGameRequest

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GetErgonomicGameRequest",
  "field": [
    {
      "name": "game_state",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GameState",
      "oneof_index": 0
    },
    {
      "name": "pgn",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0
    },
    {
      "name": "starting_game_point",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0
    }
  ],
  "oneof_decl": [
    {
      "name": "game_to_convert"
    }
  ]
}

### Evidence

- **SRC-0945** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_ergonomic_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/29d7d74cec1b9d103d521cdbeb4313597875bb6a99e2ec21b3dd9561be195cd7.bin)

**Source references:** SRC-0945, SRC-1694  
**URL references:** None independently associated  
**Related findings:** FND-13757, FND-13758

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13757"></a>
## FND-13757: chesscom.explanation_engine.v1.GetErgonomicGameRequest.game_state = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetErgonomicGameRequest",
  "name": "game_state",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.GameState",
  "label": "LABEL_OPTIONAL",
  "oneof": "game_to_convert",
  "proto3_optional": false,
  "source_id": "SRC-0945",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0945** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_ergonomic_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/29d7d74cec1b9d103d521cdbeb4313597875bb6a99e2ec21b3dd9561be195cd7.bin)

**Source references:** SRC-0945, SRC-1694  
**URL references:** None independently associated  
**Related findings:** FND-13756, FND-13758

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13758"></a>
## FND-13758: chesscom.explanation_engine.v1.GetErgonomicGameRequest.pgn = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetErgonomicGameRequest",
  "name": "pgn",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "game_to_convert",
  "proto3_optional": false,
  "source_id": "SRC-0945",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0945** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_ergonomic_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/29d7d74cec1b9d103d521cdbeb4313597875bb6a99e2ec21b3dd9561be195cd7.bin)

**Source references:** SRC-0945, SRC-1694  
**URL references:** None independently associated  
**Related findings:** FND-13756, FND-13757

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-13759"></a>
## FND-13759: chesscom.explanation_engine.v1.GetErgonomicGameRequest.starting_game_point = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GetErgonomicGameRequest",
  "name": "starting_game_point",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "game_to_convert",
  "proto3_optional": false,
  "source_id": "SRC-0945",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0945** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_feature_get_ergonomic_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/29d7d74cec1b9d103d521cdbeb4313597875bb6a99e2ec21b3dd9561be195cd7.bin)

**Source references:** SRC-0945, SRC-1694  
**URL references:** None independently associated  
**Related findings:** FND-13756, FND-13757, FND-13758

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
