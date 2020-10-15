from flask import Flask
from flask_mail import Mail

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
    from app.models import db
    db.app = app
    db.init_app(app)

    # Register all blueprints
    from .handlers import oauth, admin, detection
    app.register_blueprint(oauth.bp, url_prefix='/oauth')
    app.register_blueprint(admin.bp, url_prefix='/admin')
    app.register_blueprint(detection.bp, url_prefix='')

    return app
