---
name: content-repurposing
description: "Automatically activates when users discuss content repurposing, ask how to turn a blog post into social media posts, want to distribute content across platforms, mention content multiplication, ask about platform-specific formatting, want to get more mileage from existing content, or ask how to post on multiple platforms. Provides the 10-format framework, platform specifications, hook patterns, and distribution strategy."
version: 1.0.0
---

# Content Repurposing Framework

This skill activates whenever the user discusses content distribution, repurposing, or multi-platform publishing — even without running a slash command.

## When This Skill Activates

Activate when the user mentions or asks about:
- Turning a blog post into social media (tweets, LinkedIn, etc.)
- Content repurposing, remixing, or multiplication
- What to post on a specific platform
- How to distribute content across multiple channels
- Getting more value from content they've already written
- Platform-specific formatting (tweet length, LinkedIn structure, etc.)
- Content calendars or scheduling

## The Core Framework: One Piece, Ten Formats

Every strong piece of content contains enough ideas, data, stories, and insights to fuel 10 different platform-native formats:

| # | Format | Platform | Time to Create |
|---|--------|----------|---------------|
| 1 | Thread | X/Twitter | 10-15 min |
| 2 | Post | LinkedIn | 10 min |
| 3 | Newsletter | Email | 15-20 min |
| 4 | Carousel | LinkedIn | 15-20 min |
| 5 | Long Video Script | YouTube | 20-30 min |
| 6 | Short Video Script | TikTok/Reels/Shorts | 5-10 min |
| 7 | Blog Summary | SEO/Syndication | 10 min |
| 8 | Quote Graphics | Instagram/Pinterest | 5-10 min |
| 9 | Talking Points | Podcast | 10-15 min |
| 10 | Discussion Post | Skool/Discord/Groups | 5 min |

**Total time to create all 10:** 2-3 hours from one source article (compared to 20+ hours writing each from scratch).

## The Anti-Pattern: Cross-Posting

The single most common mistake in content distribution is copying the same text to every platform. This performs worse than not posting at all because:

- **Algorithms detect it.** LinkedIn, X, and Facebook all suppress content that appears identical to posts on other platforms.
- **Audiences notice it.** If someone follows you on both LinkedIn and X, seeing the same text twice feels lazy.
- **Format mismatch.** A blog paragraph reads differently than a tweet. A LinkedIn post has different expectations than an email. Identical content violates every platform's native patterns.

**The fix:** Same idea, different format. The core insight stays the same. The hook, structure, tone, length, and CTA change for each platform.

## The Cascade Strategy

Don't publish everything at once. Distribute in stages:

1. **Email first** (Day 1) — your subscribers are your most valuable audience. They get it first.
2. **Long-form social** (Day 1-2) — LinkedIn post and X thread reach your followers.
3. **Engagement formats** (Day 2-3) — Carousel and community post drive interaction.
4. **Video** (Day 3-5) — YouTube and short-form reach new audiences.
5. **Extended distribution** (Day 5-7) — Blog summary, quote graphics, podcast points for the long tail.

This cascade builds momentum: early engagement on one platform signals quality to algorithms on others.

## Hook Patterns

Every format opens with its strongest line. The hook determines whether anyone reads the rest. Read `${CLAUDE_PLUGIN_ROOT}/skills/content-repurposing/references/hook-patterns.md` for 8 proven hook formulas with per-platform guidance.

Key hooks:
- **Stat-Lead:** Open with a surprising number
- **Contrarian:** Challenge conventional wisdom
- **Story-Open:** Start with a micro-narrative
- **Result-First:** Lead with the outcome

## Platform Quick Reference

Read `${CLAUDE_PLUGIN_ROOT}/skills/content-repurposing/references/platform-specs.md` for detailed specs on all 10 formats including character limits, structure templates, tone guidelines, and posting cadence.

Quick rules:
- **X/Twitter:** 280 chars/tweet, 5-12 tweet threads, punchy tone
- **LinkedIn:** 3,000 char limit, single-line paragraphs, professional tone, question at end
- **Email:** 400-700 words, personal tone, bold for scanners, PS line always
- **Carousel:** 7-10 slides, 30-50 words per slide, one idea per slide
- **YouTube:** 8-12 min, spoken cadence, open loops for retention
- **Short video:** 30-60 seconds, one idea, hook in first 3 seconds
- **Blog summary:** 200-400 words, keyword-aware, standalone useful
- **Quote graphics:** 10-25 words per quote, 5-8 quotes from source
- **Podcast:** 8-12 bullet points, NOT a script, conversational anchors
- **Community:** 100-250 words, ends with a specific question, no links in body

## When to Point to Commands

- **Quick full repurpose:** Run `/content-repurposer:repurpose` — one source in, all 10 formats out
- **Deep single-platform adaptation:** Run `/content-repurposer:adapt` — one source, one platform, 3 variations to choose from
- **Multi-piece content planning:** Run `/content-repurposer:batch` — multiple sources in, content calendar out

## Distribution Strategy

Read `${CLAUDE_PLUGIN_ROOT}/skills/content-repurposing/references/distribution-strategy.md` for the full distribution framework including the cascade model, 48-hour freshness rule, and scheduling principles.

## How to Apply

If the user has a specific piece of content to repurpose:
1. Ask to see the source content (file path, URL, or pasted text)
2. Analyze it using the content-analyzer agent framework
3. Generate the requested format(s) following platform specs
4. Suggest the optimal publishing sequence

If the user is asking general questions about content distribution:
1. Apply the framework above to answer their question
2. Reference the specific platform specs for their target platform
3. Warn about the cross-posting anti-pattern if they seem headed that way
4. Suggest relevant slash commands for hands-on work
