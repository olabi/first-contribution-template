# Sharing checks and exposure response

## Instructions plus code

AGENTS.md guides AI behavior. `tools/repo_guard.py` independently inspects Git-index blobs. Reading an instruction is not proof that mistakes were prevented.

Run `python3 tools/repo_guard.py --staged` for changed index entries or `--tracked` for all tracked index entries. On Windows, use `py -3`. Git and Python must be available.

## Connect the checks

- Run `tools/install_guard_hook.py` once per clone. Existing hooks and core.hooksPath are preserved; installation stops instead of overwriting them.
- Personal-data patterns block the commit until reviewed and resolved, including false positives. This teaching template is intentionally strict.
- `.github/workflows/repository-guard.yml` demonstrates a tracked-file check for PRs. Verify Actions actually runs in the new repository.
- Administrators configure the `Repository guard / guard` required check and trusted review of policy, checker, and workflow changes, subject to plan support.
- Hooks are bypassable, and CI can be changed in the same PR. A required check name alone does not prevent tampering. Review policy changes and consider trusted checker distribution for operational use.

## Coverage and limits

Checks cover selected token shapes, credential assignments, email addresses, Korean mobile-number patterns, student-ID contexts, sensitive filenames, and required policies. International phone numbers and organization-specific identifiers are not generally covered. Use a local redaction list and human review for additional identifiers.

Files above 2 MB, binaries, unsupported extensions, symlinks, submodules, and conflicts stop the check. Logs omit raw content. File numbers follow the sorted checked-file list; locate files locally with `git diff --cached --name-only --diff-filter=ACMR` or `git ls-files`.

Images, document metadata, past commits, PR descriptions, and Linear posts are not automatically checked. Save proposed external text locally and use tools/share_check.py before posting. No continuous monitoring or outbound interception is implemented.

## If exposure is suspected

Stop sharing. If already exposed, have the owner revoke and replace the credential and inspect comments, logs, PRs, and commits. Do not repeat the value. Minimize unnecessary personal information in a separate redacted copy and review it again.

`.gitignore` does not erase history. Coordinate history rewriting with an administrator. Automatic masking does not modify originals or history. A pattern-free result still needs human review.

## Team worklogs

Raw summaries and additional redaction lists stay in .local-work. This directory and .private are blocked even if force-added. tools/share_worklog.py creates a pending-review MD draft without uploading it. Only after human review may privacy_review become approved. Approved records with residual patterns still block. The flag is a review declaration, not verified human identity. Keep actual worklogs in the team's private repository.

## Peer-review privacy

Agree on access and retention before collecting individual ratings. Do not publish personal ratings, real-name mappings, or sensitive feedback in the public template or unrestricted issue comments. Pseudonyms do not guarantee anonymity in a small team.
