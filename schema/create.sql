DROP TABLE IF EXISTS team_data;
CREATE TABLE team_stats (
  ts_id integer,
  ts_season text,
  ts_wins integer,
  ts_losses integer,
  ts_pts real,
  ts_fgm real,
  ts_3ptm real,
  ts_ftm real,
  ts_reb real,
  ts_ast real,
  ts_tov real,
  ts_stl real,
  ts_blck real,
  ts_pf real,
  ts_pfd real
  --PRIMARY KEY (t_id, t_season)
);
ALTER TABLE team_stats OWNER TO jatt;
COMMENT ON TABLE team_data IS 'NBA team statistics';


DROP TABLE IF EXISTS team_info;
CREATE TABLE team (
  t_id integer PRIMARY KEY,
  t_name text
);
ALTER TABLE team OWNER TO jatt;
COMMENT ON TABLE team_info IS 'information about NBA teams';


DROP TABLE IF EXISTS player_info;
CREATE TABLE player (
  p_id integer PRIMARY KEY,
  p_name text,
  p_position text,
  p_yearStart integer,
  p_yearEnd integer,
  p_college text
);
ALTER TABLE player OWNER TO jatt;
COMMENT ON TABLE player_info IS 'personal information about NBA players';


DROP TABLE IF EXISTS player_data;
CREATE TABLE player_stats (
  ps_id integer,
  ps_teamid integer,
  ps_season integer,
  ps_pts integer,
  ps_fg integer,
  ps_3ptm integer,
  ps_2ptm integer,
  ps_ftm integer,
  ps_reb integer,
  ps_ast integer,
  ps_tov integer,
  ps_stl integer,
  ps_blck integer
  --PRIMARY KEY (p_id, p_teamid, p_season)
);
ALTER TABLE player_stats OWNER TO jatt;
COMMENT ON TABLE player_data IS 'NBA player statistics';

DROP TABLE IF EXISTS season;
