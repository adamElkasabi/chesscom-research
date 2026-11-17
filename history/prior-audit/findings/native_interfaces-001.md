# native_interfaces — findings 1–100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-12660"></a>
## FND-12660: Native message: chesscom.api.v1.SemanticVersion

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SemanticVersion",
  "field": [
    {
      "name": "major",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "minor",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    },
    {
      "name": "patch",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32"
    }
  ]
}

### Evidence

- **SRC-0876** `research/refinement/wasm-descriptors/chesscom_api_v1_semantic_version.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a156b1122113ce57653499d07ad3a14db3e3e83363ae775b18643510fdd3aa4.bin)

**Source references:** SRC-0876, SRC-1886  
**URL references:** None independently associated  
**Related findings:** FND-12661, FND-12662

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12661"></a>
## FND-12661: chesscom.api.v1.SemanticVersion.major = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.api.v1.SemanticVersion",
  "name": "major",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0876",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0876** `research/refinement/wasm-descriptors/chesscom_api_v1_semantic_version.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a156b1122113ce57653499d07ad3a14db3e3e83363ae775b18643510fdd3aa4.bin)

**Source references:** SRC-0876, SRC-1886  
**URL references:** None independently associated  
**Related findings:** FND-12660, FND-12662

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12662"></a>
## FND-12662: chesscom.api.v1.SemanticVersion.minor = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.api.v1.SemanticVersion",
  "name": "minor",
  "number": 2,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0876",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0876** `research/refinement/wasm-descriptors/chesscom_api_v1_semantic_version.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a156b1122113ce57653499d07ad3a14db3e3e83363ae775b18643510fdd3aa4.bin)

**Source references:** SRC-0876, SRC-1886  
**URL references:** None independently associated  
**Related findings:** FND-12660, FND-12661

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12663"></a>
## FND-12663: chesscom.api.v1.SemanticVersion.patch = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.api.v1.SemanticVersion",
  "name": "patch",
  "number": 3,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0876",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0876** `research/refinement/wasm-descriptors/chesscom_api_v1_semantic_version.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a156b1122113ce57653499d07ad3a14db3e3e83363ae775b18643510fdd3aa4.bin)

**Source references:** SRC-0876, SRC-1886  
**URL references:** None independently associated  
**Related findings:** FND-12660, FND-12661, FND-12662

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12664"></a>
## FND-12664: Native message: chesscom.chess.v1.Arrow

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Arrow",
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
    }
  ]
}

### Evidence

- **SRC-0877** `research/refinement/wasm-descriptors/chesscom_chess_v1_arrow.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a4423a81159d3817f86a9796f7438a7501db429f7167ca1a97affc04182a794.bin)

**Source references:** SRC-0877, SRC-1736  
**URL references:** None independently associated  
**Related findings:** FND-12665, FND-12666

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12665"></a>
## FND-12665: chesscom.chess.v1.Arrow.from = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Arrow",
  "name": "from",
  "number": 1,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0877",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0877** `research/refinement/wasm-descriptors/chesscom_chess_v1_arrow.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a4423a81159d3817f86a9796f7438a7501db429f7167ca1a97affc04182a794.bin)

**Source references:** SRC-0877, SRC-1736  
**URL references:** None independently associated  
**Related findings:** FND-12664, FND-12666

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12666"></a>
## FND-12666: chesscom.chess.v1.Arrow.to = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Arrow",
  "name": "to",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0877",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0877** `research/refinement/wasm-descriptors/chesscom_chess_v1_arrow.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a4423a81159d3817f86a9796f7438a7501db429f7167ca1a97affc04182a794.bin)

**Source references:** SRC-0877, SRC-1736  
**URL references:** None independently associated  
**Related findings:** FND-12664, FND-12665

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12667"></a>
## FND-12667: Native message: chesscom.chess.v1.ArrowsAndSquares

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ArrowsAndSquares",
  "field": [
    {
      "name": "arrows",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Arrow"
    },
    {
      "name": "squares",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Square"
    }
  ]
}

### Evidence

- **SRC-0877** `research/refinement/wasm-descriptors/chesscom_chess_v1_arrow.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a4423a81159d3817f86a9796f7438a7501db429f7167ca1a97affc04182a794.bin)

**Source references:** SRC-0877, SRC-1736  
**URL references:** None independently associated  
**Related findings:** FND-12664, FND-12665, FND-12666

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12668"></a>
## FND-12668: chesscom.chess.v1.ArrowsAndSquares.arrows = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.ArrowsAndSquares",
  "name": "arrows",
  "number": 1,
  "type": ".chesscom.chess.v1.Arrow",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0877",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0877** `research/refinement/wasm-descriptors/chesscom_chess_v1_arrow.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a4423a81159d3817f86a9796f7438a7501db429f7167ca1a97affc04182a794.bin)

**Source references:** SRC-0877, SRC-1736  
**URL references:** None independently associated  
**Related findings:** FND-12664, FND-12665, FND-12666

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12669"></a>
## FND-12669: chesscom.chess.v1.ArrowsAndSquares.squares = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.ArrowsAndSquares",
  "name": "squares",
  "number": 2,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0877",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0877** `research/refinement/wasm-descriptors/chesscom_chess_v1_arrow.proto.bin` — [preserved redacted evidence](../evidence/descriptors/7a4423a81159d3817f86a9796f7438a7501db429f7167ca1a97affc04182a794.bin)

**Source references:** SRC-0877, SRC-1736  
**URL references:** None independently associated  
**Related findings:** FND-12664, FND-12665, FND-12666

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12670"></a>
## FND-12670: Native message: chesscom.chess.v1.ArrowMarking

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ArrowMarking",
  "field": [
    {
      "name": "arrow",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Arrow"
    },
    {
      "name": "color",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.MarkingColor"
    }
  ]
}

