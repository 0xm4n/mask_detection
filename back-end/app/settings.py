import os
from datetime import timedelta


SECRET_KEY = os.urandom(32)

# SQLite Database Config
APP_PATH = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + APP_PATH + '/models/sqlite.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# setting up email server variables
MAIL_SERVER = 'smtp.live.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'ece1779@hotmail.com'
MAIL_PASSWORD = '2Pk\Ce$e[52SzSt5'
ADMINS = ['ece1779@hotmail.com']


# MySQL Database Config
# DIALECT = 'mysql'
# DRIVER = 'pymysql'
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = 'password'
# MYSQL_HOST = 'localhost'
# MYSQL_PORT = '3306'
# DATABASE = 'mask'
# SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
#     DIALECT, DRIVER, MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, DATABASE
# )


PERMANTENT_SESSION_LIFETIME = timedelta(hours=24)
MAX_CONTENT_LENGTH = 4 * 8 * 1024 * 1024  # 2MB
ALLOWED_EXTENSIONS = set(['jpg', 'JPG', 'jpeg', 'JPEG', 'png', 'PNG', 'bmp', 'BMP'])

UPLOAD_FOLDER = "./app/static/uploads/"