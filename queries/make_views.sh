#!/bin/sh

# add environment variables to the path
export PGHOST=data.cs.jmu.edu
export PGDATABASE=jatt

#  psql commands
psql -h data.cs.jmu.edu jatt < three_ptm_wins.sql
psql -h data.cs.jmu.edu jatt < blocks_by_height.sql
psql -h data.cs.jmu.edu jatt < max_individual_3ptm.sql
psql -h data.cs.jmu.edu jatt < players_by_college.sql
psql -h data.cs.jmu.edu jatt < team_wins_over_seasons.sql