### Evidence

- **SRC-0878** `research/refinement/wasm-descriptors/chesscom_chess_v1_board_markings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d93f0b7a749fffdc0086488a4a1ede9ef02b14572c457a393f6ab75536577567.bin)

**Source references:** SRC-0878, SRC-1687  
**URL references:** None independently associated  
**Related findings:** FND-12671, FND-12672

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12671"></a>
## FND-12671: chesscom.chess.v1.ArrowMarking.arrow = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.ArrowMarking",
  "name": "arrow",
  "number": 1,
  "type": ".chesscom.chess.v1.Arrow",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0878",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0878** `research/refinement/wasm-descriptors/chesscom_chess_v1_board_markings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d93f0b7a749fffdc0086488a4a1ede9ef02b14572c457a393f6ab75536577567.bin)

**Source references:** SRC-0878, SRC-1687  
**URL references:** None independently associated  
**Related findings:** FND-12670, FND-12672

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12672"></a>
## FND-12672: chesscom.chess.v1.ArrowMarking.color = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.ArrowMarking",
  "name": "color",
  "number": 2,
  "type": ".chesscom.chess.v1.MarkingColor",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0878",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0878** `research/refinement/wasm-descriptors/chesscom_chess_v1_board_markings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d93f0b7a749fffdc0086488a4a1ede9ef02b14572c457a393f6ab75536577567.bin)

**Source references:** SRC-0878, SRC-1687  
**URL references:** None independently associated  
**Related findings:** FND-12670, FND-12671

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12673"></a>
## FND-12673: Native message: chesscom.chess.v1.SquareMarking

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "SquareMarking",
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
      "type_name": ".chesscom.chess.v1.MarkingColor"
    }
  ]
}

### Evidence

- **SRC-0878** `research/refinement/wasm-descriptors/chesscom_chess_v1_board_markings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d93f0b7a749fffdc0086488a4a1ede9ef02b14572c457a393f6ab75536577567.bin)

**Source references:** SRC-0878, SRC-1687  
**URL references:** None independently associated  
**Related findings:** FND-12670, FND-12671, FND-12672

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12674"></a>
## FND-12674: chesscom.chess.v1.SquareMarking.square = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.SquareMarking",
  "name": "square",
  "number": 1,
  "type": ".chesscom.chess.v1.Square",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0878",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0878** `research/refinement/wasm-descriptors/chesscom_chess_v1_board_markings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d93f0b7a749fffdc0086488a4a1ede9ef02b14572c457a393f6ab75536577567.bin)

**Source references:** SRC-0878, SRC-1687  
**URL references:** None independently associated  
**Related findings:** FND-12670, FND-12671, FND-12672

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12675"></a>
## FND-12675: chesscom.chess.v1.SquareMarking.color = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.SquareMarking",
  "name": "color",
  "number": 2,
  "type": ".chesscom.chess.v1.MarkingColor",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0878",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0878** `research/refinement/wasm-descriptors/chesscom_chess_v1_board_markings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d93f0b7a749fffdc0086488a4a1ede9ef02b14572c457a393f6ab75536577567.bin)

**Source references:** SRC-0878, SRC-1687  
**URL references:** None independently associated  
**Related findings:** FND-12670, FND-12671, FND-12672

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12676"></a>
## FND-12676: Native message: chesscom.chess.v1.BoardMarkings

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "BoardMarkings",
  "field": [
    {
      "name": "arrows",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.ArrowMarking"
    },
    {
      "name": "squares",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.SquareMarking"
    }
  ]
}

### Evidence

- **SRC-0878** `research/refinement/wasm-descriptors/chesscom_chess_v1_board_markings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d93f0b7a749fffdc0086488a4a1ede9ef02b14572c457a393f6ab75536577567.bin)

**Source references:** SRC-0878, SRC-1687  
**URL references:** None independently associated  
**Related findings:** FND-12670, FND-12671, FND-12672

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12677"></a>
## FND-12677: chesscom.chess.v1.BoardMarkings.arrows = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.BoardMarkings",
  "name": "arrows",
  "number": 1,
  "type": ".chesscom.chess.v1.ArrowMarking",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0878",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0878** `research/refinement/wasm-descriptors/chesscom_chess_v1_board_markings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d93f0b7a749fffdc0086488a4a1ede9ef02b14572c457a393f6ab75536577567.bin)

**Source references:** SRC-0878, SRC-1687  
**URL references:** None independently associated  
**Related findings:** FND-12670, FND-12671, FND-12672

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12678"></a>
## FND-12678: chesscom.chess.v1.BoardMarkings.squares = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.BoardMarkings",
  "name": "squares",
  "number": 2,
  "type": ".chesscom.chess.v1.SquareMarking",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0878",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0878** `research/refinement/wasm-descriptors/chesscom_chess_v1_board_markings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d93f0b7a749fffdc0086488a4a1ede9ef02b14572c457a393f6ab75536577567.bin)

