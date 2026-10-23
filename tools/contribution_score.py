"""Reproducible reference score from team-approved task records, not Git activity counts."""
import argparse
import csv
import json
import re
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path

def load_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def compute(tasks, shares, weights):
    categories = {'deliverable', 'validation', 'review', 'coordination'}
    if set(weights) != categories or any(type(v) is not int or v < 0 for v in weights.values()) or sum(weights.values()) != 100:
        raise ValueError('invalid_weights')
    indexed = {}
    for task in tasks:
        tid = task['activity_id']
        points = Decimal(task['planned_points'])
        if not re.fullmatch(r'[A-Z][A-Z0-9-]{0,31}', tid) or tid in indexed or task['category'] not in categories or points != points.to_integral_value() or not 1 <= points <= 5:
            raise ValueError('invalid_or_duplicate_activity')
        if task['plan_approved'] != 'yes' or not task['plan_ref'] or not task['criteria']:
            raise ValueError('plan_not_agreed')
        if task['status'] not in {'planned', 'in_progress', 'accepted'}:
            raise ValueError('invalid_status')
        if task['status'] == 'accepted' and (not task['evidence_ref'] or not re.fullmatch(r'P\d{2,6}',task['reviewer_id']) or task['criteria_passed'] != 'yes'):
            raise ValueError('missing_acceptance_evidence')
        indexed[tid] = (task, points)
    credits, people = {}, set()
    for row in shares:
        tid, pid = row['activity_id'], row['participant_id']
        value = Decimal(row['share'])
        if tid not in indexed or not re.fullmatch(r'P\d{2,6}',pid) or not value.is_finite() or not 0 < value <= 1 or (tid, pid) in credits:
            raise ValueError('invalid_or_duplicate_share')
        if indexed[tid][0]['status'] == 'accepted' and indexed[tid][0]['reviewer_id'] == pid:
            raise ValueError('self_acceptance_not_allowed')
        credits[tid, pid] = value
        people.add(pid)
    for tid in indexed:
        if sum((v for (activity, _), v in credits.items() if activity == tid), Decimal(0)) != 1:
            raise ValueError('shares_must_sum_to_one')
    planned = {c:sum((p for t,p in indexed.values() if t['category']==c),Decimal(0)) for c in categories}
    totals = {pid:Decimal(0) for pid in people}
    breakdown = {pid:{} for pid in people}
    evidence = {pid:[] for pid in people}
    for pid in sorted(people):
        for category in sorted(categories):
            units = sum((points*credits.get((tid,pid),Decimal(0)) for tid,(task,points) in indexed.items() if task['category']==category and task['status']=='accepted'),Decimal(0))
            points = Decimal(weights[category])*units/planned[category] if planned[category] else Decimal(0)
            totals[pid] += points
            breakdown[pid][category] = float(points.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
        evidence[pid] = sorted(tid for (tid, person),v in credits.items() if person==pid and indexed[tid][0]['status']=='accepted')
    total = sum(totals.values(),Decimal(0))
    return {'status':'calculated', 'rubric_version':'1.0', 'weights':weights,
        'team_accepted_points_of_100':float(total.quantize(Decimal('.01'))),
        'unplanned_categories':sorted(c for c in categories if not planned[c]),
        'participants':[{'participant_id':pid, 'accepted_points_of_100':float(totals[pid].quantize(Decimal('.01'))),
            'share_of_accepted_credit_percent':float((100*totals[pid]/total).quantize(Decimal('.01'))) if total else None,
            'category_points':breakdown[pid], 'accepted_activity_ids':evidence[pid]} for pid in sorted(people)],
        'notice':'Reference metric only. Plans, evidence and approvals are human-entered and not independently verified. Not a grade or authorship decision.'}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--data-dir',default='contribution')
    p.add_argument('--output',help='New JSON output file; existing files are not overwritten.')
    args=p.parse_args()
    try:
        folder=Path(args.data_dir)
        weights=json.loads((folder/'rubric.json').read_text(encoding='utf-8'))['weights']
        report=compute(load_csv(folder/'activities.csv'),load_csv(folder/'shares.csv'),weights)
        payload=json.dumps(report,ensure_ascii=False,indent=2)
        if args.output:
            with Path(args.output).open('x',encoding='utf-8') as f:f.write(payload+'\n')
        else:
            print(payload)
        return 0
    except (OSError,KeyError,ValueError,InvalidOperation,TypeError):
        print(json.dumps({'status':'HOLD','reason':'input_or_evidence_needs_review','notice':'No raw input values printed.'}))
        return 2

if __name__=='__main__':
    raise SystemExit(main())
