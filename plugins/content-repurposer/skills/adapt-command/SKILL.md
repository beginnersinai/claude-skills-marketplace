---
name: adapt
description: "This skill should be used when the user types '/adapt', asks to 'adapt this for LinkedIn', 'rewrite this for Twitter', 'make a YouTube script from this', 'write this as an email', or wants to transform content for one specific platform with multiple variations to choose from. Generates 3 variations for deep single-platform adaptation."
version: 1.0.0
---

# /adapt — Deep Adaptation for One Platform

Unlike `/repurpose` which generates all 10 formats at standard quality, `/adapt` focuses on one platform and gives the user 3 variations to choose from. Use this when the user cares deeply about one specific output.

## Step 1: Get the Source Content

Same as `/repurpose` — accept file path, URL, pasted text, or "use my latest."

## Step 2: Get the Target Platform

Ask which platform if not specified:

> "Which platform are you adapting this for?"

Accept any of these inputs and map to the correct format:

| User Says | Maps To |
|-----------|---------|
| twitter, X, tweet, thread | X/Twitter Thread |
| linkedin, LI | LinkedIn Post |
| email, newsletter, mail | Email Newsletter |
| carousel, slides | LinkedIn Carousel |
| youtube, YT, video script | YouTube Script |
| tiktok, reels, shorts, short video | Short-Form Video Script |
| blog, summary, SEO, syndication | Blog Summary |
| quotes, graphics, canva, instagram | Quote Graphics |
| podcast, talking points, episode | Podcast Talking Points |
| community, skool, discord, facebook group | Community Post |

## Step 3: Deep Analysis

Use the `content-analyzer` agent, but go deeper for the selected platform:

1. Read `${CLAUDE_PLUGIN_ROOT}/skills/content-repurposing/references/platform-specs.md` — focus on the target platform's section
2. Read `${CLAUDE_PLUGIN_ROOT}/skills/content-repurposing/references/hook-patterns.md` — identify the 3 best hook patterns for this content + platform combination

From the content analysis, identify:
- The strongest angle for this specific platform
- The best data points or quotes for this platform's audience
- The tone adjustment needed for this platform
- The ideal length (within the platform's range)

## Step 4: Generate 3 Variations

Each variation uses a different approach to the same content:

### Variation A: "Straight Repurpose"
Faithful to the original content. Adapted for the platform's format and constraints, but keeps the same structure and emphasis as the source. Best when the source is already strong and just needs formatting.

### Variation B: "Hook-First"
Leads with the most provocative, surprising, or data-driven element. Restructures the content to front-load what grabs attention on this platform. Best when the source buries the lead or opens slowly.

### Variation C: "Story-Led"
Wraps the content in a narrative or personal angle. Opens with an anecdote, experience, or "I noticed..." framing. Best when the source is informational and needs a human entry point.

## Step 5: Output

Create a single file: `ADAPTED-[platform]-[title-slug]-[YYYY-MM-DD].md`

```markdown
# Adapted for [Platform]: [Source Title]

**Source:** [Title] ([word count] words)
**Target platform:** [Platform name]
**Date:** [YYYY-MM-DD]

---

## Variation A: Straight Repurpose

**Approach:** Faithful adaptation — same structure, platform-native format
**Hook pattern:** [Pattern name]
**Length:** [Character/word count]

---

[The actual content, copy-paste ready]

---

**Why this works:** [1-2 sentences on when to use this version]

---

## Variation B: Hook-First

**Approach:** Restructured to lead with the strongest element
**Hook pattern:** [Pattern name]
**Length:** [Character/word count]

---

[The actual content, copy-paste ready]

---

**Why this works:** [1-2 sentences on when to use this version]

---

## Variation C: Story-Led

**Approach:** Wrapped in narrative — personal angle, anecdote opening
**Hook pattern:** [Pattern name]
**Length:** [Character/word count]

---

[The actual content, copy-paste ready]

---

**Why this works:** [1-2 sentences on when to use this version]

---

## Recommendation

**Use Variation [A/B/C]** because [specific reason based on the content and platform].

[If applicable: "Variation [X] is a close second — use it if [condition]."]
```

## Step 6: Present to User

> "I created 3 versions of your [format] for [platform]:
>
> **A. Straight Repurpose** — faithful to the original, formatted for [platform]
> **B. Hook-First** — leads with [the strongest element]
> **C. Story-Led** — opens with [the narrative angle]
>
> **My pick: Variation [X]** — [one sentence why]
>
> All three are in `ADAPTED-[platform]-[slug]-[date].md`, ready to copy and paste."

## Important Rules

- All three variations must be meaningfully different. Not just "the same text with different opening sentences." The structure, emphasis, and flow should differ.
- Each variation must be independently copy-paste ready.
- The recommendation must have a specific reason, not "it's the best one."
- Respect platform limits for all three variations. A LinkedIn post over 3,000 characters is useless regardless of which variation it is.
