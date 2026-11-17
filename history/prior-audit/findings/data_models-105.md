# data_models — findings 10401–10500

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-10675"></a>
## FND-10675: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_LESSON_ADOPTION_30D = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_LESSON_ADOPTION_30D = 16;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1060.

```text
3;
  PREDICTIVE_PROPERTY_DEFINITION_NURR_7D = 14;
  PREDICTIVE_PROPERTY_DEFINITION_CURR_14D = 15;
  PREDICTIVE_PROPERTY_DEFINITION_LESSON_ADOPTION_30D = 16;
  PREDICTIVE_PROPERTY_DEFINITION_REACTIVATION_7D = 17;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_PROPENSITY_SCORE = 18;
}

message PredictiveProperty {
  oneof _churn_risk_30d {
  double churn_risk_30d = 1;
  }
  oneof _predictive_scores_updated_at {
  .google.proto
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10676"></a>
## FND-10676: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_REACTIVATION_7D = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_REACTIVATION_7D = 17;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1119.

```text
IVE_PROPERTY_DEFINITION_CURR_14D = 15;
  PREDICTIVE_PROPERTY_DEFINITION_LESSON_ADOPTION_30D = 16;
  PREDICTIVE_PROPERTY_DEFINITION_REACTIVATION_7D = 17;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_PROPENSITY_SCORE = 18;
}

message PredictiveProperty {
  oneof _churn_risk_30d {
  double churn_risk_30d = 1;
  }
  oneof _predictive_scores_updated_at {
  .google.protobuf.Timestamp predictive_scores_updated_at = 2;
  }
  oneof
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10677"></a>
## FND-10677: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_TRIAL_PROPENSITY_SCORE = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_TRIAL_PROPENSITY_SCORE = 18;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1174.

```text
PERTY_DEFINITION_LESSON_ADOPTION_30D = 16;
  PREDICTIVE_PROPERTY_DEFINITION_REACTIVATION_7D = 17;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_PROPENSITY_SCORE = 18;
}

message PredictiveProperty {
  oneof _churn_risk_30d {
  double churn_risk_30d = 1;
  }
  oneof _predictive_scores_updated_at {
  .google.protobuf.Timestamp predictive_scores_updated_at = 2;
  }
  oneof _churn_risk_30d_generated_at {
  .google.protobuf.Time
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10678"></a>
## FND-10678: message declaration: chesscom.user_properties.v1.PredictiveProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PredictiveProperty {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1237.

```text
Y_DEFINITION_REACTIVATION_7D = 17;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_PROPENSITY_SCORE = 18;
}

