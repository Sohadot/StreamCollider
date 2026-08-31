# First Indexed Release Plan v0.1

## Goal

Create a public, citable, crawlable foundation early without making claims that Gate 0 has not earned.

## First release routes

1. `/`
2. `/thesis/`
3. `/boundaries/`
4. `/reference-case-001/`
5. `/advanced-compute/`
6. `/sources/`
7. `/method/`

## Required launch files

- `CNAME`
- `robots.txt`
- `sitemap.xml`
- canonical tags on every page
- unique title and description
- internal navigation
- JSON-LD `WebSite` / `TechArticle` where appropriate
- no orphan routes
- no placeholder links
- no `noindex` on the seven foundation routes

## Search Console sequence

1. Deploy the public surface.
2. Verify the property.
3. Submit `/sitemap.xml`.
4. Inspect `/`, `/thesis/`, `/reference-case-001/`, `/advanced-compute/`.
5. Request indexing for the core pages.
6. Record first discovered / crawled / indexed signals in the project log.
7. Do not change `lastmod` unless page content materially changes.

## Provenance sequence

`Git commit → production deployment → sitemap submission → Search Console crawl/indexation evidence`
