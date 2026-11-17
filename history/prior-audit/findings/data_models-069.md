# data_models — findings 6801–6900

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-07075"></a>
## FND-07075: message declaration: chesscom.payments.v1.StopRenewalByCardMatchRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StopRenewalByCardMatchRequest {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 615.

```text
_result = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
}

message StopRenewalByCardMatchRequest {
  optional string user_uuid = 1;
  optional string card_last_four = 2;
  optional int32 charge_amount_cents = 3;
  optional string charge_currency = 4;
  optional string charge_date = 5;
  optional .chesscom.support.v1.SupportActionContext context = 6;
}

message StopRenewalByCar
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07076"></a>
## FND-07076: chesscom.payments.v1.StopRenewalByCardMatchRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 153.

```text
rvice.proto
// syntax: proto3

package chesscom.payments.v1;

message CancelSubscriptionRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .ches
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07077"></a>
## FND-07077: chesscom.payments.v1.StopRenewalByCardMatchRequest.card_last_four = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string card_last_four = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 690.

```text
n refusal_reason = 4;
}

message StopRenewalByCardMatchRequest {
  optional string user_uuid = 1;
  optional string card_last_four = 2;
  optional int32 charge_amount_cents = 3;
  optional string charge_currency = 4;
  optional string charge_date = 5;
  optional .chesscom.support.v1.SupportActionContext context = 6;
}

message StopRenewalByCardMatchResponse {
  optional .chesscom.payments.v1.StopRenewalByCardMatchRes
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07078"></a>
## FND-07078: chesscom.payments.v1.StopRenewalByCardMatchRequest.charge_amount_cents = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 charge_amount_cents = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 728.

```text
enewalByCardMatchRequest {
  optional string user_uuid = 1;
  optional string card_last_four = 2;
  optional int32 charge_amount_cents = 3;
  optional string charge_currency = 4;
  optional string charge_date = 5;
  optional .chesscom.support.v1.SupportActionContext context = 6;
}

message StopRenewalByCardMatchResponse {
  optional .chesscom.payments.v1.StopRenewalByCardMatchResult result = 1;
  optional .google.pro
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07079"></a>
## FND-07079: chesscom.payments.v1.StopRenewalByCardMatchRequest.charge_currency = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string charge_currency = 4;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 770.

```text
ng user_uuid = 1;
  optional string card_last_four = 2;
  optional int32 charge_amount_cents = 3;
  optional string charge_currency = 4;
  optional string charge_date = 5;
  optional .chesscom.support.v1.SupportActionContext context = 6;
}

message StopRenewalByCardMatchResponse {
  optional .chesscom.payments.v1.StopRenewalByCardMatchResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  opti
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07080"></a>
## FND-07080: chesscom.payments.v1.StopRenewalByCardMatchRequest.charge_date = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string charge_date = 5;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 809.

```text
d_last_four = 2;
  optional int32 charge_amount_cents = 3;
  optional string charge_currency = 4;
  optional string charge_date = 5;
  optional .chesscom.support.v1.SupportActionContext context = 6;
}

message StopRenewalByCardMatchResponse {
  optional .chesscom.payments.v1.StopRenewalByCardMatchResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportAction
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07081"></a>
## FND-07081: chesscom.payments.v1.StopRenewalByCardMatchRequest.context = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionContext context = 6;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 844.

```text
harge_amount_cents = 3;
  optional string charge_currency = 4;
  optional string charge_date = 5;
  optional .chesscom.support.v1.SupportActionContext context = 6;
}

message StopRenewalByCardMatchResponse {
  optional .chesscom.payments.v1.StopRenewalByCardMatchResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
}

messag
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07082"></a>
## FND-07082: message declaration: chesscom.payments.v1.StopRenewalByCardMatchResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StopRenewalByCardMatchResponse {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 911.

```text
tional string charge_date = 5;
  optional .chesscom.support.v1.SupportActionContext context = 6;
}

message StopRenewalByCardMatchResponse {
  optional .chesscom.payments.v1.StopRenewalByCardMatchResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
}

message ExtendSubscriptionRequest {
  optional string user_uuid = 1;
  op
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07083"></a>
## FND-07083: chesscom.payments.v1.StopRenewalByCardMatchResponse.result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.StopRenewalByCardMatchResult result = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 954.

```text
chesscom.support.v1.SupportActionContext context = 6;
}

message StopRenewalByCardMatchResponse {
  optional .chesscom.payments.v1.StopRenewalByCardMatchResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
}

message ExtendSubscriptionRequest {
  optional string user_uuid = 1;
  optional int32 days = 2;
  optional .chesscom
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07084"></a>
## FND-07084: chesscom.payments.v1.StopRenewalByCardMatchResponse.access_ends_at = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp access_ends_at = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 401.

```text
ancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
}

message StopRenewalByCardMatchRequest {
  optional string user_uuid = 1;
  optional string card_last_four 
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07085"></a>
## FND-07085: chesscom.payments.v1.StopRenewalByCardMatchResponse.action_result = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionResult action_result = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 459.

```text
v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
}

message StopRenewalByCardMatchRequest {
  optional string user_uuid = 1;
  optional string card_last_four = 2;
  optional int32 charge_amount_cents = 3;
  optional 
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07086"></a>
## FND-07086: message declaration: chesscom.payments.v1.ExtendSubscriptionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ExtendSubscriptionRequest {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1158.

```text
stamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
}

message ExtendSubscriptionRequest {
  optional string user_uuid = 1;
  optional int32 days = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string subscription_id = 4;
}

