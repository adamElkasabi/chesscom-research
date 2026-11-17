# CEE semantic reconstruction: bounded, hash-specific case studies


## Focused Torch Human / bot-personality follow-up

Later focused evidence adds features9/61/70, confirms different Human search results with the same evaluation engine identifier, and separates native CEE1.211.5 from UCI/package1.130.285.

[Evidence-graded focused update](../../torch-human-bots-update/00_START_HERE.md) · [Overlay change manifest](../../torch-human-bots-update/TORCH_HUMAN_BOTS_PATCH_MANIFEST.md). This additive notice supersedes narrower earlier interpretations; it does not alter archived original documents.

---

All native function indices here refer **only** to `module-002`, SHA256:

`b94aaeec32ee0458aeba42a9d431a15f37c16740c030868c691c0697b3203373`

Indices are not assumed stable across builds. Non-export names below are inferred labels, not recovered source names. Raw evidence is in the connected-slice manifest/decompilation, function/table/memory records, and baseline JavaScript bridge.

## 1. Initialization options are not established pointer/length

`CEE_InitWithOpts` (1666) takes two i32 values and forwards them to 1664 behind Asyncify guards. In 1664, normal-flow values are clamped and passed to count-consuming initializers. The earlier “pointer/length probable” ABI placeholder is therefore **superseded**, not repeated as fact.

`CEE_Init` (1667), normal-flow pseudocode:

```text
available = fn22950()
second = clamp(available, 2, 9) - 1
fn1664(1, second)
```

Function 22950 calls `invoke_ii(slot=26277, argument=84)`, returns the positive result or zero, and propagates exceptions. Initial table slot 26277 targets 22947, a sysconf-style query.

The latter reads a signed 16-bit sentinel at `8679184 + 2*key`, then handles negative sentinels through a switch. At key 84 the original bytes are `07ff` = -249; the corresponding switch case returns 1. Under the original static table/data, default `CEE_Init` consequently invokes `1664(1,1)`.

This is an **initial-state reconstruction**, not a measured production configuration or proof of one physical core. The table or memory may change. Exact user-facing option names remain unknown.

Function 1664 initializes stream/runtime state, clamps at least one count to `1..min(available,8)`, calls initial slot 2000 → 1950, conditionally follows another counted path through slot 2002 → 252, and initializes three global collections through 1731. Function 1950 allocates 44-byte objects and appends pointers to vector-like globals at 12158908/12158912/12158916, followed by task/thread-related construction.

**Status:** 1666/1667/22950/22947 mostly understood with qualified boundaries; 1664/1950 partial. The runtime bookkeeping is not a chess algorithm.

## 2. Game handles have a concrete composite bit layout

NewFeature's candidate body 1686 reaches function 1741 through initial slot 2026. Its normal-flow behavior is:

```text
high = arithmetic_shift_right_i32(handle, 20)
low  = handle & 0x000fffff
pair = fn1670_lookup(global_collection_12157984, high)
if pair.object == null:
    result = null
else:
    base = fn7890(pair.object)
    result = fn8691(base, low)
release_temporary_shared_ownership(pair.control)
return result
```

The 20-bit split is exact. A public game handle is therefore not established as a raw linear-memory pointer. “High collection key / low subentry selector” is a bounded interpretation; no generation-counter meaning or board struct is invented. Functions 7890 and 8691 remain semantic boundaries.

**Status:** 1741 mostly understood.

## 3. The registry lookup is a reconstructable algorithm

Function 1670 takes an output pair, container pointer, and integer key. Normal-flow pseudocode:

```text
enter_or_lock(container + 4)
count   = load_u32(container + 32)
buckets = load_pointer(container + 28)
if count == 0 or load_u32(container + 40) == 0:
    write_zero_pair(); unlock(); return

bucket = key & (count - 1) if popcount(count) <= 1
         else key if key < count else key % count
node = first_chain_node(buckets[bucket])
while node != null and bucket_of(node.hash, count) == bucket:
    if node.hash == key and node.key == key:
        out.object  = node.value_object   # node +12
        out.control = node.value_control  # node +16
        if out.control: increment_refcount(out.control + 4)
        unlock(); return
    node = node.next
write_zero_pair()
unlock()
```

