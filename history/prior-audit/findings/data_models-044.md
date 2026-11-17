# data_models — findings 4301–4400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-04575"></a>
## FND-04575: message declaration: chesscom.flair.v1.ListFlairRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListFlairRequest {

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 102.

```text
 source: chesscom/flair/v1/flair_admin_service.proto
// syntax: proto3

package chesscom.flair.v1;

message ListFlairRequest {
}

message ListFlairResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByIdsRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByNamePrefixRequest {
  optional string name
```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04576, FND-04577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04576"></a>
## FND-04576: message declaration: chesscom.flair.v1.ListFlairResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListFlairResponse {

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 132.

```text
ir_admin_service.proto
// syntax: proto3

package chesscom.flair.v1;

message ListFlairRequest {
}

message ListFlairResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByIdsRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByNamePrefixRequest {
  optional string name_prefix = 1;
}

message ListFl
```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04575, FND-04577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04577"></a>
## FND-04577: chesscom.flair.v1.ListFlairResponse.flair = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.flair.v1.Flair flair = 1;

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 162.

```text
ax: proto3

package chesscom.flair.v1;

message ListFlairRequest {
}

message ListFlairResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByIdsRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByNamePrefixRequest {
  optional string name_prefix = 1;
}

message ListFlairByNamePrefixResponse {
  re
```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04575, FND-04576

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04578"></a>
## FND-04578: message declaration: chesscom.flair.v1.ListFlairByIdsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListFlairByIdsRequest {

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 210.

```text
ListFlairRequest {
}

message ListFlairResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByIdsRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByNamePrefixRequest {
  optional string name_prefix = 1;
}

message ListFlairByNamePrefixResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

me
```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04575, FND-04576, FND-04577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04579"></a>
## FND-04579: chesscom.flair.v1.ListFlairByIdsRequest.flair_ids = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string flair_ids = 1;

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 244.

```text
FlairResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByIdsRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByNamePrefixRequest {
  optional string name_prefix = 1;
}

message ListFlairByNamePrefixResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairRequest {
  opti
```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04575, FND-04576, FND-04577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04580"></a>
## FND-04580: message declaration: chesscom.flair.v1.ListFlairByIdsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListFlairByIdsResponse {

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 278.

```text
om.flair.v1.Flair flair = 1;
}

message ListFlairByIdsRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByNamePrefixRequest {
  optional string name_prefix = 1;
}

message ListFlairByNamePrefixResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairRequest {
  optional string user_id = 1;
  optiona
```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04575, FND-04576, FND-04577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04581"></a>
## FND-04581: chesscom.flair.v1.ListFlairByIdsResponse.flair = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.flair.v1.Flair flair = 1;

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 162.

```text
ax: proto3

package chesscom.flair.v1;

message ListFlairRequest {
}

message ListFlairResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByIdsRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByNamePrefixRequest {
  optional string name_prefix = 1;
}

message ListFlairByNamePrefixResponse {
  re
```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04575, FND-04576, FND-04577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04582"></a>
## FND-04582: message declaration: chesscom.flair.v1.ListFlairByNamePrefixRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListFlairByNamePrefixRequest {

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 361.

```text
lair_ids = 1;
}

message ListFlairByIdsResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByNamePrefixRequest {
  optional string name_prefix = 1;
}

message ListFlairByNamePrefixResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

message SetUserFlairResponse {
}

```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04575, FND-04576, FND-04577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04583"></a>
## FND-04583: chesscom.flair.v1.ListFlairByNamePrefixRequest.name_prefix = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name_prefix = 1;

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 402.

```text
sponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByNamePrefixRequest {
  optional string name_prefix = 1;
}

message ListFlairByNamePrefixResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

message SetUserFlairResponse {
}

```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04575, FND-04576, FND-04577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04584"></a>
## FND-04584: message declaration: chesscom.flair.v1.ListFlairByNamePrefixResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListFlairByNamePrefixResponse {

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 438.

```text
v1.Flair flair = 1;
}

message ListFlairByNamePrefixRequest {
  optional string name_prefix = 1;
}

message ListFlairByNamePrefixResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

message SetUserFlairResponse {
}

```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04575, FND-04576, FND-04577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04585"></a>
## FND-04585: chesscom.flair.v1.ListFlairByNamePrefixResponse.flair = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.flair.v1.Flair flair = 1;

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 162.

```text
ax: proto3

package chesscom.flair.v1;

message ListFlairRequest {
}

message ListFlairResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByIdsRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByNamePrefixRequest {
  optional string name_prefix = 1;
}

message ListFlairByNamePrefixResponse {
  re
```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04575, FND-04576, FND-04577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04586"></a>
## FND-04586: message declaration: chesscom.flair.v1.SetUserFlairRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetUserFlairRequest {

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 528.

```text
x = 1;
}

message ListFlairByNamePrefixResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

message SetUserFlairResponse {
}

```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04575, FND-04576, FND-04577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04587"></a>
## FND-04587: chesscom.flair.v1.SetUserFlairRequest.user_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_id = 1;

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 560.

```text
ePrefixResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

message SetUserFlairResponse {
}

```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04575, FND-04576, FND-04577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04588"></a>
## FND-04588: chesscom.flair.v1.SetUserFlairRequest.flair_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string flair_id = 2;

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 591.

```text
hesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

message SetUserFlairResponse {
}

```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04575, FND-04576, FND-04577

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04589"></a>
## FND-04589: message declaration: chesscom.flair.v1.SetUserFlairResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetUserFlairResponse {

### Evidence

- **SRC-0435** `research/proto/chesscom/flair/v1/flair_admin_service.proto` — [preserved redacted evidence](../evidence/text/d15856403c9d9542c64c3c4b8f5f99bdf6bd62e0dd25a1f884fabbd25d36b2d0.proto)
  Character offset 624.

```text

}

message SetUserFlairRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

message SetUserFlairResponse {
}

```

**Source references:** SRC-0435, SRC-1406  
**URL references:** None independently associated  
**Related findings:** FND-04575, FND-04576, FND-04577

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04590"></a>
## FND-04590: message declaration: chesscom.flair.v1.ListFlairInternalRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListFlairInternalRequest {

### Evidence

- **SRC-0436** `research/proto/chesscom/flair/v1/flair_internal_service.proto` — [preserved redacted evidence](../evidence/text/c6bdaa404aa0ab9d8dc4342ed18571573e393f092e19bcc12c9490d9ee25ac01.proto)
  Character offset 105.

```text
urce: chesscom/flair/v1/flair_internal_service.proto
// syntax: proto3

package chesscom.flair.v1;

message ListFlairInternalRequest {
}

message ListFlairInternalResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByIdsInternalRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsInternalResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairInternalR
```

**Source references:** SRC-0436, SRC-1407  
**URL references:** None independently associated  
**Related findings:** FND-04591, FND-04592

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04591"></a>
## FND-04591: message declaration: chesscom.flair.v1.ListFlairInternalResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListFlairInternalResponse {

### Evidence

- **SRC-0436** `research/proto/chesscom/flair/v1/flair_internal_service.proto` — [preserved redacted evidence](../evidence/text/c6bdaa404aa0ab9d8dc4342ed18571573e393f092e19bcc12c9490d9ee25ac01.proto)
  Character offset 143.

```text
_service.proto
// syntax: proto3

package chesscom.flair.v1;

message ListFlairInternalRequest {
}

message ListFlairInternalResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByIdsInternalRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsInternalResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairInternalRequest {
  optional string user_id = 1
```

**Source references:** SRC-0436, SRC-1407  
**URL references:** None independently associated  
**Related findings:** FND-04590, FND-04592

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04592"></a>
## FND-04592: chesscom.flair.v1.ListFlairInternalResponse.flair = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.flair.v1.Flair flair = 1;

