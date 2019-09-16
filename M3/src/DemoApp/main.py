from DemoApp import app
from flask import render_template, url_for, flash, Markup, redirect, request, make_response
from DemoApp.forms import *




@app.route("/")
@app.route("/home")
def home():
    return render_template('main.html')



@app.route("/load", methods=['GET', 'POST'])
def load():
    loadform = LoadForm()
    if loadform.search.data and loadform.validate_on_submit():
        name = loadform.name.data
        type = loadform.type.data
        return render_template("game.html", form = loadform)
    return render_template("load.html",  form=loadform)


@app.route("/game", methods=['GET', 'POST'])
def game():
    return render_template("game.html")
