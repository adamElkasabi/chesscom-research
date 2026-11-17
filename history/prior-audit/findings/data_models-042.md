# data_models — findings 4101–4200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-04375"></a>
## FND-04375: oneof declaration: chesscom.explanation_engine.v1.SearchParameters._num_threads

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _num_threads {

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 890.

```text
_line_strategy {
  .chesscom.explanation_engine.v1.MultiLineStrategy multi_line_strategy = 5;
  }
  oneof _num_threads {
  int32 num_threads = 6;
  }
}

message GameReviewSearchSettings {
  optional .chesscom.engine.v1.Strength strength = 1;
}

```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04376"></a>
## FND-04376: chesscom.explanation_engine.v1.SearchParameters.num_threads = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 num_threads = 6;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 913.

```text
sscom.explanation_engine.v1.MultiLineStrategy multi_line_strategy = 5;
  }
  oneof _num_threads {
  int32 num_threads = 6;
  }
}

message GameReviewSearchSettings {
  optional .chesscom.engine.v1.Strength strength = 1;
}

```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04377"></a>
## FND-04377: message declaration: chesscom.explanation_engine.v1.GameReviewSearchSettings

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewSearchSettings {

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 943.

```text
ltiLineStrategy multi_line_strategy = 5;
  }
  oneof _num_threads {
  int32 num_threads = 6;
  }
}

message GameReviewSearchSettings {
  optional .chesscom.engine.v1.Strength strength = 1;
}

```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04378"></a>
## FND-04378: chesscom.explanation_engine.v1.GameReviewSearchSettings.strength = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.engine.v1.Strength strength = 1;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 980.

```text
 5;
  }
  oneof _num_threads {
  int32 num_threads = 6;
  }
}

message GameReviewSearchSettings {
  optional .chesscom.engine.v1.Strength strength = 1;
}

```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04379"></a>
## FND-04379: message declaration: chesscom.explanation_engine.v1.SimpleCharmMovePrediction

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SimpleCharmMovePrediction {

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 131.

```text
_engine/v1/simple_charm_inference.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message SimpleCharmMovePrediction {
  optional string uci_move = 1;
  optional float probability = 2;
}

message SimpleCharmInference {
  oneof _rating {
  int32 rating = 2;
  }
  oneof _expected_points {
  float expected_points = 4;
  }
  optional string model_key = 1;
  repeated .chesscom.explanation_engine.v1.Simple
```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04380, FND-04381

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04380"></a>
## FND-04380: chesscom.explanation_engine.v1.SimpleCharmMovePrediction.uci_move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string uci_move = 1;

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 169.

```text
o
// syntax: proto3

package chesscom.explanation_engine.v1;

message SimpleCharmMovePrediction {
  optional string uci_move = 1;
  optional float probability = 2;
}

message SimpleCharmInference {
  oneof _rating {
  int32 rating = 2;
  }
  oneof _expected_points {
  float expected_points = 4;
  }
  optional string model_key = 1;
  repeated .chesscom.explanation_engine.v1.SimpleCharmMovePrediction moves = 3;
  repea
```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04381

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04381"></a>
## FND-04381: chesscom.explanation_engine.v1.SimpleCharmMovePrediction.probability = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float probability = 2;

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 201.

```text
sscom.explanation_engine.v1;

message SimpleCharmMovePrediction {
  optional string uci_move = 1;
  optional float probability = 2;
}

message SimpleCharmInference {
  oneof _rating {
  int32 rating = 2;
  }
  oneof _expected_points {
  float expected_points = 4;
  }
  optional string model_key = 1;
  repeated .chesscom.explanation_engine.v1.SimpleCharmMovePrediction moves = 3;
  repeated float rank_probabilities = 5
```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04382"></a>
## FND-04382: message declaration: chesscom.explanation_engine.v1.SimpleCharmInference

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SimpleCharmInference {

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 236.

```text
ge SimpleCharmMovePrediction {
  optional string uci_move = 1;
  optional float probability = 2;
}

message SimpleCharmInference {
  oneof _rating {
  int32 rating = 2;
  }
  oneof _expected_points {
  float expected_points = 4;
  }
  optional string model_key = 1;
  repeated .chesscom.explanation_engine.v1.SimpleCharmMovePrediction moves = 3;
  repeated float rank_probabilities = 5;
  repeated float strength_probabi
```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380, FND-04381

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04383"></a>
## FND-04383: oneof declaration: chesscom.explanation_engine.v1.SimpleCharmInference._rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating {

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 269.

```text
optional string uci_move = 1;
  optional float probability = 2;
}

message SimpleCharmInference {
  oneof _rating {
  int32 rating = 2;
  }
  oneof _expected_points {
  float expected_points = 4;
  }
  optional string model_key = 1;
  repeated .chesscom.explanation_engine.v1.SimpleCharmMovePrediction moves = 3;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time
```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380, FND-04381

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04384"></a>
## FND-04384: chesscom.explanation_engine.v1.SimpleCharmInference.rating = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating = 2;

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 287.

```text
i_move = 1;
  optional float probability = 2;
}

message SimpleCharmInference {
  oneof _rating {
  int32 rating = 2;
  }
  oneof _expected_points {
  float expected_points = 4;
  }
  optional string model_key = 1;
  repeated .chesscom.explanation_engine.v1.SimpleCharmMovePrediction moves = 3;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabiliti
```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380, FND-04381

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04385"></a>
## FND-04385: oneof declaration: chesscom.explanation_engine.v1.SimpleCharmInference._expected_points

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _expected_points {

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 311.

```text
loat probability = 2;
}

message SimpleCharmInference {
  oneof _rating {
  int32 rating = 2;
  }
  oneof _expected_points {
  float expected_points = 4;
  }
  optional string model_key = 1;
  repeated .chesscom.explanation_engine.v1.SimpleCharmMovePrediction moves = 3;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float
```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380, FND-04381

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04386"></a>
## FND-04386: chesscom.explanation_engine.v1.SimpleCharmInference.expected_points = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float expected_points = 4;

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 338.

```text
ssage SimpleCharmInference {
  oneof _rating {
  int32 rating = 2;
  }
  oneof _expected_points {
  float expected_points = 4;
  }
  optional string model_key = 1;
  repeated .chesscom.explanation_engine.v1.SimpleCharmMovePrediction moves = 3;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  r
```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380, FND-04381

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04387"></a>
## FND-04387: chesscom.explanation_engine.v1.SimpleCharmInference.model_key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string model_key = 1;

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 371.

```text
eof _rating {
  int32 rating = 2;
  }
  oneof _expected_points {
  float expected_points = 4;
  }
  optional string model_key = 1;
  repeated .chesscom.explanation_engine.v1.SimpleCharmMovePrediction moves = 3;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float strength_rating_sen
```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380, FND-04381

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04388"></a>
## FND-04388: chesscom.explanation_engine.v1.SimpleCharmInference.moves = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.SimpleCharmMovePrediction moves = 3;

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 404.

```text

  }
  oneof _expected_points {
  float expected_points = 4;
  }
  optional string model_key = 1;
  repeated .chesscom.explanation_engine.v1.SimpleCharmMovePrediction moves = 3;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive_probabilities = 9;
}

mess
```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380, FND-04381

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04389"></a>
## FND-04389: chesscom.explanation_engine.v1.SimpleCharmInference.rank_probabilities = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated float rank_probabilities = 5;

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 484.

```text
ng model_key = 1;
  repeated .chesscom.explanation_engine.v1.SimpleCharmMovePrediction moves = 3;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive_probabilities = 9;
}

message SimpleCharmInferences {
  repeated .chesscom.explanation_engine.v1.SimpleCha
```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380, FND-04381

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04390"></a>
## FND-04390: chesscom.explanation_engine.v1.SimpleCharmInference.strength_probabilities = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated float strength_probabilities = 6;

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 525.

```text
planation_engine.v1.SimpleCharmMovePrediction moves = 3;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive_probabilities = 9;
}

message SimpleCharmInferences {
  repeated .chesscom.explanation_engine.v1.SimpleCharmInference inferences = 1;
}

```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380, FND-04381

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04391"></a>
## FND-04391: chesscom.explanation_engine.v1.SimpleCharmInference.time_taken_probabilities = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated float time_taken_probabilities = 7;

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 570.

```text
 moves = 3;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive_probabilities = 9;
}

message SimpleCharmInferences {
  repeated .chesscom.explanation_engine.v1.SimpleCharmInference inferences = 1;
}

```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380, FND-04381

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04392"></a>
## FND-04392: chesscom.explanation_engine.v1.SimpleCharmInference.ldw_probabilities = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated float ldw_probabilities = 8;

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 617.

```text
 = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive_probabilities = 9;
}

message SimpleCharmInferences {
  repeated .chesscom.explanation_engine.v1.SimpleCharmInference inferences = 1;
}

```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380, FND-04381

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04393"></a>
## FND-04393: chesscom.explanation_engine.v1.SimpleCharmInference.strength_rating_sensitive_probabilities = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated float strength_rating_sensitive_probabilities = 9;

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 657.

```text
ities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive_probabilities = 9;
}

message SimpleCharmInferences {
  repeated .chesscom.explanation_engine.v1.SimpleCharmInference inferences = 1;
}

```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380, FND-04381

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04394"></a>
## FND-04394: message declaration: chesscom.explanation_engine.v1.SimpleCharmInferences

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SimpleCharmInferences {

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 720.

```text
eated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive_probabilities = 9;
}

message SimpleCharmInferences {
  repeated .chesscom.explanation_engine.v1.SimpleCharmInference inferences = 1;
}

```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380, FND-04381

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04395"></a>
## FND-04395: chesscom.explanation_engine.v1.SimpleCharmInferences.inferences = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.SimpleCharmInference inferences = 1;

### Evidence

- **SRC-0424** `research/proto/chesscom/explanation_engine/v1/simple_charm_inference.proto` — [preserved redacted evidence](../evidence/text/9cb1fdab6d43c74de096b64d0455265a9cfeb28f7e70e52c8da8bac9b554608f.proto)
  Character offset 754.

```text

  repeated float strength_rating_sensitive_probabilities = 9;
}

message SimpleCharmInferences {
  repeated .chesscom.explanation_engine.v1.SimpleCharmInference inferences = 1;
}

```

**Source references:** SRC-0424, SRC-1395  
**URL references:** None independently associated  
**Related findings:** FND-04379, FND-04380, FND-04381

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04396"></a>
## FND-04396: enum declaration: chesscom.explanation_engine.v1.ThreatType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ThreatType {

### Evidence

- **SRC-0425** `research/proto/chesscom/explanation_engine/v1/simple_threat.proto` — [preserved redacted evidence](../evidence/text/bd12ff0384c5819e669d751c54ab679ac11a7ae15b94651cc7f3f4ffe577da91.proto)
  Character offset 122.

```text
planation_engine/v1/simple_threat.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum ThreatType {
  THREAT_TYPE_UNSPECIFIED = 0;
  THREAT_TYPE_CHECK = 1;
  THREAT_TYPE_CAPTURE = 2;
  THREAT_TYPE_MATE = 3;
}

message SimpleThreat {
  optional .chesscom.explanation_engine.v1.ThreatType threat_type = 1;
  optional .chesscom.chess.v1.Move threatened_move = 2;
  optional .chesscom.chess.v1.Score see_va
```

**Source references:** SRC-0425, SRC-1396  
**URL references:** None independently associated  
**Related findings:** FND-04397, FND-04398

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04397"></a>
## FND-04397: chesscom.explanation_engine.v1.ThreatType.THREAT_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

THREAT_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0425** `research/proto/chesscom/explanation_engine/v1/simple_threat.proto` — [preserved redacted evidence](../evidence/text/bd12ff0384c5819e669d751c54ab679ac11a7ae15b94651cc7f3f4ffe577da91.proto)
  Character offset 142.

```text
simple_threat.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum ThreatType {
  THREAT_TYPE_UNSPECIFIED = 0;
  THREAT_TYPE_CHECK = 1;
  THREAT_TYPE_CAPTURE = 2;
  THREAT_TYPE_MATE = 3;
}

message SimpleThreat {
  optional .chesscom.explanation_engine.v1.ThreatType threat_type = 1;
  optional .chesscom.chess.v1.Move threatened_move = 2;
  optional .chesscom.chess.v1.Score see_value = 3;
  optional 
```

**Source references:** SRC-0425, SRC-1396  
**URL references:** None independently associated  
**Related findings:** FND-04396, FND-04398

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04398"></a>
## FND-04398: chesscom.explanation_engine.v1.ThreatType.THREAT_TYPE_CHECK = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

THREAT_TYPE_CHECK = 1;

### Evidence

- **SRC-0425** `research/proto/chesscom/explanation_engine/v1/simple_threat.proto` — [preserved redacted evidence](../evidence/text/bd12ff0384c5819e669d751c54ab679ac11a7ae15b94651cc7f3f4ffe577da91.proto)
  Character offset 173.

```text
proto3

package chesscom.explanation_engine.v1;

enum ThreatType {
  THREAT_TYPE_UNSPECIFIED = 0;
  THREAT_TYPE_CHECK = 1;
  THREAT_TYPE_CAPTURE = 2;
  THREAT_TYPE_MATE = 3;
}

message SimpleThreat {
  optional .chesscom.explanation_engine.v1.ThreatType threat_type = 1;
  optional .chesscom.chess.v1.Move threatened_move = 2;
  optional .chesscom.chess.v1.Score see_value = 3;
  optional .chesscom.engine.v1.Score score
```

**Source references:** SRC-0425, SRC-1396  
**URL references:** None independently associated  
**Related findings:** FND-04396, FND-04397

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04399"></a>
## FND-04399: chesscom.explanation_engine.v1.ThreatType.THREAT_TYPE_CAPTURE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

THREAT_TYPE_CAPTURE = 2;

### Evidence

- **SRC-0425** `research/proto/chesscom/explanation_engine/v1/simple_threat.proto` — [preserved redacted evidence](../evidence/text/bd12ff0384c5819e669d751c54ab679ac11a7ae15b94651cc7f3f4ffe577da91.proto)
  Character offset 198.

```text
explanation_engine.v1;

enum ThreatType {
  THREAT_TYPE_UNSPECIFIED = 0;
  THREAT_TYPE_CHECK = 1;
  THREAT_TYPE_CAPTURE = 2;
  THREAT_TYPE_MATE = 3;
}

message SimpleThreat {
  optional .chesscom.explanation_engine.v1.ThreatType threat_type = 1;
  optional .chesscom.chess.v1.Move threatened_move = 2;
  optional .chesscom.chess.v1.Score see_value = 3;
  optional .chesscom.engine.v1.Score score = 4;
}

```

**Source references:** SRC-0425, SRC-1396  
**URL references:** None independently associated  
**Related findings:** FND-04396, FND-04397, FND-04398

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04400"></a>
## FND-04400: chesscom.explanation_engine.v1.ThreatType.THREAT_TYPE_MATE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

THREAT_TYPE_MATE = 3;

### Evidence

- **SRC-0425** `research/proto/chesscom/explanation_engine/v1/simple_threat.proto` — [preserved redacted evidence](../evidence/text/bd12ff0384c5819e669d751c54ab679ac11a7ae15b94651cc7f3f4ffe577da91.proto)
  Character offset 225.

```text
m ThreatType {
  THREAT_TYPE_UNSPECIFIED = 0;
  THREAT_TYPE_CHECK = 1;
  THREAT_TYPE_CAPTURE = 2;
  THREAT_TYPE_MATE = 3;
}

message SimpleThreat {
  optional .chesscom.explanation_engine.v1.ThreatType threat_type = 1;
  optional .chesscom.chess.v1.Move threatened_move = 2;
  optional .chesscom.chess.v1.Score see_value = 3;
  optional .chesscom.engine.v1.Score score = 4;
}

```

**Source references:** SRC-0425, SRC-1396  
**URL references:** None independently associated  
**Related findings:** FND-04396, FND-04397, FND-04398

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04401"></a>
## FND-04401: message declaration: chesscom.explanation_engine.v1.SimpleThreat

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SimpleThreat {

### Evidence

- **SRC-0425** `research/proto/chesscom/explanation_engine/v1/simple_threat.proto` — [preserved redacted evidence](../evidence/text/bd12ff0384c5819e669d751c54ab679ac11a7ae15b94651cc7f3f4ffe577da91.proto)
  Character offset 250.

```text
YPE_UNSPECIFIED = 0;
  THREAT_TYPE_CHECK = 1;
  THREAT_TYPE_CAPTURE = 2;
  THREAT_TYPE_MATE = 3;
}

message SimpleThreat {
  optional .chesscom.explanation_engine.v1.ThreatType threat_type = 1;
  optional .chesscom.chess.v1.Move threatened_move = 2;
  optional .chesscom.chess.v1.Score see_value = 3;
  optional .chesscom.engine.v1.Score score = 4;
}

```

**Source references:** SRC-0425, SRC-1396  
**URL references:** None independently associated  
**Related findings:** FND-04396, FND-04397, FND-04398

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04402"></a>
## FND-04402: chesscom.explanation_engine.v1.SimpleThreat.threat_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.ThreatType threat_type = 1;

### Evidence

- **SRC-0425** `research/proto/chesscom/explanation_engine/v1/simple_threat.proto` — [preserved redacted evidence](../evidence/text/bd12ff0384c5819e669d751c54ab679ac11a7ae15b94651cc7f3f4ffe577da91.proto)
  Character offset 275.

```text
REAT_TYPE_CHECK = 1;
  THREAT_TYPE_CAPTURE = 2;
  THREAT_TYPE_MATE = 3;
}

message SimpleThreat {
  optional .chesscom.explanation_engine.v1.ThreatType threat_type = 1;
  optional .chesscom.chess.v1.Move threatened_move = 2;
  optional .chesscom.chess.v1.Score see_value = 3;
  optional .chesscom.engine.v1.Score score = 4;
}

```

**Source references:** SRC-0425, SRC-1396  
**URL references:** None independently associated  
**Related findings:** FND-04396, FND-04397, FND-04398

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04403"></a>
## FND-04403: chesscom.explanation_engine.v1.SimpleThreat.threatened_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move threatened_move = 2;

### Evidence

- **SRC-0425** `research/proto/chesscom/explanation_engine/v1/simple_threat.proto` — [preserved redacted evidence](../evidence/text/bd12ff0384c5819e669d751c54ab679ac11a7ae15b94651cc7f3f4ffe577da91.proto)
  Character offset 346.

```text

}

message SimpleThreat {
  optional .chesscom.explanation_engine.v1.ThreatType threat_type = 1;
  optional .chesscom.chess.v1.Move threatened_move = 2;
  optional .chesscom.chess.v1.Score see_value = 3;
  optional .chesscom.engine.v1.Score score = 4;
}

```

**Source references:** SRC-0425, SRC-1396  
**URL references:** None independently associated  
**Related findings:** FND-04396, FND-04397, FND-04398

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04404"></a>
## FND-04404: chesscom.explanation_engine.v1.SimpleThreat.see_value = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Score see_value = 3;

### Evidence

- **SRC-0425** `research/proto/chesscom/explanation_engine/v1/simple_threat.proto` — [preserved redacted evidence](../evidence/text/bd12ff0384c5819e669d751c54ab679ac11a7ae15b94651cc7f3f4ffe577da91.proto)
  Character offset 402.

```text
ion_engine.v1.ThreatType threat_type = 1;
  optional .chesscom.chess.v1.Move threatened_move = 2;
  optional .chesscom.chess.v1.Score see_value = 3;
  optional .chesscom.engine.v1.Score score = 4;
}

```

**Source references:** SRC-0425, SRC-1396  
**URL references:** None independently associated  
**Related findings:** FND-04396, FND-04397, FND-04398

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04405"></a>
## FND-04405: chesscom.explanation_engine.v1.SimpleThreat.score = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.engine.v1.Score score = 4;

### Evidence

- **SRC-0425** `research/proto/chesscom/explanation_engine/v1/simple_threat.proto` — [preserved redacted evidence](../evidence/text/bd12ff0384c5819e669d751c54ab679ac11a7ae15b94651cc7f3f4ffe577da91.proto)
  Character offset 453.

```text
l .chesscom.chess.v1.Move threatened_move = 2;
  optional .chesscom.chess.v1.Score see_value = 3;
  optional .chesscom.engine.v1.Score score = 4;
}

```

**Source references:** SRC-0425, SRC-1396  
**URL references:** None independently associated  
**Related findings:** FND-04396, FND-04397, FND-04398

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04406"></a>
## FND-04406: enum declaration: chesscom.explanation_engine.v1.Skill

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Skill {

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 115.

```text
scom/explanation_engine/v1/skills.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum Skill {
  SKILL_UNSPECIFIED = 0;
  SKILL_CAPTURE = 1;
  SKILL_CHECK = 2;
  SKILL_CASTLE = 3;
  SKILL_CHECKMATE = 4;
  SKILL_FREE_PIECE = 5;
  SKILL_DEFEND_PIECE = 6;
  SKILL_RETREAT = 7;
  SKILL_DEVELOPS_PIECE = 8;
  SKILL_PAWNS_IN_CENTER = 9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COM
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04407"></a>
## FND-04407: chesscom.explanation_engine.v1.Skill.SKILL_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_UNSPECIFIED = 0;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 130.

```text
n_engine/v1/skills.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum Skill {
  SKILL_UNSPECIFIED = 0;
  SKILL_CAPTURE = 1;
  SKILL_CHECK = 2;
  SKILL_CASTLE = 3;
  SKILL_CHECKMATE = 4;
  SKILL_FREE_PIECE = 5;
  SKILL_DEFEND_PIECE = 6;
  SKILL_RETREAT = 7;
  SKILL_DEVELOPS_PIECE = 8;
  SKILL_PAWNS_IN_CENTER = 9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPME
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04408"></a>
## FND-04408: chesscom.explanation_engine.v1.Skill.SKILL_CAPTURE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_CAPTURE = 1;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 155.

```text
// syntax: proto3

package chesscom.explanation_engine.v1;

enum Skill {
  SKILL_UNSPECIFIED = 0;
  SKILL_CAPTURE = 1;
  SKILL_CHECK = 2;
  SKILL_CASTLE = 3;
  SKILL_CHECKMATE = 4;
  SKILL_FREE_PIECE = 5;
  SKILL_DEFEND_PIECE = 6;
  SKILL_RETREAT = 7;
  SKILL_DEVELOPS_PIECE = 8;
  SKILL_PAWNS_IN_CENTER = 9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04409"></a>
## FND-04409: chesscom.explanation_engine.v1.Skill.SKILL_CHECK = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_CHECK = 2;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 176.

```text
ckage chesscom.explanation_engine.v1;

enum Skill {
  SKILL_UNSPECIFIED = 0;
  SKILL_CAPTURE = 1;
  SKILL_CHECK = 2;
  SKILL_CASTLE = 3;
  SKILL_CHECKMATE = 4;
  SKILL_FREE_PIECE = 5;
  SKILL_DEFEND_PIECE = 6;
  SKILL_RETREAT = 7;
  SKILL_DEVELOPS_PIECE = 8;
  SKILL_PAWNS_IN_CENTER = 9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_T
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04410"></a>
## FND-04410: chesscom.explanation_engine.v1.Skill.SKILL_CASTLE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_CASTLE = 3;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 195.

```text
anation_engine.v1;

enum Skill {
  SKILL_UNSPECIFIED = 0;
  SKILL_CAPTURE = 1;
  SKILL_CHECK = 2;
  SKILL_CASTLE = 3;
  SKILL_CHECKMATE = 4;
  SKILL_FREE_PIECE = 5;
  SKILL_DEFEND_PIECE = 6;
  SKILL_RETREAT = 7;
  SKILL_DEVELOPS_PIECE = 8;
  SKILL_PAWNS_IN_CENTER = 9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_TWO_BOOK_MOVES = 14;
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04411"></a>
## FND-04411: chesscom.explanation_engine.v1.Skill.SKILL_CHECKMATE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_CHECKMATE = 4;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 215.

```text
enum Skill {
  SKILL_UNSPECIFIED = 0;
  SKILL_CAPTURE = 1;
  SKILL_CHECK = 2;
  SKILL_CASTLE = 3;
  SKILL_CHECKMATE = 4;
  SKILL_FREE_PIECE = 5;
  SKILL_DEFEND_PIECE = 6;
  SKILL_RETREAT = 7;
  SKILL_DEVELOPS_PIECE = 8;
  SKILL_PAWNS_IN_CENTER = 9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_TWO_BOOK_MOVES = 14;
  SKILL_THREE_BOOK_
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04412"></a>
## FND-04412: chesscom.explanation_engine.v1.Skill.SKILL_FREE_PIECE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_FREE_PIECE = 5;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 238.

```text
SPECIFIED = 0;
  SKILL_CAPTURE = 1;
  SKILL_CHECK = 2;
  SKILL_CASTLE = 3;
  SKILL_CHECKMATE = 4;
  SKILL_FREE_PIECE = 5;
  SKILL_DEFEND_PIECE = 6;
  SKILL_RETREAT = 7;
  SKILL_DEVELOPS_PIECE = 8;
  SKILL_PAWNS_IN_CENTER = 9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_TWO_BOOK_MOVES = 14;
  SKILL_THREE_BOOK_MOVES = 15;
  SKILL_FOU
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04413"></a>
## FND-04413: chesscom.explanation_engine.v1.Skill.SKILL_DEFEND_PIECE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_DEFEND_PIECE = 6;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 262.

```text
APTURE = 1;
  SKILL_CHECK = 2;
  SKILL_CASTLE = 3;
  SKILL_CHECKMATE = 4;
  SKILL_FREE_PIECE = 5;
  SKILL_DEFEND_PIECE = 6;
  SKILL_RETREAT = 7;
  SKILL_DEVELOPS_PIECE = 8;
  SKILL_PAWNS_IN_CENTER = 9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_TWO_BOOK_MOVES = 14;
  SKILL_THREE_BOOK_MOVES = 15;
  SKILL_FOUR_BOOK_MOVES = 16;
  SKI
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04414"></a>
## FND-04414: chesscom.explanation_engine.v1.Skill.SKILL_RETREAT = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_RETREAT = 7;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 288.

```text
= 2;
  SKILL_CASTLE = 3;
  SKILL_CHECKMATE = 4;
  SKILL_FREE_PIECE = 5;
  SKILL_DEFEND_PIECE = 6;
  SKILL_RETREAT = 7;
  SKILL_DEVELOPS_PIECE = 8;
  SKILL_PAWNS_IN_CENTER = 9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_TWO_BOOK_MOVES = 14;
  SKILL_THREE_BOOK_MOVES = 15;
  SKILL_FOUR_BOOK_MOVES = 16;
  SKILL_FIANCHETTO = 17;
  SKIL
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04415"></a>
## FND-04415: chesscom.explanation_engine.v1.Skill.SKILL_DEVELOPS_PIECE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_DEVELOPS_PIECE = 8;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 309.

```text
 3;
  SKILL_CHECKMATE = 4;
  SKILL_FREE_PIECE = 5;
  SKILL_DEFEND_PIECE = 6;
  SKILL_RETREAT = 7;
  SKILL_DEVELOPS_PIECE = 8;
  SKILL_PAWNS_IN_CENTER = 9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_TWO_BOOK_MOVES = 14;
  SKILL_THREE_BOOK_MOVES = 15;
  SKILL_FOUR_BOOK_MOVES = 16;
  SKILL_FIANCHETTO = 17;
  SKILL_RECAPTURE = 18;
  S
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04416"></a>
## FND-04416: chesscom.explanation_engine.v1.Skill.SKILL_PAWNS_IN_CENTER = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_PAWNS_IN_CENTER = 9;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 337.

```text
 SKILL_FREE_PIECE = 5;
  SKILL_DEFEND_PIECE = 6;
  SKILL_RETREAT = 7;
  SKILL_DEVELOPS_PIECE = 8;
  SKILL_PAWNS_IN_CENTER = 9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_TWO_BOOK_MOVES = 14;
  SKILL_THREE_BOOK_MOVES = 15;
  SKILL_FOUR_BOOK_MOVES = 16;
  SKILL_FIANCHETTO = 17;
  SKILL_RECAPTURE = 18;
  SKILL_WINNING_CAPTURE = 19;
 
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04417"></a>
## FND-04417: chesscom.explanation_engine.v1.Skill.SKILL_STRIKES_AT_CENTER = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_STRIKES_AT_CENTER = 10;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 366.

```text
L_DEFEND_PIECE = 6;
  SKILL_RETREAT = 7;
  SKILL_DEVELOPS_PIECE = 8;
  SKILL_PAWNS_IN_CENTER = 9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_TWO_BOOK_MOVES = 14;
  SKILL_THREE_BOOK_MOVES = 15;
  SKILL_FOUR_BOOK_MOVES = 16;
  SKILL_FIANCHETTO = 17;
  SKILL_RECAPTURE = 18;
  SKILL_WINNING_CAPTURE = 19;
  SKILL_BLOCKS_ATTACK = 20;
  
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04418"></a>
## FND-04418: chesscom.explanation_engine.v1.Skill.SKILL_CONNECT_ROOKS = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_CONNECT_ROOKS = 11;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 398.

```text
EAT = 7;
  SKILL_DEVELOPS_PIECE = 8;
  SKILL_PAWNS_IN_CENTER = 9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_TWO_BOOK_MOVES = 14;
  SKILL_THREE_BOOK_MOVES = 15;
  SKILL_FOUR_BOOK_MOVES = 16;
  SKILL_FIANCHETTO = 17;
  SKILL_RECAPTURE = 18;
  SKILL_WINNING_CAPTURE = 19;
  SKILL_BLOCKS_ATTACK = 20;
  SKILL_FORK = 21;
  SKILL_PIN = 2
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04419"></a>
## FND-04419: chesscom.explanation_engine.v1.Skill.SKILL_COMPLETE_DEVELOPMENT = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_COMPLETE_DEVELOPMENT = 12;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 426.

```text
ECE = 8;
  SKILL_PAWNS_IN_CENTER = 9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_TWO_BOOK_MOVES = 14;
  SKILL_THREE_BOOK_MOVES = 15;
  SKILL_FOUR_BOOK_MOVES = 16;
  SKILL_FIANCHETTO = 17;
  SKILL_RECAPTURE = 18;
  SKILL_WINNING_CAPTURE = 19;
  SKILL_BLOCKS_ATTACK = 20;
  SKILL_FORK = 21;
  SKILL_PIN = 22;
  SKILL_DEFEND_CHECKMATE 
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04420"></a>
## FND-04420: chesscom.explanation_engine.v1.Skill.SKILL_ONE_BOOK_MOVE = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_ONE_BOOK_MOVE = 13;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 461.

```text
9;
  SKILL_STRIKES_AT_CENTER = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_TWO_BOOK_MOVES = 14;
  SKILL_THREE_BOOK_MOVES = 15;
  SKILL_FOUR_BOOK_MOVES = 16;
  SKILL_FIANCHETTO = 17;
  SKILL_RECAPTURE = 18;
  SKILL_WINNING_CAPTURE = 19;
  SKILL_BLOCKS_ATTACK = 20;
  SKILL_FORK = 21;
  SKILL_PIN = 22;
  SKILL_DEFEND_CHECKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04421"></a>
## FND-04421: chesscom.explanation_engine.v1.Skill.SKILL_TWO_BOOK_MOVES = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_TWO_BOOK_MOVES = 14;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 489.

```text
 = 10;
  SKILL_CONNECT_ROOKS = 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_TWO_BOOK_MOVES = 14;
  SKILL_THREE_BOOK_MOVES = 15;
  SKILL_FOUR_BOOK_MOVES = 16;
  SKILL_FIANCHETTO = 17;
  SKILL_RECAPTURE = 18;
  SKILL_WINNING_CAPTURE = 19;
  SKILL_BLOCKS_ATTACK = 20;
  SKILL_FORK = 21;
  SKILL_PIN = 22;
  SKILL_DEFEND_CHECKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04422"></a>
## FND-04422: chesscom.explanation_engine.v1.Skill.SKILL_THREE_BOOK_MOVES = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_THREE_BOOK_MOVES = 15;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 518.

```text
= 11;
  SKILL_COMPLETE_DEVELOPMENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_TWO_BOOK_MOVES = 14;
  SKILL_THREE_BOOK_MOVES = 15;
  SKILL_FOUR_BOOK_MOVES = 16;
  SKILL_FIANCHETTO = 17;
  SKILL_RECAPTURE = 18;
  SKILL_WINNING_CAPTURE = 19;
  SKILL_BLOCKS_ATTACK = 20;
  SKILL_FORK = 21;
  SKILL_PIN = 22;
  SKILL_DEFEND_CHECKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
 
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04423"></a>
## FND-04423: chesscom.explanation_engine.v1.Skill.SKILL_FOUR_BOOK_MOVES = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_FOUR_BOOK_MOVES = 16;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 549.

```text
ENT = 12;
  SKILL_ONE_BOOK_MOVE = 13;
  SKILL_TWO_BOOK_MOVES = 14;
  SKILL_THREE_BOOK_MOVES = 15;
  SKILL_FOUR_BOOK_MOVES = 16;
  SKILL_FIANCHETTO = 17;
  SKILL_RECAPTURE = 18;
  SKILL_WINNING_CAPTURE = 19;
  SKILL_BLOCKS_ATTACK = 20;
  SKILL_FORK = 21;
  SKILL_PIN = 22;
  SKILL_DEFEND_CHECKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATT
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04424"></a>
## FND-04424: chesscom.explanation_engine.v1.Skill.SKILL_FIANCHETTO = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_FIANCHETTO = 17;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 579.

```text
E = 13;
  SKILL_TWO_BOOK_MOVES = 14;
  SKILL_THREE_BOOK_MOVES = 15;
  SKILL_FOUR_BOOK_MOVES = 16;
  SKILL_FIANCHETTO = 17;
  SKILL_RECAPTURE = 18;
  SKILL_WINNING_CAPTURE = 19;
  SKILL_BLOCKS_ATTACK = 20;
  SKILL_FORK = 21;
  SKILL_PIN = 22;
  SKILL_DEFEND_CHECKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SK
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04425"></a>
## FND-04425: chesscom.explanation_engine.v1.Skill.SKILL_RECAPTURE = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_RECAPTURE = 18;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 604.

```text
MOVES = 14;
  SKILL_THREE_BOOK_MOVES = 15;
  SKILL_FOUR_BOOK_MOVES = 16;
  SKILL_FIANCHETTO = 17;
  SKILL_RECAPTURE = 18;
  SKILL_WINNING_CAPTURE = 19;
  SKILL_BLOCKS_ATTACK = 20;
  SKILL_FORK = 21;
  SKILL_PIN = 22;
  SKILL_DEFEND_CHECKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
 
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04426"></a>
## FND-04426: chesscom.explanation_engine.v1.Skill.SKILL_WINNING_CAPTURE = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_WINNING_CAPTURE = 19;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 628.

```text
E_BOOK_MOVES = 15;
  SKILL_FOUR_BOOK_MOVES = 16;
  SKILL_FIANCHETTO = 17;
  SKILL_RECAPTURE = 18;
  SKILL_WINNING_CAPTURE = 19;
  SKILL_BLOCKS_ATTACK = 20;
  SKILL_FORK = 21;
  SKILL_PIN = 22;
  SKILL_DEFEND_CHECKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
  SKILL_REMOVES_DEFENDER 
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04427"></a>
## FND-04427: chesscom.explanation_engine.v1.Skill.SKILL_BLOCKS_ATTACK = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_BLOCKS_ATTACK = 20;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 658.

```text
R_BOOK_MOVES = 16;
  SKILL_FIANCHETTO = 17;
  SKILL_RECAPTURE = 18;
  SKILL_WINNING_CAPTURE = 19;
  SKILL_BLOCKS_ATTACK = 20;
  SKILL_FORK = 21;
  SKILL_PIN = 22;
  SKILL_DEFEND_CHECKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
  SKILL_REMOVES_DEFENDER = 30;
  SKILL_ROYAL_FORK = 31;
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04428"></a>
## FND-04428: chesscom.explanation_engine.v1.Skill.SKILL_FORK = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_FORK = 21;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 686.

```text
IANCHETTO = 17;
  SKILL_RECAPTURE = 18;
  SKILL_WINNING_CAPTURE = 19;
  SKILL_BLOCKS_ATTACK = 20;
  SKILL_FORK = 21;
  SKILL_PIN = 22;
  SKILL_DEFEND_CHECKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
  SKILL_REMOVES_DEFENDER = 30;
  SKILL_ROYAL_FORK = 31;
  SKILL_DISCOVERED_CHECK = 
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04429"></a>
## FND-04429: chesscom.explanation_engine.v1.Skill.SKILL_PIN = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_PIN = 22;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 705.

```text
KILL_RECAPTURE = 18;
  SKILL_WINNING_CAPTURE = 19;
  SKILL_BLOCKS_ATTACK = 20;
  SKILL_FORK = 21;
  SKILL_PIN = 22;
  SKILL_DEFEND_CHECKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
  SKILL_REMOVES_DEFENDER = 30;
  SKILL_ROYAL_FORK = 31;
  SKILL_DISCOVERED_CHECK = 32;
  SKILL_COUNTER
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04430"></a>
## FND-04430: chesscom.explanation_engine.v1.Skill.SKILL_DEFEND_CHECKMATE = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_DEFEND_CHECKMATE = 23;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 723.

```text
8;
  SKILL_WINNING_CAPTURE = 19;
  SKILL_BLOCKS_ATTACK = 20;
  SKILL_FORK = 21;
  SKILL_PIN = 22;
  SKILL_DEFEND_CHECKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
  SKILL_REMOVES_DEFENDER = 30;
  SKILL_ROYAL_FORK = 31;
  SKILL_DISCOVERED_CHECK = 32;
  SKILL_COUNTER_THREAT = 33;
  SK
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04431"></a>
## FND-04431: chesscom.explanation_engine.v1.Skill.SKILL_ABSOLUTE_PIN = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_ABSOLUTE_PIN = 24;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 754.

```text
;
  SKILL_BLOCKS_ATTACK = 20;
  SKILL_FORK = 21;
  SKILL_PIN = 22;
  SKILL_DEFEND_CHECKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
  SKILL_REMOVES_DEFENDER = 30;
  SKILL_ROYAL_FORK = 31;
  SKILL_DISCOVERED_CHECK = 32;
  SKILL_COUNTER_THREAT = 33;
  SKILL_DEFEND_TACTIC = 34;
  SKILL
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04432"></a>
## FND-04432: chesscom.explanation_engine.v1.Skill.SKILL_DISCOVERED_ATTACK = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_DISCOVERED_ATTACK = 25;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 781.

```text
0;
  SKILL_FORK = 21;
  SKILL_PIN = 22;
  SKILL_DEFEND_CHECKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
  SKILL_REMOVES_DEFENDER = 30;
  SKILL_ROYAL_FORK = 31;
  SKILL_DISCOVERED_CHECK = 32;
  SKILL_COUNTER_THREAT = 33;
  SKILL_DEFEND_TACTIC = 34;
  SKILL_EXPLOITS_PIN = 35;
  SKILL
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04433"></a>
## FND-04433: chesscom.explanation_engine.v1.Skill.SKILL_KNIGHT_FORK = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_KNIGHT_FORK = 26;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 813.

```text
N = 22;
  SKILL_DEFEND_CHECKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
  SKILL_REMOVES_DEFENDER = 30;
  SKILL_ROYAL_FORK = 31;
  SKILL_DISCOVERED_CHECK = 32;
  SKILL_COUNTER_THREAT = 33;
  SKILL_DEFEND_TACTIC = 34;
  SKILL_EXPLOITS_PIN = 35;
  SKILL_DOUBLE_CHECK = 36;
  SKILL_BRIL
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04434"></a>
## FND-04434: chesscom.explanation_engine.v1.Skill.SKILL_SKEWER = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_SKEWER = 27;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 839.

```text
CKMATE = 23;
  SKILL_ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
  SKILL_REMOVES_DEFENDER = 30;
  SKILL_ROYAL_FORK = 31;
  SKILL_DISCOVERED_CHECK = 32;
  SKILL_COUNTER_THREAT = 33;
  SKILL_DEFEND_TACTIC = 34;
  SKILL_EXPLOITS_PIN = 35;
  SKILL_DOUBLE_CHECK = 36;
  SKILL_BRILLIANT_SACRIFICE = 37;
  SK
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04435"></a>
## FND-04435: chesscom.explanation_engine.v1.Skill.SKILL_ATTACKING_PINNED_PIECE = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_ATTACKING_PINNED_PIECE = 28;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 860.

```text
ABSOLUTE_PIN = 24;
  SKILL_DISCOVERED_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
  SKILL_REMOVES_DEFENDER = 30;
  SKILL_ROYAL_FORK = 31;
  SKILL_DISCOVERED_CHECK = 32;
  SKILL_COUNTER_THREAT = 33;
  SKILL_DEFEND_TACTIC = 34;
  SKILL_EXPLOITS_PIN = 35;
  SKILL_DOUBLE_CHECK = 36;
  SKILL_BRILLIANT_SACRIFICE = 37;
  SKILL_QUEEN_SACRIFICE =
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04436"></a>
## FND-04436: chesscom.explanation_engine.v1.Skill.SKILL_TRAPPED_PIECE = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_TRAPPED_PIECE = 29;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 897.

```text
_ATTACK = 25;
  SKILL_KNIGHT_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
  SKILL_REMOVES_DEFENDER = 30;
  SKILL_ROYAL_FORK = 31;
  SKILL_DISCOVERED_CHECK = 32;
  SKILL_COUNTER_THREAT = 33;
  SKILL_DEFEND_TACTIC = 34;
  SKILL_EXPLOITS_PIN = 35;
  SKILL_DOUBLE_CHECK = 36;
  SKILL_BRILLIANT_SACRIFICE = 37;
  SKILL_QUEEN_SACRIFICE = 38;
  SKILL_EQUAL_TRADE = 39;
  SKIL
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04437"></a>
## FND-04437: chesscom.explanation_engine.v1.Skill.SKILL_REMOVES_DEFENDER = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_REMOVES_DEFENDER = 30;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 925.

```text
_FORK = 26;
  SKILL_SKEWER = 27;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
  SKILL_REMOVES_DEFENDER = 30;
  SKILL_ROYAL_FORK = 31;
  SKILL_DISCOVERED_CHECK = 32;
  SKILL_COUNTER_THREAT = 33;
  SKILL_DEFEND_TACTIC = 34;
  SKILL_EXPLOITS_PIN = 35;
  SKILL_DOUBLE_CHECK = 36;
  SKILL_BRILLIANT_SACRIFICE = 37;
  SKILL_QUEEN_SACRIFICE = 38;
  SKILL_EQUAL_TRADE = 39;
  SKILL_POWERFUL_BISHOP = 40;
  SK
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04438"></a>
## FND-04438: chesscom.explanation_engine.v1.Skill.SKILL_ROYAL_FORK = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_ROYAL_FORK = 31;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 956.

```text
;
  SKILL_ATTACKING_PINNED_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
  SKILL_REMOVES_DEFENDER = 30;
  SKILL_ROYAL_FORK = 31;
  SKILL_DISCOVERED_CHECK = 32;
  SKILL_COUNTER_THREAT = 33;
  SKILL_DEFEND_TACTIC = 34;
  SKILL_EXPLOITS_PIN = 35;
  SKILL_DOUBLE_CHECK = 36;
  SKILL_BRILLIANT_SACRIFICE = 37;
  SKILL_QUEEN_SACRIFICE = 38;
  SKILL_EQUAL_TRADE = 39;
  SKILL_POWERFUL_BISHOP = 40;
  SKILL_ROOK_TO_OPEN_FILE = 41;
  S
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04439"></a>
## FND-04439: chesscom.explanation_engine.v1.Skill.SKILL_DISCOVERED_CHECK = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_DISCOVERED_CHECK = 32;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 981.

```text
D_PIECE = 28;
  SKILL_TRAPPED_PIECE = 29;
  SKILL_REMOVES_DEFENDER = 30;
  SKILL_ROYAL_FORK = 31;
  SKILL_DISCOVERED_CHECK = 32;
  SKILL_COUNTER_THREAT = 33;
  SKILL_DEFEND_TACTIC = 34;
  SKILL_EXPLOITS_PIN = 35;
  SKILL_DOUBLE_CHECK = 36;
  SKILL_BRILLIANT_SACRIFICE = 37;
  SKILL_QUEEN_SACRIFICE = 38;
  SKILL_EQUAL_TRADE = 39;
  SKILL_POWERFUL_BISHOP = 40;
  SKILL_ROOK_TO_OPEN_FILE = 41;
  SKILL_KICK = 42;
  SKILL_O
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04440"></a>
## FND-04440: chesscom.explanation_engine.v1.Skill.SKILL_COUNTER_THREAT = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_COUNTER_THREAT = 33;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1012.

```text
IECE = 29;
  SKILL_REMOVES_DEFENDER = 30;
  SKILL_ROYAL_FORK = 31;
  SKILL_DISCOVERED_CHECK = 32;
  SKILL_COUNTER_THREAT = 33;
  SKILL_DEFEND_TACTIC = 34;
  SKILL_EXPLOITS_PIN = 35;
  SKILL_DOUBLE_CHECK = 36;
  SKILL_BRILLIANT_SACRIFICE = 37;
  SKILL_QUEEN_SACRIFICE = 38;
  SKILL_EQUAL_TRADE = 39;
  SKILL_POWERFUL_BISHOP = 40;
  SKILL_ROOK_TO_OPEN_FILE = 41;
  SKILL_KICK = 42;
  SKILL_OUTPOST = 43;
  SKILL_TRADING_TO
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04441"></a>
## FND-04441: chesscom.explanation_engine.v1.Skill.SKILL_DEFEND_TACTIC = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_DEFEND_TACTIC = 34;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1041.

```text
FENDER = 30;
  SKILL_ROYAL_FORK = 31;
  SKILL_DISCOVERED_CHECK = 32;
  SKILL_COUNTER_THREAT = 33;
  SKILL_DEFEND_TACTIC = 34;
  SKILL_EXPLOITS_PIN = 35;
  SKILL_DOUBLE_CHECK = 36;
  SKILL_BRILLIANT_SACRIFICE = 37;
  SKILL_QUEEN_SACRIFICE = 38;
  SKILL_EQUAL_TRADE = 39;
  SKILL_POWERFUL_BISHOP = 40;
  SKILL_ROOK_TO_OPEN_FILE = 41;
  SKILL_KICK = 42;
  SKILL_OUTPOST = 43;
  SKILL_TRADING_TO_SIMPLIFY = 44;
  SKILL_DOUBL
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04442"></a>
## FND-04442: chesscom.explanation_engine.v1.Skill.SKILL_EXPLOITS_PIN = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_EXPLOITS_PIN = 35;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1069.

```text
ORK = 31;
  SKILL_DISCOVERED_CHECK = 32;
  SKILL_COUNTER_THREAT = 33;
  SKILL_DEFEND_TACTIC = 34;
  SKILL_EXPLOITS_PIN = 35;
  SKILL_DOUBLE_CHECK = 36;
  SKILL_BRILLIANT_SACRIFICE = 37;
  SKILL_QUEEN_SACRIFICE = 38;
  SKILL_EQUAL_TRADE = 39;
  SKILL_POWERFUL_BISHOP = 40;
  SKILL_ROOK_TO_OPEN_FILE = 41;
  SKILL_KICK = 42;
  SKILL_OUTPOST = 43;
  SKILL_TRADING_TO_SIMPLIFY = 44;
  SKILL_DOUBLE_ROOKS = 45;
  SKILL_CREATE
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04443"></a>
## FND-04443: chesscom.explanation_engine.v1.Skill.SKILL_DOUBLE_CHECK = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_DOUBLE_CHECK = 36;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1096.

```text
D_CHECK = 32;
  SKILL_COUNTER_THREAT = 33;
  SKILL_DEFEND_TACTIC = 34;
  SKILL_EXPLOITS_PIN = 35;
  SKILL_DOUBLE_CHECK = 36;
  SKILL_BRILLIANT_SACRIFICE = 37;
  SKILL_QUEEN_SACRIFICE = 38;
  SKILL_EQUAL_TRADE = 39;
  SKILL_POWERFUL_BISHOP = 40;
  SKILL_ROOK_TO_OPEN_FILE = 41;
  SKILL_KICK = 42;
  SKILL_OUTPOST = 43;
  SKILL_TRADING_TO_SIMPLIFY = 44;
  SKILL_DOUBLE_ROOKS = 45;
  SKILL_CREATES_BATTERY = 46;
  SKILL_PRE
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04444"></a>
## FND-04444: chesscom.explanation_engine.v1.Skill.SKILL_BRILLIANT_SACRIFICE = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_BRILLIANT_SACRIFICE = 37;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1123.

```text
ER_THREAT = 33;
  SKILL_DEFEND_TACTIC = 34;
  SKILL_EXPLOITS_PIN = 35;
  SKILL_DOUBLE_CHECK = 36;
  SKILL_BRILLIANT_SACRIFICE = 37;
  SKILL_QUEEN_SACRIFICE = 38;
  SKILL_EQUAL_TRADE = 39;
  SKILL_POWERFUL_BISHOP = 40;
  SKILL_ROOK_TO_OPEN_FILE = 41;
  SKILL_KICK = 42;
  SKILL_OUTPOST = 43;
  SKILL_TRADING_TO_SIMPLIFY = 44;
  SKILL_DOUBLE_ROOKS = 45;
  SKILL_CREATES_BATTERY = 46;
  SKILL_PREVENT_CASTLING = 47;
  SKILL
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04445"></a>
## FND-04445: chesscom.explanation_engine.v1.Skill.SKILL_QUEEN_SACRIFICE = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_QUEEN_SACRIFICE = 38;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1157.

```text
TIC = 34;
  SKILL_EXPLOITS_PIN = 35;
  SKILL_DOUBLE_CHECK = 36;
  SKILL_BRILLIANT_SACRIFICE = 37;
  SKILL_QUEEN_SACRIFICE = 38;
  SKILL_EQUAL_TRADE = 39;
  SKILL_POWERFUL_BISHOP = 40;
  SKILL_ROOK_TO_OPEN_FILE = 41;
  SKILL_KICK = 42;
  SKILL_OUTPOST = 43;
  SKILL_TRADING_TO_SIMPLIFY = 44;
  SKILL_DOUBLE_ROOKS = 45;
  SKILL_CREATES_BATTERY = 46;
  SKILL_PREVENT_CASTLING = 47;
  SKILL_WINS_TEMPO = 48;
  SKILL_AVOIDS_T
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04446"></a>
## FND-04446: chesscom.explanation_engine.v1.Skill.SKILL_EQUAL_TRADE = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_EQUAL_TRADE = 39;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1187.

```text
 = 35;
  SKILL_DOUBLE_CHECK = 36;
  SKILL_BRILLIANT_SACRIFICE = 37;
  SKILL_QUEEN_SACRIFICE = 38;
  SKILL_EQUAL_TRADE = 39;
  SKILL_POWERFUL_BISHOP = 40;
  SKILL_ROOK_TO_OPEN_FILE = 41;
  SKILL_KICK = 42;
  SKILL_OUTPOST = 43;
  SKILL_TRADING_TO_SIMPLIFY = 44;
  SKILL_DOUBLE_ROOKS = 45;
  SKILL_CREATES_BATTERY = 46;
  SKILL_PREVENT_CASTLING = 47;
  SKILL_WINS_TEMPO = 48;
  SKILL_AVOIDS_TRADE = 49;
  SKILL_DEVELOP_WIT
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04447"></a>
## FND-04447: chesscom.explanation_engine.v1.Skill.SKILL_POWERFUL_BISHOP = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_POWERFUL_BISHOP = 40;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1213.

```text
K = 36;
  SKILL_BRILLIANT_SACRIFICE = 37;
  SKILL_QUEEN_SACRIFICE = 38;
  SKILL_EQUAL_TRADE = 39;
  SKILL_POWERFUL_BISHOP = 40;
  SKILL_ROOK_TO_OPEN_FILE = 41;
  SKILL_KICK = 42;
  SKILL_OUTPOST = 43;
  SKILL_TRADING_TO_SIMPLIFY = 44;
  SKILL_DOUBLE_ROOKS = 45;
  SKILL_CREATES_BATTERY = 46;
  SKILL_PREVENT_CASTLING = 47;
  SKILL_WINS_TEMPO = 48;
  SKILL_AVOIDS_TRADE = 49;
  SKILL_DEVELOP_WITH_TEMPO = 50;
  SKILL_DAMA
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04448"></a>
## FND-04448: chesscom.explanation_engine.v1.Skill.SKILL_ROOK_TO_OPEN_FILE = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_ROOK_TO_OPEN_FILE = 41;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1243.

```text
IFICE = 37;
  SKILL_QUEEN_SACRIFICE = 38;
  SKILL_EQUAL_TRADE = 39;
  SKILL_POWERFUL_BISHOP = 40;
  SKILL_ROOK_TO_OPEN_FILE = 41;
  SKILL_KICK = 42;
  SKILL_OUTPOST = 43;
  SKILL_TRADING_TO_SIMPLIFY = 44;
  SKILL_DOUBLE_ROOKS = 45;
  SKILL_CREATES_BATTERY = 46;
  SKILL_PREVENT_CASTLING = 47;
  SKILL_WINS_TEMPO = 48;
  SKILL_AVOIDS_TRADE = 49;
  SKILL_DEVELOP_WITH_TEMPO = 50;
  SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04449"></a>
## FND-04449: chesscom.explanation_engine.v1.Skill.SKILL_KICK = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_KICK = 42;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1275.

```text
ICE = 38;
  SKILL_EQUAL_TRADE = 39;
  SKILL_POWERFUL_BISHOP = 40;
  SKILL_ROOK_TO_OPEN_FILE = 41;
  SKILL_KICK = 42;
  SKILL_OUTPOST = 43;
  SKILL_TRADING_TO_SIMPLIFY = 44;
  SKILL_DOUBLE_ROOKS = 45;
  SKILL_CREATES_BATTERY = 46;
  SKILL_PREVENT_CASTLING = 47;
  SKILL_WINS_TEMPO = 48;
  SKILL_AVOIDS_TRADE = 49;
  SKILL_DEVELOP_WITH_TEMPO = 50;
  SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 51;
  SKILL_EN_PASSANT = 52;
  S
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04450"></a>
## FND-04450: chesscom.explanation_engine.v1.Skill.SKILL_OUTPOST = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_OUTPOST = 43;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1294.

```text
QUAL_TRADE = 39;
  SKILL_POWERFUL_BISHOP = 40;
  SKILL_ROOK_TO_OPEN_FILE = 41;
  SKILL_KICK = 42;
  SKILL_OUTPOST = 43;
  SKILL_TRADING_TO_SIMPLIFY = 44;
  SKILL_DOUBLE_ROOKS = 45;
  SKILL_CREATES_BATTERY = 46;
  SKILL_PREVENT_CASTLING = 47;
  SKILL_WINS_TEMPO = 48;
  SKILL_AVOIDS_TRADE = 49;
  SKILL_DEVELOP_WITH_TEMPO = 50;
  SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 51;
  SKILL_EN_PASSANT = 52;
  SKILL_IMPROVES_PAWN_
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04451"></a>
## FND-04451: chesscom.explanation_engine.v1.Skill.SKILL_TRADING_TO_SIMPLIFY = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_TRADING_TO_SIMPLIFY = 44;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1316.

```text
LL_POWERFUL_BISHOP = 40;
  SKILL_ROOK_TO_OPEN_FILE = 41;
  SKILL_KICK = 42;
  SKILL_OUTPOST = 43;
  SKILL_TRADING_TO_SIMPLIFY = 44;
  SKILL_DOUBLE_ROOKS = 45;
  SKILL_CREATES_BATTERY = 46;
  SKILL_PREVENT_CASTLING = 47;
  SKILL_WINS_TEMPO = 48;
  SKILL_AVOIDS_TRADE = 49;
  SKILL_DEVELOP_WITH_TEMPO = 50;
  SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 51;
  SKILL_EN_PASSANT = 52;
  SKILL_IMPROVES_PAWN_STRUCTURE = 53;
  SKIL
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04452"></a>
## FND-04452: chesscom.explanation_engine.v1.Skill.SKILL_DOUBLE_ROOKS = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_DOUBLE_ROOKS = 45;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1350.

```text
OOK_TO_OPEN_FILE = 41;
  SKILL_KICK = 42;
  SKILL_OUTPOST = 43;
  SKILL_TRADING_TO_SIMPLIFY = 44;
  SKILL_DOUBLE_ROOKS = 45;
  SKILL_CREATES_BATTERY = 46;
  SKILL_PREVENT_CASTLING = 47;
  SKILL_WINS_TEMPO = 48;
  SKILL_AVOIDS_TRADE = 49;
  SKILL_DEVELOP_WITH_TEMPO = 50;
  SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 51;
  SKILL_EN_PASSANT = 52;
  SKILL_IMPROVES_PAWN_STRUCTURE = 53;
  SKILL_PAWN_STORM = 54;
  SKILL_PROMOTI
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04453"></a>
## FND-04453: chesscom.explanation_engine.v1.Skill.SKILL_CREATES_BATTERY = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_CREATES_BATTERY = 46;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1377.

```text
ILL_KICK = 42;
  SKILL_OUTPOST = 43;
  SKILL_TRADING_TO_SIMPLIFY = 44;
  SKILL_DOUBLE_ROOKS = 45;
  SKILL_CREATES_BATTERY = 46;
  SKILL_PREVENT_CASTLING = 47;
  SKILL_WINS_TEMPO = 48;
  SKILL_AVOIDS_TRADE = 49;
  SKILL_DEVELOP_WITH_TEMPO = 50;
  SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 51;
  SKILL_EN_PASSANT = 52;
  SKILL_IMPROVES_PAWN_STRUCTURE = 53;
  SKILL_PAWN_STORM = 54;
  SKILL_PROMOTION = 55;
  SKILL_LADDER_MAT
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04454"></a>
## FND-04454: chesscom.explanation_engine.v1.Skill.SKILL_PREVENT_CASTLING = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_PREVENT_CASTLING = 47;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1407.

```text
 = 43;
  SKILL_TRADING_TO_SIMPLIFY = 44;
  SKILL_DOUBLE_ROOKS = 45;
  SKILL_CREATES_BATTERY = 46;
  SKILL_PREVENT_CASTLING = 47;
  SKILL_WINS_TEMPO = 48;
  SKILL_AVOIDS_TRADE = 49;
  SKILL_DEVELOP_WITH_TEMPO = 50;
  SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 51;
  SKILL_EN_PASSANT = 52;
  SKILL_IMPROVES_PAWN_STRUCTURE = 53;
  SKILL_PAWN_STORM = 54;
  SKILL_PROMOTION = 55;
  SKILL_LADDER_MATE = 56;
  SKILL_BACKRANK_MATE 
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04455"></a>
## FND-04455: chesscom.explanation_engine.v1.Skill.SKILL_WINS_TEMPO = 48

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_WINS_TEMPO = 48;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1438.

```text
IFY = 44;
  SKILL_DOUBLE_ROOKS = 45;
  SKILL_CREATES_BATTERY = 46;
  SKILL_PREVENT_CASTLING = 47;
  SKILL_WINS_TEMPO = 48;
  SKILL_AVOIDS_TRADE = 49;
  SKILL_DEVELOP_WITH_TEMPO = 50;
  SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 51;
  SKILL_EN_PASSANT = 52;
  SKILL_IMPROVES_PAWN_STRUCTURE = 53;
  SKILL_PAWN_STORM = 54;
  SKILL_PROMOTION = 55;
  SKILL_LADDER_MATE = 56;
  SKILL_BACKRANK_MATE = 57;
  SKILL_PUSHES_PASSED_PAW
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04456"></a>
## FND-04456: chesscom.explanation_engine.v1.Skill.SKILL_AVOIDS_TRADE = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_AVOIDS_TRADE = 49;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1463.

```text
ROOKS = 45;
  SKILL_CREATES_BATTERY = 46;
  SKILL_PREVENT_CASTLING = 47;
  SKILL_WINS_TEMPO = 48;
  SKILL_AVOIDS_TRADE = 49;
  SKILL_DEVELOP_WITH_TEMPO = 50;
  SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 51;
  SKILL_EN_PASSANT = 52;
  SKILL_IMPROVES_PAWN_STRUCTURE = 53;
  SKILL_PAWN_STORM = 54;
  SKILL_PROMOTION = 55;
  SKILL_LADDER_MATE = 56;
  SKILL_BACKRANK_MATE = 57;
  SKILL_PUSHES_PASSED_PAWN = 58;
  SKILL_QUEEN_CHE
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04457"></a>
## FND-04457: chesscom.explanation_engine.v1.Skill.SKILL_DEVELOP_WITH_TEMPO = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_DEVELOP_WITH_TEMPO = 50;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1490.

```text
_BATTERY = 46;
  SKILL_PREVENT_CASTLING = 47;
  SKILL_WINS_TEMPO = 48;
  SKILL_AVOIDS_TRADE = 49;
  SKILL_DEVELOP_WITH_TEMPO = 50;
  SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 51;
  SKILL_EN_PASSANT = 52;
  SKILL_IMPROVES_PAWN_STRUCTURE = 53;
  SKILL_PAWN_STORM = 54;
  SKILL_PROMOTION = 55;
  SKILL_LADDER_MATE = 56;
  SKILL_BACKRANK_MATE = 57;
  SKILL_PUSHES_PASSED_PAWN = 58;
  SKILL_QUEEN_CHECKMATE = 59;
  SKILL_ROOK_C
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04458"></a>
## FND-04458: chesscom.explanation_engine.v1.Skill.SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 51

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 51;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1523.

```text
STLING = 47;
  SKILL_WINS_TEMPO = 48;
  SKILL_AVOIDS_TRADE = 49;
  SKILL_DEVELOP_WITH_TEMPO = 50;
  SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 51;
  SKILL_EN_PASSANT = 52;
  SKILL_IMPROVES_PAWN_STRUCTURE = 53;
  SKILL_PAWN_STORM = 54;
  SKILL_PROMOTION = 55;
  SKILL_LADDER_MATE = 56;
  SKILL_BACKRANK_MATE = 57;
  SKILL_PUSHES_PASSED_PAWN = 58;
  SKILL_QUEEN_CHECKMATE = 59;
  SKILL_ROOK_CHECKMATE = 60;
  SKILL_MAKES_PASS
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04459"></a>
## FND-04459: chesscom.explanation_engine.v1.Skill.SKILL_EN_PASSANT = 52

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_EN_PASSANT = 52;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1569.

```text
AVOIDS_TRADE = 49;
  SKILL_DEVELOP_WITH_TEMPO = 50;
  SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 51;
  SKILL_EN_PASSANT = 52;
  SKILL_IMPROVES_PAWN_STRUCTURE = 53;
  SKILL_PAWN_STORM = 54;
  SKILL_PROMOTION = 55;
  SKILL_LADDER_MATE = 56;
  SKILL_BACKRANK_MATE = 57;
  SKILL_PUSHES_PASSED_PAWN = 58;
  SKILL_QUEEN_CHECKMATE = 59;
  SKILL_ROOK_CHECKMATE = 60;
  SKILL_MAKES_PASSED_PAWN = 61;
  SKILL_ACTIVATE_KING = 62;
  SK
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04460"></a>
## FND-04460: chesscom.explanation_engine.v1.Skill.SKILL_IMPROVES_PAWN_STRUCTURE = 53

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_IMPROVES_PAWN_STRUCTURE = 53;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1594.

```text
L_DEVELOP_WITH_TEMPO = 50;
  SKILL_DAMAGES_OPPONENT_PAWN_STRUCTURE = 51;
  SKILL_EN_PASSANT = 52;
  SKILL_IMPROVES_PAWN_STRUCTURE = 53;
  SKILL_PAWN_STORM = 54;
  SKILL_PROMOTION = 55;
  SKILL_LADDER_MATE = 56;
  SKILL_BACKRANK_MATE = 57;
  SKILL_PUSHES_PASSED_PAWN = 58;
  SKILL_QUEEN_CHECKMATE = 59;
  SKILL_ROOK_CHECKMATE = 60;
  SKILL_MAKES_PASSED_PAWN = 61;
  SKILL_ACTIVATE_KING = 62;
  SKILL_ROOK_TO_SEVENTH = 63;
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04461"></a>
## FND-04461: chesscom.explanation_engine.v1.Skill.SKILL_PAWN_STORM = 54

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_PAWN_STORM = 54;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1632.

```text
AGES_OPPONENT_PAWN_STRUCTURE = 51;
  SKILL_EN_PASSANT = 52;
  SKILL_IMPROVES_PAWN_STRUCTURE = 53;
  SKILL_PAWN_STORM = 54;
  SKILL_PROMOTION = 55;
  SKILL_LADDER_MATE = 56;
  SKILL_BACKRANK_MATE = 57;
  SKILL_PUSHES_PASSED_PAWN = 58;
  SKILL_QUEEN_CHECKMATE = 59;
  SKILL_ROOK_CHECKMATE = 60;
  SKILL_MAKES_PASSED_PAWN = 61;
  SKILL_ACTIVATE_KING = 62;
  SKILL_ROOK_TO_SEVENTH = 63;
  SKILL_ROOK_BEHIND_OWN_PASSED_PAWN =
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04462"></a>
## FND-04462: chesscom.explanation_engine.v1.Skill.SKILL_PROMOTION = 55

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_PROMOTION = 55;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1657.

```text
URE = 51;
  SKILL_EN_PASSANT = 52;
  SKILL_IMPROVES_PAWN_STRUCTURE = 53;
  SKILL_PAWN_STORM = 54;
  SKILL_PROMOTION = 55;
  SKILL_LADDER_MATE = 56;
  SKILL_BACKRANK_MATE = 57;
  SKILL_PUSHES_PASSED_PAWN = 58;
  SKILL_QUEEN_CHECKMATE = 59;
  SKILL_ROOK_CHECKMATE = 60;
  SKILL_MAKES_PASSED_PAWN = 61;
  SKILL_ACTIVATE_KING = 62;
  SKILL_ROOK_TO_SEVENTH = 63;
  SKILL_ROOK_BEHIND_OWN_PASSED_PAWN = 64;
  SKILL_OPPOSITION =
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04463"></a>
## FND-04463: chesscom.explanation_engine.v1.Skill.SKILL_LADDER_MATE = 56

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_LADDER_MATE = 56;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1681.

```text
SANT = 52;
  SKILL_IMPROVES_PAWN_STRUCTURE = 53;
  SKILL_PAWN_STORM = 54;
  SKILL_PROMOTION = 55;
  SKILL_LADDER_MATE = 56;
  SKILL_BACKRANK_MATE = 57;
  SKILL_PUSHES_PASSED_PAWN = 58;
  SKILL_QUEEN_CHECKMATE = 59;
  SKILL_ROOK_CHECKMATE = 60;
  SKILL_MAKES_PASSED_PAWN = 61;
  SKILL_ACTIVATE_KING = 62;
  SKILL_ROOK_TO_SEVENTH = 63;
  SKILL_ROOK_BEHIND_OWN_PASSED_PAWN = 64;
  SKILL_OPPOSITION = 65;
  SKILL_DOUBLED_ROO
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04464"></a>
## FND-04464: chesscom.explanation_engine.v1.Skill.SKILL_BACKRANK_MATE = 57

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_BACKRANK_MATE = 57;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1707.

```text
S_PAWN_STRUCTURE = 53;
  SKILL_PAWN_STORM = 54;
  SKILL_PROMOTION = 55;
  SKILL_LADDER_MATE = 56;
  SKILL_BACKRANK_MATE = 57;
  SKILL_PUSHES_PASSED_PAWN = 58;
  SKILL_QUEEN_CHECKMATE = 59;
  SKILL_ROOK_CHECKMATE = 60;
  SKILL_MAKES_PASSED_PAWN = 61;
  SKILL_ACTIVATE_KING = 62;
  SKILL_ROOK_TO_SEVENTH = 63;
  SKILL_ROOK_BEHIND_OWN_PASSED_PAWN = 64;
  SKILL_OPPOSITION = 65;
  SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH = 66;
  
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04465"></a>
## FND-04465: chesscom.explanation_engine.v1.Skill.SKILL_PUSHES_PASSED_PAWN = 58

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_PUSHES_PASSED_PAWN = 58;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1735.

```text
LL_PAWN_STORM = 54;
  SKILL_PROMOTION = 55;
  SKILL_LADDER_MATE = 56;
  SKILL_BACKRANK_MATE = 57;
  SKILL_PUSHES_PASSED_PAWN = 58;
  SKILL_QUEEN_CHECKMATE = 59;
  SKILL_ROOK_CHECKMATE = 60;
  SKILL_MAKES_PASSED_PAWN = 61;
  SKILL_ACTIVATE_KING = 62;
  SKILL_ROOK_TO_SEVENTH = 63;
  SKILL_ROOK_BEHIND_OWN_PASSED_PAWN = 64;
  SKILL_OPPOSITION = 65;
  SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH = 66;
  SKILL_ROOK_BEHIND_OPPOSING_P
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04466"></a>
## FND-04466: chesscom.explanation_engine.v1.Skill.SKILL_QUEEN_CHECKMATE = 59

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_QUEEN_CHECKMATE = 59;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1768.

```text
TION = 55;
  SKILL_LADDER_MATE = 56;
  SKILL_BACKRANK_MATE = 57;
  SKILL_PUSHES_PASSED_PAWN = 58;
  SKILL_QUEEN_CHECKMATE = 59;
  SKILL_ROOK_CHECKMATE = 60;
  SKILL_MAKES_PASSED_PAWN = 61;
  SKILL_ACTIVATE_KING = 62;
  SKILL_ROOK_TO_SEVENTH = 63;
  SKILL_ROOK_BEHIND_OWN_PASSED_PAWN = 64;
  SKILL_OPPOSITION = 65;
  SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH = 66;
  SKILL_ROOK_BEHIND_OPPOSING_PASSED_PAWN = 67;
  SKILL_MAKES_PR
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04467"></a>
## FND-04467: chesscom.explanation_engine.v1.Skill.SKILL_ROOK_CHECKMATE = 60

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_ROOK_CHECKMATE = 60;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1798.

```text
 = 56;
  SKILL_BACKRANK_MATE = 57;
  SKILL_PUSHES_PASSED_PAWN = 58;
  SKILL_QUEEN_CHECKMATE = 59;
  SKILL_ROOK_CHECKMATE = 60;
  SKILL_MAKES_PASSED_PAWN = 61;
  SKILL_ACTIVATE_KING = 62;
  SKILL_ROOK_TO_SEVENTH = 63;
  SKILL_ROOK_BEHIND_OWN_PASSED_PAWN = 64;
  SKILL_OPPOSITION = 65;
  SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH = 66;
  SKILL_ROOK_BEHIND_OPPOSING_PASSED_PAWN = 67;
  SKILL_MAKES_PROTECTED_PASSED_PAWN = 68;
  SK
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04468"></a>
## FND-04468: chesscom.explanation_engine.v1.Skill.SKILL_MAKES_PASSED_PAWN = 61

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_MAKES_PASSED_PAWN = 61;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1827.

```text
= 57;
  SKILL_PUSHES_PASSED_PAWN = 58;
  SKILL_QUEEN_CHECKMATE = 59;
  SKILL_ROOK_CHECKMATE = 60;
  SKILL_MAKES_PASSED_PAWN = 61;
  SKILL_ACTIVATE_KING = 62;
  SKILL_ROOK_TO_SEVENTH = 63;
  SKILL_ROOK_BEHIND_OWN_PASSED_PAWN = 64;
  SKILL_OPPOSITION = 65;
  SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH = 66;
  SKILL_ROOK_BEHIND_OPPOSING_PASSED_PAWN = 67;
  SKILL_MAKES_PROTECTED_PASSED_PAWN = 68;
  SKILL_KING_AND_PAWN_ENDGAMES = 
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04469"></a>
## FND-04469: chesscom.explanation_engine.v1.Skill.SKILL_ACTIVATE_KING = 62

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_ACTIVATE_KING = 62;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1859.

```text
 = 58;
  SKILL_QUEEN_CHECKMATE = 59;
  SKILL_ROOK_CHECKMATE = 60;
  SKILL_MAKES_PASSED_PAWN = 61;
  SKILL_ACTIVATE_KING = 62;
  SKILL_ROOK_TO_SEVENTH = 63;
  SKILL_ROOK_BEHIND_OWN_PASSED_PAWN = 64;
  SKILL_OPPOSITION = 65;
  SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH = 66;
  SKILL_ROOK_BEHIND_OPPOSING_PASSED_PAWN = 67;
  SKILL_MAKES_PROTECTED_PASSED_PAWN = 68;
  SKILL_KING_AND_PAWN_ENDGAMES = 69;
  SKILL_QUEEN_ENDGAMES = 70;
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04470"></a>
## FND-04470: chesscom.explanation_engine.v1.Skill.SKILL_ROOK_TO_SEVENTH = 63

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_ROOK_TO_SEVENTH = 63;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1887.

```text
TE = 59;
  SKILL_ROOK_CHECKMATE = 60;
  SKILL_MAKES_PASSED_PAWN = 61;
  SKILL_ACTIVATE_KING = 62;
  SKILL_ROOK_TO_SEVENTH = 63;
  SKILL_ROOK_BEHIND_OWN_PASSED_PAWN = 64;
  SKILL_OPPOSITION = 65;
  SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH = 66;
  SKILL_ROOK_BEHIND_OPPOSING_PASSED_PAWN = 67;
  SKILL_MAKES_PROTECTED_PASSED_PAWN = 68;
  SKILL_KING_AND_PAWN_ENDGAMES = 69;
  SKILL_QUEEN_ENDGAMES = 70;
  SKILL_ROOK_ENDGAMES = 71;
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04471"></a>
## FND-04471: chesscom.explanation_engine.v1.Skill.SKILL_ROOK_BEHIND_OWN_PASSED_PAWN = 64

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_ROOK_BEHIND_OWN_PASSED_PAWN = 64;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1917.

```text
E = 60;
  SKILL_MAKES_PASSED_PAWN = 61;
  SKILL_ACTIVATE_KING = 62;
  SKILL_ROOK_TO_SEVENTH = 63;
  SKILL_ROOK_BEHIND_OWN_PASSED_PAWN = 64;
  SKILL_OPPOSITION = 65;
  SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH = 66;
  SKILL_ROOK_BEHIND_OPPOSING_PASSED_PAWN = 67;
  SKILL_MAKES_PROTECTED_PASSED_PAWN = 68;
  SKILL_KING_AND_PAWN_ENDGAMES = 69;
  SKILL_QUEEN_ENDGAMES = 70;
  SKILL_ROOK_ENDGAMES = 71;
  SKILL_KNIGHT_AND_BISHOP_END
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04472"></a>
## FND-04472: chesscom.explanation_engine.v1.Skill.SKILL_OPPOSITION = 65

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_OPPOSITION = 65;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1959.

```text
SKILL_ACTIVATE_KING = 62;
  SKILL_ROOK_TO_SEVENTH = 63;
  SKILL_ROOK_BEHIND_OWN_PASSED_PAWN = 64;
  SKILL_OPPOSITION = 65;
  SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH = 66;
  SKILL_ROOK_BEHIND_OPPOSING_PASSED_PAWN = 67;
  SKILL_MAKES_PROTECTED_PASSED_PAWN = 68;
  SKILL_KING_AND_PAWN_ENDGAMES = 69;
  SKILL_QUEEN_ENDGAMES = 70;
  SKILL_ROOK_ENDGAMES = 71;
  SKILL_KNIGHT_AND_BISHOP_ENDGAMES = 72;
}

message SkillsPosition {
  
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04473"></a>
## FND-04473: chesscom.explanation_engine.v1.Skill.SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH = 66

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH = 66;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 1984.

```text

  SKILL_ROOK_TO_SEVENTH = 63;
  SKILL_ROOK_BEHIND_OWN_PASSED_PAWN = 64;
  SKILL_OPPOSITION = 65;
  SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH = 66;
  SKILL_ROOK_BEHIND_OPPOSING_PASSED_PAWN = 67;
  SKILL_MAKES_PROTECTED_PASSED_PAWN = 68;
  SKILL_KING_AND_PAWN_ENDGAMES = 69;
  SKILL_QUEEN_ENDGAMES = 70;
  SKILL_ROOK_ENDGAMES = 71;
  SKILL_KNIGHT_AND_BISHOP_ENDGAMES = 72;
}

message SkillsPosition {
  optional int32 ply = 1;
 
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04474"></a>
## FND-04474: chesscom.explanation_engine.v1.Skill.SKILL_ROOK_BEHIND_OPPOSING_PASSED_PAWN = 67

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_ROOK_BEHIND_OPPOSING_PASSED_PAWN = 67;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 2027.

```text
_BEHIND_OWN_PASSED_PAWN = 64;
  SKILL_OPPOSITION = 65;
  SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH = 66;
  SKILL_ROOK_BEHIND_OPPOSING_PASSED_PAWN = 67;
  SKILL_MAKES_PROTECTED_PASSED_PAWN = 68;
  SKILL_KING_AND_PAWN_ENDGAMES = 69;
  SKILL_QUEEN_ENDGAMES = 70;
  SKILL_ROOK_ENDGAMES = 71;
  SKILL_KNIGHT_AND_BISHOP_ENDGAMES = 72;
}

message SkillsPosition {
  optional int32 ply = 1;
  repeated .chesscom.explanation_engine.v1.S
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
