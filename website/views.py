from flask import Blueprint, render_template, request, flash, jsonify,redirect, url_for
from flask_login import login_required, current_user
from .models import Note, EditProfileForm, ContactForm
from . import db
import json
from datetime import datetime  # Add this import


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            # new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            new_note = Note(data=note, user_id=current_user.id, date=datetime.utcnow())
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)
    


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if request.method == 'GET':
            form.first_name.data = current_user.first_name
            form.last_name.data = current_user.last_name
            form.age.data = current_user.age
            form.phone.data = current_user.phone
            form.address.data = current_user.address

            return render_template('edit_profile.html', form=form)

    current_user.first_name = form.first_name.data
    current_user.last_name = form.last_name.data
    current_user.age = form.age.data
    current_user.phone = form.phone.data
    current_user.address = form.address.data

    db.session.commit()
    flash('Your changes have been saved.', 'success')
    return redirect(url_for('views.home'))


@views.route('/edit_contact', methods=['GET', 'POST'])
@login_required
def edit_contact():
    form = ContactForm()

    if request.method == 'GET':   
        form.email.data = current_user.email
        form.phone.data = current_user.phone
        form.address.data = current_user.address      
        return render_template('edit_contact.html', form=form)

    current_user.email = form.email.data
    current_user.phone = form.phone.data
    current_user.address = form.address.data
    db.session.commit()
    flash('Contact information updated!', category='success')
    return redirect(url_for('views.home'))

