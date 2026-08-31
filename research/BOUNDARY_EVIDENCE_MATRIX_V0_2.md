# Boundary Evidence Matrix v0.2

**Record link:** SC-BIR-001  
**Supersedes:** v0.1 reading retained as lineage; classifications now tied to Unknown Closure Matrix.

| ID | Question | Current evidence reading | Linked Unknown | Class signal |
|---|---|---|---|---|
| B-001 | Queue authority after HPC admission | Strong — remote QPU can introduce a second queue / second-level scheduler outside the classical scheduler's direct visibility/control. | U-02 / SC-CON-001 | **S** |
| B-002 | `acquire` vs execution readiness | Strong — acquisition cannot safely be treated as synonymous with immediate execution readiness in the general case; acquire timing and blast radius vary by WLM. | U-01 / SC-CON-002 | **S** |
| B-003 | Calibration-driven availability | Strong unresolved surface — `is_accessible` does not reflect availability; return-to-service / override authority incomplete. | U-03 / SC-CON-004 | **U** |
| B-004 | Authoritative state under disagreement | Open — no complete cross-domain state-consistency / precedence contract in the current pack. | U-02 / SC-CON-003 | **U** |
| B-005 | Cancellation / partial failure | Open — API/lifecycle semantics exist; complete cross-domain termination proof and recovery-authority graph do not. | U-04 / U-05 / SC-CON-005 | **U** |
| B-006 | Credentials / access authority | Medium — multiple mechanisms described (admin config, user env, MUNGE/UID, user-scoped); joint audit model unresolved. | U-07 / SC-CON-007 | **S**/**U** |
| B-007 | Accounting / proof | Strong unresolved surface — dual accounting surfaces; responsibility split deferred; reconciled trail not evidenced. | U-06 / SC-CON-006 | **U** |
| B-008 | Negative control | Strong — a local owned/controlled resource can avoid the remote two-queue condition. | Admission | **D** |

## Preliminary originality surface

The contribution under test is treating unresolved **authority + state + proof + recovery** at independently governed boundaries as a first-class cross-source audit object — materialized here as SC-BIR-001, not as a vendor summary.

## Gate coupling

- Gate 0B: SC-BIR-001 dossier + Unknown classifications + Contradiction Register — **this revision**.
- Gate 0C: falsification / re-evaluation — **pending**.
- Expansion lock remains: no second proving domain before Gate 0C PASS.
