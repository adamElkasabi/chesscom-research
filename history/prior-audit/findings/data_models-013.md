# data_models — findings 1201–1300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-01475"></a>
## FND-01475: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_HOME = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_HOME = 14;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 668.

```text
E_DEEPLINK = 11;
  COACH_SWITCH_SOURCE_WELCOME_MODAL = 12;
  COACH_SWITCH_SOURCE_ONBOARDING = 13;
  COACH_SWITCH_SOURCE_HOME = 14;
  COACH_SWITCH_SOURCE_TRAIN = 15;
}

enum CoachTaglineUi {
  COACH_TAGLINE_UI_UNSPECIFIED = 0;
  COACH_TAGLINE_UI_CHOOSE_COACH_MODAL = 1;
  COACH_TAGLINE_UI_SIGNUP_CHOOSE_COACH_STEP = 2;
  COACH_TAGLINE_UI_SELECT_COACH_SETTINGS = 3;
}

enum PlayCoachOpenedSource {
  PLAY_COACH_OPENED_SOUR
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01476"></a>
## FND-01476: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_TRAIN = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_TRAIN = 15;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 701.

```text
OURCE_WELCOME_MODAL = 12;
  COACH_SWITCH_SOURCE_ONBOARDING = 13;
  COACH_SWITCH_SOURCE_HOME = 14;
  COACH_SWITCH_SOURCE_TRAIN = 15;
}

enum CoachTaglineUi {
  COACH_TAGLINE_UI_UNSPECIFIED = 0;
  COACH_TAGLINE_UI_CHOOSE_COACH_MODAL = 1;
  COACH_TAGLINE_UI_SIGNUP_CHOOSE_COACH_STEP = 2;
  COACH_TAGLINE_UI_SELECT_COACH_SETTINGS = 3;
}

