# data_models — findings 11401–11500

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-11675"></a>
## FND-11675: chesscom.user_properties.v1.UserAbuseProperty.abuse_score_light = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 abuse_score_light = 2;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 849.

```text

  oneof _abuse_score_automod {
  int32 abuse_score_automod = 1;
  }
  oneof _abuse_score_light {
  int32 abuse_score_light = 2;
  }
  oneof _abuse_score_heavy {
  int32 abuse_score_heavy = 3;
  }
  oneof _abuse_score_total {
  int32 abuse_score_total = 4;
  }
  oneof _username_abuse_category_score_good {
  float username_abuse_category_score_good = 5;
  }
  oneof _username_abuse_category_score_identity_hate {
  floa
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11676"></a>
## FND-11676: oneof declaration: chesscom.user_properties.v1.UserAbuseProperty._abuse_score_heavy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _abuse_score_heavy {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 884.

```text
nt32 abuse_score_automod = 1;
  }
  oneof _abuse_score_light {
  int32 abuse_score_light = 2;
  }
  oneof _abuse_score_heavy {
  int32 abuse_score_heavy = 3;
  }
  oneof _abuse_score_total {
  int32 abuse_score_total = 4;
  }
  oneof _username_abuse_category_score_good {
  float username_abuse_category_score_good = 5;
  }
  oneof _username_abuse_category_score_identity_hate {
  float username_abuse_category_score_ide
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11677"></a>
## FND-11677: chesscom.user_properties.v1.UserAbuseProperty.abuse_score_heavy = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 abuse_score_heavy = 3;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 913.

```text

  }
  oneof _abuse_score_light {
  int32 abuse_score_light = 2;
  }
  oneof _abuse_score_heavy {
  int32 abuse_score_heavy = 3;
  }
  oneof _abuse_score_total {
  int32 abuse_score_total = 4;
  }
  oneof _username_abuse_category_score_good {
  float username_abuse_category_score_good = 5;
  }
  oneof _username_abuse_category_score_identity_hate {
  float username_abuse_category_score_identity_hate = 6;
  }
  oneof _
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11678"></a>
## FND-11678: oneof declaration: chesscom.user_properties.v1.UserAbuseProperty._abuse_score_total

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _abuse_score_total {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 948.

```text
 int32 abuse_score_light = 2;
  }
  oneof _abuse_score_heavy {
  int32 abuse_score_heavy = 3;
  }
  oneof _abuse_score_total {
  int32 abuse_score_total = 4;
  }
  oneof _username_abuse_category_score_good {
  float username_abuse_category_score_good = 5;
  }
  oneof _username_abuse_category_score_identity_hate {
  float username_abuse_category_score_identity_hate = 6;
  }
  oneof _username_abuse_category_score_profa
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11679"></a>
## FND-11679: chesscom.user_properties.v1.UserAbuseProperty.abuse_score_total = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 abuse_score_total = 4;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 977.

```text

  }
  oneof _abuse_score_heavy {
  int32 abuse_score_heavy = 3;
  }
  oneof _abuse_score_total {
  int32 abuse_score_total = 4;
  }
  oneof _username_abuse_category_score_good {
  float username_abuse_category_score_good = 5;
  }
  oneof _username_abuse_category_score_identity_hate {
  float username_abuse_category_score_identity_hate = 6;
  }
  oneof _username_abuse_category_score_profanity {
  float username_abuse
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11680"></a>
## FND-11680: oneof declaration: chesscom.user_properties.v1.UserAbuseProperty._username_abuse_category_score_good

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _username_abuse_category_score_good {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1012.

```text
 int32 abuse_score_heavy = 3;
  }
  oneof _abuse_score_total {
  int32 abuse_score_total = 4;
  }
  oneof _username_abuse_category_score_good {
  float username_abuse_category_score_good = 5;
  }
  oneof _username_abuse_category_score_identity_hate {
  float username_abuse_category_score_identity_hate = 6;
  }
  oneof _username_abuse_category_score_profanity {
  float username_abuse_category_score_profanity = 7;
  }

