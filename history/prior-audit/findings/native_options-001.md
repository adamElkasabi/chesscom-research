# native_options — findings 1–100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-19030"></a>
## FND-19030: Advertised UCI LogFD

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name LogFD default -1

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 69.

```text
Explanation Engine 1.130.285 (C) 2025 Chess.com, LLC
info string CEE
option name LogFD default -1
option name IllegalMoveExplanationMode default all
option name ForceDisableInternalEngineSearches default false
option name PlayVsCoachRetryMissesEnabled default false
option name GameFinishedAtMs default 0
option name Threads default 1
option name UsePersonalizedGameOverModal default false
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19031"></a>
## FND-19031: Advertised UCI IllegalMoveExplanationMode

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name IllegalMoveExplanationMode default all

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 98.

```text
Explanation Engine 1.130.285 (C) 2025 Chess.com, LLC
info string CEE
option name LogFD default -1
option name IllegalMoveExplanationMode default all
option name ForceDisableInternalEngineSearches default false
option name PlayVsCoachRetryMissesEnabled default false
option name GameFinishedAtMs default 0
option name Threads default 1
option name UsePersonalizedGameOverModal default false
option name CoachAssetsV2 de
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19032"></a>
## FND-19032: Advertised UCI ForceDisableInternalEngineSearches

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name ForceDisableInternalEngineSearches default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 149.

```text
LLC
info string CEE
option name LogFD default -1
option name IllegalMoveExplanationMode default all
option name ForceDisableInternalEngineSearches default false
option name PlayVsCoachRetryMissesEnabled default false
option name GameFinishedAtMs default 0
option name Threads default 1
option name UsePersonalizedGameOverModal default false
option name CoachAssetsV2 default true
option name BasicVariationThemes default
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19033"></a>
## FND-19033: Advertised UCI PlayVsCoachRetryMissesEnabled

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name PlayVsCoachRetryMissesEnabled default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 210.

```text
IllegalMoveExplanationMode default all
option name ForceDisableInternalEngineSearches default false
option name PlayVsCoachRetryMissesEnabled default false
option name GameFinishedAtMs default 0
option name Threads default 1
option name UsePersonalizedGameOverModal default false
option name CoachAssetsV2 default true
option name BasicVariationThemes default false
option name CoachTextId default 
option name UseOpposi
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19034"></a>
## FND-19034: Advertised UCI GameFinishedAtMs

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name GameFinishedAtMs default 0

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 266.

```text
DisableInternalEngineSearches default false
option name PlayVsCoachRetryMissesEnabled default false
option name GameFinishedAtMs default 0
option name Threads default 1
option name UsePersonalizedGameOverModal default false
option name CoachAssetsV2 default true
option name BasicVariationThemes default false
option name CoachTextId default 
option name UseOpposingCoachSpeech default true
option name NullMoveRepresent
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19035"></a>
## FND-19035: Advertised UCI Threads

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name Threads default 1

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 305.

```text
alse
option name PlayVsCoachRetryMissesEnabled default false
option name GameFinishedAtMs default 0
option name Threads default 1
option name UsePersonalizedGameOverModal default false
option name CoachAssetsV2 default true
option name BasicVariationThemes default false
option name CoachTextId default 
option name UseOpposingCoachSpeech default true
option name NullMoveRepresentation default (none)
option name BotNam
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19036"></a>
## FND-19036: Advertised UCI UsePersonalizedGameOverModal

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name UsePersonalizedGameOverModal default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 335.

```text
tryMissesEnabled default false
option name GameFinishedAtMs default 0
option name Threads default 1
option name UsePersonalizedGameOverModal default false
option name CoachAssetsV2 default true
option name BasicVariationThemes default false
option name CoachTextId default 
option name UseOpposingCoachSpeech default true
option name NullMoveRepresentation default (none)
option name BotName default 
option name IsRated
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19037"></a>
## FND-19037: Advertised UCI CoachAssetsV2

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name CoachAssetsV2 default true

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 390.

```text
AtMs default 0
option name Threads default 1
option name UsePersonalizedGameOverModal default false
option name CoachAssetsV2 default true
option name BasicVariationThemes default false
option name CoachTextId default 
option name UseOpposingCoachSpeech default true
option name NullMoveRepresentation default (none)
option name BotName default 
option name IsRated default false
option name Chess960 default false
optio
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19038"></a>
## FND-19038: Advertised UCI BasicVariationThemes

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name BasicVariationThemes default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 429.

```text
ult 1
option name UsePersonalizedGameOverModal default false
option name CoachAssetsV2 default true
option name BasicVariationThemes default false
option name CoachTextId default 
option name UseOpposingCoachSpeech default true
option name NullMoveRepresentation default (none)
option name BotName default 
option name IsRated default false
option name Chess960 default false
option name ChesscomGameId default 
option n
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19039"></a>
## FND-19039: Advertised UCI CoachTextId

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name CoachTextId default 

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 476.

```text
default false
option name CoachAssetsV2 default true
option name BasicVariationThemes default false
option name CoachTextId default 
option name UseOpposingCoachSpeech default true
option name NullMoveRepresentation default (none)
option name BotName default 
option name IsRated default false
option name Chess960 default false
option name ChesscomGameId default 
option name UseRatingRanges default false
option name B
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19040"></a>
## FND-19040: Advertised UCI UseOpposingCoachSpeech

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name UseOpposingCoachSpeech default true

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 509.

```text
setsV2 default true
option name BasicVariationThemes default false
option name CoachTextId default 
option name UseOpposingCoachSpeech default true
option name NullMoveRepresentation default (none)
option name BotName default 
option name IsRated default false
option name Chess960 default false
option name ChesscomGameId default 
option name UseRatingRanges default false
option name BlackChesscomUserId default 
optio
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19041"></a>
## FND-19041: Advertised UCI NullMoveRepresentation

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name NullMoveRepresentation default (none)

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 557.

```text
emes default false
option name CoachTextId default 
option name UseOpposingCoachSpeech default true
option name NullMoveRepresentation default (none)
option name BotName default 
option name IsRated default false
option name Chess960 default false
option name ChesscomGameId default 
option name UseRatingRanges default false
option name BlackChesscomUserId default 
option name SerializeSpeechDetails default false
opti
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19042"></a>
## FND-19042: Advertised UCI BotName

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name BotName default 

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 607.

