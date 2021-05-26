import sqlite3

MyBook = sqlite3.connect('bookdatabase.db')
cursbook = MyBook.cursor()
cursbook.execute(''' CREATE TABLE Books(
    Name TEXT PRIMARY KEY,
    Author TEXT,
    Price INTEGER,
    Copies INTEGER); ''')
MyBook.close()
