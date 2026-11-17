# native_interfaces — findings 2301–2400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-14960"></a>
## FND-14960: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_PIN = 19

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_PIN",
  "number": 19,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14961"></a>
## FND-14961: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_KING_SAFETY = 20

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_KING_SAFETY",
  "number": 20,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14962"></a>
## FND-14962: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_PIECE_PLAY = 21

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_PIECE_PLAY",
  "number": 21,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14963"></a>
## FND-14963: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_PAWN_STRUCTURE = 22

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_PAWN_STRUCTURE",
  "number": 22,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14964"></a>
## FND-14964: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_LADDER_MATE = 23

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.PuzzleThemeType",
  "name": "PUZZLE_THEME_TYPE_LADDER_MATE",
  "number": 23,
  "source_id": "SRC-1027",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1027** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_puzzle_gen.proto.bin` — [preserved redacted evidence](../evidence/descriptors/8d035eb5cab1c1c4c316b42970cf8e2a86cd251173399d6207fc0dd11af9dbd5.bin)

**Source references:** SRC-1027, SRC-1797  
**URL references:** None independently associated  
**Related findings:** FND-14810, FND-14811, FND-14812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14965"></a>
## FND-14965: Native message: chesscom.explanation_engine.v1.GamePhaseGlyph

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GamePhaseGlyph",
  "field": [
    {
      "name": "game_phase",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.GamePhase"
    },
    {
      "name": "glyph",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
    }
  ]
}

### Evidence

- **SRC-1028** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_report_card.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9307a252f124e8645a65c22a69f9fe3aef46d01ad127da0070fe1fc14e15c3ff.bin)

**Source references:** SRC-1028, SRC-1676  
**URL references:** None independently associated  
**Related findings:** FND-14966, FND-14967

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14966"></a>
## FND-14966: chesscom.explanation_engine.v1.GamePhaseGlyph.game_phase = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GamePhaseGlyph",
  "name": "game_phase",
  "number": 1,
  "type": ".chesscom.chess.v1.GamePhase",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1028",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1028** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_report_card.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9307a252f124e8645a65c22a69f9fe3aef46d01ad127da0070fe1fc14e15c3ff.bin)

**Source references:** SRC-1028, SRC-1676  
**URL references:** None independently associated  
**Related findings:** FND-14965, FND-14967

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14967"></a>
## FND-14967: chesscom.explanation_engine.v1.GamePhaseGlyph.glyph = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GamePhaseGlyph",
  "name": "glyph",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.MoveClassification",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1028",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1028** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_report_card.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9307a252f124e8645a65c22a69f9fe3aef46d01ad127da0070fe1fc14e15c3ff.bin)

**Source references:** SRC-1028, SRC-1676  
**URL references:** None independently associated  
**Related findings:** FND-14965, FND-14966

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14968"></a>
## FND-14968: Native message: chesscom.explanation_engine.v1.PlayerReportCard

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PlayerReportCard",
  "field": [
    {
      "name": "color",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Color"
    },
    {
      "name": "glyph_by_phase",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.GamePhaseGlyph"
    },
    {
      "name": "effective_rating",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-1028** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_report_card.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9307a252f124e8645a65c22a69f9fe3aef46d01ad127da0070fe1fc14e15c3ff.bin)

**Source references:** SRC-1028, SRC-1676  
**URL references:** None independently associated  
**Related findings:** FND-14965, FND-14966, FND-14967

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14969"></a>
## FND-14969: chesscom.explanation_engine.v1.PlayerReportCard.color = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PlayerReportCard",
  "name": "color",
  "number": 1,
  "type": ".chesscom.chess.v1.Color",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1028",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1028** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_report_card.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9307a252f124e8645a65c22a69f9fe3aef46d01ad127da0070fe1fc14e15c3ff.bin)

**Source references:** SRC-1028, SRC-1676  
**URL references:** None independently associated  
**Related findings:** FND-14965, FND-14966, FND-14967

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14970"></a>
## FND-14970: chesscom.explanation_engine.v1.PlayerReportCard.glyph_by_phase = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PlayerReportCard",
  "name": "glyph_by_phase",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.GamePhaseGlyph",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1028",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1028** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_report_card.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9307a252f124e8645a65c22a69f9fe3aef46d01ad127da0070fe1fc14e15c3ff.bin)

**Source references:** SRC-1028, SRC-1676  
**URL references:** None independently associated  
**Related findings:** FND-14965, FND-14966, FND-14967

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14971"></a>
## FND-14971: chesscom.explanation_engine.v1.PlayerReportCard.effective_rating = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.PlayerReportCard",
  "name": "effective_rating",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1028",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1028** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_report_card.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9307a252f124e8645a65c22a69f9fe3aef46d01ad127da0070fe1fc14e15c3ff.bin)

**Source references:** SRC-1028, SRC-1676  
**URL references:** None independently associated  
**Related findings:** FND-14965, FND-14966, FND-14967

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14972"></a>
## FND-14972: Native message: chesscom.explanation_engine.v1.ReportCard

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ReportCard",
  "field": [
    {
      "name": "report_card_by_color",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.PlayerReportCard"
    },
    {
      "name": "speech",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1028** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_report_card.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9307a252f124e8645a65c22a69f9fe3aef46d01ad127da0070fe1fc14e15c3ff.bin)

**Source references:** SRC-1028, SRC-1676  
**URL references:** None independently associated  
**Related findings:** FND-14965, FND-14966, FND-14967

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14973"></a>
## FND-14973: chesscom.explanation_engine.v1.ReportCard.report_card_by_color = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ReportCard",
  "name": "report_card_by_color",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.PlayerReportCard",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1028",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1028** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_report_card.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9307a252f124e8645a65c22a69f9fe3aef46d01ad127da0070fe1fc14e15c3ff.bin)

**Source references:** SRC-1028, SRC-1676  
**URL references:** None independently associated  
**Related findings:** FND-14965, FND-14966, FND-14967

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14974"></a>
## FND-14974: chesscom.explanation_engine.v1.ReportCard.speech = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.ReportCard",
  "name": "speech",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1028",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1028** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_report_card.proto.bin` — [preserved redacted evidence](../evidence/descriptors/9307a252f124e8645a65c22a69f9fe3aef46d01ad127da0070fe1fc14e15c3ff.bin)

