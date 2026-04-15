# Repo Safety Audit — Quick Start

Three minutes. You'll have your first audit result before your coffee's cold.

## Step 1 — Install the skill

From the `beginnersinai-skills` marketplace:

```
/plugin marketplace add beginnersinai/claude-skills-marketplace
/plugin install repo-safety-audit@beginnersinai-skills
```

## Step 2 — (Optional but recommended) Authenticate the GitHub CLI

Step 6 of the audit (developer reputation) uses the `gh` CLI. If you don't have it authenticated, the skill gracefully skips that step — but you'll miss the account-age and repo-health signals.

```
gh auth login
```

Pick GitHub.com → HTTPS → authenticate in browser. One-time setup.

## Step 3 — Turn on auto-updates (IMPORTANT)

Third-party plugins don't auto-update by default. Flip it on once:

1. Type `/plugin`
2. Press **Tab** until you're on the **Marketplaces** tab
3. Select **beginnersinai-skills**
4. Choose **Enable auto-update**

Done once, good forever.

## Step 4 — Run your first audit

Grab any GitHub URL, paste it in Claude Code, and ask:

> audit this repo: https://github.com/some-owner/some-repo

Or any of these:
- "is this safe to install?"
- "should I install this?"
- "vet this plugin for me"
- "check this github"

The skill runs through six checks and gives you a verdict block like this:

```
### Verdict: SAFE

**Prompt injection:** Clean
**Shell exec & exfil:** Clean
**Imports:** Match purpose (requests for API calls, click for CLI)
**External URLs:** All expected (github.com, pypi.org)
**Developer:** Established (2,400 followers, 47 repos, account 6 years old)
**Repo health:** 1,200 stars, 180 forks, last push 3 days ago, MIT license

**Why this verdict:** No concerning patterns found. Developer has a long public
track record and the imports match the stated purpose of the tool.
```

## Step 5 — Act on the verdict

- **SAFE** → install and use normally
- **CAUTION** → sandbox first if possible, or read the cited concerns and judge for yourself
- **AVOID** → don't install. If the skill flagged an actual payload, consider reporting the repo.

---

## Common questions

**Q: How long does an audit take?**
Usually 30 seconds to 2 minutes, depending on repo size. Larger repos take longer because there are more files to grep.

**Q: Does it work on local installs too?**
Yes. Point it at any path on disk — e.g. `~/.claude/skills/some-skill/` — and it'll audit what's actually on your machine. This is preferred over auditing the remote repo, because what's installed may differ from what's on GitHub.

**Q: Does it work on npm packages?**
Yes. Point it at the GitHub repo for the package (or at the installed files under `node_modules/package-name/`). Pair with `npm audit` for dependency CVEs.

**Q: Can it audit MCP servers?**
Yes. MCP servers are the highest-risk install category because they can expose arbitrary tools to Claude — always audit before installing one from an unfamiliar source.

**Q: What if it says SAFE but I'm still unsure?**
Trust your gut. The skill is a strong signal, not a guarantee. If something feels off, don't install. Reply to the audit asking "what did you find suspicious?" and the skill will cite its reasoning in more detail.

---

Need help? Email hello@beginnersinai.org or post in the [Skool community](https://skool.com/beginnersinai).
