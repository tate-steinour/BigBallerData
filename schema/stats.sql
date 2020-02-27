ANALYZE VERBOSE player_data;
SELECT count(*) AS pd_cnt FROM player_data;

ANALYZE VERBOSE team_data;
SELECT count(*) AS td_cnt FROM team_data;

ANALYZE VERBOSE season;
SELECT count(*) AS s_cnt FROM season;

ANALYZE VERBOSE team_info;
SELECT count(*) AS ti_cnt FROM team_info;

ANALYZE VERBOSE player_info;
SELECT count(*) AS pi_cnt FROM player_info;

