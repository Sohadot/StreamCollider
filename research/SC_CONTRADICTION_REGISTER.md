# StreamCollider Contradiction Register v0.1

**Scope:** Contradictions and architecture/evidence tensions surfacing from Reference Case 001 / SC-BIR-001.  
**Rule:** StreamCollider records contradictions; it does not silently reconcile them into a preferred vendor narrative.  
**Status:** Living register — entries may move from OPEN → SCOPED → RESOLVED only with dated evidence.

Claim classes on consequences use the SOURCE_REGISTER vocabulary (D / S / I / U / A).

---

## SC-CON-001 — Single scheduler posture vs second-level / provider queue

| Field | Content |
|---|---|
| **ID** | SC-CON-001 |
| **Claim A** | Production HPC centers typically rely on a single workload management system to coordinate all resources, avoiding multiple scheduling layers / queues. (SC-S011) |
| **Claim B** | Remote QPU integration and HPC-QC middleware introduce a second queue and/or second-level scheduler between the batch scheduler and the QPU / provider. (SC-S001, SC-S012, SC-S014, SC-S002) |
| **Scope difference** | Claim A describes institutional preference / operational norm for classical HPC. Claim B describes what remote / independently governed quantum access forces back into the stack. |
| **Evidence available** | Direct documentation on both sides; Fluence “two-queue problem”; Pasqal second-level scheduler; QRMI examination of opaque quantum waiting. |
| **Resolution status** | **OPEN — SCOPED.** Not a documentation error. Distinct scopes: desired classical posture vs forced boundary condition. |
| **Boundary consequence** | Queue authority after HPC admission is non-singular. This is a Stream Collision admission signal, not a bug in wording. (**I**) |

---

## SC-CON-002 — Acquire-before-allocation vs acquire-during-execution-setup

| Field | Content |
|---|---|
| **ID** | SC-CON-002 |
| **Claim A** | Slurm SPANK QRMI path acquires during job setup after scheduling decisions that may already reserve classical resources; unavailable quantum resources can leave HPC resources idle. (SC-S012) |
| **Claim B** | PBS runjob hook can acquire before compute allocation; inaccessible quantum resource rejects/pends without classical idle cost. (SC-S012) |
| **Scope difference** | Same interface family (QRMI), different WLM lifecycle insertion points. |
| **Evidence available** | Direct comparative documentation in QRMI multi-WLM examination. |
| **Resolution status** | **SCOPED.** Both true; semantics of “acquired” and failure blast radius are WLM-relative. |
| **Boundary consequence** | `acquire` is not a portable readiness or safety proof across implementations. Supports U-01 / U-05. (**S**) |

---

## SC-CON-003 — Schedulable GRES abstraction vs dynamic provider readiness

| Field | Content |
|---|---|
| **ID** | SC-CON-003 |
| **Claim A** | Quantum resources are represented as first-class schedulable resources (e.g., Slurm GRES) inside the WLM. (SC-S011, SC-S012) |
| **Claim B** | Slurm does not support updating custom GRES status for provider-side readiness/queue changes; QRMI-Slurm may assume GRES always available. (SC-S012) |
| **Scope difference** | Claim A is architectural representation. Claim B is runtime authority / state fidelity. |
| **Evidence available** | Direct; mitigations (dynamic licenses, ELIM, server_dyn_res) are partial and can race. |
| **Resolution status** | **OPEN.** Mitigations exist; no universal fidelity contract. |
| **Boundary consequence** | Architecture says “scheduled resource”; boundary intelligence asks “who owns live readiness state?” (**I**) |

---

## SC-CON-004 — `is_accessible` naming vs availability semantics

| Field | Content |
|---|---|
| **ID** | SC-CON-004 |
| **Claim A** | QRMI exposes `is_accessible()` as a quantum resource method usable in lifecycle checks. (SC-S012) |
| **Claim B** | `is_accessible()` does not reflect availability; community considering `is_runnable()` for estimated start. (SC-S012) |
| **Scope difference** | Method existence vs semantic coverage of calibration/queue readiness. |
| **Evidence available** | Direct in QRMI examination. |
| **Resolution status** | **OPEN — acknowledged semantic gap.** |
| **Boundary consequence** | Accessibility checks can create false confidence about dispatchability. Feeds U-02 / U-03. (**D** on gap; **U** on successor semantics) |

