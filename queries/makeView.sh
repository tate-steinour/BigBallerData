#!/bin/sh

# add environment variables to the path
export PGHOST=data.cs.jmu.edu
export PGDATABASE=jatt

#  psql commands
psql -h data.cs.jmu.edu jatt < 3ptm_wins.sql
psql -h data.cs.jmu.edu jatt < blocksbyheight.sql
psql -h data.cs.jmu.edu jatt < maxindiv3ptm_season.sql
psql -h data.cs.jmu.edu jatt < players_bycollege.sql
psql -h data.cs.jmu.edu jatt < philly_team_pts.sql
