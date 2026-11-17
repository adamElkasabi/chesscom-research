# data_models — findings 6001–6100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-06275"></a>
## FND-06275: message declaration: chesscom.payments.v1.AdditionalDataField

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AdditionalDataField {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1307.

```text
ant_id {
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
  optional bool required = 4;
  repeat
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06276"></a>
## FND-06276: oneof declaration: chesscom.payments.v1.AdditionalDataField._validation_rule

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _validation_rule {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1339.

```text
9;
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
  optional bool required = 4;
  repeated .chesscom.payments.v1.Additio
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06277"></a>
## FND-06277: chesscom.payments.v1.AdditionalDataField.validation_rule = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string validation_rule = 6;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1366.

```text
me {
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
  optional bool required = 4;
  repeated .chesscom.payments.v1.AdditionalDataFieldSelectOption op
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06278"></a>
## FND-06278: oneof declaration: chesscom.payments.v1.AdditionalDataField._validation_err_msg

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _validation_err_msg {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1400.

```text
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
  optional bool required = 4;
  repeated .chesscom.payments.v1.AdditionalDataFieldSelectOption options = 5;
}

message AdditionalDa
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06279"></a>
## FND-06279: chesscom.payments.v1.AdditionalDataField.validation_err_msg = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string validation_err_msg = 7;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1430.

```text
ield {
  oneof _validation_rule {
  string validation_rule = 6;
  }
  oneof _validation_err_msg {
  string validation_err_msg = 7;
  }
  optional string name = 1;
  optional string label = 2;
  optional .chesscom.payments.v1.AdditionalDataFieldType type = 3;
  optional bool required = 4;
  repeated .chesscom.payments.v1.AdditionalDataFieldSelectOption options = 5;
}

message AdditionalDataFieldSelectOption {
  option
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06280"></a>
## FND-06280: chesscom.payments.v1.AdditionalDataField.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1467.

```text
tring validation_rule = 6;
  }
  oneof _validation_err_msg {
  string validation_err_msg = 7;
  }
  optional string name = 1;
  optional string label = 2;
  optional .chesscom.payments.v1.AdditionalDataFieldType type = 3;
  optional bool required = 4;
  repeated .chesscom.payments.v1.AdditionalDataFieldSelectOption options = 5;
}

message AdditionalDataFieldSelectOption {
  optional string label = 1;
  optional strin
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06281"></a>
## FND-06281: chesscom.payments.v1.AdditionalDataField.label = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string label = 2;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1495.

```text
 }
  oneof _validation_err_msg {
  string validation_err_msg = 7;
  }
  optional string name = 1;
  optional string label = 2;
  optional .chesscom.payments.v1.AdditionalDataFieldType type = 3;
  optional bool required = 4;
  repeated .chesscom.payments.v1.AdditionalDataFieldSelectOption options = 5;
}

message AdditionalDataFieldSelectOption {
  optional string label = 1;
  optional string value = 2;
}

message Stor
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06282"></a>
## FND-06282: chesscom.payments.v1.AdditionalDataField.type = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.AdditionalDataFieldType type = 3;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1524.

```text
g {
  string validation_err_msg = 7;
  }
  optional string name = 1;
  optional string label = 2;
  optional .chesscom.payments.v1.AdditionalDataFieldType type = 3;
  optional bool required = 4;
  repeated .chesscom.payments.v1.AdditionalDataFieldSelectOption options = 5;
}

message AdditionalDataFieldSelectOption {
  optional string label = 1;
  optional string value = 2;
}

message StoredPaymentDetail {
  oneof _nu
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06283"></a>
## FND-06283: chesscom.payments.v1.AdditionalDataField.required = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool required = 4;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1591.

```text
;
  optional string label = 2;
  optional .chesscom.payments.v1.AdditionalDataFieldType type = 3;
  optional bool required = 4;
  repeated .chesscom.payments.v1.AdditionalDataFieldSelectOption options = 5;
}

message AdditionalDataFieldSelectOption {
  optional string label = 1;
  optional string value = 2;
}

message StoredPaymentDetail {
  oneof _number {
  string number = 2;
  }
  oneof _owner_name {
  string owne
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06284"></a>
## FND-06284: chesscom.payments.v1.AdditionalDataField.options = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.AdditionalDataFieldSelectOption options = 5;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1621.

```text

  optional .chesscom.payments.v1.AdditionalDataFieldType type = 3;
  optional bool required = 4;
  repeated .chesscom.payments.v1.AdditionalDataFieldSelectOption options = 5;
}

message AdditionalDataFieldSelectOption {
  optional string label = 1;
  optional string value = 2;
}

message StoredPaymentDetail {
  oneof _number {
  string number = 2;
  }
  oneof _owner_name {
  string owner_name = 3;
  }
  optional str
```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06285"></a>
## FND-06285: message declaration: chesscom.payments.v1.AdditionalDataFieldSelectOption

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AdditionalDataFieldSelectOption {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1700.

```text
bool required = 4;
  repeated .chesscom.payments.v1.AdditionalDataFieldSelectOption options = 5;
}

message AdditionalDataFieldSelectOption {
  optional string label = 1;
  optional string value = 2;
}

message StoredPaymentDetail {
  oneof _number {
  string number = 2;
  }
  oneof _owner_name {
  string owner_name = 3;
  }
  optional string id = 1;
}

```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06286"></a>
## FND-06286: chesscom.payments.v1.AdditionalDataFieldSelectOption.label = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string label = 1;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1744.

```text
ents.v1.AdditionalDataFieldSelectOption options = 5;
}

message AdditionalDataFieldSelectOption {
  optional string label = 1;
  optional string value = 2;
}

message StoredPaymentDetail {
  oneof _number {
  string number = 2;
  }
  oneof _owner_name {
  string owner_name = 3;
  }
  optional string id = 1;
}

```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06287"></a>
## FND-06287: chesscom.payments.v1.AdditionalDataFieldSelectOption.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1773.

```text
lectOption options = 5;
}

message AdditionalDataFieldSelectOption {
  optional string label = 1;
  optional string value = 2;
}

message StoredPaymentDetail {
  oneof _number {
  string number = 2;
  }
  oneof _owner_name {
  string owner_name = 3;
  }
  optional string id = 1;
}

```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06288"></a>
## FND-06288: message declaration: chesscom.payments.v1.StoredPaymentDetail

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StoredPaymentDetail {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1803.

```text
sage AdditionalDataFieldSelectOption {
  optional string label = 1;
  optional string value = 2;
}

