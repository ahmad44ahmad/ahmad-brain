---
id: integration-readiness-classification
title: "Integration-Readiness Classification — Destination Tracks, STAY-as-Exception, Disqualifier-as-Barrier"
type: concept
status: active
aliases:
  - integration-readiness
  - readiness-classification
  - stay-as-exception
  - disqualifier-as-barrier
tags:
  - concept
  - empowerment
  - de-institutionalization
  - disability
  - classification
  - crpd
created: 2026-06-10
updated: 2026-06-16
valid_from: 2026-06-10
learned_at: 2026-06-10
confidence: high
source: local-fs:C:\Users\aass1\Desktop\Empowerment-Knowledge-Extract\_MISSING-DATA-APP-GAP-MAP.md
related:
  - "[[basira-v4-disability-empowerment-model]]"
  - "[[basira-capability-domain-catalog]]"
  - "[[alternative-services-catalogue]]"
  - "[[empowerment-ledger-vs-custodial-return]]"
  - "[[family-fear-barrier]]"
  - "[[community-integration-project]]"
  - "[[case-shifting-de-dilution]]"
  - "[[tai-alqaid-closure-gate]]"
  - "[[de-institutionalization-moc]]"
summary: >-
  The standalone readiness scheme, distinct from device-allocation and
  eligibility-gating. Sorts a resident toward a destination track, treats STAY as a
  justified, periodically re-reviewed exception (never a default park), reframes
  every disqualifier as a barrier to dismantle rather than a denial, and takes
  income/guardian/region as structured inputs. Recommend, never deny.
---

# Integration-Readiness Classification

## The delta this note carries

The 8 destination tracks, the 9-value disqualification enum, and the `IntegrationCandidacy` shape already live verbatim in [[basira-v4-disability-empowerment-model]] — **this note does not restate them.** Its delta is the *readiness scheme itself*: a standalone, reusable classification distinct from the device-allocation lookup and the intake eligibility-gates, with four design rules.

## The scheme

**1. Destination tracks.** Readiness routes a resident toward a destination (home-based social/medical care, vocational rehab, day-care, supported community living), not a static bed. The arrow, not the bed, is the unit of progress ([[community-integration-project]]). Track definitions are referenced from [[basira-v4-disability-empowerment-model]]; eligibility rules key into [[alternative-services-catalogue]].

**2. STAY as a re-reviewed exception.** Residential STAY (البقاء بالتأهيل) is a **justified, periodically re-reviewed exception**, never a resting state and never a default park. This is consistent with — not contrary to — the existing rule that مسار الإيواء carries QoL-in-residence as its goal-of-record for genuinely pervasive-support-needs beneficiaries ([[basira-capability-domain-catalog]], التمكين التأسيسي foundational track): for those who truly need it, STAY means active QoL-in-place goals plus a standing re-review clock; it is never the silent destination for everyone else.

**3. Disqualifier-as-barrier, never denial.** Every disqualifier (IQ cutoffs, epilepsy/psychiatric exclusions, age windows, no-pension rules, communicable disease, no first-degree provider) is a **barrier to dismantle**, not a hard deny. "Recommend, never deny." A communicable-disease flag triggers flow-not-hide handling; "no family" triggers الإرشاد الأسري + aftercare ([[family-fear-barrier]]), not a stay justification.

**4. Structured inputs.** Income bracket, guardian/provider status, and **region-availability** enter as structured fields — and region-unavailability is logged as a *system accountability gap*, never a beneficiary property ([[alternative-services-catalogue]]).

## Why it stays separate

Folding readiness into device-allocation or eligibility-gating reintroduces the medical-model ceiling. Kept standalone, it feeds the empowerment ledger's exits-with-destination ([[empowerment-ledger-vs-custodial-return]]) and supplies the post-discharge integration-quality check that pairs with any transition KPI.
