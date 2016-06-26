# -*- coding: utf-8 -*-
"""
здесь будут представления - обработчики, которые отвечают на запросы веб-браузера
"""
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import appFlask, db, models, lm   # из папки app импортируем экземпляр класса Flask
from forms import LoginForm, RegistrationForm
from models import User





@appFlask.route('/')
@appFlask.route('/index')
def index():
    user = { 'nickname': 'Zhan' } # выдуманный пользователь
    return render_template("index.html", title='Home', user=user)




@appFlask.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('User="' + form.user.data + '", password="' + form.password.data + '" remember_me=' + str(form.remember_me.data))
        return redirect('/index')
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
    return render_template('registration.html', title = 'Sign In', form = form)





