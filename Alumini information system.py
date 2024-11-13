# Initialize an empty list to store books
books = []

# Menu to perform actions
while True:
    print("\n=== Book Information System ===")
    print("1. Add a book")
    print("2. View all books")
    print("3. Search for a book")
    print("4. Update book information")
    print("5. Delete a book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':  # Add a new book
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        
        # Store the book as a dictionary in the list
        books.append({'title': title, 'author': author, 'year': year})
        print(f"Book '{title}' added successfully.")
    
    elif choice == '2':  # View all books
        if len(books) == 0:
            print("No books in the system.")
        else:
            print("Books in the system:")
            for book in books:
                print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    
    elif choice == '3':  # Search for a book
        search_title = input("Enter the title of the book to search: ")
        found = False
        for book in books:
            if book['title'].lower() == search_title.lower():
                print(f"Book found: Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
                found = True
                break
        if not found:
            print(f"No book found with title '{search_title}'.")
    
    elif choice == '4':  # Update book information
        old_title = input("Enter the title of the book to update: ")
        updated = False
        for book in books:
            if book['title'].lower() == old_title.lower():
                # Update the book details
                new_title = input("Enter new title: ")
                new_author = input("Enter new author: ")
                new_year = input("Enter new publication year: ")
                
                book['title'] = new_title
                book['author'] = new_author
                book['year'] = new_year
                print(f"Book '{old_title}' updated to '{new_title}'.")
                updated = True
                break
        if not updated:
            print(f"No book found with title '{old_title}'.")
    
    elif choice == '5':  # Delete a book
        delete_title = input("Enter the title of the book to delete: ")
        deleted = False
        for book in books:
            if book['title'].lower() == delete_title.lower():
                books.remove(book)
                print(f"Book '{delete_title}' deleted successfully.")
                deleted = True
                break
        if not deleted:
            print(f"No book found with title '{delete_title}'.")
    
    elif choice == '6':  # Exit
        print("Exiting the system.")
        break
    
    else:
        print("Invalid choice. Please try again.")
