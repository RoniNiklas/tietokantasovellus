from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from flask_bcrypt import generate_password_hash
from flask_bcrypt import check_password_hash

from application import app, db
from application.models.user import User
from application.models.restaurant import Restaurant
from application.forms.loginForm import LoginForm
from application.forms.signupForm import SignUpForm


@app.route("/login", methods=["GET", "POST"])
def auth_login():

    if request.method == "GET":
        return render_template("auth/loginForm.html", loginform=LoginForm(), signupform=SignUpForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit
    user = User.query.filter_by(
        username=form.username.data).first()

    if not user:
        return render_template("auth/loginForm.html", loginform=form, signupform=SignUpForm(),
                               error="Invalid username or password")

    if not check_password_hash(user.password, form.password.data):
        return render_template("auth/loginForm.html", loginform=form, signupform=SignUpForm(),
                               error="Invalid username or password")
    login_user(user)
    return redirect('/manager/orders/' + str(user.restaurantId))


@app.route("/signup", methods=["GET", "POST"])
def auth_signup():

    if request.method == "GET":
        return render_template("auth/loginForm.html", loginform=LoginForm(), signupform=SignUpForm())

    signupform = SignUpForm(request.form)

    if User.query.filter_by(username=signupform.newusername.data).first() != None:
        return render_template("auth/loginForm.html", error="That username is already taken", loginform=LoginForm(), signupform=signupform)

    if Restaurant.query.filter_by(name=signupform.restaurantname.data).first() != None:
        return render_template("auth/loginForm.html", error="That name for a restaurant is already taken", loginform=LoginForm(), signupform=signupform)

    if request.method == "POST" and signupform.validate():
        savedRestaurant = Restaurant(signupform.restaurantname.data, signupform.restaurantdescription.data,
                                     signupform.restaurantaddress.data, signupform.restaurantphone.data)
        db.session().add(savedRestaurant)
        db.session().commit()
        savedUser = User(signupform.name.data, signupform.newusername.data,
                         generate_password_hash(signupform.newpassword.data).decode("utf-8"), savedRestaurant.id)

        db.session().add(savedUser)
        db.session().commit()
        login_user(savedUser)
        return redirect('/manager/menu/' + str(savedUser.restaurantId))
    return render_template("auth/loginForm.html", loginform=LoginForm(), signupform=signupform)


@app.route("/logout")
def auth_logout():
    logout_user()
    return redirect('/')
