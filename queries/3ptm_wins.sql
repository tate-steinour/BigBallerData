DROP VIEW IF EXISTS three_ptm_wins;
CREATE VIEW three_ptm_wins AS
    SELECT t_name, ts_season, ts_3ptm
    FROM team_stats
        JOIN team on t_id=ts_id
    WHERE ts_wins >= 50
    ORDER BY ts_3ptm DESC;
    LIMIT 10;
SELECT * FROM three_ptm_wins;
