# Clinical Trial Data Monitoring & Query Tracker

> **Portfolio demonstration | Synthetic / fictional data only**

An educational clinical trial data management pipeline that assesses synthetic participant visits, data queries, and adverse-event reporting completeness.

## What this demonstrates
- Monitor planned versus completed research visits
- Surface missing visit and adverse event fields
- Export trial data quality monitoring summary and SQL examples

## Quick start
```bash
python src/main.py
python -m unittest discover -s tests
```

Python 3.10+ is recommended. Core functionality uses the Python standard library; no API keys or patient records are required. Run commands from the repository root.

## Repository contents
- `data/`: fictional study visits and adverse events
- `src/main.py`: monitoring report
- `sql/study_metrics.sql`: SQL reporting examples

## Relevant skills
Clinical data management, EDC concepts, data quality, Python, SQL, GCP awareness

## Data and privacy
All records, facilities, identifiers, events and organizations in this repository are fabricated for demonstrations. This is **not** a production clinical system and does not contain real protected health information (PHI). Do not upload real patient data or confidential employer files. Outputs do not substitute for clinical, privacy, security, or regulatory review.