message StoredPaymentDetail {
  oneof _number {
  string number = 2;
  }
  oneof _owner_name {
  string owner_name = 3;
  }
  optional string id = 1;
}

```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06289"></a>
## FND-06289: oneof declaration: chesscom.payments.v1.StoredPaymentDetail._number

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1835.

```text
tion {
  optional string label = 1;
  optional string value = 2;
}

message StoredPaymentDetail {
  oneof _number {
  string number = 2;
  }
  oneof _owner_name {
  string owner_name = 3;
  }
  optional string id = 1;
}

```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06290"></a>
## FND-06290: chesscom.payments.v1.StoredPaymentDetail.number = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string number = 2;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1853.

```text
string label = 1;
  optional string value = 2;
}

message StoredPaymentDetail {
  oneof _number {
  string number = 2;
  }
  oneof _owner_name {
  string owner_name = 3;
  }
  optional string id = 1;
}

```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06291"></a>
## FND-06291: oneof declaration: chesscom.payments.v1.StoredPaymentDetail._owner_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _owner_name {

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1878.

```text
nal string value = 2;
}

message StoredPaymentDetail {
  oneof _number {
  string number = 2;
  }
  oneof _owner_name {
  string owner_name = 3;
  }
  optional string id = 1;
}

```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06292"></a>
## FND-06292: chesscom.payments.v1.StoredPaymentDetail.owner_name = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string owner_name = 3;

### Evidence

- **SRC-0480** `research/proto/chesscom/payments/v1/available_payment_method.proto` — [preserved redacted evidence](../evidence/text/7b65340ca0827b77ac9d2814870940080be58ea7fa4ed3d07bc8bac416cbada8.proto)
  Character offset 1900.

```text
}

message StoredPaymentDetail {
  oneof _number {
  string number = 2;
  }
  oneof _owner_name {
  string owner_name = 3;
  }
  optional string id = 1;
}

```

**Source references:** SRC-0480, SRC-1451  
**URL references:** None independently associated  
**Related findings:** FND-06237, FND-06238, FND-06239

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06293"></a>
## FND-06293: chesscom.payments.v1.StoredPaymentDetail.id = 1

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

<a id="FND-06294"></a>
## FND-06294: message declaration: chesscom.payments.v1.BillingHistoryEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BillingHistoryEntry {

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 110.

```text
 chesscom/payments/v1/billing_history_entry.proto
// syntax: proto3

package chesscom.payments.v1;

message BillingHistoryEntry {
  oneof _display_name {
  string display_name = 2;
  }
  oneof _order_type {
  .chesscom.payments.v1.OrderType order_type = 3;
  }
  oneof _gift_receiver {
  .chesscom.payments.v1.BillingHistoryEntryUser gift_receiver = 6;
  }
  optional int32 id = 1;
  optional .chesscom.api.v1.Money pric
```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06295, FND-06296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06295"></a>
## FND-06295: oneof declaration: chesscom.payments.v1.BillingHistoryEntry._display_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _display_name {

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 142.

```text
story_entry.proto
// syntax: proto3

package chesscom.payments.v1;

message BillingHistoryEntry {
  oneof _display_name {
  string display_name = 2;
  }
  oneof _order_type {
  .chesscom.payments.v1.OrderType order_type = 3;
  }
  oneof _gift_receiver {
  .chesscom.payments.v1.BillingHistoryEntryUser gift_receiver = 6;
  }
  optional int32 id = 1;
  optional .chesscom.api.v1.Money price = 4;
  optional .chesscom.paym
```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06296"></a>
## FND-06296: chesscom.payments.v1.BillingHistoryEntry.display_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string display_name = 2;

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 166.

```text
tax: proto3

package chesscom.payments.v1;

message BillingHistoryEntry {
  oneof _display_name {
  string display_name = 2;
  }
  oneof _order_type {
  .chesscom.payments.v1.OrderType order_type = 3;
  }
  oneof _gift_receiver {
  .chesscom.payments.v1.BillingHistoryEntryUser gift_receiver = 6;
  }
  optional int32 id = 1;
  optional .chesscom.api.v1.Money price = 4;
  optional .chesscom.payments.v1.BillingHistoryEn
```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06295

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06297"></a>
## FND-06297: oneof declaration: chesscom.payments.v1.BillingHistoryEntry._order_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _order_type {

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 197.

```text
ayments.v1;

message BillingHistoryEntry {
  oneof _display_name {
  string display_name = 2;
  }
  oneof _order_type {
  .chesscom.payments.v1.OrderType order_type = 3;
  }
  oneof _gift_receiver {
  .chesscom.payments.v1.BillingHistoryEntryUser gift_receiver = 6;
  }
  optional int32 id = 1;
  optional .chesscom.api.v1.Money price = 4;
  optional .chesscom.payments.v1.BillingHistoryEntryUser placed_by = 5;
  option
```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06295, FND-06296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06298"></a>
## FND-06298: chesscom.payments.v1.BillingHistoryEntry.order_type = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.OrderType order_type = 3;

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 219.

```text
illingHistoryEntry {
  oneof _display_name {
  string display_name = 2;
  }
  oneof _order_type {
  .chesscom.payments.v1.OrderType order_type = 3;
  }
  oneof _gift_receiver {
  .chesscom.payments.v1.BillingHistoryEntryUser gift_receiver = 6;
  }
  optional int32 id = 1;
  optional .chesscom.api.v1.Money price = 4;
  optional .chesscom.payments.v1.BillingHistoryEntryUser placed_by = 5;
  optional .google.protobuf.Ti
```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06295, FND-06296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06299"></a>
## FND-06299: oneof declaration: chesscom.payments.v1.BillingHistoryEntry._gift_receiver

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gift_receiver {

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 273.

```text
display_name = 2;
  }
  oneof _order_type {
  .chesscom.payments.v1.OrderType order_type = 3;
  }
  oneof _gift_receiver {
  .chesscom.payments.v1.BillingHistoryEntryUser gift_receiver = 6;
  }
  optional int32 id = 1;
  optional .chesscom.api.v1.Money price = 4;
  optional .chesscom.payments.v1.BillingHistoryEntryUser placed_by = 5;
  optional .google.protobuf.Timestamp created_date = 7;
  optional bool invoice_avai
```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06295, FND-06296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06300"></a>
## FND-06300: chesscom.payments.v1.BillingHistoryEntry.gift_receiver = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.BillingHistoryEntryUser gift_receiver = 6;

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 298.

```text
neof _order_type {
  .chesscom.payments.v1.OrderType order_type = 3;
  }
  oneof _gift_receiver {
  .chesscom.payments.v1.BillingHistoryEntryUser gift_receiver = 6;
  }
  optional int32 id = 1;
  optional .chesscom.api.v1.Money price = 4;
  optional .chesscom.payments.v1.BillingHistoryEntryUser placed_by = 5;
  optional .google.protobuf.Timestamp created_date = 7;
  optional bool invoice_available = 8;
}

message Bil
```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06295, FND-06296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06301"></a>
## FND-06301: chesscom.payments.v1.BillingHistoryEntry.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 id = 1;

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 369.

```text
}
  oneof _gift_receiver {
  .chesscom.payments.v1.BillingHistoryEntryUser gift_receiver = 6;
  }
  optional int32 id = 1;
  optional .chesscom.api.v1.Money price = 4;
  optional .chesscom.payments.v1.BillingHistoryEntryUser placed_by = 5;
  optional .google.protobuf.Timestamp created_date = 7;
  optional bool invoice_available = 8;
}

message BillingHistoryEntryUser {
  oneof _email {
  string email = 2;
  }
  optio
```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06295, FND-06296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06302"></a>
## FND-06302: chesscom.payments.v1.BillingHistoryEntry.price = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money price = 4;

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 394.

```text
{
  .chesscom.payments.v1.BillingHistoryEntryUser gift_receiver = 6;
  }
  optional int32 id = 1;
  optional .chesscom.api.v1.Money price = 4;
  optional .chesscom.payments.v1.BillingHistoryEntryUser placed_by = 5;
  optional .google.protobuf.Timestamp created_date = 7;
  optional bool invoice_available = 8;
}

message BillingHistoryEntryUser {
  oneof _email {
  string email = 2;
  }
  optional string username = 1;

```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06295, FND-06296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06303"></a>
## FND-06303: chesscom.payments.v1.BillingHistoryEntry.placed_by = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.BillingHistoryEntryUser placed_by = 5;

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 439.

```text
User gift_receiver = 6;
  }
  optional int32 id = 1;
  optional .chesscom.api.v1.Money price = 4;
  optional .chesscom.payments.v1.BillingHistoryEntryUser placed_by = 5;
  optional .google.protobuf.Timestamp created_date = 7;
  optional bool invoice_available = 8;
}

