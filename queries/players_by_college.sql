--Able to see how many games were played in the NBA by players
--from specific colleges

DROP VIEW IF EXISTS players_by_college;
CREATE VIEW players_by_college AS
    SELECT DISTINCT p_name, ps_games, ps_season, t_name
    FROM player
        JOIN player_stats ON p_name=ps_name
        JOIN team_stats ON ps_teamid=ts_id
        JOIN team ON ts_id=t_id
    WHERE p_college='Virginia Commonwealth University'
    ORDER BY ps_season DESC
    LIMIT 10;
ALTER VIEW players_by_college OWNER TO jatt;

--SELECT * FROM players_by_college;
