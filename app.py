# Q & A app file

#imports
import os
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template  # render_template class to render HTML

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')
