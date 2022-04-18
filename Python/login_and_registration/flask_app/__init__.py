from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "shhhhhh, this is a secret key"

bcrypt = Bcrypt(app)

DATABASE = 'login_and_registration_schema'

from flask_app.controllers import controller_logins