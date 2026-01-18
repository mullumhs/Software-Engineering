"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                            LAB 3: HASH TABLES
-------------------------------------------------------------------------------
- File Name: lab3_hash_tables.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Build a URL cache using hash tables (dictionaries)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# =============================================================================
# PART 1: PROVIDED CODE (Study this to understand how it works)
# =============================================================================

# Our cache stores URL -> page info mappings
# Key: URL (string)
# Value: dictionary with title, visits, and cached status
url_cache = {}


def cache_page(url, title):
    """Add a page to the cache - ALREADY IMPLEMENTED

    Creates a cache entry with the page title, visit count, and cached status.
    If the URL already exists, it updates the title and marks as cached.
    """
    if url in url_cache:
        url_cache[url]['title'] = title
        url_cache[url]['cached'] = True
        print(f"Updated cache: {url}")
    else:
        url_cache[url] = {
            'title': title,
            'visits': 0,
            'cached': True
        }
        print(f"Cached: {url} -> {title}")


def show_cache():
    """Display all cached pages - ALREADY IMPLEMENTED"""
    print("\n--- URL Cache ---")
    if len(url_cache) == 0:
        print("Cache is empty!")
    else:
        for url, info in url_cache.items():
            status = "✓" if info['cached'] else "✗"
            print(f"[{status}] {url}")
            print(f"    Title: {info['title']}")
            print(f"    Visits: {info['visits']}")
    print(f"\nTotal cached: {len(url_cache)} pages")
    print()


# =============================================================================
# PART 2: YOUR CODE (Implement these functions)
# =============================================================================

def get_title(url):
    """
    TODO: Get the title for a URL from the cache

    Requirements:
    1. Check if the URL exists in url_cache (use: if url in url_cache)
    2. If found:
       - Increment the visits count: url_cache[url]['visits'] += 1
       - Print "Cache HIT: {title}"
       - Return the title
    3. If not found:
       - Print "Cache MISS: {url} not found"
       - Return None

    Hint: Access dictionary values with url_cache[url]['title']
    """
    # Your code here
    pass


def is_cached(url):
    """
    TODO: Check if a URL is in the cache

    Requirements:
    1. Return True if the URL exists in url_cache
    2. Return False if it doesn't

    Hint: Use the 'in' operator: url in url_cache
    """
    # Your code here
    pass


def remove_from_cache(url):
    """
    TODO: Remove a URL from the cache

    Requirements:
    1. Check if the URL exists in the cache
    2. If found, remove it using 'del url_cache[url]'
    3. Print "Removed from cache: {url}"
    4. If not found, print "URL not in cache: {url}"
    5. Return True if removed, False if not found

    Hint: Use 'del' to remove a key from a dictionary
    """
    # Your code here
    pass


def get_visit_count(url):
    """
    TODO: Get the number of times a cached page has been accessed

    Requirements:
    1. If URL is in cache, return its visits count
    2. If URL is not in cache, return 0

    Hint: Access with url_cache[url]['visits']
    """
    # Your code here
    pass


def get_most_visited():
    """
    TODO: Find the most visited page in the cache

    Requirements:
    1. If cache is empty, return None
    2. Find the URL with the highest visits count
    3. Return a tuple: (url, visits_count)

    Hint: Loop through url_cache.items() and track the max
    """
    # Your code here
    pass


# =============================================================================
# PART 3: EXTENSION CHALLENGES (Optional)
# =============================================================================

def clear_cache():
    """
    EXTENSION: Clear all cached pages

    Requirements:
    1. Clear the url_cache dictionary
    2. Print "Cache cleared! Removed X pages" (where X is the count)
    """
    # Your code here
    pass


def get_cache_stats():
    """
    EXTENSION: Return statistics about the cache

    Requirements:
    Return a dictionary with:
    - 'total_pages': number of cached pages
    - 'total_visits': sum of all visits across all pages
    - 'average_visits': average visits per page (or 0 if empty)
    """
    # Your code here
    pass


def search_by_title(keyword):
    """
    EXTENSION: Search for pages whose title contains a keyword

    Requirements:
    1. Search through all cached pages
    2. Return a list of URLs whose title contains the keyword (case-insensitive)

    Hint: Use 'keyword.lower() in title.lower()' for case-insensitive search
    """
    # Your code here
    pass


# =============================================================================
# PART 4: MAIN PROGRAM (Test your code)
# =============================================================================

def display_menu():
    """Display the menu options"""
    print("\n=== URL Cache Manager ===")
    print("1. Cache a page")
    print("2. Get page title")
    print("3. Check if cached")
    print("4. Remove from cache")
    print("5. Show cache")
    print("6. Most visited page")
    print("7. Exit")
    return input("Enter your choice: ")


def main():
    """Main program loop"""
    print("Welcome to the URL Cache Manager!")
    print("Let's cache some pages...\n")

    # Add some test pages
    cache_page("google.com", "Google Search")
    cache_page("wikipedia.org", "Wikipedia - The Free Encyclopedia")
    cache_page("youtube.com", "YouTube - Broadcast Yourself")
    cache_page("github.com", "GitHub - Where the world builds software")
    cache_page("python.org", "Python Programming Language")
    show_cache()

    # Test your implementations
    print("Testing get_title()...")
    get_title("google.com")
    get_title("google.com")  # Should increment visits
    get_title("unknown.com")  # Should be a cache miss

    print("\nTesting is_cached()...")
    print(f"Is google.com cached? {is_cached('google.com')}")
    print(f"Is unknown.com cached? {is_cached('unknown.com')}")

    print("\nTesting get_visit_count()...")
    print(f"Visit count for google.com: {get_visit_count('google.com')}")

    print("\nTesting get_most_visited()...")
    most_visited = get_most_visited()
    if most_visited:
        print(f"Most visited: {most_visited[0]} ({most_visited[1]} visits)")

    print("\nTesting remove_from_cache()...")
    remove_from_cache("python.org")
    remove_from_cache("notcached.com")
    show_cache()

    # Interactive menu (uncomment to use)
    # while True:
    #     choice = display_menu()
    #     if choice == '1':
    #         url = input("Enter URL: ")
    #         title = input("Enter title: ")
    #         cache_page(url, title)
    #     elif choice == '2':
    #         url = input("Enter URL: ")
    #         get_title(url)
    #     elif choice == '3':
    #         url = input("Enter URL: ")
    #         print(f"Cached: {is_cached(url)}")
    #     elif choice == '4':
    #         url = input("Enter URL: ")
    #         remove_from_cache(url)
    #     elif choice == '5':
    #         show_cache()
    #     elif choice == '6':
    #         result = get_most_visited()
    #         if result:
    #             print(f"Most visited: {result[0]} ({result[1]} visits)")
    #         else:
    #             print("Cache is empty!")
    #     elif choice == '7':
    #         print("Goodbye!")
    #         break
    #     else:
    #         print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
