# data_models — findings 5401–5500

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-05675"></a>
## FND-05675: chesscom.game_storage.v1.GameResult.GAME_RESULT_DRAW_BY_AGREEMENT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_DRAW_BY_AGREEMENT = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2435.

```text
CKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05676"></a>
## FND-05676: chesscom.game_storage.v1.GameResult.GAME_RESULT_DRAW_BY_REPETITION = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_DRAW_BY_REPETITION = 6;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2472.

```text
_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_W
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05677"></a>
## FND-05677: chesscom.game_storage.v1.GameResult.GAME_RESULT_DRAW_BY_STALEMATE = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_DRAW_BY_STALEMATE = 7;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2510.

```text
SE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RE
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05678"></a>
## FND-05678: chesscom.game_storage.v1.GameResult.GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2547.

```text
DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 1
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05679"></a>
## FND-05679: chesscom.game_storage.v1.GameResult.GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2596.

```text
TITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05680"></a>
## FND-05680: chesscom.game_storage.v1.GameResult.GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2656.

```text
LT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

enum PlayerProvider {
  PLAYER_PROVIDER_UNSPECIFIED = 0;
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05681"></a>
## FND-05681: chesscom.game_storage.v1.GameResult.GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2697.

```text
AME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

enum PlayerProvider {
  PLAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYE
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05682"></a>
## FND-05682: chesscom.game_storage.v1.GameResult.GAME_RESULT_ABORTED = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_ABORTED = 12;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2751.

```text
9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

enum PlayerProvider {
  PLAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;

```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05683"></a>
## FND-05683: chesscom.game_storage.v1.GameResult.GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2779.

```text
MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

enum PlayerProvider {
  PLAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_OR
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05684"></a>
## FND-05684: chesscom.game_storage.v1.GameResult.GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2823.

```text
GHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

enum PlayerProvider {
  PLAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PL
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05685"></a>
## FND-05685: chesscom.game_storage.v1.GameResult.GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2872.

```text
 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

enum PlayerProvider {
  PLAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

enum Playe
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05686"></a>
## FND-05686: enum declaration: chesscom.game_storage.v1.PlayerProvider

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayerProvider {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2920.

```text

  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

enum PlayerProvider {
  PLAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYE
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05687"></a>
## FND-05687: chesscom.game_storage.v1.PlayerProvider.PLAYER_PROVIDER_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_PROVIDER_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2944.

```text
BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

enum PlayerProvider {
  PLAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYE
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05688"></a>
## FND-05688: chesscom.game_storage.v1.PlayerProvider.PLAYER_PROVIDER_CHESS_COM = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_PROVIDER_CHESS_COM = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2979.

```text
SULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

enum PlayerProvider {
  PLAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05689"></a>
## FND-05689: chesscom.game_storage.v1.PlayerProvider.PLAYER_PROVIDER_CHESS_KID = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_PROVIDER_CHESS_KID = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3012.

```text
 15;
}

enum PlayerProvider {
  PLAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLA
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05690"></a>
## FND-05690: chesscom.game_storage.v1.PlayerProvider.PLAYER_PROVIDER_FIDE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_PROVIDER_FIDE = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3045.

```text
LAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05691"></a>
## FND-05691: chesscom.game_storage.v1.PlayerProvider.PLAYER_PROVIDER_LICHESS_ORG = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_PROVIDER_LICHESS_ORG = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3073.

```text
 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05692"></a>
## FND-05692: chesscom.game_storage.v1.PlayerProvider.PLAYER_PROVIDER_CHESSBASE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_PROVIDER_CHESSBASE = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3108.

```text
;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYE
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05693"></a>
## FND-05693: chesscom.game_storage.v1.PlayerProvider.PLAYER_PROVIDER_CHESS_COM_MASTER = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_PROVIDER_CHESS_COM_MASTER = 6;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3141.

```text
;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05694"></a>
## FND-05694: enum declaration: chesscom.game_storage.v1.PlayerTitle

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayerTitle {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3182.

```text
OVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum Pl
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05695"></a>
## FND-05695: chesscom.game_storage.v1.PlayerTitle.PLAYER_TITLE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3203.

```text
4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_T
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05696"></a>
## FND-05696: chesscom.game_storage.v1.PlayerTitle.PLAYER_TITLE_WGM = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_WGM = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3235.

```text
 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TY
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05697"></a>
## FND-05697: chesscom.game_storage.v1.PlayerTitle.PLAYER_TITLE_GM = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_GM = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3259.

```text
ESS_COM_MASTER = 6;
}

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_T
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05698"></a>
## FND-05698: chesscom.game_storage.v1.PlayerTitle.PLAYER_TITLE_WIM = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_WIM = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3282.

```text
enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLA
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05699"></a>
## FND-05699: chesscom.game_storage.v1.PlayerTitle.PLAYER_TITLE_IM = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_IM = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3306.

```text
YER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}


```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05700"></a>
## FND-05700: chesscom.game_storage.v1.PlayerTitle.PLAYER_TITLE_WFM = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_WFM = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3329.

```text
 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBeha
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05701"></a>
## FND-05701: chesscom.game_storage.v1.PlayerTitle.PLAYER_TITLE_FM = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_FM = 6;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3353.

```text
 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPOR
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05702"></a>
## FND-05702: chesscom.game_storage.v1.PlayerTitle.PLAYER_TITLE_WNM = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_WNM = 7;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3376.

```text
 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05703"></a>
## FND-05703: chesscom.game_storage.v1.PlayerTitle.PLAYER_TITLE_NM = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_NM = 8;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3400.

```text
 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05704"></a>
## FND-05704: chesscom.game_storage.v1.PlayerTitle.PLAYER_TITLE_M = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_M = 9;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3423.

```text
 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PL
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05705"></a>
## FND-05705: chesscom.game_storage.v1.PlayerTitle.PLAYER_TITLE_CM = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_CM = 10;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3445.

```text
 = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIO
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05706"></a>
## FND-05706: chesscom.game_storage.v1.PlayerTitle.PLAYER_TITLE_WCM = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_WCM = 11;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3469.

```text
= 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05707"></a>
## FND-05707: enum declaration: chesscom.game_storage.v1.PlayerType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayerType {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3495.

```text
7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BE
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05708"></a>
## FND-05708: chesscom.game_storage.v1.PlayerType.PLAYER_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3515.

```text
 = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05709"></a>
## FND-05709: chesscom.game_storage.v1.PlayerType.PLAYER_TYPE_HUMAN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TYPE_HUMAN = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3546.

```text
LAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCO
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05710"></a>
## FND-05710: chesscom.game_storage.v1.PlayerType.PLAYER_TYPE_COMPUTER = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TYPE_COMPUTER = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3571.

```text
AYER_TITLE_WCM = 11;
}

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_S
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05711"></a>
## FND-05711: chesscom.game_storage.v1.PlayerType.PLAYER_TYPE_CYBORG = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TYPE_CYBORG = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3599.

```text
 PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05712"></a>
## FND-05712: enum declaration: chesscom.game_storage.v1.PlayerBadSportBehavior

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayerBadSportBehavior {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3626.

```text
_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIO
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05713"></a>
## FND-05713: chesscom.game_storage.v1.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3658.

```text
HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05714"></a>
## FND-05714: chesscom.game_storage.v1.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3703.

```text
ER_TYPE_CYBORG = 3;
}

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05715"></a>
## FND-05715: chesscom.game_storage.v1.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3741.

```text
portBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;
}

enum VsComputerGameMode {
  VS
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05716"></a>
## FND-05716: chesscom.game_storage.v1.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3796.

```text
= 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;
}

enum VsComputerGameMode {
  VS_COMPUTER_GAME_MODE_UNSPECIFIED = 0;
  VS_COMPUTER_GAME
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05717"></a>
## FND-05717: chesscom.game_storage.v1.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3835.

```text
 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;
}

enum VsComputerGameMode {
  VS_COMPUTER_GAME_MODE_UNSPECIFIED = 0;
  VS_COMPUTER_GAME_MODE_CHALLENGE = 1;
  VS_COMPUTER_GAME
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05718"></a>
## FND-05718: chesscom.game_storage.v1.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3879.

```text
OT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;
}

enum VsComputerGameMode {
  VS_COMPUTER_GAME_MODE_UNSPECIFIED = 0;
  VS_COMPUTER_GAME_MODE_CHALLENGE = 1;
  VS_COMPUTER_GAME_MODE_FRIENDLY = 2;
  VS_COMPUTER_GAME_MODE_
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05719"></a>
## FND-05719: chesscom.game_storage.v1.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3922.

```text
ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;
}

enum VsComputerGameMode {
  VS_COMPUTER_GAME_MODE_UNSPECIFIED = 0;
  VS_COMPUTER_GAME_MODE_CHALLENGE = 1;
  VS_COMPUTER_GAME_MODE_FRIENDLY = 2;
  VS_COMPUTER_GAME_MODE_ASSISTED = 3;
  VS_COMPUTER_GAME_MODE_CUSTO
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05720"></a>
## FND-05720: chesscom.game_storage.v1.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 3971.

```text
 = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;
}

enum VsComputerGameMode {
  VS_COMPUTER_GAME_MODE_UNSPECIFIED = 0;
  VS_COMPUTER_GAME_MODE_CHALLENGE = 1;
  VS_COMPUTER_GAME_MODE_FRIENDLY = 2;
  VS_COMPUTER_GAME_MODE_ASSISTED = 3;
  VS_COMPUTER_GAME_MODE_CUSTOM = 4;
}

enum PlayMode {
  PLAY_MODE_UNSPECIFIED
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05721"></a>
## FND-05721: enum declaration: chesscom.game_storage.v1.VsComputerGameMode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum VsComputerGameMode {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4031.

```text
D_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;
}

enum VsComputerGameMode {
  VS_COMPUTER_GAME_MODE_UNSPECIFIED = 0;
  VS_COMPUTER_GAME_MODE_CHALLENGE = 1;
  VS_COMPUTER_GAME_MODE_FRIENDLY = 2;
  VS_COMPUTER_GAME_MODE_ASSISTED = 3;
  VS_COMPUTER_GAME_MODE_CUSTOM = 4;
}

enum PlayMode {
  PLAY_MODE_UNSPECIFIED = 0;
  PLAY_MODE_LIVE = 1;
  PLAY_MODE_DAILY = 2;
  PLAY_MO
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05722"></a>
## FND-05722: chesscom.game_storage.v1.VsComputerGameMode.VS_COMPUTER_GAME_MODE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VS_COMPUTER_GAME_MODE_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4059.

```text
AYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;
}

enum VsComputerGameMode {
  VS_COMPUTER_GAME_MODE_UNSPECIFIED = 0;
  VS_COMPUTER_GAME_MODE_CHALLENGE = 1;
  VS_COMPUTER_GAME_MODE_FRIENDLY = 2;
  VS_COMPUTER_GAME_MODE_ASSISTED = 3;
  VS_COMPUTER_GAME_MODE_CUSTOM = 4;
}

enum PlayMode {
  PLAY_MODE_UNSPECIFIED = 0;
  PLAY_MODE_LIVE = 1;
  PLAY_MODE_DAILY = 2;
  PLAY_MODE_VS_COMPUTER = 3;
}

messa
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05723"></a>
## FND-05723: chesscom.game_storage.v1.VsComputerGameMode.VS_COMPUTER_GAME_MODE_CHALLENGE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VS_COMPUTER_GAME_MODE_CHALLENGE = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4100.

```text
H_PLAYERS_DISCONNECTED = 7;
}

enum VsComputerGameMode {
  VS_COMPUTER_GAME_MODE_UNSPECIFIED = 0;
  VS_COMPUTER_GAME_MODE_CHALLENGE = 1;
  VS_COMPUTER_GAME_MODE_FRIENDLY = 2;
  VS_COMPUTER_GAME_MODE_ASSISTED = 3;
  VS_COMPUTER_GAME_MODE_CUSTOM = 4;
}

enum PlayMode {
  PLAY_MODE_UNSPECIFIED = 0;
  PLAY_MODE_LIVE = 1;
  PLAY_MODE_DAILY = 2;
  PLAY_MODE_VS_COMPUTER = 3;
}

message GameStored {
  oneof game {
  .chessco
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05724"></a>
## FND-05724: chesscom.game_storage.v1.VsComputerGameMode.VS_COMPUTER_GAME_MODE_FRIENDLY = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VS_COMPUTER_GAME_MODE_FRIENDLY = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4139.

```text
omputerGameMode {
  VS_COMPUTER_GAME_MODE_UNSPECIFIED = 0;
  VS_COMPUTER_GAME_MODE_CHALLENGE = 1;
  VS_COMPUTER_GAME_MODE_FRIENDLY = 2;
  VS_COMPUTER_GAME_MODE_ASSISTED = 3;
  VS_COMPUTER_GAME_MODE_CUSTOM = 4;
}

enum PlayMode {
  PLAY_MODE_UNSPECIFIED = 0;
  PLAY_MODE_LIVE = 1;
  PLAY_MODE_DAILY = 2;
  PLAY_MODE_VS_COMPUTER = 3;
}

message GameStored {
  oneof game {
  .chesscom.game_storage.v1.ChessGame chess_game 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05725"></a>
## FND-05725: chesscom.game_storage.v1.VsComputerGameMode.VS_COMPUTER_GAME_MODE_ASSISTED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VS_COMPUTER_GAME_MODE_ASSISTED = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4177.

```text
ODE_UNSPECIFIED = 0;
  VS_COMPUTER_GAME_MODE_CHALLENGE = 1;
  VS_COMPUTER_GAME_MODE_FRIENDLY = 2;
  VS_COMPUTER_GAME_MODE_ASSISTED = 3;
  VS_COMPUTER_GAME_MODE_CUSTOM = 4;
}

enum PlayMode {
  PLAY_MODE_UNSPECIFIED = 0;
  PLAY_MODE_LIVE = 1;
  PLAY_MODE_DAILY = 2;
  PLAY_MODE_VS_COMPUTER = 3;
}

message GameStored {
  oneof game {
  .chesscom.game_storage.v1.ChessGame chess_game = 30;
  .chesscom.game_storage.v1.Bugh
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05726"></a>
## FND-05726: chesscom.game_storage.v1.VsComputerGameMode.VS_COMPUTER_GAME_MODE_CUSTOM = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VS_COMPUTER_GAME_MODE_CUSTOM = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4215.

```text
E_MODE_CHALLENGE = 1;
  VS_COMPUTER_GAME_MODE_FRIENDLY = 2;
  VS_COMPUTER_GAME_MODE_ASSISTED = 3;
  VS_COMPUTER_GAME_MODE_CUSTOM = 4;
}

enum PlayMode {
  PLAY_MODE_UNSPECIFIED = 0;
  PLAY_MODE_LIVE = 1;
  PLAY_MODE_DAILY = 2;
  PLAY_MODE_VS_COMPUTER = 3;
}

message GameStored {
  oneof game {
  .chesscom.game_storage.v1.ChessGame chess_game = 30;
  .chesscom.game_storage.v1.BughouseGame bughouse_game = 31;
  .chessc
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05727"></a>
## FND-05727: enum declaration: chesscom.game_storage.v1.PlayMode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayMode {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4252.

```text
AME_MODE_FRIENDLY = 2;
  VS_COMPUTER_GAME_MODE_ASSISTED = 3;
  VS_COMPUTER_GAME_MODE_CUSTOM = 4;
}

enum PlayMode {
  PLAY_MODE_UNSPECIFIED = 0;
  PLAY_MODE_LIVE = 1;
  PLAY_MODE_DAILY = 2;
  PLAY_MODE_VS_COMPUTER = 3;
}

message GameStored {
  oneof game {
  .chesscom.game_storage.v1.ChessGame chess_game = 30;
  .chesscom.game_storage.v1.BughouseGame bughouse_game = 31;
  .chesscom.game_storage.v1.VariantGame varian
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05728"></a>
## FND-05728: chesscom.game_storage.v1.PlayMode.PLAY_MODE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_MODE_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4270.

```text
= 2;
  VS_COMPUTER_GAME_MODE_ASSISTED = 3;
  VS_COMPUTER_GAME_MODE_CUSTOM = 4;
}

enum PlayMode {
  PLAY_MODE_UNSPECIFIED = 0;
  PLAY_MODE_LIVE = 1;
  PLAY_MODE_DAILY = 2;
  PLAY_MODE_VS_COMPUTER = 3;
}

message GameStored {
  oneof game {
  .chesscom.game_storage.v1.ChessGame chess_game = 30;
  .chesscom.game_storage.v1.BughouseGame bughouse_game = 31;
  .chesscom.game_storage.v1.VariantGame variant_game = 32;
  }
 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05729"></a>
## FND-05729: chesscom.game_storage.v1.PlayMode.PLAY_MODE_LIVE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_MODE_LIVE = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4299.

```text
ASSISTED = 3;
  VS_COMPUTER_GAME_MODE_CUSTOM = 4;
}

enum PlayMode {
  PLAY_MODE_UNSPECIFIED = 0;
  PLAY_MODE_LIVE = 1;
  PLAY_MODE_DAILY = 2;
  PLAY_MODE_VS_COMPUTER = 3;
}

message GameStored {
  oneof game {
  .chesscom.game_storage.v1.ChessGame chess_game = 30;
  .chesscom.game_storage.v1.BughouseGame bughouse_game = 31;
  .chesscom.game_storage.v1.VariantGame variant_game = 32;
  }
  oneof _legacy_id {
  uint64 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05730"></a>
## FND-05730: chesscom.game_storage.v1.PlayMode.PLAY_MODE_DAILY = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_MODE_DAILY = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4321.

```text
PUTER_GAME_MODE_CUSTOM = 4;
}

enum PlayMode {
  PLAY_MODE_UNSPECIFIED = 0;
  PLAY_MODE_LIVE = 1;
  PLAY_MODE_DAILY = 2;
  PLAY_MODE_VS_COMPUTER = 3;
}

message GameStored {
  oneof game {
  .chesscom.game_storage.v1.ChessGame chess_game = 30;
  .chesscom.game_storage.v1.BughouseGame bughouse_game = 31;
  .chesscom.game_storage.v1.VariantGame variant_game = 32;
  }
  oneof _legacy_id {
  uint64 legacy_id = 33;
  }
  
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05731"></a>
## FND-05731: chesscom.game_storage.v1.PlayMode.PLAY_MODE_VS_COMPUTER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_MODE_VS_COMPUTER = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4344.

```text
= 4;
}

enum PlayMode {
  PLAY_MODE_UNSPECIFIED = 0;
  PLAY_MODE_LIVE = 1;
  PLAY_MODE_DAILY = 2;
  PLAY_MODE_VS_COMPUTER = 3;
}

message GameStored {
  oneof game {
  .chesscom.game_storage.v1.ChessGame chess_game = 30;
  .chesscom.game_storage.v1.BughouseGame bughouse_game = 31;
  .chesscom.game_storage.v1.VariantGame variant_game = 32;
  }
  oneof _legacy_id {
  uint64 legacy_id = 33;
  }
  oneof _vs_computer_game
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05732"></a>
## FND-05732: message declaration: chesscom.game_storage.v1.GameStored

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameStored {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4374.

```text
_MODE_UNSPECIFIED = 0;
  PLAY_MODE_LIVE = 1;
  PLAY_MODE_DAILY = 2;
  PLAY_MODE_VS_COMPUTER = 3;
}

message GameStored {
  oneof game {
  .chesscom.game_storage.v1.ChessGame chess_game = 30;
  .chesscom.game_storage.v1.BughouseGame bughouse_game = 31;
  .chesscom.game_storage.v1.VariantGame variant_game = 32;
  }
  oneof _legacy_id {
  uint64 legacy_id = 33;
  }
  oneof _vs_computer_game_mode {
  .chesscom.game_stora
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05733"></a>
## FND-05733: oneof declaration: chesscom.game_storage.v1.GameStored.game

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof game {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4397.

```text
  PLAY_MODE_LIVE = 1;
  PLAY_MODE_DAILY = 2;
  PLAY_MODE_VS_COMPUTER = 3;
}

message GameStored {
  oneof game {
  .chesscom.game_storage.v1.ChessGame chess_game = 30;
  .chesscom.game_storage.v1.BughouseGame bughouse_game = 31;
  .chesscom.game_storage.v1.VariantGame variant_game = 32;
  }
  oneof _legacy_id {
  uint64 legacy_id = 33;
  }
  oneof _vs_computer_game_mode {
  .chesscom.game_storage.v1.VsComputerGameMod
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05734"></a>
## FND-05734: chesscom.game_storage.v1.GameStored.chess_game = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_storage.v1.ChessGame chess_game = 30;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4412.

```text
E = 1;
  PLAY_MODE_DAILY = 2;
  PLAY_MODE_VS_COMPUTER = 3;
}

message GameStored {
  oneof game {
  .chesscom.game_storage.v1.ChessGame chess_game = 30;
  .chesscom.game_storage.v1.BughouseGame bughouse_game = 31;
  .chesscom.game_storage.v1.VariantGame variant_game = 32;
  }
  oneof _legacy_id {
  uint64 legacy_id = 33;
  }
  oneof _vs_computer_game_mode {
  .chesscom.game_storage.v1.VsComputerGameMode vs_computer_g
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05735"></a>
## FND-05735: chesscom.game_storage.v1.GameStored.bughouse_game = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_storage.v1.BughouseGame bughouse_game = 31;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4467.

```text
 3;
}

message GameStored {
  oneof game {
  .chesscom.game_storage.v1.ChessGame chess_game = 30;
  .chesscom.game_storage.v1.BughouseGame bughouse_game = 31;
  .chesscom.game_storage.v1.VariantGame variant_game = 32;
  }
  oneof _legacy_id {
  uint64 legacy_id = 33;
  }
  oneof _vs_computer_game_mode {
  .chesscom.game_storage.v1.VsComputerGameMode vs_computer_game_mode = 34;
  }
  oneof _vs_coach_game_data {
  .che
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05736"></a>
## FND-05736: chesscom.game_storage.v1.GameStored.variant_game = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_storage.v1.VariantGame variant_game = 32;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4528.

```text
torage.v1.ChessGame chess_game = 30;
  .chesscom.game_storage.v1.BughouseGame bughouse_game = 31;
  .chesscom.game_storage.v1.VariantGame variant_game = 32;
  }
  oneof _legacy_id {
  uint64 legacy_id = 33;
  }
  oneof _vs_computer_game_mode {
  .chesscom.game_storage.v1.VsComputerGameMode vs_computer_game_mode = 34;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v1.VsCoachGameData vs_coach_game_data = 35
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05737"></a>
## FND-05737: oneof declaration: chesscom.game_storage.v1.GameStored._legacy_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _legacy_id {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4591.

```text
1.BughouseGame bughouse_game = 31;
  .chesscom.game_storage.v1.VariantGame variant_game = 32;
  }
  oneof _legacy_id {
  uint64 legacy_id = 33;
  }
  oneof _vs_computer_game_mode {
  .chesscom.game_storage.v1.VsComputerGameMode vs_computer_game_mode = 34;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v1.VsCoachGameData vs_coach_game_data = 35;
  }
  optional string internal_key = 1;
  optional .chesscom.
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05738"></a>
## FND-05738: chesscom.game_storage.v1.GameStored.legacy_id = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint64 legacy_id = 33;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4612.

```text
se_game = 31;
  .chesscom.game_storage.v1.VariantGame variant_game = 32;
  }
  oneof _legacy_id {
  uint64 legacy_id = 33;
  }
  oneof _vs_computer_game_mode {
  .chesscom.game_storage.v1.VsComputerGameMode vs_computer_game_mode = 34;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v1.VsCoachGameData vs_coach_game_data = 35;
  }
  optional string internal_key = 1;
  optional .chesscom.game_storage.v1.GameP
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05739"></a>
## FND-05739: oneof declaration: chesscom.game_storage.v1.GameStored._vs_computer_game_mode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _vs_computer_game_mode {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4641.

```text
e_storage.v1.VariantGame variant_game = 32;
  }
  oneof _legacy_id {
  uint64 legacy_id = 33;
  }
  oneof _vs_computer_game_mode {
  .chesscom.game_storage.v1.VsComputerGameMode vs_computer_game_mode = 34;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v1.VsCoachGameData vs_coach_game_data = 35;
  }
  optional string internal_key = 1;
  optional .chesscom.game_storage.v1.GameProvider provider = 2;
  optio
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05740"></a>
## FND-05740: chesscom.game_storage.v1.GameStored.vs_computer_game_mode = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_storage.v1.VsComputerGameMode vs_computer_game_mode = 34;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4674.

```text
game = 32;
  }
  oneof _legacy_id {
  uint64 legacy_id = 33;
  }
  oneof _vs_computer_game_mode {
  .chesscom.game_storage.v1.VsComputerGameMode vs_computer_game_mode = 34;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v1.VsCoachGameData vs_coach_game_data = 35;
  }
  optional string internal_key = 1;
  optional .chesscom.game_storage.v1.GameProvider provider = 2;
  optional string key = 3;
  optional .g
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05741"></a>
## FND-05741: oneof declaration: chesscom.game_storage.v1.GameStored._vs_coach_game_data

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _vs_coach_game_data {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4753.

```text
mputer_game_mode {
  .chesscom.game_storage.v1.VsComputerGameMode vs_computer_game_mode = 34;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v1.VsCoachGameData vs_coach_game_data = 35;
  }
  optional string internal_key = 1;
  optional .chesscom.game_storage.v1.GameProvider provider = 2;
  optional string key = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05742"></a>
## FND-05742: chesscom.game_storage.v1.GameStored.vs_coach_game_data = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_storage.v1.VsCoachGameData vs_coach_game_data = 35;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4783.

```text
.game_storage.v1.VsComputerGameMode vs_computer_game_mode = 34;
  }
  oneof _vs_coach_game_data {
  .chesscom.game_storage.v1.VsCoachGameData vs_coach_game_data = 35;
  }
  optional string internal_key = 1;
  optional .chesscom.game_storage.v1.GameProvider provider = 2;
  optional string key = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp started_at = 5;
  optional .go
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05743"></a>
## FND-05743: chesscom.game_storage.v1.GameStored.internal_key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string internal_key = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4856.

```text
of _vs_coach_game_data {
  .chesscom.game_storage.v1.VsCoachGameData vs_coach_game_data = 35;
  }
  optional string internal_key = 1;
  optional .chesscom.game_storage.v1.GameProvider provider = 2;
  optional string key = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp started_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6;
  optional string time_control = 7;
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05744"></a>
## FND-05744: chesscom.game_storage.v1.GameStored.provider = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.GameProvider provider = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4892.

```text
.game_storage.v1.VsCoachGameData vs_coach_game_data = 35;
  }
  optional string internal_key = 1;
  optional .chesscom.game_storage.v1.GameProvider provider = 2;
  optional string key = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp started_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6;
  optional string time_control = 7;
  repeated .chesscom.game_storage.v
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05745"></a>
## FND-05745: chesscom.game_storage.v1.GameStored.key = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4956.

```text
optional string internal_key = 1;
  optional .chesscom.game_storage.v1.GameProvider provider = 2;
  optional string key = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp started_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6;
  optional string time_control = 7;
  repeated .chesscom.game_storage.v1.PerPlayerTimeControl per_player_time_controls = 8;
  optional 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05746"></a>
## FND-05746: chesscom.game_storage.v1.GameStored.created_at = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp created_at = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 4983.

```text
y = 1;
  optional .chesscom.game_storage.v1.GameProvider provider = 2;
  optional string key = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp started_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6;
  optional string time_control = 7;
  repeated .chesscom.game_storage.v1.PerPlayerTimeControl per_player_time_controls = 8;
  optional .chesscom.game_storage.v1.T
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05747"></a>
## FND-05747: chesscom.game_storage.v1.GameStored.started_at = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp started_at = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5037.

```text
er provider = 2;
  optional string key = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp started_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6;
  optional string time_control = 7;
  repeated .chesscom.game_storage.v1.PerPlayerTimeControl per_player_time_controls = 8;
  optional .chesscom.game_storage.v1.TimeClass time_class = 9;
  optional .chesscom.game_sto
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05748"></a>
## FND-05748: chesscom.game_storage.v1.GameStored.ended_at = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp ended_at = 6;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5091.

```text
 .google.protobuf.Timestamp created_at = 4;
  optional .google.protobuf.Timestamp started_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6;
  optional string time_control = 7;
  repeated .chesscom.game_storage.v1.PerPlayerTimeControl per_player_time_controls = 8;
  optional .chesscom.game_storage.v1.TimeClass time_class = 9;
  optional .chesscom.game_storage.v1.RatingClass rating_class = 10;
  optional .che
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05749"></a>
## FND-05749: chesscom.game_storage.v1.GameStored.time_control = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string time_control = 7;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5143.

```text
al .google.protobuf.Timestamp started_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6;
  optional string time_control = 7;
  repeated .chesscom.game_storage.v1.PerPlayerTimeControl per_player_time_controls = 8;
  optional .chesscom.game_storage.v1.TimeClass time_class = 9;
  optional .chesscom.game_storage.v1.RatingClass rating_class = 10;
  optional .chesscom.game_storage.v1.Variant variant = 11;
  option
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05750"></a>
## FND-05750: chesscom.game_storage.v1.GameStored.per_player_time_controls = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_storage.v1.PerPlayerTimeControl per_player_time_controls = 8;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5179.

```text
d_at = 5;
  optional .google.protobuf.Timestamp ended_at = 6;
  optional string time_control = 7;
  repeated .chesscom.game_storage.v1.PerPlayerTimeControl per_player_time_controls = 8;
  optional .chesscom.game_storage.v1.TimeClass time_class = 9;
  optional .chesscom.game_storage.v1.RatingClass rating_class = 10;
  optional .chesscom.game_storage.v1.Variant variant = 11;
  optional .chesscom.game_storage.v1.GameRes
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05751"></a>
## FND-05751: chesscom.game_storage.v1.GameStored.time_class = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.TimeClass time_class = 9;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5267.

```text
trol = 7;
  repeated .chesscom.game_storage.v1.PerPlayerTimeControl per_player_time_controls = 8;
  optional .chesscom.game_storage.v1.TimeClass time_class = 9;
  optional .chesscom.game_storage.v1.RatingClass rating_class = 10;
  optional .chesscom.game_storage.v1.Variant variant = 11;
  optional .chesscom.game_storage.v1.GameResult result = 12;
  optional .chesscom.game_storage.v1.GamePrivacy privacy = 13;
  option
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05752"></a>
## FND-05752: chesscom.game_storage.v1.GameStored.rating_class = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.RatingClass rating_class = 10;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5330.

```text
trol per_player_time_controls = 8;
  optional .chesscom.game_storage.v1.TimeClass time_class = 9;
  optional .chesscom.game_storage.v1.RatingClass rating_class = 10;
  optional .chesscom.game_storage.v1.Variant variant = 11;
  optional .chesscom.game_storage.v1.GameResult result = 12;
  optional .chesscom.game_storage.v1.GamePrivacy privacy = 13;
  optional .chesscom.game_storage.v1.GameOrigin origin = 14;
  optional
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05753"></a>
## FND-05753: chesscom.game_storage.v1.GameStored.variant = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.Variant variant = 11;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5398.

```text
.v1.TimeClass time_class = 9;
  optional .chesscom.game_storage.v1.RatingClass rating_class = 10;
  optional .chesscom.game_storage.v1.Variant variant = 11;
  optional .chesscom.game_storage.v1.GameResult result = 12;
  optional .chesscom.game_storage.v1.GamePrivacy privacy = 13;
  optional .chesscom.game_storage.v1.GameOrigin origin = 14;
  optional .chesscom.tdtools.v1.ChessComTournamentIdentifier chess_com_tournam
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05754"></a>
## FND-05754: chesscom.game_storage.v1.GameStored.result = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.GameResult result = 12;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5457.

```text
rage.v1.RatingClass rating_class = 10;
  optional .chesscom.game_storage.v1.Variant variant = 11;
  optional .chesscom.game_storage.v1.GameResult result = 12;
  optional .chesscom.game_storage.v1.GamePrivacy privacy = 13;
  optional .chesscom.game_storage.v1.GameOrigin origin = 14;
  optional .chesscom.tdtools.v1.ChessComTournamentIdentifier chess_com_tournament_identifier = 15;
  repeated string tags = 16;
}

messag
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05755"></a>
## FND-05755: chesscom.game_storage.v1.GameStored.privacy = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.GamePrivacy privacy = 13;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5518.

```text
ame_storage.v1.Variant variant = 11;
  optional .chesscom.game_storage.v1.GameResult result = 12;
  optional .chesscom.game_storage.v1.GamePrivacy privacy = 13;
  optional .chesscom.game_storage.v1.GameOrigin origin = 14;
  optional .chesscom.tdtools.v1.ChessComTournamentIdentifier chess_com_tournament_identifier = 15;
  repeated string tags = 16;
}

message ChessGame {
  oneof _initial_fen {
  string initial_fen = 1
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05756"></a>
## FND-05756: chesscom.game_storage.v1.GameStored.origin = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.GameOrigin origin = 14;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5581.

```text
storage.v1.GameResult result = 12;
  optional .chesscom.game_storage.v1.GamePrivacy privacy = 13;
  optional .chesscom.game_storage.v1.GameOrigin origin = 14;
  optional .chesscom.tdtools.v1.ChessComTournamentIdentifier chess_com_tournament_identifier = 15;
  repeated string tags = 16;
}

message ChessGame {
  oneof _initial_fen {
  string initial_fen = 1;
  }
  oneof _master_chess_game_data {
  .chesscom.game_storag
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05757"></a>
## FND-05757: chesscom.game_storage.v1.GameStored.chess_com_tournament_identifier = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.tdtools.v1.ChessComTournamentIdentifier chess_com_tournament_identifier = 15;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5642.

```text
storage.v1.GamePrivacy privacy = 13;
  optional .chesscom.game_storage.v1.GameOrigin origin = 14;
  optional .chesscom.tdtools.v1.ChessComTournamentIdentifier chess_com_tournament_identifier = 15;
  repeated string tags = 16;
}

message ChessGame {
  oneof _initial_fen {
  string initial_fen = 1;
  }
  oneof _master_chess_game_data {
  .chesscom.game_storage.v1.MasterChessGameData master_chess_game_data = 8;
  }
  op
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05758"></a>
## FND-05758: chesscom.game_storage.v1.GameStored.tags = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string tags = 16;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5741.

```text
 optional .chesscom.tdtools.v1.ChessComTournamentIdentifier chess_com_tournament_identifier = 15;
  repeated string tags = 16;
}

message ChessGame {
  oneof _initial_fen {
  string initial_fen = 1;
  }
  oneof _master_chess_game_data {
  .chesscom.game_storage.v1.MasterChessGameData master_chess_game_data = 8;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  re
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05759"></a>
## FND-05759: message declaration: chesscom.game_storage.v1.ChessGame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ChessGame {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5771.

```text
.ChessComTournamentIdentifier chess_com_tournament_identifier = 15;
  repeated string tags = 16;
}

message ChessGame {
  oneof _initial_fen {
  string initial_fen = 1;
  }
  oneof _master_chess_game_data {
  .chesscom.game_storage.v1.MasterChessGameData master_chess_game_data = 8;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05760"></a>
## FND-05760: oneof declaration: chesscom.game_storage.v1.ChessGame._initial_fen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _initial_fen {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5793.

```text
ntifier chess_com_tournament_identifier = 15;
  repeated string tags = 16;
}

message ChessGame {
  oneof _initial_fen {
  string initial_fen = 1;
  }
  oneof _master_chess_game_data {
  .chesscom.game_storage.v1.MasterChessGameData master_chess_game_data = 8;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chess
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05761"></a>
## FND-05761: chesscom.game_storage.v1.ChessGame.initial_fen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string initial_fen = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5816.

```text
ament_identifier = 15;
  repeated string tags = 16;
}

message ChessGame {
  oneof _initial_fen {
  string initial_fen = 1;
  }
  oneof _master_chess_game_data {
  .chesscom.game_storage.v1.MasterChessGameData master_chess_game_data = 8;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_storage.v1.Pla
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05762"></a>
## FND-05762: oneof declaration: chesscom.game_storage.v1.ChessGame._master_chess_game_data

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _master_chess_game_data {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5846.

```text
ted string tags = 16;
}

message ChessGame {
  oneof _initial_fen {
  string initial_fen = 1;
  }
  oneof _master_chess_game_data {
  .chesscom.game_storage.v1.MasterChessGameData master_chess_game_data = 8;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_storage.v1.Player white_player = 6;
  option
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05763"></a>
## FND-05763: chesscom.game_storage.v1.ChessGame.master_chess_game_data = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_storage.v1.MasterChessGameData master_chess_game_data = 8;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5880.

```text
hessGame {
  oneof _initial_fen {
  string initial_fen = 1;
  }
  oneof _master_chess_game_data {
  .chesscom.game_storage.v1.MasterChessGameData master_chess_game_data = 8;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_storage.v1.Player white_player = 6;
  optional .chesscom.game_storage.v1.Playe
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05764"></a>
## FND-05764: chesscom.game_storage.v1.ChessGame.final_fen = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string final_fen = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5960.

```text
chess_game_data {
  .chesscom.game_storage.v1.MasterChessGameData master_chess_game_data = 8;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_storage.v1.Player white_player = 6;
  optional .chesscom.game_storage.v1.Player black_player = 7;
}

message BughouseGame {
  optional .chesscom.game_storage.
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05765"></a>
## FND-05765: chesscom.game_storage.v1.ChessGame.ply_count = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 ply_count = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5993.

```text
e_storage.v1.MasterChessGameData master_chess_game_data = 8;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_storage.v1.Player white_player = 6;
  optional .chesscom.game_storage.v1.Player black_player = 7;
}

message BughouseGame {
  optional .chesscom.game_storage.v1.ChessGame first_board = 1;
  o
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05766"></a>
## FND-05766: chesscom.game_storage.v1.ChessGame.move_text = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string move_text = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6026.

```text
master_chess_game_data = 8;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_storage.v1.Player white_player = 6;
  optional .chesscom.game_storage.v1.Player black_player = 7;
}

message BughouseGame {
  optional .chesscom.game_storage.v1.ChessGame first_board = 1;
  optional string second_game_key = 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05767"></a>
## FND-05767: chesscom.game_storage.v1.ChessGame.move_timestamps = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 move_timestamps = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6059.

```text
 optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_storage.v1.Player white_player = 6;
  optional .chesscom.game_storage.v1.Player black_player = 7;
}

message BughouseGame {
  optional .chesscom.game_storage.v1.ChessGame first_board = 1;
  optional string second_game_key = 3;
}

message VariantGame {
  opt
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05768"></a>
## FND-05768: chesscom.game_storage.v1.ChessGame.white_player = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.Player white_player = 6;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6098.

```text
nal uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_storage.v1.Player white_player = 6;
  optional .chesscom.game_storage.v1.Player black_player = 7;
}

message BughouseGame {
  optional .chesscom.game_storage.v1.ChessGame first_board = 1;
  optional string second_game_key = 3;
}

message VariantGame {
  optional string initial_fen4 = 1;
  option
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05769"></a>
## FND-05769: chesscom.game_storage.v1.ChessGame.black_player = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.Player black_player = 7;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6160.

```text
epeated uint32 move_timestamps = 5;
  optional .chesscom.game_storage.v1.Player white_player = 6;
  optional .chesscom.game_storage.v1.Player black_player = 7;
}

message BughouseGame {
  optional .chesscom.game_storage.v1.ChessGame first_board = 1;
  optional string second_game_key = 3;
}

message VariantGame {
  optional string initial_fen4 = 1;
  optional string end_fen4 = 2;
  optional uint32 ply_count = 3;
  opt
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05770"></a>
## FND-05770: message declaration: chesscom.game_storage.v1.BughouseGame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BughouseGame {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6223.

```text
torage.v1.Player white_player = 6;
  optional .chesscom.game_storage.v1.Player black_player = 7;
}

message BughouseGame {
  optional .chesscom.game_storage.v1.ChessGame first_board = 1;
  optional string second_game_key = 3;
}

message VariantGame {
  optional string initial_fen4 = 1;
  optional string end_fen4 = 2;
  optional uint32 ply_count = 3;
  optional string pgn4 = 4;
  optional string board_dimension = 5;
 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05771"></a>
## FND-05771: chesscom.game_storage.v1.BughouseGame.first_board = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.ChessGame first_board = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6248.

```text
ayer = 6;
  optional .chesscom.game_storage.v1.Player black_player = 7;
}

message BughouseGame {
  optional .chesscom.game_storage.v1.ChessGame first_board = 1;
  optional string second_game_key = 3;
}

message VariantGame {
  optional string initial_fen4 = 1;
  optional string end_fen4 = 2;
  optional uint32 ply_count = 3;
  optional string pgn4 = 4;
  optional string board_dimension = 5;
  optional .chesscom.game_
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05772"></a>
## FND-05772: chesscom.game_storage.v1.BughouseGame.second_game_key = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string second_game_key = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6312.

```text
er = 7;
}

message BughouseGame {
  optional .chesscom.game_storage.v1.ChessGame first_board = 1;
  optional string second_game_key = 3;
}

message VariantGame {
  optional string initial_fen4 = 1;
  optional string end_fen4 = 2;
  optional uint32 ply_count = 3;
  optional string pgn4 = 4;
  optional string board_dimension = 5;
  optional .chesscom.game_storage.v1.VariantGame.VariantType type = 6;
  optional string r
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05773"></a>
## FND-05773: message declaration: chesscom.game_storage.v1.VariantGame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message VariantGame {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6352.

```text
onal .chesscom.game_storage.v1.ChessGame first_board = 1;
  optional string second_game_key = 3;
}

message VariantGame {
  optional string initial_fen4 = 1;
  optional string end_fen4 = 2;
  optional uint32 ply_count = 3;
  optional string pgn4 = 4;
  optional string board_dimension = 5;
  optional .chesscom.game_storage.v1.VariantGame.VariantType type = 6;
  optional string rating_type = 7;
  optional .chesscom.gam
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05774"></a>
## FND-05774: chesscom.game_storage.v1.VariantGame.initial_fen4 = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string initial_fen4 = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6376.

```text
age.v1.ChessGame first_board = 1;
  optional string second_game_key = 3;
}

message VariantGame {
  optional string initial_fen4 = 1;
  optional string end_fen4 = 2;
  optional uint32 ply_count = 3;
  optional string pgn4 = 4;
  optional string board_dimension = 5;
  optional .chesscom.game_storage.v1.VariantGame.VariantType type = 6;
  optional string rating_type = 7;
  optional .chesscom.game_storage.v1.Player play
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
