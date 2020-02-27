--This is to transfer data from one table to another

INSERT INTO team_info
SELECT DISTINCT t_id
FROM team_data;

INSERT INTO team_info
SELECT DISTINCT t_name
FROM team_data;

ALTER TABLE team_data
DROP COLUMN t_name;

