# Individual work and optional feedback

Submissions are individual. Classmates may discuss ideas and troubleshoot, but
each student must complete their own training run, verify outputs and explain
and repeat the process independently. Follow [docs/ASSIGNMENT.md](docs/ASSIGNMENT.md)
and the full course brief.

## Personal branches

1. Create `individual/<your-github-username>` from the frozen `origin/main` baseline.
   Joshua uses `individual/joshua`. Continue on your own branch for this assignment.
2. Keep your notebook, implementation, decisions, tests and handoff on that branch.
   Commit and push your own work when appropriate. No shared task lead, integration
   owner, mandatory PR, teammate approval or group completion record is required.
3. Run relevant checks, inspect what you publish and record actual outcomes.
   Use [docs/TESTING.md](docs/TESTING.md) and [docs/COMMITS.md](docs/COMMITS.md).
4. Complete your own training, evaluation, report and Canvas submission. Another
   student's adapter, predictions or report do not establish completion of yours.

Do not update, delete or rewrite another person's branch without explicit
permission. Git collaborators technically share write access; branch names are
a convention, not access controls. Never force-push another person's work.

## Main stays frozen

After the one-time individual-work migration, main is locked read-only on GitHub.
Personal changes stay on personal branches and are not merged into main.
Hooks block local main commits and all pushes/deletions targeting main.
Do not unlock main or change its protection without Joshua's explicit authorization
for a future baseline maintenance change.

## Optional feedback

Use discussions, issues or a branch diff to request advice. With the branch
owner's permission, create a short-lived feedback branch from their personal
branch and open a PR **back to that personal branch**, never main. The owner
decides whether to accept it and remains responsible for their individual work.
Feedback reviews are optional; no teammate approval is needed for personal work.
Do not send invitations, assign classmates or post messages on their behalf
unless instructed. Issues and existing labels are optional organizational aids.

## Records and publishing

README owns setup/use; PLAN owns personal scope; docs/ASSIGNMENT.md records verified
requirements; docs/TEST_RESULTS.md records actual evidence; handoff.md records
resumption state. Maintain these on your branch as relevant. Contributions are
optional personal notes, not shared credit for a submission. Keep credentials,
private uploads, course datasets, adapters and generated submissions outside Git.
All branches in this public repo are publicly visible.
