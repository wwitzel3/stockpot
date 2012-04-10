from pyramid.view import view_config

from stockpot.security import UserFactory

@view_config(route_name='user_index', renderer='user/index.mako')
def index(request):
    return {'user':request.user,}

@view_config(route_name='user_profile', renderer='json', permission='edit')
def profile(request):
    return {}

def user_routes(config):
    config.add_route('user_profile', '/profile', factory=UserFactory)
    config.add_route('user_index', '')

