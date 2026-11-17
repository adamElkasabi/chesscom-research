# Build system and dependencies

[Master index](00_MASTER_INDEX.md)

RuntimeevidenceincludesEmscriptenstyleModule/ccall/HEAPU8/Asyncify,protobuf schemas and embedded native engine code,Vue/Piniaimports,Svelte-related runtime patterns,Viteassetpaths,hashed client packages and workers. Noall-platformlockfile/composer.lock/package.json build manifest was available.

Reproducibilitytoolsused:newanalysisPythonstdlib,Node20.20.2,WABTnpm1.0.39,andnativeDebianWABT1.0.36. Toolswerenotinterpretedaswebsite dependencies. NativeandJSdecompilershavedifferentoutcomes,allretained. Thepriorprotobufdecoderextractionisprecomputedinthepreservedcorpus.

WASMtoolchainexactversioncannotbeobtainedfromanabsentproducerssection. Fivebinarieshavezero customsections,noDWARF/name metadata;export/import names and native error strings still provide some anchors.

[Tool commands per module](wasm-analysis/module-manifest.json) · [Reproducibility scripts](tools/INDEX.md)

