from ming import Session
from ming.datastore import DataStore
from ming.orm import ThreadLocalORMSession
from ming.orm import Mapper

session = Session()
DBSession = ThreadLocalORMSession(session)

def init_mongo(engine):
    server, database = engine
    datastore = DataStore(server, database=database)
    session.bind = datastore
    Mapper.compile_all()

    for mapper in Mapper.all_mappers():
        session.ensure_indexes(mapper.collection)
    DBSession.flush()
    DBSession.close_all()

# Database includes here allow for a simple programming API convention. By importing all the models here
# we can use the import models as M convention throughout the rest of the code.
from .velruse import Velruse
from .user import User

# Explicit is better.
__all__ = [
    'DBSession',
    'init_mongo',
    'Velruse',
    'User',
]

