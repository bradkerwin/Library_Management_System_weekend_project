authors = []
class Author_operations():
    def __init__(self):
        self.name = ""
        self.biography = ""    

    def new_author(self, name, biography):
        self.name = name
        self.biography = biography
        new_author_info = {"Name": self.name, "Bio": self.biography}
        print(f"The new author {self.name} has been added with the bio {self.biography}.")
        authors.append(new_author_info)
    
    def author_details(self):
        while True:
            author_select = input("Search for an author: ").title()
            for author in authors:
                if author_select in author.values():
                    print(author)
                    return
            print("Author not found.")
            break
    
    def get_author_menu(self):
        while True:
            select = input(''' 
        Author Operations:
        1. Add a new author
        2. View author details
        3. Display all authors
        4. Return to main menu
        ''')
            if select == '1':
                author_name = input("What is the name of the new author? ").title()
                author_bio = input("Tell us a little bit about the author. ")
                self.new_author(author_name, author_bio)
            elif select == '2':
                self.author_details()
            elif select == '3':
                print(authors)
            elif select == '4':
                break
            else:
                print("Invalid Entry. Please try again.")
                continue
