---
name: repurpose
description: "This skill should be used when the user types '/repurpose', asks to 'repurpose my content', 'turn this into social media posts', 'create a twitter thread from this', 'make this into 10 formats', 'repurpose this blog post', or wants to transform a single piece of content into multiple platform-native outputs. Generates all 10 formats from one source."
version: 1.0.0
---

# /repurpose — Turn One Piece of Content Into 10 Formats

This is the main command. It takes a single piece of source content and generates all 10 platform-native formats from it, saved as copy-paste ready files.

## Step 1: Get the Source Content

Ask the user for the source content. Accept any of these inputs:

- **File path:** Read the file directly (supports .md, .txt, .html, .pdf)
- **URL:** Fetch the page and extract the content
- **Pasted text:** Work with whatever they paste into the conversation
- **"Use my latest":** Search the workspace for the most recently modified .md or .txt file

If the user doesn't specify, ask:

> "What content do you want to repurpose? You can give me a file path, paste the text, or say 'use my latest' and I'll find your most recent article."

Read the content completely before proceeding. Do not ask the user to confirm the content — just read it and move forward.

## Step 2: Analyze the Content

Use the `content-analyzer` agent to produce a full content analysis:
- Core thesis (one sentence)
- 3-5 key points (ranked by importance)
- Statistics and data points
- Quotable lines (verbatim from source)
- Target audience
- Tone classification
- Content type
- Platform potential for all 10 formats
- 3 suggested hooks

Do NOT show the full analysis to the user. Instead, show a brief summary:

> "**Source:** [Title or description] ([word count] words)
> **Core idea:** [One sentence thesis]
> **Best platforms:** [Top 3]
> **Generating all 10 formats now...**"

## Step 3: Ask One Question

Ask exactly one question to personalize the output:

> "Which platforms do you actually use? I'll generate all 10 formats, but I'll put extra care into the ones that matter to you."

If the user lists specific platforms, prioritize quality on those. If they say "all of them" or don't have a preference, use the default priority from the distribution strategy reference.

If the user seems impatient or says "just do it," skip this question and use defaults.

## Step 4: Generate All 10 Formats

Use the `format-writer` agent to generate each format. The format-writer MUST read the reference files before writing:
- `${CLAUDE_PLUGIN_ROOT}/skills/content-repurposing/references/platform-specs.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/content-repurposing/references/hook-patterns.md`

For each format:
1. Select the best hook pattern based on the content analysis and platform
2. Apply the platform-specific structure template
3. Respect character/word limits
4. Adapt the tone for the platform
5. Write copy-paste ready content — no placeholders, no "[insert here]"

**Critical:** Each format must use a DIFFERENT hook. Do not open 10 formats with the same sentence. Vary the angle, entry point, and framing.

## Step 5: Create Output Files

Create a folder in the working directory:

```
REPURPOSED-[title-slug]-[YYYY-MM-DD]/
├── 00-source-analysis.md
├── 01-twitter-thread.md
├── 02-linkedin-post.md
├── 03-email-newsletter.md
├── 04-linkedin-carousel.md
├── 05-youtube-script.md
├── 06-short-video-script.md
├── 07-blog-summary.md
├── 08-quote-graphics.md
├── 09-podcast-talking-points.md
├── 10-community-post.md
└── README.md
```

**Each format file should include:**
```markdown
# [Format Name]

**Platform:** [Platform]
**Characters/Words:** [Count]
**Hook pattern:** [Which pattern was used]
**Copy-paste ready:** Yes

---

[THE ACTUAL CONTENT — ready to paste directly into the platform]

---

**Publishing tip:** [One sentence about when/how to post this]
```

**The README.md should include:**
```markdown
# Repurposed Content: [Source Title]

Generated [date] from [source description]

## Quick Links

| # | Format | Platform | File | Status |
|---|--------|----------|------|--------|
| 1 | Thread | X/Twitter | [01-twitter-thread.md] | Ready to post |
| 2 | Post | LinkedIn | [02-linkedin-post.md] | Ready to post |
| ... | ... | ... | ... | ... |

## Suggested Publishing Order

1. **Today:** Email newsletter → LinkedIn post → X thread
2. **Tomorrow:** LinkedIn carousel → Community post
3. **Day 3-5:** YouTube script → Short-form video
4. **Day 5-7:** Blog summary → Quote graphics → Podcast points

## Source Analysis Summary

[Brief analysis from the content-analyzer]
```

## Step 6: Present the Summary

After generating all files, tell the user:

> "Done. I created [N] pieces of content from your [source type]:
>
> **[Folder name]/**
>
> | Format | Platform | Ready |
> |--------|----------|-------|
> | Thread (7 tweets) | X/Twitter | ✓ |
> | Post (1,200 chars) | LinkedIn | ✓ |
> | ... | ... | ... |
>
> **Start here:** Post the email newsletter today, then the LinkedIn post and X thread tomorrow.
>
> **Strongest formats:** [Top 3 based on content analysis and why]
>
> Open any file and copy-paste directly into the platform. Each one is ready to publish."

## Important Rules

- Never generate placeholder content. Everything must be real, specific, and ready to publish.
- Never use the same hook across multiple formats. Vary the opening.
- If the source content is thin (under 300 words), tell the user: "This source is short — I'll generate the 4-5 formats it's strongest for rather than stretching it across all 10."
- Respect every character/word limit in the platform specs. A tweet over 280 characters is useless. A LinkedIn post over 3,000 characters won't publish.
- Include the publishing order recommendation. Users need to know what to post first, not just what was generated.
