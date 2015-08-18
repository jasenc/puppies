from puppies import app
from puppies import models
from flask import render_template, request, redirect, url_for


# Create index page that shows all shelters.
@app.route('/')
@app.route('/index/')
@app.route('/shelter/')
def index():
    shelters = models.shelter_list()
    return render_template('index.html', shelters=shelters)


# Create new shelter page.
@app.route('/shelter/new', methods=['GET', 'POST'])
def newShelter():
    if request.method == 'POST':
        new_shelter = {
            "name": request.form['name'],
            "address": request.form['address'],
            "city": request.form['city'],
            "state": request.form['state'],
            "zipCode": request.form['zipCode'],
            "website": request.form['website']
        }
        models.shelter_new(new_shelter)
        return redirect(url_for('index'))
    else:
        return render_template('newshelter.html')



# Create edit shelter page.
@app.route('/shelter/<int:shelter_id>/edit')
def editShelter(shelter_id):
    shelter = shelter_edit(shelter_id)
    print shelter
    return "This page will show a form to edit the selected shelter"


# Create a delete comfirmation page.
@app.route('/shelter/<int:shelter_id>/delete')
def deleteShelter(shelter_id):
    return "This page will ask for confirmation to delete the selected shelter"


# Create a page for each shelter.
@app.route('/shelter/<int:shelter_id>/')
def showShelter(shelter_id):
    return "This page will show the selected shelter"


# Create a page for each puppy.
@app.route('/shelter/<int:shelter_id>/puppy/<int:puppy_id>/')
def puppyPage(shelter_id, puppy_id):
    return "This page will show the selected puppy"


# Create a new page for puppies.
@app.route('/shelter/<int:shelter_id>/puppy/new')
def puppyNew(shelter_id):
    return "This page will show the new puppy page"


# Create a edit page for puppies.
@app.route('/shelter/<int:shelter_id>/puppy/<int:puppy_id>/edit')
def puppyEdit(shelter_id, puppy_id):
    return "This page will show the edit page for the selected puppy"


# Create a delete page for puppies.
@app.route('/shelter/<int:shelter_id>/puppy/<int:puppy_id>/delete')
def puppyDelete(shelter_id, puppy_id):
    return "This page will show the delete page for the selected puppy"
