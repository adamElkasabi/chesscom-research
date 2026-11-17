# data_models — findings 11301–11400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-11575"></a>
## FND-11575: oneof declaration: chesscom.user_properties.v1.SubscriptionProperty._current_subscription_renewal_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _current_subscription_renewal_date {

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 4314.

```text
st_subscription_start_date {
  .google.protobuf.Timestamp first_subscription_start_date = 37;
  }
  oneof _current_subscription_renewal_date {
  .google.protobuf.Timestamp current_subscription_renewal_date = 38;
  }
  oneof _last_subscription_cancellation_date {
  .google.protobuf.Timestamp last_subscription_cancellation_date = 39;
  }
  oneof _last_trial_cancellation_date {
  .google.protobuf.Timestamp last_trial_ca
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11576"></a>
## FND-11576: chesscom.user_properties.v1.SubscriptionProperty.current_subscription_renewal_date = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp current_subscription_renewal_date = 38;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 4359.

```text
uf.Timestamp first_subscription_start_date = 37;
  }
  oneof _current_subscription_renewal_date {
  .google.protobuf.Timestamp current_subscription_renewal_date = 38;
  }
  oneof _last_subscription_cancellation_date {
  .google.protobuf.Timestamp last_subscription_cancellation_date = 39;
  }
  oneof _last_trial_cancellation_date {
  .google.protobuf.Timestamp last_trial_cancellation_date = 40;
  }
  oneof _last_subsc
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11577"></a>
## FND-11577: oneof declaration: chesscom.user_properties.v1.SubscriptionProperty._last_subscription_cancellation_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_subscription_cancellation_date {

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 4432.

```text
scription_renewal_date {
  .google.protobuf.Timestamp current_subscription_renewal_date = 38;
  }
  oneof _last_subscription_cancellation_date {
  .google.protobuf.Timestamp last_subscription_cancellation_date = 39;
  }
  oneof _last_trial_cancellation_date {
  .google.protobuf.Timestamp last_trial_cancellation_date = 40;
  }
  oneof _last_subscription_payment_method {
  string last_subscription_payment_method = 41;

```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11578"></a>
## FND-11578: chesscom.user_properties.v1.SubscriptionProperty.last_subscription_cancellation_date = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_subscription_cancellation_date = 39;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 4479.

```text
estamp current_subscription_renewal_date = 38;
  }
  oneof _last_subscription_cancellation_date {
  .google.protobuf.Timestamp last_subscription_cancellation_date = 39;
  }
  oneof _last_trial_cancellation_date {
  .google.protobuf.Timestamp last_trial_cancellation_date = 40;
  }
  oneof _last_subscription_payment_method {
  string last_subscription_payment_method = 41;
  }
  oneof _last_trial_payment_method {
  stri
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11579"></a>
## FND-11579: oneof declaration: chesscom.user_properties.v1.SubscriptionProperty._last_trial_cancellation_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_trial_cancellation_date {

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 4554.

```text
on_cancellation_date {
  .google.protobuf.Timestamp last_subscription_cancellation_date = 39;
  }
  oneof _last_trial_cancellation_date {
  .google.protobuf.Timestamp last_trial_cancellation_date = 40;
  }
  oneof _last_subscription_payment_method {
  string last_subscription_payment_method = 41;
  }
  oneof _last_trial_payment_method {
  string last_trial_payment_method = 42;
  }
  oneof _last_subscription_payment_g
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11580"></a>
## FND-11580: chesscom.user_properties.v1.SubscriptionProperty.last_trial_cancellation_date = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_trial_cancellation_date = 40;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 4594.

```text
f.Timestamp last_subscription_cancellation_date = 39;
  }
  oneof _last_trial_cancellation_date {
  .google.protobuf.Timestamp last_trial_cancellation_date = 40;
  }
  oneof _last_subscription_payment_method {
  string last_subscription_payment_method = 41;
  }
  oneof _last_trial_payment_method {
  string last_trial_payment_method = 42;
  }
  oneof _last_subscription_payment_gateway {
  string last_subscription_paym
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11581"></a>
## FND-11581: oneof declaration: chesscom.user_properties.v1.SubscriptionProperty._last_subscription_payment_method

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_subscription_payment_method {

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 4662.

```text
ast_trial_cancellation_date {
  .google.protobuf.Timestamp last_trial_cancellation_date = 40;
  }
  oneof _last_subscription_payment_method {
  string last_subscription_payment_method = 41;
  }
  oneof _last_trial_payment_method {
  string last_trial_payment_method = 42;
  }
  oneof _last_subscription_payment_gateway {
  string last_subscription_payment_gateway = 43;
  }
  oneof _last_trial_payment_gateway {
  string
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11582"></a>
## FND-11582: chesscom.user_properties.v1.SubscriptionProperty.last_subscription_payment_method = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_subscription_payment_method = 41;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 4706.

```text
obuf.Timestamp last_trial_cancellation_date = 40;
  }
  oneof _last_subscription_payment_method {
  string last_subscription_payment_method = 41;
  }
  oneof _last_trial_payment_method {
  string last_trial_payment_method = 42;
  }
  oneof _last_subscription_payment_gateway {
  string last_subscription_payment_gateway = 43;
  }
  oneof _last_trial_payment_gateway {
  string last_trial_payment_gateway = 44;
  }
  oneo
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11583"></a>
## FND-11583: oneof declaration: chesscom.user_properties.v1.SubscriptionProperty._last_trial_payment_method

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_trial_payment_method {

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 4758.

```text
}
  oneof _last_subscription_payment_method {
  string last_subscription_payment_method = 41;
  }
  oneof _last_trial_payment_method {
  string last_trial_payment_method = 42;
  }
  oneof _last_subscription_payment_gateway {
  string last_subscription_payment_gateway = 43;
  }
  oneof _last_trial_payment_gateway {
  string last_trial_payment_gateway = 44;
  }
  oneof _user_lifecycle_secondary_state {
  string user_li
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11584"></a>
## FND-11584: chesscom.user_properties.v1.SubscriptionProperty.last_trial_payment_method = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_trial_payment_method = 42;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 4795.

```text
method {
  string last_subscription_payment_method = 41;
  }
  oneof _last_trial_payment_method {
  string last_trial_payment_method = 42;
  }
  oneof _last_subscription_payment_gateway {
  string last_subscription_payment_gateway = 43;
  }
  oneof _last_trial_payment_gateway {
  string last_trial_payment_gateway = 44;
  }
  oneof _user_lifecycle_secondary_state {
  string user_lifecycle_secondary_state = 45;
  }
  o
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11585"></a>
## FND-11585: oneof declaration: chesscom.user_properties.v1.SubscriptionProperty._last_subscription_payment_gateway

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_subscription_payment_gateway {

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 4840.

```text
ethod = 41;
  }
  oneof _last_trial_payment_method {
  string last_trial_payment_method = 42;
  }
  oneof _last_subscription_payment_gateway {
  string last_subscription_payment_gateway = 43;
  }
  oneof _last_trial_payment_gateway {
  string last_trial_payment_gateway = 44;
  }
  oneof _user_lifecycle_secondary_state {
  string user_lifecycle_secondary_state = 45;
  }
  oneof _previous_user_lifecycle_state {
  strin
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11586"></a>
## FND-11586: chesscom.user_properties.v1.SubscriptionProperty.last_subscription_payment_gateway = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_subscription_payment_gateway = 43;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 4885.

```text
ethod {
  string last_trial_payment_method = 42;
  }
  oneof _last_subscription_payment_gateway {
  string last_subscription_payment_gateway = 43;
  }
  oneof _last_trial_payment_gateway {
  string last_trial_payment_gateway = 44;
  }
  oneof _user_lifecycle_secondary_state {
  string user_lifecycle_secondary_state = 45;
  }
  oneof _previous_user_lifecycle_state {
  string previous_user_lifecycle_state = 46;
  }
  o
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11587"></a>
## FND-11587: oneof declaration: chesscom.user_properties.v1.SubscriptionProperty._last_trial_payment_gateway

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_trial_payment_gateway {

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 4938.

```text
  oneof _last_subscription_payment_gateway {
  string last_subscription_payment_gateway = 43;
  }
  oneof _last_trial_payment_gateway {
  string last_trial_payment_gateway = 44;
  }
  oneof _user_lifecycle_secondary_state {
  string user_lifecycle_secondary_state = 45;
  }
  oneof _previous_user_lifecycle_state {
  string previous_user_lifecycle_state = 46;
  }
  oneof _previous_user_lifecycle_secondary_state {
  str
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11588"></a>
## FND-11588: chesscom.user_properties.v1.SubscriptionProperty.last_trial_payment_gateway = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_trial_payment_gateway = 44;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 4976.

```text
eway {
  string last_subscription_payment_gateway = 43;
  }
  oneof _last_trial_payment_gateway {
  string last_trial_payment_gateway = 44;
  }
  oneof _user_lifecycle_secondary_state {
  string user_lifecycle_secondary_state = 45;
  }
  oneof _previous_user_lifecycle_state {
  string previous_user_lifecycle_state = 46;
  }
  oneof _previous_user_lifecycle_secondary_state {
  string previous_user_lifecycle_secondary_
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11589"></a>
## FND-11589: oneof declaration: chesscom.user_properties.v1.SubscriptionProperty._user_lifecycle_secondary_state

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_lifecycle_secondary_state {

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 5022.

```text
way = 43;
  }
  oneof _last_trial_payment_gateway {
  string last_trial_payment_gateway = 44;
  }
  oneof _user_lifecycle_secondary_state {
  string user_lifecycle_secondary_state = 45;
  }
  oneof _previous_user_lifecycle_state {
  string previous_user_lifecycle_state = 46;
  }
  oneof _previous_user_lifecycle_secondary_state {
  string previous_user_lifecycle_secondary_state = 47;
  }
  repeated string incentives_r
```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11590"></a>
## FND-11590: chesscom.user_properties.v1.SubscriptionProperty.user_lifecycle_secondary_state = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_lifecycle_secondary_state = 45;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 5064.

```text
gateway {
  string last_trial_payment_gateway = 44;
  }
  oneof _user_lifecycle_secondary_state {
  string user_lifecycle_secondary_state = 45;
  }
  oneof _previous_user_lifecycle_state {
  string previous_user_lifecycle_state = 46;
  }
  oneof _previous_user_lifecycle_secondary_state {
  string previous_user_lifecycle_secondary_state = 47;
  }
  repeated string incentives_redeemed = 32;
}

