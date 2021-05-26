import requests, bs4, webbrowser

keyword = str(input('Enter you search keyword: '))
print('Googling........')

search_page = 'https://www.google.com/search?q=' + keyword
res = requests.get(search_page)

google_soup = bs4.BeautifulSoup(res.text, features='html.parser')
#print(google_soup.prettify())
websites = google_soup.select('.kCrYT a')
#print(websites[0].get('href'))

#for links in websites[:10]:
    #webbrowser.open('http://google.com' + links.get('href'))




