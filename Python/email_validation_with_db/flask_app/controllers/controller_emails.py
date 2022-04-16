from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.model_email import Email

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validate", methods=['POST'])
def validate_email():
    if not Email.validate_email(request.form):
        return redirect('/')

    data = {
        'email': request.form['email']
    }

    Email.add_email(data)

    return redirect('/success')

@app.route("/success")
def success():
    emails = Email.show_emails()
    return render_template("success.html", all_emails=emails)