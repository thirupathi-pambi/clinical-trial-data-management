-- Import visits.csv as visits before running (SQLite-compatible).
SELECT COUNT(DISTINCT participant_id) AS participants,
 COUNT(*) AS planned_visits,
 SUM(CASE WHEN completed_date <> '' THEN 1 ELSE 0 END) AS completed_visits,
 ROUND(100.0*SUM(CASE WHEN completed_date <> '' THEN 1 ELSE 0 END)/NULLIF(COUNT(*),0),1) AS completion_pct
FROM visits;
