"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                            LAB 1: STACKS
-------------------------------------------------------------------------------
- File Name: lab1_stacks.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Build browser back/forward navigation using stacks (LIFO)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# =============================================================================
# PART 1: PROVIDED CODE (Study this to understand how it works)
# =============================================================================

history_stack = []  # Pages we've visited (LIFO - Last In, First Out)
forward_stack = []  # Pages we can go forward to
current_page = None  # The page we're currently on


def visit(url):
    """Visit a new page - ALREADY IMPLEMENTED

    When visiting a new page:
    1. Push the current page onto history_stack (if there is one)
    2. Set the new URL as current_page
    3. Clear the forward_stack (can't go forward after visiting new page)
    """
    global current_page
    if current_page:
        history_stack.append(current_page)
    current_page = url
    forward_stack.clear()
    print(f"Visiting: {url}")


def show_status():
    """Display current browser state - ALREADY IMPLEMENTED"""
    print(f"\n--- Browser Status ---")
    print(f"Current page: {current_page}")
    print(f"History stack: {history_stack}")
    print(f"Forward stack: {forward_stack}")
    print()


# =============================================================================
# PART 2: YOUR CODE (Implement these functions)
# =============================================================================

def go_back():
    """
    TODO: Go back to the previous page

    Requirements:
    1. Check if history_stack is empty - if so, print "Can't go back - no history!"
       and return early (use: if len(history_stack) == 0)
    2. Push current_page onto forward_stack (so we can go forward later)
    3. Pop from history_stack and set as current_page
    4. Print the page you went back to: print(f"Back to: {current_page}")

    Hint: Use 'global current_page' at the start to modify the global variable
    Hint: Use .append() to push and .pop() to pop from a stack
    """
    global current_page
    # Your code here
    pass


def go_forward():
    """
    TODO: Go forward to a page you went back from

    Requirements:
    1. Check if forward_stack is empty - if so, print "Can't go forward - nothing ahead!"
       and return early
    2. Push current_page onto history_stack
    3. Pop from forward_stack and set as current_page
    4. Print the page you went forward to: print(f"Forward to: {current_page}")

    Hint: This is the reverse of go_back()
    """
    global current_page
    # Your code here
    pass


def can_go_back():
    """
    TODO: Return True if we can go back, False otherwise

    Hint: We can go back if history_stack has any items
    Hint: len(history_stack) > 0 returns True/False
    """
    # Your code here
    pass


def can_go_forward():
    """
    TODO: Return True if we can go forward, False otherwise

    Hint: We can go forward if forward_stack has any items
    """
    # Your code here
    pass


# =============================================================================
# PART 3: EXTENSION CHALLENGES (Optional)
# =============================================================================

def clear_history():
    """
    EXTENSION: Clear all browsing history

    Requirements:
    1. Clear both history_stack and forward_stack
    2. Keep current_page as is (don't clear it)
    3. Print "History cleared!"

    Hint: Use .clear() on both lists
    """
    # Your code here
    pass


def go_home():
    """
    EXTENSION: Go to the very first page in history (bottom of stack)

    Requirements:
    1. If history_stack is empty, print "Already at home!" and return
    2. Push current_page onto forward_stack
    3. Push all items from history_stack onto forward_stack (in order)
    4. Pop the last item from forward_stack and set as current_page
    5. Clear history_stack

    Hint: Think about the order - you want the first page visited
    """
    global current_page
    # Your code here
    pass


# =============================================================================
# PART 4: MAIN PROGRAM (Test your code)
# =============================================================================

def display_menu():
    """Display the menu options"""
    print("\n=== Browser History Manager ===")
    print("1. Visit a new page")
    print("2. Go back")
    print("3. Go forward")
    print("4. Show status")
    print("5. Exit")
    return input("Enter your choice: ")


def main():
    """Main program loop"""
    print("Welcome to the Browser History Manager!")
    print("Let's start by visiting some pages...\n")

    # Initial visits to test
    visit("google.com")
    visit("wikipedia.org")
    visit("youtube.com")
    visit("github.com")
    show_status()

    # Test your implementations
    print("Testing go_back()...")
    go_back()
    go_back()
    show_status()

    print("Testing go_forward()...")
    go_forward()
    show_status()

    print("Testing can_go_back() and can_go_forward()...")
    print(f"Can go back? {can_go_back()}")
    print(f"Can go forward? {can_go_forward()}")

    # Interactive menu (uncomment to use)
    # while True:
    #     choice = display_menu()
    #     if choice == '1':
    #         url = input("Enter URL to visit: ")
    #         visit(url)
    #     elif choice == '2':
    #         go_back()
    #     elif choice == '3':
    #         go_forward()
    #     elif choice == '4':
    #         show_status()
    #     elif choice == '5':
    #         print("Goodbye!")
    #         break
    #     else:
    #         print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
