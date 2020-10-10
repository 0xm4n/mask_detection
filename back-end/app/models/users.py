import datetime

from . import db

from sqlalchemy import Column
from sqlalchemy import SmallInteger, Integer, String
from sqlalchemy import DateTime

from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ = 'mk_user'

    ROLE_ADMIN = 8
    ROLE_VERIFIED = 4
    ROLE_SPAMMER = -9
    ROLE_ACTIVE = 1

    id = Column(Integer, primary_key=True)
    username = Column(String(24), unique=True)
    email = Column(db.String(255), unique=True)
    _password = Column('password', String(100))

    role = Column(SmallInteger, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)