**Source references:** SRC-0878, SRC-1687  
**URL references:** None independently associated  
**Related findings:** FND-12670, FND-12671, FND-12672

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12679"></a>
## FND-12679: chesscom.chess.v1.MarkingColor.MARKING_COLOR_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.MarkingColor",
  "name": "MARKING_COLOR_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0878",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0878** `research/refinement/wasm-descriptors/chesscom_chess_v1_board_markings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d93f0b7a749fffdc0086488a4a1ede9ef02b14572c457a393f6ab75536577567.bin)

**Source references:** SRC-0878, SRC-1687  
**URL references:** None independently associated  
**Related findings:** FND-12670, FND-12671, FND-12672

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12680"></a>
## FND-12680: chesscom.chess.v1.MarkingColor.MARKING_COLOR_RED = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.MarkingColor",
  "name": "MARKING_COLOR_RED",
  "number": 1,
  "source_id": "SRC-0878",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0878** `research/refinement/wasm-descriptors/chesscom_chess_v1_board_markings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d93f0b7a749fffdc0086488a4a1ede9ef02b14572c457a393f6ab75536577567.bin)

**Source references:** SRC-0878, SRC-1687  
**URL references:** None independently associated  
**Related findings:** FND-12670, FND-12671, FND-12672

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12681"></a>
## FND-12681: chesscom.chess.v1.MarkingColor.MARKING_COLOR_BLUE = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.MarkingColor",
  "name": "MARKING_COLOR_BLUE",
  "number": 2,
  "source_id": "SRC-0878",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0878** `research/refinement/wasm-descriptors/chesscom_chess_v1_board_markings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d93f0b7a749fffdc0086488a4a1ede9ef02b14572c457a393f6ab75536577567.bin)

**Source references:** SRC-0878, SRC-1687  
**URL references:** None independently associated  
**Related findings:** FND-12670, FND-12671, FND-12672

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12682"></a>
## FND-12682: chesscom.chess.v1.MarkingColor.MARKING_COLOR_GREEN = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.MarkingColor",
  "name": "MARKING_COLOR_GREEN",
  "number": 3,
  "source_id": "SRC-0878",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0878** `research/refinement/wasm-descriptors/chesscom_chess_v1_board_markings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d93f0b7a749fffdc0086488a4a1ede9ef02b14572c457a393f6ab75536577567.bin)

