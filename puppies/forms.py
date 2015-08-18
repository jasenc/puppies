from flask.ext.wtf import Form
from wtforms.fields import StringField, DateField, IntegerField
from wtforms.validators import Required, Length


class NewPuppyForm(Form):
    name = StringField('Name', validators=[Required(), Length(max=250)])
    gender = StringField('Gender', validators=[Required(), Length(max=6)])
    dateOfBirth = DateField("Date of Birth", validators=[Required()])
    picture = StringField('Picture', validators=[Required()])
    weight = IntegerField('Weight', validators=[Required()])
