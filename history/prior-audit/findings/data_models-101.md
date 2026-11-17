# data_models — findings 10001–10100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-10275"></a>
## FND-10275: oneof declaration: chesscom.user_properties.v1.CoreProperty._timezone

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _timezone {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 775.

```text
estamp created_at = 4;
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
  oneof _user_uuid {
  string user_uuid = 11;
  }
 
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10276"></a>
## FND-10276: chesscom.user_properties.v1.CoreProperty.timezone = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string timezone = 6;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 795.

```text
4;
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
  oneof _user_uuid {
  string user_uuid = 11;
  }
  oneof _flair_id {
 
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10277"></a>
## FND-10277: oneof declaration: chesscom.user_properties.v1.CoreProperty._chess_title

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _chess_title {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 822.

```text
{
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
  oneof _user_uuid {
  string user_uuid = 11;
  }
  oneof _flair_id {
  string flair_id = 13;
  }

```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10278"></a>
## FND-10278: chesscom.user_properties.v1.CoreProperty.chess_title = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string chess_title = 7;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 845.

```text
mestamp updated_at = 5;
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
  oneof _user_uuid {
  string user_uuid = 11;
  }
  oneof _flair_id {
  string flair_id = 13;
  }
  oneof _flair_png_url 
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10279"></a>
## FND-10279: oneof declaration: chesscom.user_properties.v1.CoreProperty._flair_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _flair_code {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 875.

```text
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
  oneof _user_uuid {
  string user_uuid = 11;
  }
  oneof _flair_id {
  string flair_id = 13;
  }
  oneof _flair_png_url {
  string flair_png_url = 14;
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10280"></a>
## FND-10280: chesscom.user_properties.v1.CoreProperty.flair_code = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string flair_code = 8;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 897.

```text
ring timezone = 6;
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
  oneof _user_uuid {
  string user_uuid = 11;
  }
  oneof _flair_id {
  string flair_id = 13;
  }
  oneof _flair_png_url {
  string flair_png_url = 14;
  }
  oneof _registra
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10281"></a>
## FND-10281: oneof declaration: chesscom.user_properties.v1.CoreProperty._is_enabled

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_enabled {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 926.

```text
f _chess_title {
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
  oneof _user_uuid {
  string user_uuid = 11;
  }
  oneof _flair_id {
  string flair_id = 13;
  }
  oneof _flair_png_url {
  string flair_png_url = 14;
  }
  oneof _registration_platform {
  string regi
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10282"></a>
## FND-10282: chesscom.user_properties.v1.CoreProperty.is_enabled = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_enabled = 9;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 948.

```text
ing chess_title = 7;
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
  oneof _user_uuid {
  string user_uuid = 11;
  }
  oneof _flair_id {
  string flair_id = 13;
  }
  oneof _flair_png_url {
  string flair_png_url = 14;
  }
  oneof _registration_platform {
  string registration_platform = 15
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10283"></a>
## FND-10283: oneof declaration: chesscom.user_properties.v1.CoreProperty._bitset_offset_number

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _bitset_offset_number {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 975.

```text
oneof _flair_code {
  string flair_code = 8;
  }
  oneof _is_enabled {
  bool is_enabled = 9;
  }
  oneof _bitset_offset_number {
  int64 bitset_offset_number = 10;
  }
  oneof _user_uuid {
  string user_uuid = 11;
  }
  oneof _flair_id {
  string flair_id = 13;
  }
  oneof _flair_png_url {
  string flair_png_url = 14;
  }
  oneof _registration_platform {
  string registration_platform = 15;
  }
  repeated string pre
```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10284"></a>
## FND-10284: chesscom.user_properties.v1.CoreProperty.bitset_offset_number = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 bitset_offset_number = 10;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 1007.

```text
ir_code = 8;
  }
  oneof _is_enabled {
  bool is_enabled = 9;
  }
  oneof _bitset_offset_number {
  int64 bitset_offset_number = 10;
  }
  oneof _user_uuid {
  string user_uuid = 11;
  }
  oneof _flair_id {
  string flair_id = 13;
  }
  oneof _flair_png_url {
  string flair_png_url = 14;
  }
  oneof _registration_platform {
  string registration_platform = 15;
  }
  repeated string previous_usernames = 12;
}

```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10285"></a>
## FND-10285: oneof declaration: chesscom.user_properties.v1.CoreProperty._user_uuid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_uuid {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 1046.

```text
  bool is_enabled = 9;
  }
  oneof _bitset_offset_number {
  int64 bitset_offset_number = 10;
  }
  oneof _user_uuid {
  string user_uuid = 11;
  }
  oneof _flair_id {
  string flair_id = 13;
  }
  oneof _flair_png_url {
  string flair_png_url = 14;
  }
  oneof _registration_platform {
  string registration_platform = 15;
  }
  repeated string previous_usernames = 12;
}

```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10286"></a>
## FND-10286: chesscom.user_properties.v1.CoreProperty.user_uuid = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_uuid = 11;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 1067.

```text
;
  }
  oneof _bitset_offset_number {
  int64 bitset_offset_number = 10;
  }
  oneof _user_uuid {
  string user_uuid = 11;
  }
  oneof _flair_id {
  string flair_id = 13;
  }
  oneof _flair_png_url {
  string flair_png_url = 14;
  }
  oneof _registration_platform {
  string registration_platform = 15;
  }
  repeated string previous_usernames = 12;
}

```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10287"></a>
## FND-10287: oneof declaration: chesscom.user_properties.v1.CoreProperty._flair_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _flair_id {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 1096.

```text
number {
  int64 bitset_offset_number = 10;
  }
  oneof _user_uuid {
  string user_uuid = 11;
  }
  oneof _flair_id {
  string flair_id = 13;
  }
  oneof _flair_png_url {
  string flair_png_url = 14;
  }
  oneof _registration_platform {
  string registration_platform = 15;
  }
  repeated string previous_usernames = 12;
}

```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10288"></a>
## FND-10288: chesscom.user_properties.v1.CoreProperty.flair_id = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string flair_id = 13;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 1116.

```text
set_offset_number = 10;
  }
  oneof _user_uuid {
  string user_uuid = 11;
  }
  oneof _flair_id {
  string flair_id = 13;
  }
  oneof _flair_png_url {
  string flair_png_url = 14;
  }
  oneof _registration_platform {
  string registration_platform = 15;
  }
  repeated string previous_usernames = 12;
}

```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10289"></a>
## FND-10289: oneof declaration: chesscom.user_properties.v1.CoreProperty._flair_png_url

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _flair_png_url {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 1144.

```text
  oneof _user_uuid {
  string user_uuid = 11;
  }
  oneof _flair_id {
  string flair_id = 13;
  }
  oneof _flair_png_url {
  string flair_png_url = 14;
  }
  oneof _registration_platform {
  string registration_platform = 15;
  }
  repeated string previous_usernames = 12;
}

```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10290"></a>
## FND-10290: chesscom.user_properties.v1.CoreProperty.flair_png_url = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string flair_png_url = 14;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 1169.

```text
ring user_uuid = 11;
  }
  oneof _flair_id {
  string flair_id = 13;
  }
  oneof _flair_png_url {
  string flair_png_url = 14;
  }
  oneof _registration_platform {
  string registration_platform = 15;
  }
  repeated string previous_usernames = 12;
}

```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10291"></a>
## FND-10291: oneof declaration: chesscom.user_properties.v1.CoreProperty._registration_platform

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _registration_platform {

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 1202.

```text
_flair_id {
  string flair_id = 13;
  }
  oneof _flair_png_url {
  string flair_png_url = 14;
  }
  oneof _registration_platform {
  string registration_platform = 15;
  }
  repeated string previous_usernames = 12;
}

```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10292"></a>
## FND-10292: chesscom.user_properties.v1.CoreProperty.registration_platform = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string registration_platform = 15;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 1235.

```text
3;
  }
  oneof _flair_png_url {
  string flair_png_url = 14;
  }
  oneof _registration_platform {
  string registration_platform = 15;
  }
  repeated string previous_usernames = 12;
}

```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10293"></a>
## FND-10293: chesscom.user_properties.v1.CoreProperty.previous_usernames = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string previous_usernames = 12;

### Evidence

- **SRC-0607** `research/proto/chesscom/user_properties/v1/properties_core.proto` — [preserved redacted evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto)
  Character offset 1276.

```text
flair_png_url = 14;
  }
  oneof _registration_platform {
  string registration_platform = 15;
  }
  repeated string previous_usernames = 12;
}

