# Q & A app file

# imports
import os
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template  # render_template class to render HTML
from flask import request
from database import db
from flask import redirect, url_for  # to redirect and use 'url_for' function
from models import User as User
from models import Question as Question
from models import Answer as Answer

app = Flask(__name__)
# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///group23.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)

# Setup models
with app.app_context():
    db.create_all()  # run under the app context


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/questions")
def get_questions():
    my_questions = db.session.query(Question).all()

    return render_template('questions.html', questions=my_questions)

# View individual question
@app.route("/questions/<question_id>")
def get_question(question_id):
    my_question = db.session.query(Question).filter_by(id=question_id).one()

    return render_template('question.html', question=my_question)


@app.route('/questions/new', methods=['GET', 'POST'])
def new_question():
    # check request method
    if request.method == 'POST':
        # get data needed
        title = request.form['title']
        details = request.form['details']
        # date
        from datetime import date
        today = date.today()
        today = today.strftime("%m-%d-%Y")
        upvote = 0
        downvote = 0
        PIN = 0
        new_record = Question(title, details, today, upvote, downvote, PIN)
        db.session.add(new_record)
        db.session.commit()

        return redirect(url_for('get_questions'))
    else:
        return render_template('new.html')

