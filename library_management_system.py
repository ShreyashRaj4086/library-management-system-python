books = [
    {"id": "B001", "title": "Clean Code", "author": "Robert C. Martin", "genre": "Programming", "year": "2008", "issued_to": None},
    {"id": "B002", "title": "The Pragmatic Programmer", "author": "Hunt & Thomas", "genre": "Programming", "year": "1999", "issued_to": None},
    {"id": "B003", "title": "Dune", "author": "Frank Herbert", "genre": "Sci-Fi", "year": "1965", "issued_to": None},
    {"id": "B004", "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "year": "1960", "issued_to": None},
    {"id": "B005", "title": "A Brief History of Time", "author": "Stephen Hawking", "genre": "Science", "year": "1988", "issued_to": "Alice Smith"},
]

def add_book():
    print("\n--- Add Book ---")
    book_id = input("Book ID: ")
    if any(b["id"] == book_id for b in books):
        print("Book ID already exists!")
        return
    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    year = input("Year: ")
    books.append({"id": book_id, "title": title, "author": author, "genre": genre, "year": year, "issued_to": None})
    print(f"Book '{title}' added successfully!")

def view_books():
    print("\n--- All Books ---")
    if not books:
        print("No books available.")
        return

    total = len(books)
    available = sum(1 for b in books if not b["issued_to"])
    issued = total - available

    print(f"  Total Books  : {total}")
    print(f"  Available    : {available}")
    print(f"  Issued       : {issued}")
    print("-" * 90)
    print(f"{'No.':<5} {'ID':<8} {'Title':<25} {'Author':<22} {'Genre':<15} {'Year':<6} {'Status'}")
    print("-" * 90)
    for i, b in enumerate(books, 1):
        status = f"Issued to {b['issued_to']}" if b["issued_to"] else "Available"
        print(f"{i:<5} {b['id']:<8} {b['title']:<25} {b['author']:<22} {b['genre']:<15} {b['year']:<6} {status}")
    print("-" * 90)
    print(f"  Showing {total} book(s) | {available} available, {issued} issued")

def search_book():
    print("\n--- Search Book ---")
    query = input("Enter title, author, or ID to search: ").lower()
    results = [b for b in books if query in b["id"].lower() or query in b["title"].lower() or query in b["author"].lower()]
    if not results:
        print("No books found.")
        return
    print(f"\nFound {len(results)} result(s):\n")
    for b in results:
        status = f"Issued to {b['issued_to']}" if b["issued_to"] else "Available"
        print(f"  [{b['id']}] {b['title']} by {b['author']} | {b['genre']} | {b['year']} | {status}")

def issue_book():
    print("\n--- Issue Book ---")
    book_id = input("Enter Book ID: ")
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        print("Book not found.")
        return
    if book["issued_to"]:
        print(f"Book already issued to {book['issued_to']}.")
        return
    member = input("Enter Member Name: ")
    book["issued_to"] = member
    print(f"Book '{book['title']}' issued to {member}.")

def return_book():
    print("\n--- Return Book ---")
    book_id = input("Enter Book ID: ")
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        print("Book not found.")
        return
    if not book["issued_to"]:
        print("This book was not issued.")
        return
    print(f"Book '{book['title']}' returned from {book['issued_to']}. Thank you!")
    book["issued_to"] = None

def delete_book():
    print("\n--- Delete Book ---")
    book_id = input("Enter Book ID to delete: ")
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        print("Book not found.")
        return
    if book["issued_to"]:
        print(f"Cannot delete — book is currently issued to {book['issued_to']}.")
        return
    books.remove(book)
    print(f"Book '{book['title']}' deleted successfully.")

def show_summary():
    total = len(books)
    available = sum(1 for b in books if not b["issued_to"])
    issued = total - available
    print(f"\n  Library Summary: {total} total | {available} available | {issued} issued")

def menu():
    print("\n" + "=" * 45)
    print("      Welcome to the Library System!")
    print("=" * 45)
    print(f"  {len(books)} books loaded and ready.")

    while True:
        show_summary()
        print("\n===== Library Management System =====")
        print("  1. Add Book")
        print("  2. View Books")
        print("  3. Search Book")
        print("  4. Issue Book")
        print("  5. Return Book")
        print("  6. Delete Book")
        print("  7. Exit")
        print("=====================================")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            total = len(books)
            available = sum(1 for b in books if not b["issued_to"])
            print("\n" + "=" * 45)
            print("        Thank you for using LibraryPro!")
            print("=" * 45)
            print(f"  Books in catalog : {total}")
            print(f"  Currently issued : {total - available}")
            print(f"  Available        : {available}")
            print("\n  Have a great day! Goodbye. 📚")
            print("=" * 45 + "\n")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

menu()