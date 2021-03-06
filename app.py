# Q & A app file

# imports
import os
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template  # render_template class to render HTML
from flask import request
from database import db
from werkzeug.utils import secure_filename
from flask import redirect, url_for, flash  # to redirect and use 'url_for' function
from flask import session
from models import User as User
from models import Question as Question
from models import Reply as Reply
from forms import RegisterForm, LoginForm, ReplyForm
import bcrypt
from base64 import b64encode

app = Flask(__name__)
# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///group23.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'QWQW001032IJ'

#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)

# Setup models
with app.app_context():
    db.create_all()  # run under the app context


# Homepage reached with / or /index
@app.route("/")
@app.route("/index")
def index():
    if session.get('user'):
        return render_template('index.html', user=session['user'])
    return render_template("index.html")


# View all questions
@app.route("/questions")
def get_questions():
    if session.get('user'):
        my_questions = db.session.query(Question).all()
        return render_template('questions.html', questions=my_questions, user=session['user'],
                               user_id=session['user_id'])
    else:
        return redirect(url_for('login'))


# View individual question
@app.route("/questions/<question_id>")
def get_question(question_id):
    if session.get('user'):
        my_question = db.session.query(Question).filter_by(id=question_id).one()

        form = ReplyForm()
        image = b64encode(my_question.image).decode("utf-8")

        return render_template('question.html', question=my_question, image=image, user=session['user'], form=form)
    else:
        return redirect(url_for('login'))


# Create a new question
@app.route('/questions/new', methods=['GET', 'POST'])
def new_question():
    if session.get('user'):
        # check request method
        if request.method == 'POST':
            # get data needed
            title = request.form['title']
            details = request.form['details']
            # date
            from datetime import date
            today = date.today()
            today = today.strftime("%m-%d-%Y")
            file_name = request.files['image']
            new_record = Question(title, details, today, file_name.read(), 0, 0, 0, session['user_id'])
            db.session.add(new_record)
            db.session.commit()

            return redirect(url_for('get_questions'))
        else:
            return render_template('new.html', user=session['user'])
    else:
        return redirect(url_for('login'))


# Edit a question from database
@app.route('/questions/edit/<question_id>', methods=['GET', 'POST'])
def edit_question(question_id):
    # check method for post
    if request.method == 'POST':
        # get title data
        title = request.form['title']
        # get details of question
        details = request.form['details']
        question = db.session.query(Question).filter_by(id=question_id).one()
        # update question
        question.title = title
        question.details = details
        # update in DB
        db.session.add(question)
        db.session.commit()

        return redirect(url_for('get_questions'))
    else:
        # GET request - show form to edit question
        my_question = db.session.query(Question).filter_by(id=question_id).one()

        return render_template('new.html', question=my_question)


# Delete a question from database
@app.route('/questions/delete/<question_id>', methods=['POST'])
def delete_question(question_id):
    my_question = db.session.query(Question).filter_by(id=question_id).one()
    db.session.delete(my_question)
    db.session.commit()

    return redirect(url_for('get_questions'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        # salt and hash password
        h_password = bcrypt.hashpw(
            request.form['password'].encode('utf-8'), bcrypt.gensalt())
        # get entered user data
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        # create user model
        new_user = User(first_name, last_name, request.form['email'], h_password,)
        # add user to database and commit
        db.session.add(new_user)
        db.session.commit()
        # save the user's name to the session
        session['user'] = first_name
        session['user_id'] = new_user.id  # access id value from user model of this newly added user
        # show user dashboard view
        return redirect(url_for('get_questions'))

    # something went wrong - display register view
    return render_template('register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    # validate_on_submit only validates using POST
    if login_form.validate_on_submit():
        # we know user exists. We can use one()
        the_user = db.session.query(User).filter_by(email=request.form['email']).one()
        # user exists check password entered matches stored password
        if bcrypt.checkpw(request.form['password'].encode('utf-8'), the_user.password):
            # password match add user info to session
            session['user'] = the_user.first_name
            session['user_id'] = the_user.id
            # render view
            return redirect(url_for('get_questions'))

        # password check failed
        # set error message to alert user
        login_form.password.errors = ["Incorrect username or password."]
        return render_template("login.html", form=login_form)
    else:
        # form did not validate or GET request
        return render_template("login.html", form=login_form)


@app.route('/questions/<question_id>/reply', methods=['POST'])
def new_reply(question_id):
    if session.get('user'):
        reply_form = ReplyForm()
        if reply_form.validate_on_submit():
            reply_details = request.form['reply']
            reply = Reply(reply_details, int(question_id), 0, 0, 0, session['user_id'])
            db.session.add(reply)
            db.session.commit()

        return redirect(url_for('get_question', question_id=question_id))

    else:
        return redirect(url_for('login'))


@app.route('/questions/<question_id>/upvote', methods=['POST'])
def upvote(question_id):
    if request.method == 'POST':
        # add +1 to current upvote
        question = db.session.query(Question).filter_by(id=question_id).one()
        question.upvote = question.upvote + 1
        db.session.add(question)
        db.session.commit()

        return str(question.upvote)
    else:
        return redirect(url_for('index'))


@app.route('/questions/<question_id>/downvote', methods=['POST'])
def downvote(question_id):
    if request.method == 'POST':
        # -1 to downvote
        question = db.session.query(Question).filter_by(id=question_id).one()
        question.upvote = question.upvote - 1
        question.downvote = question.downvote + 1
        db.session.add(question)
        db.session.commit()

        return str(question.upvote)
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    # check if a user is saved in session
    if session.get('user'):
        session.clear()

    return redirect(url_for('index'))


@app.route('/user')
def profile():
    if session.get('user'):
        return render_template('profile.html', user=session['user'])
    else:
        return redirect(url_for('login'))


