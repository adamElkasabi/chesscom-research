# data_models — findings 1–100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-00275"></a>
## FND-00275: enum declaration: chesscom.analysis.v1.MoveClassification

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MoveClassification {

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 109.

```text
: chesscom/analysis/v1/move_classifications.proto
// syntax: proto3

package chesscom.analysis.v1;

enum MoveClassification {
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  BOOK = 1;
  BRILLIANT = 2;
  GREATFIND = 3;
  BEST = 4;
  EXCELLENT = 5;
  GOOD = 6;
  INACCURACY = 7;
  INACCURACY_OPENING_PHASE = 8;
  INACCURACY_MID_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MIS
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00276"></a>
## FND-00276: chesscom.analysis.v1.MoveClassification.MOVE_CLASSIFICATION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_UNSPECIFIED = 0;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 137.

```text
classifications.proto
// syntax: proto3

package chesscom.analysis.v1;

enum MoveClassification {
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  BOOK = 1;
  BRILLIANT = 2;
  GREATFIND = 3;
  BEST = 4;
  EXCELLENT = 5;
  GOOD = 6;
  INACCURACY = 7;
  INACCURACY_OPENING_PHASE = 8;
  INACCURACY_MID_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00277"></a>
## FND-00277: chesscom.analysis.v1.MoveClassification.BOOK = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOOK = 1;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 176.

```text


package chesscom.analysis.v1;

enum MoveClassification {
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  BOOK = 1;
  BRILLIANT = 2;
  GREATFIND = 3;
  BEST = 4;
  EXCELLENT = 5;
  GOOD = 6;
  INACCURACY = 7;
  INACCURACY_OPENING_PHASE = 8;
  INACCURACY_MID_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER 
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00278"></a>
## FND-00278: chesscom.analysis.v1.MoveClassification.BRILLIANT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BRILLIANT = 2;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 188.

```text
esscom.analysis.v1;

enum MoveClassification {
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  BOOK = 1;
  BRILLIANT = 2;
  GREATFIND = 3;
  BEST = 4;
  EXCELLENT = 5;
  GOOD = 6;
  INACCURACY = 7;
  INACCURACY_OPENING_PHASE = 8;
  INACCURACY_MID_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUN
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00279"></a>
## FND-00279: chesscom.analysis.v1.MoveClassification.GREATFIND = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GREATFIND = 3;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 205.

```text
1;

enum MoveClassification {
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  BOOK = 1;
  BRILLIANT = 2;
  GREATFIND = 3;
  BEST = 4;
  EXCELLENT = 5;
  GOOD = 6;
  INACCURACY = 7;
  INACCURACY_OPENING_PHASE = 8;
  INACCURACY_MID_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00280"></a>
## FND-00280: chesscom.analysis.v1.MoveClassification.BEST = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BEST = 4;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 222.

```text
sification {
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  BOOK = 1;
  BRILLIANT = 2;
  GREATFIND = 3;
  BEST = 4;
  EXCELLENT = 5;
  GOOD = 6;
  INACCURACY = 7;
  INACCURACY_OPENING_PHASE = 8;
  INACCURACY_MID_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00281"></a>
## FND-00281: chesscom.analysis.v1.MoveClassification.EXCELLENT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EXCELLENT = 5;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 234.

```text

  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  BOOK = 1;
  BRILLIANT = 2;
  GREATFIND = 3;
  BEST = 4;
  EXCELLENT = 5;
  GOOD = 6;
  INACCURACY = 7;
  INACCURACY_OPENING_PHASE = 8;
  INACCURACY_MID_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHA
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00282"></a>
## FND-00282: chesscom.analysis.v1.MoveClassification.GOOD = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GOOD = 6;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 251.

```text
ATION_UNSPECIFIED = 0;
  BOOK = 1;
  BRILLIANT = 2;
  GREATFIND = 3;
  BEST = 4;
  EXCELLENT = 5;
  GOOD = 6;
  INACCURACY = 7;
  INACCURACY_OPENING_PHASE = 8;
  INACCURACY_MID_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDE
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00283"></a>
## FND-00283: chesscom.analysis.v1.MoveClassification.INACCURACY = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INACCURACY = 7;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 263.

```text
IFIED = 0;
  BOOK = 1;
  BRILLIANT = 2;
  GREATFIND = 3;
  BEST = 4;
  EXCELLENT = 5;
  GOOD = 6;
  INACCURACY = 7;
  INACCURACY_OPENING_PHASE = 8;
  INACCURACY_MID_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_P
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00284"></a>
## FND-00284: chesscom.analysis.v1.MoveClassification.INACCURACY_OPENING_PHASE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INACCURACY_OPENING_PHASE = 8;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 281.

```text
= 1;
  BRILLIANT = 2;
  GREATFIND = 3;
  BEST = 4;
  EXCELLENT = 5;
  GOOD = 6;
  INACCURACY = 7;
  INACCURACY_OPENING_PHASE = 8;
  INACCURACY_MID_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCE
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00285"></a>
## FND-00285: chesscom.analysis.v1.MoveClassification.INACCURACY_MID_GAME_PHASE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INACCURACY_MID_GAME_PHASE = 9;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 313.

```text
D = 3;
  BEST = 4;
  EXCELLENT = 5;
  GOOD = 6;
  INACCURACY = 7;
  INACCURACY_OPENING_PHASE = 8;
  INACCURACY_MID_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPEN
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00286"></a>
## FND-00286: chesscom.analysis.v1.MoveClassification.INACCURACY_END_GAME_PHASE = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INACCURACY_END_GAME_PHASE = 10;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 346.

```text
5;
  GOOD = 6;
  INACCURACY = 7;
  INACCURACY_OPENING_PHASE = 8;
  INACCURACY_MID_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_P
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00287"></a>
## FND-00287: chesscom.analysis.v1.MoveClassification.MISTAKE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MISTAKE = 11;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 380.

```text
 INACCURACY_OPENING_PHASE = 8;
  INACCURACY_MID_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE =
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00288"></a>
## FND-00288: chesscom.analysis.v1.MoveClassification.MISTAKE_OPENING_PHASE = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MISTAKE_OPENING_PHASE = 12;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 396.

```text
ING_PHASE = 8;
  INACCURACY_MID_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MA
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00289"></a>
## FND-00289: chesscom.analysis.v1.MoveClassification.MISTAKE_MID_GAME_PHASE = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MISTAKE_MID_GAME_PHASE = 13;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 426.

```text
D_GAME_PHASE = 9;
  INACCURACY_END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
 
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00290"></a>
## FND-00290: chesscom.analysis.v1.MoveClassification.MISTAKE_END_GAME_PHASE = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MISTAKE_END_GAME_PHASE = 14;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 457.

```text
END_GAME_PHASE = 10;
  MISTAKE = 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRIT
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00291"></a>
## FND-00291: chesscom.analysis.v1.MoveClassification.BLUNDER = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BLUNDER = 15;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 488.

```text
= 11;
  MISTAKE_OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00292"></a>
## FND-00292: chesscom.analysis.v1.MoveClassification.BLUNDER_OPENING_PHASE = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BLUNDER_OPENING_PHASE = 16;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 504.

```text
OPENING_PHASE = 12;
  MISTAKE_MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENI
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00293"></a>
## FND-00293: chesscom.analysis.v1.MoveClassification.BLUNDER_MID_GAME_PHASE = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BLUNDER_MID_GAME_PHASE = 17;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 534.

```text
MID_GAME_PHASE = 13;
  MISTAKE_END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MI
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00294"></a>
## FND-00294: chesscom.analysis.v1.MoveClassification.BLUNDER_END_GAME_PHASE = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BLUNDER_END_GAME_PHASE = 18;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 565.

```text
END_GAME_PHASE = 14;
  BLUNDER = 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MID_GAME_PHASE = 30;
  MISSED_WIN
```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00295"></a>
## FND-00295: chesscom.analysis.v1.MoveClassification.FORCED = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FORCED = 19;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 596.

```text
= 15;
  BLUNDER_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MID_GAME_PHASE = 30;
  MISSED_WIN_END_GAME_PHASE = 31;
}

```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00296"></a>
## FND-00296: chesscom.analysis.v1.MoveClassification.MISS = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MISS = 20;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 611.

```text
_OPENING_PHASE = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MID_GAME_PHASE = 30;
  MISSED_WIN_END_GAME_PHASE = 31;
}

```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00297"></a>
## FND-00297: chesscom.analysis.v1.MoveClassification.MISS_OPENING_PHASE = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MISS_OPENING_PHASE = 21;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 624.

```text
E = 16;
  BLUNDER_MID_GAME_PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MID_GAME_PHASE = 30;
  MISSED_WIN_END_GAME_PHASE = 31;
}

```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00298"></a>
## FND-00298: chesscom.analysis.v1.MoveClassification.MISS_MID_GAME_PHASE = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MISS_MID_GAME_PHASE = 22;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 651.

```text
PHASE = 17;
  BLUNDER_END_GAME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MID_GAME_PHASE = 30;
  MISSED_WIN_END_GAME_PHASE = 31;
}

