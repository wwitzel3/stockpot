from pyramid.security import ALL_PERMISSIONS
from .models import DBSession
from .models.user import User

SITE_ACL = [
    ['Allow', 'system.Everyone', ['view']],
    ['Allow', 'role:viewer', ['view']],
    ['Allow', 'role:editor', ['view', 'add', 'edit']],
    ['Allow', 'role:owner', ['view', 'add', 'edit', 'manage']],
    ['Allow', 'role:admin', ALL_PERMISSIONS],
]

class RootFactory(object):
    __acl__ = SITE_ACL
    def __init__(self, request):
        pass

class UserFactory(object):
    @property
    def __acl__(self):
        if self.request.user:
            return [
                ['Allow', 'role:admin', ALL_PERMISSIONS],
                ['Allow', 'owner:{0}'.format(self.request.user.id), ALL_PERMISSIONS],
            ]
        else:
            return []
    def __init__(self, request):
        self.request = request

def groupfinder(userid, request):
    session = DBSession()
    user = session.query(User).get(userid)
    if user:
        groups = user.group_names()
        groups.append('owner:{0}'.format(user.id))
        return groups
    else:
        return []

