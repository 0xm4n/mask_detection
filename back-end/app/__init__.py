from flask import Flask


def create_app():
    # Init Flask application object
    app = Flask(__name__)
    app.config.from_object('app.settings')

    # Init flask-login
    from .utils.login import login_manager
    login_manager.init_app(app)

    # Init flask-sqlalchemy
    from app.models import db
    db.app = app
    db.init_app(app)

    # Register all blueprints
    from .handlers import oauth
    app.register_blueprint(oauth.bp, url_prefix='/oauth')
    # app.register_blueprint(session.bp, url_prefix='/session')
    # app.register_blueprint(account.bp, url_prefix='/account')

    return app
