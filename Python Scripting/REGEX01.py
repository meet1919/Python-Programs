import re


def Pattern():
    pattern = re.compile(r'(\w+)\s(\w+)')
    mo = pattern.search('wallpaper abctract')
    print(mo.group())

def Pattern1():
    text = '''
    Tesrect is the network of poets
    11223344556677889900
    meetgondaliya1999@gmail.com
    Bionic19
    abcdefghijklm
    nopqrstvuwxyz
    ABCDEFGHIJKLM
    NOPQRSTVUWXYZ
    
    _Rhyming Words_
    When cat sees the bat his hat flies and sits on the fat person he has to 
    pay money with vat added at the bank.
    
    '''
    pattern1 = re.compile(r'[^b|h]at')
    mo1 = pattern1.finditer(text)
    for match in mo1:
        print(match)

def Pattern2():
    text1 = '''
    Mr. Meet
    Mr Ajay
    Mrs. Hina
    Ms. Priya
    Mr. Tolstoy
    Mrs. Pooja
    '''
    text2 = '''
    https://www.google.com/curiocityforus.blogspot.co
    http://ww8.watchmovies.com/Breaking-Bad/
    https://mail.google.com/
    '''
    #pattern2 = re.compile(r'M(r|s|rs)(\.)?\s\w*')
    #mo2 = pattern2.finditer(text1)

    pattern2_1 = re.compile(r'https?://[a-z0-9]+\.[a-zA-Z0-9]+\.\w+/\S+?')
    mobject = pattern2_1.finditer(text2)
    for match1 in mobject:
        print(match1)

def Dates_sorter():
    data = '''
    Today at 23/11/2028 we Indian are going to mars via OG Spacecraft and it will take 7 
    earth months to reach there so We will be standing on mars at 20-06-2029. By the time
    2040/01/01 30% of the earth's population will have visited the planet mars.
    '''
    pattern3 = re.compile(r'\d+.\d+.\d+')
    extract = pattern3.findall(data)
    for match in extract:
        print(match)

    data1 = ('''
    Today at {} we Indian are going to mars via OG Spacecraft and it will take 7 
    earth months to reach there so We will be standing on mars at {}. By the time
    {} 30% of the earth's population will have visited the planet mars.
    '''.format(d1, d2, d3))
    print(data1)

def numbers():
    data = '''45,666,767 is a us standard. 4,56,66,767 is indian standard. us standard 
    is for millions and billions like 560 billions and 767 million is 560,767,000,000 
    which is hugh number which are mailny use dto describe company's market capital.
    '''
    pattern = re.compile(r'^\d{1,3}(,{3})*$')
    extract = pattern.findall(data)
    print(extract)

numbers()
