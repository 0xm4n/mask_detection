from flask_login import LoginManager

from app.models.user import User

login_manager = LoginManager()

login_manager.login_view = "oauth.login"


@login_manager.user_loader
def load_user(id):
    try:
        user = User.query.get(id)
    except Exception as e:
        user = None
    return user
