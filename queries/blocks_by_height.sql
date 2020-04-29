--Analyzes the relation between player height and average
--number of shots blocked from each season


DROP VIEW IF EXISTS blocks_by_height;
CREATE VIEW blocks_by_height AS
    SELECT DISTINCT ps_season, p_height, ROUND(AVG(p_weight), 2) AS wt, ROUND(AVG(ps_reb), 2) AS reb, ROUND(AVG(ps_blck), 2) AS blk
    FROM player_stats
        JOIN team_stats ON ps_teamid=ts_id
        JOIN team ON t_id=ts_id
        JOIN player ON ps_name=p_name
    WHERE ps_blck >= 1
	GROUP BY ps_season, p_height
    ORDER BY blk DESC, reb DESC;
ALTER VIEW blocks_by_height OWNER TO jatt;

--SELECT * FROM blocks_by_height;
