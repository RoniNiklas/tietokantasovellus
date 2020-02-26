from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.forms.restaurantInfoForm import restaurantInfoForm

from application.models.restaurant import Restaurant


@app.route("/manager/")
def goToLoginAgain():
    return redirect('/login')


@app.route("/manager/info/<browsedRestaurantId>", methods=["GET", "POST"])
@login_required
def managerMain(browsedRestaurantId):

    if str(current_user.restaurantId) != browsedRestaurantId:
        return render_template("error.html", error="You can't manage other people's restaurants.")

    restaurant = Restaurant.query.filter_by(
        id=browsedRestaurantId).first()

    form = restaurantInfoForm(request.form)

    if request.method == "POST" and form.validate():
        restaurant.name = form.name.data
        restaurant.address = form.address.data
        restaurant.description = form.description.data
        restaurant.phone = form.phone.data
        db.session.commit()
        return redirect('/manager/info/' + browsedRestaurantId)

    form.address.data = restaurant.address
    form.description.data = restaurant.description
    form.name.data = restaurant.name
    form.phone.data = restaurant.phone

    return render_template("owner/info.html", form=form, restaurantId=browsedRestaurantId)


@app.route("/manager/delete/<browsedRestaurantId>", methods=["POST"])
@login_required
def deleteRestaurant(browsedRestaurantId):

    if str(current_user.restaurantId) != browsedRestaurantId:
        return render_template("error.html", error="You can't delete other people's restaurants.")

    restaurant = Restaurant.query.filter_by(
        id=browsedRestaurantId).first()

    db.session.delete(restaurant)
    db.session.commit()
    return redirect('/login')
