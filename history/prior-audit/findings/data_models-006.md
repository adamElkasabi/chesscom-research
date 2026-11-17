# data_models — findings 501–600

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-00775"></a>
## FND-00775: oneof declaration: chesscom.bots.v1.PhraseList._user_spends_more_than_15_seconds_on_a_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_spends_more_than_15_seconds_on_a_move {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1832.

```text
g opening_d4_d5_queens_gambit = 28;
  }
  oneof _opening_other {
  string opening_other = 29;
  }
  oneof _user_spends_more_than_15_seconds_on_a_move {
  string user_spends_more_than_15_seconds_on_a_move = 30;
  }
  oneof _user_spends_more_than_1_minute_on_a_move {
  string user_spends_more_than_1_minute_on_a_move = 31;
  }
  oneof _user_spends_more_than_3_minutes_on_move {
  string user_spends_more_than_3_minutes_on
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00776"></a>
## FND-00776: chesscom.bots.v1.PhraseList.user_spends_more_than_15_seconds_on_a_move = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_spends_more_than_15_seconds_on_a_move = 30;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1886.

```text
ng_other {
  string opening_other = 29;
  }
  oneof _user_spends_more_than_15_seconds_on_a_move {
  string user_spends_more_than_15_seconds_on_a_move = 30;
  }
  oneof _user_spends_more_than_1_minute_on_a_move {
  string user_spends_more_than_1_minute_on_a_move = 31;
  }
  oneof _user_spends_more_than_3_minutes_on_move {
  string user_spends_more_than_3_minutes_on_move = 32;
  }
  oneof _r_p_endgame_reached {
  strin
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00777"></a>
## FND-00777: oneof declaration: chesscom.bots.v1.PhraseList._user_spends_more_than_1_minute_on_a_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_spends_more_than_1_minute_on_a_move {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1948.

```text
ds_more_than_15_seconds_on_a_move {
  string user_spends_more_than_15_seconds_on_a_move = 30;
  }
  oneof _user_spends_more_than_1_minute_on_a_move {
  string user_spends_more_than_1_minute_on_a_move = 31;
  }
  oneof _user_spends_more_than_3_minutes_on_move {
  string user_spends_more_than_3_minutes_on_move = 32;
  }
  oneof _r_p_endgame_reached {
  string r_p_endgame_reached = 33;
  }
  oneof _k_p_endgame_reached {
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00778"></a>
## FND-00778: chesscom.bots.v1.PhraseList.user_spends_more_than_1_minute_on_a_move = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_spends_more_than_1_minute_on_a_move = 31;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2000.

```text
ends_more_than_15_seconds_on_a_move = 30;
  }
  oneof _user_spends_more_than_1_minute_on_a_move {
  string user_spends_more_than_1_minute_on_a_move = 31;
  }
  oneof _user_spends_more_than_3_minutes_on_move {
  string user_spends_more_than_3_minutes_on_move = 32;
  }
  oneof _r_p_endgame_reached {
  string r_p_endgame_reached = 33;
  }
  oneof _k_p_endgame_reached {
  string k_p_endgame_reached = 34;
  }
  oneof _gam
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00779"></a>
## FND-00779: oneof declaration: chesscom.bots.v1.PhraseList._user_spends_more_than_3_minutes_on_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_spends_more_than_3_minutes_on_move {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2060.

```text
spends_more_than_1_minute_on_a_move {
  string user_spends_more_than_1_minute_on_a_move = 31;
  }
  oneof _user_spends_more_than_3_minutes_on_move {
  string user_spends_more_than_3_minutes_on_move = 32;
  }
  oneof _r_p_endgame_reached {
  string r_p_endgame_reached = 33;
  }
  oneof _k_p_endgame_reached {
  string k_p_endgame_reached = 34;
  }
  oneof _game_reached_move_40 {
  string game_reached_move_40 = 35;
  }

```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00780"></a>
## FND-00780: chesscom.bots.v1.PhraseList.user_spends_more_than_3_minutes_on_move = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_spends_more_than_3_minutes_on_move = 32;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2111.

```text
_spends_more_than_1_minute_on_a_move = 31;
  }
  oneof _user_spends_more_than_3_minutes_on_move {
  string user_spends_more_than_3_minutes_on_move = 32;
  }
  oneof _r_p_endgame_reached {
  string r_p_endgame_reached = 33;
  }
  oneof _k_p_endgame_reached {
  string k_p_endgame_reached = 34;
  }
  oneof _game_reached_move_40 {
  string game_reached_move_40 = 35;
  }
  oneof _game_reached_move_100 {
  string game_reac
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00781"></a>
## FND-00781: oneof declaration: chesscom.bots.v1.PhraseList._r_p_endgame_reached

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _r_p_endgame_reached {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2170.

```text
r_spends_more_than_3_minutes_on_move {
  string user_spends_more_than_3_minutes_on_move = 32;
  }
  oneof _r_p_endgame_reached {
  string r_p_endgame_reached = 33;
  }
  oneof _k_p_endgame_reached {
  string k_p_endgame_reached = 34;
  }
  oneof _game_reached_move_40 {
  string game_reached_move_40 = 35;
  }
  oneof _game_reached_move_100 {
  string game_reached_move_100 = 36;
  }
  oneof _rematch_if_user_has_played_
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00782"></a>
## FND-00782: chesscom.bots.v1.PhraseList.r_p_endgame_reached = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string r_p_endgame_reached = 33;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2201.

```text
_move {
  string user_spends_more_than_3_minutes_on_move = 32;
  }
  oneof _r_p_endgame_reached {
  string r_p_endgame_reached = 33;
  }
  oneof _k_p_endgame_reached {
  string k_p_endgame_reached = 34;
  }
  oneof _game_reached_move_40 {
  string game_reached_move_40 = 35;
  }
  oneof _game_reached_move_100 {
  string game_reached_move_100 = 36;
  }
  oneof _rematch_if_user_has_played_before {
  string rematch_if_us
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00783"></a>
## FND-00783: oneof declaration: chesscom.bots.v1.PhraseList._k_p_endgame_reached

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _k_p_endgame_reached {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2240.

```text
3_minutes_on_move = 32;
  }
  oneof _r_p_endgame_reached {
  string r_p_endgame_reached = 33;
  }
  oneof _k_p_endgame_reached {
  string k_p_endgame_reached = 34;
  }
  oneof _game_reached_move_40 {
  string game_reached_move_40 = 35;
  }
  oneof _game_reached_move_100 {
  string game_reached_move_100 = 36;
  }
  oneof _rematch_if_user_has_played_before {
  string rematch_if_user_has_played_before = 37;
  }
  oneof 
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00784"></a>
## FND-00784: chesscom.bots.v1.PhraseList.k_p_endgame_reached = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string k_p_endgame_reached = 34;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2271.

```text
neof _r_p_endgame_reached {
  string r_p_endgame_reached = 33;
  }
  oneof _k_p_endgame_reached {
  string k_p_endgame_reached = 34;
  }
  oneof _game_reached_move_40 {
  string game_reached_move_40 = 35;
  }
  oneof _game_reached_move_100 {
  string game_reached_move_100 = 36;
  }
  oneof _rematch_if_user_has_played_before {
  string rematch_if_user_has_played_before = 37;
  }
  oneof _heavy_piece_endgame_reached {

```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00785"></a>
## FND-00785: oneof declaration: chesscom.bots.v1.PhraseList._game_reached_move_40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_reached_move_40 {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2310.