```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00299"></a>
## FND-00299: chesscom.analysis.v1.MoveClassification.MISS_END_GAME_PHASE = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MISS_END_GAME_PHASE = 23;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 679.

```text
ME_PHASE = 18;
  FORCED = 19;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MID_GAME_PHASE = 30;
  MISSED_WIN_END_GAME_PHASE = 31;
}

```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00300"></a>
## FND-00300: chesscom.analysis.v1.MoveClassification.MISSED_MATE = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MISSED_MATE = 24;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 707.

```text
;
  MISS = 20;
  MISS_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MID_GAME_PHASE = 30;
  MISSED_WIN_END_GAME_PHASE = 31;
}

```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00301"></a>
## FND-00301: chesscom.analysis.v1.MoveClassification.FASTER_MATE = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FASTER_MATE = 25;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 727.

```text
S_OPENING_PHASE = 21;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MID_GAME_PHASE = 30;
  MISSED_WIN_END_GAME_PHASE = 31;
}

```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00302"></a>
## FND-00302: chesscom.analysis.v1.MoveClassification.WINNING_TO_LOSING = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

WINNING_TO_LOSING = 26;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 747.

```text
;
  MISS_MID_GAME_PHASE = 22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MID_GAME_PHASE = 30;
  MISSED_WIN_END_GAME_PHASE = 31;
}

```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00303"></a>
## FND-00303: chesscom.analysis.v1.MoveClassification.CRITICAL = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CRITICAL = 27;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 773.

```text
22;
  MISS_END_GAME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MID_GAME_PHASE = 30;
  MISSED_WIN_END_GAME_PHASE = 31;
}

```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00304"></a>
## FND-00304: chesscom.analysis.v1.MoveClassification.MISSEDWIN = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MISSEDWIN = 28;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 790.

```text
ME_PHASE = 23;
  MISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MID_GAME_PHASE = 30;
  MISSED_WIN_END_GAME_PHASE = 31;
}

```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00305"></a>
## FND-00305: chesscom.analysis.v1.MoveClassification.MISSED_WIN_OPENING_PHASE = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MISSED_WIN_OPENING_PHASE = 29;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 808.

```text
ISSED_MATE = 24;
  FASTER_MATE = 25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MID_GAME_PHASE = 30;
  MISSED_WIN_END_GAME_PHASE = 31;
}

```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00306"></a>
## FND-00306: chesscom.analysis.v1.MoveClassification.MISSED_WIN_MID_GAME_PHASE = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MISSED_WIN_MID_GAME_PHASE = 30;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 841.

```text
25;
  WINNING_TO_LOSING = 26;
  CRITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MID_GAME_PHASE = 30;
  MISSED_WIN_END_GAME_PHASE = 31;
}

```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00307"></a>
## FND-00307: chesscom.analysis.v1.MoveClassification.MISSED_WIN_END_GAME_PHASE = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MISSED_WIN_END_GAME_PHASE = 31;

### Evidence

- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
  Character offset 875.

```text
ITICAL = 27;
  MISSEDWIN = 28;
  MISSED_WIN_OPENING_PHASE = 29;
  MISSED_WIN_MID_GAME_PHASE = 30;
  MISSED_WIN_END_GAME_PHASE = 31;
}

```

**Source references:** SRC-0206, SRC-1177  
**URL references:** None independently associated  
**Related findings:** FND-00275, FND-00276, FND-00277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00308"></a>
## FND-00308: enum declaration: chesscom.analysis.v2.MoveClassification

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MoveClassification {

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 109.

```text
: chesscom/analysis/v2/move_classifications.proto
// syntax: proto3

package chesscom.analysis.v2;

