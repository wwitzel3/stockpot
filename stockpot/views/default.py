from pyramid.view import (
    view_config,
    notfound_view_config,
    )

from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
    )

from pyramid.httpexceptions import (
    HTTPFound,
    )

from pyramid.url import route_url
from velruse import login_url
from colander import Invalid

from stockpot.models import (
    DBSession,
    User,
    Group,
    )

import stockpot.schemas as S

@view_config(route_name='index', renderer='index.mako')
def index(request):
    logged_in = authenticated_userid(request)
    return {'logged_in':logged_in}

@view_config(route_name='login', renderer='login.mako')
def login_view(request):
    if 'form.submitted' in request.POST:
        try:
            cuser = S.User().deserialize(request.POST)
        except Invalid, e:
            return {'login_url':login_url, 'errors':e.asdict()}
        else:
            user = User(**cuser)
            session = DBSession()
            group = session.query(Group).filter_by(name='role:viewer').one()
            user.groups.append(group)

            session.add(user)
            session.flush()

            headers = remember(request, user.id)
            redirect_url = route_url('index', request)
            return HTTPFound(location=redirect_url, headers=headers)
    elif 'form.auth' in request.POST:
        try:
            clogin = S.Login().deserialize(request.POST)
        except Invalid, e:
            return {'login_url':login_url, 'errors':e.asdict()}
        else:
            user = User.validate(**clogin)
            if user:
                headers = remember(request, user.id)
                redirect_url = route_url('index', request)
                return HTTPFound(location=redirect_url, headers=headers)
            else:
                errors = ['Invalid username/password',]
                return {'login_url':login_url, 'errors':errors}
    return {'login_url': login_url, 'errors':[]}

@view_config(route_name='logout', permission='view')
def logout_view(request):
    headers = forget(request)
    return HTTPFound(location=route_url('index', request), headers=headers)

@view_config(context='velruse.AuthenticationComplete', renderer='json')
def login_complete_redirect(request):
    return {'success':True}

@view_config(context='velruse.AuthenticationDenied', renderer='json')
def login_denied_view(request):
    return {'denied':True}

@notfound_view_config(append_slash=True, renderer='errors/404.mako')
def notfound(request):
    return {}

def default_routes(config):
    config.add_route('index', '')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('register', '/register')
    config.add_route('auth', '/auth')

