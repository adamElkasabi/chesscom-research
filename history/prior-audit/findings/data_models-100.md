# data_models — findings 9901–10000

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-10175"></a>
## FND-10175: chesscom.user_properties.v1.AttributionProperty.signup_initial_source = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string signup_initial_source = 7;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 1000.

```text
f _signup_initial_route {
  string signup_initial_route = 6;
  }
  oneof _signup_initial_source {
  string signup_initial_source = 7;
  }
  oneof _signup_initial_term {
  string signup_initial_term = 8;
  }
  oneof _signup_initial_version {
  string signup_initial_version = 9;
  }
}

```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10176"></a>
## FND-10176: oneof declaration: chesscom.user_properties.v1.AttributionProperty._signup_initial_term

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _signup_initial_term {

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 1040.

```text
p_initial_route = 6;
  }
  oneof _signup_initial_source {
  string signup_initial_source = 7;
  }
  oneof _signup_initial_term {
  string signup_initial_term = 8;
  }
  oneof _signup_initial_version {
  string signup_initial_version = 9;
  }
}

```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10177"></a>
## FND-10177: chesscom.user_properties.v1.AttributionProperty.signup_initial_term = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string signup_initial_term = 8;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 1071.

```text
f _signup_initial_source {
  string signup_initial_source = 7;
  }
  oneof _signup_initial_term {
  string signup_initial_term = 8;
  }
  oneof _signup_initial_version {
  string signup_initial_version = 9;
  }
}

```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10178"></a>
## FND-10178: oneof declaration: chesscom.user_properties.v1.AttributionProperty._signup_initial_version

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _signup_initial_version {

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 1109.

```text
gnup_initial_source = 7;
  }
  oneof _signup_initial_term {
  string signup_initial_term = 8;
  }
  oneof _signup_initial_version {
  string signup_initial_version = 9;
  }
}

```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10179"></a>
## FND-10179: chesscom.user_properties.v1.AttributionProperty.signup_initial_version = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string signup_initial_version = 9;

### Evidence

- **SRC-0603** `research/proto/chesscom/user_properties/v1/properties_attribution.proto` — [preserved redacted evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto)
  Character offset 1143.

```text
of _signup_initial_term {
  string signup_initial_term = 8;
  }
  oneof _signup_initial_version {
  string signup_initial_version = 9;
  }
}

```

**Source references:** SRC-0603, SRC-1574  
**URL references:** None independently associated  
**Related findings:** FND-10150, FND-10151, FND-10152

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10180"></a>
## FND-10180: enum declaration: chesscom.user_properties.v1.AudiencesPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum AudiencesPropertyDefinition {

### Evidence

- **SRC-0604** `research/proto/chesscom/user_properties/v1/properties_audiences.proto` — [preserved redacted evidence](../evidence/text/2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29.proto)
  Character offset 123.

```text
r_properties/v1/properties_audiences.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum AudiencesPropertyDefinition {
  AUDIENCES_PROPERTY_UNSPECIFIED = 0;
  AUDIENCES_MEMBER_OF = 1;
  AUDIENCES_MEMBER_OF_LAST_UPDATE = 2;
  EPHEMERAL_AUDIENCES_MEMBER_OF = 3;
  EPHEMERAL_AUDIENCES_MEMBER_OF_LAST_UPDATE = 4;
}

message AudiencesProperty {
  oneof _member_of_last_update {
  .google.protobuf.Timestamp me
```

**Source references:** SRC-0604, SRC-1575  
**URL references:** None independently associated  
**Related findings:** FND-10181, FND-10182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10181"></a>
## FND-10181: chesscom.user_properties.v1.AudiencesPropertyDefinition.AUDIENCES_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

AUDIENCES_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0604** `research/proto/chesscom/user_properties/v1/properties_audiences.proto` — [preserved redacted evidence](../evidence/text/2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29.proto)
  Character offset 160.

```text
proto
// syntax: proto3

package chesscom.user_properties.v1;

enum AudiencesPropertyDefinition {
  AUDIENCES_PROPERTY_UNSPECIFIED = 0;
  AUDIENCES_MEMBER_OF = 1;
  AUDIENCES_MEMBER_OF_LAST_UPDATE = 2;
  EPHEMERAL_AUDIENCES_MEMBER_OF = 3;
  EPHEMERAL_AUDIENCES_MEMBER_OF_LAST_UPDATE = 4;
}

message AudiencesProperty {
  oneof _member_of_last_update {
  .google.protobuf.Timestamp member_of_last_update = 2;
  }
  oneof 
```

**Source references:** SRC-0604, SRC-1575  
**URL references:** None independently associated  
**Related findings:** FND-10180, FND-10182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10182"></a>
## FND-10182: chesscom.user_properties.v1.AudiencesPropertyDefinition.AUDIENCES_MEMBER_OF = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

AUDIENCES_MEMBER_OF = 1;

### Evidence

- **SRC-0604** `research/proto/chesscom/user_properties/v1/properties_audiences.proto` — [preserved redacted evidence](../evidence/text/2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29.proto)
  Character offset 198.

```text
com.user_properties.v1;

enum AudiencesPropertyDefinition {
  AUDIENCES_PROPERTY_UNSPECIFIED = 0;
  AUDIENCES_MEMBER_OF = 1;
  AUDIENCES_MEMBER_OF_LAST_UPDATE = 2;
  EPHEMERAL_AUDIENCES_MEMBER_OF = 3;
  EPHEMERAL_AUDIENCES_MEMBER_OF_LAST_UPDATE = 4;
}

message AudiencesProperty {
  oneof _member_of_last_update {
  .google.protobuf.Timestamp member_of_last_update = 2;
  }
  oneof _ephemeral_audiences_member_of_last_up
```

**Source references:** SRC-0604, SRC-1575  
**URL references:** None independently associated  
**Related findings:** FND-10180, FND-10181

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10183"></a>
## FND-10183: chesscom.user_properties.v1.AudiencesPropertyDefinition.AUDIENCES_MEMBER_OF_LAST_UPDATE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

AUDIENCES_MEMBER_OF_LAST_UPDATE = 2;

### Evidence

- **SRC-0604** `research/proto/chesscom/user_properties/v1/properties_audiences.proto` — [preserved redacted evidence](../evidence/text/2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29.proto)
  Character offset 225.

```text
um AudiencesPropertyDefinition {
  AUDIENCES_PROPERTY_UNSPECIFIED = 0;
  AUDIENCES_MEMBER_OF = 1;
  AUDIENCES_MEMBER_OF_LAST_UPDATE = 2;
  EPHEMERAL_AUDIENCES_MEMBER_OF = 3;
  EPHEMERAL_AUDIENCES_MEMBER_OF_LAST_UPDATE = 4;
}

message AudiencesProperty {
  oneof _member_of_last_update {
  .google.protobuf.Timestamp member_of_last_update = 2;
  }
  oneof _ephemeral_audiences_member_of_last_update {
  .google.protobuf.T
```

**Source references:** SRC-0604, SRC-1575  
**URL references:** None independently associated  
**Related findings:** FND-10180, FND-10181, FND-10182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10184"></a>
## FND-10184: chesscom.user_properties.v1.AudiencesPropertyDefinition.EPHEMERAL_AUDIENCES_MEMBER_OF = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EPHEMERAL_AUDIENCES_MEMBER_OF = 3;

### Evidence

- **SRC-0604** `research/proto/chesscom/user_properties/v1/properties_audiences.proto` — [preserved redacted evidence](../evidence/text/2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29.proto)
  Character offset 264.

```text
ENCES_PROPERTY_UNSPECIFIED = 0;
  AUDIENCES_MEMBER_OF = 1;
  AUDIENCES_MEMBER_OF_LAST_UPDATE = 2;
  EPHEMERAL_AUDIENCES_MEMBER_OF = 3;
  EPHEMERAL_AUDIENCES_MEMBER_OF_LAST_UPDATE = 4;
}

message AudiencesProperty {
  oneof _member_of_last_update {
  .google.protobuf.Timestamp member_of_last_update = 2;
  }
  oneof _ephemeral_audiences_member_of_last_update {
  .google.protobuf.Timestamp ephemeral_audiences_member_of_
```

**Source references:** SRC-0604, SRC-1575  
**URL references:** None independently associated  
**Related findings:** FND-10180, FND-10181, FND-10182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10185"></a>
## FND-10185: chesscom.user_properties.v1.AudiencesPropertyDefinition.EPHEMERAL_AUDIENCES_MEMBER_OF_LAST_UPDATE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EPHEMERAL_AUDIENCES_MEMBER_OF_LAST_UPDATE = 4;

### Evidence

- **SRC-0604** `research/proto/chesscom/user_properties/v1/properties_audiences.proto` — [preserved redacted evidence](../evidence/text/2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29.proto)
  Character offset 301.

```text
IENCES_MEMBER_OF = 1;
  AUDIENCES_MEMBER_OF_LAST_UPDATE = 2;
  EPHEMERAL_AUDIENCES_MEMBER_OF = 3;
  EPHEMERAL_AUDIENCES_MEMBER_OF_LAST_UPDATE = 4;
}

message AudiencesProperty {
  oneof _member_of_last_update {
  .google.protobuf.Timestamp member_of_last_update = 2;
  }
  oneof _ephemeral_audiences_member_of_last_update {
  .google.protobuf.Timestamp ephemeral_audiences_member_of_last_update = 4;
  }
  repeated strin
```

**Source references:** SRC-0604, SRC-1575  
**URL references:** None independently associated  
**Related findings:** FND-10180, FND-10181, FND-10182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10186"></a>
## FND-10186: message declaration: chesscom.user_properties.v1.AudiencesProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AudiencesProperty {

### Evidence

- **SRC-0604** `research/proto/chesscom/user_properties/v1/properties_audiences.proto` — [preserved redacted evidence](../evidence/text/2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29.proto)
  Character offset 351.

```text
PDATE = 2;
  EPHEMERAL_AUDIENCES_MEMBER_OF = 3;
  EPHEMERAL_AUDIENCES_MEMBER_OF_LAST_UPDATE = 4;
}

message AudiencesProperty {
  oneof _member_of_last_update {
  .google.protobuf.Timestamp member_of_last_update = 2;
  }
  oneof _ephemeral_audiences_member_of_last_update {
  .google.protobuf.Timestamp ephemeral_audiences_member_of_last_update = 4;
  }
  repeated string member_of = 1;
  repeated string ephemeral_audie
```

**Source references:** SRC-0604, SRC-1575  
**URL references:** None independently associated  
**Related findings:** FND-10180, FND-10181, FND-10182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10187"></a>
## FND-10187: oneof declaration: chesscom.user_properties.v1.AudiencesProperty._member_of_last_update

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _member_of_last_update {

### Evidence

- **SRC-0604** `research/proto/chesscom/user_properties/v1/properties_audiences.proto` — [preserved redacted evidence](../evidence/text/2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29.proto)
  Character offset 381.

```text
ES_MEMBER_OF = 3;
  EPHEMERAL_AUDIENCES_MEMBER_OF_LAST_UPDATE = 4;
}

message AudiencesProperty {
  oneof _member_of_last_update {
  .google.protobuf.Timestamp member_of_last_update = 2;
  }
  oneof _ephemeral_audiences_member_of_last_update {
  .google.protobuf.Timestamp ephemeral_audiences_member_of_last_update = 4;
  }
  repeated string member_of = 1;
  repeated string ephemeral_audiences_member_of = 3;
}

```

**Source references:** SRC-0604, SRC-1575  
**URL references:** None independently associated  
**Related findings:** FND-10180, FND-10181, FND-10182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10188"></a>
## FND-10188: chesscom.user_properties.v1.AudiencesProperty.member_of_last_update = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp member_of_last_update = 2;

### Evidence

- **SRC-0604** `research/proto/chesscom/user_properties/v1/properties_audiences.proto` — [preserved redacted evidence](../evidence/text/2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29.proto)
  Character offset 414.

```text
IENCES_MEMBER_OF_LAST_UPDATE = 4;
}

message AudiencesProperty {
  oneof _member_of_last_update {
  .google.protobuf.Timestamp member_of_last_update = 2;
  }
  oneof _ephemeral_audiences_member_of_last_update {
  .google.protobuf.Timestamp ephemeral_audiences_member_of_last_update = 4;
  }
  repeated string member_of = 1;
  repeated string ephemeral_audiences_member_of = 3;
}

```

**Source references:** SRC-0604, SRC-1575  
**URL references:** None independently associated  
**Related findings:** FND-10180, FND-10181, FND-10182

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10189"></a>
## FND-10189: oneof declaration: chesscom.user_properties.v1.AudiencesProperty._ephemeral_audiences_member_of_last_update

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ephemeral_audiences_member_of_last_update {

### Evidence

- **SRC-0604** `research/proto/chesscom/user_properties/v1/properties_audiences.proto` — [preserved redacted evidence](../evidence/text/2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29.proto)
  Character offset 474.

```text
ty {
  oneof _member_of_last_update {
  .google.protobuf.Timestamp member_of_last_update = 2;
  }
  oneof _ephemeral_audiences_member_of_last_update {
  .google.protobuf.Timestamp ephemeral_audiences_member_of_last_update = 4;
  }
  repeated string member_of = 1;
  repeated string ephemeral_audiences_member_of = 3;
}

```

**Source references:** SRC-0604, SRC-1575  
**URL references:** None independently associated  
**Related findings:** FND-10180, FND-10181, FND-10182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10190"></a>
## FND-10190: chesscom.user_properties.v1.AudiencesProperty.ephemeral_audiences_member_of_last_update = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp ephemeral_audiences_member_of_last_update = 4;

### Evidence

- **SRC-0604** `research/proto/chesscom/user_properties/v1/properties_audiences.proto` — [preserved redacted evidence](../evidence/text/2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29.proto)
  Character offset 527.

```text
buf.Timestamp member_of_last_update = 2;
  }
  oneof _ephemeral_audiences_member_of_last_update {
  .google.protobuf.Timestamp ephemeral_audiences_member_of_last_update = 4;
  }
  repeated string member_of = 1;
  repeated string ephemeral_audiences_member_of = 3;
}

```

**Source references:** SRC-0604, SRC-1575  
**URL references:** None independently associated  
**Related findings:** FND-10180, FND-10181, FND-10182

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10191"></a>
## FND-10191: chesscom.user_properties.v1.AudiencesProperty.member_of = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string member_of = 1;

### Evidence

- **SRC-0604** `research/proto/chesscom/user_properties/v1/properties_audiences.proto` — [preserved redacted evidence](../evidence/text/2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29.proto)
  Character offset 607.

```text
_of_last_update {
  .google.protobuf.Timestamp ephemeral_audiences_member_of_last_update = 4;
  }
  repeated string member_of = 1;
  repeated string ephemeral_audiences_member_of = 3;
}

```

**Source references:** SRC-0604, SRC-1575  
**URL references:** None independently associated  
**Related findings:** FND-10180, FND-10181, FND-10182

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10192"></a>
## FND-10192: chesscom.user_properties.v1.AudiencesProperty.ephemeral_audiences_member_of = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string ephemeral_audiences_member_of = 3;

### Evidence

- **SRC-0604** `research/proto/chesscom/user_properties/v1/properties_audiences.proto` — [preserved redacted evidence](../evidence/text/2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29.proto)
  Character offset 640.

```text
buf.Timestamp ephemeral_audiences_member_of_last_update = 4;
  }
  repeated string member_of = 1;
  repeated string ephemeral_audiences_member_of = 3;
}

```

**Source references:** SRC-0604, SRC-1575  
**URL references:** None independently associated  
**Related findings:** FND-10180, FND-10181, FND-10182

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10193"></a>
## FND-10193: enum declaration: chesscom.user_properties.v1.ClubsPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ClubsPropertyDefinition {

### Evidence

- **SRC-0605** `research/proto/chesscom/user_properties/v1/properties_clubs.proto` — [preserved redacted evidence](../evidence/text/9a7e8594cfa50a28ab9c21051573052d74b5ba58e75fee1a0d329db3ecd56ea8.proto)
  Character offset 119.

```text
/user_properties/v1/properties_clubs.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum ClubsPropertyDefinition {
  CLUBS_PROPERTY_UNSPECIFIED = 0;
  CLUBS_JOINED = 1;
  CLUBS_BANNED = 2;
  CLUBS_JOINED_COUNT = 3;
}

message ClubsProperty {
  repeated string clubs_joined = 1;
  repeated string clubs_banned = 2;
  optional int32 clubs_joined_count = 3;
}

```

**Source references:** SRC-0605, SRC-1576  
**URL references:** None independently associated  
**Related findings:** FND-10194, FND-10195

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10194"></a>
## FND-10194: chesscom.user_properties.v1.ClubsPropertyDefinition.CLUBS_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLUBS_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0605** `research/proto/chesscom/user_properties/v1/properties_clubs.proto` — [preserved redacted evidence](../evidence/text/9a7e8594cfa50a28ab9c21051573052d74b5ba58e75fee1a0d329db3ecd56ea8.proto)
  Character offset 152.

```text
ubs.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum ClubsPropertyDefinition {
  CLUBS_PROPERTY_UNSPECIFIED = 0;
  CLUBS_JOINED = 1;
  CLUBS_BANNED = 2;
  CLUBS_JOINED_COUNT = 3;
}

message ClubsProperty {
  repeated string clubs_joined = 1;
  repeated string clubs_banned = 2;
  optional int32 clubs_joined_count = 3;
}

```

**Source references:** SRC-0605, SRC-1576  
**URL references:** None independently associated  
**Related findings:** FND-10193, FND-10195

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10195"></a>
## FND-10195: chesscom.user_properties.v1.ClubsPropertyDefinition.CLUBS_JOINED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLUBS_JOINED = 1;

### Evidence

- **SRC-0605** `research/proto/chesscom/user_properties/v1/properties_clubs.proto` — [preserved redacted evidence](../evidence/text/9a7e8594cfa50a28ab9c21051573052d74b5ba58e75fee1a0d329db3ecd56ea8.proto)
  Character offset 186.

```text
ge chesscom.user_properties.v1;

enum ClubsPropertyDefinition {
  CLUBS_PROPERTY_UNSPECIFIED = 0;
  CLUBS_JOINED = 1;
  CLUBS_BANNED = 2;
  CLUBS_JOINED_COUNT = 3;
}

message ClubsProperty {
  repeated string clubs_joined = 1;
  repeated string clubs_banned = 2;
  optional int32 clubs_joined_count = 3;
}

```

**Source references:** SRC-0605, SRC-1576  
**URL references:** None independently associated  
**Related findings:** FND-10193, FND-10194

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10196"></a>
## FND-10196: chesscom.user_properties.v1.ClubsPropertyDefinition.CLUBS_BANNED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLUBS_BANNED = 2;

### Evidence

- **SRC-0605** `research/proto/chesscom/user_properties/v1/properties_clubs.proto` — [preserved redacted evidence](../evidence/text/9a7e8594cfa50a28ab9c21051573052d74b5ba58e75fee1a0d329db3ecd56ea8.proto)
  Character offset 206.

```text
perties.v1;

enum ClubsPropertyDefinition {
  CLUBS_PROPERTY_UNSPECIFIED = 0;
  CLUBS_JOINED = 1;
  CLUBS_BANNED = 2;
  CLUBS_JOINED_COUNT = 3;
}

message ClubsProperty {
  repeated string clubs_joined = 1;
  repeated string clubs_banned = 2;
  optional int32 clubs_joined_count = 3;
}

```

**Source references:** SRC-0605, SRC-1576  
**URL references:** None independently associated  
**Related findings:** FND-10193, FND-10194, FND-10195

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10197"></a>
## FND-10197: chesscom.user_properties.v1.ClubsPropertyDefinition.CLUBS_JOINED_COUNT = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLUBS_JOINED_COUNT = 3;

### Evidence

- **SRC-0605** `research/proto/chesscom/user_properties/v1/properties_clubs.proto` — [preserved redacted evidence](../evidence/text/9a7e8594cfa50a28ab9c21051573052d74b5ba58e75fee1a0d329db3ecd56ea8.proto)
  Character offset 226.

```text
ubsPropertyDefinition {
  CLUBS_PROPERTY_UNSPECIFIED = 0;
  CLUBS_JOINED = 1;
  CLUBS_BANNED = 2;
  CLUBS_JOINED_COUNT = 3;
}

message ClubsProperty {
  repeated string clubs_joined = 1;
  repeated string clubs_banned = 2;
  optional int32 clubs_joined_count = 3;
}

```

**Source references:** SRC-0605, SRC-1576  
**URL references:** None independently associated  
**Related findings:** FND-10193, FND-10194, FND-10195

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10198"></a>
## FND-10198: message declaration: chesscom.user_properties.v1.ClubsProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ClubsProperty {

### Evidence

- **SRC-0605** `research/proto/chesscom/user_properties/v1/properties_clubs.proto` — [preserved redacted evidence](../evidence/text/9a7e8594cfa50a28ab9c21051573052d74b5ba58e75fee1a0d329db3ecd56ea8.proto)
  Character offset 253.

```text
LUBS_PROPERTY_UNSPECIFIED = 0;
  CLUBS_JOINED = 1;
  CLUBS_BANNED = 2;
  CLUBS_JOINED_COUNT = 3;
}

message ClubsProperty {
  repeated string clubs_joined = 1;
  repeated string clubs_banned = 2;
  optional int32 clubs_joined_count = 3;
}

```

**Source references:** SRC-0605, SRC-1576  
**URL references:** None independently associated  
**Related findings:** FND-10193, FND-10194, FND-10195

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10199"></a>
## FND-10199: chesscom.user_properties.v1.ClubsProperty.clubs_joined = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string clubs_joined = 1;

### Evidence

- **SRC-0605** `research/proto/chesscom/user_properties/v1/properties_clubs.proto` — [preserved redacted evidence](../evidence/text/9a7e8594cfa50a28ab9c21051573052d74b5ba58e75fee1a0d329db3ecd56ea8.proto)
  Character offset 279.

```text
= 0;
  CLUBS_JOINED = 1;
  CLUBS_BANNED = 2;
  CLUBS_JOINED_COUNT = 3;
}

message ClubsProperty {
  repeated string clubs_joined = 1;
  repeated string clubs_banned = 2;
  optional int32 clubs_joined_count = 3;
}

```

**Source references:** SRC-0605, SRC-1576  
**URL references:** None independently associated  
**Related findings:** FND-10193, FND-10194, FND-10195

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10200"></a>
## FND-10200: chesscom.user_properties.v1.ClubsProperty.clubs_banned = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string clubs_banned = 2;

### Evidence

- **SRC-0605** `research/proto/chesscom/user_properties/v1/properties_clubs.proto` — [preserved redacted evidence](../evidence/text/9a7e8594cfa50a28ab9c21051573052d74b5ba58e75fee1a0d329db3ecd56ea8.proto)
  Character offset 315.

```text
NED = 2;
  CLUBS_JOINED_COUNT = 3;
}

message ClubsProperty {
  repeated string clubs_joined = 1;
  repeated string clubs_banned = 2;
  optional int32 clubs_joined_count = 3;
}

```

**Source references:** SRC-0605, SRC-1576  
**URL references:** None independently associated  
**Related findings:** FND-10193, FND-10194, FND-10195

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10201"></a>
## FND-10201: chesscom.user_properties.v1.ClubsProperty.clubs_joined_count = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 clubs_joined_count = 3;

### Evidence

- **SRC-0605** `research/proto/chesscom/user_properties/v1/properties_clubs.proto` — [preserved redacted evidence](../evidence/text/9a7e8594cfa50a28ab9c21051573052d74b5ba58e75fee1a0d329db3ecd56ea8.proto)
  Character offset 351.

```text


message ClubsProperty {
  repeated string clubs_joined = 1;
  repeated string clubs_banned = 2;
  optional int32 clubs_joined_count = 3;
}

```

**Source references:** SRC-0605, SRC-1576  
**URL references:** None independently associated  
**Related findings:** FND-10193, FND-10194, FND-10195

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10202"></a>
## FND-10202: enum declaration: chesscom.user_properties.v1.CoachesPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CoachesPropertyDefinition {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 121.

```text
ser_properties/v1/properties_coaches.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum CoachesPropertyDefinition {
  COACHES_PROPERTY_UNSPECIFIED = 0;
  DEFAULT_COACH_NAME = 1;
  DEFAULT_COACH_ID = 2;
  LAST_SELECTED_COACH_NAME = 3;
  LAST_SELECTED_COACH_ID = 4;
  LAST_SELECTED_COACH_DATE = 5;
  TOTAL_GAMES_STARTED_AGAINST_COACH = 6;
  COACH_RATING = 7;
  CURRENT_COACH_NAME = 8;
  CURRENT_COACH_ID =
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10203"></a>
## FND-10203: chesscom.user_properties.v1.CoachesPropertyDefinition.COACHES_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACHES_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 156.

```text
s.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum CoachesPropertyDefinition {
  COACHES_PROPERTY_UNSPECIFIED = 0;
  DEFAULT_COACH_NAME = 1;
  DEFAULT_COACH_ID = 2;
  LAST_SELECTED_COACH_NAME = 3;
  LAST_SELECTED_COACH_ID = 4;
  LAST_SELECTED_COACH_DATE = 5;
  TOTAL_GAMES_STARTED_AGAINST_COACH = 6;
  COACH_RATING = 7;
  CURRENT_COACH_NAME = 8;
  CURRENT_COACH_ID = 9;
  TOTAL_COACH_GAMES = 10;
  HAS
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10204"></a>
## FND-10204: chesscom.user_properties.v1.CoachesPropertyDefinition.DEFAULT_COACH_NAME = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DEFAULT_COACH_NAME = 1;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 192.

```text
hesscom.user_properties.v1;

enum CoachesPropertyDefinition {
  COACHES_PROPERTY_UNSPECIFIED = 0;
  DEFAULT_COACH_NAME = 1;
  DEFAULT_COACH_ID = 2;
  LAST_SELECTED_COACH_NAME = 3;
  LAST_SELECTED_COACH_ID = 4;
  LAST_SELECTED_COACH_DATE = 5;
  TOTAL_GAMES_STARTED_AGAINST_COACH = 6;
  COACH_RATING = 7;
  CURRENT_COACH_NAME = 8;
  CURRENT_COACH_ID = 9;
  TOTAL_COACH_GAMES = 10;
  HAS_SELECTED_COACH = 11;
  INITIAL_CHOS
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10205"></a>
## FND-10205: chesscom.user_properties.v1.CoachesPropertyDefinition.DEFAULT_COACH_ID = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DEFAULT_COACH_ID = 2;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 218.

```text
;

enum CoachesPropertyDefinition {
  COACHES_PROPERTY_UNSPECIFIED = 0;
  DEFAULT_COACH_NAME = 1;
  DEFAULT_COACH_ID = 2;
  LAST_SELECTED_COACH_NAME = 3;
  LAST_SELECTED_COACH_ID = 4;
  LAST_SELECTED_COACH_DATE = 5;
  TOTAL_GAMES_STARTED_AGAINST_COACH = 6;
  COACH_RATING = 7;
  CURRENT_COACH_NAME = 8;
  CURRENT_COACH_ID = 9;
  TOTAL_COACH_GAMES = 10;
  HAS_SELECTED_COACH = 11;
  INITIAL_CHOSEN_COACH = 12;
  INITIAL_C
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10206"></a>
## FND-10206: chesscom.user_properties.v1.CoachesPropertyDefinition.LAST_SELECTED_COACH_NAME = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_SELECTED_COACH_NAME = 3;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 242.

```text
efinition {
  COACHES_PROPERTY_UNSPECIFIED = 0;
  DEFAULT_COACH_NAME = 1;
  DEFAULT_COACH_ID = 2;
  LAST_SELECTED_COACH_NAME = 3;
  LAST_SELECTED_COACH_ID = 4;
  LAST_SELECTED_COACH_DATE = 5;
  TOTAL_GAMES_STARTED_AGAINST_COACH = 6;
  COACH_RATING = 7;
  CURRENT_COACH_NAME = 8;
  CURRENT_COACH_ID = 9;
  TOTAL_COACH_GAMES = 10;
  HAS_SELECTED_COACH = 11;
  INITIAL_CHOSEN_COACH = 12;
  INITIAL_COACH = 13;
  LAST_GAME_V
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10207"></a>
## FND-10207: chesscom.user_properties.v1.CoachesPropertyDefinition.LAST_SELECTED_COACH_ID = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_SELECTED_COACH_ID = 4;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 274.

```text
NSPECIFIED = 0;
  DEFAULT_COACH_NAME = 1;
  DEFAULT_COACH_ID = 2;
  LAST_SELECTED_COACH_NAME = 3;
  LAST_SELECTED_COACH_ID = 4;
  LAST_SELECTED_COACH_DATE = 5;
  TOTAL_GAMES_STARTED_AGAINST_COACH = 6;
  COACH_RATING = 7;
  CURRENT_COACH_NAME = 8;
  CURRENT_COACH_ID = 9;
  TOTAL_COACH_GAMES = 10;
  HAS_SELECTED_COACH = 11;
  INITIAL_CHOSEN_COACH = 12;
  INITIAL_COACH = 13;
  LAST_GAME_VS_COACH_FINISHED = 14;
}

messag
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10208"></a>
## FND-10208: chesscom.user_properties.v1.CoachesPropertyDefinition.LAST_SELECTED_COACH_DATE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_SELECTED_COACH_DATE = 5;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 304.

```text
H_NAME = 1;
  DEFAULT_COACH_ID = 2;
  LAST_SELECTED_COACH_NAME = 3;
  LAST_SELECTED_COACH_ID = 4;
  LAST_SELECTED_COACH_DATE = 5;
  TOTAL_GAMES_STARTED_AGAINST_COACH = 6;
  COACH_RATING = 7;
  CURRENT_COACH_NAME = 8;
  CURRENT_COACH_ID = 9;
  TOTAL_COACH_GAMES = 10;
  HAS_SELECTED_COACH = 11;
  INITIAL_CHOSEN_COACH = 12;
  INITIAL_COACH = 13;
  LAST_GAME_VS_COACH_FINISHED = 14;
}

message CoachesProperty {
  oneof _d
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10209"></a>
## FND-10209: chesscom.user_properties.v1.CoachesPropertyDefinition.TOTAL_GAMES_STARTED_AGAINST_COACH = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_GAMES_STARTED_AGAINST_COACH = 6;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 336.

```text
 2;
  LAST_SELECTED_COACH_NAME = 3;
  LAST_SELECTED_COACH_ID = 4;
  LAST_SELECTED_COACH_DATE = 5;
  TOTAL_GAMES_STARTED_AGAINST_COACH = 6;
  COACH_RATING = 7;
  CURRENT_COACH_NAME = 8;
  CURRENT_COACH_ID = 9;
  TOTAL_COACH_GAMES = 10;
  HAS_SELECTED_COACH = 11;
  INITIAL_CHOSEN_COACH = 12;
  INITIAL_COACH = 13;
  LAST_GAME_VS_COACH_FINISHED = 14;
}

message CoachesProperty {
  oneof _default_coach_name {
  string def
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10210"></a>
## FND-10210: chesscom.user_properties.v1.CoachesPropertyDefinition.COACH_RATING = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_RATING = 7;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 377.

```text
T_SELECTED_COACH_ID = 4;
  LAST_SELECTED_COACH_DATE = 5;
  TOTAL_GAMES_STARTED_AGAINST_COACH = 6;
  COACH_RATING = 7;
  CURRENT_COACH_NAME = 8;
  CURRENT_COACH_ID = 9;
  TOTAL_COACH_GAMES = 10;
  HAS_SELECTED_COACH = 11;
  INITIAL_CHOSEN_COACH = 12;
  INITIAL_COACH = 13;
  LAST_GAME_VS_COACH_FINISHED = 14;
}

message CoachesProperty {
  oneof _default_coach_name {
  string default_coach_name = 1;
  }
  oneof _default
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10211"></a>
## FND-10211: chesscom.user_properties.v1.CoachesPropertyDefinition.CURRENT_COACH_NAME = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CURRENT_COACH_NAME = 8;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 397.

```text
= 4;
  LAST_SELECTED_COACH_DATE = 5;
  TOTAL_GAMES_STARTED_AGAINST_COACH = 6;
  COACH_RATING = 7;
  CURRENT_COACH_NAME = 8;
  CURRENT_COACH_ID = 9;
  TOTAL_COACH_GAMES = 10;
  HAS_SELECTED_COACH = 11;
  INITIAL_CHOSEN_COACH = 12;
  INITIAL_COACH = 13;
  LAST_GAME_VS_COACH_FINISHED = 14;
}

message CoachesProperty {
  oneof _default_coach_name {
  string default_coach_name = 1;
  }
  oneof _default_coach_id {
  string
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10212"></a>
## FND-10212: chesscom.user_properties.v1.CoachesPropertyDefinition.CURRENT_COACH_ID = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CURRENT_COACH_ID = 9;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 423.

```text
_DATE = 5;
  TOTAL_GAMES_STARTED_AGAINST_COACH = 6;
  COACH_RATING = 7;
  CURRENT_COACH_NAME = 8;
  CURRENT_COACH_ID = 9;
  TOTAL_COACH_GAMES = 10;
  HAS_SELECTED_COACH = 11;
  INITIAL_CHOSEN_COACH = 12;
  INITIAL_COACH = 13;
  LAST_GAME_VS_COACH_FINISHED = 14;
}

message CoachesProperty {
  oneof _default_coach_name {
  string default_coach_name = 1;
  }
  oneof _default_coach_id {
  string default_coach_id = 2;
  }
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10213"></a>
## FND-10213: chesscom.user_properties.v1.CoachesPropertyDefinition.TOTAL_COACH_GAMES = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_COACH_GAMES = 10;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 447.

```text
_STARTED_AGAINST_COACH = 6;
  COACH_RATING = 7;
  CURRENT_COACH_NAME = 8;
  CURRENT_COACH_ID = 9;
  TOTAL_COACH_GAMES = 10;
  HAS_SELECTED_COACH = 11;
  INITIAL_CHOSEN_COACH = 12;
  INITIAL_COACH = 13;
  LAST_GAME_VS_COACH_FINISHED = 14;
}

message CoachesProperty {
  oneof _default_coach_name {
  string default_coach_name = 1;
  }
  oneof _default_coach_id {
  string default_coach_id = 2;
  }
  oneof _last_selected_
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10214"></a>
## FND-10214: chesscom.user_properties.v1.CoachesPropertyDefinition.HAS_SELECTED_COACH = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

HAS_SELECTED_COACH = 11;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 473.

```text
;
  COACH_RATING = 7;
  CURRENT_COACH_NAME = 8;
  CURRENT_COACH_ID = 9;
  TOTAL_COACH_GAMES = 10;
  HAS_SELECTED_COACH = 11;
  INITIAL_CHOSEN_COACH = 12;
  INITIAL_COACH = 13;
  LAST_GAME_VS_COACH_FINISHED = 14;
}

message CoachesProperty {
  oneof _default_coach_name {
  string default_coach_name = 1;
  }
  oneof _default_coach_id {
  string default_coach_id = 2;
  }
  oneof _last_selected_coach_name {
  string last
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10215"></a>
## FND-10215: chesscom.user_properties.v1.CoachesPropertyDefinition.INITIAL_CHOSEN_COACH = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INITIAL_CHOSEN_COACH = 12;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 500.

```text
RENT_COACH_NAME = 8;
  CURRENT_COACH_ID = 9;
  TOTAL_COACH_GAMES = 10;
  HAS_SELECTED_COACH = 11;
  INITIAL_CHOSEN_COACH = 12;
  INITIAL_COACH = 13;
  LAST_GAME_VS_COACH_FINISHED = 14;
}

message CoachesProperty {
  oneof _default_coach_name {
  string default_coach_name = 1;
  }
  oneof _default_coach_id {
  string default_coach_id = 2;
  }
  oneof _last_selected_coach_name {
  string last_selected_coach_name = 3;
 
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10216"></a>
## FND-10216: chesscom.user_properties.v1.CoachesPropertyDefinition.INITIAL_COACH = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INITIAL_COACH = 13;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 529.

```text
T_COACH_ID = 9;
  TOTAL_COACH_GAMES = 10;
  HAS_SELECTED_COACH = 11;
  INITIAL_CHOSEN_COACH = 12;
  INITIAL_COACH = 13;
  LAST_GAME_VS_COACH_FINISHED = 14;
}

message CoachesProperty {
  oneof _default_coach_name {
  string default_coach_name = 1;
  }
  oneof _default_coach_id {
  string default_coach_id = 2;
  }
  oneof _last_selected_coach_name {
  string last_selected_coach_name = 3;
  }
  oneof _last_selected_coa
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10217"></a>
## FND-10217: chesscom.user_properties.v1.CoachesPropertyDefinition.LAST_GAME_VS_COACH_FINISHED = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_GAME_VS_COACH_FINISHED = 14;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 551.

```text
L_COACH_GAMES = 10;
  HAS_SELECTED_COACH = 11;
  INITIAL_CHOSEN_COACH = 12;
  INITIAL_COACH = 13;
  LAST_GAME_VS_COACH_FINISHED = 14;
}

message CoachesProperty {
  oneof _default_coach_name {
  string default_coach_name = 1;
  }
  oneof _default_coach_id {
  string default_coach_id = 2;
  }
  oneof _last_selected_coach_name {
  string last_selected_coach_name = 3;
  }
  oneof _last_selected_coach_id {
  string last_
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10218"></a>
## FND-10218: message declaration: chesscom.user_properties.v1.CoachesProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachesProperty {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 588.

```text
ACH = 11;
  INITIAL_CHOSEN_COACH = 12;
  INITIAL_COACH = 13;
  LAST_GAME_VS_COACH_FINISHED = 14;
}

message CoachesProperty {
  oneof _default_coach_name {
  string default_coach_name = 1;
  }
  oneof _default_coach_id {
  string default_coach_id = 2;
  }
  oneof _last_selected_coach_name {
  string last_selected_coach_name = 3;
  }
  oneof _last_selected_coach_id {
  string last_selected_coach_id = 4;
  }
  oneof _l
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10219"></a>
## FND-10219: oneof declaration: chesscom.user_properties.v1.CoachesProperty._default_coach_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _default_coach_name {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 616.

```text
OACH = 12;
  INITIAL_COACH = 13;
  LAST_GAME_VS_COACH_FINISHED = 14;
}

message CoachesProperty {
  oneof _default_coach_name {
  string default_coach_name = 1;
  }
  oneof _default_coach_id {
  string default_coach_id = 2;
  }
  oneof _last_selected_coach_name {
  string last_selected_coach_name = 3;
  }
  oneof _last_selected_coach_id {
  string last_selected_coach_id = 4;
  }
  oneof _last_selected_coach_date {
  
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10220"></a>
## FND-10220: chesscom.user_properties.v1.CoachesProperty.default_coach_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string default_coach_name = 1;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 646.

```text
3;
  LAST_GAME_VS_COACH_FINISHED = 14;
}

message CoachesProperty {
  oneof _default_coach_name {
  string default_coach_name = 1;
  }
  oneof _default_coach_id {
  string default_coach_id = 2;
  }
  oneof _last_selected_coach_name {
  string last_selected_coach_name = 3;
  }
  oneof _last_selected_coach_id {
  string last_selected_coach_id = 4;
  }
  oneof _last_selected_coach_date {
  .google.protobuf.Timestamp las
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10221"></a>
## FND-10221: oneof declaration: chesscom.user_properties.v1.CoachesProperty._default_coach_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _default_coach_id {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 683.

```text
;
}

message CoachesProperty {
  oneof _default_coach_name {
  string default_coach_name = 1;
  }
  oneof _default_coach_id {
  string default_coach_id = 2;
  }
  oneof _last_selected_coach_name {
  string last_selected_coach_name = 3;
  }
  oneof _last_selected_coach_id {
  string last_selected_coach_id = 4;
  }
  oneof _last_selected_coach_date {
  .google.protobuf.Timestamp last_selected_coach_date = 5;
  }
  oneo
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10222"></a>
## FND-10222: chesscom.user_properties.v1.CoachesProperty.default_coach_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string default_coach_id = 2;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 711.

```text
 {
  oneof _default_coach_name {
  string default_coach_name = 1;
  }
  oneof _default_coach_id {
  string default_coach_id = 2;
  }
  oneof _last_selected_coach_name {
  string last_selected_coach_name = 3;
  }
  oneof _last_selected_coach_id {
  string last_selected_coach_id = 4;
  }
  oneof _last_selected_coach_date {
  .google.protobuf.Timestamp last_selected_coach_date = 5;
  }
  oneof _total_games_started_again
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10223"></a>
## FND-10223: oneof declaration: chesscom.user_properties.v1.CoachesProperty._last_selected_coach_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_selected_coach_name {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 746.

```text
string default_coach_name = 1;
  }
  oneof _default_coach_id {
  string default_coach_id = 2;
  }
  oneof _last_selected_coach_name {
  string last_selected_coach_name = 3;
  }
  oneof _last_selected_coach_id {
  string last_selected_coach_id = 4;
  }
  oneof _last_selected_coach_date {
  .google.protobuf.Timestamp last_selected_coach_date = 5;
  }
  oneof _total_games_started_against_coach {
  int32 total_games_star
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10224"></a>
## FND-10224: chesscom.user_properties.v1.CoachesProperty.last_selected_coach_name = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_selected_coach_name = 3;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 782.

```text
 oneof _default_coach_id {
  string default_coach_id = 2;
  }
  oneof _last_selected_coach_name {
  string last_selected_coach_name = 3;
  }
  oneof _last_selected_coach_id {
  string last_selected_coach_id = 4;
  }
  oneof _last_selected_coach_date {
  .google.protobuf.Timestamp last_selected_coach_date = 5;
  }
  oneof _total_games_started_against_coach {
  int32 total_games_started_against_coach = 6;
  }
  oneof _
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10225"></a>
## FND-10225: oneof declaration: chesscom.user_properties.v1.CoachesProperty._last_selected_coach_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_selected_coach_id {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 825.

```text
_coach_id = 2;
  }
  oneof _last_selected_coach_name {
  string last_selected_coach_name = 3;
  }
  oneof _last_selected_coach_id {
  string last_selected_coach_id = 4;
  }
  oneof _last_selected_coach_date {
  .google.protobuf.Timestamp last_selected_coach_date = 5;
  }
  oneof _total_games_started_against_coach {
  int32 total_games_started_against_coach = 6;
  }
  oneof _coach_rating {
  int32 coach_rating = 7;
  
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10226"></a>
## FND-10226: chesscom.user_properties.v1.CoachesProperty.last_selected_coach_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_selected_coach_id = 4;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 859.

```text
elected_coach_name {
  string last_selected_coach_name = 3;
  }
  oneof _last_selected_coach_id {
  string last_selected_coach_id = 4;
  }
  oneof _last_selected_coach_date {
  .google.protobuf.Timestamp last_selected_coach_date = 5;
  }
  oneof _total_games_started_against_coach {
  int32 total_games_started_against_coach = 6;
  }
  oneof _coach_rating {
  int32 coach_rating = 7;
  }
  oneof _current_coach_name {
  
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10227"></a>
## FND-10227: oneof declaration: chesscom.user_properties.v1.CoachesProperty._last_selected_coach_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_selected_coach_date {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 900.

```text
ed_coach_name = 3;
  }
  oneof _last_selected_coach_id {
  string last_selected_coach_id = 4;
  }
  oneof _last_selected_coach_date {
  .google.protobuf.Timestamp last_selected_coach_date = 5;
  }
  oneof _total_games_started_against_coach {
  int32 total_games_started_against_coach = 6;
  }
  oneof _coach_rating {
  int32 coach_rating = 7;
  }
  oneof _current_coach_name {
  string current_coach_name = 8;
  }
  oneo
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10228"></a>
## FND-10228: chesscom.user_properties.v1.CoachesProperty.last_selected_coach_date = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_selected_coach_date = 5;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 936.

```text
_selected_coach_id {
  string last_selected_coach_id = 4;
  }
  oneof _last_selected_coach_date {
  .google.protobuf.Timestamp last_selected_coach_date = 5;
  }
  oneof _total_games_started_against_coach {
  int32 total_games_started_against_coach = 6;
  }
  oneof _coach_rating {
  int32 coach_rating = 7;
  }
  oneof _current_coach_name {
  string current_coach_name = 8;
  }
  oneof _curent_coach_id {
  string curent
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10229"></a>
## FND-10229: oneof declaration: chesscom.user_properties.v1.CoachesProperty._total_games_started_against_coach

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_games_started_against_coach {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 999.

```text
 oneof _last_selected_coach_date {
  .google.protobuf.Timestamp last_selected_coach_date = 5;
  }
  oneof _total_games_started_against_coach {
  int32 total_games_started_against_coach = 6;
  }
  oneof _coach_rating {
  int32 coach_rating = 7;
  }
  oneof _current_coach_name {
  string current_coach_name = 8;
  }
  oneof _curent_coach_id {
  string curent_coach_id = 9;
  }
  oneof _total_coach_games {
  int32 total_c
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10230"></a>
## FND-10230: chesscom.user_properties.v1.CoachesProperty.total_games_started_against_coach = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_games_started_against_coach = 6;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1044.

```text
protobuf.Timestamp last_selected_coach_date = 5;
  }
  oneof _total_games_started_against_coach {
  int32 total_games_started_against_coach = 6;
  }
  oneof _coach_rating {
  int32 coach_rating = 7;
  }
  oneof _current_coach_name {
  string current_coach_name = 8;
  }
  oneof _curent_coach_id {
  string curent_coach_id = 9;
  }
  oneof _total_coach_games {
  int32 total_coach_games = 10;
  }
  oneof _has_selected_co
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10231"></a>
## FND-10231: oneof declaration: chesscom.user_properties.v1.CoachesProperty._coach_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _coach_rating {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1095.

```text
}
  oneof _total_games_started_against_coach {
  int32 total_games_started_against_coach = 6;
  }
  oneof _coach_rating {
  int32 coach_rating = 7;
  }
  oneof _current_coach_name {
  string current_coach_name = 8;
  }
  oneof _curent_coach_id {
  string curent_coach_id = 9;
  }
  oneof _total_coach_games {
  int32 total_coach_games = 10;
  }
  oneof _has_selected_coach {
  bool has_selected_coach = 11;
  }
  oneof _
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10232"></a>
## FND-10232: chesscom.user_properties.v1.CoachesProperty.coach_rating = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 coach_rating = 7;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1119.

```text
tarted_against_coach {
  int32 total_games_started_against_coach = 6;
  }
  oneof _coach_rating {
  int32 coach_rating = 7;
  }
  oneof _current_coach_name {
  string current_coach_name = 8;
  }
  oneof _curent_coach_id {
  string curent_coach_id = 9;
  }
  oneof _total_coach_games {
  int32 total_coach_games = 10;
  }
  oneof _has_selected_coach {
  bool has_selected_coach = 11;
  }
  oneof _initial_chosen_coach {
 
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10233"></a>
## FND-10233: oneof declaration: chesscom.user_properties.v1.CoachesProperty._current_coach_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _current_coach_name {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1149.

```text
 total_games_started_against_coach = 6;
  }
  oneof _coach_rating {
  int32 coach_rating = 7;
  }
  oneof _current_coach_name {
  string current_coach_name = 8;
  }
  oneof _curent_coach_id {
  string curent_coach_id = 9;
  }
  oneof _total_coach_games {
  int32 total_coach_games = 10;
  }
  oneof _has_selected_coach {
  bool has_selected_coach = 11;
  }
  oneof _initial_chosen_coach {
  string initial_chosen_coach =
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10234"></a>
## FND-10234: chesscom.user_properties.v1.CoachesProperty.current_coach_name = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string current_coach_name = 8;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1179.

```text
oach = 6;
  }
  oneof _coach_rating {
  int32 coach_rating = 7;
  }
  oneof _current_coach_name {
  string current_coach_name = 8;
  }
  oneof _curent_coach_id {
  string curent_coach_id = 9;
  }
  oneof _total_coach_games {
  int32 total_coach_games = 10;
  }
  oneof _has_selected_coach {
  bool has_selected_coach = 11;
  }
  oneof _initial_chosen_coach {
  string initial_chosen_coach = 12;
  }
  oneof _initial_coac
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10235"></a>
## FND-10235: oneof declaration: chesscom.user_properties.v1.CoachesProperty._curent_coach_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _curent_coach_id {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1216.

```text

  int32 coach_rating = 7;
  }
  oneof _current_coach_name {
  string current_coach_name = 8;
  }
  oneof _curent_coach_id {
  string curent_coach_id = 9;
  }
  oneof _total_coach_games {
  int32 total_coach_games = 10;
  }
  oneof _has_selected_coach {
  bool has_selected_coach = 11;
  }
  oneof _initial_chosen_coach {
  string initial_chosen_coach = 12;
  }
  oneof _initial_coach {
  string initial_coach = 13;
  }

```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10236"></a>
## FND-10236: chesscom.user_properties.v1.CoachesProperty.curent_coach_id = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string curent_coach_id = 9;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1243.

```text
  }
  oneof _current_coach_name {
  string current_coach_name = 8;
  }
  oneof _curent_coach_id {
  string curent_coach_id = 9;
  }
  oneof _total_coach_games {
  int32 total_coach_games = 10;
  }
  oneof _has_selected_coach {
  bool has_selected_coach = 11;
  }
  oneof _initial_chosen_coach {
  string initial_chosen_coach = 12;
  }
  oneof _initial_coach {
  string initial_coach = 13;
  }
  oneof _last_game_vs_coach
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10237"></a>
## FND-10237: oneof declaration: chesscom.user_properties.v1.CoachesProperty._total_coach_games

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_coach_games {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1277.

```text
  string current_coach_name = 8;
  }
  oneof _curent_coach_id {
  string curent_coach_id = 9;
  }
  oneof _total_coach_games {
  int32 total_coach_games = 10;
  }
  oneof _has_selected_coach {
  bool has_selected_coach = 11;
  }
  oneof _initial_chosen_coach {
  string initial_chosen_coach = 12;
  }
  oneof _initial_coach {
  string initial_coach = 13;
  }
  oneof _last_game_vs_coach_finished {
  .google.protobuf.Tim
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10238"></a>
## FND-10238: chesscom.user_properties.v1.CoachesProperty.total_coach_games = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_coach_games = 10;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1306.

```text
 8;
  }
  oneof _curent_coach_id {
  string curent_coach_id = 9;
  }
  oneof _total_coach_games {
  int32 total_coach_games = 10;
  }
  oneof _has_selected_coach {
  bool has_selected_coach = 11;
  }
  oneof _initial_chosen_coach {
  string initial_chosen_coach = 12;
  }
  oneof _initial_coach {
  string initial_coach = 13;
  }
  oneof _last_game_vs_coach_finished {
  .google.protobuf.Timestamp last_game_vs_coach_fin
```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10239"></a>
## FND-10239: oneof declaration: chesscom.user_properties.v1.CoachesProperty._has_selected_coach

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _has_selected_coach {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1342.

```text
 string curent_coach_id = 9;
  }
  oneof _total_coach_games {
  int32 total_coach_games = 10;
  }
  oneof _has_selected_coach {
  bool has_selected_coach = 11;
  }
  oneof _initial_chosen_coach {
  string initial_chosen_coach = 12;
  }
  oneof _initial_coach {
  string initial_coach = 13;
  }
  oneof _last_game_vs_coach_finished {
  .google.protobuf.Timestamp last_game_vs_coach_finished = 14;
  }
}

```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10240"></a>
## FND-10240: chesscom.user_properties.v1.CoachesProperty.has_selected_coach = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool has_selected_coach = 11;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1372.

```text
 }
  oneof _total_coach_games {
  int32 total_coach_games = 10;
  }
  oneof _has_selected_coach {
  bool has_selected_coach = 11;
  }
  oneof _initial_chosen_coach {
  string initial_chosen_coach = 12;
  }
  oneof _initial_coach {
  string initial_coach = 13;
  }
  oneof _last_game_vs_coach_finished {
  .google.protobuf.Timestamp last_game_vs_coach_finished = 14;
  }
}

```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10241"></a>
## FND-10241: oneof declaration: chesscom.user_properties.v1.CoachesProperty._initial_chosen_coach

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _initial_chosen_coach {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1408.

```text
t32 total_coach_games = 10;
  }
  oneof _has_selected_coach {
  bool has_selected_coach = 11;
  }
  oneof _initial_chosen_coach {
  string initial_chosen_coach = 12;
  }
  oneof _initial_coach {
  string initial_coach = 13;
  }
  oneof _last_game_vs_coach_finished {
  .google.protobuf.Timestamp last_game_vs_coach_finished = 14;
  }
}

```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10242"></a>
## FND-10242: chesscom.user_properties.v1.CoachesProperty.initial_chosen_coach = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string initial_chosen_coach = 12;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1440.

```text
  oneof _has_selected_coach {
  bool has_selected_coach = 11;
  }
  oneof _initial_chosen_coach {
  string initial_chosen_coach = 12;
  }
  oneof _initial_coach {
  string initial_coach = 13;
  }
  oneof _last_game_vs_coach_finished {
  .google.protobuf.Timestamp last_game_vs_coach_finished = 14;
  }
}

```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10243"></a>
## FND-10243: oneof declaration: chesscom.user_properties.v1.CoachesProperty._initial_coach

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _initial_coach {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1480.

```text
_selected_coach = 11;
  }
  oneof _initial_chosen_coach {
  string initial_chosen_coach = 12;
  }
  oneof _initial_coach {
  string initial_coach = 13;
  }
  oneof _last_game_vs_coach_finished {
  .google.protobuf.Timestamp last_game_vs_coach_finished = 14;
  }
}

