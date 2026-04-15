# Brand Pulse — Quick Start

5 steps. You'll have a reputation report in under 10 minutes.

## Step 1 — Install Brand Pulse

Install from the `beginnersinai-skills` marketplace in Claude Code. If you haven't added the marketplace yet:

```
/plugin marketplace add beginnersinai/claude-skills-marketplace
/plugin install brand-pulse@beginnersinai-skills
```

## Step 2 — (Optional) Install Playwright for deeper coverage

If you want Brand Pulse to cover **X, LinkedIn, Instagram, TikTok, and Facebook**, install the Playwright plugin too. It lets Claude drive your own logged-in browser.

```
/plugin install playwright@beginnersinai-skills
```

You can skip this and still get a solid report from public sources. Add it later if you want deeper social coverage.

## Step 3 — Turn on auto-updates (IMPORTANT)

Third-party plugins don't auto-update by default. Flip this on once and you'll always have the latest version:

1. Type `/plugin`
2. Press **Tab** until you're on the **Marketplaces** tab
3. Select **beginnersinai-skills**
4. Choose **Enable auto-update**

Done once, good forever.

## Step 4 — Run your first pulse

Type either of these:

```
/reputation
```

Or just ask in plain English:

> check my reputation

Brand Pulse will ask you four quick questions the first time:

1. **What brand are we tracking?** (name + optional URL)
2. **What kind of thing is it?** (Person / Company / Product / App / Creator)
3. **If Playwright is installed:** Which of X, LinkedIn, IG, TikTok, FB are you logged into?
4. **How deep?** Quick (~3 min) / Standard (~10 min) / Deep (~20+ min)

Your answers save to `~/brand-pulse/config.md`. You won't be asked again.

## Step 5 — Read the report

You'll see the report directly in chat. It has:

- **Since Last Pulse** — what changed since your last run (shows up on run #2 onward)
- **Executive Summary** — 3–5 sentences
- **Top complaints, feature requests, and recommendations**
- **Detailed breakdown** per source
- **Coverage & blind spots** — honest accounting

Brand Pulse will also ask:

- Save as PDF? *(works on any OS — either via `pandoc` if installed, or styled HTML + "Cmd+P → Save as PDF")*
- Want to run on a competitor next?

The markdown version saves automatically to `~/brand-pulse/<brand-slug>/YYYY-MM-DD.md` so the next run can track trends.

---

## Common questions

**Q: Do I need any API keys?**
No. Public mode uses only free endpoints. Enhanced mode uses your own logged-in browser.

**Q: Is it safe to use on X and LinkedIn?**
Enhanced mode drives your own browser at human-like speed (3–5 second pauses between actions). It's doing what you'd do manually, faster. Throttled, not a bulk scraper. That said, ToS on those platforms technically discourage automation of any kind — use at your discretion.

**Q: Can I track my competitors too?**
Yes. `/reputation acme-corp` runs it on any brand. `/reputation --compare acme-corp` gives you a side-by-side diff against your default brand.

**Q: How do I reset the wizard?**
`/reputation --reconfigure`

**Q: Where are reports saved?**
`~/brand-pulse/<brand-slug>/YYYY-MM-DD.md`. Delete the folder to wipe history.

**Q: Can I schedule it to run weekly?**
Not built-in, but you can pair it with the `/loop` or `/schedule` skills if you have them installed.

---

Need help? Email hello@beginnersinai.org or post in the [Skool community](https://skool.com/beginnersinai).
