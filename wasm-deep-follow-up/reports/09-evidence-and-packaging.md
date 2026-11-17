# Evidence, packaging, and reproduction

## Baseline preservation and replacement

The old ZIP is retained until replacement QC passes, then atomically replaced at the canonical `website-complete-forensic-audit.zip` path. Every baseline member's contents remain unchanged. The existing restore map and `restore-workspace.py` remain usable because the canonical filename and member paths are preserved.

## Compression compatibility

This archive uses **ZIPLZMA, method 14**. Python 3's `zipfile` and 7-Zip support it; some built-in unzip viewers do not. Plain JSONL members can be streamed through `zipfile.open`. They are not nested gzip in the final ZIP.

## Explicit raw-payload exclusions

The original five baseline binaries remain embedded. Newly retrieved large runtime binaries and NNUE parameter payloads were analyzed in scratch but are **not all embedded**, because the persistent workspace is capped. Every such decision is recorded in `packaging-retention.json` with exact URLs, bytes, hashes, status, and reason. Inline probes are included.

The retrieval logs, all derived structural/semantic records, source-map contents, bounded source evidence, and analysis scripts are included. This is an explicit delivery limitation, not complete raw-evidence preservation.

`retrieve-evidence.py` restores excluded public payloads to a downloaded local copy, checking exact SHA256. Multipart Torch uses six ordered part URLs, individual part checks, concatenation, and a final hash check. Mutable upstream URLs may change or disappear; the helper cannot guarantee future availability. Large restoration is not automatic inside this capped workspace.

## Privacy and reproducibility

Public source-map/glue text is scrubbed for email and obvious bearer credentials, while raw acquisition hashes remain in provenance. Pattern-based screening is not proof that every possible PII format is absent. Raw versus scrubbed content hashes and offsets must not be confused.

Scripts under `tools/` document the actual method and retain scratch defaults/toolchain dependencies. They are not represented as a fully portable one-command installation. The exact WABT opcode metadata is retained; native WABT/V8 tool versions and outcomes are recorded.

The follow-up has its own source/finding indices and checksums without renumbering historical IDs. The final QC report records member preservation, CRC, manifests, status totals, JSON parsing, and archive size.

## Lossless analysis container

To fit the persistence budget without deleting any baseline member or function record, the 493 logical files under `deep-functions/` are stored in **`analysis-evidence.tar.xz`**. Repetitive direct callsites use lossless delta-varint encoding; indirect callsites use lossless column/dictionary encoding. All other files are unchanged. `analysis-logical-members.json` records both physical and decoded hashes. Verification restored every logical member to exactly its original bytes.

After extracting the outer ZIP locally, change to `website-audit/wasm-deep-follow-up/` and run:

```sh
python3 materialize-analysis.py --output .
```

This uses only Python's standard library, expands roughly 620 MiB of records, and checks every output hash. Do not expand it inside the capped agent workspace. Until materialized, report references to `deep-functions/...` identify logical container members rather than directly extracted ZIP files.

The 40,119,326-byte `nn-5af11540bbfe.nnue` acquisition matches a preserved baseline member byte-for-byte and is therefore already embedded. The other newly retrieved NNUE network is excluded explicitly. No duplicate copy of an identical payload is needed.
