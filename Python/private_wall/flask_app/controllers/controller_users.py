from flask_app import app, bcrypt
from flask import render_template, redirect, request, session
from flask_app.models.model_user import User
from flask_app.models.model_message import Message

@app.route("/")
def index():
    if 'uuid' in session:
        return redirect('/wall')
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

@app.route("/login", methods=['POST'])
def login():
    is_valid = User.validate_login(request.form)
    if not is_valid:
        return redirect('/')

    return redirect("/wall")

@app.route('/send/message/<int:recepient>', methods=['POST'])
def send_message(recepient):
    data = {
        **request.form,
        'id': session['uuid'],
        'recepient': recepient
    }

    Message.send_message_to_user(data)

    return redirect('/wall')

@app.route("/logout")
def logout():
    session.pop('uuid')
    return redirect("/")