```

**Source references:** SRC-0607, SRC-1578  
**URL references:** None independently associated  
**Related findings:** FND-10247, FND-10248, FND-10249

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10294"></a>
## FND-10294: enum declaration: chesscom.user_properties.v1.CoursesPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CoursesPropertyDefinition {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 121.

```text
ser_properties/v1/properties_courses.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum CoursesPropertyDefinition {
  COURSES_PROPERTY_UNSPECIFIED = 0;
  LAST_COURSE_PURCHASED_DATE = 1;
  LAST_COURSE_STUDY_DATE = 2;
  NUMBER_OF_COURSES_PURCHASED = 3;
  TOTAL_COURSES_SPENT = 4;
  NUMBER_OF_DIAMOND_COURSES_CLAIMED = 5;
  FIRST_COURSES_SESSION_DATE = 6;
  LAST_COURSES_SESSION_DATE = 7;
  NUMBER_OF_COURS
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10295"></a>
## FND-10295: chesscom.user_properties.v1.CoursesPropertyDefinition.COURSES_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSES_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 156.

```text
s.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum CoursesPropertyDefinition {
  COURSES_PROPERTY_UNSPECIFIED = 0;
  LAST_COURSE_PURCHASED_DATE = 1;
  LAST_COURSE_STUDY_DATE = 2;
  NUMBER_OF_COURSES_PURCHASED = 3;
  TOTAL_COURSES_SPENT = 4;
  NUMBER_OF_DIAMOND_COURSES_CLAIMED = 5;
  FIRST_COURSES_SESSION_DATE = 6;
  LAST_COURSES_SESSION_DATE = 7;
  NUMBER_OF_COURSES_REFUNDED = 8;
  NUMBER_OF_COURSE
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10296"></a>
## FND-10296: chesscom.user_properties.v1.CoursesPropertyDefinition.LAST_COURSE_PURCHASED_DATE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_COURSE_PURCHASED_DATE = 1;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 192.

```text
hesscom.user_properties.v1;

enum CoursesPropertyDefinition {
  COURSES_PROPERTY_UNSPECIFIED = 0;
  LAST_COURSE_PURCHASED_DATE = 1;
  LAST_COURSE_STUDY_DATE = 2;
  NUMBER_OF_COURSES_PURCHASED = 3;
  TOTAL_COURSES_SPENT = 4;
  NUMBER_OF_DIAMOND_COURSES_CLAIMED = 5;
  FIRST_COURSES_SESSION_DATE = 6;
  LAST_COURSES_SESSION_DATE = 7;
  NUMBER_OF_COURSES_REFUNDED = 8;
  NUMBER_OF_COURSES_VARIATIONS_LEARNED = 9;
  NUMBER_O
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10297"></a>
## FND-10297: chesscom.user_properties.v1.CoursesPropertyDefinition.LAST_COURSE_STUDY_DATE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_COURSE_STUDY_DATE = 2;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 226.

```text
CoursesPropertyDefinition {
  COURSES_PROPERTY_UNSPECIFIED = 0;
  LAST_COURSE_PURCHASED_DATE = 1;
  LAST_COURSE_STUDY_DATE = 2;
  NUMBER_OF_COURSES_PURCHASED = 3;
  TOTAL_COURSES_SPENT = 4;
  NUMBER_OF_DIAMOND_COURSES_CLAIMED = 5;
  FIRST_COURSES_SESSION_DATE = 6;
  LAST_COURSES_SESSION_DATE = 7;
  NUMBER_OF_COURSES_REFUNDED = 8;
  NUMBER_OF_COURSES_VARIATIONS_LEARNED = 9;
  NUMBER_OF_COURSES_REVIEWS_PENDING = 10;
  
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10298"></a>
## FND-10298: chesscom.user_properties.v1.CoursesPropertyDefinition.NUMBER_OF_COURSES_PURCHASED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_COURSES_PURCHASED = 3;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 256.

```text
COURSES_PROPERTY_UNSPECIFIED = 0;
  LAST_COURSE_PURCHASED_DATE = 1;
  LAST_COURSE_STUDY_DATE = 2;
  NUMBER_OF_COURSES_PURCHASED = 3;
  TOTAL_COURSES_SPENT = 4;
  NUMBER_OF_DIAMOND_COURSES_CLAIMED = 5;
  FIRST_COURSES_SESSION_DATE = 6;
  LAST_COURSES_SESSION_DATE = 7;
  NUMBER_OF_COURSES_REFUNDED = 8;
  NUMBER_OF_COURSES_VARIATIONS_LEARNED = 9;
  NUMBER_OF_COURSES_REVIEWS_PENDING = 10;
  NUMBER_OF_COURSES_VARIATIONS_R
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10299"></a>
## FND-10299: chesscom.user_properties.v1.CoursesPropertyDefinition.TOTAL_COURSES_SPENT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_COURSES_SPENT = 4;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 291.

```text
 LAST_COURSE_PURCHASED_DATE = 1;
  LAST_COURSE_STUDY_DATE = 2;
  NUMBER_OF_COURSES_PURCHASED = 3;
  TOTAL_COURSES_SPENT = 4;
  NUMBER_OF_DIAMOND_COURSES_CLAIMED = 5;
  FIRST_COURSES_SESSION_DATE = 6;
  LAST_COURSES_SESSION_DATE = 7;
  NUMBER_OF_COURSES_REFUNDED = 8;
  NUMBER_OF_COURSES_VARIATIONS_LEARNED = 9;
  NUMBER_OF_COURSES_REVIEWS_PENDING = 10;
  NUMBER_OF_COURSES_VARIATIONS_REVIEWED = 11;
  NUMBER_OF_COURSES_V
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10300"></a>
## FND-10300: chesscom.user_properties.v1.CoursesPropertyDefinition.NUMBER_OF_DIAMOND_COURSES_CLAIMED = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_DIAMOND_COURSES_CLAIMED = 5;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 318.

```text
 = 1;
  LAST_COURSE_STUDY_DATE = 2;
  NUMBER_OF_COURSES_PURCHASED = 3;
  TOTAL_COURSES_SPENT = 4;
  NUMBER_OF_DIAMOND_COURSES_CLAIMED = 5;
  FIRST_COURSES_SESSION_DATE = 6;
  LAST_COURSES_SESSION_DATE = 7;
  NUMBER_OF_COURSES_REFUNDED = 8;
  NUMBER_OF_COURSES_VARIATIONS_LEARNED = 9;
  NUMBER_OF_COURSES_REVIEWS_PENDING = 10;
  NUMBER_OF_COURSES_VARIATIONS_REVIEWED = 11;
  NUMBER_OF_COURSES_VARIATIONS_PREVIEWED = 12;
 
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10301"></a>
## FND-10301: chesscom.user_properties.v1.CoursesPropertyDefinition.FIRST_COURSES_SESSION_DATE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FIRST_COURSES_SESSION_DATE = 6;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 359.

```text
BER_OF_COURSES_PURCHASED = 3;
  TOTAL_COURSES_SPENT = 4;
  NUMBER_OF_DIAMOND_COURSES_CLAIMED = 5;
  FIRST_COURSES_SESSION_DATE = 6;
  LAST_COURSES_SESSION_DATE = 7;
  NUMBER_OF_COURSES_REFUNDED = 8;
  NUMBER_OF_COURSES_VARIATIONS_LEARNED = 9;
  NUMBER_OF_COURSES_REVIEWS_PENDING = 10;
  NUMBER_OF_COURSES_VARIATIONS_REVIEWED = 11;
  NUMBER_OF_COURSES_VARIATIONS_PREVIEWED = 12;
  NUMBER_OF_COURSES_COMPLETED = 13;
  NUMB
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10302"></a>
## FND-10302: chesscom.user_properties.v1.CoursesPropertyDefinition.LAST_COURSES_SESSION_DATE = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_COURSES_SESSION_DATE = 7;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 393.

```text
TAL_COURSES_SPENT = 4;
  NUMBER_OF_DIAMOND_COURSES_CLAIMED = 5;
  FIRST_COURSES_SESSION_DATE = 6;
  LAST_COURSES_SESSION_DATE = 7;
  NUMBER_OF_COURSES_REFUNDED = 8;
  NUMBER_OF_COURSES_VARIATIONS_LEARNED = 9;
  NUMBER_OF_COURSES_REVIEWS_PENDING = 10;
  NUMBER_OF_COURSES_VARIATIONS_REVIEWED = 11;
  NUMBER_OF_COURSES_VARIATIONS_PREVIEWED = 12;
  NUMBER_OF_COURSES_COMPLETED = 13;
  NUMBER_OF_COURSES_OWNED = 14;
  COURSE
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10303"></a>
## FND-10303: chesscom.user_properties.v1.CoursesPropertyDefinition.NUMBER_OF_COURSES_REFUNDED = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_COURSES_REFUNDED = 8;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 426.

```text
F_DIAMOND_COURSES_CLAIMED = 5;
  FIRST_COURSES_SESSION_DATE = 6;
  LAST_COURSES_SESSION_DATE = 7;
  NUMBER_OF_COURSES_REFUNDED = 8;
  NUMBER_OF_COURSES_VARIATIONS_LEARNED = 9;
  NUMBER_OF_COURSES_REVIEWS_PENDING = 10;
  NUMBER_OF_COURSES_VARIATIONS_REVIEWED = 11;
  NUMBER_OF_COURSES_VARIATIONS_PREVIEWED = 12;
  NUMBER_OF_COURSES_COMPLETED = 13;
  NUMBER_OF_COURSES_OWNED = 14;
  COURSES_TUTORIAL_CLAIMED = 15;
  NUMBER
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10304"></a>
## FND-10304: chesscom.user_properties.v1.CoursesPropertyDefinition.NUMBER_OF_COURSES_VARIATIONS_LEARNED = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_COURSES_VARIATIONS_LEARNED = 9;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 460.

```text
IRST_COURSES_SESSION_DATE = 6;
  LAST_COURSES_SESSION_DATE = 7;
  NUMBER_OF_COURSES_REFUNDED = 8;
  NUMBER_OF_COURSES_VARIATIONS_LEARNED = 9;
  NUMBER_OF_COURSES_REVIEWS_PENDING = 10;
  NUMBER_OF_COURSES_VARIATIONS_REVIEWED = 11;
  NUMBER_OF_COURSES_VARIATIONS_PREVIEWED = 12;
  NUMBER_OF_COURSES_COMPLETED = 13;
  NUMBER_OF_COURSES_OWNED = 14;
  COURSES_TUTORIAL_CLAIMED = 15;
  NUMBER_OF_PREVIEW_COURSES_OWNED = 16;
  
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10305"></a>
## FND-10305: chesscom.user_properties.v1.CoursesPropertyDefinition.NUMBER_OF_COURSES_REVIEWS_PENDING = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_COURSES_REVIEWS_PENDING = 10;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 504.

```text
S_SESSION_DATE = 7;
  NUMBER_OF_COURSES_REFUNDED = 8;
  NUMBER_OF_COURSES_VARIATIONS_LEARNED = 9;
  NUMBER_OF_COURSES_REVIEWS_PENDING = 10;
  NUMBER_OF_COURSES_VARIATIONS_REVIEWED = 11;
  NUMBER_OF_COURSES_VARIATIONS_PREVIEWED = 12;
  NUMBER_OF_COURSES_COMPLETED = 13;
  NUMBER_OF_COURSES_OWNED = 14;
  COURSES_TUTORIAL_CLAIMED = 15;
  NUMBER_OF_PREVIEW_COURSES_OWNED = 16;
  COURSES_FTUE_SELECTOR_SKIPPED = 17;
}

messa
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10306"></a>
## FND-10306: chesscom.user_properties.v1.CoursesPropertyDefinition.NUMBER_OF_COURSES_VARIATIONS_REVIEWED = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_COURSES_VARIATIONS_REVIEWED = 11;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 546.

```text
FUNDED = 8;
  NUMBER_OF_COURSES_VARIATIONS_LEARNED = 9;
  NUMBER_OF_COURSES_REVIEWS_PENDING = 10;
  NUMBER_OF_COURSES_VARIATIONS_REVIEWED = 11;
  NUMBER_OF_COURSES_VARIATIONS_PREVIEWED = 12;
  NUMBER_OF_COURSES_COMPLETED = 13;
  NUMBER_OF_COURSES_OWNED = 14;
  COURSES_TUTORIAL_CLAIMED = 15;
  NUMBER_OF_PREVIEW_COURSES_OWNED = 16;
  COURSES_FTUE_SELECTOR_SKIPPED = 17;
}

message CoursesProperty {
  oneof _last_course_
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10307"></a>
## FND-10307: chesscom.user_properties.v1.CoursesPropertyDefinition.NUMBER_OF_COURSES_VARIATIONS_PREVIEWED = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_COURSES_VARIATIONS_PREVIEWED = 12;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 592.

```text
RNED = 9;
  NUMBER_OF_COURSES_REVIEWS_PENDING = 10;
  NUMBER_OF_COURSES_VARIATIONS_REVIEWED = 11;
  NUMBER_OF_COURSES_VARIATIONS_PREVIEWED = 12;
  NUMBER_OF_COURSES_COMPLETED = 13;
  NUMBER_OF_COURSES_OWNED = 14;
  COURSES_TUTORIAL_CLAIMED = 15;
  NUMBER_OF_PREVIEW_COURSES_OWNED = 16;
  COURSES_FTUE_SELECTOR_SKIPPED = 17;
}

message CoursesProperty {
  oneof _last_course_purchased_date {
  .google.protobuf.Timestamp 
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10308"></a>
## FND-10308: chesscom.user_properties.v1.CoursesPropertyDefinition.NUMBER_OF_COURSES_COMPLETED = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_COURSES_COMPLETED = 13;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 639.

```text
 10;
  NUMBER_OF_COURSES_VARIATIONS_REVIEWED = 11;
  NUMBER_OF_COURSES_VARIATIONS_PREVIEWED = 12;
  NUMBER_OF_COURSES_COMPLETED = 13;
  NUMBER_OF_COURSES_OWNED = 14;
  COURSES_TUTORIAL_CLAIMED = 15;
  NUMBER_OF_PREVIEW_COURSES_OWNED = 16;
  COURSES_FTUE_SELECTOR_SKIPPED = 17;
}

message CoursesProperty {
  oneof _last_course_purchased_date {
  .google.protobuf.Timestamp last_course_purchased_date = 1;
  }
  oneof _la
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10309"></a>
## FND-10309: chesscom.user_properties.v1.CoursesPropertyDefinition.NUMBER_OF_COURSES_OWNED = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_COURSES_OWNED = 14;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 675.

```text
REVIEWED = 11;
  NUMBER_OF_COURSES_VARIATIONS_PREVIEWED = 12;
  NUMBER_OF_COURSES_COMPLETED = 13;
  NUMBER_OF_COURSES_OWNED = 14;
  COURSES_TUTORIAL_CLAIMED = 15;
  NUMBER_OF_PREVIEW_COURSES_OWNED = 16;
  COURSES_FTUE_SELECTOR_SKIPPED = 17;
}

message CoursesProperty {
  oneof _last_course_purchased_date {
  .google.protobuf.Timestamp last_course_purchased_date = 1;
  }
  oneof _last_course_study_date {
  .google.pro
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10310"></a>
## FND-10310: chesscom.user_properties.v1.CoursesPropertyDefinition.COURSES_TUTORIAL_CLAIMED = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSES_TUTORIAL_CLAIMED = 15;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 707.

```text
ES_VARIATIONS_PREVIEWED = 12;
  NUMBER_OF_COURSES_COMPLETED = 13;
  NUMBER_OF_COURSES_OWNED = 14;
  COURSES_TUTORIAL_CLAIMED = 15;
  NUMBER_OF_PREVIEW_COURSES_OWNED = 16;
  COURSES_FTUE_SELECTOR_SKIPPED = 17;
}

message CoursesProperty {
  oneof _last_course_purchased_date {
  .google.protobuf.Timestamp last_course_purchased_date = 1;
  }
  oneof _last_course_study_date {
  .google.protobuf.Timestamp last_course_stud
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10311"></a>
## FND-10311: chesscom.user_properties.v1.CoursesPropertyDefinition.NUMBER_OF_PREVIEW_COURSES_OWNED = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_PREVIEW_COURSES_OWNED = 16;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 740.

```text
UMBER_OF_COURSES_COMPLETED = 13;
  NUMBER_OF_COURSES_OWNED = 14;
  COURSES_TUTORIAL_CLAIMED = 15;
  NUMBER_OF_PREVIEW_COURSES_OWNED = 16;
  COURSES_FTUE_SELECTOR_SKIPPED = 17;
}

message CoursesProperty {
  oneof _last_course_purchased_date {
  .google.protobuf.Timestamp last_course_purchased_date = 1;
  }
  oneof _last_course_study_date {
  .google.protobuf.Timestamp last_course_study_date = 2;
  }
  oneof _number_o
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10312"></a>
## FND-10312: chesscom.user_properties.v1.CoursesPropertyDefinition.COURSES_FTUE_SELECTOR_SKIPPED = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSES_FTUE_SELECTOR_SKIPPED = 17;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 780.

```text
R_OF_COURSES_OWNED = 14;
  COURSES_TUTORIAL_CLAIMED = 15;
  NUMBER_OF_PREVIEW_COURSES_OWNED = 16;
  COURSES_FTUE_SELECTOR_SKIPPED = 17;
}

message CoursesProperty {
  oneof _last_course_purchased_date {
  .google.protobuf.Timestamp last_course_purchased_date = 1;
  }
  oneof _last_course_study_date {
  .google.protobuf.Timestamp last_course_study_date = 2;
  }
  oneof _number_of_courses_purchased {
  int32 number_of_
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10313"></a>
## FND-10313: message declaration: chesscom.user_properties.v1.CoursesProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoursesProperty {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 819.

```text
RIAL_CLAIMED = 15;
  NUMBER_OF_PREVIEW_COURSES_OWNED = 16;
  COURSES_FTUE_SELECTOR_SKIPPED = 17;
}

message CoursesProperty {
  oneof _last_course_purchased_date {
  .google.protobuf.Timestamp last_course_purchased_date = 1;
  }
  oneof _last_course_study_date {
  .google.protobuf.Timestamp last_course_study_date = 2;
  }
  oneof _number_of_courses_purchased {
  int32 number_of_courses_purchased = 3;
  }
  oneof _tot
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10314"></a>
## FND-10314: oneof declaration: chesscom.user_properties.v1.CoursesProperty._last_course_purchased_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_course_purchased_date {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 847.

```text
OF_PREVIEW_COURSES_OWNED = 16;
  COURSES_FTUE_SELECTOR_SKIPPED = 17;
}

message CoursesProperty {
  oneof _last_course_purchased_date {
  .google.protobuf.Timestamp last_course_purchased_date = 1;
  }
  oneof _last_course_study_date {
  .google.protobuf.Timestamp last_course_study_date = 2;
  }
  oneof _number_of_courses_purchased {
  int32 number_of_courses_purchased = 3;
  }
  oneof _total_courses_spent {
  double 
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10315"></a>
## FND-10315: chesscom.user_properties.v1.CoursesProperty.last_course_purchased_date = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_course_purchased_date = 1;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 885.

```text
ES_FTUE_SELECTOR_SKIPPED = 17;
}

message CoursesProperty {
  oneof _last_course_purchased_date {
  .google.protobuf.Timestamp last_course_purchased_date = 1;
  }
  oneof _last_course_study_date {
  .google.protobuf.Timestamp last_course_study_date = 2;
  }
  oneof _number_of_courses_purchased {
  int32 number_of_courses_purchased = 3;
  }
  oneof _total_courses_spent {
  double total_courses_spent = 4;
  }
  oneof _
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10316"></a>
## FND-10316: oneof declaration: chesscom.user_properties.v1.CoursesProperty._last_course_study_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_course_study_date {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 950.

```text
of _last_course_purchased_date {
  .google.protobuf.Timestamp last_course_purchased_date = 1;
  }
  oneof _last_course_study_date {
  .google.protobuf.Timestamp last_course_study_date = 2;
  }
  oneof _number_of_courses_purchased {
  int32 number_of_courses_purchased = 3;
  }
  oneof _total_courses_spent {
  double total_courses_spent = 4;
  }
  oneof _number_of_diamond_courses_claimed {
  int32 number_of_diamond_cou
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10317"></a>
## FND-10317: chesscom.user_properties.v1.CoursesProperty.last_course_study_date = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_course_study_date = 2;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 984.

```text
 .google.protobuf.Timestamp last_course_purchased_date = 1;
  }
  oneof _last_course_study_date {
  .google.protobuf.Timestamp last_course_study_date = 2;
  }
  oneof _number_of_courses_purchased {
  int32 number_of_courses_purchased = 3;
  }
  oneof _total_courses_spent {
  double total_courses_spent = 4;
  }
  oneof _number_of_diamond_courses_claimed {
  int32 number_of_diamond_courses_claimed = 5;
  }
  oneof _fir
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10318"></a>
## FND-10318: oneof declaration: chesscom.user_properties.v1.CoursesProperty._number_of_courses_purchased

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_courses_purchased {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1045.

```text
 }
  oneof _last_course_study_date {
  .google.protobuf.Timestamp last_course_study_date = 2;
  }
  oneof _number_of_courses_purchased {
  int32 number_of_courses_purchased = 3;
  }
  oneof _total_courses_spent {
  double total_courses_spent = 4;
  }
  oneof _number_of_diamond_courses_claimed {
  int32 number_of_diamond_courses_claimed = 5;
  }
  oneof _first_courses_session_date {
  .google.protobuf.Timestamp first_
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10319"></a>
## FND-10319: chesscom.user_properties.v1.CoursesProperty.number_of_courses_purchased = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_courses_purchased = 3;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1084.

```text
.google.protobuf.Timestamp last_course_study_date = 2;
  }
  oneof _number_of_courses_purchased {
  int32 number_of_courses_purchased = 3;
  }
  oneof _total_courses_spent {
  double total_courses_spent = 4;
  }
  oneof _number_of_diamond_courses_claimed {
  int32 number_of_diamond_courses_claimed = 5;
  }
  oneof _first_courses_session_date {
  .google.protobuf.Timestamp first_courses_session_date = 6;
  }
  oneof _
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10320"></a>
## FND-10320: oneof declaration: chesscom.user_properties.v1.CoursesProperty._total_courses_spent

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_courses_spent {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1129.

```text
date = 2;
  }
  oneof _number_of_courses_purchased {
  int32 number_of_courses_purchased = 3;
  }
  oneof _total_courses_spent {
  double total_courses_spent = 4;
  }
  oneof _number_of_diamond_courses_claimed {
  int32 number_of_diamond_courses_claimed = 5;
  }
  oneof _first_courses_session_date {
  .google.protobuf.Timestamp first_courses_session_date = 6;
  }
  oneof _last_courses_session_date {
  .google.protobu
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10321"></a>
## FND-10321: chesscom.user_properties.v1.CoursesProperty.total_courses_spent = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double total_courses_spent = 4;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1160.

```text
f_courses_purchased {
  int32 number_of_courses_purchased = 3;
  }
  oneof _total_courses_spent {
  double total_courses_spent = 4;
  }
  oneof _number_of_diamond_courses_claimed {
  int32 number_of_diamond_courses_claimed = 5;
  }
  oneof _first_courses_session_date {
  .google.protobuf.Timestamp first_courses_session_date = 6;
  }
  oneof _last_courses_session_date {
  .google.protobuf.Timestamp last_courses_sessio
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10322"></a>
## FND-10322: oneof declaration: chesscom.user_properties.v1.CoursesProperty._number_of_diamond_courses_claimed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_diamond_courses_claimed {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1198.

```text
f_courses_purchased = 3;
  }
  oneof _total_courses_spent {
  double total_courses_spent = 4;
  }
  oneof _number_of_diamond_courses_claimed {
  int32 number_of_diamond_courses_claimed = 5;
  }
  oneof _first_courses_session_date {
  .google.protobuf.Timestamp first_courses_session_date = 6;
  }
  oneof _last_courses_session_date {
  .google.protobuf.Timestamp last_courses_session_date = 7;
  }
  oneof _number_of_cou
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10323"></a>
## FND-10323: chesscom.user_properties.v1.CoursesProperty.number_of_diamond_courses_claimed = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_diamond_courses_claimed = 5;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1243.

```text
ourses_spent {
  double total_courses_spent = 4;
  }
  oneof _number_of_diamond_courses_claimed {
  int32 number_of_diamond_courses_claimed = 5;
  }
  oneof _first_courses_session_date {
  .google.protobuf.Timestamp first_courses_session_date = 6;
  }
  oneof _last_courses_session_date {
  .google.protobuf.Timestamp last_courses_session_date = 7;
  }
  oneof _number_of_courses_refunded {
  int32 number_of_courses_ref
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10324"></a>
## FND-10324: oneof declaration: chesscom.user_properties.v1.CoursesProperty._first_courses_session_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _first_courses_session_date {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1294.

```text
}
  oneof _number_of_diamond_courses_claimed {
  int32 number_of_diamond_courses_claimed = 5;
  }
  oneof _first_courses_session_date {
  .google.protobuf.Timestamp first_courses_session_date = 6;
  }
  oneof _last_courses_session_date {
  .google.protobuf.Timestamp last_courses_session_date = 7;
  }
  oneof _number_of_courses_refunded {
  int32 number_of_courses_refunded = 8;
  }
  oneof _number_of_courses_variation
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10325"></a>
## FND-10325: chesscom.user_properties.v1.CoursesProperty.first_courses_session_date = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp first_courses_session_date = 6;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1332.

```text
laimed {
  int32 number_of_diamond_courses_claimed = 5;
  }
  oneof _first_courses_session_date {
  .google.protobuf.Timestamp first_courses_session_date = 6;
  }
  oneof _last_courses_session_date {
  .google.protobuf.Timestamp last_courses_session_date = 7;
  }
  oneof _number_of_courses_refunded {
  int32 number_of_courses_refunded = 8;
  }
  oneof _number_of_courses_variations_learned {
  int32 number_of_courses_
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10326"></a>
## FND-10326: oneof declaration: chesscom.user_properties.v1.CoursesProperty._last_courses_session_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_courses_session_date {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1397.

```text
of _first_courses_session_date {
  .google.protobuf.Timestamp first_courses_session_date = 6;
  }
  oneof _last_courses_session_date {
  .google.protobuf.Timestamp last_courses_session_date = 7;
  }
  oneof _number_of_courses_refunded {
  int32 number_of_courses_refunded = 8;
  }
  oneof _number_of_courses_variations_learned {
  int32 number_of_courses_variations_learned = 9;
  }
  oneof _number_of_courses_reviews_pe
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10327"></a>
## FND-10327: chesscom.user_properties.v1.CoursesProperty.last_courses_session_date = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_courses_session_date = 7;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1434.

```text
oogle.protobuf.Timestamp first_courses_session_date = 6;
  }
  oneof _last_courses_session_date {
  .google.protobuf.Timestamp last_courses_session_date = 7;
  }
  oneof _number_of_courses_refunded {
  int32 number_of_courses_refunded = 8;
  }
  oneof _number_of_courses_variations_learned {
  int32 number_of_courses_variations_learned = 9;
  }
  oneof _number_of_courses_reviews_pending {
  int32 number_of_courses_rev
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10328"></a>
## FND-10328: oneof declaration: chesscom.user_properties.v1.CoursesProperty._number_of_courses_refunded

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_courses_refunded {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1498.

```text
neof _last_courses_session_date {
  .google.protobuf.Timestamp last_courses_session_date = 7;
  }
  oneof _number_of_courses_refunded {
  int32 number_of_courses_refunded = 8;
  }
  oneof _number_of_courses_variations_learned {
  int32 number_of_courses_variations_learned = 9;
  }
  oneof _number_of_courses_reviews_pending {
  int32 number_of_courses_reviews_pending = 10;
  }
  oneof _number_of_courses_variations_rev
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10329"></a>
## FND-10329: chesscom.user_properties.v1.CoursesProperty.number_of_courses_refunded = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_courses_refunded = 8;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1536.

```text
oogle.protobuf.Timestamp last_courses_session_date = 7;
  }
  oneof _number_of_courses_refunded {
  int32 number_of_courses_refunded = 8;
  }
  oneof _number_of_courses_variations_learned {
  int32 number_of_courses_variations_learned = 9;
  }
  oneof _number_of_courses_reviews_pending {
  int32 number_of_courses_reviews_pending = 10;
  }
  oneof _number_of_courses_variations_reviewed {
  int32 number_of_courses_vari
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10330"></a>
## FND-10330: oneof declaration: chesscom.user_properties.v1.CoursesProperty._number_of_courses_variations_learned

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_courses_variations_learned {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1580.

```text
n_date = 7;
  }
  oneof _number_of_courses_refunded {
  int32 number_of_courses_refunded = 8;
  }
  oneof _number_of_courses_variations_learned {
  int32 number_of_courses_variations_learned = 9;
  }
  oneof _number_of_courses_reviews_pending {
  int32 number_of_courses_reviews_pending = 10;
  }
  oneof _number_of_courses_variations_reviewed {
  int32 number_of_courses_variations_reviewed = 11;
  }
  oneof _number_of
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10331"></a>
## FND-10331: chesscom.user_properties.v1.CoursesProperty.number_of_courses_variations_learned = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_courses_variations_learned = 9;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1628.

```text
ded {
  int32 number_of_courses_refunded = 8;
  }
  oneof _number_of_courses_variations_learned {
  int32 number_of_courses_variations_learned = 9;
  }
  oneof _number_of_courses_reviews_pending {
  int32 number_of_courses_reviews_pending = 10;
  }
  oneof _number_of_courses_variations_reviewed {
  int32 number_of_courses_variations_reviewed = 11;
  }
  oneof _number_of_courses_variations_previewed {
  int32 number_o
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10332"></a>
## FND-10332: oneof declaration: chesscom.user_properties.v1.CoursesProperty._number_of_courses_reviews_pending

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_courses_reviews_pending {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1682.

```text
eof _number_of_courses_variations_learned {
  int32 number_of_courses_variations_learned = 9;
  }
  oneof _number_of_courses_reviews_pending {
  int32 number_of_courses_reviews_pending = 10;
  }
  oneof _number_of_courses_variations_reviewed {
  int32 number_of_courses_variations_reviewed = 11;
  }
  oneof _number_of_courses_variations_previewed {
  int32 number_of_courses_variations_previewed = 12;
  }
  oneof _numb
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10333"></a>
## FND-10333: chesscom.user_properties.v1.CoursesProperty.number_of_courses_reviews_pending = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_courses_reviews_pending = 10;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1727.

```text
 int32 number_of_courses_variations_learned = 9;
  }
  oneof _number_of_courses_reviews_pending {
  int32 number_of_courses_reviews_pending = 10;
  }
  oneof _number_of_courses_variations_reviewed {
  int32 number_of_courses_variations_reviewed = 11;
  }
  oneof _number_of_courses_variations_previewed {
  int32 number_of_courses_variations_previewed = 12;
  }
  oneof _number_of_courses_completed {
  int32 number_of_c
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10334"></a>
## FND-10334: oneof declaration: chesscom.user_properties.v1.CoursesProperty._number_of_courses_variations_reviewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_courses_variations_reviewed {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1779.

```text

  oneof _number_of_courses_reviews_pending {
  int32 number_of_courses_reviews_pending = 10;
  }
  oneof _number_of_courses_variations_reviewed {
  int32 number_of_courses_variations_reviewed = 11;
  }
  oneof _number_of_courses_variations_previewed {
  int32 number_of_courses_variations_previewed = 12;
  }
  oneof _number_of_courses_completed {
  int32 number_of_courses_completed = 13;
  }
  oneof _number_of_course
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10335"></a>
## FND-10335: chesscom.user_properties.v1.CoursesProperty.number_of_courses_variations_reviewed = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_courses_variations_reviewed = 11;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1828.

```text
nt32 number_of_courses_reviews_pending = 10;
  }
  oneof _number_of_courses_variations_reviewed {
  int32 number_of_courses_variations_reviewed = 11;
  }
  oneof _number_of_courses_variations_previewed {
  int32 number_of_courses_variations_previewed = 12;
  }
  oneof _number_of_courses_completed {
  int32 number_of_courses_completed = 13;
  }
  oneof _number_of_courses_owned {
  int32 number_of_courses_owned = 14;
 
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10336"></a>
## FND-10336: oneof declaration: chesscom.user_properties.v1.CoursesProperty._number_of_courses_variations_previewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_courses_variations_previewed {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1884.

```text
 _number_of_courses_variations_reviewed {
  int32 number_of_courses_variations_reviewed = 11;
  }
  oneof _number_of_courses_variations_previewed {
  int32 number_of_courses_variations_previewed = 12;
  }
  oneof _number_of_courses_completed {
  int32 number_of_courses_completed = 13;
  }
  oneof _number_of_courses_owned {
  int32 number_of_courses_owned = 14;
  }
  oneof _courses_tutorial_claimed {
  bool courses_tu
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10337"></a>
## FND-10337: chesscom.user_properties.v1.CoursesProperty.number_of_courses_variations_previewed = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_courses_variations_previewed = 12;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1934.

```text
number_of_courses_variations_reviewed = 11;
  }
  oneof _number_of_courses_variations_previewed {
  int32 number_of_courses_variations_previewed = 12;
  }
  oneof _number_of_courses_completed {
  int32 number_of_courses_completed = 13;
  }
  oneof _number_of_courses_owned {
  int32 number_of_courses_owned = 14;
  }
  oneof _courses_tutorial_claimed {
  bool courses_tutorial_claimed = 15;
  }
  oneof _number_of_previe
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10338"></a>
## FND-10338: oneof declaration: chesscom.user_properties.v1.CoursesProperty._number_of_courses_completed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_courses_completed {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 1991.

```text
number_of_courses_variations_previewed {
  int32 number_of_courses_variations_previewed = 12;
  }
  oneof _number_of_courses_completed {
  int32 number_of_courses_completed = 13;
  }
  oneof _number_of_courses_owned {
  int32 number_of_courses_owned = 14;
  }
  oneof _courses_tutorial_claimed {
  bool courses_tutorial_claimed = 15;
  }
  oneof _number_of_preview_courses_owned {
  int32 number_of_preview_courses_owned
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10339"></a>
## FND-10339: chesscom.user_properties.v1.CoursesProperty.number_of_courses_completed = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_courses_completed = 13;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 2030.

```text
{
  int32 number_of_courses_variations_previewed = 12;
  }
  oneof _number_of_courses_completed {
  int32 number_of_courses_completed = 13;
  }
  oneof _number_of_courses_owned {
  int32 number_of_courses_owned = 14;
  }
  oneof _courses_tutorial_claimed {
  bool courses_tutorial_claimed = 15;
  }
  oneof _number_of_preview_courses_owned {
  int32 number_of_preview_courses_owned = 16;
  }
  oneof _courses_ftue_select
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10340"></a>
## FND-10340: oneof declaration: chesscom.user_properties.v1.CoursesProperty._number_of_courses_owned

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_courses_owned {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 2076.

```text
ed = 12;
  }
  oneof _number_of_courses_completed {
  int32 number_of_courses_completed = 13;
  }
  oneof _number_of_courses_owned {
  int32 number_of_courses_owned = 14;
  }
  oneof _courses_tutorial_claimed {
  bool courses_tutorial_claimed = 15;
  }
  oneof _number_of_preview_courses_owned {
  int32 number_of_preview_courses_owned = 16;
  }
  oneof _courses_ftue_selector_skipped {
  bool courses_ftue_selector_skip
```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10341"></a>
## FND-10341: chesscom.user_properties.v1.CoursesProperty.number_of_courses_owned = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_courses_owned = 14;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 2111.

```text
rses_completed {
  int32 number_of_courses_completed = 13;
  }
  oneof _number_of_courses_owned {
  int32 number_of_courses_owned = 14;
  }
  oneof _courses_tutorial_claimed {
  bool courses_tutorial_claimed = 15;
  }
  oneof _number_of_preview_courses_owned {
  int32 number_of_preview_courses_owned = 16;
  }
  oneof _courses_ftue_selector_skipped {
  bool courses_ftue_selector_skipped = 17;
  }
}

```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10342"></a>
## FND-10342: oneof declaration: chesscom.user_properties.v1.CoursesProperty._courses_tutorial_claimed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _courses_tutorial_claimed {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 2153.

```text
_completed = 13;
  }
  oneof _number_of_courses_owned {
  int32 number_of_courses_owned = 14;
  }
  oneof _courses_tutorial_claimed {
  bool courses_tutorial_claimed = 15;
  }
  oneof _number_of_preview_courses_owned {
  int32 number_of_preview_courses_owned = 16;
  }
  oneof _courses_ftue_selector_skipped {
  bool courses_ftue_selector_skipped = 17;
  }
}

```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10343"></a>
## FND-10343: chesscom.user_properties.v1.CoursesProperty.courses_tutorial_claimed = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool courses_tutorial_claimed = 15;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 2189.

```text
_of_courses_owned {
  int32 number_of_courses_owned = 14;
  }
  oneof _courses_tutorial_claimed {
  bool courses_tutorial_claimed = 15;
  }
  oneof _number_of_preview_courses_owned {
  int32 number_of_preview_courses_owned = 16;
  }
  oneof _courses_ftue_selector_skipped {
  bool courses_ftue_selector_skipped = 17;
  }
}

```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10344"></a>
## FND-10344: oneof declaration: chesscom.user_properties.v1.CoursesProperty._number_of_preview_courses_owned

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_preview_courses_owned {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 2231.

```text
ses_owned = 14;
  }
  oneof _courses_tutorial_claimed {
  bool courses_tutorial_claimed = 15;
  }
  oneof _number_of_preview_courses_owned {
  int32 number_of_preview_courses_owned = 16;
  }
  oneof _courses_ftue_selector_skipped {
  bool courses_ftue_selector_skipped = 17;
  }
}

