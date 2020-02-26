from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.models.order import Order
from application.models.menuItem import MenuItem


@app.route("/manager/orders/")
def goToLogin():
    return redirect("/login")


@app.route("/manager/orders/<browsedRestaurantId>")
@login_required
def getOrders(browsedRestaurantId):
    
    if str(current_user.restaurantId) != browsedRestaurantId:
        return render_template("error.html", error="You can only browse your own restaurant's orders.")

    foundOrders = Order.query.filter_by(restaurantId=browsedRestaurantId).all()
    for order in foundOrders:
        order.returnableItems = []
        for item in order.items:
            order.returnableItems.append(
                MenuItem.query.filter_by(id=item.itemId).first().name)
    return render_template("owner/orders.html", orders=foundOrders, restaurantId=browsedRestaurantId)
