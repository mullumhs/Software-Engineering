# D&D Character Creator

## Project Overview
This project implements a Dungeons & Dragons (D&D) character creation and management system using Object-Oriented Programming (OOP) principles in Python.

## Requirements
1. Create a base Character class with attributes like name, race, class, level, hit points, armour class, and ability scores.
2. Implement a Dice class for rolling dice.
3. Create methods for rolling random stats, leveling up characters, and displaying character information.
4. Develop a user interface for character creation, viewing, and management.
5. Implement error handling and input validation.
6. Use appropriate naming conventions and comment code effectively.
7. Organize code into separate files and classes for modularity.
8. Add unique features (e.g., save/load characters, inventory system, weapon system, initiative order).

## Key Components

### Character Class
- Attributes: name, race, class, level, hit points, armour class, ability scores
- Methods:
  - Generate random ability scores
  - Apply racial bonuses
  - Calculate hit points
  - Level up
  - Display character information

### Dice Class
- Method for rolling dice (e.g., 4d6 drop lowest for ability scores)

### Game Logic
- Ability score generation and modifiers calculation
- Hit point calculation
- Racial bonus application
- Armor class calculation

## Development Focus

1. **Object-Oriented Design**: Implement well-structured classes with appropriate encapsulation.
2. **Game Mechanics**: Accurately implement D&D 5e rules for character creation and management.
3. **Data Structures**: Effectively use dictionaries for race bonuses, class information, etc.
4. **User Interface**: Create an intuitive menu system for character creation and management.
5. **Error Handling**: Implement robust input validation and error handling.
6. **Code Quality**: Follow PEP 8 style guide, use meaningful names, and organize code logically.
7. **Documentation**: Add comments explaining functions and complex logic.
8. **Version Control**: Use GitHub for project management with regular, well-documented commits.

## Running the Application
Execute `main.py` to start the D&D Character Creator:

```bash
python main.py
```

## Course Materials

- [Project 15 - D&D Character Creator](https://sites.google.com/education.nsw.gov.au/mhs-software-engineering/preliminary/object-oriented-programming/project-15-dd-character-creator)