**Source references:** SRC-1028, SRC-1676  
**URL references:** None independently associated  
**Related findings:** FND-14965, FND-14966, FND-14967

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14975"></a>
## FND-14975: Native message: chesscom.explanation_engine.v1.SearchParameters

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SearchParameters",
  "field": [
    {
      "name": "depth_limit",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "nodes_limit",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "time_limit_ms",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "num_lines",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "multi_line_strategy",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.MultiLineStrategy",
      "oneof_index": 4,
      "proto3_optional": true
    },
    {
      "name": "num_threads",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 5,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_depth_limit"
    },
    {
      "name": "_nodes_limit"
    },
    {
      "name": "_time_limit_ms"
    },
    {
      "name": "_num_lines"
    },
    {
      "name": "_multi_line_strategy"
    },
    {
      "name": "_num_threads"
    }
  ]
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14976"></a>
## FND-14976: chesscom.explanation_engine.v1.SearchParameters.depth_limit = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SearchParameters",
  "name": "depth_limit",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_depth_limit",
  "proto3_optional": true,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14977"></a>
## FND-14977: chesscom.explanation_engine.v1.SearchParameters.nodes_limit = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SearchParameters",
  "name": "nodes_limit",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_nodes_limit",
  "proto3_optional": true,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14978"></a>
## FND-14978: chesscom.explanation_engine.v1.SearchParameters.time_limit_ms = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SearchParameters",
  "name": "time_limit_ms",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_time_limit_ms",
  "proto3_optional": true,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14979"></a>
## FND-14979: chesscom.explanation_engine.v1.SearchParameters.num_lines = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SearchParameters",
  "name": "num_lines",
  "number": 4,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_num_lines",
  "proto3_optional": true,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14980"></a>
## FND-14980: chesscom.explanation_engine.v1.SearchParameters.multi_line_strategy = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SearchParameters",
  "name": "multi_line_strategy",
  "number": 5,
  "type": ".chesscom.explanation_engine.v1.MultiLineStrategy",
  "label": "LABEL_OPTIONAL",
  "oneof": "_multi_line_strategy",
  "proto3_optional": true,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14981"></a>
## FND-14981: chesscom.explanation_engine.v1.SearchParameters.num_threads = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SearchParameters",
  "name": "num_threads",
  "number": 6,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_num_threads",
  "proto3_optional": true,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14982"></a>
