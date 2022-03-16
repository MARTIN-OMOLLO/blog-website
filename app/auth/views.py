from flask import render_template,redirect,url_for, flash,request
from . import auth
from ..models import User
from .form import LoginForm,RegistrationForm
from .. import db
from ..email import mail_message
from flask_login import login_user,logout_user,login_required
# from ..email import mail_message
@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(url_for('main.index'))
        flash('Invalid username or Password')
    title = "blog login"
    return render_template('login.html',login_form = login_form,title=title)
@auth.route('/signup',methods = ["GET","POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        # mail_message("Welcome to My Personal Blog Site","email/welcome",user.email,user=user)
        return redirect(url_for('auth.login'))
    return render_template('signup.html',form = form)
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for("main.index"))