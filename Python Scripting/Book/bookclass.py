class book:
    def __init__(self, tle, athr, pub, prc, cps):
        self.title = input('Enter Title: ')
        self.name = input('Enter Author name: ')
        self.publisher = input('Enter Publisher: ')
        self.price = int(input('Enter Price of book: '))
        self.copies = int(input('Enter number of copies sold: '))

    def get_title(self):
        return self.title

    def get_name(self):
        return self.name

    def get_publisher(self):
        return self.publisher

    def get_price(self):
        return self.price

    def royalty(self):
        rlty = 0
        if self.copies <= 500:
            rlty = rlty + (10 * self.copies * self.price) / 100
        elif 500 < self.copies < 1500:
            rlty = rlty + (10 * 500 * self.price) / 100
            rlty = rlty + (12.5 * (self.copies - 500) * self.price) / 100
        elif self.copies == 1500:
            rlty = rlty + (10 * 500 * self.price) / 100
            rlty = rlty + (12.5 * 1000 * self.price) / 100
        elif self.copies >= 1500:
            rlty = rlty + (10 * 500 * self.price) / 100
            rlty = rlty + (12.5 * 1000 * self.price) / 100
            rlty = rlty + (15 * (self.copies - 1500) * self.price) / 100
        return rlty


class ebook(book):
    def __init__(self, tle, athr, pub, prc, cps, epub, mobi, pdf):
        super().__init__(tle, athr, pub, prc, cps)
        self.Epub = epub
        self.Mobi = mobi
        self.Pdf = pdf

    def royalty(self):
        rlty = 0
        if self.copies <= 500:
            rlty = rlty + (10 * self.copies * self.price) / 100
            rlty = rlty - ((rlty * 12) / 100)
        elif 500 < self.copies < 1500:
            rlty = rlty + (10 * 500 * self.price) / 100
            rlty = rlty + (12.5 * (self.copies - 500) * self.price) / 100
            rlty = rlty - ((rlty * 12) / 100)
        elif self.copies == 1500:
            rlty = rlty + (10 * 500 * self.price) / 100
            rlty = rlty + (12.5 * 1000 * self.price) / 100
            rlty = rlty - ((rlty * 12) / 100)
        elif self.copies >= 1500:
            rlty = rlty + (10 * 500 * self.price) / 100
            rlty = rlty + (12.5 * 1000 * self.price) / 100
            rlty = rlty + (15 * (self.copies - 1500) * self.price) / 100
            rlty = rlty - ((rlty * 12) / 100)
        return rlty


print('Which type of book is sold: \n 1) Paperback\n 2) Ebook')
book_type = input('Enter your book type: ')

if book_type.upper() == 'PAPERBACK':
    b1 = book('tle', 'athr', 'pub', 'prc', 'cps')
    print('The title of book is {}'.format(b1.get_title()))
    print('Name of Author is {} and Publisher is {}'.format(b1.get_name(), b1.get_publisher()))
    print('Price of the book in ₹ is {}'.format(b1.get_price()))
    print('Royalty received to {} is ₹{}'.format(b1.get_name(), b1.royalty()))

elif book_type.upper() == 'EBOOK':
    eb1 = ebook('tle', 'athr', 'pub', 'prc', 'cps', 'epub', 'mobi', 'pdf')
    print('Royalty received to {} (deducting 12% GST on ebook) is ₹{}: '.format(eb1.get_name(), eb1.royalty()))

else:
    print('Invalid book format')
