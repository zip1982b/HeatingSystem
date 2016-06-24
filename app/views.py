# -*- coding: utf-8 -*-
"""
здесь будут представления - обработчики, которые отвечают на запросы веб-браузера
"""
from flask import render_template, flash, redirect
from app import appFlask  # из папки app импортируем экземпляр класса Flask
from forms import LoginForm, RegistrationForm



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
    if form.validate_on_submit():
        flash('User="' + form.user.data + '", email="' + form.email.data + '", password="' + form.password.data + '", repeat pass="' + form.password_repeat.data)
        return redirect('/login')
    return render_template('registration.html', title = 'Sign In', form = form)





