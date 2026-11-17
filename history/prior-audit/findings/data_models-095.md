# data_models — findings 9401–9500

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-09675"></a>
## FND-09675: chesscom.user_properties.v1.Properties.clubs = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.ClubsProperty clubs = 27;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3143.

```text
chesscom.user_properties.v1.PuzzlesAttemptedProperty puzzles_attempted = 26;
  }
  oneof _clubs {
  .chesscom.user_properties.v1.ClubsProperty clubs = 27;
  }
  oneof _puzzle_battle {
  .chesscom.user_properties.v1.PuzzleBattleProperty puzzle_battle = 28;
  }
  oneof _audiences {
  .chesscom.user_properties.v1.AudiencesProperty audiences = 29;
  }
  oneof _user_abuse {
  .chesscom.user_properties.v1.UserAbuseProperty
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09676"></a>
## FND-09676: oneof declaration: chesscom.user_properties.v1.Properties._puzzle_battle

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzle_battle {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3204.

```text
attempted = 26;
  }
  oneof _clubs {
  .chesscom.user_properties.v1.ClubsProperty clubs = 27;
  }
  oneof _puzzle_battle {
  .chesscom.user_properties.v1.PuzzleBattleProperty puzzle_battle = 28;
  }
  oneof _audiences {
  .chesscom.user_properties.v1.AudiencesProperty audiences = 29;
  }
  oneof _user_abuse {
  .chesscom.user_properties.v1.UserAbuseProperty user_abuse = 30;
  }
  oneof _daily_puzzles_solved {
  .ches
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09677"></a>
## FND-09677: chesscom.user_properties.v1.Properties.puzzle_battle = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PuzzleBattleProperty puzzle_battle = 28;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3229.

```text
of _clubs {
  .chesscom.user_properties.v1.ClubsProperty clubs = 27;
  }
  oneof _puzzle_battle {
  .chesscom.user_properties.v1.PuzzleBattleProperty puzzle_battle = 28;
  }
  oneof _audiences {
  .chesscom.user_properties.v1.AudiencesProperty audiences = 29;
  }
  oneof _user_abuse {
  .chesscom.user_properties.v1.UserAbuseProperty user_abuse = 30;
  }
  oneof _daily_puzzles_solved {
  .chesscom.user_properties.v1.D
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09678"></a>
## FND-09678: oneof declaration: chesscom.user_properties.v1.Properties._audiences

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _audiences {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3305.

```text
neof _puzzle_battle {
  .chesscom.user_properties.v1.PuzzleBattleProperty puzzle_battle = 28;
  }
  oneof _audiences {
  .chesscom.user_properties.v1.AudiencesProperty audiences = 29;
  }
  oneof _user_abuse {
  .chesscom.user_properties.v1.UserAbuseProperty user_abuse = 30;
  }
  oneof _daily_puzzles_solved {
  .chesscom.user_properties.v1.DailyPuzzlesSolvedProperty daily_puzzles_solved = 32;
  }
  oneof _play_bulle
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09679"></a>
## FND-09679: chesscom.user_properties.v1.Properties.audiences = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AudiencesProperty audiences = 29;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3326.

```text

  .chesscom.user_properties.v1.PuzzleBattleProperty puzzle_battle = 28;
  }
  oneof _audiences {
  .chesscom.user_properties.v1.AudiencesProperty audiences = 29;
  }
  oneof _user_abuse {
  .chesscom.user_properties.v1.UserAbuseProperty user_abuse = 30;
  }
  oneof _daily_puzzles_solved {
  .chesscom.user_properties.v1.DailyPuzzlesSolvedProperty daily_puzzles_solved = 32;
  }
  oneof _play_bullet_chess {
  .chesscom
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09680"></a>
## FND-09680: oneof declaration: chesscom.user_properties.v1.Properties._user_abuse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_abuse {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3395.

```text
28;
  }
  oneof _audiences {
  .chesscom.user_properties.v1.AudiencesProperty audiences = 29;
  }
  oneof _user_abuse {
  .chesscom.user_properties.v1.UserAbuseProperty user_abuse = 30;
  }
  oneof _daily_puzzles_solved {
  .chesscom.user_properties.v1.DailyPuzzlesSolvedProperty daily_puzzles_solved = 32;
  }
  oneof _play_bullet_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess = 33;
  }
  o
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09681"></a>
## FND-09681: chesscom.user_properties.v1.Properties.user_abuse = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.UserAbuseProperty user_abuse = 30;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3417.

```text
nces {
  .chesscom.user_properties.v1.AudiencesProperty audiences = 29;
  }
  oneof _user_abuse {
  .chesscom.user_properties.v1.UserAbuseProperty user_abuse = 30;
  }
  oneof _daily_puzzles_solved {
  .chesscom.user_properties.v1.DailyPuzzlesSolvedProperty daily_puzzles_solved = 32;
  }
  oneof _play_bullet_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess = 33;
  }
  oneof _play_bullet_ches
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09682"></a>
## FND-09682: oneof declaration: chesscom.user_properties.v1.Properties._daily_puzzles_solved

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _daily_puzzles_solved {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3487.

```text
;
  }
  oneof _user_abuse {
  .chesscom.user_properties.v1.UserAbuseProperty user_abuse = 30;
  }
  oneof _daily_puzzles_solved {
  .chesscom.user_properties.v1.DailyPuzzlesSolvedProperty daily_puzzles_solved = 32;
  }
  oneof _play_bullet_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess = 33;
  }
  oneof _play_bullet_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_ch
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09683"></a>
## FND-09683: chesscom.user_properties.v1.Properties.daily_puzzles_solved = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.DailyPuzzlesSolvedProperty daily_puzzles_solved = 32;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3519.

