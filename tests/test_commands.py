import unittest
from unittest.mock import patch
from io import StringIO

from book_library.commands import add_book, search_book, delete_book
from book_library.models import Book
from book_library.database import Database

class TestBookLibraryCLI(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def test_add_book(self):
        with patch("builtins.input", side_effect=["Title", "Author", "Genre", "Publication Date"]):
            add_book()
        self.assertEqual(len(self.db.books), 1)
        self.assertEqual(str(self.db.books[0]), "Title: Title, Author: Author")

    def test_search_book(self):
        book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "1925-04-10")
        book2 = Book("Gatsby's Dream", "Jane Doe", "Mystery", "1930-01-15")

        self.db.add_book(book1)
        self.db.add_book(book2)

        with patch("builtins.input", side_effect=["Gatsby", ""]):
            with patch("sys.stdout", new_callable=StringIO) as mock_output:
                search_book()

        output = mock_output.getvalue()
        self.assertIn("Matching books:", output)
        self.assertIn("Title: The Great Gatsby, Author: F. Scott Fitzgerald", output)
        self.assertIn("Title: Gatsby's Dream, Author: Jane Doe", output)
        self.assertNotIn("No matching books found.", output)

    def test_delete_book(self):
        book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "1925-04-10")
        book2 = Book("Gatsby's Dream", "Jane Doe", "Mystery", "1930-01-15")

        self.db.add_book(book1)
        self.db.add_book(book2)

        with patch("builtins.input", side_effect=["Gatsby", "", "yes"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_output:
                delete_book()

        output = mock_output.getvalue()
        self.assertIn("Matching books for deletion:", output)
        self.assertIn("Title: The Great Gatsby, Author: F. Scott Fitzgerald", output)
        self.assertIn("Title: Gatsby's Dream, Author: Jane Doe", output)
        self.assertIn("Books deleted successfully.", output)