```text
p_endgame_reached = 33;
  }
  oneof _k_p_endgame_reached {
  string k_p_endgame_reached = 34;
  }
  oneof _game_reached_move_40 {
  string game_reached_move_40 = 35;
  }
  oneof _game_reached_move_100 {
  string game_reached_move_100 = 36;
  }
  oneof _rematch_if_user_has_played_before {
  string rematch_if_user_has_played_before = 37;
  }
  oneof _heavy_piece_endgame_reached {
  string heavy_piece_endgame_reached = 
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00786"></a>
## FND-00786: chesscom.bots.v1.PhraseList.game_reached_move_40 = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string game_reached_move_40 = 35;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2342.

```text
eof _k_p_endgame_reached {
  string k_p_endgame_reached = 34;
  }
  oneof _game_reached_move_40 {
  string game_reached_move_40 = 35;
  }
  oneof _game_reached_move_100 {
  string game_reached_move_100 = 36;
  }
  oneof _rematch_if_user_has_played_before {
  string rematch_if_user_has_played_before = 37;
  }
  oneof _heavy_piece_endgame_reached {
  string heavy_piece_endgame_reached = 38;
  }
  oneof _minor_piece_end
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00787"></a>
## FND-00787: oneof declaration: chesscom.bots.v1.PhraseList._game_reached_move_100

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_reached_move_100 {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2382.

```text
endgame_reached = 34;
  }
  oneof _game_reached_move_40 {
  string game_reached_move_40 = 35;
  }
  oneof _game_reached_move_100 {
  string game_reached_move_100 = 36;
  }
  oneof _rematch_if_user_has_played_before {
  string rematch_if_user_has_played_before = 37;
  }
  oneof _heavy_piece_endgame_reached {
  string heavy_piece_endgame_reached = 38;
  }
  oneof _minor_piece_endgame_reached {
  string minor_piece_endg
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00788"></a>
## FND-00788: chesscom.bots.v1.PhraseList.game_reached_move_100 = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string game_reached_move_100 = 36;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2415.

```text
 _game_reached_move_40 {
  string game_reached_move_40 = 35;
  }
  oneof _game_reached_move_100 {
  string game_reached_move_100 = 36;
  }
  oneof _rematch_if_user_has_played_before {
  string rematch_if_user_has_played_before = 37;
  }
  oneof _heavy_piece_endgame_reached {
  string heavy_piece_endgame_reached = 38;
  }
  oneof _minor_piece_endgame_reached {
  string minor_piece_endgame_reached = 39;
  }
}

```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00789"></a>
## FND-00789: oneof declaration: chesscom.bots.v1.PhraseList._rematch_if_user_has_played_before

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rematch_if_user_has_played_before {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2456.

```text
ached_move_40 = 35;
  }
  oneof _game_reached_move_100 {
  string game_reached_move_100 = 36;
  }
  oneof _rematch_if_user_has_played_before {
  string rematch_if_user_has_played_before = 37;
  }
  oneof _heavy_piece_endgame_reached {
  string heavy_piece_endgame_reached = 38;
  }
  oneof _minor_piece_endgame_reached {
  string minor_piece_endgame_reached = 39;
  }
}

```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00790"></a>
## FND-00790: chesscom.bots.v1.PhraseList.rematch_if_user_has_played_before = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string rematch_if_user_has_played_before = 37;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2501.

```text
_move_100 {
  string game_reached_move_100 = 36;
  }
  oneof _rematch_if_user_has_played_before {
  string rematch_if_user_has_played_before = 37;
  }
  oneof _heavy_piece_endgame_reached {
  string heavy_piece_endgame_reached = 38;
  }
  oneof _minor_piece_endgame_reached {
  string minor_piece_endgame_reached = 39;
  }
}

```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00791"></a>
## FND-00791: oneof declaration: chesscom.bots.v1.PhraseList._heavy_piece_endgame_reached

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _heavy_piece_endgame_reached {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2554.

```text
  oneof _rematch_if_user_has_played_before {
  string rematch_if_user_has_played_before = 37;
  }
  oneof _heavy_piece_endgame_reached {
  string heavy_piece_endgame_reached = 38;
  }
  oneof _minor_piece_endgame_reached {
  string minor_piece_endgame_reached = 39;
  }
}

```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00792"></a>
## FND-00792: chesscom.bots.v1.PhraseList.heavy_piece_endgame_reached = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string heavy_piece_endgame_reached = 38;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2593.

```text
ore {
  string rematch_if_user_has_played_before = 37;
  }
  oneof _heavy_piece_endgame_reached {
  string heavy_piece_endgame_reached = 38;
  }
  oneof _minor_piece_endgame_reached {
  string minor_piece_endgame_reached = 39;
  }
}

```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00793"></a>
## FND-00793: oneof declaration: chesscom.bots.v1.PhraseList._minor_piece_endgame_reached

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _minor_piece_endgame_reached {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2640.

```text
e = 37;
  }
  oneof _heavy_piece_endgame_reached {
  string heavy_piece_endgame_reached = 38;
  }
  oneof _minor_piece_endgame_reached {
  string minor_piece_endgame_reached = 39;
  }
}

```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00794"></a>
## FND-00794: chesscom.bots.v1.PhraseList.minor_piece_endgame_reached = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string minor_piece_endgame_reached = 39;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 2679.

```text
e_reached {
  string heavy_piece_endgame_reached = 38;
  }
  oneof _minor_piece_endgame_reached {
  string minor_piece_endgame_reached = 39;
  }
}

```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00795"></a>
## FND-00795: enum declaration: chesscom.ceac.v1.GameAnalysisGameType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameAnalysisGameType {

### Evidence

- **SRC-0229** `research/proto/chesscom/ceac/v1/game_analysis.proto` — [preserved redacted evidence](../evidence/text/e2c3a6cf068315399867b6fa9a93166ae0d064ff8c6cef27c1d1c0ac98579b0b.proto)
  Character offset 94.

```text
// source: chesscom/ceac/v1/game_analysis.proto
// syntax: proto3

package chesscom.ceac.v1;

enum GameAnalysisGameType {
  GAME_ANALYSIS_GAME_TYPE_UNSPECIFIED = 0;
  GAME_ANALYSIS_GAME_TYPE_DAILY = 1;
  GAME_ANALYSIS_GAME_TYPE_LIVE = 2;
  GAME_ANALYSIS_GAME_TYPE_MASTER = 3;
  GAME_ANALYSIS_GAME_TYPE_PGN = 4;
  GAME_ANALYSIS_GAME_TYPE_VS_COMPUTER = 5;
  GAME_ANALYSIS_GAME_TYPE_VS_COACH = 6;
}

```

**Source references:** SRC-0229, SRC-1200  
**URL references:** None independently associated  
**Related findings:** FND-00796, FND-00797

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00796"></a>
## FND-00796: chesscom.ceac.v1.GameAnalysisGameType.GAME_ANALYSIS_GAME_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ANALYSIS_GAME_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0229** `research/proto/chesscom/ceac/v1/game_analysis.proto` — [preserved redacted evidence](../evidence/text/e2c3a6cf068315399867b6fa9a93166ae0d064ff8c6cef27c1d1c0ac98579b0b.proto)
  Character offset 124.

```text
/v1/game_analysis.proto
// syntax: proto3

package chesscom.ceac.v1;

enum GameAnalysisGameType {
  GAME_ANALYSIS_GAME_TYPE_UNSPECIFIED = 0;
  GAME_ANALYSIS_GAME_TYPE_DAILY = 1;
  GAME_ANALYSIS_GAME_TYPE_LIVE = 2;
  GAME_ANALYSIS_GAME_TYPE_MASTER = 3;
  GAME_ANALYSIS_GAME_TYPE_PGN = 4;
  GAME_ANALYSIS_GAME_TYPE_VS_COMPUTER = 5;
  GAME_ANALYSIS_GAME_TYPE_VS_COACH = 6;
}

```

**Source references:** SRC-0229, SRC-1200  
**URL references:** None independently associated  
**Related findings:** FND-00795, FND-00797

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00797"></a>
## FND-00797: chesscom.ceac.v1.GameAnalysisGameType.GAME_ANALYSIS_GAME_TYPE_DAILY = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ANALYSIS_GAME_TYPE_DAILY = 1;

### Evidence

- **SRC-0229** `research/proto/chesscom/ceac/v1/game_analysis.proto` — [preserved redacted evidence](../evidence/text/e2c3a6cf068315399867b6fa9a93166ae0d064ff8c6cef27c1d1c0ac98579b0b.proto)
  Character offset 167.

```text
package chesscom.ceac.v1;

enum GameAnalysisGameType {
  GAME_ANALYSIS_GAME_TYPE_UNSPECIFIED = 0;
  GAME_ANALYSIS_GAME_TYPE_DAILY = 1;
  GAME_ANALYSIS_GAME_TYPE_LIVE = 2;
  GAME_ANALYSIS_GAME_TYPE_MASTER = 3;
  GAME_ANALYSIS_GAME_TYPE_PGN = 4;
  GAME_ANALYSIS_GAME_TYPE_VS_COMPUTER = 5;
  GAME_ANALYSIS_GAME_TYPE_VS_COACH = 6;
}

