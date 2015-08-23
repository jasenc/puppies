from puppies import app
from puppies import models
from flask import render_template, request, redirect, url_for
from puppies import forms


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
    # Get the form for shelters out of the forms module.
    form = forms.ShelterForm(request.form)
    # If the form is submitted via POST and is validated:
    if request.method == 'POST' and form.validate():
        # Create a new shelter object to store all data from the form.
        new_shelter = {
            "name": form.name.data,
            "address": form.address.data,
            "city": form.city.data,
            "state": form.state.data,
            "zipCode": form.zipCode.data,
            "website": form.website.data,
        }
        # Pass that object to the DB via the models module.
        models.shelter_new(new_shelter)
        # Redirect to the index page.
        return redirect(url_for('index'))
    else:
        # If the route is requested via GET, render the new shelter page.
        return render_template('shelters/new.html', form=form)


# Create edit shelter page.
@app.route('/shelter/<int:shelter_id>/edit', methods=['GET', 'POST'])
def editShelter(shelter_id):
    # Get the shelter out of the DB.
    edit_shelter = models.shelter_get(shelter_id)
    # Get the form out of the form module.
    form = forms.ShelterForm(request.form)
    # If the form is submitted via POST and is validated:
    if request.method == 'POST' and form.validate():
        # Update the shelter with the form data
        edit_shelter.name = form.name.data
        edit_shelter.address = form.address.data
        edit_shelter.city = form.city.data
        edit_shelter.state = form.state.data
        edit_shelter.zipCode = form.zipCode.data
        edit_shelter.website = form.website.data
        # Send the updated shelter back to the DB.
        models.shelter_edit(edit_shelter)
        # Redirect to the index page.
        return redirect(url_for('index'))
    else:
        # If the route is requested via GET, render the edit shelter page.
        return render_template('shelters/edit.html', shelter=edit_shelter,
                               form=form)


# Create a delete comfirmation page.
@app.route('/shelter/<int:shelter_id>/delete', methods=['GET', 'POST'])
def deleteShelter(shelter_id):
    # Get the shelter to be deleted out of the DB.
    delete_shelter = models.shelter_get(shelter_id)
    if request.method == 'POST':
        # Delete the shelter out of the DB.
        models.shelter_delete(delete_shelter)
        # Redirect to the index page.
        return redirect(url_for('index'))
    else:
        # If the route is requested via GET, render the delete shelter page.
        return render_template('shelters/delete.html', shelter=delete_shelter)


# Create a page for each shelter.
@app.route('/shelter/<int:shelter_id>/')
def showShelter(shelter_id):
    # Get the selected shelter from the DB.
    shelter = models.shelter_get(shelter_id)
    # Get the puppies for that shelter out of the DB.
    puppies = models.puppies_get_by_shelter(shelter_id)
    # Show the information on the shetlers show page.
    return render_template('shelters/show.html', shelter=shelter,
                           puppies=puppies)


# The following routes are essentially repeats of the previous ones but with
# more arguments passed around.
# Create a new page for puppies.
@app.route('/shelter/<int:shelter_id>/puppy/new', methods=['GET', 'POST'])
def newPuppy(shelter_id):
    shelter = models.shelter_get(shelter_id)
    puppies = models.puppies_get_by_shelter(shelter_id)
    form = forms.PuppyForm(request.form)
    if request.method == 'POST' and form.validate():
        new_puppy = {
            "name": form.name.data,
            "gender": form.gender.data,
            "dateOfBirth": form.dateOfBirth.data,
            "picture": form.picture.data,
            "weight": form.weight.data,
        }
        models.puppy_new(shelter_id, new_puppy)
        return render_template('shelters/show.html', shelter=shelter,
                               puppies=puppies)
    else:
        return render_template('puppies/new.html', shelter=shelter, form=form)


# Create a edit page for puppies.
@app.route('/shelter/<int:shelter_id>/puppy/<int:puppy_id>/edit',
           methods=['GET', 'POST'])
def editPuppy(shelter_id, puppy_id):
    shelter = models.shelter_get(shelter_id)
    puppies = models.puppies_get_by_shelter(shelter_id)
    edit_puppy = models.puppy_get(puppy_id)
    form = forms.PuppyForm(request.form)
    int_puppy_weight = int(edit_puppy.weight)
    if request.method == 'POST' and form.validate():
        edit_puppy.name = form.name.data
        edit_puppy.gender = form.gender.data
        edit_puppy.dateOfBirth = form.dateOfBirth.data
        edit_puppy.picture = form.picture.data
        edit_puppy.weight = form.weight.data
        models.puppy_edit(edit_puppy)
        return render_template('shelters/show.html', shelter=shelter,
                               puppies=puppies, form=form)
    else:
        return render_template('puppies/edit.html', shelter=shelter,
                               puppy=edit_puppy, form=form,
                               int_puppy_weight=int_puppy_weight)


# Create a delete page for puppies.
@app.route('/shelter/<int:shelter_id>/puppy/<int:puppy_id>/delete',
           methods=['GET', 'POST'])
def deletePuppy(shelter_id, puppy_id):
    delete_puppy = models.puppy_get(puppy_id)
    shelter = models.shelter_get(shelter_id)
    if request.method == 'POST':
        models.puppy_delete(delete_puppy)
        return redirect(url_for('showShelter', shelter_id=shelter.id))
    else:
        return render_template('puppies/delete.html', shelter=shelter,
                               puppy=delete_puppy)


# Create a page for each puppy.
@app.route('/shelter/<int:shelter_id>/puppy/<int:puppy_id>/')
def showPuppy(shelter_id, puppy_id):
    shelter = models.shelter_get(shelter_id)
    puppy = models.puppy_get(puppy_id)
    return render_template('puppies/show.html', shelter=shelter,
                           puppy=puppy)
