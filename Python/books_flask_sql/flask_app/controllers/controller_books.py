from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.model_book import Book
from flask_app.models.model_author import Author

@app.route("/books")
def books():
    books = Book.get_books()
    return render_template("books.html", all_books=books)

@app.route("/create/book", methods=['POST'])
def create_book():
    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    Book.add_book(data)
    return redirect("/books")

@app.route("/books/<int:id>")
def show_book(id):
    book = Book.get_favorites_books({'id':id})
    author = Author.get_authors()
    return render_template('show_books.html', all_authors=author, all_books=book)