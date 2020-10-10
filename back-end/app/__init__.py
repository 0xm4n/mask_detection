from flask import Flask

def create_app():
    # init Flask application object
    app = Flask(__name__)
    app.config.from_object('app.settings')

    # init flask-login
    # from app.extensions.flasklogin import login_manager
    # login_manager.init_app(app)

    # init flask-sqlalchemy
    from app.models import db
    db.app = app # if without it, db query operation will throw exception in Form class
    db.init_app(app)

    # register all blueprints
    # from .handlers import session, oauth, detection, history
    from .handlers import oauth
    app.register_blueprint(oauth.bp, url_prefix='/oauth')
    # app.register_blueprint(session.bp, url_prefix='/session')
    # app.register_blueprint(account.bp, url_prefix='/account')

    return app