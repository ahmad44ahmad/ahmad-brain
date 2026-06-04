---
id: basira-v4-cross-service-triggers
title: Basira V4 — Cross-Service Impact Triggers (The Soul)
type: project
status: active
aliases: []
tags:
  - basira
  - basira-v4
  - cross-service
  - triggers
  - interlocks
  - project
created: 2026-06-04
updated: 2026-06-04
summary: >-
  The KNOW->SERVE wires that make Basira V4 an impact engine, not an e-archive: a care event in one service auto-causes a care action in another. Covers the proven dental->soft-diet loop and its real MHRSD paper origin, the new therapeutic-diet directive matrix, medication-safety interlocks (with the unsourced glucose->insulin flag), the alert-vs-hard-block design decision, outcome services, and the single transactional trigger-dispatcher pattern.
related:
  - "[[basira-v4-rebuild]]"
  - "[[basira-v4-requirements-ledger]]"
  - "[[basira-v4-disability-empowerment-model]]"
  - "[[basira-rebuild-kb]]"
source: session:s85-basira-v4-gather
---

Cross-service impact triggers are the single capability whose absence most distinguishes "real digital transformation" from "paper-to-keyboard." A care event logged in one service (dental, nursing, clinical) auto-causes a care action in another (kitchen, medication, social work). This is the operational expression of the [[basira-v4-rebuild]] compass: KNOW the human's functional, dignity, and safety facts, then SERVE him across services so the facts actually FLOW to whoever protects him. V4's first mandate is to ship ONE working interlock end-to-end before claiming any others. This facet draws from the requirements ledger §B (SERVE / cross-service triggers) and §F (medication-safety interlocks), and the ministry-context decisions §6 (services + the open interlock-semantics decision).

## The honesty discipline (read first)

This section is "the soul," which means overstating it IS the fabrication anti-pattern the corpus condemns (see [[basira-v4-compass-and-anti-drift]]). The celebrated بصيرة "engines" were never actually built; V4 builds real verified loops or claims nothing. The named soul-case interlocks below are flagged honestly as ABSENT in code today — the underlying data hooks exist, but the edges that fire the cross-service action do not. Each interlock V4 ships must come with a characterization test that proves it fires AND the negative case where the guard correctly blocks it (e.g. a time-boxed soft-diet must expire; a stale glucose reading must not release an action).

## The proven loop: dental extraction -> kitchen soft-diet

This is Ahmad's canonical proof case. A nurse or dentist logs a dental extraction; the system, in one transaction, also emits a soft-diet directive to the kitchen (serve soft and cool food for 2-3 days, no hot food, no straws). It is the clearest small demonstration that information creates impact rather than resting in a record.

The loop has a **real MHRSD paper origin** — this is not an invented UX. Two governmental forms already encode it:

- نموذج جدول وجبات الحميات (the diet-schedule / therapeutic-meals form), and
- استمارة تبليغ مطبخ بالحالة (the kitchen-notification-of-case form).

The paper workflow is exactly KNOW (a clinical event) -> SERVE (notify the kitchen to modify the meal). V4 re-authors that paper wire as a digital trigger. The proven target model on the nutrition side comes from the Drive الإعاشة (catering) folder: a beneficiary dietary plan with `diet_type` (minced / pureed / liquid) plus a `texture_modification` field, and a `calculateAdjustedPortion` rule (pureed x1.1, liquid x1.2) — the literal soft-diet mechanism. Status is honest: the edge is ABSENT in code in every version, but the nutrition target model is PROVEN as a Drive design. A real ministry alert-tag form independently validates the shape: صعوبة بلع (swallowing difficulty) -> pureed is the same SafetyFact-emits-directive pattern as dental -> soft-diet.

## The admission assessment as a fan-out router (harvest 14-g)

A deeper paper origin surfaced in Track A's read of the EHS/DR coded medical-forms manual: the **EHS-001 admission "Evaluation Sheet"** carries an **Interventions matrix** — a Yes/No checkbox per discipline (Medical / Physical / Social / Occupational / Speech / Psychological) — so **one** completed intake routes the beneficiary to **up to six services at once**. It is the cleanest "one KNOW event → N SERVE actions" pattern in the entire corpus, and it generalises the single dental→soft-diet wire into a fan-out dispatch. The same form makes the diet directive a literal field, not a Basira invention: **feeding-consistency** is captured at admission as `Normal / Grinded / Liquid` + method `Oral / NGT / Gastrostomy` + `Dysphagia Y/N` — the real paper origin of the dysphagia / dental → soft-diet edge. `Epilepsy controlled/uncontrolled` at intake is likewise the precondition signal for the epilepsy→outing-safety hold. The coded pack also carries DR-0013 (the infectious-disease report → the real anti-stigma workflow) and DR-0004, a bedside "Resident Passport" of facts that travel (diagnosis, meds, PT instructions, diet, allergy). Full field set: [[basira-rebuild-kb]] (KB: harvest/14-g §3).

## The therapeutic-diet directive matrix (NEW wiring to build)

The dental loop generalizes into a matrix of functional-fact -> diet-directive edges. This is a DESIGN GAP, not a port: the catering documents govern the *supplier* (contracts, FIFO, food-safety), but say nothing about fitting the meal to the human — so V4 designs this from the compass and wires it to the existing ServiceDirective/kitchen surface. The matrix:

