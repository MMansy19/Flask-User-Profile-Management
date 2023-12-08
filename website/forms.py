from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class EditProfileForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    age = IntegerField('Age')
    phone = StringField('Phone')
    address = StringField('Address')
    submit = SubmitField('Save Changes')
