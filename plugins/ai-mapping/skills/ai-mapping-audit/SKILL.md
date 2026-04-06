---
name: ai-mapping-audit
description: "Automatically activates when users discuss AI adoption strategy, ask where to use AI in their business, want to find new AI use cases, or mention the 'mapping problem'. Provides the 10-function framework and examples of how other firms have reorganized around AI to help users discover unmapped opportunities."
version: 1.0.0
---

# AI Mapping Audit Skill

This skill provides the framework and knowledge for performing AI Mapping Audits — systematic evaluations of where AI creates value across a business's production functions.

## When This Skill Activates

Use this knowledge when the user:
- Asks "where should I use AI in my business?"
- Wants to find new AI use cases beyond content/writing
- Mentions the "mapping problem" or AI adoption bottlenecks
- Asks how other companies are using AI
- Wants to audit their AI usage
- Is planning AI strategy for a venture

## The Research Foundation

**Paper**: "Mapping AI into Production: A Field Experiment on Firm Performance"
**Authors**: Hyunjin Kim (INSEAD), Dahyeon Kim (INSEAD), Rembrand Koning (Harvard Business School)
**Date**: March 30, 2026
**Program**: INSEAD AI Founder Sprint / AI Venture Lab

### Key Findings

**The Mapping Problem**: The central friction in AI adoption is not AI capability — it's discovering WHERE and HOW AI creates value within a firm's production process.

**The Experiment**: 515 high-growth startups. Treatment group received information about how OTHER firms had reorganized production around AI, prompting them to search for use cases across a BROADER set of firm functions.

**Results**:
- **44% more AI use cases** discovered (concentrated in product development and strategy)
- **12% more tasks** completed
- **18% more likely** to acquire paying customers
- **1.9x higher revenue**
- **39.5% less demand** for external capital investment
- **No increase in labor demand** — firms did more with less
- **Gains largest at 90th percentile** — AI expands the ceiling, not the floor

### What This Means Practically

1. Most firms only use AI for content creation and chatbots — they have a mapping problem
2. The highest-value AI applications are in product development and strategy
3. Simply SHOWING firms how others use AI causes them to discover more use cases
4. AI reduces capital requirements — you can do more without hiring or raising money
5. The biggest gains go to already-strong ventures — AI amplifies winners

## The 10-Function Framework

Read `${CLAUDE_PLUGIN_ROOT}/skills/ai-mapping-audit/references/ten-functions.md` for the complete framework.

## Examples From Other Firms

Read `${CLAUDE_PLUGIN_ROOT}/skills/ai-mapping-audit/references/examples-from-other-firms.md` for the "treatment" — examples of how real firms have reorganized around AI across all 10 functions.

## How to Apply

### Quick Assessment (2 minutes)
Ask the user: "Which of these 10 functions does your business use AI for?" Then identify the gaps.

### Full Audit (30-60 minutes)
Run the `/map` command to scan their workspace automatically.

### Single Venture (10-20 minutes)
Run `/map-venture [name]` for a focused analysis.

### Scoring (5-10 minutes)
Run `/map-score` after a map to prioritize opportunities.

## The Anti-Pattern

If a user's AI usage is concentrated only in:
- Content writing
- Social media posts
- Email drafting
- Image generation

...they have the mapping problem. The highest-value applications are in:
- Product development (synthetic testing, feature prioritization, automated QA)
- Strategy (competitive monitoring, market analysis, scenario modeling)
- Finance (revenue attribution, pricing optimization, cash flow forecasting)
- Customer development (segmentation, churn prediction, personalization)
- System optimization (analyzing AI system performance, self-improvement loops)

Always guide users toward these higher-value functions.