- dysphagia / صعوبة بلع -> pureed texture
- dental extraction -> soft diet (the proven edge above)
- diabetes / مريض سكري -> diabetic diet
- food allergy / حساسية طعام -> exclude the allergen (cross-service hard-block across both medication and catering)
- طريح فراش (bedridden) -> assisted feeding / NPO as appropriate

The directive is keyed to KNOWN functional and safety facts, which is exactly why the [[basira-v4-disability-empowerment-model]] insists those facts are functional truths that travel, never diagnoses to hide. This matrix is the most compass-relevant catering capability V4 can add.

## Medication-safety interlocks (ledger §F)

These gate a medication action on a measured reading or recorded fact before the administration write.

- **glucose-measured -> diabetic-diet** edge: PROVEN as a Drive design — a morning glucose reading drives the kitchen to show the adjusted diabetic diet. This is the safe, sourced glucose edge.
- **glucose-measured -> insulin interlock** (gate insulin admin by a high/low glucose band before writing `MedicationAdministration`): **PROVENANCE FLAG — UNSOURCED.** This case is named in the brief and is a generic clinical illustration, but it does NOT appear in any sourced Basira document. It is therefore a deliberate *hard-block safety-improvement candidate*, not a port. Before building it, confirm insulin-by-band against a real MHRSD diabetes / medication form. The honest distinction: glucose -> diabetic-diet is real-in-Drive-design; glucose -> insulin is an unsourced improvement.
- Supporting structure: V3 has `MedicationAdministration` (make it append-only) and `Prescription`, but is MISSING a `MedicationSchedule` model (so `GET /medication-schedule` is a 404 with no backing table) — V4 must add it to close the eMAR. A late **epilepsy** drug escalates to CRITICAL instantly (vs a late recreational drug = low), per the Drive governance-engine risk matrix — time-criticality varies by drug class.
- allergy + drug-restriction hard-block spans medication and catering together (the same allergen edge as the diet matrix).

## The open design decision: alert vs hard-block

Interlock semantics is a genuinely OPEN design decision (ministry-context §8 lists it as still-open for S85; do not auto-pick a universal rule). The harvest finding breaks the tie for the default:

> Every existing REAL cross-service procedure in the corpus is **alert + human-action — never auto-block.** Nabd's five live rules are detection-then-alert. The proven fall-risk and vitals-breach loops are threshold-then-alert-then-acknowledge. The real ministry referral forms (round-trip PT<->medical) are alert + human action.

Therefore the design rule is: **default = advisory alert** (emit a cross-domain alert plus a write-back directive that a human confirms), and add **HARD guarded blocks only where safety strictly demands it** — the glucose -> insulin case and the allergy hard-block being the candidates. Building everything as a hard auto-block would contradict every real procedure in the corpus and re-import the rigidity the compass rejects. Build interlocks on Nabd's reactor pattern (the only genuine cross-service reactor that exists, live in V3 — see [[basira-v4-engines-and-corpus]]) and extend from alert toward interlock only where the safety case is explicit and sourced.

## Cross-service and outcome services

Beyond the clinical interlocks, the compass reaches the outcome services that break societal barriers (the [[social-handicap-compass]] frame at the [[albaha-center-org]] center):

- **charity housing (الإسكان الخيري)** — families consent to community reintegration when the housing is registered in the beneficiary's name; an infectious-disease flag broadcast wrongly would block this service, which is precisely why the one anti-stigma restriction exists.
- **home-based personal care** — a worker visits the home (~2 years), serving 5-6 home cases instead of institutional care.
- **vocational rehabilitation in the private sector** — an API-linked "island" portal; real stipend constants exist (1,200 SAR/month married, 800 single, 300 to the trainer) with a 7-step enrollment-and-de-register procedure.
- **كسوة (clothing)** — summer and winter clothing (~1,500 SAR each), allocation driven by service-category (متحرك / مقعد / طريح فراش) so a bedridden case is not allocated running shoes; the real field تفصيل خاص لطريحي الفراش proves the mobility-aware allocation. Advance authority escalates to the Minister.

A related cross-service signal: a beneficiary's attendance state (حاضر / غائب / إجازة / مستشفى) is itself a trigger — مستشفى (in hospital) means the person is not being fed at the center, so both care and finance/catering react.

## The implementation pattern: single transactional trigger-dispatcher

The mechanism is one transactional outbox, not a brittle web of point-to-point calls. In **one DB transaction**, the source service writes BOTH the source care event AND the resulting `ServiceDirective` row. That directive row IS the outbox record; the consuming service simply READS it. The proven first loop already demonstrates this: a dental extraction write and the soft-diet `ServiceDirective` land atomically, and the kitchen page reads the directive — the `sourceCareEventId` link makes the cross-service wire real and traceable, not a UI illusion.

The V4 design rule (ledger §B) states it precisely: every clinical, dental, or safety write evaluates the rule set and may emit a cross-domain alert plus a write-back action in another service, in the same transaction. One transactional trigger-dispatcher; engines as pure library functions; the consuming surface reads the row. This keeps the soul honest — the wire either commits both halves or neither, and every fire is a row you can point at. See the full row-level detail in [[basira-v4-requirements-ledger]].