```text
hesscom.user_properties.v1.UserAbuseProperty user_abuse = 30;
  }
  oneof _daily_puzzles_solved {
  .chesscom.user_properties.v1.DailyPuzzlesSolvedProperty daily_puzzles_solved = 32;
  }
  oneof _play_bullet_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess = 33;
  }
  oneof _play_bullet_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess960 = 34;
  }
  oneof _play_b
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09684"></a>
## FND-09684: oneof declaration: chesscom.user_properties.v1.Properties._play_bullet_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_bullet_chess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3608.

```text
solved {
  .chesscom.user_properties.v1.DailyPuzzlesSolvedProperty daily_puzzles_solved = 32;
  }
  oneof _play_bullet_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess = 33;
  }
  oneof _play_bullet_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess960 = 34;
  }
  oneof _play_bullet_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_bughouse = 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09685"></a>
## FND-09685: chesscom.user_properties.v1.Properties.play_bullet_chess = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess = 33;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3637.

```text
perties.v1.DailyPuzzlesSolvedProperty daily_puzzles_solved = 32;
  }
  oneof _play_bullet_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess = 33;
  }
  oneof _play_bullet_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess960 = 34;
  }
  oneof _play_bullet_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_bughouse = 35;
  }
  oneof _play_bullet_
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09686"></a>
## FND-09686: oneof declaration: chesscom.user_properties.v1.Properties._play_bullet_chess960

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_bullet_chess960 {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3714.

```text
_play_bullet_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess = 33;
  }
  oneof _play_bullet_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess960 = 34;
  }
  oneof _play_bullet_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_bughouse = 35;
  }
  oneof _play_bullet_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_thr
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09687"></a>
## FND-09687: chesscom.user_properties.v1.Properties.play_bullet_chess960 = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess960 = 34;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3746.

```text
.user_properties.v1.PlayStatsProperty play_bullet_chess = 33;
  }
  oneof _play_bullet_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess960 = 34;
  }
  oneof _play_bullet_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_bughouse = 35;
  }
  oneof _play_bullet_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_threecheck = 36;
  }
  oneof _play_
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09688"></a>
## FND-09688: oneof declaration: chesscom.user_properties.v1.Properties._play_bullet_bughouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_bullet_bughouse {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3826.

```text
bullet_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_chess960 = 34;
  }
  oneof _play_bullet_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_bughouse = 35;
  }
  oneof _play_bullet_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_threecheck = 36;
  }
  oneof _play_bullet_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09689"></a>
## FND-09689: chesscom.user_properties.v1.Properties.play_bullet_bughouse = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_bullet_bughouse = 35;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3858.

```text
er_properties.v1.PlayStatsProperty play_bullet_chess960 = 34;
  }
  oneof _play_bullet_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_bughouse = 35;
  }
  oneof _play_bullet_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_threecheck = 36;
  }
  oneof _play_bullet_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_crazyhouse = 37;
  }
  oneof _p
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09690"></a>
## FND-09690: oneof declaration: chesscom.user_properties.v1.Properties._play_bullet_threecheck

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_bullet_threecheck {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3938.

```text
bullet_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_bughouse = 35;
  }
  oneof _play_bullet_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_threecheck = 36;
  }
  oneof _play_bullet_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_crazyhouse = 37;
  }
  oneof _play_bullet_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09691"></a>
## FND-09691: chesscom.user_properties.v1.Properties.play_bullet_threecheck = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_bullet_threecheck = 36;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3972.

```text
_properties.v1.PlayStatsProperty play_bullet_bughouse = 35;
  }
  oneof _play_bullet_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_threecheck = 36;
  }
  oneof _play_bullet_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_crazyhouse = 37;
  }
  oneof _play_bullet_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_kingofthehill = 38;
  }
  
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09692"></a>
## FND-09692: oneof declaration: chesscom.user_properties.v1.Properties._play_bullet_crazyhouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_bullet_crazyhouse {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4054.

```text
et_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_threecheck = 36;
  }
  oneof _play_bullet_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_crazyhouse = 37;
  }
  oneof _play_bullet_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_kingofthehill = 38;
  }
  oneof _play_bullet_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty pl
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09693"></a>
## FND-09693: chesscom.user_properties.v1.Properties.play_bullet_crazyhouse = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_bullet_crazyhouse = 37;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4088.

```text
roperties.v1.PlayStatsProperty play_bullet_threecheck = 36;
  }
  oneof _play_bullet_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_crazyhouse = 37;
  }
  oneof _play_bullet_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_kingofthehill = 38;
  }
  oneof _play_bullet_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_oddschess = 39;
  }
  on
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09694"></a>
## FND-09694: oneof declaration: chesscom.user_properties.v1.Properties._play_bullet_kingofthehill

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_bullet_kingofthehill {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4170.

```text
et_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_crazyhouse = 37;
  }
  oneof _play_bullet_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_kingofthehill = 38;
  }
  oneof _play_bullet_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_oddschess = 39;
  }
  oneof _play_blitz_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_blit
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09695"></a>
## FND-09695: chesscom.user_properties.v1.Properties.play_bullet_kingofthehill = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_bullet_kingofthehill = 38;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4207.

```text
erties.v1.PlayStatsProperty play_bullet_crazyhouse = 37;
  }
  oneof _play_bullet_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_kingofthehill = 38;
  }
  oneof _play_bullet_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_oddschess = 39;
  }
  oneof _play_blitz_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess = 40;
  }
  oneof _play_blitz
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09696"></a>
## FND-09696: oneof declaration: chesscom.user_properties.v1.Properties._play_bullet_oddschess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_bullet_oddschess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4292.

```text
gofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_kingofthehill = 38;
  }
  oneof _play_bullet_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_oddschess = 39;
  }
  oneof _play_blitz_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess = 40;
  }
  oneof _play_blitz_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess960 = 41
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09697"></a>
## FND-09697: chesscom.user_properties.v1.Properties.play_bullet_oddschess = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_bullet_oddschess = 39;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4325.

