from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
import psycopg2

app = Flask(__name__)



@app.route('/')
def home():
    #con = psycopg2.connect("host=localhost dbname=jatt user=jatt password=3T@R@9D@xcm_5+C+")
    #cursor = con.cursor()
    return render_template('home.html')


@app.route('/Blocks_by_height')
def get_blocks():
    minHeight = request.args.get("minHeight", "")
    maxHeight = request.args.get("maxHeight", "")
    limit = request.args.get("limit", "")
    if not minHeight and not maxHeight:
        # default when no user input. (what GP3 showed)
        return render_template('default_blocks_by_height.html')
    else:
        con = psycopg2.connect(
            "host=localhost dbname=jatt user=jatt password=3T@R@9D@xcm_5+C+")
        cursor = con.cursor()
        sql = """
        SELECT DISTINCT t_name, ps_season, ps_name, ps_blck, p_height
        FROM player_stats
            JOIN team_stats ON ps_teamid=ts_id
            JOIN team ON t_id=ts_id
            JOIN player ON ps_name=p_name
        WHERE ps_blck >= 1
            AND p_height >= %s
            AND p_height <= %s
        ORDER BY ps_blck DESC
        LIMIT %s;
        """
        cursor.execute(sql, (minHeight, maxHeight, limit))
        queuryData = cursor.fetchall()
        return render_template('blocks_by_height.html', queuryData=queuryData)


@app.route('/three_ptm_wins')
def populate():

    sql = """
    SELECT t_name, ts_season, ts_3ptm, ts_wins
    FROM team_stats
        JOIN team on t_id=ts_id
    WHERE ts_wins >= %s
        AND ts_season > %s
		AND ts_season < %s
    ORDER BY ts_3ptm DESC
    LIMIT %s;
    """

    minWins = request.args.get("minWins", "")
    sStart = request.args.get("sStart", "")
    sEnd = request.args.get("sEnd", "")
    limit = request.args.get("limit", "")
    # set defaults
    if minWins == '':
        minWins = 50
    if sStart == '':
        sStart = '2000'
    if sEnd == '':
        sEnd = '2018'
    if limit == '':
        limit = 10
    con = psycopg2.connect(
        "host=localhost dbname=jatt user=jatt password=3T@R@9D@xcm_5+C+")
    cur = con.cursor()
    cur.execute(sql, (minWins, sStart, sEnd, limit))
    dat = cur.fetchall()
    return render_template("three_ptm_wins.html", dat=dat)


@app.route('/team_wins_over_seasons')
def wins_over_season():

    sql = """
    SELECT t_name, ts_season, ts_wins
    FROM team_stats
        JOIN team ON t_id=ts_id
    WHERE t_name= %s
    ORDER BY ts_season
    LIMIT %s;
    """

    teamName = request.args.get("teamName", "")
    limit = request.args.get("limit", "")
    # set defaulls
    if teamName == '':
        teamName = 'Philadelphia 76ers'
    if limit == '':
        limit = 10
    con = psycopg2.connect("host=localhost dbname=jatt user=jatt password=3T@R@9D@xcm_5+C+")
    cur = con.cursor()
    cur.execute(sql, (teamName, limit))
    dat = cur.fetchall()
    newdat = []
    for row in dat:
        newR = []
        newR.append(row[0])
        season = row[1]
        temp = season.split("-")
        newR.append(temp[0])
        #newR.append(temp[1])
        newR.append(row[2])
        newdat.append(newR)
    return render_template('team_wins_by_season.html', dat=newdat)
