# Packaging and storage


## Focused Torch Human / bot-personality follow-up

The Torch Human/bots overlay has its own path/hash/change manifest. It adds public source/evidence and updates explanatory reports only; the 11,946,339-byte Topaz model is hash-recorded but not embedded. Old file/count/QA manifests remain baseline snapshots rather than silently regenerated totals.

[Evidence-graded focused update](torch-human-bots-update/00_START_HERE.md) · [Overlay change manifest](TORCH_HUMAN_BOTS_PATCH_MANIFEST.md). This additive notice supersedes narrower earlier interpretations; it does not alter archived original documents.

---

[Master index](00_MASTER_INDEX.md)

The primary ZIP contains every report, all prior recovery evidence, all five available original WASM binaries, their loaders, full structural/function/call inventories, offset-linked strings, small full WAT translations, selected CEE/Torch WAT excerpts, successful Stockfish decompilations, code-only Torch pseudocode, and focused CEE export pseudocode.

## Exact exclusions

[packaging-exclusions.json](audit-metadata/packaging-exclusions.json) lists each large omitted intermediate, its measured bytes and SHA-256. Full CEE WAT is about 1.6 GB uncompressed per variant. Those full text translations and the Torch text data/weight duplication do not fit the persistent workspace with useful headroom. They can be regenerated from the included exact binaries using the recorded tools. Exclusion is not a claim that these artifacts were never generated. Failed full decompilation outputs are not represented as recovered source.

No available WASM binary is excluded. Further referenced versions and multipart assets were not downloaded; their limitations are separately recorded in wasm-url-references.json. These are retrieval gaps, not packaging exclusions.

## Original material and privacy

Original documentation was not edited. The package contains separately labelled redacted copies and original-byte hashes. Existing unredacted research/source archives remain in the user's workspace and are not silently included in a new download that promises privacy redaction. The prior audit's full redacted evidence corpus is preserved under history/prior-audit.

The unused Stockfish NNUE and opening-book files are retained under preserved-workspace; other inactive assets are represented by the identical original bytes in module directories. The restore map records exact paths and hashes. This is lossless content consolidation, not a patch to a binary. Existing release ZIPs remain unchanged outside this audit ZIP.

To keep the total workspace within its limit, the final verified ZIP replaces redundant expanded/archived audit copies and becomes the storage location for the active CEE loader/binary as well. The extension's source code remains unchanged, but engine execution requires `python3 restore-workspace.py active-cee`. Restoring the engine consumes about 32 MiB; move a large archive off-workspace first if necessary. Research restoration remains available separately.
