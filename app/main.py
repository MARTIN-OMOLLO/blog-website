from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
import os

# from app import app
from . import db
from .models import  Blog, Comment, Drop

main = Blueprint('main', __name__)


@main.route('/')
def index():
    blogs = Blog.query.all()
    return render_template('index.html', blogs=blogs)


@main.route('/profile')
@login_required
def profile():
    blogs = Blog.query.filter_by(author=current_user.id).all()
    return render_template('profile.html', username=current_user.username, blogs=blogs)


@main.route('/create_blog', methods=['GET', 'POST'])
@login_required
def create_blog():

    if request.method == 'POST':
        category = request.form.get('category')
        text = request.form.get('text')

        print(len(text))
        if len(text) > 255:
            flash('Pitch is too long. Max 255 characters.')
            return redirect(url_for('main.create_blog'))
        pitch = Pitch(text=text, category=category, author=current_user.id)

        db.session.add(create_blog)
        db.session.commit()

        return redirect(url_for('main.profile'))

    return render_template('create_pitch.html', user=current_user)


@main.route('/create-comment/<pitch_id>', methods=['POST'])
@login_required
def create_comment(pitch_id):
    comment = request.form.get('text')
    blog = Blog.query.filter_by(id=blog_id).first()

    if comment and blog:
        new_comment = Comment(text=comment, author=current_user.id,
                              blog_id=blog_id)
        db.session.add(new_comment)
        db.session.commit()

    return redirect(url_for('main.index'))


@main.route('/drop/<blog_id>', methods=['POST'])
@login_required
def drop(blog_id):
    blog = blog.query.filter_by(id=blog_id).first()

    # check if user has drpped the blog
    if current_user.id in [dropped.user_id for drop in blog.drop]:
        # remove the user's drop
        print('User has already dropped')
        drop = drop.query.filter_by(user_id=current_user.id).first()
        db.session.delete(drop)
        db.session.commit()
        return redirect(url_for('main.index'))
    else:
        # add the user's upvote
        drop = drop(user_id=current_user.id, blog_id=blog_id)
        db.session.add(drop)
        db.session.commit()
        return redirect(url_for('main.index'))


@main.route('/category/<category>')
def category(category):
    blogs = blog.query.filter_by(category=category).all()
    return render_template('category.html', blogs=blogs, category=category)