"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 2
---------------------------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Refactor the simple music catalog system to use Object-Oriented Programming (OOP) 
               principles. Implement the Song class and CatalogManager class to manage songs using 
               JSON for file I/O. Utilise code from the previous lab where possible.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import json

class Song:
    # TODO: Define the Song class with properties for title, artist, album, and year.
    # This class should have a constructor (__init__ method) that initializes these properties.
    # Optionally, include a method to represent the Song's information as a string for easy display.
    pass

class CatalogManager:
    def __init__(self):
        # Initialize the catalog, which should be a list of Song objects.
        self.catalog = []

        # Call the load_catalog method at the end of the initializer to load existing songs from 'songs.json'.
        self.load_catalog()

    def add_song(self):
        # TODO: Prompt the user to input song details (title, artist, album, and year).
        # Create a Song object with these details and add it to the catalog.
        # Save the updated catalog to the JSON file by calling save_catalog().
        pass

    def list_songs(self):
        # TODO: Print details of each song in the catalog.
        # Iterate through the catalog and use the string representation method of Song (if defined) to display song details.
        pass

    def search_songs(self):
        # TODO: Ask the user for a search term and display songs that match the term.
        # The search should check if the term appears in any song's title, artist, album, or year.
        # Consider case sensitivity when implementing the search.
        pass

    def delete_song(self):
        # TODO: Ask the user for the title of the song they wish to delete.
        # Remove all Song objects from the catalog that have a matching title.
        # Save the updated catalog to the JSON file by calling save_catalog().
        pass

    def save_catalog(self):
        # TODO: Write the catalog to 'songs.json' using JSON format.
        # Convert each Song object in the catalog to a dictionary format that can be serialized.
        # Use json.dump() to write the list of dictionaries to the file.
        pass

    def load_catalog(self):
        # TODO: Load 'songs.json' and recreate the catalog of Song objects.
        # Read the JSON file, convert each JSON object back into a Song object, and append to the catalog.
        # Handle the FileNotFoundError for the case where 'songs.json' does not exist yet.
        pass

def main():
    manager = CatalogManager()
    while True:
        print("\nMusic Catalog Manager")
        print("1. Add Song")
        print("2. List Songs")
        print("3. Search Songs")
        print("4. Delete Song")
        print("5. Exit")
        choice = input("Enter option: ")

        if choice == '1':
            manager.add_song()
        elif choice == '2':
            manager.list_songs()
        elif choice == '3':
            manager.search_songs()
        elif choice == '4':
            manager.delete_song()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
