# StreamCollider Boundary Intelligence Record — SC-BIR-002

**Title:** Director-Managed Chiplet Boundary (UCIe 3.0 Manageability)  
**Record ID:** SC-BIR-002  
**Version:** 1.0-draft (Gate 1 evidence ledger)  
**Status:** EVIDENCE-BOUNDED · NOT PUBLIC · GATE 1 FALSIFICATION PENDING  
**Case ID:** SC-RC-002  
**Last verified:** 2026-08-31  
**Authorization:** Gate 1 Candidate A ADVANCE (DEC-013)  
**Machine-readable (repo only):** `data/boundaries/sc-bir-002.json`  
**Public surface:** **NONE** — no production route until evidence ledger passes Gate 1 falsification and governance review.

> UCIe manageability mechanics alone do not admit a Stream Collision. This record tests whether **director ↔ satellite chiplet** roles create a **deployment-relevant governance boundary** with authority, state, proof, and recovery gaps that survive cross-source audit.

---

## 1. Domains

| Side | Domain | Governance character (under test) |
|---|---|---|
| **A** | Director / management hub (director chiplet, anchor, or designated manageability authority) | Obtains external firmware, initializes sideband management fabric, downloads first mutable firmware, may broadcast package-level throttle/shutdown |
| **B** | Satellite / managed chiplet(s) | Waits for director-mediated mutable firmware; may request further updates; holds local bring-up, SERDES/memory init, temperature sensing, and local execution state |

**Boundary mechanism:** UCIe 3.0 manageability — early firmware download (sideband register/FSM path), Management Transport Protocol (MCTP/PLDM-class flows), priority sideband packets, open-drain fast throttle / emergency shutdown.

**Deployment question (central):** Are A and B **independently governed authorities** in production SiPs, or **protocol roles** operated under a single integrator/vendor policy?

---

## 2. Admission

| Condition | Result | Evidence basis |
|---|---|---|
| Distinct governance | **CONDITIONAL** | Protocol roles are distinct (SC-C002). Deployment-level independence is **not closed** — integrator may unify policy (SC-C003). |
| Boundary crossing | **PASS** | Firmware images, MTP/management packets, priority events, open-drain signals cross the link (SC-C002, SC-C005). |
| Mutual consequence | **PASS** | Chiplet blocked without director FW; director boot depends on chiplet responses; SiP-wide throttle/shutdown overrides local assumptions (SC-C002, SC-C005). |
| Negative control | **PASS** | Monolithic die or per-chiplet local flash / immutable-only firmware without director-mediated mutable download avoids this boundary (DEC-008; SC-C002 motivation). |

**Admission note:** Three-part admission is **not fully closed** until U-01 (deployment-level distinct governance) receives a evidence-backed classification stronger than protocol-role description alone. Ledger completion ≠ Gate 1 PASS.

---

## 3. Authority map

| Authority dimension | Domain A (director / hub) | Domain B (satellite chiplet) | Boundary note |
|---|---|---|---|
| Firmware / MTP ownership | Obtains FW from external flash; initiates first mutable download | Waits; receives; may request further updates | Ownership vs staging authority open (U-02) |
| Configuration state | Drives boot sequencing across sideband network | Holds local config after partial download | Authoritative state open (U-03, U-07) |
| Version / capability | Selects/images to push | Advertises capability; may reject | Mismatch authority open (U-04) |
| Recovery | Retries/rollback policy (integrator-defined) | Safe state / inconsistent config risk | Recovery owner fragmented (U-05) |
| Emergency control | SiP-wide fast throttle / emergency shutdown broadcast | Local Tj sensing + local mitigation | Precedence vs local state (U-06) |
| Proof / evidence | Management transaction logs (implementation-dependent) | Local fault/status visibility | Interrupted-action proof open (U-08) |
| Security / authorization | Protected management path (director↔chiplet SB link) | Access to mutable FW surface | Security boundary in verification reqs, not closed contract (U-02, U-08) |

---

## 4. Architecture says / Boundary intelligence asks

| Architecture says | Boundary intelligence asks |
|---|---|
| UCIe 3.0 adds manageability (MTP, FW download, throttle) | Who **owns** authority at deployment — protocol role, integrator, or vendor? |
| Director chiplet downloads mutable firmware | What configuration is **authoritative** after partial or staged download? |
| Chiplet waits, then boots mutable firmware | What **proves** safe boot vs inconsistent state? |
| Version/capability negotiation exists | Who decides **rejection** authority and what evidence crosses the boundary? |
| Priority sideband + open-drain emergency events | Does package-wide throttle **override** chiplet-local execution state — and who proves it? |
| Multi-vendor open chiplet ecosystem | When does “multi-vendor” mean **independent governance** vs single SiP operator? |
| Compliance testing exists | Does compliance **prove** interoperability and recovery authority? |

---

## 5. Evidence matrix (linked)

