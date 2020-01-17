from application import app
from flask import Flask, render_template

@app.route("/")
def front():
    return render_template("index.html")