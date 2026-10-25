# GitHub setup and main protection

Repository: [Assignment-4_MBAX6418](https://github.com/JoshuaKosakowsky/Assignment-4_MBAX6418).
Owner: JoshuaKosakowsky. Public visibility mirrors Assignment 3; course source
materials/datasets and secrets are excluded. Joshua handles invitations in
[collaborator settings](https://github.com/JoshuaKosakowsky/Assignment-4_MBAX6418/settings/access).
No invitation or ownership assignment is included in this setup.

## Required main protection

[main-protection.json](../.github/main-protection.json) matches Assignment 3's
live policy inspected on 2026-10-24:

- Strict passing `test` check from GitHub Actions app 15368; branch up to date.
- One approving review; dismiss stale approvals; require latest-push approval.
- Conversation resolution required and rules enforced for administrators.
- Force pushes and branch deletion disabled.
- No code-owner, signed-commit or linear-history requirement; branch not locked.

The saved JSON describes intended policy, not evidence of server enforcement.
Inspect live GitHub settings and Actions; record readback in docs/TEST_RESULTS.md.
After initial publication of the empty repository baseline, every change goes
through a task branch and reviewed PR. Never relax protection to merge.

## Maintainer commands

These use an authenticated GitHub CLI. Applying protection is an initial setup
operation; future changes need an explicitly authorized policy change.

```sh
gh api --method PUT repos/JoshuaKosakowsky/Assignment-4_MBAX6418/branches/main/protection --input .github/main-protection.json
gh api repos/JoshuaKosakowsky/Assignment-4_MBAX6418/branches/main/protection
gh run list --repo JoshuaKosakowsky/Assignment-4_MBAX6418
```

Enable hooks in each clone with README commands. They block main commits after
the first commit and all main pushes/deletion. Enable them after the one-time
empty-repo bootstrap push, before any team work. Task branch pushes require
`assignment4.allowPush=true`; this local guard complements server enforcement.

Use CONTRIBUTING's labels and review/merge rules. A public URL grants read access;
teammates still need an accepted collaborator invitation for write access.
