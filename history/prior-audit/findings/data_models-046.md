# data_models — findings 4501–4600

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-04775"></a>
## FND-04775: chesscom.friends_search.v1.FriendsSearchFriend.ratings = 90

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.friends_search.v1.FriendsSearchRatingItem ratings = 90;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6039.

```text
ng = 7;
  optional bool is_requestor_friend = 8;
  optional .chesscom.api.v1.Country country = 9;
  repeated .chesscom.friends_search.v1.FriendsSearchRatingItem ratings = 90;
}

message FriendsSearchRecommendation {
  optional string uuid = 1;
  optional .chesscom.user.v1.UserView user_view = 2;
  optional .chesscom.api.v1.Country country = 3;
  optional int32 best_rating = 4;
  repeated .chesscom.friends_search.v1.F
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04776"></a>
## FND-04776: message declaration: chesscom.friends_search.v1.FriendsSearchRecommendation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FriendsSearchRecommendation {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6117.

```text
ountry country = 9;
  repeated .chesscom.friends_search.v1.FriendsSearchRatingItem ratings = 90;
}

message FriendsSearchRecommendation {
  optional string uuid = 1;
  optional .chesscom.user.v1.UserView user_view = 2;
  optional .chesscom.api.v1.Country country = 3;
  optional int32 best_rating = 4;
  repeated .chesscom.friends_search.v1.FriendsSearchRatingItem ratings = 5;
  optional .chesscom.friends_search.v1.Fri
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04777"></a>
## FND-04777: chesscom.friends_search.v1.FriendsSearchRecommendation.uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string uuid = 1;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 5723.

```text
  .chesscom.friends_search.v1.FriendRequestDirection requestor_friend_request_direction = 10;
  }
  optional string uuid = 1;
  optional .chesscom.user.v1.UserView user_view = 2;
  optional bool is_staff = 5;
  optional .chesscom.friends_search.v1.FriendsSearchPresenceStatus presence = 6;
  optional int32 best_rating = 7;
  optional bool is_requestor_friend = 8;
  optional .chesscom.api.v1.Country country = 9;
  repe
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04778"></a>
## FND-04778: chesscom.friends_search.v1.FriendsSearchRecommendation.user_view = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user.v1.UserView user_view = 2;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 5751.

```text
1.FriendRequestDirection requestor_friend_request_direction = 10;
  }
  optional string uuid = 1;
  optional .chesscom.user.v1.UserView user_view = 2;
  optional bool is_staff = 5;
  optional .chesscom.friends_search.v1.FriendsSearchPresenceStatus presence = 6;
  optional int32 best_rating = 7;
  optional bool is_requestor_friend = 8;
  optional .chesscom.api.v1.Country country = 9;
  repeated .chesscom.friends_searc
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04779"></a>
## FND-04779: chesscom.friends_search.v1.FriendsSearchRecommendation.country = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Country country = 3;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6238.

```text
Recommendation {
  optional string uuid = 1;
  optional .chesscom.user.v1.UserView user_view = 2;
  optional .chesscom.api.v1.Country country = 3;
  optional int32 best_rating = 4;
  repeated .chesscom.friends_search.v1.FriendsSearchRatingItem ratings = 5;
  optional .chesscom.friends_search.v1.FriendsSearchPresenceStatus presence = 6;
  optional bool is_staff = 7;
  optional int32 rank = 8;
  optional double score =
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04780"></a>
## FND-04780: chesscom.friends_search.v1.FriendsSearchRecommendation.best_rating = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 best_rating = 4;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6287.

```text
tional .chesscom.user.v1.UserView user_view = 2;
  optional .chesscom.api.v1.Country country = 3;
  optional int32 best_rating = 4;
  repeated .chesscom.friends_search.v1.FriendsSearchRatingItem ratings = 5;
  optional .chesscom.friends_search.v1.FriendsSearchPresenceStatus presence = 6;
  optional bool is_staff = 7;
  optional int32 rank = 8;
  optional double score = 9;
  optional string reason = 10;
}

message Soc
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04781"></a>
## FND-04781: chesscom.friends_search.v1.FriendsSearchRecommendation.ratings = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.friends_search.v1.FriendsSearchRatingItem ratings = 5;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6321.

```text
user_view = 2;
  optional .chesscom.api.v1.Country country = 3;
  optional int32 best_rating = 4;
  repeated .chesscom.friends_search.v1.FriendsSearchRatingItem ratings = 5;
  optional .chesscom.friends_search.v1.FriendsSearchPresenceStatus presence = 6;
  optional bool is_staff = 7;
  optional int32 rank = 8;
  optional double score = 9;
  optional string reason = 10;
}

message SocialFriendsSearchFriend {
  optiona
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04782"></a>
## FND-04782: chesscom.friends_search.v1.FriendsSearchRecommendation.presence = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.friends_search.v1.FriendsSearchPresenceStatus presence = 6;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 5834.

```text
ring uuid = 1;
  optional .chesscom.user.v1.UserView user_view = 2;
  optional bool is_staff = 5;
  optional .chesscom.friends_search.v1.FriendsSearchPresenceStatus presence = 6;
  optional int32 best_rating = 7;
  optional bool is_requestor_friend = 8;
  optional .chesscom.api.v1.Country country = 9;
  repeated .chesscom.friends_search.v1.FriendsSearchRatingItem ratings = 90;
}

message FriendsSearchRecommendation {
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04783"></a>
## FND-04783: chesscom.friends_search.v1.FriendsSearchRecommendation.is_staff = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_staff = 7;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6478.

```text
tem ratings = 5;
  optional .chesscom.friends_search.v1.FriendsSearchPresenceStatus presence = 6;
  optional bool is_staff = 7;
  optional int32 rank = 8;
  optional double score = 9;
  optional string reason = 10;
}

message SocialFriendsSearchFriend {
  optional .chesscom.friends_search.v1.FriendsSearchFriend friend = 1;
  optional bool allows_challenges = 2;
  optional bool allows_messages = 3;
  optional .chessco
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04784"></a>
## FND-04784: chesscom.friends_search.v1.FriendsSearchRecommendation.rank = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 rank = 8;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6508.

```text
hesscom.friends_search.v1.FriendsSearchPresenceStatus presence = 6;
  optional bool is_staff = 7;
  optional int32 rank = 8;
  optional double score = 9;
  optional string reason = 10;
}

