from pyramid.decorator import reify
from pyramid.request import Request
from pyramid.security import unauthenticated_userid

import bson
import stockpot.models as M

def groupfinder(userid, request):
    userid = bson.ObjectId(userid)
    user = M.User.query.get(_id=userid)
    return [] if user else None

class RequestWithAttributes(Request):
    @reify
    def db(self):
        return M.DBSession()

    @reify
    def user(self):
        userid = unauthenticated_userid(self)
        userid = bson.ObjectId(userid)
        if userid:
            return M.User.query.get(_id=userid)
        return None

