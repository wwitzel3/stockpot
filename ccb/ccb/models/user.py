from hashlib import md5

from ming import schema as S
from ming.orm import FieldProperty
from ming.orm.declarative import MappedClass

from pyramid.httpexceptions import HTTPForbidden

from ccb.models import DBSession

class User(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'user'

    _id = FieldProperty(S.ObjectId)
    display_name = FieldProperty(str)
    identifier = FieldProperty(str)

    def __init__(self, *args, **kwargs):
        self.identifier = self.find_identifier(**kwargs)

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
        if provider == 'Twitter' or provider == 'Facebook' or provider == 'Google':
            identifier_hash = md5(profile.get('identifier')).hexdigest()
            return identifier_hash
        else:
            raise HTTPForbidden

