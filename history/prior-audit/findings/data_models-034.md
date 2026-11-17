# data_models — findings 3301–3400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-03575"></a>
## FND-03575: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_ADD_EVALUATIONS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_ADD_EVALUATIONS = 1;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 166.

```text
: proto3

package chesscom.explanation_engine.v1;

enum FeatureId {
  FEATURE_ID_UNSPECIFIED = 0;
  FEATURE_ID_ADD_EVALUATIONS = 1;
  FEATURE_ID_CEE_VERSION = 2;
  FEATURE_ID_EXPECTED_POINTS = 3;
  FEATURE_ID_GAME_ANALYSIS = 4;
  FEATURE_ID_GAME_PHASE_TRANSITIONS = 5;
  FEATURE_ID_GAME_POINT_INFO = 6;
  FEATURE_ID_GET_GAME_RESULT = 7;
  FEATURE_ID_GET_BOT_CHAT = 8;
  FEATURE_ID_GET_BOT_MOVE = 9;
  FEATURE_ID_GET_COMP
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03576"></a>
## FND-03576: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_CEE_VERSION = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_CEE_VERSION = 2;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 200.

```text
tion_engine.v1;

enum FeatureId {
  FEATURE_ID_UNSPECIFIED = 0;
  FEATURE_ID_ADD_EVALUATIONS = 1;
  FEATURE_ID_CEE_VERSION = 2;
  FEATURE_ID_EXPECTED_POINTS = 3;
  FEATURE_ID_GAME_ANALYSIS = 4;
  FEATURE_ID_GAME_PHASE_TRANSITIONS = 5;
  FEATURE_ID_GAME_POINT_INFO = 6;
  FEATURE_ID_GET_GAME_RESULT = 7;
  FEATURE_ID_GET_BOT_CHAT = 8;
  FEATURE_ID_GET_BOT_MOVE = 9;
  FEATURE_ID_GET_COMPRESSED_POSITION = 10;
  FEATURE_ID
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03577"></a>
## FND-03577: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_EXPECTED_POINTS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_EXPECTED_POINTS = 3;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 230.

```text
d {
  FEATURE_ID_UNSPECIFIED = 0;
  FEATURE_ID_ADD_EVALUATIONS = 1;
  FEATURE_ID_CEE_VERSION = 2;
  FEATURE_ID_EXPECTED_POINTS = 3;
  FEATURE_ID_GAME_ANALYSIS = 4;
  FEATURE_ID_GAME_PHASE_TRANSITIONS = 5;
  FEATURE_ID_GAME_POINT_INFO = 6;
  FEATURE_ID_GET_GAME_RESULT = 7;
  FEATURE_ID_GET_BOT_CHAT = 8;
  FEATURE_ID_GET_BOT_MOVE = 9;
  FEATURE_ID_GET_COMPRESSED_POSITION = 10;
  FEATURE_ID_GET_ERGONOMIC_GAME = 11;
  FE
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03578"></a>
## FND-03578: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GAME_ANALYSIS = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GAME_ANALYSIS = 4;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 264.

```text
  FEATURE_ID_ADD_EVALUATIONS = 1;
  FEATURE_ID_CEE_VERSION = 2;
  FEATURE_ID_EXPECTED_POINTS = 3;
  FEATURE_ID_GAME_ANALYSIS = 4;
  FEATURE_ID_GAME_PHASE_TRANSITIONS = 5;
  FEATURE_ID_GAME_POINT_INFO = 6;
  FEATURE_ID_GET_GAME_RESULT = 7;
  FEATURE_ID_GET_BOT_CHAT = 8;
  FEATURE_ID_GET_BOT_MOVE = 9;
  FEATURE_ID_GET_COMPRESSED_POSITION = 10;
  FEATURE_ID_GET_ERGONOMIC_GAME = 11;
  FEATURE_ID_GET_ERGONOMIC_POSITION = 
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03579"></a>
## FND-03579: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GAME_PHASE_TRANSITIONS = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GAME_PHASE_TRANSITIONS = 5;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 296.

```text
;
  FEATURE_ID_CEE_VERSION = 2;
  FEATURE_ID_EXPECTED_POINTS = 3;
  FEATURE_ID_GAME_ANALYSIS = 4;
  FEATURE_ID_GAME_PHASE_TRANSITIONS = 5;
  FEATURE_ID_GAME_POINT_INFO = 6;
  FEATURE_ID_GET_GAME_RESULT = 7;
  FEATURE_ID_GET_BOT_CHAT = 8;
  FEATURE_ID_GET_BOT_MOVE = 9;
  FEATURE_ID_GET_COMPRESSED_POSITION = 10;
  FEATURE_ID_GET_ERGONOMIC_GAME = 11;
  FEATURE_ID_GET_ERGONOMIC_POSITION = 12;
  FEATURE_ID_GET_FEN = 13;
 
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03580"></a>
## FND-03580: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GAME_POINT_INFO = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GAME_POINT_INFO = 6;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 337.

```text
_ID_EXPECTED_POINTS = 3;
  FEATURE_ID_GAME_ANALYSIS = 4;
  FEATURE_ID_GAME_PHASE_TRANSITIONS = 5;
  FEATURE_ID_GAME_POINT_INFO = 6;
  FEATURE_ID_GET_GAME_RESULT = 7;
  FEATURE_ID_GET_BOT_CHAT = 8;
  FEATURE_ID_GET_BOT_MOVE = 9;
  FEATURE_ID_GET_COMPRESSED_POSITION = 10;
  FEATURE_ID_GET_ERGONOMIC_GAME = 11;
  FEATURE_ID_GET_ERGONOMIC_POSITION = 12;
  FEATURE_ID_GET_FEN = 13;
  FEATURE_ID_GET_GAME_STATE = 14;
  FEATUR
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03581"></a>
## FND-03581: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_GAME_RESULT = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_GAME_RESULT = 7;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 371.

```text
_ID_GAME_ANALYSIS = 4;
  FEATURE_ID_GAME_PHASE_TRANSITIONS = 5;
  FEATURE_ID_GAME_POINT_INFO = 6;
  FEATURE_ID_GET_GAME_RESULT = 7;
  FEATURE_ID_GET_BOT_CHAT = 8;
  FEATURE_ID_GET_BOT_MOVE = 9;
  FEATURE_ID_GET_COMPRESSED_POSITION = 10;
  FEATURE_ID_GET_ERGONOMIC_GAME = 11;
  FEATURE_ID_GET_ERGONOMIC_POSITION = 12;
  FEATURE_ID_GET_FEN = 13;
  FEATURE_ID_GET_GAME_STATE = 14;
  FEATURE_ID_GET_MOVE_DETAILS = 15;
  FEAT
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03582"></a>
## FND-03582: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_BOT_CHAT = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_BOT_CHAT = 8;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 405.

```text
D_GAME_PHASE_TRANSITIONS = 5;
  FEATURE_ID_GAME_POINT_INFO = 6;
  FEATURE_ID_GET_GAME_RESULT = 7;
  FEATURE_ID_GET_BOT_CHAT = 8;
  FEATURE_ID_GET_BOT_MOVE = 9;
  FEATURE_ID_GET_COMPRESSED_POSITION = 10;
  FEATURE_ID_GET_ERGONOMIC_GAME = 11;
  FEATURE_ID_GET_ERGONOMIC_POSITION = 12;
  FEATURE_ID_GET_FEN = 13;
  FEATURE_ID_GET_GAME_STATE = 14;
  FEATURE_ID_GET_MOVE_DETAILS = 15;
  FEATURE_ID_GET_OPENING = 16;
  FEATURE
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03583"></a>
## FND-03583: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_BOT_MOVE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_BOT_MOVE = 9;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 436.

```text
 FEATURE_ID_GAME_POINT_INFO = 6;
  FEATURE_ID_GET_GAME_RESULT = 7;
  FEATURE_ID_GET_BOT_CHAT = 8;
  FEATURE_ID_GET_BOT_MOVE = 9;
  FEATURE_ID_GET_COMPRESSED_POSITION = 10;
  FEATURE_ID_GET_ERGONOMIC_GAME = 11;
  FEATURE_ID_GET_ERGONOMIC_POSITION = 12;
  FEATURE_ID_GET_FEN = 13;
  FEATURE_ID_GET_GAME_STATE = 14;
  FEATURE_ID_GET_MOVE_DETAILS = 15;
  FEATURE_ID_GET_OPENING = 16;
  FEATURE_ID_GET_PGN = 17;
  FEATURE_ID_
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03584"></a>
## FND-03584: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_COMPRESSED_POSITION = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_COMPRESSED_POSITION = 10;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 467.

```text
;
  FEATURE_ID_GET_GAME_RESULT = 7;
  FEATURE_ID_GET_BOT_CHAT = 8;
  FEATURE_ID_GET_BOT_MOVE = 9;
  FEATURE_ID_GET_COMPRESSED_POSITION = 10;
  FEATURE_ID_GET_ERGONOMIC_GAME = 11;
  FEATURE_ID_GET_ERGONOMIC_POSITION = 12;
  FEATURE_ID_GET_FEN = 13;
  FEATURE_ID_GET_GAME_STATE = 14;
  FEATURE_ID_GET_MOVE_DETAILS = 15;
  FEATURE_ID_GET_OPENING = 16;
  FEATURE_ID_GET_PGN = 17;
  FEATURE_ID_GET_PUNISH_MOVE = 18;
  FEATURE
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03585"></a>
## FND-03585: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_ERGONOMIC_GAME = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_ERGONOMIC_GAME = 11;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 510.

```text
RE_ID_GET_BOT_CHAT = 8;
  FEATURE_ID_GET_BOT_MOVE = 9;
  FEATURE_ID_GET_COMPRESSED_POSITION = 10;
  FEATURE_ID_GET_ERGONOMIC_GAME = 11;
  FEATURE_ID_GET_ERGONOMIC_POSITION = 12;
  FEATURE_ID_GET_FEN = 13;
  FEATURE_ID_GET_GAME_STATE = 14;
  FEATURE_ID_GET_MOVE_DETAILS = 15;
  FEATURE_ID_GET_OPENING = 16;
  FEATURE_ID_GET_PGN = 17;
  FEATURE_ID_GET_PUNISH_MOVE = 18;
  FEATURE_ID_LEGAL_MOVES = 19;
  FEATURE_ID_LEGAL_PR
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03586"></a>
## FND-03586: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_ERGONOMIC_POSITION = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_ERGONOMIC_POSITION = 12;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 548.

```text
ET_BOT_MOVE = 9;
  FEATURE_ID_GET_COMPRESSED_POSITION = 10;
  FEATURE_ID_GET_ERGONOMIC_GAME = 11;
  FEATURE_ID_GET_ERGONOMIC_POSITION = 12;
  FEATURE_ID_GET_FEN = 13;
  FEATURE_ID_GET_GAME_STATE = 14;
  FEATURE_ID_GET_MOVE_DETAILS = 15;
  FEATURE_ID_GET_OPENING = 16;
  FEATURE_ID_GET_PGN = 17;
  FEATURE_ID_GET_PUNISH_MOVE = 18;
  FEATURE_ID_LEGAL_MOVES = 19;
  FEATURE_ID_LEGAL_PREMOVES = 20;
  FEATURE_ID_LOAD_BOT = 2
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03587"></a>
## FND-03587: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_FEN = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_FEN = 13;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 590.

```text
ED_POSITION = 10;
  FEATURE_ID_GET_ERGONOMIC_GAME = 11;
  FEATURE_ID_GET_ERGONOMIC_POSITION = 12;
  FEATURE_ID_GET_FEN = 13;
  FEATURE_ID_GET_GAME_STATE = 14;
  FEATURE_ID_GET_MOVE_DETAILS = 15;
  FEATURE_ID_GET_OPENING = 16;
  FEATURE_ID_GET_PGN = 17;
  FEATURE_ID_GET_PUNISH_MOVE = 18;
  FEATURE_ID_LEGAL_MOVES = 19;
  FEATURE_ID_LEGAL_PREMOVES = 20;
  FEATURE_ID_LOAD_BOT = 21;
  FEATURE_ID_LOAD_GAME_STATE = 22;
  FE
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03588"></a>
## FND-03588: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_GAME_STATE = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_GAME_STATE = 14;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 617.

```text
_ID_GET_ERGONOMIC_GAME = 11;
  FEATURE_ID_GET_ERGONOMIC_POSITION = 12;
  FEATURE_ID_GET_FEN = 13;
  FEATURE_ID_GET_GAME_STATE = 14;
  FEATURE_ID_GET_MOVE_DETAILS = 15;
  FEATURE_ID_GET_OPENING = 16;
  FEATURE_ID_GET_PGN = 17;
  FEATURE_ID_GET_PUNISH_MOVE = 18;
  FEATURE_ID_LEGAL_MOVES = 19;
  FEATURE_ID_LEGAL_PREMOVES = 20;
  FEATURE_ID_LOAD_BOT = 21;
  FEATURE_ID_LOAD_GAME_STATE = 22;
  FEATURE_ID_LUA_COMPLETION = 2
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03589"></a>
## FND-03589: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_MOVE_DETAILS = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_MOVE_DETAILS = 15;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 651.

```text
TURE_ID_GET_ERGONOMIC_POSITION = 12;
  FEATURE_ID_GET_FEN = 13;
  FEATURE_ID_GET_GAME_STATE = 14;
  FEATURE_ID_GET_MOVE_DETAILS = 15;
  FEATURE_ID_GET_OPENING = 16;
  FEATURE_ID_GET_PGN = 17;
  FEATURE_ID_GET_PUNISH_MOVE = 18;
  FEATURE_ID_LEGAL_MOVES = 19;
  FEATURE_ID_LEGAL_PREMOVES = 20;
  FEATURE_ID_LOAD_BOT = 21;
  FEATURE_ID_LOAD_GAME_STATE = 22;
  FEATURE_ID_LUA_COMPLETION = 23;
  FEATURE_ID_MAKE_MOVES = 24;
 
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03590"></a>
## FND-03590: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_OPENING = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_OPENING = 16;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 687.

```text

