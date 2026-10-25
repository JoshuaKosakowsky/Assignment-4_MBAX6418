# Verification evidence

## Initial scaffold — 2026-10-24 America/Denver

- `python3 scripts/verify_repo.py`: PASS; 23 staged scaffold files, local links,
  tracked-file safeguards and saved protection policy.
- `python3 -m unittest discover -s tests -p 'test_*.py'`: PASS; 10 hook checks.
  Initial run exposed older system Git lacking `git hook run --to-stdin`;
  tests now feed the actual hook scripts stdin directly without that newer flag.
- `git diff --cached --check`: PASS; no whitespace errors.

## Published baseline — 2026-10-24 America/Denver

- Baseline commit: `8deef2963cd7fe434f6bc17aa205487958892b0d`.
- GitHub repository readback: PUBLIC; default branch `main`.
- [Baseline CI run](https://github.com/JoshuaKosakowsky/Assignment-4_MBAX6418/actions/runs/40147904246):
  completed successfully; required `test` job passed scaffold validation and hook tests.
- Applied `.github/main-protection.json`, then independently fetched the policy
  and compared every configured field: PASS, exact match. Admin enforcement,
  strict `test`, one review, stale dismissal, latest-push approval, conversation
  resolution, and force-push/deletion restrictions verified.
- Configured the five type labels and four status labels in CONTRIBUTING.
- Local hooks enabled with `core.hooksPath=.githooks`, `core.longpaths=true`, and
  `assignment4.allowPush=true`. Each teammate configures their own clone.
- No collaborator invitations or assignments sent; Joshua manages those.

The sections above describe the original policy and are historical. The individual-work
migration below supersedes the mandatory teammate-review workflow. GitHub Actions
and branch settings remain authoritative for current server state.

Not tested: assignment requirements, datasets, app behavior, services, deliverables
or submission readiness. No application or app dependencies exist in this scaffold.

## Individual-work migration — 2026-10-25 America/Denver

- Prepared on `codex/setup-verification` from `b64299f`; existing PR #1 is reused
  for the one-time baseline migration. Joshua explicitly authorized publication
  and changing the repository to personal branches with frozen main.
- `python scripts/verify_repo.py`: PASS; 23 tracked files, links, tracked-file
  safeguards and final locked-main policy.
- `python -m unittest discover -s tests -p 'test_*.py' -v`: PASS; all 10 tests on
  Windows with Python 3.14 and Git Bash on PATH. The first run could not find
  `sh`; adding Git for Windows' bin directory to PATH fixed the environment.
- `git diff --check`: PASS. Existing hook-only executable-bit differences were
  Windows filesystem artifacts; local `core.filemode=false` preserves the tracked
  executable modes. Hook contents were deliberately updated for frozen main.
- CI now runs on all branch pushes and optional PRs. The final saved main policy
  enables branch lock/admin enforcement, retains strict `test` and conversation
  resolution, and removes mandatory teammate/latest-push approval.
- GitHub CI, merge and final API readback are pending at this commit. Completion
  evidence will be recorded on `individual/joshua` after main is frozen.
- No assignment notebook, training, data validation, inference, service calls or
  submission artifacts were implemented or tested. No invitations were sent.
