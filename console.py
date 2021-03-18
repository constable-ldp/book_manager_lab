from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author1 = Author('Joanne', 'Rowling')
author_repository.save(author1)
author2 = Author('Philip', 'Pullman')
author_repository.save(author2)

book1 = Book('Harry Potter 1', 'Fantasy', 'Young boy goes to wizzard school', author1)
book_repository.save(book1)
book2 = Book('Northern Lights', 'Fantasy', 'Young girl travels the world with deamon', author2)
book_repository.save(book2)
