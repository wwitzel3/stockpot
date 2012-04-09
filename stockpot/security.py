from pyramid.security import ALL_PERMISSIONS
from .models import (
    DBSession,
    User,
    )

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

def groupfinder(userid, request):
    session = DBSession()
    user = session.query(User).get(userid)
    if user:
        return user.group_names()
    else:
        return []

