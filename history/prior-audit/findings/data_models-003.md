# data_models — findings 201–300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-00475"></a>
## FND-00475: chesscom.audiences.v1.IsAuthenticatedUserInAudiencesResponse.InAudienceEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0221** `research/proto/chesscom/audiences/v1/authenticated_audiences_service.proto` — [preserved redacted evidence](../evidence/text/c9b124c41ef2a6d8314aad4f81e9517e948b63507a42bd46598ddd8ceb448140.proto)
  Character offset 395.

```text
AuthenticatedUserInAudiencesResponse.InAudienceEntry in_audience = 1;
  message InAudienceEntry {
  optional string key = 1;
  optional bool value = 2;
  }
}

```

**Source references:** SRC-0221, SRC-1192  
**URL references:** None independently associated  
**Related findings:** FND-00470, FND-00471, FND-00472

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00476"></a>
## FND-00476: chesscom.audiences.v1.IsAuthenticatedUserInAudiencesResponse.InAudienceEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool value = 2;

### Evidence

- **SRC-0221** `research/proto/chesscom/audiences/v1/authenticated_audiences_service.proto` — [preserved redacted evidence](../evidence/text/c9b124c41ef2a6d8314aad4f81e9517e948b63507a42bd46598ddd8ceb448140.proto)
  Character offset 422.

```text
sResponse.InAudienceEntry in_audience = 1;
  message InAudienceEntry {
  optional string key = 1;
  optional bool value = 2;
  }
}

```