enum MoveClassification {
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_BOOK = 1;
  MOVE_CLASSIFICATION_BRILLIANT = 2;
  MOVE_CLASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CL
```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00309"></a>
## FND-00309: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_UNSPECIFIED = 0;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 137.

```text
classifications.proto
// syntax: proto3

package chesscom.analysis.v2;

enum MoveClassification {
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_BOOK = 1;
  MOVE_CLASSIFICATION_BRILLIANT = 2;
  MOVE_CLASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  
```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00310"></a>
## FND-00310: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_BOOK = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_BOOK = 1;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 176.

```text


package chesscom.analysis.v2;

enum MoveClassification {
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_BOOK = 1;
  MOVE_CLASSIFICATION_BRILLIANT = 2;
  MOVE_CLASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE
```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00311"></a>
## FND-00311: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_BRILLIANT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_BRILLIANT = 2;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 208.

```text

enum MoveClassification {
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_BOOK = 1;
  MOVE_CLASSIFICATION_BRILLIANT = 2;
  MOVE_CLASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED_WIN = 10;
```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00312"></a>
## FND-00312: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_GREAT_FIND = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_GREAT_FIND = 3;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 245.

```text
SSIFICATION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_BOOK = 1;
  MOVE_CLASSIFICATION_BRILLIANT = 2;
  MOVE_CLASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED_WIN = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
 
```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00313"></a>
## FND-00313: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_BEST = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_BEST = 4;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 283.

```text
ASSIFICATION_BOOK = 1;
  MOVE_CLASSIFICATION_BRILLIANT = 2;
  MOVE_CLASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED_WIN = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_MISSED_FASTER_MAT
```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00314"></a>
## FND-00314: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_EXCELLENT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_EXCELLENT = 5;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 315.

```text
ASSIFICATION_BRILLIANT = 2;
  MOVE_CLASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED_WIN = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_MISSED_FASTER_MATE = 12;
  MOVE_CLASSIFICATION_MI
```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00315"></a>
## FND-00315: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_GOOD = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_GOOD = 6;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 352.

```text
ASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED_WIN = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_MISSED_FASTER_MATE = 12;
  MOVE_CLASSIFICATION_MISSED_MATE = 13;
  MOVE_CLASSIFICATION
```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00316"></a>
## FND-00316: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_INACCURACY = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_INACCURACY = 7;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 384.

```text
OVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED_WIN = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_MISSED_FASTER_MATE = 12;
  MOVE_CLASSIFICATION_MISSED_MATE = 13;
  MOVE_CLASSIFICATION_MISSED_FREE_PIECE = 14;
  MOVE_
```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00317"></a>
## FND-00317: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_MISTAKE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_MISTAKE = 8;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 422.

```text
ASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED_WIN = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_MISSED_FASTER_MATE = 12;
  MOVE_CLASSIFICATION_MISSED_MATE = 13;
  MOVE_CLASSIFICATION_MISSED_FREE_PIECE = 14;
  MOVE_CLASSIFICATION_MISSED_TACTIC = 15;
  M
```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00318"></a>
## FND-00318: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_BLUNDER = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_BLUNDER = 9;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 457.

```text
CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED_WIN = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_MISSED_FASTER_MATE = 12;
  MOVE_CLASSIFICATION_MISSED_MATE = 13;
  MOVE_CLASSIFICATION_MISSED_FREE_PIECE = 14;
  MOVE_CLASSIFICATION_MISSED_TACTIC = 15;
  MOVE_CLASSIFICATION_MISSED_COMEBACK 
```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00319"></a>
## FND-00319: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_MISSED_WIN = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_MISSED_WIN = 10;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 492.

```text
SSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED_WIN = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_MISSED_FASTER_MATE = 12;
  MOVE_CLASSIFICATION_MISSED_MATE = 13;
  MOVE_CLASSIFICATION_MISSED_FREE_PIECE = 14;
  MOVE_CLASSIFICATION_MISSED_TACTIC = 15;
  MOVE_CLASSIFICATION_MISSED_COMEBACK = 16;
  MOVE_CLASSIFICATION_MISSED_
```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00320"></a>
## FND-00320: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_FORCED = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_FORCED = 11;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 531.

```text
SIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED_WIN = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_MISSED_FASTER_MATE = 12;
  MOVE_CLASSIFICATION_MISSED_MATE = 13;
  MOVE_CLASSIFICATION_MISSED_FREE_PIECE = 14;
  MOVE_CLASSIFICATION_MISSED_TACTIC = 15;
  MOVE_CLASSIFICATION_MISSED_COMEBACK = 16;
  MOVE_CLASSIFICATION_MISSED_OPPORTUNITY = 17;
  MOVE_CLASSIFICATION
```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00321"></a>
## FND-00321: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_MISSED_FASTER_MATE = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_MISSED_FASTER_MATE = 12;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 566.

```text
SIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED_WIN = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_MISSED_FASTER_MATE = 12;
  MOVE_CLASSIFICATION_MISSED_MATE = 13;
  MOVE_CLASSIFICATION_MISSED_FREE_PIECE = 14;
  MOVE_CLASSIFICATION_MISSED_TACTIC = 15;
  MOVE_CLASSIFICATION_MISSED_COMEBACK = 16;
  MOVE_CLASSIFICATION_MISSED_OPPORTUNITY = 17;
  MOVE_CLASSIFICATION_MISSED_BRILLIANT = 18;
  MOVE_CLAS
```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00322"></a>
## FND-00322: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_MISSED_MATE = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_MISSED_MATE = 13;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 613.

```text
ISSED_WIN = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_MISSED_FASTER_MATE = 12;
  MOVE_CLASSIFICATION_MISSED_MATE = 13;
  MOVE_CLASSIFICATION_MISSED_FREE_PIECE = 14;
  MOVE_CLASSIFICATION_MISSED_TACTIC = 15;
  MOVE_CLASSIFICATION_MISSED_COMEBACK = 16;
  MOVE_CLASSIFICATION_MISSED_OPPORTUNITY = 17;
  MOVE_CLASSIFICATION_MISSED_BRILLIANT = 18;
  MOVE_CLASSIFICATION_MISSED_CRITICAL = 19;
}

```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00323"></a>
## FND-00323: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_MISSED_FREE_PIECE = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_MISSED_FREE_PIECE = 14;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 653.

```text
RCED = 11;
  MOVE_CLASSIFICATION_MISSED_FASTER_MATE = 12;
  MOVE_CLASSIFICATION_MISSED_MATE = 13;
  MOVE_CLASSIFICATION_MISSED_FREE_PIECE = 14;
  MOVE_CLASSIFICATION_MISSED_TACTIC = 15;
  MOVE_CLASSIFICATION_MISSED_COMEBACK = 16;
  MOVE_CLASSIFICATION_MISSED_OPPORTUNITY = 17;
  MOVE_CLASSIFICATION_MISSED_BRILLIANT = 18;
  MOVE_CLASSIFICATION_MISSED_CRITICAL = 19;
}

```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00324"></a>
## FND-00324: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_MISSED_TACTIC = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_MISSED_TACTIC = 15;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 699.

```text
_MATE = 12;
  MOVE_CLASSIFICATION_MISSED_MATE = 13;
  MOVE_CLASSIFICATION_MISSED_FREE_PIECE = 14;
  MOVE_CLASSIFICATION_MISSED_TACTIC = 15;
  MOVE_CLASSIFICATION_MISSED_COMEBACK = 16;
  MOVE_CLASSIFICATION_MISSED_OPPORTUNITY = 17;
  MOVE_CLASSIFICATION_MISSED_BRILLIANT = 18;
  MOVE_CLASSIFICATION_MISSED_CRITICAL = 19;
}

```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00325"></a>
## FND-00325: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_MISSED_COMEBACK = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_MISSED_COMEBACK = 16;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 741.

```text
ATE = 13;
  MOVE_CLASSIFICATION_MISSED_FREE_PIECE = 14;
  MOVE_CLASSIFICATION_MISSED_TACTIC = 15;
  MOVE_CLASSIFICATION_MISSED_COMEBACK = 16;
  MOVE_CLASSIFICATION_MISSED_OPPORTUNITY = 17;
  MOVE_CLASSIFICATION_MISSED_BRILLIANT = 18;
  MOVE_CLASSIFICATION_MISSED_CRITICAL = 19;
}

```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00326"></a>
## FND-00326: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_MISSED_OPPORTUNITY = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_MISSED_OPPORTUNITY = 17;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 785.

```text
PIECE = 14;
  MOVE_CLASSIFICATION_MISSED_TACTIC = 15;
  MOVE_CLASSIFICATION_MISSED_COMEBACK = 16;
  MOVE_CLASSIFICATION_MISSED_OPPORTUNITY = 17;
  MOVE_CLASSIFICATION_MISSED_BRILLIANT = 18;
  MOVE_CLASSIFICATION_MISSED_CRITICAL = 19;
}

```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00327"></a>
## FND-00327: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_MISSED_BRILLIANT = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_MISSED_BRILLIANT = 18;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 832.

```text
 = 15;
  MOVE_CLASSIFICATION_MISSED_COMEBACK = 16;
  MOVE_CLASSIFICATION_MISSED_OPPORTUNITY = 17;
  MOVE_CLASSIFICATION_MISSED_BRILLIANT = 18;
  MOVE_CLASSIFICATION_MISSED_CRITICAL = 19;
}

```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00328"></a>
## FND-00328: chesscom.analysis.v2.MoveClassification.MOVE_CLASSIFICATION_MISSED_CRITICAL = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_MISSED_CRITICAL = 19;

### Evidence

- **SRC-0207** `research/proto/chesscom/analysis/v2/move_classifications.proto` — [preserved redacted evidence](../evidence/text/9680d3e0d6bf80a90b1a4252c969cbbba9fc1773c8547561346fc7da07cb3778.proto)
  Character offset 877.

```text
= 16;
  MOVE_CLASSIFICATION_MISSED_OPPORTUNITY = 17;
  MOVE_CLASSIFICATION_MISSED_BRILLIANT = 18;
  MOVE_CLASSIFICATION_MISSED_CRITICAL = 19;
}

