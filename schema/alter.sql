ALTER TABLE team_data ADD FOREIGN KEY (t_id) REFERENCES team_info (ti_id);

ALTER TABLE season ADD FOREIGN KEY (s_year) REFERENCES team_data (t_season);

ALTER TABLE player_data ADD FOREIGN KEY (p_teamid) REFERENCES team_data (t_id);

ALTER TABLE player_data ADD FOREIGN KEY (p_season) REFERENCES season (s_year);

ALTER TABLE player_info ADD FOREIGN KEY (pi_id) REFERENCES player_data (p_id);