message BillingHistoryEntryUser {
  oneof _email {
  string email = 2;
  }
  optional string username = 1;
}

```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06295, FND-06296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06304"></a>
## FND-06304: chesscom.payments.v1.BillingHistoryEntry.created_date = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp created_date = 7;

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 511.

```text
m.api.v1.Money price = 4;
  optional .chesscom.payments.v1.BillingHistoryEntryUser placed_by = 5;
  optional .google.protobuf.Timestamp created_date = 7;
  optional bool invoice_available = 8;
}

message BillingHistoryEntryUser {
  oneof _email {
  string email = 2;
  }
  optional string username = 1;
}

```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06295, FND-06296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06305"></a>
## FND-06305: chesscom.payments.v1.BillingHistoryEntry.invoice_available = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool invoice_available = 8;

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 567.

```text
v1.BillingHistoryEntryUser placed_by = 5;
  optional .google.protobuf.Timestamp created_date = 7;
  optional bool invoice_available = 8;
}

message BillingHistoryEntryUser {
  oneof _email {
  string email = 2;
  }
  optional string username = 1;
}

```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06295, FND-06296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06306"></a>
## FND-06306: message declaration: chesscom.payments.v1.BillingHistoryEntryUser

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BillingHistoryEntryUser {

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 607.

```text
;
  optional .google.protobuf.Timestamp created_date = 7;
  optional bool invoice_available = 8;
}

message BillingHistoryEntryUser {
  oneof _email {
  string email = 2;
  }
  optional string username = 1;
}

```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06295, FND-06296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06307"></a>
## FND-06307: oneof declaration: chesscom.payments.v1.BillingHistoryEntryUser._email

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _email {

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 643.

```text
amp created_date = 7;
  optional bool invoice_available = 8;
}

message BillingHistoryEntryUser {
  oneof _email {
  string email = 2;
  }
  optional string username = 1;
}

```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06295, FND-06296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06308"></a>
## FND-06308: chesscom.payments.v1.BillingHistoryEntryUser.email = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string email = 2;

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 660.

```text
= 7;
  optional bool invoice_available = 8;
}

message BillingHistoryEntryUser {
  oneof _email {
  string email = 2;
  }
  optional string username = 1;
}

```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06295, FND-06296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06309"></a>
## FND-06309: chesscom.payments.v1.BillingHistoryEntryUser.username = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string username = 1;

### Evidence

- **SRC-0481** `research/proto/chesscom/payments/v1/billing_history_entry.proto` — [preserved redacted evidence](../evidence/text/ca00a6b3aee197ab78c3d1405993db0e9068709e6d36af2626cc371aaeda8ade.proto)
  Character offset 684.

```text
oice_available = 8;
}

message BillingHistoryEntryUser {
  oneof _email {
  string email = 2;
  }
  optional string username = 1;
}

```

**Source references:** SRC-0481, SRC-1452  
**URL references:** None independently associated  
**Related findings:** FND-06294, FND-06295, FND-06296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06310"></a>
## FND-06310: message declaration: chesscom.payments.v1.GetUserBillingHistoryRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserBillingHistoryRequest {

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 104.

```text
ource: chesscom/payments/v1/billing_service.proto
// syntax: proto3

package chesscom.payments.v1;

message GetUserBillingHistoryRequest {
}

message GetUserBillingHistoryResponse {
  repeated .chesscom.payments.v1.BillingHistoryEntry billing_history = 1;
}

message GetUserBillingInformationRequest {
}

