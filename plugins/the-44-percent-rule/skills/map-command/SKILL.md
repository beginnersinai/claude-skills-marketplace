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

## Step 6: Generate the AI Map

Create a file called `AI-MAP-[date].md` in the user's working directory with:

1. **Executive Summary** — Total ventures scanned, current AI saturation %, number of gaps found
2. **Venture Inventory** — List of all discovered ventures with status
3. **The AI Map** — A table showing each venture x each function with status indicators
4. **Top 10 Opportunities** — Prioritized list with scores and specific implementation steps
5. **The Paper's Key Insight** — Remind the user that gains are largest at the 90th percentile (AI amplifies winners, doesn't rescue losers)
6. **30-Day Action Plan** — Week-by-week implementation sequence starting with highest-impact items

## Important Notes

- Focus recommendations on areas where AI is ABSENT, not where it's already active
- Be specific — don't say "use AI for analytics", say "connect Beehiiv MCP get_post_stats to a weekly Claude agent that identifies which content topics drive the most ad revenue"
- Reference the paper's findings throughout to ground recommendations in evidence
- The biggest wins come from product development and strategy — weight those functions higher
- Always check: if a venture only uses AI for writing/content, it has a mapping problem