```text
 
option name UseOpposingCoachSpeech default true
option name NullMoveRepresentation default (none)
option name BotName default 
option name IsRated default false
option name Chess960 default false
option name ChesscomGameId default 
option name UseRatingRanges default false
option name BlackChesscomUserId default 
option name SerializeSpeechDetails default false
option name WhiteChesscomUserId default 
option name F
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19043"></a>
## FND-19043: Advertised UCI IsRated

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name IsRated default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 636.

```text
hSpeech default true
option name NullMoveRepresentation default (none)
option name BotName default 
option name IsRated default false
option name Chess960 default false
option name ChesscomGameId default 
option name UseRatingRanges default false
option name BlackChesscomUserId default 
option name SerializeSpeechDetails default false
option name WhiteChesscomUserId default 
option name ForgivingClassificationsElo de
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19044"></a>
## FND-19044: Advertised UCI Chess960

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name Chess960 default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 670.

```text
ullMoveRepresentation default (none)
option name BotName default 
option name IsRated default false
option name Chess960 default false
option name ChesscomGameId default 
option name UseRatingRanges default false
option name BlackChesscomUserId default 
option name SerializeSpeechDetails default false
option name WhiteChesscomUserId default 
option name ForgivingClassificationsElo default 0
option name TimeControl de
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19045"></a>
## FND-19045: Advertised UCI ChesscomGameId

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name ChesscomGameId default 

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 705.

```text
)
option name BotName default 
option name IsRated default false
option name Chess960 default false
option name ChesscomGameId default 
option name UseRatingRanges default false
option name BlackChesscomUserId default 
option name SerializeSpeechDetails default false
option name WhiteChesscomUserId default 
option name ForgivingClassificationsElo default 0
option name TimeControl default 
option name HandleNullMoveCo
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19046"></a>
## FND-19046: Advertised UCI UseRatingRanges

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name UseRatingRanges default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 741.

```text
n name IsRated default false
option name Chess960 default false
option name ChesscomGameId default 
option name UseRatingRanges default false
option name BlackChesscomUserId default 
option name SerializeSpeechDetails default false
option name WhiteChesscomUserId default 
option name ForgivingClassificationsElo default 0
option name TimeControl default 
option name HandleNullMoveContinuations default false
option nam
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19047"></a>
## FND-19047: Advertised UCI BlackChesscomUserId

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name BlackChesscomUserId default 

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 783.

```text
hess960 default false
option name ChesscomGameId default 
option name UseRatingRanges default false
option name BlackChesscomUserId default 
option name SerializeSpeechDetails default false
option name WhiteChesscomUserId default 
option name ForgivingClassificationsElo default 0
option name TimeControl default 
option name HandleNullMoveContinuations default false
option name Termination default *
option name Chessc
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19048"></a>
## FND-19048: Advertised UCI SerializeSpeechDetails

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name SerializeSpeechDetails default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 824.

```text
mGameId default 
option name UseRatingRanges default false
option name BlackChesscomUserId default 
option name SerializeSpeechDetails default false
option name WhiteChesscomUserId default 
option name ForgivingClassificationsElo default 0
option name TimeControl default 
option name HandleNullMoveContinuations default false
option name Termination default *
option name ChesscomGameMetadataPb default 
option name Use
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19049"></a>
## FND-19049: Advertised UCI WhiteChesscomUserId

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name WhiteChesscomUserId default 

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 873.

```text
ult false
option name BlackChesscomUserId default 
option name SerializeSpeechDetails default false
option name WhiteChesscomUserId default 
option name ForgivingClassificationsElo default 0
option name TimeControl default 
option name HandleNullMoveContinuations default false
option name Termination default *
option name ChesscomGameMetadataPb default 
option name UserColor default NotSpecified
option name HumanPlay
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19050"></a>
## FND-19050: Advertised UCI ForgivingClassificationsElo

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name ForgivingClassificationsElo default 0

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 914.

```text
 default 
option name SerializeSpeechDetails default false
option name WhiteChesscomUserId default 
option name ForgivingClassificationsElo default 0
option name TimeControl default 
option name HandleNullMoveContinuations default false
option name Termination default *
option name ChesscomGameMetadataPb default 
option name UserColor default NotSpecified
option name HumanPlaysBlack default false
option name LogFile 
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19051"></a>
## FND-19051: Advertised UCI TimeControl

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name TimeControl default 

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 964.

```text
lt false
option name WhiteChesscomUserId default 
option name ForgivingClassificationsElo default 0
option name TimeControl default 
option name HandleNullMoveContinuations default false
option name Termination default *
option name ChesscomGameMetadataPb default 
option name UserColor default NotSpecified
option name HumanPlaysBlack default false
option name LogFile default -
option name NewSpeech default false
opti
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19052"></a>
## FND-19052: Advertised UCI HandleNullMoveContinuations

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name HandleNullMoveContinuations default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 997.

```text
mUserId default 
option name ForgivingClassificationsElo default 0
option name TimeControl default 
option name HandleNullMoveContinuations default false
option name Termination default *
option name ChesscomGameMetadataPb default 
option name UserColor default NotSpecified
option name HumanPlaysBlack default false
option name LogFile default -
option name NewSpeech default false
option name WhiteChesscomUsername def
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19053"></a>
## FND-19053: Advertised UCI Termination

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name Termination default *

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1051.

```text
lo default 0
option name TimeControl default 
option name HandleNullMoveContinuations default false
option name Termination default *
option name ChesscomGameMetadataPb default 
option name UserColor default NotSpecified
option name HumanPlaysBlack default false
option name LogFile default -
option name NewSpeech default false
option name WhiteChesscomUsername default 
option name Strength default 
option name Suppre
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19054"></a>
## FND-19054: Advertised UCI ChesscomGameMetadataPb

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name ChesscomGameMetadataPb default 

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1085.

