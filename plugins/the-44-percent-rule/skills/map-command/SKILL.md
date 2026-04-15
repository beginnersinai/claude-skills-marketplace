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

### File 2: `AI-MAP-[date].html` (full visual report)

Generate a self-contained, dark-theme HTML report. **Use the template at:**

```
${CLAUDE_PLUGIN_ROOT}/skills/ai-mapping-audit/templates/heat-map-template.html
```

The template includes a donut chart (SVG), color-coded stat cards, per-venture progress bars, a CSS-grid heat map, a radar/spider chart, a horizontal bar chart for the top 10, a vertical timeline for the 30-day plan, icon callouts, and a research footer. **All visuals are pure HTML+CSS+SVG — no external assets, no JavaScript.**

#### Step 6a — Calculate the donut chart

After classifying every (venture × function) cell, count each status across all cells.

```
total       = ventureCount × 10
sat_count   = cells marked Saturated
act_count   = cells marked Active
min_count   = cells marked Minimal
abs_count   = cells marked Absent

SAT_PCT = round(sat_count / total × 100)
ACT_PCT = round(act_count / total × 100)
MIN_PCT = round(min_count / total × 100)
ABS_PCT = round(abs_count / total × 100)

SATURATION_PERCENT = round((sat_count + act_count) / total × 100)
```

The donut uses a circle with `r=70`, so circumference = `2π × 70 ≈ 440`. Each segment's length is its share of 440. Stack the segments by adding the previous lengths to the next segment's `dashoffset`:

```
DONUT_SAT_LEN    = (sat_count / total) × 440
DONUT_ACT_LEN    = (act_count / total) × 440
DONUT_MIN_LEN    = (min_count / total) × 440
DONUT_ABS_LEN    = (abs_count / total) × 440

DONUT_SAT_OFFSET = 0
DONUT_ACT_OFFSET = -DONUT_SAT_LEN
DONUT_MIN_OFFSET = -(DONUT_SAT_LEN + DONUT_ACT_LEN)
DONUT_ABS_OFFSET = -(DONUT_SAT_LEN + DONUT_ACT_LEN + DONUT_MIN_LEN)
```

Round all dasharray/offset values to 2 decimal places when substituting.

#### Step 6b — Build per-venture progress bars

For each venture, compute its own saturation:

```
venture_score = (sat_in_venture × 1.0) + (act_in_venture × 0.6) + (min_in_venture × 0.25)
venture_pct   = round(venture_score / 10 × 100)
functions_active = sat_in_venture + act_in_venture
```

Pick the bar color class based on `venture_pct`:
- `0–15%` → `r` (red)
- `16–30%` → `y` (yellow)
- `31–60%` → `b` (blue)
- `61%+` → `g` (green)

Emit one card per venture into `{{VENTURE_BARS}}`:

```html
<div class="venture-card">
  <div class="vc-name">VentureName</div>
  <div class="vc-meta">FUNCTIONS_ACTIVE / 10 functions covered</div>
  <div class="vc-bar-wrap"><div class="vc-bar b" style="width:42%"></div></div>
  <div class="vc-pct"><span>AI Saturation</span><strong>42%</strong></div>
</div>
```

#### Step 6c — Build the heat map grid

The heat map is functions × ventures (10 rows, N columns where N = venture count). Replace `{{HM_COLS}}` in the CSS grid with the venture count.

Replace `{{HEATMAP_VENTURE_HEADERS}}` with one `<div class="hm-vh">VentureName</div>` per venture, in the same column order you'll use for the cells.

Replace `{{HEATMAP_ROWS}}` with 10 rows in this exact function order: **Product Dev, Strategy, Marketing, Sales, Customer Success, Finance, Operations, Content, Data, System Admin**.

```html
<div class="hm-row">
  <div class="hm-fn-label">Product Dev</div>
  <div class="hm-cell hm-saturated">SATURATED</div>
  <div class="hm-cell hm-active">ACTIVE</div>
  <div class="hm-cell hm-absent">ABSENT<span class="star">★</span></div>
  <!-- one cell per venture, in the same order as the headers -->
</div>
```

Cell class + label mapping:
- Saturated → `hm-saturated` / "SATURATED"
- Active → `hm-active` / "ACTIVE"
- Minimal → `hm-minimal` / "MINIMAL"
- Absent → `hm-absent` / "ABSENT"

Add `<span class="star">★</span>` inside any cell whose (venture × function) intersection appears in the top-10 priority list with composite score ≥ 12.

#### Step 6d — Calculate the radar/spider chart polygon points

The radar has 10 axes (one per function), with the first axis pointing straight up. Score every function on a 0–1 scale based on the BEST status that function reaches across all ventures (or the average — pick one and be consistent):

```
Absent    → 0.0
Minimal   → 0.25
Active    → 0.6
Saturated → 0.9
```

For each function `i` (0–9), compute the radar point:

```
angle_deg = (i × 36) − 90        # -90 so first spoke points up
angle_rad = angle_deg × π / 180
x = 250 + (score × 180) × cos(angle_rad)
y = 250 + (score × 180) × sin(angle_rad)
```

Function index order (must match the spoke positions in the SVG):
0=Product Dev, 1=Strategy, 2=Marketing, 3=Sales, 4=Customer Success, 5=Finance, 6=Operations, 7=Content, 8=Data, 9=System Admin.

Concatenate all 10 points into a `points` string:

```
"x0,y0 x1,y1 x2,y2 ... x9,y9"
```

Substitute into `{{RADAR_CUR_POINTS}}`.