```

**Source references:** SRC-0229, SRC-1200  
**URL references:** None independently associated  
**Related findings:** FND-00795, FND-00796

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00798"></a>
## FND-00798: chesscom.ceac.v1.GameAnalysisGameType.GAME_ANALYSIS_GAME_TYPE_LIVE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ANALYSIS_GAME_TYPE_LIVE = 2;

### Evidence

- **SRC-0229** `research/proto/chesscom/ceac/v1/game_analysis.proto` — [preserved redacted evidence](../evidence/text/e2c3a6cf068315399867b6fa9a93166ae0d064ff8c6cef27c1d1c0ac98579b0b.proto)
  Character offset 204.

```text
nalysisGameType {
  GAME_ANALYSIS_GAME_TYPE_UNSPECIFIED = 0;
  GAME_ANALYSIS_GAME_TYPE_DAILY = 1;
  GAME_ANALYSIS_GAME_TYPE_LIVE = 2;
  GAME_ANALYSIS_GAME_TYPE_MASTER = 3;
  GAME_ANALYSIS_GAME_TYPE_PGN = 4;
  GAME_ANALYSIS_GAME_TYPE_VS_COMPUTER = 5;
  GAME_ANALYSIS_GAME_TYPE_VS_COACH = 6;
}

```

**Source references:** SRC-0229, SRC-1200  
**URL references:** None independently associated  
**Related findings:** FND-00795, FND-00796, FND-00797

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00799"></a>
## FND-00799: chesscom.ceac.v1.GameAnalysisGameType.GAME_ANALYSIS_GAME_TYPE_MASTER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ANALYSIS_GAME_TYPE_MASTER = 3;

### Evidence

- **SRC-0229** `research/proto/chesscom/ceac/v1/game_analysis.proto` — [preserved redacted evidence](../evidence/text/e2c3a6cf068315399867b6fa9a93166ae0d064ff8c6cef27c1d1c0ac98579b0b.proto)
  Character offset 240.

```text
ME_TYPE_UNSPECIFIED = 0;
  GAME_ANALYSIS_GAME_TYPE_DAILY = 1;
  GAME_ANALYSIS_GAME_TYPE_LIVE = 2;
  GAME_ANALYSIS_GAME_TYPE_MASTER = 3;
  GAME_ANALYSIS_GAME_TYPE_PGN = 4;
  GAME_ANALYSIS_GAME_TYPE_VS_COMPUTER = 5;
  GAME_ANALYSIS_GAME_TYPE_VS_COACH = 6;
}

```

**Source references:** SRC-0229, SRC-1200  
**URL references:** None independently associated  
**Related findings:** FND-00795, FND-00796, FND-00797

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00800"></a>
## FND-00800: chesscom.ceac.v1.GameAnalysisGameType.GAME_ANALYSIS_GAME_TYPE_PGN = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ANALYSIS_GAME_TYPE_PGN = 4;

### Evidence

- **SRC-0229** `research/proto/chesscom/ceac/v1/game_analysis.proto` — [preserved redacted evidence](../evidence/text/e2c3a6cf068315399867b6fa9a93166ae0d064ff8c6cef27c1d1c0ac98579b0b.proto)
  Character offset 278.

```text
IS_GAME_TYPE_DAILY = 1;
  GAME_ANALYSIS_GAME_TYPE_LIVE = 2;
  GAME_ANALYSIS_GAME_TYPE_MASTER = 3;
  GAME_ANALYSIS_GAME_TYPE_PGN = 4;
  GAME_ANALYSIS_GAME_TYPE_VS_COMPUTER = 5;
  GAME_ANALYSIS_GAME_TYPE_VS_COACH = 6;
}

```

**Source references:** SRC-0229, SRC-1200  
**URL references:** None independently associated  
**Related findings:** FND-00795, FND-00796, FND-00797

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00801"></a>
## FND-00801: chesscom.ceac.v1.GameAnalysisGameType.GAME_ANALYSIS_GAME_TYPE_VS_COMPUTER = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ANALYSIS_GAME_TYPE_VS_COMPUTER = 5;

### Evidence

- **SRC-0229** `research/proto/chesscom/ceac/v1/game_analysis.proto` — [preserved redacted evidence](../evidence/text/e2c3a6cf068315399867b6fa9a93166ae0d064ff8c6cef27c1d1c0ac98579b0b.proto)
  Character offset 313.

```text
YSIS_GAME_TYPE_LIVE = 2;
  GAME_ANALYSIS_GAME_TYPE_MASTER = 3;
  GAME_ANALYSIS_GAME_TYPE_PGN = 4;
  GAME_ANALYSIS_GAME_TYPE_VS_COMPUTER = 5;
  GAME_ANALYSIS_GAME_TYPE_VS_COACH = 6;
}

```

**Source references:** SRC-0229, SRC-1200  
**URL references:** None independently associated  
**Related findings:** FND-00795, FND-00796, FND-00797

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00802"></a>
## FND-00802: chesscom.ceac.v1.GameAnalysisGameType.GAME_ANALYSIS_GAME_TYPE_VS_COACH = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ANALYSIS_GAME_TYPE_VS_COACH = 6;

### Evidence

- **SRC-0229** `research/proto/chesscom/ceac/v1/game_analysis.proto` — [preserved redacted evidence](../evidence/text/e2c3a6cf068315399867b6fa9a93166ae0d064ff8c6cef27c1d1c0ac98579b0b.proto)
  Character offset 356.

```text
ME_TYPE_MASTER = 3;
  GAME_ANALYSIS_GAME_TYPE_PGN = 4;
  GAME_ANALYSIS_GAME_TYPE_VS_COMPUTER = 5;
  GAME_ANALYSIS_GAME_TYPE_VS_COACH = 6;
}

```

**Source references:** SRC-0229, SRC-1200  
**URL references:** None independently associated  
**Related findings:** FND-00795, FND-00796, FND-00797

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00803"></a>
## FND-00803: enum declaration: chesscom.ceac.v2.Client

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Client {

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 87.

```text
// source: chesscom/ceac/v2/client.proto
// syntax: proto3

package chesscom.ceac.v2;

