# data_models — findings 9501–9600

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-09775"></a>
## FND-09775: chesscom.user_properties.v1.Properties.tournament_daily_chess = 78

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_chess = 78;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9078.

```text
v1.TournamentStatsProperty tournament_rapid_oddschess = 77;
  }
  oneof _tournament_daily_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_chess = 78;
  }
  oneof _tournament_daily_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_chess960 = 79;
  }
  oneof _tournament_daily_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_da
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09776"></a>
## FND-09776: oneof declaration: chesscom.user_properties.v1.Properties._tournament_daily_chess960

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_daily_chess960 {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9166.

```text
y_chess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_chess = 78;
  }
  oneof _tournament_daily_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_chess960 = 79;
  }
  oneof _tournament_daily_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_oddschess = 80;
  }
  oneof _user_engagement {
  .chesscom.user_properties.v1.UserEn
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09777"></a>
## FND-09777: chesscom.user_properties.v1.Properties.tournament_daily_chess960 = 79

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_chess960 = 79;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9203.

```text
.v1.TournamentStatsProperty tournament_daily_chess = 78;
  }
  oneof _tournament_daily_chess960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_chess960 = 79;
  }
  oneof _tournament_daily_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_oddschess = 80;
  }
  oneof _user_engagement {
  .chesscom.user_properties.v1.UserEngagementProperty user_engagement = 81
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09778"></a>
## FND-09778: oneof declaration: chesscom.user_properties.v1.Properties._tournament_daily_oddschess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tournament_daily_oddschess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9294.

```text
s960 {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_chess960 = 79;
  }
  oneof _tournament_daily_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_oddschess = 80;
  }
  oneof _user_engagement {
  .chesscom.user_properties.v1.UserEngagementProperty user_engagement = 81;
  }
  oneof _coaches {
  .chesscom.user_properties.v1.CoachesProperty coaches = 82;
  }
 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09779"></a>
## FND-09779: chesscom.user_properties.v1.Properties.tournament_daily_oddschess = 80

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_oddschess = 80;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9332.

