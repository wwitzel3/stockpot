import transaction

from sqlalchemy.exc import IntegrityError

from stockpot.model import DBSession, initialize_sql
from stockpot.model.mymodel import MyModel

class Root(object):
    __name__ = None
    __parent__ = None

    def __getitem__(self, key):
        session= DBSession()
        try:
            id = int(key)
        except (ValueError, TypeError):
            raise KeyError(key)

        item = session.query(MyModel).get(id)
        if item is None:
            raise KeyError(key)

        item.__parent__ = self
        item.__name__ = key
        return item

    def get(self, key, default=None):
        try:
            item = self.__getitem__(key)
        except KeyError:
            item = default
        return item

    def __iter__(self):
        session= DBSession()
        query = session.query(MyModel)
        return iter(query)

root = Root()

def root_factory(request):
    return root
    
def populate():
    session = DBSession()
    model = MyModel(name=u'test name', value=55)
    session.add(model)
    session.flush()
    transaction.commit()

def appmaker(engine):
    initialize_sql(engine)
    try:
        populate()
    except IntegrityError:
        DBSession.rollback()
    return root_factory