```text
ol default 
option name HandleNullMoveContinuations default false
option name Termination default *
option name ChesscomGameMetadataPb default 
option name UserColor default NotSpecified
option name HumanPlaysBlack default false
option name LogFile default -
option name NewSpeech default false
option name WhiteChesscomUsername default 
option name Strength default 
option name SuppressBrilliantSpeech default false
op
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19055"></a>
## FND-19055: Advertised UCI UserColor

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name UserColor default NotSpecified

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1129.

```text
uations default false
option name Termination default *
option name ChesscomGameMetadataPb default 
option name UserColor default NotSpecified
option name HumanPlaysBlack default false
option name LogFile default -
option name NewSpeech default false
option name WhiteChesscomUsername default 
option name Strength default 
option name SuppressBrilliantSpeech default false
option name SpeechV2 default false
option name
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19056"></a>
## FND-19056: Advertised UCI HumanPlaysBlack

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name HumanPlaysBlack default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1172.

```text
on default *
option name ChesscomGameMetadataPb default 
option name UserColor default NotSpecified
option name HumanPlaysBlack default false
option name LogFile default -
option name NewSpeech default false
option name WhiteChesscomUsername default 
option name Strength default 
option name SuppressBrilliantSpeech default false
option name SpeechV2 default false
option name BotChatPrioritizePlayerMovePercent default
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19057"></a>
## FND-19057: Advertised UCI LogFile

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name LogFile default -

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1214.

```text
ataPb default 
option name UserColor default NotSpecified
option name HumanPlaysBlack default false
option name LogFile default -
option name NewSpeech default false
option name WhiteChesscomUsername default 
option name Strength default 
option name SuppressBrilliantSpeech default false
option name SpeechV2 default false
option name BotChatPrioritizePlayerMovePercent default 50
option name BotChatPrioritizePlayerMov
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19058"></a>
## FND-19058: Advertised UCI NewSpeech

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name NewSpeech default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1244.

```text
rColor default NotSpecified
option name HumanPlaysBlack default false
option name LogFile default -
option name NewSpeech default false
option name WhiteChesscomUsername default 
option name Strength default 
option name SuppressBrilliantSpeech default false
option name SpeechV2 default false
option name BotChatPrioritizePlayerMovePercent default 50
option name BotChatPrioritizePlayerMove default false
option name Ga
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19059"></a>
## FND-19059: Advertised UCI WhiteChesscomUsername

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name WhiteChesscomUsername default 

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1280.

```text
ame HumanPlaysBlack default false
option name LogFile default -
option name NewSpeech default false
option name WhiteChesscomUsername default 
option name Strength default 
option name SuppressBrilliantSpeech default false
option name SpeechV2 default false
option name BotChatPrioritizePlayerMovePercent default 50
option name BotChatPrioritizePlayerMove default false
option name GamePhaseV2 default true
option name S
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19060"></a>
## FND-19060: Advertised UCI Strength

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name Strength default 

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1323.

```text
me LogFile default -
option name NewSpeech default false
option name WhiteChesscomUsername default 
option name Strength default 
option name SuppressBrilliantSpeech default false
option name SpeechV2 default false
option name BotChatPrioritizePlayerMovePercent default 50
option name BotChatPrioritizePlayerMove default false
option name GamePhaseV2 default true
option name ScoreWhiteToMove default false
option name D
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19061"></a>
## FND-19061: Advertised UCI SuppressBrilliantSpeech

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name SuppressBrilliantSpeech default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1353.

```text
me NewSpeech default false
option name WhiteChesscomUsername default 
option name Strength default 
option name SuppressBrilliantSpeech default false
option name SpeechV2 default false
option name BotChatPrioritizePlayerMovePercent default 50
option name BotChatPrioritizePlayerMove default false
option name GamePhaseV2 default true
option name ScoreWhiteToMove default false
option name DefaultNumNullMoveVariations de
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19062"></a>
## FND-19062: Advertised UCI SpeechV2

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name SpeechV2 default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1403.

```text
omUsername default 
option name Strength default 
option name SuppressBrilliantSpeech default false
option name SpeechV2 default false
option name BotChatPrioritizePlayerMovePercent default 50
option name BotChatPrioritizePlayerMove default false
option name GamePhaseV2 default true
option name ScoreWhiteToMove default false
option name DefaultNumNullMoveVariations default 1
option name PrintCoachTags default false
o
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19063"></a>
## FND-19063: Advertised UCI BotChatPrioritizePlayerMovePercent

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name BotChatPrioritizePlayerMovePercent default 50

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1438.

```text
ength default 
option name SuppressBrilliantSpeech default false
option name SpeechV2 default false
option name BotChatPrioritizePlayerMovePercent default 50
option name BotChatPrioritizePlayerMove default false
option name GamePhaseV2 default true
option name ScoreWhiteToMove default false
option name DefaultNumNullMoveVariations default 1
option name PrintCoachTags default false
option name SerializeLikeCEACV3 defa
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19064"></a>
## FND-19064: Advertised UCI BotChatPrioritizePlayerMove

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name BotChatPrioritizePlayerMove default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1496.

```text
 false
option name SpeechV2 default false
option name BotChatPrioritizePlayerMovePercent default 50
option name BotChatPrioritizePlayerMove default false
option name GamePhaseV2 default true
option name ScoreWhiteToMove default false
option name DefaultNumNullMoveVariations default 1
option name PrintCoachTags default false
option name SerializeLikeCEACV3 default false
option name SpeechV3 default false
option name W
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19065"></a>
## FND-19065: Advertised UCI GamePhaseV2

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name GamePhaseV2 default true

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1550.

```text
BotChatPrioritizePlayerMovePercent default 50
option name BotChatPrioritizePlayerMove default false
option name GamePhaseV2 default true
option name ScoreWhiteToMove default false
option name DefaultNumNullMoveVariations default 1
option name PrintCoachTags default false
option name SerializeLikeCEACV3 default false
option name SpeechV3 default false
option name WhiteElo default 2000
option name DoProgressUpdates def
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19066"></a>
## FND-19066: Advertised UCI ScoreWhiteToMove

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name ScoreWhiteToMove default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1587.

```text
fault 50
option name BotChatPrioritizePlayerMove default false
option name GamePhaseV2 default true
option name ScoreWhiteToMove default false
option name DefaultNumNullMoveVariations default 1
option name PrintCoachTags default false
option name SerializeLikeCEACV3 default false
option name SpeechV3 default false
option name WhiteElo default 2000
option name DoProgressUpdates default false
option name BotChatOnlyAft
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19067"></a>
## FND-19067: Advertised UCI DefaultNumNullMoveVariations

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name DefaultNumNullMoveVariations default 1

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1630.

```text
rMove default false
option name GamePhaseV2 default true
option name ScoreWhiteToMove default false
option name DefaultNumNullMoveVariations default 1
option name PrintCoachTags default false
option name SerializeLikeCEACV3 default false
option name SpeechV3 default false
option name WhiteElo default 2000
option name DoProgressUpdates default false
option name BotChatOnlyAfterBotMove default false
option name AllowTr
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19068"></a>
## FND-19068: Advertised UCI PrintCoachTags

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name PrintCoachTags default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1681.

