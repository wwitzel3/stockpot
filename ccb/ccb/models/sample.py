from ming import schema as S
from ming.orm import FieldProperty
from ming.orm.declarative import MappedClass
from ccb.models import DBSession

class Sample(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'sample'

    _id = FieldProperty(S.ObjectId)
    name = FieldProperty(str)
    value = FieldProperty(int)
