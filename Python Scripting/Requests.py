import requests
res = requests.get('https://xkcd.com')
print(res.text)