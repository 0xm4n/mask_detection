from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    # Init Flask application object
    app = Flask(__name__)
    app.config.from_object('app.settings')

    # Init flask-login
    from .utils.login import login_manager
    login_manager.init_app(app)

    # Init flask-mail
    from .utils.mail import mail
    mail.init_app(app)

    # Init flask-sqlalchemy
    db.app = app
    db.init_app(app)
    db.create_all()

    # Register all blueprints
    from .handlers import oauth, admin, detection, api
    app.register_blueprint(oauth.bp, url_prefix='/oauth')
    app.register_blueprint(admin.bp, url_prefix='/admin')
<<<<<<< HEAD
    app.register_blueprint(detection.bp, url_prefix='/detection')
=======
    app.register_blueprint(detection.bp, url_prefix='')
    app.register_blueprint(api.bp, url_prefix='/api')
>>>>>>> 934d401e039331e9110335046f057f49da03aa91

    return app