```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10244"></a>
## FND-10244: chesscom.user_properties.v1.CoachesProperty.initial_coach = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string initial_coach = 13;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1505.

```text

  oneof _initial_chosen_coach {
  string initial_chosen_coach = 12;
  }
  oneof _initial_coach {
  string initial_coach = 13;
  }
  oneof _last_game_vs_coach_finished {
  .google.protobuf.Timestamp last_game_vs_coach_finished = 14;
  }
}

```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10245"></a>
## FND-10245: oneof declaration: chesscom.user_properties.v1.CoachesProperty._last_game_vs_coach_finished

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_game_vs_coach_finished {

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1538.

```text
  string initial_chosen_coach = 12;
  }
  oneof _initial_coach {
  string initial_coach = 13;
  }
  oneof _last_game_vs_coach_finished {
  .google.protobuf.Timestamp last_game_vs_coach_finished = 14;
  }
}

```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10246"></a>
## FND-10246: chesscom.user_properties.v1.CoachesProperty.last_game_vs_coach_finished = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_game_vs_coach_finished = 14;

### Evidence

- **SRC-0606** `research/proto/chesscom/user_properties/v1/properties_coaches.proto` — [preserved redacted evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto)
  Character offset 1577.

```text

  oneof _initial_coach {
  string initial_coach = 13;
  }
  oneof _last_game_vs_coach_finished {
  .google.protobuf.Timestamp last_game_vs_coach_finished = 14;
  }
}

