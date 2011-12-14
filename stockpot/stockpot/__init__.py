from pyramid.config import Configurator
from pyramid.events import NewRequest
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

import stockpot.models as M
from stockpot.security import RequestWithAttributes
from stockpot.security import groupfinder

from stockpot.views.default import default_routes

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    authn_p = AuthTktAuthenticationPolicy(secret='stockpot-secret', callback=groupfinder)
    authz_p = ACLAuthorizationPolicy()

    config = Configurator(
        settings=settings,
        request_factory=RequestWithAttributes,
        authentication_policy=authn_p,
        authorization_policy=authz_p,
    )
    config.begin()
    ## Database
    config.scan('stockpot.models')
    M.init_mongo(engine=(settings.get('mongo.url'), settings.get('mongo.database')))

    ## Routing & Views
    config.include(default_routes, route_prefix='')

    config.scan('stockpot.views')
    config.add_static_view('static', 'stockpot:static')

    config.add_subscriber(close_mongo_db, NewRequest)
    config.end()
    return config.make_wsgi_app()

def close_mongo_db(event):
    def close(request):
        M.DBSession.close_all()
    event.request.add_finished_callback(close)