message GetUserBillingInformationResponse {
  oneof _payment_method {
  .chesscom.payments.v1.PaymentMethod payment
```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06311, FND-06312

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06311"></a>
## FND-06311: message declaration: chesscom.payments.v1.GetUserBillingHistoryResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserBillingHistoryResponse {

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 146.

```text
e.proto
// syntax: proto3

package chesscom.payments.v1;

message GetUserBillingHistoryRequest {
}

message GetUserBillingHistoryResponse {
  repeated .chesscom.payments.v1.BillingHistoryEntry billing_history = 1;
}

message GetUserBillingInformationRequest {
}

message GetUserBillingInformationResponse {
  oneof _payment_method {
  .chesscom.payments.v1.PaymentMethod payment_method = 1;
  }
  oneof _is_tax_included_
```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06312

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06312"></a>
## FND-06312: chesscom.payments.v1.GetUserBillingHistoryResponse.billing_history = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.BillingHistoryEntry billing_history = 1;

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 188.

```text
m.payments.v1;

message GetUserBillingHistoryRequest {
}

message GetUserBillingHistoryResponse {
  repeated .chesscom.payments.v1.BillingHistoryEntry billing_history = 1;
}

message GetUserBillingInformationRequest {
}

message GetUserBillingInformationResponse {
  oneof _payment_method {
  .chesscom.payments.v1.PaymentMethod payment_method = 1;
  }
  oneof _is_tax_included_in_price {
  bool is_tax_included_in_price
```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06313"></a>
## FND-06313: message declaration: chesscom.payments.v1.GetUserBillingInformationRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserBillingInformationRequest {

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 263.

```text
llingHistoryResponse {
  repeated .chesscom.payments.v1.BillingHistoryEntry billing_history = 1;
}

message GetUserBillingInformationRequest {
}

message GetUserBillingInformationResponse {
  oneof _payment_method {
  .chesscom.payments.v1.PaymentMethod payment_method = 1;
  }
  oneof _is_tax_included_in_price {
  bool is_tax_included_in_price = 3;
  }
  optional .chesscom.api.v1.Country country = 2;
  optional .ches
```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311, FND-06312

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06314"></a>
## FND-06314: message declaration: chesscom.payments.v1.GetUserBillingInformationResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserBillingInformationResponse {

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 309.

```text
yments.v1.BillingHistoryEntry billing_history = 1;
}

message GetUserBillingInformationRequest {
}

message GetUserBillingInformationResponse {
  oneof _payment_method {
  .chesscom.payments.v1.PaymentMethod payment_method = 1;
  }
  oneof _is_tax_included_in_price {
  bool is_tax_included_in_price = 3;
  }
  optional .chesscom.api.v1.Country country = 2;
  optional .chesscom.payments.v1.SubscriptionPaymentStatus sub
```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311, FND-06312

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06315"></a>
## FND-06315: oneof declaration: chesscom.payments.v1.GetUserBillingInformationResponse._payment_method

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _payment_method {

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 355.

```text
= 1;
}

message GetUserBillingInformationRequest {
}

message GetUserBillingInformationResponse {
  oneof _payment_method {
  .chesscom.payments.v1.PaymentMethod payment_method = 1;
  }
  oneof _is_tax_included_in_price {
  bool is_tax_included_in_price = 3;
  }
  optional .chesscom.api.v1.Country country = 2;
  optional .chesscom.payments.v1.SubscriptionPaymentStatus subscription_payment_status = 4;
}

message GetOr
```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311, FND-06312

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06316"></a>
## FND-06316: chesscom.payments.v1.GetUserBillingInformationResponse.payment_method = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.PaymentMethod payment_method = 1;

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 381.

```text
lingInformationRequest {
}

message GetUserBillingInformationResponse {
  oneof _payment_method {
  .chesscom.payments.v1.PaymentMethod payment_method = 1;
  }
  oneof _is_tax_included_in_price {
  bool is_tax_included_in_price = 3;
  }
  optional .chesscom.api.v1.Country country = 2;
  optional .chesscom.payments.v1.SubscriptionPaymentStatus subscription_payment_status = 4;
}

message GetOrderInvoiceRequest {
  opti
```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311, FND-06312

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06317"></a>
## FND-06317: oneof declaration: chesscom.payments.v1.GetUserBillingInformationResponse._is_tax_included_in_price

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_tax_included_in_price {

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 443.

```text
esponse {
  oneof _payment_method {
  .chesscom.payments.v1.PaymentMethod payment_method = 1;
  }
  oneof _is_tax_included_in_price {
  bool is_tax_included_in_price = 3;
  }
  optional .chesscom.api.v1.Country country = 2;
  optional .chesscom.payments.v1.SubscriptionPaymentStatus subscription_payment_status = 4;
}

message GetOrderInvoiceRequest {
  optional int32 order_id = 1;
  optional .chesscom.payments.v1.Invo
```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311, FND-06312

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06318"></a>
## FND-06318: chesscom.payments.v1.GetUserBillingInformationResponse.is_tax_included_in_price = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_tax_included_in_price = 3;

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 479.

```text
  .chesscom.payments.v1.PaymentMethod payment_method = 1;
  }
  oneof _is_tax_included_in_price {
  bool is_tax_included_in_price = 3;
  }
  optional .chesscom.api.v1.Country country = 2;
  optional .chesscom.payments.v1.SubscriptionPaymentStatus subscription_payment_status = 4;
}

message GetOrderInvoiceRequest {
  optional int32 order_id = 1;
  optional .chesscom.payments.v1.InvoiceBillTo bill_to = 2;
}

message Ge
```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311, FND-06312

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06319"></a>
## FND-06319: chesscom.payments.v1.GetUserBillingInformationResponse.country = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Country country = 2;

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 520.

```text
ment_method = 1;
  }
  oneof _is_tax_included_in_price {
  bool is_tax_included_in_price = 3;
  }
  optional .chesscom.api.v1.Country country = 2;
  optional .chesscom.payments.v1.SubscriptionPaymentStatus subscription_payment_status = 4;
}

message GetOrderInvoiceRequest {
  optional int32 order_id = 1;
  optional .chesscom.payments.v1.InvoiceBillTo bill_to = 2;
}

message GetOrderInvoiceResponse {
  optional bytes 
```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311, FND-06312

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06320"></a>
## FND-06320: chesscom.payments.v1.GetUserBillingInformationResponse.subscription_payment_status = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.SubscriptionPaymentStatus subscription_payment_status = 4;

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 569.

```text
price {
  bool is_tax_included_in_price = 3;
  }
  optional .chesscom.api.v1.Country country = 2;
  optional .chesscom.payments.v1.SubscriptionPaymentStatus subscription_payment_status = 4;
}

message GetOrderInvoiceRequest {
  optional int32 order_id = 1;
  optional .chesscom.payments.v1.InvoiceBillTo bill_to = 2;
}

message GetOrderInvoiceResponse {
  optional bytes pdf = 1;
  optional string file_name = 2;
}

```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311, FND-06312

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06321"></a>
## FND-06321: message declaration: chesscom.payments.v1.GetOrderInvoiceRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetOrderInvoiceRequest {

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 662.

```text
= 2;
  optional .chesscom.payments.v1.SubscriptionPaymentStatus subscription_payment_status = 4;
}

message GetOrderInvoiceRequest {
  optional int32 order_id = 1;
  optional .chesscom.payments.v1.InvoiceBillTo bill_to = 2;
}

message GetOrderInvoiceResponse {
  optional bytes pdf = 1;
  optional string file_name = 2;
}

```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311, FND-06312

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06322"></a>
## FND-06322: chesscom.payments.v1.GetOrderInvoiceRequest.order_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 order_id = 1;

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 697.

```text
v1.SubscriptionPaymentStatus subscription_payment_status = 4;
}

message GetOrderInvoiceRequest {
  optional int32 order_id = 1;
  optional .chesscom.payments.v1.InvoiceBillTo bill_to = 2;
}

message GetOrderInvoiceResponse {
  optional bytes pdf = 1;
  optional string file_name = 2;
}

```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311, FND-06312

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06323"></a>
## FND-06323: chesscom.payments.v1.GetOrderInvoiceRequest.bill_to = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.InvoiceBillTo bill_to = 2;

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 728.

```text
bscription_payment_status = 4;
}