message PredictiveProperty {
  oneof _churn_risk_30d {
  double churn_risk_30d = 1;
  }
  oneof _predictive_scores_updated_at {
  .google.protobuf.Timestamp predictive_scores_updated_at = 2;
  }
  oneof _churn_risk_30d_generated_at {
  .google.protobuf.Timestamp churn_risk_30d_generated_at = 3;
  }
  oneof _churn_risk_
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10679"></a>
## FND-10679: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._churn_risk_30d

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _churn_risk_30d {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1268.

```text
17;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_PROPENSITY_SCORE = 18;
}

message PredictiveProperty {
  oneof _churn_risk_30d {
  double churn_risk_30d = 1;
  }
  oneof _predictive_scores_updated_at {
  .google.protobuf.Timestamp predictive_scores_updated_at = 2;
  }
  oneof _churn_risk_30d_generated_at {
  .google.protobuf.Timestamp churn_risk_30d_generated_at = 3;
  }
  oneof _churn_risk_30d_model_version {
  string ch
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10680"></a>
## FND-10680: chesscom.user_properties.v1.PredictiveProperty.churn_risk_30d = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double churn_risk_30d = 1;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1294.

```text
DEFINITION_TRIAL_PROPENSITY_SCORE = 18;
}

message PredictiveProperty {
  oneof _churn_risk_30d {
  double churn_risk_30d = 1;
  }
  oneof _predictive_scores_updated_at {
  .google.protobuf.Timestamp predictive_scores_updated_at = 2;
  }
  oneof _churn_risk_30d_generated_at {
  .google.protobuf.Timestamp churn_risk_30d_generated_at = 3;
  }
  oneof _churn_risk_30d_model_version {
  string churn_risk_30d_model_version
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10681"></a>
## FND-10681: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._predictive_scores_updated_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _predictive_scores_updated_at {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1327.

```text
 = 18;
}

message PredictiveProperty {
  oneof _churn_risk_30d {
  double churn_risk_30d = 1;
  }
  oneof _predictive_scores_updated_at {
  .google.protobuf.Timestamp predictive_scores_updated_at = 2;
  }
  oneof _churn_risk_30d_generated_at {
  .google.protobuf.Timestamp churn_risk_30d_generated_at = 3;
  }
  oneof _churn_risk_30d_model_version {
  string churn_risk_30d_model_version = 4;
  }
  oneof _activation_7d 
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10682"></a>
## FND-10682: chesscom.user_properties.v1.PredictiveProperty.predictive_scores_updated_at = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp predictive_scores_updated_at = 2;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1367.

```text
 oneof _churn_risk_30d {
  double churn_risk_30d = 1;
  }
  oneof _predictive_scores_updated_at {
  .google.protobuf.Timestamp predictive_scores_updated_at = 2;
  }
  oneof _churn_risk_30d_generated_at {
  .google.protobuf.Timestamp churn_risk_30d_generated_at = 3;
  }
  oneof _churn_risk_30d_model_version {
  string churn_risk_30d_model_version = 4;
  }
  oneof _activation_7d {
  double activation_7d = 5;
  }
  oneo
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10683"></a>
## FND-10683: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._churn_risk_30d_generated_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _churn_risk_30d_generated_at {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1434.

```text
predictive_scores_updated_at {
  .google.protobuf.Timestamp predictive_scores_updated_at = 2;
  }
  oneof _churn_risk_30d_generated_at {
  .google.protobuf.Timestamp churn_risk_30d_generated_at = 3;
  }
  oneof _churn_risk_30d_model_version {
  string churn_risk_30d_model_version = 4;
  }
  oneof _activation_7d {
  double activation_7d = 5;
  }
  oneof _puzzle_slump_7d {
  double puzzle_slump_7d = 6;
  }
  oneof _les
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10684"></a>
## FND-10684: chesscom.user_properties.v1.PredictiveProperty.churn_risk_30d_generated_at = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp churn_risk_30d_generated_at = 3;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1473.

```text
e.protobuf.Timestamp predictive_scores_updated_at = 2;
  }
  oneof _churn_risk_30d_generated_at {
  .google.protobuf.Timestamp churn_risk_30d_generated_at = 3;
  }
  oneof _churn_risk_30d_model_version {
  string churn_risk_30d_model_version = 4;
  }
  oneof _activation_7d {
  double activation_7d = 5;
  }
  oneof _puzzle_slump_7d {
  double puzzle_slump_7d = 6;
  }
  oneof _lessons_progression_7d {
  double lessons_
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10685"></a>
## FND-10685: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._churn_risk_30d_model_version

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _churn_risk_30d_model_version {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1539.

```text
 _churn_risk_30d_generated_at {
  .google.protobuf.Timestamp churn_risk_30d_generated_at = 3;
  }
  oneof _churn_risk_30d_model_version {
  string churn_risk_30d_model_version = 4;
  }
  oneof _activation_7d {
  double activation_7d = 5;
  }
  oneof _puzzle_slump_7d {
  double puzzle_slump_7d = 6;
  }
  oneof _lessons_progression_7d {
  double lessons_progression_7d = 7;
  }
  oneof _review_upsell_30d {
  double revi
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10686"></a>
## FND-10686: chesscom.user_properties.v1.PredictiveProperty.churn_risk_30d_model_version = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string churn_risk_30d_model_version = 4;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1579.

```text
e.protobuf.Timestamp churn_risk_30d_generated_at = 3;
  }
  oneof _churn_risk_30d_model_version {
  string churn_risk_30d_model_version = 4;
  }
  oneof _activation_7d {
  double activation_7d = 5;
  }
  oneof _puzzle_slump_7d {
  double puzzle_slump_7d = 6;
  }
  oneof _lessons_progression_7d {
  double lessons_progression_7d = 7;
  }
  oneof _review_upsell_30d {
  double review_upsell_30d = 8;
  }
  oneof _return_7
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10687"></a>
## FND-10687: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._activation_7d

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _activation_7d {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1626.

```text
t = 3;
  }
  oneof _churn_risk_30d_model_version {
  string churn_risk_30d_model_version = 4;
  }
  oneof _activation_7d {
  double activation_7d = 5;
  }
  oneof _puzzle_slump_7d {
  double puzzle_slump_7d = 6;
  }
  oneof _lessons_progression_7d {
  double lessons_progression_7d = 7;
  }
  oneof _review_upsell_30d {
  double review_upsell_30d = 8;
  }
  oneof _return_7d {
  double return_7d = 9;
  }
  oneof _trial_
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10688"></a>
## FND-10688: chesscom.user_properties.v1.PredictiveProperty.activation_7d = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double activation_7d = 5;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1651.

```text
_risk_30d_model_version {
  string churn_risk_30d_model_version = 4;
  }
  oneof _activation_7d {
  double activation_7d = 5;
  }
  oneof _puzzle_slump_7d {
  double puzzle_slump_7d = 6;
  }
  oneof _lessons_progression_7d {
  double lessons_progression_7d = 7;
  }
  oneof _review_upsell_30d {
  double review_upsell_30d = 8;
  }
  oneof _return_7d {
  double return_7d = 9;
  }
  oneof _trial_start_7d {
  double trial
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10689"></a>
## FND-10689: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._puzzle_slump_7d

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzle_slump_7d {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1683.

```text
ng churn_risk_30d_model_version = 4;
  }
  oneof _activation_7d {
  double activation_7d = 5;
  }
  oneof _puzzle_slump_7d {
  double puzzle_slump_7d = 6;
  }
  oneof _lessons_progression_7d {
  double lessons_progression_7d = 7;
  }
  oneof _review_upsell_30d {
  double review_upsell_30d = 8;
  }
  oneof _return_7d {
  double return_7d = 9;
  }
  oneof _trial_start_7d {
  double trial_start_7d = 10;
  }
  oneof _tri
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10690"></a>
## FND-10690: chesscom.user_properties.v1.PredictiveProperty.puzzle_slump_7d = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double puzzle_slump_7d = 6;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1710.

```text
sion = 4;
  }
  oneof _activation_7d {
  double activation_7d = 5;
  }
  oneof _puzzle_slump_7d {
  double puzzle_slump_7d = 6;
  }
  oneof _lessons_progression_7d {
  double lessons_progression_7d = 7;
  }
  oneof _review_upsell_30d {
  double review_upsell_30d = 8;
  }
  oneof _return_7d {
  double return_7d = 9;
  }
  oneof _trial_start_7d {
  double trial_start_7d = 10;
  }
  oneof _trial_conversion_30d {
  doubl
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10691"></a>
## FND-10691: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._lessons_progression_7d

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _lessons_progression_7d {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1744.

```text
7d {
  double activation_7d = 5;
  }
  oneof _puzzle_slump_7d {
  double puzzle_slump_7d = 6;
  }
  oneof _lessons_progression_7d {
  double lessons_progression_7d = 7;
  }
  oneof _review_upsell_30d {
  double review_upsell_30d = 8;
  }
  oneof _return_7d {
  double return_7d = 9;
  }
  oneof _trial_start_7d {
  double trial_start_7d = 10;
  }
  oneof _trial_conversion_30d {
  double trial_conversion_30d = 11;
  }
 
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10692"></a>
## FND-10692: chesscom.user_properties.v1.PredictiveProperty.lessons_progression_7d = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double lessons_progression_7d = 7;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1778.

```text
 }
  oneof _puzzle_slump_7d {
  double puzzle_slump_7d = 6;
  }
  oneof _lessons_progression_7d {
  double lessons_progression_7d = 7;
  }
  oneof _review_upsell_30d {
  double review_upsell_30d = 8;
  }
  oneof _return_7d {
  double return_7d = 9;
  }
  oneof _trial_start_7d {
  double trial_start_7d = 10;
  }
  oneof _trial_conversion_30d {
  double trial_conversion_30d = 11;
  }
  oneof _subscription_conversion_30
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10693"></a>
## FND-10693: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._review_upsell_30d

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _review_upsell_30d {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1819.

```text
zzle_slump_7d = 6;
  }
  oneof _lessons_progression_7d {
  double lessons_progression_7d = 7;
  }
  oneof _review_upsell_30d {
  double review_upsell_30d = 8;
  }
  oneof _return_7d {
  double return_7d = 9;
  }
  oneof _trial_start_7d {
  double trial_start_7d = 10;
  }
  oneof _trial_conversion_30d {
  double trial_conversion_30d = 11;
  }
  oneof _subscription_conversion_30d {
  double subscription_conversion_30d 
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10694"></a>
## FND-10694: chesscom.user_properties.v1.PredictiveProperty.review_upsell_30d = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double review_upsell_30d = 8;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1848.

```text
f _lessons_progression_7d {
  double lessons_progression_7d = 7;
  }
  oneof _review_upsell_30d {
  double review_upsell_30d = 8;
  }
  oneof _return_7d {
  double return_7d = 9;
  }
  oneof _trial_start_7d {
  double trial_start_7d = 10;
  }
  oneof _trial_conversion_30d {
  double trial_conversion_30d = 11;
  }
  oneof _subscription_conversion_30d {
  double subscription_conversion_30d = 12;
  }
  oneof _annual_ren
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10695"></a>
## FND-10695: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._return_7d

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _return_7d {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1884.

```text
 lessons_progression_7d = 7;
  }
  oneof _review_upsell_30d {
  double review_upsell_30d = 8;
  }
  oneof _return_7d {
  double return_7d = 9;
  }
  oneof _trial_start_7d {
  double trial_start_7d = 10;
  }
  oneof _trial_conversion_30d {
  double trial_conversion_30d = 11;
  }
  oneof _subscription_conversion_30d {
  double subscription_conversion_30d = 12;
  }
  oneof _annual_renewal_365d {
  double annual_renewal_
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10696"></a>
## FND-10696: chesscom.user_properties.v1.PredictiveProperty.return_7d = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double return_7d = 9;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1905.

```text
7d = 7;
  }
  oneof _review_upsell_30d {
  double review_upsell_30d = 8;
  }
  oneof _return_7d {
  double return_7d = 9;
  }
  oneof _trial_start_7d {
  double trial_start_7d = 10;
  }
  oneof _trial_conversion_30d {
  double trial_conversion_30d = 11;
  }
  oneof _subscription_conversion_30d {
  double subscription_conversion_30d = 12;
  }
  oneof _annual_renewal_365d {
  double annual_renewal_365d = 13;
  }
  oneo
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10697"></a>
## FND-10697: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._trial_start_7d

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _trial_start_7d {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1933.

```text
upsell_30d {
  double review_upsell_30d = 8;
  }
  oneof _return_7d {
  double return_7d = 9;
  }
  oneof _trial_start_7d {
  double trial_start_7d = 10;
  }
  oneof _trial_conversion_30d {
  double trial_conversion_30d = 11;
  }
  oneof _subscription_conversion_30d {
  double subscription_conversion_30d = 12;
  }
  oneof _annual_renewal_365d {
  double annual_renewal_365d = 13;
  }
  oneof _nurr_7d {
  double nurr_7
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10698"></a>
## FND-10698: chesscom.user_properties.v1.PredictiveProperty.trial_start_7d = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double trial_start_7d = 10;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1959.

```text
ew_upsell_30d = 8;
  }
  oneof _return_7d {
  double return_7d = 9;
  }
  oneof _trial_start_7d {
  double trial_start_7d = 10;
  }
  oneof _trial_conversion_30d {
  double trial_conversion_30d = 11;
  }
  oneof _subscription_conversion_30d {
  double subscription_conversion_30d = 12;
  }
  oneof _annual_renewal_365d {
  double annual_renewal_365d = 13;
  }
  oneof _nurr_7d {
  double nurr_7d = 14;
  }
  oneof _curr_
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10699"></a>
## FND-10699: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._trial_conversion_30d

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _trial_conversion_30d {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1993.

```text
turn_7d {
  double return_7d = 9;
  }
  oneof _trial_start_7d {
  double trial_start_7d = 10;
  }
  oneof _trial_conversion_30d {
  double trial_conversion_30d = 11;
  }
  oneof _subscription_conversion_30d {
  double subscription_conversion_30d = 12;
  }
  oneof _annual_renewal_365d {
  double annual_renewal_365d = 13;
  }
  oneof _nurr_7d {
  double nurr_7d = 14;
  }
  oneof _curr_14d {
  double curr_14d = 15;
  }

```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10700"></a>
## FND-10700: chesscom.user_properties.v1.PredictiveProperty.trial_conversion_30d = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double trial_conversion_30d = 11;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2025.

```text
;
  }
  oneof _trial_start_7d {
  double trial_start_7d = 10;
  }
  oneof _trial_conversion_30d {
  double trial_conversion_30d = 11;
  }
  oneof _subscription_conversion_30d {
  double subscription_conversion_30d = 12;
  }
  oneof _annual_renewal_365d {
  double annual_renewal_365d = 13;
  }
  oneof _nurr_7d {
  double nurr_7d = 14;
  }
  oneof _curr_14d {
  double curr_14d = 15;
  }
  oneof _lesson_adoption_30d {
 
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10701"></a>
## FND-10701: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._subscription_conversion_30d

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _subscription_conversion_30d {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2065.

```text
 trial_start_7d = 10;
  }
  oneof _trial_conversion_30d {
  double trial_conversion_30d = 11;
  }
  oneof _subscription_conversion_30d {
  double subscription_conversion_30d = 12;
  }
  oneof _annual_renewal_365d {
  double annual_renewal_365d = 13;
  }
  oneof _nurr_7d {
  double nurr_7d = 14;
  }
  oneof _curr_14d {
  double curr_14d = 15;
  }
  oneof _lesson_adoption_30d {
  double lesson_adoption_30d = 16;
  }
  
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10702"></a>
## FND-10702: chesscom.user_properties.v1.PredictiveProperty.subscription_conversion_30d = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double subscription_conversion_30d = 12;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2104.

```text
l_conversion_30d {
  double trial_conversion_30d = 11;
  }
  oneof _subscription_conversion_30d {
  double subscription_conversion_30d = 12;
  }
  oneof _annual_renewal_365d {
  double annual_renewal_365d = 13;
  }
  oneof _nurr_7d {
  double nurr_7d = 14;
  }
  oneof _curr_14d {
  double curr_14d = 15;
  }
  oneof _lesson_adoption_30d {
  double lesson_adoption_30d = 16;
  }
  oneof _reactivation_7d {
  double react
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10703"></a>
## FND-10703: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._annual_renewal_365d

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _annual_renewal_365d {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2151.

```text
d = 11;
  }
  oneof _subscription_conversion_30d {
  double subscription_conversion_30d = 12;
  }
  oneof _annual_renewal_365d {
  double annual_renewal_365d = 13;
  }
  oneof _nurr_7d {
  double nurr_7d = 14;
  }
  oneof _curr_14d {
  double curr_14d = 15;
  }
  oneof _lesson_adoption_30d {
  double lesson_adoption_30d = 16;
  }
  oneof _reactivation_7d {
  double reactivation_7d = 17;
  }
  oneof _trial_propensity_
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10704"></a>
## FND-10704: chesscom.user_properties.v1.PredictiveProperty.annual_renewal_365d = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double annual_renewal_365d = 13;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2182.

```text
on_conversion_30d {
  double subscription_conversion_30d = 12;
  }
  oneof _annual_renewal_365d {
  double annual_renewal_365d = 13;
  }
  oneof _nurr_7d {
  double nurr_7d = 14;
  }
  oneof _curr_14d {
  double curr_14d = 15;
  }
  oneof _lesson_adoption_30d {
  double lesson_adoption_30d = 16;
  }
  oneof _reactivation_7d {
  double reactivation_7d = 17;
  }
  oneof _trial_propensity_score {
  int32 trial_propensit
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10705"></a>
## FND-10705: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._nurr_7d

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _nurr_7d {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2221.

```text
on_conversion_30d = 12;
  }
  oneof _annual_renewal_365d {
  double annual_renewal_365d = 13;
  }
  oneof _nurr_7d {
  double nurr_7d = 14;
  }
  oneof _curr_14d {
  double curr_14d = 15;
  }
  oneof _lesson_adoption_30d {
  double lesson_adoption_30d = 16;
  }
  oneof _reactivation_7d {
  double reactivation_7d = 17;
  }
  oneof _trial_propensity_score {
  int32 trial_propensity_score = 18;
  }
}

```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10706"></a>
## FND-10706: chesscom.user_properties.v1.PredictiveProperty.nurr_7d = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double nurr_7d = 14;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2240.

```text
 12;
  }
  oneof _annual_renewal_365d {
  double annual_renewal_365d = 13;
  }
  oneof _nurr_7d {
  double nurr_7d = 14;
  }
  oneof _curr_14d {
  double curr_14d = 15;
  }
  oneof _lesson_adoption_30d {
  double lesson_adoption_30d = 16;
  }
  oneof _reactivation_7d {
  double reactivation_7d = 17;
  }
  oneof _trial_propensity_score {
  int32 trial_propensity_score = 18;
  }
}

```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10707"></a>
## FND-10707: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._curr_14d

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _curr_14d {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2267.

```text
newal_365d {
  double annual_renewal_365d = 13;
  }
  oneof _nurr_7d {
  double nurr_7d = 14;
  }
  oneof _curr_14d {
  double curr_14d = 15;
  }
  oneof _lesson_adoption_30d {
  double lesson_adoption_30d = 16;
  }
  oneof _reactivation_7d {
  double reactivation_7d = 17;
  }
  oneof _trial_propensity_score {
  int32 trial_propensity_score = 18;
  }
}

```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10708"></a>
## FND-10708: chesscom.user_properties.v1.PredictiveProperty.curr_14d = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double curr_14d = 15;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2287.

```text
e annual_renewal_365d = 13;
  }
  oneof _nurr_7d {
  double nurr_7d = 14;
  }
  oneof _curr_14d {
  double curr_14d = 15;
  }
  oneof _lesson_adoption_30d {
  double lesson_adoption_30d = 16;
  }
  oneof _reactivation_7d {
  double reactivation_7d = 17;
  }
  oneof _trial_propensity_score {
  int32 trial_propensity_score = 18;
  }
}

