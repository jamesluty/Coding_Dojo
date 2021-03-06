from flask_app import app, bcrypt
from flask import render_template, redirect, request, session
from flask_app.models.model_login import User

@app.route("/")
def index():
    if 'uuid' in session:
        return redirect('/welcome')
    return render_template("index.html")

@app.route("/register", methods=['POST'])
def register():
    is_valid = User.validate_input(request.form)
    if not is_valid:
        return redirect('/')

    if not User.validate_email(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        **request.form,
        'password': pw_hash
    }

    id = User.create_user(data)

    session['uuid'] = id

    return redirect('/wall')

@app.route("/wall")
def welcome():
    context = {
        'all_users': User.get_all()
    }

    if 'uuid' in session:
        user = User.login_user({'id': session['uuid']})
        context['user'] = user
    print(context)
    return render_template("wall.html", **context)

@app.route("/login", methods=['POST'])
def login():
    is_valid = User.validate_login(request.form)
    if not is_valid:
        return redirect('/')

    return redirect("/wall")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")