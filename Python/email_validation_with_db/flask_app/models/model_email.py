import email
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def show_emails(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)

        email = []

        for item in results:
            email.append(cls(item))

        return email

    @classmethod
    def add_email(cls, data:dict):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_email(data):
        is_valid = True

        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", "err_email")
            is_valid = False

        return is_valid

