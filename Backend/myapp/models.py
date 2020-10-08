from . import db
from . import login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, login_user, LoginManager
from datetime import datetime, timedelta


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    confirm = db.Column(db.Boolean, default=False)
    # addtime = db.Column(db.Datetime, index=True, default=datetime.now)

    photos = db.relationship('Photo', backref='User', lazy='dynamic')

    def set_password_hash(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password_hash(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return "<User %r>" % self.username


class Photo(db.Model):
    __tablename__='photos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    photo_name = db.Column(db.String(512), unique=True)
    output_name = db.Column(db.String(512), unique=True)
    nfaces = db.Column(db.Integer)
    nmasks = db.Column(db.Integer)
    
    # flag == 3 no faces
    # flag == 2 some with and some without masks
    # flag == 1 all with masks
    # flag == 0 all without masks
    photo_type = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return "<Photo %r>" % self.id


