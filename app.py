from flask import Flask, make_response, render_template
from flask import request
import sqlite3
import datetime

app = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('demo.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    allrolls = conn.execute('SELECT * FROM RollName WHERE length(NameEn)>0 ORDER BY RollId').fetchall()
    conn.close()
    return render_template('index.html', rolls=allrolls)

@app.route('/set_cookie')
def set_cookie():
    response = make_response ('Hello World')
    outdate = datetime.datetime.today() + datetime.timedelta(days=30)
    response.set_cookie('Name', 'Hyman', expires = outdate)
    return response

@app.route('/get_cookie')
def get_cookie():
    name = request.cookies.get('Name')
    return name