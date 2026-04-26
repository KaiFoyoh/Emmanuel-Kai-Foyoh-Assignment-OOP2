import asyncio
from typing import List, Dict, Optional

books: List[Dict] = [
    {"id": 1, "title": "Python Basics", "author": "John Smith", "category": "Programming", "available": True},
    {"id": 2, "title": "Database Systems", "author": "Mary Cole", "category": "ICT", "available": True},
    {"id": 3, "title": "Networking Essentials", "author": "James Brown", "category": "Networking", "available": True}
]

borrowed_books: List[Dict] = []


def get_books() -> List[Dict]:
    return books


def search_books(keyword: str) -> List[Dict]:
    keyword = keyword.lower()
    return [
        book for book in books
        if keyword in book["title"].lower()
        or keyword in book["author"].lower()
        or keyword in book["category"].lower()
    ]


async def borrow_book(user: str, book_id: int) -> str:
    await asyncio.sleep(1)

    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                borrowed_books.append({"user": user, "book": book["title"], "days_overdue": 0})
                return f"{user} successfully borrowed {book['title']}."
            return f"{book['title']} is already borrowed."

    return "Book not found."


async def return_book(user: str, book_title: str) -> str:
    await asyncio.sleep(1)

    for record in borrowed_books:
        if record["user"] == user and record["book"].lower() == book_title.lower():
            borrowed_books.remove(record)

            for book in books:
                if book["title"].lower() == book_title.lower():
                    book["available"] = True

            return f"{user} successfully returned {book_title}."

    return "Borrow record not found."


def check_overdue() -> List[Dict]:
    overdue_list = []

    for record in borrowed_books:
        if record["days_overdue"] > 0:
            fine = record["days_overdue"] * 5
            overdue_list.append({
                "user": record["user"],
                "book": record["book"],
                "days_overdue": record["days_overdue"],
                "fine": fine
            })

    return overdue_list


async def main() -> None:
    print("All Books:")
    print(get_books())

    print("\nSearch Result:")
    print(search_books("Python"))

    print("\nBorrowing Books:")
    results = await asyncio.gather(
        borrow_book("Natashia", 1),
        borrow_book("Aminata", 2)
    )
    print(results)

    print("\nReturning Book:")
    print(await return_book("Natashia", "Python Basics"))

    print("\nCurrent Books:")
    print(get_books())


asyncio.run(main())