```text
 true
option name ScoreWhiteToMove default false
option name DefaultNumNullMoveVariations default 1
option name PrintCoachTags default false
option name SerializeLikeCEACV3 default false
option name SpeechV3 default false
option name WhiteElo default 2000
option name DoProgressUpdates default false
option name BotChatOnlyAfterBotMove default false
option name AllowTrickyClassification default false
option name Classi
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19069"></a>
## FND-19069: Advertised UCI SerializeLikeCEACV3

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name SerializeLikeCEACV3 default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1722.

```text
t false
option name DefaultNumNullMoveVariations default 1
option name PrintCoachTags default false
option name SerializeLikeCEACV3 default false
option name SpeechV3 default false
option name WhiteElo default 2000
option name DoProgressUpdates default false
option name BotChatOnlyAfterBotMove default false
option name AllowTrickyClassification default false
option name ClassificationV3 default false
option name Seri
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19070"></a>
## FND-19070: Advertised UCI SpeechV3

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name SpeechV3 default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1768.

```text
ns default 1
option name PrintCoachTags default false
option name SerializeLikeCEACV3 default false
option name SpeechV3 default false
option name WhiteElo default 2000
option name DoProgressUpdates default false
option name BotChatOnlyAfterBotMove default false
option name AllowTrickyClassification default false
option name ClassificationV3 default false
option name SerializeEvals default true
option name SerializeL
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19071"></a>
## FND-19071: Advertised UCI WhiteElo

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name WhiteElo default 2000

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1803.

```text
Tags default false
option name SerializeLikeCEACV3 default false
option name SpeechV3 default false
option name WhiteElo default 2000
option name DoProgressUpdates default false
option name BotChatOnlyAfterBotMove default false
option name AllowTrickyClassification default false
option name ClassificationV3 default false
option name SerializeEvals default true
option name SerializeLikeCEAC default true
option name Au
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19072"></a>
## FND-19072: Advertised UCI DoProgressUpdates

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name DoProgressUpdates default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1837.

```text
ializeLikeCEACV3 default false
option name SpeechV3 default false
option name WhiteElo default 2000
option name DoProgressUpdates default false
option name BotChatOnlyAfterBotMove default false
option name AllowTrickyClassification default false
option name ClassificationV3 default false
option name SerializeEvals default true
option name SerializeLikeCEAC default true
option name AutoDetectTermination default false

```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19073"></a>
## FND-19073: Advertised UCI BotChatOnlyAfterBotMove

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name BotChatOnlyAfterBotMove default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1881.

```text
peechV3 default false
option name WhiteElo default 2000
option name DoProgressUpdates default false
option name BotChatOnlyAfterBotMove default false
option name AllowTrickyClassification default false
option name ClassificationV3 default false
option name SerializeEvals default true
option name SerializeLikeCEAC default true
option name AutoDetectTermination default false
option name SerializeSkills default false
op
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19074"></a>
## FND-19074: Advertised UCI AllowTrickyClassification

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name AllowTrickyClassification default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1931.

```text
 2000
option name DoProgressUpdates default false
option name BotChatOnlyAfterBotMove default false
option name AllowTrickyClassification default false
option name ClassificationV3 default false
option name SerializeEvals default true
option name SerializeLikeCEAC default true
option name AutoDetectTermination default false
option name SerializeSkills default false
option name ServeCommandV2 default false
option name
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19075"></a>
## FND-19075: Advertised UCI ClassificationV3

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name ClassificationV3 default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 1983.

```text
tion name BotChatOnlyAfterBotMove default false
option name AllowTrickyClassification default false
option name ClassificationV3 default false
option name SerializeEvals default true
option name SerializeLikeCEAC default true
option name AutoDetectTermination default false
option name SerializeSkills default false
option name ServeCommandV2 default false
option name Coach default 
option name BlackElo default 2000
op
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19076"></a>
## FND-19076: Advertised UCI SerializeEvals

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name SerializeEvals default true

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2026.

```text
alse
option name AllowTrickyClassification default false
option name ClassificationV3 default false
option name SerializeEvals default true
option name SerializeLikeCEAC default true
option name AutoDetectTermination default false
option name SerializeSkills default false
option name ServeCommandV2 default false
option name Coach default 
option name BlackElo default 2000
option name SerializeBoardEvents default fals
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19077"></a>
## FND-19077: Advertised UCI SerializeLikeCEAC

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name SerializeLikeCEAC default true

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2066.

```text
on default false
option name ClassificationV3 default false
option name SerializeEvals default true
option name SerializeLikeCEAC default true
option name AutoDetectTermination default false
option name SerializeSkills default false
option name ServeCommandV2 default false
option name Coach default 
option name BlackElo default 2000
option name SerializeBoardEvents default false
option name Engine default Torch
optio
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19078"></a>
## FND-19078: Advertised UCI AutoDetectTermination

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name AutoDetectTermination default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2109.

```text
V3 default false
option name SerializeEvals default true
option name SerializeLikeCEAC default true
option name AutoDetectTermination default false
option name SerializeSkills default false
option name ServeCommandV2 default false
option name Coach default 
option name BlackElo default 2000
option name SerializeBoardEvents default false
option name Engine default Torch
option name PersonalSpeechForOpponentMoves defau
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19079"></a>
## FND-19079: Advertised UCI SerializeSkills

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name SerializeSkills default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2157.

```text
ult true
option name SerializeLikeCEAC default true
option name AutoDetectTermination default false
option name SerializeSkills default false
option name ServeCommandV2 default false
option name Coach default 
option name BlackElo default 2000
option name SerializeBoardEvents default false
option name Engine default Torch
option name PersonalSpeechForOpponentMoves default true
option name HandleNullMoveContinuationsD
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19080"></a>
## FND-19080: Advertised UCI ServeCommandV2

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name ServeCommandV2 default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2199.

```text
ault true
option name AutoDetectTermination default false
option name SerializeSkills default false
option name ServeCommandV2 default false
option name Coach default 
option name BlackElo default 2000
option name SerializeBoardEvents default false
option name Engine default Torch
option name PersonalSpeechForOpponentMoves default true
option name HandleNullMoveContinuationsDepth default 12
option name EloSensitivePD
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19081"></a>
## FND-19081: Advertised UCI Coach

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name Coach default 

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2240.

