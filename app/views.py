# -*- coding: utf-8 -*-
"""
здесь будут представления - обработчики, которые отвечают на запросы веб-браузера
"""

# Подключение модулей
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import appFlask, db, models, lm, Thread, background_thread, socketio, emit, disconnect, thread  # из папки app импортируем экземпляр класса Flask
from forms import LoginForm, RegistrationForm
from models import User




def settingsSaveInDB(argSlider, argSet_time2, argSet_time1, argSelectDay):
    data = models.SettingsData.query.all()
    for u in data:
        print u.temperature, u.time1, u.time2, u.days_of_week


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
    print g.user # смотрел что представляет из себя g.user



@appFlask.route('/')
@appFlask.route('/index')
@login_required
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.daemon = True
        thread.start()
    user = g.user
    #print request - смотрел что представляет из себя request
    return render_template("index.html", title='Home', user=user)


# ************** Приём данных по web socket и их обработка***********************************************
# принимает сообщения в json формате {u'data': u'тут распологаются сами данные!'}
# 'server receives data' - название события - такое же название события на стороне клиента в колбеке
# namespace='/temperature_setting' - позволяют клиенту открыть несколько подключений к серверу,
# который мультиплексированы на одном сокете. Если пространство имен не указано
# события привязаны к глобальному пространству имен по умолчанию
#@socketio.on('server receives data', namespace='/temperature_setting')
#def settings(message):
 #   print(message)


@socketio.on('server receives data', namespace='/temperature_setting')
def data(json):
        if len(json)==4:
            #var1 = json
            settingsSaveInDB(json['slider1'], json['set_time2'], json['set_time1'], json['selectDay'])


        print('received json: ' + str(json))








# **********отправка сообщения клиенту (в его namespace - temperature_setting)что сервер подключен***************************************************
@socketio.on('connect', namespace='/temperature_setting')
def test_connect():
    emit('Server response', {'data': 'Server is Connected!', 'count': 0})
    print("Server is connected")





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
        print session, 'this is session' # смотрел что представляет из себя session
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


