---
name: map
description: "This skill should be used when the user types '/map', asks to 'run an AI mapping audit', 'scan my workspace for AI gaps', 'find where AI should be in my business', or wants a full workspace AI audit. Runs a comprehensive AI Mapping Audit based on Kim, Kim & Koning (2026) research."
version: 1.0.0
---

# AI Mapping Audit — Full Workspace Scan

Run a comprehensive AI Mapping Audit based on the research paper "Mapping AI into Production: A Field Experiment on Firm Performance" (Kim, Kim & Koning, 2026).

## Background for the user

Tell the user:
> This audit is based on a field experiment with 515 startups that found the #1 bottleneck to getting value from AI isn't capability — it's **discovering where to deploy it**. Firms that were shown how others reorganized around AI found 44% more use cases, completed 12% more tasks, were 18% more likely to acquire paying customers, and generated 1.9x higher revenue — all while needing 39.5% less external capital.
>
> I'm going to scan your workspace, map where you're already using AI, and identify the high-value gaps where AI could be creating value but isn't.

## Step 1: Discovery Questions

Before scanning any files, ask the user these questions to understand their business. These mirror the intervention from the research paper — the act of thinking through these questions is itself valuable.

Ask these one at a time (not all at once):

1. **"Walk me through what your business does, step by step — from when a customer first finds you to when they pay you and get what they bought."**
   (This maps their production chain end-to-end)

2. **"Where in that process do you spend time moving information between tools — copying from a spreadsheet into an email, updating a CRM after a call, transferring data between apps?"**
   (This finds "glue work" — the FazeShift pattern from the paper)

3. **"What parts of your business do you currently outsource, or wish you could do faster or cheaper?"**
   (This finds automation opportunities — the Ranger pattern)

4. **"If you could instantly test three different versions of something in your business, what would it be?"**
   (This finds parallel prototyping opportunities — the RyzLabs pattern)

5. **"What decisions do you currently make based on gut feeling that you wish you had data for?"**
   (This finds strategy and analytics gaps — the highest-value functions per the research)

Record the answers — they will inform the gap analysis in later steps.

## Step 2: Venture Discovery

Use the Agent tool with subagent_type "Explore" to thoroughly scan the user's working directory and identify:
- All projects, businesses, and ventures
- Their current status (active, planned, dormant)
- Any existing AI/automation configurations
- Revenue-generating vs. developmental projects

Be thorough — check subdirectories, read READMEs, check for config files, package.json files, .env files, GitHub Actions, automation scripts, etc.

## Step 3: AI Usage Mapping

For each discovered venture, map current AI usage across these 10 production functions:

| # | Function | Description | What to Look For |
|---|----------|-------------|-----------------|
| 1 | Product Development | Building/improving the core product | AI-generated features, synthetic testing, automated QA |
| 2 | Strategy & Planning | Business decisions, roadmaps, competitive analysis | AI-assisted research, market analysis, decision frameworks |
| 3 | Marketing & Growth | Customer acquisition, brand, social media | AI content generation, ad optimization, social automation |
| 4 | Sales & Revenue | Converting prospects, closing deals, pricing | AI outreach, lead scoring, pricing optimization |
| 5 | Customer Success | Retention, support, satisfaction | AI segmentation, churn prediction, personalized journeys |
| 6 | Finance & Pricing | Revenue tracking, cost optimization, forecasting | AI analytics, attribution modeling, cash flow prediction |
| 7 | Operations & Logistics | Day-to-day execution, workflows, processes | AI workflow automation, scheduling, resource allocation |
| 8 | Content Production | Creating content assets (writing, video, design) | AI writing, editing, image generation, video production |
| 9 | Data & Analytics | Measuring, analyzing, reporting | AI dashboards, anomaly detection, trend analysis |
| 10 | System Administration | Maintaining tools, infrastructure, integrations | AI monitoring, self-healing systems, optimization |

