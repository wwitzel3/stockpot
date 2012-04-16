from stockpot.models import (
    DBSession,
    Base,
)

import cryptacular.bcrypt

from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    ForeignKey,
    Table,
    )

from sqlalchemy.orm import (
    synonym,
    relationship,
    )

from sqlalchemy.orm.exc import (
    NoResultFound,
    )

crypt = cryptacular.bcrypt.BCRYPTPasswordManager()

def hash_password(password):
    return unicode(crypt.encode(password))

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(15), unique=True)

    def __init__(self, name):
        self.name = name


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(32), unique=True)
    email = Column(Unicode(256), unique=True)
    groups = relationship(Group, secondary='user_group')
    _password = Column('password', Unicode(60))

    # Optional profile fields
    name = Column(Unicode(60))

    def _get_password(self):
        return self._password
    def _set_password(self, password):
        self._password = hash_password(password)

    password = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def group_names(self):
        return [group.name for group in self.groups]

    @classmethod
    def by_id(cls, userid):
        session = DBSession()
        return session.query(cls).get(userid)

    @classmethod
    def validate(cls, email, password):
        try:
            session = DBSession()
            user = session.query(cls).filter_by(email=email).one()
            if crypt.check(user.password, password):
                return user
        except NoResultFound:
            return None
        else:
            return None

    @property
    def __acl__(self):
        return [
            ('Allow', 'owner:{0}'.format(self.user.id), ('add', 'edit'))
        ]

user_group_table = Table('user_group', Base.metadata,
    Column('user_id', Integer, ForeignKey(User.id)),
    Column('group_id', Integer, ForeignKey(Group.id)),
)
