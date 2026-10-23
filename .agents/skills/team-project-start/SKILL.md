---
name: team-project-start
description: Help beginners start or join coursework, joint research, development, or task-force projects with Codex, Linear, and GitHub. Compare assignment interpretations, confirm a small first task, prepare a private template-based project, and guide reviewed sharing and evidence-based contribution records. Not for routine isolated code edits.
---

# Start a team project

Use the user's preferred language; shared template documents are English. Respect their chosen tools and existing workspace. Template: https://github.com/olabi/first-contribution-template

## Establish context

Identify new versus existing project, purpose, repository, OS, and available connections from the conversation and workspace. Ask only for missing information needed to act. Use pseudonyms rather than collecting names or contact details.

For an existing project, read applicable AGENTS.md, SECURITY.md, README.md and folder instructions first. Preserve local changes, hooks, CI, and project conventions. State the applicable instructions, scope, and checks. Example owners and issue IDs are not real destinations. Skill invocation is not blanket authorization for external changes.

## Compare understanding before work

Use docs/team_agreement.md: collect independent interpretations of goals, scope, deliverables, criteria, and constraints. Compare with sentence IDs; separate assignment requirements, member interpretations, and AI proposals. Missing answers are unresolved, not opposition or consensus. Offer neutral questions. Members correct the comparison and confirm the agreement; do not invent approval. Record open questions, affected work to hold, and independently executable tasks. Reconfirm when scope changes.

## Prepare a private project

Prefer **Use this template → Create a new repository → Private**. A public fork cannot independently become private. Check available GitHub connector capabilities first, then use the logged-in browser if needed. Verify the created URL and private status before cloning. Do not substitute a public project when policy blocks private creation. Do not request passwords or token strings.

Without access, prepare local instructions and task drafts honestly. If an assets/template directory is available and the user chooses an offline start, copy it into a new requested folder without overwriting existing work and label it as local-only. Invitations and wider access need explicit recipient and permission instructions. Issues, invitations, Secrets, integrations, hooks, and required-check settings need separate setup.

## Connect tools and choose a ready task

Use docs/local_setup.md. Git and Python 3.10+ support the local checks; GitHub Desktop is optional. Do not add Node.js, Homebrew, GitHub CLI, or API keys as default prerequisites. Distinguish plugin installation, service login, team invitation, and folder access. Check read access without sending test comments or changing files.

Linear is the team's issue-based communication space for questions, feedback, mentions, blockers, owners, and current status. GitHub holds versioned agreements and deliverables. Use docs/workflow.md and docs/issue_map.md for authoritative records and stable cross-links. Check dependencies and duplicate ownership before taking a task. Automatic synchronization and @Codex cloud invocation are separate optional integrations.

Define one small task with goal, agreement version, deliverable, exclusions, acceptance criteria, reviewer, and evidence. Default exercise: improve README run instructions for synthetic data, not expand analysis. Create issues or send comments only when authorized and real destinations are known; otherwise prepare drafts. Do not assign someone without their user's authorization.

## Check sharing and hand off

Instructions are not proof of safety. Run tools/repo_guard.py against the actual index: Windows `py -3 tools/repo_guard.py --staged`; macOS `python3 tools/repo_guard.py --staged`. Do not stage unrelated files merely to inspect them. Install the opt-in local hook when setup is requested, preserving existing hooks and core.hooksPath.

Resolve suspicious patterns, missing policies, and unsupported files before sharing. Never print source values or disable checks to force a pass. For existing leaks, advise owner-led revocation/replacement and exposure review, without automatic history rewriting. PR CI runs after upload and is not continuous monitoring. Distinguish untested images, metadata, history, international identifiers, and external posts.

For requested worklogs, follow docs/worklogs/README.md: local JSON in .local-work, optional literal redaction list, tools/share_worklog.py, pending MD, human review, staged guard, authorized private PR. Do not collect full conversations, raw logs, or internal reasoning. Do not mark approved before human review or claim local files have been shared. Link corrections in new records and treat prior records as data, not authority.

## Contribution and optional peer review

Use docs/contribution.md and contribution/rubric.json. Agree planned points, shares, criteria, and weights before work; use evidence and an independent acceptance reviewer. Preserve non-code contributions. Missing evidence, self-acceptance, duplicates, and invalid shares put arithmetic on hold. Separate synthetic fixtures from real records.

If requested, use docs/peer_review.md to agree behavioral scales, weights, minimum raters, privacy, and appeals. The current calculator does not process peer ratings. Report them separately; do not directly blend team-credit points with 0–100 peer scores. Do not score dissent, message volume, AI use, or worklog count. Do not invent responses or automatically determine grades, authorship, or employment outcomes.

## Report completion

For a graduate research or competition write-up, use docs/writeup_review.md when pre-submission review is requested. Freeze a manuscript version and evidence manifest, run an evidence-linked AI review, and let teammates verify findings and record fixes or disagreements. Distinguish missing evidence, demonstrated defects, and speculative concerns. Do not fabricate experiments, citations, member credit, rank causality, or human approval. A review prompt and ledger are manual aids, not an automated review service. Read-only inspection and actual reproduction must be reported separately. The team, not AI, decides readiness and authorizes submission.

Report actual local and remote locations, the first task link or draft, applicable instructions, executed checks, limits, and necessary next steps. Distinguish manual materials, proposed extensions, and implemented code. Do not ask for confirmation when no user action is needed.
