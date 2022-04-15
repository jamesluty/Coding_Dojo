from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojos
from flask_app.models.ninja import Ninja

@app.route("/dojos")
def index():
    # call the get all classmethod to get all friends
    dojos = Dojos.get_dojo()
    return render_template("index.html", all_dojos=dojos)

@app.route("/dojo/<int:id>")
def show_dojo(id):
    ninjas = Dojos.get_one({'id':id})
    return render_template("show_dojo.html", dojo=ninjas)
    

@app.route("/create/dojo", methods=['POST'])
def create_dojo():
    data = {
        'location': request.form['location'],
    }
    Dojos.add_dojo(data)
    return redirect('/dojos')