---
name: map-venture
description: "This skill should be used when the user types '/map-venture', asks to 'audit a single project', 'map AI usage for this venture', or wants a focused AI mapping audit on one specific project or business. Provide the venture name or directory path as context."
version: 1.0.0
---

# AI Mapping Audit — Single Venture

Run a focused AI Mapping Audit on a specific venture. The user will provide the venture name or path.

## What to tell the user

> Running a focused AI Mapping Audit on **[venture name]**. I'll map where AI is and isn't being used across 10 core business functions, then show you what you're missing based on how other high-performing firms have deployed AI.

## Step 1: Deep Venture Analysis

Thoroughly explore the specified venture directory:
- Read all key files (READMEs, configs, strategy docs, plans)
- Identify all automation, scripts, AI configurations
- Understand the business model, revenue streams, and current workflows
- Map the full production pipeline from input to output

## Step 2: Map the 10 Functions

For this specific venture, evaluate each of the 10 production functions:

1. **Product Development** — Is AI involved in building/improving the core offering?
2. **Strategy & Planning** — Are business decisions AI-informed?
3. **Marketing & Growth** — Is customer acquisition AI-assisted?
4. **Sales & Revenue** — Is revenue generation AI-optimized?
5. **Customer Success** — Is retention/satisfaction AI-driven?
6. **Finance & Pricing** — Is financial analysis AI-powered?
7. **Operations & Logistics** — Are workflows AI-automated?
8. **Content Production** — Is content creation AI-assisted?
9. **Data & Analytics** — Is measurement AI-enhanced?
10. **System Administration** — Is the system self-optimizing?

Rate each: Saturated / Active / Minimal / Absent

## Step 3: Generate Recommendations

Read `${CLAUDE_PLUGIN_ROOT}/skills/ai-mapping-audit/references/examples-from-other-firms.md` for inspiration.

For each gap (Minimal or Absent), provide:
- **The Opportunity**: What AI could do here, specifically
- **How Others Do It**: Real example from the reference file
- **Expected Impact**: Revenue increase, time saved, or capital reduced
- **Implementation Steps**: Concrete 3-5 step plan to activate
- **Tools Needed**: Which Claude features, MCP tools, or APIs to use
- **Priority Score**: (Revenue Impact x 2) + Capital Reduction + Ease (each 1-5)

## Step 4: Output

Create a focused report with:
1. Venture overview and current state
2. The 10-function map with status indicators
3. Top 5 opportunities ranked by priority score
4. Implementation timeline (7/14/30 day milestones)
5. Anti-pattern check: Is this venture only using AI for content? If yes, flag it prominently.

## Important

- Be brutally specific. Not "use AI for marketing" but "create a Claude agent that analyzes your Beehiiv click data weekly and recommends which topics to double down on."
- Connect recommendations to existing tools and infrastructure the venture already has
- Prioritize product development and strategy functions — the research shows these have the highest return
