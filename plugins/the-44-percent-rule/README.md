# The 44% Rule — Find 44% More AI Use Cases In Your Business

> **The 44% Rule:** A research finding (Kim, Kim & Koning, 2026) — businesses shown how other companies reorganize around AI find **44% more AI use cases**, complete **12% more tasks**, are **18% more likely to acquire paying customers**, and generate **1.9x higher revenue**. This plugin automates that "showing" so any business can apply the rule in under 10 minutes.

## What It Is

**The 44% Rule** is a free Claude Code plugin that automates a research-backed audit of any business to find where AI should be deployed but isn't.

It's based on *"Mapping AI into Production: A Field Experiment on Firm Performance"* (Kim, Kim & Koning, March 2026) — a study of 515 startups that found the #1 bottleneck to getting value from AI isn't capability. **It's discovery.** Most people use AI for writing and chatbots and stop there. The firms that were shown how others reorganized around AI found 44% more use cases and generated 1.9x higher revenue.

This plugin automates that "showing" — it scans your workspace, maps where AI is and isn't being used across **10 core business functions**, and generates a prioritized action plan.

---

## Quick Install (5 Minutes)

The fastest way to install is from the **Beginners in AI marketplace**.

### Step 1 — Add the marketplace (one time, ~30 seconds)

In Claude Code, type:

```
/plugin marketplace add beginnersinai/claude-skills-marketplace
```

This registers the marketplace catalog. No plugins are installed yet — you're just telling Claude Code where to find them.

### Step 2 — Install The 44% Rule

```
/plugin install the-44-percent-rule@beginnersinai-skills
```

Claude Code downloads the plugin and installs it. Done.

### Step 3 — Turn on auto-updates (HIGHLY RECOMMENDED — see below)

By default, third-party marketplaces have auto-updates **disabled**. That means new versions of the plugin won't reach you automatically. To enable auto-updates so you always have the latest version:

1. Type `/plugin` to open the plugin manager
2. Press **Tab** to navigate to the **Marketplaces** tab
3. Select **beginnersinai-skills** from the list
4. Choose **Enable auto-update**

From now on, every time you start Claude Code, it will check for new versions of The 44% Rule (and any other plugins from this marketplace) and pull them automatically. You'll see a notification if anything updates, and you just run `/reload-plugins` to activate the new version.

### Step 4 — Run your first audit

In any project directory, type:

```
/the-44-percent-rule:map
```

That's it. The plugin walks you through a 5-question discovery, then maps your workspace across all 10 functions and generates a prioritized action plan in under 10 minutes.

---

## Alternative Install Methods

If you don't want to use the marketplace, two other paths:

### A. Direct ZIP install

