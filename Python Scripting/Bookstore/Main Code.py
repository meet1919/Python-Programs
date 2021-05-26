import sqlite3

MyBook = sqlite3.connect('bookdatabase.db')
cursbook = MyBook.cursor()

Title = str(input('Enter Book Name: '))
print('Name, Author, Price, Number of Copies')
query = '''SELECT * from Books where Name = '%s' ''' % (Title,)
cursbook.execute(query)
data = cursbook.fetchall()
print(data)

book_tuple = data[0]
price_book = (book_tuple[2])
number_of_copies = int(input('How many copies you want: '))
total_cost = number_of_copies * price_book
more_books = str(input('Add more books(Y/N): '))

if more_books == 'N':
    print('Your total cost for {} books is {}'.format(number_of_copies, total_cost))

elif more_books == 'Y':
    Title = str(input('Enter Book Name: '))
    print('Name, Author, Price, Number of Copies')
    query = '''SELECT * from Books where Name = '%s' ''' % (Title,)
    cursbook.execute(query)
    data1 = cursbook.fetchall()
    print(data1)

    book_tuple1 = data1[0]
    price_book1 = (book_tuple1[2])
    number_of_copies1 = int(input('How many copies you want: '))
    total_books = number_of_copies + number_of_copies1
    total_cost1 = number_of_copies1 * price_book1
    total = total_cost + total_cost1
    print('Your total cost for {} books is {}'.format(total_books, total))
