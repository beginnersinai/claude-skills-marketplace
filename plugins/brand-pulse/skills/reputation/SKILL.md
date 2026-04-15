---
name: reputation
description: Reputation monitoring and competitor research. Use when the user wants to check a brand's reputation, research what people are saying about a company/person/product/app/creator, benchmark a competitor's sentiment, track brand mentions over time, or types /reputation, /brand-pulse, /competitor, or says "brand pulse". Covers Reddit, Hacker News, Trustpilot, G2, Capterra, Sitejabber, Product Hunt, BBB, Glassdoor, app stores, and Google search by default. If the Playwright plugin is installed, can also drive the user's logged-in browser to cover X/Twitter, LinkedIn, Instagram, TikTok, and Facebook.
---

# Brand Pulse — Reputation Monitoring

You are running a reputation and competitor research pulse. Produce a single readable markdown report with an executive summary, top complaints/feature requests/recommendations, a detailed per-source breakdown, and (if prior reports exist) a trend diff.

## Invocation patterns you handle

- `/reputation` — run on user's default brand (from saved config)
- `/reputation <brand>` — run on any brand
- `/competitor <brand>` — alias for `/reputation <brand>` (standalone report on that brand)
- `/reputation --compare <brand>` — side-by-side diff vs. user's default brand
- `/reputation --reconfigure` — wipe and re-run the first-session wizard
- `/reputation --mute <source>` — add a source to the mute list in config
- Natural language: "check my reputation", "what are people saying about X", "competitor research on Y", "brand pulse"

## Step 0 — Handle special flags first

- `--reconfigure` → delete `~/brand-pulse/config.md` and proceed to Step 2
- `--mute <source>` → append to a `muted_sources:` list in config, confirm, exit
- `--compare <brand>` → run the full pipeline on both brands, then produce a side-by-side report
- `/competitor <brand>` → equivalent to `/reputation <brand>`; run the standalone pipeline on that brand
- Otherwise behave normally

## Step 1 — Detect Playwright and load or create config

First, check whether any tool name starting with `mcp__plugin_playwright_playwright__` is available in this session. Record as `playwright_available` for use in Steps 2 and 3.

Then read `~/brand-pulse/config.md`. If it exists, parse the frontmatter and skip to Step 3.

If it does NOT exist, run the first-session wizard (Step 2).

Config file format:
```markdown
---
default_brand: Acme Corp
default_url: acme.com
entity_type: Company
depth: standard
playwright_available: true
logged_in_socials: [x, linkedin]
muted_sources: []
created: 2026-04-15
---

# Brand Pulse Config

(Any user notes here.)
```

## Step 2 — First-session wizard

Use `AskUserQuestion` to ask these four questions **in one batch** (one call, multiple questions):

1. **Brand / name** — free text. Ask for the canonical name + optional URL. Store as `default_brand` and `default_url`.
2. **Entity type** — `Person`, `Company`, `Product`, `App`, `Creator`. Drives which sources are relevant (see `references/sources.md`).
3. **Depth** — `Quick (~3 min)`, `Standard (~10 min)`, `Deep (~20+ min)`. Affects how many sources are hit and how many items per source.
4. **Socials** — ONLY ASK THIS IF `playwright_available` is true (from Step 1). List: X, LinkedIn, Instagram, TikTok, Facebook. Multi-select. If Playwright is not available, skip this question and note Public mode in the config.

Write the config to `~/brand-pulse/config.md` (create the directory if needed).

Briefly confirm back to the user what was saved before proceeding.

## Step 3 — Choose mode for this run

Use the `playwright_available` value from Step 1.

- **Available** → Enhanced mode is an option. Ask the user now via `AskUserQuestion`:
  > "Which mode for this run? **Public** (fast, zero setup) or **Enhanced** (Claude drives your logged-in browser to also cover X/LinkedIn/IG/TikTok/FB)."
- **Not available** → Default to Public mode. Include a one-line note in the final report's Coverage footer: *"Install the Playwright plugin to add X/LinkedIn/IG/TikTok/FB coverage."*

Respect `muted_sources` from config for both modes.

## Step 4 — Load the trend baseline (if any)

Glob `~/brand-pulse/<brand-slug>/*.md` where `<brand-slug>` is the brand name kebab-cased. If any prior reports exist, sort filenames lexically descending (YYYY-MM-DD filenames sort correctly) and read the most recent one. Extract:

- Previous sentiment split (positive/neutral/negative percentages)
- Previous top 5 complaints
- Previous top 5 feature requests
- Previous mention volume per source
- Report date

Use this for the "Since Last Pulse" section later. If no prior reports exist, skip the trend section.

## Step 5 — Plan and fan out searches

Consult `references/sources.md` to pick the source set based on entity type and depth:

- **Quick**: Reddit + HN + Google SERP + (1 review site based on entity type)
- **Standard**: above + Trustpilot + G2 + Product Hunt + BBB (if US company) + app stores (if app)
- **Deep**: above + Capterra + Sitejabber + Glassdoor + additional subreddits + deeper time window

For Enhanced mode, also add the logged-in socials from config.