**Source references:** SRC-0878, SRC-1687  
**URL references:** None independently associated  
**Related findings:** FND-12670, FND-12671, FND-12672

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12683"></a>
## FND-12683: chesscom.chess.v1.MarkingColor.MARKING_COLOR_ORANGE = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.MarkingColor",
  "name": "MARKING_COLOR_ORANGE",
  "number": 4,
  "source_id": "SRC-0878",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0878** `research/refinement/wasm-descriptors/chesscom_chess_v1_board_markings.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d93f0b7a749fffdc0086488a4a1ede9ef02b14572c457a393f6ab75536577567.bin)

**Source references:** SRC-0878, SRC-1687  
**URL references:** None independently associated  
**Related findings:** FND-12670, FND-12671, FND-12672

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12684"></a>
## FND-12684: chesscom.chess.v1.ChesscomGameSource.CHESSCOM_GAME_SOURCE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ChesscomGameSource",
  "name": "CHESSCOM_GAME_SOURCE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0879",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0879** `research/refinement/wasm-descriptors/chesscom_chess_v1_chesscom_game_source.proto.bin` — [preserved redacted evidence](../evidence/descriptors/aca0a3604c6b1828749ded468fa85f2e03305fd852e5d52f8bb2c5bb856245f1.bin)

**Source references:** SRC-0879, SRC-1887  
**URL references:** None independently associated  
**Related findings:** FND-12685, FND-12686

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12685"></a>
## FND-12685: chesscom.chess.v1.ChesscomGameSource.CHESSCOM_GAME_SOURCE_DAILY = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ChesscomGameSource",
  "name": "CHESSCOM_GAME_SOURCE_DAILY",
  "number": 1,
  "source_id": "SRC-0879",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0879** `research/refinement/wasm-descriptors/chesscom_chess_v1_chesscom_game_source.proto.bin` — [preserved redacted evidence](../evidence/descriptors/aca0a3604c6b1828749ded468fa85f2e03305fd852e5d52f8bb2c5bb856245f1.bin)

**Source references:** SRC-0879, SRC-1887  
**URL references:** None independently associated  
**Related findings:** FND-12684, FND-12686

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12686"></a>
## FND-12686: chesscom.chess.v1.ChesscomGameSource.CHESSCOM_GAME_SOURCE_LIVE = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ChesscomGameSource",
  "name": "CHESSCOM_GAME_SOURCE_LIVE",
  "number": 2,
  "source_id": "SRC-0879",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0879** `research/refinement/wasm-descriptors/chesscom_chess_v1_chesscom_game_source.proto.bin` — [preserved redacted evidence](../evidence/descriptors/aca0a3604c6b1828749ded468fa85f2e03305fd852e5d52f8bb2c5bb856245f1.bin)

**Source references:** SRC-0879, SRC-1887  
**URL references:** None independently associated  
**Related findings:** FND-12684, FND-12685

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12687"></a>
## FND-12687: chesscom.chess.v1.ChesscomGameSource.CHESSCOM_GAME_SOURCE_MASTER = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ChesscomGameSource",
  "name": "CHESSCOM_GAME_SOURCE_MASTER",
  "number": 3,
  "source_id": "SRC-0879",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0879** `research/refinement/wasm-descriptors/chesscom_chess_v1_chesscom_game_source.proto.bin` — [preserved redacted evidence](../evidence/descriptors/aca0a3604c6b1828749ded468fa85f2e03305fd852e5d52f8bb2c5bb856245f1.bin)

**Source references:** SRC-0879, SRC-1887  
**URL references:** None independently associated  
**Related findings:** FND-12684, FND-12685, FND-12686

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12688"></a>
## FND-12688: chesscom.chess.v1.ChesscomGameSource.CHESSCOM_GAME_SOURCE_PGN = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ChesscomGameSource",
  "name": "CHESSCOM_GAME_SOURCE_PGN",
  "number": 4,
  "source_id": "SRC-0879",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0879** `research/refinement/wasm-descriptors/chesscom_chess_v1_chesscom_game_source.proto.bin` — [preserved redacted evidence](../evidence/descriptors/aca0a3604c6b1828749ded468fa85f2e03305fd852e5d52f8bb2c5bb856245f1.bin)

**Source references:** SRC-0879, SRC-1887  
**URL references:** None independently associated  
**Related findings:** FND-12684, FND-12685, FND-12686

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12689"></a>
## FND-12689: chesscom.chess.v1.ChesscomGameSource.CHESSCOM_GAME_SOURCE_VS_COMPUTER = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ChesscomGameSource",
  "name": "CHESSCOM_GAME_SOURCE_VS_COMPUTER",
  "number": 5,
  "source_id": "SRC-0879",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0879** `research/refinement/wasm-descriptors/chesscom_chess_v1_chesscom_game_source.proto.bin` — [preserved redacted evidence](../evidence/descriptors/aca0a3604c6b1828749ded468fa85f2e03305fd852e5d52f8bb2c5bb856245f1.bin)

**Source references:** SRC-0879, SRC-1887  
**URL references:** None independently associated  
**Related findings:** FND-12684, FND-12685, FND-12686

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12690"></a>
## FND-12690: chesscom.chess.v1.ChesscomGameSource.CHESSCOM_GAME_SOURCE_VS_COACH = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.ChesscomGameSource",
  "name": "CHESSCOM_GAME_SOURCE_VS_COACH",
  "number": 6,
  "source_id": "SRC-0879",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0879** `research/refinement/wasm-descriptors/chesscom_chess_v1_chesscom_game_source.proto.bin` — [preserved redacted evidence](../evidence/descriptors/aca0a3604c6b1828749ded468fa85f2e03305fd852e5d52f8bb2c5bb856245f1.bin)

**Source references:** SRC-0879, SRC-1887  
**URL references:** None independently associated  
**Related findings:** FND-12684, FND-12685, FND-12686

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12691"></a>
## FND-12691: chesscom.chess.v1.Color.COLOR_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Color",
  "name": "COLOR_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0880",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0880** `research/refinement/wasm-descriptors/chesscom_chess_v1_color.proto.bin` — [preserved redacted evidence](../evidence/descriptors/859a38dd7c10485b65d3c2f5704475561bbc5074867b347955f719607f00bf5c.bin)

**Source references:** SRC-0880, SRC-1791  
**URL references:** None independently associated  
**Related findings:** FND-12692, FND-12693

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12692"></a>
## FND-12692: chesscom.chess.v1.Color.COLOR_WHITE = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Color",
  "name": "COLOR_WHITE",
  "number": 1,
  "source_id": "SRC-0880",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0880** `research/refinement/wasm-descriptors/chesscom_chess_v1_color.proto.bin` — [preserved redacted evidence](../evidence/descriptors/859a38dd7c10485b65d3c2f5704475561bbc5074867b347955f719607f00bf5c.bin)

**Source references:** SRC-0880, SRC-1791  
**URL references:** None independently associated  
**Related findings:** FND-12691, FND-12693

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12693"></a>
## FND-12693: chesscom.chess.v1.Color.COLOR_BLACK = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.Color",
  "name": "COLOR_BLACK",
  "number": 2,
  "source_id": "SRC-0880",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0880** `research/refinement/wasm-descriptors/chesscom_chess_v1_color.proto.bin` — [preserved redacted evidence](../evidence/descriptors/859a38dd7c10485b65d3c2f5704475561bbc5074867b347955f719607f00bf5c.bin)

**Source references:** SRC-0880, SRC-1791  
**URL references:** None independently associated  
**Related findings:** FND-12691, FND-12692

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12694"></a>
## FND-12694: Native message: chesscom.chess.v1.EcoFamily

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "EcoFamily",
  "field": [
    {
      "name": "eco_family_id",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32"
    },
    {
      "name": "name",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING"
    }
  ]
}

### Evidence

- **SRC-0881** `research/refinement/wasm-descriptors/chesscom_chess_v1_eco.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fc92ae107f0d053d5e9ff720d76eb13a8cb6274fb57ae13c38c95960b904c9d.bin)

**Source references:** SRC-0881, SRC-1730  
**URL references:** None independently associated  
**Related findings:** FND-12695, FND-12696

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12695"></a>
## FND-12695: chesscom.chess.v1.EcoFamily.eco_family_id = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.EcoFamily",
  "name": "eco_family_id",
  "number": 1,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0881",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0881** `research/refinement/wasm-descriptors/chesscom_chess_v1_eco.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fc92ae107f0d053d5e9ff720d76eb13a8cb6274fb57ae13c38c95960b904c9d.bin)

**Source references:** SRC-0881, SRC-1730  
**URL references:** None independently associated  
**Related findings:** FND-12694, FND-12696

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12696"></a>
## FND-12696: chesscom.chess.v1.EcoFamily.name = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.EcoFamily",
  "name": "name",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0881",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0881** `research/refinement/wasm-descriptors/chesscom_chess_v1_eco.proto.bin` — [preserved redacted evidence](../evidence/descriptors/6fc92ae107f0d053d5e9ff720d76eb13a8cb6274fb57ae13c38c95960b904c9d.bin)

