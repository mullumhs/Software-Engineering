"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                            LAB 4: TREES
-------------------------------------------------------------------------------
- File Name: lab4_trees.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Build a bookmark organizer using tree data structures
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# =============================================================================
# PART 1: PROVIDED CODE (Study this to understand how it works)
# =============================================================================

class BookmarkNode:
    """A node in the bookmark tree - ALREADY IMPLEMENTED

    Each node can be either a folder (has children) or a bookmark (has a URL).
    Folders contain other folders or bookmarks.
    """
    def __init__(self, name, url=None):
        """Create a new bookmark node

        Args:
            name: The display name (e.g., "Python Docs" or "Development")
            url: The URL if this is a bookmark (None if it's a folder)
        """
        self.name = name
        self.url = url  # None for folders, URL string for bookmarks
        self.children = []  # List of child nodes (empty for bookmarks)

    def is_folder(self):
        """Check if this node is a folder - ALREADY IMPLEMENTED"""
        return self.url is None

    def is_bookmark(self):
        """Check if this node is a bookmark - ALREADY IMPLEMENTED"""
        return self.url is not None


def display_tree(node, prefix="", is_last=True):
    """Display the bookmark tree structure - ALREADY IMPLEMENTED

    Uses box-drawing characters to show the tree hierarchy.
    """
    # Determine the connector symbol
    connector = "└── " if is_last else "├── "

    # Show folder with 📁 or bookmark with 🔖
    if node.is_folder():
        print(f"{prefix}{connector}📁 {node.name}")
    else:
        print(f"{prefix}{connector}🔖 {node.name}")
        print(f"{prefix}{'    ' if is_last else '│   '}   └─ {node.url}")

    # Prepare prefix for children
    child_prefix = prefix + ("    " if is_last else "│   ")

    # Display all children
    for i, child in enumerate(node.children):
        is_last_child = (i == len(node.children) - 1)
        display_tree(child, child_prefix, is_last_child)


# =============================================================================
# PART 2: YOUR CODE (Implement these functions)
# =============================================================================

def add_folder(parent, folder_name):
    """
    TODO: Add a new folder as a child of the parent node

    Requirements:
    1. Create a new BookmarkNode with the folder_name (no URL)
    2. Append it to parent.children
    3. Print "Created folder: {folder_name}"
    4. Return the new folder node

    Hint: BookmarkNode(name) creates a folder (url defaults to None)
    """
    # Your code here
    pass


def add_bookmark(parent, name, url):
    """
    TODO: Add a new bookmark as a child of the parent node

    Requirements:
    1. Create a new BookmarkNode with both name and url
    2. Append it to parent.children
    3. Print "Added bookmark: {name}"
    4. Return the new bookmark node

    Hint: BookmarkNode(name, url) creates a bookmark
    """
    # Your code here
    pass


def count_bookmarks(node):
    """
    TODO: Count all bookmarks in this node and its descendants

    Requirements:
    1. If the node is a bookmark (not a folder), return 1
    2. If the node is a folder, count all bookmarks in its children
    3. Use RECURSION: call count_bookmarks on each child

    Hint: Start with count = 0, then add count_bookmarks(child) for each child
    """
    # Your code here
    pass


def count_folders(node):
    """
    TODO: Count all folders in this node and its descendants

    Requirements:
    1. If the node is a bookmark, return 0
    2. If the node is a folder, count 1 plus all folders in its children
    3. Use RECURSION: call count_folders on each child

    Hint: Start with count = 1 (for this folder), then add for each child
    """
    # Your code here
    pass


def find_bookmark(node, search_name):
    """
    TODO: Search for a bookmark by name (case-insensitive)

    Requirements:
    1. If this node is a bookmark and its name matches, return this node
    2. If this node is a folder, search through all children
    3. Use RECURSION to search the entire tree
    4. Return the first matching BookmarkNode, or None if not found

    Hint: Use search_name.lower() in node.name.lower() for partial matching
    """
    # Your code here
    pass


# =============================================================================
# PART 3: EXTENSION CHALLENGES (Optional)
# =============================================================================

def get_all_urls(node):
    """
    EXTENSION: Get a list of all URLs in the tree

    Requirements:
    1. If node is a bookmark, return a list with just its URL
    2. If node is a folder, collect URLs from all children
    3. Return a flat list of all URLs

    Hint: Use list concatenation or extend()
    """
    # Your code here
    pass


