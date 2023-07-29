from app import app, db
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from .user.login import LoginForm
from .user.register import RegistrationForm
from .user.password_change import PasswordChangeForm
from .user.models import User
from datetime import datetime


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:  # from flask_login import current_user
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(
            username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!', 'error')
            return redirect(url_for('login'))
        login_user(user)  # from flask_login import login_user
        next_page = request.args.get('next')  # from flask import request
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        flash('Welcome back, {}! I remember you from somewhere...'.format(
            user.username), 'success')
        user.last_seen = datetime.utcnow()
        db.session.commit()
        return redirect(next_page)  # from flask import redirect
    return render_template('user/login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out. Now you are alone in the wild...', 'success')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations! You are now registered to the dark side!', 'success')
        return redirect(url_for('login'))
    return render_template('user/register.html', form=form)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = User.query.filter_by(username=current_user.username).first_or_404()

    form = PasswordChangeForm()
    if form.validate_on_submit():
        user.set_password(form.new_password.data)
        db.session.commit()
        flash('Your password has been changed.', 'success')
        return redirect(url_for('profile'))

    return render_template('user/profile.html', user=user, form=form)