For each function, assign one of these statuses:
- **Saturated** — AI is deeply integrated, diminishing returns from more
- **Active** — AI is used but could be expanded
- **Minimal** — Some AI usage but mostly manual
- **Absent** — No AI involvement at all

## Step 4: Gap Analysis

Read these two reference files:
- `${CLAUDE_PLUGIN_ROOT}/skills/ai-mapping-audit/references/examples-from-other-firms.md` — examples of how firms deploy AI in each function
- `${CLAUDE_PLUGIN_ROOT}/skills/ai-mapping-audit/references/case-studies-from-paper.md` — the 4 real case studies from the Harvard/INSEAD research (Gamma, RyzLabs, FazeShift, Ranger)

For each function marked "Minimal" or "Absent", generate specific recommendations:
- What Claude/AI could do in this function
- How other firms have deployed AI here (from the examples and case studies)
- Which case study pattern applies (process redesign like Gamma? Parallel prototyping like RyzLabs? Eliminating glue work like FazeShift? Services-first like Ranger?)
- Expected impact (revenue, time saved, capital reduction)
- Implementation complexity (Low/Medium/High)

### O-Ring Warning

Check for the "partial automation trap": if AI is used in only one step of a multi-step process while the rest stays manual, flag it prominently:

> **Warning: Partial automation detected.** AI is being used in [function] but the steps before and after it are still manual. Research shows that automating just one step in a chain preserves the bottleneck rather than relieving it. The biggest gains come from rethinking the entire process around AI — not just speeding up one piece.

Cross-reference with the user's answers from Step 1, especially their description of their step-by-step process and where they identified glue work.

## Step 5: Priority Scoring

Score each opportunity on three dimensions (1-5 scale):
- **Revenue Impact**: How much could this increase revenue or reduce costs?
- **Capital Reduction**: Does this reduce need for external investment or hiring?
- **Ease of Implementation**: How quickly can this be deployed with existing tools?

Calculate a composite score: (Revenue Impact x 2) + Capital Reduction + Ease of Implementation

Sort opportunities by composite score, highest first.

## Step 6: Generate the AI Map (Markdown + HTML)

Create TWO files in the user's working directory:

### File 1: `AI-MAP-[date].md` (text-readable report)

Markdown file with:

1. **Executive Summary** — Total ventures scanned, current AI saturation %, number of gaps found, number of "press-send" wins
2. **Venture Inventory** — List of all discovered ventures with status
3. **The AI Map** — A table showing each venture × each function with status indicators (Saturated/Active/Minimal/Absent)
4. **Top 10 Opportunities** — Prioritized list with scores and specific implementation steps
5. **Press-Send Wins** — The subset of opportunities where infrastructure already exists (Ease = 5, Score ≥ 15)
6. **The Paper's Key Insight** — Remind the user that gains are largest at the 90th percentile (AI amplifies winners, doesn't rescue losers)
7. **30-Day Action Plan** — Week-by-week implementation sequence starting with highest-impact items

### File 2: `AI-MAP-[date].html` (visual heat map)

Generate a self-contained HTML file with a visual heat map. **Use the template at:**

```
${CLAUDE_PLUGIN_ROOT}/skills/ai-mapping-audit/templates/heat-map-template.html
```

Read the template, then substitute these placeholders with real data:

| Placeholder | Replace With |
|---|---|
| `{{BUSINESS_NAME}}` | Best-guess name from the workspace (parent folder name, README title, or "Your Business" if unknown) |
| `{{DATE}}` | Today's date in format like "April 6, 2026" |
| `{{VENTURE_COUNT}}` | Number of ventures discovered in Step 2 |
| `{{SATURATION_PERCENT}}` | (Saturated cells + Active cells) / total cells × 100, rounded to whole number |
| `{{GAP_COUNT}}` | Number of cells marked Absent or Minimal |
| `{{PRESS_SEND_COUNT}}` | Number of opportunities scoring ≥ 15 with Ease = 5 |
| `{{HEAT_MAP_ROWS}}` | Generated `<tr>` blocks (see format below) |
| `{{PRIORITY_LIST}}` | Top 10 opportunities as `<div class="priority-item">` blocks |
| `{{PRESS_SEND_LIST}}` | Press-send opportunities as `<div class="press-send-item">` blocks |
| `{{ACTION_PLAN}}` | 4-week action plan as alternating `<h3>Week N</h3><p>...</p>` blocks |

