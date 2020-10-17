# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from . import config

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

login_manager = LoginManager(app)

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#

from . import views





# from flask_uploads import UploadSet, configure_uploads, patch_request_class
# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)
# patch_request_class(app, size=None)
from . import models, forms
