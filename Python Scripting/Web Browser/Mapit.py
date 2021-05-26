import webbrowser

place = input('Enter place you want to visit: ')
place_keys = place.split(' ')
print(place_keys)
address = ('+').join(place_keys)
print(address)
#webbrowser.open('https://www.google.com/maps/place/' + address)