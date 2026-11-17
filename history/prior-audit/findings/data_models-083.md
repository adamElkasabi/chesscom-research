# data_models — findings 8201–8300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-08475"></a>
## FND-08475: chesscom.stats.v1.AdvancedStatExample.stat = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.stats.v1.AdvancedStatType stat = 1;

### Evidence

- **SRC-0560** `research/proto/chesscom/stats/v1/advanced_stat_example.proto` — [preserved redacted evidence](../evidence/text/285641f778a6368c055c2c43fb0019f71e97dbb3b996c67bb58cf12a3149de11.proto)
  Character offset 305.

```text
AMPLE_OUTCOME_GOOD = 1;
  ADVANCED_STAT_EXAMPLE_OUTCOME_BAD = 2;
}

message AdvancedStatExample {
  optional .chesscom.stats.v1.AdvancedStatType stat = 1;
  optional .chesscom.stats.v1.AdvancedStatExampleOutcome outcome = 2;
  optional int32 ply = 3;
  optional string san = 4;
}

```

**Source references:** SRC-0560, SRC-1531  
**URL references:** None independently associated  
**Related findings:** FND-08470, FND-08471, FND-08472

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08476"></a>
## FND-08476: chesscom.stats.v1.AdvancedStatExample.outcome = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.stats.v1.AdvancedStatExampleOutcome outcome = 2;

### Evidence

- **SRC-0560** `research/proto/chesscom/stats/v1/advanced_stat_example.proto` — [preserved redacted evidence](../evidence/text/285641f778a6368c055c2c43fb0019f71e97dbb3b996c67bb58cf12a3149de11.proto)
  Character offset 362.

```text
AD = 2;
}

message AdvancedStatExample {
  optional .chesscom.stats.v1.AdvancedStatType stat = 1;
  optional .chesscom.stats.v1.AdvancedStatExampleOutcome outcome = 2;
  optional int32 ply = 3;
  optional string san = 4;
}

```

**Source references:** SRC-0560, SRC-1531  
**URL references:** None independently associated  
**Related findings:** FND-08470, FND-08471, FND-08472

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08477"></a>
## FND-08477: chesscom.stats.v1.AdvancedStatExample.ply = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 ply = 3;

### Evidence

- **SRC-0560** `research/proto/chesscom/stats/v1/advanced_stat_example.proto` — [preserved redacted evidence](../evidence/text/285641f778a6368c055c2c43fb0019f71e97dbb3b996c67bb58cf12a3149de11.proto)
  Character offset 432.

```text
.AdvancedStatType stat = 1;
  optional .chesscom.stats.v1.AdvancedStatExampleOutcome outcome = 2;
  optional int32 ply = 3;
  optional string san = 4;
}

```

**Source references:** SRC-0560, SRC-1531  
**URL references:** None independently associated  
**Related findings:** FND-08470, FND-08471, FND-08472

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08478"></a>
## FND-08478: chesscom.stats.v1.AdvancedStatExample.san = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string san = 4;

### Evidence

- **SRC-0560** `research/proto/chesscom/stats/v1/advanced_stat_example.proto` — [preserved redacted evidence](../evidence/text/285641f778a6368c055c2c43fb0019f71e97dbb3b996c67bb58cf12a3149de11.proto)
  Character offset 458.

```text
;
  optional .chesscom.stats.v1.AdvancedStatExampleOutcome outcome = 2;
  optional int32 ply = 3;
  optional string san = 4;
}

```