```text
perties.v1.PlayStatsProperty play_bullet_kingofthehill = 38;
  }
  oneof _play_bullet_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_oddschess = 39;
  }
  oneof _play_blitz_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess = 40;
  }
  oneof _play_blitz_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess960 = 41;
  }
  oneof _play_blitz_bughous
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09698"></a>
## FND-09698: oneof declaration: chesscom.user_properties.v1.Properties._play_blitz_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_blitz_chess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4406.

```text
llet_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_bullet_oddschess = 39;
  }
  oneof _play_blitz_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess = 40;
  }
  oneof _play_blitz_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess960 = 41;
  }
  oneof _play_blitz_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_bughouse = 42;
  
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09699"></a>
## FND-09699: chesscom.user_properties.v1.Properties.play_blitz_chess = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess = 40;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4434.

```text
.user_properties.v1.PlayStatsProperty play_bullet_oddschess = 39;
  }
  oneof _play_blitz_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess = 40;
  }
  oneof _play_blitz_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess960 = 41;
  }
  oneof _play_blitz_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_bughouse = 42;
  }
  oneof _play_blitz_threec
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09700"></a>
## FND-09700: oneof declaration: chesscom.user_properties.v1.Properties._play_blitz_chess960

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_blitz_chess960 {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4510.

```text
f _play_blitz_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess = 40;
  }
  oneof _play_blitz_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess960 = 41;
  }
  oneof _play_blitz_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_bughouse = 42;
  }
  oneof _play_blitz_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_threechec
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09701"></a>
## FND-09701: chesscom.user_properties.v1.Properties.play_blitz_chess960 = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess960 = 41;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4541.

```text
om.user_properties.v1.PlayStatsProperty play_blitz_chess = 40;
  }
  oneof _play_blitz_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess960 = 41;
  }
  oneof _play_blitz_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_bughouse = 42;
  }
  oneof _play_blitz_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_threecheck = 43;
  }
  oneof _play_blitz
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09702"></a>
## FND-09702: oneof declaration: chesscom.user_properties.v1.Properties._play_blitz_bughouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_blitz_bughouse {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4620.

```text
y_blitz_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_chess960 = 41;
  }
  oneof _play_blitz_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_bughouse = 42;
  }
  oneof _play_blitz_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_threecheck = 43;
  }
  oneof _play_blitz_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_crazy
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09703"></a>
## FND-09703: chesscom.user_properties.v1.Properties.play_blitz_bughouse = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_blitz_bughouse = 42;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4651.

```text
user_properties.v1.PlayStatsProperty play_blitz_chess960 = 41;
  }
  oneof _play_blitz_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_bughouse = 42;
  }
  oneof _play_blitz_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_threecheck = 43;
  }
  oneof _play_blitz_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_crazyhouse = 44;
  }
  oneof _play_b
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09704"></a>
## FND-09704: oneof declaration: chesscom.user_properties.v1.Properties._play_blitz_threecheck

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_blitz_threecheck {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4730.

```text
y_blitz_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_bughouse = 42;
  }
  oneof _play_blitz_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_threecheck = 43;
  }
  oneof _play_blitz_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_crazyhouse = 44;
  }
  oneof _play_blitz_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_blit
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09705"></a>
## FND-09705: chesscom.user_properties.v1.Properties.play_blitz_threecheck = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_blitz_threecheck = 43;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4763.

```text
er_properties.v1.PlayStatsProperty play_blitz_bughouse = 42;
  }
  oneof _play_blitz_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_threecheck = 43;
  }
  oneof _play_blitz_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_crazyhouse = 44;
  }
  oneof _play_blitz_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_kingofthehill = 45;
  }
  oneof
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09706"></a>
## FND-09706: oneof declaration: chesscom.user_properties.v1.Properties._play_blitz_crazyhouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_blitz_crazyhouse {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4844.

```text
itz_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_threecheck = 43;
  }
  oneof _play_blitz_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_crazyhouse = 44;
  }
  oneof _play_blitz_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_kingofthehill = 45;
  }
  oneof _play_blitz_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_bl
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09707"></a>
## FND-09707: chesscom.user_properties.v1.Properties.play_blitz_crazyhouse = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_blitz_crazyhouse = 44;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4877.

```text
_properties.v1.PlayStatsProperty play_blitz_threecheck = 43;
  }
  oneof _play_blitz_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_crazyhouse = 44;
  }
  oneof _play_blitz_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_kingofthehill = 45;
  }
  oneof _play_blitz_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_oddschess = 46;
  }
  oneof _
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09708"></a>
## FND-09708: oneof declaration: chesscom.user_properties.v1.Properties._play_blitz_kingofthehill

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_blitz_kingofthehill {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4958.

```text
itz_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_crazyhouse = 44;
  }
  oneof _play_blitz_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_kingofthehill = 45;
  }
  oneof _play_blitz_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_oddschess = 46;
  }
  oneof _play_rapid_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_ch
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09709"></a>
## FND-09709: chesscom.user_properties.v1.Properties.play_blitz_kingofthehill = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_blitz_kingofthehill = 45;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 4994.

