from pyramid.view import view_config
from pyramid.url import route_url
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound

import bson
import stockpot.models as M

@view_config(route_name='user.profile', renderer='user/profile.mako',
        request_method='GET')
def profile(request):
    userid = bson.ObjectId(request.matchdict.get('userid'))
    user = M.User.query.get(_id=userid)
    if not user:
        raise HTTPNotFound
    return dict(user=user)

@view_config(route_name='user.profile', request_method='POST')
def profile_update(request):
    request.user.username = request.params.get('username')
    M.DBSession.flush()
    return HTTPFound(location=route_url('user.profile', request,
                                        userid=request.userid))

def user_routes(config):
    config.add_route('user.profile', '/{userid}')

