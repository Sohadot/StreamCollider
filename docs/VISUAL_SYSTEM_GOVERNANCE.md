# Visual System Governance v0.1

## Direction

**Research instrument + systems atlas + control-room intelligence**, rendered on a light mineral surface.

## Palette roles

- `--paper`: warm mineral white
- `--ink`: deep graphite text
- `--structure`: cool steel / slate
- `--stream`: muted teal-blue for computational flow
- `--authority`: deep indigo for governance
- `--unknown`: amber/copper for unresolved state
- `--critical`: restrained rust only when evidence or recovery risk requires it

Color is semantic, not decorative.

## Geometry

- generous whitespace
- thin structural rules
- irregular-but-governed field layout
- no card-grid-first homepage
- diagrams use labels directly on the field
- radii restrained; avoid consumer-app softness

## Typography

Use system stacks only. No external font/CDN dependency.

Display: `ui-serif, Georgia, Cambria, "Times New Roman", serif`

Interface/body: `ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif`

Mono/evidence: `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`

## Accessibility

- semantic HTML
- keyboard-reachable interactive boundaries
- reduced-motion support
- no information carried by color alone
- strong focus states
- minimum readable body size 16px
- contrast targets WCAG AA or better

## Performance

- no external JavaScript
- no external CSS
- no WebGL in v0.1
- SVG inline only where explanatory
- initial JS must remain non-critical
- page remains understandable with JavaScript disabled