Use `TaskCreate` to break this into parallel tasks. Then fire the searches in parallel — **in one single message with multiple tool calls** wherever possible. `WebSearch`, `WebFetch`, and Playwright calls all run concurrently.

For each source, follow the exact query patterns and extraction targets in `references/sources.md`.

### Playwright flows (Enhanced mode)

Follow `references/playwright-flows.md` for per-site scripts. Key rules:

- Throttle: insert a 3–5 second wait between non-trivial interactions (`browser_wait_for` with time).
- Max 5 scroll iterations per site (≈50–100 items).
- If a site redirects to a login page, the user's session expired — stop that site and note it in coverage.
- Never post, like, comment, or follow. Read-only navigation and snapshots.

## Step 6 — Cluster and score

For the raw mentions from each source:

1. **Classify** each mention as: `complaint`, `feature_request`, `praise`, `neutral_mention`, or `noise`. Drop noise.
2. **Cluster** complaints and feature requests by theme. Use semantic similarity. A good cluster has ≥2 distinct mentions from ≥1 source.
3. **Score** each cluster by: `mention_count × recency_weight × source_authority_weight`.
   - `recency_weight` = exp(−days_old / 30) (30-day half-life)
   - `source_authority_weight`: Trustpilot/G2/Capterra = 1.2, BBB = 1.2, Reddit/HN/Product Hunt/Glassdoor/app stores/Enhanced socials = 1.0, Google SERP snippets = 0.8. Unlisted sources default to 1.0.
4. **Rank** clusters within each category (complaints, feature requests, praise).
5. **Overall sentiment**: count positive / neutral / negative across ALL mentions (not just clusters). Report as percentages.

## Step 7 — Compute "Since Last Pulse" diff (if baseline exists)

- Sentiment shift: percentage-point delta per bucket
- New complaint clusters: in current, not in previous
- Disappeared complaint clusters: in previous, not in current (tentatively "may be resolved")
- New feature requests
- Volume change: total mentions this run vs. last run (%)
- If data is sparse (e.g. both runs had <20 mentions), note that trend is low-confidence

## Step 8 — Write the report

Use `references/report-template.md` as the structure. Render the whole thing as a single markdown document in the chat.

Structure (in this order):

1. **Title + metadata** (brand, date, mode, depth)
2. **Since Last Pulse** — only if baseline existed
3. **Executive Summary** — 3–5 sentences, no bullet points, written in plain prose
4. **Top 3 Complaints** — with mention counts and representative quoted examples (with links)
5. **Top 3 Feature Requests** — same format
6. **Key Recommendations** — 3–5 actionable bullets derived from the clusters
7. **Detailed Breakdown** — H3 per source, each with: volume, sentiment split, 2–3 representative quotes, links
8. **Coverage & Blind Spots** — what was and wasn't covered, honestly
9. **Methodology footer** — sources, date range, recency weighting, ethical note

Quote real text from real mentions. Never fabricate quotes. If a quote is sparse or unclear, paraphrase and mark it as `[paraphrased]`.

Every quote must have a source link immediately after it in parentheses.

## Step 9 — Save and export

1. Always save the markdown report to `~/brand-pulse/<brand-slug>/YYYY-MM-DD.md` (create directory if needed). Report the absolute path to the user.
2. Use `AskUserQuestion` to ask:
   - **Export as PDF?** (Yes / No)
   - **Run on another brand next?** (Yes, name: _____ / No)
3. If PDF requested:
   - Check if `pandoc` is installed via `which pandoc`. If yes, try engines in this order: `pandoc <file>.md -o <file>.pdf --pdf-engine=xelatex` → on failure, check `which wkhtmltopdf` and retry with `--pdf-engine=wkhtmltopdf` → on failure, retry with no engine flag (pandoc picks its default).
   - If pandoc is not installed: generate a styled HTML file next to the markdown (`<file>.html`) using a clean print-ready template. Open it with the system default browser (`open <file>.html` on macOS, `xdg-open` on Linux, `start` on Windows). Tell the user: *"Press Cmd+P (Ctrl+P on Windows/Linux) → Save as PDF."* This is the zero-install path.

## Step 10 — Wrap up

Single-sentence summary of what was produced and where it lives. No wall of text.

---

## Ethical and operational rules

- **Never post, like, comment, follow, send messages, or modify any account state.** Read-only research.
- **Throttle Enhanced mode to 3–5s between actions.** Look human, not like a bot.
- **Never fabricate quotes.** If the source text is unclear, paraphrase and mark it.
- **Always show coverage gaps honestly.** If X/LinkedIn etc. weren't covered, say so in the footer.
- **Respect `muted_sources`.** User has veto power over any source.
- **If a site returns a paywall, captcha, or login redirect**, stop that source, note it in coverage, and continue with the rest.
- **If the user is running on someone they have a personal conflict with**, you still produce an objective report. This tool is factual, not editorial.

## References

- `references/sources.md` — per-source URL patterns, query construction, rate limit notes, extraction fields
- `references/report-template.md` — the full markdown report template with example sections
- `references/playwright-flows.md` — per-site Playwright scripts for Enhanced mode
