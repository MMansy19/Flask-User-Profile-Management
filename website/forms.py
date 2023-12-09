from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User
from wtforms import StringField, IntegerField, SubmitField




class EditProfileForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    age = IntegerField('Age')
    phone = IntegerField('Phone')
    address = StringField('Address')
    submit = SubmitField('Save Changes')
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])


