# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Survey:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.course = data['course']
        self.language = data['language']
        self.comment = data['comment']
        self.checkbox = data['checkbox']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_survey(cls, data):
        query = "INSERT INTO dojos (name, location, course, language, comment, checkbox) VALUES (%(name)s, %(location)s, %(course)s, %(language)s, %(comment)s, %(checkbox)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_last(cls):
        query = "SELECT * FROM dojos ORDER BY id DESC LIMIT 1"
        results = connectToMySQL(DATABASE).query_db(query)
        
        survey = []

        for item in results:
            survey.append(cls(item))

        print(survey)

        return survey

    @staticmethod
    def validate_survey(form_data):
        is_valid = True

        if len(form_data['name']) <= 0:
            flash("Name is required!", 'err_name')
            is_valid = False

        if len(form_data['location']) <= 0:
            flash("Location is required!", 'err_location')
            is_valid = False

        if form_data['course'] != 'Full Time' or form_data['course'] != 'Part Time':
            flash("Course is required!", 'err_course')
            is_valid = False

        if form_data['language'] != 'Python' or form_data['language'] != 'MERN' or form_data['language'] != 'C#' or form_data['language'] != 'JAVA':
            flash("Language is required!", 'err_language')
            is_valid = False

        return is_valid