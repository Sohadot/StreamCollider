# SC-BIR-001 — Unknown Closure Matrix v0.1

**Record:** SC-BIR-001  
**Case:** SC-RC-001  
**Boundary:** HPC Workload Manager ↔ Remote Quantum Resource  
**Status:** Evidence ledger complete — awaiting Gate 0C re-evaluation  
**Last verified:** 2026-08-31

Claim classes: **D** Directly documented · **S** Cross-source synthesis · **I** StreamCollider interpretation · **U** Unknown · **A** Assumption

Each Unknown below is classified. Classification does **not** mean the Unknown is solved. It means StreamCollider states what the evidence pack presently supports, what it does not, and what would close the gap.

---

## U-01 — Acquire semantics

### Question
What does `acquire` establish across implementations?

### Direct evidence
- QRMI lifecycle is documented as acquire → task execution → release; `acquire` is called before job execution to reserve / lock / session-bind a quantum resource and returns an acquisition token required for later release. (SC-S011, SC-S012)
- Slurm SPANK integration acquires during job setup (`slurm_spank_init_post_opt`), exposes metadata during task init, and releases at exit. (SC-S012 / SC-S003)
- PBS runjob hook can acquire **before** compute-node allocation; inaccessible resources leave the job pending rather than occupying classical nodes. (SC-S012)

### Cross-source evidence
- Pasqal / Wennersteen middleware places a second scheduling layer between Slurm and the QPU; acquisition of access through QRMI does not by itself exhaust scheduling authority. (SC-S001, SC-S014)
- Fluence / Flux experiments treat quantum queue waiting as opaque to classical dispatch timing. (SC-S012, SC-S002)

### Contradictions
See **SC-CON-002** (acquire timing across WLMs) and **SC-CON-001** (single-scheduler claim vs second scheduler).

### Known
`acquire` establishes access / reservation / session / token continuity for a subsequent execution path. It cannot safely be treated as synonymous with immediate execution readiness in the general case.

### Unknown
Whether every QRMI backend treats successful `acquire` as exclusive lock, soft reservation, session open, or provider-queue admission; public materials do not publish a single normative semantic floor across vendors.

### Assumed
No hidden production contract redefines `acquire` beyond published lifecycle descriptions.

### Evidence Boundary
Public papers and OpenQSE materials describe lifecycle hooks and tokens. They do not publish a complete cross-provider formal semantics for what rights `acquire` confers under calibration, maintenance, or multi-tenant preemption.

### StreamCollider interpretation
`acquire` is a **boundary-crossing authority act**, not a readiness proof. Architecture diagrams that place acquire next to “ready to run” overclaim unless readiness is separately evidenced.

### What evidence would close the unknown?
A normative cross-implementation matrix: for each backend, rights conferred by acquire, exclusivity, preemption rules, interaction with provider queues, and failure modes when acquire succeeds but execution cannot start.

### Classification
| Finding | Class |
|---|---|
| Acquire precedes task execution and returns a release token | **D** |
| Acquire timing differs across WLM integrations (Slurm vs PBS) | **S** |
| Acquire ≠ execution readiness in the general case | **S** |
| Exact cross-vendor rights floor of acquire | **U** |
| No unpublished production override assumed | **A** |
| **Primary classification for U-01** | **S** (with residual **U**) |

---

## U-02 — Authoritative state

### Question
If Slurm / WLM-visible state and provider state disagree, which governs dispatch?

### Direct evidence
- Slurm GRES integration can treat a quantum resource as always available; if the resource is unavailable after HPC allocation, classical resources may idle. (SC-S012)
- Dynamic License / daemon polling is proposed to reflect availability, but the daemon approach has an acknowledged race where license count may not match actual status. (SC-S012)
- PBS and LSF expose dynamic-resource / ELIM patterns that attempt to feed availability into scheduling; support remains partial across WLMs. (SC-S012)
- Fluence monitors quantum queue depth and gates classical workers to avoid idle classical allocation under opaque quantum waiting. (SC-S012, SC-S002)

