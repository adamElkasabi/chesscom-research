# data_models — findings 6501–6600

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-06775"></a>
## FND-06775: chesscom.payments.v1.Incentive.discount_percentage = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float discount_percentage = 5;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 199.

```text
essage Incentive {
  oneof _free_time {
  int32 free_time = 4;
  }
  oneof _discount_percentage {
  float discount_percentage = 5;
  }
  oneof _discount_amount {
  .chesscom.api.v1.Money discount_amount = 6;
  }
  oneof _discount_charge_type {
  .chesscom.payments.v1.IncentiveChargeType discount_charge_type = 7;
  }
  oneof _discount_recurring_limit {
  int32 discount_recurring_limit = 8;
  }
  oneof _is_payment_info
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06776"></a>
## FND-06776: oneof declaration: chesscom.payments.v1.Incentive._discount_amount

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _discount_amount {

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 236.

```text
 {
  int32 free_time = 4;
  }
  oneof _discount_percentage {
  float discount_percentage = 5;
  }
  oneof _discount_amount {
  .chesscom.api.v1.Money discount_amount = 6;
  }
  oneof _discount_charge_type {
  .chesscom.payments.v1.IncentiveChargeType discount_charge_type = 7;
  }
  oneof _discount_recurring_limit {
  int32 discount_recurring_limit = 8;
  }
  oneof _is_payment_information_required {
  bool is_payment_
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06777"></a>
## FND-06777: chesscom.payments.v1.Incentive.discount_amount = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.Money discount_amount = 6;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 263.

```text
 }
  oneof _discount_percentage {
  float discount_percentage = 5;
  }
  oneof _discount_amount {
  .chesscom.api.v1.Money discount_amount = 6;
  }
  oneof _discount_charge_type {
  .chesscom.payments.v1.IncentiveChargeType discount_charge_type = 7;
  }
  oneof _discount_recurring_limit {
  int32 discount_recurring_limit = 8;
  }
  oneof _is_payment_information_required {
  bool is_payment_information_required = 10;

```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06778"></a>
## FND-06778: oneof declaration: chesscom.payments.v1.Incentive._discount_charge_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _discount_charge_type {

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 313.

```text
_percentage = 5;
  }
  oneof _discount_amount {
  .chesscom.api.v1.Money discount_amount = 6;
  }
  oneof _discount_charge_type {
  .chesscom.payments.v1.IncentiveChargeType discount_charge_type = 7;
  }
  oneof _discount_recurring_limit {
  int32 discount_recurring_limit = 8;
  }
  oneof _is_payment_information_required {
  bool is_payment_information_required = 10;
  }
  oneof _expires_at {
  .google.protobuf.Times
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06779"></a>
## FND-06779: chesscom.payments.v1.Incentive.discount_charge_type = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.IncentiveChargeType discount_charge_type = 7;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 345.

```text
scount_amount {
  .chesscom.api.v1.Money discount_amount = 6;
  }
  oneof _discount_charge_type {
  .chesscom.payments.v1.IncentiveChargeType discount_charge_type = 7;
  }
  oneof _discount_recurring_limit {
  int32 discount_recurring_limit = 8;
  }
  oneof _is_payment_information_required {
  bool is_payment_information_required = 10;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 12;
  }
  oneo
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06780"></a>
## FND-06780: oneof declaration: chesscom.payments.v1.Incentive._discount_recurring_limit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _discount_recurring_limit {

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 419.

```text
_discount_charge_type {
  .chesscom.payments.v1.IncentiveChargeType discount_charge_type = 7;
  }
  oneof _discount_recurring_limit {
  int32 discount_recurring_limit = 8;
  }
  oneof _is_payment_information_required {
  bool is_payment_information_required = 10;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 12;
  }
  oneof _starts_at {
  .google.protobuf.Timestamp starts_at = 13;
  }
  oneof _p
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06781"></a>
## FND-06781: chesscom.payments.v1.Incentive.discount_recurring_limit = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 discount_recurring_limit = 8;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 455.

```text
payments.v1.IncentiveChargeType discount_charge_type = 7;
  }
  oneof _discount_recurring_limit {
  int32 discount_recurring_limit = 8;
  }
  oneof _is_payment_information_required {
  bool is_payment_information_required = 10;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 12;
  }
  oneof _starts_at {
  .google.protobuf.Timestamp starts_at = 13;
  }
  oneof _product {
  string product = 14;
  }

```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06782"></a>
## FND-06782: oneof declaration: chesscom.payments.v1.Incentive._is_payment_information_required

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_payment_information_required {

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 497.

```text
harge_type = 7;
  }
  oneof _discount_recurring_limit {
  int32 discount_recurring_limit = 8;
  }
  oneof _is_payment_information_required {
  bool is_payment_information_required = 10;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 12;
  }
  oneof _starts_at {
  .google.protobuf.Timestamp starts_at = 13;
  }
  oneof _product {
  string product = 14;
  }
  oneof _code {
  string code = 15;
  }
  
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06783"></a>
## FND-06783: chesscom.payments.v1.Incentive.is_payment_information_required = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_payment_information_required = 10;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 540.

```text
ring_limit {
  int32 discount_recurring_limit = 8;
  }
  oneof _is_payment_information_required {
  bool is_payment_information_required = 10;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 12;
  }
  oneof _starts_at {
  .google.protobuf.Timestamp starts_at = 13;
  }
  oneof _product {
  string product = 14;
  }
  oneof _code {
  string code = 15;
  }
  oneof _campaign_id {
  string campaign_id =
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06784"></a>
## FND-06784: oneof declaration: chesscom.payments.v1.Incentive._expires_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _expires_at {

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 589.

```text
;
  }
  oneof _is_payment_information_required {
  bool is_payment_information_required = 10;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 12;
  }
  oneof _starts_at {
  .google.protobuf.Timestamp starts_at = 13;
  }
  oneof _product {
  string product = 14;
  }
  oneof _code {
  string code = 15;
  }
  oneof _campaign_id {
  string campaign_id = 16;
  }
  oneof _template {
  .chesscom.payments
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06785"></a>
## FND-06785: chesscom.payments.v1.Incentive.expires_at = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp expires_at = 12;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 611.

```text
ent_information_required {
  bool is_payment_information_required = 10;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 12;
  }
  oneof _starts_at {
  .google.protobuf.Timestamp starts_at = 13;
  }
  oneof _product {
  string product = 14;
  }
  oneof _code {
  string code = 15;
  }
  oneof _campaign_id {
  string campaign_id = 16;
  }
  oneof _template {
  .chesscom.payments.v1.IncentiveTemplate 
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06786"></a>
## FND-06786: oneof declaration: chesscom.payments.v1.Incentive._starts_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _starts_at {

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 661.

```text
mation_required = 10;
  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 12;
  }
  oneof _starts_at {
  .google.protobuf.Timestamp starts_at = 13;
  }
  oneof _product {
  string product = 14;
  }
  oneof _code {
  string code = 15;
  }
  oneof _campaign_id {
  string campaign_id = 16;
  }
  oneof _template {
  .chesscom.payments.v1.IncentiveTemplate template = 17;
  }
  oneof _app_store_subscription
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06787"></a>
## FND-06787: chesscom.payments.v1.Incentive.starts_at = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp starts_at = 13;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 682.

```text

  }
  oneof _expires_at {
  .google.protobuf.Timestamp expires_at = 12;
  }
  oneof _starts_at {
  .google.protobuf.Timestamp starts_at = 13;
  }
  oneof _product {
  string product = 14;
  }
  oneof _code {
  string code = 15;
  }
  oneof _campaign_id {
  string campaign_id = 16;
  }
  oneof _template {
  .chesscom.payments.v1.IncentiveTemplate template = 17;
  }
  oneof _app_store_subscription_group_id {
  string 
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06788"></a>
## FND-06788: oneof declaration: chesscom.payments.v1.Incentive._product

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _product {

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 731.

```text
estamp expires_at = 12;
  }
  oneof _starts_at {
  .google.protobuf.Timestamp starts_at = 13;
  }
  oneof _product {
  string product = 14;
  }
  oneof _code {
  string code = 15;
  }
  oneof _campaign_id {
  string campaign_id = 16;
  }
  oneof _template {
  .chesscom.payments.v1.IncentiveTemplate template = 17;
  }
  oneof _app_store_subscription_group_id {
  string app_store_subscription_group_id = 18;
  }
  optio
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06789"></a>
## FND-06789: chesscom.payments.v1.Incentive.product = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string product = 14;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 750.

```text
 12;
  }
  oneof _starts_at {
  .google.protobuf.Timestamp starts_at = 13;
  }
  oneof _product {
  string product = 14;
  }
  oneof _code {
  string code = 15;
  }
  oneof _campaign_id {
  string campaign_id = 16;
  }
  oneof _template {
  .chesscom.payments.v1.IncentiveTemplate template = 17;
  }
  oneof _app_store_subscription_group_id {
  string app_store_subscription_group_id = 18;
  }
  optional string id = 1;

```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06790"></a>
## FND-06790: oneof declaration: chesscom.payments.v1.Incentive._code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _code {

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 777.