## FND-14982: Native message: chesscom.explanation_engine.v1.GameReviewSearchSettings

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameReviewSearchSettings",
  "field": [
    {
      "name": "strength",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.engine.v1.Strength"
    }
  ]
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14983"></a>
## FND-14983: chesscom.explanation_engine.v1.GameReviewSearchSettings.strength = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.GameReviewSearchSettings",
  "name": "strength",
  "number": 1,
  "type": ".chesscom.engine.v1.Strength",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14984"></a>
## FND-14984: chesscom.explanation_engine.v1.SearchPreset.SEARCH_PRESET_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.SearchPreset",
  "name": "SEARCH_PRESET_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14985"></a>
## FND-14985: chesscom.explanation_engine.v1.SearchPreset.SEARCH_PRESET_PLAY_BOT_STANDARD = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.SearchPreset",
  "name": "SEARCH_PRESET_PLAY_BOT_STANDARD",
  "number": 1,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14986"></a>
## FND-14986: chesscom.explanation_engine.v1.SearchPreset.SEARCH_PRESET_PLAY_BOT_FAST = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.SearchPreset",
  "name": "SEARCH_PRESET_PLAY_BOT_FAST",
  "number": 2,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14987"></a>
## FND-14987: chesscom.explanation_engine.v1.SearchPreset.SEARCH_PRESET_GAME_REVIEW_FAST = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.SearchPreset",
  "name": "SEARCH_PRESET_GAME_REVIEW_FAST",
  "number": 3,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14988"></a>
## FND-14988: chesscom.explanation_engine.v1.SearchPreset.SEARCH_PRESET_GAME_REVIEW_STANDARD = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.SearchPreset",
  "name": "SEARCH_PRESET_GAME_REVIEW_STANDARD",
  "number": 4,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14989"></a>
## FND-14989: chesscom.explanation_engine.v1.SearchPreset.SEARCH_PRESET_GAME_REVIEW_DEEP = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.SearchPreset",
  "name": "SEARCH_PRESET_GAME_REVIEW_DEEP",
  "number": 5,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14990"></a>
## FND-14990: chesscom.explanation_engine.v1.SearchPreset.SEARCH_PRESET_GAME_REVIEW_MAXIMUM = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.SearchPreset",
  "name": "SEARCH_PRESET_GAME_REVIEW_MAXIMUM",
  "number": 6,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14991"></a>
## FND-14991: chesscom.explanation_engine.v1.MultiLineStrategy.MULTI_LINE_STRATEGY_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MultiLineStrategy",
  "name": "MULTI_LINE_STRATEGY_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14992"></a>
## FND-14992: chesscom.explanation_engine.v1.MultiLineStrategy.MULTI_LINE_STRATEGY_UCI = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MultiLineStrategy",
  "name": "MULTI_LINE_STRATEGY_UCI",
  "number": 1,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14993"></a>