### Cross-source evidence
- Production HPC centers prefer a single WLM to avoid multi-queue operational overhead; remote quantum access reintroduces an external queue / session model. (SC-S011, SC-S006)
- Second-level / middleware schedulers intentionally hold QPU-side prioritization outside the first-level batch scheduler. (SC-S001, SC-S014)

### Contradictions
**SC-CON-001**, **SC-CON-003**.

### Known
No complete cross-domain state-consistency contract is published in the current pack. When observations diverge, dispatch behavior is implementation-specific and can leave classical resources idle or depend on external polling with race conditions.

### Unknown
Which observation is authoritative under disagreement: WLM allocation state, QRMI accessibility, provider queue/session state, middleware daemon state, or operator override.

### Assumed
No site-private reconciliation protocol is treated as public evidence.

### Evidence Boundary
Materials describe mismatch and mitigations (licenses, hooks, queue-depth monitoring). They do not define a universal authoritative-state precedence rule.

### StreamCollider interpretation
Authoritative state is the core unresolved governance object of this boundary. The absence of a precedence rule is itself the finding.

### What evidence would close the unknown?
An explicit precedence / conflict-resolution contract covering WLM state, QRMI methods, provider APIs, middleware daemons, and operator freeze/maintenance, with observed disagreement test cases.

### Classification
| Finding | Class |
|---|---|
| GRES can assume always-available; idle classical cost on mismatch | **D** |
| Dynamic license polling can race actual status | **D** |
| No published universal precedence rule | **U** |
| Authoritative-state gap is the primary audit object | **I** |
| **Primary classification for U-02** | **U** |

---

## U-03 — Calibration authority

### Question
Who has final authority when calibration / maintenance conflicts with an allocation?

### Direct evidence
- Quantum resources are “not always available due to calibration requirements” and are “usually governed by provider-specific queueing and session models.” (SC-S012)
- QRMI `is_accessible()` “does not reflect availability”; community is considering `is_runnable()` with estimated start time. (SC-S012)
- Calibration drift is treated as a temporal validity problem for program portability at execution time. (SC-S001)
- Second-level Pasqal scheduler roadmap includes calibration-aware scheduling and operational constraints not expressible in first-level batch scheduling alone. (SC-S014)

### Cross-source evidence
- Operator monitoring literature and OpenQSE materials treat QPU health, maintenance, and calibration as distinct from classical node stability. (SC-S001, SC-S006)

### Contradictions
**SC-CON-004** (accessibility method vs availability semantics).

### Known
Calibration / maintenance can invalidate scheduler assumptions after allocation. Current QRMI accessibility primitives do not fully encode dynamic availability or return-to-service timing.

### Unknown
Who may revoke, pause, or override an already-acquired allocation for calibration: provider control plane, site middleware, WLM, or joint policy — and how that revocation is proven to the classical side.

### Assumed
Calibration is not assumed to be subordinated to Slurm allocation merely because a GRES was granted.

### Evidence Boundary
Future-plan language (`is_runnable`, calibration-aware second-level scheduling) is evidence of an open surface, not of a closed authority model.

### StreamCollider interpretation
Calibration authority is a **provider-side / control-plane authority** that can remain outside WLM sovereignty after allocation. Architecture that shows “QPU allocated” without a calibration override path is incomplete.

### What evidence would close the unknown?
Documented override precedence, notification path to WLM/middleware, user-visible state transitions, and accounting consequences when calibration interrupts an allocation.

### Classification
| Finding | Class |
|---|---|
| Calibration can make resources unavailable after scheduler assumptions | **D** |
| `is_accessible` does not reflect availability | **D** |
| Final override authority under conflict | **U** |
| Calibration remains outside pure WLM sovereignty after allocation | **I** |
| **Primary classification for U-03** | **U** |

---

## U-04 — Cancellation proof

### Question
What proves that a remote task stopped after scheduler cancellation or timeout?

### Direct evidence
- Lifecycle materials emphasize acquire / task_start / task_status / task_result / release. Public descriptions focus on start and result retrieval more than cross-domain termination proof. (SC-S011, SC-S012)
- Middleware session / priority models include preemption of lower-priority jobs by production jobs in design intent; initial implementations may approximate sharing rather than hard preemption. (SC-S001)

