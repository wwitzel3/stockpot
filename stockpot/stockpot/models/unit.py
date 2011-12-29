from hashlib import sha1
from datetime import datetime

from ming import schema as S
from ming.orm import FieldProperty, FieldPropertyWithMissingNone
from ming.orm.declarative import MappedClass

from pyramid.httpexceptions import HTTPForbidden

from stockpot.models import DBSession

# If you change this AFTER a user signed up they will not be able to
# login until they perform a password reset.
SALT = 'supersecretsalt'

class User(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'users'
        custom_indexes = [
                dict(fields=('email',), unique=True, sparse=False),
                dict(fields=('username',), unique=True, sparse=False),
        ]

    _id = FieldProperty(S.ObjectId)
    username = FieldProperty(str)
    email = FieldProperty(str)
    password = FieldProperty(str)
    signup_date = FieldProperty(datetime, if_missing=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        self.signup_date = datetime.utcnow().replace(microsecond=0)
        self.username = kwargs.get('username')
        self.password = User.generate_password(kwargs.get('password'),
                str(self.signup_date))
        print self.password
        self.email = kwargs.get('email')

    @classmethod
    def authenticate(cls, login, password):
        user = cls.query.find({'$or': [{'username':login}, {'email':login}]}).one()
        print user
        if user:
            password = User.generate_password(password, str(user.signup_date))
            print password, user.password
            if password == user.password:
                return user
        else:
            return None

    @staticmethod
    def generate_password(password, salt):
        print password, salt
        password = sha1(password).hexdigest() + salt
        print password
        return sha1(password+SALT).hexdigest()

    @S.LazyProperty
    def id(self):
        return str(self._id)


