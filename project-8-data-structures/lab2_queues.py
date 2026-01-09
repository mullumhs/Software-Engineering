"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                            LAB 2: QUEUES
-------------------------------------------------------------------------------
- File Name: lab2_queues.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Build a download queue manager using queues (FIFO)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from collections import deque

# =============================================================================
# PART 1: PROVIDED CODE (Study this to understand how it works)
# =============================================================================

download_queue = deque()  # Queue of pending downloads (FIFO - First In, First Out)
completed_downloads = []   # List of completed downloads


def add_download(filename, size_mb):
    """Add a download to the queue - ALREADY IMPLEMENTED

    Each download is stored as a dictionary with filename, size, and status.
    New downloads are added to the back of the queue.
    """
    download = {
        'filename': filename,
        'size_mb': size_mb,
        'status': 'pending'
    }
    download_queue.append(download)
    print(f"Added to queue: {filename} ({size_mb}MB)")


def show_queue():
    """Display the current download queue - ALREADY IMPLEMENTED"""
    print("\n--- Download Queue ---")
    if len(download_queue) == 0:
        print("Queue is empty!")
    else:
        for i, download in enumerate(download_queue, 1):
            print(f"{i}. {download['filename']} ({download['size_mb']}MB) - {download['status']}")
    print(f"\nCompleted: {len(completed_downloads)} downloads")
    print()


# =============================================================================
# PART 2: YOUR CODE (Implement these functions)
# =============================================================================

def process_download():
    """
    TODO: Process the next download in the queue (FIFO - first added = first processed)

    Requirements:
    1. Check if download_queue is empty - if so, print "No downloads in queue!" and return None
    2. Remove the download from the FRONT of the queue (use popleft())
    3. Update the download's status to 'completed'
    4. Add it to the completed_downloads list
    5. Print a message: print(f"Downloaded: {download['filename']}")
    6. Return the download dictionary

    Hint: Use download_queue.popleft() to remove from front (FIFO)
    Hint: To update status: download['status'] = 'completed'
    """
    # Your code here
    pass


def get_queue_size():
    """
    TODO: Return the number of downloads waiting in the queue

    Hint: Use len() on download_queue
    """
    # Your code here
    pass


def get_next_download():
    """
    TODO: Peek at the next download without removing it

    Requirements:
    1. If queue is empty, return None
    2. Otherwise, return the download at the front of the queue (index 0)

    Hint: Access with download_queue[0] - but check if empty first!
    """
    # Your code here
    pass


def get_total_size():
    """
    TODO: Calculate the total size of all pending downloads

    Requirements:
    1. Loop through all downloads in download_queue
    2. Add up all the size_mb values
    3. Return the total

    Hint: Use a for loop and access download['size_mb']
    """
    # Your code here
    pass


# =============================================================================
# PART 3: EXTENSION CHALLENGES (Optional)
# =============================================================================

def process_all():
    """
    EXTENSION: Process all downloads in the queue

    Requirements:
    1. While the queue is not empty, process each download
    2. Print "All downloads complete!" when done
    3. Return the number of downloads that were processed
    """
    # Your code here
    pass


def cancel_download(filename):
    """
    EXTENSION: Cancel a specific download by filename

    Requirements:
    1. Search through the queue for the download with matching filename
    2. If found, remove it and print "Cancelled: {filename}"
    3. If not found, print "Download not found: {filename}"
    4. Return True if cancelled, False if not found

    Hint: You may need to convert deque to list, remove, then convert back
    """
    # Your code here
    pass


def prioritize_download(filename):
    """
    EXTENSION: Move a download to the front of the queue

    Requirements:
    1. Find the download with the matching filename
    2. Remove it from its current position
    3. Add it to the front of the queue (use appendleft())
    4. Print "Prioritized: {filename}"

    Hint: Similar to cancel, but add back to front instead of removing
    """
    # Your code here
    pass


# =============================================================================
# PART 4: MAIN PROGRAM (Test your code)
# =============================================================================

def display_menu():
    """Display the menu options"""
    print("\n=== Download Manager ===")
    print("1. Add download")
    print("2. Process next download")
    print("3. View queue")
    print("4. Show queue size")
    print("5. Show total size")
    print("6. Exit")
    return input("Enter your choice: ")


def main():
    """Main program loop"""
    print("Welcome to the Download Queue Manager!")
    print("Let's add some downloads to the queue...\n")

    # Add some test downloads
    add_download("movie.mp4", 1500)
    add_download("song.mp3", 5)
    add_download("document.pdf", 2)
    add_download("game.zip", 800)
    add_download("photo.jpg", 3)
    show_queue()

    # Test your implementations
    print("Testing get_queue_size()...")
    print(f"Queue size: {get_queue_size()}")

    print("\nTesting get_next_download()...")
    next_dl = get_next_download()
    if next_dl:
        print(f"Next download: {next_dl['filename']}")

    print("\nTesting get_total_size()...")
    print(f"Total size: {get_total_size()}MB")

    print("\nTesting process_download()...")
    process_download()
    process_download()
    show_queue()

    # Interactive menu (uncomment to use)
    # while True:
    #     choice = display_menu()
    #     if choice == '1':
    #         filename = input("Enter filename: ")
    #         size = int(input("Enter size in MB: "))
    #         add_download(filename, size)
    #     elif choice == '2':
    #         process_download()
    #     elif choice == '3':
    #         show_queue()
    #     elif choice == '4':
    #         print(f"Queue size: {get_queue_size()}")
    #     elif choice == '5':
    #         print(f"Total size: {get_total_size()}MB")
    #     elif choice == '6':
    #         print("Goodbye!")
    #         break
    #     else:
    #         print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