message ExtendSubscriptionResponse {
  optional int32 days_added = 1;
  optional .chesscom.support.v1.SupportActionR
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07087"></a>
## FND-07087: chesscom.payments.v1.ExtendSubscriptionRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 153.

```text
rvice.proto
// syntax: proto3

package chesscom.payments.v1;

message CancelSubscriptionRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .ches
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07088"></a>
## FND-07088: chesscom.payments.v1.ExtendSubscriptionRequest.days = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 days = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1229.

```text
Result action_result = 3;
}

message ExtendSubscriptionRequest {
  optional string user_uuid = 1;
  optional int32 days = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string subscription_id = 4;
}

message ExtendSubscriptionResponse {
  optional int32 days_added = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .google.protobuf.Timestamp current_
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07089"></a>
## FND-07089: chesscom.payments.v1.ExtendSubscriptionRequest.context = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionContext context = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1256.

```text


message ExtendSubscriptionRequest {
  optional string user_uuid = 1;
  optional int32 days = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string subscription_id = 4;
}

message ExtendSubscriptionResponse {
  optional int32 days_added = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .google.protobuf.Timestamp current_period_ends_at = 3;
  optio
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07090"></a>
## FND-07090: chesscom.payments.v1.ExtendSubscriptionRequest.subscription_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string subscription_id = 4;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1322.

```text
= 1;
  optional int32 days = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string subscription_id = 4;
}

message ExtendSubscriptionResponse {
  optional int32 days_added = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .google.protobuf.Timestamp current_period_ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_r
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07091"></a>
## FND-07091: message declaration: chesscom.payments.v1.ExtendSubscriptionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ExtendSubscriptionResponse {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1362.

```text
al .chesscom.support.v1.SupportActionContext context = 3;
  optional string subscription_id = 4;
}

message ExtendSubscriptionResponse {
  optional int32 days_added = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .google.protobuf.Timestamp current_period_ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
}

message GrantGoodwillDiamo
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07092"></a>
## FND-07092: chesscom.payments.v1.ExtendSubscriptionResponse.days_added = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 days_added = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1401.

```text
ntext context = 3;
  optional string subscription_id = 4;
}

message ExtendSubscriptionResponse {
  optional int32 days_added = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .google.protobuf.Timestamp current_period_ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
}

message GrantGoodwillDiamondRequest {
  optional string user_uuid
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07093"></a>
## FND-07093: chesscom.payments.v1.ExtendSubscriptionResponse.action_result = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionResult action_result = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1434.

```text
ing subscription_id = 4;
}

message ExtendSubscriptionResponse {
  optional int32 days_added = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .google.protobuf.Timestamp current_period_ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
}

message GrantGoodwillDiamondRequest {
  optional string user_uuid = 1;
  optional .chesscom.suppor
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07094"></a>
## FND-07094: chesscom.payments.v1.ExtendSubscriptionResponse.current_period_ends_at = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp current_period_ends_at = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1505.

```text
onal int32 days_added = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .google.protobuf.Timestamp current_period_ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
}

message GrantGoodwillDiamondRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional .chesscom.payments.v1
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07095"></a>
## FND-07095: chesscom.payments.v1.ExtendSubscriptionResponse.refusal_reason = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 530.

```text
estamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
}

message StopRenewalByCardMatchRequest {
  optional string user_uuid = 1;
  optional string card_last_four = 2;
  optional int32 charge_amount_cents = 3;
  optional string charge_currency = 4;
  optional string charge_date = 5;
  option
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07096"></a>
## FND-07096: message declaration: chesscom.payments.v1.GrantGoodwillDiamondRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GrantGoodwillDiamondRequest {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1656.

```text
ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
}

message GrantGoodwillDiamondRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional .chesscom.payments.v1.GoodwillSiteFault fault = 3;
}

message GrantGoodwillDiamondResponse {
  optional .chesscom.payments.v1.GrantGoodwillDiamondResult result = 1;
  optio
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07097"></a>
## FND-07097: chesscom.payments.v1.GrantGoodwillDiamondRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 153.

```text
rvice.proto
// syntax: proto3

package chesscom.payments.v1;

message CancelSubscriptionRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .ches
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07098"></a>
## FND-07098: chesscom.payments.v1.GrantGoodwillDiamondRequest.context = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionContext context = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 186.

```text
ckage chesscom.payments.v1;

message CancelSubscriptionRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResu
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07099"></a>
## FND-07099: chesscom.payments.v1.GrantGoodwillDiamondRequest.fault = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.GoodwillSiteFault fault = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1795.

```text
 optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional .chesscom.payments.v1.GoodwillSiteFault fault = 3;
}

message GrantGoodwillDiamondResponse {
  optional .chesscom.payments.v1.GrantGoodwillDiamondResult result = 1;
  optional int32 days_granted = 2;
  optional string plan = 3;
  optional .google.protobuf.Timestamp access_ends_at = 4;
  optional .chesscom.paym
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07100"></a>
## FND-07100: message declaration: chesscom.payments.v1.GrantGoodwillDiamondResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GrantGoodwillDiamondResponse {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1858.

```text
.SupportActionContext context = 2;
  optional .chesscom.payments.v1.GoodwillSiteFault fault = 3;
}

