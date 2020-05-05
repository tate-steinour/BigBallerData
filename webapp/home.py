from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

app.secret_key = 'jatt'

@app.route('/')
def home():
    tNBA = getTeams()
    tCol = getColleges()
    tCat = getCategories()
    return render_template('home.html', tNBA=tNBA, tCol=tCol, tCat=tCat)

def valid_year(year_str):
    y = int(year_str)
    return (y < 2018) and (y > 1999)

def getCursor():
    con = psycopg2.connect("host=localhost dbname=jatt user=jatt password=3T@R@9D@xcm_5+C+")
    return con.cursor()

def getTeams():
    list = []
    cursor = getCursor()
    sql = """
    SELECT DISTINCT t_name
    FROM team
    WHERE t_name IS NOT NULL
    ORDER BY t_name ASC;
    """
    cursor.execute(sql, ())
    queryData = cursor.fetchall()
    for row in queryData:
        list.append(row[0])
    return list

def getColleges():
    list = []
    cursor = getCursor()
    sql = """
    SELECT DISTINCT p_college 
    FROM player
    WHERE p_college IS NOT NULL
    ORDER BY p_college ASC;
    """
    cursor.execute(sql, ())
    queryData = cursor.fetchall()
    for row in queryData:
        list.append(row[0])
    return list

def getCategories():
    list = ['Points', 'Rebounds', 'Assists', 'Turnovers', 'Steals', '3-Pointers made', 'Free Throws made']
    return list


@app.route('/Blocks_by_height')
def get_blocks():
    season = request.args.get("season", "")
    season2 = request.args.get("season2", "")

    if(not season.isdigit() or not season2.isdigit()):
        flash('Please enter valid numerical inputs')
        return redirect('/')
    if(not valid_year(season) or not valid_year(season2)):
        flash('Please enter a valid season, between 2000 and 2017 inclusive')
        return redirect('/')

    cursor = getCursor()
    sql = """
    SELECT * 
    FROM blocks_by_height
    WHERE ps_season = %s
    OR ps_season = %s
    ORDER BY blk DESC, reb DESC;
    """
    cursor.execute(sql, (season,season2))
    queryData = cursor.fetchall()
    return render_template('blocks_by_height.html', queryData=queryData, season=season, season2=season2)


@app.route('/three_ptm_wins')
def populate():

    sql = """
    SELECT *
    FROM three_ptm_wins
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

    cur = getCursor()
    cur.execute(sql, (minWins, sStart, sEnd, limit))
    dat = cur.fetchall()
    return render_template("three_ptm_wins.html", dat=dat, minWins = minWins, sStart = sStart,
                                                sEnd = sEnd, limit = limit)


@app.route('/team_wins_over_seasons')
def wins_over_season():

    teamName = request.args.get("teamName", "")
    cat = request.args.get("category", "")

    # set defaults
    teamNameList = getTeams()
    if(not teamName in teamNameList):
        flash('Please enter a valid team name from the list')
        return redirect('/')

    if cat == 'Points':
        catQ = 'ts_pts'
    elif cat == 'Rebounds':
        catQ = 'ts_reb'
    elif cat == 'Assists':
        catQ = 'ts_ast'
    elif cat == 'Steals':
        catQ = 'ts_stl'
    elif cat == 'Turnovers':
        catQ = 'ts_tov'
    elif cat == 'Free Throws made':
        catQ = 'ts_ftm'
    elif cat == '3-Pointers made':
        catQ = 'ts_3ptm'
    else:
        flash('Please enter a valid statistical category from the list')
        return redirect('/')

    query = sql.SQL("""
    SELECT t_name, ts_season, ts_wins, {col}
    FROM team_wins_over_seasons
    WHERE t_name= %s
    ORDER BY ts_season;
    """).format(col=sql.Identifier(catQ))

    cur = getCursor()
    cur.execute(query, (teamName, ))
    dat = cur.fetchall()
    newdat = []
    for row in dat:
        newR = []
        newR.append(row[0])
        season = row[1]
        temp = season.split("-")
        newR.append(temp[0])
        newR.append(row[2])
        newR.append(row[3])
        newdat.append(newR)
        tNBA = getTeams()
        tCat = getCategories()
    return render_template('team_wins_by_season.html', tNBA=tNBA, dat=newdat, teamName=teamName, cat=cat, tCat=tCat)


@app.route('/max_individual_3ptm')
def get_indiv_3ptm():
    teamName = request.args.get("teamName","")
    season = request.args.get("season","")
    
    #set defaults
    if (not season.isdigit() or not valid_year(season)):
        flash('Please enter a valid season, between 2000 and 2017 inclusive')
        return redirect('/')

    teamNameList = getTeams()
    if(not teamName in teamNameList):
        flash('Please enter a valid team name from the list')
        return redirect('/')

    cursor = getCursor()
    sql = """
    SELECT *
    FROM max_individual_3ptm
    WHERE t_name = %s
        AND ps_season = %s
        AND ps_3ptm > 0
    ORDER BY ps_3ptm DESC;
    """
    cursor.execute(sql, (teamName, season))
    queryData = cursor.fetchall()
    tNBA = getTeams()
    return render_template('max_individual_3ptm.html',tNBA = tNBA, queryData = queryData, teamName=teamName, season=season)

@app.route('/players_by_college')
def players_by_college():

    sql = """
    SELECT COUNT(DISTINCT p_name), p_college, ps_season
    FROM players_by_college
    WHERE (p_college= %s
    OR p_college=%s)
    AND ps_season > 2006
    GROUP BY ps_season, p_college
    ORDER BY ps_season ASC;
    """

    college = request.args.get("college", "")
    college2 = request.args.get("college2", "")
    # set defaults
    collegeNameList = getColleges()
    if(not college in collegeNameList or not college2 in collegeNameList):
        flash('Please enter a valid college name from the list')
        return redirect('/')

    cur = getCursor()
    cur.execute(sql, (college, college2))
    dat = cur.fetchall()
    tCol = getColleges()
    return render_template("players_by_college.html", dat=dat, college=college, college2=college2, tCol=tCol)
