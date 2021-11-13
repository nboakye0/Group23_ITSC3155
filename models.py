from database import db

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(200))

class Question(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(200))
    details = db.Column("details", db.String(700))
    date = db.Column("date", db.String(100))
    upvote = db.Column("upvote", db.Integer)
    downvote = db.Column("downvote", db.Integer)
    PIN = db.Column("pin", db.Integer)   # for boolean 0 or 1

    def __init__(self, title, details, date, upvote, downvote, PIN):
        self.title = title;
        self.details = details;
        self.date = date;
        self.upvote = upvote;
        self.downvote = downvote;
        self.PIN = PIN;

class Answer(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    text = db.Column("text", db.String(700))
    date = db.Column("date", db.String(100))
    upvote = db.Column("upvote", db.Integer)
    downvote = db.Column("downvote", db.Integer)
    PIN = db.Column("pin", db.Integer)   # for boolean 0 or 1