message GetOrderInvoiceRequest {
  optional int32 order_id = 1;
  optional .chesscom.payments.v1.InvoiceBillTo bill_to = 2;
}

message GetOrderInvoiceResponse {
  optional bytes pdf = 1;
  optional string file_name = 2;
}

```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311, FND-06312

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06324"></a>
## FND-06324: message declaration: chesscom.payments.v1.GetOrderInvoiceResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetOrderInvoiceResponse {

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 789.

```text
est {
  optional int32 order_id = 1;
  optional .chesscom.payments.v1.InvoiceBillTo bill_to = 2;
}

message GetOrderInvoiceResponse {
  optional bytes pdf = 1;
  optional string file_name = 2;
}

```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311, FND-06312

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06325"></a>
## FND-06325: chesscom.payments.v1.GetOrderInvoiceResponse.pdf = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bytes pdf = 1;

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 825.

```text

  optional .chesscom.payments.v1.InvoiceBillTo bill_to = 2;
}

message GetOrderInvoiceResponse {
  optional bytes pdf = 1;
  optional string file_name = 2;
}

```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311, FND-06312

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06326"></a>
## FND-06326: chesscom.payments.v1.GetOrderInvoiceResponse.file_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string file_name = 2;

### Evidence

- **SRC-0482** `research/proto/chesscom/payments/v1/billing_service.proto` — [preserved redacted evidence](../evidence/text/bdbace3fa85c5e0d105249fce02f3fdc7bd73c0a10e15c17ae08719043bbf3d3.proto)
  Character offset 851.

```text
ents.v1.InvoiceBillTo bill_to = 2;
}

message GetOrderInvoiceResponse {
  optional bytes pdf = 1;
  optional string file_name = 2;
}

```

**Source references:** SRC-0482, SRC-1453  
**URL references:** None independently associated  
**Related findings:** FND-06310, FND-06311, FND-06312

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06327"></a>
## FND-06327: enum declaration: chesscom.payments.v1.ChargePlatform

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ChargePlatform {

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 95.

```text
// source: chesscom/payments/v1/charge.proto
// syntax: proto3

package chesscom.payments.v1;

enum ChargePlatform {
  CHARGE_PLATFORM_UNSPECIFIED = 0;
  CHARGE_PLATFORM_WEB = 1;
  CHARGE_PLATFORM_APPLE = 2;
  CHARGE_PLATFORM_GOOGLE = 3;
}

