import requests, bs4, os

# Making Directory
#os.mkdir(os.getcwd() + '\\Comic')
os.chdir(os.getcwd() + '\\Comic')
search_page = 'https://xkcd.com'
boss = input('Enter your name: ')
print('Hey there %s. I am you Downloading Bot. As you have started me, just sit back and relax.\nWhile downloading you can play Brawl Stars\nand here we go.......' %(boss))

for i in range(2453):
    # Requesting Comic Page
    res = requests.get(search_page)

    # Getting html of the web page
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #print(soup.prettify())

    # Finding Specific Pattern which leads to our required object
    comic = soup.find('div', id='comic')
    img_src = comic.img
    image_link = img_src.get('src')
    download_link = 'https:' + image_link

    # Downloading Image File
    res1 = requests.get(download_link)
    imageFile = open(image_link[23:], 'wb')
    imageFile.write(res1.content)
    imageFile.close()

    previous = soup.select('.comicNav a')
    link = previous[1].get('href')
    search_page = 'https://xkcd.com' + link

print('Boss I have completed your task. Thank you for the work :-)')


