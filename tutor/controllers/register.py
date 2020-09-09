from flask import Flask, Response, render_template, request, redirect, url_for
from .forms import RegistrationForm, LoginForm
from .. import db, bcrypt
from .models import Users

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('get_course_info_route', id=1))
    return render_template('register.html', form=form)