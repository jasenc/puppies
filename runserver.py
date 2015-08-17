# Import application.
from puppies import app
# Create a secret_key for flash method to keep track of users.
# Note: this is a silly development key.
app.secret_key = 'super_secret_key'
# Enabling debug mode tells Flask to reload the server on code changes.
# AND Provides a debugger in the browser.
app.debug = True
app.run(host='0.0.0.0', port=5000)
