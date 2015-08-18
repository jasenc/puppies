# Import Flask and initiate application.
from flask import (Flask, render_template, request, redirect, url_for, flash,
                   jsonify)
app = Flask(__name__)

# Import Views
import puppies.views  # noqa

# Import models
import puppies.models  # noqa
