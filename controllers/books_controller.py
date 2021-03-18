from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

books_blueprint = Blueprint('books', __name__)

@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template('books/index.html', all_books = books)

@books_blueprint.route('/books/<id>')
def book(id):
    book = book_repository.select(id)
    return render_template('books/show.html', book=book)

@books_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_book(id):
    book = book_repository.delete(id)
    return redirect('/books')

@books_blueprint.route('/books/new')
def create_book():
    authors = author_repository.select_all()
    return render_template('books/new.html', all_authors=authors)

@books_blueprint.route('/books', methods=['POST'])
def create_new_book():
    title = request.form['title']
    genre = request.form['genre']
    description = request.form['description']
    rating = request.form['rating']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, genre, description, author, rating)
    book_repository.save(book)
    return redirect('/books')

    