```

**Source references:** SRC-0207, SRC-1178  
**URL references:** None independently associated  
**Related findings:** FND-00308, FND-00309, FND-00310

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00329"></a>
## FND-00329: message declaration: chesscom.api.v1.Asset

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Asset {

### Evidence

- **SRC-0208** `research/proto/chesscom/api/v1/asset.proto` — [preserved redacted evidence](../evidence/text/c1a104006242a859b422c24c72e8a5475d0e62e1eabdc47fe0dda49def963f15.proto)
  Character offset 84.

```text
// source: chesscom/api/v1/asset.proto
// syntax: proto3

package chesscom.api.v1;

message Asset {
  oneof _content_type {
  string content_type = 3;
  }
  oneof _url {
  string url = 4;
  }
  oneof _alt_text {
  string alt_text = 5;
  }
  optional string name = 1;
  optional string key = 2;
}

```

**Source references:** SRC-0208, SRC-1179  
**URL references:** None independently associated  
**Related findings:** FND-00330, FND-00331

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00330"></a>
## FND-00330: oneof declaration: chesscom.api.v1.Asset._content_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _content_type {

### Evidence

- **SRC-0208** `research/proto/chesscom/api/v1/asset.proto` — [preserved redacted evidence](../evidence/text/c1a104006242a859b422c24c72e8a5475d0e62e1eabdc47fe0dda49def963f15.proto)
  Character offset 102.

```text
 source: chesscom/api/v1/asset.proto
// syntax: proto3

package chesscom.api.v1;

message Asset {
  oneof _content_type {
  string content_type = 3;
  }
  oneof _url {
  string url = 4;
  }
  oneof _alt_text {
  string alt_text = 5;
  }
  optional string name = 1;
  optional string key = 2;
}

```

**Source references:** SRC-0208, SRC-1179  
**URL references:** None independently associated  
**Related findings:** FND-00329, FND-00331

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00331"></a>
## FND-00331: chesscom.api.v1.Asset.content_type = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string content_type = 3;

### Evidence

- **SRC-0208** `research/proto/chesscom/api/v1/asset.proto` — [preserved redacted evidence](../evidence/text/c1a104006242a859b422c24c72e8a5475d0e62e1eabdc47fe0dda49def963f15.proto)
  Character offset 126.

```text
/asset.proto
// syntax: proto3

package chesscom.api.v1;

message Asset {
  oneof _content_type {
  string content_type = 3;
  }
  oneof _url {
  string url = 4;
  }
  oneof _alt_text {
  string alt_text = 5;
  }
  optional string name = 1;
  optional string key = 2;
}

```

**Source references:** SRC-0208, SRC-1179  
**URL references:** None independently associated  
**Related findings:** FND-00329, FND-00330

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00332"></a>
## FND-00332: oneof declaration: chesscom.api.v1.Asset._url

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _url {

### Evidence

- **SRC-0208** `research/proto/chesscom/api/v1/asset.proto` — [preserved redacted evidence](../evidence/text/c1a104006242a859b422c24c72e8a5475d0e62e1eabdc47fe0dda49def963f15.proto)
  Character offset 157.

```text

package chesscom.api.v1;

message Asset {
  oneof _content_type {
  string content_type = 3;
  }
  oneof _url {
  string url = 4;
  }
  oneof _alt_text {
  string alt_text = 5;
  }
  optional string name = 1;
  optional string key = 2;
}

```

**Source references:** SRC-0208, SRC-1179  
**URL references:** None independently associated  
**Related findings:** FND-00329, FND-00330, FND-00331

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00333"></a>
## FND-00333: chesscom.api.v1.Asset.url = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string url = 4;

### Evidence

- **SRC-0208** `research/proto/chesscom/api/v1/asset.proto` — [preserved redacted evidence](../evidence/text/c1a104006242a859b422c24c72e8a5475d0e62e1eabdc47fe0dda49def963f15.proto)
  Character offset 172.

```text
om.api.v1;

message Asset {
  oneof _content_type {
  string content_type = 3;
  }
  oneof _url {
  string url = 4;
  }
  oneof _alt_text {
  string alt_text = 5;
  }
  optional string name = 1;
  optional string key = 2;
}

```

**Source references:** SRC-0208, SRC-1179  
**URL references:** None independently associated  
**Related findings:** FND-00329, FND-00330, FND-00331

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00334"></a>
## FND-00334: oneof declaration: chesscom.api.v1.Asset._alt_text

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _alt_text {

### Evidence

- **SRC-0208** `research/proto/chesscom/api/v1/asset.proto` — [preserved redacted evidence](../evidence/text/c1a104006242a859b422c24c72e8a5475d0e62e1eabdc47fe0dda49def963f15.proto)
  Character offset 194.

```text
set {
  oneof _content_type {
  string content_type = 3;
  }
  oneof _url {
  string url = 4;
  }
  oneof _alt_text {
  string alt_text = 5;
  }
  optional string name = 1;
  optional string key = 2;
}

```

**Source references:** SRC-0208, SRC-1179  
**URL references:** None independently associated  
**Related findings:** FND-00329, FND-00330, FND-00331

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00335"></a>
## FND-00335: chesscom.api.v1.Asset.alt_text = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string alt_text = 5;

### Evidence

- **SRC-0208** `research/proto/chesscom/api/v1/asset.proto` — [preserved redacted evidence](../evidence/text/c1a104006242a859b422c24c72e8a5475d0e62e1eabdc47fe0dda49def963f15.proto)
  Character offset 214.

```text
nt_type {
  string content_type = 3;
  }
  oneof _url {
  string url = 4;
  }
  oneof _alt_text {
  string alt_text = 5;
  }
  optional string name = 1;
  optional string key = 2;
}

```

**Source references:** SRC-0208, SRC-1179  
**URL references:** None independently associated  
**Related findings:** FND-00329, FND-00330, FND-00331

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00336"></a>
## FND-00336: chesscom.api.v1.Asset.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0208** `research/proto/chesscom/api/v1/asset.proto` — [preserved redacted evidence](../evidence/text/c1a104006242a859b422c24c72e8a5475d0e62e1eabdc47fe0dda49def963f15.proto)
  Character offset 241.

```text
type = 3;
  }
  oneof _url {
  string url = 4;
  }
  oneof _alt_text {
  string alt_text = 5;
  }
  optional string name = 1;
  optional string key = 2;
}

```

**Source references:** SRC-0208, SRC-1179  
**URL references:** None independently associated  
**Related findings:** FND-00329, FND-00330, FND-00331

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00337"></a>
## FND-00337: chesscom.api.v1.Asset.key = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 2;

### Evidence

- **SRC-0208** `research/proto/chesscom/api/v1/asset.proto` — [preserved redacted evidence](../evidence/text/c1a104006242a859b422c24c72e8a5475d0e62e1eabdc47fe0dda49def963f15.proto)
  Character offset 269.

```text

  string url = 4;
  }
  oneof _alt_text {
  string alt_text = 5;
  }
  optional string name = 1;
  optional string key = 2;
}

```

**Source references:** SRC-0208, SRC-1179  
**URL references:** None independently associated  
**Related findings:** FND-00329, FND-00330, FND-00331

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00338"></a>
## FND-00338: message declaration: chesscom.api.v1.Country

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Country {

### Evidence

- **SRC-0209** `research/proto/chesscom/api/v1/country.proto` — [preserved redacted evidence](../evidence/text/64b4399e737aa1a1dfdba07c7b2cf931f0b532b30337173528c3e6899334990e.proto)
  Character offset 86.

```text
// source: chesscom/api/v1/country.proto
// syntax: proto3

package chesscom.api.v1;

message Country {
  optional int32 id = 1;
  optional string name = 2;
  optional string name_localized = 3;
  optional string code = 4;
}

