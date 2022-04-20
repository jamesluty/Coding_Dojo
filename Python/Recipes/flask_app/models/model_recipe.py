from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session
from flask_app.models import model_user
from flask_app.models import model_recipe


class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_created = data['date_created']
        self.time = data['time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.recipes = []

    @classmethod
    def add_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_created, time, user_id) VALUES ( %(name)s, %(description)s, %(instructions)s, %(date)s, %(time)s, %(user_id)s );"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_recipes(cls, data):
        query = "SELECT * FROM users JOIN recipes ON recipes.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        user = cls(results[0])

        if results:
            for item in results:
                recipe_data = {
                    'id': item['recipes.id'],
                    'name': item['name'],
                    'description': item['description'],
                    'instructions': item['instructions'],
                    'date_created': item['date_created'],
                    'time': item['time'],
                    'created_at': item['recipes.created_at'],
                    'updated_at': item['recipes.updated_at'],
                    'user_id': item['user_id'],
                }
                temp_recipe = Recipe(recipe_data)
                # temp_recipe.recipes = model_recipe.Recipe(item)
                user.recipes.append(temp_recipe)

        return user

    @classmethod
    def show_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        if results:
            recipe = cls(results[0])
            return recipe

        return False

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_created=%(date)s, time=%(time)s WHERE id = %(recipe_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        print("test")
        return connectToMySQL(DATABASE).query_db(query, data)