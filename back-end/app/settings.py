import os

from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.urandom(32)

# SQLite Database Config
APP_PATH = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + APP_PATH + '/models/sqlite.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# setting up email server variables
MAIL_SERVER = 'smtp.live.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
ADMINS = ['ece1779@hotmail.com']