```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10709"></a>
## FND-10709: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._lesson_adoption_30d

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _lesson_adoption_30d {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2315.

```text
  }
  oneof _nurr_7d {
  double nurr_7d = 14;
  }
  oneof _curr_14d {
  double curr_14d = 15;
  }
  oneof _lesson_adoption_30d {
  double lesson_adoption_30d = 16;
  }
  oneof _reactivation_7d {
  double reactivation_7d = 17;
  }
  oneof _trial_propensity_score {
  int32 trial_propensity_score = 18;
  }
}

```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10710"></a>
## FND-10710: chesscom.user_properties.v1.PredictiveProperty.lesson_adoption_30d = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double lesson_adoption_30d = 16;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2346.

```text
 nurr_7d = 14;
  }
  oneof _curr_14d {
  double curr_14d = 15;
  }
  oneof _lesson_adoption_30d {
  double lesson_adoption_30d = 16;
  }
  oneof _reactivation_7d {
  double reactivation_7d = 17;
  }
  oneof _trial_propensity_score {
  int32 trial_propensity_score = 18;
  }
}

```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10711"></a>
## FND-10711: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._reactivation_7d

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _reactivation_7d {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2385.

```text
  double curr_14d = 15;
  }
  oneof _lesson_adoption_30d {
  double lesson_adoption_30d = 16;
  }
  oneof _reactivation_7d {
  double reactivation_7d = 17;
  }
  oneof _trial_propensity_score {
  int32 trial_propensity_score = 18;
  }
}

```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10712"></a>
## FND-10712: chesscom.user_properties.v1.PredictiveProperty.reactivation_7d = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double reactivation_7d = 17;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2412.

```text

  oneof _lesson_adoption_30d {
  double lesson_adoption_30d = 16;
  }
  oneof _reactivation_7d {
  double reactivation_7d = 17;
  }
  oneof _trial_propensity_score {
  int32 trial_propensity_score = 18;
  }
}

```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10713"></a>
## FND-10713: oneof declaration: chesscom.user_properties.v1.PredictiveProperty._trial_propensity_score

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _trial_propensity_score {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2447.

```text
ouble lesson_adoption_30d = 16;
  }
  oneof _reactivation_7d {
  double reactivation_7d = 17;
  }
  oneof _trial_propensity_score {
  int32 trial_propensity_score = 18;
  }
}

```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10714"></a>
## FND-10714: chesscom.user_properties.v1.PredictiveProperty.trial_propensity_score = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 trial_propensity_score = 18;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 2481.

```text
}
  oneof _reactivation_7d {
  double reactivation_7d = 17;
  }
  oneof _trial_propensity_score {
  int32 trial_propensity_score = 18;
  }
}

