import requests, bs4, webbrowser, os

res = requests.get('https://www.scrapmaker.com/data/wordlists/names/surnames.txt')
surnames = res.content
file = open('surname.txt', 'wb')
file.write(surnames)