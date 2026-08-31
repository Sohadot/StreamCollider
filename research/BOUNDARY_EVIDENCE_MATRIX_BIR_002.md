# Boundary Evidence Matrix — SC-BIR-002

**Record link:** SC-BIR-002  
**Domain:** Director-managed chiplet (UCIe 3.0 manageability)

| ID | Question | Current evidence reading | Linked Unknown | Class signal |
|---|---|---|---|---|
| B2-001 | Deployment-level distinct governance | **Open** — protocol roles documented; operational independence not normatively closed in public pack | U-01 | **U** |
| B2-002 | Firmware / MTP ownership | **Open** — director-mediated flows documented; cross-party custody owner absent | U-02 | **U** |
| B2-003 | Authoritative configuration state | **Open** — inconsistent post-download config flagged in verification literature | U-03 | **U** |
| B2-004 | Version mismatch authority | **Open** — verification scenarios required; runtime rejection proof not standardized publicly | U-04 | **U** |
| B2-005 | Partial-update recovery | **Open** — retry/rollback/safe-state scenarios in verification; authority graph absent | U-05 | **U** |
| B2-006 | Emergency throttle / shutdown vs local state | **Strong partial** — SiP-wide mechanisms documented; precedence/proof open | U-06 | **S**/**U** |
| B2-007 | Director vs chiplet-local state disagreement | **Open** — cross-layer divergence documented; no precedence table | U-07 | **U** |
| B2-008 | Proof after failed / interrupted management | **Open** — verification proof requirements; production dual-sided protocol absent | U-08 | **U** |
| B2-009 | Negative control | **Strong** — monolithic / local-FW-only avoids director-mediated boundary | Admission | **D** |

## Generalization surface under test

Does StreamCollider expose **authority + state + proof + recovery** at a **director ↔ satellite manageability** boundary with Unknowns that are **not** reducible to UCIe feature lists?

## Gate coupling

- Gate 1 evidence ledger: **this revision**
- Gate 1 falsification: **pending**
- Public surface: **locked**
