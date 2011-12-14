from pyramid.decorator import reify
from pyramid.request import Request

import ccb.models as M

def groupfinder(userid, request):
    user = M.User.query.get(_id=userid)
    return [] if user else None

class RequestWithDBAttribute(Request):
    @reify
    def db(self):
        return M.DBSession()

    @reify
    def user(self):
        userid = unauthenticated_userid(self)
        if userid:
            return M.User.query.get(_id=userid)
        return None