```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11591"></a>
## FND-11591: oneof declaration: chesscom.user_properties.v1.SubscriptionProperty._previous_user_lifecycle_state

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _previous_user_lifecycle_state {

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 5114.

```text
;
  }
  oneof _user_lifecycle_secondary_state {
  string user_lifecycle_secondary_state = 45;
  }
  oneof _previous_user_lifecycle_state {
  string previous_user_lifecycle_state = 46;
  }
  oneof _previous_user_lifecycle_secondary_state {
  string previous_user_lifecycle_secondary_state = 47;
  }
  repeated string incentives_redeemed = 32;
}

```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11592"></a>
## FND-11592: chesscom.user_properties.v1.SubscriptionProperty.previous_user_lifecycle_state = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string previous_user_lifecycle_state = 46;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 5155.

```text
tate {
  string user_lifecycle_secondary_state = 45;
  }
  oneof _previous_user_lifecycle_state {
  string previous_user_lifecycle_state = 46;
  }
  oneof _previous_user_lifecycle_secondary_state {
  string previous_user_lifecycle_secondary_state = 47;
  }
  repeated string incentives_redeemed = 32;
}

```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11593"></a>
## FND-11593: oneof declaration: chesscom.user_properties.v1.SubscriptionProperty._previous_user_lifecycle_secondary_state

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _previous_user_lifecycle_secondary_state {

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 5204.

```text
45;
  }
  oneof _previous_user_lifecycle_state {
  string previous_user_lifecycle_state = 46;
  }
  oneof _previous_user_lifecycle_secondary_state {
  string previous_user_lifecycle_secondary_state = 47;
  }
  repeated string incentives_redeemed = 32;
}

```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11594"></a>
## FND-11594: chesscom.user_properties.v1.SubscriptionProperty.previous_user_lifecycle_secondary_state = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string previous_user_lifecycle_secondary_state = 47;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 5255.

```text
string previous_user_lifecycle_state = 46;
  }
  oneof _previous_user_lifecycle_secondary_state {
  string previous_user_lifecycle_secondary_state = 47;
  }
  repeated string incentives_redeemed = 32;
}

```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11595"></a>
## FND-11595: chesscom.user_properties.v1.SubscriptionProperty.incentives_redeemed = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string incentives_redeemed = 32;

### Evidence

- **SRC-0633** `research/proto/chesscom/user_properties/v1/properties_subscription.proto` — [preserved redacted evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto)
  Character offset 5314.

```text
vious_user_lifecycle_secondary_state {
  string previous_user_lifecycle_secondary_state = 47;
  }
  repeated string incentives_redeemed = 32;
}

```

**Source references:** SRC-0633, SRC-1604  
**URL references:** None independently associated  
**Related findings:** FND-11459, FND-11460, FND-11461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11596"></a>
## FND-11596: enum declaration: chesscom.user_properties.v1.SurveyPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SurveyPropertyDefinition {

### Evidence

- **SRC-0634** `research/proto/chesscom/user_properties/v1/properties_survey.proto` — [preserved redacted evidence](../evidence/text/6f259f6a10e63d839119b60fcb63c65804ab19bde02341501b26e352c8fed520.proto)
  Character offset 120.

```text
user_properties/v1/properties_survey.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum SurveyPropertyDefinition {
  SURVEY_PROPERTY_UNSPECIFIED = 0;
  SURVEY_QUESTION_ANSWERS = 1;
  SURVEY_QUESTION_DISMISSALS = 2;
}

message SurveyProperty {
  repeated string survey_question_answers = 1;
  repeated string survey_question_dismissals = 2;
}

```

**Source references:** SRC-0634, SRC-1605  
**URL references:** None independently associated  
**Related findings:** FND-11597, FND-11598

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11597"></a>
## FND-11597: chesscom.user_properties.v1.SurveyPropertyDefinition.SURVEY_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SURVEY_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0634** `research/proto/chesscom/user_properties/v1/properties_survey.proto` — [preserved redacted evidence](../evidence/text/6f259f6a10e63d839119b60fcb63c65804ab19bde02341501b26e352c8fed520.proto)
  Character offset 154.

```text
ey.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum SurveyPropertyDefinition {
  SURVEY_PROPERTY_UNSPECIFIED = 0;
  SURVEY_QUESTION_ANSWERS = 1;
  SURVEY_QUESTION_DISMISSALS = 2;
}

message SurveyProperty {
  repeated string survey_question_answers = 1;
  repeated string survey_question_dismissals = 2;
}

```

**Source references:** SRC-0634, SRC-1605  
**URL references:** None independently associated  
**Related findings:** FND-11596, FND-11598

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11598"></a>
## FND-11598: chesscom.user_properties.v1.SurveyPropertyDefinition.SURVEY_QUESTION_ANSWERS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SURVEY_QUESTION_ANSWERS = 1;

### Evidence

- **SRC-0634** `research/proto/chesscom/user_properties/v1/properties_survey.proto` — [preserved redacted evidence](../evidence/text/6f259f6a10e63d839119b60fcb63c65804ab19bde02341501b26e352c8fed520.proto)
  Character offset 189.

```text
 chesscom.user_properties.v1;

enum SurveyPropertyDefinition {
  SURVEY_PROPERTY_UNSPECIFIED = 0;
  SURVEY_QUESTION_ANSWERS = 1;
  SURVEY_QUESTION_DISMISSALS = 2;
}

message SurveyProperty {
  repeated string survey_question_answers = 1;
  repeated string survey_question_dismissals = 2;
}

```

**Source references:** SRC-0634, SRC-1605  
**URL references:** None independently associated  
**Related findings:** FND-11596, FND-11597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11599"></a>
## FND-11599: chesscom.user_properties.v1.SurveyPropertyDefinition.SURVEY_QUESTION_DISMISSALS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SURVEY_QUESTION_DISMISSALS = 2;

### Evidence

- **SRC-0634** `research/proto/chesscom/user_properties/v1/properties_survey.proto` — [preserved redacted evidence](../evidence/text/6f259f6a10e63d839119b60fcb63c65804ab19bde02341501b26e352c8fed520.proto)
  Character offset 220.

```text
enum SurveyPropertyDefinition {
  SURVEY_PROPERTY_UNSPECIFIED = 0;
  SURVEY_QUESTION_ANSWERS = 1;
  SURVEY_QUESTION_DISMISSALS = 2;
}

message SurveyProperty {
  repeated string survey_question_answers = 1;
  repeated string survey_question_dismissals = 2;
}

```

**Source references:** SRC-0634, SRC-1605  
**URL references:** None independently associated  
**Related findings:** FND-11596, FND-11597, FND-11598

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11600"></a>
## FND-11600: message declaration: chesscom.user_properties.v1.SurveyProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SurveyProperty {

### Evidence

- **SRC-0634** `research/proto/chesscom/user_properties/v1/properties_survey.proto` — [preserved redacted evidence](../evidence/text/6f259f6a10e63d839119b60fcb63c65804ab19bde02341501b26e352c8fed520.proto)
  Character offset 255.

```text
URVEY_PROPERTY_UNSPECIFIED = 0;
  SURVEY_QUESTION_ANSWERS = 1;
  SURVEY_QUESTION_DISMISSALS = 2;
}

message SurveyProperty {
  repeated string survey_question_answers = 1;
  repeated string survey_question_dismissals = 2;
}

```

**Source references:** SRC-0634, SRC-1605  
**URL references:** None independently associated  
**Related findings:** FND-11596, FND-11597, FND-11598

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11601"></a>
## FND-11601: chesscom.user_properties.v1.SurveyProperty.survey_question_answers = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string survey_question_answers = 1;

### Evidence

- **SRC-0634** `research/proto/chesscom/user_properties/v1/properties_survey.proto` — [preserved redacted evidence](../evidence/text/6f259f6a10e63d839119b60fcb63c65804ab19bde02341501b26e352c8fed520.proto)
  Character offset 282.

```text
= 0;
  SURVEY_QUESTION_ANSWERS = 1;
  SURVEY_QUESTION_DISMISSALS = 2;
}

message SurveyProperty {
  repeated string survey_question_answers = 1;
  repeated string survey_question_dismissals = 2;
}

```

**Source references:** SRC-0634, SRC-1605  
**URL references:** None independently associated  
**Related findings:** FND-11596, FND-11597, FND-11598

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11602"></a>
## FND-11602: chesscom.user_properties.v1.SurveyProperty.survey_question_dismissals = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string survey_question_dismissals = 2;

### Evidence

- **SRC-0634** `research/proto/chesscom/user_properties/v1/properties_survey.proto` — [preserved redacted evidence](../evidence/text/6f259f6a10e63d839119b60fcb63c65804ab19bde02341501b26e352c8fed520.proto)
  Character offset 329.

```text
ESTION_DISMISSALS = 2;
}

message SurveyProperty {
  repeated string survey_question_answers = 1;
  repeated string survey_question_dismissals = 2;
}

