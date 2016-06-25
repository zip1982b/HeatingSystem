# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy




appFlask = Flask(__name__)  # создаём объект приложения (appFlask это экземпляр класса Flask)
appFlask.config.from_object('config')
db = SQLAlchemy(appFlask)



from app import views, models   # импортируем модуль представлений - это обработчики, которые отвечают на запросы веб-браузера
                                # (из папки app импортируем модуль views.py)
                                # Почему в конце импорт? чтобы избежать циклических ссылок
                                # (из папки app импортируем модуль models.py)
