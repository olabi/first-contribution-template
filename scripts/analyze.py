import csv
from pathlib import Path
from statistics import mean

path = Path(__file__).resolve().parents[1] / 'data' / 'synthetic.csv'
with path.open(encoding='utf-8') as handle:
    rows = list(csv.DictReader(handle))
print(f'rows={len(rows)}')
print('mean_study_hours=%.2f' % mean(float(r['study_hours']) for r in rows))
print('mean_quiz_score=%.2f' % mean(float(r['quiz_score']) for r in rows))