```text
operties.v1.PlayStatsProperty play_blitz_crazyhouse = 44;
  }
  oneof _play_blitz_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_kingofthehill = 45;
  }
  oneof _play_blitz_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_oddschess = 46;
  }
  oneof _play_rapid_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess = 47;
  }
  oneof _play_rapid_ch
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09710"></a>
## FND-09710: oneof declaration: chesscom.user_properties.v1.Properties._play_blitz_oddschess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_blitz_oddschess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5078.

```text
ngofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_kingofthehill = 45;
  }
  oneof _play_blitz_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_oddschess = 46;
  }
  oneof _play_rapid_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess = 47;
  }
  oneof _play_rapid_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess960 = 48;

```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09711"></a>
## FND-09711: chesscom.user_properties.v1.Properties.play_blitz_oddschess = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_blitz_oddschess = 46;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5110.

```text
roperties.v1.PlayStatsProperty play_blitz_kingofthehill = 45;
  }
  oneof _play_blitz_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_oddschess = 46;
  }
  oneof _play_rapid_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess = 47;
  }
  oneof _play_rapid_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess960 = 48;
  }
  oneof _play_rapid_bughouse
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09712"></a>
## FND-09712: oneof declaration: chesscom.user_properties.v1.Properties._play_rapid_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_rapid_chess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5190.

```text
blitz_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_blitz_oddschess = 46;
  }
  oneof _play_rapid_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess = 47;
  }
  oneof _play_rapid_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess960 = 48;
  }
  oneof _play_rapid_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_bughouse = 49;
  
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09713"></a>
## FND-09713: chesscom.user_properties.v1.Properties.play_rapid_chess = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess = 47;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5218.

```text
m.user_properties.v1.PlayStatsProperty play_blitz_oddschess = 46;
  }
  oneof _play_rapid_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess = 47;
  }
  oneof _play_rapid_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess960 = 48;
  }
  oneof _play_rapid_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_bughouse = 49;
  }
  oneof _play_rapid_threec
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09714"></a>
## FND-09714: oneof declaration: chesscom.user_properties.v1.Properties._play_rapid_chess960

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_rapid_chess960 {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5294.

```text
f _play_rapid_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess = 47;
  }
  oneof _play_rapid_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess960 = 48;
  }
  oneof _play_rapid_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_bughouse = 49;
  }
  oneof _play_rapid_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_threechec
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09715"></a>
## FND-09715: chesscom.user_properties.v1.Properties.play_rapid_chess960 = 48

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess960 = 48;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5325.

```text
om.user_properties.v1.PlayStatsProperty play_rapid_chess = 47;
  }
  oneof _play_rapid_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess960 = 48;
  }
  oneof _play_rapid_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_bughouse = 49;
  }
  oneof _play_rapid_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_threecheck = 50;
  }
  oneof _play_rapid
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09716"></a>
## FND-09716: oneof declaration: chesscom.user_properties.v1.Properties._play_rapid_bughouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_rapid_bughouse {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5404.

```text
y_rapid_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_chess960 = 48;
  }
  oneof _play_rapid_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_bughouse = 49;
  }
  oneof _play_rapid_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_threecheck = 50;
  }
  oneof _play_rapid_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_crazy
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09717"></a>
## FND-09717: chesscom.user_properties.v1.Properties.play_rapid_bughouse = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_rapid_bughouse = 49;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5435.

```text
user_properties.v1.PlayStatsProperty play_rapid_chess960 = 48;
  }
  oneof _play_rapid_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_bughouse = 49;
  }
  oneof _play_rapid_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_threecheck = 50;
  }
  oneof _play_rapid_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_crazyhouse = 51;
  }
  oneof _play_r
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09718"></a>
## FND-09718: oneof declaration: chesscom.user_properties.v1.Properties._play_rapid_threecheck

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_rapid_threecheck {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5514.

```text
y_rapid_bughouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_bughouse = 49;
  }
  oneof _play_rapid_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_threecheck = 50;
  }
  oneof _play_rapid_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_crazyhouse = 51;
  }
  oneof _play_rapid_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapi
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09719"></a>
## FND-09719: chesscom.user_properties.v1.Properties.play_rapid_threecheck = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_rapid_threecheck = 50;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5547.

```text
er_properties.v1.PlayStatsProperty play_rapid_bughouse = 49;
  }
  oneof _play_rapid_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_threecheck = 50;
  }
  oneof _play_rapid_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_crazyhouse = 51;
  }
  oneof _play_rapid_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_kingofthehill = 52;
  }
  oneof
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09720"></a>
## FND-09720: oneof declaration: chesscom.user_properties.v1.Properties._play_rapid_crazyhouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_rapid_crazyhouse {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5628.

```text
pid_threecheck {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_threecheck = 50;
  }
  oneof _play_rapid_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_crazyhouse = 51;
  }
  oneof _play_rapid_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_kingofthehill = 52;
  }
  oneof _play_rapid_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_ra
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09721"></a>
## FND-09721: chesscom.user_properties.v1.Properties.play_rapid_crazyhouse = 51

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_rapid_crazyhouse = 51;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5661.

```text
_properties.v1.PlayStatsProperty play_rapid_threecheck = 50;
  }
  oneof _play_rapid_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_crazyhouse = 51;
  }
  oneof _play_rapid_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_kingofthehill = 52;
  }
  oneof _play_rapid_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_oddschess = 53;
  }
  oneof _
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09722"></a>
## FND-09722: oneof declaration: chesscom.user_properties.v1.Properties._play_rapid_kingofthehill

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_rapid_kingofthehill {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5742.

```text
pid_crazyhouse {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_crazyhouse = 51;
  }
  oneof _play_rapid_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_kingofthehill = 52;
  }
  oneof _play_rapid_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_oddschess = 53;
  }
  oneof _play_daily_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_ch
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09723"></a>
## FND-09723: chesscom.user_properties.v1.Properties.play_rapid_kingofthehill = 52

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_rapid_kingofthehill = 52;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5778.

```text
operties.v1.PlayStatsProperty play_rapid_crazyhouse = 51;
  }
  oneof _play_rapid_kingofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_kingofthehill = 52;
  }
  oneof _play_rapid_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_oddschess = 53;
  }
  oneof _play_daily_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_chess = 54;
  }
  oneof _play_daily_ch
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09724"></a>
## FND-09724: oneof declaration: chesscom.user_properties.v1.Properties._play_rapid_oddschess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_rapid_oddschess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5862.

