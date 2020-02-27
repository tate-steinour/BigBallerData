--This is to transfer team data

INSERT INTO team_info(ti_id, ti_name)
SELECT t_id, t_name
FROM team_data
LIMIT 30;

ALTER TABLE team_data
DROP COLUMN t_name;

--This is to transfer season data

INSERT INTO season(s_year)
SELECT DISTINCT p_season
FROM player_data;

--This is to transfer player data
INSERT INTO player_info(pi_id, pi_name, pi_position)
SELECT p_id, p_name, p_pos
FROM player_data;

ALTER TABLE player_data
DROP COLUMN p_name, p_pos;
