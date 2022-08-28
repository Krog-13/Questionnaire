import os
from os import environ, path
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# user = os.environ['POSTGRES_USER']
# password = os.environ['POSTGRES_PASSWORD']
# host = os.environ['POSTGRES_HOST']
# database = os.environ['POSTGRES_DB']
# port = os.environ['POSTGRES_PORT']
# Database config
user = environ.get('POSTGRES_USER')
password = environ.get('POSTGRES_PASSWORD')
host = environ.get('POSTGRES_HOST')
port = environ.get('POSTGRES_PORT')
database = environ.get('POSTGRES_DB')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DOSSIER_PER_PAGE = 4
    UPLOAD_FOLDER = os.path.join(basedir, 'app/templates/static')
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')