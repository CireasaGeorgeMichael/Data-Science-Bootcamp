"""
This module contains all the functions used in the bookstore_manager
"""
import sqlite3

def input_validator(type='str'):
    ipt = input(": ").strip()

    # Check if input is going back to main menu
    if ipt == "<":
        return ipt

    # Check if field is empty
    if len(ipt) == 0:
        print("This field can't be empty.\nTry again or type '<' to go back to menu.")
        ipt = input_validator(type)

    # In case the input type needs to be an integer number
    if type == "int":
        try:
            ipt = int(ipt)
        except ValueError:
            print("The value entered is invalid.\nTry again or type 0 to go back to menu.")
            ipt = input_validator(type)

    return ipt


def initialise():
    """ INITIALISE the database with the table and populate it"""
    db = sqlite3.connect('db/ebookstore')
    cursor = db.cursor()

    try:
        cursor.execute('''
        CREATE TABLE books(id INTEGER PRIMARY KEY,
                                        Title TEXT UNIQUE,
                                        Author TEXT,
                                        Qty INTEGER)''')
        db.commit()
    except Exception as _:
        pass

    initial_books = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
                     (3002, "Harry Potter the Philosopher's Stone", 'J.K. Rowling', 40),
                     (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
                     (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
                     (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)]

    try:
        cursor.executemany('''INSERT INTO books(id,Title,Author,Qty)
                            VALUES(?,?,?,?)''', initial_books)
        db.commit()
    except Exception as _:
        pass

    db.close()


def display(row):
    len1 = len(row[1])
    len2 = len(row[2])
    print(f'{row[0]} - {row[1] + " " * (40 - len1)} - {row[2] + " " * (20 - len2)} - {row[3]}')


def add_book(book):
    db = sqlite3.connect('db/ebookstore')
    cursor = db.cursor()

    # Get the biggest Id so the new added book is bigger by one
    cursor.execute("""SELECT MAX(id) FROM books""")
    max_id = cursor.fetchone()[0] + 1

    try:
        cursor.execute('''INSERT INTO books(id,Title,Author,Qty)
                            VALUES(?,?,?,?)''', (max_id, book['title'], book['author'], book['qty']))
        db.commit()
    except Exception:
        print(f" The book called {book['title']} is already in the database.")
    else:
        print("Book added successfully.")

    db.close()


def update_book(id, field, modification):
    db = sqlite3.connect('db/ebookstore')
    cursor = db.cursor()
    try:
        cursor.execute(f'''UPDATE books SET {field} = ? WHERE id=?''', (modification, id))
    except Exception:
        print("An Error while updating has occurred.")
    else:
        db.commit()
        print("Book has been successfully updated.")
    db.close()


def delete_book(id):
    db = sqlite3.connect('db/ebookstore')
    cursor = db.cursor()
    try:
        cursor.execute(f'''DELETE FROM books WHERE id=?''', (id,))
    except Exception:
        print("An Error while updating has occurred.")
    else:
        db.commit()
        print("Book has been successfully deleted.")
    db.close()


def search_book_by_id(id):
    db = sqlite3.connect('db/ebookstore')
    cursor = db.cursor()

    cursor.execute('''SELECT id FROM books WHERE id=?''', (id,))
    found = cursor.fetchone()
    db.close()
    return found


def search_book(field, condition):
    db = sqlite3.connect('db/ebookstore')
    cursor = db.cursor()

    if condition == "Qty":
        condition = int(condition)

    cursor.execute(f"""SELECT id,Title,Author,Qty
                        FROM books
                        WHERE {field} = ?""", (condition,))

    print(f' ID  -                  TITLE                   -        AUTHOR        - QTY')
    for row in cursor:
        display(row)

    db.close()


def show_all():
    db = sqlite3.connect('db/ebookstore')
    cursor = db.cursor()

    cursor.execute("""SELECT * FROM books""")

    print(f' ID  -                  TITLE                   -        AUTHOR        - QTY')
    for row in cursor:
        display(row)

    db.close()