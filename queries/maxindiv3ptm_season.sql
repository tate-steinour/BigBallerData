SELECT DISTINCT t_name, ps_season, ps_name, ps_3ptm
FROM player_stats
	JOIN team_stats ON ps_teamid=ts_id
	JOIN team ON t_id=ts_id
WHERE ps_3ptm >= 150
ORDER BY ps_3ptm DESC;
