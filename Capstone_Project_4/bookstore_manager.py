"""
The bookstore-functions contains all the functions used in this file to communicate with the DataBase
"""
import bookstore_functions as bkf

# Initialise the database and populate it with the initial data
bkf.initialise()

while True:
    print('''
------------------------- Menu --------------------------
Choose one of the following options by typing the number.
1. Enter book
2. Update book
3. Delete book
4. Search book
5. Show all books
0. Exit''')
    menu_option = input(": ").strip()

    if menu_option == "1":
        # Create empty dictionary to store the new books information
        book = {}

        print(f"Book's title")
        book["title"] = bkf.input_validator()
        if book['title'] == "<":
            continue

        print("Book's author")
        book['author'] = bkf.input_validator()
        if book['author'] == "<":
            continue

        print("Number of books")
        book['qty'] = bkf.input_validator("int")
        if book['qty'] == "<":
            continue

        bkf.add_book(book)

    elif menu_option == "2":
        print("Type the id of the book you want to update")
        book_id = bkf.input_validator("int")
        if book_id == "<":
            continue

        # Check if book id exists in the table
        found = bkf.search_book_by_id(book_id)
        if found is None:
            print("The id you entered doesn't exist in the database.")
            continue

        print('''Choose one of the following options by typing the number.
1. Update book title
2. Update book author
3. Update book quantity
<. Go Back''')
        user_option = bkf.input_validator()
        if user_option == "<":
            continue

        if user_option == "1":
            user_option = 'Title'
            print("Enter the new book title")
        elif user_option == "2":
            user_option = 'Author'
            print("Enter the new book author")
        elif user_option == "3":
            user_option = 'Qty'
            print("Enter the new book author")
        else:
            print("The value you entered is not valid.")
            continue

        modification = bkf.input_validator()
        if modification == "<":
            continue

        bkf.update_book(book_id, user_option, modification)

    elif menu_option == "3":
        print("Type the id of the book you want to delete")
        book_id = bkf.input_validator("int")
        if book_id == "<":
            continue

        bkf.delete_book(book_id)

    elif menu_option == "4":
        print('''Choose one of the following options to search by.
1. Search by book title
2. Search by book author
3. Search by book quantity
<. Go Back''')
        user_option = bkf.input_validator()
        if user_option == "<":
            continue

        if user_option == "1":
            user_option = 'Title'
            print("Enter the Title you want to search for")
        elif user_option == "2":
            user_option = 'Author'
            print("Enter the Author you want to search for")
        elif user_option == "3":
            user_option = 'Qty'
            print("Enter the quantity of books to search for")
        else:
            print("The value you entered is not valid.")
            continue

        criteria = bkf.input_validator()
        if criteria == "<":
            continue

        bkf.search_book(user_option, criteria)

    elif menu_option == "5":
        bkf.show_all()
    elif menu_option == "0":
        break
    else:
        print("The option selected is not valid.")