**Source references:** SRC-0881, SRC-1730  
**URL references:** None independently associated  
**Related findings:** FND-12694, FND-12695

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12697"></a>
## FND-12697: chesscom.chess.v1.File.FILE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.File",
  "name": "FILE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0882",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0882** `research/refinement/wasm-descriptors/chesscom_chess_v1_file.proto.bin` — [preserved redacted evidence](../evidence/descriptors/85b56584fa9036913a6fdbafcafd1eb3afda63bd15cc4b675c0cd97689f2e38c.bin)

**Source references:** SRC-0882, SRC-1652  
**URL references:** None independently associated  
**Related findings:** FND-12698, FND-12699

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12698"></a>
## FND-12698: chesscom.chess.v1.File.FILE_A = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.File",
  "name": "FILE_A",
  "number": 1,
  "source_id": "SRC-0882",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0882** `research/refinement/wasm-descriptors/chesscom_chess_v1_file.proto.bin` — [preserved redacted evidence](../evidence/descriptors/85b56584fa9036913a6fdbafcafd1eb3afda63bd15cc4b675c0cd97689f2e38c.bin)

**Source references:** SRC-0882, SRC-1652  
**URL references:** None independently associated  
**Related findings:** FND-12697, FND-12699

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12699"></a>
## FND-12699: chesscom.chess.v1.File.FILE_B = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.File",
  "name": "FILE_B",
  "number": 2,
  "source_id": "SRC-0882",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0882** `research/refinement/wasm-descriptors/chesscom_chess_v1_file.proto.bin` — [preserved redacted evidence](../evidence/descriptors/85b56584fa9036913a6fdbafcafd1eb3afda63bd15cc4b675c0cd97689f2e38c.bin)

**Source references:** SRC-0882, SRC-1652  
**URL references:** None independently associated  
**Related findings:** FND-12697, FND-12698

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12700"></a>
## FND-12700: chesscom.chess.v1.File.FILE_C = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.File",
  "name": "FILE_C",
  "number": 3,
  "source_id": "SRC-0882",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0882** `research/refinement/wasm-descriptors/chesscom_chess_v1_file.proto.bin` — [preserved redacted evidence](../evidence/descriptors/85b56584fa9036913a6fdbafcafd1eb3afda63bd15cc4b675c0cd97689f2e38c.bin)

**Source references:** SRC-0882, SRC-1652  
**URL references:** None independently associated  
**Related findings:** FND-12697, FND-12698, FND-12699

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12701"></a>
## FND-12701: chesscom.chess.v1.File.FILE_D = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.File",
  "name": "FILE_D",
  "number": 4,
  "source_id": "SRC-0882",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0882** `research/refinement/wasm-descriptors/chesscom_chess_v1_file.proto.bin` — [preserved redacted evidence](../evidence/descriptors/85b56584fa9036913a6fdbafcafd1eb3afda63bd15cc4b675c0cd97689f2e38c.bin)

**Source references:** SRC-0882, SRC-1652  
**URL references:** None independently associated  
**Related findings:** FND-12697, FND-12698, FND-12699

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12702"></a>
## FND-12702: chesscom.chess.v1.File.FILE_E = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.File",
  "name": "FILE_E",
  "number": 5,
  "source_id": "SRC-0882",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0882** `research/refinement/wasm-descriptors/chesscom_chess_v1_file.proto.bin` — [preserved redacted evidence](../evidence/descriptors/85b56584fa9036913a6fdbafcafd1eb3afda63bd15cc4b675c0cd97689f2e38c.bin)

**Source references:** SRC-0882, SRC-1652  
**URL references:** None independently associated  
**Related findings:** FND-12697, FND-12698, FND-12699

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12703"></a>
## FND-12703: chesscom.chess.v1.File.FILE_F = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.File",
  "name": "FILE_F",
  "number": 6,
  "source_id": "SRC-0882",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0882** `research/refinement/wasm-descriptors/chesscom_chess_v1_file.proto.bin` — [preserved redacted evidence](../evidence/descriptors/85b56584fa9036913a6fdbafcafd1eb3afda63bd15cc4b675c0cd97689f2e38c.bin)

**Source references:** SRC-0882, SRC-1652  
**URL references:** None independently associated  
**Related findings:** FND-12697, FND-12698, FND-12699

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12704"></a>
## FND-12704: chesscom.chess.v1.File.FILE_G = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.File",
  "name": "FILE_G",
  "number": 7,
  "source_id": "SRC-0882",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0882** `research/refinement/wasm-descriptors/chesscom_chess_v1_file.proto.bin` — [preserved redacted evidence](../evidence/descriptors/85b56584fa9036913a6fdbafcafd1eb3afda63bd15cc4b675c0cd97689f2e38c.bin)

**Source references:** SRC-0882, SRC-1652  
**URL references:** None independently associated  
**Related findings:** FND-12697, FND-12698, FND-12699

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12705"></a>
## FND-12705: chesscom.chess.v1.File.FILE_H = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.File",
  "name": "FILE_H",
  "number": 8,
  "source_id": "SRC-0882",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0882** `research/refinement/wasm-descriptors/chesscom_chess_v1_file.proto.bin` — [preserved redacted evidence](../evidence/descriptors/85b56584fa9036913a6fdbafcafd1eb3afda63bd15cc4b675c0cd97689f2e38c.bin)

**Source references:** SRC-0882, SRC-1652  
**URL references:** None independently associated  
**Related findings:** FND-12697, FND-12698, FND-12699

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12706"></a>
## FND-12706: Native message: chesscom.chess.v1.GameResult

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameResult",
  "field": [
    {
      "name": "result",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Result"
    },
    {
      "name": "result_type",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.ResultType"
    }
  ]
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12707"></a>
## FND-12707: chesscom.chess.v1.GameResult.result = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameResult",
  "name": "result",
  "number": 1,
  "type": ".chesscom.chess.v1.Result",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12708"></a>
