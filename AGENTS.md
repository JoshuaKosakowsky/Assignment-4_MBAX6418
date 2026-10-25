# Agent guide — Assignment 4 individual work

Follow direct user instructions first. This guide applies throughout this repo.

## Start and finish every session

1. Read handoff.md, PLAN.md and the assigned task. Verify the actual branch,
   recent commits and working-tree changes; preserve existing edits.
2. On first visit read README, CONTRIBUTING and docs/ASSIGNMENT.md.
3. Work on the requesting student's personal branch, normally
   `individual/<github-username>`; Joshua uses `individual/joshua`. If the owner
   cannot be identified, ask before editing another person's work.
4. Make the smallest useful change, run relevant checks and update handoff.md
   before ending an implementation session. Report actual outcomes and limits.

## Boundaries

- This is individual coursework with optional discussion and troubleshooting.
  Each student must complete their own training run, evaluation and submission,
  check the agent's work, and explain and repeat the process independently.
- Main is a frozen baseline after the one-time migration. Never commit, push,
  merge, delete or rewrite main, bypass protection or unlock it without explicit
  owner authorization for a baseline maintenance change.
- Personal work stays on its owner's branch. PRs and teammate approval are
  optional; feedback PRs target the requesting owner's personal branch, not main.
  Do not modify another student's branch without explicit permission.
- Joshua authorizes commits and pushes for his requested work in this repo.
  Other students' publication preferences must come from their own instructions.
- Joshua handles collaborator invitations. Do not infer task ownership, assign
  classmates or send messages without instructions.
- Keep secrets in environment variables or ignored .env. Never print or publish
  credentials, private uploads, raw datasets, adapters or generated submissions.
  This repo and all its branches are public; personal branches are not private.
- The course PDF and split_data stay outside Git. No model, prompts, training
  settings or deliverables have been chosen by this baseline. Read the full brief
  with the student before implementing their assignment; make choices with them.
- Do not spawn agents unless the user or applicable instructions ask.

## Verification and records

Use `python scripts/verify_repo.py`, `python -m unittest discover -s tests -p
'test_*.py'` and `git diff --check`; see docs/TESTING.md. Add meaningful checks
for actual implementation behavior as work develops. Repository CI is not
evidence of training, inference, data integrity or submission readiness.

Update affected docs, not every file each time. README owns setup/use; PLAN owns
personal scope; docs/ASSIGNMENT.md owns verified requirements; docs/TEST_RESULTS.md
owns evidence. docs/CONTRIBUTIONS.md is optional personal attribution, not group
submission credit. handoff.md should be concise (roughly 15–25 lines), with date
and timezone, agent, owner/branch/base, changes, commands/results, unchecked areas
and next steps. Do not include secrets or transcripts.

A personal change is ready when its stated behavior is verified, relevant checks
pass and affected records are current. No mandatory teammate review is required.
Assignment completion requires the student's own end-to-end verification of the
full course brief and all four submission files; this baseline does not provide it.