enum PlayCoachOpenedSource {
  PLAY_COACH_OPENED_SOURCE_UNSPECIFIED = 0;
  PLAY_COACH_
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01477"></a>
## FND-01477: enum declaration: chesscom.coaches.v2.CoachTaglineUi

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CoachTaglineUi {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 736.

```text
WITCH_SOURCE_ONBOARDING = 13;
  COACH_SWITCH_SOURCE_HOME = 14;
  COACH_SWITCH_SOURCE_TRAIN = 15;
}

enum CoachTaglineUi {
  COACH_TAGLINE_UI_UNSPECIFIED = 0;
  COACH_TAGLINE_UI_CHOOSE_COACH_MODAL = 1;
  COACH_TAGLINE_UI_SIGNUP_CHOOSE_COACH_STEP = 2;
  COACH_TAGLINE_UI_SELECT_COACH_SETTINGS = 3;
}

enum PlayCoachOpenedSource {
  PLAY_COACH_OPENED_SOURCE_UNSPECIFIED = 0;
  PLAY_COACH_OPENED_SOURCE_PLAY_ROOT = 1;
  PLAY
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01478"></a>
## FND-01478: chesscom.coaches.v2.CoachTaglineUi.COACH_TAGLINE_UI_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_TAGLINE_UI_UNSPECIFIED = 0;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 760.

```text
= 13;
  COACH_SWITCH_SOURCE_HOME = 14;
  COACH_SWITCH_SOURCE_TRAIN = 15;
}

enum CoachTaglineUi {
  COACH_TAGLINE_UI_UNSPECIFIED = 0;
  COACH_TAGLINE_UI_CHOOSE_COACH_MODAL = 1;
  COACH_TAGLINE_UI_SIGNUP_CHOOSE_COACH_STEP = 2;
  COACH_TAGLINE_UI_SELECT_COACH_SETTINGS = 3;
}

enum PlayCoachOpenedSource {
  PLAY_COACH_OPENED_SOURCE_UNSPECIFIED = 0;
  PLAY_COACH_OPENED_SOURCE_PLAY_ROOT = 1;
  PLAY_COACH_OPENED_SOURCE_HOM
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01479"></a>
## FND-01479: chesscom.coaches.v2.CoachTaglineUi.COACH_TAGLINE_UI_CHOOSE_COACH_MODAL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_TAGLINE_UI_CHOOSE_COACH_MODAL = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 796.

```text
4;
  COACH_SWITCH_SOURCE_TRAIN = 15;
}

enum CoachTaglineUi {
  COACH_TAGLINE_UI_UNSPECIFIED = 0;
  COACH_TAGLINE_UI_CHOOSE_COACH_MODAL = 1;
  COACH_TAGLINE_UI_SIGNUP_CHOOSE_COACH_STEP = 2;
  COACH_TAGLINE_UI_SELECT_COACH_SETTINGS = 3;
}

enum PlayCoachOpenedSource {
  PLAY_COACH_OPENED_SOURCE_UNSPECIFIED = 0;
  PLAY_COACH_OPENED_SOURCE_PLAY_ROOT = 1;
  PLAY_COACH_OPENED_SOURCE_HOME = 2;
  PLAY_COACH_OPENED_SOURCE_LE
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01480"></a>
## FND-01480: chesscom.coaches.v2.CoachTaglineUi.COACH_TAGLINE_UI_SIGNUP_CHOOSE_COACH_STEP = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_TAGLINE_UI_SIGNUP_CHOOSE_COACH_STEP = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 839.

```text
m CoachTaglineUi {
  COACH_TAGLINE_UI_UNSPECIFIED = 0;
  COACH_TAGLINE_UI_CHOOSE_COACH_MODAL = 1;
  COACH_TAGLINE_UI_SIGNUP_CHOOSE_COACH_STEP = 2;
  COACH_TAGLINE_UI_SELECT_COACH_SETTINGS = 3;
}

enum PlayCoachOpenedSource {
  PLAY_COACH_OPENED_SOURCE_UNSPECIFIED = 0;
  PLAY_COACH_OPENED_SOURCE_PLAY_ROOT = 1;
  PLAY_COACH_OPENED_SOURCE_HOME = 2;
  PLAY_COACH_OPENED_SOURCE_LEARN_ROOT = 3;
  PLAY_COACH_OPENED_SOURCE_LE
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01481"></a>
## FND-01481: chesscom.coaches.v2.CoachTaglineUi.COACH_TAGLINE_UI_SELECT_COACH_SETTINGS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_TAGLINE_UI_SELECT_COACH_SETTINGS = 3;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 888.

```text
 = 0;
  COACH_TAGLINE_UI_CHOOSE_COACH_MODAL = 1;
  COACH_TAGLINE_UI_SIGNUP_CHOOSE_COACH_STEP = 2;
  COACH_TAGLINE_UI_SELECT_COACH_SETTINGS = 3;
}

enum PlayCoachOpenedSource {
  PLAY_COACH_OPENED_SOURCE_UNSPECIFIED = 0;
  PLAY_COACH_OPENED_SOURCE_PLAY_ROOT = 1;
  PLAY_COACH_OPENED_SOURCE_HOME = 2;
  PLAY_COACH_OPENED_SOURCE_LEARN_ROOT = 3;
  PLAY_COACH_OPENED_SOURCE_LEARN_NAV = 4;
  PLAY_COACH_OPENED_SOURCE_PLAY_NAV 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01482"></a>
## FND-01482: enum declaration: chesscom.coaches.v2.PlayCoachOpenedSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayCoachOpenedSource {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 935.

```text
;
  COACH_TAGLINE_UI_SIGNUP_CHOOSE_COACH_STEP = 2;
  COACH_TAGLINE_UI_SELECT_COACH_SETTINGS = 3;
}

enum PlayCoachOpenedSource {
  PLAY_COACH_OPENED_SOURCE_UNSPECIFIED = 0;
  PLAY_COACH_OPENED_SOURCE_PLAY_ROOT = 1;
  PLAY_COACH_OPENED_SOURCE_HOME = 2;
  PLAY_COACH_OPENED_SOURCE_LEARN_ROOT = 3;
  PLAY_COACH_OPENED_SOURCE_LEARN_NAV = 4;
  PLAY_COACH_OPENED_SOURCE_PLAY_NAV = 5;
}

enum PlayCoachAssistanceSetting {
  PLA
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01483"></a>
## FND-01483: chesscom.coaches.v2.PlayCoachOpenedSource.PLAY_COACH_OPENED_SOURCE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_OPENED_SOURCE_UNSPECIFIED = 0;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 966.

```text
OSE_COACH_STEP = 2;
  COACH_TAGLINE_UI_SELECT_COACH_SETTINGS = 3;
}

enum PlayCoachOpenedSource {
  PLAY_COACH_OPENED_SOURCE_UNSPECIFIED = 0;
  PLAY_COACH_OPENED_SOURCE_PLAY_ROOT = 1;
  PLAY_COACH_OPENED_SOURCE_HOME = 2;
  PLAY_COACH_OPENED_SOURCE_LEARN_ROOT = 3;
  PLAY_COACH_OPENED_SOURCE_LEARN_NAV = 4;
  PLAY_COACH_OPENED_SOURCE_PLAY_NAV = 5;
}

enum PlayCoachAssistanceSetting {
  PLAY_COACH_ASSISTANCE_SETTING_UNSP
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01484"></a>
## FND-01484: chesscom.coaches.v2.PlayCoachOpenedSource.PLAY_COACH_OPENED_SOURCE_PLAY_ROOT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_OPENED_SOURCE_PLAY_ROOT = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1010.

```text
T_COACH_SETTINGS = 3;
}

enum PlayCoachOpenedSource {
  PLAY_COACH_OPENED_SOURCE_UNSPECIFIED = 0;
  PLAY_COACH_OPENED_SOURCE_PLAY_ROOT = 1;
  PLAY_COACH_OPENED_SOURCE_HOME = 2;
  PLAY_COACH_OPENED_SOURCE_LEARN_ROOT = 3;
  PLAY_COACH_OPENED_SOURCE_LEARN_NAV = 4;
  PLAY_COACH_OPENED_SOURCE_PLAY_NAV = 5;
}

enum PlayCoachAssistanceSetting {
  PLAY_COACH_ASSISTANCE_SETTING_UNSPECIFIED = 0;
  PLAY_COACH_ASSISTANCE_SETTING
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01485"></a>
## FND-01485: chesscom.coaches.v2.PlayCoachOpenedSource.PLAY_COACH_OPENED_SOURCE_HOME = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_OPENED_SOURCE_HOME = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1052.

```text
nedSource {
  PLAY_COACH_OPENED_SOURCE_UNSPECIFIED = 0;
  PLAY_COACH_OPENED_SOURCE_PLAY_ROOT = 1;
  PLAY_COACH_OPENED_SOURCE_HOME = 2;
  PLAY_COACH_OPENED_SOURCE_LEARN_ROOT = 3;
  PLAY_COACH_OPENED_SOURCE_LEARN_NAV = 4;
  PLAY_COACH_OPENED_SOURCE_PLAY_NAV = 5;
}

enum PlayCoachAssistanceSetting {
  PLAY_COACH_ASSISTANCE_SETTING_UNSPECIFIED = 0;
  PLAY_COACH_ASSISTANCE_SETTING_SUGGESTION_ARROWS = 1;
  PLAY_COACH_ASSIS
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01486"></a>
## FND-01486: chesscom.coaches.v2.PlayCoachOpenedSource.PLAY_COACH_OPENED_SOURCE_LEARN_ROOT = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_OPENED_SOURCE_LEARN_ROOT = 3;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1089.

```text
E_UNSPECIFIED = 0;
  PLAY_COACH_OPENED_SOURCE_PLAY_ROOT = 1;
  PLAY_COACH_OPENED_SOURCE_HOME = 2;
  PLAY_COACH_OPENED_SOURCE_LEARN_ROOT = 3;
  PLAY_COACH_OPENED_SOURCE_LEARN_NAV = 4;
  PLAY_COACH_OPENED_SOURCE_PLAY_NAV = 5;
}

enum PlayCoachAssistanceSetting {
  PLAY_COACH_ASSISTANCE_SETTING_UNSPECIFIED = 0;
  PLAY_COACH_ASSISTANCE_SETTING_SUGGESTION_ARROWS = 1;
  PLAY_COACH_ASSISTANCE_SETTING_THREAT_ARROWS = 2;
  PL
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01487"></a>
## FND-01487: chesscom.coaches.v2.PlayCoachOpenedSource.PLAY_COACH_OPENED_SOURCE_LEARN_NAV = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_OPENED_SOURCE_LEARN_NAV = 4;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1132.

```text
CE_PLAY_ROOT = 1;
  PLAY_COACH_OPENED_SOURCE_HOME = 2;
  PLAY_COACH_OPENED_SOURCE_LEARN_ROOT = 3;
  PLAY_COACH_OPENED_SOURCE_LEARN_NAV = 4;
  PLAY_COACH_OPENED_SOURCE_PLAY_NAV = 5;
}

enum PlayCoachAssistanceSetting {
  PLAY_COACH_ASSISTANCE_SETTING_UNSPECIFIED = 0;
  PLAY_COACH_ASSISTANCE_SETTING_SUGGESTION_ARROWS = 1;
  PLAY_COACH_ASSISTANCE_SETTING_THREAT_ARROWS = 2;
  PLAY_COACH_ASSISTANCE_SETTING_EVALUATION_BAR 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01488"></a>
## FND-01488: chesscom.coaches.v2.PlayCoachOpenedSource.PLAY_COACH_OPENED_SOURCE_PLAY_NAV = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_OPENED_SOURCE_PLAY_NAV = 5;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1174.

```text
CE_HOME = 2;
  PLAY_COACH_OPENED_SOURCE_LEARN_ROOT = 3;
  PLAY_COACH_OPENED_SOURCE_LEARN_NAV = 4;
  PLAY_COACH_OPENED_SOURCE_PLAY_NAV = 5;
}

enum PlayCoachAssistanceSetting {
  PLAY_COACH_ASSISTANCE_SETTING_UNSPECIFIED = 0;
  PLAY_COACH_ASSISTANCE_SETTING_SUGGESTION_ARROWS = 1;
  PLAY_COACH_ASSISTANCE_SETTING_THREAT_ARROWS = 2;
  PLAY_COACH_ASSISTANCE_SETTING_EVALUATION_BAR = 3;
  PLAY_COACH_ASSISTANCE_SETTING_MOVE_
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01489"></a>
## FND-01489: enum declaration: chesscom.coaches.v2.PlayCoachAssistanceSetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayCoachAssistanceSetting {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1216.

```text
ARN_ROOT = 3;
  PLAY_COACH_OPENED_SOURCE_LEARN_NAV = 4;
  PLAY_COACH_OPENED_SOURCE_PLAY_NAV = 5;
}

enum PlayCoachAssistanceSetting {
  PLAY_COACH_ASSISTANCE_SETTING_UNSPECIFIED = 0;
  PLAY_COACH_ASSISTANCE_SETTING_SUGGESTION_ARROWS = 1;
  PLAY_COACH_ASSISTANCE_SETTING_THREAT_ARROWS = 2;
  PLAY_COACH_ASSISTANCE_SETTING_EVALUATION_BAR = 3;
  PLAY_COACH_ASSISTANCE_SETTING_MOVE_FEEDBACK = 4;
  PLAY_COACH_ASSISTANCE_SETT
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01490"></a>
## FND-01490: chesscom.coaches.v2.PlayCoachAssistanceSetting.PLAY_COACH_ASSISTANCE_SETTING_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_ASSISTANCE_SETTING_UNSPECIFIED = 0;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1252.

```text
URCE_LEARN_NAV = 4;
  PLAY_COACH_OPENED_SOURCE_PLAY_NAV = 5;
}

enum PlayCoachAssistanceSetting {
  PLAY_COACH_ASSISTANCE_SETTING_UNSPECIFIED = 0;
  PLAY_COACH_ASSISTANCE_SETTING_SUGGESTION_ARROWS = 1;
  PLAY_COACH_ASSISTANCE_SETTING_THREAT_ARROWS = 2;
  PLAY_COACH_ASSISTANCE_SETTING_EVALUATION_BAR = 3;
  PLAY_COACH_ASSISTANCE_SETTING_MOVE_FEEDBACK = 4;
  PLAY_COACH_ASSISTANCE_SETTING_AUTO_HINTS = 5;
}

enum PlayCoac
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01491"></a>
## FND-01491: chesscom.coaches.v2.PlayCoachAssistanceSetting.PLAY_COACH_ASSISTANCE_SETTING_SUGGESTION_ARROWS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_ASSISTANCE_SETTING_SUGGESTION_ARROWS = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1301.

```text
AY_NAV = 5;
}

enum PlayCoachAssistanceSetting {
  PLAY_COACH_ASSISTANCE_SETTING_UNSPECIFIED = 0;
  PLAY_COACH_ASSISTANCE_SETTING_SUGGESTION_ARROWS = 1;
  PLAY_COACH_ASSISTANCE_SETTING_THREAT_ARROWS = 2;
  PLAY_COACH_ASSISTANCE_SETTING_EVALUATION_BAR = 3;
  PLAY_COACH_ASSISTANCE_SETTING_MOVE_FEEDBACK = 4;
  PLAY_COACH_ASSISTANCE_SETTING_AUTO_HINTS = 5;
}

enum PlayCoachHint {
  PLAY_COACH_HINT_UNSPECIFIED = 0;
  PLAY
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01492"></a>
## FND-01492: chesscom.coaches.v2.PlayCoachAssistanceSetting.PLAY_COACH_ASSISTANCE_SETTING_THREAT_ARROWS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_ASSISTANCE_SETTING_THREAT_ARROWS = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1356.

```text
_COACH_ASSISTANCE_SETTING_UNSPECIFIED = 0;
  PLAY_COACH_ASSISTANCE_SETTING_SUGGESTION_ARROWS = 1;
  PLAY_COACH_ASSISTANCE_SETTING_THREAT_ARROWS = 2;
  PLAY_COACH_ASSISTANCE_SETTING_EVALUATION_BAR = 3;
  PLAY_COACH_ASSISTANCE_SETTING_MOVE_FEEDBACK = 4;
  PLAY_COACH_ASSISTANCE_SETTING_AUTO_HINTS = 5;
}

enum PlayCoachHint {
  PLAY_COACH_HINT_UNSPECIFIED = 0;
  PLAY_COACH_HINT_SPEECH = 1;
  PLAY_COACH_HINT_HIGHLIGHTED_S
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01493"></a>
## FND-01493: chesscom.coaches.v2.PlayCoachAssistanceSetting.PLAY_COACH_ASSISTANCE_SETTING_EVALUATION_BAR = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_ASSISTANCE_SETTING_EVALUATION_BAR = 3;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1407.

```text
OACH_ASSISTANCE_SETTING_SUGGESTION_ARROWS = 1;
  PLAY_COACH_ASSISTANCE_SETTING_THREAT_ARROWS = 2;
  PLAY_COACH_ASSISTANCE_SETTING_EVALUATION_BAR = 3;
  PLAY_COACH_ASSISTANCE_SETTING_MOVE_FEEDBACK = 4;
  PLAY_COACH_ASSISTANCE_SETTING_AUTO_HINTS = 5;
}

enum PlayCoachHint {
  PLAY_COACH_HINT_UNSPECIFIED = 0;
  PLAY_COACH_HINT_SPEECH = 1;
  PLAY_COACH_HINT_HIGHLIGHTED_SQUARE = 2;
  PLAY_COACH_HINT_BEST_MOVE = 3;
}

enum
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01494"></a>
## FND-01494: chesscom.coaches.v2.PlayCoachAssistanceSetting.PLAY_COACH_ASSISTANCE_SETTING_MOVE_FEEDBACK = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_ASSISTANCE_SETTING_MOVE_FEEDBACK = 4;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1459.

```text
Y_COACH_ASSISTANCE_SETTING_THREAT_ARROWS = 2;
  PLAY_COACH_ASSISTANCE_SETTING_EVALUATION_BAR = 3;
  PLAY_COACH_ASSISTANCE_SETTING_MOVE_FEEDBACK = 4;
  PLAY_COACH_ASSISTANCE_SETTING_AUTO_HINTS = 5;
}

enum PlayCoachHint {
  PLAY_COACH_HINT_UNSPECIFIED = 0;
  PLAY_COACH_HINT_SPEECH = 1;
  PLAY_COACH_HINT_HIGHLIGHTED_SQUARE = 2;
  PLAY_COACH_HINT_BEST_MOVE = 3;
}

enum CoachMistakeWarningChoice {
  COACH_MISTAKE_WARNING
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01495"></a>
## FND-01495: chesscom.coaches.v2.PlayCoachAssistanceSetting.PLAY_COACH_ASSISTANCE_SETTING_AUTO_HINTS = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_ASSISTANCE_SETTING_AUTO_HINTS = 5;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1510.

```text
Y_COACH_ASSISTANCE_SETTING_EVALUATION_BAR = 3;
  PLAY_COACH_ASSISTANCE_SETTING_MOVE_FEEDBACK = 4;
  PLAY_COACH_ASSISTANCE_SETTING_AUTO_HINTS = 5;
}

enum PlayCoachHint {
  PLAY_COACH_HINT_UNSPECIFIED = 0;
  PLAY_COACH_HINT_SPEECH = 1;
  PLAY_COACH_HINT_HIGHLIGHTED_SQUARE = 2;
  PLAY_COACH_HINT_BEST_MOVE = 3;
}

enum CoachMistakeWarningChoice {
  COACH_MISTAKE_WARNING_CHOICE_UNSPECIFIED = 0;
  COACH_MISTAKE_WARNING_CH
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01496"></a>
## FND-01496: enum declaration: chesscom.coaches.v2.PlayCoachHint

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayCoachHint {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1559.

```text
PLAY_COACH_ASSISTANCE_SETTING_MOVE_FEEDBACK = 4;
  PLAY_COACH_ASSISTANCE_SETTING_AUTO_HINTS = 5;
}

enum PlayCoachHint {
  PLAY_COACH_HINT_UNSPECIFIED = 0;
  PLAY_COACH_HINT_SPEECH = 1;
  PLAY_COACH_HINT_HIGHLIGHTED_SQUARE = 2;
  PLAY_COACH_HINT_BEST_MOVE = 3;
}

enum CoachMistakeWarningChoice {
  COACH_MISTAKE_WARNING_CHOICE_UNSPECIFIED = 0;
  COACH_MISTAKE_WARNING_CHOICE_RETRY = 1;
  COACH_MISTAKE_WARNING_CHOICE_CO
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01497"></a>
## FND-01497: chesscom.coaches.v2.PlayCoachHint.PLAY_COACH_HINT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_HINT_UNSPECIFIED = 0;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1582.

```text
ETTING_MOVE_FEEDBACK = 4;
  PLAY_COACH_ASSISTANCE_SETTING_AUTO_HINTS = 5;
}

enum PlayCoachHint {
  PLAY_COACH_HINT_UNSPECIFIED = 0;
  PLAY_COACH_HINT_SPEECH = 1;
  PLAY_COACH_HINT_HIGHLIGHTED_SQUARE = 2;
  PLAY_COACH_HINT_BEST_MOVE = 3;
}

enum CoachMistakeWarningChoice {
  COACH_MISTAKE_WARNING_CHOICE_UNSPECIFIED = 0;
  COACH_MISTAKE_WARNING_CHOICE_RETRY = 1;
  COACH_MISTAKE_WARNING_CHOICE_CONTINUE = 2;
}

enum Coa
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01498"></a>
## FND-01498: chesscom.coaches.v2.PlayCoachHint.PLAY_COACH_HINT_SPEECH = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_HINT_SPEECH = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1617.

```text
ACH_ASSISTANCE_SETTING_AUTO_HINTS = 5;
}

enum PlayCoachHint {
  PLAY_COACH_HINT_UNSPECIFIED = 0;
  PLAY_COACH_HINT_SPEECH = 1;
  PLAY_COACH_HINT_HIGHLIGHTED_SQUARE = 2;
  PLAY_COACH_HINT_BEST_MOVE = 3;
}

enum CoachMistakeWarningChoice {
  COACH_MISTAKE_WARNING_CHOICE_UNSPECIFIED = 0;
  COACH_MISTAKE_WARNING_CHOICE_RETRY = 1;
  COACH_MISTAKE_WARNING_CHOICE_CONTINUE = 2;
}

enum CoachFlipBoardChoice {
  COACH_FLIP_BO
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01499"></a>
## FND-01499: chesscom.coaches.v2.PlayCoachHint.PLAY_COACH_HINT_HIGHLIGHTED_SQUARE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_HINT_HIGHLIGHTED_SQUARE = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1647.

```text
NTS = 5;
}

enum PlayCoachHint {
  PLAY_COACH_HINT_UNSPECIFIED = 0;
  PLAY_COACH_HINT_SPEECH = 1;
  PLAY_COACH_HINT_HIGHLIGHTED_SQUARE = 2;
  PLAY_COACH_HINT_BEST_MOVE = 3;
}

enum CoachMistakeWarningChoice {
  COACH_MISTAKE_WARNING_CHOICE_UNSPECIFIED = 0;
  COACH_MISTAKE_WARNING_CHOICE_RETRY = 1;
  COACH_MISTAKE_WARNING_CHOICE_CONTINUE = 2;
}

enum CoachFlipBoardChoice {
  COACH_FLIP_BOARD_CHOICE_UNSPECIFIED = 0;
  
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01500"></a>
## FND-01500: chesscom.coaches.v2.PlayCoachHint.PLAY_COACH_HINT_BEST_MOVE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_COACH_HINT_BEST_MOVE = 3;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1689.

```text
ACH_HINT_UNSPECIFIED = 0;
  PLAY_COACH_HINT_SPEECH = 1;
  PLAY_COACH_HINT_HIGHLIGHTED_SQUARE = 2;
  PLAY_COACH_HINT_BEST_MOVE = 3;
}

enum CoachMistakeWarningChoice {
  COACH_MISTAKE_WARNING_CHOICE_UNSPECIFIED = 0;
  COACH_MISTAKE_WARNING_CHOICE_RETRY = 1;
  COACH_MISTAKE_WARNING_CHOICE_CONTINUE = 2;
}

enum CoachFlipBoardChoice {
  COACH_FLIP_BOARD_CHOICE_UNSPECIFIED = 0;
  COACH_FLIP_BOARD_CHOICE_SWITCH_SIDES = 1;

```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01501"></a>
## FND-01501: enum declaration: chesscom.coaches.v2.CoachMistakeWarningChoice

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CoachMistakeWarningChoice {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1723.

```text
OACH_HINT_SPEECH = 1;
  PLAY_COACH_HINT_HIGHLIGHTED_SQUARE = 2;
  PLAY_COACH_HINT_BEST_MOVE = 3;
}

enum CoachMistakeWarningChoice {
  COACH_MISTAKE_WARNING_CHOICE_UNSPECIFIED = 0;
  COACH_MISTAKE_WARNING_CHOICE_RETRY = 1;
  COACH_MISTAKE_WARNING_CHOICE_CONTINUE = 2;
}

enum CoachFlipBoardChoice {
  COACH_FLIP_BOARD_CHOICE_UNSPECIFIED = 0;
  COACH_FLIP_BOARD_CHOICE_SWITCH_SIDES = 1;
  COACH_FLIP_BOARD_CHOICE_CONTINUE
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01502"></a>
## FND-01502: chesscom.coaches.v2.CoachMistakeWarningChoice.COACH_MISTAKE_WARNING_CHOICE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_MISTAKE_WARNING_CHOICE_UNSPECIFIED = 0;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1758.

```text
HINT_HIGHLIGHTED_SQUARE = 2;
  PLAY_COACH_HINT_BEST_MOVE = 3;
}

enum CoachMistakeWarningChoice {
  COACH_MISTAKE_WARNING_CHOICE_UNSPECIFIED = 0;
  COACH_MISTAKE_WARNING_CHOICE_RETRY = 1;
  COACH_MISTAKE_WARNING_CHOICE_CONTINUE = 2;
}

enum CoachFlipBoardChoice {
  COACH_FLIP_BOARD_CHOICE_UNSPECIFIED = 0;
  COACH_FLIP_BOARD_CHOICE_SWITCH_SIDES = 1;
  COACH_FLIP_BOARD_CHOICE_CONTINUE = 2;
}

enum GuidedCoachGameSource
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01503"></a>
## FND-01503: chesscom.coaches.v2.CoachMistakeWarningChoice.COACH_MISTAKE_WARNING_CHOICE_RETRY = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_MISTAKE_WARNING_CHOICE_RETRY = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1806.

```text
EST_MOVE = 3;
}

enum CoachMistakeWarningChoice {
  COACH_MISTAKE_WARNING_CHOICE_UNSPECIFIED = 0;
  COACH_MISTAKE_WARNING_CHOICE_RETRY = 1;
  COACH_MISTAKE_WARNING_CHOICE_CONTINUE = 2;
}

enum CoachFlipBoardChoice {
  COACH_FLIP_BOARD_CHOICE_UNSPECIFIED = 0;
  COACH_FLIP_BOARD_CHOICE_SWITCH_SIDES = 1;
  COACH_FLIP_BOARD_CHOICE_CONTINUE = 2;
}

enum GuidedCoachGameSource {
  GUIDED_COACH_GAME_SOURCE_UNSPECIFIED = 0;
 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01504"></a>
## FND-01504: chesscom.coaches.v2.CoachMistakeWarningChoice.COACH_MISTAKE_WARNING_CHOICE_CONTINUE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_MISTAKE_WARNING_CHOICE_CONTINUE = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1848.

```text
hoice {
  COACH_MISTAKE_WARNING_CHOICE_UNSPECIFIED = 0;
  COACH_MISTAKE_WARNING_CHOICE_RETRY = 1;
  COACH_MISTAKE_WARNING_CHOICE_CONTINUE = 2;
}

enum CoachFlipBoardChoice {
  COACH_FLIP_BOARD_CHOICE_UNSPECIFIED = 0;
  COACH_FLIP_BOARD_CHOICE_SWITCH_SIDES = 1;
  COACH_FLIP_BOARD_CHOICE_CONTINUE = 2;
}

enum GuidedCoachGameSource {
  GUIDED_COACH_GAME_SOURCE_UNSPECIFIED = 0;
  GUIDED_COACH_GAME_SOURCE_SIGNUP = 1;
  GU
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01505"></a>
## FND-01505: enum declaration: chesscom.coaches.v2.CoachFlipBoardChoice

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CoachFlipBoardChoice {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1894.

```text
FIED = 0;
  COACH_MISTAKE_WARNING_CHOICE_RETRY = 1;
  COACH_MISTAKE_WARNING_CHOICE_CONTINUE = 2;
}

enum CoachFlipBoardChoice {
  COACH_FLIP_BOARD_CHOICE_UNSPECIFIED = 0;
  COACH_FLIP_BOARD_CHOICE_SWITCH_SIDES = 1;
  COACH_FLIP_BOARD_CHOICE_CONTINUE = 2;
}

enum GuidedCoachGameSource {
  GUIDED_COACH_GAME_SOURCE_UNSPECIFIED = 0;
  GUIDED_COACH_GAME_SOURCE_SIGNUP = 1;
  GUIDED_COACH_GAME_SOURCE_PLAY_COACH_ENTRY = 2;
 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01506"></a>
## FND-01506: chesscom.coaches.v2.CoachFlipBoardChoice.COACH_FLIP_BOARD_CHOICE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_FLIP_BOARD_CHOICE_UNSPECIFIED = 0;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1924.

```text
ING_CHOICE_RETRY = 1;
  COACH_MISTAKE_WARNING_CHOICE_CONTINUE = 2;
}

enum CoachFlipBoardChoice {
  COACH_FLIP_BOARD_CHOICE_UNSPECIFIED = 0;
  COACH_FLIP_BOARD_CHOICE_SWITCH_SIDES = 1;
  COACH_FLIP_BOARD_CHOICE_CONTINUE = 2;
}

enum GuidedCoachGameSource {
  GUIDED_COACH_GAME_SOURCE_UNSPECIFIED = 0;
  GUIDED_COACH_GAME_SOURCE_SIGNUP = 1;
  GUIDED_COACH_GAME_SOURCE_PLAY_COACH_ENTRY = 2;
  GUIDED_COACH_GAME_SOURCE_REPL
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01507"></a>
## FND-01507: chesscom.coaches.v2.CoachFlipBoardChoice.COACH_FLIP_BOARD_CHOICE_SWITCH_SIDES = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_FLIP_BOARD_CHOICE_SWITCH_SIDES = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 1967.

```text
NG_CHOICE_CONTINUE = 2;
}

enum CoachFlipBoardChoice {
  COACH_FLIP_BOARD_CHOICE_UNSPECIFIED = 0;
  COACH_FLIP_BOARD_CHOICE_SWITCH_SIDES = 1;
  COACH_FLIP_BOARD_CHOICE_CONTINUE = 2;
}

enum GuidedCoachGameSource {
  GUIDED_COACH_GAME_SOURCE_UNSPECIFIED = 0;
  GUIDED_COACH_GAME_SOURCE_SIGNUP = 1;
  GUIDED_COACH_GAME_SOURCE_PLAY_COACH_ENTRY = 2;
  GUIDED_COACH_GAME_SOURCE_REPLAY = 3;
}

message CoachSwitched {
  option
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01508"></a>
## FND-01508: chesscom.coaches.v2.CoachFlipBoardChoice.COACH_FLIP_BOARD_CHOICE_CONTINUE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_FLIP_BOARD_CHOICE_CONTINUE = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2011.

```text
rdChoice {
  COACH_FLIP_BOARD_CHOICE_UNSPECIFIED = 0;
  COACH_FLIP_BOARD_CHOICE_SWITCH_SIDES = 1;
  COACH_FLIP_BOARD_CHOICE_CONTINUE = 2;
}

enum GuidedCoachGameSource {
  GUIDED_COACH_GAME_SOURCE_UNSPECIFIED = 0;
  GUIDED_COACH_GAME_SOURCE_SIGNUP = 1;
  GUIDED_COACH_GAME_SOURCE_PLAY_COACH_ENTRY = 2;
  GUIDED_COACH_GAME_SOURCE_REPLAY = 3;
}

message CoachSwitched {
  optional string new_coach_id = 1;
  optional .ches
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01509"></a>
## FND-01509: enum declaration: chesscom.coaches.v2.GuidedCoachGameSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GuidedCoachGameSource {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2052.

```text
ECIFIED = 0;
  COACH_FLIP_BOARD_CHOICE_SWITCH_SIDES = 1;
  COACH_FLIP_BOARD_CHOICE_CONTINUE = 2;
}

enum GuidedCoachGameSource {
  GUIDED_COACH_GAME_SOURCE_UNSPECIFIED = 0;
  GUIDED_COACH_GAME_SOURCE_SIGNUP = 1;
  GUIDED_COACH_GAME_SOURCE_PLAY_COACH_ENTRY = 2;
  GUIDED_COACH_GAME_SOURCE_REPLAY = 3;
}

message CoachSwitched {
  optional string new_coach_id = 1;
  optional .chesscom.coaches.v2.CoachSwitchSource source 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01510"></a>
## FND-01510: chesscom.coaches.v2.GuidedCoachGameSource.GUIDED_COACH_GAME_SOURCE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GUIDED_COACH_GAME_SOURCE_UNSPECIFIED = 0;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2083.

```text
_CHOICE_SWITCH_SIDES = 1;
  COACH_FLIP_BOARD_CHOICE_CONTINUE = 2;
}

enum GuidedCoachGameSource {
  GUIDED_COACH_GAME_SOURCE_UNSPECIFIED = 0;
  GUIDED_COACH_GAME_SOURCE_SIGNUP = 1;
  GUIDED_COACH_GAME_SOURCE_PLAY_COACH_ENTRY = 2;
  GUIDED_COACH_GAME_SOURCE_REPLAY = 3;
}

message CoachSwitched {
  optional string new_coach_id = 1;
  optional .chesscom.coaches.v2.CoachSwitchSource source = 2;
}

message ChooseYourCoach
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01511"></a>
## FND-01511: chesscom.coaches.v2.GuidedCoachGameSource.GUIDED_COACH_GAME_SOURCE_SIGNUP = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GUIDED_COACH_GAME_SOURCE_SIGNUP = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2127.

```text
_CHOICE_CONTINUE = 2;
}

enum GuidedCoachGameSource {
  GUIDED_COACH_GAME_SOURCE_UNSPECIFIED = 0;
  GUIDED_COACH_GAME_SOURCE_SIGNUP = 1;
  GUIDED_COACH_GAME_SOURCE_PLAY_COACH_ENTRY = 2;
  GUIDED_COACH_GAME_SOURCE_REPLAY = 3;
}

message CoachSwitched {
  optional string new_coach_id = 1;
  optional .chesscom.coaches.v2.CoachSwitchSource source = 2;
}

message ChooseYourCoachModalOpened {
  optional .chesscom.coaches.v
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01512"></a>
## FND-01512: chesscom.coaches.v2.GuidedCoachGameSource.GUIDED_COACH_GAME_SOURCE_PLAY_COACH_ENTRY = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GUIDED_COACH_GAME_SOURCE_PLAY_COACH_ENTRY = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2166.

```text
chGameSource {
  GUIDED_COACH_GAME_SOURCE_UNSPECIFIED = 0;
  GUIDED_COACH_GAME_SOURCE_SIGNUP = 1;
  GUIDED_COACH_GAME_SOURCE_PLAY_COACH_ENTRY = 2;
  GUIDED_COACH_GAME_SOURCE_REPLAY = 3;
}

message CoachSwitched {
  optional string new_coach_id = 1;
  optional .chesscom.coaches.v2.CoachSwitchSource source = 2;
}

message ChooseYourCoachModalOpened {
  optional .chesscom.coaches.v2.CoachSwitchSource source = 1;
}

mess
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01513"></a>
## FND-01513: chesscom.coaches.v2.GuidedCoachGameSource.GUIDED_COACH_GAME_SOURCE_REPLAY = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GUIDED_COACH_GAME_SOURCE_REPLAY = 3;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2215.

```text
FIED = 0;
  GUIDED_COACH_GAME_SOURCE_SIGNUP = 1;
  GUIDED_COACH_GAME_SOURCE_PLAY_COACH_ENTRY = 2;
  GUIDED_COACH_GAME_SOURCE_REPLAY = 3;
}

message CoachSwitched {
  optional string new_coach_id = 1;
  optional .chesscom.coaches.v2.CoachSwitchSource source = 2;
}

message ChooseYourCoachModalOpened {
  optional .chesscom.coaches.v2.CoachSwitchSource source = 1;
}

message CoachTaglineShown {
  optional string coach_i
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01514"></a>
## FND-01514: message declaration: chesscom.coaches.v2.CoachSwitched

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachSwitched {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2255.

```text
NUP = 1;
  GUIDED_COACH_GAME_SOURCE_PLAY_COACH_ENTRY = 2;
  GUIDED_COACH_GAME_SOURCE_REPLAY = 3;
}

message CoachSwitched {
  optional string new_coach_id = 1;
  optional .chesscom.coaches.v2.CoachSwitchSource source = 2;
}

message ChooseYourCoachModalOpened {
  optional .chesscom.coaches.v2.CoachSwitchSource source = 1;
}

message CoachTaglineShown {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.C
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01515"></a>
## FND-01515: chesscom.coaches.v2.CoachSwitched.new_coach_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string new_coach_id = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2281.

```text
ME_SOURCE_PLAY_COACH_ENTRY = 2;
  GUIDED_COACH_GAME_SOURCE_REPLAY = 3;
}

message CoachSwitched {
  optional string new_coach_id = 1;
  optional .chesscom.coaches.v2.CoachSwitchSource source = 2;
}

message ChooseYourCoachModalOpened {
  optional .chesscom.coaches.v2.CoachSwitchSource source = 1;
}

message CoachTaglineShown {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachTaglineUi coach_taglin
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01516"></a>
## FND-01516: chesscom.coaches.v2.CoachSwitched.source = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.CoachSwitchSource source = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2317.

```text
IDED_COACH_GAME_SOURCE_REPLAY = 3;
}

message CoachSwitched {
  optional string new_coach_id = 1;
  optional .chesscom.coaches.v2.CoachSwitchSource source = 2;
}

message ChooseYourCoachModalOpened {
  optional .chesscom.coaches.v2.CoachSwitchSource source = 1;
}

message CoachTaglineShown {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachTaglineUi coach_tagline_ui = 2;
}

message CoachWelcomeMod
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01517"></a>
## FND-01517: message declaration: chesscom.coaches.v2.ChooseYourCoachModalOpened

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ChooseYourCoachModalOpened {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2380.

```text
 optional string new_coach_id = 1;
  optional .chesscom.coaches.v2.CoachSwitchSource source = 2;
}

message ChooseYourCoachModalOpened {
  optional .chesscom.coaches.v2.CoachSwitchSource source = 1;
}

message CoachTaglineShown {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachTaglineUi coach_tagline_ui = 2;
}

message CoachWelcomeModalShown {
}

message PlayCoachOpened {
  optional .chesscom.coa
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01518"></a>
## FND-01518: chesscom.coaches.v2.ChooseYourCoachModalOpened.source = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.CoachSwitchSource source = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2419.

```text
tional .chesscom.coaches.v2.CoachSwitchSource source = 2;
}

message ChooseYourCoachModalOpened {
  optional .chesscom.coaches.v2.CoachSwitchSource source = 1;
}

message CoachTaglineShown {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachTaglineUi coach_tagline_ui = 2;
}

message CoachWelcomeModalShown {
}

message PlayCoachOpened {
  optional .chesscom.coaches.v2.PlayCoachOpenedSource source = 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01519"></a>
## FND-01519: message declaration: chesscom.coaches.v2.CoachTaglineShown

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachTaglineShown {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2482.

```text
ssage ChooseYourCoachModalOpened {
  optional .chesscom.coaches.v2.CoachSwitchSource source = 1;
}

message CoachTaglineShown {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachTaglineUi coach_tagline_ui = 2;
}

message CoachWelcomeModalShown {
}

message PlayCoachOpened {
  optional .chesscom.coaches.v2.PlayCoachOpenedSource source = 1;
}

message PlayCoachSettingChanged {
  optional .chesscom.co
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01520"></a>
## FND-01520: chesscom.coaches.v2.CoachTaglineShown.coach_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coach_id = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2512.

```text
ed {
  optional .chesscom.coaches.v2.CoachSwitchSource source = 1;
}

message CoachTaglineShown {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachTaglineUi coach_tagline_ui = 2;
}

message CoachWelcomeModalShown {
}

message PlayCoachOpened {
  optional .chesscom.coaches.v2.PlayCoachOpenedSource source = 1;
}

message PlayCoachSettingChanged {
  optional .chesscom.coaches.v2.PlayCoachAssistanceSe
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01521"></a>
## FND-01521: chesscom.coaches.v2.CoachTaglineShown.coach_tagline_ui = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.CoachTaglineUi coach_tagline_ui = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2544.

```text
s.v2.CoachSwitchSource source = 1;
}

message CoachTaglineShown {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachTaglineUi coach_tagline_ui = 2;
}

message CoachWelcomeModalShown {
}

message PlayCoachOpened {
  optional .chesscom.coaches.v2.PlayCoachOpenedSource source = 1;
}

message PlayCoachSettingChanged {
  optional .chesscom.coaches.v2.PlayCoachAssistanceSetting setting = 1;
  optional bo
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01522"></a>
## FND-01522: message declaration: chesscom.coaches.v2.CoachWelcomeModalShown

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachWelcomeModalShown {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2614.

```text
tional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachTaglineUi coach_tagline_ui = 2;
}

message CoachWelcomeModalShown {
}

message PlayCoachOpened {
  optional .chesscom.coaches.v2.PlayCoachOpenedSource source = 1;
}

message PlayCoachSettingChanged {
  optional .chesscom.coaches.v2.PlayCoachAssistanceSetting setting = 1;
  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string co
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01523"></a>
## FND-01523: message declaration: chesscom.coaches.v2.PlayCoachOpened

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayCoachOpened {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2650.

```text
al .chesscom.coaches.v2.CoachTaglineUi coach_tagline_ui = 2;
}

message CoachWelcomeModalShown {
}

message PlayCoachOpened {
  optional .chesscom.coaches.v2.PlayCoachOpenedSource source = 1;
}

message PlayCoachSettingChanged {
  optional .chesscom.coaches.v2.PlayCoachAssistanceSetting setting = 1;
  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01524"></a>
## FND-01524: chesscom.coaches.v2.PlayCoachOpened.source = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.PlayCoachOpenedSource source = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2678.

```text
hTaglineUi coach_tagline_ui = 2;
}

message CoachWelcomeModalShown {
}

message PlayCoachOpened {
  optional .chesscom.coaches.v2.PlayCoachOpenedSource source = 1;
}

message PlayCoachSettingChanged {
  optional .chesscom.coaches.v2.PlayCoachAssistanceSetting setting = 1;
  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .ches
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01525"></a>
## FND-01525: message declaration: chesscom.coaches.v2.PlayCoachSettingChanged

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayCoachSettingChanged {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2745.

```text
{
}

message PlayCoachOpened {
  optional .chesscom.coaches.v2.PlayCoachOpenedSource source = 1;
}

message PlayCoachSettingChanged {
  optional .chesscom.coaches.v2.PlayCoachAssistanceSetting setting = 1;
  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_sett
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01526"></a>
## FND-01526: chesscom.coaches.v2.PlayCoachSettingChanged.setting = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.PlayCoachAssistanceSetting setting = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2781.

```text
ional .chesscom.coaches.v2.PlayCoachOpenedSource source = 1;
}

message PlayCoachSettingChanged {
  optional .chesscom.coaches.v2.PlayCoachAssistanceSetting setting = 1;
  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_settings = 3;
  optional .chesscom.coach
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01527"></a>
## FND-01527: chesscom.coaches.v2.PlayCoachSettingChanged.enabled = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enabled = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2853.

```text
PlayCoachSettingChanged {
  optional .chesscom.coaches.v2.PlayCoachAssistanceSetting setting = 1;
  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_settings = 3;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 4;
}

message PlayCoachGame
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01528"></a>
## FND-01528: message declaration: chesscom.coaches.v2.PlayCoachGameStarted

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayCoachGameStarted {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2883.

```text
tional .chesscom.coaches.v2.PlayCoachAssistanceSetting setting = 1;
  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_settings = 3;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 4;
}

message PlayCoachGameCompleted {
  optional string 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01529"></a>
## FND-01529: chesscom.coaches.v2.PlayCoachGameStarted.coach_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coach_name = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2916.

```text
oachAssistanceSetting setting = 1;
  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_settings = 3;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 4;
}

message PlayCoachGameCompleted {
  optional string coach_name = 1;
  optional int32 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01530"></a>
## FND-01530: chesscom.coaches.v2.PlayCoachGameStarted.coach_level = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 coach_level = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2950.

```text

  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_settings = 3;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 4;
}

message PlayCoachGameCompleted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chess
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01531"></a>
## FND-01531: chesscom.coaches.v2.PlayCoachGameStarted.assistance_settings = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_settings = 3;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2984.

```text
essage PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_settings = 3;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 4;
}

message PlayCoachGameCompleted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.game_storage.v2.PlayerResult r
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01532"></a>
## FND-01532: chesscom.coaches.v2.PlayCoachGameStarted.finish_vs_coach = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 4;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3077.

```text
= 2;
  optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_settings = 3;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 4;
}

message PlayCoachGameCompleted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.game_storage.v2.PlayerResult result = 3;
  optional .chesscom.chess.v1.Result game_result = 4;
  optional .chesscom.chess.v
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01533"></a>
## FND-01533: message declaration: chesscom.coaches.v2.PlayCoachGameCompleted

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayCoachGameCompleted {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3152.

```text
sistance_settings = 3;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 4;
}

message PlayCoachGameCompleted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.game_storage.v2.PlayerResult result = 3;
  optional .chesscom.chess.v1.Result game_result = 4;
  optional .chesscom.chess.v1.ResultType game_result_type = 5;
  optional string bot_personality = 6;
 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01534"></a>
## FND-01534: chesscom.coaches.v2.PlayCoachGameCompleted.coach_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coach_name = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2916.

```text
oachAssistanceSetting setting = 1;
  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_settings = 3;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 4;
}

message PlayCoachGameCompleted {
  optional string coach_name = 1;
  optional int32 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01535"></a>
## FND-01535: chesscom.coaches.v2.PlayCoachGameCompleted.coach_level = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 coach_level = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2950.

```text

  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_settings = 3;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 4;
}

message PlayCoachGameCompleted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chess
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01536"></a>
## FND-01536: chesscom.coaches.v2.PlayCoachGameCompleted.result = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.PlayerResult result = 3;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3255.

```text
sage PlayCoachGameCompleted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.game_storage.v2.PlayerResult result = 3;
  optional .chesscom.chess.v1.Result game_result = 4;
  optional .chesscom.chess.v1.ResultType game_result_type = 5;
  optional string bot_personality = 6;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 7;
}

message PlayCoachHintReques
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01537"></a>
## FND-01537: chesscom.coaches.v2.PlayCoachGameCompleted.game_result = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Result game_result = 4;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3317.

```text
;
  optional int32 coach_level = 2;
  optional .chesscom.game_storage.v2.PlayerResult result = 3;
  optional .chesscom.chess.v1.Result game_result = 4;
  optional .chesscom.chess.v1.ResultType game_result_type = 5;
  optional string bot_personality = 6;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 7;
}

message PlayCoachHintRequested {
  optional string coach_name = 1;
  optional int32 coach
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01538"></a>
## FND-01538: chesscom.coaches.v2.PlayCoachGameCompleted.game_result_type = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.ResultType game_result_type = 5;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3371.

```text
om.game_storage.v2.PlayerResult result = 3;
  optional .chesscom.chess.v1.Result game_result = 4;
  optional .chesscom.chess.v1.ResultType game_result_type = 5;
  optional string bot_personality = 6;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 7;
}

message PlayCoachHintRequested {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional int32 stage = 3;
  optional .ch
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01539"></a>
## FND-01539: chesscom.coaches.v2.PlayCoachGameCompleted.bot_personality = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string bot_personality = 6;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3434.

```text
m.chess.v1.Result game_result = 4;
  optional .chesscom.chess.v1.ResultType game_result_type = 5;
  optional string bot_personality = 6;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 7;
}

message PlayCoachHintRequested {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional int32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
}

message PlayCoachH
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01540"></a>
## FND-01540: chesscom.coaches.v2.PlayCoachGameCompleted.finish_vs_coach = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 7;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3473.

```text
tional .chesscom.chess.v1.ResultType game_result_type = 5;
  optional string bot_personality = 6;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 7;
}

message PlayCoachHintRequested {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional int32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
}

message PlayCoachHintReceived {
  optional string coach_n
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01541"></a>
## FND-01541: message declaration: chesscom.coaches.v2.PlayCoachHintRequested

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayCoachHintRequested {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3548.

```text
g bot_personality = 6;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 7;
}

message PlayCoachHintRequested {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional int32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
}

message PlayCoachHintReceived {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional int32 stage = 3;
  op
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01542"></a>
## FND-01542: chesscom.coaches.v2.PlayCoachHintRequested.coach_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coach_name = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2916.

```text
oachAssistanceSetting setting = 1;
  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_settings = 3;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 4;
}

message PlayCoachGameCompleted {
  optional string coach_name = 1;
  optional int32 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01543"></a>
## FND-01543: chesscom.coaches.v2.PlayCoachHintRequested.coach_level = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 coach_level = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2950.

```text

  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_settings = 3;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 4;
}

message PlayCoachGameCompleted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chess
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01544"></a>
## FND-01544: chesscom.coaches.v2.PlayCoachHintRequested.stage = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 stage = 3;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3651.

```text
sage PlayCoachHintRequested {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional int32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
}

message PlayCoachHintReceived {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional int32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
  optional string fen = 5;
}

message PlayCoachMone
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01545"></a>
## FND-01545: chesscom.coaches.v2.PlayCoachHintRequested.type = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.PlayCoachHint type = 4;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3679.

```text
{
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional int32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
}

message PlayCoachHintReceived {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional int32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
  optional string fen = 5;
}

message PlayCoachMonetizationModalShowed {
}

mes
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01546"></a>
## FND-01546: message declaration: chesscom.coaches.v2.PlayCoachHintReceived

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayCoachHintReceived {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3736.

```text
h_level = 2;
  optional int32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
}

message PlayCoachHintReceived {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional int32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
  optional string fen = 5;
}

message PlayCoachMonetizationModalShowed {
}

message PlayCoachSignUpModalShowed {
}

message PlayCoachSig
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01547"></a>
## FND-01547: chesscom.coaches.v2.PlayCoachHintReceived.coach_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coach_name = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2916.

```text
oachAssistanceSetting setting = 1;
  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_settings = 3;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 4;
}

message PlayCoachGameCompleted {
  optional string coach_name = 1;
  optional int32 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01548"></a>
## FND-01548: chesscom.coaches.v2.PlayCoachHintReceived.coach_level = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 coach_level = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 2950.

```text

  optional bool enabled = 2;
}

message PlayCoachGameStarted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chesscom.coaches.v2.PlayCoachAssistanceSettingsSnapshot assistance_settings = 3;
  optional .chesscom.coaches.v2.FinishVsCoachContext finish_vs_coach = 4;
}

message PlayCoachGameCompleted {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional .chess
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01549"></a>
## FND-01549: chesscom.coaches.v2.PlayCoachHintReceived.stage = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 stage = 3;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3651.

```text
sage PlayCoachHintRequested {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional int32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
}

message PlayCoachHintReceived {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional int32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
  optional string fen = 5;
}

message PlayCoachMone
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01550"></a>
## FND-01550: chesscom.coaches.v2.PlayCoachHintReceived.type = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.PlayCoachHint type = 4;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3679.

```text
{
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional int32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
}

message PlayCoachHintReceived {
  optional string coach_name = 1;
  optional int32 coach_level = 2;
  optional int32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
  optional string fen = 5;
}

message PlayCoachMonetizationModalShowed {
}

mes
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01551"></a>
## FND-01551: chesscom.coaches.v2.PlayCoachHintReceived.fen = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string fen = 5;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3922.

```text
ch_level = 2;
  optional int32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
  optional string fen = 5;
}

message PlayCoachMonetizationModalShowed {
}

message PlayCoachSignUpModalShowed {
}

message PlayCoachSignUpModalCTATapped {
}

message CoachSettingsOpened {
}

message CoachCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedO
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01552"></a>
## FND-01552: message declaration: chesscom.coaches.v2.PlayCoachMonetizationModalShowed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayCoachMonetizationModalShowed {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3950.

```text
32 stage = 3;
  optional .chesscom.coaches.v2.PlayCoachHint type = 4;
  optional string fen = 5;
}

message PlayCoachMonetizationModalShowed {
}

message PlayCoachSignUpModalShowed {
}

message PlayCoachSignUpModalCTATapped {
}

message CoachSettingsOpened {
}

message CoachCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01553"></a>
## FND-01553: message declaration: chesscom.coaches.v2.PlayCoachSignUpModalShowed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayCoachSignUpModalShowed {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 3996.

```text
PlayCoachHint type = 4;
  optional string fen = 5;
}

message PlayCoachMonetizationModalShowed {
}

message PlayCoachSignUpModalShowed {
}

message PlayCoachSignUpModalCTATapped {
}

message CoachSettingsOpened {
}

message CoachCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string boardevent = 1;
}