## FND-14993: chesscom.explanation_engine.v1.MultiLineStrategy.MULTI_LINE_STRATEGY_MULTISEARCH = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.MultiLineStrategy",
  "name": "MULTI_LINE_STRATEGY_MULTISEARCH",
  "number": 2,
  "source_id": "SRC-1029",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1029** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_search.proto.bin` — [preserved redacted evidence](../evidence/descriptors/08bb555d02ec45fe6c62a1e39182e0974f8471bcc4bf4118bd91a8092586efbc.bin)

**Source references:** SRC-1029, SRC-1901  
**URL references:** None independently associated  
**Related findings:** FND-14975, FND-14976, FND-14977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14994"></a>
## FND-14994: Native message: chesscom.explanation_engine.v1.SimpleCharmMovePrediction

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SimpleCharmMovePrediction",
  "field": [
    {
      "name": "uci_move",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "probability",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_FLOAT"
    }
  ]
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14995, FND-14996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14995"></a>
## FND-14995: chesscom.explanation_engine.v1.SimpleCharmMovePrediction.uci_move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleCharmMovePrediction",
  "name": "uci_move",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1030",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14994, FND-14996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14996"></a>
## FND-14996: chesscom.explanation_engine.v1.SimpleCharmMovePrediction.probability = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleCharmMovePrediction",
  "name": "probability",
  "number": 2,
  "type": "TYPE_FLOAT",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1030",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14994, FND-14995

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14997"></a>
## FND-14997: Native message: chesscom.explanation_engine.v1.SimpleCharmInference

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SimpleCharmInference",
  "field": [
    {
      "name": "model_key",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    },
    {
      "name": "rating",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "moves",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SimpleCharmMovePrediction"
    },
    {
      "name": "expected_points",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_FLOAT",
      "oneof_index": 1,
      "proto3_optional": true
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
    }
  ],
  "oneof_decl": [
    {
      "name": "_rating"
    },
    {
      "name": "_expected_points"
    }
  ]
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14994, FND-14995, FND-14996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14998"></a>
## FND-14998: chesscom.explanation_engine.v1.SimpleCharmInference.model_key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleCharmInference",
  "name": "model_key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1030",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14994, FND-14995, FND-14996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-14999"></a>
## FND-14999: chesscom.explanation_engine.v1.SimpleCharmInference.rating = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleCharmInference",
  "name": "rating",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_rating",
  "proto3_optional": true,
  "source_id": "SRC-1030",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14994, FND-14995, FND-14996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15000"></a>
## FND-15000: chesscom.explanation_engine.v1.SimpleCharmInference.moves = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleCharmInference",
  "name": "moves",
  "number": 3,
  "type": ".chesscom.explanation_engine.v1.SimpleCharmMovePrediction",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1030",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14994, FND-14995, FND-14996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15001"></a>
## FND-15001: chesscom.explanation_engine.v1.SimpleCharmInference.expected_points = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleCharmInference",
  "name": "expected_points",
  "number": 4,
  "type": "TYPE_FLOAT",
  "label": "LABEL_OPTIONAL",
  "oneof": "_expected_points",
  "proto3_optional": true,
  "source_id": "SRC-1030",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14994, FND-14995, FND-14996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15002"></a>
## FND-15002: chesscom.explanation_engine.v1.SimpleCharmInference.rank_probabilities = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleCharmInference",
  "name": "rank_probabilities",
  "number": 5,
  "type": "TYPE_FLOAT",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1030",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14994, FND-14995, FND-14996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15003"></a>
## FND-15003: chesscom.explanation_engine.v1.SimpleCharmInference.strength_probabilities = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleCharmInference",
  "name": "strength_probabilities",
  "number": 6,
  "type": "TYPE_FLOAT",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1030",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14994, FND-14995, FND-14996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15004"></a>
## FND-15004: chesscom.explanation_engine.v1.SimpleCharmInference.time_taken_probabilities = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleCharmInference",
  "name": "time_taken_probabilities",
  "number": 7,
  "type": "TYPE_FLOAT",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1030",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14994, FND-14995, FND-14996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15005"></a>
## FND-15005: chesscom.explanation_engine.v1.SimpleCharmInference.ldw_probabilities = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleCharmInference",
  "name": "ldw_probabilities",
  "number": 8,
  "type": "TYPE_FLOAT",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1030",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14994, FND-14995, FND-14996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15006"></a>
## FND-15006: chesscom.explanation_engine.v1.SimpleCharmInference.strength_rating_sensitive_probabilities = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleCharmInference",
  "name": "strength_rating_sensitive_probabilities",
  "number": 9,
  "type": "TYPE_FLOAT",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1030",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14994, FND-14995, FND-14996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15007"></a>
## FND-15007: Native message: chesscom.explanation_engine.v1.SimpleCharmInferences

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SimpleCharmInferences",
  "field": [
    {
      "name": "inferences",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.explanation_engine.v1.SimpleCharmInference"
    }
  ]
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14994, FND-14995, FND-14996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15008"></a>
## FND-15008: chesscom.explanation_engine.v1.SimpleCharmInferences.inferences = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleCharmInferences",
  "name": "inferences",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.SimpleCharmInference",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1030",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1030** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_charm_inference.proto.bin` — [preserved redacted evidence](../evidence/descriptors/a97e2f464717de8faf5b1e2996ccdcc8d17852859572c92374019a080d285cb6.bin)

**Source references:** SRC-1030, SRC-1749  
**URL references:** None independently associated  
**Related findings:** FND-14994, FND-14995, FND-14996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15009"></a>
## FND-15009: Native message: chesscom.explanation_engine.v1.SimpleThreat

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SimpleThreat",
  "field": [
    {
      "name": "threat_type",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.ThreatType"
    },
    {
      "name": "threatened_move",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    },
    {
      "name": "see_value",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Score"
    },
    {
      "name": "score",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.engine.v1.Score"
    }
  ]
}

