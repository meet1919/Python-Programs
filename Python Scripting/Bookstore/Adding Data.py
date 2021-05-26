import sqlite3

MyBook = sqlite3.connect('bookdatabase.db')
cursbook = MyBook.cursor()
Row1 = '''INSERT INTO Books (Name, Author, Price, Copies) VALUES ('Zero to One', 'Peter Thiel', 330, 4)'''
Row2 = '''INSERT INTO Books (Name, Author, Price, Copies) VALUES ('Thinking Fast and Slow', 'Daniel Kahnmen', 450, 10)'''
Row3 = '''INSERT INTO Books (Name, Author, Price, Copies) VALUES ('My Inventions', 'Nikola Tesla', 150, 3)'''
Row4 = '''INSERT INTO Books (Name, Author, Price, Copies) VALUES ('A Brief History of Time', 'Stephan Hawking', 250, 5)'''
Row5 = '''INSERT INTO Books (Name, Author, Price, Copies) VALUES ('The Untethered Soul', 'Michael Singer', 170, 6)'''
cursbook.execute(Row1)
cursbook.execute(Row2)
cursbook.execute(Row3)
cursbook.execute(Row4)
cursbook.execute(Row5)
MyBook.commit()