```

**Source references:** SRC-0634, SRC-1605  
**URL references:** None independently associated  
**Related findings:** FND-11596, FND-11597, FND-11598

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11603"></a>
## FND-11603: enum declaration: chesscom.user_properties.v1.ThemesPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ThemesPropertyDefinition {

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 120.

```text
user_properties/v1/properties_themes.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum ThemesPropertyDefinition {
  THEMES_PROPERTY_UNSPECIFIED = 0;
  THEMES_THEME_ID = 1;
  THEMES_CUSTOM_BACKGROUND_ID = 2;
  THEMES_CUSTOM_BOARD_STYLE_ID = 3;
  THEMES_CUSTOM_PIECE_SET_ID = 4;
  THEMES_CUSTOM_SOUND_SET_ID = 5;
  THEMES_BACKGROUND_ID = 6;
  THEMES_BOARD_STYLE_ID = 7;
  THEMES_PIECE_SET_ID = 8;
  THEME
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11604"></a>
## FND-11604: chesscom.user_properties.v1.ThemesPropertyDefinition.THEMES_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

THEMES_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 154.

```text
es.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum ThemesPropertyDefinition {
  THEMES_PROPERTY_UNSPECIFIED = 0;
  THEMES_THEME_ID = 1;
  THEMES_CUSTOM_BACKGROUND_ID = 2;
  THEMES_CUSTOM_BOARD_STYLE_ID = 3;
  THEMES_CUSTOM_PIECE_SET_ID = 4;
  THEMES_CUSTOM_SOUND_SET_ID = 5;
  THEMES_BACKGROUND_ID = 6;
  THEMES_BOARD_STYLE_ID = 7;
  THEMES_PIECE_SET_ID = 8;
  THEMES_SOUND_SET_ID = 9;
}

message The
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11605"></a>
## FND-11605: chesscom.user_properties.v1.ThemesPropertyDefinition.THEMES_THEME_ID = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

THEMES_THEME_ID = 1;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 189.

```text
 chesscom.user_properties.v1;

enum ThemesPropertyDefinition {
  THEMES_PROPERTY_UNSPECIFIED = 0;
  THEMES_THEME_ID = 1;
  THEMES_CUSTOM_BACKGROUND_ID = 2;
  THEMES_CUSTOM_BOARD_STYLE_ID = 3;
  THEMES_CUSTOM_PIECE_SET_ID = 4;
  THEMES_CUSTOM_SOUND_SET_ID = 5;
  THEMES_BACKGROUND_ID = 6;
  THEMES_BOARD_STYLE_ID = 7;
  THEMES_PIECE_SET_ID = 8;
  THEMES_SOUND_SET_ID = 9;
}

message ThemesProperty {
  oneof _theme_id {
 
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11606"></a>
## FND-11606: chesscom.user_properties.v1.ThemesPropertyDefinition.THEMES_CUSTOM_BACKGROUND_ID = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

THEMES_CUSTOM_BACKGROUND_ID = 2;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 212.

```text
es.v1;

enum ThemesPropertyDefinition {
  THEMES_PROPERTY_UNSPECIFIED = 0;
  THEMES_THEME_ID = 1;
  THEMES_CUSTOM_BACKGROUND_ID = 2;
  THEMES_CUSTOM_BOARD_STYLE_ID = 3;
  THEMES_CUSTOM_PIECE_SET_ID = 4;
  THEMES_CUSTOM_SOUND_SET_ID = 5;
  THEMES_BACKGROUND_ID = 6;
  THEMES_BOARD_STYLE_ID = 7;
  THEMES_PIECE_SET_ID = 8;
  THEMES_SOUND_SET_ID = 9;
}

message ThemesProperty {
  oneof _theme_id {
  string theme_id = 1;
 
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11607"></a>
## FND-11607: chesscom.user_properties.v1.ThemesPropertyDefinition.THEMES_CUSTOM_BOARD_STYLE_ID = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

THEMES_CUSTOM_BOARD_STYLE_ID = 3;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 247.

```text
on {
  THEMES_PROPERTY_UNSPECIFIED = 0;
  THEMES_THEME_ID = 1;
  THEMES_CUSTOM_BACKGROUND_ID = 2;
  THEMES_CUSTOM_BOARD_STYLE_ID = 3;
  THEMES_CUSTOM_PIECE_SET_ID = 4;
  THEMES_CUSTOM_SOUND_SET_ID = 5;
  THEMES_BACKGROUND_ID = 6;
  THEMES_BOARD_STYLE_ID = 7;
  THEMES_PIECE_SET_ID = 8;
  THEMES_SOUND_SET_ID = 9;
}

message ThemesProperty {
  oneof _theme_id {
  string theme_id = 1;
  }
  oneof _custom_background_id {

```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11608"></a>
## FND-11608: chesscom.user_properties.v1.ThemesPropertyDefinition.THEMES_CUSTOM_PIECE_SET_ID = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

THEMES_CUSTOM_PIECE_SET_ID = 4;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 283.

```text
 0;
  THEMES_THEME_ID = 1;
  THEMES_CUSTOM_BACKGROUND_ID = 2;
  THEMES_CUSTOM_BOARD_STYLE_ID = 3;
  THEMES_CUSTOM_PIECE_SET_ID = 4;
  THEMES_CUSTOM_SOUND_SET_ID = 5;
  THEMES_BACKGROUND_ID = 6;
  THEMES_BOARD_STYLE_ID = 7;
  THEMES_PIECE_SET_ID = 8;
  THEMES_SOUND_SET_ID = 9;
}

message ThemesProperty {
  oneof _theme_id {
  string theme_id = 1;
  }
  oneof _custom_background_id {
  string custom_background_id = 2;
 
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11609"></a>
## FND-11609: chesscom.user_properties.v1.ThemesPropertyDefinition.THEMES_CUSTOM_SOUND_SET_ID = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

THEMES_CUSTOM_SOUND_SET_ID = 5;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 317.

```text
S_CUSTOM_BACKGROUND_ID = 2;
  THEMES_CUSTOM_BOARD_STYLE_ID = 3;
  THEMES_CUSTOM_PIECE_SET_ID = 4;
  THEMES_CUSTOM_SOUND_SET_ID = 5;
  THEMES_BACKGROUND_ID = 6;
  THEMES_BOARD_STYLE_ID = 7;
  THEMES_PIECE_SET_ID = 8;
  THEMES_SOUND_SET_ID = 9;
}

message ThemesProperty {
  oneof _theme_id {
  string theme_id = 1;
  }
  oneof _custom_background_id {
  string custom_background_id = 2;
  }
  oneof _custom_board_style_id 
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11610"></a>
## FND-11610: chesscom.user_properties.v1.ThemesPropertyDefinition.THEMES_BACKGROUND_ID = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

THEMES_BACKGROUND_ID = 6;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 351.

```text
ES_CUSTOM_BOARD_STYLE_ID = 3;
  THEMES_CUSTOM_PIECE_SET_ID = 4;
  THEMES_CUSTOM_SOUND_SET_ID = 5;
  THEMES_BACKGROUND_ID = 6;
  THEMES_BOARD_STYLE_ID = 7;
  THEMES_PIECE_SET_ID = 8;
  THEMES_SOUND_SET_ID = 9;
}

message ThemesProperty {
  oneof _theme_id {
  string theme_id = 1;
  }
  oneof _custom_background_id {
  string custom_background_id = 2;
  }
  oneof _custom_board_style_id {
  string custom_board_style_id =
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11611"></a>
## FND-11611: chesscom.user_properties.v1.ThemesPropertyDefinition.THEMES_BOARD_STYLE_ID = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

THEMES_BOARD_STYLE_ID = 7;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 379.

```text
;
  THEMES_CUSTOM_PIECE_SET_ID = 4;
  THEMES_CUSTOM_SOUND_SET_ID = 5;
  THEMES_BACKGROUND_ID = 6;
  THEMES_BOARD_STYLE_ID = 7;
  THEMES_PIECE_SET_ID = 8;
  THEMES_SOUND_SET_ID = 9;
}

message ThemesProperty {
  oneof _theme_id {
  string theme_id = 1;
  }
  oneof _custom_background_id {
  string custom_background_id = 2;
  }
  oneof _custom_board_style_id {
  string custom_board_style_id = 3;
  }
  oneof _custom_piec
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11612"></a>
## FND-11612: chesscom.user_properties.v1.ThemesPropertyDefinition.THEMES_PIECE_SET_ID = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

THEMES_PIECE_SET_ID = 8;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 408.

```text
D = 4;
  THEMES_CUSTOM_SOUND_SET_ID = 5;
  THEMES_BACKGROUND_ID = 6;
  THEMES_BOARD_STYLE_ID = 7;
  THEMES_PIECE_SET_ID = 8;
  THEMES_SOUND_SET_ID = 9;
}

message ThemesProperty {
  oneof _theme_id {
  string theme_id = 1;
  }
  oneof _custom_background_id {
  string custom_background_id = 2;
  }
  oneof _custom_board_style_id {
  string custom_board_style_id = 3;
  }
  oneof _custom_piece_set_id {
  string custom_pi
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11613"></a>
## FND-11613: chesscom.user_properties.v1.ThemesPropertyDefinition.THEMES_SOUND_SET_ID = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

THEMES_SOUND_SET_ID = 9;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 435.

```text
D_SET_ID = 5;
  THEMES_BACKGROUND_ID = 6;
  THEMES_BOARD_STYLE_ID = 7;
  THEMES_PIECE_SET_ID = 8;
  THEMES_SOUND_SET_ID = 9;
}

message ThemesProperty {
  oneof _theme_id {
  string theme_id = 1;
  }
  oneof _custom_background_id {
  string custom_background_id = 2;
  }
  oneof _custom_board_style_id {
  string custom_board_style_id = 3;
  }
  oneof _custom_piece_set_id {
  string custom_piece_set_id = 4;
  }
  oneof
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11614"></a>
## FND-11614: message declaration: chesscom.user_properties.v1.ThemesProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ThemesProperty {

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 463.

```text
ROUND_ID = 6;
  THEMES_BOARD_STYLE_ID = 7;
  THEMES_PIECE_SET_ID = 8;
  THEMES_SOUND_SET_ID = 9;
}

message ThemesProperty {
  oneof _theme_id {
  string theme_id = 1;
  }
  oneof _custom_background_id {
  string custom_background_id = 2;
  }
  oneof _custom_board_style_id {
  string custom_board_style_id = 3;
  }
  oneof _custom_piece_set_id {
  string custom_piece_set_id = 4;
  }
  oneof _custom_sound_set_id {
  st
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11615"></a>
## FND-11615: oneof declaration: chesscom.user_properties.v1.ThemesProperty._theme_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _theme_id {

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 490.

```text
D_STYLE_ID = 7;
  THEMES_PIECE_SET_ID = 8;
  THEMES_SOUND_SET_ID = 9;
}

message ThemesProperty {
  oneof _theme_id {
  string theme_id = 1;
  }
  oneof _custom_background_id {
  string custom_background_id = 2;
  }
  oneof _custom_board_style_id {
  string custom_board_style_id = 3;
  }
  oneof _custom_piece_set_id {
  string custom_piece_set_id = 4;
  }
  oneof _custom_sound_set_id {
  string custom_sound_set_id = 
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11616"></a>
## FND-11616: chesscom.user_properties.v1.ThemesProperty.theme_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string theme_id = 1;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 510.

```text
EMES_PIECE_SET_ID = 8;
  THEMES_SOUND_SET_ID = 9;
}

message ThemesProperty {
  oneof _theme_id {
  string theme_id = 1;
  }
  oneof _custom_background_id {
  string custom_background_id = 2;
  }
  oneof _custom_board_style_id {
  string custom_board_style_id = 3;
  }
  oneof _custom_piece_set_id {
  string custom_piece_set_id = 4;
  }
  oneof _custom_sound_set_id {
  string custom_sound_set_id = 5;
  }
  oneof _back
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11617"></a>
## FND-11617: oneof declaration: chesscom.user_properties.v1.ThemesProperty._custom_background_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _custom_background_id {

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 537.

```text
EMES_SOUND_SET_ID = 9;
}

message ThemesProperty {
  oneof _theme_id {
  string theme_id = 1;
  }
  oneof _custom_background_id {
  string custom_background_id = 2;
  }
  oneof _custom_board_style_id {
  string custom_board_style_id = 3;
  }
  oneof _custom_piece_set_id {
  string custom_piece_set_id = 4;
  }
  oneof _custom_sound_set_id {
  string custom_sound_set_id = 5;
  }
  oneof _background_id {
  string backgr
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11618"></a>
## FND-11618: chesscom.user_properties.v1.ThemesProperty.custom_background_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string custom_background_id = 2;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 569.

```text
e ThemesProperty {
  oneof _theme_id {
  string theme_id = 1;
  }
  oneof _custom_background_id {
  string custom_background_id = 2;
  }
  oneof _custom_board_style_id {
  string custom_board_style_id = 3;
  }
  oneof _custom_piece_set_id {
  string custom_piece_set_id = 4;
  }
  oneof _custom_sound_set_id {
  string custom_sound_set_id = 5;
  }
  oneof _background_id {
  string background_id = 6;
  }
  oneof _board_
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11619"></a>
## FND-11619: oneof declaration: chesscom.user_properties.v1.ThemesProperty._custom_board_style_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _custom_board_style_id {

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 608.

```text
  string theme_id = 1;
  }
  oneof _custom_background_id {
  string custom_background_id = 2;
  }
  oneof _custom_board_style_id {
  string custom_board_style_id = 3;
  }
  oneof _custom_piece_set_id {
  string custom_piece_set_id = 4;
  }
  oneof _custom_sound_set_id {
  string custom_sound_set_id = 5;
  }
  oneof _background_id {
  string background_id = 6;
  }
  oneof _board_style_id {
  string board_style_id = 7;
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11620"></a>
## FND-11620: chesscom.user_properties.v1.ThemesProperty.custom_board_style_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string custom_board_style_id = 3;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 641.

```text
f _custom_background_id {
  string custom_background_id = 2;
  }
  oneof _custom_board_style_id {
  string custom_board_style_id = 3;
  }
  oneof _custom_piece_set_id {
  string custom_piece_set_id = 4;
  }
  oneof _custom_sound_set_id {
  string custom_sound_set_id = 5;
  }
  oneof _background_id {
  string background_id = 6;
  }
  oneof _board_style_id {
  string board_style_id = 7;
  }
  oneof _piece_set_id {
  st
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11621"></a>
## FND-11621: oneof declaration: chesscom.user_properties.v1.ThemesProperty._custom_piece_set_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _custom_piece_set_id {

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 681.

```text
m_background_id = 2;
  }
  oneof _custom_board_style_id {
  string custom_board_style_id = 3;
  }
  oneof _custom_piece_set_id {
  string custom_piece_set_id = 4;
  }
  oneof _custom_sound_set_id {
  string custom_sound_set_id = 5;
  }
  oneof _background_id {
  string background_id = 6;
  }
  oneof _board_style_id {
  string board_style_id = 7;
  }
  oneof _piece_set_id {
  string piece_set_id = 8;
  }
  oneof _soun
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11622"></a>
## FND-11622: chesscom.user_properties.v1.ThemesProperty.custom_piece_set_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string custom_piece_set_id = 4;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 712.

```text
f _custom_board_style_id {
  string custom_board_style_id = 3;
  }
  oneof _custom_piece_set_id {
  string custom_piece_set_id = 4;
  }
  oneof _custom_sound_set_id {
  string custom_sound_set_id = 5;
  }
  oneof _background_id {
  string background_id = 6;
  }
  oneof _board_style_id {
  string board_style_id = 7;
  }
  oneof _piece_set_id {
  string piece_set_id = 8;
  }
  oneof _sound_set_id {
  string sound_set_i
```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11623"></a>
## FND-11623: oneof declaration: chesscom.user_properties.v1.ThemesProperty._custom_sound_set_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _custom_sound_set_id {

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 750.

```text
stom_board_style_id = 3;
  }
  oneof _custom_piece_set_id {
  string custom_piece_set_id = 4;
  }
  oneof _custom_sound_set_id {
  string custom_sound_set_id = 5;
  }
  oneof _background_id {
  string background_id = 6;
  }
  oneof _board_style_id {
  string board_style_id = 7;
  }
  oneof _piece_set_id {
  string piece_set_id = 8;
  }
  oneof _sound_set_id {
  string sound_set_id = 9;
  }
}

```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11624"></a>
## FND-11624: chesscom.user_properties.v1.ThemesProperty.custom_sound_set_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string custom_sound_set_id = 5;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 781.

```text
oneof _custom_piece_set_id {
  string custom_piece_set_id = 4;
  }
  oneof _custom_sound_set_id {
  string custom_sound_set_id = 5;
  }
  oneof _background_id {
  string background_id = 6;
  }
  oneof _board_style_id {
  string board_style_id = 7;
  }
  oneof _piece_set_id {
  string piece_set_id = 8;
  }
  oneof _sound_set_id {
  string sound_set_id = 9;
  }
}

```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11625"></a>
## FND-11625: oneof declaration: chesscom.user_properties.v1.ThemesProperty._background_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _background_id {

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 819.

```text
custom_piece_set_id = 4;
  }
  oneof _custom_sound_set_id {
  string custom_sound_set_id = 5;
  }
  oneof _background_id {
  string background_id = 6;
  }
  oneof _board_style_id {
  string board_style_id = 7;
  }
  oneof _piece_set_id {
  string piece_set_id = 8;
  }
  oneof _sound_set_id {
  string sound_set_id = 9;
  }
}

```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11626"></a>
## FND-11626: chesscom.user_properties.v1.ThemesProperty.background_id = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string background_id = 6;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 844.

```text
  }
  oneof _custom_sound_set_id {
  string custom_sound_set_id = 5;
  }
  oneof _background_id {
  string background_id = 6;
  }
  oneof _board_style_id {
  string board_style_id = 7;
  }
  oneof _piece_set_id {
  string piece_set_id = 8;
  }
  oneof _sound_set_id {
  string sound_set_id = 9;
  }
}

```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11627"></a>
## FND-11627: oneof declaration: chesscom.user_properties.v1.ThemesProperty._board_style_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_style_id {

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 876.

```text
 {
  string custom_sound_set_id = 5;
  }
  oneof _background_id {
  string background_id = 6;
  }
  oneof _board_style_id {
  string board_style_id = 7;
  }
  oneof _piece_set_id {
  string piece_set_id = 8;
  }
  oneof _sound_set_id {
  string sound_set_id = 9;
  }
}

```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11628"></a>
## FND-11628: chesscom.user_properties.v1.ThemesProperty.board_style_id = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string board_style_id = 7;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 902.

```text
et_id = 5;
  }
  oneof _background_id {
  string background_id = 6;
  }
  oneof _board_style_id {
  string board_style_id = 7;
  }
  oneof _piece_set_id {
  string piece_set_id = 8;
  }
  oneof _sound_set_id {
  string sound_set_id = 9;
  }
}

```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11629"></a>
## FND-11629: oneof declaration: chesscom.user_properties.v1.ThemesProperty._piece_set_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _piece_set_id {

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 935.

```text
d_id {
  string background_id = 6;
  }
  oneof _board_style_id {
  string board_style_id = 7;
  }
  oneof _piece_set_id {
  string piece_set_id = 8;
  }
  oneof _sound_set_id {
  string sound_set_id = 9;
  }
}

```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11630"></a>
## FND-11630: chesscom.user_properties.v1.ThemesProperty.piece_set_id = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string piece_set_id = 8;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 959.

```text
nd_id = 6;
  }
  oneof _board_style_id {
  string board_style_id = 7;
  }
  oneof _piece_set_id {
  string piece_set_id = 8;
  }
  oneof _sound_set_id {
  string sound_set_id = 9;
  }
}

