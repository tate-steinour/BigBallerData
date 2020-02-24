#!/bin/sh

echo COPY team_info FROM jatt
psql -c "COPY (
	SELECT ti_id, ti_name, ti_location
	FROM team_info
      ) TO STDOUT;" jatt | \
      psql -c "COPY team_info FROM STDIN;" jatt

echo COPY nba_teams FROM csv
psql -c "\copy nba_teams FROM nba_teams_stats_00_to_18_edited.csv WITH CSV HEADER" jatt