```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10345"></a>
## FND-10345: chesscom.user_properties.v1.CoursesProperty.number_of_preview_courses_owned = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_preview_courses_owned = 16;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 2274.

```text
al_claimed {
  bool courses_tutorial_claimed = 15;
  }
  oneof _number_of_preview_courses_owned {
  int32 number_of_preview_courses_owned = 16;
  }
  oneof _courses_ftue_selector_skipped {
  bool courses_ftue_selector_skipped = 17;
  }
}

```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10346"></a>
## FND-10346: oneof declaration: chesscom.user_properties.v1.CoursesProperty._courses_ftue_selector_skipped

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _courses_ftue_selector_skipped {

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 2324.

```text

  }
  oneof _number_of_preview_courses_owned {
  int32 number_of_preview_courses_owned = 16;
  }
  oneof _courses_ftue_selector_skipped {
  bool courses_ftue_selector_skipped = 17;
  }
}

```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10347"></a>
## FND-10347: chesscom.user_properties.v1.CoursesProperty.courses_ftue_selector_skipped = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool courses_ftue_selector_skipped = 17;

### Evidence

- **SRC-0608** `research/proto/chesscom/user_properties/v1/properties_courses.proto` — [preserved redacted evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto)
  Character offset 2365.

```text
wned {
  int32 number_of_preview_courses_owned = 16;
  }
  oneof _courses_ftue_selector_skipped {
  bool courses_ftue_selector_skipped = 17;
  }
}

