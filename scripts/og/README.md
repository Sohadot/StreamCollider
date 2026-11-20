# Social card (Open Graph image)

`og-card.html` is the source design for `site/assets/og-image.png` (1200×630),
which every page references via `og:image` / `twitter:image`.

Regenerate after editing the template:

```bash
node scripts/og/render_og.js
python3 -c "from PIL import Image;p='site/assets/og-image.png';Image.open(p).convert('RGB').save(p,optimize=True)"
```

Fonts (Fraunces, IBM Plex Mono) are loaded only at render time and baked into
the PNG; the published site keeps its no-external-dependency rule. Keep the PNG
under ~300 KB so WhatsApp shows the large preview.
