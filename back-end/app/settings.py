import os

SECRET_KEY = os.urandom(32)

# Database Config
DIALECT = 'mysql'
DRIVER = 'pymysql'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'password'
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
DATABASE = 'mask'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
    DIALECT, DRIVER, MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, DATABASE
)

SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_MAX_OVERFLOW = 5

# setting up email server variables
MAIL_SERVER = 'smtp.live.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'ece1779@hotmail.com'
MAIL_PASSWORD = '2Pk\Ce$e[52SzSt5'
ADMINS = ['ece1779@hotmail.com']
