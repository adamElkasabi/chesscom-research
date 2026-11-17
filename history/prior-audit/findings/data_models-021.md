# data_models — findings 2001–2100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-02275"></a>
## FND-02275: enum declaration: chesscom.courses.v1.ProductListRetrieveMode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ProductListRetrieveMode {

### Evidence

- **SRC-0303** `research/proto/chesscom/courses/v1/product_list_retrieve_mode.proto` — [preserved redacted evidence](../evidence/text/062de58cf4f4b7771e9a2436c19eff78190a098c478738fe4f9e033bd49a09a3.proto)
  Character offset 113.

```text
esscom/courses/v1/product_list_retrieve_mode.proto
// syntax: proto3

package chesscom.courses.v1;

enum ProductListRetrieveMode {
  PRODUCT_LIST_RETRIEVE_MODE_UNSPECIFIED = 0;
  PRODUCT_LIST_RETRIEVE_MODE_ALL = 1;
  PRODUCT_LIST_RETRIEVE_MODE_PRODUCT_COUNT = 2;
}

```

**Source references:** SRC-0303, SRC-1274  
**URL references:** None independently associated  
**Related findings:** FND-02276, FND-02277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02276"></a>
## FND-02276: chesscom.courses.v1.ProductListRetrieveMode.PRODUCT_LIST_RETRIEVE_MODE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_LIST_RETRIEVE_MODE_UNSPECIFIED = 0;

### Evidence

- **SRC-0303** `research/proto/chesscom/courses/v1/product_list_retrieve_mode.proto` — [preserved redacted evidence](../evidence/text/062de58cf4f4b7771e9a2436c19eff78190a098c478738fe4f9e033bd49a09a3.proto)
  Character offset 146.

```text
trieve_mode.proto
// syntax: proto3

package chesscom.courses.v1;

enum ProductListRetrieveMode {
  PRODUCT_LIST_RETRIEVE_MODE_UNSPECIFIED = 0;
  PRODUCT_LIST_RETRIEVE_MODE_ALL = 1;
  PRODUCT_LIST_RETRIEVE_MODE_PRODUCT_COUNT = 2;
}

```

**Source references:** SRC-0303, SRC-1274  
**URL references:** None independently associated  
**Related findings:** FND-02275, FND-02277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02277"></a>
## FND-02277: chesscom.courses.v1.ProductListRetrieveMode.PRODUCT_LIST_RETRIEVE_MODE_ALL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_LIST_RETRIEVE_MODE_ALL = 1;

### Evidence

- **SRC-0303** `research/proto/chesscom/courses/v1/product_list_retrieve_mode.proto` — [preserved redacted evidence](../evidence/text/062de58cf4f4b7771e9a2436c19eff78190a098c478738fe4f9e033bd49a09a3.proto)
  Character offset 192.

```text
hesscom.courses.v1;

enum ProductListRetrieveMode {
  PRODUCT_LIST_RETRIEVE_MODE_UNSPECIFIED = 0;
  PRODUCT_LIST_RETRIEVE_MODE_ALL = 1;
  PRODUCT_LIST_RETRIEVE_MODE_PRODUCT_COUNT = 2;
}

```

**Source references:** SRC-0303, SRC-1274  
**URL references:** None independently associated  
**Related findings:** FND-02275, FND-02276

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02278"></a>
## FND-02278: chesscom.courses.v1.ProductListRetrieveMode.PRODUCT_LIST_RETRIEVE_MODE_PRODUCT_COUNT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_LIST_RETRIEVE_MODE_PRODUCT_COUNT = 2;

### Evidence

- **SRC-0303** `research/proto/chesscom/courses/v1/product_list_retrieve_mode.proto` — [preserved redacted evidence](../evidence/text/062de58cf4f4b7771e9a2436c19eff78190a098c478738fe4f9e033bd49a09a3.proto)
  Character offset 230.

```text
etrieveMode {
  PRODUCT_LIST_RETRIEVE_MODE_UNSPECIFIED = 0;
  PRODUCT_LIST_RETRIEVE_MODE_ALL = 1;
  PRODUCT_LIST_RETRIEVE_MODE_PRODUCT_COUNT = 2;
}

```

**Source references:** SRC-0303, SRC-1274  
**URL references:** None independently associated  
**Related findings:** FND-02275, FND-02276, FND-02277

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02279"></a>
## FND-02279: enum declaration: chesscom.courses.v1.RewardType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum RewardType {

### Evidence

- **SRC-0304** `research/proto/chesscom/courses/v1/reward.proto` — [preserved redacted evidence](../evidence/text/eb48930c4511e577a3800293521ab1948fb41c432e67c27eafe0fca40ef85ac1.proto)
  Character offset 93.

```text
// source: chesscom/courses/v1/reward.proto
// syntax: proto3

package chesscom.courses.v1;

enum RewardType {
  REWARD_TYPE_UNSPECIFIED = 0;
  REWARD_TYPE_ANY_DIAMOND_COURSE = 1;
  REWARD_TYPE_PAID_COURSE = 2;
}

message Reward {
  oneof _value {
  string value = 2;
  }
  optional .chesscom.courses.v1.RewardType type = 1;
}

```

**Source references:** SRC-0304, SRC-1275  
**URL references:** None independently associated  
**Related findings:** FND-02280, FND-02281

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02280"></a>
## FND-02280: chesscom.courses.v1.RewardType.REWARD_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

REWARD_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0304** `research/proto/chesscom/courses/v1/reward.proto` — [preserved redacted evidence](../evidence/text/eb48930c4511e577a3800293521ab1948fb41c432e67c27eafe0fca40ef85ac1.proto)
  Character offset 113.

```text
esscom/courses/v1/reward.proto
// syntax: proto3

package chesscom.courses.v1;

enum RewardType {
  REWARD_TYPE_UNSPECIFIED = 0;
  REWARD_TYPE_ANY_DIAMOND_COURSE = 1;
  REWARD_TYPE_PAID_COURSE = 2;
}

message Reward {
  oneof _value {
  string value = 2;
  }
  optional .chesscom.courses.v1.RewardType type = 1;
}

```

**Source references:** SRC-0304, SRC-1275  
**URL references:** None independently associated  
**Related findings:** FND-02279, FND-02281

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02281"></a>
## FND-02281: chesscom.courses.v1.RewardType.REWARD_TYPE_ANY_DIAMOND_COURSE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

REWARD_TYPE_ANY_DIAMOND_COURSE = 1;

### Evidence

- **SRC-0304** `research/proto/chesscom/courses/v1/reward.proto` — [preserved redacted evidence](../evidence/text/eb48930c4511e577a3800293521ab1948fb41c432e67c27eafe0fca40ef85ac1.proto)
  Character offset 144.

```text
// syntax: proto3

package chesscom.courses.v1;

enum RewardType {
  REWARD_TYPE_UNSPECIFIED = 0;
  REWARD_TYPE_ANY_DIAMOND_COURSE = 1;
  REWARD_TYPE_PAID_COURSE = 2;
}

message Reward {
  oneof _value {
  string value = 2;
  }
  optional .chesscom.courses.v1.RewardType type = 1;
}

```

**Source references:** SRC-0304, SRC-1275  
**URL references:** None independently associated  
**Related findings:** FND-02279, FND-02280

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02282"></a>
## FND-02282: chesscom.courses.v1.RewardType.REWARD_TYPE_PAID_COURSE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

REWARD_TYPE_PAID_COURSE = 2;

### Evidence

- **SRC-0304** `research/proto/chesscom/courses/v1/reward.proto` — [preserved redacted evidence](../evidence/text/eb48930c4511e577a3800293521ab1948fb41c432e67c27eafe0fca40ef85ac1.proto)
  Character offset 182.

```text
urses.v1;

enum RewardType {
  REWARD_TYPE_UNSPECIFIED = 0;
  REWARD_TYPE_ANY_DIAMOND_COURSE = 1;
  REWARD_TYPE_PAID_COURSE = 2;
}

message Reward {
  oneof _value {
  string value = 2;
  }
  optional .chesscom.courses.v1.RewardType type = 1;
}

```