```

**Source references:** SRC-0209, SRC-1180  
**URL references:** None independently associated  
**Related findings:** FND-00339, FND-00340

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00339"></a>
## FND-00339: chesscom.api.v1.Country.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 id = 1;

### Evidence

- **SRC-0209** `research/proto/chesscom/api/v1/country.proto` — [preserved redacted evidence](../evidence/text/64b4399e737aa1a1dfdba07c7b2cf931f0b532b30337173528c3e6899334990e.proto)
  Character offset 106.

```text
rce: chesscom/api/v1/country.proto
// syntax: proto3

package chesscom.api.v1;

message Country {
  optional int32 id = 1;
  optional string name = 2;
  optional string name_localized = 3;
  optional string code = 4;
}

```

**Source references:** SRC-0209, SRC-1180  
**URL references:** None independently associated  
**Related findings:** FND-00338, FND-00340

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00340"></a>
## FND-00340: chesscom.api.v1.Country.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0209** `research/proto/chesscom/api/v1/country.proto` — [preserved redacted evidence](../evidence/text/64b4399e737aa1a1dfdba07c7b2cf931f0b532b30337173528c3e6899334990e.proto)
  Character offset 131.

```text
try.proto
// syntax: proto3

package chesscom.api.v1;

message Country {
  optional int32 id = 1;
  optional string name = 2;
  optional string name_localized = 3;
  optional string code = 4;
}

```

**Source references:** SRC-0209, SRC-1180  
**URL references:** None independently associated  
**Related findings:** FND-00338, FND-00339

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00341"></a>
## FND-00341: chesscom.api.v1.Country.name_localized = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name_localized = 3;

### Evidence

- **SRC-0209** `research/proto/chesscom/api/v1/country.proto` — [preserved redacted evidence](../evidence/text/64b4399e737aa1a1dfdba07c7b2cf931f0b532b30337173528c3e6899334990e.proto)
  Character offset 159.

```text

package chesscom.api.v1;

message Country {
  optional int32 id = 1;
  optional string name = 2;
  optional string name_localized = 3;
  optional string code = 4;
}

```

**Source references:** SRC-0209, SRC-1180  
**URL references:** None independently associated  
**Related findings:** FND-00338, FND-00339, FND-00340

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00342"></a>
## FND-00342: chesscom.api.v1.Country.code = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string code = 4;

### Evidence

- **SRC-0209** `research/proto/chesscom/api/v1/country.proto` — [preserved redacted evidence](../evidence/text/64b4399e737aa1a1dfdba07c7b2cf931f0b532b30337173528c3e6899334990e.proto)
  Character offset 197.

```text
ntry {
  optional int32 id = 1;
  optional string name = 2;
  optional string name_localized = 3;
  optional string code = 4;
}

```

**Source references:** SRC-0209, SRC-1180  
**URL references:** None independently associated  
**Related findings:** FND-00338, FND-00339, FND-00340

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00343"></a>
## FND-00343: message declaration: chesscom.api.v1.Date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Date {

### Evidence

- **SRC-0210** `research/proto/chesscom/api/v1/date.proto` — [preserved redacted evidence](../evidence/text/4c9682a776e1fa33c2e9107df277646a1409db82f24de6eb312ecc4646f08a55.proto)
  Character offset 83.

```text
// source: chesscom/api/v1/date.proto
// syntax: proto3

package chesscom.api.v1;

message Date {
  optional int32 year = 1;
  optional int32 month = 2;
  optional int32 day = 3;
}

```

**Source references:** SRC-0210, SRC-1181  
**URL references:** None independently associated  
**Related findings:** FND-00344, FND-00345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00344"></a>
## FND-00344: chesscom.api.v1.Date.year = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 year = 1;

### Evidence

- **SRC-0210** `research/proto/chesscom/api/v1/date.proto` — [preserved redacted evidence](../evidence/text/4c9682a776e1fa33c2e9107df277646a1409db82f24de6eb312ecc4646f08a55.proto)
  Character offset 100.

```text
// source: chesscom/api/v1/date.proto
// syntax: proto3

package chesscom.api.v1;

message Date {
  optional int32 year = 1;
  optional int32 month = 2;
  optional int32 day = 3;
}

```

**Source references:** SRC-0210, SRC-1181  
**URL references:** None independently associated  
**Related findings:** FND-00343, FND-00345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00345"></a>
## FND-00345: chesscom.api.v1.Date.month = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 month = 2;

### Evidence

- **SRC-0210** `research/proto/chesscom/api/v1/date.proto` — [preserved redacted evidence](../evidence/text/4c9682a776e1fa33c2e9107df277646a1409db82f24de6eb312ecc4646f08a55.proto)
  Character offset 127.

```text
date.proto
// syntax: proto3

package chesscom.api.v1;

message Date {
  optional int32 year = 1;
  optional int32 month = 2;
  optional int32 day = 3;
}

```

**Source references:** SRC-0210, SRC-1181  
**URL references:** None independently associated  
**Related findings:** FND-00343, FND-00344

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00346"></a>
## FND-00346: chesscom.api.v1.Date.day = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 day = 3;

### Evidence

- **SRC-0210** `research/proto/chesscom/api/v1/date.proto` — [preserved redacted evidence](../evidence/text/4c9682a776e1fa33c2e9107df277646a1409db82f24de6eb312ecc4646f08a55.proto)
  Character offset 155.

```text


package chesscom.api.v1;

message Date {
  optional int32 year = 1;
  optional int32 month = 2;
  optional int32 day = 3;
}

```

**Source references:** SRC-0210, SRC-1181  
**URL references:** None independently associated  
**Related findings:** FND-00343, FND-00344, FND-00345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00347"></a>
## FND-00347: message declaration: chesscom.api.v1.Decimal

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Decimal {

### Evidence

- **SRC-0211** `research/proto/chesscom/api/v1/decimal.proto` — [preserved redacted evidence](../evidence/text/c4afecb8863a9455437b9a3d5dcd28bfdea90a75a0698034c6c78ce6cd44c32b.proto)
  Character offset 86.

```text
// source: chesscom/api/v1/decimal.proto
// syntax: proto3

package chesscom.api.v1;

message Decimal {
  optional int64 value = 1;
  optional int32 scale = 2;
}

```

**Source references:** SRC-0211, SRC-1182  
**URL references:** None independently associated  
**Related findings:** FND-00348, FND-00349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00348"></a>
## FND-00348: chesscom.api.v1.Decimal.value = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 value = 1;

### Evidence

- **SRC-0211** `research/proto/chesscom/api/v1/decimal.proto` — [preserved redacted evidence](../evidence/text/c4afecb8863a9455437b9a3d5dcd28bfdea90a75a0698034c6c78ce6cd44c32b.proto)
  Character offset 106.

```text
rce: chesscom/api/v1/decimal.proto
// syntax: proto3

package chesscom.api.v1;

message Decimal {
  optional int64 value = 1;
  optional int32 scale = 2;
}

```

**Source references:** SRC-0211, SRC-1182  
**URL references:** None independently associated  
**Related findings:** FND-00347, FND-00349

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00349"></a>
## FND-00349: chesscom.api.v1.Decimal.scale = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 scale = 2;

### Evidence

- **SRC-0211** `research/proto/chesscom/api/v1/decimal.proto` — [preserved redacted evidence](../evidence/text/c4afecb8863a9455437b9a3d5dcd28bfdea90a75a0698034c6c78ce6cd44c32b.proto)
  Character offset 134.

```text
.proto
// syntax: proto3

package chesscom.api.v1;

message Decimal {
  optional int64 value = 1;
  optional int32 scale = 2;
}

