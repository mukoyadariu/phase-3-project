# book_library/database.py
class Database:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_books(self, title="", author=""):
        matching_books = []
        for book in self.books:
            if title.lower() in book.title.lower() and author.lower() in book.author.lower():
                matching_books.append(book)
        return matching_books

    def delete_books(self, title="", author=""):
        books_to_delete = self.search_books(title, author)
        if not books_to_delete:
            return False

        print("Matching books for deletion:")
        for book in books_to_delete:
            print(book)

        confirmation = input("Do you want to delete these books? (yes/no) [no]: ").strip().lower()
        if confirmation == "yes":
            self.books = [book for book in self.books if book not in books_to_delete]
            return True
        return False
