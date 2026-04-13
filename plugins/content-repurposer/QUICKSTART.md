# Quick Start — AI Content Repurposer

**Time required:** 5 minutes
**You need:** Claude Code installed on your machine ([install guide](https://docs.claude.com/en/docs/claude-code/quickstart))

This is the absolute beginner version. Type each command exactly as shown.

---

## Step 1 — Add the Marketplace (30 seconds)

The AI Content Repurposer lives in the **Beginners in AI marketplace**, which is a free catalog of AI plugins. You add the marketplace once, then install plugins from it.

In Claude Code, type:

```
/plugin marketplace add beginnersinai/claude-skills-marketplace
```

You'll see a confirmation message. The marketplace is now registered.

---

## Step 2 — Install AI Content Repurposer (30 seconds)

```
/plugin install content-repurposer@beginnersinai-skills
```

Claude Code downloads the plugin and confirms installation.

---

## Step 3 — Turn on Auto-Updates (1 minute) ⭐ DON'T SKIP THIS ⭐

By default, Claude Code does **not** automatically update plugins from third-party marketplaces. That means when we ship a new version with bug fixes or new features, you won't get it unless you opt in.

Here's how to opt in (one time, takes 30 seconds):

1. Type `/plugin` and press Enter — this opens the plugin manager
2. Press **Tab** until you reach the **Marketplaces** tab
3. Select **beginnersinai-skills** from the list
4. Choose **Enable auto-update**
5. Press **Esc** to close the manager

Done. Every time Claude Code starts from now on, it will check for new versions and pull them automatically. You'll see a notification if anything was updated, and Claude will prompt you to run `/reload-plugins` to activate.

> **Why is this off by default?** Anthropic enables auto-update for the official marketplace they maintain, but disables it for third-party marketplaces (like Beginners in AI) so you have to explicitly trust the source. Once you enable it, you're saying "I trust this marketplace to send me updates."

---

## Step 4 — Run Your First Command (2-3 minutes)

Open a project that has a blog post, article, or any written content. Then type:

```
/content-repurposer:repurpose
```

The plugin will ask you to point to your source content. You can:
- Give it a file path (e.g., `blog-post.md`)
- Paste text directly
- Say "use my latest" and it'll find your most recent article

It will then generate 10 platform-native formats in a folder, each one ready to copy and paste:

1. **X/Twitter Thread** — 5-12 tweets with a hook
2. **LinkedIn Post** — professional, under 3,000 characters
3. **Email Newsletter** — with subject line and PS
4. **LinkedIn Carousel** — 7-10 text slides for Canva
5. **YouTube Script** — 8-12 minutes with speaking cues
6. **Short-Form Video** — 30-60 second TikTok/Reels script
7. **Blog Summary** — 200-400 words with SEO keywords
8. **Quote Graphics** — 5-8 pull quotes for Canva
9. **Podcast Talking Points** — bullet format (not a script)
10. **Community Post** — discussion-starter for Skool/Discord

---

## How Often Should I Use This?

**Every time you publish content.** The whole point is that you already did the hard part — the writing. This plugin turns that one effort into 10 pieces of distribution content.

A good rhythm:
- Write one article per week
- Run `/content-repurposer:repurpose` on it
- Spend 30-60 minutes posting the generated content across platforms throughout the week

For deeper single-platform work: `/content-repurposer:adapt` gives you 3 variations for one platform.

For batch planning: `/content-repurposer:batch` takes multiple articles and builds a content calendar.

---

## Help — Something Isn't Working

### "Command not found"
You forgot the namespace prefix. It's `/content-repurposer:repurpose`, not just `/repurpose`. Plugin commands are always prefixed with the plugin name.

### "Plugin not found in marketplace"
Run this to refresh the marketplace catalog:
```
/plugin marketplace update beginnersinai-skills
```
Then try installing again.

### "I installed it but nothing happens when I type the command"
Run this to reload all plugins in the current session:
```
/reload-plugins
```

### "I don't see the auto-update toggle"
Your Claude Code version might be too old. Update with:
- **Homebrew:** `brew upgrade claude-code`
- **npm:** `npm update -g @anthropic-ai/claude-code`
- **Native installer:** Re-run the install command from the [Setup guide](https://docs.claude.com/en/docs/claude-code/setup)

### "I had a previous version under a different name"
If the plugin was renamed at some point, Claude Code treats the old name and new name as different plugins. To migrate:

```
/plugin uninstall [old-name]@beginnersinai-skills
/plugin install content-repurposer@beginnersinai-skills
/reload-plugins
```

Then enable auto-update (Step 3 above) so future updates land automatically.

---

## Manual Updates (if you skipped auto-update)

If you didn't enable auto-update, here's how to manually pull the latest version:

```
/plugin marketplace update beginnersinai-skills
/plugin update content-repurposer@beginnersinai-skills
/reload-plugins
```

The first command refreshes the marketplace catalog. The second command pulls any new version of this specific plugin. The third command activates the new version without restarting Claude Code.

---

## Uninstalling

If you ever want to remove the plugin:

```
/plugin uninstall content-repurposer@beginnersinai-skills
```

Or via the UI: `/plugin` → **Installed** tab → select the plugin → **Uninstall**.

---

## Next Steps

After your first run:
1. **Open the generated folder** and browse the 10 files
2. **Post one format today** — start with email or LinkedIn
3. **Post 2-3 more tomorrow** — X thread, community post
4. **Run it again next week** on your next article
5. **Share your results** in the Beginners in AI community: https://www.skool.com/beginnersinai

---

**Made by [Beginners in AI](https://beginnersinai.org)** — turning AI research into practical tools for non-technical business owners.