```text
 {
  .google.protobuf.Timestamp starts_at = 13;
  }
  oneof _product {
  string product = 14;
  }
  oneof _code {
  string code = 15;
  }
  oneof _campaign_id {
  string campaign_id = 16;
  }
  oneof _template {
  .chesscom.payments.v1.IncentiveTemplate template = 17;
  }
  oneof _app_store_subscription_group_id {
  string app_store_subscription_group_id = 18;
  }
  optional string id = 1;
  optional string name = 2;
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06791"></a>
## FND-06791: chesscom.payments.v1.Incentive.code = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string code = 15;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 793.

```text
tobuf.Timestamp starts_at = 13;
  }
  oneof _product {
  string product = 14;
  }
  oneof _code {
  string code = 15;
  }
  oneof _campaign_id {
  string campaign_id = 16;
  }
  oneof _template {
  .chesscom.payments.v1.IncentiveTemplate template = 17;
  }
  oneof _app_store_subscription_group_id {
  string app_store_subscription_group_id = 18;
  }
  optional string id = 1;
  optional string name = 2;
  optional .che
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06792"></a>
## FND-06792: oneof declaration: chesscom.payments.v1.Incentive._campaign_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _campaign_id {

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 817.

```text
t = 13;
  }
  oneof _product {
  string product = 14;
  }
  oneof _code {
  string code = 15;
  }
  oneof _campaign_id {
  string campaign_id = 16;
  }
  oneof _template {
  .chesscom.payments.v1.IncentiveTemplate template = 17;
  }
  oneof _app_store_subscription_group_id {
  string app_store_subscription_group_id = 18;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.payments.v1.Incent
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06793"></a>
## FND-06793: chesscom.payments.v1.Incentive.campaign_id = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string campaign_id = 16;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 840.

```text
oduct {
  string product = 14;
  }
  oneof _code {
  string code = 15;
  }
  oneof _campaign_id {
  string campaign_id = 16;
  }
  oneof _template {
  .chesscom.payments.v1.IncentiveTemplate template = 17;
  }
  oneof _app_store_subscription_group_id {
  string app_store_subscription_group_id = 18;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.payments.v1.IncentiveType type = 3;
  rep
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06794"></a>
## FND-06794: oneof declaration: chesscom.payments.v1.Incentive._template

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _template {

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 871.

```text
  }
  oneof _code {
  string code = 15;
  }
  oneof _campaign_id {
  string campaign_id = 16;
  }
  oneof _template {
  .chesscom.payments.v1.IncentiveTemplate template = 17;
  }
  oneof _app_store_subscription_group_id {
  string app_store_subscription_group_id = 18;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.payments.v1.IncentiveType type = 3;
  repeated .chesscom.payments.v1.Inc
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06795"></a>
## FND-06795: chesscom.payments.v1.Incentive.template = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.IncentiveTemplate template = 17;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 891.

```text
  string code = 15;
  }
  oneof _campaign_id {
  string campaign_id = 16;
  }
  oneof _template {
  .chesscom.payments.v1.IncentiveTemplate template = 17;
  }
  oneof _app_store_subscription_group_id {
  string app_store_subscription_group_id = 18;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.payments.v1.IncentiveType type = 3;
  repeated .chesscom.payments.v1.IncentiveOffer incentiv
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06796"></a>
## FND-06796: oneof declaration: chesscom.payments.v1.Incentive._app_store_subscription_group_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _app_store_subscription_group_id {

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 952.

```text
ign_id = 16;
  }
  oneof _template {
  .chesscom.payments.v1.IncentiveTemplate template = 17;
  }
  oneof _app_store_subscription_group_id {
  string app_store_subscription_group_id = 18;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.payments.v1.IncentiveType type = 3;
  repeated .chesscom.payments.v1.IncentiveOffer incentive_offers = 9;
  repeated .chesscom.payments.v1.IncentiveExter
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06797"></a>
## FND-06797: chesscom.payments.v1.Incentive.app_store_subscription_group_id = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string app_store_subscription_group_id = 18;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 995.

```text
sscom.payments.v1.IncentiveTemplate template = 17;
  }
  oneof _app_store_subscription_group_id {
  string app_store_subscription_group_id = 18;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.payments.v1.IncentiveType type = 3;
  repeated .chesscom.payments.v1.IncentiveOffer incentive_offers = 9;
  repeated .chesscom.payments.v1.IncentiveExternalAssociation incentive_external_associati
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06798"></a>
## FND-06798: chesscom.payments.v1.Incentive.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 1046.

```text
  }
  oneof _app_store_subscription_group_id {
  string app_store_subscription_group_id = 18;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.payments.v1.IncentiveType type = 3;
  repeated .chesscom.payments.v1.IncentiveOffer incentive_offers = 9;
  repeated .chesscom.payments.v1.IncentiveExternalAssociation incentive_external_associations = 11;
}

```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06799"></a>
## FND-06799: chesscom.payments.v1.Incentive.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 1072.

```text
scription_group_id {
  string app_store_subscription_group_id = 18;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.payments.v1.IncentiveType type = 3;
  repeated .chesscom.payments.v1.IncentiveOffer incentive_offers = 9;
  repeated .chesscom.payments.v1.IncentiveExternalAssociation incentive_external_associations = 11;
}

```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06800"></a>
## FND-06800: chesscom.payments.v1.Incentive.type = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.IncentiveType type = 3;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 1100.

```text
g app_store_subscription_group_id = 18;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.payments.v1.IncentiveType type = 3;
  repeated .chesscom.payments.v1.IncentiveOffer incentive_offers = 9;
  repeated .chesscom.payments.v1.IncentiveExternalAssociation incentive_external_associations = 11;
}

```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06801"></a>
## FND-06801: chesscom.payments.v1.Incentive.incentive_offers = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.IncentiveOffer incentive_offers = 9;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 1157.

```text
ring id = 1;
  optional string name = 2;
  optional .chesscom.payments.v1.IncentiveType type = 3;
  repeated .chesscom.payments.v1.IncentiveOffer incentive_offers = 9;
  repeated .chesscom.payments.v1.IncentiveExternalAssociation incentive_external_associations = 11;
}

```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06802"></a>
## FND-06802: chesscom.payments.v1.Incentive.incentive_external_associations = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.IncentiveExternalAssociation incentive_external_associations = 11;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 1227.

```text
.v1.IncentiveType type = 3;
  repeated .chesscom.payments.v1.IncentiveOffer incentive_offers = 9;
  repeated .chesscom.payments.v1.IncentiveExternalAssociation incentive_external_associations = 11;
}

```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06803"></a>
## FND-06803: message declaration: chesscom.payments.v1.IncentiveExternalAssociation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message IncentiveExternalAssociation {

### Evidence

- **SRC-0496** `research/proto/chesscom/payments/v1/incentive_external_association.proto` — [preserved redacted evidence](../evidence/text/a6a9967dad9bd78f388ee04f50b2583936750f88c44be98d41d7ad73b309e9bc.proto)
  Character offset 119.

```text
/payments/v1/incentive_external_association.proto
// syntax: proto3

package chesscom.payments.v1;

message IncentiveExternalAssociation {
  optional int32 id = 1;
  optional string incentive_id = 2;
  optional string identifier = 3;
  optional .chesscom.api.v1.Platform platform = 4;
}

```

**Source references:** SRC-0496, SRC-1467  
**URL references:** None independently associated  
**Related findings:** FND-06804, FND-06805

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06804"></a>
## FND-06804: chesscom.payments.v1.IncentiveExternalAssociation.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 id = 1;

### Evidence

- **SRC-0496** `research/proto/chesscom/payments/v1/incentive_external_association.proto` — [preserved redacted evidence](../evidence/text/a6a9967dad9bd78f388ee04f50b2583936750f88c44be98d41d7ad73b309e9bc.proto)
  Character offset 160.

```text
on.proto
// syntax: proto3

package chesscom.payments.v1;

message IncentiveExternalAssociation {
  optional int32 id = 1;
  optional string incentive_id = 2;
  optional string identifier = 3;
  optional .chesscom.api.v1.Platform platform = 4;
}

```

**Source references:** SRC-0496, SRC-1467  
**URL references:** None independently associated  
**Related findings:** FND-06803, FND-06805

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06805"></a>
## FND-06805: chesscom.payments.v1.IncentiveExternalAssociation.incentive_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string incentive_id = 2;

### Evidence

- **SRC-0496** `research/proto/chesscom/payments/v1/incentive_external_association.proto` — [preserved redacted evidence](../evidence/text/a6a9967dad9bd78f388ee04f50b2583936750f88c44be98d41d7ad73b309e9bc.proto)
  Character offset 185.

```text
3

package chesscom.payments.v1;

message IncentiveExternalAssociation {
  optional int32 id = 1;
  optional string incentive_id = 2;
  optional string identifier = 3;
  optional .chesscom.api.v1.Platform platform = 4;
}

```

**Source references:** SRC-0496, SRC-1467  
**URL references:** None independently associated  
**Related findings:** FND-06803, FND-06804

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06806"></a>
## FND-06806: chesscom.payments.v1.IncentiveExternalAssociation.identifier = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string identifier = 3;

### Evidence

- **SRC-0496** `research/proto/chesscom/payments/v1/incentive_external_association.proto` — [preserved redacted evidence](../evidence/text/a6a9967dad9bd78f388ee04f50b2583936750f88c44be98d41d7ad73b309e9bc.proto)
  Character offset 221.

```text
ssage IncentiveExternalAssociation {
  optional int32 id = 1;
  optional string incentive_id = 2;
  optional string identifier = 3;
  optional .chesscom.api.v1.Platform platform = 4;
}

```

**Source references:** SRC-0496, SRC-1467  
**URL references:** None independently associated  
**Related findings:** FND-06803, FND-06804, FND-06805

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06807"></a>
## FND-06807: chesscom.payments.v1.IncentiveExternalAssociation.platform = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Platform platform = 4;

### Evidence

- **SRC-0496** `research/proto/chesscom/payments/v1/incentive_external_association.proto` — [preserved redacted evidence](../evidence/text/a6a9967dad9bd78f388ee04f50b2583936750f88c44be98d41d7ad73b309e9bc.proto)
  Character offset 255.

```text
 {
  optional int32 id = 1;
  optional string incentive_id = 2;
  optional string identifier = 3;
  optional .chesscom.api.v1.Platform platform = 4;
}

```

**Source references:** SRC-0496, SRC-1467  
**URL references:** None independently associated  
**Related findings:** FND-06803, FND-06804, FND-06805

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06808"></a>
## FND-06808: message declaration: chesscom.payments.v1.IncentiveOffer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message IncentiveOffer {

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 104.

```text
ource: chesscom/payments/v1/incentive_offer.proto
// syntax: proto3

package chesscom.payments.v1;

message IncentiveOffer {
  oneof _description {
  string description = 3;
  }
  oneof _period_end {
  int32 period_end = 7;
  }
  oneof _duration {
  int32 duration = 8;
  }
  oneof _duration_unit {
  .chesscom.payments.v1.SubscriptionDurationUnit duration_unit = 9;
  }
  optional string id = 1;
  optional string incen
```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06809, FND-06810

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06809"></a>
## FND-06809: oneof declaration: chesscom.payments.v1.IncentiveOffer._description

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _description {

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 131.

```text
/incentive_offer.proto
// syntax: proto3

package chesscom.payments.v1;

message IncentiveOffer {
  oneof _description {
  string description = 3;
  }
  oneof _period_end {
  int32 period_end = 7;
  }
  oneof _duration {
  int32 duration = 8;
  }
  oneof _duration_unit {
  .chesscom.payments.v1.SubscriptionDurationUnit duration_unit = 9;
  }
  optional string id = 1;
  optional string incentive_id = 2;
  optional .ch
```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06810

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06810"></a>
## FND-06810: chesscom.payments.v1.IncentiveOffer.description = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string description = 3;

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 154.

```text
// syntax: proto3

package chesscom.payments.v1;

message IncentiveOffer {
  oneof _description {
  string description = 3;
  }
  oneof _period_end {
  int32 period_end = 7;
  }
  oneof _duration {
  int32 duration = 8;
  }
  oneof _duration_unit {
  .chesscom.payments.v1.SubscriptionDurationUnit duration_unit = 9;
  }
  optional string id = 1;
  optional string incentive_id = 2;
  optional .chesscom.payments.v1.Ince
```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06811"></a>
## FND-06811: oneof declaration: chesscom.payments.v1.IncentiveOffer._period_end

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _period_end {

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 184.

```text
sscom.payments.v1;

message IncentiveOffer {
  oneof _description {
  string description = 3;
  }
  oneof _period_end {
  int32 period_end = 7;
  }
  oneof _duration {
  int32 duration = 8;
  }
  oneof _duration_unit {
  .chesscom.payments.v1.SubscriptionDurationUnit duration_unit = 9;
  }
  optional string id = 1;
  optional string incentive_id = 2;
  optional .chesscom.payments.v1.IncentiveOfferType type = 4;
  opt
```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06812"></a>
## FND-06812: chesscom.payments.v1.IncentiveOffer.period_end = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 period_end = 7;

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 206.

```text
ssage IncentiveOffer {
  oneof _description {
  string description = 3;
  }
  oneof _period_end {
  int32 period_end = 7;
  }
  oneof _duration {
  int32 duration = 8;
  }
  oneof _duration_unit {
  .chesscom.payments.v1.SubscriptionDurationUnit duration_unit = 9;
  }
  optional string id = 1;
  optional string incentive_id = 2;
  optional .chesscom.payments.v1.IncentiveOfferType type = 4;
  optional float value = 5;
```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06813"></a>
## FND-06813: oneof declaration: chesscom.payments.v1.IncentiveOffer._duration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _duration {

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 234.

```text
of _description {
  string description = 3;
  }
  oneof _period_end {
  int32 period_end = 7;
  }
  oneof _duration {
  int32 duration = 8;
  }
  oneof _duration_unit {
  .chesscom.payments.v1.SubscriptionDurationUnit duration_unit = 9;
  }
  optional string id = 1;
  optional string incentive_id = 2;
  optional .chesscom.payments.v1.IncentiveOfferType type = 4;
  optional float value = 5;
  optional int32 period_sta
```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06814"></a>
## FND-06814: chesscom.payments.v1.IncentiveOffer.duration = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 duration = 8;

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 254.

```text
string description = 3;
  }
  oneof _period_end {
  int32 period_end = 7;
  }
  oneof _duration {
  int32 duration = 8;
  }
  oneof _duration_unit {
  .chesscom.payments.v1.SubscriptionDurationUnit duration_unit = 9;
  }
  optional string id = 1;
  optional string incentive_id = 2;
  optional .chesscom.payments.v1.IncentiveOfferType type = 4;
  optional float value = 5;
  optional int32 period_start = 6;
  repeated .
```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06815"></a>
## FND-06815: oneof declaration: chesscom.payments.v1.IncentiveOffer._duration_unit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _duration_unit {

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 280.

```text
}
  oneof _period_end {
  int32 period_end = 7;
  }
  oneof _duration {
  int32 duration = 8;
  }
  oneof _duration_unit {
  .chesscom.payments.v1.SubscriptionDurationUnit duration_unit = 9;
  }
  optional string id = 1;
  optional string incentive_id = 2;
  optional .chesscom.payments.v1.IncentiveOfferType type = 4;
  optional float value = 5;
  optional int32 period_start = 6;
  repeated .chesscom.payments.v1.Incen
```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06816"></a>
## FND-06816: chesscom.payments.v1.IncentiveOffer.duration_unit = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.SubscriptionDurationUnit duration_unit = 9;

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 305.

```text
 int32 period_end = 7;
  }
  oneof _duration {
  int32 duration = 8;
  }
  oneof _duration_unit {
  .chesscom.payments.v1.SubscriptionDurationUnit duration_unit = 9;
  }
  optional string id = 1;
  optional string incentive_id = 2;
  optional .chesscom.payments.v1.IncentiveOfferType type = 4;
  optional float value = 5;
  optional int32 period_start = 6;
  repeated .chesscom.payments.v1.IncentiveOfferPrice prices = 1
```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06817"></a>
## FND-06817: chesscom.payments.v1.IncentiveOffer.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 377.

```text

  oneof _duration_unit {
  .chesscom.payments.v1.SubscriptionDurationUnit duration_unit = 9;
  }
  optional string id = 1;
  optional string incentive_id = 2;
  optional .chesscom.payments.v1.IncentiveOfferType type = 4;
  optional float value = 5;
  optional int32 period_start = 6;
  repeated .chesscom.payments.v1.IncentiveOfferPrice prices = 10;
}

message IncentiveOfferPrice {
  oneof _country {
  .chesscom.api.v
```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06818"></a>
## FND-06818: chesscom.payments.v1.IncentiveOffer.incentive_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string incentive_id = 2;

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 403.

```text
  .chesscom.payments.v1.SubscriptionDurationUnit duration_unit = 9;
  }
  optional string id = 1;
  optional string incentive_id = 2;
  optional .chesscom.payments.v1.IncentiveOfferType type = 4;
  optional float value = 5;
  optional int32 period_start = 6;
  repeated .chesscom.payments.v1.IncentiveOfferPrice prices = 10;
}

message IncentiveOfferPrice {
  oneof _country {
  .chesscom.api.v1.Country country = 2;
  }
```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06819"></a>
## FND-06819: chesscom.payments.v1.IncentiveOffer.type = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.IncentiveOfferType type = 4;

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 439.

```text
DurationUnit duration_unit = 9;
  }
  optional string id = 1;
  optional string incentive_id = 2;
  optional .chesscom.payments.v1.IncentiveOfferType type = 4;
  optional float value = 5;
  optional int32 period_start = 6;
  repeated .chesscom.payments.v1.IncentiveOfferPrice prices = 10;
}

message IncentiveOfferPrice {
  oneof _country {
  .chesscom.api.v1.Country country = 2;
  }
  optional .chesscom.api.v1.Money p
```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06820"></a>
## FND-06820: chesscom.payments.v1.IncentiveOffer.value = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float value = 5;

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 501.

```text
  optional string incentive_id = 2;
  optional .chesscom.payments.v1.IncentiveOfferType type = 4;
  optional float value = 5;
  optional int32 period_start = 6;
  repeated .chesscom.payments.v1.IncentiveOfferPrice prices = 10;
}

message IncentiveOfferPrice {
  oneof _country {
  .chesscom.api.v1.Country country = 2;
  }
  optional .chesscom.api.v1.Money price = 1;
}

```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06821"></a>
## FND-06821: chesscom.payments.v1.IncentiveOffer.period_start = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 period_start = 6;

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 529.

```text
id = 2;
  optional .chesscom.payments.v1.IncentiveOfferType type = 4;
  optional float value = 5;
  optional int32 period_start = 6;
  repeated .chesscom.payments.v1.IncentiveOfferPrice prices = 10;
}

message IncentiveOfferPrice {
  oneof _country {
  .chesscom.api.v1.Country country = 2;
  }
  optional .chesscom.api.v1.Money price = 1;
}

```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06822"></a>
## FND-06822: chesscom.payments.v1.IncentiveOffer.prices = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.IncentiveOfferPrice prices = 10;

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 564.

```text
ts.v1.IncentiveOfferType type = 4;
  optional float value = 5;
  optional int32 period_start = 6;
  repeated .chesscom.payments.v1.IncentiveOfferPrice prices = 10;
}

message IncentiveOfferPrice {
  oneof _country {
  .chesscom.api.v1.Country country = 2;
  }
  optional .chesscom.api.v1.Money price = 1;
}

```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06823"></a>
## FND-06823: message declaration: chesscom.payments.v1.IncentiveOfferPrice

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message IncentiveOfferPrice {

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 631.

```text
tional int32 period_start = 6;
  repeated .chesscom.payments.v1.IncentiveOfferPrice prices = 10;
}

message IncentiveOfferPrice {
  oneof _country {
  .chesscom.api.v1.Country country = 2;
  }
  optional .chesscom.api.v1.Money price = 1;
}

```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06824"></a>
## FND-06824: oneof declaration: chesscom.payments.v1.IncentiveOfferPrice._country

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _country {

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 663.

```text
 repeated .chesscom.payments.v1.IncentiveOfferPrice prices = 10;
}

message IncentiveOfferPrice {
  oneof _country {
  .chesscom.api.v1.Country country = 2;
  }
  optional .chesscom.api.v1.Money price = 1;
}

```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06825"></a>
## FND-06825: chesscom.payments.v1.IncentiveOfferPrice.country = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.Country country = 2;

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 682.

```text
.payments.v1.IncentiveOfferPrice prices = 10;
}

message IncentiveOfferPrice {
  oneof _country {
  .chesscom.api.v1.Country country = 2;
  }
  optional .chesscom.api.v1.Money price = 1;
}

```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06826"></a>
## FND-06826: chesscom.payments.v1.IncentiveOfferPrice.price = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money price = 1;

### Evidence

- **SRC-0497** `research/proto/chesscom/payments/v1/incentive_offer.proto` — [preserved redacted evidence](../evidence/text/4adc93d9e561390f6a8ea2b699d49874be3eabb797137cde26f1bbb6d44afe7f.proto)
  Character offset 726.

```text
;
}

message IncentiveOfferPrice {
  oneof _country {
  .chesscom.api.v1.Country country = 2;
  }
  optional .chesscom.api.v1.Money price = 1;
}

```

**Source references:** SRC-0497, SRC-1468  
**URL references:** None independently associated  
**Related findings:** FND-06808, FND-06809, FND-06810

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06827"></a>
## FND-06827: message declaration: chesscom.payments.v1.InvoiceBillTo

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InvoiceBillTo {

### Evidence

- **SRC-0498** `research/proto/chesscom/payments/v1/invoice_bill_to.proto` — [preserved redacted evidence](../evidence/text/3afad4105323292b9a339ee3ab7efa0d9b1036fab0a1a36b3275ef193d224e38.proto)
  Character offset 104.

```text
ource: chesscom/payments/v1/invoice_bill_to.proto
// syntax: proto3

package chesscom.payments.v1;

message InvoiceBillTo {
  optional string name = 1;
  repeated string address_lines = 2;
  optional string country_code = 3;
  optional string tax_id = 4;
}

```

**Source references:** SRC-0498, SRC-1469  
**URL references:** None independently associated  
**Related findings:** FND-06828, FND-06829

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06828"></a>
## FND-06828: chesscom.payments.v1.InvoiceBillTo.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0498** `research/proto/chesscom/payments/v1/invoice_bill_to.proto` — [preserved redacted evidence](../evidence/text/3afad4105323292b9a339ee3ab7efa0d9b1036fab0a1a36b3275ef193d224e38.proto)
  Character offset 130.

```text
1/invoice_bill_to.proto
// syntax: proto3

package chesscom.payments.v1;

message InvoiceBillTo {
  optional string name = 1;
  repeated string address_lines = 2;
  optional string country_code = 3;
  optional string tax_id = 4;
}

```

**Source references:** SRC-0498, SRC-1469  
**URL references:** None independently associated  
**Related findings:** FND-06827, FND-06829

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06829"></a>
## FND-06829: chesscom.payments.v1.InvoiceBillTo.address_lines = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string address_lines = 2;

### Evidence

- **SRC-0498** `research/proto/chesscom/payments/v1/invoice_bill_to.proto` — [preserved redacted evidence](../evidence/text/3afad4105323292b9a339ee3ab7efa0d9b1036fab0a1a36b3275ef193d224e38.proto)
  Character offset 158.

```text
yntax: proto3

package chesscom.payments.v1;

message InvoiceBillTo {
  optional string name = 1;
  repeated string address_lines = 2;
  optional string country_code = 3;
  optional string tax_id = 4;
}

```

**Source references:** SRC-0498, SRC-1469  
**URL references:** None independently associated  
**Related findings:** FND-06827, FND-06828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06830"></a>
## FND-06830: chesscom.payments.v1.InvoiceBillTo.country_code = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string country_code = 3;

### Evidence

- **SRC-0498** `research/proto/chesscom/payments/v1/invoice_bill_to.proto` — [preserved redacted evidence](../evidence/text/3afad4105323292b9a339ee3ab7efa0d9b1036fab0a1a36b3275ef193d224e38.proto)
  Character offset 195.

```text
nts.v1;

message InvoiceBillTo {
  optional string name = 1;
  repeated string address_lines = 2;
  optional string country_code = 3;
  optional string tax_id = 4;
}

```

**Source references:** SRC-0498, SRC-1469  
**URL references:** None independently associated  
**Related findings:** FND-06827, FND-06828, FND-06829

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06831"></a>
## FND-06831: chesscom.payments.v1.InvoiceBillTo.tax_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string tax_id = 4;

### Evidence

- **SRC-0498** `research/proto/chesscom/payments/v1/invoice_bill_to.proto` — [preserved redacted evidence](../evidence/text/3afad4105323292b9a339ee3ab7efa0d9b1036fab0a1a36b3275ef193d224e38.proto)
  Character offset 231.

```text
ptional string name = 1;
  repeated string address_lines = 2;
  optional string country_code = 3;
  optional string tax_id = 4;
}

```

**Source references:** SRC-0498, SRC-1469  
**URL references:** None independently associated  
**Related findings:** FND-06827, FND-06828, FND-06829

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06832"></a>
## FND-06832: message declaration: chesscom.payments.v1.MemberPromotion

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MemberPromotion {

### Evidence

- **SRC-0499** `research/proto/chesscom/payments/v1/member_promotion.proto` — [preserved redacted evidence](../evidence/text/cbd659564e0a0380e1244d6197618e9dab74b5a2c650eab126b8a93de990fafd.proto)
  Character offset 105.

```text
urce: chesscom/payments/v1/member_promotion.proto
// syntax: proto3

package chesscom.payments.v1;

message MemberPromotion {
  optional string name = 1;
  optional .chesscom.payments.v1.IncentiveType type = 2;
  optional float discount_percent = 3;
  optional int32 free_time_days = 4;
  optional .google.protobuf.Timestamp ends_at = 5;
  repeated .chesscom.api.v1.Platform redeemable_platforms = 6;
}

message Promotio
```

**Source references:** SRC-0499, SRC-1470  
**URL references:** None independently associated  
**Related findings:** FND-06833, FND-06834

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06833"></a>
## FND-06833: chesscom.payments.v1.MemberPromotion.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0499** `research/proto/chesscom/payments/v1/member_promotion.proto` — [preserved redacted evidence](../evidence/text/cbd659564e0a0380e1244d6197618e9dab74b5a2c650eab126b8a93de990fafd.proto)
  Character offset 133.

```text
ember_promotion.proto
// syntax: proto3

package chesscom.payments.v1;

message MemberPromotion {
  optional string name = 1;
  optional .chesscom.payments.v1.IncentiveType type = 2;
  optional float discount_percent = 3;
  optional int32 free_time_days = 4;
  optional .google.protobuf.Timestamp ends_at = 5;
  repeated .chesscom.api.v1.Platform redeemable_platforms = 6;
}

message PromotionOnCharge {
  optional strin
```

**Source references:** SRC-0499, SRC-1470  
**URL references:** None independently associated  
**Related findings:** FND-06832, FND-06834

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06834"></a>
## FND-06834: chesscom.payments.v1.MemberPromotion.type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.IncentiveType type = 2;

### Evidence

- **SRC-0499** `research/proto/chesscom/payments/v1/member_promotion.proto` — [preserved redacted evidence](../evidence/text/cbd659564e0a0380e1244d6197618e9dab74b5a2c650eab126b8a93de990fafd.proto)
  Character offset 161.

```text
tax: proto3

package chesscom.payments.v1;

message MemberPromotion {
  optional string name = 1;
  optional .chesscom.payments.v1.IncentiveType type = 2;
  optional float discount_percent = 3;
  optional int32 free_time_days = 4;
  optional .google.protobuf.Timestamp ends_at = 5;
  repeated .chesscom.api.v1.Platform redeemable_platforms = 6;
}

message PromotionOnCharge {
  optional string charge_id = 1;
  optional 
```

**Source references:** SRC-0499, SRC-1470  
**URL references:** None independently associated  
**Related findings:** FND-06832, FND-06833

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06835"></a>
## FND-06835: chesscom.payments.v1.MemberPromotion.discount_percent = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float discount_percent = 3;

### Evidence

- **SRC-0499** `research/proto/chesscom/payments/v1/member_promotion.proto` — [preserved redacted evidence](../evidence/text/cbd659564e0a0380e1244d6197618e9dab74b5a2c650eab126b8a93de990fafd.proto)
  Character offset 218.

```text
rPromotion {
  optional string name = 1;
  optional .chesscom.payments.v1.IncentiveType type = 2;
  optional float discount_percent = 3;
  optional int32 free_time_days = 4;
  optional .google.protobuf.Timestamp ends_at = 5;
  repeated .chesscom.api.v1.Platform redeemable_platforms = 6;
}

message PromotionOnCharge {
  optional string charge_id = 1;
  optional .google.protobuf.Timestamp charged_at = 2;
  optional .ch
```

**Source references:** SRC-0499, SRC-1470  
**URL references:** None independently associated  
**Related findings:** FND-06832, FND-06833, FND-06834

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06836"></a>
## FND-06836: chesscom.payments.v1.MemberPromotion.free_time_days = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 free_time_days = 4;

### Evidence

- **SRC-0499** `research/proto/chesscom/payments/v1/member_promotion.proto` — [preserved redacted evidence](../evidence/text/cbd659564e0a0380e1244d6197618e9dab74b5a2c650eab126b8a93de990fafd.proto)
  Character offset 257.

```text
;
  optional .chesscom.payments.v1.IncentiveType type = 2;
  optional float discount_percent = 3;
  optional int32 free_time_days = 4;
  optional .google.protobuf.Timestamp ends_at = 5;
  repeated .chesscom.api.v1.Platform redeemable_platforms = 6;
}

message PromotionOnCharge {
  optional string charge_id = 1;
  optional .google.protobuf.Timestamp charged_at = 2;
  optional .chesscom.payments.v1.MemberPromotion prom
```

**Source references:** SRC-0499, SRC-1470  
**URL references:** None independently associated  
**Related findings:** FND-06832, FND-06833, FND-06834

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06837"></a>
## FND-06837: chesscom.payments.v1.MemberPromotion.ends_at = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp ends_at = 5;

### Evidence

- **SRC-0499** `research/proto/chesscom/payments/v1/member_promotion.proto` — [preserved redacted evidence](../evidence/text/cbd659564e0a0380e1244d6197618e9dab74b5a2c650eab126b8a93de990fafd.proto)
  Character offset 294.

```text
centiveType type = 2;
  optional float discount_percent = 3;
  optional int32 free_time_days = 4;
  optional .google.protobuf.Timestamp ends_at = 5;
  repeated .chesscom.api.v1.Platform redeemable_platforms = 6;
}

message PromotionOnCharge {
  optional string charge_id = 1;
  optional .google.protobuf.Timestamp charged_at = 2;
  optional .chesscom.payments.v1.MemberPromotion promotion = 3;
  optional bool coupon_cod
```

**Source references:** SRC-0499, SRC-1470  
**URL references:** None independently associated  
**Related findings:** FND-06832, FND-06833, FND-06834

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06838"></a>
## FND-06838: chesscom.payments.v1.MemberPromotion.redeemable_platforms = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.api.v1.Platform redeemable_platforms = 6;

### Evidence

- **SRC-0499** `research/proto/chesscom/payments/v1/member_promotion.proto` — [preserved redacted evidence](../evidence/text/cbd659564e0a0380e1244d6197618e9dab74b5a2c650eab126b8a93de990fafd.proto)
  Character offset 345.

```text
cent = 3;
  optional int32 free_time_days = 4;
  optional .google.protobuf.Timestamp ends_at = 5;
  repeated .chesscom.api.v1.Platform redeemable_platforms = 6;
}

message PromotionOnCharge {
  optional string charge_id = 1;
  optional .google.protobuf.Timestamp charged_at = 2;
  optional .chesscom.payments.v1.MemberPromotion promotion = 3;
  optional bool coupon_code_used = 4;
  optional .chesscom.api.v1.Platform pl
```

**Source references:** SRC-0499, SRC-1470  
**URL references:** None independently associated  
**Related findings:** FND-06832, FND-06833, FND-06834

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06839"></a>
## FND-06839: message declaration: chesscom.payments.v1.PromotionOnCharge

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PromotionOnCharge {

### Evidence

- **SRC-0499** `research/proto/chesscom/payments/v1/member_promotion.proto` — [preserved redacted evidence](../evidence/text/cbd659564e0a0380e1244d6197618e9dab74b5a2c650eab126b8a93de990fafd.proto)
  Character offset 409.

```text
e.protobuf.Timestamp ends_at = 5;
  repeated .chesscom.api.v1.Platform redeemable_platforms = 6;
}

message PromotionOnCharge {
  optional string charge_id = 1;
  optional .google.protobuf.Timestamp charged_at = 2;
  optional .chesscom.payments.v1.MemberPromotion promotion = 3;
  optional bool coupon_code_used = 4;
  optional .chesscom.api.v1.Platform platform = 5;
}

```

**Source references:** SRC-0499, SRC-1470  
**URL references:** None independently associated  
**Related findings:** FND-06832, FND-06833, FND-06834

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06840"></a>
## FND-06840: chesscom.payments.v1.PromotionOnCharge.charge_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string charge_id = 1;

### Evidence

- **SRC-0499** `research/proto/chesscom/payments/v1/member_promotion.proto` — [preserved redacted evidence](../evidence/text/cbd659564e0a0380e1244d6197618e9dab74b5a2c650eab126b8a93de990fafd.proto)
  Character offset 439.

```text
 5;
  repeated .chesscom.api.v1.Platform redeemable_platforms = 6;
}

message PromotionOnCharge {
  optional string charge_id = 1;
  optional .google.protobuf.Timestamp charged_at = 2;
  optional .chesscom.payments.v1.MemberPromotion promotion = 3;
  optional bool coupon_code_used = 4;
  optional .chesscom.api.v1.Platform platform = 5;
}

```

**Source references:** SRC-0499, SRC-1470  
**URL references:** None independently associated  
**Related findings:** FND-06832, FND-06833, FND-06834

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06841"></a>
## FND-06841: chesscom.payments.v1.PromotionOnCharge.charged_at = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp charged_at = 2;

### Evidence

- **SRC-0499** `research/proto/chesscom/payments/v1/member_promotion.proto` — [preserved redacted evidence](../evidence/text/cbd659564e0a0380e1244d6197618e9dab74b5a2c650eab126b8a93de990fafd.proto)
  Character offset 472.

```text
latform redeemable_platforms = 6;
}

message PromotionOnCharge {
  optional string charge_id = 1;
  optional .google.protobuf.Timestamp charged_at = 2;
  optional .chesscom.payments.v1.MemberPromotion promotion = 3;
  optional bool coupon_code_used = 4;
  optional .chesscom.api.v1.Platform platform = 5;
}

```

**Source references:** SRC-0499, SRC-1470  
**URL references:** None independently associated  
**Related findings:** FND-06832, FND-06833, FND-06834

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06842"></a>
## FND-06842: chesscom.payments.v1.PromotionOnCharge.promotion = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.MemberPromotion promotion = 3;

### Evidence

- **SRC-0499** `research/proto/chesscom/payments/v1/member_promotion.proto` — [preserved redacted evidence](../evidence/text/cbd659564e0a0380e1244d6197618e9dab74b5a2c650eab126b8a93de990fafd.proto)
  Character offset 526.

```text
OnCharge {
  optional string charge_id = 1;
  optional .google.protobuf.Timestamp charged_at = 2;
  optional .chesscom.payments.v1.MemberPromotion promotion = 3;
  optional bool coupon_code_used = 4;
  optional .chesscom.api.v1.Platform platform = 5;
}

```

**Source references:** SRC-0499, SRC-1470  
**URL references:** None independently associated  
**Related findings:** FND-06832, FND-06833, FND-06834

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06843"></a>
## FND-06843: chesscom.payments.v1.PromotionOnCharge.coupon_code_used = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool coupon_code_used = 4;

### Evidence

- **SRC-0499** `research/proto/chesscom/payments/v1/member_promotion.proto` — [preserved redacted evidence](../evidence/text/cbd659564e0a0380e1244d6197618e9dab74b5a2c650eab126b8a93de990fafd.proto)
  Character offset 590.

```text
rotobuf.Timestamp charged_at = 2;
  optional .chesscom.payments.v1.MemberPromotion promotion = 3;
  optional bool coupon_code_used = 4;
  optional .chesscom.api.v1.Platform platform = 5;
}

```

**Source references:** SRC-0499, SRC-1470  
**URL references:** None independently associated  
**Related findings:** FND-06832, FND-06833, FND-06834

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06844"></a>
## FND-06844: chesscom.payments.v1.PromotionOnCharge.platform = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Platform platform = 5;

### Evidence

- **SRC-0499** `research/proto/chesscom/payments/v1/member_promotion.proto` — [preserved redacted evidence](../evidence/text/cbd659564e0a0380e1244d6197618e9dab74b5a2c650eab126b8a93de990fafd.proto)
  Character offset 628.

```text
tional .chesscom.payments.v1.MemberPromotion promotion = 3;
  optional bool coupon_code_used = 4;
  optional .chesscom.api.v1.Platform platform = 5;
}

```

**Source references:** SRC-0499, SRC-1470  
**URL references:** None independently associated  
**Related findings:** FND-06832, FND-06833, FND-06834

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06845"></a>
## FND-06845: message declaration: chesscom.payments.v1.MemberSubscription

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MemberSubscription {

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 108.

```text
e: chesscom/payments/v1/member_subscription.proto
// syntax: proto3

package chesscom.payments.v1;

message MemberSubscription {
  oneof _price_cents {
  int32 price_cents = 6;
  }
  optional string subscription_id = 1;
  optional .chesscom.payments.v1.MembershipLevel membership_level = 2;
  optional .chesscom.payments.v1.PlanState plan_state = 3;
  optional int32 plan_length = 4;
  optional .chesscom.payments.v1.Sub
```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06846, FND-06847

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06846"></a>
## FND-06846: oneof declaration: chesscom.payments.v1.MemberSubscription._price_cents

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _price_cents {

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 139.

```text
subscription.proto
// syntax: proto3

package chesscom.payments.v1;

message MemberSubscription {
  oneof _price_cents {
  int32 price_cents = 6;
  }
  optional string subscription_id = 1;
  optional .chesscom.payments.v1.MembershipLevel membership_level = 2;
  optional .chesscom.payments.v1.PlanState plan_state = 3;
  optional int32 plan_length = 4;
  optional .chesscom.payments.v1.SubscriptionDurationUnit plan_unit
```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06847

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06847"></a>
## FND-06847: chesscom.payments.v1.MemberSubscription.price_cents = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 price_cents = 6;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 162.

```text
yntax: proto3

package chesscom.payments.v1;

message MemberSubscription {
  oneof _price_cents {
  int32 price_cents = 6;
  }
  optional string subscription_id = 1;
  optional .chesscom.payments.v1.MembershipLevel membership_level = 2;
  optional .chesscom.payments.v1.PlanState plan_state = 3;
  optional int32 plan_length = 4;
  optional .chesscom.payments.v1.SubscriptionDurationUnit plan_unit = 5;
  optional string
```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06848"></a>
## FND-06848: chesscom.payments.v1.MemberSubscription.subscription_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string subscription_id = 1;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 191.

```text
om.payments.v1;

message MemberSubscription {
  oneof _price_cents {
  int32 price_cents = 6;
  }
  optional string subscription_id = 1;
  optional .chesscom.payments.v1.MembershipLevel membership_level = 2;
  optional .chesscom.payments.v1.PlanState plan_state = 3;
  optional int32 plan_length = 4;
  optional .chesscom.payments.v1.SubscriptionDurationUnit plan_unit = 5;
  optional string currency = 7;
  optional .ch
```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846, FND-06847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06849"></a>
## FND-06849: chesscom.payments.v1.MemberSubscription.membership_level = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.MembershipLevel membership_level = 2;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 230.

```text
tion {
  oneof _price_cents {
  int32 price_cents = 6;
  }
  optional string subscription_id = 1;
  optional .chesscom.payments.v1.MembershipLevel membership_level = 2;
  optional .chesscom.payments.v1.PlanState plan_state = 3;
  optional int32 plan_length = 4;
  optional .chesscom.payments.v1.SubscriptionDurationUnit plan_unit = 5;
  optional string currency = 7;
  optional .chesscom.payments.v1.ChargePlatform platf
```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846, FND-06847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06850"></a>
## FND-06850: chesscom.payments.v1.MemberSubscription.plan_state = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.PlanState plan_state = 3;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 301.

```text
tring subscription_id = 1;
  optional .chesscom.payments.v1.MembershipLevel membership_level = 2;
  optional .chesscom.payments.v1.PlanState plan_state = 3;
  optional int32 plan_length = 4;
  optional .chesscom.payments.v1.SubscriptionDurationUnit plan_unit = 5;
  optional string currency = 7;
  optional .chesscom.payments.v1.ChargePlatform platform = 8;
  optional .chesscom.payments.v1.PaymentGateway gateway = 9;
 
```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846, FND-06847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06851"></a>
## FND-06851: chesscom.payments.v1.MemberSubscription.plan_length = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 plan_length = 4;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 360.

```text
.MembershipLevel membership_level = 2;
  optional .chesscom.payments.v1.PlanState plan_state = 3;
  optional int32 plan_length = 4;
  optional .chesscom.payments.v1.SubscriptionDurationUnit plan_unit = 5;
  optional string currency = 7;
  optional .chesscom.payments.v1.ChargePlatform platform = 8;
  optional .chesscom.payments.v1.PaymentGateway gateway = 9;
  optional .google.protobuf.Timestamp started_at = 10;
  opt
```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846, FND-06847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06852"></a>
## FND-06852: chesscom.payments.v1.MemberSubscription.plan_unit = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.SubscriptionDurationUnit plan_unit = 5;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 394.

```text
= 2;
  optional .chesscom.payments.v1.PlanState plan_state = 3;
  optional int32 plan_length = 4;
  optional .chesscom.payments.v1.SubscriptionDurationUnit plan_unit = 5;
  optional string currency = 7;
  optional .chesscom.payments.v1.ChargePlatform platform = 8;
  optional .chesscom.payments.v1.PaymentGateway gateway = 9;
  optional .google.protobuf.Timestamp started_at = 10;
  optional .google.protobuf.Timestamp c
```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846, FND-06847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06853"></a>
## FND-06853: chesscom.payments.v1.MemberSubscription.currency = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string currency = 7;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 467.

```text
l int32 plan_length = 4;
  optional .chesscom.payments.v1.SubscriptionDurationUnit plan_unit = 5;
  optional string currency = 7;
  optional .chesscom.payments.v1.ChargePlatform platform = 8;
  optional .chesscom.payments.v1.PaymentGateway gateway = 9;
  optional .google.protobuf.Timestamp started_at = 10;
  optional .google.protobuf.Timestamp current_period_ends_at = 11;
  optional .google.protobuf.Timestamp cancell
```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846, FND-06847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06854"></a>
## FND-06854: chesscom.payments.v1.MemberSubscription.platform = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.ChargePlatform platform = 8;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 499.

```text
nal .chesscom.payments.v1.SubscriptionDurationUnit plan_unit = 5;
  optional string currency = 7;
  optional .chesscom.payments.v1.ChargePlatform platform = 8;
  optional .chesscom.payments.v1.PaymentGateway gateway = 9;
  optional .google.protobuf.Timestamp started_at = 10;
  optional .google.protobuf.Timestamp current_period_ends_at = 11;
  optional .google.protobuf.Timestamp cancelled_at = 12;
  optional .chesscom
```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846, FND-06847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06855"></a>
## FND-06855: chesscom.payments.v1.MemberSubscription.gateway = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.PaymentGateway gateway = 9;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 561.

```text
 5;
  optional string currency = 7;
  optional .chesscom.payments.v1.ChargePlatform platform = 8;
  optional .chesscom.payments.v1.PaymentGateway gateway = 9;
  optional .google.protobuf.Timestamp started_at = 10;
  optional .google.protobuf.Timestamp current_period_ends_at = 11;
  optional .google.protobuf.Timestamp cancelled_at = 12;
  optional .chesscom.payments.v1.CancellationEffect cancellation_effect = 13;
  op
```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846, FND-06847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06856"></a>
## FND-06856: chesscom.payments.v1.MemberSubscription.started_at = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp started_at = 10;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 622.

```text
ents.v1.ChargePlatform platform = 8;
  optional .chesscom.payments.v1.PaymentGateway gateway = 9;
  optional .google.protobuf.Timestamp started_at = 10;
  optional .google.protobuf.Timestamp current_period_ends_at = 11;
  optional .google.protobuf.Timestamp cancelled_at = 12;
  optional .chesscom.payments.v1.CancellationEffect cancellation_effect = 13;
  optional .chesscom.payments.v1.TrialState trial_state = 14;
  o
```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846, FND-06847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06857"></a>
## FND-06857: chesscom.payments.v1.MemberSubscription.current_period_ends_at = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp current_period_ends_at = 11;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 677.

```text
om.payments.v1.PaymentGateway gateway = 9;
  optional .google.protobuf.Timestamp started_at = 10;
  optional .google.protobuf.Timestamp current_period_ends_at = 11;
  optional .google.protobuf.Timestamp cancelled_at = 12;
  optional .chesscom.payments.v1.CancellationEffect cancellation_effect = 13;
  optional .chesscom.payments.v1.TrialState trial_state = 14;
  optional .chesscom.payments.v1.SubscriptionPaymentStatus
```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846, FND-06847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06858"></a>
## FND-06858: chesscom.payments.v1.MemberSubscription.cancelled_at = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp cancelled_at = 12;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 744.

```text
buf.Timestamp started_at = 10;
  optional .google.protobuf.Timestamp current_period_ends_at = 11;
  optional .google.protobuf.Timestamp cancelled_at = 12;
  optional .chesscom.payments.v1.CancellationEffect cancellation_effect = 13;
  optional .chesscom.payments.v1.TrialState trial_state = 14;
  optional .chesscom.payments.v1.SubscriptionPaymentStatus payment_status = 15;
}

```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846, FND-06847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06859"></a>
## FND-06859: chesscom.payments.v1.MemberSubscription.cancellation_effect = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.CancellationEffect cancellation_effect = 13;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 801.

```text
f.Timestamp current_period_ends_at = 11;
  optional .google.protobuf.Timestamp cancelled_at = 12;
  optional .chesscom.payments.v1.CancellationEffect cancellation_effect = 13;
  optional .chesscom.payments.v1.TrialState trial_state = 14;
  optional .chesscom.payments.v1.SubscriptionPaymentStatus payment_status = 15;
}

```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846, FND-06847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06860"></a>
## FND-06860: chesscom.payments.v1.MemberSubscription.trial_state = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.TrialState trial_state = 14;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 879.

```text
 cancelled_at = 12;
  optional .chesscom.payments.v1.CancellationEffect cancellation_effect = 13;
  optional .chesscom.payments.v1.TrialState trial_state = 14;
  optional .chesscom.payments.v1.SubscriptionPaymentStatus payment_status = 15;
}

```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846, FND-06847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06861"></a>
## FND-06861: chesscom.payments.v1.MemberSubscription.payment_status = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.SubscriptionPaymentStatus payment_status = 15;

### Evidence

- **SRC-0500** `research/proto/chesscom/payments/v1/member_subscription.proto` — [preserved redacted evidence](../evidence/text/b46353c868c214c0f59c9421cacf9d38ac13cfa19917ed34b66982a538dcd2f5.proto)
  Character offset 941.

```text
ionEffect cancellation_effect = 13;
  optional .chesscom.payments.v1.TrialState trial_state = 14;
  optional .chesscom.payments.v1.SubscriptionPaymentStatus payment_status = 15;
}

```

**Source references:** SRC-0500, SRC-1471  
**URL references:** None independently associated  
**Related findings:** FND-06845, FND-06846, FND-06847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06862"></a>
## FND-06862: message declaration: chesscom.payments.v1.MembershipProductDetails

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MembershipProductDetails {

### Evidence

- **SRC-0501** `research/proto/chesscom/payments/v1/membership_product_details.proto` — [preserved redacted evidence](../evidence/text/51456623a7a3e431027763ebad2ec93c071f0f3d4899aa2f4bc75c5c79194386.proto)
  Character offset 115.

```text
scom/payments/v1/membership_product_details.proto
// syntax: proto3

package chesscom.payments.v1;

message MembershipProductDetails {
  optional string name = 1;
  optional string image_url = 2;
  optional string code = 3;
  optional int32 level = 4;
  optional string short_name = 5;
  optional int32 max_applicable_accounts = 6;
  repeated .chesscom.permissions.v1.PremiumFeature displayed_premium_features = 7;
  rep
```

**Source references:** SRC-0501, SRC-1472  
**URL references:** None independently associated  
**Related findings:** FND-06863, FND-06864

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06863"></a>
## FND-06863: chesscom.payments.v1.MembershipProductDetails.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0501** `research/proto/chesscom/payments/v1/membership_product_details.proto` — [preserved redacted evidence](../evidence/text/51456623a7a3e431027763ebad2ec93c071f0f3d4899aa2f4bc75c5c79194386.proto)
  Character offset 152.

```text
etails.proto
// syntax: proto3

package chesscom.payments.v1;

message MembershipProductDetails {
  optional string name = 1;
  optional string image_url = 2;
  optional string code = 3;
  optional int32 level = 4;
  optional string short_name = 5;
  optional int32 max_applicable_accounts = 6;
  repeated .chesscom.permissions.v1.PremiumFeature displayed_premium_features = 7;
  repeated .chesscom.premium_access.v1.Pre
```

**Source references:** SRC-0501, SRC-1472  
**URL references:** None independently associated  
**Related findings:** FND-06862, FND-06864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06864"></a>
## FND-06864: chesscom.payments.v1.MembershipProductDetails.image_url = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string image_url = 2;

### Evidence

- **SRC-0501** `research/proto/chesscom/payments/v1/membership_product_details.proto` — [preserved redacted evidence](../evidence/text/51456623a7a3e431027763ebad2ec93c071f0f3d4899aa2f4bc75c5c79194386.proto)
  Character offset 180.

```text
o3

package chesscom.payments.v1;

message MembershipProductDetails {
  optional string name = 1;
  optional string image_url = 2;
  optional string code = 3;
  optional int32 level = 4;
  optional string short_name = 5;
  optional int32 max_applicable_accounts = 6;
  repeated .chesscom.permissions.v1.PremiumFeature displayed_premium_features = 7;
  repeated .chesscom.premium_access.v1.PremiumFeature displayed_premiu
```

**Source references:** SRC-0501, SRC-1472  
**URL references:** None independently associated  
**Related findings:** FND-06862, FND-06863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06865"></a>
## FND-06865: chesscom.payments.v1.MembershipProductDetails.code = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string code = 3;

### Evidence

- **SRC-0501** `research/proto/chesscom/payments/v1/membership_product_details.proto` — [preserved redacted evidence](../evidence/text/51456623a7a3e431027763ebad2ec93c071f0f3d4899aa2f4bc75c5c79194386.proto)
  Character offset 213.

```text


message MembershipProductDetails {
  optional string name = 1;
  optional string image_url = 2;
  optional string code = 3;
  optional int32 level = 4;
  optional string short_name = 5;
  optional int32 max_applicable_accounts = 6;
  repeated .chesscom.permissions.v1.PremiumFeature displayed_premium_features = 7;
  repeated .chesscom.premium_access.v1.PremiumFeature displayed_premium_features_v2 = 8;
}

```

**Source references:** SRC-0501, SRC-1472  
**URL references:** None independently associated  
**Related findings:** FND-06862, FND-06863, FND-06864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06866"></a>
## FND-06866: chesscom.payments.v1.MembershipProductDetails.level = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 level = 4;

### Evidence

- **SRC-0501** `research/proto/chesscom/payments/v1/membership_product_details.proto` — [preserved redacted evidence](../evidence/text/51456623a7a3e431027763ebad2ec93c071f0f3d4899aa2f4bc75c5c79194386.proto)
  Character offset 241.

```text
etails {
  optional string name = 1;
  optional string image_url = 2;
  optional string code = 3;
  optional int32 level = 4;
  optional string short_name = 5;
  optional int32 max_applicable_accounts = 6;
  repeated .chesscom.permissions.v1.PremiumFeature displayed_premium_features = 7;
  repeated .chesscom.premium_access.v1.PremiumFeature displayed_premium_features_v2 = 8;
}

```

**Source references:** SRC-0501, SRC-1472  
**URL references:** None independently associated  
**Related findings:** FND-06862, FND-06863, FND-06864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06867"></a>
## FND-06867: chesscom.payments.v1.MembershipProductDetails.short_name = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string short_name = 5;

### Evidence

- **SRC-0501** `research/proto/chesscom/payments/v1/membership_product_details.proto` — [preserved redacted evidence](../evidence/text/51456623a7a3e431027763ebad2ec93c071f0f3d4899aa2f4bc75c5c79194386.proto)
  Character offset 269.

```text
ame = 1;
  optional string image_url = 2;
  optional string code = 3;
  optional int32 level = 4;
  optional string short_name = 5;
  optional int32 max_applicable_accounts = 6;
  repeated .chesscom.permissions.v1.PremiumFeature displayed_premium_features = 7;
  repeated .chesscom.premium_access.v1.PremiumFeature displayed_premium_features_v2 = 8;
}

```

**Source references:** SRC-0501, SRC-1472  
**URL references:** None independently associated  
**Related findings:** FND-06862, FND-06863, FND-06864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06868"></a>
## FND-06868: chesscom.payments.v1.MembershipProductDetails.max_applicable_accounts = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 max_applicable_accounts = 6;

### Evidence

- **SRC-0501** `research/proto/chesscom/payments/v1/membership_product_details.proto` — [preserved redacted evidence](../evidence/text/51456623a7a3e431027763ebad2ec93c071f0f3d4899aa2f4bc75c5c79194386.proto)
  Character offset 303.

```text
rl = 2;
  optional string code = 3;
  optional int32 level = 4;
  optional string short_name = 5;
  optional int32 max_applicable_accounts = 6;
  repeated .chesscom.permissions.v1.PremiumFeature displayed_premium_features = 7;
  repeated .chesscom.premium_access.v1.PremiumFeature displayed_premium_features_v2 = 8;
}

```

**Source references:** SRC-0501, SRC-1472  
**URL references:** None independently associated  
**Related findings:** FND-06862, FND-06863, FND-06864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06869"></a>
## FND-06869: chesscom.payments.v1.MembershipProductDetails.displayed_premium_features = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.permissions.v1.PremiumFeature displayed_premium_features = 7;

### Evidence

- **SRC-0501** `research/proto/chesscom/payments/v1/membership_product_details.proto` — [preserved redacted evidence](../evidence/text/51456623a7a3e431027763ebad2ec93c071f0f3d4899aa2f4bc75c5c79194386.proto)
  Character offset 349.

```text
 int32 level = 4;
  optional string short_name = 5;
  optional int32 max_applicable_accounts = 6;
  repeated .chesscom.permissions.v1.PremiumFeature displayed_premium_features = 7;
  repeated .chesscom.premium_access.v1.PremiumFeature displayed_premium_features_v2 = 8;
}

```

**Source references:** SRC-0501, SRC-1472  
**URL references:** None independently associated  
**Related findings:** FND-06862, FND-06863, FND-06864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06870"></a>
## FND-06870: chesscom.payments.v1.MembershipProductDetails.displayed_premium_features_v2 = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.premium_access.v1.PremiumFeature displayed_premium_features_v2 = 8;

### Evidence

- **SRC-0501** `research/proto/chesscom/payments/v1/membership_product_details.proto` — [preserved redacted evidence](../evidence/text/51456623a7a3e431027763ebad2ec93c071f0f3d4899aa2f4bc75c5c79194386.proto)
  Character offset 432.

```text
_accounts = 6;
  repeated .chesscom.permissions.v1.PremiumFeature displayed_premium_features = 7;
  repeated .chesscom.premium_access.v1.PremiumFeature displayed_premium_features_v2 = 8;
}

```

**Source references:** SRC-0501, SRC-1472  
**URL references:** None independently associated  
**Related findings:** FND-06862, FND-06863, FND-06864

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06871"></a>
## FND-06871: message declaration: chesscom.payments.v1.CancelMembershipRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CancelMembershipRequest {

### Evidence

- **SRC-0502** `research/proto/chesscom/payments/v1/membership_service.proto` — [preserved redacted evidence](../evidence/text/7aeff6a6dd7ca5c79ccd7a122049a900ee479ac6b4d1982ebc60bd14bd5e2243.proto)
  Character offset 107.

```text
ce: chesscom/payments/v1/membership_service.proto
// syntax: proto3

package chesscom.payments.v1;

message CancelMembershipRequest {
}

message CancelMembershipResponse {
}

message SubmitCancellationSurveyRequest {
  oneof _feedback {
  string feedback = 2;
  }
  optional .chesscom.payments.v1.CancelSurveyReason reason = 1;
}

message SubmitCancellationSurveyResponse {
}

message ExtendMembershipRequest {
}

messag
```

**Source references:** SRC-0502, SRC-1473  
**URL references:** None independently associated  
**Related findings:** FND-06872, FND-06873

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06872"></a>
## FND-06872: message declaration: chesscom.payments.v1.CancelMembershipResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CancelMembershipResponse {

### Evidence

- **SRC-0502** `research/proto/chesscom/payments/v1/membership_service.proto` — [preserved redacted evidence](../evidence/text/7aeff6a6dd7ca5c79ccd7a122049a900ee479ac6b4d1982ebc60bd14bd5e2243.proto)
  Character offset 144.

```text
ervice.proto
// syntax: proto3

package chesscom.payments.v1;

message CancelMembershipRequest {
}

message CancelMembershipResponse {
}

message SubmitCancellationSurveyRequest {
  oneof _feedback {
  string feedback = 2;
  }
  optional .chesscom.payments.v1.CancelSurveyReason reason = 1;
}

message SubmitCancellationSurveyResponse {
}

message ExtendMembershipRequest {
}

message ExtendMembershipResponse {
}

```

**Source references:** SRC-0502, SRC-1473  
**URL references:** None independently associated  
**Related findings:** FND-06871, FND-06873

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06873"></a>
## FND-06873: message declaration: chesscom.payments.v1.SubmitCancellationSurveyRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SubmitCancellationSurveyRequest {

### Evidence

- **SRC-0502** `research/proto/chesscom/payments/v1/membership_service.proto` — [preserved redacted evidence](../evidence/text/7aeff6a6dd7ca5c79ccd7a122049a900ee479ac6b4d1982ebc60bd14bd5e2243.proto)
  Character offset 182.

```text
e chesscom.payments.v1;

message CancelMembershipRequest {
}

message CancelMembershipResponse {
}

message SubmitCancellationSurveyRequest {
  oneof _feedback {
  string feedback = 2;
  }
  optional .chesscom.payments.v1.CancelSurveyReason reason = 1;
}

message SubmitCancellationSurveyResponse {
}

message ExtendMembershipRequest {
}

message ExtendMembershipResponse {
}

```

**Source references:** SRC-0502, SRC-1473  
**URL references:** None independently associated  
**Related findings:** FND-06871, FND-06872

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06874"></a>
## FND-06874: oneof declaration: chesscom.payments.v1.SubmitCancellationSurveyRequest._feedback

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _feedback {

### Evidence

- **SRC-0502** `research/proto/chesscom/payments/v1/membership_service.proto` — [preserved redacted evidence](../evidence/text/7aeff6a6dd7ca5c79ccd7a122049a900ee479ac6b4d1982ebc60bd14bd5e2243.proto)
  Character offset 226.

```text
rshipRequest {
}

message CancelMembershipResponse {
}

message SubmitCancellationSurveyRequest {
  oneof _feedback {
  string feedback = 2;
  }
  optional .chesscom.payments.v1.CancelSurveyReason reason = 1;
}

message SubmitCancellationSurveyResponse {
}

message ExtendMembershipRequest {
}

message ExtendMembershipResponse {
}

```

**Source references:** SRC-0502, SRC-1473  
**URL references:** None independently associated  
**Related findings:** FND-06871, FND-06872, FND-06873

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