message SocialFriendsSearchFriend {
  optional .chesscom.friends_search.v1.FriendsSearchFriend friend = 1;
  optional bool allows_challenges = 2;
  optional bool allows_messages = 3;
  optional .chesscom.presence.v1.UserPresence ful
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04785"></a>
## FND-04785: chesscom.friends_search.v1.FriendsSearchRecommendation.score = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double score = 9;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6535.

```text
riendsSearchPresenceStatus presence = 6;
  optional bool is_staff = 7;
  optional int32 rank = 8;
  optional double score = 9;
  optional string reason = 10;
}

message SocialFriendsSearchFriend {
  optional .chesscom.friends_search.v1.FriendsSearchFriend friend = 1;
  optional bool allows_challenges = 2;
  optional bool allows_messages = 3;
  optional .chesscom.presence.v1.UserPresence full_presence = 4;
}

message 
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04786"></a>
## FND-04786: chesscom.friends_search.v1.FriendsSearchRecommendation.reason = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string reason = 10;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6564.

```text
esence = 6;
  optional bool is_staff = 7;
  optional int32 rank = 8;
  optional double score = 9;
  optional string reason = 10;
}

message SocialFriendsSearchFriend {
  optional .chesscom.friends_search.v1.FriendsSearchFriend friend = 1;
  optional bool allows_challenges = 2;
  optional bool allows_messages = 3;
  optional .chesscom.presence.v1.UserPresence full_presence = 4;
}

message PendingFriendsSearchFriend {

```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04787"></a>
## FND-04787: message declaration: chesscom.friends_search.v1.SocialFriendsSearchFriend

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SocialFriendsSearchFriend {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6596.

```text
taff = 7;
  optional int32 rank = 8;
  optional double score = 9;
  optional string reason = 10;
}

message SocialFriendsSearchFriend {
  optional .chesscom.friends_search.v1.FriendsSearchFriend friend = 1;
  optional bool allows_challenges = 2;
  optional bool allows_messages = 3;
  optional .chesscom.presence.v1.UserPresence full_presence = 4;
}

message PendingFriendsSearchFriend {
  optional .chesscom.friends_sea
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04788"></a>
## FND-04788: chesscom.friends_search.v1.SocialFriendsSearchFriend.friend = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.friends_search.v1.FriendsSearchFriend friend = 1;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6634.

```text
 optional double score = 9;
  optional string reason = 10;
}

message SocialFriendsSearchFriend {
  optional .chesscom.friends_search.v1.FriendsSearchFriend friend = 1;
  optional bool allows_challenges = 2;
  optional bool allows_messages = 3;
  optional .chesscom.presence.v1.UserPresence full_presence = 4;
}

message PendingFriendsSearchFriend {
  optional .chesscom.friends_search.v1.SocialFriendsSearchFriend frien
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04789"></a>
## FND-04789: chesscom.friends_search.v1.SocialFriendsSearchFriend.allows_challenges = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool allows_challenges = 2;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6705.

```text
ocialFriendsSearchFriend {
  optional .chesscom.friends_search.v1.FriendsSearchFriend friend = 1;
  optional bool allows_challenges = 2;
  optional bool allows_messages = 3;
  optional .chesscom.presence.v1.UserPresence full_presence = 4;
}

message PendingFriendsSearchFriend {
  optional .chesscom.friends_search.v1.SocialFriendsSearchFriend friend = 1;
  optional bool is_incoming_request = 2;
}

message FriendsSearc
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04790"></a>
## FND-04790: chesscom.friends_search.v1.SocialFriendsSearchFriend.allows_messages = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool allows_messages = 3;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6744.

```text
chesscom.friends_search.v1.FriendsSearchFriend friend = 1;
  optional bool allows_challenges = 2;
  optional bool allows_messages = 3;
  optional .chesscom.presence.v1.UserPresence full_presence = 4;
}

message PendingFriendsSearchFriend {
  optional .chesscom.friends_search.v1.SocialFriendsSearchFriend friend = 1;
  optional bool is_incoming_request = 2;
}

message FriendsSearchFriendship {
  optional .google.protob
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04791"></a>
## FND-04791: chesscom.friends_search.v1.SocialFriendsSearchFriend.full_presence = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.presence.v1.UserPresence full_presence = 4;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6781.

```text
rchFriend friend = 1;
  optional bool allows_challenges = 2;
  optional bool allows_messages = 3;
  optional .chesscom.presence.v1.UserPresence full_presence = 4;
}

message PendingFriendsSearchFriend {
  optional .chesscom.friends_search.v1.SocialFriendsSearchFriend friend = 1;
  optional bool is_incoming_request = 2;
}

