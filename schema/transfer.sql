--This is to transfer data from one table to another

INSERT INTO team_info(ti_id, ti_name)
SELECT t_id, t_name
FROM team_data
LIMIT 30;

ALTER TABLE team_data
DROP COLUMN t_name;

