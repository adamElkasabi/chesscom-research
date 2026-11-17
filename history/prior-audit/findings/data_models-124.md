# data_models — findings 12301–12391

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-12575"></a>
## FND-12575: message declaration: chesscom.user_targeting.v1.Criterion

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Criterion {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1413.

```text
iterion criteria = 4;
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 6;
}

message Criterion {
  oneof _value {
  string value = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.BinaryOperatorModifier modifier = 4;
  }
  oneof _second_value {
  string second_value = 6;
  }
  optional string user_property = 1;
  optional .chesscom.user_targeting.v1.BinaryOperator binary_operator = 2;
 
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12576"></a>
## FND-12576: oneof declaration: chesscom.user_targeting.v1.Criterion._value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _value {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1435.

```text
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 6;
}

message Criterion {
  oneof _value {
  string value = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.BinaryOperatorModifier modifier = 4;
  }
  oneof _second_value {
  string second_value = 6;
  }
  optional string user_property = 1;
  optional .chesscom.user_targeting.v1.BinaryOperator binary_operator = 2;
  optional string key =
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12577"></a>
## FND-12577: chesscom.user_targeting.v1.Criterion.value = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string value = 3;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1452.

```text
com.user_targeting.v1.NestedCriteria criteria_groups = 6;
}

message Criterion {
  oneof _value {
  string value = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.BinaryOperatorModifier modifier = 4;
  }
  oneof _second_value {
  string second_value = 6;
  }
  optional string user_property = 1;
  optional .chesscom.user_targeting.v1.BinaryOperator binary_operator = 2;
  optional string key = 5;
}

message Bi
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12578"></a>
## FND-12578: oneof declaration: chesscom.user_targeting.v1.Criterion._modifier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _modifier {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1476.

```text
stedCriteria criteria_groups = 6;
}

message Criterion {
  oneof _value {
  string value = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.BinaryOperatorModifier modifier = 4;
  }
  oneof _second_value {
  string second_value = 6;
  }
  optional string user_property = 1;
  optional .chesscom.user_targeting.v1.BinaryOperator binary_operator = 2;
  optional string key = 5;
}

message BinaryOperatorModifier {
 
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12579"></a>
## FND-12579: chesscom.user_targeting.v1.Criterion.modifier = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_targeting.v1.BinaryOperatorModifier modifier = 4;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1496.

```text
a_groups = 6;
}

message Criterion {
  oneof _value {
  string value = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.BinaryOperatorModifier modifier = 4;
  }
  oneof _second_value {
  string second_value = 6;
  }
  optional string user_property = 1;
  optional .chesscom.user_targeting.v1.BinaryOperator binary_operator = 2;
  optional string key = 5;
}

message BinaryOperatorModifier {
  oneof time_windows 
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12580"></a>
## FND-12580: oneof declaration: chesscom.user_targeting.v1.Criterion._second_value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _second_value {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1567.

```text
3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.BinaryOperatorModifier modifier = 4;
  }
  oneof _second_value {
  string second_value = 6;
  }
  optional string user_property = 1;
  optional .chesscom.user_targeting.v1.BinaryOperator binary_operator = 2;
  optional string key = 5;
}

message BinaryOperatorModifier {
  oneof time_windows {
  .chesscom.user_targeting.v1.RelativeTimeWindows relative = 50;
  }

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12581"></a>
## FND-12581: chesscom.user_targeting.v1.Criterion.second_value = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string second_value = 6;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1591.

```text
 {
  .chesscom.user_targeting.v1.BinaryOperatorModifier modifier = 4;
  }
  oneof _second_value {
  string second_value = 6;
  }
  optional string user_property = 1;
  optional .chesscom.user_targeting.v1.BinaryOperator binary_operator = 2;
  optional string key = 5;
}

message BinaryOperatorModifier {
  oneof time_windows {
  .chesscom.user_targeting.v1.RelativeTimeWindows relative = 50;
  }
  oneof _is_negated {
  
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12582"></a>
## FND-12582: chesscom.user_targeting.v1.Criterion.user_property = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_property = 1;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1622.

```text
1.BinaryOperatorModifier modifier = 4;
  }
  oneof _second_value {
  string second_value = 6;
  }
  optional string user_property = 1;
  optional .chesscom.user_targeting.v1.BinaryOperator binary_operator = 2;
  optional string key = 5;
}

message BinaryOperatorModifier {
  oneof time_windows {
  .chesscom.user_targeting.v1.RelativeTimeWindows relative = 50;
  }
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneo
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12583"></a>
## FND-12583: chesscom.user_targeting.v1.Criterion.binary_operator = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_targeting.v1.BinaryOperator binary_operator = 2;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1659.

```text
;
  }
  oneof _second_value {
  string second_value = 6;
  }
  optional string user_property = 1;
  optional .chesscom.user_targeting.v1.BinaryOperator binary_operator = 2;
  optional string key = 5;
}

message BinaryOperatorModifier {
  oneof time_windows {
  .chesscom.user_targeting.v1.RelativeTimeWindows relative = 50;
  }
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _is_case_insensitive {
  bool is_ca
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12584"></a>
## FND-12584: chesscom.user_targeting.v1.Criterion.key = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 5;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1734.

```text
ing user_property = 1;
  optional .chesscom.user_targeting.v1.BinaryOperator binary_operator = 2;
  optional string key = 5;
}