message FriendsSearchFriendship {
  optional .google.protobuf.Timestamp created_at = 1;
  option
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04792"></a>
## FND-04792: message declaration: chesscom.friends_search.v1.PendingFriendsSearchFriend

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PendingFriendsSearchFriend {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6847.

```text
ional bool allows_messages = 3;
  optional .chesscom.presence.v1.UserPresence full_presence = 4;
}

message PendingFriendsSearchFriend {
  optional .chesscom.friends_search.v1.SocialFriendsSearchFriend friend = 1;
  optional bool is_incoming_request = 2;
}

message FriendsSearchFriendship {
  optional .google.protobuf.Timestamp created_at = 1;
  optional string friend_uuid = 2;
}

message FriendsSearchRatingItem {
  
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04793"></a>
## FND-04793: chesscom.friends_search.v1.PendingFriendsSearchFriend.friend = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.friends_search.v1.SocialFriendsSearchFriend friend = 1;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6886.

```text
nal .chesscom.presence.v1.UserPresence full_presence = 4;
}

message PendingFriendsSearchFriend {
  optional .chesscom.friends_search.v1.SocialFriendsSearchFriend friend = 1;
  optional bool is_incoming_request = 2;
}

message FriendsSearchFriendship {
  optional .google.protobuf.Timestamp created_at = 1;
  optional string friend_uuid = 2;
}

message FriendsSearchRatingItem {
  optional .chesscom.friends_search.v1.Fr
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04794"></a>
## FND-04794: chesscom.friends_search.v1.PendingFriendsSearchFriend.is_incoming_request = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_incoming_request = 2;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 6963.

```text
riendsSearchFriend {
  optional .chesscom.friends_search.v1.SocialFriendsSearchFriend friend = 1;
  optional bool is_incoming_request = 2;
}

message FriendsSearchFriendship {
  optional .google.protobuf.Timestamp created_at = 1;
  optional string friend_uuid = 2;
}

message FriendsSearchRatingItem {
  optional .chesscom.friends_search.v1.FriendsSearchVariantTimeclass variant_timeclass = 1;
  optional int32 rating = 
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04795"></a>
## FND-04795: message declaration: chesscom.friends_search.v1.FriendsSearchFriendship

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FriendsSearchFriendship {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7005.

```text
friends_search.v1.SocialFriendsSearchFriend friend = 1;
  optional bool is_incoming_request = 2;
}

message FriendsSearchFriendship {
  optional .google.protobuf.Timestamp created_at = 1;
  optional string friend_uuid = 2;
}

message FriendsSearchRatingItem {
  optional .chesscom.friends_search.v1.FriendsSearchVariantTimeclass variant_timeclass = 1;
  optional int32 rating = 2;
}

message FriendsSearchOrderBy {
  one
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04796"></a>
## FND-04796: chesscom.friends_search.v1.FriendsSearchFriendship.created_at = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp created_at = 1;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7041.

```text
hFriend friend = 1;
  optional bool is_incoming_request = 2;
}

message FriendsSearchFriendship {
  optional .google.protobuf.Timestamp created_at = 1;
  optional string friend_uuid = 2;
}

message FriendsSearchRatingItem {
  optional .chesscom.friends_search.v1.FriendsSearchVariantTimeclass variant_timeclass = 1;
  optional int32 rating = 2;
}

message FriendsSearchOrderBy {
  oneof _order {
  .chesscom.friends_sear
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04797"></a>
## FND-04797: chesscom.friends_search.v1.FriendsSearchFriendship.friend_uuid = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string friend_uuid = 2;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7095.

```text
t = 2;
}

message FriendsSearchFriendship {
  optional .google.protobuf.Timestamp created_at = 1;
  optional string friend_uuid = 2;
}

message FriendsSearchRatingItem {
  optional .chesscom.friends_search.v1.FriendsSearchVariantTimeclass variant_timeclass = 1;
  optional int32 rating = 2;
}

message FriendsSearchOrderBy {
  oneof _order {
  .chesscom.friends_search.v1.FriendsSearchOrder order = 2;
  }
  optional .ch
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04798"></a>
## FND-04798: message declaration: chesscom.friends_search.v1.FriendsSearchRatingItem

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FriendsSearchRatingItem {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7131.

```text
dship {
  optional .google.protobuf.Timestamp created_at = 1;
  optional string friend_uuid = 2;
}

message FriendsSearchRatingItem {
  optional .chesscom.friends_search.v1.FriendsSearchVariantTimeclass variant_timeclass = 1;
  optional int32 rating = 2;
}

message FriendsSearchOrderBy {
  oneof _order {
  .chesscom.friends_search.v1.FriendsSearchOrder order = 2;
  }
  optional .chesscom.friends_search.v1.FriendsSear
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04799"></a>
## FND-04799: chesscom.friends_search.v1.FriendsSearchRatingItem.variant_timeclass = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.friends_search.v1.FriendsSearchVariantTimeclass variant_timeclass = 1;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7167.

```text
Timestamp created_at = 1;
  optional string friend_uuid = 2;
}

message FriendsSearchRatingItem {
  optional .chesscom.friends_search.v1.FriendsSearchVariantTimeclass variant_timeclass = 1;
  optional int32 rating = 2;
}

message FriendsSearchOrderBy {
  oneof _order {
  .chesscom.friends_search.v1.FriendsSearchOrder order = 2;
  }
  optional .chesscom.friends_search.v1.FriendsSearchSearchableField field = 1;
}

mess
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04800"></a>
## FND-04800: chesscom.friends_search.v1.FriendsSearchRatingItem.rating = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 rating = 2;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7259.

```text
tem {
  optional .chesscom.friends_search.v1.FriendsSearchVariantTimeclass variant_timeclass = 1;
  optional int32 rating = 2;
}

message FriendsSearchOrderBy {
  oneof _order {
  .chesscom.friends_search.v1.FriendsSearchOrder order = 2;
  }
  optional .chesscom.friends_search.v1.FriendsSearchSearchableField field = 1;
}

message FriendsSearchCursorToken {
  oneof _how_many_pages {
  int32 how_many_pages = 3;
  }
  o
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04801"></a>
## FND-04801: message declaration: chesscom.friends_search.v1.FriendsSearchOrderBy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FriendsSearchOrderBy {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7289.

```text
ends_search.v1.FriendsSearchVariantTimeclass variant_timeclass = 1;
  optional int32 rating = 2;
}

message FriendsSearchOrderBy {
  oneof _order {
  .chesscom.friends_search.v1.FriendsSearchOrder order = 2;
  }
  optional .chesscom.friends_search.v1.FriendsSearchSearchableField field = 1;
}

message FriendsSearchCursorToken {
  oneof _how_many_pages {
  int32 how_many_pages = 3;
  }
  oneof _total_elements {
  int64
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04802"></a>
## FND-04802: oneof declaration: chesscom.friends_search.v1.FriendsSearchOrderBy._order

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _order {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7322.

```text
ntTimeclass variant_timeclass = 1;
  optional int32 rating = 2;
}

message FriendsSearchOrderBy {
  oneof _order {
  .chesscom.friends_search.v1.FriendsSearchOrder order = 2;
  }
  optional .chesscom.friends_search.v1.FriendsSearchSearchableField field = 1;
}

message FriendsSearchCursorToken {
  oneof _how_many_pages {
  int32 how_many_pages = 3;
  }
  oneof _total_elements {
  int64 total_elements = 4;
  }
  option
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04803"></a>
## FND-04803: chesscom.friends_search.v1.FriendsSearchOrderBy.order = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.friends_search.v1.FriendsSearchOrder order = 2;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7339.

```text
nt_timeclass = 1;
  optional int32 rating = 2;
}

message FriendsSearchOrderBy {
  oneof _order {
  .chesscom.friends_search.v1.FriendsSearchOrder order = 2;
  }
  optional .chesscom.friends_search.v1.FriendsSearchSearchableField field = 1;
}

message FriendsSearchCursorToken {
  oneof _how_many_pages {
  int32 how_many_pages = 3;
  }
  oneof _total_elements {
  int64 total_elements = 4;
  }
  optional int32 page_num
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04804"></a>
## FND-04804: chesscom.friends_search.v1.FriendsSearchOrderBy.field = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.friends_search.v1.FriendsSearchSearchableField field = 1;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7403.

```text
sSearchOrderBy {
  oneof _order {
  .chesscom.friends_search.v1.FriendsSearchOrder order = 2;
  }
  optional .chesscom.friends_search.v1.FriendsSearchSearchableField field = 1;
}

message FriendsSearchCursorToken {
  oneof _how_many_pages {
  int32 how_many_pages = 3;
  }
  oneof _total_elements {
  int64 total_elements = 4;
  }
  optional int32 page_number = 1;
  optional int32 page_size = 2;
}

message BlockedUsers
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04805"></a>
## FND-04805: message declaration: chesscom.friends_search.v1.FriendsSearchCursorToken

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FriendsSearchCursorToken {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7483.

```text
er order = 2;
  }
  optional .chesscom.friends_search.v1.FriendsSearchSearchableField field = 1;
}

message FriendsSearchCursorToken {
  oneof _how_many_pages {
  int32 how_many_pages = 3;
  }
  oneof _total_elements {
  int64 total_elements = 4;
  }
  optional int32 page_number = 1;
  optional int32 page_size = 2;
}

message BlockedUsers {
  optional string uuid = 1;
  optional int64 legacy_id = 2;
  optional string
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04806"></a>
## FND-04806: oneof declaration: chesscom.friends_search.v1.FriendsSearchCursorToken._how_many_pages

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _how_many_pages {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7520.

```text
m.friends_search.v1.FriendsSearchSearchableField field = 1;
}

message FriendsSearchCursorToken {
  oneof _how_many_pages {
  int32 how_many_pages = 3;
  }
  oneof _total_elements {
  int64 total_elements = 4;
  }
  optional int32 page_number = 1;
  optional int32 page_size = 2;
}

message BlockedUsers {
  optional string uuid = 1;
  optional int64 legacy_id = 2;
  optional string username = 3;
  repeated .chesscom.f
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04807"></a>
## FND-04807: chesscom.friends_search.v1.FriendsSearchCursorToken.how_many_pages = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 how_many_pages = 3;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7546.

```text
sSearchSearchableField field = 1;
}

message FriendsSearchCursorToken {
  oneof _how_many_pages {
  int32 how_many_pages = 3;
  }
  oneof _total_elements {
  int64 total_elements = 4;
  }
  optional int32 page_number = 1;
  optional int32 page_size = 2;
}

message BlockedUsers {
  optional string uuid = 1;
  optional int64 legacy_id = 2;
  optional string username = 3;
  repeated .chesscom.friends_search.v1.FriendsSe
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04808"></a>
## FND-04808: oneof declaration: chesscom.friends_search.v1.FriendsSearchCursorToken._total_elements

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_elements {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7578.

```text
;
}

message FriendsSearchCursorToken {
  oneof _how_many_pages {
  int32 how_many_pages = 3;
  }
  oneof _total_elements {
  int64 total_elements = 4;
  }
  optional int32 page_number = 1;
  optional int32 page_size = 2;
}

message BlockedUsers {
  optional string uuid = 1;
  optional int64 legacy_id = 2;
  optional string username = 3;
  repeated .chesscom.friends_search.v1.FriendsSearchExtraFieldResponse extra_fie
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04809"></a>
## FND-04809: chesscom.friends_search.v1.FriendsSearchCursorToken.total_elements = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 total_elements = 4;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7604.

```text
CursorToken {
  oneof _how_many_pages {
  int32 how_many_pages = 3;
  }
  oneof _total_elements {
  int64 total_elements = 4;
  }
  optional int32 page_number = 1;
  optional int32 page_size = 2;
}

message BlockedUsers {
  optional string uuid = 1;
  optional int64 legacy_id = 2;
  optional string username = 3;
  repeated .chesscom.friends_search.v1.FriendsSearchExtraFieldResponse extra_fields = 4;
}

message Friend
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04810"></a>
## FND-04810: chesscom.friends_search.v1.FriendsSearchCursorToken.page_number = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 page_number = 1;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7636.

```text
pages {
  int32 how_many_pages = 3;
  }
  oneof _total_elements {
  int64 total_elements = 4;
  }
  optional int32 page_number = 1;
  optional int32 page_size = 2;
}

message BlockedUsers {
  optional string uuid = 1;
  optional int64 legacy_id = 2;
  optional string username = 3;
  repeated .chesscom.friends_search.v1.FriendsSearchExtraFieldResponse extra_fields = 4;
}

message FriendsSearchExtraFieldResponse {
  on
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04811"></a>
## FND-04811: chesscom.friends_search.v1.FriendsSearchCursorToken.page_size = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 page_size = 2;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7670.

```text
;
  }
  oneof _total_elements {
  int64 total_elements = 4;
  }
  optional int32 page_number = 1;
  optional int32 page_size = 2;
}

message BlockedUsers {
  optional string uuid = 1;
  optional int64 legacy_id = 2;
  optional string username = 3;
  repeated .chesscom.friends_search.v1.FriendsSearchExtraFieldResponse extra_fields = 4;
}

message FriendsSearchExtraFieldResponse {
  oneof value {
  string string_value 
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04812"></a>
## FND-04812: message declaration: chesscom.friends_search.v1.BlockedUsers

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BlockedUsers {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7703.

```text
 int64 total_elements = 4;
  }
  optional int32 page_number = 1;
  optional int32 page_size = 2;
}

message BlockedUsers {
  optional string uuid = 1;
  optional int64 legacy_id = 2;
  optional string username = 3;
  repeated .chesscom.friends_search.v1.FriendsSearchExtraFieldResponse extra_fields = 4;
}

message FriendsSearchExtraFieldResponse {
  oneof value {
  string string_value = 2;
  int64 long_value = 3;
  in
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04813"></a>
## FND-04813: chesscom.friends_search.v1.BlockedUsers.uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string uuid = 1;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 5723.

```text
  .chesscom.friends_search.v1.FriendRequestDirection requestor_friend_request_direction = 10;
  }
  optional string uuid = 1;
  optional .chesscom.user.v1.UserView user_view = 2;
  optional bool is_staff = 5;
  optional .chesscom.friends_search.v1.FriendsSearchPresenceStatus presence = 6;
  optional int32 best_rating = 7;
  optional bool is_requestor_friend = 8;
  optional .chesscom.api.v1.Country country = 9;
  repe
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04814"></a>
## FND-04814: chesscom.friends_search.v1.BlockedUsers.legacy_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 legacy_id = 2;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7756.

```text
number = 1;
  optional int32 page_size = 2;
}

message BlockedUsers {
  optional string uuid = 1;
  optional int64 legacy_id = 2;
  optional string username = 3;
  repeated .chesscom.friends_search.v1.FriendsSearchExtraFieldResponse extra_fields = 4;
}

message FriendsSearchExtraFieldResponse {
  oneof value {
  string string_value = 2;
  int64 long_value = 3;
  int32 integer_value = 4;
  float float_value = 5;
  dou
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04815"></a>
## FND-04815: chesscom.friends_search.v1.BlockedUsers.username = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string username = 3;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7788.

```text
e_size = 2;
}

message BlockedUsers {
  optional string uuid = 1;
  optional int64 legacy_id = 2;
  optional string username = 3;
  repeated .chesscom.friends_search.v1.FriendsSearchExtraFieldResponse extra_fields = 4;
}

message FriendsSearchExtraFieldResponse {
  oneof value {
  string string_value = 2;
  int64 long_value = 3;
  int32 integer_value = 4;
  float float_value = 5;
  double double_value = 6;
  bool boo
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04816"></a>
## FND-04816: chesscom.friends_search.v1.BlockedUsers.extra_fields = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.friends_search.v1.FriendsSearchExtraFieldResponse extra_fields = 4;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7820.

```text
ers {
  optional string uuid = 1;
  optional int64 legacy_id = 2;
  optional string username = 3;
  repeated .chesscom.friends_search.v1.FriendsSearchExtraFieldResponse extra_fields = 4;
}

message FriendsSearchExtraFieldResponse {
  oneof value {
  string string_value = 2;
  int64 long_value = 3;
  int32 integer_value = 4;
  float float_value = 5;
  double double_value = 6;
  bool bool_value = 7;
  }
  optional .che
```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04817"></a>
## FND-04817: message declaration: chesscom.friends_search.v1.FriendsSearchExtraFieldResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FriendsSearchExtraFieldResponse {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7910.

```text
me = 3;
  repeated .chesscom.friends_search.v1.FriendsSearchExtraFieldResponse extra_fields = 4;
}

message FriendsSearchExtraFieldResponse {
  oneof value {
  string string_value = 2;
  int64 long_value = 3;
  int32 integer_value = 4;
  float float_value = 5;
  double double_value = 6;
  bool bool_value = 7;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRetrievableField field = 1;
}

```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04818"></a>
## FND-04818: oneof declaration: chesscom.friends_search.v1.FriendsSearchExtraFieldResponse.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7954.

```text
v1.FriendsSearchExtraFieldResponse extra_fields = 4;
}

message FriendsSearchExtraFieldResponse {
  oneof value {
  string string_value = 2;
  int64 long_value = 3;
  int32 integer_value = 4;
  float float_value = 5;
  double double_value = 6;
  bool bool_value = 7;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRetrievableField field = 1;
}

```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04819"></a>
## FND-04819: chesscom.friends_search.v1.FriendsSearchExtraFieldResponse.string_value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string string_value = 2;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7970.

```text
ExtraFieldResponse extra_fields = 4;
}

message FriendsSearchExtraFieldResponse {
  oneof value {
  string string_value = 2;
  int64 long_value = 3;
  int32 integer_value = 4;
  float float_value = 5;
  double double_value = 6;
  bool bool_value = 7;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRetrievableField field = 1;
}

```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04820"></a>
## FND-04820: chesscom.friends_search.v1.FriendsSearchExtraFieldResponse.long_value = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 long_value = 3;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 7997.

```text
elds = 4;
}

message FriendsSearchExtraFieldResponse {
  oneof value {
  string string_value = 2;
  int64 long_value = 3;
  int32 integer_value = 4;
  float float_value = 5;
  double double_value = 6;
  bool bool_value = 7;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRetrievableField field = 1;
}

```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04821"></a>
## FND-04821: chesscom.friends_search.v1.FriendsSearchExtraFieldResponse.integer_value = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 integer_value = 4;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 8021.

```text
endsSearchExtraFieldResponse {
  oneof value {
  string string_value = 2;
  int64 long_value = 3;
  int32 integer_value = 4;
  float float_value = 5;
  double double_value = 6;
  bool bool_value = 7;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRetrievableField field = 1;
}

```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04822"></a>
## FND-04822: chesscom.friends_search.v1.FriendsSearchExtraFieldResponse.float_value = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float float_value = 5;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 8048.

```text
e {
  oneof value {
  string string_value = 2;
  int64 long_value = 3;
  int32 integer_value = 4;
  float float_value = 5;
  double double_value = 6;
  bool bool_value = 7;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRetrievableField field = 1;
}

```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04823"></a>
## FND-04823: chesscom.friends_search.v1.FriendsSearchExtraFieldResponse.double_value = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double double_value = 6;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 8073.

```text
ing string_value = 2;
  int64 long_value = 3;
  int32 integer_value = 4;
  float float_value = 5;
  double double_value = 6;
  bool bool_value = 7;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRetrievableField field = 1;
}

```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04824"></a>
## FND-04824: chesscom.friends_search.v1.FriendsSearchExtraFieldResponse.bool_value = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool bool_value = 7;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 8100.

```text
64 long_value = 3;
  int32 integer_value = 4;
  float float_value = 5;
  double double_value = 6;
  bool bool_value = 7;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRetrievableField field = 1;
}

```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04825"></a>
## FND-04825: chesscom.friends_search.v1.FriendsSearchExtraFieldResponse.field = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.friends_search.v1.FriendsSearchRetrievableField field = 1;

### Evidence

- **SRC-0440** `research/proto/chesscom/friends_search/v1/friends_search.proto` — [preserved redacted evidence](../evidence/text/7ae90580df8c43e71275bbf68f858f2570d040833ecfda88d8d95cc84ab8dd91.proto)
  Character offset 8127.

```text
integer_value = 4;
  float float_value = 5;
  double double_value = 6;
  bool bool_value = 7;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRetrievableField field = 1;
}

```

**Source references:** SRC-0440, SRC-1411  
**URL references:** None independently associated  
**Related findings:** FND-04658, FND-04659, FND-04660

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04826"></a>
## FND-04826: message declaration: chesscom.friends_search.v1.QueryFriendsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message QueryFriendsRequest {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 123.

```text
ends_search/v1/friends_search_service.proto
// syntax: proto3

package chesscom.friends_search.v1;

message QueryFriendsRequest {
  oneof _uuid {
  string uuid = 1;
  }
  oneof _include_presence_status {
  bool include_presence_status = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;
}

message QueryFriendsR
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04827"></a>
## FND-04827: oneof declaration: chesscom.friends_search.v1.QueryFriendsRequest._uuid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _uuid {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 155.

```text
rvice.proto
// syntax: proto3

package chesscom.friends_search.v1;

message QueryFriendsRequest {
  oneof _uuid {
  string uuid = 1;
  }
  oneof _include_presence_status {
  bool include_presence_status = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;
}

message QueryFriendsResponse {
  optional .chesscom.a
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04828"></a>
## FND-04828: chesscom.friends_search.v1.QueryFriendsRequest.uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string uuid = 1;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 171.

```text
yntax: proto3

package chesscom.friends_search.v1;

message QueryFriendsRequest {
  oneof _uuid {
  string uuid = 1;
  }
  oneof _include_presence_status {
  bool include_presence_status = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;
}

message QueryFriendsResponse {
  optional .chesscom.api.v1.ResponsePa
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04829"></a>
## FND-04829: oneof declaration: chesscom.friends_search.v1.QueryFriendsRequest._include_presence_status

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _include_presence_status {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 194.

```text
chesscom.friends_search.v1;

message QueryFriendsRequest {
  oneof _uuid {
  string uuid = 1;
  }
  oneof _include_presence_status {
  bool include_presence_status = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;
}

message QueryFriendsResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04830"></a>
## FND-04830: chesscom.friends_search.v1.QueryFriendsRequest.include_presence_status = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool include_presence_status = 2;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 229.

```text
e QueryFriendsRequest {
  oneof _uuid {
  string uuid = 1;
  }
  oneof _include_presence_status {
  bool include_presence_status = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;
}

message QueryFriendsResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_sear
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04831"></a>
## FND-04831: oneof declaration: chesscom.friends_search.v1.QueryFriendsRequest._pagination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pagination {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 269.

```text
  string uuid = 1;
  }
  oneof _include_presence_status {
  bool include_presence_status = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;
}

message QueryFriendsResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 2;
}
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04832"></a>
## FND-04832: chesscom.friends_search.v1.QueryFriendsRequest.pagination = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.RequestPagination pagination = 3;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 291.

```text

  oneof _include_presence_status {
  bool include_presence_status = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;
}

message QueryFriendsResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 2;
}

message Autocomplete
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04833"></a>
## FND-04833: chesscom.friends_search.v1.QueryFriendsRequest.query = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 348.

```text
ce_status = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;
}

message QueryFriendsResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 2;
}

message AutocompleteRequest {
  oneof _include_friends {
  bool include_frien
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04834"></a>
## FND-04834: message declaration: chesscom.friends_search.v1.QueryFriendsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message QueryFriendsResponse {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 422.

```text
ion pagination = 3;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;
}

message QueryFriendsResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 2;
}

message AutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 2;
  }
  oneof _include_suggestions {
  bool include_suggestions = 3;
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04835"></a>
## FND-04835: chesscom.friends_search.v1.QueryFriendsResponse.pagination = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.ResponsePagination pagination = 1;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 455.

```text
l .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;
}

message QueryFriendsResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 2;
}

message AutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 2;
  }
  oneof _include_suggestions {
  bool include_suggestions = 3;
  }
  oneof _friends_limit {
  i
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04836"></a>
## FND-04836: chesscom.friends_search.v1.QueryFriendsResponse.friends = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 2;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 518.

```text

}

message QueryFriendsResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 2;
}

message AutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 2;
  }
  oneof _include_suggestions {
  bool include_suggestions = 3;
  }
  oneof _friends_limit {
  int32 friends_limit = 4;
  }
  oneof _suggestions_limit {
  int3
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04837"></a>
## FND-04837: message declaration: chesscom.friends_search.v1.AutocompleteRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AutocompleteRequest {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 591.

```text
gination pagination = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 2;
}

message AutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 2;
  }
  oneof _include_suggestions {
  bool include_suggestions = 3;
  }
  oneof _friends_limit {
  int32 friends_limit = 4;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 5;
  }
  oneof _exact_username_first {
  bool exact
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04838"></a>
## FND-04838: oneof declaration: chesscom.friends_search.v1.AutocompleteRequest._include_friends

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _include_friends {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 623.

```text
ted .chesscom.friends_search.v1.FriendsSearchFriend friends = 2;
}

message AutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 2;
  }
  oneof _include_suggestions {
  bool include_suggestions = 3;
  }
  oneof _friends_limit {
  int32 friends_limit = 4;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 5;
  }
  oneof _exact_username_first {
  bool exact_username_first = 6;
  }
  oneof
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04839"></a>
## FND-04839: chesscom.friends_search.v1.AutocompleteRequest.include_friends = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool include_friends = 2;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 650.

```text
h.v1.FriendsSearchFriend friends = 2;
}

message AutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 2;
  }
  oneof _include_suggestions {
  bool include_suggestions = 3;
  }
  oneof _friends_limit {
  int32 friends_limit = 4;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 5;
  }
  oneof _exact_username_first {
  bool exact_username_first = 6;
  }
  oneof _boost_username {
  bool b
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04840"></a>
## FND-04840: oneof declaration: chesscom.friends_search.v1.AutocompleteRequest._include_suggestions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _include_suggestions {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 682.

```text
 = 2;
}

message AutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 2;
  }
  oneof _include_suggestions {
  bool include_suggestions = 3;
  }
  oneof _friends_limit {
  int32 friends_limit = 4;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 5;
  }
  oneof _exact_username_first {
  bool exact_username_first = 6;
  }
  oneof _boost_username {
  bool boost_username = 7;
  }
  optiona
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04841"></a>
## FND-04841: chesscom.friends_search.v1.AutocompleteRequest.include_suggestions = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool include_suggestions = 3;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 713.

```text
quest {
  oneof _include_friends {
  bool include_friends = 2;
  }
  oneof _include_suggestions {
  bool include_suggestions = 3;
  }
  oneof _friends_limit {
  int32 friends_limit = 4;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 5;
  }
  oneof _exact_username_first {
  bool exact_username_first = 6;
  }
  oneof _boost_username {
  bool boost_username = 7;
  }
  optional string prefix = 1;
}

message
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04842"></a>
## FND-04842: oneof declaration: chesscom.friends_search.v1.AutocompleteRequest._friends_limit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _friends_limit {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 749.

```text
 bool include_friends = 2;
  }
  oneof _include_suggestions {
  bool include_suggestions = 3;
  }
  oneof _friends_limit {
  int32 friends_limit = 4;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 5;
  }
  oneof _exact_username_first {
  bool exact_username_first = 6;
  }
  oneof _boost_username {
  bool boost_username = 7;
  }
  optional string prefix = 1;
}

message AutocompleteResponse {
  repeated .
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04843"></a>
## FND-04843: chesscom.friends_search.v1.AutocompleteRequest.friends_limit = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 friends_limit = 4;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 774.

```text
;
  }
  oneof _include_suggestions {
  bool include_suggestions = 3;
  }
  oneof _friends_limit {
  int32 friends_limit = 4;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 5;
  }
  oneof _exact_username_first {
  bool exact_username_first = 6;
  }
  oneof _boost_username {
  bool boost_username = 7;
  }
  optional string prefix = 1;
}

message AutocompleteResponse {
  repeated .chesscom.friends_search.v
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04844"></a>
## FND-04844: oneof declaration: chesscom.friends_search.v1.AutocompleteRequest._suggestions_limit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _suggestions_limit {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 805.

```text
ons {
  bool include_suggestions = 3;
  }
  oneof _friends_limit {
  int32 friends_limit = 4;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 5;
  }
  oneof _exact_username_first {
  bool exact_username_first = 6;
  }
  oneof _boost_username {
  bool boost_username = 7;
  }
  optional string prefix = 1;
}

message AutocompleteResponse {
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends =
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04845"></a>
## FND-04845: chesscom.friends_search.v1.AutocompleteRequest.suggestions_limit = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 suggestions_limit = 5;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 834.

```text
ons = 3;
  }
  oneof _friends_limit {
  int32 friends_limit = 4;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 5;
  }
  oneof _exact_username_first {
  bool exact_username_first = 6;
  }
  oneof _boost_username {
  bool boost_username = 7;
  }
  optional string prefix = 1;
}

message AutocompleteResponse {
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 1;
  repeated .chesscom.frie
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04846"></a>
## FND-04846: oneof declaration: chesscom.friends_search.v1.AutocompleteRequest._exact_username_first

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _exact_username_first {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 869.

```text
 {
  int32 friends_limit = 4;
  }
  oneof _suggestions_limit {
  int32 suggestions_limit = 5;
  }
  oneof _exact_username_first {
  bool exact_username_first = 6;
  }
  oneof _boost_username {
  bool boost_username = 7;
  }
  optional string prefix = 1;
}

message AutocompleteResponse {
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend s
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04847"></a>
## FND-04847: chesscom.friends_search.v1.AutocompleteRequest.exact_username_first = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool exact_username_first = 6;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 901.

```text
}
  oneof _suggestions_limit {
  int32 suggestions_limit = 5;
  }
  oneof _exact_username_first {
  bool exact_username_first = 6;
  }
  oneof _boost_username {
  bool boost_username = 7;
  }
  optional string prefix = 1;
}

message AutocompleteResponse {
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend suggestions = 2;
}

message GetBl
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04848"></a>
## FND-04848: oneof declaration: chesscom.friends_search.v1.AutocompleteRequest._boost_username

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _boost_username {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 938.

```text
2 suggestions_limit = 5;
  }
  oneof _exact_username_first {
  bool exact_username_first = 6;
  }
  oneof _boost_username {
  bool boost_username = 7;
  }
  optional string prefix = 1;
}

message AutocompleteResponse {
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend suggestions = 2;
}

message GetBlockersOfRequest {
  oneof _pagination
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04849"></a>
## FND-04849: chesscom.friends_search.v1.AutocompleteRequest.boost_username = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool boost_username = 7;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 964.

```text
 }
  oneof _exact_username_first {
  bool exact_username_first = 6;
  }
  oneof _boost_username {
  bool boost_username = 7;
  }
  optional string prefix = 1;
}

