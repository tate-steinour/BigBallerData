--Analyzes the relation between the number of points a team averages in a
--season and their win total

DROP VIEW IF EXISTS team_wins_over_seasons;
CREATE VIEW team_wins_over_seasons AS
    SELECT t_name, ts_season, ts_wins, ts_pts, ts_3ptm, ts_ftm, ts_reb, ts_ast, ts_tov, ts_stl
    FROM team_stats
        JOIN team ON t_id=ts_id
    ORDER BY ts_season;
ALTER VIEW team_wins_over_seasons OWNER TO jatt;

