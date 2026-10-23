# Same Assignment, Different Understanding

A team agreement starter for ChatGPT Edu, Codex, Linear, and GitHub. Surface different interpretations of a shared assignment before dividing the work. Suitable for coursework, joint research, software projects, and task forces.

## Start here

1. Use **Use this template → Create a new repository → Private**. Verify the Private label and invite your team. A public fork cannot be independently converted to private.
2. Follow [Windows and macOS setup](docs/local_setup.md) for Git and Python, plus optional Node.js when a web/npm project needs it, and open your private clone in Codex.
3. Read the [beginner workflow](docs/workflow.md). Individually answer the [agreement questions](docs/team_agreement.md), then compare interpretations in ChatGPT Edu.
4. Confirm the goal, scope, deliverables, and acceptance criteria together. Keep unanswered questions visible.
5. Discuss tasks in [Linear](docs/linear_tasks.md), implement one small agreed change, and request a PR review.
6. Share [redacted worklogs](docs/worklogs/README.md) and optionally use [contribution records and peer review](docs/contribution.md).
7. Prepare a research write-up with contribution evidence, run the [pre-submission AI review](docs/writeup_review.md), and have teammates verify findings and approve the final version.

The aim is to improve how teams work with AI: compare understanding before assigning tasks, preserve evidence while experimenting, and challenge the draft before submission. AI drafts and flags concerns; people confirm agreements, validate findings, and decide what to submit.

## What each tool does

| Tool | Team role |
|---|---|
| ChatGPT Edu | Compare independent interpretations, cite supplied evidence, and draft questions and agreements |
| Codex | Read repository instructions and the confirmed agreement; help implement and verify the agreed task |
| Linear | Team communication and task coordination: issue comments, mentions, questions, blockers, owners, and current status |
| GitHub | Versioned deliverables, design and agreement documents, redacted handoffs, and pull-request reviews |

Linear discussions link to the approved agreement version in GitHub. Current task status belongs in Linear; avoid maintaining a second live status table in Markdown. Without Linear, use GitHub Issues as the single task tracker. Service integrations require separate setup; links do not automatically synchronize anything.

## Use the Codex skill

Open the private repository in Codex and ask:

`$team-project-start Help our team compare our understanding of this assignment, confirm scope and completion criteria, and prepare our first task and sharing checks.`

The repository skill is in `.agents/skills/team-project-start`. Reopen the project or start a new chat if discovery needs refreshing. It does not grant account access or invite teammates. It can explain in your preferred language; shared template documents are in English.

## Implemented versus manual

Implemented: local pattern checks, Git-index checks, an opt-in pre-commit hook, redacted worklog drafts, and arithmetic from approved contribution records.

Manual starter materials: agreement questionnaire, comparison prompt, approval records, issue map, optional peer-review rubric, research write-up guide, and pre-submission AI review prompt and response ledger. There is no agreement web app, automatic approval verification, live Linear monitoring, automatic peer-score calculation, or automated paper-review service. Actual team impact has not been measured.

## Install local checks

Windows: `py -3 tools/install_guard_hook.py`

macOS: `python3 tools/install_guard_hook.py`

Before committing selected files: `python3 tools/repo_guard.py --staged` (Windows: `py -3`). The guard reads the Git index, not unstaged working-tree copies. See [AGENTS.md](AGENTS.md) and [SECURITY.md](SECURITY.md).

Hooks can be bypassed; PR CI runs after upload. Pattern checks do not prove that a file contains no secrets or personal data. Review changes locally and configure required checks and policy reviewers in each new repository.

## First contribution exercise

Improve this README by documenting how to run `scripts/analyze.py` from the repository root and what its output means. It reads six synthetic rows in `data/synthetic.csv`. Expanding the analysis or changing the data is outside this exercise.

## Contribution arithmetic

Run `python3 tools/contribution_score.py` (Windows: `py -3`). Use agreed activity points, credit shares, evidence, and independent acceptance, not commit counts or generated code volume. The synthetic example totals 80 accepted points: P01=25, P02=35, P03=20. It is not a grade or an authorship decision. Optional peer ratings are reported separately; see [the rubric](docs/peer_review.md).

## Privacy, reuse, and inspiration

Real team records belong only in your private project. Issues, invitations, Secrets, integrations, hooks, and required-check settings are not automatically copied. All public examples are synthetic. Code and original documentation are MIT licensed; project research and third-party materials retain their own rights.

The workflow design was informed by [GUAM's collaboration documentation](docs/reference_review.md). No GUAM source code, benchmark results, or team-specific configuration is included.
