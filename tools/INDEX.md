# Reproducibility tools

[Master](../chapters/00_MASTER_INDEX.md)

Scriptsretainexplicitfilesystempathsusedinthisbatch;adaptBASE/ROOTbeforeoutsideexecution. Theyareanalysisutilities,notproductionwebsitecode. Do notexecuteuntrustedmoduleswithoutthelistedresource/capabilitylimits.

- [architecture_extract.py](architecture_extract.py)
- [build_architecture.py](build_architecture.py)
- [focused_decompile.py](focused_decompile.py)
- [passive_research.py](passive_research.py)
- [render_mission.py](render_mission.py)
- [runtime_probe.cjs](runtime_probe.cjs)
- [runtime_probe.py](runtime_probe.py)
- [wasm_analyze.py](wasm_analyze.py)

WABTversions:JS1.0.39andnative1.0.36. npmtoolsarenotbundledtoavoidsnapshotbloat;installintotemporaryscratch. FullWATreproduction:`wasm2wat --enable-all module.wasm -o module.wat`. ThiscanexpandCEEtoabout1.6GBpermodule;checkdiskspaceandlimitsfirst.