1. Download `the-44-percent-rule.zip` from [Releases](https://github.com/beginnersinai/the-44-percent-rule/releases) (or click **Code → Download ZIP** above)
2. In **Claude Cowork**: Customize → click **+** next to "Personal plugins" → drag the ZIP in
3. Type `/the-44-percent-rule:map` to start

ZIP installs do NOT receive auto-updates. You'll need to manually re-download and reinstall when new versions ship.

### B. Local development install

For testing or modifying the plugin yourself:

```
git clone https://github.com/beginnersinai/the-44-percent-rule.git
claude --plugin-dir ./the-44-percent-rule
```

Local-dir installs are only active for that Claude Code session.

---

## What's In the Plugin

### 3 Slash Commands

| Command | What It Does |
|---------|-------------|
| `/the-44-percent-rule:map` | Full workspace scan. Discovers all your projects, maps AI usage across 10 functions for each, identifies gaps, scores opportunities, generates a complete AI Map report. |
| `/the-44-percent-rule:map-venture [name]` | Focused audit of a single project or business. Same 10-function analysis but deep on one venture. |
| `/the-44-percent-rule:map-score` | Scores and ranks all opportunities found by `/map`. Prioritizes by revenue impact, capital reduction, and ease of implementation. |

> **Note on namespacing:** Plugin commands in Claude Code are always prefixed with the plugin name to prevent conflicts between plugins. So `/map` becomes `/the-44-percent-rule:map`. After typing `/` you'll see autocomplete suggestions.

### 3 Specialized AI Agents

| Agent | Role | Color |
|-------|------|-------|
| **Venture Scanner** | Explores your workspace to discover and inventory all projects, businesses, and ventures | Cyan |
| **Gap Finder** | Maps AI usage across 10 functions and identifies where AI is absent | Green |
| **Priority Scorer** | Scores opportunities and creates a ranked action plan | Yellow |

### 1 Auto-Activating Skill

The audit skill activates automatically whenever you discuss AI adoption strategy, ask where to use AI, or mention the mapping problem. It loads the 10-function framework and examples without you needing to run a command.

### Reference Materials

- **Ten Functions Framework** — The complete 10 production functions where AI can create value, with specific indicators for each
- **Examples From Other Firms** — Real examples of how firms have deployed AI across all 10 functions (this is the "treatment" from the research paper — the "showing" that produces the 44% lift)
- **Case Studies From the Paper** — Gamma, RyzLabs, FazeShift, Ranger and the specific AI deployments that generated revenue

---

## The 10 Production Functions

Every business has 10 functions where AI can create value. Most only use AI in 1-2 of them:

1. **Product Development** — Building and improving your core offering
2. **Strategy & Planning** — Business decisions and competitive positioning
3. **Marketing & Growth** — Customer acquisition and audience building
4. **Sales & Revenue** — Converting prospects and optimizing pricing
5. **Customer Success** — Retention, satisfaction, and churn prevention
6. **Finance & Pricing** — Revenue tracking, forecasting, and pricing intelligence
7. **Operations & Logistics** — Workflows, processes, and resource allocation
8. **Content Production** — Creating content (where most people already use AI)
9. **Data & Analytics** — Measurement, reporting, and insights
10. **System Administration** — Maintaining and optimizing your tools and AI systems

If your AI usage is concentrated only in #8 (Content) and maybe #3 (Marketing), you have the mapping problem. The 44% Rule fixes it.

---

## How to Use It

### Quick Start
1. Open Claude Code in any project directory
2. Type `/the-44-percent-rule:map`
3. Wait for the scan to complete (takes 2-5 minutes depending on workspace size)
4. Review the generated `AI-MAP-[date].md` report
5. Type `/the-44-percent-rule:map-score` to get a prioritized action plan

### For a Single Project
1. Type `/the-44-percent-rule:map-venture MyProject`
2. Get a focused 10-function analysis with specific recommendations

### The Scoring System
Each opportunity is scored on:
- **Revenue Impact** (1-5, weighted 2x) — How much money does this make or save?
- **Capital Reduction** (1-5) — Does this eliminate a hire or expense?
- **Ease of Implementation** (1-5) — Can you do this today?

**Composite Score** = (Revenue × 2) + Capital + Ease. Maximum: 20 points.

Opportunities scoring 15+ with Ease = 5 are flagged as **"Press Send"** — infrastructure exists, nobody activated it.

---

## Keeping Up to Date

This is the part most people miss. By default, Claude Code does NOT automatically update plugins from third-party marketplaces. You have to opt in.

### The auto-update toggle (do this once)

1. Open Claude Code
2. Type `/plugin`
3. Press **Tab** until you see the **Marketplaces** tab
4. Select **beginnersinai-skills** from the list
5. Choose **Enable auto-update**

From now on, every time Claude Code starts, it will:
1. Check the marketplace for new plugin versions
2. Pull any updates automatically
3. Show you a notification if anything was updated
4. Wait for you to run `/reload-plugins` to activate the changes

You'll never have to think about updating again.

### Manual update (if you skipped the auto-update toggle)

If you didn't enable auto-update, you can manually pull the latest version anytime:

```
/plugin marketplace update beginnersinai-skills
/plugin update the-44-percent-rule@beginnersinai-skills
/reload-plugins
```

The first command refreshes the marketplace catalog. The second command pulls any new version of this specific plugin. The third command activates the new version without restarting Claude Code.

### Checking your version

To see what version of The 44% Rule you currently have:

1. Type `/plugin` to open the plugin manager
2. Press **Tab** to the **Installed** tab
3. Find **The 44% Rule** in the list
4. The version number is displayed alongside the name

If you want the absolute latest, compare against the version at https://github.com/beginnersinai/the-44-percent-rule/blob/main/.claude-plugin/plugin.json

---

## Uninstalling

If you ever want to remove the plugin:

```
/plugin uninstall the-44-percent-rule@beginnersinai-skills
```

Or via the UI: `/plugin` → **Installed** tab → select **The 44% Rule** → **Uninstall**.

---

## The Research Behind The 44% Rule

**Paper**: *"Mapping AI into Production: A Field Experiment on Firm Performance"*
**Authors**: Hyunjin Kim (INSEAD), Dahyeon Kim (INSEAD), Rembrand Koning (Harvard Business School)
**Date**: March 30, 2026
**Sample**: 515 startups

**Key findings**:
- **44% more AI use cases** discovered when shown how others use AI ← **the 44% Rule**
- 12% more tasks completed
- 18% more likely to acquire paying customers
- 1.9x higher revenue
- 39.5% less demand for external capital
- No increase in labor demand
- Gains largest at the 90th percentile — AI amplifies winners

**The core insight**: The bottleneck is discovering **where** to deploy AI, not AI capability. This plugin automates that discovery so you don't have to read the paper or hire a consultant to apply the finding.

---

## Read More

- **Plugin landing page**: https://beginnersinai.org/get-the-44-percent-rule/
- **Full article walkthrough**: https://beginnersinai.org/the-44-percent-rule/
- **The research paper, explained for beginners**: https://beginnersinai.org/mapping-ai-research-study/
- **Quick Start Guide**: See `QUICKSTART.md` in this repo

---

## Version History & Renames

**v1.1.0 (April 6, 2026)** — Plugin renamed from "AI Mapping Plugin" to "The 44% Rule" to make the value proposition clearer at a glance. The internal package name also changed from `ai-mapping` to `the-44-percent-rule`. Skill commands are now namespaced as `/the-44-percent-rule:map` etc.

If you had **v1.0.0 installed under the old name `ai-mapping`**, Claude Code treats this as a different plugin and will NOT auto-migrate. To upgrade:

1. Uninstall the old plugin: `/plugin uninstall ai-mapping@beginnersinai-skills`
2. Install the new one: `/plugin install the-44-percent-rule@beginnersinai-skills`
3. Enable auto-update on the marketplace (see "Keeping Up to Date" above) so future updates land automatically

Going forward, the plugin will receive standard version-bump updates (1.1.0 → 1.1.1 → 1.2.0 → etc.) under the new name. As long as you have auto-update enabled, you won't need to think about updates.

**v1.0.0 (April 5, 2026)** — Initial release as "The AI Mapping Plugin" (`ai-mapping`).
