# Boundary Evidence Matrix v0.1

| ID | Question | Current evidence reading |
|---|---|---|
| B-001 | Queue authority after HPC admission | Strong — remote QPU can introduce a second queue outside the classical scheduler's direct visibility/control. |
| B-002 | `acquire` vs execution readiness | Strong — acquisition cannot safely be treated as synonymous with immediate execution readiness in the general case. |
| B-003 | Calibration-driven availability | Strong unresolved surface — current QRMI material notes incomplete knowledge of when the resource becomes available again. |
| B-004 | Authoritative state under disagreement | Open — no complete cross-domain state-consistency contract in the current pack. |
| B-005 | Cancellation / partial failure | Open — API semantics exist, but complete cross-domain recovery proof does not. |
| B-006 | Credentials / access authority | Medium — mechanisms are described; complete authority model remains unresolved. |
| B-007 | Accounting / proof | Strong unresolved surface — operators request usage, cost and pending-time visibility. |
| B-008 | Negative control | Strong — a local owned/controlled resource can avoid the remote two-queue condition. |

## Preliminary originality surface

The contribution under test is treating unresolved **authority + state + proof + recovery** at independently governed boundaries as a first-class cross-source audit object.
