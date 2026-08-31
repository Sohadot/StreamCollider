# StreamCollider Interface Foundation v0.1

This package is deployment-oriented.

## Governance
- `docs/INTERFACE_THESIS.md`
- `docs/VISUAL_SYSTEM_GOVERNANCE.md`
- `docs/HOME_INFORMATION_ARCHITECTURE.md`
- `docs/MOTION_MEANING_SYSTEM.md`
- `docs/INDEXATION_RELEASE_PLAN.md`

## Public surface
Deploy the contents of `site/` to the GitHub Pages publishing root.

Routes:
- `/`
- `/thesis/`
- `/boundaries/`
- `/reference-case-001/`
- `/advanced-compute/`
- `/sources/`
- `/method/`

## Design posture
- light mineral interface, not black/neon
- conceptual Boundary Field on the homepage
- semantic motion only
- no CDN
- no external JS
- no WebGL
- crawlable without JS
- Advanced Compute visible as context from first indexation
- Reference Case 001 remains the only proving case

## Before production
1. Confirm GitHub Pages publishes from the directory where `site/` contents will live.
2. Move the contents of `site/` to the configured publishing root if necessary.
3. Confirm DNS for `streamcollider.com`.
4. Deploy.
5. Submit `https://streamcollider.com/sitemap.xml` in Google Search Console.
6. Request indexing for `/`, `/thesis/`, `/reference-case-001/`, and `/advanced-compute/`.
