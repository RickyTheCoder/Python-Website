from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note') #will get note from the HTML

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id) #current_user allows us to know all information about user if they are logged in (name, notes, email)
            db.session.add(new_note) #adds note to database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
        note = json.loads(request.data) # takes in data from post request
        noteId = note['noteId'] # will access noteId atribute from index.js
        note = Note.query.get(noteId) #note.query.get will look for the note that has that Id
        if note: #checks if it exists 
             if note.user_id == current_user.id: #security check
                  db.session.delete(note)
                  db.session.commit()

        return jsonify({}) # turns this into json object that can be returned (nothing is being returned but it is a requirement)