```text
ngofthehill {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_kingofthehill = 52;
  }
  oneof _play_rapid_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_oddschess = 53;
  }
  oneof _play_daily_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_chess = 54;
  }
  oneof _play_daily_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_chess960 = 55;

```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09725"></a>
## FND-09725: chesscom.user_properties.v1.Properties.play_rapid_oddschess = 53

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_rapid_oddschess = 53;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5894.

```text
roperties.v1.PlayStatsProperty play_rapid_kingofthehill = 52;
  }
  oneof _play_rapid_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_oddschess = 53;
  }
  oneof _play_daily_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_chess = 54;
  }
  oneof _play_daily_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_chess960 = 55;
  }
  oneof _play_daily_oddsches
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09726"></a>
## FND-09726: oneof declaration: chesscom.user_properties.v1.Properties._play_daily_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_daily_chess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 5974.

```text
rapid_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_rapid_oddschess = 53;
  }
  oneof _play_daily_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_chess = 54;
  }
  oneof _play_daily_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_chess960 = 55;
  }
  oneof _play_daily_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_oddschess = 56;

```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09727"></a>
## FND-09727: chesscom.user_properties.v1.Properties.play_daily_chess = 54

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_daily_chess = 54;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6002.

```text
m.user_properties.v1.PlayStatsProperty play_rapid_oddschess = 53;
  }
  oneof _play_daily_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_chess = 54;
  }
  oneof _play_daily_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_chess960 = 55;
  }
  oneof _play_daily_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_oddschess = 56;
  }
  oneof _tournament_bull
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09728"></a>
## FND-09728: oneof declaration: chesscom.user_properties.v1.Properties._play_daily_chess960

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_daily_chess960 {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6078.

```text
f _play_daily_chess {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_chess = 54;
  }
  oneof _play_daily_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_chess960 = 55;
  }
  oneof _play_daily_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_oddschess = 56;
  }
  oneof _tournament_bullet_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09729"></a>
## FND-09729: chesscom.user_properties.v1.Properties.play_daily_chess960 = 55

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_daily_chess960 = 55;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6109.

```text
om.user_properties.v1.PlayStatsProperty play_daily_chess = 54;
  }
  oneof _play_daily_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_chess960 = 55;
  }
  oneof _play_daily_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_oddschess = 56;
  }
  oneof _tournament_bullet_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_chess = 57;
  }
  oneof
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09730"></a>
## FND-09730: oneof declaration: chesscom.user_properties.v1.Properties._play_daily_oddschess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_daily_oddschess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6188.

```text
y_daily_chess960 {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_chess960 = 55;
  }
  oneof _play_daily_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_oddschess = 56;
  }
  oneof _tournament_bullet_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_chess = 57;
  }
  oneof _tournament_bullet_chess960 {
  .chesscom.user_properties.v1.TournamentStatsPr
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09731"></a>
## FND-09731: chesscom.user_properties.v1.Properties.play_daily_oddschess = 56

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsProperty play_daily_oddschess = 56;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6220.

```text
ser_properties.v1.PlayStatsProperty play_daily_chess960 = 55;
  }
  oneof _play_daily_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_oddschess = 56;
  }
  oneof _tournament_bullet_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_chess = 57;
  }
  oneof _tournament_bullet_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_chess96
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09732"></a>
## FND-09732: oneof declaration: chesscom.user_properties.v1.Properties._tournament_bullet_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_bullet_chess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6300.

```text
daily_oddschess {
  .chesscom.user_properties.v1.PlayStatsProperty play_daily_oddschess = 56;
  }
  oneof _tournament_bullet_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_chess = 57;
  }
  oneof _tournament_bullet_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_chess960 = 58;
  }
  oneof _tournament_bullet_bughouse {
  .chesscom.user_properties.v1
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09733"></a>
## FND-09733: chesscom.user_properties.v1.Properties.tournament_bullet_chess = 57

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_chess = 57;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6335.

```text
properties.v1.PlayStatsProperty play_daily_oddschess = 56;
  }
  oneof _tournament_bullet_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_chess = 57;
  }
  oneof _tournament_bullet_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_chess960 = 58;
  }
  oneof _tournament_bullet_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09734"></a>
## FND-09734: oneof declaration: chesscom.user_properties.v1.Properties._tournament_bullet_chess960

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_bullet_chess960 {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6424.

```text
_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_chess = 57;
  }
  oneof _tournament_bullet_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_chess960 = 58;
  }
  oneof _tournament_bullet_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_bughouse = 59;
  }
  oneof _tournament_bullet_threecheck {
  .chesscom.user_prope
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09735"></a>
## FND-09735: chesscom.user_properties.v1.Properties.tournament_bullet_chess960 = 58

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_chess960 = 58;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6462.

```text
1.TournamentStatsProperty tournament_bullet_chess = 57;
  }
  oneof _tournament_bullet_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_chess960 = 58;
  }
  oneof _tournament_bullet_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_bughouse = 59;
  }
  oneof _tournament_bullet_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tourn
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09736"></a>
## FND-09736: oneof declaration: chesscom.user_properties.v1.Properties._tournament_bullet_bughouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_bullet_bughouse {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6554.

