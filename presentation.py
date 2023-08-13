from domain import Book
from data import BookStore

if __name__ == "__main__":
    book_store = BookStore()

    book1 = Book("1", "Clean Code", "Robert C. Martin", 34.99)
    book2 = Book("2", "Effective Java", "Joshua Bloch", 29.99)
    book_store.add_book(book1)
    book_store.add_book(book2)

    all_books = book_store.get_all_books()
    for book in all_books:
        print(f"Книга: {book.title}, Автор: {book.author}, Цена: ${str(book.price)}")
