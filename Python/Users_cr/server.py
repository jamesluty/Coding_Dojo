from flask import Flask, render_template, request, redirect

# import the class from friend.py
from users import Users
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    user = Users.get_all()
    # print(user)
    return render_template("index.html", all_users=user)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route('/create_user', methods=["POST"])
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
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