## FND-12708: chesscom.chess.v1.GameResult.result_type = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameResult",
  "name": "result_type",
  "number": 2,
  "type": ".chesscom.chess.v1.ResultType",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12709"></a>
## FND-12709: Native message: chesscom.chess.v1.Game

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Game",
  "field": [
    {
      "name": "starting_position",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Position"
    },
    {
      "name": "moves",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.GameMove"
    },
    {
      "name": "metadata",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.GameMetadata"
    }
  ]
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12710"></a>
## FND-12710: chesscom.chess.v1.Game.starting_position = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Game",
  "name": "starting_position",
  "number": 1,
  "type": ".chesscom.chess.v1.Position",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12711"></a>
## FND-12711: chesscom.chess.v1.Game.moves = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Game",
  "name": "moves",
  "number": 2,
  "type": ".chesscom.chess.v1.GameMove",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12712"></a>
## FND-12712: chesscom.chess.v1.Game.metadata = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Game",
  "name": "metadata",
  "number": 3,
  "type": ".chesscom.chess.v1.GameMetadata",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12713"></a>
## FND-12713: Native message: chesscom.chess.v1.GameMove

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameMove",
  "field": [
    {
      "name": "move",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Move"
    },
    {
      "name": "metadata",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.GameMoveMetadata",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "variations",
      "number": 3,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.MoveVariation"
    }
  ],
  "oneof_decl": [
    {
      "name": "_metadata"
    }
  ]
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12714"></a>
## FND-12714: chesscom.chess.v1.GameMove.move = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMove",
  "name": "move",
  "number": 1,
  "type": ".chesscom.chess.v1.Move",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12715"></a>
## FND-12715: chesscom.chess.v1.GameMove.metadata = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMove",
  "name": "metadata",
  "number": 2,
  "type": ".chesscom.chess.v1.GameMoveMetadata",
  "label": "LABEL_OPTIONAL",
  "oneof": "_metadata",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12716"></a>
## FND-12716: chesscom.chess.v1.GameMove.variations = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMove",
  "name": "variations",
  "number": 3,
  "type": ".chesscom.chess.v1.MoveVariation",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12717"></a>
## FND-12717: Native message: chesscom.chess.v1.GameMoveMetadata

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameMoveMetadata",
  "field": [
    {
      "name": "score",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Score",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "time_remaining_ms",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_UINT32",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "comment_before",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "comments_after",
      "number": 4,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING"
    },
    {
      "name": "nags",
      "number": 5,
      "label": "LABEL_REPEATED",
      "type": "TYPE_UINT32"
    }
  ],
  "oneof_decl": [
    {
      "name": "_score"
    },
    {
      "name": "_time_remaining_ms"
    },
    {
      "name": "_comment_before"
    }
  ]
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12718"></a>
## FND-12718: chesscom.chess.v1.GameMoveMetadata.score = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMoveMetadata",
  "name": "score",
  "number": 1,
  "type": ".chesscom.chess.v1.Score",
  "label": "LABEL_OPTIONAL",
  "oneof": "_score",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12719"></a>
## FND-12719: chesscom.chess.v1.GameMoveMetadata.time_remaining_ms = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMoveMetadata",
  "name": "time_remaining_ms",
  "number": 2,
  "type": "TYPE_UINT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_time_remaining_ms",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12720"></a>
## FND-12720: chesscom.chess.v1.GameMoveMetadata.comment_before = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMoveMetadata",
  "name": "comment_before",
  "number": 3,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_comment_before",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12721"></a>
## FND-12721: chesscom.chess.v1.GameMoveMetadata.comments_after = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMoveMetadata",
  "name": "comments_after",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12722"></a>
## FND-12722: chesscom.chess.v1.GameMoveMetadata.nags = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMoveMetadata",
  "name": "nags",
  "number": 5,
  "type": "TYPE_UINT32",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12723"></a>
## FND-12723: Native message: chesscom.chess.v1.MoveVariation

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "MoveVariation",
  "field": [
    {
      "name": "moves",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.GameMove"
    }
  ]
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12724"></a>
## FND-12724: chesscom.chess.v1.MoveVariation.moves = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.MoveVariation",
  "name": "moves",
  "number": 1,
  "type": ".chesscom.chess.v1.GameMove",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12725"></a>
## FND-12725: Native message: chesscom.chess.v1.Rules

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Rules",
  "field": [
    {
      "name": "is_chess960",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_is_chess960"
    }
  ]
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12726"></a>
## FND-12726: chesscom.chess.v1.Rules.is_chess960 = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Rules",
  "name": "is_chess960",
  "number": 1,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_is_chess960",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12727"></a>
## FND-12727: Native message: chesscom.chess.v1.GameMetadata

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "GameMetadata",
  "field": [
    {
      "name": "players",
      "number": 1,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.PlayerMetadata"
    },
    {
      "name": "time_control",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.TimeControl",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "timestamps",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Timestamps",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "result",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.GameResult",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "rules",
      "number": 5,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Rules",
      "oneof_index": 3,
      "proto3_optional": true
    },
    {
      "name": "chesscom_metadata",
      "number": 6,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.ChesscomGameMetadata",
      "oneof_index": 4,
      "proto3_optional": true
    },
    {
      "name": "pgn_headers",
      "number": 7,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.GameMetadata.PgnHeadersEntry"
    },
    {
      "name": "link",
      "number": 8,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 5,
      "proto3_optional": true
    },
    {
      "name": "time_class",
      "number": 9,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.TimeClass",
      "oneof_index": 6,
      "proto3_optional": true
    },
    {
      "name": "is_rated",
      "number": 10,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "oneof_index": 7,
      "proto3_optional": true
    }
  ],
  "nested_type": [
    {
      "name": "PgnHeadersEntry",
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
      "name": "_time_control"
    },
    {
      "name": "_timestamps"
    },
    {
      "name": "_result"
    },
    {
      "name": "_rules"
    },
    {
      "name": "_chesscom_metadata"
    },
    {
      "name": "_link"
    },
    {
      "name": "_time_class"
    },
    {
      "name": "_is_rated"
    }
  ]
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12728"></a>
## FND-12728: chesscom.chess.v1.GameMetadata.players = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMetadata",
  "name": "players",
  "number": 1,
  "type": ".chesscom.chess.v1.PlayerMetadata",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12729"></a>
