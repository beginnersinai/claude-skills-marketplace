# Playwright Flows — Enhanced Mode

Per-site scripts for authenticated social coverage. Only runs when:
1. The Playwright MCP plugin is installed (tools `mcp__plugin_playwright_playwright__*` available), AND
2. The user selected Enhanced mode for this run, AND
3. The user has that specific social listed in their `logged_in_socials` config.

## Global rules

- **Read-only.** Never click Like, Follow, Share, Comment, Send, Post, or any state-changing button. Only navigate, scroll, and snapshot.
- **Throttle.** `browser_wait_for({time: 3})` between substantive interactions. Longer (5s) before scroll. Longer still (8–10s) if a CAPTCHA or interstitial appears.
- **Max 5 scroll iterations per site.** That's enough for 50–100 items, more than we need.
- **Graceful failure.** If a site redirects to a login page, the user's session expired. Stop that source, log it in the coverage section, move on. Do not try to log in.
- **Snapshot over screenshot.** Use `browser_snapshot` for structured accessibility-tree data (better for extraction). Reserve `browser_take_screenshot` for when the user asks for visual proof.
- **No PII capture.** If a snapshot includes a DM inbox, a personal email, or unrelated private content, discard the snapshot and navigate directly to the intended URL.

## X / Twitter

```
1. browser_navigate → https://twitter.com/search?q={brand}&src=typed_query&f=live
2. browser_wait_for({time: 3})
3. browser_snapshot → note initial tweet set
4. Loop up to 5x:
     browser_press_key → End  (scrolls timeline)
     browser_wait_for({time: 4})
     browser_snapshot
     if no new tweets appeared → break
5. Extract per tweet: author handle, display name, tweet text, timestamp, like count, reply count, retweet count, URL
6. Filter: discard ads (have "Ad" badge), discard replies to unrelated threads where the brand is only in quoted text
```

If redirected to `/i/flow/login` → session expired. Note and skip.

## LinkedIn

```
1. browser_navigate → https://www.linkedin.com/search/results/content/?keywords={brand}&sortBy=%22date_posted%22
2. browser_wait_for({time: 4})
3. browser_snapshot
4. Loop up to 5x:
     browser_press_key → PageDown
     browser_wait_for({time: 4})
     browser_snapshot
5. Extract per post: author name, author title, post text (expand "see more" where present via browser_click on that element specifically), reactions count, comments count, timestamp, post URL
6. Also try company page: https://www.linkedin.com/company/{slug}/posts/?feedView=all
```

Triggering LinkedIn's bot detection leads to a session lock. If you see any "verify you're a human" interstitial, stop immediately.

## Instagram

```
1. browser_navigate → https://www.instagram.com/explore/tags/{brand-no-spaces}/
2. browser_wait_for({time: 4})
3. browser_snapshot → capture top posts grid
4. Pick top 6 recent posts (non-reels preferred for caption depth)
5. For each:
     browser_click → the post thumbnail
     browser_wait_for({time: 3})
     browser_snapshot → capture caption + visible comments
     browser_press_key → Escape  (close modal)
     browser_wait_for({time: 2})
6. Extract: caption text, like count, comment count, top 3–5 comment texts, post URL
```

If tag page is empty → try `https://www.instagram.com/{handle}/` if user provided a handle, else note no coverage.

## TikTok

```
1. browser_navigate → https://www.tiktok.com/search?q={brand}&t=videos
2. browser_wait_for({time: 4})
3. browser_snapshot → top video grid
4. Loop up to 5x:
     browser_press_key → PageDown
     browser_wait_for({time: 4})
     browser_snapshot
5. Extract per video: creator handle, video caption, like count, comment count, view count, share count, video URL
6. For the top 3 videos:
     browser_click → video thumbnail
     browser_wait_for({time: 4})
     browser_snapshot → capture top comments from comment drawer
     browser_navigate_back
     browser_wait_for({time: 2})
```

## Facebook

Only for Companies. Facebook's search is aggressively rate-limited.

```
1. browser_navigate → https://www.facebook.com/{brand}/reviews (if page exists)
   Fallback: https://www.facebook.com/search/posts/?q={brand}
2. browser_wait_for({time: 5})
3. browser_snapshot
4. Loop up to 3x (FB is stricter):
     browser_press_key → End
     browser_wait_for({time: 6})
     browser_snapshot
5. Extract per review/post: reviewer/author, text, recommendation (pos/neg), date, reaction counts
```

Facebook is the most likely to hit a rate-limit or CAPTCHA. If anything abnormal appears, stop and note in coverage.

## Extraction format (all sites)

For each item captured, produce a JSON-like record:

```
{
  "source": "x" | "linkedin" | "instagram" | "tiktok" | "facebook",
  "url": "...",
  "author": "...",
  "text": "...",
  "engagement": { "likes": N, "comments": N, "shares": N },
  "timestamp": "YYYY-MM-DD" or "approx_date: 3 days ago",
  "classification": "complaint" | "feature_request" | "praise" | "neutral" | "noise"
}
```

Then hand this to the clustering step (SKILL Step 6).

## When to bail

- Login page redirect → session expired. Note and move on.
- CAPTCHA or "verify you're a human" → stop immediately. Note and move on.
- HTTP 429 or obvious throttling → stop that site, don't retry. Note coverage gap.
- Any unexpected page structure (redesign, A/B test) → extract what's visible via `browser_snapshot`, don't force-fit. Note that the extraction may be incomplete.

## Ethical guardrails — non-negotiable

- **No writes.** No clicks on interactive state-changing elements. Ever.
- **No scraping DMs.** Even if surfaced in a snapshot, discard.
- **No capturing third-party PII.** Skip profile photos, bios of non-public figures.
- **No impersonation.** Never fill forms, never type anywhere except search boxes.
- **Rate limit yourself.** Better to get 30 items politely than 200 items and a banned account.
