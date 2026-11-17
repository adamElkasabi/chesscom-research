# data_models — findings 5901–6000

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-06175"></a>
## FND-06175: chesscom.oauth.v1.Scope.SCOPE_OPENID = 202

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_OPENID = 202;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 231.

```text
PE_PUBLIC = 1;
  SCOPE_NONE = 2;
  SCOPE_CHESS = 100;
  SCOPE_ADDRESS = 200;
  SCOPE_EMAIL = 201;
  SCOPE_OPENID = 202;
  SCOPE_PROFILE = 203;
  SCOPE_EBOARD = 204;
  SCOPE_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES_MANAGE = 304;
  SCOPE_COMPUTER_GAMES_PLAY = 305;
  SCOPE_CONTACT
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06176"></a>
## FND-06176: chesscom.oauth.v1.Scope.SCOPE_PROFILE = 203

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_PROFILE = 203;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 253.

```text
_NONE = 2;
  SCOPE_CHESS = 100;
  SCOPE_ADDRESS = 200;
  SCOPE_EMAIL = 201;
  SCOPE_OPENID = 202;
  SCOPE_PROFILE = 203;
  SCOPE_EBOARD = 204;
  SCOPE_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES_MANAGE = 304;
  SCOPE_COMPUTER_GAMES_PLAY = 305;
  SCOPE_CONTACTS_READ = 306;
  SCOPE_
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06177"></a>
## FND-06177: chesscom.oauth.v1.Scope.SCOPE_EBOARD = 204

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_EBOARD = 204;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 276.

```text
S = 100;
  SCOPE_ADDRESS = 200;
  SCOPE_EMAIL = 201;
  SCOPE_OPENID = 202;
  SCOPE_PROFILE = 203;
  SCOPE_EBOARD = 204;
  SCOPE_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES_MANAGE = 304;
  SCOPE_COMPUTER_GAMES_PLAY = 305;
  SCOPE_CONTACTS_READ = 306;
  SCOPE_CONTACTS_WRITE = 307;
 
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06178"></a>
## FND-06178: chesscom.oauth.v1.Scope.SCOPE_NOADS = 205

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_NOADS = 205;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 298.

```text
SS = 200;
  SCOPE_EMAIL = 201;
  SCOPE_OPENID = 202;
  SCOPE_PROFILE = 203;
  SCOPE_EBOARD = 204;
  SCOPE_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES_MANAGE = 304;
  SCOPE_COMPUTER_GAMES_PLAY = 305;
  SCOPE_CONTACTS_READ = 306;
  SCOPE_CONTACTS_WRITE = 307;
  SCOPE_ENDGAMES = 308;
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06179"></a>
## FND-06179: chesscom.oauth.v1.Scope.SCOPE_PROLONGED_TOKEN = 206

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_PROLONGED_TOKEN = 206;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 319.

```text
IL = 201;
  SCOPE_OPENID = 202;
  SCOPE_PROFILE = 203;
  SCOPE_EBOARD = 204;
  SCOPE_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES_MANAGE = 304;
  SCOPE_COMPUTER_GAMES_PLAY = 305;
  SCOPE_CONTACTS_READ = 306;
  SCOPE_CONTACTS_WRITE = 307;
  SCOPE_ENDGAMES = 308;
  SCOPE_EXPLORER = 3
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06180"></a>
## FND-06180: chesscom.oauth.v1.Scope.SCOPE_ANALYSIS = 300

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_ANALYSIS = 300;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 350.

```text

  SCOPE_PROFILE = 203;
  SCOPE_EBOARD = 204;
  SCOPE_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES_MANAGE = 304;
  SCOPE_COMPUTER_GAMES_PLAY = 305;
  SCOPE_CONTACTS_READ = 306;
  SCOPE_CONTACTS_WRITE = 307;
  SCOPE_ENDGAMES = 308;
  SCOPE_EXPLORER = 347;
  SCOPE_FAIRPLAY_READ = 349
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06181"></a>
## FND-06181: chesscom.oauth.v1.Scope.SCOPE_ARTICLES_READ = 301

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_ARTICLES_READ = 301;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 374.

```text
  SCOPE_EBOARD = 204;
  SCOPE_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES_MANAGE = 304;
  SCOPE_COMPUTER_GAMES_PLAY = 305;
  SCOPE_CONTACTS_READ = 306;
  SCOPE_CONTACTS_WRITE = 307;
  SCOPE_ENDGAMES = 308;
  SCOPE_EXPLORER = 347;
  SCOPE_FAIRPLAY_READ = 349;
  SCOPE_FAIRPLAY_WRITE
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06182"></a>
## FND-06182: chesscom.oauth.v1.Scope.SCOPE_ATTRIBUTION_WRITE = 302

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_ATTRIBUTION_WRITE = 302;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 403.

```text
_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES_MANAGE = 304;
  SCOPE_COMPUTER_GAMES_PLAY = 305;
  SCOPE_CONTACTS_READ = 306;
  SCOPE_CONTACTS_WRITE = 307;
  SCOPE_ENDGAMES = 308;
  SCOPE_EXPLORER = 347;
  SCOPE_FAIRPLAY_READ = 349;
  SCOPE_FAIRPLAY_WRITE = 350;
  SCOPE_FCM = 309;
  
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06183"></a>
## FND-06183: chesscom.oauth.v1.Scope.SCOPE_COMMENTS_WRITE = 303

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_COMMENTS_WRITE = 303;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 436.

```text
OKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES_MANAGE = 304;
  SCOPE_COMPUTER_GAMES_PLAY = 305;
  SCOPE_CONTACTS_READ = 306;
  SCOPE_CONTACTS_WRITE = 307;
  SCOPE_ENDGAMES = 308;
  SCOPE_EXPLORER = 347;
  SCOPE_FAIRPLAY_READ = 349;
  SCOPE_FAIRPLAY_WRITE = 350;
  SCOPE_FCM = 309;
  SCOPE_FORUMS_WRITE = 310;
  SCOPE
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06184"></a>
## FND-06184: chesscom.oauth.v1.Scope.SCOPE_COMPUTER_GAMES_MANAGE = 304

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_COMPUTER_GAMES_MANAGE = 304;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 466.

```text
 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES_MANAGE = 304;
  SCOPE_COMPUTER_GAMES_PLAY = 305;
  SCOPE_CONTACTS_READ = 306;
  SCOPE_CONTACTS_WRITE = 307;
  SCOPE_ENDGAMES = 308;
  SCOPE_EXPLORER = 347;
  SCOPE_FAIRPLAY_READ = 349;
  SCOPE_FAIRPLAY_WRITE = 350;
  SCOPE_FCM = 309;
  SCOPE_FORUMS_WRITE = 310;
  SCOPE_FRIENDS_READ = 311;
  SCOPE_F
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06185"></a>
## FND-06185: chesscom.oauth.v1.Scope.SCOPE_COMPUTER_GAMES_PLAY = 305

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_COMPUTER_GAMES_PLAY = 305;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 503.

```text
SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES_MANAGE = 304;
  SCOPE_COMPUTER_GAMES_PLAY = 305;
  SCOPE_CONTACTS_READ = 306;
  SCOPE_CONTACTS_WRITE = 307;
  SCOPE_ENDGAMES = 308;
  SCOPE_EXPLORER = 347;
  SCOPE_FAIRPLAY_READ = 349;
  SCOPE_FAIRPLAY_WRITE = 350;
  SCOPE_FCM = 309;
  SCOPE_FORUMS_WRITE = 310;
  SCOPE_FRIENDS_READ = 311;
  SCOPE_FRIENDS_WRITE = 312;
  SCOPE_GAMES = 6
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06186"></a>
## FND-06186: chesscom.oauth.v1.Scope.SCOPE_CONTACTS_READ = 306

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_CONTACTS_READ = 306;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 538.

```text
OPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES_MANAGE = 304;
  SCOPE_COMPUTER_GAMES_PLAY = 305;
  SCOPE_CONTACTS_READ = 306;
  SCOPE_CONTACTS_WRITE = 307;
  SCOPE_ENDGAMES = 308;
  SCOPE_EXPLORER = 347;
  SCOPE_FAIRPLAY_READ = 349;
  SCOPE_FAIRPLAY_WRITE = 350;
  SCOPE_FCM = 309;
  SCOPE_FORUMS_WRITE = 310;
  SCOPE_FRIENDS_READ = 311;
  SCOPE_FRIENDS_WRITE = 312;
  SCOPE_GAMES = 600;
  SCOPE_GAMES_SEEKS_READ = 313;
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06187"></a>
## FND-06187: chesscom.oauth.v1.Scope.SCOPE_CONTACTS_WRITE = 307

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_CONTACTS_WRITE = 307;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 567.

