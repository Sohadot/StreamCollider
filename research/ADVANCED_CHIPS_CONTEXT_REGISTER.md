# Advanced Chips Context Register v0.1

**Status:** Context-only. Gate 1 candidate screen complete — see [`GATE_1_ADVANCED_CHIP_CANDIDATE_SCREEN.md`](./GATE_1_ADVANCED_CHIP_CANDIDATE_SCREEN.md). Candidate A authorized to advance to SC-BIR-002 dossier work. No advanced-chip case is admitted as a Stream Collision yet.

## Context proposition

> **As advanced compute decomposes into more specialized components, the number and importance of system boundaries increase.**

UCIe 3.0 and current heterogeneous-integration work support the importance of system-level coordination and manageability, but do not by themselves prove independently governed authority domains.

## Candidate future cases

- Cross-vendor chiplet management boundary
- Host ↔ independently managed accelerator
- Electronic ↔ photonic control boundary
- Compute ↔ independently managed memory/fabric domain
- Package-level throttle/shutdown authority boundary

## Admission questions

- Who governs side A?
- Who governs side B?
- What exact stream/state/action crosses?
- What authority changes or must be reconciled?
- What can each side not know or prove alone?
- What happens on partial failure?
- Which established engineering terms already describe the consequence?
- Is the result more than a re-description of the interconnect specification?

**Do not select a case merely because it uses UCIe.**
