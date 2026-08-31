# Gate 1 — Advanced-Chip Candidate Admission Screen

**Date:** 2026-08-31  
**Status:** SCREEN COMPLETE — ONE CANDIDATE ADVANCES  
**Authorization:** Gate 0C PASS (DEC-012)  
**Rule:** Do not admit a chiplet, UCIe link, or package fabric by default (DEC-008). A candidate must survive the same three-part admission test **and** six screen criteria before any SC-BIR-002 dossier or public surface work begins.

## Purpose

Gate 1 tests whether StreamCollider’s boundary-intelligence method generalizes beyond HPC ↔ remote quantum. This document is **not** a proving dossier. It screens 3–5 real candidates and selects **at most one** to advance.

## Six screen criteria

| # | Criterion | Pass requires |
|---|---|---|
| 1 | **Distinct authority** | Side A and side B hold materially different control or governance — not merely different layers under one operator |
| 2 | **Boundary crossing** | Stream, state, firmware, control action, measurement, or policy crosses between domains |
| 3 | **Mutual consequence** | Each side can materially alter what the other can execute, schedule, interpret, prove, or recover |
| 4 | **Public auditable evidence** | Stable locators exist for independent audit (spec, paper, standards org — not slide-only) |
| 5 | **Non-trivial Unknown** | Residual authority/state/proof/recovery questions remain **beyond** restating protocol mechanics |
| 6 | **Negative control** | A configuration exists that avoids the boundary condition without denying the technology exists |

Screen verdicts: **HOLD** (do not advance) · **INVESTIGATE** (evidence gap; pack needed) · **ADVANCE** (authorized for SC-BIR-002 dossier on a later branch)

---

## Candidate screening matrix

| Candidate | Distinct authority | Crossing | Mutual consequence | Public evidence | Non-trivial Unknown | Negative control | Verdict |
|---|---:|---:|---:|---:|---:|---|---|
| **A. Director-managed chiplet boundary** (UCIe 3.0 MTP / sideband manageability) | Partial→Strong | Yes | Yes | Yes | Yes | Yes | **ADVANCE** |
| **B. Host ↔ independently managed accelerator** | Yes | Yes | Yes | Yes | Weak | Yes | **HOLD** |
| **C. Electronic ↔ photonic control boundary** | Unclear | Partial | Partial | Weak | Unclear | Partial | **HOLD** |
| **D. Compute ↔ independently managed memory / fabric** | Partial | Yes | Yes | Insufficient in pack | Possible | Partial | **INVESTIGATE** |
| **E. Package-level emergency throttle / shutdown** (open-drain broadcast) | Partial | Yes | Yes | Yes | Weak alone | Yes | **HOLD** |

---

## Candidate A — Director-managed chiplet boundary (UCIe 3.0)

**Boundary sketch:** Director chiplet (management authority) ↔ satellite chiplet(s) awaiting mutable firmware, sideband priority events, and system-wide throttle/shutdown signals.

### Why each criterion reads as it does

