# Extended findings

[Master index](../chapters/00_MASTER_INDEX.md)

<a id="FND-30000"></a>
## FND-30000 — PHP — Backend language

PHP is strongly indicated for the main website. The fpm label is infrastructure naming evidence,not direct process inspection; CEAC analysis service language remains unknown.

- Category: technology_stack
- Classification/confidence: STRONGLY INDICATED
- Verification: qualified inference / external historical report
- Sources: SRC-3005, SRC-3024
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
Public job posting explicitly requests PHP/Symfony; live public response pool label k8s-prod-fpm-catch-all.
```

<a id="FND-30001"></a>
## FND-30001 — Symfony — Backend framework

Symfony-based web tier historically documented and supported by client routing artifacts; no exact deployed Symfony version or controller source retrieved.

- Category: technology_stack
- Classification/confidence: STRONGLY INDICATED
- Verification: qualified inference / external historical report
- Sources: SRC-3005, SRC-0090
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
PHP job advert names Symfony; saved route token/default/requirement/host tables follow Symfony routing conventions.
```

<a id="FND-30002"></a>
## FND-30002 — MySQL / Cloud SQL Enterprise Plus — Database

Confirmed publicly reported use of MySQL and Cloud SQL Enterprise Plus,not an inspection of a live database. Article specifically discusses settings and other persisted domains; no endpoint-to-cluster mapping.

- Category: technology_stack
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3001, SRC-3003
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
2024-03-11 Google Cloud article authored by Chess.com principal engineer: migration to Cloud SQL for MySQL Enterprise Plus; independent MySQL customer page.
```

<a id="FND-30003"></a>
## FND-30003 — ScyllaDB — Data systems

Confirmed use reported in the 2024 engineering article. Exact current versions,schemas,keys,ownership and service assignment remain unknown.

- Category: technology_stack
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3001
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
Google Cloud article explicitly lists MySQL,ScyllaDB,Elasticsearch and Redis among operational databases.
```

<a id="FND-30004"></a>
## FND-30004 — Elasticsearch — Data systems

Confirmed use reported in the 2024 engineering article. Exact current versions,schemas,keys,ownership and service assignment remain unknown.

- Category: technology_stack
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3001
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
Google Cloud article explicitly lists MySQL,ScyllaDB,Elasticsearch and Redis among operational databases.
```

<a id="FND-30005"></a>
## FND-30005 — Redis — Data systems

Confirmed use reported in the 2024 engineering article. Exact current versions,schemas,keys,ownership and service assignment remain unknown.

- Category: technology_stack
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3001
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
Google Cloud article explicitly lists MySQL,ScyllaDB,Elasticsearch and Redis among operational databases.
```

<a id="FND-30006"></a>
## FND-30006 — Doctrine — ORM / data access

Historically advertised stack; no composer.lock,entity mapping,Doctrine connection config or server source available. Do not assert all current services use Doctrine.

- Category: technology_stack
- Classification/confidence: PROBABLE
- Verification: qualified inference / external historical report
- Sources: SRC-3005
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
Expired PHP backend job posting names Doctrine.
```

<a id="FND-30007"></a>
## FND-30007 — Vue — Frontend

Saved analysis/play bundles contain these client implementation indicators. Product/page-specific and historical; exact major versions need literal package metadata. Vue and Svelte-related compiled code can coexist.

- Category: technology_stack
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0090
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
Vue compiled __name,__vccOpts declarations and versioned vendor imports
```

<a id="FND-30008"></a>
## FND-30008 — Pinia — Frontend

Saved analysis/play bundles contain these client implementation indicators. Product/page-specific and historical; exact major versions need literal package metadata. Vue and Svelte-related compiled code can coexist.

- Category: technology_stack
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0090
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
Pinia imports and createPinia usage
```

<a id="FND-30009"></a>
## FND-30009 — Svelte runtime — Frontend

Saved analysis/play bundles contain these client implementation indicators. Product/page-specific and historical; exact major versions need literal package metadata. Vue and Svelte-related compiled code can coexist.

- Category: technology_stack
- Classification/confidence: STRONGLY INDICATED
- Verification: qualified inference / external historical report
- Sources: SRC-0090
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
svelte-related style/runtime markers and compiled component lifecycle helpers
```

<a id="FND-30010"></a>
## FND-30010 — Custom cc-* components — UI framework

Compiled component declarations and current design-system stylesheet establish a custom shared component layer; the inventory is declaration-level,not a complete runtime tree.

- Category: technology_stack
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0090
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
367 recovered implementation declarations/references across stored code; cc-button,cc-icon,cc-avatar,cc-select,cc-tooltip among literal names.
```

<a id="FND-30011"></a>
## FND-30011 — Custom design system; no generic framework established — CSS framework

Custom CSS is directly observed. Bootstrap,Tailwind and Material UI are not established by this batch; absence of recognized markers is not proof of absence.

- Category: technology_stack
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3011
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
Four fetched named stylesheets; custom --color/--font/--motion tokens and cc-* selectors.
```

<a id="FND-30012"></a>
## FND-30012 — JavaScript and compiled modular bundles — JavaScript

Delivered JavaScript is direct evidence; TypeScript authoring is probable from ecosystem/compiled patterns,not proven for every module.

- Category: technology_stack
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0090
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
Existing source files,ES imports,workers,dynamic chunk names and package paths.
```

<a id="FND-30013"></a>
## FND-30013 — Hybrid multi-page/client-component frontend — Architecture pattern

Not a single uniform SPA. Server-rendered shell plus client-rendered applications is supported; exact SSR framework/template engine unknown.

- Category: technology_stack
- Classification/confidence: STRONGLY INDICATED
- Verification: qualified inference / external historical report
- Sources: SRC-0090, SRC-0781, SRC-3024
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
Saved pages contain server-provided HTML/bootstrap data and import page-specific client packages; reactive components update analysis state.
```

