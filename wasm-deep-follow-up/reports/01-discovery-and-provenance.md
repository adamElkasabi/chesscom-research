# Discovery and provenance

## Verified starting point

The authoritative baseline ZIP contained 2,475 members and 100,385,944 bytes, with SHA256:

`aa4a215514161ca7f588a0dda342e36bace49ead965012e2ec0662bb4ef9321f`

It was verified before extraction. Every baseline member's contents are checked again against the replacement. Compression changes do not change member contents.

## Search coverage

The loader/reference scan fully reads 423 selected distinct textual sources from the existing manifest. `discovery-source-scan.json` records exact source IDs, locations, bytes, and hashes. This is **not** a claim to have OCR-reviewed every screenshot or semantically interpreted every source.

Discovery followed historical WASM references; default/no-SIMD/no-Worker/single variants; embedded Rive package versions; primary/fallback URLs; multipart loader logic; workers; source maps; model references; and inline `Uint8Array` modules. Constructed URL candidates are marked as such.

| Evidence log | GET records | Meaning |
|---|---:|---|
| `retrieval-log.json` | 37 | Binary/reference attempts, aliases, failures, HTML, six Torch parts |
| `companion-loader-retrieval.json` | 24 | Declared or derived wrapper URLs |
| `additional-companion-retrieval.json` | 3 | Multipart wrapper and two Rive source maps |
| `worker-and-glue-default-retrieval.json` | 6 | Four worker defaults and two generated-glue defaults; all 404 |
| `model-companion-retrieval.json` | 4 | Two WDL 404s and two complete NNUE 200 payloads |

**Total: 74 HTTP GET records across five logs.** No credentials, cookies, private keys, signed-URL bypass, or unauthorized testing were used. Returned HTTP metadata are retained where available; missing headers or timestamps are not fabricated.

## Identity rules applied

- `binary-inventory.json` is the unique complete-module inventory by SHA256.
- URL identity is separate from binary identity. Equal filenames or exports do not merge modules.
- A GitHub HTML response is not a module. A magic prefix alone is not sufficient proof of a complete module.
- Torch part zero was removed as a standalone identity. The loader declares six parts and concatenates them in numeric order. The resulting 74,951,979-byte module validates, with SHA256 `38b70a9507d46b1f2b6f73583b7658cda514041e72beb7ae8708eb995d688b30`.
- Four inline/constructed capability probes have their own exact bytes and identities. Four-byte magic-comparison constants are not modules.
- JavaScript `.data` properties are not asset paths. `classified-companion-assets.json` separates concrete NNUE parameters, opening books, frontend WDL metadata, and unresolved model/data candidates.

## Discovery boundary

This was a bounded passive/static investigation with legitimate public retrieval. It does not enumerate every imaginable version number, authenticated production request, screenshot-only reference, dynamic script payload, or unobserved asset catalog. The inventory is expanded evidence, not proof of universal completeness.