```text
960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_chess960 = 58;
  }
  oneof _tournament_bullet_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_bughouse = 59;
  }
  oneof _tournament_bullet_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_threecheck = 60;
  }
  oneof _tournament_bullet_crazyhouse {
  .chesscom.user_p
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09737"></a>
## FND-09737: chesscom.user_properties.v1.Properties.tournament_bullet_bughouse = 59

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_bughouse = 59;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6592.

```text
ournamentStatsProperty tournament_bullet_chess960 = 58;
  }
  oneof _tournament_bullet_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_bughouse = 59;
  }
  oneof _tournament_bullet_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_threecheck = 60;
  }
  oneof _tournament_bullet_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty t
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09738"></a>
## FND-09738: oneof declaration: chesscom.user_properties.v1.Properties._tournament_bullet_threecheck

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_bullet_threecheck {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6684.

```text
use {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_bughouse = 59;
  }
  oneof _tournament_bullet_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_threecheck = 60;
  }
  oneof _tournament_bullet_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_crazyhouse = 61;
  }
  oneof _tournament_bullet_kingofthehill {
  .chesscom
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09739"></a>
## FND-09739: chesscom.user_properties.v1.Properties.tournament_bullet_threecheck = 60

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_threecheck = 60;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6724.

```text
rnamentStatsProperty tournament_bullet_bughouse = 59;
  }
  oneof _tournament_bullet_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_threecheck = 60;
  }
  oneof _tournament_bullet_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_crazyhouse = 61;
  }
  oneof _tournament_bullet_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsPrope
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09740"></a>
## FND-09740: oneof declaration: chesscom.user_properties.v1.Properties._tournament_bullet_crazyhouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_bullet_crazyhouse {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6818.

```text
k {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_threecheck = 60;
  }
  oneof _tournament_bullet_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_crazyhouse = 61;
  }
  oneof _tournament_bullet_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_kingofthehill = 62;
  }
  oneof _tournament_bullet_oddschess {
  .chessc
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09741"></a>
## FND-09741: chesscom.user_properties.v1.Properties.tournament_bullet_crazyhouse = 61

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_crazyhouse = 61;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6858.

```text
amentStatsProperty tournament_bullet_threecheck = 60;
  }
  oneof _tournament_bullet_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_crazyhouse = 61;
  }
  oneof _tournament_bullet_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_kingofthehill = 62;
  }
  oneof _tournament_bullet_oddschess {
  .chesscom.user_properties.v1.TournamentStatsPro
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09742"></a>
## FND-09742: oneof declaration: chesscom.user_properties.v1.Properties._tournament_bullet_kingofthehill

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_bullet_kingofthehill {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6952.

```text
e {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_crazyhouse = 61;
  }
  oneof _tournament_bullet_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_kingofthehill = 62;
  }
  oneof _tournament_bullet_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_oddschess = 63;
  }
  oneof _tournament_blitz_chess {
  .chesscom.user
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09743"></a>
## FND-09743: chesscom.user_properties.v1.Properties.tournament_bullet_kingofthehill = 62

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_kingofthehill = 62;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 6995.

```text
ntStatsProperty tournament_bullet_crazyhouse = 61;
  }
  oneof _tournament_bullet_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_kingofthehill = 62;
  }
  oneof _tournament_bullet_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_oddschess = 63;
  }
  oneof _tournament_blitz_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tour
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09744"></a>
## FND-09744: oneof declaration: chesscom.user_properties.v1.Properties._tournament_bullet_oddschess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_bullet_oddschess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 7092.

```text

  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_kingofthehill = 62;
  }
  oneof _tournament_bullet_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_oddschess = 63;
  }
  oneof _tournament_blitz_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_chess = 64;
  }
  oneof _tournament_blitz_chess960 {
  .chesscom.user_properties.v1.
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09745"></a>
## FND-09745: chesscom.user_properties.v1.Properties.tournament_bullet_oddschess = 63

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_oddschess = 63;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 7131.

```text
entStatsProperty tournament_bullet_kingofthehill = 62;
  }
  oneof _tournament_bullet_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_oddschess = 63;
  }
  oneof _tournament_blitz_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_chess = 64;
  }
  oneof _tournament_blitz_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blit
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09746"></a>
## FND-09746: oneof declaration: chesscom.user_properties.v1.Properties._tournament_blitz_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_blitz_chess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 7224.

```text
ss {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bullet_oddschess = 63;
  }
  oneof _tournament_blitz_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_chess = 64;
  }
  oneof _tournament_blitz_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_chess960 = 65;
  }
  oneof _tournament_blitz_bughouse {
  .chesscom.user_properties.v1.Tour
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09747"></a>
## FND-09747: chesscom.user_properties.v1.Properties.tournament_blitz_chess = 64

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_chess = 64;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 7258.

```text
1.TournamentStatsProperty tournament_bullet_oddschess = 63;
  }
  oneof _tournament_blitz_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_chess = 64;
  }
  oneof _tournament_blitz_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_chess960 = 65;
  }
  oneof _tournament_blitz_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_bli
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09748"></a>
## FND-09748: oneof declaration: chesscom.user_properties.v1.Properties._tournament_blitz_chess960

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_blitz_chess960 {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 7346.

```text
z_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_chess = 64;
  }
  oneof _tournament_blitz_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_chess960 = 65;
  }
  oneof _tournament_blitz_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_bughouse = 66;
  }
  oneof _tournament_blitz_threecheck {
  .chesscom.user_properties
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09749"></a>
## FND-09749: chesscom.user_properties.v1.Properties.tournament_blitz_chess960 = 65

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_chess960 = 65;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 7383.

```text
.v1.TournamentStatsProperty tournament_blitz_chess = 64;
  }
  oneof _tournament_blitz_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_chess960 = 65;
  }
  oneof _tournament_blitz_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_bughouse = 66;
  }
  oneof _tournament_blitz_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournamen
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09750"></a>
## FND-09750: oneof declaration: chesscom.user_properties.v1.Properties._tournament_blitz_bughouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_blitz_bughouse {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 7474.

