#!/usr/bin/env python3
"""
UserPromptSubmit hook for the repo-safety-audit plugin.

Detects GitHub repository URLs in user prompts and injects a reminder
to ask the user whether to run a safety audit before acting on the URL.

Skips prompting when the user's message already explicitly requests an
audit. Deduplicates multiple URLs to the same repo.

Opt-out:
  Set env var REPO_SAFETY_AUDIT_SKIP_PROMPT=1 to silence this hook.
"""
import json
import os
import re
import sys

GITHUB_REPO_RE = re.compile(
    r'https?://(?:www\.)?github\.com/([\w.-]+)/([\w.-]+?)(?:/|\.git|$|\s|\)|,|\?|#|")',
    re.IGNORECASE,
)

AUDIT_REQUEST_PHRASES = (
    'audit this', 'audit the', 'audit it',
    'is this safe', 'is it safe',
    'should i install', 'safe to install',
    'vet this', 'vet it', 'vet the',
    'review this repo', 'check this github', 'check this repo',
    'safety audit', 'security audit',
    'repo-safety-audit', 'repo safety audit',
    'is this legit',
)


def main() -> None:
    if os.environ.get('REPO_SAFETY_AUDIT_SKIP_PROMPT') == '1':
        sys.exit(0)

    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    prompt = (data.get('prompt') or '').strip()
    if not prompt:
        sys.exit(0)

    matches = GITHUB_REPO_RE.findall(prompt)
    if not matches:
        sys.exit(0)

    repos = sorted({
        f"{owner}/{name[:-4] if name.lower().endswith('.git') else name}"
        for owner, name in matches
        if name and owner and owner.lower() not in ('orgs', 'users', 'settings')
    })
    if not repos:
        sys.exit(0)

    prompt_lower = prompt.lower()
    if any(phrase in prompt_lower for phrase in AUDIT_REQUEST_PHRASES):
        sys.exit(0)

    display = ', '.join(repos[:5])
    if len(repos) > 5:
        display += f' (and {len(repos) - 5} more)'

    reminder = (
        f"[repo-safety-audit plugin] The user's message contains a GitHub "
        f"repository URL ({display}). Before acting on it, pause and use the "
        "AskUserQuestion tool to ask: \"Want me to run a repo-safety-audit on "
        "this first to check for prompt injection, shell exfiltration, "
        "obfuscation, and developer-reputation concerns?\" with options "
        "'Yes, audit first (recommended)' and 'No, just proceed'. "
        "If they choose Yes, invoke the repo-safety-audit skill on the URL "
        "before doing anything else they originally asked. "
        "If they choose No, proceed with the original request but note that "
        "the audit was offered. "
        "(Users can silence this prompt by setting "
        "REPO_SAFETY_AUDIT_SKIP_PROMPT=1 in their shell environment.)"
    )

    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": reminder,
        }
    }
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