### Evidence

- **SRC-1031** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_threat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b1f11ad3940e9a2d689a3e750e7c7430819a439d2a47cbf153f32f4a983819a5.bin)

**Source references:** SRC-1031, SRC-1690  
**URL references:** None independently associated  
**Related findings:** FND-15010, FND-15011

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15010"></a>
## FND-15010: chesscom.explanation_engine.v1.SimpleThreat.threat_type = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleThreat",
  "name": "threat_type",
  "number": 1,
  "type": ".chesscom.explanation_engine.v1.ThreatType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1031",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1031** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_threat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b1f11ad3940e9a2d689a3e750e7c7430819a439d2a47cbf153f32f4a983819a5.bin)

**Source references:** SRC-1031, SRC-1690  
**URL references:** None independently associated  
**Related findings:** FND-15009, FND-15011

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15011"></a>
## FND-15011: chesscom.explanation_engine.v1.SimpleThreat.threatened_move = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleThreat",
  "name": "threatened_move",
  "number": 2,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1031",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1031** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_threat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b1f11ad3940e9a2d689a3e750e7c7430819a439d2a47cbf153f32f4a983819a5.bin)

**Source references:** SRC-1031, SRC-1690  
**URL references:** None independently associated  
**Related findings:** FND-15009, FND-15010

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15012"></a>
## FND-15012: chesscom.explanation_engine.v1.SimpleThreat.see_value = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleThreat",
  "name": "see_value",
  "number": 3,
  "type": ".chesscom.chess.v1.Score",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1031",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1031** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_threat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b1f11ad3940e9a2d689a3e750e7c7430819a439d2a47cbf153f32f4a983819a5.bin)

**Source references:** SRC-1031, SRC-1690  
**URL references:** None independently associated  
**Related findings:** FND-15009, FND-15010, FND-15011

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15013"></a>
## FND-15013: chesscom.explanation_engine.v1.SimpleThreat.score = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SimpleThreat",
  "name": "score",
  "number": 4,
  "type": ".chesscom.engine.v1.Score",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1031",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1031** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_threat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b1f11ad3940e9a2d689a3e750e7c7430819a439d2a47cbf153f32f4a983819a5.bin)

**Source references:** SRC-1031, SRC-1690  
**URL references:** None independently associated  
**Related findings:** FND-15009, FND-15010, FND-15011

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15014"></a>
## FND-15014: chesscom.explanation_engine.v1.ThreatType.THREAT_TYPE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.ThreatType",
  "name": "THREAT_TYPE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1031",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1031** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_threat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b1f11ad3940e9a2d689a3e750e7c7430819a439d2a47cbf153f32f4a983819a5.bin)

**Source references:** SRC-1031, SRC-1690  
**URL references:** None independently associated  
**Related findings:** FND-15009, FND-15010, FND-15011

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15015"></a>
## FND-15015: chesscom.explanation_engine.v1.ThreatType.THREAT_TYPE_CHECK = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.ThreatType",
  "name": "THREAT_TYPE_CHECK",
  "number": 1,
  "source_id": "SRC-1031",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1031** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_threat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b1f11ad3940e9a2d689a3e750e7c7430819a439d2a47cbf153f32f4a983819a5.bin)

**Source references:** SRC-1031, SRC-1690  
**URL references:** None independently associated  
**Related findings:** FND-15009, FND-15010, FND-15011

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15016"></a>
## FND-15016: chesscom.explanation_engine.v1.ThreatType.THREAT_TYPE_CAPTURE = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.ThreatType",
  "name": "THREAT_TYPE_CAPTURE",
  "number": 2,
  "source_id": "SRC-1031",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1031** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_threat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b1f11ad3940e9a2d689a3e750e7c7430819a439d2a47cbf153f32f4a983819a5.bin)

**Source references:** SRC-1031, SRC-1690  
**URL references:** None independently associated  
**Related findings:** FND-15009, FND-15010, FND-15011

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15017"></a>
## FND-15017: chesscom.explanation_engine.v1.ThreatType.THREAT_TYPE_MATE = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.ThreatType",
  "name": "THREAT_TYPE_MATE",
  "number": 3,
  "source_id": "SRC-1031",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1031** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_simple_threat.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b1f11ad3940e9a2d689a3e750e7c7430819a439d2a47cbf153f32f4a983819a5.bin)