```text
s960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_chess960 = 65;
  }
  oneof _tournament_blitz_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_bughouse = 66;
  }
  oneof _tournament_blitz_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_threecheck = 67;
  }
  oneof _tournament_blitz_crazyhouse {
  .chesscom.user_proper
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09751"></a>
## FND-09751: chesscom.user_properties.v1.Properties.tournament_blitz_bughouse = 66

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_bughouse = 66;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 7511.

```text
.TournamentStatsProperty tournament_blitz_chess960 = 65;
  }
  oneof _tournament_blitz_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_bughouse = 66;
  }
  oneof _tournament_blitz_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_threecheck = 67;
  }
  oneof _tournament_blitz_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tourn
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09752"></a>
## FND-09752: oneof declaration: chesscom.user_properties.v1.Properties._tournament_blitz_threecheck

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_blitz_threecheck {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 7602.

```text
ouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_bughouse = 66;
  }
  oneof _tournament_blitz_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_threecheck = 67;
  }
  oneof _tournament_blitz_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_crazyhouse = 68;
  }
  oneof _tournament_blitz_kingofthehill {
  .chesscom.user
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09753"></a>
## FND-09753: chesscom.user_properties.v1.Properties.tournament_blitz_threecheck = 67

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_threecheck = 67;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 7641.

```text
ournamentStatsProperty tournament_blitz_bughouse = 66;
  }
  oneof _tournament_blitz_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_threecheck = 67;
  }
  oneof _tournament_blitz_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_crazyhouse = 68;
  }
  oneof _tournament_blitz_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsProperty 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09754"></a>
## FND-09754: oneof declaration: chesscom.user_properties.v1.Properties._tournament_blitz_crazyhouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_blitz_crazyhouse {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 7734.

```text
ck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_threecheck = 67;
  }
  oneof _tournament_blitz_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_crazyhouse = 68;
  }
  oneof _tournament_blitz_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_kingofthehill = 69;
  }
  oneof _tournament_blitz_oddschess {
  .chesscom.us
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09755"></a>
## FND-09755: chesscom.user_properties.v1.Properties.tournament_blitz_crazyhouse = 68

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_crazyhouse = 68;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 7773.

```text
rnamentStatsProperty tournament_blitz_threecheck = 67;
  }
  oneof _tournament_blitz_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_crazyhouse = 68;
  }
  oneof _tournament_blitz_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_kingofthehill = 69;
  }
  oneof _tournament_blitz_oddschess {
  .chesscom.user_properties.v1.TournamentStatsPropert
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09756"></a>
## FND-09756: oneof declaration: chesscom.user_properties.v1.Properties._tournament_blitz_kingofthehill

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_blitz_kingofthehill {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 7866.

```text
se {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_crazyhouse = 68;
  }
  oneof _tournament_blitz_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_kingofthehill = 69;
  }
  oneof _tournament_blitz_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_oddschess = 70;
  }
  oneof _tournament_rapid_chess {
  .chesscom.user_pro
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09757"></a>
## FND-09757: chesscom.user_properties.v1.Properties.tournament_blitz_kingofthehill = 69

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_kingofthehill = 69;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 7908.

```text
mentStatsProperty tournament_blitz_crazyhouse = 68;
  }
  oneof _tournament_blitz_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_kingofthehill = 69;
  }
  oneof _tournament_blitz_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_oddschess = 70;
  }
  oneof _tournament_rapid_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournam
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09758"></a>
## FND-09758: oneof declaration: chesscom.user_properties.v1.Properties._tournament_blitz_oddschess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_blitz_oddschess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8004.

```text
{
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_kingofthehill = 69;
  }
  oneof _tournament_blitz_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_oddschess = 70;
  }
  oneof _tournament_rapid_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_chess = 71;
  }
  oneof _tournament_rapid_chess960 {
  .chesscom.user_properties.v1.To
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09759"></a>
## FND-09759: chesscom.user_properties.v1.Properties.tournament_blitz_oddschess = 70

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_oddschess = 70;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8042.

```text
amentStatsProperty tournament_blitz_kingofthehill = 69;
  }
  oneof _tournament_blitz_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_oddschess = 70;
  }
  oneof _tournament_rapid_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_chess = 71;
  }
  oneof _tournament_rapid_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09760"></a>
## FND-09760: oneof declaration: chesscom.user_properties.v1.Properties._tournament_rapid_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_rapid_chess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8134.

