# -*- coding: utf-8 -*-
import os
import eventlet
eventlet.monkey_patch()

import time
from threading import Thread



from flask import Flask, session, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit, disconnect
from flask.ext.login import LoginManager
from config import basedir








appFlask = Flask(__name__)  # создаём объект приложения (appFlask это экземпляр класса Flask)




appFlask.config.from_object('config')
db = SQLAlchemy(appFlask)

socketio = SocketIO(appFlask, async_mode='eventlet')
thread = None

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        time.sleep(10)
        count += 1
        socketio.emit('Server response',
                      {'data': 'Server generated event and send to client', 'count': count},
                      namespace='/temperature_setting')













lm = LoginManager()     # создаём экземпляр класса LoginManager()
lm.init_app(appFlask)   # Когда приложение (appFlask) полностью сконфигурировано, необходимо передать его в lm
lm.login_view = 'login'


from app import views, models   # view - импортируем модуль представлений - это обработчики, которые отвечают на запросы веб-браузера
                                # (из папки app импортируем модуль views.py)
                                # Почему в конце импорт? чтобы избежать циклических ссылок
                                # models - (из папки app импортируем модуль models.py)
print appFlask.url_map