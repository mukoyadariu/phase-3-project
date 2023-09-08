# phase-3-project

# Book Library Command Line Interface (CLI)

The **Book Library CLI** is a command-line application that allows users to manage a library of books. Users can add books to the library, search for books based on title and author, and delete books from the library.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Database](#database)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Add a Book**: Users can add books to the library by providing book details such as title, author, genre, and publication date.

- **Search for a Book**: Users can search for books based on title and author, and the CLI will display matching books.

- **Delete a Book**: Users can delete books from the library based on title and author.

- **Interactive User Interface**: The CLI provides an interactive menu for users to easily navigate and perform actions.

## Installation

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/book-library-cli.git
   ```

2. Navigate to the project directory:
   ```
   cd book-library-cli
   ```

3. Install the required dependencies using [Pipenv](https://pipenv.pypa.io/):
   ```
   pipenv install
   ```

4. Activate the virtual environment:
   ```
   pipenv shell
   ```

## Usage

To run the Book Library CLI, use the following command from the project directory:

```
python book_library/commands.py
```

The CLI will display a menu with options for adding, searching, and deleting books.

## Commands

- **Add a Book**: Select option 1 from the menu to add a book. You will be prompted to enter the book's title, author, genre, and publication date.

- **Search for a Book**: Select option 2 from the menu to search for a book. You can enter title and author information to find matching books.

- **Delete a Book**: Select option 3 from the menu to delete a book. Enter title and author information to identify the books to delete.

## Database

The CLI uses SQLAlchemy to manage the database. By default, it uses SQLite as the database engine, which is included in the project. You can find the database file named `library.db` in the project directory.

## Testing

To run the unit tests for the CLI, use the following command:

```
python -m unittest tests/test_commands.py
```

## Contributing

Contributions to this project are welcome! If you have suggestions, bug reports, or want to add new features, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
This project was created by Dennis Darius Mukoya
