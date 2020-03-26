DROP VIEW IF EXISTS philly_team_pts;
CREATE VIEW philly_team_pts AS
    SELECT t_name, ts_season, ts_wins
    FROM team_stats
        JOIN team ON t_id=ts_id
    WHERE t_name='Philadelphia 76ers'
    ORDER BY ts_season;

SELECT * FROM philly_team_pts;