```text
COPE_COMPUTER_GAMES_MANAGE = 304;
  SCOPE_COMPUTER_GAMES_PLAY = 305;
  SCOPE_CONTACTS_READ = 306;
  SCOPE_CONTACTS_WRITE = 307;
  SCOPE_ENDGAMES = 308;
  SCOPE_EXPLORER = 347;
  SCOPE_FAIRPLAY_READ = 349;
  SCOPE_FAIRPLAY_WRITE = 350;
  SCOPE_FCM = 309;
  SCOPE_FORUMS_WRITE = 310;
  SCOPE_FRIENDS_READ = 311;
  SCOPE_FRIENDS_WRITE = 312;
  SCOPE_GAMES = 600;
  SCOPE_GAMES_SEEKS_READ = 313;
  SCOPE_GAMES_SEEKS_WRITE = 
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06188"></a>
## FND-06188: chesscom.oauth.v1.Scope.SCOPE_ENDGAMES = 308

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_ENDGAMES = 308;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 597.

```text
04;
  SCOPE_COMPUTER_GAMES_PLAY = 305;
  SCOPE_CONTACTS_READ = 306;
  SCOPE_CONTACTS_WRITE = 307;
  SCOPE_ENDGAMES = 308;
  SCOPE_EXPLORER = 347;
  SCOPE_FAIRPLAY_READ = 349;
  SCOPE_FAIRPLAY_WRITE = 350;
  SCOPE_FCM = 309;
  SCOPE_FORUMS_WRITE = 310;
  SCOPE_FRIENDS_READ = 311;
  SCOPE_FRIENDS_WRITE = 312;
  SCOPE_GAMES = 600;
  SCOPE_GAMES_SEEKS_READ = 313;
  SCOPE_GAMES_SEEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 31
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06189"></a>
## FND-06189: chesscom.oauth.v1.Scope.SCOPE_EXPLORER = 347

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_EXPLORER = 347;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 621.

```text
ES_PLAY = 305;
  SCOPE_CONTACTS_READ = 306;
  SCOPE_CONTACTS_WRITE = 307;
  SCOPE_ENDGAMES = 308;
  SCOPE_EXPLORER = 347;
  SCOPE_FAIRPLAY_READ = 349;
  SCOPE_FAIRPLAY_WRITE = 350;
  SCOPE_FCM = 309;
  SCOPE_FORUMS_WRITE = 310;
  SCOPE_FRIENDS_READ = 311;
  SCOPE_FRIENDS_WRITE = 312;
  SCOPE_GAMES = 600;
  SCOPE_GAMES_SEEKS_READ = 313;
  SCOPE_GAMES_SEEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06190"></a>
## FND-06190: chesscom.oauth.v1.Scope.SCOPE_FAIRPLAY_READ = 349

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_FAIRPLAY_READ = 349;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 645.

```text
ONTACTS_READ = 306;
  SCOPE_CONTACTS_WRITE = 307;
  SCOPE_ENDGAMES = 308;
  SCOPE_EXPLORER = 347;
  SCOPE_FAIRPLAY_READ = 349;
  SCOPE_FAIRPLAY_WRITE = 350;
  SCOPE_FCM = 309;
  SCOPE_FORUMS_WRITE = 310;
  SCOPE_FRIENDS_READ = 311;
  SCOPE_FRIENDS_WRITE = 312;
  SCOPE_GAMES = 600;
  SCOPE_GAMES_SEEKS_READ = 313;
  SCOPE_GAMES_SEEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ 
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06191"></a>
## FND-06191: chesscom.oauth.v1.Scope.SCOPE_FAIRPLAY_WRITE = 350

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_FAIRPLAY_WRITE = 350;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 674.

```text
ONTACTS_WRITE = 307;
  SCOPE_ENDGAMES = 308;
  SCOPE_EXPLORER = 347;
  SCOPE_FAIRPLAY_READ = 349;
  SCOPE_FAIRPLAY_WRITE = 350;
  SCOPE_FCM = 309;
  SCOPE_FORUMS_WRITE = 310;
  SCOPE_FRIENDS_READ = 311;
  SCOPE_FRIENDS_WRITE = 312;
  SCOPE_GAMES = 600;
  SCOPE_GAMES_SEEKS_READ = 313;
  SCOPE_GAMES_SEEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06192"></a>
## FND-06192: chesscom.oauth.v1.Scope.SCOPE_FCM = 309

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_FCM = 309;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 704.

```text
NDGAMES = 308;
  SCOPE_EXPLORER = 347;
  SCOPE_FAIRPLAY_READ = 349;
  SCOPE_FAIRPLAY_WRITE = 350;
  SCOPE_FCM = 309;
  SCOPE_FORUMS_WRITE = 310;
  SCOPE_FRIENDS_READ = 311;
  SCOPE_FRIENDS_WRITE = 312;
  SCOPE_GAMES = 600;
  SCOPE_GAMES_SEEKS_READ = 313;
  SCOPE_GAMES_SEEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOP
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06193"></a>
## FND-06193: chesscom.oauth.v1.Scope.SCOPE_FORUMS_WRITE = 310

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_FORUMS_WRITE = 310;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 723.

```text
OPE_EXPLORER = 347;
  SCOPE_FAIRPLAY_READ = 349;
  SCOPE_FAIRPLAY_WRITE = 350;
  SCOPE_FCM = 309;
  SCOPE_FORUMS_WRITE = 310;
  SCOPE_FRIENDS_READ = 311;
  SCOPE_FRIENDS_WRITE = 312;
  SCOPE_GAMES = 600;
  SCOPE_GAMES_SEEKS_READ = 313;
  SCOPE_GAMES_SEEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOPE_MARKETING = 320;

```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06194"></a>
## FND-06194: chesscom.oauth.v1.Scope.SCOPE_FRIENDS_READ = 311

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_FRIENDS_READ = 311;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 751.

```text
FAIRPLAY_READ = 349;
  SCOPE_FAIRPLAY_WRITE = 350;
  SCOPE_FCM = 309;
  SCOPE_FORUMS_WRITE = 310;
  SCOPE_FRIENDS_READ = 311;
  SCOPE_FRIENDS_WRITE = 312;
  SCOPE_GAMES = 600;
  SCOPE_GAMES_SEEKS_READ = 313;
  SCOPE_GAMES_SEEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOPE_MARKETING = 320;
  SCOPE_MEMBERSHIP = 321;
  
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06195"></a>
## FND-06195: chesscom.oauth.v1.Scope.SCOPE_FRIENDS_WRITE = 312

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_FRIENDS_WRITE = 312;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 779.

```text
_FAIRPLAY_WRITE = 350;
  SCOPE_FCM = 309;
  SCOPE_FORUMS_WRITE = 310;
  SCOPE_FRIENDS_READ = 311;
  SCOPE_FRIENDS_WRITE = 312;
  SCOPE_GAMES = 600;
  SCOPE_GAMES_SEEKS_READ = 313;
  SCOPE_GAMES_SEEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOPE_MARKETING = 320;
  SCOPE_MEMBERSHIP = 321;
  SCOPE_MESSAGES_READ = 322;
 
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06196"></a>
## FND-06196: chesscom.oauth.v1.Scope.SCOPE_GAMES = 600

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_GAMES = 600;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 808.

```text
E_FCM = 309;
  SCOPE_FORUMS_WRITE = 310;
  SCOPE_FRIENDS_READ = 311;
  SCOPE_FRIENDS_WRITE = 312;
  SCOPE_GAMES = 600;
  SCOPE_GAMES_SEEKS_READ = 313;
  SCOPE_GAMES_SEEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOPE_MARKETING = 320;
  SCOPE_MEMBERSHIP = 321;
  SCOPE_MESSAGES_READ = 322;
  SCOPE_MESSAGES_WRITE = 323;

```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06197"></a>
## FND-06197: chesscom.oauth.v1.Scope.SCOPE_GAMES_SEEKS_READ = 313

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_GAMES_SEEKS_READ = 313;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 829.

