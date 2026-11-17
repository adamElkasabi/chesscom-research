# data_models — findings 6101–6200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-06375"></a>
## FND-06375: chesscom.payments.v1.GetStorefrontDetailsResponse.membership_level = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.MembershipLevel membership_level = 2;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 1226.

```text
n request_location = 1;
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
  optional .chesscom.payments.v1.PaymentContext paymen
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06376"></a>
## FND-06376: chesscom.payments.v1.GetStorefrontDetailsResponse.storefront_country = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.StorefrontCountry storefront_country = 1;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 1292.

```text
e {
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
  optional .chesscom.payments.v1.PaymentContext payment_context = 2;
}

message GetAvailablePaymentMethodsResponse {
  r
```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06377"></a>
## FND-06377: message declaration: chesscom.payments.v1.GetAvailablePaymentMethodsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetAvailablePaymentMethodsRequest {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 1368.

```text
ership_level = 2;
  }
  optional .chesscom.payments.v1.StorefrontCountry storefront_country = 1;
}

message GetAvailablePaymentMethodsRequest {
  oneof _coupon_code {
  string coupon_code = 3;
  }
  optional string sku = 1;
  optional .chesscom.payments.v1.PaymentContext payment_context = 2;
}

message GetAvailablePaymentMethodsResponse {
  repeated .chesscom.payments.v1.AvailablePaymentMethod payment_methods = 1;
}

```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06378"></a>
## FND-06378: oneof declaration: chesscom.payments.v1.GetAvailablePaymentMethodsRequest._coupon_code

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

<a id="FND-06379"></a>
## FND-06379: chesscom.payments.v1.GetAvailablePaymentMethodsRequest.coupon_code = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string coupon_code = 3;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 1437.

```text
try storefront_country = 1;
}

message GetAvailablePaymentMethodsRequest {
  oneof _coupon_code {
  string coupon_code = 3;
  }
  optional string sku = 1;
  optional .chesscom.payments.v1.PaymentContext payment_context = 2;
}

message GetAvailablePaymentMethodsResponse {
  repeated .chesscom.payments.v1.AvailablePaymentMethod payment_methods = 1;
}

```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06380"></a>
## FND-06380: chesscom.payments.v1.GetAvailablePaymentMethodsRequest.sku = 1

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

<a id="FND-06381"></a>
## FND-06381: chesscom.payments.v1.GetAvailablePaymentMethodsRequest.payment_context = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.PaymentContext payment_context = 2;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 1494.

```text
tMethodsRequest {
  oneof _coupon_code {
  string coupon_code = 3;
  }
  optional string sku = 1;
  optional .chesscom.payments.v1.PaymentContext payment_context = 2;
}

message GetAvailablePaymentMethodsResponse {
  repeated .chesscom.payments.v1.AvailablePaymentMethod payment_methods = 1;
}

```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06382"></a>
## FND-06382: message declaration: chesscom.payments.v1.GetAvailablePaymentMethodsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetAvailablePaymentMethodsResponse {

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 1564.

```text

  optional string sku = 1;
  optional .chesscom.payments.v1.PaymentContext payment_context = 2;
}

message GetAvailablePaymentMethodsResponse {
  repeated .chesscom.payments.v1.AvailablePaymentMethod payment_methods = 1;
}

```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06383"></a>
## FND-06383: chesscom.payments.v1.GetAvailablePaymentMethodsResponse.payment_methods = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.AvailablePaymentMethod payment_methods = 1;

### Evidence

- **SRC-0484** `research/proto/chesscom/payments/v1/checkout_service.proto` — [preserved redacted evidence](../evidence/text/44846e0c23a42e401589ecc50290d015e0202280687ca5bcfad84323c6298b56.proto)
  Character offset 1611.

```text
m.payments.v1.PaymentContext payment_context = 2;
}

message GetAvailablePaymentMethodsResponse {
  repeated .chesscom.payments.v1.AvailablePaymentMethod payment_methods = 1;
}

```

**Source references:** SRC-0484, SRC-1455  
**URL references:** None independently associated  
**Related findings:** FND-06346, FND-06347, FND-06348

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06384"></a>
## FND-06384: message declaration: chesscom.payments.v1.CheckoutTotal

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CheckoutTotal {

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 103.

```text
source: chesscom/payments/v1/checkout_total.proto
// syntax: proto3

package chesscom.payments.v1;

