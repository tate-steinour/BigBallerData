DROP TABLE IF EXISTS team_data;
CREATE TABLE team_data (
  t_id integer,  
  t_name text,
  t_season text,
  t_wins integer,
  t_losses integer,
  t_pts real,
  t_fgm real,
  t_3ptm real,
  t_ftm real,
  t_reb real,
  t_ast real,
  t_tov real,
  t_stl real,
  t_blck real,
  t_pf real,
  t_pfd real
  --PRIMARY KEY (t_id, t_season)
);
ALTER TABLE team_data OWNER TO jatt;
COMMENT ON TABLE team_data IS 'NBA team statistics';


DROP TABLE IF EXISTS team_info;
CREATE TABLE team_info (
  ti_id integer PRIMARY KEY,
  ti_name text,
  ti_location text
);
ALTER TABLE team_info OWNER TO jatt;
COMMENT ON TABLE team_info IS 'information about NBA teams';


DROP TABLE IF EXISTS player_info;
CREATE TABLE player_info (
  pi_id integer PRIMARY KEY,
  pi_name text,
  pi_position text,
  pi_yearStart integer,
  pi_yearEnd integer,
  pi_college text
);
ALTER TABLE player_info OWNER TO jatt;
COMMENT ON TABLE player_info IS 'personal information about NBA players';


DROP TABLE IF EXISTS player_data;
CREATE TABLE player_data (
  p_id integer,
  p_name text,
  p_teamid integer,
  p_season integer,
  p_pos text,
  p_pts integer,
  p_fg integer,
  p_3ptm integer,
  p_2ptm integer,
  p_ftm integer,
  p_reb integer,
  p_ast integer,
  p_tov integer,
  p_stl integer,
  p_blck integer
  --PRIMARY KEY (p_id, p_teamid, p_season)
);
ALTER TABLE player_data OWNER TO jatt;
COMMENT ON TABLE player_data IS 'NBA player statistics';


DROP TABLE IF EXISTS season;
CREATE TABLE season (
  s_year integer PRIMARY KEY
);
ALTER TABLE season OWNER TO jatt;
COMMENT ON TABLE season IS 'every season in the NBA starting at 2000';


