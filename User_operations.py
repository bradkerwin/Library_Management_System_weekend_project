users = []
class User_operations():
    def __init__(self):
        self.name = ""
        self.library_ID = ""

    def new_user(self, name, library_ID):
        self.name = name
        self.library_ID = library_ID
        new_user_info = {"name": self.name, "library_ID": self.library_ID}
        print(f"Congrats! The new user {self.name} {self.library_ID} has been created successfully!")
        users.append(new_user_info)


    def user_details(self):
        while True:
            user_search = input("Please enter the name of the user you are looking for. ").title()
            for user in users:
                if user_search in user.values():
                    print(user)
                    return
            print("User not found.")
            break

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
                lib_id = input("Enter the user's Library ID: ")
                self.new_user(name, lib_id)
            elif select == '2':
                self.user_details()
            elif select == '3':
                print(users)
            elif select == '4':
                break
            else:
                print("Invalid Entry. Please try again.")
                continue
