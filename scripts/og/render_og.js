#!/usr/bin/env node
// Renders scripts/og/og-card.html to site/assets/og-image.png (1200x630).
// Usage: node scripts/og/render_og.js   (requires Playwright + Chromium)
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const root = path.resolve(__dirname, '..', '..');
  const src = 'file://' + path.join(__dirname, 'og-card.html');
  const out = path.join(root, 'site', 'assets', 'og-image.png');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
  await page.goto(src, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: out, type: 'png' });
  await browser.close();
  console.log('wrote', path.relative(root, out));
})();