message Charge {
  optional string charge_id = 1;
  optional int32 amount_cents = 2;
  optional string currency = 3;
  optional .google.protobuf.Timestamp charged_at = 4;
  o
```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06328, FND-06329

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06328"></a>
## FND-06328: chesscom.payments.v1.ChargePlatform.CHARGE_PLATFORM_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHARGE_PLATFORM_UNSPECIFIED = 0;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 119.

```text
/payments/v1/charge.proto
// syntax: proto3

package chesscom.payments.v1;

enum ChargePlatform {
  CHARGE_PLATFORM_UNSPECIFIED = 0;
  CHARGE_PLATFORM_WEB = 1;
  CHARGE_PLATFORM_APPLE = 2;
  CHARGE_PLATFORM_GOOGLE = 3;
}

message Charge {
  optional string charge_id = 1;
  optional int32 amount_cents = 2;
  optional string currency = 3;
  optional .google.protobuf.Timestamp charged_at = 4;
  optional string gateway =
```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06329

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06329"></a>
## FND-06329: chesscom.payments.v1.ChargePlatform.CHARGE_PLATFORM_WEB = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHARGE_PLATFORM_WEB = 1;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 154.

```text
: proto3

package chesscom.payments.v1;

enum ChargePlatform {
  CHARGE_PLATFORM_UNSPECIFIED = 0;
  CHARGE_PLATFORM_WEB = 1;
  CHARGE_PLATFORM_APPLE = 2;
  CHARGE_PLATFORM_GOOGLE = 3;
}

message Charge {
  optional string charge_id = 1;
  optional int32 amount_cents = 2;
  optional string currency = 3;
  optional .google.protobuf.Timestamp charged_at = 4;
  optional string gateway = 5;
  optional string payment_metho
```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06330"></a>
## FND-06330: chesscom.payments.v1.ChargePlatform.CHARGE_PLATFORM_APPLE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHARGE_PLATFORM_APPLE = 2;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 181.

```text
payments.v1;

enum ChargePlatform {
  CHARGE_PLATFORM_UNSPECIFIED = 0;
  CHARGE_PLATFORM_WEB = 1;
  CHARGE_PLATFORM_APPLE = 2;
  CHARGE_PLATFORM_GOOGLE = 3;
}

message Charge {
  optional string charge_id = 1;
  optional int32 amount_cents = 2;
  optional string currency = 3;
  optional .google.protobuf.Timestamp charged_at = 4;
  optional string gateway = 5;
  optional string payment_method = 6;
  optional .chesscom
```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06331"></a>
## FND-06331: chesscom.payments.v1.ChargePlatform.CHARGE_PLATFORM_GOOGLE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHARGE_PLATFORM_GOOGLE = 3;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 210.

```text
form {
  CHARGE_PLATFORM_UNSPECIFIED = 0;
  CHARGE_PLATFORM_WEB = 1;
  CHARGE_PLATFORM_APPLE = 2;
  CHARGE_PLATFORM_GOOGLE = 3;
}

message Charge {
  optional string charge_id = 1;
  optional int32 amount_cents = 2;
  optional string currency = 3;
  optional .google.protobuf.Timestamp charged_at = 4;
  optional string gateway = 5;
  optional string payment_method = 6;
  optional .chesscom.payments.v1.ChargePlatform p
```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06332"></a>
## FND-06332: message declaration: chesscom.payments.v1.Charge

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Charge {

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 241.

```text
IFIED = 0;
  CHARGE_PLATFORM_WEB = 1;
  CHARGE_PLATFORM_APPLE = 2;
  CHARGE_PLATFORM_GOOGLE = 3;
}

message Charge {
  optional string charge_id = 1;
  optional int32 amount_cents = 2;
  optional string currency = 3;
  optional .google.protobuf.Timestamp charged_at = 4;
  optional string gateway = 5;
  optional string payment_method = 6;
  optional .chesscom.payments.v1.ChargePlatform platform = 7;
  optional int32 r
```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06333"></a>
## FND-06333: chesscom.payments.v1.Charge.charge_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string charge_id = 1;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 260.

```text
_PLATFORM_WEB = 1;
  CHARGE_PLATFORM_APPLE = 2;
  CHARGE_PLATFORM_GOOGLE = 3;
}

message Charge {
  optional string charge_id = 1;
  optional int32 amount_cents = 2;
  optional string currency = 3;
  optional .google.protobuf.Timestamp charged_at = 4;
  optional string gateway = 5;
  optional string payment_method = 6;
  optional .chesscom.payments.v1.ChargePlatform platform = 7;
  optional int32 refunded_cents = 8;

```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06334"></a>
## FND-06334: chesscom.payments.v1.Charge.amount_cents = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 amount_cents = 2;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 293.

```text
ORM_APPLE = 2;
  CHARGE_PLATFORM_GOOGLE = 3;
}

message Charge {
  optional string charge_id = 1;
  optional int32 amount_cents = 2;
  optional string currency = 3;
  optional .google.protobuf.Timestamp charged_at = 4;
  optional string gateway = 5;
  optional string payment_method = 6;
  optional .chesscom.payments.v1.ChargePlatform platform = 7;
  optional int32 refunded_cents = 8;
  optional bool is_trial = 9;
  o
```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06335"></a>
## FND-06335: chesscom.payments.v1.Charge.currency = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string currency = 3;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 328.

```text
OGLE = 3;
}

message Charge {
  optional string charge_id = 1;
  optional int32 amount_cents = 2;
  optional string currency = 3;
  optional .google.protobuf.Timestamp charged_at = 4;
  optional string gateway = 5;
  optional string payment_method = 6;
  optional .chesscom.payments.v1.ChargePlatform platform = 7;
  optional int32 refunded_cents = 8;
  optional bool is_trial = 9;
  optional string plan = 10;
  optiona
```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06336"></a>
## FND-06336: chesscom.payments.v1.Charge.charged_at = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp charged_at = 4;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 360.

```text
optional string charge_id = 1;
  optional int32 amount_cents = 2;
  optional string currency = 3;
  optional .google.protobuf.Timestamp charged_at = 4;
  optional string gateway = 5;
  optional string payment_method = 6;
  optional .chesscom.payments.v1.ChargePlatform platform = 7;
  optional int32 refunded_cents = 8;
  optional bool is_trial = 9;
  optional string plan = 10;
  optional string subscription_id = 11;
 
```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06337"></a>
## FND-06337: chesscom.payments.v1.Charge.gateway = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string gateway = 5;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 414.

```text
_cents = 2;
  optional string currency = 3;
  optional .google.protobuf.Timestamp charged_at = 4;
  optional string gateway = 5;
  optional string payment_method = 6;
  optional .chesscom.payments.v1.ChargePlatform platform = 7;
  optional int32 refunded_cents = 8;
  optional bool is_trial = 9;
  optional string plan = 10;
  optional string subscription_id = 11;
  optional bool auto_refund_eligible = 12;
  optional .
```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06338"></a>
## FND-06338: chesscom.payments.v1.Charge.payment_method = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string payment_method = 6;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 445.

```text
urrency = 3;
  optional .google.protobuf.Timestamp charged_at = 4;
  optional string gateway = 5;
  optional string payment_method = 6;
  optional .chesscom.payments.v1.ChargePlatform platform = 7;
  optional int32 refunded_cents = 8;
  optional bool is_trial = 9;
  optional string plan = 10;
  optional string subscription_id = 11;
  optional bool auto_refund_eligible = 12;
  optional .chesscom.support.v1.RefundIneli
```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06339"></a>
## FND-06339: chesscom.payments.v1.Charge.platform = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.ChargePlatform platform = 7;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 483.

```text
uf.Timestamp charged_at = 4;
  optional string gateway = 5;
  optional string payment_method = 6;
  optional .chesscom.payments.v1.ChargePlatform platform = 7;
  optional int32 refunded_cents = 8;
  optional bool is_trial = 9;
  optional string plan = 10;
  optional string subscription_id = 11;
  optional bool auto_refund_eligible = 12;
  optional .chesscom.support.v1.RefundIneligibilityReason ineligibility_reason = 
```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06340"></a>
## FND-06340: chesscom.payments.v1.Charge.refunded_cents = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 refunded_cents = 8;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 545.

```text
optional string payment_method = 6;
  optional .chesscom.payments.v1.ChargePlatform platform = 7;
  optional int32 refunded_cents = 8;
  optional bool is_trial = 9;
  optional string plan = 10;
  optional string subscription_id = 11;
  optional bool auto_refund_eligible = 12;
  optional .chesscom.support.v1.RefundIneligibilityReason ineligibility_reason = 13;
}

```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06341"></a>
## FND-06341: chesscom.payments.v1.Charge.is_trial = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_trial = 9;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 582.

```text
 optional .chesscom.payments.v1.ChargePlatform platform = 7;
  optional int32 refunded_cents = 8;
  optional bool is_trial = 9;
  optional string plan = 10;
  optional string subscription_id = 11;
  optional bool auto_refund_eligible = 12;
  optional .chesscom.support.v1.RefundIneligibilityReason ineligibility_reason = 13;
}

```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06342"></a>
## FND-06342: chesscom.payments.v1.Charge.plan = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string plan = 10;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 612.

```text
1.ChargePlatform platform = 7;
  optional int32 refunded_cents = 8;
  optional bool is_trial = 9;
  optional string plan = 10;
  optional string subscription_id = 11;
  optional bool auto_refund_eligible = 12;
  optional .chesscom.support.v1.RefundIneligibilityReason ineligibility_reason = 13;
}

```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06343"></a>
## FND-06343: chesscom.payments.v1.Charge.subscription_id = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string subscription_id = 11;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 641.

```text
;
  optional int32 refunded_cents = 8;
  optional bool is_trial = 9;
  optional string plan = 10;
  optional string subscription_id = 11;
  optional bool auto_refund_eligible = 12;
  optional .chesscom.support.v1.RefundIneligibilityReason ineligibility_reason = 13;
}

```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06344"></a>
## FND-06344: chesscom.payments.v1.Charge.auto_refund_eligible = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool auto_refund_eligible = 12;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 681.

```text
 optional bool is_trial = 9;
  optional string plan = 10;
  optional string subscription_id = 11;
  optional bool auto_refund_eligible = 12;
  optional .chesscom.support.v1.RefundIneligibilityReason ineligibility_reason = 13;
}