```text
FORUMS_WRITE = 310;
  SCOPE_FRIENDS_READ = 311;
  SCOPE_FRIENDS_WRITE = 312;
  SCOPE_GAMES = 600;
  SCOPE_GAMES_SEEKS_READ = 313;
  SCOPE_GAMES_SEEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOPE_MARKETING = 320;
  SCOPE_MEMBERSHIP = 321;
  SCOPE_MESSAGES_READ = 322;
  SCOPE_MESSAGES_WRITE = 323;
  SCOPE_NOTIFICATIONS
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06198"></a>
## FND-06198: chesscom.oauth.v1.Scope.SCOPE_GAMES_SEEKS_WRITE = 314

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_GAMES_SEEKS_WRITE = 314;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 861.

```text
NDS_READ = 311;
  SCOPE_FRIENDS_WRITE = 312;
  SCOPE_GAMES = 600;
  SCOPE_GAMES_SEEKS_READ = 313;
  SCOPE_GAMES_SEEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOPE_MARKETING = 320;
  SCOPE_MEMBERSHIP = 321;
  SCOPE_MESSAGES_READ = 322;
  SCOPE_MESSAGES_WRITE = 323;
  SCOPE_NOTIFICATIONS = 324;
  SCOPE_ORDERS_READ = 32
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06199"></a>
## FND-06199: chesscom.oauth.v1.Scope.SCOPE_GAMES_MANAGE = 315

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_GAMES_MANAGE = 315;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 894.

```text
RITE = 312;
  SCOPE_GAMES = 600;
  SCOPE_GAMES_SEEKS_READ = 313;
  SCOPE_GAMES_SEEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOPE_MARKETING = 320;
  SCOPE_MEMBERSHIP = 321;
  SCOPE_MESSAGES_READ = 322;
  SCOPE_MESSAGES_WRITE = 323;
  SCOPE_NOTIFICATIONS = 324;
  SCOPE_ORDERS_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 35
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06200"></a>
## FND-06200: chesscom.oauth.v1.Scope.SCOPE_GAMES_PLAY = 316

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_GAMES_PLAY = 316;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 922.

```text
600;
  SCOPE_GAMES_SEEKS_READ = 313;
  SCOPE_GAMES_SEEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOPE_MARKETING = 320;
  SCOPE_MEMBERSHIP = 321;
  SCOPE_MESSAGES_READ = 322;
  SCOPE_MESSAGES_WRITE = 323;
  SCOPE_NOTIFICATIONS = 324;
  SCOPE_ORDERS_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06201"></a>
## FND-06201: chesscom.oauth.v1.Scope.SCOPE_GAMES_READ = 317

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_GAMES_READ = 317;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 948.

```text
EAD = 313;
  SCOPE_GAMES_SEEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOPE_MARKETING = 320;
  SCOPE_MEMBERSHIP = 321;
  SCOPE_MESSAGES_READ = 322;
  SCOPE_MESSAGES_WRITE = 323;
  SCOPE_NOTIFICATIONS = 324;
  SCOPE_ORDERS_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326;
  SCOPE_PRACTICE = 327;

```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06202"></a>
## FND-06202: chesscom.oauth.v1.Scope.SCOPE_LEAGUES = 318

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_LEAGUES = 318;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 974.

```text
EEKS_WRITE = 314;
  SCOPE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOPE_MARKETING = 320;
  SCOPE_MEMBERSHIP = 321;
  SCOPE_MESSAGES_READ = 322;
  SCOPE_MESSAGES_WRITE = 323;
  SCOPE_NOTIFICATIONS = 324;
  SCOPE_ORDERS_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326;
  SCOPE_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 3
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06203"></a>
## FND-06203: chesscom.oauth.v1.Scope.SCOPE_LESSONS = 319

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_LESSONS = 319;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 997.

```text
PE_GAMES_MANAGE = 315;
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOPE_MARKETING = 320;
  SCOPE_MEMBERSHIP = 321;
  SCOPE_MESSAGES_READ = 322;
  SCOPE_MESSAGES_WRITE = 323;
  SCOPE_NOTIFICATIONS = 324;
  SCOPE_ORDERS_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326;
  SCOPE_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 328;
  SCOPE_PUZZLES_REA
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06204"></a>
## FND-06204: chesscom.oauth.v1.Scope.SCOPE_MARKETING = 320

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_MARKETING = 320;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1020.

```text
  SCOPE_GAMES_PLAY = 316;
  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOPE_MARKETING = 320;
  SCOPE_MEMBERSHIP = 321;
  SCOPE_MESSAGES_READ = 322;
  SCOPE_MESSAGES_WRITE = 323;
  SCOPE_NOTIFICATIONS = 324;
  SCOPE_ORDERS_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326;
  SCOPE_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 328;
  SCOPE_PUZZLES_READ = 329;
  SCOPE_SESSIO
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06205"></a>
## FND-06205: chesscom.oauth.v1.Scope.SCOPE_MEMBERSHIP = 321

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_MEMBERSHIP = 321;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1045.

```text

  SCOPE_GAMES_READ = 317;
  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOPE_MARKETING = 320;
  SCOPE_MEMBERSHIP = 321;
  SCOPE_MESSAGES_READ = 322;
  SCOPE_MESSAGES_WRITE = 323;
  SCOPE_NOTIFICATIONS = 324;
  SCOPE_ORDERS_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326;
  SCOPE_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 328;
  SCOPE_PUZZLES_READ = 329;
  SCOPE_SESSION = 330;
  SCOPE_GATEWAY_
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06206"></a>
## FND-06206: chesscom.oauth.v1.Scope.SCOPE_MESSAGES_READ = 322

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_MESSAGES_READ = 322;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1071.

```text

  SCOPE_LEAGUES = 318;
  SCOPE_LESSONS = 319;
  SCOPE_MARKETING = 320;
  SCOPE_MEMBERSHIP = 321;
  SCOPE_MESSAGES_READ = 322;
  SCOPE_MESSAGES_WRITE = 323;
  SCOPE_NOTIFICATIONS = 324;
  SCOPE_ORDERS_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326;
  SCOPE_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 328;
  SCOPE_PUZZLES_READ = 329;
  SCOPE_SESSION = 330;
  SCOPE_GATEWAY_THEMES = 900;
  SCOPE_STAT
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06207"></a>
## FND-06207: chesscom.oauth.v1.Scope.SCOPE_MESSAGES_WRITE = 323

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_MESSAGES_WRITE = 323;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1100.

```text
PE_LESSONS = 319;
  SCOPE_MARKETING = 320;
  SCOPE_MEMBERSHIP = 321;
  SCOPE_MESSAGES_READ = 322;
  SCOPE_MESSAGES_WRITE = 323;
  SCOPE_NOTIFICATIONS = 324;
  SCOPE_ORDERS_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326;
  SCOPE_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 328;
  SCOPE_PUZZLES_READ = 329;
  SCOPE_SESSION = 330;
  SCOPE_GATEWAY_THEMES = 900;
  SCOPE_STATS_READ = 331;
  SCOPE_STREAKS
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06208"></a>
## FND-06208: chesscom.oauth.v1.Scope.SCOPE_NOTIFICATIONS = 324

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_NOTIFICATIONS = 324;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1130.

```text
ETING = 320;
  SCOPE_MEMBERSHIP = 321;
  SCOPE_MESSAGES_READ = 322;
  SCOPE_MESSAGES_WRITE = 323;
  SCOPE_NOTIFICATIONS = 324;
  SCOPE_ORDERS_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326;
  SCOPE_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 328;
  SCOPE_PUZZLES_READ = 329;
  SCOPE_SESSION = 330;
  SCOPE_GATEWAY_THEMES = 900;
  SCOPE_STATS_READ = 331;
  SCOPE_STREAKS_ADMIN_READ = 348;
  SCOPE_SUP
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06209"></a>
## FND-06209: chesscom.oauth.v1.Scope.SCOPE_ORDERS_READ = 325

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_ORDERS_READ = 325;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1159.

```text
IP = 321;
  SCOPE_MESSAGES_READ = 322;
  SCOPE_MESSAGES_WRITE = 323;
  SCOPE_NOTIFICATIONS = 324;
  SCOPE_ORDERS_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326;
  SCOPE_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 328;
  SCOPE_PUZZLES_READ = 329;
  SCOPE_SESSION = 330;
  SCOPE_GATEWAY_THEMES = 900;
  SCOPE_STATS_READ = 331;
  SCOPE_STREAKS_ADMIN_READ = 348;
  SCOPE_SUPPORT = 10000;
  SCOPE_SUPPORT
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06210"></a>
## FND-06210: chesscom.oauth.v1.Scope.SCOPE_PAGE_CONTEXT_READ = 351

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_PAGE_CONTEXT_READ = 351;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1186.

