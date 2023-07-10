from flask import Flask
import sqlite3

app = Flask(__name__)
db = sqlite3.connect(orchestrion_collect/demo.db)

@app.route("/")
def hello_world():
    
    return "<p>Hello, World!</p>"