<a id="FND-30014"></a>
## FND-30014 — Separate web / analysis / verification service boundaries — Backend architecture

Observable API boundaries,not proof of a specific Kubernetes pod count,microservice source organization,controller class tree or one service per protocol.

- Category: technology_stack
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0090
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
Game Review WebSocket host,run-search variants,BrilliantVerification RPC definitions and main web routes.
```

<a id="FND-30015"></a>
## FND-30015 — Cloudflare edge — Web server / edge

Observed edge response; origin web server may differ and is not exposed by Server header. Apache,Nginx,IIS unknown.

- Category: technology_stack
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3024, SRC-3025
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
New public responses: Server:cloudflare,CF-RAY,cf-cache-status,Cloudflare NEL report host.
```

<a id="FND-30016"></a>
## FND-30016 — FPM-named Kubernetes web pool — Application runtime

Strong naming evidence for Kubernetes/FPM web path. Exact PHP version,container image,orchestration topology and ingress implementation unknown.

- Category: technology_stack
- Classification/confidence: STRONGLY INDICATED
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
X-Chesscom-Server-Pool and X-Chesscom-Ingress-Pool: k8s-prod-fpm-catch-all.
```

<a id="FND-30017"></a>
## FND-30017 — Google Cloud multi-region database deployment — Hosting

Confirmed published deployment at article date; not proof every service or asset origin lives in Google Cloud.

- Category: technology_stack
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3001
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
Google Cloud engineering article describes databases in several regions and Cloud SQL migration.
```

<a id="FND-30018"></a>
## FND-30018 — Vite-style asset pipeline / hashed client packages — Build system

Observed output conventions. Rolldown-related wrappers appear in some packages but exact full build pipeline and all tool versions unknown.

