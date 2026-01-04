"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 3
-----------------------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Develop a user interface for the Inventory Management System. This interface will
               allow users to interact with the InventoryManager to add, update, remove, and view
               items in the inventory using a command-line interface.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import necessary classes (Item class from lab1, InventoryManager class from lab2)


# Step 2: Define an add_item function that prompts the user for item details and adds the item to the inventory


# Step 3: Define an update_item function that prompts the user for item details and updates the item in the inventory


# Step 4: Define a remove_item function that prompts the user for an item name and removes the item from the inventory


# Step 5: Define a display_inventory function that displays all items in the inventory


def main():
    # Step 6: Initialise an instance of InventoryManager
    

    # Step 7: Use the actions dictionary to map user input to the corresponding functions
    actions = {}
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Enter choice: ")

        # Step 8: Implement the logic to call the appropriate function based on user input
        # Exit the loop if the user chooses 5, otherwise display an error message for invalid choices


        

if __name__ == "__main__":
    main()