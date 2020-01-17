from application import app
from flask import Flask, render_template, jsonify
from application.models.models import Restaurant


@app.route("/")
def front():
    return render_template("main.html")


@app.route("/api/restaurants/<restaurantId>")
def getRestaurant(restaurantId):
    restaurant = Restaurant.query.get(restaurantId)
    return jsonify({
        "name": restaurant.name,
        "description": restaurant.description,
        "address": restaurant.address,
        "phone": restaurant.phone,
        "url": restaurant.url
   })

@app.route("/api/menus/<restaurantId>")
def getMenu(restaurantId):
    menu = Restaurant.query.get(restaurantId).menu
    returnable = []
    for item in menu:
        returnable.append({"name": item.name, "description": item.description, "price": item.price})
    return jsonify(returnable)