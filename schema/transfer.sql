--This is to transfer team stats

INSERT INTO team(t_id, t_name)
SELECT ts_id, ts_name
FROM team_stats
LIMIT 30;

ALTER TABLE team_stats
DROP COLUMN ts_name;