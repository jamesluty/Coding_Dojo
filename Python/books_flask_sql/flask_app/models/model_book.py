# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_author

DATABASE = 'books_schema'

class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

    @classmethod
    def get_books(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL(DATABASE).query_db(query)

        books = []

        for book in results:
            books.append(cls(book))

        return books

    @classmethod
    def add_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUE (%(title)s, %(num_of_pages)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_favorites_books(cls, data:dict):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        book = cls(results[0])
        

        for item in results:
            authors_data = {
                'id': item['authors.id'],
                'name': item['name'],
                'created_at': item['authors.created_at'],
                'updated_at': item['authors.updated_at']
            }
            book.books.append(model_author.Author(authors_data))

        print(book)

        return book