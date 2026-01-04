"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    CONTACTS
---------------------------------------------------------------------------------
- File Name: contacts.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Learn about the procedural programming paradigm
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def display_menu():
    print("Welcome to Contacts Manager")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")        # TODO: Implement the delete contact functionality
    print("5. Update a contact")        # TODO: Implement the update contact functionality
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_contact(contacts):
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    contacts[name] = phone
    print("Contact added successfully!")

def view_contacts(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts to display.")

def search_contact(contacts):
    """
    TODO: Implement this function

    Requirements:
    1. Ask the user for a name to search for
    2. Check if the name exists in the contacts dictionary
    3. If found, display the contact's name and phone number
    4. If not found, display an appropriate message

    Hint: Use the 'in' operator to check if a key exists in a dictionary
    """
    search_name = input("Enter the name of the contact to search for: ")
    # Your code goes here
    pass

def delete_contact(contacts):
    """
    TODO: Implement this function

    Requirements:
    1. Ask the user for the name of the contact to delete
    2. Check if the contact exists
    3. If found, remove the contact and confirm deletion
    4. If not found, display an appropriate message

    Hint: Use the 'del' keyword or .pop() method to remove from a dictionary
    """
    delete_name = input("Enter the name of the contact to delete: ")
    # Your code goes here
    pass

def update_contact(contacts):
    """
    TODO: Implement this function

    Requirements:
    1. Ask the user for the name of the contact to update
    2. Check if the contact exists
    3. If found, ask for the new phone number and update it
    4. If not found, display an appropriate message
    """
    update_name = input("Enter the name of the contact to update: ")
    # Your code goes here
    pass

def main():
    contacts = {}
    while True:
        choice = display_menu()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            update_contact(contacts)
        elif choice == '6':
            print("Thank you for using Contacts Manager!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