---

## SC-CON-005 — Cancellation surface vs termination proof

| Field | Content |
|---|---|
| **ID** | SC-CON-005 |
| **Claim A** | Architecture and WLM lifecycle imply jobs can be cancelled / completed with release of quantum resources. (SC-S011, SC-S012) |
| **Claim B** | Current evidence pack does not supply a cross-domain proof artifact that remote execution has stopped after local cancel/timeout. (U-04 ledger) |
| **Scope difference** | Control API existence vs evidentiary completeness. |
| **Evidence available** | Lifecycle APIs documented; proof contract absent. |
| **Resolution status** | **OPEN — EVIDENCE GAP.** |
| **Boundary consequence** | Release/cancel without remote ACK is incomplete proof authority. (**U**) |

---

## SC-CON-006 — Dual accounting without defined responsibility split

| Field | Content |
|---|---|
| **ID** | SC-CON-006 |
| **Claim A** | QRMI provides accounting information; WLMs provide accounting information; some integrations write QRMI fields into job usage. (SC-S012) |
| **Claim B** | Defining responsibilities between QRMI and WLM accounting is explicitly out of scope in the multi-WLM examination; reconciled wait/run/cancel/cost trail not closed. (SC-S012; U-06) |
| **Scope difference** | Capability presence vs authority assignment. |
| **Evidence available** | Direct statement of deferred responsibility. |
| **Resolution status** | **OPEN.** |
| **Boundary consequence** | Two meters without a join contract cannot adjudicate chargeable time across the boundary. (**D**/**U**) |

---

## SC-CON-007 — Administrator-central credentials vs user-scoped credentials

| Field | Content |
|---|---|
| **ID** | SC-CON-007 |
| **Claim A** | Default / convenient QRMI deployments place credentials in administrator-managed config and environment channels. (SC-S012) |
| **Claim B** | Stronger multi-tenant patterns keep credentials user-scoped (Fluence) or map cluster identity via MUNGE/UID without config credentials (pasqal-local). (SC-S012) |
| **Scope difference** | Deployment convenience vs adversarial multi-tenant security posture; on-prem vs cloud bursting. |
| **Evidence available** | Direct enumeration of distinct preferred credential models. |
| **Resolution status** | **SCOPED — model fork, not factual error.** |
| **Boundary consequence** | Identity/credential continuity cannot be described as a single architecture; audit join differs by model. Feeds U-07. (**S**) |

---

## Register index

| ID | Title | Status |
|---|---|---|
| SC-CON-001 | Single scheduler vs second queue / second-level scheduler | OPEN — SCOPED |
| SC-CON-002 | Acquire timing across WLMs | SCOPED |
| SC-CON-003 | GRES representation vs live readiness | OPEN |
| SC-CON-004 | `is_accessible` vs availability | OPEN |
| SC-CON-005 | Cancel surface vs termination proof | OPEN — EVIDENCE GAP |
| SC-CON-006 | Dual accounting without responsibility split | OPEN |
| SC-CON-007 | Admin-central vs user-scoped credentials | SCOPED |

**Falsification note for Gate 0C:** If these contradictions collapse into ordinary single-document clarifications with no residual cross-domain authority gap, StreamCollider must revise the originality claim before expansion.

---

## SC-BIR-002 scope (director-managed chiplet)

---

## SC-CON-008 — Open multi-vendor ecosystem vs integrator-unified SiP policy

| Field | Content |
|---|---|
| **ID** | SC-CON-008 |
| **Claim A** | UCIe targets open chiplet ecosystem — dies from different vendors, assemblies, process nodes (SC-C001, SC-C002). |
| **Claim B** | Verification literature: system integrator and chiplet supplier must agree delivery contract; integration defects arise from incompatible assumptions about firmware ownership, timeouts, recovery (SC-C003). |
| **Scope difference** | Ecosystem openness vs operational unification under one SiP integrator. |
| **Evidence available** | Direct on both sides. |
| **Resolution status** | **OPEN — SCOPED.** Multi-vendor ≠ independent governance by default. |
| **Boundary consequence** | U-01 remains open. Feeds admission CONDITIONAL status. (**I**) |

---

## SC-CON-009 — Director as optional role vs mandatory manageability hub

| Field | Content |
|---|---|
| **ID** | SC-CON-009 |
| **Claim A** | UCIe 3.0 early FW download flow centers **Director Chiplet** obtaining FW and downloading to satellites (SC-C002). |
| **Claim B** | Deployments may assign director/anchor differently; manageability topology is integrator-configurable; not every SiP uses identical director semantics in production. |
| **Scope difference** | Normative reference flow vs deployment topology flexibility. |
| **Evidence available** | Spec brief + verification integrator/supplier contract framing. |
| **Resolution status** | **SCOPED.** |
| **Boundary consequence** | Recovery and MTP ownership (U-02, U-05) vary by topology assignment. (**S**) |

---

## SC-CON-010 — Successful FW transfer vs authoritative safe configuration

| Field | Content |
|---|---|
| **ID** | SC-CON-010 |
| **Claim A** | Director downloads first mutable firmware; chiplet boots mutable firmware (SC-C002). |
| **Claim B** | Verification: successful transfer insufficient if chiplet starts from inconsistent configuration; partial/interrupted transfer scenarios required (SC-C003). |
| **Scope difference** | Transfer completion vs operational authority/state validity. |
| **Evidence available** | Direct. |
| **Resolution status** | **OPEN — EVIDENCE GAP.** |
| **Boundary consequence** | Feeds U-03, U-07, U-08. (**D** on gap; **U** on production proof) |

---

## SC-CON-011 — SiP-wide emergency throttle vs chiplet-local Tj authority

| Field | Content |
|---|---|
| **ID** | SC-CON-011 |
| **Claim A** | Fast throttle / emergency shutdown broadcast SiP-wide via open-drain; standard cross-vendor approach required (SC-C002, SC-C005). |
| **Claim B** | Each chiplet has own Tj limits, sensing error bars, and local mitigation responsibilities (SC-C005). |
| **Scope difference** | Package broadcast authority vs local thermal governance. |
| **Evidence available** | Direct in UCIe manageability materials. |
| **Resolution status** | **OPEN.** |
| **Boundary consequence** | Precedence and proof when local and SiP-wide mitigation diverge (U-06). (**S**) |

---

## SC-CON-012 — Compliance vs multi-vendor interoperability

| Field | Content |
|---|---|
| **ID** | SC-CON-012 |
| **Claim A** | UCIe provides compliance mechanisms and standardized requirements (SC-C001). |
| **Claim B** | Verification literature: compliance does not guarantee interoperability; failures from firmware policy, capability interpretation, recovery behaviour (SC-C003). |
| **Scope difference** | Conformance testing vs deployment authority/recovery reality. |
| **Evidence available** | Direct statement in verification analysis. |
| **Resolution status** | **SCOPED — widely acknowledged.** |
| **Boundary consequence** | Version mismatch and recovery Unknowns (U-04, U-05) cannot be closed by compliance alone. (**D**/**S**) |

---

## Register index (BIR-002 additions)

| ID | Title | Status |
|---|---|---|
| SC-CON-008 | Multi-vendor ecosystem vs integrator-unified policy | OPEN — SCOPED |
| SC-CON-009 | Director reference flow vs deployment topology | SCOPED |
| SC-CON-010 | FW transfer success vs safe configuration | OPEN — EVIDENCE GAP |
| SC-CON-011 | SiP-wide throttle vs local Tj authority | OPEN |
| SC-CON-012 | Compliance vs interoperability | SCOPED |

**Falsification note for Gate 1:** If SC-BIR-002 contradictions collapse into spec feature lists with no residual authority gap, Gate 1 must FAIL and scope narrows to HPC–QPU only.