message AutocompleteResponse {
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend suggestions = 2;
}

message GetBlockersOfRequest {
  oneof _pagination {
  .chesscom.api.v1.Requ
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04850"></a>
## FND-04850: chesscom.friends_search.v1.AutocompleteRequest.prefix = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string prefix = 1;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 995.

```text
t {
  bool exact_username_first = 6;
  }
  oneof _boost_username {
  bool boost_username = 7;
  }
  optional string prefix = 1;
}

message AutocompleteResponse {
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend suggestions = 2;
}

message GetBlockersOfRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
 
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04851"></a>
## FND-04851: message declaration: chesscom.friends_search.v1.AutocompleteResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AutocompleteResponse {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1026.

```text
 = 6;
  }
  oneof _boost_username {
  bool boost_username = 7;
  }
  optional string prefix = 1;
}

message AutocompleteResponse {
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend suggestions = 2;
}

message GetBlockersOfRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional string uuid = 1;

```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04852"></a>
## FND-04852: chesscom.friends_search.v1.AutocompleteResponse.friends = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 1;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1059.

```text
 {
  bool boost_username = 7;
  }
  optional string prefix = 1;
}

message AutocompleteResponse {
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend suggestions = 2;
}

message GetBlockersOfRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional string uuid = 1;
  repeated .chesscom.friends_sear
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04853"></a>
## FND-04853: chesscom.friends_search.v1.AutocompleteResponse.suggestions = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.friends_search.v1.FriendsSearchFriend suggestions = 2;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1131.

