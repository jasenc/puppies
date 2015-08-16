# Imports and configuration
from __future__ import division
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Puppy, Shelter
from datetime import date, timedelta
from math import floor
engine = create_engine('sqlite:///puppy_shelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# 1. Query all puppies and return the results in ascending alphabetical order.
puppies = session.query(Puppy).order_by(Puppy.name).all()

print '1. All Puppies:'
for puppy in puppies:
    print puppy.name
print "\n"

# 2. Query all of the puppies less than 6 months old, youngest first.
six_months_ago = (date.today() - timedelta(days=floor((6/12)*365)))

youngsters = session.query(Puppy).filter(Puppy.dateOfBirth >= six_months_ago).all()

print '2. Puppies under six months old:'
for puppy in youngsters:
    print "{0} : DOB - {1}".format(puppy.name, puppy.dateOfBirth)
print "\n"

# 3. Query all puppies by ascending weight.
by_weight = session.query(Puppy).order_by(Puppy.weight).all()
print '3. All puppies by weight:'
for puppy in by_weight:
    print "{0} : weight - {1}".format(puppy.name, round(puppy.weight, 1))
print "\n"

# 4. Query all puppies grouped by the shelter in which they are staying.
by_shelter = session.query(Puppy).order_by(Puppy.shelter_id).all()
print '4. All puppies by shelter:'
for puppy in by_shelter:
    print puppy
print "\n"
