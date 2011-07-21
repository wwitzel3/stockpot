from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import Column

from stockpot.model import Base

class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True)
    value = Column(Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value