```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10715"></a>
## FND-10715: enum declaration: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ProductActivityRankingsPropertyDefinition {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 139.

```text
properties_product_activity_rankings.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum ProductActivityRankingsPropertyDefinition {
  PRODUCT_RANKINGS_PROPERTY_UNSPECIFIED = 0;
  DAILY_TIME_ON_PLATFORM_IN_SECONDS_RANK = 1;
  FRIEND_GAMES_RANK = 2;
  DAILY_MOVES_RANK = 3;
  LESSON_ACTIVITY_RANK = 4;
  GAME_REVIEWS_STARTED_RANK = 5;
  GAME_REVIEW_ACTIVITY_RANK = 6;
  ARTICLE_ACTIVITY_RANK = 7;
  EVENTS
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10716"></a>
## FND-10716: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.PRODUCT_RANKINGS_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_RANKINGS_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 190.

```text
x: proto3

package chesscom.user_properties.v1;

enum ProductActivityRankingsPropertyDefinition {
  PRODUCT_RANKINGS_PROPERTY_UNSPECIFIED = 0;
  DAILY_TIME_ON_PLATFORM_IN_SECONDS_RANK = 1;
  FRIEND_GAMES_RANK = 2;
  DAILY_MOVES_RANK = 3;
  LESSON_ACTIVITY_RANK = 4;
  GAME_REVIEWS_STARTED_RANK = 5;
  GAME_REVIEW_ACTIVITY_RANK = 6;
  ARTICLE_ACTIVITY_RANK = 7;
  EVENTS_ACTIVITY_RANK = 8;
  VS_COACH_ACTIVITY_RANK = 9;
 
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10717"></a>
## FND-10717: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.DAILY_TIME_ON_PLATFORM_IN_SECONDS_RANK = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DAILY_TIME_ON_PLATFORM_IN_SECONDS_RANK = 1;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 235.

```text
1;

enum ProductActivityRankingsPropertyDefinition {
  PRODUCT_RANKINGS_PROPERTY_UNSPECIFIED = 0;
  DAILY_TIME_ON_PLATFORM_IN_SECONDS_RANK = 1;
  FRIEND_GAMES_RANK = 2;
  DAILY_MOVES_RANK = 3;
  LESSON_ACTIVITY_RANK = 4;
  GAME_REVIEWS_STARTED_RANK = 5;
  GAME_REVIEW_ACTIVITY_RANK = 6;
  ARTICLE_ACTIVITY_RANK = 7;
  EVENTS_ACTIVITY_RANK = 8;
  VS_COACH_ACTIVITY_RANK = 9;
  VS_COACH_GAMES_RANK = 10;
  LIVE_BULLET_GAME
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10718"></a>
## FND-10718: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.FRIEND_GAMES_RANK = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIEND_GAMES_RANK = 2;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 281.

```text
tion {
  PRODUCT_RANKINGS_PROPERTY_UNSPECIFIED = 0;
  DAILY_TIME_ON_PLATFORM_IN_SECONDS_RANK = 1;
  FRIEND_GAMES_RANK = 2;
  DAILY_MOVES_RANK = 3;
  LESSON_ACTIVITY_RANK = 4;
  GAME_REVIEWS_STARTED_RANK = 5;
  GAME_REVIEW_ACTIVITY_RANK = 6;
  ARTICLE_ACTIVITY_RANK = 7;
  EVENTS_ACTIVITY_RANK = 8;
  VS_COACH_ACTIVITY_RANK = 9;
  VS_COACH_GAMES_RANK = 10;
  LIVE_BULLET_GAMES_RANK = 11;
  LIVE_BLITZ_GAMES_RANK = 12;
  L
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10719"></a>
## FND-10719: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.DAILY_MOVES_RANK = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DAILY_MOVES_RANK = 3;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 306.

```text
_PROPERTY_UNSPECIFIED = 0;
  DAILY_TIME_ON_PLATFORM_IN_SECONDS_RANK = 1;
  FRIEND_GAMES_RANK = 2;
  DAILY_MOVES_RANK = 3;
  LESSON_ACTIVITY_RANK = 4;
  GAME_REVIEWS_STARTED_RANK = 5;
  GAME_REVIEW_ACTIVITY_RANK = 6;
  ARTICLE_ACTIVITY_RANK = 7;
  EVENTS_ACTIVITY_RANK = 8;
  VS_COACH_ACTIVITY_RANK = 9;
  VS_COACH_GAMES_RANK = 10;
  LIVE_BULLET_GAMES_RANK = 11;
  LIVE_BLITZ_GAMES_RANK = 12;
  LIVE_RAPID_GAMES_RANK = 13
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10720"></a>
## FND-10720: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.LESSON_ACTIVITY_RANK = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LESSON_ACTIVITY_RANK = 4;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 330.

```text
0;
  DAILY_TIME_ON_PLATFORM_IN_SECONDS_RANK = 1;
  FRIEND_GAMES_RANK = 2;
  DAILY_MOVES_RANK = 3;
  LESSON_ACTIVITY_RANK = 4;
  GAME_REVIEWS_STARTED_RANK = 5;
  GAME_REVIEW_ACTIVITY_RANK = 6;
  ARTICLE_ACTIVITY_RANK = 7;
  EVENTS_ACTIVITY_RANK = 8;
  VS_COACH_ACTIVITY_RANK = 9;
  VS_COACH_GAMES_RANK = 10;
  LIVE_BULLET_GAMES_RANK = 11;
  LIVE_BLITZ_GAMES_RANK = 12;
  LIVE_RAPID_GAMES_RANK = 13;
  LESSON_START_RANK = 
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10721"></a>
## FND-10721: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.GAME_REVIEWS_STARTED_RANK = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEWS_STARTED_RANK = 5;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 358.

```text
IN_SECONDS_RANK = 1;
  FRIEND_GAMES_RANK = 2;
  DAILY_MOVES_RANK = 3;
  LESSON_ACTIVITY_RANK = 4;
  GAME_REVIEWS_STARTED_RANK = 5;
  GAME_REVIEW_ACTIVITY_RANK = 6;
  ARTICLE_ACTIVITY_RANK = 7;
  EVENTS_ACTIVITY_RANK = 8;
  VS_COACH_ACTIVITY_RANK = 9;
  VS_COACH_GAMES_RANK = 10;
  LIVE_BULLET_GAMES_RANK = 11;
  LIVE_BLITZ_GAMES_RANK = 12;
  LIVE_RAPID_GAMES_RANK = 13;
  LESSON_START_RANK = 14;
  SOCIAL_ACTIVITY_RANK =
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10722"></a>
## FND-10722: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.GAME_REVIEW_ACTIVITY_RANK = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_ACTIVITY_RANK = 6;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 391.

```text
ES_RANK = 2;
  DAILY_MOVES_RANK = 3;
  LESSON_ACTIVITY_RANK = 4;
  GAME_REVIEWS_STARTED_RANK = 5;
  GAME_REVIEW_ACTIVITY_RANK = 6;
  ARTICLE_ACTIVITY_RANK = 7;
  EVENTS_ACTIVITY_RANK = 8;
  VS_COACH_ACTIVITY_RANK = 9;
  VS_COACH_GAMES_RANK = 10;
  LIVE_BULLET_GAMES_RANK = 11;
  LIVE_BLITZ_GAMES_RANK = 12;
  LIVE_RAPID_GAMES_RANK = 13;
  LESSON_START_RANK = 14;
  SOCIAL_ACTIVITY_RANK = 15;
  BOT_GAMES_RANK = 16;
  UPG
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10723"></a>
## FND-10723: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.ARTICLE_ACTIVITY_RANK = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ARTICLE_ACTIVITY_RANK = 7;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 424.

```text
 3;
  LESSON_ACTIVITY_RANK = 4;
  GAME_REVIEWS_STARTED_RANK = 5;
  GAME_REVIEW_ACTIVITY_RANK = 6;
  ARTICLE_ACTIVITY_RANK = 7;
  EVENTS_ACTIVITY_RANK = 8;
  VS_COACH_ACTIVITY_RANK = 9;
  VS_COACH_GAMES_RANK = 10;
  LIVE_BULLET_GAMES_RANK = 11;
  LIVE_BLITZ_GAMES_RANK = 12;
  LIVE_RAPID_GAMES_RANK = 13;
  LESSON_START_RANK = 14;
  SOCIAL_ACTIVITY_RANK = 15;
  BOT_GAMES_RANK = 16;
  UPGRADE_ACTIVITY_RANK = 17;
  ACTIVE
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10724"></a>
## FND-10724: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.EVENTS_ACTIVITY_RANK = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENTS_ACTIVITY_RANK = 8;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 453.

```text
4;
  GAME_REVIEWS_STARTED_RANK = 5;
  GAME_REVIEW_ACTIVITY_RANK = 6;
  ARTICLE_ACTIVITY_RANK = 7;
  EVENTS_ACTIVITY_RANK = 8;
  VS_COACH_ACTIVITY_RANK = 9;
  VS_COACH_GAMES_RANK = 10;
  LIVE_BULLET_GAMES_RANK = 11;
  LIVE_BLITZ_GAMES_RANK = 12;
  LIVE_RAPID_GAMES_RANK = 13;
  LESSON_START_RANK = 14;
  SOCIAL_ACTIVITY_RANK = 15;
  BOT_GAMES_RANK = 16;
  UPGRADE_ACTIVITY_RANK = 17;
  ACTIVE_EVENTS_RANK = 18;
  LIVE_GAM
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10725"></a>
## FND-10725: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.VS_COACH_ACTIVITY_RANK = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VS_COACH_ACTIVITY_RANK = 9;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 481.

```text
NK = 5;
  GAME_REVIEW_ACTIVITY_RANK = 6;
  ARTICLE_ACTIVITY_RANK = 7;
  EVENTS_ACTIVITY_RANK = 8;
  VS_COACH_ACTIVITY_RANK = 9;
  VS_COACH_GAMES_RANK = 10;
  LIVE_BULLET_GAMES_RANK = 11;
  LIVE_BLITZ_GAMES_RANK = 12;
  LIVE_RAPID_GAMES_RANK = 13;
  LESSON_START_RANK = 14;
  SOCIAL_ACTIVITY_RANK = 15;
  BOT_GAMES_RANK = 16;
  UPGRADE_ACTIVITY_RANK = 17;
  ACTIVE_EVENTS_RANK = 18;
  LIVE_GAMES_RANK = 19;
  TOURNAMENT_G
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10726"></a>
## FND-10726: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.VS_COACH_GAMES_RANK = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VS_COACH_GAMES_RANK = 10;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 511.

```text
_RANK = 6;
  ARTICLE_ACTIVITY_RANK = 7;
  EVENTS_ACTIVITY_RANK = 8;
  VS_COACH_ACTIVITY_RANK = 9;
  VS_COACH_GAMES_RANK = 10;
  LIVE_BULLET_GAMES_RANK = 11;
  LIVE_BLITZ_GAMES_RANK = 12;
  LIVE_RAPID_GAMES_RANK = 13;
  LESSON_START_RANK = 14;
  SOCIAL_ACTIVITY_RANK = 15;
  BOT_GAMES_RANK = 16;
  UPGRADE_ACTIVITY_RANK = 17;
  ACTIVE_EVENTS_RANK = 18;
  LIVE_GAMES_RANK = 19;
  TOURNAMENT_GAMES_RANK = 20;
  TACTICS_RANK
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10727"></a>
## FND-10727: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.LIVE_BULLET_GAMES_RANK = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LIVE_BULLET_GAMES_RANK = 11;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 539.

```text
Y_RANK = 7;
  EVENTS_ACTIVITY_RANK = 8;
  VS_COACH_ACTIVITY_RANK = 9;
  VS_COACH_GAMES_RANK = 10;
  LIVE_BULLET_GAMES_RANK = 11;
  LIVE_BLITZ_GAMES_RANK = 12;
  LIVE_RAPID_GAMES_RANK = 13;
  LESSON_START_RANK = 14;
  SOCIAL_ACTIVITY_RANK = 15;
  BOT_GAMES_RANK = 16;
  UPGRADE_ACTIVITY_RANK = 17;
  ACTIVE_EVENTS_RANK = 18;
  LIVE_GAMES_RANK = 19;
  TOURNAMENT_GAMES_RANK = 20;
  TACTICS_RANK = 21;
  PUZZLE_RUSHES_RANK 
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10728"></a>
## FND-10728: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.LIVE_BLITZ_GAMES_RANK = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LIVE_BLITZ_GAMES_RANK = 12;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 570.

```text
ANK = 8;
  VS_COACH_ACTIVITY_RANK = 9;
  VS_COACH_GAMES_RANK = 10;
  LIVE_BULLET_GAMES_RANK = 11;
  LIVE_BLITZ_GAMES_RANK = 12;
  LIVE_RAPID_GAMES_RANK = 13;
  LESSON_START_RANK = 14;
  SOCIAL_ACTIVITY_RANK = 15;
  BOT_GAMES_RANK = 16;
  UPGRADE_ACTIVITY_RANK = 17;
  ACTIVE_EVENTS_RANK = 18;
  LIVE_GAMES_RANK = 19;
  TOURNAMENT_GAMES_RANK = 20;
  TACTICS_RANK = 21;
  PUZZLE_RUSHES_RANK = 22;
  PUZZLE_BATTLES_RANK = 2
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10729"></a>
## FND-10729: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.LIVE_RAPID_GAMES_RANK = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LIVE_RAPID_GAMES_RANK = 13;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 600.

```text
ANK = 9;
  VS_COACH_GAMES_RANK = 10;
  LIVE_BULLET_GAMES_RANK = 11;
  LIVE_BLITZ_GAMES_RANK = 12;
  LIVE_RAPID_GAMES_RANK = 13;
  LESSON_START_RANK = 14;
  SOCIAL_ACTIVITY_RANK = 15;
  BOT_GAMES_RANK = 16;
  UPGRADE_ACTIVITY_RANK = 17;
  ACTIVE_EVENTS_RANK = 18;
  LIVE_GAMES_RANK = 19;
  TOURNAMENT_GAMES_RANK = 20;
  TACTICS_RANK = 21;
  PUZZLE_RUSHES_RANK = 22;
  PUZZLE_BATTLES_RANK = 23;
  DAILY_PUZZLES_RANK = 24;

```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10730"></a>
## FND-10730: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.LESSON_START_RANK = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LESSON_START_RANK = 14;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 630.

```text
 = 10;
  LIVE_BULLET_GAMES_RANK = 11;
  LIVE_BLITZ_GAMES_RANK = 12;
  LIVE_RAPID_GAMES_RANK = 13;
  LESSON_START_RANK = 14;
  SOCIAL_ACTIVITY_RANK = 15;
  BOT_GAMES_RANK = 16;
  UPGRADE_ACTIVITY_RANK = 17;
  ACTIVE_EVENTS_RANK = 18;
  LIVE_GAMES_RANK = 19;
  TOURNAMENT_GAMES_RANK = 20;
  TACTICS_RANK = 21;
  PUZZLE_RUSHES_RANK = 22;
  PUZZLE_BATTLES_RANK = 23;
  DAILY_PUZZLES_RANK = 24;
  COURSES_STARTED_RANK = 25;
 
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10731"></a>
## FND-10731: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.SOCIAL_ACTIVITY_RANK = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SOCIAL_ACTIVITY_RANK = 15;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 656.

```text
_RANK = 11;
  LIVE_BLITZ_GAMES_RANK = 12;
  LIVE_RAPID_GAMES_RANK = 13;
  LESSON_START_RANK = 14;
  SOCIAL_ACTIVITY_RANK = 15;
  BOT_GAMES_RANK = 16;
  UPGRADE_ACTIVITY_RANK = 17;
  ACTIVE_EVENTS_RANK = 18;
  LIVE_GAMES_RANK = 19;
  TOURNAMENT_GAMES_RANK = 20;
  TACTICS_RANK = 21;
  PUZZLE_RUSHES_RANK = 22;
  PUZZLE_BATTLES_RANK = 23;
  DAILY_PUZZLES_RANK = 24;
  COURSES_STARTED_RANK = 25;
  PRACTICE_ENDGAME_STARTED_
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10732"></a>
## FND-10732: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.BOT_GAMES_RANK = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_GAMES_RANK = 16;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 685.

```text
S_RANK = 12;
  LIVE_RAPID_GAMES_RANK = 13;
  LESSON_START_RANK = 14;
  SOCIAL_ACTIVITY_RANK = 15;
  BOT_GAMES_RANK = 16;
  UPGRADE_ACTIVITY_RANK = 17;
  ACTIVE_EVENTS_RANK = 18;
  LIVE_GAMES_RANK = 19;
  TOURNAMENT_GAMES_RANK = 20;
  TACTICS_RANK = 21;
  PUZZLE_RUSHES_RANK = 22;
  PUZZLE_BATTLES_RANK = 23;
  DAILY_PUZZLES_RANK = 24;
  COURSES_STARTED_RANK = 25;
  PRACTICE_ENDGAME_STARTED_RANK = 26;
  ANALYSIS_STARTED
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10733"></a>
## FND-10733: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.UPGRADE_ACTIVITY_RANK = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

UPGRADE_ACTIVITY_RANK = 17;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 708.

```text
ID_GAMES_RANK = 13;
  LESSON_START_RANK = 14;
  SOCIAL_ACTIVITY_RANK = 15;
  BOT_GAMES_RANK = 16;
  UPGRADE_ACTIVITY_RANK = 17;
  ACTIVE_EVENTS_RANK = 18;
  LIVE_GAMES_RANK = 19;
  TOURNAMENT_GAMES_RANK = 20;
  TACTICS_RANK = 21;
  PUZZLE_RUSHES_RANK = 22;
  PUZZLE_BATTLES_RANK = 23;
  DAILY_PUZZLES_RANK = 24;
  COURSES_STARTED_RANK = 25;
  PRACTICE_ENDGAME_STARTED_RANK = 26;
  ANALYSIS_STARTED_RANK = 27;
  STATS_PAG
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10734"></a>
## FND-10734: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.ACTIVE_EVENTS_RANK = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ACTIVE_EVENTS_RANK = 18;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 738.

```text
TART_RANK = 14;
  SOCIAL_ACTIVITY_RANK = 15;
  BOT_GAMES_RANK = 16;
  UPGRADE_ACTIVITY_RANK = 17;
  ACTIVE_EVENTS_RANK = 18;
  LIVE_GAMES_RANK = 19;
  TOURNAMENT_GAMES_RANK = 20;
  TACTICS_RANK = 21;
  PUZZLE_RUSHES_RANK = 22;
  PUZZLE_BATTLES_RANK = 23;
  DAILY_PUZZLES_RANK = 24;
  COURSES_STARTED_RANK = 25;
  PRACTICE_ENDGAME_STARTED_RANK = 26;
  ANALYSIS_STARTED_RANK = 27;
  STATS_PAGE_VIEWS_RANK = 28;
  CHESS_TV_
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10735"></a>
## FND-10735: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.LIVE_GAMES_RANK = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LIVE_GAMES_RANK = 19;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 765.

```text
TIVITY_RANK = 15;
  BOT_GAMES_RANK = 16;
  UPGRADE_ACTIVITY_RANK = 17;
  ACTIVE_EVENTS_RANK = 18;
  LIVE_GAMES_RANK = 19;
  TOURNAMENT_GAMES_RANK = 20;
  TACTICS_RANK = 21;
  PUZZLE_RUSHES_RANK = 22;
  PUZZLE_BATTLES_RANK = 23;
  DAILY_PUZZLES_RANK = 24;
  COURSES_STARTED_RANK = 25;
  PRACTICE_ENDGAME_STARTED_RANK = 26;
  ANALYSIS_STARTED_RANK = 27;
  STATS_PAGE_VIEWS_RANK = 28;
  CHESS_TV_EVENT_VIEWS_RANK = 29;
  AR
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10736"></a>
## FND-10736: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.TOURNAMENT_GAMES_RANK = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOURNAMENT_GAMES_RANK = 20;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 789.

```text
GAMES_RANK = 16;
  UPGRADE_ACTIVITY_RANK = 17;
  ACTIVE_EVENTS_RANK = 18;
  LIVE_GAMES_RANK = 19;
  TOURNAMENT_GAMES_RANK = 20;
  TACTICS_RANK = 21;
  PUZZLE_RUSHES_RANK = 22;
  PUZZLE_BATTLES_RANK = 23;
  DAILY_PUZZLES_RANK = 24;
  COURSES_STARTED_RANK = 25;
  PRACTICE_ENDGAME_STARTED_RANK = 26;
  ANALYSIS_STARTED_RANK = 27;
  STATS_PAGE_VIEWS_RANK = 28;
  CHESS_TV_EVENT_VIEWS_RANK = 29;
  ARTICLE_NEWS_BLOG_FORUM_VI
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10737"></a>
## FND-10737: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.TACTICS_RANK = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TACTICS_RANK = 21;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 819.

```text
IVITY_RANK = 17;
  ACTIVE_EVENTS_RANK = 18;
  LIVE_GAMES_RANK = 19;
  TOURNAMENT_GAMES_RANK = 20;
  TACTICS_RANK = 21;
  PUZZLE_RUSHES_RANK = 22;
  PUZZLE_BATTLES_RANK = 23;
  DAILY_PUZZLES_RANK = 24;
  COURSES_STARTED_RANK = 25;
  PRACTICE_ENDGAME_STARTED_RANK = 26;
  ANALYSIS_STARTED_RANK = 27;
  STATS_PAGE_VIEWS_RANK = 28;
  CHESS_TV_EVENT_VIEWS_RANK = 29;
  ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30;
  SOCIAL_SHARES
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10738"></a>
## FND-10738: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.PUZZLE_RUSHES_RANK = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_RUSHES_RANK = 22;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 840.

```text
TIVE_EVENTS_RANK = 18;
  LIVE_GAMES_RANK = 19;
  TOURNAMENT_GAMES_RANK = 20;
  TACTICS_RANK = 21;
  PUZZLE_RUSHES_RANK = 22;
  PUZZLE_BATTLES_RANK = 23;
  DAILY_PUZZLES_RANK = 24;
  COURSES_STARTED_RANK = 25;
  PRACTICE_ENDGAME_STARTED_RANK = 26;
  ANALYSIS_STARTED_RANK = 27;
  STATS_PAGE_VIEWS_RANK = 28;
  CHESS_TV_EVENT_VIEWS_RANK = 29;
  ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30;
  SOCIAL_SHARES_RANK = 31;
  CHAT_ME
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10739"></a>
## FND-10739: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.PUZZLE_BATTLES_RANK = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_BATTLES_RANK = 23;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 867.

```text
VE_GAMES_RANK = 19;
  TOURNAMENT_GAMES_RANK = 20;
  TACTICS_RANK = 21;
  PUZZLE_RUSHES_RANK = 22;
  PUZZLE_BATTLES_RANK = 23;
  DAILY_PUZZLES_RANK = 24;
  COURSES_STARTED_RANK = 25;
  PRACTICE_ENDGAME_STARTED_RANK = 26;
  ANALYSIS_STARTED_RANK = 27;
  STATS_PAGE_VIEWS_RANK = 28;
  CHESS_TV_EVENT_VIEWS_RANK = 29;
  ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30;
  SOCIAL_SHARES_RANK = 31;
  CHAT_MESSAGES_RANK = 32;
  FRIENDS
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10740"></a>
## FND-10740: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.DAILY_PUZZLES_RANK = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DAILY_PUZZLES_RANK = 24;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 895.

```text
MENT_GAMES_RANK = 20;
  TACTICS_RANK = 21;
  PUZZLE_RUSHES_RANK = 22;
  PUZZLE_BATTLES_RANK = 23;
  DAILY_PUZZLES_RANK = 24;
  COURSES_STARTED_RANK = 25;
  PRACTICE_ENDGAME_STARTED_RANK = 26;
  ANALYSIS_STARTED_RANK = 27;
  STATS_PAGE_VIEWS_RANK = 28;
  CHESS_TV_EVENT_VIEWS_RANK = 29;
  ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30;
  SOCIAL_SHARES_RANK = 31;
  CHAT_MESSAGES_RANK = 32;
  FRIENDS_ADDED_RANK = 33;
  FRIEND_I
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10741"></a>
## FND-10741: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.COURSES_STARTED_RANK = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSES_STARTED_RANK = 25;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 922.

```text
TICS_RANK = 21;
  PUZZLE_RUSHES_RANK = 22;
  PUZZLE_BATTLES_RANK = 23;
  DAILY_PUZZLES_RANK = 24;
  COURSES_STARTED_RANK = 25;
  PRACTICE_ENDGAME_STARTED_RANK = 26;
  ANALYSIS_STARTED_RANK = 27;
  STATS_PAGE_VIEWS_RANK = 28;
  CHESS_TV_EVENT_VIEWS_RANK = 29;
  ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30;
  SOCIAL_SHARES_RANK = 31;
  CHAT_MESSAGES_RANK = 32;
  FRIENDS_ADDED_RANK = 33;
  FRIEND_INVITES_SENT_RANK = 34;
}

m
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10742"></a>
## FND-10742: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.PRACTICE_ENDGAME_STARTED_RANK = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRACTICE_ENDGAME_STARTED_RANK = 26;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 951.

```text
ES_RANK = 22;
  PUZZLE_BATTLES_RANK = 23;
  DAILY_PUZZLES_RANK = 24;
  COURSES_STARTED_RANK = 25;
  PRACTICE_ENDGAME_STARTED_RANK = 26;
  ANALYSIS_STARTED_RANK = 27;
  STATS_PAGE_VIEWS_RANK = 28;
  CHESS_TV_EVENT_VIEWS_RANK = 29;
  ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30;
  SOCIAL_SHARES_RANK = 31;
  CHAT_MESSAGES_RANK = 32;
  FRIENDS_ADDED_RANK = 33;
  FRIEND_INVITES_SENT_RANK = 34;
}

message ProductActivityRanking
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10743"></a>
## FND-10743: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.ANALYSIS_STARTED_RANK = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_STARTED_RANK = 27;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 989.

```text
23;
  DAILY_PUZZLES_RANK = 24;
  COURSES_STARTED_RANK = 25;
  PRACTICE_ENDGAME_STARTED_RANK = 26;
  ANALYSIS_STARTED_RANK = 27;
  STATS_PAGE_VIEWS_RANK = 28;
  CHESS_TV_EVENT_VIEWS_RANK = 29;
  ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30;
  SOCIAL_SHARES_RANK = 31;
  CHAT_MESSAGES_RANK = 32;
  FRIENDS_ADDED_RANK = 33;
  FRIEND_INVITES_SENT_RANK = 34;
}

message ProductActivityRankingsProperty {
  oneof _daily_time_on_pla
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10744"></a>
## FND-10744: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.STATS_PAGE_VIEWS_RANK = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_PAGE_VIEWS_RANK = 28;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1019.

```text

  COURSES_STARTED_RANK = 25;
  PRACTICE_ENDGAME_STARTED_RANK = 26;
  ANALYSIS_STARTED_RANK = 27;
  STATS_PAGE_VIEWS_RANK = 28;
  CHESS_TV_EVENT_VIEWS_RANK = 29;
  ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30;
  SOCIAL_SHARES_RANK = 31;
  CHAT_MESSAGES_RANK = 32;
  FRIENDS_ADDED_RANK = 33;
  FRIEND_INVITES_SENT_RANK = 34;
}

