---
id: mhrsd-cyber-policy-library
title: "MHRSD Cybersecurity Policy Library (63-doc ISMS) — NCA-ECC / PDPL anchor + Basira anti-drift validator"
type: source
status: active
aliases:
  - cyber-policy-harvest
  - DT-IS-POL
  - mhrsd-isms
  - الأمن-السيبراني-السياسات
  - NCA-ECC-2-2024
tags:
  - mhrsd
  - cybersecurity
  - nca-ecc
  - pdpl
  - governance
  - basira-v4
  - anti-drift
  - source
created: 2026-06-05
updated: 2026-06-05
source: local-fs:C:\Users\aass1\Desktop\Cyber-Policy-Harvest\
summary: >-
  MHRSD's own 63-document ISMS policy library (DT-IS-POL/FRM codes; NCA-ECC-2:2024,
  CSCC-1:2019, CCC-1:2020, PDPL/SDAIA, ISO-27001 aligned), harvested 2026-06-05.
  Its 33 PERIMETER-ADOPT vs 9 DO-NOT-IMPORT split independently validates Basira V4's
  settled doctrine: enforce security at the residency/perimeter/AccessLog layer, never by
  in-app field-masking. Carries the V4 deployment-compliance skeleton and the live
  Supabase PDPL-exposure tie.
related:
  - "[[basira-v4-compass-and-anti-drift]]"
  - "[[basira-v4-rebuild]]"
  - "[[basira-rebuild-kb]]"
  - "[[basira-v4-requirements-ledger]]"
  - "[[mhrsd-risk-excellence-policies-2025]]"
  - "[[basira]]"
  - "[[hrsd-work]]"
---

# MHRSD Cybersecurity Policy Library

## What this source is

A **63-document Saudi-government ISMS policy library** — MHRSD's *own* information-security policy set, coded `DT-IS-POL-####` / `DT-IS-FRM-####` (plus privacy/governance policies under `DT/DTE/DG/...`). Harvested 2026-06-05 from `D:\الأمن السبراني-...\الأمن السبراني` (62/64 PDFs/docx extracted clean via PyMuPDF; 2 governance PDFs are image-scans, OCR-deferred). A 9-subagent workflow extracted each policy's purpose, key controls, NCA-ECC domain, PDPL relevance, Basira-deployment relevance, and an anti-drift flag; **57 documents registered**.

The corpus is aligned to the live Saudi regulatory stack: **NCA ECC-2:2024** (current Essential Cybersecurity Controls) + ECC-1:2018, **CSCC-1:2019** (Critical Systems), **CCC-1:2020** (Cloud), **PDPL** + **SDAIA**, **DGA / NORA / COBIT 2019 / ISO 27001-27017-27018-22301-38500 / TOGAF 10 / OWASP-NIST / ITIL-SACM-PMBOK**. NCA-ECC domain 5 (ICS/OT) is absent and not applicable to a web information system.

This is the *operational* ISMS detail layer beneath [[mhrsd-risk-excellence-policies-2025]] (the April-2025 Al-Ghamdi-chaired risk/excellence/innovation bundle) — same ministry, finer grain. Where that note documents the governance *promulgation*, this documents the **per-control** security policies Basira must answer to. The map lives at `Cyber-Policy-Harvest\00-INDEX.md`; the per-policy control text is in `harvest\01..09-*.md` — **point there for any audit quote, don't paraphrase from this note.**

## The anti-drift firewall — and why the 9-vs-33 split validates Basira

Every policy was tagged: **PERIMETER-ADOPT 33 · NEUTRAL 15 · DO-NOT-IMPORT-AS-IN-APP-TIER 9.**

- **PERIMETER-ADOPT (33)** = a deployment / infra / build / governance control Basira meets **at the perimeter** (hosting, residency, auth front-door, crypto, SDLC pipeline, logging, backup, incident, vendor) — most are ministry-provided infra *post-approval*.
- **DO-NOT-IMPORT-AS-IN-APP-TIER (9)** = the **data-classification / IAM-tier / asset-labelling** policies (POL-1000 classification, POL-1400 ×2 IAM, POL-900/POL-2800 data-protection, POL-700 sensitive-systems, POL-100/DG-01-50 asset-&-config, Data-Privacy V5.0). Each *must* be satisfied — but at the **residency + perimeter-auth + AccessLog** layer, **never** by rebuilding سري/مقيد (secret/restricted) field-masking inside the serving app.

