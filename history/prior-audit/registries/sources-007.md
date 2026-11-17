# Source inventory

[Master index](../00_MASTER_INDEX.md)

## SRC-0601 — `research/proto/chesscom/user_properties/v1/properties_activity.proto`

- Type: rendered_protobuf_schema; bytes: 7399; SHA-256: `e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 179; types: {"verified observation": 179}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/e4530f3517f3bd03654957b3fcdaec2630f90e890ca3ae168e4808d5750a01a7.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-09938](../findings/data_models-097.md#FND-09938), [FND-09939](../findings/data_models-097.md#FND-09939), [FND-09940](../findings/data_models-097.md#FND-09940), [FND-09941](../findings/data_models-097.md#FND-09941), [FND-09942](../findings/data_models-097.md#FND-09942), [FND-09943](../findings/data_models-097.md#FND-09943), [FND-09944](../findings/data_models-097.md#FND-09944), [FND-09945](../findings/data_models-097.md#FND-09945), [FND-09946](../findings/data_models-097.md#FND-09946), [FND-09947](../findings/data_models-097.md#FND-09947), [FND-09948](../findings/data_models-097.md#FND-09948), [FND-09949](../findings/data_models-097.md#FND-09949), [FND-09950](../findings/data_models-097.md#FND-09950), [FND-09951](../findings/data_models-097.md#FND-09951), [FND-09952](../findings/data_models-097.md#FND-09952), [FND-09953](../findings/data_models-097.md#FND-09953), [FND-09954](../findings/data_models-097.md#FND-09954), [FND-09955](../findings/data_models-097.md#FND-09955), [FND-09956](../findings/data_models-097.md#FND-09956), [FND-09957](../findings/data_models-097.md#FND-09957), [FND-09958](../findings/data_models-097.md#FND-09958), [FND-09959](../findings/data_models-097.md#FND-09959), [FND-09960](../findings/data_models-097.md#FND-09960), [FND-09961](../findings/data_models-097.md#FND-09961), [FND-09962](../findings/data_models-097.md#FND-09962), [FND-09963](../findings/data_models-097.md#FND-09963), [FND-09964](../findings/data_models-097.md#FND-09964), [FND-09965](../findings/data_models-097.md#FND-09965), [FND-09966](../findings/data_models-097.md#FND-09966), [FND-09967](../findings/data_models-097.md#FND-09967), [FND-09968](../findings/data_models-097.md#FND-09968), [FND-09969](../findings/data_models-097.md#FND-09969), [FND-09970](../findings/data_models-097.md#FND-09970), [FND-09971](../findings/data_models-097.md#FND-09971), [FND-09972](../findings/data_models-097.md#FND-09972), [FND-09973](../findings/data_models-097.md#FND-09973), [FND-09974](../findings/data_models-097.md#FND-09974), [FND-09975](../findings/data_models-098.md#FND-09975), [FND-09976](../findings/data_models-098.md#FND-09976), [FND-09977](../findings/data_models-098.md#FND-09977), [FND-09978](../findings/data_models-098.md#FND-09978), [FND-09979](../findings/data_models-098.md#FND-09979), [FND-09980](../findings/data_models-098.md#FND-09980), [FND-09981](../findings/data_models-098.md#FND-09981), [FND-09982](../findings/data_models-098.md#FND-09982), [FND-09983](../findings/data_models-098.md#FND-09983), [FND-09984](../findings/data_models-098.md#FND-09984), [FND-09985](../findings/data_models-098.md#FND-09985), [FND-09986](../findings/data_models-098.md#FND-09986), [FND-09987](../findings/data_models-098.md#FND-09987), [FND-09988](../findings/data_models-098.md#FND-09988), [FND-09989](../findings/data_models-098.md#FND-09989), [FND-09990](../findings/data_models-098.md#FND-09990), [FND-09991](../findings/data_models-098.md#FND-09991), [FND-09992](../findings/data_models-098.md#FND-09992), [FND-09993](../findings/data_models-098.md#FND-09993), [FND-09994](../findings/data_models-098.md#FND-09994), [FND-09995](../findings/data_models-098.md#FND-09995), [FND-09996](../findings/data_models-098.md#FND-09996), [FND-09997](../findings/data_models-098.md#FND-09997), [FND-09998](../findings/data_models-098.md#FND-09998), [FND-09999](../findings/data_models-098.md#FND-09999), [FND-10000](../findings/data_models-098.md#FND-10000), [FND-10001](../findings/data_models-098.md#FND-10001), [FND-10002](../findings/data_models-098.md#FND-10002), [FND-10003](../findings/data_models-098.md#FND-10003), [FND-10004](../findings/data_models-098.md#FND-10004), [FND-10005](../findings/data_models-098.md#FND-10005), [FND-10006](../findings/data_models-098.md#FND-10006), [FND-10007](../findings/data_models-098.md#FND-10007), [FND-10008](../findings/data_models-098.md#FND-10008), [FND-10009](../findings/data_models-098.md#FND-10009), [FND-10010](../findings/data_models-098.md#FND-10010), [FND-10011](../findings/data_models-098.md#FND-10011), [FND-10012](../findings/data_models-098.md#FND-10012), [FND-10013](../findings/data_models-098.md#FND-10013), [FND-10014](../findings/data_models-098.md#FND-10014), [FND-10015](../findings/data_models-098.md#FND-10015), [FND-10016](../findings/data_models-098.md#FND-10016), [FND-10017](../findings/data_models-098.md#FND-10017), [FND-10018](../findings/data_models-098.md#FND-10018), [FND-10019](../findings/data_models-098.md#FND-10019), [FND-10020](../findings/data_models-098.md#FND-10020), [FND-10021](../findings/data_models-098.md#FND-10021), [FND-10022](../findings/data_models-098.md#FND-10022), [FND-10023](../findings/data_models-098.md#FND-10023), [FND-10024](../findings/data_models-098.md#FND-10024), [FND-10025](../findings/data_models-098.md#FND-10025), [FND-10026](../findings/data_models-098.md#FND-10026), [FND-10027](../findings/data_models-098.md#FND-10027), [FND-10028](../findings/data_models-098.md#FND-10028), [FND-10029](../findings/data_models-098.md#FND-10029), [FND-10030](../findings/data_models-098.md#FND-10030), [FND-10031](../findings/data_models-098.md#FND-10031), [FND-10032](../findings/data_models-098.md#FND-10032), [FND-10033](../findings/data_models-098.md#FND-10033), [FND-10034](../findings/data_models-098.md#FND-10034), [FND-10035](../findings/data_models-098.md#FND-10035), [FND-10036](../findings/data_models-098.md#FND-10036), [FND-10037](../findings/data_models-098.md#FND-10037), [FND-10038](../findings/data_models-098.md#FND-10038), [FND-10039](../findings/data_models-098.md#FND-10039), [FND-10040](../findings/data_models-098.md#FND-10040), [FND-10041](../findings/data_models-098.md#FND-10041), [FND-10042](../findings/data_models-098.md#FND-10042), [FND-10043](../findings/data_models-098.md#FND-10043), [FND-10044](../findings/data_models-098.md#FND-10044), [FND-10045](../findings/data_models-098.md#FND-10045), [FND-10046](../findings/data_models-098.md#FND-10046), [FND-10047](../findings/data_models-098.md#FND-10047), [FND-10048](../findings/data_models-098.md#FND-10048), [FND-10049](../findings/data_models-098.md#FND-10049), [FND-10050](../findings/data_models-098.md#FND-10050), [FND-10051](../findings/data_models-098.md#FND-10051), [FND-10052](../findings/data_models-098.md#FND-10052), [FND-10053](../findings/data_models-098.md#FND-10053), [FND-10054](../findings/data_models-098.md#FND-10054), [FND-10055](../findings/data_models-098.md#FND-10055), [FND-10056](../findings/data_models-098.md#FND-10056), [FND-10057](../findings/data_models-098.md#FND-10057), [FND-10058](../findings/data_models-098.md#FND-10058), [FND-10059](../findings/data_models-098.md#FND-10059), [FND-10060](../findings/data_models-098.md#FND-10060), [FND-10061](../findings/data_models-098.md#FND-10061), [FND-10062](../findings/data_models-098.md#FND-10062), [FND-10063](../findings/data_models-098.md#FND-10063), [FND-10064](../findings/data_models-098.md#FND-10064), [FND-10065](../findings/data_models-098.md#FND-10065), [FND-10066](../findings/data_models-098.md#FND-10066), [FND-10067](../findings/data_models-098.md#FND-10067), [FND-10068](../findings/data_models-098.md#FND-10068), [FND-10069](../findings/data_models-098.md#FND-10069), [FND-10070](../findings/data_models-098.md#FND-10070), [FND-10071](../findings/data_models-098.md#FND-10071), [FND-10072](../findings/data_models-098.md#FND-10072), [FND-10073](../findings/data_models-098.md#FND-10073), [FND-10074](../findings/data_models-098.md#FND-10074), [FND-10075](../findings/data_models-099.md#FND-10075), [FND-10076](../findings/data_models-099.md#FND-10076), [FND-10077](../findings/data_models-099.md#FND-10077), [FND-10078](../findings/data_models-099.md#FND-10078), [FND-10079](../findings/data_models-099.md#FND-10079), [FND-10080](../findings/data_models-099.md#FND-10080), [FND-10081](../findings/data_models-099.md#FND-10081), [FND-10082](../findings/data_models-099.md#FND-10082), [FND-10083](../findings/data_models-099.md#FND-10083), [FND-10084](../findings/data_models-099.md#FND-10084), [FND-10085](../findings/data_models-099.md#FND-10085), [FND-10086](../findings/data_models-099.md#FND-10086), [FND-10087](../findings/data_models-099.md#FND-10087), [FND-10088](../findings/data_models-099.md#FND-10088), [FND-10089](../findings/data_models-099.md#FND-10089), [FND-10090](../findings/data_models-099.md#FND-10090), [FND-10091](../findings/data_models-099.md#FND-10091), [FND-10092](../findings/data_models-099.md#FND-10092), [FND-10093](../findings/data_models-099.md#FND-10093), [FND-10094](../findings/data_models-099.md#FND-10094), [FND-10095](../findings/data_models-099.md#FND-10095), [FND-10096](../findings/data_models-099.md#FND-10096), [FND-10097](../findings/data_models-099.md#FND-10097), [FND-10098](../findings/data_models-099.md#FND-10098), [FND-10099](../findings/data_models-099.md#FND-10099), [FND-10100](../findings/data_models-099.md#FND-10100), [FND-10101](../findings/data_models-099.md#FND-10101), [FND-10102](../findings/data_models-099.md#FND-10102), [FND-10103](../findings/data_models-099.md#FND-10103), [FND-10104](../findings/data_models-099.md#FND-10104), [FND-10105](../findings/data_models-099.md#FND-10105), [FND-10106](../findings/data_models-099.md#FND-10106), [FND-10107](../findings/data_models-099.md#FND-10107), [FND-10108](../findings/data_models-099.md#FND-10108), [FND-10109](../findings/data_models-099.md#FND-10109), [FND-10110](../findings/data_models-099.md#FND-10110), [FND-10111](../findings/data_models-099.md#FND-10111), [FND-10112](../findings/data_models-099.md#FND-10112), [FND-10113](../findings/data_models-099.md#FND-10113), [FND-10114](../findings/data_models-099.md#FND-10114), [FND-10115](../findings/data_models-099.md#FND-10115), [FND-10116](../findings/data_models-099.md#FND-10116)

## SRC-0602 — `research/proto/chesscom/user_properties/v1/properties_analysis.proto`

- Type: rendered_protobuf_schema; bytes: 1478; SHA-256: `b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 33; types: {"verified observation": 33}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/b2db79442e97061d515f89467ec09e093b259cf1e074475cd066336f9c417193.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10117](../findings/data_models-099.md#FND-10117), [FND-10118](../findings/data_models-099.md#FND-10118), [FND-10119](../findings/data_models-099.md#FND-10119), [FND-10120](../findings/data_models-099.md#FND-10120), [FND-10121](../findings/data_models-099.md#FND-10121), [FND-10122](../findings/data_models-099.md#FND-10122), [FND-10123](../findings/data_models-099.md#FND-10123), [FND-10124](../findings/data_models-099.md#FND-10124), [FND-10125](../findings/data_models-099.md#FND-10125), [FND-10126](../findings/data_models-099.md#FND-10126), [FND-10127](../findings/data_models-099.md#FND-10127), [FND-10128](../findings/data_models-099.md#FND-10128), [FND-10129](../findings/data_models-099.md#FND-10129), [FND-10130](../findings/data_models-099.md#FND-10130), [FND-10131](../findings/data_models-099.md#FND-10131), [FND-10132](../findings/data_models-099.md#FND-10132), [FND-10133](../findings/data_models-099.md#FND-10133), [FND-10134](../findings/data_models-099.md#FND-10134), [FND-10135](../findings/data_models-099.md#FND-10135), [FND-10136](../findings/data_models-099.md#FND-10136), [FND-10137](../findings/data_models-099.md#FND-10137), [FND-10138](../findings/data_models-099.md#FND-10138), [FND-10139](../findings/data_models-099.md#FND-10139), [FND-10140](../findings/data_models-099.md#FND-10140), [FND-10141](../findings/data_models-099.md#FND-10141), [FND-10142](../findings/data_models-099.md#FND-10142), [FND-10143](../findings/data_models-099.md#FND-10143), [FND-10144](../findings/data_models-099.md#FND-10144), [FND-10145](../findings/data_models-099.md#FND-10145), [FND-10146](../findings/data_models-099.md#FND-10146), [FND-10147](../findings/data_models-099.md#FND-10147), [FND-10148](../findings/data_models-099.md#FND-10148), [FND-10149](../findings/data_models-099.md#FND-10149)

## SRC-0603 — `research/proto/chesscom/user_properties/v1/properties_attribution.proto`

- Type: rendered_protobuf_schema; bytes: 1184; SHA-256: `5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 30; types: {"verified observation": 30}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/5480283920adabb955ee9e5cb861bbf7f90c631318c7c4eb9496aaa8a0238e4e.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10150](../findings/data_models-099.md#FND-10150), [FND-10151](../findings/data_models-099.md#FND-10151), [FND-10152](../findings/data_models-099.md#FND-10152), [FND-10153](../findings/data_models-099.md#FND-10153), [FND-10154](../findings/data_models-099.md#FND-10154), [FND-10155](../findings/data_models-099.md#FND-10155), [FND-10156](../findings/data_models-099.md#FND-10156), [FND-10157](../findings/data_models-099.md#FND-10157), [FND-10158](../findings/data_models-099.md#FND-10158), [FND-10159](../findings/data_models-099.md#FND-10159), [FND-10160](../findings/data_models-099.md#FND-10160), [FND-10161](../findings/data_models-099.md#FND-10161), [FND-10162](../findings/data_models-099.md#FND-10162), [FND-10163](../findings/data_models-099.md#FND-10163), [FND-10164](../findings/data_models-099.md#FND-10164), [FND-10165](../findings/data_models-099.md#FND-10165), [FND-10166](../findings/data_models-099.md#FND-10166), [FND-10167](../findings/data_models-099.md#FND-10167), [FND-10168](../findings/data_models-099.md#FND-10168), [FND-10169](../findings/data_models-099.md#FND-10169), [FND-10170](../findings/data_models-099.md#FND-10170), [FND-10171](../findings/data_models-099.md#FND-10171), [FND-10172](../findings/data_models-099.md#FND-10172), [FND-10173](../findings/data_models-099.md#FND-10173), [FND-10174](../findings/data_models-099.md#FND-10174), [FND-10175](../findings/data_models-100.md#FND-10175), [FND-10176](../findings/data_models-100.md#FND-10176), [FND-10177](../findings/data_models-100.md#FND-10177), [FND-10178](../findings/data_models-100.md#FND-10178), [FND-10179](../findings/data_models-100.md#FND-10179)

## SRC-0604 — `research/proto/chesscom/user_properties/v1/properties_audiences.proto`

- Type: rendered_protobuf_schema; bytes: 693; SHA-256: `2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 13; types: {"verified observation": 13}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/2920715d3f2ce71fce8d860a903bf6d0879a90427e7c4881cd65f788939e2f29.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10180](../findings/data_models-100.md#FND-10180), [FND-10181](../findings/data_models-100.md#FND-10181), [FND-10182](../findings/data_models-100.md#FND-10182), [FND-10183](../findings/data_models-100.md#FND-10183), [FND-10184](../findings/data_models-100.md#FND-10184), [FND-10185](../findings/data_models-100.md#FND-10185), [FND-10186](../findings/data_models-100.md#FND-10186), [FND-10187](../findings/data_models-100.md#FND-10187), [FND-10188](../findings/data_models-100.md#FND-10188), [FND-10189](../findings/data_models-100.md#FND-10189), [FND-10190](../findings/data_models-100.md#FND-10190), [FND-10191](../findings/data_models-100.md#FND-10191), [FND-10192](../findings/data_models-100.md#FND-10192)

## SRC-0605 — `research/proto/chesscom/user_properties/v1/properties_clubs.proto`

- Type: rendered_protobuf_schema; bytes: 392; SHA-256: `9a7e8594cfa50a28ab9c21051573052d74b5ba58e75fee1a0d329db3ecd56ea8`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 9; types: {"verified observation": 9}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/9a7e8594cfa50a28ab9c21051573052d74b5ba58e75fee1a0d329db3ecd56ea8.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10193](../findings/data_models-100.md#FND-10193), [FND-10194](../findings/data_models-100.md#FND-10194), [FND-10195](../findings/data_models-100.md#FND-10195), [FND-10196](../findings/data_models-100.md#FND-10196), [FND-10197](../findings/data_models-100.md#FND-10197), [FND-10198](../findings/data_models-100.md#FND-10198), [FND-10199](../findings/data_models-100.md#FND-10199), [FND-10200](../findings/data_models-100.md#FND-10200), [FND-10201](../findings/data_models-100.md#FND-10201)

## SRC-0606 — `research/proto/chesscom/user_properties/v1/properties_coaches.proto`

- Type: rendered_protobuf_schema; bytes: 1644; SHA-256: `9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 45; types: {"verified observation": 45}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/9d22dcf1f1f86e2975c9a632a3ce99bd7d53fb6374126205c20c22d6f07f3054.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10202](../findings/data_models-100.md#FND-10202), [FND-10203](../findings/data_models-100.md#FND-10203), [FND-10204](../findings/data_models-100.md#FND-10204), [FND-10205](../findings/data_models-100.md#FND-10205), [FND-10206](../findings/data_models-100.md#FND-10206), [FND-10207](../findings/data_models-100.md#FND-10207), [FND-10208](../findings/data_models-100.md#FND-10208), [FND-10209](../findings/data_models-100.md#FND-10209), [FND-10210](../findings/data_models-100.md#FND-10210), [FND-10211](../findings/data_models-100.md#FND-10211), [FND-10212](../findings/data_models-100.md#FND-10212), [FND-10213](../findings/data_models-100.md#FND-10213), [FND-10214](../findings/data_models-100.md#FND-10214), [FND-10215](../findings/data_models-100.md#FND-10215), [FND-10216](../findings/data_models-100.md#FND-10216), [FND-10217](../findings/data_models-100.md#FND-10217), [FND-10218](../findings/data_models-100.md#FND-10218), [FND-10219](../findings/data_models-100.md#FND-10219), [FND-10220](../findings/data_models-100.md#FND-10220), [FND-10221](../findings/data_models-100.md#FND-10221), [FND-10222](../findings/data_models-100.md#FND-10222), [FND-10223](../findings/data_models-100.md#FND-10223), [FND-10224](../findings/data_models-100.md#FND-10224), [FND-10225](../findings/data_models-100.md#FND-10225), [FND-10226](../findings/data_models-100.md#FND-10226), [FND-10227](../findings/data_models-100.md#FND-10227), [FND-10228](../findings/data_models-100.md#FND-10228), [FND-10229](../findings/data_models-100.md#FND-10229), [FND-10230](../findings/data_models-100.md#FND-10230), [FND-10231](../findings/data_models-100.md#FND-10231), [FND-10232](../findings/data_models-100.md#FND-10232), [FND-10233](../findings/data_models-100.md#FND-10233), [FND-10234](../findings/data_models-100.md#FND-10234), [FND-10235](../findings/data_models-100.md#FND-10235), [FND-10236](../findings/data_models-100.md#FND-10236), [FND-10237](../findings/data_models-100.md#FND-10237), [FND-10238](../findings/data_models-100.md#FND-10238), [FND-10239](../findings/data_models-100.md#FND-10239), [FND-10240](../findings/data_models-100.md#FND-10240), [FND-10241](../findings/data_models-100.md#FND-10241), [FND-10242](../findings/data_models-100.md#FND-10242), [FND-10243](../findings/data_models-100.md#FND-10243), [FND-10244](../findings/data_models-100.md#FND-10244), [FND-10245](../findings/data_models-100.md#FND-10245), [FND-10246](../findings/data_models-100.md#FND-10246)

## SRC-0607 — `research/proto/chesscom/user_properties/v1/properties_core.proto`

- Type: rendered_protobuf_schema; bytes: 1319; SHA-256: `065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 47; types: {"verified observation": 47}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/065aec516f7ccd528721c1281fd6f25a2ea34d25462121a88ca46a32a6218767.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10247](../findings/data_models-100.md#FND-10247), [FND-10248](../findings/data_models-100.md#FND-10248), [FND-10249](../findings/data_models-100.md#FND-10249), [FND-10250](../findings/data_models-100.md#FND-10250), [FND-10251](../findings/data_models-100.md#FND-10251), [FND-10252](../findings/data_models-100.md#FND-10252), [FND-10253](../findings/data_models-100.md#FND-10253), [FND-10254](../findings/data_models-100.md#FND-10254), [FND-10255](../findings/data_models-100.md#FND-10255), [FND-10256](../findings/data_models-100.md#FND-10256), [FND-10257](../findings/data_models-100.md#FND-10257), [FND-10258](../findings/data_models-100.md#FND-10258), [FND-10259](../findings/data_models-100.md#FND-10259), [FND-10260](../findings/data_models-100.md#FND-10260), [FND-10261](../findings/data_models-100.md#FND-10261), [FND-10262](../findings/data_models-100.md#FND-10262), [FND-10263](../findings/data_models-100.md#FND-10263), [FND-10264](../findings/data_models-100.md#FND-10264), [FND-10265](../findings/data_models-100.md#FND-10265), [FND-10266](../findings/data_models-100.md#FND-10266), [FND-10267](../findings/data_models-100.md#FND-10267), [FND-10268](../findings/data_models-100.md#FND-10268), [FND-10269](../findings/data_models-100.md#FND-10269), [FND-10270](../findings/data_models-100.md#FND-10270), [FND-10271](../findings/data_models-100.md#FND-10271), [FND-10272](../findings/data_models-100.md#FND-10272), [FND-10273](../findings/data_models-100.md#FND-10273), [FND-10274](../findings/data_models-100.md#FND-10274), [FND-10275](../findings/data_models-101.md#FND-10275), [FND-10276](../findings/data_models-101.md#FND-10276), [FND-10277](../findings/data_models-101.md#FND-10277), [FND-10278](../findings/data_models-101.md#FND-10278), [FND-10279](../findings/data_models-101.md#FND-10279), [FND-10280](../findings/data_models-101.md#FND-10280), [FND-10281](../findings/data_models-101.md#FND-10281), [FND-10282](../findings/data_models-101.md#FND-10282), [FND-10283](../findings/data_models-101.md#FND-10283), [FND-10284](../findings/data_models-101.md#FND-10284), [FND-10285](../findings/data_models-101.md#FND-10285), [FND-10286](../findings/data_models-101.md#FND-10286), [FND-10287](../findings/data_models-101.md#FND-10287), [FND-10288](../findings/data_models-101.md#FND-10288), [FND-10289](../findings/data_models-101.md#FND-10289), [FND-10290](../findings/data_models-101.md#FND-10290), [FND-10291](../findings/data_models-101.md#FND-10291), [FND-10292](../findings/data_models-101.md#FND-10292), [FND-10293](../findings/data_models-101.md#FND-10293)

## SRC-0608 — `research/proto/chesscom/user_properties/v1/properties_courses.proto`

- Type: rendered_protobuf_schema; bytes: 2412; SHA-256: `f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 54; types: {"verified observation": 54}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/f92d4f25a82671408f1364e61fcde5b3c904df7498ca7c0e8214250b01518566.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10294](../findings/data_models-101.md#FND-10294), [FND-10295](../findings/data_models-101.md#FND-10295), [FND-10296](../findings/data_models-101.md#FND-10296), [FND-10297](../findings/data_models-101.md#FND-10297), [FND-10298](../findings/data_models-101.md#FND-10298), [FND-10299](../findings/data_models-101.md#FND-10299), [FND-10300](../findings/data_models-101.md#FND-10300), [FND-10301](../findings/data_models-101.md#FND-10301), [FND-10302](../findings/data_models-101.md#FND-10302), [FND-10303](../findings/data_models-101.md#FND-10303), [FND-10304](../findings/data_models-101.md#FND-10304), [FND-10305](../findings/data_models-101.md#FND-10305), [FND-10306](../findings/data_models-101.md#FND-10306), [FND-10307](../findings/data_models-101.md#FND-10307), [FND-10308](../findings/data_models-101.md#FND-10308), [FND-10309](../findings/data_models-101.md#FND-10309), [FND-10310](../findings/data_models-101.md#FND-10310), [FND-10311](../findings/data_models-101.md#FND-10311), [FND-10312](../findings/data_models-101.md#FND-10312), [FND-10313](../findings/data_models-101.md#FND-10313), [FND-10314](../findings/data_models-101.md#FND-10314), [FND-10315](../findings/data_models-101.md#FND-10315), [FND-10316](../findings/data_models-101.md#FND-10316), [FND-10317](../findings/data_models-101.md#FND-10317), [FND-10318](../findings/data_models-101.md#FND-10318), [FND-10319](../findings/data_models-101.md#FND-10319), [FND-10320](../findings/data_models-101.md#FND-10320), [FND-10321](../findings/data_models-101.md#FND-10321), [FND-10322](../findings/data_models-101.md#FND-10322), [FND-10323](../findings/data_models-101.md#FND-10323), [FND-10324](../findings/data_models-101.md#FND-10324), [FND-10325](../findings/data_models-101.md#FND-10325), [FND-10326](../findings/data_models-101.md#FND-10326), [FND-10327](../findings/data_models-101.md#FND-10327), [FND-10328](../findings/data_models-101.md#FND-10328), [FND-10329](../findings/data_models-101.md#FND-10329), [FND-10330](../findings/data_models-101.md#FND-10330), [FND-10331](../findings/data_models-101.md#FND-10331), [FND-10332](../findings/data_models-101.md#FND-10332), [FND-10333](../findings/data_models-101.md#FND-10333), [FND-10334](../findings/data_models-101.md#FND-10334), [FND-10335](../findings/data_models-101.md#FND-10335), [FND-10336](../findings/data_models-101.md#FND-10336), [FND-10337](../findings/data_models-101.md#FND-10337), [FND-10338](../findings/data_models-101.md#FND-10338), [FND-10339](../findings/data_models-101.md#FND-10339), [FND-10340](../findings/data_models-101.md#FND-10340), [FND-10341](../findings/data_models-101.md#FND-10341), [FND-10342](../findings/data_models-101.md#FND-10342), [FND-10343](../findings/data_models-101.md#FND-10343), [FND-10344](../findings/data_models-101.md#FND-10344), [FND-10345](../findings/data_models-101.md#FND-10345), [FND-10346](../findings/data_models-101.md#FND-10346), [FND-10347](../findings/data_models-101.md#FND-10347)

## SRC-0609 — `research/proto/chesscom/user_properties/v1/properties_daily_puzzles_solved.proto`

- Type: rendered_protobuf_schema; bytes: 1081; SHA-256: `d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 21; types: {"verified observation": 21}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/d38f194a26d027fa39a78f5780670c550db5eaf9a9dba757d428a8b710536930.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10348](../findings/data_models-101.md#FND-10348), [FND-10349](../findings/data_models-101.md#FND-10349), [FND-10350](../findings/data_models-101.md#FND-10350), [FND-10351](../findings/data_models-101.md#FND-10351), [FND-10352](../findings/data_models-101.md#FND-10352), [FND-10353](../findings/data_models-101.md#FND-10353), [FND-10354](../findings/data_models-101.md#FND-10354), [FND-10355](../findings/data_models-101.md#FND-10355), [FND-10356](../findings/data_models-101.md#FND-10356), [FND-10357](../findings/data_models-101.md#FND-10357), [FND-10358](../findings/data_models-101.md#FND-10358), [FND-10359](../findings/data_models-101.md#FND-10359), [FND-10360](../findings/data_models-101.md#FND-10360), [FND-10361](../findings/data_models-101.md#FND-10361), [FND-10362](../findings/data_models-101.md#FND-10362), [FND-10363](../findings/data_models-101.md#FND-10363), [FND-10364](../findings/data_models-101.md#FND-10364), [FND-10365](../findings/data_models-101.md#FND-10365), [FND-10366](../findings/data_models-101.md#FND-10366), [FND-10367](../findings/data_models-101.md#FND-10367), [FND-10368](../findings/data_models-101.md#FND-10368)

## SRC-0610 — `research/proto/chesscom/user_properties/v1/properties_definition.proto`

- Type: rendered_protobuf_schema; bytes: 2095; SHA-256: `fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 48; types: {"verified observation": 48}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10369](../findings/data_models-101.md#FND-10369), [FND-10370](../findings/data_models-101.md#FND-10370), [FND-10371](../findings/data_models-101.md#FND-10371), [FND-10372](../findings/data_models-101.md#FND-10372), [FND-10373](../findings/data_models-101.md#FND-10373), [FND-10374](../findings/data_models-101.md#FND-10374), [FND-10375](../findings/data_models-102.md#FND-10375), [FND-10376](../findings/data_models-102.md#FND-10376), [FND-10377](../findings/data_models-102.md#FND-10377), [FND-10378](../findings/data_models-102.md#FND-10378), [FND-10379](../findings/data_models-102.md#FND-10379), [FND-10380](../findings/data_models-102.md#FND-10380), [FND-10381](../findings/data_models-102.md#FND-10381), [FND-10382](../findings/data_models-102.md#FND-10382), [FND-10383](../findings/data_models-102.md#FND-10383), [FND-10384](../findings/data_models-102.md#FND-10384), [FND-10385](../findings/data_models-102.md#FND-10385), [FND-10386](../findings/data_models-102.md#FND-10386), [FND-10387](../findings/data_models-102.md#FND-10387), [FND-10388](../findings/data_models-102.md#FND-10388), [FND-10389](../findings/data_models-102.md#FND-10389), [FND-10390](../findings/data_models-102.md#FND-10390), [FND-10391](../findings/data_models-102.md#FND-10391), [FND-10392](../findings/data_models-102.md#FND-10392), [FND-10393](../findings/data_models-102.md#FND-10393), [FND-10394](../findings/data_models-102.md#FND-10394), [FND-10395](../findings/data_models-102.md#FND-10395), [FND-10396](../findings/data_models-102.md#FND-10396), [FND-10397](../findings/data_models-102.md#FND-10397), [FND-10398](../findings/data_models-102.md#FND-10398), [FND-10399](../findings/data_models-102.md#FND-10399), [FND-10400](../findings/data_models-102.md#FND-10400), [FND-10401](../findings/data_models-102.md#FND-10401), [FND-10402](../findings/data_models-102.md#FND-10402), [FND-10403](../findings/data_models-102.md#FND-10403), [FND-10404](../findings/data_models-102.md#FND-10404), [FND-10405](../findings/data_models-102.md#FND-10405), [FND-10406](../findings/data_models-102.md#FND-10406), [FND-10407](../findings/data_models-102.md#FND-10407), [FND-10408](../findings/data_models-102.md#FND-10408), [FND-10409](../findings/data_models-102.md#FND-10409), [FND-10410](../findings/data_models-102.md#FND-10410), [FND-10411](../findings/data_models-102.md#FND-10411), [FND-10412](../findings/data_models-102.md#FND-10412), [FND-10413](../findings/data_models-102.md#FND-10413), [FND-10414](../findings/data_models-102.md#FND-10414), [FND-10415](../findings/data_models-102.md#FND-10415), [FND-10416](../findings/data_models-102.md#FND-10416)

## SRC-0611 — `research/proto/chesscom/user_properties/v1/properties_fair_play.proto`

- Type: rendered_protobuf_schema; bytes: 720; SHA-256: `9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 18; types: {"verified observation": 18}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10417](../findings/data_models-102.md#FND-10417), [FND-10418](../findings/data_models-102.md#FND-10418), [FND-10419](../findings/data_models-102.md#FND-10419), [FND-10420](../findings/data_models-102.md#FND-10420), [FND-10421](../findings/data_models-102.md#FND-10421), [FND-10422](../findings/data_models-102.md#FND-10422), [FND-10423](../findings/data_models-102.md#FND-10423), [FND-10424](../findings/data_models-102.md#FND-10424), [FND-10425](../findings/data_models-102.md#FND-10425), [FND-10426](../findings/data_models-102.md#FND-10426), [FND-10427](../findings/data_models-102.md#FND-10427), [FND-10428](../findings/data_models-102.md#FND-10428), [FND-10429](../findings/data_models-102.md#FND-10429), [FND-10430](../findings/data_models-102.md#FND-10430), [FND-10431](../findings/data_models-102.md#FND-10431), [FND-10432](../findings/data_models-102.md#FND-10432), [FND-10433](../findings/data_models-102.md#FND-10433), [FND-10434](../findings/data_models-102.md#FND-10434)

## SRC-0612 — `research/proto/chesscom/user_properties/v1/properties_growth.proto`

- Type: rendered_protobuf_schema; bytes: 608; SHA-256: `e2c2fa3e2c8133dfc7827827d41504b9b0a5b52f3aff1fc96fe62d8d342d4e22`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 12; types: {"verified observation": 12}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/e2c2fa3e2c8133dfc7827827d41504b9b0a5b52f3aff1fc96fe62d8d342d4e22.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10435](../findings/data_models-102.md#FND-10435), [FND-10436](../findings/data_models-102.md#FND-10436), [FND-10437](../findings/data_models-102.md#FND-10437), [FND-10438](../findings/data_models-102.md#FND-10438), [FND-10439](../findings/data_models-102.md#FND-10439), [FND-10440](../findings/data_models-102.md#FND-10440), [FND-10441](../findings/data_models-102.md#FND-10441), [FND-10442](../findings/data_models-102.md#FND-10442), [FND-10443](../findings/data_models-102.md#FND-10443), [FND-10444](../findings/data_models-102.md#FND-10444), [FND-10445](../findings/data_models-102.md#FND-10445), [FND-10446](../findings/data_models-102.md#FND-10446)

## SRC-0613 — `research/proto/chesscom/user_properties/v1/properties_ipqs.proto`

- Type: rendered_protobuf_schema; bytes: 1317; SHA-256: `e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 39; types: {"verified observation": 39}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10447](../findings/data_models-102.md#FND-10447), [FND-10448](../findings/data_models-102.md#FND-10448), [FND-10449](../findings/data_models-102.md#FND-10449), [FND-10450](../findings/data_models-102.md#FND-10450), [FND-10451](../findings/data_models-102.md#FND-10451), [FND-10452](../findings/data_models-102.md#FND-10452), [FND-10453](../findings/data_models-102.md#FND-10453), [FND-10454](../findings/data_models-102.md#FND-10454), [FND-10455](../findings/data_models-102.md#FND-10455), [FND-10456](../findings/data_models-102.md#FND-10456), [FND-10457](../findings/data_models-102.md#FND-10457), [FND-10458](../findings/data_models-102.md#FND-10458), [FND-10459](../findings/data_models-102.md#FND-10459), [FND-10460](../findings/data_models-102.md#FND-10460), [FND-10461](../findings/data_models-102.md#FND-10461), [FND-10462](../findings/data_models-102.md#FND-10462), [FND-10463](../findings/data_models-102.md#FND-10463), [FND-10464](../findings/data_models-102.md#FND-10464), [FND-10465](../findings/data_models-102.md#FND-10465), [FND-10466](../findings/data_models-102.md#FND-10466), [FND-10467](../findings/data_models-102.md#FND-10467), [FND-10468](../findings/data_models-102.md#FND-10468), [FND-10469](../findings/data_models-102.md#FND-10469), [FND-10470](../findings/data_models-102.md#FND-10470), [FND-10471](../findings/data_models-102.md#FND-10471), [FND-10472](../findings/data_models-102.md#FND-10472), [FND-10473](../findings/data_models-102.md#FND-10473), [FND-10474](../findings/data_models-102.md#FND-10474), [FND-10475](../findings/data_models-103.md#FND-10475), [FND-10476](../findings/data_models-103.md#FND-10476), [FND-10477](../findings/data_models-103.md#FND-10477), [FND-10478](../findings/data_models-103.md#FND-10478), [FND-10479](../findings/data_models-103.md#FND-10479), [FND-10480](../findings/data_models-103.md#FND-10480), [FND-10481](../findings/data_models-103.md#FND-10481), [FND-10482](../findings/data_models-103.md#FND-10482), [FND-10483](../findings/data_models-103.md#FND-10483), [FND-10484](../findings/data_models-103.md#FND-10484), [FND-10485](../findings/data_models-103.md#FND-10485)

## SRC-0614 — `research/proto/chesscom/user_properties/v1/properties_league.proto`

- Type: rendered_protobuf_schema; bytes: 716; SHA-256: `c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 18; types: {"verified observation": 18}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10486](../findings/data_models-103.md#FND-10486), [FND-10487](../findings/data_models-103.md#FND-10487), [FND-10488](../findings/data_models-103.md#FND-10488), [FND-10489](../findings/data_models-103.md#FND-10489), [FND-10490](../findings/data_models-103.md#FND-10490), [FND-10491](../findings/data_models-103.md#FND-10491), [FND-10492](../findings/data_models-103.md#FND-10492), [FND-10493](../findings/data_models-103.md#FND-10493), [FND-10494](../findings/data_models-103.md#FND-10494), [FND-10495](../findings/data_models-103.md#FND-10495), [FND-10496](../findings/data_models-103.md#FND-10496), [FND-10497](../findings/data_models-103.md#FND-10497), [FND-10498](../findings/data_models-103.md#FND-10498), [FND-10499](../findings/data_models-103.md#FND-10499), [FND-10500](../findings/data_models-103.md#FND-10500), [FND-10501](../findings/data_models-103.md#FND-10501), [FND-10502](../findings/data_models-103.md#FND-10502), [FND-10503](../findings/data_models-103.md#FND-10503)

## SRC-0615 — `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto`

- Type: rendered_protobuf_schema; bytes: 735; SHA-256: `7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 15; types: {"verified observation": 15}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10504](../findings/data_models-103.md#FND-10504), [FND-10505](../findings/data_models-103.md#FND-10505), [FND-10506](../findings/data_models-103.md#FND-10506), [FND-10507](../findings/data_models-103.md#FND-10507), [FND-10508](../findings/data_models-103.md#FND-10508), [FND-10509](../findings/data_models-103.md#FND-10509), [FND-10510](../findings/data_models-103.md#FND-10510), [FND-10511](../findings/data_models-103.md#FND-10511), [FND-10512](../findings/data_models-103.md#FND-10512), [FND-10513](../findings/data_models-103.md#FND-10513), [FND-10514](../findings/data_models-103.md#FND-10514), [FND-10515](../findings/data_models-103.md#FND-10515), [FND-10516](../findings/data_models-103.md#FND-10516), [FND-10517](../findings/data_models-103.md#FND-10517), [FND-10518](../findings/data_models-103.md#FND-10518)

## SRC-0616 — `research/proto/chesscom/user_properties/v1/properties_navbar.proto`

- Type: rendered_protobuf_schema; bytes: 372; SHA-256: `9d1b69156e82a8f9b951c07ffd0aec097563e79fd4370e12289245069a9465ae`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 7; types: {"verified observation": 7}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/9d1b69156e82a8f9b951c07ffd0aec097563e79fd4370e12289245069a9465ae.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10519](../findings/data_models-103.md#FND-10519), [FND-10520](../findings/data_models-103.md#FND-10520), [FND-10521](../findings/data_models-103.md#FND-10521), [FND-10522](../findings/data_models-103.md#FND-10522), [FND-10523](../findings/data_models-103.md#FND-10523), [FND-10524](../findings/data_models-103.md#FND-10524), [FND-10525](../findings/data_models-103.md#FND-10525)

## SRC-0617 — `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto`

- Type: rendered_protobuf_schema; bytes: 1842; SHA-256: `dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 33; types: {"verified observation": 33}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10526](../findings/data_models-103.md#FND-10526), [FND-10527](../findings/data_models-103.md#FND-10527), [FND-10528](../findings/data_models-103.md#FND-10528), [FND-10529](../findings/data_models-103.md#FND-10529), [FND-10530](../findings/data_models-103.md#FND-10530), [FND-10531](../findings/data_models-103.md#FND-10531), [FND-10532](../findings/data_models-103.md#FND-10532), [FND-10533](../findings/data_models-103.md#FND-10533), [FND-10534](../findings/data_models-103.md#FND-10534), [FND-10535](../findings/data_models-103.md#FND-10535), [FND-10536](../findings/data_models-103.md#FND-10536), [FND-10537](../findings/data_models-103.md#FND-10537), [FND-10538](../findings/data_models-103.md#FND-10538), [FND-10539](../findings/data_models-103.md#FND-10539), [FND-10540](../findings/data_models-103.md#FND-10540), [FND-10541](../findings/data_models-103.md#FND-10541), [FND-10542](../findings/data_models-103.md#FND-10542), [FND-10543](../findings/data_models-103.md#FND-10543), [FND-10544](../findings/data_models-103.md#FND-10544), [FND-10545](../findings/data_models-103.md#FND-10545), [FND-10546](../findings/data_models-103.md#FND-10546), [FND-10547](../findings/data_models-103.md#FND-10547), [FND-10548](../findings/data_models-103.md#FND-10548), [FND-10549](../findings/data_models-103.md#FND-10549), [FND-10550](../findings/data_models-103.md#FND-10550), [FND-10551](../findings/data_models-103.md#FND-10551), [FND-10552](../findings/data_models-103.md#FND-10552), [FND-10553](../findings/data_models-103.md#FND-10553), [FND-10554](../findings/data_models-103.md#FND-10554), [FND-10555](../findings/data_models-103.md#FND-10555), [FND-10556](../findings/data_models-103.md#FND-10556), [FND-10557](../findings/data_models-103.md#FND-10557), [FND-10558](../findings/data_models-103.md#FND-10558)

## SRC-0618 — `research/proto/chesscom/user_properties/v1/properties_pii.proto`

- Type: rendered_protobuf_schema; bytes: 1700; SHA-256: `35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 60; types: {"verified observation": 60}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10559](../findings/data_models-103.md#FND-10559), [FND-10560](../findings/data_models-103.md#FND-10560), [FND-10561](../findings/data_models-103.md#FND-10561), [FND-10562](../findings/data_models-103.md#FND-10562), [FND-10563](../findings/data_models-103.md#FND-10563), [FND-10564](../findings/data_models-103.md#FND-10564), [FND-10565](../findings/data_models-103.md#FND-10565), [FND-10566](../findings/data_models-103.md#FND-10566), [FND-10567](../findings/data_models-103.md#FND-10567), [FND-10568](../findings/data_models-103.md#FND-10568), [FND-10569](../findings/data_models-103.md#FND-10569), [FND-10570](../findings/data_models-103.md#FND-10570), [FND-10571](../findings/data_models-103.md#FND-10571), [FND-10572](../findings/data_models-103.md#FND-10572), [FND-10573](../findings/data_models-103.md#FND-10573), [FND-10574](../findings/data_models-103.md#FND-10574), [FND-10575](../findings/data_models-104.md#FND-10575), [FND-10576](../findings/data_models-104.md#FND-10576), [FND-10577](../findings/data_models-104.md#FND-10577), [FND-10578](../findings/data_models-104.md#FND-10578), [FND-10579](../findings/data_models-104.md#FND-10579), [FND-10580](../findings/data_models-104.md#FND-10580), [FND-10581](../findings/data_models-104.md#FND-10581), [FND-10582](../findings/data_models-104.md#FND-10582), [FND-10583](../findings/data_models-104.md#FND-10583), [FND-10584](../findings/data_models-104.md#FND-10584), [FND-10585](../findings/data_models-104.md#FND-10585), [FND-10586](../findings/data_models-104.md#FND-10586), [FND-10587](../findings/data_models-104.md#FND-10587), [FND-10588](../findings/data_models-104.md#FND-10588), [FND-10589](../findings/data_models-104.md#FND-10589), [FND-10590](../findings/data_models-104.md#FND-10590), [FND-10591](../findings/data_models-104.md#FND-10591), [FND-10592](../findings/data_models-104.md#FND-10592), [FND-10593](../findings/data_models-104.md#FND-10593), [FND-10594](../findings/data_models-104.md#FND-10594), [FND-10595](../findings/data_models-104.md#FND-10595), [FND-10596](../findings/data_models-104.md#FND-10596), [FND-10597](../findings/data_models-104.md#FND-10597), [FND-10598](../findings/data_models-104.md#FND-10598), [FND-10599](../findings/data_models-104.md#FND-10599), [FND-10600](../findings/data_models-104.md#FND-10600), [FND-10601](../findings/data_models-104.md#FND-10601), [FND-10602](../findings/data_models-104.md#FND-10602), [FND-10603](../findings/data_models-104.md#FND-10603), [FND-10604](../findings/data_models-104.md#FND-10604), [FND-10605](../findings/data_models-104.md#FND-10605), [FND-10606](../findings/data_models-104.md#FND-10606), [FND-10607](../findings/data_models-104.md#FND-10607), [FND-10608](../findings/data_models-104.md#FND-10608), [FND-10609](../findings/data_models-104.md#FND-10609), [FND-10610](../findings/data_models-104.md#FND-10610), [FND-10611](../findings/data_models-104.md#FND-10611), [FND-10612](../findings/data_models-104.md#FND-10612), [FND-10613](../findings/data_models-104.md#FND-10613), [FND-10614](../findings/data_models-104.md#FND-10614), [FND-10615](../findings/data_models-104.md#FND-10615), [FND-10616](../findings/data_models-104.md#FND-10616), [FND-10617](../findings/data_models-104.md#FND-10617), [FND-10618](../findings/data_models-104.md#FND-10618)

## SRC-0619 — `research/proto/chesscom/user_properties/v1/properties_play_stats.proto`

- Type: rendered_protobuf_schema; bytes: 1898; SHA-256: `d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 39; types: {"verified observation": 39}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10619](../findings/data_models-104.md#FND-10619), [FND-10620](../findings/data_models-104.md#FND-10620), [FND-10621](../findings/data_models-104.md#FND-10621), [FND-10622](../findings/data_models-104.md#FND-10622), [FND-10623](../findings/data_models-104.md#FND-10623), [FND-10624](../findings/data_models-104.md#FND-10624), [FND-10625](../findings/data_models-104.md#FND-10625), [FND-10626](../findings/data_models-104.md#FND-10626), [FND-10627](../findings/data_models-104.md#FND-10627), [FND-10628](../findings/data_models-104.md#FND-10628), [FND-10629](../findings/data_models-104.md#FND-10629), [FND-10630](../findings/data_models-104.md#FND-10630), [FND-10631](../findings/data_models-104.md#FND-10631), [FND-10632](../findings/data_models-104.md#FND-10632), [FND-10633](../findings/data_models-104.md#FND-10633), [FND-10634](../findings/data_models-104.md#FND-10634), [FND-10635](../findings/data_models-104.md#FND-10635), [FND-10636](../findings/data_models-104.md#FND-10636), [FND-10637](../findings/data_models-104.md#FND-10637), [FND-10638](../findings/data_models-104.md#FND-10638), [FND-10639](../findings/data_models-104.md#FND-10639), [FND-10640](../findings/data_models-104.md#FND-10640), [FND-10641](../findings/data_models-104.md#FND-10641), [FND-10642](../findings/data_models-104.md#FND-10642), [FND-10643](../findings/data_models-104.md#FND-10643), [FND-10644](../findings/data_models-104.md#FND-10644), [FND-10645](../findings/data_models-104.md#FND-10645), [FND-10646](../findings/data_models-104.md#FND-10646), [FND-10647](../findings/data_models-104.md#FND-10647), [FND-10648](../findings/data_models-104.md#FND-10648), [FND-10649](../findings/data_models-104.md#FND-10649), [FND-10650](../findings/data_models-104.md#FND-10650), [FND-10651](../findings/data_models-104.md#FND-10651), [FND-10652](../findings/data_models-104.md#FND-10652), [FND-10653](../findings/data_models-104.md#FND-10653), [FND-10654](../findings/data_models-104.md#FND-10654), [FND-10655](../findings/data_models-104.md#FND-10655), [FND-10656](../findings/data_models-104.md#FND-10656), [FND-10657](../findings/data_models-104.md#FND-10657)

## SRC-0620 — `research/proto/chesscom/user_properties/v1/properties_predictive.proto`

- Type: rendered_protobuf_schema; bytes: 2522; SHA-256: `a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 57; types: {"verified observation": 57}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10658](../findings/data_models-104.md#FND-10658), [FND-10659](../findings/data_models-104.md#FND-10659), [FND-10660](../findings/data_models-104.md#FND-10660), [FND-10661](../findings/data_models-104.md#FND-10661), [FND-10662](../findings/data_models-104.md#FND-10662), [FND-10663](../findings/data_models-104.md#FND-10663), [FND-10664](../findings/data_models-104.md#FND-10664), [FND-10665](../findings/data_models-104.md#FND-10665), [FND-10666](../findings/data_models-104.md#FND-10666), [FND-10667](../findings/data_models-104.md#FND-10667), [FND-10668](../findings/data_models-104.md#FND-10668), [FND-10669](../findings/data_models-104.md#FND-10669), [FND-10670](../findings/data_models-104.md#FND-10670), [FND-10671](../findings/data_models-104.md#FND-10671), [FND-10672](../findings/data_models-104.md#FND-10672), [FND-10673](../findings/data_models-104.md#FND-10673), [FND-10674](../findings/data_models-104.md#FND-10674), [FND-10675](../findings/data_models-105.md#FND-10675), [FND-10676](../findings/data_models-105.md#FND-10676), [FND-10677](../findings/data_models-105.md#FND-10677), [FND-10678](../findings/data_models-105.md#FND-10678), [FND-10679](../findings/data_models-105.md#FND-10679), [FND-10680](../findings/data_models-105.md#FND-10680), [FND-10681](../findings/data_models-105.md#FND-10681), [FND-10682](../findings/data_models-105.md#FND-10682), [FND-10683](../findings/data_models-105.md#FND-10683), [FND-10684](../findings/data_models-105.md#FND-10684), [FND-10685](../findings/data_models-105.md#FND-10685), [FND-10686](../findings/data_models-105.md#FND-10686), [FND-10687](../findings/data_models-105.md#FND-10687), [FND-10688](../findings/data_models-105.md#FND-10688), [FND-10689](../findings/data_models-105.md#FND-10689), [FND-10690](../findings/data_models-105.md#FND-10690), [FND-10691](../findings/data_models-105.md#FND-10691), [FND-10692](../findings/data_models-105.md#FND-10692), [FND-10693](../findings/data_models-105.md#FND-10693), [FND-10694](../findings/data_models-105.md#FND-10694), [FND-10695](../findings/data_models-105.md#FND-10695), [FND-10696](../findings/data_models-105.md#FND-10696), [FND-10697](../findings/data_models-105.md#FND-10697), [FND-10698](../findings/data_models-105.md#FND-10698), [FND-10699](../findings/data_models-105.md#FND-10699), [FND-10700](../findings/data_models-105.md#FND-10700), [FND-10701](../findings/data_models-105.md#FND-10701), [FND-10702](../findings/data_models-105.md#FND-10702), [FND-10703](../findings/data_models-105.md#FND-10703), [FND-10704](../findings/data_models-105.md#FND-10704), [FND-10705](../findings/data_models-105.md#FND-10705), [FND-10706](../findings/data_models-105.md#FND-10706), [FND-10707](../findings/data_models-105.md#FND-10707), [FND-10708](../findings/data_models-105.md#FND-10708), [FND-10709](../findings/data_models-105.md#FND-10709), [FND-10710](../findings/data_models-105.md#FND-10710), [FND-10711](../findings/data_models-105.md#FND-10711), [FND-10712](../findings/data_models-105.md#FND-10712), [FND-10713](../findings/data_models-105.md#FND-10713), [FND-10714](../findings/data_models-105.md#FND-10714)

## SRC-0621 — `research/proto/chesscom/user_properties/v1/properties_product_activity_rankings.proto`

- Type: rendered_protobuf_schema; bytes: 3780; SHA-256: `26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 105; types: {"verified observation": 105}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/26df5ac072e6ab9879de81560b81d3b16e5f91115a261400bbe114a43b8ffd67.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10715](../findings/data_models-105.md#FND-10715), [FND-10716](../findings/data_models-105.md#FND-10716), [FND-10717](../findings/data_models-105.md#FND-10717), [FND-10718](../findings/data_models-105.md#FND-10718), [FND-10719](../findings/data_models-105.md#FND-10719), [FND-10720](../findings/data_models-105.md#FND-10720), [FND-10721](../findings/data_models-105.md#FND-10721), [FND-10722](../findings/data_models-105.md#FND-10722), [FND-10723](../findings/data_models-105.md#FND-10723), [FND-10724](../findings/data_models-105.md#FND-10724), [FND-10725](../findings/data_models-105.md#FND-10725), [FND-10726](../findings/data_models-105.md#FND-10726), [FND-10727](../findings/data_models-105.md#FND-10727), [FND-10728](../findings/data_models-105.md#FND-10728), [FND-10729](../findings/data_models-105.md#FND-10729), [FND-10730](../findings/data_models-105.md#FND-10730), [FND-10731](../findings/data_models-105.md#FND-10731), [FND-10732](../findings/data_models-105.md#FND-10732), [FND-10733](../findings/data_models-105.md#FND-10733), [FND-10734](../findings/data_models-105.md#FND-10734), [FND-10735](../findings/data_models-105.md#FND-10735), [FND-10736](../findings/data_models-105.md#FND-10736), [FND-10737](../findings/data_models-105.md#FND-10737), [FND-10738](../findings/data_models-105.md#FND-10738), [FND-10739](../findings/data_models-105.md#FND-10739), [FND-10740](../findings/data_models-105.md#FND-10740), [FND-10741](../findings/data_models-105.md#FND-10741), [FND-10742](../findings/data_models-105.md#FND-10742), [FND-10743](../findings/data_models-105.md#FND-10743), [FND-10744](../findings/data_models-105.md#FND-10744), [FND-10745](../findings/data_models-105.md#FND-10745), [FND-10746](../findings/data_models-105.md#FND-10746), [FND-10747](../findings/data_models-105.md#FND-10747), [FND-10748](../findings/data_models-105.md#FND-10748), [FND-10749](../findings/data_models-105.md#FND-10749), [FND-10750](../findings/data_models-105.md#FND-10750), [FND-10751](../findings/data_models-105.md#FND-10751), [FND-10752](../findings/data_models-105.md#FND-10752), [FND-10753](../findings/data_models-105.md#FND-10753), [FND-10754](../findings/data_models-105.md#FND-10754), [FND-10755](../findings/data_models-105.md#FND-10755), [FND-10756](../findings/data_models-105.md#FND-10756), [FND-10757](../findings/data_models-105.md#FND-10757), [FND-10758](../findings/data_models-105.md#FND-10758), [FND-10759](../findings/data_models-105.md#FND-10759), [FND-10760](../findings/data_models-105.md#FND-10760), [FND-10761](../findings/data_models-105.md#FND-10761), [FND-10762](../findings/data_models-105.md#FND-10762), [FND-10763](../findings/data_models-105.md#FND-10763), [FND-10764](../findings/data_models-105.md#FND-10764), [FND-10765](../findings/data_models-105.md#FND-10765), [FND-10766](../findings/data_models-105.md#FND-10766), [FND-10767](../findings/data_models-105.md#FND-10767), [FND-10768](../findings/data_models-105.md#FND-10768), [FND-10769](../findings/data_models-105.md#FND-10769), [FND-10770](../findings/data_models-105.md#FND-10770), [FND-10771](../findings/data_models-105.md#FND-10771), [FND-10772](../findings/data_models-105.md#FND-10772), [FND-10773](../findings/data_models-105.md#FND-10773), [FND-10774](../findings/data_models-105.md#FND-10774), [FND-10775](../findings/data_models-106.md#FND-10775), [FND-10776](../findings/data_models-106.md#FND-10776), [FND-10777](../findings/data_models-106.md#FND-10777), [FND-10778](../findings/data_models-106.md#FND-10778), [FND-10779](../findings/data_models-106.md#FND-10779), [FND-10780](../findings/data_models-106.md#FND-10780), [FND-10781](../findings/data_models-106.md#FND-10781), [FND-10782](../findings/data_models-106.md#FND-10782), [FND-10783](../findings/data_models-106.md#FND-10783), [FND-10784](../findings/data_models-106.md#FND-10784), [FND-10785](../findings/data_models-106.md#FND-10785), [FND-10786](../findings/data_models-106.md#FND-10786), [FND-10787](../findings/data_models-106.md#FND-10787), [FND-10788](../findings/data_models-106.md#FND-10788), [FND-10789](../findings/data_models-106.md#FND-10789), [FND-10790](../findings/data_models-106.md#FND-10790), [FND-10791](../findings/data_models-106.md#FND-10791), [FND-10792](../findings/data_models-106.md#FND-10792), [FND-10793](../findings/data_models-106.md#FND-10793), [FND-10794](../findings/data_models-106.md#FND-10794), [FND-10795](../findings/data_models-106.md#FND-10795), [FND-10796](../findings/data_models-106.md#FND-10796), [FND-10797](../findings/data_models-106.md#FND-10797), [FND-10798](../findings/data_models-106.md#FND-10798), [FND-10799](../findings/data_models-106.md#FND-10799), [FND-10800](../findings/data_models-106.md#FND-10800), [FND-10801](../findings/data_models-106.md#FND-10801), [FND-10802](../findings/data_models-106.md#FND-10802), [FND-10803](../findings/data_models-106.md#FND-10803), [FND-10804](../findings/data_models-106.md#FND-10804), [FND-10805](../findings/data_models-106.md#FND-10805), [FND-10806](../findings/data_models-106.md#FND-10806), [FND-10807](../findings/data_models-106.md#FND-10807), [FND-10808](../findings/data_models-106.md#FND-10808), [FND-10809](../findings/data_models-106.md#FND-10809), [FND-10810](../findings/data_models-106.md#FND-10810), [FND-10811](../findings/data_models-106.md#FND-10811), [FND-10812](../findings/data_models-106.md#FND-10812), [FND-10813](../findings/data_models-106.md#FND-10813), [FND-10814](../findings/data_models-106.md#FND-10814), [FND-10815](../findings/data_models-106.md#FND-10815), [FND-10816](../findings/data_models-106.md#FND-10816), [FND-10817](../findings/data_models-106.md#FND-10817), [FND-10818](../findings/data_models-106.md#FND-10818), [FND-10819](../findings/data_models-106.md#FND-10819)

## SRC-0622 — `research/proto/chesscom/user_properties/v1/properties_puzzle_battle.proto`

- Type: rendered_protobuf_schema; bytes: 317; SHA-256: `24036b0dc4a95de4de0861146e9419cc8b72e40d594d5244a03fc86fe9b75ae9`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 6; types: {"verified observation": 6}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/24036b0dc4a95de4de0861146e9419cc8b72e40d594d5244a03fc86fe9b75ae9.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10820](../findings/data_models-106.md#FND-10820), [FND-10821](../findings/data_models-106.md#FND-10821), [FND-10822](../findings/data_models-106.md#FND-10822), [FND-10823](../findings/data_models-106.md#FND-10823), [FND-10824](../findings/data_models-106.md#FND-10824), [FND-10825](../findings/data_models-106.md#FND-10825)

## SRC-0623 — `research/proto/chesscom/user_properties/v1/properties_puzzle_rush.proto`

- Type: rendered_protobuf_schema; bytes: 625; SHA-256: `988f2dfe7fc245240ce0b1286da394d75940d731c2abadee9da919ad8b61cc28`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 12; types: {"verified observation": 12}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/988f2dfe7fc245240ce0b1286da394d75940d731c2abadee9da919ad8b61cc28.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10826](../findings/data_models-106.md#FND-10826), [FND-10827](../findings/data_models-106.md#FND-10827), [FND-10828](../findings/data_models-106.md#FND-10828), [FND-10829](../findings/data_models-106.md#FND-10829), [FND-10830](../findings/data_models-106.md#FND-10830), [FND-10831](../findings/data_models-106.md#FND-10831), [FND-10832](../findings/data_models-106.md#FND-10832), [FND-10833](../findings/data_models-106.md#FND-10833), [FND-10834](../findings/data_models-106.md#FND-10834), [FND-10835](../findings/data_models-106.md#FND-10835), [FND-10836](../findings/data_models-106.md#FND-10836), [FND-10837](../findings/data_models-106.md#FND-10837)

## SRC-0624 — `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto`

- Type: rendered_protobuf_schema; bytes: 3286; SHA-256: `c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 75; types: {"verified observation": 75}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10838](../findings/data_models-106.md#FND-10838), [FND-10839](../findings/data_models-106.md#FND-10839), [FND-10840](../findings/data_models-106.md#FND-10840), [FND-10841](../findings/data_models-106.md#FND-10841), [FND-10842](../findings/data_models-106.md#FND-10842), [FND-10843](../findings/data_models-106.md#FND-10843), [FND-10844](../findings/data_models-106.md#FND-10844), [FND-10845](../findings/data_models-106.md#FND-10845), [FND-10846](../findings/data_models-106.md#FND-10846), [FND-10847](../findings/data_models-106.md#FND-10847), [FND-10848](../findings/data_models-106.md#FND-10848), [FND-10849](../findings/data_models-106.md#FND-10849), [FND-10850](../findings/data_models-106.md#FND-10850), [FND-10851](../findings/data_models-106.md#FND-10851), [FND-10852](../findings/data_models-106.md#FND-10852), [FND-10853](../findings/data_models-106.md#FND-10853), [FND-10854](../findings/data_models-106.md#FND-10854), [FND-10855](../findings/data_models-106.md#FND-10855), [FND-10856](../findings/data_models-106.md#FND-10856), [FND-10857](../findings/data_models-106.md#FND-10857), [FND-10858](../findings/data_models-106.md#FND-10858), [FND-10859](../findings/data_models-106.md#FND-10859), [FND-10860](../findings/data_models-106.md#FND-10860), [FND-10861](../findings/data_models-106.md#FND-10861), [FND-10862](../findings/data_models-106.md#FND-10862), [FND-10863](../findings/data_models-106.md#FND-10863), [FND-10864](../findings/data_models-106.md#FND-10864), [FND-10865](../findings/data_models-106.md#FND-10865), [FND-10866](../findings/data_models-106.md#FND-10866), [FND-10867](../findings/data_models-106.md#FND-10867), [FND-10868](../findings/data_models-106.md#FND-10868), [FND-10869](../findings/data_models-106.md#FND-10869), [FND-10870](../findings/data_models-106.md#FND-10870), [FND-10871](../findings/data_models-106.md#FND-10871), [FND-10872](../findings/data_models-106.md#FND-10872), [FND-10873](../findings/data_models-106.md#FND-10873), [FND-10874](../findings/data_models-106.md#FND-10874), [FND-10875](../findings/data_models-107.md#FND-10875), [FND-10876](../findings/data_models-107.md#FND-10876), [FND-10877](../findings/data_models-107.md#FND-10877), [FND-10878](../findings/data_models-107.md#FND-10878), [FND-10879](../findings/data_models-107.md#FND-10879), [FND-10880](../findings/data_models-107.md#FND-10880), [FND-10881](../findings/data_models-107.md#FND-10881), [FND-10882](../findings/data_models-107.md#FND-10882), [FND-10883](../findings/data_models-107.md#FND-10883), [FND-10884](../findings/data_models-107.md#FND-10884), [FND-10885](../findings/data_models-107.md#FND-10885), [FND-10886](../findings/data_models-107.md#FND-10886), [FND-10887](../findings/data_models-107.md#FND-10887), [FND-10888](../findings/data_models-107.md#FND-10888), [FND-10889](../findings/data_models-107.md#FND-10889), [FND-10890](../findings/data_models-107.md#FND-10890), [FND-10891](../findings/data_models-107.md#FND-10891), [FND-10892](../findings/data_models-107.md#FND-10892), [FND-10893](../findings/data_models-107.md#FND-10893), [FND-10894](../findings/data_models-107.md#FND-10894), [FND-10895](../findings/data_models-107.md#FND-10895), [FND-10896](../findings/data_models-107.md#FND-10896), [FND-10897](../findings/data_models-107.md#FND-10897), [FND-10898](../findings/data_models-107.md#FND-10898), [FND-10899](../findings/data_models-107.md#FND-10899), [FND-10900](../findings/data_models-107.md#FND-10900), [FND-10901](../findings/data_models-107.md#FND-10901), [FND-10902](../findings/data_models-107.md#FND-10902), [FND-10903](../findings/data_models-107.md#FND-10903), [FND-10904](../findings/data_models-107.md#FND-10904), [FND-10905](../findings/data_models-107.md#FND-10905), [FND-10906](../findings/data_models-107.md#FND-10906), [FND-10907](../findings/data_models-107.md#FND-10907), [FND-10908](../findings/data_models-107.md#FND-10908), [FND-10909](../findings/data_models-107.md#FND-10909), [FND-10910](../findings/data_models-107.md#FND-10910), [FND-10911](../findings/data_models-107.md#FND-10911), [FND-10912](../findings/data_models-107.md#FND-10912)

## SRC-0625 — `research/proto/chesscom/user_properties/v1/properties_ratings.proto`

- Type: rendered_protobuf_schema; bytes: 2102; SHA-256: `670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 63; types: {"verified observation": 63}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10913](../findings/data_models-107.md#FND-10913), [FND-10914](../findings/data_models-107.md#FND-10914), [FND-10915](../findings/data_models-107.md#FND-10915), [FND-10916](../findings/data_models-107.md#FND-10916), [FND-10917](../findings/data_models-107.md#FND-10917), [FND-10918](../findings/data_models-107.md#FND-10918), [FND-10919](../findings/data_models-107.md#FND-10919), [FND-10920](../findings/data_models-107.md#FND-10920), [FND-10921](../findings/data_models-107.md#FND-10921), [FND-10922](../findings/data_models-107.md#FND-10922), [FND-10923](../findings/data_models-107.md#FND-10923), [FND-10924](../findings/data_models-107.md#FND-10924), [FND-10925](../findings/data_models-107.md#FND-10925), [FND-10926](../findings/data_models-107.md#FND-10926), [FND-10927](../findings/data_models-107.md#FND-10927), [FND-10928](../findings/data_models-107.md#FND-10928), [FND-10929](../findings/data_models-107.md#FND-10929), [FND-10930](../findings/data_models-107.md#FND-10930), [FND-10931](../findings/data_models-107.md#FND-10931), [FND-10932](../findings/data_models-107.md#FND-10932), [FND-10933](../findings/data_models-107.md#FND-10933), [FND-10934](../findings/data_models-107.md#FND-10934), [FND-10935](../findings/data_models-107.md#FND-10935), [FND-10936](../findings/data_models-107.md#FND-10936), [FND-10937](../findings/data_models-107.md#FND-10937), [FND-10938](../findings/data_models-107.md#FND-10938), [FND-10939](../findings/data_models-107.md#FND-10939), [FND-10940](../findings/data_models-107.md#FND-10940), [FND-10941](../findings/data_models-107.md#FND-10941), [FND-10942](../findings/data_models-107.md#FND-10942), [FND-10943](../findings/data_models-107.md#FND-10943), [FND-10944](../findings/data_models-107.md#FND-10944), [FND-10945](../findings/data_models-107.md#FND-10945), [FND-10946](../findings/data_models-107.md#FND-10946), [FND-10947](../findings/data_models-107.md#FND-10947), [FND-10948](../findings/data_models-107.md#FND-10948), [FND-10949](../findings/data_models-107.md#FND-10949), [FND-10950](../findings/data_models-107.md#FND-10950), [FND-10951](../findings/data_models-107.md#FND-10951), [FND-10952](../findings/data_models-107.md#FND-10952), [FND-10953](../findings/data_models-107.md#FND-10953), [FND-10954](../findings/data_models-107.md#FND-10954), [FND-10955](../findings/data_models-107.md#FND-10955), [FND-10956](../findings/data_models-107.md#FND-10956), [FND-10957](../findings/data_models-107.md#FND-10957), [FND-10958](../findings/data_models-107.md#FND-10958), [FND-10959](../findings/data_models-107.md#FND-10959), [FND-10960](../findings/data_models-107.md#FND-10960), [FND-10961](../findings/data_models-107.md#FND-10961), [FND-10962](../findings/data_models-107.md#FND-10962), [FND-10963](../findings/data_models-107.md#FND-10963), [FND-10964](../findings/data_models-107.md#FND-10964), [FND-10965](../findings/data_models-107.md#FND-10965), [FND-10966](../findings/data_models-107.md#FND-10966), [FND-10967](../findings/data_models-107.md#FND-10967), [FND-10968](../findings/data_models-107.md#FND-10968), [FND-10969](../findings/data_models-107.md#FND-10969), [FND-10970](../findings/data_models-107.md#FND-10970), [FND-10971](../findings/data_models-107.md#FND-10971), [FND-10972](../findings/data_models-107.md#FND-10972), [FND-10973](../findings/data_models-107.md#FND-10973), [FND-10974](../findings/data_models-107.md#FND-10974), [FND-10975](../findings/data_models-108.md#FND-10975)

## SRC-0626 — `research/proto/chesscom/user_properties/v1/properties_roles.proto`

- Type: rendered_protobuf_schema; bytes: 499; SHA-256: `72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 14; types: {"verified observation": 14}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10976](../findings/data_models-108.md#FND-10976), [FND-10977](../findings/data_models-108.md#FND-10977), [FND-10978](../findings/data_models-108.md#FND-10978), [FND-10979](../findings/data_models-108.md#FND-10979), [FND-10980](../findings/data_models-108.md#FND-10980), [FND-10981](../findings/data_models-108.md#FND-10981), [FND-10982](../findings/data_models-108.md#FND-10982), [FND-10983](../findings/data_models-108.md#FND-10983), [FND-10984](../findings/data_models-108.md#FND-10984), [FND-10985](../findings/data_models-108.md#FND-10985), [FND-10986](../findings/data_models-108.md#FND-10986), [FND-10987](../findings/data_models-108.md#FND-10987), [FND-10988](../findings/data_models-108.md#FND-10988), [FND-10989](../findings/data_models-108.md#FND-10989)

## SRC-0627 — `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto`

- Type: rendered_protobuf_schema; bytes: 2294; SHA-256: `21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 72; types: {"verified observation": 72}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-10990](../findings/data_models-108.md#FND-10990), [FND-10991](../findings/data_models-108.md#FND-10991), [FND-10992](../findings/data_models-108.md#FND-10992), [FND-10993](../findings/data_models-108.md#FND-10993), [FND-10994](../findings/data_models-108.md#FND-10994), [FND-10995](../findings/data_models-108.md#FND-10995), [FND-10996](../findings/data_models-108.md#FND-10996), [FND-10997](../findings/data_models-108.md#FND-10997), [FND-10998](../findings/data_models-108.md#FND-10998), [FND-10999](../findings/data_models-108.md#FND-10999), [FND-11000](../findings/data_models-108.md#FND-11000), [FND-11001](../findings/data_models-108.md#FND-11001), [FND-11002](../findings/data_models-108.md#FND-11002), [FND-11003](../findings/data_models-108.md#FND-11003), [FND-11004](../findings/data_models-108.md#FND-11004), [FND-11005](../findings/data_models-108.md#FND-11005), [FND-11006](../findings/data_models-108.md#FND-11006), [FND-11007](../findings/data_models-108.md#FND-11007), [FND-11008](../findings/data_models-108.md#FND-11008), [FND-11009](../findings/data_models-108.md#FND-11009), [FND-11010](../findings/data_models-108.md#FND-11010), [FND-11011](../findings/data_models-108.md#FND-11011), [FND-11012](../findings/data_models-108.md#FND-11012), [FND-11013](../findings/data_models-108.md#FND-11013), [FND-11014](../findings/data_models-108.md#FND-11014), [FND-11015](../findings/data_models-108.md#FND-11015), [FND-11016](../findings/data_models-108.md#FND-11016), [FND-11017](../findings/data_models-108.md#FND-11017), [FND-11018](../findings/data_models-108.md#FND-11018), [FND-11019](../findings/data_models-108.md#FND-11019), [FND-11020](../findings/data_models-108.md#FND-11020), [FND-11021](../findings/data_models-108.md#FND-11021), [FND-11022](../findings/data_models-108.md#FND-11022), [FND-11023](../findings/data_models-108.md#FND-11023), [FND-11024](../findings/data_models-108.md#FND-11024), [FND-11025](../findings/data_models-108.md#FND-11025), [FND-11026](../findings/data_models-108.md#FND-11026), [FND-11027](../findings/data_models-108.md#FND-11027), [FND-11028](../findings/data_models-108.md#FND-11028), [FND-11029](../findings/data_models-108.md#FND-11029), [FND-11030](../findings/data_models-108.md#FND-11030), [FND-11031](../findings/data_models-108.md#FND-11031), [FND-11032](../findings/data_models-108.md#FND-11032), [FND-11033](../findings/data_models-108.md#FND-11033), [FND-11034](../findings/data_models-108.md#FND-11034), [FND-11035](../findings/data_models-108.md#FND-11035), [FND-11036](../findings/data_models-108.md#FND-11036), [FND-11037](../findings/data_models-108.md#FND-11037), [FND-11038](../findings/data_models-108.md#FND-11038), [FND-11039](../findings/data_models-108.md#FND-11039), [FND-11040](../findings/data_models-108.md#FND-11040), [FND-11041](../findings/data_models-108.md#FND-11041), [FND-11042](../findings/data_models-108.md#FND-11042), [FND-11043](../findings/data_models-108.md#FND-11043), [FND-11044](../findings/data_models-108.md#FND-11044), [FND-11045](../findings/data_models-108.md#FND-11045), [FND-11046](../findings/data_models-108.md#FND-11046), [FND-11047](../findings/data_models-108.md#FND-11047), [FND-11048](../findings/data_models-108.md#FND-11048), [FND-11049](../findings/data_models-108.md#FND-11049), [FND-11050](../findings/data_models-108.md#FND-11050), [FND-11051](../findings/data_models-108.md#FND-11051), [FND-11052](../findings/data_models-108.md#FND-11052), [FND-11053](../findings/data_models-108.md#FND-11053), [FND-11054](../findings/data_models-108.md#FND-11054), [FND-11055](../findings/data_models-108.md#FND-11055), [FND-11056](../findings/data_models-108.md#FND-11056), [FND-11057](../findings/data_models-108.md#FND-11057), [FND-11058](../findings/data_models-108.md#FND-11058), [FND-11059](../findings/data_models-108.md#FND-11059), [FND-11060](../findings/data_models-108.md#FND-11060), [FND-11061](../findings/data_models-108.md#FND-11061)

## SRC-0628 — `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto`

- Type: rendered_protobuf_schema; bytes: 2477; SHA-256: `072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 75; types: {"verified observation": 75}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11062](../findings/data_models-108.md#FND-11062), [FND-11063](../findings/data_models-108.md#FND-11063), [FND-11064](../findings/data_models-108.md#FND-11064), [FND-11065](../findings/data_models-108.md#FND-11065), [FND-11066](../findings/data_models-108.md#FND-11066), [FND-11067](../findings/data_models-108.md#FND-11067), [FND-11068](../findings/data_models-108.md#FND-11068), [FND-11069](../findings/data_models-108.md#FND-11069), [FND-11070](../findings/data_models-108.md#FND-11070), [FND-11071](../findings/data_models-108.md#FND-11071), [FND-11072](../findings/data_models-108.md#FND-11072), [FND-11073](../findings/data_models-108.md#FND-11073), [FND-11074](../findings/data_models-108.md#FND-11074), [FND-11075](../findings/data_models-109.md#FND-11075), [FND-11076](../findings/data_models-109.md#FND-11076), [FND-11077](../findings/data_models-109.md#FND-11077), [FND-11078](../findings/data_models-109.md#FND-11078), [FND-11079](../findings/data_models-109.md#FND-11079), [FND-11080](../findings/data_models-109.md#FND-11080), [FND-11081](../findings/data_models-109.md#FND-11081), [FND-11082](../findings/data_models-109.md#FND-11082), [FND-11083](../findings/data_models-109.md#FND-11083), [FND-11084](../findings/data_models-109.md#FND-11084), [FND-11085](../findings/data_models-109.md#FND-11085), [FND-11086](../findings/data_models-109.md#FND-11086), [FND-11087](../findings/data_models-109.md#FND-11087), [FND-11088](../findings/data_models-109.md#FND-11088), [FND-11089](../findings/data_models-109.md#FND-11089), [FND-11090](../findings/data_models-109.md#FND-11090), [FND-11091](../findings/data_models-109.md#FND-11091), [FND-11092](../findings/data_models-109.md#FND-11092), [FND-11093](../findings/data_models-109.md#FND-11093), [FND-11094](../findings/data_models-109.md#FND-11094), [FND-11095](../findings/data_models-109.md#FND-11095), [FND-11096](../findings/data_models-109.md#FND-11096), [FND-11097](../findings/data_models-109.md#FND-11097), [FND-11098](../findings/data_models-109.md#FND-11098), [FND-11099](../findings/data_models-109.md#FND-11099), [FND-11100](../findings/data_models-109.md#FND-11100), [FND-11101](../findings/data_models-109.md#FND-11101), [FND-11102](../findings/data_models-109.md#FND-11102), [FND-11103](../findings/data_models-109.md#FND-11103), [FND-11104](../findings/data_models-109.md#FND-11104), [FND-11105](../findings/data_models-109.md#FND-11105), [FND-11106](../findings/data_models-109.md#FND-11106), [FND-11107](../findings/data_models-109.md#FND-11107), [FND-11108](../findings/data_models-109.md#FND-11108), [FND-11109](../findings/data_models-109.md#FND-11109), [FND-11110](../findings/data_models-109.md#FND-11110), [FND-11111](../findings/data_models-109.md#FND-11111), [FND-11112](../findings/data_models-109.md#FND-11112), [FND-11113](../findings/data_models-109.md#FND-11113), [FND-11114](../findings/data_models-109.md#FND-11114), [FND-11115](../findings/data_models-109.md#FND-11115), [FND-11116](../findings/data_models-109.md#FND-11116), [FND-11117](../findings/data_models-109.md#FND-11117), [FND-11118](../findings/data_models-109.md#FND-11118), [FND-11119](../findings/data_models-109.md#FND-11119), [FND-11120](../findings/data_models-109.md#FND-11120), [FND-11121](../findings/data_models-109.md#FND-11121), [FND-11122](../findings/data_models-109.md#FND-11122), [FND-11123](../findings/data_models-109.md#FND-11123), [FND-11124](../findings/data_models-109.md#FND-11124), [FND-11125](../findings/data_models-109.md#FND-11125), [FND-11126](../findings/data_models-109.md#FND-11126), [FND-11127](../findings/data_models-109.md#FND-11127), [FND-11128](../findings/data_models-109.md#FND-11128), [FND-11129](../findings/data_models-109.md#FND-11129), [FND-11130](../findings/data_models-109.md#FND-11130), [FND-11131](../findings/data_models-109.md#FND-11131), [FND-11132](../findings/data_models-109.md#FND-11132), [FND-11133](../findings/data_models-109.md#FND-11133), [FND-11134](../findings/data_models-109.md#FND-11134), [FND-11135](../findings/data_models-109.md#FND-11135), [FND-11136](../findings/data_models-109.md#FND-11136)

## SRC-0629 — `research/proto/chesscom/user_properties/v1/properties_skills.proto`

- Type: rendered_protobuf_schema; bytes: 406; SHA-256: `f52240cb37433d05089da30b8b3b69106c34fedb91580ba2e0cf3faf0119e3da`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 7; types: {"verified observation": 7}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/f52240cb37433d05089da30b8b3b69106c34fedb91580ba2e0cf3faf0119e3da.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11137](../findings/data_models-109.md#FND-11137), [FND-11138](../findings/data_models-109.md#FND-11138), [FND-11139](../findings/data_models-109.md#FND-11139), [FND-11140](../findings/data_models-109.md#FND-11140), [FND-11141](../findings/data_models-109.md#FND-11141), [FND-11142](../findings/data_models-109.md#FND-11142), [FND-11143](../findings/data_models-109.md#FND-11143)

## SRC-0630 — `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto`

- Type: rendered_protobuf_schema; bytes: 4851; SHA-256: `bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 132; types: {"verified observation": 132}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11144](../findings/data_models-109.md#FND-11144), [FND-11145](../findings/data_models-109.md#FND-11145), [FND-11146](../findings/data_models-109.md#FND-11146), [FND-11147](../findings/data_models-109.md#FND-11147), [FND-11148](../findings/data_models-109.md#FND-11148), [FND-11149](../findings/data_models-109.md#FND-11149), [FND-11150](../findings/data_models-109.md#FND-11150), [FND-11151](../findings/data_models-109.md#FND-11151), [FND-11152](../findings/data_models-109.md#FND-11152), [FND-11153](../findings/data_models-109.md#FND-11153), [FND-11154](../findings/data_models-109.md#FND-11154), [FND-11155](../findings/data_models-109.md#FND-11155), [FND-11156](../findings/data_models-109.md#FND-11156), [FND-11157](../findings/data_models-109.md#FND-11157), [FND-11158](../findings/data_models-109.md#FND-11158), [FND-11159](../findings/data_models-109.md#FND-11159), [FND-11160](../findings/data_models-109.md#FND-11160), [FND-11161](../findings/data_models-109.md#FND-11161), [FND-11162](../findings/data_models-109.md#FND-11162), [FND-11163](../findings/data_models-109.md#FND-11163), [FND-11164](../findings/data_models-109.md#FND-11164), [FND-11165](../findings/data_models-109.md#FND-11165), [FND-11166](../findings/data_models-109.md#FND-11166), [FND-11167](../findings/data_models-109.md#FND-11167), [FND-11168](../findings/data_models-109.md#FND-11168), [FND-11169](../findings/data_models-109.md#FND-11169), [FND-11170](../findings/data_models-109.md#FND-11170), [FND-11171](../findings/data_models-109.md#FND-11171), [FND-11172](../findings/data_models-109.md#FND-11172), [FND-11173](../findings/data_models-109.md#FND-11173), [FND-11174](../findings/data_models-109.md#FND-11174), [FND-11175](../findings/data_models-110.md#FND-11175), [FND-11176](../findings/data_models-110.md#FND-11176), [FND-11177](../findings/data_models-110.md#FND-11177), [FND-11178](../findings/data_models-110.md#FND-11178), [FND-11179](../findings/data_models-110.md#FND-11179), [FND-11180](../findings/data_models-110.md#FND-11180), [FND-11181](../findings/data_models-110.md#FND-11181), [FND-11182](../findings/data_models-110.md#FND-11182), [FND-11183](../findings/data_models-110.md#FND-11183), [FND-11184](../findings/data_models-110.md#FND-11184), [FND-11185](../findings/data_models-110.md#FND-11185), [FND-11186](../findings/data_models-110.md#FND-11186), [FND-11187](../findings/data_models-110.md#FND-11187), [FND-11188](../findings/data_models-110.md#FND-11188), [FND-11189](../findings/data_models-110.md#FND-11189), [FND-11190](../findings/data_models-110.md#FND-11190), [FND-11191](../findings/data_models-110.md#FND-11191), [FND-11192](../findings/data_models-110.md#FND-11192), [FND-11193](../findings/data_models-110.md#FND-11193), [FND-11194](../findings/data_models-110.md#FND-11194), [FND-11195](../findings/data_models-110.md#FND-11195), [FND-11196](../findings/data_models-110.md#FND-11196), [FND-11197](../findings/data_models-110.md#FND-11197), [FND-11198](../findings/data_models-110.md#FND-11198), [FND-11199](../findings/data_models-110.md#FND-11199), [FND-11200](../findings/data_models-110.md#FND-11200), [FND-11201](../findings/data_models-110.md#FND-11201), [FND-11202](../findings/data_models-110.md#FND-11202), [FND-11203](../findings/data_models-110.md#FND-11203), [FND-11204](../findings/data_models-110.md#FND-11204), [FND-11205](../findings/data_models-110.md#FND-11205), [FND-11206](../findings/data_models-110.md#FND-11206), [FND-11207](../findings/data_models-110.md#FND-11207), [FND-11208](../findings/data_models-110.md#FND-11208), [FND-11209](../findings/data_models-110.md#FND-11209), [FND-11210](../findings/data_models-110.md#FND-11210), [FND-11211](../findings/data_models-110.md#FND-11211), [FND-11212](../findings/data_models-110.md#FND-11212), [FND-11213](../findings/data_models-110.md#FND-11213), [FND-11214](../findings/data_models-110.md#FND-11214), [FND-11215](../findings/data_models-110.md#FND-11215), [FND-11216](../findings/data_models-110.md#FND-11216), [FND-11217](../findings/data_models-110.md#FND-11217), [FND-11218](../findings/data_models-110.md#FND-11218), [FND-11219](../findings/data_models-110.md#FND-11219), [FND-11220](../findings/data_models-110.md#FND-11220), [FND-11221](../findings/data_models-110.md#FND-11221), [FND-11222](../findings/data_models-110.md#FND-11222), [FND-11223](../findings/data_models-110.md#FND-11223), [FND-11224](../findings/data_models-110.md#FND-11224), [FND-11225](../findings/data_models-110.md#FND-11225), [FND-11226](../findings/data_models-110.md#FND-11226), [FND-11227](../findings/data_models-110.md#FND-11227), [FND-11228](../findings/data_models-110.md#FND-11228), [FND-11229](../findings/data_models-110.md#FND-11229), [FND-11230](../findings/data_models-110.md#FND-11230), [FND-11231](../findings/data_models-110.md#FND-11231), [FND-11232](../findings/data_models-110.md#FND-11232), [FND-11233](../findings/data_models-110.md#FND-11233), [FND-11234](../findings/data_models-110.md#FND-11234), [FND-11235](../findings/data_models-110.md#FND-11235), [FND-11236](../findings/data_models-110.md#FND-11236), [FND-11237](../findings/data_models-110.md#FND-11237), [FND-11238](../findings/data_models-110.md#FND-11238), [FND-11239](../findings/data_models-110.md#FND-11239), [FND-11240](../findings/data_models-110.md#FND-11240), [FND-11241](../findings/data_models-110.md#FND-11241), [FND-11242](../findings/data_models-110.md#FND-11242), [FND-11243](../findings/data_models-110.md#FND-11243), [FND-11244](../findings/data_models-110.md#FND-11244), [FND-11245](../findings/data_models-110.md#FND-11245), [FND-11246](../findings/data_models-110.md#FND-11246), [FND-11247](../findings/data_models-110.md#FND-11247), [FND-11248](../findings/data_models-110.md#FND-11248), [FND-11249](../findings/data_models-110.md#FND-11249), [FND-11250](../findings/data_models-110.md#FND-11250), [FND-11251](../findings/data_models-110.md#FND-11251), [FND-11252](../findings/data_models-110.md#FND-11252), [FND-11253](../findings/data_models-110.md#FND-11253), [FND-11254](../findings/data_models-110.md#FND-11254), [FND-11255](../findings/data_models-110.md#FND-11255), [FND-11256](../findings/data_models-110.md#FND-11256), [FND-11257](../findings/data_models-110.md#FND-11257), [FND-11258](../findings/data_models-110.md#FND-11258), [FND-11259](../findings/data_models-110.md#FND-11259), [FND-11260](../findings/data_models-110.md#FND-11260), [FND-11261](../findings/data_models-110.md#FND-11261), [FND-11262](../findings/data_models-110.md#FND-11262), [FND-11263](../findings/data_models-110.md#FND-11263), [FND-11264](../findings/data_models-110.md#FND-11264), [FND-11265](../findings/data_models-110.md#FND-11265), [FND-11266](../findings/data_models-110.md#FND-11266), [FND-11267](../findings/data_models-110.md#FND-11267), [FND-11268](../findings/data_models-110.md#FND-11268), [FND-11269](../findings/data_models-110.md#FND-11269), [FND-11270](../findings/data_models-110.md#FND-11270), [FND-11271](../findings/data_models-110.md#FND-11271), [FND-11272](../findings/data_models-110.md#FND-11272), [FND-11273](../findings/data_models-110.md#FND-11273), [FND-11274](../findings/data_models-110.md#FND-11274), [FND-11275](../findings/data_models-111.md#FND-11275)

## SRC-0631 — `research/proto/chesscom/user_properties/v1/properties_stats_daily_chess960.proto`

- Type: rendered_protobuf_schema; bytes: 2093; SHA-256: `cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 54; types: {"verified observation": 54}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/cbe88eee38f818a0f12c34c1522e790bee3a135a148a462181d7c82d8b9f2a80.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11276](../findings/data_models-111.md#FND-11276), [FND-11277](../findings/data_models-111.md#FND-11277), [FND-11278](../findings/data_models-111.md#FND-11278), [FND-11279](../findings/data_models-111.md#FND-11279), [FND-11280](../findings/data_models-111.md#FND-11280), [FND-11281](../findings/data_models-111.md#FND-11281), [FND-11282](../findings/data_models-111.md#FND-11282), [FND-11283](../findings/data_models-111.md#FND-11283), [FND-11284](../findings/data_models-111.md#FND-11284), [FND-11285](../findings/data_models-111.md#FND-11285), [FND-11286](../findings/data_models-111.md#FND-11286), [FND-11287](../findings/data_models-111.md#FND-11287), [FND-11288](../findings/data_models-111.md#FND-11288), [FND-11289](../findings/data_models-111.md#FND-11289), [FND-11290](../findings/data_models-111.md#FND-11290), [FND-11291](../findings/data_models-111.md#FND-11291), [FND-11292](../findings/data_models-111.md#FND-11292), [FND-11293](../findings/data_models-111.md#FND-11293), [FND-11294](../findings/data_models-111.md#FND-11294), [FND-11295](../findings/data_models-111.md#FND-11295), [FND-11296](../findings/data_models-111.md#FND-11296), [FND-11297](../findings/data_models-111.md#FND-11297), [FND-11298](../findings/data_models-111.md#FND-11298), [FND-11299](../findings/data_models-111.md#FND-11299), [FND-11300](../findings/data_models-111.md#FND-11300), [FND-11301](../findings/data_models-111.md#FND-11301), [FND-11302](../findings/data_models-111.md#FND-11302), [FND-11303](../findings/data_models-111.md#FND-11303), [FND-11304](../findings/data_models-111.md#FND-11304), [FND-11305](../findings/data_models-111.md#FND-11305), [FND-11306](../findings/data_models-111.md#FND-11306), [FND-11307](../findings/data_models-111.md#FND-11307), [FND-11308](../findings/data_models-111.md#FND-11308), [FND-11309](../findings/data_models-111.md#FND-11309), [FND-11310](../findings/data_models-111.md#FND-11310), [FND-11311](../findings/data_models-111.md#FND-11311), [FND-11312](../findings/data_models-111.md#FND-11312), [FND-11313](../findings/data_models-111.md#FND-11313), [FND-11314](../findings/data_models-111.md#FND-11314), [FND-11315](../findings/data_models-111.md#FND-11315), [FND-11316](../findings/data_models-111.md#FND-11316), [FND-11317](../findings/data_models-111.md#FND-11317), [FND-11318](../findings/data_models-111.md#FND-11318), [FND-11319](../findings/data_models-111.md#FND-11319), [FND-11320](../findings/data_models-111.md#FND-11320), [FND-11321](../findings/data_models-111.md#FND-11321), [FND-11322](../findings/data_models-111.md#FND-11322), [FND-11323](../findings/data_models-111.md#FND-11323), [FND-11324](../findings/data_models-111.md#FND-11324), [FND-11325](../findings/data_models-111.md#FND-11325), [FND-11326](../findings/data_models-111.md#FND-11326), [FND-11327](../findings/data_models-111.md#FND-11327), [FND-11328](../findings/data_models-111.md#FND-11328), [FND-11329](../findings/data_models-111.md#FND-11329)

## SRC-0632 — `research/proto/chesscom/user_properties/v1/properties_stats_live.proto`

- Type: rendered_protobuf_schema; bytes: 4775; SHA-256: `d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 129; types: {"verified observation": 129}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/d6a7e892bdfff83d5682c6fc9bb6036fe4cf9b3946dd5d05b49016e79ad52313.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11330](../findings/data_models-111.md#FND-11330), [FND-11331](../findings/data_models-111.md#FND-11331), [FND-11332](../findings/data_models-111.md#FND-11332), [FND-11333](../findings/data_models-111.md#FND-11333), [FND-11334](../findings/data_models-111.md#FND-11334), [FND-11335](../findings/data_models-111.md#FND-11335), [FND-11336](../findings/data_models-111.md#FND-11336), [FND-11337](../findings/data_models-111.md#FND-11337), [FND-11338](../findings/data_models-111.md#FND-11338), [FND-11339](../findings/data_models-111.md#FND-11339), [FND-11340](../findings/data_models-111.md#FND-11340), [FND-11341](../findings/data_models-111.md#FND-11341), [FND-11342](../findings/data_models-111.md#FND-11342), [FND-11343](../findings/data_models-111.md#FND-11343), [FND-11344](../findings/data_models-111.md#FND-11344), [FND-11345](../findings/data_models-111.md#FND-11345), [FND-11346](../findings/data_models-111.md#FND-11346), [FND-11347](../findings/data_models-111.md#FND-11347), [FND-11348](../findings/data_models-111.md#FND-11348), [FND-11349](../findings/data_models-111.md#FND-11349), [FND-11350](../findings/data_models-111.md#FND-11350), [FND-11351](../findings/data_models-111.md#FND-11351), [FND-11352](../findings/data_models-111.md#FND-11352), [FND-11353](../findings/data_models-111.md#FND-11353), [FND-11354](../findings/data_models-111.md#FND-11354), [FND-11355](../findings/data_models-111.md#FND-11355), [FND-11356](../findings/data_models-111.md#FND-11356), [FND-11357](../findings/data_models-111.md#FND-11357), [FND-11358](../findings/data_models-111.md#FND-11358), [FND-11359](../findings/data_models-111.md#FND-11359), [FND-11360](../findings/data_models-111.md#FND-11360), [FND-11361](../findings/data_models-111.md#FND-11361), [FND-11362](../findings/data_models-111.md#FND-11362), [FND-11363](../findings/data_models-111.md#FND-11363), [FND-11364](../findings/data_models-111.md#FND-11364), [FND-11365](../findings/data_models-111.md#FND-11365), [FND-11366](../findings/data_models-111.md#FND-11366), [FND-11367](../findings/data_models-111.md#FND-11367), [FND-11368](../findings/data_models-111.md#FND-11368), [FND-11369](../findings/data_models-111.md#FND-11369), [FND-11370](../findings/data_models-111.md#FND-11370), [FND-11371](../findings/data_models-111.md#FND-11371), [FND-11372](../findings/data_models-111.md#FND-11372), [FND-11373](../findings/data_models-111.md#FND-11373), [FND-11374](../findings/data_models-111.md#FND-11374), [FND-11375](../findings/data_models-112.md#FND-11375), [FND-11376](../findings/data_models-112.md#FND-11376), [FND-11377](../findings/data_models-112.md#FND-11377), [FND-11378](../findings/data_models-112.md#FND-11378), [FND-11379](../findings/data_models-112.md#FND-11379), [FND-11380](../findings/data_models-112.md#FND-11380), [FND-11381](../findings/data_models-112.md#FND-11381), [FND-11382](../findings/data_models-112.md#FND-11382), [FND-11383](../findings/data_models-112.md#FND-11383), [FND-11384](../findings/data_models-112.md#FND-11384), [FND-11385](../findings/data_models-112.md#FND-11385), [FND-11386](../findings/data_models-112.md#FND-11386), [FND-11387](../findings/data_models-112.md#FND-11387), [FND-11388](../findings/data_models-112.md#FND-11388), [FND-11389](../findings/data_models-112.md#FND-11389), [FND-11390](../findings/data_models-112.md#FND-11390), [FND-11391](../findings/data_models-112.md#FND-11391), [FND-11392](../findings/data_models-112.md#FND-11392), [FND-11393](../findings/data_models-112.md#FND-11393), [FND-11394](../findings/data_models-112.md#FND-11394), [FND-11395](../findings/data_models-112.md#FND-11395), [FND-11396](../findings/data_models-112.md#FND-11396), [FND-11397](../findings/data_models-112.md#FND-11397), [FND-11398](../findings/data_models-112.md#FND-11398), [FND-11399](../findings/data_models-112.md#FND-11399), [FND-11400](../findings/data_models-112.md#FND-11400), [FND-11401](../findings/data_models-112.md#FND-11401), [FND-11402](../findings/data_models-112.md#FND-11402), [FND-11403](../findings/data_models-112.md#FND-11403), [FND-11404](../findings/data_models-112.md#FND-11404), [FND-11405](../findings/data_models-112.md#FND-11405), [FND-11406](../findings/data_models-112.md#FND-11406), [FND-11407](../findings/data_models-112.md#FND-11407), [FND-11408](../findings/data_models-112.md#FND-11408), [FND-11409](../findings/data_models-112.md#FND-11409), [FND-11410](../findings/data_models-112.md#FND-11410), [FND-11411](../findings/data_models-112.md#FND-11411), [FND-11412](../findings/data_models-112.md#FND-11412), [FND-11413](../findings/data_models-112.md#FND-11413), [FND-11414](../findings/data_models-112.md#FND-11414), [FND-11415](../findings/data_models-112.md#FND-11415), [FND-11416](../findings/data_models-112.md#FND-11416), [FND-11417](../findings/data_models-112.md#FND-11417), [FND-11418](../findings/data_models-112.md#FND-11418), [FND-11419](../findings/data_models-112.md#FND-11419), [FND-11420](../findings/data_models-112.md#FND-11420), [FND-11421](../findings/data_models-112.md#FND-11421), [FND-11422](../findings/data_models-112.md#FND-11422), [FND-11423](../findings/data_models-112.md#FND-11423), [FND-11424](../findings/data_models-112.md#FND-11424), [FND-11425](../findings/data_models-112.md#FND-11425), [FND-11426](../findings/data_models-112.md#FND-11426), [FND-11427](../findings/data_models-112.md#FND-11427), [FND-11428](../findings/data_models-112.md#FND-11428), [FND-11429](../findings/data_models-112.md#FND-11429), [FND-11430](../findings/data_models-112.md#FND-11430), [FND-11431](../findings/data_models-112.md#FND-11431), [FND-11432](../findings/data_models-112.md#FND-11432), [FND-11433](../findings/data_models-112.md#FND-11433), [FND-11434](../findings/data_models-112.md#FND-11434), [FND-11435](../findings/data_models-112.md#FND-11435), [FND-11436](../findings/data_models-112.md#FND-11436), [FND-11437](../findings/data_models-112.md#FND-11437), [FND-11438](../findings/data_models-112.md#FND-11438), [FND-11439](../findings/data_models-112.md#FND-11439), [FND-11440](../findings/data_models-112.md#FND-11440), [FND-11441](../findings/data_models-112.md#FND-11441), [FND-11442](../findings/data_models-112.md#FND-11442), [FND-11443](../findings/data_models-112.md#FND-11443), [FND-11444](../findings/data_models-112.md#FND-11444), [FND-11445](../findings/data_models-112.md#FND-11445), [FND-11446](../findings/data_models-112.md#FND-11446), [FND-11447](../findings/data_models-112.md#FND-11447), [FND-11448](../findings/data_models-112.md#FND-11448), [FND-11449](../findings/data_models-112.md#FND-11449), [FND-11450](../findings/data_models-112.md#FND-11450), [FND-11451](../findings/data_models-112.md#FND-11451), [FND-11452](../findings/data_models-112.md#FND-11452), [FND-11453](../findings/data_models-112.md#FND-11453), [FND-11454](../findings/data_models-112.md#FND-11454), [FND-11455](../findings/data_models-112.md#FND-11455), [FND-11456](../findings/data_models-112.md#FND-11456), [FND-11457](../findings/data_models-112.md#FND-11457), [FND-11458](../findings/data_models-112.md#FND-11458)

## SRC-0633 — `research/proto/chesscom/user_properties/v1/properties_subscription.proto`

- Type: rendered_protobuf_schema; bytes: 5358; SHA-256: `f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 137; types: {"verified observation": 137}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/f28a784c5b570a470a224a17c2c107249e9738d1a664e5fd30ebeaccab2d3963.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11459](../findings/data_models-112.md#FND-11459), [FND-11460](../findings/data_models-112.md#FND-11460), [FND-11461](../findings/data_models-112.md#FND-11461), [FND-11462](../findings/data_models-112.md#FND-11462), [FND-11463](../findings/data_models-112.md#FND-11463), [FND-11464](../findings/data_models-112.md#FND-11464), [FND-11465](../findings/data_models-112.md#FND-11465), [FND-11466](../findings/data_models-112.md#FND-11466), [FND-11467](../findings/data_models-112.md#FND-11467), [FND-11468](../findings/data_models-112.md#FND-11468), [FND-11469](../findings/data_models-112.md#FND-11469), [FND-11470](../findings/data_models-112.md#FND-11470), [FND-11471](../findings/data_models-112.md#FND-11471), [FND-11472](../findings/data_models-112.md#FND-11472), [FND-11473](../findings/data_models-112.md#FND-11473), [FND-11474](../findings/data_models-112.md#FND-11474), [FND-11475](../findings/data_models-113.md#FND-11475), [FND-11476](../findings/data_models-113.md#FND-11476), [FND-11477](../findings/data_models-113.md#FND-11477), [FND-11478](../findings/data_models-113.md#FND-11478), [FND-11479](../findings/data_models-113.md#FND-11479), [FND-11480](../findings/data_models-113.md#FND-11480), [FND-11481](../findings/data_models-113.md#FND-11481), [FND-11482](../findings/data_models-113.md#FND-11482), [FND-11483](../findings/data_models-113.md#FND-11483), [FND-11484](../findings/data_models-113.md#FND-11484), [FND-11485](../findings/data_models-113.md#FND-11485), [FND-11486](../findings/data_models-113.md#FND-11486), [FND-11487](../findings/data_models-113.md#FND-11487), [FND-11488](../findings/data_models-113.md#FND-11488), [FND-11489](../findings/data_models-113.md#FND-11489), [FND-11490](../findings/data_models-113.md#FND-11490), [FND-11491](../findings/data_models-113.md#FND-11491), [FND-11492](../findings/data_models-113.md#FND-11492), [FND-11493](../findings/data_models-113.md#FND-11493), [FND-11494](../findings/data_models-113.md#FND-11494), [FND-11495](../findings/data_models-113.md#FND-11495), [FND-11496](../findings/data_models-113.md#FND-11496), [FND-11497](../findings/data_models-113.md#FND-11497), [FND-11498](../findings/data_models-113.md#FND-11498), [FND-11499](../findings/data_models-113.md#FND-11499), [FND-11500](../findings/data_models-113.md#FND-11500), [FND-11501](../findings/data_models-113.md#FND-11501), [FND-11502](../findings/data_models-113.md#FND-11502), [FND-11503](../findings/data_models-113.md#FND-11503), [FND-11504](../findings/data_models-113.md#FND-11504), [FND-11505](../findings/data_models-113.md#FND-11505), [FND-11506](../findings/data_models-113.md#FND-11506), [FND-11507](../findings/data_models-113.md#FND-11507), [FND-11508](../findings/data_models-113.md#FND-11508), [FND-11509](../findings/data_models-113.md#FND-11509), [FND-11510](../findings/data_models-113.md#FND-11510), [FND-11511](../findings/data_models-113.md#FND-11511), [FND-11512](../findings/data_models-113.md#FND-11512), [FND-11513](../findings/data_models-113.md#FND-11513), [FND-11514](../findings/data_models-113.md#FND-11514), [FND-11515](../findings/data_models-113.md#FND-11515), [FND-11516](../findings/data_models-113.md#FND-11516), [FND-11517](../findings/data_models-113.md#FND-11517), [FND-11518](../findings/data_models-113.md#FND-11518), [FND-11519](../findings/data_models-113.md#FND-11519), [FND-11520](../findings/data_models-113.md#FND-11520), [FND-11521](../findings/data_models-113.md#FND-11521), [FND-11522](../findings/data_models-113.md#FND-11522), [FND-11523](../findings/data_models-113.md#FND-11523), [FND-11524](../findings/data_models-113.md#FND-11524), [FND-11525](../findings/data_models-113.md#FND-11525), [FND-11526](../findings/data_models-113.md#FND-11526), [FND-11527](../findings/data_models-113.md#FND-11527), [FND-11528](../findings/data_models-113.md#FND-11528), [FND-11529](../findings/data_models-113.md#FND-11529), [FND-11530](../findings/data_models-113.md#FND-11530), [FND-11531](../findings/data_models-113.md#FND-11531), [FND-11532](../findings/data_models-113.md#FND-11532), [FND-11533](../findings/data_models-113.md#FND-11533), [FND-11534](../findings/data_models-113.md#FND-11534), [FND-11535](../findings/data_models-113.md#FND-11535), [FND-11536](../findings/data_models-113.md#FND-11536), [FND-11537](../findings/data_models-113.md#FND-11537), [FND-11538](../findings/data_models-113.md#FND-11538), [FND-11539](../findings/data_models-113.md#FND-11539), [FND-11540](../findings/data_models-113.md#FND-11540), [FND-11541](../findings/data_models-113.md#FND-11541), [FND-11542](../findings/data_models-113.md#FND-11542), [FND-11543](../findings/data_models-113.md#FND-11543), [FND-11544](../findings/data_models-113.md#FND-11544), [FND-11545](../findings/data_models-113.md#FND-11545), [FND-11546](../findings/data_models-113.md#FND-11546), [FND-11547](../findings/data_models-113.md#FND-11547), [FND-11548](../findings/data_models-113.md#FND-11548), [FND-11549](../findings/data_models-113.md#FND-11549), [FND-11550](../findings/data_models-113.md#FND-11550), [FND-11551](../findings/data_models-113.md#FND-11551), [FND-11552](../findings/data_models-113.md#FND-11552), [FND-11553](../findings/data_models-113.md#FND-11553), [FND-11554](../findings/data_models-113.md#FND-11554), [FND-11555](../findings/data_models-113.md#FND-11555), [FND-11556](../findings/data_models-113.md#FND-11556), [FND-11557](../findings/data_models-113.md#FND-11557), [FND-11558](../findings/data_models-113.md#FND-11558), [FND-11559](../findings/data_models-113.md#FND-11559), [FND-11560](../findings/data_models-113.md#FND-11560), [FND-11561](../findings/data_models-113.md#FND-11561), [FND-11562](../findings/data_models-113.md#FND-11562), [FND-11563](../findings/data_models-113.md#FND-11563), [FND-11564](../findings/data_models-113.md#FND-11564), [FND-11565](../findings/data_models-113.md#FND-11565), [FND-11566](../findings/data_models-113.md#FND-11566), [FND-11567](../findings/data_models-113.md#FND-11567), [FND-11568](../findings/data_models-113.md#FND-11568), [FND-11569](../findings/data_models-113.md#FND-11569), [FND-11570](../findings/data_models-113.md#FND-11570), [FND-11571](../findings/data_models-113.md#FND-11571), [FND-11572](../findings/data_models-113.md#FND-11572), [FND-11573](../findings/data_models-113.md#FND-11573), [FND-11574](../findings/data_models-113.md#FND-11574), [FND-11575](../findings/data_models-114.md#FND-11575), [FND-11576](../findings/data_models-114.md#FND-11576), [FND-11577](../findings/data_models-114.md#FND-11577), [FND-11578](../findings/data_models-114.md#FND-11578), [FND-11579](../findings/data_models-114.md#FND-11579), [FND-11580](../findings/data_models-114.md#FND-11580), [FND-11581](../findings/data_models-114.md#FND-11581), [FND-11582](../findings/data_models-114.md#FND-11582), [FND-11583](../findings/data_models-114.md#FND-11583), [FND-11584](../findings/data_models-114.md#FND-11584), [FND-11585](../findings/data_models-114.md#FND-11585), [FND-11586](../findings/data_models-114.md#FND-11586), [FND-11587](../findings/data_models-114.md#FND-11587), [FND-11588](../findings/data_models-114.md#FND-11588), [FND-11589](../findings/data_models-114.md#FND-11589), [FND-11590](../findings/data_models-114.md#FND-11590), [FND-11591](../findings/data_models-114.md#FND-11591), [FND-11592](../findings/data_models-114.md#FND-11592), [FND-11593](../findings/data_models-114.md#FND-11593), [FND-11594](../findings/data_models-114.md#FND-11594), [FND-11595](../findings/data_models-114.md#FND-11595)

## SRC-0634 — `research/proto/chesscom/user_properties/v1/properties_survey.proto`

- Type: rendered_protobuf_schema; bytes: 379; SHA-256: `6f259f6a10e63d839119b60fcb63c65804ab19bde02341501b26e352c8fed520`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 7; types: {"verified observation": 7}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/6f259f6a10e63d839119b60fcb63c65804ab19bde02341501b26e352c8fed520.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11596](../findings/data_models-114.md#FND-11596), [FND-11597](../findings/data_models-114.md#FND-11597), [FND-11598](../findings/data_models-114.md#FND-11598), [FND-11599](../findings/data_models-114.md#FND-11599), [FND-11600](../findings/data_models-114.md#FND-11600), [FND-11601](../findings/data_models-114.md#FND-11601), [FND-11602](../findings/data_models-114.md#FND-11602)

## SRC-0635 — `research/proto/chesscom/user_properties/v1/properties_themes.proto`

- Type: rendered_protobuf_schema; bytes: 1045; SHA-256: `c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 30; types: {"verified observation": 30}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/c733c04b90f8c52c0152e096371a6eab16190855522859de88a553260781845e.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11603](../findings/data_models-114.md#FND-11603), [FND-11604](../findings/data_models-114.md#FND-11604), [FND-11605](../findings/data_models-114.md#FND-11605), [FND-11606](../findings/data_models-114.md#FND-11606), [FND-11607](../findings/data_models-114.md#FND-11607), [FND-11608](../findings/data_models-114.md#FND-11608), [FND-11609](../findings/data_models-114.md#FND-11609), [FND-11610](../findings/data_models-114.md#FND-11610), [FND-11611](../findings/data_models-114.md#FND-11611), [FND-11612](../findings/data_models-114.md#FND-11612), [FND-11613](../findings/data_models-114.md#FND-11613), [FND-11614](../findings/data_models-114.md#FND-11614), [FND-11615](../findings/data_models-114.md#FND-11615), [FND-11616](../findings/data_models-114.md#FND-11616), [FND-11617](../findings/data_models-114.md#FND-11617), [FND-11618](../findings/data_models-114.md#FND-11618), [FND-11619](../findings/data_models-114.md#FND-11619), [FND-11620](../findings/data_models-114.md#FND-11620), [FND-11621](../findings/data_models-114.md#FND-11621), [FND-11622](../findings/data_models-114.md#FND-11622), [FND-11623](../findings/data_models-114.md#FND-11623), [FND-11624](../findings/data_models-114.md#FND-11624), [FND-11625](../findings/data_models-114.md#FND-11625), [FND-11626](../findings/data_models-114.md#FND-11626), [FND-11627](../findings/data_models-114.md#FND-11627), [FND-11628](../findings/data_models-114.md#FND-11628), [FND-11629](../findings/data_models-114.md#FND-11629), [FND-11630](../findings/data_models-114.md#FND-11630), [FND-11631](../findings/data_models-114.md#FND-11631), [FND-11632](../findings/data_models-114.md#FND-11632)

## SRC-0636 — `research/proto/chesscom/user_properties/v1/properties_time_windows.proto`

- Type: rendered_protobuf_schema; bytes: 632; SHA-256: `be1bbbf01764114244981c0f2a0766d8178588c3c06356c80248f8e54b0295a5`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 10; types: {"verified observation": 10}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/be1bbbf01764114244981c0f2a0766d8178588c3c06356c80248f8e54b0295a5.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11633](../findings/data_models-114.md#FND-11633), [FND-11634](../findings/data_models-114.md#FND-11634), [FND-11635](../findings/data_models-114.md#FND-11635), [FND-11636](../findings/data_models-114.md#FND-11636), [FND-11637](../findings/data_models-114.md#FND-11637), [FND-11638](../findings/data_models-114.md#FND-11638), [FND-11639](../findings/data_models-114.md#FND-11639), [FND-11640](../findings/data_models-114.md#FND-11640), [FND-11641](../findings/data_models-114.md#FND-11641), [FND-11642](../findings/data_models-114.md#FND-11642)

## SRC-0637 — `research/proto/chesscom/user_properties/v1/properties_tournament_stats.proto`

- Type: rendered_protobuf_schema; bytes: 623; SHA-256: `93e27332899cf92a6c6439629aafeb21d448fdbc1543b40aef294a4c7576a83b`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 12; types: {"verified observation": 12}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/93e27332899cf92a6c6439629aafeb21d448fdbc1543b40aef294a4c7576a83b.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11643](../findings/data_models-114.md#FND-11643), [FND-11644](../findings/data_models-114.md#FND-11644), [FND-11645](../findings/data_models-114.md#FND-11645), [FND-11646](../findings/data_models-114.md#FND-11646), [FND-11647](../findings/data_models-114.md#FND-11647), [FND-11648](../findings/data_models-114.md#FND-11648), [FND-11649](../findings/data_models-114.md#FND-11649), [FND-11650](../findings/data_models-114.md#FND-11650), [FND-11651](../findings/data_models-114.md#FND-11651), [FND-11652](../findings/data_models-114.md#FND-11652), [FND-11653](../findings/data_models-114.md#FND-11653), [FND-11654](../findings/data_models-114.md#FND-11654)

## SRC-0638 — `research/proto/chesscom/user_properties/v1/properties_trust_and_safety.proto`

- Type: rendered_protobuf_schema; bytes: 2033; SHA-256: `610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 45; types: {"verified observation": 45}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/610a7766dc80645e483b37418d5c58d1b06532dc45737d6ef27c45cee505630c.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11655](../findings/data_models-114.md#FND-11655), [FND-11656](../findings/data_models-114.md#FND-11656), [FND-11657](../findings/data_models-114.md#FND-11657), [FND-11658](../findings/data_models-114.md#FND-11658), [FND-11659](../findings/data_models-114.md#FND-11659), [FND-11660](../findings/data_models-114.md#FND-11660), [FND-11661](../findings/data_models-114.md#FND-11661), [FND-11662](../findings/data_models-114.md#FND-11662), [FND-11663](../findings/data_models-114.md#FND-11663), [FND-11664](../findings/data_models-114.md#FND-11664), [FND-11665](../findings/data_models-114.md#FND-11665), [FND-11666](../findings/data_models-114.md#FND-11666), [FND-11667](../findings/data_models-114.md#FND-11667), [FND-11668](../findings/data_models-114.md#FND-11668), [FND-11669](../findings/data_models-114.md#FND-11669), [FND-11670](../findings/data_models-114.md#FND-11670), [FND-11671](../findings/data_models-114.md#FND-11671), [FND-11672](../findings/data_models-114.md#FND-11672), [FND-11673](../findings/data_models-114.md#FND-11673), [FND-11674](../findings/data_models-114.md#FND-11674), [FND-11675](../findings/data_models-115.md#FND-11675), [FND-11676](../findings/data_models-115.md#FND-11676), [FND-11677](../findings/data_models-115.md#FND-11677), [FND-11678](../findings/data_models-115.md#FND-11678), [FND-11679](../findings/data_models-115.md#FND-11679), [FND-11680](../findings/data_models-115.md#FND-11680), [FND-11681](../findings/data_models-115.md#FND-11681), [FND-11682](../findings/data_models-115.md#FND-11682), [FND-11683](../findings/data_models-115.md#FND-11683), [FND-11684](../findings/data_models-115.md#FND-11684), [FND-11685](../findings/data_models-115.md#FND-11685), [FND-11686](../findings/data_models-115.md#FND-11686), [FND-11687](../findings/data_models-115.md#FND-11687), [FND-11688](../findings/data_models-115.md#FND-11688), [FND-11689](../findings/data_models-115.md#FND-11689), [FND-11690](../findings/data_models-115.md#FND-11690), [FND-11691](../findings/data_models-115.md#FND-11691), [FND-11692](../findings/data_models-115.md#FND-11692), [FND-11693](../findings/data_models-115.md#FND-11693), [FND-11694](../findings/data_models-115.md#FND-11694), [FND-11695](../findings/data_models-115.md#FND-11695), [FND-11696](../findings/data_models-115.md#FND-11696), [FND-11697](../findings/data_models-115.md#FND-11697), [FND-11698](../findings/data_models-115.md#FND-11698), [FND-11699](../findings/data_models-115.md#FND-11699)

## SRC-0639 — `research/proto/chesscom/user_properties/v1/properties_turnstile.proto`

- Type: rendered_protobuf_schema; bytes: 326; SHA-256: `ebbe6d87208d6a18aa139c6fc677a7703c8f9e51c1e688b6b753962f5adaeb78`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 6; types: {"verified observation": 6}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/ebbe6d87208d6a18aa139c6fc677a7703c8f9e51c1e688b6b753962f5adaeb78.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11700](../findings/data_models-115.md#FND-11700), [FND-11701](../findings/data_models-115.md#FND-11701), [FND-11702](../findings/data_models-115.md#FND-11702), [FND-11703](../findings/data_models-115.md#FND-11703), [FND-11704](../findings/data_models-115.md#FND-11704), [FND-11705](../findings/data_models-115.md#FND-11705)

## SRC-0640 — `research/proto/chesscom/user_properties/v1/properties_user_details.proto`

- Type: rendered_protobuf_schema; bytes: 4941; SHA-256: `6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 153; types: {"verified observation": 153}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11706](../findings/data_models-115.md#FND-11706), [FND-11707](../findings/data_models-115.md#FND-11707), [FND-11708](../findings/data_models-115.md#FND-11708), [FND-11709](../findings/data_models-115.md#FND-11709), [FND-11710](../findings/data_models-115.md#FND-11710), [FND-11711](../findings/data_models-115.md#FND-11711), [FND-11712](../findings/data_models-115.md#FND-11712), [FND-11713](../findings/data_models-115.md#FND-11713), [FND-11714](../findings/data_models-115.md#FND-11714), [FND-11715](../findings/data_models-115.md#FND-11715), [FND-11716](../findings/data_models-115.md#FND-11716), [FND-11717](../findings/data_models-115.md#FND-11717), [FND-11718](../findings/data_models-115.md#FND-11718), [FND-11719](../findings/data_models-115.md#FND-11719), [FND-11720](../findings/data_models-115.md#FND-11720), [FND-11721](../findings/data_models-115.md#FND-11721), [FND-11722](../findings/data_models-115.md#FND-11722), [FND-11723](../findings/data_models-115.md#FND-11723), [FND-11724](../findings/data_models-115.md#FND-11724), [FND-11725](../findings/data_models-115.md#FND-11725), [FND-11726](../findings/data_models-115.md#FND-11726), [FND-11727](../findings/data_models-115.md#FND-11727), [FND-11728](../findings/data_models-115.md#FND-11728), [FND-11729](../findings/data_models-115.md#FND-11729), [FND-11730](../findings/data_models-115.md#FND-11730), [FND-11731](../findings/data_models-115.md#FND-11731), [FND-11732](../findings/data_models-115.md#FND-11732), [FND-11733](../findings/data_models-115.md#FND-11733), [FND-11734](../findings/data_models-115.md#FND-11734), [FND-11735](../findings/data_models-115.md#FND-11735), [FND-11736](../findings/data_models-115.md#FND-11736), [FND-11737](../findings/data_models-115.md#FND-11737), [FND-11738](../findings/data_models-115.md#FND-11738), [FND-11739](../findings/data_models-115.md#FND-11739), [FND-11740](../findings/data_models-115.md#FND-11740), [FND-11741](../findings/data_models-115.md#FND-11741), [FND-11742](../findings/data_models-115.md#FND-11742), [FND-11743](../findings/data_models-115.md#FND-11743), [FND-11744](../findings/data_models-115.md#FND-11744), [FND-11745](../findings/data_models-115.md#FND-11745), [FND-11746](../findings/data_models-115.md#FND-11746), [FND-11747](../findings/data_models-115.md#FND-11747), [FND-11748](../findings/data_models-115.md#FND-11748), [FND-11749](../findings/data_models-115.md#FND-11749), [FND-11750](../findings/data_models-115.md#FND-11750), [FND-11751](../findings/data_models-115.md#FND-11751), [FND-11752](../findings/data_models-115.md#FND-11752), [FND-11753](../findings/data_models-115.md#FND-11753), [FND-11754](../findings/data_models-115.md#FND-11754), [FND-11755](../findings/data_models-115.md#FND-11755), [FND-11756](../findings/data_models-115.md#FND-11756), [FND-11757](../findings/data_models-115.md#FND-11757), [FND-11758](../findings/data_models-115.md#FND-11758), [FND-11759](../findings/data_models-115.md#FND-11759), [FND-11760](../findings/data_models-115.md#FND-11760), [FND-11761](../findings/data_models-115.md#FND-11761), [FND-11762](../findings/data_models-115.md#FND-11762), [FND-11763](../findings/data_models-115.md#FND-11763), [FND-11764](../findings/data_models-115.md#FND-11764), [FND-11765](../findings/data_models-115.md#FND-11765), [FND-11766](../findings/data_models-115.md#FND-11766), [FND-11767](../findings/data_models-115.md#FND-11767), [FND-11768](../findings/data_models-115.md#FND-11768), [FND-11769](../findings/data_models-115.md#FND-11769), [FND-11770](../findings/data_models-115.md#FND-11770), [FND-11771](../findings/data_models-115.md#FND-11771), [FND-11772](../findings/data_models-115.md#FND-11772), [FND-11773](../findings/data_models-115.md#FND-11773), [FND-11774](../findings/data_models-115.md#FND-11774), [FND-11775](../findings/data_models-116.md#FND-11775), [FND-11776](../findings/data_models-116.md#FND-11776), [FND-11777](../findings/data_models-116.md#FND-11777), [FND-11778](../findings/data_models-116.md#FND-11778), [FND-11779](../findings/data_models-116.md#FND-11779), [FND-11780](../findings/data_models-116.md#FND-11780), [FND-11781](../findings/data_models-116.md#FND-11781), [FND-11782](../findings/data_models-116.md#FND-11782), [FND-11783](../findings/data_models-116.md#FND-11783), [FND-11784](../findings/data_models-116.md#FND-11784), [FND-11785](../findings/data_models-116.md#FND-11785), [FND-11786](../findings/data_models-116.md#FND-11786), [FND-11787](../findings/data_models-116.md#FND-11787), [FND-11788](../findings/data_models-116.md#FND-11788), [FND-11789](../findings/data_models-116.md#FND-11789), [FND-11790](../findings/data_models-116.md#FND-11790), [FND-11791](../findings/data_models-116.md#FND-11791), [FND-11792](../findings/data_models-116.md#FND-11792), [FND-11793](../findings/data_models-116.md#FND-11793), [FND-11794](../findings/data_models-116.md#FND-11794), [FND-11795](../findings/data_models-116.md#FND-11795), [FND-11796](../findings/data_models-116.md#FND-11796), [FND-11797](../findings/data_models-116.md#FND-11797), [FND-11798](../findings/data_models-116.md#FND-11798), [FND-11799](../findings/data_models-116.md#FND-11799), [FND-11800](../findings/data_models-116.md#FND-11800), [FND-11801](../findings/data_models-116.md#FND-11801), [FND-11802](../findings/data_models-116.md#FND-11802), [FND-11803](../findings/data_models-116.md#FND-11803), [FND-11804](../findings/data_models-116.md#FND-11804), [FND-11805](../findings/data_models-116.md#FND-11805), [FND-11806](../findings/data_models-116.md#FND-11806), [FND-11807](../findings/data_models-116.md#FND-11807), [FND-11808](../findings/data_models-116.md#FND-11808), [FND-11809](../findings/data_models-116.md#FND-11809), [FND-11810](../findings/data_models-116.md#FND-11810), [FND-11811](../findings/data_models-116.md#FND-11811), [FND-11812](../findings/data_models-116.md#FND-11812), [FND-11813](../findings/data_models-116.md#FND-11813), [FND-11814](../findings/data_models-116.md#FND-11814), [FND-11815](../findings/data_models-116.md#FND-11815), [FND-11816](../findings/data_models-116.md#FND-11816), [FND-11817](../findings/data_models-116.md#FND-11817), [FND-11818](../findings/data_models-116.md#FND-11818), [FND-11819](../findings/data_models-116.md#FND-11819), [FND-11820](../findings/data_models-116.md#FND-11820), [FND-11821](../findings/data_models-116.md#FND-11821), [FND-11822](../findings/data_models-116.md#FND-11822), [FND-11823](../findings/data_models-116.md#FND-11823), [FND-11824](../findings/data_models-116.md#FND-11824), [FND-11825](../findings/data_models-116.md#FND-11825), [FND-11826](../findings/data_models-116.md#FND-11826), [FND-11827](../findings/data_models-116.md#FND-11827), [FND-11828](../findings/data_models-116.md#FND-11828), [FND-11829](../findings/data_models-116.md#FND-11829), [FND-11830](../findings/data_models-116.md#FND-11830), [FND-11831](../findings/data_models-116.md#FND-11831), [FND-11832](../findings/data_models-116.md#FND-11832), [FND-11833](../findings/data_models-116.md#FND-11833), [FND-11834](../findings/data_models-116.md#FND-11834), [FND-11835](../findings/data_models-116.md#FND-11835), [FND-11836](../findings/data_models-116.md#FND-11836), [FND-11837](../findings/data_models-116.md#FND-11837), [FND-11838](../findings/data_models-116.md#FND-11838), [FND-11839](../findings/data_models-116.md#FND-11839), [FND-11840](../findings/data_models-116.md#FND-11840), [FND-11841](../findings/data_models-116.md#FND-11841), [FND-11842](../findings/data_models-116.md#FND-11842), [FND-11843](../findings/data_models-116.md#FND-11843), [FND-11844](../findings/data_models-116.md#FND-11844), [FND-11845](../findings/data_models-116.md#FND-11845), [FND-11846](../findings/data_models-116.md#FND-11846), [FND-11847](../findings/data_models-116.md#FND-11847), [FND-11848](../findings/data_models-116.md#FND-11848), [FND-11849](../findings/data_models-116.md#FND-11849), [FND-11850](../findings/data_models-116.md#FND-11850), [FND-11851](../findings/data_models-116.md#FND-11851), [FND-11852](../findings/data_models-116.md#FND-11852), [FND-11853](../findings/data_models-116.md#FND-11853), [FND-11854](../findings/data_models-116.md#FND-11854), [FND-11855](../findings/data_models-116.md#FND-11855), [FND-11856](../findings/data_models-116.md#FND-11856), [FND-11857](../findings/data_models-116.md#FND-11857), [FND-11858](../findings/data_models-116.md#FND-11858)

## SRC-0641 — `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto`

- Type: rendered_protobuf_schema; bytes: 2182; SHA-256: `7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 42; types: {"verified observation": 42}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11859](../findings/data_models-116.md#FND-11859), [FND-11860](../findings/data_models-116.md#FND-11860), [FND-11861](../findings/data_models-116.md#FND-11861), [FND-11862](../findings/data_models-116.md#FND-11862), [FND-11863](../findings/data_models-116.md#FND-11863), [FND-11864](../findings/data_models-116.md#FND-11864), [FND-11865](../findings/data_models-116.md#FND-11865), [FND-11866](../findings/data_models-116.md#FND-11866), [FND-11867](../findings/data_models-116.md#FND-11867), [FND-11868](../findings/data_models-116.md#FND-11868), [FND-11869](../findings/data_models-116.md#FND-11869), [FND-11870](../findings/data_models-116.md#FND-11870), [FND-11871](../findings/data_models-116.md#FND-11871), [FND-11872](../findings/data_models-116.md#FND-11872), [FND-11873](../findings/data_models-116.md#FND-11873), [FND-11874](../findings/data_models-116.md#FND-11874), [FND-11875](../findings/data_models-117.md#FND-11875), [FND-11876](../findings/data_models-117.md#FND-11876), [FND-11877](../findings/data_models-117.md#FND-11877), [FND-11878](../findings/data_models-117.md#FND-11878), [FND-11879](../findings/data_models-117.md#FND-11879), [FND-11880](../findings/data_models-117.md#FND-11880), [FND-11881](../findings/data_models-117.md#FND-11881), [FND-11882](../findings/data_models-117.md#FND-11882), [FND-11883](../findings/data_models-117.md#FND-11883), [FND-11884](../findings/data_models-117.md#FND-11884), [FND-11885](../findings/data_models-117.md#FND-11885), [FND-11886](../findings/data_models-117.md#FND-11886), [FND-11887](../findings/data_models-117.md#FND-11887), [FND-11888](../findings/data_models-117.md#FND-11888), [FND-11889](../findings/data_models-117.md#FND-11889), [FND-11890](../findings/data_models-117.md#FND-11890), [FND-11891](../findings/data_models-117.md#FND-11891), [FND-11892](../findings/data_models-117.md#FND-11892), [FND-11893](../findings/data_models-117.md#FND-11893), [FND-11894](../findings/data_models-117.md#FND-11894), [FND-11895](../findings/data_models-117.md#FND-11895), [FND-11896](../findings/data_models-117.md#FND-11896), [FND-11897](../findings/data_models-117.md#FND-11897), [FND-11898](../findings/data_models-117.md#FND-11898), [FND-11899](../findings/data_models-117.md#FND-11899), [FND-11900](../findings/data_models-117.md#FND-11900)

## SRC-0642 — `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto`

- Type: rendered_protobuf_schema; bytes: 666; SHA-256: `5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 18; types: {"verified observation": 18}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11901](../findings/data_models-117.md#FND-11901), [FND-11902](../findings/data_models-117.md#FND-11902), [FND-11903](../findings/data_models-117.md#FND-11903), [FND-11904](../findings/data_models-117.md#FND-11904), [FND-11905](../findings/data_models-117.md#FND-11905), [FND-11906](../findings/data_models-117.md#FND-11906), [FND-11907](../findings/data_models-117.md#FND-11907), [FND-11908](../findings/data_models-117.md#FND-11908), [FND-11909](../findings/data_models-117.md#FND-11909), [FND-11910](../findings/data_models-117.md#FND-11910), [FND-11911](../findings/data_models-117.md#FND-11911), [FND-11912](../findings/data_models-117.md#FND-11912), [FND-11913](../findings/data_models-117.md#FND-11913), [FND-11914](../findings/data_models-117.md#FND-11914), [FND-11915](../findings/data_models-117.md#FND-11915), [FND-11916](../findings/data_models-117.md#FND-11916), [FND-11917](../findings/data_models-117.md#FND-11917), [FND-11918](../findings/data_models-117.md#FND-11918)

## SRC-0643 — `research/proto/chesscom/user_properties/v1/properties_user_settings.proto`

- Type: rendered_protobuf_schema; bytes: 17700; SHA-256: `b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 405; types: {"verified observation": 405}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-11919](../findings/data_models-117.md#FND-11919), [FND-11920](../findings/data_models-117.md#FND-11920), [FND-11921](../findings/data_models-117.md#FND-11921), [FND-11922](../findings/data_models-117.md#FND-11922), [FND-11923](../findings/data_models-117.md#FND-11923), [FND-11924](../findings/data_models-117.md#FND-11924), [FND-11925](../findings/data_models-117.md#FND-11925), [FND-11926](../findings/data_models-117.md#FND-11926), [FND-11927](../findings/data_models-117.md#FND-11927), [FND-11928](../findings/data_models-117.md#FND-11928), [FND-11929](../findings/data_models-117.md#FND-11929), [FND-11930](../findings/data_models-117.md#FND-11930), [FND-11931](../findings/data_models-117.md#FND-11931), [FND-11932](../findings/data_models-117.md#FND-11932), [FND-11933](../findings/data_models-117.md#FND-11933), [FND-11934](../findings/data_models-117.md#FND-11934), [FND-11935](../findings/data_models-117.md#FND-11935), [FND-11936](../findings/data_models-117.md#FND-11936), [FND-11937](../findings/data_models-117.md#FND-11937), [FND-11938](../findings/data_models-117.md#FND-11938), [FND-11939](../findings/data_models-117.md#FND-11939), [FND-11940](../findings/data_models-117.md#FND-11940), [FND-11941](../findings/data_models-117.md#FND-11941), [FND-11942](../findings/data_models-117.md#FND-11942), [FND-11943](../findings/data_models-117.md#FND-11943), [FND-11944](../findings/data_models-117.md#FND-11944), [FND-11945](../findings/data_models-117.md#FND-11945), [FND-11946](../findings/data_models-117.md#FND-11946), [FND-11947](../findings/data_models-117.md#FND-11947), [FND-11948](../findings/data_models-117.md#FND-11948), [FND-11949](../findings/data_models-117.md#FND-11949), [FND-11950](../findings/data_models-117.md#FND-11950), [FND-11951](../findings/data_models-117.md#FND-11951), [FND-11952](../findings/data_models-117.md#FND-11952), [FND-11953](../findings/data_models-117.md#FND-11953), [FND-11954](../findings/data_models-117.md#FND-11954), [FND-11955](../findings/data_models-117.md#FND-11955), [FND-11956](../findings/data_models-117.md#FND-11956), [FND-11957](../findings/data_models-117.md#FND-11957), [FND-11958](../findings/data_models-117.md#FND-11958), [FND-11959](../findings/data_models-117.md#FND-11959), [FND-11960](../findings/data_models-117.md#FND-11960), [FND-11961](../findings/data_models-117.md#FND-11961), [FND-11962](../findings/data_models-117.md#FND-11962), [FND-11963](../findings/data_models-117.md#FND-11963), [FND-11964](../findings/data_models-117.md#FND-11964), [FND-11965](../findings/data_models-117.md#FND-11965), [FND-11966](../findings/data_models-117.md#FND-11966), [FND-11967](../findings/data_models-117.md#FND-11967), [FND-11968](../findings/data_models-117.md#FND-11968), [FND-11969](../findings/data_models-117.md#FND-11969), [FND-11970](../findings/data_models-117.md#FND-11970), [FND-11971](../findings/data_models-117.md#FND-11971), [FND-11972](../findings/data_models-117.md#FND-11972), [FND-11973](../findings/data_models-117.md#FND-11973), [FND-11974](../findings/data_models-117.md#FND-11974), [FND-11975](../findings/data_models-118.md#FND-11975), [FND-11976](../findings/data_models-118.md#FND-11976), [FND-11977](../findings/data_models-118.md#FND-11977), [FND-11978](../findings/data_models-118.md#FND-11978), [FND-11979](../findings/data_models-118.md#FND-11979), [FND-11980](../findings/data_models-118.md#FND-11980), [FND-11981](../findings/data_models-118.md#FND-11981), [FND-11982](../findings/data_models-118.md#FND-11982), [FND-11983](../findings/data_models-118.md#FND-11983), [FND-11984](../findings/data_models-118.md#FND-11984), [FND-11985](../findings/data_models-118.md#FND-11985), [FND-11986](../findings/data_models-118.md#FND-11986), [FND-11987](../findings/data_models-118.md#FND-11987), [FND-11988](../findings/data_models-118.md#FND-11988), [FND-11989](../findings/data_models-118.md#FND-11989), [FND-11990](../findings/data_models-118.md#FND-11990), [FND-11991](../findings/data_models-118.md#FND-11991), [FND-11992](../findings/data_models-118.md#FND-11992), [FND-11993](../findings/data_models-118.md#FND-11993), [FND-11994](../findings/data_models-118.md#FND-11994), [FND-11995](../findings/data_models-118.md#FND-11995), [FND-11996](../findings/data_models-118.md#FND-11996), [FND-11997](../findings/data_models-118.md#FND-11997), [FND-11998](../findings/data_models-118.md#FND-11998), [FND-11999](../findings/data_models-118.md#FND-11999), [FND-12000](../findings/data_models-118.md#FND-12000), [FND-12001](../findings/data_models-118.md#FND-12001), [FND-12002](../findings/data_models-118.md#FND-12002), [FND-12003](../findings/data_models-118.md#FND-12003), [FND-12004](../findings/data_models-118.md#FND-12004), [FND-12005](../findings/data_models-118.md#FND-12005), [FND-12006](../findings/data_models-118.md#FND-12006), [FND-12007](../findings/data_models-118.md#FND-12007), [FND-12008](../findings/data_models-118.md#FND-12008), [FND-12009](../findings/data_models-118.md#FND-12009), [FND-12010](../findings/data_models-118.md#FND-12010), [FND-12011](../findings/data_models-118.md#FND-12011), [FND-12012](../findings/data_models-118.md#FND-12012), [FND-12013](../findings/data_models-118.md#FND-12013), [FND-12014](../findings/data_models-118.md#FND-12014), [FND-12015](../findings/data_models-118.md#FND-12015), [FND-12016](../findings/data_models-118.md#FND-12016), [FND-12017](../findings/data_models-118.md#FND-12017), [FND-12018](../findings/data_models-118.md#FND-12018), [FND-12019](../findings/data_models-118.md#FND-12019), [FND-12020](../findings/data_models-118.md#FND-12020), [FND-12021](../findings/data_models-118.md#FND-12021), [FND-12022](../findings/data_models-118.md#FND-12022), [FND-12023](../findings/data_models-118.md#FND-12023), [FND-12024](../findings/data_models-118.md#FND-12024), [FND-12025](../findings/data_models-118.md#FND-12025), [FND-12026](../findings/data_models-118.md#FND-12026), [FND-12027](../findings/data_models-118.md#FND-12027), [FND-12028](../findings/data_models-118.md#FND-12028), [FND-12029](../findings/data_models-118.md#FND-12029), [FND-12030](../findings/data_models-118.md#FND-12030), [FND-12031](../findings/data_models-118.md#FND-12031), [FND-12032](../findings/data_models-118.md#FND-12032), [FND-12033](../findings/data_models-118.md#FND-12033), [FND-12034](../findings/data_models-118.md#FND-12034), [FND-12035](../findings/data_models-118.md#FND-12035), [FND-12036](../findings/data_models-118.md#FND-12036), [FND-12037](../findings/data_models-118.md#FND-12037), [FND-12038](../findings/data_models-118.md#FND-12038), [FND-12039](../findings/data_models-118.md#FND-12039), [FND-12040](../findings/data_models-118.md#FND-12040), [FND-12041](../findings/data_models-118.md#FND-12041), [FND-12042](../findings/data_models-118.md#FND-12042), [FND-12043](../findings/data_models-118.md#FND-12043), [FND-12044](../findings/data_models-118.md#FND-12044), [FND-12045](../findings/data_models-118.md#FND-12045), [FND-12046](../findings/data_models-118.md#FND-12046), [FND-12047](../findings/data_models-118.md#FND-12047), [FND-12048](../findings/data_models-118.md#FND-12048), [FND-12049](../findings/data_models-118.md#FND-12049), [FND-12050](../findings/data_models-118.md#FND-12050), [FND-12051](../findings/data_models-118.md#FND-12051), [FND-12052](../findings/data_models-118.md#FND-12052), [FND-12053](../findings/data_models-118.md#FND-12053), [FND-12054](../findings/data_models-118.md#FND-12054), [FND-12055](../findings/data_models-118.md#FND-12055), [FND-12056](../findings/data_models-118.md#FND-12056), [FND-12057](../findings/data_models-118.md#FND-12057), [FND-12058](../findings/data_models-118.md#FND-12058), [FND-12059](../findings/data_models-118.md#FND-12059), [FND-12060](../findings/data_models-118.md#FND-12060), [FND-12061](../findings/data_models-118.md#FND-12061), [FND-12062](../findings/data_models-118.md#FND-12062), [FND-12063](../findings/data_models-118.md#FND-12063), [FND-12064](../findings/data_models-118.md#FND-12064), [FND-12065](../findings/data_models-118.md#FND-12065), [FND-12066](../findings/data_models-118.md#FND-12066), [FND-12067](../findings/data_models-118.md#FND-12067), [FND-12068](../findings/data_models-118.md#FND-12068), [FND-12069](../findings/data_models-118.md#FND-12069), [FND-12070](../findings/data_models-118.md#FND-12070), [FND-12071](../findings/data_models-118.md#FND-12071), [FND-12072](../findings/data_models-118.md#FND-12072), [FND-12073](../findings/data_models-118.md#FND-12073), [FND-12074](../findings/data_models-118.md#FND-12074), [FND-12075](../findings/data_models-119.md#FND-12075), [FND-12076](../findings/data_models-119.md#FND-12076), [FND-12077](../findings/data_models-119.md#FND-12077), [FND-12078](../findings/data_models-119.md#FND-12078), [FND-12079](../findings/data_models-119.md#FND-12079), [FND-12080](../findings/data_models-119.md#FND-12080), [FND-12081](../findings/data_models-119.md#FND-12081), [FND-12082](../findings/data_models-119.md#FND-12082), [FND-12083](../findings/data_models-119.md#FND-12083), [FND-12084](../findings/data_models-119.md#FND-12084), [FND-12085](../findings/data_models-119.md#FND-12085), [FND-12086](../findings/data_models-119.md#FND-12086), [FND-12087](../findings/data_models-119.md#FND-12087), [FND-12088](../findings/data_models-119.md#FND-12088), [FND-12089](../findings/data_models-119.md#FND-12089), [FND-12090](../findings/data_models-119.md#FND-12090), [FND-12091](../findings/data_models-119.md#FND-12091), [FND-12092](../findings/data_models-119.md#FND-12092), [FND-12093](../findings/data_models-119.md#FND-12093), [FND-12094](../findings/data_models-119.md#FND-12094), [FND-12095](../findings/data_models-119.md#FND-12095), [FND-12096](../findings/data_models-119.md#FND-12096), [FND-12097](../findings/data_models-119.md#FND-12097), [FND-12098](../findings/data_models-119.md#FND-12098), [FND-12099](../findings/data_models-119.md#FND-12099), [FND-12100](../findings/data_models-119.md#FND-12100), [FND-12101](../findings/data_models-119.md#FND-12101), [FND-12102](../findings/data_models-119.md#FND-12102), [FND-12103](../findings/data_models-119.md#FND-12103), [FND-12104](../findings/data_models-119.md#FND-12104), [FND-12105](../findings/data_models-119.md#FND-12105), [FND-12106](../findings/data_models-119.md#FND-12106), [FND-12107](../findings/data_models-119.md#FND-12107), [FND-12108](../findings/data_models-119.md#FND-12108), [FND-12109](../findings/data_models-119.md#FND-12109), [FND-12110](../findings/data_models-119.md#FND-12110), [FND-12111](../findings/data_models-119.md#FND-12111), [FND-12112](../findings/data_models-119.md#FND-12112), [FND-12113](../findings/data_models-119.md#FND-12113), [FND-12114](../findings/data_models-119.md#FND-12114), [FND-12115](../findings/data_models-119.md#FND-12115), [FND-12116](../findings/data_models-119.md#FND-12116), [FND-12117](../findings/data_models-119.md#FND-12117), [FND-12118](../findings/data_models-119.md#FND-12118), [FND-12119](../findings/data_models-119.md#FND-12119), [FND-12120](../findings/data_models-119.md#FND-12120), [FND-12121](../findings/data_models-119.md#FND-12121), [FND-12122](../findings/data_models-119.md#FND-12122), [FND-12123](../findings/data_models-119.md#FND-12123), [FND-12124](../findings/data_models-119.md#FND-12124), [FND-12125](../findings/data_models-119.md#FND-12125), [FND-12126](../findings/data_models-119.md#FND-12126), [FND-12127](../findings/data_models-119.md#FND-12127), [FND-12128](../findings/data_models-119.md#FND-12128), [FND-12129](../findings/data_models-119.md#FND-12129), [FND-12130](../findings/data_models-119.md#FND-12130), [FND-12131](../findings/data_models-119.md#FND-12131), [FND-12132](../findings/data_models-119.md#FND-12132), [FND-12133](../findings/data_models-119.md#FND-12133), [FND-12134](../findings/data_models-119.md#FND-12134), [FND-12135](../findings/data_models-119.md#FND-12135), [FND-12136](../findings/data_models-119.md#FND-12136), [FND-12137](../findings/data_models-119.md#FND-12137), [FND-12138](../findings/data_models-119.md#FND-12138), [FND-12139](../findings/data_models-119.md#FND-12139), [FND-12140](../findings/data_models-119.md#FND-12140), [FND-12141](../findings/data_models-119.md#FND-12141), [FND-12142](../findings/data_models-119.md#FND-12142), [FND-12143](../findings/data_models-119.md#FND-12143), [FND-12144](../findings/data_models-119.md#FND-12144), [FND-12145](../findings/data_models-119.md#FND-12145), [FND-12146](../findings/data_models-119.md#FND-12146), [FND-12147](../findings/data_models-119.md#FND-12147), [FND-12148](../findings/data_models-119.md#FND-12148), [FND-12149](../findings/data_models-119.md#FND-12149), [FND-12150](../findings/data_models-119.md#FND-12150), [FND-12151](../findings/data_models-119.md#FND-12151), [FND-12152](../findings/data_models-119.md#FND-12152), [FND-12153](../findings/data_models-119.md#FND-12153), [FND-12154](../findings/data_models-119.md#FND-12154), [FND-12155](../findings/data_models-119.md#FND-12155), [FND-12156](../findings/data_models-119.md#FND-12156), [FND-12157](../findings/data_models-119.md#FND-12157), [FND-12158](../findings/data_models-119.md#FND-12158), [FND-12159](../findings/data_models-119.md#FND-12159), [FND-12160](../findings/data_models-119.md#FND-12160), [FND-12161](../findings/data_models-119.md#FND-12161), [FND-12162](../findings/data_models-119.md#FND-12162), [FND-12163](../findings/data_models-119.md#FND-12163), [FND-12164](../findings/data_models-119.md#FND-12164), [FND-12165](../findings/data_models-119.md#FND-12165), [FND-12166](../findings/data_models-119.md#FND-12166), [FND-12167](../findings/data_models-119.md#FND-12167), [FND-12168](../findings/data_models-119.md#FND-12168), [FND-12169](../findings/data_models-119.md#FND-12169), [FND-12170](../findings/data_models-119.md#FND-12170), [FND-12171](../findings/data_models-119.md#FND-12171), [FND-12172](../findings/data_models-119.md#FND-12172), [FND-12173](../findings/data_models-119.md#FND-12173), [FND-12174](../findings/data_models-119.md#FND-12174), [FND-12175](../findings/data_models-120.md#FND-12175), [FND-12176](../findings/data_models-120.md#FND-12176), [FND-12177](../findings/data_models-120.md#FND-12177), [FND-12178](../findings/data_models-120.md#FND-12178), [FND-12179](../findings/data_models-120.md#FND-12179), [FND-12180](../findings/data_models-120.md#FND-12180), [FND-12181](../findings/data_models-120.md#FND-12181), [FND-12182](../findings/data_models-120.md#FND-12182), [FND-12183](../findings/data_models-120.md#FND-12183), [FND-12184](../findings/data_models-120.md#FND-12184), [FND-12185](../findings/data_models-120.md#FND-12185), [FND-12186](../findings/data_models-120.md#FND-12186), [FND-12187](../findings/data_models-120.md#FND-12187), [FND-12188](../findings/data_models-120.md#FND-12188), [FND-12189](../findings/data_models-120.md#FND-12189), [FND-12190](../findings/data_models-120.md#FND-12190), [FND-12191](../findings/data_models-120.md#FND-12191), [FND-12192](../findings/data_models-120.md#FND-12192), [FND-12193](../findings/data_models-120.md#FND-12193), [FND-12194](../findings/data_models-120.md#FND-12194), [FND-12195](../findings/data_models-120.md#FND-12195), [FND-12196](../findings/data_models-120.md#FND-12196), [FND-12197](../findings/data_models-120.md#FND-12197), [FND-12198](../findings/data_models-120.md#FND-12198), [FND-12199](../findings/data_models-120.md#FND-12199), [FND-12200](../findings/data_models-120.md#FND-12200), [FND-12201](../findings/data_models-120.md#FND-12201), [FND-12202](../findings/data_models-120.md#FND-12202), [FND-12203](../findings/data_models-120.md#FND-12203), [FND-12204](../findings/data_models-120.md#FND-12204), [FND-12205](../findings/data_models-120.md#FND-12205), [FND-12206](../findings/data_models-120.md#FND-12206), [FND-12207](../findings/data_models-120.md#FND-12207), [FND-12208](../findings/data_models-120.md#FND-12208), [FND-12209](../findings/data_models-120.md#FND-12209), [FND-12210](../findings/data_models-120.md#FND-12210), [FND-12211](../findings/data_models-120.md#FND-12211), [FND-12212](../findings/data_models-120.md#FND-12212), [FND-12213](../findings/data_models-120.md#FND-12213), [FND-12214](../findings/data_models-120.md#FND-12214), [FND-12215](../findings/data_models-120.md#FND-12215), [FND-12216](../findings/data_models-120.md#FND-12216), [FND-12217](../findings/data_models-120.md#FND-12217), [FND-12218](../findings/data_models-120.md#FND-12218), [FND-12219](../findings/data_models-120.md#FND-12219), [FND-12220](../findings/data_models-120.md#FND-12220), [FND-12221](../findings/data_models-120.md#FND-12221), [FND-12222](../findings/data_models-120.md#FND-12222), [FND-12223](../findings/data_models-120.md#FND-12223), [FND-12224](../findings/data_models-120.md#FND-12224), [FND-12225](../findings/data_models-120.md#FND-12225), [FND-12226](../findings/data_models-120.md#FND-12226), [FND-12227](../findings/data_models-120.md#FND-12227), [FND-12228](../findings/data_models-120.md#FND-12228), [FND-12229](../findings/data_models-120.md#FND-12229), [FND-12230](../findings/data_models-120.md#FND-12230), [FND-12231](../findings/data_models-120.md#FND-12231), [FND-12232](../findings/data_models-120.md#FND-12232), [FND-12233](../findings/data_models-120.md#FND-12233), [FND-12234](../findings/data_models-120.md#FND-12234), [FND-12235](../findings/data_models-120.md#FND-12235), [FND-12236](../findings/data_models-120.md#FND-12236), [FND-12237](../findings/data_models-120.md#FND-12237), [FND-12238](../findings/data_models-120.md#FND-12238), [FND-12239](../findings/data_models-120.md#FND-12239), [FND-12240](../findings/data_models-120.md#FND-12240), [FND-12241](../findings/data_models-120.md#FND-12241), [FND-12242](../findings/data_models-120.md#FND-12242), [FND-12243](../findings/data_models-120.md#FND-12243), [FND-12244](../findings/data_models-120.md#FND-12244), [FND-12245](../findings/data_models-120.md#FND-12245), [FND-12246](../findings/data_models-120.md#FND-12246), [FND-12247](../findings/data_models-120.md#FND-12247), [FND-12248](../findings/data_models-120.md#FND-12248), [FND-12249](../findings/data_models-120.md#FND-12249), [FND-12250](../findings/data_models-120.md#FND-12250), [FND-12251](../findings/data_models-120.md#FND-12251), [FND-12252](../findings/data_models-120.md#FND-12252), [FND-12253](../findings/data_models-120.md#FND-12253), [FND-12254](../findings/data_models-120.md#FND-12254), [FND-12255](../findings/data_models-120.md#FND-12255), [FND-12256](../findings/data_models-120.md#FND-12256), [FND-12257](../findings/data_models-120.md#FND-12257), [FND-12258](../findings/data_models-120.md#FND-12258), [FND-12259](../findings/data_models-120.md#FND-12259), [FND-12260](../findings/data_models-120.md#FND-12260), [FND-12261](../findings/data_models-120.md#FND-12261), [FND-12262](../findings/data_models-120.md#FND-12262), [FND-12263](../findings/data_models-120.md#FND-12263), [FND-12264](../findings/data_models-120.md#FND-12264), [FND-12265](../findings/data_models-120.md#FND-12265), [FND-12266](../findings/data_models-120.md#FND-12266), [FND-12267](../findings/data_models-120.md#FND-12267), [FND-12268](../findings/data_models-120.md#FND-12268), [FND-12269](../findings/data_models-120.md#FND-12269), [FND-12270](../findings/data_models-120.md#FND-12270), [FND-12271](../findings/data_models-120.md#FND-12271), [FND-12272](../findings/data_models-120.md#FND-12272), [FND-12273](../findings/data_models-120.md#FND-12273), [FND-12274](../findings/data_models-120.md#FND-12274), [FND-12275](../findings/data_models-121.md#FND-12275), [FND-12276](../findings/data_models-121.md#FND-12276), [FND-12277](../findings/data_models-121.md#FND-12277), [FND-12278](../findings/data_models-121.md#FND-12278), [FND-12279](../findings/data_models-121.md#FND-12279), [FND-12280](../findings/data_models-121.md#FND-12280), [FND-12281](../findings/data_models-121.md#FND-12281), [FND-12282](../findings/data_models-121.md#FND-12282), [FND-12283](../findings/data_models-121.md#FND-12283), [FND-12284](../findings/data_models-121.md#FND-12284), [FND-12285](../findings/data_models-121.md#FND-12285), [FND-12286](../findings/data_models-121.md#FND-12286), [FND-12287](../findings/data_models-121.md#FND-12287), [FND-12288](../findings/data_models-121.md#FND-12288), [FND-12289](../findings/data_models-121.md#FND-12289), [FND-12290](../findings/data_models-121.md#FND-12290), [FND-12291](../findings/data_models-121.md#FND-12291), [FND-12292](../findings/data_models-121.md#FND-12292), [FND-12293](../findings/data_models-121.md#FND-12293), [FND-12294](../findings/data_models-121.md#FND-12294), [FND-12295](../findings/data_models-121.md#FND-12295), [FND-12296](../findings/data_models-121.md#FND-12296), [FND-12297](../findings/data_models-121.md#FND-12297), [FND-12298](../findings/data_models-121.md#FND-12298), [FND-12299](../findings/data_models-121.md#FND-12299), [FND-12300](../findings/data_models-121.md#FND-12300), [FND-12301](../findings/data_models-121.md#FND-12301), [FND-12302](../findings/data_models-121.md#FND-12302), [FND-12303](../findings/data_models-121.md#FND-12303), [FND-12304](../findings/data_models-121.md#FND-12304), [FND-12305](../findings/data_models-121.md#FND-12305), [FND-12306](../findings/data_models-121.md#FND-12306), [FND-12307](../findings/data_models-121.md#FND-12307), [FND-12308](../findings/data_models-121.md#FND-12308), [FND-12309](../findings/data_models-121.md#FND-12309), [FND-12310](../findings/data_models-121.md#FND-12310), [FND-12311](../findings/data_models-121.md#FND-12311), [FND-12312](../findings/data_models-121.md#FND-12312), [FND-12313](../findings/data_models-121.md#FND-12313), [FND-12314](../findings/data_models-121.md#FND-12314), [FND-12315](../findings/data_models-121.md#FND-12315), [FND-12316](../findings/data_models-121.md#FND-12316), [FND-12317](../findings/data_models-121.md#FND-12317), [FND-12318](../findings/data_models-121.md#FND-12318), [FND-12319](../findings/data_models-121.md#FND-12319), [FND-12320](../findings/data_models-121.md#FND-12320), [FND-12321](../findings/data_models-121.md#FND-12321), [FND-12322](../findings/data_models-121.md#FND-12322), [FND-12323](../findings/data_models-121.md#FND-12323)

## SRC-0644 — `research/proto/chesscom/user_properties/v1/properties_user_streak_v2.proto`

- Type: rendered_protobuf_schema; bytes: 926; SHA-256: `ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 23; types: {"verified observation": 23}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/ee5bc58e41fa2d994ea451baa988e653083bbbe0aef9da3c229ed9b303d2c383.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-12324](../findings/data_models-121.md#FND-12324), [FND-12325](../findings/data_models-121.md#FND-12325), [FND-12326](../findings/data_models-121.md#FND-12326), [FND-12327](../findings/data_models-121.md#FND-12327), [FND-12328](../findings/data_models-121.md#FND-12328), [FND-12329](../findings/data_models-121.md#FND-12329), [FND-12330](../findings/data_models-121.md#FND-12330), [FND-12331](../findings/data_models-121.md#FND-12331), [FND-12332](../findings/data_models-121.md#FND-12332), [FND-12333](../findings/data_models-121.md#FND-12333), [FND-12334](../findings/data_models-121.md#FND-12334), [FND-12335](../findings/data_models-121.md#FND-12335), [FND-12336](../findings/data_models-121.md#FND-12336), [FND-12337](../findings/data_models-121.md#FND-12337), [FND-12338](../findings/data_models-121.md#FND-12338), [FND-12339](../findings/data_models-121.md#FND-12339), [FND-12340](../findings/data_models-121.md#FND-12340), [FND-12341](../findings/data_models-121.md#FND-12341), [FND-12342](../findings/data_models-121.md#FND-12342), [FND-12343](../findings/data_models-121.md#FND-12343), [FND-12344](../findings/data_models-121.md#FND-12344), [FND-12345](../findings/data_models-121.md#FND-12345), [FND-12346](../findings/data_models-121.md#FND-12346)

## SRC-0645 — `research/proto/chesscom/user_properties/v1/properties_wdl.proto`

- Type: rendered_protobuf_schema; bytes: 4775; SHA-256: `ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 138; types: {"verified observation": 138}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-12347](../findings/data_models-121.md#FND-12347), [FND-12348](../findings/data_models-121.md#FND-12348), [FND-12349](../findings/data_models-121.md#FND-12349), [FND-12350](../findings/data_models-121.md#FND-12350), [FND-12351](../findings/data_models-121.md#FND-12351), [FND-12352](../findings/data_models-121.md#FND-12352), [FND-12353](../findings/data_models-121.md#FND-12353), [FND-12354](../findings/data_models-121.md#FND-12354), [FND-12355](../findings/data_models-121.md#FND-12355), [FND-12356](../findings/data_models-121.md#FND-12356), [FND-12357](../findings/data_models-121.md#FND-12357), [FND-12358](../findings/data_models-121.md#FND-12358), [FND-12359](../findings/data_models-121.md#FND-12359), [FND-12360](../findings/data_models-121.md#FND-12360), [FND-12361](../findings/data_models-121.md#FND-12361), [FND-12362](../findings/data_models-121.md#FND-12362), [FND-12363](../findings/data_models-121.md#FND-12363), [FND-12364](../findings/data_models-121.md#FND-12364), [FND-12365](../findings/data_models-121.md#FND-12365), [FND-12366](../findings/data_models-121.md#FND-12366), [FND-12367](../findings/data_models-121.md#FND-12367), [FND-12368](../findings/data_models-121.md#FND-12368), [FND-12369](../findings/data_models-121.md#FND-12369), [FND-12370](../findings/data_models-121.md#FND-12370), [FND-12371](../findings/data_models-121.md#FND-12371), [FND-12372](../findings/data_models-121.md#FND-12372), [FND-12373](../findings/data_models-121.md#FND-12373), [FND-12374](../findings/data_models-121.md#FND-12374), [FND-12375](../findings/data_models-122.md#FND-12375), [FND-12376](../findings/data_models-122.md#FND-12376), [FND-12377](../findings/data_models-122.md#FND-12377), [FND-12378](../findings/data_models-122.md#FND-12378), [FND-12379](../findings/data_models-122.md#FND-12379), [FND-12380](../findings/data_models-122.md#FND-12380), [FND-12381](../findings/data_models-122.md#FND-12381), [FND-12382](../findings/data_models-122.md#FND-12382), [FND-12383](../findings/data_models-122.md#FND-12383), [FND-12384](../findings/data_models-122.md#FND-12384), [FND-12385](../findings/data_models-122.md#FND-12385), [FND-12386](../findings/data_models-122.md#FND-12386), [FND-12387](../findings/data_models-122.md#FND-12387), [FND-12388](../findings/data_models-122.md#FND-12388), [FND-12389](../findings/data_models-122.md#FND-12389), [FND-12390](../findings/data_models-122.md#FND-12390), [FND-12391](../findings/data_models-122.md#FND-12391), [FND-12392](../findings/data_models-122.md#FND-12392), [FND-12393](../findings/data_models-122.md#FND-12393), [FND-12394](../findings/data_models-122.md#FND-12394), [FND-12395](../findings/data_models-122.md#FND-12395), [FND-12396](../findings/data_models-122.md#FND-12396), [FND-12397](../findings/data_models-122.md#FND-12397), [FND-12398](../findings/data_models-122.md#FND-12398), [FND-12399](../findings/data_models-122.md#FND-12399), [FND-12400](../findings/data_models-122.md#FND-12400), [FND-12401](../findings/data_models-122.md#FND-12401), [FND-12402](../findings/data_models-122.md#FND-12402), [FND-12403](../findings/data_models-122.md#FND-12403), [FND-12404](../findings/data_models-122.md#FND-12404), [FND-12405](../findings/data_models-122.md#FND-12405), [FND-12406](../findings/data_models-122.md#FND-12406), [FND-12407](../findings/data_models-122.md#FND-12407), [FND-12408](../findings/data_models-122.md#FND-12408), [FND-12409](../findings/data_models-122.md#FND-12409), [FND-12410](../findings/data_models-122.md#FND-12410), [FND-12411](../findings/data_models-122.md#FND-12411), [FND-12412](../findings/data_models-122.md#FND-12412), [FND-12413](../findings/data_models-122.md#FND-12413), [FND-12414](../findings/data_models-122.md#FND-12414), [FND-12415](../findings/data_models-122.md#FND-12415), [FND-12416](../findings/data_models-122.md#FND-12416), [FND-12417](../findings/data_models-122.md#FND-12417), [FND-12418](../findings/data_models-122.md#FND-12418), [FND-12419](../findings/data_models-122.md#FND-12419), [FND-12420](../findings/data_models-122.md#FND-12420), [FND-12421](../findings/data_models-122.md#FND-12421), [FND-12422](../findings/data_models-122.md#FND-12422), [FND-12423](../findings/data_models-122.md#FND-12423), [FND-12424](../findings/data_models-122.md#FND-12424), [FND-12425](../findings/data_models-122.md#FND-12425), [FND-12426](../findings/data_models-122.md#FND-12426), [FND-12427](../findings/data_models-122.md#FND-12427), [FND-12428](../findings/data_models-122.md#FND-12428), [FND-12429](../findings/data_models-122.md#FND-12429), [FND-12430](../findings/data_models-122.md#FND-12430), [FND-12431](../findings/data_models-122.md#FND-12431), [FND-12432](../findings/data_models-122.md#FND-12432), [FND-12433](../findings/data_models-122.md#FND-12433), [FND-12434](../findings/data_models-122.md#FND-12434), [FND-12435](../findings/data_models-122.md#FND-12435), [FND-12436](../findings/data_models-122.md#FND-12436), [FND-12437](../findings/data_models-122.md#FND-12437), [FND-12438](../findings/data_models-122.md#FND-12438), [FND-12439](../findings/data_models-122.md#FND-12439), [FND-12440](../findings/data_models-122.md#FND-12440), [FND-12441](../findings/data_models-122.md#FND-12441), [FND-12442](../findings/data_models-122.md#FND-12442), [FND-12443](../findings/data_models-122.md#FND-12443), [FND-12444](../findings/data_models-122.md#FND-12444), [FND-12445](../findings/data_models-122.md#FND-12445), [FND-12446](../findings/data_models-122.md#FND-12446), [FND-12447](../findings/data_models-122.md#FND-12447), [FND-12448](../findings/data_models-122.md#FND-12448), [FND-12449](../findings/data_models-122.md#FND-12449), [FND-12450](../findings/data_models-122.md#FND-12450), [FND-12451](../findings/data_models-122.md#FND-12451), [FND-12452](../findings/data_models-122.md#FND-12452), [FND-12453](../findings/data_models-122.md#FND-12453), [FND-12454](../findings/data_models-122.md#FND-12454), [FND-12455](../findings/data_models-122.md#FND-12455), [FND-12456](../findings/data_models-122.md#FND-12456), [FND-12457](../findings/data_models-122.md#FND-12457), [FND-12458](../findings/data_models-122.md#FND-12458), [FND-12459](../findings/data_models-122.md#FND-12459), [FND-12460](../findings/data_models-122.md#FND-12460), [FND-12461](../findings/data_models-122.md#FND-12461), [FND-12462](../findings/data_models-122.md#FND-12462), [FND-12463](../findings/data_models-122.md#FND-12463), [FND-12464](../findings/data_models-122.md#FND-12464), [FND-12465](../findings/data_models-122.md#FND-12465), [FND-12466](../findings/data_models-122.md#FND-12466), [FND-12467](../findings/data_models-122.md#FND-12467), [FND-12468](../findings/data_models-122.md#FND-12468), [FND-12469](../findings/data_models-122.md#FND-12469), [FND-12470](../findings/data_models-122.md#FND-12470), [FND-12471](../findings/data_models-122.md#FND-12471), [FND-12472](../findings/data_models-122.md#FND-12472), [FND-12473](../findings/data_models-122.md#FND-12473), [FND-12474](../findings/data_models-122.md#FND-12474), [FND-12475](../findings/data_models-123.md#FND-12475), [FND-12476](../findings/data_models-123.md#FND-12476), [FND-12477](../findings/data_models-123.md#FND-12477), [FND-12478](../findings/data_models-123.md#FND-12478), [FND-12479](../findings/data_models-123.md#FND-12479), [FND-12480](../findings/data_models-123.md#FND-12480), [FND-12481](../findings/data_models-123.md#FND-12481), [FND-12482](../findings/data_models-123.md#FND-12482), [FND-12483](../findings/data_models-123.md#FND-12483), [FND-12484](../findings/data_models-123.md#FND-12484)

## SRC-0646 — `research/proto/chesscom/user_properties/v1/properties_widgets.proto`

- Type: rendered_protobuf_schema; bytes: 339; SHA-256: `df433be187454b21e61bff09f0e69d4539c8be15435a53280688986b5f5e5c87`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 7; types: {"verified observation": 7}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/df433be187454b21e61bff09f0e69d4539c8be15435a53280688986b5f5e5c87.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-12485](../findings/data_models-123.md#FND-12485), [FND-12486](../findings/data_models-123.md#FND-12486), [FND-12487](../findings/data_models-123.md#FND-12487), [FND-12488](../findings/data_models-123.md#FND-12488), [FND-12489](../findings/data_models-123.md#FND-12489), [FND-12490](../findings/data_models-123.md#FND-12490), [FND-12491](../findings/data_models-123.md#FND-12491)

## SRC-0647 — `research/proto/chesscom/user_relationships/v2/list_user_relationships_model.proto`

- Type: rendered_protobuf_schema; bytes: 433; SHA-256: `3625d965c1861d7b76ee7b2a00db7f6eabe22af311d284e164e3613e53732c4c`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 5; types: {"verified observation": 5}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/3625d965c1861d7b76ee7b2a00db7f6eabe22af311d284e164e3613e53732c4c.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-12492](../findings/data_models-123.md#FND-12492), [FND-12493](../findings/data_models-123.md#FND-12493), [FND-12494](../findings/data_models-123.md#FND-12494), [FND-12495](../findings/data_models-123.md#FND-12495), [FND-12496](../findings/data_models-123.md#FND-12496)

## SRC-0648 — `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto`

- Type: rendered_protobuf_schema; bytes: 1268; SHA-256: `993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 22; types: {"verified observation": 22}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-12497](../findings/data_models-123.md#FND-12497), [FND-12498](../findings/data_models-123.md#FND-12498), [FND-12499](../findings/data_models-123.md#FND-12499), [FND-12500](../findings/data_models-123.md#FND-12500), [FND-12501](../findings/data_models-123.md#FND-12501), [FND-12502](../findings/data_models-123.md#FND-12502), [FND-12503](../findings/data_models-123.md#FND-12503), [FND-12504](../findings/data_models-123.md#FND-12504), [FND-12505](../findings/data_models-123.md#FND-12505), [FND-12506](../findings/data_models-123.md#FND-12506), [FND-12507](../findings/data_models-123.md#FND-12507), [FND-12508](../findings/data_models-123.md#FND-12508), [FND-12509](../findings/data_models-123.md#FND-12509), [FND-12510](../findings/data_models-123.md#FND-12510), [FND-12511](../findings/data_models-123.md#FND-12511), [FND-12512](../findings/data_models-123.md#FND-12512), [FND-12513](../findings/data_models-123.md#FND-12513), [FND-12514](../findings/data_models-123.md#FND-12514), [FND-12515](../findings/data_models-123.md#FND-12515), [FND-12516](../findings/data_models-123.md#FND-12516), [FND-12517](../findings/data_models-123.md#FND-12517), [FND-12518](../findings/data_models-123.md#FND-12518)

## SRC-0649 — `research/proto/chesscom/user_targeting/v1/user_targeting.proto`

- Type: rendered_protobuf_schema; bytes: 3543; SHA-256: `4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 112; types: {"verified observation": 112}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-12519](../findings/data_models-123.md#FND-12519), [FND-12520](../findings/data_models-123.md#FND-12520), [FND-12521](../findings/data_models-123.md#FND-12521), [FND-12522](../findings/data_models-123.md#FND-12522), [FND-12523](../findings/data_models-123.md#FND-12523), [FND-12524](../findings/data_models-123.md#FND-12524), [FND-12525](../findings/data_models-123.md#FND-12525), [FND-12526](../findings/data_models-123.md#FND-12526), [FND-12527](../findings/data_models-123.md#FND-12527), [FND-12528](../findings/data_models-123.md#FND-12528), [FND-12529](../findings/data_models-123.md#FND-12529), [FND-12530](../findings/data_models-123.md#FND-12530), [FND-12531](../findings/data_models-123.md#FND-12531), [FND-12532](../findings/data_models-123.md#FND-12532), [FND-12533](../findings/data_models-123.md#FND-12533), [FND-12534](../findings/data_models-123.md#FND-12534), [FND-12535](../findings/data_models-123.md#FND-12535), [FND-12536](../findings/data_models-123.md#FND-12536), [FND-12537](../findings/data_models-123.md#FND-12537), [FND-12538](../findings/data_models-123.md#FND-12538), [FND-12539](../findings/data_models-123.md#FND-12539), [FND-12540](../findings/data_models-123.md#FND-12540), [FND-12541](../findings/data_models-123.md#FND-12541), [FND-12542](../findings/data_models-123.md#FND-12542), [FND-12543](../findings/data_models-123.md#FND-12543), [FND-12544](../findings/data_models-123.md#FND-12544), [FND-12545](../findings/data_models-123.md#FND-12545), [FND-12546](../findings/data_models-123.md#FND-12546), [FND-12547](../findings/data_models-123.md#FND-12547), [FND-12548](../findings/data_models-123.md#FND-12548), [FND-12549](../findings/data_models-123.md#FND-12549), [FND-12550](../findings/data_models-123.md#FND-12550), [FND-12551](../findings/data_models-123.md#FND-12551), [FND-12552](../findings/data_models-123.md#FND-12552), [FND-12553](../findings/data_models-123.md#FND-12553), [FND-12554](../findings/data_models-123.md#FND-12554), [FND-12555](../findings/data_models-123.md#FND-12555), [FND-12556](../findings/data_models-123.md#FND-12556), [FND-12557](../findings/data_models-123.md#FND-12557), [FND-12558](../findings/data_models-123.md#FND-12558), [FND-12559](../findings/data_models-123.md#FND-12559), [FND-12560](../findings/data_models-123.md#FND-12560), [FND-12561](../findings/data_models-123.md#FND-12561), [FND-12562](../findings/data_models-123.md#FND-12562), [FND-12563](../findings/data_models-123.md#FND-12563), [FND-12564](../findings/data_models-123.md#FND-12564), [FND-12565](../findings/data_models-123.md#FND-12565), [FND-12566](../findings/data_models-123.md#FND-12566), [FND-12567](../findings/data_models-123.md#FND-12567), [FND-12568](../findings/data_models-123.md#FND-12568), [FND-12569](../findings/data_models-123.md#FND-12569), [FND-12570](../findings/data_models-123.md#FND-12570), [FND-12571](../findings/data_models-123.md#FND-12571), [FND-12572](../findings/data_models-123.md#FND-12572), [FND-12573](../findings/data_models-123.md#FND-12573), [FND-12574](../findings/data_models-123.md#FND-12574), [FND-12575](../findings/data_models-124.md#FND-12575), [FND-12576](../findings/data_models-124.md#FND-12576), [FND-12577](../findings/data_models-124.md#FND-12577), [FND-12578](../findings/data_models-124.md#FND-12578), [FND-12579](../findings/data_models-124.md#FND-12579), [FND-12580](../findings/data_models-124.md#FND-12580), [FND-12581](../findings/data_models-124.md#FND-12581), [FND-12582](../findings/data_models-124.md#FND-12582), [FND-12583](../findings/data_models-124.md#FND-12583), [FND-12584](../findings/data_models-124.md#FND-12584), [FND-12585](../findings/data_models-124.md#FND-12585), [FND-12586](../findings/data_models-124.md#FND-12586), [FND-12587](../findings/data_models-124.md#FND-12587), [FND-12588](../findings/data_models-124.md#FND-12588), [FND-12589](../findings/data_models-124.md#FND-12589), [FND-12590](../findings/data_models-124.md#FND-12590), [FND-12591](../findings/data_models-124.md#FND-12591), [FND-12592](../findings/data_models-124.md#FND-12592), [FND-12593](../findings/data_models-124.md#FND-12593), [FND-12594](../findings/data_models-124.md#FND-12594), [FND-12595](../findings/data_models-124.md#FND-12595), [FND-12596](../findings/data_models-124.md#FND-12596), [FND-12597](../findings/data_models-124.md#FND-12597), [FND-12598](../findings/data_models-124.md#FND-12598), [FND-12599](../findings/data_models-124.md#FND-12599), [FND-12600](../findings/data_models-124.md#FND-12600), [FND-12601](../findings/data_models-124.md#FND-12601), [FND-12602](../findings/data_models-124.md#FND-12602), [FND-12603](../findings/data_models-124.md#FND-12603), [FND-12604](../findings/data_models-124.md#FND-12604), [FND-12605](../findings/data_models-124.md#FND-12605), [FND-12606](../findings/data_models-124.md#FND-12606), [FND-12607](../findings/data_models-124.md#FND-12607), [FND-12608](../findings/data_models-124.md#FND-12608), [FND-12609](../findings/data_models-124.md#FND-12609), [FND-12610](../findings/data_models-124.md#FND-12610), [FND-12611](../findings/data_models-124.md#FND-12611), [FND-12612](../findings/data_models-124.md#FND-12612), [FND-12613](../findings/data_models-124.md#FND-12613), [FND-12614](../findings/data_models-124.md#FND-12614), [FND-12615](../findings/data_models-124.md#FND-12615), [FND-12616](../findings/data_models-124.md#FND-12616), [FND-12617](../findings/data_models-124.md#FND-12617), [FND-12618](../findings/data_models-124.md#FND-12618), [FND-12619](../findings/data_models-124.md#FND-12619), [FND-12620](../findings/data_models-124.md#FND-12620), [FND-12621](../findings/data_models-124.md#FND-12621), [FND-12622](../findings/data_models-124.md#FND-12622), [FND-12623](../findings/data_models-124.md#FND-12623), [FND-12624](../findings/data_models-124.md#FND-12624), [FND-12625](../findings/data_models-124.md#FND-12625), [FND-12626](../findings/data_models-124.md#FND-12626), [FND-12627](../findings/data_models-124.md#FND-12627), [FND-12628](../findings/data_models-124.md#FND-12628), [FND-12629](../findings/data_models-124.md#FND-12629), [FND-12630](../findings/data_models-124.md#FND-12630)

## SRC-0650 — `research/proto/google/protobuf/any.proto`

- Type: rendered_protobuf_schema; bytes: 158; SHA-256: `a0d4f8867d12205accf8412c60e1f6dbdb2f063d4ac60b91f7eecf65bf9bf9a4`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 3; types: {"verified observation": 3}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/a0d4f8867d12205accf8412c60e1f6dbdb2f063d4ac60b91f7eecf65bf9bf9a4.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-12631](../findings/data_models-124.md#FND-12631), [FND-12632](../findings/data_models-124.md#FND-12632), [FND-12633](../findings/data_models-124.md#FND-12633)

## SRC-0651 — `research/proto/google/protobuf/duration.proto`

- Type: rendered_protobuf_schema; bytes: 166; SHA-256: `fdcba2cacfec3d23f2243080281fdb2093a7508041f090ad4253b922d7da78f5`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 3; types: {"verified observation": 3}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/fdcba2cacfec3d23f2243080281fdb2093a7508041f090ad4253b922d7da78f5.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-12634](../findings/data_models-124.md#FND-12634), [FND-12635](../findings/data_models-124.md#FND-12635), [FND-12636](../findings/data_models-124.md#FND-12636)

## SRC-0652 — `research/proto/google/protobuf/empty.proto`

- Type: rendered_protobuf_schema; bytes: 102; SHA-256: `8b5841292fcaa8f62fb6fe698c0e317ed4543ccf21b53284808ead3a59e2fcd8`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 1; types: {"verified observation": 1}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/8b5841292fcaa8f62fb6fe698c0e317ed4543ccf21b53284808ead3a59e2fcd8.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-12637](../findings/data_models-124.md#FND-12637)

## SRC-0653 — `research/proto/google/protobuf/field_mask.proto`

- Type: rendered_protobuf_schema; bytes: 140; SHA-256: `015c71a0c00eb2785937c5f846e2c9c87f35922cc3b8a86a13da5d22c62a20d0`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 2; types: {"verified observation": 2}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/015c71a0c00eb2785937c5f846e2c9c87f35922cc3b8a86a13da5d22c62a20d0.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-12638](../findings/data_models-124.md#FND-12638), [FND-12639](../findings/data_models-124.md#FND-12639)

## SRC-0654 — `research/proto/google/protobuf/struct.proto`

- Type: rendered_protobuf_schema; bytes: 619; SHA-256: `38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 17; types: {"verified observation": 17}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/38dac8f82281a986ce1aba1afb14023c3f0a5347d87daf4f69785949bd4e9fd9.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-12640](../findings/data_models-124.md#FND-12640), [FND-12641](../findings/data_models-124.md#FND-12641), [FND-12642](../findings/data_models-124.md#FND-12642), [FND-12643](../findings/data_models-124.md#FND-12643), [FND-12644](../findings/data_models-124.md#FND-12644), [FND-12645](../findings/data_models-124.md#FND-12645), [FND-12646](../findings/data_models-124.md#FND-12646), [FND-12647](../findings/data_models-124.md#FND-12647), [FND-12648](../findings/data_models-124.md#FND-12648), [FND-12649](../findings/data_models-124.md#FND-12649), [FND-12650](../findings/data_models-124.md#FND-12650), [FND-12651](../findings/data_models-124.md#FND-12651), [FND-12652](../findings/data_models-124.md#FND-12652), [FND-12653](../findings/data_models-124.md#FND-12653), [FND-12654](../findings/data_models-124.md#FND-12654), [FND-12655](../findings/data_models-124.md#FND-12655), [FND-12656](../findings/data_models-124.md#FND-12656)

## SRC-0655 — `research/proto/google/protobuf/timestamp.proto`

- Type: rendered_protobuf_schema; bytes: 168; SHA-256: `a748421bf54d9c568ff1c578cb2476b41321619a634adf5c80bca407c086100b`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: data_models.
- Findings: 3; types: {"verified observation": 3}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/a748421bf54d9c568ff1c578cb2476b41321619a634adf5c80bca407c086100b.proto) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-12657](../findings/data_models-124.md#FND-12657), [FND-12658](../findings/data_models-124.md#FND-12658), [FND-12659](../findings/data_models-124.md#FND-12659)

## SRC-0656 — `research/proto/index.json`

- Type: json_artifact; bytes: 23453; SHA-256: `218d9faaad81f610109eb65bbc05b35de552e879c2e350be736d85b8d68b768d`.
- Purpose: Recovered schema definition; field presence is an interface declaration, not proof of deployed endpoint use.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/218d9faaad81f610109eb65bbc05b35de552e879c2e350be736d85b8d68b768d.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0657 — `research/quota-hook.sha256`

- Type: notes_logs_or_dataset; bytes: 89; SHA-256: `80aa6ec81e0d3b9fb2740eb4c2f82033b24b47355c5f86c85fa8f89a179f9a6e`.
- Purpose: Historical investigation material; preserve exact contents and provenance.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/80aa6ec81e0d3b9fb2740eb4c2f82033b24b47355c5f86c85fa8f89a179f9a6e.sha256) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0658 — `research/quota-regression-v0.1.7.out`

