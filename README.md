# Assignment 4 — MBAX 6418-801

**Status: team collaboration scaffold only.** Assignment requirements, deliverables,
application design and implementation have deliberately not been started.

Repository: [Assignment-4_MBAX6418](https://github.com/JoshuaKosakowsky/Assignment-4_MBAX6418).
Joshua manages teammate invitations through [GitHub collaborator settings](https://github.com/JoshuaKosakowsky/Assignment-4_MBAX6418/settings/access).
No collaborator invitations or task assignments have been made by this scaffold.

## Start here

- Agents: [AGENTS.md](AGENTS.md), then [handoff.md](handoff.md).
- Team workflow: [CONTRIBUTING.md](CONTRIBUTING.md).
- Current scope and next steps: [PLAN.md](PLAN.md).
- Assignment intake boundary: [docs/ASSIGNMENT.md](docs/ASSIGNMENT.md).
- GitHub protections: [docs/GITHUB_SETUP.md](docs/GITHUB_SETUP.md).
- Verification: [docs/TESTING.md](docs/TESTING.md), [docs/TEST_RESULTS.md](docs/TEST_RESULTS.md).
- Completion credit: [docs/CONTRIBUTIONS.md](docs/CONTRIBUTIONS.md).

## Join and configure your clone

Accept Joshua's GitHub invitation, then use Git and Python 3.12+:

```sh
git clone https://github.com/JoshuaKosakowsky/Assignment-4_MBAX6418.git
cd Assignment-4_MBAX6418
git config --local core.hooksPath .githooks
git config --local core.longpaths true
git config --local assignment4.allowPush true
python scripts/verify_repo.py
python -m unittest discover -s tests -p 'test_*.py'
git switch -c codex/your-task
```

Use `python3` if that is your local Python command. The checks use only the
standard library; no application dependencies or install/launch command exist yet.
Hooks are local Git configuration and must be enabled in each clone. GitHub
protects `main` independently. All changes after the initial empty-repo bootstrap
use task branches and reviewed pull requests, including documentation/setup.

## Scope and local course materials

This scaffold adapts Assignment 3's collaboration process at commit `301585b`.
It does not reuse its music app requirements, service contracts or credentials.
The supplied assignment PDF and `split_data/` remain in the parent Assignment 4
folder, outside this repository. They have not been analyzed or published.
Teammates need their own course-provided copies until the team reviews sharing
permission and records a reproducible data/setup process. Do not copy source
course materials or datasets into Git merely to make a check pass.

Keep credentials in environment variables or ignored `.env`; `.env.example`
contains comments only until configuration is chosen. Do not copy another
assignment's keys. No project license or application stack has been selected.
CI success means the repository checks passed, not assignment completion.
