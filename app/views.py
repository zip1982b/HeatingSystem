# -*- coding: utf-8 -*-
"""
здесь будут представления - обработчики, которые отвечают на запросы веб-браузера
"""
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import appFlask, db, models, lm   # из папки app импортируем экземпляр класса Flask
from forms import LoginForm, RegistrationForm
from models import User




# Чтобы найти объект User уже авторизованного пользователя, при его последующих запросах исходя из ID который хранится в его сессии.
# Поиск пользователя в базе данных по его ID
# вернёт None, если ID не существует
# вернёт объект User, если пользователь с таким ID существует
@lm.user_loader
def load_user(id):
    #print models.User.query.get(int(id))
    return models.User.query.get(int(id))

# ID который хранится в его сессии.
@appFlask.before_request
def before_request():
    g.user = current_user



@appFlask.route('/')
@appFlask.route('/index')
@login_required
def index():
    user = g.user
    return render_template("index.html", title='Home', user=user)







def get_user(arg_login, arg_pwd):
    users = models.User.query.all()
    for u in users:
        if arg_login == u.nickname and arg_pwd == u.password:
            return u
    else:
        return None











@appFlask.route('/login', methods = ['GET', 'POST'])
def login():
    # авторизированный пользователь
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # не авторизированнный пользователь
    if form.validate_on_submit() and request.method == "POST":
        session['remember_me'] = form.remember_me.data
        user = get_user(form.user.data, form.password.data)
        if user:
            login_user(user)
            return redirect(url_for("index"))
    return render_template('login.html', title = 'Sign In', form = form)


@appFlask.route('/registration', methods = ['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        u = models.User(nickname=form.user.data, email=form.email.data, password=form.password.data)
        db.session.add(u)
        flash('Thanks for registering')
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registration.html', title = 'Registr', form = form)



@appFlask.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


