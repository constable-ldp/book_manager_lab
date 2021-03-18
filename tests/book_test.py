import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    
    def setUp(self):
        self.book = Book('Harry Potter', 'Fantasy', 'Wizard goes to school', 'J.K Rowling')
    
    
    def test_book_has_title(self):
        self.assertEqual('Harry Potter', self.book.title)
        
        
    def test_book_has_genre(self):
        self.assertEqual('Fantasy', self.book.genre)
       
        
    def test_book_has_description(self):
        self.assertEqual('Wizard goes to school', self.book.description)


    def test_book_has_author(self):
        self.assertEqual('J.K Rowling', self.book.author)
    
    
    def test_book_rating_starts_0(self):
        self.assertEqual(0, self.book.rating)


    def test_book_id_starts_none(self):
        self.assertEqual(None, self.book.id)
    
    def test_can_change_rating(self):
        self.book.update_rating(5)
        self.assertEqual(5, self.book.rating)