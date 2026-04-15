# Repo Safety Audit

**Vet any third-party skill, plugin, MCP server, GitHub repo, or npm package before you install it — in under two minutes.**

Every skill you install in Claude Code runs with your agent permissions. One malicious `SKILL.md` can read your `.env`, exfiltrate your credentials, or redirect Claude to attack your own files. Repo Safety Audit is the security review you'd want to do before clicking "install" — codified into a six-step workflow and a clear verdict.

## What it does

You paste a GitHub URL (or point it at a local install), and the skill runs through:

1. **File inventory** — catalogs the attack surface
2. **Prompt-injection scan** — greps markdown files for classic and novel injection patterns
3. **Shell execution & exfiltration** — looks for `curl | sh`, `eval`, base64-to-exec chains, unscoped `rm -rf`, credential reads
4. **Import / dependency audit** — checks whether imports match the stated purpose (networking libs in a tool that claims to work offline = flag)
5. **URL allowlist filter** — extracts every URL, filters known-safe domains, surfaces pastebins / webhooks / raw IPs
6. **Developer reputation** — queries GitHub API for account age, repo history, star/fork ratio, last push

Then it gives you a verdict: **SAFE**, **CAUTION**, or **AVOID** — with specific file and line citations for every concern.

## Quick start

1. Install from the `beginnersinai-skills` marketplace:
   ```
   /plugin install repo-safety-audit@beginnersinai-skills
   ```
2. Paste a GitHub URL in chat and ask: *"audit this repo"* / *"is this safe to install?"* / *"should I install this?"*
3. Read the verdict block.

The skill also auto-suggests itself after you install any third-party skill/plugin/MCP server from a source you haven't used before.

## When to run it

- Before installing any third-party Claude Code skill, plugin, or MCP server
- Before trusting an npm package with broad filesystem access
- Before running a bash installer piped from the web
- Any time a stranger's README says "just run this"
- Proactively after an unfamiliar install, if you forgot to do it before

## Verdict calibration

- **SAFE** — Clean across all 6 checks, developer has a real track record, code matches purpose. Proceed with normal caution.
- **CAUTION** — One or two yellow flags (new developer, unpinned deps, unusual but benign-looking imports). Safe to use with awareness; maybe sandbox first.
- **AVOID** — Confirmed injection payload, exfil pattern, obfuscation, or unscoped destructive command. Or a brand-new anonymous account shipping a tool that wants broad permissions.

When the skill is uncertain between SAFE and CAUTION, it errs toward CAUTION. Uncertain between CAUTION and AVOID, it errs toward AVOID. Your install, your risk — always prefer a false positive over a false negative.

## How it's different from `npm audit` / Snyk / Socket

Automated scanners catch **known CVEs** in dependencies — essential work, but reactive. Repo Safety Audit catches **intent**: a malicious skill author writing fresh exfiltration code will not show up in any CVE database, but a grep for `curl | sh` or `base64 | eval` will catch it instantly.

Use both layers:
- CVE scanners for dependency vulns
- This skill for novel malicious intent + prompt-injection

## What this skill does NOT do

- It does **not** execute the code. It reads it, greps it, and checks it against patterns.
- It does **not** replace your own judgment. When in doubt, sandbox first or don't install.
- It does **not** guarantee safety — a clever attacker can still slip something past static checks. Treat the verdict as a strong signal, not a certificate.

## Keeping Up to Date

Third-party marketplaces have auto-update **off** by default. Flip it on once and future versions land automatically:

1. Type `/plugin` in Claude Code
2. Press Tab to the **Marketplaces** tab
3. Select **beginnersinai-skills**
4. Choose **Enable auto-update**

Or update manually:

```
/plugin marketplace update beginnersinai-skills
/plugin update repo-safety-audit@beginnersinai-skills
/reload-plugins
```

## Privacy

- The skill reads public files on GitHub and local files you point it at.
- It makes read-only GitHub API calls via your `gh` CLI (if installed).
- Nothing leaves your machine. No telemetry. No accounts.

## License

MIT. Free forever.

---

Made by [Beginners in AI](https://beginnersinai.org). If this catches one bad install before it bites you, it's already paid for itself a hundred times over.
