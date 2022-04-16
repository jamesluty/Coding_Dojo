# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'books_schema'

class Favorite:
    def __init__( self , data ):
        self.id = data['id']
        self.author_id = data['author_id']
        self.book_id = data['book_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']