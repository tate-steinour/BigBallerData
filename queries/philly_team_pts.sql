--Analyzes the relation between the number of points a team averages in a
--season and their win total, in this instance we analyze the 76ers

DROP VIEW IF EXISTS philly_team_pts;
CREATE VIEW philly_team_pts AS
    SELECT t_name, ts_season, ts_wins
    FROM team_stats
        JOIN team ON t_id=ts_id
    WHERE t_name='Philadelphia 76ers'
    ORDER BY ts_season;
ALTER VIEW philly_team_pts OWNER TO jatt;

--SELECT * FROM philly_team_pts;