```text
READ = 322;
  SCOPE_MESSAGES_WRITE = 323;
  SCOPE_NOTIFICATIONS = 324;
  SCOPE_ORDERS_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326;
  SCOPE_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 328;
  SCOPE_PUZZLES_READ = 329;
  SCOPE_SESSION = 330;
  SCOPE_GATEWAY_THEMES = 900;
  SCOPE_STATS_READ = 331;
  SCOPE_STREAKS_ADMIN_READ = 348;
  SCOPE_SUPPORT = 10000;
  SCOPE_SUPPORT_INTERCOM = 10010;
  SCOPE_
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06211"></a>
## FND-06211: chesscom.oauth.v1.Scope.SCOPE_PEACEKEEPER = 326

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_PEACEKEEPER = 326;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1219.

```text
E = 323;
  SCOPE_NOTIFICATIONS = 324;
  SCOPE_ORDERS_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326;
  SCOPE_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 328;
  SCOPE_PUZZLES_READ = 329;
  SCOPE_SESSION = 330;
  SCOPE_GATEWAY_THEMES = 900;
  SCOPE_STATS_READ = 331;
  SCOPE_STREAKS_ADMIN_READ = 348;
  SCOPE_SUPPORT = 10000;
  SCOPE_SUPPORT_INTERCOM = 10010;
  SCOPE_THEMES = 332;
  SCOPE_USERS_ACKNO
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06212"></a>
## FND-06212: chesscom.oauth.v1.Scope.SCOPE_PRACTICE = 327

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_PRACTICE = 327;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1246.

```text
ONS = 324;
  SCOPE_ORDERS_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326;
  SCOPE_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 328;
  SCOPE_PUZZLES_READ = 329;
  SCOPE_SESSION = 330;
  SCOPE_GATEWAY_THEMES = 900;
  SCOPE_STATS_READ = 331;
  SCOPE_STREAKS_ADMIN_READ = 348;
  SCOPE_SUPPORT = 10000;
  SCOPE_SUPPORT_INTERCOM = 10010;
  SCOPE_THEMES = 332;
  SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333;
 
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06213"></a>
## FND-06213: chesscom.oauth.v1.Scope.SCOPE_PUZZLES_MANAGE = 328

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_PUZZLES_MANAGE = 328;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1270.

```text
S_READ = 325;
  SCOPE_PAGE_CONTEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326;
  SCOPE_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 328;
  SCOPE_PUZZLES_READ = 329;
  SCOPE_SESSION = 330;
  SCOPE_GATEWAY_THEMES = 900;
  SCOPE_STATS_READ = 331;
  SCOPE_STREAKS_ADMIN_READ = 348;
  SCOPE_SUPPORT = 10000;
  SCOPE_SUPPORT_INTERCOM = 10010;
  SCOPE_THEMES = 332;
  SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333;
  SCOPE_USERS_AGE_ASSURAN
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06214"></a>
## FND-06214: chesscom.oauth.v1.Scope.SCOPE_PUZZLES_READ = 329

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_PUZZLES_READ = 329;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1300.

```text
TEXT_READ = 351;
  SCOPE_PEACEKEEPER = 326;
  SCOPE_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 328;
  SCOPE_PUZZLES_READ = 329;
  SCOPE_SESSION = 330;
  SCOPE_GATEWAY_THEMES = 900;
  SCOPE_STATS_READ = 331;
  SCOPE_STREAKS_ADMIN_READ = 348;
  SCOPE_SUPPORT = 10000;
  SCOPE_SUPPORT_INTERCOM = 10010;
  SCOPE_THEMES = 332;
  SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333;
  SCOPE_USERS_AGE_ASSURANCE_MANAGE = 346;
  SCOPE_USERS
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06215"></a>
## FND-06215: chesscom.oauth.v1.Scope.SCOPE_SESSION = 330

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_SESSION = 330;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1328.

```text
CEKEEPER = 326;
  SCOPE_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 328;
  SCOPE_PUZZLES_READ = 329;
  SCOPE_SESSION = 330;
  SCOPE_GATEWAY_THEMES = 900;
  SCOPE_STATS_READ = 331;
  SCOPE_STREAKS_ADMIN_READ = 348;
  SCOPE_SUPPORT = 10000;
  SCOPE_SUPPORT_INTERCOM = 10010;
  SCOPE_THEMES = 332;
  SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333;
  SCOPE_USERS_AGE_ASSURANCE_MANAGE = 346;
  SCOPE_USERS_CONSENT_MANAGE = 334;
  SCO
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06216"></a>
## FND-06216: chesscom.oauth.v1.Scope.SCOPE_GATEWAY_THEMES = 900

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_GATEWAY_THEMES = 900;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1351.

```text
_PRACTICE = 327;
  SCOPE_PUZZLES_MANAGE = 328;
  SCOPE_PUZZLES_READ = 329;
  SCOPE_SESSION = 330;
  SCOPE_GATEWAY_THEMES = 900;
  SCOPE_STATS_READ = 331;
  SCOPE_STREAKS_ADMIN_READ = 348;
  SCOPE_SUPPORT = 10000;
  SCOPE_SUPPORT_INTERCOM = 10010;
  SCOPE_THEMES = 332;
  SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333;
  SCOPE_USERS_AGE_ASSURANCE_MANAGE = 346;
  SCOPE_USERS_CONSENT_MANAGE = 334;
  SCOPE_USERS_MEMBERSHIP_REA
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06217"></a>
## FND-06217: chesscom.oauth.v1.Scope.SCOPE_STATS_READ = 331

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_STATS_READ = 331;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1381.

```text
ES_MANAGE = 328;
  SCOPE_PUZZLES_READ = 329;
  SCOPE_SESSION = 330;
  SCOPE_GATEWAY_THEMES = 900;
  SCOPE_STATS_READ = 331;
  SCOPE_STREAKS_ADMIN_READ = 348;
  SCOPE_SUPPORT = 10000;
  SCOPE_SUPPORT_INTERCOM = 10010;
  SCOPE_THEMES = 332;
  SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333;
  SCOPE_USERS_AGE_ASSURANCE_MANAGE = 346;
  SCOPE_USERS_CONSENT_MANAGE = 334;
  SCOPE_USERS_MEMBERSHIP_READ = 335;
  SCOPE_USERS_PROFILE
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06218"></a>
## FND-06218: chesscom.oauth.v1.Scope.SCOPE_STREAKS_ADMIN_READ = 348

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_STREAKS_ADMIN_READ = 348;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1407.

```text
UZZLES_READ = 329;
  SCOPE_SESSION = 330;
  SCOPE_GATEWAY_THEMES = 900;
  SCOPE_STATS_READ = 331;
  SCOPE_STREAKS_ADMIN_READ = 348;
  SCOPE_SUPPORT = 10000;
  SCOPE_SUPPORT_INTERCOM = 10010;
  SCOPE_THEMES = 332;
  SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333;
  SCOPE_USERS_AGE_ASSURANCE_MANAGE = 346;
  SCOPE_USERS_CONSENT_MANAGE = 334;
  SCOPE_USERS_MEMBERSHIP_READ = 335;
  SCOPE_USERS_PROFILE_MANAGE = 336;
  SCOPE_USE
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06219"></a>
## FND-06219: chesscom.oauth.v1.Scope.SCOPE_SUPPORT = 10000

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_SUPPORT = 10000;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1441.

```text
 = 330;
  SCOPE_GATEWAY_THEMES = 900;
  SCOPE_STATS_READ = 331;
  SCOPE_STREAKS_ADMIN_READ = 348;
  SCOPE_SUPPORT = 10000;
  SCOPE_SUPPORT_INTERCOM = 10010;
  SCOPE_THEMES = 332;
  SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333;
  SCOPE_USERS_AGE_ASSURANCE_MANAGE = 346;
  SCOPE_USERS_CONSENT_MANAGE = 334;
  SCOPE_USERS_MEMBERSHIP_READ = 335;
  SCOPE_USERS_PROFILE_MANAGE = 336;
  SCOPE_USERS_SETTINGS_READ = 337;
  SCOPE_US
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06220"></a>
## FND-06220: chesscom.oauth.v1.Scope.SCOPE_SUPPORT_INTERCOM = 10010

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_SUPPORT_INTERCOM = 10010;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1466.

