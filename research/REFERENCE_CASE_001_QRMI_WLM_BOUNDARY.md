# Reference Case 001 — WLM ↔ Remote Quantum Resource Boundary

**Case ID:** SC-RC-001  
**Sovereign record:** [SC-BIR-001](./SC_BIR_001_BOUNDARY_INTELLIGENCE_RECORD.md)  
**Status:** EVIDENCE LEDGER COMPLETE — AWAITING GATE 0C RE-EVALUATION  
**Last verified:** 2026-08-31

## Admission result

- Distinct governance: PASS
- Boundary crossing: PASS
- Mutual consequence: PASS
- Negative control: PASS

## Evidence-backed unknowns (classified)

Full ledger: [`SC_BIR_001_UNKNOWN_CLOSURE_MATRIX.md`](./SC_BIR_001_UNKNOWN_CLOSURE_MATRIX.md)

| ID | Question | Primary class |
|---|---|---|
| U-01 | What does `acquire` establish across implementations? | **S** (residual **U**) |
| U-02 | If WLM-visible availability and provider state disagree, which controls dispatch? | **U** |
| U-03 | Who has final authority when calibration/maintenance conflicts with an allocation? | **U** |
| U-04 | What proves that a remote task stopped after scheduler cancellation or timeout? | **U** |
| U-05 | What is the recovery authority after partial failure? | **U** |
| U-06 | Can one record reconcile allocated time, provider waiting, actual execution, retry/cancellation and cost? | **U** |
| U-07 | How are HPC identity and provider credential authority joined and audited? | **S** (residual **U**) |

## Newly resolved points

- `acquire` cannot safely be treated as synonymous with execution readiness in the general case.
- The two-queue problem is governance-sensitive, not simply quantum-sensitive.
- Calibration availability remains an explicit unresolved state surface (`is_accessible` does not reflect availability; `is_runnable` is prospective).
- All seven Unknowns now carry explicit `D / S / I / U / A` classifications; contradictions are recorded in [`SC_CONTRADICTION_REGISTER.md`](./SC_CONTRADICTION_REGISTER.md).

## Completion trigger

**Met for classification.** Gate 0 must now be re-evaluated (Gate 0C) before any second proving domain.

## Artifact coupling

| Artifact | Path |
|---|---|
| Boundary Intelligence Record | `research/SC_BIR_001_BOUNDARY_INTELLIGENCE_RECORD.md` |
| Unknown Closure Matrix | `research/SC_BIR_001_UNKNOWN_CLOSURE_MATRIX.md` |
| Contradiction Register | `research/SC_CONTRADICTION_REGISTER.md` |
| Evidence Matrix v0.2 | `research/BOUNDARY_EVIDENCE_MATRIX_V0_2.md` |
| Public page | `site/reference-case-001/` |
| Machine-readable | `data/boundaries/sc-bir-001.json` |
