# Frontend architecture


## Focused Torch Human / bot-personality follow-up

See the focused update for metadata ingestion, experiment gate, Configurator v3/v4 wrapper, resource setup, move precedence, and separate chat path.

[Evidence-graded focused update](../torch-human-bots-update/00_START_HERE.md) · [Overlay change manifest](../TORCH_HUMAN_BOTS_PATCH_MANIFEST.md). This additive notice supersedes narrower earlier interpretations; it does not alter archived original documents.

---

[Master index](00_MASTER_INDEX.md)

## Observed layers

1.Server-delivered HTML/bootstrap state and generated route tables.
2.Page-specific `/r2/client-packages/<page>/<version>/`apps with eagerly shared and lazy chunks.
3.Vue compiled components and Pinia store creation/imports in saved analysis/play packages. Svelte-related compiled runtime/style markers also exist; no claim of one uniform framework across the whole site.
4.Shared cc-*component/designsystem and chess custom elements.
5.Workers for UCI engines/CEE and browser storage for preferences/assets.
6.Network adapters for full review,QuickAnalysisverificationandotherservices.

- [1,213static script import records](../registries/script-imports.json)
- [Browser storage call-site contexts](../registries/browser-storage.json)
- [Technology lexical indicators and false-positive caveats](../registries/technology-literal-indicators.json)
- [Prior frontend call-site findings](../history/prior-audit/06_FRONTEND_ARCHITECTURE.md)

A static import may be unused,conditionally loaded or code-split; it is not a runtime fetch. No source-map references were found by the explicit `sourceMappingURL`scan of the selected existing code/HTML. No broad `.map`path guessing was performed. Authoring languages,repository layout,template framework and precise package major versions remain unknown where not literal.
