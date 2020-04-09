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
    season = request.args.get("season", "")
    limit = request.args.get("limit", "")
    if not season:
        return render_template('default_blocks_by_height.html') #default when no user input. (what GP3 showed)
    else:
        con = psycopg2.connect("host=localhost dbname=jatt user=jatt password=3T@R@9D@xcm_5+C+")
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
        queuryData = cursor.fetchall()
        return render_template('blocks_by_height.html', queuryData = queuryData)

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

    minWins = request.args.get("minWins","")
    sStart = request.args.get("sStart","")
    sEnd   = request.args.get("sEnd","")
    limit  = request.args.get("limit","")
    # set defaults
    if minWins == '':
        minWins = 50
    if sStart == '':
        sStart = '2000'
    if sEnd == '':
        sEnd = '2018'
    if limit == '':
        limit = 10
    con = psycopg2.connect("host=localhost dbname=jatt user=jatt password=3T@R@9D@xcm_5+C+")
    cur = con.cursor()
    cur.execute(sql, (minWins,sStart,sEnd,limit))
    dat = cur.fetchall()
    return render_template("three_ptm_wins.html",dat = dat)