## FND-12729: chesscom.chess.v1.GameMetadata.time_control = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMetadata",
  "name": "time_control",
  "number": 2,
  "type": ".chesscom.chess.v1.TimeControl",
  "label": "LABEL_OPTIONAL",
  "oneof": "_time_control",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12730"></a>
## FND-12730: chesscom.chess.v1.GameMetadata.timestamps = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMetadata",
  "name": "timestamps",
  "number": 3,
  "type": ".chesscom.chess.v1.Timestamps",
  "label": "LABEL_OPTIONAL",
  "oneof": "_timestamps",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12731"></a>
## FND-12731: chesscom.chess.v1.GameMetadata.result = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMetadata",
  "name": "result",
  "number": 4,
  "type": ".chesscom.chess.v1.GameResult",
  "label": "LABEL_OPTIONAL",
  "oneof": "_result",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12732"></a>
## FND-12732: chesscom.chess.v1.GameMetadata.rules = 5

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMetadata",
  "name": "rules",
  "number": 5,
  "type": ".chesscom.chess.v1.Rules",
  "label": "LABEL_OPTIONAL",
  "oneof": "_rules",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12733"></a>
## FND-12733: chesscom.chess.v1.GameMetadata.chesscom_metadata = 6

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMetadata",
  "name": "chesscom_metadata",
  "number": 6,
  "type": ".chesscom.chess.v1.ChesscomGameMetadata",
  "label": "LABEL_OPTIONAL",
  "oneof": "_chesscom_metadata",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12734"></a>
## FND-12734: chesscom.chess.v1.GameMetadata.pgn_headers = 7

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMetadata",
  "name": "pgn_headers",
  "number": 7,
  "type": ".chesscom.chess.v1.GameMetadata.PgnHeadersEntry",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12735"></a>
## FND-12735: chesscom.chess.v1.GameMetadata.link = 8

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMetadata",
  "name": "link",
  "number": 8,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_link",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12736"></a>
## FND-12736: chesscom.chess.v1.GameMetadata.time_class = 9

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMetadata",
  "name": "time_class",
  "number": 9,
  "type": ".chesscom.chess.v1.TimeClass",
  "label": "LABEL_OPTIONAL",
  "oneof": "_time_class",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12737"></a>
## FND-12737: chesscom.chess.v1.GameMetadata.is_rated = 10

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMetadata",
  "name": "is_rated",
  "number": 10,
  "type": "TYPE_BOOL",
  "label": "LABEL_OPTIONAL",
  "oneof": "_is_rated",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12738"></a>
## FND-12738: Native message: chesscom.chess.v1.GameMetadata.PgnHeadersEntry

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PgnHeadersEntry",
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

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12739"></a>
## FND-12739: chesscom.chess.v1.GameMetadata.PgnHeadersEntry.key = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMetadata.PgnHeadersEntry",
  "name": "key",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12740"></a>
## FND-12740: chesscom.chess.v1.GameMetadata.PgnHeadersEntry.value = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.GameMetadata.PgnHeadersEntry",
  "name": "value",
  "number": 2,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12741"></a>
## FND-12741: Native message: chesscom.chess.v1.Timestamps

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Timestamps",
  "field": [
    {
      "name": "started_at",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT64",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "finished_at",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT64",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_started_at"
    },
    {
      "name": "_finished_at"
    }
  ]
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12742"></a>
## FND-12742: chesscom.chess.v1.Timestamps.started_at = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Timestamps",
  "name": "started_at",
  "number": 1,
  "type": "TYPE_INT64",
  "label": "LABEL_OPTIONAL",
  "oneof": "_started_at",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12743"></a>
## FND-12743: chesscom.chess.v1.Timestamps.finished_at = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Timestamps",
  "name": "finished_at",
  "number": 2,
  "type": "TYPE_INT64",
  "label": "LABEL_OPTIONAL",
  "oneof": "_finished_at",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12744"></a>
## FND-12744: Native message: chesscom.chess.v1.ChesscomGameMetadata

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ChesscomGameMetadata",
  "field": [
    {
      "name": "game_id",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "legacy_game_id",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT64",
      "oneof_index": 1,
      "proto3_optional": true
    },
    {
      "name": "eco_id",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT64",
      "oneof_index": 2,
      "proto3_optional": true
    },
    {
      "name": "game_source",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.ChesscomGameSource",
      "oneof_index": 3,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_game_id"
    },
    {
      "name": "_legacy_game_id"
    },
    {
      "name": "_eco_id"
    },
    {
      "name": "_game_source"
    }
  ]
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12745"></a>
## FND-12745: chesscom.chess.v1.ChesscomGameMetadata.game_id = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.ChesscomGameMetadata",
  "name": "game_id",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_game_id",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12746"></a>
