from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession
from .views import default_routes

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    config.include(default_routes, route_prefix='')

    config.include('pyramid_beaker')

    config.include('velruse.providers.facebook')
    config.setup_facebook_login_from_settings(prefix='facebook.')

    config.scan()
    return config.make_wsgi_app()

