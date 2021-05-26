import bs4, requests

res = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.78938000000005&lon=-122.39495#.YH20y-gzbIU')

exampleSoup = bs4.BeautifulSoup(res.text, features="html.parser")
elems = exampleSoup.select('p.myforecast-current-sm')     # p.myforecast-current-sm
                                                          # Here 'p' is tag and 'myforecast-current-sm' is attribute value
temperature = elems[0].getText()
print(temperature)



