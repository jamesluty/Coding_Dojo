from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import Users

@app.route("/user")
def index():
    # call the get all classmethod to get all friends
    user = Users.get_all()
    # print(user)
    return render_template("index.html", all_users=user)

@app.route("/user/add")
def create():
    return render_template("create.html")

@app.route('/create', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Users.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/user')

@app.route('/user/show/<int:id>')
def show_user(id):
    user = Users.get_one({'id':id})
    return render_template('show_user.html', user=user)

@app.route('/user/edit/<int:id>')
def edit_user(id):
    user = Users.get_one({'id':id})
    return render_template('edit_user.html', user=user)

@app.route('/user/update', methods=['POST'])
def update():
    data = {
        "id": request.form['id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    Users.update(data)
    return redirect('/user')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    Users.destroy({'id':id})

    return redirect('/user')