- Category: technology_stack
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0090, SRC-3024
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
/bundles/app/vite/ stylesheets,/r2/client-packages/<page>/<version>/ imports and hashed chunks.
```

<a id="FND-30019"></a>
## FND-30019 — Emscripten-style C/C++ toolchain — WASM compiler

Generated runtime fingerprint strongly supports Emscripten/LLVM-family C/C++ compilation. No name,producers or DWARF custom sections in the five binaries; exact compiler/toolchain versions unknown.

- Category: technology_stack
- Classification/confidence: STRONGLY INDICATED
- Verification: qualified inference / external historical report
- Sources: SRC-0031
- Alternatives: Different products/services may use other stacks; no exclusive platform-wide claim.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

```text
Module.ccall,HEAPU8,embind,Asyncify,env.invoke_*,C++ exception imports and native .cc/.cpp strings.
```

<a id="FND-30020"></a>
## FND-30020 — C# / ASP.NET / ASP.NET Core / MVC / Web Forms / Razor Pages remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30021"></a>
## FND-30021 — Node.js / Express / NestJS remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30022"></a>
## FND-30022 — Python / Django / Flask / FastAPI remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30023"></a>
## FND-30023 — Java / Spring / Spring Boot / Jakarta EE remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30024"></a>
## FND-30024 — Ruby / Rails remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30025"></a>
## FND-30025 — Go / other service languages remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30026"></a>
## FND-30026 — Laravel remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30027"></a>
## FND-30027 — CodeIgniter / CakePHP / Yii remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30028"></a>
## FND-30028 — WordPress / Drupal / Joomla remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30029"></a>
## FND-30029 — MariaDB remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30030"></a>
## FND-30030 — Microsoft SQL Server remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30031"></a>
## FND-30031 — PostgreSQL remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30032"></a>
## FND-30032 — SQLite remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30033"></a>
## FND-30033 — Oracle remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30034"></a>
## FND-30034 — MongoDB remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30035"></a>
## FND-30035 — Entity Framework remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30036"></a>
## FND-30036 — Eloquent remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30037"></a>
## FND-30037 — Hibernate remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30038"></a>
## FND-30038 — Sequelize / Prisma remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30039"></a>
## FND-30039 — SQLAlchemy / Django ORM remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30040"></a>
## FND-30040 — Active Record / raw SQL / custom DAL remains unconfirmed

Alternative investigated; no sufficient direct service-specific evidence. This is an unknown,not a finding that the technology is absent.

- Category: technology_alternatives
- Classification/confidence: UNKNOWN
- Verification: qualified inference / external historical report
- Sources: SRC-3024
- Alternatives: Technology could be used by services not visible in the inspected assets.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records

<a id="FND-30041"></a>
## FND-30041 — Public response matched route web_jobs

https://www.chess.com/jobs returned200with matched route metadata. No controller method/class or DB query captured.

- Category: routing
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3024
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Physical controller,PHPmethod,authorization middleware and downstream query remain unknown.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../audit-metadata/public-request-log.json)

```text
{"Date": "Sun, 15 Nov 2026 12:25:42 GMT", "Content-Type": "text/html; charset=UTF-8", "Transfer-Encoding": "chunked", "Connection": "close", "Nel": "{\"report_to\":\"cf-nel\",\"success_fraction\":1.0,\"max_age\":604800}", "Report-To": "{\"group\":\"cf-nel\",\"max_age\":604800,\"endpoints\":[{\"url\":\"https://a.nel.cloudflare.com/report/v4?s=p39j%2BjXy%2B9%2F2vv9iJaf%2BFuZHHDjKGxb1iV8Av1a9rIkOwPvnAVMVyKgdP5GZrrw9%2BZUqG0VoKxNJNvrNTc0ziemwVXAWWLFdMic0WLmM4QeStGxY9LUSNNfIK%2F613vFMsRXVEXUvmxHnx6OIXmxfZjhQWZ%2Bl9yen%2BqZeDyLKDR4I88lZii3LIGKP%2FfQa\"}]}", "Cache-Control": "max-age=0, must-revalidate, private", "X-Content-Type-Options": "nosniff", "X-Chesscom-Version": "20261113125220", "X-Chesscom-Matched": "web_jobs", "X-Chesscom-Server-Pool": "k8s-prod-fpm-catch-all", "X-Chesscom-Request-Id-Lb": "a9d18b08db76717f152331e14043fed2", "X-Chesscom-Request-Id-Cdn": "a5ae3d74ae515719-IAD", "X-Frame-Options": "SAMEORIGIN", "Content-Security-Policy": "frame-ancestors 'self'", "Cross-Origin-Opener-Policy": "same-origin-allow-popups", "Expires": "Sun, 15 Nov 2026 12:25:42 GMT", "Strict-Transport-Security": "max-age=31536000; includeSubDomains", "X-Chesscom-Ingress-Pool": "k8s-prod-fpm-catch-all", "cf-cache-status": "DYNAMIC", "Set-Cookie": "[VALUE OMITTED]", "set-cookie": "[VALUE OMITTED]", "Server": "cloudflare", "CF-RAY": "a5ae3d74ae515719-SEA", "alt-svc": "h3=\":443\"; ma=86400"}
```

<a id="FND-30042"></a>
## FND-30042 — Public response matched route web_index

https://www.chess.com/ returned200with matched route metadata. No controller method/class or DB query captured.

- Category: routing
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3024
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Physical controller,PHPmethod,authorization middleware and downstream query remain unknown.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../audit-metadata/public-request-log.json)

```text
{"Date": "Sun, 15 Nov 2026 12:25:42 GMT", "Content-Type": "text/html; charset=UTF-8", "Transfer-Encoding": "chunked", "Connection": "close", "Nel": "{\"report_to\":\"cf-nel\",\"success_fraction\":1.0,\"max_age\":604800}", "Report-To": "{\"group\":\"cf-nel\",\"max_age\":604800,\"endpoints\":[{\"url\":\"https://a.nel.cloudflare.com/report/v4?s=7XD0B056baf2u8LWXZv%2BdUseVRY8HwGAtYopvmW5HP%2FutxckB9j2LkB7c2du4qwi63uYHPoaOYkegcg6yOY0%2Bmvvs3wzcJWVgMfl5SljKnfWTOM8ejoZUUSBKd0QMhr%2BSZZZ9SgnbeHJDhFmksLeyUJVRyF4FZTWP8%2F2YfldO157YeZ0YUzwBPu0ZKUN\"}]}", "Cache-Control": "max-age=0, must-revalidate, private", "X-Content-Type-Options": "nosniff", "X-Chesscom-Version": "20261113125220", "X-Chesscom-Matched": "web_index", "X-Chesscom-Server-Pool": "k8s-prod-fpm-catch-all", "X-Chesscom-Request-Id-Lb": "8dbe72b5e8e9c0838e2096b7b155842b", "X-Chesscom-Request-Id-Cdn": "a5ae3d76bd791f63-IAD", "X-Frame-Options": "SAMEORIGIN", "Content-Security-Policy": "frame-ancestors 'self'", "Cross-Origin-Opener-Policy": "same-origin-allow-popups", "Expires": "Sun, 15 Nov 2026 12:25:42 GMT", "Strict-Transport-Security": "max-age=31536000; includeSubDomains", "X-Chesscom-Ingress-Pool": "k8s-prod-fpm-catch-all", "cf-cache-status": "DYNAMIC", "Set-Cookie": "[VALUE OMITTED]", "set-cookie": "[VALUE OMITTED]", "Server": "cloudflare", "CF-RAY": "a5ae3d76bd791f63-SEA", "alt-svc": "h3=\":443\"; ma=86400"}
```

<a id="FND-30043"></a>
## FND-30043 — Public response security headers

Two newly fetched unauthenticated HTML responses carry HSTSmax-age31536000/includeSubDomains,X-Content-Type-Options:nosniff,X-Frame-Options:SAMEORIGIN,CSPframe-ancestors self,andCOOPsame-origin-allow-popups. These are per-response observations,not all-site policy guarantees.

- Category: security
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3024
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: No authenticated session,CORS credential flow,CSRF processing,rate-limit test or full cookie attributes preserved. No CSP-script-src policy inferred from frame-ancestors alone.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../audit-metadata/public-request-log.json)

```text
See PUBLIC-004 and PUBLIC-005 response header objects.
```

<a id="FND-30044"></a>
## FND-30044 — Reported clock/date conflict retained

System/session date is2026-11-13 while public Date headers report2026-11-15 and historical artifacts include later timestamps. Preserve original raw labels; do not use this discrepancy to invent chronology or assert current deploy age.

- Category: provenance
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-3024
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Current authenticated cloud behavior and unobserved branches are not established.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../audit-metadata/public-request-log.json)

```text
Date headers and source labels retained; new verification is labelled by batch,not silently normalized.
```

<a id="FND-30045"></a>
## FND-30045 — Implementation component game-list

Vue compiled component __name declaration. Name suggests game list; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
:vF}:{},introModalClient:_P,tabAnalysisCoachClient:SF,takeawaysClient:jF,trainCtaClient:FF}})),zF,BF=n((()=>{lf(),zF=W({__name:`game-list`,props:{selectedSelfAnalysis:{},selfAnalyses:{default:()=>[]}},emits:[`select-self-analysis`],setup(e){let t=e,n=L(()=>t.selfAnalyses.map(e=>({label:e.title,value:e.id})));return(t,r)=>e.selfAnalyses.length>1?(K(),B(`div`,{key:0,class:G(t.$style.component)},[U(Th,{name:`selectedSelfAnalysis`,size:`small`,class:G(t.$style.select),"model-value":e.selectedSelfAnalysis,options:n.value,"onUpdate:modelValue":r[0]||=e=>t.$emit(`select-self-analysis`,{id:e})},null,8,[`class`,`model-value`,`options`])],2)):z(``,!0)}})})),VF,HF,UF=n((()=>{BF(),BF(),LT(),x(),VF={$style:IT},HF=_(zF,[[`__cssModules`,VF]])})),WF,GF,KF=n((()=>{Xn(),re(),Bf(),WF=[`data-pane-id`],GF=W({__name:`advanced-pane`,props:{pane:{}},emits:[`request-close`,`request-drag`],setup(e,{emit:t}){let n=e,r=t;function i(e){e.stopPropagation(),r(`request-close`,n.pane.id)}function a(e){let t=e.target;e.button!==0||!(t instanceof Element)||t.closest(`button, a, input, select, textarea, [role="button"]`)||r(`request-drag`,n.pane.id,e)}return(t,n)=>(K(),B(`section`,{class:G([t.$style.component,{[t.$style[`height-fill`]]:
```

