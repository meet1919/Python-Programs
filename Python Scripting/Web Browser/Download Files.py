import requests

res = requests.get('https://www.scrapmaker.com/data/wordlists/names/surnames.txt')
res.raise_for_status()
playFile = open('Surname.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)