- Type: notes_logs_or_dataset; bytes: 455; SHA-256: `72dac1e92f79a2efc12202d1fc63b251b183408e2d186d6628903eb05d6f7e05`.
- Purpose: Historical investigation material; preserve exact contents and provenance.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/72dac1e92f79a2efc12202d1fc63b251b183408e2d186d6628903eb05d6f7e05.out) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0659 — `research/refinement/build-comparison.py`

- Type: source_code; bytes: 4865; SHA-256: `589a5a02880edb1d00fec9f345624ed378b081cecf708ab8ee79f92f30ec8250`.
- Purpose: Historical investigation material; preserve exact contents and provenance.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: url_references.
- Findings: 1; types: {"verified observation": 1}.
- URL/reference count: 1.
- Incorporated: True.
- [Preserved evidence](../evidence/text/589a5a02880edb1d00fec9f345624ed378b081cecf708ab8ee79f92f30ec8250.py) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-20168](../findings/url_references-011.md#FND-20168)

## SRC-0660 — `research/refinement/build-report.mjs`

- Type: source_code; bytes: 6218; SHA-256: `e3872aef2c888219d18f135652c89bc8920d4e8def2b5b1409d7fd8ad8ea3b09`.
- Purpose: Historical investigation material; preserve exact contents and provenance.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: url_references.
- Findings: 1; types: {"verified observation": 1}.
- URL/reference count: 1.
- Incorporated: True.
- [Preserved evidence](../evidence/text/e3872aef2c888219d18f135652c89bc8920d4e8def2b5b1409d7fd8ad8ea3b09.mjs) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-20178](../findings/url_references-011.md#FND-20178)

## SRC-0661 — `research/refinement/comparison-trial.mjs`

- Type: source_code; bytes: 6899; SHA-256: `bdb6bf4b1463f5150da2084c0c861ed31474afe70bcea58bbb0bc33564073a70`.
- Purpose: Historical investigation material; preserve exact contents and provenance.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: experiments.
- Findings: 1; types: {"verified observation": 1}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/bdb6bf4b1463f5150da2084c0c861ed31474afe70bcea58bbb0bc33564073a70.mjs) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Finding IDs: [FND-18969](../findings/experiments-001.md#FND-18969)

## SRC-0662 — `research/refinement/configs/baseline.json`

- Type: json_artifact; bytes: 44; SHA-256: `634efbaebe97cb8fe83bec0c35b54167a97e9ab52dcbbbed7434303f30f2cf33`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/634efbaebe97cb8fe83bec0c35b54167a97e9ab52dcbbbed7434303f30f2cf33.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0663 — `research/refinement/configs/comparison-control.json`

- Type: json_artifact; bytes: 213; SHA-256: `64b02c478c792b3a6ab72001b3daa539cf578e33adfd256b911c0d5049f06e6f`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/64b02c478c792b3a6ab72001b3daa539cf578e33adfd256b911c0d5049f06e6f.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0664 — `research/refinement/configs/comparison-human.json`

- Type: json_artifact; bytes: 312; SHA-256: `23c59932ae05b77fd34ef4f8e3bf2a6899c6c6ad8fec1bc20f5cfd55c85e061d`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/23c59932ae05b77fd34ef4f8e3bf2a6899c6c6ad8fec1bc20f5cfd55c85e061d.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0665 — `research/refinement/configs/depth-12.json`

- Type: json_artifact; bytes: 315; SHA-256: `8f22bd694857e5644a97a12822a5a796d3021afe629e62d6837211d7b84a3f49`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/8f22bd694857e5644a97a12822a5a796d3021afe629e62d6837211d7b84a3f49.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0666 — `research/refinement/configs/depth-16.json`

- Type: json_artifact; bytes: 315; SHA-256: `53f372ada98bb09c633ab219371fb96ead61acaf9d8fdce5accbaacece9b5624`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/53f372ada98bb09c633ab219371fb96ead61acaf9d8fdce5accbaacece9b5624.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0667 — `research/refinement/configs/depth-18.json`

- Type: json_artifact; bytes: 339; SHA-256: `45669e9b560c1baea0cdafcb159e3a96a523a84464be2e1cbec40c9535d89601`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/45669e9b560c1baea0cdafcb159e3a96a523a84464be2e1cbec40c9535d89601.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0668 — `research/refinement/configs/depth-22.json`

- Type: json_artifact; bytes: 339; SHA-256: `ca28baa1df111d30a7adaa84181004146659bba9ff45edb0397b02b9f430477c`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/ca28baa1df111d30a7adaa84181004146659bba9ff45edb0397b02b9f430477c.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0669 — `research/refinement/configs/embedded-human-pvtrees.json`

- Type: json_artifact; bytes: 389; SHA-256: `59c5daea5e0b73c8849c3851a9852e15890db2677adbe6bc04986e53ebe65740`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/59c5daea5e0b73c8849c3851a9852e15890db2677adbe6bc04986e53ebe65740.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0670 — `research/refinement/configs/followup-hash128-softfalse.json`

- Type: json_artifact; bytes: 150; SHA-256: `fe1d885bacc290248153731ba1da5dc75ba506d6fc22598047f313f6b245f5d5`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/fe1d885bacc290248153731ba1da5dc75ba506d6fc22598047f313f6b245f5d5.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0671 — `research/refinement/configs/followup-hash128-softtrue.json`

- Type: json_artifact; bytes: 148; SHA-256: `153c4d7e52cd36e141d65d6cd5a8ea2fb6314127e17fd8645d0942fe091409a7`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/153c4d7e52cd36e141d65d6cd5a8ea2fb6314127e17fd8645d0942fe091409a7.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0672 — `research/refinement/configs/followup-hash32-softfalse.json`

- Type: json_artifact; bytes: 148; SHA-256: `502ee1cd639f79799f1e82c1609271236e6bf4f2f29fdc39762ba4f29a2c342d`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/502ee1cd639f79799f1e82c1609271236e6bf4f2f29fdc39762ba4f29a2c342d.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0673 — `research/refinement/configs/followup-hash32-softtrue.json`

- Type: json_artifact; bytes: 146; SHA-256: `273a93c4aaf96bdbd56d1203f256159056bc3011e3cffdf2b9e663155a174e9a`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/273a93c4aaf96bdbd56d1203f256159056bc3011e3cffdf2b9e663155a174e9a.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0674 — `research/refinement/configs/followup-hash64-repeat.json`

- Type: json_artifact; bytes: 118; SHA-256: `cafe6334b2119c003b595cc7745c11d8d9118ab4af5a60cb6dfaa548f65d2977`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/cafe6334b2119c003b595cc7745c11d8d9118ab4af5a60cb6dfaa548f65d2977.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0675 — `research/refinement/configs/followup-hash64-softfalse.json`

- Type: json_artifact; bytes: 148; SHA-256: `0b7623d739451d5051acc9ac61031b4641595aec386d51ab30b4a738999d08f7`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/0b7623d739451d5051acc9ac61031b4641595aec386d51ab30b4a738999d08f7.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0676 — `research/refinement/configs/followup-hash64-softtrue.json`

- Type: json_artifact; bytes: 146; SHA-256: `728ef760c30900a710c8e3984c943ef0ef40831bf0de8e6fe235c5aa0fab00fb`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/728ef760c30900a710c8e3984c943ef0ef40831bf0de8e6fe235c5aa0fab00fb.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0677 — `research/refinement/configs/followup-soft-factor200.json`

- Type: json_artifact; bytes: 160; SHA-256: `ffbc6ee74324f5f01835c4637b07ee337a9db742c9e7b6b30bf48a8bd7ba6e79`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/ffbc6ee74324f5f01835c4637b07ee337a9db742c9e7b6b30bf48a8bd7ba6e79.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0678 — `research/refinement/configs/followup-soft-factor50.json`

- Type: json_artifact; bytes: 158; SHA-256: `29492cfdb25929f164f006ba9f7bd7a0c0eaa53bc0ce02e3b568c15620e3f60a`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/29492cfdb25929f164f006ba9f7bd7a0c0eaa53bc0ce02e3b568c15620e3f60a.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0679 — `research/refinement/configs/nodes-150000.json`

- Type: json_artifact; bytes: 327; SHA-256: `31622dc830d6b7e0b8881154e38fa26e62ff0e1f4e05914b8e7562eda95da78c`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/31622dc830d6b7e0b8881154e38fa26e62ff0e1f4e05914b8e7562eda95da78c.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0680 — `research/refinement/configs/nodes-300000.json`

- Type: json_artifact; bytes: 327; SHA-256: `92667900f9c7f40cd34cc506a620aae6faf7a39ae0f38c24a00376e1a0852a81`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/92667900f9c7f40cd34cc506a620aae6faf7a39ae0f38c24a00376e1a0852a81.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0681 — `research/refinement/configs/nodes-40000.json`

- Type: json_artifact; bytes: 324; SHA-256: `a8fd788fb8ac2a720a9dc13eb4f8b1780d6a298ec5b22ab06a31f59450c9c0c7`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/a8fd788fb8ac2a720a9dc13eb4f8b1780d6a298ec5b22ab06a31f59450c9c0c7.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0682 — `research/refinement/configs/nodes-600000.json`

- Type: json_artifact; bytes: 327; SHA-256: `ad455442a1f966b488bbf24adf3e4ebacb4e5cd16e45365aa11371cccb3af4e0`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/ad455442a1f966b488bbf24adf3e4ebacb4e5cd16e45365aa11371cccb3af4e0.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0683 — `research/refinement/configs/normalized-ClearBetweenSearches-true.json`

- Type: json_artifact; bytes: 128; SHA-256: `1ae842821cea9840ac59424ffa240f0f0b0ed62241fed34acdcf8ee4b31376de`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/1ae842821cea9840ac59424ffa240f0f0b0ed62241fed34acdcf8ee4b31376de.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0684 — `research/refinement/configs/normalized-HardSoftNodeFactor-200.json`

- Type: json_artifact; bytes: 122; SHA-256: `8e23f2f714ac199c87d5535962f95e3409d3751257c8f930e54234a43aac3530`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/8e23f2f714ac199c87d5535962f95e3409d3751257c8f930e54234a43aac3530.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0685 — `research/refinement/configs/normalized-HardSoftNodeFactor-50.json`

- Type: json_artifact; bytes: 120; SHA-256: `9fee5fa9366d7d68a33be95b0fb1f3275466cfb3e5b6ee099bba8de8c2c77a7c`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/9fee5fa9366d7d68a33be95b0fb1f3275466cfb3e5b6ee099bba8de8c2c77a7c.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0686 — `research/refinement/configs/normalized-Hash-64.json`

- Type: json_artifact; bytes: 92; SHA-256: `3560f6d08f2df6dcac4e0bed96b6210240762e411d26e12b74741c3f3107b8f4`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/3560f6d08f2df6dcac4e0bed96b6210240762e411d26e12b74741c3f3107b8f4.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0687 — `research/refinement/configs/normalized-Minimal-true.json`

- Type: json_artifact; bytes: 102; SHA-256: `cb433ab51fd591e85e82fd0ea9b554b27b0cc3b0e9818c92e84ceb5b7df648eb`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/cb433ab51fd591e85e82fd0ea9b554b27b0cc3b0e9818c92e84ceb5b7df648eb.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0688 — `research/refinement/configs/normalized-NodeFudging-100.json`

- Type: json_artifact; bytes: 108; SHA-256: `ea40d261ea5ef3bd71ed02a8965c90b89324b26be6df665804299f04074b19c9`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/ea40d261ea5ef3bd71ed02a8965c90b89324b26be6df665804299f04074b19c9.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0689 — `research/refinement/configs/normalized-NodeFudging-1000.json`

- Type: json_artifact; bytes: 110; SHA-256: `c67f541c0f8001a77f7b424e3eed6ed0ce60067660a9b270298558b5ac658a46`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/c67f541c0f8001a77f7b424e3eed6ed0ce60067660a9b270298558b5ac658a46.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0690 — `research/refinement/configs/normalized-UseSoftNodes-true.json`

- Type: json_artifact; bytes: 112; SHA-256: `66c3239c233a78d2795141ea7bf8d85c79f8e8f0032dfdddc43a69285e02cf8e`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/66c3239c233a78d2795141ea7bf8d85c79f8e8f0032dfdddc43a69285e02cf8e.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0691 — `research/refinement/configs/normalized-class-v2.json`

- Type: json_artifact; bytes: 133; SHA-256: `3038aad8f34bfc8a1732ae27c9b0aadd37715ab2cb15bbe4a7b8b60e1610f533`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/3038aad8f34bfc8a1732ae27c9b0aadd37715ab2cb15bbe4a7b8b60e1610f533.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0692 — `research/refinement/configs/normalized-evaluate-normal.json`

- Type: json_artifact; bytes: 220; SHA-256: `7b7c826974e89eba0f5282ff2521bc9eb872be9447b5ca199452be3c45339328`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/7b7c826974e89eba0f5282ff2521bc9eb872be9447b5ca199452be3c45339328.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0693 — `research/refinement/configs/normalized-human-no-maia.json`

- Type: json_artifact; bytes: 382; SHA-256: `30156287ccc8418f92ff9e48783ae116d6fa4adc87c0cc7b14b8652b38e5ba4f`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/30156287ccc8418f92ff9e48783ae116d6fa4adc87c0cc7b14b8652b38e5ba4f.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0694 — `research/refinement/configs/normalized-human.json`

- Type: json_artifact; bytes: 357; SHA-256: `c0e33205eab382b29af3c0d6399e8f198839f5636c2a2a76ae7fa0ae23ff518f`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/c0e33205eab382b29af3c0d6399e8f198839f5636c2a2a76ae7fa0ae23ff518f.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0695 — `research/refinement/configs/normalized-nodes-300000.json`

- Type: json_artifact; bytes: 435; SHA-256: `90e1c198a668bfe5518d4b700fed666cf3393e75418857707e107d1240c9db8b`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/90e1c198a668bfe5518d4b700fed666cf3393e75418857707e107d1240c9db8b.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0696 — `research/refinement/configs/normalized-nodes-40000.json`

- Type: json_artifact; bytes: 433; SHA-256: `fe8ceb0c83ab246178adab8fb9ead76080b68039b012a91c6077397e5c008c84`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/fe8ceb0c83ab246178adab8fb9ead76080b68039b012a91c6077397e5c008c84.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0697 — `research/refinement/configs/normalized-nodes-600000.json`

- Type: json_artifact; bytes: 435; SHA-256: `2e08d990afc1c80a0e63589fe5eeccd9bbbe31c0353975ec7f01382341937b0e`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/2e08d990afc1c80a0e63589fe5eeccd9bbbe31c0353975ec7f01382341937b0e.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0698 — `research/refinement/configs/normalized-nodes-75000.json`

- Type: json_artifact; bytes: 433; SHA-256: `eca1c041e4291afc307003f0077085e60836b8a5a18116deb1d9b089d55b2aab`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/eca1c041e4291afc307003f0077085e60836b8a5a18116deb1d9b089d55b2aab.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0699 — `research/refinement/configs/normalized-repeat-1.json`

- Type: json_artifact; bytes: 99; SHA-256: `57a47be47c456a3f8f3c732dc7b83a8b505fe96aefce058f08e8c67758a8c08e`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/57a47be47c456a3f8f3c732dc7b83a8b505fe96aefce058f08e8c67758a8c08e.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.

## SRC-0700 — `research/refinement/configs/normalized-repeat-2.json`

- Type: json_artifact; bytes: 77; SHA-256: `9a973c8d2aecbc532748fb433ff946cc1140745093eeb17e20cad76cd3e7fa70`.
- Purpose: Experiment input; configuration existence is NOT proof the trial completed.
- Reviewed: full content processed; method: full text read; URL and reference scan; type-specific structured extraction.
- Semantic review: partial unless a structured type or explicitly reviewed document.
- Main topics: No separately extracted finding; see preserved evidence.
- Findings: 0; types: {}.
- URL/reference count: 0.
- Incorporated: True.
- [Preserved evidence](../evidence/text/9a973c8d2aecbc532748fb433ff946cc1140745093eeb17e20cad76cd3e7fa70.json) (privacy-redacted where needed).
- Cross-references: None extracted.
- Limits / potential missing sections: Static artifacts do not verify current deployed behavior.
- Accounting: Full content scan, URL/reference extraction where present, checksum/evidence preservation. No standalone finding extracted; not proof it contains no further semantics.