## FND-12746: chesscom.chess.v1.ChesscomGameMetadata.legacy_game_id = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.ChesscomGameMetadata",
  "name": "legacy_game_id",
  "number": 2,
  "type": "TYPE_INT64",
  "label": "LABEL_OPTIONAL",
  "oneof": "_legacy_game_id",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12747"></a>
## FND-12747: chesscom.chess.v1.ChesscomGameMetadata.eco_id = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.ChesscomGameMetadata",
  "name": "eco_id",
  "number": 3,
  "type": "TYPE_INT64",
  "label": "LABEL_OPTIONAL",
  "oneof": "_eco_id",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12748"></a>
## FND-12748: chesscom.chess.v1.ChesscomGameMetadata.game_source = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.ChesscomGameMetadata",
  "name": "game_source",
  "number": 4,
  "type": ".chesscom.chess.v1.ChesscomGameSource",
  "label": "LABEL_OPTIONAL",
  "oneof": "_game_source",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12749"></a>
## FND-12749: Native message: chesscom.chess.v1.PlayerMetadata

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "PlayerMetadata",
  "field": [
    {
      "name": "color",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.chess.v1.Color"
    },
    {
      "name": "ratings",
      "number": 2,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.Rating"
    },
    {
      "name": "name",
      "number": 4,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "chesscom_metadata",
      "number": 3,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.chess.v1.ChesscomPlayerMetadata",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_name"
    },
    {
      "name": "_chesscom_metadata"
    }
  ]
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12750"></a>
## FND-12750: chesscom.chess.v1.PlayerMetadata.color = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.PlayerMetadata",
  "name": "color",
  "number": 1,
  "type": ".chesscom.chess.v1.Color",
  "label": "LABEL_OPTIONAL",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12751"></a>
## FND-12751: chesscom.chess.v1.PlayerMetadata.ratings = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.PlayerMetadata",
  "name": "ratings",
  "number": 2,
  "type": ".chesscom.chess.v1.Rating",
  "label": "LABEL_REPEATED",
  "oneof": null,
  "proto3_optional": false,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12752"></a>
## FND-12752: chesscom.chess.v1.PlayerMetadata.name = 4

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.PlayerMetadata",
  "name": "name",
  "number": 4,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_name",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12753"></a>
## FND-12753: chesscom.chess.v1.PlayerMetadata.chesscom_metadata = 3

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.PlayerMetadata",
  "name": "chesscom_metadata",
  "number": 3,
  "type": ".chesscom.chess.v1.ChesscomPlayerMetadata",
  "label": "LABEL_OPTIONAL",
  "oneof": "_chesscom_metadata",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12754"></a>
## FND-12754: Native message: chesscom.chess.v1.Rating

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "Rating",
  "field": [
    {
      "name": "rating",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "oneof_index": 0,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_rating"
    }
  ]
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12755"></a>
## FND-12755: chesscom.chess.v1.Rating.rating = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.Rating",
  "name": "rating",
  "number": 1,
  "type": "TYPE_INT32",
  "label": "LABEL_OPTIONAL",
  "oneof": "_rating",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12756"></a>
## FND-12756: Native message: chesscom.chess.v1.ChesscomPlayerMetadata

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "ChesscomPlayerMetadata",
  "field": [
    {
      "name": "user_id",
      "number": 1,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "oneof_index": 0,
      "proto3_optional": true
    },
    {
      "name": "legacy_user_id",
      "number": 2,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT64",
      "oneof_index": 1,
      "proto3_optional": true
    }
  ],
  "oneof_decl": [
    {
      "name": "_user_id"
    },
    {
      "name": "_legacy_user_id"
    }
  ]
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12757"></a>
## FND-12757: chesscom.chess.v1.ChesscomPlayerMetadata.user_id = 1

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.ChesscomPlayerMetadata",
  "name": "user_id",
  "number": 1,
  "type": "TYPE_STRING",
  "label": "LABEL_OPTIONAL",
  "oneof": "_user_id",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12758"></a>
## FND-12758: chesscom.chess.v1.ChesscomPlayerMetadata.legacy_user_id = 2

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "field",
  "message": "chesscom.chess.v1.ChesscomPlayerMetadata",
  "name": "legacy_user_id",
  "number": 2,
  "type": "TYPE_INT64",
  "label": "LABEL_OPTIONAL",
  "oneof": "_legacy_user_id",
  "proto3_optional": true,
  "source_id": "SRC-0883",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0883** `research/refinement/wasm-descriptors/chesscom_chess_v1_game.proto.bin` — [preserved redacted evidence](../evidence/descriptors/5c5bcbb636b16652a6a1976e3c80fb4101f0df88458f17656c7fff008567966b.bin)

**Source references:** SRC-0883, SRC-1900  
**URL references:** None independently associated  
**Related findings:** FND-12706, FND-12707, FND-12708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12759"></a>
## FND-12759: chesscom.chess.v1.GamePhase.GAME_PHASE_UNSPECIFIED = 0

**Category:** native_interfaces  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "kind": "enum_value",
  "enum": "chesscom.chess.v1.GamePhase",
  "name": "GAME_PHASE_UNSPECIFIED",
  "number": 0,
  "source_id": "SRC-0884",
  "source_format": "native descriptor"
}

### Evidence

- **SRC-0884** `research/refinement/wasm-descriptors/chesscom_chess_v1_game_phase.proto.bin` — [preserved redacted evidence](../evidence/descriptors/d6f84b0a3e21ebc8a831c74cb5212ed8b1f0d5b500adc0da6f34ff140ea73062.bin)

**Source references:** SRC-0884, SRC-1884  
**URL references:** None independently associated  
**Related findings:** FND-12760, FND-12761

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