### Cross-source evidence
- Classical WLM cancellation ends local job control; remote provider execution may continue under provider session semantics unless an explicit remote cancel path is invoked and acknowledged.

### Contradictions
None recorded as direct textual conflict; gap is absence rather than clash → **SC-CON-005** (architecture implies cancel completeness; evidence shows API surface without proof contract).

### Known
Cancellation / timeout APIs and hooks exist in WLM space. Complete cross-domain proof that the remote task has terminated is not established in the current pack.

### Unknown
What observation constitutes termination proof: local hook success, QRMI release, provider cancel ACK, session close, or absence of further billing/queue presence.

### Assumed
Local WLM job end is **not** assumed to equal remote termination without provider-side evidence.

### Evidence Boundary
No published end-to-end cancel→ACK→reconcile contract across WLM + QRMI + provider control plane is in the pack.

### StreamCollider interpretation
Cancellation without remote proof is a **proof-authority gap**. The classical side can know it stopped asking; it may not know the remote side stopped executing.

### What evidence would close the unknown?
A falsifiable cancel protocol: initiator, transport, provider ACK, timeout on missing ACK, and reconciliation into both accounting systems.

### Classification
| Finding | Class |
|---|---|
| Local cancel/lifecycle hooks exist | **D** |
| Complete remote termination proof missing from pack | **U** |
| Local end ≠ remote end without provider evidence | **A** (working assumption) / **I** |
| **Primary classification for U-04** | **U** |

---

## U-05 — Partial-failure recovery

### Question
What is the recovery authority after partial failure?

### Direct evidence
- PBS inaccessible-acquire path rejects before classical allocation; Slurm SPANK acquire-during-setup can leave classical resources held while quantum side fails readiness. (SC-S012)
- Dynamic license race can desynchronize availability representation and actual status. (SC-S012)
- Two-queue opacity creates classical idle / wasted allocation under conservative co-start. (SC-S012, SC-S002)

### Cross-source evidence
- Multi-stakeholder deployments (site admins, HPC-QC team, vendor) surface operational recovery complexity beyond a single plugin. (SC-S012 CINECA notes)

### Contradictions
**SC-CON-002** (recoverability differs by when acquire runs).

### Known
Failure modes are documented asymmetrically: some WLM integrations avoid classical idle on acquire failure; others do not. No single recovery authority graph is published.

### Unknown
After partial failure (classical allocated / quantum not ready; quantum running / classical cancelled; middleware crash mid-session), who owns rollback, retry, compensation, and user-visible status.

### Assumed
No automatic cross-domain saga / transaction manager is assumed to exist unless evidenced.

### Evidence Boundary
Case studies describe problems and local mitigations; they do not publish a complete recovery-authority matrix.

### StreamCollider interpretation
Recovery authority is fragmented across WLM hooks, QRMI release, provider session control, and human operators. Fragmentation is the governance fact.

### What evidence would close the unknown?
A recovery matrix of partial-failure scenarios with owner, action, proof artifact, and user-visible outcome for each side.

### Classification
| Finding | Class |
|---|---|
| Acquire placement changes failure blast radius | **S** |
| Complete recovery-authority graph absent | **U** |
| Recovery is multi-party, not plugin-local | **I** |
| **Primary classification for U-05** | **U** |

---

## U-06 — Accounting / evidence reconciliation

### Question
Can one record reconcile allocated time, provider waiting, actual execution, retry/cancellation, and cost?

### Direct evidence
- Both QRMI and WLMs can expose discovery/accounting information; “the challenge is defining the responsibilities of QRMI and the workload managers. This challenge is out of scope for this paper.” (SC-S012)
- Grid Engine integration writes QRMI accounting fields into job usage data for `qacct`-style tools. (SC-S012)
- Future QRMI work calls for technology-aware usage abstractions associating records with users, projects, and allocations without exposing provider credentials. (SC-S012)
- Operators care about usage, cost, and pending-time visibility (matrix B-007; SC-S006 / SC-S010 context).

### Cross-source evidence
- Second-level queue waiting is not identical to Slurm pending or to provider billing time; three clocks can diverge. (SC-S001, SC-S012)

### Contradictions
**SC-CON-006**.

