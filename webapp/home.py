from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
import psycopg2

app = Flask(__name__)

app.secret_key = 'jatt'

@app.route('/')
def home():
    #con = psycopg2.connect("host=localhost dbname=jatt user=jatt password=3T@R@9D@xcm_5+C+")
    #cursor = con.cursor()
    return render_template('home.html')

def valid_year(year_str):
    y = int(year_str)
    return (y < 2018) and (y > 1999)


@app.route('/Blocks_by_height')
def get_blocks():
    season = request.args.get("season", "")
    limit = request.args.get("limit", "")

    if not limit.isdigit() or int(limit) < 1:
        limit = 10
    if(not season.isdigit() or not limit.isdigit()):
        flash('Please enter valid numerical inputs')
        return redirect('/')
    if(not valid_year(season)):
        flash('Please enter a valid season, between 2000 and 2017 inclusive')
        return redirect('/')

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
    AND ps_season = %s
    ORDER BY ps_blck DESC
    LIMIT %s;
    """
    cursor.execute(sql, (season, limit))
    queryData = cursor.fetchall()
    return render_template('blocks_by_height.html', queryData=queryData, season = season, limit = limit)


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
    
    if not limit.isdigit() or int(limit) < 1:
        limit = 10
    if(not minWins.isdigit() or not sStart.isdigit() 
        or not sEnd.isdigit()):
        flash('Please enter valid numerical inputs')
        return redirect('/')
    if (not valid_year(sStart)) or (not valid_year(sEnd)):
        flash('Please enter valid seasons, between 2000 and 2017 inclusive')
        return redirect('/')
    if(int(minWins) < 0):
        flash('Please enter positive number for minWins')
        return redirect('/')

    con = psycopg2.connect(
        "host=localhost dbname=jatt user=jatt password=3T@R@9D@xcm_5+C+")
    cur = con.cursor()
    cur.execute(sql, (minWins, sStart, sEnd, limit))
    dat = cur.fetchall()
    return render_template("three_ptm_wins.html", dat=dat, minWins = minWins, sStart = sStart,
                                                sEnd = sEnd, limit = limit)


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
    if not limit.isdigit() or int(limit) < 1:
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
    return render_template('team_wins_by_season.html', dat=newdat, teamName=teamName, limit=limit)


@app.route('/max_individual_3ptm')
def get_indiv_3ptm():
    teamName = request.args.get("teamName","")
    season = request.args.get("season","")
    limit = request.args.get("limit", "")
    
    #set defaults
    if teamName == '':
        teamName == 'Golden State Warriors'

    if not limit.isdigit() or int(limit) < 1:
        limit = 10

    if (not season.isdigit() or not valid_year(season)):
        flash('Please enter a valid season, between 2000 and 2017 inclusive')
        return redirect('/')

    con = psycopg2.connect("host=localhost dbname=jatt user=jatt password=3T@R@9D@xcm_5+C+")
    cursor = con.cursor()
    sql = """
    SELECT DISTINCT t_name, ps_season, ps_name, ps_3ptm
    FROM player_stats
        JOIN team_stats ON ps_teamid=ts_id
        JOIN team ON t_id=ts_id
    WHERE t_name = %s
        AND ps_season = %s
    ORDER BY ps_3ptm DESC
    LIMIT %s;
    """
    cursor.execute(sql, (teamName, season, limit))
    queryData = cursor.fetchall()
    return render_template('max_individual_3ptm.html', queryData = queryData, teamName=teamName, season=season, limit=limit)

@app.route('/players_by_college')
def players_by_college():

    sql = """
    SELECT DISTINCT p_name, ps_games, ps_season, t_name
    FROM player
        JOIN player_stats ON p_name=ps_name
        JOIN team_stats ON ps_teamid=ts_id
        JOIN team ON ts_id=t_id
    WHERE p_college= %s
    ORDER BY ps_season DESC
    LIMIT %s;
    """

    college = request.args.get("college", "")
    limit = request.args.get("limit", "")
    # set defaults
    if college == '':
        college = 'Virginia Commonwealth University'
    if not limit.isdigit() or int(limit) < 1:
        limit = 10

    con = psycopg2.connect("host=localhost dbname=jatt user=jatt password=3T@R@9D@xcm_5+C+")
    cur = con.cursor()
    cur.execute(sql, (college, limit))
    dat = cur.fetchall()
    return render_template("players_by_college.html", dat=dat, college = college, limit = limit)