For `{{RADAR_TOP_POINTS}}` (the 90th-percentile reference polygon), use `score = 0.85` for every function — this represents the "top performers" from the research. The polygon will be a near-perfect circle, making the gap between blue (current) and green (top performers) immediately visible.

#### Step 6e — Build the horizontal bar chart for top 10 opportunities

For each opportunity in the top 10, compute the bar width:

```
bar_width_pct = (composite_score / 20) × 100
```

Apply the `top` class (red gradient) to the **top 2** highest-scoring opportunities — these are the visual "press send" callouts.

Emit into `{{OPPORTUNITY_BARS}}`:

```html
<div class="bar-row">
  <div class="bar-label"><span class="rk">1</span>VentureName × Function</div>
  <div class="bar-track"><div class="bar-fill top" style="width:90%"></div></div>
  <div class="bar-score">18/20</div>
</div>
```

(Use `bar-fill` without `top` for ranks 3–10.)

#### Step 6f — Build the priority detail list

`{{PRIORITY_LIST}}` is the same top 10 opportunities with full explanation:

```html
<div class="priority-detail-item">
  <div class="pdi-head">
    <span class="rank">1</span>
    <span class="pdi-title">VentureName × Function: short action description</span>
    <span class="pdi-score">18/20</span>
  </div>
  <p class="pdi-body">Why this matters in plain language. Which case study pattern applies (Gamma's process redesign / RyzLabs's parallel prototyping / FazeShift's glue-work elimination / Ranger's services-first). The first concrete step to take this week.</p>
</div>
```

#### Step 6g — Build the press-send list

Filter the priority list to opportunities with `composite_score ≥ 15` AND `Ease = 5`. Emit into `{{PRESS_SEND_LIST}}`:

```html
<div class="ps-item">
  <strong>VentureName × Function:</strong> What to activate
  <small>Why it's "press send": infrastructure already exists because [specific reason]</small>
</div>
```

#### Step 6h — Group the timeline into 4 weekly themes

Group the top opportunities into 4 weekly buckets by theme:
- **Week 1 — Activate** (`w1`, red): Press-send wins. Anything with Ease=5 and infrastructure already in place.
- **Week 2 — Customer** (`w2`, orange): Customer-facing opportunities (Sales, Marketing, Customer Success).
- **Week 3 — Finance** (`w3`, yellow): Finance & Pricing, Data & Analytics, Operations.
- **Week 4 — Strategy** (`w4`, green): Product Dev and Strategy & Planning — the highest-value functions per the research.

If a theme has no relevant top-10 opportunities, fill it with the next-highest-scoring opportunity that fits.

Emit into `{{TIMELINE_WEEKS}}`:

```html
<div class="timeline-week w1">
  <span class="tw-tag">Week 1 · Activate</span>
  <h3 class="tw-title">Highest-impact press-send wins</h3>
  <ul class="tw-tasks">
    <li>Specific action 1 from this theme</li>
    <li>Specific action 2 from this theme</li>
  </ul>
</div>
```

Repeat for `w2`, `w3`, `w4`.

#### Step 6i — Substitute the remaining placeholders

| Placeholder | Replace With |
|---|---|
| `{{BUSINESS_NAME}}` | Best-guess from workspace (parent folder, README title, or "Your Business") |
| `{{DATE}}` | Today's date in format like "April 6, 2026" |
| `{{VENTURE_COUNT}}` | Number of ventures discovered in Step 2 |
| `{{GAP_COUNT}}` | Cells marked Absent or Minimal |
| `{{PRESS_SEND_COUNT}}` | Opportunities scoring ≥ 15 with Ease = 5 |
| `{{TOP_SCORE}}` | The composite score of the #1 opportunity |
| `{{TOP_OPPORTUNITY_LABEL}}` | Short label like "VentureName × Strategy" |
| `{{SATURATION_PERCENT}}` | Big number in donut center |
| `{{SAT_PCT}}` `{{ACT_PCT}}` `{{MIN_PCT}}` `{{ABS_PCT}}` | Donut legend percentages |
| `{{DONUT_SAT_LEN}}` `{{DONUT_ACT_LEN}}` `{{DONUT_MIN_LEN}}` `{{DONUT_ABS_LEN}}` | Donut dasharray lengths (Step 6a) |
| `{{DONUT_SAT_OFFSET}}` `{{DONUT_ACT_OFFSET}}` `{{DONUT_MIN_OFFSET}}` `{{DONUT_ABS_OFFSET}}` | Donut dashoffset values (Step 6a) |
| `{{HM_COLS}}` | Venture count (for the CSS grid template) |
| `{{HEATMAP_VENTURE_HEADERS}}` | One `<div class="hm-vh">...</div>` per venture (Step 6c) |
| `{{HEATMAP_ROWS}}` | 10 function rows (Step 6c) |
| `{{VENTURE_BARS}}` | One progress card per venture (Step 6b) |
| `{{RADAR_CUR_POINTS}}` | 10 x,y pairs for current state polygon (Step 6d) |
| `{{RADAR_TOP_POINTS}}` | 10 x,y pairs for top performers polygon (Step 6d) |
| `{{OPPORTUNITY_BARS}}` | Top 10 bar rows (Step 6e) |
| `{{PRIORITY_LIST}}` | Top 10 detailed items (Step 6f) |
| `{{PRESS_SEND_LIST}}` | Press-send opportunity items (Step 6g) |
| `{{TIMELINE_WEEKS}}` | 4 weekly theme blocks (Step 6h) |

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