message ProductActivityRankingsProperty {
  oneof _daily_time_on_platform_in_seconds_rank {
  doub
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10745"></a>
## FND-10745: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.CHESS_TV_EVENT_VIEWS_RANK = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESS_TV_EVENT_VIEWS_RANK = 29;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1049.

```text
  PRACTICE_ENDGAME_STARTED_RANK = 26;
  ANALYSIS_STARTED_RANK = 27;
  STATS_PAGE_VIEWS_RANK = 28;
  CHESS_TV_EVENT_VIEWS_RANK = 29;
  ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30;
  SOCIAL_SHARES_RANK = 31;
  CHAT_MESSAGES_RANK = 32;
  FRIENDS_ADDED_RANK = 33;
  FRIEND_INVITES_SENT_RANK = 34;
}

message ProductActivityRankingsProperty {
  oneof _daily_time_on_platform_in_seconds_rank {
  double daily_time_on_platform_in_s
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10746"></a>
## FND-10746: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1083.

```text
26;
  ANALYSIS_STARTED_RANK = 27;
  STATS_PAGE_VIEWS_RANK = 28;
  CHESS_TV_EVENT_VIEWS_RANK = 29;
  ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30;
  SOCIAL_SHARES_RANK = 31;
  CHAT_MESSAGES_RANK = 32;
  FRIENDS_ADDED_RANK = 33;
  FRIEND_INVITES_SENT_RANK = 34;
}

message ProductActivityRankingsProperty {
  oneof _daily_time_on_platform_in_seconds_rank {
  double daily_time_on_platform_in_seconds_rank = 1;
  }
  oneof _frie
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10747"></a>
## FND-10747: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.SOCIAL_SHARES_RANK = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SOCIAL_SHARES_RANK = 31;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1126.

```text
AGE_VIEWS_RANK = 28;
  CHESS_TV_EVENT_VIEWS_RANK = 29;
  ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30;
  SOCIAL_SHARES_RANK = 31;
  CHAT_MESSAGES_RANK = 32;
  FRIENDS_ADDED_RANK = 33;
  FRIEND_INVITES_SENT_RANK = 34;
}

message ProductActivityRankingsProperty {
  oneof _daily_time_on_platform_in_seconds_rank {
  double daily_time_on_platform_in_seconds_rank = 1;
  }
  oneof _friend_games_rank {
  double friend_games_rank 
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10748"></a>
## FND-10748: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.CHAT_MESSAGES_RANK = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHAT_MESSAGES_RANK = 32;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1153.

```text
S_TV_EVENT_VIEWS_RANK = 29;
  ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30;
  SOCIAL_SHARES_RANK = 31;
  CHAT_MESSAGES_RANK = 32;
  FRIENDS_ADDED_RANK = 33;
  FRIEND_INVITES_SENT_RANK = 34;
}

message ProductActivityRankingsProperty {
  oneof _daily_time_on_platform_in_seconds_rank {
  double daily_time_on_platform_in_seconds_rank = 1;
  }
  oneof _friend_games_rank {
  double friend_games_rank = 2;
  }
  oneof _daily_mov
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10749"></a>
## FND-10749: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.FRIENDS_ADDED_RANK = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIENDS_ADDED_RANK = 33;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1180.

```text

  ARTICLE_NEWS_BLOG_FORUM_VIEWS_RANK = 30;
  SOCIAL_SHARES_RANK = 31;
  CHAT_MESSAGES_RANK = 32;
  FRIENDS_ADDED_RANK = 33;
  FRIEND_INVITES_SENT_RANK = 34;
}

message ProductActivityRankingsProperty {
  oneof _daily_time_on_platform_in_seconds_rank {
  double daily_time_on_platform_in_seconds_rank = 1;
  }
  oneof _friend_games_rank {
  double friend_games_rank = 2;
  }
  oneof _daily_moves_rank {
  double daily_mo
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10750"></a>
## FND-10750: chesscom.user_properties.v1.ProductActivityRankingsPropertyDefinition.FRIEND_INVITES_SENT_RANK = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIEND_INVITES_SENT_RANK = 34;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1207.

```text
VIEWS_RANK = 30;
  SOCIAL_SHARES_RANK = 31;
  CHAT_MESSAGES_RANK = 32;
  FRIENDS_ADDED_RANK = 33;
  FRIEND_INVITES_SENT_RANK = 34;
}

message ProductActivityRankingsProperty {
  oneof _daily_time_on_platform_in_seconds_rank {
  double daily_time_on_platform_in_seconds_rank = 1;
  }
  oneof _friend_games_rank {
  double friend_games_rank = 2;
  }
  oneof _daily_moves_rank {
  double daily_moves_rank = 3;
  }
  oneof _
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10751"></a>
## FND-10751: message declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ProductActivityRankingsProperty {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1241.

```text
ANK = 31;
  CHAT_MESSAGES_RANK = 32;
  FRIENDS_ADDED_RANK = 33;
  FRIEND_INVITES_SENT_RANK = 34;
}

message ProductActivityRankingsProperty {
  oneof _daily_time_on_platform_in_seconds_rank {
  double daily_time_on_platform_in_seconds_rank = 1;
  }
  oneof _friend_games_rank {
  double friend_games_rank = 2;
  }
  oneof _daily_moves_rank {
  double daily_moves_rank = 3;
  }
  oneof _lesson_activity_rank {
  double le
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10752"></a>
## FND-10752: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._daily_time_on_platform_in_seconds_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _daily_time_on_platform_in_seconds_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1285.

```text
DS_ADDED_RANK = 33;
  FRIEND_INVITES_SENT_RANK = 34;
}

message ProductActivityRankingsProperty {
  oneof _daily_time_on_platform_in_seconds_rank {
  double daily_time_on_platform_in_seconds_rank = 1;
  }
  oneof _friend_games_rank {
  double friend_games_rank = 2;
  }
  oneof _daily_moves_rank {
  double daily_moves_rank = 3;
  }
  oneof _lesson_activity_rank {
  double lesson_activity_rank = 4;
  }
  oneof _game_re
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10753"></a>
## FND-10753: chesscom.user_properties.v1.ProductActivityRankingsProperty.daily_time_on_platform_in_seconds_rank = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double daily_time_on_platform_in_seconds_rank = 1;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1335.

```text
4;
}

message ProductActivityRankingsProperty {
  oneof _daily_time_on_platform_in_seconds_rank {
  double daily_time_on_platform_in_seconds_rank = 1;
  }
  oneof _friend_games_rank {
  double friend_games_rank = 2;
  }
  oneof _daily_moves_rank {
  double daily_moves_rank = 3;
  }
  oneof _lesson_activity_rank {
  double lesson_activity_rank = 4;
  }
  oneof _game_reviews_started_rank {
  double game_reviews_started
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10754"></a>
## FND-10754: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._friend_games_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _friend_games_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1392.

```text
daily_time_on_platform_in_seconds_rank {
  double daily_time_on_platform_in_seconds_rank = 1;
  }
  oneof _friend_games_rank {
  double friend_games_rank = 2;
  }
  oneof _daily_moves_rank {
  double daily_moves_rank = 3;
  }
  oneof _lesson_activity_rank {
  double lesson_activity_rank = 4;
  }
  oneof _game_reviews_started_rank {
  double game_reviews_started_rank = 5;
  }
  oneof _game_review_activity_rank {
  dou
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10755"></a>
## FND-10755: chesscom.user_properties.v1.ProductActivityRankingsProperty.friend_games_rank = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double friend_games_rank = 2;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1421.

```text
onds_rank {
  double daily_time_on_platform_in_seconds_rank = 1;
  }
  oneof _friend_games_rank {
  double friend_games_rank = 2;
  }
  oneof _daily_moves_rank {
  double daily_moves_rank = 3;
  }
  oneof _lesson_activity_rank {
  double lesson_activity_rank = 4;
  }
  oneof _game_reviews_started_rank {
  double game_reviews_started_rank = 5;
  }
  oneof _game_review_activity_rank {
  double game_review_activity_rank
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10756"></a>
## FND-10756: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._daily_moves_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _daily_moves_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1457.

```text
latform_in_seconds_rank = 1;
  }
  oneof _friend_games_rank {
  double friend_games_rank = 2;
  }
  oneof _daily_moves_rank {
  double daily_moves_rank = 3;
  }
  oneof _lesson_activity_rank {
  double lesson_activity_rank = 4;
  }
  oneof _game_reviews_started_rank {
  double game_reviews_started_rank = 5;
  }
  oneof _game_review_activity_rank {
  double game_review_activity_rank = 6;
  }
  oneof _article_activity_
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10757"></a>
## FND-10757: chesscom.user_properties.v1.ProductActivityRankingsProperty.daily_moves_rank = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double daily_moves_rank = 3;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1485.

```text

  }
  oneof _friend_games_rank {
  double friend_games_rank = 2;
  }
  oneof _daily_moves_rank {
  double daily_moves_rank = 3;
  }
  oneof _lesson_activity_rank {
  double lesson_activity_rank = 4;
  }
  oneof _game_reviews_started_rank {
  double game_reviews_started_rank = 5;
  }
  oneof _game_review_activity_rank {
  double game_review_activity_rank = 6;
  }
  oneof _article_activity_rank {
  double article_acti
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10758"></a>
## FND-10758: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._lesson_activity_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _lesson_activity_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1520.

```text
 double friend_games_rank = 2;
  }
  oneof _daily_moves_rank {
  double daily_moves_rank = 3;
  }
  oneof _lesson_activity_rank {
  double lesson_activity_rank = 4;
  }
  oneof _game_reviews_started_rank {
  double game_reviews_started_rank = 5;
  }
  oneof _game_review_activity_rank {
  double game_review_activity_rank = 6;
  }
  oneof _article_activity_rank {
  double article_activity_rank = 7;
  }
  oneof _events_
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10759"></a>
## FND-10759: chesscom.user_properties.v1.ProductActivityRankingsProperty.lesson_activity_rank = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double lesson_activity_rank = 4;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1552.

```text
 }
  oneof _daily_moves_rank {
  double daily_moves_rank = 3;
  }
  oneof _lesson_activity_rank {
  double lesson_activity_rank = 4;
  }
  oneof _game_reviews_started_rank {
  double game_reviews_started_rank = 5;
  }
  oneof _game_review_activity_rank {
  double game_review_activity_rank = 6;
  }
  oneof _article_activity_rank {
  double article_activity_rank = 7;
  }
  oneof _events_activity_rank {
  double events_
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10760"></a>
## FND-10760: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._game_reviews_started_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_reviews_started_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1591.

```text
 daily_moves_rank = 3;
  }
  oneof _lesson_activity_rank {
  double lesson_activity_rank = 4;
  }
  oneof _game_reviews_started_rank {
  double game_reviews_started_rank = 5;
  }
  oneof _game_review_activity_rank {
  double game_review_activity_rank = 6;
  }
  oneof _article_activity_rank {
  double article_activity_rank = 7;
  }
  oneof _events_activity_rank {
  double events_activity_rank = 8;
  }
  oneof _vs_coac
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10761"></a>
## FND-10761: chesscom.user_properties.v1.ProductActivityRankingsProperty.game_reviews_started_rank = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double game_reviews_started_rank = 5;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1628.

