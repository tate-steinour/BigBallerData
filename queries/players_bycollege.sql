CREATE VIEW players_by_college AS
    SELECT DISTINCT p_name, ps_games, ps_season, t_name
    FROM player
        JOIN player_stats ON p_name=ps_name
        JOIN team_stats ON ps_teamid=ts_id
        JOIN team ON ts_id=t_id
    WHERE p_college='Virginia Commonwealth University'
    ORDER BY ps_season DESC;

SELECT * FROM players_by_college;
