# Sources — Query Patterns and Extraction

For each source: URL pattern, auth requirement, depth scaling, extraction fields, and notes.

Slug the brand name (kebab-case, lowercase, URL-safe) for all patterns below. Denote as `{brand}`. If a canonical URL is provided, denote its domain as `{domain}`.

---

## Public sources (Public mode)

### Reddit — broad search
- **URL**: `https://www.reddit.com/search.json?q={brand}&sort=new&limit=100&t=year`
- **Auth**: none
- **Method**: `WebFetch`
- **Extract per item**: `data.children[].data` → `title`, `selftext`, `score`, `num_comments`, `created_utc`, `permalink`, `subreddit`
- **Time filter**: `t=month` for Quick, `t=year` for Standard, `t=all` for Deep
- **Notes**: Reddit's public JSON is rate-limited. Space out requests ≥1s. If you get HTTP 429, wait 60s and retry once.

### Reddit — subreddit-scoped (Deep only)
- Pick 3–5 relevant subreddits based on entity type:
  - Person/Creator: relevant niche subs, r/PublicFigures
  - Company: r/{industry}, r/BusinessOwners, r/consumer-specific
  - Product: product-specific subs, r/BuyItForLife, r/reviews
  - App: r/androidapps, r/iosapps, category subs
- **URL**: `https://www.reddit.com/r/{subreddit}/search.json?q={brand}&restrict_sr=1&sort=new&limit=50`

### Hacker News (Algolia)
- **URL**: `https://hn.algolia.com/api/v1/search_by_date?query={brand}&tags=story&hitsPerPage=50`
- **Also**: `?tags=comment` for comment mentions
- **Auth**: none (Algolia public API, free, no key)
- **Method**: `WebFetch`
- **Extract**: `hits[]` → `title`, `story_text`, `comment_text`, `author`, `created_at`, `url`, `points`, `num_comments`, `objectID`
- **Notes**: Especially valuable for tech/dev/B2B brands. Auto-skip for pure consumer brands unless Deep mode.

### Trustpilot
- **URL**: `https://www.trustpilot.com/review/{domain}` (requires `default_url` from config)
- **Fallback search**: `https://www.trustpilot.com/search?query={brand}`
- **Auth**: none
- **Method**: `WebFetch`
- **Extract**: review text, star rating, date, reviewer name (pseudonymize if needed), response from company (if any)
- **Notes**: Sort by newest. Grab first 2 pages for Standard, 5 for Deep.

### G2
- **URL**: `https://www.g2.com/products/{brand-slug}/reviews` (try first)
- **Search fallback**: `https://www.g2.com/search?query={brand}`
- **Auth**: none
- **Method**: `WebFetch`
- **Extract**: review title, body, star rating, pros/cons, date, reviewer role
- **Notes**: B2B SaaS focus. Highest-signal source for software products.

### Capterra
- **URL**: `https://www.capterra.com/p/{id}/{brand-slug}/reviews/`
- **Search**: `https://www.capterra.com/search/?search={brand}`
- **Notes**: Similar to G2, sometimes has different review population.

### Sitejabber
- **URL**: `https://www.sitejabber.com/reviews/{domain}`
- **Notes**: Consumer-focused. Useful for ecommerce / DTC brands.

### Product Hunt
- **URL**: `https://www.producthunt.com/products/{brand-slug}` (try first)
- **Search**: `https://www.producthunt.com/search?q={brand}`
- **Extract**: product score, comment count, discussions, launch-day feedback
- **Notes**: Strongest for launch reception and early-adopter feature asks.

### BBB (Better Business Bureau)
- **URL**: `https://www.bbb.org/search?find_text={brand}&find_country=USA`
- **Extract**: complaint count, complaint categories, rating, years in business
- **Skip if**: non-US entity, or entity type is Person/Creator
- **Notes**: Formal complaint data — treat as high-weight signal.

### Glassdoor
- **URL**: `https://www.glassdoor.com/Reviews/company-reviews.htm?sc.keyword={brand}`
- **Skip if**: entity type is not Company
- **Notes**: Employee sentiment, not customer. Useful for company-reputation runs. Include as a separate section, do not merge with customer sentiment.

### Google search (WebSearch)
- Run these queries in parallel:
  - `"{brand}" review 2026`
  - `"{brand}" complaint OR problem`
  - `"{brand}" vs` (captures comparison posts)
  - `"{brand}" alternative` (signal for churn drivers)
  - `"{brand}" scam OR fraud` (only surface if results are real; many brands have noise)
