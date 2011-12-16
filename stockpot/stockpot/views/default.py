try:
    import cPickle as pickle
except ImportError:
    import pickle

from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPForbidden
from pyramid.security import forget
from pyramid.security import remember
from pyramid.security import unauthenticated_userid
from pyramid.view import view_config
from pyramid.url import route_url

import stockpot.models as M

@view_config(route_name='index', renderer='default/index.mako')
def index(request):
    return dict(userid=unauthenticated_userid(request))

@view_config(route_name='login', request_param='token')
def login(request):
    token = request.params.get('token')
    storage = M.Velruse.query.get(key=token)
    values = pickle.loads(storage.value)
    user = M.User.find(**values)

    if not user:
        user = M.User(**values)
        M.DBSession.flush()

    userid = str(user._id)
    headers = remember(request, str(user._id))

    if user.username:
        return HTTPFound(location=route_url('index', request),
                         headers=headers)
    else:
        return HTTPFound(location=route_url('user.profile', request,
                         userid=userid), headers=headers)

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location=route_url('index', request),
                     headers=headers)

@view_config(context=HTTPForbidden, renderer='default/forbidden.mako')
def forbidden(request):
    return dict()

def default_routes(config):
    config.add_route('index', '')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

