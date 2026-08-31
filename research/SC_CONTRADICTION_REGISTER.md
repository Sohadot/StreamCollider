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
| **Evidence available** | Direct enumeration of incompatible preferred models. |
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