**Why this independently validates V4's settled doctrine.** Basira V4's security model is already closed (see [[basira-v4-compass-and-anti-drift]] §2): every user is a pledged مؤتمن (*entrusted employee*) who signs a تعهد, sees what they need to serve, default-OPEN, every read logged in `AccessLog` — **no masking, no classification tiers, no security-spine**. An external observer would expect a ministry ISMS full of classification mandates to *contradict* that. It does the opposite: when the corpus's own classification/IAM policies are read carefully, **every one of them is satisfiable at residency/perimeter/log** without a single in-app tier. The reconciliation the harvest states once and everywhere: *"data classification / access tiering" is met by data RESIDENCY (KSA) + PERIMETER AUTH (Nafath/MFA) + the immutable ACCESS-LOG* — which is exactly Basira's model. So MHRSD's own ISMS, far from forcing the V3 سري-sewer drift back in, is documentary cover that the V4 doctrine is *compliant by design*. The classification clauses inside otherwise-adopt policies (e.g. cloud POL-400 §3.4.2 "classify before hosting") are **deferrals** to the separate POL-1000 family, not in-app masking mandates — treat the whole V4 store as ONE مقيّد, KSA-resident, encrypted, audit-logged CI for the ministry CMDB. (Harvest detail: `09-BASIRA-DEPLOYMENT-RELEVANCE.md` §2; ledger anti-pattern `J-NA-9`.)

## The load-bearing policies for Basira deployment

Compact per-policy table; full controls in `harvest\NN-*.md` as noted.

| Policy | What it binds for Basira | Flag |
|---|---|---|
| **POL-2700** Web App Security | 2FA at login, OWASP input-validation, dev/test/prod separation, no dev→prod-config access, restricted source access, **vuln-scan + pen-test + remediate-all before go-live**, go-live approval gate | ADOPT |
| **POL-3100** Secure SDLC + **DG/01/24** Software-Dev | security-by-design (OWASP+NIST), **PR code-review + unit tests before merge**, branch protection, SAST + OSS license/vuln scan + inventory, POT/UAT gate, secure decommission | ADOPT |
| **POL-400** Cloud (CCC-1:2020) + **DG/01/25** | **PHI hosted inside KSA** on an NCA/CCC-registered provider; tenant isolation; encrypt at-rest+in-transit (National Crypto Standards); MFA-privileged; audit logs reviewed; 3-monthly vuln remediation; BC/DR; **irreversible exit-erasure** | ADOPT |
| **POL-1300** Event Logs & Monitoring | `AccessLog` *is* the audit trail: actor+action+timestamp+result, immutable, ≥**12-month** retention, NTP time-sync, shipped to ministry **SIEM**, read-only audit access | ADOPT |
| **POL-1600** Incident & Threat Mgmt | wire into ministry IR plan; **PDPL breach path — any beneficiary-data leak → notify SDAIA + report NCA ≤72h** | ADOPT |
| **POL-2200** Remote Work | the literal spec for `basira-nafath-gate`: MFA, session mgmt + idle timeout, in-transit encryption, KSA residency, ≥12-mo log retention, annual access review | ADOPT |
| **POL-2900 / POL-3000** AI + **DG/01/22** AI (DGA/SDAIA) | **never send beneficiary PII to external/generative AI**; de-identify; minimum-necessary; approved tools; vendor NDA; model governance — a *real* constraint on any "engine" ambition | ADOPT |
| **POL-800** Cryptography | TLS/IPsec all transit; PHI at-rest encryption; **salted-hash all passwords**; valid CA certs in prod; key mgmt + CRL | ADOPT |
| **POL-2600** Third-Party & Project | any Basira vendor/hosting/ETL/Nafath integrator: supplier eval, NDA+SLA, **KSA-resident SOC**, screened staff, revoke-on-exit, audit-record availability | ADOPT |
| **POL-200/300** Backup + BC | DB/config/log backup ≥monthly **+ full backup around every migration**; tested restore; RTO/RPO/DR | ADOPT |
| **POL-1000** Data Classification · **POL-1400 ×2** IAM · **POL-100/DG-01-50** Asset/CMDB · **Data-Privacy V5.0** | the classification/tier engines — satisfy at **residency + perimeter-auth + AccessLog**; the `role` is a *capability* (nurse/nutrition), **not** a secrecy tier | **DO-NOT-IMPORT** |

