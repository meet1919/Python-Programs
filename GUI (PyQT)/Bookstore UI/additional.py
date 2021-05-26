        self.pushButton.pressed.connect(self.Get_Price)
        self.pushButton_2.pressed.connect(self.Total)
        self.cost = 0



    def Get_Price(self):
        import sqlite3
        MyBook = sqlite3.connect('bookdatabase.db')
        cursbook = MyBook.cursor()
        name = str(self.t1.text())
        query = '''SELECT * from Books where Name = '%s' ''' % (name,)
        cursbook.execute(query)
        data = cursbook.fetchall()
        book_tuple = data[0]
        name_book = book_tuple[0]
        self.price = book_tuple[2]
        if name == name_book:
            self.t2.setText(str(self.price))
            self.cost = int(self.price)
        else:
            return 'Book not found'

    def Total(self):
        self.num = float(self.t3.text())
        self.t4.setText(str(self.cost * self.num))