```text
on default false
option name SerializeSkills default false
option name ServeCommandV2 default false
option name Coach default 
option name BlackElo default 2000
option name SerializeBoardEvents default false
option name Engine default Torch
option name PersonalSpeechForOpponentMoves default true
option name HandleNullMoveContinuationsDepth default 12
option name EloSensitivePD default false
option name HandleContinua
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19082"></a>
## FND-19082: Advertised UCI BlackElo

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name BlackElo default 2000

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2267.

```text
e SerializeSkills default false
option name ServeCommandV2 default false
option name Coach default 
option name BlackElo default 2000
option name SerializeBoardEvents default false
option name Engine default Torch
option name PersonalSpeechForOpponentMoves default true
option name HandleNullMoveContinuationsDepth default 12
option name EloSensitivePD default false
option name HandleContinuationsDepth default 12
optio
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19083"></a>
## FND-19083: Advertised UCI SerializeBoardEvents

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name SerializeBoardEvents default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2301.

```text
tion name ServeCommandV2 default false
option name Coach default 
option name BlackElo default 2000
option name SerializeBoardEvents default false
option name Engine default Torch
option name PersonalSpeechForOpponentMoves default true
option name HandleNullMoveContinuationsDepth default 12
option name EloSensitivePD default false
option name HandleContinuationsDepth default 12
option name GetThemes default false
opt
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19084"></a>
## FND-19084: Advertised UCI Engine

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name Engine default Torch

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2348.

```text
ame Coach default 
option name BlackElo default 2000
option name SerializeBoardEvents default false
option name Engine default Torch
option name PersonalSpeechForOpponentMoves default true
option name HandleNullMoveContinuationsDepth default 12
option name EloSensitivePD default false
option name HandleContinuationsDepth default 12
option name GetThemes default false
option name TestMode default false
option name Eva
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19085"></a>
## FND-19085: Advertised UCI PersonalSpeechForOpponentMoves

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name PersonalSpeechForOpponentMoves default true

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2381.

```text
ackElo default 2000
option name SerializeBoardEvents default false
option name Engine default Torch
option name PersonalSpeechForOpponentMoves default true
option name HandleNullMoveContinuationsDepth default 12
option name EloSensitivePD default false
option name HandleContinuationsDepth default 12
option name GetThemes default false
option name TestMode default false
option name EvalSourceEngine default Komodo
opti
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19086"></a>
## FND-19086: Advertised UCI HandleNullMoveContinuationsDepth

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name HandleNullMoveContinuationsDepth default 12

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2437.

```text
ault false
option name Engine default Torch
option name PersonalSpeechForOpponentMoves default true
option name HandleNullMoveContinuationsDepth default 12
option name EloSensitivePD default false
option name HandleContinuationsDepth default 12
option name GetThemes default false
option name TestMode default false
option name EvalSourceEngine default Komodo
option name AllowBoardEventsWithoutSpeech default false
opti
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19087"></a>
## FND-19087: Advertised UCI EloSensitivePD

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name EloSensitivePD default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2493.

```text
PersonalSpeechForOpponentMoves default true
option name HandleNullMoveContinuationsDepth default 12
option name EloSensitivePD default false
option name HandleContinuationsDepth default 12
option name GetThemes default false
option name TestMode default false
option name EvalSourceEngine default Komodo
option name AllowBoardEventsWithoutSpeech default false
option name HandleNullMoveContinuationsNodes default 0
optio
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19088"></a>
## FND-19088: Advertised UCI HandleContinuationsDepth

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name HandleContinuationsDepth default 12

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2534.

```text
ue
option name HandleNullMoveContinuationsDepth default 12
option name EloSensitivePD default false
option name HandleContinuationsDepth default 12
option name GetThemes default false
option name TestMode default false
option name EvalSourceEngine default Komodo
option name AllowBoardEventsWithoutSpeech default false
option name HandleNullMoveContinuationsNodes default 0
option name UseImmediateStop default false
opt
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19089"></a>
## FND-19089: Advertised UCI GetThemes

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name GetThemes default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2582.

```text
default 12
option name EloSensitivePD default false
option name HandleContinuationsDepth default 12
option name GetThemes default false
option name TestMode default false
option name EvalSourceEngine default Komodo
option name AllowBoardEventsWithoutSpeech default false
option name HandleNullMoveContinuationsNodes default 0
option name UseImmediateStop default false
option name IgnoreStopCommand default false
option 
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19090"></a>
## FND-19090: Advertised UCI TestMode

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name TestMode default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2618.

```text
D default false
option name HandleContinuationsDepth default 12
option name GetThemes default false
option name TestMode default false
option name EvalSourceEngine default Komodo
option name AllowBoardEventsWithoutSpeech default false
option name HandleNullMoveContinuationsNodes default 0
option name UseImmediateStop default false
option name IgnoreStopCommand default false
option name HandleContinuationsNodes defaul
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19091"></a>
## FND-19091: Advertised UCI EvalSourceEngine

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name EvalSourceEngine default Komodo

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2653.

```text
ontinuationsDepth default 12
option name GetThemes default false
option name TestMode default false
option name EvalSourceEngine default Komodo
option name AllowBoardEventsWithoutSpeech default false
option name HandleNullMoveContinuationsNodes default 0
option name UseImmediateStop default false
option name IgnoreStopCommand default false
option name HandleContinuationsNodes default 0
option name BlackChesscomUserna
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19092"></a>
## FND-19092: Advertised UCI AllowBoardEventsWithoutSpeech

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name AllowBoardEventsWithoutSpeech default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2697.

```text
Themes default false
option name TestMode default false
option name EvalSourceEngine default Komodo
option name AllowBoardEventsWithoutSpeech default false
option name HandleNullMoveContinuationsNodes default 0
option name UseImmediateStop default false
option name IgnoreStopCommand default false
option name HandleContinuationsNodes default 0
option name BlackChesscomUsername default 
option name HandleCharmInference
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19093"></a>
## FND-19093: Advertised UCI HandleNullMoveContinuationsNodes

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name HandleNullMoveContinuationsNodes default 0

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2753.

