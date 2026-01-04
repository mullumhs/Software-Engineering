"""
Unit Tests for Contacts OOP
---------------------------
File Name: test_contacts.py
Teacher: David Steedman
Class: Software Engineering

Run these tests with: python -m unittest test_contacts
Or: python test_contacts.py
"""

import unittest


# =============================================================================
# STUDENT IMPLEMENTATION SECTION
# =============================================================================
# 
# TODO: Import your Contact class from contact_manager.py or create it here.
# 
# Your Contact class should look something like:
# 
# class Contact:
#     def __init__(self, name, phone, email=None):
#         self.name = name
#         self.phone = phone
#         self.email = email
#     
#     def get_name(self):
#         return self.name
#     
#     def get_phone(self):
#         return self.phone
#     
#     def set_phone(self, phone):
#         self.phone = phone
#
# Uncomment the import below if you've completed contact_manager.py:
# from contact_manager import Contact, ContactManager
# =============================================================================


class Contact:
    """A simple Contact class. Replace with your implementation."""
    
    def __init__(self, name, phone, email=None):
        self._name = name
        self._phone = phone
        self._email = email
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_phone(self):
        return self._phone
    
    def set_phone(self, phone):
        self._phone = phone
    
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email
    
    def __str__(self):
        return f"Contact: {self._name}, Phone: {self._phone}"


class ContactManager:
    """A simple ContactManager class. Replace with your implementation."""
    
    def __init__(self):
        self._contacts = []
    
    def add_contact(self, contact):
        self._contacts.append(contact)
    
    def get_all_contacts(self):
        return self._contacts
    
    def find_contact(self, name):
        for contact in self._contacts:
            if contact.get_name().lower() == name.lower():
                return contact
        return None
    
    def remove_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            self._contacts.remove(contact)
            return True
        return False


# =============================================================================
# TEST CASES
# =============================================================================

class TestContact(unittest.TestCase):
    """Tests for the Contact class."""
    
    def setUp(self):
        """Create a fresh contact before each test."""
        self.contact = Contact("Alice Smith", "0412345678", "alice@example.com")
    
    def test_create_contact(self):
        """Contact should store name, phone, and email."""
        self.assertEqual(self.contact.get_name(), "Alice Smith")
        self.assertEqual(self.contact.get_phone(), "0412345678")
        self.assertEqual(self.contact.get_email(), "alice@example.com")
    
    def test_create_contact_without_email(self):
        """Contact should work without an email address."""
        contact = Contact("Bob Jones", "0498765432")
        self.assertEqual(contact.get_name(), "Bob Jones")
        self.assertEqual(contact.get_phone(), "0498765432")
        self.assertIsNone(contact.get_email())
    
    def test_update_phone(self):
        """Should be able to update phone number."""
        self.contact.set_phone("0499999999")
        self.assertEqual(self.contact.get_phone(), "0499999999")
    
    def test_update_email(self):
        """Should be able to update email address."""
        self.contact.set_email("newemail@example.com")
        self.assertEqual(self.contact.get_email(), "newemail@example.com")
    
    def test_str_representation(self):
        """Contact should have a string representation."""
        str_repr = str(self.contact)
        self.assertIn("Alice Smith", str_repr)


class TestContactManager(unittest.TestCase):
    """Tests for the ContactManager class."""
    
    def setUp(self):
        """Create a fresh manager and contacts before each test."""
        self.manager = ContactManager()
        self.alice = Contact("Alice Smith", "0412345678")
        self.bob = Contact("Bob Jones", "0498765432")
    
    def test_add_contact(self):
        """Should be able to add a contact."""
        self.manager.add_contact(self.alice)
        contacts = self.manager.get_all_contacts()
        self.assertEqual(len(contacts), 1)
        self.assertIn(self.alice, contacts)
    
    def test_add_multiple_contacts(self):
        """Should be able to add multiple contacts."""
        self.manager.add_contact(self.alice)
        self.manager.add_contact(self.bob)
        contacts = self.manager.get_all_contacts()
        self.assertEqual(len(contacts), 2)
    
    def test_find_contact_by_name(self):
        """Should be able to find a contact by name."""
        self.manager.add_contact(self.alice)
        self.manager.add_contact(self.bob)
        found = self.manager.find_contact("Alice Smith")
        self.assertEqual(found.get_name(), "Alice Smith")
    
    def test_find_contact_case_insensitive(self):
        """Finding a contact should be case insensitive."""
        self.manager.add_contact(self.alice)
        found = self.manager.find_contact("alice smith")
        self.assertIsNotNone(found)
    
    def test_find_nonexistent_contact(self):
        """Finding a nonexistent contact should return None."""
        self.manager.add_contact(self.alice)
        found = self.manager.find_contact("Charlie Brown")
        self.assertIsNone(found)
    
    def test_remove_contact(self):
        """Should be able to remove a contact."""
        self.manager.add_contact(self.alice)
        self.manager.add_contact(self.bob)
        result = self.manager.remove_contact("Alice Smith")
        self.assertTrue(result)
        self.assertEqual(len(self.manager.get_all_contacts()), 1)
    
    def test_remove_nonexistent_contact(self):
        """Removing a nonexistent contact should return False."""
        result = self.manager.remove_contact("Nobody")
        self.assertFalse(result)


if __name__ == '__main__':
    print("Running Contacts OOP Tests...")
    print("=" * 50)
    unittest.main(verbosity=2)