message CoachMistakeWarnin
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01554"></a>
## FND-01554: message declaration: chesscom.coaches.v2.PlayCoachSignUpModalCTATapped

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayCoachSignUpModalCTATapped {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4036.

```text
g fen = 5;
}

message PlayCoachMonetizationModalShowed {
}

message PlayCoachSignUpModalShowed {
}

message PlayCoachSignUpModalCTATapped {
}

message CoachSettingsOpened {
}

message CoachCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string boardevent = 1;
}

message CoachMistakeWarningAnswered {
  optional string boardevent
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01555"></a>
## FND-01555: message declaration: chesscom.coaches.v2.CoachSettingsOpened

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachSettingsOpened {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4079.

```text
ModalShowed {
}

message PlayCoachSignUpModalShowed {
}

message PlayCoachSignUpModalCTATapped {
}

message CoachSettingsOpened {
}

message CoachCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string boardevent = 1;
}

message CoachMistakeWarningAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.Coach
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01556"></a>
## FND-01556: message declaration: chesscom.coaches.v2.CoachCouldWarnOfMistake

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachCouldWarnOfMistake {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4112.

```text
hSignUpModalShowed {
}

message PlayCoachSignUpModalCTATapped {
}

message CoachSettingsOpened {
}

message CoachCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string boardevent = 1;
}

message CoachMistakeWarningAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachMistakeWarningChoice choice = 2;

```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01557"></a>
## FND-01557: chesscom.coaches.v2.CoachCouldWarnOfMistake.boardevent = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string boardevent = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4148.

```text
CoachSignUpModalCTATapped {
}

message CoachSettingsOpened {
}

message CoachCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string boardevent = 1;
}

message CoachMistakeWarningAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachMistakeWarningChoice choice = 2;
}

message CoachFlipBoardOffered {
 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01558"></a>
## FND-01558: chesscom.coaches.v2.CoachCouldWarnOfMistake.cooldown_counter = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 cooldown_counter = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4182.

```text
sage CoachSettingsOpened {
}

message CoachCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string boardevent = 1;
}

message CoachMistakeWarningAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachMistakeWarningChoice choice = 2;
}

message CoachFlipBoardOffered {
  optional string boardevent = 1;
}
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01559"></a>
## FND-01559: message declaration: chesscom.coaches.v2.CoachWarnedOfMistake

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachWarnedOfMistake {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4222.

```text
achCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string boardevent = 1;
}

message CoachMistakeWarningAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachMistakeWarningChoice choice = 2;
}

message CoachFlipBoardOffered {
  optional string boardevent = 1;
}

message CoachFlipBoardAnswered {
  opt
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01560"></a>
## FND-01560: chesscom.coaches.v2.CoachWarnedOfMistake.boardevent = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string boardevent = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4148.

```text
CoachSignUpModalCTATapped {
}

message CoachSettingsOpened {
}

message CoachCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string boardevent = 1;
}

message CoachMistakeWarningAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachMistakeWarningChoice choice = 2;
}

message CoachFlipBoardOffered {
 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01561"></a>
## FND-01561: message declaration: chesscom.coaches.v2.CoachMistakeWarningAnswered

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachMistakeWarningAnswered {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4290.

```text
 int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string boardevent = 1;
}

message CoachMistakeWarningAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachMistakeWarningChoice choice = 2;
}

message CoachFlipBoardOffered {
  optional string boardevent = 1;
}

message CoachFlipBoardAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachFl
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01562"></a>
## FND-01562: chesscom.coaches.v2.CoachMistakeWarningAnswered.boardevent = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string boardevent = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4148.

```text
CoachSignUpModalCTATapped {
}

message CoachSettingsOpened {
}

message CoachCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string boardevent = 1;
}

message CoachMistakeWarningAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachMistakeWarningChoice choice = 2;
}

