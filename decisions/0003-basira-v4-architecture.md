---
id: 0003-basira-v4-architecture
title: ADR-0003 — Basira V4 Architecture & Build Decisions
type: decision
status: accepted
aliases: [basira-v4-architecture]
tags:
  - architecture
  - adr
  - basira
  - basira-v4
created: 2026-06-04
updated: 2026-06-04
supersedes:
superseded-by:
deciders: [ahmad, claude]
summary: >-
  Basira V4 is a clean rebuild — the humane-first operational layer of the CRPD community-integration project — after V1/V2/V3 proved hollow. Decisions: Next.js 16 full-stack + Prisma + Postgres; one process and one DB so the transactional write is the outbox; engines as pure lib functions built only on demand; settled مؤتمن/تعهد/open/AccessLog security; demo beneficiaries with real plug-in later; data residency deferred to the ministry.
related:
  - "[[basira-v4-rebuild]]"
  - "[[basira-v4-compass-and-anti-drift]]"
  - "[[0001-vault-architecture]]"
---

## Context

Three prior Basira codebases exist and all three are hollow. V1 and V2 carry real beneficiary data and some real logic but were never ministry-ready. V3 (at `C:\Users\aass1\Basira`) reached ~78k lines of code across roughly 30 sessions yet never produced a single verified cross-service loop. Two forces hollowed it. First, ceremony: a Turborepo monorepo plus NestJS plus BullMQ plus Redis plus Kafka-style plumbing whose weight outgrew the product. Second, security-classification drift — repeated cycles of field masking, سري/مقيد (secret/restricted) tiers, and a "security spine" that consumed sessions while the beneficiary-facing surface stayed empty. The celebrated بصيرة "engines" (predictive نبض, governance auto-CAPA, an SROI/triangulation index, خوارزمية الإحسان) were aspirational prose, never code. Ahmad's verdict, taken at face value: *"you cannot get back unless we do a V4."* This ADR records the rebuild decisions that came out of session S84 (2026-06-04) and the gather phase that fed it. The compass is fixed in [[basira-v4-compass-and-anti-drift]]: KNOW the human (functional + dignity + safety), SERVE him across services via cross-service impact triggers, break societal barriers — المستفيد أولًا (the beneficiary first); disability is social and functional, never a ceiling. The work is the operational layer of the ministry's existing CRPD-anchored مشروع الدمج المجتمعي (community-integration / de-institutionalization project), validated even by the ministry's own national report, which found the current system measures Outputs not Outcomes ("وهم الإنجاز", the illusion of achievement) and that the medical gateway (البوابة الطبية) forces a medical model — so V4 starts from "ما أهدافك؟" (what are your goals?), not "ما تشخيصك؟" (what is your diagnosis?). See [[basira-v4-rebuild]], [[social-handicap-compass]], and [[community-integration-project]].

## Decision

