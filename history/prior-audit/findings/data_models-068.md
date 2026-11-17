# data_models — findings 6701–6800

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-06975"></a>
## FND-06975: chesscom.payments.v1.FindChargesRequest.user_uuid = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 7;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 995.

```text
ng apple_transaction_id = 3;
  string apple_order_id = 5;
  string chesscom_order_number = 6;
  }
  optional string user_uuid = 7;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message FindChargesResponse {
  repeated .chesscom.payments.v1.FoundCharge charges = 1;
  optional bool privacy_withheld = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
}

message ListSubscrip
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06976"></a>
## FND-06976: chesscom.payments.v1.FindChargesRequest.context = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionContext context = 4;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 1028.

```text
ring apple_order_id = 5;
  string chesscom_order_number = 6;
  }
  optional string user_uuid = 7;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message FindChargesResponse {
  repeated .chesscom.payments.v1.FoundCharge charges = 1;
  optional bool privacy_withheld = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
}

message ListSubscriptionsRequest {
  optional string 
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06977"></a>
## FND-06977: message declaration: chesscom.payments.v1.FindChargesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FindChargesResponse {

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 1095.

```text
optional string user_uuid = 7;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message FindChargesResponse {
  repeated .chesscom.payments.v1.FoundCharge charges = 1;
  optional bool privacy_withheld = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
}

message ListSubscriptionsRequest {
  optional string user_uuid = 1;
}

message ListSubscriptionsResponse {
  repeated .c
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06978"></a>
## FND-06978: chesscom.payments.v1.FindChargesResponse.charges = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.FoundCharge charges = 1;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 1127.

```text
 optional .chesscom.support.v1.SupportActionContext context = 4;
}

message FindChargesResponse {
  repeated .chesscom.payments.v1.FoundCharge charges = 1;
  optional bool privacy_withheld = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
}

message ListSubscriptionsRequest {
  optional string user_uuid = 1;
}

message ListSubscriptionsResponse {
  repeated .chesscom.payments.v1.MemberSubscr
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06979"></a>
## FND-06979: chesscom.payments.v1.FindChargesResponse.privacy_withheld = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool privacy_withheld = 2;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 1185.

```text
t = 4;
}

message FindChargesResponse {
  repeated .chesscom.payments.v1.FoundCharge charges = 1;
  optional bool privacy_withheld = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
}

message ListSubscriptionsRequest {
  optional string user_uuid = 1;
}

message ListSubscriptionsResponse {
  repeated .chesscom.payments.v1.MemberSubscription subscriptions = 1;
}

```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06980"></a>
## FND-06980: chesscom.payments.v1.FindChargesResponse.action_result = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionResult action_result = 3;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 486.

```text
 IssueRefundResponse {
  optional bool already_refunded = 1;
  optional int32 refunded_cents = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
  optional string refund_id = 4;
}

message ListChargesRequest {
  optional string user_uuid = 1;
  optional int32 limit = 2;
}

message ListChargesResponse {
  repeated .chesscom.payments.v1.Charge charges = 1;
}

message FindChargesRequest {
  oneof
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06981"></a>
## FND-06981: message declaration: chesscom.payments.v1.ListSubscriptionsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListSubscriptionsRequest {

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 1295.

```text
ool privacy_withheld = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
}

message ListSubscriptionsRequest {
  optional string user_uuid = 1;
}

message ListSubscriptionsResponse {
  repeated .chesscom.payments.v1.MemberSubscription subscriptions = 1;
}

```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06982"></a>
## FND-06982: chesscom.payments.v1.ListSubscriptionsRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 134.

```text
fund_service.proto
// syntax: proto3

package chesscom.payments.v1;

message IssueRefundRequest {
  optional string user_uuid = 1;
  optional string charge_id = 2;
  optional int32 amount_cents = 4;
  optional .chesscom.support.v1.SupportActionContext context = 6;
  optional .chesscom.payments.v1.CancellationEffect cancellation_effect = 8;
}