```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11631"></a>
## FND-11631: oneof declaration: chesscom.user_properties.v1.ThemesProperty._sound_set_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _sound_set_id {

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 990.

```text
tyle_id {
  string board_style_id = 7;
  }
  oneof _piece_set_id {
  string piece_set_id = 8;
  }
  oneof _sound_set_id {
  string sound_set_id = 9;
  }
}

```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11632"></a>
## FND-11632: chesscom.user_properties.v1.ThemesProperty.sound_set_id = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string sound_set_id = 9;

### Evidence

- **SRC-0635** `research/proto/chesscom/user_properties/v1/properties_themes.proto` — [preserved redacted evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto)
  Character offset 1014.

```text
_style_id = 7;
  }
  oneof _piece_set_id {
  string piece_set_id = 8;
  }
  oneof _sound_set_id {
  string sound_set_id = 9;
  }
}

```

**Source references:** SRC-0635, SRC-1606  
**URL references:** None independently associated  
**Related findings:** FND-11603, FND-11604, FND-11605

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11633"></a>
## FND-11633: message declaration: chesscom.user_properties.v1.TimeWindowsPropertiesData

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TimeWindowsPropertiesData {

### Evidence

- **SRC-0636** `research/proto/chesscom/user_properties/v1/properties_time_windows.proto` — [preserved redacted evidence](../evidence/text/be1bbbf01764114244981c0f2a0766d8178588c3c06356c80248f8e54b0295a5.proto)
  Character offset 126.

```text
roperties/v1/properties_time_windows.proto
// syntax: proto3

