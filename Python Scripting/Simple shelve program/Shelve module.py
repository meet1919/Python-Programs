import shelve

shelveFile = shelve.open('mydata')
cats = ['Robin', 'Alex', 'Biladi']
dogs = ['Doggo', 'Kutta', 'Bob']
shelveFile['cats'] = cats
shelveFile['dogs'] = dogs


animal_1 = shelveFile['cats']
animal_2 = shelveFile['dogs']
print(animal_1)
print(animal_2)

list = shelveFile.get('cats')
print(list)
shelveFile.close()