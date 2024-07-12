class Book():
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.status = "Available"

class Book_operations():
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        new_book_info = Book(title, author, genre, publication_date)
        self.books.append(new_book_info)

    def borrow_book(self):
        while True:
            book_select = input("What book would you like to borrow?: ").title()
            for book in self.books:
                if book_select == book.title and book.status == "Available":
                    print(f"You may borrow {book_select}. Thank you.")
                    book.status = "Not available"
                    self.books.remove(book)
                    self.borrowed_books.append(book)
                    return                
            print("It appears that book is not available at the moment. Please try again later.")
            break

    def return_book(self):
        while True:
            book_return = input("What book are you returning? ").title()
            for book in self.books:
                if book_return == book.title and book.status == "Available":
                        print("Looks like that book is still here.")
                        return
            for book in self.borrowed_books:
                if book_return == book.title and book.status == "Not available":
                    print(f"Thank you for returning {book_return}. Have a great day.")
                    self.borrowed_books.remove(book)
                    self.books.append(book)
                    book.status = "Available"
                    return
            print("There's no record of that book on file.")
            break

    def search_book(self):
        while True:
            book_search = input("What book are you looking for? ").title()
            for book in self.borrowed_books:
                if book_search == book.title:
                    print("Looks like that book is being borrowed at the moment.")
                    return
            for book in self.books:
                if book_search == book.title:
                    print(f"{book.title} by {book.author} is {book.status}")
                    return
            print("Book not found. Please try again later.")
            break

    def display_books(self):
        for book in self.books:
            print('='*30)
            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Publication Date: {book.publication_date}, Availability: {book.status.upper()}")
            print('='*30)
        for book in self.borrowed_books:
            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Publication Date: {book.publication_date}, Availability: {book.status.upper()}")
            print('='*30)


    def get_books_menu(self):
        while True:
            select = input(''' 
Book Operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
6. Return to Main Menu
''')
            if select == '1':
                title = input("Please enter the title. ").title()
                author = input("Please enter the author. ").title()
                genre = input("Please enter the genre. ").title()
                pub_date = input("Please enter the publication date. ")
                self.add_book(title, author, genre, pub_date)
            elif select == '2':
                self.borrow_book()
            elif select == '3':
                self.return_book()
            elif select == '4':
                self.search_book()
            elif select == '5':
                self.display_books()
            elif select == '6':
                break
            else:
                print("Invalid Entry. Please try again.")
                continue