### Evidence

- **SRC-0436** `research/proto/chesscom/flair/v1/flair_internal_service.proto` — [preserved redacted evidence](../evidence/text/c6bdaa404aa0ab9d8dc4342ed18571573e393f092e19bcc12c9490d9ee25ac01.proto)
  Character offset 181.

```text
age chesscom.flair.v1;

message ListFlairInternalRequest {
}

message ListFlairInternalResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByIdsInternalRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsInternalResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairInternalRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

m
```

**Source references:** SRC-0436, SRC-1407  
**URL references:** None independently associated  
**Related findings:** FND-04590, FND-04591

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04593"></a>
## FND-04593: message declaration: chesscom.flair.v1.ListFlairByIdsInternalRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListFlairByIdsInternalRequest {

### Evidence

- **SRC-0436** `research/proto/chesscom/flair/v1/flair_internal_service.proto` — [preserved redacted evidence](../evidence/text/c6bdaa404aa0ab9d8dc4342ed18571573e393f092e19bcc12c9490d9ee25ac01.proto)
  Character offset 229.

```text
lRequest {
}

message ListFlairInternalResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByIdsInternalRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsInternalResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairInternalRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

message SetUserFlairInternalResponse {
}

```

**Source references:** SRC-0436, SRC-1407  
**URL references:** None independently associated  
**Related findings:** FND-04590, FND-04591, FND-04592

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04594"></a>
## FND-04594: chesscom.flair.v1.ListFlairByIdsInternalRequest.flair_ids = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string flair_ids = 1;

### Evidence

- **SRC-0436** `research/proto/chesscom/flair/v1/flair_internal_service.proto` — [preserved redacted evidence](../evidence/text/c6bdaa404aa0ab9d8dc4342ed18571573e393f092e19bcc12c9490d9ee25ac01.proto)
  Character offset 271.

```text
ponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByIdsInternalRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsInternalResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairInternalRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

message SetUserFlairInternalResponse {
}

```

**Source references:** SRC-0436, SRC-1407  
**URL references:** None independently associated  
**Related findings:** FND-04590, FND-04591, FND-04592

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04595"></a>
## FND-04595: message declaration: chesscom.flair.v1.ListFlairByIdsInternalResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListFlairByIdsInternalResponse {

### Evidence

- **SRC-0436** `research/proto/chesscom/flair/v1/flair_internal_service.proto` — [preserved redacted evidence](../evidence/text/c6bdaa404aa0ab9d8dc4342ed18571573e393f092e19bcc12c9490d9ee25ac01.proto)
  Character offset 305.

```text
.v1.Flair flair = 1;
}

message ListFlairByIdsInternalRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsInternalResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairInternalRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

message SetUserFlairInternalResponse {
}

```

**Source references:** SRC-0436, SRC-1407  
**URL references:** None independently associated  
**Related findings:** FND-04590, FND-04591, FND-04592

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04596"></a>
## FND-04596: chesscom.flair.v1.ListFlairByIdsInternalResponse.flair = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.flair.v1.Flair flair = 1;

### Evidence

- **SRC-0436** `research/proto/chesscom/flair/v1/flair_internal_service.proto` — [preserved redacted evidence](../evidence/text/c6bdaa404aa0ab9d8dc4342ed18571573e393f092e19bcc12c9490d9ee25ac01.proto)
  Character offset 181.

```text
age chesscom.flair.v1;

message ListFlairInternalRequest {
}

message ListFlairInternalResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message ListFlairByIdsInternalRequest {
  repeated string flair_ids = 1;
}

message ListFlairByIdsInternalResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairInternalRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

m
```

**Source references:** SRC-0436, SRC-1407  
**URL references:** None independently associated  
**Related findings:** FND-04590, FND-04591, FND-04592

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04597"></a>
## FND-04597: message declaration: chesscom.flair.v1.SetUserFlairInternalRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetUserFlairInternalRequest {

### Evidence

- **SRC-0436** `research/proto/chesscom/flair/v1/flair_internal_service.proto` — [preserved redacted evidence](../evidence/text/c6bdaa404aa0ab9d8dc4342ed18571573e393f092e19bcc12c9490d9ee25ac01.proto)
  Character offset 396.

```text
 = 1;
}

message ListFlairByIdsInternalResponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairInternalRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

message SetUserFlairInternalResponse {
}

```

**Source references:** SRC-0436, SRC-1407  
**URL references:** None independently associated  
**Related findings:** FND-04590, FND-04591, FND-04592

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04598"></a>
## FND-04598: chesscom.flair.v1.SetUserFlairInternalRequest.user_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_id = 1;

### Evidence

- **SRC-0436** `research/proto/chesscom/flair/v1/flair_internal_service.proto` — [preserved redacted evidence](../evidence/text/c6bdaa404aa0ab9d8dc4342ed18571573e393f092e19bcc12c9490d9ee25ac01.proto)
  Character offset 436.

```text
esponse {
  repeated .chesscom.flair.v1.Flair flair = 1;
}

message SetUserFlairInternalRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

message SetUserFlairInternalResponse {
}

```

**Source references:** SRC-0436, SRC-1407  
**URL references:** None independently associated  
**Related findings:** FND-04590, FND-04591, FND-04592

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04599"></a>
## FND-04599: chesscom.flair.v1.SetUserFlairInternalRequest.flair_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string flair_id = 2;

### Evidence

- **SRC-0436** `research/proto/chesscom/flair/v1/flair_internal_service.proto` — [preserved redacted evidence](../evidence/text/c6bdaa404aa0ab9d8dc4342ed18571573e393f092e19bcc12c9490d9ee25ac01.proto)
  Character offset 467.

```text
flair.v1.Flair flair = 1;
}

message SetUserFlairInternalRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

message SetUserFlairInternalResponse {
}

```

**Source references:** SRC-0436, SRC-1407  
**URL references:** None independently associated  
**Related findings:** FND-04590, FND-04591, FND-04592

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04600"></a>
## FND-04600: message declaration: chesscom.flair.v1.SetUserFlairInternalResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetUserFlairInternalResponse {

### Evidence

- **SRC-0436** `research/proto/chesscom/flair/v1/flair_internal_service.proto` — [preserved redacted evidence](../evidence/text/c6bdaa404aa0ab9d8dc4342ed18571573e393f092e19bcc12c9490d9ee25ac01.proto)
  Character offset 500.

```text
age SetUserFlairInternalRequest {
  optional string user_id = 1;
  optional string flair_id = 2;
}

message SetUserFlairInternalResponse {
}

```

**Source references:** SRC-0436, SRC-1407  
**URL references:** None independently associated  
**Related findings:** FND-04590, FND-04591, FND-04592

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04601"></a>
## FND-04601: message declaration: chesscom.flair.v1.ListFlairSelectionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListFlairSelectionRequest {

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 96.

```text
// source: chesscom/flair/v1/flair_service.proto
// syntax: proto3

package chesscom.flair.v1;

message ListFlairSelectionRequest {
}

message ListFlairSelectionResponse {
  repeated .chesscom.flair.v1.FlairSelectionItem flair_selection = 1;
}

message SelectFlairRequest {
  optional string flair_id = 1;
}

message SelectFlairResponse {
}

message RemoveFlairRequest {
}

message RemoveFlairResponse {
}

message G
```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04602, FND-04603

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04602"></a>
## FND-04602: message declaration: chesscom.flair.v1.ListFlairSelectionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListFlairSelectionResponse {

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 135.

