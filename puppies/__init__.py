# Import database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy

# Import Flask and initiate application.
from flask import (Flask, render_template, request, redirect, url_for, flash,
                   jsonify)
app = Flask(__name__)

# Import Views
import puppies.views  # noqa

# Connect to database and create session
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
