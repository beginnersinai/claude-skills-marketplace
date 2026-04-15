# Report Template

Use this structure for every report. Exact headings, exact order.

```markdown
# Brand Pulse: {Brand Name}

*Generated {YYYY-MM-DD} · {Public|Enhanced} mode · Depth: {Quick|Standard|Deep}*
*Entity: {Person|Company|Product|App|Creator} · Tracked since: {first-run-date}*

---

## Since Last Pulse
*Compared to {previous-report-date} ({N} days ago)*

- **Sentiment**: {pos_prev}% positive → {pos_curr}% positive ({delta} pts)
- **Mention volume**: {n_prev} → {n_curr} ({pct_change}%)
- **New complaint themes**: {count} — {short list, e.g. "shipping delays, subscription UX"}
- **Complaint themes that disappeared**: {count} — {list} *(may indicate resolution; verify)*
- **New feature requests**: {count} — {list}
- **Biggest narrative shift**: {one-line description, e.g. "Sentiment dropped on r/Product after Oct 8 pricing change"}

*(Omit this section entirely if no prior report exists for this brand.)*

---

## Executive Summary

{3–5 sentences of plain prose. No bullets here. Capture: overall sentiment, main storyline, and the single most important thing to know. Tone: neutral, analytical, direct. No hype, no hedging beyond what the data supports.}

---

## Top 3 Complaints
*Ranked by volume × recency × source authority*

### 1. {Cluster name}
- **Volume**: {N} mentions across {M} sources
- **Recency skew**: {recent|older|mixed} — {most recent date}
- **Representative quotes**:
  > "{Real quoted text}" — [{source-name}]({url})
  > "{Real quoted text}" — [{source-name}]({url})

### 2. {Cluster name}
...

### 3. {Cluster name}
...

---

## Top 3 Feature Requests

### 1. {Cluster name}
- **Volume**: {N} mentions
- **Representative quotes**:
  > "{Quote}" — [{source}]({url})

### 2. ...

### 3. ...

---

## Key Recommendations

*Derived from the data above. Each should be concrete and actionable.*

- **{Action-oriented heading}** — {1–2 sentence explanation tied to a specific cluster or data point}
- **{Action-oriented heading}** — ...
- **{Action-oriented heading}** — ...

*(3–5 recommendations total. Skip this section if data is too thin to justify any; say so explicitly.)*

---

## Detailed Breakdown

### Reddit
- **Mentions scanned**: {N} (time window: {window})
- **Sentiment split**: {pos}% positive / {neu}% neutral / {neg}% negative
- **Top subreddits**: {list with mention counts}
- **Notable quotes**:
  > "{Quote}" — [r/{subreddit}]({permalink}) · {date}
  > "{Quote}" — [r/{subreddit}]({permalink}) · {date}

### Hacker News
*(Only include if source was queried and returned results.)*
- **Mentions**: {N}
- **Top story**: [{title}]({url}) · {points} points · {comments} comments
- **Themes**: {1-2 sentences}

### Trustpilot
- **Overall rating**: {X.X} / 5 from {N} reviews
- **Recent trend**: {improving|stable|declining} over last {period}
- **Most-mentioned positives**: {list}
- **Most-mentioned complaints**: {list}

### G2 / Capterra
*(One block each if both queried; omit if not applicable.)*
- **Average rating**: ...
- **Pros cluster**: ...
- **Cons cluster**: ...

### Product Hunt
- **Launch reception**: {score, date if findable}
- **Key feature requests from comments**: {list}

### BBB
*(Companies only; US-centric.)*
- **Rating**: {letter grade or score}
- **Complaint count** (last 3 years): {N}
- **Top complaint categories**: {list}

### Glassdoor
*(Companies only — employee sentiment, not customer.)*
- **Overall rating**: {X.X} / 5
- **Pros (employees)**: {list}
- **Cons (employees)**: {list}
- **Note**: *Employee sentiment, not customer-facing — included for completeness.*

### Google Search
- **Queries run**: {list}
- **High-signal results**: {bulleted links with 1-line summaries}

### App Stores
*(Apps only.)*
- **iOS**: {rating} / 5 · {N} reviews · {short summary}
- **Android**: {rating} / 5 · {N} reviews · {short summary}

### X / Twitter
*(Enhanced mode only.)*
- **Mentions**: {N}
- **Engagement**: {avg likes, avg replies on top mentions}
- **Sentiment split**: {pos/neu/neg}%
- **Top tweets**: {link, author, engagement}

### LinkedIn
*(Enhanced mode only.)*
- **Mentions**: {N}
- **Source breakdown**: {employees / customers / industry commentators}
- **Notable posts**: {links}

### Instagram
*(Enhanced mode only.)*
- **Tag volume**: {N recent posts on #{brand}}
- **Notable captions/comments**: {quotes}

### TikTok
*(Enhanced mode only.)*
- **Volume**: {N videos, aggregate views}
- **Notable content**: {links}

### Facebook
*(Enhanced mode only, companies only.)*
- **Page reviews**: {rating} / 5 · {N} reviews
- **Recent complaint themes**: {list}

---

## Coverage & Blind Spots

**Sources covered**: {comma-separated list}
**Sources skipped (reason)**:
- {Source} — {reason, e.g. "not applicable to entity type", "hit 403", "muted by user config"}

**Sources not covered by this run**:
{If Public mode: "X/Twitter, LinkedIn, Instagram, TikTok, Facebook — install the Playwright plugin and select Enhanced mode to include these."}
{If Enhanced mode but some socials unchecked: list which ones and why.}

**Known blind spots for this run**:
- {Only if applicable — e.g. "User reported IG logged in, but session appeared expired. Skipped."}

---

## Methodology

- **Date range**: {actual window used per source}
- **Sentiment classification**: AI-clustered into positive / neutral / negative. Directional indicator, not survey-grade.
- **Recency weighting**: 30-day half-life exponential decay on volume scores
- **Source authority weighting**: review sites (G2/Capterra/Trustpilot) 1.2x, community forums (Reddit/HN) 1.0x, SERP snippets 0.8x
- **Total raw mentions analyzed**: {N}
- **Total after deduplication**: {N}

*Enhanced-mode data was accessed via the user's own logged-in browser session at human-speed pacing. Treat as manual research automation, not a bulk scraper. No posts, likes, or messages were sent.*

*Report saved to: `~/brand-pulse/{brand-slug}/{date}.md`*
```

---

## Rendering rules

- Keep the executive summary under 120 words. No bullets inside it.
- Top complaints / feature requests = exactly 3 each unless fewer than 3 real clusters exist. In that case, say so: *"Only N meaningful clusters surfaced; additional items would dilute signal."*
- Every quoted line must have a real link right after it in markdown format.
- If a source returned nothing useful, include its subsection and write: *"No meaningful results this run."* Do not silently omit.
- If the entire run had <20 total mentions, add a warning block at top:
  > ⚠️ Low data volume ({N} total mentions). Treat rankings as directional, not conclusive.
- Dates: use ISO format (YYYY-MM-DD). Relative times only in "Since Last Pulse."