```text
HEMES = 900;
  SCOPE_STATS_READ = 331;
  SCOPE_STREAKS_ADMIN_READ = 348;
  SCOPE_SUPPORT = 10000;
  SCOPE_SUPPORT_INTERCOM = 10010;
  SCOPE_THEMES = 332;
  SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333;
  SCOPE_USERS_AGE_ASSURANCE_MANAGE = 346;
  SCOPE_USERS_CONSENT_MANAGE = 334;
  SCOPE_USERS_MEMBERSHIP_READ = 335;
  SCOPE_USERS_PROFILE_MANAGE = 336;
  SCOPE_USERS_SETTINGS_READ = 337;
  SCOPE_USERS_SETTINGS_WRITE = 338;
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06221"></a>
## FND-06221: chesscom.oauth.v1.Scope.SCOPE_THEMES = 332

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_THEMES = 332;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1500.

```text
331;
  SCOPE_STREAKS_ADMIN_READ = 348;
  SCOPE_SUPPORT = 10000;
  SCOPE_SUPPORT_INTERCOM = 10010;
  SCOPE_THEMES = 332;
  SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333;
  SCOPE_USERS_AGE_ASSURANCE_MANAGE = 346;
  SCOPE_USERS_CONSENT_MANAGE = 334;
  SCOPE_USERS_MEMBERSHIP_READ = 335;
  SCOPE_USERS_PROFILE_MANAGE = 336;
  SCOPE_USERS_SETTINGS_READ = 337;
  SCOPE_USERS_SETTINGS_WRITE = 338;
  SCOPE_USERS_TRACKING_READ = 339
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06222"></a>
## FND-06222: chesscom.oauth.v1.Scope.SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1522.

```text
DMIN_READ = 348;
  SCOPE_SUPPORT = 10000;
  SCOPE_SUPPORT_INTERCOM = 10010;
  SCOPE_THEMES = 332;
  SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333;
  SCOPE_USERS_AGE_ASSURANCE_MANAGE = 346;
  SCOPE_USERS_CONSENT_MANAGE = 334;
  SCOPE_USERS_MEMBERSHIP_READ = 335;
  SCOPE_USERS_PROFILE_MANAGE = 336;
  SCOPE_USERS_SETTINGS_READ = 337;
  SCOPE_USERS_SETTINGS_WRITE = 338;
  SCOPE_USERS_TRACKING_READ = 339;
  SCOPE_USERS_TRACKI
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06223"></a>
## FND-06223: chesscom.oauth.v1.Scope.SCOPE_USERS_AGE_ASSURANCE_MANAGE = 346

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_USERS_AGE_ASSURANCE_MANAGE = 346;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1567.

```text
COPE_SUPPORT_INTERCOM = 10010;
  SCOPE_THEMES = 332;
  SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333;
  SCOPE_USERS_AGE_ASSURANCE_MANAGE = 346;
  SCOPE_USERS_CONSENT_MANAGE = 334;
  SCOPE_USERS_MEMBERSHIP_READ = 335;
  SCOPE_USERS_PROFILE_MANAGE = 336;
  SCOPE_USERS_SETTINGS_READ = 337;
  SCOPE_USERS_SETTINGS_WRITE = 338;
  SCOPE_USERS_TRACKING_READ = 339;
  SCOPE_USERS_TRACKING_WRITE = 340;
  SCOPE_USERS_READ = 341;
  S
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06224"></a>
## FND-06224: chesscom.oauth.v1.Scope.SCOPE_USERS_CONSENT_MANAGE = 334

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_USERS_CONSENT_MANAGE = 334;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1609.

```text
MES = 332;
  SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE = 333;
  SCOPE_USERS_AGE_ASSURANCE_MANAGE = 346;
  SCOPE_USERS_CONSENT_MANAGE = 334;
  SCOPE_USERS_MEMBERSHIP_READ = 335;
  SCOPE_USERS_PROFILE_MANAGE = 336;
  SCOPE_USERS_SETTINGS_READ = 337;
  SCOPE_USERS_SETTINGS_WRITE = 338;
  SCOPE_USERS_TRACKING_READ = 339;
  SCOPE_USERS_TRACKING_WRITE = 340;
  SCOPE_USERS_READ = 341;
  SCOPE_USERS_SEARCH = 342;
  SCOPE_VIDEOS_WR
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06225"></a>
## FND-06225: chesscom.oauth.v1.Scope.SCOPE_USERS_MEMBERSHIP_READ = 335

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_USERS_MEMBERSHIP_READ = 335;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1645.

```text
MENTS_MANAGE = 333;
  SCOPE_USERS_AGE_ASSURANCE_MANAGE = 346;
  SCOPE_USERS_CONSENT_MANAGE = 334;
  SCOPE_USERS_MEMBERSHIP_READ = 335;
  SCOPE_USERS_PROFILE_MANAGE = 336;
  SCOPE_USERS_SETTINGS_READ = 337;
  SCOPE_USERS_SETTINGS_WRITE = 338;
  SCOPE_USERS_TRACKING_READ = 339;
  SCOPE_USERS_TRACKING_WRITE = 340;
  SCOPE_USERS_READ = 341;
  SCOPE_USERS_SEARCH = 342;
  SCOPE_VIDEOS_WRITE = 343;
  SCOPE_VISION = 344;
  S
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06226"></a>
## FND-06226: chesscom.oauth.v1.Scope.SCOPE_USERS_PROFILE_MANAGE = 336

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_USERS_PROFILE_MANAGE = 336;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1682.

```text
_ASSURANCE_MANAGE = 346;
  SCOPE_USERS_CONSENT_MANAGE = 334;
  SCOPE_USERS_MEMBERSHIP_READ = 335;
  SCOPE_USERS_PROFILE_MANAGE = 336;
  SCOPE_USERS_SETTINGS_READ = 337;
  SCOPE_USERS_SETTINGS_WRITE = 338;
  SCOPE_USERS_TRACKING_READ = 339;
  SCOPE_USERS_TRACKING_WRITE = 340;
  SCOPE_USERS_READ = 341;
  SCOPE_USERS_SEARCH = 342;
  SCOPE_VIDEOS_WRITE = 343;
  SCOPE_VISION = 344;
  SCOPE_WORKFLOWS_INCENTIVES_READ = 345;
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06227"></a>
## FND-06227: chesscom.oauth.v1.Scope.SCOPE_USERS_SETTINGS_READ = 337

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_USERS_SETTINGS_READ = 337;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1718.

```text
RS_CONSENT_MANAGE = 334;
  SCOPE_USERS_MEMBERSHIP_READ = 335;
  SCOPE_USERS_PROFILE_MANAGE = 336;
  SCOPE_USERS_SETTINGS_READ = 337;
  SCOPE_USERS_SETTINGS_WRITE = 338;
  SCOPE_USERS_TRACKING_READ = 339;
  SCOPE_USERS_TRACKING_WRITE = 340;
  SCOPE_USERS_READ = 341;
  SCOPE_USERS_SEARCH = 342;
  SCOPE_VIDEOS_WRITE = 343;
  SCOPE_VISION = 344;
  SCOPE_WORKFLOWS_INCENTIVES_READ = 345;
  SCOPE_ADMIN_FAIRPLAY = 20000;
}

```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06228"></a>
## FND-06228: chesscom.oauth.v1.Scope.SCOPE_USERS_SETTINGS_WRITE = 338

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_USERS_SETTINGS_WRITE = 338;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1753.

```text
ERS_MEMBERSHIP_READ = 335;
  SCOPE_USERS_PROFILE_MANAGE = 336;
  SCOPE_USERS_SETTINGS_READ = 337;
  SCOPE_USERS_SETTINGS_WRITE = 338;
  SCOPE_USERS_TRACKING_READ = 339;
  SCOPE_USERS_TRACKING_WRITE = 340;
  SCOPE_USERS_READ = 341;
  SCOPE_USERS_SEARCH = 342;
  SCOPE_VIDEOS_WRITE = 343;
  SCOPE_VISION = 344;
  SCOPE_WORKFLOWS_INCENTIVES_READ = 345;
  SCOPE_ADMIN_FAIRPLAY = 20000;
}

