from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from . import config
# from flask_uploads import UploadSet, configure_uploads, patch_request_class




app = Flask(__name__)
app.config.from_object(config) 

db = SQLAlchemy(app)
login_manager = LoginManager(app)

# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)
# patch_request_class(app, size=None)


from . import views, models, forms