```text
esson_activity_rank {
  double lesson_activity_rank = 4;
  }
  oneof _game_reviews_started_rank {
  double game_reviews_started_rank = 5;
  }
  oneof _game_review_activity_rank {
  double game_review_activity_rank = 6;
  }
  oneof _article_activity_rank {
  double article_activity_rank = 7;
  }
  oneof _events_activity_rank {
  double events_activity_rank = 8;
  }
  oneof _vs_coach_activity_rank {
  double vs_coach_a
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10762"></a>
## FND-10762: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._game_review_activity_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_review_activity_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1672.

```text
ty_rank = 4;
  }
  oneof _game_reviews_started_rank {
  double game_reviews_started_rank = 5;
  }
  oneof _game_review_activity_rank {
  double game_review_activity_rank = 6;
  }
  oneof _article_activity_rank {
  double article_activity_rank = 7;
  }
  oneof _events_activity_rank {
  double events_activity_rank = 8;
  }
  oneof _vs_coach_activity_rank {
  double vs_coach_activity_rank = 9;
  }
  oneof _vs_coach_game
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10763"></a>
## FND-10763: chesscom.user_properties.v1.ProductActivityRankingsProperty.game_review_activity_rank = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double game_review_activity_rank = 6;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1709.

```text
s_started_rank {
  double game_reviews_started_rank = 5;
  }
  oneof _game_review_activity_rank {
  double game_review_activity_rank = 6;
  }
  oneof _article_activity_rank {
  double article_activity_rank = 7;
  }
  oneof _events_activity_rank {
  double events_activity_rank = 8;
  }
  oneof _vs_coach_activity_rank {
  double vs_coach_activity_rank = 9;
  }
  oneof _vs_coach_games_rank {
  double vs_coach_games_rank
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10764"></a>
## FND-10764: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._article_activity_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _article_activity_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1753.

```text
ed_rank = 5;
  }
  oneof _game_review_activity_rank {
  double game_review_activity_rank = 6;
  }
  oneof _article_activity_rank {
  double article_activity_rank = 7;
  }
  oneof _events_activity_rank {
  double events_activity_rank = 8;
  }
  oneof _vs_coach_activity_rank {
  double vs_coach_activity_rank = 9;
  }
  oneof _vs_coach_games_rank {
  double vs_coach_games_rank = 10;
  }
  oneof _live_bullet_games_rank {
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10765"></a>
## FND-10765: chesscom.user_properties.v1.ProductActivityRankingsProperty.article_activity_rank = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double article_activity_rank = 7;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1786.

```text
view_activity_rank {
  double game_review_activity_rank = 6;
  }
  oneof _article_activity_rank {
  double article_activity_rank = 7;
  }
  oneof _events_activity_rank {
  double events_activity_rank = 8;
  }
  oneof _vs_coach_activity_rank {
  double vs_coach_activity_rank = 9;
  }
  oneof _vs_coach_games_rank {
  double vs_coach_games_rank = 10;
  }
  oneof _live_bullet_games_rank {
  double live_bullet_games_rank 
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10766"></a>
## FND-10766: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._events_activity_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _events_activity_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1826.

```text
w_activity_rank = 6;
  }
  oneof _article_activity_rank {
  double article_activity_rank = 7;
  }
  oneof _events_activity_rank {
  double events_activity_rank = 8;
  }
  oneof _vs_coach_activity_rank {
  double vs_coach_activity_rank = 9;
  }
  oneof _vs_coach_games_rank {
  double vs_coach_games_rank = 10;
  }
  oneof _live_bullet_games_rank {
  double live_bullet_games_rank = 11;
  }
  oneof _live_blitz_games_rank
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10767"></a>
## FND-10767: chesscom.user_properties.v1.ProductActivityRankingsProperty.events_activity_rank = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double events_activity_rank = 8;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1858.

