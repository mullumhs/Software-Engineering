"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 1
---------------------------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Develop a simple music catalog system. Functions include adding songs, listing
               songs, searching for songs, and deleting songs from the catalog. Each song is
               stored as a line in a text file with details such as title, artist, album, and year
               separated by commas.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def add_song():
    # TODO: Open the file 'songs.txt' in append mode.
    # Ask the user to input the song title, artist, album, and release year.
    # Write this information to the file in the format: title, artist, album, year followed by a newline.
    pass

def list_songs():
    # TODO: Open the file 'songs.txt' in read mode.
    # Read each line from the file, split the line into title, artist, album, and year using ', ' as the delimiter.
    # Print each song's details in a readable format.
    pass

def search_songs():
    # TODO: Ask the user for a search term.
    # Open the file 'songs.txt' in read mode and search for lines that contain the search term (consider case sensitivity).
    # Print the details of each matching song in a readable format.
    pass

def delete_song():
    # TODO: Ask the user for the title of the song to delete.
    # Open 'songs.txt' in read mode and read all lines.
    # Re-open 'songs.txt' in write mode and write back only those lines that do not contain the title of the song to delete.
    pass

def main():
    while True:
        print("\nMusic Catalog Manager")
        print("1. Add Song")
        print("2. List Songs")
        print("3. Search Songs")
        print("4. Delete Song")
        print("5. Exit")
        choice = input("Enter option: ")

        if choice == '1':
            add_song()
        elif choice == '2':
            list_songs()
        elif choice == '3':
            search_songs()
        elif choice == '4':
            delete_song()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()