# SC-BIR-002 — Unknown Closure Matrix v0.1

**Record:** SC-BIR-002  
**Case:** SC-RC-002  
**Boundary:** Director-Managed Chiplet (UCIe 3.0 Manageability)  
**Status:** Evidence ledger complete — awaiting Gate 1 falsification  
**Last verified:** 2026-08-31

Claim classes: **D** Directly documented · **S** Cross-source synthesis · **I** StreamCollider interpretation · **U** Unknown · **A** Assumption

Central test: **deployment-level independent governance**, not protocol roles alone.

---

## U-01 — Deployment-level distinct governance

### Question
Do director and satellite chiplet represent **independently governed control authorities in deployment**, or only UCIe protocol roles under one SiP operator?

### Direct evidence
- UCIe 3.0 defines Director Chiplet responsibilities vs satellite chiplet wait/request behavior (SC-C002).
- Open chiplet ecosystem assumes dies from different vendors and integrators (SC-C001, SC-C002).
- Verification literature: chiplet supplier and system integrator must agree verification evidence / delivery contract; gaps appear at SiP integration (SC-C003).

### Cross-source evidence
- Gate 1 screen flagged **Partial→Strong** at protocol level, reservation at deployment level (GATE_1 screen).
- DEC-008: chiplet link alone does not admit collision.

### Contradictions
SC-CON-008, SC-CON-012.

### Known
Protocol assigns distinct **roles** (director initiates FW fabric; satellite waits). Multi-vendor SiP is an explicit ecosystem goal.

### Unknown
When integrator, director-vendor, and satellite-vendor are the same entity or under unified SiP policy, whether **governance** is non-singular or only **role separation** within one authority.

### Assumed
Director designation in a product diagram is not treated as proof of independent governance.

### Evidence Boundary
Public materials specify roles and interoperability goals; they do not publish a normative **deployment authority model** (integrator vs vendor vs director runtime).

### StreamCollider interpretation
This is the **Gate 1 kill question**. If U-01 collapses to “integrator always governs,” SC-BIR-002 fails as a generalization case.

### What evidence would close the unknown?
Documented cross-vendor SiP where director policy, satellite vendor FW policy, and integrator ops are **separably attributable** with conflict examples and audit paths.

### Classification
| Finding | Class |
|---|---|
| Protocol director/satellite roles | **D** |
| Multi-vendor ecosystem goal | **D** |
| Deployment-level independence | **U** |
| Role ≠ governance unless evidenced | **I** |
| **Primary for U-01** | **U** |

---

## U-02 — Firmware / MTP ownership

### Question
Who owns firmware image authority, staging, and management-transport ownership across director ↔ satellite?

### Direct evidence
- Director obtains firmware (e.g., external flash), initializes sideband network, downloads first mutable firmware; chiplet waits (SC-C002).
- Chiplet may request further updates via sideband/mainband using MCTP/PLDM-class flows (SC-C002).
- Management fabric defined with director, ports, elements, MCTP (SC-C002).

### Cross-source evidence
- Verification: security boundary, authorization, protected debug/management access required (SC-C003).
- Motivation: avoid every chiplet carrying own flash or implementing full MCTP/PLDM in immutable FW (SC-C002).

### Contradictions
SC-CON-009, SC-CON-010.

### Known
First mutable firmware path is **director-mediated** by design. Immutable vs mutable split is explicit.

### Unknown
Ownership when satellite vendor ships FW images but director selects/schedules; who may revoke staged images; audit join across vendor, director, and integrator.

### Assumed
Successful download does not equal ownership transfer of operational policy.

### Evidence Boundary
Spec defines flows; public brief does not assign **legal/operational owner** per image or MTP session.

### StreamCollider interpretation
MTP is a **boundary-crossing custody chain**, not a single owner.

### What evidence would close the unknown?
End-to-end custody model: who signs, stages, activates, revokes — with proof artifacts on both sides.

