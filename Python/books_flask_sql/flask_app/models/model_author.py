# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_book

DATABASE = 'books_schema'

class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []

    @classmethod
    def get_authors(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL(DATABASE).query_db(query)

        authors = []

        for author in results:
            authors.append(cls(author))

        return authors

    @classmethod
    def add_author(cls, data):
        query = "INSERT INTO authors (name) VALUE (%(name)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_favorites_authors(cls, data:dict):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        author = cls(results[0])
        

        for item in results:
            books_data = {
                'id': item['books.id'],
                'title': item['title'],
                'num_of_pages': item['num_of_pages'],
                'created_at': item['books.created_at'],
                'updated_at': item['books.updated_at']
            }
            author.authors.append(model_book.Book(books_data))

        print(author)

        return author

    # @classmethod
    # def get_not_favorites(cls, date):
    #     query = "SELECT * FROM authors JOIN favorites ON favorites.author_id = authors.id JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"

    # @classmethod
    # def add_book(cls, data):
    #     query = "INSERT INTO authors (title, num_of_pages) VALUES "

