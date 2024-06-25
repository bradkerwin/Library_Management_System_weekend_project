# Library Management System:
from User_operations import User_operations
from Author_operations import Author_operations
from Book_operations import Book_operations

class Main():
    
    def __init__(self):
        self.user_operations = User_operations()
        self.author_operations = Author_operations()
        self.book_operations = Book_operations()

    def main_menu(self):
        while True:
            user = input('''
    Welcome to the Library Management System!

        Main Menu:
        1. Book Operations
        2. User Operations
        3. Author Operations
        4. Quit
    ''')
            if user == '1':
                self.book_operations.get_books_menu()
            elif user == '2':
                self.user_operations.get_user_menu()
            elif user == '3':
                self.author_operations.get_author_menu()
            elif user == '4':
                print("Thanks for using our Library Management System. Have a great day")
                break
            else:
                print("Invalid entry. Please try again.")
                continue

main_page = Main()
main_page.main_menu()