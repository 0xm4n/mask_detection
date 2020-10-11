import datetime
from . import db

from sqlalchemy import Column
from sqlalchemy import SmallInteger, Integer, String
from sqlalchemy import DateTime

from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ = 'md_user'

    ROLE_ADMIN = 8
    ROLE_VERIFIED = 4
    ROLE_SPAMMER = -9
    ROLE_ACTIVE = 1

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(255), unique=True)
    _password = Column('password', String(100))

    role = Column(SmallInteger, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    @property
    def password(self):
        return self._password

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    @password.setter
    def update_password(self, new_password):
        self.password = generate_password_hash(new_password)
