# -*- coding: utf-8 -*-
import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')  # Это путь к файлу с нашей базой данных
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')  # это папка, где мы будем хранить файлы SQLAlchemy-migrate