```text
service.proto
// syntax: proto3

package chesscom.flair.v1;

message ListFlairSelectionRequest {
}

message ListFlairSelectionResponse {
  repeated .chesscom.flair.v1.FlairSelectionItem flair_selection = 1;
}

message SelectFlairRequest {
  optional string flair_id = 1;
}

message SelectFlairResponse {
}

message RemoveFlairRequest {
}

message RemoveFlairResponse {
}

message GetUserFlairRequest {
  oneof _user_id {
```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04603

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04603"></a>
## FND-04603: chesscom.flair.v1.ListFlairSelectionResponse.flair_selection = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.flair.v1.FlairSelectionItem flair_selection = 1;

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 174.

```text
e chesscom.flair.v1;

message ListFlairSelectionRequest {
}

message ListFlairSelectionResponse {
  repeated .chesscom.flair.v1.FlairSelectionItem flair_selection = 1;
}

message SelectFlairRequest {
  optional string flair_id = 1;
}

message SelectFlairResponse {
}

message RemoveFlairRequest {
}

message RemoveFlairResponse {
}

message GetUserFlairRequest {
  oneof _user_id {
  string user_id = 16;
  }
}

message 
```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04604"></a>
## FND-04604: message declaration: chesscom.flair.v1.SelectFlairRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SelectFlairRequest {

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 245.

```text
stFlairSelectionResponse {
  repeated .chesscom.flair.v1.FlairSelectionItem flair_selection = 1;
}

message SelectFlairRequest {
  optional string flair_id = 1;
}

message SelectFlairResponse {
}

message RemoveFlairRequest {
}

message RemoveFlairResponse {
}

message GetUserFlairRequest {
  oneof _user_id {
  string user_id = 16;
  }
}

message GetUserFlairResponse {
  optional .chesscom.flair.v1.UserFlair user_fla
```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602, FND-04603

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04605"></a>
## FND-04605: chesscom.flair.v1.SelectFlairRequest.flair_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string flair_id = 1;

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 276.

```text
peated .chesscom.flair.v1.FlairSelectionItem flair_selection = 1;
}

message SelectFlairRequest {
  optional string flair_id = 1;
}

message SelectFlairResponse {
}

message RemoveFlairRequest {
}

message RemoveFlairResponse {
}

message GetUserFlairRequest {
  oneof _user_id {
  string user_id = 16;
  }
}

message GetUserFlairResponse {
  optional .chesscom.flair.v1.UserFlair user_flair = 1;
}

message ListUserFlai
```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602, FND-04603

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04606"></a>
## FND-04606: message declaration: chesscom.flair.v1.SelectFlairResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SelectFlairResponse {

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 309.

```text
lectionItem flair_selection = 1;
}

message SelectFlairRequest {
  optional string flair_id = 1;
}

message SelectFlairResponse {
}

message RemoveFlairRequest {
}

message RemoveFlairResponse {
}

message GetUserFlairRequest {
  oneof _user_id {
  string user_id = 16;
  }
}

message GetUserFlairResponse {
  optional .chesscom.flair.v1.UserFlair user_flair = 1;
}

message ListUserFlairRequest {
  repeated string user
```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602, FND-04603

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04607"></a>
## FND-04607: message declaration: chesscom.flair.v1.RemoveFlairRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RemoveFlairRequest {

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 342.

```text
}

message SelectFlairRequest {
  optional string flair_id = 1;
}

message SelectFlairResponse {
}

message RemoveFlairRequest {
}

message RemoveFlairResponse {
}

message GetUserFlairRequest {
  oneof _user_id {
  string user_id = 16;
  }
}

message GetUserFlairResponse {
  optional .chesscom.flair.v1.UserFlair user_flair = 1;
}

message ListUserFlairRequest {
  repeated string user_ids = 1;
}

message ListUserFlai
```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602, FND-04603

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04608"></a>
## FND-04608: message declaration: chesscom.flair.v1.RemoveFlairResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RemoveFlairResponse {

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 374.

```text
  optional string flair_id = 1;
}

message SelectFlairResponse {
}

message RemoveFlairRequest {
}

message RemoveFlairResponse {
}

message GetUserFlairRequest {
  oneof _user_id {
  string user_id = 16;
  }
}

message GetUserFlairResponse {
  optional .chesscom.flair.v1.UserFlair user_flair = 1;
}

message ListUserFlairRequest {
  repeated string user_ids = 1;
}

message ListUserFlairResponse {
  repeated .chesscom
```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602, FND-04603

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04609"></a>
## FND-04609: message declaration: chesscom.flair.v1.GetUserFlairRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserFlairRequest {

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 407.

```text


message SelectFlairResponse {
}

message RemoveFlairRequest {
}

message RemoveFlairResponse {
}

message GetUserFlairRequest {
  oneof _user_id {
  string user_id = 16;
  }
}

message GetUserFlairResponse {
  optional .chesscom.flair.v1.UserFlair user_flair = 1;
}

message ListUserFlairRequest {
  repeated string user_ids = 1;
}

message ListUserFlairResponse {
  repeated .chesscom.flair.v1.UserFlair user_flair = 
```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602, FND-04603

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04610"></a>
## FND-04610: oneof declaration: chesscom.flair.v1.GetUserFlairRequest._user_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_id {

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 439.

```text
}

message RemoveFlairRequest {
}

message RemoveFlairResponse {
}

message GetUserFlairRequest {
  oneof _user_id {
  string user_id = 16;
  }
}

message GetUserFlairResponse {
  optional .chesscom.flair.v1.UserFlair user_flair = 1;
}

message ListUserFlairRequest {
  repeated string user_ids = 1;
}

message ListUserFlairResponse {
  repeated .chesscom.flair.v1.UserFlair user_flair = 1;
}

```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602, FND-04603

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04611"></a>
## FND-04611: chesscom.flair.v1.GetUserFlairRequest.user_id = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_id = 16;

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 458.

```text
airRequest {
}

message RemoveFlairResponse {
}

message GetUserFlairRequest {
  oneof _user_id {
  string user_id = 16;
  }
}

message GetUserFlairResponse {
  optional .chesscom.flair.v1.UserFlair user_flair = 1;
}

message ListUserFlairRequest {
  repeated string user_ids = 1;
}

message ListUserFlairResponse {
  repeated .chesscom.flair.v1.UserFlair user_flair = 1;
}

```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602, FND-04603

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04612"></a>
## FND-04612: message declaration: chesscom.flair.v1.GetUserFlairResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserFlairResponse {

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 486.

```text
veFlairResponse {
}

message GetUserFlairRequest {
  oneof _user_id {
  string user_id = 16;
  }
}

message GetUserFlairResponse {
  optional .chesscom.flair.v1.UserFlair user_flair = 1;
}

message ListUserFlairRequest {
  repeated string user_ids = 1;
}

message ListUserFlairResponse {
  repeated .chesscom.flair.v1.UserFlair user_flair = 1;
}

```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602, FND-04603

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04613"></a>
## FND-04613: chesscom.flair.v1.GetUserFlairResponse.user_flair = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.flair.v1.UserFlair user_flair = 1;

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 519.

```text
serFlairRequest {
  oneof _user_id {
  string user_id = 16;
  }
}

message GetUserFlairResponse {
  optional .chesscom.flair.v1.UserFlair user_flair = 1;
}

message ListUserFlairRequest {
  repeated string user_ids = 1;
}

message ListUserFlairResponse {
  repeated .chesscom.flair.v1.UserFlair user_flair = 1;
}

```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602, FND-04603

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04614"></a>
## FND-04614: message declaration: chesscom.flair.v1.ListUserFlairRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListUserFlairRequest {

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 576.

```text
6;
  }
}

message GetUserFlairResponse {
  optional .chesscom.flair.v1.UserFlair user_flair = 1;
}

message ListUserFlairRequest {
  repeated string user_ids = 1;
}

message ListUserFlairResponse {
  repeated .chesscom.flair.v1.UserFlair user_flair = 1;
}

```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602, FND-04603

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04615"></a>
## FND-04615: chesscom.flair.v1.ListUserFlairRequest.user_ids = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string user_ids = 1;

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 609.

