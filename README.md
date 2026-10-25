# Assignment 4 — MBAX 6418-801

**Individual submissions; optional discussion and troubleshooting.** Each student
owns their code, notebook, training run, evaluation, interpretation and submission.
This repository provides a common starting point and optional visibility into
classmates' work. It does not represent a combined group submission.

## Start here

- Agents: [AGENTS.md](AGENTS.md), then [handoff.md](handoff.md).
- Personal branches and feedback: [CONTRIBUTING.md](CONTRIBUTING.md).
- Joshua's completion plan: [PLAN.md](PLAN.md); requirements: [docs/ASSIGNMENT.md](docs/ASSIGNMENT.md).
- Adapter backups and recovery: [docs/ADAPTER_RECOVERY.md](docs/ADAPTER_RECOVERY.md).
- Main protection: [docs/GITHUB_SETUP.md](docs/GITHUB_SETUP.md).
- Checks: [docs/TESTING.md](docs/TESTING.md), [docs/TEST_RESULTS.md](docs/TEST_RESULTS.md).
- Individual work record: [docs/CONTRIBUTIONS.md](docs/CONTRIBUTIONS.md).

## Configure your clone and personal branch

Accept Joshua's invitation if you want to push a personal branch. Use Git and
Python 3.12+ (or `python3` where appropriate):

```sh
git clone https://github.com/JoshuaKosakowsky/Assignment-4_MBAX6418.git
cd Assignment-4_MBAX6418
git config --local core.hooksPath .githooks
git config --local core.longpaths true
git config --local assignment4.allowPush true
git fetch origin
git switch -c individual/YOUR-GITHUB-USERNAME origin/main
python scripts/verify_repo.py
python -m unittest discover -s tests -p 'test_*.py'
git push -u origin HEAD
```

Replace the placeholder with your own username. If your branch already exists
on GitHub, use `git switch --track origin/individual/YOUR-GITHUB-USERNAME` instead
of creating it from main. Continue on your own persistent branch each session.
Joshua's branch is `individual/joshua`.

`main` is the frozen common baseline after this workflow migration. Do not commit,
push or merge personal work into it. Personal branches are final homes for each
student's work; they do not need PRs or teammate approval. Feedback PRs must target
the requesting student's branch, with that student's permission.

This repository is **public**: every published branch is visible. Branch names
express ownership but do not enforce privacy or exclusive write access. Do not
edit someone else's branch without permission. Use your own repository if you
need a separate access boundary. Joshua manages collaborator invitations.

## Course materials and execution

The assignment PDF and `split_data/` remain in the parent Assignment 4 folder.
Use your own course-provided copies. Keep datasets, personal uploads, credentials,
adapter files and generated submission outputs outside Git. A personal branch
has the same public visibility as main. Store credentials in environment variables
or ignored `.env`; do not copy keys from another assignment.

Joshua's requirements review and completion plan are recorded on this branch.
No notebook, model, application stack or deliverables are implemented yet.
The checks use only Python's standard library and validate repository safeguards,
not assignment correctness. Each student must implement, execute and verify their
own work against the full course brief. The repository does not select model,
training settings, prompts or few-shot examples for students.
