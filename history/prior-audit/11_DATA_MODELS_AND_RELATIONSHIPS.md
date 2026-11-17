# Data models and relationships

[Master index](00_MASTER_INDEX.md)

17254structured schema declaration records preserve rendered frontend and native descriptors separately. Field numbers,types,repetition,oneofs,enumvalues,packages and service methods are retained. These are protocol/interface models,not database schemas; optional fields need not appear in every payload. Duplicate namespaces and wire-compatible variants are not silently merged.

- [Complete schema registry](registries/schemas.json)
- [Decoded native descriptor files](registries/native-descriptors/)
- [Detailed data-model findings](findings/FINDINGS_INDEX.md)

## Curated model distinctions

- [FND-18890](findings/data_models-124.md#FND-18890) — Full frontend descriptors retain service metadata omitted by old rendered schemas
- [FND-18912](findings/data_models-124.md#FND-18912) — Compact CEE classification enum differs from legacy analysis enum
- [FND-18913](findings/data_models-124.md#FND-18913) — MoveClassificationVersion numeric names
- [FND-18914](findings/data_models-124.md#FND-18914) — White-point-of-view scores and board-bar pawn scores
- [FND-18915](findings/data_models-124.md#FND-18915) — Skills hash prerequisites do not prove cryptographic security
- [FND-18916](findings/data_models-124.md#FND-18916) — Both native and frontend metadata versions are retained

Native-interface and field-level entries are split into bounded findings files rather than repeated here.
