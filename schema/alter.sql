ALTER TABLE team_stats ADD FOREIGN KEY (ts_id) REFERENCES team (t_id);

ALTER TABLE player_stats ADD FOREIGN KEY (ps_teamid) REFERENCES team_stats (ts_id);

ALTER TABLE player_stats ADD FOREIGN KEY (ps_season) REFERENCES team_stats (ts_season);

ALTER TABLE player_stats ADD FOREIGN KEY (ps_id) REFERENCES player (p_id);
