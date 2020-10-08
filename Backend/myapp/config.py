import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# Flask-SQLAlchemy
# mysql
DIALECT = 'mysql'
DRIVE = 'pymysql'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'password'
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_DATABASE = 'flaskapp'
# SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(
#     DIALECT, DRIVE, MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE
#     )
### SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/flaskapp"

# sqlite
SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False


# Static Assets
UPLOAD_FOLDER = "./myapp/static/uploads/"
# SECRET_KEY = os.urandom(24)
SECRET_KEY = 'A SECRET KEY'
PERMANTENT_SESSION_LIFETIME = timedelta(hours=24)
MAX_CONTENT_LENGTH = 4 * 8 * 1024 * 1024  # 2MB
ALLOWED_EXTENSIONS = set(['jpg', 'JPG', 'jpeg', 'JPEG', 'png', 'PNG', 'bmp', 'BMP'])