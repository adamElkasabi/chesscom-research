# data_models — findings 7201–7300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-07475"></a>
## FND-07475: oneof declaration: chesscom.proto_options.api.v1.ApiAuthenticationDefinition.auth

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof auth {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 479.

```text
ader = 1;
  }
  oneof _cookie {
  string cookie = 2;
  }
}

message ApiAuthenticationDefinition {
  oneof auth {
  .chesscom.proto_options.api.v1.ApiNoAuth no_auth = 1;
  .chesscom.proto_options.api.v1.ApiSecurityBasicAuth basic_auth = 2;
  .chesscom.proto_options.api.v1.ApiSecurityBearerAuth bearer_auth = 3;
  .chesscom.proto_options.api.v1.ApiSecurityApiKeyAuth api_key_auth = 4;
  }
  optional string description = 
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07476"></a>
## FND-07476: chesscom.proto_options.api.v1.ApiAuthenticationDefinition.no_auth = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.api.v1.ApiNoAuth no_auth = 1;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 494.

```text
 oneof _cookie {
  string cookie = 2;
  }
}

message ApiAuthenticationDefinition {
  oneof auth {
  .chesscom.proto_options.api.v1.ApiNoAuth no_auth = 1;
  .chesscom.proto_options.api.v1.ApiSecurityBasicAuth basic_auth = 2;
  .chesscom.proto_options.api.v1.ApiSecurityBearerAuth bearer_auth = 3;
  .chesscom.proto_options.api.v1.ApiSecurityApiKeyAuth api_key_auth = 4;
  }
  optional string description = 5;
}

message A
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07477"></a>
## FND-07477: chesscom.proto_options.api.v1.ApiAuthenticationDefinition.basic_auth = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.api.v1.ApiSecurityBasicAuth basic_auth = 2;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 550.

```text
AuthenticationDefinition {
  oneof auth {
  .chesscom.proto_options.api.v1.ApiNoAuth no_auth = 1;
  .chesscom.proto_options.api.v1.ApiSecurityBasicAuth basic_auth = 2;
  .chesscom.proto_options.api.v1.ApiSecurityBearerAuth bearer_auth = 3;
  .chesscom.proto_options.api.v1.ApiSecurityApiKeyAuth api_key_auth = 4;
  }
  optional string description = 5;
}

message ApiAuthenticationOption {
  repeated .chesscom.proto_opti
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07478"></a>
## FND-07478: chesscom.proto_options.api.v1.ApiAuthenticationDefinition.bearer_auth = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.api.v1.ApiSecurityBearerAuth bearer_auth = 3;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 620.

```text
i.v1.ApiNoAuth no_auth = 1;
  .chesscom.proto_options.api.v1.ApiSecurityBasicAuth basic_auth = 2;
  .chesscom.proto_options.api.v1.ApiSecurityBearerAuth bearer_auth = 3;
  .chesscom.proto_options.api.v1.ApiSecurityApiKeyAuth api_key_auth = 4;
  }
  optional string description = 5;
}

message ApiAuthenticationOption {
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationDefinition definition = 1;
  repeated stri
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07479"></a>
## FND-07479: chesscom.proto_options.api.v1.ApiAuthenticationDefinition.api_key_auth = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.api.v1.ApiSecurityApiKeyAuth api_key_auth = 4;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 692.

```text
BasicAuth basic_auth = 2;
  .chesscom.proto_options.api.v1.ApiSecurityBearerAuth bearer_auth = 3;
  .chesscom.proto_options.api.v1.ApiSecurityApiKeyAuth api_key_auth = 4;
  }
  optional string description = 5;
}

message ApiAuthenticationOption {
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServerDefinition {
  oneof _description 
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07480"></a>
## FND-07480: chesscom.proto_options.api.v1.ApiAuthenticationDefinition.description = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string description = 5;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 769.

```text
uth bearer_auth = 3;
  .chesscom.proto_options.api.v1.ApiSecurityApiKeyAuth api_key_auth = 4;
  }
  optional string description = 5;
}

