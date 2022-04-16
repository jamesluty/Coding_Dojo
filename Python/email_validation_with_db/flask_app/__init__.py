from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"

DATABASE = 'email_validation_schema'

from flask_app.controllers import controller_emails