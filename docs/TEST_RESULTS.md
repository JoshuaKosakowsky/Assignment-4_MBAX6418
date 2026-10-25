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

GitHub Actions and branch settings remain authoritative for current server state.
This verification record uses a task branch/PR after bootstrap; it cannot bypass
teammate approval or merge itself without an eligible review.

Not tested: assignment requirements, datasets, app behavior, services, deliverables
or submission readiness. No application or app dependencies exist in this scaffold.
