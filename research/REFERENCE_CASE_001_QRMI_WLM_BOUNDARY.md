# Reference Case 001 — WLM ↔ Remote Quantum Resource Boundary

**Case ID:** SC-RC-001
**Status:** IN PROGRESS

## Admission result

- Distinct governance: PASS
- Boundary crossing: PASS
- Mutual consequence: PASS
- Negative control: PASS

## Evidence-backed unknowns

1. What does `acquire` establish across implementations?
2. If WLM-visible availability and provider state disagree, which controls dispatch?
3. Who has final authority when calibration/maintenance conflicts with an allocation?
4. What proves that a remote task stopped after scheduler cancellation or timeout?
5. What is the recovery authority after partial failure?
6. Can one record reconcile allocated time, provider waiting, actual execution, retry/cancellation and cost?
7. How are HPC identity and provider credential authority joined and audited?

## Newly resolved points

- `acquire` cannot safely be treated as synonymous with execution readiness in the general case.
- The two-queue problem is governance-sensitive, not simply quantum-sensitive.
- Calibration availability remains an explicit unresolved state surface in QRMI's own future plan.

## Completion trigger

When all seven Unknowns receive a `D / S / I / U / A` classification and contradictions are explicitly recorded, Gate 0 must be re-evaluated before any second proving domain.
