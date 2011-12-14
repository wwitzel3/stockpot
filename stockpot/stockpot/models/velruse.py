from datetime import datetime

from ming import schema as S
from ming.orm import FieldProperty
from ming.orm.declarative import MappedClass
from stockpot.models import DBSession

class Velruse(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'velruse_ustore'

    _id = FieldProperty(S.ObjectId, if_missing=None)
    key = FieldProperty(str)
    expires = FieldProperty(S.DateTime)
    value = FieldProperty(S.Binary)

