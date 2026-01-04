"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                            LIBRARY SYSTEM
---------------------------------------------------------------------------------------------------
- File Name: library_system.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Refactor the existing library system to implement data persistence using JSON.
               This will involve understanding and modifying the the Book, Person, and Library files. 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from book import Book
from person import Person
from library import Library

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. List Books")
        print("4. List Members")
        print("5. Loan Book")
        print("6. Return Book")
        print("7. View Current Loans")
        print("8. Exit")
        choice = input("Enter option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)
        elif choice == '2':
            name = input("Enter member's name: ")
            library.add_member(name)
        elif choice == '3':
            library.list_books()
        elif choice == '4':
            library.list_members()
        elif choice == '5':
            isbn = input("Enter ISBN of the book to loan: ")
            member_id = int(input("Enter member ID: "))
            library.loan_book(isbn, member_id)
        elif choice == '6':
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(isbn)
        elif choice == '7':
            library.view_loans()
        elif choice == '8':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()