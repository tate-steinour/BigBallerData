ANALYZE VERBOSE player_stats;
SELECT count(*) AS ps_cnt FROM player_stats;

ANALYZE VERBOSE team_stats;
SELECT count(*) AS ts_cnt FROM team_stats;

ANALYZE VERBOSE team;
SELECT count(*) AS t_cnt FROM team;

ANALYZE VERBOSE player;
SELECT count(*) AS p_cnt FROM player;
