from person import Person

class Book:
    def __init__(self, title, author, isbn, is_loaned=False, loaned_to=None):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._loaned_to = loaned_to

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def is_loaned(self):
        return self._loaned_to

    @property
    def loaned_to(self):
        return self._loaned_to

    def loan(self, person):
        self._loaned_to = person

    def return_book(self):
        if self.is_loaned:
            self._loaned_to = None

    def __repr__(self):
        return f"'{self.title}' by {self.author}, ISBN: {self.isbn}"