**Heat map row format** — one row per venture, 10 cells per row:

```html
<tr>
  <td class="venture-name">Venture Name</td>
  <td class="cell cell-saturated">SAT</td>
  <td class="cell cell-active">ACT</td>
  <td class="cell cell-minimal">MIN</td>
  <td class="cell cell-absent">ABS<span class="opportunity-star">★</span></td>
  ... continue for all 10 functions in this exact order:
  Product Dev, Strategy, Marketing, Sales, Customer Success, Finance, Operations, Content, Data, System Admin
</tr>
```

**Cell class mapping:**
- Saturated → `cell cell-saturated` with text "SAT"
- Active → `cell cell-active` with text "ACT"
- Minimal → `cell cell-minimal` with text "MIN"
- Absent → `cell cell-absent` with text "ABS"

**Star marker:** Add `<span class="opportunity-star">★</span>` inside any cell that corresponds to a top-10 opportunity (i.e., the cell is in the priority-scored list with composite score ≥ 12). The star indicates "this is where the 44% Rule says to act first."

**Priority list item format:**

```html
<div class="priority-item">
  <span class="priority-rank">1</span>
  <span class="priority-title">Venture Name × Function Name: Brief action description</span>
  <span class="priority-score">17/20</span>
  <p class="priority-detail">Why this matters in plain language. Which case study pattern applies (Gamma's process redesign / RyzLabs's parallel prototyping / FazeShift's glue work elimination / Ranger's services-first). The first concrete step the user should take this week.</p>
</div>
```

**Press-send item format:**

```html
<div class="press-send-item">
  <strong>Venture Name × Function Name:</strong> What to activate
  <br><small>Why it's "press send": brief explanation of why the infrastructure already exists</small>
</div>
```

**Action plan format:**

```html
<h3>Week 1</h3>
<p>Specific action item from the highest-priority opportunity</p>
<h3>Week 2</h3>
<p>Next action — should build on Week 1 or attack a parallel opportunity</p>
<h3>Week 3</h3>
<p>...</p>
<h3>Week 4</h3>
<p>Reassessment + next-quarter planning</p>
```

### Why both formats

- **Markdown** is easy for the user to read in their editor, version-control friendly, can be re-processed by other tools
- **HTML** opens directly in any browser with a styled visual heat map — much easier to share with co-founders, investors, or team members who don't read markdown
- The HTML file is **self-contained** (all CSS inline, no external assets) so it works offline and can be emailed as an attachment

After generating both files, tell the user:
> I've generated two files in your working directory:
> 1. **AI-MAP-[date].md** — text report with the full analysis (open in your editor)
> 2. **AI-MAP-[date].html** — visual heat map (open in any browser by double-clicking it)
>
> The heat map color-codes every venture × function intersection — green where AI is active, red where it's absent. Stars (★) mark the highest-impact gaps to fill first.
>
> Your top opportunity is: [briefly describe #1 from the priority list]
>
> Want me to run `/the-44-percent-rule:map-score` to drill into the prioritization, or `/the-44-percent-rule:map-venture [name]` to do a deep audit of a specific project?

## Important Notes

- Focus recommendations on areas where AI is ABSENT, not where it's already active
- Be specific — don't say "use AI for analytics", say "connect Beehiiv MCP get_post_stats to a weekly Claude agent that identifies which content topics drive the most ad revenue"
- Reference the paper's findings throughout to ground recommendations in evidence
- The biggest wins come from product development and strategy — weight those functions higher
- Always check: if a venture only uses AI for writing/content, it has a mapping problem
