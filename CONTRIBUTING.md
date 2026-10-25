# Contributing — Assignment 4

Agents follow [AGENTS.md](AGENTS.md). Start with README and PLAN.
Current work is setup only; assignment requirements and implementation are deferred.
Joshua/the team arranges invitations and assignments.

## Team workflow

1. Claim a substantial task with concrete completion checks, one lead and up to
   two contributors (maximum three assignees). The lead owns acceptance and merge.
   Before issues exist use PLAN; afterward GitHub issues own active task status.
2. Branch from current main: `codex/<task>` for agents or `type/slug` for teammates.
   Keep one substantial PR active per contributor; coordinate shared files/interfaces.
3. Implement the smallest useful result. Small related fixes stay in the same
   change; separate independent scope changes. Avoid process issues for typos.
4. Run relevant checks in docs/TESTING.md, inspect the diff and update affected docs
   and handoff. Follow docs/COMMITS.md; wording preferences are non-blocking.
5. Open a focused PR with result, actual validation and linked task. Use `Refs #N`
   for partial work; `Closes #N` only when that issue's completion checks are met.
6. Batch blocking findings, fix them and rerun relevant checks before re-review.

All changes after the initial empty-repository bootstrap use reviewed PRs,
including setup. Local task-branch commits and publication of assigned work are
authorized. No direct main updates, protection bypasses or force pushes.

## Review and merge

- Main requires one approving review, current passing `test`, an up-to-date branch,
  resolved conversations and approval of the latest push. Rules apply to admins.
- The PR author cannot self-approve. A teammate with no commits on the PR may
  review/approve/request changes. Freeze branch pushes when requesting review;
  new pushes dismiss stale approvals. The approving reviewer must not be the pusher
  of the latest reviewable push.
- The approving reviewer or issue lead merges when GitHub permits it. Prefer a
  non-author merge; an author may merge after eligible approval exists.
- Blocking findings: broken required behavior, unsafe handling, incompatible
  contracts, failed relevant checks or unmet acceptance. Include reproduction and
  expected behavior. Preferences, optional refactors and wording are suggestions.
- Review the actual behavior, not test counts. After intake, parent features close
  only after integrated user-flow verification; component PRs may have narrower scope.

### Original blocking reviewer unavailable

Prefer the original reviewer for re-review. If unavailable, a teammate other than
the fix author must independently verify every blocking finding against the current
PR head, including relevant regressions. Record findings, fix commit, actual results
and verifier in the PR. A maintainer with permission may then dismiss the outdated
review with the reason and evidence link. This is not the original reviewer's
approval. An eligible replacement reviewer can approve; all remaining protections
still apply. Never dismiss unresolved findings or weaken rules for a deadline.

## Labels

Each work issue and PR has one primary type and one current status. Replace the
previous status as work progresses; closed/merged state records completion.

| Type | Use |
|---|---|
| bug | Broken behavior |
| enhancement | New/improved feature |
| documentation | Instructions, report, handoff |
| testing | Tests and evidence |
| infrastructure | Setup, CI, dependencies, deployment |

Statuses: `status: ready`, `status: in progress`, `status: blocked` (explain blocker
and next action), `status: review`. Use assignees for ownership; prefer the linked
issue's type for its PR. Do not create issues merely to attach labels.

## Maintain useful records

README owns setup/use; PLAN owns scope/milestones/integration ownership; issues
own active status; docs/ASSIGNMENT.md owns verified requirements after intake;
docs/TEST_RESULTS.md owns evidence; handoff owns resumption. Update the affected
source and summary rather than duplicating status everywhere.

When substantial work merges or a review finishes, add a brief evidence-backed
entry to docs/CONTRIBUTIONS.md. Credit implementation, review, debugging, testing,
integration and docs to the responsible teammate(s), including AI-assisted work.
No rankings or commit/line counts. Do not claim a whole feature from a component.
Never include credentials, private uploads or unreviewed course data in reports.