  FEATURE_ID_GET_FEN = 13;
  FEATURE_ID_GET_GAME_STATE = 14;
  FEATURE_ID_GET_MOVE_DETAILS = 15;
  FEATURE_ID_GET_OPENING = 16;
  FEATURE_ID_GET_PGN = 17;
  FEATURE_ID_GET_PUNISH_MOVE = 18;
  FEATURE_ID_LEGAL_MOVES = 19;
  FEATURE_ID_LEGAL_PREMOVES = 20;
  FEATURE_ID_LOAD_BOT = 21;
  FEATURE_ID_LOAD_GAME_STATE = 22;
  FEATURE_ID_LUA_COMPLETION = 23;
  FEATURE_ID_MAKE_MOVES = 24;
  FEATURE_ID_MOVE_CLASSIFICATION = 25
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03591"></a>
## FND-03591: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_PGN = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_PGN = 17;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 718.

```text
EATURE_ID_GET_GAME_STATE = 14;
  FEATURE_ID_GET_MOVE_DETAILS = 15;
  FEATURE_ID_GET_OPENING = 16;
  FEATURE_ID_GET_PGN = 17;
  FEATURE_ID_GET_PUNISH_MOVE = 18;
  FEATURE_ID_LEGAL_MOVES = 19;
  FEATURE_ID_LEGAL_PREMOVES = 20;
  FEATURE_ID_LOAD_BOT = 21;
  FEATURE_ID_LOAD_GAME_STATE = 22;
  FEATURE_ID_LUA_COMPLETION = 23;
  FEATURE_ID_MAKE_MOVES = 24;
  FEATURE_ID_MOVE_CLASSIFICATION = 25;
  FEATURE_ID_NEW_GAME = 26;
 
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03592"></a>
## FND-03592: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_PUNISH_MOVE = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_PUNISH_MOVE = 18;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 745.

```text
14;
  FEATURE_ID_GET_MOVE_DETAILS = 15;
  FEATURE_ID_GET_OPENING = 16;
  FEATURE_ID_GET_PGN = 17;
  FEATURE_ID_GET_PUNISH_MOVE = 18;
  FEATURE_ID_LEGAL_MOVES = 19;
  FEATURE_ID_LEGAL_PREMOVES = 20;
  FEATURE_ID_LOAD_BOT = 21;
  FEATURE_ID_LOAD_GAME_STATE = 22;
  FEATURE_ID_LUA_COMPLETION = 23;
  FEATURE_ID_MAKE_MOVES = 24;
  FEATURE_ID_MOVE_CLASSIFICATION = 25;
  FEATURE_ID_NEW_GAME = 26;
  FEATURE_ID_RUN_LUA = 28;
 
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03593"></a>
## FND-03593: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_LEGAL_MOVES = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_LEGAL_MOVES = 19;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 780.

```text
 15;
  FEATURE_ID_GET_OPENING = 16;
  FEATURE_ID_GET_PGN = 17;
  FEATURE_ID_GET_PUNISH_MOVE = 18;
  FEATURE_ID_LEGAL_MOVES = 19;
  FEATURE_ID_LEGAL_PREMOVES = 20;
  FEATURE_ID_LOAD_BOT = 21;
  FEATURE_ID_LOAD_GAME_STATE = 22;
  FEATURE_ID_LUA_COMPLETION = 23;
  FEATURE_ID_MAKE_MOVES = 24;
  FEATURE_ID_MOVE_CLASSIFICATION = 25;
  FEATURE_ID_NEW_GAME = 26;
  FEATURE_ID_RUN_LUA = 28;
  FEATURE_ID_RUN_SEARCH = 29;
  FEAT
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03594"></a>
## FND-03594: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_LEGAL_PREMOVES = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_LEGAL_PREMOVES = 20;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 811.

```text
 16;
  FEATURE_ID_GET_PGN = 17;
  FEATURE_ID_GET_PUNISH_MOVE = 18;
  FEATURE_ID_LEGAL_MOVES = 19;
  FEATURE_ID_LEGAL_PREMOVES = 20;
  FEATURE_ID_LOAD_BOT = 21;
  FEATURE_ID_LOAD_GAME_STATE = 22;
  FEATURE_ID_LUA_COMPLETION = 23;
  FEATURE_ID_MAKE_MOVES = 24;
  FEATURE_ID_MOVE_CLASSIFICATION = 25;
  FEATURE_ID_NEW_GAME = 26;
  FEATURE_ID_RUN_LUA = 28;
  FEATURE_ID_RUN_SEARCH = 29;
  FEATURE_ID_SET_GAME_RESULT = 30;
  
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03595"></a>
## FND-03595: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_LOAD_BOT = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_LOAD_BOT = 21;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 845.

```text
FEATURE_ID_GET_PUNISH_MOVE = 18;
  FEATURE_ID_LEGAL_MOVES = 19;
  FEATURE_ID_LEGAL_PREMOVES = 20;
  FEATURE_ID_LOAD_BOT = 21;
  FEATURE_ID_LOAD_GAME_STATE = 22;
  FEATURE_ID_LUA_COMPLETION = 23;
  FEATURE_ID_MAKE_MOVES = 24;
  FEATURE_ID_MOVE_CLASSIFICATION = 25;
  FEATURE_ID_NEW_GAME = 26;
  FEATURE_ID_RUN_LUA = 28;
  FEATURE_ID_RUN_SEARCH = 29;
  FEATURE_ID_SET_GAME_RESULT = 30;
  FEATURE_ID_SIMPLE_THREATS = 31;
  
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03596"></a>
## FND-03596: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_LOAD_GAME_STATE = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_LOAD_GAME_STATE = 22;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 873.

```text
 18;
  FEATURE_ID_LEGAL_MOVES = 19;
  FEATURE_ID_LEGAL_PREMOVES = 20;
  FEATURE_ID_LOAD_BOT = 21;
  FEATURE_ID_LOAD_GAME_STATE = 22;
  FEATURE_ID_LUA_COMPLETION = 23;
  FEATURE_ID_MAKE_MOVES = 24;
  FEATURE_ID_MOVE_CLASSIFICATION = 25;
  FEATURE_ID_NEW_GAME = 26;
  FEATURE_ID_RUN_LUA = 28;
  FEATURE_ID_RUN_SEARCH = 29;
  FEATURE_ID_SET_GAME_RESULT = 30;
  FEATURE_ID_SIMPLE_THREATS = 31;
  FEATURE_ID_VALIDATE_FEN = 32
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03597"></a>
## FND-03597: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_LUA_COMPLETION = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_LUA_COMPLETION = 23;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 908.

```text

  FEATURE_ID_LEGAL_PREMOVES = 20;
  FEATURE_ID_LOAD_BOT = 21;
  FEATURE_ID_LOAD_GAME_STATE = 22;
  FEATURE_ID_LUA_COMPLETION = 23;
  FEATURE_ID_MAKE_MOVES = 24;
  FEATURE_ID_MOVE_CLASSIFICATION = 25;
  FEATURE_ID_NEW_GAME = 26;
  FEATURE_ID_RUN_LUA = 28;
  FEATURE_ID_RUN_SEARCH = 29;
  FEATURE_ID_SET_GAME_RESULT = 30;
  FEATURE_ID_SIMPLE_THREATS = 31;
  FEATURE_ID_VALIDATE_FEN = 32;
  FEATURE_ID_CEE_INTERNAL_COMPONE
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03598"></a>
## FND-03598: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_MAKE_MOVES = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_MAKE_MOVES = 24;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 942.

```text

