from utils import database as db


USER_CHOICE = """ 
Enter 
'a' to add a book
'l' to list  all books
'r' to mark a book as read
'd' to delete a book
'q' to quit

"""

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
           prompt_add_book()

        elif user_input == 'l':
            list_books()

        elif user_input == 'r':
            prompt_read_book()

        elif user_input == 'd':
            prompt_delete_book()

        else:
            print('Please try again')
        # elif user_input == 'q':
        #     print('Stopping Program...')

        user_input = input(USER_CHOICE)
    print('End')
        

"""
def prompt_add_book()  ask for book name and author
def list_books() show all books in our list
def prompt_read_book() ask for book name and change it to 'read' in our list
def prompt_delete_book() ask for book name and remove book from list

"""

def prompt_add_book():
    title = input('Enter book name :')
    author = input('Enter author :')
    db.add_book(title, author)
    print('Book added')

    
def list_books():
    # for book in db.books:
    #     print(f"Title : {book['name']}\nAuthor: {book['author']}")
    books = db.get_all_books()
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"{book['name']} by {book['author']}, read : {read}")

def prompt_read_book():
    name = input('Enter name of book you just finished reading: ')
    db.mark_book_as_read(name)
    


def prompt_delete_book():
    name = input('Enter name of book to delete : ')
    db.delete_book(name)




menu()