The power-of-two masking versus modulo selection and chained lookup are real algorithm evidence. Offsets describe this 32-bit build, not a universal C++ ABI. C++ unordered-map/shared-pointer attribution is supported by the pattern, but exact typedefs and concurrency guarantees are not recovered.

Function 1671 repeats the bucket/key walk, then invokes unlink helper 1672 and reference-count/destructor cleanup. Removing an entry is not assumed equivalent to one `free`.

**Status:** lookup 1670 mostly understood; erase 1671 partial.

## 4. NewFeature: marshalling, factory, parse, registration

The baseline JavaScript bridge supplies four numeric arguments:

```text
bytes = jsBuffer.length * jsBuffer.BYTES_PER_ELEMENT
p = malloc(bytes)
HEAPU8.set(jsBuffer, p)
try:
    h = ccall('CEE_NewFeature', number,
              [number,number,number,number],
              [gameHandle, featureID, p, bytes])
    post_error_if(h < 0) else post_handle(h)
finally:
    if p != 0: free(p)
```

This proves the JS staging-buffer lifetime. It does not prove every native path copies all bytes before return. Typed-array behavior must be checked against real callers; all non-Uint8 cases have not been validated.

Export 1694 is an Asyncify/exception shell. Initial slot 2038 → 1686 exposes these stages:

1. Resolve the composite game handle through 1741.
2. Enter feature-ID-driven factory/descriptor work, including slot 2027 → 1984 and slot 2028 → 1687.
3. Follow an input-message validation/parse path with the exact error text **“Unable to parse feature message”** at memory 115868.
4. Allocate 184 bytes and invoke constructor-like function 1961.
5. Insert into global registry 12157936 through slot 2031 → 1688 and return a handle.
6. Handle exceptions and error/log formatting, including **“exception occurred: {}; callstack: {}”** and **“unknown exception occurred”**.

Conservative pseudocode:

```text
NewFeature(gameHandle, featureID, input, length):
    game = resolve_composite_handle(gameHandle)
    factory_state = feature_factory_dispatch(featureID, game, ...unknown...)
    descriptor = resolve_feature_descriptor(featureID)
    parse_and_validate_input_or_report_error()
    feature = construct_state_in_184byte_allocation(...unknown fields...)
    return insert_feature_registry(feature)
```

Function 1984 is 31,638 bytes and decompiles to approximately 200 KB. It is preserved in the selected connected analysis, but most of its large lazy-initialization/factory branches are not interpreted. There is no proven exhaustive feature-ID-to-schema dictionary or reconstructed scoring formula.

**Status:** 1694/1686 partial; 1984 structurally analyzed. The presence of parser errors does not identify review classification math.

## 5. Run and disposal use the same registry family

JavaScript calls `CEE_Run(handle,0)` through async `ccall`; a result ≤0 produces an error. The integer return is not established as the completed score payload; output/completion have separate bridge channels.

Export 1699 reaches candidate body 1698 through initial slot 2052. That body uses initial slot 2043 → 1670 to look up a handle in global registry 12157936. Its failure path contains **“Invalid Feature handle”** at memory 114487. Later object/virtual/host-mediated work dispatch and cleanup remain only partially interpreted.

Disposal export 1697 reaches 1671 through initial slot 2041. The resulting map erase and shared-ownership cleanup are stronger evidence of a feature-handle API than the misleading JS local variable name `game_point` in that wrapper.

**Status:** Run/disposal shells and candidate Run body partial. Actual feature execution, callback schemas, and scheduling remain open.

## 6. Compiler state is not domain state

Global 0 initializes to 26,691,088 and acts as the linear-memory stack pointer in selected decompiled frames. Global 2/3 usage is consistent with Asyncify state/data bookkeeping: normal, unwind, and rewind paths. Memory word 18297676 is repeatedly used around Emscripten exception wrappers.

Those patterns must not be renamed as chess feature/classification states. Readable pseudocode above omits bookkeeping only for explanation; raw decompilation retains it. Cleanup and exception paths are not claimed equivalent to normal flow.