```text
 _article_activity_rank {
  double article_activity_rank = 7;
  }
  oneof _events_activity_rank {
  double events_activity_rank = 8;
  }
  oneof _vs_coach_activity_rank {
  double vs_coach_activity_rank = 9;
  }
  oneof _vs_coach_games_rank {
  double vs_coach_games_rank = 10;
  }
  oneof _live_bullet_games_rank {
  double live_bullet_games_rank = 11;
  }
  oneof _live_blitz_games_rank {
  double live_blitz_games_ran
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10768"></a>
## FND-10768: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._vs_coach_activity_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _vs_coach_activity_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1897.

```text
cle_activity_rank = 7;
  }
  oneof _events_activity_rank {
  double events_activity_rank = 8;
  }
  oneof _vs_coach_activity_rank {
  double vs_coach_activity_rank = 9;
  }
  oneof _vs_coach_games_rank {
  double vs_coach_games_rank = 10;
  }
  oneof _live_bullet_games_rank {
  double live_bullet_games_rank = 11;
  }
  oneof _live_blitz_games_rank {
  double live_blitz_games_rank = 12;
  }
  oneof _live_rapid_games_r
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10769"></a>
## FND-10769: chesscom.user_properties.v1.ProductActivityRankingsProperty.vs_coach_activity_rank = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double vs_coach_activity_rank = 9;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1931.

