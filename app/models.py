# -*- coding: utf-8 -*-
#*********Модель базы данных******************
from app import db

""" class User это название таблицы в базе app.db
    id, nickname, email - это наши записи в таблице user"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(255))
    settings_data = db.relationship('SettingsData', backref='author', lazy='dynamic')


    @property
    def is_authenticated(self):
        return True


    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3



    def __repr__(self):
        return '<User %r>' % (self.nickname)



class SettingsData(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    temperature = db.Column(db.REAL)
    time1 = db.Column(db.String)
    time2 = db.Column(db.String)
    days_of_week = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<SettingsData %r>' % (self.temperature)















    