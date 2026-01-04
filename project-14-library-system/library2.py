import json
from book import Book
from person import Person

class Library:
    def __init__(self):
        self._books = []
        self._members = []
        self.load_books()
        self.load_members()

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self._books.append(new_book)
        self.save_books()

    def add_member(self, name):
        member_id = len(self._members) + 1
        new_member = Person(name, member_id)
        self._members.append(new_member)
        self.save_members()

    def list_books(self):
        for book in self._books:
            if book.is_loaned:
                print(f"{book} - Loaned to {self.get_member_details(book.loaned_to)}")
            else:
                print(f"{book} - Available")

    def list_members(self):
        for member in self._members:
            print(member)
            self.print_member_loans(member)

    def print_member_loans(self, member):
        loans = [self.get_book_details(book.isbn) for book in self._books if book.loaned_to == member.member_id]
        for loan in loans:
            print(f" --> {loan}")

    def loan_book(self, isbn, member_id):
        book = self.get_book_by_isbn(isbn)
        member = self.get_member_by_id(member_id)
        if book and member and not book.is_loaned:
            book.loan(member.member_id)
            self.save_books()

    def return_book(self, isbn):
        book = self.get_book_by_isbn(isbn)
        if book and book.is_loaned:
            book.return_book()
            self.save_books()

    def view_loans(self):
        for book in self._books:
            if book.is_loaned:
                print(f"{book} - Loaned to {self.get_member_details(book.loaned_to)}")

    def get_book_by_isbn(self, isbn):
        return next((book for book in self._books if book.isbn == isbn), None)

    def get_member_by_id(self, member_id):
        return next((member for member in self._members if member.member_id == member_id), None)

    def get_book_details(self, isbn):
        book = self.get_book_by_isbn(isbn)
        return str(book)

    def get_member_details(self, member_id):
        member = self.get_member_by_id(member_id)
        return str(member)

    def save_books(self):
        with open('books.json', 'w') as f:
            json.dump([book.__dict__ for book in self._books], f, indent=4)

    def save_members(self):
        with open('members.json', 'w') as f:
            json.dump([member.__dict__ for member in self._members], f, indent=4)

    def load_books(self):
        try:
            with open('books.json', 'r') as f:
                books_data = json.load(f)
                self._books = [Book(**book) for book in books_data]
        except FileNotFoundError:
            self._books = []

    def load_members(self):
        try:
            with open('members.json', 'r') as f:
                members_data = json.load(f)
                self._members = [Person(**member) for member in members_data]
        except FileNotFoundError:
            self._members = []