def get_depth(node, current_depth=0):
    """
    EXTENSION: Find the maximum depth of the tree

    Requirements:
    1. If node has no children, return current_depth
    2. Otherwise, find the max depth among all children
    3. Return the maximum depth found
    """
    # Your code here
    pass


def delete_bookmark(parent, bookmark_name):
    """
    EXTENSION: Delete a bookmark from a folder by name

    Requirements:
    1. Search through parent.children for a bookmark with matching name
    2. If found, remove it from the children list
    3. Print "Deleted: {bookmark_name}"
    4. Return True if deleted, False if not found

    Hint: Use a loop with index to find and remove, or list comprehension
    """
    # Your code here
    pass


def move_bookmark(source_folder, dest_folder, bookmark_name):
    """
    EXTENSION: Move a bookmark from one folder to another

    Requirements:
    1. Find the bookmark in source_folder
    2. Remove it from source_folder.children
    3. Add it to dest_folder.children
    4. Print "Moved {bookmark_name} to {dest_folder.name}"
    5. Return True if moved, False if not found
    """
    # Your code here
    pass


# =============================================================================
# PART 4: MAIN PROGRAM (Test your code)
# =============================================================================

def display_menu():
    """Display the menu options"""
    print("\n=== Bookmark Manager ===")
    print("1. Add folder")
    print("2. Add bookmark")
    print("3. Display tree")
    print("4. Count bookmarks")
    print("5. Search")
    print("6. Exit")
    return input("Enter your choice: ")


def main():
    """Main program loop"""
    print("Welcome to the Bookmark Manager!")
    print("Let's build a bookmark tree...\n")

    # Create root node
    root = BookmarkNode("Bookmarks")

    # Build a sample tree structure
    print("Building sample bookmark tree...\n")

    # Test add_folder
    dev = add_folder(root, "Development")
    social = add_folder(root, "Social Media")
    entertainment = add_folder(root, "Entertainment")

    # Test add_bookmark
    if dev:  # Only if add_folder is implemented
        add_bookmark(dev, "Python Docs", "https://docs.python.org")
        add_bookmark(dev, "GitHub", "https://github.com")
        add_bookmark(dev, "Stack Overflow", "https://stackoverflow.com")

        # Add a subfolder
        tutorials = add_folder(dev, "Tutorials")
        if tutorials:
            add_bookmark(tutorials, "W3Schools", "https://w3schools.com")
            add_bookmark(tutorials, "MDN Web Docs", "https://developer.mozilla.org")

    if social:
        add_bookmark(social, "Twitter", "https://twitter.com")
        add_bookmark(social, "LinkedIn", "https://linkedin.com")

    if entertainment:
        add_bookmark(entertainment, "YouTube", "https://youtube.com")
        add_bookmark(entertainment, "Netflix", "https://netflix.com")

    # Display the tree
    print("\n📂 Bookmark Tree:")
    print("=" * 40)
    display_tree(root)

    # Test count functions
    print("\nTesting count_bookmarks()...")
    total = count_bookmarks(root)
    print(f"Total bookmarks: {total}")

    print("\nTesting count_folders()...")
    folders = count_folders(root)
    print(f"Total folders: {folders}")

    # Test search
    print("\nTesting find_bookmark()...")
    result = find_bookmark(root, "GitHub")
    if result:
        print(f"Found: {result.name} -> {result.url}")
    else:
        print("Not found")

    result = find_bookmark(root, "python")  # Case-insensitive partial match
    if result:
        print(f"Found: {result.name} -> {result.url}")

    # Interactive menu (uncomment to use)
    # while True:
    #     choice = display_menu()
    #     if choice == '1':
    #         name = input("Folder name: ")
    #         add_folder(root, name)
    #     elif choice == '2':
    #         name = input("Bookmark name: ")
    #         url = input("URL: ")
    #         add_bookmark(root, name, url)
    #     elif choice == '3':
    #         print("\n📂 Bookmark Tree:")
    #         display_tree(root)
    #     elif choice == '4':
    #         print(f"Total bookmarks: {count_bookmarks(root)}")
    #         print(f"Total folders: {count_folders(root)}")
    #     elif choice == '5':
    #         search = input("Search for: ")
    #         result = find_bookmark(root, search)
    #         if result:
    #             print(f"Found: {result.name} -> {result.url}")
    #         else:
    #             print("Not found")
    #     elif choice == '6':
    #         print("Goodbye!")
    #         break
    #     else:
    #         print("Invalid choice.")


if __name__ == "__main__":
    main()
