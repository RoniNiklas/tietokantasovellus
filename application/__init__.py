from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

from flask_sqlalchemy import SQLAlchemy


import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"    
    app.config["SQLALCHEMY_ECHO"] = False ## True

db = SQLAlchemy(app)

from application.controllers import customer
from application.controllers import orderManagement
from application.controllers import menuManagement
from application.controllers import auth
from application.controllers import owner

from application.models.restaurant import Restaurant
from application.models.menuItem import MenuItem
from application.models.order import Order
from application.models.orderMenuItem import OrderMenuItem
from application.models.user import User

try: 
    db.create_all()
except:
    pass

# kirjautuminen
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if len(Restaurant.query.all()) == 0:
    db.session().add(Restaurant("Ronin Pizza", "Halpaa ja hyvää pizzaa", "Leipurinmäki 1 a", "555-666-777"))
    db.session().commit()

if len(Restaurant.query.limit(1).all()[0].menu) == 0:
    id = Restaurant.query.limit(1).all()[0].id
    db.session().add(MenuItem(id, "Pizza Bolognese", "Pizzaa jauhelihakastikkeella. Saatavana myös vegaanisena.", 8.50, True))
    db.session().add(MenuItem(id, "Neapolitan Pizza", "Aito Napolilainen pizza leivottuna italialaisesta 00-jauhosta. Saatavana myös gluteenittomana.", 9.60, True))
    db.session().add(MenuItem(id, "Meat Lover's Fantasy", "Pizza, jossa täytteenä herkkusientä, grillattua munakoisoa, paprikaa, oliiveja ja valkosipulia.", 8.50, True))
    db.session().commit()

if len(User.query.all())== 0:
    db.session().add(User("Make", "Admin", bcrypt.generate_password_hash("Password").decode("utf-8"), 1))
    db.session().commit()