message ApiAuthenticationOption {
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServerDefinition {
  oneof _description {
  string description = 2;
  }
  optional string url = 1;
  repeated .chessc
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07481"></a>
## FND-07481: message declaration: chesscom.proto_options.api.v1.ApiAuthenticationOption

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ApiAuthenticationOption {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 805.

```text
to_options.api.v1.ApiSecurityApiKeyAuth api_key_auth = 4;
  }
  optional string description = 5;
}

message ApiAuthenticationOption {
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServerDefinition {
  oneof _description {
  string description = 2;
  }
  optional string url = 1;
  repeated .chesscom.proto_options.api.v1.ApiAuthentic
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07482"></a>
## FND-07482: chesscom.proto_options.api.v1.ApiAuthenticationOption.definition = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.proto_options.api.v1.ApiAuthenticationDefinition definition = 1;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 841.

```text
uth api_key_auth = 4;
  }
  optional string description = 5;
}

message ApiAuthenticationOption {
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServerDefinition {
  oneof _description {
  string description = 2;
  }
  optional string url = 1;
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
}

m
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07483"></a>
## FND-07483: chesscom.proto_options.api.v1.ApiAuthenticationOption.reference = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string reference = 2;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 927.

```text
ionOption {
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServerDefinition {
  oneof _description {
  string description = 2;
  }
  optional string url = 1;
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
}

message ApiServerOption {
  repeated .chesscom.proto_options.api.v1.ApiServerDefinition
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07484"></a>
## FND-07484: message declaration: chesscom.proto_options.api.v1.ApiServerDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ApiServerDefinition {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 961.

```text
roto_options.api.v1.ApiAuthenticationDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServerDefinition {
  oneof _description {
  string description = 2;
  }
  optional string url = 1;
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
}

message ApiServerOption {
  repeated .chesscom.proto_options.api.v1.ApiServerDefinition definition = 1;
  repeated string
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07485"></a>
## FND-07485: oneof declaration: chesscom.proto_options.api.v1.ApiServerDefinition._description

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _description {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 993.

```text
ationDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServerDefinition {
  oneof _description {
  string description = 2;
  }
  optional string url = 1;
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
}

message ApiServerOption {
  repeated .chesscom.proto_options.api.v1.ApiServerDefinition definition = 1;
  repeated string reference = 2;
}

message ApiSe
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07486"></a>
## FND-07486: chesscom.proto_options.api.v1.ApiServerDefinition.description = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string description = 2;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1016.

```text
ion = 1;
  repeated string reference = 2;
}

message ApiServerDefinition {
  oneof _description {
  string description = 2;
  }
  optional string url = 1;
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
}

message ApiServerOption {
  repeated .chesscom.proto_options.api.v1.ApiServerDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServiceMetadata {
  optio
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07487"></a>
## FND-07487: chesscom.proto_options.api.v1.ApiServerDefinition.url = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string url = 1;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1046.

```text
erence = 2;
}

message ApiServerDefinition {
  oneof _description {
  string description = 2;
  }
  optional string url = 1;
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
}

message ApiServerOption {
  repeated .chesscom.proto_options.api.v1.ApiServerDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServiceMetadata {
  optional bool is_platform_service =
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07488"></a>
## FND-07488: chesscom.proto_options.api.v1.ApiServerDefinition.authentication = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1073.

```text
erverDefinition {
  oneof _description {
  string description = 2;
  }
  optional string url = 1;
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
}

message ApiServerOption {
  repeated .chesscom.proto_options.api.v1.ApiServerDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServiceMetadata {
  optional bool is_platform_service = 1;
  optional bool is_mcp_
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07489"></a>
## FND-07489: message declaration: chesscom.proto_options.api.v1.ApiServerOption

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ApiServerOption {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1160.

```text
g url = 1;
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
}

message ApiServerOption {
  repeated .chesscom.proto_options.api.v1.ApiServerDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServiceMetadata {
  optional bool is_platform_service = 1;
  optional bool is_mcp_service = 2;
}

message ApiOptions {
  oneof _prefix {
  string prefix = 1;
  }
  oneof
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07490"></a>
## FND-07490: chesscom.proto_options.api.v1.ApiServerOption.definition = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.proto_options.api.v1.ApiServerDefinition definition = 1;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1188.

```text
com.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
}

message ApiServerOption {
  repeated .chesscom.proto_options.api.v1.ApiServerDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServiceMetadata {
  optional bool is_platform_service = 1;
  optional bool is_mcp_service = 2;
}

message ApiOptions {
  oneof _prefix {
  string prefix = 1;
  }
  oneof _server {
  .chesscom.proto
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07491"></a>
## FND-07491: chesscom.proto_options.api.v1.ApiServerOption.reference = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string reference = 2;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 927.

```text
ionOption {
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServerDefinition {
  oneof _description {
  string description = 2;
  }
  optional string url = 1;
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
}

message ApiServerOption {
  repeated .chesscom.proto_options.api.v1.ApiServerDefinition
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07492"></a>
## FND-07492: message declaration: chesscom.proto_options.api.v1.ApiServiceMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ApiServiceMetadata {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1300.

```text
esscom.proto_options.api.v1.ApiServerDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServiceMetadata {
  optional bool is_platform_service = 1;
  optional bool is_mcp_service = 2;
}

message ApiOptions {
  oneof _prefix {
  string prefix = 1;
  }
  oneof _server {
  .chesscom.proto_options.api.v1.ApiServerOption server = 2;
  }
  oneof _metadata {
  .chesscom.proto_options.api.v1.ApiServiceM
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07493"></a>
## FND-07493: chesscom.proto_options.api.v1.ApiServiceMetadata.is_platform_service = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_platform_service = 1;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1331.

```text
ServerDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServiceMetadata {
  optional bool is_platform_service = 1;
  optional bool is_mcp_service = 2;
}

message ApiOptions {
  oneof _prefix {
  string prefix = 1;
  }
  oneof _server {
  .chesscom.proto_options.api.v1.ApiServerOption server = 2;
  }
  oneof _metadata {
  .chesscom.proto_options.api.v1.ApiServiceMetadata metadata = 4;
  }
  rep
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07494"></a>
## FND-07494: chesscom.proto_options.api.v1.ApiServiceMetadata.is_mcp_service = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_mcp_service = 2;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1372.

```text
ed string reference = 2;
}

message ApiServiceMetadata {
  optional bool is_platform_service = 1;
  optional bool is_mcp_service = 2;
}

message ApiOptions {
  oneof _prefix {
  string prefix = 1;
  }
  oneof _server {
  .chesscom.proto_options.api.v1.ApiServerOption server = 2;
  }
  oneof _metadata {
  .chesscom.proto_options.api.v1.ApiServiceMetadata metadata = 4;
  }
  repeated .chesscom.proto_options.api.v1.ApiA
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07495"></a>
## FND-07495: message declaration: chesscom.proto_options.api.v1.ApiOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ApiOptions {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1409.

```text
piServiceMetadata {
  optional bool is_platform_service = 1;
  optional bool is_mcp_service = 2;
}

message ApiOptions {
  oneof _prefix {
  string prefix = 1;
  }
  oneof _server {
  .chesscom.proto_options.api.v1.ApiServerOption server = 2;
  }
  oneof _metadata {
  .chesscom.proto_options.api.v1.ApiServiceMetadata metadata = 4;
  }
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07496"></a>
## FND-07496: oneof declaration: chesscom.proto_options.api.v1.ApiOptions._prefix

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _prefix {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1432.

```text
ptional bool is_platform_service = 1;
  optional bool is_mcp_service = 2;
}

message ApiOptions {
  oneof _prefix {
  string prefix = 1;
  }
  oneof _server {
  .chesscom.proto_options.api.v1.ApiServerOption server = 2;
  }
  oneof _metadata {
  .chesscom.proto_options.api.v1.ApiServiceMetadata metadata = 4;
  }
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
  repeated .chesscom
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07497"></a>
## FND-07497: chesscom.proto_options.api.v1.ApiOptions.prefix = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string prefix = 1;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1450.

```text
atform_service = 1;
  optional bool is_mcp_service = 2;
}

message ApiOptions {
  oneof _prefix {
  string prefix = 1;
  }
  oneof _server {
  .chesscom.proto_options.api.v1.ApiServerOption server = 2;
  }
  oneof _metadata {
  .chesscom.proto_options.api.v1.ApiServiceMetadata metadata = 4;
  }
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
  repeated .chesscom.oauth.v1.Scope sc
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07498"></a>
## FND-07498: oneof declaration: chesscom.proto_options.api.v1.ApiOptions._server

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _server {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1475.

```text
ional bool is_mcp_service = 2;
}

message ApiOptions {
  oneof _prefix {
  string prefix = 1;
  }
  oneof _server {
  .chesscom.proto_options.api.v1.ApiServerOption server = 2;
  }
  oneof _metadata {
  .chesscom.proto_options.api.v1.ApiServiceMetadata metadata = 4;
  }
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
  repeated .chesscom.oauth.v1.Scope scope = 5;
  optional .ches
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07499"></a>
## FND-07499: chesscom.proto_options.api.v1.ApiOptions.server = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.api.v1.ApiServerOption server = 2;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1493.

```text
service = 2;
}

message ApiOptions {
  oneof _prefix {
  string prefix = 1;
  }
  oneof _server {
  .chesscom.proto_options.api.v1.ApiServerOption server = 2;
  }
  oneof _metadata {
  .chesscom.proto_options.api.v1.ApiServiceMetadata metadata = 4;
  }
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
  repeated .chesscom.oauth.v1.Scope scope = 5;
  optional .chesscom.proto_options
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07500"></a>
## FND-07500: oneof declaration: chesscom.proto_options.api.v1.ApiOptions._metadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _metadata {

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1558.

```text
refix = 1;
  }
  oneof _server {
  .chesscom.proto_options.api.v1.ApiServerOption server = 2;
  }
  oneof _metadata {
  .chesscom.proto_options.api.v1.ApiServiceMetadata metadata = 4;
  }
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
  repeated .chesscom.oauth.v1.Scope scope = 5;
  optional .chesscom.proto_options.api.v1.RpcProtocol protocol = 6;
}

```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07501"></a>
## FND-07501: chesscom.proto_options.api.v1.ApiOptions.metadata = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.api.v1.ApiServiceMetadata metadata = 4;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1578.

```text
of _server {
  .chesscom.proto_options.api.v1.ApiServerOption server = 2;
  }
  oneof _metadata {
  .chesscom.proto_options.api.v1.ApiServiceMetadata metadata = 4;
  }
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
  repeated .chesscom.oauth.v1.Scope scope = 5;
  optional .chesscom.proto_options.api.v1.RpcProtocol protocol = 6;
}

```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07502"></a>
## FND-07502: chesscom.proto_options.api.v1.ApiOptions.authentication = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1073.

```text
erverDefinition {
  oneof _description {
  string description = 2;
  }
  optional string url = 1;
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
}

message ApiServerOption {
  repeated .chesscom.proto_options.api.v1.ApiServerDefinition definition = 1;
  repeated string reference = 2;
}

message ApiServiceMetadata {
  optional bool is_platform_service = 1;
  optional bool is_mcp_
```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07503"></a>
## FND-07503: chesscom.proto_options.api.v1.ApiOptions.scope = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.oauth.v1.Scope scope = 5;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1734.

```text
ta = 4;
  }
  repeated .chesscom.proto_options.api.v1.ApiAuthenticationOption authentication = 3;
  repeated .chesscom.oauth.v1.Scope scope = 5;
  optional .chesscom.proto_options.api.v1.RpcProtocol protocol = 6;
}

```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07504"></a>
## FND-07504: chesscom.proto_options.api.v1.ApiOptions.protocol = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.api.v1.RpcProtocol protocol = 6;

### Evidence

- **SRC-0521** `research/proto/chesscom/proto_options/api/v1/api_options.proto` — [preserved redacted evidence](../evidence/text/28a91b696d08bd17b266875a28feb6a6a1883912ad7c5db423da9b89a1dcaa28.proto)
  Character offset 1781.

```text
api.v1.ApiAuthenticationOption authentication = 3;
  repeated .chesscom.oauth.v1.Scope scope = 5;
  optional .chesscom.proto_options.api.v1.RpcProtocol protocol = 6;
}

```

**Source references:** SRC-0521, SRC-1492  
**URL references:** None independently associated  
**Related findings:** FND-07462, FND-07463, FND-07464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07505"></a>
## FND-07505: message declaration: chesscom.proto_options.configurator.v1.ConfiguratorMessageOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ConfiguratorMessageOptions {

### Evidence

- **SRC-0522** `research/proto/chesscom/proto_options/configurator/v1/configurator_options.proto` — [preserved redacted evidence](../evidence/text/41090bf525e5caa7562a08ef5ff94b2b9d846cfe92f1fa6c09e1a400e5629a6b.proto)
  Character offset 145.

```text
r/v1/configurator_options.proto
// syntax: proto3

package chesscom.proto_options.configurator.v1;

message ConfiguratorMessageOptions {
  optional bool configurable = 1;
}

```

**Source references:** SRC-0522, SRC-1493  
**URL references:** None independently associated  
**Related findings:** FND-07506

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07506"></a>
## FND-07506: chesscom.proto_options.configurator.v1.ConfiguratorMessageOptions.configurable = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool configurable = 1;

### Evidence

- **SRC-0522** `research/proto/chesscom/proto_options/configurator/v1/configurator_options.proto` — [preserved redacted evidence](../evidence/text/41090bf525e5caa7562a08ef5ff94b2b9d846cfe92f1fa6c09e1a400e5629a6b.proto)
  Character offset 184.

```text
ax: proto3

package chesscom.proto_options.configurator.v1;

message ConfiguratorMessageOptions {
  optional bool configurable = 1;
}

```

**Source references:** SRC-0522, SRC-1493  
**URL references:** None independently associated  
**Related findings:** FND-07505

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07507"></a>
## FND-07507: enum declaration: chesscom.proto_options.events.v1.EventCategory

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum EventCategory {

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 126.

```text
options/events/v1/event_options.proto
// syntax: proto3

package chesscom.proto_options.events.v1;

enum EventCategory {
  EVENT_CATEGORY_UNSPECIFIED = 0;
  EVENT_CATEGORY_IMPRESSION = 1;
  EVENT_CATEGORY_USER_ACTION = 2;
  EVENT_CATEGORY_SERVER_ACTION = 3;
  EVENT_CATEGORY_LOG = 4;
}

enum EventType {
  EVENT_TYPE_UNSPECIFIED = 0;
  EVENT_TYPE_IMPRESSION = 1;
  EVENT_TYPE_INTERFACE_OPENED = 2;
  EVENT_TYPE_INTERFACE
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07508"></a>
## FND-07508: chesscom.proto_options.events.v1.EventCategory.EVENT_CATEGORY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_CATEGORY_UNSPECIFIED = 0;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 149.

```text
_options.proto
// syntax: proto3

package chesscom.proto_options.events.v1;

enum EventCategory {
  EVENT_CATEGORY_UNSPECIFIED = 0;
  EVENT_CATEGORY_IMPRESSION = 1;
  EVENT_CATEGORY_USER_ACTION = 2;
  EVENT_CATEGORY_SERVER_ACTION = 3;
  EVENT_CATEGORY_LOG = 4;
}

enum EventType {
  EVENT_TYPE_UNSPECIFIED = 0;
  EVENT_TYPE_IMPRESSION = 1;
  EVENT_TYPE_INTERFACE_OPENED = 2;
  EVENT_TYPE_INTERFACE_CLOSED = 3;
  EVENT_TY
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07509"></a>
## FND-07509: chesscom.proto_options.events.v1.EventCategory.EVENT_CATEGORY_IMPRESSION = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_CATEGORY_IMPRESSION = 1;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 183.

```text
package chesscom.proto_options.events.v1;

enum EventCategory {
  EVENT_CATEGORY_UNSPECIFIED = 0;
  EVENT_CATEGORY_IMPRESSION = 1;
  EVENT_CATEGORY_USER_ACTION = 2;
  EVENT_CATEGORY_SERVER_ACTION = 3;
  EVENT_CATEGORY_LOG = 4;
}

enum EventType {
  EVENT_TYPE_UNSPECIFIED = 0;
  EVENT_TYPE_IMPRESSION = 1;
  EVENT_TYPE_INTERFACE_OPENED = 2;
  EVENT_TYPE_INTERFACE_CLOSED = 3;
  EVENT_TYPE_BUTTON_CLICK = 4;
  EVENT_TYPE_
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07510"></a>
## FND-07510: chesscom.proto_options.events.v1.EventCategory.EVENT_CATEGORY_USER_ACTION = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_CATEGORY_USER_ACTION = 2;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 216.

```text
ents.v1;

enum EventCategory {
  EVENT_CATEGORY_UNSPECIFIED = 0;
  EVENT_CATEGORY_IMPRESSION = 1;
  EVENT_CATEGORY_USER_ACTION = 2;
  EVENT_CATEGORY_SERVER_ACTION = 3;
  EVENT_CATEGORY_LOG = 4;
}

enum EventType {
  EVENT_TYPE_UNSPECIFIED = 0;
  EVENT_TYPE_IMPRESSION = 1;
  EVENT_TYPE_INTERFACE_OPENED = 2;
  EVENT_TYPE_INTERFACE_CLOSED = 3;
  EVENT_TYPE_BUTTON_CLICK = 4;
  EVENT_TYPE_TEXT_ENTRY = 5;
  EVENT_TYPE_MODA
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07511"></a>
## FND-07511: chesscom.proto_options.events.v1.EventCategory.EVENT_CATEGORY_SERVER_ACTION = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_CATEGORY_SERVER_ACTION = 3;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 250.

```text
VENT_CATEGORY_UNSPECIFIED = 0;
  EVENT_CATEGORY_IMPRESSION = 1;
  EVENT_CATEGORY_USER_ACTION = 2;
  EVENT_CATEGORY_SERVER_ACTION = 3;
  EVENT_CATEGORY_LOG = 4;
}

enum EventType {
  EVENT_TYPE_UNSPECIFIED = 0;
  EVENT_TYPE_IMPRESSION = 1;
  EVENT_TYPE_INTERFACE_OPENED = 2;
  EVENT_TYPE_INTERFACE_CLOSED = 3;
  EVENT_TYPE_BUTTON_CLICK = 4;
  EVENT_TYPE_TEXT_ENTRY = 5;
  EVENT_TYPE_MODAL_OPENED = 6;
  EVENT_TYPE_NOTIFIC
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07512"></a>
## FND-07512: chesscom.proto_options.events.v1.EventCategory.EVENT_CATEGORY_LOG = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_CATEGORY_LOG = 4;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 286.

```text
NT_CATEGORY_IMPRESSION = 1;
  EVENT_CATEGORY_USER_ACTION = 2;
  EVENT_CATEGORY_SERVER_ACTION = 3;
  EVENT_CATEGORY_LOG = 4;
}

enum EventType {
  EVENT_TYPE_UNSPECIFIED = 0;
  EVENT_TYPE_IMPRESSION = 1;
  EVENT_TYPE_INTERFACE_OPENED = 2;
  EVENT_TYPE_INTERFACE_CLOSED = 3;
  EVENT_TYPE_BUTTON_CLICK = 4;
  EVENT_TYPE_TEXT_ENTRY = 5;
  EVENT_TYPE_MODAL_OPENED = 6;
  EVENT_TYPE_NOTIFICATION_SENT = 7;
  EVENT_TYPE_LINK_CL
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07513"></a>
## FND-07513: enum declaration: chesscom.proto_options.events.v1.EventType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum EventType {

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 313.

```text

  EVENT_CATEGORY_USER_ACTION = 2;
  EVENT_CATEGORY_SERVER_ACTION = 3;
  EVENT_CATEGORY_LOG = 4;
}

enum EventType {
  EVENT_TYPE_UNSPECIFIED = 0;
  EVENT_TYPE_IMPRESSION = 1;
  EVENT_TYPE_INTERFACE_OPENED = 2;
  EVENT_TYPE_INTERFACE_CLOSED = 3;
  EVENT_TYPE_BUTTON_CLICK = 4;
  EVENT_TYPE_TEXT_ENTRY = 5;
  EVENT_TYPE_MODAL_OPENED = 6;
  EVENT_TYPE_NOTIFICATION_SENT = 7;
  EVENT_TYPE_LINK_CLICKED = 8;
  EVENT_TYPE_NOT
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07514"></a>
## FND-07514: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 332.

```text
SER_ACTION = 2;
  EVENT_CATEGORY_SERVER_ACTION = 3;
  EVENT_CATEGORY_LOG = 4;
}

enum EventType {
  EVENT_TYPE_UNSPECIFIED = 0;
  EVENT_TYPE_IMPRESSION = 1;
  EVENT_TYPE_INTERFACE_OPENED = 2;
  EVENT_TYPE_INTERFACE_CLOSED = 3;
  EVENT_TYPE_BUTTON_CLICK = 4;
  EVENT_TYPE_TEXT_ENTRY = 5;
  EVENT_TYPE_MODAL_OPENED = 6;
  EVENT_TYPE_NOTIFICATION_SENT = 7;
  EVENT_TYPE_LINK_CLICKED = 8;
  EVENT_TYPE_NOTIFICATION_OPENED = 
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07515"></a>
## FND-07515: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_IMPRESSION = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_IMPRESSION = 1;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 362.

```text
RY_SERVER_ACTION = 3;
  EVENT_CATEGORY_LOG = 4;
}

enum EventType {
  EVENT_TYPE_UNSPECIFIED = 0;
  EVENT_TYPE_IMPRESSION = 1;
  EVENT_TYPE_INTERFACE_OPENED = 2;
  EVENT_TYPE_INTERFACE_CLOSED = 3;
  EVENT_TYPE_BUTTON_CLICK = 4;
  EVENT_TYPE_TEXT_ENTRY = 5;
  EVENT_TYPE_MODAL_OPENED = 6;
  EVENT_TYPE_NOTIFICATION_SENT = 7;
  EVENT_TYPE_LINK_CLICKED = 8;
  EVENT_TYPE_NOTIFICATION_OPENED = 9;
  EVENT_TYPE_GAME_ACTION = 
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07516"></a>
## FND-07516: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_INTERFACE_OPENED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_INTERFACE_OPENED = 2;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 391.

```text
_CATEGORY_LOG = 4;
}

enum EventType {
  EVENT_TYPE_UNSPECIFIED = 0;
  EVENT_TYPE_IMPRESSION = 1;
  EVENT_TYPE_INTERFACE_OPENED = 2;
  EVENT_TYPE_INTERFACE_CLOSED = 3;
  EVENT_TYPE_BUTTON_CLICK = 4;
  EVENT_TYPE_TEXT_ENTRY = 5;
  EVENT_TYPE_MODAL_OPENED = 6;
  EVENT_TYPE_NOTIFICATION_SENT = 7;
  EVENT_TYPE_LINK_CLICKED = 8;
  EVENT_TYPE_NOTIFICATION_OPENED = 9;
  EVENT_TYPE_GAME_ACTION = 10;
  EVENT_TYPE_USER_STATUS_
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07517"></a>
## FND-07517: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_INTERFACE_CLOSED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_INTERFACE_CLOSED = 3;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 426.

```text
e {
  EVENT_TYPE_UNSPECIFIED = 0;
  EVENT_TYPE_IMPRESSION = 1;
  EVENT_TYPE_INTERFACE_OPENED = 2;
  EVENT_TYPE_INTERFACE_CLOSED = 3;
  EVENT_TYPE_BUTTON_CLICK = 4;
  EVENT_TYPE_TEXT_ENTRY = 5;
  EVENT_TYPE_MODAL_OPENED = 6;
  EVENT_TYPE_NOTIFICATION_SENT = 7;
  EVENT_TYPE_LINK_CLICKED = 8;
  EVENT_TYPE_NOTIFICATION_OPENED = 9;
  EVENT_TYPE_GAME_ACTION = 10;
  EVENT_TYPE_USER_STATUS_SYSTEM_ACTION = 11;
  EVENT_TYPE_MO
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07518"></a>
## FND-07518: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_BUTTON_CLICK = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_BUTTON_CLICK = 4;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 461.

```text
 EVENT_TYPE_IMPRESSION = 1;
  EVENT_TYPE_INTERFACE_OPENED = 2;
  EVENT_TYPE_INTERFACE_CLOSED = 3;
  EVENT_TYPE_BUTTON_CLICK = 4;
  EVENT_TYPE_TEXT_ENTRY = 5;
  EVENT_TYPE_MODAL_OPENED = 6;
  EVENT_TYPE_NOTIFICATION_SENT = 7;
  EVENT_TYPE_LINK_CLICKED = 8;
  EVENT_TYPE_NOTIFICATION_OPENED = 9;
  EVENT_TYPE_GAME_ACTION = 10;
  EVENT_TYPE_USER_STATUS_SYSTEM_ACTION = 11;
  EVENT_TYPE_MODAL_CLOSED = 12;
  EVENT_TYPE_SOCIA
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07519"></a>
## FND-07519: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_TEXT_ENTRY = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_TEXT_ENTRY = 5;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 492.

```text
VENT_TYPE_INTERFACE_OPENED = 2;
  EVENT_TYPE_INTERFACE_CLOSED = 3;
  EVENT_TYPE_BUTTON_CLICK = 4;
  EVENT_TYPE_TEXT_ENTRY = 5;
  EVENT_TYPE_MODAL_OPENED = 6;
  EVENT_TYPE_NOTIFICATION_SENT = 7;
  EVENT_TYPE_LINK_CLICKED = 8;
  EVENT_TYPE_NOTIFICATION_OPENED = 9;
  EVENT_TYPE_GAME_ACTION = 10;
  EVENT_TYPE_USER_STATUS_SYSTEM_ACTION = 11;
  EVENT_TYPE_MODAL_CLOSED = 12;
  EVENT_TYPE_SOCIAL_ACTION = 13;
  EVENT_TYPE_NOT
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07520"></a>
## FND-07520: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_MODAL_OPENED = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_MODAL_OPENED = 6;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 521.

```text
2;
  EVENT_TYPE_INTERFACE_CLOSED = 3;
  EVENT_TYPE_BUTTON_CLICK = 4;
  EVENT_TYPE_TEXT_ENTRY = 5;
  EVENT_TYPE_MODAL_OPENED = 6;
  EVENT_TYPE_NOTIFICATION_SENT = 7;
  EVENT_TYPE_LINK_CLICKED = 8;
  EVENT_TYPE_NOTIFICATION_OPENED = 9;
  EVENT_TYPE_GAME_ACTION = 10;
  EVENT_TYPE_USER_STATUS_SYSTEM_ACTION = 11;
  EVENT_TYPE_MODAL_CLOSED = 12;
  EVENT_TYPE_SOCIAL_ACTION = 13;
  EVENT_TYPE_NOTIFICATION_CLICKED = 14;
  EVE
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07521"></a>
## FND-07521: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_NOTIFICATION_SENT = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_NOTIFICATION_SENT = 7;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 552.

```text
D = 3;
  EVENT_TYPE_BUTTON_CLICK = 4;
  EVENT_TYPE_TEXT_ENTRY = 5;
  EVENT_TYPE_MODAL_OPENED = 6;
  EVENT_TYPE_NOTIFICATION_SENT = 7;
  EVENT_TYPE_LINK_CLICKED = 8;
  EVENT_TYPE_NOTIFICATION_OPENED = 9;
  EVENT_TYPE_GAME_ACTION = 10;
  EVENT_TYPE_USER_STATUS_SYSTEM_ACTION = 11;
  EVENT_TYPE_MODAL_CLOSED = 12;
  EVENT_TYPE_SOCIAL_ACTION = 13;
  EVENT_TYPE_NOTIFICATION_CLICKED = 14;
  EVENT_TYPE_UNSUBSCRIBED = 15;
  EV
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07522"></a>
## FND-07522: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_LINK_CLICKED = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_LINK_CLICKED = 8;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 588.

```text
;
  EVENT_TYPE_TEXT_ENTRY = 5;
  EVENT_TYPE_MODAL_OPENED = 6;
  EVENT_TYPE_NOTIFICATION_SENT = 7;
  EVENT_TYPE_LINK_CLICKED = 8;
  EVENT_TYPE_NOTIFICATION_OPENED = 9;
  EVENT_TYPE_GAME_ACTION = 10;
  EVENT_TYPE_USER_STATUS_SYSTEM_ACTION = 11;
  EVENT_TYPE_MODAL_CLOSED = 12;
  EVENT_TYPE_SOCIAL_ACTION = 13;
  EVENT_TYPE_NOTIFICATION_CLICKED = 14;
  EVENT_TYPE_UNSUBSCRIBED = 15;
  EVENT_TYPE_NOTIFICATION_DELIVERED = 16
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07523"></a>
## FND-07523: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_NOTIFICATION_OPENED = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_NOTIFICATION_OPENED = 9;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 619.

```text
  EVENT_TYPE_MODAL_OPENED = 6;
  EVENT_TYPE_NOTIFICATION_SENT = 7;
  EVENT_TYPE_LINK_CLICKED = 8;
  EVENT_TYPE_NOTIFICATION_OPENED = 9;
  EVENT_TYPE_GAME_ACTION = 10;
  EVENT_TYPE_USER_STATUS_SYSTEM_ACTION = 11;
  EVENT_TYPE_MODAL_CLOSED = 12;
  EVENT_TYPE_SOCIAL_ACTION = 13;
  EVENT_TYPE_NOTIFICATION_CLICKED = 14;
  EVENT_TYPE_UNSUBSCRIBED = 15;
  EVENT_TYPE_NOTIFICATION_DELIVERED = 16;
}

enum Funnel {
  FUNNEL_UNS
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07524"></a>
## FND-07524: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_GAME_ACTION = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_GAME_ACTION = 10;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 657.

```text
_TYPE_NOTIFICATION_SENT = 7;
  EVENT_TYPE_LINK_CLICKED = 8;
  EVENT_TYPE_NOTIFICATION_OPENED = 9;
  EVENT_TYPE_GAME_ACTION = 10;
  EVENT_TYPE_USER_STATUS_SYSTEM_ACTION = 11;
  EVENT_TYPE_MODAL_CLOSED = 12;
  EVENT_TYPE_SOCIAL_ACTION = 13;
  EVENT_TYPE_NOTIFICATION_CLICKED = 14;
  EVENT_TYPE_UNSUBSCRIBED = 15;
  EVENT_TYPE_NOTIFICATION_DELIVERED = 16;
}

enum Funnel {
  FUNNEL_UNSPECIFIED = 0;
  FUNNEL_RECOMMENDED_MAT
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07525"></a>
## FND-07525: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_USER_STATUS_SYSTEM_ACTION = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_USER_STATUS_SYSTEM_ACTION = 11;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 688.

```text
EVENT_TYPE_LINK_CLICKED = 8;
  EVENT_TYPE_NOTIFICATION_OPENED = 9;
  EVENT_TYPE_GAME_ACTION = 10;
  EVENT_TYPE_USER_STATUS_SYSTEM_ACTION = 11;
  EVENT_TYPE_MODAL_CLOSED = 12;
  EVENT_TYPE_SOCIAL_ACTION = 13;
  EVENT_TYPE_NOTIFICATION_CLICKED = 14;
  EVENT_TYPE_UNSUBSCRIBED = 15;
  EVENT_TYPE_NOTIFICATION_DELIVERED = 16;
}

enum Funnel {
  FUNNEL_UNSPECIFIED = 0;
  FUNNEL_RECOMMENDED_MATCH = 1;
  FUNNEL_SIGNUP = 2;
  
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07526"></a>
## FND-07526: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_MODAL_CLOSED = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_MODAL_CLOSED = 12;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 733.

```text
IFICATION_OPENED = 9;
  EVENT_TYPE_GAME_ACTION = 10;
  EVENT_TYPE_USER_STATUS_SYSTEM_ACTION = 11;
  EVENT_TYPE_MODAL_CLOSED = 12;
  EVENT_TYPE_SOCIAL_ACTION = 13;
  EVENT_TYPE_NOTIFICATION_CLICKED = 14;
  EVENT_TYPE_UNSUBSCRIBED = 15;
  EVENT_TYPE_NOTIFICATION_DELIVERED = 16;
}

enum Funnel {
  FUNNEL_UNSPECIFIED = 0;
  FUNNEL_RECOMMENDED_MATCH = 1;
  FUNNEL_SIGNUP = 2;
  FUNNEL_GAME_CREATE = 3;
  FUNNEL_GAME_REVIEW 
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07527"></a>
## FND-07527: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_SOCIAL_ACTION = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_SOCIAL_ACTION = 13;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 765.

```text
PE_GAME_ACTION = 10;
  EVENT_TYPE_USER_STATUS_SYSTEM_ACTION = 11;
  EVENT_TYPE_MODAL_CLOSED = 12;
  EVENT_TYPE_SOCIAL_ACTION = 13;
  EVENT_TYPE_NOTIFICATION_CLICKED = 14;
  EVENT_TYPE_UNSUBSCRIBED = 15;
  EVENT_TYPE_NOTIFICATION_DELIVERED = 16;
}

enum Funnel {
  FUNNEL_UNSPECIFIED = 0;
  FUNNEL_RECOMMENDED_MATCH = 1;
  FUNNEL_SIGNUP = 2;
  FUNNEL_GAME_CREATE = 3;
  FUNNEL_GAME_REVIEW = 4;
  FUNNEL_PUZZLES = 5;
  FUN
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07528"></a>
## FND-07528: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_NOTIFICATION_CLICKED = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_NOTIFICATION_CLICKED = 14;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 798.

```text
_USER_STATUS_SYSTEM_ACTION = 11;
  EVENT_TYPE_MODAL_CLOSED = 12;
  EVENT_TYPE_SOCIAL_ACTION = 13;
  EVENT_TYPE_NOTIFICATION_CLICKED = 14;
  EVENT_TYPE_UNSUBSCRIBED = 15;
  EVENT_TYPE_NOTIFICATION_DELIVERED = 16;
}

enum Funnel {
  FUNNEL_UNSPECIFIED = 0;
  FUNNEL_RECOMMENDED_MATCH = 1;
  FUNNEL_SIGNUP = 2;
  FUNNEL_GAME_CREATE = 3;
  FUNNEL_GAME_REVIEW = 4;
  FUNNEL_PUZZLES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07529"></a>
## FND-07529: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_UNSUBSCRIBED = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_UNSUBSCRIBED = 15;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 838.

```text
_TYPE_MODAL_CLOSED = 12;
  EVENT_TYPE_SOCIAL_ACTION = 13;
  EVENT_TYPE_NOTIFICATION_CLICKED = 14;
  EVENT_TYPE_UNSUBSCRIBED = 15;
  EVENT_TYPE_NOTIFICATION_DELIVERED = 16;
}

enum Funnel {
  FUNNEL_UNSPECIFIED = 0;
  FUNNEL_RECOMMENDED_MATCH = 1;
  FUNNEL_SIGNUP = 2;
  FUNNEL_GAME_CREATE = 3;
  FUNNEL_GAME_REVIEW = 4;
  FUNNEL_PUZZLES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_P
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07530"></a>
## FND-07530: chesscom.proto_options.events.v1.EventType.EVENT_TYPE_NOTIFICATION_DELIVERED = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_NOTIFICATION_DELIVERED = 16;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 870.

```text
_TYPE_SOCIAL_ACTION = 13;
  EVENT_TYPE_NOTIFICATION_CLICKED = 14;
  EVENT_TYPE_UNSUBSCRIBED = 15;
  EVENT_TYPE_NOTIFICATION_DELIVERED = 16;
}

enum Funnel {
  FUNNEL_UNSPECIFIED = 0;
  FUNNEL_RECOMMENDED_MATCH = 1;
  FUNNEL_SIGNUP = 2;
  FUNNEL_GAME_CREATE = 3;
  FUNNEL_GAME_REVIEW = 4;
  FUNNEL_PUZZLES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07531"></a>
## FND-07531: enum declaration: chesscom.proto_options.events.v1.Funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Funnel {

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 913.

```text
FICATION_CLICKED = 14;
  EVENT_TYPE_UNSUBSCRIBED = 15;
  EVENT_TYPE_NOTIFICATION_DELIVERED = 16;
}

enum Funnel {
  FUNNEL_UNSPECIFIED = 0;
  FUNNEL_RECOMMENDED_MATCH = 1;
  FUNNEL_SIGNUP = 2;
  FUNNEL_GAME_CREATE = 3;
  FUNNEL_GAME_REVIEW = 4;
  FUNNEL_PUZZLES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH 
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07532"></a>
## FND-07532: chesscom.proto_options.events.v1.Funnel.FUNNEL_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_UNSPECIFIED = 0;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 929.

```text
 = 14;
  EVENT_TYPE_UNSUBSCRIBED = 15;
  EVENT_TYPE_NOTIFICATION_DELIVERED = 16;
}

enum Funnel {
  FUNNEL_UNSPECIFIED = 0;
  FUNNEL_RECOMMENDED_MATCH = 1;
  FUNNEL_SIGNUP = 2;
  FUNNEL_GAME_CREATE = 3;
  FUNNEL_GAME_REVIEW = 4;
  FUNNEL_PUZZLES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_C
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07533"></a>
## FND-07533: chesscom.proto_options.events.v1.Funnel.FUNNEL_RECOMMENDED_MATCH = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_RECOMMENDED_MATCH = 1;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 955.

```text
CRIBED = 15;
  EVENT_TYPE_NOTIFICATION_DELIVERED = 16;
}

enum Funnel {
  FUNNEL_UNSPECIFIED = 0;
  FUNNEL_RECOMMENDED_MATCH = 1;
  FUNNEL_SIGNUP = 2;
  FUNNEL_GAME_CREATE = 3;
  FUNNEL_GAME_REVIEW = 4;
  FUNNEL_PUZZLES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LES
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07534"></a>
## FND-07534: chesscom.proto_options.events.v1.Funnel.FUNNEL_SIGNUP = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_SIGNUP = 2;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 987.

```text
CATION_DELIVERED = 16;
}

enum Funnel {
  FUNNEL_UNSPECIFIED = 0;
  FUNNEL_RECOMMENDED_MATCH = 1;
  FUNNEL_SIGNUP = 2;
  FUNNEL_GAME_CREATE = 3;
  FUNNEL_GAME_REVIEW = 4;
  FUNNEL_PUZZLES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07535"></a>
## FND-07535: chesscom.proto_options.events.v1.Funnel.FUNNEL_GAME_CREATE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_GAME_CREATE = 3;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1008.

```text
;
}

enum Funnel {
  FUNNEL_UNSPECIFIED = 0;
  FUNNEL_RECOMMENDED_MATCH = 1;
  FUNNEL_SIGNUP = 2;
  FUNNEL_GAME_CREATE = 3;
  FUNNEL_GAME_REVIEW = 4;
  FUNNEL_PUZZLES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07536"></a>
## FND-07536: chesscom.proto_options.events.v1.Funnel.FUNNEL_GAME_REVIEW = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_GAME_REVIEW = 4;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1034.

```text
L_UNSPECIFIED = 0;
  FUNNEL_RECOMMENDED_MATCH = 1;
  FUNNEL_SIGNUP = 2;
  FUNNEL_GAME_CREATE = 3;
  FUNNEL_GAME_REVIEW = 4;
  FUNNEL_PUZZLES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FU
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07537"></a>
## FND-07537: chesscom.proto_options.events.v1.Funnel.FUNNEL_PUZZLES = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_PUZZLES = 5;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1060.

```text
L_RECOMMENDED_MATCH = 1;
  FUNNEL_SIGNUP = 2;
  FUNNEL_GAME_CREATE = 3;
  FUNNEL_GAME_REVIEW = 4;
  FUNNEL_PUZZLES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNN
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07538"></a>
## FND-07538: chesscom.proto_options.events.v1.Funnel.FUNNEL_FRIENDS = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_FRIENDS = 6;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1082.

```text
1;
  FUNNEL_SIGNUP = 2;
  FUNNEL_GAME_CREATE = 3;
  FUNNEL_GAME_REVIEW = 4;
  FUNNEL_PUZZLES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07539"></a>
## FND-07539: chesscom.proto_options.events.v1.Funnel.FUNNEL_HOME = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_HOME = 7;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1104.

```text
;
  FUNNEL_GAME_CREATE = 3;
  FUNNEL_GAME_REVIEW = 4;
  FUNNEL_PUZZLES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FU
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07540"></a>
## FND-07540: chesscom.proto_options.events.v1.Funnel.FUNNEL_GAME_ARCHIVE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_GAME_ARCHIVE = 8;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1123.

```text
ATE = 3;
  FUNNEL_GAME_REVIEW = 4;
  FUNNEL_PUZZLES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMB
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07541"></a>
## FND-07541: chesscom.proto_options.events.v1.Funnel.FUNNEL_PROFILE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_PROFILE = 9;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1150.

```text
EW = 4;
  FUNNEL_PUZZLES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS 
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07542"></a>
## FND-07542: chesscom.proto_options.events.v1.Funnel.FUNNEL_GAMEPLAY = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_GAMEPLAY = 10;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1172.

```text
ES = 5;
  FUNNEL_FRIENDS = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOA
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07543"></a>
## FND-07543: chesscom.proto_options.events.v1.Funnel.FUNNEL_CRM = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_CRM = 11;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1196.

```text
 = 6;
  FUNNEL_HOME = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUN
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07544"></a>
## FND-07544: chesscom.proto_options.events.v1.Funnel.FUNNEL_PLAY_COACH = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_PLAY_COACH = 12;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1215.

```text
 = 7;
  FUNNEL_GAME_ARCHIVE = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
 
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07545"></a>
## FND-07545: chesscom.proto_options.events.v1.Funnel.FUNNEL_CONTACTS = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_CONTACTS = 13;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1241.

```text
E = 8;
  FUNNEL_PROFILE = 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUN
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07546"></a>
## FND-07546: chesscom.proto_options.events.v1.Funnel.FUNNEL_LESSONS = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_LESSONS = 14;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1265.

```text
= 9;
  FUNNEL_GAMEPLAY = 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNN
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07547"></a>
## FND-07547: chesscom.proto_options.events.v1.Funnel.FUNNEL_COURSES = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_COURSES = 15;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1288.

```text
= 10;
  FUNNEL_CRM = 11;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  F
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07548"></a>
## FND-07548: chesscom.proto_options.events.v1.Funnel.FUNNEL_LOGIN = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_LOGIN = 16;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1311.

```text
;
  FUNNEL_PLAY_COACH = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07549"></a>
## FND-07549: chesscom.proto_options.events.v1.Funnel.FUNNEL_BOTS = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_BOTS = 17;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1332.

```text
 = 12;
  FUNNEL_CONTACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07550"></a>
## FND-07550: chesscom.proto_options.events.v1.Funnel.FUNNEL_PAYMENTS = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_PAYMENTS = 18;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1352.

```text
ACTS = 13;
  FUNNEL_LESSONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07551"></a>
## FND-07551: chesscom.proto_options.events.v1.Funnel.FUNNEL_CHALLENGES = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_CHALLENGES = 19;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1376.

```text
ONS = 14;
  FUNNEL_COURSES = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
 
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07552"></a>
## FND-07552: chesscom.proto_options.events.v1.Funnel.FUNNEL_USER = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_USER = 20;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1402.

```text
 = 15;
  FUNNEL_LOGIN = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNN
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07553"></a>
## FND-07553: chesscom.proto_options.events.v1.Funnel.FUNNEL_ADD_PHONE_NUMBER = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_ADD_PHONE_NUMBER = 21;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1422.

```text
N = 16;
  FUNNEL_BOTS = 17;
  FUNNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07554"></a>
## FND-07554: chesscom.proto_options.events.v1.Funnel.FUNNEL_SETTINGS = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_SETTINGS = 22;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1454.

```text
NNEL_PAYMENTS = 18;
  FUNNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
 
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07555"></a>
## FND-07555: chesscom.proto_options.events.v1.Funnel.FUNNEL_DOWNLOAD_MOBILE_APP = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_DOWNLOAD_MOBILE_APP = 23;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1478.

```text
NNEL_CHALLENGES = 19;
  FUNNEL_USER = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FU
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07556"></a>
## FND-07556: chesscom.proto_options.events.v1.Funnel.FUNNEL_MESSAGE = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_MESSAGE = 24;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1513.

```text
 = 20;
  FUNNEL_ADD_PHONE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZ
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07557"></a>
## FND-07557: chesscom.proto_options.events.v1.Funnel.FUNNEL_SOCIAL = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_SOCIAL = 25;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1536.

```text
NE_NUMBER = 21;
  FUNNEL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNN
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07558"></a>
## FND-07558: chesscom.proto_options.events.v1.Funnel.FUNNEL_STREAKS = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_STREAKS = 26;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1558.

```text
EL_SETTINGS = 22;
  FUNNEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07559"></a>
## FND-07559: chesscom.proto_options.events.v1.Funnel.FUNNEL_ONBOARDING = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_ONBOARDING = 27;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1581.

```text
NEL_DOWNLOAD_MOBILE_APP = 23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07560"></a>
## FND-07560: chesscom.proto_options.events.v1.Funnel.FUNNEL_MONETIZATION = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_MONETIZATION = 28;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1607.

```text
23;
  FUNNEL_MESSAGE = 24;
  FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07561"></a>
## FND-07561: chesscom.proto_options.events.v1.Funnel.FUNNEL_INDEX = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_INDEX = 29;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1635.

```text
 FUNNEL_SOCIAL = 25;
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUN
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07562"></a>
## FND-07562: chesscom.proto_options.events.v1.Funnel.FUNNEL_CHAT = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_CHAT = 30;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1656.

```text
  FUNNEL_STREAKS = 26;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUN
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07563"></a>
## FND-07563: chesscom.proto_options.events.v1.Funnel.FUNNEL_COACH = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_COACH = 31;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1676.

```text
6;
  FUNNEL_ONBOARDING = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07564"></a>
## FND-07564: chesscom.proto_options.events.v1.Funnel.FUNNEL_SHARE = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_SHARE = 32;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1697.

```text
G = 27;
  FUNNEL_MONETIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABL
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07565"></a>
## FND-07565: chesscom.proto_options.events.v1.Funnel.FUNNEL_DAILY_PUZZLE = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_DAILY_PUZZLE = 33;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1718.

```text
TIZATION = 28;
  FUNNEL_INDEX = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANAL
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07566"></a>
## FND-07566: chesscom.proto_options.events.v1.Funnel.FUNNEL_NOTIFICATIONS = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_NOTIFICATIONS = 34;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1746.

```text
X = 29;
  FUNNEL_CHAT = 30;
  FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07567"></a>
## FND-07567: chesscom.proto_options.events.v1.Funnel.FUNNEL_CLUBS = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_CLUBS = 35;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1775.

```text
 FUNNEL_COACH = 31;
  FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKAB
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07568"></a>
## FND-07568: chesscom.proto_options.events.v1.Funnel.FUNNEL_PUZZLE_RUSH = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_PUZZLE_RUSH = 36;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1796.

```text
 FUNNEL_SHARE = 32;
  FUNNEL_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SO
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07569"></a>
## FND-07569: chesscom.proto_options.events.v1.Funnel.FUNNEL_PUZZLE_BATTLE = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_PUZZLE_BATTLE = 37;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1823.

```text
L_DAILY_PUZZLE = 33;
  FUNNEL_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNN
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07570"></a>
## FND-07570: chesscom.proto_options.events.v1.Funnel.FUNNEL_CUSTOM_PUZZLES = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_CUSTOM_PUZZLES = 38;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1852.

```text
_NOTIFICATIONS = 34;
  FUNNEL_CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message Eve
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07571"></a>
## FND-07571: chesscom.proto_options.events.v1.Funnel.FUNNEL_AWARDS = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_AWARDS = 39;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1882.

```text
CLUBS = 35;
  FUNNEL_PUZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07572"></a>
## FND-07572: chesscom.proto_options.events.v1.Funnel.FUNNEL_UNOCKABLES = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_UNOCKABLES = 40;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1904.

```text
UZZLE_RUSH = 36;
  FUNNEL_PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07573"></a>
## FND-07573: chesscom.proto_options.events.v1.Funnel.FUNNEL_EVENTS = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_EVENTS = 41;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1930.

```text
PUZZLE_BATTLE = 37;
  FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  }
  oneof _category {
  .c
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07574"></a>
## FND-07574: chesscom.proto_options.events.v1.Funnel.FUNNEL_STATS = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_STATS = 42;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1952.

```text
FUNNEL_CUSTOM_PUZZLES = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  }
  oneof _category {
  .chesscom.proto_options.
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
