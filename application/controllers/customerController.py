from application import app
from flask import Flask, render_template, jsonify, request
from application import db
from application.models.restaurant import Restaurant
from application.models.menuItem import MenuItem
from application.models.order import Order
from application.models.orderMenuItem import OrderMenuItem
import json


@app.route("/")
def front():
    return render_template("customer/main.html")


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
        if (item.active):
            returnable.append({"id": item.id, "name": item.name,
                               "description": item.description, "price": item.price})
    return jsonify(returnable)


@app.route("/api/orders/<restaurantId>", methods=['POST'])
def postOrder(restaurantId):
    order = json.loads(request.data)
    order['price'] = 0
    returnableItemList = []
    savedOrder = Order(
        restaurantId, order['name'], order['address'], order['phone'], order['price'])
    db.session().add(savedOrder)
    for item in order['items']:
        # Use actual db prices and items to calculate the price and give descriptions, rather than accepting whatever's posted by user
        itemInDb = MenuItem.query.filter_by(id=item['id']).first()
        savedOrder.price = round((savedOrder.price + itemInDb.price), 2)
        returnableItemList.append({"id": itemInDb.id, "name": itemInDb.name,
                                   "description": itemInDb.description, "price": itemInDb.price})
        # Create OrderMenuItem table items
        db.session().add(OrderMenuItem(savedOrder.id, itemInDb.id))
    db.session().commit()

    return jsonify({
        "orderId": savedOrder.id,
        "restaurantName": Restaurant.query.get(restaurantId).name,
        "name": savedOrder.name,
        "address": savedOrder.address,
        "phone": savedOrder.phone,
        "price": savedOrder.price,
        "items": returnableItemList
    })
