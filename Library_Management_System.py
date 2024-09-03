# Library Management System

class Library_Management_System:
    def __init__(self):
        """To store books"""
        self.books = {}
    
    def add_books(self, title, author): #To add books
        """To add books to library"""
        if title not in self.books:
            self.books[title] = {"author":author, "available":True}
            print(f"{title} by {author} successfully added to the library.")
        else:
            print(f"{title} by {author} is already available in the library.")
    
    def lend_book(self, title, author): #To delete books
        """To lend a book from library"""
        if title in self.books:
            self.books[title] = {"author":author, "available":False}
            print(f"You've successfully borrowed {title} by {author}.")
        else: print(f"{title} by {author} is not available in library.")
    
    def donate_books(self, title, author): #Same as add_books
        """To add books to library"""
        if title not in self.books:
            self.books[title] = {"author":author, "available":True}
            print(f"{title} by {author} successfully added to the library.")
        else:
            print(f"{title} by {author} is already available in the library.")
    
    def return_book(self, title, author):
        """To return books"""
        if title in self.books:
            self.books[title] = {"author":author, "available":True}
            print(f"Thank you for returning {title} by {author} book.")
        else: print("You've not borrowed this book from our library.")


my_library = Library_Management_System()
show_books = my_library.books

while(True):
    choice = int(input("Options:\n-----------------\n1. Add Books \n2. Show Books\n3. Lend Books\n4. Donate Books\n5. Return Book\n0. Exit\nChoose: "))
    if choice == 1:
        title = input("Enter title of the book: ")
        author = input("Enter author name of the book: ")
        my_library.add_books(title, author)
    elif choice == 2:
        for title, author in show_books.items():
            if author['available']:
                print(f"{title} by {author['author']}")
    elif choice == 3:
        title = input("Enter title of the book: ")
        author = input("Enter author name of the book: ")
        my_library.lend_book(title, author)
    elif choice == 4:
        title = input("Enter title of the book: ")
        author = input("Enter author name of the book: ")
        my_library.donate_books(title, author)
    elif choice == 5:
        title = input("Enter title of the book: ")
        author = input("Enter author name of the book: ")
        my_library.return_book(title, author)
    elif choice == 0: break
    else: continue