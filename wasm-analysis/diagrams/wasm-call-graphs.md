# WASM call graphs

[Master](../00_WASM_MASTER_INDEX.md)

Completeper-modulemachinegraphsareinmodules/<id>/call-graph.jsonl.gz. Graphsincludeexactdirectcallsbutnotresolveddynamiccall_indirecttargets.

```mermaid
flowchart TD
 A[CEE_InitWithOpts export function1666 SIMD] --> B[Internal function1664]
 C[CEE_Init] --> Other[Direct callees indexed in functions JSON]
 Async[Asyncify state globals] --> A
 B -. detailed callee semantics not fully reconstructed .-> U[Unknown initialization internals]
 Note[Complete direct-call pairs in per-module call-graph JSONL; indirect targets unresolved]
```