```text
option name EvalSourceEngine default Komodo
option name AllowBoardEventsWithoutSpeech default false
option name HandleNullMoveContinuationsNodes default 0
option name UseImmediateStop default false
option name IgnoreStopCommand default false
option name HandleContinuationsNodes default 0
option name BlackChesscomUsername default 
option name HandleCharmInferences default false
option name HandleContinuationsTimeMs de
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19094"></a>
## FND-19094: Advertised UCI UseImmediateStop

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name UseImmediateStop default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2808.

```text
 AllowBoardEventsWithoutSpeech default false
option name HandleNullMoveContinuationsNodes default 0
option name UseImmediateStop default false
option name IgnoreStopCommand default false
option name HandleContinuationsNodes default 0
option name BlackChesscomUsername default 
option name HandleCharmInferences default false
option name HandleContinuationsTimeMs default 0
option name CoachLocale default 
option name De
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19095"></a>
## FND-19095: Advertised UCI IgnoreStopCommand

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name IgnoreStopCommand default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2851.

```text
e
option name HandleNullMoveContinuationsNodes default 0
option name UseImmediateStop default false
option name IgnoreStopCommand default false
option name HandleContinuationsNodes default 0
option name BlackChesscomUsername default 
option name HandleCharmInferences default false
option name HandleContinuationsTimeMs default 0
option name CoachLocale default 
option name DefaultNumVariations default 2
option name Pl
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19096"></a>
## FND-19096: Advertised UCI HandleContinuationsNodes

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name HandleContinuationsNodes default 0

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2895.

```text
es default 0
option name UseImmediateStop default false
option name IgnoreStopCommand default false
option name HandleContinuationsNodes default 0
option name BlackChesscomUsername default 
option name HandleCharmInferences default false
option name HandleContinuationsTimeMs default 0
option name CoachLocale default 
option name DefaultNumVariations default 2
option name PlayVsCoachFlipBoardEnabled default false
opti
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19097"></a>
## FND-19097: Advertised UCI BlackChesscomUsername

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name BlackChesscomUsername default 

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2942.

```text
lt false
option name IgnoreStopCommand default false
option name HandleContinuationsNodes default 0
option name BlackChesscomUsername default 
option name HandleCharmInferences default false
option name HandleContinuationsTimeMs default 0
option name CoachLocale default 
option name DefaultNumVariations default 2
option name PlayVsCoachFlipBoardEnabled default false
option name GameStartedAtMs default 0
option name U
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19098"></a>
## FND-19098: Advertised UCI HandleCharmInferences

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name HandleCharmInferences default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 2985.

```text
ult false
option name HandleContinuationsNodes default 0
option name BlackChesscomUsername default 
option name HandleCharmInferences default false
option name HandleContinuationsTimeMs default 0
option name CoachLocale default 
option name DefaultNumVariations default 2
option name PlayVsCoachFlipBoardEnabled default false
option name GameStartedAtMs default 0
option name UseExplainSpeechType default true
option nam
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19099"></a>
## FND-19099: Advertised UCI HandleContinuationsTimeMs

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name HandleContinuationsTimeMs default 0

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3033.

```text
efault 0
option name BlackChesscomUsername default 
option name HandleCharmInferences default false
option name HandleContinuationsTimeMs default 0
option name CoachLocale default 
option name DefaultNumVariations default 2
option name PlayVsCoachFlipBoardEnabled default false
option name GameStartedAtMs default 0
option name UseExplainSpeechType default true
option name HandleContinuations default false
option name 
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19100"></a>
## FND-19100: Advertised UCI CoachLocale

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name CoachLocale default 

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3081.

```text
lt 
option name HandleCharmInferences default false
option name HandleContinuationsTimeMs default 0
option name CoachLocale default 
option name DefaultNumVariations default 2
option name PlayVsCoachFlipBoardEnabled default false
option name GameStartedAtMs default 0
option name UseExplainSpeechType default true
option name HandleContinuations default false
option name Language default en_US
option name PgnHeadersJso
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19101"></a>
## FND-19101: Advertised UCI DefaultNumVariations

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name DefaultNumVariations default 2

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3114.

```text
nces default false
option name HandleContinuationsTimeMs default 0
option name CoachLocale default 
option name DefaultNumVariations default 2
option name PlayVsCoachFlipBoardEnabled default false
option name GameStartedAtMs default 0
option name UseExplainSpeechType default true
option name HandleContinuations default false
option name Language default en_US
option name PgnHeadersJson default {}
option name HandleNu
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19102"></a>
## FND-19102: Advertised UCI PlayVsCoachFlipBoardEnabled

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name PlayVsCoachFlipBoardEnabled default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3157.

```text
uationsTimeMs default 0
option name CoachLocale default 
option name DefaultNumVariations default 2
option name PlayVsCoachFlipBoardEnabled default false
option name GameStartedAtMs default 0
option name UseExplainSpeechType default true
option name HandleContinuations default false
option name Language default en_US
option name PgnHeadersJson default {}
option name HandleNullMoveContinuationsTimeMs default 0
option 
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19103"></a>
## FND-19103: Advertised UCI GameStartedAtMs

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name GameStartedAtMs default 0

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3211.

```text
t 
option name DefaultNumVariations default 2
option name PlayVsCoachFlipBoardEnabled default false
option name GameStartedAtMs default 0
option name UseExplainSpeechType default true
option name HandleContinuations default false
option name Language default en_US
option name PgnHeadersJson default {}
option name HandleNullMoveContinuationsTimeMs default 0
option name UseDeclarativePositionCommand default false
optio
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19104"></a>
## FND-19104: Advertised UCI UseExplainSpeechType

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name UseExplainSpeechType default true

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3249.

```text
fault 2
option name PlayVsCoachFlipBoardEnabled default false
option name GameStartedAtMs default 0
option name UseExplainSpeechType default true
option name HandleContinuations default false
option name Language default en_US
option name PgnHeadersJson default {}
option name HandleNullMoveContinuationsTimeMs default 0
option name UseDeclarativePositionCommand default false
option name BadKeyMomentsNeedMaterialOrMate
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19105"></a>
## FND-19105: Advertised UCI HandleContinuations

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name HandleContinuations default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3295.

