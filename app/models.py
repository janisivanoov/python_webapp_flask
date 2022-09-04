from datetime import datetime
from app import db

ROLE_ONE = 1
ROLE_TWO = 2
ROLE_THREE = 3

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    role = db.Column(db.SmallInteger)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer)
    body = db.Column(db.String(140))
    link = db.Column(db.String(150))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
