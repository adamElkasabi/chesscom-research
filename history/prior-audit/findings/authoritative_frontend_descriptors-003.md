# authoritative_frontend_descriptors — findings 201–300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-17648"></a>
## FND-17648: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_coach_hint.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_coach_hint.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetCoachHintRequest",
      "options": {}
    },
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
      "options": {},
      "oneof_decl": [
        {
          "name": "_hint"
        }
      ]
    },
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
      "options": {},
      "oneof_decl": [
        {
          "name": "_speech"
        },
        {
          "name": "_speech_debug_info"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 255201.

```text
vdmVDbGFzc2lmaWNhdGlvbhIlCh1wbHlfdW50aWxfZmxpcF9ib2FyZF9jb29sZG93bhgCIAEoBToHgqYdAwoBAWIGcHJvdG8z","chesscom/explanation_engine/v1/feature_get_coach_hint.proto":"CjtjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfY29hY2hfaGludC5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIh4KE0dldENvYWNoSGludFJlcXVlc3Q6B4KmHQMKAQEiZgoUR2V0Q29hY2hIaW50UmVzcG9uc2USPAoEaGludBgBIAEoCzIpLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17649"></a>
## FND-17649: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_compressed_position.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_compressed_position.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
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
    },
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
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 255898.

```text
2MS5TcGVlY2hEZWJ1Z0luZm9IAYgBAToHgqYdAwoBAUIJCgdfc3BlZWNoQhQKEl9zcGVlY2hfZGVidWdfaW5mb2IGcHJvdG8z","chesscom/explanation_engine/v1/feature_get_compressed_position.proto":"CkRjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfY29tcHJlc3NlZF9wb3NpdGlvbi5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxInUKHEdldENvbXByZXNzZWRQb3NpdGlvblJlcXVlc3QSLwoIcG9zaXRpb24YASABKAsyGy5jaGVzc2NvbS5jaGVzcy52MS5Qb3NpdGlvbkgAEg0KA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17650"></a>
## FND-17650: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_ergonomic_position.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_ergonomic_position.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetErgonomicPositionRequest",
      "field": [
        {
          "name": "compressed_position",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BYTES",
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
      "options": {},
      "oneof_decl": [
        {
          "name": "position_to_convert"
        }
      ]
    },
    {
      "name": "GetErgonomicPositionResponse",
      "field": [
        {
          "name": "position",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Position"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 256360.

```text
lcnQiPAodR2V0Q29tcHJlc3NlZFBvc2l0aW9uUmVzcG9uc2USGwoTY29tcHJlc3NlZF9wb3NpdGlvbhgBIAEoDGIGcHJvdG8z","chesscom/explanation_engine/v1/feature_get_ergonomic_position.proto":"CkNjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfZXJnb25vbWljX3Bvc2l0aW9uLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEiawobR2V0RXJnb25vbWljUG9zaXRpb25SZXF1ZXN0Eh0KE2NvbXByZXNzZWRfcG9zaXRpb24YASABKAxIABINCgNmZW4YAiABKAlIADoHgqYdAwoBAU
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17651"></a>
## FND-17651: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_fen.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_fen.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetFenRequest",
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
          "name": "compressed_position",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BYTES",
          "oneof_index": 0
        },
        {
          "name": "fen_notation",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.FenNotation",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "position_to_convert"
        },
        {
          "name": "_fen_notation"
        }
      ]
    },
    {
      "name": "GetFenResponse",
      "field": [
        {
          "name": "fen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 256841.

```text
uUmVzcG9uc2USLQoIcG9zaXRpb24YASABKAsyGy5jaGVzc2NvbS5jaGVzcy52MS5Qb3NpdGlvbjoHgqYdAwoBAWIGcHJvdG8z","chesscom/explanation_engine/v1/feature_get_fen.proto":"CjRjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfZmVuLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEi2AEKDUdldEZlblJlcXVlc3QSLwoIcG9zaXRpb24YASABKAsyGy5jaGVzc2NvbS5jaGVzcy52MS5Qb3NpdGlvbkgAEh0KE2NvbXByZXNzZWRfcG9zaXRpb24YAiABKAxIABJGCgxmZW5fbm90YXRpb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17652"></a>
## FND-17652: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_game_result.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_game_result.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetGameResultRequest",
      "options": {}
    },
    {
      "name": "GetGameResultResponse",
      "field": [
        {
          "name": "game_result",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameResult",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_game_result"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 257370.

```text
9jb252ZXJ0Qg8KDV9mZW5fbm90YXRpb24iJgoOR2V0RmVuUmVzcG9uc2USCwoDZmVuGAEgASgJOgeCph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/feature_get_game_result.proto":"CjxjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfZ2FtZV9yZXN1bHQucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSIfChRHZXRHYW1lUmVzdWx0UmVxdWVzdDoHgqYdAwoBASJpChVHZXRHYW1lUmVzdWx0UmVzcG9uc2USNwoLZ2FtZV9yZXN1bHQYASABKAsyHS5jaGVzc2NvbS5jaGVzcy52M
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17653"></a>
## FND-17653: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_san_moves.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_san_moves.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetSanMovesRequest",
      "field": [
        {
          "name": "fen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "proto_moves",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.MoveList",
          "oneof_index": 0
        },
        {
          "name": "uci_moves",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.UciMoveList",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "variation"
        },
        {
          "name": "_fen"
        }
      ]
    },
    {
      "name": "GetSanMovesResponse",
      "field": [
        {
          "name": "san_moves",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 257759.

```text
ABKAsyHS5jaGVzc2NvbS5jaGVzcy52MS5HYW1lUmVzdWx0SACIAQE6B4KmHQMKAQFCDgoMX2dhbWVfcmVzdWx0YgZwcm90bzM","chesscom/explanation_engine/v1/feature_get_san_moves.proto":"CjpjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfc2FuX21vdmVzLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEixwEKEkdldFNhbk1vdmVzUmVxdWVzdBIQCgNmZW4YASABKAlIAYgBARI/Cgtwcm90b19tb3ZlcxgCIAEoCzIoLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Nb3ZlTGl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17654"></a>
## FND-17654: Full frontend descriptor: chesscom/explanation_engine/v1/feature_legal_moves.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_legal_moves.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "LegalMovesRequest",
      "options": {}
    },
    {
      "name": "LegalMovesResponse",
      "field": [
        {
          "name": "legal_moves",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 258294.

```text
lhdGlvbkIGCgRfZmVuIjEKE0dldFNhbk1vdmVzUmVzcG9uc2USEQoJc2FuX21vdmVzGAEgAygJOgeCph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/feature_legal_moves.proto":"CjhjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9sZWdhbF9tb3Zlcy5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIhwKEUxlZ2FsTW92ZXNSZXF1ZXN0OgeCph0DCgEBIksKEkxlZ2FsTW92ZXNSZXNwb25zZRIsCgtsZWdhbF9tb3ZlcxgBIAMoCzIXLmNoZXNzY29tLmNoZXNzLnYxLk1vdmU6B4KmHQMKA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17655"></a>
## FND-17655: Full frontend descriptor: chesscom/explanation_engine/v1/feature_load_and_set_coach.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_load_and_set_coach.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "LoadAndSetCoachRequest",
      "field": [
        {
          "name": "text_asset",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.TextAsset"
        }
      ],
      "options": {}
    },
    {
      "name": "LoadAndSetCoachResponse",
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 258630.

```text
XNSZXNwb25zZRIsCgtsZWdhbF9tb3ZlcxgBIAMoCzIXLmNoZXNzY29tLmNoZXNzLnYxLk1vdmU6B4KmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/feature_load_and_set_coach.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9sb2FkX2FuZF9zZXRfY29hY2gucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSJgChZMb2FkQW5kU2V0Q29hY2hSZXF1ZXN0Ej0KCnRleHRfYXNzZXQYAiABKAsyKS5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuVGV4dEFzc2V0OgeCph
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17656"></a>
## FND-17656: Full frontend descriptor: chesscom/explanation_engine/v1/feature_load_bot.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_load_bot.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "LoadBotRequest",
      "field": [
        {
          "name": "bot_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "content_format",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.BotContentFormat"
        },
        {
          "name": "bot_content",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "artifact_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "LoadBotResponse",
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "BotContentFormat",
      "value": [
        {
          "name": "BOT_CONTENT_FORMAT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "BOT_CONTENT_FORMAT_JSON",
          "number": 1
        },
        {
          "name": "BOT_CONTENT_FORMAT_BASE64",
          "number": 2
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 259018.

```text
9lbmdpbmUudjEuVGV4dEFzc2V0OgeCph0DCgEBIiIKF0xvYWRBbmRTZXRDb2FjaFJlc3BvbnNlOgeCph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/feature_load_bot.proto":"CjVjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9sb2FkX2JvdC5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIp8BCg5Mb2FkQm90UmVxdWVzdBIQCghib3RfbmFtZRgBIAEoCRJICg5jb250ZW50X2Zvcm1hdBgCIAEoDjIwLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Cb3RDb250ZW50Rm9ybWF0
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17657"></a>
## FND-17657: Full frontend descriptor: chesscom/explanation_engine/v1/feature_lua_completion.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_lua_completion.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "LuaCompletionRequest"
    },
    {
      "name": "LuaCompletionResponse",
      "field": [
        {
          "name": "items",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 259624.

```text
JPVF9DT05URU5UX0ZPUk1BVF9KU09OEAESHQoZQk9UX0NPTlRFTlRfRk9STUFUX0JBU0U2NBACGgeKph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/feature_lua_completion.proto":"CjtjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9sdWFfY29tcGxldGlvbi5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIhYKFEx1YUNvbXBsZXRpb25SZXF1ZXN0IiYKFUx1YUNvbXBsZXRpb25SZXNwb25zZRINCgVpdGVtcxgBIAMoCWIGcHJvdG8z","chesscom/explanation_engine/v1/feat
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17658"></a>
## FND-17658: Full frontend descriptor: chesscom/explanation_engine/v1/feature_make_moves.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_make_moves.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "MakeMovesRequest",
      "field": [
        {
          "name": "moves",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "is_played_line",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "MakeMovesResponse",
      "field": [
        {
          "name": "line",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePointInfo"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 259909.

```text
xIhYKFEx1YUNvbXBsZXRpb25SZXF1ZXN0IiYKFUx1YUNvbXBsZXRpb25SZXNwb25zZRINCgVpdGVtcxgBIAMoCWIGcHJvdG8z","chesscom/explanation_engine/v1/feature_make_moves.proto":"CjdjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9tYWtlX21vdmVzLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEiWwoQTWFrZU1vdmVzUmVxdWVzdBImCgVtb3ZlcxgBIAMoCzIXLmNoZXNzY29tLmNoZXNzLnYxLk1vdmUSFgoOaXNfcGxheWVkX2xpbmUYAiABKAg6B4KmHQMKAQEiWQoRTWFrZU1vdmVzUm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17659"></a>
## FND-17659: Full frontend descriptor: chesscom/explanation_engine/v1/feature_run_lua.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_run_lua.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "RunLuaRequest",
      "field": [
        {
          "name": "lua_code",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "keep_lua_session",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "lua_session_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "artifact_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "oneof_decl": [
        {
          "name": "_lua_session_id"
        }
      ]
    },
    {
      "name": "RunLuaResponse",
      "field": [
        {
          "name": "is_lua_error",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "lua_error_msg",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "script_stdout",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "json_result",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "lua_session_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_lua_session_id"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 260345.

```text
luZRgBIAMoCzItLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5HYW1lUG9pbnRJbmZvOgeCph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/feature_run_lua.proto":"CjRjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9ydW5fbHVhLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEigAEKDVJ1bkx1YVJlcXVlc3QSEAoIbHVhX2NvZGUYASABKAkSGAoQa2VlcF9sdWFfc2Vzc2lvbhgCIAEoCBIbCg5sdWFfc2Vzc2lvbl9pZBgDIAEoBUgAiAEBEhMKC2FydGlmYWN0X2lkGAQgASgJQ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17660"></a>
## FND-17660: Full frontend descriptor: chesscom/explanation_engine/v1/feature_set_game_result.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_set_game_result.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "SetGameResultRequest",
      "field": [
        {
          "name": "claimed_game_result",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameResult"
        }
      ],
      "options": {}
    },
    {
      "name": "SetGameResultResponse",
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 260911.

```text
qc29uX3Jlc3VsdBgEIAEoCRIbCg5sdWFfc2Vzc2lvbl9pZBgFIAEoBUgAiAEBQhEKD19sdWFfc2Vzc2lvbl9pZGIGcHJvdG8z","chesscom/explanation_engine/v1/feature_set_game_result.proto":"CjxjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9zZXRfZ2FtZV9yZXN1bHQucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSJbChRTZXRHYW1lUmVzdWx0UmVxdWVzdBI6ChNjbGFpbWVkX2dhbWVfcmVzdWx0GAEgASgLMh0uY2hlc3Njb20uY2hlc3MudjEuR2FtZVJlc3VsdDoHgqYdAwoBASIgChVTZ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17661"></a>
## FND-17661: Full frontend descriptor: chesscom/explanation_engine/v1/feature_set_played_line.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_set_played_line.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "SetPlayedLineRequest",
      "options": {}
    },
    {
      "name": "SetPlayedLineResponse",
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 261283.

```text
20uY2hlc3MudjEuR2FtZVJlc3VsdDoHgqYdAwoBASIgChVTZXRHYW1lUmVzdWx0UmVzcG9uc2U6B4KmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/feature_set_played_line.proto":"CjxjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9zZXRfcGxheWVkX2xpbmUucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSIfChRTZXRQbGF5ZWRMaW5lUmVxdWVzdDoHgqYdAwoBASIgChVTZXRQbGF5ZWRMaW5lUmVzcG9uc2U6B4KmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17662"></a>
## FND-17662: Full frontend descriptor: chesscom/explanation_engine/v1/feature_update_experimental_options.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_update_experimental_options.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "UpdateExperimentalOptionsRequest",
      "field": [
        {
          "name": "options",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.ExperimentalOptions"
        }
      ],
      "options": {}
    },
    {
      "name": "UpdateExperimentalOptionsResponse",
      "field": [
        {
          "name": "options",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.ExperimentalOptions"
        }
      ],
      "options": {}
    },
    {
      "name": "ExperimentalOptions",
      "field": [
        {
          "name": "play_coach_flip_board_enabled",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "play_coach_retry_misses_enabled",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "illegal_move_explanation_mode",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.IllegalMoveExplanationMode",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "allow_tricky_classification",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 3,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_play_coach_flip_board_enabled"
        },
        {
          "name": "_play_coach_retry_misses_enabled"
        },
        {
          "name": "_illegal_move_explanation_mode"
        },
        {
          "name": "_allow_tricky_classification"
        }
      ],
      "reserved_range": [
        {
          "start": 1,
          "end": 5
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 261575.

```text
hRTZXRQbGF5ZWRMaW5lUmVxdWVzdDoHgqYdAwoBASIgChVTZXRQbGF5ZWRMaW5lUmVzcG9uc2U6B4KmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/feature_update_experimental_options.proto":"CkhjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV91cGRhdGVfZXhwZXJpbWVudGFsX29wdGlvbnMucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSJxCiBVcGRhdGVFeHBlcmltZW50YWxPcHRpb25zUmVxdWVzdBJECgdvcHRpb25zGAEgASgLMjMuY2hlc3Njb20uZXhwbGFuYXRpb25fZ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17663"></a>
## FND-17663: Full frontend descriptor: chesscom/explanation_engine/v1/feature_validate_fen.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_validate_fen.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "ValidateFenRequest",
      "field": [
        {
          "name": "fen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "check_syntax_only",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "ValidateFenResponse",
      "field": [
        {
          "name": "error",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "result_type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.ResultType",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_error"
        },
        {
          "name": "_result_type"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 262661.

```text
sZWdhbF9tb3ZlX2V4cGxhbmF0aW9uX21vZGVCHgocX2FsbG93X3RyaWNreV9jbGFzc2lmaWNhdGlvbkoECAEQBWIGcHJvdG8z","chesscom/explanation_engine/v1/feature_validate_fen.proto":"CjljaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV92YWxpZGF0ZV9mZW4ucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSJFChJWYWxpZGF0ZUZlblJlcXVlc3QSCwoDZmVuGAEgASgJEhkKEWNoZWNrX3N5bnRheF9vbmx5GAIgASgIOgeCph0DCgEBIoUBChNWYWxpZGF0ZUZlblJlc3BvbnNlEhIKBWVycm9y
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17664"></a>
## FND-17664: Full frontend descriptor: chesscom/explanation_engine/v1/internal_feature_maia_botmove.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/internal_feature_maia_botmove.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "InternalFeatureMaiaBotMoveRequest",
      "field": [
        {
          "name": "elo_self",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "elo_oppo",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "json",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "InternalFeatureMaiaBotMoveResponse",
      "field": [
        {
          "name": "move",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "json",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 263132.

```text
zc2NvbS5jaGVzcy52MS5SZXN1bHRUeXBlSAGIAQE6B4KmHQMKAQFCCAoGX2Vycm9yQg4KDF9yZXN1bHRfdHlwZWIGcHJvdG8z","chesscom/explanation_engine/v1/internal_feature_maia_botmove.proto":"CkJjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvaW50ZXJuYWxfZmVhdHVyZV9tYWlhX2JvdG1vdmUucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSJVCiFJbnRlcm5hbEZlYXR1cmVNYWlhQm90TW92ZVJlcXVlc3QSEAoIZWxvX3NlbGYYASABKAUSEAoIZWxvX29wcG8YAiABKAUSDAoEanNvbhgDIAEoCSJ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17665"></a>
## FND-17665: Full frontend descriptor: chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "PuzzleGenFailureReason",
      "field": [
        {
          "name": "failure_phase",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleGenPhase"
        },
        {
          "name": "failure_type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleGenFailureType"
        },
        {
          "name": "failure_message",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "InternalFeaturePuzzleGenRequest",
      "field": [
        {
          "name": "stream_progress",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "full_selected_line",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "do_puzzle_tree_generation",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "do_selected_line_verification",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "do_pitch_verification",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "add_variations_to_pgn",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "mode",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleGenMode",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "engine",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.CeeInternalEngine",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "include_board_events_in_pgn",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "filter_board_events_in_pgn",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "include_speech_in_pgn",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "heartbeat_interval_seconds",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "oneof_decl": [
        {
          "name": "_do_puzzle_tree_generation"
        },
        {
          "name": "_do_selected_line_verification"
        },
        {
          "name": "_do_pitch_verification"
        },
        {
          "name": "_add_variations_to_pgn"
        },
        {
          "name": "_mode"
        },
        {
          "name": "_engine"
        },
        {
          "name": "_include_board_events_in_pgn"
        },
        {
          "name": "_filter_board_events_in_pgn"
        },
        {
          "name": "_include_speech_in_pgn"
        }
      ]
    },
    {
      "name": "InternalFeaturePuzzleGenResponse",
      "field": [
        {
          "name": "puzzle_gen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleGen",
          "oneof_index": 0
        },
        {
          "name": "progress",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleGenPhase",
          "oneof_index": 0
        },
        {
          "name": "log",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "failure_reason",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleGenFailureReason",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "is_heartbeat",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "oneof_decl": [
        {
          "name": "puzzle_response"
        },
        {
          "name": "_failure_reason"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "PuzzleGenPhase",
      "value": [
        {
          "name": "PUZZLE_GEN_PHASE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PUZZLE_GEN_PHASE_INIT",
          "number": 1
        },
        {
          "name": "PUZZLE_GEN_PHASE_BUILDING_PUZZLE_TREE",
          "number": 2
        },
        {
          "name": "PUZZLE_GEN_PHASE_ADDED_PUZZLE_TREE_NODE",
          "number": 3
        },
        {
          "name": "PUZZLE_GEN_PHASE_SELECTING_PUZZLE_LINE",
          "number": 4
        },
        {
          "name": "PUZZLE_GEN_PHASE_VERIFYING_SELECTED_LINE_EVALS",
          "number": 5
        },
        {
          "name": "PUZZLE_GEN_PHASE_PUZZLE_POSITION_VERIFICATION_IN_PROGRESS",
          "number": 6
        },
        {
          "name": "PUZZLE_GEN_PHASE_COMPUTING_GOALS",
          "number": 7
        },
        {
          "name": "PUZZLE_GEN_PHASE_COMPUTING_THEMES",
          "number": 8
        },
        {
          "name": "PUZZLE_GEN_PHASE_DONE",
          "number": 9
        }
      ]
    },
    {
      "name": "PuzzleGenFailureType",
      "value": [
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_ILLEGAL_MOVE",
          "number": 1
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_PUZZLE_TOO_SHORT",
          "number": 2
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME",
          "number": 3
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_AFTER_PITCH_TOO_LOSING",
          "number": 4
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_BEFORE_PITCH_TOO_WINNING",
          "number": 5
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_TOO_STRONG",
          "number": 6
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_BEST_MOVE_TOO_LOSING",
          "number": 7
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_ABSOLUTE",
          "number": 8
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_RELATIVE",
          "number": 9
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_PLAYER_MOVE_NOT_CRITICAL",
          "number": 10
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_NOT_A_MISTAKE",
          "number": 11
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_GAME_PHASE",
          "number": 12
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_LOSES_MATERIAL",
          "number": 13
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_MATERIAL_IMBALANCE",
          "number": 14
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_EXPECTED_OUTCOME",
          "number": 15
        },
        {
          "name": "PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_BOARD_EVENT",
          "number": 16
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 263586.

```text
W92ZVJlc3BvbnNlEiUKBG1vdmUYASABKAsyFy5jaGVzc2NvbS5jaGVzcy52MS5Nb3ZlEgwKBGpzb24YAiABKAliBnByb3RvMw","chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto":"CkBjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvaW50ZXJuYWxfZmVhdHVyZV9wdXp6bGVfZ2VuLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEixAEKFlB1enpsZUdlbkZhaWx1cmVSZWFzb24SRQoNZmFpbHVyZV9waGFzZRgBIAEoDjIuLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5QdXp6bGVHZ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17666"></a>
## FND-17666: Full frontend descriptor: chesscom/explanation_engine/v1/explanation_engine_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/explanation_engine_service.proto",
  "package": "chesscom.explanation_engine.v1",
  "service": [
    {
      "name": "ExplanationEngineService",
      "method": [
        {
          "name": "GetCeeVersion",
          "input_type": ".chesscom.explanation_engine.v1.CeeVersionRequest",
          "output_type": ".chesscom.explanation_engine.v1.CeeVersionResponse",
          "options": {}
        },
        {
          "name": "CreateNewGame",
          "input_type": ".chesscom.explanation_engine.v1.NewGameRequest",
          "output_type": ".chesscom.explanation_engine.v1.NewGameResponse",
          "options": {}
        },
        {
          "name": "LoadGameState",
          "input_type": ".chesscom.explanation_engine.v1.LoadGameStateRequest",
          "output_type": ".chesscom.explanation_engine.v1.LoadGameStateResponse",
          "options": {}
        },
        {
          "name": "AddEvaluations",
          "input_type": ".chesscom.explanation_engine.v1.AddEvaluationsRequest",
          "output_type": ".chesscom.explanation_engine.v1.AddEvaluationsResponse",
          "options": {}
        },
        {
          "name": "GetExpectedPoints",
          "input_type": ".chesscom.explanation_engine.v1.ExpectedPointsRequest",
          "output_type": ".chesscom.explanation_engine.v1.ExpectedPointsResponse",
          "options": {}
        },
        {
          "name": "ValidateFen",
          "input_type": ".chesscom.explanation_engine.v1.ValidateFenRequest",
          "output_type": ".chesscom.explanation_engine.v1.ValidateFenResponse",
          "options": {}
        },
        {
          "name": "ValidatePgn",
          "input_type": ".chesscom.explanation_engine.v1.ValidatePgnRequest",
          "output_type": ".chesscom.explanation_engine.v1.ValidatePgnResponse",
          "options": {}
        },
        {
          "name": "GetPgn",
          "input_type": ".chesscom.explanation_engine.v1.GetPgnRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetPgnResponse",
          "options": {}
        },
        {
          "name": "GetFen",
          "input_type": ".chesscom.explanation_engine.v1.GetFenRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetFenResponse",
          "options": {}
        },
        {
          "name": "GetMoveDetails",
          "input_type": ".chesscom.explanation_engine.v1.GetMoveDetailsRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetMoveDetailsResponse",
          "options": {}
        },
        {
          "name": "GetMoveClassification",
          "input_type": ".chesscom.explanation_engine.v1.MoveClassificationRequest",
          "output_type": ".chesscom.explanation_engine.v1.MoveClassificationResponse",
          "options": {}
        },
        {
          "name": "GetAnalysisAnnotations",
          "input_type": ".chesscom.explanation_engine.v1.AnalysisAnnotationsRequest",
          "output_type": ".chesscom.explanation_engine.v1.AnalysisAnnotationsResponse",
          "options": {},
          "server_streaming": true
        },
        {
          "name": "MakeMoves",
          "input_type": ".chesscom.explanation_engine.v1.MakeMovesRequest",
          "output_type": ".chesscom.explanation_engine.v1.MakeMovesResponse",
          "options": {}
        },
        {
          "name": "SetPlayedLine",
          "input_type": ".chesscom.explanation_engine.v1.SetPlayedLineRequest",
          "output_type": ".chesscom.explanation_engine.v1.SetPlayedLineResponse",
          "options": {}
        },
        {
          "name": "GetGameReview",
          "input_type": ".chesscom.explanation_engine.v1.GameReviewRequest",
          "output_type": ".chesscom.explanation_engine.v1.GameReviewResponse",
          "options": {}
        },
        {
          "name": "GetGameState",
          "input_type": ".chesscom.explanation_engine.v1.GetGameStateRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetGameStateResponse",
          "options": {}
        },
        {
          "name": "GetGamePointInfo",
          "input_type": ".chesscom.explanation_engine.v1.GamePointInfoRequest",
          "output_type": ".chesscom.explanation_engine.v1.GamePointInfoResponse",
          "options": {}
        },
        {
          "name": "GetGameTree",
          "input_type": ".chesscom.explanation_engine.v1.GameTreeRequest",
          "output_type": ".chesscom.explanation_engine.v1.GameTreeResponse",
          "options": {}
        },
        {
          "name": "GetGameResult",
          "input_type": ".chesscom.explanation_engine.v1.GetGameResultRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetGameResultResponse",
          "options": {}
        },
        {
          "name": "SetGameResult",
          "input_type": ".chesscom.explanation_engine.v1.SetGameResultRequest",
          "output_type": ".chesscom.explanation_engine.v1.SetGameResultResponse",
          "options": {}
        },
        {
          "name": "GetLegalMoves",
          "input_type": ".chesscom.explanation_engine.v1.LegalMovesRequest",
          "output_type": ".chesscom.explanation_engine.v1.LegalMovesResponse",
          "options": {}
        },
        {
          "name": "GetLegalPremoves",
          "input_type": ".chesscom.explanation_engine.v1.LegalPremovesRequest",
          "output_type": ".chesscom.explanation_engine.v1.LegalPremovesResponse",
          "options": {}
        },
        {
          "name": "GetSanMoves",
          "input_type": ".chesscom.explanation_engine.v1.GetSanMovesRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetSanMovesResponse",
          "options": {}
        },
        {
          "name": "GetThreats",
          "input_type": ".chesscom.explanation_engine.v1.SimpleThreatsRequest",
          "output_type": ".chesscom.explanation_engine.v1.SimpleThreatsResponse",
          "options": {}
        },
        {
          "name": "GetGamePhaseTransitions",
          "input_type": ".chesscom.explanation_engine.v1.GamePhaseTransitionsRequest",
          "output_type": ".chesscom.explanation_engine.v1.GamePhaseTransitionsResponse",
          "options": {}
        },
        {
          "name": "GetOpening",
          "input_type": ".chesscom.explanation_engine.v1.GetOpeningRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetOpeningResponse",
          "options": {}
        },
        {
          "name": "LoadBot",
          "input_type": ".chesscom.explanation_engine.v1.LoadBotRequest",
          "output_type": ".chesscom.explanation_engine.v1.LoadBotResponse",
          "options": {}
        },
        {
          "name": "GetBotMove",
          "input_type": ".chesscom.explanation_engine.v1.GetBotMoveRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetBotMoveResponse",
          "options": {}
        },
        {
          "name": "GetBotMoveFromConfig",
          "input_type": ".chesscom.explanation_engine.v1.BotMoveFromConfigRequest",
          "output_type": ".chesscom.explanation_engine.v1.BotMoveFromConfigResponse",
          "options": {}
        },
        {
          "name": "GetBotConfigResources",
          "input_type": ".chesscom.explanation_engine.v1.BotConfigResourcesRequest",
          "output_type": ".chesscom.explanation_engine.v1.BotConfigResourcesResponse",
          "options": {}
        },
        {
          "name": "GetBotChat",
          "input_type": ".chesscom.explanation_engine.v1.GetBotChatRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetBotChatResponse",
          "options": {}
        },
        {
          "name": "GetPunishMove",
          "input_type": ".chesscom.explanation_engine.v1.GetPunishMoveRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetPunishMoveResponse",
          "options": {}
        },
        {
          "name": "LoadCoach",
          "input_type": ".chesscom.explanation_engine.v1.LoadCoachRequest",
          "output_type": ".chesscom.explanation_engine.v1.LoadCoachResponse",
          "options": {}
        },
        {
          "name": "SetCoach",
          "input_type": ".chesscom.explanation_engine.v1.SetCoachRequest",
          "output_type": ".chesscom.explanation_engine.v1.SetCoachResponse",
          "options": {}
        },
        {
          "name": "LoadAndSetCoach",
          "input_type": ".chesscom.explanation_engine.v1.LoadAndSetCoachRequest",
          "output_type": ".chesscom.explanation_engine.v1.LoadAndSetCoachResponse",
          "options": {}
        },
        {
          "name": "GetCoachChat",
          "input_type": ".chesscom.explanation_engine.v1.GetCoachChatRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetCoachChatResponse",
          "options": {}
        },
        {
          "name": "GetCoachHint",
          "input_type": ".chesscom.explanation_engine.v1.GetCoachHintRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetCoachHintResponse",
          "options": {}
        },
        {
          "name": "GetErgonomicPosition",
          "input_type": ".chesscom.explanation_engine.v1.GetErgonomicPositionRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetErgonomicPositionResponse",
          "options": {}
        },
        {
          "name": "GetErgonomicGame",
          "input_type": ".chesscom.explanation_engine.v1.GetErgonomicGameRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetErgonomicGameResponse",
          "options": {}
        },
        {
          "name": "GetCompressedPosition",
          "input_type": ".chesscom.explanation_engine.v1.GetCompressedPositionRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetCompressedPositionResponse",
          "options": {}
        },
        {
          "name": "ConvertToProtoMoves",
          "input_type": ".chesscom.explanation_engine.v1.ConvertToProtoMovesRequest",
          "output_type": ".chesscom.explanation_engine.v1.ConvertToProtoMovesResponse",
          "options": {}
        },
        {
          "name": "GetLuaCompletion",
          "input_type": ".chesscom.explanation_engine.v1.LuaCompletionRequest",
          "output_type": ".chesscom.explanation_engine.v1.LuaCompletionResponse",
          "options": {}
        },
        {
          "name": "RunLua",
          "input_type": ".chesscom.explanation_engine.v1.RunLuaRequest",
          "output_type": ".chesscom.explanation_engine.v1.RunLuaResponse",
          "options": {}
        },
        {
          "name": "UpdateExperimentalOptions",
          "input_type": ".chesscom.explanation_engine.v1.UpdateExperimentalOptionsRequest",
          "output_type": ".chesscom.explanation_engine.v1.UpdateExperimentalOptionsResponse",
          "options": {}
        },
        {
          "name": "GetCeeInternalComponents",
          "input_type": ".chesscom.explanation_engine.v1.CeeInternalComponentsRequest",
          "output_type": ".chesscom.explanation_engine.v1.CeeInternalComponentsResponse",
          "options": {}
        },
        {
          "name": "InternalFeaturePuzzleGen",
          "input_type": ".chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest",
          "output_type": ".chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse",
          "options": {}
        },
        {
          "name": "InternalFeatureUpdateDeveloperOptions",
          "input_type": ".chesscom.explanation_engine.v1.InternalFeatureUpdateDeveloperOptionsRequest",
          "output_type": ".chesscom.explanation_engine.v1.InternalFeatureUpdateDeveloperOptionsResponse",
          "options": {}
        },
        {
          "name": "InternalFeatureMaiaBotMove",
          "input_type": ".chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveRequest",
          "output_type": ".chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveResponse",
          "options": {}
        },
        {
          "name": "RunSearch",
          "input_type": ".chesscom.explanation_engine.v1.RunSearchRequest",
          "output_type": ".chesscom.explanation_engine.v1.RunSearchResponse",
          "options": {},
          "server_streaming": true
        },
        {
          "name": "DisposeGamePoint",
          "input_type": ".chesscom.explanation_engine.v1.DisposeGamePointRequest",
          "output_type": ".chesscom.explanation_engine.v1.DisposeGamePointResponse",
          "options": {}
        },
        {
          "name": "GetNonChessText",
          "input_type": ".chesscom.explanation_engine.v1.GetNonChessTextRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetNonChessTextResponse",
          "options": {}
        },
        {
          "name": "GetIllegalMoveExplanation",
          "input_type": ".chesscom.explanation_engine.v1.GetIllegalMoveExplanationRequest",
          "output_type": ".chesscom.explanation_engine.v1.GetIllegalMoveExplanationResponse",
          "options": {}
        }
      ]
    }
  ],
  "extension": [
    {
      "name": "command_type",
      "extendee": ".google.protobuf.MethodOptions",
      "number": 50001,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.CommandType",
      "json_name": "commandType"
    },
    {
      "name": "has_gp",
      "extendee": ".google.protobuf.MethodOptions",
      "number": 50002,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "json_name": "hasGp"
    },
    {
      "name": "ceac_field",
      "extendee": ".google.protobuf.MethodOptions",
      "number": 50003,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "json_name": "ceacField"
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17719"></a>
## FND-17719: Full frontend descriptor: chesscom/explanation_engine/v1/analyzability.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/analyzability.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "UnanalyzableGameTorchOnly",
      "options": {}
    },
    {
      "name": "UnanalyzableGameImpracticalTooLong",
      "options": {}
    },
    {
      "name": "UnanalyzableGameImpracticalNoMoves",
      "options": {}
    },
    {
      "name": "UnanalyzableGameImpracticalNoLegalMove",
      "options": {}
    },
    {
      "name": "UnanalyzableGameImpractical",
      "field": [
        {
          "name": "too_long",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.UnanalyzableGameImpracticalTooLong",
          "oneof_index": 0
        },
        {
          "name": "no_moves",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.UnanalyzableGameImpracticalNoMoves",
          "oneof_index": 0
        },
        {
          "name": "no_legal_move",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.UnanalyzableGameImpracticalNoLegalMove",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "impracticality"
        }
      ]
    },
    {
      "name": "UnanalyzableGame",
      "field": [
        {
          "name": "torch_only",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.UnanalyzableGameTorchOnly",
          "oneof_index": 0
        },
        {
          "name": "impractical",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.UnanalyzableGameImpractical",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "analyzability_constraint"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 278408.

```text
pzdGFnaW5nLmNoZXNzLXBsYXRmb3JtLmNvbRIXcHJvZC5jaGVzcy1wbGF0Zm9ybS5jb20aCxIJeC1hcGkta2V5YgZwcm90bzM","chesscom/explanation_engine/v1/analyzability.proto":"CjJjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvYW5hbHl6YWJpbGl0eS5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIiQKGVVuYW5hbHl6YWJsZUdhbWVUb3JjaE9ubHk6B4KmHQMKAQEiLQoiVW5hbmFseXphYmxlR2FtZUltcHJhY3RpY2FsVG9vTG9uZzoHgqYdAwoBASItCiJVbmFuYWx5emFibGVHYW1lSW1wcmFjdGljYWx
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17720"></a>
## FND-17720: Full frontend descriptor: chesscom/ceac/v2/error.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/ceac/v2/error.proto",
  "package": "chesscom.ceac.v2",
  "message_type": [
    {
      "name": "NoCapacityError"
    },
    {
      "name": "InvalidGameError",
      "options": {}
    },
    {
      "name": "GeneralError",
      "options": {}
    },
    {
      "name": "BadRequest",
      "field": [
        {
          "name": "invalid_game",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.InvalidGame",
          "oneof_index": 0
        },
        {
          "name": "unanalyzable_game",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.UnanalyzableGame",
          "oneof_index": 0
        },
        {
          "name": "invalid_request",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.InvalidRequestError",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "reason"
        }
      ]
    },
    {
      "name": "RateLimitedError",
      "options": {}
    },
    {
      "name": "InvalidRequestError",
      "options": {}
    },
    {
      "name": "AuthRequiredError",
      "options": {}
    },
    {
      "name": "ClientError",
      "field": [
        {
          "name": "bad_request",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.BadRequest",
          "oneof_index": 0
        },
        {
          "name": "rate_limited",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.RateLimitedError",
          "oneof_index": 0
        },
        {
          "name": "auth_required",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.AuthRequiredError",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "reason"
        }
      ]
    },
    {
      "name": "ServerError",
      "options": {}
    },
    {
      "name": "FailureError",
      "field": [
        {
          "name": "client_error",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.ClientError",
          "oneof_index": 0
        },
        {
          "name": "server_error",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.ServerError",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "kind"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 279571.

```text
5hbmFseXphYmxlR2FtZUltcHJhY3RpY2FsSAA6B4KmHQMKAQFCGgoYYW5hbHl6YWJpbGl0eV9jb25zdHJhaW50YgZwcm90bzM","chesscom/ceac/v2/error.proto":"ChxjaGVzc2NvbS9jZWFjL3YyL2Vycm9yLnByb3RvEhBjaGVzc2NvbS5jZWFjLnYyIhEKD05vQ2FwYWNpdHlFcnJvciIbChBJbnZhbGlkR2FtZUVycm9yOgeCph0DCgEBIhcKDEdlbmVyYWxFcnJvcjoHgqYdAwoBASL1AQoKQmFkUmVxdWVzdBJDCgxpbnZhbGlkX2dhbWUYASABKAsyKy5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuSW52YWxpZEdhbWVIABJNChF1bmFuYWx5e
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17721"></a>
## FND-17721: Full frontend descriptor: chesscom/ceac/v2/heartbeat.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/ceac/v2/heartbeat.proto",
  "package": "chesscom.ceac.v2",
  "message_type": [
    {
      "name": "Heartbeat",
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 280733.

```text
2ZXJfZXJyb3IYAiABKAsyHS5jaGVzc2NvbS5jZWFjLnYyLlNlcnZlckVycm9ySAA6B4KmHQMKAQFCBgoEa2luZGIGcHJvdG8z","chesscom/ceac/v2/heartbeat.proto":"CiBjaGVzc2NvbS9jZWFjL3YyL2hlYXJ0YmVhdC5wcm90bxIQY2hlc3Njb20uY2VhYy52MiIUCglIZWFydGJlYXQ6B4KmHQMKAQFiBnByb3RvMw","chesscom/ceac/v2/waiting_for_capacity.proto":"CitjaGVzc2NvbS9jZWFjL3YyL3dhaXRpbmdfZm9yX2NhcGFjaXR5LnByb3RvEhBjaGVzc2NvbS5jZWFjLnYyIh0KEldhaXRpbmdGb3JDYXBhY2l0eToHgqYdAwoBAW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17722"></a>
## FND-17722: Full frontend descriptor: chesscom/ceac/v2/waiting_for_capacity.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/ceac/v2/waiting_for_capacity.proto",
  "package": "chesscom.ceac.v2",
  "message_type": [
    {
      "name": "WaitingForCapacity",
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 280881.

```text
S9jZWFjL3YyL2hlYXJ0YmVhdC5wcm90bxIQY2hlc3Njb20uY2VhYy52MiIUCglIZWFydGJlYXQ6B4KmHQMKAQFiBnByb3RvMw","chesscom/ceac/v2/waiting_for_capacity.proto":"CitjaGVzc2NvbS9jZWFjL3YyL3dhaXRpbmdfZm9yX2NhcGFjaXR5LnByb3RvEhBjaGVzc2NvbS5jZWFjLnYyIh0KEldhaXRpbmdGb3JDYXBhY2l0eToHgqYdAwoBAWIGcHJvdG8z","chesscom/ceac/v2/client.proto":"Ch1jaGVzc2NvbS9jZWFjL3YyL2NsaWVudC5wcm90bxIQY2hlc3Njb20uY2VhYy52MiqcAwoGQ2xpZW50EhYKEkNMSUVOVF9VTlNQRUN
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17723"></a>
## FND-17723: Full frontend descriptor: chesscom/ceac/v2/client.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/ceac/v2/client.proto",
  "package": "chesscom.ceac.v2",
  "enum_type": [
    {
      "name": "Client",
      "value": [
        {
          "name": "CLIENT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CLIENT_WEB",
          "number": 1
        },
        {
          "name": "CLIENT_ANDROID",
          "number": 2
        },
        {
          "name": "CLIENT_IOS",
          "number": 3
        },
        {
          "name": "CLIENT_LC",
          "number": 4
        },
        {
          "name": "CLIENT_RCN",
          "number": 5
        },
        {
          "name": "CLIENT_EVENTS",
          "number": 6
        },
        {
          "name": "CLIENT_INSIGHTS",
          "number": 7
        },
        {
          "name": "CLIENT_STATS",
          "number": 8
        },
        {
          "name": "CLIENT_COACH_ASSET_UPDATER",
          "number": 9
        },
        {
          "name": "CLIENT_EVAL_CACHE_GENERATOR",
          "number": 10
        },
        {
          "name": "CLIENT_DEVELOPER",
          "number": 11
        },
        {
          "name": "CLIENT_PUZZLE_GEN",
          "number": 12
        },
        {
          "name": "CLIENT_TEXT_AUDIO",
          "number": 13
        },
        {
          "name": "CLIENT_CHESSKID_WEB",
          "number": 14
        },
        {
          "name": "CLIENT_CHESSKID_IOS",
          "number": 15
        },
        {
          "name": "CLIENT_CHESSKID_ANDROID",
          "number": 16
        },
        {
          "name": "CLIENT_TRAIN",
          "number": 17
        }
      ],
      "options": {}
    },
    {
      "name": "Product",
      "value": [
        {
          "name": "PRODUCT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PRODUCT_CEAC_INTERNAL",
          "number": 1
        },
        {
          "name": "PRODUCT_GAME_REVIEW",
          "number": 2
        },
        {
          "name": "PRODUCT_INSIGHTS",
          "number": 3
        },
        {
          "name": "PRODUCT_RAGE_QUIT_DETECTION",
          "number": 4
        },
        {
          "name": "PRODUCT_FAIR_PLAY_PRODUCTION",
          "number": 5
        },
        {
          "name": "PRODUCT_FAIR_PLAY_RESEARCH",
          "number": 6
        },
        {
          "name": "PRODUCT_EVENTS",
          "number": 7
        },
        {
          "name": "PRODUCT_ADVANCED_STATS",
          "number": 8
        },
        {
          "name": "PRODUCT_CORE_CHESS_RESEARCH",
          "number": 9
        },
        {
          "name": "PRODUCT_PUZZLES",
          "number": 10
        },
        {
          "name": "PRODUCT_TEXT_AUDIO",
          "number": 11
        },
        {
          "name": "PRODUCT_BRILLIANT_VERIFICATION",
          "number": 12
        },
        {
          "name": "PRODUCT_TRAIN",
          "number": 13
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 281066.

```text
yX2NhcGFjaXR5LnByb3RvEhBjaGVzc2NvbS5jZWFjLnYyIh0KEldhaXRpbmdGb3JDYXBhY2l0eToHgqYdAwoBAWIGcHJvdG8z","chesscom/ceac/v2/client.proto":"Ch1jaGVzc2NvbS9jZWFjL3YyL2NsaWVudC5wcm90bxIQY2hlc3Njb20uY2VhYy52MiqcAwoGQ2xpZW50EhYKEkNMSUVOVF9VTlNQRUNJRklFRBAAEg4KCkNMSUVOVF9XRUIQARISCg5DTElFTlRfQU5EUk9JRBACEg4KCkNMSUVOVF9JT1MQAxINCglDTElFTlRfTEMQBBIOCgpDTElFTlRfUkNOEAUSEQoNQ0xJRU5UX0VWRU5UUxAGEhMKD0NMSUVOVF9JTlNJR0hUUxAHEhAKDENMSUVO
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17724"></a>
## FND-17724: Full frontend descriptor: chesscom/ceac/v2/request_metadata.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/ceac/v2/request_metadata.proto",
  "package": "chesscom.ceac.v2",
  "message_type": [
    {
      "name": "RequestMetadata",
      "field": [
        {
          "name": "client",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.ceac.v2.Client"
        },
        {
          "name": "product",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.ceac.v2.Product"
        },
        {
          "name": "received_time",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "debug_mode",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "RequestOptions",
      "field": [
        {
          "name": "heartbeat_interval_seconds",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "use_progress_updates",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 282264.

```text
sSIgoeUFJPRFVDVF9CUklMTElBTlRfVkVSSUZJQ0FUSU9OEAwSEQoNUFJPRFVDVF9UUkFJThANGgeKph0DCgEBYgZwcm90bzM","chesscom/ceac/v2/request_metadata.proto":"CidjaGVzc2NvbS9jZWFjL3YyL3JlcXVlc3RfbWV0YWRhdGEucHJvdG8SEGNoZXNzY29tLmNlYWMudjIitwEKD1JlcXVlc3RNZXRhZGF0YRIoCgZjbGllbnQYASABKA4yGC5jaGVzc2NvbS5jZWFjLnYyLkNsaWVudBIqCgdwcm9kdWN0GAIgASgOMhkuY2hlc3Njb20uY2VhYy52Mi5Qcm9kdWN0EjEKDXJlY2VpdmVkX3RpbWUYAyABKAsyGi5nb29nbGUucHJvdG9idWYuVG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17725"></a>
## FND-17725: Full frontend descriptor: chesscom/ceac/v2/game_evaluation_options.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/ceac/v2/game_evaluation_options.proto",
  "package": "chesscom.ceac.v2",
  "message_type": [
    {
      "name": "GameEvaluationOptions",
      "field": [
        {
          "name": "use_game_state_cache",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "use_serial_evaluations",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 282771.

```text
WF0X2ludGVydmFsX3NlY29uZHMYBCABKAUSHAoUdXNlX3Byb2dyZXNzX3VwZGF0ZXMYBSABKAg6B4KmHQMKAQFiBnByb3RvMw","chesscom/ceac/v2/game_evaluation_options.proto":"Ci5jaGVzc2NvbS9jZWFjL3YyL2dhbWVfZXZhbHVhdGlvbl9vcHRpb25zLnByb3RvEhBjaGVzc2NvbS5jZWFjLnYyIl4KFUdhbWVFdmFsdWF0aW9uT3B0aW9ucxIcChR1c2VfZ2FtZV9zdGF0ZV9jYWNoZRgBIAEoCBIeChZ1c2Vfc2VyaWFsX2V2YWx1YXRpb25zGAIgASgIOgeCph0DCgEBYgZwcm90bzM","chesscom/ceac/v2/game_review_options.prot
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17726"></a>
## FND-17726: Full frontend descriptor: chesscom/ceac/v2/game_review_options.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/ceac/v2/game_review_options.proto",
  "package": "chesscom.ceac.v2",
  "message_type": [
    {
      "name": "GameReviewOptions",
      "field": [
        {
          "name": "report_card_entitled",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "include_train_takeaways",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "can_access_locked_takeaways",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 283050.

```text
VfZ2FtZV9zdGF0ZV9jYWNoZRgBIAEoCBIeChZ1c2Vfc2VyaWFsX2V2YWx1YXRpb25zGAIgASgIOgeCph0DCgEBYgZwcm90bzM","chesscom/ceac/v2/game_review_options.proto":"CipjaGVzc2NvbS9jZWFjL3YyL2dhbWVfcmV2aWV3X29wdGlvbnMucHJvdG8SEGNoZXNzY29tLmNlYWMudjIigAEKEUdhbWVSZXZpZXdPcHRpb25zEhwKFHJlcG9ydF9jYXJkX2VudGl0bGVkGAEgASgIEh8KF2luY2x1ZGVfdHJhaW5fdGFrZWF3YXlzGAIgASgIEiMKG2Nhbl9hY2Nlc3NfbG9ja2VkX3Rha2Vhd2F5cxgDIAEoCDoHgqYdAwoBAWIGcHJvdG8z","ches
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17727"></a>
## FND-17727: Full frontend descriptor: chesscom/ceac/v2/game_review.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/ceac/v2/game_review.proto",
  "package": "chesscom.ceac.v2",
  "message_type": [
    {
      "name": "GameReviewRequest",
      "field": [
        {
          "name": "new_game_req",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.NewGameRequest"
        },
        {
          "name": "run_search_req",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.RunSearchRequest"
        },
        {
          "name": "charm_inf_req",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CharmInferenceRequest"
        },
        {
          "name": "engine",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.engine.v1.Engine"
        },
        {
          "name": "game_evaluation_options",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.GameEvaluationOptions"
        },
        {
          "name": "request_metadata",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.RequestMetadata"
        },
        {
          "name": "request_options",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.RequestOptions"
        },
        {
          "name": "set_coach",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SetCoachRequest"
        },
        {
          "name": "game_review_options",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.GameReviewOptions"
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewResponse",
      "field": [
        {
          "name": "progress",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.GameReviewResponseProgress",
          "oneof_index": 0
        },
        {
          "name": "success",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.GameReviewResponseSuccess",
          "oneof_index": 0
        },
        {
          "name": "failure",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.GameReviewResponseFailure",
          "oneof_index": 0
        },
        {
          "name": "heartbeat",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.Heartbeat",
          "oneof_index": 0
        },
        {
          "name": "waiting_for_capacity",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.WaitingForCapacity",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "result"
        }
      ]
    },
    {
      "name": "GameReviewResponseSuccess",
      "field": [
        {
          "name": "game_review",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameReview"
        },
        {
          "name": "cee_c_api_calls",
          "number": 100,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewResponseProgress",
      "field": [
        {
          "name": "progress",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        }
      ],
      "options": {}
    },
    {
      "name": "GameReviewResponseFailure",
      "field": [
        {
          "name": "reason",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "invalid_game_error",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.InvalidGameError",
          "oneof_index": 0
        },
        {
          "name": "general_error",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.GeneralError",
          "oneof_index": 0
        },
        {
          "name": "failure_error",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.FailureError"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "error"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 283366.

```text
haW5fdGFrZWF3YXlzGAIgASgIEiMKG2Nhbl9hY2Nlc3NfbG9ja2VkX3Rha2Vhd2F5cxgDIAEoCDoHgqYdAwoBAWIGcHJvdG8z","chesscom/ceac/v2/game_review.proto":"CiJjaGVzc2NvbS9jZWFjL3YyL2dhbWVfcmV2aWV3LnByb3RvEhBjaGVzc2NvbS5jZWFjLnYyIu4EChFHYW1lUmV2aWV3UmVxdWVzdBJECgxuZXdfZ2FtZV9yZXEYASABKAsyLi5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuTmV3R2FtZVJlcXVlc3QSSAoOcnVuX3NlYXJjaF9yZXEYAiABKAsyMC5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuUnVuU2VhcmN
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17728"></a>
## FND-17728: Full frontend descriptor: chesscom/ceac/v2/run_search.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/ceac/v2/run_search.proto",
  "package": "chesscom.ceac.v2",
  "message_type": [
    {
      "name": "RunSearchRequest",
      "field": [
        {
          "name": "new_game_req",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.NewGameRequest"
        },
        {
          "name": "run_search_req",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.RunSearchRequest"
        },
        {
          "name": "engine",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.engine.v1.Engine"
        },
        {
          "name": "request_metadata",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.RequestMetadata"
        },
        {
          "name": "request_options",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.RequestOptions"
        },
        {
          "name": "key_position_search",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ]
    },
    {
      "name": "RunSearchResponse",
      "field": [
        {
          "name": "progress",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.RunSearchResponseProgress",
          "oneof_index": 0
        },
        {
          "name": "success",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.RunSearchResponseSuccess",
          "oneof_index": 0
        },
        {
          "name": "failure",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.RunSearchResponseFailure",
          "oneof_index": 0
        },
        {
          "name": "heartbeat",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.Heartbeat",
          "oneof_index": 0
        },
        {
          "name": "waiting_for_capacity",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.WaitingForCapacity",
          "oneof_index": 0
        }
      ],
      "oneof_decl": [
        {
          "name": "result"
        }
      ]
    },
    {
      "name": "RunSearchResponseSuccess",
      "field": [
        {
          "name": "run_search",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.RunSearchResponse"
        },
        {
          "name": "position_search_key",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_position_search_key"
        }
      ]
    },
    {
      "name": "RunSearchResponseProgress",
      "field": [
        {
          "name": "run_search",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.RunSearchResponse"
        }
      ]
    },
    {
      "name": "RunSearchResponseFailure",
      "field": [
        {
          "name": "reason",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "invalid_game_error",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.InvalidGameError",
          "oneof_index": 0
        },
        {
          "name": "general_error",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.GeneralError",
          "oneof_index": 0
        },
        {
          "name": "failure_error",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ceac.v2.FailureError"
        }
      ],
      "oneof_decl": [
        {
          "name": "error"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 285366.

```text
1cmVfZXJyb3IYBSABKAsyHi5jaGVzc2NvbS5jZWFjLnYyLkZhaWx1cmVFcnJvcjoHgqYdAwoBAUIHCgVlcnJvcmIGcHJvdG8z","chesscom/ceac/v2/run_search.proto":"CiFjaGVzc2NvbS9jZWFjL3YyL3J1bl9zZWFyY2gucHJvdG8SEGNoZXNzY29tLmNlYWMudjIi4wIKEFJ1blNlYXJjaFJlcXVlc3QSRAoMbmV3X2dhbWVfcmVxGAEgASgLMi4uY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLk5ld0dhbWVSZXF1ZXN0EkgKDnJ1bl9zZWFyY2hfcmVxGAIgASgLMjAuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLlJ1blNlYXJjaFJl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17729"></a>
## FND-17729: Full frontend descriptor: chesscom/shared_board/v1alpha/shared_board.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/shared_board/v1alpha/shared_board.proto",
  "package": "chesscom.shared_board.v1alpha",
  "message_type": [
    {
      "name": "SharedBoard",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "session_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "flipped",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "initial_position",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "pgn",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "line",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "move",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "squares",
          "number": 9,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSquareHighlight"
        },
        {
          "name": "arrows",
          "number": 10,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardArrow"
        },
        {
          "name": "images",
          "number": 11,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardImageMarking"
        },
        {
          "name": "draft",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "version",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "sequence",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "created_at",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "updated_at",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "source",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSource"
        },
        {
          "name": "hide_engine_lines",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "hide_move_list",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ]
    },
    {
      "name": "SharedBoardSource",
      "field": [
        {
          "name": "event_game",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardEventGameSource",
          "oneof_index": 0
        },
        {
          "name": "analysis_game",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardAnalysisGameSource",
          "oneof_index": 0
        }
      ],
      "oneof_decl": [
        {
          "name": "source"
        }
      ]
    },
    {
      "name": "SharedBoardEventGameSource",
      "field": [
        {
          "name": "event_slug",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "round_slug",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "game_slug",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "game_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "SharedBoardAnalysisGameSource",
      "field": [
        {
          "name": "library_game",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardAnalysisLibraryGameSource",
          "oneof_index": 0
        },
        {
          "name": "chesscom_game",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardAnalysisChesscomGameSource",
          "oneof_index": 0
        }
      ],
      "oneof_decl": [
        {
          "name": "game"
        }
      ]
    },
    {
      "name": "SharedBoardAnalysisLibraryGameSource",
      "field": [
        {
          "name": "library_user_collection_game_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "collection_slug",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "library_item_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "collection_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "SharedBoardAnalysisChesscomGameSource",
      "field": [
        {
          "name": "game_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardAnalysisGameType"
        },
        {
          "name": "game_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "game_uuid",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "SharedBoardSquareHighlight",
      "field": [
        {
          "name": "key_modifier",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardKeyModifier"
        },
        {
          "name": "square",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        }
      ]
    },
    {
      "name": "SharedBoardArrow",
      "field": [
        {
          "name": "key_modifier",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardKeyModifier"
        },
        {
          "name": "from",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "to",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        }
      ]
    },
    {
      "name": "SharedBoardImageMarking",
      "field": [
        {
          "name": "type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "square",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "SharedBoardAnalysisGameType",
      "value": [
        {
          "name": "SHARED_BOARD_ANALYSIS_GAME_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SHARED_BOARD_ANALYSIS_GAME_TYPE_DAILY",
          "number": 1
        },
        {
          "name": "SHARED_BOARD_ANALYSIS_GAME_TYPE_LIVE",
          "number": 2
        },
        {
          "name": "SHARED_BOARD_ANALYSIS_GAME_TYPE_MASTER",
          "number": 3
        },
        {
          "name": "SHARED_BOARD_ANALYSIS_GAME_TYPE_PGN",
          "number": 4
        },
        {
          "name": "SHARED_BOARD_ANALYSIS_GAME_TYPE_OTB",
          "number": 5
        },
        {
          "name": "SHARED_BOARD_ANALYSIS_GAME_TYPE_COACH",
          "number": 6
        },
        {
          "name": "SHARED_BOARD_ANALYSIS_GAME_TYPE_COMPUTER",
          "number": 7
        }
      ]
    },
    {
      "name": "SharedBoardKeyModifier",
      "value": [
        {
          "name": "SHARED_BOARD_KEY_MODIFIER_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SHARED_BOARD_KEY_MODIFIER_NONE",
          "number": 1
        },
        {
          "name": "SHARED_BOARD_KEY_MODIFIER_SHIFT",
          "number": 2
        },
        {
          "name": "SHARED_BOARD_KEY_MODIFIER_CTRL",
          "number": 3
        },
        {
          "name": "SHARED_BOARD_KEY_MODIFIER_ALT",
          "number": 4
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 287075.

```text
BI1Cg1mYWlsdXJlX2Vycm9yGAUgASgLMh4uY2hlc3Njb20uY2VhYy52Mi5GYWlsdXJlRXJyb3JCBwoFZXJyb3JiBnByb3RvMw","chesscom/shared_board/v1alpha/shared_board.proto":"CjBjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmQucHJvdG8SHWNoZXNzY29tLnNoYXJlZF9ib2FyZC52MWFscGhhIu4ECgtTaGFyZWRCb2FyZBIKCgJpZBgBIAEoCRISCgpzZXNzaW9uX2lkGAIgASgJEg8KB3VzZXJfaWQYAyABKAkSDwoHZmxpcHBlZBgEIAEoCBIYChBpbml0aWFsX3Bvc2l0aW9uGAUgASgJEgsKA3BnbhgGIAEoC
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17730"></a>
## FND-17730: Full frontend descriptor: chesscom/shared_board/v1alpha/shared_board_clock.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/shared_board/v1alpha/shared_board_clock.proto",
  "package": "chesscom.shared_board.v1alpha",
  "message_type": [
    {
      "name": "SharedBoardClock",
      "field": [
        {
          "name": "type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardClockType"
        },
        {
          "name": "timer",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardClockValue"
        },
        {
          "name": "stopwatch",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardClockValue"
        },
        {
          "name": "created_at",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        }
      ]
    },
    {
      "name": "SharedBoardClockValue",
      "field": [
        {
          "name": "duration",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Duration"
        },
        {
          "name": "state",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardClockState"
        },
        {
          "name": "updated_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "SharedBoardClockType",
      "value": [
        {
          "name": "SHARED_BOARD_CLOCK_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SHARED_BOARD_CLOCK_TYPE_CURRENT_TIME",
          "number": 1
        },
        {
          "name": "SHARED_BOARD_CLOCK_TYPE_SESSION_TIME",
          "number": 2
        },
        {
          "name": "SHARED_BOARD_CLOCK_TYPE_TIMER",
          "number": 3
        },
        {
          "name": "SHARED_BOARD_CLOCK_TYPE_STOPWATCH",
          "number": 4
        }
      ]
    },
    {
      "name": "SharedBoardClockState",
      "value": [
        {
          "name": "SHARED_BOARD_CLOCK_STATE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SHARED_BOARD_CLOCK_STATE_ENDED",
          "number": 1
        },
        {
          "name": "SHARED_BOARD_CLOCK_STATE_STARTED",
          "number": 2
        },
        {
          "name": "SHARED_BOARD_CLOCK_STATE_STOPPED",
          "number": 3
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 290575.

```text
VJFRF9CT0FSRF9LRVlfTU9ESUZJRVJfQ1RSTBADEiEKHVNIQVJFRF9CT0FSRF9LRVlfTU9ESUZJRVJfQUxUEARiBnByb3RvMw","chesscom/shared_board/v1alpha/shared_board_clock.proto":"CjZjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfY2xvY2sucHJvdG8SHWNoZXNzY29tLnNoYXJlZF9ib2FyZC52MWFscGhhIpMCChBTaGFyZWRCb2FyZENsb2NrEkEKBHR5cGUYASABKA4yMy5jaGVzc2NvbS5zaGFyZWRfYm9hcmQudjFhbHBoYS5TaGFyZWRCb2FyZENsb2NrVHlwZRJDCgV0aW1lchgCIAEoCzI0LmNoZXN
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17731"></a>
## FND-17731: Full frontend descriptor: chesscom/shared_board/v1alpha/shared_board_participant.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/shared_board/v1alpha/shared_board_participant.proto",
  "package": "chesscom.shared_board.v1alpha",
  "message_type": [
    {
      "name": "SharedBoardParticipant",
      "field": [
        {
          "name": "user_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "role",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardRole"
        },
        {
          "name": "status",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardParticipantStatus"
        },
        {
          "name": "capabilities",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardCapability"
        },
        {
          "name": "invited_by_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "created_at",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "updated_at",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "username",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "avatar_url",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "chess_title",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "country",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "flair_code",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "is_streamer",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "flair",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.flair.v1.FlairView",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "membership",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 7,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_username"
        },
        {
          "name": "_avatar_url"
        },
        {
          "name": "_chess_title"
        },
        {
          "name": "_country"
        },
        {
          "name": "_flair_code"
        },
        {
          "name": "_is_streamer"
        },
        {
          "name": "_flair"
        },
        {
          "name": "_membership"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "SharedBoardRole",
      "value": [
        {
          "name": "SHARED_BOARD_ROLE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SHARED_BOARD_ROLE_HOST",
          "number": 1
        },
        {
          "name": "SHARED_BOARD_ROLE_CO_HOST",
          "number": 2
        },
        {
          "name": "SHARED_BOARD_ROLE_VIEWER",
          "number": 3
        }
      ]
    },
    {
      "name": "SharedBoardParticipantStatus",
      "value": [
        {
          "name": "SHARED_BOARD_PARTICIPANT_STATUS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SHARED_BOARD_PARTICIPANT_STATUS_PENDING",
          "number": 1
        },
        {
          "name": "SHARED_BOARD_PARTICIPANT_STATUS_REQUESTING",
          "number": 2
        },
        {
          "name": "SHARED_BOARD_PARTICIPANT_STATUS_ACCEPTED",
          "number": 3
        },
        {
          "name": "SHARED_BOARD_PARTICIPANT_STATUS_DECLINED",
          "number": 4
        }
      ]
    },
    {
      "name": "SharedBoardCapability",
      "value": [
        {
          "name": "SHARED_BOARD_CAPABILITY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SHARED_BOARD_CAPABILITY_MOVE_WHITE",
          "number": 1
        },
        {
          "name": "SHARED_BOARD_CAPABILITY_MOVE_BLACK",
          "number": 2
        },
        {
          "name": "SHARED_BOARD_CAPABILITY_DRAW_ARROWS",
          "number": 3
        },
        {
          "name": "SHARED_BOARD_CAPABILITY_EDIT_COLLECTION",
          "number": 4
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 291922.

```text
JPQVJEX0NMT0NLX1NUQVRFX1NUQVJURUQQAhIkCiBTSEFSRURfQk9BUkRfQ0xPQ0tfU1RBVEVfU1RPUFBFRBADYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_participant.proto":"CjxjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfcGFydGljaXBhbnQucHJvdG8SHWNoZXNzY29tLnNoYXJlZF9ib2FyZC52MWFscGhhIsUFChZTaGFyZWRCb2FyZFBhcnRpY2lwYW50Eg8KB3VzZXJfaWQYASABKAkSPAoEcm9sZRgCIAEoDjIuLmNoZXNzY29tLnNoYXJlZF9ib2FyZC52MWFscGhhLlNoYXJlZEJvY
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17732"></a>
## FND-17732: Full frontend descriptor: chesscom/shared_board/v1alpha/shared_board_session_resource.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/shared_board/v1alpha/shared_board_session_resource.proto",
  "package": "chesscom.shared_board.v1alpha",
  "message_type": [
    {
      "name": "SharedBoardSessionResource",
      "field": [
        {
          "name": "resource_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "resource_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 293931.

```text
JJTElUWV9EUkFXX0FSUk9XUxADEisKJ1NIQVJFRF9CT0FSRF9DQVBBQklMSVRZX0VESVRfQ09MTEVDVElPThAEYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_session_resource.proto":"CkFjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfc2Vzc2lvbl9yZXNvdXJjZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEiSAoaU2hhcmVkQm9hcmRTZXNzaW9uUmVzb3VyY2USFQoNcmVzb3VyY2VfdHlwZRgBIAEoCRITCgtyZXNvdXJjZV9pZBgCIAEoCWIGcHJvdG8z","chesscom/
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17733"></a>
## FND-17733: Full frontend descriptor: chesscom/shared_board/v1alpha/shared_board_session.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/shared_board/v1alpha/shared_board_session.proto",
  "package": "chesscom.shared_board.v1alpha",
  "message_type": [
    {
      "name": "SharedBoardSessionId",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        },
        {
          "name": "slug",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        }
      ],
      "oneof_decl": [
        {
          "name": "id"
        }
      ]
    },
    {
      "name": "SharedBoardSession",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "current_board_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "boards",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoard"
        },
        {
          "name": "created_at",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "slug",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "participants",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardParticipant"
        },
        {
          "name": "open_enrollment",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "status",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSessionStatus"
        },
        {
          "name": "clock",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardClock"
        },
        {
          "name": "source",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSessionSource"
        },
        {
          "name": "linked_resource",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSessionResource"
        }
      ]
    },
    {
      "name": "SharedBoardSessionSummary",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "slug",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "source",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSessionSource"
        },
        {
          "name": "open_enrollment",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "status",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSessionStatus"
        },
        {
          "name": "role",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardRole"
        },
        {
          "name": "participant_status",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardParticipantStatus"
        },
        {
          "name": "created_at",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "updated_at",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "SharedBoardSessionStatus",
      "value": [
        {
          "name": "SHARED_BOARD_SESSION_STATUS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SHARED_BOARD_SESSION_STATUS_ACTIVE",
          "number": 1
        },
        {
          "name": "SHARED_BOARD_SESSION_STATUS_ENDED",
          "number": 2
        }
      ]
    },
    {
      "name": "SharedBoardSessionSource",
      "value": [
        {
          "name": "SHARED_BOARD_SESSION_SOURCE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SHARED_BOARD_SESSION_SOURCE_ANALYSIS",
          "number": 1
        },
        {
          "name": "SHARED_BOARD_SESSION_SOURCE_EVENTS",
          "number": 2
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 294242.

```text
kQm9hcmRTZXNzaW9uUmVzb3VyY2USFQoNcmVzb3VyY2VfdHlwZRgBIAEoCRITCgtyZXNvdXJjZV9pZBgCIAEoCWIGcHJvdG8z","chesscom/shared_board/v1alpha/shared_board_session.proto":"CjhjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfc2Vzc2lvbi5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEiQgoUU2hhcmVkQm9hcmRTZXNzaW9uSWQSFAoKc2Vzc2lvbl9pZBgBIAEoCUgAEg4KBHNsdWcYAiABKAlIAEIECgJpZCLABAoSU2hhcmVkQm9hcmRTZXNzaW9uEgoKAmlkGAEgASgJEhgKE
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17734"></a>
## FND-17734: Full frontend descriptor: chesscom/shared_board/v1alpha/shared_board_updated_notification.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/shared_board/v1alpha/shared_board_updated_notification.proto",
  "package": "chesscom.shared_board.v1alpha",
  "message_type": [
    {
      "name": "SharedBoardUpdatedNotification",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "author_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "board",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoard"
        },
        {
          "name": "update_type",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardUpdateType"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "SharedBoardUpdateType",
      "value": [
        {
          "name": "SHARED_BOARD_UPDATE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SHARED_BOARD_UPDATE_TYPE_CREATED",
          "number": 1
        },
        {
          "name": "SHARED_BOARD_UPDATE_TYPE_UPDATED",
          "number": 2
        },
        {
          "name": "SHARED_BOARD_UPDATE_TYPE_DELETED",
          "number": 3
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 296340.

```text
TRVNTSU9OX1NPVVJDRV9BTkFMWVNJUxABEiYKIlNIQVJFRF9CT0FSRF9TRVNTSU9OX1NPVVJDRV9FVkVOVFMQAmIGcHJvdG8z","chesscom/shared_board/v1alpha/shared_board_updated_notification.proto":"CkVjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfdXBkYXRlZF9ub3RpZmljYXRpb24ucHJvdG8SHWNoZXNzY29tLnNoYXJlZF9ib2FyZC52MWFscGhhIs0BCh5TaGFyZWRCb2FyZFVwZGF0ZWROb3RpZmljYXRpb24SEgoKc2Vzc2lvbl9pZBgBIAEoCRIRCglhdXRob3JfaWQYAiABKAkSOQoFYm9hcmQY
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17735"></a>
## FND-17735: Full frontend descriptor: chesscom/shared_board/v1alpha/shared_board_participant_updated_notification.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/shared_board/v1alpha/shared_board_participant_updated_notification.proto",
  "package": "chesscom.shared_board.v1alpha",
  "message_type": [
    {
      "name": "SharedBoardParticipantUpdatedNotification",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "participant",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardParticipant"
        },
        {
          "name": "removed",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "author_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 297082.

```text
JPQVJEX1VQREFURV9UWVBFX1VQREFURUQQAhIkCiBTSEFSRURfQk9BUkRfVVBEQVRFX1RZUEVfREVMRVRFRBADYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_participant_updated_notification.proto":"ClFjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfcGFydGljaXBhbnRfdXBkYXRlZF9ub3RpZmljYXRpb24ucHJvdG8SHWNoZXNzY29tLnNoYXJlZF9ib2FyZC52MWFscGhhIq8BCilTaGFyZWRCb2FyZFBhcnRpY2lwYW50VXBkYXRlZE5vdGlmaWNhdGlvbhISCgpzZXNzaW9uX2lkGAEg
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17736"></a>
## FND-17736: Full frontend descriptor: chesscom/shared_board/v1alpha/shared_board_session_updated_notification.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/shared_board/v1alpha/shared_board_session_updated_notification.proto",
  "package": "chesscom.shared_board.v1alpha",
  "message_type": [
    {
      "name": "SharedBoardSessionUpdatedNotification",
      "field": [
        {
          "name": "session",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSession"
        },
        {
          "name": "author_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 297569.

```text
xYWxwaGEuU2hhcmVkQm9hcmRQYXJ0aWNpcGFudBIPCgdyZW1vdmVkGAMgASgIEhEKCWF1dGhvcl9pZBgEIAEoCWIGcHJvdG8z","chesscom/shared_board/v1alpha/shared_board_session_updated_notification.proto":"Ck1jaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfc2Vzc2lvbl91cGRhdGVkX25vdGlmaWNhdGlvbi5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEifgolU2hhcmVkQm9hcmRTZXNzaW9uVXBkYXRlZE5vdGlmaWNhdGlvbhJCCgdzZXNzaW9uGAEgASgLMjEuY2hlc3Njb20u
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17737"></a>
## FND-17737: Full frontend descriptor: chesscom/shared_board/v1alpha/shared_board_session_ended_notification.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/shared_board/v1alpha/shared_board_session_ended_notification.proto",
  "package": "chesscom.shared_board.v1alpha",
  "message_type": [
    {
      "name": "SharedBoardSessionEndedNotification",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "author_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 297980.

```text
lc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEuU2hhcmVkQm9hcmRTZXNzaW9uEhEKCWF1dGhvcl9pZBgCIAEoCWIGcHJvdG8z","chesscom/shared_board/v1alpha/shared_board_session_ended_notification.proto":"CktjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfc2Vzc2lvbl9lbmRlZF9ub3RpZmljYXRpb24ucHJvdG8SHWNoZXNzY29tLnNoYXJlZF9ib2FyZC52MWFscGhhIkwKI1NoYXJlZEJvYXJkU2Vzc2lvbkVuZGVkTm90aWZpY2F0aW9uEhIKCnNlc3Npb25faWQYASABKAkSEQoJYXV0aG9yX2lkGA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17738"></a>
## FND-17738: Full frontend descriptor: chesscom/shared_board/v1alpha/shared_board_participant_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/shared_board/v1alpha/shared_board_participant_service.proto",
  "package": "chesscom.shared_board.v1alpha",
  "message_type": [
    {
      "name": "InviteSharedBoardParticipantRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "role",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardRole"
        },
        {
          "name": "capabilities",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardCapability"
        }
      ]
    },
    {
      "name": "InviteSharedBoardParticipantResponse",
      "field": [
        {
          "name": "participant",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardParticipant"
        }
      ]
    },
    {
      "name": "RequestToJoinSharedBoardSessionRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSessionId"
        }
      ]
    },
    {
      "name": "RequestToJoinSharedBoardSessionResponse",
      "field": [
        {
          "name": "participant",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardParticipant"
        },
        {
          "name": "session_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "RespondToSharedBoardInvitationRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "accept",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ]
    },
    {
      "name": "RespondToSharedBoardInvitationResponse",
      "field": [
        {
          "name": "participant",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardParticipant"
        }
      ]
    },
    {
      "name": "RespondToSharedBoardJoinRequestRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "accept",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ]
    },
    {
      "name": "RespondToSharedBoardJoinRequestResponse",
      "field": [
        {
          "name": "participant",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardParticipant"
        }
      ]
    },
    {
      "name": "UpdateSharedBoardParticipantRoleRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "role",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardRole"
        }
      ]
    },
    {
      "name": "UpdateSharedBoardParticipantRoleResponse",
      "field": [
        {
          "name": "participant",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardParticipant"
        }
      ]
    },
    {
      "name": "SetSharedBoardParticipantCapabilitiesRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "capabilities",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardCapability"
        }
      ]
    },
    {
      "name": "SetSharedBoardParticipantCapabilitiesResponse",
      "field": [
        {
          "name": "participant",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardParticipant"
        }
      ]
    },
    {
      "name": "TransferSharedBoardHostRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "TransferSharedBoardHostResponse",
      "field": [
        {
          "name": "session",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSession"
        }
      ]
    },
    {
      "name": "RemoveSharedBoardParticipantRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "RemoveSharedBoardParticipantResponse",
      "field": [
        {
          "name": "session",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSession"
        }
      ]
    },
    {
      "name": "LeaveSharedBoardSessionRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "LeaveSharedBoardSessionResponse",
      "field": [
        {
          "name": "session",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSession"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "SharedBoardSessionParticipantService",
      "method": [
        {
          "name": "InviteSharedBoardParticipant",
          "input_type": ".chesscom.shared_board.v1alpha.InviteSharedBoardParticipantRequest",
          "output_type": ".chesscom.shared_board.v1alpha.InviteSharedBoardParticipantResponse"
        },
        {
          "name": "RequestToJoinSharedBoardSession",
          "input_type": ".chesscom.shared_board.v1alpha.RequestToJoinSharedBoardSessionRequest",
          "output_type": ".chesscom.shared_board.v1alpha.RequestToJoinSharedBoardSessionResponse"
        },
        {
          "name": "RespondToSharedBoardInvitation",
          "input_type": ".chesscom.shared_board.v1alpha.RespondToSharedBoardInvitationRequest",
          "output_type": ".chesscom.shared_board.v1alpha.RespondToSharedBoardInvitationResponse"
        },
        {
          "name": "RespondToSharedBoardJoinRequest",
          "input_type": ".chesscom.shared_board.v1alpha.RespondToSharedBoardJoinRequestRequest",
          "output_type": ".chesscom.shared_board.v1alpha.RespondToSharedBoardJoinRequestResponse"
        },
        {
          "name": "UpdateSharedBoardParticipantRole",
          "input_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardParticipantRoleRequest",
          "output_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardParticipantRoleResponse"
        },
        {
          "name": "SetSharedBoardParticipantCapabilities",
          "input_type": ".chesscom.shared_board.v1alpha.SetSharedBoardParticipantCapabilitiesRequest",
          "output_type": ".chesscom.shared_board.v1alpha.SetSharedBoardParticipantCapabilitiesResponse"
        },
        {
          "name": "TransferSharedBoardHost",
          "input_type": ".chesscom.shared_board.v1alpha.TransferSharedBoardHostRequest",
          "output_type": ".chesscom.shared_board.v1alpha.TransferSharedBoardHostResponse"
        },
        {
          "name": "RemoveSharedBoardParticipant",
          "input_type": ".chesscom.shared_board.v1alpha.RemoveSharedBoardParticipantRequest",
          "output_type": ".chesscom.shared_board.v1alpha.RemoveSharedBoardParticipantResponse"
        },
        {
          "name": "LeaveSharedBoardSession",
          "input_type": ".chesscom.shared_board.v1alpha.LeaveSharedBoardSessionRequest",
          "output_type": ".chesscom.shared_board.v1alpha.LeaveSharedBoardSessionResponse"
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 298320.

```text
JkU2Vzc2lvbkVuZGVkTm90aWZpY2F0aW9uEhIKCnNlc3Npb25faWQYASABKAkSEQoJYXV0aG9yX2lkGAIgASgJYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_participant_service.proto":"CkRjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfcGFydGljaXBhbnRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEi1AEKI0ludml0ZVNoYXJlZEJvYXJkUGFydGljaXBhbnRSZXF1ZXN0EhIKCnNlc3Npb25faWQYASABKAkSDwoHdXNlcl9pZBgCIAEoCRI8CgRyb2xlG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17748"></a>
## FND-17748: Full frontend descriptor: chesscom/shared_board/v1alpha/shared_board_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/shared_board/v1alpha/shared_board_service.proto",
  "package": "chesscom.shared_board.v1alpha",
  "message_type": [
    {
      "name": "CreateSharedBoardSessionRequest",
      "field": [
        {
          "name": "boards",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoard"
        },
        {
          "name": "open_enrollment",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "source",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSessionSource"
        }
      ]
    },
    {
      "name": "CreateSharedBoardSessionResponse",
      "field": [
        {
          "name": "session",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSession"
        }
      ]
    },
    {
      "name": "GetSharedBoardSessionRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSessionId"
        }
      ]
    },
    {
      "name": "GetSharedBoardSessionResponse",
      "field": [
        {
          "name": "session",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSession"
        }
      ]
    },
    {
      "name": "FindSharedBoardSessionByResourceRequest",
      "field": [
        {
          "name": "resource",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSessionResource"
        }
      ]
    },
    {
      "name": "FindSharedBoardSessionByResourceResponse",
      "field": [
        {
          "name": "session",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSession"
        }
      ]
    },
    {
      "name": "CreateSharedBoardSessionForResourceRequest",
      "field": [
        {
          "name": "resource",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSessionResource"
        },
        {
          "name": "boards",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoard"
        },
        {
          "name": "open_enrollment",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "source",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSessionSource"
        }
      ]
    },
    {
      "name": "CreateSharedBoardSessionForResourceResponse",
      "field": [
        {
          "name": "session",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSession"
        }
      ]
    },
    {
      "name": "SyncCollectionRosterRequest",
      "field": [
        {
          "name": "resource",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSessionResource"
        }
      ]
    },
    {
      "name": "SyncCollectionRosterResponse",
      "field": [
        {
          "name": "session",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSession"
        }
      ]
    },
    {
      "name": "ListSharedBoardSessionsRequest",
      "field": [
        {
          "name": "source",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSessionSource"
        },
        {
          "name": "pagination",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.RequestPagination",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "role",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardRole"
        },
        {
          "name": "participant_status",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardParticipantStatus"
        }
      ],
      "oneof_decl": [
        {
          "name": "_pagination"
        }
      ]
    },
    {
      "name": "ListSharedBoardSessionsResponse",
      "field": [
        {
          "name": "sessions",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSessionSummary"
        },
        {
          "name": "pagination",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.ResponsePagination",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_pagination"
        }
      ]
    },
    {
      "name": "UpdateSharedBoardSessionRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "current_board_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "open_enrollment",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ]
    },
    {
      "name": "UpdateSharedBoardSessionResponse",
      "field": [
        {
          "name": "session",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSession"
        }
      ]
    },
    {
      "name": "UpdateSharedBoardClockRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "clock",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardClock"
        }
      ]
    },
    {
      "name": "UpdateSharedBoardClockResponse",
      "field": [
        {
          "name": "session",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSession"
        }
      ]
    },
    {
      "name": "CreateSharedBoardRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "board",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoard"
        }
      ]
    },
    {
      "name": "CreateSharedBoardResponse",
      "field": [
        {
          "name": "board",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoard"
        }
      ]
    },
    {
      "name": "DeleteSharedBoardRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "board_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "DeleteSharedBoardResponse",
      "field": [
        {
          "name": "session",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSession"
        }
      ]
    },
    {
      "name": "UpdateSharedBoardRequest",
      "field": [
        {
          "name": "board",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoard"
        }
      ]
    },
    {
      "name": "UpdateSharedBoardResponse",
      "field": [
        {
          "name": "board",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoard"
        }
      ]
    },
    {
      "name": "EndSharedBoardSessionRequest",
      "field": [
        {
          "name": "session_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "EndSharedBoardSessionResponse",
      "field": [
        {
          "name": "session",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.shared_board.v1alpha.SharedBoardSession"
        }
      ]
    }
  ],
  "service": [
    {
      "name": "SharedBoardService",
      "method": [
        {
          "name": "GetSharedBoardSession",
          "input_type": ".chesscom.shared_board.v1alpha.GetSharedBoardSessionRequest",
          "output_type": ".chesscom.shared_board.v1alpha.GetSharedBoardSessionResponse"
        },
        {
          "name": "FindSharedBoardSessionByResource",
          "input_type": ".chesscom.shared_board.v1alpha.FindSharedBoardSessionByResourceRequest",
          "output_type": ".chesscom.shared_board.v1alpha.FindSharedBoardSessionByResourceResponse"
        },
        {
          "name": "ListSharedBoardSessions",
          "input_type": ".chesscom.shared_board.v1alpha.ListSharedBoardSessionsRequest",
          "output_type": ".chesscom.shared_board.v1alpha.ListSharedBoardSessionsResponse"
        },
        {
          "name": "CreateSharedBoardSession",
          "input_type": ".chesscom.shared_board.v1alpha.CreateSharedBoardSessionRequest",
          "output_type": ".chesscom.shared_board.v1alpha.CreateSharedBoardSessionResponse"
        },
        {
          "name": "CreateSharedBoardSessionForResource",
          "input_type": ".chesscom.shared_board.v1alpha.CreateSharedBoardSessionForResourceRequest",
          "output_type": ".chesscom.shared_board.v1alpha.CreateSharedBoardSessionForResourceResponse"
        },
        {
          "name": "SyncCollectionRoster",
          "input_type": ".chesscom.shared_board.v1alpha.SyncCollectionRosterRequest",
          "output_type": ".chesscom.shared_board.v1alpha.SyncCollectionRosterResponse",
          "options": {
            "idempotency_level": "IDEMPOTENT"
          }
        },
        {
          "name": "UpdateSharedBoardSession",
          "input_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardSessionRequest",
          "output_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardSessionResponse"
        },
        {
          "name": "UpdateSharedBoardClock",
          "input_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardClockRequest",
          "output_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardClockResponse"
        },
        {
          "name": "CreateSharedBoard",
          "input_type": ".chesscom.shared_board.v1alpha.CreateSharedBoardRequest",
          "output_type": ".chesscom.shared_board.v1alpha.CreateSharedBoardResponse"
        },
        {
          "name": "DeleteSharedBoard",
          "input_type": ".chesscom.shared_board.v1alpha.DeleteSharedBoardRequest",
          "output_type": ".chesscom.shared_board.v1alpha.DeleteSharedBoardResponse"
        },
        {
          "name": "UpdateSharedBoard",
          "input_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardRequest",
          "output_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardResponse"
        },
        {
          "name": "EndSharedBoardSession",
          "input_type": ".chesscom.shared_board.v1alpha.EndSharedBoardSessionRequest",
          "output_type": ".chesscom.shared_board.v1alpha.EndSharedBoardSessionResponse"
        }
      ]
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 303501.

```text
Jlc3BvbnNlQjfKtywzChkvc2VydmljZS9zaGFyZWQtYm9hcmQvcnBjEgAaEBIOeC1zZXNzaW9uLXVzZXIiAggBYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_service.proto":"CjhjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEivwEKH0NyZWF0ZVNoYXJlZEJvYXJkU2Vzc2lvblJlcXVlc3QSOgoGYm9hcmRzGAEgAygLMiouY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEuU2hhcmVkQm9hcmQSFwoPb3Blbl9lb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17761"></a>
## FND-17761: Full frontend descriptor: chesscom/gameplay/v1/game_ref.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/gameplay/v1/game_ref.proto",
  "package": "chesscom.gameplay.v1",
  "message_type": [
    {
      "name": "GameRef",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "numeric_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "variant",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Variant",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "timeclass",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.TimeClass",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "source",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.gameplay.v1.GameSource",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "is_private",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "legacy_id",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "oneof_index": 6,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_id"
        },
        {
          "name": "_numeric_id"
        },
        {
          "name": "_variant"
        },
        {
          "name": "_timeclass"
        },
        {
          "name": "_source"
        },
        {
          "name": "_is_private"
        },
        {
          "name": "_legacy_id"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "GameSource",
      "value": [
        {
          "name": "GAME_SOURCE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_SOURCE_RCN",
          "number": 1
        },
        {
          "name": "GAME_SOURCE_LC",
          "number": 2
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 310247.

```text
SZXNwb25zZUI3yrcsMwoZL3NlcnZpY2Uvc2hhcmVkLWJvYXJkL3JwYxIAGhASDngtc2Vzc2lvbi11c2VyIgIIAWIGcHJvdG8z","chesscom/gameplay/v1/game_ref.proto":"CiNjaGVzc2NvbS9nYW1lcGxheS92MS9nYW1lX3JlZi5wcm90bxIUY2hlc3Njb20uZ2FtZXBsYXkudjEi5QIKB0dhbWVSZWYSDwoCaWQYASABKAlIAIgBARIXCgpudW1lcmljX2lkGAIgASgDSAGIAQESMAoHdmFyaWFudBgDIAEoDjIaLmNoZXNzY29tLmNoZXNzLnYxLlZhcmlhbnRIAogBARI0Cgl0aW1lY2xhc3MYBCABKA4yHC5jaGVzc2NvbS5jaGVzcy52MS5UaW1lQ2xhc3
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17762"></a>
## FND-17762: Full frontend descriptor: chesscom/gameplay/v1/battle_ref.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/gameplay/v1/battle_ref.proto",
  "package": "chesscom.gameplay.v1",
  "message_type": [
    {
      "name": "BattleRef",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_id"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 310983.

```text
9VTlNQRUNJRklFRBAAEhMKD0dBTUVfU09VUkNFX1JDThABEhIKDkdBTUVfU09VUkNFX0xDEAIaCIqmHQQKAgECYgZwcm90bzM","chesscom/gameplay/v1/battle_ref.proto":"CiVjaGVzc2NvbS9nYW1lcGxheS92MS9iYXR0bGVfcmVmLnByb3RvEhRjaGVzc2NvbS5nYW1lcGxheS52MSItCglCYXR0bGVSZWYSDwoCaWQYASABKAlIAIgBAToIgqYdBAoCAQJCBQoDX2lkYgZwcm90bzM","chesscom/themes/v2/core.proto":"Ch1jaGVzc2NvbS90aGVtZXMvdjIvY29yZS5wcm90bxISY2hlc3Njb20udGhlbWVzLnYyIpgDCgVUaGVtZRIKCgJpZB
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17763"></a>
## FND-17763: Full frontend descriptor: chesscom/themes/v2/core.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/themes/v2/core.proto",
  "package": "chesscom.themes.v2",
  "message_type": [
    {
      "name": "Theme",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "is_default",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "legacy_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "localized_name",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "display_priority",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "onboarding",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "background",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.Background"
        },
        {
          "name": "board_style",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.BoardStyle"
        },
        {
          "name": "piece_set",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.PieceSet"
        },
        {
          "name": "sound_set",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.SoundSet"
        },
        {
          "name": "is_accessibility_friendly",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_legacy_id"
        }
      ]
    },
    {
      "name": "PresetTheme",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "attributes",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.Attributes"
        },
        {
          "name": "element_ids",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.ThemeElementIds"
        },
        {
          "name": "onboarding",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "is_accessibility_friendly",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "Background",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "is_default",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "legacy_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "localized_name",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "display_priority",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "supported_platforms",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.api.v1.Platform"
        },
        {
          "name": "unlockable_preview",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.unlockables.v1.UnlockablePreview"
        },
        {
          "name": "preview_image",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "image",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.Background.ImageStyle",
          "oneof_index": 0
        },
        {
          "name": "color",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.Background.PlainColorStyle",
          "oneof_index": 0
        }
      ],
      "nested_type": [
        {
          "name": "ImageStyle",
          "field": [
            {
              "name": "url",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "fallback_color",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.themes.v2.Background.PlainColorStyle",
              "oneof_index": 0,
              "proto3_optional": true
            }
          ],
          "oneof_decl": [
            {
              "name": "_fallback_color"
            }
          ]
        },
        {
          "name": "PlainColorStyle",
          "field": [
            {
              "name": "hex_code",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            }
          ]
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "style"
        },
        {
          "name": "_legacy_id"
        }
      ]
    },
    {
      "name": "BoardStyle",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "is_default",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "legacy_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "localized_name",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "display_priority",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "supported_platforms",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.api.v1.Platform"
        },
        {
          "name": "unlockable_preview",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.unlockables.v1.UnlockablePreview"
        },
        {
          "name": "preview_image",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.BoardStyle.PreviewImage"
        },
        {
          "name": "image",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "image_3d",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.BoardStyle.ThreeDimensionalImage"
        },
        {
          "name": "coordinate_color_dark",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "coordinate_color_light",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "highlight_color",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "category_id",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "nested_type": [
        {
          "name": "PreviewImage",
          "field": [
            {
              "name": "square",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "linear",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            }
          ]
        },
        {
          "name": "ThreeDimensionalImage",
          "field": [
            {
              "name": "board",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "coordinates",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            }
          ]
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_legacy_id"
        }
      ]
    },
    {
      "name": "PieceSet",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "is_default",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "legacy_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "localized_name",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "display_priority",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "supported_platforms",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.api.v1.Platform"
        },
        {
          "name": "unlockable_preview",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.unlockables.v1.UnlockablePreview"
        },
        {
          "name": "preview_image",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.PieceSet.PreviewImage"
        },
        {
          "name": "images",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.PieceSet.Images"
        },
        {
          "name": "perspective",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.themes.v2.PieceSet.PiecePerspective"
        },
        {
          "name": "category_id",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "nested_type": [
        {
          "name": "PreviewImage",
          "field": [
            {
              "name": "square",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "linear",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            }
          ]
        },
        {
          "name": "Images",
          "field": [
            {
              "name": "white_pawn",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "white_knight",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "white_bishop",
              "number": 3,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "white_rook",
              "number": 4,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "white_queen",
              "number": 5,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "white_king",
              "number": 6,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "black_pawn",
              "number": 7,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "black_knight",
              "number": 8,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "black_bishop",
              "number": 9,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "black_rook",
              "number": 10,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "black_queen",
              "number": 11,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "black_king",
              "number": 12,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            }
          ]
        }
      ],
      "enum_type": [
        {
          "name": "PiecePerspective",
          "value": [
            {
              "name": "PIECE_PERSPECTIVE_UNSPECIFIED",
              "number": 0
            },
            {
              "name": "PIECE_PERSPECTIVE_TOP_DOWN",
              "number": 1
            },
            {
              "name": "PIECE_PERSPECTIVE_PSEUDO_3D",
              "number": 2
            },
            {
              "name": "PIECE_PERSPECTIVE_REAL_3D",
              "number": 3
            }
          ]
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_legacy_id"
        }
      ]
    },
    {
      "name": "SoundSet",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "is_default",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "legacy_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "localized_name",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "display_priority",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "supported_platforms",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.api.v1.Platform"
        },
        {
          "name": "unlockable_preview",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.unlockables.v1.UnlockablePreview"
        },
        {
          "name": "sound_archives",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.SoundSet.SoundArchives",
          "oneof_index": 0
        },
        {
          "name": "sound_files",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.SoundSet.SoundFiles",
          "oneof_index": 0
        },
        {
          "name": "category_id",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "nested_type": [
        {
          "name": "SoundArchives",
          "field": [
            {
              "name": "mp3",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "ogg",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "wav",
              "number": 3,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "webm",
              "number": 4,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            }
          ]
        },
        {
          "name": "SoundFiles",
          "field": [
            {
              "name": "mp3",
              "number": 1,
              "label": "LABEL_REPEATED",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.themes.v2.SoundSet.SoundFiles.Mp3Entry"
            },
            {
              "name": "ogg",
              "number": 2,
              "label": "LABEL_REPEATED",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.themes.v2.SoundSet.SoundFiles.OggEntry"
            },
            {
              "name": "wav",
              "number": 3,
              "label": "LABEL_REPEATED",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.themes.v2.SoundSet.SoundFiles.WavEntry"
            },
            {
              "name": "webm",
              "number": 4,
              "label": "LABEL_REPEATED",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry"
            }
          ],
          "nested_type": [
            {
              "name": "Mp3Entry",
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
            },
            {
              "name": "OggEntry",
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
            },
            {
              "name": "WavEntry",
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
            },
            {
              "name": "WebmEntry",
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
          ]
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "sounds"
        },
        {
          "name": "_legacy_id"
        }
      ]
    },
    {
      "name": "Attributes",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "is_default",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "legacy_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "localized_name",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "display_priority",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_legacy_id"
        }
      ]
    },
    {
      "name": "ThemeElementCategory",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "localized_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "display_priority",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "ThemeId",
      "field": [
        {
          "name": "preset",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        },
        {
          "name": "custom",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.ThemeElementIds",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "id"
        }
      ]
    },
    {
      "name": "ThemeElementIds",
      "field": [
        {
          "name": "background_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "board_style_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "piece_set_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "sound_set_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "ThemeSelectionItem",
      "field": [
        {
          "name": "theme",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.PresetTheme"
        },
        {
          "name": "is_unlocked",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "BackgroundSelectionItem",
      "field": [
        {
          "name": "background",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.Background"
        },
        {
          "name": "is_unlocked",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "BoardStyleSelectionItem",
      "field": [
        {
          "name": "board_style",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.BoardStyle"
        },
        {
          "name": "is_unlocked",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "PieceSetSelectionItem",
      "field": [
        {
          "name": "piece_set",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.PieceSet"
        },
        {
          "name": "is_unlocked",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "SoundSetSelectionItem",
      "field": [
        {
          "name": "sound_set",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.SoundSet"
        },
        {
          "name": "is_unlocked",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "ThemeSelection",
      "field": [
        {
          "name": "background_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "board_style_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "piece_set_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "sound_set_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "theme_id",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_theme_id"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 311181.

```text
Vzc2NvbS5nYW1lcGxheS52MSItCglCYXR0bGVSZWYSDwoCaWQYASABKAlIAIgBAToIgqYdBAoCAQJCBQoDX2lkYgZwcm90bzM","chesscom/themes/v2/core.proto":"Ch1jaGVzc2NvbS90aGVtZXMvdjIvY29yZS5wcm90bxISY2hlc3Njb20udGhlbWVzLnYyIpgDCgVUaGVtZRIKCgJpZBgBIAEoCRIMCgRuYW1lGAIgASgJEhIKCmlzX2RlZmF1bHQYAyABKAgSFgoJbGVnYWN5X2lkGAQgASgFSACIAQESFgoObG9jYWxpemVkX25hbWUYBSABKAkSGAoQZGlzcGxheV9wcmlvcml0eRgGIAEoBRISCgpvbmJvYXJkaW5nGAogASgIEjIKCmJhY2tncm91bmQY
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17764"></a>
## FND-17764: Full frontend descriptor: chesscom/themes/v2/platform.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/themes/v2/platform.proto",
  "package": "chesscom.themes.v2",
  "enum_type": [
    {
      "name": "Platform",
      "value": [
        {
          "name": "PLATFORM_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLATFORM_WEB",
          "number": 1
        },
        {
          "name": "PLATFORM_ANDROID",
          "number": 2
        },
        {
          "name": "PLATFORM_IPHONE",
          "number": 3
        }
      ],
      "options": {
        "deprecated": true
      }
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 317864.

```text
kGAMgASgJEhQKDHNvdW5kX3NldF9pZBgEIAEoCRIVCgh0aGVtZV9pZBgQIAEoCUgAiAEBQgsKCV90aGVtZV9pZGIGcHJvdG8z","chesscom/themes/v2/platform.proto":"CiFjaGVzc2NvbS90aGVtZXMvdjIvcGxhdGZvcm0ucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MipsCghQbGF0Zm9ybRIYChRQTEFURk9STV9VTlNQRUNJRklFRBAAEhAKDFBMQVRGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17765"></a>
## FND-17765: Full frontend descriptor: chesscom/themes/v2/themes_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/themes/v2/themes_service.proto",
  "package": "chesscom.themes.v2",
  "message_type": [
    {
      "name": "ListAllThemeElementsRequest",
      "field": [
        {
          "name": "board_size",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "pieces_size",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "ListAllThemeElementsResponse",
      "field": [
        {
          "name": "themes",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.PresetTheme"
        },
        {
          "name": "backgrounds",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.Background"
        },
        {
          "name": "board_styles",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.BoardStyle"
        },
        {
          "name": "piece_sets",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.PieceSet"
        },
        {
          "name": "sound_sets",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.SoundSet"
        }
      ],
      "options": {}
    },
    {
      "name": "ListThemesSelectionRequest",
      "options": {}
    },
    {
      "name": "ListThemesSelectionResponse",
      "field": [
        {
          "name": "themes",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.ThemeSelectionItem"
        },
        {
          "name": "backgrounds",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.BackgroundSelectionItem"
        },
        {
          "name": "board_styles",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.BoardStyleSelectionItem"
        },
        {
          "name": "piece_sets",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.PieceSetSelectionItem"
        },
        {
          "name": "sound_sets",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.SoundSetSelectionItem"
        },
        {
          "name": "board_style_categories",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.ThemeElementCategory"
        },
        {
          "name": "piece_set_categories",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.ThemeElementCategory"
        },
        {
          "name": "sound_set_categories",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.ThemeElementCategory"
        }
      ],
      "options": {}
    },
    {
      "name": "ListThemesRequest",
      "field": [
        {
          "name": "platform",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.themes.v2.Platform"
        },
        {
          "name": "board_size",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "pieces_size",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "ListThemesResponse",
      "field": [
        {
          "name": "themes",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.Theme"
        }
      ],
      "options": {}
    },
    {
      "name": "ListBackgroundsRequest",
      "field": [
        {
          "name": "platform",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.themes.v2.Platform"
        }
      ],
      "options": {}
    },
    {
      "name": "ListBackgroundsResponse",
      "field": [
        {
          "name": "backgrounds",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.Background"
        }
      ],
      "options": {}
    },
    {
      "name": "ListBoardStylesRequest",
      "field": [
        {
          "name": "platform",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.themes.v2.Platform"
        },
        {
          "name": "board_size",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "ListBoardStylesResponse",
      "field": [
        {
          "name": "board_styles",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.BoardStyle"
        }
      ],
      "options": {}
    },
    {
      "name": "ListPieceSetsRequest",
      "field": [
        {
          "name": "platform",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.themes.v2.Platform"
        },
        {
          "name": "pieces_size",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "ListPieceSetsResponse",
      "field": [
        {
          "name": "piece_sets",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.PieceSet"
        }
      ],
      "options": {}
    },
    {
      "name": "ListSoundSetsRequest",
      "field": [
        {
          "name": "platform",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.themes.v2.Platform"
        }
      ],
      "options": {}
    },
    {
      "name": "ListSoundSetsResponse",
      "field": [
        {
          "name": "sound_sets",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.SoundSet"
        }
      ],
      "options": {}
    },
    {
      "name": "ListOnboardingThemesRequest",
      "field": [
        {
          "name": "platform",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.themes.v2.Platform"
        },
        {
          "name": "board_size",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "pieces_size",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "ListOnboardingThemesResponse",
      "field": [
        {
          "name": "themes",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.Theme"
        }
      ],
      "options": {}
    },
    {
      "name": "GetThemeRequest",
      "field": [
        {
          "name": "theme_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "platform",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.themes.v2.Platform"
        },
        {
          "name": "board_size",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "pieces_size",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "GetThemeResponse",
      "field": [
        {
          "name": "theme",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.Theme"
        }
      ],
      "options": {}
    },
    {
      "name": "GetCustomThemeRequest",
      "field": [
        {
          "name": "background_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "board_style_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "piece_set_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "sound_set_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "platform",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.themes.v2.Platform"
        },
        {
          "name": "board_size",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "pieces_size",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_background_id"
        }
      ]
    },
    {
      "name": "GetCustomThemeResponse",
      "field": [
        {
          "name": "theme",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.Theme"
        }
      ],
      "options": {}
    },
    {
      "name": "SelectThemeRequest",
      "field": [
        {
          "name": "theme_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "platform",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.themes.v2.Platform"
        }
      ],
      "options": {}
    },
    {
      "name": "SelectThemeResponse",
      "options": {}
    },
    {
      "name": "SelectCustomThemeRequest",
      "field": [
        {
          "name": "background_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "board_style_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "piece_set_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "sound_set_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "platform",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.themes.v2.Platform"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_background_id"
        },
        {
          "name": "_board_style_id"
        },
        {
          "name": "_piece_set_id"
        },
        {
          "name": "_sound_set_id"
        }
      ]
    },
    {
      "name": "SelectCustomThemeResponse",
      "options": {}
    },
    {
      "name": "GetActiveThemeRequest",
      "field": [
        {
          "name": "platform",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.themes.v2.Platform"
        },
        {
          "name": "board_size",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "pieces_size",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "user_id",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_id"
        }
      ]
    },
    {
      "name": "GetActiveThemeResponse",
      "field": [
        {
          "name": "theme",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.themes.v2.Theme"
        }
      ],
      "options": {}
    }
  ],
  "service": [
    {
      "name": "ThemesService",
      "method": [
        {
          "name": "ListAllThemeElements",
          "input_type": ".chesscom.themes.v2.ListAllThemeElementsRequest",
          "output_type": ".chesscom.themes.v2.ListAllThemeElementsResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "ListThemesSelection",
          "input_type": ".chesscom.themes.v2.ListThemesSelectionRequest",
          "output_type": ".chesscom.themes.v2.ListThemesSelectionResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "ListThemes",
          "input_type": ".chesscom.themes.v2.ListThemesRequest",
          "output_type": ".chesscom.themes.v2.ListThemesResponse",
          "options": {
            "deprecated": true,
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "ListBackgrounds",
          "input_type": ".chesscom.themes.v2.ListBackgroundsRequest",
          "output_type": ".chesscom.themes.v2.ListBackgroundsResponse",
          "options": {
            "deprecated": true,
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "ListBoardStyles",
          "input_type": ".chesscom.themes.v2.ListBoardStylesRequest",
          "output_type": ".chesscom.themes.v2.ListBoardStylesResponse",
          "options": {
            "deprecated": true,
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "ListPieceSets",
          "input_type": ".chesscom.themes.v2.ListPieceSetsRequest",
          "output_type": ".chesscom.themes.v2.ListPieceSetsResponse",
          "options": {
            "deprecated": true,
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "ListSoundSets",
          "input_type": ".chesscom.themes.v2.ListSoundSetsRequest",
          "output_type": ".chesscom.themes.v2.ListSoundSetsResponse",
          "options": {
            "deprecated": true,
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "ListOnboardingThemes",
          "input_type": ".chesscom.themes.v2.ListOnboardingThemesRequest",
          "output_type": ".chesscom.themes.v2.ListOnboardingThemesResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "GetTheme",
          "input_type": ".chesscom.themes.v2.GetThemeRequest",
          "output_type": ".chesscom.themes.v2.GetThemeResponse",
          "options": {
            "deprecated": true,
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "GetCustomTheme",
          "input_type": ".chesscom.themes.v2.GetCustomThemeRequest",
          "output_type": ".chesscom.themes.v2.GetCustomThemeResponse",
          "options": {
            "deprecated": true,
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "SelectTheme",
          "input_type": ".chesscom.themes.v2.SelectThemeRequest",
          "output_type": ".chesscom.themes.v2.SelectThemeResponse",
          "options": {}
        },
        {
          "name": "SelectCustomTheme",
          "input_type": ".chesscom.themes.v2.SelectCustomThemeRequest",
          "output_type": ".chesscom.themes.v2.SelectCustomThemeResponse",
          "options": {}
        },
        {
          "name": "GetActiveTheme",
          "input_type": ".chesscom.themes.v2.GetActiveThemeRequest",
          "output_type": ".chesscom.themes.v2.GetActiveThemeResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        }
      ],
      "options": {}
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 318134.

```text
RGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVzc2NvbS90aGVtZXMvdjIvdGhlbWVzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MiJPChtMaXN0QWxsVGhlbWVFbGVtZW50c1JlcXVlc3QSEgoKYm9hcmRfc2l6ZRgBIAEoBRITCgtwaWVjZXNfc2l6ZRgCIAEoBToHgqYdAwoBASKnAgocTGlzdEFsbFRoZW1lRWxlbWVudHNSZXNwb25zZRIvCgZ0aGVtZXMYASADKAsyHy5jaGVzc2NvbS50aGVtZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17779"></a>
## FND-17779: Full frontend descriptor: chesscom/progression/v1/event_specifics.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/progression/v1/event_specifics.proto",
  "package": "chesscom.progression.v1",
  "message_type": [
    {
      "name": "BotEventSpecifics",
      "field": [
        {
          "name": "active_variations",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.progression.v1.BotEventSpecifics.ActiveVariationsEntry"
        },
        {
          "name": "variation_timestamp",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        }
      ],
      "nested_type": [
        {
          "name": "ActiveVariationsEntry",
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
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.progression.v1.BotOverrides"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {}
    },
    {
      "name": "BotOverrides",
      "field": [
        {
          "name": "bot_label",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.progression.v1.BotLabel",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "fen_player_is_white",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "fen_player_is_black",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_bot_label"
        },
        {
          "name": "_fen_player_is_white"
        },
        {
          "name": "_fen_player_is_black"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "BotVariationSupport",
      "value": [
        {
          "name": "BOT_VARIATION_SUPPORT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "BOT_VARIATION_SUPPORT_CUSTOM_FEN",
          "number": 1
        }
      ],
      "options": {}
    },
    {
      "name": "BotLabel",
      "value": [
        {
          "name": "BOT_LABEL_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "BOT_LABEL_TYPE_HARDER",
          "number": 1
        },
        {
          "name": "BOT_LABEL_TYPE_EASIER",
          "number": 2
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 324813.

```text
gHatywBARoHkqYdAwoBAUIvyrcsKwoEL3JwYxIeEg13d3cuY2hlc3MuY29tEg1hcGkuY2hlc3MuY29tGgAqAWRiBnByb3RvMw","chesscom/progression/v1/event_specifics.proto":"Ci1jaGVzc2NvbS9wcm9ncmVzc2lvbi92MS9ldmVudF9zcGVjaWZpY3MucHJvdG8SF2NoZXNzY29tLnByb2dyZXNzaW9uLnYxIpICChFCb3RFdmVudFNwZWNpZmljcxJbChFhY3RpdmVfdmFyaWF0aW9ucxgBIAMoCzJALmNoZXNzY29tLnByb2dyZXNzaW9uLnYxLkJvdEV2ZW50U3BlY2lmaWNzLkFjdGl2ZVZhcmlhdGlvbnNFbnRyeRI3ChN2YXJpYXRpb25fdGlt
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17780"></a>
## FND-17780: Full frontend descriptor: chesscom/i18n/v1/translation.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/i18n/v1/translation.proto",
  "package": "chesscom.i18n.v1",
  "message_type": [
    {
      "name": "TranslationResourceStats",
      "field": [
        {
          "name": "resource_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "key",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "translation_entry_rates",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.i18n.v1.TranslationResourceStats.TranslationEntryRatesEntry"
        },
        {
          "name": "overall_completion_rate",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        }
      ],
      "nested_type": [
        {
          "name": "TranslationEntryRatesEntry",
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
              "type": "TYPE_DOUBLE"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ]
    },
    {
      "name": "Translation",
      "field": [
        {
          "name": "string_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "key",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "source",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "project_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "resource_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "translation_metadata",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.i18n.v1.TranslationMetadata",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "translation_entries",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.i18n.v1.Translation.TranslationEntriesEntry"
        }
      ],
      "nested_type": [
        {
          "name": "TranslationEntriesEntry",
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
      "options": {},
      "oneof_decl": [
        {
          "name": "_project_id"
        },
        {
          "name": "_resource_id"
        },
        {
          "name": "_translation_metadata"
        }
      ]
    },
    {
      "name": "FileTranslation",
      "field": [
        {
          "name": "file_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "file_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "file_path",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "file_format",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "project_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "resource_id",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "translation_metadata",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.i18n.v1.TranslationMetadata",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "translation_entries",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.i18n.v1.FileTranslation.TranslationEntriesEntry",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "tags",
          "number": 9,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "nested_type": [
        {
          "name": "TranslationEntriesEntry",
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
          "name": "_project_id"
        },
        {
          "name": "_resource_id"
        },
        {
          "name": "_translation_metadata"
        }
      ]
    },
    {
      "name": "TranslationMetadata",
      "field": [
        {
          "name": "completion_rate",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.i18n.v1.TranslationMetadata.CompletionRateEntry"
        }
      ],
      "nested_type": [
        {
          "name": "CompletionRateEntry",
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
              "type": "TYPE_DOUBLE"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {}
    },
    {
      "name": "LanguageDefinition",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "editor_code",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "two_letters_code",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "three_letters_code",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "locale",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "android_code",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "osx_code",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "osx_locale",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "plural_category_names",
          "number": 10,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "plural_rules",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "plural_examples",
          "number": 12,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "text_direction",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "dialect_of",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_dialect_of"
        }
      ]
    },
    {
      "name": "UpdateString",
      "field": [
        {
          "name": "string_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "new_value",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "UpdateFileData",
      "field": [
        {
          "name": "file_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "new_value",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "SyncFailure",
      "field": [
        {
          "name": "file_path",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "error_code",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.i18n.v1.FailedSyncErrorCode"
        },
        {
          "name": "error_message",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "keys",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "SyncWarning",
      "field": [
        {
          "name": "file_path",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "kind",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.i18n.v1.SyncWarningKind"
        },
        {
          "name": "message",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "keys",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "FailedSyncErrorCode",
      "value": [
        {
          "name": "FAILED_SYNC_ERROR_CODE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "FAILED_SYNC_ERROR_CODE_CROWDIN_API_ERROR",
          "number": 1
        },
        {
          "name": "FAILED_SYNC_ERROR_CODE_NETWORK_TIMEOUT",
          "number": 2
        },
        {
          "name": "FAILED_SYNC_ERROR_CODE_SYNC_ERROR",
          "number": 3
        },
        {
          "name": "FAILED_SYNC_ERROR_CODE_SOURCE_DIVERGENCE",
          "number": 4
        }
      ]
    },
    {
      "name": "SyncWarningKind",
      "value": [
        {
          "name": "SYNC_WARNING_KIND_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SYNC_WARNING_KIND_MISSING_IN_DB",
          "number": 1
        },
        {
          "name": "SYNC_WARNING_KIND_UNAPPROVED_IN_DB",
          "number": 2
        },
        {
          "name": "SYNC_WARNING_KIND_MISSING_IN_VENDOR",
          "number": 3
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 325915.

```text
AAEhkKFUJPVF9MQUJFTF9UWVBFX0hBUkRFUhABEhkKFUJPVF9MQUJFTF9UWVBFX0VBU0lFUhACGgeKph0DCgEBYgZwcm90bzM","chesscom/i18n/v1/translation.proto":"CiJjaGVzc2NvbS9pMThuL3YxL3RyYW5zbGF0aW9uLnByb3RvEhBjaGVzc2NvbS5pMThuLnYxIoMCChhUcmFuc2xhdGlvblJlc291cmNlU3RhdHMSEwoLcmVzb3VyY2VfaWQYASABKAkSCwoDa2V5GAIgASgJEmYKF3RyYW5zbGF0aW9uX2VudHJ5X3JhdGVzGAMgAygLMkUuY2hlc3Njb20uaTE4bi52MS5UcmFuc2xhdGlvblJlc291cmNlU3RhdHMuVHJhbnNsYXRpb25FbnRyeVJ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17781"></a>
## FND-17781: Full frontend descriptor: chesscom/progression/v1/event_configuration.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/progression/v1/event_configuration.proto",
  "package": "chesscom.progression.v1",
  "message_type": [
    {
      "name": "ProgressionRewardConfiguration",
      "field": [
        {
          "name": "required_points",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "reward_asset",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Asset",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "reward_description",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.i18n.v1.Translation",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "unlockable",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.unlockables.v1.UnlockableResourceIdentifier"
        },
        {
          "name": "premium_only",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_reward_description"
        },
        {
          "name": "_premium_only"
        }
      ]
    },
    {
      "name": "ProgressionModifierTrigger",
      "field": [
        {
          "name": "start_time",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 0
        },
        {
          "name": "start_max_games_played",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0
        },
        {
          "name": "start_max_wins",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0
        },
        {
          "name": "end_time",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 1
        },
        {
          "name": "duration_minutes",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "start_criteria"
        },
        {
          "name": "end_criteria"
        }
      ]
    },
    {
      "name": "EventProgress",
      "field": [
        {
          "name": "current_points",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "rewards",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.progression.v1.EventReward",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "event_config_key",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "bot_event_specifics",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.progression.v1.BotEventSpecifics",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "event_specifics"
        }
      ]
    },
    {
      "name": "EventUnlockable",
      "field": [
        {
          "name": "required_points",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "unlockable",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.unlockables.v1.UnlockableResourceIdentifier"
        },
        {
          "name": "image_url",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "premium_only",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "user_meets_external_requirements",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "is_premium_reward",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_premium_only"
        },
        {
          "name": "_user_meets_external_requirements"
        },
        {
          "name": "_is_premium_reward"
        }
      ]
    },
    {
      "name": "EventReward",
      "field": [
        {
          "name": "icon",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Asset"
        },
        {
          "name": "type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.progression.v1.EventRewardType"
        },
        {
          "name": "required_points",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "unlocked_at",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {
        "deprecated": true
      },
      "oneof_decl": [
        {
          "name": "_unlocked_at"
        }
      ]
    },
    {
      "name": "EventProgressUpdate",
      "field": [
        {
          "name": "current_points",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "progress_update_steps",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.progression.v1.EventProgressUpdateStep"
        },
        {
          "name": "event_config_key",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "EventProgressUpdateStep",
      "field": [
        {
          "name": "points_to_add",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "bonus_type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.progression.v1.EventProgressBonusType"
        },
        {
          "name": "multiplier",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_multiplier"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "EventRewardType",
      "value": [
        {
          "name": "EVENT_REWARD_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "EVENT_REWARD_TYPE_FLAIR",
          "number": 1
        },
        {
          "name": "EVENT_REWARD_TYPE_BOARD",
          "number": 2
        },
        {
          "name": "EVENT_REWARD_TYPE_PIECES",
          "number": 3
        },
        {
          "name": "EVENT_REWARD_TYPE_SOUNDS",
          "number": 4
        }
      ],
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "EventProgressBonusType",
      "value": [
        {
          "name": "EVENT_PROGRESS_BONUS_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "EVENT_PROGRESS_BONUS_TYPE_DAILY_BONUS",
          "number": 1
        },
        {
          "name": "EVENT_PROGRESS_BONUS_TYPE_BOT_BUFF",
          "number": 2
        },
        {
          "name": "EVENT_PROGRESS_BONUS_TYPE_BASE",
          "number": 3
        },
        {
          "name": "EVENT_PROGRESS_BONUS_TYPE_VICTORY_MULTIPLIER",
          "number": 4
        },
        {
          "name": "EVENT_PROGRESS_BONUS_TYPE_GAME_REVIEW",
          "number": 5
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 329217.

```text
0tJTkRfVU5BUFBST1ZFRF9JTl9EQhACEicKI1NZTkNfV0FSTklOR19LSU5EX01JU1NJTkdfSU5fVkVORE9SEANiBnByb3RvMw","chesscom/progression/v1/event_configuration.proto":"CjFjaGVzc2NvbS9wcm9ncmVzc2lvbi92MS9ldmVudF9jb25maWd1cmF0aW9uLnByb3RvEhdjaGVzc2NvbS5wcm9ncmVzc2lvbi52MSLGAgoeUHJvZ3Jlc3Npb25SZXdhcmRDb25maWd1cmF0aW9uEhcKD3JlcXVpcmVkX3BvaW50cxgBIAEoDRIwCgxyZXdhcmRfYXNzZXQYAiABKAsyFi5jaGVzc2NvbS5hcGkudjEuQXNzZXRCAhgBEkIKEnJld2FyZF9kZXNj
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17782"></a>
## FND-17782: Full frontend descriptor: chesscom/bots/v1/bot_event.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/bots/v1/bot_event.proto",
  "package": "chesscom.bots.v1",
  "message_type": [
    {
      "name": "BotEvent",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "description",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "theme",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotEventTheme"
        },
        {
          "name": "progress",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.progression.v1.EventProgress",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "progress_unit_name",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "end_time",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "bot_event_key",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "variation_modal_data",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotVariationModalData"
        },
        {
          "name": "unlockables",
          "number": 9,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.progression.v1.EventUnlockable"
        },
        {
          "name": "resign_min_plies",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "intro_modal_data",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotEventIntroModalData"
        },
        {
          "name": "premium_multiplier",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "game_review_data",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.GameReviewEventData",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_premium_multiplier"
        },
        {
          "name": "_game_review_data"
        }
      ]
    },
    {
      "name": "GameReviewEventData",
      "field": [
        {
          "name": "points",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "points_icon",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Asset"
        }
      ],
      "options": {}
    },
    {
      "name": "BotProperties",
      "field": [
        {
          "name": "win_points",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "loss_points",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "draw_points",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "assistance_use_penalty",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "fen",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "play_as_white",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "label",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotLabel",
          "options": {
            "deprecated": true
          },
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "komodo_skill_override",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "fen_player_is_white",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "fen_player_is_black",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 5,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_fen"
        },
        {
          "name": "_play_as_white"
        },
        {
          "name": "_label"
        },
        {
          "name": "_komodo_skill_override"
        },
        {
          "name": "_fen_player_is_white"
        },
        {
          "name": "_fen_player_is_black"
        }
      ]
    },
    {
      "name": "BotLabel",
      "field": [
        {
          "name": "type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.bots.v1.BotLabelType"
        }
      ],
      "options": {}
    },
    {
      "name": "BotEventTheme",
      "field": [
        {
          "name": "primary_color",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "secondary_color",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "points_icon",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Asset"
        },
        {
          "name": "banner_image",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Asset"
        },
        {
          "name": "background_image",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Asset"
        },
        {
          "name": "sounds",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotEventSounds"
        }
      ],
      "options": {}
    },
    {
      "name": "BotEventSounds",
      "field": [
        {
          "name": "game_start",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Asset",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "gameplay_ambient",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Asset",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_game_start"
        },
        {
          "name": "_gameplay_ambient"
        }
      ]
    },
    {
      "name": "BotVariationModalData",
      "field": [
        {
          "name": "image",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Asset"
        },
        {
          "name": "title",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "bot_advantage_text",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "bot_disadvantage_text",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "BotEventIntroModalData",
      "field": [
        {
          "name": "image",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Asset"
        },
        {
          "name": "title",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "subtitle",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "info_items",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotEventIntroModalInfoItemData"
        }
      ],
      "options": {}
    },
    {
      "name": "BotEventIntroModalInfoItemData",
      "field": [
        {
          "name": "icon",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Asset"
        },
        {
          "name": "text",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "BotLabelType",
      "value": [
        {
          "name": "BOT_LABEL_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "BOT_LABEL_TYPE_HARDER",
          "number": 1
        },
        {
          "name": "BOT_LABEL_TYPE_EASIER",
          "number": 2
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 332306.

```text
01VTFRJUExJRVIQBBIpCiVFVkVOVF9QUk9HUkVTU19CT05VU19UWVBFX0dBTUVfUkVWSUVXEAUaB4qmHQMKAQFiBnByb3RvMw","chesscom/bots/v1/bot_event.proto":"CiBjaGVzc2NvbS9ib3RzL3YxL2JvdF9ldmVudC5wcm90bxIQY2hlc3Njb20uYm90cy52MSL8BAoIQm90RXZlbnQSDAoEbmFtZRgBIAEoCRITCgtkZXNjcmlwdGlvbhgCIAEoCRIuCgV0aGVtZRgDIAEoCzIfLmNoZXNzY29tLmJvdHMudjEuQm90RXZlbnRUaGVtZRI8Cghwcm9ncmVzcxgEIAEoCzImLmNoZXNzY29tLnByb2dyZXNzaW9uLnYxLkV2ZW50UHJvZ3Jlc3NCAhgBEhoKE
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17783"></a>
## FND-17783: Full frontend descriptor: chesscom/bots/v1/phrase_list.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/bots/v1/phrase_list.proto",
  "package": "chesscom.bots.v1",
  "message_type": [
    {
      "name": "PhraseList",
      "field": [
        {
          "name": "greeting",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "won",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "lost",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "draw",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "winning",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "losing",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "giving_check",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "being_checked",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "capturing_queen",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "queen_captured",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "promoting_pawn",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "player_pawn_promote",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "first_capture",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "threatening",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "threatened",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "computer_has_mate_in_x",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "player_has_mate_in_x",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "random",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "opening_e4",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "opening_d4",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "opening_c4_english",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "opening_nf3",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "opening_e4_e5_kings_pawn",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 22,
          "proto3_optional": true
        },
        {
          "name": "opening_e4_c5_sicilian",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 23,
          "proto3_optional": true
        },
        {
          "name": "opening_e4_c6_carokann",
          "number": 25,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 24,
          "proto3_optional": true
        },
        {
          "name": "opening_e4_e6_french",
          "number": 26,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 25,
          "proto3_optional": true
        },
        {
          "name": "opening_d4_nf6_indian",
          "number": 27,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 26,
          "proto3_optional": true
        },
        {
          "name": "opening_d4_d5_queens_gambit",
          "number": 28,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 27,
          "proto3_optional": true
        },
        {
          "name": "opening_other",
          "number": 29,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 28,
          "proto3_optional": true
        },
        {
          "name": "user_spends_more_than_15_seconds_on_a_move",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 29,
          "proto3_optional": true
        },
        {
          "name": "user_spends_more_than_1_minute_on_a_move",
          "number": 31,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 30,
          "proto3_optional": true
        },
        {
          "name": "user_spends_more_than_3_minutes_on_move",
          "number": 32,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 31,
          "proto3_optional": true
        },
        {
          "name": "r_p_endgame_reached",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 32,
          "proto3_optional": true
        },
        {
          "name": "k_p_endgame_reached",
          "number": 34,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 33,
          "proto3_optional": true
        },
        {
          "name": "game_reached_move_40",
          "number": 35,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 34,
          "proto3_optional": true
        },
        {
          "name": "game_reached_move_100",
          "number": 36,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 35,
          "proto3_optional": true
        },
        {
          "name": "rematch_if_user_has_played_before",
          "number": 37,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 36,
          "proto3_optional": true
        },
        {
          "name": "heavy_piece_endgame_reached",
          "number": 38,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 37,
          "proto3_optional": true
        },
        {
          "name": "minor_piece_endgame_reached",
          "number": 39,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 38,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_greeting"
        },
        {
          "name": "_won"
        },
        {
          "name": "_lost"
        },
        {
          "name": "_draw"
        },
        {
          "name": "_winning"
        },
        {
          "name": "_losing"
        },
        {
          "name": "_giving_check"
        },
        {
          "name": "_being_checked"
        },
        {
          "name": "_capturing_queen"
        },
        {
          "name": "_queen_captured"
        },
        {
          "name": "_promoting_pawn"
        },
        {
          "name": "_player_pawn_promote"
        },
        {
          "name": "_first_capture"
        },
        {
          "name": "_threatening"
        },
        {
          "name": "_threatened"
        },
        {
          "name": "_computer_has_mate_in_x"
        },
        {
          "name": "_player_has_mate_in_x"
        },
        {
          "name": "_random"
        },
        {
          "name": "_opening_e4"
        },
        {
          "name": "_opening_d4"
        },
        {
          "name": "_opening_c4_english"
        },
        {
          "name": "_opening_nf3"
        },
        {
          "name": "_opening_e4_e5_kings_pawn"
        },
        {
          "name": "_opening_e4_c5_sicilian"
        },
        {
          "name": "_opening_e4_c6_carokann"
        },
        {
          "name": "_opening_e4_e6_french"
        },
        {
          "name": "_opening_d4_nf6_indian"
        },
        {
          "name": "_opening_d4_d5_queens_gambit"
        },
        {
          "name": "_opening_other"
        },
        {
          "name": "_user_spends_more_than_15_seconds_on_a_move"
        },
        {
          "name": "_user_spends_more_than_1_minute_on_a_move"
        },
        {
          "name": "_user_spends_more_than_3_minutes_on_move"
        },
        {
          "name": "_r_p_endgame_reached"
        },
        {
          "name": "_k_p_endgame_reached"
        },
        {
          "name": "_game_reached_move_40"
        },
        {
          "name": "_game_reached_move_100"
        },
        {
          "name": "_rematch_if_user_has_played_before"
        },
        {
          "name": "_heavy_piece_endgame_reached"
        },
        {
          "name": "_minor_piece_endgame_reached"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 335398.

```text
AASGQoVQk9UX0xBQkVMX1RZUEVfSEFSREVSEAESGQoVQk9UX0xBQkVMX1RZUEVfRUFTSUVSEAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/bots/v1/phrase_list.proto":"CiJjaGVzc2NvbS9ib3RzL3YxL3BocmFzZV9saXN0LnByb3RvEhBjaGVzc2NvbS5ib3RzLnYxIv0QCgpQaHJhc2VMaXN0EhUKCGdyZWV0aW5nGAEgASgJSACIAQESEAoDd29uGAIgASgJSAGIAQESEQoEbG9zdBgDIAEoCUgCiAEBEhEKBGRyYXcYBCABKAlIA4gBARIUCgd3aW5uaW5nGAUgASgJSASIAQESEwoGbG9zaW5nGAYgASgJSAWIAQESGQoMZ2l2aW5nX2NoZWNrGAcgASg
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17784"></a>
## FND-17784: Full frontend descriptor: chesscom/bots/v1/bot_personality.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/bots/v1/bot_personality.proto",
  "package": "chesscom.bots.v1",
  "message_type": [
    {
      "name": "BotPersonality",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "sort_order",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "enabled",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "username",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "classification",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "updated_at",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "name",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_id",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "classification_hint_text",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "premium",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "komodo_skill_level",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "komodo_skill",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "adapt",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "human",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "personality",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.bots.v1.Personality"
        },
        {
          "name": "book",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "country_code",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "gender",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "rating",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "rating_text",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "live_online_rating",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "description",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "pawn_endgame",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "major_piece_endgame",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "minor_piece_endgame",
          "number": 25,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "v2",
          "number": 26,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "theme_uuid",
          "number": 27,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "minimum_cee_version",
          "number": 28,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "crown_earned",
          "number": 29,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "image_url",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "image_url_override",
          "number": 31,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "phrase_list",
          "number": 32,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.PhraseList"
        },
        {
          "name": "v2_spread_sheet",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "supported_languages",
          "number": 34,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "book_fallback",
          "number": 35,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "can_play",
          "number": 36,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 22,
          "proto3_optional": true
        },
        {
          "name": "fen_as_black",
          "number": 37,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 23,
          "proto3_optional": true
        },
        {
          "name": "fen_as_white",
          "number": 38,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 24,
          "proto3_optional": true
        },
        {
          "name": "avatar_without_background",
          "number": 39,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 25,
          "proto3_optional": true
        },
        {
          "name": "has_custom_modal",
          "number": 40,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 26,
          "proto3_optional": true
        },
        {
          "name": "custom_modal_requires_account_activation",
          "number": 41,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 27,
          "proto3_optional": true
        },
        {
          "name": "properties",
          "number": 42,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotProperties",
          "oneof_index": 28,
          "proto3_optional": true
        },
        {
          "name": "bot_move_configuration_key",
          "number": 43,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 29,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_premium"
        },
        {
          "name": "_komodo_skill_level"
        },
        {
          "name": "_komodo_skill"
        },
        {
          "name": "_adapt"
        },
        {
          "name": "_human"
        },
        {
          "name": "_book"
        },
        {
          "name": "_country_code"
        },
        {
          "name": "_gender"
        },
        {
          "name": "_rating"
        },
        {
          "name": "_rating_text"
        },
        {
          "name": "_live_online_rating"
        },
        {
          "name": "_description"
        },
        {
          "name": "_pawn_endgame"
        },
        {
          "name": "_major_piece_endgame"
        },
        {
          "name": "_minor_piece_endgame"
        },
        {
          "name": "_theme_uuid"
        },
        {
          "name": "_minimum_cee_version"
        },
        {
          "name": "_crown_earned"
        },
        {
          "name": "_image_url"
        },
        {
          "name": "_image_url_override"
        },
        {
          "name": "_v2_spread_sheet"
        },
        {
          "name": "_book_fallback"
        },
        {
          "name": "_can_play"
        },
        {
          "name": "_fen_as_black"
        },
        {
          "name": "_fen_as_white"
        },
        {
          "name": "_avatar_without_background"
        },
        {
          "name": "_has_custom_modal"
        },
        {
          "name": "_custom_modal_requires_account_activation"
        },
        {
          "name": "_properties"
        },
        {
          "name": "_bot_move_configuration_key"
        }
      ]
    },
    {
      "name": "SupportedBot",
      "field": [
        {
          "name": "bot_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "Personality",
      "value": [
        {
          "name": "PERSONALITY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PERSONALITY_UNSPECIFIED_DEFAULT",
          "number": 1
        },
        {
          "name": "PERSONALITY_UNSPECIFIED_BEGINNER",
          "number": 2
        },
        {
          "name": "PERSONALITY_UNSPECIFIED_AGGRESSIVE",
          "number": 3
        },
        {
          "name": "PERSONALITY_UNSPECIFIED_POSITIONAL",
          "number": 4
        },
        {
          "name": "PERSONALITY_UNSPECIFIED_DEFENSIVE",
          "number": 5
        },
        {
          "name": "PERSONALITY_UNSPECIFIED_ENDGAME",
          "number": 6
        },
        {
          "name": "PERSONALITY_UNSPECIFIED_HUMAN",
          "number": 7
        },
        {
          "name": "PERSONALITY_UNSPECIFIED_HIKARU",
          "number": 8
        },
        {
          "name": "PERSONALITY_UNSPECIFIED_DANNY",
          "number": 9
        },
        {
          "name": "PERSONALITY_UNSPECIFIED_ACTIVE",
          "number": 10
        },
        {
          "name": "PERSONALITY_UNSPECIFIED_NEW_TO_CHESS",
          "number": 11
        },
        {
          "name": "PERSONALITY_UNSPECIFIED_UNLEASHED",
          "number": 12
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 338422.

```text
lQh4KHF9oZWF2eV9waWVjZV9lbmRnYW1lX3JlYWNoZWRCHgocX21pbm9yX3BpZWNlX2VuZGdhbWVfcmVhY2hlZGIGcHJvdG8z","chesscom/bots/v1/bot_personality.proto":"CiZjaGVzc2NvbS9ib3RzL3YxL2JvdF9wZXJzb25hbGl0eS5wcm90bxIQY2hlc3Njb20uYm90cy52MSKiDgoOQm90UGVyc29uYWxpdHkSCgoCaWQYASABKAkSEgoKc29ydF9vcmRlchgCIAEoBRIPCgdlbmFibGVkGAMgASgIEhAKCHVzZXJuYW1lGAQgASgJEhYKDmNsYXNzaWZpY2F0aW9uGAUgASgJEi4KCnVwZGF0ZWRfYXQYBiABKAsyGi5nb29nbGUucHJvdG9idWYuVGl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17785"></a>
## FND-17785: Full frontend descriptor: chesscom/bots/v1/bot_group.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/bots/v1/bot_group.proto",
  "package": "chesscom.bots.v1",
  "message_type": [
    {
      "name": "BotGroup",
      "field": [
        {
          "name": "uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "hint_description",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "club_uuid",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "bot_personalities",
          "number": 12,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotPersonality"
        },
        {
          "name": "avatar",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "featured",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "configuration_key",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "event",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotEvent",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "url",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "enabled",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "staff_enabled",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 6,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_club_uuid"
        },
        {
          "name": "_avatar"
        },
        {
          "name": "_configuration_key"
        },
        {
          "name": "_event"
        },
        {
          "name": "_url"
        },
        {
          "name": "_enabled"
        },
        {
          "name": "_staff_enabled"
        }
      ],
      "reserved_range": [
        {
          "start": 4,
          "end": 5
        },
        {
          "start": 5,
          "end": 6
        },
        {
          "start": 6,
          "end": 7
        },
        {
          "start": 7,
          "end": 8
        },
        {
          "start": 8,
          "end": 9
        },
        {
          "start": 10,
          "end": 11
        },
        {
          "start": 11,
          "end": 12
        },
        {
          "start": 13,
          "end": 14
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 341728.

```text
URfTkVXX1RPX0NIRVNTEAsSJQohUEVSU09OQUxJVFlfVU5TUEVDSUZJRURfVU5MRUFTSEVEEAwaB4qmHQMKAQFiBnByb3RvMw","chesscom/bots/v1/bot_group.proto":"CiBjaGVzc2NvbS9ib3RzL3YxL2JvdF9ncm91cC5wcm90bxIQY2hlc3Njb20uYm90cy52MSLsAwoIQm90R3JvdXASDAoEdXVpZBgBIAEoCRIMCgRuYW1lGAIgASgJEhgKEGhpbnRfZGVzY3JpcHRpb24YAyABKAkSFgoJY2x1Yl91dWlkGAkgASgJSACIAQESOwoRYm90X3BlcnNvbmFsaXRpZXMYDCADKAsyIC5jaGVzc2NvbS5ib3RzLnYxLkJvdFBlcnNvbmFsaXR5EhMKBmF2YXRhc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17786"></a>
## FND-17786: Full frontend descriptor: chesscom/bots/v1/bot_group_service.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/bots/v1/bot_group_service.proto",
  "package": "chesscom.bots.v1",
  "message_type": [
    {
      "name": "ListBotGroupsRequest",
      "field": [
        {
          "name": "bot_group_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "with_bots",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "supported_languages",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_bot_group_uuid"
        },
        {
          "name": "_with_bots"
        }
      ]
    },
    {
      "name": "ListBotGroupsResponse",
      "field": [
        {
          "name": "bot_groups",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotGroup"
        },
        {
          "name": "recommended_bot_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_recommended_bot_id"
        }
      ]
    },
    {
      "name": "ListAllBotsInGroupRequest",
      "field": [
        {
          "name": "bot_group_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "supported_languages",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "ListAllBotsInGroupResponse",
      "field": [
        {
          "name": "bot_group",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotGroup"
        },
        {
          "name": "bot_personalities",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotPersonality"
        }
      ],
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "ListAllBotsForClubRequest",
      "field": [
        {
          "name": "club_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "ListAllBotsForClubResponse",
      "field": [
        {
          "name": "bot_group",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotGroup"
        },
        {
          "name": "bot_personalities",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.BotPersonality"
        }
      ],
      "options": {}
    },
    {
      "name": "ListAllBotNamesRequest",
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "ListAllBotNamesResponse",
      "field": [
        {
          "name": "supported_bot",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.bots.v1.SupportedBot"
        }
      ],
      "options": {
        "deprecated": true
      }
    }
  ],
  "service": [
    {
      "name": "BotGroupService",
      "method": [
        {
          "name": "ListBotGroups",
          "input_type": ".chesscom.bots.v1.ListBotGroupsRequest",
          "output_type": ".chesscom.bots.v1.ListBotGroupsResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "ListAllBotsInGroup",
          "input_type": ".chesscom.bots.v1.ListAllBotsInGroupRequest",
          "output_type": ".chesscom.bots.v1.ListAllBotsInGroupResponse",
          "options": {
            "deprecated": true,
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "ListAllBotsForClub",
          "input_type": ".chesscom.bots.v1.ListAllBotsForClubRequest",
          "output_type": ".chesscom.bots.v1.ListAllBotsForClubResponse",
          "options": {
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        },
        {
          "name": "ListAllBotNames",
          "input_type": ".chesscom.bots.v1.ListAllBotNamesRequest",
          "output_type": ".chesscom.bots.v1.ListAllBotNamesResponse",
          "options": {
            "deprecated": true,
            "idempotency_level": "NO_SIDE_EFFECTS"
          }
        }
      ],
      "options": {}
    }
  ],
  "options": {},
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 342506.

```text
QCg5fc3RhZmZfZW5hYmxlZEoECAQQBUoECAUQBkoECAYQB0oECAcQCEoECAgQCUoECAoQC0oECAsQDEoECA0QDmIGcHJvdG8z","chesscom/bots/v1/bot_group_service.proto":"CihjaGVzc2NvbS9ib3RzL3YxL2JvdF9ncm91cF9zZXJ2aWNlLnByb3RvEhBjaGVzc2NvbS5ib3RzLnYxIpIBChRMaXN0Qm90R3JvdXBzUmVxdWVzdBIbCg5ib3RfZ3JvdXBfdXVpZBgBIAEoCUgAiAEBEhYKCXdpdGhfYm90cxgFIAEoCEgBiAEBEhsKE3N1cHBvcnRlZF9sYW5ndWFnZXMYBiADKAk6B4KmHQMKAQFCEQoPX2JvdF9ncm91cF91dWlkQgwKCl93aXRoX2Jvd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17791"></a>
## FND-17791: Full frontend descriptor: chesscom/presence/v1/presence.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/presence/v1/presence.proto",
  "package": "chesscom.presence.v1",
  "message_type": [
    {
      "name": "UserPresence",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "status",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.presence.v1.ConnectionStatus"
        },
        {
          "name": "status_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "updated_at",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "activity",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.presence.v1.PresenceActivity",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "activity_context",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.presence.v1.PresenceActivityContext",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "status_at_uncertain",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "streaming",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.presence.v1.Streaming",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "quality",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.presence.v1.ConnectionQuality",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "location",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Location",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "clients",
          "number": 11,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.presence.v1.ClientInfo"
        },
        {
          "name": "attributes",
          "number": 12,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "capabilities",
          "number": 13,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_activity"
        },
        {
          "name": "_activity_context"
        },
        {
          "name": "_status_at_uncertain"
        },
        {
          "name": "_streaming"
        },
        {
          "name": "_quality"
        },
        {
          "name": "_location"
        }
      ]
    },
    {
      "name": "Streaming",
      "field": [
        {
          "name": "started_at",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "url",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "PresenceActivityContext",
      "field": [
        {
          "name": "games",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.gameplay.v1.GameRef"
        },
        {
          "name": "battles",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.gameplay.v1.BattleRef"
        }
      ],
      "options": {}
    },
    {
      "name": "ClientInfo",
      "field": [
        {
          "name": "type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.presence.v1.ClientType",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_type"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "PresenceStatus",
      "value": [
        {
          "name": "PRESENCE_STATUS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PRESENCE_STATUS_OFFLINE",
          "number": 1
        },
        {
          "name": "PRESENCE_STATUS_ONLINE",
          "number": 2
        },
        {
          "name": "PRESENCE_STATUS_PLAYING",
          "number": 3
        }
      ],
      "options": {}
    },
    {
      "name": "ConnectionStatus",
      "value": [
        {
          "name": "CONNECTION_STATUS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CONNECTION_STATUS_OFFLINE",
          "number": 1
        },
        {
          "name": "CONNECTION_STATUS_ONLINE",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "PresenceActivity",
      "value": [
        {
          "name": "PRESENCE_ACTIVITY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PRESENCE_ACTIVITY_NONE",
          "number": 1
        },
        {
          "name": "PRESENCE_ACTIVITY_PLAYING",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "ConnectionQuality",
      "value": [
        {
          "name": "CONNECTION_QUALITY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CONNECTION_QUALITY_OFFLINE",
          "number": 1
        },
        {
          "name": "CONNECTION_QUALITY_POOR",
          "number": 2
        },
        {
          "name": "CONNECTION_QUALITY_OK",
          "number": 3
        },
        {
          "name": "CONNECTION_QUALITY_GOOD",
          "number": 4
        },
        {
          "name": "CONNECTION_QUALITY_EXCELLENT",
          "number": 5
        }
      ],
      "options": {}
    },
    {
      "name": "ClientType",
      "value": [
        {
          "name": "CLIENT_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CLIENT_TYPE_WEB",
          "number": 1
        },
        {
          "name": "CLIENT_TYPE_IOS",
          "number": 2
        },
        {
          "name": "CLIENT_TYPE_ANDROID",
          "number": 3
        },
        {
          "name": "CLIENT_TYPE_UNKNOWN",
          "number": 4
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 344504.

```text
lIgaIAgGQAgEaB5KmHQMKAQFCLcq3LCkKBC9ycGMSDxINd3d3LmNoZXNzLmNvbRoNEgtiZWFyZXJfYXV0aCoBAWIGcHJvdG8z","chesscom/presence/v1/presence.proto":"CiNjaGVzc2NvbS9wcmVzZW5jZS92MS9wcmVzZW5jZS5wcm90bxIUY2hlc3Njb20ucHJlc2VuY2UudjEi0gUKDFVzZXJQcmVzZW5jZRIKCgJpZBgBIAEoCRI2CgZzdGF0dXMYAiABKA4yJi5jaGVzc2NvbS5wcmVzZW5jZS52MS5Db25uZWN0aW9uU3RhdHVzEi0KCXN0YXR1c19hdBgDIAEoCzIaLmdvb2dsZS5wcm90b2J1Zi5UaW1lc3RhbXASLgoKdXBkYXRlZF9hdBgEIAEoCz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17792"></a>
## FND-17792: Full frontend descriptor: chesscom/ratings/v2/rating.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/ratings/v2/rating.proto",
  "package": "chesscom.ratings.v2",
  "message_type": [
    {
      "name": "Rating",
      "field": [
        {
          "name": "value",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "deviation",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Decimal"
        },
        {
          "name": "timestamp",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_timestamp"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 347023.

```text
U9TEAISFwoTQ0xJRU5UX1RZUEVfQU5EUk9JRBADEhcKE0NMSUVOVF9UWVBFX1VOS05PV04QBBoIiqYdBAoCAQJiBnByb3RvMw","chesscom/ratings/v2/rating.proto":"CiBjaGVzc2NvbS9yYXRpbmdzL3YyL3JhdGluZy5wcm90bxITY2hlc3Njb20ucmF0aW5ncy52MiKPAQoGUmF0aW5nEg0KBXZhbHVlGAEgASgNEisKCWRldmlhdGlvbhgCIAEoCzIYLmNoZXNzY29tLmFwaS52MS5EZWNpbWFsEjIKCXRpbWVzdGFtcBgDIAEoCzIaLmdvb2dsZS5wcm90b2J1Zi5UaW1lc3RhbXBIAIgBAToHgqYdAwoBAUIMCgpfdGltZXN0YW1wYgZwcm90bzM","che
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17793"></a>
## FND-17793: Full frontend descriptor: chesscom/ratings/v2/variant_time_class_rating.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/ratings/v2/variant_time_class_rating.proto",
  "package": "chesscom.ratings.v2",
  "message_type": [
    {
      "name": "VariantTimeClassRating",
      "field": [
        {
          "name": "variant",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Variant"
        },
        {
          "name": "time_class",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.TimeClass"
        },
        {
          "name": "rating",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ratings.v2.Rating"
        }
      ]
    },
    {
      "name": "VariantTimeClassRatingGroup",
      "field": [
        {
          "name": "variant",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Variant"
        },
        {
          "name": "time_class_rating",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ratings.v2.TimeClassRating"
        }
      ],
      "options": {}
    },
    {
      "name": "TimeClassRating",
      "field": [
        {
          "name": "time_class",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.TimeClass"
        },
        {
          "name": "rating",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.ratings.v2.Rating"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 347340.

```text
FtcBgDIAEoCzIaLmdvb2dsZS5wcm90b2J1Zi5UaW1lc3RhbXBIAIgBAToHgqYdAwoBAUIMCgpfdGltZXN0YW1wYgZwcm90bzM","chesscom/ratings/v2/variant_time_class_rating.proto":"CjNjaGVzc2NvbS9yYXRpbmdzL3YyL3ZhcmlhbnRfdGltZV9jbGFzc19yYXRpbmcucHJvdG8SE2NoZXNzY29tLnJhdGluZ3MudjIipAEKFlZhcmlhbnRUaW1lQ2xhc3NSYXRpbmcSKwoHdmFyaWFudBgBIAEoDjIaLmNoZXNzY29tLmNoZXNzLnYxLlZhcmlhbnQSMAoKdGltZV9jbGFzcxgCIAEoDjIcLmNoZXNzY29tLmNoZXNzLnYxLlRpbWVDbGFzcxIrCg
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17794"></a>
## FND-17794: Full frontend descriptor: chesscom/user/v1/user_skill_level.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user/v1/user_skill_level.proto",
  "package": "chesscom.user.v1",
  "enum_type": [
    {
      "name": "SkillLevel",
      "value": [
        {
          "name": "SKILL_LEVEL_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SKILL_LEVEL_NEW",
          "number": 1
        },
        {
          "name": "SKILL_LEVEL_BEGINNER",
          "number": 2
        },
        {
          "name": "SKILL_LEVEL_INTERMEDIATE",
          "number": 3
        },
        {
          "name": "SKILL_LEVEL_ADVANCED",
          "number": 4
        },
        {
          "name": "SKILL_LEVEL_EXPERT",
          "number": 5
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 348095.

```text
S5UaW1lQ2xhc3MSKwoGcmF0aW5nGAIgASgLMhsuY2hlc3Njb20ucmF0aW5ncy52Mi5SYXRpbmc6B4KmHQMKAQFiBnByb3RvMw","chesscom/user/v1/user_skill_level.proto":"CidjaGVzc2NvbS91c2VyL3YxL3VzZXJfc2tpbGxfbGV2ZWwucHJvdG8SEGNoZXNzY29tLnVzZXIudjEqsQEKClNraWxsTGV2ZWwSGwoXU0tJTExfTEVWRUxfVU5TUEVDSUZJRUQQABITCg9TS0lMTF9MRVZFTF9ORVcQARIYChRTS0lMTF9MRVZFTF9CRUdJTk5FUhACEhwKGFNLSUxMX0xFVkVMX0lOVEVSTUVESUFURRADEhgKFFNLSUxMX0xFVkVMX0FEVkFOQ0VEEAQSFg
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17795"></a>
## FND-17795: Full frontend descriptor: chesscom/user_relationships/v2/user_relationships_model.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_relationships/v2/user_relationships_model.proto",
  "package": "chesscom.user_relationships.v2",
  "message_type": [
    {
      "name": "UserRelationship",
      "field": [
        {
          "name": "type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_relationships.v2.UserRelationshipType"
        },
        {
          "name": "direction",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_relationships.v2.UserRelationshipDirection"
        },
        {
          "name": "created_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        }
      ]
    },
    {
      "name": "UserRelationshipRequestCriteria",
      "field": [
        {
          "name": "relationship_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_relationships.v2.UserRelationshipType"
        },
        {
          "name": "direction",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_relationships.v2.UserRelationshipDirection"
        }
      ],
      "options": {}
    },
    {
      "name": "UserRelationshipInteraction",
      "field": [
        {
          "name": "type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_relationships.v2.UserRelationshipType"
        },
        {
          "name": "direction",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_relationships.v2.UserRelationshipDirection"
        },
        {
          "name": "created_at",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_created_at"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "UserRelationshipDirection",
      "value": [
        {
          "name": "USER_RELATIONSHIP_DIRECTION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "USER_RELATIONSHIP_DIRECTION_INCOMING",
          "number": 1
        },
        {
          "name": "USER_RELATIONSHIP_DIRECTION_OUTGOING",
          "number": 2
        },
        {
          "name": "USER_RELATIONSHIP_DIRECTION_MUTUAL",
          "number": 3
        }
      ],
      "options": {}
    },
    {
      "name": "UserRelationshipType",
      "value": [
        {
          "name": "USER_RELATIONSHIP_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "USER_RELATIONSHIP_TYPE_FRIENDSHIP",
          "number": 1
        },
        {
          "name": "USER_RELATIONSHIP_TYPE_BLOCK",
          "number": 2
        },
        {
          "name": "USER_RELATIONSHIP_TYPE_FRIEND_REQUEST",
          "number": 3
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 348470.

```text
UFURRADEhgKFFNLSUxMX0xFVkVMX0FEVkFOQ0VEEAQSFgoSU0tJTExfTEVWRUxfRVhQRVJUEAUaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_relationships/v2/user_relationships_model.proto":"Cj1jaGVzc2NvbS91c2VyX3JlbGF0aW9uc2hpcHMvdjIvdXNlcl9yZWxhdGlvbnNoaXBzX21vZGVsLnByb3RvEh5jaGVzc2NvbS51c2VyX3JlbGF0aW9uc2hpcHMudjIi1AEKEFVzZXJSZWxhdGlvbnNoaXASQgoEdHlwZRgBIAEoDjI0LmNoZXNzY29tLnVzZXJfcmVsYXRpb25zaGlwcy52Mi5Vc2VyUmVsYXRpb25zaGlwVHlwZRJMCglkaXJl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17796"></a>
## FND-17796: Full frontend descriptor: chesscom/user_relationships/v2/list_user_relationships_model.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_relationships/v2/list_user_relationships_model.proto",
  "package": "chesscom.user_relationships.v2",
  "message_type": [
    {
      "name": "ListableUserRelationship",
      "field": [
        {
          "name": "user_uuid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "created_at",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "user_relationship",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_relationships.v2.UserRelationshipType"
        },
        {
          "name": "direction",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_relationships.v2.UserRelationshipDirection"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 350104.

```text
9UWVBFX0JMT0NLEAISKQolVVNFUl9SRUxBVElPTlNISVBfVFlQRV9GUklFTkRfUkVRVUVTVBADGgeKph0DCgEBYgZwcm90bzM","chesscom/user_relationships/v2/list_user_relationships_model.proto":"CkJjaGVzc2NvbS91c2VyX3JlbGF0aW9uc2hpcHMvdjIvbGlzdF91c2VyX3JlbGF0aW9uc2hpcHNfbW9kZWwucHJvdG8SHmNoZXNzY29tLnVzZXJfcmVsYXRpb25zaGlwcy52MiKFAgoYTGlzdGFibGVVc2VyUmVsYXRpb25zaGlwEhEKCXVzZXJfdXVpZBgBIAEoCRIuCgpjcmVhdGVkX2F0GAIgASgLMhouZ29vZ2xlLnByb3RvYnVmLlR
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17797"></a>
## FND-17797: Full frontend descriptor: chesscom/navigation/v1/screen_entity.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/navigation/v1/screen_entity.proto",
  "package": "chesscom.navigation.v1",
  "message_type": [
    {
      "name": "ScreenEntity",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.navigation.v1.ScreenEntityType"
        },
        {
          "name": "name",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_name"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "ScreenEntityType",
      "value": [
        {
          "name": "SCREEN_ENTITY_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SCREEN_ENTITY_TYPE_FORUM_TOPIC",
          "number": 1
        },
        {
          "name": "SCREEN_ENTITY_TYPE_ARTICLE",
          "number": 2
        },
        {
          "name": "SCREEN_ENTITY_TYPE_NEWS_ARTICLE",
          "number": 3
        },
        {
          "name": "SCREEN_ENTITY_TYPE_EVENT",
          "number": 4
        },
        {
          "name": "SCREEN_ENTITY_TYPE_PLAYER",
          "number": 5
        },
        {
          "name": "SCREEN_ENTITY_TYPE_MEMBER",
          "number": 6
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 350672.

```text
jaGVzc2NvbS51c2VyX3JlbGF0aW9uc2hpcHMudjIuVXNlclJlbGF0aW9uc2hpcERpcmVjdGlvbjoHgqYdAwoBAWIGcHJvdG8z","chesscom/navigation/v1/screen_entity.proto":"CipjaGVzc2NvbS9uYXZpZ2F0aW9uL3YxL3NjcmVlbl9lbnRpdHkucHJvdG8SFmNoZXNzY29tLm5hdmlnYXRpb24udjEidwoMU2NyZWVuRW50aXR5EgoKAmlkGAEgASgJEjYKBHR5cGUYAiABKA4yKC5jaGVzc2NvbS5uYXZpZ2F0aW9uLnYxLlNjcmVlbkVudGl0eVR5cGUSEQoEbmFtZRgDIAEoCUgAiAEBOgeCph0DCgEBQgcKBV9uYW1lKoQCChBTY3JlZW5FbnRpdHl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17798"></a>
## FND-17798: Full frontend descriptor: chesscom/proto_options/user_activity_connector/v1/options.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/proto_options/user_activity_connector/v1/options.proto",
  "package": "chesscom.proto_options.user_activity_connector.v1",
  "message_type": [
    {
      "name": "UserActivityConnectorDefinition"
    }
  ],
  "extension": [
    {
      "name": "chart_color",
      "extendee": ".google.protobuf.EnumValueOptions",
      "number": 52000,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "json_name": "chartColor",
      "proto3_optional": true
    },
    {
      "name": "repository",
      "extendee": ".google.protobuf.EnumValueOptions",
      "number": 52001,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "json_name": "repository",
      "proto3_optional": true
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 351334.

```text
kVFTl9FTlRJVFlfVFlQRV9QTEFZRVIQBRIdChlTQ1JFRU5fRU5USVRZX1RZUEVfTUVNQkVSEAYaB4qmHQMKAQFiBnByb3RvMw","chesscom/proto_options/user_activity_connector/v1/options.proto":"Cj9jaGVzc2NvbS9wcm90b19vcHRpb25zL3VzZXJfYWN0aXZpdHlfY29ubmVjdG9yL3YxL29wdGlvbnMucHJvdG8SMWNoZXNzY29tLnByb3RvX29wdGlvbnMudXNlcl9hY3Rpdml0eV9jb25uZWN0b3IudjEiIQofVXNlckFjdGl2aXR5Q29ubmVjdG9yRGVmaW5pdGlvbjpHCgtjaGFydF9jb2xvchIhLmdvb2dsZS5wcm90b2J1Zi5FbnVtVm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17799"></a>
## FND-17799: Full frontend descriptor: chesscom/user_activity/v1/user_activity.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_activity/v1/user_activity.proto",
  "package": "chesscom.user_activity.v1",
  "message_type": [
    {
      "name": "TrackEvent",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "headers",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.EventHeaders"
        },
        {
          "name": "context",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Context"
        },
        {
          "name": "event_properties",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.TrackEvent.EventPropertiesEntry"
        },
        {
          "name": "user_properties",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.TrackEvent.UserPropertiesEntry"
        },
        {
          "name": "page",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Page",
          "oneof_index": 0
        },
        {
          "name": "screen",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Screen",
          "oneof_index": 0
        },
        {
          "name": "increment_properties",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.TrackEvent.IncrementPropertiesEntry"
        },
        {
          "name": "user_properties_cohorts",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.UserProperties",
          "options": {
            "deprecated": true
          },
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "enrichment_user_properties",
          "number": 10,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.TrackEvent.EnrichmentUserPropertiesEntry"
        }
      ],
      "nested_type": [
        {
          "name": "EventPropertiesEntry",
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
              "type": "TYPE_MESSAGE",
              "type_name": ".google.protobuf.Value"
            }
          ],
          "options": {
            "map_entry": true
          }
        },
        {
          "name": "UserPropertiesEntry",
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
              "type": "TYPE_MESSAGE",
              "type_name": ".google.protobuf.Value"
            }
          ],
          "options": {
            "map_entry": true
          }
        },
        {
          "name": "IncrementPropertiesEntry",
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
              "type": "TYPE_INT64"
            }
          ],
          "options": {
            "map_entry": true
          }
        },
        {
          "name": "EnrichmentUserPropertiesEntry",
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
              "type": "TYPE_MESSAGE",
              "type_name": ".google.protobuf.Value"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "source"
        },
        {
          "name": "_user_properties_cohorts"
        }
      ]
    },
    {
      "name": "TypedEvent",
      "field": [
        {
          "name": "event",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Any"
        },
        {
          "name": "headers",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.EventHeaders"
        },
        {
          "name": "context",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Context"
        },
        {
          "name": "page",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Page",
          "oneof_index": 0
        },
        {
          "name": "screen",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Screen",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "source"
        }
      ]
    },
    {
      "name": "IdentifyEvent",
      "field": [
        {
          "name": "headers",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.EventHeaders"
        },
        {
          "name": "context",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Context"
        },
        {
          "name": "user_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "user_properties",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.IdentifyEvent.UserPropertiesEntry"
        },
        {
          "name": "increment_properties",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.IdentifyEvent.IncrementPropertiesEntry"
        }
      ],
      "nested_type": [
        {
          "name": "UserPropertiesEntry",
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
              "type": "TYPE_MESSAGE",
              "type_name": ".google.protobuf.Value"
            }
          ],
          "options": {
            "map_entry": true
          }
        },
        {
          "name": "IncrementPropertiesEntry",
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
              "type": "TYPE_INT64"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {}
    },
    {
      "name": "NavigationEvent",
      "field": [
        {
          "name": "headers",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.EventHeaders"
        },
        {
          "name": "context",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Context"
        },
        {
          "name": "page",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Page",
          "oneof_index": 0
        },
        {
          "name": "screen",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Screen",
          "oneof_index": 0
        },
        {
          "name": "deeplink",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Deeplink",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "source"
        },
        {
          "name": "_deeplink"
        }
      ]
    },
    {
      "name": "Deeplink",
      "field": [
        {
          "name": "link",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "data",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Deeplink.DataEntry"
        }
      ],
      "nested_type": [
        {
          "name": "DataEntry",
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
              "type": "TYPE_MESSAGE",
              "type_name": ".google.protobuf.Value"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {}
    },
    {
      "name": "EventHeaders",
      "field": [
        {
          "name": "event_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "timestamp",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "local_time",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "user_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "legacy_user_id",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT64",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "sequence_number",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT64"
        },
        {
          "name": "sent_at",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "product_session_id",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "auth_user_id",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "event_trusted",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 6,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_local_time"
        },
        {
          "name": "_user_id"
        },
        {
          "name": "_legacy_user_id"
        },
        {
          "name": "_sent_at"
        },
        {
          "name": "_product_session_id"
        },
        {
          "name": "_auth_user_id"
        },
        {
          "name": "_event_trusted"
        }
      ]
    },
    {
      "name": "Context",
      "field": [
        {
          "name": "application",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_activity.v1.Application"
        },
        {
          "name": "client",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Client"
        },
        {
          "name": "library",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Library"
        },
        {
          "name": "ip",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "user_agent",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "campaign",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Campaign",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "location",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Location",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "network",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Network",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "os",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.OS",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "screen_resolution",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.ScreenResolution",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "device",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Device",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "language",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "bucketing_id",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "interaction_event_id",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "extensions",
          "number": 15,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Any"
        },
        {
          "name": "unified_screen",
          "number": 16,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_ip"
        },
        {
          "name": "_user_agent"
        },
        {
          "name": "_campaign"
        },
        {
          "name": "_location"
        },
        {
          "name": "_network"
        },
        {
          "name": "_os"
        },
        {
          "name": "_screen_resolution"
        },
        {
          "name": "_device"
        },
        {
          "name": "_language"
        },
        {
          "name": "_bucketing_id"
        },
        {
          "name": "_interaction_event_id"
        }
      ]
    },
    {
      "name": "Network",
      "field": [
        {
          "name": "type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "effective_type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "provider_name",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "Screen",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "properties",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_activity.v1.Screen.PropertiesEntry"
        },
        {
          "name": "entity",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.navigation.v1.ScreenEntity",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "nested_type": [
        {
          "name": "PropertiesEntry",
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
              "type": "TYPE_MESSAGE",
              "type_name": ".google.protobuf.Value"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_entity"
        }
      ]
    },
    {
      "name": "ScreenResolution",
      "field": [
        {
          "name": "width",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "height",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "dpi",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        }
      ],
      "options": {}
    },
    {
      "name": "Page",
      "field": [
        {
          "name": "host",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "path",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "title",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "referrer",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "search",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "hash",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "route_name",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "display_mode",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_activity.v1.DisplayMode",
          "oneof_index": 4,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_referrer"
        },
        {
          "name": "_search"
        },
        {
          "name": "_hash"
        },
        {
          "name": "_route_name"
        },
        {
          "name": "_display_mode"
        }
      ]
    },
    {
      "name": "OS",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "version",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "Library",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_activity.v1.Library.Name"
        },
        {
          "name": "version",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "enum_type": [
        {
          "name": "Name",
          "value": [
            {
              "name": "LIBRARY_NAME_UNSPECIFIED",
              "number": 0
            },
            {
              "name": "CHESSCOM_PHP_SDK",
              "number": 1,
              "options": {}
            },
            {
              "name": "CHESSCOM_IOS_SDK",
              "number": 2,
              "options": {}
            },
            {
              "name": "CHESSCOM_ANDROID_SDK",
              "number": 3,
              "options": {}
            },
            {
              "name": "CHESSCOM_JS_SDK",
              "number": 4,
              "options": {}
            },
            {
              "name": "CHESSCOM_JAVA_SDK",
              "number": 5,
              "options": {}
            },
            {
              "name": "CHESSCOM_COURSES_PHP_SDK",
              "number": 6,
              "options": {}
            }
          ]
        }
      ],
      "options": {}
    },
    {
      "name": "Device",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "manufacturer",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "model",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "type",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_activity.v1.DeviceType"
        },
        {
          "name": "brand",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_brand"
        }
      ]
    },
    {
      "name": "Campaign",
      "field": [
        {
          "name": "source",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "medium",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "term",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "content",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "campaign_id",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "template_id",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_campaign_id"
        },
        {
          "name": "_template_id"
        }
      ]
    },
    {
      "name": "Client",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_activity.v1.Client.Name"
        },
        {
          "name": "version",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "build",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "enum_type": [
        {
          "name": "Name",
          "value": [
            {
              "name": "CLIENT_NAME_UNSPECIFIED",
              "number": 0
            },
            {
              "name": "WEB",
              "number": 1
            },
            {
              "name": "IOS",
              "number": 2
            },
            {
              "name": "ANDROID",
              "number": 3
            },
            {
              "name": "USER_PROPERTIES",
              "number": 4
            },
            {
              "name": "ON_PLATFORM_MESSAGING",
              "number": 5
            },
            {
              "name": "WORKFLOWS",
              "number": 6
            },
            {
              "name": "COURSES",
              "number": 7
            },
            {
              "name": "RCN_SERVICE",
              "number": 8
            },
            {
              "name": "PROGRESSION_SERVICE",
              "number": 9
            },
            {
              "name": "ITERABLE_CONNECTOR",
              "number": 10
            },
            {
              "name": "SENDGRID_WEBHOOKS",
              "number": 11
            },
            {
              "name": "EMAIL_SENDER",
              "number": 12
            },
            {
              "name": "PUSH_SENDER",
              "number": 13
            }
          ]
        }
      ],
      "options": {}
    },
    {
      "name": "UserProperties",
      "field": [
        {
          "name": "client_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_activity.v1.Client.Name",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "country",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "skill_level",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user.v1.SkillLevel",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {
        "deprecated": true
      },
      "oneof_decl": [
        {
          "name": "_client_name"
        },
        {
          "name": "_country"
        },
        {
          "name": "_skill_level"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "DisplayMode",
      "value": [
        {
          "name": "DISPLAY_MODE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "DISPLAY_MODE_BROWSER",
          "number": 1
        },
        {
          "name": "DISPLAY_MODE_STANDALONE",
          "number": 2
        },
        {
          "name": "DISPLAY_MODE_FULLSCREEN",
          "number": 3
        },
        {
          "name": "DISPLAY_MODE_MINIMAL_UI",
          "number": 4
        }
      ],
      "options": {}
    },
    {
      "name": "DeviceType",
      "value": [
        {
          "name": "DEVICE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "DESKTOP",
          "number": 1
        },
        {
          "name": "MOBILE",
          "number": 2
        },
        {
          "name": "TABLET",
          "number": 3
        },
        {
          "name": "TV",
          "number": 4
        },
        {
          "name": "VR_HEADSET",
          "number": 5
        },
        {
          "name": "AR_HEADSET",
          "number": 6
        }
      ],
      "options": {}
    },
    {
      "name": "Destination",
      "value": [
        {
          "name": "DESTINATION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "DESTINATION_ITERABLE",
          "number": 1,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "DESTINATION_AMPLITUDE",
          "number": 2
        },
        {
          "name": "DESTINATION_BIGQUERY",
          "number": 3
        },
        {
          "name": "DESTINATION_WORKFLOWS",
          "number": 4
        },
        {
          "name": "DESTINATION_USER_PROPERTIES",
          "number": 5
        }
      ],
      "options": {}
    },
    {
      "name": "Application",
      "value": [
        {
          "name": "APPLICATION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "APPLICATION_CHESSCOM",
          "number": 1
        }
      ],
      "options": {}
    },
    {
      "name": "DestinationUpdateType",
      "value": [
        {
          "name": "DESTINATION_UPDATE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "DESTINATION_UPDATE_TYPE_ADDED",
          "number": 1
        },
        {
          "name": "DESTINATION_UPDATE_TYPE_REMOVED",
          "number": 2
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 351809.

```text
3NpdG9yeRIhLmdvb2dsZS5wcm90b2J1Zi5FbnVtVmFsdWVPcHRpb25zGKGWAyABKAlSCnJlcG9zaXRvcnmIAQFiBnByb3RvMw","chesscom/user_activity/v1/user_activity.proto":"Ci1jaGVzc2NvbS91c2VyX2FjdGl2aXR5L3YxL3VzZXJfYWN0aXZpdHkucHJvdG8SGWNoZXNzY29tLnVzZXJfYWN0aXZpdHkudjEimAgKClRyYWNrRXZlbnQSDAoEbmFtZRgBIAEoCRI4CgdoZWFkZXJzGAIgASgLMicuY2hlc3Njb20udXNlcl9hY3Rpdml0eS52MS5FdmVudEhlYWRlcnMSMwoHY29udGV4dBgDIAEoCzIiLmNoZXNzY29tLnVzZXJfYWN0aXZpdHku
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17800"></a>
## FND-17800: Full frontend descriptor: chesscom/user_targeting/v1/user_targeting.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_targeting/v1/user_targeting.proto",
  "package": "chesscom.user_targeting.v1",
  "message_type": [
    {
      "name": "Ruleset",
      "field": [
        {
          "name": "key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "enabled",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "criteria",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_targeting.v1.Criterion"
        },
        {
          "name": "logical_operator",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_targeting.v1.LogicalOperator",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "criteria_groups",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_targeting.v1.NestedCriteria"
        }
      ],
      "oneof_decl": [
        {
          "name": "_logical_operator"
        }
      ]
    },
    {
      "name": "Criterion",
      "field": [
        {
          "name": "user_property",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "binary_operator",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_targeting.v1.BinaryOperator"
        },
        {
          "name": "value",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "modifier",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_targeting.v1.BinaryOperatorModifier",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "key",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "second_value",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_value"
        },
        {
          "name": "_modifier"
        },
        {
          "name": "_second_value"
        }
      ]
    },
    {
      "name": "BinaryOperatorModifier",
      "field": [
        {
          "name": "is_negated",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "is_case_insensitive",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "time_unit",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_targeting.v1.TimeUnit",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "true_on_missing_values",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "relative",
          "number": 50,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_targeting.v1.RelativeTimeWindows",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0
        },
        {
          "name": "time_direction",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_targeting.v1.TimeDirection",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "second_time_unit",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_targeting.v1.TimeUnit",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "second_time_direction",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_targeting.v1.TimeDirection",
          "oneof_index": 7,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "time_windows"
        },
        {
          "name": "_is_negated"
        },
        {
          "name": "_is_case_insensitive"
        },
        {
          "name": "_time_unit"
        },
        {
          "name": "_true_on_missing_values"
        },
        {
          "name": "_time_direction"
        },
        {
          "name": "_second_time_unit"
        },
        {
          "name": "_second_time_direction"
        }
      ]
    },
    {
      "name": "NestedCriteriaModifier",
      "field": [
        {
          "name": "is_negated",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "related_with_entity_type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_targeting.v1.DataSourceType",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "min_relations_matching",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "max_relations_matching",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "data_source_identifier",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 4,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_is_negated"
        },
        {
          "name": "_related_with_entity_type"
        },
        {
          "name": "_min_relations_matching"
        },
        {
          "name": "_max_relations_matching"
        },
        {
          "name": "_data_source_identifier"
        }
      ]
    },
    {
      "name": "RelativeTimeWindows",
      "field": [
        {
          "name": "from",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "to",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "time_unit",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_targeting.v1.TimeUnit",
          "options": {
            "deprecated": true
          },
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {
        "deprecated": true
      },
      "oneof_decl": [
        {
          "name": "_from"
        },
        {
          "name": "_to"
        },
        {
          "name": "_time_unit"
        }
      ]
    },
    {
      "name": "NestedCriteria",
      "field": [
        {
          "name": "criteria_groups",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_targeting.v1.NestedCriteria"
        },
        {
          "name": "criteria",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_targeting.v1.Criterion"
        },
        {
          "name": "logical_operator",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_targeting.v1.LogicalOperator",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "modifier",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_targeting.v1.NestedCriteriaModifier",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_logical_operator"
        },
        {
          "name": "_modifier"
        }
      ]
    },
    {
      "name": "Sort",
      "field": [
        {
          "name": "key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "sort_order",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_targeting.v1.SortOrder",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_sort_order"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "BinaryOperator",
      "value": [
        {
          "name": "BINARY_OPERATOR_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GREATER",
          "number": 1
        },
        {
          "name": "GREATER_OR_EQUAL",
          "number": 2
        },
        {
          "name": "LESSER",
          "number": 3
        },
        {
          "name": "LESSER_OR_EQUAL",
          "number": 4
        },
        {
          "name": "EQUALS",
          "number": 5
        },
        {
          "name": "NOT_EQUALS",
          "number": 6
        },
        {
          "name": "CONTAINS",
          "number": 7
        },
        {
          "name": "DOES_NOT_CONTAIN",
          "number": 8
        },
        {
          "name": "WITHIN",
          "number": 9
        },
        {
          "name": "STARTS_WITH",
          "number": 10
        },
        {
          "name": "ENDS_WITH",
          "number": 11
        },
        {
          "name": "MATCHES",
          "number": 12
        },
        {
          "name": "NOT_WITHIN",
          "number": 13
        },
        {
          "name": "ANY_OF",
          "number": 14
        },
        {
          "name": "NONE_OF",
          "number": 15
        },
        {
          "name": "EXISTS",
          "number": 16
        },
        {
          "name": "NOT_EXISTS",
          "number": 17
        },
        {
          "name": "BETWEEN",
          "number": 18
        },
        {
          "name": "NOT_BETWEEN",
          "number": 19
        }
      ],
      "options": {}
    },
    {
      "name": "LogicalOperator",
      "value": [
        {
          "name": "LOGICAL_OPERATOR_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "AND",
          "number": 1
        },
        {
          "name": "OR",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "DataSourceType",
      "value": [
        {
          "name": "DATA_SOURCE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "EVENT",
          "number": 1
        },
        {
          "name": "EVENT_TYPE_TRACK",
          "number": 2
        },
        {
          "name": "EVENT_TYPE_TYPED",
          "number": 3
        },
        {
          "name": "TEMPORARY_USER_DATA",
          "number": 4
        }
      ],
      "options": {}
    },
    {
      "name": "TimeUnit",
      "value": [
        {
          "name": "TIME_UNIT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MILLISECONDS",
          "number": 1
        },
        {
          "name": "SECONDS",
          "number": 2
        },
        {
          "name": "MINUTES",
          "number": 3
        },
        {
          "name": "HOURS",
          "number": 4
        },
        {
          "name": "DAYS",
          "number": 5
        },
        {
          "name": "MONTHS",
          "number": 6
        },
        {
          "name": "YEARS",
          "number": 7
        }
      ],
      "options": {}
    },
    {
      "name": "TimeDirection",
      "value": [
        {
          "name": "TIME_DIRECTION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "LAST",
          "number": 1
        },
        {
          "name": "NEXT",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "SortOrder",
      "value": [
        {
          "name": "SORT_ORDER_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SORT_ORDER_ASC",
          "number": 1
        },
        {
          "name": "SORT_ORDER_DESC",
          "number": 2
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 360576.

```text
USU5BVElPTl9VUERBVEVfVFlQRV9BRERFRBABEiMKH0RFU1RJTkFUSU9OX1VQREFURV9UWVBFX1JFTU9WRUQQAmIGcHJvdG8z","chesscom/user_targeting/v1/user_targeting.proto":"Ci9jaGVzc2NvbS91c2VyX3RhcmdldGluZy92MS91c2VyX3RhcmdldGluZy5wcm90bxIaY2hlc3Njb20udXNlcl90YXJnZXRpbmcudjEilAIKB1J1bGVzZXQSCwoDa2V5GAEgASgJEgwKBG5hbWUYAiABKAkSDwoHZW5hYmxlZBgDIAEoCBI3Cghjcml0ZXJpYRgEIAMoCzIlLmNoZXNzY29tLnVzZXJfdGFyZ2V0aW5nLnYxLkNyaXRlcmlvbhJKChBsb2dpY2FsX2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17801"></a>
## FND-17801: Full frontend descriptor: chesscom/user_properties/v1/properties_definition.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_definition.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "PropertyDefinitionMetadata",
      "field": [
        {
          "name": "property_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "property_name_suffix",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "description",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "is_backfilled",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "repeated_limit",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "destination",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_activity.v1.Destination"
        },
        {
          "name": "deprecation_date",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "is_private",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "permission_level",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PropertyPermissionLevel",
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "user_activity_enrichment_field_name",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "range_transformer",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.RangeTransformer",
          "oneof_index": 0
        },
        {
          "name": "year_transformer",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.YearTransformer",
          "oneof_index": 0
        },
        {
          "name": "event_name_allowlist",
          "number": 13,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "customizable_views",
          "number": 14,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PropertyPermissionCustomizableView"
        }
      ],
      "oneof_decl": [
        {
          "name": "user_activity_enrichment_transformer"
        },
        {
          "name": "_property_name"
        },
        {
          "name": "_property_name_suffix"
        },
        {
          "name": "_description"
        },
        {
          "name": "_is_backfilled"
        },
        {
          "name": "_repeated_limit"
        },
        {
          "name": "_deprecation_date"
        },
        {
          "name": "_is_private"
        },
        {
          "name": "_permission_level"
        },
        {
          "name": "_user_activity_enrichment_field_name"
        }
      ]
    },
    {
      "name": "PropertyDefinition",
      "extension": [
        {
          "name": "metadata",
          "extendee": ".google.protobuf.EnumValueOptions",
          "number": 1000,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.PropertyDefinitionMetadata",
          "json_name": "metadata"
        }
      ]
    },
    {
      "name": "RangeTransformer",
      "field": [
        {
          "name": "range",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "range_modifier",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.RangeModifier",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_range_modifier"
        }
      ]
    },
    {
      "name": "YearTransformer"
    },
    {
      "name": "PropertyPermissionCustomizableView",
      "field": [
        {
          "name": "levels",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PropertyPermissionLevel"
        },
        {
          "name": "allowlist",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.AllowlistViewCustomization",
          "oneof_index": 0
        }
      ],
      "oneof_decl": [
        {
          "name": "customization"
        }
      ]
    },
    {
      "name": "AllowlistViewCustomization",
      "field": [
        {
          "name": "values",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "RangeModifier",
      "value": [
        {
          "name": "RANGE_MODIFIER_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "RANGE_MODIFIER_RANGE",
          "number": 1
        },
        {
          "name": "RANGE_MODIFIER_CEIL",
          "number": 2
        },
        {
          "name": "RANGE_MODIFIER_FLOOR",
          "number": 3
        }
      ]
    },
    {
      "name": "PropertyPermissionLevel",
      "value": [
        {
          "name": "PROPERTY_PERMISSION_LEVEL_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PROPERTY_PERMISSION_LEVEL_PRIVATE",
          "number": 1
        },
        {
          "name": "PROPERTY_PERMISSION_LEVEL_SELF",
          "number": 2
        },
        {
          "name": "PROPERTY_PERMISSION_LEVEL_FRIENDS",
          "number": 3
        },
        {
          "name": "PROPERTY_PERMISSION_LEVEL_PUBLIC",
          "number": 4
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 364853.

```text
TT1JUX09SREVSX1VOU1BFQ0lGSUVEEAASEgoOU09SVF9PUkRFUl9BU0MQARITCg9TT1JUX09SREVSX0RFU0MQAmIGcHJvdG8z","chesscom/user_properties/v1/properties_definition.proto":"CjdjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19kZWZpbml0aW9uLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEiwAcKGlByb3BlcnR5RGVmaW5pdGlvbk1ldGFkYXRhEhoKDXByb3BlcnR5X25hbWUYASABKAlIAYgBARIhChRwcm9wZXJ0eV9uYW1lX3N1ZmZpeBgCIAEoCUgCiAEBEhgKC2Rlc2NyaXB0aW9uGA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17802"></a>
## FND-17802: Full frontend descriptor: chesscom/user_properties/v1/properties_core.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_core.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "CoreProperty",
      "field": [
        {
          "name": "user_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT64",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "username",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "created_at",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "updated_at",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "timezone",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "chess_title",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "flair_code",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "is_enabled",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "bitset_offset_number",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "user_uuid",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "previous_usernames",
          "number": 12,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "flair_id",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "flair_png_url",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "registration_platform",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 13,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1001,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.CorePropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_id"
        },
        {
          "name": "_username"
        },
        {
          "name": "_type"
        },
        {
          "name": "_created_at"
        },
        {
          "name": "_updated_at"
        },
        {
          "name": "_timezone"
        },
        {
          "name": "_chess_title"
        },
        {
          "name": "_flair_code"
        },
        {
          "name": "_is_enabled"
        },
        {
          "name": "_bitset_offset_number"
        },
        {
          "name": "_user_uuid"
        },
        {
          "name": "_flair_id"
        },
        {
          "name": "_flair_png_url"
        },
        {
          "name": "_registration_platform"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "CorePropertyDefinition",
      "value": [
        {
          "name": "CORE_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "USER_ID",
          "number": 1,
          "options": {}
        },
        {
          "name": "USERNAME",
          "number": 2,
          "options": {}
        },
        {
          "name": "TYPE",
          "number": 3,
          "options": {}
        },
        {
          "name": "CREATED_AT",
          "number": 4,
          "options": {}
        },
        {
          "name": "UPDATED_AT",
          "number": 5,
          "options": {}
        },
        {
          "name": "TIMEZONE",
          "number": 6,
          "options": {}
        },
        {
          "name": "CHESS_TITLE",
          "number": 7,
          "options": {}
        },
        {
          "name": "FLAIR_CODE",
          "number": 8,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "IS_ENABLED",
          "number": 9,
          "options": {}
        },
        {
          "name": "BITSET_OFFSET_NUMBER",
          "number": 10,
          "options": {}
        },
        {
          "name": "USER_UUID",
          "number": 11,
          "options": {}
        },
        {
          "name": "PREVIOUS_USERNAMES",
          "number": 12,
          "options": {}
        },
        {
          "name": "FLAIR_ID",
          "number": 13,
          "options": {}
        },
        {
          "name": "FLAIR_PNG_URL",
          "number": 14,
          "options": {}
        },
        {
          "name": "REGISTRATION_PLATFORM",
          "number": 15,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 367509.

```text
9QRVJNSVNTSU9OX0xFVkVMX0ZSSUVORFMQAxIkCiBQUk9QRVJUWV9QRVJNSVNTSU9OX0xFVkVMX1BVQkxJQxAEYgZwcm90bzM","chesscom/user_properties/v1/properties_core.proto":"CjFjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19jb3JlLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEi7wYKDENvcmVQcm9wZXJ0eRIZCgd1c2VyX2lkGAEgASgEQgPIPgFIAIgBARIaCgh1c2VybmFtZRgCIAEoCUIDyD4CSAGIAQESFgoEdHlwZRgDIAEoCUIDyD4DSAKIAQESOAoKY3JlYXRlZF9hdBgEIAEoCzIaLmdv
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17803"></a>
## FND-17803: Full frontend descriptor: chesscom/user_properties/v1/properties_pii.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_pii.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "PIIProperty",
      "field": [
        {
          "name": "email",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "first_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "last_name",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "country",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "last_country",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "last_ip_address",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "last_timezone",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "last_continent",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "last_city",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "last_region",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "last_latitude",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "last_longitude",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "previous_emails",
          "number": 13,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "payment_country",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "payment_country_confidence_level",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "paypal_emails",
          "number": 16,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "phone_number",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "previous_phone_numbers",
          "number": 18,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "uscf_id",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "fide_id",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "options": {},
          "oneof_index": 16,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1002,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PIIPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_email"
        },
        {
          "name": "_first_name"
        },
        {
          "name": "_last_name"
        },
        {
          "name": "_country"
        },
        {
          "name": "_last_country"
        },
        {
          "name": "_last_ip_address"
        },
        {
          "name": "_last_timezone"
        },
        {
          "name": "_last_continent"
        },
        {
          "name": "_last_city"
        },
        {
          "name": "_last_region"
        },
        {
          "name": "_last_latitude"
        },
        {
          "name": "_last_longitude"
        },
        {
          "name": "_payment_country"
        },
        {
          "name": "_payment_country_confidence_level"
        },
        {
          "name": "_phone_number"
        },
        {
          "name": "_uscf_id"
        },
        {
          "name": "_fide_id"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "PIIPropertyDefinition",
      "value": [
        {
          "name": "PII_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "EMAIL",
          "number": 1,
          "options": {}
        },
        {
          "name": "FIRST_NAME",
          "number": 2,
          "options": {}
        },
        {
          "name": "LAST_NAME",
          "number": 3,
          "options": {}
        },
        {
          "name": "COUNTRY",
          "number": 4,
          "options": {}
        },
        {
          "name": "LAST_COUNTRY",
          "number": 5,
          "options": {}
        },
        {
          "name": "LAST_IP_ADDRESS",
          "number": 6,
          "options": {}
        },
        {
          "name": "LAST_TIMEZONE",
          "number": 7,
          "options": {}
        },
        {
          "name": "LAST_CONTINENT",
          "number": 8,
          "options": {}
        },
        {
          "name": "LAST_CITY",
          "number": 9,
          "options": {}
        },
        {
          "name": "LAST_REGION",
          "number": 10,
          "options": {}
        },
        {
          "name": "LAST_LATITUDE",
          "number": 11,
          "options": {}
        },
        {
          "name": "LAST_LONGITUDE",
          "number": 12,
          "options": {}
        },
        {
          "name": "PREVIOUS_EMAILS",
          "number": 13,
          "options": {}
        },
        {
          "name": "PAYMENT_COUNTRY",
          "number": 14,
          "options": {}
        },
        {
          "name": "PAYMENT_COUNTRY_CONFIDENCE_LEVEL",
          "number": 15,
          "options": {}
        },
        {
          "name": "PAYPAL_EMAILS",
          "number": 16,
          "options": {}
        },
        {
          "name": "PHONE_NUMBER",
          "number": 17,
          "options": {}
        },
        {
          "name": "PREVIOUS_PHONE_NUMBERS",
          "number": 18,
          "options": {}
        },
        {
          "name": "USCF_ID",
          "number": 19,
          "options": {}
        },
        {
          "name": "FIDE_ID",
          "number": 20,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 369738.

```text
m0vY2xpZW50IHVzZWQgZHVyaW5nIHJlZ2lzdHJhdGlvbiAod2VifGlPU3xBbmRyb2lkKSAASAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_pii.proto":"CjBjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19waWkucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSKsCAoLUElJUHJvcGVydHkSFwoFZW1haWwYASABKAlCA9A+AUgAiAEBEhwKCmZpcnN0X25hbWUYAiABKAlCA9A+AkgBiAEBEhsKCWxhc3RfbmFtZRgDIAEoCUID0D4DSAKIAQESGQoHY291bnRyeRgEIAEoCUID0D4ES
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17804"></a>
## FND-17804: Full frontend descriptor: chesscom/user_properties/v1/properties_user_details.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_user_details.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "UserDetailsProperty",
      "field": [
        {
          "name": "avatar_url",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "high_res_avatar_url",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "content_language_includes_english",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "is_email_deliverable",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "is_activated",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "has_opened_verification_email",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "referred_by_method",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "is_content_hidden",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "is_verified",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "has_sendgrid_invalid_email",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "last_bounce_date",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "last_open_email_date",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "last_dropped_email_date",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "last_spam_report_date",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "is_pawniversary",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "is_reactivated",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "skill_level",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "last_click_email_date",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "is_on_do_not_email_list",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "is_pawniversary_tomorrow",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "is_guest",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "user_right_to_be_forgotten_status",
          "number": 25,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "next_pawniversary_start_date",
          "number": 26,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 22,
          "proto3_optional": true
        },
        {
          "name": "experiment_bucketing_results",
          "number": 27,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "opt_in_status",
          "number": 28,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 23,
          "proto3_optional": true
        },
        {
          "name": "account_status",
          "number": 29,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 24,
          "proto3_optional": true
        },
        {
          "name": "closure_type",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 25,
          "proto3_optional": true
        },
        {
          "name": "closure_reason",
          "number": 31,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 26,
          "proto3_optional": true
        },
        {
          "name": "activation_type",
          "number": 32,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 27,
          "proto3_optional": true
        },
        {
          "name": "has_avatar",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 28,
          "proto3_optional": true
        },
        {
          "name": "language",
          "number": 34,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 29,
          "proto3_optional": true
        },
        {
          "name": "language_cloudflare",
          "number": 35,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 30,
          "proto3_optional": true
        },
        {
          "name": "has_fcm_token",
          "number": 36,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 31,
          "proto3_optional": true
        },
        {
          "name": "has_ios_fcm_token",
          "number": 37,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 32,
          "proto3_optional": true
        },
        {
          "name": "has_android_fcm_token",
          "number": 38,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 33,
          "proto3_optional": true
        },
        {
          "name": "has_web_fcm_token",
          "number": 39,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 34,
          "proto3_optional": true
        },
        {
          "name": "experiment_bucketing_id",
          "number": 40,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 35,
          "proto3_optional": true
        },
        {
          "name": "lists_member_of",
          "number": 41,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "is_bot",
          "number": 42,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 36,
          "proto3_optional": true
        },
        {
          "name": "trust_level",
          "number": 43,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 37,
          "proto3_optional": true
        },
        {
          "name": "pawniversary_years",
          "number": 44,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 38,
          "proto3_optional": true
        },
        {
          "name": "initial_rating",
          "number": 45,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 39,
          "proto3_optional": true
        },
        {
          "name": "is_trusted",
          "number": 46,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 40,
          "proto3_optional": true
        },
        {
          "name": "has_twitch_connection",
          "number": 47,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 41,
          "proto3_optional": true
        },
        {
          "name": "has_youtube_connection",
          "number": 48,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 42,
          "proto3_optional": true
        },
        {
          "name": "blog_id",
          "number": 49,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 43,
          "proto3_optional": true
        },
        {
          "name": "stream_url",
          "number": 50,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 44,
          "proto3_optional": true
        },
        {
          "name": "closure_status",
          "number": 51,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 45,
          "proto3_optional": true
        },
        {
          "name": "temporary_datasets_member_of",
          "number": 52,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "is_beta",
          "number": 53,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 46,
          "proto3_optional": true
        },
        {
          "name": "has_linkedin_connection",
          "number": 54,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 47,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1003,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.UserDetailsPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_avatar_url"
        },
        {
          "name": "_high_res_avatar_url"
        },
        {
          "name": "_content_language_includes_english"
        },
        {
          "name": "_is_email_deliverable"
        },
        {
          "name": "_is_activated"
        },
        {
          "name": "_has_opened_verification_email"
        },
        {
          "name": "_referred_by_method"
        },
        {
          "name": "_is_content_hidden"
        },
        {
          "name": "_is_verified"
        },
        {
          "name": "_has_sendgrid_invalid_email"
        },
        {
          "name": "_last_bounce_date"
        },
        {
          "name": "_last_open_email_date"
        },
        {
          "name": "_last_dropped_email_date"
        },
        {
          "name": "_last_spam_report_date"
        },
        {
          "name": "_is_pawniversary"
        },
        {
          "name": "_is_reactivated"
        },
        {
          "name": "_skill_level"
        },
        {
          "name": "_last_click_email_date"
        },
        {
          "name": "_is_on_do_not_email_list"
        },
        {
          "name": "_is_pawniversary_tomorrow"
        },
        {
          "name": "_is_guest"
        },
        {
          "name": "_user_right_to_be_forgotten_status"
        },
        {
          "name": "_next_pawniversary_start_date"
        },
        {
          "name": "_opt_in_status"
        },
        {
          "name": "_account_status"
        },
        {
          "name": "_closure_type"
        },
        {
          "name": "_closure_reason"
        },
        {
          "name": "_activation_type"
        },
        {
          "name": "_has_avatar"
        },
        {
          "name": "_language"
        },
        {
          "name": "_language_cloudflare"
        },
        {
          "name": "_has_fcm_token"
        },
        {
          "name": "_has_ios_fcm_token"
        },
        {
          "name": "_has_android_fcm_token"
        },
        {
          "name": "_has_web_fcm_token"
        },
        {
          "name": "_experiment_bucketing_id"
        },
        {
          "name": "_is_bot"
        },
        {
          "name": "_trust_level"
        },
        {
          "name": "_pawniversary_years"
        },
        {
          "name": "_initial_rating"
        },
        {
          "name": "_is_trusted"
        },
        {
          "name": "_has_twitch_connection"
        },
        {
          "name": "_has_youtube_connection"
        },
        {
          "name": "_blog_id"
        },
        {
          "name": "_stream_url"
        },
        {
          "name": "_closure_status"
        },
        {
          "name": "_is_beta"
        },
        {
          "name": "_has_linkedin_connection"
        }
      ],
      "reserved_range": [
        {
          "start": 7,
          "end": 8
        },
        {
          "start": 8,
          "end": 9
        },
        {
          "start": 24,
          "end": 25
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "UserDetailsPropertyDefinition",
      "value": [
        {
          "name": "USER_DETAILS_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "AVATAR_URL",
          "number": 1,
          "options": {}
        },
        {
          "name": "HIGH_RES_AVATAR_URL",
          "number": 2,
          "options": {}
        },
        {
          "name": "CONTENT_LANGUAGE_INCLUDES_ENGLISH",
          "number": 3,
          "options": {}
        },
        {
          "name": "IS_EMAIL_DELIVERABLE",
          "number": 4,
          "options": {}
        },
        {
          "name": "IS_ACTIVATED",
          "number": 5,
          "options": {}
        },
        {
          "name": "HAS_OPENED_VERIFICATION_EMAIL",
          "number": 6,
          "options": {}
        },
        {
          "name": "REFERRED_BY_METHOD",
          "number": 9,
          "options": {}
        },
        {
          "name": "IS_CONTENT_HIDDEN",
          "number": 10,
          "options": {}
        },
        {
          "name": "IS_VERIFIED",
          "number": 11,
          "options": {}
        },
        {
          "name": "HAS_SENDGRID_INVALID_EMAIL",
          "number": 12,
          "options": {}
        },
        {
          "name": "LAST_BOUNCE_DATE",
          "number": 13,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "LAST_OPEN_EMAIL_DATE",
          "number": 14,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "LAST_DROPPED_EMAIL_DATE",
          "number": 15,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "LAST_SPAM_REPORT_DATE",
          "number": 16,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "IS_PAWNIVERSARY",
          "number": 17,
          "options": {}
        },
        {
          "name": "IS_REACTIVATED",
          "number": 18,
          "options": {}
        },
        {
          "name": "SKILL_LEVEL",
          "number": 19,
          "options": {}
        },
        {
          "name": "LAST_CLICK_EMAIL_DATE",
          "number": 20,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "IS_ON_DO_NOT_EMAIL_LIST",
          "number": 21,
          "options": {}
        },
        {
          "name": "IS_PAWNIVERSARY_TOMORROW",
          "number": 22,
          "options": {}
        },
        {
          "name": "IS_GUEST",
          "number": 23,
          "options": {}
        },
        {
          "name": "USER_RIGHT_TO_BE_FORGOTTEN_STATUS",
          "number": 25,
          "options": {}
        },
        {
          "name": "NEXT_PAWNIVERSARY_START_DATE",
          "number": 26,
          "options": {}
        },
        {
          "name": "EXPERIMENT_BUCKETING_RESULTS",
          "number": 27,
          "options": {}
        },
        {
          "name": "OPT_IN_STATUS",
          "number": 28,
          "options": {}
        },
        {
          "name": "ACCOUNT_STATUS",
          "number": 29,
          "options": {}
        },
        {
          "name": "CLOSURE_TYPE",
          "number": 30,
          "options": {}
        },
        {
          "name": "CLOSURE_REASON",
          "number": 31,
          "options": {}
        },
        {
          "name": "ACTIVATION_TYPE",
          "number": 32,
          "options": {}
        },
        {
          "name": "HAS_AVATAR",
          "number": 33,
          "options": {}
        },
        {
          "name": "LANGUAGE",
          "number": 34,
          "options": {}
        },
        {
          "name": "LANGUAGE_CLOUDFLARE",
          "number": 35,
          "options": {}
        },
        {
          "name": "HAS_FCM_TOKEN",
          "number": 36,
          "options": {}
        },
        {
          "name": "HAS_IOS_FCM_TOKEN",
          "number": 37,
          "options": {}
        },
        {
          "name": "HAS_ANDROID_FCM_TOKEN",
          "number": 38,
          "options": {}
        },
        {
          "name": "HAS_WEB_FCM_TOKEN",
          "number": 39,
          "options": {}
        },
        {
          "name": "EXPERIMENT_BUCKETING_ID",
          "number": 40,
          "options": {}
        },
        {
          "name": "LISTS_MEMBER_OF",
          "number": 41,
          "options": {}
        },
        {
          "name": "IS_BOT",
          "number": 42,
          "options": {}
        },
        {
          "name": "TRUST_LEVEL",
          "number": 43,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "PAWNIVERSARY_YEARS",
          "number": 44,
          "options": {}
        },
        {
          "name": "INITIAL_RATING",
          "number": 45,
          "options": {}
        },
        {
          "name": "IS_TRUSTED",
          "number": 46,
          "options": {}
        },
        {
          "name": "HAS_TWITCH_CONNECTION",
          "number": 47,
          "options": {}
        },
        {
          "name": "HAS_YOUTUBE_CONNECTION",
          "number": 48,
          "options": {}
        },
        {
          "name": "BLOG_ID",
          "number": 49,
          "options": {}
        },
        {
          "name": "STREAM_URL",
          "number": 50,
          "options": {}
        },
        {
          "name": "CLOSURE_STATUS",
          "number": 51,
          "options": {}
        },
        {
          "name": "TEMPORARY_DATASETS_MEMBER_OF",
          "number": 52,
          "options": {}
        },
        {
          "name": "IS_BETA",
          "number": 53,
          "options": {}
        },
        {
          "name": "HAS_LINKEDIN_CONNECTION",
          "number": 54,
          "options": {}
        }
      ],
      "options": {},
      "reserved_range": [
        {
          "start": 7,
          "end": 7
        },
        {
          "start": 8,
          "end": 8
        },
        {
          "start": 24,
          "end": 24
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 372748.

```text
EEBQaM8I+MBoqUGxheWVyJ3MgSW50ZXJuYXRpb25hbCBDaGVzcyBGZWRlcmF0aW9uIElEIABAARoHiqYdAwoBAWIGcHJvdG8z","chesscom/user_properties/v1/properties_user_details.proto":"CjljaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc191c2VyX2RldGFpbHMucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSLaGQoTVXNlckRldGFpbHNQcm9wZXJ0eRIcCgphdmF0YXJfdXJsGAEgASgJQgPYPgFIAIgBARIlChNoaWdoX3Jlc19hdmF0YXJfdXJsGAIgASgJQgPYPgJIAYgBARIzCiFjb250ZW50X2xh
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17805"></a>
## FND-17805: Full frontend descriptor: chesscom/user_properties/v1/properties_roles.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_roles.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "RolesProperty",
      "field": [
        {
          "name": "is_streamer",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "roles",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "trust_level",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "is_affiliate_enabled",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1004,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.RolesPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_is_streamer"
        },
        {
          "name": "_trust_level"
        },
        {
          "name": "_is_affiliate_enabled"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "RolesPropertyDefinition",
      "value": [
        {
          "name": "ROLES_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "IS_STREAMER",
          "number": 1,
          "options": {}
        },
        {
          "name": "ROLES",
          "number": 2,
          "options": {}
        },
        {
          "name": "ROLES_TRUST_LEVEL",
          "number": 3,
          "options": {}
        },
        {
          "name": "IS_AFFILIATE_ENABLED",
          "number": 4,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 382345.

```text
yBjb25uZWN0ZWQgdGhlaXIgTGlua2VkSW4gYWNjb3VudCABSAQaB4qmHQMKAQEiBAgHEAciBAgIEAgiBAgYEBhiBnByb3RvMw","chesscom/user_properties/v1/properties_roles.proto":"CjJjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19yb2xlcy5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIsECCg1Sb2xlc1Byb3BlcnR5Eh0KC2lzX3N0cmVhbWVyGAEgASgIQgPgPgFIAIgBARISCgVyb2xlcxgCIAMoCUID4D4CEh0KC3RydXN0X2xldmVsGAMgASgFQgPgPgNIAYgBARImChRpc19hZmZpbGlhdGVfZW5
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17806"></a>
## FND-17806: Full frontend descriptor: chesscom/user_properties/v1/properties_activity.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_activity.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "ActivityProperty",
      "field": [
        {
          "name": "last_login_date",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "last_game_played",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "last_game_finished",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "last_stream_date",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "total_time_spent",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "total_logins",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "total_video_views",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "profile_view_count",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "is_in_iterable",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "activity_streak_count",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {
            "deprecated": true
          },
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "activity_streak_max_count",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {
            "deprecated": true
          },
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "activity_streak_is_frozen",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "activity_streak_days",
          "number": 13,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "activity_streak_frozen_days",
          "number": 14,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "activity_streak_last_update_date",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "last_used_client",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "has_used_web_client",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "has_used_ios_client",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "has_used_android_client",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "friends_count",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "activity_streak_max_count_day",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "total_trophies_received",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "total_lessons_completed",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "total_courses_completed",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "activity_streak_last_notification_date",
          "number": 25,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 22,
          "proto3_optional": true
        },
        {
          "name": "last_friend_added_date",
          "number": 26,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 23,
          "proto3_optional": true
        },
        {
          "name": "activity_streak_last_reminder_sent_date",
          "number": 27,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 24,
          "proto3_optional": true
        },
        {
          "name": "total_lessons_attempted",
          "number": 28,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 25,
          "proto3_optional": true
        },
        {
          "name": "total_courses_attempted",
          "number": 29,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 26,
          "proto3_optional": true
        },
        {
          "name": "last_attempted_lesson_uuid",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 27,
          "proto3_optional": true
        },
        {
          "name": "last_attempted_course_uuid",
          "number": 31,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 28,
          "proto3_optional": true
        },
        {
          "name": "last_completed_lesson_uuid",
          "number": 32,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 29,
          "proto3_optional": true
        },
        {
          "name": "last_completed_course_uuid",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 30,
          "proto3_optional": true
        },
        {
          "name": "last_lesson_attempted_date",
          "number": 34,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 31,
          "proto3_optional": true
        },
        {
          "name": "last_course_attempted_date",
          "number": 35,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 32,
          "proto3_optional": true
        },
        {
          "name": "last_lesson_completed_date",
          "number": 36,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 33,
          "proto3_optional": true
        },
        {
          "name": "last_course_completed_date",
          "number": 37,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 34,
          "proto3_optional": true
        },
        {
          "name": "completed_lesson_level_ids",
          "number": 38,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32",
          "options": {}
        },
        {
          "name": "completed_lesson_max_level_id",
          "number": 39,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 35,
          "proto3_optional": true
        },
        {
          "name": "last_lesson_completed_dates",
          "number": 40,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {}
        },
        {
          "name": "last_lesson_history_reset_date",
          "number": 41,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 36,
          "proto3_optional": true
        },
        {
          "name": "blocked_by_count",
          "number": 42,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 37,
          "proto3_optional": true
        },
        {
          "name": "last_session_start_date",
          "number": 43,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 38,
          "proto3_optional": true
        },
        {
          "name": "last_session_end_date",
          "number": 44,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 39,
          "proto3_optional": true
        },
        {
          "name": "daily_games_in_progress_count",
          "number": 45,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 40,
          "proto3_optional": true
        },
        {
          "name": "daily_games_chess_in_progress_to_move",
          "number": 46,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 41,
          "proto3_optional": true
        },
        {
          "name": "daily_games_chess960_in_progress_to_move",
          "number": 47,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 42,
          "proto3_optional": true
        },
        {
          "name": "daily_games_chess_time_percentage_used_to_move",
          "number": 48,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 43,
          "proto3_optional": true
        },
        {
          "name": "daily_games_chess960_time_percentage_used_to_move",
          "number": 49,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 44,
          "proto3_optional": true
        },
        {
          "name": "daily_games_chess_in_progress_ids",
          "number": 50,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "daily_games_chess960_in_progress_ids",
          "number": 51,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "old_mobile_client_played_on_lc_date",
          "number": 52,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 45,
          "proto3_optional": true
        },
        {
          "name": "blocked_count",
          "number": 53,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 46,
          "proto3_optional": true
        },
        {
          "name": "last_friend_removed_date",
          "number": 54,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 47,
          "proto3_optional": true
        },
        {
          "name": "added_to_iterable_date",
          "number": 55,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 48,
          "proto3_optional": true
        },
        {
          "name": "last_ios_version_used",
          "number": 56,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 49,
          "proto3_optional": true
        },
        {
          "name": "last_android_version_used",
          "number": 57,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 50,
          "proto3_optional": true
        },
        {
          "name": "last_web_version_used",
          "number": 58,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 51,
          "proto3_optional": true
        },
        {
          "name": "learn_path_completed_date",
          "number": 59,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 52,
          "proto3_optional": true
        },
        {
          "name": "last_game_vs_computer_finished",
          "number": 60,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 53,
          "proto3_optional": true
        },
        {
          "name": "last_live_time_controls",
          "number": 61,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1005,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.ActivityPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_last_login_date"
        },
        {
          "name": "_last_game_played"
        },
        {
          "name": "_last_game_finished"
        },
        {
          "name": "_last_stream_date"
        },
        {
          "name": "_total_time_spent"
        },
        {
          "name": "_total_logins"
        },
        {
          "name": "_total_video_views"
        },
        {
          "name": "_profile_view_count"
        },
        {
          "name": "_is_in_iterable"
        },
        {
          "name": "_activity_streak_count"
        },
        {
          "name": "_activity_streak_max_count"
        },
        {
          "name": "_activity_streak_is_frozen"
        },
        {
          "name": "_activity_streak_last_update_date"
        },
        {
          "name": "_last_used_client"
        },
        {
          "name": "_has_used_web_client"
        },
        {
          "name": "_has_used_ios_client"
        },
        {
          "name": "_has_used_android_client"
        },
        {
          "name": "_friends_count"
        },
        {
          "name": "_activity_streak_max_count_day"
        },
        {
          "name": "_total_trophies_received"
        },
        {
          "name": "_total_lessons_completed"
        },
        {
          "name": "_total_courses_completed"
        },
        {
          "name": "_activity_streak_last_notification_date"
        },
        {
          "name": "_last_friend_added_date"
        },
        {
          "name": "_activity_streak_last_reminder_sent_date"
        },
        {
          "name": "_total_lessons_attempted"
        },
        {
          "name": "_total_courses_attempted"
        },
        {
          "name": "_last_attempted_lesson_uuid"
        },
        {
          "name": "_last_attempted_course_uuid"
        },
        {
          "name": "_last_completed_lesson_uuid"
        },
        {
          "name": "_last_completed_course_uuid"
        },
        {
          "name": "_last_lesson_attempted_date"
        },
        {
          "name": "_last_course_attempted_date"
        },
        {
          "name": "_last_lesson_completed_date"
        },
        {
          "name": "_last_course_completed_date"
        },
        {
          "name": "_completed_lesson_max_level_id"
        },
        {
          "name": "_last_lesson_history_reset_date"
        },
        {
          "name": "_blocked_by_count"
        },
        {
          "name": "_last_session_start_date"
        },
        {
          "name": "_last_session_end_date"
        },
        {
          "name": "_daily_games_in_progress_count"
        },
        {
          "name": "_daily_games_chess_in_progress_to_move"
        },
        {
          "name": "_daily_games_chess960_in_progress_to_move"
        },
        {
          "name": "_daily_games_chess_time_percentage_used_to_move"
        },
        {
          "name": "_daily_games_chess960_time_percentage_used_to_move"
        },
        {
          "name": "_old_mobile_client_played_on_lc_date"
        },
        {
          "name": "_blocked_count"
        },
        {
          "name": "_last_friend_removed_date"
        },
        {
          "name": "_added_to_iterable_date"
        },
        {
          "name": "_last_ios_version_used"
        },
        {
          "name": "_last_android_version_used"
        },
        {
          "name": "_last_web_version_used"
        },
        {
          "name": "_learn_path_completed_date"
        },
        {
          "name": "_last_game_vs_computer_finished"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "ActivityPropertyDefinition",
      "value": [
        {
          "name": "ACTIVITY_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "LAST_LOGIN_DATE",
          "number": 1,
          "options": {}
        },
        {
          "name": "LAST_GAME_PLAYED",
          "number": 2,
          "options": {}
        },
        {
          "name": "LAST_GAME_FINISHED",
          "number": 3,
          "options": {}
        },
        {
          "name": "LAST_STREAM_DATE",
          "number": 4,
          "options": {}
        },
        {
          "name": "TOTAL_TIME_SPENT",
          "number": 5,
          "options": {}
        },
        {
          "name": "TOTAL_LOGINS",
          "number": 6,
          "options": {}
        },
        {
          "name": "TOTAL_VIDEO_VIEWS",
          "number": 7,
          "options": {}
        },
        {
          "name": "PROFILE_VIEW_COUNT",
          "number": 8,
          "options": {}
        },
        {
          "name": "IS_IN_ITERABLE",
          "number": 9,
          "options": {}
        },
        {
          "name": "ACTIVITY_STREAK_COUNT",
          "number": 10,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "ACTIVITY_STREAK_MAX_COUNT",
          "number": 11,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "ACTIVITY_STREAK_IS_FROZEN",
          "number": 12,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "ACTIVITY_STREAK_DAYS",
          "number": 13,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "ACTIVITY_STREAK_FROZEN_DAYS",
          "number": 14,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "ACTIVITY_STREAK_LAST_UPDATE_DATE",
          "number": 15,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "LAST_USED_CLIENT",
          "number": 16,
          "options": {}
        },
        {
          "name": "HAS_USED_WEB_CLIENT",
          "number": 17,
          "options": {}
        },
        {
          "name": "HAS_USED_IOS_CLIENT",
          "number": 18,
          "options": {}
        },
        {
          "name": "HAS_USED_ANDROID_CLIENT",
          "number": 19,
          "options": {}
        },
        {
          "name": "FRIENDS_COUNT",
          "number": 20,
          "options": {}
        },
        {
          "name": "ACTIVITY_STREAK_MAX_COUNT_DAY",
          "number": 21,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "TOTAL_TROPHIES_RECEIVED",
          "number": 22,
          "options": {}
        },
        {
          "name": "TOTAL_LESSONS_COMPLETED",
          "number": 23,
          "options": {}
        },
        {
          "name": "TOTAL_COURSES_COMPLETED",
          "number": 24,
          "options": {}
        },
        {
          "name": "ACTIVITY_STREAK_LAST_NOTIFICATION_DATE",
          "number": 25,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "LAST_FRIEND_ADDED_DATE",
          "number": 26,
          "options": {}
        },
        {
          "name": "ACTIVITY_STREAK_LAST_REMINDER_SENT_DATE",
          "number": 27,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "TOTAL_LESSONS_ATTEMPTED",
          "number": 28,
          "options": {}
        },
        {
          "name": "TOTAL_COURSES_ATTEMPTED",
          "number": 29,
          "options": {}
        },
        {
          "name": "LAST_ATTEMPTED_LESSON_UUID",
          "number": 30,
          "options": {}
        },
        {
          "name": "LAST_ATTEMPTED_COURSE_UUID",
          "number": 31,
          "options": {}
        },
        {
          "name": "LAST_COMPLETED_LESSON_UUID",
          "number": 32,
          "options": {}
        },
        {
          "name": "LAST_COMPLETED_COURSE_UUID",
          "number": 33,
          "options": {}
        },
        {
          "name": "LAST_LESSON_ATTEMPTED_DATE",
          "number": 34,
          "options": {}
        },
        {
          "name": "LAST_COURSE_ATTEMPTED_DATE",
          "number": 35,
          "options": {}
        },
        {
          "name": "LAST_LESSON_COMPLETED_DATE",
          "number": 36,
          "options": {}
        },
        {
          "name": "LAST_COURSE_COMPLETED_DATE",
          "number": 37,
          "options": {}
        },
        {
          "name": "COMPLETED_LESSON_LEVEL_IDS",
          "number": 38,
          "options": {}
        },
        {
          "name": "COMPLETED_LESSON_MAX_LEVEL_ID",
          "number": 39,
          "options": {}
        },
        {
          "name": "LAST_LESSON_COMPLETED_DATES",
          "number": 40,
          "options": {}
        },
        {
          "name": "LAST_LESSON_HISTORY_RESET_DATE",
          "number": 41,
          "options": {}
        },
        {
          "name": "BLOCKED_BY_COUNT",
          "number": 42,
          "options": {}
        },
        {
          "name": "LAST_SESSION_START_DATE",
          "number": 43,
          "options": {}
        },
        {
          "name": "LAST_SESSION_END_DATE",
          "number": 44,
          "options": {}
        },
        {
          "name": "DAILY_GAMES_IN_PROGRESS_COUNT",
          "number": 45,
          "options": {}
        },
        {
          "name": "DAILY_GAMES_CHESS_IN_PROGRESS_TO_MOVE",
          "number": 46,
          "options": {}
        },
        {
          "name": "DAILY_GAMES_CHESS960_IN_PROGRESS_TO_MOVE",
          "number": 47,
          "options": {}
        },
        {
          "name": "DAILY_GAMES_CHESS_TIME_PERCENTAGE_USED_TO_MOVE",
          "number": 48,
          "options": {}
        },
        {
          "name": "DAILY_GAMES_CHESS960_TIME_PERCENTAGE_USED_TO_MOVE",
          "number": 49,
          "options": {}
        },
        {
          "name": "DAILY_GAMES_CHESS_IN_PROGRESS_IDS",
          "number": 50,
          "options": {}
        },
        {
          "name": "DAILY_GAMES_CHESS960_IN_PROGRESS_IDS",
          "number": 51,
          "options": {}
        },
        {
          "name": "OLD_MOBILE_CLIENT_PLAYED_ON_LC_DATE",
          "number": 52,
          "options": {}
        },
        {
          "name": "BLOCKED_COUNT",
          "number": 53,
          "options": {}
        },
        {
          "name": "LAST_FRIEND_REMOVED_DATE",
          "number": 54,
          "options": {}
        },
        {
          "name": "ADDED_TO_ITERABLE_DATE",
          "number": 55,
          "options": {}
        },
        {
          "name": "LAST_IOS_VERSION_USED",
          "number": 56,
          "options": {}
        },
        {
          "name": "LAST_ANDROID_VERSION_USED",
          "number": 57,
          "options": {}
        },
        {
          "name": "LAST_WEB_VERSION_USED",
          "number": 58,
          "options": {}
        },
        {
          "name": "LEARN_PATH_COMPLETED_DATE",
          "number": 59,
          "options": {}
        },
        {
          "name": "LAST_GAME_VS_COMPUTER_FINISHED",
          "number": 60,
          "options": {}
        },
        {
          "name": "LAST_LIVE_TIME_CONTROLS",
          "number": 61,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 383647.

```text
WFya2V0aW5nIGZvciBFbmdhZ2VvdHJvbiBhZmZpbGlhdGUgYXVkaWVuY2UgYnVpbGRpbmcuIAAaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_activity.proto":"CjVjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19hY3Rpdml0eS5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIrUnChBBY3Rpdml0eVByb3BlcnR5Ej0KD2xhc3RfbG9naW5fZGF0ZRgBIAEoCzIaLmdvb2dsZS5wcm90b2J1Zi5UaW1lc3RhbXBCA+g+AUgAiAEBEj4KEGxhc3RfZ2FtZV9wbGF5ZWQYAiABKAsyGi5n
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17807"></a>
## FND-17807: Full frontend descriptor: chesscom/user_properties/v1/properties_subscription.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_subscription.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "SubscriptionProperty",
      "field": [
        {
          "name": "last_transition",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "membership_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "membership_level",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "is_trial",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "ltv",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {
            "deprecated": true
          },
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "last_subscription_deactivation_date",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "last_subscription_activation_date",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "last_trial_deactivation_date",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "last_trial_activation_date",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "plan",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "plan_code",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "plan_billing_amount",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "options": {
            "deprecated": true
          },
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "plan_state",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "payment_method",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "trial_state",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "user_lifecycle_state",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "renewal_date",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "is_deactivated",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "previous_membership_name",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "previous_membership_level",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "previous_plan",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "previous_plan_code",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "previous_plan_billing_amount",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "options": {
            "deprecated": true
          },
          "oneof_index": 22,
          "proto3_optional": true
        },
        {
          "name": "is_trial_eligible",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 23,
          "proto3_optional": true
        },
        {
          "name": "cancellation_date",
          "number": 25,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 24,
          "proto3_optional": true
        },
        {
          "name": "cumulative_spend",
          "number": 26,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 25,
          "proto3_optional": true
        },
        {
          "name": "forced_trial_eligibibility_status",
          "number": 29,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 26,
          "proto3_optional": true
        },
        {
          "name": "forced_trial_eligibility_reason",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 27,
          "proto3_optional": true
        },
        {
          "name": "last_subscription_length",
          "number": 31,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 28,
          "proto3_optional": true
        },
        {
          "name": "incentives_redeemed",
          "number": 32,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "current_subscription_end_date",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 29,
          "proto3_optional": true
        },
        {
          "name": "current_subscription_payment_method",
          "number": 34,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 30,
          "proto3_optional": true
        },
        {
          "name": "current_subscription_payment_gateway",
          "number": 35,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 31,
          "proto3_optional": true
        },
        {
          "name": "current_subscription_cancellation_source",
          "number": 36,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 32,
          "proto3_optional": true
        },
        {
          "name": "first_subscription_start_date",
          "number": 37,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 33,
          "proto3_optional": true
        },
        {
          "name": "current_subscription_renewal_date",
          "number": 38,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 34,
          "proto3_optional": true
        },
        {
          "name": "last_subscription_cancellation_date",
          "number": 39,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 35,
          "proto3_optional": true
        },
        {
          "name": "last_trial_cancellation_date",
          "number": 40,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 36,
          "proto3_optional": true
        },
        {
          "name": "last_subscription_payment_method",
          "number": 41,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 37,
          "proto3_optional": true
        },
        {
          "name": "last_trial_payment_method",
          "number": 42,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 38,
          "proto3_optional": true
        },
        {
          "name": "last_subscription_payment_gateway",
          "number": 43,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 39,
          "proto3_optional": true
        },
        {
          "name": "last_trial_payment_gateway",
          "number": 44,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 40,
          "proto3_optional": true
        },
        {
          "name": "user_lifecycle_secondary_state",
          "number": 45,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 41,
          "proto3_optional": true
        },
        {
          "name": "previous_user_lifecycle_state",
          "number": 46,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 42,
          "proto3_optional": true
        },
        {
          "name": "previous_user_lifecycle_secondary_state",
          "number": 47,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 43,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1006,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.SubscriptionPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_last_transition"
        },
        {
          "name": "_membership_name"
        },
        {
          "name": "_membership_level"
        },
        {
          "name": "_is_trial"
        },
        {
          "name": "_ltv"
        },
        {
          "name": "_last_subscription_deactivation_date"
        },
        {
          "name": "_last_subscription_activation_date"
        },
        {
          "name": "_last_trial_deactivation_date"
        },
        {
          "name": "_last_trial_activation_date"
        },
        {
          "name": "_plan"
        },
        {
          "name": "_plan_code"
        },
        {
          "name": "_plan_billing_amount"
        },
        {
          "name": "_plan_state"
        },
        {
          "name": "_payment_method"
        },
        {
          "name": "_trial_state"
        },
        {
          "name": "_user_lifecycle_state"
        },
        {
          "name": "_renewal_date"
        },
        {
          "name": "_is_deactivated"
        },
        {
          "name": "_previous_membership_name"
        },
        {
          "name": "_previous_membership_level"
        },
        {
          "name": "_previous_plan"
        },
        {
          "name": "_previous_plan_code"
        },
        {
          "name": "_previous_plan_billing_amount"
        },
        {
          "name": "_is_trial_eligible"
        },
        {
          "name": "_cancellation_date"
        },
        {
          "name": "_cumulative_spend"
        },
        {
          "name": "_forced_trial_eligibibility_status"
        },
        {
          "name": "_forced_trial_eligibility_reason"
        },
        {
          "name": "_last_subscription_length"
        },
        {
          "name": "_current_subscription_end_date"
        },
        {
          "name": "_current_subscription_payment_method"
        },
        {
          "name": "_current_subscription_payment_gateway"
        },
        {
          "name": "_current_subscription_cancellation_source"
        },
        {
          "name": "_first_subscription_start_date"
        },
        {
          "name": "_current_subscription_renewal_date"
        },
        {
          "name": "_last_subscription_cancellation_date"
        },
        {
          "name": "_last_trial_cancellation_date"
        },
        {
          "name": "_last_subscription_payment_method"
        },
        {
          "name": "_last_trial_payment_method"
        },
        {
          "name": "_last_subscription_payment_gateway"
        },
        {
          "name": "_last_trial_payment_gateway"
        },
        {
          "name": "_user_lifecycle_secondary_state"
        },
        {
          "name": "_previous_user_lifecycle_state"
        },
        {
          "name": "_previous_user_lifecycle_secondary_state"
        }
      ],
      "reserved_range": [
        {
          "start": 27,
          "end": 28
        },
        {
          "start": 28,
          "end": 29
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "SubscriptionPropertyDefinition",
      "value": [
        {
          "name": "SUBSCRIPTION_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "LAST_TRANSITION",
          "number": 1,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "MEMBERSHIP_LEVEL",
          "number": 2,
          "options": {}
        },
        {
          "name": "IS_TRIAL",
          "number": 4,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "LTV",
          "number": 5,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "LAST_SUBSCRIPTION_DEACTIVATION_DATE",
          "number": 6,
          "options": {}
        },
        {
          "name": "LAST_SUBSCRIPTION_ACTIVATION_DATE",
          "number": 7,
          "options": {}
        },
        {
          "name": "LAST_TRIAL_DEACTIVATION_DATE",
          "number": 8,
          "options": {}
        },
        {
          "name": "LAST_TRIAL_ACTIVATION_DATE",
          "number": 9,
          "options": {}
        },
        {
          "name": "PLAN",
          "number": 10,
          "options": {}
        },
        {
          "name": "PLAN_CODE",
          "number": 11,
          "options": {}
        },
        {
          "name": "PLAN_BILLING_AMOUNT",
          "number": 12,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "PLAN_STATE",
          "number": 13,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "PAYMENT_METHOD",
          "number": 14,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "TRIAL_STATE",
          "number": 15,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "USER_LIFECYCLE_STATE",
          "number": 16,
          "options": {}
        },
        {
          "name": "RENEWAL_DATE",
          "number": 17,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "IS_DEACTIVATED",
          "number": 18,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "PREVIOUS_MEMBERSHIP_LEVEL",
          "number": 19,
          "options": {}
        },
        {
          "name": "PREVIOUS_PLAN",
          "number": 21,
          "options": {}
        },
        {
          "name": "PREVIOUS_PLAN_CODE",
          "number": 22,
          "options": {}
        },
        {
          "name": "PREVIOUS_PLAN_BILLING_AMOUNT",
          "number": 23,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "IS_TRIAL_ELIGIBLE",
          "number": 24,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "CANCELLATION_DATE",
          "number": 25,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "CUMULATIVE_SPEND",
          "number": 26,
          "options": {}
        },
        {
          "name": "MEMBERSHIP_NAME",
          "number": 27,
          "options": {}
        },
        {
          "name": "PREVIOUS_MEMBERSHIP_NAME",
          "number": 28,
          "options": {}
        },
        {
          "name": "FORCED_TRIAL_ELIGIBILITY_STATUS",
          "number": 29,
          "options": {}
        },
        {
          "name": "FORCED_TRIAL_ELIGIBILITY_REASON",
          "number": 30,
          "options": {}
        },
        {
          "name": "LAST_SUBSCRIPTION_LENGTH",
          "number": 31,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "INCENTIVES_REDEEMED",
          "number": 32,
          "options": {}
        },
        {
          "name": "CURRENT_SUBSCRIPTION_END_DATE",
          "number": 33,
          "options": {}
        },
        {
          "name": "CURRENT_SUBSCRIPTION_PAYMENT_METHOD",
          "number": 34,
          "options": {}
        },
        {
          "name": "CURRENT_SUBSCRIPTION_PAYMENT_GATEWAY",
          "number": 35,
          "options": {}
        },
        {
          "name": "CURRENT_SUBSCRIPTION_CANCELLATION_SOURCE",
          "number": 36,
          "options": {}
        },
        {
          "name": "FIRST_SUBSCRIPTION_START_DATE",
          "number": 37,
          "options": {}
        },
        {
          "name": "CURRENT_SUBSCRIPTION_RENEWAL_DATE",
          "number": 38,
          "options": {}
        },
        {
          "name": "LAST_SUBSCRIPTION_CANCELLATION_DATE",
          "number": 39,
          "options": {}
        },
        {
          "name": "LAST_TRIAL_CANCELLATION_DATE",
          "number": 40,
          "options": {}
        },
        {
          "name": "LAST_SUBSCRIPTION_PAYMENT_METHOD",
          "number": 41,
          "options": {}
        },
        {
          "name": "LAST_TRIAL_PAYMENT_METHOD",
          "number": 42,
          "options": {}
        },
        {
          "name": "LAST_SUBSCRIPTION_PAYMENT_GATEWAY",
          "number": 43,
          "options": {}
        },
        {
          "name": "LAST_TRIAL_PAYMENT_GATEWAY",
          "number": 44,
          "options": {}
        },
        {
          "name": "USER_LIFECYCLE_SECONDARY_STATE",
          "number": 45,
          "options": {}
        },
        {
          "name": "PREVIOUS_USER_LIFECYCLE_STATE",
          "number": 46,
          "options": {}
        },
        {
          "name": "PREVIOUS_USER_LIFECYCLE_SECONDARY_STATE",
          "number": 47,
          "options": {}
        }
      ],
      "options": {},
      "reserved_range": [
        {
          "start": 3,
          "end": 3
        },
        {
          "start": 20,
          "end": 20
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 397812.

```text
WRyYXRlZCBmcm9tIHRoZSAnR2FtZSAtIENvbXBsZXRlJyBhY3Rpdml0eSBldmVudC4gACgDSAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_subscription.proto":"CjljaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19zdWJzY3JpcHRpb24ucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSLWHAoUU3Vic2NyaXB0aW9uUHJvcGVydHkSIwoPbGFzdF90cmFuc2l0aW9uGAEgASgJQgUYAfA+AUgAiAEBEiEKD21lbWJlcnNoaXBfbmFtZRgCIAEoCUID8D4bSAGIAQESIgoQbWVtYmVy
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17808"></a>
## FND-17808: Full frontend descriptor: chesscom/user_properties/v1/properties_attribution.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_attribution.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "AttributionProperty",
      "field": [
        {
          "name": "signup_initial_campaign",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "signup_initial_content",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "signup_initial_create_date_time",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "signup_initial_medium",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "signup_initial_referer",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "signup_initial_route",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "signup_initial_source",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "signup_initial_term",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "signup_initial_version",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1007,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.AttributionPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_signup_initial_campaign"
        },
        {
          "name": "_signup_initial_content"
        },
        {
          "name": "_signup_initial_create_date_time"
        },
        {
          "name": "_signup_initial_medium"
        },
        {
          "name": "_signup_initial_referer"
        },
        {
          "name": "_signup_initial_route"
        },
        {
          "name": "_signup_initial_source"
        },
        {
          "name": "_signup_initial_term"
        },
        {
          "name": "_signup_initial_version"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "AttributionPropertyDefinition",
      "value": [
        {
          "name": "ATTRIBUTION_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ATTRIBUTION_CAMPAIGN",
          "number": 1,
          "options": {}
        },
        {
          "name": "ATTRIBUTION_CONTENT",
          "number": 2,
          "options": {}
        },
        {
          "name": "ATTRIBUTION_CREATE_DATE_TIME",
          "number": 3,
          "options": {}
        },
        {
          "name": "ATTRIBUTION_MEDIUM",
          "number": 4,
          "options": {}
        },
        {
          "name": "ATTRIBUTION_REFERER",
          "number": 5,
          "options": {}
        },
        {
          "name": "ATTRIBUTION_ROUTE",
          "number": 6,
          "options": {}
        },
        {
          "name": "ATTRIBUTION_SOURCE",
          "number": 7,
          "options": {}
        },
        {
          "name": "ATTRIBUTION_TERM",
          "number": 8,
          "options": {}
        },
        {
          "name": "ATTRIBUTION_VERSION",
          "number": 9,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 409691.

```text
ldmlvdXMgc3ViLXN0YXRlIG9mIHRoZSB1c2VyIGxpZmVjeWNsZS4gATIBAhoHiqYdAwoBASIECAMQAyIECBQQFGIGcHJvdG8z","chesscom/user_properties/v1/properties_attribution.proto":"CjhjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19hdHRyaWJ1dGlvbi5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIqkGChNBdHRyaWJ1dGlvblByb3BlcnR5EikKF3NpZ251cF9pbml0aWFsX2NhbXBhaWduGAEgASgJQgP4PgFIAIgBARIoChZzaWdudXBfaW5pdGlhbF9jb250ZW50GAIgASgJQgP4PgJIAYgBA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17809"></a>
## FND-17809: Full frontend descriptor: chesscom/user_properties/v1/properties_ratings.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_ratings.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "RatingsProperty",
      "field": [
        {
          "name": "rating_chess_blitz",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "rating_chess_bullet",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "rating_chess_daily",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "rating_chess_rapid",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "rating_chess960_blitz",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "rating_chess960_bullet",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "rating_chess960_daily",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "rating_chess960_rapid",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "rating_crazyhouse",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "rating_bughouse",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "rating_kingofthehill",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "rating_oddschess",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "rating_threecheck",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "rating_one",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "rating_chess_blitz_rd",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "rating_chess_bullet_rd",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "rating_chess_daily_rd",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "rating_chess_rapid_rd",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "rating_best",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "rating_best_type",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 19,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1011,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.RatingsPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_rating_chess_blitz"
        },
        {
          "name": "_rating_chess_bullet"
        },
        {
          "name": "_rating_chess_daily"
        },
        {
          "name": "_rating_chess_rapid"
        },
        {
          "name": "_rating_chess960_blitz"
        },
        {
          "name": "_rating_chess960_bullet"
        },
        {
          "name": "_rating_chess960_daily"
        },
        {
          "name": "_rating_chess960_rapid"
        },
        {
          "name": "_rating_crazyhouse"
        },
        {
          "name": "_rating_bughouse"
        },
        {
          "name": "_rating_kingofthehill"
        },
        {
          "name": "_rating_oddschess"
        },
        {
          "name": "_rating_threecheck"
        },
        {
          "name": "_rating_one"
        },
        {
          "name": "_rating_chess_blitz_rd"
        },
        {
          "name": "_rating_chess_bullet_rd"
        },
        {
          "name": "_rating_chess_daily_rd"
        },
        {
          "name": "_rating_chess_rapid_rd"
        },
        {
          "name": "_rating_best"
        },
        {
          "name": "_rating_best_type"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "RatingsPropertyDefinition",
      "value": [
        {
          "name": "RATING_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "RATING_CHESS_BLITZ",
          "number": 1,
          "options": {}
        },
        {
          "name": "RATING_CHESS_BULLET",
          "number": 2,
          "options": {}
        },
        {
          "name": "RATING_CHESS_DAILY",
          "number": 3,
          "options": {}
        },
        {
          "name": "RATING_CHESS_RAPID",
          "number": 4,
          "options": {}
        },
        {
          "name": "RATING_CHESS960_BLITZ",
          "number": 5,
          "options": {}
        },
        {
          "name": "RATING_CHESS960_BULLET",
          "number": 6,
          "options": {}
        },
        {
          "name": "RATING_CHESS960_DAILY",
          "number": 7,
          "options": {}
        },
        {
          "name": "RATING_CHESS960_RAPID",
          "number": 8,
          "options": {}
        },
        {
          "name": "RATING_CRAZYHOUSE",
          "number": 9,
          "options": {}
        },
        {
          "name": "RATING_BUGHOUSE",
          "number": 10,
          "options": {}
        },
        {
          "name": "RATING_KINGOFTHEHILL",
          "number": 11,
          "options": {}
        },
        {
          "name": "RATING_ODDSCHESS",
          "number": 12,
          "options": {}
        },
        {
          "name": "RATING_THREECHECK",
          "number": 13,
          "options": {}
        },
        {
          "name": "RATING_ONE",
          "number": 14,
          "options": {}
        },
        {
          "name": "RATING_CHESS_BLITZ_RD",
          "number": 15,
          "options": {}
        },
        {
          "name": "RATING_CHESS_BULLET_RD",
          "number": 16,
          "options": {}
        },
        {
          "name": "RATING_CHESS_DAILY_RD",
          "number": 17,
          "options": {}
        },
        {
          "name": "RATING_CHESS_RAPID_RD",
          "number": 18,
          "options": {}
        },
        {
          "name": "RATING_BEST",
          "number": 19,
          "options": {}
        },
        {
          "name": "RATING_BEST_TYPE",
          "number": 20,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 411571.

```text
AgaC8I+CBIEdGVybSABEicKE0FUVFJJQlVUSU9OX1ZFUlNJT04QCRoOwj4LEgd2ZXJzaW9uIAEaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_ratings.proto":"CjRjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19yYXRpbmdzLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEi4AoKD1JhdGluZ3NQcm9wZXJ0eRIkChJyYXRpbmdfY2hlc3NfYmxpdHoYASABKAVCA5g/AUgAiAEBEiUKE3JhdGluZ19jaGVzc19idWxsZXQYAiABKAVCA5g/AkgBiAEBEiQKEnJhdGluZ19jaGVzc19kY
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17810"></a>
## FND-17810: Full frontend descriptor: chesscom/user_properties/v1/properties_wdl.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_wdl.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "WDLProperty",
      "field": [
        {
          "name": "total_wins",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "total_wins_bughouse",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "total_wins_chess960",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "total_wins_chess",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "total_wins_crazyhouse",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "total_wins_kingofthehill",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "total_wins_oddschess",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "total_wins_threecheck",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "total_draws",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "total_draws_bughouse",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "total_draws_chess960",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "total_draws_chess",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "total_draws_crazyhouse",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "total_draws_kingofthehill",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "total_draws_oddschess",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "total_draws_threecheck",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "total_losses",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "total_losses_bughouse",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "total_losses_chess960",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "total_losses_chess",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "total_losses_crazyhouse",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "total_losses_kingofthehill",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "total_losses_oddschess",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 22,
          "proto3_optional": true
        },
        {
          "name": "total_losses_threecheck",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 23,
          "proto3_optional": true
        },
        {
          "name": "total_games",
          "number": 25,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 24,
          "proto3_optional": true
        },
        {
          "name": "total_games_4pc",
          "number": 26,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 25,
          "proto3_optional": true
        },
        {
          "name": "total_games_bughouse",
          "number": 27,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 26,
          "proto3_optional": true
        },
        {
          "name": "total_games_chess960",
          "number": 28,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 27,
          "proto3_optional": true
        },
        {
          "name": "total_games_chess",
          "number": 29,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 28,
          "proto3_optional": true
        },
        {
          "name": "total_games_crazyhouse",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 29,
          "proto3_optional": true
        },
        {
          "name": "total_games_kingofthehill",
          "number": 31,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 30,
          "proto3_optional": true
        },
        {
          "name": "total_games_oddschess",
          "number": 32,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 31,
          "proto3_optional": true
        },
        {
          "name": "total_games_threecheck",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 32,
          "proto3_optional": true
        },
        {
          "name": "total_games_vs_computer",
          "number": 34,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 33,
          "proto3_optional": true
        },
        {
          "name": "last_game_result",
          "number": 35,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 34,
          "proto3_optional": true
        },
        {
          "name": "last_game_result_code",
          "number": 36,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 35,
          "proto3_optional": true
        },
        {
          "name": "last_daily_game_result",
          "number": 37,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 36,
          "proto3_optional": true
        },
        {
          "name": "last_daily_game_result_code",
          "number": 38,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 37,
          "proto3_optional": true
        },
        {
          "name": "total_aborted_games",
          "number": 39,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 38,
          "proto3_optional": true
        },
        {
          "name": "total_rated_games_chess_daily",
          "number": 40,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 39,
          "proto3_optional": true
        },
        {
          "name": "total_rated_games_chess_bullet",
          "number": 41,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 40,
          "proto3_optional": true
        },
        {
          "name": "total_rated_games_chess_blitz",
          "number": 42,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 41,
          "proto3_optional": true
        },
        {
          "name": "total_rated_games_chess_rapid",
          "number": 43,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 42,
          "proto3_optional": true
        },
        {
          "name": "total_rated_games",
          "number": 44,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 43,
          "proto3_optional": true
        },
        {
          "name": "total_unrated_games",
          "number": 45,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 44,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1012,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.WDLPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_total_wins"
        },
        {
          "name": "_total_wins_bughouse"
        },
        {
          "name": "_total_wins_chess960"
        },
        {
          "name": "_total_wins_chess"
        },
        {
          "name": "_total_wins_crazyhouse"
        },
        {
          "name": "_total_wins_kingofthehill"
        },
        {
          "name": "_total_wins_oddschess"
        },
        {
          "name": "_total_wins_threecheck"
        },
        {
          "name": "_total_draws"
        },
        {
          "name": "_total_draws_bughouse"
        },
        {
          "name": "_total_draws_chess960"
        },
        {
          "name": "_total_draws_chess"
        },
        {
          "name": "_total_draws_crazyhouse"
        },
        {
          "name": "_total_draws_kingofthehill"
        },
        {
          "name": "_total_draws_oddschess"
        },
        {
          "name": "_total_draws_threecheck"
        },
        {
          "name": "_total_losses"
        },
        {
          "name": "_total_losses_bughouse"
        },
        {
          "name": "_total_losses_chess960"
        },
        {
          "name": "_total_losses_chess"
        },
        {
          "name": "_total_losses_crazyhouse"
        },
        {
          "name": "_total_losses_kingofthehill"
        },
        {
          "name": "_total_losses_oddschess"
        },
        {
          "name": "_total_losses_threecheck"
        },
        {
          "name": "_total_games"
        },
        {
          "name": "_total_games_4pc"
        },
        {
          "name": "_total_games_bughouse"
        },
        {
          "name": "_total_games_chess960"
        },
        {
          "name": "_total_games_chess"
        },
        {
          "name": "_total_games_crazyhouse"
        },
        {
          "name": "_total_games_kingofthehill"
        },
        {
          "name": "_total_games_oddschess"
        },
        {
          "name": "_total_games_threecheck"
        },
        {
          "name": "_total_games_vs_computer"
        },
        {
          "name": "_last_game_result"
        },
        {
          "name": "_last_game_result_code"
        },
        {
          "name": "_last_daily_game_result"
        },
        {
          "name": "_last_daily_game_result_code"
        },
        {
          "name": "_total_aborted_games"
        },
        {
          "name": "_total_rated_games_chess_daily"
        },
        {
          "name": "_total_rated_games_chess_bullet"
        },
        {
          "name": "_total_rated_games_chess_blitz"
        },
        {
          "name": "_total_rated_games_chess_rapid"
        },
        {
          "name": "_total_rated_games"
        },
        {
          "name": "_total_unrated_games"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "WDLPropertyDefinition",
      "value": [
        {
          "name": "WDL_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TOTAL_WINS",
          "number": 1,
          "options": {}
        },
        {
          "name": "TOTAL_WINS_BUGHOUSE",
          "number": 2,
          "options": {}
        },
        {
          "name": "TOTAL_WINS_CHESS960",
          "number": 3,
          "options": {}
        },
        {
          "name": "TOTAL_WINS_CHESS",
          "number": 4,
          "options": {}
        },
        {
          "name": "TOTAL_WINS_CRAZYHOUSE",
          "number": 5,
          "options": {}
        },
        {
          "name": "TOTAL_WINS_KINGOFTHEHILL",
          "number": 6,
          "options": {}
        },
        {
          "name": "TOTAL_WINS_ODDSCHESS",
          "number": 7,
          "options": {}
        },
        {
          "name": "TOTAL_WINS_THREECHECK",
          "number": 8,
          "options": {}
        },
        {
          "name": "TOTAL_DRAWS",
          "number": 9,
          "options": {}
        },
        {
          "name": "TOTAL_DRAWS_BUGHOUSE",
          "number": 10,
          "options": {}
        },
        {
          "name": "TOTAL_DRAWS_CHESS960",
          "number": 11,
          "options": {}
        },
        {
          "name": "TOTAL_DRAWS_CHESS",
          "number": 12,
          "options": {}
        },
        {
          "name": "TOTAL_DRAWS_CRAZYHOUSE",
          "number": 13,
          "options": {}
        },
        {
          "name": "TOTAL_DRAWS_KINGOFTHEHILL",
          "number": 14,
          "options": {}
        },
        {
          "name": "TOTAL_DRAWS_ODDSCHESS",
          "number": 15,
          "options": {}
        },
        {
          "name": "TOTAL_DRAWS_THREECHECK",
          "number": 16,
          "options": {}
        },
        {
          "name": "TOTAL_LOSSES",
          "number": 17,
          "options": {}
        },
        {
          "name": "TOTAL_LOSSES_BUGHOUSE",
          "number": 18,
          "options": {}
        },
        {
          "name": "TOTAL_LOSSES_CHESS960",
          "number": 19,
          "options": {}
        },
        {
          "name": "TOTAL_LOSSES_CHESS",
          "number": 20,
          "options": {}
        },
        {
          "name": "TOTAL_LOSSES_CRAZYHOUSE",
          "number": 21,
          "options": {}
        },
        {
          "name": "TOTAL_LOSSES_KINGOFTHEHILL",
          "number": 22,
          "options": {}
        },
        {
          "name": "TOTAL_LOSSES_ODDSCHESS",
          "number": 23,
          "options": {}
        },
        {
          "name": "TOTAL_LOSSES_THREECHECK",
          "number": 24,
          "options": {}
        },
        {
          "name": "TOTAL_GAMES",
          "number": 25,
          "options": {}
        },
        {
          "name": "TOTAL_GAMES_4PC",
          "number": 26,
          "options": {}
        },
        {
          "name": "TOTAL_GAMES_BUGHOUSE",
          "number": 27,
          "options": {}
        },
        {
          "name": "TOTAL_GAMES_CHESS960",
          "number": 28,
          "options": {}
        },
        {
          "name": "TOTAL_GAMES_CHESS",
          "number": 29,
          "options": {}
        },
        {
          "name": "TOTAL_GAMES_CRAZYHOUSE",
          "number": 30,
          "options": {}
        },
        {
          "name": "TOTAL_GAMES_KINGOFTHEHILL",
          "number": 31,
          "options": {}
        },
        {
          "name": "TOTAL_GAMES_ODDSCHESS",
          "number": 32,
          "options": {}
        },
        {
          "name": "TOTAL_GAMES_THREECHECK",
          "number": 33,
          "options": {}
        },
        {
          "name": "TOTAL_GAMES_VS_COMPUTER",
          "number": 34,
          "options": {}
        },
        {
          "name": "LAST_GAME_RESULT",
          "number": 35,
          "options": {}
        },
        {
          "name": "LAST_GAME_RESULT_CODE",
          "number": 36,
          "options": {}
        },
        {
          "name": "LAST_DAILY_GAME_RESULT",
          "number": 37,
          "options": {}
        },
        {
          "name": "LAST_DAILY_GAME_RESULT_CODE",
          "number": 38,
          "options": {}
        },
        {
          "name": "TOTAL_ABORTED_GAMES",
          "number": 39,
          "options": {}
        },
        {
          "name": "TOTAL_RATED_GAMES_CHESS_DAILY",
          "number": 40,
          "options": {}
        },
        {
          "name": "TOTAL_RATED_GAMES_CHESS_BULLET",
          "number": 41,
          "options": {}
        },
        {
          "name": "TOTAL_RATED_GAMES_CHESS_BLITZ",
          "number": 42,
          "options": {}
        },
        {
          "name": "TOTAL_RATED_GAMES_CHESS_RAPID",
          "number": 43,
          "options": {}
        },
        {
          "name": "TOTAL_RATED_GAMES",
          "number": 44,
          "options": {}
        },
        {
          "name": "TOTAL_UNRATED_GAMES",
          "number": 45,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 415248.

```text
hlIGJlc3QgcmF0aW5nIChlLmcuIGJ1bGxldCwgZGFpbHksIHJhcGlkLCBjaGVzczk2MCkgAUgEGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_wdl.proto":"CjBjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc193ZGwucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSKvGAoLV0RMUHJvcGVydHkSHAoKdG90YWxfd2lucxgBIAEoBUIDoD8BSACIAQESJQoTdG90YWxfd2luc19idWdob3VzZRgCIAEoBUIDoD8CSAGIAQESJQoTdG90YWxfd2luc19jaGVzczk2MBgDIAEoBUIDoD8DSAKIA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17811"></a>
## FND-17811: Full frontend descriptor: chesscom/user_properties/v1/properties_analysis.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_analysis.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "AnalysisProperty",
      "field": [
        {
          "name": "total_games_analyzed",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "total_game_reviews_requested",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "last_game_review_requested_date",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "is_last_game_reviewed",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "game_review_last_game_legacy_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "game_review_last_game_opponent_username",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "game_review_last_game_final_fen",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "game_review_last_game_type",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "game_review_last_game_result",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "game_review_last_game_color",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1013,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.AnalysisPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_total_games_analyzed"
        },
        {
          "name": "_total_game_reviews_requested"
        },
        {
          "name": "_last_game_review_requested_date"
        },
        {
          "name": "_is_last_game_reviewed"
        },
        {
          "name": "_game_review_last_game_legacy_id"
        },
        {
          "name": "_game_review_last_game_opponent_username"
        },
        {
          "name": "_game_review_last_game_final_fen"
        },
        {
          "name": "_game_review_last_game_type"
        },
        {
          "name": "_game_review_last_game_result"
        },
        {
          "name": "_game_review_last_game_color"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "AnalysisPropertyDefinition",
      "value": [
        {
          "name": "ANALYSIS_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TOTAL_GAMES_ANALYZED",
          "number": 1,
          "options": {}
        },
        {
          "name": "TOTAL_GAME_REVIEWS_REQUESTED",
          "number": 2,
          "options": {}
        },
        {
          "name": "LAST_GAME_REVIEW_REQUESTED_DATE",
          "number": 3,
          "options": {}
        },
        {
          "name": "IS_LAST_GAME_REVIEWED",
          "number": 4,
          "options": {}
        },
        {
          "name": "GAME_REVIEW_LAST_GAME_LEGACY_ID",
          "number": 5,
          "options": {}
        },
        {
          "name": "GAME_REVIEW_LAST_GAME_OPPONENT_USERNAME",
          "number": 6,
          "options": {}
        },
        {
          "name": "GAME_REVIEW_LAST_GAME_FINAL_FEN",
          "number": 7,
          "options": {}
        },
        {
          "name": "GAME_REVIEW_LAST_GAME_TYPE",
          "number": 8,
          "options": {}
        },
        {
          "name": "GAME_REVIEW_LAST_GAME_RESULT",
          "number": 9,
          "options": {}
        },
        {
          "name": "GAME_REVIEW_LAST_GAME_COLOR",
          "number": 10,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 424002.

```text
EX0dBTUVTEC0aLcI+KhokVG90YWwgbnVtYmVyIG9mIHVucmF0ZWQgZ2FtZXMgcGxheWVkIAFIAhoHiqYdAwoBAWIGcHJvdG8z","chesscom/user_properties/v1/properties_analysis.proto":"CjVjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19hbmFseXNpcy5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIt4HChBBbmFseXNpc1Byb3BlcnR5EiYKFHRvdGFsX2dhbWVzX2FuYWx5emVkGAEgASgFQgOoPwFIAIgBARIuChx0b3RhbF9nYW1lX3Jldmlld3NfcmVxdWVzdGVkGAIgASgFQgOoPwJIAYgBARJNCh9s
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17812"></a>
## FND-17812: Full frontend descriptor: chesscom/user_properties/v1/properties_settings_daily_chess.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_settings_daily_chess.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "SettingsDailyChessProperty",
      "field": [
        {
          "name": "max_game_count",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "min_opponent_rating",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "max_opponent_rating",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "min_days_per_move",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "max_days_per_move",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "is_friend_exempt",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "is_touch_move",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "is_not_available",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "game_piece_style_id",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "game_board_color_id",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "game_board_size_id",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "post_move_action",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "vacation_time",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "vacation_leave_date",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "is_white_on_bottom",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "show_coordinates",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "auto_win_on_time",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "highlight_moves",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "sounds_enabled",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "default_tab",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "shared_sound_on_move",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "show_legal_moves",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "sounds_id",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 22,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1014,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_max_game_count"
        },
        {
          "name": "_min_opponent_rating"
        },
        {
          "name": "_max_opponent_rating"
        },
        {
          "name": "_min_days_per_move"
        },
        {
          "name": "_max_days_per_move"
        },
        {
          "name": "_is_friend_exempt"
        },
        {
          "name": "_is_touch_move"
        },
        {
          "name": "_is_not_available"
        },
        {
          "name": "_game_piece_style_id"
        },
        {
          "name": "_game_board_color_id"
        },
        {
          "name": "_game_board_size_id"
        },
        {
          "name": "_post_move_action"
        },
        {
          "name": "_vacation_time"
        },
        {
          "name": "_vacation_leave_date"
        },
        {
          "name": "_is_white_on_bottom"
        },
        {
          "name": "_show_coordinates"
        },
        {
          "name": "_auto_win_on_time"
        },
        {
          "name": "_highlight_moves"
        },
        {
          "name": "_sounds_enabled"
        },
        {
          "name": "_default_tab"
        },
        {
          "name": "_shared_sound_on_move"
        },
        {
          "name": "_show_legal_moves"
        },
        {
          "name": "_sounds_id"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "SettingsDailyChessPropertyDefinition",
      "value": [
        {
          "name": "DAILY_CHESS_SETTINGS_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MAX_GAME_COUNT",
          "number": 1,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "MIN_OPPONENT_RATING",
          "number": 2,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "MAX_OPPONENT_RATING",
          "number": 3,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "MIN_DAYS_PER_MOVE",
          "number": 4,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "MAX_DAYS_PER_MOVE",
          "number": 5,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "IS_FRIEND_EXEMPT",
          "number": 6,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "IS_TOUCH_MOVE",
          "number": 7,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "IS_NOT_AVAILABLE",
          "number": 8,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "GAME_PIECE_STYLE_ID",
          "number": 9,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "GAME_BOARD_COLOR_ID",
          "number": 10,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "GAME_BOARD_SIZE_ID",
          "number": 11,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "POST_MOVE_ACTION",
          "number": 12,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "VACATION_TIME",
          "number": 13,
          "options": {}
        },
        {
          "name": "VACATION_LEAVE_DATE",
          "number": 14,
          "options": {}
        },
        {
          "name": "IS_WHITE_ON_BOTTOM",
          "number": 15,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SHOW_COORDINATES",
          "number": 16,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "AUTO_WIN_ON_TIME",
          "number": 17,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "HIGHLIGHT_MOVES",
          "number": 18,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SOUNDS_ENABLED",
          "number": 19,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "DEFAULT_TAB",
          "number": 20,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SHARED_SOUND_ON_MOVE",
          "number": 21,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SHOW_LEGAL_MOVES",
          "number": 22,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SOUNDS_ID",
          "number": 23,
          "options": {
            "deprecated": true
          }
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 426821.

```text
vciB5b3UgcGxheWVkIGluIHlvdXIgbGFzdCBwb3RlbnRpYWwgcmV2aWV3YWJsZSBnYW1lIABIAhoHiqYdAwoBAWIGcHJvdG8z","chesscom/user_properties/v1/properties_settings_daily_chess.proto":"CkFjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19zZXR0aW5nc19kYWlseV9jaGVzcy5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIpIMChpTZXR0aW5nc0RhaWx5Q2hlc3NQcm9wZXJ0eRIiCg5tYXhfZ2FtZV9jb3VudBgBIAEoBUIFGAGwPwFIAIgBARInChNtaW5fb3Bwb25lbnRfcmF0aW5nGAIg
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17813"></a>
## FND-17813: Full frontend descriptor: chesscom/user_properties/v1/properties_settings_live_chess.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_settings_live_chess.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "SettingsLiveChessProperty",
      "field": [
        {
          "name": "auto_queen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "play_multiple_games",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "seek_increment",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "seek_rated",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "seek_filter_premium_only",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "premove_enabled",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "seek_filter_rated_only",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "allow_chat_request_from",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "auto_top",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "focus_mode_enabled",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "allow_challenges_from",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "seek_base_time",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "seek_min_rating",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "seek_max_rating",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "challenge_popup_alert",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "friend_popup_alert",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "event_announcement",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "challenge_min_rating",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "challenge_max_rating",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "seek_base_time_variants",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "seek_increment_variants",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "seek_base_time_chess",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "seek_increment_chess",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 22,
          "proto3_optional": true
        },
        {
          "name": "allow_game_chat",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 23,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1015,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {
        "deprecated": true
      },
      "oneof_decl": [
        {
          "name": "_auto_queen"
        },
        {
          "name": "_play_multiple_games"
        },
        {
          "name": "_seek_increment"
        },
        {
          "name": "_seek_rated"
        },
        {
          "name": "_seek_filter_premium_only"
        },
        {
          "name": "_premove_enabled"
        },
        {
          "name": "_seek_filter_rated_only"
        },
        {
          "name": "_allow_chat_request_from"
        },
        {
          "name": "_auto_top"
        },
        {
          "name": "_focus_mode_enabled"
        },
        {
          "name": "_allow_challenges_from"
        },
        {
          "name": "_seek_base_time"
        },
        {
          "name": "_seek_min_rating"
        },
        {
          "name": "_seek_max_rating"
        },
        {
          "name": "_challenge_popup_alert"
        },
        {
          "name": "_friend_popup_alert"
        },
        {
          "name": "_event_announcement"
        },
        {
          "name": "_challenge_min_rating"
        },
        {
          "name": "_challenge_max_rating"
        },
        {
          "name": "_seek_base_time_variants"
        },
        {
          "name": "_seek_increment_variants"
        },
        {
          "name": "_seek_base_time_chess"
        },
        {
          "name": "_seek_increment_chess"
        },
        {
          "name": "_allow_game_chat"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "SettingsLiveChessPropertyDefinition",
      "value": [
        {
          "name": "LIVE_CHESS_SETTINGS_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "AUTO_QUEEN",
          "number": 1,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "PLAY_MULTIPLE_GAMES",
          "number": 2,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SEEK_INCREMENT",
          "number": 3,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SEEK_RATED",
          "number": 4,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SEEK_FILTER_PREMIUM_ONLY",
          "number": 5,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "PREMOVE_ENABLED",
          "number": 6,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SEEK_FILTER_RATED_ONLY",
          "number": 7,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "ALLOW_CHAT_REQUEST_FROM",
          "number": 8,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "AUTO_TOP",
          "number": 9,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "FOCUS_MODE_ENABLED",
          "number": 10,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "ALLOW_CHALLENGES_FROM",
          "number": 11,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SEEK_BASE_TIME",
          "number": 12,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SEEK_MIN_RATING",
          "number": 13,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SEEK_MAX_RATING",
          "number": 14,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "CHALLENGE_POPUP_ALERT",
          "number": 15,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "FRIEND_POPUP_ALERT",
          "number": 16,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "EVENT_ANNOUNCEMENT",
          "number": 17,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "CHALLENGE_MIN_RATING",
          "number": 18,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "CHALLENGE_MAX_RATING",
          "number": 19,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SEEK_BASE_TIME_VARIANTS",
          "number": 20,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SEEK_INCREMENT_VARIANTS",
          "number": 21,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SEEK_BASE_TIME_CHESS",
          "number": 22,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SEEK_INCREMENT_CHESS",
          "number": 23,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "ALLOW_GAME_CHAT",
          "number": 24,
          "options": {
            "deprecated": true
          }
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 431668.

```text
fSUQQFxoxCAHCPiwKHmRhaWx5X2NoZXNzX3NldHRpbmdzX3NvdW5kc19pZCAAOgYIgKWqsgZIAhoHiqYdAwoBAWIGcHJvdG8z","chesscom/user_properties/v1/properties_settings_live_chess.proto":"CkBjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19zZXR0aW5nc19saXZlX2NoZXNzLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEihQ0KGVNldHRpbmdzTGl2ZUNoZXNzUHJvcGVydHkSHgoKYXV0b19xdWVlbhgBIAEoCEIFGAG4PwFIAIgBARInChNwbGF5X211bHRpcGxlX2dhbWVzGAIgASgIQgUYA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17814"></a>
## FND-17814: Full frontend descriptor: chesscom/user_properties/v1/properties_stats_daily.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_stats_daily.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "StatsDailyProperty",
      "field": [
        {
          "name": "total_game_count",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "tournament_count",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "tournament_game_win_count",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "tournament_game_loss_count",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "tournament_game_draw_count",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "tournament_1st_place",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "tournament_2nd_place",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "tournament_3rd_place",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "tournament_host_count",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "tournament_host_user_count",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "tournament_withdraw_count",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "tournament_in_progress_count",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "tournament_cancel_count",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "tournament_points",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "tournament_count_total",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "tournament_points_total",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "tournament_count_previous",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "tournament_points_previous",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "unrated_game_count",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "in_progress_count",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "timeout_count",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "moves_per_game",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "total_move_time",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT64",
          "options": {
            "deprecated": true
          },
          "oneof_index": 22,
          "proto3_optional": true
        },
        {
          "name": "total_move_count",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 23,
          "proto3_optional": true
        },
        {
          "name": "last_game_date",
          "number": 25,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 24,
          "proto3_optional": true
        },
        {
          "name": "current_streak",
          "number": 26,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 25,
          "proto3_optional": true
        },
        {
          "name": "max_win_streak",
          "number": 27,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 26,
          "proto3_optional": true
        },
        {
          "name": "max_loss_streak",
          "number": 28,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 27,
          "proto3_optional": true
        },
        {
          "name": "rating",
          "number": 29,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 28,
          "proto3_optional": true
        },
        {
          "name": "rd",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "options": {
            "deprecated": true
          },
          "oneof_index": 29,
          "proto3_optional": true
        },
        {
          "name": "is_active",
          "number": 31,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 30,
          "proto3_optional": true
        },
        {
          "name": "timeout_percent",
          "number": 32,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {
            "deprecated": true
          },
          "oneof_index": 31,
          "proto3_optional": true
        },
        {
          "name": "avg_time_per_move",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {
            "deprecated": true
          },
          "oneof_index": 32,
          "proto3_optional": true
        },
        {
          "name": "is_unrated",
          "number": 34,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 33,
          "proto3_optional": true
        },
        {
          "name": "highest_rating",
          "number": 35,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 34,
          "proto3_optional": true
        },
        {
          "name": "highest_rating_date",
          "number": 36,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 35,
          "proto3_optional": true
        },
        {
          "name": "avg_opponent_rating",
          "number": 37,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 36,
          "proto3_optional": true
        },
        {
          "name": "best_win_game_id",
          "number": 38,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "options": {
            "deprecated": true
          },
          "oneof_index": 37,
          "proto3_optional": true
        },
        {
          "name": "total_rated_game_count",
          "number": 39,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 38,
          "proto3_optional": true
        },
        {
          "name": "total_rated_win_count",
          "number": 40,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 39,
          "proto3_optional": true
        },
        {
          "name": "total_rated_loss_count",
          "number": 41,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 40,
          "proto3_optional": true
        },
        {
          "name": "total_rated_draw_count",
          "number": 42,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 41,
          "proto3_optional": true
        },
        {
          "name": "last_date",
          "number": 43,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 42,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1016,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.StatsDailyPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_total_game_count"
        },
        {
          "name": "_tournament_count"
        },
        {
          "name": "_tournament_game_win_count"
        },
        {
          "name": "_tournament_game_loss_count"
        },
        {
          "name": "_tournament_game_draw_count"
        },
        {
          "name": "_tournament_1st_place"
        },
        {
          "name": "_tournament_2nd_place"
        },
        {
          "name": "_tournament_3rd_place"
        },
        {
          "name": "_tournament_host_count"
        },
        {
          "name": "_tournament_host_user_count"
        },
        {
          "name": "_tournament_withdraw_count"
        },
        {
          "name": "_tournament_in_progress_count"
        },
        {
          "name": "_tournament_cancel_count"
        },
        {
          "name": "_tournament_points"
        },
        {
          "name": "_tournament_count_total"
        },
        {
          "name": "_tournament_points_total"
        },
        {
          "name": "_tournament_count_previous"
        },
        {
          "name": "_tournament_points_previous"
        },
        {
          "name": "_unrated_game_count"
        },
        {
          "name": "_in_progress_count"
        },
        {
          "name": "_timeout_count"
        },
        {
          "name": "_moves_per_game"
        },
        {
          "name": "_total_move_time"
        },
        {
          "name": "_total_move_count"
        },
        {
          "name": "_last_game_date"
        },
        {
          "name": "_current_streak"
        },
        {
          "name": "_max_win_streak"
        },
        {
          "name": "_max_loss_streak"
        },
        {
          "name": "_rating"
        },
        {
          "name": "_rd"
        },
        {
          "name": "_is_active"
        },
        {
          "name": "_timeout_percent"
        },
        {
          "name": "_avg_time_per_move"
        },
        {
          "name": "_is_unrated"
        },
        {
          "name": "_highest_rating"
        },
        {
          "name": "_highest_rating_date"
        },
        {
          "name": "_avg_opponent_rating"
        },
        {
          "name": "_best_win_game_id"
        },
        {
          "name": "_total_rated_game_count"
        },
        {
          "name": "_total_rated_win_count"
        },
        {
          "name": "_total_rated_loss_count"
        },
        {
          "name": "_total_rated_draw_count"
        },
        {
          "name": "_last_date"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "StatsDailyPropertyDefinition",
      "value": [
        {
          "name": "STATS_DAILY_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "STATS_DAILY_TOTAL_GAME_COUNT",
          "number": 1,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_COUNT",
          "number": 2,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_GAME_WIN_COUNT",
          "number": 3,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_GAME_LOSS_COUNT",
          "number": 4,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_GAME_DRAW_COUNT",
          "number": 5,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_1ST_PLACE",
          "number": 6,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_2ND_PLACE",
          "number": 7,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_3RD_PLACE",
          "number": 8,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_HOST_COUNT",
          "number": 9,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_HOST_USER_COUNT",
          "number": 10,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_WITHDRAW_COUNT",
          "number": 11,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_IN_PROGRESS_COUNT",
          "number": 12,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_CANCEL_COUNT",
          "number": 13,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_POINTS",
          "number": 14,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_COUNT_TOTAL",
          "number": 15,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_POINTS_TOTAL",
          "number": 16,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_COUNT_PREVIOUS",
          "number": 17,
          "options": {}
        },
        {
          "name": "STATS_DAILY_TOURNAMENT_POINTS_PREVIOUS",
          "number": 18,
          "options": {}
        },
        {
          "name": "STATS_DAILY_UNRATED_GAME_COUNT",
          "number": 19,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_IN_PROGRESS_COUNT",
          "number": 20,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_TIMEOUT_COUNT",
          "number": 21,
          "options": {}
        },
        {
          "name": "STATS_DAILY_MOVES_PER_GAME",
          "number": 22,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_TOTAL_MOVE_TIME",
          "number": 23,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_TOTAL_MOVE_COUNT",
          "number": 24,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_LAST_GAME_DATE",
          "number": 25,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CURRENT_STREAK",
          "number": 26,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_MAX_WIN_STREAK",
          "number": 27,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_MAX_LOSS_STREAK",
          "number": 28,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_RATING",
          "number": 29,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_RD",
          "number": 30,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_IS_ACTIVE",
          "number": 31,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_TIMEOUT_PERCENT",
          "number": 32,
          "options": {}
        },
        {
          "name": "STATS_DAILY_AVG_TIME_PER_MOVE",
          "number": 33,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_IS_UNRATED",
          "number": 34,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_HIGHEST_RATING",
          "number": 35,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_HIGHEST_RATING_DATE",
          "number": 36,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_AVG_OPPONENT_RATING",
          "number": 37,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_BEST_WIN_GAME_ID",
          "number": 38,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_TOTAL_RATED_GAME_COUNT",
          "number": 39,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_TOTAL_RATED_WIN_COUNT",
          "number": 40,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_TOTAL_RATED_DRAW_COUNT",
          "number": 41,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_TOTAL_RATED_LOSS_COUNT",
          "number": 42,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_LAST_DATE",
          "number": 43,
          "options": {
            "deprecated": true
          }
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 436840.

```text
Bo1CAHCPjAKImdhbWVfc2V0dGluZ3NfbGl2ZV9hbGxvd19nYW1lX2NoYXQgADoGCIClqrIGSAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_stats_daily.proto":"CjhjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19zdGF0c19kYWlseS5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIuUWChJTdGF0c0RhaWx5UHJvcGVydHkSIgoQdG90YWxfZ2FtZV9jb3VudBgBIAEoBUIDwD8BSACIAQESIgoQdG91cm5hbWVudF9jb3VudBgCIAEoBUIDwD8CSAGIAQESKwoZdG91cm5hbWVud
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17815"></a>
## FND-17815: Full frontend descriptor: chesscom/user_properties/v1/properties_stats_daily_chess960.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_stats_daily_chess960.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "StatsDailyChess960Property",
      "field": [
        {
          "name": "last_game_date",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "current_streak",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "max_win_streak",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "max_loss_streak",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "rating",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "rd",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "options": {
            "deprecated": true
          },
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "is_active",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "is_unrated",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "highest_rating",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "highest_rating_date",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "avg_opponent_rating",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "best_win_game_id",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "options": {
            "deprecated": true
          },
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "total_rated_game_count",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "total_rated_win_count",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "total_rated_loss_count",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "total_rated_draw_count",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "last_date",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 16,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1017,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_last_game_date"
        },
        {
          "name": "_current_streak"
        },
        {
          "name": "_max_win_streak"
        },
        {
          "name": "_max_loss_streak"
        },
        {
          "name": "_rating"
        },
        {
          "name": "_rd"
        },
        {
          "name": "_is_active"
        },
        {
          "name": "_is_unrated"
        },
        {
          "name": "_highest_rating"
        },
        {
          "name": "_highest_rating_date"
        },
        {
          "name": "_avg_opponent_rating"
        },
        {
          "name": "_best_win_game_id"
        },
        {
          "name": "_total_rated_game_count"
        },
        {
          "name": "_total_rated_win_count"
        },
        {
          "name": "_total_rated_loss_count"
        },
        {
          "name": "_total_rated_draw_count"
        },
        {
          "name": "_last_date"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "StatsDailyChess960PropertyDefinition",
      "value": [
        {
          "name": "STATS_DAILY_CHESS960_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "STATS_DAILY_CHESS960_LAST_GAME_DATE",
          "number": 1,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_CURRENT_STREAK",
          "number": 2,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_MAX_WIN_STREAK",
          "number": 3,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_MAX_LOSS_STREAK",
          "number": 4,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_RATING",
          "number": 5,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_RD",
          "number": 6,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_IS_ACTIVE",
          "number": 7,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_IS_UNRATED",
          "number": 8,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_HIGHEST_RATING",
          "number": 9,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_HIGHEST_RATING_DATE",
          "number": 10,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_AVG_OPPONENT_RATING",
          "number": 11,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_BEST_WIN_GAME_ID",
          "number": 12,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_TOTAL_RATED_GAME_COUNT",
          "number": 13,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_TOTAL_RATED_WIN_COUNT",
          "number": 14,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_TOTAL_RATED_DRAW_COUNT",
          "number": 15,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_TOTAL_RATED_LOSS_COUNT",
          "number": 16,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_DAILY_CHESS960_LAST_DATE",
          "number": 17,
          "options": {
            "deprecated": true
          }
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 445073.

```text
cKFVNUQVRTX0RBSUxZX0xBU1RfREFURRArGhwIAcI+FxIJbGFzdF9kYXRlIAE6BgiAsO7BBkgCGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_stats_daily_chess960.proto":"CkFjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19zdGF0c19kYWlseV9jaGVzczk2MC5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIrgJChpTdGF0c0RhaWx5Q2hlc3M5NjBQcm9wZXJ0eRI+Cg5sYXN0X2dhbWVfZGF0ZRgBIAEoCzIaLmdvb2dsZS5wcm90b2J1Zi5UaW1lc3RhbXBCBRgByD8BSACI
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17816"></a>
## FND-17816: Full frontend descriptor: chesscom/user_properties/v1/properties_stats_live.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_stats_live.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "StatsLiveProperty",
      "field": [
        {
          "name": "rating",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "game_time_class",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "total_move_count",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "unrated_game_count",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "disconnect_count",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "best_win_game_id",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT64",
          "options": {
            "deprecated": true
          },
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "highest_opponent_rating",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "last_date",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "highest_rating",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "highest_rating_date",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "last_game_date",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {
            "deprecated": true
          },
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "is_active",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "total_rated_game_count",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "total_rated_win_count",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "total_rated_loss_count",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "total_rated_draw_count",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "current_streak",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "max_win_streak",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "max_loss_streak",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "is_unrated",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {
            "deprecated": true
          },
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "avg_opponent_rating",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {
            "deprecated": true
          },
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "best_win_game",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "moves_per_game",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 22,
          "proto3_optional": true
        },
        {
          "name": "adjudicated_count",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 23,
          "proto3_optional": true
        },
        {
          "name": "dw_count",
          "number": 25,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 24,
          "proto3_optional": true
        },
        {
          "name": "tournament_count",
          "number": 26,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 25,
          "proto3_optional": true
        },
        {
          "name": "tournament_game_win_count",
          "number": 27,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 26,
          "proto3_optional": true
        },
        {
          "name": "tournament_game_loss_count",
          "number": 28,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 27,
          "proto3_optional": true
        },
        {
          "name": "tournament_game_draw_count",
          "number": 29,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 28,
          "proto3_optional": true
        },
        {
          "name": "tournament_host_count",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 29,
          "proto3_optional": true
        },
        {
          "name": "tournament_1st_place",
          "number": 31,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 30,
          "proto3_optional": true
        },
        {
          "name": "tournament_2nd_place",
          "number": 32,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 31,
          "proto3_optional": true
        },
        {
          "name": "tournament_3rd_place",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 32,
          "proto3_optional": true
        },
        {
          "name": "tournament_host_user_count",
          "number": 34,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 33,
          "proto3_optional": true
        },
        {
          "name": "tournament_withdraw_count",
          "number": 35,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 34,
          "proto3_optional": true
        },
        {
          "name": "tournament_in_progress_count",
          "number": 36,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 35,
          "proto3_optional": true
        },
        {
          "name": "tournament_cancel_count",
          "number": 37,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 36,
          "proto3_optional": true
        },
        {
          "name": "tournament_points",
          "number": 38,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 37,
          "proto3_optional": true
        },
        {
          "name": "tournament_count_total",
          "number": 39,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 38,
          "proto3_optional": true
        },
        {
          "name": "tournament_points_total",
          "number": 40,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 39,
          "proto3_optional": true
        },
        {
          "name": "tournament_count_previous",
          "number": 41,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 40,
          "proto3_optional": true
        },
        {
          "name": "tournament_points_previous",
          "number": 42,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 41,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1018,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.StatsLivePropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_rating"
        },
        {
          "name": "_game_time_class"
        },
        {
          "name": "_total_move_count"
        },
        {
          "name": "_unrated_game_count"
        },
        {
          "name": "_disconnect_count"
        },
        {
          "name": "_best_win_game_id"
        },
        {
          "name": "_highest_opponent_rating"
        },
        {
          "name": "_last_date"
        },
        {
          "name": "_highest_rating"
        },
        {
          "name": "_highest_rating_date"
        },
        {
          "name": "_last_game_date"
        },
        {
          "name": "_is_active"
        },
        {
          "name": "_total_rated_game_count"
        },
        {
          "name": "_total_rated_win_count"
        },
        {
          "name": "_total_rated_loss_count"
        },
        {
          "name": "_total_rated_draw_count"
        },
        {
          "name": "_current_streak"
        },
        {
          "name": "_max_win_streak"
        },
        {
          "name": "_max_loss_streak"
        },
        {
          "name": "_is_unrated"
        },
        {
          "name": "_avg_opponent_rating"
        },
        {
          "name": "_best_win_game"
        },
        {
          "name": "_moves_per_game"
        },
        {
          "name": "_adjudicated_count"
        },
        {
          "name": "_dw_count"
        },
        {
          "name": "_tournament_count"
        },
        {
          "name": "_tournament_game_win_count"
        },
        {
          "name": "_tournament_game_loss_count"
        },
        {
          "name": "_tournament_game_draw_count"
        },
        {
          "name": "_tournament_host_count"
        },
        {
          "name": "_tournament_1st_place"
        },
        {
          "name": "_tournament_2nd_place"
        },
        {
          "name": "_tournament_3rd_place"
        },
        {
          "name": "_tournament_host_user_count"
        },
        {
          "name": "_tournament_withdraw_count"
        },
        {
          "name": "_tournament_in_progress_count"
        },
        {
          "name": "_tournament_cancel_count"
        },
        {
          "name": "_tournament_points"
        },
        {
          "name": "_tournament_count_total"
        },
        {
          "name": "_tournament_points_total"
        },
        {
          "name": "_tournament_count_previous"
        },
        {
          "name": "_tournament_points_previous"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "StatsLivePropertyDefinition",
      "value": [
        {
          "name": "STATS_LIVE_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "STATS_LIVE_RATING",
          "number": 1,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_GAME_TIME_CLASS",
          "number": 2,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOTAL_MOVE_COUNT",
          "number": 3,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_UNRATED_GAME_COUNT",
          "number": 4,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_DISCONNECT_COUNT",
          "number": 5,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_BEST_WIN_GAME_ID",
          "number": 6,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_HIGHEST_OPPONENT_RATING",
          "number": 7,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_LAST_DATE",
          "number": 8,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_HIGHEST_RATING",
          "number": 9,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_HIGHEST_RATING_DATE",
          "number": 10,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_LAST_GAME_DATE",
          "number": 11,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_IS_ACTIVE",
          "number": 12,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOTAL_RATED_GAME_COUNT",
          "number": 13,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOTAL_RATED_WIN_COUNT",
          "number": 14,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOTAL_RATED_LOSS_COUNT",
          "number": 15,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOTAL_RATED_DRAW_COUNT",
          "number": 16,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_CURRENT_STREAK",
          "number": 17,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_MAX_WIN_STREAK",
          "number": 18,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_MAX_LOSS_STREAK",
          "number": 19,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_IS_UNRATED",
          "number": 20,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_AVG_OPPONENT_RATING",
          "number": 21,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_BEST_WIN_GAME",
          "number": 22,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_MOVES_PER_GAME",
          "number": 23,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_ADJUDICATED_COUNT",
          "number": 24,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_DW_COUNT",
          "number": 25,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_COUNT",
          "number": 26,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_GAME_WIN_COUNT",
          "number": 27,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_GAME_LOSS_COUNT",
          "number": 28,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_GAME_DRAW_COUNT",
          "number": 29,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_HOST_COUNT",
          "number": 30,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_1ST_PLACE",
          "number": 31,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_2ND_PLACE",
          "number": 32,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_3RD_PLACE",
          "number": 33,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_HOST_USER_COUNT",
          "number": 34,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_WITHDRAW_COUNT",
          "number": 35,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_IN_PROGRESS_COUNT",
          "number": 36,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_CANCEL_COUNT",
          "number": 37,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_POINTS",
          "number": 38,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_COUNT_TOTAL",
          "number": 49,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_POINTS_TOTAL",
          "number": 40,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_COUNT_PREVIOUS",
          "number": 41,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "STATS_LIVE_TOURNAMENT_POINTS_PREVIOUS",
          "number": 42,
          "options": {
            "deprecated": true
          }
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 448776.

```text
EQUlMWV9DSEVTUzk2MF9MQVNUX0RBVEUQERocCAHCPhcSCWxhc3RfZGF0ZSABOgYIgJrPsgZIAhoHiqYdAwoBAWIGcHJvdG8z","chesscom/user_properties/v1/properties_stats_live.proto":"CjdjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19zdGF0c19saXZlLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEi5hYKEVN0YXRzTGl2ZVByb3BlcnR5EhoKBnJhdGluZxgBIAEoDUIFGAHQPwFIAIgBARIjCg9nYW1lX3RpbWVfY2xhc3MYAiABKAlCBRgB0D8CSAGIAQESJAoQdG90YWxfbW92ZV9jb3VudBgDIA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17817"></a>
## FND-17817: Full frontend descriptor: chesscom/user_properties/v1/properties_user_settings.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_user_settings.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "UserSettingsProperty",
      "field": [
        {
          "name": "notification_mobile_chess_tv",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "notification_web_chess_tv",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "gameplay_challenge_min_rating",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_game_event",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_allow_offline_challenges",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_new_content",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_my_turn_to_move",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_news_and_announcements",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "gameplay_challenge_max_rating",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "notification_web_lesson_and_practice",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "board_play_sounds",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "notification_email_new_content",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "notification_email_new_social_trophy",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "board_move_method",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "board_sound_theme",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "notification_email_news_and_announcements",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_friend_activity_updates",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "board_move_list_style",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_recommended_match",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "notification_email_new_comment",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "gameplay_daily_confirm_move",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "gameplay_seek_min_rating",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "notification_web_new_user_comment",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 22,
          "proto3_optional": true
        },
        {
          "name": "board_show_legal_moves",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 23,
          "proto3_optional": true
        },
        {
          "name": "gameplay_show_timestamps",
          "number": 25,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 24,
          "proto3_optional": true
        },
        {
          "name": "notification_web_game_event",
          "number": 26,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 25,
          "proto3_optional": true
        },
        {
          "name": "privacy_friends_list_privacy",
          "number": 27,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 26,
          "proto3_optional": true
        },
        {
          "name": "notification_web_vote_chess",
          "number": 28,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 27,
          "proto3_optional": true
        },
        {
          "name": "board_coordinates",
          "number": 29,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 28,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_play_multiple_games",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 29,
          "proto3_optional": true
        },
        {
          "name": "notification_email_chess_tv",
          "number": 31,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 30,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_auto_promote_queen",
          "number": 32,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 31,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_new_comment",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 32,
          "proto3_optional": true
        },
        {
          "name": "gameplay_daily_max_days_per_move",
          "number": 34,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 33,
          "proto3_optional": true
        },
        {
          "name": "gameplay_confirm_resign",
          "number": 35,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 34,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_seek_base_time_variants",
          "number": 36,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 35,
          "proto3_optional": true
        },
        {
          "name": "notification_email_lesson_quota",
          "number": 37,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 36,
          "proto3_optional": true
        },
        {
          "name": "notification_email_lesson_and_practice",
          "number": 38,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 37,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_challenge_alerts",
          "number": 39,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 38,
          "proto3_optional": true
        },
        {
          "name": "board_white_always_on_bottom",
          "number": 40,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 39,
          "proto3_optional": true
        },
        {
          "name": "notification_web_new_comment",
          "number": 41,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 40,
          "proto3_optional": true
        },
        {
          "name": "privacy_insights_privacy",
          "number": 42,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 41,
          "proto3_optional": true
        },
        {
          "name": "notification_web_new_content",
          "number": 43,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 42,
          "proto3_optional": true
        },
        {
          "name": "privacy_allow_friend_requests",
          "number": 44,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 43,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_lesson_quota",
          "number": 45,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 44,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_premoves",
          "number": 46,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 45,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_new_message",
          "number": 47,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 46,
          "proto3_optional": true
        },
        {
          "name": "notification_web_news_and_announcements",
          "number": 48,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 47,
          "proto3_optional": true
        },
        {
          "name": "notification_email_hero_playing",
          "number": 49,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 48,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_evaluation_bar",
          "number": 50,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 49,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_vote_chess",
          "number": 51,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 50,
          "proto3_optional": true
        },
        {
          "name": "notification_web_new_message",
          "number": 52,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 51,
          "proto3_optional": true
        },
        {
          "name": "board_highlight_moves",
          "number": 53,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 52,
          "proto3_optional": true
        },
        {
          "name": "gameplay_seek_max_rating",
          "number": 54,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 53,
          "proto3_optional": true
        },
        {
          "name": "gameplay_analysis_evaluation_bar_mode_wdl_for_openings",
          "number": 55,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 54,
          "proto3_optional": true
        },
        {
          "name": "board_board_style",
          "number": 56,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 55,
          "proto3_optional": true
        },
        {
          "name": "gameplay_allow_challenges_from",
          "number": 57,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 56,
          "proto3_optional": true
        },
        {
          "name": "gameplay_play_streaks",
          "number": 58,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 57,
          "proto3_optional": true
        },
        {
          "name": "privacy_allow_global_chat_requests_from",
          "number": 59,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 58,
          "proto3_optional": true
        },
        {
          "name": "puzzles_show_details",
          "number": 60,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 59,
          "proto3_optional": true
        },
        {
          "name": "notification_web_new_social_trophy",
          "number": 61,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 60,
          "proto3_optional": true
        },
        {
          "name": "privacy_blog_privacy",
          "number": 62,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 61,
          "proto3_optional": true
        },
        {
          "name": "gameplay_friends_can_challenge_me_no_matter_what",
          "number": 63,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 62,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_seek_filter_premium_only",
          "number": 64,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 63,
          "proto3_optional": true
        },
        {
          "name": "notification_email_game_event",
          "number": 65,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 64,
          "proto3_optional": true
        },
        {
          "name": "gameplay_seek_game_type",
          "number": 66,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 65,
          "proto3_optional": true
        },
        {
          "name": "ui_enable_special_theme_forcing",
          "number": 67,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 66,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_seek_base_time_chess",
          "number": 68,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 67,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_new_user_comment",
          "number": 69,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 68,
          "proto3_optional": true
        },
        {
          "name": "notification_email_friend_activity_updates",
          "number": 70,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 69,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_seek_increment_variants",
          "number": 71,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 70,
          "proto3_optional": true
        },
        {
          "name": "gameplay_auto_analysis",
          "number": 72,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 71,
          "proto3_optional": true
        },
        {
          "name": "privacy_allow_club_invitations",
          "number": 73,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 72,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_low_time_warning",
          "number": 74,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 73,
          "proto3_optional": true
        },
        {
          "name": "notification_web_lesson_quota",
          "number": 75,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 74,
          "proto3_optional": true
        },
        {
          "name": "gameplay_daily_min_days_per_move",
          "number": 76,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 75,
          "proto3_optional": true
        },
        {
          "name": "gameplay_focus_mode",
          "number": 77,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 76,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_seek_is_rated",
          "number": 78,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 77,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_friends_alerts",
          "number": 79,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 78,
          "proto3_optional": true
        },
        {
          "name": "privacy_safe_mode",
          "number": 80,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 79,
          "proto3_optional": true
        },
        {
          "name": "board_show_animations",
          "number": 81,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 80,
          "proto3_optional": true
        },
        {
          "name": "ui_mode",
          "number": 82,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 81,
          "proto3_optional": true
        },
        {
          "name": "gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame",
          "number": 83,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 82,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_hero_playing",
          "number": 84,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 83,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_puzzle_reminder",
          "number": 85,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 84,
          "proto3_optional": true
        },
        {
          "name": "notification_web_friend_activity_updates",
          "number": 86,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 85,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_engine_evaluation",
          "number": 87,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 86,
          "proto3_optional": true
        },
        {
          "name": "notification_email_new_user_comment",
          "number": 88,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 87,
          "proto3_optional": true
        },
        {
          "name": "gameplay_allow_game_chat_with",
          "number": 89,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 88,
          "proto3_optional": true
        },
        {
          "name": "notification_email_new_friend_request",
          "number": 90,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 89,
          "proto3_optional": true
        },
        {
          "name": "notification_email_new_message",
          "number": 91,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 90,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_auto_watch_top_game",
          "number": 92,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 91,
          "proto3_optional": true
        },
        {
          "name": "board_pieces_style",
          "number": 93,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 92,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_seek_increment_chess",
          "number": 94,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 93,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_new_friend_request",
          "number": 95,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 94,
          "proto3_optional": true
        },
        {
          "name": "gameplay_daily_after_moving",
          "number": 96,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 95,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_allow_chat_requests_from",
          "number": 97,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 96,
          "proto3_optional": true
        },
        {
          "name": "notification_email_my_turn_to_move",
          "number": 98,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 97,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_new_social_trophy",
          "number": 99,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 98,
          "proto3_optional": true
        },
        {
          "name": "gameplay_daily_max_game_count",
          "number": 100,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 99,
          "proto3_optional": true
        },
        {
          "name": "puzzles_show_timer",
          "number": 101,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 100,
          "proto3_optional": true
        },
        {
          "name": "privacy_notes_privacy",
          "number": 102,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 101,
          "proto3_optional": true
        },
        {
          "name": "learn_coach",
          "number": 103,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 102,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_right_button_arrows",
          "number": 104,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 103,
          "proto3_optional": true
        },
        {
          "name": "privacy_allow_tournament_invitations",
          "number": 105,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 104,
          "proto3_optional": true
        },
        {
          "name": "notification_web_new_friend_request",
          "number": 106,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 105,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_event_announcements",
          "number": 107,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 106,
          "proto3_optional": true
        },
        {
          "name": "notification_email_puzzle_reminder",
          "number": 108,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 107,
          "proto3_optional": true
        },
        {
          "name": "notification_email_vote_chess",
          "number": 109,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 108,
          "proto3_optional": true
        },
        {
          "name": "notification_auto_track_content",
          "number": 110,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 109,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_seek_filter_hide_variants",
          "number": 111,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 110,
          "proto3_optional": true
        },
        {
          "name": "privacy_messages_privacy",
          "number": 112,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 111,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_seek_filter_rated_only",
          "number": 113,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 112,
          "proto3_optional": true
        },
        {
          "name": "notification_web_my_turn_to_move",
          "number": 114,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 113,
          "proto3_optional": true
        },
        {
          "name": "gameplay_live_auto_switch_game",
          "number": 115,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 114,
          "proto3_optional": true
        },
        {
          "name": "notification_web_hero_playing",
          "number": 116,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 115,
          "proto3_optional": true
        },
        {
          "name": "gameplay_daily_auto_win_on_time",
          "number": 117,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 116,
          "proto3_optional": true
        },
        {
          "name": "board_animation_type",
          "number": 118,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 117,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_lesson_and_practice",
          "number": 119,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 118,
          "proto3_optional": true
        },
        {
          "name": "board_win_celebration",
          "number": 120,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 119,
          "proto3_optional": true
        },
        {
          "name": "notification_web_streaks_reminders",
          "number": 121,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 120,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_streaks_reminders",
          "number": 122,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 121,
          "proto3_optional": true
        },
        {
          "name": "notification_email_streaks_reminders",
          "number": 123,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 122,
          "proto3_optional": true
        },
        {
          "name": "notification_web_leagues_reminders",
          "number": 124,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 123,
          "proto3_optional": true
        },
        {
          "name": "notification_mobile_leagues_reminders",
          "number": 125,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 124,
          "proto3_optional": true
        },
        {
          "name": "notification_email_leagues_reminders",
          "number": 126,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 125,
          "proto3_optional": true
        },
        {
          "name": "puzzles_show_classic_mode",
          "number": 127,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 126,
          "proto3_optional": true
        },
        {
          "name": "gameplay_show_membership_badges",
          "number": 128,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 127,
          "proto3_optional": true
        },
        {
          "name": "learn_coach_id",
          "number": 129,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 128,
          "proto3_optional": true
        },
        {
          "name": "learn_coach_nudge",
          "number": 130,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 129,
          "proto3_optional": true
        },
        {
          "name": "toaster_center_show_club_request_toasters",
          "number": 131,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 130,
          "proto3_optional": true
        },
        {
          "name": "toaster_center_show_friend_request_toasters",
          "number": 132,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 131,
          "proto3_optional": true
        },
        {
          "name": "toaster_center_automatically_expand_toasters",
          "number": 133,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 132,
          "proto3_optional": true
        },
        {
          "name": "board_castling_type",
          "number": 134,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 133,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1019,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.UserSettingsPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_notification_mobile_chess_tv"
        },
        {
          "name": "_notification_web_chess_tv"
        },
        {
          "name": "_gameplay_challenge_min_rating"
        },
        {
          "name": "_notification_mobile_game_event"
        },
        {
          "name": "_gameplay_live_allow_offline_challenges"
        },
        {
          "name": "_notification_mobile_new_content"
        },
        {
          "name": "_notification_mobile_my_turn_to_move"
        },
        {
          "name": "_notification_mobile_news_and_announcements"
        },
        {
          "name": "_gameplay_challenge_max_rating"
        },
        {
          "name": "_notification_web_lesson_and_practice"
        },
        {
          "name": "_board_play_sounds"
        },
        {
          "name": "_notification_email_new_content"
        },
        {
          "name": "_notification_email_new_social_trophy"
        },
        {
          "name": "_board_move_method"
        },
        {
          "name": "_board_sound_theme"
        },
        {
          "name": "_notification_email_news_and_announcements"
        },
        {
          "name": "_notification_mobile_friend_activity_updates"
        },
        {
          "name": "_board_move_list_style"
        },
        {
          "name": "_notification_mobile_recommended_match"
        },
        {
          "name": "_notification_email_new_comment"
        },
        {
          "name": "_gameplay_daily_confirm_move"
        },
        {
          "name": "_gameplay_seek_min_rating"
        },
        {
          "name": "_notification_web_new_user_comment"
        },
        {
          "name": "_board_show_legal_moves"
        },
        {
          "name": "_gameplay_show_timestamps"
        },
        {
          "name": "_notification_web_game_event"
        },
        {
          "name": "_privacy_friends_list_privacy"
        },
        {
          "name": "_notification_web_vote_chess"
        },
        {
          "name": "_board_coordinates"
        },
        {
          "name": "_gameplay_live_play_multiple_games"
        },
        {
          "name": "_notification_email_chess_tv"
        },
        {
          "name": "_gameplay_live_auto_promote_queen"
        },
        {
          "name": "_notification_mobile_new_comment"
        },
        {
          "name": "_gameplay_daily_max_days_per_move"
        },
        {
          "name": "_gameplay_confirm_resign"
        },
        {
          "name": "_gameplay_live_seek_base_time_variants"
        },
        {
          "name": "_notification_email_lesson_quota"
        },
        {
          "name": "_notification_email_lesson_and_practice"
        },
        {
          "name": "_gameplay_live_challenge_alerts"
        },
        {
          "name": "_board_white_always_on_bottom"
        },
        {
          "name": "_notification_web_new_comment"
        },
        {
          "name": "_privacy_insights_privacy"
        },
        {
          "name": "_notification_web_new_content"
        },
        {
          "name": "_privacy_allow_friend_requests"
        },
        {
          "name": "_notification_mobile_lesson_quota"
        },
        {
          "name": "_gameplay_live_premoves"
        },
        {
          "name": "_notification_mobile_new_message"
        },
        {
          "name": "_notification_web_news_and_announcements"
        },
        {
          "name": "_notification_email_hero_playing"
        },
        {
          "name": "_gameplay_live_evaluation_bar"
        },
        {
          "name": "_notification_mobile_vote_chess"
        },
        {
          "name": "_notification_web_new_message"
        },
        {
          "name": "_board_highlight_moves"
        },
        {
          "name": "_gameplay_seek_max_rating"
        },
        {
          "name": "_gameplay_analysis_evaluation_bar_mode_wdl_for_openings"
        },
        {
          "name": "_board_board_style"
        },
        {
          "name": "_gameplay_allow_challenges_from"
        },
        {
          "name": "_gameplay_play_streaks"
        },
        {
          "name": "_privacy_allow_global_chat_requests_from"
        },
        {
          "name": "_puzzles_show_details"
        },
        {
          "name": "_notification_web_new_social_trophy"
        },
        {
          "name": "_privacy_blog_privacy"
        },
        {
          "name": "_gameplay_friends_can_challenge_me_no_matter_what"
        },
        {
          "name": "_gameplay_live_seek_filter_premium_only"
        },
        {
          "name": "_notification_email_game_event"
        },
        {
          "name": "_gameplay_seek_game_type"
        },
        {
          "name": "_ui_enable_special_theme_forcing"
        },
        {
          "name": "_gameplay_live_seek_base_time_chess"
        },
        {
          "name": "_notification_mobile_new_user_comment"
        },
        {
          "name": "_notification_email_friend_activity_updates"
        },
        {
          "name": "_gameplay_live_seek_increment_variants"
        },
        {
          "name": "_gameplay_auto_analysis"
        },
        {
          "name": "_privacy_allow_club_invitations"
        },
        {
          "name": "_gameplay_live_low_time_warning"
        },
        {
          "name": "_notification_web_lesson_quota"
        },
        {
          "name": "_gameplay_daily_min_days_per_move"
        },
        {
          "name": "_gameplay_focus_mode"
        },
        {
          "name": "_gameplay_live_seek_is_rated"
        },
        {
          "name": "_gameplay_live_friends_alerts"
        },
        {
          "name": "_privacy_safe_mode"
        },
        {
          "name": "_board_show_animations"
        },
        {
          "name": "_ui_mode"
        },
        {
          "name": "_gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame"
        },
        {
          "name": "_notification_mobile_hero_playing"
        },
        {
          "name": "_notification_mobile_puzzle_reminder"
        },
        {
          "name": "_notification_web_friend_activity_updates"
        },
        {
          "name": "_gameplay_live_engine_evaluation"
        },
        {
          "name": "_notification_email_new_user_comment"
        },
        {
          "name": "_gameplay_allow_game_chat_with"
        },
        {
          "name": "_notification_email_new_friend_request"
        },
        {
          "name": "_notification_email_new_message"
        },
        {
          "name": "_gameplay_live_auto_watch_top_game"
        },
        {
          "name": "_board_pieces_style"
        },
        {
          "name": "_gameplay_live_seek_increment_chess"
        },
        {
          "name": "_notification_mobile_new_friend_request"
        },
        {
          "name": "_gameplay_daily_after_moving"
        },
        {
          "name": "_gameplay_live_allow_chat_requests_from"
        },
        {
          "name": "_notification_email_my_turn_to_move"
        },
        {
          "name": "_notification_mobile_new_social_trophy"
        },
        {
          "name": "_gameplay_daily_max_game_count"
        },
        {
          "name": "_puzzles_show_timer"
        },
        {
          "name": "_privacy_notes_privacy"
        },
        {
          "name": "_learn_coach"
        },
        {
          "name": "_gameplay_live_right_button_arrows"
        },
        {
          "name": "_privacy_allow_tournament_invitations"
        },
        {
          "name": "_notification_web_new_friend_request"
        },
        {
          "name": "_gameplay_live_event_announcements"
        },
        {
          "name": "_notification_email_puzzle_reminder"
        },
        {
          "name": "_notification_email_vote_chess"
        },
        {
          "name": "_notification_auto_track_content"
        },
        {
          "name": "_gameplay_live_seek_filter_hide_variants"
        },
        {
          "name": "_privacy_messages_privacy"
        },
        {
          "name": "_gameplay_live_seek_filter_rated_only"
        },
        {
          "name": "_notification_web_my_turn_to_move"
        },
        {
          "name": "_gameplay_live_auto_switch_game"
        },
        {
          "name": "_notification_web_hero_playing"
        },
        {
          "name": "_gameplay_daily_auto_win_on_time"
        },
        {
          "name": "_board_animation_type"
        },
        {
          "name": "_notification_mobile_lesson_and_practice"
        },
        {
          "name": "_board_win_celebration"
        },
        {
          "name": "_notification_web_streaks_reminders"
        },
        {
          "name": "_notification_mobile_streaks_reminders"
        },
        {
          "name": "_notification_email_streaks_reminders"
        },
        {
          "name": "_notification_web_leagues_reminders"
        },
        {
          "name": "_notification_mobile_leagues_reminders"
        },
        {
          "name": "_notification_email_leagues_reminders"
        },
        {
          "name": "_puzzles_show_classic_mode"
        },
        {
          "name": "_gameplay_show_membership_badges"
        },
        {
          "name": "_learn_coach_id"
        },
        {
          "name": "_learn_coach_nudge"
        },
        {
          "name": "_toaster_center_show_club_request_toasters"
        },
        {
          "name": "_toaster_center_show_friend_request_toasters"
        },
        {
          "name": "_toaster_center_automatically_expand_toasters"
        },
        {
          "name": "_board_castling_type"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "UserSettingsPropertyDefinition",
      "value": [
        {
          "name": "USER_SETTINGS_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "NOTIFICATION_MOBILE_CHESS_TV",
          "number": 1,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_CHESS_TV",
          "number": 2,
          "options": {}
        },
        {
          "name": "GAMEPLAY_CHALLENGE_MIN_RATING",
          "number": 3,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_GAME_EVENT",
          "number": 4,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_ALLOW_OFFLINE_CHALLENGES",
          "number": 5,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_NEW_CONTENT",
          "number": 6,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_MY_TURN_TO_MOVE",
          "number": 7,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_NEWS_AND_ANNOUNCEMENTS",
          "number": 8,
          "options": {}
        },
        {
          "name": "GAMEPLAY_CHALLENGE_MAX_RATING",
          "number": 9,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_LESSON_AND_PRACTICE",
          "number": 10,
          "options": {}
        },
        {
          "name": "BOARD_PLAY_SOUNDS",
          "number": 11,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_NEW_CONTENT",
          "number": 12,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_NEW_SOCIAL_TROPHY",
          "number": 13,
          "options": {}
        },
        {
          "name": "BOARD_MOVE_METHOD",
          "number": 14,
          "options": {}
        },
        {
          "name": "BOARD_SOUND_THEME",
          "number": 15,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "NOTIFICATION_EMAIL_NEWS_AND_ANNOUNCEMENTS",
          "number": 16,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_FRIEND_ACTIVITY_UPDATES",
          "number": 17,
          "options": {}
        },
        {
          "name": "BOARD_MOVE_LIST_STYLE",
          "number": 18,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_RECOMMENDED_MATCH",
          "number": 19,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_NEW_COMMENT",
          "number": 20,
          "options": {}
        },
        {
          "name": "GAMEPLAY_DAILY_CONFIRM_MOVE",
          "number": 21,
          "options": {}
        },
        {
          "name": "GAMEPLAY_SEEK_MIN_RATING",
          "number": 22,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_NEW_USER_COMMENT",
          "number": 23,
          "options": {}
        },
        {
          "name": "BOARD_SHOW_LEGAL_MOVES",
          "number": 24,
          "options": {}
        },
        {
          "name": "GAMEPLAY_SHOW_TIMESTAMPS",
          "number": 25,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_GAME_EVENT",
          "number": 26,
          "options": {}
        },
        {
          "name": "PRIVACY_FRIENDS_LIST_PRIVACY",
          "number": 27,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_VOTE_CHESS",
          "number": 28,
          "options": {}
        },
        {
          "name": "BOARD_COORDINATES",
          "number": 29,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_PLAY_MULTIPLE_GAMES",
          "number": 30,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_CHESS_TV",
          "number": 31,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_AUTO_PROMOTE_QUEEN",
          "number": 32,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_NEW_COMMENT",
          "number": 33,
          "options": {}
        },
        {
          "name": "GAMEPLAY_DAILY_MAX_DAYS_PER_MOVE",
          "number": 34,
          "options": {}
        },
        {
          "name": "GAMEPLAY_CONFIRM_RESIGN",
          "number": 35,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_SEEK_BASE_TIME_VARIANTS",
          "number": 36,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_LESSON_QUOTA",
          "number": 37,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_LESSON_AND_PRACTICE",
          "number": 38,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_CHALLENGE_ALERTS",
          "number": 39,
          "options": {}
        },
        {
          "name": "BOARD_WHITE_ALWAYS_ON_BOTTOM",
          "number": 40,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_NEW_COMMENT",
          "number": 41,
          "options": {}
        },
        {
          "name": "PRIVACY_INSIGHTS_PRIVACY",
          "number": 42,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_NEW_CONTENT",
          "number": 43,
          "options": {}
        },
        {
          "name": "PRIVACY_ALLOW_FRIEND_REQUESTS",
          "number": 44,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_LESSON_QUOTA",
          "number": 45,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_PREMOVES",
          "number": 46,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_NEW_MESSAGE",
          "number": 47,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_NEWS_AND_ANNOUNCEMENTS",
          "number": 48,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_HERO_PLAYING",
          "number": 49,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_EVALUATION_BAR",
          "number": 50,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_VOTE_CHESS",
          "number": 51,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_NEW_MESSAGE",
          "number": 52,
          "options": {}
        },
        {
          "name": "BOARD_HIGHLIGHT_MOVES",
          "number": 53,
          "options": {}
        },
        {
          "name": "GAMEPLAY_SEEK_MAX_RATING",
          "number": 54,
          "options": {}
        },
        {
          "name": "GAMEPLAY_ANALYSIS_EVALUATION_BAR_MODE_WDL_FOR_OPENINGS",
          "number": 55,
          "options": {}
        },
        {
          "name": "BOARD_BOARD_STYLE",
          "number": 56,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "GAMEPLAY_ALLOW_CHALLENGES_FROM",
          "number": 57,
          "options": {}
        },
        {
          "name": "GAMEPLAY_PLAY_STREAKS",
          "number": 58,
          "options": {}
        },
        {
          "name": "PRIVACY_ALLOW_GLOBAL_CHAT_REQUESTS_FROM",
          "number": 59,
          "options": {}
        },
        {
          "name": "PUZZLES_SHOW_DETAILS",
          "number": 60,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_NEW_SOCIAL_TROPHY",
          "number": 61,
          "options": {}
        },
        {
          "name": "PRIVACY_BLOG_PRIVACY",
          "number": 62,
          "options": {}
        },
        {
          "name": "GAMEPLAY_FRIENDS_CAN_CHALLENGE_ME_NO_MATTER_WHAT",
          "number": 63,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_SEEK_FILTER_PREMIUM_ONLY",
          "number": 64,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_GAME_EVENT",
          "number": 65,
          "options": {}
        },
        {
          "name": "GAMEPLAY_SEEK_GAME_TYPE",
          "number": 66,
          "options": {}
        },
        {
          "name": "UI_ENABLE_SPECIAL_THEME_FORCING",
          "number": 67,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_SEEK_BASE_TIME_CHESS",
          "number": 68,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_NEW_USER_COMMENT",
          "number": 69,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_FRIEND_ACTIVITY_UPDATES",
          "number": 70,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_SEEK_INCREMENT_VARIANTS",
          "number": 71,
          "options": {}
        },
        {
          "name": "GAMEPLAY_AUTO_ANALYSIS",
          "number": 72,
          "options": {}
        },
        {
          "name": "PRIVACY_ALLOW_CLUB_INVITATIONS",
          "number": 73,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_LOW_TIME_WARNING",
          "number": 74,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_LESSON_QUOTA",
          "number": 75,
          "options": {}
        },
        {
          "name": "GAMEPLAY_DAILY_MIN_DAYS_PER_MOVE",
          "number": 76,
          "options": {}
        },
        {
          "name": "GAMEPLAY_FOCUS_MODE",
          "number": 77,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_SEEK_IS_RATED",
          "number": 78,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_FRIENDS_ALERTS",
          "number": 79,
          "options": {}
        },
        {
          "name": "PRIVACY_SAFE_MODE",
          "number": 80,
          "options": {}
        },
        {
          "name": "BOARD_SHOW_ANIMATIONS",
          "number": 81,
          "options": {}
        },
        {
          "name": "UI_MODE",
          "number": 82,
          "options": {}
        },
        {
          "name": "GAMEPLAY_ANALYSIS_EVALUATION_BAR_MODE_TABLEBASE_IN_ENDGAME",
          "number": 83,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_HERO_PLAYING",
          "number": 84,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_PUZZLE_REMINDER",
          "number": 85,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_FRIEND_ACTIVITY_UPDATES",
          "number": 86,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_ENGINE_EVALUATION",
          "number": 87,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_NEW_USER_COMMENT",
          "number": 88,
          "options": {}
        },
        {
          "name": "GAMEPLAY_ALLOW_GAME_CHAT_WITH",
          "number": 89,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_NEW_FRIEND_REQUEST",
          "number": 90,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_NEW_MESSAGE",
          "number": 91,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_AUTO_WATCH_TOP_GAME",
          "number": 92,
          "options": {}
        },
        {
          "name": "BOARD_PIECES_STYLE",
          "number": 93,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "GAMEPLAY_LIVE_SEEK_INCREMENT_CHESS",
          "number": 94,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_NEW_FRIEND_REQUEST",
          "number": 95,
          "options": {}
        },
        {
          "name": "GAMEPLAY_DAILY_AFTER_MOVING",
          "number": 96,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_ALLOW_CHAT_REQUESTS_FROM",
          "number": 97,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_MY_TURN_TO_MOVE",
          "number": 98,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_NEW_SOCIAL_TROPHY",
          "number": 99,
          "options": {}
        },
        {
          "name": "GAMEPLAY_DAILY_MAX_GAME_COUNT",
          "number": 100,
          "options": {}
        },
        {
          "name": "PUZZLES_SHOW_TIMER",
          "number": 101,
          "options": {}
        },
        {
          "name": "PRIVACY_NOTES_PRIVACY",
          "number": 102,
          "options": {}
        },
        {
          "name": "LEARN_COACH",
          "number": 103,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_RIGHT_BUTTON_ARROWS",
          "number": 104,
          "options": {}
        },
        {
          "name": "PRIVACY_ALLOW_TOURNAMENT_INVITATIONS",
          "number": 105,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_NEW_FRIEND_REQUEST",
          "number": 106,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_EVENT_ANNOUNCEMENTS",
          "number": 107,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_PUZZLE_REMINDER",
          "number": 108,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_VOTE_CHESS",
          "number": 109,
          "options": {}
        },
        {
          "name": "NOTIFICATION_AUTO_TRACK_CONTENT",
          "number": 110,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_SEEK_FILTER_HIDE_VARIANTS",
          "number": 111,
          "options": {}
        },
        {
          "name": "PRIVACY_MESSAGES_PRIVACY",
          "number": 112,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_SEEK_FILTER_RATED_ONLY",
          "number": 113,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_MY_TURN_TO_MOVE",
          "number": 114,
          "options": {}
        },
        {
          "name": "GAMEPLAY_LIVE_AUTO_SWITCH_GAME",
          "number": 115,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_HERO_PLAYING",
          "number": 116,
          "options": {}
        },
        {
          "name": "GAMEPLAY_DAILY_AUTO_WIN_ON_TIME",
          "number": 117,
          "options": {}
        },
        {
          "name": "BOARD_ANIMATION_TYPE",
          "number": 118,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_LESSON_AND_PRACTICE",
          "number": 119,
          "options": {}
        },
        {
          "name": "BOARD_WIN_CELEBRATION",
          "number": 120,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_STREAKS_REMINDERS",
          "number": 121,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_STREAKS_REMINDERS",
          "number": 122,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_STREAKS_REMINDERS",
          "number": 123,
          "options": {}
        },
        {
          "name": "NOTIFICATION_WEB_LEAGUES_REMINDERS",
          "number": 124,
          "options": {}
        },
        {
          "name": "NOTIFICATION_MOBILE_LEAGUES_REMINDERS",
          "number": 125,
          "options": {}
        },
        {
          "name": "NOTIFICATION_EMAIL_LEAGUES_REMINDERS",
          "number": 126,
          "options": {}
        },
        {
          "name": "PUZZLES_SHOW_CLASSIC_MODE",
          "number": 127,
          "options": {}
        },
        {
          "name": "GAMEPLAY_SHOW_MEMBERSHIP_BADGES",
          "number": 128,
          "options": {}
        },
        {
          "name": "LEARN_COACH_ID",
          "number": 129,
          "options": {}
        },
        {
          "name": "LEARN_COACH_NUDGE",
          "number": 130,
          "options": {}
        },
        {
          "name": "TOASTER_CENTER_SHOW_CLUB_REQUEST_TOASTERS",
          "number": 131,
          "options": {}
        },
        {
          "name": "TOASTER_CENTER_SHOW_FRIEND_REQUEST_TOASTERS",
          "number": 132,
          "options": {}
        },
        {
          "name": "TOASTER_CENTER_AUTOMATICALLY_EXPAND_TOASTERS",
          "number": 133,
          "options": {}
        },
        {
          "name": "BOARD_CASTLING_TYPE",
          "number": 134,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "options": {
    "deprecated": true
  },
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 457156.

```text
JFVklPVVMQKhotCAHCPigSGnRvdXJuYW1lbnRfcG9pbnRzX3ByZXZpb3VzIAE6BgiAms+yBkgCGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_user_settings.proto":"CjpjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc191c2VyX3NldHRpbmdzLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEi2FoKFFVzZXJTZXR0aW5nc1Byb3BlcnR5Ei4KHG5vdGlmaWNhdGlvbl9tb2JpbGVfY2hlc3NfdHYYASABKAhCA9g/AUgAiAEBEisKGW5vdGlmaWNhdGlvbl93ZWJfY2hlc3NfdHYYAiA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17818"></a>
## FND-17818: Full frontend descriptor: chesscom/user_properties/v1/properties_puzzles_attempted.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_puzzles_attempted.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "PuzzlesAttemptedProperty",
      "field": [
        {
          "name": "last_timestamp",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "rating",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "total_seconds",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "rated_attempt_count",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "rated_passed_count",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "unrated_attempt_count",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "min_rating",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "min_rating_timestamp",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "max_rating",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "max_rating_timestamp",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "rated_longest_streak",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "rated_longest_streak_timestamp",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "rated_current_streak",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "history_reset_last_timestamp",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "shadow_rating",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "min_shadow_rating",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "min_shadow_rating_timestamp",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "max_shadow_rating",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "max_shadow_rating_timestamp",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "boosted_shadow_rating",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "min_boosted_shadow_rating",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "min_boosted_shadow_rating_timestamp",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "max_boosted_shadow_rating",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 22,
          "proto3_optional": true
        },
        {
          "name": "max_boosted_shadow_rating_timestamp",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 23,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1020,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_last_timestamp"
        },
        {
          "name": "_rating"
        },
        {
          "name": "_total_seconds"
        },
        {
          "name": "_rated_attempt_count"
        },
        {
          "name": "_rated_passed_count"
        },
        {
          "name": "_unrated_attempt_count"
        },
        {
          "name": "_min_rating"
        },
        {
          "name": "_min_rating_timestamp"
        },
        {
          "name": "_max_rating"
        },
        {
          "name": "_max_rating_timestamp"
        },
        {
          "name": "_rated_longest_streak"
        },
        {
          "name": "_rated_longest_streak_timestamp"
        },
        {
          "name": "_rated_current_streak"
        },
        {
          "name": "_history_reset_last_timestamp"
        },
        {
          "name": "_shadow_rating"
        },
        {
          "name": "_min_shadow_rating"
        },
        {
          "name": "_min_shadow_rating_timestamp"
        },
        {
          "name": "_max_shadow_rating"
        },
        {
          "name": "_max_shadow_rating_timestamp"
        },
        {
          "name": "_boosted_shadow_rating"
        },
        {
          "name": "_min_boosted_shadow_rating"
        },
        {
          "name": "_min_boosted_shadow_rating_timestamp"
        },
        {
          "name": "_max_boosted_shadow_rating"
        },
        {
          "name": "_max_boosted_shadow_rating_timestamp"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "PuzzlesAttemptedPropertyDefinition",
      "value": [
        {
          "name": "PUZZLES_ATTEMPTED_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PUZZLES_ATTEMPTED_LAST_TIMESTAMP",
          "number": 1,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_RATING",
          "number": 2,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_TOTAL_SECONDS",
          "number": 3,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_RATED_ATTEMPT_COUNT",
          "number": 4,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_RATED_PASSED_COUNT",
          "number": 5,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_UNRATED_ATTEMPT_COUNT",
          "number": 6,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_MIN_RATING",
          "number": 7,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_MIN_RATING_TIMESTAMP",
          "number": 8,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_MAX_RATING",
          "number": 9,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_MAX_RATING_TIMESTAMP",
          "number": 10,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK",
          "number": 11,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_RATED_LONGEST_STREAK_TIMESTAMP",
          "number": 12,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_RATED_CURRENT_STREAK",
          "number": 13,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_HISTORY_RESET_LAST_TIMESTAMP",
          "number": 14,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_SHADOW_RATING",
          "number": 15,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_MIN_SHADOW_RATING",
          "number": 16,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_MIN_SHADOW_RATING_TIMESTAMP",
          "number": 17,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_MAX_SHADOW_RATING",
          "number": 18,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_MAX_SHADOW_RATING_TIMESTAMP",
          "number": 19,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_BOOSTED_SHADOW_RATING",
          "number": 20,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING",
          "number": 21,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_MIN_BOOSTED_SHADOW_RATING_TIMESTAMP",
          "number": 22,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING",
          "number": 23,
          "options": {}
        },
        {
          "name": "PUZZLES_ATTEMPTED_MAX_BOOSTED_SHADOW_RATING_TIMESTAMP",
          "number": 24,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 487459.

```text
5HX1RZUEUQhgEaJ8I+JBoeSG93IGNhc3RsaW5nIHdpbGwgYmUgcGVyZm9ybWVkIAFIAhoHiqYdAwoBAUIDuAEBYgZwcm90bzM","chesscom/user_properties/v1/properties_puzzles_attempted.proto":"Cj5jaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19wdXp6bGVzX2F0dGVtcHRlZC5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIs4PChhQdXp6bGVzQXR0ZW1wdGVkUHJvcGVydHkSPAoObGFzdF90aW1lc3RhbXAYASABKAsyGi5nb29nbGUucHJvdG9idWYuVGltZXN0YW1wQgPgPwFIAIgBARIYCgZyYXR
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17819"></a>
## FND-17819: Full frontend descriptor: chesscom/user_properties/v1/properties_daily_puzzles_solved.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_daily_puzzles_solved.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "DailyPuzzlesSolvedProperty",
      "field": [
        {
          "name": "last_completed_timestamp",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "current_streak",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "longest_streak",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "longest_streak_timestamp",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "current_streak_is_longest_daily_puzzle_streak",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "current_streak_end_timestamp",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1025,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_last_completed_timestamp"
        },
        {
          "name": "_current_streak"
        },
        {
          "name": "_longest_streak"
        },
        {
          "name": "_longest_streak_timestamp"
        },
        {
          "name": "_current_streak_is_longest_daily_puzzle_streak"
        },
        {
          "name": "_current_streak_end_timestamp"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "DailyPuzzlesSolvedPropertyDefinition",
      "value": [
        {
          "name": "DAILY_PUZZLES_SOLVED_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "DAILY_PUZZLES_LAST_COMPLETED_TIMESTAMP",
          "number": 1,
          "options": {}
        },
        {
          "name": "DAILY_PUZZLES_CURRENT_STREAK",
          "number": 2,
          "options": {}
        },
        {
          "name": "DAILY_PUZZLES_LONGEST_STREAK",
          "number": 3,
          "options": {}
        },
        {
          "name": "DAILY_PUZZLES_LONGEST_STREAK_TIMESTAMP",
          "number": 4,
          "options": {}
        },
        {
          "name": "DAILY_PUZZLES_CURRENT_STREAK_IS_LONGEST_DAILY_PUZZLE_STREAK",
          "number": 5,
          "options": {}
        },
        {
          "name": "DAILY_PUZZLES_CURRENT_STREAK_END_TIMESTAMP",
          "number": 6,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 493274.

```text
VUaW1lIGF0IHdoaWNoIG1heCBib29zdGVkIHVzZXIgc2hhZG93IHJhdGluZyBvY2N1cnJlZCAAGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_daily_puzzles_solved.proto":"CkFjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19kYWlseV9wdXp6bGVzX3NvbHZlZC5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIr0FChpEYWlseVB1enpsZXNTb2x2ZWRQcm9wZXJ0eRJGChhsYXN0X2NvbXBsZXRlZF90aW1lc3RhbXAYASABKAsyGi5nb29nbGUucHJvdG9idWYuVGltZXN0YW1w
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17820"></a>
## FND-17820: Full frontend descriptor: chesscom/user_properties/v1/properties_clubs.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_clubs.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "ClubsProperty",
      "field": [
        {
          "name": "clubs_joined",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "clubs_banned",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "clubs_joined_count",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {}
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1021,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.ClubsPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "ClubsPropertyDefinition",
      "value": [
        {
          "name": "CLUBS_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CLUBS_JOINED",
          "number": 1,
          "options": {}
        },
        {
          "name": "CLUBS_BANNED",
          "number": 2,
          "options": {}
        },
        {
          "name": "CLUBS_JOINED_COUNT",
          "number": 3,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 495291.

```text
VAQBhoywj4vGilEYWlseSBwdXp6bGUgY3VycmVudCBzdHJlYWsgZW5kIHRpbWVzdGFtcCABSAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_clubs.proto":"CjJjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19jbHVicy5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIuUBCg1DbHVic1Byb3BlcnR5EhkKDGNsdWJzX2pvaW5lZBgBIAMoCUID6D8BEhkKDGNsdWJzX2Jhbm5lZBgCIAMoCUID6D8CEh8KEmNsdWJzX2pvaW5lZF9jb3VudBgDIAEoBUID6D8DMnQKCmRlZmluaXRpb24
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17821"></a>
## FND-17821: Full frontend descriptor: chesscom/user_properties/v1/properties_puzzle_battle.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_puzzle_battle.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "PuzzleBattleProperty",
      "field": [
        {
          "name": "win_streak",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1022,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PuzzleBattlePropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_win_streak"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "PuzzleBattlePropertyDefinition",
      "value": [
        {
          "name": "PUZZLES_BATTLE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PUZZLE_BATTLE_WIN_STREAK",
          "number": 1,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 495983.

```text
DTFVCU19CQU5ORUQQAhoHwj4EIAFIAhIfChJDTFVCU19KT0lORURfQ09VTlQQAxoHwj4EIAFIAhoHiqYdAwoBAWIGcHJvdG8z","chesscom/user_properties/v1/properties_puzzle_battle.proto":"CjpjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19wdXp6bGVfYmF0dGxlLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEiyQEKFFB1enpsZUJhdHRsZVByb3BlcnR5EhwKCndpbl9zdHJlYWsYASABKAVCA/A/AUgAiAEBMnsKCmRlZmluaXRpb24SHS5nb29nbGUucHJvdG9idWYuRmllbGRPcHRpb25zGP4HIAE
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17822"></a>
## FND-17822: Full frontend descriptor: chesscom/user_properties/v1/properties_audiences.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_audiences.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "AudiencesProperty",
      "field": [
        {
          "name": "member_of",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "member_of_last_update",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "ephemeral_audiences_member_of",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "ephemeral_audiences_member_of_last_update",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1023,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.AudiencesPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_member_of_last_update"
        },
        {
          "name": "_ephemeral_audiences_member_of_last_update"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "AudiencesPropertyDefinition",
      "value": [
        {
          "name": "AUDIENCES_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "AUDIENCES_MEMBER_OF",
          "number": 1,
          "options": {}
        },
        {
          "name": "AUDIENCES_MEMBER_OF_LAST_UPDATE",
          "number": 2,
          "options": {}
        },
        {
          "name": "EPHEMERAL_AUDIENCES_MEMBER_OF",
          "number": 3,
          "options": {}
        },
        {
          "name": "EPHEMERAL_AUDIENCES_MEMBER_OF_LAST_UPDATE",
          "number": 4,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 496638.

```text
9CQVRUTEVfV0lOX1NUUkVBSxABGiLCPh8aGVVzZXIgcHV6emxlIGJhdHRsZSBzdHJlYWsgAEgCGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_audiences.proto":"CjZjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19hdWRpZW5jZXMucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSLAAwoRQXVkaWVuY2VzUHJvcGVydHkSFgoJbWVtYmVyX29mGAEgAygJQgP4PwESQwoVbWVtYmVyX29mX2xhc3RfdXBkYXRlGAIgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcEID+D8CSAC
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17823"></a>
## FND-17823: Full frontend descriptor: chesscom/user_properties/v1/properties_trust_and_safety.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_trust_and_safety.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "UserAbuseProperty",
      "field": [
        {
          "name": "abuse_score_automod",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "abuse_score_light",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "abuse_score_heavy",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "abuse_score_total",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "username_abuse_category_score_good",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "username_abuse_category_score_identity_hate",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "username_abuse_category_score_profanity",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "username_abuse_category_score_sexual",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "username_abuse_category_score_violent",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "username_abuse_category_score_pedophilic",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "last_username_abuse_prediction_date",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "username_abuse_confidence_score",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "abusive_chat_messages",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "about_last_updated_at",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 13,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1024,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.UserAbusePropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_abuse_score_automod"
        },
        {
          "name": "_abuse_score_light"
        },
        {
          "name": "_abuse_score_heavy"
        },
        {
          "name": "_abuse_score_total"
        },
        {
          "name": "_username_abuse_category_score_good"
        },
        {
          "name": "_username_abuse_category_score_identity_hate"
        },
        {
          "name": "_username_abuse_category_score_profanity"
        },
        {
          "name": "_username_abuse_category_score_sexual"
        },
        {
          "name": "_username_abuse_category_score_violent"
        },
        {
          "name": "_username_abuse_category_score_pedophilic"
        },
        {
          "name": "_last_username_abuse_prediction_date"
        },
        {
          "name": "_username_abuse_confidence_score"
        },
        {
          "name": "_abusive_chat_messages"
        },
        {
          "name": "_about_last_updated_at"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "UserAbusePropertyDefinition",
      "value": [
        {
          "name": "USER_ABUSE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ABUSE_SCORE_AUTOMOD",
          "number": 1,
          "options": {}
        },
        {
          "name": "ABUSE_SCORE_LIGHT",
          "number": 2,
          "options": {}
        },
        {
          "name": "ABUSE_SCORE_HEAVY",
          "number": 3,
          "options": {}
        },
        {
          "name": "ABUSE_SCORE_TOTAL",
          "number": 4,
          "options": {}
        },
        {
          "name": "USERNAME_ABUSE_CATEGORY_SCORE_GOOD",
          "number": 5,
          "options": {}
        },
        {
          "name": "USERNAME_ABUSE_CATEGORY_SCORE_IDENTITY_HATE",
          "number": 6,
          "options": {}
        },
        {
          "name": "USERNAME_ABUSE_CATEGORY_SCORE_PROFANITY",
          "number": 7,
          "options": {}
        },
        {
          "name": "USERNAME_ABUSE_CATEGORY_SCORE_SEXUAL",
          "number": 8,
          "options": {}
        },
        {
          "name": "USERNAME_ABUSE_CATEGORY_SCORE_VIOLENT",
          "number": 9,
          "options": {}
        },
        {
          "name": "USERNAME_ABUSE_CATEGORY_SCORE_PEDOPHILIC",
          "number": 10,
          "options": {}
        },
        {
          "name": "LAST_USERNAME_ABUSE_PREDICTION_DATE",
          "number": 11,
          "options": {}
        },
        {
          "name": "USERNAME_ABUSE_CONFIDENCE_SCORE",
          "number": 12,
          "options": {}
        },
        {
          "name": "ABUSIVE_CHAT_MESSAGES",
          "number": 13,
          "options": {}
        },
        {
          "name": "ABOUT_LAST_UPDATED_AT",
          "number": 14,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 498161.

```text
dlIGFkZGVkL3JlbW92ZWQgdGhpcyB1c2VyIGZyb20gYW4gZXBoZW1lcmFsIGF1ZGllbmNlLiABGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_trust_and_safety.proto":"Cj1jaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc190cnVzdF9hbmRfc2FmZXR5LnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEi2goKEVVzZXJBYnVzZVByb3BlcnR5EiUKE2FidXNlX3Njb3JlX2F1dG9tb2QYASABKAVCA4BAAUgAiAEBEiMKEWFidXNlX3Njb3JlX2xpZ2h0GAIgASgFQgOAQAJIAYgBARIj
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17824"></a>
## FND-17824: Full frontend descriptor: chesscom/user_properties/v1/properties_time_windows.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_time_windows.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "TimeWindowsPropertiesData",
      "field": [
        {
          "name": "properties",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TimeWindowsPropertiesData.PropertiesEntry",
          "options": {
            "deprecated": true
          }
        }
      ],
      "nested_type": [
        {
          "name": "PropertiesEntry",
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
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.user_properties.v1.TimeWindowsPropertyData"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "TimeWindowsPropertyData",
      "field": [
        {
          "name": "daily_aggregated",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.user_properties.v1.TimeWindowsPropertyData.DailyAggregatedEntry",
          "options": {
            "deprecated": true
          }
        }
      ],
      "nested_type": [
        {
          "name": "DailyAggregatedEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_INT32"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_DOUBLE"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {
        "deprecated": true
      }
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 502568.

```text
vbSBVc2VyQWJvdXRVcGRhdGVkIGV2ZW50cyBmb3IgVCZTIGJpby1zcGFtIG1vbml0b3JpbmcgABoHiqYdAwoBAWIGcHJvdG8z","chesscom/user_properties/v1/properties_time_windows.proto":"CjljaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc190aW1lX3dpbmRvd3MucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSLvAQoZVGltZVdpbmRvd3NQcm9wZXJ0aWVzRGF0YRJeCgpwcm9wZXJ0aWVzGAEgAygLMkYuY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxLlRpbWVXaW5kb3dzUHJvcGVydGllc0RhdGEu
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17825"></a>
## FND-17825: Full frontend descriptor: chesscom/user_properties/v1/properties_play_stats.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_play_stats.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "PlayStatsProperty",
      "field": [
        {
          "name": "avg_moves_per_game",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "avg_opponent_rating",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "highest_opponent_rating",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "highest_rated_opponent_win_game",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "highest_rated_opponent_win_game_timestamp",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "last_game_date",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "total_game_count_all",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "total_game_count_rated",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "total_game_count_unrated",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "total_win_count",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "total_draw_count",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "total_loss_count",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1026,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.PlayStatsPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_avg_moves_per_game"
        },
        {
          "name": "_avg_opponent_rating"
        },
        {
          "name": "_highest_opponent_rating"
        },
        {
          "name": "_highest_rated_opponent_win_game"
        },
        {
          "name": "_highest_rated_opponent_win_game_timestamp"
        },
        {
          "name": "_last_game_date"
        },
        {
          "name": "_total_game_count_all"
        },
        {
          "name": "_total_game_count_rated"
        },
        {
          "name": "_total_game_count_unrated"
        },
        {
          "name": "_total_win_count"
        },
        {
          "name": "_total_draw_count"
        },
        {
          "name": "_total_loss_count"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "PlayStatsPropertyDefinition",
      "value": [
        {
          "name": "PLAY_STATS_PROPERTY_DEFINITION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAY_STATS_PROPERTY_DEFINITION_AVG_MOVES_PER_GAME",
          "number": 1,
          "options": {}
        },
        {
          "name": "PLAY_STATS_PROPERTY_DEFINITION_AVG_OPPONENT_RATING",
          "number": 2,
          "options": {}
        },
        {
          "name": "PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_OPPONENT_RATING",
          "number": 3,
          "options": {}
        },
        {
          "name": "PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME",
          "number": 4,
          "options": {}
        },
        {
          "name": "PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME_TIMESTAMP",
          "number": 5,
          "options": {}
        },
        {
          "name": "PLAY_STATS_PROPERTY_DEFINITION_LAST_GAME_DATE",
          "number": 6,
          "options": {}
        },
        {
          "name": "PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_ALL",
          "number": 7,
          "options": {}
        },
        {
          "name": "PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_RATED",
          "number": 8,
          "options": {}
        },
        {
          "name": "PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_UNRATED",
          "number": 9,
          "options": {}
        },
        {
          "name": "PLAY_STATS_PROPERTY_DEFINITION_TOTAL_WIN_COUNT",
          "number": 10,
          "options": {}
        },
        {
          "name": "PLAY_STATS_PROPERTY_DEFINITION_TOTAL_DRAW_COUNT",
          "number": 11,
          "options": {}
        },
        {
          "name": "PLAY_STATS_PROPERTY_DEFINITION_TOTAL_LOSS_COUNT",
          "number": 12,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 503349.

```text
hREYWlseUFnZ3JlZ2F0ZWRFbnRyeRILCgNrZXkYASABKAUSDQoFdmFsdWUYAiABKAE6AjgBOgkYAYKmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_play_stats.proto":"CjdjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19wbGF5X3N0YXRzLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEigAgKEVBsYXlTdGF0c1Byb3BlcnR5EiQKEmF2Z19tb3Zlc19wZXJfZ2FtZRgBIAEoAUIDkEABSACIAQESJQoTYXZnX29wcG9uZW50X3JhdGluZxgCIAEoAUIDkEACSAGIAQESKQoXaGlnaGVzdF
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17826"></a>
## FND-17826: Full frontend descriptor: chesscom/user_properties/v1/properties_tournament_stats.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_tournament_stats.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "TournamentStatsProperty",
      "field": [
        {
          "name": "game_win_count",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "game_draw_count",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "game_loss_count",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1027,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TournamentStatsPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_game_win_count"
        },
        {
          "name": "_game_draw_count"
        },
        {
          "name": "_game_loss_count"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "TournamentStatsPropertyDefinition",
      "value": [
        {
          "name": "TOURNAMENT_STATS_PROPERTY_DEFINITION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_WIN_COUNT",
          "number": 1,
          "options": {}
        },
        {
          "name": "TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_DRAW_COUNT",
          "number": 2,
          "options": {}
        },
        {
          "name": "TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_LOSS_COUNT",
          "number": 3,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 506484.

```text
EVGSU5JVElPTl9UT1RBTF9MT1NTX0NPVU5UEAwaGcI+FhIQdG90YWxfbG9zc19jb3VudCABSAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_tournament_stats.proto":"Cj1jaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc190b3VybmFtZW50X3N0YXRzLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEixQIKF1RvdXJuYW1lbnRTdGF0c1Byb3BlcnR5EiAKDmdhbWVfd2luX2NvdW50GAEgASgFQgOYQAFIAIgBARIhCg9nYW1lX2RyYXdfY291bnQYAiABKAVCA5hAAkgBiAEBEiEK
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17827"></a>
## FND-17827: Full frontend descriptor: chesscom/user_properties/v1/properties_user_engagement.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_user_engagement.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "UserEngagementProperty",
      "field": [
        {
          "name": "last_bounce_date_sendgrid",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "last_open_email_date_sendgrid",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "last_click_email_date_sendgrid",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "last_bounce_date_iterable",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "last_open_email_date_iterable",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "last_click_email_date_iterable",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "last_dropped_email_date_sendgrid",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "last_spam_report_date_sendgrid",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "last_opened_push_notification_date_firebase",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "last_viewed_payment_page_date",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "last_push_open_date_iterable",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "last_email_complaint_date_iterable",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "total_email_bounces_iterable",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 12,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1028,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.UserEngagementPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_last_bounce_date_sendgrid"
        },
        {
          "name": "_last_open_email_date_sendgrid"
        },
        {
          "name": "_last_click_email_date_sendgrid"
        },
        {
          "name": "_last_bounce_date_iterable"
        },
        {
          "name": "_last_open_email_date_iterable"
        },
        {
          "name": "_last_click_email_date_iterable"
        },
        {
          "name": "_last_dropped_email_date_sendgrid"
        },
        {
          "name": "_last_spam_report_date_sendgrid"
        },
        {
          "name": "_last_opened_push_notification_date_firebase"
        },
        {
          "name": "_last_viewed_payment_page_date"
        },
        {
          "name": "_last_push_open_date_iterable"
        },
        {
          "name": "_last_email_complaint_date_iterable"
        },
        {
          "name": "_total_email_bounces_iterable"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "UserEngagementPropertyDefinition",
      "value": [
        {
          "name": "USER_ENGAGEMENT_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "LAST_BOUNCE_DATE_SENDGRID",
          "number": 1,
          "options": {}
        },
        {
          "name": "LAST_OPEN_EMAIL_DATE_SENDGRID",
          "number": 2,
          "options": {}
        },
        {
          "name": "LAST_CLICK_EMAIL_DATE_SENDGRID",
          "number": 3,
          "options": {}
        },
        {
          "name": "LAST_BOUNCE_DATE_ITERABLE",
          "number": 4,
          "options": {}
        },
        {
          "name": "LAST_OPEN_EMAIL_DATE_ITERABLE",
          "number": 5,
          "options": {}
        },
        {
          "name": "LAST_CLICK_EMAIL_DATE_ITERABLE",
          "number": 6,
          "options": {}
        },
        {
          "name": "LAST_DROPPED_EMAIL_DATE_SENDGRID",
          "number": 7,
          "options": {}
        },
        {
          "name": "LAST_SPAM_REPORT_DATE_SENDGRID",
          "number": 8,
          "options": {}
        },
        {
          "name": "LAST_OPENED_PUSH_NOTIFICATION_DATE_FIREBASE",
          "number": 9,
          "options": {}
        },
        {
          "name": "LAST_VIEWED_PAYMENT_PAGE_DATE",
          "number": 10,
          "options": {}
        },
        {
          "name": "LAST_PUSH_OPEN_DATE_ITERABLE",
          "number": 11,
          "options": {}
        },
        {
          "name": "LAST_EMAIL_COMPLAINT_DATE_ITERABLE",
          "number": 12,
          "options": {}
        },
        {
          "name": "TOTAL_EMAIL_BOUNCES_ITERABLE",
          "number": 13,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 507590.

```text
lfREVGSU5JVElPTl9HQU1FX0xPU1NfQ09VTlQQAxoYwj4VEg9nYW1lX2xvc3NfY291bnQgAUgCGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_user_engagement.proto":"CjxjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc191c2VyX2VuZ2FnZW1lbnQucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSLFDAoWVXNlckVuZ2FnZW1lbnRQcm9wZXJ0eRJHChlsYXN0X2JvdW5jZV9kYXRlX3NlbmRncmlkGAEgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcEIDoEABSACIAQESS
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17828"></a>
## FND-17828: Full frontend descriptor: chesscom/user_properties/v1/properties_coaches.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_coaches.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "CoachesProperty",
      "field": [
        {
          "name": "default_coach_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "default_coach_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "last_selected_coach_name",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "last_selected_coach_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "last_selected_coach_date",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "total_games_started_against_coach",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "coach_rating",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "current_coach_name",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "curent_coach_id",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "total_coach_games",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "has_selected_coach",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "initial_chosen_coach",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "initial_coach",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "last_game_vs_coach_finished",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 13,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1029,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.CoachesPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_default_coach_name"
        },
        {
          "name": "_default_coach_id"
        },
        {
          "name": "_last_selected_coach_name"
        },
        {
          "name": "_last_selected_coach_id"
        },
        {
          "name": "_last_selected_coach_date"
        },
        {
          "name": "_total_games_started_against_coach"
        },
        {
          "name": "_coach_rating"
        },
        {
          "name": "_current_coach_name"
        },
        {
          "name": "_curent_coach_id"
        },
        {
          "name": "_total_coach_games"
        },
        {
          "name": "_has_selected_coach"
        },
        {
          "name": "_initial_chosen_coach"
        },
        {
          "name": "_initial_coach"
        },
        {
          "name": "_last_game_vs_coach_finished"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "CoachesPropertyDefinition",
      "value": [
        {
          "name": "COACHES_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "DEFAULT_COACH_NAME",
          "number": 1,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "DEFAULT_COACH_ID",
          "number": 2,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "LAST_SELECTED_COACH_NAME",
          "number": 3,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "LAST_SELECTED_COACH_ID",
          "number": 4,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "LAST_SELECTED_COACH_DATE",
          "number": 5,
          "options": {}
        },
        {
          "name": "TOTAL_GAMES_STARTED_AGAINST_COACH",
          "number": 6,
          "options": {}
        },
        {
          "name": "COACH_RATING",
          "number": 7,
          "options": {}
        },
        {
          "name": "CURRENT_COACH_NAME",
          "number": 8,
          "options": {}
        },
        {
          "name": "CURRENT_COACH_ID",
          "number": 9,
          "options": {}
        },
        {
          "name": "TOTAL_COACH_GAMES",
          "number": 10,
          "options": {}
        },
        {
          "name": "HAS_SELECTED_COACH",
          "number": 11,
          "options": {}
        },
        {
          "name": "INITIAL_CHOSEN_COACH",
          "number": 12,
          "options": {}
        },
        {
          "name": "INITIAL_COACH",
          "number": 13,
          "options": {}
        },
        {
          "name": "LAST_GAME_VS_COACH_FINISHED",
          "number": 14,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 512223.

```text
JMRRANGjHCPi4aKlRvdGFsIG51bWJlciBvZiBlbWFpbCBib3VuY2VzIGZvciBpdGVyYWJsZSABGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_coaches.proto":"CjRjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19jb2FjaGVzLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEi2ggKD0NvYWNoZXNQcm9wZXJ0eRImChJkZWZhdWx0X2NvYWNoX25hbWUYASABKAlCBRgBqEABSACIAQESJAoQZGVmYXVsdF9jb2FjaF9pZBgCIAEoCUIFGAGoQAJIAYgBARIsChhsYXN0X3NlbGVjdGVkX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17829"></a>
## FND-17829: Full frontend descriptor: chesscom/user_properties/v1/properties_themes.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_themes.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "ThemesProperty",
      "field": [
        {
          "name": "theme_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "custom_background_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "custom_board_style_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "custom_piece_set_id",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "custom_sound_set_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          },
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "background_id",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "board_style_id",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "piece_set_id",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "sound_set_id",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1030,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.ThemesPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_theme_id"
        },
        {
          "name": "_custom_background_id"
        },
        {
          "name": "_custom_board_style_id"
        },
        {
          "name": "_custom_piece_set_id"
        },
        {
          "name": "_custom_sound_set_id"
        },
        {
          "name": "_background_id"
        },
        {
          "name": "_board_style_id"
        },
        {
          "name": "_piece_set_id"
        },
        {
          "name": "_sound_set_id"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "ThemesPropertyDefinition",
      "value": [
        {
          "name": "THEMES_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "THEMES_THEME_ID",
          "number": 1,
          "options": {}
        },
        {
          "name": "THEMES_CUSTOM_BACKGROUND_ID",
          "number": 2,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "THEMES_CUSTOM_BOARD_STYLE_ID",
          "number": 3,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "THEMES_CUSTOM_PIECE_SET_ID",
          "number": 4,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "THEMES_CUSTOM_SOUND_SET_ID",
          "number": 5,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "THEMES_BACKGROUND_ID",
          "number": 6,
          "options": {}
        },
        {
          "name": "THEMES_BOARD_STYLE_ID",
          "number": 7,
          "options": {}
        },
        {
          "name": "THEMES_PIECE_SET_ID",
          "number": 8,
          "options": {}
        },
        {
          "name": "THEMES_SOUND_SET_ID",
          "number": 9,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 515992.

```text
ltZSB0aGUgdXNlciBmaW5pc2hlZCBhIGdhbWUgdnMgYSBjb2FjaCAoUGxheSBDb2FjaCkgAEgCGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_themes.proto":"CjNjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc190aGVtZXMucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSKNBQoOVGhlbWVzUHJvcGVydHkSGgoIdGhlbWVfaWQYASABKAlCA7BAAUgAiAEBEigKFGN1c3RvbV9iYWNrZ3JvdW5kX2lkGAIgASgJQgUYAbBAAkgBiAEBEikKFWN1c3RvbV9ib2FyZF9zdHlsZV9pZBgDIA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17830"></a>
## FND-17830: Full frontend descriptor: chesscom/user_properties/v1/properties_ipqs.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_ipqs.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "IpqsProperty",
      "field": [
        {
          "name": "ipqs_fraud_score",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "ipqs_is_low_quality_email",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "ipqs_first_seen",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "ipqs_is_bot",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "ipqs_is_proxy",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "ipqs_is_known_attacker",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "ipqs_abuse_velocity",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "ipqs_has_abused_recently",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "ipqs_is_vpn",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "ipqs_is_tor",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "ipqs_ip_fraud_score",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "ipqs_ip_has_abused_recently",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "ipqs_definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1031,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.IpqsPropertyDefinition",
          "json_name": "ipqsDefinition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_ipqs_fraud_score"
        },
        {
          "name": "_ipqs_is_low_quality_email"
        },
        {
          "name": "_ipqs_first_seen"
        },
        {
          "name": "_ipqs_is_bot"
        },
        {
          "name": "_ipqs_is_proxy"
        },
        {
          "name": "_ipqs_is_known_attacker"
        },
        {
          "name": "_ipqs_abuse_velocity"
        },
        {
          "name": "_ipqs_has_abused_recently"
        },
        {
          "name": "_ipqs_is_vpn"
        },
        {
          "name": "_ipqs_is_tor"
        },
        {
          "name": "_ipqs_ip_fraud_score"
        },
        {
          "name": "_ipqs_ip_has_abused_recently"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "IpqsPropertyDefinition",
      "value": [
        {
          "name": "IPQS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "IPQS_FRAUD_SCORE",
          "number": 1,
          "options": {}
        },
        {
          "name": "IPQS_IS_LOW_QUALITY_EMAIL",
          "number": 2,
          "options": {}
        },
        {
          "name": "IPQS_FIRST_SEEN",
          "number": 3,
          "options": {}
        },
        {
          "name": "IPQS_IS_BOT",
          "number": 4,
          "options": {}
        },
        {
          "name": "IPQS_IS_PROXY",
          "number": 5,
          "options": {}
        },
        {
          "name": "IPQS_IS_KNOWN_ATTACKER",
          "number": 6,
          "options": {}
        },
        {
          "name": "IPQS_ABUSE_VELOCITY",
          "number": 7,
          "options": {}
        },
        {
          "name": "IPQS_HAS_ABUSED_RECENTLY",
          "number": 8,
          "options": {}
        },
        {
          "name": "IPQS_IS_VPN",
          "number": 9,
          "options": {}
        },
        {
          "name": "IPQS_IS_TOR",
          "number": 10,
          "options": {}
        },
        {
          "name": "IPQS_IP_FRAUD_SCORE",
          "number": 11,
          "options": {}
        },
        {
          "name": "IPQS_IP_HAS_ABUSED_RECENTLY",
          "number": 12,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 518331.

```text
Ro1wj4yGixUaGUgSUQgb2YgdGhlIFNvdW5kIFNldCBzZWxlY3RlZCBieSB0aGUgdXNlciABSAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_ipqs.proto":"CjFjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19pcHFzLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEihwcKDElwcXNQcm9wZXJ0eRIiChBpcHFzX2ZyYXVkX3Njb3JlGAEgASgBQgO4QAFIAIgBARIrChlpcHFzX2lzX2xvd19xdWFsaXR5X2VtYWlsGAIgASgIQgO4QAJIAYgBARI9Cg9pcHFzX2ZpcnN0X3NlZW4YAyAB
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17831"></a>
## FND-17831: Full frontend descriptor: chesscom/user_properties/v1/properties_user_puzzle_stats.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_user_puzzle_stats.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "UserPuzzleStatsProperty",
      "field": [
        {
          "name": "points",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "level",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "tier",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "prestige",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "total_tactics_completed",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1032,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.UserPuzzleStatsPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_points"
        },
        {
          "name": "_level"
        },
        {
          "name": "_tier"
        },
        {
          "name": "_prestige"
        },
        {
          "name": "_total_tactics_completed"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "UserPuzzleStatsPropertyDefinition",
      "value": [
        {
          "name": "USER_PUZZLE_STATS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "USER_PUZZLE_STATS_POINTS",
          "number": 1,
          "options": {}
        },
        {
          "name": "USER_PUZZLE_STATS_LEVEL",
          "number": 2,
          "options": {}
        },
        {
          "name": "USER_PUZZLE_STATS_TIER",
          "number": 3,
          "options": {}
        },
        {
          "name": "USER_PUZZLE_STATS_PRESTIGE",
          "number": 4,
          "options": {}
        },
        {
          "name": "USER_PUZZLE_STATS_TOTAL_TACTICS_COMPLETED",
          "number": 5,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 521942.

```text
jaW91cyBiZWhhdmlvciB3aXRoaW4gdGhlIHBhc3QgZmV3IGRheXMgb24gaXAgZW5kcG9pbnQgABoHiqYdAwoBAWIGcHJvdG8z","chesscom/user_properties/v1/properties_user_puzzle_stats.proto":"Cj5jaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc191c2VyX3B1enpsZV9zdGF0cy5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIvsCChdVc2VyUHV6emxlU3RhdHNQcm9wZXJ0eRIYCgZwb2ludHMYASABKAVCA8BAAUgAiAEBEhcKBWxldmVsGAIgASgFQgPAQAJIAYgBARIWCgR0aWVyGAMgASgFQgPAQAN
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17832"></a>
## FND-17832: Full frontend descriptor: chesscom/user_properties/v1/properties_courses.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_courses.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "CoursesProperty",
      "field": [
        {
          "name": "last_course_purchased_date",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "last_course_study_date",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "number_of_courses_purchased",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "total_courses_spent",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "number_of_diamond_courses_claimed",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "first_courses_session_date",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "last_courses_session_date",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "number_of_courses_refunded",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "number_of_courses_variations_learned",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "number_of_courses_reviews_pending",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "number_of_courses_variations_reviewed",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "number_of_courses_variations_previewed",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "number_of_courses_completed",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "number_of_courses_owned",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "courses_tutorial_claimed",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "number_of_preview_courses_owned",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "courses_ftue_selector_skipped",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "options": {},
          "oneof_index": 16,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1033,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.CoursesPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_last_course_purchased_date"
        },
        {
          "name": "_last_course_study_date"
        },
        {
          "name": "_number_of_courses_purchased"
        },
        {
          "name": "_total_courses_spent"
        },
        {
          "name": "_number_of_diamond_courses_claimed"
        },
        {
          "name": "_first_courses_session_date"
        },
        {
          "name": "_last_courses_session_date"
        },
        {
          "name": "_number_of_courses_refunded"
        },
        {
          "name": "_number_of_courses_variations_learned"
        },
        {
          "name": "_number_of_courses_reviews_pending"
        },
        {
          "name": "_number_of_courses_variations_reviewed"
        },
        {
          "name": "_number_of_courses_variations_previewed"
        },
        {
          "name": "_number_of_courses_completed"
        },
        {
          "name": "_number_of_courses_owned"
        },
        {
          "name": "_courses_tutorial_claimed"
        },
        {
          "name": "_number_of_preview_courses_owned"
        },
        {
          "name": "_courses_ftue_selector_skipped"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "CoursesPropertyDefinition",
      "value": [
        {
          "name": "COURSES_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "LAST_COURSE_PURCHASED_DATE",
          "number": 1,
          "options": {}
        },
        {
          "name": "LAST_COURSE_STUDY_DATE",
          "number": 2,
          "options": {}
        },
        {
          "name": "NUMBER_OF_COURSES_PURCHASED",
          "number": 3,
          "options": {}
        },
        {
          "name": "TOTAL_COURSES_SPENT",
          "number": 4,
          "options": {}
        },
        {
          "name": "NUMBER_OF_DIAMOND_COURSES_CLAIMED",
          "number": 5,
          "options": {}
        },
        {
          "name": "FIRST_COURSES_SESSION_DATE",
          "number": 6,
          "options": {}
        },
        {
          "name": "LAST_COURSES_SESSION_DATE",
          "number": 7,
          "options": {}
        },
        {
          "name": "NUMBER_OF_COURSES_REFUNDED",
          "number": 8,
          "options": {}
        },
        {
          "name": "NUMBER_OF_COURSES_VARIATIONS_LEARNED",
          "number": 9,
          "options": {}
        },
        {
          "name": "NUMBER_OF_COURSES_REVIEWS_PENDING",
          "number": 10,
          "options": {}
        },
        {
          "name": "NUMBER_OF_COURSES_VARIATIONS_REVIEWED",
          "number": 11,
          "options": {}
        },
        {
          "name": "NUMBER_OF_COURSES_VARIATIONS_PREVIEWED",
          "number": 12,
          "options": {}
        },
        {
          "name": "NUMBER_OF_COURSES_COMPLETED",
          "number": 13,
          "options": {}
        },
        {
          "name": "NUMBER_OF_COURSES_OWNED",
          "number": 14,
          "options": {}
        },
        {
          "name": "COURSES_TUTORIAL_CLAIMED",
          "number": 15,
          "options": {}
        },
        {
          "name": "NUMBER_OF_PREVIEW_COURSES_OWNED",
          "number": 16,
          "options": {}
        },
        {
          "name": "COURSES_FTUE_SELECTOR_SKIPPED",
          "number": 17,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 523146.

```text
jcm9zcyBhbGwgbW9kZXMgKHJhdGVkLCB1bnJhdGVkLCBydXNoLCBiYXR0bGUsIGV0Yy4pIABIAhoHiqYdAwoBAWIGcHJvdG8z","chesscom/user_properties/v1/properties_courses.proto":"CjRjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19jb3Vyc2VzLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEi7wwKD0NvdXJzZXNQcm9wZXJ0eRJIChpsYXN0X2NvdXJzZV9wdXJjaGFzZWRfZGF0ZRgBIAEoCzIaLmdvb2dsZS5wcm90b2J1Zi5UaW1lc3RhbXBCA8hAAUgAiAEBEkQKFmxhc3RfY291cnNlX3N0dWR5X
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17833"></a>
## FND-17833: Full frontend descriptor: chesscom/user_properties/v1/properties_survey.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_survey.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "SurveyProperty",
      "field": [
        {
          "name": "survey_question_answers",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "survey_question_dismissals",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1034,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.SurveyPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "SurveyPropertyDefinition",
      "value": [
        {
          "name": "SURVEY_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SURVEY_QUESTION_ANSWERS",
          "number": 1,
          "options": {}
        },
        {
          "name": "SURVEY_QUESTION_DISMISSALS",
          "number": 2,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 527679.

```text
I+NRovRGlkIHRoZSB1c2VyIHNraXAgdGhlIGNvdXJzZXMgdHV0b3JpYWwgc2VsZWN0b3IgAEgCGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_survey.proto":"CjNjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19zdXJ2ZXkucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSLfAQoOU3VydmV5UHJvcGVydHkSJAoXc3VydmV5X3F1ZXN0aW9uX2Fuc3dlcnMYASADKAlCA9BAARInChpzdXJ2ZXlfcXVlc3Rpb25fZGlzbWlzc2FscxgCIAMoCUID0EACMnUKCmRlZmluaXRpb24SHS5nb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17834"></a>
## FND-17834: Full frontend descriptor: chesscom/user_properties/v1/properties_product_activity_rankings.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_product_activity_rankings.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "ProductActivityRankingsProperty",
      "field": [
        {
          "name": "daily_time_on_platform_in_seconds_rank",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "friend_games_rank",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "daily_moves_rank",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "lesson_activity_rank",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "game_reviews_started_rank",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "game_review_activity_rank",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "article_activity_rank",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "events_activity_rank",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "vs_coach_activity_rank",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 8,
          "proto3_optional": true
        },
        {
          "name": "vs_coach_games_rank",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 9,
          "proto3_optional": true
        },
        {
          "name": "live_bullet_games_rank",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 10,
          "proto3_optional": true
        },
        {
          "name": "live_blitz_games_rank",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 11,
          "proto3_optional": true
        },
        {
          "name": "live_rapid_games_rank",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 12,
          "proto3_optional": true
        },
        {
          "name": "lesson_start_rank",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 13,
          "proto3_optional": true
        },
        {
          "name": "social_activity_rank",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 14,
          "proto3_optional": true
        },
        {
          "name": "bot_games_rank",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 15,
          "proto3_optional": true
        },
        {
          "name": "upgrade_activity_rank",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 16,
          "proto3_optional": true
        },
        {
          "name": "active_events_rank",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 17,
          "proto3_optional": true
        },
        {
          "name": "live_games_rank",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 18,
          "proto3_optional": true
        },
        {
          "name": "tournament_games_rank",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 19,
          "proto3_optional": true
        },
        {
          "name": "tactics_rank",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 20,
          "proto3_optional": true
        },
        {
          "name": "puzzle_rushes_rank",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 21,
          "proto3_optional": true
        },
        {
          "name": "puzzle_battles_rank",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 22,
          "proto3_optional": true
        },
        {
          "name": "daily_puzzles_rank",
          "number": 24,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 23,
          "proto3_optional": true
        },
        {
          "name": "courses_started_rank",
          "number": 25,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 24,
          "proto3_optional": true
        },
        {
          "name": "practice_endgame_started_rank",
          "number": 26,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 25,
          "proto3_optional": true
        },
        {
          "name": "analysis_started_rank",
          "number": 27,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 26,
          "proto3_optional": true
        },
        {
          "name": "stats_page_views_rank",
          "number": 28,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 27,
          "proto3_optional": true
        },
        {
          "name": "chess_tv_event_views_rank",
          "number": 29,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 28,
          "proto3_optional": true
        },
        {
          "name": "article_news_blog_forum_views_rank",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 29,
          "proto3_optional": true
        },
        {
          "name": "social_shares_rank",
          "number": 31,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 30,
          "proto3_optional": true
        },
        {
          "name": "chat_messages_rank",
          "number": 32,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 31,
          "proto3_optional": true
        },
        {
          "name": "friends_added_rank",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 32,
          "proto3_optional": true
        },
        {
          "name": "friend_invites_sent_rank",
          "number": 34,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "options": {},
          "oneof_index": 33,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1036,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_daily_time_on_platform_in_seconds_rank"
        },
        {
          "name": "_friend_games_rank"
        },
        {
          "name": "_daily_moves_rank"
        },
        {
          "name": "_lesson_activity_rank"
        },
        {
          "name": "_game_reviews_started_rank"
        },
        {
          "name": "_game_review_activity_rank"
        },
        {
          "name": "_article_activity_rank"
        },
        {
          "name": "_events_activity_rank"
        },
        {
          "name": "_vs_coach_activity_rank"
        },
        {
          "name": "_vs_coach_games_rank"
        },
        {
          "name": "_live_bullet_games_rank"
        },
        {
          "name": "_live_blitz_games_rank"
        },
        {
          "name": "_live_rapid_games_rank"
        },
        {
          "name": "_lesson_start_rank"
        },
        {
          "name": "_social_activity_rank"
        },
        {
          "name": "_bot_games_rank"
        },
        {
          "name": "_upgrade_activity_rank"
        },
        {
          "name": "_active_events_rank"
        },
        {
          "name": "_live_games_rank"
        },
        {
          "name": "_tournament_games_rank"
        },
        {
          "name": "_tactics_rank"
        },
        {
          "name": "_puzzle_rushes_rank"
        },
        {
          "name": "_puzzle_battles_rank"
        },
        {
          "name": "_daily_puzzles_rank"
        },
        {
          "name": "_courses_started_rank"
        },
        {
          "name": "_practice_endgame_started_rank"
        },
        {
          "name": "_analysis_started_rank"
        },
        {
          "name": "_stats_page_views_rank"
        },
        {
          "name": "_chess_tv_event_views_rank"
        },
        {
          "name": "_article_news_blog_forum_views_rank"
        },
        {
          "name": "_social_shares_rank"
        },
        {
          "name": "_chat_messages_rank"
        },
        {
          "name": "_friends_added_rank"
        },
        {
          "name": "_friend_invites_sent_rank"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "ProductActivityRankingsPropertyDefinition",
      "value": [
        {
          "name": "PRODUCT_RANKINGS_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "DAILY_TIME_ON_PLATFORM_IN_SECONDS_RANK",
          "number": 1,
          "options": {}
        },
        {
          "name": "FRIEND_GAMES_RANK",
          "number": 2,
          "options": {}
        },
        {
          "name": "DAILY_MOVES_RANK",
          "number": 3,
          "options": {}
        },
        {
          "name": "LESSON_ACTIVITY_RANK",
          "number": 4,
          "options": {}
        },
        {
          "name": "GAME_REVIEWS_STARTED_RANK",
          "number": 5,
          "options": {}
        },
        {
          "name": "GAME_REVIEW_ACTIVITY_RANK",
          "number": 6,
          "options": {}
        },
        {
          "name": "ARTICLE_ACTIVITY_RANK",
          "number": 7,
          "options": {}
        },
        {
          "name": "EVENTS_ACTIVITY_RANK",
          "number": 8,
          "options": {}
        },
        {
          "name": "VS_COACH_ACTIVITY_RANK",
          "number": 9,
          "options": {}
        },
        {
          "name": "VS_COACH_GAMES_RANK",
          "number": 10,
          "options": {}
        },
        {
          "name": "LIVE_BULLET_GAMES_RANK",
          "number": 11,
          "options": {}
        },
        {
          "name": "LIVE_BLITZ_GAMES_RANK",
          "number": 12,
          "options": {}
        },
        {
          "name": "LIVE_RAPID_GAMES_RANK",
          "number": 13,
          "options": {}
        },
        {
          "name": "LESSON_START_RANK",
          "number": 14,
          "options": {}
        },
        {
          "name": "SOCIAL_ACTIVITY_RANK",
          "number": 15,
          "options": {}
        },
        {
          "name": "BOT_GAMES_RANK",
          "number": 16,
          "options": {}
        },
        {
          "name": "UPGRADE_ACTIVITY_RANK",
          "number": 17,
          "options": {}
        },
        {
          "name": "ACTIVE_EVENTS_RANK",
          "number": 18,
          "options": {}
        },
        {
          "name": "LIVE_GAMES_RANK",
          "number": 19,
          "options": {}
        },
        {
          "name": "TOURNAMENT_GAMES_RANK",
          "number": 20,
          "options": {}
        },
        {
          "name": "TACTICS_RANK",
          "number": 21,
          "options": {}
        },
        {
          "name": "PUZZLE_RUSHES_RANK",
          "number": 22,
          "options": {}
        },
        {
          "name": "PUZZLE_BATTLES_RANK",
          "number": 23,
          "options": {}
        },
        {
          "name": "DAILY_PUZZLES_RANK",
          "number": 24,
          "options": {}
        },
        {
          "name": "COURSES_STARTED_RANK",
          "number": 25,
          "options": {}
        },
        {
          "name": "PRACTICE_ENDGAME_STARTED_RANK",
          "number": 26,
          "options": {}
        },
        {
          "name": "ANALYSIS_STARTED_RANK",
          "number": 27,
          "options": {}
        },
        {
          "name": "STATS_PAGE_VIEWS_RANK",
          "number": 28,
          "options": {}
        },
        {
          "name": "CHESS_TV_EVENT_VIEWS_RANK",
          "number": 29,
          "options": {}
        },
        {
          "name": "ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK",
          "number": 30,
          "options": {}
        },
        {
          "name": "SOCIAL_SHARES_RANK",
          "number": 31,
          "options": {}
        },
        {
          "name": "CHAT_MESSAGES_RANK",
          "number": 32,
          "options": {}
        },
        {
          "name": "FRIENDS_ADDED_RANK",
          "number": 33,
          "options": {}
        },
        {
          "name": "FRIEND_INVITES_SENT_RANK",
          "number": 34,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 528626.

```text
GRpc21pc3NlZCBieSBhIHVzZXIgaW4gZm9ybWF0IHN1cnZleV9rZXk6cXVlc3Rpb25fa2V5IAAaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_product_activity_rankings.proto":"CkZjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19wcm9kdWN0X2FjdGl2aXR5X3JhbmtpbmdzLnByb3RvEhtjaGVzc2NvbS51c2VyX3Byb3BlcnRpZXMudjEijRMKH1Byb2R1Y3RBY3Rpdml0eVJhbmtpbmdzUHJvcGVydHkSOAomZGFpbHlfdGltZV9vbl9wbGF0Zm9ybV9pbl9zZWNvbmRzX3JhbmsYASABKAF
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17835"></a>
## FND-17835: Full frontend descriptor: chesscom/user_properties/v1/properties_turnstile.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_turnstile.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "TurnstileProperty",
      "field": [
        {
          "name": "registration_status",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "turnstile_definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1035,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.TurnstilePropertyDefinition",
          "json_name": "turnstileDefinition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_registration_status"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "TurnstilePropertyDefinition",
      "value": [
        {
          "name": "TURNSTILE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TURNSTILE_REGISTRATION_STATUS",
          "number": 1,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 535341.

```text
lURVNfU0VOVF9SQU5LECIaJsI+IxodUmFuayBmb3IgZnJpZW5kIGludml0ZXMgc2VudC4gAEgBGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_turnstile.proto":"CjZjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc190dXJuc3RpbGUucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSLpAQoRVHVybnN0aWxlUHJvcGVydHkSJQoTcmVnaXN0cmF0aW9uX3N0YXR1cxgBIAEoCUID2EABSACIAQEyiwEKFHR1cm5zdGlsZV9kZWZpbml0aW9uEh0uZ29vZ2xlLnByb3RvYnVmLkZpZWxkT3B
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17836"></a>
## FND-17836: Full frontend descriptor: chesscom/user_properties/v1/properties_user_streak_v2.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_user_streak_v2.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "UserStreakV2Property",
      "field": [
        {
          "name": "updated_at",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "duration_days",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "status_by_days",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "expires_at",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "resets_count",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "longest_streak",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "longest_streak_date",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 5,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1037,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.UserStreakV2PropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_updated_at"
        },
        {
          "name": "_duration_days"
        },
        {
          "name": "_expires_at"
        },
        {
          "name": "_resets_count"
        },
        {
          "name": "_longest_streak"
        },
        {
          "name": "_longest_streak_date"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "UserStreakV2PropertyDefinition",
      "value": [
        {
          "name": "USER_STREAK_V2_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "USER_STREAK_V2_UPDATED_AT",
          "number": 1,
          "options": {}
        },
        {
          "name": "USER_STREAK_V2_DURATION_DAYS",
          "number": 2,
          "options": {}
        },
        {
          "name": "USER_STREAK_V2_STATUS_BY_DAYS",
          "number": 3,
          "options": {}
        },
        {
          "name": "USER_STREAK_V2_EXPIRES_AT",
          "number": 4,
          "options": {}
        },
        {
          "name": "USER_STREAK_V2_RESETS_COUNT",
          "number": 5,
          "options": {}
        },
        {
          "name": "USER_STREAK_V2_LONGEST_STREAK",
          "number": 6,
          "options": {}
        },
        {
          "name": "USER_STREAK_V2_LONGEST_STREAK_DATE",
          "number": 7,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 536056.

```text
42GjRUaGUgdHVybnN0aWxlIHN0YXR1cyB3aGVuIHRoZSBhY2NvdW50IHdhcyByZWdpc3RlcmVkGgeKph0DCgEBYgZwcm90bzM","chesscom/user_properties/v1/properties_user_streak_v2.proto":"CjtjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc191c2VyX3N0cmVha192Mi5wcm90bxIbY2hlc3Njb20udXNlcl9wcm9wZXJ0aWVzLnYxIr8EChRVc2VyU3RyZWFrVjJQcm9wZXJ0eRI4Cgp1cGRhdGVkX2F0GAEgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcEID6EABSACIAQESHwoNZHVyYXRpb25fZGF5cxgCIA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17837"></a>
## FND-17837: Full frontend descriptor: chesscom/user_properties/v1/properties_fair_play.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/user_properties/v1/properties_fair_play.proto",
  "package": "chesscom.user_properties.v1",
  "message_type": [
    {
      "name": "FairPlayProperty",
      "field": [
        {
          "name": "cheat_report_count",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "options": {},
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "last_cheat_report_date",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp",
          "options": {},
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "previous_chance_user",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "next_chance_user",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "second_chance_tag",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {},
          "oneof_index": 4,
          "proto3_optional": true
        }
      ],
      "extension": [
        {
          "name": "definition",
          "extendee": ".google.protobuf.FieldOptions",
          "number": 1038,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.user_properties.v1.FairPlayPropertyDefinition",
          "json_name": "definition"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_cheat_report_count"
        },
        {
          "name": "_last_cheat_report_date"
        },
        {
          "name": "_previous_chance_user"
        },
        {
          "name": "_next_chance_user"
        },
        {
          "name": "_second_chance_tag"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "FairPlayPropertyDefinition",
      "value": [
        {
          "name": "FAIR_PLAY_PROPERTY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CHEAT_REPORT_COUNT",
          "number": 1,
          "options": {}
        },
        {
          "name": "LAST_CHEAT_REPORT_DATE",
          "number": 2,
          "options": {}
        },
        {
          "name": "PREVIOUS_CHANCE_USER",
          "number": 3,
          "options": {}
        },
        {
          "name": "NEXT_CHANCE_USER",
          "number": 4,
          "options": {}
        },
        {
          "name": "SECOND_CHANCE_TAG",
          "number": 5,
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 538275.

```text
jYaMERhdGUgd2hlbiB0aGUgdXNlciBhY2hpZXZlZCB0aGVpciBsb25nZXN0IHN0cmVhayAASAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/user_properties/v1/properties_fair_play.proto":"CjZjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvcHJvcGVydGllc19mYWlyX3BsYXkucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSLnAwoQRmFpclBsYXlQcm9wZXJ0eRIkChJjaGVhdF9yZXBvcnRfY291bnQYASABKAVCA/BAAUgAiAEBEkQKFmxhc3RfY2hlYXRfcmVwb3J0X2RhdGUYAiABKAsyGi5nb29nbGUucHJvdG9idWYuVGl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.