```text
ess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_blitz_oddschess = 70;
  }
  oneof _tournament_rapid_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_chess = 71;
  }
  oneof _tournament_rapid_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_chess960 = 72;
  }
  oneof _tournament_rapid_bughouse {
  .chesscom.user_properties.v1.Tour
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09761"></a>
## FND-09761: chesscom.user_properties.v1.Properties.tournament_rapid_chess = 71

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_chess = 71;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8168.

```text
v1.TournamentStatsProperty tournament_blitz_oddschess = 70;
  }
  oneof _tournament_rapid_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_chess = 71;
  }
  oneof _tournament_rapid_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_chess960 = 72;
  }
  oneof _tournament_rapid_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rap
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09762"></a>
## FND-09762: oneof declaration: chesscom.user_properties.v1.Properties._tournament_rapid_chess960

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_rapid_chess960 {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8256.

```text
d_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_chess = 71;
  }
  oneof _tournament_rapid_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_chess960 = 72;
  }
  oneof _tournament_rapid_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_bughouse = 73;
  }
  oneof _tournament_rapid_threecheck {
  .chesscom.user_properties
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09763"></a>
## FND-09763: chesscom.user_properties.v1.Properties.tournament_rapid_chess960 = 72

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_chess960 = 72;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8293.

```text
.v1.TournamentStatsProperty tournament_rapid_chess = 71;
  }
  oneof _tournament_rapid_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_chess960 = 72;
  }
  oneof _tournament_rapid_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_bughouse = 73;
  }
  oneof _tournament_rapid_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournamen
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09764"></a>
## FND-09764: oneof declaration: chesscom.user_properties.v1.Properties._tournament_rapid_bughouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_rapid_bughouse {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8384.

```text
s960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_chess960 = 72;
  }
  oneof _tournament_rapid_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_bughouse = 73;
  }
  oneof _tournament_rapid_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_threecheck = 74;
  }
  oneof _tournament_rapid_crazyhouse {
  .chesscom.user_proper
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09765"></a>
## FND-09765: chesscom.user_properties.v1.Properties.tournament_rapid_bughouse = 73

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_bughouse = 73;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8421.

```text
.TournamentStatsProperty tournament_rapid_chess960 = 72;
  }
  oneof _tournament_rapid_bughouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_bughouse = 73;
  }
  oneof _tournament_rapid_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_threecheck = 74;
  }
  oneof _tournament_rapid_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tourn
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09766"></a>
## FND-09766: oneof declaration: chesscom.user_properties.v1.Properties._tournament_rapid_threecheck

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_rapid_threecheck {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8512.

```text
ouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_bughouse = 73;
  }
  oneof _tournament_rapid_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_threecheck = 74;
  }
  oneof _tournament_rapid_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_crazyhouse = 75;
  }
  oneof _tournament_rapid_kingofthehill {
  .chesscom.user
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09767"></a>
## FND-09767: chesscom.user_properties.v1.Properties.tournament_rapid_threecheck = 74

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_threecheck = 74;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8551.

```text
ournamentStatsProperty tournament_rapid_bughouse = 73;
  }
  oneof _tournament_rapid_threecheck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_threecheck = 74;
  }
  oneof _tournament_rapid_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_crazyhouse = 75;
  }
  oneof _tournament_rapid_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsProperty 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09768"></a>
## FND-09768: oneof declaration: chesscom.user_properties.v1.Properties._tournament_rapid_crazyhouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_rapid_crazyhouse {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8644.

```text
ck {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_threecheck = 74;
  }
  oneof _tournament_rapid_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_crazyhouse = 75;
  }
  oneof _tournament_rapid_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_kingofthehill = 76;
  }
  oneof _tournament_rapid_oddschess {
  .chesscom.us
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09769"></a>
## FND-09769: chesscom.user_properties.v1.Properties.tournament_rapid_crazyhouse = 75

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_crazyhouse = 75;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8683.

```text
rnamentStatsProperty tournament_rapid_threecheck = 74;
  }
  oneof _tournament_rapid_crazyhouse {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_crazyhouse = 75;
  }
  oneof _tournament_rapid_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_kingofthehill = 76;
  }
  oneof _tournament_rapid_oddschess {
  .chesscom.user_properties.v1.TournamentStatsPropert
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09770"></a>
## FND-09770: oneof declaration: chesscom.user_properties.v1.Properties._tournament_rapid_kingofthehill

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_rapid_kingofthehill {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8776.

```text
se {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_crazyhouse = 75;
  }
  oneof _tournament_rapid_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_kingofthehill = 76;
  }
  oneof _tournament_rapid_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_oddschess = 77;
  }
  oneof _tournament_daily_chess {
  .chesscom.user_pro
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09771"></a>
## FND-09771: chesscom.user_properties.v1.Properties.tournament_rapid_kingofthehill = 76

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_kingofthehill = 76;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8818.

```text
mentStatsProperty tournament_rapid_crazyhouse = 75;
  }
  oneof _tournament_rapid_kingofthehill {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_kingofthehill = 76;
  }
  oneof _tournament_rapid_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_oddschess = 77;
  }
  oneof _tournament_daily_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournam
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09772"></a>
## FND-09772: oneof declaration: chesscom.user_properties.v1.Properties._tournament_rapid_oddschess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_rapid_oddschess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8914.

```text
{
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_kingofthehill = 76;
  }
  oneof _tournament_rapid_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_oddschess = 77;
  }
  oneof _tournament_daily_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_chess = 78;
  }
  oneof _tournament_daily_chess960 {
  .chesscom.user_properties.v1.To
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09773"></a>
## FND-09773: chesscom.user_properties.v1.Properties.tournament_rapid_oddschess = 77

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_oddschess = 77;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 8952.

```text
amentStatsProperty tournament_rapid_kingofthehill = 76;
  }
  oneof _tournament_rapid_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_oddschess = 77;
  }
  oneof _tournament_daily_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_chess = 78;
  }
  oneof _tournament_daily_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09774"></a>
## FND-09774: oneof declaration: chesscom.user_properties.v1.Properties._tournament_daily_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_daily_chess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9044.

```text
ess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_rapid_oddschess = 77;
  }
  oneof _tournament_daily_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_chess = 78;
  }
  oneof _tournament_daily_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_chess960 = 79;
  }
  oneof _tournament_daily_oddschess {
  .chesscom.user_properties.v1.Tou
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
