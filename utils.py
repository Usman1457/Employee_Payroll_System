from datetime import datetime


def current_date():
    return datetime.now().strftime("%Y-%m-%d")


def current_time():
    return datetime.now().strftime("%H:%M:%S")


def overtime_pay(hours):
    return hours * 500