See `research/BOUNDARY_EVIDENCE_MATRIX_BIR_002.md` and `research/SC_BIR_002_UNKNOWN_CLOSURE_MATRIX.md`.

| ID | Surface | Reading |
|---|---|---|
| B2-001 | Deployment-level distinct governance | **Open** — protocol roles strong; operational independence not normatively closed |
| B2-002 | Firmware / MTP ownership | **Open** — flows documented; ownership/precedence incomplete in public pack |
| B2-003 | Authoritative configuration state | **Open** — partial download / inconsistent config explicitly flagged in verification literature |
| B2-004 | Version mismatch authority | **Open** — rejection scenarios required in verification; normative cross-party contract not in brief |
| B2-005 | Partial-update recovery | **Open** — retry/rollback/safe-state owner not standardized in public materials |
| B2-006 | Emergency throttle / shutdown vs local state | **Strong partial** — SiP-wide mechanisms documented; precedence proof open |
| B2-007 | Director vs chiplet state disagreement | **Open** — no universal precedence table |
| B2-008 | Proof after failed / interrupted management | **Open** — verification requires evidence; production proof contract absent |
| B2-009 | Negative control | **Strong** — monolithic / local-FW-only path documented |

---

## 6. Known / Unknown / Assumed

### Known
- UCIe 3.0 standardizes early mutable firmware download via director-mediated sideband flow; satellite chiplet waits (SC-C002).
- Priority sideband and open-drain fast throttle / emergency shutdown provide SiP-wide low-latency control paths (SC-C002, SC-C005).
- Verification literature treats MTP boot, version mismatch, partial transfer, recovery, and security as **required test surfaces** — not solved by link compliance alone (SC-C003).
- Multi-vendor interoperability can fail despite local compliance due to firmware policy, timeouts, and recovery differences (SC-C003).

### Unknown
- Whether director vs satellite constitutes **independent governance** in deployment, or a single integrator policy wearing two protocol hats (U-01).
- Authoritative configuration state after partial download; version-mismatch rejection proof; recovery owner graph; throttle vs local state precedence; proof artifact after interrupted management (U-03…U-08).

### Assumed
- No unpublished SiP integrator runbook is treated as public evidence.
- Director role assignment in a product does not by itself prove governance independence.

### Evidence Boundary
Public UCIe consortium briefs and verification analysis end before normative cross-vendor **deployment authority**, **recovery ownership**, and **reconciled proof** contracts.

---

## 7. Contradiction register (linked)

`research/SC_CONTRADICTION_REGISTER.md` — entries SC-CON-008…012 (BIR-002 scope).

---

## 8. Negative control

**Monolithic die** or **satellite with local immutable/flash firmware only** (no director-mediated first mutable download path) avoids the director↔satellite management boundary under test. UCIe may still be present as transport; the governance seam being tested is **manageability authority split**, not die-to-die links alone.

---

## 9. Relationship to SC-BIR-001

| Dimension | SC-BIR-001 (HPC ↔ remote QPU) | SC-BIR-002 (director ↔ chiplet) |
|---|---|---|
| Primary Unknown pattern | Queue/state/precedence across schedulers | FW/config/precedence across management roles |
| Independence test | Provider vs WLM | Satellite vendor vs director vs integrator |
| Risk if forced | Quantum-specific framework | UCIe mechanics repackaged as intelligence |

Gate 1 falsification must ask: did the **same method** (Architecture≠Authority, contradiction register, classified Unknowns) reveal a **new** boundary object — or only rename manageability features?

---

## 10. Change history

| Version | Date | Change |
|---|---|---|
| 1.0-draft | 2026-08-31 | Initial evidence ledger — repo only; no public surface |

---

## 11. Gate 1 falsification (pending)

**Status:** NOT YET RUN.

Run only after ledger review. Same vocabulary as Gate 0C: PASS / PASS WITH RESERVATION / FAIL → single **GATE 1 PASS** or **GATE 1 FAIL** decision.

If **FAIL:** narrow StreamCollider scope; do not publish SC-BIR-002 or admit advanced silicon by default.

If **PASS:** authorize public surface + machine-readable JSON under same rules as SC-BIR-001.

---

## 12. Research coupling (no production)

| Layer | Path |
|---|---|
| Dossier | `research/SC_BIR_002_BOUNDARY_INTELLIGENCE_RECORD.md` |
| Unknown ledger | `research/SC_BIR_002_UNKNOWN_CLOSURE_MATRIX.md` |
| Contradictions | `research/SC_CONTRADICTION_REGISTER.md` |
| Evidence matrix | `research/BOUNDARY_EVIDENCE_MATRIX_BIR_002.md` |
| Candidate screen | `research/GATE_1_ADVANCED_CHIP_CANDIDATE_SCREEN.md` |
| Machine-readable | `data/boundaries/sc-bir-002.json` |
