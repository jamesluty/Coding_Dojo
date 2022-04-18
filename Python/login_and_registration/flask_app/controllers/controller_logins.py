from flask_app import app, bcrypt
from flask import render_template, redirect, request, session
from flask_app.models.model_login import Login

@app.route("/")
def index():
    if 'uuid' in session:
        return redirect('/welcome')
    return render_template("index.html")

@app.route("/register", methods=['POST'])
def register():
    is_valid = Login.validate_input(request.form)
    if not is_valid:
        return redirect('/')

    if not Login.validate_email(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        **request.form,
        'password': pw_hash
    }

    id = Login.create_user(data)

    session['uuid'] = id

    return redirect('/welcome')

@app.route("/welcome")
def welcome():
    context = {
        'all_users': Login.get_all()
    }

    if 'uuid' in session:
        user = Login.login_user({'id': session['uuid']})
        context['user'] = user

    return render_template("welcome.html", **context)

@app.route("/login", methods=['POST'])
def login():
    is_valid = Login.validate_login(request.form)
    if not is_valid:
        return redirect('/')

    return redirect("/welcome")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")