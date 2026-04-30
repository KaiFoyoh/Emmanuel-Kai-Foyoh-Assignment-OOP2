# Emmanuel-Kai-Foyoh-Assignment-OOP2
# Basic Library API Simulation Using Python

## Project Description

This project is a basic digital library API simulation created for the Object-Oriented Programming 2 assignment. The system allows users to search for books, borrow books, return books, and check overdue books with fines.

This version does not use FastAPI. Instead, it uses normal Python functions to simulate API endpoints and asynchronous programming with `async` and `await` to show how multiple users can borrow or return books at the same time.

## Features

- View all available books
- Search books by title, author, or category
- Borrow books
- Return borrowed books
- Check overdue books and fines
- Support multiple users using asynchronous programming
- Uses type annotations for better code structure

## Simulated API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/books` | Displays all books in the library |
| GET | `/books/search` | Searches for books by title, author, or category |
| POST | `/borrow` | Allows a user to borrow a book |
| POST | `/return` | Allows a user to return a borrowed book |
| GET | `/overdue` | Displays overdue books and calculates fines |

## Technologies Used

- Python
- Asyncio
- GitHub

## How to Run the Project

1. Make sure Python is installed on your computer.

2. Clone the repository:

```bash
git clone your-repository-link

	3.	Open the project folder:

cd your-project-folder

	4.	Run the Python file:

assignment.py

Example Output

All Books:
[{'id': 1, 'title': 'Python Basics', 'author': 'John Smith', 'category': 'Programming', 'available': True}]

Search Result:
[{'id': 1, 'title': 'Python Basics', 'author': 'John Smith', 'category': 'Programming', 'available': True}]

Borrowing Books:
['Natashia successfully borrowed Python Basics.', 'Aminata successfully borrowed Database Systems.']

Returning Book:
Natashia successfully returned Python Basics.

Project Files

library-api-simulation/
│
├── library_api.py
├── README.md
└── .gitignore

Importance of the Project

This project shows how a simple library system can improve efficiency by reducing manual work. Instead of staff searching records by hand, the system allows books to be searched, borrowed, returned, and tracked easily.

It also supports Sustainable Development Goal 4, which focuses on quality education. A digital library system helps students and staff access learning materials more easily and improves the management of educational resources.

Challenges Faced

Some challenges faced during the project included designing the correct structure for book data, handling multiple users borrowing or returning books at the same time, and organizing the information in a JSON-like format.

Another challenge was making sure the borrow and return functions correctly updated book availability.

Future Improvement

If the library expands, the system can be improved by adding a database to store books and user records permanently. A login system can also be added so each student or staff member can have an account.

Author

Emmanuel Kai Foyoh

Course

Object-Oriented Programming 2

Institution

Limkokwing University of Creative Technology, Sierra Leone
