# MHS Software Engineering

**Teacher:** David Steedman

This repository contains all projects for the NSW HSC Software Engineering course at MHS (Mullumbimby High School), covering both Preliminary (Year 11) and HSC (Year 12) content.

## Course Website

[MHS Software Engineering Course](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/home)

---

## Year 11 - Preliminary

### Programming Fundamentals

| Project | Name | Topics | Link |
|---------|------|--------|------|
| 1 | [Mad Libs](project-1-mad-libs/) | Variables, strings, user input | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/programming-fundamentals/project-1-mad-libs) |
| 2 | [Temperature Converter](project-2-temp-converter/) | Numbers, operations, conditionals | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/programming-fundamentals/project-2-temperature-converter) |
| 3 | [Guessing Game](project-3-guessing-game/) | Loops, input validation, random | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/programming-fundamentals/project-3-guessing-game) |
| 4 | [Dice Roller](project-4-dice-roller/) | Functions, parameters, exceptions | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/programming-fundamentals/project-4-dice-roller) |
| 5 | [To-Do List](project-5-todo-list/) | Lists, list manipulation | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/programming-fundamentals/project-5-to-do-list) |
| 6 | [Shopping List](project-6-shopping-list/) | Dictionaries, data validation | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/programming-fundamentals/project-6-shopping-list) |
| 7 | [Tic-Tac-Toe](project-7-tic-tac-toe/) | Game development, SDLC | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/programming-fundamentals/project-7-tic-tac-toe) |
| 8 | [Contacts](project-8-contacts/) | Procedural programming | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/programming-fundamentals/project-8-contacts) |

### Object-Oriented Programming

| Project | Name | Topics | Link |
|---------|------|--------|------|
| 9 | [Contacts OOP](project-9-contacts-oop/) | Classes, objects, methods | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/object-oriented-programming/project-9-contacts-oop) |
| 10 | [Animal Kingdom](project-10-animal-kingdom/) | Inheritance, polymorphism | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/object-oriented-programming/project-10-animal-kingdom) |
| 11 | [Shapes & Geometry](project-11-shapes-geometry/) | OOP design, SDLC | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/object-oriented-programming/project-11-shapes-geometry) |
| 12 | [Inventory System](project-12-inventory-system/) | Encapsulation, facade pattern | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/object-oriented-programming/project-12-inventory-system) |
| 13 | [Banking System](project-13-banking-system/) | Design patterns, UML | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/object-oriented-programming/project-13-banking-system) |
| 14 | [Library System](project-14-library-system/) | File I/O, JSON persistence | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/object-oriented-programming/project-14-library-system) |
| 15 | [D&D Character Creator](project-15-dnd-character-creator/) | Assessment task | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/object-oriented-programming/project-15-dd-character-creator) |

---

## Year 12 - HSC

### Programming for the Web

| Project | Name | Topics | Link |
|---------|------|--------|------|
| 16 | [HTML & CSS](project-16-html/) | HTML5, CSS3, semantic elements | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/hsc/programming-for-the-web/html) |
| 17 | [Bootstrap](project-17-bootstrap/) | Bootstrap 5, responsive design | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/hsc/programming-for-the-web/bootstrap) |
| 18 | [Flask](project-18-flask/) | Python Flask, routing, templates | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/hsc/programming-for-the-web/flask) |
| 19 | [SQLite](project-19-sqlite/) | Databases, SQL, ORM | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/hsc/programming-for-the-web/sqlite) |
| 20 | [PWA](project-20-pwa/) | Progressive Web Apps (Assessment) | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/hsc/programming-for-the-web/pwa-assessment-task) |

### Secure Software Architecture

| Project | Name | Topics | Link |
|---------|------|--------|------|
| 21 | [Unsecure PWA](project-21-unsecure-pwa/) | Security vulnerabilities, testing | [Course Page](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/hsc/secure-software-architecture) |

---

## Getting Started

### For Students

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to your current project folder:
   ```bash
   cd project-1-mad-libs
   ```

3. Follow the instructions in the project's README.md file.

### Prerequisites

- **Python 3.8+** - For all Python projects
- **VS Code** - Recommended IDE
- **Git** - Version control

### For Web Projects (16-21)

Some projects require additional setup:

```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate

# Install dependencies (if requirements.txt exists)
pip install -r requirements.txt
```

---

## Project Structure

```
Software-Engineering/
├── README.md                          # This file
├── .gitignore                         # Git ignore rules
│
├── project-1-mad-libs/                # Year 11 - Fundamentals
├── project-2-temp-converter/
├── project-3-guessing-game/
├── project-4-dice-roller/
├── project-5-todo-list/
├── project-6-shopping-list/
├── project-7-tic-tac-toe/
├── project-8-contacts/
│
├── project-9-contacts-oop/            # Year 11 - OOP
├── project-10-animal-kingdom/
├── project-11-shapes-geometry/
├── project-12-inventory-system/
├── project-13-banking-system/
├── project-14-library-system/
├── project-15-dnd-character-creator/
│
├── project-16-html/                   # Year 12 - Web
├── project-17-bootstrap/
├── project-18-flask/
├── project-19-sqlite/
├── project-20-pwa/
│
└── project-21-unsecure-pwa/           # Year 12 - Security
```

---

## Running Tests

Some projects include unit tests. Run them with:

```bash
cd project-2-temp-converter
python -m unittest test_temp_converter -v
```

Projects with tests:
- Project 2: Temperature Converter
- Project 4: Dice Roller
- Project 9: Contacts OOP
- Project 11: Shapes & Geometry

---

## Resources

- [NESA HSC Software Engineering Syllabus](https://curriculum.nsw.edu.au/learning-areas/tas/software-engineering-11-12-2022)
- [Python Documentation](https://docs.python.org/3/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [MDN Web Docs](https://developer.mozilla.org/)

---

## License

This educational material is provided for students of MHS Software Engineering.