```text
ge AutocompleteResponse {
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend suggestions = 2;
}

message GetBlockersOfRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional string uuid = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;
}

message GetBloc
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04854"></a>
## FND-04854: message declaration: chesscom.friends_search.v1.GetBlockersOfRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetBlockersOfRequest {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1208.

```text
hFriend friends = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend suggestions = 2;
}

message GetBlockersOfRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional string uuid = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;
}

message GetBlockersOfResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04855"></a>
## FND-04855: oneof declaration: chesscom.friends_search.v1.GetBlockersOfRequest._pagination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pagination {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 269.

```text
  string uuid = 1;
  }
  oneof _include_presence_status {
  bool include_presence_status = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;
}

message QueryFriendsResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 2;
}
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04856"></a>
## FND-04856: chesscom.friends_search.v1.GetBlockersOfRequest.pagination = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.RequestPagination pagination = 2;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1263.

```text
h.v1.FriendsSearchFriend suggestions = 2;
}

message GetBlockersOfRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional string uuid = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;
}

message GetBlockersOfResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.BlockedUsers 
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04857"></a>
## FND-04857: chesscom.friends_search.v1.GetBlockersOfRequest.uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string uuid = 1;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1320.

```text
lockersOfRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional string uuid = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;
}

message GetBlockersOfResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.BlockedUsers blocked_users = 2;
}

message GetUsersBlockedByRequest {

```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04858"></a>
## FND-04858: chesscom.friends_search.v1.GetBlockersOfRequest.extra_fields = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1348.

