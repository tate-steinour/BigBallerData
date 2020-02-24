# Jatt

## About
Jatt is an interactive database utility designed to bring users the latest sports statistics.

## Data Sources
The data used to populate our player information can be found here:
https://www.kaggle.com/drgilermo/nba-players-stats#Seasons_Stats.csv

The data used to populate our team information can be found here:
https://www.kaggle.com/mharvnek/nba-team-stats-00-to-18

## Creating the Database
To create the database:

1. Ensure that a Postgres database has been created at the desired location (e.g using the command "createdb jatt").

2. Ensure that the CSVs from Kaggle listed above are located the working directory (they should be included in the repository by default).

3. To create the initial schema, run the "create.sql" file like so:

    $ psql -h data.cs.jmu.edu jatt < create.sql

4. After the schema has been created, run "copy.sh" to generate the copy instructions for Postgres:

    $ ./copy.sh

5. To copy the data into the database, run the following command with the newly generated "stats.sql" file:

    $ psql -h data.cs.jmu.edu jatt < stats.sql

6. To enforce the primary and foreign key constraints on the database, run the following command:

    $ psql -h data.cs.jmu.edu jatt < alter.sql

7. To help speed up queries, run the index SQL script:

    $ psql -h data.cs.jmu.edu jatt < index.sql



