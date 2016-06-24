# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


"""
DataRequired это класс, который может быть прикреплен к полю, для выполнения валидации данных отправленных пользователем.
Валидатор DataRequired просто проверяет, что поле не было отправлено пустым
"""


class LoginForm(Form):
    user = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class RegistrationForm(LoginForm):
    email = StringField('E-mail', validators=[Email(),DataRequired()])
    password_repeat = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])








