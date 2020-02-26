from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.models.menuItem import MenuItem
from application.forms.newItemForm import NewItemForm


def addToDb(restaurantId, name, description, price):
    db.session.add(MenuItem(restaurantId, name,
                            description, price, True))
    db.session.commit()


def deactivateItem(oldItemId):
    oldItem = MenuItem.query.get(oldItemId)
    oldItem.active = False
    db.session.commit()


@app.route("/manager/menu/")
def goToLogin2():
    return redirect("/login")


@app.route("/manager/menu/<browsedRestaurantId>", methods=["GET", "POST"])
@login_required
def getMenuManager(browsedRestaurantId):

    if str(current_user.restaurantId) != browsedRestaurantId:
        return render_template("error.html", error="You can't edit other people's menu items.")

    form = NewItemForm(request.form)

    if request.method == "POST" and form.validate():
        addToDb(browsedRestaurantId, form.name.data,
                form.description.data, form.price.data)
        return redirect('/manager/menu/' + browsedRestaurantId)

    foundItems = MenuItem.query.filter_by(
        restaurantId=browsedRestaurantId, active=True).all()

    return render_template("owner/menu.html", form=form, items=foundItems, restaurantId=browsedRestaurantId)


@app.route("/manager/menu/<browsedRestaurantId>/edit/<itemId>", methods=["GET", "POST"])
@login_required
def itemEditor(browsedRestaurantId, itemId):

    if str(current_user.restaurantId) != browsedRestaurantId:
        return render_template("error.html", error="You can't edit other people's menu items.")

    foundItem = MenuItem.query.get(itemId)

    if current_user.restaurantId != foundItem.restaurantId:
        return render_template("error.html", error="You can't edit other people's menu items.")

    form = NewItemForm(request.form)

    if request.method == "POST":
        if form.validate():
            deactivateItem(foundItem.id)
            addToDb(browsedRestaurantId, form.name.data,
                    form.description.data, form.price.data)
            return redirect('/manager/menu/' + browsedRestaurantId)
        return render_template("owner/editItem.html", form=form, item=foundItem, restaurantId=browsedRestaurantId)

    form = NewItemForm()
    form.price.data = foundItem.price
    form.description.data = foundItem.description
    form.name.data = foundItem.name

    return render_template("owner/editItem.html", form=form, item=foundItem, restaurantId=browsedRestaurantId)


@app.route("/manager/menu/<browsedRestaurantId>/delete/<itemId>", methods=["POST"])
@login_required
def deleteItem(browsedRestaurantId, itemId):
    if str(current_user.restaurantId) != browsedRestaurantId:
        return render_template("error.html", error="You can't delete other people's menu items.")

    foundItem = MenuItem.query.filter_by(id=itemId).first()
    if current_user.restaurantId != foundItem.restaurantId:
        return render_template("error.html", error="You can't delete other people's menu items.")
    foundItem.active = False
    db.session.commit()
    return redirect("/manager/menu/" + browsedRestaurantId)