**1. Clean rebuild, not strangler.** V4 is a from-scratch build, not an incremental cut-over from V3. V3 is a parts-bin only — port the *logic* of the salvageable محرك مروءة (Muru'ah, burnout-aware staff matching) and محرك نبض (Nabd, abandonment/isolation early-warning), never their NestJS/Redis plumbing. V4 is positioned as the humane-first operational layer of the CRPD community-integration project, not a generic case-management app.

**2. Stack = Next.js 16 full-stack.** App Router plus React 19 plus TypeScript. Server actions are the home of the KNOW→SERVE triggers — a server action opens one transactional boundary over one database and writes both sides of a cross-service effect in a single ACID transaction. Route handlers under `app/api/*` are the external surface for the mobile/manager app, Seha (MoH medical record), and Civil Defense 997; a mobile client or a Seha webhook calls a route handler, the web UI calls a server action, and both run the same domain functions in `lib/`. There is no separate API service: a NestJS/Hono split would reintroduce the dual-write problem the monolith avoids for free. Persistence is Prisma plus Postgres, with SQLite for local development and Postgres for production PHI; the swap is one datasource line, schema identical across tiers. Styling is plain CSS on the HRSD palette, RTL Arabic (no Tailwind/UI-kit yet — flagged as a failure surface). Every server action and route handler re-checks the مؤتمن plus pledge inside itself; nothing trusts the caller.

**3. One process plus one DB — the transactional write IS the outbox.** Because there is a single process over a single database, a domain event and its cross-service effect commit together in one transaction; the written `ServiceDirective` / `CAPA` / `PulseAlert` row is itself the durable, queryable record of the effect. The transactional-outbox machinery (Debezium, Kafka, `FOR UPDATE SKIP LOCKED` relays) exists only to solve dual-write across *process* boundaries, which V4 does not have. Therefore: **no Kafka, no message broker, no microservices, no event bus.** The existing dental-extraction → soft-diet loop is generalized into one reusable transactional trigger dispatcher (a typed trigger registry); each new interlock — epilepsy→outing-safety hold, glucose-measured→insulin-release gate — becomes one declarative file plus one test, not a new endpoint. Read-side interlocks (the insulin screen reads whether a fresh glucose `Reading` exists and blocks if not) use the same primitive. Details in [[basira-v4-cross-service-triggers]].

**4. Engines as pure `lib/engines/*` functions, built only on demand.** The four engines — predictive نبض, governance CAPA, an emergency orchestrator, and the unified bio-psycho-social DB — live as pure functions over Prisma, invoked synchronously by server actions or on a schedule by cron route handlers. Critically, **no engine is scaffolded before a real care loop demands it.** Building empty engines upfront is exactly the V3 hollow-shell failure (3 of 7 V3 "engines" were UI-only). The unified impact DB is not an engine at all — it is the schema; the bio-psycho-social link between records IS the product. See [[basira-v4-engines-and-corpus]].

**5. Security = the settled مؤتمن / تعهد / default-open / AccessLog model.** Every authenticated user is a مؤتمن (a trusted government employee) on the ministry's internal network who signs a تعهد (pledge), sees everything needed to serve, bears full responsibility, and has every access logged — `AccessLog` is the pledge's teeth. **No field masking. No سري/مقيد classification tiers. No security spine.** Re-introducing field classification under a "gov security" banner is the exact drift that ate V3 — it is explicitly out of scope, and the `basira-security-spine` skill is retired from V4. Perimeter control is a different layer: Nafath OIDC (national SSO) plus ZTNA plus MFA apply ONLY on the gated remote/mobile exception path, satisfying NCA ECC at the perimeter+MFA+audit layer — not by classifying fields. The single genuine internal restriction is infectious-disease status (e.g. Hep B / التهاب كبد وبائي): visible only to direct-care medical roles (doctor, nurse) and suppressed on external printouts. Its rationale is **anti-stigma, not privacy** — broadcasting it makes staff fear contact and would block services such as charity housing (الإسكان الخيري); it *serves* the compass by removing a societal barrier and is implemented as a single purpose-built rule, never a tiering system. Roles and delegation are detailed in [[basira-v4-org-roles-rbac]].

**6. Data model = demo beneficiaries plus real-ish employees, real data plugs in later.** Beneficiaries are all DEMO from the start — fake names, no national ID, no real مستفيد (beneficiary) number — but with realistic Al-Baha diagnoses spanning the real population spectrum (ذكور/نساء wards, مجهولو النسب / unknown-parentage cases, ages from the 20s to ~60, employable / athletic Boccia and table-tennis champions / care-only). Diagnosis exists to prevent a service mismatch, never as a ceiling. Employees are not secret — real-style names are fine. The plug-in model: an "add beneficiary" flow takes a national-ID / مستفيد-number, pulls basic social-research data from the ministry DB, and auto-provisions the empowerment program, nutrition/إعاشة program, care team, assigned social worker, and family linkage — so demo rows become real rows transparently with no change to app behavior. Full CRUD on both beneficiary and employee. The disability-empowerment framing is in [[basira-v4-disability-empowerment-model]].

**7. Data residency = the ministry's call, post-approval.** The app is currently Ahmad's innovation submission (مشاركة platform), not yet approved; if approved it goes first to وكالة التأهيل والتوجيه الاجتماعي (the social rehabilitation and guidance agency). Residency, hosting, and integration are handled post-approval by the ministry's Digital Transformation and Compliance agencies. The dev/pitch tier may run on Vercel + Supabase but must carry synthetic data only (no PHI); production must be KSA-resident. Whether the ministry mandates a specific KSA host and whether Supabase is available in-Kingdom remains an open question for Ahmad — it cannot be answered from outside the ministry network — but it is explicitly **not a blocker**: build demo now.

## Consequences

### Positive

- **Lean and verifiable.** One small Next.js app already produced — in ~870 LoC — the working cross-service loop V3 never produced in ~78k LoC. The form/CRUD bulk is carried by generators (a humane-form generator, a cross-trigger scaffolder, an engine-spec generator), keeping the target ~40k LoC reachable.
- **One transactional truth.** Cross-service effects are exactly-once and durable by construction; the directive/CAPA/alert row is the outbox, queryable directly, with no broker to operate or to fail.
- **Honest by design.** Honesty over green: engines ship only from a real, browser-plus-DB-verified loop, structurally preventing the V3 hollow-engine relapse. "It didn't happen unless verified in browser + DB" is the working definition of done.
- **Security simplified.** The settled مؤتمن/pledge/open/log model removes the entire classification-drift surface that consumed V3; gov-grade controls are concentrated where they belong (the remote/mobile perimeter).

### Negative

- **No microservice scaling story yet.** A single process plus single DB means there is no horizontal-scaling or independent-deploy answer until one engine becomes CPU-bound enough to warrant extraction as a sidecar (e.g. a Python ML نبض model the route handler calls). Accepted deliberately — the app is an always-on intranet system, not a public high-scale service.
- **Demo data only until approval.** No real PII is in the build; the realistic-diagnosis demo cohort stands in for the real population until the national-ID plug-in is wired post-approval. This bounds what can be demonstrated end-to-end before ministry sign-off.

### Neutral

- **Postgres swap is deferred.** Development runs on SQLite; the Postgres production datasource is a one-line change made when needed, not now.
- **Production residency is external.** The KSA-resident host (government cloud / STC / Deem / on-prem, and Supabase's in-Kingdom availability) is the ministry's decision after approval — tracked as an open question, not designed around.
- **Open design items remain** and are not auto-decided: per-interlock semantics (advisory alert vs soft-warning vs hard guarded block — sources favor alert + human-action, with glucose→insulin as a deliberate hard improvement), the B1–B10 social-handicap barrier legend (only part survives in sources; recover or define fresh), and re-authoring the PT 5-page clinical assessment from scratch.

## References

- [[basira-v4-rebuild]] — the rebuild hub and gather-phase knowledge base.
- [[basira-v4-compass-and-anti-drift]] — the compass and the settled/anti-drift rules this ADR enforces.
- [[basira-v4-cross-service-triggers]] — the transactional trigger dispatcher and the directive/CAPA/alert row as outbox.
- [[basira-v4-engines-and-corpus]] — the four engines and the corpus that grounds them.
- [[basira-v4-org-roles-rbac]] — roles, delegation, and the مؤتمن authorization model.
- [[basira-v4-disability-empowerment-model]] — demo cohort, disability taxonomy, and empowerment framing.
- [[community-integration-project]] — the CRPD-anchored مشروع الدمج المجتمعي V4 operationalizes.
- [[social-handicap-compass]] — the social-handicap frame, externally validated by the ministry's own report.
- [[ali-alqarni]] — Ahmad's direct manager at the Al-Baha center.
- [[0001-vault-architecture]] — the vault's ADR/MADR conventions this note follows.

> Sources distilled: `C:\dev\basira-v4\CLAUDE.md`; `Desktop\Basira-REBUILD\05-MINISTRY-CONTEXT-AND-DECISIONS-S84.md`; `Desktop\Basira-REBUILD\harvest\10-bestpractices-and-skills.md`; `Desktop\Basira-REBUILD\NEXT-SESSION-PROMPT.md` (S84/S85). This ADR is APPEND-ONLY once accepted.
