# Import Flask and initiate application.
from flask import (Flask)
app = Flask(__name__)

# Import Views
import puppies.views  # noqa

# Import models
import puppies.models  # noqa