```text
ponse {
  optional .chesscom.flair.v1.UserFlair user_flair = 1;
}

message ListUserFlairRequest {
  repeated string user_ids = 1;
}

message ListUserFlairResponse {
  repeated .chesscom.flair.v1.UserFlair user_flair = 1;
}

```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602, FND-04603

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04616"></a>
## FND-04616: message declaration: chesscom.flair.v1.ListUserFlairResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListUserFlairResponse {

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 642.

```text
r.v1.UserFlair user_flair = 1;
}

message ListUserFlairRequest {
  repeated string user_ids = 1;
}

message ListUserFlairResponse {
  repeated .chesscom.flair.v1.UserFlair user_flair = 1;
}

```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602, FND-04603

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04617"></a>
## FND-04617: chesscom.flair.v1.ListUserFlairResponse.user_flair = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.flair.v1.UserFlair user_flair = 1;

### Evidence

- **SRC-0437** `research/proto/chesscom/flair/v1/flair_service.proto` — [preserved redacted evidence](../evidence/text/e7a1f0483dee9062c4e8975d38896b0f1e55a62b6607043594fe158e81d42abb.proto)
  Character offset 676.

```text
message ListUserFlairRequest {
  repeated string user_ids = 1;
}

message ListUserFlairResponse {
  repeated .chesscom.flair.v1.UserFlair user_flair = 1;
}

```

