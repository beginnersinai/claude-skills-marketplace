# How Other Firms Reorganized Around AI

This document is the "treatment" from Kim, Kim & Koning (2026). The paper showed that simply exposing firms to examples of how OTHER firms reorganized around AI caused them to discover 44% more use cases. These examples serve the same purpose — they show what's possible beyond content generation.

---

## Product Development

### Synthetic User Testing
A SaaS startup uses Claude to simulate 10 different customer personas interacting with new features before launch. Each persona has a distinct background, technical skill level, and set of goals. The AI walks through the feature as each persona, flagging confusion points, missing functionality, and edge cases. This replaced 2 weeks of beta testing with 2 hours of synthetic testing, catching 73% of the issues that beta users later confirmed.

### Automated Feature Prioritization
An e-commerce platform feeds Claude their product backlog, customer support tickets, competitor feature lists, and usage analytics. The AI scores each potential feature on: customer demand signal, competitive necessity, implementation effort, and revenue impact. The team still makes the final call, but the AI's scoring replaced 4 hours of weekly prioritization meetings.

### Competitive Product Monitoring
A newsletter business uses Firecrawl MCP + Claude to automatically scrape competitor newsletters weekly, analyze formatting changes, new sections, pricing updates, and content strategy shifts. A summary lands in Slack every Monday morning before the editorial meeting.

---

## Strategy & Planning

### Continuous Competitive Radar
A startup founder runs a weekly Claude agent that searches for competitor news, funding announcements, product launches, and hiring patterns. The agent produces a 1-page competitive brief highlighting anything that should change the company's strategy. This runs automatically via a scheduled task.

### Scenario Modeling for Pricing
Before changing subscription pricing, a solo entrepreneur has Claude model 5 scenarios: current price maintained, 20% increase, 50% increase, freemium introduction, and annual-only. For each scenario, Claude estimates subscriber retention, revenue impact, and competitive positioning based on market data. The founder used this to justify a 30% price increase that resulted in only 5% churn.

### Strategic Decision Journal
After every major business decision, Claude automatically generates a "decision record" documenting: what was decided, what alternatives were considered, what data informed the choice, and what would signal the decision was wrong. Six months later, the founder reviews these to improve decision quality.

---

## Sales & Revenue

### AI-Powered Speaking Pipeline
A consultant built a 6-agent pipeline in Claude Code: venue researcher (finds and qualifies speaking opportunities), outreach drafter (personalizes emails), response handler (classifies and drafts replies), meeting prepper (builds briefing sheets before calls), call processor (creates CRM updates after calls), and pipeline reporter (weekly performance dashboards). The system handles 80% of the speaking business workflow, with the human only needed for actual presentations and final email approval.

### Lead Scoring for Newsletters
A newsletter operator uses Beehiiv MCP tools to pull subscriber engagement data, then has Claude score each subscriber on: open rate trend, click frequency, referral activity, and time-on-site. High-scorers get personalized upsell offers. Low-scorers get re-engagement sequences. This increased paid conversions by 22%.

### Dynamic Pricing Intelligence
An AI tools directory operator has Claude monitor competitor pricing weekly using Firecrawl, then recommend price adjustments. The AI considers: competitor price changes, feature parity, market positioning, and customer acquisition cost. Quarterly price adjustments based on AI recommendations increased revenue 15% without losing customers.

---

## Customer Success & Retention

### Subscriber Churn Prediction
A daily newsletter uses Claude to analyze subscriber behavior patterns weekly: declining open rates, reduced click frequency, unsubscribe page visits. Subscribers flagged as "at-risk" receive a personalized re-engagement email with content tailored to their historical click patterns. This reduced monthly churn by 31%.

### Engagement-Based Segmentation
Instead of treating all 5,000 subscribers the same, a newsletter creator has Claude segment subscribers into 5 tiers based on engagement data from Beehiiv MCP. Each tier gets slightly different content emphasis, different referral offers, and different upgrade prompts. The top tier gets early access to new content.

### Automated Satisfaction Surveys
After every 10th newsletter, a subset of subscribers receives a 2-question survey. Claude analyzes responses, clusters feedback themes, and generates a monthly "voice of subscriber" report with specific content recommendations.

