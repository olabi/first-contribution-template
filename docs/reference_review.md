# Review of GUAM collaboration documentation

Reviewed on 2026-10-23. Scope: documentation and workflow design, not a source-code or benchmark audit. No GUAM code, figures, benchmark data, personal contacts, or team-specific settings are copied into this template.

## Adopted and adapted

| Observed practice | Source | Adaptation here |
|---|---|---|
| Beginner guide separate from agent operating rules | WORKFLOW.md / AGENTS.md | docs/workflow.md explains the same process in plain English |
| GitHub documents plus Linear tickets | WORKFLOW.md | Versioned agreements in GitHub; current task communication and status in Linear |
| Dependencies and duplicate ownership checked before self-assignment | AGENTS.md | Beginner task-readiness checks and explicit blockers |
| Stable identifiers link work, paths, issues, and PRs | AGENTS.md / ISSUE-MAP.md | Lightweight docs/issue_map.md and consistent real issue IDs |
| Stable maps separated from live status and dated snapshots | AGENTS.md / ISSUE-MAP.md | One live tracker; static link map avoids stale duplicate status |
| Evidence includes environment, source version, and unexecuted checks | TEST-PLAN.md | PR and handoff fields distinguish actual checks from unavailable ones |

## Not adopted

GPU-residency restrictions, RAPIDS dependencies, class-per-issue sizing, team-specific owners, workspace IDs, deadlines, benchmark numbers, and extensive Epic structures are domain-specific. This starter retains small goal-based tasks, a lightweight agreement-first process, and no new mandatory runtime dependencies.

Peer-review rubrics and the agreement comparison prompt are our proposed additions, not features established by this GUAM review. Automatic comparisons and peer-score calculation are not implemented.

## Sources and provenance

- [GUAM README](https://github.com/ModulabsRAPIDSLAB/GUAM/blob/main/README.md)
- [Agent operating rules](https://github.com/ModulabsRAPIDSLAB/GUAM/blob/main/AGENTS.md), reviewed blob 977bd4f98140a721c11d64d7cf77185831f95e36
- [Beginner workflow](https://github.com/ModulabsRAPIDSLAB/GUAM/blob/main/docs/WORKFLOW.md), reviewed lines 1–150, blob 09696ed0c63f36efc4837f457138afe30fc85195
- [Issue map](https://github.com/ModulabsRAPIDSLAB/GUAM/blob/main/docs/ISSUE-MAP.md), reviewed blob 26100a0d9eedc3deb349ae23ca52e8addb2fd460
- [Test plan](https://github.com/ModulabsRAPIDSLAB/GUAM/blob/main/docs/TEST-PLAN.md), reviewed blob 7aaa735f70c59585d97dbd92f0497375b8f37439

GUAM is licensed under Apache-2.0. This document describes adapted workflow ideas in original wording; it does not relicense GUAM material under this template's MIT license.