```

**Source references:** SRC-0606, SRC-1577  
**URL references:** None independently associated  
**Related findings:** FND-10202, FND-10203, FND-10204

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10247"></a>
## FND-10247: enum declaration: chesscom.user_properties.v1.CorePropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CorePropertyDefinition {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 118.

```text
m/user_properties/v1/properties_core.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum CorePropertyDefinition {
  CORE_PROPERTY_UNSPECIFIED = 0;
  USER_ID = 1;
  USERNAME = 2;
  TYPE = 3;
  CREATED_AT = 4;
  UPDATED_AT = 5;
  TIMEZONE = 6;
  CHESS_TITLE = 7;
  FLAIR_CODE = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL 
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10248"></a>
## FND-10248: chesscom.user_properties.v1.CorePropertyDefinition.CORE_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CORE_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 150.

```text
core.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum CorePropertyDefinition {
  CORE_PROPERTY_UNSPECIFIED = 0;
  USER_ID = 1;
  USERNAME = 2;
  TYPE = 3;
  CREATED_AT = 4;
  UPDATED_AT = 5;
  TIMEZONE = 6;
  CHESS_TITLE = 7;
  FLAIR_CODE = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10249"></a>
## FND-10249: chesscom.user_properties.v1.CorePropertyDefinition.USER_ID = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_ID = 1;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 183.

```text
kage chesscom.user_properties.v1;

enum CorePropertyDefinition {
  CORE_PROPERTY_UNSPECIFIED = 0;
  USER_ID = 1;
  USERNAME = 2;
  TYPE = 3;
  CREATED_AT = 4;
  UPDATED_AT = 5;
  TIMEZONE = 6;
  CHESS_TITLE = 7;
  FLAIR_CODE = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  o
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10250"></a>
## FND-10250: chesscom.user_properties.v1.CorePropertyDefinition.USERNAME = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USERNAME = 2;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 198.

```text
ser_properties.v1;

enum CorePropertyDefinition {
  CORE_PROPERTY_UNSPECIFIED = 0;
  USER_ID = 1;
  USERNAME = 2;
  TYPE = 3;
  CREATED_AT = 4;
  UPDATED_AT = 5;
  TIMEZONE = 6;
  CHESS_TITLE = 7;
  FLAIR_CODE = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10251"></a>
## FND-10251: chesscom.user_properties.v1.CorePropertyDefinition.TYPE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TYPE = 3;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 214.

```text
1;

enum CorePropertyDefinition {
  CORE_PROPERTY_UNSPECIFIED = 0;
  USER_ID = 1;
  USERNAME = 2;
  TYPE = 3;
  CREATED_AT = 4;
  UPDATED_AT = 5;
  TIMEZONE = 6;
  CHESS_TITLE = 7;
  FLAIR_CODE = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_i
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10252"></a>
## FND-10252: chesscom.user_properties.v1.CorePropertyDefinition.CREATED_AT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CREATED_AT = 4;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 226.

```text
ePropertyDefinition {
  CORE_PROPERTY_UNSPECIFIED = 0;
  USER_ID = 1;
  USERNAME = 2;
  TYPE = 3;
  CREATED_AT = 4;
  UPDATED_AT = 5;
  TIMEZONE = 6;
  CHESS_TITLE = 7;
  FLAIR_CODE = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
 
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10253"></a>
## FND-10253: chesscom.user_properties.v1.CorePropertyDefinition.UPDATED_AT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

UPDATED_AT = 5;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 244.

```text
n {
  CORE_PROPERTY_UNSPECIFIED = 0;
  USER_ID = 1;
  USERNAME = 2;
  TYPE = 3;
  CREATED_AT = 4;
  UPDATED_AT = 5;
  TIMEZONE = 6;
  CHESS_TITLE = 7;
  FLAIR_CODE = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10254"></a>
## FND-10254: chesscom.user_properties.v1.CorePropertyDefinition.TIMEZONE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIMEZONE = 6;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 262.

```text
Y_UNSPECIFIED = 0;
  USER_ID = 1;
  USERNAME = 2;
  TYPE = 3;
  CREATED_AT = 4;
  UPDATED_AT = 5;
  TIMEZONE = 6;
  CHESS_TITLE = 7;
  FLAIR_CODE = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10255"></a>
## FND-10255: chesscom.user_properties.v1.CorePropertyDefinition.CHESS_TITLE = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESS_TITLE = 7;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 278.

```text
0;
  USER_ID = 1;
  USERNAME = 2;
  TYPE = 3;
  CREATED_AT = 4;
  UPDATED_AT = 5;
  TIMEZONE = 6;
  CHESS_TITLE = 7;
  FLAIR_CODE = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneo
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10256"></a>
## FND-10256: chesscom.user_properties.v1.CorePropertyDefinition.FLAIR_CODE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FLAIR_CODE = 8;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 297.

```text
 USERNAME = 2;
  TYPE = 3;
  CREATED_AT = 4;
  UPDATED_AT = 5;
  TIMEZONE = 6;
  CHESS_TITLE = 7;
  FLAIR_CODE = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string 
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10257"></a>
## FND-10257: chesscom.user_properties.v1.CorePropertyDefinition.IS_ENABLED = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_ENABLED = 9;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 315.

```text
YPE = 3;
  CREATED_AT = 4;
  UPDATED_AT = 5;
  TIMEZONE = 6;
  CHESS_TITLE = 7;
  FLAIR_CODE = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  on
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10258"></a>
## FND-10258: chesscom.user_properties.v1.CorePropertyDefinition.BITSET_OFFSET_NUMBER = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BITSET_OFFSET_NUMBER = 10;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 333.

```text
_AT = 4;
  UPDATED_AT = 5;
  TIMEZONE = 6;
  CHESS_TITLE = 7;
  FLAIR_CODE = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {

```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10259"></a>
## FND-10259: chesscom.user_properties.v1.CorePropertyDefinition.USER_UUID = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_UUID = 11;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 362.

```text
TIMEZONE = 6;
  CHESS_TITLE = 7;
  FLAIR_CODE = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp 
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10260"></a>
## FND-10260: chesscom.user_properties.v1.CorePropertyDefinition.PREVIOUS_USERNAMES = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREVIOUS_USERNAMES = 12;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 380.

```text
ESS_TITLE = 7;
  FLAIR_CODE = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10261"></a>
## FND-10261: chesscom.user_properties.v1.CorePropertyDefinition.FLAIR_ID = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FLAIR_ID = 13;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 407.

```text
 = 8;
  IS_ENABLED = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  }
  oneof _updated_at {
  .
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10262"></a>
## FND-10262: chesscom.user_properties.v1.CorePropertyDefinition.FLAIR_PNG_URL = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FLAIR_PNG_URL = 14;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 424.

```text
D = 9;
  BITSET_OFFSET_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  }
  oneof _updated_at {
  .google.protobuf.T
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10263"></a>
## FND-10263: chesscom.user_properties.v1.CorePropertyDefinition.REGISTRATION_PLATFORM = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

REGISTRATION_PLATFORM = 15;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 446.

```text
_NUMBER = 10;
  USER_UUID = 11;
  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  }
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10264"></a>
## FND-10264: message declaration: chesscom.user_properties.v1.CoreProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoreProperty {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 477.

```text

  PREVIOUS_USERNAMES = 12;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  }
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 5;
  }
  oneof _timezone {
  st
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10265"></a>
## FND-10265: oneof declaration: chesscom.user_properties.v1.CoreProperty._user_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_id {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 502.

```text
2;
  FLAIR_ID = 13;
  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  }
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 5;
  }
  oneof _timezone {
  string timezone = 6;
  }
  
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10266"></a>
## FND-10266: chesscom.user_properties.v1.CoreProperty.user_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint64 user_id = 1;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 521.

```text

  FLAIR_PNG_URL = 14;
  REGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  }
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 5;
  }
  oneof _timezone {
  string timezone = 6;
  }
  oneof _chess_title 
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10267"></a>
## FND-10267: oneof declaration: chesscom.user_properties.v1.CoreProperty._username

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _username {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 547.

```text
EGISTRATION_PLATFORM = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  }
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 5;
  }
  oneof _timezone {
  string timezone = 6;
  }
  oneof _chess_title {
  string chess_title = 7
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10268"></a>
## FND-10268: chesscom.user_properties.v1.CoreProperty.username = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string username = 2;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 567.

```text
 = 15;
}

message CoreProperty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  }
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 5;
  }
  oneof _timezone {
  string timezone = 6;
  }
  oneof _chess_title {
  string chess_title = 7;
  }
  oneof _flair
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10269"></a>
## FND-10269: oneof declaration: chesscom.user_properties.v1.CoreProperty._type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _type {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 594.

