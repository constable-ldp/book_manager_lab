import unittest
from models.author import Author

class TestAuthor(unittest.TestCase):
    
    def setUp(self):
        self.author = Author('J.K', 'Rowling')

    def test_author_has_first_name(self):
        self.assertEqual('J.K', self.author.first_name)
    
    def test_author_has_last_name(self):
        self.assertEqual('Rowling', self.author.last_name)

    def test_author_id_starts_none(self):
        self.assertEqual(None, self.author.id)