### Classification
| Finding | Class |
|---|---|
| Director-mediated first mutable download | **D** |
| MTP/MCTP-class update paths | **D** |
| Cross-party FW custody owner | **U** |
| **Primary for U-02** | **U** |

---

## U-03 — Authoritative configuration state

### Question
After partial firmware download or staged boot, which configuration state is **authoritative** — director view, chiplet local state, or integrator policy?

### Direct evidence
- Early FW download uses register mechanism / simple FSM on sideband; secure staging mentioned (SC-C002).
- Verification: “successful transfer is not enough if receiving chiplet starts from inconsistent configuration” (SC-C003).

### Cross-source evidence
- Priority sideband can interrupt “normal” management traffic (FW download/debug) — concurrent authority surfaces (SC-C002).

### Contradictions
SC-CON-010.

### Known
Inconsistent post-download configuration is a **recognized failure class** in verification guidance.

### Unknown
Normative precedence when director believes FW complete but chiplet reports partial/invalid state; authoritative state for runtime recalibration concurrent with management.

### Assumed
No hidden integrator-only state machine is treated as evidence.

### Evidence Boundary
Verification scenarios listed publicly; production authoritative-state contract not published.

### Classification
| Finding | Class |
|---|---|
| Inconsistent config is explicit risk | **D** |
| Authoritative state precedence | **U** |
| **Primary for U-03** | **U** |

---

## U-04 — Version mismatch authority

### Question
When firmware or capability versions disagree, who has authority to reject, defer, or force — and what proof crosses the boundary?

### Direct evidence
- Verification scenario table includes version mismatch: older/newer image, unsupported capability, explicit rejection (SC-C003).

### Cross-source evidence
- Interoperability failures from firmware versions and capability interpretation despite compliance (SC-C003).

### Contradictions
SC-CON-012.

### Known
Version mismatch handling is a **required verification surface**.

### Unknown
Cross-vendor normative rejection authority and operator-visible proof in production SiP.

### Assumed
Rejection in testbench ≠ closed operational governance.

### Evidence Boundary
Test scenarios documented; cross-party runtime contract absent in public pack.

### Classification
| Finding | Class |
|---|---|
| Version mismatch scenarios required in verification | **D** |
| Production rejection authority + proof | **U** |
| **Primary for U-04** | **U** |

---

## U-05 — Partial firmware-update recovery

### Question
Who owns recovery after interrupted or partial firmware update — retry, rollback, safe state, diagnostic visibility?

### Direct evidence
- Verification scenarios: interrupted transfer (reset, power, link error, timeout); recovery with retry, rollback, safe state (SC-C003).
- UCIe brief: chiplet can request further firmware update after first mutable boot (SC-C002).

### Cross-source evidence
- Delivery contract must include recovery behaviour or integration defects appear at SiP level (SC-C003).

### Contradictions
SC-CON-009.

### Known
Recovery is **multi-step and multi-party** in verification framing; not reducible to link-layer retry alone.

### Unknown
Authoritative recovery owner graph; proof that satellite reached safe state; integrator override paths.

### Assumed
Link-layer recovery ≠ management-action recovery.

### Evidence Boundary
Verification literature defines scenarios; standardized recovery **authority assignment** not in consortium brief.

### Classification
| Finding | Class |
|---|---|
| Recovery scenarios documented for verification | **D** |
| Recovery authority owner graph | **U** |
| **Primary for U-05** | **U** |

---

## U-06 — Emergency throttle / shutdown authority

### Question
When SiP-wide fast throttle or emergency shutdown fires, how does it interact with chiplet-local temperature sensing, mitigation, and execution state — and who proves override?

### Direct evidence
- Open-drain pins for SiP-wide simultaneous broadcast; fast throttle and emergency shutdown specified (SC-C002, SC-C005).
- Multi-vendor chiplets with **own** Tj limits and sensing; SiP must implement mitigation (SC-C005).
- Standard approach across vendors required for critical function interoperability (SC-C005).