```

**Source references:** SRC-0608, SRC-1579  
**URL references:** None independently associated  
**Related findings:** FND-10294, FND-10295, FND-10296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10348"></a>
## FND-10348: enum declaration: chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum DailyPuzzlesSolvedPropertyDefinition {

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 134.

```text
s/v1/properties_daily_puzzles_solved.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum DailyPuzzlesSolvedPropertyDefinition {
  DAILY_PUZZLES_SOLVED_UNSPECIFIED = 0;
  DAILY_PUZZLES_LAST_COMPLETED_TIMESTAMP = 1;
  DAILY_PUZZLES_CURRENT_STREAK = 2;
  DAILY_PUZZLES_LONGEST_STREAK = 3;
  DAILY_PUZZLES_LONGEST_STREAK_TIMESTAMP = 4;
  DAILY_PUZZLES_CURRENT_STREAK_IS_LONGEST_DAILY_PUZZLE_STREAK = 5;
  DAI
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10349, FND-10350

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10349"></a>
## FND-10349: chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition.DAILY_PUZZLES_SOLVED_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DAILY_PUZZLES_SOLVED_UNSPECIFIED = 0;

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 180.

```text
syntax: proto3

package chesscom.user_properties.v1;

enum DailyPuzzlesSolvedPropertyDefinition {
  DAILY_PUZZLES_SOLVED_UNSPECIFIED = 0;
  DAILY_PUZZLES_LAST_COMPLETED_TIMESTAMP = 1;
  DAILY_PUZZLES_CURRENT_STREAK = 2;
  DAILY_PUZZLES_LONGEST_STREAK = 3;
  DAILY_PUZZLES_LONGEST_STREAK_TIMESTAMP = 4;
  DAILY_PUZZLES_CURRENT_STREAK_IS_LONGEST_DAILY_PUZZLE_STREAK = 5;
  DAILY_PUZZLES_CURRENT_STREAK_END_TIMESTAMP = 6;
}
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10350

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10350"></a>
## FND-10350: chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition.DAILY_PUZZLES_LAST_COMPLETED_TIMESTAMP = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DAILY_PUZZLES_LAST_COMPLETED_TIMESTAMP = 1;

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 220.

```text
operties.v1;

enum DailyPuzzlesSolvedPropertyDefinition {
  DAILY_PUZZLES_SOLVED_UNSPECIFIED = 0;
  DAILY_PUZZLES_LAST_COMPLETED_TIMESTAMP = 1;
  DAILY_PUZZLES_CURRENT_STREAK = 2;
  DAILY_PUZZLES_LONGEST_STREAK = 3;
  DAILY_PUZZLES_LONGEST_STREAK_TIMESTAMP = 4;
  DAILY_PUZZLES_CURRENT_STREAK_IS_LONGEST_DAILY_PUZZLE_STREAK = 5;
  DAILY_PUZZLES_CURRENT_STREAK_END_TIMESTAMP = 6;
}

message DailyPuzzlesSolvedProperty {
 
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10351"></a>
## FND-10351: chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition.DAILY_PUZZLES_CURRENT_STREAK = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DAILY_PUZZLES_CURRENT_STREAK = 2;

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 266.

```text
efinition {
  DAILY_PUZZLES_SOLVED_UNSPECIFIED = 0;
  DAILY_PUZZLES_LAST_COMPLETED_TIMESTAMP = 1;
  DAILY_PUZZLES_CURRENT_STREAK = 2;
  DAILY_PUZZLES_LONGEST_STREAK = 3;
  DAILY_PUZZLES_LONGEST_STREAK_TIMESTAMP = 4;
  DAILY_PUZZLES_CURRENT_STREAK_IS_LONGEST_DAILY_PUZZLE_STREAK = 5;
  DAILY_PUZZLES_CURRENT_STREAK_END_TIMESTAMP = 6;
}

message DailyPuzzlesSolvedProperty {
  oneof _last_completed_timestamp {
  .google.p
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10352"></a>
## FND-10352: chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition.DAILY_PUZZLES_LONGEST_STREAK = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DAILY_PUZZLES_LONGEST_STREAK = 3;

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 302.

```text
NSPECIFIED = 0;
  DAILY_PUZZLES_LAST_COMPLETED_TIMESTAMP = 1;
  DAILY_PUZZLES_CURRENT_STREAK = 2;
  DAILY_PUZZLES_LONGEST_STREAK = 3;
  DAILY_PUZZLES_LONGEST_STREAK_TIMESTAMP = 4;
  DAILY_PUZZLES_CURRENT_STREAK_IS_LONGEST_DAILY_PUZZLE_STREAK = 5;
  DAILY_PUZZLES_CURRENT_STREAK_END_TIMESTAMP = 6;
}

message DailyPuzzlesSolvedProperty {
  oneof _last_completed_timestamp {
  .google.protobuf.Timestamp last_completed_tim
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10353"></a>
## FND-10353: chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition.DAILY_PUZZLES_LONGEST_STREAK_TIMESTAMP = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DAILY_PUZZLES_LONGEST_STREAK_TIMESTAMP = 4;

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 338.

```text
_COMPLETED_TIMESTAMP = 1;
  DAILY_PUZZLES_CURRENT_STREAK = 2;
  DAILY_PUZZLES_LONGEST_STREAK = 3;
  DAILY_PUZZLES_LONGEST_STREAK_TIMESTAMP = 4;
  DAILY_PUZZLES_CURRENT_STREAK_IS_LONGEST_DAILY_PUZZLE_STREAK = 5;
  DAILY_PUZZLES_CURRENT_STREAK_END_TIMESTAMP = 6;
}

message DailyPuzzlesSolvedProperty {
  oneof _last_completed_timestamp {
  .google.protobuf.Timestamp last_completed_timestamp = 1;
  }
  oneof _current_str
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10354"></a>
## FND-10354: chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition.DAILY_PUZZLES_CURRENT_STREAK_IS_LONGEST_DAILY_PUZZLE_STREAK = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DAILY_PUZZLES_CURRENT_STREAK_IS_LONGEST_DAILY_PUZZLE_STREAK = 5;

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 384.

```text
ENT_STREAK = 2;
  DAILY_PUZZLES_LONGEST_STREAK = 3;
  DAILY_PUZZLES_LONGEST_STREAK_TIMESTAMP = 4;
  DAILY_PUZZLES_CURRENT_STREAK_IS_LONGEST_DAILY_PUZZLE_STREAK = 5;
  DAILY_PUZZLES_CURRENT_STREAK_END_TIMESTAMP = 6;
}

message DailyPuzzlesSolvedProperty {
  oneof _last_completed_timestamp {
  .google.protobuf.Timestamp last_completed_timestamp = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof 
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10355"></a>
## FND-10355: chesscom.user_properties.v1.DailyPuzzlesSolvedPropertyDefinition.DAILY_PUZZLES_CURRENT_STREAK_END_TIMESTAMP = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DAILY_PUZZLES_CURRENT_STREAK_END_TIMESTAMP = 6;

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 451.

```text
_LONGEST_STREAK_TIMESTAMP = 4;
  DAILY_PUZZLES_CURRENT_STREAK_IS_LONGEST_DAILY_PUZZLE_STREAK = 5;
  DAILY_PUZZLES_CURRENT_STREAK_END_TIMESTAMP = 6;
}

message DailyPuzzlesSolvedProperty {
  oneof _last_completed_timestamp {
  .google.protobuf.Timestamp last_completed_timestamp = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _longest_streak {
  int32 longest_streak = 3;
  }
  oneof _longest_
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10356"></a>
## FND-10356: message declaration: chesscom.user_properties.v1.DailyPuzzlesSolvedProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DailyPuzzlesSolvedProperty {

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 502.

```text
ENT_STREAK_IS_LONGEST_DAILY_PUZZLE_STREAK = 5;
  DAILY_PUZZLES_CURRENT_STREAK_END_TIMESTAMP = 6;
}

message DailyPuzzlesSolvedProperty {
  oneof _last_completed_timestamp {
  .google.protobuf.Timestamp last_completed_timestamp = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _longest_streak {
  int32 longest_streak = 3;
  }
  oneof _longest_streak_timestamp {
  .google.protobuf.Timestamp lon
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10357"></a>
## FND-10357: oneof declaration: chesscom.user_properties.v1.DailyPuzzlesSolvedProperty._last_completed_timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_completed_timestamp {

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 541.

```text
AK = 5;
  DAILY_PUZZLES_CURRENT_STREAK_END_TIMESTAMP = 6;
}

message DailyPuzzlesSolvedProperty {
  oneof _last_completed_timestamp {
  .google.protobuf.Timestamp last_completed_timestamp = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _longest_streak {
  int32 longest_streak = 3;
  }
  oneof _longest_streak_timestamp {
  .google.protobuf.Timestamp longest_streak_timestamp = 4;
  }
  oneof 
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10358"></a>
## FND-10358: chesscom.user_properties.v1.DailyPuzzlesSolvedProperty.last_completed_timestamp = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_completed_timestamp = 1;

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 577.

```text
AK_END_TIMESTAMP = 6;
}

message DailyPuzzlesSolvedProperty {
  oneof _last_completed_timestamp {
  .google.protobuf.Timestamp last_completed_timestamp = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _longest_streak {
  int32 longest_streak = 3;
  }
  oneof _longest_streak_timestamp {
  .google.protobuf.Timestamp longest_streak_timestamp = 4;
  }
  oneof _current_streak_is_longest_daily_puz
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10359"></a>
## FND-10359: oneof declaration: chesscom.user_properties.v1.DailyPuzzlesSolvedProperty._current_streak

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _current_streak {

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 640.

```text
 oneof _last_completed_timestamp {
  .google.protobuf.Timestamp last_completed_timestamp = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _longest_streak {
  int32 longest_streak = 3;
  }
  oneof _longest_streak_timestamp {
  .google.protobuf.Timestamp longest_streak_timestamp = 4;
  }
  oneof _current_streak_is_longest_daily_puzzle_streak {
  bool current_streak_is_longest_daily_puzzle_stre
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10360"></a>
## FND-10360: chesscom.user_properties.v1.DailyPuzzlesSolvedProperty.current_streak = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 current_streak = 2;

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 666.

```text
estamp {
  .google.protobuf.Timestamp last_completed_timestamp = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _longest_streak {
  int32 longest_streak = 3;
  }
  oneof _longest_streak_timestamp {
  .google.protobuf.Timestamp longest_streak_timestamp = 4;
  }
  oneof _current_streak_is_longest_daily_puzzle_streak {
  bool current_streak_is_longest_daily_puzzle_streak = 5;
  }
  oneof _curre
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10361"></a>
## FND-10361: oneof declaration: chesscom.user_properties.v1.DailyPuzzlesSolvedProperty._longest_streak

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _longest_streak {

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 698.

```text
stamp last_completed_timestamp = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _longest_streak {
  int32 longest_streak = 3;
  }
  oneof _longest_streak_timestamp {
  .google.protobuf.Timestamp longest_streak_timestamp = 4;
  }
  oneof _current_streak_is_longest_daily_puzzle_streak {
  bool current_streak_is_longest_daily_puzzle_streak = 5;
  }
  oneof _current_streak_end_timestamp {
  .goo
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10362"></a>
## FND-10362: chesscom.user_properties.v1.DailyPuzzlesSolvedProperty.longest_streak = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 longest_streak = 3;

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 724.

```text
tamp = 1;
  }
  oneof _current_streak {
  int32 current_streak = 2;
  }
  oneof _longest_streak {
  int32 longest_streak = 3;
  }
  oneof _longest_streak_timestamp {
  .google.protobuf.Timestamp longest_streak_timestamp = 4;
  }
  oneof _current_streak_is_longest_daily_puzzle_streak {
  bool current_streak_is_longest_daily_puzzle_streak = 5;
  }
  oneof _current_streak_end_timestamp {
  .google.protobuf.Timestamp cur
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10363"></a>
## FND-10363: oneof declaration: chesscom.user_properties.v1.DailyPuzzlesSolvedProperty._longest_streak_timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _longest_streak_timestamp {

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 756.

```text
treak {
  int32 current_streak = 2;
  }
  oneof _longest_streak {
  int32 longest_streak = 3;
  }
  oneof _longest_streak_timestamp {
  .google.protobuf.Timestamp longest_streak_timestamp = 4;
  }
  oneof _current_streak_is_longest_daily_puzzle_streak {
  bool current_streak_is_longest_daily_puzzle_streak = 5;
  }
  oneof _current_streak_end_timestamp {
  .google.protobuf.Timestamp current_streak_end_timestamp = 6;
 
```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10364"></a>
## FND-10364: chesscom.user_properties.v1.DailyPuzzlesSolvedProperty.longest_streak_timestamp = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp longest_streak_timestamp = 4;

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 792.

```text
  }
  oneof _longest_streak {
  int32 longest_streak = 3;
  }
  oneof _longest_streak_timestamp {
  .google.protobuf.Timestamp longest_streak_timestamp = 4;
  }
  oneof _current_streak_is_longest_daily_puzzle_streak {
  bool current_streak_is_longest_daily_puzzle_streak = 5;
  }
  oneof _current_streak_end_timestamp {
  .google.protobuf.Timestamp current_streak_end_timestamp = 6;
  }
}

```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10365"></a>
## FND-10365: oneof declaration: chesscom.user_properties.v1.DailyPuzzlesSolvedProperty._current_streak_is_longest_daily_puzzle_streak

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _current_streak_is_longest_daily_puzzle_streak {

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 855.

```text
 oneof _longest_streak_timestamp {
  .google.protobuf.Timestamp longest_streak_timestamp = 4;
  }
  oneof _current_streak_is_longest_daily_puzzle_streak {
  bool current_streak_is_longest_daily_puzzle_streak = 5;
  }
  oneof _current_streak_end_timestamp {
  .google.protobuf.Timestamp current_streak_end_timestamp = 6;
  }
}

```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10366"></a>
## FND-10366: chesscom.user_properties.v1.DailyPuzzlesSolvedProperty.current_streak_is_longest_daily_puzzle_streak = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool current_streak_is_longest_daily_puzzle_streak = 5;

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 912.

```text
estamp longest_streak_timestamp = 4;
  }
  oneof _current_streak_is_longest_daily_puzzle_streak {
  bool current_streak_is_longest_daily_puzzle_streak = 5;
  }
  oneof _current_streak_end_timestamp {
  .google.protobuf.Timestamp current_streak_end_timestamp = 6;
  }
}

```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10367"></a>
## FND-10367: oneof declaration: chesscom.user_properties.v1.DailyPuzzlesSolvedProperty._current_streak_end_timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _current_streak_end_timestamp {

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 974.

```text
ak_is_longest_daily_puzzle_streak {
  bool current_streak_is_longest_daily_puzzle_streak = 5;
  }
  oneof _current_streak_end_timestamp {
  .google.protobuf.Timestamp current_streak_end_timestamp = 6;
  }
}

```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10368"></a>
## FND-10368: chesscom.user_properties.v1.DailyPuzzlesSolvedProperty.current_streak_end_timestamp = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp current_streak_end_timestamp = 6;

### Evidence

- **SRC-0609** `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto` — [preserved redacted evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto)
  Character offset 1014.

```text
ol current_streak_is_longest_daily_puzzle_streak = 5;
  }
  oneof _current_streak_end_timestamp {
  .google.protobuf.Timestamp current_streak_end_timestamp = 6;
  }
}

```

**Source references:** SRC-0609, SRC-1580  
**URL references:** None independently associated  
**Related findings:** FND-10348, FND-10349, FND-10350

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10369"></a>
## FND-10369: enum declaration: chesscom.user_properties.v1.RangeModifier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum RangeModifier {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 124.

```text
_properties/v1/properties_definition.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum RangeModifier {
  RANGE_MODIFIER_UNSPECIFIED = 0;
  RANGE_MODIFIER_RANGE = 1;
  RANGE_MODIFIER_CEIL = 2;
  RANGE_MODIFIER_FLOOR = 3;
}

enum PropertyPermissionLevel {
  PROPERTY_PERMISSION_LEVEL_UNSPECIFIED = 0;
  PROPERTY_PERMISSION_LEVEL_PRIVATE = 1;
  PROPERTY_PERMISSION_LEVEL_SELF = 2;
  PROPERTY_PERMISSION_LE
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10370"></a>
## FND-10370: chesscom.user_properties.v1.RangeModifier.RANGE_MODIFIER_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RANGE_MODIFIER_UNSPECIFIED = 0;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 147.

```text
es_definition.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum RangeModifier {
  RANGE_MODIFIER_UNSPECIFIED = 0;
  RANGE_MODIFIER_RANGE = 1;
  RANGE_MODIFIER_CEIL = 2;
  RANGE_MODIFIER_FLOOR = 3;
}

enum PropertyPermissionLevel {
  PROPERTY_PERMISSION_LEVEL_UNSPECIFIED = 0;
  PROPERTY_PERMISSION_LEVEL_PRIVATE = 1;
  PROPERTY_PERMISSION_LEVEL_SELF = 2;
  PROPERTY_PERMISSION_LEVEL_FRIENDS = 3;
  PROP
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10371"></a>
## FND-10371: chesscom.user_properties.v1.RangeModifier.RANGE_MODIFIER_RANGE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RANGE_MODIFIER_RANGE = 1;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 181.

```text
to3

package chesscom.user_properties.v1;

enum RangeModifier {
  RANGE_MODIFIER_UNSPECIFIED = 0;
  RANGE_MODIFIER_RANGE = 1;
  RANGE_MODIFIER_CEIL = 2;
  RANGE_MODIFIER_FLOOR = 3;
}

enum PropertyPermissionLevel {
  PROPERTY_PERMISSION_LEVEL_UNSPECIFIED = 0;
  PROPERTY_PERMISSION_LEVEL_PRIVATE = 1;
  PROPERTY_PERMISSION_LEVEL_SELF = 2;
  PROPERTY_PERMISSION_LEVEL_FRIENDS = 3;
  PROPERTY_PERMISSION_LEVEL_PUBLIC = 4;

```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10372"></a>
## FND-10372: chesscom.user_properties.v1.RangeModifier.RANGE_MODIFIER_CEIL = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RANGE_MODIFIER_CEIL = 2;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 209.

```text
roperties.v1;

enum RangeModifier {
  RANGE_MODIFIER_UNSPECIFIED = 0;
  RANGE_MODIFIER_RANGE = 1;
  RANGE_MODIFIER_CEIL = 2;
  RANGE_MODIFIER_FLOOR = 3;
}

enum PropertyPermissionLevel {
  PROPERTY_PERMISSION_LEVEL_UNSPECIFIED = 0;
  PROPERTY_PERMISSION_LEVEL_PRIVATE = 1;
  PROPERTY_PERMISSION_LEVEL_SELF = 2;
  PROPERTY_PERMISSION_LEVEL_FRIENDS = 3;
  PROPERTY_PERMISSION_LEVEL_PUBLIC = 4;
}

message PropertyDefinitio
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10373"></a>
## FND-10373: chesscom.user_properties.v1.RangeModifier.RANGE_MODIFIER_FLOOR = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RANGE_MODIFIER_FLOOR = 3;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 236.

```text
difier {
  RANGE_MODIFIER_UNSPECIFIED = 0;
  RANGE_MODIFIER_RANGE = 1;
  RANGE_MODIFIER_CEIL = 2;
  RANGE_MODIFIER_FLOOR = 3;
}

enum PropertyPermissionLevel {
  PROPERTY_PERMISSION_LEVEL_UNSPECIFIED = 0;
  PROPERTY_PERMISSION_LEVEL_PRIVATE = 1;
  PROPERTY_PERMISSION_LEVEL_SELF = 2;
  PROPERTY_PERMISSION_LEVEL_FRIENDS = 3;
  PROPERTY_PERMISSION_LEVEL_PUBLIC = 4;
}

message PropertyDefinitionMetadata {
  oneof user_ac
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10374"></a>
## FND-10374: enum declaration: chesscom.user_properties.v1.PropertyPermissionLevel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PropertyPermissionLevel {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 265.

```text
PECIFIED = 0;
  RANGE_MODIFIER_RANGE = 1;
  RANGE_MODIFIER_CEIL = 2;
  RANGE_MODIFIER_FLOOR = 3;
}

enum PropertyPermissionLevel {
  PROPERTY_PERMISSION_LEVEL_UNSPECIFIED = 0;
  PROPERTY_PERMISSION_LEVEL_PRIVATE = 1;
  PROPERTY_PERMISSION_LEVEL_SELF = 2;
  PROPERTY_PERMISSION_LEVEL_FRIENDS = 3;
  PROPERTY_PERMISSION_LEVEL_PUBLIC = 4;
}

message PropertyDefinitionMetadata {
  oneof user_activity_enrichment_transformer
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
