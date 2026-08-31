# StreamCollider Boundary Intelligence Record — SC-BIR-001

**Title:** HPC Workload Manager ↔ Remote Quantum Resource Boundary  
**Record ID:** SC-BIR-001  
**Version:** 1.0-draft (Gate 0B)  
**Status:** EVIDENCE-BOUNDED  
**Case ID:** SC-RC-001  
**Last verified:** 2026-08-31  
**Public surface:** `/reference-case-001/`  
**Machine-readable:** [`/data/boundaries/sc-bir-001.json`](https://streamcollider.com/data/boundaries/sc-bir-001.json) (repo mirror: `data/boundaries/sc-bir-001.json`)

> This record is a sovereign, citable StreamCollider artifact. It is not a restatement of any single vendor, scheduler, or interface document.

---

## 1. Domains

| Side | Domain | Governance character |
|---|---|---|
| **A** | HPC workload management (Slurm / PBS / LSF / Grid Engine / Flux-class WLM) | Site scheduling, allocation, local job lifecycle, classical accounting |
| **B** | Remote / independently governed quantum resource (provider QPU, cloud quantum service, or site QPU under separate control plane) | Provider queue/session, calibration/maintenance, remote execution, provider credentials / billing |

**Boundary mechanism:** QRMI-class resource interface + WLM plugins/hooks + optional middleware / second-level scheduler mediating acquire–execute–release across independently governed domains.

---

## 2. Admission

| Condition | Result | Evidence basis |
|---|---|---|
| Distinct governance | **PASS** | WLM authority ≠ provider/control-plane authority (SC-S001, SC-S011, SC-S012) |
| Boundary crossing | **PASS** | Jobs, tokens, credentials, tasks, status, and release cross the interface |
| Mutual consequence | **PASS** | Provider queue/calibration alters classical utilization; WLM cancel/alloc alters remote demand |
| Negative control | **PASS** | Local owned/controlled resource under one queue can avoid the remote two-queue condition (SC-S011; Gate 0 note) |

---

## 3. Authority map

| Authority dimension | Domain A (WLM / site) | Domain B (remote quantum) | Boundary note |
|---|---|---|---|
| Scheduling | Batch queue, partitions, priorities | Provider queue and/or second-level middleware scheduler | Non-singular after remote admission (SC-CON-001) |
| Execution | Classical tasks within allocation | QPU task / session execution | Co-scheduling opacity |
| Resource | Nodes, GRES, licenses | QPU partitions, sessions, shots | Representation ≠ readiness (SC-CON-003) |
| State | Job/alloc state | Provider readiness / queue / calibration | No universal precedence (U-02) |
| Calibration / maintenance | Observes via plugins/daemons if wired | Owns physical/calibration control | Override authority open (U-03) |
| Recovery | Hooks, requeue, local cleanup | Session/task cleanup on provider | Fragmented (U-05) |
| Proof / accounting | sacct / qacct / site systems | Provider usage / cost / wait | Dual meters, open split (U-06) |
| Identity / security | HPC UID/project | Provider credentials / tokens | Model fork (U-07, SC-CON-007) |

---

## 4. Architecture says / Boundary intelligence asks

| Architecture says | Boundary intelligence asks |
|---|---|
| Slurm / WLM allocates a quantum resource | What remains outside WLM authority after allocation? |
| QRMI `acquire` succeeds | What exactly has been acquired — lock, session, queue admission, or token only? |
| QPU has state / accessibility methods | Who owns authoritative state when WLM and provider disagree? |
| Cancellation / job end exists | Who proves remote termination? |
| Accounting exists on both sides | Can both domains reconcile one evidence trail? |
| Credentials are configured | Which identity is authoritative under override, and can it be audited end-to-end? |
| Calibration is an operational concern | Who may revoke an allocation for calibration, and how is that proven to Domain A? |

This dual table is the difference between StreamCollider and vendor documentation.

---

## 5. Evidence Matrix (linked)

See `research/BOUNDARY_EVIDENCE_MATRIX_V0_2.md` and the full Unknown ledger in `research/SC_BIR_001_UNKNOWN_CLOSURE_MATRIX.md`.

| ID | Surface | Reading |
|---|---|---|
| B-001 | Queue authority after HPC admission | **Strong** — second queue / second-level scheduling is evidenced |
| B-002 | Acquire vs execution readiness | **Strong** — acquire ≠ readiness in general |
| B-003 | Calibration-driven availability | **Strong unresolved** — `is_accessible` gap; future `is_runnable` |
| B-004 | Authoritative state under disagreement | **Open** — no precedence contract |
| B-005 | Cancellation / partial failure | **Open** — APIs without complete proof/recovery graph |
| B-006 | Credentials / access authority | **Medium** — mechanisms yes; joint audit no |
| B-007 | Accounting / proof | **Strong unresolved** — dual surfaces; deferred responsibility |
| B-008 | Negative control | **Strong** — local owned/controlled path avoids remote two-queue |

---

## 6. Known / Unknown / Assumed

### Known
- Remote QPU integration can introduce a second queue outside classical scheduler direct visibility/control.
- `acquire` establishes access/session/token continuity; it is not portable proof of immediate execution readiness.
- Calibration and provider-side dynamics can invalidate WLM availability assumptions after allocation.
- Credential and accounting mechanisms exist in multiple distinct models; the current evidence pack does not establish a single interoperable authority or audit model.

### Unknown
- Authoritative-state precedence under disagreement (U-02).
- Calibration override owner and proof path (U-03).
- Remote cancellation termination proof (U-04).
- Partial-failure recovery authority graph (U-05).
- Single reconciled accounting trail and chargeable-time clock (U-06).
- Exact cross-vendor acquire rights floor; joint identity audit join keys (residual U-01 / U-07).

### Assumed
- No unpublished site-private production contract is treated as public evidence.
- Local WLM job end is not assumed to equal remote termination without provider-side evidence.

### Evidence Boundary
Public QRMI / OpenQSE / HPC-QC materials end before full cross-domain precedence, termination proof, recovery matrix, and reconciled accounting contracts.

---

## 7. Contradiction register (linked)

Full entries: `research/SC_CONTRADICTION_REGISTER.md`

| ID | Title | Status |
|---|---|---|
| SC-CON-001 | Single scheduler vs second queue | OPEN — SCOPED |
| SC-CON-002 | Acquire timing across WLMs | SCOPED |
| SC-CON-003 | GRES vs live readiness | OPEN |
| SC-CON-004 | `is_accessible` vs availability | OPEN |
| SC-CON-005 | Cancel vs termination proof | OPEN — EVIDENCE GAP |
| SC-CON-006 | Dual accounting without split | OPEN |
| SC-CON-007 | Admin vs user-scoped credentials | SCOPED |

---

## 8. Evidence gaps

1. Normative cross-backend semantics of `acquire`.
2. Authoritative-state precedence table.
3. Calibration interrupt protocol with WLM-visible proof.
4. Cancel → remote ACK → reconcile path.
5. Partial-failure recovery owner matrix.
6. Joinable accounting example across both domains.
7. End-to-end identity attribution example for cloud bursting.

---

## 9. Negative control

A quantum (or other) resource that is local, owned, and controlled under the same scheduling authority as the classical allocation can avoid the remote two-queue / independent-control condition. That configuration may still be operationally hard; it does not instantiate the same governance boundary under test.

---

## 10. Source register (this record)

Primary: SC-S001, SC-S002, SC-S003, SC-S006, SC-S010, SC-S011, SC-S012, SC-S014  
Supporting OpenQSE context: SC-S004, SC-S005, SC-S007, SC-S008, SC-S009  
Full list: `SOURCE_REGISTER.md`

---

## 11. Change history

| Version | Date | Change |
|---|---|---|
| 0.1 / 1.0-draft | 2026-08-31 | Gate 0B initial Boundary Intelligence Record from Reference Case 001 evidence pack |

---

## 12. Falsification result (Gate 0C pending)

**Status:** NOT YET RUN.

Gate 0C must ask only:

1. Did StreamCollider surface knowledge not obtainable by reading QRMI / OpenQSE / Pasqal materials each in isolation?
2. Did the governance-boundary method produce operationally useful Unknowns?
3. Did Known / Unknown / Assumed / Evidence Boundary improve understanding, or merely reorganize documentation?

Until Gate 0C completes: **no second proving domain**, **no category claim upgrade**, **no ontology expansion**.

---

## 13. Production coupling

| Layer | Path |
|---|---|
| Research dossier | `research/SC_BIR_001_BOUNDARY_INTELLIGENCE_RECORD.md` |
| Unknown ledger | `research/SC_BIR_001_UNKNOWN_CLOSURE_MATRIX.md` |
| Contradictions | `research/SC_CONTRADICTION_REGISTER.md` |
| Evidence matrix | `research/BOUNDARY_EVIDENCE_MATRIX_V0_2.md` |
| Public reference | `site/reference-case-001/` |
| Machine-readable | `site/data/boundaries/sc-bir-001.json` → https://streamcollider.com/data/boundaries/sc-bir-001.json |