```

**Source references:** SRC-0211, SRC-1182  
**URL references:** None independently associated  
**Related findings:** FND-00347, FND-00348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00350"></a>
## FND-00350: message declaration: chesscom.api.v1.TwirpError

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TwirpError {

### Evidence

- **SRC-0212** `research/proto/chesscom/api/v1/error.proto` — [preserved redacted evidence](../evidence/text/d8ca1402fb62c020bad82173b10d5aed44ad222e7e2dc7c050a1c638fac80188.proto)
  Character offset 84.

```text
// source: chesscom/api/v1/error.proto
// syntax: proto3

package chesscom.api.v1;

message TwirpError {
  optional string msg = 1;
  optional string code = 2;
  repeated .chesscom.api.v1.TwirpError.MetaEntry meta = 3;
  message MetaEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

```

**Source references:** SRC-0212, SRC-1183  
**URL references:** None independently associated  
**Related findings:** FND-00351, FND-00352

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00351"></a>
## FND-00351: chesscom.api.v1.TwirpError.msg = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string msg = 1;

### Evidence

- **SRC-0212** `research/proto/chesscom/api/v1/error.proto` — [preserved redacted evidence](../evidence/text/d8ca1402fb62c020bad82173b10d5aed44ad222e7e2dc7c050a1c638fac80188.proto)
  Character offset 107.

```text
ce: chesscom/api/v1/error.proto
// syntax: proto3

package chesscom.api.v1;

message TwirpError {
  optional string msg = 1;
  optional string code = 2;
  repeated .chesscom.api.v1.TwirpError.MetaEntry meta = 3;
  message MetaEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

```

**Source references:** SRC-0212, SRC-1183  
**URL references:** None independently associated  
**Related findings:** FND-00350, FND-00352

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00352"></a>
## FND-00352: chesscom.api.v1.TwirpError.code = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string code = 2;

### Evidence

- **SRC-0212** `research/proto/chesscom/api/v1/error.proto` — [preserved redacted evidence](../evidence/text/d8ca1402fb62c020bad82173b10d5aed44ad222e7e2dc7c050a1c638fac80188.proto)
  Character offset 134.

```text
roto
// syntax: proto3

package chesscom.api.v1;

message TwirpError {
  optional string msg = 1;
  optional string code = 2;
  repeated .chesscom.api.v1.TwirpError.MetaEntry meta = 3;
  message MetaEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

```

**Source references:** SRC-0212, SRC-1183  
**URL references:** None independently associated  
**Related findings:** FND-00350, FND-00351

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00353"></a>
## FND-00353: chesscom.api.v1.TwirpError.meta = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.api.v1.TwirpError.MetaEntry meta = 3;

### Evidence

- **SRC-0212** `research/proto/chesscom/api/v1/error.proto` — [preserved redacted evidence](../evidence/text/d8ca1402fb62c020bad82173b10d5aed44ad222e7e2dc7c050a1c638fac80188.proto)
  Character offset 162.

```text
age chesscom.api.v1;

message TwirpError {
  optional string msg = 1;
  optional string code = 2;
  repeated .chesscom.api.v1.TwirpError.MetaEntry meta = 3;
  message MetaEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

```

**Source references:** SRC-0212, SRC-1183  
**URL references:** None independently associated  
**Related findings:** FND-00350, FND-00351, FND-00352

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00354"></a>
## FND-00354: message declaration: chesscom.api.v1.TwirpError.MetaEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MetaEntry {

### Evidence

- **SRC-0212** `research/proto/chesscom/api/v1/error.proto` — [preserved redacted evidence](../evidence/text/d8ca1402fb62c020bad82173b10d5aed44ad222e7e2dc7c050a1c638fac80188.proto)
  Character offset 221.

```text
g msg = 1;
  optional string code = 2;
  repeated .chesscom.api.v1.TwirpError.MetaEntry meta = 3;
  message MetaEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

```

**Source references:** SRC-0212, SRC-1183  
**URL references:** None independently associated  
**Related findings:** FND-00350, FND-00351, FND-00352

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00355"></a>
## FND-00355: chesscom.api.v1.TwirpError.MetaEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0212** `research/proto/chesscom/api/v1/error.proto` — [preserved redacted evidence](../evidence/text/d8ca1402fb62c020bad82173b10d5aed44ad222e7e2dc7c050a1c638fac80188.proto)
  Character offset 243.

```text
string code = 2;
  repeated .chesscom.api.v1.TwirpError.MetaEntry meta = 3;
  message MetaEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

```

**Source references:** SRC-0212, SRC-1183  
**URL references:** None independently associated  
**Related findings:** FND-00350, FND-00351, FND-00352

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00356"></a>
## FND-00356: chesscom.api.v1.TwirpError.MetaEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0212** `research/proto/chesscom/api/v1/error.proto` — [preserved redacted evidence](../evidence/text/d8ca1402fb62c020bad82173b10d5aed44ad222e7e2dc7c050a1c638fac80188.proto)
  Character offset 270.

```text
 .chesscom.api.v1.TwirpError.MetaEntry meta = 3;
  message MetaEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

```

**Source references:** SRC-0212, SRC-1183  
**URL references:** None independently associated  
**Related findings:** FND-00350, FND-00351, FND-00352

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00357"></a>
## FND-00357: enum declaration: chesscom.api.v1.ErrorReason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ErrorReason {

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 91.

```text
// source: chesscom/api/v1/error_reason.proto
// syntax: proto3

package chesscom.api.v1;

enum ErrorReason {
  ERROR_REASON_UNSPECIFIED = 0;
  ERROR_REASON_INVALID_INPUT = 1;
  ERROR_REASON_INVALID_CAPTCHA = 12;
  ERROR_REASON_USER_DISABLED = 2;
  ERROR_REASON_USER_NOT_FOUND = 3;
  ERROR_REASON_AUTHENTICATION_INVALID_CHALLENGE = 4;
  ERROR_REASON_AUTHENTICATION_INVALID_VERIFICATION_CODE = 5;
  ERROR_REASON_
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00358"></a>
## FND-00358: chesscom.api.v1.ErrorReason.ERROR_REASON_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_UNSPECIFIED = 0;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 112.

```text
hesscom/api/v1/error_reason.proto
// syntax: proto3

package chesscom.api.v1;

enum ErrorReason {
  ERROR_REASON_UNSPECIFIED = 0;
  ERROR_REASON_INVALID_INPUT = 1;
  ERROR_REASON_INVALID_CAPTCHA = 12;
  ERROR_REASON_USER_DISABLED = 2;
  ERROR_REASON_USER_NOT_FOUND = 3;
  ERROR_REASON_AUTHENTICATION_INVALID_CHALLENGE = 4;
  ERROR_REASON_AUTHENTICATION_INVALID_VERIFICATION_CODE = 5;
  ERROR_REASON_AUTHENTICATION_INVALI
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00359"></a>
## FND-00359: chesscom.api.v1.ErrorReason.ERROR_REASON_INVALID_INPUT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_INVALID_INPUT = 1;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 144.

```text
o
// syntax: proto3

package chesscom.api.v1;

enum ErrorReason {
  ERROR_REASON_UNSPECIFIED = 0;
  ERROR_REASON_INVALID_INPUT = 1;
  ERROR_REASON_INVALID_CAPTCHA = 12;
  ERROR_REASON_USER_DISABLED = 2;
  ERROR_REASON_USER_NOT_FOUND = 3;
  ERROR_REASON_AUTHENTICATION_INVALID_CHALLENGE = 4;
  ERROR_REASON_AUTHENTICATION_INVALID_VERIFICATION_CODE = 5;
  ERROR_REASON_AUTHENTICATION_INVALID_NEW_DEVICE_VERIFICATION_CODE =
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00360"></a>
## FND-00360: chesscom.api.v1.ErrorReason.ERROR_REASON_INVALID_CAPTCHA = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_INVALID_CAPTCHA = 12;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 178.

```text
com.api.v1;

enum ErrorReason {
  ERROR_REASON_UNSPECIFIED = 0;
  ERROR_REASON_INVALID_INPUT = 1;
  ERROR_REASON_INVALID_CAPTCHA = 12;
  ERROR_REASON_USER_DISABLED = 2;
  ERROR_REASON_USER_NOT_FOUND = 3;
  ERROR_REASON_AUTHENTICATION_INVALID_CHALLENGE = 4;
  ERROR_REASON_AUTHENTICATION_INVALID_VERIFICATION_CODE = 5;
  ERROR_REASON_AUTHENTICATION_INVALID_NEW_DEVICE_VERIFICATION_CODE = 54;
  ERROR_REASON_AUTHENTICATION
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00361"></a>
## FND-00361: chesscom.api.v1.ErrorReason.ERROR_REASON_USER_DISABLED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_USER_DISABLED = 2;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 215.

```text
OR_REASON_UNSPECIFIED = 0;
  ERROR_REASON_INVALID_INPUT = 1;
  ERROR_REASON_INVALID_CAPTCHA = 12;
  ERROR_REASON_USER_DISABLED = 2;
  ERROR_REASON_USER_NOT_FOUND = 3;
  ERROR_REASON_AUTHENTICATION_INVALID_CHALLENGE = 4;
  ERROR_REASON_AUTHENTICATION_INVALID_VERIFICATION_CODE = 5;
  ERROR_REASON_AUTHENTICATION_INVALID_NEW_DEVICE_VERIFICATION_CODE = 54;
  ERROR_REASON_AUTHENTICATION_INVALID_OLD_DEVICE_VERIFICATION_CODE
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00362"></a>
## FND-00362: chesscom.api.v1.ErrorReason.ERROR_REASON_USER_NOT_FOUND = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_USER_NOT_FOUND = 3;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 249.

```text
_REASON_INVALID_INPUT = 1;
  ERROR_REASON_INVALID_CAPTCHA = 12;
  ERROR_REASON_USER_DISABLED = 2;
  ERROR_REASON_USER_NOT_FOUND = 3;
  ERROR_REASON_AUTHENTICATION_INVALID_CHALLENGE = 4;
  ERROR_REASON_AUTHENTICATION_INVALID_VERIFICATION_CODE = 5;
  ERROR_REASON_AUTHENTICATION_INVALID_NEW_DEVICE_VERIFICATION_CODE = 54;
  ERROR_REASON_AUTHENTICATION_INVALID_OLD_DEVICE_VERIFICATION_CODE = 55;
  ERROR_REASON_AUTHENTICATI
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00363"></a>
## FND-00363: chesscom.api.v1.ErrorReason.ERROR_REASON_AUTHENTICATION_INVALID_CHALLENGE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_AUTHENTICATION_INVALID_CHALLENGE = 4;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 284.

```text
REASON_INVALID_CAPTCHA = 12;
  ERROR_REASON_USER_DISABLED = 2;
  ERROR_REASON_USER_NOT_FOUND = 3;
  ERROR_REASON_AUTHENTICATION_INVALID_CHALLENGE = 4;
  ERROR_REASON_AUTHENTICATION_INVALID_VERIFICATION_CODE = 5;
  ERROR_REASON_AUTHENTICATION_INVALID_NEW_DEVICE_VERIFICATION_CODE = 54;
  ERROR_REASON_AUTHENTICATION_INVALID_OLD_DEVICE_VERIFICATION_CODE = 55;
  ERROR_REASON_AUTHENTICATION_VERIFICATION_FAILED = 6;
  ERROR
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00364"></a>
## FND-00364: chesscom.api.v1.ErrorReason.ERROR_REASON_AUTHENTICATION_INVALID_VERIFICATION_CODE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_AUTHENTICATION_INVALID_VERIFICATION_CODE = 5;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 337.

```text
BLED = 2;
  ERROR_REASON_USER_NOT_FOUND = 3;
  ERROR_REASON_AUTHENTICATION_INVALID_CHALLENGE = 4;
  ERROR_REASON_AUTHENTICATION_INVALID_VERIFICATION_CODE = 5;
  ERROR_REASON_AUTHENTICATION_INVALID_NEW_DEVICE_VERIFICATION_CODE = 54;
  ERROR_REASON_AUTHENTICATION_INVALID_OLD_DEVICE_VERIFICATION_CODE = 55;
  ERROR_REASON_AUTHENTICATION_VERIFICATION_FAILED = 6;
  ERROR_REASON_AUTHENTICATION_VERIFICATION_BLOCKED = 47;
  E
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00365"></a>
## FND-00365: chesscom.api.v1.ErrorReason.ERROR_REASON_AUTHENTICATION_INVALID_NEW_DEVICE_VERIFICATION_CODE = 54

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_AUTHENTICATION_INVALID_NEW_DEVICE_VERIFICATION_CODE = 54;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 398.

```text
UTHENTICATION_INVALID_CHALLENGE = 4;
  ERROR_REASON_AUTHENTICATION_INVALID_VERIFICATION_CODE = 5;
  ERROR_REASON_AUTHENTICATION_INVALID_NEW_DEVICE_VERIFICATION_CODE = 54;
  ERROR_REASON_AUTHENTICATION_INVALID_OLD_DEVICE_VERIFICATION_CODE = 55;
  ERROR_REASON_AUTHENTICATION_VERIFICATION_FAILED = 6;
  ERROR_REASON_AUTHENTICATION_VERIFICATION_BLOCKED = 47;
  ERROR_REASON_PHONE_NUMBER_UPDATE_LIMIT_REACHED = 7;
  ERROR_RE
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00366"></a>
## FND-00366: chesscom.api.v1.ErrorReason.ERROR_REASON_AUTHENTICATION_INVALID_OLD_DEVICE_VERIFICATION_CODE = 55

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_AUTHENTICATION_INVALID_OLD_DEVICE_VERIFICATION_CODE = 55;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 471.

```text
D_VERIFICATION_CODE = 5;
  ERROR_REASON_AUTHENTICATION_INVALID_NEW_DEVICE_VERIFICATION_CODE = 54;
  ERROR_REASON_AUTHENTICATION_INVALID_OLD_DEVICE_VERIFICATION_CODE = 55;
  ERROR_REASON_AUTHENTICATION_VERIFICATION_FAILED = 6;
  ERROR_REASON_AUTHENTICATION_VERIFICATION_BLOCKED = 47;
  ERROR_REASON_PHONE_NUMBER_UPDATE_LIMIT_REACHED = 7;
  ERROR_REASON_PHONE_NUMBER_UPDATE_MUST_BE_DIFFERENT = 8;
  ERROR_REASON_PHONE_NUMB
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00367"></a>
## FND-00367: chesscom.api.v1.ErrorReason.ERROR_REASON_AUTHENTICATION_VERIFICATION_FAILED = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_AUTHENTICATION_VERIFICATION_FAILED = 6;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 544.

```text
_VERIFICATION_CODE = 54;
  ERROR_REASON_AUTHENTICATION_INVALID_OLD_DEVICE_VERIFICATION_CODE = 55;
  ERROR_REASON_AUTHENTICATION_VERIFICATION_FAILED = 6;
  ERROR_REASON_AUTHENTICATION_VERIFICATION_BLOCKED = 47;
  ERROR_REASON_PHONE_NUMBER_UPDATE_LIMIT_REACHED = 7;
  ERROR_REASON_PHONE_NUMBER_UPDATE_MUST_BE_DIFFERENT = 8;
  ERROR_REASON_PHONE_NUMBER_ALREADY_IN_USE = 9;
  ERROR_REASON_PHONE_NUMBER_REMOVE_NO_LOGIN_OPTION
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00368"></a>
## FND-00368: chesscom.api.v1.ErrorReason.ERROR_REASON_AUTHENTICATION_VERIFICATION_BLOCKED = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_AUTHENTICATION_VERIFICATION_BLOCKED = 47;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 599.

```text
INVALID_OLD_DEVICE_VERIFICATION_CODE = 55;
  ERROR_REASON_AUTHENTICATION_VERIFICATION_FAILED = 6;
  ERROR_REASON_AUTHENTICATION_VERIFICATION_BLOCKED = 47;
  ERROR_REASON_PHONE_NUMBER_UPDATE_LIMIT_REACHED = 7;
  ERROR_REASON_PHONE_NUMBER_UPDATE_MUST_BE_DIFFERENT = 8;
  ERROR_REASON_PHONE_NUMBER_ALREADY_IN_USE = 9;
  ERROR_REASON_PHONE_NUMBER_REMOVE_NO_LOGIN_OPTIONS = 10;
  ERROR_REASON_PHONE_NUMBER_ACCOUNT_RECOVERY_LI
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00369"></a>
## FND-00369: chesscom.api.v1.ErrorReason.ERROR_REASON_PHONE_NUMBER_UPDATE_LIMIT_REACHED = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_PHONE_NUMBER_UPDATE_LIMIT_REACHED = 7;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 656.

```text
_AUTHENTICATION_VERIFICATION_FAILED = 6;
  ERROR_REASON_AUTHENTICATION_VERIFICATION_BLOCKED = 47;
  ERROR_REASON_PHONE_NUMBER_UPDATE_LIMIT_REACHED = 7;
  ERROR_REASON_PHONE_NUMBER_UPDATE_MUST_BE_DIFFERENT = 8;
  ERROR_REASON_PHONE_NUMBER_ALREADY_IN_USE = 9;
  ERROR_REASON_PHONE_NUMBER_REMOVE_NO_LOGIN_OPTIONS = 10;
  ERROR_REASON_PHONE_NUMBER_ACCOUNT_RECOVERY_LIMIT_REACHED = 11;
  ERROR_REASON_PHONE_NUMBER_INVALID_TYP
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00370"></a>
## FND-00370: chesscom.api.v1.ErrorReason.ERROR_REASON_PHONE_NUMBER_UPDATE_MUST_BE_DIFFERENT = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_PHONE_NUMBER_UPDATE_MUST_BE_DIFFERENT = 8;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 710.

```text
N_AUTHENTICATION_VERIFICATION_BLOCKED = 47;
  ERROR_REASON_PHONE_NUMBER_UPDATE_LIMIT_REACHED = 7;
  ERROR_REASON_PHONE_NUMBER_UPDATE_MUST_BE_DIFFERENT = 8;
  ERROR_REASON_PHONE_NUMBER_ALREADY_IN_USE = 9;
  ERROR_REASON_PHONE_NUMBER_REMOVE_NO_LOGIN_OPTIONS = 10;
  ERROR_REASON_PHONE_NUMBER_ACCOUNT_RECOVERY_LIMIT_REACHED = 11;
  ERROR_REASON_PHONE_NUMBER_INVALID_TYPE = 13;
  ERROR_REASON_PHONE_NUMBER_INVALID = 21;
  ER
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00371"></a>
## FND-00371: chesscom.api.v1.ErrorReason.ERROR_REASON_PHONE_NUMBER_ALREADY_IN_USE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_PHONE_NUMBER_ALREADY_IN_USE = 9;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 768.

```text
_PHONE_NUMBER_UPDATE_LIMIT_REACHED = 7;
  ERROR_REASON_PHONE_NUMBER_UPDATE_MUST_BE_DIFFERENT = 8;
  ERROR_REASON_PHONE_NUMBER_ALREADY_IN_USE = 9;
  ERROR_REASON_PHONE_NUMBER_REMOVE_NO_LOGIN_OPTIONS = 10;
  ERROR_REASON_PHONE_NUMBER_ACCOUNT_RECOVERY_LIMIT_REACHED = 11;
  ERROR_REASON_PHONE_NUMBER_INVALID_TYPE = 13;
  ERROR_REASON_PHONE_NUMBER_INVALID = 21;
  ERROR_REASON_PHONE_NUMBER_UNSUPPORTED_COUNTRY = 22;
  ERROR_
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00372"></a>
## FND-00372: chesscom.api.v1.ErrorReason.ERROR_REASON_PHONE_NUMBER_REMOVE_NO_LOGIN_OPTIONS = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_PHONE_NUMBER_REMOVE_NO_LOGIN_OPTIONS = 10;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 816.

```text
REASON_PHONE_NUMBER_UPDATE_MUST_BE_DIFFERENT = 8;
  ERROR_REASON_PHONE_NUMBER_ALREADY_IN_USE = 9;
  ERROR_REASON_PHONE_NUMBER_REMOVE_NO_LOGIN_OPTIONS = 10;
  ERROR_REASON_PHONE_NUMBER_ACCOUNT_RECOVERY_LIMIT_REACHED = 11;
  ERROR_REASON_PHONE_NUMBER_INVALID_TYPE = 13;
  ERROR_REASON_PHONE_NUMBER_INVALID = 21;
  ERROR_REASON_PHONE_NUMBER_UNSUPPORTED_COUNTRY = 22;
  ERROR_REASON_PHONE_NUMBER_MISSING = 25;
  ERROR_REASON
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00373"></a>
## FND-00373: chesscom.api.v1.ErrorReason.ERROR_REASON_PHONE_NUMBER_ACCOUNT_RECOVERY_LIMIT_REACHED = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_PHONE_NUMBER_ACCOUNT_RECOVERY_LIMIT_REACHED = 11;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 874.

```text
REASON_PHONE_NUMBER_ALREADY_IN_USE = 9;
  ERROR_REASON_PHONE_NUMBER_REMOVE_NO_LOGIN_OPTIONS = 10;
  ERROR_REASON_PHONE_NUMBER_ACCOUNT_RECOVERY_LIMIT_REACHED = 11;
  ERROR_REASON_PHONE_NUMBER_INVALID_TYPE = 13;
  ERROR_REASON_PHONE_NUMBER_INVALID = 21;
  ERROR_REASON_PHONE_NUMBER_UNSUPPORTED_COUNTRY = 22;
  ERROR_REASON_PHONE_NUMBER_MISSING = 25;
  ERROR_REASON_PHONE_NUMBER_VERIFICATION_LIMIT_REACHED = 45;
  ERROR_REA
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00374"></a>
## FND-00374: chesscom.api.v1.ErrorReason.ERROR_REASON_PHONE_NUMBER_INVALID_TYPE = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_PHONE_NUMBER_INVALID_TYPE = 13;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 939.

```text
ER_REMOVE_NO_LOGIN_OPTIONS = 10;
  ERROR_REASON_PHONE_NUMBER_ACCOUNT_RECOVERY_LIMIT_REACHED = 11;
  ERROR_REASON_PHONE_NUMBER_INVALID_TYPE = 13;
  ERROR_REASON_PHONE_NUMBER_INVALID = 21;
  ERROR_REASON_PHONE_NUMBER_UNSUPPORTED_COUNTRY = 22;
  ERROR_REASON_PHONE_NUMBER_MISSING = 25;
  ERROR_REASON_PHONE_NUMBER_VERIFICATION_LIMIT_REACHED = 45;
  ERROR_REASON_PHONE_NUMBER_FRAUDULENT_ACTIVITY = 48;
  ERROR_REASON_PHONE_N
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
