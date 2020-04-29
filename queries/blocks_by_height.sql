--Analyzes the relation between player height and average
--number of shots blocked from each season


DROP VIEW IF EXISTS blocks_by_height;
CREATE VIEW blocks_by_height AS
    SELECT DISTINCT ps_season, p_height, ROUND(AVG(ps_blck), 2)
    FROM player_stats
        JOIN team_stats ON ps_teamid=ts_id
        JOIN team ON t_id=ts_id
        JOIN player ON ps_name=p_name
    WHERE ps_blck >= 1
    GROUP BY ps_season, p_height
    ORDER BY ROUND DESC;
ALTER VIEW blocks_by_height OWNER TO jatt;

--SELECT * FROM blocks_by_height;
