# Verification

From the repository root, with Git and Python 3.12+:

```sh
python scripts/verify_repo.py
python -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

Use `python3` where needed. No third-party dependencies are required.
The scaffold check needs tracked/staged files; stage an intended new scaffold
file before checking. It checks required files, Markdown links, known credential
patterns/private paths, the saved protection policy and handoff sections. It is
a limited guard, not a complete secret scanner; inspect the staged diff too.

Hook tests use a temporary repository and do not push to any remote. They check
main commit/push/deletion/rewrite rejection and task branch permission.
GitHub CI's `test` job runs the scaffold check and hook tests on main and PRs.
It does not validate assignment behavior or apply server protection.

Record commands, actual outcomes, tested commit and unchecked areas in
[TEST_RESULTS.md](TEST_RESULTS.md). Add appropriate behavior tests and actual
integration evidence once the implementation scope is authorized. There is no
application, service, dataset, deliverable or submission acceptance check yet.