message CoachFlipBoardOffered {
 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01563"></a>
## FND-01563: chesscom.coaches.v2.CoachMistakeWarningAnswered.choice = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.CoachMistakeWarningChoice choice = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4364.

```text
string boardevent = 1;
}

message CoachMistakeWarningAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachMistakeWarningChoice choice = 2;
}

message CoachFlipBoardOffered {
  optional string boardevent = 1;
}

message CoachFlipBoardAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachFlipBoardChoice choice = 2;
}

message CoachFlipBoardExerciseCompleted {
  o
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01564"></a>
## FND-01564: message declaration: chesscom.coaches.v2.CoachFlipBoardOffered

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachFlipBoardOffered {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4435.

```text
nal string boardevent = 1;
  optional .chesscom.coaches.v2.CoachMistakeWarningChoice choice = 2;
}

message CoachFlipBoardOffered {
  optional string boardevent = 1;
}

message CoachFlipBoardAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachFlipBoardChoice choice = 2;
}

message CoachFlipBoardExerciseCompleted {
  optional string boardevent = 1;
  optional bool found_correct_move = 2;

```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01565"></a>
## FND-01565: chesscom.coaches.v2.CoachFlipBoardOffered.boardevent = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string boardevent = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4148.

```text
CoachSignUpModalCTATapped {
}

message CoachSettingsOpened {
}

message CoachCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string boardevent = 1;
}

message CoachMistakeWarningAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachMistakeWarningChoice choice = 2;
}

message CoachFlipBoardOffered {
 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01566"></a>
## FND-01566: message declaration: chesscom.coaches.v2.CoachFlipBoardAnswered

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachFlipBoardAnswered {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4504.

```text
keWarningChoice choice = 2;
}

message CoachFlipBoardOffered {
  optional string boardevent = 1;
}

message CoachFlipBoardAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachFlipBoardChoice choice = 2;
}

message CoachFlipBoardExerciseCompleted {
  optional string boardevent = 1;
  optional bool found_correct_move = 2;
  optional int32 wrong_attempts = 3;
}

message CoachContextExtension
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01567"></a>
## FND-01567: chesscom.coaches.v2.CoachFlipBoardAnswered.boardevent = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string boardevent = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4148.

```text
CoachSignUpModalCTATapped {
}

message CoachSettingsOpened {
}

message CoachCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string boardevent = 1;
}

message CoachMistakeWarningAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachMistakeWarningChoice choice = 2;
}

message CoachFlipBoardOffered {
 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01568"></a>
## FND-01568: chesscom.coaches.v2.CoachFlipBoardAnswered.choice = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.CoachFlipBoardChoice choice = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4573.

```text
onal string boardevent = 1;
}

message CoachFlipBoardAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachFlipBoardChoice choice = 2;
}

message CoachFlipBoardExerciseCompleted {
  optional string boardevent = 1;
  optional bool found_correct_move = 2;
  optional int32 wrong_attempts = 3;
}

message CoachContextExtension {
  optional string coach_analytics_id = 1;
  optional string coach_
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01569"></a>
## FND-01569: message declaration: chesscom.coaches.v2.CoachFlipBoardExerciseCompleted

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachFlipBoardExerciseCompleted {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4639.

```text
optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachFlipBoardChoice choice = 2;
}