```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06345"></a>
## FND-06345: chesscom.payments.v1.Charge.ineligibility_reason = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.RefundIneligibilityReason ineligibility_reason = 13;

### Evidence

- **SRC-0483** `research/proto/chesscom/payments/v1/charge.proto` — [preserved redacted evidence](../evidence/text/9d7bd34bb0f28d5af1946541b96e8d9d7c333d99ee60591f8c226158eaf41945.proto)
  Character offset 724.

```text
ing plan = 10;
  optional string subscription_id = 11;
  optional bool auto_refund_eligible = 12;
  optional .chesscom.support.v1.RefundIneligibilityReason ineligibility_reason = 13;
}

```

**Source references:** SRC-0483, SRC-1454  
**URL references:** None independently associated  
**Related findings:** FND-06327, FND-06328, FND-06329

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06346"></a>
## FND-06346: message declaration: chesscom.payments.v1.GetTotalBySkuRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetTotalBySkuRequest {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 105.

```text
urce: chesscom/payments/v1/checkout_service.proto
// syntax: proto3

package chesscom.payments.v1;

message GetTotalBySkuRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06347"></a>
## FND-06347: oneof declaration: chesscom.payments.v1.GetTotalBySkuRequest._coupon_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _coupon_code {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 138.

```text
ut_service.proto
// syntax: proto3

package chesscom.payments.v1;

message GetTotalBySkuRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.P
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06348"></a>
## FND-06348: chesscom.payments.v1.GetTotalBySkuRequest.coupon_code = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string coupon_code = 2;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 161.

```text
tax: proto3

package chesscom.payments.v1;

message GetTotalBySkuRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
 
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06349"></a>
## FND-06349: oneof declaration: chesscom.payments.v1.GetTotalBySkuRequest._request_location

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _request_location {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 191.

```text
payments.v1;

message GetTotalBySkuRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;

```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06350"></a>
## FND-06350: chesscom.payments.v1.GetTotalBySkuRequest.request_location = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.RequestLocation request_location = 3;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 219.

```text
alBySkuRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;
}

message GetTotalBySkuResp
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06351"></a>
## FND-06351: oneof declaration: chesscom.payments.v1.GetTotalBySkuRequest._payment_target

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _payment_target {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 285.

```text
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;
}

message GetTotalBySkuResponse {
  optional .chesscom.payments.v1.CheckoutTotal checkout_tot
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06352"></a>
## FND-06352: chesscom.payments.v1.GetTotalBySkuRequest.payment_target = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.PaymentTarget payment_target = 4;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 311.

```text
ion {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;
}

message GetTotalBySkuResponse {
  optional .chesscom.payments.v1.CheckoutTotal checkout_total = 1;
}

message GetTota
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06353"></a>
## FND-06353: oneof declaration: chesscom.payments.v1.GetTotalBySkuRequest._offer_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _offer_id {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 373.

```text
 = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;
}

message GetTotalBySkuResponse {
  optional .chesscom.payments.v1.CheckoutTotal checkout_total = 1;
}

message GetTotalBySkuListRequest {
  oneof _coupon_code {
  string coupon_cod
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06354"></a>
## FND-06354: chesscom.payments.v1.GetTotalBySkuRequest.offer_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string offer_id = 5;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 393.

```text
ayment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;
}

message GetTotalBySkuResponse {
  optional .chesscom.payments.v1.CheckoutTotal checkout_total = 1;
}

message GetTotalBySkuListRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06355"></a>
## FND-06355: oneof declaration: chesscom.payments.v1.GetTotalBySkuRequest._platform

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _platform {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 420.

```text
.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;
}

message GetTotalBySkuResponse {
  optional .chesscom.payments.v1.CheckoutTotal checkout_total = 1;
}

message GetTotalBySkuListRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chess
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06356"></a>
## FND-06356: chesscom.payments.v1.GetTotalBySkuRequest.platform = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.Platform platform = 6;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 440.

```text
Target payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;
}

message GetTotalBySkuResponse {
  optional .chesscom.payments.v1.CheckoutTotal checkout_total = 1;
}

message GetTotalBySkuListRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.Requ
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06357"></a>
## FND-06357: chesscom.payments.v1.GetTotalBySkuRequest.sku = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string sku = 1;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 486.

```text
id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;
}

message GetTotalBySkuResponse {
  optional .chesscom.payments.v1.CheckoutTotal checkout_total = 1;
}

message GetTotalBySkuListRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof 
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06358"></a>
## FND-06358: message declaration: chesscom.payments.v1.GetTotalBySkuResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetTotalBySkuResponse {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 514.

```text
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;
}

message GetTotalBySkuResponse {
  optional .chesscom.payments.v1.CheckoutTotal checkout_total = 1;
}

message GetTotalBySkuListRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chessco
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06359"></a>
## FND-06359: chesscom.payments.v1.GetTotalBySkuResponse.checkout_total = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.CheckoutTotal checkout_total = 1;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 548.

```text
m.api.v1.Platform platform = 6;
  }
  optional string sku = 1;
}

message GetTotalBySkuResponse {
  optional .chesscom.payments.v1.CheckoutTotal checkout_total = 1;
}

message GetTotalBySkuListRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget paymen
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06360"></a>
## FND-06360: message declaration: chesscom.payments.v1.GetTotalBySkuListRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetTotalBySkuListRequest {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 616.

