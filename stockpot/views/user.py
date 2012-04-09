from pyramid.view import view_config

@view_config(route_name='user_index', renderer='user/index.mako')
def index(request):
    return {'user':request.user,}

def user_routes(config):
    config.add_route('user_index', '')

