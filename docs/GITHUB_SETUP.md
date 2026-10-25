# GitHub setup — frozen main and personal branches

Repository: [Assignment-4_MBAX6418](https://github.com/JoshuaKosakowsky/Assignment-4_MBAX6418).
Owner: JoshuaKosakowsky. Visibility: public, including every personal branch.
Joshua manages [collaborator access](https://github.com/JoshuaKosakowsky/Assignment-4_MBAX6418/settings/access).
No invitation or assignment is part of this migration.

## Final main policy

[main-protection.json](../.github/main-protection.json) describes the final policy:

- Main is locked read-only, with rules enforced for administrators.
- Force pushes, branch deletion and fork syncing are disabled.
- Strict GitHub Actions `test` check and conversation resolution remain enabled.
- Mandatory teammate approval and latest-push approval are disabled. Personal
  work has no mandatory PR or review and is never merged into main.

The saved JSON is intended configuration; only a live API readback confirms
enforcement. See [TEST_RESULTS](TEST_RESULTS.md) for evidence. Branch lock does
not change public visibility or prevent an administrator from changing settings.

## One-time transition

Joshua explicitly authorized publishing the individual-work setup on 2026-10-25.
Update existing setup PR #1, change the obsolete mandatory review policy while
retaining required CI, merge normally after green CI, then apply the final locked
policy and verify it. This is the last baseline update for this migration.
Do not use admin merge bypasses. Future unlocking needs explicit owner approval.

Use the authenticated CLI to inspect policy:

```sh
gh api repos/JoshuaKosakowsky/Assignment-4_MBAX6418/branches/main/protection
gh run list --repo JoshuaKosakowsky/Assignment-4_MBAX6418
```

Enable local hooks following README. They block main commits and all pushes or
deletions targeting main. Personal branch pushes require the local opt-in
`assignment4.allowPush=true`. Hooks supplement GitHub enforcement and must be
enabled separately in each clone. Personal branch names are ownership conventions;
they do not restrict other collaborators' technical write access.
