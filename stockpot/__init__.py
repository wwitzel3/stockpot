from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from pyramid.security import unauthenticated_userid

from sqlalchemy import engine_from_config

from .models import DBSession
from .models import User

from .security import groupfinder
from .views.user import user_routes
from .views.default import default_routes

def get_user(request):
    session = DBSession()
    userid = unauthenticated_userid(request)
    if userid is not None:
        return session.query(User).get(userid)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    authn_policy = AuthTktAuthenticationPolicy(
        settings.get('authn_secret'), callback=groupfinder)
    authz_policy = ACLAuthorizationPolicy()

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    config = Configurator(settings=settings,
                          root_factory='stockpot.security.RootFactory')

    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.set_request_property(get_user, 'user', reify=True)

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.include(default_routes)
    config.include(user_routes, route_prefix='user')

    config.include('pyramid_beaker')

    config.include('velruse.providers.facebook')
    config.setup_facebook_login_from_settings(prefix='facebook.')

    config.scan()
    return config.make_wsgi_app()