message CoachFlipBoardExerciseCompleted {
  optional string boardevent = 1;
  optional bool found_correct_move = 2;
  optional int32 wrong_attempts = 3;
}

message CoachContextExtension {
  optional string coach_analytics_id = 1;
  optional string coach_locale = 2;
}

message PlayCoachRetryMissContextExtension {
  oneo
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01570"></a>
## FND-01570: chesscom.coaches.v2.CoachFlipBoardExerciseCompleted.boardevent = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string boardevent = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4148.

```text
CoachSignUpModalCTATapped {
}

message CoachSettingsOpened {
}

message CoachCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string boardevent = 1;
}

message CoachMistakeWarningAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachMistakeWarningChoice choice = 2;
}

message CoachFlipBoardOffered {
 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01571"></a>
## FND-01571: chesscom.coaches.v2.CoachFlipBoardExerciseCompleted.found_correct_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool found_correct_move = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4717.

```text
Choice choice = 2;
}

message CoachFlipBoardExerciseCompleted {
  optional string boardevent = 1;
  optional bool found_correct_move = 2;
  optional int32 wrong_attempts = 3;
}

message CoachContextExtension {
  optional string coach_analytics_id = 1;
  optional string coach_locale = 2;
}

message PlayCoachRetryMissContextExtension {
  oneof _found_correct_move {
  bool found_correct_move = 2;
  }
  oneof _wrong_atte
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01572"></a>
## FND-01572: chesscom.coaches.v2.CoachFlipBoardExerciseCompleted.wrong_attempts = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 wrong_attempts = 3;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4757.

```text
oardExerciseCompleted {
  optional string boardevent = 1;
  optional bool found_correct_move = 2;
  optional int32 wrong_attempts = 3;
}

message CoachContextExtension {
  optional string coach_analytics_id = 1;
  optional string coach_locale = 2;
}

message PlayCoachRetryMissContextExtension {
  oneof _found_correct_move {
  bool found_correct_move = 2;
  }
  oneof _wrong_attempts {
  int32 wrong_attempts = 3;
  }
 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01573"></a>
## FND-01573: message declaration: chesscom.coaches.v2.CoachContextExtension

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachContextExtension {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4795.

```text
ing boardevent = 1;
  optional bool found_correct_move = 2;
  optional int32 wrong_attempts = 3;
}

message CoachContextExtension {
  optional string coach_analytics_id = 1;
  optional string coach_locale = 2;
}

message PlayCoachRetryMissContextExtension {
  oneof _found_correct_move {
  bool found_correct_move = 2;
  }
  oneof _wrong_attempts {
  int32 wrong_attempts = 3;
  }
  optional string boardevent = 1;
}

me
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01574"></a>
## FND-01574: chesscom.coaches.v2.CoachContextExtension.coach_analytics_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coach_analytics_id = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4829.

```text
l found_correct_move = 2;
  optional int32 wrong_attempts = 3;
}

message CoachContextExtension {
  optional string coach_analytics_id = 1;
  optional string coach_locale = 2;
}

message PlayCoachRetryMissContextExtension {
  oneof _found_correct_move {
  bool found_correct_move = 2;
  }
  oneof _wrong_attempts {
  int32 wrong_attempts = 3;
  }
  optional string boardevent = 1;
}

message CoachAnimationShown {
  opti
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