**Source references:** SRC-0437, SRC-1408  
**URL references:** None independently associated  
**Related findings:** FND-04601, FND-04602, FND-04603

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04618"></a>
## FND-04618: message declaration: chesscom.flair.v1.FlairView

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FlairView {

### Evidence

- **SRC-0438** `research/proto/chesscom/flair/v1/flair_view.proto` — [preserved redacted evidence](../evidence/text/0a7d4294bf8190a11a1e9f0544249b33bdae2bee99e51cefbd15e695399b1cf8.proto)
  Character offset 93.

```text
// source: chesscom/flair/v1/flair_view.proto
// syntax: proto3

package chesscom.flair.v1;

message FlairView {
  optional string id = 1;
  repeated .chesscom.flair.v1.FlairView.ImagesEntry images = 2;
  optional string description = 3;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message UserFlair {
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 2;
  }
  opt
```

**Source references:** SRC-0438, SRC-1409  
**URL references:** None independently associated  
**Related findings:** FND-04619, FND-04620

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04619"></a>
## FND-04619: chesscom.flair.v1.FlairView.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0438** `research/proto/chesscom/flair/v1/flair_view.proto` — [preserved redacted evidence](../evidence/text/0a7d4294bf8190a11a1e9f0544249b33bdae2bee99e51cefbd15e695399b1cf8.proto)
  Character offset 115.

```text
scom/flair/v1/flair_view.proto
// syntax: proto3

package chesscom.flair.v1;

message FlairView {
  optional string id = 1;
  repeated .chesscom.flair.v1.FlairView.ImagesEntry images = 2;
  optional string description = 3;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message UserFlair {
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 2;
  }
  optional string user_id =
```

**Source references:** SRC-0438, SRC-1409  
**URL references:** None independently associated  
**Related findings:** FND-04618, FND-04620

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04620"></a>
## FND-04620: chesscom.flair.v1.FlairView.images = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.flair.v1.FlairView.ImagesEntry images = 2;

### Evidence

- **SRC-0438** `research/proto/chesscom/flair/v1/flair_view.proto` — [preserved redacted evidence](../evidence/text/0a7d4294bf8190a11a1e9f0544249b33bdae2bee99e51cefbd15e695399b1cf8.proto)
  Character offset 141.

```text
roto
// syntax: proto3

package chesscom.flair.v1;

message FlairView {
  optional string id = 1;
  repeated .chesscom.flair.v1.FlairView.ImagesEntry images = 2;
  optional string description = 3;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message UserFlair {
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 2;
  }
  optional string user_id = 1;
}

```

**Source references:** SRC-0438, SRC-1409  
**URL references:** None independently associated  
**Related findings:** FND-04618, FND-04619

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04621"></a>
## FND-04621: chesscom.flair.v1.FlairView.description = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string description = 3;

### Evidence

- **SRC-0438** `research/proto/chesscom/flair/v1/flair_view.proto` — [preserved redacted evidence](../evidence/text/0a7d4294bf8190a11a1e9f0544249b33bdae2bee99e51cefbd15e695399b1cf8.proto)
  Character offset 205.

```text
rView {
  optional string id = 1;
  repeated .chesscom.flair.v1.FlairView.ImagesEntry images = 2;
  optional string description = 3;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message UserFlair {
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 2;
  }
  optional string user_id = 1;
}

```

**Source references:** SRC-0438, SRC-1409  
**URL references:** None independently associated  
**Related findings:** FND-04618, FND-04619, FND-04620

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04622"></a>
## FND-04622: message declaration: chesscom.flair.v1.FlairView.ImagesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ImagesEntry {

### Evidence

- **SRC-0438** `research/proto/chesscom/flair/v1/flair_view.proto` — [preserved redacted evidence](../evidence/text/0a7d4294bf8190a11a1e9f0544249b33bdae2bee99e51cefbd15e695399b1cf8.proto)
  Character offset 240.

```text
 repeated .chesscom.flair.v1.FlairView.ImagesEntry images = 2;
  optional string description = 3;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message UserFlair {
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 2;
  }
  optional string user_id = 1;
}

```

**Source references:** SRC-0438, SRC-1409  
**URL references:** None independently associated  
**Related findings:** FND-04618, FND-04619, FND-04620

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04623"></a>
## FND-04623: chesscom.flair.v1.FlairView.ImagesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0438** `research/proto/chesscom/flair/v1/flair_view.proto` — [preserved redacted evidence](../evidence/text/0a7d4294bf8190a11a1e9f0544249b33bdae2bee99e51cefbd15e695399b1cf8.proto)
  Character offset 264.

```text
r.v1.FlairView.ImagesEntry images = 2;
  optional string description = 3;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message UserFlair {
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 2;
  }
  optional string user_id = 1;
}

```

**Source references:** SRC-0438, SRC-1409  
**URL references:** None independently associated  
**Related findings:** FND-04618, FND-04619, FND-04620

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04624"></a>
## FND-04624: chesscom.flair.v1.FlairView.ImagesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0438** `research/proto/chesscom/flair/v1/flair_view.proto` — [preserved redacted evidence](../evidence/text/0a7d4294bf8190a11a1e9f0544249b33bdae2bee99e51cefbd15e695399b1cf8.proto)
  Character offset 291.

```text
images = 2;
  optional string description = 3;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message UserFlair {
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 2;
  }
  optional string user_id = 1;
}

```

**Source references:** SRC-0438, SRC-1409  
**URL references:** None independently associated  
**Related findings:** FND-04618, FND-04619, FND-04620

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04625"></a>
## FND-04625: message declaration: chesscom.flair.v1.UserFlair

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserFlair {

### Evidence

- **SRC-0438** `research/proto/chesscom/flair/v1/flair_view.proto` — [preserved redacted evidence](../evidence/text/0a7d4294bf8190a11a1e9f0544249b33bdae2bee99e51cefbd15e695399b1cf8.proto)
  Character offset 325.

```text
ription = 3;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message UserFlair {
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 2;
  }
  optional string user_id = 1;
}

```

**Source references:** SRC-0438, SRC-1409  
**URL references:** None independently associated  
**Related findings:** FND-04618, FND-04619, FND-04620

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04626"></a>
## FND-04626: oneof declaration: chesscom.flair.v1.UserFlair._flair

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _flair {

### Evidence

- **SRC-0438** `research/proto/chesscom/flair/v1/flair_view.proto` — [preserved redacted evidence](../evidence/text/0a7d4294bf8190a11a1e9f0544249b33bdae2bee99e51cefbd15e695399b1cf8.proto)
  Character offset 347.

```text
 ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message UserFlair {
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 2;
  }
  optional string user_id = 1;
}

```

**Source references:** SRC-0438, SRC-1409  
**URL references:** None independently associated  
**Related findings:** FND-04618, FND-04619, FND-04620

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04627"></a>
## FND-04627: chesscom.flair.v1.UserFlair.flair = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.flair.v1.FlairView flair = 2;

### Evidence

- **SRC-0438** `research/proto/chesscom/flair/v1/flair_view.proto` — [preserved redacted evidence](../evidence/text/0a7d4294bf8190a11a1e9f0544249b33bdae2bee99e51cefbd15e695399b1cf8.proto)
  Character offset 364.

```text
optional string key = 1;
  optional string value = 2;
  }
}

message UserFlair {
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 2;
  }
  optional string user_id = 1;
}

```

**Source references:** SRC-0438, SRC-1409  
**URL references:** None independently associated  
**Related findings:** FND-04618, FND-04619, FND-04620

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04628"></a>
## FND-04628: chesscom.flair.v1.UserFlair.user_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_id = 1;

### Evidence

- **SRC-0438** `research/proto/chesscom/flair/v1/flair_view.proto` — [preserved redacted evidence](../evidence/text/0a7d4294bf8190a11a1e9f0544249b33bdae2bee99e51cefbd15e695399b1cf8.proto)
  Character offset 410.

```text
ue = 2;
  }
}

message UserFlair {
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 2;
  }
  optional string user_id = 1;
}

```

**Source references:** SRC-0438, SRC-1409  
**URL references:** None independently associated  
**Related findings:** FND-04618, FND-04619, FND-04620

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04629"></a>
## FND-04629: message declaration: chesscom.friends_search.v1.ListRecentFriendsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListRecentFriendsRequest {

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 127.

```text
_search/v1/friends_navigation_service.proto
// syntax: proto3

package chesscom.friends_search.v1;

message ListRecentFriendsRequest {
}

message ListRecentFriendsResponse {
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;
}

message ListRecentPendingFriendsRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  oneof _direction {
  .chesscom.friends_sea
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04630, FND-04631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04630"></a>
## FND-04630: message declaration: chesscom.friends_search.v1.ListRecentFriendsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListRecentFriendsResponse {

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 165.

```text
proto
// syntax: proto3

package chesscom.friends_search.v1;

message ListRecentFriendsRequest {
}

message ListRecentFriendsResponse {
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;
}

message ListRecentPendingFriendsRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  oneof _direction {
  .chesscom.friends_search.v1.FriendRequestDirection directio
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04631"></a>
## FND-04631: chesscom.friends_search.v1.ListRecentFriendsResponse.friends = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 203.

```text
com.friends_search.v1;

message ListRecentFriendsRequest {
}

message ListRecentFriendsResponse {
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;
}

message ListRecentPendingFriendsRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  oneof _direction {
  .chesscom.friends_search.v1.FriendRequestDirection direction = 2;
  }
}

message ListRecentPendin
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04632"></a>
## FND-04632: message declaration: chesscom.friends_search.v1.ListRecentPendingFriendsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListRecentPendingFriendsRequest {

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 282.

```text
tFriendsResponse {
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;
}

message ListRecentPendingFriendsRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  oneof _direction {
  .chesscom.friends_search.v1.FriendRequestDirection direction = 2;
  }
}

message ListRecentPendingFriendsResponse {
  repeated .chesscom.friends_search.v1.PendingFriendsSearchF
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04633"></a>
## FND-04633: oneof declaration: chesscom.friends_search.v1.ListRecentPendingFriendsRequest._pagination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pagination {

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 326.

```text
nds_search.v1.SocialFriendsSearchFriend friends = 1;
}

message ListRecentPendingFriendsRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  oneof _direction {
  .chesscom.friends_search.v1.FriendRequestDirection direction = 2;
  }
}

message ListRecentPendingFriendsResponse {
  repeated .chesscom.friends_search.v1.PendingFriendsSearchFriend pending_friends = 1;
  optional .chess
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04634"></a>
## FND-04634: chesscom.friends_search.v1.ListRecentPendingFriendsRequest.pagination = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.RequestPagination pagination = 1;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 348.

```text
iendsSearchFriend friends = 1;
}

message ListRecentPendingFriendsRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  oneof _direction {
  .chesscom.friends_search.v1.FriendRequestDirection direction = 2;
  }
}

message ListRecentPendingFriendsResponse {
  repeated .chesscom.friends_search.v1.PendingFriendsSearchFriend pending_friends = 1;
  optional .chesscom.api.v1.ResponsePag
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04635"></a>
## FND-04635: oneof declaration: chesscom.friends_search.v1.ListRecentPendingFriendsRequest._direction

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _direction {

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 405.

```text
ngFriendsRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  oneof _direction {
  .chesscom.friends_search.v1.FriendRequestDirection direction = 2;
  }
}

message ListRecentPendingFriendsResponse {
  repeated .chesscom.friends_search.v1.PendingFriendsSearchFriend pending_friends = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message SocialAutocompleteRequ
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04636"></a>
## FND-04636: chesscom.friends_search.v1.ListRecentPendingFriendsRequest.direction = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.friends_search.v1.FriendRequestDirection direction = 2;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 426.

```text
oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  oneof _direction {
  .chesscom.friends_search.v1.FriendRequestDirection direction = 2;
  }
}

message ListRecentPendingFriendsResponse {
  repeated .chesscom.friends_search.v1.PendingFriendsSearchFriend pending_friends = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message SocialAutocompleteRequest {
  oneof _includ
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04637"></a>
## FND-04637: message declaration: chesscom.friends_search.v1.ListRecentPendingFriendsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListRecentPendingFriendsResponse {

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 499.

```text
  }
  oneof _direction {
  .chesscom.friends_search.v1.FriendRequestDirection direction = 2;
  }
}

message ListRecentPendingFriendsResponse {
  repeated .chesscom.friends_search.v1.PendingFriendsSearchFriend pending_friends = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message SocialAutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 3;
  }
  oneof _include_suggestions 
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04638"></a>
## FND-04638: chesscom.friends_search.v1.ListRecentPendingFriendsResponse.pending_friends = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.friends_search.v1.PendingFriendsSearchFriend pending_friends = 1;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 544.

```text
search.v1.FriendRequestDirection direction = 2;
  }
}

message ListRecentPendingFriendsResponse {
  repeated .chesscom.friends_search.v1.PendingFriendsSearchFriend pending_friends = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message SocialAutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 3;
  }
  oneof _include_suggestions {
  bool include_suggestions = 4;
  }
  oneof
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04639"></a>
## FND-04639: chesscom.friends_search.v1.ListRecentPendingFriendsResponse.pagination = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.ResponsePagination pagination = 2;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 631.

```text
Response {
  repeated .chesscom.friends_search.v1.PendingFriendsSearchFriend pending_friends = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message SocialAutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 3;
  }
  oneof _include_suggestions {
  bool include_suggestions = 4;
  }
  oneof _friends_limit {
  int32 friends_limit = 5;
  }
  oneof _suggestions_limit {
  int32 s
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04640"></a>
## FND-04640: message declaration: chesscom.friends_search.v1.SocialAutocompleteRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SocialAutocompleteRequest {

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 695.

```text
SearchFriend pending_friends = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message SocialAutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 3;
  }
  oneof _include_suggestions {
  bool include_suggestions = 4;
  }
  oneof _friends_limit {
  int32 friends_limit = 5;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 6;
  }
  oneof _exact_username_first {
  bool
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04641"></a>
## FND-04641: oneof declaration: chesscom.friends_search.v1.SocialAutocompleteRequest._include_friends

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _include_friends {

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 733.

```text
tional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message SocialAutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 3;
  }
  oneof _include_suggestions {
  bool include_suggestions = 4;
  }
  oneof _friends_limit {
  int32 friends_limit = 5;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 6;
  }
  oneof _exact_username_first {
  bool exact_username_first = 7;
  }
  oneof
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04642"></a>
## FND-04642: chesscom.friends_search.v1.SocialAutocompleteRequest.include_friends = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool include_friends = 3;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 760.

```text
ponsePagination pagination = 2;
}

message SocialAutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 3;
  }
  oneof _include_suggestions {
  bool include_suggestions = 4;
  }
  oneof _friends_limit {
  int32 friends_limit = 5;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 6;
  }
  oneof _exact_username_first {
  bool exact_username_first = 7;
  }
  oneof _boost_username {
  bool b
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04643"></a>
## FND-04643: oneof declaration: chesscom.friends_search.v1.SocialAutocompleteRequest._include_suggestions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _include_suggestions {

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 792.

```text
}

message SocialAutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 3;
  }
  oneof _include_suggestions {
  bool include_suggestions = 4;
  }
  oneof _friends_limit {
  int32 friends_limit = 5;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 6;
  }
  oneof _exact_username_first {
  bool exact_username_first = 7;
  }
  oneof _boost_username {
  bool boost_username = 8;
  }
  optiona
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04644"></a>
## FND-04644: chesscom.friends_search.v1.SocialAutocompleteRequest.include_suggestions = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool include_suggestions = 4;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 823.

```text
quest {
  oneof _include_friends {
  bool include_friends = 3;
  }
  oneof _include_suggestions {
  bool include_suggestions = 4;
  }
  oneof _friends_limit {
  int32 friends_limit = 5;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 6;
  }
  oneof _exact_username_first {
  bool exact_username_first = 7;
  }
  oneof _boost_username {
  bool boost_username = 8;
  }
  optional string user_uuid = 1;
  optio
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04645"></a>
## FND-04645: oneof declaration: chesscom.friends_search.v1.SocialAutocompleteRequest._friends_limit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _friends_limit {

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 859.

```text
 bool include_friends = 3;
  }
  oneof _include_suggestions {
  bool include_suggestions = 4;
  }
  oneof _friends_limit {
  int32 friends_limit = 5;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 6;
  }
  oneof _exact_username_first {
  bool exact_username_first = 7;
  }
  oneof _boost_username {
  bool boost_username = 8;
  }
  optional string user_uuid = 1;
  optional string prefix = 2;
}

message So
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04646"></a>
## FND-04646: chesscom.friends_search.v1.SocialAutocompleteRequest.friends_limit = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 friends_limit = 5;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 884.

```text
;
  }
  oneof _include_suggestions {
  bool include_suggestions = 4;
  }
  oneof _friends_limit {
  int32 friends_limit = 5;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 6;
  }
  oneof _exact_username_first {
  bool exact_username_first = 7;
  }
  oneof _boost_username {
  bool boost_username = 8;
  }
  optional string user_uuid = 1;
  optional string prefix = 2;
}

message SocialAutocompleteResponse 
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04647"></a>
## FND-04647: oneof declaration: chesscom.friends_search.v1.SocialAutocompleteRequest._suggestions_limit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _suggestions_limit {

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 915.

```text
ons {
  bool include_suggestions = 4;
  }
  oneof _friends_limit {
  int32 friends_limit = 5;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 6;
  }
  oneof _exact_username_first {
  bool exact_username_first = 7;
  }
  oneof _boost_username {
  bool boost_username = 8;
  }
  optional string user_uuid = 1;
  optional string prefix = 2;
}

message SocialAutocompleteResponse {
  repeated .chesscom.friends_
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04648"></a>
## FND-04648: chesscom.friends_search.v1.SocialAutocompleteRequest.suggestions_limit = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 suggestions_limit = 6;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 944.

```text
ons = 4;
  }
  oneof _friends_limit {
  int32 friends_limit = 5;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 6;
  }
  oneof _exact_username_first {
  bool exact_username_first = 7;
  }
  oneof _boost_username {
  bool boost_username = 8;
  }
  optional string user_uuid = 1;
  optional string prefix = 2;
}