```text
pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional string uuid = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;
}

message GetBlockersOfResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.BlockedUsers blocked_users = 2;
}

message GetUsersBlockedByRequest {
  oneof _last_login_date {
 
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04859"></a>
## FND-04859: message declaration: chesscom.friends_search.v1.GetBlockersOfResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetBlockersOfResponse {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1436.

```text
uuid = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;
}

message GetBlockersOfResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.BlockedUsers blocked_users = 2;
}

message GetUsersBlockedByRequest {
  oneof _last_login_date {
  .google.protobuf.Timestamp last_login_date = 2;
  }
  oneof _pagination {
  .chesscom.a
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04860"></a>
## FND-04860: chesscom.friends_search.v1.GetBlockersOfResponse.pagination = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.ResponsePagination pagination = 1;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 455.

```text
l .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;
}

message QueryFriendsResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 2;
}

message AutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 2;
  }
  oneof _include_suggestions {
  bool include_suggestions = 3;
  }
  oneof _friends_limit {
  i
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04861"></a>
## FND-04861: chesscom.friends_search.v1.GetBlockersOfResponse.blocked_users = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.friends_search.v1.BlockedUsers blocked_users = 2;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1533.

```text
}

message GetBlockersOfResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.BlockedUsers blocked_users = 2;
}

