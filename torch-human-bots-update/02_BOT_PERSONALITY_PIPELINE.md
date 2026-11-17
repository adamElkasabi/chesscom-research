# 02 — How bot personalities are applied

[Start](00_START_HERE.md) · Package scope: public `play-computer/2026.11.5`

## 1. Metadata enters a page-specific bot model

The page's bot-loading chunk (`client.3755d359.C_dFGAfc_J.chunk.js`) calls `BotGroupService.ListBotGroups({withBots:true,supportedLanguages:[]})`. On failure, `Ge` calls `Be` to import bundled offline bot-group data. There is no captured live RPC response in this update.

The fetched fallback contains **13 groups / 212 bot records**. Three carry a `botMoveConfigurationKey`: `Martin-BOT`, `Mateo-BOT`, `Isla-BOT`, using their corresponding `bots-move_configuration-...` keys. This is the **offline fallback catalog**, not proof that only those three bots use the new path on the live service. The raw public fallback source is archived; a reduced metadata/strength analysis is supplied separately.

The frontend model `FJ` stores such fields as `adapt`, `book`, `personality`, `komodoSkill`, `komodoSkillLevel`, displayed `rating`, and `botMoveConfigurationKey` separately. `getPersonality()` returns a lowercase label for presentation. It is not the engine enum conversion and does not select Torch Human.

## 2. Gate controls the new implementation

Exact source functions `Kpt` and `R5` require:

```text
web_bot_move_next
AND (web_bot_move_next_experiment_bypass
     OR experiment bot_move_next_experiment == "Segment A")
```

A feature literal alone is insufficient. The retrieved public page mentions `web_bot_move_next` but provides no recovered matching experiment bucket; no bypass flag was found. This investigation therefore does **not** assert that the new branch executed in that browser session. Analytics suffixes `+charm` / `+bmn` reflect gate/key conditions, not native architecture proof.

## 3. Setup before play — exact `ac` source

`ac` creates a CEE game using TCN/initial FEN and selected bot ratings in **both players' metadata**. That metadata use is distinct from legacy bot engine strength. Search setup `sc` uses `PLAY_BOT_STANDARD` when the node-search feature is on and the fast condition is off; otherwise it supplies depthLimit9/15 and two lines for ordinary/null-move search settings. It does not say every bot move is searched to that exact depth.

If the new gate is on:

1. Fetch the model literal `Y6e()` → `/r2/assets-chess-engine/models/topaz_jackdaw.bin.q8mix` once per this frontend setup state.
2. Call `loadCharmModel(bytes,"m-topaz-jackdaw")`; set the one-time flag only after completion.
3. If the selected bot has no config key, clear `botMoveConfig`.
4. Otherwise call Configurator `getConfig({configKey,resolveAssets:false})` and parse `response.config.data.storedJson` into the generated `BotMoveConfiguration` descriptor.
5. Ask feature70 `getBotConfigResources({protoConfig})`. This callsite consumes the returned **book**; it does not fetch a returned `nn` resource here. The model was already explicitly loaded.
6. Fetch the book through `Z6e(key.replace('.bin',''))` and call `addArtifact(bytes,key)`.

Configurator is not necessarily a single hardwired version: `web_configurator_v4_runtime` selects the v4 wrapper branch; the surrounding client implements v3/v4 handling and fallback. Only the setup-facing request/decoded JSON use is needed for this conclusion; no production configuration response or private values were retrieved.

If config retrieval raises NotFound, `botMoveConfig` is cleared; other errors propagate. A failed book HTTP response is logged without an explicit config-clear at this callsite. Thus “all failures safely fall back to legacy” is **not** an accurate reading.

If the gate is off, setup calls the ordinary frontend book loader `Fpt(selectedBot.book)`. Gate-on/no-config does **not** run that same setup branch. `Fpt` has cached `D5/O5` book state. Whether a book can remain stale across a particular gate/selection transition requires lifecycle execution; it is a **risk/question**, not a confirmed bug.

## 4. Actual per-move precedence — exact `Z5`

```text
if game over: no move
else if gate AND botMoveConfig exists:
    feature61 BotMoveFromConfig(protoConfig); return its move
else if validated browser book pick exists:
    return book move
else:
    feature9 GetBotMove(engine=KOMODO,
      options={adaptive, skill-derived rating, translated personality})
```

The configured branch returns directly. An empty response does not continue into the book/legacy branch, and a rejection propagates at this function. This behavior was also checked by executing the exact extracted `Z5` with stubs: config-success, empty, error, book, legacy, gate-off/config-present and game-over scenarios all passed their expected ordering. This is **function-level execution**, not a full browser integration test.

