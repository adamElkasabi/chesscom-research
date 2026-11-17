# Memory, static data, and companion resources


## Focused Torch Human / bot-personality follow-up

Newly recovered companion: public topaz_jackdaw.bin.q8mix, SHA256 1f78db3d3184550ff56db7a0f14b72910b039a894dcc97ff8ef7bb8915f26423, self-described charm-small; 134 tensor records parsed and model-dependent native bot move executed. It is distinct from old failed resources/NNUE files.

[Evidence-graded focused update](../../torch-human-bots-update/00_START_HERE.md) · [Overlay change manifest](../../TORCH_HUMAN_BOTS_PATCH_MANIFEST.md). This additive notice supersedes narrower earlier interpretations; it does not alter archived original documents.

---

Every module has a `memory-data-map.json` with active/passive segment lengths, hashes, binary offsets, initial memory addresses, and bounded hex previews. Limits and shared/memory64 flags are structural facts; `memory.grow` instruction counts are separate observations. Runtime heap shape, growth, and allocation lifetimes were not measured.

Baseline facts remain:

| Module | Memory |
|---|---|
| CEE 001/002 | 386 MiB initial, 2 GiB maximum, nonshared |
| Stockfish 003 | Fixed 512 MiB imported shared memory |
| Stockfish 004 | 64 MiB initial, 2 GiB maximum, nonshared |
| Torch 005 | Fixed 512 MiB, nonshared |

New modules' exact declarations are in the comparison matrix. Variant names are not treated as proof of thread support.

## Bounded CEE layout reconstruction

- Composite game handle: arithmetic high part shifted by 20, low 20-bit mask.
- Lookup container: bucket pointer +28, bucket count +32, nonempty/state field +40.
- Lookup node: next +0, hash +4, key +8, value object +12, control pointer +16.
- Shared output pair: two 32-bit pointers; observed control-block counter at +4.
- Feature construction requests 184 bytes; one counted-pool path requests 44 bytes. This does not mean all fields are known.
- Small-string-style patterns use a sign byte at +11 and pointer/length fields. Exact source `std::string` typedef/ABI is inferred, not recovered from debug types.
- The JS protobuf command bridge allocates request bytes and an 8,192-byte response buffer, calls a four-number ABI, copies via `.slice()`, then frees. This is marshalling evidence, not proof that every native path respects the capacity or every schema is mapped.

## Two actual NNUE networks

| Public filename | Complete bytes | SHA256 |
|---|---:|---|
| `nn-ad9b42354671.nnue` | 47,001,499 | `ad9b423546714137916bd38978af6fd68d7b8951bef25ff76bf43da72d6cb786` |
| `nn-5af11540bbfe.nnue` | 40,119,326 | `5af11540bbfefcb54e38c5dd000cab4b469dfa7599a1d55be5d2722c20a8929b` |

Both returned HTTP 200 in full. Their observed NNUE-layout version is `0x7af32f20`, with different architecture hashes and the 75-byte description:

> Network trained with the https://github.com/glinscott/nnue-pytorch trainer.

This is real parameter-file evidence. Complete tensor decoding and compatibility with every Stockfish build are not established. Historical one-byte 206 responses are not substituted for these full acquisitions.

## Other companion boundaries

Saved HTML explicitly declares `/bundles/web/wdl/model.json` and `group1-shard1of1.bin`; both returned 404 in this pass. They are frontend WDL leads, not proven CEE/Torch imports. Already-abandoned coach/charm endpoints were not reprobed. The Charm bridge accepts model bytes and an optional key, but no private key or encrypted model was bypassed/recovered.

Large Torch data sections demonstrate static-payload variation, not automatically a `.pt`, ONNX format, tensor layout, or recovered model algorithm. Opening books are classified separately; hundreds are optional application assets, not proven dependencies of every WASM module. JavaScript `.data` properties are not asset paths.