```text
 _events_activity_rank {
  double events_activity_rank = 8;
  }
  oneof _vs_coach_activity_rank {
  double vs_coach_activity_rank = 9;
  }
  oneof _vs_coach_games_rank {
  double vs_coach_games_rank = 10;
  }
  oneof _live_bullet_games_rank {
  double live_bullet_games_rank = 11;
  }
  oneof _live_blitz_games_rank {
  double live_blitz_games_rank = 12;
  }
  oneof _live_rapid_games_rank {
  double live_rapid_games_ra
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10770"></a>
## FND-10770: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._vs_coach_games_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _vs_coach_games_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 1972.

```text
activity_rank = 8;
  }
  oneof _vs_coach_activity_rank {
  double vs_coach_activity_rank = 9;
  }
  oneof _vs_coach_games_rank {
  double vs_coach_games_rank = 10;
  }
  oneof _live_bullet_games_rank {
  double live_bullet_games_rank = 11;
  }
  oneof _live_blitz_games_rank {
  double live_blitz_games_rank = 12;
  }
  oneof _live_rapid_games_rank {
  double live_rapid_games_rank = 13;
  }
  oneof _lesson_start_rank {
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10771"></a>
## FND-10771: chesscom.user_properties.v1.ProductActivityRankingsProperty.vs_coach_games_rank = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double vs_coach_games_rank = 10;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2003.

```text
_vs_coach_activity_rank {
  double vs_coach_activity_rank = 9;
  }
  oneof _vs_coach_games_rank {
  double vs_coach_games_rank = 10;
  }
  oneof _live_bullet_games_rank {
  double live_bullet_games_rank = 11;
  }
  oneof _live_blitz_games_rank {
  double live_blitz_games_rank = 12;
  }
  oneof _live_rapid_games_rank {
  double live_rapid_games_rank = 13;
  }
  oneof _lesson_start_rank {
  double lesson_start_rank = 1
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10772"></a>
## FND-10772: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._live_bullet_games_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _live_bullet_games_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2042.

```text
oach_activity_rank = 9;
  }
  oneof _vs_coach_games_rank {
  double vs_coach_games_rank = 10;
  }
  oneof _live_bullet_games_rank {
  double live_bullet_games_rank = 11;
  }
  oneof _live_blitz_games_rank {
  double live_blitz_games_rank = 12;
  }
  oneof _live_rapid_games_rank {
  double live_rapid_games_rank = 13;
  }
  oneof _lesson_start_rank {
  double lesson_start_rank = 14;
  }
  oneof _social_activity_rank {

```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10773"></a>
## FND-10773: chesscom.user_properties.v1.ProductActivityRankingsProperty.live_bullet_games_rank = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double live_bullet_games_rank = 11;

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2076.

```text
f _vs_coach_games_rank {
  double vs_coach_games_rank = 10;
  }
  oneof _live_bullet_games_rank {
  double live_bullet_games_rank = 11;
  }
  oneof _live_blitz_games_rank {
  double live_blitz_games_rank = 12;
  }
  oneof _live_rapid_games_rank {
  double live_rapid_games_rank = 13;
  }
  oneof _lesson_start_rank {
  double lesson_start_rank = 14;
  }
  oneof _social_activity_rank {
  double social_activity_rank = 15
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10774"></a>
## FND-10774: oneof declaration: chesscom.user_properties.v1.ProductActivityRankingsProperty._live_blitz_games_rank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _live_blitz_games_rank {

### Evidence

- **SRC-0621** `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto` — [preserved redacted evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto)
  Character offset 2118.

```text
_games_rank = 10;
  }
  oneof _live_bullet_games_rank {
  double live_bullet_games_rank = 11;
  }
  oneof _live_blitz_games_rank {
  double live_blitz_games_rank = 12;
  }
  oneof _live_rapid_games_rank {
  double live_rapid_games_rank = 13;
  }
  oneof _lesson_start_rank {
  double lesson_start_rank = 14;
  }
  oneof _social_activity_rank {
  double social_activity_rank = 15;
  }
  oneof _bot_games_rank {
  double b
```

**Source references:** SRC-0621, SRC-1592  
**URL references:** None independently associated  
**Related findings:** FND-10715, FND-10716, FND-10717

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
