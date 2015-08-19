from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, validators
from wtforms.fields.html5 import DateField


class NewPuppyForm(Form):
    name = StringField('Name', [validators.InputRequired(),
                                validators.Length(max=80,
                                message="Let's keep this to 80 characters!")])
    gender = StringField('Gender', [validators.InputRequired(),
                                    validators.Length(max=6,
                                    message="Sorry, genders are at most 6\
                                            characters!")])
    dateOfBirth = DateField("Date of Birth", [validators.InputRequired()])
    picture = StringField('Picture', [validators.InputRequired()])
    weight = IntegerField('Weight', [validators.InputRequired(),
                                     validators.NumberRange(min=1, max=10,
                                     message="Between 1 and 10")])
