from pyramid.view import view_config
from pyramid.url import route_url
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound
from pyramid.renderers import render

from formencode import Invalid
from formencode import htmlfill

import stockpot.models as M
import stockpot.schema as S

@view_config(route_name='user.profile', renderer='user/profile.mako',
             request_method='GET')
def profile(request):
    user = M.User.query.get(**request.matchdict)
    if not user:
        raise HTTPNotFound
    update_form = render('stockpot:templates/widgets/user/update.mako',
            dict(user=user))
    return dict(user=user, update_form=update_form)

@view_config(route_name='user.profile',  renderer='user/profile.mako',
             request_method='POST')
def profile_update(request):
    user = M.User.query.get(**request.matchdict)
    try:
        clean_data = S.UserUpdateSchema(user=user).to_python(request.params)
        user.update(**clean_data)
        M.DBSession.flush()
        return HTTPFound(location=route_url('user.profile', request,
                     username=user.username))
    except Invalid, e:
        e.value['password'] = ''
        e.value['password_verify'] = ''
        update_form = render('stockpot:templates/widgets/user/update.mako', dict(user=user))
        update_form = htmlfill.render(update_form, e.value, e.error_dict or {})

    return dict(user=user, update_form=update_form)

def user_routes(config):
    config.add_route('user.profile', '/{username}')

