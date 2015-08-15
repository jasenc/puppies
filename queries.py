# Imports and configuration
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Puppy, Shelter
engine = create_engine('sqlite:///puppy_shelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

puppies = session.query(Puppy).order_by(Puppy.name).all()

for puppy in puppies:
    print puppy.name
