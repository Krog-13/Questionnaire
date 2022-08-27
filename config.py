import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1/team'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DOSSIER_PER_PAGE = 4
    UPLOAD_FOLDER = os.path.join(basedir, 'app/templates/static')
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')