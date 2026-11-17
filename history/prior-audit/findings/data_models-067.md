# data_models — findings 6601–6700

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-06875"></a>
## FND-06875: chesscom.payments.v1.SubmitCancellationSurveyRequest.feedback = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string feedback = 2;

### Evidence

- **SRC-0502** `research/proto/chesscom/payments/v1/membership_service.proto` — [preserved redacted evidence](../evidence/text/7aeff6a6dd7ca5c79ccd7a122049a900ee479ac6b4d1982ebc60bd14bd5e2243.proto)
  Character offset 246.

```text
ssage CancelMembershipResponse {
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

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06876"></a>
## FND-06876: chesscom.payments.v1.SubmitCancellationSurveyRequest.reason = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.CancelSurveyReason reason = 1;

### Evidence

- **SRC-0502** `research/proto/chesscom/payments/v1/membership_service.proto` — [preserved redacted evidence](../evidence/text/7aeff6a6dd7ca5c79ccd7a122049a900ee479ac6b4d1982ebc60bd14bd5e2243.proto)
  Character offset 273.

```text
nse {
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

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06877"></a>
## FND-06877: message declaration: chesscom.payments.v1.SubmitCancellationSurveyResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SubmitCancellationSurveyResponse {

### Evidence

- **SRC-0502** `research/proto/chesscom/payments/v1/membership_service.proto` — [preserved redacted evidence](../evidence/text/7aeff6a6dd7ca5c79ccd7a122049a900ee479ac6b4d1982ebc60bd14bd5e2243.proto)
  Character offset 338.

```text
ack {
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

<a id="FND-06878"></a>
## FND-06878: message declaration: chesscom.payments.v1.ExtendMembershipRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ExtendMembershipRequest {

### Evidence

- **SRC-0502** `research/proto/chesscom/payments/v1/membership_service.proto` — [preserved redacted evidence](../evidence/text/7aeff6a6dd7ca5c79ccd7a122049a900ee479ac6b4d1982ebc60bd14bd5e2243.proto)
  Character offset 384.

```text
hesscom.payments.v1.CancelSurveyReason reason = 1;
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

<a id="FND-06879"></a>
## FND-06879: message declaration: chesscom.payments.v1.ExtendMembershipResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ExtendMembershipResponse {

### Evidence

- **SRC-0502** `research/proto/chesscom/payments/v1/membership_service.proto` — [preserved redacted evidence](../evidence/text/7aeff6a6dd7ca5c79ccd7a122049a900ee479ac6b4d1982ebc60bd14bd5e2243.proto)
  Character offset 421.

```text
n reason = 1;
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

<a id="FND-06880"></a>
## FND-06880: message declaration: chesscom.payments.v1.GetPriceForAllCountriesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetPriceForAllCountriesRequest {

### Evidence

- **SRC-0503** `research/proto/chesscom/payments/v1/prices_service.proto` — [preserved redacted evidence](../evidence/text/be18ef2368577655af7d4d35020bcae98a7eef3fc850daee19d4bc79fa4b49d4.proto)
  Character offset 103.

```text
source: chesscom/payments/v1/prices_service.proto
// syntax: proto3

package chesscom.payments.v1;

message GetPriceForAllCountriesRequest {
  repeated string sku = 1;
}

message GetPriceForAllCountriesResponse {
  repeated .chesscom.payments.v1.ProductPrices products_prices = 1;
}

```

**Source references:** SRC-0503, SRC-1474  
**URL references:** None independently associated  
**Related findings:** FND-06881, FND-06882

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06881"></a>
## FND-06881: chesscom.payments.v1.GetPriceForAllCountriesRequest.sku = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string sku = 1;

### Evidence

- **SRC-0503** `research/proto/chesscom/payments/v1/prices_service.proto` — [preserved redacted evidence](../evidence/text/be18ef2368577655af7d4d35020bcae98a7eef3fc850daee19d4bc79fa4b49d4.proto)
  Character offset 146.

```text
.proto
// syntax: proto3

package chesscom.payments.v1;

message GetPriceForAllCountriesRequest {
  repeated string sku = 1;
}

message GetPriceForAllCountriesResponse {
  repeated .chesscom.payments.v1.ProductPrices products_prices = 1;
}

```

**Source references:** SRC-0503, SRC-1474  
**URL references:** None independently associated  
**Related findings:** FND-06880, FND-06882

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06882"></a>
## FND-06882: message declaration: chesscom.payments.v1.GetPriceForAllCountriesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetPriceForAllCountriesResponse {

### Evidence

- **SRC-0503** `research/proto/chesscom/payments/v1/prices_service.proto` — [preserved redacted evidence](../evidence/text/be18ef2368577655af7d4d35020bcae98a7eef3fc850daee19d4bc79fa4b49d4.proto)
  Character offset 174.

```text
ckage chesscom.payments.v1;

message GetPriceForAllCountriesRequest {
  repeated string sku = 1;
}

message GetPriceForAllCountriesResponse {
  repeated .chesscom.payments.v1.ProductPrices products_prices = 1;
}

```

**Source references:** SRC-0503, SRC-1474  
**URL references:** None independently associated  
**Related findings:** FND-06880, FND-06881

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06883"></a>
## FND-06883: chesscom.payments.v1.GetPriceForAllCountriesResponse.products_prices = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.ProductPrices products_prices = 1;

### Evidence

- **SRC-0503** `research/proto/chesscom/payments/v1/prices_service.proto` — [preserved redacted evidence](../evidence/text/be18ef2368577655af7d4d35020bcae98a7eef3fc850daee19d4bc79fa4b49d4.proto)
  Character offset 218.

```text
eForAllCountriesRequest {
  repeated string sku = 1;
}

message GetPriceForAllCountriesResponse {
  repeated .chesscom.payments.v1.ProductPrices products_prices = 1;
}

```

**Source references:** SRC-0503, SRC-1474  
**URL references:** None independently associated  
**Related findings:** FND-06880, FND-06881, FND-06882

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06884"></a>
## FND-06884: message declaration: chesscom.payments.v1.Product

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Product {

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 96.

```text
// source: chesscom/payments/v1/product.proto
// syntax: proto3

package chesscom.payments.v1;

message Product {
  oneof _subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  opt
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06885, FND-06886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06885"></a>
## FND-06885: oneof declaration: chesscom.payments.v1.Product._subscription

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _subscription {

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 116.

```text
com/payments/v1/product.proto
// syntax: proto3

package chesscom.payments.v1;

message Product {
  oneof _subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06886"></a>
## FND-06886: chesscom.payments.v1.Product.subscription = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.Subscription subscription = 4;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 140.

```text
proto
// syntax: proto3

package chesscom.payments.v1;

message Product {
  oneof _subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.a
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06887"></a>
## FND-06887: oneof declaration: chesscom.payments.v1.Product._description

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _description {

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 199.

```text
sage Product {
  oneof _subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06888"></a>
## FND-06888: chesscom.payments.v1.Product.description = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string description = 5;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 222.

```text
_subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06889"></a>
## FND-06889: oneof declaration: chesscom.payments.v1.Product._image

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _image {

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 252.

```text
yments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductS
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06890"></a>
## FND-06890: chesscom.payments.v1.Product.image = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string image = 6;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 269.

```text
ption subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof 
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06891"></a>
## FND-06891: oneof declaration: chesscom.payments.v1.Product._membership_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _membership_code {

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 293.

```text
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06892"></a>
## FND-06892: chesscom.payments.v1.Product.membership_code = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.MembershipLevel membership_code = 8;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 320.

```text
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 1;
  }
  oneof _price_amoun
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06893"></a>
## FND-06893: chesscom.payments.v1.Product.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 385.

```text
;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 1;
  }
  oneof _price_amount {
  .chesscom.api.v1.Money price_amount = 3;
  }
  oneof _subsc
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06894"></a>
## FND-06894: chesscom.payments.v1.Product.sku = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string sku = 2;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 413.

```text
de {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 1;
  }
  oneof _price_amount {
  .chesscom.api.v1.Money price_amount = 3;
  }
  oneof _subscription {
  .chesscom.paymen
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06895"></a>
## FND-06895: chesscom.payments.v1.Product.price_amount = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money price_amount = 3;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 440.

```text
1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 1;
  }
  oneof _price_amount {
  .chesscom.api.v1.Money price_amount = 3;
  }
  oneof _subscription {
  .chesscom.payments.v1.Subscription subscrip
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06896"></a>
## FND-06896: chesscom.payments.v1.Product.product_type = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.ProductType product_type = 7;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 492.

```text
l string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 1;
  }
  oneof _price_amount {
  .chesscom.api.v1.Money price_amount = 3;
  }
  oneof _subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string descri
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06897"></a>
## FND-06897: message declaration: chesscom.payments.v1.ProductSummary

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ProductSummary {

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 556.

```text
om.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 1;
  }
  oneof _price_amount {
  .chesscom.api.v1.Money price_amount = 3;
  }
  oneof _subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof 
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06898"></a>
## FND-06898: oneof declaration: chesscom.payments.v1.ProductSummary._name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _name {

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 583.

```text
t = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 1;
  }
  oneof _price_amount {
  .chesscom.api.v1.Money price_amount = 3;
  }
  oneof _subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _product_type {
  .chesscom
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06899"></a>
## FND-06899: chesscom.payments.v1.ProductSummary.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string name = 1;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 394.

```text
neof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 1;
  }
  oneof _price_amount {
  .chesscom.api.v1.Money price_amount = 3;
  }
  oneof _subscription {
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06900"></a>
## FND-06900: oneof declaration: chesscom.payments.v1.ProductSummary._price_amount

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _price_amount {

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 622.

```text
.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 1;
  }
  oneof _price_amount {
  .chesscom.api.v1.Money price_amount = 3;
  }
  oneof _subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _product_type {
  .chesscom.payments.v1.ProductType product_type =
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06901"></a>
## FND-06901: chesscom.payments.v1.ProductSummary.price_amount = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.Money price_amount = 3;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 449.

```text
hipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 1;
  }
  oneof _price_amount {
  .chesscom.api.v1.Money price_amount = 3;
  }
  oneof _subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06902"></a>
## FND-06902: oneof declaration: chesscom.payments.v1.ProductSummary._subscription

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _subscription {

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 116.

```text
com/payments/v1/product.proto
// syntax: proto3

package chesscom.payments.v1;

message Product {
  oneof _subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06903"></a>
## FND-06903: chesscom.payments.v1.ProductSummary.subscription = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.Subscription subscription = 4;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 140.

```text
proto
// syntax: proto3

package chesscom.payments.v1;

message Product {
  oneof _subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.a
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06904"></a>
## FND-06904: oneof declaration: chesscom.payments.v1.ProductSummary._description

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _description {

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 199.

```text
sage Product {
  oneof _subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06905"></a>
## FND-06905: chesscom.payments.v1.ProductSummary.description = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string description = 5;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 222.

```text
_subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06906"></a>
## FND-06906: oneof declaration: chesscom.payments.v1.ProductSummary._image

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _image {

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 252.

```text
yments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductS
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06907"></a>
## FND-06907: chesscom.payments.v1.ProductSummary.image = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string image = 6;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 269.

```text
ption subscription = 4;
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof 
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06908"></a>
## FND-06908: oneof declaration: chesscom.payments.v1.ProductSummary._product_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _product_type {

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 870.

```text
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _product_type {
  .chesscom.payments.v1.ProductType product_type = 7;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string sku = 2;
}

```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06909"></a>
## FND-06909: chesscom.payments.v1.ProductSummary.product_type = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.ProductType product_type = 7;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 501.

```text
name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 1;
  }
  oneof _price_amount {
  .chesscom.api.v1.Money price_amount = 3;
  }
  oneof _subscription {
  .chesscom.payments.v1.Subscription subscription = 4;
  }
  oneof _description {
  string description = 5
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06910"></a>
## FND-06910: oneof declaration: chesscom.payments.v1.ProductSummary._membership_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _membership_code {

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 293.

```text
  }
  oneof _description {
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06911"></a>
## FND-06911: chesscom.payments.v1.ProductSummary.membership_code = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.MembershipLevel membership_code = 8;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 320.

```text
  string description = 5;
  }
  oneof _image {
  string image = 6;
  }
  oneof _membership_code {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 1;
  }
  oneof _price_amoun
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06912"></a>
## FND-06912: chesscom.payments.v1.ProductSummary.sku = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string sku = 2;

### Evidence

- **SRC-0504** `research/proto/chesscom/payments/v1/product.proto` — [preserved redacted evidence](../evidence/text/415718484501f9f91ac7eab0b23d3e4fff2cd94487966f900afdb2ba48e7bedd.proto)
  Character offset 413.

```text
de {
  .chesscom.payments.v1.MembershipLevel membership_code = 8;
  }
  optional string name = 1;
  optional string sku = 2;
  optional .chesscom.api.v1.Money price_amount = 3;
  optional .chesscom.payments.v1.ProductType product_type = 7;
}

message ProductSummary {
  oneof _name {
  string name = 1;
  }
  oneof _price_amount {
  .chesscom.api.v1.Money price_amount = 3;
  }
  oneof _subscription {
  .chesscom.paymen
```

**Source references:** SRC-0504, SRC-1475  
**URL references:** None independently associated  
**Related findings:** FND-06884, FND-06885, FND-06886

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06913"></a>
## FND-06913: message declaration: chesscom.payments.v1.ProductPrices

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ProductPrices {

### Evidence

- **SRC-0505** `research/proto/chesscom/payments/v1/product_prices.proto` — [preserved redacted evidence](../evidence/text/caeaafb7cf0fbd63ad3419c5b799a2b67deac1980bd336cf09761e3ebee2ce4a.proto)
  Character offset 103.

```text
source: chesscom/payments/v1/product_prices.proto
// syntax: proto3

package chesscom.payments.v1;

message ProductPrices {
  optional string sku = 1;
  repeated .chesscom.payments.v1.CountryPrice country_prices = 2;
}

```

**Source references:** SRC-0505, SRC-1476  
**URL references:** None independently associated  
**Related findings:** FND-06914, FND-06915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06914"></a>
## FND-06914: chesscom.payments.v1.ProductPrices.sku = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string sku = 1;

### Evidence

- **SRC-0505** `research/proto/chesscom/payments/v1/product_prices.proto` — [preserved redacted evidence](../evidence/text/caeaafb7cf0fbd63ad3419c5b799a2b67deac1980bd336cf09761e3ebee2ce4a.proto)
  Character offset 129.

```text
v1/product_prices.proto
// syntax: proto3

package chesscom.payments.v1;

message ProductPrices {
  optional string sku = 1;
  repeated .chesscom.payments.v1.CountryPrice country_prices = 2;
}

```

**Source references:** SRC-0505, SRC-1476  
**URL references:** None independently associated  
**Related findings:** FND-06913, FND-06915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06915"></a>
## FND-06915: chesscom.payments.v1.ProductPrices.country_prices = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.CountryPrice country_prices = 2;

### Evidence

- **SRC-0505** `research/proto/chesscom/payments/v1/product_prices.proto` — [preserved redacted evidence](../evidence/text/caeaafb7cf0fbd63ad3419c5b799a2b67deac1980bd336cf09761e3ebee2ce4a.proto)
  Character offset 156.

```text
syntax: proto3

package chesscom.payments.v1;

message ProductPrices {
  optional string sku = 1;
  repeated .chesscom.payments.v1.CountryPrice country_prices = 2;
}

```

**Source references:** SRC-0505, SRC-1476  
**URL references:** None independently associated  
**Related findings:** FND-06913, FND-06914

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06916"></a>
## FND-06916: message declaration: chesscom.payments.v1.GetUserActiveMembershipRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserActiveMembershipRequest {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 104.

```text
ource: chesscom/payments/v1/product_service.proto
// syntax: proto3

package chesscom.payments.v1;

message GetUserActiveMembershipRequest {
}

message GetUserActiveMembershipResponse {
  oneof _product {
  .chesscom.payments.v1.Product product = 2;
  }
  oneof _will_expire {
  bool will_expire = 4;
  }
  oneof _status_code {
  .chesscom.payments.v1.StatusCode status_code = 6;
  }
  oneof _group_membership_type {
  .
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06917"></a>
## FND-06917: message declaration: chesscom.payments.v1.GetUserActiveMembershipResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserActiveMembershipResponse {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 148.

```text
proto
// syntax: proto3

package chesscom.payments.v1;

message GetUserActiveMembershipRequest {
}

message GetUserActiveMembershipResponse {
  oneof _product {
  .chesscom.payments.v1.Product product = 2;
  }
  oneof _will_expire {
  bool will_expire = 4;
  }
  oneof _status_code {
  .chesscom.payments.v1.StatusCode status_code = 6;
  }
  oneof _group_membership_type {
  .chesscom.payments.v1.GroupMembershipType gro
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06918"></a>
## FND-06918: oneof declaration: chesscom.payments.v1.GetUserActiveMembershipResponse._product

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _product {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 192.

```text
yments.v1;

message GetUserActiveMembershipRequest {
}

message GetUserActiveMembershipResponse {
  oneof _product {
  .chesscom.payments.v1.Product product = 2;
  }
  oneof _will_expire {
  bool will_expire = 4;
  }
  oneof _status_code {
  .chesscom.payments.v1.StatusCode status_code = 6;
  }
  oneof _group_membership_type {
  .chesscom.payments.v1.GroupMembershipType group_membership_type = 7;
  }
  oneof _renewal
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06919"></a>
## FND-06919: chesscom.payments.v1.GetUserActiveMembershipResponse.product = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.Product product = 2;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 211.

```text
 GetUserActiveMembershipRequest {
}

message GetUserActiveMembershipResponse {
  oneof _product {
  .chesscom.payments.v1.Product product = 2;
  }
  oneof _will_expire {
  bool will_expire = 4;
  }
  oneof _status_code {
  .chesscom.payments.v1.StatusCode status_code = 6;
  }
  oneof _group_membership_type {
  .chesscom.payments.v1.GroupMembershipType group_membership_type = 7;
  }
  oneof _renewal_date {
  .google.p
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06920"></a>
## FND-06920: oneof declaration: chesscom.payments.v1.GetUserActiveMembershipResponse._will_expire

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _will_expire {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 260.

```text
serActiveMembershipResponse {
  oneof _product {
  .chesscom.payments.v1.Product product = 2;
  }
  oneof _will_expire {
  bool will_expire = 4;
  }
  oneof _status_code {
  .chesscom.payments.v1.StatusCode status_code = 6;
  }
  oneof _group_membership_type {
  .chesscom.payments.v1.GroupMembershipType group_membership_type = 7;
  }
  oneof _renewal_date {
  .google.protobuf.Timestamp renewal_date = 8;
  }
  oneof _
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06921"></a>
## FND-06921: chesscom.payments.v1.GetUserActiveMembershipResponse.will_expire = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool will_expire = 4;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 283.

```text
onse {
  oneof _product {
  .chesscom.payments.v1.Product product = 2;
  }
  oneof _will_expire {
  bool will_expire = 4;
  }
  oneof _status_code {
  .chesscom.payments.v1.StatusCode status_code = 6;
  }
  oneof _group_membership_type {
  .chesscom.payments.v1.GroupMembershipType group_membership_type = 7;
  }
  oneof _renewal_date {
  .google.protobuf.Timestamp renewal_date = 8;
  }
  oneof _renewal_price {
  .ches
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06922"></a>
## FND-06922: oneof declaration: chesscom.payments.v1.GetUserActiveMembershipResponse._status_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _status_code {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 311.

```text
.chesscom.payments.v1.Product product = 2;
  }
  oneof _will_expire {
  bool will_expire = 4;
  }
  oneof _status_code {
  .chesscom.payments.v1.StatusCode status_code = 6;
  }
  oneof _group_membership_type {
  .chesscom.payments.v1.GroupMembershipType group_membership_type = 7;
  }
  oneof _renewal_date {
  .google.protobuf.Timestamp renewal_date = 8;
  }
  oneof _renewal_price {
  .chesscom.api.v1.Money renewal_pr
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06923"></a>
## FND-06923: chesscom.payments.v1.GetUserActiveMembershipResponse.status_code = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.StatusCode status_code = 6;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 334.

```text
roduct product = 2;
  }
  oneof _will_expire {
  bool will_expire = 4;
  }
  oneof _status_code {
  .chesscom.payments.v1.StatusCode status_code = 6;
  }
  oneof _group_membership_type {
  .chesscom.payments.v1.GroupMembershipType group_membership_type = 7;
  }
  oneof _renewal_date {
  .google.protobuf.Timestamp renewal_date = 8;
  }
  oneof _renewal_price {
  .chesscom.api.v1.Money renewal_price = 9;
  }
  oneof _e
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06924"></a>
## FND-06924: oneof declaration: chesscom.payments.v1.GetUserActiveMembershipResponse._group_membership_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _group_membership_type {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 390.

```text
ll_expire = 4;
  }
  oneof _status_code {
  .chesscom.payments.v1.StatusCode status_code = 6;
  }
  oneof _group_membership_type {
  .chesscom.payments.v1.GroupMembershipType group_membership_type = 7;
  }
  oneof _renewal_date {
  .google.protobuf.Timestamp renewal_date = 8;
  }
  oneof _renewal_price {
  .chesscom.api.v1.Money renewal_price = 9;
  }
  oneof _expiry_date {
  .google.protobuf.Timestamp expiry_date = 
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06925"></a>
## FND-06925: chesscom.payments.v1.GetUserActiveMembershipResponse.group_membership_type = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.GroupMembershipType group_membership_type = 7;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 423.

```text
s_code {
  .chesscom.payments.v1.StatusCode status_code = 6;
  }
  oneof _group_membership_type {
  .chesscom.payments.v1.GroupMembershipType group_membership_type = 7;
  }
  oneof _renewal_date {
  .google.protobuf.Timestamp renewal_date = 8;
  }
  oneof _renewal_price {
  .chesscom.api.v1.Money renewal_price = 9;
  }
  oneof _expiry_date {
  .google.protobuf.Timestamp expiry_date = 10;
  }
  oneof _membership_descr
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06926"></a>
## FND-06926: oneof declaration: chesscom.payments.v1.GetUserActiveMembershipResponse._renewal_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _renewal_date {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 498.

```text
roup_membership_type {
  .chesscom.payments.v1.GroupMembershipType group_membership_type = 7;
  }
  oneof _renewal_date {
  .google.protobuf.Timestamp renewal_date = 8;
  }
  oneof _renewal_price {
  .chesscom.api.v1.Money renewal_price = 9;
  }
  oneof _expiry_date {
  .google.protobuf.Timestamp expiry_date = 10;
  }
  oneof _membership_description {
  string membership_description = 11;
  }
  oneof _is_gift {
  boo
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06927"></a>
## FND-06927: chesscom.payments.v1.GetUserActiveMembershipResponse.renewal_date = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp renewal_date = 8;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 522.

```text
 .chesscom.payments.v1.GroupMembershipType group_membership_type = 7;
  }
  oneof _renewal_date {
  .google.protobuf.Timestamp renewal_date = 8;
  }
  oneof _renewal_price {
  .chesscom.api.v1.Money renewal_price = 9;
  }
  oneof _expiry_date {
  .google.protobuf.Timestamp expiry_date = 10;
  }
  oneof _membership_description {
  string membership_description = 11;
  }
  oneof _is_gift {
  bool is_gift = 12;
  }
  on
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06928"></a>
## FND-06928: oneof declaration: chesscom.payments.v1.GetUserActiveMembershipResponse._renewal_price

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _renewal_price {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 573.

```text
mbership_type = 7;
  }
  oneof _renewal_date {
  .google.protobuf.Timestamp renewal_date = 8;
  }
  oneof _renewal_price {
  .chesscom.api.v1.Money renewal_price = 9;
  }
  oneof _expiry_date {
  .google.protobuf.Timestamp expiry_date = 10;
  }
  oneof _membership_description {
  string membership_description = 11;
  }
  oneof _is_gift {
  bool is_gift = 12;
  }
  oneof _is_free {
  bool is_free = 13;
  }
  oneof _ha
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06929"></a>
## FND-06929: chesscom.payments.v1.GetUserActiveMembershipResponse.renewal_price = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.Money renewal_price = 9;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 598.

```text
oneof _renewal_date {
  .google.protobuf.Timestamp renewal_date = 8;
  }
  oneof _renewal_price {
  .chesscom.api.v1.Money renewal_price = 9;
  }
  oneof _expiry_date {
  .google.protobuf.Timestamp expiry_date = 10;
  }
  oneof _membership_description {
  string membership_description = 11;
  }
  oneof _is_gift {
  bool is_gift = 12;
  }
  oneof _is_free {
  bool is_free = 13;
  }
  oneof _has_active_billing {
  bool
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06930"></a>
## FND-06930: oneof declaration: chesscom.payments.v1.GetUserActiveMembershipResponse._expiry_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _expiry_date {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 646.

```text
mp renewal_date = 8;
  }
  oneof _renewal_price {
  .chesscom.api.v1.Money renewal_price = 9;
  }
  oneof _expiry_date {
  .google.protobuf.Timestamp expiry_date = 10;
  }
  oneof _membership_description {
  string membership_description = 11;
  }
  oneof _is_gift {
  bool is_gift = 12;
  }
  oneof _is_free {
  bool is_free = 13;
  }
  oneof _has_active_billing {
  bool has_active_billing = 14;
  }
  oneof _disallow_
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06931"></a>
## FND-06931: chesscom.payments.v1.GetUserActiveMembershipResponse.expiry_date = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp expiry_date = 10;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 669.

```text
}
  oneof _renewal_price {
  .chesscom.api.v1.Money renewal_price = 9;
  }
  oneof _expiry_date {
  .google.protobuf.Timestamp expiry_date = 10;
  }
  oneof _membership_description {
  string membership_description = 11;
  }
  oneof _is_gift {
  bool is_gift = 12;
  }
  oneof _is_free {
  bool is_free = 13;
  }
  oneof _has_active_billing {
  bool has_active_billing = 14;
  }
  oneof _disallow_cancellation_reason {
 
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06932"></a>
## FND-06932: oneof declaration: chesscom.payments.v1.GetUserActiveMembershipResponse._membership_description

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _membership_description {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 720.

```text
 renewal_price = 9;
  }
  oneof _expiry_date {
  .google.protobuf.Timestamp expiry_date = 10;
  }
  oneof _membership_description {
  string membership_description = 11;
  }
  oneof _is_gift {
  bool is_gift = 12;
  }
  oneof _is_free {
  bool is_free = 13;
  }
  oneof _has_active_billing {
  bool has_active_billing = 14;
  }
  oneof _disallow_cancellation_reason {
  string disallow_cancellation_reason = 15;
  }
  on
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06933"></a>
## FND-06933: chesscom.payments.v1.GetUserActiveMembershipResponse.membership_description = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string membership_description = 11;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 754.

```text
xpiry_date {
  .google.protobuf.Timestamp expiry_date = 10;
  }
  oneof _membership_description {
  string membership_description = 11;
  }
  oneof _is_gift {
  bool is_gift = 12;
  }
  oneof _is_free {
  bool is_free = 13;
  }
  oneof _has_active_billing {
  bool has_active_billing = 14;
  }
  oneof _disallow_cancellation_reason {
  string disallow_cancellation_reason = 15;
  }
  oneof _primary_account_holder {
  .c
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06934"></a>
## FND-06934: oneof declaration: chesscom.payments.v1.GetUserActiveMembershipResponse._is_gift

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_gift {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 796.

```text
expiry_date = 10;
  }
  oneof _membership_description {
  string membership_description = 11;
  }
  oneof _is_gift {
  bool is_gift = 12;
  }
  oneof _is_free {
  bool is_free = 13;
  }
  oneof _has_active_billing {
  bool has_active_billing = 14;
  }
  oneof _disallow_cancellation_reason {
  string disallow_cancellation_reason = 15;
  }
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_h
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06935"></a>
## FND-06935: chesscom.payments.v1.GetUserActiveMembershipResponse.is_gift = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_gift = 12;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 815.

```text
 }
  oneof _membership_description {
  string membership_description = 11;
  }
  oneof _is_gift {
  bool is_gift = 12;
  }
  oneof _is_free {
  bool is_free = 13;
  }
  oneof _has_active_billing {
  bool has_active_billing = 14;
  }
  oneof _disallow_cancellation_reason {
  string disallow_cancellation_reason = 15;
  }
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 16;
  }
  o
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06936"></a>
## FND-06936: oneof declaration: chesscom.payments.v1.GetUserActiveMembershipResponse._is_free

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_free {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 840.

```text
scription {
  string membership_description = 11;
  }
  oneof _is_gift {
  bool is_gift = 12;
  }
  oneof _is_free {
  bool is_free = 13;
  }
  oneof _has_active_billing {
  bool has_active_billing = 14;
  }
  oneof _disallow_cancellation_reason {
  string disallow_cancellation_reason = 15;
  }
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 16;
  }
  optional .chesscom.payment
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06937"></a>
## FND-06937: chesscom.payments.v1.GetUserActiveMembershipResponse.is_free = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_free = 13;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 859.

```text
g membership_description = 11;
  }
  oneof _is_gift {
  bool is_gift = 12;
  }
  oneof _is_free {
  bool is_free = 13;
  }
  oneof _has_active_billing {
  bool has_active_billing = 14;
  }
  oneof _disallow_cancellation_reason {
  string disallow_cancellation_reason = 15;
  }
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 16;
  }
  optional .chesscom.payments.v1.MembershipLeve
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06938"></a>
## FND-06938: oneof declaration: chesscom.payments.v1.GetUserActiveMembershipResponse._has_active_billing

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _has_active_billing {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 884.

```text
= 11;
  }
  oneof _is_gift {
  bool is_gift = 12;
  }
  oneof _is_free {
  bool is_free = 13;
  }
  oneof _has_active_billing {
  bool has_active_billing = 14;
  }
  oneof _disallow_cancellation_reason {
  string disallow_cancellation_reason = 15;
  }
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 16;
  }
  optional .chesscom.payments.v1.MembershipLevel membership_level = 1;
 
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06939"></a>
## FND-06939: chesscom.payments.v1.GetUserActiveMembershipResponse.has_active_billing = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool has_active_billing = 14;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 914.

```text
 bool is_gift = 12;
  }
  oneof _is_free {
  bool is_free = 13;
  }
  oneof _has_active_billing {
  bool has_active_billing = 14;
  }
  oneof _disallow_cancellation_reason {
  string disallow_cancellation_reason = 15;
  }
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 16;
  }
  optional .chesscom.payments.v1.MembershipLevel membership_level = 1;
  optional string membership_na
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06940"></a>
## FND-06940: oneof declaration: chesscom.payments.v1.GetUserActiveMembershipResponse._disallow_cancellation_reason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _disallow_cancellation_reason {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 950.

```text
free {
  bool is_free = 13;
  }
  oneof _has_active_billing {
  bool has_active_billing = 14;
  }
  oneof _disallow_cancellation_reason {
  string disallow_cancellation_reason = 15;
  }
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 16;
  }
  optional .chesscom.payments.v1.MembershipLevel membership_level = 1;
  optional string membership_name = 3;
  optional bool is_lifetime 
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06941"></a>
## FND-06941: chesscom.payments.v1.GetUserActiveMembershipResponse.disallow_cancellation_reason = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string disallow_cancellation_reason = 15;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 990.

```text
_has_active_billing {
  bool has_active_billing = 14;
  }
  oneof _disallow_cancellation_reason {
  string disallow_cancellation_reason = 15;
  }
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 16;
  }
  optional .chesscom.payments.v1.MembershipLevel membership_level = 1;
  optional string membership_name = 3;
  optional bool is_lifetime = 5;
}

message GetUserIsEligibleToResta
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06942"></a>
## FND-06942: oneof declaration: chesscom.payments.v1.GetUserActiveMembershipResponse._primary_account_holder

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _primary_account_holder {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 1038.

```text
= 14;
  }
  oneof _disallow_cancellation_reason {
  string disallow_cancellation_reason = 15;
  }
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 16;
  }
  optional .chesscom.payments.v1.MembershipLevel membership_level = 1;
  optional string membership_name = 3;
  optional bool is_lifetime = 5;
}

message GetUserIsEligibleToRestartMembershipRequest {
}

message GetUserIsEligib
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06943"></a>
## FND-06943: chesscom.payments.v1.GetUserActiveMembershipResponse.primary_account_holder = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user.v1.UserView primary_account_holder = 16;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 1072.

```text
lation_reason {
  string disallow_cancellation_reason = 15;
  }
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 16;
  }
  optional .chesscom.payments.v1.MembershipLevel membership_level = 1;
  optional string membership_name = 3;
  optional bool is_lifetime = 5;
}

message GetUserIsEligibleToRestartMembershipRequest {
}

message GetUserIsEligibleToRestartMembershipResponse {
  
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06944"></a>
## FND-06944: chesscom.payments.v1.GetUserActiveMembershipResponse.membership_level = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.MembershipLevel membership_level = 1;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 1134.

```text
}
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 16;
  }
  optional .chesscom.payments.v1.MembershipLevel membership_level = 1;
  optional string membership_name = 3;
  optional bool is_lifetime = 5;
}

message GetUserIsEligibleToRestartMembershipRequest {
}

message GetUserIsEligibleToRestartMembershipResponse {
  optional bool is_eligible = 1;
}

message RestartMembershipReq
```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06945"></a>
## FND-06945: chesscom.payments.v1.GetUserActiveMembershipResponse.membership_name = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string membership_name = 3;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 1205.

```text
y_account_holder = 16;
  }
  optional .chesscom.payments.v1.MembershipLevel membership_level = 1;
  optional string membership_name = 3;
  optional bool is_lifetime = 5;
}

message GetUserIsEligibleToRestartMembershipRequest {
}

message GetUserIsEligibleToRestartMembershipResponse {
  optional bool is_eligible = 1;
}

message RestartMembershipRequest {
}

message RestartMembershipResponse {
}

```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06946"></a>
## FND-06946: chesscom.payments.v1.GetUserActiveMembershipResponse.is_lifetime = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_lifetime = 5;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 1244.

```text
chesscom.payments.v1.MembershipLevel membership_level = 1;
  optional string membership_name = 3;
  optional bool is_lifetime = 5;
}

message GetUserIsEligibleToRestartMembershipRequest {
}

message GetUserIsEligibleToRestartMembershipResponse {
  optional bool is_eligible = 1;
}

message RestartMembershipRequest {
}

message RestartMembershipResponse {
}

```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06947"></a>
## FND-06947: message declaration: chesscom.payments.v1.GetUserIsEligibleToRestartMembershipRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserIsEligibleToRestartMembershipRequest {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 1278.

```text
el membership_level = 1;
  optional string membership_name = 3;
  optional bool is_lifetime = 5;
}

message GetUserIsEligibleToRestartMembershipRequest {
}

message GetUserIsEligibleToRestartMembershipResponse {
  optional bool is_eligible = 1;
}

message RestartMembershipRequest {
}

message RestartMembershipResponse {
}

```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06948"></a>
## FND-06948: message declaration: chesscom.payments.v1.GetUserIsEligibleToRestartMembershipResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserIsEligibleToRestartMembershipResponse {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 1335.

```text
e = 3;
  optional bool is_lifetime = 5;
}

message GetUserIsEligibleToRestartMembershipRequest {
}

message GetUserIsEligibleToRestartMembershipResponse {
  optional bool is_eligible = 1;
}

message RestartMembershipRequest {
}

message RestartMembershipResponse {
}

```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06949"></a>
## FND-06949: chesscom.payments.v1.GetUserIsEligibleToRestartMembershipResponse.is_eligible = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_eligible = 1;

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 1392.

```text
rIsEligibleToRestartMembershipRequest {
}

message GetUserIsEligibleToRestartMembershipResponse {
  optional bool is_eligible = 1;
}

message RestartMembershipRequest {
}

message RestartMembershipResponse {
}

```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06950"></a>
## FND-06950: message declaration: chesscom.payments.v1.RestartMembershipRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RestartMembershipRequest {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 1426.

```text
est {
}

message GetUserIsEligibleToRestartMembershipResponse {
  optional bool is_eligible = 1;
}

message RestartMembershipRequest {
}

message RestartMembershipResponse {
}

```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06951"></a>
## FND-06951: message declaration: chesscom.payments.v1.RestartMembershipResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RestartMembershipResponse {

### Evidence

- **SRC-0506** `research/proto/chesscom/payments/v1/product_service.proto` — [preserved redacted evidence](../evidence/text/0817fb12f2e1c802ca5b039b33b86f3a26fff83076320a9ade9fe1401c2e4784.proto)
  Character offset 1464.

```text
startMembershipResponse {
  optional bool is_eligible = 1;
}

message RestartMembershipRequest {
}

message RestartMembershipResponse {
}

```

**Source references:** SRC-0506, SRC-1477  
**URL references:** None independently associated  
**Related findings:** FND-06916, FND-06917, FND-06918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06952"></a>
## FND-06952: message declaration: chesscom.payments.v1.IssueRefundRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message IssueRefundRequest {

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 103.

```text
source: chesscom/payments/v1/refund_service.proto
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
  optional boo
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06953, FND-06954

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06953"></a>
## FND-06953: chesscom.payments.v1.IssueRefundRequest.user_uuid = 1

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
**Related findings:** FND-06952, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06954"></a>
## FND-06954: chesscom.payments.v1.IssueRefundRequest.charge_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string charge_id = 2;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 167.

```text
to3

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
  optional int32 refunded_cents = 2;
  o
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06955"></a>
## FND-06955: chesscom.payments.v1.IssueRefundRequest.amount_cents = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 amount_cents = 4;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 200.

```text
;

message IssueRefundRequest {
  optional string user_uuid = 1;
  optional string charge_id = 2;
  optional int32 amount_cents = 4;
  optional .chesscom.support.v1.SupportActionContext context = 6;
  optional .chesscom.payments.v1.CancellationEffect cancellation_effect = 8;
}

message IssueRefundResponse {
  optional bool already_refunded = 1;
  optional int32 refunded_cents = 2;
  optional .chesscom.support.v1.Supp
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06956"></a>
## FND-06956: chesscom.payments.v1.IssueRefundRequest.context = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionContext context = 6;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 235.

```text
ptional string user_uuid = 1;
  optional string charge_id = 2;
  optional int32 amount_cents = 4;
  optional .chesscom.support.v1.SupportActionContext context = 6;
  optional .chesscom.payments.v1.CancellationEffect cancellation_effect = 8;
}

message IssueRefundResponse {
  optional bool already_refunded = 1;
  optional int32 refunded_cents = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;

```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06957"></a>
## FND-06957: chesscom.payments.v1.IssueRefundRequest.cancellation_effect = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.CancellationEffect cancellation_effect = 8;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 301.

```text
ptional int32 amount_cents = 4;
  optional .chesscom.support.v1.SupportActionContext context = 6;
  optional .chesscom.payments.v1.CancellationEffect cancellation_effect = 8;
}

message IssueRefundResponse {
  optional bool already_refunded = 1;
  optional int32 refunded_cents = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
  optional string refund_id = 4;
}

message ListChargesRequest {
 
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06958"></a>
## FND-06958: message declaration: chesscom.payments.v1.IssueRefundResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message IssueRefundResponse {

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 379.

```text
ontext context = 6;
  optional .chesscom.payments.v1.CancellationEffect cancellation_effect = 8;
}

message IssueRefundResponse {
  optional bool already_refunded = 1;
  optional int32 refunded_cents = 2;
  optional .chesscom.support.v1.SupportActionResult action_result = 3;
  optional string refund_id = 4;
}

message ListChargesRequest {
  optional string user_uuid = 1;
  optional int32 limit = 2;
}

message ListCha
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06959"></a>
## FND-06959: chesscom.payments.v1.IssueRefundResponse.already_refunded = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool already_refunded = 1;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 411.

```text
chesscom.payments.v1.CancellationEffect cancellation_effect = 8;
}

message IssueRefundResponse {
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
  repeated .chess
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06960"></a>
## FND-06960: chesscom.payments.v1.IssueRefundResponse.refunded_cents = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 refunded_cents = 2;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 449.

```text
t cancellation_effect = 8;
}

message IssueRefundResponse {
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

```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06961"></a>
## FND-06961: chesscom.payments.v1.IssueRefundResponse.action_result = 3

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

<a id="FND-06962"></a>
## FND-06962: chesscom.payments.v1.IssueRefundResponse.refund_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string refund_id = 4;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 557.

```text
 int32 refunded_cents = 2;
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
  oneof identifier {
  string adyen_psp_reference = 1;
  string google_play_or
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06963"></a>
## FND-06963: message declaration: chesscom.payments.v1.ListChargesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListChargesRequest {

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 591.

```text
nal .chesscom.support.v1.SupportActionResult action_result = 3;
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
  oneof identifier {
  string adyen_psp_reference = 1;
  string google_play_order_id = 2;
  string apple_transac
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06964"></a>
## FND-06964: chesscom.payments.v1.ListChargesRequest.user_uuid = 1

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

<a id="FND-06965"></a>
## FND-06965: chesscom.payments.v1.ListChargesRequest.limit = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 limit = 2;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 655.

```text
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
  oneof identifier {
  string adyen_psp_reference = 1;
  string google_play_order_id = 2;
  string apple_transaction_id = 3;
  string apple_order_id = 5;
  string chesscom_orde
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06966"></a>
## FND-06966: message declaration: chesscom.payments.v1.ListChargesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListChargesResponse {

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 684.

```text
 4;
}

message ListChargesRequest {
  optional string user_uuid = 1;
  optional int32 limit = 2;
}

message ListChargesResponse {
  repeated .chesscom.payments.v1.Charge charges = 1;
}

message FindChargesRequest {
  oneof identifier {
  string adyen_psp_reference = 1;
  string google_play_order_id = 2;
  string apple_transaction_id = 3;
  string apple_order_id = 5;
  string chesscom_order_number = 6;
  }
  optional 
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06967"></a>
## FND-06967: chesscom.payments.v1.ListChargesResponse.charges = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.Charge charges = 1;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 716.

```text
t {
  optional string user_uuid = 1;
  optional int32 limit = 2;
}

message ListChargesResponse {
  repeated .chesscom.payments.v1.Charge charges = 1;
}

message FindChargesRequest {
  oneof identifier {
  string adyen_psp_reference = 1;
  string google_play_order_id = 2;
  string apple_transaction_id = 3;
  string apple_order_id = 5;
  string chesscom_order_number = 6;
  }
  optional string user_uuid = 7;
  optional
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06968"></a>
## FND-06968: message declaration: chesscom.payments.v1.FindChargesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FindChargesRequest {

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 770.

```text
limit = 2;
}

message ListChargesResponse {
  repeated .chesscom.payments.v1.Charge charges = 1;
}

message FindChargesRequest {
  oneof identifier {
  string adyen_psp_reference = 1;
  string google_play_order_id = 2;
  string apple_transaction_id = 3;
  string apple_order_id = 5;
  string chesscom_order_number = 6;
  }
  optional string user_uuid = 7;
  optional .chesscom.support.v1.SupportActionContext context = 4
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06969"></a>
## FND-06969: oneof declaration: chesscom.payments.v1.FindChargesRequest.identifier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof identifier {

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 801.

```text
esResponse {
  repeated .chesscom.payments.v1.Charge charges = 1;
}

message FindChargesRequest {
  oneof identifier {
  string adyen_psp_reference = 1;
  string google_play_order_id = 2;
  string apple_transaction_id = 3;
  string apple_order_id = 5;
  string chesscom_order_number = 6;
  }
  optional string user_uuid = 7;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message FindChargesRespons
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06970"></a>
## FND-06970: chesscom.payments.v1.FindChargesRequest.adyen_psp_reference = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string adyen_psp_reference = 1;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 822.

```text
ed .chesscom.payments.v1.Charge charges = 1;
}

message FindChargesRequest {
  oneof identifier {
  string adyen_psp_reference = 1;
  string google_play_order_id = 2;
  string apple_transaction_id = 3;
  string apple_order_id = 5;
  string chesscom_order_number = 6;
  }
  optional string user_uuid = 7;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message FindChargesResponse {
  repeated .chess
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06971"></a>
## FND-06971: chesscom.payments.v1.FindChargesRequest.google_play_order_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string google_play_order_id = 2;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 856.

```text
arges = 1;
}

message FindChargesRequest {
  oneof identifier {
  string adyen_psp_reference = 1;
  string google_play_order_id = 2;
  string apple_transaction_id = 3;
  string apple_order_id = 5;
  string chesscom_order_number = 6;
  }
  optional string user_uuid = 7;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message FindChargesResponse {
  repeated .chesscom.payments.v1.FoundCharge charge
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06972"></a>
## FND-06972: chesscom.payments.v1.FindChargesRequest.apple_transaction_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string apple_transaction_id = 3;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 891.

```text
quest {
  oneof identifier {
  string adyen_psp_reference = 1;
  string google_play_order_id = 2;
  string apple_transaction_id = 3;
  string apple_order_id = 5;
  string chesscom_order_number = 6;
  }
  optional string user_uuid = 7;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message FindChargesResponse {
  repeated .chesscom.payments.v1.FoundCharge charges = 1;
  optional bool privacy_with
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06973"></a>
## FND-06973: chesscom.payments.v1.FindChargesRequest.apple_order_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string apple_order_id = 5;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 926.

```text
ng adyen_psp_reference = 1;
  string google_play_order_id = 2;
  string apple_transaction_id = 3;
  string apple_order_id = 5;
  string chesscom_order_number = 6;
  }
  optional string user_uuid = 7;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message FindChargesResponse {
  repeated .chesscom.payments.v1.FoundCharge charges = 1;
  optional bool privacy_withheld = 2;
  optional .chesscom.supp
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06974"></a>
## FND-06974: chesscom.payments.v1.FindChargesRequest.chesscom_order_number = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string chesscom_order_number = 6;

### Evidence

- **SRC-0507** `research/proto/chesscom/payments/v1/refund_service.proto` — [preserved redacted evidence](../evidence/text/6a6b0f742e4ec44f889fd8884638dcd38020e86fed0878a16c5a86dcbc951e2e.proto)
  Character offset 955.

```text
 string google_play_order_id = 2;
  string apple_transaction_id = 3;
  string apple_order_id = 5;
  string chesscom_order_number = 6;
  }
  optional string user_uuid = 7;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message FindChargesResponse {
  repeated .chesscom.payments.v1.FoundCharge charges = 1;
  optional bool privacy_withheld = 2;
  optional .chesscom.support.v1.SupportActionResult ac
```

**Source references:** SRC-0507, SRC-1478  
**URL references:** None independently associated  
**Related findings:** FND-06952, FND-06953, FND-06954

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
