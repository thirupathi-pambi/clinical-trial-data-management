import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def monitor(visits, events):
    visits=list(visits);events=list(events)
    completed=sum(bool(r['completed_date']) for r in visits)
    issues=[]
    for r in visits:
        if not r['completed_date']:issues.append({'type':'missing_visit_completion','record':r['participant_id']+':'+r['visit_name']})
    for e in events:
        for field in ('term','severity','reported_date','outcome'):
            if not e[field]:issues.append({'type':'missing_ae_'+field,'record':e['ae_id']})
    return {'participants':len({v['participant_id'] for v in visits}), 'planned_visits':len(visits),
            'completed_visits':completed,'completion_rate_pct':round(100*completed/len(visits),1) if visits else 0,
            'adverse_events':len(events),'queries':issues}

def main():
    with (ROOT/'data/visits.csv').open() as f:visits=list(csv.DictReader(f))
    with (ROOT/'data/adverse_events.csv').open() as f:events=list(csv.DictReader(f))
    report=monitor(visits,events);out=ROOT/'output/study_monitoring.json';out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
