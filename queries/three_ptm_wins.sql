--Observes the number of 3 pointers made by the top teams
--from each season 

DROP VIEW IF EXISTS three_ptm_wins;
CREATE VIEW three_ptm_wins AS
    SELECT t_name, ts_season, ts_3ptm, ts_wins
    FROM team_stats
        JOIN team on t_id=ts_id
    ORDER BY ts_3ptm DESC
ALTER VIEW three_ptm_wins OWNER TO jatt;
--SELECT * FROM three_ptm_wins;
