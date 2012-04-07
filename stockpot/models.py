import cryptacular.bcrypt

from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    synonym,
    )

from sqlalchemy.orm.exc import (
    NoResultFound,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
crypt = cryptacular.bcrypt.BCRYPTPasswordManager()

def hash_password(password):
    return unicode(crypt.encode(password))

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(32), unique=True)
    email = Column(Unicode(256))
    name = Column(Unicode(60))
    _password = Column('password', Unicode(60))

    def _get_password(self):
        return self._password
    def _set_password(self, password):
        self._password = hash_password(password)

    password = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    @classmethod
    def validate_user(cls, username, password):
        try:
            user = cls.query.filter_by(username=username).one()
            if crypt.check(user.password, password):
                return user
        except NoResultFound:
            return None
        else:
            return None
