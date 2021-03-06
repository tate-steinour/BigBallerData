#!/bin/sh

# add environment variables to the path
export PGHOST=data.cs.jmu.edu
export PGDATABASE=jatt

#  psql commands
psql -h data.cs.jmu.edu jatt < create.sql
./copy.sh
psql -h data.cs.jmu.edu jatt < transfer.sql
psql -h data.cs.jmu.edu jatt < stats.sql
psql -h data.cs.jmu.edu jatt < alter.sql
psql -h data.cs.jmu.edu jatt < index.sql
