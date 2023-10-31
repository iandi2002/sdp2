# Класс, представляющий книгу в библиотеке
class Book:
    def __init__(self, title, author, borrower=None):
        self.title = title
        self.author = author
        self.borrower = borrower

    def is_borrowed(self):
        return self.borrower is not None

    def get_borrower_name(self):
        if self.is_borrowed():
            return self.borrower
        else:
            return "Книга в библиотеке"

# Класс, представляющий библиотеку
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

# Адаптер для упрощения взаимодействия библиотекаря с библиотекой
class LibrarianAdapter:
    def __init__(self, library):
        self.library = library

    def get_borrower_info(self, book_title):
        book = self.library.find_book(book_title)
        if book:
            if book.is_borrowed():
                return f"Книга '{book.title}' взята у {book.get_borrower_name()}"
            else:
                return f"Книга '{book.title}' в библиотеке"
        else:
            return f"Книга '{book_title}' не найдена в библиотеке"

if __name__ == "__main__":
    library = Library()
    book1 = Book("Война и мир", "Лев Толстой")
    book2 = Book("Преступление и наказание", "Федор Достоевский")
    library.add_book(book1)
    library.add_book(book2)

    librarian = LibrarianAdapter(library)

    while True:
        print("Что хотите сделать?")
        print("1. Узнать информацию о книге")
        print("2. Выйти")
        choice = input("Ваш выбор: ")

        if choice == "1":
            book_title = input("Введите название книги: ")
            info = librarian.get_borrower_info(book_title)
            print(info)
        elif choice == "2":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
