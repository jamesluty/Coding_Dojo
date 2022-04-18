from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Login:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)

        users = []

        for item in results:
            users.append(item)

        return users

    @classmethod
    def login_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        
        if results:
            user = cls(results[0])
            return user

        return False

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        if results:
            user = cls(results[0])
            return user

        return False

    @staticmethod
    def validate_email(data):
        query = "SELECT * FROM users"
        results = connectToMySQL(DATABASE).query_db(query)
        is_valid = True

        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", "err_email")
            is_valid = False

        emails = []

        for item in results:
            emails.append(item['email'])

        for email in emails:
            if data['email'] == email:
                flash("Email has already been used", "err_email")
                is_valid = False
                break

        return is_valid

    @staticmethod
    def validate_login(form_data):
        is_valid = True
        if len(form_data['email']) <= 0:
            flash("Email must be included!", 'err_email_login')
            is_valid = False
        elif not EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email address!", "err_email_login")
            is_valid = False

        if len(form_data['password']) <= 8:
            flash("Password must be at least 8 characters!", 'err_password_login')
            is_valid = False
        else:
            potential_user = Login.get_one_by_email({'email': form_data['email']})
            if not bcrypt.check_password_hash(potential_user.password, form_data['password']):
                flash("Invalid credentials!", 'err_password_login')
                is_valid = False
            else:
                session['uuid'] = potential_user.id

        return is_valid

    @staticmethod
    def validate_input(form_data):
        is_valid = True

        if len(form_data['first_name']) <= 0:
            flash("First name is required!", 'err_first_name')
            is_valid = False

        if len(form_data['last_name']) <= 0:
            flash("Last name is required!", 'err_last_name')
            is_valid = False

        if len(form_data['email']) <= 0:
            flash("Email is required!", 'err_email')
            is_valid = False

        if len(form_data['password']) <= 8:
            flash("Password must be at least 8 characters!", 'err_password')
            is_valid = False
        
        if len(form_data['confirm_password']) <= 8:
            flash("Password must be at least 8 characters!", 'err_confirm_password')
            is_valid = False

        if form_data['password'] != form_data['confirm_password']:
            flash("Passwords must be the same!", 'err_confirm_password')
            is_valid = False

        return is_valid
