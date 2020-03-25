DROP VIEW IF EXISTS team_pts_wins;
CREATE VIEW team_pts_wins AS
    SELECT t_name, ts_season, ts_wins, ts_pts
    FROM team_stats
        JOIN team ON t_id=ts_id
    WHERE t_name='Philadelphia 76ers'
    ORDER BY ts_season;

SELECT * FROM team_pts_wins;