### Known
Accounting surfaces exist on both sides. A single reconciled evidence trail covering allocation, provider wait, execution, retry/cancel, and cost is not demonstrated as a closed contract in the current pack.

### Unknown
Canonical join key across WLM job ID, QRMI acquisition token, provider task/session ID, and billing record — and which clock is authoritative for chargeable time.

### Assumed
Presence of metrics APIs is not treated as presence of reconciled audit proof.

### Evidence Boundary
Responsibility split between QRMI and WLM accounting is explicitly deferred in published QRMI examination material.

### StreamCollider interpretation
Accounting without joinable evidence is **proof without authority**. Boundary intelligence requires one trail, not two dashboards.

### What evidence would close the unknown?
A worked reconciliation example with IDs, timestamps, wait vs run vs cancel, and matching cost fields across both domains for the same hybrid job.

### Classification
| Finding | Class |
|---|---|
| Dual accounting surfaces exist; responsibility split open | **D** |
| Single reconciled trail not evidenced | **U** |
| Metrics ≠ audit proof | **I** |
| **Primary classification for U-06** | **U** |

---

## U-07 — Identity / credential continuity

### Question
How are HPC identity and provider credential authority joined and audited?

### Direct evidence
- QRMI “does not dictate how credentials are managed”; admin file, user env vars, or user home files are all possible. (SC-S012)
- Default convenience path places credentials in administrator-owned `qrmi_config.json` and environment variables; adversarial multi-tenant settings need stronger models. (SC-S012)
- Pasqal-local QRMI can use MUNGE tokens scoped to the cluster, mapping to Linux UID as access-control source of truth — no credentials in `qrmi_config.json`. (SC-S012)
- Fluence keeps credentials owned by and scoped to the application user, not in system space. (SC-S012)
- Users may override system-wide credentials with their own. (SC-S011)

### Cross-source evidence
- Session tokens from middleware daemons create an additional identity surface between HPC user identity and provider auth. (SC-S001)

### Contradictions
**SC-CON-007** (admin-central credentials vs user-scoped credentials).

### Known
Multiple viable credential models exist. Mechanisms are described. A complete joint audit model linking HPC identity ↔ middleware session ↔ provider credential use is not standardized in the pack.

### Unknown
Who is the authority of record for access decisions under override; how credential use is attributable in provider logs back to HPC project/allocation; continuity across acquire/release and cancel.

### Assumed
Site security policy chooses a model; StreamCollider does not assume one model is universal.

### Evidence Boundary
Published material enumerates options and one strong on-prem pattern (MUNGE/UID). It does not close cloud-provider identity join/audit for all deployments.

### StreamCollider interpretation
Identity continuity is a **cross-domain authority seam**. Without joinable identity evidence, responsibility after incident or cost dispute cannot be adjudicated from one side alone.

### What evidence would close the unknown?
An end-to-end attribution example: HPC user/project → WLM job → QRMI acquire token → provider principal → cancel/release → audit records on both sides.

### Classification
| Finding | Class |
|---|---|
| Multiple credential models documented | **D** |
| Complete joint audit model not standardized | **U** |
| Identity seam is governance-critical | **I** |
| **Primary classification for U-07** | **S** (mechanisms) / residual **U** (joint audit) |

---

## Closure summary

| ID | Question | Primary class | Residual gap |
|---|---|---|---|
| U-01 | Acquire semantics | **S** | Exact cross-vendor rights floor (**U**) |
| U-02 | Authoritative state | **U** | Precedence contract |
| U-03 | Calibration authority | **U** | Override owner + proof |
| U-04 | Cancellation proof | **U** | Remote termination ACK |
| U-05 | Partial-failure recovery | **U** | Recovery-authority matrix |
| U-06 | Accounting reconciliation | **U** | Single evidence trail |
| U-07 | Identity / credential continuity | **S** | Joint audit join keys (**U**) |

**Completion trigger status:** All seven Unknowns now carry explicit `D/S/I/U/A` classifications and residual gaps. Contradictions are recorded in `research/SC_CONTRADICTION_REGISTER.md`.

**Mandatory next step:** Gate 0C — re-evaluate Gate 0 against SC-BIR-001. No second proving domain authorized.