message GetUsersBlockedByRequest {
  oneof _last_login_date {
  .google.protobuf.Timestamp last_login_date = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 99;
  }
  optional string uuid = 1;
  repeated .chesscom.fri
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04862"></a>
## FND-04862: message declaration: chesscom.friends_search.v1.GetUsersBlockedByRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUsersBlockedByRequest {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1605.

```text
agination pagination = 1;
  repeated .chesscom.friends_search.v1.BlockedUsers blocked_users = 2;
}

message GetUsersBlockedByRequest {
  oneof _last_login_date {
  .google.protobuf.Timestamp last_login_date = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 99;
  }
  optional string uuid = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;
}

messag
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04863"></a>
## FND-04863: oneof declaration: chesscom.friends_search.v1.GetUsersBlockedByRequest._last_login_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_login_date {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1642.

```text
.chesscom.friends_search.v1.BlockedUsers blocked_users = 2;
}

message GetUsersBlockedByRequest {
  oneof _last_login_date {
  .google.protobuf.Timestamp last_login_date = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 99;
  }
  optional string uuid = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;
}

message GetUsersBlockedByResponse {
  optio
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04864"></a>
## FND-04864: chesscom.friends_search.v1.GetUsersBlockedByRequest.last_login_date = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_login_date = 2;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1669.

```text
.BlockedUsers blocked_users = 2;
}

message GetUsersBlockedByRequest {
  oneof _last_login_date {
  .google.protobuf.Timestamp last_login_date = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 99;
  }
  optional string uuid = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;
}

message GetUsersBlockedByResponse {
  optional .chesscom.api.v1.Respon
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04865"></a>
## FND-04865: oneof declaration: chesscom.friends_search.v1.GetUsersBlockedByRequest._pagination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pagination {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 269.

```text
  string uuid = 1;
  }
  oneof _include_presence_status {
  bool include_presence_status = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 3;
  }
  optional .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;
}

message QueryFriendsResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 2;
}
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04866"></a>
## FND-04866: chesscom.friends_search.v1.GetUsersBlockedByRequest.pagination = 99

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.RequestPagination pagination = 99;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1745.

```text
of _last_login_date {
  .google.protobuf.Timestamp last_login_date = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 99;
  }
  optional string uuid = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;
}

message GetUsersBlockedByResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.BlockedU
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04867"></a>
## FND-04867: chesscom.friends_search.v1.GetUsersBlockedByRequest.uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string uuid = 1;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1320.

```text
lockersOfRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional string uuid = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;
}

message GetBlockersOfResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.BlockedUsers blocked_users = 2;
}

message GetUsersBlockedByRequest {

```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04868"></a>
## FND-04868: chesscom.friends_search.v1.GetUsersBlockedByRequest.extra_fields = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1348.

```text
pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional string uuid = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;
}

message GetBlockersOfResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.BlockedUsers blocked_users = 2;
}

message GetUsersBlockedByRequest {
  oneof _last_login_date {
 
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04869"></a>
## FND-04869: message declaration: chesscom.friends_search.v1.GetUsersBlockedByResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUsersBlockedByResponse {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1919.

```text
uuid = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;
}

message GetUsersBlockedByResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.BlockedUsers blocked_users = 2;
}

message GetFriendsCountRequest {
  optional string uuid = 1;
}

message GetFriendsCountResponse {
  optional int32 friend_count = 4;
}

```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04870"></a>
## FND-04870: chesscom.friends_search.v1.GetUsersBlockedByResponse.pagination = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.ResponsePagination pagination = 1;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 455.

```text
l .chesscom.friends_search.v1.FriendsSearchRootQuery query = 4;
}

message QueryFriendsResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchFriend friends = 2;
}

message AutocompleteRequest {
  oneof _include_friends {
  bool include_friends = 2;
  }
  oneof _include_suggestions {
  bool include_suggestions = 3;
  }
  oneof _friends_limit {
  i
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04871"></a>
## FND-04871: chesscom.friends_search.v1.GetUsersBlockedByResponse.blocked_users = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.friends_search.v1.BlockedUsers blocked_users = 2;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1533.

```text
}

message GetBlockersOfResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.BlockedUsers blocked_users = 2;
}

message GetUsersBlockedByRequest {
  oneof _last_login_date {
  .google.protobuf.Timestamp last_login_date = 2;
  }
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 99;
  }
  optional string uuid = 1;
  repeated .chesscom.fri
```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04872"></a>
## FND-04872: message declaration: chesscom.friends_search.v1.GetFriendsCountRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetFriendsCountRequest {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 2092.

```text
agination pagination = 1;
  repeated .chesscom.friends_search.v1.BlockedUsers blocked_users = 2;
}

message GetFriendsCountRequest {
  optional string uuid = 1;
}

message GetFriendsCountResponse {
  optional int32 friend_count = 4;
}

```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04873"></a>
## FND-04873: chesscom.friends_search.v1.GetFriendsCountRequest.uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string uuid = 1;

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 1320.

```text
lockersOfRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional string uuid = 1;
  repeated .chesscom.friends_search.v1.FriendsSearchRetrievableField extra_fields = 3;
}

message GetBlockersOfResponse {
  optional .chesscom.api.v1.ResponsePagination pagination = 1;
  repeated .chesscom.friends_search.v1.BlockedUsers blocked_users = 2;
}

message GetUsersBlockedByRequest {

```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04874"></a>
## FND-04874: message declaration: chesscom.friends_search.v1.GetFriendsCountResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetFriendsCountResponse {

### Evidence

- **SRC-0441** `research/proto/chesscom/friends_search/v1/friends_search_service.proto` — [preserved redacted evidence](../evidence/text/356b94f3cf4f37c28f5b3293945f80e07c6a2b9c2307f39ec9af367f02407017.proto)
  Character offset 2156.

```text
.BlockedUsers blocked_users = 2;
}

message GetFriendsCountRequest {
  optional string uuid = 1;
}

message GetFriendsCountResponse {
  optional int32 friend_count = 4;
}

```

**Source references:** SRC-0441, SRC-1412  
**URL references:** None independently associated  
**Related findings:** FND-04826, FND-04827, FND-04828

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
