from stockpot.models import (
    Base,
)

from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    Boolean,
    Numeric,
    ForeignKey,
    )

from sqlalchemy.orm import (
    relationship,
    )

class FoodGroup(Base):
    __tablename__ = 'food_group'
    id = Column(Integer, primary_key=True)
    desc = Column(Unicode(60))

class Food(Base):
    __tablename__ = 'foods'
    id = Column(Integer, primary_key=True)

    group_id = Column(Integer, ForeignKey(FoodGroup.id), nullable=False)
    group = relationship(FoodGroup)

#    nutrients = relationship(FoodNutrients, secondary='food_nutrients')

    desc = Column(Unicode(200), nullable=False)
    short_desc = Column(Unicode(60), nullable=False)
    common_name = Column(Unicode(100))
    manufc_name = Column(Unicode(65))
    sci_name = Column(Unicode(65))

    # indicates if food is used in USDA food studies, and thus has a complete
    # nutrient profile for the 65 FNDDS nutrients.
    survey = Column(Boolean())

    # description of inedible parts of a food item (refuse), such as
    # seeds or bone.
    refuse_desc = Column(Unicode(135))
    refuse = Column(Numeric())

    # factor for convering nitrogen to protein
    n_factor = Column(Numeric())
    # factor for calc calories from protein
    pro_factor = Column(Numeric())
    # factor for calc calories from fat
    fat_factor = Column(Numeric())
    # factor for calc calorites from carbs
    cho_factor = Column(Numeric())

class Nutrient(Base):
    __tablename__ = 'nutrients'
    id = Column(Integer, primary_key=True)

class FoodNutrients(Base):
    __tablename__  = 'food_nutrients'
    food_id = Column(Integer, ForeignKey(Food.id), primary_key=True)
    nutrient_id = Column(Integer, ForeignKey(Nutrient.id), primayr_key=True)

