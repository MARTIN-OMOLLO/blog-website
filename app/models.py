from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager

class User(db.Model, UserMixin):
    _tablename_ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True, nullable = False)
    email  = db.Column(db.String(255), unique = True, index = True, nullable = False)
    secure_password = db.Column(db.String(300),nullable = False)
    bio = db.Column(db.String(300))
    profile_pic_path = db.Column(db.String())
    blogs = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='user',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='user',lazy='dynamic')
