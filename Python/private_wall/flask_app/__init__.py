from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "shhhhhh, this is a secret key"

bcrypt = Bcrypt(app)

DATABASE = 'private_wall'

from flask_app.controllers import controller_messages, controller_users