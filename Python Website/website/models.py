from . import db 
from flask_login import UserMixin 
from sqlalchemy.sql import func
# func will get current date and time and store as default value from line 10)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



# foreign key relationships: notes must belong to a user (how to associate different information with different users: relationship between note object and user object, lines 7 and 15.)
# foreign key is a key on one of database tables that always references an ID to another database column 
# one to many relationship: one user that has many notes (databases). This allows us to know whenever a user creates a note (note will be associated with the user ID) line 11. 
# many to one is having one note belonging to many users
# primary key here is 'user.id' 
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

# line 24 tells flask and sql, whenever a note is added, the relationship field will store all of the different notes created be users. Relationship references the name of the class (ex. line 7 'Note' and line 24)