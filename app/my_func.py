# -*- coding: utf-8 -*-
# В Этом модуле будут мои функции
from app import models

week_day={1:'monday', 2:'tuesday', 3:'wednesday', 4:'thursday', 5:'friday', 6:'saturday', 7:'sunday'}

def selectSettings(argSelectDay):
    d = models.SettingsData.query.filter_by(days_of_week=argSelectDay).all()
    for set in d:
        print set.id, set.temperature, set.time1, set.time2, set.days_of_week







