try:
    import cPickle as pickle
except ImportError:
    import pickle

from pyramid.httpexceptions import HTTPFound
from pyramid.security import forget
from pyramid.security import remember
from pyramid.security import unauthenticated_userid
from pyramid.view import view_config
from pyramid.url import route_url

import ccb.models as M

@view_config(route_name='index', renderer='default/index.mako')
def index(request):
    return dict(user_id=unauthenticated_userid(request))

@view_config(route_name='login')
def login(request):
    if 'token' in request.params:
        token = request.params.get('token')
        storage = M.Velruse.query.get(key=token)
        values = pickle.loads(storage.value)

        user = M.User.find(**values)

        if not user:
            user = M.User(**values)
            M.DBSession.flush()

        headers = remember(request, str(user._id))
        return HTTPFound(location=route_url('index', request),
                         headers=headers)


