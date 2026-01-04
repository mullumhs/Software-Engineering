from book import Book
from person import Person

# TODO: Call load_books and load_members at appropriate places within the __init__ method
# TODO: Call save_books and save_members at appropriate places within the other methods

class Library:
    def __init__(self):
        self._books = []
        self._members = []

    # TODO: Implement JSON data persistence for books
    def save_books(self):
        # Save the list of books to 'books.json'
        pass

    # TODO: Implement JSON data persistence for members
    def save_members(self):
        # Save the list of members to 'members.json'
        pass

    # TODO: Load books from 'books.json'
    def load_books(self):
        # Load books from 'books.json' and recreate the book objects
        pass

    # TODO: Load members from 'members.json'
    def load_members(self):
        # Load members from 'members.json' and recreate the person objects
        pass

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self._books.append(new_book)
        print(f"Added {new_book}")

    def add_member(self, name):
        member_id = len(self._members) + 1
        new_member = Person(name, member_id)
        self._members.append(new_member)
        print(f"Added new member: {new_member}")

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

    def return_book(self, isbn):
        book = self.get_book_by_isbn(isbn)
        if book and book.is_loaned:
            book.loaned_to = None

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