# 03 — Recovered model and native execution

[Start](00_START_HERE.md) · Evidence: `model-*`, `runtime-*`, `attempt-ledger.json`

## 1. This model is now actually recovered and used in a bounded trial

The exact public code references a same-origin path resolved by `jJ(path,false)`:

`https://www.chess.com/r2/assets-chess-engine/models/topaz_jackdaw.bin.q8mix`

GET returned200 and **11,946,339 bytes**, SHA256:

`1f78db3d3184550ff56db7a0f14b72910b039a894dcc97ff8ef7bb8915f26423`

This was discovered as a literal in the retrieved frontend, not guessed from the earlier failed coach/Charm paths. Those failed paths were not retried. The downloaded weights were not trained, modified or substituted. The 11.4MiB binary is **not embedded in the small overlay ZIP**; exact retrieval provenance, native success/error evidence, full tensor record manifest, parser and opt-in hash-checking downloader are included.

## 2. Byte-level container evidence

The file starts with ASCII `json`, followed by an8-byte little-endian JSON-byte length **436**, then the JSON at offset12 through447. An8-byte little-endian record count **134** follows at448. A consistent record parse is:

```text
u64 name_length; UTF-8 tensor_name[name_length]; u8 stored_bits;
f32 scalar (observed in every 8/16-bit record);
u64 element_count; payload[element_count * stored_bits/8]
```

All **134/134** records parsed, ending at offset **11,946,339**, with **zero unparsed bytes** and finite record scalars. **112 records are16-bit;22 are8-bit; total stored element count11,233,640.** That is a tensor-storage count (including normalization buffers/counters), not a claim of exactly that many trainable weights. Per-record offsets, names, scalar values, sizes and payload SHA256s are in `model-tensor-manifest.json`.

The storage layout is a structurally consistent recovery validated by native acceptance of the same binary. This work does not claim an independently implemented/dequantized forward pass or that the observed scalar's exact runtime application has been proven solely by this parse.

## 3. The model describes itself

Embedded JSON:

- `arch: "charm-small"`;
- rating range min100/max2500/step100;
- `fc_1:512→1880`, `fc_2:512→2021`, `fc_3_1:512→128`, `fc_3:128→3`;
- rank head512→6;
- strength and rating-sensitive-strength heads512→5;
- time-taken head512→4;
- move-strength expected-point split values `[0.02,0.05,0.1,0.2]`;
- time split values `[1.0,2.5,5.0]` seconds.

Tensor names include `chess_cnn.layers.*`, normalization buffers, `to_patch_embedding.*`, `pos_embedding`, `elo_embedding.weight`, `transformer.elo_layers.*.to_qkv.weight`, `elo_query.weight`, move/expected-point triplet embeddings and the listed output heads. This supports a CNN/transformer/rating-conditioned multi-head architecture interpretation much more strongly than a filename alone. It still does not reveal training corpus, loss functions, board encoding, exact token layout, attention/activation equations, calibration or mapping of all head indices to chess actions. A512-wide head inventory does not by itself establish every hidden layer's shape.

The head names/splits and recovered inference response schema align with move probabilities, rank/strength/time and loss/draw/win-related outputs. **Schema alignment is not proof that every head participates in every bot decision.** Topaz/Charm-small is not thereby identified as the Maia model or as Torch Human's private cloud model.

## 4. Native binary identity and version correction

All final probes use unchanged baseline bytes:

| Asset | Identity |
|---|---|
| Worker/glue wrapper (baseline SRC-0014) | `46761f54ffdd6550b3fe90553e3c13d1a49828b3c44b680845afcc20c0666c70` |
| Original CEE module-002 WASM | `b94aaeec32ee0458aeba42a9d431a15f37c16740c030868c691c0697b3203373` |

Feature2 `CeeVersion` returns **CEE1.211.5**, native git **7a94cbd4**, definitions git **8c0f7769c299cbc1ef53ea1eed2c30495a1c3f25**, and **UCI1.130.285**. The banner/package says Explanation Engine1.130.285. These identifiers are not contradictions to erase: the wrapper/UCI/package and native CEE report different version fields. Older prose that called1.130.285 the native CEE version should be read with this correction. This is not a new/replaced WASM identity or a claim the website executed these exact local bytes during the page visit.

## 5. Positive control: actual model-dependent move generation

The supplied diagnostic config is explicitly **synthetic research input**, not a recovered Martin/Mateo/Isla production configuration. It uses real schema fields:

```text
settings.depth = 2
mode.nnmult.n_top_nn_candidates = 5
mode.nnmult.nn = {
  arch: CHARM_SMALL, model: "m-topaz-jackdaw", rating:1200,
  weight:1, charm_input_search_depth:2, temperature:1
}
```

The request uses the actual oneof encodings (`searchLimit:{case:'depth',...}`, `mode:{case:'nnmult',...}`) in the JS codec. The runner:

1. Loads the genuine model bytes with `CEE_LoadCharmModel`.
2. Receives `{call:"CEE_LoadCharmModel_done",key:"m-topaz-jackdaw",success:true}`.
3. Native log reports `[model] charm-small: key=m-topaz-jackdaw`.
4. Feature70 resource inspection no longer reports that NN key as missing.
5. Feature61 returns move `{from:34,to:25}`, `suggestedDelaySeconds:0` for the small test position.

The final positive trial's measured local elapsed time was about1.7seconds including initialization. It is not a production latency promise or a benchmark.

## 6. Negative control and state-dependent resource discovery

A fresh process uses the **same diagnostic NN config**, but does **not** load the model:

- Feature70 returns `nn:{key:"m-topaz-jackdaw"}`.
- With a diagnostic book setting `{name:"beginner",moveCount:12}`, feature70 returns both `book:{key:"beginner",moveCount:12}` and that NN key. The book name is sourced from public fallback bot metadata; no speculative book download was attempted.
- Feature61 errors: `Global NN inference failed: failed to load charm-small model: m-topaz-jackdaw`. Native error provenance identifies `src/features/feature_bot_move_from_config.cpp:21` and CEE1.211.5.

With the model already loaded, the equivalent resource requests return `{}` or book-only, respectively. **Resource output depends on what is already loaded.** Therefore an empty `nn` response is not proof that the configuration has no NN component. This explains why frontend setup can pre-load one model, then consume only a book resource from the resource-discovery call.

Together, positive and negative controls establish that this real local native configuration path can depend on the real retrieved model. They do not establish any production bot's exact settings or prove parity with remote service behavior.

## 7. Scope, failures and safeguards

The fixture is a small artificial opening, not an authenticated game operation. JS `fetch` is replaced with a rejecting hook and recorded attempt arrays are empty. This is a host-level guard, not a claim of OS-enforced socket isolation. Native processes were run sequentially after a parallel attempt incurred OS kills; the exact failed-attempt ledger is retained. An initial75-second harness timeout was caused by awaiting the wrong acknowledgment shape; it is **not** evidence of model rejection. No bytecode derivative, placeholder-data module or invented engine was executed. No production extension file was changed.
