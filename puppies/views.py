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
        return render_template('shelters/new.html')


# Create edit shelter page.
@app.route('/shelter/<int:shelter_id>/edit', methods=['GET', 'POST'])
def editShelter(shelter_id):
    edit_shelter = models.shelter_get(shelter_id)
    if request.method == 'POST':
        edit_shelter.name = request.form['name']
        edit_shelter.address = request.form['address']
        edit_shelter.city = request.form['city']
        edit_shelter.state = request.form['state']
        edit_shelter.zipCode = request.form['zipCode']
        edit_shelter.website = request.form['website']
        models.shelter_edit(edit_shelter)
        return redirect(url_for('index'))
    else:
        return render_template('shelters/edit.html', shelter=edit_shelter)


# Create a delete comfirmation page.
@app.route('/shelter/<int:shelter_id>/delete', methods=['GET', 'POST'])
def deleteShelter(shelter_id):
    delete_shelter = models.shelter_get(shelter_id)
    if request.method == 'POST':
        models.shelter_delete(delete_shelter)
        return redirect(url_for('index'))
    else:
        return render_template('shelters/delete.html', shelter_id=shelter_id,
                               shelter=delete_shelter)


# Create a page for each shelter.
@app.route('/shelter/<int:shelter_id>/')
def showShelter(shelter_id):
    shelter = models.shelter_get(shelter_id)
    puppies = models.puppies_get_by_shelter(shelter_id)
    return render_template('shelters/show.html', shelter=shelter,
                           puppies=puppies)


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
                               puppies=puppies, form=form)
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
@app.route('/shelter/<int:shelter_id>/puppy/<int:puppy_id>/delete')
def deletePuppy(shelter_id, puppy_id):
    return "This page will show the delete page for the selected puppy"


# Create a page for each puppy.
@app.route('/shelter/<int:shelter_id>/puppy/<int:puppy_id>/')
def showPuppy(shelter_id, puppy_id):
    return "This page will show the selected puppy"
