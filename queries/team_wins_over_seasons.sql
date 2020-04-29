--Analyzes the relation between the number of points a team averages in a
--season and their win total, in this instance we analyze the 76ers

DROP VIEW IF EXISTS team_wins_over_seasons;
CREATE VIEW team_wins_over_seasons AS
    SELECT t_name, ts_season, ts_wins
    FROM team_stats
        JOIN team ON t_id=ts_id
    ORDER BY ts_season;
ALTER VIEW team_wins_over_seasons OWNER TO jatt;

--SELECT * FROM philly_team_pts;
