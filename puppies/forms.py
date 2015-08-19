from flask.ext.wtf import Form
from wtforms import StringField, DateField, IntegerField, validators


class NewPuppyForm(Form):
    name = StringField('Name', [validators.InputRequired()])
    gender = StringField('Gender', [validators.InputRequired()])
    dateOfBirth = DateField("Date of Birth", [validators.InputRequired()])
    picture = StringField('Picture', [validators.InputRequired()])
    weight = IntegerField('Weight', [validators.InputRequired()])