```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11681"></a>
## FND-11681: chesscom.user_properties.v1.UserAbuseProperty.username_abuse_category_score_good = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float username_abuse_category_score_good = 5;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1058.

```text
se_score_total {
  int32 abuse_score_total = 4;
  }
  oneof _username_abuse_category_score_good {
  float username_abuse_category_score_good = 5;
  }
  oneof _username_abuse_category_score_identity_hate {
  float username_abuse_category_score_identity_hate = 6;
  }
  oneof _username_abuse_category_score_profanity {
  float username_abuse_category_score_profanity = 7;
  }
  oneof _username_abuse_category_score_sexual 
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11682"></a>
## FND-11682: oneof declaration: chesscom.user_properties.v1.UserAbuseProperty._username_abuse_category_score_identity_hate

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _username_abuse_category_score_identity_hate {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1110.

```text
  oneof _username_abuse_category_score_good {
  float username_abuse_category_score_good = 5;
  }
  oneof _username_abuse_category_score_identity_hate {
  float username_abuse_category_score_identity_hate = 6;
  }
  oneof _username_abuse_category_score_profanity {
  float username_abuse_category_score_profanity = 7;
  }
  oneof _username_abuse_category_score_sexual {
  float username_abuse_category_score_sexual = 8;

```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11683"></a>
## FND-11683: chesscom.user_properties.v1.UserAbuseProperty.username_abuse_category_score_identity_hate = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float username_abuse_category_score_identity_hate = 6;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1165.

```text
sername_abuse_category_score_good = 5;
  }
  oneof _username_abuse_category_score_identity_hate {
  float username_abuse_category_score_identity_hate = 6;
  }
  oneof _username_abuse_category_score_profanity {
  float username_abuse_category_score_profanity = 7;
  }
  oneof _username_abuse_category_score_sexual {
  float username_abuse_category_score_sexual = 8;
  }
  oneof _username_abuse_category_score_violent {
  
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11684"></a>
## FND-11684: oneof declaration: chesscom.user_properties.v1.UserAbuseProperty._username_abuse_category_score_profanity

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _username_abuse_category_score_profanity {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1226.

```text
abuse_category_score_identity_hate {
  float username_abuse_category_score_identity_hate = 6;
  }
  oneof _username_abuse_category_score_profanity {
  float username_abuse_category_score_profanity = 7;
  }
  oneof _username_abuse_category_score_sexual {
  float username_abuse_category_score_sexual = 8;
  }
  oneof _username_abuse_category_score_violent {
  float username_abuse_category_score_violent = 9;
  }
  oneof 
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11685"></a>
## FND-11685: chesscom.user_properties.v1.UserAbuseProperty.username_abuse_category_score_profanity = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float username_abuse_category_score_profanity = 7;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1277.

```text
me_abuse_category_score_identity_hate = 6;
  }
  oneof _username_abuse_category_score_profanity {
  float username_abuse_category_score_profanity = 7;
  }
  oneof _username_abuse_category_score_sexual {
  float username_abuse_category_score_sexual = 8;
  }
  oneof _username_abuse_category_score_violent {
  float username_abuse_category_score_violent = 9;
  }
  oneof _username_abuse_category_score_pedophilic {
  float
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11686"></a>
## FND-11686: oneof declaration: chesscom.user_properties.v1.UserAbuseProperty._username_abuse_category_score_sexual

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _username_abuse_category_score_sexual {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1334.

```text
sername_abuse_category_score_profanity {
  float username_abuse_category_score_profanity = 7;
  }
  oneof _username_abuse_category_score_sexual {
  float username_abuse_category_score_sexual = 8;
  }
  oneof _username_abuse_category_score_violent {
  float username_abuse_category_score_violent = 9;
  }
  oneof _username_abuse_category_score_pedophilic {
  float username_abuse_category_score_pedophilic = 10;
  }
  one
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11687"></a>
## FND-11687: chesscom.user_properties.v1.UserAbuseProperty.username_abuse_category_score_sexual = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float username_abuse_category_score_sexual = 8;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1382.

```text
 username_abuse_category_score_profanity = 7;
  }
  oneof _username_abuse_category_score_sexual {
  float username_abuse_category_score_sexual = 8;
  }
  oneof _username_abuse_category_score_violent {
  float username_abuse_category_score_violent = 9;
  }
  oneof _username_abuse_category_score_pedophilic {
  float username_abuse_category_score_pedophilic = 10;
  }
  oneof _last_username_abuse_prediction_date {
  .goo
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11688"></a>
## FND-11688: oneof declaration: chesscom.user_properties.v1.UserAbuseProperty._username_abuse_category_score_violent

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _username_abuse_category_score_violent {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1436.

```text
eof _username_abuse_category_score_sexual {
  float username_abuse_category_score_sexual = 8;
  }
  oneof _username_abuse_category_score_violent {
  float username_abuse_category_score_violent = 9;
  }
  oneof _username_abuse_category_score_pedophilic {
  float username_abuse_category_score_pedophilic = 10;
  }
  oneof _last_username_abuse_prediction_date {
  .google.protobuf.Timestamp last_username_abuse_prediction_
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11689"></a>
## FND-11689: chesscom.user_properties.v1.UserAbuseProperty.username_abuse_category_score_violent = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float username_abuse_category_score_violent = 9;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1485.

```text
at username_abuse_category_score_sexual = 8;
  }
  oneof _username_abuse_category_score_violent {
  float username_abuse_category_score_violent = 9;
  }
  oneof _username_abuse_category_score_pedophilic {
  float username_abuse_category_score_pedophilic = 10;
  }
  oneof _last_username_abuse_prediction_date {
  .google.protobuf.Timestamp last_username_abuse_prediction_date = 11;
  }
  oneof _username_abuse_confidence
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11690"></a>
## FND-11690: oneof declaration: chesscom.user_properties.v1.UserAbuseProperty._username_abuse_category_score_pedophilic

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _username_abuse_category_score_pedophilic {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1540.

```text
f _username_abuse_category_score_violent {
  float username_abuse_category_score_violent = 9;
  }
  oneof _username_abuse_category_score_pedophilic {
  float username_abuse_category_score_pedophilic = 10;
  }
  oneof _last_username_abuse_prediction_date {
  .google.protobuf.Timestamp last_username_abuse_prediction_date = 11;
  }
  oneof _username_abuse_confidence_score {
  float username_abuse_confidence_score = 12;

```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11691"></a>
## FND-11691: chesscom.user_properties.v1.UserAbuseProperty.username_abuse_category_score_pedophilic = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float username_abuse_category_score_pedophilic = 10;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1592.

```text
sername_abuse_category_score_violent = 9;
  }
  oneof _username_abuse_category_score_pedophilic {
  float username_abuse_category_score_pedophilic = 10;
  }
  oneof _last_username_abuse_prediction_date {
  .google.protobuf.Timestamp last_username_abuse_prediction_date = 11;
  }
  oneof _username_abuse_confidence_score {
  float username_abuse_confidence_score = 12;
  }
  oneof _abusive_chat_messages {
  int32 abusive
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11692"></a>
## FND-11692: oneof declaration: chesscom.user_properties.v1.UserAbuseProperty._last_username_abuse_prediction_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_username_abuse_prediction_date {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1651.

```text
name_abuse_category_score_pedophilic {
  float username_abuse_category_score_pedophilic = 10;
  }
  oneof _last_username_abuse_prediction_date {
  .google.protobuf.Timestamp last_username_abuse_prediction_date = 11;
  }
  oneof _username_abuse_confidence_score {
  float username_abuse_confidence_score = 12;
  }
  oneof _abusive_chat_messages {
  int32 abusive_chat_messages = 13;
  }
  oneof _about_last_updated_at {
 
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11693"></a>
## FND-11693: chesscom.user_properties.v1.UserAbuseProperty.last_username_abuse_prediction_date = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_username_abuse_prediction_date = 11;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1698.

```text
username_abuse_category_score_pedophilic = 10;
  }
  oneof _last_username_abuse_prediction_date {
  .google.protobuf.Timestamp last_username_abuse_prediction_date = 11;
  }
  oneof _username_abuse_confidence_score {
  float username_abuse_confidence_score = 12;
  }
  oneof _abusive_chat_messages {
  int32 abusive_chat_messages = 13;
  }
  oneof _about_last_updated_at {
  .google.protobuf.Timestamp about_last_updated_
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11694"></a>
## FND-11694: oneof declaration: chesscom.user_properties.v1.UserAbuseProperty._username_abuse_confidence_score

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _username_abuse_confidence_score {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1773.

```text
buse_prediction_date {
  .google.protobuf.Timestamp last_username_abuse_prediction_date = 11;
  }
  oneof _username_abuse_confidence_score {
  float username_abuse_confidence_score = 12;
  }
  oneof _abusive_chat_messages {
  int32 abusive_chat_messages = 13;
  }
  oneof _about_last_updated_at {
  .google.protobuf.Timestamp about_last_updated_at = 14;
  }
}

```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11695"></a>
## FND-11695: chesscom.user_properties.v1.UserAbuseProperty.username_abuse_confidence_score = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float username_abuse_confidence_score = 12;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1816.

```text
imestamp last_username_abuse_prediction_date = 11;
  }
  oneof _username_abuse_confidence_score {
  float username_abuse_confidence_score = 12;
  }
  oneof _abusive_chat_messages {
  int32 abusive_chat_messages = 13;
  }
  oneof _about_last_updated_at {
  .google.protobuf.Timestamp about_last_updated_at = 14;
  }
}

```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11696"></a>
## FND-11696: oneof declaration: chesscom.user_properties.v1.UserAbuseProperty._abusive_chat_messages

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _abusive_chat_messages {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1866.

```text

  }
  oneof _username_abuse_confidence_score {
  float username_abuse_confidence_score = 12;
  }
  oneof _abusive_chat_messages {
  int32 abusive_chat_messages = 13;
  }
  oneof _about_last_updated_at {
  .google.protobuf.Timestamp about_last_updated_at = 14;
  }
}

```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11697"></a>
## FND-11697: chesscom.user_properties.v1.UserAbuseProperty.abusive_chat_messages = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 abusive_chat_messages = 13;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1899.

```text
idence_score {
  float username_abuse_confidence_score = 12;
  }
  oneof _abusive_chat_messages {
  int32 abusive_chat_messages = 13;
  }
  oneof _about_last_updated_at {
  .google.protobuf.Timestamp about_last_updated_at = 14;
  }
}

```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11698"></a>
## FND-11698: oneof declaration: chesscom.user_properties.v1.UserAbuseProperty._about_last_updated_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _about_last_updated_at {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1939.

```text
nfidence_score = 12;
  }
  oneof _abusive_chat_messages {
  int32 abusive_chat_messages = 13;
  }
  oneof _about_last_updated_at {
  .google.protobuf.Timestamp about_last_updated_at = 14;
  }
}

```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11699"></a>
## FND-11699: chesscom.user_properties.v1.UserAbuseProperty.about_last_updated_at = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp about_last_updated_at = 14;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 1972.

```text
_abusive_chat_messages {
  int32 abusive_chat_messages = 13;
  }
  oneof _about_last_updated_at {
  .google.protobuf.Timestamp about_last_updated_at = 14;
  }
}

```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11700"></a>
## FND-11700: enum declaration: chesscom.user_properties.v1.TurnstilePropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TurnstilePropertyDefinition {

### Evidence

- **SRC-0639** `research/proto/chesscom/user_properties/v1/properties_turnstile.proto` — [preserved redacted evidence](../evidence/text/ebbe6d87208d6a18aa139c6fc677a7703c8f9e51c1e688b6b753962f5adaeb78.proto)
  Character offset 123.

```text
r_properties/v1/properties_turnstile.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum TurnstilePropertyDefinition {
  TURNSTILE_UNSPECIFIED = 0;
  TURNSTILE_REGISTRATION_STATUS = 1;
}

message TurnstileProperty {
  oneof _registration_status {
  string registration_status = 1;
  }
}

```

**Source references:** SRC-0639, SRC-1610  
**URL references:** None independently associated  
**Related findings:** FND-11701, FND-11702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11701"></a>
## FND-11701: chesscom.user_properties.v1.TurnstilePropertyDefinition.TURNSTILE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TURNSTILE_UNSPECIFIED = 0;

### Evidence

- **SRC-0639** `research/proto/chesscom/user_properties/v1/properties_turnstile.proto` — [preserved redacted evidence](../evidence/text/ebbe6d87208d6a18aa139c6fc677a7703c8f9e51c1e688b6b753962f5adaeb78.proto)
  Character offset 160.

```text
proto
// syntax: proto3

package chesscom.user_properties.v1;

enum TurnstilePropertyDefinition {
  TURNSTILE_UNSPECIFIED = 0;
  TURNSTILE_REGISTRATION_STATUS = 1;
}

message TurnstileProperty {
  oneof _registration_status {
  string registration_status = 1;
  }
}

```

**Source references:** SRC-0639, SRC-1610  
**URL references:** None independently associated  
**Related findings:** FND-11700, FND-11702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11702"></a>
## FND-11702: chesscom.user_properties.v1.TurnstilePropertyDefinition.TURNSTILE_REGISTRATION_STATUS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TURNSTILE_REGISTRATION_STATUS = 1;

### Evidence

- **SRC-0639** `research/proto/chesscom/user_properties/v1/properties_turnstile.proto` — [preserved redacted evidence](../evidence/text/ebbe6d87208d6a18aa139c6fc677a7703c8f9e51c1e688b6b753962f5adaeb78.proto)
  Character offset 189.

```text
age chesscom.user_properties.v1;

enum TurnstilePropertyDefinition {
  TURNSTILE_UNSPECIFIED = 0;
  TURNSTILE_REGISTRATION_STATUS = 1;
}

message TurnstileProperty {
  oneof _registration_status {
  string registration_status = 1;
  }
}

```

**Source references:** SRC-0639, SRC-1610  
**URL references:** None independently associated  
**Related findings:** FND-11700, FND-11701

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11703"></a>
## FND-11703: message declaration: chesscom.user_properties.v1.TurnstileProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TurnstileProperty {

### Evidence

- **SRC-0639** `research/proto/chesscom/user_properties/v1/properties_turnstile.proto` — [preserved redacted evidence](../evidence/text/ebbe6d87208d6a18aa139c6fc677a7703c8f9e51c1e688b6b753962f5adaeb78.proto)
  Character offset 227.

```text
 TurnstilePropertyDefinition {
  TURNSTILE_UNSPECIFIED = 0;
  TURNSTILE_REGISTRATION_STATUS = 1;
}

message TurnstileProperty {
  oneof _registration_status {
  string registration_status = 1;
  }
}

```

**Source references:** SRC-0639, SRC-1610  
**URL references:** None independently associated  
**Related findings:** FND-11700, FND-11701, FND-11702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11704"></a>
## FND-11704: oneof declaration: chesscom.user_properties.v1.TurnstileProperty._registration_status

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _registration_status {

### Evidence

- **SRC-0639** `research/proto/chesscom/user_properties/v1/properties_turnstile.proto` — [preserved redacted evidence](../evidence/text/ebbe6d87208d6a18aa139c6fc677a7703c8f9e51c1e688b6b753962f5adaeb78.proto)
  Character offset 257.

```text

  TURNSTILE_UNSPECIFIED = 0;
  TURNSTILE_REGISTRATION_STATUS = 1;
}

message TurnstileProperty {
  oneof _registration_status {
  string registration_status = 1;
  }
}

```

**Source references:** SRC-0639, SRC-1610  
**URL references:** None independently associated  
**Related findings:** FND-11700, FND-11701, FND-11702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11705"></a>
## FND-11705: chesscom.user_properties.v1.TurnstileProperty.registration_status = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string registration_status = 1;

### Evidence

- **SRC-0639** `research/proto/chesscom/user_properties/v1/properties_turnstile.proto` — [preserved redacted evidence](../evidence/text/ebbe6d87208d6a18aa139c6fc677a7703c8f9e51c1e688b6b753962f5adaeb78.proto)
  Character offset 288.

```text
 TURNSTILE_REGISTRATION_STATUS = 1;
}

message TurnstileProperty {
  oneof _registration_status {
  string registration_status = 1;
  }
}

```

**Source references:** SRC-0639, SRC-1610  
**URL references:** None independently associated  
**Related findings:** FND-11700, FND-11701, FND-11702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11706"></a>
## FND-11706: enum declaration: chesscom.user_properties.v1.UserDetailsPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum UserDetailsPropertyDefinition {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 126.

```text
roperties/v1/properties_user_details.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum UserDetailsPropertyDefinition {
  USER_DETAILS_PROPERTY_UNSPECIFIED = 0;
  AVATAR_URL = 1;
  HIGH_RES_AVATAR_URL = 2;
  CONTENT_LANGUAGE_INCLUDES_ENGLISH = 3;
  IS_EMAIL_DELIVERABLE = 4;
  IS_ACTIVATED = 5;
  HAS_OPENED_VERIFICATION_EMAIL = 6;
  REFERRED_BY_METHOD = 9;
  IS_CONTENT_HIDDEN = 10;
  IS_VERIFIED = 11;
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11707"></a>
## FND-11707: chesscom.user_properties.v1.UserDetailsPropertyDefinition.USER_DETAILS_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_DETAILS_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 165.

```text
oto
// syntax: proto3

package chesscom.user_properties.v1;

enum UserDetailsPropertyDefinition {
  USER_DETAILS_PROPERTY_UNSPECIFIED = 0;
  AVATAR_URL = 1;
  HIGH_RES_AVATAR_URL = 2;
  CONTENT_LANGUAGE_INCLUDES_ENGLISH = 3;
  IS_EMAIL_DELIVERABLE = 4;
  IS_ACTIVATED = 5;
  HAS_OPENED_VERIFICATION_EMAIL = 6;
  REFERRED_BY_METHOD = 9;
  IS_CONTENT_HIDDEN = 10;
  IS_VERIFIED = 11;
  HAS_SENDGRID_INVALID_EMAIL = 12;
  L
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11708"></a>
## FND-11708: chesscom.user_properties.v1.UserDetailsPropertyDefinition.AVATAR_URL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

AVATAR_URL = 1;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 206.

```text
ser_properties.v1;

enum UserDetailsPropertyDefinition {
  USER_DETAILS_PROPERTY_UNSPECIFIED = 0;
  AVATAR_URL = 1;
  HIGH_RES_AVATAR_URL = 2;
  CONTENT_LANGUAGE_INCLUDES_ENGLISH = 3;
  IS_EMAIL_DELIVERABLE = 4;
  IS_ACTIVATED = 5;
  HAS_OPENED_VERIFICATION_EMAIL = 6;
  REFERRED_BY_METHOD = 9;
  IS_CONTENT_HIDDEN = 10;
  IS_VERIFIED = 11;
  HAS_SENDGRID_INVALID_EMAIL = 12;
  LAST_BOUNCE_DATE = 13;
  LAST_OPEN_EMAIL_D
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11709"></a>
## FND-11709: chesscom.user_properties.v1.UserDetailsPropertyDefinition.HIGH_RES_AVATAR_URL = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

HIGH_RES_AVATAR_URL = 2;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 224.

```text


enum UserDetailsPropertyDefinition {
  USER_DETAILS_PROPERTY_UNSPECIFIED = 0;
  AVATAR_URL = 1;
  HIGH_RES_AVATAR_URL = 2;
  CONTENT_LANGUAGE_INCLUDES_ENGLISH = 3;
  IS_EMAIL_DELIVERABLE = 4;
  IS_ACTIVATED = 5;
  HAS_OPENED_VERIFICATION_EMAIL = 6;
  REFERRED_BY_METHOD = 9;
  IS_CONTENT_HIDDEN = 10;
  IS_VERIFIED = 11;
  HAS_SENDGRID_INVALID_EMAIL = 12;
  LAST_BOUNCE_DATE = 13;
  LAST_OPEN_EMAIL_DATE = 14;
  LAST_D
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11710"></a>
## FND-11710: chesscom.user_properties.v1.UserDetailsPropertyDefinition.CONTENT_LANGUAGE_INCLUDES_ENGLISH = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CONTENT_LANGUAGE_INCLUDES_ENGLISH = 3;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 251.

```text
efinition {
  USER_DETAILS_PROPERTY_UNSPECIFIED = 0;
  AVATAR_URL = 1;
  HIGH_RES_AVATAR_URL = 2;
  CONTENT_LANGUAGE_INCLUDES_ENGLISH = 3;
  IS_EMAIL_DELIVERABLE = 4;
  IS_ACTIVATED = 5;
  HAS_OPENED_VERIFICATION_EMAIL = 6;
  REFERRED_BY_METHOD = 9;
  IS_CONTENT_HIDDEN = 10;
  IS_VERIFIED = 11;
  HAS_SENDGRID_INVALID_EMAIL = 12;
  LAST_BOUNCE_DATE = 13;
  LAST_OPEN_EMAIL_DATE = 14;
  LAST_DROPPED_EMAIL_DATE = 15;
  L
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11711"></a>
## FND-11711: chesscom.user_properties.v1.UserDetailsPropertyDefinition.IS_EMAIL_DELIVERABLE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_EMAIL_DELIVERABLE = 4;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 292.

```text
CIFIED = 0;
  AVATAR_URL = 1;
  HIGH_RES_AVATAR_URL = 2;
  CONTENT_LANGUAGE_INCLUDES_ENGLISH = 3;
  IS_EMAIL_DELIVERABLE = 4;
  IS_ACTIVATED = 5;
  HAS_OPENED_VERIFICATION_EMAIL = 6;
  REFERRED_BY_METHOD = 9;
  IS_CONTENT_HIDDEN = 10;
  IS_VERIFIED = 11;
  HAS_SENDGRID_INVALID_EMAIL = 12;
  LAST_BOUNCE_DATE = 13;
  LAST_OPEN_EMAIL_DATE = 14;
  LAST_DROPPED_EMAIL_DATE = 15;
  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERS
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11712"></a>
## FND-11712: chesscom.user_properties.v1.UserDetailsPropertyDefinition.IS_ACTIVATED = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_ACTIVATED = 5;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 320.

```text
;
  HIGH_RES_AVATAR_URL = 2;
  CONTENT_LANGUAGE_INCLUDES_ENGLISH = 3;
  IS_EMAIL_DELIVERABLE = 4;
  IS_ACTIVATED = 5;
  HAS_OPENED_VERIFICATION_EMAIL = 6;
  REFERRED_BY_METHOD = 9;
  IS_CONTENT_HIDDEN = 10;
  IS_VERIFIED = 11;
  HAS_SENDGRID_INVALID_EMAIL = 12;
  LAST_BOUNCE_DATE = 13;
  LAST_OPEN_EMAIL_DATE = 14;
  LAST_DROPPED_EMAIL_DATE = 15;
  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED =
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11713"></a>
## FND-11713: chesscom.user_properties.v1.UserDetailsPropertyDefinition.HAS_OPENED_VERIFICATION_EMAIL = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

HAS_OPENED_VERIFICATION_EMAIL = 6;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 340.

```text
URL = 2;
  CONTENT_LANGUAGE_INCLUDES_ENGLISH = 3;
  IS_EMAIL_DELIVERABLE = 4;
  IS_ACTIVATED = 5;
  HAS_OPENED_VERIFICATION_EMAIL = 6;
  REFERRED_BY_METHOD = 9;
  IS_CONTENT_HIDDEN = 10;
  IS_VERIFIED = 11;
  HAS_SENDGRID_INVALID_EMAIL = 12;
  LAST_BOUNCE_DATE = 13;
  LAST_OPEN_EMAIL_DATE = 14;
  LAST_DROPPED_EMAIL_DATE = 15;
  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED = 18;
  SKILL_LEVEL =
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11714"></a>
## FND-11714: chesscom.user_properties.v1.UserDetailsPropertyDefinition.REFERRED_BY_METHOD = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

REFERRED_BY_METHOD = 9;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 377.

```text
ENGLISH = 3;
  IS_EMAIL_DELIVERABLE = 4;
  IS_ACTIVATED = 5;
  HAS_OPENED_VERIFICATION_EMAIL = 6;
  REFERRED_BY_METHOD = 9;
  IS_CONTENT_HIDDEN = 10;
  IS_VERIFIED = 11;
  HAS_SENDGRID_INVALID_EMAIL = 12;
  LAST_BOUNCE_DATE = 13;
  LAST_OPEN_EMAIL_DATE = 14;
  LAST_DROPPED_EMAIL_DATE = 15;
  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED = 18;
  SKILL_LEVEL = 19;
  LAST_CLICK_EMAIL_DATE = 20;
  
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11715"></a>
## FND-11715: chesscom.user_properties.v1.UserDetailsPropertyDefinition.IS_CONTENT_HIDDEN = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_CONTENT_HIDDEN = 10;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 403.

```text
LIVERABLE = 4;
  IS_ACTIVATED = 5;
  HAS_OPENED_VERIFICATION_EMAIL = 6;
  REFERRED_BY_METHOD = 9;
  IS_CONTENT_HIDDEN = 10;
  IS_VERIFIED = 11;
  HAS_SENDGRID_INVALID_EMAIL = 12;
  LAST_BOUNCE_DATE = 13;
  LAST_OPEN_EMAIL_DATE = 14;
  LAST_DROPPED_EMAIL_DATE = 15;
  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED = 18;
  SKILL_LEVEL = 19;
  LAST_CLICK_EMAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11716"></a>
## FND-11716: chesscom.user_properties.v1.UserDetailsPropertyDefinition.IS_VERIFIED = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_VERIFIED = 11;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 429.

```text
TED = 5;
  HAS_OPENED_VERIFICATION_EMAIL = 6;
  REFERRED_BY_METHOD = 9;
  IS_CONTENT_HIDDEN = 10;
  IS_VERIFIED = 11;
  HAS_SENDGRID_INVALID_EMAIL = 12;
  LAST_BOUNCE_DATE = 13;
  LAST_OPEN_EMAIL_DATE = 14;
  LAST_DROPPED_EMAIL_DATE = 15;
  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED = 18;
  SKILL_LEVEL = 19;
  LAST_CLICK_EMAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 21;
  IS_PAWNIVERSARY_TOMO
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11717"></a>
## FND-11717: chesscom.user_properties.v1.UserDetailsPropertyDefinition.HAS_SENDGRID_INVALID_EMAIL = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

HAS_SENDGRID_INVALID_EMAIL = 12;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 449.

```text
D_VERIFICATION_EMAIL = 6;
  REFERRED_BY_METHOD = 9;
  IS_CONTENT_HIDDEN = 10;
  IS_VERIFIED = 11;
  HAS_SENDGRID_INVALID_EMAIL = 12;
  LAST_BOUNCE_DATE = 13;
  LAST_OPEN_EMAIL_DATE = 14;
  LAST_DROPPED_EMAIL_DATE = 15;
  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED = 18;
  SKILL_LEVEL = 19;
  LAST_CLICK_EMAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 21;
  IS_PAWNIVERSARY_TOMORROW = 22;
  IS_GUES
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11718"></a>
## FND-11718: chesscom.user_properties.v1.UserDetailsPropertyDefinition.LAST_BOUNCE_DATE = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_BOUNCE_DATE = 13;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 484.

```text
D_BY_METHOD = 9;
  IS_CONTENT_HIDDEN = 10;
  IS_VERIFIED = 11;
  HAS_SENDGRID_INVALID_EMAIL = 12;
  LAST_BOUNCE_DATE = 13;
  LAST_OPEN_EMAIL_DATE = 14;
  LAST_DROPPED_EMAIL_DATE = 15;
  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED = 18;
  SKILL_LEVEL = 19;
  LAST_CLICK_EMAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 21;
  IS_PAWNIVERSARY_TOMORROW = 22;
  IS_GUEST = 23;
  USER_RIGHT_TO_BE_FORGOTTE
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11719"></a>
## FND-11719: chesscom.user_properties.v1.UserDetailsPropertyDefinition.LAST_OPEN_EMAIL_DATE = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_OPEN_EMAIL_DATE = 14;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 509.

```text
TENT_HIDDEN = 10;
  IS_VERIFIED = 11;
  HAS_SENDGRID_INVALID_EMAIL = 12;
  LAST_BOUNCE_DATE = 13;
  LAST_OPEN_EMAIL_DATE = 14;
  LAST_DROPPED_EMAIL_DATE = 15;
  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED = 18;
  SKILL_LEVEL = 19;
  LAST_CLICK_EMAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 21;
  IS_PAWNIVERSARY_TOMORROW = 22;
  IS_GUEST = 23;
  USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25;
  NEXT_PAW
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11720"></a>
## FND-11720: chesscom.user_properties.v1.UserDetailsPropertyDefinition.LAST_DROPPED_EMAIL_DATE = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_DROPPED_EMAIL_DATE = 15;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 538.

```text
ED = 11;
  HAS_SENDGRID_INVALID_EMAIL = 12;
  LAST_BOUNCE_DATE = 13;
  LAST_OPEN_EMAIL_DATE = 14;
  LAST_DROPPED_EMAIL_DATE = 15;
  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED = 18;
  SKILL_LEVEL = 19;
  LAST_CLICK_EMAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 21;
  IS_PAWNIVERSARY_TOMORROW = 22;
  IS_GUEST = 23;
  USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25;
  NEXT_PAWNIVERSARY_START_DATE = 26;
  
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11721"></a>
## FND-11721: chesscom.user_properties.v1.UserDetailsPropertyDefinition.LAST_SPAM_REPORT_DATE = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_SPAM_REPORT_DATE = 16;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 570.

```text
EMAIL = 12;
  LAST_BOUNCE_DATE = 13;
  LAST_OPEN_EMAIL_DATE = 14;
  LAST_DROPPED_EMAIL_DATE = 15;
  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED = 18;
  SKILL_LEVEL = 19;
  LAST_CLICK_EMAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 21;
  IS_PAWNIVERSARY_TOMORROW = 22;
  IS_GUEST = 23;
  USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25;
  NEXT_PAWNIVERSARY_START_DATE = 26;
  EXPERIMENT_BUCKETING_RESULTS = 2
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11722"></a>
## FND-11722: chesscom.user_properties.v1.UserDetailsPropertyDefinition.IS_PAWNIVERSARY = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_PAWNIVERSARY = 17;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 600.

```text
 = 13;
  LAST_OPEN_EMAIL_DATE = 14;
  LAST_DROPPED_EMAIL_DATE = 15;
  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED = 18;
  SKILL_LEVEL = 19;
  LAST_CLICK_EMAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 21;
  IS_PAWNIVERSARY_TOMORROW = 22;
  IS_GUEST = 23;
  USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25;
  NEXT_PAWNIVERSARY_START_DATE = 26;
  EXPERIMENT_BUCKETING_RESULTS = 27;
  OPT_IN_STATUS = 28;
  ACC
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11723"></a>
## FND-11723: chesscom.user_properties.v1.UserDetailsPropertyDefinition.IS_REACTIVATED = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_REACTIVATED = 18;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 624.

```text
_DATE = 14;
  LAST_DROPPED_EMAIL_DATE = 15;
  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED = 18;
  SKILL_LEVEL = 19;
  LAST_CLICK_EMAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 21;
  IS_PAWNIVERSARY_TOMORROW = 22;
  IS_GUEST = 23;
  USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25;
  NEXT_PAWNIVERSARY_START_DATE = 26;
  EXPERIMENT_BUCKETING_RESULTS = 27;
  OPT_IN_STATUS = 28;
  ACCOUNT_STATUS = 29;
  CLOS
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11724"></a>
## FND-11724: chesscom.user_properties.v1.UserDetailsPropertyDefinition.SKILL_LEVEL = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_LEVEL = 19;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 647.

```text
PED_EMAIL_DATE = 15;
  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED = 18;
  SKILL_LEVEL = 19;
  LAST_CLICK_EMAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 21;
  IS_PAWNIVERSARY_TOMORROW = 22;
  IS_GUEST = 23;
  USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25;
  NEXT_PAWNIVERSARY_START_DATE = 26;
  EXPERIMENT_BUCKETING_RESULTS = 27;
  OPT_IN_STATUS = 28;
  ACCOUNT_STATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSUR
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11725"></a>
## FND-11725: chesscom.user_properties.v1.UserDetailsPropertyDefinition.LAST_CLICK_EMAIL_DATE = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_CLICK_EMAIL_DATE = 20;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 667.

```text

  LAST_SPAM_REPORT_DATE = 16;
  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED = 18;
  SKILL_LEVEL = 19;
  LAST_CLICK_EMAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 21;
  IS_PAWNIVERSARY_TOMORROW = 22;
  IS_GUEST = 23;
  USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25;
  NEXT_PAWNIVERSARY_START_DATE = 26;
  EXPERIMENT_BUCKETING_RESULTS = 27;
  OPT_IN_STATUS = 28;
  ACCOUNT_STATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACT
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11726"></a>
## FND-11726: chesscom.user_properties.v1.UserDetailsPropertyDefinition.IS_ON_DO_NOT_EMAIL_LIST = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_ON_DO_NOT_EMAIL_LIST = 21;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 697.

```text

  IS_PAWNIVERSARY = 17;
  IS_REACTIVATED = 18;
  SKILL_LEVEL = 19;
  LAST_CLICK_EMAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 21;
  IS_PAWNIVERSARY_TOMORROW = 22;
  IS_GUEST = 23;
  USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25;
  NEXT_PAWNIVERSARY_START_DATE = 26;
  EXPERIMENT_BUCKETING_RESULTS = 27;
  OPT_IN_STATUS = 28;
  ACCOUNT_STATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATA
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11727"></a>
## FND-11727: chesscom.user_properties.v1.UserDetailsPropertyDefinition.IS_PAWNIVERSARY_TOMORROW = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_PAWNIVERSARY_TOMORROW = 22;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 729.

```text
ACTIVATED = 18;
  SKILL_LEVEL = 19;
  LAST_CLICK_EMAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 21;
  IS_PAWNIVERSARY_TOMORROW = 22;
  IS_GUEST = 23;
  USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25;
  NEXT_PAWNIVERSARY_START_DATE = 26;
  EXPERIMENT_BUCKETING_RESULTS = 27;
  OPT_IN_STATUS = 28;
  ACCOUNT_STATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGU
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11728"></a>
## FND-11728: chesscom.user_properties.v1.UserDetailsPropertyDefinition.IS_GUEST = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_GUEST = 23;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 762.

```text
9;
  LAST_CLICK_EMAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 21;
  IS_PAWNIVERSARY_TOMORROW = 22;
  IS_GUEST = 23;
  USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25;
  NEXT_PAWNIVERSARY_START_DATE = 26;
  EXPERIMENT_BUCKETING_RESULTS = 27;
  OPT_IN_STATUS = 28;
  ACCOUNT_STATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TO
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11729"></a>
## FND-11729: chesscom.user_properties.v1.UserDetailsPropertyDefinition.USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 779.

```text
MAIL_DATE = 20;
  IS_ON_DO_NOT_EMAIL_LIST = 21;
  IS_PAWNIVERSARY_TOMORROW = 22;
  IS_GUEST = 23;
  USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25;
  NEXT_PAWNIVERSARY_START_DATE = 26;
  EXPERIMENT_BUCKETING_RESULTS = 27;
  OPT_IN_STATUS = 28;
  ACCOUNT_STATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_I
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11730"></a>
## FND-11730: chesscom.user_properties.v1.UserDetailsPropertyDefinition.NEXT_PAWNIVERSARY_START_DATE = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NEXT_PAWNIVERSARY_START_DATE = 26;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 821.

```text
= 21;
  IS_PAWNIVERSARY_TOMORROW = 22;
  IS_GUEST = 23;
  USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25;
  NEXT_PAWNIVERSARY_START_DATE = 26;
  EXPERIMENT_BUCKETING_RESULTS = 27;
  OPT_IN_STATUS = 28;
  ACCOUNT_STATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11731"></a>
## FND-11731: chesscom.user_properties.v1.UserDetailsPropertyDefinition.EXPERIMENT_BUCKETING_RESULTS = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EXPERIMENT_BUCKETING_RESULTS = 27;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 858.

```text
;
  IS_GUEST = 23;
  USER_RIGHT_TO_BE_FORGOTTEN_STATUS = 25;
  NEXT_PAWNIVERSARY_START_DATE = 26;
  EXPERIMENT_BUCKETING_RESULTS = 27;
  OPT_IN_STATUS = 28;
  ACCOUNT_STATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EX
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11732"></a>
## FND-11732: chesscom.user_properties.v1.UserDetailsPropertyDefinition.OPT_IN_STATUS = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

OPT_IN_STATUS = 28;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 895.

```text
_FORGOTTEN_STATUS = 25;
  NEXT_PAWNIVERSARY_START_DATE = 26;
  EXPERIMENT_BUCKETING_RESULTS = 27;
  OPT_IN_STATUS = 28;
  ACCOUNT_STATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_M
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11733"></a>
## FND-11733: chesscom.user_properties.v1.UserDetailsPropertyDefinition.ACCOUNT_STATUS = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ACCOUNT_STATUS = 29;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 917.

```text
;
  NEXT_PAWNIVERSARY_START_DATE = 26;
  EXPERIMENT_BUCKETING_RESULTS = 27;
  OPT_IN_STATUS = 28;
  ACCOUNT_STATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BO
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11734"></a>
## FND-11734: chesscom.user_properties.v1.UserDetailsPropertyDefinition.CLOSURE_TYPE = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLOSURE_TYPE = 30;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 940.

```text
TART_DATE = 26;
  EXPERIMENT_BUCKETING_RESULTS = 27;
  OPT_IN_STATUS = 28;
  ACCOUNT_STATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL =
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11735"></a>
## FND-11735: chesscom.user_properties.v1.UserDetailsPropertyDefinition.CLOSURE_REASON = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLOSURE_REASON = 31;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 961.

```text
ERIMENT_BUCKETING_RESULTS = 27;
  OPT_IN_STATUS = 28;
  ACCOUNT_STATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_Y
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11736"></a>
## FND-11736: chesscom.user_properties.v1.UserDetailsPropertyDefinition.ACTIVATION_TYPE = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ACTIVATION_TYPE = 32;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 984.

```text
TS = 27;
  OPT_IN_STATUS = 28;
  ACCOUNT_STATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RA
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11737"></a>
## FND-11737: chesscom.user_properties.v1.UserDetailsPropertyDefinition.HAS_AVATAR = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

HAS_AVATAR = 33;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1008.

```text
 = 28;
  ACCOUNT_STATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11738"></a>
## FND-11738: chesscom.user_properties.v1.UserDetailsPropertyDefinition.LANGUAGE = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LANGUAGE = 34;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1027.

```text
ATUS = 29;
  CLOSURE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11739"></a>
## FND-11739: chesscom.user_properties.v1.UserDetailsPropertyDefinition.LANGUAGE_CLOUDFLARE = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LANGUAGE_CLOUDFLARE = 35;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1044.

```text
URE_TYPE = 30;
  CLOSURE_REASON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11740"></a>
## FND-11740: chesscom.user_properties.v1.UserDetailsPropertyDefinition.HAS_FCM_TOKEN = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

HAS_FCM_TOKEN = 36;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1072.

```text
SON = 31;
  ACTIVATION_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 4
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11741"></a>
## FND-11741: chesscom.user_properties.v1.UserDetailsPropertyDefinition.HAS_IOS_FCM_TOKEN = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

HAS_IOS_FCM_TOKEN = 37;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1094.

```text
_TYPE = 32;
  HAS_AVATAR = 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  S
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11742"></a>
## FND-11742: chesscom.user_properties.v1.UserDetailsPropertyDefinition.HAS_ANDROID_FCM_TOKEN = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

HAS_ANDROID_FCM_TOKEN = 38;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1120.

```text
 33;
  LANGUAGE = 34;
  LANGUAGE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11743"></a>
## FND-11743: chesscom.user_properties.v1.UserDetailsPropertyDefinition.HAS_WEB_FCM_TOKEN = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

HAS_WEB_FCM_TOKEN = 39;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1150.

```text
GE_CLOUDFLARE = 35;
  HAS_FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATAS
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11744"></a>
## FND-11744: chesscom.user_properties.v1.UserDetailsPropertyDefinition.EXPERIMENT_BUCKETING_ID = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EXPERIMENT_BUCKETING_ID = 40;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1176.

```text
FCM_TOKEN = 36;
  HAS_IOS_FCM_TOKEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_B
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11745"></a>
## FND-11745: chesscom.user_properties.v1.UserDetailsPropertyDefinition.LISTS_MEMBER_OF = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LISTS_MEMBER_OF = 41;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1208.

```text
KEN = 37;
  HAS_ANDROID_FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECT
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11746"></a>
## FND-11746: chesscom.user_properties.v1.UserDetailsPropertyDefinition.IS_BOT = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_BOT = 42;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1232.

```text
FCM_TOKEN = 38;
  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message Use
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11747"></a>
## FND-11747: chesscom.user_properties.v1.UserDetailsPropertyDefinition.TRUST_LEVEL = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRUST_LEVEL = 43;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1247.

```text

  HAS_WEB_FCM_TOKEN = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsPropert
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11748"></a>
## FND-11748: chesscom.user_properties.v1.UserDetailsPropertyDefinition.PAWNIVERSARY_YEARS = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAWNIVERSARY_YEARS = 44;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1267.

```text
 = 39;
  EXPERIMENT_BUCKETING_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11749"></a>
## FND-11749: chesscom.user_properties.v1.UserDetailsPropertyDefinition.INITIAL_RATING = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INITIAL_RATING = 45;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1294.

```text
NG_ID = 40;
  LISTS_MEMBER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_url {
  string avatar_url =
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11750"></a>
## FND-11750: chesscom.user_properties.v1.UserDetailsPropertyDefinition.IS_TRUSTED = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_TRUSTED = 46;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1317.

```text
BER_OF = 41;
  IS_BOT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_url {
  string avatar_url = 1;
  }
  oneof _high_r
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11751"></a>
## FND-11751: chesscom.user_properties.v1.UserDetailsPropertyDefinition.HAS_TWITCH_CONNECTION = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

HAS_TWITCH_CONNECTION = 47;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1336.

```text
OT = 42;
  TRUST_LEVEL = 43;
  PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_url {
  string avatar_url = 1;
  }
  oneof _high_res_avatar_url {
  s
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11752"></a>
## FND-11752: chesscom.user_properties.v1.UserDetailsPropertyDefinition.HAS_YOUTUBE_CONNECTION = 48

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

HAS_YOUTUBE_CONNECTION = 48;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1366.

```text
 PAWNIVERSARY_YEARS = 44;
  INITIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_url {
  string avatar_url = 1;
  }
  oneof _high_res_avatar_url {
  string high_res_avatar_url = 2;
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11753"></a>
## FND-11753: chesscom.user_properties.v1.UserDetailsPropertyDefinition.BLOG_ID = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BLOG_ID = 49;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1397.

```text
TIAL_RATING = 45;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_url {
  string avatar_url = 1;
  }
  oneof _high_res_avatar_url {
  string high_res_avatar_url = 2;
  }
  oneof _content_language_
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11754"></a>
## FND-11754: chesscom.user_properties.v1.UserDetailsPropertyDefinition.STREAM_URL = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STREAM_URL = 50;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1413.

```text
;
  IS_TRUSTED = 46;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_url {
  string avatar_url = 1;
  }
  oneof _high_res_avatar_url {
  string high_res_avatar_url = 2;
  }
  oneof _content_language_includes_english
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11755"></a>
## FND-11755: chesscom.user_properties.v1.UserDetailsPropertyDefinition.CLOSURE_STATUS = 51

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLOSURE_STATUS = 51;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1432.

```text
;
  HAS_TWITCH_CONNECTION = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_url {
  string avatar_url = 1;
  }
  oneof _high_res_avatar_url {
  string high_res_avatar_url = 2;
  }
  oneof _content_language_includes_english {
  bool content_l
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11756"></a>
## FND-11756: chesscom.user_properties.v1.UserDetailsPropertyDefinition.TEMPORARY_DATASETS_MEMBER_OF = 52

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TEMPORARY_DATASETS_MEMBER_OF = 52;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1455.

```text
ON = 47;
  HAS_YOUTUBE_CONNECTION = 48;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_url {
  string avatar_url = 1;
  }
  oneof _high_res_avatar_url {
  string high_res_avatar_url = 2;
  }
  oneof _content_language_includes_english {
  bool content_language_includes_englis
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11757"></a>
## FND-11757: chesscom.user_properties.v1.UserDetailsPropertyDefinition.IS_BETA = 53

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_BETA = 53;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1492.

```text
8;
  BLOG_ID = 49;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_url {
  string avatar_url = 1;
  }
  oneof _high_res_avatar_url {
  string high_res_avatar_url = 2;
  }
  oneof _content_language_includes_english {
  bool content_language_includes_english = 3;
  }
  oneof _is_email_delivera
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11758"></a>
## FND-11758: chesscom.user_properties.v1.UserDetailsPropertyDefinition.HAS_LINKEDIN_CONNECTION = 54

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

HAS_LINKEDIN_CONNECTION = 54;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1508.

```text
9;
  STREAM_URL = 50;
  CLOSURE_STATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_url {
  string avatar_url = 1;
  }
  oneof _high_res_avatar_url {
  string high_res_avatar_url = 2;
  }
  oneof _content_language_includes_english {
  bool content_language_includes_english = 3;
  }
  oneof _is_email_deliverable {
  bool is_
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11759"></a>
## FND-11759: message declaration: chesscom.user_properties.v1.UserDetailsProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserDetailsProperty {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1541.

```text
TATUS = 51;
  TEMPORARY_DATASETS_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_url {
  string avatar_url = 1;
  }
  oneof _high_res_avatar_url {
  string high_res_avatar_url = 2;
  }
  oneof _content_language_includes_english {
  bool content_language_includes_english = 3;
  }
  oneof _is_email_deliverable {
  bool is_email_deliverable = 4;
  }
  oneo
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11760"></a>
## FND-11760: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._avatar_url

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _avatar_url {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1573.

```text
_MEMBER_OF = 52;
  IS_BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_url {
  string avatar_url = 1;
  }
  oneof _high_res_avatar_url {
  string high_res_avatar_url = 2;
  }
  oneof _content_language_includes_english {
  bool content_language_includes_english = 3;
  }
  oneof _is_email_deliverable {
  bool is_email_deliverable = 4;
  }
  oneof _is_activated {
  bool is_acti
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11761"></a>
## FND-11761: chesscom.user_properties.v1.UserDetailsProperty.avatar_url = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string avatar_url = 1;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1595.

```text
BETA = 53;
  HAS_LINKEDIN_CONNECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_url {
  string avatar_url = 1;
  }
  oneof _high_res_avatar_url {
  string high_res_avatar_url = 2;
  }
  oneof _content_language_includes_english {
  bool content_language_includes_english = 3;
  }
  oneof _is_email_deliverable {
  bool is_email_deliverable = 4;
  }
  oneof _is_activated {
  bool is_activated = 5;
  }
  oneof
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11762"></a>
## FND-11762: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._high_res_avatar_url

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _high_res_avatar_url {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1624.

```text
NECTION = 54;
}

message UserDetailsProperty {
  oneof _avatar_url {
  string avatar_url = 1;
  }
  oneof _high_res_avatar_url {
  string high_res_avatar_url = 2;
  }
  oneof _content_language_includes_english {
  bool content_language_includes_english = 3;
  }
  oneof _is_email_deliverable {
  bool is_email_deliverable = 4;
  }
  oneof _is_activated {
  bool is_activated = 5;
  }
  oneof _has_opened_verification_ema
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11763"></a>
## FND-11763: chesscom.user_properties.v1.UserDetailsProperty.high_res_avatar_url = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string high_res_avatar_url = 2;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1655.

```text
tailsProperty {
  oneof _avatar_url {
  string avatar_url = 1;
  }
  oneof _high_res_avatar_url {
  string high_res_avatar_url = 2;
  }
  oneof _content_language_includes_english {
  bool content_language_includes_english = 3;
  }
  oneof _is_email_deliverable {
  bool is_email_deliverable = 4;
  }
  oneof _is_activated {
  bool is_activated = 5;
  }
  oneof _has_opened_verification_email {
  bool has_opened_verifica
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11764"></a>
## FND-11764: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._content_language_includes_english

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _content_language_includes_english {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1693.

```text
  string avatar_url = 1;
  }
  oneof _high_res_avatar_url {
  string high_res_avatar_url = 2;
  }
  oneof _content_language_includes_english {
  bool content_language_includes_english = 3;
  }
  oneof _is_email_deliverable {
  bool is_email_deliverable = 4;
  }
  oneof _is_activated {
  bool is_activated = 5;
  }
  oneof _has_opened_verification_email {
  bool has_opened_verification_email = 6;
  }
  oneof _referred_
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11765"></a>
## FND-11765: chesscom.user_properties.v1.UserDetailsProperty.content_language_includes_english = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool content_language_includes_english = 3;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1738.

```text
s_avatar_url {
  string high_res_avatar_url = 2;
  }
  oneof _content_language_includes_english {
  bool content_language_includes_english = 3;
  }
  oneof _is_email_deliverable {
  bool is_email_deliverable = 4;
  }
  oneof _is_activated {
  bool is_activated = 5;
  }
  oneof _has_opened_verification_email {
  bool has_opened_verification_email = 6;
  }
  oneof _referred_by_method {
  string referred_by_method = 9;

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11766"></a>
## FND-11766: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._is_email_deliverable

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_email_deliverable {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1788.

```text
 }
  oneof _content_language_includes_english {
  bool content_language_includes_english = 3;
  }
  oneof _is_email_deliverable {
  bool is_email_deliverable = 4;
  }
  oneof _is_activated {
  bool is_activated = 5;
  }
  oneof _has_opened_verification_email {
  bool has_opened_verification_email = 6;
  }
  oneof _referred_by_method {
  string referred_by_method = 9;
  }
  oneof _is_content_hidden {
  bool is_content
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11767"></a>
## FND-11767: chesscom.user_properties.v1.UserDetailsProperty.is_email_deliverable = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_email_deliverable = 4;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1820.

```text
ludes_english {
  bool content_language_includes_english = 3;
  }
  oneof _is_email_deliverable {
  bool is_email_deliverable = 4;
  }
  oneof _is_activated {
  bool is_activated = 5;
  }
  oneof _has_opened_verification_email {
  bool has_opened_verification_email = 6;
  }
  oneof _referred_by_method {
  string referred_by_method = 9;
  }
  oneof _is_content_hidden {
  bool is_content_hidden = 10;
  }
  oneof _is_ve
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11768"></a>
## FND-11768: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._is_activated

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_activated {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1857.

```text
ge_includes_english = 3;
  }
  oneof _is_email_deliverable {
  bool is_email_deliverable = 4;
  }
  oneof _is_activated {
  bool is_activated = 5;
  }
  oneof _has_opened_verification_email {
  bool has_opened_verification_email = 6;
  }
  oneof _referred_by_method {
  string referred_by_method = 9;
  }
  oneof _is_content_hidden {
  bool is_content_hidden = 10;
  }
  oneof _is_verified {
  bool is_verified = 11;
  }
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11769"></a>
## FND-11769: chesscom.user_properties.v1.UserDetailsProperty.is_activated = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_activated = 5;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1881.

```text

  }
  oneof _is_email_deliverable {
  bool is_email_deliverable = 4;
  }
  oneof _is_activated {
  bool is_activated = 5;
  }
  oneof _has_opened_verification_email {
  bool has_opened_verification_email = 6;
  }
  oneof _referred_by_method {
  string referred_by_method = 9;
  }
  oneof _is_content_hidden {
  bool is_content_hidden = 10;
  }
  oneof _is_verified {
  bool is_verified = 11;
  }
  oneof _has_sendgrid_i
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11770"></a>
## FND-11770: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._has_opened_verification_email

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _has_opened_verification_email {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1910.

```text
rable {
  bool is_email_deliverable = 4;
  }
  oneof _is_activated {
  bool is_activated = 5;
  }
  oneof _has_opened_verification_email {
  bool has_opened_verification_email = 6;
  }
  oneof _referred_by_method {
  string referred_by_method = 9;
  }
  oneof _is_content_hidden {
  bool is_content_hidden = 10;
  }
  oneof _is_verified {
  bool is_verified = 11;
  }
  oneof _has_sendgrid_invalid_email {
  bool has_sen
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11771"></a>
## FND-11771: chesscom.user_properties.v1.UserDetailsProperty.has_opened_verification_email = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool has_opened_verification_email = 6;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1951.

```text
  }
  oneof _is_activated {
  bool is_activated = 5;
  }
  oneof _has_opened_verification_email {
  bool has_opened_verification_email = 6;
  }
  oneof _referred_by_method {
  string referred_by_method = 9;
  }
  oneof _is_content_hidden {
  bool is_content_hidden = 10;
  }
  oneof _is_verified {
  bool is_verified = 11;
  }
  oneof _has_sendgrid_invalid_email {
  bool has_sendgrid_invalid_email = 12;
  }
  oneof _la
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11772"></a>
## FND-11772: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._referred_by_method

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _referred_by_method {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 1997.

```text
d = 5;
  }
  oneof _has_opened_verification_email {
  bool has_opened_verification_email = 6;
  }
  oneof _referred_by_method {
  string referred_by_method = 9;
  }
  oneof _is_content_hidden {
  bool is_content_hidden = 10;
  }
  oneof _is_verified {
  bool is_verified = 11;
  }
  oneof _has_sendgrid_invalid_email {
  bool has_sendgrid_invalid_email = 12;
  }
  oneof _last_bounce_date {
  .google.protobuf.Timestamp 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11773"></a>
## FND-11773: chesscom.user_properties.v1.UserDetailsProperty.referred_by_method = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string referred_by_method = 9;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2027.

```text
_verification_email {
  bool has_opened_verification_email = 6;
  }
  oneof _referred_by_method {
  string referred_by_method = 9;
  }
  oneof _is_content_hidden {
  bool is_content_hidden = 10;
  }
  oneof _is_verified {
  bool is_verified = 11;
  }
  oneof _has_sendgrid_invalid_email {
  bool has_sendgrid_invalid_email = 12;
  }
  oneof _last_bounce_date {
  .google.protobuf.Timestamp last_bounce_date = 13;
  }
  o
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11774"></a>
## FND-11774: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._is_content_hidden

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_content_hidden {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2064.

```text
ed_verification_email = 6;
  }
  oneof _referred_by_method {
  string referred_by_method = 9;
  }
  oneof _is_content_hidden {
  bool is_content_hidden = 10;
  }
  oneof _is_verified {
  bool is_verified = 11;
  }
  oneof _has_sendgrid_invalid_email {
  bool has_sendgrid_invalid_email = 12;
  }
  oneof _last_bounce_date {
  .google.protobuf.Timestamp last_bounce_date = 13;
  }
  oneof _last_open_email_date {
  .googl
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
