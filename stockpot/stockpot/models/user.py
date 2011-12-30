from hashlib import sha1
from datetime import datetime
from string import ascii_letters, digits
from random import choice

from ming import schema as S
from ming.orm import FieldProperty, FieldPropertyWithMissingNone
from ming.orm.declarative import MappedClass

from pyramid.httpexceptions import HTTPForbidden

from stockpot.models import DBSession

# If you change this AFTER a user signed up they will not be able to
# login until they perform a password reset.
SALT = 'supersecretsalt'
CHARS = ascii_letters + digits
MAX_TRIES = 100

class User(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'users'
        custom_indexes = [
                dict(fields=('email',), unique=True, sparse=False),
                dict(fields=('username',), unique=True, sparse=False),
                dict(fields=('identifier',), unique=True, sparse=False),
        ]

    _id = FieldProperty(S.ObjectId)
    username = FieldProperty(str)
    email = FieldProperty(str)
    password = FieldProperty(str, if_missing=S.Missing)
    signup_date = FieldProperty(datetime, if_missing=datetime.utcnow())

    identifier = FieldProperty(str)
   
    twitter_id = FieldProperty(str)
    twitter_auth_token = FieldProperty(str)
    twitter_auth_secret = FieldProperty(str)

    facebook_id = FieldProperty(str)
    facebook_auth_token = FieldProperty(str)

    def __init__(self, *args, **kwargs):
        self.signup_date = datetime.utcnow().replace(microsecond=0)
        self.username = kwargs.get('username')
        if kwargs.get('password'):
            self.password = User.generate_password(kwargs.get('password'),
                    str(self.signup_date))
        self.email = kwargs.get('email', '{0}@example.com'.format(self.username))

    def update(self, *args, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def social(cls, *args, **kwargs):
        print kwargs
        if not kwargs.get('status') == 'ok':
            raise HTTPForbidden

        # Grab out passed in values from end_point callback
        profile = kwargs.get('profile')
        provider = profile.get('providerName')
        credentials = kwargs.get('credentials')
        identifier = sha1(profile.get('identifier') + SALT).hexdigest()

        # Check if we already have a user with that identity?
        user = cls.query.get(identifier=identifier)
        if user:
            user.update_social_tokens(profile, credentials)
            return user

        # Get the username depending on the provider
        if provider == 'Facebook':
            username = profile.get('preferredUsername', None)
        elif provider == 'Twitter':
            username = profile.get('displayName', [None])[0]

        # Ensure the username is unique
        tries = 0
        while tries < MAX_TRIES:
            if not username:
                username = User.random_username(_range=7)
            if username and cls.query.get(username=username):
                username = username + User.random_username(_range=3, prefix='_')
            if username and not cls.query.get(username=username):
                break
            tries += 1
        else:
            raise HTTPForbidden

        # Create the user, update the identifier, and socal tokens
        user = cls(username=username)
        user.identifier = identifier
        user.update_social_tokens(profile, credentials)

        return user

    def update_social_tokens(self, profile, credentials):
        provider = profile.get('providerName')
        if provider == 'Facebook':
            self.facebook_id = profile.get('preferredUsername')
            email = profile.get('verifiedEmail')
            if not self.query.get(email=email):
                self.email = profile.get('verifiedEmail')
            self.facebook_auth_token = credentials.get('oauthAccessToken')
        elif provider == 'Twitter':
            self.twitter_id = profile.get('displayName')[0]
            self.twitter_auth_token = credentials.get('oauthAccessToken')[0]
            self.twitter_auth_secret = credentials.get('oauthAccessTokenSecret')[0]

    @classmethod
    def authenticate(cls, login, password):
        user = cls.query.find({'$or': [{'username':login}, {'email':login}]}).one()
        if user:
            password = User.generate_password(password, str(user.signup_date))
            if password == user.password:
                return user
        else:
            return None

    @staticmethod
    def generate_password(password, salt):
        password = sha1(password).hexdigest() + salt
        return sha1(password+SALT).hexdigest()

    @staticmethod
    def random_username(_range=5, prefix=''):
        return prefix + ''.join([choice(CHARS) for i in range(_range)])

    @S.LazyProperty
    def id(self):
        return str(self._id)