The book branch chooses a random book move through `Ipt`, then validates it by applying it in a scratch JS chess game; invalid picks do not bypass the engine. Therefore “personality caused this opening move” cannot be concluded without checking the book branch.

## 5. Personality values must be translated

`Npt` explicitly maps the Bots metadata enum (`chesscom.bots.v1.Personality`) to CEE `BotPersonality`. Integer passthrough would be wrong for several common styles.

| Bots value / label | CEE value / label |
|---|---|
| 0 UNSPECIFIED | 0 UNSPECIFIED (default branch) |
| 1 DEFAULT | 0 UNSPECIFIED (default branch) |
| 2 BEGINNER | 4 BEGINNER |
| 3 AGGRESSIVE | 3 AGRESSIVE (native spelling) |
| 4 POSITIONAL | 8 POSITIONAL |
| 5 DEFENSIVE | 5 DEFENSIVE |
| 6 ENDGAME | 6 ENDGAME |
| 7 HUMAN | 7 HUMAN |
| 8 HIKARU | 11 HIKARU |
| 9 DANNY | **0 UNSPECIFIED (unhandled)** |
| 10 ACTIVE | 2 ACTIVE |
| 11 NEW_TO_CHESS | 13 NEW_TO_CHESS |
| 12 UNLEASHED | 15 UNLEASHED |

CEE also declares CARLSEN9/FISCHER10/KASPAROV12/DANNY14. Those declarations do not prove this frontend mapping selects them. The unhandled DANNY metadata case is verified source behavior, not a claim that every Danny-named bot has no distinct configuration/book/chat elsewhere.

## 6. Strength is not simply the displayed rating

Exact getters and `Mpt`:

```text
skill = komodoSkill || komodoSkillLevel
is25Levels = Boolean(komodoSkillLevel) && !komodoSkill
requested rating = skill*100 + (is25Levels ? 200 : 0)
                   when skill is truthy; otherwise 1500 at Z5
```

For example, skill12 in the older scheme yields1200; level25 in the 25-level scheme yields2700. The fallback catalog's Maximum/Komodo25 displays3200 but supplies `komodoSkillLevel:25`, so this frontend conversion requests2700. That mismatch is data/adapter evidence, **not a measurement that the bot plays at2700** or proof of a frontend bug. Native rating calibration is not recovered.

Adaptive is passed as its own boolean. Its full native adjustment formula, history dependence and interaction with strength/style are not recovered; it must not be replaced with an invented win/loss adjustment.

## 7. New-style configurations are richer than a personality enum

The recovered schema supports settings with a **depth OR nodes** search-limit oneof, book settings and sampling threshold, plus an **additive OR nnmult** mode oneof.

- Additive mode: top/bad candidate counts; enabled, weighted behaviors; circumstances, tags and move classifications; piece bonuses; centipawn/advantage thresholds; phase/eval/position-shape context; optional legacy-bot, NN and coherence components.
- NN-multiplicative mode: top NN candidates, an NN config, weighted behaviors, piece gates and board-event matcher groups, context and thresholds.
- `NnConfig`: architecture enum, model key, rating, weight, input-search depth, temperature, rating-scale string, time-taken multiplier.
- Architecture enum: CHARM=1, CHARM_SMALL=2, MAIA=3, MAIA3=4. The third item is `MODEL_ARCH_MAIA = 3`; the fourth is `MODEL_ARCH_MAIA3 = 4`—do not confuse enum value and model-name suffix.
- Coherence config can reference prior context (`n_back`), architecture/model/rating/search-depth/weight.

These fields are **capability/schema evidence**. Names “additive” and “nnmult” do not by themselves recover the precise score algebra, order of filtering, normalization, random sampling, fallback behavior or actual production values. We deliberately do not invent a weighted-sum formula.

## 8. Chat and delay are a separate layer

`jft` returns empty chat for engine-classified bots or disabled botChat; coach bots call `GetCoachChat`; ordinary bots call `GetBotChat({botName:username})`. Setup separately obtains speech assets and calls `LoadBot` with content format BASE64. Metadata phrases, names and avatars are not passed as the legacy move-selection personality options.

A courtesy delay exists in the UI path. Feature61 can return `suggested_delay_seconds`; `Z5` reads the returned move, not that delay. Do not infer that the configured model's predicted time is applied throughout the page just because the response schema contains a delay field.

## 9. Native confirmation, with limits

Final feature9 tests using personality0/3/5/7/8, rating1200 and a100ms time limit all return legal moves through the genuine local WASM. On this single position they all choose the same move. That validates accepted options and the local API path, **not** the exact personality algorithm or a measurable style difference. The separate Charm positive/negative controls in chapter03 are stronger evidence for actual model-dependent configured move generation.
