#!/bin/sh
echo COPY team_data FROM nba_team_stats_00_to_18_edited.csv
psql -c "\copy team_data FROM ../csv/nba_team_stats_00_to_18_edited.csv WITH CSV HEADER" jatt

echo COPY player_data FROM Seasons_Stats_edited_withID.csv
psql -c "\copy player_data FROM ../csv/Seasons_Stats_edited_withID.csv WITH CSV HEADER" jatt
