from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojos
from flask_app.models.ninja import Ninja

@app.route("/ninjas")
def ninjas():
    # call the get all classmethod to get all friends
    dojos = Dojos.get_dojo()
    return render_template("ninjas.html", all_dojos=dojos)

@app.route("/create/ninja", methods=['POST'])
def create_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Ninja.add_ninja(data)
    return redirect('/dojos')