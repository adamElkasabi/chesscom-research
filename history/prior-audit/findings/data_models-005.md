# data_models — findings 401–500

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-00675"></a>
## FND-00675: oneof declaration: chesscom.bots.v1.BotPersonality._crown_earned

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _crown_earned {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1581.

```text
string theme_uuid = 27;
  }
  oneof _minimum_cee_version {
  string minimum_cee_version = 28;
  }
  oneof _crown_earned {
  int32 crown_earned = 29;
  }
  oneof _image_url {
  string image_url = 30;
  }
  oneof _image_url_override {
  string image_url_override = 31;
  }
  oneof _v2_spread_sheet {
  string v2_spread_sheet = 33;
  }
  oneof _book_fallback {
  string book_fallback = 35;
  }
  oneof _can_play {
  bool ca
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00676"></a>
## FND-00676: chesscom.bots.v1.BotPersonality.crown_earned = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 crown_earned = 29;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1605.

```text
  }
  oneof _minimum_cee_version {
  string minimum_cee_version = 28;
  }
  oneof _crown_earned {
  int32 crown_earned = 29;
  }
  oneof _image_url {
  string image_url = 30;
  }
  oneof _image_url_override {
  string image_url_override = 31;
  }
  oneof _v2_spread_sheet {
  string v2_spread_sheet = 33;
  }
  oneof _book_fallback {
  string book_fallback = 35;
  }
  oneof _can_play {
  bool can_play = 36;
  }
  oneof
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00677"></a>
## FND-00677: oneof declaration: chesscom.bots.v1.BotPersonality._image_url

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _image_url {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1636.

```text
n {
  string minimum_cee_version = 28;
  }
  oneof _crown_earned {
  int32 crown_earned = 29;
  }
  oneof _image_url {
  string image_url = 30;
  }
  oneof _image_url_override {
  string image_url_override = 31;
  }
  oneof _v2_spread_sheet {
  string v2_spread_sheet = 33;
  }
  oneof _book_fallback {
  string book_fallback = 35;
  }
  oneof _can_play {
  bool can_play = 36;
  }
  oneof _fen_as_black {
  string fen_a
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00678"></a>
## FND-00678: chesscom.bots.v1.BotPersonality.image_url = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string image_url = 30;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1657.

```text
cee_version = 28;
  }
  oneof _crown_earned {
  int32 crown_earned = 29;
  }
  oneof _image_url {
  string image_url = 30;
  }
  oneof _image_url_override {
  string image_url_override = 31;
  }
  oneof _v2_spread_sheet {
  string v2_spread_sheet = 33;
  }
  oneof _book_fallback {
  string book_fallback = 35;
  }
  oneof _can_play {
  bool can_play = 36;
  }
  oneof _fen_as_black {
  string fen_as_black = 37;
  }
  o
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00679"></a>
## FND-00679: oneof declaration: chesscom.bots.v1.BotPersonality._image_url_override

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _image_url_override {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1686.

```text
 _crown_earned {
  int32 crown_earned = 29;
  }
  oneof _image_url {
  string image_url = 30;
  }
  oneof _image_url_override {
  string image_url_override = 31;
  }
  oneof _v2_spread_sheet {
  string v2_spread_sheet = 33;
  }
  oneof _book_fallback {
  string book_fallback = 35;
  }
  oneof _can_play {
  bool can_play = 36;
  }
  oneof _fen_as_black {
  string fen_as_black = 37;
  }
  oneof _fen_as_white {
  string
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00680"></a>
## FND-00680: chesscom.bots.v1.BotPersonality.image_url_override = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string image_url_override = 31;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1716.

```text
_earned = 29;
  }
  oneof _image_url {
  string image_url = 30;
  }
  oneof _image_url_override {
  string image_url_override = 31;
  }
  oneof _v2_spread_sheet {
  string v2_spread_sheet = 33;
  }
  oneof _book_fallback {
  string book_fallback = 35;
  }
  oneof _can_play {
  bool can_play = 36;
  }
  oneof _fen_as_black {
  string fen_as_black = 37;
  }
  oneof _fen_as_white {
  string fen_as_white = 38;
  }
  oneo
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00681"></a>
## FND-00681: oneof declaration: chesscom.bots.v1.BotPersonality._v2_spread_sheet

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _v2_spread_sheet {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1754.

```text

  string image_url = 30;
  }
  oneof _image_url_override {
  string image_url_override = 31;
  }
  oneof _v2_spread_sheet {
  string v2_spread_sheet = 33;
  }
  oneof _book_fallback {
  string book_fallback = 35;
  }
  oneof _can_play {
  bool can_play = 36;
  }
  oneof _fen_as_black {
  string fen_as_black = 37;
  }
  oneof _fen_as_white {
  string fen_as_white = 38;
  }
  oneof _avatar_without_background {
  strin
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00682"></a>
## FND-00682: chesscom.bots.v1.BotPersonality.v2_spread_sheet = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string v2_spread_sheet = 33;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1781.

```text
 }
  oneof _image_url_override {
  string image_url_override = 31;
  }
  oneof _v2_spread_sheet {
  string v2_spread_sheet = 33;
  }
  oneof _book_fallback {
  string book_fallback = 35;
  }
  oneof _can_play {
  bool can_play = 36;
  }
  oneof _fen_as_black {
  string fen_as_black = 37;
  }
  oneof _fen_as_white {
  string fen_as_white = 38;
  }
  oneof _avatar_without_background {
  string avatar_without_background
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00683"></a>
## FND-00683: oneof declaration: chesscom.bots.v1.BotPersonality._book_fallback

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _book_fallback {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1816.

```text
string image_url_override = 31;
  }
  oneof _v2_spread_sheet {
  string v2_spread_sheet = 33;
  }
  oneof _book_fallback {
  string book_fallback = 35;
  }
  oneof _can_play {
  bool can_play = 36;
  }
  oneof _fen_as_black {
  string fen_as_black = 37;
  }
  oneof _fen_as_white {
  string fen_as_white = 38;
  }
  oneof _avatar_without_background {
  string avatar_without_background = 39;
  }
  oneof _has_custom_moda
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00684"></a>
## FND-00684: chesscom.bots.v1.BotPersonality.book_fallback = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string book_fallback = 35;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1841.

```text
 = 31;
  }
  oneof _v2_spread_sheet {
  string v2_spread_sheet = 33;
  }
  oneof _book_fallback {
  string book_fallback = 35;
  }
  oneof _can_play {
  bool can_play = 36;
  }
  oneof _fen_as_black {
  string fen_as_black = 37;
  }
  oneof _fen_as_white {
  string fen_as_white = 38;
  }
  oneof _avatar_without_background {
  string avatar_without_background = 39;
  }
  oneof _has_custom_modal {
  bool has_custom_mod
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00685"></a>
## FND-00685: oneof declaration: chesscom.bots.v1.BotPersonality._can_play

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _can_play {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1874.

```text
et {
  string v2_spread_sheet = 33;
  }
  oneof _book_fallback {
  string book_fallback = 35;
  }
  oneof _can_play {
  bool can_play = 36;
  }
  oneof _fen_as_black {
  string fen_as_black = 37;
  }
  oneof _fen_as_white {
  string fen_as_white = 38;
  }
  oneof _avatar_without_background {
  string avatar_without_background = 39;
  }
  oneof _has_custom_modal {
  bool has_custom_modal = 40;
  }
  oneof _custom_moda
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00686"></a>
## FND-00686: chesscom.bots.v1.BotPersonality.can_play = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool can_play = 36;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1894.

```text
ead_sheet = 33;
  }
  oneof _book_fallback {
  string book_fallback = 35;
  }
  oneof _can_play {
  bool can_play = 36;
  }
  oneof _fen_as_black {
  string fen_as_black = 37;
  }
  oneof _fen_as_white {
  string fen_as_white = 38;
  }
  oneof _avatar_without_background {
  string avatar_without_background = 39;
  }
  oneof _has_custom_modal {
  bool has_custom_modal = 40;
  }
  oneof _custom_modal_requires_account_a
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00687"></a>
## FND-00687: oneof declaration: chesscom.bots.v1.BotPersonality._fen_as_black

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _fen_as_black {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1920.

```text
f _book_fallback {
  string book_fallback = 35;
  }
  oneof _can_play {
  bool can_play = 36;
  }
  oneof _fen_as_black {
  string fen_as_black = 37;
  }
  oneof _fen_as_white {
  string fen_as_white = 38;
  }
  oneof _avatar_without_background {
  string avatar_without_background = 39;
  }
  oneof _has_custom_modal {
  bool has_custom_modal = 40;
  }
  oneof _custom_modal_requires_account_activation {
  bool custom_
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00688"></a>
## FND-00688: chesscom.bots.v1.BotPersonality.fen_as_black = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string fen_as_black = 37;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1944.

```text
ing book_fallback = 35;
  }
  oneof _can_play {
  bool can_play = 36;
  }
  oneof _fen_as_black {
  string fen_as_black = 37;
  }
  oneof _fen_as_white {
  string fen_as_white = 38;
  }
  oneof _avatar_without_background {
  string avatar_without_background = 39;
  }
  oneof _has_custom_modal {
  bool has_custom_modal = 40;
  }
  oneof _custom_modal_requires_account_activation {
  bool custom_modal_requires_account_a
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00689"></a>
## FND-00689: oneof declaration: chesscom.bots.v1.BotPersonality._fen_as_white

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _fen_as_white {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 1976.

```text
eof _can_play {
  bool can_play = 36;
  }
  oneof _fen_as_black {
  string fen_as_black = 37;
  }
  oneof _fen_as_white {
  string fen_as_white = 38;
  }
  oneof _avatar_without_background {
  string avatar_without_background = 39;
  }
  oneof _has_custom_modal {
  bool has_custom_modal = 40;
  }
  oneof _custom_modal_requires_account_activation {
  bool custom_modal_requires_account_activation = 41;
  }
  oneof _pro
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00690"></a>
## FND-00690: chesscom.bots.v1.BotPersonality.fen_as_white = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string fen_as_white = 38;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2000.

```text
an_play = 36;
  }
  oneof _fen_as_black {
  string fen_as_black = 37;
  }
  oneof _fen_as_white {
  string fen_as_white = 38;
  }
  oneof _avatar_without_background {
  string avatar_without_background = 39;
  }
  oneof _has_custom_modal {
  bool has_custom_modal = 40;
  }
  oneof _custom_modal_requires_account_activation {
  bool custom_modal_requires_account_activation = 41;
  }
  oneof _properties {
  .chesscom.bo
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00691"></a>
## FND-00691: oneof declaration: chesscom.bots.v1.BotPersonality._avatar_without_background

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _avatar_without_background {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2032.

```text
s_black {
  string fen_as_black = 37;
  }
  oneof _fen_as_white {
  string fen_as_white = 38;
  }
  oneof _avatar_without_background {
  string avatar_without_background = 39;
  }
  oneof _has_custom_modal {
  bool has_custom_modal = 40;
  }
  oneof _custom_modal_requires_account_activation {
  bool custom_modal_requires_account_activation = 41;
  }
  oneof _properties {
  .chesscom.bots.v1.BotProperties properties =
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00692"></a>
## FND-00692: chesscom.bots.v1.BotPersonality.avatar_without_background = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string avatar_without_background = 39;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2069.

```text

  }
  oneof _fen_as_white {
  string fen_as_white = 38;
  }
  oneof _avatar_without_background {
  string avatar_without_background = 39;
  }
  oneof _has_custom_modal {
  bool has_custom_modal = 40;
  }
  oneof _custom_modal_requires_account_activation {
  bool custom_modal_requires_account_activation = 41;
  }
  oneof _properties {
  .chesscom.bots.v1.BotProperties properties = 42;
  }
  oneof _bot_move_configurat
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00693"></a>
## FND-00693: oneof declaration: chesscom.bots.v1.BotPersonality._has_custom_modal

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _has_custom_modal {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2114.

```text
white = 38;
  }
  oneof _avatar_without_background {
  string avatar_without_background = 39;
  }
  oneof _has_custom_modal {
  bool has_custom_modal = 40;
  }
  oneof _custom_modal_requires_account_activation {
  bool custom_modal_requires_account_activation = 41;
  }
  oneof _properties {
  .chesscom.bots.v1.BotProperties properties = 42;
  }
  oneof _bot_move_configuration_key {
  string bot_move_configuration_key
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00694"></a>
## FND-00694: chesscom.bots.v1.BotPersonality.has_custom_modal = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool has_custom_modal = 40;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2142.

```text
tar_without_background {
  string avatar_without_background = 39;
  }
  oneof _has_custom_modal {
  bool has_custom_modal = 40;
  }
  oneof _custom_modal_requires_account_activation {
  bool custom_modal_requires_account_activation = 41;
  }
  oneof _properties {
  .chesscom.bots.v1.BotProperties properties = 42;
  }
  oneof _bot_move_configuration_key {
  string bot_move_configuration_key = 43;
  }
  optional string
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00695"></a>
## FND-00695: oneof declaration: chesscom.bots.v1.BotPersonality._custom_modal_requires_account_activation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _custom_modal_requires_account_activation {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2176.

```text
avatar_without_background = 39;
  }
  oneof _has_custom_modal {
  bool has_custom_modal = 40;
  }
  oneof _custom_modal_requires_account_activation {
  bool custom_modal_requires_account_activation = 41;
  }
  oneof _properties {
  .chesscom.bots.v1.BotProperties properties = 42;
  }
  oneof _bot_move_configuration_key {
  string bot_move_configuration_key = 43;
  }
  optional string id = 1;
  optional int32 sort_ord
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00696"></a>
## FND-00696: chesscom.bots.v1.BotPersonality.custom_modal_requires_account_activation = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool custom_modal_requires_account_activation = 41;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2228.

```text
tom_modal {
  bool has_custom_modal = 40;
  }
  oneof _custom_modal_requires_account_activation {
  bool custom_modal_requires_account_activation = 41;
  }
  oneof _properties {
  .chesscom.bots.v1.BotProperties properties = 42;
  }
  oneof _bot_move_configuration_key {
  string bot_move_configuration_key = 43;
  }
  optional string id = 1;
  optional int32 sort_order = 2;
  optional bool enabled = 3;
  optional stri
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00697"></a>
## FND-00697: oneof declaration: chesscom.bots.v1.BotPersonality._properties

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _properties {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2286.

```text
tom_modal_requires_account_activation {
  bool custom_modal_requires_account_activation = 41;
  }
  oneof _properties {
  .chesscom.bots.v1.BotProperties properties = 42;
  }
  oneof _bot_move_configuration_key {
  string bot_move_configuration_key = 43;
  }
  optional string id = 1;
  optional int32 sort_order = 2;
  optional bool enabled = 3;
  optional string username = 4;
  optional string classification = 5;
  o
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00698"></a>
## FND-00698: chesscom.bots.v1.BotPersonality.properties = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.bots.v1.BotProperties properties = 42;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2308.

```text
ount_activation {
  bool custom_modal_requires_account_activation = 41;
  }
  oneof _properties {
  .chesscom.bots.v1.BotProperties properties = 42;
  }
  oneof _bot_move_configuration_key {
  string bot_move_configuration_key = 43;
  }
  optional string id = 1;
  optional int32 sort_order = 2;
  optional bool enabled = 3;
  optional string username = 4;
  optional string classification = 5;
  optional .google.protob
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00699"></a>
## FND-00699: oneof declaration: chesscom.bots.v1.BotPersonality._bot_move_configuration_key

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _bot_move_configuration_key {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2363.

```text
activation = 41;
  }
  oneof _properties {
  .chesscom.bots.v1.BotProperties properties = 42;
  }
  oneof _bot_move_configuration_key {
  string bot_move_configuration_key = 43;
  }
  optional string id = 1;
  optional int32 sort_order = 2;
  optional bool enabled = 3;
  optional string username = 4;
  optional string classification = 5;
  optional .google.protobuf.Timestamp updated_at = 6;
  optional string name = 7
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00700"></a>
## FND-00700: chesscom.bots.v1.BotPersonality.bot_move_configuration_key = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string bot_move_configuration_key = 43;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2401.

```text
es {
  .chesscom.bots.v1.BotProperties properties = 42;
  }
  oneof _bot_move_configuration_key {
  string bot_move_configuration_key = 43;
  }
  optional string id = 1;
  optional int32 sort_order = 2;
  optional bool enabled = 3;
  optional string username = 4;
  optional string classification = 5;
  optional .google.protobuf.Timestamp updated_at = 6;
  optional string name = 7;
  optional int32 user_id = 8;
  opti
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00701"></a>
## FND-00701: chesscom.bots.v1.BotPersonality.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2447.

```text
ies = 42;
  }
  oneof _bot_move_configuration_key {
  string bot_move_configuration_key = 43;
  }
  optional string id = 1;
  optional int32 sort_order = 2;
  optional bool enabled = 3;
  optional string username = 4;
  optional string classification = 5;
  optional .google.protobuf.Timestamp updated_at = 6;
  optional string name = 7;
  optional int32 user_id = 8;
  optional string classification_hint_text = 9;
  op
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00702"></a>
## FND-00702: chesscom.bots.v1.BotPersonality.sort_order = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 sort_order = 2;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2473.

```text
_move_configuration_key {
  string bot_move_configuration_key = 43;
  }
  optional string id = 1;
  optional int32 sort_order = 2;
  optional bool enabled = 3;
  optional string username = 4;
  optional string classification = 5;
  optional .google.protobuf.Timestamp updated_at = 6;
  optional string name = 7;
  optional int32 user_id = 8;
  optional string classification_hint_text = 9;
  optional .chesscom.bots.v1.P
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00703"></a>
## FND-00703: chesscom.bots.v1.BotPersonality.enabled = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enabled = 3;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2506.

```text
g bot_move_configuration_key = 43;
  }
  optional string id = 1;
  optional int32 sort_order = 2;
  optional bool enabled = 3;
  optional string username = 4;
  optional string classification = 5;
  optional .google.protobuf.Timestamp updated_at = 6;
  optional string name = 7;
  optional int32 user_id = 8;
  optional string classification_hint_text = 9;
  optional .chesscom.bots.v1.Personality personality = 15;
  op
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00704"></a>
## FND-00704: chesscom.bots.v1.BotPersonality.username = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string username = 4;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2535.

```text
= 43;
  }
  optional string id = 1;
  optional int32 sort_order = 2;
  optional bool enabled = 3;
  optional string username = 4;
  optional string classification = 5;
  optional .google.protobuf.Timestamp updated_at = 6;
  optional string name = 7;
  optional int32 user_id = 8;
  optional string classification_hint_text = 9;
  optional .chesscom.bots.v1.Personality personality = 15;
  optional bool v2 = 26;
  option
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00705"></a>
## FND-00705: chesscom.bots.v1.BotPersonality.classification = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string classification = 5;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2567.

```text
 1;
  optional int32 sort_order = 2;
  optional bool enabled = 3;
  optional string username = 4;
  optional string classification = 5;
  optional .google.protobuf.Timestamp updated_at = 6;
  optional string name = 7;
  optional int32 user_id = 8;
  optional string classification_hint_text = 9;
  optional .chesscom.bots.v1.Personality personality = 15;
  optional bool v2 = 26;
  optional .chesscom.bots.v1.PhraseList 
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00706"></a>
## FND-00706: chesscom.bots.v1.BotPersonality.updated_at = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp updated_at = 6;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2605.

```text
 optional bool enabled = 3;
  optional string username = 4;
  optional string classification = 5;
  optional .google.protobuf.Timestamp updated_at = 6;
  optional string name = 7;
  optional int32 user_id = 8;
  optional string classification_hint_text = 9;
  optional .chesscom.bots.v1.Personality personality = 15;
  optional bool v2 = 26;
  optional .chesscom.bots.v1.PhraseList phrase_list = 32;
  repeated string su
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00707"></a>
## FND-00707: chesscom.bots.v1.BotPersonality.name = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 7;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2659.

```text
 = 4;
  optional string classification = 5;
  optional .google.protobuf.Timestamp updated_at = 6;
  optional string name = 7;
  optional int32 user_id = 8;
  optional string classification_hint_text = 9;
  optional .chesscom.bots.v1.Personality personality = 15;
  optional bool v2 = 26;
  optional .chesscom.bots.v1.PhraseList phrase_list = 32;
  repeated string supported_languages = 34;
}

message SupportedBot {
  op
```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00708"></a>
## FND-00708: chesscom.bots.v1.BotPersonality.user_id = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 user_id = 8;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2687.

```text
sification = 5;
  optional .google.protobuf.Timestamp updated_at = 6;
  optional string name = 7;
  optional int32 user_id = 8;
  optional string classification_hint_text = 9;
  optional .chesscom.bots.v1.Personality personality = 15;
  optional bool v2 = 26;
  optional .chesscom.bots.v1.PhraseList phrase_list = 32;
  repeated string supported_languages = 34;
}

message SupportedBot {
  optional string bot_name = 1;

```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00709"></a>
## FND-00709: chesscom.bots.v1.BotPersonality.classification_hint_text = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string classification_hint_text = 9;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2717.

```text
ogle.protobuf.Timestamp updated_at = 6;
  optional string name = 7;
  optional int32 user_id = 8;
  optional string classification_hint_text = 9;
  optional .chesscom.bots.v1.Personality personality = 15;
  optional bool v2 = 26;
  optional .chesscom.bots.v1.PhraseList phrase_list = 32;
  repeated string supported_languages = 34;
}

message SupportedBot {
  optional string bot_name = 1;
}

```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00710"></a>
## FND-00710: chesscom.bots.v1.BotPersonality.personality = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.bots.v1.Personality personality = 15;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2765.

```text
al string name = 7;
  optional int32 user_id = 8;
  optional string classification_hint_text = 9;
  optional .chesscom.bots.v1.Personality personality = 15;
  optional bool v2 = 26;
  optional .chesscom.bots.v1.PhraseList phrase_list = 32;
  repeated string supported_languages = 34;
}

message SupportedBot {
  optional string bot_name = 1;
}

```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00711"></a>
## FND-00711: chesscom.bots.v1.BotPersonality.v2 = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool v2 = 26;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2824.

```text
l string classification_hint_text = 9;
  optional .chesscom.bots.v1.Personality personality = 15;
  optional bool v2 = 26;
  optional .chesscom.bots.v1.PhraseList phrase_list = 32;
  repeated string supported_languages = 34;
}

message SupportedBot {
  optional string bot_name = 1;
}

```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00712"></a>
## FND-00712: chesscom.bots.v1.BotPersonality.phrase_list = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.bots.v1.PhraseList phrase_list = 32;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2849.

```text
int_text = 9;
  optional .chesscom.bots.v1.Personality personality = 15;
  optional bool v2 = 26;
  optional .chesscom.bots.v1.PhraseList phrase_list = 32;
  repeated string supported_languages = 34;
}

message SupportedBot {
  optional string bot_name = 1;
}

```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00713"></a>
## FND-00713: chesscom.bots.v1.BotPersonality.supported_languages = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string supported_languages = 34;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2907.

```text
sonality = 15;
  optional bool v2 = 26;
  optional .chesscom.bots.v1.PhraseList phrase_list = 32;
  repeated string supported_languages = 34;
}

message SupportedBot {
  optional string bot_name = 1;
}

```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00714"></a>
## FND-00714: message declaration: chesscom.bots.v1.SupportedBot

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SupportedBot {

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2952.

```text
ional .chesscom.bots.v1.PhraseList phrase_list = 32;
  repeated string supported_languages = 34;
}

message SupportedBot {
  optional string bot_name = 1;
}

```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00715"></a>
## FND-00715: chesscom.bots.v1.SupportedBot.bot_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string bot_name = 1;

### Evidence

- **SRC-0227** `research/proto/chesscom/bots/v1/bot_personality.proto` — [preserved redacted evidence](../evidence/text/877b56dc81d776d15f1f2f2cef31cdb47a9876383ccf37755a694803c2cbc1bb.proto)
  Character offset 2977.

```text
hraseList phrase_list = 32;
  repeated string supported_languages = 34;
}

message SupportedBot {
  optional string bot_name = 1;
}

```

**Source references:** SRC-0227, SRC-1198  
**URL references:** None independently associated  
**Related findings:** FND-00626, FND-00627, FND-00628

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00716"></a>
## FND-00716: message declaration: chesscom.bots.v1.PhraseList

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PhraseList {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 92.

```text
// source: chesscom/bots/v1/phrase_list.proto
// syntax: proto3

package chesscom.bots.v1;

message PhraseList {
  oneof _greeting {
  string greeting = 1;
  }
  oneof _won {
  string won = 2;
  }
  oneof _lost {
  string lost = 3;
  }
  oneof _draw {
  string draw = 4;
  }
  oneof _winning {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00717"></a>
## FND-00717: oneof declaration: chesscom.bots.v1.PhraseList._greeting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _greeting {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 115.

```text
scom/bots/v1/phrase_list.proto
// syntax: proto3

package chesscom.bots.v1;

message PhraseList {
  oneof _greeting {
  string greeting = 1;
  }
  oneof _won {
  string won = 2;
  }
  oneof _lost {
  string lost = 3;
  }
  oneof _draw {
  string draw = 4;
  }
  oneof _winning {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_ch
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00718"></a>
## FND-00718: chesscom.bots.v1.PhraseList.greeting = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string greeting = 1;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 135.

```text
list.proto
// syntax: proto3

package chesscom.bots.v1;

message PhraseList {
  oneof _greeting {
  string greeting = 1;
  }
  oneof _won {
  string won = 2;
  }
  oneof _lost {
  string lost = 3;
  }
  oneof _draw {
  string draw = 4;
  }
  oneof _winning {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string bei
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00719"></a>
## FND-00719: oneof declaration: chesscom.bots.v1.PhraseList._won

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _won {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 162.

```text
3

package chesscom.bots.v1;

message PhraseList {
  oneof _greeting {
  string greeting = 1;
  }
  oneof _won {
  string won = 2;
  }
  oneof _lost {
  string lost = 3;
  }
  oneof _draw {
  string draw = 4;
  }
  oneof _winning {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00720"></a>
## FND-00720: chesscom.bots.v1.PhraseList.won = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string won = 2;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 177.

```text
scom.bots.v1;

message PhraseList {
  oneof _greeting {
  string greeting = 1;
  }
  oneof _won {
  string won = 2;
  }
  oneof _lost {
  string lost = 3;
  }
  oneof _draw {
  string draw = 4;
  }
  oneof _winning {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_que
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00721"></a>
## FND-00721: oneof declaration: chesscom.bots.v1.PhraseList._lost

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _lost {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 199.

```text
 PhraseList {
  oneof _greeting {
  string greeting = 1;
  }
  oneof _won {
  string won = 2;
  }
  oneof _lost {
  string lost = 3;
  }
  oneof _draw {
  string draw = 4;
  }
  oneof _winning {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturin
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00722"></a>
## FND-00722: chesscom.bots.v1.PhraseList.lost = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string lost = 3;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 215.

```text
oneof _greeting {
  string greeting = 1;
  }
  oneof _won {
  string won = 2;
  }
  oneof _lost {
  string lost = 3;
  }
  oneof _draw {
  string draw = 4;
  }
  oneof _winning {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00723"></a>
## FND-00723: oneof declaration: chesscom.bots.v1.PhraseList._draw

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _draw {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 238.

```text
ing greeting = 1;
  }
  oneof _won {
  string won = 2;
  }
  oneof _lost {
  string lost = 3;
  }
  oneof _draw {
  string draw = 4;
  }
  oneof _winning {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
  oneof _queen_capture
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00724"></a>
## FND-00724: chesscom.bots.v1.PhraseList.draw = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string draw = 4;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 254.

```text
;
  }
  oneof _won {
  string won = 2;
  }
  oneof _lost {
  string lost = 3;
  }
  oneof _draw {
  string draw = 4;
  }
  oneof _winning {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
  oneof _queen_captured {
  string que
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00725"></a>
## FND-00725: oneof declaration: chesscom.bots.v1.PhraseList._winning

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _winning {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 277.

```text
string won = 2;
  }
  oneof _lost {
  string lost = 3;
  }
  oneof _draw {
  string draw = 4;
  }
  oneof _winning {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
  oneof _queen_captured {
  string queen_captured = 10;
  }
 
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00726"></a>
## FND-00726: chesscom.bots.v1.PhraseList.winning = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string winning = 5;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 296.

```text

  oneof _lost {
  string lost = 3;
  }
  oneof _draw {
  string draw = 4;
  }
  oneof _winning {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
  oneof _queen_captured {
  string queen_captured = 10;
  }
  oneof _promoting_p
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00727"></a>
## FND-00727: oneof declaration: chesscom.bots.v1.PhraseList._losing

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _losing {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 322.

```text
lost = 3;
  }
  oneof _draw {
  string draw = 4;
  }
  oneof _winning {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
  oneof _queen_captured {
  string queen_captured = 10;
  }
  oneof _promoting_pawn {
  string promoting_p
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00728"></a>
## FND-00728: chesscom.bots.v1.PhraseList.losing = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string losing = 6;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 340.

```text
eof _draw {
  string draw = 4;
  }
  oneof _winning {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
  oneof _queen_captured {
  string queen_captured = 10;
  }
  oneof _promoting_pawn {
  string promoting_pawn = 11;
  }
  on
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00729"></a>
## FND-00729: oneof declaration: chesscom.bots.v1.PhraseList._giving_check

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _giving_check {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 365.

```text
 = 4;
  }
  oneof _winning {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
  oneof _queen_captured {
  string queen_captured = 10;
  }
  oneof _promoting_pawn {
  string promoting_pawn = 11;
  }
  oneof _player_pawn_promote 
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00730"></a>
## FND-00730: chesscom.bots.v1.PhraseList.giving_check = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string giving_check = 7;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 389.

```text
ng {
  string winning = 5;
  }
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
  oneof _queen_captured {
  string queen_captured = 10;
  }
  oneof _promoting_pawn {
  string promoting_pawn = 11;
  }
  oneof _player_pawn_promote {
  string player_pawn_p
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00731"></a>
## FND-00731: oneof declaration: chesscom.bots.v1.PhraseList._being_checked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _being_checked {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 420.

```text
  oneof _losing {
  string losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
  oneof _queen_captured {
  string queen_captured = 10;
  }
  oneof _promoting_pawn {
  string promoting_pawn = 11;
  }
  oneof _player_pawn_promote {
  string player_pawn_promote = 12;
  }
  oneof _first
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00732"></a>
## FND-00732: chesscom.bots.v1.PhraseList.being_checked = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string being_checked = 8;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 445.

```text
g losing = 6;
  }
  oneof _giving_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
  oneof _queen_captured {
  string queen_captured = 10;
  }
  oneof _promoting_pawn {
  string promoting_pawn = 11;
  }
  oneof _player_pawn_promote {
  string player_pawn_promote = 12;
  }
  oneof _first_capture {
  string first
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00733"></a>
## FND-00733: oneof declaration: chesscom.bots.v1.PhraseList._capturing_queen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _capturing_queen {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 477.

```text
g_check {
  string giving_check = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
  oneof _queen_captured {
  string queen_captured = 10;
  }
  oneof _promoting_pawn {
  string promoting_pawn = 11;
  }
  oneof _player_pawn_promote {
  string player_pawn_promote = 12;
  }
  oneof _first_capture {
  string first_capture = 13;
  }
  oneof _thre
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00734"></a>
## FND-00734: chesscom.bots.v1.PhraseList.capturing_queen = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string capturing_queen = 9;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 504.

```text
heck = 7;
  }
  oneof _being_checked {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
  oneof _queen_captured {
  string queen_captured = 10;
  }
  oneof _promoting_pawn {
  string promoting_pawn = 11;
  }
  oneof _player_pawn_promote {
  string player_pawn_promote = 12;
  }
  oneof _first_capture {
  string first_capture = 13;
  }
  oneof _threatening {
  string threaten
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00735"></a>
## FND-00735: oneof declaration: chesscom.bots.v1.PhraseList._queen_captured

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _queen_captured {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 538.

```text
ed {
  string being_checked = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
  oneof _queen_captured {
  string queen_captured = 10;
  }
  oneof _promoting_pawn {
  string promoting_pawn = 11;
  }
  oneof _player_pawn_promote {
  string player_pawn_promote = 12;
  }
  oneof _first_capture {
  string first_capture = 13;
  }
  oneof _threatening {
  string threatening = 14;
  }
  oneof _threatened 
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00736"></a>
## FND-00736: chesscom.bots.v1.PhraseList.queen_captured = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string queen_captured = 10;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 564.

```text
d = 8;
  }
  oneof _capturing_queen {
  string capturing_queen = 9;
  }
  oneof _queen_captured {
  string queen_captured = 10;
  }
  oneof _promoting_pawn {
  string promoting_pawn = 11;
  }
  oneof _player_pawn_promote {
  string player_pawn_promote = 12;
  }
  oneof _first_capture {
  string first_capture = 13;
  }
  oneof _threatening {
  string threatening = 14;
  }
  oneof _threatened {
  string threatened = 15
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00737"></a>
## FND-00737: oneof declaration: chesscom.bots.v1.PhraseList._promoting_pawn

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _promoting_pawn {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 598.

```text
n {
  string capturing_queen = 9;
  }
  oneof _queen_captured {
  string queen_captured = 10;
  }
  oneof _promoting_pawn {
  string promoting_pawn = 11;
  }
  oneof _player_pawn_promote {
  string player_pawn_promote = 12;
  }
  oneof _first_capture {
  string first_capture = 13;
  }
  oneof _threatening {
  string threatening = 14;
  }
  oneof _threatened {
  string threatened = 15;
  }
  oneof _computer_has_mate_i
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00738"></a>
## FND-00738: chesscom.bots.v1.PhraseList.promoting_pawn = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string promoting_pawn = 11;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 624.

```text
en = 9;
  }
  oneof _queen_captured {
  string queen_captured = 10;
  }
  oneof _promoting_pawn {
  string promoting_pawn = 11;
  }
  oneof _player_pawn_promote {
  string player_pawn_promote = 12;
  }
  oneof _first_capture {
  string first_capture = 13;
  }
  oneof _threatening {
  string threatening = 14;
  }
  oneof _threatened {
  string threatened = 15;
  }
  oneof _computer_has_mate_in_x {
  string computer_ha
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00739"></a>
## FND-00739: oneof declaration: chesscom.bots.v1.PhraseList._player_pawn_promote

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _player_pawn_promote {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 658.

```text
d {
  string queen_captured = 10;
  }
  oneof _promoting_pawn {
  string promoting_pawn = 11;
  }
  oneof _player_pawn_promote {
  string player_pawn_promote = 12;
  }
  oneof _first_capture {
  string first_capture = 13;
  }
  oneof _threatening {
  string threatening = 14;
  }
  oneof _threatened {
  string threatened = 15;
  }
  oneof _computer_has_mate_in_x {
  string computer_has_mate_in_x = 16;
  }
  oneof _pla
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00740"></a>
## FND-00740: chesscom.bots.v1.PhraseList.player_pawn_promote = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string player_pawn_promote = 12;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 689.

```text
0;
  }
  oneof _promoting_pawn {
  string promoting_pawn = 11;
  }
  oneof _player_pawn_promote {
  string player_pawn_promote = 12;
  }
  oneof _first_capture {
  string first_capture = 13;
  }
  oneof _threatening {
  string threatening = 14;
  }
  oneof _threatened {
  string threatened = 15;
  }
  oneof _computer_has_mate_in_x {
  string computer_has_mate_in_x = 16;
  }
  oneof _player_has_mate_in_x {
  string pl
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00741"></a>
## FND-00741: oneof declaration: chesscom.bots.v1.PhraseList._first_capture

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _first_capture {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 728.

```text
ng promoting_pawn = 11;
  }
  oneof _player_pawn_promote {
  string player_pawn_promote = 12;
  }
  oneof _first_capture {
  string first_capture = 13;
  }
  oneof _threatening {
  string threatening = 14;
  }
  oneof _threatened {
  string threatened = 15;
  }
  oneof _computer_has_mate_in_x {
  string computer_has_mate_in_x = 16;
  }
  oneof _player_has_mate_in_x {
  string player_has_mate_in_x = 17;
  }
  oneof _r
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00742"></a>
## FND-00742: chesscom.bots.v1.PhraseList.first_capture = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string first_capture = 13;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 753.

```text
 }
  oneof _player_pawn_promote {
  string player_pawn_promote = 12;
  }
  oneof _first_capture {
  string first_capture = 13;
  }
  oneof _threatening {
  string threatening = 14;
  }
  oneof _threatened {
  string threatened = 15;
  }
  oneof _computer_has_mate_in_x {
  string computer_has_mate_in_x = 16;
  }
  oneof _player_has_mate_in_x {
  string player_has_mate_in_x = 17;
  }
  oneof _random {
  string random =
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00743"></a>
## FND-00743: oneof declaration: chesscom.bots.v1.PhraseList._threatening

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _threatening {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 786.

```text

  string player_pawn_promote = 12;
  }
  oneof _first_capture {
  string first_capture = 13;
  }
  oneof _threatening {
  string threatening = 14;
  }
  oneof _threatened {
  string threatened = 15;
  }
  oneof _computer_has_mate_in_x {
  string computer_has_mate_in_x = 16;
  }
  oneof _player_has_mate_in_x {
  string player_has_mate_in_x = 17;
  }
  oneof _random {
  string random = 18;
  }
  oneof _opening_e4 {
  
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00744"></a>
## FND-00744: chesscom.bots.v1.PhraseList.threatening = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string threatening = 14;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 809.

```text
romote = 12;
  }
  oneof _first_capture {
  string first_capture = 13;
  }
  oneof _threatening {
  string threatening = 14;
  }
  oneof _threatened {
  string threatened = 15;
  }
  oneof _computer_has_mate_in_x {
  string computer_has_mate_in_x = 16;
  }
  oneof _player_has_mate_in_x {
  string player_has_mate_in_x = 17;
  }
  oneof _random {
  string random = 18;
  }
  oneof _opening_e4 {
  string opening_e4 = 19;
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00745"></a>
## FND-00745: oneof declaration: chesscom.bots.v1.PhraseList._threatened

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _threatened {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 840.

```text
_capture {
  string first_capture = 13;
  }
  oneof _threatening {
  string threatening = 14;
  }
  oneof _threatened {
  string threatened = 15;
  }
  oneof _computer_has_mate_in_x {
  string computer_has_mate_in_x = 16;
  }
  oneof _player_has_mate_in_x {
  string player_has_mate_in_x = 17;
  }
  oneof _random {
  string random = 18;
  }
  oneof _opening_e4 {
  string opening_e4 = 19;
  }
  oneof _opening_d4 {
  st
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00746"></a>
## FND-00746: chesscom.bots.v1.PhraseList.threatened = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string threatened = 15;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 862.

```text
rst_capture = 13;
  }
  oneof _threatening {
  string threatening = 14;
  }
  oneof _threatened {
  string threatened = 15;
  }
  oneof _computer_has_mate_in_x {
  string computer_has_mate_in_x = 16;
  }
  oneof _player_has_mate_in_x {
  string player_has_mate_in_x = 17;
  }
  oneof _random {
  string random = 18;
  }
  oneof _opening_e4 {
  string opening_e4 = 19;
  }
  oneof _opening_d4 {
  string opening_d4 = 20;

```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00747"></a>
## FND-00747: oneof declaration: chesscom.bots.v1.PhraseList._computer_has_mate_in_x

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _computer_has_mate_in_x {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 892.

```text
_threatening {
  string threatening = 14;
  }
  oneof _threatened {
  string threatened = 15;
  }
  oneof _computer_has_mate_in_x {
  string computer_has_mate_in_x = 16;
  }
  oneof _player_has_mate_in_x {
  string player_has_mate_in_x = 17;
  }
  oneof _random {
  string random = 18;
  }
  oneof _opening_e4 {
  string opening_e4 = 19;
  }
  oneof _opening_d4 {
  string opening_d4 = 20;
  }
  oneof _opening_c4_englis
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00748"></a>
## FND-00748: chesscom.bots.v1.PhraseList.computer_has_mate_in_x = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string computer_has_mate_in_x = 16;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 926.

```text
g = 14;
  }
  oneof _threatened {
  string threatened = 15;
  }
  oneof _computer_has_mate_in_x {
  string computer_has_mate_in_x = 16;
  }
  oneof _player_has_mate_in_x {
  string player_has_mate_in_x = 17;
  }
  oneof _random {
  string random = 18;
  }
  oneof _opening_e4 {
  string opening_e4 = 19;
  }
  oneof _opening_d4 {
  string opening_d4 = 20;
  }
  oneof _opening_c4_english {
  string opening_c4_english = 
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00749"></a>
## FND-00749: oneof declaration: chesscom.bots.v1.PhraseList._player_has_mate_in_x

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _player_has_mate_in_x {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 968.

```text
 threatened = 15;
  }
  oneof _computer_has_mate_in_x {
  string computer_has_mate_in_x = 16;
  }
  oneof _player_has_mate_in_x {
  string player_has_mate_in_x = 17;
  }
  oneof _random {
  string random = 18;
  }
  oneof _opening_e4 {
  string opening_e4 = 19;
  }
  oneof _opening_d4 {
  string opening_d4 = 20;
  }
  oneof _opening_c4_english {
  string opening_c4_english = 21;
  }
  oneof _opening_nf3 {
  string op
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00750"></a>
## FND-00750: chesscom.bots.v1.PhraseList.player_has_mate_in_x = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string player_has_mate_in_x = 17;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1000.

```text
omputer_has_mate_in_x {
  string computer_has_mate_in_x = 16;
  }
  oneof _player_has_mate_in_x {
  string player_has_mate_in_x = 17;
  }
  oneof _random {
  string random = 18;
  }
  oneof _opening_e4 {
  string opening_e4 = 19;
  }
  oneof _opening_d4 {
  string opening_d4 = 20;
  }
  oneof _opening_c4_english {
  string opening_c4_english = 21;
  }
  oneof _opening_nf3 {
  string opening_nf3 = 22;
  }
  oneof _ope
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00751"></a>
## FND-00751: oneof declaration: chesscom.bots.v1.PhraseList._random

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _random {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1040.

```text
r_has_mate_in_x = 16;
  }
  oneof _player_has_mate_in_x {
  string player_has_mate_in_x = 17;
  }
  oneof _random {
  string random = 18;
  }
  oneof _opening_e4 {
  string opening_e4 = 19;
  }
  oneof _opening_d4 {
  string opening_d4 = 20;
  }
  oneof _opening_c4_english {
  string opening_c4_english = 21;
  }
  oneof _opening_nf3 {
  string opening_nf3 = 22;
  }
  oneof _opening_e4_e5_kings_pawn {
  string opening
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00752"></a>
## FND-00752: chesscom.bots.v1.PhraseList.random = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string random = 18;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1058.

```text
16;
  }
  oneof _player_has_mate_in_x {
  string player_has_mate_in_x = 17;
  }
  oneof _random {
  string random = 18;
  }
  oneof _opening_e4 {
  string opening_e4 = 19;
  }
  oneof _opening_d4 {
  string opening_d4 = 20;
  }
  oneof _opening_c4_english {
  string opening_c4_english = 21;
  }
  oneof _opening_nf3 {
  string opening_nf3 = 22;
  }
  oneof _opening_e4_e5_kings_pawn {
  string opening_e4_e5_kings_pawn 
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00753"></a>
## FND-00753: oneof declaration: chesscom.bots.v1.PhraseList._opening_e4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening_e4 {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1084.

```text
s_mate_in_x {
  string player_has_mate_in_x = 17;
  }
  oneof _random {
  string random = 18;
  }
  oneof _opening_e4 {
  string opening_e4 = 19;
  }
  oneof _opening_d4 {
  string opening_d4 = 20;
  }
  oneof _opening_c4_english {
  string opening_c4_english = 21;
  }
  oneof _opening_nf3 {
  string opening_nf3 = 22;
  }
  oneof _opening_e4_e5_kings_pawn {
  string opening_e4_e5_kings_pawn = 23;
  }
  oneof _opening
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00754"></a>
## FND-00754: chesscom.bots.v1.PhraseList.opening_e4 = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opening_e4 = 19;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1106.

```text
 player_has_mate_in_x = 17;
  }
  oneof _random {
  string random = 18;
  }
  oneof _opening_e4 {
  string opening_e4 = 19;
  }
  oneof _opening_d4 {
  string opening_d4 = 20;
  }
  oneof _opening_c4_english {
  string opening_c4_english = 21;
  }
  oneof _opening_nf3 {
  string opening_nf3 = 22;
  }
  oneof _opening_e4_e5_kings_pawn {
  string opening_e4_e5_kings_pawn = 23;
  }
  oneof _opening_e4_c5_sicilian {
  st
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00755"></a>
## FND-00755: oneof declaration: chesscom.bots.v1.PhraseList._opening_d4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening_d4 {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1136.

```text
}
  oneof _random {
  string random = 18;
  }
  oneof _opening_e4 {
  string opening_e4 = 19;
  }
  oneof _opening_d4 {
  string opening_d4 = 20;
  }
  oneof _opening_c4_english {
  string opening_c4_english = 21;
  }
  oneof _opening_nf3 {
  string opening_nf3 = 22;
  }
  oneof _opening_e4_e5_kings_pawn {
  string opening_e4_e5_kings_pawn = 23;
  }
  oneof _opening_e4_c5_sicilian {
  string opening_e4_c5_sicilian = 
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00756"></a>
## FND-00756: chesscom.bots.v1.PhraseList.opening_d4 = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opening_d4 = 20;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1158.

```text
string random = 18;
  }
  oneof _opening_e4 {
  string opening_e4 = 19;
  }
  oneof _opening_d4 {
  string opening_d4 = 20;
  }
  oneof _opening_c4_english {
  string opening_c4_english = 21;
  }
  oneof _opening_nf3 {
  string opening_nf3 = 22;
  }
  oneof _opening_e4_e5_kings_pawn {
  string opening_e4_e5_kings_pawn = 23;
  }
  oneof _opening_e4_c5_sicilian {
  string opening_e4_c5_sicilian = 24;
  }
  oneof _openi
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00757"></a>
## FND-00757: oneof declaration: chesscom.bots.v1.PhraseList._opening_c4_english

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening_c4_english {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1188.

```text
f _opening_e4 {
  string opening_e4 = 19;
  }
  oneof _opening_d4 {
  string opening_d4 = 20;
  }
  oneof _opening_c4_english {
  string opening_c4_english = 21;
  }
  oneof _opening_nf3 {
  string opening_nf3 = 22;
  }
  oneof _opening_e4_e5_kings_pawn {
  string opening_e4_e5_kings_pawn = 23;
  }
  oneof _opening_e4_c5_sicilian {
  string opening_e4_c5_sicilian = 24;
  }
  oneof _opening_e4_c6_carokann {
  string o
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00758"></a>
## FND-00758: chesscom.bots.v1.PhraseList.opening_c4_english = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opening_c4_english = 21;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1218.

```text
ng_e4 = 19;
  }
  oneof _opening_d4 {
  string opening_d4 = 20;
  }
  oneof _opening_c4_english {
  string opening_c4_english = 21;
  }
  oneof _opening_nf3 {
  string opening_nf3 = 22;
  }
  oneof _opening_e4_e5_kings_pawn {
  string opening_e4_e5_kings_pawn = 23;
  }
  oneof _opening_e4_c5_sicilian {
  string opening_e4_c5_sicilian = 24;
  }
  oneof _opening_e4_c6_carokann {
  string opening_e4_c6_carokann = 25;
  
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00759"></a>
## FND-00759: oneof declaration: chesscom.bots.v1.PhraseList._opening_nf3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening_nf3 {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1256.

```text
  string opening_d4 = 20;
  }
  oneof _opening_c4_english {
  string opening_c4_english = 21;
  }
  oneof _opening_nf3 {
  string opening_nf3 = 22;
  }
  oneof _opening_e4_e5_kings_pawn {
  string opening_e4_e5_kings_pawn = 23;
  }
  oneof _opening_e4_c5_sicilian {
  string opening_e4_c5_sicilian = 24;
  }
  oneof _opening_e4_c6_carokann {
  string opening_e4_c6_carokann = 25;
  }
  oneof _opening_e4_e6_french {
  st
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00760"></a>
## FND-00760: chesscom.bots.v1.PhraseList.opening_nf3 = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opening_nf3 = 22;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1279.

```text
0;
  }
  oneof _opening_c4_english {
  string opening_c4_english = 21;
  }
  oneof _opening_nf3 {
  string opening_nf3 = 22;
  }
  oneof _opening_e4_e5_kings_pawn {
  string opening_e4_e5_kings_pawn = 23;
  }
  oneof _opening_e4_c5_sicilian {
  string opening_e4_c5_sicilian = 24;
  }
  oneof _opening_e4_c6_carokann {
  string opening_e4_c6_carokann = 25;
  }
  oneof _opening_e4_e6_french {
  string opening_e4_e6_fren
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00761"></a>
## FND-00761: oneof declaration: chesscom.bots.v1.PhraseList._opening_e4_e5_kings_pawn

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening_e4_e5_kings_pawn {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1310.

```text
ish {
  string opening_c4_english = 21;
  }
  oneof _opening_nf3 {
  string opening_nf3 = 22;
  }
  oneof _opening_e4_e5_kings_pawn {
  string opening_e4_e5_kings_pawn = 23;
  }
  oneof _opening_e4_c5_sicilian {
  string opening_e4_c5_sicilian = 24;
  }
  oneof _opening_e4_c6_carokann {
  string opening_e4_c6_carokann = 25;
  }
  oneof _opening_e4_e6_french {
  string opening_e4_e6_french = 26;
  }
  oneof _opening_d
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00762"></a>
## FND-00762: chesscom.bots.v1.PhraseList.opening_e4_e5_kings_pawn = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opening_e4_e5_kings_pawn = 23;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1346.

```text
21;
  }
  oneof _opening_nf3 {
  string opening_nf3 = 22;
  }
  oneof _opening_e4_e5_kings_pawn {
  string opening_e4_e5_kings_pawn = 23;
  }
  oneof _opening_e4_c5_sicilian {
  string opening_e4_c5_sicilian = 24;
  }
  oneof _opening_e4_c6_carokann {
  string opening_e4_c6_carokann = 25;
  }
  oneof _opening_e4_e6_french {
  string opening_e4_e6_french = 26;
  }
  oneof _opening_d4_nf6_indian {
  string opening_d4_n
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00763"></a>
## FND-00763: oneof declaration: chesscom.bots.v1.PhraseList._opening_e4_c5_sicilian

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening_e4_c5_sicilian {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1390.

```text
ing_nf3 = 22;
  }
  oneof _opening_e4_e5_kings_pawn {
  string opening_e4_e5_kings_pawn = 23;
  }
  oneof _opening_e4_c5_sicilian {
  string opening_e4_c5_sicilian = 24;
  }
  oneof _opening_e4_c6_carokann {
  string opening_e4_c6_carokann = 25;
  }
  oneof _opening_e4_e6_french {
  string opening_e4_e6_french = 26;
  }
  oneof _opening_d4_nf6_indian {
  string opening_d4_nf6_indian = 27;
  }
  oneof _opening_d4_d5_q
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00764"></a>
## FND-00764: chesscom.bots.v1.PhraseList.opening_e4_c5_sicilian = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opening_e4_c5_sicilian = 24;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1424.

```text
_e4_e5_kings_pawn {
  string opening_e4_e5_kings_pawn = 23;
  }
  oneof _opening_e4_c5_sicilian {
  string opening_e4_c5_sicilian = 24;
  }
  oneof _opening_e4_c6_carokann {
  string opening_e4_c6_carokann = 25;
  }
  oneof _opening_e4_e6_french {
  string opening_e4_e6_french = 26;
  }
  oneof _opening_d4_nf6_indian {
  string opening_d4_nf6_indian = 27;
  }
  oneof _opening_d4_d5_queens_gambit {
  string opening_d4
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00765"></a>
## FND-00765: oneof declaration: chesscom.bots.v1.PhraseList._opening_e4_c6_carokann

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening_e4_c6_carokann {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1466.

```text
_kings_pawn = 23;
  }
  oneof _opening_e4_c5_sicilian {
  string opening_e4_c5_sicilian = 24;
  }
  oneof _opening_e4_c6_carokann {
  string opening_e4_c6_carokann = 25;
  }
  oneof _opening_e4_e6_french {
  string opening_e4_e6_french = 26;
  }
  oneof _opening_d4_nf6_indian {
  string opening_d4_nf6_indian = 27;
  }
  oneof _opening_d4_d5_queens_gambit {
  string opening_d4_d5_queens_gambit = 28;
  }
  oneof _openi
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00766"></a>
## FND-00766: chesscom.bots.v1.PhraseList.opening_e4_c6_carokann = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opening_e4_c6_carokann = 25;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1500.

```text
ning_e4_c5_sicilian {
  string opening_e4_c5_sicilian = 24;
  }
  oneof _opening_e4_c6_carokann {
  string opening_e4_c6_carokann = 25;
  }
  oneof _opening_e4_e6_french {
  string opening_e4_e6_french = 26;
  }
  oneof _opening_d4_nf6_indian {
  string opening_d4_nf6_indian = 27;
  }
  oneof _opening_d4_d5_queens_gambit {
  string opening_d4_d5_queens_gambit = 28;
  }
  oneof _opening_other {
  string opening_other 
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00767"></a>
## FND-00767: oneof declaration: chesscom.bots.v1.PhraseList._opening_e4_e6_french

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening_e4_e6_french {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1542.

```text
c5_sicilian = 24;
  }
  oneof _opening_e4_c6_carokann {
  string opening_e4_c6_carokann = 25;
  }
  oneof _opening_e4_e6_french {
  string opening_e4_e6_french = 26;
  }
  oneof _opening_d4_nf6_indian {
  string opening_d4_nf6_indian = 27;
  }
  oneof _opening_d4_d5_queens_gambit {
  string opening_d4_d5_queens_gambit = 28;
  }
  oneof _opening_other {
  string opening_other = 29;
  }
  oneof _user_spends_more_than_1
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00768"></a>
## FND-00768: chesscom.bots.v1.PhraseList.opening_e4_e6_french = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opening_e4_e6_french = 26;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1574.

```text
pening_e4_c6_carokann {
  string opening_e4_c6_carokann = 25;
  }
  oneof _opening_e4_e6_french {
  string opening_e4_e6_french = 26;
  }
  oneof _opening_d4_nf6_indian {
  string opening_d4_nf6_indian = 27;
  }
  oneof _opening_d4_d5_queens_gambit {
  string opening_d4_d5_queens_gambit = 28;
  }
  oneof _opening_other {
  string opening_other = 29;
  }
  oneof _user_spends_more_than_15_seconds_on_a_move {
  string u
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00769"></a>
## FND-00769: oneof declaration: chesscom.bots.v1.PhraseList._opening_d4_nf6_indian

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening_d4_nf6_indian {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1614.

```text
_e4_c6_carokann = 25;
  }
  oneof _opening_e4_e6_french {
  string opening_e4_e6_french = 26;
  }
  oneof _opening_d4_nf6_indian {
  string opening_d4_nf6_indian = 27;
  }
  oneof _opening_d4_d5_queens_gambit {
  string opening_d4_d5_queens_gambit = 28;
  }
  oneof _opening_other {
  string opening_other = 29;
  }
  oneof _user_spends_more_than_15_seconds_on_a_move {
  string user_spends_more_than_15_seconds_on_a_mov
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00770"></a>
## FND-00770: chesscom.bots.v1.PhraseList.opening_d4_nf6_indian = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opening_d4_nf6_indian = 27;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1647.

```text
 _opening_e4_e6_french {
  string opening_e4_e6_french = 26;
  }
  oneof _opening_d4_nf6_indian {
  string opening_d4_nf6_indian = 27;
  }
  oneof _opening_d4_d5_queens_gambit {
  string opening_d4_d5_queens_gambit = 28;
  }
  oneof _opening_other {
  string opening_other = 29;
  }
  oneof _user_spends_more_than_15_seconds_on_a_move {
  string user_spends_more_than_15_seconds_on_a_move = 30;
  }
  oneof _user_spends_
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00771"></a>
## FND-00771: oneof declaration: chesscom.bots.v1.PhraseList._opening_d4_d5_queens_gambit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening_d4_d5_queens_gambit {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1688.

```text
_e4_e6_french = 26;
  }
  oneof _opening_d4_nf6_indian {
  string opening_d4_nf6_indian = 27;
  }
  oneof _opening_d4_d5_queens_gambit {
  string opening_d4_d5_queens_gambit = 28;
  }
  oneof _opening_other {
  string opening_other = 29;
  }
  oneof _user_spends_more_than_15_seconds_on_a_move {
  string user_spends_more_than_15_seconds_on_a_move = 30;
  }
  oneof _user_spends_more_than_1_minute_on_a_move {
  string u
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00772"></a>
## FND-00772: chesscom.bots.v1.PhraseList.opening_d4_d5_queens_gambit = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opening_d4_d5_queens_gambit = 28;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1727.

```text
g_d4_nf6_indian {
  string opening_d4_nf6_indian = 27;
  }
  oneof _opening_d4_d5_queens_gambit {
  string opening_d4_d5_queens_gambit = 28;
  }
  oneof _opening_other {
  string opening_other = 29;
  }
  oneof _user_spends_more_than_15_seconds_on_a_move {
  string user_spends_more_than_15_seconds_on_a_move = 30;
  }
  oneof _user_spends_more_than_1_minute_on_a_move {
  string user_spends_more_than_1_minute_on_a_move
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00773"></a>
## FND-00773: oneof declaration: chesscom.bots.v1.PhraseList._opening_other

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening_other {

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1774.

```text
n = 27;
  }
  oneof _opening_d4_d5_queens_gambit {
  string opening_d4_d5_queens_gambit = 28;
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
  oneof _user_spends_more_than_3_min
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00774"></a>
## FND-00774: chesscom.bots.v1.PhraseList.opening_other = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opening_other = 29;

### Evidence

- **SRC-0228** `research/proto/chesscom/bots/v1/phrase_list.proto` — [preserved redacted evidence](../evidence/text/68f410c03d508998f64836d10428fdb2483a43c4df97fd44e986ba05d2613f63.proto)
  Character offset 1799.

```text
ing_d4_d5_queens_gambit {
  string opening_d4_d5_queens_gambit = 28;
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
  string u
```

**Source references:** SRC-0228, SRC-1199  
**URL references:** None independently associated  
**Related findings:** FND-00716, FND-00717, FND-00718

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
