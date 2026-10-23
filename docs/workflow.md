# Beginner workflow

## Two spaces with different jobs

**Linear is the team's communication and task-coordination space.** Ask questions, leave feedback, mention a teammate, and discuss blockers in the relevant issue. **GitHub stores versioned deliverables and agreements**, with changes reviewed in PRs. Link the approved document version from the Linear issue; summarize a decision in the agreement rather than relying only on a long comment thread.

| Question | Source of truth |
|---|---|
| What did we agree to build? | Confirmed agreement version in GitHub |
| Who owns the task and what blocks it now? | Linear issue (or GitHub Issues if that is your chosen tracker) |
| What changed and what was checked? | PR, evidence, and reviewed worklog |
| How do stable task IDs map to documents and PRs? | docs/issue_map.md |

## Before dividing work

Each member answers the questions in team_agreement.md independently. ChatGPT Edu compares interpretations with sentence IDs. Members correct the comparison, settle questions, and confirm the agreement. Unresolved requirements remain open. Do not convert an AI suggestion into an approved requirement.

## Choose one ready task

Check dependencies and the current owner. `Blocked by` names a prerequisite; `Blocks` identifies work waiting on this task. Do not duplicate an in-progress task. A proposed owner is not an accepted assignment. Record a clear deliverable, out-of-scope work, acceptance criteria, reviewer, and evidence location.

Suggested status flow: Backlog → Todo → In Progress → In Review → Done. Teams may use their own statuses. A merge does not itself prove research validity or agreement approval.

## Implement, review, and hand over

Work on one agreed branch. Check the actual index before an authorized commit and push. Link the issue, agreement version, and evidence in the PR. Share a human-reviewed redacted worklog. When requirements change, record the impact and reconfirm the agreement before affected work continues.

Integration is optional and separately configured. Using Linear from a Codex conversation and invoking @Codex in Linear are different connections; the latter is not required for this beginner workflow.

Official reference: [Linear comments](https://linear.app/docs/comment-on-issues) and [Inbox notifications](https://linear.app/docs/inbox).
