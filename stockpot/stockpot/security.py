from pyramid.security import unauthenticated_userid
from pyramid.decorator import reify
from pyramid.request import Request

from cookbook.model import DBSession
from cookbook.model.user import User

def groupfinder(userid, request):
    user = request.user
    if user is not None:
        return [group.name for group in user.user_groups] + ['owner:{0}'.format(userid)]
    return None
    
class RequestWithUserAttribute(Request):
    @reify
    def db(self):
        return DBSession()
        
    @reify
    def user(self):
        userid = unauthenticated_userid(self)
        if userid is not None:
            return self.db.query(User).get(userid)
        return None