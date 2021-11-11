import typing


class Book:
    _name: str
    _author: str
    _publisher: str
    _publication_year: int

    def __init__(self, name: str, author: str, publisher: str, _publication_year: int):
        self._name = name
        self._author = author
        self._publisher = publisher
        self._publication_year = _publication_year

    def get_name(self):
        return self._name

    def get_author(self):
        return self._author

    def get_publisher(self):
        return self._publisher

    def get_publication_year(self):
        return self._publication_year


class BookLibrary:
    _books: typing.List[Book]

    def __init__(self):
        pass

    def add_book(self, book: Book):
        self._books.append(book)

    def remove_book(self, book: Book):
        self._books.remove(book)

    def find_by_name(self, name: str):
        for book in self._books:
            if book.get_name() == name:
                return book

        return None

    def find_by_author(self, author: str):
        for book in self._books:
            if book.get_author() == author:
                return book

        return None

    def find_by_publication_year(self, publication_year: int):
        for book in self._books:
            if book.get_publication_year() == publication_year:
                return book

        return None