```text
ssage GetTotalBySkuResponse {
  optional .chesscom.payments.v1.CheckoutTotal checkout_total = 1;
}

message GetTotalBySkuListRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  repeated string sku = 1;
}

message GetTotalBySk
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06361"></a>
## FND-06361: oneof declaration: chesscom.payments.v1.GetTotalBySkuListRequest._coupon_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _coupon_code {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 138.

```text
ut_service.proto
// syntax: proto3

package chesscom.payments.v1;

message GetTotalBySkuRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.P
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06362"></a>
## FND-06362: chesscom.payments.v1.GetTotalBySkuListRequest.coupon_code = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string coupon_code = 2;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 161.

```text
tax: proto3

package chesscom.payments.v1;

message GetTotalBySkuRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
 
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06363"></a>
## FND-06363: oneof declaration: chesscom.payments.v1.GetTotalBySkuListRequest._request_location

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _request_location {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 191.

```text
payments.v1;

message GetTotalBySkuRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;

```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06364"></a>
## FND-06364: chesscom.payments.v1.GetTotalBySkuListRequest.request_location = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.RequestLocation request_location = 3;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 219.

```text
alBySkuRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;
}

message GetTotalBySkuResp
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06365"></a>
## FND-06365: oneof declaration: chesscom.payments.v1.GetTotalBySkuListRequest._payment_target

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _payment_target {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 285.

```text
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;
}

message GetTotalBySkuResponse {
  optional .chesscom.payments.v1.CheckoutTotal checkout_tot
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06366"></a>
## FND-06366: chesscom.payments.v1.GetTotalBySkuListRequest.payment_target = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.PaymentTarget payment_target = 4;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 311.

```text
ion {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;
}

message GetTotalBySkuResponse {
  optional .chesscom.payments.v1.CheckoutTotal checkout_total = 1;
}

message GetTota
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06367"></a>
## FND-06367: chesscom.payments.v1.GetTotalBySkuListRequest.sku = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string sku = 1;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 888.

```text
 = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  repeated string sku = 1;
}

message GetTotalBySkuListResponse {
  repeated .chesscom.payments.v1.CheckoutTotal checkout_total = 1;
}

message GetStorefrontDetailsRequest {
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 1;
  }
}

message GetStorefrontDetailsResponse {
  oneof _mem
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06368"></a>
## FND-06368: message declaration: chesscom.payments.v1.GetTotalBySkuListResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetTotalBySkuListResponse {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 916.

```text
arget {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  repeated string sku = 1;
}

message GetTotalBySkuListResponse {
  repeated .chesscom.payments.v1.CheckoutTotal checkout_total = 1;
}

message GetStorefrontDetailsRequest {
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 1;
  }
}

message GetStorefrontDetailsResponse {
  oneof _membership_level {
  .chesscom.
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06369"></a>
## FND-06369: chesscom.payments.v1.GetTotalBySkuListResponse.checkout_total = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.CheckoutTotal checkout_total = 1;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 954.

```text
tTarget payment_target = 4;
  }
  repeated string sku = 1;
}

message GetTotalBySkuListResponse {
  repeated .chesscom.payments.v1.CheckoutTotal checkout_total = 1;
}

message GetStorefrontDetailsRequest {
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 1;
  }
}

message GetStorefrontDetailsResponse {
  oneof _membership_level {
  .chesscom.payments.v1.MembershipLevel membership
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06370"></a>
## FND-06370: message declaration: chesscom.payments.v1.GetStorefrontDetailsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetStorefrontDetailsRequest {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 1022.

```text
e GetTotalBySkuListResponse {
  repeated .chesscom.payments.v1.CheckoutTotal checkout_total = 1;
}

message GetStorefrontDetailsRequest {
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 1;
  }
}

message GetStorefrontDetailsResponse {
  oneof _membership_level {
  .chesscom.payments.v1.MembershipLevel membership_level = 2;
  }
  optional .chesscom.payments.v1.StorefrontCountry s
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06371"></a>
## FND-06371: oneof declaration: chesscom.payments.v1.GetStorefrontDetailsRequest._request_location

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _request_location {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 191.

```text
payments.v1;

message GetTotalBySkuRequest {
  oneof _coupon_code {
  string coupon_code = 2;
  }
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 3;
  }
  oneof _payment_target {
  .chesscom.payments.v1.PaymentTarget payment_target = 4;
  }
  oneof _offer_id {
  string offer_id = 5;
  }
  oneof _platform {
  .chesscom.api.v1.Platform platform = 6;
  }
  optional string sku = 1;

```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06372"></a>
## FND-06372: chesscom.payments.v1.GetStorefrontDetailsRequest.request_location = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.RequestLocation request_location = 1;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 1090.

```text
outTotal checkout_total = 1;
}

message GetStorefrontDetailsRequest {
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 1;
  }
}

message GetStorefrontDetailsResponse {
  oneof _membership_level {
  .chesscom.payments.v1.MembershipLevel membership_level = 2;
  }
  optional .chesscom.payments.v1.StorefrontCountry storefront_country = 1;
}

message GetAvailablePaymentMethodsRequest 
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06373"></a>
## FND-06373: message declaration: chesscom.payments.v1.GetStorefrontDetailsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetStorefrontDetailsResponse {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 1157.

```text
 {
  oneof _request_location {
  .chesscom.payments.v1.RequestLocation request_location = 1;
  }
}

message GetStorefrontDetailsResponse {
  oneof _membership_level {
  .chesscom.payments.v1.MembershipLevel membership_level = 2;
  }
  optional .chesscom.payments.v1.StorefrontCountry storefront_country = 1;
}

message GetAvailablePaymentMethodsRequest {
  oneof _coupon_code {
  string coupon_code = 3;
  }
  optional s
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06374"></a>
## FND-06374: oneof declaration: chesscom.payments.v1.GetStorefrontDetailsResponse._membership_level

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _membership_level {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 1198.

```text
m.payments.v1.RequestLocation request_location = 1;
  }
}

message GetStorefrontDetailsResponse {
  oneof _membership_level {
  .chesscom.payments.v1.MembershipLevel membership_level = 2;
  }
  optional .chesscom.payments.v1.StorefrontCountry storefront_country = 1;
}

message GetAvailablePaymentMethodsRequest {
  oneof _coupon_code {
  string coupon_code = 3;
  }
  optional string sku = 1;
  optional .chesscom.payme
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