**Source references:** SRC-0221, SRC-1192  
**URL references:** None independently associated  
**Related findings:** FND-00470, FND-00471, FND-00472

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00477"></a>
## FND-00477: enum declaration: chesscom.audit_logs.v1.FieldSensitivity

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum FieldSensitivity {

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 106.

```text
rce: chesscom/audit_logs/v1/audit_options.proto
// syntax: proto3

package chesscom.audit_logs.v1;

enum FieldSensitivity {
  FIELD_SENSITIVITY_UNSPECIFIED = 0;
  FIELD_SENSITIVITY_DEFAULT = 1;
  FIELD_SENSITIVITY_ADVANCED = 2;
  FIELD_SENSITIVITY_RESTRICTED = 3;
}

enum MessageSensitivity {
  MESSAGE_SENSITIVITY_UNSPECIFIED = 0;
  MESSAGE_SENSITIVITY_DEFAULT = 1;
  MESSAGE_SENSITIVITY_RESTRICTED = 2;
}

message Audi
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00478, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00478"></a>
## FND-00478: chesscom.audit_logs.v1.FieldSensitivity.FIELD_SENSITIVITY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FIELD_SENSITIVITY_UNSPECIFIED = 0;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 132.

```text
1/audit_options.proto
// syntax: proto3

package chesscom.audit_logs.v1;

enum FieldSensitivity {
  FIELD_SENSITIVITY_UNSPECIFIED = 0;
  FIELD_SENSITIVITY_DEFAULT = 1;
  FIELD_SENSITIVITY_ADVANCED = 2;
  FIELD_SENSITIVITY_RESTRICTED = 3;
}

enum MessageSensitivity {
  MESSAGE_SENSITIVITY_UNSPECIFIED = 0;
  MESSAGE_SENSITIVITY_DEFAULT = 1;
  MESSAGE_SENSITIVITY_RESTRICTED = 2;
}

message AuditFieldOptions {
  oneof _i
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00479"></a>
## FND-00479: chesscom.audit_logs.v1.FieldSensitivity.FIELD_SENSITIVITY_DEFAULT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FIELD_SENSITIVITY_DEFAULT = 1;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 169.

```text
o3

package chesscom.audit_logs.v1;

enum FieldSensitivity {
  FIELD_SENSITIVITY_UNSPECIFIED = 0;
  FIELD_SENSITIVITY_DEFAULT = 1;
  FIELD_SENSITIVITY_ADVANCED = 2;
  FIELD_SENSITIVITY_RESTRICTED = 3;
}

enum MessageSensitivity {
  MESSAGE_SENSITIVITY_UNSPECIFIED = 0;
  MESSAGE_SENSITIVITY_DEFAULT = 1;
  MESSAGE_SENSITIVITY_RESTRICTED = 2;
}

message AuditFieldOptions {
  oneof _indexed {
  bool indexed = 4;
  }
  on
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00480"></a>
## FND-00480: chesscom.audit_logs.v1.FieldSensitivity.FIELD_SENSITIVITY_ADVANCED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FIELD_SENSITIVITY_ADVANCED = 2;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 202.

```text
1;

enum FieldSensitivity {
  FIELD_SENSITIVITY_UNSPECIFIED = 0;
  FIELD_SENSITIVITY_DEFAULT = 1;
  FIELD_SENSITIVITY_ADVANCED = 2;
  FIELD_SENSITIVITY_RESTRICTED = 3;
}

enum MessageSensitivity {
  MESSAGE_SENSITIVITY_UNSPECIFIED = 0;
  MESSAGE_SENSITIVITY_DEFAULT = 1;
  MESSAGE_SENSITIVITY_RESTRICTED = 2;
}

message AuditFieldOptions {
  oneof _indexed {
  bool indexed = 4;
  }
  oneof _index_alias {
  string index
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00481"></a>
## FND-00481: chesscom.audit_logs.v1.FieldSensitivity.FIELD_SENSITIVITY_RESTRICTED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FIELD_SENSITIVITY_RESTRICTED = 3;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 236.

```text
D_SENSITIVITY_UNSPECIFIED = 0;
  FIELD_SENSITIVITY_DEFAULT = 1;
  FIELD_SENSITIVITY_ADVANCED = 2;
  FIELD_SENSITIVITY_RESTRICTED = 3;
}

enum MessageSensitivity {
  MESSAGE_SENSITIVITY_UNSPECIFIED = 0;
  MESSAGE_SENSITIVITY_DEFAULT = 1;
  MESSAGE_SENSITIVITY_RESTRICTED = 2;
}

message AuditFieldOptions {
  oneof _indexed {
  bool indexed = 4;
  }
  oneof _index_alias {
  string index_alias = 5;
  }
  optional .chessc
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00482"></a>
## FND-00482: enum declaration: chesscom.audit_logs.v1.MessageSensitivity

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MessageSensitivity {

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 273.

```text
D_SENSITIVITY_DEFAULT = 1;
  FIELD_SENSITIVITY_ADVANCED = 2;
  FIELD_SENSITIVITY_RESTRICTED = 3;
}

enum MessageSensitivity {
  MESSAGE_SENSITIVITY_UNSPECIFIED = 0;
  MESSAGE_SENSITIVITY_DEFAULT = 1;
  MESSAGE_SENSITIVITY_RESTRICTED = 2;
}

message AuditFieldOptions {
  oneof _indexed {
  bool indexed = 4;
  }
  oneof _index_alias {
  string index_alias = 5;
  }
  optional .chesscom.audit_logs.v1.FieldSensitivity fie
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00483"></a>
## FND-00483: chesscom.audit_logs.v1.MessageSensitivity.MESSAGE_SENSITIVITY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MESSAGE_SENSITIVITY_UNSPECIFIED = 0;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 301.

```text
 FIELD_SENSITIVITY_ADVANCED = 2;
  FIELD_SENSITIVITY_RESTRICTED = 3;
}

enum MessageSensitivity {
  MESSAGE_SENSITIVITY_UNSPECIFIED = 0;
  MESSAGE_SENSITIVITY_DEFAULT = 1;
  MESSAGE_SENSITIVITY_RESTRICTED = 2;
}

message AuditFieldOptions {
  oneof _indexed {
  bool indexed = 4;
  }
  oneof _index_alias {
  string index_alias = 5;
  }
  optional .chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;
  option
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00484"></a>
## FND-00484: chesscom.audit_logs.v1.MessageSensitivity.MESSAGE_SENSITIVITY_DEFAULT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MESSAGE_SENSITIVITY_DEFAULT = 1;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 340.

```text
D_SENSITIVITY_RESTRICTED = 3;
}

enum MessageSensitivity {
  MESSAGE_SENSITIVITY_UNSPECIFIED = 0;
  MESSAGE_SENSITIVITY_DEFAULT = 1;
  MESSAGE_SENSITIVITY_RESTRICTED = 2;
}

message AuditFieldOptions {
  oneof _indexed {
  bool indexed = 4;
  }
  oneof _index_alias {
  string index_alias = 5;
  }
  optional .chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;
  optional string description = 2;
  repeated s
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00485"></a>
## FND-00485: chesscom.audit_logs.v1.MessageSensitivity.MESSAGE_SENSITIVITY_RESTRICTED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MESSAGE_SENSITIVITY_RESTRICTED = 2;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 375.

```text
um MessageSensitivity {
  MESSAGE_SENSITIVITY_UNSPECIFIED = 0;
  MESSAGE_SENSITIVITY_DEFAULT = 1;
  MESSAGE_SENSITIVITY_RESTRICTED = 2;
}

message AuditFieldOptions {
  oneof _indexed {
  bool indexed = 4;
  }
  oneof _index_alias {
  string index_alias = 5;
  }
  optional .chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}


```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00486"></a>
## FND-00486: message declaration: chesscom.audit_logs.v1.AuditFieldOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AuditFieldOptions {

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 414.

```text
TIVITY_UNSPECIFIED = 0;
  MESSAGE_SENSITIVITY_DEFAULT = 1;
  MESSAGE_SENSITIVITY_RESTRICTED = 2;
}

message AuditFieldOptions {
  oneof _indexed {
  bool indexed = 4;
  }
  oneof _index_alias {
  string index_alias = 5;
  }
  optional .chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMessageOptions {
  optiona
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00487"></a>
## FND-00487: oneof declaration: chesscom.audit_logs.v1.AuditFieldOptions._indexed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _indexed {

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 444.

```text
AGE_SENSITIVITY_DEFAULT = 1;
  MESSAGE_SENSITIVITY_RESTRICTED = 2;
}

message AuditFieldOptions {
  oneof _indexed {
  bool indexed = 4;
  }
  oneof _index_alias {
  string index_alias = 5;
  }
  optional .chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMessageOptions {
  optional .chesscom.audit_logs.v1.Mess
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00488"></a>
## FND-00488: chesscom.audit_logs.v1.AuditFieldOptions.indexed = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool indexed = 4;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 463.

```text
AULT = 1;
  MESSAGE_SENSITIVITY_RESTRICTED = 2;
}

message AuditFieldOptions {
  oneof _indexed {
  bool indexed = 4;
  }
  oneof _index_alias {
  string index_alias = 5;
  }
  optional .chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMessageOptions {
  optional .chesscom.audit_logs.v1.MessageSensitivity mess
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00489"></a>
## FND-00489: oneof declaration: chesscom.audit_logs.v1.AuditFieldOptions._index_alias

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _index_alias {

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 487.

```text
ITIVITY_RESTRICTED = 2;
}

message AuditFieldOptions {
  oneof _indexed {
  bool indexed = 4;
  }
  oneof _index_alias {
  string index_alias = 5;
  }
  optional .chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMessageOptions {
  optional .chesscom.audit_logs.v1.MessageSensitivity message_sensitivity = 1;
  o
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00490"></a>
## FND-00490: chesscom.audit_logs.v1.AuditFieldOptions.index_alias = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string index_alias = 5;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 510.

```text

}

message AuditFieldOptions {
  oneof _indexed {
  bool indexed = 4;
  }
  oneof _index_alias {
  string index_alias = 5;
  }
  optional .chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMessageOptions {
  optional .chesscom.audit_logs.v1.MessageSensitivity message_sensitivity = 1;
  optional string descript
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00491"></a>
## FND-00491: chesscom.audit_logs.v1.AuditFieldOptions.field_sensitivity = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 540.

```text
{
  oneof _indexed {
  bool indexed = 4;
  }
  oneof _index_alias {
  string index_alias = 5;
  }
  optional .chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMessageOptions {
  optional .chesscom.audit_logs.v1.MessageSensitivity message_sensitivity = 1;
  optional string description = 2;
  repeated string req
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00492"></a>
## FND-00492: chesscom.audit_logs.v1.AuditFieldOptions.description = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string description = 2;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 615.

```text
g index_alias = 5;
  }
  optional .chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMessageOptions {
  optional .chesscom.audit_logs.v1.MessageSensitivity message_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMethodOptions {
  oneof _log_errors 
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00493"></a>
## FND-00493: chesscom.audit_logs.v1.AuditFieldOptions.required_permissions = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string required_permissions = 3;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 650.

```text
chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMessageOptions {
  optional .chesscom.audit_logs.v1.MessageSensitivity message_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMethodOptions {
  oneof _log_errors {
  bool log_errors = 6;
  }
  oneo
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00494"></a>
## FND-00494: message declaration: chesscom.audit_logs.v1.AuditMessageOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AuditMessageOptions {

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 695.

```text
_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMessageOptions {
  optional .chesscom.audit_logs.v1.MessageSensitivity message_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMethodOptions {
  oneof _log_errors {
  bool log_errors = 6;
  }
  oneof _log_response {
  bool log_response = 7;
  
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00495"></a>
## FND-00495: chesscom.audit_logs.v1.AuditMessageOptions.message_sensitivity = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.audit_logs.v1.MessageSensitivity message_sensitivity = 1;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 727.

```text
ing description = 2;
  repeated string required_permissions = 3;
}

message AuditMessageOptions {
  optional .chesscom.audit_logs.v1.MessageSensitivity message_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMethodOptions {
  oneof _log_errors {
  bool log_errors = 6;
  }
  oneof _log_response {
  bool log_response = 7;
  }
  optional string action_name 
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00496"></a>
## FND-00496: chesscom.audit_logs.v1.AuditMessageOptions.description = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string description = 2;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 615.

```text
g index_alias = 5;
  }
  optional .chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMessageOptions {
  optional .chesscom.audit_logs.v1.MessageSensitivity message_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMethodOptions {
  oneof _log_errors 
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00497"></a>
## FND-00497: chesscom.audit_logs.v1.AuditMessageOptions.required_permissions = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string required_permissions = 3;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 650.

```text
chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMessageOptions {
  optional .chesscom.audit_logs.v1.MessageSensitivity message_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMethodOptions {
  oneof _log_errors {
  bool log_errors = 6;
  }
  oneo
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00498"></a>
## FND-00498: message declaration: chesscom.audit_logs.v1.AuditMethodOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AuditMethodOptions {

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 886.

```text
_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMethodOptions {
  oneof _log_errors {
  bool log_errors = 6;
  }
  oneof _log_response {
  bool log_response = 7;
  }
  optional string action_name = 1;
  optional .chesscom.audit_logs.v1.MessageSensitivity sensitivity = 2;
  repeated string required_permissions = 3;
  optional string request_reference_id_
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00499"></a>
## FND-00499: oneof declaration: chesscom.audit_logs.v1.AuditMethodOptions._log_errors

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _log_errors {

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 917.

```text
ring description = 2;
  repeated string required_permissions = 3;
}

message AuditMethodOptions {
  oneof _log_errors {
  bool log_errors = 6;
  }
  oneof _log_response {
  bool log_response = 7;
  }
  optional string action_name = 1;
  optional .chesscom.audit_logs.v1.MessageSensitivity sensitivity = 2;
  repeated string required_permissions = 3;
  optional string request_reference_id_field = 4;
  optional string re
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00500"></a>
## FND-00500: chesscom.audit_logs.v1.AuditMethodOptions.log_errors = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool log_errors = 6;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 939.

```text
  repeated string required_permissions = 3;
}

message AuditMethodOptions {
  oneof _log_errors {
  bool log_errors = 6;
  }
  oneof _log_response {
  bool log_response = 7;
  }
  optional string action_name = 1;
  optional .chesscom.audit_logs.v1.MessageSensitivity sensitivity = 2;
  repeated string required_permissions = 3;
  optional string request_reference_id_field = 4;
  optional string response_reference_id_fi
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00501"></a>
## FND-00501: oneof declaration: chesscom.audit_logs.v1.AuditMethodOptions._log_response

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _log_response {

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 966.

```text
permissions = 3;
}

message AuditMethodOptions {
  oneof _log_errors {
  bool log_errors = 6;
  }
  oneof _log_response {
  bool log_response = 7;
  }
  optional string action_name = 1;
  optional .chesscom.audit_logs.v1.MessageSensitivity sensitivity = 2;
  repeated string required_permissions = 3;
  optional string request_reference_id_field = 4;
  optional string response_reference_id_field = 5;
}

```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00502"></a>
## FND-00502: chesscom.audit_logs.v1.AuditMethodOptions.log_response = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool log_response = 7;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 990.

```text
age AuditMethodOptions {
  oneof _log_errors {
  bool log_errors = 6;
  }
  oneof _log_response {
  bool log_response = 7;
  }
  optional string action_name = 1;
  optional .chesscom.audit_logs.v1.MessageSensitivity sensitivity = 2;
  repeated string required_permissions = 3;
  optional string request_reference_id_field = 4;
  optional string response_reference_id_field = 5;
}

```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00503"></a>
## FND-00503: chesscom.audit_logs.v1.AuditMethodOptions.action_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string action_name = 1;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 1019.

```text
eof _log_errors {
  bool log_errors = 6;
  }
  oneof _log_response {
  bool log_response = 7;
  }
  optional string action_name = 1;
  optional .chesscom.audit_logs.v1.MessageSensitivity sensitivity = 2;
  repeated string required_permissions = 3;
  optional string request_reference_id_field = 4;
  optional string response_reference_id_field = 5;
}

```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00504"></a>
## FND-00504: chesscom.audit_logs.v1.AuditMethodOptions.sensitivity = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.audit_logs.v1.MessageSensitivity sensitivity = 2;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 1054.

```text
 = 6;
  }
  oneof _log_response {
  bool log_response = 7;
  }
  optional string action_name = 1;
  optional .chesscom.audit_logs.v1.MessageSensitivity sensitivity = 2;
  repeated string required_permissions = 3;
  optional string request_reference_id_field = 4;
  optional string response_reference_id_field = 5;
}

```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00505"></a>
## FND-00505: chesscom.audit_logs.v1.AuditMethodOptions.required_permissions = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string required_permissions = 3;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 650.

```text
chesscom.audit_logs.v1.FieldSensitivity field_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMessageOptions {
  optional .chesscom.audit_logs.v1.MessageSensitivity message_sensitivity = 1;
  optional string description = 2;
  repeated string required_permissions = 3;
}

message AuditMethodOptions {
  oneof _log_errors {
  bool log_errors = 6;
  }
  oneo
```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00506"></a>
## FND-00506: chesscom.audit_logs.v1.AuditMethodOptions.request_reference_id_field = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string request_reference_id_field = 4;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 1169.

```text
com.audit_logs.v1.MessageSensitivity sensitivity = 2;
  repeated string required_permissions = 3;
  optional string request_reference_id_field = 4;
  optional string response_reference_id_field = 5;
}

```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00507"></a>
## FND-00507: chesscom.audit_logs.v1.AuditMethodOptions.response_reference_id_field = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string response_reference_id_field = 5;

### Evidence

- **SRC-0222** `research/proto/chesscom/audit_logs/v1/audit_options.proto` — [preserved redacted evidence](../evidence/text/9eb8f97c1cb837d95394c70b62684e9a3cf5878fe95701197be584199eda29cf.proto)
  Character offset 1219.

```text
 2;
  repeated string required_permissions = 3;
  optional string request_reference_id_field = 4;
  optional string response_reference_id_field = 5;
}

```

**Source references:** SRC-0222, SRC-1193  
**URL references:** None independently associated  
**Related findings:** FND-00477, FND-00478, FND-00479

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00508"></a>
## FND-00508: enum declaration: chesscom.bots.v1.BotLabelType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum BotLabelType {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 90.

```text
// source: chesscom/bots/v1/bot_event.proto
// syntax: proto3

package chesscom.bots.v1;

enum BotLabelType {
  BOT_LABEL_TYPE_UNSPECIFIED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEvent {
  oneof _premium_multiplier {
  uint32 premium_multiplier = 12;
  }
  oneof _game_review_data {
  .chesscom.bots.v1.GameReviewEventData game_review_data = 13;
  }
  optional string name 
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00509"></a>
## FND-00509: chesscom.bots.v1.BotLabelType.BOT_LABEL_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_LABEL_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 112.

```text
hesscom/bots/v1/bot_event.proto
// syntax: proto3

package chesscom.bots.v1;

enum BotLabelType {
  BOT_LABEL_TYPE_UNSPECIFIED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEvent {
  oneof _premium_multiplier {
  uint32 premium_multiplier = 12;
  }
  oneof _game_review_data {
  .chesscom.bots.v1.GameReviewEventData game_review_data = 13;
  }
  optional string name = 1;
  optional string
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00510"></a>
## FND-00510: chesscom.bots.v1.BotLabelType.BOT_LABEL_TYPE_HARDER = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_LABEL_TYPE_HARDER = 1;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 146.

```text
 syntax: proto3

package chesscom.bots.v1;

enum BotLabelType {
  BOT_LABEL_TYPE_UNSPECIFIED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEvent {
  oneof _premium_multiplier {
  uint32 premium_multiplier = 12;
  }
  oneof _game_review_data {
  .chesscom.bots.v1.GameReviewEventData game_review_data = 13;
  }
  optional string name = 1;
  optional string description = 2;
  optional .ches
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00511"></a>
## FND-00511: chesscom.bots.v1.BotLabelType.BOT_LABEL_TYPE_EASIER = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_LABEL_TYPE_EASIER = 2;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 175.

```text
scom.bots.v1;

enum BotLabelType {
  BOT_LABEL_TYPE_UNSPECIFIED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEvent {
  oneof _premium_multiplier {
  uint32 premium_multiplier = 12;
  }
  oneof _game_review_data {
  .chesscom.bots.v1.GameReviewEventData game_review_data = 13;
  }
  optional string name = 1;
  optional string description = 2;
  optional .chesscom.bots.v1.BotEventTheme th
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00512"></a>
## FND-00512: message declaration: chesscom.bots.v1.BotEvent

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotEvent {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 205.

```text
pe {
  BOT_LABEL_TYPE_UNSPECIFIED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEvent {
  oneof _premium_multiplier {
  uint32 premium_multiplier = 12;
  }
  oneof _game_review_data {
  .chesscom.bots.v1.GameReviewEventData game_review_data = 13;
  }
  optional string name = 1;
  optional string description = 2;
  optional .chesscom.bots.v1.BotEventTheme theme = 3;
  optional .chesscom.
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00513"></a>
## FND-00513: oneof declaration: chesscom.bots.v1.BotEvent._premium_multiplier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _premium_multiplier {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 226.

```text
_UNSPECIFIED = 0;
  BOT_LABEL_TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEvent {
  oneof _premium_multiplier {
  uint32 premium_multiplier = 12;
  }
  oneof _game_review_data {
  .chesscom.bots.v1.GameReviewEventData game_review_data = 13;
  }
  optional string name = 1;
  optional string description = 2;
  optional .chesscom.bots.v1.BotEventTheme theme = 3;
  optional .chesscom.progression.v1.EventP
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00514"></a>
## FND-00514: chesscom.bots.v1.BotEvent.premium_multiplier = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 premium_multiplier = 12;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 256.

```text
TYPE_HARDER = 1;
  BOT_LABEL_TYPE_EASIER = 2;
}

message BotEvent {
  oneof _premium_multiplier {
  uint32 premium_multiplier = 12;
  }
  oneof _game_review_data {
  .chesscom.bots.v1.GameReviewEventData game_review_data = 13;
  }
  optional string name = 1;
  optional string description = 2;
  optional .chesscom.bots.v1.BotEventTheme theme = 3;
  optional .chesscom.progression.v1.EventProgress progress = 4;
  option
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00515"></a>
## FND-00515: oneof declaration: chesscom.bots.v1.BotEvent._game_review_data

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_review_data {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 294.

```text
ER = 2;
}

message BotEvent {
  oneof _premium_multiplier {
  uint32 premium_multiplier = 12;
  }
  oneof _game_review_data {
  .chesscom.bots.v1.GameReviewEventData game_review_data = 13;
  }
  optional string name = 1;
  optional string description = 2;
  optional .chesscom.bots.v1.BotEventTheme theme = 3;
  optional .chesscom.progression.v1.EventProgress progress = 4;
  optional string progress_unit_name = 5;
  op
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00516"></a>
## FND-00516: chesscom.bots.v1.BotEvent.game_review_data = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.bots.v1.GameReviewEventData game_review_data = 13;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 322.

```text
{
  oneof _premium_multiplier {
  uint32 premium_multiplier = 12;
  }
  oneof _game_review_data {
  .chesscom.bots.v1.GameReviewEventData game_review_data = 13;
  }
  optional string name = 1;
  optional string description = 2;
  optional .chesscom.bots.v1.BotEventTheme theme = 3;
  optional .chesscom.progression.v1.EventProgress progress = 4;
  optional string progress_unit_name = 5;
  optional .google.protobuf.Time
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00517"></a>
## FND-00517: chesscom.bots.v1.BotEvent.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 389.

```text
 }
  oneof _game_review_data {
  .chesscom.bots.v1.GameReviewEventData game_review_data = 13;
  }
  optional string name = 1;
  optional string description = 2;
  optional .chesscom.bots.v1.BotEventTheme theme = 3;
  optional .chesscom.progression.v1.EventProgress progress = 4;
  optional string progress_unit_name = 5;
  optional .google.protobuf.Timestamp end_time = 6;
  optional string bot_event_key = 7;
  optional
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00518"></a>
## FND-00518: chesscom.bots.v1.BotEvent.description = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string description = 2;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 417.

```text
 {
  .chesscom.bots.v1.GameReviewEventData game_review_data = 13;
  }
  optional string name = 1;
  optional string description = 2;
  optional .chesscom.bots.v1.BotEventTheme theme = 3;
  optional .chesscom.progression.v1.EventProgress progress = 4;
  optional string progress_unit_name = 5;
  optional .google.protobuf.Timestamp end_time = 6;
  optional string bot_event_key = 7;
  optional .chesscom.bots.v1.BotVariat
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00519"></a>
## FND-00519: chesscom.bots.v1.BotEvent.theme = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.bots.v1.BotEventTheme theme = 3;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 452.

```text
entData game_review_data = 13;
  }
  optional string name = 1;
  optional string description = 2;
  optional .chesscom.bots.v1.BotEventTheme theme = 3;
  optional .chesscom.progression.v1.EventProgress progress = 4;
  optional string progress_unit_name = 5;
  optional .google.protobuf.Timestamp end_time = 6;
  optional string bot_event_key = 7;
  optional .chesscom.bots.v1.BotVariationModalData variation_modal_data =
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00520"></a>
## FND-00520: chesscom.bots.v1.BotEvent.progress = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.progression.v1.EventProgress progress = 4;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 506.

```text
ame = 1;
  optional string description = 2;
  optional .chesscom.bots.v1.BotEventTheme theme = 3;
  optional .chesscom.progression.v1.EventProgress progress = 4;
  optional string progress_unit_name = 5;
  optional .google.protobuf.Timestamp end_time = 6;
  optional string bot_event_key = 7;
  optional .chesscom.bots.v1.BotVariationModalData variation_modal_data = 8;
  repeated .chesscom.progression.v1.EventUnlockabl
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00521"></a>
## FND-00521: chesscom.bots.v1.BotEvent.progress_unit_name = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string progress_unit_name = 5;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 570.

```text
.bots.v1.BotEventTheme theme = 3;
  optional .chesscom.progression.v1.EventProgress progress = 4;
  optional string progress_unit_name = 5;
  optional .google.protobuf.Timestamp end_time = 6;
  optional string bot_event_key = 7;
  optional .chesscom.bots.v1.BotVariationModalData variation_modal_data = 8;
  repeated .chesscom.progression.v1.EventUnlockable unlockables = 9;
  optional uint32 resign_min_plies = 10;
  op
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00522"></a>
## FND-00522: chesscom.bots.v1.BotEvent.end_time = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp end_time = 6;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 612.

```text
al .chesscom.progression.v1.EventProgress progress = 4;
  optional string progress_unit_name = 5;
  optional .google.protobuf.Timestamp end_time = 6;
  optional string bot_event_key = 7;
  optional .chesscom.bots.v1.BotVariationModalData variation_modal_data = 8;
  repeated .chesscom.progression.v1.EventUnlockable unlockables = 9;
  optional uint32 resign_min_plies = 10;
  optional .chesscom.bots.v1.BotEventIntroModa
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00523"></a>
## FND-00523: chesscom.bots.v1.BotEvent.bot_event_key = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string bot_event_key = 7;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 664.

```text
 4;
  optional string progress_unit_name = 5;
  optional .google.protobuf.Timestamp end_time = 6;
  optional string bot_event_key = 7;
  optional .chesscom.bots.v1.BotVariationModalData variation_modal_data = 8;
  repeated .chesscom.progression.v1.EventUnlockable unlockables = 9;
  optional uint32 resign_min_plies = 10;
  optional .chesscom.bots.v1.BotEventIntroModalData intro_modal_data = 11;
}

message GameReviewEv
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00524"></a>
## FND-00524: chesscom.bots.v1.BotEvent.variation_modal_data = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.bots.v1.BotVariationModalData variation_modal_data = 8;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 701.

```text
ame = 5;
  optional .google.protobuf.Timestamp end_time = 6;
  optional string bot_event_key = 7;
  optional .chesscom.bots.v1.BotVariationModalData variation_modal_data = 8;
  repeated .chesscom.progression.v1.EventUnlockable unlockables = 9;
  optional uint32 resign_min_plies = 10;
  optional .chesscom.bots.v1.BotEventIntroModalData intro_modal_data = 11;
}

message GameReviewEventData {
  optional uint32 points = 
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00525"></a>
## FND-00525: chesscom.bots.v1.BotEvent.unlockables = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.progression.v1.EventUnlockable unlockables = 9;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 778.

```text
g bot_event_key = 7;
  optional .chesscom.bots.v1.BotVariationModalData variation_modal_data = 8;
  repeated .chesscom.progression.v1.EventUnlockable unlockables = 9;
  optional uint32 resign_min_plies = 10;
  optional .chesscom.bots.v1.BotEventIntroModalData intro_modal_data = 11;
}

message GameReviewEventData {
  optional uint32 points = 1;
  optional .chesscom.api.v1.Asset points_icon = 2;
}

message BotPropertie
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00526"></a>
## FND-00526: chesscom.bots.v1.BotEvent.resign_min_plies = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 resign_min_plies = 10;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 847.

```text
ta variation_modal_data = 8;
  repeated .chesscom.progression.v1.EventUnlockable unlockables = 9;
  optional uint32 resign_min_plies = 10;
  optional .chesscom.bots.v1.BotEventIntroModalData intro_modal_data = 11;
}

message GameReviewEventData {
  optional uint32 points = 1;
  optional .chesscom.api.v1.Asset points_icon = 2;
}

message BotProperties {
  oneof _fen {
  string fen = 5;
  }
  oneof _play_as_white {
  b
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00527"></a>
## FND-00527: chesscom.bots.v1.BotEvent.intro_modal_data = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.bots.v1.BotEventIntroModalData intro_modal_data = 11;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 888.

```text
chesscom.progression.v1.EventUnlockable unlockables = 9;
  optional uint32 resign_min_plies = 10;
  optional .chesscom.bots.v1.BotEventIntroModalData intro_modal_data = 11;
}

message GameReviewEventData {
  optional uint32 points = 1;
  optional .chesscom.api.v1.Asset points_icon = 2;
}

message BotProperties {
  oneof _fen {
  string fen = 5;
  }
  oneof _play_as_white {
  bool play_as_white = 6;
  }
  oneof _label
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00528"></a>
## FND-00528: message declaration: chesscom.bots.v1.GameReviewEventData

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewEventData {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 964.

```text
esign_min_plies = 10;
  optional .chesscom.bots.v1.BotEventIntroModalData intro_modal_data = 11;
}

message GameReviewEventData {
  optional uint32 points = 1;
  optional .chesscom.api.v1.Asset points_icon = 2;
}

message BotProperties {
  oneof _fen {
  string fen = 5;
  }
  oneof _play_as_white {
  bool play_as_white = 6;
  }
  oneof _label {
  .chesscom.bots.v1.BotLabel label = 7;
  }
  oneof _komodo_skill_overrid
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00529"></a>
## FND-00529: chesscom.bots.v1.GameReviewEventData.points = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 points = 1;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 996.

```text
 .chesscom.bots.v1.BotEventIntroModalData intro_modal_data = 11;
}

message GameReviewEventData {
  optional uint32 points = 1;
  optional .chesscom.api.v1.Asset points_icon = 2;
}

message BotProperties {
  oneof _fen {
  string fen = 5;
  }
  oneof _play_as_white {
  bool play_as_white = 6;
  }
  oneof _label {
  .chesscom.bots.v1.BotLabel label = 7;
  }
  oneof _komodo_skill_override {
  uint32 komodo_skill_overri
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00530"></a>
## FND-00530: chesscom.bots.v1.GameReviewEventData.points_icon = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Asset points_icon = 2;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1026.

```text
roModalData intro_modal_data = 11;
}

message GameReviewEventData {
  optional uint32 points = 1;
  optional .chesscom.api.v1.Asset points_icon = 2;
}

message BotProperties {
  oneof _fen {
  string fen = 5;
  }
  oneof _play_as_white {
  bool play_as_white = 6;
  }
  oneof _label {
  .chesscom.bots.v1.BotLabel label = 7;
  }
  oneof _komodo_skill_override {
  uint32 komodo_skill_override = 8;
  }
  oneof _fen_playe
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00531"></a>
## FND-00531: message declaration: chesscom.bots.v1.BotProperties

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotProperties {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1078.

```text
viewEventData {
  optional uint32 points = 1;
  optional .chesscom.api.v1.Asset points_icon = 2;
}

message BotProperties {
  oneof _fen {
  string fen = 5;
  }
  oneof _play_as_white {
  bool play_as_white = 6;
  }
  oneof _label {
  .chesscom.bots.v1.BotLabel label = 7;
  }
  oneof _komodo_skill_override {
  uint32 komodo_skill_override = 8;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 9;
  }
 
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00532"></a>
## FND-00532: oneof declaration: chesscom.bots.v1.BotProperties._fen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _fen {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1104.

```text
 uint32 points = 1;
  optional .chesscom.api.v1.Asset points_icon = 2;
}

message BotProperties {
  oneof _fen {
  string fen = 5;
  }
  oneof _play_as_white {
  bool play_as_white = 6;
  }
  oneof _label {
  .chesscom.bots.v1.BotLabel label = 7;
  }
  oneof _komodo_skill_override {
  uint32 komodo_skill_override = 8;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 9;
  }
  oneof _fen_player_is_blac
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00533"></a>
## FND-00533: chesscom.bots.v1.BotProperties.fen = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string fen = 5;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1119.

```text
= 1;
  optional .chesscom.api.v1.Asset points_icon = 2;
}

message BotProperties {
  oneof _fen {
  string fen = 5;
  }
  oneof _play_as_white {
  bool play_as_white = 6;
  }
  oneof _label {
  .chesscom.bots.v1.BotLabel label = 7;
  }
  oneof _komodo_skill_override {
  uint32 komodo_skill_override = 8;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 9;
  }
  oneof _fen_player_is_black {
  string fe
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00534"></a>
## FND-00534: oneof declaration: chesscom.bots.v1.BotProperties._play_as_white

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_as_white {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1141.

```text
com.api.v1.Asset points_icon = 2;
}

message BotProperties {
  oneof _fen {
  string fen = 5;
  }
  oneof _play_as_white {
  bool play_as_white = 6;
  }
  oneof _label {
  .chesscom.bots.v1.BotLabel label = 7;
  }
  oneof _komodo_skill_override {
  uint32 komodo_skill_override = 8;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 9;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 10
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00535"></a>
## FND-00535: chesscom.bots.v1.BotProperties.play_as_white = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool play_as_white = 6;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1166.

```text
con = 2;
}

message BotProperties {
  oneof _fen {
  string fen = 5;
  }
  oneof _play_as_white {
  bool play_as_white = 6;
  }
  oneof _label {
  .chesscom.bots.v1.BotLabel label = 7;
  }
  oneof _komodo_skill_override {
  uint32 komodo_skill_override = 8;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 9;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 10;
  }
  optional uint32 w
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00536"></a>
## FND-00536: oneof declaration: chesscom.bots.v1.BotProperties._label

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _label {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1196.

```text
ies {
  oneof _fen {
  string fen = 5;
  }
  oneof _play_as_white {
  bool play_as_white = 6;
  }
  oneof _label {
  .chesscom.bots.v1.BotLabel label = 7;
  }
  oneof _komodo_skill_override {
  uint32 komodo_skill_override = 8;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 9;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 10;
  }
  optional uint32 win_points = 1;
  optional uint
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00537"></a>
## FND-00537: chesscom.bots.v1.BotProperties.label = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.bots.v1.BotLabel label = 7;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1213.

```text
n {
  string fen = 5;
  }
  oneof _play_as_white {
  bool play_as_white = 6;
  }
  oneof _label {
  .chesscom.bots.v1.BotLabel label = 7;
  }
  oneof _komodo_skill_override {
  uint32 komodo_skill_override = 8;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 9;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 10;
  }
  optional uint32 win_points = 1;
  optional uint32 loss_points = 
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00538"></a>
## FND-00538: oneof declaration: chesscom.bots.v1.BotProperties._komodo_skill_override

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _komodo_skill_override {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1257.

```text
hite {
  bool play_as_white = 6;
  }
  oneof _label {
  .chesscom.bots.v1.BotLabel label = 7;
  }
  oneof _komodo_skill_override {
  uint32 komodo_skill_override = 8;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 9;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 10;
  }
  optional uint32 win_points = 1;
  optional uint32 loss_points = 2;
  optional uint32 draw_points = 3;
  opti
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00539"></a>
## FND-00539: chesscom.bots.v1.BotProperties.komodo_skill_override = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 komodo_skill_override = 8;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1290.

```text
  }
  oneof _label {
  .chesscom.bots.v1.BotLabel label = 7;
  }
  oneof _komodo_skill_override {
  uint32 komodo_skill_override = 8;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 9;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 10;
  }
  optional uint32 win_points = 1;
  optional uint32 loss_points = 2;
  optional uint32 draw_points = 3;
  optional bool assistance_use_penalty 
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00540"></a>
## FND-00540: oneof declaration: chesscom.bots.v1.BotProperties._fen_player_is_white

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _fen_player_is_white {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1330.

```text
.BotLabel label = 7;
  }
  oneof _komodo_skill_override {
  uint32 komodo_skill_override = 8;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 9;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 10;
  }
  optional uint32 win_points = 1;
  optional uint32 loss_points = 2;
  optional uint32 draw_points = 3;
  optional bool assistance_use_penalty = 4;
}

message BotLabel {
  optional .c
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00541"></a>
## FND-00541: chesscom.bots.v1.BotProperties.fen_player_is_white = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string fen_player_is_white = 9;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1361.

```text
f _komodo_skill_override {
  uint32 komodo_skill_override = 8;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 9;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 10;
  }
  optional uint32 win_points = 1;
  optional uint32 loss_points = 2;
  optional uint32 draw_points = 3;
  optional bool assistance_use_penalty = 4;
}

message BotLabel {
  optional .chesscom.bots.v1.BotLabelType ty
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00542"></a>
## FND-00542: oneof declaration: chesscom.bots.v1.BotProperties._fen_player_is_black

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _fen_player_is_black {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1399.

```text
modo_skill_override = 8;
  }
  oneof _fen_player_is_white {
  string fen_player_is_white = 9;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 10;
  }
  optional uint32 win_points = 1;
  optional uint32 loss_points = 2;
  optional uint32 draw_points = 3;
  optional bool assistance_use_penalty = 4;
}

message BotLabel {
  optional .chesscom.bots.v1.BotLabelType type = 1;
}

message BotEventTheme {
  o
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00543"></a>
## FND-00543: chesscom.bots.v1.BotProperties.fen_player_is_black = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string fen_player_is_black = 10;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1430.

```text
oneof _fen_player_is_white {
  string fen_player_is_white = 9;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 10;
  }
  optional uint32 win_points = 1;
  optional uint32 loss_points = 2;
  optional uint32 draw_points = 3;
  optional bool assistance_use_penalty = 4;
}

message BotLabel {
  optional .chesscom.bots.v1.BotLabelType type = 1;
}

message BotEventTheme {
  optional string primary_color = 
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00544"></a>
## FND-00544: chesscom.bots.v1.BotProperties.win_points = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 win_points = 1;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1469.

```text
en_player_is_white = 9;
  }
  oneof _fen_player_is_black {
  string fen_player_is_black = 10;
  }
  optional uint32 win_points = 1;
  optional uint32 loss_points = 2;
  optional uint32 draw_points = 3;
  optional bool assistance_use_penalty = 4;
}

message BotLabel {
  optional .chesscom.bots.v1.BotLabelType type = 1;
}

message BotEventTheme {
  optional string primary_color = 1;
  optional string secondary_color = 
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00545"></a>
## FND-00545: chesscom.bots.v1.BotProperties.loss_points = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 loss_points = 2;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1503.

```text
f _fen_player_is_black {
  string fen_player_is_black = 10;
  }
  optional uint32 win_points = 1;
  optional uint32 loss_points = 2;
  optional uint32 draw_points = 3;
  optional bool assistance_use_penalty = 4;
}

message BotLabel {
  optional .chesscom.bots.v1.BotLabelType type = 1;
}

message BotEventTheme {
  optional string primary_color = 1;
  optional string secondary_color = 2;
  optional .chesscom.api.v1.Ass
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00546"></a>
## FND-00546: chesscom.bots.v1.BotProperties.draw_points = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 draw_points = 3;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1538.

```text
en_player_is_black = 10;
  }
  optional uint32 win_points = 1;
  optional uint32 loss_points = 2;
  optional uint32 draw_points = 3;
  optional bool assistance_use_penalty = 4;
}

message BotLabel {
  optional .chesscom.bots.v1.BotLabelType type = 1;
}

message BotEventTheme {
  optional string primary_color = 1;
  optional string secondary_color = 2;
  optional .chesscom.api.v1.Asset points_icon = 3;
  optional .che
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00547"></a>
## FND-00547: chesscom.bots.v1.BotProperties.assistance_use_penalty = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool assistance_use_penalty = 4;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1573.

```text
onal uint32 win_points = 1;
  optional uint32 loss_points = 2;
  optional uint32 draw_points = 3;
  optional bool assistance_use_penalty = 4;
}

message BotLabel {
  optional .chesscom.bots.v1.BotLabelType type = 1;
}

message BotEventTheme {
  optional string primary_color = 1;
  optional string secondary_color = 2;
  optional .chesscom.api.v1.Asset points_icon = 3;
  optional .chesscom.api.v1.Asset banner_image = 4
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00548"></a>
## FND-00548: message declaration: chesscom.bots.v1.BotLabel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotLabel {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1618.

```text
 loss_points = 2;
  optional uint32 draw_points = 3;
  optional bool assistance_use_penalty = 4;
}

message BotLabel {
  optional .chesscom.bots.v1.BotLabelType type = 1;
}

message BotEventTheme {
  optional string primary_color = 1;
  optional string secondary_color = 2;
  optional .chesscom.api.v1.Asset points_icon = 3;
  optional .chesscom.api.v1.Asset banner_image = 4;
  optional .chesscom.api.v1.Asset backgroun
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00549"></a>
## FND-00549: chesscom.bots.v1.BotLabel.type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.bots.v1.BotLabelType type = 1;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1639.

```text
ptional uint32 draw_points = 3;
  optional bool assistance_use_penalty = 4;
}

message BotLabel {
  optional .chesscom.bots.v1.BotLabelType type = 1;
}

message BotEventTheme {
  optional string primary_color = 1;
  optional string secondary_color = 2;
  optional .chesscom.api.v1.Asset points_icon = 3;
  optional .chesscom.api.v1.Asset banner_image = 4;
  optional .chesscom.api.v1.Asset background_image = 5;
  option
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00550"></a>
## FND-00550: message declaration: chesscom.bots.v1.BotEventTheme

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotEventTheme {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1692.

```text
tance_use_penalty = 4;
}

message BotLabel {
  optional .chesscom.bots.v1.BotLabelType type = 1;
}

message BotEventTheme {
  optional string primary_color = 1;
  optional string secondary_color = 2;
  optional .chesscom.api.v1.Asset points_icon = 3;
  optional .chesscom.api.v1.Asset banner_image = 4;
  optional .chesscom.api.v1.Asset background_image = 5;
  optional .chesscom.bots.v1.BotEventSounds sounds = 6;
}

me
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00551"></a>
## FND-00551: chesscom.bots.v1.BotEventTheme.primary_color = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string primary_color = 1;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1718.

```text
message BotLabel {
  optional .chesscom.bots.v1.BotLabelType type = 1;
}

message BotEventTheme {
  optional string primary_color = 1;
  optional string secondary_color = 2;
  optional .chesscom.api.v1.Asset points_icon = 3;
  optional .chesscom.api.v1.Asset banner_image = 4;
  optional .chesscom.api.v1.Asset background_image = 5;
  optional .chesscom.bots.v1.BotEventSounds sounds = 6;
}

message BotEventSounds {
  o
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00552"></a>
## FND-00552: chesscom.bots.v1.BotEventTheme.secondary_color = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string secondary_color = 2;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1755.

```text
om.bots.v1.BotLabelType type = 1;
}

message BotEventTheme {
  optional string primary_color = 1;
  optional string secondary_color = 2;
  optional .chesscom.api.v1.Asset points_icon = 3;
  optional .chesscom.api.v1.Asset banner_image = 4;
  optional .chesscom.api.v1.Asset background_image = 5;
  optional .chesscom.bots.v1.BotEventSounds sounds = 6;
}

message BotEventSounds {
  oneof _game_start {
  .chesscom.api.v1
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00553"></a>
## FND-00553: chesscom.bots.v1.BotEventTheme.points_icon = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Asset points_icon = 3;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1794.

```text
ssage BotEventTheme {
  optional string primary_color = 1;
  optional string secondary_color = 2;
  optional .chesscom.api.v1.Asset points_icon = 3;
  optional .chesscom.api.v1.Asset banner_image = 4;
  optional .chesscom.api.v1.Asset background_image = 5;
  optional .chesscom.bots.v1.BotEventSounds sounds = 6;
}

message BotEventSounds {
  oneof _game_start {
  .chesscom.api.v1.Asset game_start = 1;
  }
  oneof _gam
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00554"></a>
## FND-00554: chesscom.bots.v1.BotEventTheme.banner_image = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Asset banner_image = 4;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1845.

```text
or = 1;
  optional string secondary_color = 2;
  optional .chesscom.api.v1.Asset points_icon = 3;
  optional .chesscom.api.v1.Asset banner_image = 4;
  optional .chesscom.api.v1.Asset background_image = 5;
  optional .chesscom.bots.v1.BotEventSounds sounds = 6;
}

message BotEventSounds {
  oneof _game_start {
  .chesscom.api.v1.Asset game_start = 1;
  }
  oneof _gameplay_ambient {
  .chesscom.api.v1.Asset gameplay_a
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00555"></a>
## FND-00555: chesscom.bots.v1.BotEventTheme.background_image = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Asset background_image = 5;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1897.

```text
ional .chesscom.api.v1.Asset points_icon = 3;
  optional .chesscom.api.v1.Asset banner_image = 4;
  optional .chesscom.api.v1.Asset background_image = 5;
  optional .chesscom.bots.v1.BotEventSounds sounds = 6;
}

message BotEventSounds {
  oneof _game_start {
  .chesscom.api.v1.Asset game_start = 1;
  }
  oneof _gameplay_ambient {
  .chesscom.api.v1.Asset gameplay_ambient = 2;
  }
}

message BotVariationModalData {
 
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00556"></a>
## FND-00556: chesscom.bots.v1.BotEventTheme.sounds = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.bots.v1.BotEventSounds sounds = 6;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 1953.

```text
 .chesscom.api.v1.Asset banner_image = 4;
  optional .chesscom.api.v1.Asset background_image = 5;
  optional .chesscom.bots.v1.BotEventSounds sounds = 6;
}

message BotEventSounds {
  oneof _game_start {
  .chesscom.api.v1.Asset game_start = 1;
  }
  oneof _gameplay_ambient {
  .chesscom.api.v1.Asset gameplay_ambient = 2;
  }
}

message BotVariationModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional s
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00557"></a>
## FND-00557: message declaration: chesscom.bots.v1.BotEventSounds

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotEventSounds {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2010.

```text
sscom.api.v1.Asset background_image = 5;
  optional .chesscom.bots.v1.BotEventSounds sounds = 6;
}

message BotEventSounds {
  oneof _game_start {
  .chesscom.api.v1.Asset game_start = 1;
  }
  oneof _gameplay_ambient {
  .chesscom.api.v1.Asset gameplay_ambient = 2;
  }
}

message BotVariationModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string bot_advantage_text = 3
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00558"></a>
## FND-00558: oneof declaration: chesscom.bots.v1.BotEventSounds._game_start

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_start {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2037.

```text
nd_image = 5;
  optional .chesscom.bots.v1.BotEventSounds sounds = 6;
}

message BotEventSounds {
  oneof _game_start {
  .chesscom.api.v1.Asset game_start = 1;
  }
  oneof _gameplay_ambient {
  .chesscom.api.v1.Asset gameplay_ambient = 2;
  }
}

message BotVariationModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string bot_advantage_text = 3;
  optional string bot_dis
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00559"></a>
## FND-00559: chesscom.bots.v1.BotEventSounds.game_start = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.Asset game_start = 1;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2059.

```text
al .chesscom.bots.v1.BotEventSounds sounds = 6;
}

message BotEventSounds {
  oneof _game_start {
  .chesscom.api.v1.Asset game_start = 1;
  }
  oneof _gameplay_ambient {
  .chesscom.api.v1.Asset gameplay_ambient = 2;
  }
}

message BotVariationModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string bot_advantage_text = 3;
  optional string bot_disadvantage_text = 4;
}

```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00560"></a>
## FND-00560: oneof declaration: chesscom.bots.v1.BotEventSounds._gameplay_ambient

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_ambient {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2104.

```text
6;
}

message BotEventSounds {
  oneof _game_start {
  .chesscom.api.v1.Asset game_start = 1;
  }
  oneof _gameplay_ambient {
  .chesscom.api.v1.Asset gameplay_ambient = 2;
  }
}

message BotVariationModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string bot_advantage_text = 3;
  optional string bot_disadvantage_text = 4;
}

message BotEventIntroModalData {
  optional 
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00561"></a>
## FND-00561: chesscom.bots.v1.BotEventSounds.gameplay_ambient = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.Asset gameplay_ambient = 2;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2132.

```text
 {
  oneof _game_start {
  .chesscom.api.v1.Asset game_start = 1;
  }
  oneof _gameplay_ambient {
  .chesscom.api.v1.Asset gameplay_ambient = 2;
  }
}

message BotVariationModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string bot_advantage_text = 3;
  optional string bot_disadvantage_text = 4;
}

message BotEventIntroModalData {
  optional .chesscom.api.v1.Asset image
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00562"></a>
## FND-00562: message declaration: chesscom.bots.v1.BotVariationModalData

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotVariationModalData {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2184.

```text
me_start = 1;
  }
  oneof _gameplay_ambient {
  .chesscom.api.v1.Asset gameplay_ambient = 2;
  }
}

message BotVariationModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string bot_advantage_text = 3;
  optional string bot_disadvantage_text = 4;
}

message BotEventIntroModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00563"></a>
## FND-00563: chesscom.bots.v1.BotVariationModalData.image = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Asset image = 1;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2218.

```text
y_ambient {
  .chesscom.api.v1.Asset gameplay_ambient = 2;
  }
}

message BotVariationModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string bot_advantage_text = 3;
  optional string bot_disadvantage_text = 4;
}

message BotEventIntroModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string subtitle = 3;
  repeated .chessco
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00564"></a>
## FND-00564: chesscom.bots.v1.BotVariationModalData.title = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string title = 2;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2263.

```text
_ambient = 2;
  }
}

message BotVariationModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string bot_advantage_text = 3;
  optional string bot_disadvantage_text = 4;
}

message BotEventIntroModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string subtitle = 3;
  repeated .chesscom.bots.v1.BotEventIntroModalInfoItemData info
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00565"></a>
## FND-00565: chesscom.bots.v1.BotVariationModalData.bot_advantage_text = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string bot_advantage_text = 3;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2292.

```text
BotVariationModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string bot_advantage_text = 3;
  optional string bot_disadvantage_text = 4;
}

message BotEventIntroModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string subtitle = 3;
  repeated .chesscom.bots.v1.BotEventIntroModalInfoItemData info_items = 4;
}

message BotEve
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00566"></a>
## FND-00566: chesscom.bots.v1.BotVariationModalData.bot_disadvantage_text = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string bot_disadvantage_text = 4;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2334.

```text
om.api.v1.Asset image = 1;
  optional string title = 2;
  optional string bot_advantage_text = 3;
  optional string bot_disadvantage_text = 4;
}

message BotEventIntroModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string subtitle = 3;
  repeated .chesscom.bots.v1.BotEventIntroModalInfoItemData info_items = 4;
}

message BotEventIntroModalInfoItemData {
  optional .che
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00567"></a>
## FND-00567: message declaration: chesscom.bots.v1.BotEventIntroModalData

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotEventIntroModalData {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2380.

```text
itle = 2;
  optional string bot_advantage_text = 3;
  optional string bot_disadvantage_text = 4;
}

message BotEventIntroModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string subtitle = 3;
  repeated .chesscom.bots.v1.BotEventIntroModalInfoItemData info_items = 4;
}

message BotEventIntroModalInfoItemData {
  optional .chesscom.api.v1.Asset icon = 1;
  optional string
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00568"></a>
## FND-00568: chesscom.bots.v1.BotEventIntroModalData.image = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Asset image = 1;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2218.

```text
y_ambient {
  .chesscom.api.v1.Asset gameplay_ambient = 2;
  }
}

message BotVariationModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string bot_advantage_text = 3;
  optional string bot_disadvantage_text = 4;
}

message BotEventIntroModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string subtitle = 3;
  repeated .chessco
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00569"></a>
## FND-00569: chesscom.bots.v1.BotEventIntroModalData.title = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string title = 2;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2263.

```text
_ambient = 2;
  }
}

message BotVariationModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string bot_advantage_text = 3;
  optional string bot_disadvantage_text = 4;
}

message BotEventIntroModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string subtitle = 3;
  repeated .chesscom.bots.v1.BotEventIntroModalInfoItemData info
```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00570"></a>
## FND-00570: chesscom.bots.v1.BotEventIntroModalData.subtitle = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string subtitle = 3;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2489.

```text
otEventIntroModalData {
  optional .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string subtitle = 3;
  repeated .chesscom.bots.v1.BotEventIntroModalInfoItemData info_items = 4;
}

message BotEventIntroModalInfoItemData {
  optional .chesscom.api.v1.Asset icon = 1;
  optional string text = 2;
}

```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00571"></a>
## FND-00571: chesscom.bots.v1.BotEventIntroModalData.info_items = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.bots.v1.BotEventIntroModalInfoItemData info_items = 4;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2521.

```text
al .chesscom.api.v1.Asset image = 1;
  optional string title = 2;
  optional string subtitle = 3;
  repeated .chesscom.bots.v1.BotEventIntroModalInfoItemData info_items = 4;
}

message BotEventIntroModalInfoItemData {
  optional .chesscom.api.v1.Asset icon = 1;
  optional string text = 2;
}

```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00572"></a>
## FND-00572: message declaration: chesscom.bots.v1.BotEventIntroModalInfoItemData

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotEventIntroModalInfoItemData {

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2598.

```text
string subtitle = 3;
  repeated .chesscom.bots.v1.BotEventIntroModalInfoItemData info_items = 4;
}

message BotEventIntroModalInfoItemData {
  optional .chesscom.api.v1.Asset icon = 1;
  optional string text = 2;
}

```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00573"></a>
## FND-00573: chesscom.bots.v1.BotEventIntroModalInfoItemData.icon = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Asset icon = 1;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2641.

```text
ots.v1.BotEventIntroModalInfoItemData info_items = 4;
}

message BotEventIntroModalInfoItemData {
  optional .chesscom.api.v1.Asset icon = 1;
  optional string text = 2;
}

```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00574"></a>
## FND-00574: chesscom.bots.v1.BotEventIntroModalInfoItemData.text = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string text = 2;

### Evidence

- **SRC-0223** `research/proto/chesscom/bots/v1/bot_event.proto` — [preserved redacted evidence](../evidence/text/8dde1ccb83191fab53b616d2f2b84e73bf1c9358e510e8639226c7b2458c0dee.proto)
  Character offset 2685.

```text
tems = 4;
}

message BotEventIntroModalInfoItemData {
  optional .chesscom.api.v1.Asset icon = 1;
  optional string text = 2;
}

```

**Source references:** SRC-0223, SRC-1194  
**URL references:** None independently associated  
**Related findings:** FND-00508, FND-00509, FND-00510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
