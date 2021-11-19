from database import db
import datetime

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column("first_name", db.String(100))
    last_name = db.Column("last_name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    questions = db.relationship("Question", backref="user", lazy=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.registered_on = datetime.date.today()

class Question(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    details = db.Column("details", db.String(700))
    date = db.Column("date", db.String(100))
    upvote = db.Column("upvote", db.Integer)
    downvote = db.Column("downvote", db.Integer)
    PIN = db.Column("pin", db.Integer)   # for boolean 0 or 1
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, title, details, date, upvote, downvote, PIN, user_id):
        self.title = title
        self.details = details
        self.date = date
        self.upvote = upvote
        self.downvote = downvote
        self.PIN = PIN
        self.user_id = user_id

class Answer(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    text = db.Column("text", db.String(700))
    date = db.Column("date", db.String(100))
    upvote = db.Column("upvote", db.Integer)
    downvote = db.Column("downvote", db.Integer)
    PIN = db.Column("pin", db.Integer)   # for boolean 0 or 1
