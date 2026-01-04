"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                contact_manager.py
---------------------------------------------------------------------------------
- Description: File containing the ContactManager class for managing contact info.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Import the Contact class from lab3.py
from lab3 import Contact

class ContactManager:
    # __init__ method initialises the contacts list.
    def __init__(self):
        self.contacts = []

    # The parameters 'name', 'email', and 'phone' are used to create a new contact.
    def add_contact(self, name, email, phone):
        new_contact = Contact(name, email, phone)
        self.contacts.append(new_contact)
        print(f"Added new contact: {name}")

    def display_contacts(self):
        # TODO: Implement this method to print all contact details.
        # You may choose to create a __str__ method in the Contact class or implement this method here.
        pass # Then, remove this line.

    # The parameter 'name' is used to identify the contact to update.
    # The parameters 'new_email' and 'new_phone' are optional and can be used to update the contact's email and phone.
    # You can update only the email, only the phone, or both by providing the respective parameters.
    # E.g. update_contact("John Doe", new_phone="12345678")
    def update_contact(self, name, new_email=None, new_phone=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_email:
                    contact.email = new_email
                    print(f"Updated {name}'s email to {new_email}")
                if new_phone:
                    contact.phone = new_phone
                    print(f"Updated {name}'s phone to {new_phone}")
                break
        else:
            print("Contact not found.")

    # The parameter 'name' is used to identify the contact to remove.
    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} has been removed.")
                break
        print("Contact not found.")