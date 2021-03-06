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
    # Instantiate a new Shelter object from the information stored in the
    # newShelter object passed through as an arguement.
    newShelter = Shelter(name=new_shelter["name"],
                         address=new_shelter["address"],
                         city=new_shelter["city"],
                         state=new_shelter["state"],
                         zipCode=new_shelter["zipCode"],
                         website=new_shelter["website"])
    session.add(newShelter)
    session.commit()


def shelter_get(shelter_id):
    # Return all information for the shelter that has the id that was passed
    # through as an argument.
    return session.query(Shelter).filter_by(id=shelter_id).one()


def shelter_edit(edit_shelter):
    # Update the edited shelter in the DB.
    session.add(edit_shelter)
    session.commit()


def shelter_delete(delete_shelter):
    # Delete the shelter passed as an argument out of the DB.
    session.delete(delete_shelter)
    session.commit()


def puppies_get_by_shelter(shelter_id):
    # Return all puppies assigned to the shelter_id passed as an argument.
    return session.query(Puppy).filter_by(shelter_id=shelter_id)


def puppy_new(shelter_id, new_puppy):
    # Instantiate a new Puppy object from the information stored in the
    # newPuppy object passed through as an arguement.
    newPuppy = Puppy(name=new_puppy["name"],
                     gender=new_puppy["gender"],
                     dateOfBirth=new_puppy["dateOfBirth"],
                     picture=new_puppy["picture"],
                     shelter_id=shelter_id,
                     weight=new_puppy["weight"])
    session.add(newPuppy)
    session.commit()


def puppy_get(puppy_id):
    # Return the information for the puppy that matches the id passed as an
    # argument.
    return session.query(Puppy).filter_by(id=puppy_id).one()


def puppy_edit(edit_puppy):
    # Update the edited puppy in the DB.
    session.add(edit_puppy)
    session.commit()


def puppy_delete(delete_puppy):
    # Delete the puppy passed as an argument out of the DB.
    session.delete(delete_puppy)
    session.commit()
