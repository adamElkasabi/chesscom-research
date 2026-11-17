# Technology stack — evidence and alternatives

[Master index](00_MASTER_INDEX.md)

| Layer | Technology | Confidence | Evidence / scope |
| --- | --- | --- | --- |
| Backend language | PHP | STRONGLY INDICATED | Public job posting explicitly requests PHP/Symfony; live public response pool label k8s-prod-fpm-catch-all. |
| Backend framework | Symfony | STRONGLY INDICATED | PHP job advert names Symfony; saved route token/default/requirement/host tables follow Symfony routing conventions. |
| Database | MySQL / Cloud SQL Enterprise Plus | CONFIRMED | 2024-03-11 Google Cloud article authored by Chess.com principal engineer: migration to Cloud SQL for MySQL Enterprise Plus; independent MySQL customer page. |
| Data systems | ScyllaDB | CONFIRMED | Google Cloud article explicitly lists MySQL,ScyllaDB,Elasticsearch and Redis among operational databases. |
| Data systems | Elasticsearch | CONFIRMED | Google Cloud article explicitly lists MySQL,ScyllaDB,Elasticsearch and Redis among operational databases. |
| Data systems | Redis | CONFIRMED | Google Cloud article explicitly lists MySQL,ScyllaDB,Elasticsearch and Redis among operational databases. |
| ORM / data access | Doctrine | PROBABLE | Expired PHP backend job posting names Doctrine. |
| Frontend | Vue | CONFIRMED | Vue compiled __name,__vccOpts declarations and versioned vendor imports |
| Frontend | Pinia | CONFIRMED | Pinia imports and createPinia usage |
| Frontend | Svelte runtime | STRONGLY INDICATED | svelte-related style/runtime markers and compiled component lifecycle helpers |
| UI framework | Custom cc-* components | CONFIRMED | 367 recovered implementation declarations/references across stored code; cc-button,cc-icon,cc-avatar,cc-select,cc-tooltip among literal names. |
| CSS framework | Custom design system; no generic framework established | CONFIRMED | Four fetched named stylesheets; custom --color/--font/--motion tokens and cc-* selectors. |
| JavaScript | JavaScript and compiled modular bundles | CONFIRMED | Existing source files,ES imports,workers,dynamic chunk names and package paths. |
| Architecture pattern | Hybrid multi-page/client-component frontend | STRONGLY INDICATED | Saved pages contain server-provided HTML/bootstrap data and import page-specific client packages; reactive components update analysis state. |
| Backend architecture | Separate web / analysis / verification service boundaries | CONFIRMED | Game Review WebSocket host,run-search variants,BrilliantVerification RPC definitions and main web routes. |
| Web server / edge | Cloudflare edge | CONFIRMED | New public responses: Server:cloudflare,CF-RAY,cf-cache-status,Cloudflare NEL report host. |
| Application runtime | FPM-named Kubernetes web pool | STRONGLY INDICATED | X-Chesscom-Server-Pool and X-Chesscom-Ingress-Pool: k8s-prod-fpm-catch-all. |
| Hosting | Google Cloud multi-region database deployment | CONFIRMED | Google Cloud engineering article describes databases in several regions and Cloud SQL migration. |
| Build system | Vite-style asset pipeline / hashed client packages | CONFIRMED | /bundles/app/vite/ stylesheets,/r2/client-packages/<page>/<version>/ imports and hashed chunks. |
| WASM compiler | Emscripten-style C/C++ toolchain | STRONGLY INDICATED | Module.ccall,HEAPU8,embind,Asyncify,env.invoke_*,C++ exception imports and native .cc/.cpp strings. |

## Requested alternative technologies

| Area | Candidate | Assessment |
| --- | --- | --- |
| Backend alternatives | C# / ASP.NET / ASP.NET Core / MVC / Web Forms / Razor Pages | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| Backend alternatives | Node.js / Express / NestJS | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| Backend alternatives | Python / Django / Flask / FastAPI | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| Backend alternatives | Java / Spring / Spring Boot / Jakarta EE | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| Backend alternatives | Ruby / Rails | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| Backend alternatives | Go / other service languages | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| Other PHP frameworks | Laravel | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| Other PHP frameworks | CodeIgniter / CakePHP / Yii | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| Other PHP frameworks | WordPress / Drupal / Joomla | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| Database alternatives | MariaDB | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| Database alternatives | Microsoft SQL Server | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| Database alternatives | PostgreSQL | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| Database alternatives | SQLite | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| Database alternatives | Oracle | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| Database alternatives | MongoDB | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| ORM alternatives | Entity Framework | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| ORM alternatives | Eloquent | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| ORM alternatives | Hibernate | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| ORM alternatives | Sequelize / Prisma | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| ORM alternatives | SQLAlchemy / Django ORM | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |
| ORM alternatives | Active Record / raw SQL / custom DAL | UNKNOWN — No authoritative service-specific server config/source/driver/DB query evidence in available artifacts or the selected primary-source batch. Lexical hits are not installation proof. |

[Complete technology evidence and finding IDs](audit-metadata/technology-evidence.json)

Multiple job mirrors are not independent implementation probes. The selected posting is expired and historically scoped. PHPdoesnotimplyMySQL;MySQLhasindependentprimaryevidence. No SQLServer,PostgreSQL,MariaDB,Node,ASP.NET,Laravelorotherbackendabsenceisclaimed.
