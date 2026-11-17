# Database schema versus application/protocol models

[Master index](00_MASTER_INDEX.md)

## 1.Confirmed relational schema

**None recovered.** NoSQLDDL,migrations,table/column/index/constraint/foreign-key metadata or query logs available. NorealERdiagramcanbereconstructed.

## 2.Application-level models

Games,positions,moves,players,reviews,ratings,settings and skills appear in client logic/protocols. Theseareapplicationconcepts,notconfirmedMySQLtables.

## 3.Observed API/protobuf structures

NewGameRequest,GameReviewRequest,GameReviewResponse,GameReview,ColorAccuracy,MoveClassification,scores,playedLine,report-cardmetadata,speech fragments and audio hashes are preserved in the full schemas. Enumvaluesarescopedbynamespace. Protofieldnumbersarewiretags,notSQLcolumnIDs.

## 4.Suspected persistent entities

Thepublishedengineeringarticleconfirmsdatapersistenceindomains,butnoentity-to-tableorbackend-to-cluster join is proven. AnyconventionalUsers/Games/MovesERdiagramwouldbeinventedandisdeliberatelyomitted.

[Schema inventory](../history/prior-audit/registries/schemas.json) · [Explicit model-boundary diagram](../diagrams/06-data-model-boundary.mmd)

