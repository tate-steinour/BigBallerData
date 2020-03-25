SELECT t_name, ts_season, ts_3ptm
FROM team_stats
    JOIN team on t_id=ts_id
WHERE ts_wins >= 50
ORDER BY ts_3ptm DESC;