```text
d default false
option name GameStartedAtMs default 0
option name UseExplainSpeechType default true
option name HandleContinuations default false
option name Language default en_US
option name PgnHeadersJson default {}
option name HandleNullMoveContinuationsTimeMs default 0
option name UseDeclarativePositionCommand default false
option name BadKeyMomentsNeedMaterialOrMate default false
option name Result default *
op
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19106"></a>
## FND-19106: Advertised UCI Language

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name Language default en_US

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3341.

```text
fault 0
option name UseExplainSpeechType default true
option name HandleContinuations default false
option name Language default en_US
option name PgnHeadersJson default {}
option name HandleNullMoveContinuationsTimeMs default 0
option name UseDeclarativePositionCommand default false
option name BadKeyMomentsNeedMaterialOrMate default false
option name Result default *
option name InsightsTags default false
info stri
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19107"></a>
## FND-19107: Advertised UCI PgnHeadersJson

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name PgnHeadersJson default {}

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3376.

```text
hType default true
option name HandleContinuations default false
option name Language default en_US
option name PgnHeadersJson default {}
option name HandleNullMoveContinuationsTimeMs default 0
option name UseDeclarativePositionCommand default false
option name BadKeyMomentsNeedMaterialOrMate default false
option name Result default *
option name InsightsTags default false
info string Torch
option name ClearBetweenSe
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19108"></a>
## FND-19108: Advertised UCI HandleNullMoveContinuationsTimeMs

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name HandleNullMoveContinuationsTimeMs default 0

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3414.

```text
ontinuations default false
option name Language default en_US
option name PgnHeadersJson default {}
option name HandleNullMoveContinuationsTimeMs default 0
option name UseDeclarativePositionCommand default false
option name BadKeyMomentsNeedMaterialOrMate default false
option name Result default *
option name InsightsTags default false
info string Torch
option name ClearBetweenSearches type check default false
option
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19109"></a>
## FND-19109: Advertised UCI UseDeclarativePositionCommand

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name UseDeclarativePositionCommand default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3470.

```text
en_US
option name PgnHeadersJson default {}
option name HandleNullMoveContinuationsTimeMs default 0
option name UseDeclarativePositionCommand default false
option name BadKeyMomentsNeedMaterialOrMate default false
option name Result default *
option name InsightsTags default false
info string Torch
option name ClearBetweenSearches type check default false
option name ClearHash type button
option name HardSoftNodeFact
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19110"></a>
## FND-19110: Advertised UCI BadKeyMomentsNeedMaterialOrMate

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name BadKeyMomentsNeedMaterialOrMate default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3526.

```text
HandleNullMoveContinuationsTimeMs default 0
option name UseDeclarativePositionCommand default false
option name BadKeyMomentsNeedMaterialOrMate default false
option name Result default *
option name InsightsTags default false
info string Torch
option name ClearBetweenSearches type check default false
option name ClearHash type button
option name HardSoftNodeFactor type spin default 100 min 1 max 1000
option name Hash
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19111"></a>
## FND-19111: Advertised UCI Result

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name Result default *

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3584.

```text
eDeclarativePositionCommand default false
option name BadKeyMomentsNeedMaterialOrMate default false
option name Result default *
option name InsightsTags default false
info string Torch
option name ClearBetweenSearches type check default false
option name ClearHash type button
option name HardSoftNodeFactor type spin default 100 min 1 max 1000
option name Hash type spin default 16 min 2 max 1048576
option name Minima
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19112"></a>
## FND-19112: Advertised UCI InsightsTags

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name InsightsTags default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3613.

```text
efault false
option name BadKeyMomentsNeedMaterialOrMate default false
option name Result default *
option name InsightsTags default false
info string Torch
option name ClearBetweenSearches type check default false
option name ClearHash type button
option name HardSoftNodeFactor type spin default 100 min 1 max 1000
option name Hash type spin default 16 min 2 max 1048576
option name Minimal type check default false
op
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19113"></a>
## FND-19113: Advertised UCI ClearBetweenSearches

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name ClearBetweenSearches type check default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3670.

```text
default false
option name Result default *
option name InsightsTags default false
info string Torch
option name ClearBetweenSearches type check default false
option name ClearHash type button
option name HardSoftNodeFactor type spin default 100 min 1 max 1000
option name Hash type spin default 16 min 2 max 1048576
option name Minimal type check default false
option name MoveOverhead type spin default 100 min 0 max 50
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19114"></a>
## FND-19114: Advertised UCI ClearHash

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name ClearHash type button

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3728.

```text
ightsTags default false
info string Torch
option name ClearBetweenSearches type check default false
option name ClearHash type button
option name HardSoftNodeFactor type spin default 100 min 1 max 1000
option name Hash type spin default 16 min 2 max 1048576
option name Minimal type check default false
option name MoveOverhead type spin default 100 min 0 max 5000
option name MultiPV type spin default 1 min 1 max 384
o
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19115"></a>
## FND-19115: Advertised UCI HardSoftNodeFactor

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name HardSoftNodeFactor type spin default 100 min 1 max 1000

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3762.

```text
g Torch
option name ClearBetweenSearches type check default false
option name ClearHash type button
option name HardSoftNodeFactor type spin default 100 min 1 max 1000
option name Hash type spin default 16 min 2 max 1048576
option name Minimal type check default false
option name MoveOverhead type spin default 100 min 0 max 5000
option name MultiPV type spin default 1 min 1 max 384
option name NodeFudging type spin d
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19116"></a>
## FND-19116: Advertised UCI Hash

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name Hash type spin default 16 min 2 max 1048576

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3830.

```text
tion name ClearHash type button
option name HardSoftNodeFactor type spin default 100 min 1 max 1000
option name Hash type spin default 16 min 2 max 1048576
option name Minimal type check default false
option name MoveOverhead type spin default 100 min 0 max 5000
option name MultiPV type spin default 1 min 1 max 384
option name NodeFudging type spin default 0 min 0 max 10000
option name Normalize type check default tr
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19117"></a>
## FND-19117: Advertised UCI Minimal

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name Minimal type check default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3886.

