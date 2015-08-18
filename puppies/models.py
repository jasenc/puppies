# Import database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy

# Connect to database and create session
engine = create_engine('sqlite:///puppy_shelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def shelter_list():
    return session.query(Shelter).all()