```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06229"></a>
## FND-06229: chesscom.oauth.v1.Scope.SCOPE_USERS_TRACKING_READ = 339

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_USERS_TRACKING_READ = 339;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1789.

```text
SERS_PROFILE_MANAGE = 336;
  SCOPE_USERS_SETTINGS_READ = 337;
  SCOPE_USERS_SETTINGS_WRITE = 338;
  SCOPE_USERS_TRACKING_READ = 339;
  SCOPE_USERS_TRACKING_WRITE = 340;
  SCOPE_USERS_READ = 341;
  SCOPE_USERS_SEARCH = 342;
  SCOPE_VIDEOS_WRITE = 343;
  SCOPE_VISION = 344;
  SCOPE_WORKFLOWS_INCENTIVES_READ = 345;
  SCOPE_ADMIN_FAIRPLAY = 20000;
}

```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06230"></a>
## FND-06230: chesscom.oauth.v1.Scope.SCOPE_USERS_TRACKING_WRITE = 340

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_USERS_TRACKING_WRITE = 340;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1824.

```text
USERS_SETTINGS_READ = 337;
  SCOPE_USERS_SETTINGS_WRITE = 338;
  SCOPE_USERS_TRACKING_READ = 339;
  SCOPE_USERS_TRACKING_WRITE = 340;
  SCOPE_USERS_READ = 341;
  SCOPE_USERS_SEARCH = 342;
  SCOPE_VIDEOS_WRITE = 343;
  SCOPE_VISION = 344;
  SCOPE_WORKFLOWS_INCENTIVES_READ = 345;
  SCOPE_ADMIN_FAIRPLAY = 20000;
}

```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06231"></a>
## FND-06231: chesscom.oauth.v1.Scope.SCOPE_USERS_READ = 341

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_USERS_READ = 341;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1860.

```text
SERS_SETTINGS_WRITE = 338;
  SCOPE_USERS_TRACKING_READ = 339;
  SCOPE_USERS_TRACKING_WRITE = 340;
  SCOPE_USERS_READ = 341;
  SCOPE_USERS_SEARCH = 342;
  SCOPE_VIDEOS_WRITE = 343;
  SCOPE_VISION = 344;
  SCOPE_WORKFLOWS_INCENTIVES_READ = 345;
  SCOPE_ADMIN_FAIRPLAY = 20000;
}

```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06232"></a>
## FND-06232: chesscom.oauth.v1.Scope.SCOPE_USERS_SEARCH = 342

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_USERS_SEARCH = 342;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1886.

```text

  SCOPE_USERS_TRACKING_READ = 339;
  SCOPE_USERS_TRACKING_WRITE = 340;
  SCOPE_USERS_READ = 341;
  SCOPE_USERS_SEARCH = 342;
  SCOPE_VIDEOS_WRITE = 343;
  SCOPE_VISION = 344;
  SCOPE_WORKFLOWS_INCENTIVES_READ = 345;
  SCOPE_ADMIN_FAIRPLAY = 20000;
}

```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06233"></a>
## FND-06233: chesscom.oauth.v1.Scope.SCOPE_VIDEOS_WRITE = 343

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_VIDEOS_WRITE = 343;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1914.

```text
 = 339;
  SCOPE_USERS_TRACKING_WRITE = 340;
  SCOPE_USERS_READ = 341;
  SCOPE_USERS_SEARCH = 342;
  SCOPE_VIDEOS_WRITE = 343;
  SCOPE_VISION = 344;
  SCOPE_WORKFLOWS_INCENTIVES_READ = 345;
  SCOPE_ADMIN_FAIRPLAY = 20000;
}

```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06234"></a>
## FND-06234: chesscom.oauth.v1.Scope.SCOPE_VISION = 344

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_VISION = 344;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1942.

```text
NG_WRITE = 340;
  SCOPE_USERS_READ = 341;
  SCOPE_USERS_SEARCH = 342;
  SCOPE_VIDEOS_WRITE = 343;
  SCOPE_VISION = 344;
  SCOPE_WORKFLOWS_INCENTIVES_READ = 345;
  SCOPE_ADMIN_FAIRPLAY = 20000;
}

```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06235"></a>
## FND-06235: chesscom.oauth.v1.Scope.SCOPE_WORKFLOWS_INCENTIVES_READ = 345

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_WORKFLOWS_INCENTIVES_READ = 345;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 1964.

```text
E_USERS_READ = 341;
  SCOPE_USERS_SEARCH = 342;
  SCOPE_VIDEOS_WRITE = 343;
  SCOPE_VISION = 344;
  SCOPE_WORKFLOWS_INCENTIVES_READ = 345;
  SCOPE_ADMIN_FAIRPLAY = 20000;
}

```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06236"></a>
## FND-06236: chesscom.oauth.v1.Scope.SCOPE_ADMIN_FAIRPLAY = 20000

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_ADMIN_FAIRPLAY = 20000;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 2005.

```text
= 342;
  SCOPE_VIDEOS_WRITE = 343;
  SCOPE_VISION = 344;
  SCOPE_WORKFLOWS_INCENTIVES_READ = 345;
  SCOPE_ADMIN_FAIRPLAY = 20000;
}

```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06237"></a>
## FND-06237: message declaration: chesscom.payments.v1.AvailablePaymentMethod

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AvailablePaymentMethod {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 113.

```text
esscom/payments/v1/available_payment_method.proto
// syntax: proto3

package chesscom.payments.v1;

message AvailablePaymentMethod {
  optional string gateway = 1;
  optional string method = 2;
  optional .chesscom.payments.v1.PaymentMethodConfig config = 3;
}