```text
Factor type spin default 100 min 1 max 1000
option name Hash type spin default 16 min 2 max 1048576
option name Minimal type check default false
option name MoveOverhead type spin default 100 min 0 max 5000
option name MultiPV type spin default 1 min 1 max 384
option name NodeFudging type spin default 0 min 0 max 10000
option name Normalize type check default true
option name Ponder type check default false
option na
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19118"></a>
## FND-19118: Advertised UCI MoveOverhead

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name MoveOverhead type spin default 100 min 0 max 5000

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3931.

```text
ption name Hash type spin default 16 min 2 max 1048576
option name Minimal type check default false
option name MoveOverhead type spin default 100 min 0 max 5000
option name MultiPV type spin default 1 min 1 max 384
option name NodeFudging type spin default 0 min 0 max 10000
option name Normalize type check default true
option name Ponder type check default false
option name SilenceUCI type check default false
option
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19119"></a>
## FND-19119: Advertised UCI MultiPV

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name MultiPV type spin default 1 min 1 max 384

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 3993.

```text
name Minimal type check default false
option name MoveOverhead type spin default 100 min 0 max 5000
option name MultiPV type spin default 1 min 1 max 384
option name NodeFudging type spin default 0 min 0 max 10000
option name Normalize type check default true
option name Ponder type check default false
option name SilenceUCI type check default false
option name Syzygy50MoveRule type check default false
option name Sy
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19120"></a>
## FND-19120: Advertised UCI NodeFudging

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name NodeFudging type spin default 0 min 0 max 10000

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 4047.

```text
Overhead type spin default 100 min 0 max 5000
option name MultiPV type spin default 1 min 1 max 384
option name NodeFudging type spin default 0 min 0 max 10000
option name Normalize type check default true
option name Ponder type check default false
option name SilenceUCI type check default false
option name Syzygy50MoveRule type check default false
option name SyzygyDTZFiltering type check default true
option name S
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19121"></a>
## FND-19121: Advertised UCI Normalize

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name Normalize type check default true

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 4107.

```text
ltiPV type spin default 1 min 1 max 384
option name NodeFudging type spin default 0 min 0 max 10000
option name Normalize type check default true
option name Ponder type check default false
option name SilenceUCI type check default false
option name Syzygy50MoveRule type check default false
option name SyzygyDTZFiltering type check default true
option name SyzygyPath type string default <empty>
option name SyzygyProb
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19122"></a>
## FND-19122: Advertised UCI Ponder

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name Ponder type check default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 4153.

```text
 name NodeFudging type spin default 0 min 0 max 10000
option name Normalize type check default true
option name Ponder type check default false
option name SilenceUCI type check default false
option name Syzygy50MoveRule type check default false
option name SyzygyDTZFiltering type check default true
option name SyzygyPath type string default <empty>
option name SyzygyProbeDepth type spin default 1 min 1 max 127
optio
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19123"></a>
## FND-19123: Advertised UCI SilenceUCI

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name SilenceUCI type check default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 4197.

```text
max 10000
option name Normalize type check default true
option name Ponder type check default false
option name SilenceUCI type check default false
option name Syzygy50MoveRule type check default false
option name SyzygyDTZFiltering type check default true
option name SyzygyPath type string default <empty>
option name SyzygyProbeDepth type spin default 1 min 1 max 127
option name SyzygyProbeLimit type spin default 7 
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19124"></a>
## FND-19124: Advertised UCI Syzygy50MoveRule

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name Syzygy50MoveRule type check default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 4245.

```text
lt true
option name Ponder type check default false
option name SilenceUCI type check default false
option name Syzygy50MoveRule type check default false
option name SyzygyDTZFiltering type check default true
option name SyzygyPath type string default <empty>
option name SyzygyProbeDepth type spin default 1 min 1 max 127
option name SyzygyProbeLimit type spin default 7 min 1 max 7
option name Threads type spin defaul
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19125"></a>
## FND-19125: Advertised UCI SyzygyDTZFiltering

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name SyzygyDTZFiltering type check default true

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 4299.

```text
tion name SilenceUCI type check default false
option name Syzygy50MoveRule type check default false
option name SyzygyDTZFiltering type check default true
option name SyzygyPath type string default <empty>
option name SyzygyProbeDepth type spin default 1 min 1 max 127
option name SyzygyProbeLimit type spin default 7 min 1 max 7
option name Threads type spin default 1 min 1 max 1
option name UCI_Chess960 type check de
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19126"></a>
## FND-19126: Advertised UCI SyzygyPath

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name SyzygyPath type string default <empty>

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 4354.

```text
me Syzygy50MoveRule type check default false
option name SyzygyDTZFiltering type check default true
option name SyzygyPath type string default <empty>
option name SyzygyProbeDepth type spin default 1 min 1 max 127
option name SyzygyProbeLimit type spin default 7 min 1 max 7
option name Threads type spin default 1 min 1 max 1
option name UCI_Chess960 type check default false
option name UseSoftNodes type check default
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19127"></a>
## FND-19127: Advertised UCI SyzygyProbeDepth

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name SyzygyProbeDepth type spin default 1 min 1 max 127

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 4405.

```text
 name SyzygyDTZFiltering type check default true
option name SyzygyPath type string default <empty>
option name SyzygyProbeDepth type spin default 1 min 1 max 127
option name SyzygyProbeLimit type spin default 7 min 1 max 7
option name Threads type spin default 1 min 1 max 1
option name UCI_Chess960 type check default false
option name UseSoftNodes type check default false
uciok
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19128"></a>
## FND-19128: Advertised UCI SyzygyProbeLimit

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name SyzygyProbeLimit type spin default 7 min 1 max 7

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 4468.

```text
zygyPath type string default <empty>
option name SyzygyProbeDepth type spin default 1 min 1 max 127
option name SyzygyProbeLimit type spin default 7 min 1 max 7
option name Threads type spin default 1 min 1 max 1
option name UCI_Chess960 type check default false
option name UseSoftNodes type check default false
uciok
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19129"></a>
## FND-19129: Advertised UCI Threads

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name Threads type spin default 1 min 1 max 1

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 4529.

```text
epth type spin default 1 min 1 max 127
option name SyzygyProbeLimit type spin default 7 min 1 max 7
option name Threads type spin default 1 min 1 max 1
option name UCI_Chess960 type check default false
option name UseSoftNodes type check default false
uciok
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
