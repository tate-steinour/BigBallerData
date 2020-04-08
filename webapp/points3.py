from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
import psycopg2

app = Flask(__name__)

sql = """
SELECT t_name, ts_season, ts_3ptm, ts_wins
	FROM team_stats
		JOIN team on t_id=ts_id
	WHERE ts_wins >= 50
	ORDER BY ts_3ptm DESC
"""

@app.route('/Points3')
def populate():
    data = None
    con = psycopg2.connect("host=localhost dbname=jatt user=jatt password=3T@R@9D@xcm_5+C+")
    cur = con.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    return render_template("three_ptm_wins.html",dat = data)


