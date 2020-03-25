#!/bin/sh
echo COPY team_stats FROM nba_team_stats_00_to_18_edited.csv
psql -c "\copy team_stats FROM ../csv/nba_team_stats_00_to_18_edited.csv WITH CSV HEADER" jatt

echo COPY player_stats FROM Seasons_Stats_edited_withID.csv
psql -c "\copy player_stats FROM ../csv/Seasons_Stats_edited_withID.csv WITH CSV HEADER" jatt

echo COPY player FROM player_data.csv
psql -c "\copy player FROM ../csv/player_data.csv WITH CSV HEADER" jatt