### Cross-source evidence
- Priority sideband for low-latency events vs normal FW/debug traffic (SC-C002).

### Contradictions
SC-CON-011.

### Known
Package-level emergency control can **override** local timing assumptions by design intent.

### Unknown
Precedence when local chiplet mitigation conflicts with SiP-wide throttle; proof that satellite entered throttled/shutdown state; recovery authority after emergency.

### Assumed
Broadcast received ≠ provable local compliance without satellite-attested state.

### Evidence Boundary
Mechanisms documented; cross-domain proof contract open.

### Classification
| Finding | Class |
|---|---|
| SiP-wide throttle/shutdown mechanisms | **D** |
| Local vs package precedence + proof | **U** |
| **Primary for U-06** | **U** |

---

## U-07 — Director state vs chiplet-local state

### Question
If director management state and chiplet-local operational state disagree, which is authoritative for dispatch, debug, and recovery?

### Direct evidence
- Director initializes management network and drives FW sequencing; chiplet holds local bring-up domains (SC-C002).
- Verification: local PHY result can depend on firmware policy; recovery may preserve link while violating software assumptions (SC-C003).

### Cross-source evidence
- Analogous pattern to SC-BIR-001 U-02 (WLM vs provider state) at package scale — **I** cross-case synthesis.

### Contradictions
SC-CON-010, SC-CON-011.

### Known
Cross-layer state divergence is an explicit verification concern.

### Unknown
Universal precedence table for management vs local operational state.

### Assumed
Management transaction success on director side ≠ chiplet-local truth.

### Evidence Boundary
Same as U-03/U-08 — scenarios without normative precedence.

### Classification
| Finding | Class |
|---|---|
| Cross-layer state divergence documented | **S** |
| Precedence rule | **U** |
| Package-scale authority-state parallel to BIR-001 | **I** |
| **Primary for U-07** | **U** |

---

## U-08 — Proof after failed / interrupted management action

### Question
What evidence proves failure, safe abort, or completed recovery to **both** sides after an interrupted management action?

### Direct evidence
- Verification requires diagnostic visibility, safe state, failure reporting, security boundary (SC-C003).
- Delivery contract should include debug access and recovery behaviour (SC-C003).

### Cross-source evidence
- SC-BIR-001 U-04/U-05 pattern (cancel/recovery proof) at management plane — **I**.

### Contradictions
SC-CON-010.

### Known
Proof requirements exist in **verification / delivery-contract** framing.

### Unknown
Standardized dual-sided proof artifact in production (log join, attestation, rollback proof).

### Assumed
Director-side log alone is insufficient for audit.

### Evidence Boundary
Public pack defines what must be **tested**; not a shipped proof protocol.

### Classification
| Finding | Class |
|---|---|
| Verification proof requirements | **D** |
| Production dual-sided proof protocol | **U** |
| **Primary for U-08** | **U** |

---

## Closure summary

| ID | Question | Primary class | Residual |
|---|---|---|---|
| U-01 | Deployment-level distinct governance | **U** | integrator-unified vs independent |
| U-02 | Firmware / MTP ownership | **U** | custody chain |
| U-03 | Authoritative configuration state | **U** | precedence |
| U-04 | Version mismatch authority | **U** | rejection proof |
| U-05 | Partial-update recovery | **U** | owner graph |
| U-06 | Emergency throttle vs local state | **U** | precedence + proof |
| U-07 | Director vs chiplet-local state | **U** | precedence |
| U-08 | Proof after interrupted management | **U** | dual-sided artifact |

**Admission impact:** Distinct governance remains **CONDITIONAL** until U-01 is strengthened or Gate 1 falsification accepts protocol-role boundary as sufficient (unlikely without narrowing thesis).

**Next:** Gate 1 falsification — did this ledger generalize the method beyond SC-BIR-001?

**Forbidden:** public dossier, `site/` routes, ontology, SEO until Gate 1 PASS.
