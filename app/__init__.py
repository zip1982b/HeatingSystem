# -*- coding: utf-8 -*-
import os


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.login import LoginManager
from config import basedir





appFlask = Flask(__name__)  # создаём объект приложения (appFlask это экземпляр класса Flask)
appFlask.config.from_object('config')
db = SQLAlchemy(appFlask)

lm = LoginManager()     # создаём экземпляр класса LoginManager()
lm.init_app(appFlask)   # Когда приложение (appFlask) полностью сконфигурировано, необходимо передать его в lm
lm.login_view = 'login'


from app import views, models   # view - импортируем модуль представлений - это обработчики, которые отвечают на запросы веб-браузера
                                # (из папки app импортируем модуль views.py)
                                # Почему в конце импорт? чтобы избежать циклических ссылок
                                # models - (из папки app импортируем модуль models.py)
