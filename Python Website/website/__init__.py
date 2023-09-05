from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SanPellegrino1738'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

# lines 17-18 registers our blueprints

    from .models import User, Note

# purpose of importing '.models' (line 22) is because we need to make sure models.py file runs before we create our database 

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
# tells flask how to load a user 
# User.query.get looks for the primary key 

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

# line 31 is a path module that will check if database exists and if it does not exist, line 32 will create it 
# line 32 app has the SQLalchemy database uri which tells us where to create the database 
# line 22 syntax is important because we can't start a variable with a '.' so we change the name. 