Governance gates (ministry-onboarding, *not* demo blockers): a **CSRMF risk assessment** (FRM-2320) before cloud go-live, an **Enterprise-Architecture review** (EA/01/02), and an **ECC-2:2024 / CSCC-1:2019 self-assessment** (FRM-520). Name the owner; don't block the demo. (`09-...` §1-J.)

## The compliance gap this implies for the *current* Basira

The corpus turns Basira's hygiene problems into **named PDPL + POL obligations**, not optional polish:

- **KSA data residency is mandated by ≥6 policies** (POL-400/700/1900/2200, Data-Privacy V5.0, DG/01/25). This validates "real PHI only on KSA-resident prod Postgres; synthetic-only on the Vercel/Supabase pitch tier" (V4 plan §4.4) — and converts the **live Supabase exposure into a documented breach**, not just hygiene.
- **The 139 real beneficiaries are anon-readable on the legacy Supabase** (RLS off + `GRANT ALL anon` from the 2026-04-14 recovery) — see [[basira-v4-requirements-ledger]] and the rebuild data findings in [[basira-rebuild-kb]]. Against this corpus that posture **violates POL-400 §3.4 (access restricted to authenticated/authorized), POL-1300 (no audit trail), POL-1000 (an unclassified open store), and PDPL security-of-processing** — and triggers **POL-1600's SDAIA+NCA ≤72h breach path**.
- **GitHub PHI-repo exposure** (8 Basira/beneficiary repos were public; real Google creds + `DB_PASS` + beneficiary SQL in history — memory `project_github_repo_exposure_2026-06`). Still-PENDING on Ahmad: **credential rotation + a PDPL/NCA breach assessment through the GRC process**. The corpus is the regulatory yardstick that assessment is measured against.
- **National-ID-lookup integration** to ministry DBs is a **Data-Sharing boundary** → needs a signed **DSA**, secure government channel, anonymize-on-export, and a **DPIA** (POL-900). Flag for the post-approval plug-in path.

The V4 ETL is therefore the **last read from an exposed DB — then lock it** (RLS on, revoke anon). For the مشاركة/onboarding submission, use `09-...` §1 as the "how is it secure/compliant" skeleton, marking each control **met-by-design** (SDLC, AccessLog, encryption, residency decision) vs **ministry-infra post-approval** (hosting/SIEM/IR/DR). One open provenance check (`09-...` §4-5): the agents *inferred* this is MHRSD's authoritative live ISMS from internal HRSD/DTA/Himmah references — confirm it is the production policy set (vs a template) before citing it in a submission.

---INTEGRATION-NOTES---

- **[[basira-v4-compass-and-anti-drift]]** — add a reciprocal back-link: its §2 (settled security model) and §6 (NOT-ADOPTED ledger) now have an *external ministry-ISMS validator*; one line like "MHRSD's own 63-doc ISMS independently confirms this is compliant-by-design — see [[mhrsd-cyber-policy-library]]" strengthens the closed-decision case.
- **[[basira-v4-requirements-ledger]]** / **[[basira-rebuild-kb]]** — back-link from the §D governance + data-exposure findings; this note is the regulatory yardstick for the Supabase/GitHub exposure rows (anchors the J-NA-9 anti-pattern to real policy codes).
- **[[mhrsd-risk-excellence-policies-2025]]** — reciprocal link: that note's §"regulatory surface Basira sits inside" should point here as the per-control ISMS detail layer beneath its April-2025 governance bundle.
- A separate **synthesis note is NOT yet warranted** — the harvest's own `09-BASIRA-DEPLOYMENT-RELEVANCE.md` already is the synthesis, and this source note distils it. If/when Ahmad drafts the actual compliance one-pager for the مشاركة submission, *that* deliverable (a `project`-type note, not a source) would be the place to fuse this with the residency/exposure remediation plan.
