#!/usr/bin/env python3
"""PR validation for StreamCollider Gate 0B artifacts. No deployment."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
ERRORS: list[str] = []


def fail(msg: str) -> None:
    ERRORS.append(msg)


def require(path: Path, label: str | None = None) -> None:
    if not path.exists():
        fail(f"missing required file: {label or path}")


def main() -> int:
    required = [
        SITE / "index.html",
        SITE / "reference-case-001" / "index.html",
        SITE / "sources" / "index.html",
        SITE / "sitemap.xml",
        SITE / "robots.txt",
        SITE / "CNAME",
        SITE / "data" / "boundaries" / "sc-bir-001.json",
        ROOT / "data" / "boundaries" / "sc-bir-001.json",
        ROOT / "research" / "SC_BIR_001_BOUNDARY_INTELLIGENCE_RECORD.md",
        ROOT / "research" / "SC_BIR_001_UNKNOWN_CLOSURE_MATRIX.md",
        ROOT / "research" / "SC_CONTRADICTION_REGISTER.md",
        ROOT / "SOURCE_REGISTER.md",
        ROOT / "INDEXATION_LOG.md",
    ]
    for path in required:
        require(path)

    repo_json = ROOT / "data" / "boundaries" / "sc-bir-001.json"
    site_json = SITE / "data" / "boundaries" / "sc-bir-001.json"
    try:
        repo_obj = json.loads(repo_json.read_text(encoding="utf-8"))
        site_obj = json.loads(site_json.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        fail(f"JSON parse error: {exc}")
        repo_obj = site_obj = None

    if repo_obj is not None and site_obj is not None:
        if repo_obj != site_obj:
            fail("repo and public sc-bir-001.json diverge; keep data/ and site/data/ in sync")
        for key in ("record_id", "status", "domain_a", "domain_b", "admission", "unknowns", "sources"):
            if key not in site_obj:
                fail(f"sc-bir-001.json missing key: {key}")
        if site_obj.get("record_id") != "SC-BIR-001":
            fail("sc-bir-001.json record_id must be SC-BIR-001")
        if site_obj.get("machine_readable_url") != "https://streamcollider.com/data/boundaries/sc-bir-001.json":
            fail("sc-bir-001.json machine_readable_url must point to public JSON")

    # Claim restraint on public dossier
    dossier = (SITE / "reference-case-001" / "index.html").read_text(encoding="utf-8")
    if "the first citable cross-source audit" in dossier:
        fail("unscoped 'first citable' claim still present on public dossier")
    if "Machine-readable record" not in dossier or "/data/boundaries/sc-bir-001.json" not in dossier:
        fail("public dossier must link Machine-readable record → JSON")

    # Canonical URLs on HTML pages
    html_pages = sorted(SITE.rglob("index.html"))
    for page in html_pages:
        text = page.read_text(encoding="utf-8")
        m = re.search(r'rel="canonical"\s+href="([^"]+)"', text)
        if not m:
            fail(f"missing canonical: {page.relative_to(ROOT)}")
            continue
        href = m.group(1)
        if not href.startswith("https://streamcollider.com/"):
            fail(f"canonical must be streamcollider.com: {page.relative_to(ROOT)} -> {href}")

    # Sitemap consistency
    sitemap = (SITE / "sitemap.xml").read_text(encoding="utf-8")
    locs = re.findall(r"<loc>([^<]+)</loc>", sitemap)
    if "https://streamcollider.com/data/boundaries/sc-bir-001.json" not in locs:
        fail("sitemap missing public sc-bir-001.json")
    for loc in locs:
        parsed = urlparse(loc)
        if parsed.netloc != "streamcollider.com":
            fail(f"sitemap loc outside streamcollider.com: {loc}")
            continue
        rel = parsed.path.lstrip("/")
        if not rel:
            target = SITE / "index.html"
        elif rel.endswith(".json") or rel.endswith(".xml") or rel.endswith(".txt"):
            target = SITE / rel
        else:
            target = SITE / rel / "index.html" if not rel.endswith(".html") else SITE / rel
            if rel.endswith("/"):
                target = SITE / rel / "index.html"
            elif (SITE / rel).is_dir():
                target = SITE / rel / "index.html"
            elif not rel.endswith((".html", ".json", ".xml", ".txt")):
                target = SITE / rel / "index.html"
        if not target.exists():
            # also try path as file
            alt = SITE / rel
            if not alt.exists():
                fail(f"sitemap loc has no local file: {loc}")

    # Internal site links from HTML
    href_re = re.compile(r'href="(/[^"#]*)"')
    for page in html_pages:
        text = page.read_text(encoding="utf-8")
        for href in href_re.findall(text):
            if href.startswith("//"):
                continue
            path = href.split("?", 1)[0]
            if path.endswith("/"):
                target = SITE / path.lstrip("/") / "index.html"
            elif path.endswith((".css", ".js", ".json", ".xml", ".txt", ".html")):
                target = SITE / path.lstrip("/")
            else:
                target = SITE / path.lstrip("/") / "index.html"
                if not target.exists() and (SITE / path.lstrip("/")).exists():
                    target = SITE / path.lstrip("/")
            if not target.exists():
                fail(f"broken internal link in {page.relative_to(ROOT)}: {href}")

    # Source register must expose primary locators
    register = (ROOT / "SOURCE_REGISTER.md").read_text(encoding="utf-8")
    for needle in (
        "https://arxiv.org/abs/2509.20525",
        "https://arxiv.org/abs/2506.10052",
        "https://arxiv.org/abs/2607.19591",
        "https://arxiv.org/abs/2604.20912",
        "https://awennersteen.com/talks/2026-01-19-OpenQSE/",
    ):
        if needle not in register:
            fail(f"SOURCE_REGISTER missing stable locator: {needle}")

    if ERRORS:
        print("VALIDATE FAILED")
        for err in ERRORS:
            print(f"- {err}")
        return 1

    print("VALIDATE OK")
    print(f"checked {len(html_pages)} HTML pages, {len(locs)} sitemap locs, JSON sync, claim restraint")
    return 0


if __name__ == "__main__":
    sys.exit(main())
