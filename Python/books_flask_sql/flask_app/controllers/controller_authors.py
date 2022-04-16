import re
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.model_author import Author
from flask_app.models.model_book import Book

@app.route("/authors")
def index():
    authors = Author.get_authors()
    return render_template("index.html", all_authors=authors)

@app.route("/create/author", methods=['POST'])
def create_author():
    data = {
        'name': request.form['name']
    }
    Author.add_author(data)
    return redirect("/authors")

@app.route("/author/<int:id>")
def show_author(id):
    author = Author.get_favorites_authors({'id':id})
    books = Book.get_books()
    return render_template('show_author.html', all_authors=author, all_books=books)

@app.route("/author/add", methods=['POST'])
def add_favorite():
    book = Book.add_book()
    return redirect('/author/<int:id>')
