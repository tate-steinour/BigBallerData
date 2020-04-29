--Analyzes the relation between the top shotblockers from each season
--and their heights

DROP VIEW IF EXISTS blocks_by_height;
CREATE VIEW blocks_by_height AS
    SELECT DISTINCT t_name, ps_season, ps_name, ps_blck, p_height
    FROM player_stats
        JOIN team_stats ON ps_teamid=ts_id
        JOIN team ON t_id=ts_id
        JOIN player ON ps_name=p_name
    WHERE ps_blck >= 1
    ORDER BY ps_blck DESC
ALTER VIEW blocks_by_height OWNER TO jatt;

--SELECT * FROM blocks_by_height;
