from hashlib import md5

from ming import schema as S
from ming.orm import FieldProperty, FieldPropertyWithMissingNone
from ming.orm.declarative import MappedClass

from pyramid.httpexceptions import HTTPForbidden

from stockpot.models import DBSession

providers = ['Twitter', 'Google', 'Facebook']

class User(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'user'
        custom_indexes = [
                dict(fields=('identifier',), unique=True, sparse=False), 
                dict(fields=('email',), unique=True, sparse=True),
                dict(fields=('username',), unique=True, sparse=True),
        ]

    _id = FieldProperty(S.ObjectId)
    username = FieldPropertyWithMissingNone(str, if_missing=S.Missing)
    email = FieldProperty(str, if_missing=S.Missing)
    identifier = FieldProperty(str)
    provider = FieldProperty(str)

    first_name = FieldProperty(str)
    last_name = FieldProperty(str)
     
    def __init__(self, *args, **kwargs):
        self.identifier = self.find_identifier(**kwargs)
        self.provider = kwargs.get('providerName')

    @classmethod
    def find(cls, *arg, **kwargs):
        """Locate a User record using the identifier from a given
        provider. Note that the same user, using different OAuth accounts
        will end up with an account per provider.
        """
        identifier = cls.find_identifier(**kwargs)
        return cls.query.get(identifier=identifier)

    @classmethod
    def find_identifier(cls, *arg, **kwargs):
        """Using the providerNamer name determine which identifier to use
        This method will raise a pyramid.exceptions.Forbidden exception
        if the status is not 'ok' or if no known providerName is found
        """
        if not kwargs.get('status') == 'ok':
            raise HTTPForbidden

        profile = kwargs.get('profile')
        provider = kwargs.get('providerName') or profile.get('providerName')
        if provider in providers:
            return md5(profile.get('identifier')).hexdigest()
        else:
            raise HTTPForbidden

