from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    age= db.Column(db.String(150)) 
    phone = db.Column(db.String(150))
    address = db.Column(db.String(150))
    notes = db.relationship('Note')
    contact = db.relationship('Contact', backref='user', uselist=False)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class EditProfileForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    age = IntegerField('Age')
    phone = IntegerField('Phone')
    address = StringField('Address')
    submit = SubmitField('Save Changes')
    

class ContactForm(FlaskForm):
    email = StringField('Email')
    phone = StringField('Phone')
    address = StringField('Address')
    submit = SubmitField('Save Changes')
