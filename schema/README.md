## Data Sources
The original data used to populate our player information can be found here:  
https://www.kaggle.com/drgilermo/nba-players-stats#Seasons_Stats.csv

The data used to populate our team information can be found here:  
https://www.kaggle.com/mharvnek/nba-team-stats-00-to-18

Note: The CSVs are slightly modified from their source to better align with our schema and allow for easy copying.

## Creating the Database
To create the database:

1. Ensure that a Postgres database has been created at the desired location (e.g using the command "createdb jatt").

2. Ensure that the modified CSVs from Kaggle listed above are located the working directory.

3. To create the initial schema, run the "create.sql" file like so:

    ```
    $ psql -h data.cs.jmu.edu jatt < create.sql
    ```

4. After the schema has been created, run "copy.sh" to copy the CSV data into the database:
    ```
    $ ./copy.sh
    ```

5. To verify that the copy has completed successfully, run the following command with the newly generated "stats.sql" file:

    ```
    $ psql -h data.cs.jmu.edu jatt < stats.sql
    ```

6. To enforce the primary and foreign key constraints on the database, run the following command:

    ```
    $ psql -h data.cs.jmu.edu jatt < alter.sql
    ```

7. To help speed up queries, run the index SQL script:

    ```
    $ psql -h data.cs.jmu.edu jatt < index.sql
    ```



