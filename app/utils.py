import datetime


def get_age(date):
    """return age of person"""
    return datetime.datetime.today().year - date.year

