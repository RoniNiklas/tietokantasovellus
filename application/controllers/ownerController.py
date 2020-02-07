from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from application.models.user import User
from application.forms.loginForm import LoginForm


@app.route("/manager/")
def goToLoginAgain():
    return redirect('/login')


@app.route("/manager/<restaurantId>")
def managerMain(restaurantId):
    return render_template("owner/main.html", restaurantId=restaurantId)