**Source references:** SRC-1031, SRC-1690  
**URL references:** None independently associated  
**Related findings:** FND-15009, FND-15010, FND-15011

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15018"></a>
## FND-15018: Native message: chesscom.explanation_engine.v1.SkillsPosition

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SkillsPosition",
  "field": [
    {
      "name": "ply",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "skills",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.explanation_engine.v1.Skill"
    },
    {
      "name": "validation_hash",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15019"></a>
## FND-15019: chesscom.explanation_engine.v1.SkillsPosition.ply = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SkillsPosition",
  "name": "ply",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15020"></a>
## FND-15020: chesscom.explanation_engine.v1.SkillsPosition.skills = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SkillsPosition",
  "name": "skills",
  "number": 2,
  "type": ".chesscom.explanation_engine.v1.Skill",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15021"></a>
## FND-15021: chesscom.explanation_engine.v1.SkillsPosition.validation_hash = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.explanation_engine.v1.SkillsPosition",
  "name": "validation_hash",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15022"></a>
## FND-15022: chesscom.explanation_engine.v1.Skill.SKILL_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15023"></a>
## FND-15023: chesscom.explanation_engine.v1.Skill.SKILL_CAPTURE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_CAPTURE",
  "number": 1,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15024"></a>
## FND-15024: chesscom.explanation_engine.v1.Skill.SKILL_CHECK = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_CHECK",
  "number": 2,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15025"></a>
## FND-15025: chesscom.explanation_engine.v1.Skill.SKILL_CASTLE = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_CASTLE",
  "number": 3,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15026"></a>
## FND-15026: chesscom.explanation_engine.v1.Skill.SKILL_CHECKMATE = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_CHECKMATE",
  "number": 4,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15027"></a>
## FND-15027: chesscom.explanation_engine.v1.Skill.SKILL_FREE_PIECE = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_FREE_PIECE",
  "number": 5,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15028"></a>
## FND-15028: chesscom.explanation_engine.v1.Skill.SKILL_DEFEND_PIECE = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_DEFEND_PIECE",
  "number": 6,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15029"></a>
## FND-15029: chesscom.explanation_engine.v1.Skill.SKILL_RETREAT = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_RETREAT",
  "number": 7,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15030"></a>
## FND-15030: chesscom.explanation_engine.v1.Skill.SKILL_DEVELOPS_PIECE = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_DEVELOPS_PIECE",
  "number": 8,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15031"></a>
## FND-15031: chesscom.explanation_engine.v1.Skill.SKILL_PAWNS_IN_CENTER = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_PAWNS_IN_CENTER",
  "number": 9,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15032"></a>
## FND-15032: chesscom.explanation_engine.v1.Skill.SKILL_STRIKES_AT_CENTER = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_STRIKES_AT_CENTER",
  "number": 10,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15033"></a>
## FND-15033: chesscom.explanation_engine.v1.Skill.SKILL_CONNECT_ROOKS = 11

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_CONNECT_ROOKS",
  "number": 11,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15034"></a>
## FND-15034: chesscom.explanation_engine.v1.Skill.SKILL_COMPLETE_DEVELOPMENT = 12

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_COMPLETE_DEVELOPMENT",
  "number": 12,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15035"></a>
## FND-15035: chesscom.explanation_engine.v1.Skill.SKILL_ONE_BOOK_MOVE = 13

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_ONE_BOOK_MOVE",
  "number": 13,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15036"></a>
## FND-15036: chesscom.explanation_engine.v1.Skill.SKILL_TWO_BOOK_MOVES = 14

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_TWO_BOOK_MOVES",
  "number": 14,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15037"></a>
## FND-15037: chesscom.explanation_engine.v1.Skill.SKILL_THREE_BOOK_MOVES = 15

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_THREE_BOOK_MOVES",
  "number": 15,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15038"></a>
## FND-15038: chesscom.explanation_engine.v1.Skill.SKILL_FOUR_BOOK_MOVES = 16

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_FOUR_BOOK_MOVES",
  "number": 16,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15039"></a>
## FND-15039: chesscom.explanation_engine.v1.Skill.SKILL_FIANCHETTO = 17

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_FIANCHETTO",
  "number": 17,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15040"></a>
## FND-15040: chesscom.explanation_engine.v1.Skill.SKILL_RECAPTURE = 18

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_RECAPTURE",
  "number": 18,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15041"></a>
## FND-15041: chesscom.explanation_engine.v1.Skill.SKILL_WINNING_CAPTURE = 19

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_WINNING_CAPTURE",
  "number": 19,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15042"></a>
## FND-15042: chesscom.explanation_engine.v1.Skill.SKILL_BLOCKS_ATTACK = 20

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_BLOCKS_ATTACK",
  "number": 20,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15043"></a>
## FND-15043: chesscom.explanation_engine.v1.Skill.SKILL_FORK = 21

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_FORK",
  "number": 21,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15044"></a>
## FND-15044: chesscom.explanation_engine.v1.Skill.SKILL_PIN = 22

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_PIN",
  "number": 22,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15045"></a>
## FND-15045: chesscom.explanation_engine.v1.Skill.SKILL_DEFEND_CHECKMATE = 23

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_DEFEND_CHECKMATE",
  "number": 23,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15046"></a>
## FND-15046: chesscom.explanation_engine.v1.Skill.SKILL_ABSOLUTE_PIN = 24

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_ABSOLUTE_PIN",
  "number": 24,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15047"></a>
## FND-15047: chesscom.explanation_engine.v1.Skill.SKILL_DISCOVERED_ATTACK = 25

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_DISCOVERED_ATTACK",
  "number": 25,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15048"></a>
## FND-15048: chesscom.explanation_engine.v1.Skill.SKILL_KNIGHT_FORK = 26

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_KNIGHT_FORK",
  "number": 26,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15049"></a>
## FND-15049: chesscom.explanation_engine.v1.Skill.SKILL_SKEWER = 27

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_SKEWER",
  "number": 27,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15050"></a>
## FND-15050: chesscom.explanation_engine.v1.Skill.SKILL_ATTACKING_PINNED_PIECE = 28

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_ATTACKING_PINNED_PIECE",
  "number": 28,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15051"></a>
## FND-15051: chesscom.explanation_engine.v1.Skill.SKILL_TRAPPED_PIECE = 29

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_TRAPPED_PIECE",
  "number": 29,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15052"></a>
## FND-15052: chesscom.explanation_engine.v1.Skill.SKILL_REMOVES_DEFENDER = 30

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_REMOVES_DEFENDER",
  "number": 30,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15053"></a>
## FND-15053: chesscom.explanation_engine.v1.Skill.SKILL_ROYAL_FORK = 31

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_ROYAL_FORK",
  "number": 31,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15054"></a>
## FND-15054: chesscom.explanation_engine.v1.Skill.SKILL_DISCOVERED_CHECK = 32

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_DISCOVERED_CHECK",
  "number": 32,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15055"></a>
## FND-15055: chesscom.explanation_engine.v1.Skill.SKILL_COUNTER_THREAT = 33

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_COUNTER_THREAT",
  "number": 33,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15056"></a>
## FND-15056: chesscom.explanation_engine.v1.Skill.SKILL_DEFEND_TACTIC = 34

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_DEFEND_TACTIC",
  "number": 34,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15057"></a>
## FND-15057: chesscom.explanation_engine.v1.Skill.SKILL_EXPLOITS_PIN = 35

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_EXPLOITS_PIN",
  "number": 35,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15058"></a>
## FND-15058: chesscom.explanation_engine.v1.Skill.SKILL_DOUBLE_CHECK = 36

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_DOUBLE_CHECK",
  "number": 36,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-15059"></a>
## FND-15059: chesscom.explanation_engine.v1.Skill.SKILL_BRILLIANT_SACRIFICE = 37

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.explanation_engine.v1.Skill",
  "name": "SKILL_BRILLIANT_SACRIFICE",
  "number": 37,
  "source_id": "SRC-1032",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-1032** `research/refinement/wasm-descriptors/chesscom_explanation_engine_v1_skills.proto.bin` — [preserved redacted evidence](../evidence/descriptors/b96a5330269910e9e62baddf06434ec85840f733c6e6280d2e478024d3d4891b.bin)

**Source references:** SRC-1032, SRC-1766  
**URL references:** None independently associated  
**Related findings:** FND-15018, FND-15019, FND-15020

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