package chesscom.user_properties.v1;

message TimeWindowsPropertiesData {
  repeated .chesscom.user_properties.v1.TimeWindowsPropertiesData.PropertiesEntry properties = 1;
  message PropertiesEntry {
  optional string key = 1;
  optional .chesscom.user_properties.v1.TimeWindowsPropertyData value = 2;
  }
}

message TimeWindowsPropertyData {
  repeated .che
```

**Source references:** SRC-0636, SRC-1607  
**URL references:** None independently associated  
**Related findings:** FND-11634, FND-11635

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11634"></a>
## FND-11634: chesscom.user_properties.v1.TimeWindowsPropertiesData.properties = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_properties.v1.TimeWindowsPropertiesData.PropertiesEntry properties = 1;

### Evidence

- **SRC-0636** `research/proto/chesscom/user_properties/v1/properties_time_windows.proto` — [preserved redacted evidence](../evidence/text/be1bbbf01764114244981c0f2a0766d8178588c3c06356c80248f8e54b0295a5.proto)
  Character offset 164.

```text
roto
// syntax: proto3

package chesscom.user_properties.v1;

message TimeWindowsPropertiesData {
  repeated .chesscom.user_properties.v1.TimeWindowsPropertiesData.PropertiesEntry properties = 1;
  message PropertiesEntry {
  optional string key = 1;
  optional .chesscom.user_properties.v1.TimeWindowsPropertyData value = 2;
  }
}

message TimeWindowsPropertyData {
  repeated .chesscom.user_properties.v1.TimeWindowsPr
```

**Source references:** SRC-0636, SRC-1607  
**URL references:** None independently associated  
**Related findings:** FND-11633, FND-11635

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11635"></a>
## FND-11635: message declaration: chesscom.user_properties.v1.TimeWindowsPropertiesData.PropertiesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PropertiesEntry {

### Evidence

- **SRC-0636** `research/proto/chesscom/user_properties/v1/properties_time_windows.proto` — [preserved redacted evidence](../evidence/text/be1bbbf01764114244981c0f2a0766d8178588c3c06356c80248f8e54b0295a5.proto)
  Character offset 262.

```text
  repeated .chesscom.user_properties.v1.TimeWindowsPropertiesData.PropertiesEntry properties = 1;
  message PropertiesEntry {
  optional string key = 1;
  optional .chesscom.user_properties.v1.TimeWindowsPropertyData value = 2;
  }
}

message TimeWindowsPropertyData {
  repeated .chesscom.user_properties.v1.TimeWindowsPropertyData.DailyAggregatedEntry daily_aggregated = 1;
  message DailyAggregatedEntry {
  optional 
```

**Source references:** SRC-0636, SRC-1607  
**URL references:** None independently associated  
**Related findings:** FND-11633, FND-11634

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11636"></a>
## FND-11636: chesscom.user_properties.v1.TimeWindowsPropertiesData.PropertiesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0636** `research/proto/chesscom/user_properties/v1/properties_time_windows.proto` — [preserved redacted evidence](../evidence/text/be1bbbf01764114244981c0f2a0766d8178588c3c06356c80248f8e54b0295a5.proto)
  Character offset 290.

```text
operties.v1.TimeWindowsPropertiesData.PropertiesEntry properties = 1;
  message PropertiesEntry {
  optional string key = 1;
  optional .chesscom.user_properties.v1.TimeWindowsPropertyData value = 2;
  }
}

message TimeWindowsPropertyData {
  repeated .chesscom.user_properties.v1.TimeWindowsPropertyData.DailyAggregatedEntry daily_aggregated = 1;
  message DailyAggregatedEntry {
  optional int32 key = 1;
  optional do
```

**Source references:** SRC-0636, SRC-1607  
**URL references:** None independently associated  
**Related findings:** FND-11633, FND-11634, FND-11635

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11637"></a>
## FND-11637: chesscom.user_properties.v1.TimeWindowsPropertiesData.PropertiesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_properties.v1.TimeWindowsPropertyData value = 2;

### Evidence

- **SRC-0636** `research/proto/chesscom/user_properties/v1/properties_time_windows.proto` — [preserved redacted evidence](../evidence/text/be1bbbf01764114244981c0f2a0766d8178588c3c06356c80248f8e54b0295a5.proto)
  Character offset 317.

```text
ertiesData.PropertiesEntry properties = 1;
  message PropertiesEntry {
  optional string key = 1;
  optional .chesscom.user_properties.v1.TimeWindowsPropertyData value = 2;
  }
}

message TimeWindowsPropertyData {
  repeated .chesscom.user_properties.v1.TimeWindowsPropertyData.DailyAggregatedEntry daily_aggregated = 1;
  message DailyAggregatedEntry {
  optional int32 key = 1;
  optional double value = 2;
  }
}

```

**Source references:** SRC-0636, SRC-1607  
**URL references:** None independently associated  
**Related findings:** FND-11633, FND-11634, FND-11635

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11638"></a>
## FND-11638: message declaration: chesscom.user_properties.v1.TimeWindowsPropertyData

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TimeWindowsPropertyData {

### Evidence

- **SRC-0636** `research/proto/chesscom/user_properties/v1/properties_time_windows.proto` — [preserved redacted evidence](../evidence/text/be1bbbf01764114244981c0f2a0766d8178588c3c06356c80248f8e54b0295a5.proto)
  Character offset 397.

```text
l string key = 1;
  optional .chesscom.user_properties.v1.TimeWindowsPropertyData value = 2;
  }
}

message TimeWindowsPropertyData {
  repeated .chesscom.user_properties.v1.TimeWindowsPropertyData.DailyAggregatedEntry daily_aggregated = 1;
  message DailyAggregatedEntry {
  optional int32 key = 1;
  optional double value = 2;
  }
}

```

**Source references:** SRC-0636, SRC-1607  
**URL references:** None independently associated  
**Related findings:** FND-11633, FND-11634, FND-11635

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11639"></a>
## FND-11639: chesscom.user_properties.v1.TimeWindowsPropertyData.daily_aggregated = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_properties.v1.TimeWindowsPropertyData.DailyAggregatedEntry daily_aggregated = 1;

### Evidence

- **SRC-0636** `research/proto/chesscom/user_properties/v1/properties_time_windows.proto` — [preserved redacted evidence](../evidence/text/be1bbbf01764114244981c0f2a0766d8178588c3c06356c80248f8e54b0295a5.proto)
  Character offset 433.

```text
om.user_properties.v1.TimeWindowsPropertyData value = 2;
  }
}

message TimeWindowsPropertyData {
  repeated .chesscom.user_properties.v1.TimeWindowsPropertyData.DailyAggregatedEntry daily_aggregated = 1;
  message DailyAggregatedEntry {
  optional int32 key = 1;
  optional double value = 2;
  }
}

```

**Source references:** SRC-0636, SRC-1607  
**URL references:** None independently associated  
**Related findings:** FND-11633, FND-11634, FND-11635

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11640"></a>
## FND-11640: message declaration: chesscom.user_properties.v1.TimeWindowsPropertyData.DailyAggregatedEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DailyAggregatedEntry {

### Evidence

- **SRC-0636** `research/proto/chesscom/user_properties/v1/properties_time_windows.proto` — [preserved redacted evidence](../evidence/text/be1bbbf01764114244981c0f2a0766d8178588c3c06356c80248f8e54b0295a5.proto)
  Character offset 540.

```text
d .chesscom.user_properties.v1.TimeWindowsPropertyData.DailyAggregatedEntry daily_aggregated = 1;
  message DailyAggregatedEntry {
  optional int32 key = 1;
  optional double value = 2;
  }
}

```

**Source references:** SRC-0636, SRC-1607  
**URL references:** None independently associated  
**Related findings:** FND-11633, FND-11634, FND-11635

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11641"></a>
## FND-11641: chesscom.user_properties.v1.TimeWindowsPropertyData.DailyAggregatedEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 key = 1;

### Evidence

- **SRC-0636** `research/proto/chesscom/user_properties/v1/properties_time_windows.proto` — [preserved redacted evidence](../evidence/text/be1bbbf01764114244981c0f2a0766d8178588c3c06356c80248f8e54b0295a5.proto)
  Character offset 573.

```text
meWindowsPropertyData.DailyAggregatedEntry daily_aggregated = 1;
  message DailyAggregatedEntry {
  optional int32 key = 1;
  optional double value = 2;
  }
}

