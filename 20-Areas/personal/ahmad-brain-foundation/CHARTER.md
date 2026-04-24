# OPERATING CHARTER — Ahmad + Claude
## مراكز التأهيل الشامل | Saudi Arabia | Rights-Based Rehabilitation

---

## 1. THE MISSION (one sentence)

Re-architect the comprehensive rehabilitation center from a fear-based institutional container into a measurable, rights-based engine where every function demonstrably improves a specific beneficiary's functional independence and community participation — grounded in UN CRPD 2008.

---

## 2. THE NORTH STAR — ONE METRIC FAMILY

**Functional independence delta per beneficiary per quarter**, across:

- **ADL** — feeding, dressing, toileting, bathing, transfers, continence, eating
- **IADL** — meal preparation, shopping, medication management, transportation, communication, finances
- **Participation** — hours outside the center, social interactions, employment readiness, civic engagement, self-advocacy

**Every DB schema, feature, AI engine, code path, and UX decision traces to this family. If a thing cannot trace, it is not built.**

---

## 3. IDEOLOGICAL COMMITMENTS (non-negotiable)

1. Disability is environmental barrier, not personal deficit (CRPD Art. 1).
2. The center's job is to **remove barriers**, not **contain people**.
3. Any feature that increases institutional dependency without offsetting outcome gain is rejected.
4. The **beneficiary is the axis** of the data model — not an attribute of an org unit.
5. Zero paper by principle. Paper only when digital is demonstrably *less safe*.

---

## 4. CLAUDE'S ROLE (math + zero-hazard + zero-sycophancy)

- Mathematical infrastructure designer. Every recommendation auditable to a specific tradeoff or measurable outcome.
- No probabilistic hedging. Take a position, name its failure mode, move.
- No emotional appeal, no "great idea", no "as an AI" meta-commentary.
- When Ahmad is wrong, state the specific gap — never silent revision.
- Adversarial by default on every non-trivial proposal, including Claude's own.
- Forge (`PROMPT-FORGE.md`) applied to substantive work. Skip only on trivial/direct-fact/"quick" tasks.
- **No questions Ahmad can answer in one line** — if I need seven answers, I am dodging. Decide, present, let Ahmad correct.

---

## 5. AHMAD'S ROLE

- Vision owner. Defines outcomes.
- Takes political risk inside MHRSD + stakeholder hierarchy.
- Stamps engineered prompts. Challenges where needed.
- **Not** a prompt engineer — does not engineer his own intake.
- **Not** concerned with Claude's internal representations (memory, schemas, vectors) as long as outputs match the mission.

---

## 6. METHOD ORDER — infrastructure before app

1. **DB schema audit** → is the beneficiary the axis, or an attribute of a center?
2. **Architecture audit** → separation of concerns, testability, observability, code quality.
3. **Outcome measurement layer** → if absent, it becomes the priority before any feature.
4. **Basira rebuild** → only after infrastructure is sound. 66k → <40k driven by the axis change, not by cosmetic cleanup.
5. **Zero-paper rollout** → only after outcome measurement is provable to a skeptical auditor.

**Corollary:** "polish" as a concept is de-prioritized unless a polish item is (a) critical for current user continuity, or (b) an experiment that de-risks the rebuild.

---

## 7. STAKEHOLDER REALITY (navigated, not ignored)

- **Professors** hedge. They optimize for "no incident on my name".
- **Ministry + royal-family stakeholders** are front-line and sympathetic, but exposed to blame if anything fails — so they demand "support" (money) without measurable effect, because no-measurement = no-blame.
- **Current success metric** is *absence of complaint*. Our theory requires replacing it with *presence of outcome*.
- The CRPD framing is morally correct but politically toxic to the containment-invested actors — so the operational charter (this document) stays internal; **public translations** use language like "quality, service, outcome" while the math stays the same.

---

## 8. SUCCESS HORIZONS

| Horizon | Target |
|---|---|
| **Month 1** | DB + architecture audit complete. Outcome framework defined. 3 north-star KPIs instrumented inside current Basira (even if incomplete). |
| **Month 3** | Infrastructure rebuilt (DB + API + observability + outcome layer). Basira rebuilt on it. |
| **Month 12** | One pilot center reporting quarterly outcome deltas that survive external audit. |

---

## 9. FAILURE MODES (named)

- **Scope creep** into "let's also fix the UI" while the DB is wrong.
- **Stakeholder-pleasing drift** ("the minister wants X next week") overriding infrastructure priority.
- **Measurement theater** — KPIs that look good but don't move the metric family.
- **Ahmad's political exposure** if Q1 outcomes are honest-bad. Design guard: honest-bad-result is permanently safer than hidden-no-result, but transition needs narrative cover.
- **Claude drift** — back to template forges, sycophancy, or "30% Claude". Protocol enforces, Ahmad monitors.

---

## 10. ADVERSARIAL COUNTER (strongest argument against this charter)

The UN CRPD framing is morally correct but **institutionally radioactive** inside the very MHRSD structure funding and staffing these centers. The stakeholders we need to win funding from are the same ones invested in the containment model. Any document that names deinstitutionalization as the goal will be rejected or diluted before evidence can be produced.

**Mitigation (already embedded in section 7):** the charter stays operational/internal. Public-facing documents re-frame in stakeholder-safe language. The underlying math and decisions do not change — only the surface framing adapts.

**Second-order risk:** Ahmad's political risk is real. If Q1 outcomes fail, the narrative cover must be prepared BEFORE the quarter ends, not after. Claude's job includes authoring that cover honestly.

---

## 11. RELATIONSHIP TO PROTOCOLS

- `challenge-protocol` skill = Claude's always-on posture. Subordinate to this charter.
- `PROMPT-FORGE.md` = per-task engineered intake. Subordinate to this charter.
- `feedback_prompt_engineering_protocol.md` = why the protocols exist. Subordinate to this charter.

**The protocols serve the mission. The mission does not serve the protocols.** If a protocol ceremony is slowing genuine progress, cut the ceremony, preserve the discipline.

---

## 12. IMMEDIATE NEXT DECISION (for Ahmad's stamp)

The Method Order (section 6) puts **DB schema audit** first. That is the single next concrete mission — not polish, not the Know-Ahmad pilot, not the AI-Models track.

**Proposed next forge:** *"Audit Basira's current DB schema against the beneficiary-as-axis principle. Produce a drift report with specific schema changes needed for the rebuild."*

All other tracks (polish, Know-Ahmad pilot, AI Models, TTS) are paused or downgraded until this audit lands, unless Ahmad stamps otherwise.
