# 01 — Torch Human: activation, actual behavior and review boundary

[Start](00_START_HERE.md) · [Evidence and reproduction](06_EVIDENCE_AND_REPRODUCTION.md)

## 1. Four things that must not be merged

| Name | Owning API / purpose | What it establishes |
|---|---|---|
| `Engine.TORCH_3 = 11`, `Engine.TORCH_HUMAN = 12` | `chesscom.engine.v1.Engine`, evaluation/cloud request identification | Distinct engine identifiers; not native pool handles |
| `BotEngine.TORCH = 2`, `BotEngine.KOMODO = 1` | Local legacy `GetBotMoveRequest.engine` | Which legacy bot engine was requested |
| `BotPersonality.HUMAN = 7` | Legacy bot options | A style option; does not select `TorchSearchMode.human` |
| `TorchSearchMode.mode.human` | Local search request oneof | Explicit Human search mode, with optional nested `disable_maia` |

**`RunSearchRequest.engineId` is yet another concept:** an engine-pool identifier, not the above engine enum. A preliminary probe incorrectly supplied `11` there and received “no engine with id 11 was added to any pool.” Final valid tests omit that field. Returned evaluation `engine:11` does not mean the Human request was ignored.

## 2. Website Game Review activation — STATIC, baseline SRC-1137

Exact function spans are in `evidence/extracted-functions.json`; the original source is still identified by `evidence/baseline-source-references.json` and is not edited.

`A4e(fullAnalysisOption)` selects:

- if `web_analysis_torch_human_v2` is **off**: `SF16_1_NNUE`;
- if the flag is **on**, but the user selected the Stockfish16 full-analysis option: `SF16_1_NNUE`;
- otherwise: `TORCH_HUMAN`.

`W4e` builds the CEAC request from the game, strength, user-color/optional skills and optional coach state. It sets `engine` to that selection and `gameEvaluationOptions.useGameStateCache` to `engine !== TORCH_HUMAN`. Strength mapping is 18→Fast, 22→Standard, 24→Deep, 26→Maximum (default Fast); those numbers must not be reinterpreted as exact Torch search depths.

The request can also add `charmInfReq` for separately gated tricky classification / Game Rating V2. This is evidence that Charm-related downstream analysis is separately requested; it does **not** establish that Torch Human itself is the Topaz/Charm-small bot model or that a fixed formula is shared between those products.

`O4e` selects sandbox/staging/production Game Review routing. The production literal is `wss://analysis.chess.com:443/v2/game-review`. The existing `x3e`/`S3e` connection chain uses this remote interface. This is **not** a recovered private backend implementation and not a newly captured authenticated WebSocket session.

**Consequence:** the inspected full website review flow is server-routed, even though the browser-distributed CEE can perform useful local searches and reviews.

## 3. Local Human protocol — STATIC

Recovered `torch_search_mode.proto` exposes a real oneof:

```text
mode = human { optional bool disable_maia }
    OR multisearch { optional bool reduce_nodes_on_successive_searches }
```

There is no public rating field inside `Human` in the recovered schema. `RunSearchRequest` also has an independent top-level `disable_maia`; that is not the same serialized field as the nested Human option. No equivalence between those two switches was established here.

Inputs include the current game-point position, selected search settings/limits, optional search moves, selected Human mode, and available engine/model state. Outputs are ordinary evaluation structures (score, nodes/depth, PV and log) even when their search procedure differs. An evaluation engine label is not a full provenance record of the request mode.

## 4. Prior command-level proof — HISTORICAL-EXPERIMENT

Preserved excerpts in `evidence/historical-search-logs/` remove the fixture PGN/identity header, retaining the exact engine command/output section. They show ordinary search using `searchmoves`, versus Human search issuing:

```text
go nodes 1000 pvtrees
  use_split_depth_limit true use_split_width_limit true
  keep_equal_subtrees false show_only_optimal_mates true
  at_least_n_root_moves 1 split_depth_limit 6 split_width_limit 2
  allowed_excess_depth 0 allowed_excess_width 2
  rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02
```

The command's actual spelling is `pvtrees`; it is not a UI-only label. The log emits multiple `pvtree quality good ... pv ...` alternatives. This supports a tree/refutation-oriented Human search distinct from a single ordinary best-line request. It does **not** recover how all tree candidates are selected, the exact human-likelihood model, or every pruning/weighting formula. Names such as `max_allowed_cp_margin` are parameter evidence, not permission to invent the underlying equation.

The prior starting-position probe returned ordinary +17cp/depth6 versus Human +18cp/depth5. The command's `rating 2100` is an observed local default for that trial, **not** a recovered cloud or bot rating policy. Prior fetch-rejecting local trials reported no fetch attempts.

## 5. New controlled position check — EXECUTED-NATIVE

All final runs create the same small PGN position after `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6`; each mode runs in a fresh sequential process. Request: `searchParameters.nodesLimit=1000`, `numLines=1`, with Human mode absent / present / present with nested `disableMaia:true`. No explicit `engineId` is supplied. Full request, response and binary hashes are in the corresponding `runtime-human-*.json` files.

| Mode | Score (White cp) | Depth | Reported nodes | Progress |
|---|---:|---:|---:|---:|
| Ordinary | 38 | 7 | 1000 | 1 |
| Human | 18 | 6 | 681 | 1 |
| Human + nested disableMaia | 18 | 6 | 681 | 1 |

All three return evaluation `engine:11` and `engine: Torch master-20260925-87ee25a` in the response log. **Mode changes can alter the result despite identical evaluation engine identifiers.** This one position produced no difference between the two Human variants; that does not prove the switch is ignored, that Maia never participates, or that other positions/settings behave identically. A node limit is a bound/request, not a promise that every mode reports exactly that many nodes. These are bounded illustrations, not an Elo/style benchmark or statistical proof.

## 6. Local completed review is real, parity is not

The preserved original `SRC-1628-torch-human-comparison.md` supersedes earlier “no completed Human review” statements in `SRC-1629`/`SRC-1631`. Its successful pipeline was:

1. Create game points for the fixture.
2. Feature **79** `GetGameReviewEvaluations` with Fast/Human, per position (20 Human searches plus auxiliary ordinary search work in that experiment).
3. Feature **1** `AddEvaluations` to preload the returned evaluations.
4. Feature **42** `GameReview` to assemble the report; the recorded review stage issued no additional searches.

For that prior fixture, ordinary control accuracy was **60.2 / 96.1**, effective ratings **300 / 1000**; Human preload was **59.0 / 95.4**, ratings **400 / 1000**. The saved website reference was **71.7 / 99**, ratings **100 / 1000**. Neither path demonstrated parity; Human was not shown to improve parity. Those are fixture-specific historical values, not a current service measurement or generic quality ranking.

Whole-game feature54 aborts and feature288 timeouts remain real failed attempts but do not negate the later successful feature79/per-position route. No production extension change or tuning recommendation is made by this update.

## 7. What “human” means at the supported boundary

The evidence supports **different search policy/tree output and optional model-related controls**, not “randomly choose an engine blunder,” “play like a named celebrity,” “a renamed Maia network,” or “a separately trained model whose full architecture has been recovered.” Torch Human search, Maia model support, Charm-small bot configuration, game-rating inference and chat are related capabilities in a broader stack, but their identities and activation paths remain distinct.
