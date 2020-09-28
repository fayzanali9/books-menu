from utils import database as db

user_value = """
a to add  a bookmark
l to list all books
d to delete a book 
r to read a book
q to quit
Your option : """


def menu():
    db.create_book_table()
    user_input = input(user_value)
    print()
    while user_input != "q":
        if user_input == "a":
            add_book()
        elif user_input == "l":
            list_books()
        elif user_input == "d":
            delete_book()
        elif user_input == "r":
            read_book()
        else:
            print("Invalid user_input")
        user_input = input(user_value)
        print()
    print('End')


def add_book():
    name = input("Enter name of the book to add : ")
    author = input("Enter author : ")
    db.add_book(name,author)


def list_books():
    books = db.get_all_books()
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"{book['name']} by {book['author']} ,read : {read}\n")


def read_book():
    name = input('Enter the name of the book you just read : ')
    db.mark_as_read(name)


def delete_book():
    name = input('Enter the name to delete the book : ')
    db.delete_book(name)


menu()