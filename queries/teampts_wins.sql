CREATE VIEW team_pts_wins AS
    SELECT t_name, ts_season, ts_wins, ts_pts
    FROM team_stats
        JOIN team ON t_id=ts_id
    WHERE t_name='Philadelphia 76ers'
    ORDER BY ts_wins DESC;

SELECT * FROM team_pts_wins;
