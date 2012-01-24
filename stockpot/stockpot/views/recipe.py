from pyramid.view import view_config
from pyramid.url import route_url
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound

import stockpot.models as M

@view_config(route_name='recipe.add', renderer='recipe/add.mako', request_method='GET')
def recipe_add(request):
    return dict()

def recipe_routes(config):
    config.add_route('recipe.add', '/add')

