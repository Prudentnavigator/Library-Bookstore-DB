# Lesson SE-T48
# Task Capstone Project-V Database SQLite


# ebookstore.py--a program that can be used by a bookstore or library.


# Import SQLite module
import sqlite3

# Create or open a DB file named ebookstore.db.
db = sqlite3.connect('ebookstore.db')
cursor = db.cursor()  

# Create table named books if it does not exist.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT,
                   	Qty INTEGER)
    ''')

db.commit()

# A function to search for a book by it's id.
def search_bookId(book_id):
    try:
        cursor.execute('''
        SELECT id, Title, Author, Qty FROM books WHERE id = ?''', (book_id,))
        book = cursor.fetchone()
        return(f'''
                            id: {book[0]}
                            Title: {book[1]}
                            Author: {book[2]}
                            Quantity: {book[3]} ''')
    except TypeError:
        return False

# A function to search for a book by it's Title.
def search_bookTitle(title):
    try:
        cursor.execute('''
        SELECT id, Title, Author, Qty FROM books WHERE Title = ?''', (title,))
        book = cursor.fetchone()
        return(f'''
                            id: {book[0]}
                            Title: {book[1]}
                            Author: {book[2]}
                            Quantity: {book[3]} ''')
    except TypeError:
        return False 

# A function to search for a book by it's Author.
def search_bookAuthor(author):
    try:
        cursor.execute('''
        SELECT id, Title, Author, Qty FROM books WHERE Author = ?''', (author,))
        book = cursor.fetchone()
        return(f'''
                            id: {book[0]}
                            Title: {book[1]}
                            Author: {book[2]}
                            Quantity: {book[3]} ''')
    except TypeError:
        return False        

# A function to update book information (quantity of books).
def update_book(book_id, quantity):
    try:
        cursor.execute('''UPDATE books SET QTY = ? WHERE id = ? ''', (quantity, book_id))
        db.commit()

    except TypeError:
        return False

# A function to add a book to the DB.
def add_book(book_id, title, author, quantity):
    new_book = [(book_id, title, author, quantity)] 

    # Insert the book values into the book table.
    cursor.executemany('''INSERT or IGNORE INTO books(id,Title,Author,Qty)VALUES(?,?,?,?)''',new_book)
    db.commit()

# A function to delete a book.
def delete_book(book_id):
    cursor.execute('''DELETE FROM books WHERE id = ? ''', (book_id,))
    db.commit()

# A function that returns the id of the last entry from the books table.
def last_id():
    try:
        cursor.execute(''' SELECT id FROM books ''')
        for row in cursor:
            last_id = row

        return print(f'''
                            Last id of the books: {last_id[0]}''')
    except UnboundLocalError:
        return print(''' 
                            *** There are no entries in the database ***

                    Please check that ebookstore.db is in the same folder/directory
                    as ebookstore.py or add books to the DB if you're just starting 
                    to create a new database.
                    ''')

# Display the name of the program.
print('''
                    ------------------ ebookstore.py -------------------
                    ''')

# Display a main-menu that allows the user to search, update quanties, add and delete
#   books from the books table in the database.
while True:
    menu = input('''
                    ____________________________________________________

                    ---Please enter a number of the following options---
    
                            1 - Search the database for a book
                            2 - Update the quantity of a book
                            3 - Add new books to the database 
                            4 - Delete books from the database 
                            0 - Exit the program
                    
                            : ''')
    
    if menu == "0":
        print(''' 
                    ---------------------- Goodby! ---------------------
                                            ''')
        exit()

    # Sub-menu for searching books by id, title or author.
    elif menu == "1":
        while True:
            print("""
                    ____________________________________________________
    
                            ---Search the database for a book---
                             
                             Choose one of the following options

                                    1 - Search by id
                                    2 - by Title
                                    3 - by Author
                                    q - Quit this menu
                             """)
            choice = input('''
                            Please enter: ''')
    
            if choice == "q":
                break

            elif choice == "1":

                # Display the last id of the book table.
                last_id()
                book_id = input('''
                            Please enter the id: ''')

                if search_bookId(book_id) == False:
                    print('''
                    *** There is no book with that id in the database *** ''')
                else:
                    print(search_bookId(book_id))

            elif choice == "2":
                title = input('''
                            Please enter the Title: ''')

                if search_bookTitle(title) == False:
                    print('''
                    *** There is no book with that title in the database *** ''')

                else:
                    print(search_bookTitle(title))

            elif choice == "3":
                author = input('''
                            Please enter the Author: ''')

                if search_bookAuthor(author) == False:
                    print('''
                   *** There is no book from this author in the database *** ''')

                else:
                    print(search_bookAuthor(author))

            else:
                print("""
                            *** This option is not available *** """)

    # Sub-menu for updating the quantity of a book.
    elif menu == "2":
        while True:
            print("""
                    ___________________________________________________

                            ---Update the quantity of a book---
                         
                                 To quit this menu enter q 
                         """)
    
            while True:
                book_id = input('''
                            Enter id number: ''')
    
                if book_id == "q":
                    break

                elif search_bookId(book_id) == False:
                    print('''
                    *** There is no book with that id in the database *** ''')
    
                else:
                    print("     ", search_bookId(book_id))
                    break

            if book_id == "q":
                    break

            while True:
                quantity = input('''
                            Enter the quantity: ''')

                if quantity.isdigit() or quantity == "q":
                    break

                else:
                    print('''
                              *** Quantity must be numeric *** ''')

            if quantity == "q":
                print('''
                           *** Book updated has been aborted *** ''')

                break

            else:
                update_book(book_id, quantity)
                print('''
                              *** The book has been updated *** ''')
            
    # Sub-menu for adding new books.
    elif menu == "3":
        while True:
            print("""
                    ____________________________________________________

                            ---Add a new book to the database---
                         
                                  To quit this menu enter q 
                         """)
    
            # Display the last id of the book table.
            last_id()

            while True:
                book_id = input('''
                            Enter id number: ''')

                if book_id.isdigit():
                    if search_bookId(book_id) == False: 
                        break

                    else:
                        print('''
                                  ***Id already exists*** ''')

                elif book_id == "q":
                    break

                else:
                    print('''
                               *** The id must be numeric ***
                                     or enter q to quit ''')
            if book_id == "q":
                    break
                
            while True:
                title = input('''
                            Title: ''')

                if title == "q":
                    break

                author = input('''
                            Enter the author: ''')

                if author == "q":
                    break

                elif search_bookTitle(title) == False and search_bookAuthor(author) == False: 
                    break           

                else:
                    print('''
                        *** This book is already in the database *** ''')

            if title == "q":
                break

            if author == "q":
                break

            while True:
                quantity = input('''
                            Enter the quantity: ''')

                if quantity.isdigit() or quantity == "q":
                    break

                else:
                    print('''
                            *** Quantity must be numeric ***
                                   or enter q to quit ''')

            if quantity == "q":
                break

            add_book(book_id, title, author, quantity)
            print('''
                            *** The book has been added *** ''')

    
    # Sub-menu for deleting books.
    elif menu == "4":
        while True:
            print("""
                    ____________________________________________________

                            ---Delete books from the database---
                         
                                 To quit this menu enter q 
                         """)
        
            book_id = input('''
                            Enter id number: ''')

            if book_id == "q":
                break

            elif search_bookId(book_id) == False: 
                print('''
                           *** There is no entry with that id ***
                            ''')

            else:
                print(search_bookId(book_id))
                remove = input('''
                            Would you like to delete this book y/n: ''')

                if remove.lower() == "y":
                    delete_book(book_id)
                    print('''
                            *** The book has been deleted ***
                            ''')
                else:
                    print('''
                         *** The book deletion has been aborted *** ''')
                    break

    else:
        print("""
                           *** This option is not available *** """)

db.close()