**Source references:** SRC-0304, SRC-1275  
**URL references:** None independently associated  
**Related findings:** FND-02279, FND-02280, FND-02281

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02283"></a>
## FND-02283: message declaration: chesscom.courses.v1.Reward

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Reward {

### Evidence

- **SRC-0304** `research/proto/chesscom/courses/v1/reward.proto` — [preserved redacted evidence](../evidence/text/eb48930c4511e577a3800293521ab1948fb41c432e67c27eafe0fca40ef85ac1.proto)
  Character offset 214.

```text
EWARD_TYPE_UNSPECIFIED = 0;
  REWARD_TYPE_ANY_DIAMOND_COURSE = 1;
  REWARD_TYPE_PAID_COURSE = 2;
}

message Reward {
  oneof _value {
  string value = 2;
  }
  optional .chesscom.courses.v1.RewardType type = 1;
}

```

**Source references:** SRC-0304, SRC-1275  
**URL references:** None independently associated  
**Related findings:** FND-02279, FND-02280, FND-02281

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02284"></a>
## FND-02284: oneof declaration: chesscom.courses.v1.Reward._value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _value {

### Evidence

- **SRC-0304** `research/proto/chesscom/courses/v1/reward.proto` — [preserved redacted evidence](../evidence/text/eb48930c4511e577a3800293521ab1948fb41c432e67c27eafe0fca40ef85ac1.proto)
  Character offset 233.

```text
IED = 0;
  REWARD_TYPE_ANY_DIAMOND_COURSE = 1;
  REWARD_TYPE_PAID_COURSE = 2;
}

message Reward {
  oneof _value {
  string value = 2;
  }
  optional .chesscom.courses.v1.RewardType type = 1;
}

```

**Source references:** SRC-0304, SRC-1275  
**URL references:** None independently associated  
**Related findings:** FND-02279, FND-02280, FND-02281

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02285"></a>
## FND-02285: chesscom.courses.v1.Reward.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string value = 2;

### Evidence

- **SRC-0304** `research/proto/chesscom/courses/v1/reward.proto` — [preserved redacted evidence](../evidence/text/eb48930c4511e577a3800293521ab1948fb41c432e67c27eafe0fca40ef85ac1.proto)
  Character offset 250.

```text
_TYPE_ANY_DIAMOND_COURSE = 1;
  REWARD_TYPE_PAID_COURSE = 2;
}

message Reward {
  oneof _value {
  string value = 2;
  }
  optional .chesscom.courses.v1.RewardType type = 1;
}

```

**Source references:** SRC-0304, SRC-1275  
**URL references:** None independently associated  
**Related findings:** FND-02279, FND-02280, FND-02281

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02286"></a>
## FND-02286: chesscom.courses.v1.Reward.type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.RewardType type = 1;

### Evidence

- **SRC-0304** `research/proto/chesscom/courses/v1/reward.proto` — [preserved redacted evidence](../evidence/text/eb48930c4511e577a3800293521ab1948fb41c432e67c27eafe0fca40ef85ac1.proto)
  Character offset 274.

```text
 = 1;
  REWARD_TYPE_PAID_COURSE = 2;
}

message Reward {
  oneof _value {
  string value = 2;
  }
  optional .chesscom.courses.v1.RewardType type = 1;
}

```

**Source references:** SRC-0304, SRC-1275  
**URL references:** None independently associated  
**Related findings:** FND-02279, FND-02280, FND-02281

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02287"></a>
## FND-02287: enum declaration: chesscom.courses.v1.ShopSortOption

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ShopSortOption {

### Evidence

- **SRC-0305** `research/proto/chesscom/courses/v1/shop_sort_option.proto` — [preserved redacted evidence](../evidence/text/aaec68f6b8156906c4421cafb27d63ec276e12c5c67cef2eb9fa9fc43f445805.proto)
  Character offset 103.

```text
source: chesscom/courses/v1/shop_sort_option.proto
// syntax: proto3

package chesscom.courses.v1;

enum ShopSortOption {
  SHOP_SORT_OPTION_UNSPECIFIED = 0;
  SHOP_SORT_OPTION_PRICE_ASC = 1;
  SHOP_SORT_OPTION_PRICE_DESC = 2;
  SHOP_SORT_OPTION_VARIATIONS_DESC = 3;
  SHOP_SORT_OPTION_RELEASE_DATE_DESC = 4;
}

```

**Source references:** SRC-0305, SRC-1276  
**URL references:** None independently associated  
**Related findings:** FND-02288, FND-02289

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02288"></a>
## FND-02288: chesscom.courses.v1.ShopSortOption.SHOP_SORT_OPTION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHOP_SORT_OPTION_UNSPECIFIED = 0;

### Evidence

- **SRC-0305** `research/proto/chesscom/courses/v1/shop_sort_option.proto` — [preserved redacted evidence](../evidence/text/aaec68f6b8156906c4421cafb27d63ec276e12c5c67cef2eb9fa9fc43f445805.proto)
  Character offset 127.

```text
/v1/shop_sort_option.proto
// syntax: proto3

package chesscom.courses.v1;

enum ShopSortOption {
  SHOP_SORT_OPTION_UNSPECIFIED = 0;
  SHOP_SORT_OPTION_PRICE_ASC = 1;
  SHOP_SORT_OPTION_PRICE_DESC = 2;
  SHOP_SORT_OPTION_VARIATIONS_DESC = 3;
  SHOP_SORT_OPTION_RELEASE_DATE_DESC = 4;
}

```

**Source references:** SRC-0305, SRC-1276  
**URL references:** None independently associated  
**Related findings:** FND-02287, FND-02289

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02289"></a>
## FND-02289: chesscom.courses.v1.ShopSortOption.SHOP_SORT_OPTION_PRICE_ASC = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHOP_SORT_OPTION_PRICE_ASC = 1;

### Evidence

- **SRC-0305** `research/proto/chesscom/courses/v1/shop_sort_option.proto` — [preserved redacted evidence](../evidence/text/aaec68f6b8156906c4421cafb27d63ec276e12c5c67cef2eb9fa9fc43f445805.proto)
  Character offset 163.

```text
: proto3

package chesscom.courses.v1;

enum ShopSortOption {
  SHOP_SORT_OPTION_UNSPECIFIED = 0;
  SHOP_SORT_OPTION_PRICE_ASC = 1;
  SHOP_SORT_OPTION_PRICE_DESC = 2;
  SHOP_SORT_OPTION_VARIATIONS_DESC = 3;
  SHOP_SORT_OPTION_RELEASE_DATE_DESC = 4;
}

```

**Source references:** SRC-0305, SRC-1276  
**URL references:** None independently associated  
**Related findings:** FND-02287, FND-02288

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02290"></a>
## FND-02290: chesscom.courses.v1.ShopSortOption.SHOP_SORT_OPTION_PRICE_DESC = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHOP_SORT_OPTION_PRICE_DESC = 2;

### Evidence

- **SRC-0305** `research/proto/chesscom/courses/v1/shop_sort_option.proto` — [preserved redacted evidence](../evidence/text/aaec68f6b8156906c4421cafb27d63ec276e12c5c67cef2eb9fa9fc43f445805.proto)
  Character offset 197.

```text
.v1;

enum ShopSortOption {
  SHOP_SORT_OPTION_UNSPECIFIED = 0;
  SHOP_SORT_OPTION_PRICE_ASC = 1;
  SHOP_SORT_OPTION_PRICE_DESC = 2;
  SHOP_SORT_OPTION_VARIATIONS_DESC = 3;
  SHOP_SORT_OPTION_RELEASE_DATE_DESC = 4;
}

```

**Source references:** SRC-0305, SRC-1276  
**URL references:** None independently associated  
**Related findings:** FND-02287, FND-02288, FND-02289

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02291"></a>
## FND-02291: chesscom.courses.v1.ShopSortOption.SHOP_SORT_OPTION_VARIATIONS_DESC = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHOP_SORT_OPTION_VARIATIONS_DESC = 3;

### Evidence

- **SRC-0305** `research/proto/chesscom/courses/v1/shop_sort_option.proto` — [preserved redacted evidence](../evidence/text/aaec68f6b8156906c4421cafb27d63ec276e12c5c67cef2eb9fa9fc43f445805.proto)
  Character offset 232.

```text
SORT_OPTION_UNSPECIFIED = 0;
  SHOP_SORT_OPTION_PRICE_ASC = 1;
  SHOP_SORT_OPTION_PRICE_DESC = 2;
  SHOP_SORT_OPTION_VARIATIONS_DESC = 3;
  SHOP_SORT_OPTION_RELEASE_DATE_DESC = 4;
}

```

**Source references:** SRC-0305, SRC-1276  
**URL references:** None independently associated  
**Related findings:** FND-02287, FND-02288, FND-02289

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02292"></a>
## FND-02292: chesscom.courses.v1.ShopSortOption.SHOP_SORT_OPTION_RELEASE_DATE_DESC = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHOP_SORT_OPTION_RELEASE_DATE_DESC = 4;

### Evidence

- **SRC-0305** `research/proto/chesscom/courses/v1/shop_sort_option.proto` — [preserved redacted evidence](../evidence/text/aaec68f6b8156906c4421cafb27d63ec276e12c5c67cef2eb9fa9fc43f445805.proto)
  Character offset 272.

```text
_OPTION_PRICE_ASC = 1;
  SHOP_SORT_OPTION_PRICE_DESC = 2;
  SHOP_SORT_OPTION_VARIATIONS_DESC = 3;
  SHOP_SORT_OPTION_RELEASE_DATE_DESC = 4;
}

```

**Source references:** SRC-0305, SRC-1276  
**URL references:** None independently associated  
**Related findings:** FND-02287, FND-02288, FND-02289

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02293"></a>
## FND-02293: enum declaration: chesscom.courses.v1.TutorialCategory

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TutorialCategory {

### Evidence

- **SRC-0306** `research/proto/chesscom/courses/v1/tutorial_category.proto` — [preserved redacted evidence](../evidence/text/028f43cb620c4807db035eba67c042d56cdc62d0228126ea32b681fb8df4fc62.proto)
  Character offset 104.

```text
ource: chesscom/courses/v1/tutorial_category.proto
// syntax: proto3

package chesscom.courses.v1;

enum TutorialCategory {
  TUTORIAL_CATEGORY_UNSPECIFIED = 0;
  TUTORIAL_CATEGORY_OPENING = 1;
  TUTORIAL_CATEGORY_TACTICS = 2;
  TUTORIAL_CATEGORY_STRATEGY = 3;
  TUTORIAL_CATEGORY_ENDGAME = 4;
}

```

**Source references:** SRC-0306, SRC-1277  
**URL references:** None independently associated  
**Related findings:** FND-02294, FND-02295

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02294"></a>
## FND-02294: chesscom.courses.v1.TutorialCategory.TUTORIAL_CATEGORY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TUTORIAL_CATEGORY_UNSPECIFIED = 0;

### Evidence

- **SRC-0306** `research/proto/chesscom/courses/v1/tutorial_category.proto` — [preserved redacted evidence](../evidence/text/028f43cb620c4807db035eba67c042d56cdc62d0228126ea32b681fb8df4fc62.proto)
  Character offset 130.

```text
/tutorial_category.proto
// syntax: proto3

package chesscom.courses.v1;

enum TutorialCategory {
  TUTORIAL_CATEGORY_UNSPECIFIED = 0;
  TUTORIAL_CATEGORY_OPENING = 1;
  TUTORIAL_CATEGORY_TACTICS = 2;
  TUTORIAL_CATEGORY_STRATEGY = 3;
  TUTORIAL_CATEGORY_ENDGAME = 4;
}

```

**Source references:** SRC-0306, SRC-1277  
**URL references:** None independently associated  
**Related findings:** FND-02293, FND-02295

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02295"></a>
## FND-02295: chesscom.courses.v1.TutorialCategory.TUTORIAL_CATEGORY_OPENING = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TUTORIAL_CATEGORY_OPENING = 1;

### Evidence

- **SRC-0306** `research/proto/chesscom/courses/v1/tutorial_category.proto` — [preserved redacted evidence](../evidence/text/028f43cb620c4807db035eba67c042d56cdc62d0228126ea32b681fb8df4fc62.proto)
  Character offset 167.

```text
roto3

package chesscom.courses.v1;

enum TutorialCategory {
  TUTORIAL_CATEGORY_UNSPECIFIED = 0;
  TUTORIAL_CATEGORY_OPENING = 1;
  TUTORIAL_CATEGORY_TACTICS = 2;
  TUTORIAL_CATEGORY_STRATEGY = 3;
  TUTORIAL_CATEGORY_ENDGAME = 4;
}

```

**Source references:** SRC-0306, SRC-1277  
**URL references:** None independently associated  
**Related findings:** FND-02293, FND-02294

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02296"></a>
## FND-02296: chesscom.courses.v1.TutorialCategory.TUTORIAL_CATEGORY_TACTICS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TUTORIAL_CATEGORY_TACTICS = 2;

### Evidence

- **SRC-0306** `research/proto/chesscom/courses/v1/tutorial_category.proto` — [preserved redacted evidence](../evidence/text/028f43cb620c4807db035eba67c042d56cdc62d0228126ea32b681fb8df4fc62.proto)
  Character offset 200.

```text
1;

enum TutorialCategory {
  TUTORIAL_CATEGORY_UNSPECIFIED = 0;
  TUTORIAL_CATEGORY_OPENING = 1;
  TUTORIAL_CATEGORY_TACTICS = 2;
  TUTORIAL_CATEGORY_STRATEGY = 3;
  TUTORIAL_CATEGORY_ENDGAME = 4;
}

```

**Source references:** SRC-0306, SRC-1277  
**URL references:** None independently associated  
**Related findings:** FND-02293, FND-02294, FND-02295

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02297"></a>
## FND-02297: chesscom.courses.v1.TutorialCategory.TUTORIAL_CATEGORY_STRATEGY = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TUTORIAL_CATEGORY_STRATEGY = 3;

### Evidence

- **SRC-0306** `research/proto/chesscom/courses/v1/tutorial_category.proto` — [preserved redacted evidence](../evidence/text/028f43cb620c4807db035eba67c042d56cdc62d0228126ea32b681fb8df4fc62.proto)
  Character offset 233.

```text
ORIAL_CATEGORY_UNSPECIFIED = 0;
  TUTORIAL_CATEGORY_OPENING = 1;
  TUTORIAL_CATEGORY_TACTICS = 2;
  TUTORIAL_CATEGORY_STRATEGY = 3;
  TUTORIAL_CATEGORY_ENDGAME = 4;
}

```

**Source references:** SRC-0306, SRC-1277  
**URL references:** None independently associated  
**Related findings:** FND-02293, FND-02294, FND-02295

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02298"></a>
## FND-02298: chesscom.courses.v1.TutorialCategory.TUTORIAL_CATEGORY_ENDGAME = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TUTORIAL_CATEGORY_ENDGAME = 4;

### Evidence

- **SRC-0306** `research/proto/chesscom/courses/v1/tutorial_category.proto` — [preserved redacted evidence](../evidence/text/028f43cb620c4807db035eba67c042d56cdc62d0228126ea32b681fb8df4fc62.proto)
  Character offset 267.

```text
TUTORIAL_CATEGORY_OPENING = 1;
  TUTORIAL_CATEGORY_TACTICS = 2;
  TUTORIAL_CATEGORY_STRATEGY = 3;
  TUTORIAL_CATEGORY_ENDGAME = 4;
}

```

**Source references:** SRC-0306, SRC-1277  
**URL references:** None independently associated  
**Related findings:** FND-02293, FND-02294, FND-02295

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02299"></a>
## FND-02299: enum declaration: chesscom.courses.v1.UserAccessGrant

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum UserAccessGrant {

### Evidence

- **SRC-0307** `research/proto/chesscom/courses/v1/user_access_grant.proto` — [preserved redacted evidence](../evidence/text/e2c7b16ac1b17729b42559775522cae76c4800058fe3be9c37158ae1a244aa62.proto)
  Character offset 104.

```text
ource: chesscom/courses/v1/user_access_grant.proto
// syntax: proto3

package chesscom.courses.v1;

enum UserAccessGrant {
  USER_ACCESS_GRANT_UNSPECIFIED = 0;
  USER_ACCESS_GRANT_FULL = 1;
  USER_ACCESS_GRANT_DIAMOND_EXCLUSIVE = 2;
  USER_ACCESS_GRANT_PREVIEW = 3;
}

```

**Source references:** SRC-0307, SRC-1278  
**URL references:** None independently associated  
**Related findings:** FND-02300, FND-02301

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02300"></a>
## FND-02300: chesscom.courses.v1.UserAccessGrant.USER_ACCESS_GRANT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_ACCESS_GRANT_UNSPECIFIED = 0;

### Evidence

- **SRC-0307** `research/proto/chesscom/courses/v1/user_access_grant.proto` — [preserved redacted evidence](../evidence/text/e2c7b16ac1b17729b42559775522cae76c4800058fe3be9c37158ae1a244aa62.proto)
  Character offset 129.

```text
1/user_access_grant.proto
// syntax: proto3

package chesscom.courses.v1;

enum UserAccessGrant {
  USER_ACCESS_GRANT_UNSPECIFIED = 0;
  USER_ACCESS_GRANT_FULL = 1;
  USER_ACCESS_GRANT_DIAMOND_EXCLUSIVE = 2;
  USER_ACCESS_GRANT_PREVIEW = 3;
}

```

**Source references:** SRC-0307, SRC-1278  
**URL references:** None independently associated  
**Related findings:** FND-02299, FND-02301

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02301"></a>
## FND-02301: chesscom.courses.v1.UserAccessGrant.USER_ACCESS_GRANT_FULL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_ACCESS_GRANT_FULL = 1;

### Evidence

- **SRC-0307** `research/proto/chesscom/courses/v1/user_access_grant.proto` — [preserved redacted evidence](../evidence/text/e2c7b16ac1b17729b42559775522cae76c4800058fe3be9c37158ae1a244aa62.proto)
  Character offset 166.

```text
proto3

package chesscom.courses.v1;

enum UserAccessGrant {
  USER_ACCESS_GRANT_UNSPECIFIED = 0;
  USER_ACCESS_GRANT_FULL = 1;
  USER_ACCESS_GRANT_DIAMOND_EXCLUSIVE = 2;
  USER_ACCESS_GRANT_PREVIEW = 3;
}

```

**Source references:** SRC-0307, SRC-1278  
**URL references:** None independently associated  
**Related findings:** FND-02299, FND-02300

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02302"></a>
## FND-02302: chesscom.courses.v1.UserAccessGrant.USER_ACCESS_GRANT_DIAMOND_EXCLUSIVE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_ACCESS_GRANT_DIAMOND_EXCLUSIVE = 2;

### Evidence

- **SRC-0307** `research/proto/chesscom/courses/v1/user_access_grant.proto` — [preserved redacted evidence](../evidence/text/e2c7b16ac1b17729b42559775522cae76c4800058fe3be9c37158ae1a244aa62.proto)
  Character offset 196.

```text
es.v1;

enum UserAccessGrant {
  USER_ACCESS_GRANT_UNSPECIFIED = 0;
  USER_ACCESS_GRANT_FULL = 1;
  USER_ACCESS_GRANT_DIAMOND_EXCLUSIVE = 2;
  USER_ACCESS_GRANT_PREVIEW = 3;
}

```

**Source references:** SRC-0307, SRC-1278  
**URL references:** None independently associated  
**Related findings:** FND-02299, FND-02300, FND-02301

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02303"></a>
## FND-02303: chesscom.courses.v1.UserAccessGrant.USER_ACCESS_GRANT_PREVIEW = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_ACCESS_GRANT_PREVIEW = 3;

### Evidence

- **SRC-0307** `research/proto/chesscom/courses/v1/user_access_grant.proto` — [preserved redacted evidence](../evidence/text/e2c7b16ac1b17729b42559775522cae76c4800058fe3be9c37158ae1a244aa62.proto)
  Character offset 239.

```text
S_GRANT_UNSPECIFIED = 0;
  USER_ACCESS_GRANT_FULL = 1;
  USER_ACCESS_GRANT_DIAMOND_EXCLUSIVE = 2;
  USER_ACCESS_GRANT_PREVIEW = 3;
}

```

**Source references:** SRC-0307, SRC-1278  
**URL references:** None independently associated  
**Related findings:** FND-02299, FND-02300, FND-02301

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02304"></a>
## FND-02304: enum declaration: chesscom.courses.v1.RecommendationTouchpoint

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum RecommendationTouchpoint {

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 113.

```text
esscom/courses/v1/user_course_recommendation.proto
// syntax: proto3

package chesscom.courses.v1;

enum RecommendationTouchpoint {
  RECOMMENDATION_TOUCHPOINT_UNSPECIFIED = 0;
  RECOMMENDATION_TOUCHPOINT_DASHBOARD = 1;
  RECOMMENDATION_TOUCHPOINT_SHOP = 2;
  RECOMMENDATION_TOUCHPOINT_APP = 3;
}

enum RecommendationSignal {
  RECOMMENDATION_SIGNAL_UNSPECIFIED = 0;
  RECOMMENDATION_SIGNAL_OPENING_MATCH = 1;
  RECOMMEN
```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02305, FND-02306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02305"></a>
## FND-02305: chesscom.courses.v1.RecommendationTouchpoint.RECOMMENDATION_TOUCHPOINT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RECOMMENDATION_TOUCHPOINT_UNSPECIFIED = 0;

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 147.

```text
mmendation.proto
// syntax: proto3

package chesscom.courses.v1;

enum RecommendationTouchpoint {
  RECOMMENDATION_TOUCHPOINT_UNSPECIFIED = 0;
  RECOMMENDATION_TOUCHPOINT_DASHBOARD = 1;
  RECOMMENDATION_TOUCHPOINT_SHOP = 2;
  RECOMMENDATION_TOUCHPOINT_APP = 3;
}

enum RecommendationSignal {
  RECOMMENDATION_SIGNAL_UNSPECIFIED = 0;
  RECOMMENDATION_SIGNAL_OPENING_MATCH = 1;
  RECOMMENDATION_SIGNAL_WEAKNESS_MATCH = 2;

```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02306"></a>
## FND-02306: chesscom.courses.v1.RecommendationTouchpoint.RECOMMENDATION_TOUCHPOINT_DASHBOARD = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RECOMMENDATION_TOUCHPOINT_DASHBOARD = 1;

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 192.

```text
hesscom.courses.v1;

enum RecommendationTouchpoint {
  RECOMMENDATION_TOUCHPOINT_UNSPECIFIED = 0;
  RECOMMENDATION_TOUCHPOINT_DASHBOARD = 1;
  RECOMMENDATION_TOUCHPOINT_SHOP = 2;
  RECOMMENDATION_TOUCHPOINT_APP = 3;
}

enum RecommendationSignal {
  RECOMMENDATION_SIGNAL_UNSPECIFIED = 0;
  RECOMMENDATION_SIGNAL_OPENING_MATCH = 1;
  RECOMMENDATION_SIGNAL_WEAKNESS_MATCH = 2;
  RECOMMENDATION_SIGNAL_ACTIVITY = 3;
  RECOM
```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02307"></a>
## FND-02307: chesscom.courses.v1.RecommendationTouchpoint.RECOMMENDATION_TOUCHPOINT_SHOP = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RECOMMENDATION_TOUCHPOINT_SHOP = 2;

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 235.

```text
chpoint {
  RECOMMENDATION_TOUCHPOINT_UNSPECIFIED = 0;
  RECOMMENDATION_TOUCHPOINT_DASHBOARD = 1;
  RECOMMENDATION_TOUCHPOINT_SHOP = 2;
  RECOMMENDATION_TOUCHPOINT_APP = 3;
}

enum RecommendationSignal {
  RECOMMENDATION_SIGNAL_UNSPECIFIED = 0;
  RECOMMENDATION_SIGNAL_OPENING_MATCH = 1;
  RECOMMENDATION_SIGNAL_WEAKNESS_MATCH = 2;
  RECOMMENDATION_SIGNAL_ACTIVITY = 3;
  RECOMMENDATION_SIGNAL_QUALITY = 4;
}

message Re
```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305, FND-02306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02308"></a>
## FND-02308: chesscom.courses.v1.RecommendationTouchpoint.RECOMMENDATION_TOUCHPOINT_APP = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RECOMMENDATION_TOUCHPOINT_APP = 3;

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 273.

```text
UNSPECIFIED = 0;
  RECOMMENDATION_TOUCHPOINT_DASHBOARD = 1;
  RECOMMENDATION_TOUCHPOINT_SHOP = 2;
  RECOMMENDATION_TOUCHPOINT_APP = 3;
}

enum RecommendationSignal {
  RECOMMENDATION_SIGNAL_UNSPECIFIED = 0;
  RECOMMENDATION_SIGNAL_OPENING_MATCH = 1;
  RECOMMENDATION_SIGNAL_WEAKNESS_MATCH = 2;
  RECOMMENDATION_SIGNAL_ACTIVITY = 3;
  RECOMMENDATION_SIGNAL_QUALITY = 4;
}

message RecommendedCourse {
  oneof _eco_family 
```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305, FND-02306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02309"></a>
## FND-02309: enum declaration: chesscom.courses.v1.RecommendationSignal

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum RecommendationSignal {

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 311.

```text
HPOINT_DASHBOARD = 1;
  RECOMMENDATION_TOUCHPOINT_SHOP = 2;
  RECOMMENDATION_TOUCHPOINT_APP = 3;
}

enum RecommendationSignal {
  RECOMMENDATION_SIGNAL_UNSPECIFIED = 0;
  RECOMMENDATION_SIGNAL_OPENING_MATCH = 1;
  RECOMMENDATION_SIGNAL_WEAKNESS_MATCH = 2;
  RECOMMENDATION_SIGNAL_ACTIVITY = 3;
  RECOMMENDATION_SIGNAL_QUALITY = 4;
}

message RecommendedCourse {
  oneof _eco_family {
  .chesscom.chess.v1.EcoFamily eco_f
```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305, FND-02306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02310"></a>
## FND-02310: chesscom.courses.v1.RecommendationSignal.RECOMMENDATION_SIGNAL_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RECOMMENDATION_SIGNAL_UNSPECIFIED = 0;

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 341.

```text
ENDATION_TOUCHPOINT_SHOP = 2;
  RECOMMENDATION_TOUCHPOINT_APP = 3;
}

enum RecommendationSignal {
  RECOMMENDATION_SIGNAL_UNSPECIFIED = 0;
  RECOMMENDATION_SIGNAL_OPENING_MATCH = 1;
  RECOMMENDATION_SIGNAL_WEAKNESS_MATCH = 2;
  RECOMMENDATION_SIGNAL_ACTIVITY = 3;
  RECOMMENDATION_SIGNAL_QUALITY = 4;
}

message RecommendedCourse {
  oneof _eco_family {
  .chesscom.chess.v1.EcoFamily eco_family = 4;
  }
  optional .che
```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305, FND-02306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02311"></a>
## FND-02311: chesscom.courses.v1.RecommendationSignal.RECOMMENDATION_SIGNAL_OPENING_MATCH = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RECOMMENDATION_SIGNAL_OPENING_MATCH = 1;

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 382.

```text
ATION_TOUCHPOINT_APP = 3;
}

enum RecommendationSignal {
  RECOMMENDATION_SIGNAL_UNSPECIFIED = 0;
  RECOMMENDATION_SIGNAL_OPENING_MATCH = 1;
  RECOMMENDATION_SIGNAL_WEAKNESS_MATCH = 2;
  RECOMMENDATION_SIGNAL_ACTIVITY = 3;
  RECOMMENDATION_SIGNAL_QUALITY = 4;
}

message RecommendedCourse {
  oneof _eco_family {
  .chesscom.chess.v1.EcoFamily eco_family = 4;
  }
  optional .chesscom.courses.v1.CourseProduct product = 
```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305, FND-02306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02312"></a>
## FND-02312: chesscom.courses.v1.RecommendationSignal.RECOMMENDATION_SIGNAL_WEAKNESS_MATCH = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RECOMMENDATION_SIGNAL_WEAKNESS_MATCH = 2;

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 425.

```text
ationSignal {
  RECOMMENDATION_SIGNAL_UNSPECIFIED = 0;
  RECOMMENDATION_SIGNAL_OPENING_MATCH = 1;
  RECOMMENDATION_SIGNAL_WEAKNESS_MATCH = 2;
  RECOMMENDATION_SIGNAL_ACTIVITY = 3;
  RECOMMENDATION_SIGNAL_QUALITY = 4;
}

message RecommendedCourse {
  oneof _eco_family {
  .chesscom.chess.v1.EcoFamily eco_family = 4;
  }
  optional .chesscom.courses.v1.CourseProduct product = 1;
  optional int32 rank = 2;
  optional .c
```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305, FND-02306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02313"></a>
## FND-02313: chesscom.courses.v1.RecommendationSignal.RECOMMENDATION_SIGNAL_ACTIVITY = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RECOMMENDATION_SIGNAL_ACTIVITY = 3;

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 469.

```text
IFIED = 0;
  RECOMMENDATION_SIGNAL_OPENING_MATCH = 1;
  RECOMMENDATION_SIGNAL_WEAKNESS_MATCH = 2;
  RECOMMENDATION_SIGNAL_ACTIVITY = 3;
  RECOMMENDATION_SIGNAL_QUALITY = 4;
}

message RecommendedCourse {
  oneof _eco_family {
  .chesscom.chess.v1.EcoFamily eco_family = 4;
  }
  optional .chesscom.courses.v1.CourseProduct product = 1;
  optional int32 rank = 2;
  optional .chesscom.courses.v1.RecommendationSignal prim
```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305, FND-02306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02314"></a>
## FND-02314: chesscom.courses.v1.RecommendationSignal.RECOMMENDATION_SIGNAL_QUALITY = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RECOMMENDATION_SIGNAL_QUALITY = 4;

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 507.

```text
NING_MATCH = 1;
  RECOMMENDATION_SIGNAL_WEAKNESS_MATCH = 2;
  RECOMMENDATION_SIGNAL_ACTIVITY = 3;
  RECOMMENDATION_SIGNAL_QUALITY = 4;
}

message RecommendedCourse {
  oneof _eco_family {
  .chesscom.chess.v1.EcoFamily eco_family = 4;
  }
  optional .chesscom.courses.v1.CourseProduct product = 1;
  optional int32 rank = 2;
  optional .chesscom.courses.v1.RecommendationSignal primary_signal = 3;
}

```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305, FND-02306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02315"></a>
## FND-02315: message declaration: chesscom.courses.v1.RecommendedCourse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RecommendedCourse {

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 545.

```text
L_WEAKNESS_MATCH = 2;
  RECOMMENDATION_SIGNAL_ACTIVITY = 3;
  RECOMMENDATION_SIGNAL_QUALITY = 4;
}

message RecommendedCourse {
  oneof _eco_family {
  .chesscom.chess.v1.EcoFamily eco_family = 4;
  }
  optional .chesscom.courses.v1.CourseProduct product = 1;
  optional int32 rank = 2;
  optional .chesscom.courses.v1.RecommendationSignal primary_signal = 3;
}

```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305, FND-02306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02316"></a>
## FND-02316: oneof declaration: chesscom.courses.v1.RecommendedCourse._eco_family

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _eco_family {

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 575.

```text
ENDATION_SIGNAL_ACTIVITY = 3;
  RECOMMENDATION_SIGNAL_QUALITY = 4;
}

message RecommendedCourse {
  oneof _eco_family {
  .chesscom.chess.v1.EcoFamily eco_family = 4;
  }
  optional .chesscom.courses.v1.CourseProduct product = 1;
  optional int32 rank = 2;
  optional .chesscom.courses.v1.RecommendationSignal primary_signal = 3;
}

```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305, FND-02306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02317"></a>
## FND-02317: chesscom.courses.v1.RecommendedCourse.eco_family = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.EcoFamily eco_family = 4;

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 597.

```text
TY = 3;
  RECOMMENDATION_SIGNAL_QUALITY = 4;
}

message RecommendedCourse {
  oneof _eco_family {
  .chesscom.chess.v1.EcoFamily eco_family = 4;
  }
  optional .chesscom.courses.v1.CourseProduct product = 1;
  optional int32 rank = 2;
  optional .chesscom.courses.v1.RecommendationSignal primary_signal = 3;
}

```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305, FND-02306

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02318"></a>
## FND-02318: chesscom.courses.v1.RecommendedCourse.product = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseProduct product = 1;

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 648.

```text
sage RecommendedCourse {
  oneof _eco_family {
  .chesscom.chess.v1.EcoFamily eco_family = 4;
  }
  optional .chesscom.courses.v1.CourseProduct product = 1;
  optional int32 rank = 2;
  optional .chesscom.courses.v1.RecommendationSignal primary_signal = 3;
}

```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305, FND-02306

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02319"></a>
## FND-02319: chesscom.courses.v1.RecommendedCourse.rank = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 rank = 2;

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 707.

```text
chess.v1.EcoFamily eco_family = 4;
  }
  optional .chesscom.courses.v1.CourseProduct product = 1;
  optional int32 rank = 2;
  optional .chesscom.courses.v1.RecommendationSignal primary_signal = 3;
}

```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305, FND-02306

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02320"></a>
## FND-02320: chesscom.courses.v1.RecommendedCourse.primary_signal = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.RecommendationSignal primary_signal = 3;

### Evidence

- **SRC-0308** `research/proto/chesscom/courses/v1/user_course_recommendation.proto` — [preserved redacted evidence](../evidence/text/3365ade0a5121ffce312c3b7d5396d1a40951175694cdf4fa6137d80c82d74ad.proto)
  Character offset 734.

```text
ly = 4;
  }
  optional .chesscom.courses.v1.CourseProduct product = 1;
  optional int32 rank = 2;
  optional .chesscom.courses.v1.RecommendationSignal primary_signal = 3;
}

```

**Source references:** SRC-0308, SRC-1279  
**URL references:** None independently associated  
**Related findings:** FND-02304, FND-02305, FND-02306

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02321"></a>
## FND-02321: enum declaration: chesscom.courses.v1.UserFlag

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum UserFlag {

### Evidence

- **SRC-0309** `research/proto/chesscom/courses/v1/user_flag.proto` — [preserved redacted evidence](../evidence/text/0266ba1bc1ce55c55f76ebd6039e635e353cabc615e71a23f6128a97d13eb97b.proto)
  Character offset 96.

```text
// source: chesscom/courses/v1/user_flag.proto
// syntax: proto3

package chesscom.courses.v1;

enum UserFlag {
  USER_FLAG_UNSPECIFIED = 0;
  USER_FLAG_HAS_EXCLUSIVE_COURSES = 1;
  USER_FLAG_HAS_GLOBAL_STACKABLE_DISCOUNT = 2;
  USER_FLAG_HAS_UNLIMITED_PREVIEWS = 3;
  USER_FLAG_HAS_CLOSED_GIVE_FEEDBACK_WIDGET = 4;
  USER_FLAG_HAS_TUTORIAL = 5;
  USER_FLAG_HAS_CLOSED_WELCOME_WIDGET = 6;
  USER_FLAG_OWNS_A_COURSE =
```

**Source references:** SRC-0309, SRC-1280  
**URL references:** None independently associated  
**Related findings:** FND-02322, FND-02323

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02322"></a>
## FND-02322: chesscom.courses.v1.UserFlag.USER_FLAG_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_FLAG_UNSPECIFIED = 0;

### Evidence

- **SRC-0309** `research/proto/chesscom/courses/v1/user_flag.proto` — [preserved redacted evidence](../evidence/text/0266ba1bc1ce55c55f76ebd6039e635e353cabc615e71a23f6128a97d13eb97b.proto)
  Character offset 114.

```text
sscom/courses/v1/user_flag.proto
// syntax: proto3

package chesscom.courses.v1;

enum UserFlag {
  USER_FLAG_UNSPECIFIED = 0;
  USER_FLAG_HAS_EXCLUSIVE_COURSES = 1;
  USER_FLAG_HAS_GLOBAL_STACKABLE_DISCOUNT = 2;
  USER_FLAG_HAS_UNLIMITED_PREVIEWS = 3;
  USER_FLAG_HAS_CLOSED_GIVE_FEEDBACK_WIDGET = 4;
  USER_FLAG_HAS_TUTORIAL = 5;
  USER_FLAG_HAS_CLOSED_WELCOME_WIDGET = 6;
  USER_FLAG_OWNS_A_COURSE = 7;
  USER_FLAG_HA
```

**Source references:** SRC-0309, SRC-1280  
**URL references:** None independently associated  
**Related findings:** FND-02321, FND-02323

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02323"></a>
## FND-02323: chesscom.courses.v1.UserFlag.USER_FLAG_HAS_EXCLUSIVE_COURSES = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_FLAG_HAS_EXCLUSIVE_COURSES = 1;

### Evidence

- **SRC-0309** `research/proto/chesscom/courses/v1/user_flag.proto` — [preserved redacted evidence](../evidence/text/0266ba1bc1ce55c55f76ebd6039e635e353cabc615e71a23f6128a97d13eb97b.proto)
  Character offset 143.

```text
oto
// syntax: proto3

package chesscom.courses.v1;

enum UserFlag {
  USER_FLAG_UNSPECIFIED = 0;
  USER_FLAG_HAS_EXCLUSIVE_COURSES = 1;
  USER_FLAG_HAS_GLOBAL_STACKABLE_DISCOUNT = 2;
  USER_FLAG_HAS_UNLIMITED_PREVIEWS = 3;
  USER_FLAG_HAS_CLOSED_GIVE_FEEDBACK_WIDGET = 4;
  USER_FLAG_HAS_TUTORIAL = 5;
  USER_FLAG_HAS_CLOSED_WELCOME_WIDGET = 6;
  USER_FLAG_OWNS_A_COURSE = 7;
  USER_FLAG_HAS_GLOBAL_NON_STACKABLE_DISCOU
```

**Source references:** SRC-0309, SRC-1280  
**URL references:** None independently associated  
**Related findings:** FND-02321, FND-02322

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02324"></a>
## FND-02324: chesscom.courses.v1.UserFlag.USER_FLAG_HAS_GLOBAL_STACKABLE_DISCOUNT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_FLAG_HAS_GLOBAL_STACKABLE_DISCOUNT = 2;

### Evidence

- **SRC-0309** `research/proto/chesscom/courses/v1/user_flag.proto` — [preserved redacted evidence](../evidence/text/0266ba1bc1ce55c55f76ebd6039e635e353cabc615e71a23f6128a97d13eb97b.proto)
  Character offset 182.

```text
.courses.v1;

enum UserFlag {
  USER_FLAG_UNSPECIFIED = 0;
  USER_FLAG_HAS_EXCLUSIVE_COURSES = 1;
  USER_FLAG_HAS_GLOBAL_STACKABLE_DISCOUNT = 2;
  USER_FLAG_HAS_UNLIMITED_PREVIEWS = 3;
  USER_FLAG_HAS_CLOSED_GIVE_FEEDBACK_WIDGET = 4;
  USER_FLAG_HAS_TUTORIAL = 5;
  USER_FLAG_HAS_CLOSED_WELCOME_WIDGET = 6;
  USER_FLAG_OWNS_A_COURSE = 7;
  USER_FLAG_HAS_GLOBAL_NON_STACKABLE_DISCOUNT = 8;
  USER_FLAG_HAS_PREVIEW_COURSES
```

**Source references:** SRC-0309, SRC-1280  
**URL references:** None independently associated  
**Related findings:** FND-02321, FND-02322, FND-02323

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02325"></a>
## FND-02325: chesscom.courses.v1.UserFlag.USER_FLAG_HAS_UNLIMITED_PREVIEWS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_FLAG_HAS_UNLIMITED_PREVIEWS = 3;

### Evidence

- **SRC-0309** `research/proto/chesscom/courses/v1/user_flag.proto` — [preserved redacted evidence](../evidence/text/0266ba1bc1ce55c55f76ebd6039e635e353cabc615e71a23f6128a97d13eb97b.proto)
  Character offset 229.

```text
CIFIED = 0;
  USER_FLAG_HAS_EXCLUSIVE_COURSES = 1;
  USER_FLAG_HAS_GLOBAL_STACKABLE_DISCOUNT = 2;
  USER_FLAG_HAS_UNLIMITED_PREVIEWS = 3;
  USER_FLAG_HAS_CLOSED_GIVE_FEEDBACK_WIDGET = 4;
  USER_FLAG_HAS_TUTORIAL = 5;
  USER_FLAG_HAS_CLOSED_WELCOME_WIDGET = 6;
  USER_FLAG_OWNS_A_COURSE = 7;
  USER_FLAG_HAS_GLOBAL_NON_STACKABLE_DISCOUNT = 8;
  USER_FLAG_HAS_PREVIEW_COURSES = 9;
  USER_FLAG_HAS_SKIPPED_FTUE_SELECTOR = 1
```

**Source references:** SRC-0309, SRC-1280  
**URL references:** None independently associated  
**Related findings:** FND-02321, FND-02322, FND-02323

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02326"></a>
## FND-02326: chesscom.courses.v1.UserFlag.USER_FLAG_HAS_CLOSED_GIVE_FEEDBACK_WIDGET = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_FLAG_HAS_CLOSED_GIVE_FEEDBACK_WIDGET = 4;

### Evidence

- **SRC-0309** `research/proto/chesscom/courses/v1/user_flag.proto` — [preserved redacted evidence](../evidence/text/0266ba1bc1ce55c55f76ebd6039e635e353cabc615e71a23f6128a97d13eb97b.proto)
  Character offset 269.

```text
URSES = 1;
  USER_FLAG_HAS_GLOBAL_STACKABLE_DISCOUNT = 2;
  USER_FLAG_HAS_UNLIMITED_PREVIEWS = 3;
  USER_FLAG_HAS_CLOSED_GIVE_FEEDBACK_WIDGET = 4;
  USER_FLAG_HAS_TUTORIAL = 5;
  USER_FLAG_HAS_CLOSED_WELCOME_WIDGET = 6;
  USER_FLAG_OWNS_A_COURSE = 7;
  USER_FLAG_HAS_GLOBAL_NON_STACKABLE_DISCOUNT = 8;
  USER_FLAG_HAS_PREVIEW_COURSES = 9;
  USER_FLAG_HAS_SKIPPED_FTUE_SELECTOR = 10;
  USER_FLAG_COACH_DEFAULT_OFF = 11;
}
```

**Source references:** SRC-0309, SRC-1280  
**URL references:** None independently associated  
**Related findings:** FND-02321, FND-02322, FND-02323

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02327"></a>
## FND-02327: chesscom.courses.v1.UserFlag.USER_FLAG_HAS_TUTORIAL = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_FLAG_HAS_TUTORIAL = 5;

### Evidence

- **SRC-0309** `research/proto/chesscom/courses/v1/user_flag.proto` — [preserved redacted evidence](../evidence/text/0266ba1bc1ce55c55f76ebd6039e635e353cabc615e71a23f6128a97d13eb97b.proto)
  Character offset 318.

```text
UNT = 2;
  USER_FLAG_HAS_UNLIMITED_PREVIEWS = 3;
  USER_FLAG_HAS_CLOSED_GIVE_FEEDBACK_WIDGET = 4;
  USER_FLAG_HAS_TUTORIAL = 5;
  USER_FLAG_HAS_CLOSED_WELCOME_WIDGET = 6;
  USER_FLAG_OWNS_A_COURSE = 7;
  USER_FLAG_HAS_GLOBAL_NON_STACKABLE_DISCOUNT = 8;
  USER_FLAG_HAS_PREVIEW_COURSES = 9;
  USER_FLAG_HAS_SKIPPED_FTUE_SELECTOR = 10;
  USER_FLAG_COACH_DEFAULT_OFF = 11;
}

```

**Source references:** SRC-0309, SRC-1280  
**URL references:** None independently associated  
**Related findings:** FND-02321, FND-02322, FND-02323

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02328"></a>
## FND-02328: chesscom.courses.v1.UserFlag.USER_FLAG_HAS_CLOSED_WELCOME_WIDGET = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_FLAG_HAS_CLOSED_WELCOME_WIDGET = 6;

### Evidence

- **SRC-0309** `research/proto/chesscom/courses/v1/user_flag.proto` — [preserved redacted evidence](../evidence/text/0266ba1bc1ce55c55f76ebd6039e635e353cabc615e71a23f6128a97d13eb97b.proto)
  Character offset 348.

```text
ITED_PREVIEWS = 3;
  USER_FLAG_HAS_CLOSED_GIVE_FEEDBACK_WIDGET = 4;
  USER_FLAG_HAS_TUTORIAL = 5;
  USER_FLAG_HAS_CLOSED_WELCOME_WIDGET = 6;
  USER_FLAG_OWNS_A_COURSE = 7;
  USER_FLAG_HAS_GLOBAL_NON_STACKABLE_DISCOUNT = 8;
  USER_FLAG_HAS_PREVIEW_COURSES = 9;
  USER_FLAG_HAS_SKIPPED_FTUE_SELECTOR = 10;
  USER_FLAG_COACH_DEFAULT_OFF = 11;
}

```

**Source references:** SRC-0309, SRC-1280  
**URL references:** None independently associated  
**Related findings:** FND-02321, FND-02322, FND-02323

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02329"></a>
## FND-02329: chesscom.courses.v1.UserFlag.USER_FLAG_OWNS_A_COURSE = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_FLAG_OWNS_A_COURSE = 7;

### Evidence

- **SRC-0309** `research/proto/chesscom/courses/v1/user_flag.proto` — [preserved redacted evidence](../evidence/text/0266ba1bc1ce55c55f76ebd6039e635e353cabc615e71a23f6128a97d13eb97b.proto)
  Character offset 391.

```text
IVE_FEEDBACK_WIDGET = 4;
  USER_FLAG_HAS_TUTORIAL = 5;
  USER_FLAG_HAS_CLOSED_WELCOME_WIDGET = 6;
  USER_FLAG_OWNS_A_COURSE = 7;
  USER_FLAG_HAS_GLOBAL_NON_STACKABLE_DISCOUNT = 8;
  USER_FLAG_HAS_PREVIEW_COURSES = 9;
  USER_FLAG_HAS_SKIPPED_FTUE_SELECTOR = 10;
  USER_FLAG_COACH_DEFAULT_OFF = 11;
}

```

**Source references:** SRC-0309, SRC-1280  
**URL references:** None independently associated  
**Related findings:** FND-02321, FND-02322, FND-02323

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02330"></a>
## FND-02330: chesscom.courses.v1.UserFlag.USER_FLAG_HAS_GLOBAL_NON_STACKABLE_DISCOUNT = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_FLAG_HAS_GLOBAL_NON_STACKABLE_DISCOUNT = 8;

### Evidence

- **SRC-0309** `research/proto/chesscom/courses/v1/user_flag.proto` — [preserved redacted evidence](../evidence/text/0266ba1bc1ce55c55f76ebd6039e635e353cabc615e71a23f6128a97d13eb97b.proto)
  Character offset 422.

```text
_FLAG_HAS_TUTORIAL = 5;
  USER_FLAG_HAS_CLOSED_WELCOME_WIDGET = 6;
  USER_FLAG_OWNS_A_COURSE = 7;
  USER_FLAG_HAS_GLOBAL_NON_STACKABLE_DISCOUNT = 8;
  USER_FLAG_HAS_PREVIEW_COURSES = 9;
  USER_FLAG_HAS_SKIPPED_FTUE_SELECTOR = 10;
  USER_FLAG_COACH_DEFAULT_OFF = 11;
}

```

**Source references:** SRC-0309, SRC-1280  
**URL references:** None independently associated  
**Related findings:** FND-02321, FND-02322, FND-02323

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02331"></a>
## FND-02331: chesscom.courses.v1.UserFlag.USER_FLAG_HAS_PREVIEW_COURSES = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_FLAG_HAS_PREVIEW_COURSES = 9;

### Evidence

- **SRC-0309** `research/proto/chesscom/courses/v1/user_flag.proto` — [preserved redacted evidence](../evidence/text/0266ba1bc1ce55c55f76ebd6039e635e353cabc615e71a23f6128a97d13eb97b.proto)
  Character offset 473.

```text
OME_WIDGET = 6;
  USER_FLAG_OWNS_A_COURSE = 7;
  USER_FLAG_HAS_GLOBAL_NON_STACKABLE_DISCOUNT = 8;
  USER_FLAG_HAS_PREVIEW_COURSES = 9;
  USER_FLAG_HAS_SKIPPED_FTUE_SELECTOR = 10;
  USER_FLAG_COACH_DEFAULT_OFF = 11;
}

```

**Source references:** SRC-0309, SRC-1280  
**URL references:** None independently associated  
**Related findings:** FND-02321, FND-02322, FND-02323

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02332"></a>
## FND-02332: chesscom.courses.v1.UserFlag.USER_FLAG_HAS_SKIPPED_FTUE_SELECTOR = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_FLAG_HAS_SKIPPED_FTUE_SELECTOR = 10;

### Evidence

- **SRC-0309** `research/proto/chesscom/courses/v1/user_flag.proto` — [preserved redacted evidence](../evidence/text/0266ba1bc1ce55c55f76ebd6039e635e353cabc615e71a23f6128a97d13eb97b.proto)
  Character offset 510.

```text
URSE = 7;
  USER_FLAG_HAS_GLOBAL_NON_STACKABLE_DISCOUNT = 8;
  USER_FLAG_HAS_PREVIEW_COURSES = 9;
  USER_FLAG_HAS_SKIPPED_FTUE_SELECTOR = 10;
  USER_FLAG_COACH_DEFAULT_OFF = 11;
}

```

**Source references:** SRC-0309, SRC-1280  
**URL references:** None independently associated  
**Related findings:** FND-02321, FND-02322, FND-02323

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02333"></a>
## FND-02333: chesscom.courses.v1.UserFlag.USER_FLAG_COACH_DEFAULT_OFF = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_FLAG_COACH_DEFAULT_OFF = 11;

### Evidence

- **SRC-0309** `research/proto/chesscom/courses/v1/user_flag.proto` — [preserved redacted evidence](../evidence/text/0266ba1bc1ce55c55f76ebd6039e635e353cabc615e71a23f6128a97d13eb97b.proto)
  Character offset 554.

```text
LE_DISCOUNT = 8;
  USER_FLAG_HAS_PREVIEW_COURSES = 9;
  USER_FLAG_HAS_SKIPPED_FTUE_SELECTOR = 10;
  USER_FLAG_COACH_DEFAULT_OFF = 11;
}

```

**Source references:** SRC-0309, SRC-1280  
**URL references:** None independently associated  
**Related findings:** FND-02321, FND-02322, FND-02323

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02334"></a>
## FND-02334: message declaration: chesscom.courses.v1.UserGoal

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserGoal {

### Evidence

- **SRC-0310** `research/proto/chesscom/courses/v1/user_goal.proto` — [preserved redacted evidence](../evidence/text/90fa4eb19d31ab6bd4f962d7173fe87d5347e98f5cd113bb6174cb421d965d7c.proto)
  Character offset 96.

```text
// source: chesscom/courses/v1/user_goal.proto
// syntax: proto3

package chesscom.courses.v1;

message UserGoal {
  optional .chesscom.courses.v1.GoalType goal_type = 1;
  repeated .chesscom.courses.v1.GoalStep steps = 2;
  repeated .chesscom.courses.v1.Reward reward = 3;
  optional .google.protobuf.Timestamp achieved_at = 4;
  optional .google.protobuf.Timestamp reward_claimed_at = 5;
}

```

**Source references:** SRC-0310, SRC-1281  
**URL references:** None independently associated  
**Related findings:** FND-02335, FND-02336

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02335"></a>
## FND-02335: chesscom.courses.v1.UserGoal.goal_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.GoalType goal_type = 1;

### Evidence

- **SRC-0310** `research/proto/chesscom/courses/v1/user_goal.proto` — [preserved redacted evidence](../evidence/text/90fa4eb19d31ab6bd4f962d7173fe87d5347e98f5cd113bb6174cb421d965d7c.proto)
  Character offset 117.

```text
om/courses/v1/user_goal.proto
// syntax: proto3

package chesscom.courses.v1;

message UserGoal {
  optional .chesscom.courses.v1.GoalType goal_type = 1;
  repeated .chesscom.courses.v1.GoalStep steps = 2;
  repeated .chesscom.courses.v1.Reward reward = 3;
  optional .google.protobuf.Timestamp achieved_at = 4;
  optional .google.protobuf.Timestamp reward_claimed_at = 5;
}

```

**Source references:** SRC-0310, SRC-1281  
**URL references:** None independently associated  
**Related findings:** FND-02334, FND-02336

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02336"></a>
## FND-02336: chesscom.courses.v1.UserGoal.steps = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.GoalStep steps = 2;

### Evidence

- **SRC-0310** `research/proto/chesscom/courses/v1/user_goal.proto` — [preserved redacted evidence](../evidence/text/90fa4eb19d31ab6bd4f962d7173fe87d5347e98f5cd113bb6174cb421d965d7c.proto)
  Character offset 173.

```text
 chesscom.courses.v1;

message UserGoal {
  optional .chesscom.courses.v1.GoalType goal_type = 1;
  repeated .chesscom.courses.v1.GoalStep steps = 2;
  repeated .chesscom.courses.v1.Reward reward = 3;
  optional .google.protobuf.Timestamp achieved_at = 4;
  optional .google.protobuf.Timestamp reward_claimed_at = 5;
}

```

**Source references:** SRC-0310, SRC-1281  
**URL references:** None independently associated  
**Related findings:** FND-02334, FND-02335

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02337"></a>
## FND-02337: chesscom.courses.v1.UserGoal.reward = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.Reward reward = 3;

### Evidence

- **SRC-0310** `research/proto/chesscom/courses/v1/user_goal.proto` — [preserved redacted evidence](../evidence/text/90fa4eb19d31ab6bd4f962d7173fe87d5347e98f5cd113bb6174cb421d965d7c.proto)
  Character offset 225.

```text
 .chesscom.courses.v1.GoalType goal_type = 1;
  repeated .chesscom.courses.v1.GoalStep steps = 2;
  repeated .chesscom.courses.v1.Reward reward = 3;
  optional .google.protobuf.Timestamp achieved_at = 4;
  optional .google.protobuf.Timestamp reward_claimed_at = 5;
}

```

**Source references:** SRC-0310, SRC-1281  
**URL references:** None independently associated  
**Related findings:** FND-02334, FND-02335, FND-02336

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02338"></a>
## FND-02338: chesscom.courses.v1.UserGoal.achieved_at = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp achieved_at = 4;

### Evidence

- **SRC-0310** `research/proto/chesscom/courses/v1/user_goal.proto` — [preserved redacted evidence](../evidence/text/90fa4eb19d31ab6bd4f962d7173fe87d5347e98f5cd113bb6174cb421d965d7c.proto)
  Character offset 276.

```text
eated .chesscom.courses.v1.GoalStep steps = 2;
  repeated .chesscom.courses.v1.Reward reward = 3;
  optional .google.protobuf.Timestamp achieved_at = 4;
  optional .google.protobuf.Timestamp reward_claimed_at = 5;
}

```

**Source references:** SRC-0310, SRC-1281  
**URL references:** None independently associated  
**Related findings:** FND-02334, FND-02335, FND-02336

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02339"></a>
## FND-02339: chesscom.courses.v1.UserGoal.reward_claimed_at = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp reward_claimed_at = 5;

### Evidence

- **SRC-0310** `research/proto/chesscom/courses/v1/user_goal.proto` — [preserved redacted evidence](../evidence/text/90fa4eb19d31ab6bd4f962d7173fe87d5347e98f5cd113bb6174cb421d965d7c.proto)
  Character offset 331.

```text
ed .chesscom.courses.v1.Reward reward = 3;
  optional .google.protobuf.Timestamp achieved_at = 4;
  optional .google.protobuf.Timestamp reward_claimed_at = 5;
}

```

**Source references:** SRC-0310, SRC-1281  
**URL references:** None independently associated  
**Related findings:** FND-02334, FND-02335, FND-02336

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02340"></a>
## FND-02340: message declaration: chesscom.courses.v1.SetUserGoalRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetUserGoalRequest {

### Evidence

- **SRC-0311** `research/proto/chesscom/courses/v1/user_goal_service.proto` — [preserved redacted evidence](../evidence/text/a7d92b4462ffa5163833dc58f835fd7b81fe71dbaf97665af0a2dc7baae148c1.proto)
  Character offset 104.

```text
ource: chesscom/courses/v1/user_goal_service.proto
// syntax: proto3

package chesscom.courses.v1;

message SetUserGoalRequest {
  optional .chesscom.courses.v1.GoalType goal_type = 1;
}

message SetUserGoalResponse {
}

message ClaimRewardRequest {
  optional .chesscom.courses.v1.GoalType goal_type = 1;
  repeated .chesscom.courses.v1.Reward reward = 2;
}

message ClaimRewardResponse {
}

```

**Source references:** SRC-0311, SRC-1282  
**URL references:** None independently associated  
**Related findings:** FND-02341, FND-02342

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02341"></a>
## FND-02341: chesscom.courses.v1.SetUserGoalRequest.goal_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.GoalType goal_type = 1;

### Evidence

- **SRC-0311** `research/proto/chesscom/courses/v1/user_goal_service.proto` — [preserved redacted evidence](../evidence/text/a7d92b4462ffa5163833dc58f835fd7b81fe71dbaf97665af0a2dc7baae148c1.proto)
  Character offset 135.

```text
_goal_service.proto
// syntax: proto3

package chesscom.courses.v1;

message SetUserGoalRequest {
  optional .chesscom.courses.v1.GoalType goal_type = 1;
}

message SetUserGoalResponse {
}

message ClaimRewardRequest {
  optional .chesscom.courses.v1.GoalType goal_type = 1;
  repeated .chesscom.courses.v1.Reward reward = 2;
}

message ClaimRewardResponse {
}

```

**Source references:** SRC-0311, SRC-1282  
**URL references:** None independently associated  
**Related findings:** FND-02340, FND-02342

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02342"></a>
## FND-02342: message declaration: chesscom.courses.v1.SetUserGoalResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetUserGoalResponse {

### Evidence

- **SRC-0311** `research/proto/chesscom/courses/v1/user_goal_service.proto` — [preserved redacted evidence](../evidence/text/a7d92b4462ffa5163833dc58f835fd7b81fe71dbaf97665af0a2dc7baae148c1.proto)
  Character offset 192.

```text
ourses.v1;

message SetUserGoalRequest {
  optional .chesscom.courses.v1.GoalType goal_type = 1;
}

message SetUserGoalResponse {
}

message ClaimRewardRequest {
  optional .chesscom.courses.v1.GoalType goal_type = 1;
  repeated .chesscom.courses.v1.Reward reward = 2;
}

message ClaimRewardResponse {
}

```

**Source references:** SRC-0311, SRC-1282  
**URL references:** None independently associated  
**Related findings:** FND-02340, FND-02341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02343"></a>
## FND-02343: message declaration: chesscom.courses.v1.ClaimRewardRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ClaimRewardRequest {

### Evidence

- **SRC-0311** `research/proto/chesscom/courses/v1/user_goal_service.proto` — [preserved redacted evidence](../evidence/text/a7d92b4462ffa5163833dc58f835fd7b81fe71dbaf97665af0a2dc7baae148c1.proto)
  Character offset 225.

```text
quest {
  optional .chesscom.courses.v1.GoalType goal_type = 1;
}

message SetUserGoalResponse {
}

message ClaimRewardRequest {
  optional .chesscom.courses.v1.GoalType goal_type = 1;
  repeated .chesscom.courses.v1.Reward reward = 2;
}

message ClaimRewardResponse {
}

```

**Source references:** SRC-0311, SRC-1282  
**URL references:** None independently associated  
**Related findings:** FND-02340, FND-02341, FND-02342

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02344"></a>
## FND-02344: chesscom.courses.v1.ClaimRewardRequest.goal_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.GoalType goal_type = 1;

### Evidence

- **SRC-0311** `research/proto/chesscom/courses/v1/user_goal_service.proto` — [preserved redacted evidence](../evidence/text/a7d92b4462ffa5163833dc58f835fd7b81fe71dbaf97665af0a2dc7baae148c1.proto)
  Character offset 135.

```text
_goal_service.proto
// syntax: proto3

package chesscom.courses.v1;

message SetUserGoalRequest {
  optional .chesscom.courses.v1.GoalType goal_type = 1;
}

message SetUserGoalResponse {
}

message ClaimRewardRequest {
  optional .chesscom.courses.v1.GoalType goal_type = 1;
  repeated .chesscom.courses.v1.Reward reward = 2;
}

message ClaimRewardResponse {
}

```

**Source references:** SRC-0311, SRC-1282  
**URL references:** None independently associated  
**Related findings:** FND-02340, FND-02341, FND-02342

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02345"></a>
## FND-02345: chesscom.courses.v1.ClaimRewardRequest.reward = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.Reward reward = 2;

### Evidence

- **SRC-0311** `research/proto/chesscom/courses/v1/user_goal_service.proto` — [preserved redacted evidence](../evidence/text/a7d92b4462ffa5163833dc58f835fd7b81fe71dbaf97665af0a2dc7baae148c1.proto)
  Character offset 312.

```text
esponse {
}

message ClaimRewardRequest {
  optional .chesscom.courses.v1.GoalType goal_type = 1;
  repeated .chesscom.courses.v1.Reward reward = 2;
}

message ClaimRewardResponse {
}

```

**Source references:** SRC-0311, SRC-1282  
**URL references:** None independently associated  
**Related findings:** FND-02340, FND-02341, FND-02342

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02346"></a>
## FND-02346: message declaration: chesscom.courses.v1.ClaimRewardResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ClaimRewardResponse {

### Evidence

- **SRC-0311** `research/proto/chesscom/courses/v1/user_goal_service.proto` — [preserved redacted evidence](../evidence/text/a7d92b4462ffa5163833dc58f835fd7b81fe71dbaf97665af0a2dc7baae148c1.proto)
  Character offset 364.

```text
 .chesscom.courses.v1.GoalType goal_type = 1;
  repeated .chesscom.courses.v1.Reward reward = 2;
}

message ClaimRewardResponse {
}

```

**Source references:** SRC-0311, SRC-1282  
**URL references:** None independently associated  
**Related findings:** FND-02340, FND-02341, FND-02342

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02347"></a>
## FND-02347: enum declaration: chesscom.courses.v1.VariationAccessType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum VariationAccessType {

### Evidence

- **SRC-0312** `research/proto/chesscom/courses/v1/variation_access_type.proto` — [preserved redacted evidence](../evidence/text/81be6f1b643afd4ea0d4cd85b00c659f0f251fcfe6fe7ac96f97d46fe88e363b.proto)
  Character offset 108.

```text
e: chesscom/courses/v1/variation_access_type.proto
// syntax: proto3

package chesscom.courses.v1;

enum VariationAccessType {
  VARIATION_ACCESS_TYPE_UNSPECIFIED = 0;
  VARIATION_ACCESS_TYPE_PREVIEWABLE = 1;
  VARIATION_ACCESS_TYPE_LOCKED = 2;
  VARIATION_ACCESS_TYPE_FULL_ACCESS = 3;
}

```

**Source references:** SRC-0312, SRC-1283  
**URL references:** None independently associated  
**Related findings:** FND-02348, FND-02349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02348"></a>
## FND-02348: chesscom.courses.v1.VariationAccessType.VARIATION_ACCESS_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIATION_ACCESS_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0312** `research/proto/chesscom/courses/v1/variation_access_type.proto` — [preserved redacted evidence](../evidence/text/81be6f1b643afd4ea0d4cd85b00c659f0f251fcfe6fe7ac96f97d46fe88e363b.proto)
  Character offset 137.

```text
ion_access_type.proto
// syntax: proto3

package chesscom.courses.v1;

enum VariationAccessType {
  VARIATION_ACCESS_TYPE_UNSPECIFIED = 0;
  VARIATION_ACCESS_TYPE_PREVIEWABLE = 1;
  VARIATION_ACCESS_TYPE_LOCKED = 2;
  VARIATION_ACCESS_TYPE_FULL_ACCESS = 3;
}

```

**Source references:** SRC-0312, SRC-1283  
**URL references:** None independently associated  
**Related findings:** FND-02347, FND-02349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02349"></a>
## FND-02349: chesscom.courses.v1.VariationAccessType.VARIATION_ACCESS_TYPE_PREVIEWABLE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIATION_ACCESS_TYPE_PREVIEWABLE = 1;

### Evidence

- **SRC-0312** `research/proto/chesscom/courses/v1/variation_access_type.proto` — [preserved redacted evidence](../evidence/text/81be6f1b643afd4ea0d4cd85b00c659f0f251fcfe6fe7ac96f97d46fe88e363b.proto)
  Character offset 178.

```text
package chesscom.courses.v1;

enum VariationAccessType {
  VARIATION_ACCESS_TYPE_UNSPECIFIED = 0;
  VARIATION_ACCESS_TYPE_PREVIEWABLE = 1;
  VARIATION_ACCESS_TYPE_LOCKED = 2;
  VARIATION_ACCESS_TYPE_FULL_ACCESS = 3;
}

```

**Source references:** SRC-0312, SRC-1283  
**URL references:** None independently associated  
**Related findings:** FND-02347, FND-02348

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02350"></a>
## FND-02350: chesscom.courses.v1.VariationAccessType.VARIATION_ACCESS_TYPE_LOCKED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIATION_ACCESS_TYPE_LOCKED = 2;

### Evidence

- **SRC-0312** `research/proto/chesscom/courses/v1/variation_access_type.proto` — [preserved redacted evidence](../evidence/text/81be6f1b643afd4ea0d4cd85b00c659f0f251fcfe6fe7ac96f97d46fe88e363b.proto)
  Character offset 219.

```text
ionAccessType {
  VARIATION_ACCESS_TYPE_UNSPECIFIED = 0;
  VARIATION_ACCESS_TYPE_PREVIEWABLE = 1;
  VARIATION_ACCESS_TYPE_LOCKED = 2;
  VARIATION_ACCESS_TYPE_FULL_ACCESS = 3;
}

```

**Source references:** SRC-0312, SRC-1283  
**URL references:** None independently associated  
**Related findings:** FND-02347, FND-02348, FND-02349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02351"></a>
## FND-02351: chesscom.courses.v1.VariationAccessType.VARIATION_ACCESS_TYPE_FULL_ACCESS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIATION_ACCESS_TYPE_FULL_ACCESS = 3;

### Evidence

- **SRC-0312** `research/proto/chesscom/courses/v1/variation_access_type.proto` — [preserved redacted evidence](../evidence/text/81be6f1b643afd4ea0d4cd85b00c659f0f251fcfe6fe7ac96f97d46fe88e363b.proto)
  Character offset 255.

```text
YPE_UNSPECIFIED = 0;
  VARIATION_ACCESS_TYPE_PREVIEWABLE = 1;
  VARIATION_ACCESS_TYPE_LOCKED = 2;
  VARIATION_ACCESS_TYPE_FULL_ACCESS = 3;
}

```

**Source references:** SRC-0312, SRC-1283  
**URL references:** None independently associated  
**Related findings:** FND-02347, FND-02348, FND-02349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02352"></a>
## FND-02352: message declaration: chesscom.courses.v1alpha.CourseDeviation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseDeviation {

### Evidence

- **SRC-0313** `research/proto/chesscom/courses/v1alpha/course_deviation.proto` — [preserved redacted evidence](../evidence/text/61590f148a888a367c984cb2b603d375f43dce2e1de17b4b767a247f3da62370.proto)
  Character offset 113.

```text
esscom/courses/v1alpha/course_deviation.proto
// syntax: proto3

package chesscom.courses.v1alpha;

message CourseDeviation {
  repeated string correct_line = 1;
  optional .chesscom.chess.v1.Arrow correct_line_move_arrow = 2;
  optional string variation_url = 3;
  optional int32 ply = 4;
  optional string course_url = 5;
  optional string course_name = 6;
  optional string thumbnail_url = 7;
  optional string author
```

**Source references:** SRC-0313, SRC-1284  
**URL references:** None independently associated  
**Related findings:** FND-02353, FND-02354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02353"></a>
## FND-02353: chesscom.courses.v1alpha.CourseDeviation.correct_line = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string correct_line = 1;

### Evidence

- **SRC-0313** `research/proto/chesscom/courses/v1alpha/course_deviation.proto` — [preserved redacted evidence](../evidence/text/61590f148a888a367c984cb2b603d375f43dce2e1de17b4b767a247f3da62370.proto)
  Character offset 141.

```text
e_deviation.proto
// syntax: proto3

package chesscom.courses.v1alpha;

message CourseDeviation {
  repeated string correct_line = 1;
  optional .chesscom.chess.v1.Arrow correct_line_move_arrow = 2;
  optional string variation_url = 3;
  optional int32 ply = 4;
  optional string course_url = 5;
  optional string course_name = 6;
  optional string thumbnail_url = 7;
  optional string author_name = 8;
  optional string
```

**Source references:** SRC-0313, SRC-1284  
**URL references:** None independently associated  
**Related findings:** FND-02352, FND-02354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02354"></a>
## FND-02354: chesscom.courses.v1alpha.CourseDeviation.correct_line_move_arrow = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Arrow correct_line_move_arrow = 2;

### Evidence

- **SRC-0313** `research/proto/chesscom/courses/v1alpha/course_deviation.proto` — [preserved redacted evidence](../evidence/text/61590f148a888a367c984cb2b603d375f43dce2e1de17b4b767a247f3da62370.proto)
  Character offset 177.

```text

package chesscom.courses.v1alpha;

message CourseDeviation {
  repeated string correct_line = 1;
  optional .chesscom.chess.v1.Arrow correct_line_move_arrow = 2;
  optional string variation_url = 3;
  optional int32 ply = 4;
  optional string course_url = 5;
  optional string course_name = 6;
  optional string thumbnail_url = 7;
  optional string author_name = 8;
  optional string fen_in_course = 9;
  optional strin
```

**Source references:** SRC-0313, SRC-1284  
**URL references:** None independently associated  
**Related findings:** FND-02352, FND-02353

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02355"></a>
## FND-02355: chesscom.courses.v1alpha.CourseDeviation.variation_url = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string variation_url = 3;

### Evidence

- **SRC-0313** `research/proto/chesscom/courses/v1alpha/course_deviation.proto` — [preserved redacted evidence](../evidence/text/61590f148a888a367c984cb2b603d375f43dce2e1de17b4b767a247f3da62370.proto)
  Character offset 242.

```text
epeated string correct_line = 1;
  optional .chesscom.chess.v1.Arrow correct_line_move_arrow = 2;
  optional string variation_url = 3;
  optional int32 ply = 4;
  optional string course_url = 5;
  optional string course_name = 6;
  optional string thumbnail_url = 7;
  optional string author_name = 8;
  optional string fen_in_course = 9;
  optional string fen_deviated = 10;
}

```

**Source references:** SRC-0313, SRC-1284  
**URL references:** None independently associated  
**Related findings:** FND-02352, FND-02353, FND-02354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02356"></a>
## FND-02356: chesscom.courses.v1alpha.CourseDeviation.ply = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 ply = 4;

### Evidence

- **SRC-0313** `research/proto/chesscom/courses/v1alpha/course_deviation.proto` — [preserved redacted evidence](../evidence/text/61590f148a888a367c984cb2b603d375f43dce2e1de17b4b767a247f3da62370.proto)
  Character offset 279.

```text
tional .chesscom.chess.v1.Arrow correct_line_move_arrow = 2;
  optional string variation_url = 3;
  optional int32 ply = 4;
  optional string course_url = 5;
  optional string course_name = 6;
  optional string thumbnail_url = 7;
  optional string author_name = 8;
  optional string fen_in_course = 9;
  optional string fen_deviated = 10;
}

```

**Source references:** SRC-0313, SRC-1284  
**URL references:** None independently associated  
**Related findings:** FND-02352, FND-02353, FND-02354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02357"></a>
## FND-02357: chesscom.courses.v1alpha.CourseDeviation.course_url = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_url = 5;

### Evidence

- **SRC-0313** `research/proto/chesscom/courses/v1alpha/course_deviation.proto` — [preserved redacted evidence](../evidence/text/61590f148a888a367c984cb2b603d375f43dce2e1de17b4b767a247f3da62370.proto)
  Character offset 305.

```text
Arrow correct_line_move_arrow = 2;
  optional string variation_url = 3;
  optional int32 ply = 4;
  optional string course_url = 5;
  optional string course_name = 6;
  optional string thumbnail_url = 7;
  optional string author_name = 8;
  optional string fen_in_course = 9;
  optional string fen_deviated = 10;
}

```

**Source references:** SRC-0313, SRC-1284  
**URL references:** None independently associated  
**Related findings:** FND-02352, FND-02353, FND-02354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02358"></a>
## FND-02358: chesscom.courses.v1alpha.CourseDeviation.course_name = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_name = 6;

### Evidence

- **SRC-0313** `research/proto/chesscom/courses/v1alpha/course_deviation.proto` — [preserved redacted evidence](../evidence/text/61590f148a888a367c984cb2b603d375f43dce2e1de17b4b767a247f3da62370.proto)
  Character offset 339.

```text

  optional string variation_url = 3;
  optional int32 ply = 4;
  optional string course_url = 5;
  optional string course_name = 6;
  optional string thumbnail_url = 7;
  optional string author_name = 8;
  optional string fen_in_course = 9;
  optional string fen_deviated = 10;
}

```

**Source references:** SRC-0313, SRC-1284  
**URL references:** None independently associated  
**Related findings:** FND-02352, FND-02353, FND-02354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02359"></a>
## FND-02359: chesscom.courses.v1alpha.CourseDeviation.thumbnail_url = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string thumbnail_url = 7;

### Evidence

- **SRC-0313** `research/proto/chesscom/courses/v1alpha/course_deviation.proto` — [preserved redacted evidence](../evidence/text/61590f148a888a367c984cb2b603d375f43dce2e1de17b4b767a247f3da62370.proto)
  Character offset 374.

```text
3;
  optional int32 ply = 4;
  optional string course_url = 5;
  optional string course_name = 6;
  optional string thumbnail_url = 7;
  optional string author_name = 8;
  optional string fen_in_course = 9;
  optional string fen_deviated = 10;
}

```

**Source references:** SRC-0313, SRC-1284  
**URL references:** None independently associated  
**Related findings:** FND-02352, FND-02353, FND-02354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02360"></a>
## FND-02360: chesscom.courses.v1alpha.CourseDeviation.author_name = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string author_name = 8;

### Evidence

- **SRC-0313** `research/proto/chesscom/courses/v1alpha/course_deviation.proto` — [preserved redacted evidence](../evidence/text/61590f148a888a367c984cb2b603d375f43dce2e1de17b4b767a247f3da62370.proto)
  Character offset 411.

```text
al string course_url = 5;
  optional string course_name = 6;
  optional string thumbnail_url = 7;
  optional string author_name = 8;
  optional string fen_in_course = 9;
  optional string fen_deviated = 10;
}

```

**Source references:** SRC-0313, SRC-1284  
**URL references:** None independently associated  
**Related findings:** FND-02352, FND-02353, FND-02354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02361"></a>
## FND-02361: chesscom.courses.v1alpha.CourseDeviation.fen_in_course = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string fen_in_course = 9;

### Evidence

- **SRC-0313** `research/proto/chesscom/courses/v1alpha/course_deviation.proto` — [preserved redacted evidence](../evidence/text/61590f148a888a367c984cb2b603d375f43dce2e1de17b4b767a247f3da62370.proto)
  Character offset 446.

```text
l string course_name = 6;
  optional string thumbnail_url = 7;
  optional string author_name = 8;
  optional string fen_in_course = 9;
  optional string fen_deviated = 10;
}

```

**Source references:** SRC-0313, SRC-1284  
**URL references:** None independently associated  
**Related findings:** FND-02352, FND-02353, FND-02354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02362"></a>
## FND-02362: chesscom.courses.v1alpha.CourseDeviation.fen_deviated = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string fen_deviated = 10;

### Evidence

- **SRC-0313** `research/proto/chesscom/courses/v1alpha/course_deviation.proto` — [preserved redacted evidence](../evidence/text/61590f148a888a367c984cb2b603d375f43dce2e1de17b4b767a247f3da62370.proto)
  Character offset 483.

```text
string thumbnail_url = 7;
  optional string author_name = 8;
  optional string fen_in_course = 9;
  optional string fen_deviated = 10;
}

```

**Source references:** SRC-0313, SRC-1284  
**URL references:** None independently associated  
**Related findings:** FND-02352, FND-02353, FND-02354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02363"></a>
## FND-02363: message declaration: chesscom.courses.v1alpha.GetCourseDeviationsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseDeviationsRequest {

### Evidence

- **SRC-0314** `research/proto/chesscom/courses/v1alpha/course_deviations_service.proto` — [preserved redacted evidence](../evidence/text/e761cbc7e9042efe4f6743ded7148678037fa32395f2ef60c244d376c65ef8c7.proto)
  Character offset 122.

```text
urses/v1alpha/course_deviations_service.proto
// syntax: proto3

package chesscom.courses.v1alpha;

message GetCourseDeviationsRequest {
  optional .chesscom.chess.v1.Color color = 1;
  repeated string fens = 2;
}

message GetCourseDeviationsResponse {
  repeated .chesscom.courses.v1alpha.CourseDeviation deviations = 1;
}

```

**Source references:** SRC-0314, SRC-1285  
**URL references:** None independently associated  
**Related findings:** FND-02364, FND-02365

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02364"></a>
## FND-02364: chesscom.courses.v1alpha.GetCourseDeviationsRequest.color = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Color color = 1;

### Evidence

- **SRC-0314** `research/proto/chesscom/courses/v1alpha/course_deviations_service.proto` — [preserved redacted evidence](../evidence/text/e761cbc7e9042efe4f6743ded7148678037fa32395f2ef60c244d376c65ef8c7.proto)
  Character offset 161.

```text
.proto
// syntax: proto3

package chesscom.courses.v1alpha;

message GetCourseDeviationsRequest {
  optional .chesscom.chess.v1.Color color = 1;
  repeated string fens = 2;
}

message GetCourseDeviationsResponse {
  repeated .chesscom.courses.v1alpha.CourseDeviation deviations = 1;
}

```

**Source references:** SRC-0314, SRC-1285  
**URL references:** None independently associated  
**Related findings:** FND-02363, FND-02365

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02365"></a>
## FND-02365: chesscom.courses.v1alpha.GetCourseDeviationsRequest.fens = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string fens = 2;

### Evidence

- **SRC-0314** `research/proto/chesscom/courses/v1alpha/course_deviations_service.proto` — [preserved redacted evidence](../evidence/text/e761cbc7e9042efe4f6743ded7148678037fa32395f2ef60c244d376c65ef8c7.proto)
  Character offset 208.

```text
ses.v1alpha;

message GetCourseDeviationsRequest {
  optional .chesscom.chess.v1.Color color = 1;
  repeated string fens = 2;
}

message GetCourseDeviationsResponse {
  repeated .chesscom.courses.v1alpha.CourseDeviation deviations = 1;
}

```

**Source references:** SRC-0314, SRC-1285  
**URL references:** None independently associated  
**Related findings:** FND-02363, FND-02364

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02366"></a>
## FND-02366: message declaration: chesscom.courses.v1alpha.GetCourseDeviationsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseDeviationsResponse {

### Evidence

- **SRC-0314** `research/proto/chesscom/courses/v1alpha/course_deviations_service.proto` — [preserved redacted evidence](../evidence/text/e761cbc7e9042efe4f6743ded7148678037fa32395f2ef60c244d376c65ef8c7.proto)
  Character offset 237.

```text
seDeviationsRequest {
  optional .chesscom.chess.v1.Color color = 1;
  repeated string fens = 2;
}

message GetCourseDeviationsResponse {
  repeated .chesscom.courses.v1alpha.CourseDeviation deviations = 1;
}

```

**Source references:** SRC-0314, SRC-1285  
**URL references:** None independently associated  
**Related findings:** FND-02363, FND-02364, FND-02365

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02367"></a>
## FND-02367: chesscom.courses.v1alpha.GetCourseDeviationsResponse.deviations = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1alpha.CourseDeviation deviations = 1;

### Evidence

- **SRC-0314** `research/proto/chesscom/courses/v1alpha/course_deviations_service.proto` — [preserved redacted evidence](../evidence/text/e761cbc7e9042efe4f6743ded7148678037fa32395f2ef60c244d376c65ef8c7.proto)
  Character offset 277.

```text
om.chess.v1.Color color = 1;
  repeated string fens = 2;
}

message GetCourseDeviationsResponse {
  repeated .chesscom.courses.v1alpha.CourseDeviation deviations = 1;
}

```

**Source references:** SRC-0314, SRC-1285  
**URL references:** None independently associated  
**Related findings:** FND-02363, FND-02364, FND-02365

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02368"></a>
## FND-02368: message declaration: chesscom.courses_common.v1.CourseBoardPreview

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseBoardPreview {

### Evidence

- **SRC-0315** `research/proto/chesscom/courses_common/v1/course_board_preview.proto` — [preserved redacted evidence](../evidence/text/bb78e2133ee25d81cf1c907f9325b0d20b3140a43b3c58c206b6a105752faa6a.proto)
  Character offset 121.

```text
ourses_common/v1/course_board_preview.proto
// syntax: proto3

package chesscom.courses_common.v1;

message CourseBoardPreview {
  oneof _crop_size {
  int32 crop_size = 2;
  }
  optional .chesscom.chess.v1.Square start_square = 1;
}

```

**Source references:** SRC-0315, SRC-1286  
**URL references:** None independently associated  
**Related findings:** FND-02369, FND-02370

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02369"></a>
## FND-02369: oneof declaration: chesscom.courses_common.v1.CourseBoardPreview._crop_size

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _crop_size {

### Evidence

- **SRC-0315** `research/proto/chesscom/courses_common/v1/course_board_preview.proto` — [preserved redacted evidence](../evidence/text/bb78e2133ee25d81cf1c907f9325b0d20b3140a43b3c58c206b6a105752faa6a.proto)
  Character offset 152.

```text
review.proto
// syntax: proto3

package chesscom.courses_common.v1;

message CourseBoardPreview {
  oneof _crop_size {
  int32 crop_size = 2;
  }
  optional .chesscom.chess.v1.Square start_square = 1;
}

```

**Source references:** SRC-0315, SRC-1286  
**URL references:** None independently associated  
**Related findings:** FND-02368, FND-02370

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02370"></a>
## FND-02370: chesscom.courses_common.v1.CourseBoardPreview.crop_size = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 crop_size = 2;

### Evidence

- **SRC-0315** `research/proto/chesscom/courses_common/v1/course_board_preview.proto` — [preserved redacted evidence](../evidence/text/bb78e2133ee25d81cf1c907f9325b0d20b3140a43b3c58c206b6a105752faa6a.proto)
  Character offset 173.

```text
x: proto3

package chesscom.courses_common.v1;

message CourseBoardPreview {
  oneof _crop_size {
  int32 crop_size = 2;
  }
  optional .chesscom.chess.v1.Square start_square = 1;
}

```

**Source references:** SRC-0315, SRC-1286  
**URL references:** None independently associated  
**Related findings:** FND-02368, FND-02369

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02371"></a>
## FND-02371: chesscom.courses_common.v1.CourseBoardPreview.start_square = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square start_square = 1;

### Evidence

- **SRC-0315** `research/proto/chesscom/courses_common/v1/course_board_preview.proto` — [preserved redacted evidence](../evidence/text/bb78e2133ee25d81cf1c907f9325b0d20b3140a43b3c58c206b6a105752faa6a.proto)
  Character offset 200.

```text
.courses_common.v1;

message CourseBoardPreview {
  oneof _crop_size {
  int32 crop_size = 2;
  }
  optional .chesscom.chess.v1.Square start_square = 1;
}

```

**Source references:** SRC-0315, SRC-1286  
**URL references:** None independently associated  
**Related findings:** FND-02368, FND-02369, FND-02370

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02372"></a>
## FND-02372: message declaration: chesscom.courses_common.v1.CourseChapterStats

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseChapterStats {

### Evidence

- **SRC-0316** `research/proto/chesscom/courses_common/v1/course_chapter_stats.proto` — [preserved redacted evidence](../evidence/text/4641142454a7008c3c5b1c72b8c9e47a004ea12ce4ae9efc63572d227a9827cb.proto)
  Character offset 121.

```text
ourses_common/v1/course_chapter_stats.proto
// syntax: proto3

package chesscom.courses_common.v1;

message CourseChapterStats {
  optional int32 trainable_variations = 1;
  optional int32 informational_variations = 2;
  optional int32 quickstarter_variations = 3;
  optional int32 alternative_variations = 4;
  optional int32 puzzles = 5;
  optional float average_training_depth = 6;
  optional int32 paid_video_minutes
```

**Source references:** SRC-0316, SRC-1287  
**URL references:** None independently associated  
**Related findings:** FND-02373, FND-02374

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02373"></a>
## FND-02373: chesscom.courses_common.v1.CourseChapterStats.trainable_variations = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 trainable_variations = 1;

### Evidence

- **SRC-0316** `research/proto/chesscom/courses_common/v1/course_chapter_stats.proto` — [preserved redacted evidence](../evidence/text/4641142454a7008c3c5b1c72b8c9e47a004ea12ce4ae9efc63572d227a9827cb.proto)
  Character offset 152.

```text
_stats.proto
// syntax: proto3

package chesscom.courses_common.v1;

message CourseChapterStats {
  optional int32 trainable_variations = 1;
  optional int32 informational_variations = 2;
  optional int32 quickstarter_variations = 3;
  optional int32 alternative_variations = 4;
  optional int32 puzzles = 5;
  optional float average_training_depth = 6;
  optional int32 paid_video_minutes = 7;
}

```

**Source references:** SRC-0316, SRC-1287  
**URL references:** None independently associated  
**Related findings:** FND-02372, FND-02374

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02374"></a>
## FND-02374: chesscom.courses_common.v1.CourseChapterStats.informational_variations = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 informational_variations = 2;

### Evidence

- **SRC-0316** `research/proto/chesscom/courses_common/v1/course_chapter_stats.proto` — [preserved redacted evidence](../evidence/text/4641142454a7008c3c5b1c72b8c9e47a004ea12ce4ae9efc63572d227a9827cb.proto)
  Character offset 195.

```text
sscom.courses_common.v1;

message CourseChapterStats {
  optional int32 trainable_variations = 1;
  optional int32 informational_variations = 2;
  optional int32 quickstarter_variations = 3;
  optional int32 alternative_variations = 4;
  optional int32 puzzles = 5;
  optional float average_training_depth = 6;
  optional int32 paid_video_minutes = 7;
}

```

**Source references:** SRC-0316, SRC-1287  
**URL references:** None independently associated  
**Related findings:** FND-02372, FND-02373

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