message CheckoutTotal {
  oneof product_details {
  .chesscom.courses.v1.CourseProduct course_product_details = 16;
  .chesscom.payments.v1.MembershipProductDetails membership_product_details = 17;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 13;
  }
  oneof _subtotal_amount_in_months {
  .che
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06385, FND-06386

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06385"></a>
## FND-06385: oneof declaration: chesscom.payments.v1.CheckoutTotal.product_details

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof product_details {

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 129.

```text
v1/checkout_total.proto
// syntax: proto3

package chesscom.payments.v1;

message CheckoutTotal {
  oneof product_details {
  .chesscom.courses.v1.CourseProduct course_product_details = 16;
  .chesscom.payments.v1.MembershipProductDetails membership_product_details = 17;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 13;
  }
  oneof _subtotal_amount_in_months {
  .chesscom.api.v1.Money subtota
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06386

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06386"></a>
## FND-06386: chesscom.payments.v1.CheckoutTotal.course_product_details = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseProduct course_product_details = 16;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 155.

```text
 syntax: proto3

package chesscom.payments.v1;

message CheckoutTotal {
  oneof product_details {
  .chesscom.courses.v1.CourseProduct course_product_details = 16;
  .chesscom.payments.v1.MembershipProductDetails membership_product_details = 17;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 13;
  }
  oneof _subtotal_amount_in_months {
  .chesscom.api.v1.Money subtotal_amount_in_months = 19;
 
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06387"></a>
## FND-06387: chesscom.payments.v1.CheckoutTotal.membership_product_details = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.MembershipProductDetails membership_product_details = 17;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 221.

```text
tal {
  oneof product_details {
  .chesscom.courses.v1.CourseProduct course_product_details = 16;
  .chesscom.payments.v1.MembershipProductDetails membership_product_details = 17;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 13;
  }
  oneof _subtotal_amount_in_months {
  .chesscom.api.v1.Money subtotal_amount_in_months = 19;
  }
  oneof _subtotal_amount_with_taxes_in_months {
  .chesscom.api
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06388"></a>
## FND-06388: oneof declaration: chesscom.payments.v1.CheckoutTotal._incentive

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _incentive {

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 307.

```text
tails = 16;
  .chesscom.payments.v1.MembershipProductDetails membership_product_details = 17;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 13;
  }
  oneof _subtotal_amount_in_months {
  .chesscom.api.v1.Money subtotal_amount_in_months = 19;
  }
  oneof _subtotal_amount_with_taxes_in_months {
  .chesscom.api.v1.Money subtotal_amount_with_taxes_in_months = 20;
  }
  optional .chesscom.payments
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06389"></a>
## FND-06389: chesscom.payments.v1.CheckoutTotal.incentive = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.Incentive incentive = 13;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 328.

```text
om.payments.v1.MembershipProductDetails membership_product_details = 17;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 13;
  }
  oneof _subtotal_amount_in_months {
  .chesscom.api.v1.Money subtotal_amount_in_months = 19;
  }
  oneof _subtotal_amount_with_taxes_in_months {
  .chesscom.api.v1.Money subtotal_amount_with_taxes_in_months = 20;
  }
  optional .chesscom.payments.v1.Product product =
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06390"></a>
## FND-06390: oneof declaration: chesscom.payments.v1.CheckoutTotal._subtotal_amount_in_months

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _subtotal_amount_in_months {

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 382.

```text
duct_details = 17;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 13;
  }
  oneof _subtotal_amount_in_months {
  .chesscom.api.v1.Money subtotal_amount_in_months = 19;
  }
  oneof _subtotal_amount_with_taxes_in_months {
  .chesscom.api.v1.Money subtotal_amount_with_taxes_in_months = 20;
  }
  optional .chesscom.payments.v1.Product product = 1;
  optional .chesscom.api.v1.Money original_amount 
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06391"></a>
## FND-06391: chesscom.payments.v1.CheckoutTotal.subtotal_amount_in_months = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.Money subtotal_amount_in_months = 19;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 419.

```text
tive {
  .chesscom.payments.v1.Incentive incentive = 13;
  }
  oneof _subtotal_amount_in_months {
  .chesscom.api.v1.Money subtotal_amount_in_months = 19;
  }
  oneof _subtotal_amount_with_taxes_in_months {
  .chesscom.api.v1.Money subtotal_amount_with_taxes_in_months = 20;
  }
  optional .chesscom.payments.v1.Product product = 1;
  optional .chesscom.api.v1.Money original_amount = 2;
  optional .chesscom.api.v1.Mone
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06392"></a>
## FND-06392: oneof declaration: chesscom.payments.v1.CheckoutTotal._subtotal_amount_with_taxes_in_months

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _subtotal_amount_with_taxes_in_months {

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 480.

```text
  oneof _subtotal_amount_in_months {
  .chesscom.api.v1.Money subtotal_amount_in_months = 19;
  }
  oneof _subtotal_amount_with_taxes_in_months {
  .chesscom.api.v1.Money subtotal_amount_with_taxes_in_months = 20;
  }
  optional .chesscom.payments.v1.Product product = 1;
  optional .chesscom.api.v1.Money original_amount = 2;
  optional .chesscom.api.v1.Money original_amount_with_taxes = 3;
  optional .chesscom.api.v1
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06393"></a>
## FND-06393: chesscom.payments.v1.CheckoutTotal.subtotal_amount_with_taxes_in_months = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.Money subtotal_amount_with_taxes_in_months = 20;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 528.

```text
.api.v1.Money subtotal_amount_in_months = 19;
  }
  oneof _subtotal_amount_with_taxes_in_months {
  .chesscom.api.v1.Money subtotal_amount_with_taxes_in_months = 20;
  }
  optional .chesscom.payments.v1.Product product = 1;
  optional .chesscom.api.v1.Money original_amount = 2;
  optional .chesscom.api.v1.Money original_amount_with_taxes = 3;
  optional .chesscom.api.v1.Money discount_amount = 4;
  optional .chesscom
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06394"></a>
## FND-06394: chesscom.payments.v1.CheckoutTotal.product = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.Product product = 1;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 600.

```text
nt_with_taxes_in_months {
  .chesscom.api.v1.Money subtotal_amount_with_taxes_in_months = 20;
  }
  optional .chesscom.payments.v1.Product product = 1;
  optional .chesscom.api.v1.Money original_amount = 2;
  optional .chesscom.api.v1.Money original_amount_with_taxes = 3;
  optional .chesscom.api.v1.Money discount_amount = 4;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 5;
  optional .chesscom.api.v
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06395"></a>
## FND-06395: chesscom.payments.v1.CheckoutTotal.original_amount = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money original_amount = 2;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 654.

```text
total_amount_with_taxes_in_months = 20;
  }
  optional .chesscom.payments.v1.Product product = 1;
  optional .chesscom.api.v1.Money original_amount = 2;
  optional .chesscom.api.v1.Money original_amount_with_taxes = 3;
  optional .chesscom.api.v1.Money discount_amount = 4;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 5;
  optional .chesscom.api.v1.Money subtotal_amount = 6;
  optional .chesscom.api.
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06396"></a>
## FND-06396: chesscom.payments.v1.CheckoutTotal.original_amount_with_taxes = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money original_amount_with_taxes = 3;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 709.

```text
.chesscom.payments.v1.Product product = 1;
  optional .chesscom.api.v1.Money original_amount = 2;
  optional .chesscom.api.v1.Money original_amount_with_taxes = 3;
  optional .chesscom.api.v1.Money discount_amount = 4;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 5;
  optional .chesscom.api.v1.Money subtotal_amount = 6;
  optional .chesscom.api.v1.Money subtotal_amount_with_taxes = 7;
  optional .ch
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06397"></a>
## FND-06397: chesscom.payments.v1.CheckoutTotal.discount_amount = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money discount_amount = 4;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 775.

```text
i.v1.Money original_amount = 2;
  optional .chesscom.api.v1.Money original_amount_with_taxes = 3;
  optional .chesscom.api.v1.Money discount_amount = 4;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 5;
  optional .chesscom.api.v1.Money subtotal_amount = 6;
  optional .chesscom.api.v1.Money subtotal_amount_with_taxes = 7;
  optional .chesscom.api.v1.Money credit_amount = 8;
  optional .chesscom.api.v1
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06398"></a>
## FND-06398: chesscom.payments.v1.CheckoutTotal.discount_amount_with_taxes = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money discount_amount_with_taxes = 5;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 830.

```text
i.v1.Money original_amount_with_taxes = 3;
  optional .chesscom.api.v1.Money discount_amount = 4;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 5;
  optional .chesscom.api.v1.Money subtotal_amount = 6;
  optional .chesscom.api.v1.Money subtotal_amount_with_taxes = 7;
  optional .chesscom.api.v1.Money credit_amount = 8;
  optional .chesscom.api.v1.Money credit_amount_with_taxes = 9;
  optional .chessc
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06399"></a>
## FND-06399: chesscom.payments.v1.CheckoutTotal.subtotal_amount = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money subtotal_amount = 6;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 896.

```text
i.v1.Money discount_amount = 4;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 5;
  optional .chesscom.api.v1.Money subtotal_amount = 6;
  optional .chesscom.api.v1.Money subtotal_amount_with_taxes = 7;
  optional .chesscom.api.v1.Money credit_amount = 8;
  optional .chesscom.api.v1.Money credit_amount_with_taxes = 9;
  optional .chesscom.api.v1.Money total_amount = 10;
  optional .chesscom.api.v1.Mon
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06400"></a>
## FND-06400: chesscom.payments.v1.CheckoutTotal.subtotal_amount_with_taxes = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money subtotal_amount_with_taxes = 7;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 951.

```text
i.v1.Money discount_amount_with_taxes = 5;
  optional .chesscom.api.v1.Money subtotal_amount = 6;
  optional .chesscom.api.v1.Money subtotal_amount_with_taxes = 7;
  optional .chesscom.api.v1.Money credit_amount = 8;
  optional .chesscom.api.v1.Money credit_amount_with_taxes = 9;
  optional .chesscom.api.v1.Money total_amount = 10;
  optional .chesscom.api.v1.Money tax_amount = 11;
  optional .chesscom.api.v1.Money t
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06401"></a>
## FND-06401: chesscom.payments.v1.CheckoutTotal.credit_amount = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money credit_amount = 8;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1017.

```text
i.v1.Money subtotal_amount = 6;
  optional .chesscom.api.v1.Money subtotal_amount_with_taxes = 7;
  optional .chesscom.api.v1.Money credit_amount = 8;
  optional .chesscom.api.v1.Money credit_amount_with_taxes = 9;
  optional .chesscom.api.v1.Money total_amount = 10;
  optional .chesscom.api.v1.Money tax_amount = 11;
  optional .chesscom.api.v1.Money total_amount_with_taxes = 12;
  repeated .chesscom.payments.v1.TaxL
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06402"></a>
## FND-06402: chesscom.payments.v1.CheckoutTotal.credit_amount_with_taxes = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money credit_amount_with_taxes = 9;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1070.

```text
api.v1.Money subtotal_amount_with_taxes = 7;
  optional .chesscom.api.v1.Money credit_amount = 8;
  optional .chesscom.api.v1.Money credit_amount_with_taxes = 9;
  optional .chesscom.api.v1.Money total_amount = 10;
  optional .chesscom.api.v1.Money tax_amount = 11;
  optional .chesscom.api.v1.Money total_amount_with_taxes = 12;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 14;
  optional float usd_fx_rate = 15
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06403"></a>
## FND-06403: chesscom.payments.v1.CheckoutTotal.total_amount = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money total_amount = 10;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1134.

```text
m.api.v1.Money credit_amount = 8;
  optional .chesscom.api.v1.Money credit_amount_with_taxes = 9;
  optional .chesscom.api.v1.Money total_amount = 10;
  optional .chesscom.api.v1.Money tax_amount = 11;
  optional .chesscom.api.v1.Money total_amount_with_taxes = 12;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 14;
  optional float usd_fx_rate = 15;
  repeated .chesscom.payments.v1.Discount discount_amount_brea
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06404"></a>
## FND-06404: chesscom.payments.v1.CheckoutTotal.tax_amount = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money tax_amount = 11;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1187.

```text
m.api.v1.Money credit_amount_with_taxes = 9;
  optional .chesscom.api.v1.Money total_amount = 10;
  optional .chesscom.api.v1.Money tax_amount = 11;
  optional .chesscom.api.v1.Money total_amount_with_taxes = 12;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 14;
  optional float usd_fx_rate = 15;
  repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 18;
}

message TaxLine {
  optional string de
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06405"></a>
## FND-06405: chesscom.payments.v1.CheckoutTotal.total_amount_with_taxes = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money total_amount_with_taxes = 12;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1238.

```text
onal .chesscom.api.v1.Money total_amount = 10;
  optional .chesscom.api.v1.Money tax_amount = 11;
  optional .chesscom.api.v1.Money total_amount_with_taxes = 12;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 14;
  optional float usd_fx_rate = 15;
  repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 18;
}

message TaxLine {
  optional string description = 1;
  optional float rate = 2;
  optiona
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06406"></a>
## FND-06406: chesscom.payments.v1.CheckoutTotal.tax_lines = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.TaxLine tax_lines = 14;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1302.

```text
com.api.v1.Money tax_amount = 11;
  optional .chesscom.api.v1.Money total_amount_with_taxes = 12;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 14;
  optional float usd_fx_rate = 15;
  repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 18;
}

message TaxLine {
  optional string description = 1;
  optional float rate = 2;
  optional .chesscom.api.v1.Money amount = 3;
}

message TotalBreakdown {
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06407"></a>
## FND-06407: chesscom.payments.v1.CheckoutTotal.usd_fx_rate = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float usd_fx_rate = 15;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1359.

```text
i.v1.Money total_amount_with_taxes = 12;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 14;
  optional float usd_fx_rate = 15;
  repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 18;
}

message TaxLine {
  optional string description = 1;
  optional float rate = 2;
  optional .chesscom.api.v1.Money amount = 3;
}

message TotalBreakdown {
  optional .chesscom.api.v1.Money original_amount = 1;
 
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06408"></a>
## FND-06408: chesscom.payments.v1.CheckoutTotal.discount_amount_breakdown = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 18;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1394.

```text
= 12;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 14;
  optional float usd_fx_rate = 15;
  repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 18;
}

message TaxLine {
  optional string description = 1;
  optional float rate = 2;
  optional .chesscom.api.v1.Money amount = 3;
}

message TotalBreakdown {
  optional .chesscom.api.v1.Money original_amount = 1;
  optional .chesscom.api.v1.Money or
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06409"></a>
## FND-06409: message declaration: chesscom.payments.v1.TaxLine

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TaxLine {

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1469.

```text
loat usd_fx_rate = 15;
  repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 18;
}

message TaxLine {
  optional string description = 1;
  optional float rate = 2;
  optional .chesscom.api.v1.Money amount = 3;
}

message TotalBreakdown {
  optional .chesscom.api.v1.Money original_amount = 1;
  optional .chesscom.api.v1.Money original_amount_with_taxes = 2;
  optional .chesscom.api.v1.Money discount_am
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06410"></a>
## FND-06410: chesscom.payments.v1.TaxLine.description = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string description = 1;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1489.

```text
5;
  repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 18;
}

message TaxLine {
  optional string description = 1;
  optional float rate = 2;
  optional .chesscom.api.v1.Money amount = 3;
}

message TotalBreakdown {
  optional .chesscom.api.v1.Money original_amount = 1;
  optional .chesscom.api.v1.Money original_amount_with_taxes = 2;
  optional .chesscom.api.v1.Money discount_amount = 3;
  optional
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06411"></a>
## FND-06411: chesscom.payments.v1.TaxLine.rate = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float rate = 2;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1524.

```text
.Discount discount_amount_breakdown = 18;
}

message TaxLine {
  optional string description = 1;
  optional float rate = 2;
  optional .chesscom.api.v1.Money amount = 3;
}

message TotalBreakdown {
  optional .chesscom.api.v1.Money original_amount = 1;
  optional .chesscom.api.v1.Money original_amount_with_taxes = 2;
  optional .chesscom.api.v1.Money discount_amount = 3;
  optional .chesscom.api.v1.Money discount_am
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06412"></a>
## FND-06412: chesscom.payments.v1.TaxLine.amount = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money amount = 3;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1551.

```text
reakdown = 18;
}

message TaxLine {
  optional string description = 1;
  optional float rate = 2;
  optional .chesscom.api.v1.Money amount = 3;
}

message TotalBreakdown {
  optional .chesscom.api.v1.Money original_amount = 1;
  optional .chesscom.api.v1.Money original_amount_with_taxes = 2;
  optional .chesscom.api.v1.Money discount_amount = 3;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 4;
  opti
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06413"></a>
## FND-06413: message declaration: chesscom.payments.v1.TotalBreakdown

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TotalBreakdown {

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1598.

```text
string description = 1;
  optional float rate = 2;
  optional .chesscom.api.v1.Money amount = 3;
}

message TotalBreakdown {
  optional .chesscom.api.v1.Money original_amount = 1;
  optional .chesscom.api.v1.Money original_amount_with_taxes = 2;
  optional .chesscom.api.v1.Money discount_amount = 3;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 4;
  optional .chesscom.api.v1.Money subtotal_amount = 5
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06414"></a>
## FND-06414: chesscom.payments.v1.TotalBreakdown.original_amount = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money original_amount = 1;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1625.

```text
ptional float rate = 2;
  optional .chesscom.api.v1.Money amount = 3;
}

message TotalBreakdown {
  optional .chesscom.api.v1.Money original_amount = 1;
  optional .chesscom.api.v1.Money original_amount_with_taxes = 2;
  optional .chesscom.api.v1.Money discount_amount = 3;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 4;
  optional .chesscom.api.v1.Money subtotal_amount = 5;
  optional .chesscom.api.
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06415"></a>
## FND-06415: chesscom.payments.v1.TotalBreakdown.original_amount_with_taxes = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money original_amount_with_taxes = 2;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1680.

```text
ey amount = 3;
}

message TotalBreakdown {
  optional .chesscom.api.v1.Money original_amount = 1;
  optional .chesscom.api.v1.Money original_amount_with_taxes = 2;
  optional .chesscom.api.v1.Money discount_amount = 3;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 4;
  optional .chesscom.api.v1.Money subtotal_amount = 5;
  optional .chesscom.api.v1.Money subtotal_amount_with_taxes = 6;
  optional .ch
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06416"></a>
## FND-06416: chesscom.payments.v1.TotalBreakdown.discount_amount = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money discount_amount = 3;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1746.

```text
i.v1.Money original_amount = 1;
  optional .chesscom.api.v1.Money original_amount_with_taxes = 2;
  optional .chesscom.api.v1.Money discount_amount = 3;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 4;
  optional .chesscom.api.v1.Money subtotal_amount = 5;
  optional .chesscom.api.v1.Money subtotal_amount_with_taxes = 6;
  optional .chesscom.api.v1.Money credit_amount = 7;
  optional .chesscom.api.v1
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06417"></a>
## FND-06417: chesscom.payments.v1.TotalBreakdown.discount_amount_with_taxes = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money discount_amount_with_taxes = 4;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1801.

```text
i.v1.Money original_amount_with_taxes = 2;
  optional .chesscom.api.v1.Money discount_amount = 3;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 4;
  optional .chesscom.api.v1.Money subtotal_amount = 5;
  optional .chesscom.api.v1.Money subtotal_amount_with_taxes = 6;
  optional .chesscom.api.v1.Money credit_amount = 7;
  optional .chesscom.api.v1.Money credit_amount_with_taxes = 8;
  optional .chessc
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06418"></a>
## FND-06418: chesscom.payments.v1.TotalBreakdown.subtotal_amount = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money subtotal_amount = 5;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1867.

```text
i.v1.Money discount_amount = 3;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 4;
  optional .chesscom.api.v1.Money subtotal_amount = 5;
  optional .chesscom.api.v1.Money subtotal_amount_with_taxes = 6;
  optional .chesscom.api.v1.Money credit_amount = 7;
  optional .chesscom.api.v1.Money credit_amount_with_taxes = 8;
  optional .chesscom.api.v1.Money total_amount = 9;
  optional .chesscom.api.v1.Mone
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06419"></a>
## FND-06419: chesscom.payments.v1.TotalBreakdown.subtotal_amount_with_taxes = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money subtotal_amount_with_taxes = 6;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1922.

```text
i.v1.Money discount_amount_with_taxes = 4;
  optional .chesscom.api.v1.Money subtotal_amount = 5;
  optional .chesscom.api.v1.Money subtotal_amount_with_taxes = 6;
  optional .chesscom.api.v1.Money credit_amount = 7;
  optional .chesscom.api.v1.Money credit_amount_with_taxes = 8;
  optional .chesscom.api.v1.Money total_amount = 9;
  optional .chesscom.api.v1.Money tax_amount = 10;
  optional .chesscom.api.v1.Money to
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06420"></a>
## FND-06420: chesscom.payments.v1.TotalBreakdown.credit_amount = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money credit_amount = 7;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 1988.

```text
i.v1.Money subtotal_amount = 5;
  optional .chesscom.api.v1.Money subtotal_amount_with_taxes = 6;
  optional .chesscom.api.v1.Money credit_amount = 7;
  optional .chesscom.api.v1.Money credit_amount_with_taxes = 8;
  optional .chesscom.api.v1.Money total_amount = 9;
  optional .chesscom.api.v1.Money tax_amount = 10;
  optional .chesscom.api.v1.Money total_amount_with_taxes = 11;
}

message CheckoutTotalSummary {
  on
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06421"></a>
## FND-06421: chesscom.payments.v1.TotalBreakdown.credit_amount_with_taxes = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money credit_amount_with_taxes = 8;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2041.

```text
api.v1.Money subtotal_amount_with_taxes = 6;
  optional .chesscom.api.v1.Money credit_amount = 7;
  optional .chesscom.api.v1.Money credit_amount_with_taxes = 8;
  optional .chesscom.api.v1.Money total_amount = 9;
  optional .chesscom.api.v1.Money tax_amount = 10;
  optional .chesscom.api.v1.Money total_amount_with_taxes = 11;
}

message CheckoutTotalSummary {
  oneof _total_breakdown {
  .chesscom.payments.v1.TotalB
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06422"></a>
## FND-06422: chesscom.payments.v1.TotalBreakdown.total_amount = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money total_amount = 9;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2105.

```text
m.api.v1.Money credit_amount = 7;
  optional .chesscom.api.v1.Money credit_amount_with_taxes = 8;
  optional .chesscom.api.v1.Money total_amount = 9;
  optional .chesscom.api.v1.Money tax_amount = 10;
  optional .chesscom.api.v1.Money total_amount_with_taxes = 11;
}

message CheckoutTotalSummary {
  oneof _total_breakdown {
  .chesscom.payments.v1.TotalBreakdown total_breakdown = 2;
  }
  oneof _incentive {
  .chessc
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06423"></a>
## FND-06423: chesscom.payments.v1.TotalBreakdown.tax_amount = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money tax_amount = 10;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2157.

```text
om.api.v1.Money credit_amount_with_taxes = 8;
  optional .chesscom.api.v1.Money total_amount = 9;
  optional .chesscom.api.v1.Money tax_amount = 10;
  optional .chesscom.api.v1.Money total_amount_with_taxes = 11;
}

message CheckoutTotalSummary {
  oneof _total_breakdown {
  .chesscom.payments.v1.TotalBreakdown total_breakdown = 2;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 3;
  }
  oneof 
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06424"></a>
## FND-06424: chesscom.payments.v1.TotalBreakdown.total_amount_with_taxes = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money total_amount_with_taxes = 11;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2208.

```text
ional .chesscom.api.v1.Money total_amount = 9;
  optional .chesscom.api.v1.Money tax_amount = 10;
  optional .chesscom.api.v1.Money total_amount_with_taxes = 11;
}

message CheckoutTotalSummary {
  oneof _total_breakdown {
  .chesscom.payments.v1.TotalBreakdown total_breakdown = 2;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 3;
  }
  oneof _usd_fx_rate {
  float usd_fx_rate = 5;
  }
  oneof
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06425"></a>
## FND-06425: message declaration: chesscom.payments.v1.CheckoutTotalSummary

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CheckoutTotalSummary {

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2273.

```text
om.api.v1.Money tax_amount = 10;
  optional .chesscom.api.v1.Money total_amount_with_taxes = 11;
}

message CheckoutTotalSummary {
  oneof _total_breakdown {
  .chesscom.payments.v1.TotalBreakdown total_breakdown = 2;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 3;
  }
  oneof _usd_fx_rate {
  float usd_fx_rate = 5;
  }
  oneof _country {
  .chesscom.api.v1.Country country = 7;
  }
  optiona
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06426"></a>
## FND-06426: oneof declaration: chesscom.payments.v1.CheckoutTotalSummary._total_breakdown

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_breakdown {

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2306.

```text
  optional .chesscom.api.v1.Money total_amount_with_taxes = 11;
}

message CheckoutTotalSummary {
  oneof _total_breakdown {
  .chesscom.payments.v1.TotalBreakdown total_breakdown = 2;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 3;
  }
  oneof _usd_fx_rate {
  float usd_fx_rate = 5;
  }
  oneof _country {
  .chesscom.api.v1.Country country = 7;
  }
  optional .chesscom.payments.v1.ProductSu
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06427"></a>
## FND-06427: chesscom.payments.v1.CheckoutTotalSummary.total_breakdown = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.TotalBreakdown total_breakdown = 2;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2333.

```text
.Money total_amount_with_taxes = 11;
}

message CheckoutTotalSummary {
  oneof _total_breakdown {
  .chesscom.payments.v1.TotalBreakdown total_breakdown = 2;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 3;
  }
  oneof _usd_fx_rate {
  float usd_fx_rate = 5;
  }
  oneof _country {
  .chesscom.api.v1.Country country = 7;
  }
  optional .chesscom.payments.v1.ProductSummary product = 1;
  repeat
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06428"></a>
## FND-06428: oneof declaration: chesscom.payments.v1.CheckoutTotalSummary._incentive

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _incentive {

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 307.

```text
tails = 16;
  .chesscom.payments.v1.MembershipProductDetails membership_product_details = 17;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 13;
  }
  oneof _subtotal_amount_in_months {
  .chesscom.api.v1.Money subtotal_amount_in_months = 19;
  }
  oneof _subtotal_amount_with_taxes_in_months {
  .chesscom.api.v1.Money subtotal_amount_with_taxes_in_months = 20;
  }
  optional .chesscom.payments
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06429"></a>
## FND-06429: chesscom.payments.v1.CheckoutTotalSummary.incentive = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.Incentive incentive = 3;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2418.

```text
_breakdown {
  .chesscom.payments.v1.TotalBreakdown total_breakdown = 2;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 3;
  }
  oneof _usd_fx_rate {
  float usd_fx_rate = 5;
  }
  oneof _country {
  .chesscom.api.v1.Country country = 7;
  }
  optional .chesscom.payments.v1.ProductSummary product = 1;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 4;
  repeated .chesscom.payments.v1.Disc
```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06430"></a>
## FND-06430: oneof declaration: chesscom.payments.v1.CheckoutTotalSummary._usd_fx_rate

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _usd_fx_rate {

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2471.

```text
otal_breakdown = 2;
  }
  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 3;
  }
  oneof _usd_fx_rate {
  float usd_fx_rate = 5;
  }
  oneof _country {
  .chesscom.api.v1.Country country = 7;
  }
  optional .chesscom.payments.v1.ProductSummary product = 1;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 4;
  repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 6;
}

```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06431"></a>
## FND-06431: chesscom.payments.v1.CheckoutTotalSummary.usd_fx_rate = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float usd_fx_rate = 5;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2494.

```text

  oneof _incentive {
  .chesscom.payments.v1.Incentive incentive = 3;
  }
  oneof _usd_fx_rate {
  float usd_fx_rate = 5;
  }
  oneof _country {
  .chesscom.api.v1.Country country = 7;
  }
  optional .chesscom.payments.v1.ProductSummary product = 1;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 4;
  repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 6;
}

```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06432"></a>
## FND-06432: oneof declaration: chesscom.payments.v1.CheckoutTotalSummary._country

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _country {

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2523.

```text
scom.payments.v1.Incentive incentive = 3;
  }
  oneof _usd_fx_rate {
  float usd_fx_rate = 5;
  }
  oneof _country {
  .chesscom.api.v1.Country country = 7;
  }
  optional .chesscom.payments.v1.ProductSummary product = 1;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 4;
  repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 6;
}

```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06433"></a>
## FND-06433: chesscom.payments.v1.CheckoutTotalSummary.country = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.Country country = 7;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2542.

```text
centive incentive = 3;
  }
  oneof _usd_fx_rate {
  float usd_fx_rate = 5;
  }
  oneof _country {
  .chesscom.api.v1.Country country = 7;
  }
  optional .chesscom.payments.v1.ProductSummary product = 1;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 4;
  repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 6;
}

```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06434"></a>
## FND-06434: chesscom.payments.v1.CheckoutTotalSummary.product = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.ProductSummary product = 1;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2586.

```text
ate {
  float usd_fx_rate = 5;
  }
  oneof _country {
  .chesscom.api.v1.Country country = 7;
  }
  optional .chesscom.payments.v1.ProductSummary product = 1;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 4;
  repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 6;
}

```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06435"></a>
## FND-06435: chesscom.payments.v1.CheckoutTotalSummary.tax_lines = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.TaxLine tax_lines = 4;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2647.

```text
scom.api.v1.Country country = 7;
  }
  optional .chesscom.payments.v1.ProductSummary product = 1;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 4;
  repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 6;
}

```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06436"></a>
## FND-06436: chesscom.payments.v1.CheckoutTotalSummary.discount_amount_breakdown = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 6;

### Evidence

- **SRC-0485** `research/proto/chesscom/payments/v1/checkout_total.proto` — [preserved redacted evidence](../evidence/text/01d076c7bb1452a219aafd6bdb2357554bac0b24e2735b03fa89a549b522f46e.proto)
  Character offset 2703.

```text
m.payments.v1.ProductSummary product = 1;
  repeated .chesscom.payments.v1.TaxLine tax_lines = 4;
  repeated .chesscom.payments.v1.Discount discount_amount_breakdown = 6;
}

```

**Source references:** SRC-0485, SRC-1456  
**URL references:** None independently associated  
**Related findings:** FND-06384, FND-06385, FND-06386

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06437"></a>
## FND-06437: message declaration: chesscom.payments.v1.CountryPrice

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CountryPrice {

### Evidence

- **SRC-0486** `research/proto/chesscom/payments/v1/country_price.proto` — [preserved redacted evidence](../evidence/text/0b273c1b895add921ada664e7080e51aed05154a8ecb28573e060f46ae00da93.proto)
  Character offset 102.

```text
 source: chesscom/payments/v1/country_price.proto
// syntax: proto3

package chesscom.payments.v1;

message CountryPrice {
  optional string country_code = 1;
  optional .chesscom.api.v1.Money original_price = 2;
  optional .chesscom.api.v1.Money current_price = 3;
  optional .chesscom.api.v1.Money special_price = 4;
}

```

**Source references:** SRC-0486, SRC-1457  
**URL references:** None independently associated  
**Related findings:** FND-06438, FND-06439

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06438"></a>
## FND-06438: chesscom.payments.v1.CountryPrice.country_code = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string country_code = 1;

### Evidence

- **SRC-0486** `research/proto/chesscom/payments/v1/country_price.proto` — [preserved redacted evidence](../evidence/text/0b273c1b895add921ada664e7080e51aed05154a8ecb28573e060f46ae00da93.proto)
  Character offset 127.

```text
s/v1/country_price.proto
// syntax: proto3

package chesscom.payments.v1;

message CountryPrice {
  optional string country_code = 1;
  optional .chesscom.api.v1.Money original_price = 2;
  optional .chesscom.api.v1.Money current_price = 3;
  optional .chesscom.api.v1.Money special_price = 4;
}

```

**Source references:** SRC-0486, SRC-1457  
**URL references:** None independently associated  
**Related findings:** FND-06437, FND-06439

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06439"></a>
## FND-06439: chesscom.payments.v1.CountryPrice.original_price = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money original_price = 2;

### Evidence

- **SRC-0486** `research/proto/chesscom/payments/v1/country_price.proto` — [preserved redacted evidence](../evidence/text/0b273c1b895add921ada664e7080e51aed05154a8ecb28573e060f46ae00da93.proto)
  Character offset 163.

```text
proto3

package chesscom.payments.v1;

message CountryPrice {
  optional string country_code = 1;
  optional .chesscom.api.v1.Money original_price = 2;
  optional .chesscom.api.v1.Money current_price = 3;
  optional .chesscom.api.v1.Money special_price = 4;
}

```

**Source references:** SRC-0486, SRC-1457  
**URL references:** None independently associated  
**Related findings:** FND-06437, FND-06438

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06440"></a>
## FND-06440: chesscom.payments.v1.CountryPrice.current_price = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money current_price = 3;

### Evidence

- **SRC-0486** `research/proto/chesscom/payments/v1/country_price.proto` — [preserved redacted evidence](../evidence/text/0b273c1b895add921ada664e7080e51aed05154a8ecb28573e060f46ae00da93.proto)
  Character offset 217.

```text
Price {
  optional string country_code = 1;
  optional .chesscom.api.v1.Money original_price = 2;
  optional .chesscom.api.v1.Money current_price = 3;
  optional .chesscom.api.v1.Money special_price = 4;
}

```

**Source references:** SRC-0486, SRC-1457  
**URL references:** None independently associated  
**Related findings:** FND-06437, FND-06438, FND-06439

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06441"></a>
## FND-06441: chesscom.payments.v1.CountryPrice.special_price = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money special_price = 4;

### Evidence

- **SRC-0486** `research/proto/chesscom/payments/v1/country_price.proto` — [preserved redacted evidence](../evidence/text/0b273c1b895add921ada664e7080e51aed05154a8ecb28573e060f46ae00da93.proto)
  Character offset 270.

```text
l .chesscom.api.v1.Money original_price = 2;
  optional .chesscom.api.v1.Money current_price = 3;
  optional .chesscom.api.v1.Money special_price = 4;
}

```

**Source references:** SRC-0486, SRC-1457  
**URL references:** None independently associated  
**Related findings:** FND-06437, FND-06438, FND-06439

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06442"></a>
## FND-06442: message declaration: chesscom.payments.v1.Discount

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Discount {

### Evidence

- **SRC-0487** `research/proto/chesscom/payments/v1/discount.proto` — [preserved redacted evidence](../evidence/text/3905317533385c546efb529f63e59fd481ddf6761805f738288e1c5f3f8dcb3c.proto)
  Character offset 97.

```text
// source: chesscom/payments/v1/discount.proto
// syntax: proto3

package chesscom.payments.v1;

message Discount {
  oneof _incentive_offer_id {
  int32 incentive_offer_id = 3;
  }
  oneof _offer_id {
  string offer_id = 4;
  }
  optional .chesscom.api.v1.Money discount_amount = 1;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 2;
}

```

**Source references:** SRC-0487, SRC-1458  
**URL references:** None independently associated  
**Related findings:** FND-06443, FND-06444

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06443"></a>
## FND-06443: oneof declaration: chesscom.payments.v1.Discount._incentive_offer_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _incentive_offer_id {

### Evidence

- **SRC-0487** `research/proto/chesscom/payments/v1/discount.proto` — [preserved redacted evidence](../evidence/text/3905317533385c546efb529f63e59fd481ddf6761805f738288e1c5f3f8dcb3c.proto)
  Character offset 118.

```text
m/payments/v1/discount.proto
// syntax: proto3

package chesscom.payments.v1;

message Discount {
  oneof _incentive_offer_id {
  int32 incentive_offer_id = 3;
  }
  oneof _offer_id {
  string offer_id = 4;
  }
  optional .chesscom.api.v1.Money discount_amount = 1;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 2;
}

```

**Source references:** SRC-0487, SRC-1458  
**URL references:** None independently associated  
**Related findings:** FND-06442, FND-06444

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06444"></a>
## FND-06444: chesscom.payments.v1.Discount.incentive_offer_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 incentive_offer_id = 3;

### Evidence

- **SRC-0487** `research/proto/chesscom/payments/v1/discount.proto` — [preserved redacted evidence](../evidence/text/3905317533385c546efb529f63e59fd481ddf6761805f738288e1c5f3f8dcb3c.proto)
  Character offset 148.

```text
/ syntax: proto3

package chesscom.payments.v1;

message Discount {
  oneof _incentive_offer_id {
  int32 incentive_offer_id = 3;
  }
  oneof _offer_id {
  string offer_id = 4;
  }
  optional .chesscom.api.v1.Money discount_amount = 1;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 2;
}

```

**Source references:** SRC-0487, SRC-1458  
**URL references:** None independently associated  
**Related findings:** FND-06442, FND-06443

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06445"></a>
## FND-06445: oneof declaration: chesscom.payments.v1.Discount._offer_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _offer_id {

### Evidence

- **SRC-0487** `research/proto/chesscom/payments/v1/discount.proto` — [preserved redacted evidence](../evidence/text/3905317533385c546efb529f63e59fd481ddf6761805f738288e1c5f3f8dcb3c.proto)
  Character offset 184.

```text
ayments.v1;

message Discount {
  oneof _incentive_offer_id {
  int32 incentive_offer_id = 3;
  }
  oneof _offer_id {
  string offer_id = 4;
  }
  optional .chesscom.api.v1.Money discount_amount = 1;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 2;
}

```

**Source references:** SRC-0487, SRC-1458  
**URL references:** None independently associated  
**Related findings:** FND-06442, FND-06443, FND-06444

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06446"></a>
## FND-06446: chesscom.payments.v1.Discount.offer_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string offer_id = 4;

### Evidence

- **SRC-0487** `research/proto/chesscom/payments/v1/discount.proto` — [preserved redacted evidence](../evidence/text/3905317533385c546efb529f63e59fd481ddf6761805f738288e1c5f3f8dcb3c.proto)
  Character offset 204.

```text
 Discount {
  oneof _incentive_offer_id {
  int32 incentive_offer_id = 3;
  }
  oneof _offer_id {
  string offer_id = 4;
  }
  optional .chesscom.api.v1.Money discount_amount = 1;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 2;
}

```

**Source references:** SRC-0487, SRC-1458  
**URL references:** None independently associated  
**Related findings:** FND-06442, FND-06443, FND-06444

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06447"></a>
## FND-06447: chesscom.payments.v1.Discount.discount_amount = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money discount_amount = 1;

### Evidence

- **SRC-0487** `research/proto/chesscom/payments/v1/discount.proto` — [preserved redacted evidence](../evidence/text/3905317533385c546efb529f63e59fd481ddf6761805f738288e1c5f3f8dcb3c.proto)
  Character offset 231.

```text
ive_offer_id {
  int32 incentive_offer_id = 3;
  }
  oneof _offer_id {
  string offer_id = 4;
  }
  optional .chesscom.api.v1.Money discount_amount = 1;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 2;
}

```

**Source references:** SRC-0487, SRC-1458  
**URL references:** None independently associated  
**Related findings:** FND-06442, FND-06443, FND-06444

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06448"></a>
## FND-06448: chesscom.payments.v1.Discount.discount_amount_with_taxes = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money discount_amount_with_taxes = 2;

### Evidence

- **SRC-0487** `research/proto/chesscom/payments/v1/discount.proto` — [preserved redacted evidence](../evidence/text/3905317533385c546efb529f63e59fd481ddf6761805f738288e1c5f3f8dcb3c.proto)
  Character offset 286.

```text
eof _offer_id {
  string offer_id = 4;
  }
  optional .chesscom.api.v1.Money discount_amount = 1;
  optional .chesscom.api.v1.Money discount_amount_with_taxes = 2;
}

```

**Source references:** SRC-0487, SRC-1458  
**URL references:** None independently associated  
**Related findings:** FND-06442, FND-06443, FND-06444

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06449"></a>
## FND-06449: enum declaration: chesscom.payments.v1.AdditionalDataFieldType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum AdditionalDataFieldType {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 94.

```text
// source: chesscom/payments/v1/enums.proto
// syntax: proto3

package chesscom.payments.v1;

enum AdditionalDataFieldType {
  ADDITIONAL_DATA_FIELD_TYPE_UNSPECIFIED = 0;
  ADDITIONAL_DATA_FIELD_TYPE_SELECT = 1;
  ADDITIONAL_DATA_FIELD_TYPE_TEXT = 2;
  ADDITIONAL_DATA_FIELD_TYPE_EMAIL = 3;
  ADDITIONAL_DATA_FIELD_TYPE_TEL = 4;
}

enum CancellationContext {
  CANCELLATION_CONTEXT_UNSPECIFIED = 0;
  CANCELLATION_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06450"></a>
## FND-06450: chesscom.payments.v1.AdditionalDataFieldType.ADDITIONAL_DATA_FIELD_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADDITIONAL_DATA_FIELD_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 127.

```text
s/v1/enums.proto
// syntax: proto3

package chesscom.payments.v1;

enum AdditionalDataFieldType {
  ADDITIONAL_DATA_FIELD_TYPE_UNSPECIFIED = 0;
  ADDITIONAL_DATA_FIELD_TYPE_SELECT = 1;
  ADDITIONAL_DATA_FIELD_TYPE_TEXT = 2;
  ADDITIONAL_DATA_FIELD_TYPE_EMAIL = 3;
  ADDITIONAL_DATA_FIELD_TYPE_TEL = 4;
}

enum CancellationContext {
  CANCELLATION_CONTEXT_UNSPECIFIED = 0;
  CANCELLATION_CONTEXT_USER_DECISION = 1;
  CANC
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06451"></a>
## FND-06451: chesscom.payments.v1.AdditionalDataFieldType.ADDITIONAL_DATA_FIELD_TYPE_SELECT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADDITIONAL_DATA_FIELD_TYPE_SELECT = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 173.

```text
esscom.payments.v1;

enum AdditionalDataFieldType {
  ADDITIONAL_DATA_FIELD_TYPE_UNSPECIFIED = 0;
  ADDITIONAL_DATA_FIELD_TYPE_SELECT = 1;
  ADDITIONAL_DATA_FIELD_TYPE_TEXT = 2;
  ADDITIONAL_DATA_FIELD_TYPE_EMAIL = 3;
  ADDITIONAL_DATA_FIELD_TYPE_TEL = 4;
}

enum CancellationContext {
  CANCELLATION_CONTEXT_UNSPECIFIED = 0;
  CANCELLATION_CONTEXT_USER_DECISION = 1;
  CANCELLATION_CONTEXT_ADMIN_ACTION = 2;
  CANCELLAT
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06452"></a>
## FND-06452: chesscom.payments.v1.AdditionalDataFieldType.ADDITIONAL_DATA_FIELD_TYPE_TEXT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADDITIONAL_DATA_FIELD_TYPE_TEXT = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 214.

```text
ieldType {
  ADDITIONAL_DATA_FIELD_TYPE_UNSPECIFIED = 0;
  ADDITIONAL_DATA_FIELD_TYPE_SELECT = 1;
  ADDITIONAL_DATA_FIELD_TYPE_TEXT = 2;
  ADDITIONAL_DATA_FIELD_TYPE_EMAIL = 3;
  ADDITIONAL_DATA_FIELD_TYPE_TEL = 4;
}

enum CancellationContext {
  CANCELLATION_CONTEXT_UNSPECIFIED = 0;
  CANCELLATION_CONTEXT_USER_DECISION = 1;
  CANCELLATION_CONTEXT_ADMIN_ACTION = 2;
  CANCELLATION_CONTEXT_PAYMENT_PROCESSING = 3;
}

en
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06453"></a>
## FND-06453: chesscom.payments.v1.AdditionalDataFieldType.ADDITIONAL_DATA_FIELD_TYPE_EMAIL = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADDITIONAL_DATA_FIELD_TYPE_EMAIL = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 253.

```text
_UNSPECIFIED = 0;
  ADDITIONAL_DATA_FIELD_TYPE_SELECT = 1;
  ADDITIONAL_DATA_FIELD_TYPE_TEXT = 2;
  ADDITIONAL_DATA_FIELD_TYPE_EMAIL = 3;
  ADDITIONAL_DATA_FIELD_TYPE_TEL = 4;
}

enum CancellationContext {
  CANCELLATION_CONTEXT_UNSPECIFIED = 0;
  CANCELLATION_CONTEXT_USER_DECISION = 1;
  CANCELLATION_CONTEXT_ADMIN_ACTION = 2;
  CANCELLATION_CONTEXT_PAYMENT_PROCESSING = 3;
}

enum CancellationEffect {
  CANCELLATION_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06454"></a>
## FND-06454: chesscom.payments.v1.AdditionalDataFieldType.ADDITIONAL_DATA_FIELD_TYPE_TEL = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADDITIONAL_DATA_FIELD_TYPE_TEL = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 293.

```text
D_TYPE_SELECT = 1;
  ADDITIONAL_DATA_FIELD_TYPE_TEXT = 2;
  ADDITIONAL_DATA_FIELD_TYPE_EMAIL = 3;
  ADDITIONAL_DATA_FIELD_TYPE_TEL = 4;
}

enum CancellationContext {
  CANCELLATION_CONTEXT_UNSPECIFIED = 0;
  CANCELLATION_CONTEXT_USER_DECISION = 1;
  CANCELLATION_CONTEXT_ADMIN_ACTION = 2;
  CANCELLATION_CONTEXT_PAYMENT_PROCESSING = 3;
}

enum CancellationEffect {
  CANCELLATION_EFFECT_UNSPECIFIED = 0;
  CANCELLATION_E
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06455"></a>
## FND-06455: enum declaration: chesscom.payments.v1.CancellationContext

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CancellationContext {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 332.

```text
ELD_TYPE_TEXT = 2;
  ADDITIONAL_DATA_FIELD_TYPE_EMAIL = 3;
  ADDITIONAL_DATA_FIELD_TYPE_TEL = 4;
}

enum CancellationContext {
  CANCELLATION_CONTEXT_UNSPECIFIED = 0;
  CANCELLATION_CONTEXT_USER_DECISION = 1;
  CANCELLATION_CONTEXT_ADMIN_ACTION = 2;
  CANCELLATION_CONTEXT_PAYMENT_PROCESSING = 3;
}

enum CancellationEffect {
  CANCELLATION_EFFECT_UNSPECIFIED = 0;
  CANCELLATION_EFFECT_END_OF_PERIOD = 1;
  CANCELLATION
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06456"></a>
## FND-06456: chesscom.payments.v1.CancellationContext.CANCELLATION_CONTEXT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCELLATION_CONTEXT_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 361.

```text
AL_DATA_FIELD_TYPE_EMAIL = 3;
  ADDITIONAL_DATA_FIELD_TYPE_TEL = 4;
}

enum CancellationContext {
  CANCELLATION_CONTEXT_UNSPECIFIED = 0;
  CANCELLATION_CONTEXT_USER_DECISION = 1;
  CANCELLATION_CONTEXT_ADMIN_ACTION = 2;
  CANCELLATION_CONTEXT_PAYMENT_PROCESSING = 3;
}

enum CancellationEffect {
  CANCELLATION_EFFECT_UNSPECIFIED = 0;
  CANCELLATION_EFFECT_END_OF_PERIOD = 1;
  CANCELLATION_EFFECT_IMMEDIATE = 2;
}

enu
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06457"></a>
## FND-06457: chesscom.payments.v1.CancellationContext.CANCELLATION_CONTEXT_USER_DECISION = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCELLATION_CONTEXT_USER_DECISION = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 401.

```text
AL_DATA_FIELD_TYPE_TEL = 4;
}

enum CancellationContext {
  CANCELLATION_CONTEXT_UNSPECIFIED = 0;
  CANCELLATION_CONTEXT_USER_DECISION = 1;
  CANCELLATION_CONTEXT_ADMIN_ACTION = 2;
  CANCELLATION_CONTEXT_PAYMENT_PROCESSING = 3;
}

enum CancellationEffect {
  CANCELLATION_EFFECT_UNSPECIFIED = 0;
  CANCELLATION_EFFECT_END_OF_PERIOD = 1;
  CANCELLATION_EFFECT_IMMEDIATE = 2;
}

enum CancellationSource {
  CANCELLATION_SO
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06458"></a>
## FND-06458: chesscom.payments.v1.CancellationContext.CANCELLATION_CONTEXT_ADMIN_ACTION = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCELLATION_CONTEXT_ADMIN_ACTION = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 443.

```text
lationContext {
  CANCELLATION_CONTEXT_UNSPECIFIED = 0;
  CANCELLATION_CONTEXT_USER_DECISION = 1;
  CANCELLATION_CONTEXT_ADMIN_ACTION = 2;
  CANCELLATION_CONTEXT_PAYMENT_PROCESSING = 3;
}

enum CancellationEffect {
  CANCELLATION_EFFECT_UNSPECIFIED = 0;
  CANCELLATION_EFFECT_END_OF_PERIOD = 1;
  CANCELLATION_EFFECT_IMMEDIATE = 2;
}

enum CancellationSource {
  CANCELLATION_SOURCE_UNSPECIFIED = 0;
  CANCELLATION_SOURC
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06459"></a>
## FND-06459: chesscom.payments.v1.CancellationContext.CANCELLATION_CONTEXT_PAYMENT_PROCESSING = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCELLATION_CONTEXT_PAYMENT_PROCESSING = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 484.

```text
SPECIFIED = 0;
  CANCELLATION_CONTEXT_USER_DECISION = 1;
  CANCELLATION_CONTEXT_ADMIN_ACTION = 2;
  CANCELLATION_CONTEXT_PAYMENT_PROCESSING = 3;
}

enum CancellationEffect {
  CANCELLATION_EFFECT_UNSPECIFIED = 0;
  CANCELLATION_EFFECT_END_OF_PERIOD = 1;
  CANCELLATION_EFFECT_IMMEDIATE = 2;
}

enum CancellationSource {
  CANCELLATION_SOURCE_UNSPECIFIED = 0;
  CANCELLATION_SOURCE_VOLUNTARY = 1;
  CANCELLATION_SOURCE_IN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06460"></a>
## FND-06460: enum declaration: chesscom.payments.v1.CancellationEffect

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CancellationEffect {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 532.

```text
ION = 1;
  CANCELLATION_CONTEXT_ADMIN_ACTION = 2;
  CANCELLATION_CONTEXT_PAYMENT_PROCESSING = 3;
}

enum CancellationEffect {
  CANCELLATION_EFFECT_UNSPECIFIED = 0;
  CANCELLATION_EFFECT_END_OF_PERIOD = 1;
  CANCELLATION_EFFECT_IMMEDIATE = 2;
}

enum CancellationSource {
  CANCELLATION_SOURCE_UNSPECIFIED = 0;
  CANCELLATION_SOURCE_VOLUNTARY = 1;
  CANCELLATION_SOURCE_INVOLUNTARY = 2;
}

enum IncentiveChargeType {
  I
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06461"></a>
## FND-06461: chesscom.payments.v1.CancellationEffect.CANCELLATION_EFFECT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCELLATION_EFFECT_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 560.

```text
EXT_ADMIN_ACTION = 2;
  CANCELLATION_CONTEXT_PAYMENT_PROCESSING = 3;
}

enum CancellationEffect {
  CANCELLATION_EFFECT_UNSPECIFIED = 0;
  CANCELLATION_EFFECT_END_OF_PERIOD = 1;
  CANCELLATION_EFFECT_IMMEDIATE = 2;
}

enum CancellationSource {
  CANCELLATION_SOURCE_UNSPECIFIED = 0;
  CANCELLATION_SOURCE_VOLUNTARY = 1;
  CANCELLATION_SOURCE_INVOLUNTARY = 2;
}

enum IncentiveChargeType {
  INCENTIVE_CHARGE_TYPE_UNSPECI
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06462"></a>
## FND-06462: chesscom.payments.v1.CancellationEffect.CANCELLATION_EFFECT_END_OF_PERIOD = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCELLATION_EFFECT_END_OF_PERIOD = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 599.

```text
NTEXT_PAYMENT_PROCESSING = 3;
}

enum CancellationEffect {
  CANCELLATION_EFFECT_UNSPECIFIED = 0;
  CANCELLATION_EFFECT_END_OF_PERIOD = 1;
  CANCELLATION_EFFECT_IMMEDIATE = 2;
}

enum CancellationSource {
  CANCELLATION_SOURCE_UNSPECIFIED = 0;
  CANCELLATION_SOURCE_VOLUNTARY = 1;
  CANCELLATION_SOURCE_INVOLUNTARY = 2;
}

enum IncentiveChargeType {
  INCENTIVE_CHARGE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_CHARGE_TYPE_FIRST
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06463"></a>
## FND-06463: chesscom.payments.v1.CancellationEffect.CANCELLATION_EFFECT_IMMEDIATE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCELLATION_EFFECT_IMMEDIATE = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 640.

```text
cellationEffect {
  CANCELLATION_EFFECT_UNSPECIFIED = 0;
  CANCELLATION_EFFECT_END_OF_PERIOD = 1;
  CANCELLATION_EFFECT_IMMEDIATE = 2;
}

enum CancellationSource {
  CANCELLATION_SOURCE_UNSPECIFIED = 0;
  CANCELLATION_SOURCE_VOLUNTARY = 1;
  CANCELLATION_SOURCE_INVOLUNTARY = 2;
}

enum IncentiveChargeType {
  INCENTIVE_CHARGE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_CHARGE_TYPE_FIRST_CHARGE = 1;
  INCENTIVE_CHARGE_TYPE_ALL_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06464"></a>
## FND-06464: enum declaration: chesscom.payments.v1.CancellationSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CancellationSource {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 678.

```text
T_UNSPECIFIED = 0;
  CANCELLATION_EFFECT_END_OF_PERIOD = 1;
  CANCELLATION_EFFECT_IMMEDIATE = 2;
}

enum CancellationSource {
  CANCELLATION_SOURCE_UNSPECIFIED = 0;
  CANCELLATION_SOURCE_VOLUNTARY = 1;
  CANCELLATION_SOURCE_INVOLUNTARY = 2;
}

enum IncentiveChargeType {
  INCENTIVE_CHARGE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_CHARGE_TYPE_FIRST_CHARGE = 1;
  INCENTIVE_CHARGE_TYPE_ALL_CHARGES = 2;
  INCENTIVE_CHARGE_TYPE_N
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06465"></a>
## FND-06465: chesscom.payments.v1.CancellationSource.CANCELLATION_SOURCE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCELLATION_SOURCE_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 706.

```text
ATION_EFFECT_END_OF_PERIOD = 1;
  CANCELLATION_EFFECT_IMMEDIATE = 2;
}

enum CancellationSource {
  CANCELLATION_SOURCE_UNSPECIFIED = 0;
  CANCELLATION_SOURCE_VOLUNTARY = 1;
  CANCELLATION_SOURCE_INVOLUNTARY = 2;
}

enum IncentiveChargeType {
  INCENTIVE_CHARGE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_CHARGE_TYPE_FIRST_CHARGE = 1;
  INCENTIVE_CHARGE_TYPE_ALL_CHARGES = 2;
  INCENTIVE_CHARGE_TYPE_NEXT_X_CHARGES = 3;
}

enum I
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06466"></a>
## FND-06466: chesscom.payments.v1.CancellationSource.CANCELLATION_SOURCE_VOLUNTARY = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCELLATION_SOURCE_VOLUNTARY = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 745.

```text
LLATION_EFFECT_IMMEDIATE = 2;
}

enum CancellationSource {
  CANCELLATION_SOURCE_UNSPECIFIED = 0;
  CANCELLATION_SOURCE_VOLUNTARY = 1;
  CANCELLATION_SOURCE_INVOLUNTARY = 2;
}

enum IncentiveChargeType {
  INCENTIVE_CHARGE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_CHARGE_TYPE_FIRST_CHARGE = 1;
  INCENTIVE_CHARGE_TYPE_ALL_CHARGES = 2;
  INCENTIVE_CHARGE_TYPE_NEXT_X_CHARGES = 3;
}

enum IncentiveType {
  INCENTIVE_TYPE_UNSPECI
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06467"></a>
## FND-06467: chesscom.payments.v1.CancellationSource.CANCELLATION_SOURCE_INVOLUNTARY = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCELLATION_SOURCE_INVOLUNTARY = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 782.

```text
 CancellationSource {
  CANCELLATION_SOURCE_UNSPECIFIED = 0;
  CANCELLATION_SOURCE_VOLUNTARY = 1;
  CANCELLATION_SOURCE_INVOLUNTARY = 2;
}

enum IncentiveChargeType {
  INCENTIVE_CHARGE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_CHARGE_TYPE_FIRST_CHARGE = 1;
  INCENTIVE_CHARGE_TYPE_ALL_CHARGES = 2;
  INCENTIVE_CHARGE_TYPE_NEXT_X_CHARGES = 3;
}

enum IncentiveType {
  INCENTIVE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_TYPE_COUPON = 1
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06468"></a>
## FND-06468: enum declaration: chesscom.payments.v1.IncentiveChargeType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum IncentiveChargeType {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 822.

```text
RCE_UNSPECIFIED = 0;
  CANCELLATION_SOURCE_VOLUNTARY = 1;
  CANCELLATION_SOURCE_INVOLUNTARY = 2;
}

enum IncentiveChargeType {
  INCENTIVE_CHARGE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_CHARGE_TYPE_FIRST_CHARGE = 1;
  INCENTIVE_CHARGE_TYPE_ALL_CHARGES = 2;
  INCENTIVE_CHARGE_TYPE_NEXT_X_CHARGES = 3;
}

enum IncentiveType {
  INCENTIVE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_TYPE_COUPON = 1;
  INCENTIVE_TYPE_SPECIAL_OFFER = 2;
  
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06469"></a>
## FND-06469: chesscom.payments.v1.IncentiveChargeType.INCENTIVE_CHARGE_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_CHARGE_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 851.

```text
LATION_SOURCE_VOLUNTARY = 1;
  CANCELLATION_SOURCE_INVOLUNTARY = 2;
}

enum IncentiveChargeType {
  INCENTIVE_CHARGE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_CHARGE_TYPE_FIRST_CHARGE = 1;
  INCENTIVE_CHARGE_TYPE_ALL_CHARGES = 2;
  INCENTIVE_CHARGE_TYPE_NEXT_X_CHARGES = 3;
}

enum IncentiveType {
  INCENTIVE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_TYPE_COUPON = 1;
  INCENTIVE_TYPE_SPECIAL_OFFER = 2;
  INCENTIVE_TYPE_SPECIAL_OFFER_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06470"></a>
## FND-06470: chesscom.payments.v1.IncentiveChargeType.INCENTIVE_CHARGE_TYPE_FIRST_CHARGE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_CHARGE_TYPE_FIRST_CHARGE = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 892.

```text
ON_SOURCE_INVOLUNTARY = 2;
}

enum IncentiveChargeType {
  INCENTIVE_CHARGE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_CHARGE_TYPE_FIRST_CHARGE = 1;
  INCENTIVE_CHARGE_TYPE_ALL_CHARGES = 2;
  INCENTIVE_CHARGE_TYPE_NEXT_X_CHARGES = 3;
}

enum IncentiveType {
  INCENTIVE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_TYPE_COUPON = 1;
  INCENTIVE_TYPE_SPECIAL_OFFER = 2;
  INCENTIVE_TYPE_SPECIAL_OFFER_WINDOW = 3;
  INCENTIVE_TYPE_SPECIAL_OFFE
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06471"></a>
## FND-06471: chesscom.payments.v1.IncentiveChargeType.INCENTIVE_CHARGE_TYPE_ALL_CHARGES = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_CHARGE_TYPE_ALL_CHARGES = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 934.

```text
veChargeType {
  INCENTIVE_CHARGE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_CHARGE_TYPE_FIRST_CHARGE = 1;
  INCENTIVE_CHARGE_TYPE_ALL_CHARGES = 2;
  INCENTIVE_CHARGE_TYPE_NEXT_X_CHARGES = 3;
}

enum IncentiveType {
  INCENTIVE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_TYPE_COUPON = 1;
  INCENTIVE_TYPE_SPECIAL_OFFER = 2;
  INCENTIVE_TYPE_SPECIAL_OFFER_WINDOW = 3;
  INCENTIVE_TYPE_SPECIAL_OFFER_TENURE_BASED = 4;
  INCENTIVE_TYPE_STUDE
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06472"></a>
## FND-06472: chesscom.payments.v1.IncentiveChargeType.INCENTIVE_CHARGE_TYPE_NEXT_X_CHARGES = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_CHARGE_TYPE_NEXT_X_CHARGES = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 975.

```text
SPECIFIED = 0;
  INCENTIVE_CHARGE_TYPE_FIRST_CHARGE = 1;
  INCENTIVE_CHARGE_TYPE_ALL_CHARGES = 2;
  INCENTIVE_CHARGE_TYPE_NEXT_X_CHARGES = 3;
}

enum IncentiveType {
  INCENTIVE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_TYPE_COUPON = 1;
  INCENTIVE_TYPE_SPECIAL_OFFER = 2;
  INCENTIVE_TYPE_SPECIAL_OFFER_WINDOW = 3;
  INCENTIVE_TYPE_SPECIAL_OFFER_TENURE_BASED = 4;
  INCENTIVE_TYPE_STUDENT_DISCOUNT = 5;
  INCENTIVE_TYPE_REACTIV
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06473"></a>
## FND-06473: enum declaration: chesscom.payments.v1.IncentiveType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum IncentiveType {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1020.

```text
CHARGE = 1;
  INCENTIVE_CHARGE_TYPE_ALL_CHARGES = 2;
  INCENTIVE_CHARGE_TYPE_NEXT_X_CHARGES = 3;
}

enum IncentiveType {
  INCENTIVE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_TYPE_COUPON = 1;
  INCENTIVE_TYPE_SPECIAL_OFFER = 2;
  INCENTIVE_TYPE_SPECIAL_OFFER_WINDOW = 3;
  INCENTIVE_TYPE_SPECIAL_OFFER_TENURE_BASED = 4;
  INCENTIVE_TYPE_STUDENT_DISCOUNT = 5;
  INCENTIVE_TYPE_REACTIVATION_OFFER = 6;
  INCENTIVE_TYPE_FREEVIEW = 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06474"></a>
## FND-06474: chesscom.payments.v1.IncentiveType.INCENTIVE_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1043.

```text
_CHARGE_TYPE_ALL_CHARGES = 2;
  INCENTIVE_CHARGE_TYPE_NEXT_X_CHARGES = 3;
}

enum IncentiveType {
  INCENTIVE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_TYPE_COUPON = 1;
  INCENTIVE_TYPE_SPECIAL_OFFER = 2;
  INCENTIVE_TYPE_SPECIAL_OFFER_WINDOW = 3;
  INCENTIVE_TYPE_SPECIAL_OFFER_TENURE_BASED = 4;
  INCENTIVE_TYPE_STUDENT_DISCOUNT = 5;
  INCENTIVE_TYPE_REACTIVATION_OFFER = 6;
  INCENTIVE_TYPE_FREEVIEW = 7;
}

enum IncentiveOff
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
