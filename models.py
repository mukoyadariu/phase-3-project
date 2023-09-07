# book_library/models.py
class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"
