# Q & A app file

#imports
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Start</h1>"
