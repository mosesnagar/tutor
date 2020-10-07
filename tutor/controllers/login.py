from flask import render_template, redirect, url_for, flash
from .forms import LoginForm
from .. import bcrypt
from flask_login import login_user, current_user
from ..routes import course # noqa
from ..models.users import Users


def login():
    if current_user.is_authenticated:
        flash('You are already logged in.', 'success')
        return redirect(url_for('courses_route'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Welcome, {0}'.format(user.username), 'success')
            return redirect(url_for('courses_route'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', form=form)
