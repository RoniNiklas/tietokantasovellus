from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
  
from application import app
from application.models.user import User
from application.forms.loginForm import LoginForm

@app.route("/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginForm.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginForm.html", form = form,
                                error = "No such username or password")


    login_user(user)
    return redirect('/manager/' + str(user.restaurantId))   

@app.route("/logout")
def auth_logout():
    logout_user()
    return redirect('/login') 