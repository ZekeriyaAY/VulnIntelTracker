from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True,
                         unique=True, nullable=False)
    role = db.Column(db.String(64), index=True)
    email = db.Column(
        db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))  # hash: fixed length string
    member_since = db.Column(db.DateTime, default=datetime.utcnow)
    last_seen = db.Column(db.DateTime)
    last_password_change = db.Column(db.DateTime)

    def __repr__(self):
        return '<User {}>'.format(self.username)  # for debugging

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        self.last_password_change = datetime.utcnow()

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