message PaymentMethodConfig {
  oneof _parameters {
  .chesscom.payments.v1.PaymentParameters parameters = 5;
  }
  oneof _cvv_confirmation_required {
  bool 
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06238"></a>
## FND-06238: chesscom.payments.v1.AvailablePaymentMethod.gateway = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string gateway = 1;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 148.

```text
t_method.proto
// syntax: proto3

package chesscom.payments.v1;

message AvailablePaymentMethod {
  optional string gateway = 1;
  optional string method = 2;
  optional .chesscom.payments.v1.PaymentMethodConfig config = 3;
}

message PaymentMethodConfig {
  oneof _parameters {
  .chesscom.payments.v1.PaymentParameters parameters = 5;
  }
  oneof _cvv_confirmation_required {
  bool cvv_confirmation_required = 8;
  }

```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06239"></a>
## FND-06239: chesscom.payments.v1.AvailablePaymentMethod.method = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string method = 2;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 179.

```text
3

package chesscom.payments.v1;

message AvailablePaymentMethod {
  optional string gateway = 1;
  optional string method = 2;
  optional .chesscom.payments.v1.PaymentMethodConfig config = 3;
}

message PaymentMethodConfig {
  oneof _parameters {
  .chesscom.payments.v1.PaymentParameters parameters = 5;
  }
  oneof _cvv_confirmation_required {
  bool cvv_confirmation_required = 8;
  }
  oneof _captcha {
  string cap
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06240"></a>
## FND-06240: chesscom.payments.v1.AvailablePaymentMethod.config = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.PaymentMethodConfig config = 3;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 209.

```text
1;

message AvailablePaymentMethod {
  optional string gateway = 1;
  optional string method = 2;
  optional .chesscom.payments.v1.PaymentMethodConfig config = 3;
}

message PaymentMethodConfig {
  oneof _parameters {
  .chesscom.payments.v1.PaymentParameters parameters = 5;
  }
  oneof _cvv_confirmation_required {
  bool cvv_confirmation_required = 8;
  }
  oneof _captcha {
  string captcha = 9;
  }
  optional strin
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06241"></a>
## FND-06241: message declaration: chesscom.payments.v1.PaymentMethodConfig

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PaymentMethodConfig {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 275.

```text
;
  optional string method = 2;
  optional .chesscom.payments.v1.PaymentMethodConfig config = 3;
}

message PaymentMethodConfig {
  oneof _parameters {
  .chesscom.payments.v1.PaymentParameters parameters = 5;
  }
  oneof _cvv_confirmation_required {
  bool cvv_confirmation_required = 8;
  }
  oneof _captcha {
  string captcha = 9;
  }
  optional string id = 1;
  optional string type = 2;
  optional string name = 3;

```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06242"></a>
## FND-06242: oneof declaration: chesscom.payments.v1.PaymentMethodConfig._parameters

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _parameters {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 307.

```text
  optional .chesscom.payments.v1.PaymentMethodConfig config = 3;
}

message PaymentMethodConfig {
  oneof _parameters {
  .chesscom.payments.v1.PaymentParameters parameters = 5;
  }
  oneof _cvv_confirmation_required {
  bool cvv_confirmation_required = 8;
  }
  oneof _captcha {
  string captcha = 9;
  }
  optional string id = 1;
  optional string type = 2;
  optional string name = 3;
  optional string image = 4;
  r
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06243"></a>
## FND-06243: chesscom.payments.v1.PaymentMethodConfig.parameters = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.PaymentParameters parameters = 5;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 329.

```text
ayments.v1.PaymentMethodConfig config = 3;
}

message PaymentMethodConfig {
  oneof _parameters {
  .chesscom.payments.v1.PaymentParameters parameters = 5;
  }
  oneof _cvv_confirmation_required {
  bool cvv_confirmation_required = 8;
  }
  oneof _captcha {
  string captcha = 9;
  }
  optional string id = 1;
  optional string type = 2;
  optional string name = 3;
  optional string image = 4;
  repeated .chesscom.paym
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06244"></a>
## FND-06244: oneof declaration: chesscom.payments.v1.PaymentMethodConfig._cvv_confirmation_required

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _cvv_confirmation_required {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 391.

```text
ethodConfig {
  oneof _parameters {
  .chesscom.payments.v1.PaymentParameters parameters = 5;
  }
  oneof _cvv_confirmation_required {
  bool cvv_confirmation_required = 8;
  }
  oneof _captcha {
  string captcha = 9;
  }
  optional string id = 1;
  optional string type = 2;
  optional string name = 3;
  optional string image = 4;
  repeated .chesscom.payments.v1.AdditionalDataField additional_data_required = 6;
  re
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06245"></a>
## FND-06245: chesscom.payments.v1.PaymentMethodConfig.cvv_confirmation_required = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool cvv_confirmation_required = 8;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 428.

```text
 .chesscom.payments.v1.PaymentParameters parameters = 5;
  }
  oneof _cvv_confirmation_required {
  bool cvv_confirmation_required = 8;
  }
  oneof _captcha {
  string captcha = 9;
  }
  optional string id = 1;
  optional string type = 2;
  optional string name = 3;
  optional string image = 4;
  repeated .chesscom.payments.v1.AdditionalDataField additional_data_required = 6;
  repeated .chesscom.payments.v1.StoredPa
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06246"></a>
## FND-06246: oneof declaration: chesscom.payments.v1.PaymentMethodConfig._captcha

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _captcha {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 470.

```text
arameters = 5;
  }
  oneof _cvv_confirmation_required {
  bool cvv_confirmation_required = 8;
  }
  oneof _captcha {
  string captcha = 9;
  }
  optional string id = 1;
  optional string type = 2;
  optional string name = 3;
  optional string image = 4;
  repeated .chesscom.payments.v1.AdditionalDataField additional_data_required = 6;
  repeated .chesscom.payments.v1.StoredPaymentDetail stored_payment_details = 7;
}

```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06247"></a>
## FND-06247: chesscom.payments.v1.PaymentMethodConfig.captcha = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string captcha = 9;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 489.

```text
  oneof _cvv_confirmation_required {
  bool cvv_confirmation_required = 8;
  }
  oneof _captcha {
  string captcha = 9;
  }
  optional string id = 1;
  optional string type = 2;
  optional string name = 3;
  optional string image = 4;
  repeated .chesscom.payments.v1.AdditionalDataField additional_data_required = 6;
  repeated .chesscom.payments.v1.StoredPaymentDetail stored_payment_details = 7;
}

message PaymentPar
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06248"></a>
## FND-06248: chesscom.payments.v1.PaymentMethodConfig.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 515.

```text
required {
  bool cvv_confirmation_required = 8;
  }
  oneof _captcha {
  string captcha = 9;
  }
  optional string id = 1;
  optional string type = 2;
  optional string name = 3;
  optional string image = 4;
  repeated .chesscom.payments.v1.AdditionalDataField additional_data_required = 6;
  repeated .chesscom.payments.v1.StoredPaymentDetail stored_payment_details = 7;
}

message PaymentParameters {
  oneof _environ
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06249"></a>
## FND-06249: chesscom.payments.v1.PaymentMethodConfig.type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string type = 2;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 541.

```text
irmation_required = 8;
  }
  oneof _captcha {
  string captcha = 9;
  }
  optional string id = 1;
  optional string type = 2;
  optional string name = 3;
  optional string image = 4;
  repeated .chesscom.payments.v1.AdditionalDataField additional_data_required = 6;
  repeated .chesscom.payments.v1.StoredPaymentDetail stored_payment_details = 7;
}

message PaymentParameters {
  oneof _environment {
  string environmen
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06250"></a>
## FND-06250: chesscom.payments.v1.PaymentMethodConfig.name = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 3;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 569.

```text
 oneof _captcha {
  string captcha = 9;
  }
  optional string id = 1;
  optional string type = 2;
  optional string name = 3;
  optional string image = 4;
  repeated .chesscom.payments.v1.AdditionalDataField additional_data_required = 6;
  repeated .chesscom.payments.v1.StoredPaymentDetail stored_payment_details = 7;
}

message PaymentParameters {
  oneof _environment {
  string environment = 1;
  }
  oneof _integrit
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06251"></a>
## FND-06251: chesscom.payments.v1.PaymentMethodConfig.image = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string image = 4;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 597.

```text
aptcha = 9;
  }
  optional string id = 1;
  optional string type = 2;
  optional string name = 3;
  optional string image = 4;
  repeated .chesscom.payments.v1.AdditionalDataField additional_data_required = 6;
  repeated .chesscom.payments.v1.StoredPaymentDetail stored_payment_details = 7;
}

message PaymentParameters {
  oneof _environment {
  string environment = 1;
  }
  oneof _integrity {
  string integrity = 2;

```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06252"></a>
## FND-06252: chesscom.payments.v1.PaymentMethodConfig.additional_data_required = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.AdditionalDataField additional_data_required = 6;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 626.

```text
ring id = 1;
  optional string type = 2;
  optional string name = 3;
  optional string image = 4;
  repeated .chesscom.payments.v1.AdditionalDataField additional_data_required = 6;
  repeated .chesscom.payments.v1.StoredPaymentDetail stored_payment_details = 7;
}

message PaymentParameters {
  oneof _environment {
  string environment = 1;
  }
  oneof _integrity {
  string integrity = 2;
  }
  oneof _client_id {
  st
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06253"></a>
## FND-06253: chesscom.payments.v1.PaymentMethodConfig.stored_payment_details = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.StoredPaymentDetail stored_payment_details = 7;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 709.

```text
ing image = 4;
  repeated .chesscom.payments.v1.AdditionalDataField additional_data_required = 6;
  repeated .chesscom.payments.v1.StoredPaymentDetail stored_payment_details = 7;
}

message PaymentParameters {
  oneof _environment {
  string environment = 1;
  }
  oneof _integrity {
  string integrity = 2;
  }
  oneof _client_id {
  string client_id = 3;
  }
  oneof _key {
  string key = 4;
  }
  oneof _merchant {
  
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06254"></a>
## FND-06254: message declaration: chesscom.payments.v1.PaymentParameters

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PaymentParameters {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 791.

```text
a_required = 6;
  repeated .chesscom.payments.v1.StoredPaymentDetail stored_payment_details = 7;
}

message PaymentParameters {
  oneof _environment {
  string environment = 1;
  }
  oneof _integrity {
  string integrity = 2;
  }
  oneof _client_id {
  string client_id = 3;
  }
  oneof _key {
  string key = 4;
  }
  oneof _merchant {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneo
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06255"></a>
## FND-06255: oneof declaration: chesscom.payments.v1.PaymentParameters._environment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _environment {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 821.

```text
esscom.payments.v1.StoredPaymentDetail stored_payment_details = 7;
}

message PaymentParameters {
  oneof _environment {
  string environment = 1;
  }
  oneof _integrity {
  string integrity = 2;
  }
  oneof _client_id {
  string client_id = 3;
  }
  oneof _key {
  string key = 4;
  }
  oneof _merchant {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06256"></a>
## FND-06256: chesscom.payments.v1.PaymentParameters.environment = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string environment = 1;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 844.

```text
edPaymentDetail stored_payment_details = 7;
}

message PaymentParameters {
  oneof _environment {
  string environment = 1;
  }
  oneof _integrity {
  string integrity = 2;
  }
  oneof _client_id {
  string client_id = 3;
  }
  oneof _key {
  string key = 4;
  }
  oneof _merchant {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {

```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06257"></a>
## FND-06257: oneof declaration: chesscom.payments.v1.PaymentParameters._integrity

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _integrity {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 874.

```text
_details = 7;
}

message PaymentParameters {
  oneof _environment {
  string environment = 1;
  }
  oneof _integrity {
  string integrity = 2;
  }
  oneof _client_id {
  string client_id = 3;
  }
  oneof _key {
  string key = 4;
  }
  oneof _merchant {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
 
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06258"></a>
## FND-06258: chesscom.payments.v1.PaymentParameters.integrity = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string integrity = 2;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 895.

```text
age PaymentParameters {
  oneof _environment {
  string environment = 1;
  }
  oneof _integrity {
  string integrity = 2;
  }
  oneof _client_id {
  string client_id = 3;
  }
  oneof _key {
  string key = 4;
  }
  oneof _merchant {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06259"></a>
## FND-06259: oneof declaration: chesscom.payments.v1.PaymentParameters._client_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _client_id {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 923.

```text
eof _environment {
  string environment = 1;
  }
  oneof _integrity {
  string integrity = 2;
  }
  oneof _client_id {
  string client_id = 3;
  }
  oneof _key {
  string key = 4;
  }
  oneof _merchant {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
 
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06260"></a>
## FND-06260: chesscom.payments.v1.PaymentParameters.client_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string client_id = 3;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 944.

```text
string environment = 1;
  }
  oneof _integrity {
  string integrity = 2;
  }
  oneof _client_id {
  string client_id = 3;
  }
  oneof _key {
  string key = 4;
  }
  oneof _merchant {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06261"></a>
## FND-06261: oneof declaration: chesscom.payments.v1.PaymentParameters._key

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _key {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 972.

```text
  oneof _integrity {
  string integrity = 2;
  }
  oneof _client_id {
  string client_id = 3;
  }
  oneof _key {
  string key = 4;
  }
  oneof _merchant {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_name {
  string merchant_nam
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06262"></a>
## FND-06262: chesscom.payments.v1.PaymentParameters.key = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string key = 4;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 987.

```text
ity {
  string integrity = 2;
  }
  oneof _client_id {
  string client_id = 3;
  }
  oneof _key {
  string key = 4;
  }
  oneof _merchant {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_name {
  string merchant_name = 10;
  }
}


```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06263"></a>
## FND-06263: oneof declaration: chesscom.payments.v1.PaymentParameters._merchant

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _merchant {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1009.

```text
ty = 2;
  }
  oneof _client_id {
  string client_id = 3;
  }
  oneof _key {
  string key = 4;
  }
  oneof _merchant {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_name {
  string merchant_name = 10;
  }
}

message AdditionalData
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06264"></a>
## FND-06264: chesscom.payments.v1.PaymentParameters.merchant = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string merchant = 5;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1029.

```text
_client_id {
  string client_id = 3;
  }
  oneof _key {
  string key = 4;
  }
  oneof _merchant {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_name {
  string merchant_name = 10;
  }
}

message AdditionalDataField {
  oneof _val
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06265"></a>
## FND-06265: oneof declaration: chesscom.payments.v1.PaymentParameters._origin_key

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _origin_key {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1056.

```text
t_id = 3;
  }
  oneof _key {
  string key = 4;
  }
  oneof _merchant {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_name {
  string merchant_name = 10;
  }
}

message AdditionalDataField {
  oneof _validation_rule {
  string val
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06266"></a>
## FND-06266: chesscom.payments.v1.PaymentParameters.origin_key = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string origin_key = 6;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1078.

```text
_key {
  string key = 4;
  }
  oneof _merchant {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_name {
  string merchant_name = 10;
  }
}

message AdditionalDataField {
  oneof _validation_rule {
  string validation_rule = 6;
  }

```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06267"></a>
## FND-06267: oneof declaration: chesscom.payments.v1.PaymentParameters._sdk

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _sdk {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1107.

```text
  oneof _merchant {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_name {
  string merchant_name = 10;
  }
}

message AdditionalDataField {
  oneof _validation_rule {
  string validation_rule = 6;
  }
  oneof _validation_err_msg {
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06268"></a>
## FND-06268: chesscom.payments.v1.PaymentParameters.sdk = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string sdk = 7;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1122.

```text
nt {
  string merchant = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_name {
  string merchant_name = 10;
  }
}

message AdditionalDataField {
  oneof _validation_rule {
  string validation_rule = 6;
  }
  oneof _validation_err_msg {
  string valid
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06269"></a>
## FND-06269: oneof declaration: chesscom.payments.v1.PaymentParameters._script_src

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _script_src {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1144.

```text
 = 5;
  }
  oneof _origin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_name {
  string merchant_name = 10;
  }
}

message AdditionalDataField {
  oneof _validation_rule {
  string validation_rule = 6;
  }
  oneof _validation_err_msg {
  string validation_err_msg = 7;
  }
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06270"></a>
## FND-06270: chesscom.payments.v1.PaymentParameters.script_src = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string script_src = 8;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1166.

```text
gin_key {
  string origin_key = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_name {
  string merchant_name = 10;
  }
}

message AdditionalDataField {
  oneof _validation_rule {
  string validation_rule = 6;
  }
  oneof _validation_err_msg {
  string validation_err_msg = 7;
  }
  optional string nam
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06271"></a>
## FND-06271: oneof declaration: chesscom.payments.v1.PaymentParameters._merchant_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _merchant_id {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1195.

```text
 = 6;
  }
  oneof _sdk {
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_name {
  string merchant_name = 10;
  }
}

message AdditionalDataField {
  oneof _validation_rule {
  string validation_rule = 6;
  }
  oneof _validation_err_msg {
  string validation_err_msg = 7;
  }
  optional string name = 1;
  optional string labe
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06272"></a>
## FND-06272: chesscom.payments.v1.PaymentParameters.merchant_id = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string merchant_id = 9;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1218.

```text
{
  string sdk = 7;
  }
  oneof _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_name {
  string merchant_name = 10;
  }
}

message AdditionalDataField {
  oneof _validation_rule {
  string validation_rule = 6;
  }
  oneof _validation_err_msg {
  string validation_err_msg = 7;
  }
  optional string name = 1;
  optional string label = 2;
  optional .ches
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06273"></a>
## FND-06273: oneof declaration: chesscom.payments.v1.PaymentParameters._merchant_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _merchant_name {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1248.

```text
f _script_src {
  string script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_name {
  string merchant_name = 10;
  }
}

message AdditionalDataField {
  oneof _validation_rule {
  string validation_rule = 6;
  }
  oneof _validation_err_msg {
  string validation_err_msg = 7;
  }
  optional string name = 1;
  optional string label = 2;
  optional .chesscom.payments.v1.AdditionalDat
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06274"></a>
## FND-06274: chesscom.payments.v1.PaymentParameters.merchant_name = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string merchant_name = 10;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1273.

```text
script_src = 8;
  }
  oneof _merchant_id {
  string merchant_id = 9;
  }
  oneof _merchant_name {
  string merchant_name = 10;
  }
}

message AdditionalDataField {
  oneof _validation_rule {
  string validation_rule = 6;
  }
  oneof _validation_err_msg {
  string validation_err_msg = 7;
  }
  optional string name = 1;
  optional string label = 2;
  optional .chesscom.payments.v1.AdditionalDataFieldType type = 3;
  op
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