enum Client {
  CLIENT_UNSPECIFIED = 0;
  CLIENT_WEB = 1;
  CLIENT_ANDROID = 2;
  CLIENT_IOS = 3;
  CLIENT_LC = 4;
  CLIENT_RCN = 5;
  CLIENT_EVENTS = 6;
  CLIENT_INSIGHTS = 7;
  CLIENT_STATS = 8;
  CLIENT_COACH_ASSET_UPDATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00804"></a>
## FND-00804: chesscom.ceac.v2.Client.CLIENT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_UNSPECIFIED = 0;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 103.

```text
source: chesscom/ceac/v2/client.proto
// syntax: proto3

package chesscom.ceac.v2;

enum Client {
  CLIENT_UNSPECIFIED = 0;
  CLIENT_WEB = 1;
  CLIENT_ANDROID = 2;
  CLIENT_IOS = 3;
  CLIENT_LC = 4;
  CLIENT_RCN = 5;
  CLIENT_EVENTS = 6;
  CLIENT_INSIGHTS = 7;
  CLIENT_STATS = 8;
  CLIENT_COACH_ASSET_UPDATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDI
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00805"></a>
## FND-00805: chesscom.ceac.v2.Client.CLIENT_WEB = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_WEB = 1;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 129.

```text
lient.proto
// syntax: proto3

package chesscom.ceac.v2;

enum Client {
  CLIENT_UNSPECIFIED = 0;
  CLIENT_WEB = 1;
  CLIENT_ANDROID = 2;
  CLIENT_IOS = 3;
  CLIENT_LC = 4;
  CLIENT_RCN = 5;
  CLIENT_EVENTS = 6;
  CLIENT_INSIGHTS = 7;
  CLIENT_STATS = 8;
  CLIENT_COACH_ASSET_UPDATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00806"></a>
## FND-00806: chesscom.ceac.v2.Client.CLIENT_ANDROID = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_ANDROID = 2;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 147.

```text
tax: proto3

package chesscom.ceac.v2;

enum Client {
  CLIENT_UNSPECIFIED = 0;
  CLIENT_WEB = 1;
  CLIENT_ANDROID = 2;
  CLIENT_IOS = 3;
  CLIENT_LC = 4;
  CLIENT_RCN = 5;
  CLIENT_EVENTS = 6;
  CLIENT_INSIGHTS = 7;
  CLIENT_STATS = 8;
  CLIENT_COACH_ASSET_UPDATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00807"></a>
## FND-00807: chesscom.ceac.v2.Client.CLIENT_IOS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_IOS = 3;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 169.

```text
hesscom.ceac.v2;

enum Client {
  CLIENT_UNSPECIFIED = 0;
  CLIENT_WEB = 1;
  CLIENT_ANDROID = 2;
  CLIENT_IOS = 3;
  CLIENT_LC = 4;
  CLIENT_RCN = 5;
  CLIENT_EVENTS = 6;
  CLIENT_INSIGHTS = 7;
  CLIENT_STATS = 8;
  CLIENT_COACH_ASSET_UPDATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00808"></a>
## FND-00808: chesscom.ceac.v2.Client.CLIENT_LC = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_LC = 4;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 187.

```text
enum Client {
  CLIENT_UNSPECIFIED = 0;
  CLIENT_WEB = 1;
  CLIENT_ANDROID = 2;
  CLIENT_IOS = 3;
  CLIENT_LC = 4;
  CLIENT_RCN = 5;
  CLIENT_EVENTS = 6;
  CLIENT_INSIGHTS = 7;
  CLIENT_STATS = 8;
  CLIENT_COACH_ASSET_UPDATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_AN
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00809"></a>
## FND-00809: chesscom.ceac.v2.Client.CLIENT_RCN = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_RCN = 5;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 204.

```text
LIENT_UNSPECIFIED = 0;
  CLIENT_WEB = 1;
  CLIENT_ANDROID = 2;
  CLIENT_IOS = 3;
  CLIENT_LC = 4;
  CLIENT_RCN = 5;
  CLIENT_EVENTS = 6;
  CLIENT_INSIGHTS = 7;
  CLIENT_STATS = 8;
  CLIENT_COACH_ASSET_UPDATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLI
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00810"></a>
## FND-00810: chesscom.ceac.v2.Client.CLIENT_EVENTS = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_EVENTS = 6;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 222.

```text
= 0;
  CLIENT_WEB = 1;
  CLIENT_ANDROID = 2;
  CLIENT_IOS = 3;
  CLIENT_LC = 4;
  CLIENT_RCN = 5;
  CLIENT_EVENTS = 6;
  CLIENT_INSIGHTS = 7;
  CLIENT_STATS = 8;
  CLIENT_COACH_ASSET_UPDATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00811"></a>
## FND-00811: chesscom.ceac.v2.Client.CLIENT_INSIGHTS = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_INSIGHTS = 7;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 243.

```text
;
  CLIENT_ANDROID = 2;
  CLIENT_IOS = 3;
  CLIENT_LC = 4;
  CLIENT_RCN = 5;
  CLIENT_EVENTS = 6;
  CLIENT_INSIGHTS = 7;
  CLIENT_STATS = 8;
  CLIENT_COACH_ASSET_UPDATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRO
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00812"></a>
## FND-00812: chesscom.ceac.v2.Client.CLIENT_STATS = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_STATS = 8;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 266.

```text

  CLIENT_IOS = 3;
  CLIENT_LC = 4;
  CLIENT_RCN = 5;
  CLIENT_EVENTS = 6;
  CLIENT_INSIGHTS = 7;
  CLIENT_STATS = 8;
  CLIENT_COACH_ASSET_UPDATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRODUCT_UNSPECIFIED = 0;
 
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00813"></a>
## FND-00813: chesscom.ceac.v2.Client.CLIENT_COACH_ASSET_UPDATER = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_COACH_ASSET_UPDATER = 9;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 286.

```text
 CLIENT_LC = 4;
  CLIENT_RCN = 5;
  CLIENT_EVENTS = 6;
  CLIENT_INSIGHTS = 7;
  CLIENT_STATS = 8;
  CLIENT_COACH_ASSET_UPDATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRODUCT_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERN
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00814"></a>
## FND-00814: chesscom.ceac.v2.Client.CLIENT_EVAL_CACHE_GENERATOR = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_EVAL_CACHE_GENERATOR = 10;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 320.

```text
  CLIENT_EVENTS = 6;
  CLIENT_INSIGHTS = 7;
  CLIENT_STATS = 8;
  CLIENT_COACH_ASSET_UPDATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRODUCT_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00815"></a>
## FND-00815: chesscom.ceac.v2.Client.CLIENT_DEVELOPER = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_DEVELOPER = 11;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 356.

```text
TS = 7;
  CLIENT_STATS = 8;
  CLIENT_COACH_ASSET_UPDATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRODUCT_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_R
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00816"></a>
## FND-00816: chesscom.ceac.v2.Client.CLIENT_PUZZLE_GEN = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_PUZZLE_GEN = 12;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 381.

```text
8;
  CLIENT_COACH_ASSET_UPDATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRODUCT_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_RAGE_QUIT_DETECTION = 4;
 
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00817"></a>
## FND-00817: chesscom.ceac.v2.Client.CLIENT_TEXT_AUDIO = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_TEXT_AUDIO = 13;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 407.

```text
DATER = 9;
  CLIENT_EVAL_CACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRODUCT_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_RAGE_QUIT_DETECTION = 4;
  PRODUCT_FAIR_PLAY_PRODUCT
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00818"></a>
## FND-00818: chesscom.ceac.v2.Client.CLIENT_CHESSKID_WEB = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_CHESSKID_WEB = 14;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 433.

```text
ACHE_GENERATOR = 10;
  CLIENT_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRODUCT_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_RAGE_QUIT_DETECTION = 4;
  PRODUCT_FAIR_PLAY_PRODUCTION = 5;
  PRODUCT_FAIR_PL
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00819"></a>
## FND-00819: chesscom.ceac.v2.Client.CLIENT_CHESSKID_IOS = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_CHESSKID_IOS = 15;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 461.

```text
T_DEVELOPER = 11;
  CLIENT_PUZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRODUCT_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_RAGE_QUIT_DETECTION = 4;
  PRODUCT_FAIR_PLAY_PRODUCTION = 5;
  PRODUCT_FAIR_PLAY_RESEARCH = 6;
  PRODUCT_E
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00820"></a>
## FND-00820: chesscom.ceac.v2.Client.CLIENT_CHESSKID_ANDROID = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_CHESSKID_ANDROID = 16;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 489.

```text
UZZLE_GEN = 12;
  CLIENT_TEXT_AUDIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRODUCT_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_RAGE_QUIT_DETECTION = 4;
  PRODUCT_FAIR_PLAY_PRODUCTION = 5;
  PRODUCT_FAIR_PLAY_RESEARCH = 6;
  PRODUCT_EVENTS = 7;
  PRODUCT_ADVANCE
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00821"></a>
## FND-00821: chesscom.ceac.v2.Client.CLIENT_TRAIN = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_TRAIN = 17;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 521.

```text
DIO = 13;
  CLIENT_CHESSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRODUCT_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_RAGE_QUIT_DETECTION = 4;
  PRODUCT_FAIR_PLAY_PRODUCTION = 5;
  PRODUCT_FAIR_PLAY_RESEARCH = 6;
  PRODUCT_EVENTS = 7;
  PRODUCT_ADVANCED_STATS = 8;
  PRODUCT_CORE_CHES
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00822"></a>
## FND-00822: enum declaration: chesscom.ceac.v2.Product

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Product {

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 543.

```text
SSKID_WEB = 14;
  CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRODUCT_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_RAGE_QUIT_DETECTION = 4;
  PRODUCT_FAIR_PLAY_PRODUCTION = 5;
  PRODUCT_FAIR_PLAY_RESEARCH = 6;
  PRODUCT_EVENTS = 7;
  PRODUCT_ADVANCED_STATS = 8;
  PRODUCT_CORE_CHESS_RESEARCH = 9;
  PROD
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00823"></a>
## FND-00823: chesscom.ceac.v2.Product.PRODUCT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_UNSPECIFIED = 0;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 560.

```text
 CLIENT_CHESSKID_IOS = 15;
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRODUCT_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_RAGE_QUIT_DETECTION = 4;
  PRODUCT_FAIR_PLAY_PRODUCTION = 5;
  PRODUCT_FAIR_PLAY_RESEARCH = 6;
  PRODUCT_EVENTS = 7;
  PRODUCT_ADVANCED_STATS = 8;
  PRODUCT_CORE_CHESS_RESEARCH = 9;
  PRODUCT_PUZZLES = 10;
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00824"></a>
## FND-00824: chesscom.ceac.v2.Product.PRODUCT_CEAC_INTERNAL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_CEAC_INTERNAL = 1;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 587.

```text
  CLIENT_CHESSKID_ANDROID = 16;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRODUCT_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_RAGE_QUIT_DETECTION = 4;
  PRODUCT_FAIR_PLAY_PRODUCTION = 5;
  PRODUCT_FAIR_PLAY_RESEARCH = 6;
  PRODUCT_EVENTS = 7;
  PRODUCT_ADVANCED_STATS = 8;
  PRODUCT_CORE_CHESS_RESEARCH = 9;
  PRODUCT_PUZZLES = 10;
  PRODUCT_TEXT_AUDIO = 11;
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00825"></a>
## FND-00825: chesscom.ceac.v2.Product.PRODUCT_GAME_REVIEW = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_GAME_REVIEW = 2;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 616.

```text
6;
  CLIENT_TRAIN = 17;
}

enum Product {
  PRODUCT_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_RAGE_QUIT_DETECTION = 4;
  PRODUCT_FAIR_PLAY_PRODUCTION = 5;
  PRODUCT_FAIR_PLAY_RESEARCH = 6;
  PRODUCT_EVENTS = 7;
  PRODUCT_ADVANCED_STATS = 8;
  PRODUCT_CORE_CHESS_RESEARCH = 9;
  PRODUCT_PUZZLES = 10;
  PRODUCT_TEXT_AUDIO = 11;
  PRODUCT_BRILLIANT_VERIFICA
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00826"></a>
## FND-00826: chesscom.ceac.v2.Product.PRODUCT_INSIGHTS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_INSIGHTS = 3;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 643.

```text
enum Product {
  PRODUCT_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_RAGE_QUIT_DETECTION = 4;
  PRODUCT_FAIR_PLAY_PRODUCTION = 5;
  PRODUCT_FAIR_PLAY_RESEARCH = 6;
  PRODUCT_EVENTS = 7;
  PRODUCT_ADVANCED_STATS = 8;
  PRODUCT_CORE_CHESS_RESEARCH = 9;
  PRODUCT_PUZZLES = 10;
  PRODUCT_TEXT_AUDIO = 11;
  PRODUCT_BRILLIANT_VERIFICATION = 12;
  PRODUCT_TRAIN 
```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00827"></a>
## FND-00827: chesscom.ceac.v2.Product.PRODUCT_RAGE_QUIT_DETECTION = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_RAGE_QUIT_DETECTION = 4;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 667.

```text
_UNSPECIFIED = 0;
  PRODUCT_CEAC_INTERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_RAGE_QUIT_DETECTION = 4;
  PRODUCT_FAIR_PLAY_PRODUCTION = 5;
  PRODUCT_FAIR_PLAY_RESEARCH = 6;
  PRODUCT_EVENTS = 7;
  PRODUCT_ADVANCED_STATS = 8;
  PRODUCT_CORE_CHESS_RESEARCH = 9;
  PRODUCT_PUZZLES = 10;
  PRODUCT_TEXT_AUDIO = 11;
  PRODUCT_BRILLIANT_VERIFICATION = 12;
  PRODUCT_TRAIN = 13;
}

```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00828"></a>
## FND-00828: chesscom.ceac.v2.Product.PRODUCT_FAIR_PLAY_PRODUCTION = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_FAIR_PLAY_PRODUCTION = 5;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 702.

```text
TERNAL = 1;
  PRODUCT_GAME_REVIEW = 2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_RAGE_QUIT_DETECTION = 4;
  PRODUCT_FAIR_PLAY_PRODUCTION = 5;
  PRODUCT_FAIR_PLAY_RESEARCH = 6;
  PRODUCT_EVENTS = 7;
  PRODUCT_ADVANCED_STATS = 8;
  PRODUCT_CORE_CHESS_RESEARCH = 9;
  PRODUCT_PUZZLES = 10;
  PRODUCT_TEXT_AUDIO = 11;
  PRODUCT_BRILLIANT_VERIFICATION = 12;
  PRODUCT_TRAIN = 13;
}

```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00829"></a>
## FND-00829: chesscom.ceac.v2.Product.PRODUCT_FAIR_PLAY_RESEARCH = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_FAIR_PLAY_RESEARCH = 6;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 738.

```text
2;
  PRODUCT_INSIGHTS = 3;
  PRODUCT_RAGE_QUIT_DETECTION = 4;
  PRODUCT_FAIR_PLAY_PRODUCTION = 5;
  PRODUCT_FAIR_PLAY_RESEARCH = 6;
  PRODUCT_EVENTS = 7;
  PRODUCT_ADVANCED_STATS = 8;
  PRODUCT_CORE_CHESS_RESEARCH = 9;
  PRODUCT_PUZZLES = 10;
  PRODUCT_TEXT_AUDIO = 11;
  PRODUCT_BRILLIANT_VERIFICATION = 12;
  PRODUCT_TRAIN = 13;
}

```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00830"></a>
## FND-00830: chesscom.ceac.v2.Product.PRODUCT_EVENTS = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_EVENTS = 7;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 772.

```text
CT_RAGE_QUIT_DETECTION = 4;
  PRODUCT_FAIR_PLAY_PRODUCTION = 5;
  PRODUCT_FAIR_PLAY_RESEARCH = 6;
  PRODUCT_EVENTS = 7;
  PRODUCT_ADVANCED_STATS = 8;
  PRODUCT_CORE_CHESS_RESEARCH = 9;
  PRODUCT_PUZZLES = 10;
  PRODUCT_TEXT_AUDIO = 11;
  PRODUCT_BRILLIANT_VERIFICATION = 12;
  PRODUCT_TRAIN = 13;
}

```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00831"></a>
## FND-00831: chesscom.ceac.v2.Product.PRODUCT_ADVANCED_STATS = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_ADVANCED_STATS = 8;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 794.

```text
 = 4;
  PRODUCT_FAIR_PLAY_PRODUCTION = 5;
  PRODUCT_FAIR_PLAY_RESEARCH = 6;
  PRODUCT_EVENTS = 7;
  PRODUCT_ADVANCED_STATS = 8;
  PRODUCT_CORE_CHESS_RESEARCH = 9;
  PRODUCT_PUZZLES = 10;
  PRODUCT_TEXT_AUDIO = 11;
  PRODUCT_BRILLIANT_VERIFICATION = 12;
  PRODUCT_TRAIN = 13;
}

```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00832"></a>
## FND-00832: chesscom.ceac.v2.Product.PRODUCT_CORE_CHESS_RESEARCH = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_CORE_CHESS_RESEARCH = 9;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 824.

```text
UCTION = 5;
  PRODUCT_FAIR_PLAY_RESEARCH = 6;
  PRODUCT_EVENTS = 7;
  PRODUCT_ADVANCED_STATS = 8;
  PRODUCT_CORE_CHESS_RESEARCH = 9;
  PRODUCT_PUZZLES = 10;
  PRODUCT_TEXT_AUDIO = 11;
  PRODUCT_BRILLIANT_VERIFICATION = 12;
  PRODUCT_TRAIN = 13;
}

```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00833"></a>
## FND-00833: chesscom.ceac.v2.Product.PRODUCT_PUZZLES = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_PUZZLES = 10;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 859.

```text
EARCH = 6;
  PRODUCT_EVENTS = 7;
  PRODUCT_ADVANCED_STATS = 8;
  PRODUCT_CORE_CHESS_RESEARCH = 9;
  PRODUCT_PUZZLES = 10;
  PRODUCT_TEXT_AUDIO = 11;
  PRODUCT_BRILLIANT_VERIFICATION = 12;
  PRODUCT_TRAIN = 13;
}

```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00834"></a>
## FND-00834: chesscom.ceac.v2.Product.PRODUCT_TEXT_AUDIO = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_TEXT_AUDIO = 11;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 883.

```text
NTS = 7;
  PRODUCT_ADVANCED_STATS = 8;
  PRODUCT_CORE_CHESS_RESEARCH = 9;
  PRODUCT_PUZZLES = 10;
  PRODUCT_TEXT_AUDIO = 11;
  PRODUCT_BRILLIANT_VERIFICATION = 12;
  PRODUCT_TRAIN = 13;
}

```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00835"></a>
## FND-00835: chesscom.ceac.v2.Product.PRODUCT_BRILLIANT_VERIFICATION = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_BRILLIANT_VERIFICATION = 12;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 910.

```text
_STATS = 8;
  PRODUCT_CORE_CHESS_RESEARCH = 9;
  PRODUCT_PUZZLES = 10;
  PRODUCT_TEXT_AUDIO = 11;
  PRODUCT_BRILLIANT_VERIFICATION = 12;
  PRODUCT_TRAIN = 13;
}

```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00836"></a>
## FND-00836: chesscom.ceac.v2.Product.PRODUCT_TRAIN = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_TRAIN = 13;

### Evidence

- **SRC-0230** `research/proto/chesscom/ceac/v2/client.proto` — [preserved redacted evidence](../evidence/text/595f9ed304ae56c4abc02ba6ff9773f0f429719d69a3499e5dae218966b4fc9c.proto)
  Character offset 949.

```text
CH = 9;
  PRODUCT_PUZZLES = 10;
  PRODUCT_TEXT_AUDIO = 11;
  PRODUCT_BRILLIANT_VERIFICATION = 12;
  PRODUCT_TRAIN = 13;
}

```

**Source references:** SRC-0230, SRC-1201  
**URL references:** None independently associated  
**Related findings:** FND-00803, FND-00804, FND-00805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00837"></a>
## FND-00837: message declaration: chesscom.ceac.v2.NoCapacityError

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NoCapacityError {

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 86.

```text
// source: chesscom/ceac/v2/error.proto
// syntax: proto3

package chesscom.ceac.v2;

message NoCapacityError {
}

message InvalidGameError {
}

message GeneralError {
}

message BadRequest {
  oneof reason {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 1;
  .chesscom.explanation_engine.v1.UnanalyzableGame unanalyzable_game = 2;
  .chesscom.ceac.v2.InvalidRequestError invalid_request = 3
```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00838, FND-00839

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00838"></a>
## FND-00838: message declaration: chesscom.ceac.v2.InvalidGameError

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InvalidGameError {

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 115.

```text
scom/ceac/v2/error.proto
// syntax: proto3

package chesscom.ceac.v2;

message NoCapacityError {
}

message InvalidGameError {
}

message GeneralError {
}

message BadRequest {
  oneof reason {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 1;
  .chesscom.explanation_engine.v1.UnanalyzableGame unanalyzable_game = 2;
  .chesscom.ceac.v2.InvalidRequestError invalid_request = 3;
  }
}

message RateLimitedE
```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00839

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00839"></a>
## FND-00839: message declaration: chesscom.ceac.v2.GeneralError

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GeneralError {

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 145.

```text
ntax: proto3

package chesscom.ceac.v2;

message NoCapacityError {
}

message InvalidGameError {
}

message GeneralError {
}

message BadRequest {
  oneof reason {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 1;
  .chesscom.explanation_engine.v1.UnanalyzableGame unanalyzable_game = 2;
  .chesscom.ceac.v2.InvalidRequestError invalid_request = 3;
  }
}

message RateLimitedError {
}

message InvalidReque
```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00840"></a>
## FND-00840: message declaration: chesscom.ceac.v2.BadRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BadRequest {

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 171.

```text
scom.ceac.v2;

message NoCapacityError {
}

message InvalidGameError {
}

message GeneralError {
}

message BadRequest {
  oneof reason {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 1;
  .chesscom.explanation_engine.v1.UnanalyzableGame unanalyzable_game = 2;
  .chesscom.ceac.v2.InvalidRequestError invalid_request = 3;
  }
}

message RateLimitedError {
}

message InvalidRequestError {
}

message AuthR
```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00841"></a>
## FND-00841: oneof declaration: chesscom.ceac.v2.BadRequest.reason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof reason {

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 194.

```text
NoCapacityError {
}

message InvalidGameError {
}

message GeneralError {
}

message BadRequest {
  oneof reason {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 1;
  .chesscom.explanation_engine.v1.UnanalyzableGame unanalyzable_game = 2;
  .chesscom.ceac.v2.InvalidRequestError invalid_request = 3;
  }
}

message RateLimitedError {
}

message InvalidRequestError {
}

message AuthRequiredError {
}

messa
```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00842"></a>
## FND-00842: chesscom.ceac.v2.BadRequest.invalid_game = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.InvalidGame invalid_game = 1;

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 211.

```text

}

message InvalidGameError {
}

message GeneralError {
}

message BadRequest {
  oneof reason {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 1;
  .chesscom.explanation_engine.v1.UnanalyzableGame unanalyzable_game = 2;
  .chesscom.ceac.v2.InvalidRequestError invalid_request = 3;
  }
}

message RateLimitedError {
}

message InvalidRequestError {
}

message AuthRequiredError {
}

message ClientError {

```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00843"></a>
## FND-00843: chesscom.ceac.v2.BadRequest.unanalyzable_game = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.UnanalyzableGame unanalyzable_game = 2;

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 275.

```text
age BadRequest {
  oneof reason {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 1;
  .chesscom.explanation_engine.v1.UnanalyzableGame unanalyzable_game = 2;
  .chesscom.ceac.v2.InvalidRequestError invalid_request = 3;
  }
}

message RateLimitedError {
}

message InvalidRequestError {
}

message AuthRequiredError {
}

message ClientError {
  oneof reason {
  .chesscom.ceac.v2.BadRequest bad_request = 1;
```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00844"></a>
## FND-00844: chesscom.ceac.v2.BadRequest.invalid_request = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.InvalidRequestError invalid_request = 3;

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 349.

```text
dGame invalid_game = 1;
  .chesscom.explanation_engine.v1.UnanalyzableGame unanalyzable_game = 2;
  .chesscom.ceac.v2.InvalidRequestError invalid_request = 3;
  }
}

message RateLimitedError {
}

message InvalidRequestError {
}

message AuthRequiredError {
}

message ClientError {
  oneof reason {
  .chesscom.ceac.v2.BadRequest bad_request = 1;
  .chesscom.ceac.v2.RateLimitedError rate_limited = 2;
  .chesscom.ceac.v
```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00845"></a>
## FND-00845: message declaration: chesscom.ceac.v2.RateLimitedError

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RateLimitedError {

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 415.

```text
ableGame unanalyzable_game = 2;
  .chesscom.ceac.v2.InvalidRequestError invalid_request = 3;
  }
}

message RateLimitedError {
}

message InvalidRequestError {
}

message AuthRequiredError {
}

message ClientError {
  oneof reason {
  .chesscom.ceac.v2.BadRequest bad_request = 1;
  .chesscom.ceac.v2.RateLimitedError rate_limited = 2;
  .chesscom.ceac.v2.AuthRequiredError auth_required = 3;
  }
}

message ServerError 
```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00846"></a>
## FND-00846: message declaration: chesscom.ceac.v2.InvalidRequestError

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InvalidRequestError {

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 445.

```text
;
  .chesscom.ceac.v2.InvalidRequestError invalid_request = 3;
  }
}

message RateLimitedError {
}

message InvalidRequestError {
}

message AuthRequiredError {
}

message ClientError {
  oneof reason {
  .chesscom.ceac.v2.BadRequest bad_request = 1;
  .chesscom.ceac.v2.RateLimitedError rate_limited = 2;
  .chesscom.ceac.v2.AuthRequiredError auth_required = 3;
  }
}

message ServerError {
}

message FailureError {
  
```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00847"></a>
## FND-00847: message declaration: chesscom.ceac.v2.AuthRequiredError

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AuthRequiredError {

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 478.

```text
estError invalid_request = 3;
  }
}

message RateLimitedError {
}

message InvalidRequestError {
}

message AuthRequiredError {
}

message ClientError {
  oneof reason {
  .chesscom.ceac.v2.BadRequest bad_request = 1;
  .chesscom.ceac.v2.RateLimitedError rate_limited = 2;
  .chesscom.ceac.v2.AuthRequiredError auth_required = 3;
  }
}

message ServerError {
}

message FailureError {
  oneof kind {
  .chesscom.ceac.v2.
```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00848"></a>
## FND-00848: message declaration: chesscom.ceac.v2.ClientError

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ClientError {

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 509.

```text
 }
}

message RateLimitedError {
}

message InvalidRequestError {
}

message AuthRequiredError {
}

message ClientError {
  oneof reason {
  .chesscom.ceac.v2.BadRequest bad_request = 1;
  .chesscom.ceac.v2.RateLimitedError rate_limited = 2;
  .chesscom.ceac.v2.AuthRequiredError auth_required = 3;
  }
}

message ServerError {
}

message FailureError {
  oneof kind {
  .chesscom.ceac.v2.ClientError client_error = 1;
 
```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00849"></a>
## FND-00849: oneof declaration: chesscom.ceac.v2.ClientError.reason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof reason {

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 194.

```text
NoCapacityError {
}

message InvalidGameError {
}

message GeneralError {
}

message BadRequest {
  oneof reason {
  .chesscom.explanation_engine.v1.InvalidGame invalid_game = 1;
  .chesscom.explanation_engine.v1.UnanalyzableGame unanalyzable_game = 2;
  .chesscom.ceac.v2.InvalidRequestError invalid_request = 3;
  }
}

message RateLimitedError {
}

message InvalidRequestError {
}

message AuthRequiredError {
}

messa
```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00850"></a>
## FND-00850: chesscom.ceac.v2.ClientError.bad_request = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.BadRequest bad_request = 1;

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 550.

```text
ge InvalidRequestError {
}

message AuthRequiredError {
}

message ClientError {
  oneof reason {
  .chesscom.ceac.v2.BadRequest bad_request = 1;
  .chesscom.ceac.v2.RateLimitedError rate_limited = 2;
  .chesscom.ceac.v2.AuthRequiredError auth_required = 3;
  }
}

message ServerError {
}

message FailureError {
  oneof kind {
  .chesscom.ceac.v2.ClientError client_error = 1;
  .chesscom.ceac.v2.ServerError server_err
```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00851"></a>
## FND-00851: chesscom.ceac.v2.ClientError.rate_limited = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.RateLimitedError rate_limited = 2;

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 598.

```text
Error {
}

message ClientError {
  oneof reason {
  .chesscom.ceac.v2.BadRequest bad_request = 1;
  .chesscom.ceac.v2.RateLimitedError rate_limited = 2;
  .chesscom.ceac.v2.AuthRequiredError auth_required = 3;
  }
}

message ServerError {
}

message FailureError {
  oneof kind {
  .chesscom.ceac.v2.ClientError client_error = 1;
  .chesscom.ceac.v2.ServerError server_error = 2;
  }
}

```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00852"></a>
## FND-00852: chesscom.ceac.v2.ClientError.auth_required = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.AuthRequiredError auth_required = 3;

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 653.

```text
esscom.ceac.v2.BadRequest bad_request = 1;
  .chesscom.ceac.v2.RateLimitedError rate_limited = 2;
  .chesscom.ceac.v2.AuthRequiredError auth_required = 3;
  }
}

message ServerError {
}

message FailureError {
  oneof kind {
  .chesscom.ceac.v2.ClientError client_error = 1;
  .chesscom.ceac.v2.ServerError server_error = 2;
  }
}

```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00853"></a>
## FND-00853: message declaration: chesscom.ceac.v2.ServerError

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ServerError {

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 715.

```text
.RateLimitedError rate_limited = 2;
  .chesscom.ceac.v2.AuthRequiredError auth_required = 3;
  }
}

message ServerError {
}

message FailureError {
  oneof kind {
  .chesscom.ceac.v2.ClientError client_error = 1;
  .chesscom.ceac.v2.ServerError server_error = 2;
  }
}

```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00854"></a>
## FND-00854: message declaration: chesscom.ceac.v2.FailureError

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FailureError {

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 740.

```text
mited = 2;
  .chesscom.ceac.v2.AuthRequiredError auth_required = 3;
  }
}

message ServerError {
}

message FailureError {
  oneof kind {
  .chesscom.ceac.v2.ClientError client_error = 1;
  .chesscom.ceac.v2.ServerError server_error = 2;
  }
}

```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00855"></a>
## FND-00855: oneof declaration: chesscom.ceac.v2.FailureError.kind

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof kind {

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 765.

```text
ac.v2.AuthRequiredError auth_required = 3;
  }
}

message ServerError {
}

message FailureError {
  oneof kind {
  .chesscom.ceac.v2.ClientError client_error = 1;
  .chesscom.ceac.v2.ServerError server_error = 2;
  }
}

```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00856"></a>
## FND-00856: chesscom.ceac.v2.FailureError.client_error = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.ClientError client_error = 1;

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 780.

```text
redError auth_required = 3;
  }
}

message ServerError {
}

message FailureError {
  oneof kind {
  .chesscom.ceac.v2.ClientError client_error = 1;
  .chesscom.ceac.v2.ServerError server_error = 2;
  }
}

```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00857"></a>
## FND-00857: chesscom.ceac.v2.FailureError.server_error = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.ServerError server_error = 2;

### Evidence

- **SRC-0231** `research/proto/chesscom/ceac/v2/error.proto` — [preserved redacted evidence](../evidence/text/785995c5e09da92ee3101b70736081197b1577f82a3c8a0b749b90dc35a1e4c9.proto)
  Character offset 830.

```text
rror {
}

message FailureError {
  oneof kind {
  .chesscom.ceac.v2.ClientError client_error = 1;
  .chesscom.ceac.v2.ServerError server_error = 2;
  }
}

```

**Source references:** SRC-0231, SRC-1202  
**URL references:** None independently associated  
**Related findings:** FND-00837, FND-00838, FND-00839

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00858"></a>
## FND-00858: message declaration: chesscom.ceac.v2.GameEvaluationOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameEvaluationOptions {

### Evidence

- **SRC-0232** `research/proto/chesscom/ceac/v2/game_evaluation_options.proto` — [preserved redacted evidence](../evidence/text/25f396a74705134d41b92ab9ebbcb0dd42b6c89a16be9a2e046376677fa67fca.proto)
  Character offset 104.

```text
ource: chesscom/ceac/v2/game_evaluation_options.proto
// syntax: proto3

package chesscom.ceac.v2;

message GameEvaluationOptions {
  optional bool use_game_state_cache = 1;
  optional bool use_serial_evaluations = 2;
}

```

**Source references:** SRC-0232, SRC-1203  
**URL references:** None independently associated  
**Related findings:** FND-00859, FND-00860

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00859"></a>
## FND-00859: chesscom.ceac.v2.GameEvaluationOptions.use_game_state_cache = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool use_game_state_cache = 1;

### Evidence

- **SRC-0232** `research/proto/chesscom/ceac/v2/game_evaluation_options.proto` — [preserved redacted evidence](../evidence/text/25f396a74705134d41b92ab9ebbcb0dd42b6c89a16be9a2e046376677fa67fca.proto)
  Character offset 138.

```text
ation_options.proto
// syntax: proto3

package chesscom.ceac.v2;

message GameEvaluationOptions {
  optional bool use_game_state_cache = 1;
  optional bool use_serial_evaluations = 2;
}

```

**Source references:** SRC-0232, SRC-1203  
**URL references:** None independently associated  
**Related findings:** FND-00858, FND-00860

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00860"></a>
## FND-00860: chesscom.ceac.v2.GameEvaluationOptions.use_serial_evaluations = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool use_serial_evaluations = 2;

### Evidence

- **SRC-0232** `research/proto/chesscom/ceac/v2/game_evaluation_options.proto` — [preserved redacted evidence](../evidence/text/25f396a74705134d41b92ab9ebbcb0dd42b6c89a16be9a2e046376677fa67fca.proto)
  Character offset 180.

```text
kage chesscom.ceac.v2;

message GameEvaluationOptions {
  optional bool use_game_state_cache = 1;
  optional bool use_serial_evaluations = 2;
}

```

**Source references:** SRC-0232, SRC-1203  
**URL references:** None independently associated  
**Related findings:** FND-00858, FND-00859

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00861"></a>
## FND-00861: message declaration: chesscom.ceac.v2.GameReviewRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewRequest {

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 92.

```text
// source: chesscom/ceac/v2/game_review.proto
// syntax: proto3

package chesscom.ceac.v2;

message GameReviewRequest {
  optional .chesscom.explanation_engine.v1.NewGameRequest new_game_req = 1;
  optional .chesscom.explanation_engine.v1.RunSearchRequest run_search_req = 2;
  optional .chesscom.explanation_engine.v1.CharmInferenceRequest charm_inf_req = 8;
  optional .chesscom.engine.v1.Engine engine = 3;
  
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00862, FND-00863

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00862"></a>
## FND-00862: chesscom.ceac.v2.GameReviewRequest.new_game_req = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.NewGameRequest new_game_req = 1;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 122.

```text
ac/v2/game_review.proto
// syntax: proto3

package chesscom.ceac.v2;

message GameReviewRequest {
  optional .chesscom.explanation_engine.v1.NewGameRequest new_game_req = 1;
  optional .chesscom.explanation_engine.v1.RunSearchRequest run_search_req = 2;
  optional .chesscom.explanation_engine.v1.CharmInferenceRequest charm_inf_req = 8;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional .chesscom.ceac.v2.Gam
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00863"></a>
## FND-00863: chesscom.ceac.v2.GameReviewRequest.run_search_req = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.RunSearchRequest run_search_req = 2;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 198.

```text
e GameReviewRequest {
  optional .chesscom.explanation_engine.v1.NewGameRequest new_game_req = 1;
  optional .chesscom.explanation_engine.v1.RunSearchRequest run_search_req = 2;
  optional .chesscom.explanation_engine.v1.CharmInferenceRequest charm_inf_req = 8;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional .chesscom.ceac.v2.GameEvaluationOptions game_evaluation_options = 4;
  optional .chesscom.ceac.v2
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00864"></a>
## FND-00864: chesscom.ceac.v2.GameReviewRequest.charm_inf_req = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CharmInferenceRequest charm_inf_req = 8;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 278.

```text
new_game_req = 1;
  optional .chesscom.explanation_engine.v1.RunSearchRequest run_search_req = 2;
  optional .chesscom.explanation_engine.v1.CharmInferenceRequest charm_inf_req = 8;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional .chesscom.ceac.v2.GameEvaluationOptions game_evaluation_options = 4;
  optional .chesscom.ceac.v2.RequestMetadata request_metadata = 5;
  optional .chesscom.ceac.v2.RequestOptio
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00865"></a>
## FND-00865: chesscom.ceac.v2.GameReviewRequest.engine = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.engine.v1.Engine engine = 3;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 362.

```text
arch_req = 2;
  optional .chesscom.explanation_engine.v1.CharmInferenceRequest charm_inf_req = 8;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional .chesscom.ceac.v2.GameEvaluationOptions game_evaluation_options = 4;
  optional .chesscom.ceac.v2.RequestMetadata request_metadata = 5;
  optional .chesscom.ceac.v2.RequestOptions request_options = 6;
  optional .chesscom.explanation_engine.v1.SetCoachRequest s
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00866"></a>
## FND-00866: chesscom.ceac.v2.GameReviewRequest.game_evaluation_options = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ceac.v2.GameEvaluationOptions game_evaluation_options = 4;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 412.

```text
ine.v1.CharmInferenceRequest charm_inf_req = 8;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional .chesscom.ceac.v2.GameEvaluationOptions game_evaluation_options = 4;
  optional .chesscom.ceac.v2.RequestMetadata request_metadata = 5;
  optional .chesscom.ceac.v2.RequestOptions request_options = 6;
  optional .chesscom.explanation_engine.v1.SetCoachRequest set_coach = 7;
  optional .chesscom.ceac.v2.GameRev
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00867"></a>
## FND-00867: chesscom.ceac.v2.GameReviewRequest.request_metadata = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ceac.v2.RequestMetadata request_metadata = 5;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 492.

```text
ngine engine = 3;
  optional .chesscom.ceac.v2.GameEvaluationOptions game_evaluation_options = 4;
  optional .chesscom.ceac.v2.RequestMetadata request_metadata = 5;
  optional .chesscom.ceac.v2.RequestOptions request_options = 6;
  optional .chesscom.explanation_engine.v1.SetCoachRequest set_coach = 7;
  optional .chesscom.ceac.v2.GameReviewOptions game_review_options = 9;
}

message GameReviewResponse {
  oneof resu
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00868"></a>
## FND-00868: chesscom.ceac.v2.GameReviewRequest.request_options = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ceac.v2.RequestOptions request_options = 6;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 559.

```text
s game_evaluation_options = 4;
  optional .chesscom.ceac.v2.RequestMetadata request_metadata = 5;
  optional .chesscom.ceac.v2.RequestOptions request_options = 6;
  optional .chesscom.explanation_engine.v1.SetCoachRequest set_coach = 7;
  optional .chesscom.ceac.v2.GameReviewOptions game_review_options = 9;
}

message GameReviewResponse {
  oneof result {
  .chesscom.ceac.v2.GameReviewResponseProgress progress = 1;
 
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00869"></a>
## FND-00869: chesscom.ceac.v2.GameReviewRequest.set_coach = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.SetCoachRequest set_coach = 7;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 624.

```text
stMetadata request_metadata = 5;
  optional .chesscom.ceac.v2.RequestOptions request_options = 6;
  optional .chesscom.explanation_engine.v1.SetCoachRequest set_coach = 7;
  optional .chesscom.ceac.v2.GameReviewOptions game_review_options = 9;
}

message GameReviewResponse {
  oneof result {
  .chesscom.ceac.v2.GameReviewResponseProgress progress = 1;
  .chesscom.ceac.v2.GameReviewResponseSuccess success = 2;
  .ches
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00870"></a>
## FND-00870: chesscom.ceac.v2.GameReviewRequest.game_review_options = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ceac.v2.GameReviewOptions game_review_options = 9;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 698.

```text
ns request_options = 6;
  optional .chesscom.explanation_engine.v1.SetCoachRequest set_coach = 7;
  optional .chesscom.ceac.v2.GameReviewOptions game_review_options = 9;
}

message GameReviewResponse {
  oneof result {
  .chesscom.ceac.v2.GameReviewResponseProgress progress = 1;
  .chesscom.ceac.v2.GameReviewResponseSuccess success = 2;
  .chesscom.ceac.v2.GameReviewResponseFailure failure = 3;
  .chesscom.ceac.v2.He
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00871"></a>
## FND-00871: message declaration: chesscom.ceac.v2.GameReviewResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewResponse {

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 771.

```text
chRequest set_coach = 7;
  optional .chesscom.ceac.v2.GameReviewOptions game_review_options = 9;
}

message GameReviewResponse {
  oneof result {
  .chesscom.ceac.v2.GameReviewResponseProgress progress = 1;
  .chesscom.ceac.v2.GameReviewResponseSuccess success = 2;
  .chesscom.ceac.v2.GameReviewResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00872"></a>
## FND-00872: oneof declaration: chesscom.ceac.v2.GameReviewResponse.result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof result {

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 802.

```text
onal .chesscom.ceac.v2.GameReviewOptions game_review_options = 9;
}

message GameReviewResponse {
  oneof result {
  .chesscom.ceac.v2.GameReviewResponseProgress progress = 1;
  .chesscom.ceac.v2.GameReviewResponseSuccess success = 2;
  .chesscom.ceac.v2.GameReviewResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message G
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00873"></a>
## FND-00873: chesscom.ceac.v2.GameReviewResponse.progress = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.GameReviewResponseProgress progress = 1;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 819.

```text
ac.v2.GameReviewOptions game_review_options = 9;
}

message GameReviewResponse {
  oneof result {
  .chesscom.ceac.v2.GameReviewResponseProgress progress = 1;
  .chesscom.ceac.v2.GameReviewResponseSuccess success = 2;
  .chesscom.ceac.v2.GameReviewResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message GameReviewResponse
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00874"></a>
## FND-00874: chesscom.ceac.v2.GameReviewResponse.success = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.GameReviewResponseSuccess success = 2;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 880.

```text
ameReviewResponse {
  oneof result {
  .chesscom.ceac.v2.GameReviewResponseProgress progress = 1;
  .chesscom.ceac.v2.GameReviewResponseSuccess success = 2;
  .chesscom.ceac.v2.GameReviewResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message GameReviewResponseSuccess {
  optional .chesscom.explanation_engine.v1.GameRevi
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
