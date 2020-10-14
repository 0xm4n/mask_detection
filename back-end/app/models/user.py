import datetime
from . import db

from sqlalchemy import Column
from sqlalchemy import SmallInteger, Integer, String
from sqlalchemy import DateTime

from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ = 'md_user'

    ROLE_ADMIN = 1
    ROLE_USER = 0

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True)
    password = Column(db.String(255))

    role = Column(SmallInteger, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.Integer, nullable=False, default=1)

    def __init__(self, id, username, email, password, role, status):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.status = status

    def check_password(self, raw):
        if not self.password:
            return False
        return check_password_hash(self.password, raw)

    def update_password(self, new_password):
        self.password = generate_password_hash(new_password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.status

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username
