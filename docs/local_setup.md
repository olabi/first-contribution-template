# Windows and macOS setup

## Create your private project

Choose **Use this template → Create a new repository → Private**, confirm the Private label, and clone your new repository. Public forks cannot independently become private. Invitations, issues, Secrets, integrations, hooks, and required-check settings need separate setup.

## Required and optional tools

- Codex access through your institution or supported account, subject to its policies.
- Command-line Git for history and index checks.
- Python 3.10 or later for this template's scripts. No pip dependencies or API keys are required.
- GitHub account and private-repository access for remote collaboration.
- Linear account and team access only if using Linear; its browser interface is sufficient.
- GitHub Desktop is optional. Git must still be callable from the terminal for the checks.
- VS Code, Node.js, Homebrew, and GitHub CLI are not required by this kit.

## Windows

Install [Git for Windows](https://git-scm.com/install/windows) and a supported stable [Python](https://www.python.org/downloads/windows/) for your CPU architecture. Enable command-line access/PATH where offered. Reopen PowerShell and Codex, then check:

```powershell
git --version
py -3 --version
```

If the Python launcher is unavailable, verify `python --version` and use that command instead. Do not use the embeddable package for beginner installation. If `python` opens the Store, check the launcher or the official installation path. Managed devices may need administrator help.

Clone your private project, open it in Codex, and run from the repository root:

```powershell
py -3 tools/install_guard_hook.py
py -3 scripts/analyze.py
py -3 tools/contribution_score.py
```

## macOS

Check `git --version`. If Git is missing, install Apple's Command Line Tools:

```sh
xcode-select --install
git --version
```

Existing Homebrew users may follow Git's official installation instructions instead. Install a supported stable [Python for macOS](https://www.python.org/downloads/macos/) compatible with your OS. In a new terminal:

```sh
python3 --version
python3 tools/install_guard_hook.py
python3 scripts/analyze.py
python3 tools/contribution_score.py
```

Optional [GitHub Desktop](https://desktop.github.com/download/) downloads differ for Intel and Apple Silicon; check About This Mac.

## Git identity and first check

Commit author names and email addresses become part of Git history. Configure a team-approved display name and the exact GitHub noreply address shown in your account settings locally; do not submit that address in chat.

```sh
git config user.name "[display name]"
git config user.email "[your GitHub noreply address]"
git status
git remote -v
```

Confirm the remote points to the team's private repository. Use official browser authentication, not tokens pasted into commands or documents. Do not make the repository public to solve an access problem.

Expected synthetic output: rows=6, mean_study_hours=3.50, mean_quiz_score=75.00. The contribution fixture totals 80 accepted points (P01=25, P02=35, P03=20).

Read AGENTS.md and SECURITY.md, stage only intended files, and run `python3 tools/repo_guard.py --staged` (Windows: `py -3`). Install hooks in every clone and review changes to hooks, checkers, and CI.

This teaching setup was tested on Windows. macOS instructions follow official installation guidance and still need real-device verification. Prefer supported stable releases rather than fixed version numbers. Reference date: 2026-10-23.

Official reference: [Create a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