<a id="FND-30046"></a>
## FND-30046 — Implementation component advanced-pane

Vue compiled component __name declaration. Name suggests advanced pane; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
F(),LT(),x(),VF={$style:IT},HF=_(zF,[[`__cssModules`,VF]])})),WF,GF,KF=n((()=>{Xn(),re(),Bf(),WF=[`data-pane-id`],GF=W({__name:`advanced-pane`,props:{pane:{}},emits:[`request-close`,`request-drag`],setup(e,{emit:t}){let n=e,r=t;function i(e){e.stopPropagation(),r(`request-close`,n.pane.id)}function a(e){let t=e.target;e.button!==0||!(t instanceof Element)||t.closest(`button, a, input, select, textarea, [role="button"]`)||r(`request-drag`,n.pane.id,e)}return(t,n)=>(K(),B(`section`,{class:G([t.$style.component,{[t.$style[`height-fill`]]:e.pane.geometry.heightBehavior===`fill`,[t.$style[`height-engine-lines`]]:e.pane.geometry.heightBehavior===`engine-lines`}]),"data-pane-id":e.pane.id},[V(`header`,{class:G(t.$style.header),onPointerdown:a},[V(`div`,{class:G(t.$style[`header-leading`])},[U(f,{name:e.pane.icon,size:16,variant:`glyph`},null,8,[`name`]),n[0]||=H(),V(`h2`,{class:G(t.$style.title)},Hv(e.pane.title),3)],2),n[2]||=H(),V(`div`,{class:G(t.$style.actions)},[U(f,{is:J(Is),size:16,variant:`glyph`},null,8,[`is`]),n[1]||=H(),U(ga,{class:G(t.$style.close),size:`small`,variant:`subtle`,onClick:i},null,8,[`class`])],2)],34),n[3]||=H(),V(`div`,{class:G(t.$style.body)},[Bv(t.$slots,`default`,{},()=>[V(`span
```

<a id="FND-30047"></a>
## FND-30047 — Implementation component analysis-tool-rail

Vue compiled component __name declaration. Name suggests analysis tool rail; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
n((()=>{KF(),KF(),mE(),x(),qF={$style:pE},JF=_(GF,[[`__cssModules`,qF]])})),XF,ZF=n((()=>{XF=W({name:`AnalysisToolRail`,__name:`analysis-tool-rail`,setup(e){return(e,t)=>(K(),B(`div`,{class:G(e.$style.component),"aria-hidden":`true`},null,2))}})})),QF,$F,eI=n((()=>{ZF(),ZF(),_E(),x(),QF={$style:gE},$F=_(XF,[[`__cssModules`,QF]])})),tI,nI=n((()=>{tI=W({__name:`pane-drag-shell`,props:{height:{},isReturning:{type:Boolean},title:{},width:{},x:{},y:{}},setup(e){let t=e,n=L(()=>({height:`${t.height/10}rem`,transform:`translate3d(${t.x/10}rem, ${t.y/10}rem, 0)`,width:`${t.width/10}rem`}));return(t,r)=>(K(),R(Av,{to:`body`},[V(`div`,{class:G([t.$style.component,{[t.$style.returning]:e.isReturning}]),style:Pv(n.value),"aria-hidden":`true`},Hv(e.title),7)]))}})})),rI,iI,aI=n((()=>{nI(),nI(),xE(),x(),rI={$style:bE},iI=_(tI,[[`__cssModules`,rI]])})),oI,sI,cI=n((()=>{oI=[`aria-label`,`aria-orientation`,`aria-valuemax`,`aria-valuemin`,`aria-valuenow`],sI=W({__name:`pane-resize-handle`,props:{axis:{},paneSlot:{},value:{},minimum:{},maximum:{},label:{default:`Resize analysis panes`},keyboardStep:{default:16}},emits:[`resize`,`resize-start`,`resize-end`],setup(e,{emit:t}){let n=e,r=t,i=q(!1),a=q(null),o=0,s=L(()=>n.ax
```

<a id="FND-30048"></a>
## FND-30048 — Implementation component pane-drag-shell

Vue compiled component __name declaration. Name suggests pane drag shell; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
null,2))}})})),QF,$F,eI=n((()=>{ZF(),ZF(),_E(),x(),QF={$style:gE},$F=_(XF,[[`__cssModules`,QF]])})),tI,nI=n((()=>{tI=W({__name:`pane-drag-shell`,props:{height:{},isReturning:{type:Boolean},title:{},width:{},x:{},y:{}},setup(e){let t=e,n=L(()=>({height:`${t.height/10}rem`,transform:`translate3d(${t.x/10}rem, ${t.y/10}rem, 0)`,width:`${t.width/10}rem`}));return(t,r)=>(K(),R(Av,{to:`body`},[V(`div`,{class:G([t.$style.component,{[t.$style.returning]:e.isReturning}]),style:Pv(n.value),"aria-hidden":`true`},Hv(e.title),7)]))}})})),rI,iI,aI=n((()=>{nI(),nI(),xE(),x(),rI={$style:bE},iI=_(tI,[[`__cssModules`,rI]])})),oI,sI,cI=n((()=>{oI=[`aria-label`,`aria-orientation`,`aria-valuemax`,`aria-valuemin`,`aria-valuenow`],sI=W({__name:`pane-resize-handle`,props:{axis:{},paneSlot:{},value:{},minimum:{},maximum:{},label:{default:`Resize analysis panes`},keyboardStep:{default:16}},emits:[`resize`,`resize-start`,`resize-end`],setup(e,{emit:t}){let n=e,r=t,i=q(!1),a=q(null),o=0,s=L(()=>n.axis===`horizontal`?`vertical`:`horizontal`);function c(e){return n.axis===`horizontal`?e.clientX:e.clientY}function l(e){e.button===0&&(e.preventDefault(),a.value=e.pointerId,i.value=!0,o=c(e),e.currentTarget instanceof Element&&e.curr
```

<a id="FND-30049"></a>
## FND-30049 — Implementation component pane-resize-handle

Vue compiled component __name declaration. Name suggests pane resize handle; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
s`,rI]])})),oI,sI,cI=n((()=>{oI=[`aria-label`,`aria-orientation`,`aria-valuemax`,`aria-valuemin`,`aria-valuenow`],sI=W({__name:`pane-resize-handle`,props:{axis:{},paneSlot:{},value:{},minimum:{},maximum:{},label:{default:`Resize analysis panes`},keyboardStep:{default:16}},emits:[`resize`,`resize-start`,`resize-end`],setup(e,{emit:t}){let n=e,r=t,i=q(!1),a=q(null),o=0,s=L(()=>n.axis===`horizontal`?`vertical`:`horizontal`);function c(e){return n.axis===`horizontal`?e.clientX:e.clientY}function l(e){e.button===0&&(e.preventDefault(),a.value=e.pointerId,i.value=!0,o=c(e),e.currentTarget instanceof Element&&e.currentTarget.setPointerCapture(e.pointerId),r(`resize-start`))}function u(e){if(e.pointerId!==a.value)return;let t=c(e),n=t-o;o=t,n!==0&&r(`resize`,n)}function d(e){e.pointerId===a.value&&(e.currentTarget instanceof Element&&e.currentTarget.hasPointerCapture(e.pointerId)&&e.currentTarget.releasePointerCapture(e.pointerId),ee())}function ee(){i.value&&(a.value=null,i.value=!1,r(`resize-end`))}function te(e){let t=n.axis===`horizontal`?`ArrowLeft`:`ArrowUp`,i=n.axis===`horizontal`?`ArrowRight`:`ArrowDown`,a=null;e.key===t?a=-n.keyboardStep:e.key===i?a=n.keyboardStep:e.key===`Home`?a=n.minimum-n.value:e
```

<a id="FND-30050"></a>
## FND-30050 — Implementation component advanced-analysis-layout

Vue compiled component __name declaration. Name suggests advanced analysis layout; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ta-advanced-drop-pane`,`data-advanced-drop-slot`],XI=[`data-advanced-drop-pane`,`data-advanced-drop-slot`],ZI=100,QI=W({__name:`advanced-analysis-layout`,props:{layoutState:{default:fI}},emits:[`request-close`,`request-reopen`,`request-drag`,`update:layout-state`],setup(e,{emit:t}){let n=e,r=t,{layoutState:i,resizePanePair:a}=BI(n.layoutState),o=Gv(`stackElement`),s=Gv(`bottomRowElement`),c=q(0),l=q({}),u=.5,d=null;qv(()=>n.layoutState,e=>{i.value=e});let{activeDropTarget:ee,beginDrag:te,draggedPaneId:ne,dragPosition:re,isDragging:ie,isReturning:ae}=EI({layoutState:i,onLayoutChange(e){i.value=e,r(`update:layout-state`,e)}}),oe={"--advanced-sidebar-width":`500px`,"--advanced-board-companion-minimum-height":`88px`,"--advanced-pane-header-height":`40px`,"--advanced-pane-minimum-height":`220px`,"--advanced-pane-gap":`8px`},se=L(()=>i.value.order.map(e=>i.value.panes[e]).filter(e=>!e.isOpen)),ce=L(()=>[CD.Engine,CD.Analysis,CD.AddedGames].map(ge).filter(e=>!!e)),le=L(()=>[CD.BottomLeading,CD.BottomTrailing].map(ge).filter(e=>!!e)),ue=L(()=>le.value[0]?.geometry.widthPercent??0);function de(){let e=_e(),t=document.getElementById(`board-layout-chessboard`);if(!e||!t)return null;let n=window.getComputedStyle(
```

<a id="FND-30051"></a>
## FND-30051 — Implementation component cc-sidebar-header

Vue compiled component __name declaration. Name suggests cc sidebar header; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
label`],oL=[`disabled`,`aria-label`],sL=[`textContent`],cL=[`disabled`,`aria-label`],lL=[`disabled`,`aria-label`],uL=W({__name:`cc-sidebar-header`,props:{endIcon:{},endIconSecondary:{},featureIcon:{},hasBackButton:{type:Boolean},startIcon:{},startIconSecondary:{},transparent:{type:Boolean},title:{},variant:{default:`primary`}},emits:[`click-header-title`,`click-start`,`click-start-secondary`,`click-end`,`click-end-secondary`],setup(e){let{trans:t}=sm(),n=e,r=L(()=>n.hasBackButton?{icon:{is:Ra,variant:`glyph`},ariaLabel:t.Back,disabled:n.startIcon?.disabled,disabledTooltipText:n.startIcon?.disabledTooltipText}:n.startIcon),i=L(()=>n.variant===`tertiary`||n.variant===`secondary-flat`?`glyph`:`color`);return(t,n)=>(K(),B(`div`,{class:G([t.$style.component,t.$style[e.variant],{[t.$style.transparent]:e.transparent}])},[r.value?.icon||t.$slots[`icon-start`]||e.startIconSecondary?.icon||t.$slots[`icon-start-secondary`]?(K(),B(`div`,{key:0,class:G(t.$style[`header-start`])},[r.value?.icon||t.$slots[`icon-start`]?(K(),B(`button`,{key:0,type:`button`,disabled:r.value?.disabled,"aria-label":r.value?.ariaLabel,class:G([t.$style[`icon-start`],{[t.$style.disabled]:r.value?.disabled}]),onClick:n[0]||=e=>t.$emit(`cli
```

<a id="FND-30052"></a>
## FND-30052 — Implementation component sidebar-header

Vue compiled component __name declaration. Name suggests sidebar header; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),Wx(),x(),fL={$style:Ux},pL=_(uL,[[`__cssModules`,fL]])})),hL,gL=n((()=>{Xn(),iL(),ph(),Bf(),mL(),O_(),$s(),TD(),hL=W({__name:`sidebar-header`,props:{gameCollection:{},hasFavoriteGame:{type:Boolean},hasBackButton:{type:Boolean},isAnalysisTabCoachActive:{type:Boolean},isCoachAudioEnabled:{type:Boolean},isCoachAudioFeatureAvailable:{type:Boolean},isCoachAudioMutedByPlaySounds:{type:Boolean},isFavorite:{type:Boolean},isGameReview:{type:Boolean},isGameReviewOverview:{type:Boolean},isCollectionSettings:{type:Boolean},isMobile:{type:Boolean},layoutMode:{},titleText:{}},emits:[`click-back-button`,`click-collection-settings`,`click-settings`,`select-tab`,`toggle-advanced-layout`,`toggle-coach-speech`,`toggle-favorite`],setup(e,{emit:t}){let n=e,r=window.chesscom.features.includes(`analysis_advanced_layout`),i=t,a=L(()=>n.isFavorite?C(`Remove from Favorites`):C(`Add to Favorites`)),o=L(()=>{if(n.hasFavoriteGame)return{ariaLabel:a.value}}),s=L(()=>{if(!n.isMobile&&n.isGameReviewOverview)return o.value}),c=L(()=>{if(!(!(n.isGameReview||n.isAnalysisTabCoachActive)||!n.isCoachAudioFeatureAvailable))return{icon:{is:n.isCoachAudioEnabled?ni:qi,variant:`glyph`},ariaLabel:C(`Toggle Coach Audio`),disabled:n.isCoachAud
```

<a id="FND-30053"></a>
## FND-30053 — Implementation component board-tab-container

Vue compiled component __name declaration. Name suggests board tab container; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
((()=>{gL(),gL(),ME(),x(),_L={$style:jE},vL=_(hL,[[`__cssModules`,_L]])})),bL,xL=n((()=>{bL=W({name:`BoardTabContainer`,__name:`board-tab-container`,setup(e){return(e,t)=>(K(),B(`div`,{class:G(e.$style.component),role:`tablist`},[Bv(e.$slots,`default`)],2))}})})),SL,CL,wL=n((()=>{xL(),xL(),Mb(),x(),SL={$style:jb},CL=_(bL,[[`__cssModules`,SL]])})),TL,EL,DL=n((()=>{Bf(),TL=[`disabled`,`aria-selected`],EL=W({__name:`board-tab-item`,props:{disabled:{type:Boolean,default:!1},icon:{},showBadge:{type:Boolean,default:!1},isActive:{type:Boolean,default:!1},label:{}},emits:[`click`],setup(e,{emit:t}){let n=t;return(t,r)=>(K(),B(`button`,Nv(t.$attrs,{role:`tab`,type:`button`,disabled:e.disabled,"aria-selected":e.isActive?`true`:`false`,class:[t.$style.component,{[t.$style.active]:e.isActive}],onClick:r[0]||=e=>n(`click`,e)}),[U(f,{"aria-hidden":`true`,is:e.icon,variant:`glyph`,size:24,class:G(t.$style.icon)},null,8,[`is`,`class`]),r[1]||=H(),V(`span`,{class:G(t.$style.label)},Hv(e.label),3),r[2]||=H(),e.showBadge?Bv(t.$slots,`badge`,{},()=>[V(`span`,{class:G(t.$style.badge)},`*`,2)],void 0,0):z(``,!0)],16,TL))}})})),OL,kL,AL=n((()=>{DL(),DL(),zb(),x(),OL={$style:Rb},kL=_(EL,[[`__cssModules`,OL]])})),jL,ML=n((()=
```

<a id="FND-30054"></a>
## FND-30054 — Implementation component board-tab-item

Vue compiled component __name declaration. Name suggests board tab item; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
),Mb(),x(),SL={$style:jb},CL=_(bL,[[`__cssModules`,SL]])})),TL,EL,DL=n((()=>{Bf(),TL=[`disabled`,`aria-selected`],EL=W({__name:`board-tab-item`,props:{disabled:{type:Boolean,default:!1},icon:{},showBadge:{type:Boolean,default:!1},isActive:{type:Boolean,default:!1},label:{}},emits:[`click`],setup(e,{emit:t}){let n=t;return(t,r)=>(K(),B(`button`,Nv(t.$attrs,{role:`tab`,type:`button`,disabled:e.disabled,"aria-selected":e.isActive?`true`:`false`,class:[t.$style.component,{[t.$style.active]:e.isActive}],onClick:r[0]||=e=>n(`click`,e)}),[U(f,{"aria-hidden":`true`,is:e.icon,variant:`glyph`,size:24,class:G(t.$style.icon)},null,8,[`is`,`class`]),r[1]||=H(),V(`span`,{class:G(t.$style.label)},Hv(e.label),3),r[2]||=H(),e.showBadge?Bv(t.$slots,`badge`,{},()=>[V(`span`,{class:G(t.$style.badge)},`*`,2)],void 0,0):z(``,!0)],16,TL))}})})),OL,kL,AL=n((()=>{DL(),DL(),zb(),x(),OL={$style:Rb},kL=_(EL,[[`__cssModules`,OL]])})),jL,ML=n((()=>{wL(),AL(),j(),jL=W({name:`SidebarTabs`,__name:`sidebar-tabs`,props:{selectedTab:{},isSharedBoardEntryLocked:{type:Boolean},tabs:{}},emits:[`select-tab`],setup(e,{emit:t}){let n=e,r=t;function i(e){n.isSharedBoardEntryLocked&&e!==P.Tabs.Analysis||r(`select-tab`,{tab:e})}return(t,n)=>(K()
```

<a id="FND-30055"></a>
## FND-30055 — Implementation component sidebar-tabs

Vue compiled component __name declaration. Name suggests sidebar tabs; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
L(),DL(),zb(),x(),OL={$style:Rb},kL=_(EL,[[`__cssModules`,OL]])})),jL,ML=n((()=>{wL(),AL(),j(),jL=W({name:`SidebarTabs`,__name:`sidebar-tabs`,props:{selectedTab:{},isSharedBoardEntryLocked:{type:Boolean},tabs:{}},emits:[`select-tab`],setup(e,{emit:t}){let n=e,r=t;function i(e){n.isSharedBoardEntryLocked&&e!==P.Tabs.Analysis||r(`select-tab`,{tab:e})}return(t,n)=>(K(),R(CL,{class:G(t.$style.container)},{default:Jv(()=>[(K(!0),B(kv,null,zv(e.tabs,t=>(K(),R(kL,{key:t.key,icon:t.icon,"is-active":e.selectedTab===t.key,label:t.label,disabled:e.isSharedBoardEntryLocked&&t.key!==J(P).Tabs.Analysis,onClick:e=>i(t.key)},null,8,[`icon`,`is-active`,`label`,`disabled`,`onClick`]))),128))]),_:1},8,[`class`]))}})})),NL,PL,FL=n((()=>{ML(),ML(),zE(),x(),NL={$style:RE},PL=_(jL,[[`__cssModules`,NL]])})),IL,LL=n((()=>{ws(),IL=W({name:`SidebarLoader`,__name:`sidebar-loader`,setup(e){return(e,t)=>(K(),B(`div`,{class:G(e.$style.component)},[V(`div`,{class:G(e.$style.content)},[U(Sn,{"is-circle":!0,size:40})],2)],2))}})})),RL,zL,BL=n((()=>{LL(),LL(),IE(),x(),RL={$style:FE},zL=_(IL,[[`__cssModules`,RL]])})),VL,HL,UL=n((()=>{BL(),j(),A(),VL={[P.Tabs.Analysis]:Mv({loader:()=>O(()=>e(()=>import(`./tab-analysis.3e85b73f.BKvewUswZJ
```

<a id="FND-30056"></a>
## FND-30056 — Implementation component sidebar-loader

Vue compiled component __name declaration. Name suggests sidebar loader; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
(()=>{ML(),ML(),zE(),x(),NL={$style:RE},PL=_(jL,[[`__cssModules`,NL]])})),IL,LL=n((()=>{ws(),IL=W({name:`SidebarLoader`,__name:`sidebar-loader`,setup(e){return(e,t)=>(K(),B(`div`,{class:G(e.$style.component)},[V(`div`,{class:G(e.$style.content)},[U(Sn,{"is-circle":!0,size:40})],2)],2))}})})),RL,zL,BL=n((()=>{LL(),LL(),IE(),x(),RL={$style:FE},zL=_(IL,[[`__cssModules`,RL]])})),VL,HL,UL=n((()=>{BL(),j(),A(),VL={[P.Tabs.Analysis]:Mv({loader:()=>O(()=>e(()=>import(`./tab-analysis.3e85b73f.BKvewUswZJ.chunk.js`),`./tab-analysis.3e85b73f.BKvewUswZJ.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0,9,10,11]),import.meta.url),loadingComponent:zL}),[P.Tabs.Members]:Mv({loader:()=>O(()=>e(()=>import(`./tab-members.21cb9b32.BLq0rNYlKe.chunk.js`),`./tab-members.21cb9b32.BLq0rNYlKe.chunk.js`).then(e=>(e.t(),e.n)),__vite__mapDeps([0,12,13,14,15,9,16,17]),import.meta.url),loadingComponent:zL}),[P.Tabs.Explore]:Mv({loader:()=>O(()=>e(()=>import(`./shared.533ee0c1.EEu7uiiDnx.chunk.js`),`./shared.533ee0c1.EEu7uiiDnx.chunk.js`).then(e=>(e.t(),e.r)),__vite__mapDeps([0,12,13,18,19,15,5,10,20,21,22,23,14,24,25]),import.meta.url),loadingComponent:zL}),[P.Tabs.Review]:Mv({loader:()=>O(()=>e(()=>import(`./tab-review.88a71be6.G
```

<a id="FND-30057"></a>
## FND-30057 — Implementation component sidebar-view

Vue compiled component __name declaration. Name suggests sidebar view; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
a.url),loadingComponent:zL})})),WL,GL=n((()=>{zs(),$s(),nL(),dI(),yL(),FL(),VI(),TD(),UL(),j(),WL=W({name:`SidebarView`,__name:`sidebar-view`,props:{hasFavoriteGame:{type:Boolean},isAnalysisTabCoachActive:{type:Boolean},isCoachAudioEnabled:{type:Boolean},isCoachAudioFeatureAvailable:{type:Boolean},isCoachAudioMutedByPlaySounds:{type:Boolean},isCollectionSettingsThumbnail:{type:Boolean},isFavorite:{type:Boolean},isGameReviewOverview:{type:Boolean},isSkillsAnimating:{type:Boolean},selectedTab:{},showBackButton:{type:Boolean},showGameList:{type:Boolean},tabs:{},gameCollection:{},isBoardInitialized:{type:Boolean},isSelfAnalysisLoaded:{type:Boolean},isEmptyGameCollection:{type:Boolean},isSharedBoardEntryLocked:{type:Boolean}},emits:[`click-analysis-button`,`click-back-button`,`click-collection-settings`,`click-settings`,`select-tab`,`toggle-coach-audio`,`toggle-favorite`],setup(e){let t=e,n=L(()=>t.selectedTab===P.Tabs.Review),r=q(SD.Board),i=q(532),{closePane:a,layoutState:o,reopenPane:s}=BI(),c=L(()=>t.selectedTab===P.Tabs.CollectionSettings),l=L(()=>r.value===SD.Advanced&&!n.value&&!fa());qv(l,e=>{document.body.classList.toggle(`analysis-advanced-layout`,e),e?u():d()},{immediate:!0}),Fv(()=>{document.bo
```

<a id="FND-30058"></a>
## FND-30058 — Implementation component game-controls-primary

Vue compiled component __name declaration. Name suggests game controls primary; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
ction aR(){ku(th(ml,{}))}var oR=n((()=>{_r(),pd(),Kg()})),sR,cR=n((()=>{bv(),qd(),O_(),sR=W({name:`SidebarControlsMain`,__name:`game-controls-primary`,props:{controls:{},hasSecondaryControls:{type:Boolean}},setup(e,{emit:t}){let n=t,r=window.innerWidth<960,i=window,a=document.querySelector(`.board-sidebar`)||document.querySelector(`.board-layout-sidebar`)||document.querySelector(`.layout-sidebar`),o=Gv(`el`),s=Wv(),c=()=>{let e=a,t=o.value;if(!e||!t)return;let n=i?i.scrollTop:document.documentElement.scrollTop;window.innerHeight+n>e.offsetTop+e.getBoundingClientRect().height?(t.classList?.remove(s.float),Object.assign(document.body.style,{paddingBottom:null})):(t.classList?.add(s.float),Object.assign(document.body.style,{paddingBottom:`${t.offsetHeight}px`}))},l=Wo(c,500);return Iv(()=>{r&&(c(),(i||window).addEventListener(`scroll`,l))}),Lv(()=>{r&&(i||window).removeEventListener(`scroll`,l)}),(t,r)=>(K(),B(`div`,{ref_key:`el`,ref:o,class:G([J(s).component,{[J(s)[`has-secondary-controls`]]:e.hasSecondaryControls}])},[(K(!0),B(kv,null,zv(e.controls,e=>(K(),R(Gp,{key:e.tooltip,"full-width":``,size:`large`,disabled:!e.enabled(),"aria-label":e.tooltip,icon:e.icon.value?{is:e.icon.value,variant:`glyph`}:vo
```

<a id="FND-30059"></a>
## FND-30059 — Implementation component game-controls-more-menu

Vue compiled component __name declaration. Name suggests game controls more menu; precise props/events captured only in the adjacent source excerpt, not inferred globally. Declaration/import context, not a recovered complete runtime hierarchy.

- Category: ui_components
- Classification/confidence: CONFIRMED
- Verification: direct stored evidence reviewed
- Sources: SRC-0066
- Alternatives: No alternative to the exact stored declaration; its runtime applicability may differ.
- Remaining unknowns: Only preserved declaration context is established. Props/events/full render hierarchy and backend relationship require further per-component call-site review.
- Related findings: See related source/module/category records
- [Exact supporting artifact](../registries/components.json)

```text
idth(),window.addEventListener(`resize`,this.setSidebarWidth.bind(this)))}},mR=new Map})),gR,_R=n((()=>{Td(),ll(),gR=W({__name:`game-controls-more-menu`,props:{controls:{}},emits:[`close-more`,`click-menu-item`],setup(e,{emit:t}){let n=t,r=Gv(`menuMore`);Hc(r,()=>{n(`close-more`)});function i(e){n(`click-menu-item`,{value:e.event})}return(t,n)=>(K(),B(`div`,{ref_key:`menuMore`,ref:r,class:G(t.$style.component)},[(K(!0),B(kv,null,zv(e.controls,(e,t)=>(K(),R(hf,{key:t,icon:{is:e.icon,variant:`glyph`},label:e.tooltip(),"is-disabled":!e.enabled(),onClick:t=>i(e)},null,8,[`icon`,`label`,`is-disabled`,`onClick`]))),128))],2))}})})),vR,yR,bR=n((()=>{_R(),_R(),aw(),x(),vR={$style:iw},yR=_(gR,[[`__cssModules`,vR]])})),xR,SR=n((()=>{Xn(),qd(),Zh(),hR(),bR(),xR=W({__name:`game-controls-secondary`,props:{controls:{}},emits:[`click`],setup(e,{emit:t}){let n=t,r=q(!1),i=q(fR().width),a=window.context?.locale===`en_US`,o=Gv(`container`),s=L(()=>!a&&i.value<350),c=new ResizeObserver(()=>{i.value=fR().width});Iv(()=>{o.value&&c.observe(o.value)}),Fv(()=>{c.disconnect()});function l(e){n(`click`,{value:e.value})}function u(e){r.value=!1,l(e)}function d(){r.value||=!0}function ee(){setTimeout(()=>{r.value=!1})}return(t,
```
