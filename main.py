""" Program to create and manage a list of books that the user wishes to read, and books that the user has read. """

from bookstore import BookStore
from menu import Menu
import ui

store = BookStore()

QUIT = 'Q'


def main():

    menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice == QUIT:
            break


def create_menu():
    menu = Menu()
    menu.add_option('1', 'Add Book', add_book)
    menu.add_option('2', 'Search For Book', search_book)
    menu.add_option('3', 'Show Unread Books', show_unread_books)
    menu.add_option('4', 'Show Read Books', show_read_books)
    menu.add_option('5', 'Show All Books', show_all_books)
    menu.add_option('6', 'Change Book Read Status', change_read)
    menu.add_option('7', 'Delete a Book', delete_book)
    menu.add_option(QUIT, 'Quit', quit_program)

    return menu


def add_book():
    new_book = ui.get_book_info()
    store.add_book(new_book)
    # TODO show an error message if a book is already in the store, don't add book


def show_read_books():
    read_books = store.get_books_by_read_value(True)
    ui.show_books(read_books)


def show_unread_books():
    unread_books = store.get_books_by_read_value(False)
    ui.show_books(unread_books)


def show_all_books():
    books = store.get_all_books()
    ui.show_books(books)


def search_book():
    search_term = ui.ask_question('Enter search term, will match partial authors or titles.')
    matches = store.book_search(search_term)
    ui.show_books(matches)


def change_read():
    # use try - catch blocks to display the error message if book not found
    try:
        book_id = ui.get_book_id()
        new_read = ui.get_read_value()
        store.set_book_read(book_id, new_read)
    except Exception as not_found:
        print('Book Does Not Exist in the List!', not_found)

    # TODO show error message if book's ID is not found.

def delete_book():

    delete_id = ui.get_book_id()

    try:
        store.delete_book(delete_id)
    except Exception as does_not_exist:
        print('This ID does not exist in the list!', does_not_exist)



def quit_program():
    ui.message('Thanks and bye!')


if __name__ == '__main__':
    main()
