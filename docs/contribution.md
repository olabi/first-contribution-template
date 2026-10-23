# Evidence-based contribution records

This is consistent arithmetic from a team's agreed records, not a fully objective measure of effort or ability. Do not automatically decide grades, authorship, rewards, or employment outcomes from it.

## Agree before work

Default category weights are deliverables 50, validation 20, peer-review activity 20, and coordination/documentation 10. Teams may adjust contribution/rubric.json before work; weights must total 100. Agree on roles and opportunities rather than imposing mechanically identical expectations.

For each activity, agree on a 1–5 planned-point value, scope, acceptance criteria, and joint credit shares. Record the plan reference and only then mark plan_approved yes. Record reasons and agreement for changes. Do not count commits, lines, generated code, speaking frequency, or worklog length.

Literature review and writing can be deliverables; reproducibility checks are validation; PR or research-design feedback is review; meeting decisions and scheduling can be coordination. Do not double-count the same work or split activities merely to increase points.

## Inputs and formula

- activities.csv: activity ID, category, planned points, status, agreement reference, criteria, evidence, reviewer, and criteria_passed.
- shares.csv: activity ID, pseudonymous participant ID, and agreed share; each activity totals exactly 1.
- rubric.json: category weights.

Participant category points = category weight × sum of accepted activity planned points × participant credit share / all planned points in that category.

Sum category points for the participant total. The team total reflects accepted work against the complete plan, up to 100. Credit composition divides participant points by the accepted team total. Unfinished work scores zero and does not redistribute its budget; unplanned categories are flagged.

Accepted activities need evidence, an independent reviewer, and criteria_passed=yes. A contributor to that activity cannot approve it. Missing evidence, duplicate IDs, invalid shares, or unagreed plans put calculation on hold.

## Review and privacy

The code checks inputs and arithmetic, not linked content, actual effort, or reviewer identity. Give each member a chance to identify missing contributions and challenge errors. Return disputed activities to in_progress until reviewed. Consider undocumented mentoring and coordination.

Keep real records in the private project with agreed access. Use P01-style pseudonyms; keep real-name mappings outside the repository. Separate synthetic fixtures before real use. The fixture produces P01=25, P02=35, P03=20, team=80, and credit composition 31.25%, 43.75%, 25%. This is not a ranking of people.

## Optional peer ratings and behavioral rubric

Teams may add [peer ratings](peer_review.md) when agreed before work. **Review activity credit** rewards a documented review task; **peer ratings** describe observed collaboration and are a separate instrument. The current calculator does not read or combine peer ratings. Report the two measures side by side by default. Specify scale, item weights, minimum raters, privacy, missing-data handling, and appeals before collection.
