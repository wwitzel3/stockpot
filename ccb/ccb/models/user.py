from ming import schema as S
from ming.orm import FieldProperty
from ming.orm.declarative import MappedClass

from pyramid.exceptions import Forbidden

from ccb.models import DBSession

class User(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'user'

    _id = FieldProperty(S.ObjectId)
    display_name = FieldProperty(str)
    access_token = FieldProperty(str)

    def __init__(self, *args, **kwargs):
        self.access_token = self.find_access_token(**kwargs)

    @classmethod
    def find(cls, *arg, **kwargs):
        """Locate a User record using the access_token from a given
        provider. Note that the same user, using different OAuth accounts
        will end up with an account per provider.
        """
        access_token = cls.find_access_token(**kwargs)
        return cls.query.get(access_token=access_token)

    @classmethod
    def find_access_token(cls, *arg, **kwargs):
        """Using the providerNamer name determine which access token to use
        This method will raise a pyramid.exceptions.Forbidden exception
        if the status is not 'ok' or if no known providerName is found
        """
        if not kwargs.get('status') == 'ok':
            raise Forbidden

        profile = kwargs.get('profile')
        provider = kwargs.get('providerName') or profile.get('providerName')
        if provider == 'Twitter':
            return kwargs.get('credentials').get('oauthAccessToken')[0]
        elif provider == 'Facebook':
            return kwargs.get('credentials').get('oauthAccessToken')
        elif provider == 'Google':
            return profile.get('identifier')
        else:
            raise Forbidden

