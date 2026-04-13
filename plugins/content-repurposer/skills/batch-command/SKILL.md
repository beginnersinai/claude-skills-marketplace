---
name: batch
description: "This skill should be used when the user types '/batch', asks to 'create a content calendar', 'repurpose all my recent content', 'plan my content distribution', 'batch repurpose these articles', or wants to turn multiple source pieces into a scheduled multi-platform content plan."
version: 1.0.0
---

# /batch — Multi-Source Content Calendar

Takes multiple pieces of source content and generates a complete content calendar with platform-native formats scheduled across days and weeks.

## Step 1: Collect Source Material

Ask the user to point to their content. Accept:

- **Folder path:** Scan the folder for .md, .txt, and .html files
- **Multiple file paths:** Read each one
- **"Scan my workspace":** Search the working directory for content files modified in the last 30 days

```
"Point me to your content. You can give me a folder path, list specific files, or say 'scan my workspace' and I'll find your recent articles."
```

If scanning, look for:
- `.md` files in common content directories (posts/, articles/, blog/, content/, drafts/)
- `.txt` files over 200 words
- `.html` files that contain article-like content
- Exclude: config files, templates, README files, changelogs

## Step 2: Analyze Each Source

Use the `content-analyzer` agent on each piece:

1. Core topic and angle
2. Content quality assessment (deep/solid/thin)
3. Evergreen vs. time-sensitive
4. Platform potential (best 3, weakest 2)

Then compare across sources:
- Flag any sources with >60% topic overlap (redundancy risk)
- Identify topic clusters that could build on each other
- Note which sources are strong enough for all 10 formats vs. better suited for 3-5

Show the user a summary:

> "Found [N] pieces of content:
>
> | # | Source | Words | Type | Strength | Best Platforms |
> |---|--------|-------|------|----------|----------------|
> | 1 | [Title] | [count] | [type] | All 10 formats | [top 3] |
> | 2 | [Title] | [count] | [type] | 5-6 formats | [top 3] |
> | ... | ... | ... | ... | ... | ... |
>
> **Overlap flag:** Sources 2 and 4 cover similar ground — I'll distribute them to different platforms.
>
> Ready to generate the calendar?"

## Step 3: Ask Planning Questions

Ask at most 2 questions:

1. **"Which platforms do you actively publish on?"** — to prioritize the right channels
2. **"How many weeks should this calendar cover?"** — default to 2 weeks if they don't specify

## Step 4: Generate Content

Use the `format-writer` agent to generate the formats for each source, following the same rules as `/repurpose`:
- Read platform specs and hook patterns references
- Different hook per format per source
- Copy-paste ready output
- Respect all platform limits

Skip formats that are a weak fit for a given source (don't stretch thin content).

## Step 5: Build the Calendar

Use the `distribution-planner` agent to schedule everything. The planner MUST read:
- `${CLAUDE_PLUGIN_ROOT}/skills/content-repurposing/references/platform-specs.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/content-repurposing/references/distribution-strategy.md`

Calendar rules:
- Follow the cascade model (email → long-form social → engagement → video → long tail)
- Never post the same source to the same platform twice in one week
- Interleave topics so the audience doesn't get the same theme multiple days in a row
- Include one rest day per week (no content published)
- Max 3 posts per platform per day

## Step 6: Create Output

Create a folder: `CONTENT-CALENDAR-[YYYY-MM-DD]/`

```
CONTENT-CALENDAR-[YYYY-MM-DD]/
├── calendar.md           (the full calendar with schedule)
├── source-1/
│   ├── 01-twitter-thread.md
│   ├── 02-linkedin-post.md
│   ├── ... (only formats generated for this source)
│   └── README.md
├── source-2/
│   ├── 01-twitter-thread.md
│   ├── ... 
│   └── README.md
├── content-bank.md       (formats generated but not scheduled)
└── README.md             (overview and instructions)
```

**calendar.md format:**

```markdown
# Content Calendar: [Date Range]

**Sources:** [N] pieces of content
**Total publishable pieces:** [N]
**Calendar length:** [N] weeks
**Platforms covered:** [list]

## Week 1: [Date Range]

| Day | Platform | Format | Source | File | Status |
|-----|----------|--------|--------|------|--------|
| Mon | Email | Newsletter | [Source 1] | source-1/03-email-newsletter.md | Ready |
| Mon | LinkedIn | Post | [Source 1] | source-1/02-linkedin-post.md | Ready |
| Tue | X | Thread | [Source 1] | source-1/01-twitter-thread.md | Ready |
| Tue | LinkedIn | Carousel | [Source 2] | source-2/04-linkedin-carousel.md | Ready |
| Wed | Community | Post | [Source 1] | source-1/10-community-post.md | Ready |
| Thu | YouTube | Script | [Source 2] | source-2/05-youtube-script.md | Ready |
| Fri | Short Video | Script | [Source 1] | source-1/06-short-video-script.md | Ready |
| Sat-Sun | — | Rest | — | — | — |

## Week 2: [Date Range]
[Same format]

## Content Bank

Formats generated but not scheduled (publish when you have a gap):

| Source | Format | File |
|--------|--------|------|
| [Source 3] | Quote Graphics | source-3/08-quote-graphics.md |
| ... | ... | ... |
```

## Step 7: Present the Summary

> "Done. Here's your content calendar:
>
> **[N] sources → [X] publishable pieces across [Z] platforms over [W] weeks**
>
> **This week's priorities:**
> 1. Monday: Send [Source 1] newsletter + post LinkedIn version
> 2. Tuesday: Post X thread from [Source 1] + LinkedIn carousel from [Source 2]
> 3. [Continue...]
>
> Everything is in `CONTENT-CALENDAR-[date]/`. Open any file and copy-paste directly into the platform.
>
> **Content bank:** [Y] extra pieces ready whenever you need them."

## Important Rules

- Don't generate formats for sources that are too thin. If a 200-word piece can only support 3 formats, generate 3. Don't pad to 10.
- Don't schedule more than 2 weeks out unless the user asks. Content becomes stale.
- Always include the content bank for generated-but-unscheduled formats.
- The calendar must be actionable — specific days, specific files, specific platforms. Not "post something on LinkedIn this week."
- Flag redundancy clearly. If two sources are too similar, the user should know before publishing both.
