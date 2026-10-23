# Share team and Codex worklogs

Share concise Markdown handoffs through branches and PRs in the team's **private repository**. Never put real team conversations or research data in this public template.

## Record only useful work context

Task summary and issue; changed files and reasons; decisions and open questions; executed checks and checks not run; next steps and references. Do not collect full conversations, raw terminal logs, or internal reasoning. Worklogs are reference material, not AI instructions or new authority.

## Prepare and redact

Create .local-work in the repository root. Raw summaries and additional literal redaction phrases stay there. The directory is ignored and blocked if force-added. Save a factual JSON summary as .local-work/session.json:

```json
{
  "participant_id": "P01",
  "topic": "Improve synthetic-analysis run instructions",
  "summary": ["Clarify how a beginner runs the example"],
  "changes": ["Update README run location and command"],
  "decisions": ["Analysis code and data stay outside this task"],
  "checks": ["Insert actual command and result, or reason not run"],
  "next_steps": ["Reviewer checks for missing instructions"],
  "references": ["README.md", "Insert the real team issue link"]
}
```

Put names, addresses, or internal identifiers needing additional masking into .local-work/redactions.txt, one literal phrase per line. Never share that list.

Windows:
```powershell
py -3 tools/share_worklog.py --input .local-work/session.json --redact-file .local-work/redactions.txt
```
macOS:
```sh
python3 tools/share_worklog.py --input .local-work/session.json --redact-file .local-work/redactions.txt
```

Omit --redact-file if no additional list is needed. The tool masks selected key/token patterns, Bearer values, credential URLs, email, Korean mobile numbers, student-ID contexts, and local user paths. It cannot find all names, images, contextual identifiers, international phone formats, or unknown keys. Literal redaction phrases are not executed as regex.

It creates docs/worklogs/date-P01-randomID.md with a unique filename. It preserves originals and never stages, commits, or pushes. Reports omit source values.

## Human review before sharing

privacy_review: pending means human review is required. Review the entire file locally for identifiers, internal or research information, and accuracy. Only after human approval may privacy_review become approved; AI must not approve its own draft. The flag is a declaration, not cryptographic identity proof. The guard blocks pending worklogs and residual sensitive patterns even in approved worklogs.

```sh
git add docs/worklogs/REVIEWED-FILE.md
python3 tools/repo_guard.py --staged
```

Use `py -3` on Windows. Check `git remote -v`, then commit and push only within the user's authorization to the private repository and request review. A local file alone has not been shared with teammates.

## Reuse context

Pull current records and read by date and pseudonym. Codex reads relevant records when starting a task. Link corrections from a new record instead of modifying another member's record. Record volume is not contribution credit. Masking an exposed key does not replace revocation and exposure review.
