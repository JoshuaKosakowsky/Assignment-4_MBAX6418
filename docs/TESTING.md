# Verification

From the repository root with Git and Python 3.12+:

```sh
python scripts/verify_repo.py
python -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

On Windows, run from Git Bash or add Git for Windows' `bin` directory to the
current PowerShell process before running hook tests (adjust the install path):

```powershell
$env:PATH = 'C:\Program Files\Git\bin;' + $env:PATH
```

Use python3 where needed. No third-party dependencies are required. The scaffold
check inspects tracked/staged files, required files, Markdown links, known
credential patterns/private paths, final main policy and handoff headings.
It is a limited safeguard, not a complete secret scanner. Inspect your diff too.

Hook tests use a temporary repository and never push to a remote. They verify
main commit/update/deletion/rewrite rejection, mixed-push rejection and personal
branch commits/pushes with publication opt-in. CI's `test` runs on all branch
pushes, PRs and manual dispatch, so personal work needs no PR to receive checks.
CI does not apply GitHub protection or enforce ownership of personal branches.

Record evidence and limitations in [TEST_RESULTS.md](TEST_RESULTS.md) on your
personal branch. Add meaningful behavior tests as implementation develops.
These checks do not validate datasets, training, model output, notebook execution,
evaluation results or submission artifacts. Check those against the full brief.
