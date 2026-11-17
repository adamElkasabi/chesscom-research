# Torch Human and bot personalities — focused audit update

**Status: PARTIALLY AUDITED.** This update resolves important activation, routing, model and native-execution questions. It does **not** recover every native function, all live bot configurations, training data, cloud settings or exact personality/sampling formulas.

## The answer in one page

1. **Torch Human is a search mode, not a synonym for a human-labeled bot.** The local `TorchSearchMode.human` request produces a distinct Torch search. The inspected website Game Review route selects the separate remote `Engine.TORCH_HUMAN = 12` identifier behind a feature flag. A bot's `BotPersonality.HUMAN = 7` is a different namespace and is mapped into the **legacy Komodo** request in the inspected play-computer code.
2. **Bot play has two implementations in this package, not one global engine choice.** A gated, configured bot goes through feature **61** (`BotMoveFromConfig`); otherwise a valid browser-side book move takes priority, then feature **9** (`GetBotMove`) explicitly requests **Komodo** with translated personality, adaptive flag and skill-derived rating. This is a callsite conclusion for package `2026.11.5`, not a claim about every Chess.com product/account/version.
3. **The new configuration path is genuinely model-backed.** The frontend references `topaz_jackdaw.bin.q8mix`, loads it as `m-topaz-jackdaw`, and obtains bot configuration from Configurator. We retrieved that exact public model, parsed **134 tensor records / 11,233,640 stored elements / zero trailing bytes**, and executed a diagnostic configuration using it in genuine CEE WASM. The model's own metadata says **`charm-small`**. No production bot weights were invented or claimed recovered.
4. **Labels, playing strength, openings and chat are separable inputs.** Metadata personality enums require explicit translation; legacy strength comes from `komodoSkill`/`komodoSkillLevel`, not directly the displayed rating. Books can bypass an engine request. Speech assets and `GetBotChat` are separate from move generation. A witty phrase or avatar does not establish a move algorithm.
5. **Local capability is not website parity.** Prior human-mode preload experiments completed a local review but did not reproduce the reference site's numbers. New one-position Human tests also differ from ordinary search; they do not identify the private cloud policy or prove Maia participation. `disable_maia` is a supported switch, not evidence that every Human search uses Maia.

## Read in order

- [01 — Torch Human activation, search and review](01_TORCH_HUMAN.md)
- [02 — How bot personalities actually reach move generation](02_BOT_PERSONALITY_PIPELINE.md)
- [03 — Recovered Charm-small model and native positive/negative controls](03_MODEL_AND_NATIVE_TESTS.md)
- [04 — Worker/protobuf/native boundary and namespaces](04_WORKER_AND_NAMESPACES.md)
- [05 — Corrections, supersession and remaining gaps](05_CORRECTIONS_AND_LIMITS.md)
- [06 — Evidence map and reproduction](06_EVIDENCE_AND_REPRODUCTION.md)
- [07 — Architecture diagrams](07_ARCHITECTURE_DIAGRAMS.md)
- [Machine claim ledger](evidence/claims.json)
- [Patch verification / overlay instructions](../TORCH_HUMAN_BOTS_PATCH_MANIFEST.md)

## Evidence grades

**STATIC** = inspected exact source or decoded descriptor; **EXECUTED-FRONTEND** = exact extracted function with dependency stubs; **EXECUTED-NATIVE** = genuine original WASM and wrapper; **HISTORICAL-EXPERIMENT** = prior preserved local trial, not newly rerun; **UNKNOWN** = unobserved/private/unfinished. These grades are not interchangeable.

Session date is **2026-11-13**. Public response headers and sandbox clocks report **2026-11-15**. Those raw provenance clocks are retained; they are not silently normalized into an unsupported deployment date. The inspected package identifies itself as `play-computer/2026.11.5`.
