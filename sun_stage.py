__author__ = 'Umar Sear'

from astral import Astral
from datetime import date, datetime


def its_light_in(city_name):
    a = Astral()
    a.solar_depression = 'civil'
    city = a[city_name]
    sun = city.sun(date=date.today(), local=True)
    dawn_today = (sun['dawn']).replace(tzinfo=None)

    if dawn_today < datetime.today():
        return True
    else:
        return False


def its_dark_in(city_name):
    a = Astral()
    a.solar_depression = 'civil'
    city = a[city_name]
    sun = city.sun(date=date.today(), local=True)
    sunset_today = (sun['sunset']).replace(tzinfo=None)

    if sunset_today < datetime.today():
        return True
    else:
        return False


def its_between_dawn_sunset(city_name):
    a = Astral()
    a.solar_depression = 'civil'
    city = a[city_name]
    sun = city.sun(date=date.today(), local=True)
    dawn_today = (sun['dawn']).replace(tzinfo=None)
    sunset_today = (sun['sunset']).replace(tzinfo=None)
    if (dawn_today < datetime.today()) and (sunset_today > datetime.today()):
        return True
    else:
        return False


def its_after_sunset(city_name):
    a = Astral()
    a.solar_depression = 'civil'
    city = a[city_name]
    sun = city.sun(date=date.today(), local=True)
    sunset_today = (sun['sunset']).replace(tzinfo=None)
    if sunset_today < datetime.today():
        return True
    else:
        return False