message IssueRefundResponse {
  optional bool already_refunded = 1;
  optio
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06983"></a>
## FND-06983: message declaration: chesscom.payments.v1.ListSubscriptionsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListSubscriptionsResponse {

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 1366.

```text
Result action_result = 3;
}

message ListSubscriptionsRequest {
  optional string user_uuid = 1;
}

message ListSubscriptionsResponse {
  repeated .chesscom.payments.v1.MemberSubscription subscriptions = 1;
}

```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06984"></a>
## FND-06984: chesscom.payments.v1.ListSubscriptionsResponse.subscriptions = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.MemberSubscription subscriptions = 1;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 1404.

```text
istSubscriptionsRequest {
  optional string user_uuid = 1;
}

message ListSubscriptionsResponse {
  repeated .chesscom.payments.v1.MemberSubscription subscriptions = 1;
}

```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06985"></a>
## FND-06985: message declaration: chesscom.payments.v1.RequestLocation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RequestLocation {

### Evidence

- **SRC-0508** `research/proto/chesscom/payments/v1/request_location.proto` — [preserved redacted evidence](../evidence/text/48209b37e4c21454459018e37c76732ee10b333cda5f42572f761d5638d1186d.proto)
  Character offset 105.

```text
urce: chesscom/payments/v1/request_location.proto
// syntax: proto3

package chesscom.payments.v1;

message RequestLocation {
  oneof _zip_code {
  string zip_code = 1;
  }
  oneof _region {
  string region = 2;
  }
}

```

**Source references:** SRC-0508, SRC-1479  
**URL references:** None independently associated  
**Related findings:** FND-06986, FND-06987

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06986"></a>
## FND-06986: oneof declaration: chesscom.payments.v1.RequestLocation._zip_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _zip_code {

### Evidence

- **SRC-0508** `research/proto/chesscom/payments/v1/request_location.proto` — [preserved redacted evidence](../evidence/text/48209b37e4c21454459018e37c76732ee10b333cda5f42572f761d5638d1186d.proto)
  Character offset 133.

```text
equest_location.proto
// syntax: proto3

package chesscom.payments.v1;

message RequestLocation {
  oneof _zip_code {
  string zip_code = 1;
  }
  oneof _region {
  string region = 2;
  }
}

```

**Source references:** SRC-0508, SRC-1479  
**URL references:** None independently associated  
**Related findings:** FND-06985, FND-06987

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06987"></a>
## FND-06987: chesscom.payments.v1.RequestLocation.zip_code = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string zip_code = 1;

### Evidence

- **SRC-0508** `research/proto/chesscom/payments/v1/request_location.proto` — [preserved redacted evidence](../evidence/text/48209b37e4c21454459018e37c76732ee10b333cda5f42572f761d5638d1186d.proto)
  Character offset 153.

```text
o
// syntax: proto3

package chesscom.payments.v1;

message RequestLocation {
  oneof _zip_code {
  string zip_code = 1;
  }
  oneof _region {
  string region = 2;
  }
}

```

**Source references:** SRC-0508, SRC-1479  
**URL references:** None independently associated  
**Related findings:** FND-06985, FND-06986

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06988"></a>
## FND-06988: oneof declaration: chesscom.payments.v1.RequestLocation._region

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _region {

### Evidence

- **SRC-0508** `research/proto/chesscom/payments/v1/request_location.proto` — [preserved redacted evidence](../evidence/text/48209b37e4c21454459018e37c76732ee10b333cda5f42572f761d5638d1186d.proto)
  Character offset 180.

```text
e chesscom.payments.v1;

message RequestLocation {
  oneof _zip_code {
  string zip_code = 1;
  }
  oneof _region {
  string region = 2;
  }
}

```

**Source references:** SRC-0508, SRC-1479  
**URL references:** None independently associated  
**Related findings:** FND-06985, FND-06986, FND-06987

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06989"></a>
## FND-06989: chesscom.payments.v1.RequestLocation.region = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string region = 2;

### Evidence

- **SRC-0508** `research/proto/chesscom/payments/v1/request_location.proto` — [preserved redacted evidence](../evidence/text/48209b37e4c21454459018e37c76732ee10b333cda5f42572f761d5638d1186d.proto)
  Character offset 198.

```text
s.v1;

message RequestLocation {
  oneof _zip_code {
  string zip_code = 1;
  }
  oneof _region {
  string region = 2;
  }
}

```

**Source references:** SRC-0508, SRC-1479  
**URL references:** None independently associated  
**Related findings:** FND-06985, FND-06986, FND-06987

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06990"></a>
## FND-06990: message declaration: chesscom.payments.v1.StorefrontCountry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StorefrontCountry {

### Evidence

- **SRC-0509** `research/proto/chesscom/payments/v1/storefront_country.proto` — [preserved redacted evidence](../evidence/text/17e015796ab9eb574b8854bbf454f7a92dd149b4817de15b018b5ab7b9dd8e22.proto)
  Character offset 107.

```text
ce: chesscom/payments/v1/storefront_country.proto
// syntax: proto3

package chesscom.payments.v1;

message StorefrontCountry {
  optional string country_code = 1;
  optional string currency_code = 2;
  optional bool tax_inclusive_prices = 3;
  optional bool should_display_checkout_disclaimer = 4;
}

```

**Source references:** SRC-0509, SRC-1480  
**URL references:** None independently associated  
**Related findings:** FND-06991, FND-06992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06991"></a>
## FND-06991: chesscom.payments.v1.StorefrontCountry.country_code = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string country_code = 1;

### Evidence

- **SRC-0509** `research/proto/chesscom/payments/v1/storefront_country.proto` — [preserved redacted evidence](../evidence/text/17e015796ab9eb574b8854bbf454f7a92dd149b4817de15b018b5ab7b9dd8e22.proto)
  Character offset 137.

```text
front_country.proto
// syntax: proto3

package chesscom.payments.v1;

message StorefrontCountry {
  optional string country_code = 1;
  optional string currency_code = 2;
  optional bool tax_inclusive_prices = 3;
  optional bool should_display_checkout_disclaimer = 4;
}

```

**Source references:** SRC-0509, SRC-1480  
**URL references:** None independently associated  
**Related findings:** FND-06990, FND-06992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06992"></a>
## FND-06992: chesscom.payments.v1.StorefrontCountry.currency_code = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string currency_code = 2;

### Evidence

- **SRC-0509** `research/proto/chesscom/payments/v1/storefront_country.proto` — [preserved redacted evidence](../evidence/text/17e015796ab9eb574b8854bbf454f7a92dd149b4817de15b018b5ab7b9dd8e22.proto)
  Character offset 173.

```text
3

package chesscom.payments.v1;

message StorefrontCountry {
  optional string country_code = 1;
  optional string currency_code = 2;
  optional bool tax_inclusive_prices = 3;
  optional bool should_display_checkout_disclaimer = 4;
}

```

**Source references:** SRC-0509, SRC-1480  
**URL references:** None independently associated  
**Related findings:** FND-06990, FND-06991

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06993"></a>
## FND-06993: chesscom.payments.v1.StorefrontCountry.tax_inclusive_prices = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool tax_inclusive_prices = 3;

### Evidence

- **SRC-0509** `research/proto/chesscom/payments/v1/storefront_country.proto` — [preserved redacted evidence](../evidence/text/17e015796ab9eb574b8854bbf454f7a92dd149b4817de15b018b5ab7b9dd8e22.proto)
  Character offset 210.

```text
sage StorefrontCountry {
  optional string country_code = 1;
  optional string currency_code = 2;
  optional bool tax_inclusive_prices = 3;
  optional bool should_display_checkout_disclaimer = 4;
}

```

**Source references:** SRC-0509, SRC-1480  
**URL references:** None independently associated  
**Related findings:** FND-06990, FND-06991, FND-06992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06994"></a>
## FND-06994: chesscom.payments.v1.StorefrontCountry.should_display_checkout_disclaimer = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool should_display_checkout_disclaimer = 4;

### Evidence

- **SRC-0509** `research/proto/chesscom/payments/v1/storefront_country.proto` — [preserved redacted evidence](../evidence/text/17e015796ab9eb574b8854bbf454f7a92dd149b4817de15b018b5ab7b9dd8e22.proto)
  Character offset 252.

```text
 country_code = 1;
  optional string currency_code = 2;
  optional bool tax_inclusive_prices = 3;
  optional bool should_display_checkout_disclaimer = 4;
}

```

**Source references:** SRC-0509, SRC-1480  
**URL references:** None independently associated  
**Related findings:** FND-06990, FND-06991, FND-06992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06995"></a>
## FND-06995: message declaration: chesscom.payments.v1.Subscription

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Subscription {

### Evidence

- **SRC-0510** `research/proto/chesscom/payments/v1/subscription.proto` — [preserved redacted evidence](../evidence/text/ebbd2dc382a13c94e1e7ab618da0bda7ac757c74fa731a3ccb632e06711ce081.proto)
  Character offset 101.

```text
/ source: chesscom/payments/v1/subscription.proto
// syntax: proto3

package chesscom.payments.v1;

message Subscription {
  optional int32 length = 1;
  optional string unit = 2;
}

```

**Source references:** SRC-0510, SRC-1481  
**URL references:** None independently associated  
**Related findings:** FND-06996, FND-06997

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06996"></a>
## FND-06996: chesscom.payments.v1.Subscription.length = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 length = 1;

### Evidence

- **SRC-0510** `research/proto/chesscom/payments/v1/subscription.proto` — [preserved redacted evidence](../evidence/text/ebbd2dc382a13c94e1e7ab618da0bda7ac757c74fa731a3ccb632e06711ce081.proto)
  Character offset 126.

```text
ts/v1/subscription.proto
// syntax: proto3

package chesscom.payments.v1;

message Subscription {
  optional int32 length = 1;
  optional string unit = 2;
}

```

**Source references:** SRC-0510, SRC-1481  
**URL references:** None independently associated  
**Related findings:** FND-06995, FND-06997

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06997"></a>
## FND-06997: chesscom.payments.v1.Subscription.unit = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string unit = 2;

### Evidence

- **SRC-0510** `research/proto/chesscom/payments/v1/subscription.proto` — [preserved redacted evidence](../evidence/text/ebbd2dc382a13c94e1e7ab618da0bda7ac757c74fa731a3ccb632e06711ce081.proto)
  Character offset 155.

```text
yntax: proto3

package chesscom.payments.v1;

message Subscription {
  optional int32 length = 1;
  optional string unit = 2;
}

```

**Source references:** SRC-0510, SRC-1481  
**URL references:** None independently associated  
**Related findings:** FND-06995, FND-06996

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06998"></a>
## FND-06998: enum declaration: chesscom.payments.v1.CancelSubscriptionResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CancelSubscriptionResult {

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 107.

```text
ce: chesscom/payments/v1/subscription_admin.proto
// syntax: proto3

package chesscom.payments.v1;

enum CancelSubscriptionResult {
  CANCEL_SUBSCRIPTION_RESULT_UNSPECIFIED = 0;
  CANCEL_SUBSCRIPTION_RESULT_CANCELLED = 1;
  CANCEL_SUBSCRIPTION_RESULT_ALREADY_CANCELLED = 2;
}

enum SubscriptionAdminRefusalReason {
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_UNSPECIFIED = 0;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ACTIVE_SUBSCR
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06999"></a>
## FND-06999: chesscom.payments.v1.CancelSubscriptionResult.CANCEL_SUBSCRIPTION_RESULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCEL_SUBSCRIPTION_RESULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 141.

```text
ion_admin.proto
// syntax: proto3

package chesscom.payments.v1;

enum CancelSubscriptionResult {
  CANCEL_SUBSCRIPTION_RESULT_UNSPECIFIED = 0;
  CANCEL_SUBSCRIPTION_RESULT_CANCELLED = 1;
  CANCEL_SUBSCRIPTION_RESULT_ALREADY_CANCELLED = 2;
}

enum SubscriptionAdminRefusalReason {
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_UNSPECIFIED = 0;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ACTIVE_SUBSCRIPTION = 1;
  SUBSCRIPTION_ADMIN_R
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07000"></a>
## FND-07000: chesscom.payments.v1.CancelSubscriptionResult.CANCEL_SUBSCRIPTION_RESULT_CANCELLED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCEL_SUBSCRIPTION_RESULT_CANCELLED = 1;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 187.

```text
sscom.payments.v1;

enum CancelSubscriptionResult {
  CANCEL_SUBSCRIPTION_RESULT_UNSPECIFIED = 0;
  CANCEL_SUBSCRIPTION_RESULT_CANCELLED = 1;
  CANCEL_SUBSCRIPTION_RESULT_ALREADY_CANCELLED = 2;
}

enum SubscriptionAdminRefusalReason {
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_UNSPECIFIED = 0;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ACTIVE_SUBSCRIPTION = 1;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_STORE_BILLED_APPLE = 2;
  SUBSCR
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07001"></a>
## FND-07001: chesscom.payments.v1.CancelSubscriptionResult.CANCEL_SUBSCRIPTION_RESULT_ALREADY_CANCELLED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCEL_SUBSCRIPTION_RESULT_ALREADY_CANCELLED = 2;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 231.

```text
esult {
  CANCEL_SUBSCRIPTION_RESULT_UNSPECIFIED = 0;
  CANCEL_SUBSCRIPTION_RESULT_CANCELLED = 1;
  CANCEL_SUBSCRIPTION_RESULT_ALREADY_CANCELLED = 2;
}

enum SubscriptionAdminRefusalReason {
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_UNSPECIFIED = 0;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ACTIVE_SUBSCRIPTION = 1;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_STORE_BILLED_APPLE = 2;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_CAN
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07002"></a>
## FND-07002: enum declaration: chesscom.payments.v1.SubscriptionAdminRefusalReason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SubscriptionAdminRefusalReason {

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 284.

```text

  CANCEL_SUBSCRIPTION_RESULT_CANCELLED = 1;
  CANCEL_SUBSCRIPTION_RESULT_ALREADY_CANCELLED = 2;
}

enum SubscriptionAdminRefusalReason {
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_UNSPECIFIED = 0;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ACTIVE_SUBSCRIPTION = 1;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_STORE_BILLED_APPLE = 2;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_CANCELLED = 3;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_E
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07003"></a>
## FND-07003: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_UNSPECIFIED = 0;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 324.

```text
= 1;
  CANCEL_SUBSCRIPTION_RESULT_ALREADY_CANCELLED = 2;
}

enum SubscriptionAdminRefusalReason {
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_UNSPECIFIED = 0;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ACTIVE_SUBSCRIPTION = 1;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_STORE_BILLED_APPLE = 2;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_CANCELLED = 3;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_EXTENDABLE = 4;
  SUBSCRIPTION_ADMIN_REFU
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07004"></a>
## FND-07004: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ACTIVE_SUBSCRIPTION = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ACTIVE_SUBSCRIPTION = 1;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 377.

```text
 2;
}

enum SubscriptionAdminRefusalReason {
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_UNSPECIFIED = 0;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ACTIVE_SUBSCRIPTION = 1;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_STORE_BILLED_APPLE = 2;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_CANCELLED = 3;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_EXTENDABLE = 4;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_RECENTLY_EXTENDED = 5;
  SUBSCRIPTION_ADMI
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07005"></a>
## FND-07005: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_STORE_BILLED_APPLE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_STORE_BILLED_APPLE = 2;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 441.

```text
N_REFUSAL_REASON_UNSPECIFIED = 0;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ACTIVE_SUBSCRIPTION = 1;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_STORE_BILLED_APPLE = 2;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_CANCELLED = 3;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_EXTENDABLE = 4;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_RECENTLY_EXTENDED = 5;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SAME_ACCOUNT = 6;
  SUBSCRIPTION_ADMIN_REFUSAL_
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07006"></a>
## FND-07006: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_CANCELLED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_CANCELLED = 3;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 501.

```text
AL_REASON_NO_ACTIVE_SUBSCRIPTION = 1;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_STORE_BILLED_APPLE = 2;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_CANCELLED = 3;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_EXTENDABLE = 4;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_RECENTLY_EXTENDED = 5;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SAME_ACCOUNT = 6;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_TARGET_HAS_SUBSCRIPTION = 7;
  SUBSCRIPTION_ADMIN_REF
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07007"></a>
## FND-07007: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_EXTENDABLE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_EXTENDABLE = 4;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 565.

```text
AL_REASON_STORE_BILLED_APPLE = 2;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_CANCELLED = 3;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_EXTENDABLE = 4;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_RECENTLY_EXTENDED = 5;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SAME_ACCOUNT = 6;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_TARGET_HAS_SUBSCRIPTION = 7;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_HUMAN_CONFIRMATION_REQUIRED = 8;
  SUBSCRIPTION_ADMI
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07008"></a>
## FND-07008: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_RECENTLY_EXTENDED = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_RECENTLY_EXTENDED = 5;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 621.

```text
EFUSAL_REASON_SUBSCRIPTION_CANCELLED = 3;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_EXTENDABLE = 4;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_RECENTLY_EXTENDED = 5;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SAME_ACCOUNT = 6;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_TARGET_HAS_SUBSCRIPTION = 7;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_HUMAN_CONFIRMATION_REQUIRED = 8;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_MISMATCH = 9;
  SUBSCRIPTI
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07009"></a>
## FND-07009: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_SAME_ACCOUNT = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_SAME_ACCOUNT = 6;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 680.

```text
MIN_REFUSAL_REASON_NOT_EXTENDABLE = 4;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_RECENTLY_EXTENDED = 5;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SAME_ACCOUNT = 6;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_TARGET_HAS_SUBSCRIPTION = 7;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_HUMAN_CONFIRMATION_REQUIRED = 8;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_MISMATCH = 9;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_VERIFICATION_REQUIRED = 10;
  SUBSC
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07010"></a>
## FND-07010: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_TARGET_HAS_SUBSCRIPTION = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_TARGET_HAS_SUBSCRIPTION = 7;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 734.

```text
ADMIN_REFUSAL_REASON_RECENTLY_EXTENDED = 5;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SAME_ACCOUNT = 6;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_TARGET_HAS_SUBSCRIPTION = 7;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_HUMAN_CONFIRMATION_REQUIRED = 8;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_MISMATCH = 9;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_VERIFICATION_REQUIRED = 10;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_ELIGIBLE = 11;
  SUBS
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07011"></a>
## FND-07011: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_HUMAN_CONFIRMATION_REQUIRED = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_HUMAN_CONFIRMATION_REQUIRED = 8;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 799.

```text
REFUSAL_REASON_SAME_ACCOUNT = 6;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_TARGET_HAS_SUBSCRIPTION = 7;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_HUMAN_CONFIRMATION_REQUIRED = 8;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_MISMATCH = 9;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_VERIFICATION_REQUIRED = 10;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_ELIGIBLE = 11;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ALREADY_GRANTED = 12;
  SUBSCRIPTIO
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07012"></a>
## FND-07012: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_MISMATCH = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_MISMATCH = 9;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 868.

```text
TARGET_HAS_SUBSCRIPTION = 7;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_HUMAN_CONFIRMATION_REQUIRED = 8;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_MISMATCH = 9;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_VERIFICATION_REQUIRED = 10;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_ELIGIBLE = 11;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ALREADY_GRANTED = 12;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ORDER_NOT_PAID = 13;
  SUBSCRIPTION_ADMIN_REFU
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07013"></a>
## FND-07013: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_VERIFICATION_REQUIRED = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_VERIFICATION_REQUIRED = 10;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 931.

```text
N_HUMAN_CONFIRMATION_REQUIRED = 8;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_SUBSCRIPTION_MISMATCH = 9;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_VERIFICATION_REQUIRED = 10;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_ELIGIBLE = 11;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ALREADY_GRANTED = 12;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ORDER_NOT_PAID = 13;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_PARTNER_NOT_VERIFIED = 14;
  SUBSCRIPTION_ADMIN_REFU
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07014"></a>
## FND-07014: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_ELIGIBLE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_ELIGIBLE = 11;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 995.

```text
REASON_SUBSCRIPTION_MISMATCH = 9;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_VERIFICATION_REQUIRED = 10;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_ELIGIBLE = 11;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ALREADY_GRANTED = 12;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ORDER_NOT_PAID = 13;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_PARTNER_NOT_VERIFIED = 14;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_ALREADY_ACTIVE = 15;
  SUBSCRIPTION_ADMIN_REFU
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07015"></a>
## FND-07015: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_ALREADY_GRANTED = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_ALREADY_GRANTED = 12;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1050.

```text
REFUSAL_REASON_VERIFICATION_REQUIRED = 10;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_ELIGIBLE = 11;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ALREADY_GRANTED = 12;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ORDER_NOT_PAID = 13;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_PARTNER_NOT_VERIFIED = 14;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_ALREADY_ACTIVE = 15;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ACCOUNT_CLOSED = 16;
  SUBSCRIPTION_ADMIN_RE
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07016"></a>
## FND-07016: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_ORDER_NOT_PAID = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_ORDER_NOT_PAID = 13;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1108.

```text
ADMIN_REFUSAL_REASON_NOT_ELIGIBLE = 11;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ALREADY_GRANTED = 12;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ORDER_NOT_PAID = 13;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_PARTNER_NOT_VERIFIED = 14;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_ALREADY_ACTIVE = 15;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ACCOUNT_CLOSED = 16;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_NOT_ELIGIBLE = 17;
  SUBSCRIPTION_ADMI
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07017"></a>
## FND-07017: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_PARTNER_NOT_VERIFIED = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_PARTNER_NOT_VERIFIED = 14;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1165.

```text
MIN_REFUSAL_REASON_ALREADY_GRANTED = 12;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ORDER_NOT_PAID = 13;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_PARTNER_NOT_VERIFIED = 14;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_ALREADY_ACTIVE = 15;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ACCOUNT_CLOSED = 16;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_NOT_ELIGIBLE = 17;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ADS_OFFER_RECENTLY_GIVEN = 18;
  SUBS
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07018"></a>
## FND-07018: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_ALREADY_ACTIVE = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_ALREADY_ACTIVE = 15;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1228.

```text
EFUSAL_REASON_ORDER_NOT_PAID = 13;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_PARTNER_NOT_VERIFIED = 14;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_ALREADY_ACTIVE = 15;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ACCOUNT_CLOSED = 16;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_NOT_ELIGIBLE = 17;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ADS_OFFER_RECENTLY_GIVEN = 18;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_SWITCHABLE = 19;
}

enum Stop
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07019"></a>
## FND-07019: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_ACCOUNT_CLOSED = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_ACCOUNT_CLOSED = 16;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1292.

```text
REASON_PARTNER_NOT_VERIFIED = 14;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_ALREADY_ACTIVE = 15;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ACCOUNT_CLOSED = 16;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_NOT_ELIGIBLE = 17;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ADS_OFFER_RECENTLY_GIVEN = 18;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_SWITCHABLE = 19;
}

enum StopRenewalByCardMatchResult {
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_U
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07020"></a>
## FND-07020: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_NOT_ELIGIBLE = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_NOT_ELIGIBLE = 17;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1349.

```text
FUSAL_REASON_MEMBER_ALREADY_ACTIVE = 15;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_ACCOUNT_CLOSED = 16;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_NOT_ELIGIBLE = 17;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ADS_OFFER_RECENTLY_GIVEN = 18;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_SWITCHABLE = 19;
}

enum StopRenewalByCardMatchResult {
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_UNSPECIFIED = 0;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_RENEW
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07021"></a>
## FND-07021: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ADS_OFFER_RECENTLY_GIVEN = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ADS_OFFER_RECENTLY_GIVEN = 18;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1411.

```text
REFUSAL_REASON_ACCOUNT_CLOSED = 16;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_MEMBER_NOT_ELIGIBLE = 17;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ADS_OFFER_RECENTLY_GIVEN = 18;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_SWITCHABLE = 19;
}

enum StopRenewalByCardMatchResult {
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_UNSPECIFIED = 0;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_RENEWAL_STOPPED = 1;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NOT_RENEWI
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07022"></a>
## FND-07022: chesscom.payments.v1.SubscriptionAdminRefusalReason.SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_SWITCHABLE = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_SWITCHABLE = 19;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1481.

```text
N_MEMBER_NOT_ELIGIBLE = 17;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NO_ADS_OFFER_RECENTLY_GIVEN = 18;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_SWITCHABLE = 19;
}

enum StopRenewalByCardMatchResult {
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_UNSPECIFIED = 0;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_RENEWAL_STOPPED = 1;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NOT_RENEWING = 2;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_STORE_BILLED = 3;
  STOP_R
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07023"></a>
## FND-07023: enum declaration: chesscom.payments.v1.StopRenewalByCardMatchResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum StopRenewalByCardMatchResult {

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1539.

```text
EASON_NO_ADS_OFFER_RECENTLY_GIVEN = 18;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_SWITCHABLE = 19;
}

enum StopRenewalByCardMatchResult {
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_UNSPECIFIED = 0;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_RENEWAL_STOPPED = 1;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NOT_RENEWING = 2;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_STORE_BILLED = 3;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NO_MATCH = 4;
}

enum SwitchTo
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07024"></a>
## FND-07024: chesscom.payments.v1.StopRenewalByCardMatchResult.STOP_RENEWAL_BY_CARD_MATCH_RESULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STOP_RENEWAL_BY_CARD_MATCH_RESULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1577.

```text
;
  SUBSCRIPTION_ADMIN_REFUSAL_REASON_NOT_SWITCHABLE = 19;
}

enum StopRenewalByCardMatchResult {
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_UNSPECIFIED = 0;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_RENEWAL_STOPPED = 1;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NOT_RENEWING = 2;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_STORE_BILLED = 3;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NO_MATCH = 4;
}

enum SwitchToMonthlyResult {
  SWITCH_TO_MONTHLY_RE
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07025"></a>
## FND-07025: chesscom.payments.v1.StopRenewalByCardMatchResult.STOP_RENEWAL_BY_CARD_MATCH_RESULT_RENEWAL_STOPPED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STOP_RENEWAL_BY_CARD_MATCH_RESULT_RENEWAL_STOPPED = 1;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1630.

```text
= 19;
}

enum StopRenewalByCardMatchResult {
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_UNSPECIFIED = 0;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_RENEWAL_STOPPED = 1;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NOT_RENEWING = 2;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_STORE_BILLED = 3;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NO_MATCH = 4;
}

enum SwitchToMonthlyResult {
  SWITCH_TO_MONTHLY_RESULT_UNSPECIFIED = 0;
  SWITCH_TO_MONTHLY_RESULT_SWIT
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07026"></a>
## FND-07026: chesscom.payments.v1.StopRenewalByCardMatchResult.STOP_RENEWAL_BY_CARD_MATCH_RESULT_NOT_RENEWING = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STOP_RENEWAL_BY_CARD_MATCH_RESULT_NOT_RENEWING = 2;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1687.

```text
AL_BY_CARD_MATCH_RESULT_UNSPECIFIED = 0;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_RENEWAL_STOPPED = 1;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NOT_RENEWING = 2;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_STORE_BILLED = 3;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NO_MATCH = 4;
}

enum SwitchToMonthlyResult {
  SWITCH_TO_MONTHLY_RESULT_UNSPECIFIED = 0;
  SWITCH_TO_MONTHLY_RESULT_SWITCHED = 1;
  SWITCH_TO_MONTHLY_RESULT_SWITCH_PENDING_REFUN
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07027"></a>
## FND-07027: chesscom.payments.v1.StopRenewalByCardMatchResult.STOP_RENEWAL_BY_CARD_MATCH_RESULT_STORE_BILLED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STOP_RENEWAL_BY_CARD_MATCH_RESULT_STORE_BILLED = 3;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1741.

```text
L_BY_CARD_MATCH_RESULT_RENEWAL_STOPPED = 1;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NOT_RENEWING = 2;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_STORE_BILLED = 3;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NO_MATCH = 4;
}

enum SwitchToMonthlyResult {
  SWITCH_TO_MONTHLY_RESULT_UNSPECIFIED = 0;
  SWITCH_TO_MONTHLY_RESULT_SWITCHED = 1;
  SWITCH_TO_MONTHLY_RESULT_SWITCH_PENDING_REFUND = 2;
  SWITCH_TO_MONTHLY_RESULT_REFUNDED_NOT_SWITCHE
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07028"></a>
## FND-07028: chesscom.payments.v1.StopRenewalByCardMatchResult.STOP_RENEWAL_BY_CARD_MATCH_RESULT_NO_MATCH = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STOP_RENEWAL_BY_CARD_MATCH_RESULT_NO_MATCH = 4;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1795.

```text
EWAL_BY_CARD_MATCH_RESULT_NOT_RENEWING = 2;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_STORE_BILLED = 3;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NO_MATCH = 4;
}

enum SwitchToMonthlyResult {
  SWITCH_TO_MONTHLY_RESULT_UNSPECIFIED = 0;
  SWITCH_TO_MONTHLY_RESULT_SWITCHED = 1;
  SWITCH_TO_MONTHLY_RESULT_SWITCH_PENDING_REFUND = 2;
  SWITCH_TO_MONTHLY_RESULT_REFUNDED_NOT_SWITCHED = 3;
}

enum MonthlySwitchIneligibility {
  MONTHLY_
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07029"></a>
## FND-07029: enum declaration: chesscom.payments.v1.SwitchToMonthlyResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SwitchToMonthlyResult {

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1846.

```text
RENEWAL_BY_CARD_MATCH_RESULT_STORE_BILLED = 3;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NO_MATCH = 4;
}

enum SwitchToMonthlyResult {
  SWITCH_TO_MONTHLY_RESULT_UNSPECIFIED = 0;
  SWITCH_TO_MONTHLY_RESULT_SWITCHED = 1;
  SWITCH_TO_MONTHLY_RESULT_SWITCH_PENDING_REFUND = 2;
  SWITCH_TO_MONTHLY_RESULT_REFUNDED_NOT_SWITCHED = 3;
}

enum MonthlySwitchIneligibility {
  MONTHLY_SWITCH_INELIGIBILITY_UNSPECIFIED = 0;
  MONTHLY_SWI
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07030"></a>
## FND-07030: chesscom.payments.v1.SwitchToMonthlyResult.SWITCH_TO_MONTHLY_RESULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SWITCH_TO_MONTHLY_RESULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1877.

```text
ORE_BILLED = 3;
  STOP_RENEWAL_BY_CARD_MATCH_RESULT_NO_MATCH = 4;
}

enum SwitchToMonthlyResult {
  SWITCH_TO_MONTHLY_RESULT_UNSPECIFIED = 0;
  SWITCH_TO_MONTHLY_RESULT_SWITCHED = 1;
  SWITCH_TO_MONTHLY_RESULT_SWITCH_PENDING_REFUND = 2;
  SWITCH_TO_MONTHLY_RESULT_REFUNDED_NOT_SWITCHED = 3;
}

enum MonthlySwitchIneligibility {
  MONTHLY_SWITCH_INELIGIBILITY_UNSPECIFIED = 0;
  MONTHLY_SWITCH_INELIGIBILITY_NO_ACTIVE_SUB
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07031"></a>
## FND-07031: chesscom.payments.v1.SwitchToMonthlyResult.SWITCH_TO_MONTHLY_RESULT_SWITCHED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SWITCH_TO_MONTHLY_RESULT_SWITCHED = 1;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1921.

```text
_RESULT_NO_MATCH = 4;
}

enum SwitchToMonthlyResult {
  SWITCH_TO_MONTHLY_RESULT_UNSPECIFIED = 0;
  SWITCH_TO_MONTHLY_RESULT_SWITCHED = 1;
  SWITCH_TO_MONTHLY_RESULT_SWITCH_PENDING_REFUND = 2;
  SWITCH_TO_MONTHLY_RESULT_REFUNDED_NOT_SWITCHED = 3;
}

enum MonthlySwitchIneligibility {
  MONTHLY_SWITCH_INELIGIBILITY_UNSPECIFIED = 0;
  MONTHLY_SWITCH_INELIGIBILITY_NO_ACTIVE_SUBSCRIPTION = 1;
  MONTHLY_SWITCH_INELIGIBILIT
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07032"></a>
## FND-07032: chesscom.payments.v1.SwitchToMonthlyResult.SWITCH_TO_MONTHLY_RESULT_SWITCH_PENDING_REFUND = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SWITCH_TO_MONTHLY_RESULT_SWITCH_PENDING_REFUND = 2;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 1962.

```text
thlyResult {
  SWITCH_TO_MONTHLY_RESULT_UNSPECIFIED = 0;
  SWITCH_TO_MONTHLY_RESULT_SWITCHED = 1;
  SWITCH_TO_MONTHLY_RESULT_SWITCH_PENDING_REFUND = 2;
  SWITCH_TO_MONTHLY_RESULT_REFUNDED_NOT_SWITCHED = 3;
}

enum MonthlySwitchIneligibility {
  MONTHLY_SWITCH_INELIGIBILITY_UNSPECIFIED = 0;
  MONTHLY_SWITCH_INELIGIBILITY_NO_ACTIVE_SUBSCRIPTION = 1;
  MONTHLY_SWITCH_INELIGIBILITY_NOT_A_PAID_SUBSCRIPTION = 2;
  MONTHLY_
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07033"></a>
## FND-07033: chesscom.payments.v1.SwitchToMonthlyResult.SWITCH_TO_MONTHLY_RESULT_REFUNDED_NOT_SWITCHED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SWITCH_TO_MONTHLY_RESULT_REFUNDED_NOT_SWITCHED = 3;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2016.

```text
0;
  SWITCH_TO_MONTHLY_RESULT_SWITCHED = 1;
  SWITCH_TO_MONTHLY_RESULT_SWITCH_PENDING_REFUND = 2;
  SWITCH_TO_MONTHLY_RESULT_REFUNDED_NOT_SWITCHED = 3;
}

enum MonthlySwitchIneligibility {
  MONTHLY_SWITCH_INELIGIBILITY_UNSPECIFIED = 0;
  MONTHLY_SWITCH_INELIGIBILITY_NO_ACTIVE_SUBSCRIPTION = 1;
  MONTHLY_SWITCH_INELIGIBILITY_NOT_A_PAID_SUBSCRIPTION = 2;
  MONTHLY_SWITCH_INELIGIBILITY_TRIAL_SUBSCRIPTION = 3;
  MONTHLY
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07034"></a>
## FND-07034: enum declaration: chesscom.payments.v1.MonthlySwitchIneligibility

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MonthlySwitchIneligibility {

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2071.

```text
_MONTHLY_RESULT_SWITCH_PENDING_REFUND = 2;
  SWITCH_TO_MONTHLY_RESULT_REFUNDED_NOT_SWITCHED = 3;
}

enum MonthlySwitchIneligibility {
  MONTHLY_SWITCH_INELIGIBILITY_UNSPECIFIED = 0;
  MONTHLY_SWITCH_INELIGIBILITY_NO_ACTIVE_SUBSCRIPTION = 1;
  MONTHLY_SWITCH_INELIGIBILITY_NOT_A_PAID_SUBSCRIPTION = 2;
  MONTHLY_SWITCH_INELIGIBILITY_TRIAL_SUBSCRIPTION = 3;
  MONTHLY_SWITCH_INELIGIBILITY_OPENING_OFFER_SUBSCRIPTION = 4;
 
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07035"></a>
## FND-07035: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_UNSPECIFIED = 0;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2107.

```text
D = 2;
  SWITCH_TO_MONTHLY_RESULT_REFUNDED_NOT_SWITCHED = 3;
}

enum MonthlySwitchIneligibility {
  MONTHLY_SWITCH_INELIGIBILITY_UNSPECIFIED = 0;
  MONTHLY_SWITCH_INELIGIBILITY_NO_ACTIVE_SUBSCRIPTION = 1;
  MONTHLY_SWITCH_INELIGIBILITY_NOT_A_PAID_SUBSCRIPTION = 2;
  MONTHLY_SWITCH_INELIGIBILITY_TRIAL_SUBSCRIPTION = 3;
  MONTHLY_SWITCH_INELIGIBILITY_OPENING_OFFER_SUBSCRIPTION = 4;
  MONTHLY_SWITCH_INELIGIBILITY_MISSIN
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07036"></a>
## FND-07036: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_NO_ACTIVE_SUBSCRIPTION = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_NO_ACTIVE_SUBSCRIPTION = 1;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2155.

```text
WITCHED = 3;
}

enum MonthlySwitchIneligibility {
  MONTHLY_SWITCH_INELIGIBILITY_UNSPECIFIED = 0;
  MONTHLY_SWITCH_INELIGIBILITY_NO_ACTIVE_SUBSCRIPTION = 1;
  MONTHLY_SWITCH_INELIGIBILITY_NOT_A_PAID_SUBSCRIPTION = 2;
  MONTHLY_SWITCH_INELIGIBILITY_TRIAL_SUBSCRIPTION = 3;
  MONTHLY_SWITCH_INELIGIBILITY_OPENING_OFFER_SUBSCRIPTION = 4;
  MONTHLY_SWITCH_INELIGIBILITY_MISSING_ORDER_ITEM = 5;
  MONTHLY_SWITCH_INELIGIBILITY
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07037"></a>
## FND-07037: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_NOT_A_PAID_SUBSCRIPTION = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_NOT_A_PAID_SUBSCRIPTION = 2;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2214.

```text
_SWITCH_INELIGIBILITY_UNSPECIFIED = 0;
  MONTHLY_SWITCH_INELIGIBILITY_NO_ACTIVE_SUBSCRIPTION = 1;
  MONTHLY_SWITCH_INELIGIBILITY_NOT_A_PAID_SUBSCRIPTION = 2;
  MONTHLY_SWITCH_INELIGIBILITY_TRIAL_SUBSCRIPTION = 3;
  MONTHLY_SWITCH_INELIGIBILITY_OPENING_OFFER_SUBSCRIPTION = 4;
  MONTHLY_SWITCH_INELIGIBILITY_MISSING_ORDER_ITEM = 5;
  MONTHLY_SWITCH_INELIGIBILITY_UNSUPPORTED_GATEWAY = 6;
  MONTHLY_SWITCH_INELIGIBILITY_GR
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07038"></a>
## FND-07038: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_TRIAL_SUBSCRIPTION = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_TRIAL_SUBSCRIPTION = 3;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2274.

```text
IGIBILITY_NO_ACTIVE_SUBSCRIPTION = 1;
  MONTHLY_SWITCH_INELIGIBILITY_NOT_A_PAID_SUBSCRIPTION = 2;
  MONTHLY_SWITCH_INELIGIBILITY_TRIAL_SUBSCRIPTION = 3;
  MONTHLY_SWITCH_INELIGIBILITY_OPENING_OFFER_SUBSCRIPTION = 4;
  MONTHLY_SWITCH_INELIGIBILITY_MISSING_ORDER_ITEM = 5;
  MONTHLY_SWITCH_INELIGIBILITY_UNSUPPORTED_GATEWAY = 6;
  MONTHLY_SWITCH_INELIGIBILITY_GROUP_MEMBERSHIP_NOT_SUPPORTED = 7;
  MONTHLY_SWITCH_INELIGIBI
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07039"></a>
## FND-07039: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_OPENING_OFFER_SUBSCRIPTION = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_OPENING_OFFER_SUBSCRIPTION = 4;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2329.

```text
INELIGIBILITY_NOT_A_PAID_SUBSCRIPTION = 2;
  MONTHLY_SWITCH_INELIGIBILITY_TRIAL_SUBSCRIPTION = 3;
  MONTHLY_SWITCH_INELIGIBILITY_OPENING_OFFER_SUBSCRIPTION = 4;
  MONTHLY_SWITCH_INELIGIBILITY_MISSING_ORDER_ITEM = 5;
  MONTHLY_SWITCH_INELIGIBILITY_UNSUPPORTED_GATEWAY = 6;
  MONTHLY_SWITCH_INELIGIBILITY_GROUP_MEMBERSHIP_NOT_SUPPORTED = 7;
  MONTHLY_SWITCH_INELIGIBILITY_NOT_A_YEARLY_PLAN = 8;
  MONTHLY_SWITCH_INELIGIBIL
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07040"></a>
## FND-07040: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_MISSING_ORDER_ITEM = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_MISSING_ORDER_ITEM = 5;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2392.

```text
LIGIBILITY_TRIAL_SUBSCRIPTION = 3;
  MONTHLY_SWITCH_INELIGIBILITY_OPENING_OFFER_SUBSCRIPTION = 4;
  MONTHLY_SWITCH_INELIGIBILITY_MISSING_ORDER_ITEM = 5;
  MONTHLY_SWITCH_INELIGIBILITY_UNSUPPORTED_GATEWAY = 6;
  MONTHLY_SWITCH_INELIGIBILITY_GROUP_MEMBERSHIP_NOT_SUPPORTED = 7;
  MONTHLY_SWITCH_INELIGIBILITY_NOT_A_YEARLY_PLAN = 8;
  MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_CANNOT_BE_REACTIVATED = 9;
  MONTHLY_SWITCH_IN
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07041"></a>
## FND-07041: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_UNSUPPORTED_GATEWAY = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_UNSUPPORTED_GATEWAY = 6;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2447.

```text
LIGIBILITY_OPENING_OFFER_SUBSCRIPTION = 4;
  MONTHLY_SWITCH_INELIGIBILITY_MISSING_ORDER_ITEM = 5;
  MONTHLY_SWITCH_INELIGIBILITY_UNSUPPORTED_GATEWAY = 6;
  MONTHLY_SWITCH_INELIGIBILITY_GROUP_MEMBERSHIP_NOT_SUPPORTED = 7;
  MONTHLY_SWITCH_INELIGIBILITY_NOT_A_YEARLY_PLAN = 8;
  MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_CANNOT_BE_REACTIVATED = 9;
  MONTHLY_SWITCH_INELIGIBILITY_MISSING_EXPIRY_DATE = 10;
  MONTHLY_SWITCH_
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07042"></a>
## FND-07042: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_GROUP_MEMBERSHIP_NOT_SUPPORTED = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_GROUP_MEMBERSHIP_NOT_SUPPORTED = 7;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2503.

```text
TCH_INELIGIBILITY_MISSING_ORDER_ITEM = 5;
  MONTHLY_SWITCH_INELIGIBILITY_UNSUPPORTED_GATEWAY = 6;
  MONTHLY_SWITCH_INELIGIBILITY_GROUP_MEMBERSHIP_NOT_SUPPORTED = 7;
  MONTHLY_SWITCH_INELIGIBILITY_NOT_A_YEARLY_PLAN = 8;
  MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_CANNOT_BE_REACTIVATED = 9;
  MONTHLY_SWITCH_INELIGIBILITY_MISSING_EXPIRY_DATE = 10;
  MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_EXPIRED = 11;
  MONTHLY_SWITC
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07043"></a>
## FND-07043: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_NOT_A_YEARLY_PLAN = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_NOT_A_YEARLY_PLAN = 8;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2570.

```text
ILITY_UNSUPPORTED_GATEWAY = 6;
  MONTHLY_SWITCH_INELIGIBILITY_GROUP_MEMBERSHIP_NOT_SUPPORTED = 7;
  MONTHLY_SWITCH_INELIGIBILITY_NOT_A_YEARLY_PLAN = 8;
  MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_CANNOT_BE_REACTIVATED = 9;
  MONTHLY_SWITCH_INELIGIBILITY_MISSING_EXPIRY_DATE = 10;
  MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_EXPIRED = 11;
  MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_EQUIVALENT_NOT_FOUND = 12;
  MONTHLY_SWITCH
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07044"></a>
## FND-07044: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_CANNOT_BE_REACTIVATED = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_CANNOT_BE_REACTIVATED = 9;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2624.

```text
IBILITY_GROUP_MEMBERSHIP_NOT_SUPPORTED = 7;
  MONTHLY_SWITCH_INELIGIBILITY_NOT_A_YEARLY_PLAN = 8;
  MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_CANNOT_BE_REACTIVATED = 9;
  MONTHLY_SWITCH_INELIGIBILITY_MISSING_EXPIRY_DATE = 10;
  MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_EXPIRED = 11;
  MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_EQUIVALENT_NOT_FOUND = 12;
  MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_PRICE_UNAVAILABLE = 13;
  MONTH
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07045"></a>
## FND-07045: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_MISSING_EXPIRY_DATE = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_MISSING_EXPIRY_DATE = 10;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2695.

```text
ITY_NOT_A_YEARLY_PLAN = 8;
  MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_CANNOT_BE_REACTIVATED = 9;
  MONTHLY_SWITCH_INELIGIBILITY_MISSING_EXPIRY_DATE = 10;
  MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_EXPIRED = 11;
  MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_EQUIVALENT_NOT_FOUND = 12;
  MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_PRICE_UNAVAILABLE = 13;
  MONTHLY_SWITCH_INELIGIBILITY_ORDER_ALREADY_REFUNDED = 14;
  MONTHLY_SWITCH_I
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07046"></a>
## FND-07046: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_EXPIRED = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_EXPIRED = 11;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2752.

```text
_SUBSCRIPTION_CANNOT_BE_REACTIVATED = 9;
  MONTHLY_SWITCH_INELIGIBILITY_MISSING_EXPIRY_DATE = 10;
  MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_EXPIRED = 11;
  MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_EQUIVALENT_NOT_FOUND = 12;
  MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_PRICE_UNAVAILABLE = 13;
  MONTHLY_SWITCH_INELIGIBILITY_ORDER_ALREADY_REFUNDED = 14;
  MONTHLY_SWITCH_INELIGIBILITY_PAID_ORDER_NOT_FOUND = 15;
  MONTHLY_SWITCH_
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07047"></a>
## FND-07047: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_EQUIVALENT_NOT_FOUND = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_EQUIVALENT_NOT_FOUND = 12;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2810.

```text
INELIGIBILITY_MISSING_EXPIRY_DATE = 10;
  MONTHLY_SWITCH_INELIGIBILITY_SUBSCRIPTION_EXPIRED = 11;
  MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_EQUIVALENT_NOT_FOUND = 12;
  MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_PRICE_UNAVAILABLE = 13;
  MONTHLY_SWITCH_INELIGIBILITY_ORDER_ALREADY_REFUNDED = 14;
  MONTHLY_SWITCH_INELIGIBILITY_PAID_ORDER_NOT_FOUND = 15;
  MONTHLY_SWITCH_INELIGIBILITY_TERM_LENGTH_UNKNOWN = 16;
  MONTHLY_SWITCH_I
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07048"></a>
## FND-07048: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_PRICE_UNAVAILABLE = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_PRICE_UNAVAILABLE = 13;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2876.

```text
LITY_SUBSCRIPTION_EXPIRED = 11;
  MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_EQUIVALENT_NOT_FOUND = 12;
  MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_PRICE_UNAVAILABLE = 13;
  MONTHLY_SWITCH_INELIGIBILITY_ORDER_ALREADY_REFUNDED = 14;
  MONTHLY_SWITCH_INELIGIBILITY_PAID_ORDER_NOT_FOUND = 15;
  MONTHLY_SWITCH_INELIGIBILITY_TERM_LENGTH_UNKNOWN = 16;
  MONTHLY_SWITCH_INELIGIBILITY_GIFT_NOT_SUPPORTED = 17;
  MONTHLY_SWITCH_INELIGIBILI
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07049"></a>
## FND-07049: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_ORDER_ALREADY_REFUNDED = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_ORDER_ALREADY_REFUNDED = 14;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2939.

```text
MONTHLY_EQUIVALENT_NOT_FOUND = 12;
  MONTHLY_SWITCH_INELIGIBILITY_MONTHLY_PRICE_UNAVAILABLE = 13;
  MONTHLY_SWITCH_INELIGIBILITY_ORDER_ALREADY_REFUNDED = 14;
  MONTHLY_SWITCH_INELIGIBILITY_PAID_ORDER_NOT_FOUND = 15;
  MONTHLY_SWITCH_INELIGIBILITY_TERM_LENGTH_UNKNOWN = 16;
  MONTHLY_SWITCH_INELIGIBILITY_GIFT_NOT_SUPPORTED = 17;
  MONTHLY_SWITCH_INELIGIBILITY_CURRENCY_MISMATCH = 18;
  MONTHLY_SWITCH_INELIGIBILITY_MANUA
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07050"></a>
## FND-07050: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_PAID_ORDER_NOT_FOUND = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_PAID_ORDER_NOT_FOUND = 15;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 2999.

```text
ILITY_MONTHLY_PRICE_UNAVAILABLE = 13;
  MONTHLY_SWITCH_INELIGIBILITY_ORDER_ALREADY_REFUNDED = 14;
  MONTHLY_SWITCH_INELIGIBILITY_PAID_ORDER_NOT_FOUND = 15;
  MONTHLY_SWITCH_INELIGIBILITY_TERM_LENGTH_UNKNOWN = 16;
  MONTHLY_SWITCH_INELIGIBILITY_GIFT_NOT_SUPPORTED = 17;
  MONTHLY_SWITCH_INELIGIBILITY_CURRENCY_MISMATCH = 18;
  MONTHLY_SWITCH_INELIGIBILITY_MANUAL_REFUND_REQUIRED = 19;
}

enum MembershipPartner {
  MEMBER
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07051"></a>
## FND-07051: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_TERM_LENGTH_UNKNOWN = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_TERM_LENGTH_UNKNOWN = 16;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3057.

```text
LIGIBILITY_ORDER_ALREADY_REFUNDED = 14;
  MONTHLY_SWITCH_INELIGIBILITY_PAID_ORDER_NOT_FOUND = 15;
  MONTHLY_SWITCH_INELIGIBILITY_TERM_LENGTH_UNKNOWN = 16;
  MONTHLY_SWITCH_INELIGIBILITY_GIFT_NOT_SUPPORTED = 17;
  MONTHLY_SWITCH_INELIGIBILITY_CURRENCY_MISMATCH = 18;
  MONTHLY_SWITCH_INELIGIBILITY_MANUAL_REFUND_REQUIRED = 19;
}

enum MembershipPartner {
  MEMBERSHIP_PARTNER_UNSPECIFIED = 0;
  MEMBERSHIP_PARTNER_REVOLUT
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07052"></a>
## FND-07052: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_GIFT_NOT_SUPPORTED = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_GIFT_NOT_SUPPORTED = 17;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3114.

```text
INELIGIBILITY_PAID_ORDER_NOT_FOUND = 15;
  MONTHLY_SWITCH_INELIGIBILITY_TERM_LENGTH_UNKNOWN = 16;
  MONTHLY_SWITCH_INELIGIBILITY_GIFT_NOT_SUPPORTED = 17;
  MONTHLY_SWITCH_INELIGIBILITY_CURRENCY_MISMATCH = 18;
  MONTHLY_SWITCH_INELIGIBILITY_MANUAL_REFUND_REQUIRED = 19;
}

enum MembershipPartner {
  MEMBERSHIP_PARTNER_UNSPECIFIED = 0;
  MEMBERSHIP_PARTNER_REVOLUT = 1;
  MEMBERSHIP_PARTNER_UNIDAYS = 2;
}

message PaidOr
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07053"></a>
## FND-07053: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_CURRENCY_MISMATCH = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_CURRENCY_MISMATCH = 18;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3170.

```text
H_INELIGIBILITY_TERM_LENGTH_UNKNOWN = 16;
  MONTHLY_SWITCH_INELIGIBILITY_GIFT_NOT_SUPPORTED = 17;
  MONTHLY_SWITCH_INELIGIBILITY_CURRENCY_MISMATCH = 18;
  MONTHLY_SWITCH_INELIGIBILITY_MANUAL_REFUND_REQUIRED = 19;
}

enum MembershipPartner {
  MEMBERSHIP_PARTNER_UNSPECIFIED = 0;
  MEMBERSHIP_PARTNER_REVOLUT = 1;
  MEMBERSHIP_PARTNER_UNIDAYS = 2;
}

message PaidOrderBasis {
  optional string charge_id = 1;
}

message P
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07054"></a>
## FND-07054: chesscom.payments.v1.MonthlySwitchIneligibility.MONTHLY_SWITCH_INELIGIBILITY_MANUAL_REFUND_REQUIRED = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_SWITCH_INELIGIBILITY_MANUAL_REFUND_REQUIRED = 19;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3225.

```text
TCH_INELIGIBILITY_GIFT_NOT_SUPPORTED = 17;
  MONTHLY_SWITCH_INELIGIBILITY_CURRENCY_MISMATCH = 18;
  MONTHLY_SWITCH_INELIGIBILITY_MANUAL_REFUND_REQUIRED = 19;
}

enum MembershipPartner {
  MEMBERSHIP_PARTNER_UNSPECIFIED = 0;
  MEMBERSHIP_PARTNER_REVOLUT = 1;
  MEMBERSHIP_PARTNER_UNIDAYS = 2;
}

message PaidOrderBasis {
  optional string charge_id = 1;
}

message PartnerMembershipBasis {
  oneof reference {
  string ch
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07055"></a>
## FND-07055: enum declaration: chesscom.payments.v1.MembershipPartner

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MembershipPartner {

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3286.

```text
NELIGIBILITY_CURRENCY_MISMATCH = 18;
  MONTHLY_SWITCH_INELIGIBILITY_MANUAL_REFUND_REQUIRED = 19;
}

enum MembershipPartner {
  MEMBERSHIP_PARTNER_UNSPECIFIED = 0;
  MEMBERSHIP_PARTNER_REVOLUT = 1;
  MEMBERSHIP_PARTNER_UNIDAYS = 2;
}

message PaidOrderBasis {
  optional string charge_id = 1;
}

message PartnerMembershipBasis {
  oneof reference {
  string charge_id = 2;
  string revolut_code = 3;
  }
  optional .chess
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07056"></a>
## FND-07056: chesscom.payments.v1.MembershipPartner.MEMBERSHIP_PARTNER_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_PARTNER_UNSPECIFIED = 0;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3313.

```text
TCH = 18;
  MONTHLY_SWITCH_INELIGIBILITY_MANUAL_REFUND_REQUIRED = 19;
}

enum MembershipPartner {
  MEMBERSHIP_PARTNER_UNSPECIFIED = 0;
  MEMBERSHIP_PARTNER_REVOLUT = 1;
  MEMBERSHIP_PARTNER_UNIDAYS = 2;
}

message PaidOrderBasis {
  optional string charge_id = 1;
}

message PartnerMembershipBasis {
  oneof reference {
  string charge_id = 2;
  string revolut_code = 3;
  }
  optional .chesscom.payments.v1.MembershipP
```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07057"></a>
## FND-07057: chesscom.payments.v1.MembershipPartner.MEMBERSHIP_PARTNER_REVOLUT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_PARTNER_REVOLUT = 1;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3351.

```text
TY_MANUAL_REFUND_REQUIRED = 19;
}

enum MembershipPartner {
  MEMBERSHIP_PARTNER_UNSPECIFIED = 0;
  MEMBERSHIP_PARTNER_REVOLUT = 1;
  MEMBERSHIP_PARTNER_UNIDAYS = 2;
}

message PaidOrderBasis {
  optional string charge_id = 1;
}

message PartnerMembershipBasis {
  oneof reference {
  string charge_id = 2;
  string revolut_code = 3;
  }
  optional .chesscom.payments.v1.MembershipPartner partner = 1;
}

```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07058"></a>
## FND-07058: chesscom.payments.v1.MembershipPartner.MEMBERSHIP_PARTNER_UNIDAYS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_PARTNER_UNIDAYS = 2;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3385.

```text

enum MembershipPartner {
  MEMBERSHIP_PARTNER_UNSPECIFIED = 0;
  MEMBERSHIP_PARTNER_REVOLUT = 1;
  MEMBERSHIP_PARTNER_UNIDAYS = 2;
}

message PaidOrderBasis {
  optional string charge_id = 1;
}

message PartnerMembershipBasis {
  oneof reference {
  string charge_id = 2;
  string revolut_code = 3;
  }
  optional .chesscom.payments.v1.MembershipPartner partner = 1;
}

```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07059"></a>
## FND-07059: message declaration: chesscom.payments.v1.PaidOrderBasis

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PaidOrderBasis {

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3420.

```text
HIP_PARTNER_UNSPECIFIED = 0;
  MEMBERSHIP_PARTNER_REVOLUT = 1;
  MEMBERSHIP_PARTNER_UNIDAYS = 2;
}

message PaidOrderBasis {
  optional string charge_id = 1;
}

message PartnerMembershipBasis {
  oneof reference {
  string charge_id = 2;
  string revolut_code = 3;
  }
  optional .chesscom.payments.v1.MembershipPartner partner = 1;
}

```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07060"></a>
## FND-07060: chesscom.payments.v1.PaidOrderBasis.charge_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string charge_id = 1;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3447.

```text
;
  MEMBERSHIP_PARTNER_REVOLUT = 1;
  MEMBERSHIP_PARTNER_UNIDAYS = 2;
}

message PaidOrderBasis {
  optional string charge_id = 1;
}

message PartnerMembershipBasis {
  oneof reference {
  string charge_id = 2;
  string revolut_code = 3;
  }
  optional .chesscom.payments.v1.MembershipPartner partner = 1;
}

```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07061"></a>
## FND-07061: message declaration: chesscom.payments.v1.PartnerMembershipBasis

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PartnerMembershipBasis {

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3481.

```text
;
  MEMBERSHIP_PARTNER_UNIDAYS = 2;
}

message PaidOrderBasis {
  optional string charge_id = 1;
}

message PartnerMembershipBasis {
  oneof reference {
  string charge_id = 2;
  string revolut_code = 3;
  }
  optional .chesscom.payments.v1.MembershipPartner partner = 1;
}

```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07062"></a>
## FND-07062: oneof declaration: chesscom.payments.v1.PartnerMembershipBasis.reference

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof reference {

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3516.

```text

}

message PaidOrderBasis {
  optional string charge_id = 1;
}

message PartnerMembershipBasis {
  oneof reference {
  string charge_id = 2;
  string revolut_code = 3;
  }
  optional .chesscom.payments.v1.MembershipPartner partner = 1;
}

```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07063"></a>
## FND-07063: chesscom.payments.v1.PartnerMembershipBasis.charge_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string charge_id = 2;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3536.

```text
rBasis {
  optional string charge_id = 1;
}

message PartnerMembershipBasis {
  oneof reference {
  string charge_id = 2;
  string revolut_code = 3;
  }
  optional .chesscom.payments.v1.MembershipPartner partner = 1;
}

```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07064"></a>
## FND-07064: chesscom.payments.v1.PartnerMembershipBasis.revolut_code = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string revolut_code = 3;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3560.

```text
ng charge_id = 1;
}

message PartnerMembershipBasis {
  oneof reference {
  string charge_id = 2;
  string revolut_code = 3;
  }
  optional .chesscom.payments.v1.MembershipPartner partner = 1;
}

```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07065"></a>
## FND-07065: chesscom.payments.v1.PartnerMembershipBasis.partner = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.MembershipPartner partner = 1;

### Evidence

- **SRC-0511** `research/proto/chesscom/payments/v1/subscription_admin.proto` — [preserved redacted evidence](../evidence/text/6202f66b5695c5db50e7eb794534b6435c69dd69066805d5c0ad13c62881b5e0.proto)
  Character offset 3591.

```text
rtnerMembershipBasis {
  oneof reference {
  string charge_id = 2;
  string revolut_code = 3;
  }
  optional .chesscom.payments.v1.MembershipPartner partner = 1;
}

```

**Source references:** SRC-0511, SRC-1482  
**URL references:** None independently associated  
**Related findings:** FND-06998, FND-06999, FND-07000

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07066"></a>
## FND-07066: message declaration: chesscom.payments.v1.CancelSubscriptionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CancelSubscriptionRequest {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 115.

```text
scom/payments/v1/subscription_admin_service.proto
// syntax: proto3

package chesscom.payments.v1;

message CancelSubscriptionRequest {
  optional string user_uuid = 1;
  optional .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestam
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07067"></a>
## FND-07067: chesscom.payments.v1.CancelSubscriptionRequest.user_uuid = 1

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
**Related findings:** FND-07066, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07068"></a>
## FND-07068: chesscom.payments.v1.CancelSubscriptionRequest.context = 2

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
**Related findings:** FND-07066, FND-07067

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07069"></a>
## FND-07069: chesscom.payments.v1.CancelSubscriptionRequest.subscription_id = 3

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

<a id="FND-07070"></a>
## FND-07070: message declaration: chesscom.payments.v1.CancelSubscriptionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CancelSubscriptionResponse {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 292.

```text
al .chesscom.support.v1.SupportActionContext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;

```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07071"></a>
## FND-07071: chesscom.payments.v1.CancelSubscriptionResponse.result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 331.

```text
ntext context = 2;
  optional string subscription_id = 3;
}

message CancelSubscriptionResponse {
  optional .chesscom.payments.v1.CancelSubscriptionResult result = 1;
  optional .google.protobuf.Timestamp access_ends_at = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
}

message StopRenewalByCardMatchReques
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07072"></a>
## FND-07072: chesscom.payments.v1.CancelSubscriptionResponse.access_ends_at = 2

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

<a id="FND-07073"></a>
## FND-07073: chesscom.payments.v1.CancelSubscriptionResponse.action_result = 3

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

<a id="FND-07074"></a>
## FND-07074: chesscom.payments.v1.CancelSubscriptionResponse.refusal_reason = 4

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