  FEATURE_ID_LOAD_BOT = 21;
  FEATURE_ID_LOAD_GAME_STATE = 22;
  FEATURE_ID_LUA_COMPLETION = 23;
  FEATURE_ID_MAKE_MOVES = 24;
  FEATURE_ID_MOVE_CLASSIFICATION = 25;
  FEATURE_ID_NEW_GAME = 26;
  FEATURE_ID_RUN_LUA = 28;
  FEATURE_ID_RUN_SEARCH = 29;
  FEATURE_ID_SET_GAME_RESULT = 30;
  FEATURE_ID_SIMPLE_THREATS = 31;
  FEATURE_ID_VALIDATE_FEN = 32;
  FEATURE_ID_CEE_INTERNAL_COMPONENTS = 33;
  FEATURE_ID_GAME_TREE =
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03599"></a>
## FND-03599: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_MOVE_CLASSIFICATION = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_MOVE_CLASSIFICATION = 25;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 972.

```text
 FEATURE_ID_LOAD_GAME_STATE = 22;
  FEATURE_ID_LUA_COMPLETION = 23;
  FEATURE_ID_MAKE_MOVES = 24;
  FEATURE_ID_MOVE_CLASSIFICATION = 25;
  FEATURE_ID_NEW_GAME = 26;
  FEATURE_ID_RUN_LUA = 28;
  FEATURE_ID_RUN_SEARCH = 29;
  FEATURE_ID_SET_GAME_RESULT = 30;
  FEATURE_ID_SIMPLE_THREATS = 31;
  FEATURE_ID_VALIDATE_FEN = 32;
  FEATURE_ID_CEE_INTERNAL_COMPONENTS = 33;
  FEATURE_ID_GAME_TREE = 34;
  FEATURE_ID_INIT_ENGINE_
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03600"></a>
## FND-03600: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_NEW_GAME = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_NEW_GAME = 26;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1011.

```text
TURE_ID_LUA_COMPLETION = 23;
  FEATURE_ID_MAKE_MOVES = 24;
  FEATURE_ID_MOVE_CLASSIFICATION = 25;
  FEATURE_ID_NEW_GAME = 26;
  FEATURE_ID_RUN_LUA = 28;
  FEATURE_ID_RUN_SEARCH = 29;
  FEATURE_ID_SET_GAME_RESULT = 30;
  FEATURE_ID_SIMPLE_THREATS = 31;
  FEATURE_ID_VALIDATE_FEN = 32;
  FEATURE_ID_CEE_INTERNAL_COMPONENTS = 33;
  FEATURE_ID_GAME_TREE = 34;
  FEATURE_ID_INIT_ENGINE_POOL = 35;
  FEATURE_ID_SET_INTERNAL_EN
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03601"></a>
## FND-03601: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_RUN_LUA = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_RUN_LUA = 28;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1039.

```text

  FEATURE_ID_MAKE_MOVES = 24;
  FEATURE_ID_MOVE_CLASSIFICATION = 25;
  FEATURE_ID_NEW_GAME = 26;
  FEATURE_ID_RUN_LUA = 28;
  FEATURE_ID_RUN_SEARCH = 29;
  FEATURE_ID_SET_GAME_RESULT = 30;
  FEATURE_ID_SIMPLE_THREATS = 31;
  FEATURE_ID_VALIDATE_FEN = 32;
  FEATURE_ID_CEE_INTERNAL_COMPONENTS = 33;
  FEATURE_ID_GAME_TREE = 34;
  FEATURE_ID_INIT_ENGINE_POOL = 35;
  FEATURE_ID_SET_INTERNAL_ENGINE = 36;
  FEATURE_ID_ADD_
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03602"></a>
## FND-03602: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_RUN_SEARCH = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_RUN_SEARCH = 29;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1066.

```text
24;
  FEATURE_ID_MOVE_CLASSIFICATION = 25;
  FEATURE_ID_NEW_GAME = 26;
  FEATURE_ID_RUN_LUA = 28;
  FEATURE_ID_RUN_SEARCH = 29;
  FEATURE_ID_SET_GAME_RESULT = 30;
  FEATURE_ID_SIMPLE_THREATS = 31;
  FEATURE_ID_VALIDATE_FEN = 32;
  FEATURE_ID_CEE_INTERNAL_COMPONENTS = 33;
  FEATURE_ID_GAME_TREE = 34;
  FEATURE_ID_INIT_ENGINE_POOL = 35;
  FEATURE_ID_SET_INTERNAL_ENGINE = 36;
  FEATURE_ID_ADD_EXTERNAL_ENGINE = 37;
  FEA
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03603"></a>
## FND-03603: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_SET_GAME_RESULT = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_SET_GAME_RESULT = 30;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1096.

```text
CATION = 25;
  FEATURE_ID_NEW_GAME = 26;
  FEATURE_ID_RUN_LUA = 28;
  FEATURE_ID_RUN_SEARCH = 29;
  FEATURE_ID_SET_GAME_RESULT = 30;
  FEATURE_ID_SIMPLE_THREATS = 31;
  FEATURE_ID_VALIDATE_FEN = 32;
  FEATURE_ID_CEE_INTERNAL_COMPONENTS = 33;
  FEATURE_ID_GAME_TREE = 34;
  FEATURE_ID_INIT_ENGINE_POOL = 35;
  FEATURE_ID_SET_INTERNAL_ENGINE = 36;
  FEATURE_ID_ADD_EXTERNAL_ENGINE = 37;
  FEATURE_ID_REMOVE_EXTERNAL_ENGINE
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03604"></a>
## FND-03604: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_SIMPLE_THREATS = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_SIMPLE_THREATS = 31;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1131.

```text
= 26;
  FEATURE_ID_RUN_LUA = 28;
  FEATURE_ID_RUN_SEARCH = 29;
  FEATURE_ID_SET_GAME_RESULT = 30;
  FEATURE_ID_SIMPLE_THREATS = 31;
  FEATURE_ID_VALIDATE_FEN = 32;
  FEATURE_ID_CEE_INTERNAL_COMPONENTS = 33;
  FEATURE_ID_GAME_TREE = 34;
  FEATURE_ID_INIT_ENGINE_POOL = 35;
  FEATURE_ID_SET_INTERNAL_ENGINE = 36;
  FEATURE_ID_ADD_EXTERNAL_ENGINE = 37;
  FEATURE_ID_REMOVE_EXTERNAL_ENGINE = 38;
  FEATURE_ID_GET_SAN_MOVES =
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03605"></a>
## FND-03605: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_VALIDATE_FEN = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_VALIDATE_FEN = 32;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1165.

```text
 FEATURE_ID_RUN_SEARCH = 29;
  FEATURE_ID_SET_GAME_RESULT = 30;
  FEATURE_ID_SIMPLE_THREATS = 31;
  FEATURE_ID_VALIDATE_FEN = 32;
  FEATURE_ID_CEE_INTERNAL_COMPONENTS = 33;
  FEATURE_ID_GAME_TREE = 34;
  FEATURE_ID_INIT_ENGINE_POOL = 35;
  FEATURE_ID_SET_INTERNAL_ENGINE = 36;
  FEATURE_ID_ADD_EXTERNAL_ENGINE = 37;
  FEATURE_ID_REMOVE_EXTERNAL_ENGINE = 38;
  FEATURE_ID_GET_SAN_MOVES = 39;
  FEATURE_ID_LOAD_COACH = 40;
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03606"></a>
## FND-03606: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_CEE_INTERNAL_COMPONENTS = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_CEE_INTERNAL_COMPONENTS = 33;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1197.

```text
EATURE_ID_SET_GAME_RESULT = 30;
  FEATURE_ID_SIMPLE_THREATS = 31;
  FEATURE_ID_VALIDATE_FEN = 32;
  FEATURE_ID_CEE_INTERNAL_COMPONENTS = 33;
  FEATURE_ID_GAME_TREE = 34;
  FEATURE_ID_INIT_ENGINE_POOL = 35;
  FEATURE_ID_SET_INTERNAL_ENGINE = 36;
  FEATURE_ID_ADD_EXTERNAL_ENGINE = 37;
  FEATURE_ID_REMOVE_EXTERNAL_ENGINE = 38;
  FEATURE_ID_GET_SAN_MOVES = 39;
  FEATURE_ID_LOAD_COACH = 40;
  FEATURE_ID_SET_COACH = 41;
  
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03607"></a>
## FND-03607: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GAME_TREE = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GAME_TREE = 34;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1240.

```text
D_SIMPLE_THREATS = 31;
  FEATURE_ID_VALIDATE_FEN = 32;
  FEATURE_ID_CEE_INTERNAL_COMPONENTS = 33;
  FEATURE_ID_GAME_TREE = 34;
  FEATURE_ID_INIT_ENGINE_POOL = 35;
  FEATURE_ID_SET_INTERNAL_ENGINE = 36;
  FEATURE_ID_ADD_EXTERNAL_ENGINE = 37;
  FEATURE_ID_REMOVE_EXTERNAL_ENGINE = 38;
  FEATURE_ID_GET_SAN_MOVES = 39;
  FEATURE_ID_LOAD_COACH = 40;
  FEATURE_ID_SET_COACH = 41;
  FEATURE_ID_GAME_REVIEW = 42;
  FEATURE_ID_U
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03608"></a>
## FND-03608: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INIT_ENGINE_POOL = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INIT_ENGINE_POOL = 35;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1269.

```text
URE_ID_VALIDATE_FEN = 32;
  FEATURE_ID_CEE_INTERNAL_COMPONENTS = 33;
  FEATURE_ID_GAME_TREE = 34;
  FEATURE_ID_INIT_ENGINE_POOL = 35;
  FEATURE_ID_SET_INTERNAL_ENGINE = 36;
  FEATURE_ID_ADD_EXTERNAL_ENGINE = 37;
  FEATURE_ID_REMOVE_EXTERNAL_ENGINE = 38;
  FEATURE_ID_GET_SAN_MOVES = 39;
  FEATURE_ID_LOAD_COACH = 40;
  FEATURE_ID_SET_COACH = 41;
  FEATURE_ID_GAME_REVIEW = 42;
  FEATURE_ID_UNMAKE_MOVES = 43;
  FEATURE_I
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03609"></a>
## FND-03609: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_SET_INTERNAL_ENGINE = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_SET_INTERNAL_ENGINE = 36;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1305.

```text
ID_CEE_INTERNAL_COMPONENTS = 33;
  FEATURE_ID_GAME_TREE = 34;
  FEATURE_ID_INIT_ENGINE_POOL = 35;
  FEATURE_ID_SET_INTERNAL_ENGINE = 36;
  FEATURE_ID_ADD_EXTERNAL_ENGINE = 37;
  FEATURE_ID_REMOVE_EXTERNAL_ENGINE = 38;
  FEATURE_ID_GET_SAN_MOVES = 39;
  FEATURE_ID_LOAD_COACH = 40;
  FEATURE_ID_SET_COACH = 41;
  FEATURE_ID_GAME_REVIEW = 42;
  FEATURE_ID_UNMAKE_MOVES = 43;
  FEATURE_ID_GET_CHESS960_INITIAL_POSITION = 44
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03610"></a>
## FND-03610: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_ADD_EXTERNAL_ENGINE = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_ADD_EXTERNAL_ENGINE = 37;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1344.

```text
URE_ID_GAME_TREE = 34;
  FEATURE_ID_INIT_ENGINE_POOL = 35;
  FEATURE_ID_SET_INTERNAL_ENGINE = 36;
  FEATURE_ID_ADD_EXTERNAL_ENGINE = 37;
  FEATURE_ID_REMOVE_EXTERNAL_ENGINE = 38;
  FEATURE_ID_GET_SAN_MOVES = 39;
  FEATURE_ID_LOAD_COACH = 40;
  FEATURE_ID_SET_COACH = 41;
  FEATURE_ID_GAME_REVIEW = 42;
  FEATURE_ID_UNMAKE_MOVES = 43;
  FEATURE_ID_GET_CHESS960_INITIAL_POSITION = 44;
  FEATURE_ID_GET_COACH_CHAT = 45;
  F
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03611"></a>
## FND-03611: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_REMOVE_EXTERNAL_ENGINE = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_REMOVE_EXTERNAL_ENGINE = 38;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1383.

```text
T_ENGINE_POOL = 35;
  FEATURE_ID_SET_INTERNAL_ENGINE = 36;
  FEATURE_ID_ADD_EXTERNAL_ENGINE = 37;
  FEATURE_ID_REMOVE_EXTERNAL_ENGINE = 38;
  FEATURE_ID_GET_SAN_MOVES = 39;
  FEATURE_ID_LOAD_COACH = 40;
  FEATURE_ID_SET_COACH = 41;
  FEATURE_ID_GAME_REVIEW = 42;
  FEATURE_ID_UNMAKE_MOVES = 43;
  FEATURE_ID_GET_CHESS960_INITIAL_POSITION = 44;
  FEATURE_ID_GET_COACH_CHAT = 45;
  FEATURE_ID_UPDATE_EXPERIMENTAL_OPTIONS =
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03612"></a>
## FND-03612: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_SAN_MOVES = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_SAN_MOVES = 39;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1425.

```text
NAL_ENGINE = 36;
  FEATURE_ID_ADD_EXTERNAL_ENGINE = 37;
  FEATURE_ID_REMOVE_EXTERNAL_ENGINE = 38;
  FEATURE_ID_GET_SAN_MOVES = 39;
  FEATURE_ID_LOAD_COACH = 40;
  FEATURE_ID_SET_COACH = 41;
  FEATURE_ID_GAME_REVIEW = 42;
  FEATURE_ID_UNMAKE_MOVES = 43;
  FEATURE_ID_GET_CHESS960_INITIAL_POSITION = 44;
  FEATURE_ID_GET_COACH_CHAT = 45;
  FEATURE_ID_UPDATE_EXPERIMENTAL_OPTIONS = 46;
  FEATURE_ID_GET_COACH_HINT = 47;
  F
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03613"></a>
## FND-03613: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_LOAD_COACH = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_LOAD_COACH = 40;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1458.

```text
_EXTERNAL_ENGINE = 37;
  FEATURE_ID_REMOVE_EXTERNAL_ENGINE = 38;
  FEATURE_ID_GET_SAN_MOVES = 39;
  FEATURE_ID_LOAD_COACH = 40;
  FEATURE_ID_SET_COACH = 41;
  FEATURE_ID_GAME_REVIEW = 42;
  FEATURE_ID_UNMAKE_MOVES = 43;
  FEATURE_ID_GET_CHESS960_INITIAL_POSITION = 44;
  FEATURE_ID_GET_COACH_CHAT = 45;
  FEATURE_ID_UPDATE_EXPERIMENTAL_OPTIONS = 46;
  FEATURE_ID_GET_COACH_HINT = 47;
  FEATURE_ID_LOAD_AND_SET_COACH = 48
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03614"></a>
## FND-03614: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_SET_COACH = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_SET_COACH = 41;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1488.

```text
RE_ID_REMOVE_EXTERNAL_ENGINE = 38;
  FEATURE_ID_GET_SAN_MOVES = 39;
  FEATURE_ID_LOAD_COACH = 40;
  FEATURE_ID_SET_COACH = 41;
  FEATURE_ID_GAME_REVIEW = 42;
  FEATURE_ID_UNMAKE_MOVES = 43;
  FEATURE_ID_GET_CHESS960_INITIAL_POSITION = 44;
  FEATURE_ID_GET_COACH_CHAT = 45;
  FEATURE_ID_UPDATE_EXPERIMENTAL_OPTIONS = 46;
  FEATURE_ID_GET_COACH_HINT = 47;
  FEATURE_ID_LOAD_AND_SET_COACH = 48;
  FEATURE_ID_SWITCH_SIDES = 
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03615"></a>
## FND-03615: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GAME_REVIEW = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GAME_REVIEW = 42;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1517.

```text
= 38;
  FEATURE_ID_GET_SAN_MOVES = 39;
  FEATURE_ID_LOAD_COACH = 40;
  FEATURE_ID_SET_COACH = 41;
  FEATURE_ID_GAME_REVIEW = 42;
  FEATURE_ID_UNMAKE_MOVES = 43;
  FEATURE_ID_GET_CHESS960_INITIAL_POSITION = 44;
  FEATURE_ID_GET_COACH_CHAT = 45;
  FEATURE_ID_UPDATE_EXPERIMENTAL_OPTIONS = 46;
  FEATURE_ID_GET_COACH_HINT = 47;
  FEATURE_ID_LOAD_AND_SET_COACH = 48;
  FEATURE_ID_SWITCH_SIDES = 49;
  FEATURE_ID_CONVERT_TO_P
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03616"></a>
## FND-03616: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_UNMAKE_MOVES = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_UNMAKE_MOVES = 43;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1548.

```text
S = 39;
  FEATURE_ID_LOAD_COACH = 40;
  FEATURE_ID_SET_COACH = 41;
  FEATURE_ID_GAME_REVIEW = 42;
  FEATURE_ID_UNMAKE_MOVES = 43;
  FEATURE_ID_GET_CHESS960_INITIAL_POSITION = 44;
  FEATURE_ID_GET_COACH_CHAT = 45;
  FEATURE_ID_UPDATE_EXPERIMENTAL_OPTIONS = 46;
  FEATURE_ID_GET_COACH_HINT = 47;
  FEATURE_ID_LOAD_AND_SET_COACH = 48;
  FEATURE_ID_SWITCH_SIDES = 49;
  FEATURE_ID_CONVERT_TO_PROTO_MOVES = 50;
  FEATURE_ID_R
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03617"></a>
## FND-03617: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_CHESS960_INITIAL_POSITION = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_CHESS960_INITIAL_POSITION = 44;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1580.

```text
= 40;
  FEATURE_ID_SET_COACH = 41;
  FEATURE_ID_GAME_REVIEW = 42;
  FEATURE_ID_UNMAKE_MOVES = 43;
  FEATURE_ID_GET_CHESS960_INITIAL_POSITION = 44;
  FEATURE_ID_GET_COACH_CHAT = 45;
  FEATURE_ID_UPDATE_EXPERIMENTAL_OPTIONS = 46;
  FEATURE_ID_GET_COACH_HINT = 47;
  FEATURE_ID_LOAD_AND_SET_COACH = 48;
  FEATURE_ID_SWITCH_SIDES = 49;
  FEATURE_ID_CONVERT_TO_PROTO_MOVES = 50;
  FEATURE_ID_RELAXED_LEGAL_MOVES = 51;
  FEATU
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03618"></a>
## FND-03618: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_COACH_CHAT = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_COACH_CHAT = 45;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1629.

```text
AME_REVIEW = 42;
  FEATURE_ID_UNMAKE_MOVES = 43;
  FEATURE_ID_GET_CHESS960_INITIAL_POSITION = 44;
  FEATURE_ID_GET_COACH_CHAT = 45;
  FEATURE_ID_UPDATE_EXPERIMENTAL_OPTIONS = 46;
  FEATURE_ID_GET_COACH_HINT = 47;
  FEATURE_ID_LOAD_AND_SET_COACH = 48;
  FEATURE_ID_SWITCH_SIDES = 49;
  FEATURE_ID_CONVERT_TO_PROTO_MOVES = 50;
  FEATURE_ID_RELAXED_LEGAL_MOVES = 51;
  FEATURE_ID_RELAXED_APPLY_MOVE = 52;
  FEATURE_ID_GET_N
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03619"></a>
## FND-03619: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_UPDATE_EXPERIMENTAL_OPTIONS = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_UPDATE_EXPERIMENTAL_OPTIONS = 46;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1663.

```text
KE_MOVES = 43;
  FEATURE_ID_GET_CHESS960_INITIAL_POSITION = 44;
  FEATURE_ID_GET_COACH_CHAT = 45;
  FEATURE_ID_UPDATE_EXPERIMENTAL_OPTIONS = 46;
  FEATURE_ID_GET_COACH_HINT = 47;
  FEATURE_ID_LOAD_AND_SET_COACH = 48;
  FEATURE_ID_SWITCH_SIDES = 49;
  FEATURE_ID_CONVERT_TO_PROTO_MOVES = 50;
  FEATURE_ID_RELAXED_LEGAL_MOVES = 51;
  FEATURE_ID_RELAXED_APPLY_MOVE = 52;
  FEATURE_ID_GET_NON_CHESS_TEXT = 53;
  FEATURE_ID_E
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03620"></a>
## FND-03620: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_COACH_HINT = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_COACH_HINT = 47;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1710.

```text
L_POSITION = 44;
  FEATURE_ID_GET_COACH_CHAT = 45;
  FEATURE_ID_UPDATE_EXPERIMENTAL_OPTIONS = 46;
  FEATURE_ID_GET_COACH_HINT = 47;
  FEATURE_ID_LOAD_AND_SET_COACH = 48;
  FEATURE_ID_SWITCH_SIDES = 49;
  FEATURE_ID_CONVERT_TO_PROTO_MOVES = 50;
  FEATURE_ID_RELAXED_LEGAL_MOVES = 51;
  FEATURE_ID_RELAXED_APPLY_MOVE = 52;
  FEATURE_ID_GET_NON_CHESS_TEXT = 53;
  FEATURE_ID_EVALUATE_GAME = 54;
  FEATURE_ID_RELAXED_CONVERT
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03621"></a>
## FND-03621: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_LOAD_AND_SET_COACH = 48

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_LOAD_AND_SET_COACH = 48;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1744.

```text
COACH_CHAT = 45;
  FEATURE_ID_UPDATE_EXPERIMENTAL_OPTIONS = 46;
  FEATURE_ID_GET_COACH_HINT = 47;
  FEATURE_ID_LOAD_AND_SET_COACH = 48;
  FEATURE_ID_SWITCH_SIDES = 49;
  FEATURE_ID_CONVERT_TO_PROTO_MOVES = 50;
  FEATURE_ID_RELAXED_LEGAL_MOVES = 51;
  FEATURE_ID_RELAXED_APPLY_MOVE = 52;
  FEATURE_ID_GET_NON_CHESS_TEXT = 53;
  FEATURE_ID_EVALUATE_GAME = 54;
  FEATURE_ID_RELAXED_CONVERT_TO_PROTO_MOVES = 55;
  FEATURE_ID
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03622"></a>
## FND-03622: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_SWITCH_SIDES = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_SWITCH_SIDES = 49;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1782.

```text
XPERIMENTAL_OPTIONS = 46;
  FEATURE_ID_GET_COACH_HINT = 47;
  FEATURE_ID_LOAD_AND_SET_COACH = 48;
  FEATURE_ID_SWITCH_SIDES = 49;
  FEATURE_ID_CONVERT_TO_PROTO_MOVES = 50;
  FEATURE_ID_RELAXED_LEGAL_MOVES = 51;
  FEATURE_ID_RELAXED_APPLY_MOVE = 52;
  FEATURE_ID_GET_NON_CHESS_TEXT = 53;
  FEATURE_ID_EVALUATE_GAME = 54;
  FEATURE_ID_RELAXED_CONVERT_TO_PROTO_MOVES = 55;
  FEATURE_ID_RESET_ENGINE_STATE = 56;
  FEATURE_ID
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03623"></a>
## FND-03623: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_CONVERT_TO_PROTO_MOVES = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_CONVERT_TO_PROTO_MOVES = 50;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1814.

```text
URE_ID_GET_COACH_HINT = 47;
  FEATURE_ID_LOAD_AND_SET_COACH = 48;
  FEATURE_ID_SWITCH_SIDES = 49;
  FEATURE_ID_CONVERT_TO_PROTO_MOVES = 50;
  FEATURE_ID_RELAXED_LEGAL_MOVES = 51;
  FEATURE_ID_RELAXED_APPLY_MOVE = 52;
  FEATURE_ID_GET_NON_CHESS_TEXT = 53;
  FEATURE_ID_EVALUATE_GAME = 54;
  FEATURE_ID_RELAXED_CONVERT_TO_PROTO_MOVES = 55;
  FEATURE_ID_RESET_ENGINE_STATE = 56;
  FEATURE_ID_CONVERT_FROM_PROTO_MOVES = 57;

```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03624"></a>
## FND-03624: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_RELAXED_LEGAL_MOVES = 51

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_RELAXED_LEGAL_MOVES = 51;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1856.

```text
OAD_AND_SET_COACH = 48;
  FEATURE_ID_SWITCH_SIDES = 49;
  FEATURE_ID_CONVERT_TO_PROTO_MOVES = 50;
  FEATURE_ID_RELAXED_LEGAL_MOVES = 51;
  FEATURE_ID_RELAXED_APPLY_MOVE = 52;
  FEATURE_ID_GET_NON_CHESS_TEXT = 53;
  FEATURE_ID_EVALUATE_GAME = 54;
  FEATURE_ID_RELAXED_CONVERT_TO_PROTO_MOVES = 55;
  FEATURE_ID_RESET_ENGINE_STATE = 56;
  FEATURE_ID_CONVERT_FROM_PROTO_MOVES = 57;
  FEATURE_ID_FORCE_CRASH = 58;
  FEATURE_I
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03625"></a>
## FND-03625: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_RELAXED_APPLY_MOVE = 52

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_RELAXED_APPLY_MOVE = 52;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1895.

```text
ITCH_SIDES = 49;
  FEATURE_ID_CONVERT_TO_PROTO_MOVES = 50;
  FEATURE_ID_RELAXED_LEGAL_MOVES = 51;
  FEATURE_ID_RELAXED_APPLY_MOVE = 52;
  FEATURE_ID_GET_NON_CHESS_TEXT = 53;
  FEATURE_ID_EVALUATE_GAME = 54;
  FEATURE_ID_RELAXED_CONVERT_TO_PROTO_MOVES = 55;
  FEATURE_ID_RESET_ENGINE_STATE = 56;
  FEATURE_ID_CONVERT_FROM_PROTO_MOVES = 57;
  FEATURE_ID_FORCE_CRASH = 58;
  FEATURE_ID_GET_PGN_MOVE_ANNOTATIONS = 59;
  FEAT
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03626"></a>
## FND-03626: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_NON_CHESS_TEXT = 53

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_NON_CHESS_TEXT = 53;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1933.

```text
TO_PROTO_MOVES = 50;
  FEATURE_ID_RELAXED_LEGAL_MOVES = 51;
  FEATURE_ID_RELAXED_APPLY_MOVE = 52;
  FEATURE_ID_GET_NON_CHESS_TEXT = 53;
  FEATURE_ID_EVALUATE_GAME = 54;
  FEATURE_ID_RELAXED_CONVERT_TO_PROTO_MOVES = 55;
  FEATURE_ID_RESET_ENGINE_STATE = 56;
  FEATURE_ID_CONVERT_FROM_PROTO_MOVES = 57;
  FEATURE_ID_FORCE_CRASH = 58;
  FEATURE_ID_GET_PGN_MOVE_ANNOTATIONS = 59;
  FEATURE_ID_VALIDATE_GAME_FOR_ANALYSIS = 60
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03627"></a>
## FND-03627: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_EVALUATE_GAME = 54

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_EVALUATE_GAME = 54;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 1971.

```text
XED_LEGAL_MOVES = 51;
  FEATURE_ID_RELAXED_APPLY_MOVE = 52;
  FEATURE_ID_GET_NON_CHESS_TEXT = 53;
  FEATURE_ID_EVALUATE_GAME = 54;
  FEATURE_ID_RELAXED_CONVERT_TO_PROTO_MOVES = 55;
  FEATURE_ID_RESET_ENGINE_STATE = 56;
  FEATURE_ID_CONVERT_FROM_PROTO_MOVES = 57;
  FEATURE_ID_FORCE_CRASH = 58;
  FEATURE_ID_GET_PGN_MOVE_ANNOTATIONS = 59;
  FEATURE_ID_VALIDATE_GAME_FOR_ANALYSIS = 60;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG = 
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03628"></a>
## FND-03628: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_RELAXED_CONVERT_TO_PROTO_MOVES = 55

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_RELAXED_CONVERT_TO_PROTO_MOVES = 55;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2004.

```text
D_RELAXED_APPLY_MOVE = 52;
  FEATURE_ID_GET_NON_CHESS_TEXT = 53;
  FEATURE_ID_EVALUATE_GAME = 54;
  FEATURE_ID_RELAXED_CONVERT_TO_PROTO_MOVES = 55;
  FEATURE_ID_RESET_ENGINE_STATE = 56;
  FEATURE_ID_CONVERT_FROM_PROTO_MOVES = 57;
  FEATURE_ID_FORCE_CRASH = 58;
  FEATURE_ID_GET_PGN_MOVE_ANNOTATIONS = 59;
  FEATURE_ID_VALIDATE_GAME_FOR_ANALYSIS = 60;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG = 61;
  FEATURE_ID_LOAD_CHARM_MODEL
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03629"></a>
## FND-03629: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_RESET_ENGINE_STATE = 56

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_RESET_ENGINE_STATE = 56;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2054.

```text
ESS_TEXT = 53;
  FEATURE_ID_EVALUATE_GAME = 54;
  FEATURE_ID_RELAXED_CONVERT_TO_PROTO_MOVES = 55;
  FEATURE_ID_RESET_ENGINE_STATE = 56;
  FEATURE_ID_CONVERT_FROM_PROTO_MOVES = 57;
  FEATURE_ID_FORCE_CRASH = 58;
  FEATURE_ID_GET_PGN_MOVE_ANNOTATIONS = 59;
  FEATURE_ID_VALIDATE_GAME_FOR_ANALYSIS = 60;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG = 61;
  FEATURE_ID_LOAD_CHARM_MODEL = 62;
  FEATURE_ID_VALIDATE_PGN = 63;
  FEATURE_I
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03630"></a>
## FND-03630: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_CONVERT_FROM_PROTO_MOVES = 57

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_CONVERT_FROM_PROTO_MOVES = 57;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2092.

```text
AME = 54;
  FEATURE_ID_RELAXED_CONVERT_TO_PROTO_MOVES = 55;
  FEATURE_ID_RESET_ENGINE_STATE = 56;
  FEATURE_ID_CONVERT_FROM_PROTO_MOVES = 57;
  FEATURE_ID_FORCE_CRASH = 58;
  FEATURE_ID_GET_PGN_MOVE_ANNOTATIONS = 59;
  FEATURE_ID_VALIDATE_GAME_FOR_ANALYSIS = 60;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG = 61;
  FEATURE_ID_LOAD_CHARM_MODEL = 62;
  FEATURE_ID_VALIDATE_PGN = 63;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG_V2 = 64;
  FEAT
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03631"></a>
## FND-03631: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_FORCE_CRASH = 58

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_FORCE_CRASH = 58;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2136.

```text
OTO_MOVES = 55;
  FEATURE_ID_RESET_ENGINE_STATE = 56;
  FEATURE_ID_CONVERT_FROM_PROTO_MOVES = 57;
  FEATURE_ID_FORCE_CRASH = 58;
  FEATURE_ID_GET_PGN_MOVE_ANNOTATIONS = 59;
  FEATURE_ID_VALIDATE_GAME_FOR_ANALYSIS = 60;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG = 61;
  FEATURE_ID_LOAD_CHARM_MODEL = 62;
  FEATURE_ID_VALIDATE_PGN = 63;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG_V2 = 64;
  FEATURE_ID_EDIT_PGN_MOVE_ANNOTATION = 65;
  FEAT
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03632"></a>
## FND-03632: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_PGN_MOVE_ANNOTATIONS = 59

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_PGN_MOVE_ANNOTATIONS = 59;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2167.

```text
SET_ENGINE_STATE = 56;
  FEATURE_ID_CONVERT_FROM_PROTO_MOVES = 57;
  FEATURE_ID_FORCE_CRASH = 58;
  FEATURE_ID_GET_PGN_MOVE_ANNOTATIONS = 59;
  FEATURE_ID_VALIDATE_GAME_FOR_ANALYSIS = 60;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG = 61;
  FEATURE_ID_LOAD_CHARM_MODEL = 62;
  FEATURE_ID_VALIDATE_PGN = 63;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG_V2 = 64;
  FEATURE_ID_EDIT_PGN_MOVE_ANNOTATION = 65;
  FEATURE_ID_EDIT_PGN_NAGS = 66;
  FE
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03633"></a>
## FND-03633: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_VALIDATE_GAME_FOR_ANALYSIS = 60

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_VALIDATE_GAME_FOR_ANALYSIS = 60;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2211.

```text
FROM_PROTO_MOVES = 57;
  FEATURE_ID_FORCE_CRASH = 58;
  FEATURE_ID_GET_PGN_MOVE_ANNOTATIONS = 59;
  FEATURE_ID_VALIDATE_GAME_FOR_ANALYSIS = 60;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG = 61;
  FEATURE_ID_LOAD_CHARM_MODEL = 62;
  FEATURE_ID_VALIDATE_PGN = 63;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG_V2 = 64;
  FEATURE_ID_EDIT_PGN_MOVE_ANNOTATION = 65;
  FEATURE_ID_EDIT_PGN_NAGS = 66;
  FEATURE_ID_SET_PGN_HEADERS = 67;
  FEATURE_ID_
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03634"></a>
## FND-03634: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_BOT_MOVE_FROM_CONFIG = 61

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_BOT_MOVE_FROM_CONFIG = 61;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2257.

```text
H = 58;
  FEATURE_ID_GET_PGN_MOVE_ANNOTATIONS = 59;
  FEATURE_ID_VALIDATE_GAME_FOR_ANALYSIS = 60;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG = 61;
  FEATURE_ID_LOAD_CHARM_MODEL = 62;
  FEATURE_ID_VALIDATE_PGN = 63;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG_V2 = 64;
  FEATURE_ID_EDIT_PGN_MOVE_ANNOTATION = 65;
  FEATURE_ID_EDIT_PGN_NAGS = 66;
  FEATURE_ID_SET_PGN_HEADERS = 67;
  FEATURE_ID_CHARM_INFERENCE = 68;
  FEATURE_ID_ADD_CHARM_I
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03635"></a>
## FND-03635: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_LOAD_CHARM_MODEL = 62

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_LOAD_CHARM_MODEL = 62;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2297.

```text
TIONS = 59;
  FEATURE_ID_VALIDATE_GAME_FOR_ANALYSIS = 60;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG = 61;
  FEATURE_ID_LOAD_CHARM_MODEL = 62;
  FEATURE_ID_VALIDATE_PGN = 63;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG_V2 = 64;
  FEATURE_ID_EDIT_PGN_MOVE_ANNOTATION = 65;
  FEATURE_ID_EDIT_PGN_NAGS = 66;
  FEATURE_ID_SET_PGN_HEADERS = 67;
  FEATURE_ID_CHARM_INFERENCE = 68;
  FEATURE_ID_ADD_CHARM_INFERENCE = 69;
  FEATURE_ID_BOT_CONFIG_R
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03636"></a>
## FND-03636: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_VALIDATE_PGN = 63

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_VALIDATE_PGN = 63;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2333.

```text
ME_FOR_ANALYSIS = 60;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG = 61;
  FEATURE_ID_LOAD_CHARM_MODEL = 62;
  FEATURE_ID_VALIDATE_PGN = 63;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG_V2 = 64;
  FEATURE_ID_EDIT_PGN_MOVE_ANNOTATION = 65;
  FEATURE_ID_EDIT_PGN_NAGS = 66;
  FEATURE_ID_SET_PGN_HEADERS = 67;
  FEATURE_ID_CHARM_INFERENCE = 68;
  FEATURE_ID_ADD_CHARM_INFERENCE = 69;
  FEATURE_ID_BOT_CONFIG_RESOURCES = 70;
  FEATURE_ID_SET_PLAY
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03637"></a>
## FND-03637: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_BOT_MOVE_FROM_CONFIG_V2 = 64

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_BOT_MOVE_FROM_CONFIG_V2 = 64;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2365.

```text
ID_BOT_MOVE_FROM_CONFIG = 61;
  FEATURE_ID_LOAD_CHARM_MODEL = 62;
  FEATURE_ID_VALIDATE_PGN = 63;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG_V2 = 64;
  FEATURE_ID_EDIT_PGN_MOVE_ANNOTATION = 65;
  FEATURE_ID_EDIT_PGN_NAGS = 66;
  FEATURE_ID_SET_PGN_HEADERS = 67;
  FEATURE_ID_CHARM_INFERENCE = 68;
  FEATURE_ID_ADD_CHARM_INFERENCE = 69;
  FEATURE_ID_BOT_CONFIG_RESOURCES = 70;
  FEATURE_ID_SET_PLAYED_LINE = 71;
  FEATURE_ID_GENER
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03638"></a>
## FND-03638: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_EDIT_PGN_MOVE_ANNOTATION = 65

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_EDIT_PGN_MOVE_ANNOTATION = 65;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2408.

```text
LOAD_CHARM_MODEL = 62;
  FEATURE_ID_VALIDATE_PGN = 63;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG_V2 = 64;
  FEATURE_ID_EDIT_PGN_MOVE_ANNOTATION = 65;
  FEATURE_ID_EDIT_PGN_NAGS = 66;
  FEATURE_ID_SET_PGN_HEADERS = 67;
  FEATURE_ID_CHARM_INFERENCE = 68;
  FEATURE_ID_ADD_CHARM_INFERENCE = 69;
  FEATURE_ID_BOT_CONFIG_RESOURCES = 70;
  FEATURE_ID_SET_PLAYED_LINE = 71;
  FEATURE_ID_GENERATE_UUID_V1 = 72;
  FEATURE_ID_GET_ILLEGAL_
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03639"></a>
## FND-03639: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_EDIT_PGN_NAGS = 66

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_EDIT_PGN_NAGS = 66;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2452.

```text
_PGN = 63;
  FEATURE_ID_BOT_MOVE_FROM_CONFIG_V2 = 64;
  FEATURE_ID_EDIT_PGN_MOVE_ANNOTATION = 65;
  FEATURE_ID_EDIT_PGN_NAGS = 66;
  FEATURE_ID_SET_PGN_HEADERS = 67;
  FEATURE_ID_CHARM_INFERENCE = 68;
  FEATURE_ID_ADD_CHARM_INFERENCE = 69;
  FEATURE_ID_BOT_CONFIG_RESOURCES = 70;
  FEATURE_ID_SET_PLAYED_LINE = 71;
  FEATURE_ID_GENERATE_UUID_V1 = 72;
  FEATURE_ID_GET_ILLEGAL_MOVE_EXPLANATION = 73;
  FEATURE_ID_ANALYSIS
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03640"></a>
## FND-03640: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_SET_PGN_HEADERS = 67

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_SET_PGN_HEADERS = 67;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2485.

```text
FROM_CONFIG_V2 = 64;
  FEATURE_ID_EDIT_PGN_MOVE_ANNOTATION = 65;
  FEATURE_ID_EDIT_PGN_NAGS = 66;
  FEATURE_ID_SET_PGN_HEADERS = 67;
  FEATURE_ID_CHARM_INFERENCE = 68;
  FEATURE_ID_ADD_CHARM_INFERENCE = 69;
  FEATURE_ID_BOT_CONFIG_RESOURCES = 70;
  FEATURE_ID_SET_PLAYED_LINE = 71;
  FEATURE_ID_GENERATE_UUID_V1 = 72;
  FEATURE_ID_GET_ILLEGAL_MOVE_EXPLANATION = 73;
  FEATURE_ID_ANALYSIS_ANNOTATIONS = 74;
  FEATURE_ID_D
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03641"></a>
## FND-03641: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_CHARM_INFERENCE = 68

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_CHARM_INFERENCE = 68;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2520.

```text
DIT_PGN_MOVE_ANNOTATION = 65;
  FEATURE_ID_EDIT_PGN_NAGS = 66;
  FEATURE_ID_SET_PGN_HEADERS = 67;
  FEATURE_ID_CHARM_INFERENCE = 68;
  FEATURE_ID_ADD_CHARM_INFERENCE = 69;
  FEATURE_ID_BOT_CONFIG_RESOURCES = 70;
  FEATURE_ID_SET_PLAYED_LINE = 71;
  FEATURE_ID_GENERATE_UUID_V1 = 72;
  FEATURE_ID_GET_ILLEGAL_MOVE_EXPLANATION = 73;
  FEATURE_ID_ANALYSIS_ANNOTATIONS = 74;
  FEATURE_ID_DELETE_PGN_MOVE = 75;
  FEATURE_ID_G
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03642"></a>
## FND-03642: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_ADD_CHARM_INFERENCE = 69

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_ADD_CHARM_INFERENCE = 69;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2555.

```text
TURE_ID_EDIT_PGN_NAGS = 66;
  FEATURE_ID_SET_PGN_HEADERS = 67;
  FEATURE_ID_CHARM_INFERENCE = 68;
  FEATURE_ID_ADD_CHARM_INFERENCE = 69;
  FEATURE_ID_BOT_CONFIG_RESOURCES = 70;
  FEATURE_ID_SET_PLAYED_LINE = 71;
  FEATURE_ID_GENERATE_UUID_V1 = 72;
  FEATURE_ID_GET_ILLEGAL_MOVE_EXPLANATION = 73;
  FEATURE_ID_ANALYSIS_ANNOTATIONS = 74;
  FEATURE_ID_DELETE_PGN_MOVE = 75;
  FEATURE_ID_GENERATE_TRAIN_ITEM_GOAL_SPEECH = 76
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03643"></a>
## FND-03643: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_BOT_CONFIG_RESOURCES = 70

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_BOT_CONFIG_RESOURCES = 70;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2594.

```text
D_SET_PGN_HEADERS = 67;
  FEATURE_ID_CHARM_INFERENCE = 68;
  FEATURE_ID_ADD_CHARM_INFERENCE = 69;
  FEATURE_ID_BOT_CONFIG_RESOURCES = 70;
  FEATURE_ID_SET_PLAYED_LINE = 71;
  FEATURE_ID_GENERATE_UUID_V1 = 72;
  FEATURE_ID_GET_ILLEGAL_MOVE_EXPLANATION = 73;
  FEATURE_ID_ANALYSIS_ANNOTATIONS = 74;
  FEATURE_ID_DELETE_PGN_MOVE = 75;
  FEATURE_ID_GENERATE_TRAIN_ITEM_GOAL_SPEECH = 76;
  FEATURE_ID_GRADE_TRAIN_ITEM_MOVE = 
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03644"></a>
## FND-03644: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_SET_PLAYED_LINE = 71

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_SET_PLAYED_LINE = 71;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2634.

```text
RM_INFERENCE = 68;
  FEATURE_ID_ADD_CHARM_INFERENCE = 69;
  FEATURE_ID_BOT_CONFIG_RESOURCES = 70;
  FEATURE_ID_SET_PLAYED_LINE = 71;
  FEATURE_ID_GENERATE_UUID_V1 = 72;
  FEATURE_ID_GET_ILLEGAL_MOVE_EXPLANATION = 73;
  FEATURE_ID_ANALYSIS_ANNOTATIONS = 74;
  FEATURE_ID_DELETE_PGN_MOVE = 75;
  FEATURE_ID_GENERATE_TRAIN_ITEM_GOAL_SPEECH = 76;
  FEATURE_ID_GRADE_TRAIN_ITEM_MOVE = 77;
  FEATURE_ID_BOT_CONFIG_RESOURCES_V2
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03645"></a>
## FND-03645: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GENERATE_UUID_V1 = 72

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GENERATE_UUID_V1 = 72;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2669.

```text
_CHARM_INFERENCE = 69;
  FEATURE_ID_BOT_CONFIG_RESOURCES = 70;
  FEATURE_ID_SET_PLAYED_LINE = 71;
  FEATURE_ID_GENERATE_UUID_V1 = 72;
  FEATURE_ID_GET_ILLEGAL_MOVE_EXPLANATION = 73;
  FEATURE_ID_ANALYSIS_ANNOTATIONS = 74;
  FEATURE_ID_DELETE_PGN_MOVE = 75;
  FEATURE_ID_GENERATE_TRAIN_ITEM_GOAL_SPEECH = 76;
  FEATURE_ID_GRADE_TRAIN_ITEM_MOVE = 77;
  FEATURE_ID_BOT_CONFIG_RESOURCES_V2 = 78;
  FEATURE_ID_GET_GAME_REVIEW
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03646"></a>
## FND-03646: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_ILLEGAL_MOVE_EXPLANATION = 73

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_ILLEGAL_MOVE_EXPLANATION = 73;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2705.

```text
BOT_CONFIG_RESOURCES = 70;
  FEATURE_ID_SET_PLAYED_LINE = 71;
  FEATURE_ID_GENERATE_UUID_V1 = 72;
  FEATURE_ID_GET_ILLEGAL_MOVE_EXPLANATION = 73;
  FEATURE_ID_ANALYSIS_ANNOTATIONS = 74;
  FEATURE_ID_DELETE_PGN_MOVE = 75;
  FEATURE_ID_GENERATE_TRAIN_ITEM_GOAL_SPEECH = 76;
  FEATURE_ID_GRADE_TRAIN_ITEM_MOVE = 77;
  FEATURE_ID_BOT_CONFIG_RESOURCES_V2 = 78;
  FEATURE_ID_GET_GAME_REVIEW_EVALUATIONS = 79;
  FEATURE_ID_LOAD
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03647"></a>
## FND-03647: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_ANALYSIS_ANNOTATIONS = 74

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_ANALYSIS_ANNOTATIONS = 74;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2753.

```text
ED_LINE = 71;
  FEATURE_ID_GENERATE_UUID_V1 = 72;
  FEATURE_ID_GET_ILLEGAL_MOVE_EXPLANATION = 73;
  FEATURE_ID_ANALYSIS_ANNOTATIONS = 74;
  FEATURE_ID_DELETE_PGN_MOVE = 75;
  FEATURE_ID_GENERATE_TRAIN_ITEM_GOAL_SPEECH = 76;
  FEATURE_ID_GRADE_TRAIN_ITEM_MOVE = 77;
  FEATURE_ID_BOT_CONFIG_RESOURCES_V2 = 78;
  FEATURE_ID_GET_GAME_REVIEW_EVALUATIONS = 79;
  FEATURE_ID_LOAD_ECO_BOOK = 80;
  FEATURE_ID_INTERNAL_FEATURES =
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03648"></a>
## FND-03648: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_DELETE_PGN_MOVE = 75

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_DELETE_PGN_MOVE = 75;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2793.

```text
_V1 = 72;
  FEATURE_ID_GET_ILLEGAL_MOVE_EXPLANATION = 73;
  FEATURE_ID_ANALYSIS_ANNOTATIONS = 74;
  FEATURE_ID_DELETE_PGN_MOVE = 75;
  FEATURE_ID_GENERATE_TRAIN_ITEM_GOAL_SPEECH = 76;
  FEATURE_ID_GRADE_TRAIN_ITEM_MOVE = 77;
  FEATURE_ID_BOT_CONFIG_RESOURCES_V2 = 78;
  FEATURE_ID_GET_GAME_REVIEW_EVALUATIONS = 79;
  FEATURE_ID_LOAD_ECO_BOOK = 80;
  FEATURE_ID_INTERNAL_FEATURES = 255;
  FEATURE_ID_INTERNAL_FEATURE_POSI
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03649"></a>
## FND-03649: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GENERATE_TRAIN_ITEM_GOAL_SPEECH = 76

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GENERATE_TRAIN_ITEM_GOAL_SPEECH = 76;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2828.

```text
MOVE_EXPLANATION = 73;
  FEATURE_ID_ANALYSIS_ANNOTATIONS = 74;
  FEATURE_ID_DELETE_PGN_MOVE = 75;
  FEATURE_ID_GENERATE_TRAIN_ITEM_GOAL_SPEECH = 76;
  FEATURE_ID_GRADE_TRAIN_ITEM_MOVE = 77;
  FEATURE_ID_BOT_CONFIG_RESOURCES_V2 = 78;
  FEATURE_ID_GET_GAME_REVIEW_EVALUATIONS = 79;
  FEATURE_ID_LOAD_ECO_BOOK = 80;
  FEATURE_ID_INTERNAL_FEATURES = 255;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_FEATURES = 258;
  F
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03650"></a>
## FND-03650: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GRADE_TRAIN_ITEM_MOVE = 77

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GRADE_TRAIN_ITEM_MOVE = 77;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2879.

```text
TIONS = 74;
  FEATURE_ID_DELETE_PGN_MOVE = 75;
  FEATURE_ID_GENERATE_TRAIN_ITEM_GOAL_SPEECH = 76;
  FEATURE_ID_GRADE_TRAIN_ITEM_MOVE = 77;
  FEATURE_ID_BOT_CONFIG_RESOURCES_V2 = 78;
  FEATURE_ID_GET_GAME_REVIEW_EVALUATIONS = 79;
  FEATURE_ID_LOAD_ECO_BOOK = 80;
  FEATURE_ID_INTERNAL_FEATURES = 255;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_FEATURES = 258;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_LABE
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03651"></a>
## FND-03651: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_BOT_CONFIG_RESOURCES_V2 = 78

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_BOT_CONFIG_RESOURCES_V2 = 78;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2920.

```text
= 75;
  FEATURE_ID_GENERATE_TRAIN_ITEM_GOAL_SPEECH = 76;
  FEATURE_ID_GRADE_TRAIN_ITEM_MOVE = 77;
  FEATURE_ID_BOT_CONFIG_RESOURCES_V2 = 78;
  FEATURE_ID_GET_GAME_REVIEW_EVALUATIONS = 79;
  FEATURE_ID_LOAD_ECO_BOOK = 80;
  FEATURE_ID_INTERNAL_FEATURES = 255;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_FEATURES = 258;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_LABELS = 259;
  FEATURE_ID_INTERNAL_FEATURE_P
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03652"></a>
## FND-03652: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_GET_GAME_REVIEW_EVALUATIONS = 79

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_GET_GAME_REVIEW_EVALUATIONS = 79;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 2963.

```text
_SPEECH = 76;
  FEATURE_ID_GRADE_TRAIN_ITEM_MOVE = 77;
  FEATURE_ID_BOT_CONFIG_RESOURCES_V2 = 78;
  FEATURE_ID_GET_GAME_REVIEW_EVALUATIONS = 79;
  FEATURE_ID_LOAD_ECO_BOOK = 80;
  FEATURE_ID_INTERNAL_FEATURES = 255;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_FEATURES = 258;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_LABELS = 259;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_PREDICTIONS = 260;
  FEA
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03653"></a>
## FND-03653: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_LOAD_ECO_BOOK = 80

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_LOAD_ECO_BOOK = 80;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3010.

```text
E = 77;
  FEATURE_ID_BOT_CONFIG_RESOURCES_V2 = 78;
  FEATURE_ID_GET_GAME_REVIEW_EVALUATIONS = 79;
  FEATURE_ID_LOAD_ECO_BOOK = 80;
  FEATURE_ID_INTERNAL_FEATURES = 255;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_FEATURES = 258;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_LABELS = 259;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_PREDICTIONS = 260;
  FEATURE_ID_INTERNAL_FEATURE_GAME_ANALYSIS_JSON = 2
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03654"></a>
## FND-03654: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURES = 255

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURES = 255;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3043.

```text
ESOURCES_V2 = 78;
  FEATURE_ID_GET_GAME_REVIEW_EVALUATIONS = 79;
  FEATURE_ID_LOAD_ECO_BOOK = 80;
  FEATURE_ID_INTERNAL_FEATURES = 255;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_FEATURES = 258;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_LABELS = 259;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_PREDICTIONS = 260;
  FEATURE_ID_INTERNAL_FEATURE_GAME_ANALYSIS_JSON = 261;
  FEATURE_ID_INTERNAL_FEATURE
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03655"></a>
## FND-03655: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_FEATURES = 258

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_FEATURES = 258;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3081.

```text
E_REVIEW_EVALUATIONS = 79;
  FEATURE_ID_LOAD_ECO_BOOK = 80;
  FEATURE_ID_INTERNAL_FEATURES = 255;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_FEATURES = 258;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_LABELS = 259;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_PREDICTIONS = 260;
  FEATURE_ID_INTERNAL_FEATURE_GAME_ANALYSIS_JSON = 261;
  FEATURE_ID_INTERNAL_FEATURE_BOARD_EVENTS = 262;
  FEATURE_ID_INTE
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03656"></a>
## FND-03656: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_LABELS = 259

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_LABELS = 259;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3147.

```text
URE_ID_INTERNAL_FEATURES = 255;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_FEATURES = 258;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_LABELS = 259;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_PREDICTIONS = 260;
  FEATURE_ID_INTERNAL_FEATURE_GAME_ANALYSIS_JSON = 261;
  FEATURE_ID_INTERNAL_FEATURE_BOARD_EVENTS = 262;
  FEATURE_ID_INTERNAL_FEATURE_UCI_TO_GAME_STATE = 263;
  FEATURE_ID_INTERNAL_FEATUR
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03657"></a>
## FND-03657: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_PREDICTIONS = 260

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_PREDICTIONS = 260;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3211.

```text
SITION_DIFFICULTY_FEATURES = 258;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_LABELS = 259;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_PREDICTIONS = 260;
  FEATURE_ID_INTERNAL_FEATURE_GAME_ANALYSIS_JSON = 261;
  FEATURE_ID_INTERNAL_FEATURE_BOARD_EVENTS = 262;
  FEATURE_ID_INTERNAL_FEATURE_UCI_TO_GAME_STATE = 263;
  FEATURE_ID_INTERNAL_FEATURE_NEW_GAME = 264;
  FEATURE_ID_INTERNAL_FEATURE_DEBUG_INFO = 265
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03658"></a>
## FND-03658: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_GAME_ANALYSIS_JSON = 261

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_GAME_ANALYSIS_JSON = 261;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3280.

```text
ION_DIFFICULTY_LABELS = 259;
  FEATURE_ID_INTERNAL_FEATURE_POSITION_DIFFICULTY_PREDICTIONS = 260;
  FEATURE_ID_INTERNAL_FEATURE_GAME_ANALYSIS_JSON = 261;
  FEATURE_ID_INTERNAL_FEATURE_BOARD_EVENTS = 262;
  FEATURE_ID_INTERNAL_FEATURE_UCI_TO_GAME_STATE = 263;
  FEATURE_ID_INTERNAL_FEATURE_NEW_GAME = 264;
  FEATURE_ID_INTERNAL_FEATURE_DEBUG_INFO = 265;
  FEATURE_ID_INTERNAL_FEATURE_PUZZLE_GEN = 266;
  FEATURE_ID_INTERN
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03659"></a>
## FND-03659: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_BOARD_EVENTS = 262

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_BOARD_EVENTS = 262;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3336.

```text
RE_POSITION_DIFFICULTY_PREDICTIONS = 260;
  FEATURE_ID_INTERNAL_FEATURE_GAME_ANALYSIS_JSON = 261;
  FEATURE_ID_INTERNAL_FEATURE_BOARD_EVENTS = 262;
  FEATURE_ID_INTERNAL_FEATURE_UCI_TO_GAME_STATE = 263;
  FEATURE_ID_INTERNAL_FEATURE_NEW_GAME = 264;
  FEATURE_ID_INTERNAL_FEATURE_DEBUG_INFO = 265;
  FEATURE_ID_INTERNAL_FEATURE_PUZZLE_GEN = 266;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_PVTREE = 267;
  FEATURE_ID_INTERNAL_
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03660"></a>
## FND-03660: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_UCI_TO_GAME_STATE = 263

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_UCI_TO_GAME_STATE = 263;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3386.

```text
E_ID_INTERNAL_FEATURE_GAME_ANALYSIS_JSON = 261;
  FEATURE_ID_INTERNAL_FEATURE_BOARD_EVENTS = 262;
  FEATURE_ID_INTERNAL_FEATURE_UCI_TO_GAME_STATE = 263;
  FEATURE_ID_INTERNAL_FEATURE_NEW_GAME = 264;
  FEATURE_ID_INTERNAL_FEATURE_DEBUG_INFO = 265;
  FEATURE_ID_INTERNAL_FEATURE_PUZZLE_GEN = 266;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_PVTREE = 267;
  FEATURE_ID_INTERNAL_FEATURE_EXTRACT_PVLINE = 268;
  FEATURE_ID_INTERNA
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03661"></a>
## FND-03661: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_NEW_GAME = 264

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_NEW_GAME = 264;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3441.

```text
RE_ID_INTERNAL_FEATURE_BOARD_EVENTS = 262;
  FEATURE_ID_INTERNAL_FEATURE_UCI_TO_GAME_STATE = 263;
  FEATURE_ID_INTERNAL_FEATURE_NEW_GAME = 264;
  FEATURE_ID_INTERNAL_FEATURE_DEBUG_INFO = 265;
  FEATURE_ID_INTERNAL_FEATURE_PUZZLE_GEN = 266;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_PVTREE = 267;
  FEATURE_ID_INTERNAL_FEATURE_EXTRACT_PVLINE = 268;
  FEATURE_ID_INTERNAL_FEATURE_ADVANCED_STATS_DATAPOINT = 269;
  FEATURE_ID_
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03662"></a>
## FND-03662: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_DEBUG_INFO = 265

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_DEBUG_INFO = 265;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3487.

```text
EATURE_ID_INTERNAL_FEATURE_UCI_TO_GAME_STATE = 263;
  FEATURE_ID_INTERNAL_FEATURE_NEW_GAME = 264;
  FEATURE_ID_INTERNAL_FEATURE_DEBUG_INFO = 265;
  FEATURE_ID_INTERNAL_FEATURE_PUZZLE_GEN = 266;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_PVTREE = 267;
  FEATURE_ID_INTERNAL_FEATURE_EXTRACT_PVLINE = 268;
  FEATURE_ID_INTERNAL_FEATURE_ADVANCED_STATS_DATAPOINT = 269;
  FEATURE_ID_INTERNAL_FEATURE_COMPRESS_DATA = 270;
  FEATUR
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03663"></a>
## FND-03663: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_PUZZLE_GEN = 266

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_PUZZLE_GEN = 266;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3535.

```text
63;
  FEATURE_ID_INTERNAL_FEATURE_NEW_GAME = 264;
  FEATURE_ID_INTERNAL_FEATURE_DEBUG_INFO = 265;
  FEATURE_ID_INTERNAL_FEATURE_PUZZLE_GEN = 266;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_PVTREE = 267;
  FEATURE_ID_INTERNAL_FEATURE_EXTRACT_PVLINE = 268;
  FEATURE_ID_INTERNAL_FEATURE_ADVANCED_STATS_DATAPOINT = 269;
  FEATURE_ID_INTERNAL_FEATURE_COMPRESS_DATA = 270;
  FEATURE_ID_INTERNAL_FEATURE_RUN_SEARCH = 271;
  FEATUR
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03664"></a>
## FND-03664: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_GENERATE_PVTREE = 267

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_GENERATE_PVTREE = 267;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3583.

```text
;
  FEATURE_ID_INTERNAL_FEATURE_DEBUG_INFO = 265;
  FEATURE_ID_INTERNAL_FEATURE_PUZZLE_GEN = 266;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_PVTREE = 267;
  FEATURE_ID_INTERNAL_FEATURE_EXTRACT_PVLINE = 268;
  FEATURE_ID_INTERNAL_FEATURE_ADVANCED_STATS_DATAPOINT = 269;
  FEATURE_ID_INTERNAL_FEATURE_COMPRESS_DATA = 270;
  FEATURE_ID_INTERNAL_FEATURE_RUN_SEARCH = 271;
  FEATURE_ID_INTERNAL_FEATURE_ENABLE_TEST_MODE = 272;
  
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03665"></a>
## FND-03665: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_EXTRACT_PVLINE = 268

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_EXTRACT_PVLINE = 268;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3636.

```text
EATURE_ID_INTERNAL_FEATURE_PUZZLE_GEN = 266;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_PVTREE = 267;
  FEATURE_ID_INTERNAL_FEATURE_EXTRACT_PVLINE = 268;
  FEATURE_ID_INTERNAL_FEATURE_ADVANCED_STATS_DATAPOINT = 269;
  FEATURE_ID_INTERNAL_FEATURE_COMPRESS_DATA = 270;
  FEATURE_ID_INTERNAL_FEATURE_RUN_SEARCH = 271;
  FEATURE_ID_INTERNAL_FEATURE_ENABLE_TEST_MODE = 272;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_COACH_TEXT_ASSET
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03666"></a>
## FND-03666: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_ADVANCED_STATS_DATAPOINT = 269

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_ADVANCED_STATS_DATAPOINT = 269;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3688.

```text
RE_ID_INTERNAL_FEATURE_GENERATE_PVTREE = 267;
  FEATURE_ID_INTERNAL_FEATURE_EXTRACT_PVLINE = 268;
  FEATURE_ID_INTERNAL_FEATURE_ADVANCED_STATS_DATAPOINT = 269;
  FEATURE_ID_INTERNAL_FEATURE_COMPRESS_DATA = 270;
  FEATURE_ID_INTERNAL_FEATURE_RUN_SEARCH = 271;
  FEATURE_ID_INTERNAL_FEATURE_ENABLE_TEST_MODE = 272;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_COACH_TEXT_ASSET = 273;
  FEATURE_ID_INTERNAL_FEATURE_MAIA_BOT_MOVE 
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03667"></a>
## FND-03667: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_COMPRESS_DATA = 270

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_COMPRESS_DATA = 270;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3750.

```text
ERNAL_FEATURE_EXTRACT_PVLINE = 268;
  FEATURE_ID_INTERNAL_FEATURE_ADVANCED_STATS_DATAPOINT = 269;
  FEATURE_ID_INTERNAL_FEATURE_COMPRESS_DATA = 270;
  FEATURE_ID_INTERNAL_FEATURE_RUN_SEARCH = 271;
  FEATURE_ID_INTERNAL_FEATURE_ENABLE_TEST_MODE = 272;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_COACH_TEXT_ASSET = 273;
  FEATURE_ID_INTERNAL_FEATURE_MAIA_BOT_MOVE = 274;
  FEATURE_ID_INTERNAL_FEATURE_UNCOMPRESS_DATA = 275;
  
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03668"></a>
## FND-03668: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_RUN_SEARCH = 271

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_RUN_SEARCH = 271;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3801.

```text
TERNAL_FEATURE_ADVANCED_STATS_DATAPOINT = 269;
  FEATURE_ID_INTERNAL_FEATURE_COMPRESS_DATA = 270;
  FEATURE_ID_INTERNAL_FEATURE_RUN_SEARCH = 271;
  FEATURE_ID_INTERNAL_FEATURE_ENABLE_TEST_MODE = 272;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_COACH_TEXT_ASSET = 273;
  FEATURE_ID_INTERNAL_FEATURE_MAIA_BOT_MOVE = 274;
  FEATURE_ID_INTERNAL_FEATURE_UNCOMPRESS_DATA = 275;
  FEATURE_ID_INTERNAL_FEATURE_UPDATE_DEVELOPER_OPTION
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03669"></a>
## FND-03669: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_ENABLE_TEST_MODE = 272

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_ENABLE_TEST_MODE = 272;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3849.

```text
 FEATURE_ID_INTERNAL_FEATURE_COMPRESS_DATA = 270;
  FEATURE_ID_INTERNAL_FEATURE_RUN_SEARCH = 271;
  FEATURE_ID_INTERNAL_FEATURE_ENABLE_TEST_MODE = 272;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_COACH_TEXT_ASSET = 273;
  FEATURE_ID_INTERNAL_FEATURE_MAIA_BOT_MOVE = 274;
  FEATURE_ID_INTERNAL_FEATURE_UNCOMPRESS_DATA = 275;
  FEATURE_ID_INTERNAL_FEATURE_UPDATE_DEVELOPER_OPTIONS = 276;
  FEATURE_ID_INTERNAL_FEATURE_KEY_GAME_
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03670"></a>
## FND-03670: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_GENERATE_COACH_TEXT_ASSET = 273

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_GENERATE_COACH_TEXT_ASSET = 273;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3903.

```text
ATURE_ID_INTERNAL_FEATURE_RUN_SEARCH = 271;
  FEATURE_ID_INTERNAL_FEATURE_ENABLE_TEST_MODE = 272;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_COACH_TEXT_ASSET = 273;
  FEATURE_ID_INTERNAL_FEATURE_MAIA_BOT_MOVE = 274;
  FEATURE_ID_INTERNAL_FEATURE_UNCOMPRESS_DATA = 275;
  FEATURE_ID_INTERNAL_FEATURE_UPDATE_DEVELOPER_OPTIONS = 276;
  FEATURE_ID_INTERNAL_FEATURE_KEY_GAME_STATE = 277;
  FEATURE_ID_INTERNAL_FEATURE_KEY_POSITIO
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03671"></a>
## FND-03671: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_MAIA_BOT_MOVE = 274

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_MAIA_BOT_MOVE = 274;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 3966.

```text
AL_FEATURE_ENABLE_TEST_MODE = 272;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_COACH_TEXT_ASSET = 273;
  FEATURE_ID_INTERNAL_FEATURE_MAIA_BOT_MOVE = 274;
  FEATURE_ID_INTERNAL_FEATURE_UNCOMPRESS_DATA = 275;
  FEATURE_ID_INTERNAL_FEATURE_UPDATE_DEVELOPER_OPTIONS = 276;
  FEATURE_ID_INTERNAL_FEATURE_KEY_GAME_STATE = 277;
  FEATURE_ID_INTERNAL_FEATURE_KEY_POSITION_SEARCH = 278;
  FEATURE_ID_ADVANCED_STATS_CATEGORY_SPEECH = 2
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03672"></a>
## FND-03672: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_UNCOMPRESS_DATA = 275

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_UNCOMPRESS_DATA = 275;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 4017.

```text
ERNAL_FEATURE_GENERATE_COACH_TEXT_ASSET = 273;
  FEATURE_ID_INTERNAL_FEATURE_MAIA_BOT_MOVE = 274;
  FEATURE_ID_INTERNAL_FEATURE_UNCOMPRESS_DATA = 275;
  FEATURE_ID_INTERNAL_FEATURE_UPDATE_DEVELOPER_OPTIONS = 276;
  FEATURE_ID_INTERNAL_FEATURE_KEY_GAME_STATE = 277;
  FEATURE_ID_INTERNAL_FEATURE_KEY_POSITION_SEARCH = 278;
  FEATURE_ID_ADVANCED_STATS_CATEGORY_SPEECH = 279;
  FEATURE_ID_INTERNAL_FEATURE_CAPS2 = 280;
  FE
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03673"></a>
## FND-03673: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_UPDATE_DEVELOPER_OPTIONS = 276

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_UPDATE_DEVELOPER_OPTIONS = 276;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 4070.

```text
URE_ID_INTERNAL_FEATURE_MAIA_BOT_MOVE = 274;
  FEATURE_ID_INTERNAL_FEATURE_UNCOMPRESS_DATA = 275;
  FEATURE_ID_INTERNAL_FEATURE_UPDATE_DEVELOPER_OPTIONS = 276;
  FEATURE_ID_INTERNAL_FEATURE_KEY_GAME_STATE = 277;
  FEATURE_ID_INTERNAL_FEATURE_KEY_POSITION_SEARCH = 278;
  FEATURE_ID_ADVANCED_STATS_CATEGORY_SPEECH = 279;
  FEATURE_ID_INTERNAL_FEATURE_CAPS2 = 280;
  FEATURE_ID_INTERNAL_FEATURE_GET_COACH_EMOTION = 281;
  
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03674"></a>
## FND-03674: chesscom.explanation_engine.v1.FeatureId.FEATURE_ID_INTERNAL_FEATURE_KEY_GAME_STATE = 277

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEATURE_ID_INTERNAL_FEATURE_KEY_GAME_STATE = 277;

### Evidence

- **SRC-0400** `research/proto/chesscom/explanation_engine/v1/features.proto` — [preserved redacted evidence](../evidence/text/66724324edca4bc1306a021d1c325b247a7c6af26f4fee5be7622facf4575fdf.proto)
  Character offset 4132.

```text
RNAL_FEATURE_UNCOMPRESS_DATA = 275;
  FEATURE_ID_INTERNAL_FEATURE_UPDATE_DEVELOPER_OPTIONS = 276;
  FEATURE_ID_INTERNAL_FEATURE_KEY_GAME_STATE = 277;
  FEATURE_ID_INTERNAL_FEATURE_KEY_POSITION_SEARCH = 278;
  FEATURE_ID_ADVANCED_STATS_CATEGORY_SPEECH = 279;
  FEATURE_ID_INTERNAL_FEATURE_CAPS2 = 280;
  FEATURE_ID_INTERNAL_FEATURE_GET_COACH_EMOTION = 281;
  FEATURE_ID_INTERNAL_FEATURE_GENERATE_COACH_TEXT_ITEMS = 282;
 
```

**Source references:** SRC-0400, SRC-1371  
**URL references:** None independently associated  
**Related findings:** FND-03573, FND-03574, FND-03575

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
