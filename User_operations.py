class User():
    def __init__(self, name, library_ID):
        self.name = name
        self.library_ID = library_ID

class User_operations():
    def __init__(self):
        self.users = []

    def new_user(self, name, library_ID):
        self.name = name
        self.library_ID = library_ID
        new_user_info = User(name, library_ID)
        print(f"Congrats! The new user {self.name} with the library ID: {self.library_ID} has been created successfully!")
        self.users.append(new_user_info)


    def user_details(self):
        while True:
            user_search = input("Please enter the name of the user you are looking for. ").title()
            for user in self.users:
                if user_search == user.name:
                    print(f"Name: {user.name}, Library_ID: {user.library_ID}.")
                    return
            print("User not found.")
            break

    def display_users(self):
        for user in self.users:
            print('='*30)
            print(f"User name: {user.name}, User Library ID: {user.library_ID}.")
            print('='*30)

    def get_user_menu(self):
        while True:
            select = input(''' 
        User Operations:
        1. Add a new user
        2. View user details
        3. Display all users
        4. Return to main menu
        ''')
            if select == '1':
                name = input("Enter the user's name: ").title()
                lib_id = input("Create a Library ID for the user: ")
                self.new_user(name, lib_id)
            elif select == '2':
                self.user_details()
            elif select == '3':
                self.display_users()
            elif select == '4':
                break
            else:
                print("Invalid Entry. Please try again.")
                continue