```text
rty {
  oneof _user_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  }
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 5;
  }
  oneof _timezone {
  string timezone = 6;
  }
  oneof _chess_title {
  string chess_title = 7;
  }
  oneof _flair_code {
  string flair_code
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10270"></a>
## FND-10270: chesscom.user_properties.v1.CoreProperty.type = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string type = 3;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 610.

```text
ser_id {
  uint64 user_id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  }
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 5;
  }
  oneof _timezone {
  string timezone = 6;
  }
  oneof _chess_title {
  string chess_title = 7;
  }
  oneof _flair_code {
  string flair_code = 8;
  }
  oneo
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10271"></a>
## FND-10271: oneof declaration: chesscom.user_properties.v1.CoreProperty._created_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _created_at {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 633.

```text
id = 1;
  }
  oneof _username {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  }
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 5;
  }
  oneof _timezone {
  string timezone = 6;
  }
  oneof _chess_title {
  string chess_title = 7;
  }
  oneof _flair_code {
  string flair_code = 8;
  }
  oneof _is_enabled {
  bool 
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10272"></a>
## FND-10272: chesscom.user_properties.v1.CoreProperty.created_at = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp created_at = 4;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 655.

```text
sername {
  string username = 2;
  }
  oneof _type {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  }
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 5;
  }
  oneof _timezone {
  string timezone = 6;
  }
  oneof _chess_title {
  string chess_title = 7;
  }
  oneof _flair_code {
  string flair_code = 8;
  }
  oneof _is_enabled {
  bool is_enabled = 9;
  }
  
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10273"></a>
## FND-10273: oneof declaration: chesscom.user_properties.v1.CoreProperty._updated_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _updated_at {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 704.

```text
e {
  string type = 3;
  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  }
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 5;
  }
  oneof _timezone {
  string timezone = 6;
  }
  oneof _chess_title {
  string chess_title = 7;
  }
  oneof _flair_code {
  string flair_code = 8;
  }
  oneof _is_enabled {
  bool is_enabled = 9;
  }
  oneof _bitset_offset_number {
  int64 bitset_offs
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10274"></a>
## FND-10274: chesscom.user_properties.v1.CoreProperty.updated_at = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp updated_at = 5;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 726.

```text

  }
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 4;
  }
  oneof _updated_at {
  .google.protobuf.Timestamp updated_at = 5;
  }
  oneof _timezone {
  string timezone = 6;
  }
  oneof _chess_title {
  string chess_title = 7;
  }
  oneof _flair_code {
  string flair_code = 8;
  }
  oneof _is_enabled {
  bool is_enabled = 9;
  }
  oneof _bitset_offset_number {
  int64 bitset_offset_number = 10;
  }
  
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
