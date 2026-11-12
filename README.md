# Clinical Trial Data Monitoring & Query Tracker

This is a small data-cleaning check I wrote for a made-up clinical study. It's the kind of check a data manager runs before a monitoring visit: which visits never got completed, and which adverse event records are missing information. Each problem it finds becomes a "query" that someone at the site would have to go back and resolve.

All participants, dates and events here are fictional. There's no real patient data in this repo.

## What it checks

I used two CSV files:

- `data/visits.csv` has one row per scheduled visit (Screening, Week 4) for each participant, with the scheduled date and the completed date.
- `data/adverse_events.csv` has one row per adverse event, with the term, severity, reported date and outcome.

`src/main.py` loads both files and:

- counts participants, planned visits and completed visits
- calculates the visit completion rate
- raises a query for any visit with no completed date
- raises a query for any AE that's missing its term, severity, reported date or outcome

The report prints to the screen and is saved to `output/study_monitoring.json`.

## Running it

You need Python 3.10 or newer. There's nothing to install.

```bash
python src/main.py
python -m unittest discover -s tests
```

Run both commands from the repo root.

## What the sample data shows

There are 3 participants and 6 planned visits. 5 of those visits are completed, which is an 83.3% completion rate. The script raises 3 queries:

| Query                    | Record        | Issue                              |
|--------------------------|---------------|------------------------------------|
| missing_visit_completion | SUB002:Week 4 | Visit scheduled but never completed |
| missing_ae_reported_date | AE02          | Nausea logged with no reported date |
| missing_ae_severity      | AE03          | Dizziness logged with no severity   |

The two AE gaps matter most. If you don't know an event's severity, you can't tell whether it needs expedited reporting.

## SQL version

`sql/study_metrics.sql` calculates the same visit numbers in SQL (SQLite syntax). I wanted to confirm the Python and SQL results matched, and they do: 3 participants, 6 planned visits, 5 completed, 83.3%. Import `visits.csv` as a table called `visits`, then run the file.

## Some decisions I made

- **Every gap is its own query.** If one AE is missing two fields, that's two queries, not one. That's how query tracking works at a site, since each field gets resolved separately.
- **Each query shows its record ID.** For visits that's `participant:visit`, so the person reading the report knows exactly where to look without searching through the CSV.
- **An empty study doesn't crash.** With zero visits, the completion rate comes out as 0 instead of a divide-by-zero error. There's a unit test for this.

## Files

```
data/visits.csv            scheduled and completed visits
data/adverse_events.csv    adverse event log
src/main.py                monitoring report and query logic
sql/study_metrics.sql      same visit metrics in SQL
tests/test_main.py         unit tests
output/                    generated report (created on run)
```

## What I'd add next

- Visit window checks. `scheduled_date` is already in the data, so I could flag visits completed outside a ±3-day window. SUB001's Week 4 visit came a day late, for example.
- A query status (open, answered, closed) so queries can be tracked over time
- An AE severity grade check against a fixed list of allowed values
- A per-site breakdown once there's more than one site