message SocialAutocompleteResponse {
  repeated .chesscom.friends_search.v1.SocialFriendsSearch
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04649"></a>
## FND-04649: oneof declaration: chesscom.friends_search.v1.SocialAutocompleteRequest._exact_username_first

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _exact_username_first {

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 979.

```text
 {
  int32 friends_limit = 5;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 6;
  }
  oneof _exact_username_first {
  bool exact_username_first = 7;
  }
  oneof _boost_username {
  bool boost_username = 8;
  }
  optional string user_uuid = 1;
  optional string prefix = 2;
}

message SocialAutocompleteResponse {
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;
  repeated .che
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04650"></a>
## FND-04650: chesscom.friends_search.v1.SocialAutocompleteRequest.exact_username_first = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool exact_username_first = 7;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 1011.

```text
}
  oneof _suggestions_limit {
  int32 suggestions_limit = 6;
  }
  oneof _exact_username_first {
  bool exact_username_first = 7;
  }
  oneof _boost_username {
  bool boost_username = 8;
  }
  optional string user_uuid = 1;
  optional string prefix = 2;
}

message SocialAutocompleteResponse {
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.SocialFr
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04651"></a>
## FND-04651: oneof declaration: chesscom.friends_search.v1.SocialAutocompleteRequest._boost_username

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _boost_username {

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 1048.

```text
2 suggestions_limit = 6;
  }
  oneof _exact_username_first {
  bool exact_username_first = 7;
  }
  oneof _boost_username {
  bool boost_username = 8;
  }
  optional string user_uuid = 1;
  optional string prefix = 2;
}

message SocialAutocompleteResponse {
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend suggestions = 2;
}

```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04652"></a>
## FND-04652: chesscom.friends_search.v1.SocialAutocompleteRequest.boost_username = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool boost_username = 8;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 1074.

```text
 }
  oneof _exact_username_first {
  bool exact_username_first = 7;
  }
  oneof _boost_username {
  bool boost_username = 8;
  }
  optional string user_uuid = 1;
  optional string prefix = 2;
}

message SocialAutocompleteResponse {
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend suggestions = 2;
}

```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04653"></a>
## FND-04653: chesscom.friends_search.v1.SocialAutocompleteRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 1105.

```text
t {
  bool exact_username_first = 7;
  }
  oneof _boost_username {
  bool boost_username = 8;
  }
  optional string user_uuid = 1;
  optional string prefix = 2;
}

message SocialAutocompleteResponse {
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend suggestions = 2;
}

```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04654"></a>
## FND-04654: chesscom.friends_search.v1.SocialAutocompleteRequest.prefix = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string prefix = 2;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 1138.

```text
 7;
  }
  oneof _boost_username {
  bool boost_username = 8;
  }
  optional string user_uuid = 1;
  optional string prefix = 2;
}

message SocialAutocompleteResponse {
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend suggestions = 2;
}

```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04655"></a>
## FND-04655: message declaration: chesscom.friends_search.v1.SocialAutocompleteResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SocialAutocompleteResponse {

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 1169.

```text
 {
  bool boost_username = 8;
  }
  optional string user_uuid = 1;
  optional string prefix = 2;
}

message SocialAutocompleteResponse {
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend suggestions = 2;
}

```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04656"></a>
## FND-04656: chesscom.friends_search.v1.SocialAutocompleteResponse.friends = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 203.

```text
com.friends_search.v1;

message ListRecentFriendsRequest {
}

message ListRecentFriendsResponse {
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;
}

message ListRecentPendingFriendsRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  oneof _direction {
  .chesscom.friends_search.v1.FriendRequestDirection direction = 2;
  }
}

message ListRecentPendin
```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04657"></a>
## FND-04657: chesscom.friends_search.v1.SocialAutocompleteResponse.suggestions = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend suggestions = 2;

### Evidence

- **SRC-0439** `research/proto/chesscom/friends_search/v1/friends_navigation_service.proto` — [preserved redacted evidence](../evidence/text/46bfb8d86eb81d2abd1426c9a678f174d878c5f2ea8c2842ee6990cc15c7659c.proto)
  Character offset 1286.

```text
ocompleteResponse {
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.SocialFriendsSearchFriend suggestions = 2;
}

```

**Source references:** SRC-0439, SRC-1410  
**URL references:** None independently associated  
**Related findings:** FND-04629, FND-04630, FND-04631

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04658"></a>
## FND-04658: enum declaration: chesscom.friends_search.v1.FriendsSearchPresenceStatus

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum FriendsSearchPresenceStatus {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 115.

```text
scom/friends_search/v1/friends_search.proto
// syntax: proto3

package chesscom.friends_search.v1;

enum FriendsSearchPresenceStatus {
  FRIENDS_SEARCH_PRESENCE_STATUS_UNSPECIFIED = 0;
  FRIENDS_SEARCH_PRESENCE_STATUS_OFFLINE = 1;
  FRIENDS_SEARCH_PRESENCE_STATUS_ONLINE = 2;
  FRIENDS_SEARCH_PRESENCE_STATUS_PLAYING = 3;
}

enum FriendRequestDirection {
  FRIEND_REQUEST_DIRECTION_UNSPECIFIED = 0;
  FRIEND_REQUEST_DIRE
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04659"></a>
## FND-04659: chesscom.friends_search.v1.FriendsSearchPresenceStatus.FRIENDS_SEARCH_PRESENCE_STATUS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIENDS_SEARCH_PRESENCE_STATUS_UNSPECIFIED = 0;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 152.

```text
.proto
// syntax: proto3

package chesscom.friends_search.v1;

enum FriendsSearchPresenceStatus {
  FRIENDS_SEARCH_PRESENCE_STATUS_UNSPECIFIED = 0;
  FRIENDS_SEARCH_PRESENCE_STATUS_OFFLINE = 1;
  FRIENDS_SEARCH_PRESENCE_STATUS_ONLINE = 2;
  FRIENDS_SEARCH_PRESENCE_STATUS_PLAYING = 3;
}

enum FriendRequestDirection {
  FRIEND_REQUEST_DIRECTION_UNSPECIFIED = 0;
  FRIEND_REQUEST_DIRECTION_OUTGOING = 1;
  FRIEND_REQUEST_
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04660"></a>
## FND-04660: chesscom.friends_search.v1.FriendsSearchPresenceStatus.FRIENDS_SEARCH_PRESENCE_STATUS_OFFLINE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIENDS_SEARCH_PRESENCE_STATUS_OFFLINE = 1;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 202.

```text
_search.v1;

enum FriendsSearchPresenceStatus {
  FRIENDS_SEARCH_PRESENCE_STATUS_UNSPECIFIED = 0;
  FRIENDS_SEARCH_PRESENCE_STATUS_OFFLINE = 1;
  FRIENDS_SEARCH_PRESENCE_STATUS_ONLINE = 2;
  FRIENDS_SEARCH_PRESENCE_STATUS_PLAYING = 3;
}

enum FriendRequestDirection {
  FRIEND_REQUEST_DIRECTION_UNSPECIFIED = 0;
  FRIEND_REQUEST_DIRECTION_OUTGOING = 1;
  FRIEND_REQUEST_DIRECTION_INCOMING = 2;
}

enum FriendsSearchOrder
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04661"></a>
## FND-04661: chesscom.friends_search.v1.FriendsSearchPresenceStatus.FRIENDS_SEARCH_PRESENCE_STATUS_ONLINE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIENDS_SEARCH_PRESENCE_STATUS_ONLINE = 2;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 248.

```text
{
  FRIENDS_SEARCH_PRESENCE_STATUS_UNSPECIFIED = 0;
  FRIENDS_SEARCH_PRESENCE_STATUS_OFFLINE = 1;
  FRIENDS_SEARCH_PRESENCE_STATUS_ONLINE = 2;
  FRIENDS_SEARCH_PRESENCE_STATUS_PLAYING = 3;
}

enum FriendRequestDirection {
  FRIEND_REQUEST_DIRECTION_UNSPECIFIED = 0;
  FRIEND_REQUEST_DIRECTION_OUTGOING = 1;
  FRIEND_REQUEST_DIRECTION_INCOMING = 2;
}

enum FriendsSearchOrder {
  FRIENDS_SEARCH_ORDER_UNSPECIFIED = 0;
  F
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04662"></a>
## FND-04662: chesscom.friends_search.v1.FriendsSearchPresenceStatus.FRIENDS_SEARCH_PRESENCE_STATUS_PLAYING = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIENDS_SEARCH_PRESENCE_STATUS_PLAYING = 3;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 293.

```text
D = 0;
  FRIENDS_SEARCH_PRESENCE_STATUS_OFFLINE = 1;
  FRIENDS_SEARCH_PRESENCE_STATUS_ONLINE = 2;
  FRIENDS_SEARCH_PRESENCE_STATUS_PLAYING = 3;
}

enum FriendRequestDirection {
  FRIEND_REQUEST_DIRECTION_UNSPECIFIED = 0;
  FRIEND_REQUEST_DIRECTION_OUTGOING = 1;
  FRIEND_REQUEST_DIRECTION_INCOMING = 2;
}

enum FriendsSearchOrder {
  FRIENDS_SEARCH_ORDER_UNSPECIFIED = 0;
  FRIENDS_SEARCH_ORDER_ASC = 1;
  FRIENDS_SEARCH
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04663"></a>
## FND-04663: enum declaration: chesscom.friends_search.v1.FriendRequestDirection

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum FriendRequestDirection {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 340.

```text
 = 1;
  FRIENDS_SEARCH_PRESENCE_STATUS_ONLINE = 2;
  FRIENDS_SEARCH_PRESENCE_STATUS_PLAYING = 3;
}

enum FriendRequestDirection {
  FRIEND_REQUEST_DIRECTION_UNSPECIFIED = 0;
  FRIEND_REQUEST_DIRECTION_OUTGOING = 1;
  FRIEND_REQUEST_DIRECTION_INCOMING = 2;
}

enum FriendsSearchOrder {
  FRIENDS_SEARCH_ORDER_UNSPECIFIED = 0;
  FRIENDS_SEARCH_ORDER_ASC = 1;
  FRIENDS_SEARCH_ORDER_DESC = 2;
}

enum FriendsSearchSearchabl
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04664"></a>
## FND-04664: chesscom.friends_search.v1.FriendRequestDirection.FRIEND_REQUEST_DIRECTION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIEND_REQUEST_DIRECTION_UNSPECIFIED = 0;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 372.

```text
STATUS_ONLINE = 2;
  FRIENDS_SEARCH_PRESENCE_STATUS_PLAYING = 3;
}

enum FriendRequestDirection {
  FRIEND_REQUEST_DIRECTION_UNSPECIFIED = 0;
  FRIEND_REQUEST_DIRECTION_OUTGOING = 1;
  FRIEND_REQUEST_DIRECTION_INCOMING = 2;
}

enum FriendsSearchOrder {
  FRIENDS_SEARCH_ORDER_UNSPECIFIED = 0;
  FRIENDS_SEARCH_ORDER_ASC = 1;
  FRIENDS_SEARCH_ORDER_DESC = 2;
}

enum FriendsSearchSearchableField {
  FRIENDS_SEARCH_SEARCH
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04665"></a>
## FND-04665: chesscom.friends_search.v1.FriendRequestDirection.FRIEND_REQUEST_DIRECTION_OUTGOING = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIEND_REQUEST_DIRECTION_OUTGOING = 1;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 416.

```text
_STATUS_PLAYING = 3;
}

enum FriendRequestDirection {
  FRIEND_REQUEST_DIRECTION_UNSPECIFIED = 0;
  FRIEND_REQUEST_DIRECTION_OUTGOING = 1;
  FRIEND_REQUEST_DIRECTION_INCOMING = 2;
}

enum FriendsSearchOrder {
  FRIENDS_SEARCH_ORDER_UNSPECIFIED = 0;
  FRIENDS_SEARCH_ORDER_ASC = 1;
  FRIENDS_SEARCH_ORDER_DESC = 2;
}

enum FriendsSearchSearchableField {
  FRIENDS_SEARCH_SEARCHABLE_FIELD_UNSPECIFIED = 0;
  FRIENDS_SEARCH
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04666"></a>
## FND-04666: chesscom.friends_search.v1.FriendRequestDirection.FRIEND_REQUEST_DIRECTION_INCOMING = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIEND_REQUEST_DIRECTION_INCOMING = 2;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 457.

```text
tDirection {
  FRIEND_REQUEST_DIRECTION_UNSPECIFIED = 0;
  FRIEND_REQUEST_DIRECTION_OUTGOING = 1;
  FRIEND_REQUEST_DIRECTION_INCOMING = 2;
}

enum FriendsSearchOrder {
  FRIENDS_SEARCH_ORDER_UNSPECIFIED = 0;
  FRIENDS_SEARCH_ORDER_ASC = 1;
  FRIENDS_SEARCH_ORDER_DESC = 2;
}

enum FriendsSearchSearchableField {
  FRIENDS_SEARCH_SEARCHABLE_FIELD_UNSPECIFIED = 0;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_FIRST_NAME = 1;
  FRIEN
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04667"></a>
## FND-04667: enum declaration: chesscom.friends_search.v1.FriendsSearchOrder

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum FriendsSearchOrder {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 499.

```text
SPECIFIED = 0;
  FRIEND_REQUEST_DIRECTION_OUTGOING = 1;
  FRIEND_REQUEST_DIRECTION_INCOMING = 2;
}

enum FriendsSearchOrder {
  FRIENDS_SEARCH_ORDER_UNSPECIFIED = 0;
  FRIENDS_SEARCH_ORDER_ASC = 1;
  FRIENDS_SEARCH_ORDER_DESC = 2;
}

enum FriendsSearchSearchableField {
  FRIENDS_SEARCH_SEARCHABLE_FIELD_UNSPECIFIED = 0;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_FIRST_NAME = 1;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_NAME = 2;

```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04668"></a>
## FND-04668: chesscom.friends_search.v1.FriendsSearchOrder.FRIENDS_SEARCH_ORDER_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIENDS_SEARCH_ORDER_UNSPECIFIED = 0;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 527.

```text
EST_DIRECTION_OUTGOING = 1;
  FRIEND_REQUEST_DIRECTION_INCOMING = 2;
}

enum FriendsSearchOrder {
  FRIENDS_SEARCH_ORDER_UNSPECIFIED = 0;
  FRIENDS_SEARCH_ORDER_ASC = 1;
  FRIENDS_SEARCH_ORDER_DESC = 2;
}

enum FriendsSearchSearchableField {
  FRIENDS_SEARCH_SEARCHABLE_FIELD_UNSPECIFIED = 0;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_FIRST_NAME = 1;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_NAME = 2;
  FRIENDS_SEARCH_SEARCHABLE_
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04669"></a>
## FND-04669: chesscom.friends_search.v1.FriendsSearchOrder.FRIENDS_SEARCH_ORDER_ASC = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIENDS_SEARCH_ORDER_ASC = 1;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 567.

```text
UEST_DIRECTION_INCOMING = 2;
}

enum FriendsSearchOrder {
  FRIENDS_SEARCH_ORDER_UNSPECIFIED = 0;
  FRIENDS_SEARCH_ORDER_ASC = 1;
  FRIENDS_SEARCH_ORDER_DESC = 2;
}

enum FriendsSearchSearchableField {
  FRIENDS_SEARCH_SEARCHABLE_FIELD_UNSPECIFIED = 0;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_FIRST_NAME = 1;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_NAME = 2;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_EMAIL = 3;
  FRIENDS_SEARCH_SEARCH
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04670"></a>
## FND-04670: chesscom.friends_search.v1.FriendsSearchOrder.FRIENDS_SEARCH_ORDER_DESC = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIENDS_SEARCH_ORDER_DESC = 2;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 599.

```text
enum FriendsSearchOrder {
  FRIENDS_SEARCH_ORDER_UNSPECIFIED = 0;
  FRIENDS_SEARCH_ORDER_ASC = 1;
  FRIENDS_SEARCH_ORDER_DESC = 2;
}

enum FriendsSearchSearchableField {
  FRIENDS_SEARCH_SEARCHABLE_FIELD_UNSPECIFIED = 0;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_FIRST_NAME = 1;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_NAME = 2;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_EMAIL = 3;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_COUNTRY = 4;
  FRIEND
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04671"></a>
## FND-04671: enum declaration: chesscom.friends_search.v1.FriendsSearchSearchableField

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum FriendsSearchSearchableField {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 633.

```text
S_SEARCH_ORDER_UNSPECIFIED = 0;
  FRIENDS_SEARCH_ORDER_ASC = 1;
  FRIENDS_SEARCH_ORDER_DESC = 2;
}

enum FriendsSearchSearchableField {
  FRIENDS_SEARCH_SEARCHABLE_FIELD_UNSPECIFIED = 0;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_FIRST_NAME = 1;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_NAME = 2;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_EMAIL = 3;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_COUNTRY = 4;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_USERNAME
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04672"></a>
## FND-04672: chesscom.friends_search.v1.FriendsSearchSearchableField.FRIENDS_SEARCH_SEARCHABLE_FIELD_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIENDS_SEARCH_SEARCHABLE_FIELD_UNSPECIFIED = 0;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 671.

```text
NDS_SEARCH_ORDER_ASC = 1;
  FRIENDS_SEARCH_ORDER_DESC = 2;
}

enum FriendsSearchSearchableField {
  FRIENDS_SEARCH_SEARCHABLE_FIELD_UNSPECIFIED = 0;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_FIRST_NAME = 1;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_NAME = 2;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_EMAIL = 3;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_COUNTRY = 4;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_USERNAME = 5;
  FRIENDS_SEARCH_SEARCHABLE_FIEL
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04673"></a>
## FND-04673: chesscom.friends_search.v1.FriendsSearchSearchableField.FRIENDS_SEARCH_SEARCHABLE_FIELD_FIRST_NAME = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIENDS_SEARCH_SEARCHABLE_FIELD_FIRST_NAME = 1;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 722.

```text
SC = 2;
}

enum FriendsSearchSearchableField {
  FRIENDS_SEARCH_SEARCHABLE_FIELD_UNSPECIFIED = 0;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_FIRST_NAME = 1;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_NAME = 2;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_EMAIL = 3;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_COUNTRY = 4;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_USERNAME = 5;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_LOGIN_DATE = 6;
  FRIENDS_SEARCH_SEARCHABLE_
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04674"></a>
## FND-04674: chesscom.friends_search.v1.FriendsSearchSearchableField.FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_NAME = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_NAME = 2;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 772.

```text
RIENDS_SEARCH_SEARCHABLE_FIELD_UNSPECIFIED = 0;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_FIRST_NAME = 1;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_NAME = 2;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_EMAIL = 3;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_COUNTRY = 4;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_USERNAME = 5;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_LAST_LOGIN_DATE = 6;
  FRIENDS_SEARCH_SEARCHABLE_FIELD_IS_ONLINE = 7;
  FRIENDS_SEARCH_SEARCHABLE_F
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
