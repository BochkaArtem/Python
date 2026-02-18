class Book:
    def __init__(self, id, name, pages):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=None):
        """
        Конструктор класса Library
        :param books: список книг (по умолчанию None - пустая библиотека)
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Возвращает идентификатор для добавления новой книги в библиотеку
        Если книг нет, возвращает 1
        Если книги есть, возвращает id последней книги + 1
        """
        if not self.books:  # если список книг пуст
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, id):
        """
        Возвращает индекс книги в списке по её id
        :param id: идентификатор книги
        :return: индекс книги в списке
        :raises ValueError: если книги с таким id не существует
        """
        for index, book in enumerate(self.books):
            if book.id == id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book


# TODO написать класс Library


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