```text
TournamentStatsProperty tournament_daily_chess960 = 79;
  }
  oneof _tournament_daily_oddschess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_oddschess = 80;
  }
  oneof _user_engagement {
  .chesscom.user_properties.v1.UserEngagementProperty user_engagement = 81;
  }
  oneof _coaches {
  .chesscom.user_properties.v1.CoachesProperty coaches = 82;
  }
  oneof _themes {
  .chesscom.user_prop
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09780"></a>
## FND-09780: oneof declaration: chesscom.user_properties.v1.Properties._user_engagement

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_engagement {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9424.

```text
ess {
  .chesscom.user_properties.v1.TournamentStatsProperty tournament_daily_oddschess = 80;
  }
  oneof _user_engagement {
  .chesscom.user_properties.v1.UserEngagementProperty user_engagement = 81;
  }
  oneof _coaches {
  .chesscom.user_properties.v1.CoachesProperty coaches = 82;
  }
  oneof _themes {
  .chesscom.user_properties.v1.ThemesProperty themes = 83;
  }
  oneof _ipqs {
  .chesscom.user_properties.v1.Ipq
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09781"></a>
## FND-09781: chesscom.user_properties.v1.Properties.user_engagement = 81

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.UserEngagementProperty user_engagement = 81;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9451.

```text
erties.v1.TournamentStatsProperty tournament_daily_oddschess = 80;
  }
  oneof _user_engagement {
  .chesscom.user_properties.v1.UserEngagementProperty user_engagement = 81;
  }
  oneof _coaches {
  .chesscom.user_properties.v1.CoachesProperty coaches = 82;
  }
  oneof _themes {
  .chesscom.user_properties.v1.ThemesProperty themes = 83;
  }
  oneof _ipqs {
  .chesscom.user_properties.v1.IpqsProperty ipqs = 84;
  }
  
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09782"></a>
## FND-09782: oneof declaration: chesscom.user_properties.v1.Properties._coaches

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _coaches {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9531.

```text
user_engagement {
  .chesscom.user_properties.v1.UserEngagementProperty user_engagement = 81;
  }
  oneof _coaches {
  .chesscom.user_properties.v1.CoachesProperty coaches = 82;
  }
  oneof _themes {
  .chesscom.user_properties.v1.ThemesProperty themes = 83;
  }
  oneof _ipqs {
  .chesscom.user_properties.v1.IpqsProperty ipqs = 84;
  }
  oneof _puzzle_stats {
  .chesscom.user_properties.v1.UserPuzzleStatsProperty puz
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09783"></a>
## FND-09783: chesscom.user_properties.v1.Properties.coaches = 82

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.CoachesProperty coaches = 82;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9550.

```text
 .chesscom.user_properties.v1.UserEngagementProperty user_engagement = 81;
  }
  oneof _coaches {
  .chesscom.user_properties.v1.CoachesProperty coaches = 82;
  }
  oneof _themes {
  .chesscom.user_properties.v1.ThemesProperty themes = 83;
  }
  oneof _ipqs {
  .chesscom.user_properties.v1.IpqsProperty ipqs = 84;
  }
  oneof _puzzle_stats {
  .chesscom.user_properties.v1.UserPuzzleStatsProperty puzzle_stats = 85;
  }
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09784"></a>
## FND-09784: oneof declaration: chesscom.user_properties.v1.Properties._themes

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _themes {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9615.

```text
ent = 81;
  }
  oneof _coaches {
  .chesscom.user_properties.v1.CoachesProperty coaches = 82;
  }
  oneof _themes {
  .chesscom.user_properties.v1.ThemesProperty themes = 83;
  }
  oneof _ipqs {
  .chesscom.user_properties.v1.IpqsProperty ipqs = 84;
  }
  oneof _puzzle_stats {
  .chesscom.user_properties.v1.UserPuzzleStatsProperty puzzle_stats = 85;
  }
  oneof _courses {
  .chesscom.user_properties.v1.CoursesPropert
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09785"></a>
## FND-09785: chesscom.user_properties.v1.Properties.themes = 83

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.ThemesProperty themes = 83;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9633.

```text
eof _coaches {
  .chesscom.user_properties.v1.CoachesProperty coaches = 82;
  }
  oneof _themes {
  .chesscom.user_properties.v1.ThemesProperty themes = 83;
  }
  oneof _ipqs {
  .chesscom.user_properties.v1.IpqsProperty ipqs = 84;
  }
  oneof _puzzle_stats {
  .chesscom.user_properties.v1.UserPuzzleStatsProperty puzzle_stats = 85;
  }
  oneof _courses {
  .chesscom.user_properties.v1.CoursesProperty courses = 86;
  
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09786"></a>
## FND-09786: oneof declaration: chesscom.user_properties.v1.Properties._ipqs

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ipqs {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9696.

```text
oaches = 82;
  }
  oneof _themes {
  .chesscom.user_properties.v1.ThemesProperty themes = 83;
  }
  oneof _ipqs {
  .chesscom.user_properties.v1.IpqsProperty ipqs = 84;
  }
  oneof _puzzle_stats {
  .chesscom.user_properties.v1.UserPuzzleStatsProperty puzzle_stats = 85;
  }
  oneof _courses {
  .chesscom.user_properties.v1.CoursesProperty courses = 86;
  }
  oneof _survey {
  .chesscom.user_properties.v1.SurveyProper
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09787"></a>
## FND-09787: chesscom.user_properties.v1.Properties.ipqs = 84

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.IpqsProperty ipqs = 84;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9712.

```text

  oneof _themes {
  .chesscom.user_properties.v1.ThemesProperty themes = 83;
  }
  oneof _ipqs {
  .chesscom.user_properties.v1.IpqsProperty ipqs = 84;
  }
  oneof _puzzle_stats {
  .chesscom.user_properties.v1.UserPuzzleStatsProperty puzzle_stats = 85;
  }
  oneof _courses {
  .chesscom.user_properties.v1.CoursesProperty courses = 86;
  }
  oneof _survey {
  .chesscom.user_properties.v1.SurveyProperty survey = 87;

```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09788"></a>
## FND-09788: oneof declaration: chesscom.user_properties.v1.Properties._puzzle_stats

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzle_stats {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9771.

```text
perty themes = 83;
  }
  oneof _ipqs {
  .chesscom.user_properties.v1.IpqsProperty ipqs = 84;
  }
  oneof _puzzle_stats {
  .chesscom.user_properties.v1.UserPuzzleStatsProperty puzzle_stats = 85;
  }
  oneof _courses {
  .chesscom.user_properties.v1.CoursesProperty courses = 86;
  }
  oneof _survey {
  .chesscom.user_properties.v1.SurveyProperty survey = 87;
  }
  oneof _attribution_subscription_upgrade_initial {
  .
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09789"></a>
## FND-09789: chesscom.user_properties.v1.Properties.puzzle_stats = 85

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.UserPuzzleStatsProperty puzzle_stats = 85;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9795.

```text
 oneof _ipqs {
  .chesscom.user_properties.v1.IpqsProperty ipqs = 84;
  }
  oneof _puzzle_stats {
  .chesscom.user_properties.v1.UserPuzzleStatsProperty puzzle_stats = 85;
  }
  oneof _courses {
  .chesscom.user_properties.v1.CoursesProperty courses = 86;
  }
  oneof _survey {
  .chesscom.user_properties.v1.SurveyProperty survey = 87;
  }
  oneof _attribution_subscription_upgrade_initial {
  .chesscom.user_properties
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09790"></a>
## FND-09790: oneof declaration: chesscom.user_properties.v1.Properties._courses

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _courses {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9873.

```text
eof _puzzle_stats {
  .chesscom.user_properties.v1.UserPuzzleStatsProperty puzzle_stats = 85;
  }
  oneof _courses {
  .chesscom.user_properties.v1.CoursesProperty courses = 86;
  }
  oneof _survey {
  .chesscom.user_properties.v1.SurveyProperty survey = 87;
  }
  oneof _attribution_subscription_upgrade_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_subscription_upgrade_initial = 88;
  }
  o
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09791"></a>
## FND-09791: chesscom.user_properties.v1.Properties.courses = 86

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.CoursesProperty courses = 86;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9892.

```text

  .chesscom.user_properties.v1.UserPuzzleStatsProperty puzzle_stats = 85;
  }
  oneof _courses {
  .chesscom.user_properties.v1.CoursesProperty courses = 86;
  }
  oneof _survey {
  .chesscom.user_properties.v1.SurveyProperty survey = 87;
  }
  oneof _attribution_subscription_upgrade_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_subscription_upgrade_initial = 88;
  }
  oneof _attribution_s
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09792"></a>
## FND-09792: oneof declaration: chesscom.user_properties.v1.Properties._survey

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _survey {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9957.

```text
ats = 85;
  }
  oneof _courses {
  .chesscom.user_properties.v1.CoursesProperty courses = 86;
  }
  oneof _survey {
  .chesscom.user_properties.v1.SurveyProperty survey = 87;
  }
  oneof _attribution_subscription_upgrade_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_subscription_upgrade_initial = 88;
  }
  oneof _attribution_subscription_upgrade_last {
  .chesscom.user_properties.v1.Attribu
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09793"></a>
## FND-09793: chesscom.user_properties.v1.Properties.survey = 87

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.SurveyProperty survey = 87;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 9975.

```text
eof _courses {
  .chesscom.user_properties.v1.CoursesProperty courses = 86;
  }
  oneof _survey {
  .chesscom.user_properties.v1.SurveyProperty survey = 87;
  }
  oneof _attribution_subscription_upgrade_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_subscription_upgrade_initial = 88;
  }
  oneof _attribution_subscription_upgrade_last {
  .chesscom.user_properties.v1.AttributionProperty attri
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09794"></a>
## FND-09794: oneof declaration: chesscom.user_properties.v1.Properties._attribution_subscription_upgrade_initial

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _attribution_subscription_upgrade_initial {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10038.

```text
ourses = 86;
  }
  oneof _survey {
  .chesscom.user_properties.v1.SurveyProperty survey = 87;
  }
  oneof _attribution_subscription_upgrade_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_subscription_upgrade_initial = 88;
  }
  oneof _attribution_subscription_upgrade_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_subscription_upgrade_last = 89;
  }
  oneof _product_act
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09795"></a>
## FND-09795: chesscom.user_properties.v1.Properties.attribution_subscription_upgrade_initial = 88

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AttributionProperty attribution_subscription_upgrade_initial = 88;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10090.

```text
properties.v1.SurveyProperty survey = 87;
  }
  oneof _attribution_subscription_upgrade_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_subscription_upgrade_initial = 88;
  }
  oneof _attribution_subscription_upgrade_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_subscription_upgrade_last = 89;
  }
  oneof _product_activity_rankings {
  .chesscom.user_properties.v1.Prod
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09796"></a>
## FND-09796: oneof declaration: chesscom.user_properties.v1.Properties._attribution_subscription_upgrade_last

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _attribution_subscription_upgrade_last {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10192.

```text
hesscom.user_properties.v1.AttributionProperty attribution_subscription_upgrade_initial = 88;
  }
  oneof _attribution_subscription_upgrade_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_subscription_upgrade_last = 89;
  }
  oneof _product_activity_rankings {
  .chesscom.user_properties.v1.ProductActivityRankingsProperty product_activity_rankings = 90;
  }
  oneof _turnstile {
  .chesscom.user_
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09797"></a>
## FND-09797: chesscom.user_properties.v1.Properties.attribution_subscription_upgrade_last = 89

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AttributionProperty attribution_subscription_upgrade_last = 89;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10241.

```text
tribution_subscription_upgrade_initial = 88;
  }
  oneof _attribution_subscription_upgrade_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_subscription_upgrade_last = 89;
  }
  oneof _product_activity_rankings {
  .chesscom.user_properties.v1.ProductActivityRankingsProperty product_activity_rankings = 90;
  }
  oneof _turnstile {
  .chesscom.user_properties.v1.TurnstileProperty turnstile = 91;
 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09798"></a>
## FND-09798: oneof declaration: chesscom.user_properties.v1.Properties._product_activity_rankings

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _product_activity_rankings {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10340.

```text
 .chesscom.user_properties.v1.AttributionProperty attribution_subscription_upgrade_last = 89;
  }
  oneof _product_activity_rankings {
  .chesscom.user_properties.v1.ProductActivityRankingsProperty product_activity_rankings = 90;
  }
  oneof _turnstile {
  .chesscom.user_properties.v1.TurnstileProperty turnstile = 91;
  }
  oneof _user_streak_v2 {
  .chesscom.user_properties.v1.UserStreakV2Property user_streak_v2 = 9
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09799"></a>
## FND-09799: chesscom.user_properties.v1.Properties.product_activity_rankings = 90

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.ProductActivityRankingsProperty product_activity_rankings = 90;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10377.

```text
tionProperty attribution_subscription_upgrade_last = 89;
  }
  oneof _product_activity_rankings {
  .chesscom.user_properties.v1.ProductActivityRankingsProperty product_activity_rankings = 90;
  }
  oneof _turnstile {
  .chesscom.user_properties.v1.TurnstileProperty turnstile = 91;
  }
  oneof _user_streak_v2 {
  .chesscom.user_properties.v1.UserStreakV2Property user_streak_v2 = 92;
  }
  oneof _fair_play {
  .chessc
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09800"></a>
## FND-09800: oneof declaration: chesscom.user_properties.v1.Properties._turnstile

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _turnstile {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10476.

```text
 .chesscom.user_properties.v1.ProductActivityRankingsProperty product_activity_rankings = 90;
  }
  oneof _turnstile {
  .chesscom.user_properties.v1.TurnstileProperty turnstile = 91;
  }
  oneof _user_streak_v2 {
  .chesscom.user_properties.v1.UserStreakV2Property user_streak_v2 = 92;
  }
  oneof _fair_play {
  .chesscom.user_properties.v1.FairPlayProperty fair_play = 93;
  }
  oneof _navbar {
  .chesscom.user_prope
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09801"></a>
## FND-09801: chesscom.user_properties.v1.Properties.turnstile = 91

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TurnstileProperty turnstile = 91;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10497.

```text
rties.v1.ProductActivityRankingsProperty product_activity_rankings = 90;
  }
  oneof _turnstile {
  .chesscom.user_properties.v1.TurnstileProperty turnstile = 91;
  }
  oneof _user_streak_v2 {
  .chesscom.user_properties.v1.UserStreakV2Property user_streak_v2 = 92;
  }
  oneof _fair_play {
  .chesscom.user_properties.v1.FairPlayProperty fair_play = 93;
  }
  oneof _navbar {
  .chesscom.user_properties.v1.NavbarProper
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09802"></a>
## FND-09802: oneof declaration: chesscom.user_properties.v1.Properties._user_streak_v2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_streak_v2 {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10566.

```text
90;
  }
  oneof _turnstile {
  .chesscom.user_properties.v1.TurnstileProperty turnstile = 91;
  }
  oneof _user_streak_v2 {
  .chesscom.user_properties.v1.UserStreakV2Property user_streak_v2 = 92;
  }
  oneof _fair_play {
  .chesscom.user_properties.v1.FairPlayProperty fair_play = 93;
  }
  oneof _navbar {
  .chesscom.user_properties.v1.NavbarProperty navbar = 94;
  }
  oneof _themes_ios {
  .chesscom.user_properties
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09803"></a>
## FND-09803: chesscom.user_properties.v1.Properties.user_streak_v2 = 92

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.UserStreakV2Property user_streak_v2 = 92;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10592.

```text
 {
  .chesscom.user_properties.v1.TurnstileProperty turnstile = 91;
  }
  oneof _user_streak_v2 {
  .chesscom.user_properties.v1.UserStreakV2Property user_streak_v2 = 92;
  }
  oneof _fair_play {
  .chesscom.user_properties.v1.FairPlayProperty fair_play = 93;
  }
  oneof _navbar {
  .chesscom.user_properties.v1.NavbarProperty navbar = 94;
  }
  oneof _themes_ios {
  .chesscom.user_properties.v1.ThemesProperty themes_
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09804"></a>
## FND-09804: oneof declaration: chesscom.user_properties.v1.Properties._fair_play

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _fair_play {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10669.

```text
of _user_streak_v2 {
  .chesscom.user_properties.v1.UserStreakV2Property user_streak_v2 = 92;
  }
  oneof _fair_play {
  .chesscom.user_properties.v1.FairPlayProperty fair_play = 93;
  }
  oneof _navbar {
  .chesscom.user_properties.v1.NavbarProperty navbar = 94;
  }
  oneof _themes_ios {
  .chesscom.user_properties.v1.ThemesProperty themes_ios = 95;
  }
  oneof _themes_android {
  .chesscom.user_properties.v1.Themes
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09805"></a>
## FND-09805: chesscom.user_properties.v1.Properties.fair_play = 93

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.FairPlayProperty fair_play = 93;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10690.

```text
  .chesscom.user_properties.v1.UserStreakV2Property user_streak_v2 = 92;
  }
  oneof _fair_play {
  .chesscom.user_properties.v1.FairPlayProperty fair_play = 93;
  }
  oneof _navbar {
  .chesscom.user_properties.v1.NavbarProperty navbar = 94;
  }
  oneof _themes_ios {
  .chesscom.user_properties.v1.ThemesProperty themes_ios = 95;
  }
  oneof _themes_android {
  .chesscom.user_properties.v1.ThemesProperty themes_andro
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09806"></a>
## FND-09806: oneof declaration: chesscom.user_properties.v1.Properties._navbar

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _navbar {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10758.

```text
 92;
  }
  oneof _fair_play {
  .chesscom.user_properties.v1.FairPlayProperty fair_play = 93;
  }
  oneof _navbar {
  .chesscom.user_properties.v1.NavbarProperty navbar = 94;
  }
  oneof _themes_ios {
  .chesscom.user_properties.v1.ThemesProperty themes_ios = 95;
  }
  oneof _themes_android {
  .chesscom.user_properties.v1.ThemesProperty themes_android = 96;
  }
  oneof _widgets_ios {
  .chesscom.user_properties.v1.W
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09807"></a>
## FND-09807: chesscom.user_properties.v1.Properties.navbar = 94

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.NavbarProperty navbar = 94;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10776.

```text
fair_play {
  .chesscom.user_properties.v1.FairPlayProperty fair_play = 93;
  }
  oneof _navbar {
  .chesscom.user_properties.v1.NavbarProperty navbar = 94;
  }
  oneof _themes_ios {
  .chesscom.user_properties.v1.ThemesProperty themes_ios = 95;
  }
  oneof _themes_android {
  .chesscom.user_properties.v1.ThemesProperty themes_android = 96;
  }
  oneof _widgets_ios {
  .chesscom.user_properties.v1.WidgetsProperty wid
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09808"></a>
## FND-09808: oneof declaration: chesscom.user_properties.v1.Properties._themes_ios

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _themes_ios {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10839.

```text
r_play = 93;
  }
  oneof _navbar {
  .chesscom.user_properties.v1.NavbarProperty navbar = 94;
  }
  oneof _themes_ios {
  .chesscom.user_properties.v1.ThemesProperty themes_ios = 95;
  }
  oneof _themes_android {
  .chesscom.user_properties.v1.ThemesProperty themes_android = 96;
  }
  oneof _widgets_ios {
  .chesscom.user_properties.v1.WidgetsProperty widgets_ios = 97;
  }
  oneof _widgets_android {
  .chesscom.user_
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09809"></a>
## FND-09809: chesscom.user_properties.v1.Properties.themes_ios = 95

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.ThemesProperty themes_ios = 95;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10861.

```text
of _navbar {
  .chesscom.user_properties.v1.NavbarProperty navbar = 94;
  }
  oneof _themes_ios {
  .chesscom.user_properties.v1.ThemesProperty themes_ios = 95;
  }
  oneof _themes_android {
  .chesscom.user_properties.v1.ThemesProperty themes_android = 96;
  }
  oneof _widgets_ios {
  .chesscom.user_properties.v1.WidgetsProperty widgets_ios = 97;
  }
  oneof _widgets_android {
  .chesscom.user_properties.v1.WidgetsP
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09810"></a>
## FND-09810: oneof declaration: chesscom.user_properties.v1.Properties._themes_android

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _themes_android {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10928.

```text
 94;
  }
  oneof _themes_ios {
  .chesscom.user_properties.v1.ThemesProperty themes_ios = 95;
  }
  oneof _themes_android {
  .chesscom.user_properties.v1.ThemesProperty themes_android = 96;
  }
  oneof _widgets_ios {
  .chesscom.user_properties.v1.WidgetsProperty widgets_ios = 97;
  }
  oneof _widgets_android {
  .chesscom.user_properties.v1.WidgetsProperty widgets_android = 98;
  }
  oneof _league {
  .chesscom.use
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09811"></a>
## FND-09811: chesscom.user_properties.v1.Properties.themes_android = 96

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.ThemesProperty themes_android = 96;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 10954.

```text
os {
  .chesscom.user_properties.v1.ThemesProperty themes_ios = 95;
  }
  oneof _themes_android {
  .chesscom.user_properties.v1.ThemesProperty themes_android = 96;
  }
  oneof _widgets_ios {
  .chesscom.user_properties.v1.WidgetsProperty widgets_ios = 97;
  }
  oneof _widgets_android {
  .chesscom.user_properties.v1.WidgetsProperty widgets_android = 98;
  }
  oneof _league {
  .chesscom.user_properties.v1.LeagueProp
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09812"></a>
## FND-09812: oneof declaration: chesscom.user_properties.v1.Properties._widgets_ios

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _widgets_ios {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11025.

```text

  oneof _themes_android {
  .chesscom.user_properties.v1.ThemesProperty themes_android = 96;
  }
  oneof _widgets_ios {
  .chesscom.user_properties.v1.WidgetsProperty widgets_ios = 97;
  }
  oneof _widgets_android {
  .chesscom.user_properties.v1.WidgetsProperty widgets_android = 98;
  }
  oneof _league {
  .chesscom.user_properties.v1.LeagueProperty league = 99;
  }
  oneof _puzzle_rush {
  .chesscom.user_propertie
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09813"></a>
## FND-09813: chesscom.user_properties.v1.Properties.widgets_ios = 97

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.WidgetsProperty widgets_ios = 97;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11048.

```text
d {
  .chesscom.user_properties.v1.ThemesProperty themes_android = 96;
  }
  oneof _widgets_ios {
  .chesscom.user_properties.v1.WidgetsProperty widgets_ios = 97;
  }
  oneof _widgets_android {
  .chesscom.user_properties.v1.WidgetsProperty widgets_android = 98;
  }
  oneof _league {
  .chesscom.user_properties.v1.LeagueProperty league = 99;
  }
  oneof _puzzle_rush {
  .chesscom.user_properties.v1.PuzzleRushProperty
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09814"></a>
## FND-09814: oneof declaration: chesscom.user_properties.v1.Properties._widgets_android

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _widgets_android {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11117.

```text
;
  }
  oneof _widgets_ios {
  .chesscom.user_properties.v1.WidgetsProperty widgets_ios = 97;
  }
  oneof _widgets_android {
  .chesscom.user_properties.v1.WidgetsProperty widgets_android = 98;
  }
  oneof _league {
  .chesscom.user_properties.v1.LeagueProperty league = 99;
  }
  oneof _puzzle_rush {
  .chesscom.user_properties.v1.PuzzleRushProperty puzzle_rush = 100;
  }
  oneof _monthly_bot_event {
  .chesscom.user
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09815"></a>
## FND-09815: chesscom.user_properties.v1.Properties.widgets_android = 98

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.WidgetsProperty widgets_android = 98;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11144.

```text
{
  .chesscom.user_properties.v1.WidgetsProperty widgets_ios = 97;
  }
  oneof _widgets_android {
  .chesscom.user_properties.v1.WidgetsProperty widgets_android = 98;
  }
  oneof _league {
  .chesscom.user_properties.v1.LeagueProperty league = 99;
  }
  oneof _puzzle_rush {
  .chesscom.user_properties.v1.PuzzleRushProperty puzzle_rush = 100;
  }
  oneof _monthly_bot_event {
  .chesscom.user_properties.v1.MonthlyBotEv
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09816"></a>
## FND-09816: oneof declaration: chesscom.user_properties.v1.Properties._league

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _league {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11217.

```text
oneof _widgets_android {
  .chesscom.user_properties.v1.WidgetsProperty widgets_android = 98;
  }
  oneof _league {
  .chesscom.user_properties.v1.LeagueProperty league = 99;
  }
  oneof _puzzle_rush {
  .chesscom.user_properties.v1.PuzzleRushProperty puzzle_rush = 100;
  }
  oneof _monthly_bot_event {
  .chesscom.user_properties.v1.MonthlyBotEventProperty monthly_bot_event = 101;
  }
  oneof _predictive {
  .chessco
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09817"></a>
## FND-09817: chesscom.user_properties.v1.Properties.league = 99

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.LeagueProperty league = 99;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11235.

```text
roid {
  .chesscom.user_properties.v1.WidgetsProperty widgets_android = 98;
  }
  oneof _league {
  .chesscom.user_properties.v1.LeagueProperty league = 99;
  }
  oneof _puzzle_rush {
  .chesscom.user_properties.v1.PuzzleRushProperty puzzle_rush = 100;
  }
  oneof _monthly_bot_event {
  .chesscom.user_properties.v1.MonthlyBotEventProperty monthly_bot_event = 101;
  }
  oneof _predictive {
  .chesscom.user_properties.
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09818"></a>
## FND-09818: oneof declaration: chesscom.user_properties.v1.Properties._puzzle_rush

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzle_rush {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11298.

```text
ndroid = 98;
  }
  oneof _league {
  .chesscom.user_properties.v1.LeagueProperty league = 99;
  }
  oneof _puzzle_rush {
  .chesscom.user_properties.v1.PuzzleRushProperty puzzle_rush = 100;
  }
  oneof _monthly_bot_event {
  .chesscom.user_properties.v1.MonthlyBotEventProperty monthly_bot_event = 101;
  }
  oneof _predictive {
  .chesscom.user_properties.v1.PredictiveProperty predictive = 102;
  }
  oneof _growth {
 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09819"></a>
## FND-09819: chesscom.user_properties.v1.Properties.puzzle_rush = 100

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PuzzleRushProperty puzzle_rush = 100;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11321.

```text
f _league {
  .chesscom.user_properties.v1.LeagueProperty league = 99;
  }
  oneof _puzzle_rush {
  .chesscom.user_properties.v1.PuzzleRushProperty puzzle_rush = 100;
  }
  oneof _monthly_bot_event {
  .chesscom.user_properties.v1.MonthlyBotEventProperty monthly_bot_event = 101;
  }
  oneof _predictive {
  .chesscom.user_properties.v1.PredictiveProperty predictive = 102;
  }
  oneof _growth {
  .chesscom.user_propert
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09820"></a>
## FND-09820: oneof declaration: chesscom.user_properties.v1.Properties._monthly_bot_event

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _monthly_bot_event {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11394.

```text
}
  oneof _puzzle_rush {
  .chesscom.user_properties.v1.PuzzleRushProperty puzzle_rush = 100;
  }
  oneof _monthly_bot_event {
  .chesscom.user_properties.v1.MonthlyBotEventProperty monthly_bot_event = 101;
  }
  oneof _predictive {
  .chesscom.user_properties.v1.PredictiveProperty predictive = 102;
  }
  oneof _growth {
  .chesscom.user_properties.v1.GrowthProperty growth = 103;
  }
  oneof _skills {
  .chesscom.use
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09821"></a>
## FND-09821: chesscom.user_properties.v1.Properties.monthly_bot_event = 101

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.MonthlyBotEventProperty monthly_bot_event = 101;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11423.

```text
hesscom.user_properties.v1.PuzzleRushProperty puzzle_rush = 100;
  }
  oneof _monthly_bot_event {
  .chesscom.user_properties.v1.MonthlyBotEventProperty monthly_bot_event = 101;
  }
  oneof _predictive {
  .chesscom.user_properties.v1.PredictiveProperty predictive = 102;
  }
  oneof _growth {
  .chesscom.user_properties.v1.GrowthProperty growth = 103;
  }
  oneof _skills {
  .chesscom.user_properties.v1.SkillsPropert
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09822"></a>
## FND-09822: oneof declaration: chesscom.user_properties.v1.Properties._predictive

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _predictive {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11507.

```text
y_bot_event {
  .chesscom.user_properties.v1.MonthlyBotEventProperty monthly_bot_event = 101;
  }
  oneof _predictive {
  .chesscom.user_properties.v1.PredictiveProperty predictive = 102;
  }
  oneof _growth {
  .chesscom.user_properties.v1.GrowthProperty growth = 103;
  }
  oneof _skills {
  .chesscom.user_properties.v1.SkillsProperty skills = 104;
  }
  oneof _opening_courses {
  .chesscom.user_properties.v1.Openin
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09823"></a>
## FND-09823: chesscom.user_properties.v1.Properties.predictive = 102

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PredictiveProperty predictive = 102;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11529.

```text
com.user_properties.v1.MonthlyBotEventProperty monthly_bot_event = 101;
  }
  oneof _predictive {
  .chesscom.user_properties.v1.PredictiveProperty predictive = 102;
  }
  oneof _growth {
  .chesscom.user_properties.v1.GrowthProperty growth = 103;
  }
  oneof _skills {
  .chesscom.user_properties.v1.SkillsProperty skills = 104;
  }
  oneof _opening_courses {
  .chesscom.user_properties.v1.OpeningCoursesProperty openi
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09824"></a>
## FND-09824: oneof declaration: chesscom.user_properties.v1.Properties._growth

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _growth {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11601.

```text
  }
  oneof _predictive {
  .chesscom.user_properties.v1.PredictiveProperty predictive = 102;
  }
  oneof _growth {
  .chesscom.user_properties.v1.GrowthProperty growth = 103;
  }
  oneof _skills {
  .chesscom.user_properties.v1.SkillsProperty skills = 104;
  }
  oneof _opening_courses {
  .chesscom.user_properties.v1.OpeningCoursesProperty opening_courses = 105;
  }
  repeated .chesscom.settings.v1.Setting settings 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09825"></a>
## FND-09825: chesscom.user_properties.v1.Properties.growth = 103

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.GrowthProperty growth = 103;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11619.

```text
ctive {
  .chesscom.user_properties.v1.PredictiveProperty predictive = 102;
  }
  oneof _growth {
  .chesscom.user_properties.v1.GrowthProperty growth = 103;
  }
  oneof _skills {
  .chesscom.user_properties.v1.SkillsProperty skills = 104;
  }
  oneof _opening_courses {
  .chesscom.user_properties.v1.OpeningCoursesProperty opening_courses = 105;
  }
  repeated .chesscom.settings.v1.Setting settings = 31;
}

message D
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09826"></a>
## FND-09826: oneof declaration: chesscom.user_properties.v1.Properties._skills

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _skills {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11683.

```text
tive = 102;
  }
  oneof _growth {
  .chesscom.user_properties.v1.GrowthProperty growth = 103;
  }
  oneof _skills {
  .chesscom.user_properties.v1.SkillsProperty skills = 104;
  }
  oneof _opening_courses {
  .chesscom.user_properties.v1.OpeningCoursesProperty opening_courses = 105;
  }
  repeated .chesscom.settings.v1.Setting settings = 31;
}

message Definitions {
  oneof definition {
  .chesscom.user_properties.v1
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09827"></a>
## FND-09827: chesscom.user_properties.v1.Properties.skills = 104

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.SkillsProperty skills = 104;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11701.

```text
oneof _growth {
  .chesscom.user_properties.v1.GrowthProperty growth = 103;
  }
  oneof _skills {
  .chesscom.user_properties.v1.SkillsProperty skills = 104;
  }
  oneof _opening_courses {
  .chesscom.user_properties.v1.OpeningCoursesProperty opening_courses = 105;
  }
  repeated .chesscom.settings.v1.Setting settings = 31;
}

message Definitions {
  oneof definition {
  .chesscom.user_properties.v1.CorePropertyDefin
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09828"></a>
## FND-09828: oneof declaration: chesscom.user_properties.v1.Properties._opening_courses

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening_courses {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11765.

```text
owth = 103;
  }
  oneof _skills {
  .chesscom.user_properties.v1.SkillsProperty skills = 104;
  }
  oneof _opening_courses {
  .chesscom.user_properties.v1.OpeningCoursesProperty opening_courses = 105;
  }
  repeated .chesscom.settings.v1.Setting settings = 31;
}

message Definitions {
  oneof definition {
  .chesscom.user_properties.v1.CorePropertyDefinition core = 1;
  .chesscom.user_properties.v1.PIIPropertyDefini
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09829"></a>
## FND-09829: chesscom.user_properties.v1.Properties.opening_courses = 105

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.OpeningCoursesProperty opening_courses = 105;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11792.

```text
ills {
  .chesscom.user_properties.v1.SkillsProperty skills = 104;
  }
  oneof _opening_courses {
  .chesscom.user_properties.v1.OpeningCoursesProperty opening_courses = 105;
  }
  repeated .chesscom.settings.v1.Setting settings = 31;
}

message Definitions {
  oneof definition {
  .chesscom.user_properties.v1.CorePropertyDefinition core = 1;
  .chesscom.user_properties.v1.PIIPropertyDefinition pii = 2;
  .chesscom.u
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09830"></a>
## FND-09830: chesscom.user_properties.v1.Properties.settings = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.settings.v1.Setting settings = 31;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11873.

```text
pening_courses {
  .chesscom.user_properties.v1.OpeningCoursesProperty opening_courses = 105;
  }
  repeated .chesscom.settings.v1.Setting settings = 31;
}

message Definitions {
  oneof definition {
  .chesscom.user_properties.v1.CorePropertyDefinition core = 1;
  .chesscom.user_properties.v1.PIIPropertyDefinition pii = 2;
  .chesscom.user_properties.v1.UserDetailsPropertyDefinition user_details = 3;
  .chesscom.use
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09831"></a>
## FND-09831: message declaration: chesscom.user_properties.v1.Definitions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Definitions {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11930.

```text
ursesProperty opening_courses = 105;
  }
  repeated .chesscom.settings.v1.Setting settings = 31;
}

message Definitions {
  oneof definition {
  .chesscom.user_properties.v1.CorePropertyDefinition core = 1;
  .chesscom.user_properties.v1.PIIPropertyDefinition pii = 2;
  .chesscom.user_properties.v1.UserDetailsPropertyDefinition user_details = 3;
  .chesscom.user_properties.v1.RolesPropertyDefinition roles = 4;
  .che
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09832"></a>
## FND-09832: oneof declaration: chesscom.user_properties.v1.Definitions.definition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof definition {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11954.

```text
urses = 105;
  }
  repeated .chesscom.settings.v1.Setting settings = 31;
}

message Definitions {
  oneof definition {
  .chesscom.user_properties.v1.CorePropertyDefinition core = 1;
  .chesscom.user_properties.v1.PIIPropertyDefinition pii = 2;
  .chesscom.user_properties.v1.UserDetailsPropertyDefinition user_details = 3;
  .chesscom.user_properties.v1.RolesPropertyDefinition roles = 4;
  .chesscom.user_properties.v1
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09833"></a>
## FND-09833: chesscom.user_properties.v1.Definitions.core = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.CorePropertyDefinition core = 1;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 11975.

```text
peated .chesscom.settings.v1.Setting settings = 31;
}

message Definitions {
  oneof definition {
  .chesscom.user_properties.v1.CorePropertyDefinition core = 1;
  .chesscom.user_properties.v1.PIIPropertyDefinition pii = 2;
  .chesscom.user_properties.v1.UserDetailsPropertyDefinition user_details = 3;
  .chesscom.user_properties.v1.RolesPropertyDefinition roles = 4;
  .chesscom.user_properties.v1.ActivityPropertyDefi
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09834"></a>
## FND-09834: chesscom.user_properties.v1.Definitions.pii = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PIIPropertyDefinition pii = 2;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 12039.

```text
efinitions {
  oneof definition {
  .chesscom.user_properties.v1.CorePropertyDefinition core = 1;
  .chesscom.user_properties.v1.PIIPropertyDefinition pii = 2;
  .chesscom.user_properties.v1.UserDetailsPropertyDefinition user_details = 3;
  .chesscom.user_properties.v1.RolesPropertyDefinition roles = 4;
  .chesscom.user_properties.v1.ActivityPropertyDefinition activity = 5;
  .chesscom.user_properties.v1.Subscription
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09835"></a>
## FND-09835: chesscom.user_properties.v1.Definitions.user_details = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.UserDetailsPropertyDefinition user_details = 3;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 12101.

```text
v1.CorePropertyDefinition core = 1;
  .chesscom.user_properties.v1.PIIPropertyDefinition pii = 2;
  .chesscom.user_properties.v1.UserDetailsPropertyDefinition user_details = 3;
  .chesscom.user_properties.v1.RolesPropertyDefinition roles = 4;
  .chesscom.user_properties.v1.ActivityPropertyDefinition activity = 5;
  .chesscom.user_properties.v1.SubscriptionPropertyDefinition subscription = 6;
  .chesscom.user_properti
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09836"></a>
## FND-09836: chesscom.user_properties.v1.Definitions.roles = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.RolesPropertyDefinition roles = 4;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 12180.

```text
efinition pii = 2;
  .chesscom.user_properties.v1.UserDetailsPropertyDefinition user_details = 3;
  .chesscom.user_properties.v1.RolesPropertyDefinition roles = 4;
  .chesscom.user_properties.v1.ActivityPropertyDefinition activity = 5;
  .chesscom.user_properties.v1.SubscriptionPropertyDefinition subscription = 6;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_signup_initial = 7;
  .chesscom
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09837"></a>
## FND-09837: chesscom.user_properties.v1.Definitions.activity = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.ActivityPropertyDefinition activity = 5;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 12246.

```text
rtyDefinition user_details = 3;
  .chesscom.user_properties.v1.RolesPropertyDefinition roles = 4;
  .chesscom.user_properties.v1.ActivityPropertyDefinition activity = 5;
  .chesscom.user_properties.v1.SubscriptionPropertyDefinition subscription = 6;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_signup_initial = 7;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_sign
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09838"></a>
## FND-09838: chesscom.user_properties.v1.Definitions.subscription = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.SubscriptionPropertyDefinition subscription = 6;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 12318.

```text
ertyDefinition roles = 4;
  .chesscom.user_properties.v1.ActivityPropertyDefinition activity = 5;
  .chesscom.user_properties.v1.SubscriptionPropertyDefinition subscription = 6;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_signup_initial = 7;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_signup_last = 8;
  .chesscom.user_properties.v1.AttributionPropertyDefinitio
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09839"></a>
## FND-09839: chesscom.user_properties.v1.Definitions.attribution_signup_initial = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AttributionPropertyDefinition attribution_signup_initial = 7;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 12398.

```text
ion activity = 5;
  .chesscom.user_properties.v1.SubscriptionPropertyDefinition subscription = 6;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_signup_initial = 7;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_signup_last = 8;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_trial_initial = 9;
  .chesscom.user_properties.v1.AttributionPrope
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09840"></a>
## FND-09840: chesscom.user_properties.v1.Definitions.attribution_signup_last = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AttributionPropertyDefinition attribution_signup_last = 8;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 12491.

```text
= 6;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_signup_initial = 7;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_signup_last = 8;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_trial_initial = 9;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_trial_last = 10;
  .chesscom.user_properties.v1.RatingsPropertyDefi
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09841"></a>
## FND-09841: chesscom.user_properties.v1.Definitions.attribution_trial_initial = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AttributionPropertyDefinition attribution_trial_initial = 9;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 12581.

```text
al = 7;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_signup_last = 8;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_trial_initial = 9;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_trial_last = 10;
  .chesscom.user_properties.v1.RatingsPropertyDefinition ratings = 11;
  .chesscom.user_properties.v1.WDLPropertyDefinition wdl = 12;
  .che
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09842"></a>
## FND-09842: chesscom.user_properties.v1.Definitions.attribution_trial_last = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AttributionPropertyDefinition attribution_trial_last = 10;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 12673.

```text
 = 8;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_trial_initial = 9;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_trial_last = 10;
  .chesscom.user_properties.v1.RatingsPropertyDefinition ratings = 11;
  .chesscom.user_properties.v1.WDLPropertyDefinition wdl = 12;
  .chesscom.user_properties.v1.AnalysisPropertyDefinition analysis = 13;
  .chesscom.user_properti
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09843"></a>
## FND-09843: chesscom.user_properties.v1.Definitions.ratings = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.RatingsPropertyDefinition ratings = 11;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 12763.

```text
al = 9;
  .chesscom.user_properties.v1.AttributionPropertyDefinition attribution_trial_last = 10;
  .chesscom.user_properties.v1.RatingsPropertyDefinition ratings = 11;
  .chesscom.user_properties.v1.WDLPropertyDefinition wdl = 12;
  .chesscom.user_properties.v1.AnalysisPropertyDefinition analysis = 13;
  .chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition settings_daily_chess = 14;
  .chesscom.user_pro
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09844"></a>
## FND-09844: chesscom.user_properties.v1.Definitions.wdl = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.WDLPropertyDefinition wdl = 12;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 12834.

```text
tribution_trial_last = 10;
  .chesscom.user_properties.v1.RatingsPropertyDefinition ratings = 11;
  .chesscom.user_properties.v1.WDLPropertyDefinition wdl = 12;
  .chesscom.user_properties.v1.AnalysisPropertyDefinition analysis = 13;
  .chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition settings_daily_chess = 14;
  .chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition settings_live_chess = 15
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09845"></a>
## FND-09845: chesscom.user_properties.v1.Definitions.analysis = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AnalysisPropertyDefinition analysis = 13;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 12897.

```text
gsPropertyDefinition ratings = 11;
  .chesscom.user_properties.v1.WDLPropertyDefinition wdl = 12;
  .chesscom.user_properties.v1.AnalysisPropertyDefinition analysis = 13;
  .chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition settings_daily_chess = 14;
  .chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition settings_live_chess = 15;
  .chesscom.user_properties.v1.StatsDailyPropertyDefinition s
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09846"></a>
## FND-09846: chesscom.user_properties.v1.Definitions.settings_daily_chess = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition settings_daily_chess = 14;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 12970.

```text
ertyDefinition wdl = 12;
  .chesscom.user_properties.v1.AnalysisPropertyDefinition analysis = 13;
  .chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition settings_daily_chess = 14;
  .chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition settings_live_chess = 15;
  .chesscom.user_properties.v1.StatsDailyPropertyDefinition stats_daily_chess = 16;
  .chesscom.user_properties.v1.StatsDailyChess960P
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09847"></a>
## FND-09847: chesscom.user_properties.v1.Definitions.settings_live_chess = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition settings_live_chess = 15;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 13065.

```text
3;
  .chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition settings_daily_chess = 14;
  .chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition settings_live_chess = 15;
  .chesscom.user_properties.v1.StatsDailyPropertyDefinition stats_daily_chess = 16;
  .chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition stats_daily_chess960 = 17;
  .chesscom.user_properties.v1.StatsLivePropertyDe
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09848"></a>
## FND-09848: chesscom.user_properties.v1.Definitions.stats_daily_chess = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsDailyPropertyDefinition stats_daily_chess = 16;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 13158.

```text
 14;
  .chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition settings_live_chess = 15;
  .chesscom.user_properties.v1.StatsDailyPropertyDefinition stats_daily_chess = 16;
  .chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition stats_daily_chess960 = 17;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_bullet = 18;
  .chesscom.user_properties.v1.StatsLivePropertyDefini
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09849"></a>
## FND-09849: chesscom.user_properties.v1.Definitions.stats_daily_chess960 = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition stats_daily_chess960 = 17;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 13242.

```text
e_chess = 15;
  .chesscom.user_properties.v1.StatsDailyPropertyDefinition stats_daily_chess = 16;
  .chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition stats_daily_chess960 = 17;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_bullet = 18;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_blitz = 19;
  .chesscom.user_properties.v1.StatsLivePropertyDe
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09850"></a>
## FND-09850: chesscom.user_properties.v1.Definitions.stats_live_chess_bullet = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_bullet = 18;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 13337.

```text
6;
  .chesscom.user_properties.v1.StatsDailyChess960PropertyDefinition stats_daily_chess960 = 17;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_bullet = 18;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_blitz = 19;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_rapid = 20;
  .chesscom.user_properties.v1.StatsLivePropertyDefinitio
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09851"></a>
## FND-09851: chesscom.user_properties.v1.Definitions.stats_live_chess_blitz = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_blitz = 19;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 13426.

```text
60 = 17;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_bullet = 18;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_blitz = 19;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_rapid = 20;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_bullet = 21;
  .chesscom.user_properties.v1.StatsLivePropertyDefini
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09852"></a>
## FND-09852: chesscom.user_properties.v1.Definitions.stats_live_chess_rapid = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_rapid = 20;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 13514.

```text
let = 18;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_blitz = 19;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_rapid = 20;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_bullet = 21;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_blitz = 22;
  .chesscom.user_properties.v1.StatsLivePropertyDef
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09853"></a>
## FND-09853: chesscom.user_properties.v1.Definitions.stats_live_chess960_bullet = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_bullet = 21;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 13602.

```text
itz = 19;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess_rapid = 20;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_bullet = 21;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_blitz = 22;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_rapid = 23;
  .chesscom.user_properties.v1.StatsLiveProperty
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09854"></a>
## FND-09854: chesscom.user_properties.v1.Definitions.stats_live_chess960_blitz = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_blitz = 22;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 13694.

```text
= 20;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_bullet = 21;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_blitz = 22;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_rapid = 23;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_bughouse = 24;
  .chesscom.user_properties.v1.UserSettingsPropertyDefi
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09855"></a>
## FND-09855: chesscom.user_properties.v1.Definitions.stats_live_chess960_rapid = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_rapid = 23;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 13785.

```text
 = 21;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_blitz = 22;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_rapid = 23;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_bughouse = 24;
  .chesscom.user_properties.v1.UserSettingsPropertyDefinition user_settings = 25;
  .chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinitio
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09856"></a>
## FND-09856: chesscom.user_properties.v1.Definitions.stats_live_bughouse = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_bughouse = 24;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 13876.

```text
 = 22;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_chess960_rapid = 23;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_bughouse = 24;
  .chesscom.user_properties.v1.UserSettingsPropertyDefinition user_settings = 25;
  .chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition puzzles_attempted = 26;
  .chesscom.user_properties.v1.ClubsPropertyDefinition clubs = 27
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09857"></a>
## FND-09857: chesscom.user_properties.v1.Definitions.user_settings = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.UserSettingsPropertyDefinition user_settings = 25;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 13961.

```text
_rapid = 23;
  .chesscom.user_properties.v1.StatsLivePropertyDefinition stats_live_bughouse = 24;
  .chesscom.user_properties.v1.UserSettingsPropertyDefinition user_settings = 25;
  .chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition puzzles_attempted = 26;
  .chesscom.user_properties.v1.ClubsPropertyDefinition clubs = 27;
  .chesscom.user_properties.v1.PuzzleBattlePropertyDefinition puzzle_battle = 28;
 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09858"></a>
## FND-09858: chesscom.user_properties.v1.Definitions.puzzles_attempted = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition puzzles_attempted = 26;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 14043.

```text
_bughouse = 24;
  .chesscom.user_properties.v1.UserSettingsPropertyDefinition user_settings = 25;
  .chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition puzzles_attempted = 26;
  .chesscom.user_properties.v1.ClubsPropertyDefinition clubs = 27;
  .chesscom.user_properties.v1.PuzzleBattlePropertyDefinition puzzle_battle = 28;
  .chesscom.user_properties.v1.AudiencesPropertyDefinition audiences = 29;
  .chess
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09859"></a>
## FND-09859: chesscom.user_properties.v1.Definitions.clubs = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.ClubsPropertyDefinition clubs = 27;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 14133.

```text
s = 25;
  .chesscom.user_properties.v1.PuzzlesAttemptedPropertyDefinition puzzles_attempted = 26;
  .chesscom.user_properties.v1.ClubsPropertyDefinition clubs = 27;
  .chesscom.user_properties.v1.PuzzleBattlePropertyDefinition puzzle_battle = 28;
  .chesscom.user_properties.v1.AudiencesPropertyDefinition audiences = 29;
  .chesscom.user_properties.v1.UserAbusePropertyDefinition user_abuse = 30;
  .chesscom.settings.v
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09860"></a>
## FND-09860: chesscom.user_properties.v1.Definitions.puzzle_battle = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PuzzleBattlePropertyDefinition puzzle_battle = 28;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 14200.

```text
nition puzzles_attempted = 26;
  .chesscom.user_properties.v1.ClubsPropertyDefinition clubs = 27;
  .chesscom.user_properties.v1.PuzzleBattlePropertyDefinition puzzle_battle = 28;
  .chesscom.user_properties.v1.AudiencesPropertyDefinition audiences = 29;
  .chesscom.user_properties.v1.UserAbusePropertyDefinition user_abuse = 30;
  .chesscom.settings.v1.Setting setting = 31;
  .chesscom.user_properties.v1.DailyPuzzles
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09861"></a>
## FND-09861: chesscom.user_properties.v1.Definitions.audiences = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AudiencesPropertyDefinition audiences = 29;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 14282.

```text
ion clubs = 27;
  .chesscom.user_properties.v1.PuzzleBattlePropertyDefinition puzzle_battle = 28;
  .chesscom.user_properties.v1.AudiencesPropertyDefinition audiences = 29;
  .chesscom.user_properties.v1.UserAbusePropertyDefinition user_abuse = 30;
  .chesscom.settings.v1.Setting setting = 31;
  .chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition daily_puzzles_solved = 32;
  .chesscom.user_properties.v1
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09862"></a>
## FND-09862: chesscom.user_properties.v1.Definitions.user_abuse = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.UserAbusePropertyDefinition user_abuse = 30;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 14357.

```text
on puzzle_battle = 28;
  .chesscom.user_properties.v1.AudiencesPropertyDefinition audiences = 29;
  .chesscom.user_properties.v1.UserAbusePropertyDefinition user_abuse = 30;
  .chesscom.settings.v1.Setting setting = 31;
  .chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition daily_puzzles_solved = 32;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_chess = 33;
  .chesscom.user_prope
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09863"></a>
## FND-09863: chesscom.user_properties.v1.Definitions.setting = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.Setting setting = 31;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 14433.

```text
ition audiences = 29;
  .chesscom.user_properties.v1.UserAbusePropertyDefinition user_abuse = 30;
  .chesscom.settings.v1.Setting setting = 31;
  .chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition daily_puzzles_solved = 32;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_chess = 33;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_chess960 = 34;
  .chesscom.
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09864"></a>
## FND-09864: chesscom.user_properties.v1.Definitions.daily_puzzles_solved = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition daily_puzzles_solved = 32;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 14479.

```text
ies.v1.UserAbusePropertyDefinition user_abuse = 30;
  .chesscom.settings.v1.Setting setting = 31;
  .chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition daily_puzzles_solved = 32;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_chess = 33;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_chess960 = 34;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09865"></a>
## FND-09865: chesscom.user_properties.v1.Definitions.play_bullet_chess = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_chess = 33;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 14574.

```text
1;
  .chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition daily_puzzles_solved = 32;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_chess = 33;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_chess960 = 34;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_bughouse = 35;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bul
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09866"></a>
## FND-09866: chesscom.user_properties.v1.Definitions.play_bullet_chess960 = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_chess960 = 34;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 14657.

```text
s_solved = 32;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_chess = 33;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_chess960 = 34;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_bughouse = 35;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_threecheck = 36;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition pla
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09867"></a>
## FND-09867: chesscom.user_properties.v1.Definitions.play_bullet_bughouse = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_bughouse = 35;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 14743.

```text
chess = 33;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_chess960 = 34;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_bughouse = 35;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_threecheck = 36;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_crazyhouse = 37;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition p
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09868"></a>
## FND-09868: chesscom.user_properties.v1.Definitions.play_bullet_threecheck = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_threecheck = 36;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 14829.

```text
ss960 = 34;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_bughouse = 35;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_threecheck = 36;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_crazyhouse = 37;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_kingofthehill = 38;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinit
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09869"></a>
## FND-09869: chesscom.user_properties.v1.Definitions.play_bullet_crazyhouse = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_crazyhouse = 37;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 14917.

```text
use = 35;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_threecheck = 36;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_crazyhouse = 37;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_kingofthehill = 38;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_oddschess = 39;
  .chesscom.user_properties.v1.PlayStatsPropertyDefiniti
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09870"></a>
## FND-09870: chesscom.user_properties.v1.Definitions.play_bullet_kingofthehill = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_kingofthehill = 38;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 15005.

```text
eck = 36;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_crazyhouse = 37;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_kingofthehill = 38;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_oddschess = 39;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_chess = 40;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition pla
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09871"></a>
## FND-09871: chesscom.user_properties.v1.Definitions.play_bullet_oddschess = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_oddschess = 39;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 15096.

```text
 = 37;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_kingofthehill = 38;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_oddschess = 39;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_chess = 40;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_chess960 = 41;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blit
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09872"></a>
## FND-09872: chesscom.user_properties.v1.Definitions.play_blitz_chess = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_chess = 40;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 15183.

```text
hill = 38;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_bullet_oddschess = 39;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_chess = 40;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_chess960 = 41;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_bughouse = 42;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09873"></a>
## FND-09873: chesscom.user_properties.v1.Definitions.play_blitz_chess960 = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_chess960 = 41;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 15265.

```text
oddschess = 39;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_chess = 40;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_chess960 = 41;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_bughouse = 42;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_threecheck = 43;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_b
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09874"></a>
## FND-09874: chesscom.user_properties.v1.Definitions.play_blitz_bughouse = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_bughouse = 42;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 15350.

```text
_chess = 40;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_chess960 = 41;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_bughouse = 42;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_threecheck = 43;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play_blitz_crazyhouse = 44;
  .chesscom.user_properties.v1.PlayStatsPropertyDefinition play
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
