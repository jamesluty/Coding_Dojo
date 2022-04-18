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

    @classmethod
    def delete_email(cls, data):
        print(data)
        query = "DELETE FROM emails WHERE id = %(id)s;"
        print(query)
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_email(data):
        query = "SELECT * FROM emails"
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