message BinaryOperatorModifier {
  oneof time_windows {
  .chesscom.user_targeting.v1.RelativeTimeWindows relative = 50;
  }
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _is_case_insensitive {
  bool is_case_insensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12585"></a>
## FND-12585: message declaration: chesscom.user_targeting.v1.BinaryOperatorModifier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BinaryOperatorModifier {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1762.

```text
ional .chesscom.user_targeting.v1.BinaryOperator binary_operator = 2;
  optional string key = 5;
}

message BinaryOperatorModifier {
  oneof time_windows {
  .chesscom.user_targeting.v1.RelativeTimeWindows relative = 50;
  }
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _is_case_insensitive {
  bool is_case_insensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12586"></a>
## FND-12586: oneof declaration: chesscom.user_targeting.v1.BinaryOperatorModifier.time_windows

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof time_windows {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1797.

```text
inaryOperator binary_operator = 2;
  optional string key = 5;
}

message BinaryOperatorModifier {
  oneof time_windows {
  .chesscom.user_targeting.v1.RelativeTimeWindows relative = 50;
  }
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _is_case_insensitive {
  bool is_case_insensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
 
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12587"></a>
## FND-12587: chesscom.user_targeting.v1.BinaryOperatorModifier.relative = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_targeting.v1.RelativeTimeWindows relative = 50;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1820.

```text
erator = 2;
  optional string key = 5;
}

message BinaryOperatorModifier {
  oneof time_windows {
  .chesscom.user_targeting.v1.RelativeTimeWindows relative = 50;
  }
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _is_case_insensitive {
  bool is_case_insensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
  bool true_on_missing_v
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12588"></a>
## FND-12588: oneof declaration: chesscom.user_targeting.v1.BinaryOperatorModifier._is_negated

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_negated {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1889.

```text
ier {
  oneof time_windows {
  .chesscom.user_targeting.v1.RelativeTimeWindows relative = 50;
  }
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _is_case_insensitive {
  bool is_case_insensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
  bool true_on_missing_values = 4;
  }
  oneof _time_direction {
  .chesscom.user_targeting.v
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12589"></a>
## FND-12589: chesscom.user_targeting.v1.BinaryOperatorModifier.is_negated = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_negated = 1;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1911.

```text
dows {
  .chesscom.user_targeting.v1.RelativeTimeWindows relative = 50;
  }
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _is_case_insensitive {
  bool is_case_insensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
  bool true_on_missing_values = 4;
  }
  oneof _time_direction {
  .chesscom.user_targeting.v1.TimeDirection time_d
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12590"></a>
## FND-12590: oneof declaration: chesscom.user_targeting.v1.BinaryOperatorModifier._is_case_insensitive

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_case_insensitive {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1938.

```text
geting.v1.RelativeTimeWindows relative = 50;
  }
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _is_case_insensitive {
  bool is_case_insensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
  bool true_on_missing_values = 4;
  }
  oneof _time_direction {
  .chesscom.user_targeting.v1.TimeDirection time_direction = 5;
  }
  oneof _
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12591"></a>
## FND-12591: chesscom.user_targeting.v1.BinaryOperatorModifier.is_case_insensitive = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_case_insensitive = 2;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1969.

```text
elative = 50;
  }
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _is_case_insensitive {
  bool is_case_insensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
  bool true_on_missing_values = 4;
  }
  oneof _time_direction {
  .chesscom.user_targeting.v1.TimeDirection time_direction = 5;
  }
  oneof _second_time_unit {
  .chesscom.
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12592"></a>
## FND-12592: oneof declaration: chesscom.user_targeting.v1.BinaryOperatorModifier._time_unit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_unit {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2005.

```text
d {
  bool is_negated = 1;
  }
  oneof _is_case_insensitive {
  bool is_case_insensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
  bool true_on_missing_values = 4;
  }
  oneof _time_direction {
  .chesscom.user_targeting.v1.TimeDirection time_direction = 5;
  }
  oneof _second_time_unit {
  .chesscom.user_targeting.v1.TimeUnit second_ti
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12593"></a>
## FND-12593: chesscom.user_targeting.v1.BinaryOperatorModifier.time_unit = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_targeting.v1.TimeUnit time_unit = 3;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2026.

```text
 = 1;
  }
  oneof _is_case_insensitive {
  bool is_case_insensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
  bool true_on_missing_values = 4;
  }
  oneof _time_direction {
  .chesscom.user_targeting.v1.TimeDirection time_direction = 5;
  }
  oneof _second_time_unit {
  .chesscom.user_targeting.v1.TimeUnit second_time_unit = 6;
  }
  on
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12594"></a>
## FND-12594: oneof declaration: chesscom.user_targeting.v1.BinaryOperatorModifier._true_on_missing_values

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _true_on_missing_values {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2084.

```text
sensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
  bool true_on_missing_values = 4;
  }
  oneof _time_direction {
  .chesscom.user_targeting.v1.TimeDirection time_direction = 5;
  }
  oneof _second_time_unit {
  .chesscom.user_targeting.v1.TimeUnit second_time_unit = 6;
  }
  oneof _second_time_direction {
  .chesscom.user_targeting.v1
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12595"></a>
## FND-12595: chesscom.user_targeting.v1.BinaryOperatorModifier.true_on_missing_values = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool true_on_missing_values = 4;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2118.

```text
nit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
  bool true_on_missing_values = 4;
  }
  oneof _time_direction {
  .chesscom.user_targeting.v1.TimeDirection time_direction = 5;
  }
  oneof _second_time_unit {
  .chesscom.user_targeting.v1.TimeUnit second_time_unit = 6;
  }
  oneof _second_time_direction {
  .chesscom.user_targeting.v1.TimeDirection second_time_directi
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12596"></a>
## FND-12596: oneof declaration: chesscom.user_targeting.v1.BinaryOperatorModifier._time_direction

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_direction {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2157.

```text
eUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
  bool true_on_missing_values = 4;
  }
  oneof _time_direction {
  .chesscom.user_targeting.v1.TimeDirection time_direction = 5;
  }
  oneof _second_time_unit {
  .chesscom.user_targeting.v1.TimeUnit second_time_unit = 6;
  }
  oneof _second_time_direction {
  .chesscom.user_targeting.v1.TimeDirection second_time_direction = 7;
  }
}

message NestedCriteriaMo
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12597"></a>
## FND-12597: chesscom.user_targeting.v1.BinaryOperatorModifier.time_direction = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_targeting.v1.TimeDirection time_direction = 5;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2183.

```text
 oneof _true_on_missing_values {
  bool true_on_missing_values = 4;
  }
  oneof _time_direction {
  .chesscom.user_targeting.v1.TimeDirection time_direction = 5;
  }
  oneof _second_time_unit {
  .chesscom.user_targeting.v1.TimeUnit second_time_unit = 6;
  }
  oneof _second_time_direction {
  .chesscom.user_targeting.v1.TimeDirection second_time_direction = 7;
  }
}

message NestedCriteriaModifier {
  oneof _is_negat
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12598"></a>
## FND-12598: oneof declaration: chesscom.user_targeting.v1.BinaryOperatorModifier._second_time_unit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _second_time_unit {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2251.

```text
  }
  oneof _time_direction {
  .chesscom.user_targeting.v1.TimeDirection time_direction = 5;
  }
  oneof _second_time_unit {
  .chesscom.user_targeting.v1.TimeUnit second_time_unit = 6;
  }
  oneof _second_time_direction {
  .chesscom.user_targeting.v1.TimeDirection second_time_direction = 7;
  }
}

message NestedCriteriaModifier {
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _related_with_entity_type {

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12599"></a>
## FND-12599: chesscom.user_targeting.v1.BinaryOperatorModifier.second_time_unit = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_targeting.v1.TimeUnit second_time_unit = 6;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2279.

```text
{
  .chesscom.user_targeting.v1.TimeDirection time_direction = 5;
  }
  oneof _second_time_unit {
  .chesscom.user_targeting.v1.TimeUnit second_time_unit = 6;
  }
  oneof _second_time_direction {
  .chesscom.user_targeting.v1.TimeDirection second_time_direction = 7;
  }
}

message NestedCriteriaModifier {
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _related_with_entity_type {
  .chesscom.user_targeting.v
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12600"></a>
## FND-12600: oneof declaration: chesscom.user_targeting.v1.BinaryOperatorModifier._second_time_direction

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _second_time_direction {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2344.

```text

  }
  oneof _second_time_unit {
  .chesscom.user_targeting.v1.TimeUnit second_time_unit = 6;
  }
  oneof _second_time_direction {
  .chesscom.user_targeting.v1.TimeDirection second_time_direction = 7;
  }
}

message NestedCriteriaModifier {
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _related_with_entity_type {
  .chesscom.user_targeting.v1.DataSourceType related_with_entity_type = 2;
  }
  oneof _min_r
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12601"></a>
## FND-12601: chesscom.user_targeting.v1.BinaryOperatorModifier.second_time_direction = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_targeting.v1.TimeDirection second_time_direction = 7;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2377.

```text
  .chesscom.user_targeting.v1.TimeUnit second_time_unit = 6;
  }
  oneof _second_time_direction {
  .chesscom.user_targeting.v1.TimeDirection second_time_direction = 7;
  }
}

message NestedCriteriaModifier {
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _related_with_entity_type {
  .chesscom.user_targeting.v1.DataSourceType related_with_entity_type = 2;
  }
  oneof _min_relations_matching {
  int32 min_r
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12602"></a>
## FND-12602: message declaration: chesscom.user_targeting.v1.NestedCriteriaModifier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NestedCriteriaModifier {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2453.

```text
cond_time_direction {
  .chesscom.user_targeting.v1.TimeDirection second_time_direction = 7;
  }
}

message NestedCriteriaModifier {
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _related_with_entity_type {
  .chesscom.user_targeting.v1.DataSourceType related_with_entity_type = 2;
  }
  oneof _min_relations_matching {
  int32 min_relations_matching = 3;
  }
  oneof _max_relations_matching {
  int32 max_rel
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12603"></a>
## FND-12603: oneof declaration: chesscom.user_targeting.v1.NestedCriteriaModifier._is_negated

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_negated {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1889.

```text
ier {
  oneof time_windows {
  .chesscom.user_targeting.v1.RelativeTimeWindows relative = 50;
  }
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _is_case_insensitive {
  bool is_case_insensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
  bool true_on_missing_values = 4;
  }
  oneof _time_direction {
  .chesscom.user_targeting.v
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12604"></a>
## FND-12604: chesscom.user_targeting.v1.NestedCriteriaModifier.is_negated = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_negated = 1;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1911.

```text
dows {
  .chesscom.user_targeting.v1.RelativeTimeWindows relative = 50;
  }
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _is_case_insensitive {
  bool is_case_insensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
  bool true_on_missing_values = 4;
  }
  oneof _time_direction {
  .chesscom.user_targeting.v1.TimeDirection time_d
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12605"></a>
## FND-12605: oneof declaration: chesscom.user_targeting.v1.NestedCriteriaModifier._related_with_entity_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _related_with_entity_type {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2537.

```text
ion = 7;
  }
}

message NestedCriteriaModifier {
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _related_with_entity_type {
  .chesscom.user_targeting.v1.DataSourceType related_with_entity_type = 2;
  }
  oneof _min_relations_matching {
  int32 min_relations_matching = 3;
  }
  oneof _max_relations_matching {
  int32 max_relations_matching = 4;
  }
  oneof _data_source_identifier {
  string data_source_iden
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12606"></a>
## FND-12606: chesscom.user_targeting.v1.NestedCriteriaModifier.related_with_entity_type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_targeting.v1.DataSourceType related_with_entity_type = 2;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2573.

```text
iaModifier {
  oneof _is_negated {
  bool is_negated = 1;
  }
  oneof _related_with_entity_type {
  .chesscom.user_targeting.v1.DataSourceType related_with_entity_type = 2;
  }
  oneof _min_relations_matching {
  int32 min_relations_matching = 3;
  }
  oneof _max_relations_matching {
  int32 max_relations_matching = 4;
  }
  oneof _data_source_identifier {
  string data_source_identifier = 5;
  }
}

message RelativeT
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12607"></a>
## FND-12607: oneof declaration: chesscom.user_targeting.v1.NestedCriteriaModifier._min_relations_matching

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _min_relations_matching {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2652.

```text
with_entity_type {
  .chesscom.user_targeting.v1.DataSourceType related_with_entity_type = 2;
  }
  oneof _min_relations_matching {
  int32 min_relations_matching = 3;
  }
  oneof _max_relations_matching {
  int32 max_relations_matching = 4;
  }
  oneof _data_source_identifier {
  string data_source_identifier = 5;
  }
}

message RelativeTimeWindows {
  oneof _from {
  int32 from = 1;
  }
  oneof _to {
  int32 to = 2
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12608"></a>
## FND-12608: chesscom.user_targeting.v1.NestedCriteriaModifier.min_relations_matching = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 min_relations_matching = 3;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2686.

```text
r_targeting.v1.DataSourceType related_with_entity_type = 2;
  }
  oneof _min_relations_matching {
  int32 min_relations_matching = 3;
  }
  oneof _max_relations_matching {
  int32 max_relations_matching = 4;
  }
  oneof _data_source_identifier {
  string data_source_identifier = 5;
  }
}

message RelativeTimeWindows {
  oneof _from {
  int32 from = 1;
  }
  oneof _to {
  int32 to = 2;
  }
  oneof _time_unit {
  .ches
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12609"></a>
## FND-12609: oneof declaration: chesscom.user_targeting.v1.NestedCriteriaModifier._max_relations_matching

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_relations_matching {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2726.

```text
th_entity_type = 2;
  }
  oneof _min_relations_matching {
  int32 min_relations_matching = 3;
  }
  oneof _max_relations_matching {
  int32 max_relations_matching = 4;
  }
  oneof _data_source_identifier {
  string data_source_identifier = 5;
  }
}

message RelativeTimeWindows {
  oneof _from {
  int32 from = 1;
  }
  oneof _to {
  int32 to = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_uni
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12610"></a>
## FND-12610: chesscom.user_targeting.v1.NestedCriteriaModifier.max_relations_matching = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max_relations_matching = 4;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2760.

```text
in_relations_matching {
  int32 min_relations_matching = 3;
  }
  oneof _max_relations_matching {
  int32 max_relations_matching = 4;
  }
  oneof _data_source_identifier {
  string data_source_identifier = 5;
  }
}

message RelativeTimeWindows {
  oneof _from {
  int32 from = 1;
  }
  oneof _to {
  int32 to = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
}

message NestedCriter
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12611"></a>
## FND-12611: oneof declaration: chesscom.user_targeting.v1.NestedCriteriaModifier._data_source_identifier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _data_source_identifier {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2800.

```text
tions_matching = 3;
  }
  oneof _max_relations_matching {
  int32 max_relations_matching = 4;
  }
  oneof _data_source_identifier {
  string data_source_identifier = 5;
  }
}

message RelativeTimeWindows {
  oneof _from {
  int32 from = 1;
  }
  oneof _to {
  int32 to = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
}

message NestedCriteria {
  oneof _logical_operator {
  .ches
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12612"></a>
## FND-12612: chesscom.user_targeting.v1.NestedCriteriaModifier.data_source_identifier = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string data_source_identifier = 5;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2834.

```text
ax_relations_matching {
  int32 max_relations_matching = 4;
  }
  oneof _data_source_identifier {
  string data_source_identifier = 5;
  }
}

message RelativeTimeWindows {
  oneof _from {
  int32 from = 1;
  }
  oneof _to {
  int32 to = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
}

message NestedCriteria {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOper
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12613"></a>
## FND-12613: message declaration: chesscom.user_targeting.v1.RelativeTimeWindows

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RelativeTimeWindows {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2876.

```text
ons_matching = 4;
  }
  oneof _data_source_identifier {
  string data_source_identifier = 5;
  }
}

message RelativeTimeWindows {
  oneof _from {
  int32 from = 1;
  }
  oneof _to {
  int32 to = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
}

message NestedCriteria {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 3;
  }
  oneof _mo
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12614"></a>
## FND-12614: oneof declaration: chesscom.user_targeting.v1.RelativeTimeWindows._from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _from {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2908.

```text
ata_source_identifier {
  string data_source_identifier = 5;
  }
}

message RelativeTimeWindows {
  oneof _from {
  int32 from = 1;
  }
  oneof _to {
  int32 to = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
}

message NestedCriteria {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 3;
  }
  oneof _modifier {
  .chesscom.user_target
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12615"></a>
## FND-12615: chesscom.user_targeting.v1.RelativeTimeWindows.from = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 from = 1;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2924.

```text
ifier {
  string data_source_identifier = 5;
  }
}

message RelativeTimeWindows {
  oneof _from {
  int32 from = 1;
  }
  oneof _to {
  int32 to = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
}

message NestedCriteria {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.NestedCri
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12616"></a>
## FND-12616: oneof declaration: chesscom.user_targeting.v1.RelativeTimeWindows._to

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _to {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2946.

```text
source_identifier = 5;
  }
}

message RelativeTimeWindows {
  oneof _from {
  int32 from = 1;
  }
  oneof _to {
  int32 to = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
}

message NestedCriteria {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.NestedCriteriaModifier modifier
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12617"></a>
## FND-12617: chesscom.user_targeting.v1.RelativeTimeWindows.to = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 to = 2;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2960.

```text
ier = 5;
  }
}

message RelativeTimeWindows {
  oneof _from {
  int32 from = 1;
  }
  oneof _to {
  int32 to = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
}

message NestedCriteria {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.NestedCriteriaModifier modifier = 4;
  }
  re
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12618"></a>
## FND-12618: oneof declaration: chesscom.user_targeting.v1.RelativeTimeWindows._time_unit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_unit {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2005.

```text
d {
  bool is_negated = 1;
  }
  oneof _is_case_insensitive {
  bool is_case_insensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
  bool true_on_missing_values = 4;
  }
  oneof _time_direction {
  .chesscom.user_targeting.v1.TimeDirection time_direction = 5;
  }
  oneof _second_time_unit {
  .chesscom.user_targeting.v1.TimeUnit second_ti
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12619"></a>
## FND-12619: chesscom.user_targeting.v1.RelativeTimeWindows.time_unit = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_targeting.v1.TimeUnit time_unit = 3;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 2026.

```text
 = 1;
  }
  oneof _is_case_insensitive {
  bool is_case_insensitive = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
  oneof _true_on_missing_values {
  bool true_on_missing_values = 4;
  }
  oneof _time_direction {
  .chesscom.user_targeting.v1.TimeDirection time_direction = 5;
  }
  oneof _second_time_unit {
  .chesscom.user_targeting.v1.TimeUnit second_time_unit = 6;
  }
  on
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12620"></a>
## FND-12620: message declaration: chesscom.user_targeting.v1.NestedCriteria

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NestedCriteria {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 3060.

```text
int32 to = 2;
  }
  oneof _time_unit {
  .chesscom.user_targeting.v1.TimeUnit time_unit = 3;
  }
}

message NestedCriteria {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.NestedCriteriaModifier modifier = 4;
  }
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 1;
  repeated .chesscom.user_tar
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12621"></a>
## FND-12621: oneof declaration: chesscom.user_targeting.v1.NestedCriteria._logical_operator

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _logical_operator {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1090.

```text
{
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 4;
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 6;

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12622"></a>
## FND-12622: chesscom.user_targeting.v1.NestedCriteria.logical_operator = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_targeting.v1.LogicalOperator logical_operator = 3;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 3115.

```text
_targeting.v1.TimeUnit time_unit = 3;
  }
}

message NestedCriteria {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.NestedCriteriaModifier modifier = 4;
  }
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 1;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 2;
}

message Sort {
  o
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12623"></a>
## FND-12623: oneof declaration: chesscom.user_targeting.v1.NestedCriteria._modifier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _modifier {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1476.

```text
stedCriteria criteria_groups = 6;
}

message Criterion {
  oneof _value {
  string value = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.BinaryOperatorModifier modifier = 4;
  }
  oneof _second_value {
  string second_value = 6;
  }
  optional string user_property = 1;
  optional .chesscom.user_targeting.v1.BinaryOperator binary_operator = 2;
  optional string key = 5;
}

message BinaryOperatorModifier {
 
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12624"></a>
## FND-12624: chesscom.user_targeting.v1.NestedCriteria.modifier = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_targeting.v1.NestedCriteriaModifier modifier = 4;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 3207.

```text
tor {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.NestedCriteriaModifier modifier = 4;
  }
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 1;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 2;
}

message Sort {
  oneof _sort_order {
  .chesscom.user_targeting.v1.SortOrder sort_order = 2;
  }
  optional st
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12625"></a>
## FND-12625: chesscom.user_targeting.v1.NestedCriteria.criteria_groups = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 1;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 3278.

```text
3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.NestedCriteriaModifier modifier = 4;
  }
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 1;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 2;
}

message Sort {
  oneof _sort_order {
  .chesscom.user_targeting.v1.SortOrder sort_order = 2;
  }
  optional string key = 1;
}

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12626"></a>
## FND-12626: chesscom.user_targeting.v1.NestedCriteria.criteria = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_targeting.v1.Criterion criteria = 2;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 3353.

```text
fier modifier = 4;
  }
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 1;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 2;
}

message Sort {
  oneof _sort_order {
  .chesscom.user_targeting.v1.SortOrder sort_order = 2;
  }
  optional string key = 1;
}

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12627"></a>
## FND-12627: message declaration: chesscom.user_targeting.v1.Sort

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Sort {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 3417.

```text
stedCriteria criteria_groups = 1;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 2;
}

message Sort {
  oneof _sort_order {
  .chesscom.user_targeting.v1.SortOrder sort_order = 2;
  }
  optional string key = 1;
}

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12628"></a>
## FND-12628: oneof declaration: chesscom.user_targeting.v1.Sort._sort_order

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _sort_order {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 3434.

```text
eria_groups = 1;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 2;
}

message Sort {
  oneof _sort_order {
  .chesscom.user_targeting.v1.SortOrder sort_order = 2;
  }
  optional string key = 1;
}

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12629"></a>
## FND-12629: chesscom.user_targeting.v1.Sort.sort_order = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_targeting.v1.SortOrder sort_order = 2;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 3456.

```text
eated .chesscom.user_targeting.v1.Criterion criteria = 2;
}

message Sort {
  oneof _sort_order {
  .chesscom.user_targeting.v1.SortOrder sort_order = 2;
  }
  optional string key = 1;
}

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12630"></a>
## FND-12630: chesscom.user_targeting.v1.Sort.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1190.

```text
oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 4;
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 6;
}

message Criterion {
  oneof _value {
  string value = 3;
  }
  oneof _modifier {
  .chesscom.user
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12631"></a>
## FND-12631: message declaration: google.protobuf.Any

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Any {

### Evidence

- **SRC-0650** `research/proto/google/protobuf/any.proto` — [preserved redacted evidence](../evidence/text/a0d4f8867d12205accf8412c60e1f6dbdb2f063d4ac60b91f7eecf65bf9bf9a4.proto)
  Character offset 82.

```text
// source: google/protobuf/any.proto
// syntax: proto3

package google.protobuf;

message Any {
  optional string type_url = 1;
  optional bytes value = 2;
}

```

**Source references:** SRC-0650, SRC-1621  
**URL references:** None independently associated  
**Related findings:** FND-12632, FND-12633

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12632"></a>
## FND-12632: google.protobuf.Any.type_url = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string type_url = 1;

### Evidence

- **SRC-0650** `research/proto/google/protobuf/any.proto` — [preserved redacted evidence](../evidence/text/a0d4f8867d12205accf8412c60e1f6dbdb2f063d4ac60b91f7eecf65bf9bf9a4.proto)
  Character offset 98.

```text
// source: google/protobuf/any.proto
// syntax: proto3

package google.protobuf;

message Any {
  optional string type_url = 1;
  optional bytes value = 2;
}

```

**Source references:** SRC-0650, SRC-1621  
**URL references:** None independently associated  
**Related findings:** FND-12631, FND-12633

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12633"></a>
## FND-12633: google.protobuf.Any.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bytes value = 2;

### Evidence

- **SRC-0650** `research/proto/google/protobuf/any.proto` — [preserved redacted evidence](../evidence/text/a0d4f8867d12205accf8412c60e1f6dbdb2f063d4ac60b91f7eecf65bf9bf9a4.proto)
  Character offset 130.

```text
.proto
// syntax: proto3

package google.protobuf;

message Any {
  optional string type_url = 1;
  optional bytes value = 2;
}

```

**Source references:** SRC-0650, SRC-1621  
**URL references:** None independently associated  
**Related findings:** FND-12631, FND-12632

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12634"></a>
## FND-12634: message declaration: google.protobuf.Duration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Duration {

### Evidence

- **SRC-0651** `research/proto/google/protobuf/duration.proto` — [preserved redacted evidence](../evidence/text/fdcba2cacfec3d23f2243080281fdb2093a7508041f090ad4253b922d7da78f5.proto)
  Character offset 87.

```text
// source: google/protobuf/duration.proto
// syntax: proto3

package google.protobuf;

message Duration {
  optional int64 seconds = 1;
  optional int32 nanos = 2;
}

```

**Source references:** SRC-0651, SRC-1622  
**URL references:** None independently associated  
**Related findings:** FND-12635, FND-12636

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12635"></a>
## FND-12635: google.protobuf.Duration.seconds = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 seconds = 1;

### Evidence

- **SRC-0651** `research/proto/google/protobuf/duration.proto` — [preserved redacted evidence](../evidence/text/fdcba2cacfec3d23f2243080281fdb2093a7508041f090ad4253b922d7da78f5.proto)
  Character offset 108.

```text
e: google/protobuf/duration.proto
// syntax: proto3

package google.protobuf;

message Duration {
  optional int64 seconds = 1;
  optional int32 nanos = 2;
}

```

**Source references:** SRC-0651, SRC-1622  
**URL references:** None independently associated  
**Related findings:** FND-12634, FND-12636

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12636"></a>
## FND-12636: google.protobuf.Duration.nanos = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 nanos = 2;

### Evidence

- **SRC-0651** `research/proto/google/protobuf/duration.proto` — [preserved redacted evidence](../evidence/text/fdcba2cacfec3d23f2243080281fdb2093a7508041f090ad4253b922d7da78f5.proto)
  Character offset 138.

```text
oto
// syntax: proto3

package google.protobuf;

message Duration {
  optional int64 seconds = 1;
  optional int32 nanos = 2;
}

```

**Source references:** SRC-0651, SRC-1622  
**URL references:** None independently associated  
**Related findings:** FND-12634, FND-12635

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12637"></a>
## FND-12637: message declaration: google.protobuf.Empty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Empty {

### Evidence

- **SRC-0652** `research/proto/google/protobuf/empty.proto` — [preserved redacted evidence](../evidence/text/8b5841292fcaa8f62fb6fe698c0e317ed4543ccf21b53284808ead3a59e2fcd8.proto)
  Character offset 84.

```text
// source: google/protobuf/empty.proto
// syntax: proto3

package google.protobuf;

message Empty {
}

```

**Source references:** SRC-0652, SRC-1623  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12638"></a>
## FND-12638: message declaration: google.protobuf.FieldMask

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FieldMask {

### Evidence

- **SRC-0653** `research/proto/google/protobuf/field_mask.proto` — [preserved redacted evidence](../evidence/text/015c71a0c00eb2785937c5f846e2c9c87f35922cc3b8a86a13da5d22c62a20d0.proto)
  Character offset 89.

```text
// source: google/protobuf/field_mask.proto
// syntax: proto3

package google.protobuf;

message FieldMask {
  repeated string paths = 1;
}

```

**Source references:** SRC-0653, SRC-1624  
**URL references:** None independently associated  
**Related findings:** FND-12639

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12639"></a>
## FND-12639: google.protobuf.FieldMask.paths = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string paths = 1;

### Evidence

- **SRC-0653** `research/proto/google/protobuf/field_mask.proto` — [preserved redacted evidence](../evidence/text/015c71a0c00eb2785937c5f846e2c9c87f35922cc3b8a86a13da5d22c62a20d0.proto)
  Character offset 111.

```text
google/protobuf/field_mask.proto
// syntax: proto3

package google.protobuf;

message FieldMask {
  repeated string paths = 1;
}

```

**Source references:** SRC-0653, SRC-1624  
**URL references:** None independently associated  
**Related findings:** FND-12638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12640"></a>
## FND-12640: enum declaration: google.protobuf.NullValue

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum NullValue {

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 85.

```text
// source: google/protobuf/struct.proto
// syntax: proto3

package google.protobuf;

enum NullValue {
  NULL_VALUE = 0;
}

message Struct {
  repeated .google.protobuf.Struct.FieldsEntry fields = 1;
  message FieldsEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message Value {
  oneof kind {
  .google.protobuf.NullValue null_value = 1;
  double number_value = 2;

```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12641, FND-12642

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12641"></a>
## FND-12641: google.protobuf.NullValue.NULL_VALUE = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NULL_VALUE = 0;

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 104.

```text
ource: google/protobuf/struct.proto
// syntax: proto3

package google.protobuf;

enum NullValue {
  NULL_VALUE = 0;
}

message Struct {
  repeated .google.protobuf.Struct.FieldsEntry fields = 1;
  message FieldsEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message Value {
  oneof kind {
  .google.protobuf.NullValue null_value = 1;
  double number_value = 2;
  string string_val
```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12642

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12642"></a>
## FND-12642: message declaration: google.protobuf.Struct

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Struct {

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 123.

```text
buf/struct.proto
// syntax: proto3

package google.protobuf;

enum NullValue {
  NULL_VALUE = 0;
}

message Struct {
  repeated .google.protobuf.Struct.FieldsEntry fields = 1;
  message FieldsEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message Value {
  oneof kind {
  .google.protobuf.NullValue null_value = 1;
  double number_value = 2;
  string string_value = 3;
  bool bool
```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12643"></a>
## FND-12643: google.protobuf.Struct.fields = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .google.protobuf.Struct.FieldsEntry fields = 1;

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 142.

```text
 syntax: proto3

package google.protobuf;

enum NullValue {
  NULL_VALUE = 0;
}

message Struct {
  repeated .google.protobuf.Struct.FieldsEntry fields = 1;
  message FieldsEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message Value {
  oneof kind {
  .google.protobuf.NullValue null_value = 1;
  double number_value = 2;
  string string_value = 3;
  bool bool_value = 4;
  .goog
```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641, FND-12642

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12644"></a>
## FND-12644: message declaration: google.protobuf.Struct.FieldsEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FieldsEntry {

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 201.

```text

  NULL_VALUE = 0;
}

message Struct {
  repeated .google.protobuf.Struct.FieldsEntry fields = 1;
  message FieldsEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message Value {
  oneof kind {
  .google.protobuf.NullValue null_value = 1;
  double number_value = 2;
  string string_value = 3;
  bool bool_value = 4;
  .google.protobuf.Struct struct_value = 5;
  .google.protobuf.Lis
```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641, FND-12642

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12645"></a>
## FND-12645: google.protobuf.Struct.FieldsEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 225.

```text
ssage Struct {
  repeated .google.protobuf.Struct.FieldsEntry fields = 1;
  message FieldsEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message Value {
  oneof kind {
  .google.protobuf.NullValue null_value = 1;
  double number_value = 2;
  string string_value = 3;
  bool bool_value = 4;
  .google.protobuf.Struct struct_value = 5;
  .google.protobuf.ListValue list_value = 6;
 
```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641, FND-12642

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12646"></a>
## FND-12646: google.protobuf.Struct.FieldsEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Value value = 2;

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 252.

```text
google.protobuf.Struct.FieldsEntry fields = 1;
  message FieldsEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message Value {
  oneof kind {
  .google.protobuf.NullValue null_value = 1;
  double number_value = 2;
  string string_value = 3;
  bool bool_value = 4;
  .google.protobuf.Struct struct_value = 5;
  .google.protobuf.ListValue list_value = 6;
  }
}

message ListValue {
 
```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641, FND-12642

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12647"></a>
## FND-12647: message declaration: google.protobuf.Value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Value {

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 302.

```text
essage FieldsEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message Value {
  oneof kind {
  .google.protobuf.NullValue null_value = 1;
  double number_value = 2;
  string string_value = 3;
  bool bool_value = 4;
  .google.protobuf.Struct struct_value = 5;
  .google.protobuf.ListValue list_value = 6;
  }
}

message ListValue {
  repeated .google.protobuf.Value values = 1;
}

```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641, FND-12642

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12648"></a>
## FND-12648: oneof declaration: google.protobuf.Value.kind

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof kind {

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 320.

```text
 {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message Value {
  oneof kind {
  .google.protobuf.NullValue null_value = 1;
  double number_value = 2;
  string string_value = 3;
  bool bool_value = 4;
  .google.protobuf.Struct struct_value = 5;
  .google.protobuf.ListValue list_value = 6;
  }
}

message ListValue {
  repeated .google.protobuf.Value values = 1;
}

```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641, FND-12642

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12649"></a>
## FND-12649: google.protobuf.Value.null_value = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.NullValue null_value = 1;

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 335.

```text
tring key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message Value {
  oneof kind {
  .google.protobuf.NullValue null_value = 1;
  double number_value = 2;
  string string_value = 3;
  bool bool_value = 4;
  .google.protobuf.Struct struct_value = 5;
  .google.protobuf.ListValue list_value = 6;
  }
}

message ListValue {
  repeated .google.protobuf.Value values = 1;
}

```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641, FND-12642

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12650"></a>
## FND-12650: google.protobuf.Value.number_value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double number_value = 2;

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 380.

```text
lue value = 2;
  }
}

message Value {
  oneof kind {
  .google.protobuf.NullValue null_value = 1;
  double number_value = 2;
  string string_value = 3;
  bool bool_value = 4;
  .google.protobuf.Struct struct_value = 5;
  .google.protobuf.ListValue list_value = 6;
  }
}

message ListValue {
  repeated .google.protobuf.Value values = 1;
}

```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641, FND-12642

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12651"></a>
## FND-12651: google.protobuf.Value.string_value = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string string_value = 3;

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 407.

```text
ge Value {
  oneof kind {
  .google.protobuf.NullValue null_value = 1;
  double number_value = 2;
  string string_value = 3;
  bool bool_value = 4;
  .google.protobuf.Struct struct_value = 5;
  .google.protobuf.ListValue list_value = 6;
  }
}

message ListValue {
  repeated .google.protobuf.Value values = 1;
}

```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641, FND-12642

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12652"></a>
## FND-12652: google.protobuf.Value.bool_value = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool bool_value = 4;

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 434.

```text
 .google.protobuf.NullValue null_value = 1;
  double number_value = 2;
  string string_value = 3;
  bool bool_value = 4;
  .google.protobuf.Struct struct_value = 5;
  .google.protobuf.ListValue list_value = 6;
  }
}

message ListValue {
  repeated .google.protobuf.Value values = 1;
}

```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641, FND-12642

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12653"></a>
## FND-12653: google.protobuf.Value.struct_value = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Struct struct_value = 5;

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 457.

```text
alue null_value = 1;
  double number_value = 2;
  string string_value = 3;
  bool bool_value = 4;
  .google.protobuf.Struct struct_value = 5;
  .google.protobuf.ListValue list_value = 6;
  }
}

message ListValue {
  repeated .google.protobuf.Value values = 1;
}

```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641, FND-12642

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12654"></a>
## FND-12654: google.protobuf.Value.list_value = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.ListValue list_value = 6;

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 501.

```text
 2;
  string string_value = 3;
  bool bool_value = 4;
  .google.protobuf.Struct struct_value = 5;
  .google.protobuf.ListValue list_value = 6;
  }
}

message ListValue {
  repeated .google.protobuf.Value values = 1;
}

```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641, FND-12642

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12655"></a>
## FND-12655: message declaration: google.protobuf.ListValue

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListValue {

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 551.

```text
 4;
  .google.protobuf.Struct struct_value = 5;
  .google.protobuf.ListValue list_value = 6;
  }
}

message ListValue {
  repeated .google.protobuf.Value values = 1;
}

```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641, FND-12642

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12656"></a>
## FND-12656: google.protobuf.ListValue.values = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .google.protobuf.Value values = 1;

### Evidence

- **SRC-0654** `research/proto/google/protobuf/struct.proto` — [preserved redacted evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto)
  Character offset 573.

```text
.Struct struct_value = 5;
  .google.protobuf.ListValue list_value = 6;
  }
}

message ListValue {
  repeated .google.protobuf.Value values = 1;
}

```

**Source references:** SRC-0654, SRC-1625  
**URL references:** None independently associated  
**Related findings:** FND-12640, FND-12641, FND-12642

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12657"></a>
## FND-12657: message declaration: google.protobuf.Timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Timestamp {

### Evidence

- **SRC-0655** `research/proto/google/protobuf/timestamp.proto` — [preserved redacted evidence](../evidence/text/a748421bf54d9c568ff1c578cb2476b41321619a634adf5c80bca407c086100b.proto)
  Character offset 88.

```text
// source: google/protobuf/timestamp.proto
// syntax: proto3

package google.protobuf;

message Timestamp {
  optional int64 seconds = 1;
  optional int32 nanos = 2;
}

```

**Source references:** SRC-0655, SRC-1626  
**URL references:** None independently associated  
**Related findings:** FND-12658, FND-12659

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12658"></a>
## FND-12658: google.protobuf.Timestamp.seconds = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 seconds = 1;

### Evidence

- **SRC-0655** `research/proto/google/protobuf/timestamp.proto` — [preserved redacted evidence](../evidence/text/a748421bf54d9c568ff1c578cb2476b41321619a634adf5c80bca407c086100b.proto)
  Character offset 110.

```text
 google/protobuf/timestamp.proto
// syntax: proto3

package google.protobuf;

message Timestamp {
  optional int64 seconds = 1;
  optional int32 nanos = 2;
}

```

**Source references:** SRC-0655, SRC-1626  
**URL references:** None independently associated  
**Related findings:** FND-12657, FND-12659

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12659"></a>
## FND-12659: google.protobuf.Timestamp.nanos = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 nanos = 2;

### Evidence

- **SRC-0655** `research/proto/google/protobuf/timestamp.proto` — [preserved redacted evidence](../evidence/text/a748421bf54d9c568ff1c578cb2476b41321619a634adf5c80bca407c086100b.proto)
  Character offset 140.

```text
to
// syntax: proto3

package google.protobuf;

message Timestamp {
  optional int64 seconds = 1;
  optional int32 nanos = 2;
}

```

**Source references:** SRC-0655, SRC-1626  
**URL references:** None independently associated  
**Related findings:** FND-12657, FND-12658

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-18890"></a>
## FND-18890: Full frontend descriptors retain service metadata omitted by old rendered schemas

**Category:** data_models  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

The original extension/lib/descriptors.js contains base64 FileDescriptorProto blobs. The older research/extract_desc.py renderer handles messages/enums but drops service declarations and some options. This recovery decodes the authoritative original registry offline,retaining full JSON and RPC methods in registries/frontend-descriptors and rpc-services.json. This is new extraction of existing evidence,not a new network investigation.

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 319.

```text
ndle's `J()` helper).
// Personal-use reverse engineering artifact. Not redistributed.
export const DESCRIPTORS = {"google/protobuf/timestamp.proto":"Ch9nb29nbGUvcHJvdG9idWYvdGltZXN0YW1wLnByb3RvEg9nb29nbGUucHJvdG9idWYiKwoJVGltZXN0YW1wEg8KB3NlY29uZHMYASABKAMSDQoFbmFub3MYAiABKAVChQEKE2NvbS5nb29nbGUucHJvdG9idWZCDlRpbWVzdGFtcFByb3RvUAFaMmdvb2dsZS5nb2xhbmcub3JnL3Byb3RvYnVmL3R5cGVzL2tub3duL3RpbWVzdGFtcHBi+AEBogIDR1BCqgIeR2
```
- **SRC-0124** `research/extract_desc.py` — [preserved redacted evidence](../evidence/text/3f5cb2b88101cc5b85af653203fffdb91377b3961f22a8bf8be335fb9ae2125c.py)

**Source references:** SRC-0045, SRC-0124  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18912"></a>
## FND-18912: Compact CEE classification enum differs from legacy analysis enum

**Category:** data_models  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

chesscom.explanation_engine.v1.MoveClassification uses Mistake8,Blunder9,Missed10,Forced11,Tricky20. chesscom.analysis.v1.MoveClassification uses Mistake11,Blunder15,Forced19,Miss20 and phase splits. Do not decode CEE output using the legacy32-value table.

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 441.

```text
ASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_TRICKY = 20;
}

enum MoveClassificationVersion {
  MOVE_CLASSIFICATION_VERSION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_VERSION_V2 = 1;
  MOVE_CLASSIFICATION_VERS
```
- **SRC-0206** `research/proto/chesscom/analysis/v1/move_classifications.proto` — [preserved redacted evidence](../evidence/text/6e1b7e8e4f787511e0a30503f542c79c0919fbb086112dd57b67f0b1490606fd.proto)
- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)

**Source references:** SRC-0414, SRC-0206, SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061, FND-00275, FND-00276

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18913"></a>
## FND-18913: MoveClassificationVersion numeric names

**Category:** data_models  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CEE version UNSPECIFIED0,V2=1,V3=2. Sweep labels such as class-v2/ClassificationV3 must be interpreted through actual config fields, not their informal label; a "class0" omitted setting is not an explicit algorithm-version0 run.

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 622.

```text
FICATION_MISSED = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_TRICKY = 20;
}

enum MoveClassificationVersion {
  MOVE_CLASSIFICATION_VERSION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_VERSION_V2 = 1;
  MOVE_CLASSIFICATION_VERSION_V3 = 2;
}

message EvalClassification {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional .chesscom.engine.v1.Evaluation evaluati
```
- **SRC-0869** `research/refinement/sweep.mjs` — [preserved redacted evidence](../evidence/text/07d6432e87a9745880904485680ea6dbdbc545aca922f2c55ffc066941fbba9c.mjs)

**Source references:** SRC-0414, SRC-0869  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061, FND-18967, FND-18973

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18914"></a>
## FND-18914: White-point-of-view scores and board-bar pawn scores

**Category:** data_models  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Native chess Score can encode score_centipawns_white or mate cases. UI conversion divides CP by100. Legacy evaluation-bar payload uses pawns and White POV; UCI side-to-move scores must be normalized by the wrapper. Always preserve the namespace/unit rather than assuming all score fields have identical meaning.

### Evidence

- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Character offset 15276.

```text
he shared currency everywhere (`chesscom/chess/v1/score.proto`):

```proto
message Score {
  sint32 score_centipawns_white = 1;   // always white's point of view
  int32  mate_in_white          = 2;
  int32  mate_in_black          = 3;
  Stalemate stalemate           = 4;
}
```

The client immediately converts it to pawns (`zU()`, offset ≈ 1,699,000):
`cp = score_centipawns_white / 100` (`Tqe = 100`), mate → `±1000` 
```
- **SRC-2048** `uploads/REVERSE-ENGINEERING.md` — [preserved redacted evidence](../evidence/text/6baef459d177ce57b003a33a273327c13e793a1236190f942fe7669797fdb50c.md)
- **SRC-0048** `extension/lib/protobuf.js` — [preserved redacted evidence](../evidence/text/9bfe315bd2c6c56a3c843cfd78efac6ff20485db2d0ca073cc752b1266e44e5a.js)

**Source references:** SRC-2047, SRC-2048, SRC-0048  
**URL references:** None independently associated  
**Related findings:** FND-00085, FND-00086, FND-00087, FND-00217, FND-00218

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18915"></a>
## FND-18915: Skills hash prerequisites do not prove cryptographic security

**Category:** data_models  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Frontend logs say CEE needs White user ID,Black user ID,game ID to sign validationHash and warns it will be empty otherwise. The log wording and schema support dependency/intent, not an independently assessed signature algorithm, server validation behavior, or guaranteed skill credit.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 1710227.

```text
ayedMove?.boardMarkings,d=e.skillsEarned,f=d?.skills&&d.skills.length?{ply:d.ply??0,skills:d.skills,validationHash:d.validationHash??``}:void 0;return{analysisTypes:yj,color:xqe(e.movedColor),suggestedMove:l,bestAlternativeMove:c,playedMove:{...n,coachEmotion:Sqe(e.coachEmotion),variationThemes:o,...u?{contextualArrows:vJe(u)}:{},...f?{skillsEarned:f}:{}},classificationName:a,isCriticalPosition:!1,isKeyMoment:i,scena
```
- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Character offset 29188.

```text
n the ids CEE needs are missing:

```
'0/3 IDL /v2/game-review — skills on; CEE has the ids to sign validationHash'
'0/3 IDL /v2/game-review — skills on but MISSING ids CEE needs; validationHash will come back empty'
```

CEE needs **white user id, black user id and game id** to sign. A game without
all three (guest, anonymous import) gets an empty hash and therefore no
persisted skill credit.

### 9.3 Explanations


```

**Source references:** SRC-1137, SRC-2047  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117, FND-00085, FND-00086

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18916"></a>
## FND-18916: Both native and frontend metadata versions are retained

**Category:** data_models  
**Classification:** inference  
**Verification:** partially verified  
**Confidence:** medium — Exact content of the cited stored artifact; not a claim of current live deployment.

CEE startup banner1.130.285 and review metadata1.211.5 were recorded in different contexts. They may refer to packaging/API metadata versus internal engine build. Do not overwrite one with the other or conclude a contradiction without a version mapping.

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 19.

```text
Explanation Engine 1.130.285 (C) 2025 Chess.com, LLC
info string CEE
option name LogFD default -1
option name IllegalMoveExplanationMode default all
option name ForceDisableInternalEngineSearches default false
option name PlayVsCoachRetryMissesEnabled default false
option name GameFinishedAtMs default 0
option name Threads default 1
opti
```
- **SRC-0109** `research/doting-cee-baseline.json` — [preserved redacted evidence](../evidence/text/f20a1fa1142b6cf57a0920249bd12b40a94624dcc57ac221168e9a8d120fd205.json)
- **SRC-2049** `accessible-conversation/current-and-condensed-history` — [preserved redacted evidence](../evidence/text/b295bb5af6a3f9a3463e5be596f3ba2ea176d41d66915d311049a0980c38495a.txt)
  Character offset 3066.

```text
code/artifacts where available rather than relying on this condensed statement.
- Runtime CEE banner1.130.285 and review metadata1.211.5 both appeared; these version namespaces must not automatically be treated as contradictory.

Visible follow-up investigation:
- User supplied https://www.chess.com/game/live/187158515860 as an example of a page loading explanation-engine.js/.wasm. A fetch_page result displayed game 
```

**Source references:** SRC-0874, SRC-0109, SRC-2049  
**URL references:** None independently associated  
**Related findings:** FND-19030, FND-19031, FND-18427, FND-18428, FND-18429

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
