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


def shelter_new(new_shelter):
    newShelter = Shelter(name=new_shelter["name"],
                         address=new_shelter["address"],
                         city=new_shelter["city"],
                         state=new_shelter["state"],
                         zipCode=new_shelter["zipCode"],
                         website=new_shelter["website"])
    session.add(newShelter)
    session.commit()


def shelter_get(shelter_id):
    return session.query(Shelter).filter_by(id=shelter_id).one()


def shelter_edit(edit_shelter):
    session.add(edit_shelter)
    session.commit()


def shelter_delete(delete_shelter):
    session.delete(delete_shelter)
    session.commit()
