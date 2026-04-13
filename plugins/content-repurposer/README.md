# AI Content Repurposer

**Turn one piece of content into 10 platform-native formats.** Blog post to X thread, LinkedIn post, email newsletter, YouTube script, short-form video, carousel, podcast talking points, and more. Copy-paste ready.

---

## What It Is

A free Claude Code plugin that reads your existing content — blog posts, articles, transcripts, notes — and generates platform-specific versions for 10 different channels. Each output is formatted natively for its platform, not a copy-paste of the original.

Built by [Beginners in AI](https://beginnersinai.org) for solo creators, small business owners, and anyone who writes content but only publishes it once.

## What's In the Plugin

### 3 Slash Commands

| Command | What It Does |
|---------|-------------|
| `/content-repurposer:repurpose` | One source → all 10 formats → output folder with copy-paste ready files |
| `/content-repurposer:adapt` | One source → one platform → 3 variations to choose from |
| `/content-repurposer:batch` | Multiple sources → content calendar with scheduled posts across platforms |

### 3 Specialized Agents

| Agent | Role |
|-------|------|
| `content-analyzer` | Breaks down source content into thesis, key points, quotes, tone, and platform potential |
| `format-writer` | Generates platform-native content following character limits, structure rules, and hook patterns |
| `distribution-planner` | Plans multi-platform publishing schedules and content calendars |

### 1 Auto-Activating Skill

The `content-repurposing` skill activates automatically when you discuss content distribution, repurposing, or multi-platform publishing in normal conversation — no slash command needed.

### Reference Materials

| File | Contains |
|------|----------|
| `platform-specs.md` | Character limits, structure templates, tone rules, posting cadence for all 10 formats |
| `hook-patterns.md` | 8 proven hook formulas with per-platform effectiveness ratings |
| `distribution-strategy.md` | The cascade model, 48-hour freshness rule, and scheduling principles |

## The 10 Formats

| # | Format | Platform | What You Get |
|---|--------|----------|-------------|
| 1 | Thread | X/Twitter | 5-12 tweet thread with hook, points, and CTA |
| 2 | Post | LinkedIn | Under 3,000 chars, professional tone, question-driven close |
| 3 | Newsletter | Email | Subject line, preview text, 400-700 word body, PS line |
| 4 | Carousel | LinkedIn | 7-10 slides, text-only (ready for Canva), one idea per slide |
| 5 | Long Video | YouTube | 8-12 min script with hooks, B-roll notes, timestamps |
| 6 | Short Video | TikTok/Reels/Shorts | 30-60 sec script with text overlays and pacing marks |
| 7 | Blog Summary | SEO/Syndication | 200-400 words with meta description and keywords |
| 8 | Quote Graphics | Instagram/Pinterest | 5-8 pull quotes with style suggestions (ready for Canva) |
| 9 | Talking Points | Podcast | 8-12 bullet points with sub-bullets (NOT a script) |
| 10 | Community Post | Skool/Discord/Groups | 100-250 words ending with a discussion question |

## How to Install

### Option 1: Marketplace (recommended)

```
/plugin marketplace add beginnersinai/claude-skills-marketplace
/plugin install content-repurposer@beginnersinai-skills
```

### Option 2: Direct Download

1. Download the ZIP from [GitHub](https://github.com/beginnersinai/content-repurposer)
2. In Claude Code, go to Plugins
3. Drag the ZIP file in
4. Done

### Option 3: Git Clone

```bash
git clone https://github.com/beginnersinai/content-repurposer.git
```

Then add the folder as a plugin in Claude Code.

## How to Use It

### Quick Start: Repurpose One Article

```
/content-repurposer:repurpose
```

Point it at a blog post, article, or any written content. It will generate all 10 formats in a folder you can open and copy from.

### Deep Dive: Adapt for One Platform

```
/content-repurposer:adapt
```

Choose a platform (e.g., "LinkedIn" or "Twitter") and get 3 different versions to choose from — a straight repurpose, a hook-first version, and a story-led version.

### Plan Ahead: Batch Content Calendar

```
/content-repurposer:batch
```

Point it at a folder of articles and get a week-by-week content calendar with every piece scheduled and ready to post.

## The Distribution Framework

This plugin is built around three core principles:

### 1. Repurposing ≠ Cross-Posting

The biggest mistake in content distribution is posting the same text everywhere. Algorithms detect it, audiences notice it, and engagement drops across every platform. Each format should feel like it was originally written for that platform.

### 2. The Cascade Model

Don't publish everything at once. Start with your owned channels (email), then move to social (LinkedIn, X), then engagement formats (carousel, community), then video, then the long tail (SEO, quotes, podcast). Each stage reaches a different audience.

### 3. Hook Diversity

Every format opens with its strongest line — but each format uses a different hook. A stat-lead for Twitter, a story-open for email, a contrarian take for LinkedIn. Same idea, different door.

## Keeping Up to Date

By default, Claude Code does **not** auto-update plugins from third-party marketplaces. To get future updates automatically:

1. Type `/plugin` and press Enter
2. Press **Tab** to reach the **Marketplaces** tab
3. Select **beginnersinai-skills**
4. Choose **Enable auto-update**

After enabling, Claude Code will check for updates on every startup.

### Manual Update

```
/plugin marketplace update beginnersinai-skills
/plugin update content-repurposer@beginnersinai-skills
/reload-plugins
```

## Read More

- [Full article: How the AI Content Repurposer works](https://beginnersinai.org/the-content-repurposer/)
- [Download page](https://beginnersinai.org/get-the-content-repurposer/)
- [All free Claude Code skills](https://beginnersinai.org/skills/)
- [Beginners in AI community](https://skool.com/beginnersinai)

---

**Made by [Beginners in AI](https://beginnersinai.org)** — turning practical AI knowledge into tools for non-technical professionals.
