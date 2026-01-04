# Project 14: Library System

Teacher: David Steedman

This repository hosts Project 14 for the MHS Software Engineering class. The project focuses on file I/O and data persistence by integrating these elements into an Object-Oriented Programming (OOP) framework to develop a comprehensive Library Management System.

## Main Project: Lab Exercises
- Lab 1: [`lab1.py`](lab1.py) - Develop a simple music catalog system using basic file operations. Functions include adding, listing, searching, and deleting songs, storing each song's details in a text file.
- Lab 2: [`lab2.py`](lab2.py) - Refactor the music catalog to use OOP and JSON for data management. Implement classes `Song` and `CatalogManager` to manage the songs with JSON serialisation and deserialisation.
- Lab 3: [`lab3.py`](lab3.py) - Complete the library system by implementing JSON data persistence for managing books and library members. This involves creating methods for loading and saving books and members to and from JSON files.

## Other Files
- [`book.py`](book.py): Defines the `Book` class, which includes properties like title, author, and ISBN, and methods to manage book loans.
- [`books.json`](books.json): Stores data about books in JSON format, used for persisting book information across sessions.
- [`library.py`](library.py): Contains the `Library` class, which orchestrates the overall management of books and members within the library.
- [`members.json`](members.json): Contains member information in JSON format, facilitating the persistence of library member data.
- [`person.py`](person.py): Defines the `Person` class for handling library member details such as name and member ID.

## Extension Tasks
- **Enhanced Features**: Students are encouraged to enhance the library system by adding features such as loan management, due dates for books, and a system for penalties.
- **Advanced Search**: Implement advanced search capabilities that allow filtering by multiple fields such as author, title, and ISBN.

## Learning Outcomes
- **Basic File I/O with Text**: Understand and apply basic file input/output operations to manage data stored in text files, developing foundational skills in data handling.
- **Advanced Data Persistence with JSON**: Master the use of JSON for data persistence in Python, enhancing capabilities in managing more complex data structures effectively.
- **Serialising and Deserialising Classes with JSON**: Gain proficiency in serialising and deserialising objects in Python using JSON, enabling the storage and retrieval of class instances in a maintainable and scalable manner.

## Course Materials

- [Project 14 - Library System](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/object-oriented-programming/project-14-library-system)
- [Lab 1 - Basic Text IO](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/object-oriented-programming/project-14-library-system/lab-1-basic-text-io)
- [Lab 2 - Introduction to JSON](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/object-oriented-programming/project-14-library-system/lab-2-introduction-to-json)
- [Lab 3 - Library System](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/object-oriented-programming/project-14-library-system/lab-3-library-system)