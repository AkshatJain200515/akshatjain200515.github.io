class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def check_out(self) -> str:
        if self.is_checked_out:
            return f"The book '{self.title}' is already checked out."
        self.is_checked_out = True
        return f"The book '{self.title}' has been checked out."

    def return_book(self) -> str:
        if not self.is_checked_out:
            return f"The book '{self.title}' was not checked out."
        self.is_checked_out = False
        return f"The book '{self.title}' has been returned."


class Member:
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book: Book) -> str:
        if book.is_checked_out:
            return f"The book '{book.title}' is currently checked out."
        self.borrowed_books.append(book)
        book.check_out()
        return f"{self.name} has borrowed the book '{book.title}'."

    def return_book(self, book: Book) -> str:
        if book not in self.borrowed_books:
            return f"The book '{book.title}' was not borrowed by {self.name}."
        self.borrowed_books.remove(book)
        book.return_book()
        return f"{self.name} has returned the book '{book.title}'."


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book: Book) -> str:
        self.books.append(book)
        return f"The book '{book.title}' has been added to the library."

    def add_member(self, member: Member) -> str:
        self.members.append(member)
        return f"The member '{member.name}' has been added to the library."

    def find_book_by_title(self, title: str) -> Book:
        for book in self.books:
            if book.title.lower() == title.lower(): 
                return book
        return None

    def find_member_by_name(self, name: str) -> Member:
        for member in self.members:
            if member.name.lower() == name.lower():  
                return member
        return None


def add_book(title, author, isbn, library):  # Function to add book
    book = Book(title, author, isbn)
    print(library.add_book(book))


def add_member(name, mem_id, library):  # Function to add member
    member = Member(name, mem_id)
    print(library.add_member(member))


def borrow_book(member_name, book_title, library):  # Function to borrow book
    member = library.find_member_by_name(member_name)
    book = library.find_book_by_title(book_title)
    
    if member and book:
        print(member.borrow_book(book))
    else:
        print("Invalid member or book.")


def return_book(member_name, book_title, library):  # Function to return book
    member = library.find_member_by_name(member_name)
    book = library.find_book_by_title(book_title)
    
    if member and book:
        print(member.return_book(book))
    else:
        print("Invalid member or book.")


# Main program loop
if __name__ == "__main__":
    library = Library()

    while True:
        choice = int(input("\n\n1- Add Book\n2- Add Member\n3- Borrow Book\n4- Return Book\n5- Exit\nEnter your choice: "))
        
        if choice == 1:
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            isbn = input("Enter ISBN: ")
            add_book(title, author, isbn, library)

        elif choice == 2:
            name = input("Enter Member Name: ")
            mem_id = input("Enter Member ID: ")
            add_member(name, mem_id, library)

        elif choice == 3:
            member_name = input("Enter Member Name: ")
            book_title = input("Enter Book Title to Borrow: ")
            borrow_book(member_name, book_title, library)

        elif choice == 4:
            member_name = input("Enter Member Name: ")
            book_title = input("Enter Book Title to Return: ")
            return_book(member_name, book_title, library)

        elif choice == 5:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")