- **Method**: `WebSearch` then `WebFetch` on the top 3–5 non-owned results per query
- **Skip owned domains** (brand's own site, their social profiles) — they don't count as third-party sentiment.

### App Store (Apple) — apps only
- **URL**: `https://apps.apple.com/us/app/{slug}/id{id}` — need app ID; search Google for it first if unknown
- **Extract**: average rating, review count, recent reviews (visible on page)
- **Notes**: Only deep reviews visible via iTunes API; the web page shows top reviews which is usually enough.

### Play Store (Google) — apps only
- **URL**: `https://play.google.com/store/apps/details?id={package}`
- **Extract**: rating, review count, top reviews section
- **Notes**: Review sort options limited via web; focus on most relevant and most recent.

---

## Enhanced sources (require Playwright + user login)

See `playwright-flows.md` for per-site scripts. Query patterns:

### X / Twitter
- Search URL: `https://twitter.com/search?q={brand}&src=typed_query&f=live` (live = most recent)

### LinkedIn
- Content search: `https://www.linkedin.com/search/results/content/?keywords={brand}&sortBy=%22date_posted%22`
- Company page (if exists): `https://www.linkedin.com/company/{slug}/`

### Instagram
- Tag search: `https://www.instagram.com/explore/tags/{brand_no_spaces}/`
- Username (if exists): `https://www.instagram.com/{handle}/` — scan comment sections of recent posts

### TikTok
- Search: `https://www.tiktok.com/search?q={brand}`
- Hashtag: `https://www.tiktok.com/tag/{brand_no_spaces}`

### Facebook
- Search: `https://www.facebook.com/search/posts/?q={brand}`
- Page (if exists): `https://www.facebook.com/{brand}/reviews`

---

## Entity type → source matrix

| Source | Person | Company | Product | App | Creator |
|---|---|---|---|---|---|
| Reddit | ✓ | ✓ | ✓ | ✓ | ✓ |
| Hacker News | Deep only | ✓ | ✓ | ✓ | Deep only |
| Trustpilot | — | ✓ | ✓ | — | — |
| G2 | — | ✓ (B2B) | ✓ (B2B) | — | — |
| Capterra | — | ✓ (SaaS) | ✓ (SaaS) | — | — |
| Sitejabber | — | ✓ (DTC) | ✓ (DTC) | — | — |
| Product Hunt | — | ✓ | ✓ | ✓ | — |
| BBB | — | ✓ (US) | — | — | — |
| Glassdoor | — | ✓ | — | — | — |
| Google SERP | ✓ | ✓ | ✓ | ✓ | ✓ |
| App Store | — | — | — | ✓ | — |
| Play Store | — | — | — | ✓ | — |
| X (Enhanced) | ✓ | ✓ | ✓ | ✓ | ✓ |
| LinkedIn (Enhanced) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Instagram (Enhanced) | ✓ | ✓ | ✓ | — | ✓ |
| TikTok (Enhanced) | ✓ | ✓ | ✓ | — | ✓ |
| Facebook (Enhanced) | — | ✓ | — | — | — |

---

## Depth scaling

- **Quick (~3 min)**: Reddit broad + HN + Google SERP (3 queries) + 1 review site by entity type. Items per source: 20–30.
- **Standard (~10 min)**: Add Trustpilot, G2/Product Hunt, BBB (if applicable), app stores (if applicable), all 5 Google queries. Items per source: 50.
- **Deep (~20+ min)**: Add Capterra, Sitejabber, Glassdoor (companies), subreddit-scoped searches (3–5 subs), extend time window to `t=all` on Reddit. Items per source: 100.

Enhanced mode adds the selected social sources to whichever depth is chosen.

---

## Robustness notes

- Always set a User-Agent when WebFetching. Reddit's JSON API accepts anything, but some sites 403 a blank UA.
- If a source 403s, times out, or returns <5 items, note it in coverage and move on. Don't retry more than once.
- Parsing tolerance: treat `WebFetch` output as messy HTML converted to text. Look for signal in the noise; don't panic if structure is inconsistent.
- Date extraction: if exact dates aren't available, estimate from relative timestamps ("3 days ago"). Flag in data as `approx_date`.