```

**Source references:** SRC-0636, SRC-1607  
**URL references:** None independently associated  
**Related findings:** FND-11633, FND-11634, FND-11635

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11642"></a>
## FND-11642: chesscom.user_properties.v1.TimeWindowsPropertyData.DailyAggregatedEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double value = 2;

### Evidence

- **SRC-0636** `research/proto/chesscom/user_properties/v1/properties_time_windows.proto` — [preserved redacted evidence](../evidence/text/be1bbbf01764114244981c0f2a0766d8178588c3c06356c80248f8e54b0295a5.proto)
  Character offset 599.

```text
yAggregatedEntry daily_aggregated = 1;
  message DailyAggregatedEntry {
  optional int32 key = 1;
  optional double value = 2;
  }
}

```

**Source references:** SRC-0636, SRC-1607  
**URL references:** None independently associated  
**Related findings:** FND-11633, FND-11634, FND-11635

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11643"></a>
## FND-11643: enum declaration: chesscom.user_properties.v1.TournamentStatsPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TournamentStatsPropertyDefinition {

### Evidence

- **SRC-0637** `research/proto/chesscom/user_properties/v1/properties_tournament_stats.proto` — [preserved redacted evidence](../evidence/text/93e27332899cf92a6c6439629aafeb21d448fdbc1543b40aef294a4c7576a83b.proto)
  Character offset 130.

```text
rties/v1/properties_tournament_stats.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum TournamentStatsPropertyDefinition {
  TOURNAMENT_STATS_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_WIN_COUNT = 1;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_DRAW_COUNT = 2;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_LOSS_COUNT = 3;
}

message TournamentStatsProperty {
  oneof
```

**Source references:** SRC-0637, SRC-1608  
**URL references:** None independently associated  
**Related findings:** FND-11644, FND-11645

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11644"></a>
## FND-11644: chesscom.user_properties.v1.TournamentStatsPropertyDefinition.TOURNAMENT_STATS_PROPERTY_DEFINITION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOURNAMENT_STATS_PROPERTY_DEFINITION_UNSPECIFIED = 0;

### Evidence

- **SRC-0637** `research/proto/chesscom/user_properties/v1/properties_tournament_stats.proto` — [preserved redacted evidence](../evidence/text/93e27332899cf92a6c6439629aafeb21d448fdbc1543b40aef294a4c7576a83b.proto)
  Character offset 173.

```text
// syntax: proto3

package chesscom.user_properties.v1;

enum TournamentStatsPropertyDefinition {
  TOURNAMENT_STATS_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_WIN_COUNT = 1;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_DRAW_COUNT = 2;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_LOSS_COUNT = 3;
}

message TournamentStatsProperty {
  oneof _game_win_count {
  int32 game_win_count =
```

**Source references:** SRC-0637, SRC-1608  
**URL references:** None independently associated  
**Related findings:** FND-11643, FND-11645

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11645"></a>
## FND-11645: chesscom.user_properties.v1.TournamentStatsPropertyDefinition.TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_WIN_COUNT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_WIN_COUNT = 1;

### Evidence

- **SRC-0637** `research/proto/chesscom/user_properties/v1/properties_tournament_stats.proto` — [preserved redacted evidence](../evidence/text/93e27332899cf92a6c6439629aafeb21d448fdbc1543b40aef294a4c7576a83b.proto)
  Character offset 229.

```text

enum TournamentStatsPropertyDefinition {
  TOURNAMENT_STATS_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_WIN_COUNT = 1;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_DRAW_COUNT = 2;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_LOSS_COUNT = 3;
}

message TournamentStatsProperty {
  oneof _game_win_count {
  int32 game_win_count = 1;
  }
  oneof _game_draw_count {
  int32 game_draw_cou
```

**Source references:** SRC-0637, SRC-1608  
**URL references:** None independently associated  
**Related findings:** FND-11643, FND-11644

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11646"></a>
## FND-11646: chesscom.user_properties.v1.TournamentStatsPropertyDefinition.TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_DRAW_COUNT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_DRAW_COUNT = 2;

### Evidence

- **SRC-0637** `research/proto/chesscom/user_properties/v1/properties_tournament_stats.proto` — [preserved redacted evidence](../evidence/text/93e27332899cf92a6c6439629aafeb21d448fdbc1543b40aef294a4c7576a83b.proto)
  Character offset 288.

```text
S_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_WIN_COUNT = 1;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_DRAW_COUNT = 2;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_LOSS_COUNT = 3;
}

message TournamentStatsProperty {
  oneof _game_win_count {
  int32 game_win_count = 1;
  }
  oneof _game_draw_count {
  int32 game_draw_count = 2;
  }
  oneof _game_loss_count {
  int32 game_loss_co
```

**Source references:** SRC-0637, SRC-1608  
**URL references:** None independently associated  
**Related findings:** FND-11643, FND-11644, FND-11645

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11647"></a>
## FND-11647: chesscom.user_properties.v1.TournamentStatsPropertyDefinition.TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_LOSS_COUNT = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_LOSS_COUNT = 3;

### Evidence

- **SRC-0637** `research/proto/chesscom/user_properties/v1/properties_tournament_stats.proto` — [preserved redacted evidence](../evidence/text/93e27332899cf92a6c6439629aafeb21d448fdbc1543b40aef294a4c7576a83b.proto)
  Character offset 348.

```text
OPERTY_DEFINITION_GAME_WIN_COUNT = 1;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_DRAW_COUNT = 2;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_LOSS_COUNT = 3;
}

message TournamentStatsProperty {
  oneof _game_win_count {
  int32 game_win_count = 1;
  }
  oneof _game_draw_count {
  int32 game_draw_count = 2;
  }
  oneof _game_loss_count {
  int32 game_loss_count = 3;
  }
}

```

**Source references:** SRC-0637, SRC-1608  
**URL references:** None independently associated  
**Related findings:** FND-11643, FND-11644, FND-11645

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11648"></a>
## FND-11648: message declaration: chesscom.user_properties.v1.TournamentStatsProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TournamentStatsProperty {

### Evidence

- **SRC-0637** `research/proto/chesscom/user_properties/v1/properties_tournament_stats.proto` — [preserved redacted evidence](../evidence/text/93e27332899cf92a6c6439629aafeb21d448fdbc1543b40aef294a4c7576a83b.proto)
  Character offset 409.

```text
ERTY_DEFINITION_GAME_DRAW_COUNT = 2;
  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_LOSS_COUNT = 3;
}

message TournamentStatsProperty {
  oneof _game_win_count {
  int32 game_win_count = 1;
  }
  oneof _game_draw_count {
  int32 game_draw_count = 2;
  }
  oneof _game_loss_count {
  int32 game_loss_count = 3;
  }
}

```

**Source references:** SRC-0637, SRC-1608  
**URL references:** None independently associated  
**Related findings:** FND-11643, FND-11644, FND-11645

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11649"></a>
## FND-11649: oneof declaration: chesscom.user_properties.v1.TournamentStatsProperty._game_win_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_win_count {

### Evidence

- **SRC-0637** `research/proto/chesscom/user_properties/v1/properties_tournament_stats.proto` — [preserved redacted evidence](../evidence/text/93e27332899cf92a6c6439629aafeb21d448fdbc1543b40aef294a4c7576a83b.proto)
  Character offset 445.

```text

  TOURNAMENT_STATS_PROPERTY_DEFINITION_GAME_LOSS_COUNT = 3;
}

message TournamentStatsProperty {
  oneof _game_win_count {
  int32 game_win_count = 1;
  }
  oneof _game_draw_count {
  int32 game_draw_count = 2;
  }
  oneof _game_loss_count {
  int32 game_loss_count = 3;
  }
}

```

**Source references:** SRC-0637, SRC-1608  
**URL references:** None independently associated  
**Related findings:** FND-11643, FND-11644, FND-11645

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11650"></a>
## FND-11650: chesscom.user_properties.v1.TournamentStatsProperty.game_win_count = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 game_win_count = 1;

### Evidence

- **SRC-0637** `research/proto/chesscom/user_properties/v1/properties_tournament_stats.proto` — [preserved redacted evidence](../evidence/text/93e27332899cf92a6c6439629aafeb21d448fdbc1543b40aef294a4c7576a83b.proto)
  Character offset 471.

```text
TY_DEFINITION_GAME_LOSS_COUNT = 3;
}

message TournamentStatsProperty {
  oneof _game_win_count {
  int32 game_win_count = 1;
  }
  oneof _game_draw_count {
  int32 game_draw_count = 2;
  }
  oneof _game_loss_count {
  int32 game_loss_count = 3;
  }
}

```

**Source references:** SRC-0637, SRC-1608  
**URL references:** None independently associated  
**Related findings:** FND-11643, FND-11644, FND-11645

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11651"></a>
## FND-11651: oneof declaration: chesscom.user_properties.v1.TournamentStatsProperty._game_draw_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_draw_count {

### Evidence

- **SRC-0637** `research/proto/chesscom/user_properties/v1/properties_tournament_stats.proto` — [preserved redacted evidence](../evidence/text/93e27332899cf92a6c6439629aafeb21d448fdbc1543b40aef294a4c7576a83b.proto)
  Character offset 503.

```text
3;
}

message TournamentStatsProperty {
  oneof _game_win_count {
  int32 game_win_count = 1;
  }
  oneof _game_draw_count {
  int32 game_draw_count = 2;
  }
  oneof _game_loss_count {
  int32 game_loss_count = 3;
  }
}

```

**Source references:** SRC-0637, SRC-1608  
**URL references:** None independently associated  
**Related findings:** FND-11643, FND-11644, FND-11645

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11652"></a>
## FND-11652: chesscom.user_properties.v1.TournamentStatsProperty.game_draw_count = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 game_draw_count = 2;

### Evidence

- **SRC-0637** `research/proto/chesscom/user_properties/v1/properties_tournament_stats.proto` — [preserved redacted evidence](../evidence/text/93e27332899cf92a6c6439629aafeb21d448fdbc1543b40aef294a4c7576a83b.proto)
  Character offset 530.

```text
tsProperty {
  oneof _game_win_count {
  int32 game_win_count = 1;
  }
  oneof _game_draw_count {
  int32 game_draw_count = 2;
  }
  oneof _game_loss_count {
  int32 game_loss_count = 3;
  }
}

```

**Source references:** SRC-0637, SRC-1608  
**URL references:** None independently associated  
**Related findings:** FND-11643, FND-11644, FND-11645

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11653"></a>
## FND-11653: oneof declaration: chesscom.user_properties.v1.TournamentStatsProperty._game_loss_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_loss_count {

### Evidence

- **SRC-0637** `research/proto/chesscom/user_properties/v1/properties_tournament_stats.proto` — [preserved redacted evidence](../evidence/text/93e27332899cf92a6c6439629aafeb21d448fdbc1543b40aef294a4c7576a83b.proto)
  Character offset 563.

```text
unt {
  int32 game_win_count = 1;
  }
  oneof _game_draw_count {
  int32 game_draw_count = 2;
  }
  oneof _game_loss_count {
  int32 game_loss_count = 3;
  }
}

