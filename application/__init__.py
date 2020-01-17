from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import controller

from application.models import models

db.create_all()

from application.models.models import Restaurant, MenuItem
if len(Restaurant.query.all()) == 0:
    db.session().add(Restaurant("Ronin Pizza", "Halpaa ja hyvää pizzaa", "Leipurinmäki 1 a", "555-666-777", "https://google.com"))
    db.session.commit()

if len(Restaurant.query.limit(1).all()[0].menu) == 0:
    id = Restaurant.query.limit(1).all()[0].id
    db.session().add(MenuItem(id, "Pizza Bolognese", "Pizzaa jauhelihakastikkeella. Saatavana myös vegaanisena.", 8.50))
    db.session().add(MenuItem(id, "Neapolitan Pizza", "Aito Napolilainen pizza leivottuna italialaisesta 00-jauhosta. Saatavana myös gluteenittomana.", 9.60))
    db.session.commit()