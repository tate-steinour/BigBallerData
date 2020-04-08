from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
import psycopg2

app = Flask(__name__)




@app.route('/')
def home():
    con = psycopg2.connect("host=localhost dbname=jatt user=jatt password=3T@R@9D@xcm_5+C+")
    return render_template('home.html')


