# Agent guide — Assignment 4, MBAX 6418-801

Follow direct user instructions first. This guide applies throughout this repo.

## Start and finish every session

1. Read `handoff.md`; verify branch, recent commits and working-tree changes.
   Preserve other people's edits and check handoff claims against actual state.
2. Read the assigned task and `PLAN.md`. On the first visit read README,
   CONTRIBUTING and docs/ASSIGNMENT.md; then inspect files relevant to the task.
3. Make the smallest useful change, run relevant checks and update **handoff.md
   before ending the session or switching agents/models**. Report actual results.

## Current boundary

- Initial setup only. Do not analyze the assignment, invent requirements, create
  feature issues, choose an app stack or implement deliverables until asked.
- Local commits on task branches are authorized. After initial empty-repository
  bootstrap, all changes use task branches and reviewed PRs. No direct main
  commits/pushes, admin bypasses or weakening of main protection.
- Joshua/the team handles invitations and lead/contributor assignments; do not
  send invitations, assign people or infer ownership from Assignment 3.
- Secrets stay in environment variables or ignored `.env`. Never print, commit
  or copy credentials from another assignment. No live service calls in setup/CI.
- Course PDF and `split_data/` stay outside this repo pending an explicit sharing
  review. No raw datasets, uploads, generated output or private service docs in Git.
- Report implemented, tested, untested and deferred behavior accurately.

## Work and collaboration

Use `codex/<task>` branches from current main. Follow CONTRIBUTING for review,
labels and ownership; follow docs/COMMITS.md for commit style. Keep one substantial
PR active per contributor. Coordinate shared interfaces and files before parallel
implementation. Do not spawn agents unless the user or applicable instructions ask.

Fix small related reversible problems directly in the current change. Avoid
unnecessary issues, abstractions, dependencies, duplicate logic and unrelated
refactors. Separate independent scope/interface changes and preserve others' work.
After requirements intake, connect work to verified acceptance checks; never
substitute CI or component tests for demonstration of required user behavior.

Current checks: `python scripts/verify_repo.py` and
`python -m unittest discover -s tests -p 'test_*.py'`. Use docs/TESTING.md.
Do not add tests that merely repeat prose. Rerun after changes/failures or an
unresolved concern, rather than repeatedly running passing checks.

## Records to maintain

- README: onboarding, setup and use.
- PLAN: scope, milestones, integration ownership; GitHub issues own active status.
- docs/ASSIGNMENT.md: verified requirements after authorized intake.
- docs/TEST_RESULTS.md: actual verification evidence and limitations.
- docs/CONTRIBUTIONS.md: substantial completed work and reviews with evidence.
- handoff.md: concise resumption state every session (roughly 15–25 lines).

Update affected records, not every document on every edit. Handoff includes date
and timezone, agent, task/branch/base commit, changes/decisions, commands/results,
unchecked areas/blockers and next 1–3 actions/links. Preserve pending parallel
notes if any. Never include secrets or chat transcripts. Record a pre-handoff
hash rather than repeatedly amending to cite the handoff's own commit.

## Done

A PR meets its stated checks, has relevant passing validation, safe inspected
files, current affected docs and handoff, and an eligible teammate approval.
Assignment completion can only be assessed after requirements intake and actual
end-to-end verification; this scaffold does not establish readiness to submit.
