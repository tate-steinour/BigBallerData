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
            AND p_height >= %s
            AND p_height <= %s 
        ORDER BY ps_blck DESC
        LIMIT %s;
        """
        cursor.execute(sql, (minHeight, maxHeight, limit))
        queuryData = cursor.fetchall()
        return render_template('blocks_by_height.html', queuryData = queuryData)