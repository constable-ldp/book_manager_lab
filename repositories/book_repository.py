from db.run_sql import run_sql
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository

def save(book):
    sql = """INSERT INTO books (title, genre, description, rating, author_id)
             VALUES (%s, %s, %s, %s, %s)
             RETURNING *"""
    values = [book.title, book.genre, book.description, book.rating, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author_id = author_repository.select(row['author_id'])
        book = Book(row['title'], row['genre'], row['description'], author_id, row['rating'])
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        author_id = author_repository.select(row['author_id'])
        book = Book(result['title'], result['genre'], result['description'], author_id, result['rating'])
    return book

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql)