message GrantGoodwillDiamondResponse {
  optional .chesscom.payments.v1.GrantGoodwillDiamondResult result = 1;
  optional int32 days_granted = 2;
  optional string plan = 3;
  optional .google.protobuf.Timestamp access_ends_at = 4;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;
  op
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07101"></a>
## FND-07101: chesscom.payments.v1.GrantGoodwillDiamondResponse.result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.GrantGoodwillDiamondResult result = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1899.

```text
onal .chesscom.payments.v1.GoodwillSiteFault fault = 3;
}

message GrantGoodwillDiamondResponse {
  optional .chesscom.payments.v1.GrantGoodwillDiamondResult result = 1;
  optional int32 days_granted = 2;
  optional string plan = 3;
  optional .google.protobuf.Timestamp access_ends_at = 4;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;
  optional .google.protobuf.Timestamp next_el
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07102"></a>
## FND-07102: chesscom.payments.v1.GrantGoodwillDiamondResponse.days_granted = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 days_granted = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1971.

```text
GoodwillDiamondResponse {
  optional .chesscom.payments.v1.GrantGoodwillDiamondResult result = 1;
  optional int32 days_granted = 2;
  optional string plan = 3;
  optional .google.protobuf.Timestamp access_ends_at = 4;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;
  optional .google.protobuf.Timestamp next_eligible_at = 6;
  optional .chesscom.support.v1.SupportActionResult actio
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07103"></a>
## FND-07103: chesscom.payments.v1.GrantGoodwillDiamondResponse.plan = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string plan = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2006.

```text
l .chesscom.payments.v1.GrantGoodwillDiamondResult result = 1;
  optional int32 days_granted = 2;
  optional string plan = 3;
  optional .google.protobuf.Timestamp access_ends_at = 4;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;
  optional .google.protobuf.Timestamp next_eligible_at = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
}

message GrantNoAds
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07104"></a>
## FND-07104: chesscom.payments.v1.GrantGoodwillDiamondResponse.access_ends_at = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp access_ends_at = 4;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2034.

```text
tGoodwillDiamondResult result = 1;
  optional int32 days_granted = 2;
  optional string plan = 3;
  optional .google.protobuf.Timestamp access_ends_at = 4;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;
  optional .google.protobuf.Timestamp next_eligible_at = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
}

message GrantNoAdsOfferRequest {
  optional st
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07105"></a>
## FND-07105: chesscom.payments.v1.GrantGoodwillDiamondResponse.refusal_reason = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2092.

```text
ranted = 2;
  optional string plan = 3;
  optional .google.protobuf.Timestamp access_ends_at = 4;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;
  optional .google.protobuf.Timestamp next_eligible_at = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
}

message GrantNoAdsOfferRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.Suppor
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07106"></a>
## FND-07106: chesscom.payments.v1.GrantGoodwillDiamondResponse.next_eligible_at = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp next_eligible_at = 6;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2176.

```text
_ends_at = 4;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;
  optional .google.protobuf.Timestamp next_eligible_at = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
}

message GrantNoAdsOfferRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
}

message GrantNoAdsOfferResponse {
  optional int32 da
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07107"></a>
## FND-07107: chesscom.payments.v1.GrantGoodwillDiamondResponse.action_result = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionResult action_result = 7;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2236.

```text
dminRefusalReason refusal_reason = 5;
  optional .google.protobuf.Timestamp next_eligible_at = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
}

message GrantNoAdsOfferRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
}

message GrantNoAdsOfferResponse {
  optional int32 days_granted = 1;
  optional string plan = 2;
  optional .goog
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07108"></a>
## FND-07108: message declaration: chesscom.payments.v1.GrantNoAdsOfferRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GrantNoAdsOfferRequest {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2308.

```text
amp next_eligible_at = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
}

message GrantNoAdsOfferRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
}

message GrantNoAdsOfferResponse {
  optional int32 days_granted = 1;
  optional string plan = 2;
  optional .google.protobuf.Timestamp access_ends_at = 3;
  optional .chesscom.payments.
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07109"></a>
## FND-07109: chesscom.payments.v1.GrantNoAdsOfferRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 153.

```text
rvice.proto
// syntax: proto3

package chesscom.payments.v1;

message CancelSubscriptionRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .ches
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07110"></a>
## FND-07110: chesscom.payments.v1.GrantNoAdsOfferRequest.context = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionContext context = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 186.

```text
ckage chesscom.payments.v1;

message CancelSubscriptionRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResu
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07111"></a>
## FND-07111: message declaration: chesscom.payments.v1.GrantNoAdsOfferResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GrantNoAdsOfferResponse {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2443.

```text
optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
}

message GrantNoAdsOfferResponse {
  optional int32 days_granted = 1;
  optional string plan = 2;
  optional .google.protobuf.Timestamp access_ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
  optional .google.protobuf.Timestamp next_eligible_at = 5;
  optional .chesscom.
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07112"></a>
## FND-07112: chesscom.payments.v1.GrantNoAdsOfferResponse.days_granted = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 days_granted = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2479.

```text
ional .chesscom.support.v1.SupportActionContext context = 2;
}

