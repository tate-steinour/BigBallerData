#!/bin/sh

echo COPY team_info FROM jatt
psql -c "COPY (
	SELECT ti_id, ti_name, ti_location
	FROM team_info
	) TO STDOUT;" jatt | \
	psql -c "COPY team_info FROM STDIN;" jatt

echo COPY team_data FROM csv
psql -c "\copy team_data FROM nba_team_stats_00_to_18_edited.csv WITH CSV HEADER" jatt

echo COPY player_data FROM csv
psql -c "\copy player_data FROM Seasons_Stats_edited.csv WITH CSV HEADER" jatt
