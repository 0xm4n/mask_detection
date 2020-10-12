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
    password = Column(db.String(255))

    role = Column(SmallInteger, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def check_password(self, raw):
        if not self.password:
            return False
        return check_password_hash(self.password, raw)

    def update_password(self, new_password):
        self.password = generate_password_hash(new_password)