**Source references:** SRC-0560, SRC-1531  
**URL references:** None independently associated  
**Related findings:** FND-08470, FND-08471, FND-08472

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08479"></a>
## FND-08479: message declaration: chesscom.stats.v1.AdvancedStatPercentile

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AdvancedStatPercentile {

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 107.

```text
ce: chesscom/stats/v1/advanced_stat_percentile.proto
// syntax: proto3

package chesscom.stats.v1;

message AdvancedStatPercentile {
  oneof _ewma_12_percentile {
  float ewma_12_percentile = 3;
  }
  oneof _ewma_50_percentile {
  float ewma_50_percentile = 4;
  }
  oneof _requested_game_percentile {
  float requested_game_percentile = 5;
  }
  optional .chesscom.stats.v1.AdvancedStatType type = 1;
  optional uint32 
```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08480, FND-08481

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08480"></a>
## FND-08480: oneof declaration: chesscom.stats.v1.AdvancedStatPercentile._ewma_12_percentile

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ewma_12_percentile {

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 142.

```text
_percentile.proto
// syntax: proto3

package chesscom.stats.v1;

message AdvancedStatPercentile {
  oneof _ewma_12_percentile {
  float ewma_12_percentile = 3;
  }
  oneof _ewma_50_percentile {
  float ewma_50_percentile = 4;
  }
  oneof _requested_game_percentile {
  float requested_game_percentile = 5;
  }
  optional .chesscom.stats.v1.AdvancedStatType type = 1;
  optional uint32 games_played = 2;
}

message Advanc
```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08481

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08481"></a>
## FND-08481: chesscom.stats.v1.AdvancedStatPercentile.ewma_12_percentile = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float ewma_12_percentile = 3;

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 172.

```text
roto3

package chesscom.stats.v1;

message AdvancedStatPercentile {
  oneof _ewma_12_percentile {
  float ewma_12_percentile = 3;
  }
  oneof _ewma_50_percentile {
  float ewma_50_percentile = 4;
  }
  oneof _requested_game_percentile {
  float requested_game_percentile = 5;
  }
  optional .chesscom.stats.v1.AdvancedStatType type = 1;
  optional uint32 games_played = 2;
}

message AdvancedStatCategoryStats {
  option
```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08482"></a>
## FND-08482: oneof declaration: chesscom.stats.v1.AdvancedStatPercentile._ewma_50_percentile

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ewma_50_percentile {

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 208.

```text
essage AdvancedStatPercentile {
  oneof _ewma_12_percentile {
  float ewma_12_percentile = 3;
  }
  oneof _ewma_50_percentile {
  float ewma_50_percentile = 4;
  }
  oneof _requested_game_percentile {
  float requested_game_percentile = 5;
  }
  optional .chesscom.stats.v1.AdvancedStatType type = 1;
  optional uint32 games_played = 2;
}

message AdvancedStatCategoryStats {
  optional .chesscom.stats.v1.AdvancedStatTy
```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480, FND-08481

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08483"></a>
## FND-08483: chesscom.stats.v1.AdvancedStatPercentile.ewma_50_percentile = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float ewma_50_percentile = 4;

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 238.

```text
{
  oneof _ewma_12_percentile {
  float ewma_12_percentile = 3;
  }
  oneof _ewma_50_percentile {
  float ewma_50_percentile = 4;
  }
  oneof _requested_game_percentile {
  float requested_game_percentile = 5;
  }
  optional .chesscom.stats.v1.AdvancedStatType type = 1;
  optional uint32 games_played = 2;
}

message AdvancedStatCategoryStats {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional fl
```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480, FND-08481

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08484"></a>
## FND-08484: oneof declaration: chesscom.stats.v1.AdvancedStatPercentile._requested_game_percentile

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _requested_game_percentile {

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 274.

```text
oat ewma_12_percentile = 3;
  }
  oneof _ewma_50_percentile {
  float ewma_50_percentile = 4;
  }
  oneof _requested_game_percentile {
  float requested_game_percentile = 5;
  }
  optional .chesscom.stats.v1.AdvancedStatType type = 1;
  optional uint32 games_played = 2;
}

message AdvancedStatCategoryStats {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
  optional uint3
```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480, FND-08481

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08485"></a>
## FND-08485: chesscom.stats.v1.AdvancedStatPercentile.requested_game_percentile = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float requested_game_percentile = 5;

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 311.

```text
of _ewma_50_percentile {
  float ewma_50_percentile = 4;
  }
  oneof _requested_game_percentile {
  float requested_game_percentile = 5;
  }
  optional .chesscom.stats.v1.AdvancedStatType type = 1;
  optional uint32 games_played = 2;
}

message AdvancedStatCategoryStats {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
  optional uint32 old_rating = 3;
  optional uint32 n
```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480, FND-08481

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08486"></a>
## FND-08486: chesscom.stats.v1.AdvancedStatPercentile.type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.stats.v1.AdvancedStatType type = 1;

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 354.

```text
rcentile = 4;
  }
  oneof _requested_game_percentile {
  float requested_game_percentile = 5;
  }
  optional .chesscom.stats.v1.AdvancedStatType type = 1;
  optional uint32 games_played = 2;
}

message AdvancedStatCategoryStats {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
  optional uint32 old_rating = 3;
  optional uint32 new_rating = 4;
}

message AdvancedStatCateg
```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480, FND-08481

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08487"></a>
## FND-08487: chesscom.stats.v1.AdvancedStatPercentile.games_played = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 games_played = 2;

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 411.

```text
float requested_game_percentile = 5;
  }
  optional .chesscom.stats.v1.AdvancedStatType type = 1;
  optional uint32 games_played = 2;
}

message AdvancedStatCategoryStats {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
  optional uint32 old_rating = 3;
  optional uint32 new_rating = 4;
}

message AdvancedStatCategoryGamePerformance {
  optional .chesscom.stats.v1.Advanc
```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480, FND-08481

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08488"></a>
## FND-08488: message declaration: chesscom.stats.v1.AdvancedStatCategoryStats

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AdvancedStatCategoryStats {

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 448.

```text
  }
  optional .chesscom.stats.v1.AdvancedStatType type = 1;
  optional uint32 games_played = 2;
}

message AdvancedStatCategoryStats {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
  optional uint32 old_rating = 3;
  optional uint32 new_rating = 4;
}

message AdvancedStatCategoryGamePerformance {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional f
```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480, FND-08481

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08489"></a>
## FND-08489: chesscom.stats.v1.AdvancedStatCategoryStats.category = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.stats.v1.AdvancedStatType category = 1;

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 486.

```text
ncedStatType type = 1;
  optional uint32 games_played = 2;
}

message AdvancedStatCategoryStats {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
  optional uint32 old_rating = 3;
  optional uint32 new_rating = 4;
}

message AdvancedStatCategoryGamePerformance {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
}

```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480, FND-08481

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08490"></a>
## FND-08490: chesscom.stats.v1.AdvancedStatCategoryStats.percentile = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float percentile = 2;

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 547.

```text

message AdvancedStatCategoryStats {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
  optional uint32 old_rating = 3;
  optional uint32 new_rating = 4;
}

message AdvancedStatCategoryGamePerformance {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
}

```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480, FND-08481

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08491"></a>
## FND-08491: chesscom.stats.v1.AdvancedStatCategoryStats.old_rating = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 old_rating = 3;

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 580.

```text
s {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
  optional uint32 old_rating = 3;
  optional uint32 new_rating = 4;
}

message AdvancedStatCategoryGamePerformance {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
}

```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480, FND-08481

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08492"></a>
## FND-08492: chesscom.stats.v1.AdvancedStatCategoryStats.new_rating = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 new_rating = 4;

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 614.

```text
AdvancedStatType category = 1;
  optional float percentile = 2;
  optional uint32 old_rating = 3;
  optional uint32 new_rating = 4;
}

message AdvancedStatCategoryGamePerformance {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
}

```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480, FND-08481

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08493"></a>
## FND-08493: message declaration: chesscom.stats.v1.AdvancedStatCategoryGamePerformance

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AdvancedStatCategoryGamePerformance {

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 649.

```text
tional float percentile = 2;
  optional uint32 old_rating = 3;
  optional uint32 new_rating = 4;
}

message AdvancedStatCategoryGamePerformance {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
}

```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480, FND-08481

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08494"></a>
## FND-08494: chesscom.stats.v1.AdvancedStatCategoryGamePerformance.category = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.stats.v1.AdvancedStatType category = 1;

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 486.

```text
ncedStatType type = 1;
  optional uint32 games_played = 2;
}

message AdvancedStatCategoryStats {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
  optional uint32 old_rating = 3;
  optional uint32 new_rating = 4;
}

message AdvancedStatCategoryGamePerformance {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
}

```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480, FND-08481

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08495"></a>
## FND-08495: chesscom.stats.v1.AdvancedStatCategoryGamePerformance.percentile = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float percentile = 2;

### Evidence

- **SRC-0561** `research/proto/chesscom/stats/v1/advanced_stat_percentile.proto` — [preserved redacted evidence](../evidence/text/8cb5d78e1f65ab65bd42bda191387d8839211a91fd04a63883aec6d8f5193cf9.proto)
  Character offset 547.

```text

message AdvancedStatCategoryStats {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
  optional uint32 old_rating = 3;
  optional uint32 new_rating = 4;
}

message AdvancedStatCategoryGamePerformance {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional float percentile = 2;
}

```

**Source references:** SRC-0561, SRC-1532  
**URL references:** None independently associated  
**Related findings:** FND-08479, FND-08480, FND-08481

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08496"></a>
## FND-08496: enum declaration: chesscom.stats.v1.AdvancedStatType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum AdvancedStatType {

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 101.

```text
/ source: chesscom/stats/v1/advanced_stat_type.proto
// syntax: proto3

package chesscom.stats.v1;

enum AdvancedStatType {
  ADVANCED_STAT_TYPE_UNSPECIFIED = 0;
  ADVANCED_STAT_TYPE_OPENING_ACCURACY = 1;
  ADVANCED_STAT_TYPE_OPENING_MISTAKES = 2;
  ADVANCED_STAT_TYPE_BOOK_MOVES = 3;
  ADVANCED_STAT_TYPE_FOUND_CHECKMATE = 4;
  ADVANCED_STAT_TYPE_FOUND_FREE_PIECES = 5;
  ADVANCED_STAT_TYPE_FOUND_ALL_TACTICS = 6;
  ADV
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08497"></a>
## FND-08497: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 127.

```text
1/advanced_stat_type.proto
// syntax: proto3

package chesscom.stats.v1;

enum AdvancedStatType {
  ADVANCED_STAT_TYPE_UNSPECIFIED = 0;
  ADVANCED_STAT_TYPE_OPENING_ACCURACY = 1;
  ADVANCED_STAT_TYPE_OPENING_MISTAKES = 2;
  ADVANCED_STAT_TYPE_BOOK_MOVES = 3;
  ADVANCED_STAT_TYPE_FOUND_CHECKMATE = 4;
  ADVANCED_STAT_TYPE_FOUND_FREE_PIECES = 5;
  ADVANCED_STAT_TYPE_FOUND_ALL_TACTICS = 6;
  ADVANCED_STAT_TYPE_FOUND_UNTH
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08498"></a>
## FND-08498: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_OPENING_ACCURACY = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_OPENING_ACCURACY = 1;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 165.

```text
proto3

package chesscom.stats.v1;

enum AdvancedStatType {
  ADVANCED_STAT_TYPE_UNSPECIFIED = 0;
  ADVANCED_STAT_TYPE_OPENING_ACCURACY = 1;
  ADVANCED_STAT_TYPE_OPENING_MISTAKES = 2;
  ADVANCED_STAT_TYPE_BOOK_MOVES = 3;
  ADVANCED_STAT_TYPE_FOUND_CHECKMATE = 4;
  ADVANCED_STAT_TYPE_FOUND_FREE_PIECES = 5;
  ADVANCED_STAT_TYPE_FOUND_ALL_TACTICS = 6;
  ADVANCED_STAT_TYPE_FOUND_UNTHEMED_TACTICS = 7;
  ADVANCED_STAT_TYPE
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08499"></a>
## FND-08499: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_OPENING_MISTAKES = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_OPENING_MISTAKES = 2;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 208.

```text
vancedStatType {
  ADVANCED_STAT_TYPE_UNSPECIFIED = 0;
  ADVANCED_STAT_TYPE_OPENING_ACCURACY = 1;
  ADVANCED_STAT_TYPE_OPENING_MISTAKES = 2;
  ADVANCED_STAT_TYPE_BOOK_MOVES = 3;
  ADVANCED_STAT_TYPE_FOUND_CHECKMATE = 4;
  ADVANCED_STAT_TYPE_FOUND_FREE_PIECES = 5;
  ADVANCED_STAT_TYPE_FOUND_ALL_TACTICS = 6;
  ADVANCED_STAT_TYPE_FOUND_UNTHEMED_TACTICS = 7;
  ADVANCED_STAT_TYPE_FOUND_FORKS = 8;
  ADVANCED_STAT_TYPE_FOUN
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08500"></a>
## FND-08500: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_BOOK_MOVES = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_BOOK_MOVES = 3;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 251.

```text
CIFIED = 0;
  ADVANCED_STAT_TYPE_OPENING_ACCURACY = 1;
  ADVANCED_STAT_TYPE_OPENING_MISTAKES = 2;
  ADVANCED_STAT_TYPE_BOOK_MOVES = 3;
  ADVANCED_STAT_TYPE_FOUND_CHECKMATE = 4;
  ADVANCED_STAT_TYPE_FOUND_FREE_PIECES = 5;
  ADVANCED_STAT_TYPE_FOUND_ALL_TACTICS = 6;
  ADVANCED_STAT_TYPE_FOUND_UNTHEMED_TACTICS = 7;
  ADVANCED_STAT_TYPE_FOUND_FORKS = 8;
  ADVANCED_STAT_TYPE_FOUND_PINS = 9;
  ADVANCED_STAT_TYPE_FOUND_DISC
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08501"></a>
## FND-08501: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_FOUND_CHECKMATE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_FOUND_CHECKMATE = 4;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 288.

```text
ING_ACCURACY = 1;
  ADVANCED_STAT_TYPE_OPENING_MISTAKES = 2;
  ADVANCED_STAT_TYPE_BOOK_MOVES = 3;
  ADVANCED_STAT_TYPE_FOUND_CHECKMATE = 4;
  ADVANCED_STAT_TYPE_FOUND_FREE_PIECES = 5;
  ADVANCED_STAT_TYPE_FOUND_ALL_TACTICS = 6;
  ADVANCED_STAT_TYPE_FOUND_UNTHEMED_TACTICS = 7;
  ADVANCED_STAT_TYPE_FOUND_FORKS = 8;
  ADVANCED_STAT_TYPE_FOUND_PINS = 9;
  ADVANCED_STAT_TYPE_FOUND_DISCOVERIES = 10;
  ADVANCED_STAT_TYPE_FO
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08502"></a>
## FND-08502: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_FOUND_FREE_PIECES = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_FOUND_FREE_PIECES = 5;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 330.

```text
NING_MISTAKES = 2;
  ADVANCED_STAT_TYPE_BOOK_MOVES = 3;
  ADVANCED_STAT_TYPE_FOUND_CHECKMATE = 4;
  ADVANCED_STAT_TYPE_FOUND_FREE_PIECES = 5;
  ADVANCED_STAT_TYPE_FOUND_ALL_TACTICS = 6;
  ADVANCED_STAT_TYPE_FOUND_UNTHEMED_TACTICS = 7;
  ADVANCED_STAT_TYPE_FOUND_FORKS = 8;
  ADVANCED_STAT_TYPE_FOUND_PINS = 9;
  ADVANCED_STAT_TYPE_FOUND_DISCOVERIES = 10;
  ADVANCED_STAT_TYPE_FOUND_REMOVES_DEFENDERS = 11;
  ADVANCED_STA
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08503"></a>
## FND-08503: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_FOUND_ALL_TACTICS = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_FOUND_ALL_TACTICS = 6;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 374.

```text
_MOVES = 3;
  ADVANCED_STAT_TYPE_FOUND_CHECKMATE = 4;
  ADVANCED_STAT_TYPE_FOUND_FREE_PIECES = 5;
  ADVANCED_STAT_TYPE_FOUND_ALL_TACTICS = 6;
  ADVANCED_STAT_TYPE_FOUND_UNTHEMED_TACTICS = 7;
  ADVANCED_STAT_TYPE_FOUND_FORKS = 8;
  ADVANCED_STAT_TYPE_FOUND_PINS = 9;
  ADVANCED_STAT_TYPE_FOUND_DISCOVERIES = 10;
  ADVANCED_STAT_TYPE_FOUND_REMOVES_DEFENDERS = 11;
  ADVANCED_STAT_TYPE_FOUND_TRAPPED_PIECES = 12;
  ADVANCED
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08504"></a>
## FND-08504: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_FOUND_UNTHEMED_TACTICS = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_FOUND_UNTHEMED_TACTICS = 7;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 418.

```text
MATE = 4;
  ADVANCED_STAT_TYPE_FOUND_FREE_PIECES = 5;
  ADVANCED_STAT_TYPE_FOUND_ALL_TACTICS = 6;
  ADVANCED_STAT_TYPE_FOUND_UNTHEMED_TACTICS = 7;
  ADVANCED_STAT_TYPE_FOUND_FORKS = 8;
  ADVANCED_STAT_TYPE_FOUND_PINS = 9;
  ADVANCED_STAT_TYPE_FOUND_DISCOVERIES = 10;
  ADVANCED_STAT_TYPE_FOUND_REMOVES_DEFENDERS = 11;
  ADVANCED_STAT_TYPE_FOUND_TRAPPED_PIECES = 12;
  ADVANCED_STAT_TYPE_FOUND_SACRIFICES = 13;
  ADVANCED
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08505"></a>
## FND-08505: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_FOUND_FORKS = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_FOUND_FORKS = 8;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 467.

```text
= 5;
  ADVANCED_STAT_TYPE_FOUND_ALL_TACTICS = 6;
  ADVANCED_STAT_TYPE_FOUND_UNTHEMED_TACTICS = 7;
  ADVANCED_STAT_TYPE_FOUND_FORKS = 8;
  ADVANCED_STAT_TYPE_FOUND_PINS = 9;
  ADVANCED_STAT_TYPE_FOUND_DISCOVERIES = 10;
  ADVANCED_STAT_TYPE_FOUND_REMOVES_DEFENDERS = 11;
  ADVANCED_STAT_TYPE_FOUND_TRAPPED_PIECES = 12;
  ADVANCED_STAT_TYPE_FOUND_SACRIFICES = 13;
  ADVANCED_STAT_TYPE_ALLOWED_CHECKMATE = 14;
  ADVANCED_STA
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08506"></a>
## FND-08506: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_FOUND_PINS = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_FOUND_PINS = 9;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 505.

```text
CTICS = 6;
  ADVANCED_STAT_TYPE_FOUND_UNTHEMED_TACTICS = 7;
  ADVANCED_STAT_TYPE_FOUND_FORKS = 8;
  ADVANCED_STAT_TYPE_FOUND_PINS = 9;
  ADVANCED_STAT_TYPE_FOUND_DISCOVERIES = 10;
  ADVANCED_STAT_TYPE_FOUND_REMOVES_DEFENDERS = 11;
  ADVANCED_STAT_TYPE_FOUND_TRAPPED_PIECES = 12;
  ADVANCED_STAT_TYPE_FOUND_SACRIFICES = 13;
  ADVANCED_STAT_TYPE_ALLOWED_CHECKMATE = 14;
  ADVANCED_STAT_TYPE_ALLOWED_FREE_PIECES = 15;
  ADV
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08507"></a>
## FND-08507: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_FOUND_DISCOVERIES = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_FOUND_DISCOVERIES = 10;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 542.

```text
_UNTHEMED_TACTICS = 7;
  ADVANCED_STAT_TYPE_FOUND_FORKS = 8;
  ADVANCED_STAT_TYPE_FOUND_PINS = 9;
  ADVANCED_STAT_TYPE_FOUND_DISCOVERIES = 10;
  ADVANCED_STAT_TYPE_FOUND_REMOVES_DEFENDERS = 11;
  ADVANCED_STAT_TYPE_FOUND_TRAPPED_PIECES = 12;
  ADVANCED_STAT_TYPE_FOUND_SACRIFICES = 13;
  ADVANCED_STAT_TYPE_ALLOWED_CHECKMATE = 14;
  ADVANCED_STAT_TYPE_ALLOWED_FREE_PIECES = 15;
  ADVANCED_STAT_TYPE_ALLOWED_ALL_TACTICS =
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08508"></a>
## FND-08508: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_FOUND_REMOVES_DEFENDERS = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_FOUND_REMOVES_DEFENDERS = 11;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 587.

```text
OUND_FORKS = 8;
  ADVANCED_STAT_TYPE_FOUND_PINS = 9;
  ADVANCED_STAT_TYPE_FOUND_DISCOVERIES = 10;
  ADVANCED_STAT_TYPE_FOUND_REMOVES_DEFENDERS = 11;
  ADVANCED_STAT_TYPE_FOUND_TRAPPED_PIECES = 12;
  ADVANCED_STAT_TYPE_FOUND_SACRIFICES = 13;
  ADVANCED_STAT_TYPE_ALLOWED_CHECKMATE = 14;
  ADVANCED_STAT_TYPE_ALLOWED_FREE_PIECES = 15;
  ADVANCED_STAT_TYPE_ALLOWED_ALL_TACTICS = 16;
  ADVANCED_STAT_TYPE_ALLOWED_UNTHEMED_TA
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08509"></a>
## FND-08509: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_FOUND_TRAPPED_PIECES = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_FOUND_TRAPPED_PIECES = 12;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 638.

```text
;
  ADVANCED_STAT_TYPE_FOUND_DISCOVERIES = 10;
  ADVANCED_STAT_TYPE_FOUND_REMOVES_DEFENDERS = 11;
  ADVANCED_STAT_TYPE_FOUND_TRAPPED_PIECES = 12;
  ADVANCED_STAT_TYPE_FOUND_SACRIFICES = 13;
  ADVANCED_STAT_TYPE_ALLOWED_CHECKMATE = 14;
  ADVANCED_STAT_TYPE_ALLOWED_FREE_PIECES = 15;
  ADVANCED_STAT_TYPE_ALLOWED_ALL_TACTICS = 16;
  ADVANCED_STAT_TYPE_ALLOWED_UNTHEMED_TACTICS = 17;
  ADVANCED_STAT_TYPE_ALLOWED_FORKS = 18
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08510"></a>
## FND-08510: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_FOUND_SACRIFICES = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_FOUND_SACRIFICES = 13;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 686.

```text
 ADVANCED_STAT_TYPE_FOUND_REMOVES_DEFENDERS = 11;
  ADVANCED_STAT_TYPE_FOUND_TRAPPED_PIECES = 12;
  ADVANCED_STAT_TYPE_FOUND_SACRIFICES = 13;
  ADVANCED_STAT_TYPE_ALLOWED_CHECKMATE = 14;
  ADVANCED_STAT_TYPE_ALLOWED_FREE_PIECES = 15;
  ADVANCED_STAT_TYPE_ALLOWED_ALL_TACTICS = 16;
  ADVANCED_STAT_TYPE_ALLOWED_UNTHEMED_TACTICS = 17;
  ADVANCED_STAT_TYPE_ALLOWED_FORKS = 18;
  ADVANCED_STAT_TYPE_ALLOWED_PINS = 19;
  ADVA
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08511"></a>
## FND-08511: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ALLOWED_CHECKMATE = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ALLOWED_CHECKMATE = 14;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 730.

```text
= 11;
  ADVANCED_STAT_TYPE_FOUND_TRAPPED_PIECES = 12;
  ADVANCED_STAT_TYPE_FOUND_SACRIFICES = 13;
  ADVANCED_STAT_TYPE_ALLOWED_CHECKMATE = 14;
  ADVANCED_STAT_TYPE_ALLOWED_FREE_PIECES = 15;
  ADVANCED_STAT_TYPE_ALLOWED_ALL_TACTICS = 16;
  ADVANCED_STAT_TYPE_ALLOWED_UNTHEMED_TACTICS = 17;
  ADVANCED_STAT_TYPE_ALLOWED_FORKS = 18;
  ADVANCED_STAT_TYPE_ALLOWED_PINS = 19;
  ADVANCED_STAT_TYPE_ALLOWED_DISCOVERIES = 20;
  A
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08512"></a>
## FND-08512: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ALLOWED_FREE_PIECES = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ALLOWED_FREE_PIECES = 15;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 775.

```text
ES = 12;
  ADVANCED_STAT_TYPE_FOUND_SACRIFICES = 13;
  ADVANCED_STAT_TYPE_ALLOWED_CHECKMATE = 14;
  ADVANCED_STAT_TYPE_ALLOWED_FREE_PIECES = 15;
  ADVANCED_STAT_TYPE_ALLOWED_ALL_TACTICS = 16;
  ADVANCED_STAT_TYPE_ALLOWED_UNTHEMED_TACTICS = 17;
  ADVANCED_STAT_TYPE_ALLOWED_FORKS = 18;
  ADVANCED_STAT_TYPE_ALLOWED_PINS = 19;
  ADVANCED_STAT_TYPE_ALLOWED_DISCOVERIES = 20;
  ADVANCED_STAT_TYPE_ALLOWED_REMOVES_DEFENDERS =
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08513"></a>
## FND-08513: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ALLOWED_ALL_TACTICS = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ALLOWED_ALL_TACTICS = 16;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 822.

```text
= 13;
  ADVANCED_STAT_TYPE_ALLOWED_CHECKMATE = 14;
  ADVANCED_STAT_TYPE_ALLOWED_FREE_PIECES = 15;
  ADVANCED_STAT_TYPE_ALLOWED_ALL_TACTICS = 16;
  ADVANCED_STAT_TYPE_ALLOWED_UNTHEMED_TACTICS = 17;
  ADVANCED_STAT_TYPE_ALLOWED_FORKS = 18;
  ADVANCED_STAT_TYPE_ALLOWED_PINS = 19;
  ADVANCED_STAT_TYPE_ALLOWED_DISCOVERIES = 20;
  ADVANCED_STAT_TYPE_ALLOWED_REMOVES_DEFENDERS = 21;
  ADVANCED_STAT_TYPE_ALLOWED_TRAPPED_PIECE
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08514"></a>
## FND-08514: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ALLOWED_UNTHEMED_TACTICS = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ALLOWED_UNTHEMED_TACTICS = 17;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 869.

```text
14;
  ADVANCED_STAT_TYPE_ALLOWED_FREE_PIECES = 15;
  ADVANCED_STAT_TYPE_ALLOWED_ALL_TACTICS = 16;
  ADVANCED_STAT_TYPE_ALLOWED_UNTHEMED_TACTICS = 17;
  ADVANCED_STAT_TYPE_ALLOWED_FORKS = 18;
  ADVANCED_STAT_TYPE_ALLOWED_PINS = 19;
  ADVANCED_STAT_TYPE_ALLOWED_DISCOVERIES = 20;
  ADVANCED_STAT_TYPE_ALLOWED_REMOVES_DEFENDERS = 21;
  ADVANCED_STAT_TYPE_ALLOWED_TRAPPED_PIECES = 22;
  ADVANCED_STAT_TYPE_ALLOWED_SACRIFICES
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08515"></a>
## FND-08515: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ALLOWED_FORKS = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ALLOWED_FORKS = 18;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 921.

```text
 ADVANCED_STAT_TYPE_ALLOWED_ALL_TACTICS = 16;
  ADVANCED_STAT_TYPE_ALLOWED_UNTHEMED_TACTICS = 17;
  ADVANCED_STAT_TYPE_ALLOWED_FORKS = 18;
  ADVANCED_STAT_TYPE_ALLOWED_PINS = 19;
  ADVANCED_STAT_TYPE_ALLOWED_DISCOVERIES = 20;
  ADVANCED_STAT_TYPE_ALLOWED_REMOVES_DEFENDERS = 21;
  ADVANCED_STAT_TYPE_ALLOWED_TRAPPED_PIECES = 22;
  ADVANCED_STAT_TYPE_ALLOWED_SACRIFICES = 23;
  ADVANCED_STAT_TYPE_STRATEGIC_ACCURACY = 24;
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08516"></a>
## FND-08516: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ALLOWED_PINS = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ALLOWED_PINS = 19;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 962.

```text
 16;
  ADVANCED_STAT_TYPE_ALLOWED_UNTHEMED_TACTICS = 17;
  ADVANCED_STAT_TYPE_ALLOWED_FORKS = 18;
  ADVANCED_STAT_TYPE_ALLOWED_PINS = 19;
  ADVANCED_STAT_TYPE_ALLOWED_DISCOVERIES = 20;
  ADVANCED_STAT_TYPE_ALLOWED_REMOVES_DEFENDERS = 21;
  ADVANCED_STAT_TYPE_ALLOWED_TRAPPED_PIECES = 22;
  ADVANCED_STAT_TYPE_ALLOWED_SACRIFICES = 23;
  ADVANCED_STAT_TYPE_STRATEGIC_ACCURACY = 24;
  ADVANCED_STAT_TYPE_ATTACKING_ACCURACY 
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08517"></a>
## FND-08517: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ALLOWED_DISCOVERIES = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ALLOWED_DISCOVERIES = 20;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1002.

```text
ED_TACTICS = 17;
  ADVANCED_STAT_TYPE_ALLOWED_FORKS = 18;
  ADVANCED_STAT_TYPE_ALLOWED_PINS = 19;
  ADVANCED_STAT_TYPE_ALLOWED_DISCOVERIES = 20;
  ADVANCED_STAT_TYPE_ALLOWED_REMOVES_DEFENDERS = 21;
  ADVANCED_STAT_TYPE_ALLOWED_TRAPPED_PIECES = 22;
  ADVANCED_STAT_TYPE_ALLOWED_SACRIFICES = 23;
  ADVANCED_STAT_TYPE_STRATEGIC_ACCURACY = 24;
  ADVANCED_STAT_TYPE_ATTACKING_ACCURACY = 25;
  ADVANCED_STAT_TYPE_DEFENDING_ACC
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08518"></a>
## FND-08518: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ALLOWED_REMOVES_DEFENDERS = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ALLOWED_REMOVES_DEFENDERS = 21;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1049.

```text
ORKS = 18;
  ADVANCED_STAT_TYPE_ALLOWED_PINS = 19;
  ADVANCED_STAT_TYPE_ALLOWED_DISCOVERIES = 20;
  ADVANCED_STAT_TYPE_ALLOWED_REMOVES_DEFENDERS = 21;
  ADVANCED_STAT_TYPE_ALLOWED_TRAPPED_PIECES = 22;
  ADVANCED_STAT_TYPE_ALLOWED_SACRIFICES = 23;
  ADVANCED_STAT_TYPE_STRATEGIC_ACCURACY = 24;
  ADVANCED_STAT_TYPE_ATTACKING_ACCURACY = 25;
  ADVANCED_STAT_TYPE_DEFENDING_ACCURACY = 26;
  ADVANCED_STAT_TYPE_SPACE_ADVANTAG
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08519"></a>
## FND-08519: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ALLOWED_TRAPPED_PIECES = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ALLOWED_TRAPPED_PIECES = 22;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1102.

```text
ADVANCED_STAT_TYPE_ALLOWED_DISCOVERIES = 20;
  ADVANCED_STAT_TYPE_ALLOWED_REMOVES_DEFENDERS = 21;
  ADVANCED_STAT_TYPE_ALLOWED_TRAPPED_PIECES = 22;
  ADVANCED_STAT_TYPE_ALLOWED_SACRIFICES = 23;
  ADVANCED_STAT_TYPE_STRATEGIC_ACCURACY = 24;
  ADVANCED_STAT_TYPE_ATTACKING_ACCURACY = 25;
  ADVANCED_STAT_TYPE_DEFENDING_ACCURACY = 26;
  ADVANCED_STAT_TYPE_SPACE_ADVANTAGE_ACCURACY = 27;
  ADVANCED_STAT_TYPE_PIECE_ACTIVITY_
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08520"></a>
## FND-08520: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ALLOWED_SACRIFICES = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ALLOWED_SACRIFICES = 23;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1152.

```text
ANCED_STAT_TYPE_ALLOWED_REMOVES_DEFENDERS = 21;
  ADVANCED_STAT_TYPE_ALLOWED_TRAPPED_PIECES = 22;
  ADVANCED_STAT_TYPE_ALLOWED_SACRIFICES = 23;
  ADVANCED_STAT_TYPE_STRATEGIC_ACCURACY = 24;
  ADVANCED_STAT_TYPE_ATTACKING_ACCURACY = 25;
  ADVANCED_STAT_TYPE_DEFENDING_ACCURACY = 26;
  ADVANCED_STAT_TYPE_SPACE_ADVANTAGE_ACCURACY = 27;
  ADVANCED_STAT_TYPE_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 28;
  ADVANCED_STAT_TYPE_PAWN
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08521"></a>
## FND-08521: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_STRATEGIC_ACCURACY = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_STRATEGIC_ACCURACY = 24;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1198.

```text
;
  ADVANCED_STAT_TYPE_ALLOWED_TRAPPED_PIECES = 22;
  ADVANCED_STAT_TYPE_ALLOWED_SACRIFICES = 23;
  ADVANCED_STAT_TYPE_STRATEGIC_ACCURACY = 24;
  ADVANCED_STAT_TYPE_ATTACKING_ACCURACY = 25;
  ADVANCED_STAT_TYPE_DEFENDING_ACCURACY = 26;
  ADVANCED_STAT_TYPE_SPACE_ADVANTAGE_ACCURACY = 27;
  ADVANCED_STAT_TYPE_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 28;
  ADVANCED_STAT_TYPE_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 29;
  ADVANCED
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08522"></a>
## FND-08522: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ATTACKING_ACCURACY = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ATTACKING_ACCURACY = 25;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1244.

```text
= 22;
  ADVANCED_STAT_TYPE_ALLOWED_SACRIFICES = 23;
  ADVANCED_STAT_TYPE_STRATEGIC_ACCURACY = 24;
  ADVANCED_STAT_TYPE_ATTACKING_ACCURACY = 25;
  ADVANCED_STAT_TYPE_DEFENDING_ACCURACY = 26;
  ADVANCED_STAT_TYPE_SPACE_ADVANTAGE_ACCURACY = 27;
  ADVANCED_STAT_TYPE_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 28;
  ADVANCED_STAT_TYPE_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 29;
  ADVANCED_STAT_TYPE_OPEN_ACCURACY = 30;
  ADVANCED_STAT
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08523"></a>
## FND-08523: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_DEFENDING_ACCURACY = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_DEFENDING_ACCURACY = 26;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1290.

```text
= 23;
  ADVANCED_STAT_TYPE_STRATEGIC_ACCURACY = 24;
  ADVANCED_STAT_TYPE_ATTACKING_ACCURACY = 25;
  ADVANCED_STAT_TYPE_DEFENDING_ACCURACY = 26;
  ADVANCED_STAT_TYPE_SPACE_ADVANTAGE_ACCURACY = 27;
  ADVANCED_STAT_TYPE_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 28;
  ADVANCED_STAT_TYPE_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 29;
  ADVANCED_STAT_TYPE_OPEN_ACCURACY = 30;
  ADVANCED_STAT_TYPE_OPEN_ATTACKING_ACCURACY = 31;
  ADVANCED
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08524"></a>
## FND-08524: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_SPACE_ADVANTAGE_ACCURACY = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_SPACE_ADVANTAGE_ACCURACY = 27;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1336.

```text
= 24;
  ADVANCED_STAT_TYPE_ATTACKING_ACCURACY = 25;
  ADVANCED_STAT_TYPE_DEFENDING_ACCURACY = 26;
  ADVANCED_STAT_TYPE_SPACE_ADVANTAGE_ACCURACY = 27;
  ADVANCED_STAT_TYPE_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 28;
  ADVANCED_STAT_TYPE_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 29;
  ADVANCED_STAT_TYPE_OPEN_ACCURACY = 30;
  ADVANCED_STAT_TYPE_OPEN_ATTACKING_ACCURACY = 31;
  ADVANCED_STAT_TYPE_OPEN_DEFENDING_ACCURACY = 32;
  ADV
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08525"></a>
## FND-08525: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 28;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1388.

```text
  ADVANCED_STAT_TYPE_DEFENDING_ACCURACY = 26;
  ADVANCED_STAT_TYPE_SPACE_ADVANTAGE_ACCURACY = 27;
  ADVANCED_STAT_TYPE_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 28;
  ADVANCED_STAT_TYPE_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 29;
  ADVANCED_STAT_TYPE_OPEN_ACCURACY = 30;
  ADVANCED_STAT_TYPE_OPEN_ATTACKING_ACCURACY = 31;
  ADVANCED_STAT_TYPE_OPEN_DEFENDING_ACCURACY = 32;
  ADVANCED_STAT_TYPE_OPEN_SPACE_ADVANTAGE_ACCURACY = 33;

```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08526"></a>
## FND-08526: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 29;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1449.

```text
_TYPE_SPACE_ADVANTAGE_ACCURACY = 27;
  ADVANCED_STAT_TYPE_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 28;
  ADVANCED_STAT_TYPE_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 29;
  ADVANCED_STAT_TYPE_OPEN_ACCURACY = 30;
  ADVANCED_STAT_TYPE_OPEN_ATTACKING_ACCURACY = 31;
  ADVANCED_STAT_TYPE_OPEN_DEFENDING_ACCURACY = 32;
  ADVANCED_STAT_TYPE_OPEN_SPACE_ADVANTAGE_ACCURACY = 33;
  ADVANCED_STAT_TYPE_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY =
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08527"></a>
## FND-08527: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_OPEN_ACCURACY = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_OPEN_ACCURACY = 30;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1510.

```text
CE_ACTIVITY_ADVANTAGE_ACCURACY = 28;
  ADVANCED_STAT_TYPE_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 29;
  ADVANCED_STAT_TYPE_OPEN_ACCURACY = 30;
  ADVANCED_STAT_TYPE_OPEN_ATTACKING_ACCURACY = 31;
  ADVANCED_STAT_TYPE_OPEN_DEFENDING_ACCURACY = 32;
  ADVANCED_STAT_TYPE_OPEN_SPACE_ADVANTAGE_ACCURACY = 33;
  ADVANCED_STAT_TYPE_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 34;
  ADVANCED_STAT_TYPE_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCUR
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08528"></a>
## FND-08528: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_OPEN_ATTACKING_ACCURACY = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_OPEN_ATTACKING_ACCURACY = 31;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1551.

```text
VANCED_STAT_TYPE_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 29;
  ADVANCED_STAT_TYPE_OPEN_ACCURACY = 30;
  ADVANCED_STAT_TYPE_OPEN_ATTACKING_ACCURACY = 31;
  ADVANCED_STAT_TYPE_OPEN_DEFENDING_ACCURACY = 32;
  ADVANCED_STAT_TYPE_OPEN_SPACE_ADVANTAGE_ACCURACY = 33;
  ADVANCED_STAT_TYPE_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 34;
  ADVANCED_STAT_TYPE_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 35;
  ADVANCED_STAT_TYPE_SEMI_OPEN_
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08529"></a>
## FND-08529: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_OPEN_DEFENDING_ACCURACY = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_OPEN_DEFENDING_ACCURACY = 32;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1602.

```text
= 29;
  ADVANCED_STAT_TYPE_OPEN_ACCURACY = 30;
  ADVANCED_STAT_TYPE_OPEN_ATTACKING_ACCURACY = 31;
  ADVANCED_STAT_TYPE_OPEN_DEFENDING_ACCURACY = 32;
  ADVANCED_STAT_TYPE_OPEN_SPACE_ADVANTAGE_ACCURACY = 33;
  ADVANCED_STAT_TYPE_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 34;
  ADVANCED_STAT_TYPE_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 35;
  ADVANCED_STAT_TYPE_SEMI_OPEN_ACCURACY = 36;
  ADVANCED_STAT_TYPE_SEMI_OPEN_ATTAC
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08530"></a>
## FND-08530: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_OPEN_SPACE_ADVANTAGE_ACCURACY = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_OPEN_SPACE_ADVANTAGE_ACCURACY = 33;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1653.

```text
VANCED_STAT_TYPE_OPEN_ATTACKING_ACCURACY = 31;
  ADVANCED_STAT_TYPE_OPEN_DEFENDING_ACCURACY = 32;
  ADVANCED_STAT_TYPE_OPEN_SPACE_ADVANTAGE_ACCURACY = 33;
  ADVANCED_STAT_TYPE_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 34;
  ADVANCED_STAT_TYPE_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 35;
  ADVANCED_STAT_TYPE_SEMI_OPEN_ACCURACY = 36;
  ADVANCED_STAT_TYPE_SEMI_OPEN_ATTACKING_ACCURACY = 37;
  ADVANCED_STAT_TYPE_SEMI_OPEN_
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08531"></a>
## FND-08531: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 34;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1710.

```text
_STAT_TYPE_OPEN_DEFENDING_ACCURACY = 32;
  ADVANCED_STAT_TYPE_OPEN_SPACE_ADVANTAGE_ACCURACY = 33;
  ADVANCED_STAT_TYPE_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 34;
  ADVANCED_STAT_TYPE_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 35;
  ADVANCED_STAT_TYPE_SEMI_OPEN_ACCURACY = 36;
  ADVANCED_STAT_TYPE_SEMI_OPEN_ATTACKING_ACCURACY = 37;
  ADVANCED_STAT_TYPE_SEMI_OPEN_DEFENDING_ACCURACY = 38;
  ADVANCED_STAT_TYPE_SEMI_OPEN_S
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08532"></a>
## FND-08532: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 35;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1776.

```text
_SPACE_ADVANTAGE_ACCURACY = 33;
  ADVANCED_STAT_TYPE_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 34;
  ADVANCED_STAT_TYPE_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 35;
  ADVANCED_STAT_TYPE_SEMI_OPEN_ACCURACY = 36;
  ADVANCED_STAT_TYPE_SEMI_OPEN_ATTACKING_ACCURACY = 37;
  ADVANCED_STAT_TYPE_SEMI_OPEN_DEFENDING_ACCURACY = 38;
  ADVANCED_STAT_TYPE_SEMI_OPEN_SPACE_ADVANTAGE_ACCURACY = 39;
  ADVANCED_STAT_TYPE_SEMI_OPEN_PIECE
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08533"></a>
## FND-08533: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_SEMI_OPEN_ACCURACY = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_SEMI_OPEN_ACCURACY = 36;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1842.

```text
TIVITY_ADVANTAGE_ACCURACY = 34;
  ADVANCED_STAT_TYPE_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 35;
  ADVANCED_STAT_TYPE_SEMI_OPEN_ACCURACY = 36;
  ADVANCED_STAT_TYPE_SEMI_OPEN_ATTACKING_ACCURACY = 37;
  ADVANCED_STAT_TYPE_SEMI_OPEN_DEFENDING_ACCURACY = 38;
  ADVANCED_STAT_TYPE_SEMI_OPEN_SPACE_ADVANTAGE_ACCURACY = 39;
  ADVANCED_STAT_TYPE_SEMI_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 40;
  ADVANCED_STAT_TYPE_SEMI_OPEN_
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08534"></a>
## FND-08534: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_SEMI_OPEN_ATTACKING_ACCURACY = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_SEMI_OPEN_ATTACKING_ACCURACY = 37;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1888.

```text
T_TYPE_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 35;
  ADVANCED_STAT_TYPE_SEMI_OPEN_ACCURACY = 36;
  ADVANCED_STAT_TYPE_SEMI_OPEN_ATTACKING_ACCURACY = 37;
  ADVANCED_STAT_TYPE_SEMI_OPEN_DEFENDING_ACCURACY = 38;
  ADVANCED_STAT_TYPE_SEMI_OPEN_SPACE_ADVANTAGE_ACCURACY = 39;
  ADVANCED_STAT_TYPE_SEMI_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 40;
  ADVANCED_STAT_TYPE_SEMI_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 41;
  ADVA
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08535"></a>
## FND-08535: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_SEMI_OPEN_DEFENDING_ACCURACY = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_SEMI_OPEN_DEFENDING_ACCURACY = 38;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 1944.

```text
VANCED_STAT_TYPE_SEMI_OPEN_ACCURACY = 36;
  ADVANCED_STAT_TYPE_SEMI_OPEN_ATTACKING_ACCURACY = 37;
  ADVANCED_STAT_TYPE_SEMI_OPEN_DEFENDING_ACCURACY = 38;
  ADVANCED_STAT_TYPE_SEMI_OPEN_SPACE_ADVANTAGE_ACCURACY = 39;
  ADVANCED_STAT_TYPE_SEMI_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 40;
  ADVANCED_STAT_TYPE_SEMI_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 41;
  ADVANCED_STAT_TYPE_CLOSED_ACCURACY = 42;
  ADVANCED_STAT_TYP
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08536"></a>
## FND-08536: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_SEMI_OPEN_SPACE_ADVANTAGE_ACCURACY = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_SEMI_OPEN_SPACE_ADVANTAGE_ACCURACY = 39;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2000.

```text
T_TYPE_SEMI_OPEN_ATTACKING_ACCURACY = 37;
  ADVANCED_STAT_TYPE_SEMI_OPEN_DEFENDING_ACCURACY = 38;
  ADVANCED_STAT_TYPE_SEMI_OPEN_SPACE_ADVANTAGE_ACCURACY = 39;
  ADVANCED_STAT_TYPE_SEMI_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 40;
  ADVANCED_STAT_TYPE_SEMI_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 41;
  ADVANCED_STAT_TYPE_CLOSED_ACCURACY = 42;
  ADVANCED_STAT_TYPE_CLOSED_ATTACKING_ACCURACY = 43;
  ADVANCED_STAT_TYPE_C
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08537"></a>
## FND-08537: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_SEMI_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_SEMI_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 40;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2062.

```text
_SEMI_OPEN_DEFENDING_ACCURACY = 38;
  ADVANCED_STAT_TYPE_SEMI_OPEN_SPACE_ADVANTAGE_ACCURACY = 39;
  ADVANCED_STAT_TYPE_SEMI_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 40;
  ADVANCED_STAT_TYPE_SEMI_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 41;
  ADVANCED_STAT_TYPE_CLOSED_ACCURACY = 42;
  ADVANCED_STAT_TYPE_CLOSED_ATTACKING_ACCURACY = 43;
  ADVANCED_STAT_TYPE_CLOSED_DEFENDING_ACCURACY = 44;
  ADVANCED_STAT_TYPE_CLOSED_SPA
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08538"></a>
## FND-08538: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_SEMI_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_SEMI_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 41;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2133.

```text
E_ADVANTAGE_ACCURACY = 39;
  ADVANCED_STAT_TYPE_SEMI_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 40;
  ADVANCED_STAT_TYPE_SEMI_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 41;
  ADVANCED_STAT_TYPE_CLOSED_ACCURACY = 42;
  ADVANCED_STAT_TYPE_CLOSED_ATTACKING_ACCURACY = 43;
  ADVANCED_STAT_TYPE_CLOSED_DEFENDING_ACCURACY = 44;
  ADVANCED_STAT_TYPE_CLOSED_SPACE_ADVANTAGE_ACCURACY = 45;
  ADVANCED_STAT_TYPE_CLOSED_PIECE_ACTIVITY_
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08539"></a>
## FND-08539: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_CLOSED_ACCURACY = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_CLOSED_ACCURACY = 42;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2204.

```text
Y_ADVANTAGE_ACCURACY = 40;
  ADVANCED_STAT_TYPE_SEMI_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 41;
  ADVANCED_STAT_TYPE_CLOSED_ACCURACY = 42;
  ADVANCED_STAT_TYPE_CLOSED_ATTACKING_ACCURACY = 43;
  ADVANCED_STAT_TYPE_CLOSED_DEFENDING_ACCURACY = 44;
  ADVANCED_STAT_TYPE_CLOSED_SPACE_ADVANTAGE_ACCURACY = 45;
  ADVANCED_STAT_TYPE_CLOSED_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 46;
  ADVANCED_STAT_TYPE_CLOSED_PAWN_STRUCTURE_ADV
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08540"></a>
## FND-08540: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_CLOSED_ATTACKING_ACCURACY = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_CLOSED_ATTACKING_ACCURACY = 43;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2247.

```text
TYPE_SEMI_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 41;
  ADVANCED_STAT_TYPE_CLOSED_ACCURACY = 42;
  ADVANCED_STAT_TYPE_CLOSED_ATTACKING_ACCURACY = 43;
  ADVANCED_STAT_TYPE_CLOSED_DEFENDING_ACCURACY = 44;
  ADVANCED_STAT_TYPE_CLOSED_SPACE_ADVANTAGE_ACCURACY = 45;
  ADVANCED_STAT_TYPE_CLOSED_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 46;
  ADVANCED_STAT_TYPE_CLOSED_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 47;
  ADVANCED_STAT_TYPE_
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08541"></a>
## FND-08541: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_CLOSED_DEFENDING_ACCURACY = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_CLOSED_DEFENDING_ACCURACY = 44;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2300.

```text
;
  ADVANCED_STAT_TYPE_CLOSED_ACCURACY = 42;
  ADVANCED_STAT_TYPE_CLOSED_ATTACKING_ACCURACY = 43;
  ADVANCED_STAT_TYPE_CLOSED_DEFENDING_ACCURACY = 44;
  ADVANCED_STAT_TYPE_CLOSED_SPACE_ADVANTAGE_ACCURACY = 45;
  ADVANCED_STAT_TYPE_CLOSED_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 46;
  ADVANCED_STAT_TYPE_CLOSED_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 47;
  ADVANCED_STAT_TYPE_ENDGAME_ACCURACY = 48;
  ADVANCED_STAT_TYPE_ENDGAME_W
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08542"></a>
## FND-08542: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_CLOSED_SPACE_ADVANTAGE_ACCURACY = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_CLOSED_SPACE_ADVANTAGE_ACCURACY = 45;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2353.

```text
ED_STAT_TYPE_CLOSED_ATTACKING_ACCURACY = 43;
  ADVANCED_STAT_TYPE_CLOSED_DEFENDING_ACCURACY = 44;
  ADVANCED_STAT_TYPE_CLOSED_SPACE_ADVANTAGE_ACCURACY = 45;
  ADVANCED_STAT_TYPE_CLOSED_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 46;
  ADVANCED_STAT_TYPE_CLOSED_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 47;
  ADVANCED_STAT_TYPE_ENDGAME_ACCURACY = 48;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_BETTER = 49;
  ADVANCED_STAT_TYPE_ENDGA
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08543"></a>
## FND-08543: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_CLOSED_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_CLOSED_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 46;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2412.

```text
T_TYPE_CLOSED_DEFENDING_ACCURACY = 44;
  ADVANCED_STAT_TYPE_CLOSED_SPACE_ADVANTAGE_ACCURACY = 45;
  ADVANCED_STAT_TYPE_CLOSED_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 46;
  ADVANCED_STAT_TYPE_CLOSED_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 47;
  ADVANCED_STAT_TYPE_ENDGAME_ACCURACY = 48;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_BETTER = 49;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_EQUAL = 50;
  ADVANCED_STAT_TYPE_ENDGAME_
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08544"></a>
## FND-08544: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_CLOSED_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_CLOSED_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 47;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2480.

```text
PACE_ADVANTAGE_ACCURACY = 45;
  ADVANCED_STAT_TYPE_CLOSED_PIECE_ACTIVITY_ADVANTAGE_ACCURACY = 46;
  ADVANCED_STAT_TYPE_CLOSED_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 47;
  ADVANCED_STAT_TYPE_ENDGAME_ACCURACY = 48;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_BETTER = 49;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_EQUAL = 50;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_WORSE = 51;
  ADVANCED_STAT_TYPE_KING_PAWN_ACCURACY =
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08545"></a>
## FND-08545: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ENDGAME_ACCURACY = 48

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ENDGAME_ACCURACY = 48;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2548.

```text
VITY_ADVANTAGE_ACCURACY = 46;
  ADVANCED_STAT_TYPE_CLOSED_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 47;
  ADVANCED_STAT_TYPE_ENDGAME_ACCURACY = 48;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_BETTER = 49;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_EQUAL = 50;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_WORSE = 51;
  ADVANCED_STAT_TYPE_KING_PAWN_ACCURACY = 52;
  ADVANCED_STAT_TYPE_ROOK_PAWN_ACCURACY = 53;
  ADVANCED_STAT_T
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08546"></a>
## FND-08546: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_BETTER = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_BETTER = 49;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2592.

```text
T_TYPE_CLOSED_PAWN_STRUCTURE_ADVANTAGE_ACCURACY = 47;
  ADVANCED_STAT_TYPE_ENDGAME_ACCURACY = 48;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_BETTER = 49;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_EQUAL = 50;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_WORSE = 51;
  ADVANCED_STAT_TYPE_KING_PAWN_ACCURACY = 52;
  ADVANCED_STAT_TYPE_ROOK_PAWN_ACCURACY = 53;
  ADVANCED_STAT_TYPE_QUEEN_ACCURACY = 54;
  ADVANCED_STAT_TYP
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08547"></a>
## FND-08547: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_EQUAL = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_EQUAL = 50;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2649.

```text
DVANCED_STAT_TYPE_ENDGAME_ACCURACY = 48;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_BETTER = 49;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_EQUAL = 50;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_WORSE = 51;
  ADVANCED_STAT_TYPE_KING_PAWN_ACCURACY = 52;
  ADVANCED_STAT_TYPE_ROOK_PAWN_ACCURACY = 53;
  ADVANCED_STAT_TYPE_QUEEN_ACCURACY = 54;
  ADVANCED_STAT_TYPE_OTHER_ACCURACY = 55;
  ADVANCED_STAT_TYPE_GOOD_KING_SAF
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08548"></a>
## FND-08548: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_WORSE = 51

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_WORSE = 51;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2705.

```text
_TYPE_ENDGAME_WIN_PERCENTAGE_BETTER = 49;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_EQUAL = 50;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_WORSE = 51;
  ADVANCED_STAT_TYPE_KING_PAWN_ACCURACY = 52;
  ADVANCED_STAT_TYPE_ROOK_PAWN_ACCURACY = 53;
  ADVANCED_STAT_TYPE_QUEEN_ACCURACY = 54;
  ADVANCED_STAT_TYPE_OTHER_ACCURACY = 55;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY_AND_CASTLING = 56;
  ADVANCED_STAT_TYPE_GOOD_DEVELOP
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08549"></a>
## FND-08549: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_KING_PAWN_ACCURACY = 52

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_KING_PAWN_ACCURACY = 52;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2761.

```text
T_TYPE_ENDGAME_WIN_PERCENTAGE_EQUAL = 50;
  ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_WORSE = 51;
  ADVANCED_STAT_TYPE_KING_PAWN_ACCURACY = 52;
  ADVANCED_STAT_TYPE_ROOK_PAWN_ACCURACY = 53;
  ADVANCED_STAT_TYPE_QUEEN_ACCURACY = 54;
  ADVANCED_STAT_TYPE_OTHER_ACCURACY = 55;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY_AND_CASTLING = 56;
  ADVANCED_STAT_TYPE_GOOD_DEVELOPMENT = 57;
  ADVANCED_STAT_TYPE_GOOD_CENTER_CONTROL = 58
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08550"></a>
## FND-08550: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_ROOK_PAWN_ACCURACY = 53

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_ROOK_PAWN_ACCURACY = 53;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2807.

```text
VANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_WORSE = 51;
  ADVANCED_STAT_TYPE_KING_PAWN_ACCURACY = 52;
  ADVANCED_STAT_TYPE_ROOK_PAWN_ACCURACY = 53;
  ADVANCED_STAT_TYPE_QUEEN_ACCURACY = 54;
  ADVANCED_STAT_TYPE_OTHER_ACCURACY = 55;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY_AND_CASTLING = 56;
  ADVANCED_STAT_TYPE_GOOD_DEVELOPMENT = 57;
  ADVANCED_STAT_TYPE_GOOD_CENTER_CONTROL = 58;
  ADVANCED_STAT_TYPE_BAD_KING_SAFETY_AND_CAS
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08551"></a>
## FND-08551: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_QUEEN_ACCURACY = 54

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_QUEEN_ACCURACY = 54;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2853.

```text
= 51;
  ADVANCED_STAT_TYPE_KING_PAWN_ACCURACY = 52;
  ADVANCED_STAT_TYPE_ROOK_PAWN_ACCURACY = 53;
  ADVANCED_STAT_TYPE_QUEEN_ACCURACY = 54;
  ADVANCED_STAT_TYPE_OTHER_ACCURACY = 55;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY_AND_CASTLING = 56;
  ADVANCED_STAT_TYPE_GOOD_DEVELOPMENT = 57;
  ADVANCED_STAT_TYPE_GOOD_CENTER_CONTROL = 58;
  ADVANCED_STAT_TYPE_BAD_KING_SAFETY_AND_CASTLING = 59;
  ADVANCED_STAT_TYPE_BAD_DEVELOPME
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08552"></a>
## FND-08552: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_OTHER_ACCURACY = 55

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_OTHER_ACCURACY = 55;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2895.

```text
ACY = 52;
  ADVANCED_STAT_TYPE_ROOK_PAWN_ACCURACY = 53;
  ADVANCED_STAT_TYPE_QUEEN_ACCURACY = 54;
  ADVANCED_STAT_TYPE_OTHER_ACCURACY = 55;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY_AND_CASTLING = 56;
  ADVANCED_STAT_TYPE_GOOD_DEVELOPMENT = 57;
  ADVANCED_STAT_TYPE_GOOD_CENTER_CONTROL = 58;
  ADVANCED_STAT_TYPE_BAD_KING_SAFETY_AND_CASTLING = 59;
  ADVANCED_STAT_TYPE_BAD_DEVELOPMENT = 60;
  ADVANCED_STAT_TYPE_BAD_CENTER_C
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08553"></a>
## FND-08553: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_KING_SAFETY_AND_CASTLING = 56

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_KING_SAFETY_AND_CASTLING = 56;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2937.

```text
CCURACY = 53;
  ADVANCED_STAT_TYPE_QUEEN_ACCURACY = 54;
  ADVANCED_STAT_TYPE_OTHER_ACCURACY = 55;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY_AND_CASTLING = 56;
  ADVANCED_STAT_TYPE_GOOD_DEVELOPMENT = 57;
  ADVANCED_STAT_TYPE_GOOD_CENTER_CONTROL = 58;
  ADVANCED_STAT_TYPE_BAD_KING_SAFETY_AND_CASTLING = 59;
  ADVANCED_STAT_TYPE_BAD_DEVELOPMENT = 60;
  ADVANCED_STAT_TYPE_BAD_CENTER_CONTROL = 61;
  ADVANCED_STAT_TYPE_GOOD_BAC
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08554"></a>
## FND-08554: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_DEVELOPMENT = 57

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_DEVELOPMENT = 57;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 2994.

```text
 ADVANCED_STAT_TYPE_OTHER_ACCURACY = 55;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY_AND_CASTLING = 56;
  ADVANCED_STAT_TYPE_GOOD_DEVELOPMENT = 57;
  ADVANCED_STAT_TYPE_GOOD_CENTER_CONTROL = 58;
  ADVANCED_STAT_TYPE_BAD_KING_SAFETY_AND_CASTLING = 59;
  ADVANCED_STAT_TYPE_BAD_DEVELOPMENT = 60;
  ADVANCED_STAT_TYPE_BAD_CENTER_CONTROL = 61;
  ADVANCED_STAT_TYPE_GOOD_BACKWARD_PAWNS = 62;
  ADVANCED_STAT_TYPE_GOOD_ISOLATED_PAWN
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08555"></a>
## FND-08555: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_CENTER_CONTROL = 58

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_CENTER_CONTROL = 58;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3038.

```text
DVANCED_STAT_TYPE_GOOD_KING_SAFETY_AND_CASTLING = 56;
  ADVANCED_STAT_TYPE_GOOD_DEVELOPMENT = 57;
  ADVANCED_STAT_TYPE_GOOD_CENTER_CONTROL = 58;
  ADVANCED_STAT_TYPE_BAD_KING_SAFETY_AND_CASTLING = 59;
  ADVANCED_STAT_TYPE_BAD_DEVELOPMENT = 60;
  ADVANCED_STAT_TYPE_BAD_CENTER_CONTROL = 61;
  ADVANCED_STAT_TYPE_GOOD_BACKWARD_PAWNS = 62;
  ADVANCED_STAT_TYPE_GOOD_ISOLATED_PAWNS = 63;
  ADVANCED_STAT_TYPE_GOOD_DOUBLED_PA
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08556"></a>
## FND-08556: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_BAD_KING_SAFETY_AND_CASTLING = 59

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_BAD_KING_SAFETY_AND_CASTLING = 59;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3085.

```text
 = 56;
  ADVANCED_STAT_TYPE_GOOD_DEVELOPMENT = 57;
  ADVANCED_STAT_TYPE_GOOD_CENTER_CONTROL = 58;
  ADVANCED_STAT_TYPE_BAD_KING_SAFETY_AND_CASTLING = 59;
  ADVANCED_STAT_TYPE_BAD_DEVELOPMENT = 60;
  ADVANCED_STAT_TYPE_BAD_CENTER_CONTROL = 61;
  ADVANCED_STAT_TYPE_GOOD_BACKWARD_PAWNS = 62;
  ADVANCED_STAT_TYPE_GOOD_ISOLATED_PAWNS = 63;
  ADVANCED_STAT_TYPE_GOOD_DOUBLED_PAWNS = 64;
  ADVANCED_STAT_TYPE_GOOD_PAWN_CHAINS
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08557"></a>
## FND-08557: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_BAD_DEVELOPMENT = 60

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_BAD_DEVELOPMENT = 60;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3141.

```text
ANCED_STAT_TYPE_GOOD_CENTER_CONTROL = 58;
  ADVANCED_STAT_TYPE_BAD_KING_SAFETY_AND_CASTLING = 59;
  ADVANCED_STAT_TYPE_BAD_DEVELOPMENT = 60;
  ADVANCED_STAT_TYPE_BAD_CENTER_CONTROL = 61;
  ADVANCED_STAT_TYPE_GOOD_BACKWARD_PAWNS = 62;
  ADVANCED_STAT_TYPE_GOOD_ISOLATED_PAWNS = 63;
  ADVANCED_STAT_TYPE_GOOD_DOUBLED_PAWNS = 64;
  ADVANCED_STAT_TYPE_GOOD_PAWN_CHAINS = 65;
  ADVANCED_STAT_TYPE_GOOD_PASSED_PAWNS = 66;
  AD
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08558"></a>
## FND-08558: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_BAD_CENTER_CONTROL = 61

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_BAD_CENTER_CONTROL = 61;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3184.

```text
 ADVANCED_STAT_TYPE_BAD_KING_SAFETY_AND_CASTLING = 59;
  ADVANCED_STAT_TYPE_BAD_DEVELOPMENT = 60;
  ADVANCED_STAT_TYPE_BAD_CENTER_CONTROL = 61;
  ADVANCED_STAT_TYPE_GOOD_BACKWARD_PAWNS = 62;
  ADVANCED_STAT_TYPE_GOOD_ISOLATED_PAWNS = 63;
  ADVANCED_STAT_TYPE_GOOD_DOUBLED_PAWNS = 64;
  ADVANCED_STAT_TYPE_GOOD_PAWN_CHAINS = 65;
  ADVANCED_STAT_TYPE_GOOD_PASSED_PAWNS = 66;
  ADVANCED_STAT_TYPE_GOOD_OUTPOSTS = 67;
  ADVA
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08559"></a>
## FND-08559: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_BACKWARD_PAWNS = 62

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_BACKWARD_PAWNS = 62;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3230.

```text
NG = 59;
  ADVANCED_STAT_TYPE_BAD_DEVELOPMENT = 60;
  ADVANCED_STAT_TYPE_BAD_CENTER_CONTROL = 61;
  ADVANCED_STAT_TYPE_GOOD_BACKWARD_PAWNS = 62;
  ADVANCED_STAT_TYPE_GOOD_ISOLATED_PAWNS = 63;
  ADVANCED_STAT_TYPE_GOOD_DOUBLED_PAWNS = 64;
  ADVANCED_STAT_TYPE_GOOD_PAWN_CHAINS = 65;
  ADVANCED_STAT_TYPE_GOOD_PASSED_PAWNS = 66;
  ADVANCED_STAT_TYPE_GOOD_OUTPOSTS = 67;
  ADVANCED_STAT_TYPE_GOOD_OPEN_FILES = 68;
  ADVANCE
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08560"></a>
## FND-08560: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_ISOLATED_PAWNS = 63

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_ISOLATED_PAWNS = 63;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3277.

```text
 60;
  ADVANCED_STAT_TYPE_BAD_CENTER_CONTROL = 61;
  ADVANCED_STAT_TYPE_GOOD_BACKWARD_PAWNS = 62;
  ADVANCED_STAT_TYPE_GOOD_ISOLATED_PAWNS = 63;
  ADVANCED_STAT_TYPE_GOOD_DOUBLED_PAWNS = 64;
  ADVANCED_STAT_TYPE_GOOD_PAWN_CHAINS = 65;
  ADVANCED_STAT_TYPE_GOOD_PASSED_PAWNS = 66;
  ADVANCED_STAT_TYPE_GOOD_OUTPOSTS = 67;
  ADVANCED_STAT_TYPE_GOOD_OPEN_FILES = 68;
  ADVANCED_STAT_TYPE_GOOD_PIECE_ACTIVITY = 69;
  ADVANCE
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08561"></a>
## FND-08561: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_DOUBLED_PAWNS = 64

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_DOUBLED_PAWNS = 64;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3324.

```text
61;
  ADVANCED_STAT_TYPE_GOOD_BACKWARD_PAWNS = 62;
  ADVANCED_STAT_TYPE_GOOD_ISOLATED_PAWNS = 63;
  ADVANCED_STAT_TYPE_GOOD_DOUBLED_PAWNS = 64;
  ADVANCED_STAT_TYPE_GOOD_PAWN_CHAINS = 65;
  ADVANCED_STAT_TYPE_GOOD_PASSED_PAWNS = 66;
  ADVANCED_STAT_TYPE_GOOD_OUTPOSTS = 67;
  ADVANCED_STAT_TYPE_GOOD_OPEN_FILES = 68;
  ADVANCED_STAT_TYPE_GOOD_PIECE_ACTIVITY = 69;
  ADVANCED_STAT_TYPE_GOOD_BLOCKADES = 70;
  ADVANCED_STA
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08562"></a>
## FND-08562: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_PAWN_CHAINS = 65

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_PAWN_CHAINS = 65;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3370.

```text
 62;
  ADVANCED_STAT_TYPE_GOOD_ISOLATED_PAWNS = 63;
  ADVANCED_STAT_TYPE_GOOD_DOUBLED_PAWNS = 64;
  ADVANCED_STAT_TYPE_GOOD_PAWN_CHAINS = 65;
  ADVANCED_STAT_TYPE_GOOD_PASSED_PAWNS = 66;
  ADVANCED_STAT_TYPE_GOOD_OUTPOSTS = 67;
  ADVANCED_STAT_TYPE_GOOD_OPEN_FILES = 68;
  ADVANCED_STAT_TYPE_GOOD_PIECE_ACTIVITY = 69;
  ADVANCED_STAT_TYPE_GOOD_BLOCKADES = 70;
  ADVANCED_STAT_TYPE_GOOD_TRADES = 71;
  ADVANCED_STAT_TYPE_
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08563"></a>
## FND-08563: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_PASSED_PAWNS = 66

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_PASSED_PAWNS = 66;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3414.

```text
S = 63;
  ADVANCED_STAT_TYPE_GOOD_DOUBLED_PAWNS = 64;
  ADVANCED_STAT_TYPE_GOOD_PAWN_CHAINS = 65;
  ADVANCED_STAT_TYPE_GOOD_PASSED_PAWNS = 66;
  ADVANCED_STAT_TYPE_GOOD_OUTPOSTS = 67;
  ADVANCED_STAT_TYPE_GOOD_OPEN_FILES = 68;
  ADVANCED_STAT_TYPE_GOOD_PIECE_ACTIVITY = 69;
  ADVANCED_STAT_TYPE_GOOD_BLOCKADES = 70;
  ADVANCED_STAT_TYPE_GOOD_TRADES = 71;
  ADVANCED_STAT_TYPE_GOOD_SPACE = 72;
  ADVANCED_STAT_TYPE_GOOD_O
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08564"></a>
## FND-08564: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_OUTPOSTS = 67

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_OUTPOSTS = 67;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3459.

```text
NS = 64;
  ADVANCED_STAT_TYPE_GOOD_PAWN_CHAINS = 65;
  ADVANCED_STAT_TYPE_GOOD_PASSED_PAWNS = 66;
  ADVANCED_STAT_TYPE_GOOD_OUTPOSTS = 67;
  ADVANCED_STAT_TYPE_GOOD_OPEN_FILES = 68;
  ADVANCED_STAT_TYPE_GOOD_PIECE_ACTIVITY = 69;
  ADVANCED_STAT_TYPE_GOOD_BLOCKADES = 70;
  ADVANCED_STAT_TYPE_GOOD_TRADES = 71;
  ADVANCED_STAT_TYPE_GOOD_SPACE = 72;
  ADVANCED_STAT_TYPE_GOOD_OCCUPYING_CENTER = 73;
  ADVANCED_STAT_TYPE_GO
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08565"></a>
## FND-08565: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_OPEN_FILES = 68

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_OPEN_FILES = 68;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3500.

```text
HAINS = 65;
  ADVANCED_STAT_TYPE_GOOD_PASSED_PAWNS = 66;
  ADVANCED_STAT_TYPE_GOOD_OUTPOSTS = 67;
  ADVANCED_STAT_TYPE_GOOD_OPEN_FILES = 68;
  ADVANCED_STAT_TYPE_GOOD_PIECE_ACTIVITY = 69;
  ADVANCED_STAT_TYPE_GOOD_BLOCKADES = 70;
  ADVANCED_STAT_TYPE_GOOD_TRADES = 71;
  ADVANCED_STAT_TYPE_GOOD_SPACE = 72;
  ADVANCED_STAT_TYPE_GOOD_OCCUPYING_CENTER = 73;
  ADVANCED_STAT_TYPE_GOOD_CENTRAL_BREAKS = 74;
  ADVANCED_STAT_T
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08566"></a>
## FND-08566: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_PIECE_ACTIVITY = 69

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_PIECE_ACTIVITY = 69;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3543.

```text
D_PAWNS = 66;
  ADVANCED_STAT_TYPE_GOOD_OUTPOSTS = 67;
  ADVANCED_STAT_TYPE_GOOD_OPEN_FILES = 68;
  ADVANCED_STAT_TYPE_GOOD_PIECE_ACTIVITY = 69;
  ADVANCED_STAT_TYPE_GOOD_BLOCKADES = 70;
  ADVANCED_STAT_TYPE_GOOD_TRADES = 71;
  ADVANCED_STAT_TYPE_GOOD_SPACE = 72;
  ADVANCED_STAT_TYPE_GOOD_OCCUPYING_CENTER = 73;
  ADVANCED_STAT_TYPE_GOOD_CENTRAL_BREAKS = 74;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY = 75;
  ADVANCED_STAT_
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08567"></a>
## FND-08567: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_BLOCKADES = 70

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_BLOCKADES = 70;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3590.

```text
S = 67;
  ADVANCED_STAT_TYPE_GOOD_OPEN_FILES = 68;
  ADVANCED_STAT_TYPE_GOOD_PIECE_ACTIVITY = 69;
  ADVANCED_STAT_TYPE_GOOD_BLOCKADES = 70;
  ADVANCED_STAT_TYPE_GOOD_TRADES = 71;
  ADVANCED_STAT_TYPE_GOOD_SPACE = 72;
  ADVANCED_STAT_TYPE_GOOD_OCCUPYING_CENTER = 73;
  ADVANCED_STAT_TYPE_GOOD_CENTRAL_BREAKS = 74;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY = 75;
  ADVANCED_STAT_TYPE_BAD_BACKWARD_PAWNS = 76;
  ADVANCED_STAT_T
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08568"></a>
## FND-08568: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_TRADES = 71

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_TRADES = 71;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3632.

```text
ES = 68;
  ADVANCED_STAT_TYPE_GOOD_PIECE_ACTIVITY = 69;
  ADVANCED_STAT_TYPE_GOOD_BLOCKADES = 70;
  ADVANCED_STAT_TYPE_GOOD_TRADES = 71;
  ADVANCED_STAT_TYPE_GOOD_SPACE = 72;
  ADVANCED_STAT_TYPE_GOOD_OCCUPYING_CENTER = 73;
  ADVANCED_STAT_TYPE_GOOD_CENTRAL_BREAKS = 74;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY = 75;
  ADVANCED_STAT_TYPE_BAD_BACKWARD_PAWNS = 76;
  ADVANCED_STAT_TYPE_BAD_ISOLATED_PAWNS = 77;
  ADVANCED_ST
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08569"></a>
## FND-08569: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_SPACE = 72

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_SPACE = 72;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3671.

```text
E_ACTIVITY = 69;
  ADVANCED_STAT_TYPE_GOOD_BLOCKADES = 70;
  ADVANCED_STAT_TYPE_GOOD_TRADES = 71;
  ADVANCED_STAT_TYPE_GOOD_SPACE = 72;
  ADVANCED_STAT_TYPE_GOOD_OCCUPYING_CENTER = 73;
  ADVANCED_STAT_TYPE_GOOD_CENTRAL_BREAKS = 74;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY = 75;
  ADVANCED_STAT_TYPE_BAD_BACKWARD_PAWNS = 76;
  ADVANCED_STAT_TYPE_BAD_ISOLATED_PAWNS = 77;
  ADVANCED_STAT_TYPE_BAD_DOUBLED_PAWNS = 78;
  ADVAN
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08570"></a>
## FND-08570: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_OCCUPYING_CENTER = 73

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_OCCUPYING_CENTER = 73;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3709.

```text
GOOD_BLOCKADES = 70;
  ADVANCED_STAT_TYPE_GOOD_TRADES = 71;
  ADVANCED_STAT_TYPE_GOOD_SPACE = 72;
  ADVANCED_STAT_TYPE_GOOD_OCCUPYING_CENTER = 73;
  ADVANCED_STAT_TYPE_GOOD_CENTRAL_BREAKS = 74;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY = 75;
  ADVANCED_STAT_TYPE_BAD_BACKWARD_PAWNS = 76;
  ADVANCED_STAT_TYPE_BAD_ISOLATED_PAWNS = 77;
  ADVANCED_STAT_TYPE_BAD_DOUBLED_PAWNS = 78;
  ADVANCED_STAT_TYPE_BAD_PAWN_CHAINS = 79;
  
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08571"></a>
## FND-08571: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_CENTRAL_BREAKS = 74

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_CENTRAL_BREAKS = 74;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3758.

```text
ADES = 71;
  ADVANCED_STAT_TYPE_GOOD_SPACE = 72;
  ADVANCED_STAT_TYPE_GOOD_OCCUPYING_CENTER = 73;
  ADVANCED_STAT_TYPE_GOOD_CENTRAL_BREAKS = 74;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY = 75;
  ADVANCED_STAT_TYPE_BAD_BACKWARD_PAWNS = 76;
  ADVANCED_STAT_TYPE_BAD_ISOLATED_PAWNS = 77;
  ADVANCED_STAT_TYPE_BAD_DOUBLED_PAWNS = 78;
  ADVANCED_STAT_TYPE_BAD_PAWN_CHAINS = 79;
  ADVANCED_STAT_TYPE_BAD_PASSED_PAWNS = 80;
  ADVAN
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08572"></a>
## FND-08572: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_GOOD_KING_SAFETY = 75

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_GOOD_KING_SAFETY = 75;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3805.

```text
;
  ADVANCED_STAT_TYPE_GOOD_OCCUPYING_CENTER = 73;
  ADVANCED_STAT_TYPE_GOOD_CENTRAL_BREAKS = 74;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY = 75;
  ADVANCED_STAT_TYPE_BAD_BACKWARD_PAWNS = 76;
  ADVANCED_STAT_TYPE_BAD_ISOLATED_PAWNS = 77;
  ADVANCED_STAT_TYPE_BAD_DOUBLED_PAWNS = 78;
  ADVANCED_STAT_TYPE_BAD_PAWN_CHAINS = 79;
  ADVANCED_STAT_TYPE_BAD_PASSED_PAWNS = 80;
  ADVANCED_STAT_TYPE_BAD_OUTPOSTS = 81;
  ADVANCED_STA
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08573"></a>
## FND-08573: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_BAD_BACKWARD_PAWNS = 76

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_BAD_BACKWARD_PAWNS = 76;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3849.

```text
 = 73;
  ADVANCED_STAT_TYPE_GOOD_CENTRAL_BREAKS = 74;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY = 75;
  ADVANCED_STAT_TYPE_BAD_BACKWARD_PAWNS = 76;
  ADVANCED_STAT_TYPE_BAD_ISOLATED_PAWNS = 77;
  ADVANCED_STAT_TYPE_BAD_DOUBLED_PAWNS = 78;
  ADVANCED_STAT_TYPE_BAD_PAWN_CHAINS = 79;
  ADVANCED_STAT_TYPE_BAD_PASSED_PAWNS = 80;
  ADVANCED_STAT_TYPE_BAD_OUTPOSTS = 81;
  ADVANCED_STAT_TYPE_BAD_OPEN_FILES = 82;
  ADVANCED_STAT_
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08574"></a>
## FND-08574: chesscom.stats.v1.AdvancedStatType.ADVANCED_STAT_TYPE_BAD_ISOLATED_PAWNS = 77

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_TYPE_BAD_ISOLATED_PAWNS = 77;

### Evidence

- **SRC-0562** `research/proto/chesscom/stats/v1/advanced_stat_type.proto` — [preserved redacted evidence](../evidence/text/e73630d18abd75920a931ead145dfc328edf5581ec8a8399062104e176d7a585.proto)
  Character offset 3895.

```text
S = 74;
  ADVANCED_STAT_TYPE_GOOD_KING_SAFETY = 75;
  ADVANCED_STAT_TYPE_BAD_BACKWARD_PAWNS = 76;
  ADVANCED_STAT_TYPE_BAD_ISOLATED_PAWNS = 77;
  ADVANCED_STAT_TYPE_BAD_DOUBLED_PAWNS = 78;
  ADVANCED_STAT_TYPE_BAD_PAWN_CHAINS = 79;
  ADVANCED_STAT_TYPE_BAD_PASSED_PAWNS = 80;
  ADVANCED_STAT_TYPE_BAD_OUTPOSTS = 81;
  ADVANCED_STAT_TYPE_BAD_OPEN_FILES = 82;
  ADVANCED_STAT_TYPE_BAD_PIECE_ACTIVITY = 83;
  ADVANCED_STAT_
```

**Source references:** SRC-0562, SRC-1533  
**URL references:** None independently associated  
**Related findings:** FND-08496, FND-08497, FND-08498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
