# Expanded audit — deep WASM follow-up

**PARTIALLY AUDITED. The extreme-depth semantic mission is not fully complete.**

[Read the new follow-up](reports/00-START-HERE.md).

29 module identities include 25 downloaded/assembled runtimes and 4 inline probes. There are 225,335 explicitly statused defined functions; most remain structural. The original 2,475 baseline members are preserved byte-for-byte. New large raw runtime/parameter exclusions are explicit, not concealed.

This ZIP uses ZIPLZMA: use Python3 zipfile or 7-Zip if your extractor does not support it. The 493 complete logical analysis files are in a lossless nested container. To restore them, extract the outer ZIP locally, change to `website-audit/wasm-deep-follow-up/`, then run:

```sh
python3 materialize-analysis.py --output .
```

This expands about 620 MiB and verifies all decoded hashes. Do not expand it inside the capped agent workspace. Small reports and selected CEE decompilation/CFGs are directly accessible in the outer ZIP.

Canonical ZIP filename/member paths remain unchanged so `restore-workspace.py` continues to work.