| Criterion | Reading | Evidence |
|---|---|---|
| Distinct authority | **Partial→Strong.** UCIe 3.0 defines Director vs chiplet roles: director obtains firmware, initializes sideband network, downloads first mutable firmware; chiplet waits, then may request further updates via sideband or mainband (MCTP/PLDM-class flows). Cross-vendor SiP may still unify policy at integrator level — dossier must test **deployment-level** independence, not protocol roles alone. | SC-C001; UCIe 3.0 specification materials |
| Crossing | **Yes.** Firmware images, management transport, priority sideband packets, open-drain emergency events cross the link. | SC-C001 |
| Mutual consequence | **Yes.** Chiplet cannot reach operational mutable firmware without director action; director boot/configuration depends on chiplet responses; fast throttle / emergency shutdown can override local chiplet execution assumptions. | SC-C001 |
| Public evidence | **Yes.** Stable consortium specification and public technical briefs. | [uciexpress.org/specifications](https://www.uciexpress.org/specifications) |
| Non-trivial Unknown | **Yes.** Spec and verification literature surface open surfaces: interrupted FW transfer recovery, version/capability mismatch rejection, authoritative configuration state after partial download, security/authorization boundary, emergency throttle vs chiplet-local execution state, ordering when one chiplet configures another. These are authority/state/proof questions, not link-speed mechanics. | SC-C001; verification notes on MTP recovery |
| Negative control | **Yes.** Monolithic die or single-package design with immutable/local firmware only (no director-mediated mutable download path) avoids the director↔satellite management boundary under test. | DEC-008 pattern |

### Reservation (mandatory for dossier)
UCIe alone does not prove a Stream Collision. Candidate A advances because **manageability roles create a consequential governance seam** with documented recovery and authority gaps — not because the interconnect exists.

### Verdict
**ADVANCE** → authorized next artifact: **SC-BIR-002 — Advanced-Chip Generalization Record** (separate branch; not in this PR)

---

## Candidate B — Host ↔ independently managed accelerator

| Criterion | Reading |
|---|---|
| Distinct authority | Host OS / hypervisor / site scheduler vs device firmware / internal accelerator scheduler — often **Yes** in production. |
| Crossing / consequence | **Yes** — allocation, execution, telemetry, reset, power. |
| Public evidence | Abundant vendor and datacenter literature. |
| Non-trivial Unknown | **Weak for Gate 1.** Operational models (GPU/IPU/BMC) are extensively documented; risk that SC-BIR-002 becomes reorganization of existing device-management docs without a new cross-source audit object. |
| Negative control | CPU-only or fully host-synchronous accelerator without independent execution authority. |

### Verdict
**HOLD** — valid boundary in industry, but poor Gate 1 falsification target given originality risk vs SC-BIR-001.

---

## Candidate C — Electronic ↔ photonic control boundary

| Criterion | Reading |
|---|---|
| Distinct authority | **Unclear** in current StreamCollider evidence pack. |
| Public evidence | **Weak** — imec / photonics context (SC-C003–C005) lacks durable locators in `SOURCE_REGISTER`. |
| Non-trivial Unknown | Cannot be asserted without auditable sources. |

### Verdict
**HOLD** — revisit only after locator-backed evidence pack is added.

---

## Candidate D — Compute ↔ independently managed memory / fabric domain

| Criterion | Reading |
|---|---|
| Distinct authority | **Partial** — CXL / fabric controllers can hold management authority distinct from host compute domain. |
| Crossing / consequence | Plausible for memory expansion, tiering, fabric policy. |
| Public evidence | **Insufficient in current pack** — no SC-C* locator set for CXL/fabric management authority comparable to SC-C001. |
| Non-trivial Unknown | Likely exists, but cannot be screened to **ADVANCE** without sources. |

### Verdict
**INVESTIGATE** — add locator-backed sources before re-screening; do not parallel SC-BIR-002.

---

## Candidate E — Package-level emergency throttle / shutdown (open-drain)

| Criterion | Reading |
|---|---|
| Distinct authority | **Partial** — package-wide broadcast authority vs chiplet-local execution. |
| Public evidence | **Yes** within UCIe 3.0 manageability (SC-C001). |
| Non-trivial Unknown | **Weak as standalone case** — throttle/shutdown is one control plane signal; deeper Unknowns (FW recovery, authoritative state) belong to Candidate A. |
| Negative control | System without package-wide emergency broadcast path. |

### Verdict
**HOLD** — treat as **in-scope sub-boundary** of Candidate A if SC-BIR-002 proceeds, not a second proving domain.

---

## Selection decision

| Outcome | Candidate |
|---|---|
| **ADVANCE (one only)** | **A — Director-managed chiplet boundary (UCIe 3.0 manageability)** |
| HOLD | B, C, E |
| INVESTIGATE (later) | D |

**No SC-BIR-002 dossier, public page, ontology, or SEO work in this PR.**

---

## Authorized next step (separate branch after merge)

Open dossier work as:

```text
SC-BIR-002 — Director-Managed Chiplet Boundary (UCIe 3.0 Manageability)
```

Minimum dossier contents (future PR):

- Domains A/B with explicit governance characterization (director vs satellite; integrator vs vendor where evidenced)
- Architecture ≠ Authority dual table
- Unknown Closure Matrix (new U-IDs)
- Contradiction Register entries
- Negative control
- Evidence pack with stable locators (extend `SOURCE_REGISTER` SC-C* first)
- Gate 1 falsification section — did the method generalize or only fit quantum/HPC?

If SC-BIR-002 fails falsification, **narrow scope** — do not force advanced silicon into the framework.

---

## Explicit non-actions

- No admission of “UCIe” or “chiplet” as a Stream Collision by name
- No `/reference-case-002/` or other new public routes yet
- No machine-readable JSON until evidence ledger exists
- No category-wide heterogeneous-compute claim until Gate 1 falsification passes