---

## Finance & Pricing

### Revenue Attribution
A multi-channel creator (newsletter + YouTube + speaking + courses) uses Claude to trace revenue back to its source. For each dollar earned, the AI determines: which content drove the subscriber, which channel converted them, and what the lifetime value trajectory looks like. This revealed that YouTube viewers who subscribed had 3x the LTV of social media subscribers, shifting content investment.

### AI Cost Tracking
A creator using multiple AI tools (Claude API, Midjourney, Eleven Labs) has Claude analyze monthly costs vs. output. The AI calculates cost-per-article, cost-per-video, cost-per-image, and identifies which AI tools deliver the best ROI. This led to consolidating from 5 AI tools to 2, saving $200/month.

### Cash Flow Forecasting
A solo entrepreneur feeds Claude their income history, upcoming obligations, seasonal patterns, and pipeline data. The AI generates a rolling 90-day cash flow forecast with confidence intervals. When projected cash dips below a threshold, the AI suggests specific actions (accelerate invoicing, pause discretionary spending, launch a promotion).

---

## Operations & Logistics

### Workflow Bottleneck Detection
A content team has Claude analyze their production pipeline weekly: time from idea to published piece, where drafts sit longest, which review stages cause delays. The AI identified that the "final edit" stage was the bottleneck — not because editing was slow, but because the editor didn't receive notifications when drafts were ready. A simple Slack notification eliminated 2-day average delays.

### Automated SOP Generation
Every time a team member figures out a new workflow (Beehiiv template setup, affiliate link configuration, social media scheduling), they tell Claude what they did. Claude generates a step-by-step SOP, adds it to the team's operations wiki, and tags it for discoverability. The team now has 40+ SOPs that new team members can reference.

### Meeting Elimination
A founder replaced 3 weekly meetings with Claude-generated async briefs. The AI pulls data from project management tools, analyzes progress, identifies blockers, and generates a brief that each team member reviews on their own time. Meetings only happen when the AI flags something that requires discussion.

---

## Data & Analytics

### Natural Language Data Querying
Instead of logging into analytics dashboards, a newsletter operator asks Claude questions: "Which articles got the most clicks last week?", "What's my subscriber growth rate this month vs. last?", "Which day of the week gets the best open rates?" Claude queries Beehiiv MCP tools and returns plain-English answers with data tables.

### Anomaly Alerts
A SaaS founder has Claude check key metrics daily: signups, revenue, error rates, page load times. When anything deviates more than 2 standard deviations from the 30-day average, Claude sends a Slack alert with possible explanations and suggested next steps.

### Content Performance Correlation
A creator uses Claude to correlate content characteristics (topic, length, format, headline style, publish time) with engagement metrics. The AI identified that articles with numbered lists in the headline got 40% more clicks — but only on Tuesdays and Wednesdays.

---

## System Administration

### AI System Self-Analysis
A creator running 15 GitHub Actions workflows has Claude analyze workflow logs weekly: success/failure rates, execution times, cost, and output quality. The AI generates a "system health" report and flags any workflow whose failure rate exceeds 5%. This caught a broken API integration 3 days before it would have caused a visible outage.

### Cost-Per-Output Tracking
A team using Claude Code extensively has the AI track its own usage: how many tokens consumed per task type, which agents are most/least efficient, and whether output quality correlates with token usage. This revealed that one agent was consuming 5x the tokens of others while producing lower-quality output — a simple prompt revision fixed it.

### Automated Backup Verification
A solo operator has Claude periodically verify that all critical data (subscriber lists, content archives, financial records) are properly backed up. The AI checks backup timestamps, file sizes, and runs spot-checks on data integrity. This caught a backup that had silently failed 3 weeks prior.

---

## The Pattern

Across all these examples, the pattern is the same:

1. **The capability existed** — the AI tools were available
2. **The mapping was missing** — nobody had thought to apply AI to that function
3. **The trigger was exposure** — seeing how someone else did it sparked the idea
4. **The gain was outsized** — the non-obvious applications delivered bigger returns than the obvious ones

This is exactly what Kim, Kim & Koning (2026) found: the intervention that caused 44% more use cases was simply **showing firms what other firms were doing with AI**.
