# Brand Pulse

**Find out what the internet really thinks about any brand — in minutes, not days.**

Brand Pulse scans Reddit, Hacker News, Trustpilot, G2, Capterra, Sitejabber, Product Hunt, BBB, Glassdoor, app stores, and Google search for mentions of any brand, person, product, or company. It clusters complaints, feature requests, and praise; ranks them by recency-weighted volume; and writes you a single readable report.

Run it again next month and it tells you **what changed** — sentiment shifts, new complaints, resolved issues, mention volume deltas.

## What you get

Every report includes:

- **Since Last Pulse** — trend diff versus your last report (if one exists)
- **Executive Summary** — 3–5 sentence distilled take
- **Top 3 Complaints** — ranked by volume × recency
- **Top 3 Feature Requests**
- **Key Recommendations** — what to actually do about it
- **Detailed Breakdown** — per-source findings with quoted examples and links
- **Coverage & Blind Spots** — honest accounting of what was (and wasn't) covered

## Quick start

1. Install Brand Pulse from the `beginnersinai-skills` marketplace
2. Type `/reputation` in Claude Code (or just say *"check my reputation"* / *"what are people saying about Figma"*)
3. Answer the 4-question first-run wizard
4. Wait 3–20 minutes depending on depth setting
5. Read the report in chat → optionally save as PDF

That's it. No API keys. No accounts. No setup.

## Two modes

### Public mode (default — zero setup)
Uses only public sources:
- **Reddit** (via public `.json` endpoint)
- **Hacker News** (via free Algolia API)
- **Trustpilot, G2, Capterra, Sitejabber, Product Hunt, BBB, Glassdoor**
- **Google search** (via Claude's built-in WebSearch)
- **App Store / Play Store** reviews (for apps)

No API keys. Runs out of the box.

### Enhanced mode (optional — covers socials)
If you have the Playwright plugin installed, Brand Pulse can drive your logged-in browser to pull data from sites that require auth:

- **X / Twitter**
- **LinkedIn**
- **Instagram**
- **TikTok**
- **Facebook pages**

You stay logged in in your own browser — Brand Pulse just navigates and reads, like a very fast research assistant. Throttled to human-speed pacing (3–5s between actions). Only runs when you pick Enhanced mode at the start of a session.

To enable: install the `playwright` plugin alongside Brand Pulse. The skill auto-detects it.

## Commands

- `/reputation` — run on your default brand (from config)
- `/reputation acme-corp` — run on any brand
- `/reputation --compare acme-corp` — side-by-side benchmark against your brand
- `/reputation --reconfigure` — reset the first-run wizard
- `/reputation --mute reddit` — hide a source from future reports

The skill also fires on natural language:

- "check my reputation"
- "what are people saying about Figma?"
- "competitor research on Notion"
- "brand pulse on Anthropic"

## Trend tracking

Every report saves to `~/brand-pulse/<brand-slug>/YYYY-MM-DD.md`. The next run reads the most recent prior report and prepends a **Since Last Pulse** section showing:

- Sentiment shift (e.g. 62% positive → 58% positive, −4 pts)
- New complaints that weren't there before
- Complaints that have disappeared (potentially resolved)
- Mention volume change
- Top narrative shifts

Delete the folder any time to wipe history.

## Honest limitations

- **Social coverage requires Enhanced mode.** Public mode does not cover X, LinkedIn, Instagram, TikTok, or Facebook. There is no free scraping path for those post-2023.
- **US-centric review sites.** BBB and Glassdoor are US-focused. International brands get shallower data from those two.
- **Sentiment is AI-inferred, not survey-grade.** Good for trends and clusters. Don't quote the exact percentages to your board without context.
- **Enhanced mode is research automation, not bulk scraping.** It uses your own logged-in session, throttled. Treat it like it's you, reading faster.

## Keeping Up to Date

Third-party marketplaces have auto-update **off** by default. To get future versions automatically:

1. Type `/plugin` in Claude Code
2. Press Tab to the **Marketplaces** tab
3. Select **beginnersinai-skills**
4. Choose **Enable auto-update**

Or update manually any time:

```
/plugin marketplace update beginnersinai-skills
/plugin update brand-pulse@beginnersinai-skills
/reload-plugins
```

## Privacy

- Brand Pulse never sends your data anywhere except the public websites it fetches from.
- In Enhanced mode, all browser actions happen in **your** browser session on **your** machine.
- Reports save to your local disk at `~/brand-pulse/`. Nothing uploads.
- No analytics, no telemetry, no accounts.

## License

MIT. Free forever.

---

Made by [Beginners in AI](https://beginnersinai.org).
