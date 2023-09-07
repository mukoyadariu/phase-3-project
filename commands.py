# book_library/commands.py
from models import Book
from database import Database

db = Database()

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    publication_date = input("Publication Date: ")

    book = Book(title, author, genre, publication_date)
    db.add_book(book)
    print(f"Added book: {book}")

def search_book():
    title = input("Title: ")
    author = input("Author: ")

    matching_books = db.search_books(title, author)
    if matching_books:
        print("Matching books:")
        for book in matching_books:
            print(book)
    else:
        print("No matching books found.")

def delete_book():
    title = input("Title: ")
    author = input("Author: ")

    if db.delete_books(title, author):
        print("Books deleted successfully.")
    else:
        print("No matching books found for deletion.")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Delete a Book")
        print("4. Exit")
        
        choice = input("Select an option (1/2/3/4): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")