```

**Source references:** SRC-0637, SRC-1608  
**URL references:** None independently associated  
**Related findings:** FND-11643, FND-11644, FND-11645

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11654"></a>
## FND-11654: chesscom.user_properties.v1.TournamentStatsProperty.game_loss_count = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 game_loss_count = 3;

### Evidence

- **SRC-0637** `research/proto/chesscom/user_properties/v1/properties_tournament_stats.proto` — [preserved redacted evidence](../evidence/text/93e27332899cf92a6c6439629aafeb21d448fdbc1543b40aef294a4c7576a83b.proto)
  Character offset 590.

```text
t = 1;
  }
  oneof _game_draw_count {
  int32 game_draw_count = 2;
  }
  oneof _game_loss_count {
  int32 game_loss_count = 3;
  }
}

```

**Source references:** SRC-0637, SRC-1608  
**URL references:** None independently associated  
**Related findings:** FND-11643, FND-11644, FND-11645

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11655"></a>
## FND-11655: enum declaration: chesscom.user_properties.v1.UserAbusePropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum UserAbusePropertyDefinition {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 130.

```text
rties/v1/properties_trust_and_safety.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum UserAbusePropertyDefinition {
  USER_ABUSE_UNSPECIFIED = 0;
  ABUSE_SCORE_AUTOMOD = 1;
  ABUSE_SCORE_LIGHT = 2;
  ABUSE_SCORE_HEAVY = 3;
  ABUSE_SCORE_TOTAL = 4;
  USERNAME_ABUSE_CATEGORY_SCORE_GOOD = 5;
  USERNAME_ABUSE_CATEGORY_SCORE_IDENTITY_HATE = 6;
  USERNAME_ABUSE_CATEGORY_SCORE_PROFANITY = 7;
  USERNAME_AB
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11656"></a>
## FND-11656: chesscom.user_properties.v1.UserAbusePropertyDefinition.USER_ABUSE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_ABUSE_UNSPECIFIED = 0;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 167.

```text
proto
// syntax: proto3

package chesscom.user_properties.v1;

enum UserAbusePropertyDefinition {
  USER_ABUSE_UNSPECIFIED = 0;
  ABUSE_SCORE_AUTOMOD = 1;
  ABUSE_SCORE_LIGHT = 2;
  ABUSE_SCORE_HEAVY = 3;
  ABUSE_SCORE_TOTAL = 4;
  USERNAME_ABUSE_CATEGORY_SCORE_GOOD = 5;
  USERNAME_ABUSE_CATEGORY_SCORE_IDENTITY_HATE = 6;
  USERNAME_ABUSE_CATEGORY_SCORE_PROFANITY = 7;
  USERNAME_ABUSE_CATEGORY_SCORE_SEXUAL = 8;
  USER
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11657"></a>
## FND-11657: chesscom.user_properties.v1.UserAbusePropertyDefinition.ABUSE_SCORE_AUTOMOD = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ABUSE_SCORE_AUTOMOD = 1;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 197.

```text
ge chesscom.user_properties.v1;

enum UserAbusePropertyDefinition {
  USER_ABUSE_UNSPECIFIED = 0;
  ABUSE_SCORE_AUTOMOD = 1;
  ABUSE_SCORE_LIGHT = 2;
  ABUSE_SCORE_HEAVY = 3;
  ABUSE_SCORE_TOTAL = 4;
  USERNAME_ABUSE_CATEGORY_SCORE_GOOD = 5;
  USERNAME_ABUSE_CATEGORY_SCORE_IDENTITY_HATE = 6;
  USERNAME_ABUSE_CATEGORY_SCORE_PROFANITY = 7;
  USERNAME_ABUSE_CATEGORY_SCORE_SEXUAL = 8;
  USERNAME_ABUSE_CATEGORY_SCORE_VIOL
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11658"></a>
## FND-11658: chesscom.user_properties.v1.UserAbusePropertyDefinition.ABUSE_SCORE_LIGHT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ABUSE_SCORE_LIGHT = 2;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 224.

```text
.v1;

enum UserAbusePropertyDefinition {
  USER_ABUSE_UNSPECIFIED = 0;
  ABUSE_SCORE_AUTOMOD = 1;
  ABUSE_SCORE_LIGHT = 2;
  ABUSE_SCORE_HEAVY = 3;
  ABUSE_SCORE_TOTAL = 4;
  USERNAME_ABUSE_CATEGORY_SCORE_GOOD = 5;
  USERNAME_ABUSE_CATEGORY_SCORE_IDENTITY_HATE = 6;
  USERNAME_ABUSE_CATEGORY_SCORE_PROFANITY = 7;
  USERNAME_ABUSE_CATEGORY_SCORE_SEXUAL = 8;
  USERNAME_ABUSE_CATEGORY_SCORE_VIOLENT = 9;
  USERNAME_ABUSE_C
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11659"></a>
## FND-11659: chesscom.user_properties.v1.UserAbusePropertyDefinition.ABUSE_SCORE_HEAVY = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ABUSE_SCORE_HEAVY = 3;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 249.

```text
rtyDefinition {
  USER_ABUSE_UNSPECIFIED = 0;
  ABUSE_SCORE_AUTOMOD = 1;
  ABUSE_SCORE_LIGHT = 2;
  ABUSE_SCORE_HEAVY = 3;
  ABUSE_SCORE_TOTAL = 4;
  USERNAME_ABUSE_CATEGORY_SCORE_GOOD = 5;
  USERNAME_ABUSE_CATEGORY_SCORE_IDENTITY_HATE = 6;
  USERNAME_ABUSE_CATEGORY_SCORE_PROFANITY = 7;
  USERNAME_ABUSE_CATEGORY_SCORE_SEXUAL = 8;
  USERNAME_ABUSE_CATEGORY_SCORE_VIOLENT = 9;
  USERNAME_ABUSE_CATEGORY_SCORE_PEDOPHILIC 
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11660"></a>
## FND-11660: chesscom.user_properties.v1.UserAbusePropertyDefinition.ABUSE_SCORE_TOTAL = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ABUSE_SCORE_TOTAL = 4;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 274.

```text
USE_UNSPECIFIED = 0;
  ABUSE_SCORE_AUTOMOD = 1;
  ABUSE_SCORE_LIGHT = 2;
  ABUSE_SCORE_HEAVY = 3;
  ABUSE_SCORE_TOTAL = 4;
  USERNAME_ABUSE_CATEGORY_SCORE_GOOD = 5;
  USERNAME_ABUSE_CATEGORY_SCORE_IDENTITY_HATE = 6;
  USERNAME_ABUSE_CATEGORY_SCORE_PROFANITY = 7;
  USERNAME_ABUSE_CATEGORY_SCORE_SEXUAL = 8;
  USERNAME_ABUSE_CATEGORY_SCORE_VIOLENT = 9;
  USERNAME_ABUSE_CATEGORY_SCORE_PEDOPHILIC = 10;
  LAST_USERNAME_ABU
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11661"></a>
## FND-11661: chesscom.user_properties.v1.UserAbusePropertyDefinition.USERNAME_ABUSE_CATEGORY_SCORE_GOOD = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USERNAME_ABUSE_CATEGORY_SCORE_GOOD = 5;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 299.

```text
USE_SCORE_AUTOMOD = 1;
  ABUSE_SCORE_LIGHT = 2;
  ABUSE_SCORE_HEAVY = 3;
  ABUSE_SCORE_TOTAL = 4;
  USERNAME_ABUSE_CATEGORY_SCORE_GOOD = 5;
  USERNAME_ABUSE_CATEGORY_SCORE_IDENTITY_HATE = 6;
  USERNAME_ABUSE_CATEGORY_SCORE_PROFANITY = 7;
  USERNAME_ABUSE_CATEGORY_SCORE_SEXUAL = 8;
  USERNAME_ABUSE_CATEGORY_SCORE_VIOLENT = 9;
  USERNAME_ABUSE_CATEGORY_SCORE_PEDOPHILIC = 10;
  LAST_USERNAME_ABUSE_PREDICTION_DATE = 11;

```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11662"></a>
## FND-11662: chesscom.user_properties.v1.UserAbusePropertyDefinition.USERNAME_ABUSE_CATEGORY_SCORE_IDENTITY_HATE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USERNAME_ABUSE_CATEGORY_SCORE_IDENTITY_HATE = 6;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 341.

```text
 = 2;
  ABUSE_SCORE_HEAVY = 3;
  ABUSE_SCORE_TOTAL = 4;
  USERNAME_ABUSE_CATEGORY_SCORE_GOOD = 5;
  USERNAME_ABUSE_CATEGORY_SCORE_IDENTITY_HATE = 6;
  USERNAME_ABUSE_CATEGORY_SCORE_PROFANITY = 7;
  USERNAME_ABUSE_CATEGORY_SCORE_SEXUAL = 8;
  USERNAME_ABUSE_CATEGORY_SCORE_VIOLENT = 9;
  USERNAME_ABUSE_CATEGORY_SCORE_PEDOPHILIC = 10;
  LAST_USERNAME_ABUSE_PREDICTION_DATE = 11;
  USERNAME_ABUSE_CONFIDENCE_SCORE = 12;
  
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11663"></a>
## FND-11663: chesscom.user_properties.v1.UserAbusePropertyDefinition.USERNAME_ABUSE_CATEGORY_SCORE_PROFANITY = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USERNAME_ABUSE_CATEGORY_SCORE_PROFANITY = 7;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 392.

```text
= 4;
  USERNAME_ABUSE_CATEGORY_SCORE_GOOD = 5;
  USERNAME_ABUSE_CATEGORY_SCORE_IDENTITY_HATE = 6;
  USERNAME_ABUSE_CATEGORY_SCORE_PROFANITY = 7;
  USERNAME_ABUSE_CATEGORY_SCORE_SEXUAL = 8;
  USERNAME_ABUSE_CATEGORY_SCORE_VIOLENT = 9;
  USERNAME_ABUSE_CATEGORY_SCORE_PEDOPHILIC = 10;
  LAST_USERNAME_ABUSE_PREDICTION_DATE = 11;
  USERNAME_ABUSE_CONFIDENCE_SCORE = 12;
  ABUSIVE_CHAT_MESSAGES = 13;
  ABOUT_LAST_UPDATED_AT
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11664"></a>
## FND-11664: chesscom.user_properties.v1.UserAbusePropertyDefinition.USERNAME_ABUSE_CATEGORY_SCORE_SEXUAL = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USERNAME_ABUSE_CATEGORY_SCORE_SEXUAL = 8;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 439.

```text
  USERNAME_ABUSE_CATEGORY_SCORE_IDENTITY_HATE = 6;
  USERNAME_ABUSE_CATEGORY_SCORE_PROFANITY = 7;
  USERNAME_ABUSE_CATEGORY_SCORE_SEXUAL = 8;
  USERNAME_ABUSE_CATEGORY_SCORE_VIOLENT = 9;
  USERNAME_ABUSE_CATEGORY_SCORE_PEDOPHILIC = 10;
  LAST_USERNAME_ABUSE_PREDICTION_DATE = 11;
  USERNAME_ABUSE_CONFIDENCE_SCORE = 12;
  ABUSIVE_CHAT_MESSAGES = 13;
  ABOUT_LAST_UPDATED_AT = 14;
}

message UserAbuseProperty {
  oneof _
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11665"></a>
## FND-11665: chesscom.user_properties.v1.UserAbusePropertyDefinition.USERNAME_ABUSE_CATEGORY_SCORE_VIOLENT = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USERNAME_ABUSE_CATEGORY_SCORE_VIOLENT = 9;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 483.

```text
E = 6;
  USERNAME_ABUSE_CATEGORY_SCORE_PROFANITY = 7;
  USERNAME_ABUSE_CATEGORY_SCORE_SEXUAL = 8;
  USERNAME_ABUSE_CATEGORY_SCORE_VIOLENT = 9;
  USERNAME_ABUSE_CATEGORY_SCORE_PEDOPHILIC = 10;
  LAST_USERNAME_ABUSE_PREDICTION_DATE = 11;
  USERNAME_ABUSE_CONFIDENCE_SCORE = 12;
  ABUSIVE_CHAT_MESSAGES = 13;
  ABOUT_LAST_UPDATED_AT = 14;
}

message UserAbuseProperty {
  oneof _abuse_score_automod {
  int32 abuse_score_au
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11666"></a>
## FND-11666: chesscom.user_properties.v1.UserAbusePropertyDefinition.USERNAME_ABUSE_CATEGORY_SCORE_PEDOPHILIC = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USERNAME_ABUSE_CATEGORY_SCORE_PEDOPHILIC = 10;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 528.

```text
ITY = 7;
  USERNAME_ABUSE_CATEGORY_SCORE_SEXUAL = 8;
  USERNAME_ABUSE_CATEGORY_SCORE_VIOLENT = 9;
  USERNAME_ABUSE_CATEGORY_SCORE_PEDOPHILIC = 10;
  LAST_USERNAME_ABUSE_PREDICTION_DATE = 11;
  USERNAME_ABUSE_CONFIDENCE_SCORE = 12;
  ABUSIVE_CHAT_MESSAGES = 13;
  ABOUT_LAST_UPDATED_AT = 14;
}

message UserAbuseProperty {
  oneof _abuse_score_automod {
  int32 abuse_score_automod = 1;
  }
  oneof _abuse_score_light {
 
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11667"></a>
## FND-11667: chesscom.user_properties.v1.UserAbusePropertyDefinition.LAST_USERNAME_ABUSE_PREDICTION_DATE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_USERNAME_ABUSE_PREDICTION_DATE = 11;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 577.

```text
 8;
  USERNAME_ABUSE_CATEGORY_SCORE_VIOLENT = 9;
  USERNAME_ABUSE_CATEGORY_SCORE_PEDOPHILIC = 10;
  LAST_USERNAME_ABUSE_PREDICTION_DATE = 11;
  USERNAME_ABUSE_CONFIDENCE_SCORE = 12;
  ABUSIVE_CHAT_MESSAGES = 13;
  ABOUT_LAST_UPDATED_AT = 14;
}

message UserAbuseProperty {
  oneof _abuse_score_automod {
  int32 abuse_score_automod = 1;
  }
  oneof _abuse_score_light {
  int32 abuse_score_light = 2;
  }
  oneof _abuse_
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11668"></a>
## FND-11668: chesscom.user_properties.v1.UserAbusePropertyDefinition.USERNAME_ABUSE_CONFIDENCE_SCORE = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USERNAME_ABUSE_CONFIDENCE_SCORE = 12;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 621.

```text
= 9;
  USERNAME_ABUSE_CATEGORY_SCORE_PEDOPHILIC = 10;
  LAST_USERNAME_ABUSE_PREDICTION_DATE = 11;
  USERNAME_ABUSE_CONFIDENCE_SCORE = 12;
  ABUSIVE_CHAT_MESSAGES = 13;
  ABOUT_LAST_UPDATED_AT = 14;
}

message UserAbuseProperty {
  oneof _abuse_score_automod {
  int32 abuse_score_automod = 1;
  }
  oneof _abuse_score_light {
  int32 abuse_score_light = 2;
  }
  oneof _abuse_score_heavy {
  int32 abuse_score_heavy = 3;
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11669"></a>
## FND-11669: chesscom.user_properties.v1.UserAbusePropertyDefinition.ABUSIVE_CHAT_MESSAGES = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ABUSIVE_CHAT_MESSAGES = 13;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 661.

```text
OPHILIC = 10;
  LAST_USERNAME_ABUSE_PREDICTION_DATE = 11;
  USERNAME_ABUSE_CONFIDENCE_SCORE = 12;
  ABUSIVE_CHAT_MESSAGES = 13;
  ABOUT_LAST_UPDATED_AT = 14;
}

message UserAbuseProperty {
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
  int3
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11670"></a>
## FND-11670: chesscom.user_properties.v1.UserAbusePropertyDefinition.ABOUT_LAST_UPDATED_AT = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ABOUT_LAST_UPDATED_AT = 14;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 691.

```text
ABUSE_PREDICTION_DATE = 11;
  USERNAME_ABUSE_CONFIDENCE_SCORE = 12;
  ABUSIVE_CHAT_MESSAGES = 13;
  ABOUT_LAST_UPDATED_AT = 14;
}

message UserAbuseProperty {
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
 
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11671"></a>
## FND-11671: message declaration: chesscom.user_properties.v1.UserAbuseProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserAbuseProperty {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 722.

```text
SERNAME_ABUSE_CONFIDENCE_SCORE = 12;
  ABUSIVE_CHAT_MESSAGES = 13;
  ABOUT_LAST_UPDATED_AT = 14;
}

message UserAbuseProperty {
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
  oneof _username_abuse_category
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11672"></a>
## FND-11672: oneof declaration: chesscom.user_properties.v1.UserAbuseProperty._abuse_score_automod

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _abuse_score_automod {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 752.

```text
 = 12;
  ABUSIVE_CHAT_MESSAGES = 13;
  ABOUT_LAST_UPDATED_AT = 14;
}

message UserAbuseProperty {
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
  float username
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11673"></a>
## FND-11673: chesscom.user_properties.v1.UserAbuseProperty.abuse_score_automod = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 abuse_score_automod = 1;

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 783.

```text
= 13;
  ABOUT_LAST_UPDATED_AT = 14;
}

message UserAbuseProperty {
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
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11674"></a>
## FND-11674: oneof declaration: chesscom.user_properties.v1.UserAbuseProperty._abuse_score_light

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _abuse_score_light {

### Evidence

- **SRC-0638** `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto` — [preserved redacted evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto)
  Character offset 820.

```text


message UserAbuseProperty {
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
  oneof _username_abuse_category
```

**Source references:** SRC-0638, SRC-1609  
**URL references:** None independently associated  
**Related findings:** FND-11655, FND-11656, FND-11657

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
