# Quick Start — The 44% Rule

**Time required:** 5 minutes
**You need:** Claude Code installed on your machine ([install guide](https://docs.claude.com/en/docs/claude-code/quickstart))

This is the absolute beginner version. Type each command exactly as shown.

---

## Step 1 — Add the Marketplace (30 seconds)

The 44% Rule lives in the **Beginners in AI marketplace**, which is a free catalog of AI plugins. You add the marketplace once, then install plugins from it.

In Claude Code, type:

```
/plugin marketplace add beginnersinai/claude-skills-marketplace
```

You'll see a confirmation message. The marketplace is now registered.

---

## Step 2 — Install The 44% Rule (30 seconds)

```
/plugin install the-44-percent-rule@beginnersinai-skills
```

Claude Code downloads the plugin and confirms installation.

---

## Step 3 — Turn on Auto-Updates (1 minute) ⭐ DON'T SKIP THIS ⭐

By default, Claude Code does **not** automatically update plugins from third-party marketplaces. That means when we ship a new version with bug fixes or new features, you won't get it unless you opt in.

Here's how to opt in (one time, takes 30 seconds):

1. Type `/plugin` and press Enter — this opens the plugin manager
2. Press **Tab** until you reach the **Marketplaces** tab
3. Select **beginnersinai-skills** from the list
4. Choose **Enable auto-update**
5. Press **Esc** to close the manager

Done. Every time Claude Code starts from now on, it will check for new versions and pull them automatically. You'll see a notification if anything was updated, and Claude will prompt you to run `/reload-plugins` to activate.

> **Why is this off by default?** Anthropic enables auto-update for the official marketplace they maintain, but disables it for third-party marketplaces (like Beginners in AI) so you have to explicitly trust the source. Once you enable it, you're saying "I trust this marketplace to send me updates."

---

## Step 4 — Run Your First Audit (3 minutes)

Open Claude Code in any project directory (a folder with code, documents, or anything you work on). Then type:

```
/the-44-percent-rule:map
```

The plugin will:
1. Ask you 5 plain-English questions about your business
2. Scan your workspace to see what tools and projects you already have
3. Map your AI usage across 10 core business functions
4. Identify the gaps (where AI is missing)
5. Generate a prioritized action plan saved as `AI-MAP-[today's-date].md`

The whole thing takes 2-5 minutes. You don't need to know anything about AI to answer the questions — just describe your business in your own words.

---

## Step 5 — Get Your Action Plan

After the map is generated, type:

```
/the-44-percent-rule:map-score
```

This scores every opportunity by:
- **Revenue Impact** (how much money it makes or saves)
- **Capital Reduction** (whether it eliminates a hire or expense)
- **Ease of Implementation** (whether you can do it today)

You get a ranked list. Items scoring 15+ with maximum ease are flagged as **"Press Send"** — meaning the infrastructure already exists, you just need to activate it.

That's the most valuable output. Start there.

---

## What If I Want Just One Project Audited?

Instead of `/the-44-percent-rule:map` (which scans everything), use:

```
/the-44-percent-rule:map-venture MyProjectName
```

It does a deep 10-function analysis of just that one project.

---

## How Often Should I Run It?

- **Once per quarter** is the typical cadence — businesses change, new AI tools emerge, your gaps shift
- **After any major business change** (new product launch, new market, new hire, restructure)
- **Whenever you feel stuck** about where to use AI next

The dedup logic in the plugin prevents it from re-flagging gaps you've already addressed, so re-runs are fast.

---

## Help — Something Isn't Working

### "Command not found"
You forgot the namespace prefix. It's `/the-44-percent-rule:map`, not just `/map`. Plugin commands are always prefixed.

### "Plugin not found in marketplace"
Run this to refresh the marketplace catalog:
```
/plugin marketplace update beginnersinai-skills
```
Then try installing again.

### "I installed it but nothing happens when I type /map"
Run this to reload all plugins in the current session:
```
/reload-plugins
```

### "I had the old AI Mapping Plugin installed"
The plugin was renamed on April 6, 2026. The old name (`ai-mapping`) and new name (`the-44-percent-rule`) are different plugins from Claude Code's perspective. To upgrade:

```
/plugin uninstall ai-mapping@beginnersinai-skills
/plugin install the-44-percent-rule@beginnersinai-skills
/reload-plugins
```

Then enable auto-update (Step 3 above) so future renames are handled smoothly.

### "I don't see the auto-update toggle"
Your Claude Code version might be too old. Update with:
- **Homebrew:** `brew upgrade claude-code`
- **npm:** `npm update -g @anthropic-ai/claude-code`
- **Native installer:** Re-run the install command from the [Setup guide](https://docs.claude.com/en/docs/claude-code/setup)

---

## The Research

This plugin is based on a real Harvard/INSEAD research paper. If you want to read it:

- **Paper:** "Mapping AI into Production: A Field Experiment on Firm Performance"
- **Authors:** Hyunjin Kim, Dahyeon Kim, Rembrand Koning
- **Published:** March 30, 2026
- **Sample size:** 515 startups
- **Plain-English explainer:** https://beginnersinai.org/mapping-ai-research-study/

**The 44% finding in one sentence:** Companies that were shown specific examples of how OTHER companies use AI found 44% more AI use cases in their own business than companies that weren't shown anything. This plugin automates that "showing" so you don't need to manually research how 50 other companies use AI.

---

## Next Steps

After your first audit:
1. **Read the action plan** Claude generates (`AI-MAP-[date].md`)
2. **Pick the highest-scoring "Press Send" opportunity** and implement it this week
3. **Re-run the audit in 90 days** to see what new opportunities have emerged
4. **Share results** in the Beginners in AI community: https://www.skool.com/beginnersinai

You can also explore the related articles:
- **The full plugin walkthrough**: https://beginnersinai.org/the-44-percent-rule/
- **The research paper, explained**: https://beginnersinai.org/mapping-ai-research-study/

---

**Made by [Beginners in AI](https://beginnersinai.org)** — turning AI research into practical tools for non-technical business owners.
