from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True, nullable = False)
    email  = db.Column(db.String(280), unique = True, index = True, nullable = False)
    secure_password = db.Column(db.String(300),nullable = False)
    bio = db.Column(db.String(350))
    profile_pic_path = db.Column(db.String())
    blogs = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    drop = db.relationship('Drop',backref='user',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='user',lazy='dynamic')

    def is_active(self):
        return True
    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password,password) 
    
    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def _repr_(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250),nullable = False)
    post = db.Column(db.Text(), nullable = False)
    comment = db.relationship('Comment',backref='blog',lazy='dynamic')
    downvote = db.relationship('Drop',backref='blog',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category = db.Column(db.String(100), index = True,nullable = False)

    def save_p(self):
        db.session.add(self)
        db.session.commit()

        
    def _repr_(self):
        return f'Blog {self.post}'


class Drop(db.Model):
    __tablename__ = 'drops'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_drops(cls,id):
        drop = Drop.query.filter_by(blog_id=id).all()
        return drop


    def _repr_(self):
        return f'{self.user_id}:{self.blog_id}'
class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    

    def save(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_downvotes(cls,id):
        downvote = Downvote.query.filter_by(blog_id=id).all()
        return downvote

    def _repr_(self):
        return f'{self.user_id}:{self.blog_id}'

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'),nullable = False)

    def save_c(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,blog_id):
        comments = Comment.query.filter_by(blog_id=blog_id).all()

        return comments

    
    # def _repr_(self):
    #     return f"comment:{self.comment}

    