message GrantNoAdsOfferResponse {
  optional int32 days_granted = 1;
  optional string plan = 2;
  optional .google.protobuf.Timestamp access_ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
  optional .google.protobuf.Timestamp next_eligible_at = 5;
  optional .chesscom.support.v1.SupportActionResult actio
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07113"></a>
## FND-07113: chesscom.payments.v1.GrantNoAdsOfferResponse.plan = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string plan = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2514.

```text
ctionContext context = 2;
}

message GrantNoAdsOfferResponse {
  optional int32 days_granted = 1;
  optional string plan = 2;
  optional .google.protobuf.Timestamp access_ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
  optional .google.protobuf.Timestamp next_eligible_at = 5;
  optional .chesscom.support.v1.SupportActionResult action_result = 6;
}

message TransferMe
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07114"></a>
## FND-07114: chesscom.payments.v1.GrantNoAdsOfferResponse.access_ends_at = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp access_ends_at = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2542.

```text

message GrantNoAdsOfferResponse {
  optional int32 days_granted = 1;
  optional string plan = 2;
  optional .google.protobuf.Timestamp access_ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
  optional .google.protobuf.Timestamp next_eligible_at = 5;
  optional .chesscom.support.v1.SupportActionResult action_result = 6;
}

message TransferMembershipRequest {
  optional
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07115"></a>
## FND-07115: chesscom.payments.v1.GrantNoAdsOfferResponse.refusal_reason = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 530.

```text
estamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
}

message StopRenewalByCardMatchRequest {
  optional string user_uuid = 1;
  optional string card_last_four = 2;
  optional int32 charge_amount_cents = 3;
  optional string charge_currency = 4;
  optional string charge_date = 5;
  option
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07116"></a>
## FND-07116: chesscom.payments.v1.GrantNoAdsOfferResponse.next_eligible_at = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp next_eligible_at = 5;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2684.

```text
_ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
  optional .google.protobuf.Timestamp next_eligible_at = 5;
  optional .chesscom.support.v1.SupportActionResult action_result = 6;
}

message TransferMembershipRequest {
  optional string from_user_uuid = 1;
  optional string to_user_uuid = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional s
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07117"></a>
## FND-07117: chesscom.payments.v1.GrantNoAdsOfferResponse.action_result = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionResult action_result = 6;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2744.

```text
dminRefusalReason refusal_reason = 4;
  optional .google.protobuf.Timestamp next_eligible_at = 5;
  optional .chesscom.support.v1.SupportActionResult action_result = 6;
}

message TransferMembershipRequest {
  optional string from_user_uuid = 1;
  optional string to_user_uuid = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string from_verification_id = 4;
  optional string to_verific
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07118"></a>
## FND-07118: message declaration: chesscom.payments.v1.TransferMembershipRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TransferMembershipRequest {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2816.

```text
amp next_eligible_at = 5;
  optional .chesscom.support.v1.SupportActionResult action_result = 6;
}

message TransferMembershipRequest {
  optional string from_user_uuid = 1;
  optional string to_user_uuid = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string from_verification_id = 4;
  optional string to_verification_id = 5;
}

message TransferMembershipResponse {
  optional int32 s
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07119"></a>
## FND-07119: chesscom.payments.v1.TransferMembershipRequest.from_user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string from_user_uuid = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2854.

```text
chesscom.support.v1.SupportActionResult action_result = 6;
}

message TransferMembershipRequest {
  optional string from_user_uuid = 1;
  optional string to_user_uuid = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string from_verification_id = 4;
  optional string to_verification_id = 5;
}

message TransferMembershipResponse {
  optional int32 subscriptions_transferred = 1;
  option
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07120"></a>
## FND-07120: chesscom.payments.v1.TransferMembershipRequest.to_user_uuid = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string to_user_uuid = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2892.

```text
t action_result = 6;
}

message TransferMembershipRequest {
  optional string from_user_uuid = 1;
  optional string to_user_uuid = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string from_verification_id = 4;
  optional string to_verification_id = 5;
}

message TransferMembershipResponse {
  optional int32 subscriptions_transferred = 1;
  optional .chesscom.support.v1.SupportActionR
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07121"></a>
## FND-07121: chesscom.payments.v1.TransferMembershipRequest.context = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionContext context = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1256.

```text


message ExtendSubscriptionRequest {
  optional string user_uuid = 1;
  optional int32 days = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string subscription_id = 4;
}

message ExtendSubscriptionResponse {
  optional int32 days_added = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .google.protobuf.Timestamp current_period_ends_at = 3;
  optio
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07122"></a>
## FND-07122: chesscom.payments.v1.TransferMembershipRequest.from_verification_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string from_verification_id = 4;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2994.

```text
tional string to_user_uuid = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string from_verification_id = 4;
  optional string to_verification_id = 5;
}

message TransferMembershipResponse {
  optional int32 subscriptions_transferred = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reaso
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07123"></a>
## FND-07123: chesscom.payments.v1.TransferMembershipRequest.to_verification_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string to_verification_id = 5;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 3038.

```text
chesscom.support.v1.SupportActionContext context = 3;
  optional string from_verification_id = 4;
  optional string to_verification_id = 5;
}

message TransferMembershipResponse {
  optional int32 subscriptions_transferred = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 3;
}

message GrantMembershipRequest {
 
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07124"></a>
## FND-07124: message declaration: chesscom.payments.v1.TransferMembershipResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TransferMembershipResponse {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 3081.

```text
ntext = 3;
  optional string from_verification_id = 4;
  optional string to_verification_id = 5;
}

message TransferMembershipResponse {
  optional int32 subscriptions_transferred = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 3;
}

message GrantMembershipRequest {
  oneof basis {
  .chesscom.payments.v1.Paid
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07125"></a>
## FND-07125: chesscom.payments.v1.TransferMembershipResponse.subscriptions_transferred = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 subscriptions_transferred = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 3120.

```text
ication_id = 4;
  optional string to_verification_id = 5;
}

message TransferMembershipResponse {
  optional int32 subscriptions_transferred = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 3;
}

message GrantMembershipRequest {
  oneof basis {
  .chesscom.payments.v1.PaidOrderBasis paid_order = 3;
  .chesscom.
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07126"></a>
## FND-07126: chesscom.payments.v1.TransferMembershipResponse.action_result = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionResult action_result = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1434.

```text
ing subscription_id = 4;
}

message ExtendSubscriptionResponse {
  optional int32 days_added = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .google.protobuf.Timestamp current_period_ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
}

message GrantGoodwillDiamondRequest {
  optional string user_uuid = 1;
  optional .chesscom.suppor
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07127"></a>
## FND-07127: chesscom.payments.v1.TransferMembershipResponse.refusal_reason = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 3239.

```text
criptions_transferred = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 3;
}

message GrantMembershipRequest {
  oneof basis {
  .chesscom.payments.v1.PaidOrderBasis paid_order = 3;
  .chesscom.payments.v1.PartnerMembershipBasis partner_membership = 4;
  }
  optional string user_uuid = 1;
  optional .chesscom.su
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07128"></a>
## FND-07128: message declaration: chesscom.payments.v1.GrantMembershipRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GrantMembershipRequest {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 3324.

```text
_result = 2;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 3;
}

message GrantMembershipRequest {
  oneof basis {
  .chesscom.payments.v1.PaidOrderBasis paid_order = 3;
  .chesscom.payments.v1.PartnerMembershipBasis partner_membership = 4;
  }
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
}

message GrantMembershipResponse {
  opt
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07129"></a>
## FND-07129: oneof declaration: chesscom.payments.v1.GrantMembershipRequest.basis

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof basis {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 3359.

```text
ayments.v1.SubscriptionAdminRefusalReason refusal_reason = 3;
}

message GrantMembershipRequest {
  oneof basis {
  .chesscom.payments.v1.PaidOrderBasis paid_order = 3;
  .chesscom.payments.v1.PartnerMembershipBasis partner_membership = 4;
  }
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
}

message GrantMembershipResponse {
  optional string plan = 1;
  optional s
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07130"></a>
## FND-07130: chesscom.payments.v1.GrantMembershipRequest.paid_order = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.PaidOrderBasis paid_order = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 3375.

```text
riptionAdminRefusalReason refusal_reason = 3;
}

message GrantMembershipRequest {
  oneof basis {
  .chesscom.payments.v1.PaidOrderBasis paid_order = 3;
  .chesscom.payments.v1.PartnerMembershipBasis partner_membership = 4;
  }
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
}

message GrantMembershipResponse {
  optional string plan = 1;
  optional string subscripti
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07131"></a>
## FND-07131: chesscom.payments.v1.GrantMembershipRequest.partner_membership = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.PartnerMembershipBasis partner_membership = 4;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 3430.

```text
e GrantMembershipRequest {
  oneof basis {
  .chesscom.payments.v1.PaidOrderBasis paid_order = 3;
  .chesscom.payments.v1.PartnerMembershipBasis partner_membership = 4;
  }
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
}

message GrantMembershipResponse {
  optional string plan = 1;
  optional string subscription_id = 2;
  optional .google.protobuf.Timestamp access
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07132"></a>
## FND-07132: chesscom.payments.v1.GrantMembershipRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 153.

```text
rvice.proto
// syntax: proto3

package chesscom.payments.v1;

message CancelSubscriptionRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .ches
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07133"></a>
## FND-07133: chesscom.payments.v1.GrantMembershipRequest.context = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionContext context = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 186.

```text
ckage chesscom.payments.v1;

message CancelSubscriptionRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResu
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07134"></a>
## FND-07134: message declaration: chesscom.payments.v1.GrantMembershipResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GrantMembershipResponse {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 3605.

```text
optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
}

message GrantMembershipResponse {
  optional string plan = 1;
  optional string subscription_id = 2;
  optional .google.protobuf.Timestamp access_ends_at = 3;
  optional .chesscom.support.v1.SupportActionResult action_result = 4;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;
}

mes
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07135"></a>
## FND-07135: chesscom.payments.v1.GrantMembershipResponse.plan = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string plan = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 3641.

```text
ional .chesscom.support.v1.SupportActionContext context = 2;
}

message GrantMembershipResponse {
  optional string plan = 1;
  optional string subscription_id = 2;
  optional .google.protobuf.Timestamp access_ends_at = 3;
  optional .chesscom.support.v1.SupportActionResult action_result = 4;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;
}

message SwitchToMonthlyRequest {
  opti
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07136"></a>
## FND-07136: chesscom.payments.v1.GrantMembershipResponse.subscription_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string subscription_id = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 3669.

```text
upportActionContext context = 2;
}

message GrantMembershipResponse {
  optional string plan = 1;
  optional string subscription_id = 2;
  optional .google.protobuf.Timestamp access_ends_at = 3;
  optional .chesscom.support.v1.SupportActionResult action_result = 4;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;
}

message SwitchToMonthlyRequest {
  optional string user_uuid = 1;
 
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07137"></a>
## FND-07137: chesscom.payments.v1.GrantMembershipResponse.access_ends_at = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp access_ends_at = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2542.

```text

message GrantNoAdsOfferResponse {
  optional int32 days_granted = 1;
  optional string plan = 2;
  optional .google.protobuf.Timestamp access_ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
  optional .google.protobuf.Timestamp next_eligible_at = 5;
  optional .chesscom.support.v1.SupportActionResult action_result = 6;
}

message TransferMembershipRequest {
  optional
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07138"></a>
## FND-07138: chesscom.payments.v1.GrantMembershipResponse.action_result = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionResult action_result = 4;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 3766.

```text

  optional string subscription_id = 2;
  optional .google.protobuf.Timestamp access_ends_at = 3;
  optional .chesscom.support.v1.SupportActionResult action_result = 4;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;
}

message SwitchToMonthlyRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_i
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07139"></a>
## FND-07139: chesscom.payments.v1.GrantMembershipResponse.refusal_reason = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2092.

```text
ranted = 2;
  optional string plan = 3;
  optional .google.protobuf.Timestamp access_ends_at = 4;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;
  optional .google.protobuf.Timestamp next_eligible_at = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
}

message GrantNoAdsOfferRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.Suppor
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07140"></a>
## FND-07140: message declaration: chesscom.payments.v1.SwitchToMonthlyRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SwitchToMonthlyRequest {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 3922.

```text
_result = 4;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 5;
}

message SwitchToMonthlyRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message SwitchToMonthlyResponse {
  optional .chesscom.payments.v1.SwitchToMonthlyResult result = 1;
  optional string current_plan = 2;
  optiona
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07141"></a>
## FND-07141: chesscom.payments.v1.SwitchToMonthlyRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 153.

```text
rvice.proto
// syntax: proto3

package chesscom.payments.v1;

message CancelSubscriptionRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .ches
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07142"></a>
## FND-07142: chesscom.payments.v1.SwitchToMonthlyRequest.context = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionContext context = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 186.

```text
ckage chesscom.payments.v1;

message CancelSubscriptionRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResu
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07143"></a>
## FND-07143: chesscom.payments.v1.SwitchToMonthlyRequest.subscription_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string subscription_id = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 252.

```text
 optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
  optional .chesscom.payments.v1.Subscriptio
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07144"></a>
## FND-07144: message declaration: chesscom.payments.v1.SwitchToMonthlyResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SwitchToMonthlyResponse {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4096.

```text
al .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message SwitchToMonthlyResponse {
  optional .chesscom.payments.v1.SwitchToMonthlyResult result = 1;
  optional string current_plan = 2;
  optional string target_plan = 3;
  optional int32 refund_cents = 4;
  optional string currency = 5;
  optional string refund_id = 6;
  optional .chesscom.support.v1.SupportActionRes
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07145"></a>
## FND-07145: chesscom.payments.v1.SwitchToMonthlyResponse.result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.SwitchToMonthlyResult result = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4132.

```text
nContext context = 2;
  optional string subscription_id = 3;
}

message SwitchToMonthlyResponse {
  optional .chesscom.payments.v1.SwitchToMonthlyResult result = 1;
  optional string current_plan = 2;
  optional string target_plan = 3;
  optional int32 refund_cents = 4;
  optional string currency = 5;
  optional string refund_id = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
  optional .c
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07146"></a>
## FND-07146: chesscom.payments.v1.SwitchToMonthlyResponse.current_plan = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string current_plan = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4199.

```text
sage SwitchToMonthlyResponse {
  optional .chesscom.payments.v1.SwitchToMonthlyResult result = 1;
  optional string current_plan = 2;
  optional string target_plan = 3;
  optional int32 refund_cents = 4;
  optional string currency = 5;
  optional string refund_id = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason =
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07147"></a>
## FND-07147: chesscom.payments.v1.SwitchToMonthlyResponse.target_plan = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string target_plan = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4235.

```text
ional .chesscom.payments.v1.SwitchToMonthlyResult result = 1;
  optional string current_plan = 2;
  optional string target_plan = 3;
  optional int32 refund_cents = 4;
  optional string currency = 5;
  optional string refund_id = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 8;
  optional .chesscom.payments.v1
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07148"></a>
## FND-07148: chesscom.payments.v1.SwitchToMonthlyResponse.refund_cents = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 refund_cents = 4;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4270.

```text
oMonthlyResult result = 1;
  optional string current_plan = 2;
  optional string target_plan = 3;
  optional int32 refund_cents = 4;
  optional string currency = 5;
  optional string refund_id = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 8;
  optional .chesscom.payments.v1.MonthlySwitchIneligibility ineligi
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07149"></a>
## FND-07149: chesscom.payments.v1.SwitchToMonthlyResponse.currency = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string currency = 5;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4305.

```text
al string current_plan = 2;
  optional string target_plan = 3;
  optional int32 refund_cents = 4;
  optional string currency = 5;
  optional string refund_id = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 8;
  optional .chesscom.payments.v1.MonthlySwitchIneligibility ineligibility = 9;
}

message GetFamilyPla
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07150"></a>
## FND-07150: chesscom.payments.v1.SwitchToMonthlyResponse.refund_id = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string refund_id = 6;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4337.

```text
tional string target_plan = 3;
  optional int32 refund_cents = 4;
  optional string currency = 5;
  optional string refund_id = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 8;
  optional .chesscom.payments.v1.MonthlySwitchIneligibility ineligibility = 9;
}

message GetFamilyPlanInvitationsRequest {
  optional
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07151"></a>
## FND-07151: chesscom.payments.v1.SwitchToMonthlyResponse.action_result = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionResult action_result = 7;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 2236.

```text
dminRefusalReason refusal_reason = 5;
  optional .google.protobuf.Timestamp next_eligible_at = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
}

message GrantNoAdsOfferRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
}

message GrantNoAdsOfferResponse {
  optional int32 days_granted = 1;
  optional string plan = 2;
  optional .goog
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07152"></a>
## FND-07152: chesscom.payments.v1.SwitchToMonthlyResponse.refusal_reason = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 8;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4441.

```text
onal string refund_id = 6;
  optional .chesscom.support.v1.SupportActionResult action_result = 7;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 8;
  optional .chesscom.payments.v1.MonthlySwitchIneligibility ineligibility = 9;
}

message GetFamilyPlanInvitationsRequest {
  optional string user_uuid = 1;
  repeated string invitee_user_uuids = 2;
  optional string verification_id = 3;

```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07153"></a>
## FND-07153: chesscom.payments.v1.SwitchToMonthlyResponse.ineligibility = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.MonthlySwitchIneligibility ineligibility = 9;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4525.

```text
n_result = 7;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 8;
  optional .chesscom.payments.v1.MonthlySwitchIneligibility ineligibility = 9;
}

message GetFamilyPlanInvitationsRequest {
  optional string user_uuid = 1;
  repeated string invitee_user_uuids = 2;
  optional string verification_id = 3;
}

message GetFamilyPlanInvitationsResponse {
  optional .chesscom.payments.v1.Suppo
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07154"></a>
## FND-07154: message declaration: chesscom.payments.v1.GetFamilyPlanInvitationsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetFamilyPlanInvitationsRequest {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4605.

```text
fusal_reason = 8;
  optional .chesscom.payments.v1.MonthlySwitchIneligibility ineligibility = 9;
}

message GetFamilyPlanInvitationsRequest {
  optional string user_uuid = 1;
  repeated string invitee_user_uuids = 2;
  optional string verification_id = 3;
}

message GetFamilyPlanInvitationsResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanState plan_state = 1;
  optional int32 secondary_member_count = 2;
 
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07155"></a>
## FND-07155: chesscom.payments.v1.GetFamilyPlanInvitationsRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 153.

```text
rvice.proto
// syntax: proto3

package chesscom.payments.v1;

message CancelSubscriptionRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .ches
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07156"></a>
## FND-07156: chesscom.payments.v1.GetFamilyPlanInvitationsRequest.invitee_user_uuids = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string invitee_user_uuids = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4682.

```text
 ineligibility = 9;
}

message GetFamilyPlanInvitationsRequest {
  optional string user_uuid = 1;
  repeated string invitee_user_uuids = 2;
  optional string verification_id = 3;
}

message GetFamilyPlanInvitationsResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanState plan_state = 1;
  optional int32 secondary_member_count = 2;
  optional int32 max_secondary_members = 3;
  repeated .chesscom.payments.v1.S
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07157"></a>
## FND-07157: chesscom.payments.v1.GetFamilyPlanInvitationsRequest.verification_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string verification_id = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4724.

```text
anInvitationsRequest {
  optional string user_uuid = 1;
  repeated string invitee_user_uuids = 2;
  optional string verification_id = 3;
}

message GetFamilyPlanInvitationsResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanState plan_state = 1;
  optional int32 secondary_member_count = 2;
  optional int32 max_secondary_members = 3;
  repeated .chesscom.payments.v1.SupportFamilyPlanInvitation invitations = 4
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07158"></a>
## FND-07158: message declaration: chesscom.payments.v1.GetFamilyPlanInvitationsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetFamilyPlanInvitationsResponse {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4764.

```text
 user_uuid = 1;
  repeated string invitee_user_uuids = 2;
  optional string verification_id = 3;
}

message GetFamilyPlanInvitationsResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanState plan_state = 1;
  optional int32 secondary_member_count = 2;
  optional int32 max_secondary_members = 3;
  repeated .chesscom.payments.v1.SupportFamilyPlanInvitation invitations = 4;
  repeated .chesscom.payments.v1.Suppo
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07159"></a>
## FND-07159: chesscom.payments.v1.GetFamilyPlanInvitationsResponse.plan_state = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.SupportFamilyPlanState plan_state = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4809.

```text
r_uuids = 2;
  optional string verification_id = 3;
}

message GetFamilyPlanInvitationsResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanState plan_state = 1;
  optional int32 secondary_member_count = 2;
  optional int32 max_secondary_members = 3;
  repeated .chesscom.payments.v1.SupportFamilyPlanInvitation invitations = 4;
  repeated .chesscom.payments.v1.SupportFamilyPlanInviteeCheck invitee_checks = 5;

```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07160"></a>
## FND-07160: chesscom.payments.v1.GetFamilyPlanInvitationsResponse.secondary_member_count = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 secondary_member_count = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4881.

```text
PlanInvitationsResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanState plan_state = 1;
  optional int32 secondary_member_count = 2;
  optional int32 max_secondary_members = 3;
  repeated .chesscom.payments.v1.SupportFamilyPlanInvitation invitations = 4;
  repeated .chesscom.payments.v1.SupportFamilyPlanInviteeCheck invitee_checks = 5;
}

message RevokeFamilyPlanInvitationRequest {
  optional string user_uu
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07161"></a>
## FND-07161: chesscom.payments.v1.GetFamilyPlanInvitationsResponse.max_secondary_members = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 max_secondary_members = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4926.

```text
m.payments.v1.SupportFamilyPlanState plan_state = 1;
  optional int32 secondary_member_count = 2;
  optional int32 max_secondary_members = 3;
  repeated .chesscom.payments.v1.SupportFamilyPlanInvitation invitations = 4;
  repeated .chesscom.payments.v1.SupportFamilyPlanInviteeCheck invitee_checks = 5;
}

message RevokeFamilyPlanInvitationRequest {
  optional string user_uuid = 1;
  optional string invitation_ref = 2;
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07162"></a>
## FND-07162: chesscom.payments.v1.GetFamilyPlanInvitationsResponse.invitations = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.SupportFamilyPlanInvitation invitations = 4;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4970.

```text
ate = 1;
  optional int32 secondary_member_count = 2;
  optional int32 max_secondary_members = 3;
  repeated .chesscom.payments.v1.SupportFamilyPlanInvitation invitations = 4;
  repeated .chesscom.payments.v1.SupportFamilyPlanInviteeCheck invitee_checks = 5;
}

message RevokeFamilyPlanInvitationRequest {
  optional string user_uuid = 1;
  optional string invitation_ref = 2;
  optional string verification_id = 3;
  op
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07163"></a>
## FND-07163: chesscom.payments.v1.GetFamilyPlanInvitationsResponse.invitee_checks = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.SupportFamilyPlanInviteeCheck invitee_checks = 5;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 5048.

```text
ondary_members = 3;
  repeated .chesscom.payments.v1.SupportFamilyPlanInvitation invitations = 4;
  repeated .chesscom.payments.v1.SupportFamilyPlanInviteeCheck invitee_checks = 5;
}

message RevokeFamilyPlanInvitationRequest {
  optional string user_uuid = 1;
  optional string invitation_ref = 2;
  optional string verification_id = 3;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message Revok
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07164"></a>
## FND-07164: message declaration: chesscom.payments.v1.RevokeFamilyPlanInvitationRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RevokeFamilyPlanInvitationRequest {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 5132.

```text
itations = 4;
  repeated .chesscom.payments.v1.SupportFamilyPlanInviteeCheck invitee_checks = 5;
}

message RevokeFamilyPlanInvitationRequest {
  optional string user_uuid = 1;
  optional string invitation_ref = 2;
  optional string verification_id = 3;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message RevokeFamilyPlanInvitationResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanRe
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07165"></a>
## FND-07165: chesscom.payments.v1.RevokeFamilyPlanInvitationRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 153.

```text
rvice.proto
// syntax: proto3

package chesscom.payments.v1;

message CancelSubscriptionRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .ches
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07166"></a>
## FND-07166: chesscom.payments.v1.RevokeFamilyPlanInvitationRequest.invitation_ref = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string invitation_ref = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 5211.

```text
vitee_checks = 5;
}

message RevokeFamilyPlanInvitationRequest {
  optional string user_uuid = 1;
  optional string invitation_ref = 2;
  optional string verification_id = 3;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message RevokeFamilyPlanInvitationResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanRevokeResult result = 1;
  optional .chesscom.support.v1.SupportActionResult acti
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07167"></a>
## FND-07167: chesscom.payments.v1.RevokeFamilyPlanInvitationRequest.verification_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string verification_id = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4724.

```text
anInvitationsRequest {
  optional string user_uuid = 1;
  repeated string invitee_user_uuids = 2;
  optional string verification_id = 3;
}

message GetFamilyPlanInvitationsResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanState plan_state = 1;
  optional int32 secondary_member_count = 2;
  optional int32 max_secondary_members = 3;
  repeated .chesscom.payments.v1.SupportFamilyPlanInvitation invitations = 4
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07168"></a>
## FND-07168: chesscom.payments.v1.RevokeFamilyPlanInvitationRequest.context = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionContext context = 4;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 5288.

```text
tring user_uuid = 1;
  optional string invitation_ref = 2;
  optional string verification_id = 3;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message RevokeFamilyPlanInvitationResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanRevokeResult result = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
}

message ClearFamilyPlanTrialCooldownRequest {
  optional st
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07169"></a>
## FND-07169: message declaration: chesscom.payments.v1.RevokeFamilyPlanInvitationResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RevokeFamilyPlanInvitationResponse {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 5355.

```text
al string verification_id = 3;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message RevokeFamilyPlanInvitationResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanRevokeResult result = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
}

message ClearFamilyPlanTrialCooldownRequest {
  optional string user_uuid = 1;
  optional string invitee_user_uuid = 2;
  opti
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07170"></a>
## FND-07170: chesscom.payments.v1.RevokeFamilyPlanInvitationResponse.result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.SupportFamilyPlanRevokeResult result = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 5402.

```text
scom.support.v1.SupportActionContext context = 4;
}

message RevokeFamilyPlanInvitationResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanRevokeResult result = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
}

message ClearFamilyPlanTrialCooldownRequest {
  optional string user_uuid = 1;
  optional string invitee_user_uuid = 2;
  optional string verification_id = 3;
  optional .ch
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07171"></a>
## FND-07171: chesscom.payments.v1.RevokeFamilyPlanInvitationResponse.action_result = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionResult action_result = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1434.

```text
ing subscription_id = 4;
}

message ExtendSubscriptionResponse {
  optional int32 days_added = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .google.protobuf.Timestamp current_period_ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
}

message GrantGoodwillDiamondRequest {
  optional string user_uuid = 1;
  optional .chesscom.suppor
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07172"></a>
## FND-07172: message declaration: chesscom.payments.v1.ClearFamilyPlanTrialCooldownRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ClearFamilyPlanTrialCooldownRequest {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 5549.

```text
nRevokeResult result = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
}

message ClearFamilyPlanTrialCooldownRequest {
  optional string user_uuid = 1;
  optional string invitee_user_uuid = 2;
  optional string verification_id = 3;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message ClearFamilyPlanTrialCooldownResponse {
  optional .chesscom.payments.v1.SupportFamil
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07173"></a>
## FND-07173: chesscom.payments.v1.ClearFamilyPlanTrialCooldownRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 153.

```text
rvice.proto
// syntax: proto3

package chesscom.payments.v1;

message CancelSubscriptionRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .ches
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07174"></a>
## FND-07174: chesscom.payments.v1.ClearFamilyPlanTrialCooldownRequest.invitee_user_uuid = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string invitee_user_uuid = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 5630.

```text
ion_result = 2;
}

message ClearFamilyPlanTrialCooldownRequest {
  optional string user_uuid = 1;
  optional string invitee_user_uuid = 2;
  optional string verification_id = 3;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message ClearFamilyPlanTrialCooldownResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanCooldownResult result = 1;
  optional .chesscom.support.v1.SupportActionResu
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
