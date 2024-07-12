class Author():
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

class Author_operations():
    def __init__(self):
        self.authors = []    

    def new_author(self, name, biography):
        self.name = name
        self.biography = biography
        new_author_info = Author(name, biography)
        print(f"The new author {self.name} has been added with the bio: {self.biography}.")
        self.authors.append(new_author_info)
    
    def author_details(self):
        while True:
            author_select = input("Search for an author: ").title()
            for author in self.authors:
                if author_select == author.name:
                    print(f"{author.name}: {author.biography}")
                    return
            print("Author not found.")
            break

    def display_authors(self):
        for author in self.authors:
            print('='*30)
            print(f"Author name: {author.name}; Author bio: {author.biography}.")
            print('='*30)
    
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
                self.display_authors()
            elif select == '4':
                break
            else:
                print("Invalid Entry. Please try again.")
                continue
