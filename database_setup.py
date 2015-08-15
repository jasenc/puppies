# CONFIGURATION - Beginning of file.
# Import system-specific parameters and functions for interacting with the
# Python interpreter.
import sys

# From the SQLAlchemy module import the necessary classes to build our DB.
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric

# Import declarative_base to use for class input.
from sqlalchemy.ext.declarative import declarative_base

# Import relationship from SQLAlchemy ORM to create foreign key relationships.
from sqlalchemy.orm import relationship


from sqlalchemy import create_engine

# Create instance of declarative_base as Base.
# declarative_base lets SQLAlchemy know our classes are SQLAlchemy classes.
Base = declarative_base()


# Create a class to represent the Restaurant table in our DB.
class Shelter(Base):
    # Create table representation.
    __tablename__ = 'shelter'
    # Create a column "name" that is a string with a maximum of 80 characters,
    # nullable=False so this column cannot be blank.
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(20))
    zipCode = Column(String(10))
    website = Column(String)


# Note classes use CamelCase.
class Puppy(Base):
    # Note table names follow SQL conventions
    __tablename__ = 'puppy'
    # The following statements are known as Mappers.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(6), nullable=False)
    dateOfBirth = Column(Date)
    picture = Column(String)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    weight = Column(Numeric(10))

# CONFIGURATION - End of file.
# Create instance of create_engine and point to the database that will be used.
engine = create_engine('sqlite:///puppy_shelter.db')

# This adds the necessary classes for tables we will create in our database.
Base.metadata.create_all(engine)
