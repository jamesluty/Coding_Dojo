# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

DATABASE = 'dojos_and_ninjas_schema'

class Dojos:
    def __init__( self , data ):
        self.id = data['id']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_dojo(cls):
        query = "SELECT * FROM dojos;"

        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)

        # Create an empty list to append our instances of friends
        dojos = []

        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )

        return dojos

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojo_id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls(results[0])
        # print(dojo)

        for row in results:
            ninja_data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
                'dojo_id': row['dojo_id']
            }
            ninja_actual = ninja.Ninja(ninja_data)
            dojo.ninjas.append(ninja_actual)
            # results.dojo.append(ninja_actual)

        return dojo

    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (location) VALUE (%(location)s);"
        return connectToMySQL(DATABASE).query_db(query, data)